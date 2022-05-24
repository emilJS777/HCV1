from src.__general.Parents import Repository
from .ProductSaleModel import ProductSale
from flask import g
from typing import List


class ProductSaleRepository(Repository):

    # CREATE
    def create(self, product_id: int, count: float, wholesale: bool, unit_id: int,
               total_price: float, storage_id: int, income_type_id: int) -> ProductSale:
        product_sale: ProductSale = ProductSale(
            product_id=product_id,
            count=count,
            wholesale=wholesale,
            total_price=total_price,
            storage_id=storage_id,
            client_id=g.client_id,
            income_type_id=income_type_id
        )
        product_sale.unit_id = unit_id
        product_sale.save_db()
        return product_sale

    # DELETE
    def delete(self, product_sale_id: int) -> ProductSale:
        product_sale: ProductSale = ProductSale.query.filter_by(id=product_sale_id).first()
        product_sale.delete_db()
        return product_sale

    # GET BY ID
    def get_by_id(self, product_sale_id: int) -> dict:
        product_sale: dict = self.get_dict_items(ProductSale.query.filter_by(id=product_sale_id).first())
        return product_sale

#     GET ALL
    def get_all(self, page: int, per_page: int) -> dict:
        products_sale: dict = self.get_page_items(ProductSale.query
                                                  .filter_by(client_id=g.client_id)
                                                  .order_by(-ProductSale.id)
                                                  .paginate(page=page, per_page=per_page))
        return products_sale

