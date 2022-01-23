from sqlalchemy import String, Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app.models.base import BaseModelFields


class Product(BaseModelFields):
    __tablename__ = 'product'

    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'))
    manufacturer = relationship('Manufacturer')
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category')
    model_id = Column(Integer, ForeignKey('model.id'))
    model = relationship('Model')
    part_category_id = Column(Integer, ForeignKey('part_category.id'))
    part_category = relationship('PartCategory')
    part_number = Column(String)

    __table_args__ = (UniqueConstraint('manufacturer_id', 'category_id',
                      'model_id' , 'part_category_id', 'part_number', name='product_unique_combinations'), )
