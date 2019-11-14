from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Product(Base):
   __tablename__ = 'products'
   Id = Column(Integer, primary_key=True)
   name = Column(String)
   price = Column(Float)
   picture_link = Column(String)
   description = Column(String)

class Cart(Base):
	__tablename__ = 'cart'
	Id = Column(Integer, primary_key=True)
	productID = Column(Integer)

addProduct('Toby Sweatpants',99.99,'https://www.tobykpatterns.com/wp-content/uploads/2017/03/Joggers-Adult-Info-Page-5.jpg','These are the hottest sweatpants out there!')