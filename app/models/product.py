from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base


class Product(Base):
    id:Mapped[int] = mapped_column(primary_key=True, )
    name: Mapped[str] 
    description: Mapped[str]
    price: Mapped[float] = mapped_column(default=0.0)

    
    def __repr__(self) -> str:
        return f"Product(name={self.name!r})" #f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"