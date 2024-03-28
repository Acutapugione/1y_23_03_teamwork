from flask import render_template
from sqlalchemy import select
from .. models import Product, Session
from .. import app



@app.get("/products")
def product_list():
    context = {}
    with Session() as session:
        context['products'] = session.scalars(select(Product)).all()
        return render_template("product/list.html", **context)


@app.get("/products/<int:id>")
def product(id):
    context = {}
    with Session() as session:
        context['product'] = session.scalars(select(Product).where(Product.id==id)).first()
    return render_template("product/index.html", **context)
