from ast import For
from sqlalchemy import String, Column, Integer, ForeignKey, UniqueConstraint

from app.models.base import BaseModelFields


class Product(BaseModelFields):
    __tablename__ = 'product'

    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'))
    category_id = Column(Integer, ForeignKey('category.id'))
    model_id = Column(Integer, ForeignKey('model.id'))
    part_category_id = Column(Integer, ForeignKey('part_category.id'))
    part_number = Column(String)

    __table_args__ = (UniqueConstraint('manufacturer_id', 'category_id',
                      'model_id' , 'part_category_id', 'part_number', name='product_unique_combinations'), )
