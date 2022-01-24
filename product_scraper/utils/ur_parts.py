from multiprocessing import Pool
from product_scraper.utils.base_scraper import BaseProductScraper
from product_scraper.utils.utils import append_path
import requests
from app.db.database import get_db, SessionLocal
from bs4 import BeautifulSoup
from app.crud.base import get_or_create
from app.models import manufacturer, category, model, part_category, product


class UrPartsScraper(BaseProductScraper):
    def __init__(self, website_url : str):
        self.website_url = website_url

    def get_manufacturer_list(self) -> list[str]:
        page = requests.get(self.website_url)
        manufacterer_page_soup = BeautifulSoup(page.content, "html.parser")
        manufacterer_list_items = manufacterer_page_soup.find(
            id="content").find("ul").find_all("li")
        manufacterer_list = [manufacterer_item.find(
            "a").text.strip() for manufacterer_item in manufacterer_list_items]
        return manufacterer_list

    def get_category_list(self, category_url: str) -> list[str]:
        page = requests.get(category_url)
        category_page_soup = BeautifulSoup(page.content, "html.parser")
        category_list_items = category_page_soup.find(
            id="content").find("ul").find_all("li")
        category_list = [category_item.find(
            "a").text.strip() for category_item in category_list_items]
        return category_list

    def get_model_list(self, model_url : str) -> list[str]:
        page = requests.get(model_url)
        model_page_soup = BeautifulSoup(page.content, "html.parser")
        model_list_items = model_page_soup.find(
            id="content").find("div", attrs={'class': "c_container allmodels"}).find("ul").find_all("li")
        model_list = [category_item.find(
            "a").text.strip() for category_item in model_list_items]
        return model_list

    def get_part_category_list(self, part_category_url: str) -> list[str]:
        page = requests.get(part_category_url)
        part_category_soup = BeautifulSoup(page.content, "html.parser")
        part_category_items = part_category_soup.find(
            id="content").find("div", attrs={'class': "c_container allparts"})
        if not part_category_items:
            return []
        part_category_items = part_category_items.find("ul").find_all("li")
        part_category_list = [category_item.find(
            "a").text.strip() for category_item in part_category_items]
        return part_category_list

    def process_manufacturer_products(self, manufacturer_name: str) -> None:
        db_session = SessionLocal()
        print(manufacturer_name)
        manufacturer_obj, _ = get_or_create(
            db_session, manufacturer.Manufacturer, name=manufacturer_name)
        category_url = append_path(self.website_url, manufacturer_name)
        category_list = self.get_category_list(category_url)
        for category_name in category_list:
            print(" " * 10, category_name)
            category_obj, _ = get_or_create(
                db_session, category.Category, name=category_name)
            model_url = append_path(category_url, category_name)
            model_list = self.get_model_list(model_url)
            for model_name in model_list:
                print(" " * 25, model_name)
                model_obj, _ = get_or_create(
                    db_session, model.Model, name=model_name)
                part_category_url = append_path(model_url, model_name)
                part_category_list = self.get_part_category_list(part_category_url)
                part_category_dict = dict()
                for part_category_name_number in part_category_list:
                    part_category_name = part_category_name_number.split(
                        '-')[-1].strip()
                    part_number = ''.join(
                        part_category_name_number.split('-')[:-1]).strip()
                    # print(
                    #     f"{' ' * 35 } part_category_name_number : {part_category_name_number}  part_number: {part_number}  part_category_name : {part_category_name}")
                    part_category_obj = part_category_dict.get(
                        part_category_name)
                    if not part_category_obj:
                        part_category_obj, _ = get_or_create(
                            db_session, part_category.PartCategory, name=part_category_name)
                        part_category_dict[part_category_name] = part_category_obj
                    product_obj, _ = get_or_create(
                        db_session,
                        product.Product,
                        manufacturer_id=manufacturer_obj.id,
                        category_id=category_obj.id,
                        model_id=model_obj.id,
                        part_category_id=part_category_obj.id,
                        part_number=part_number
                    )

    def scraper_site(self) -> None:
        # starts scraping the given site.
        print(f"Scraping : {self.website_url}")
        manufacterer_list = self.get_manufacturer_list()
        with Pool(10) as p:
            p.map(self.process_manufacturer_products, manufacterer_list)
