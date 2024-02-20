from core.db.mixins import IdentifierMixin, TimestampMixin
from core.db.models import Base
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

PRODUCT_NAME_LENGTH = 45


class OrderedProduct(Base):
    __tablename__ = "ordered_products"

    order_id: Mapped[str] = mapped_column(ForeignKey("orders.id"), primary_key=True)
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"), primary_key=True)

    quantity: Mapped[int] = mapped_column(Integer)

    product: Mapped["Product"] = relationship(back_populates="orders_association")
    order: Mapped["Order"] = relationship(back_populates="ordered_products")


class Product(IdentifierMixin, TimestampMixin, Base):
    __tablename__ = "products"

    name: Mapped[str] = mapped_column(String(length=PRODUCT_NAME_LENGTH), unique=True)
    quantity: Mapped[int] = mapped_column(Integer)
    price: Mapped[int] = mapped_column(Integer)

    orders: Mapped[list["Order"]] = relationship(
        secondary="ordered_products", back_populates="products", viewonly=True
    )
    orders_association: Mapped[list["OrderedProduct"]] = relationship(
        back_populates="product"
    )


class Order(IdentifierMixin, TimestampMixin, Base):
    __tablename__ = "orders"

    products: Mapped[list["Product"]] = relationship(
        secondary="ordered_products", back_populates="orders", viewonly=True
    )
    ordered_products: Mapped[list["OrderedProduct"]] = relationship(
        back_populates="order"
    )
