from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite://", echo=True)
Session = sessionmaker(engine)

class Base(DeclarativeBase):
    ...

from .product import Product



Base.metadata.create_all(engine)