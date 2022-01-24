from abc import ABC, abstractmethod


class BaseProductScraper(ABC):
    @abstractmethod
    def scraper_site(self):
        pass
