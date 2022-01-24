from app.db.database import engine
from app import models


def create_tables():
    try:
        print("#"*30)
        print("Creating tables...")
        models.category.Category.metadata.create_all(bind=engine)
        models.manufacturer.Manufacturer.metadata.create_all(bind=engine)
        models.part_category.PartCategory.metadata.create_all(bind=engine)
        models.model.Model.metadata.create_all(bind=engine)
        models.source_site.SourceSite.metadata.create_all(bind=engine)
        models.product.Product.metadata.create_all(bind=engine)
        print("Created all the tables.")
        print("#"*30)
    except Exception as e:
        print("#"*30)
        print(e)
        print("#"*30)
