from unicodedata import decimal

from src.__general.Parents import Service
from src.Product import ProductServiceDb
from .ProductSaleRepository import ProductSaleRepository
from .ProductSaleRepository import ProductSale


class ProductSaleService(Service):

    # CREATE
    def create(self, product_id: int, count: float, wholesale: bool, income_type_id: int) -> dict:

        product: ProductServiceDb.Product = ProductServiceDb.get_by_id(product_id)

        if not product or count > product.count:
            return self.response(False, {'msg': 'product and/or product count not found'}, 200)

        # IF ALL READY UPDATE PRODUCT COUNT AND SAVE PRODUCT SALE
        ProductServiceDb.update_count(product_id=product_id, count=float(float(product.count)-float(count)))

        product_sale_repository = ProductSaleRepository()

        product_sale_repository.create(
            product_id=product_id,
            count=count,
            wholesale=wholesale,
            unit_id=product.unit_id,
            total_price=float(float(product.wholesale_price) * float(count) if wholesale else float(product.retail_price) * float(count)),
            storage_id=product.storage_id,
            income_type_id=income_type_id
        )
        return self.response(True, {'msg': 'sale successfully created'}, 200)

    # DELETE
    def delete(self, product_sale_id: int):
        product_sale: ProductSaleRepository = ProductSaleRepository()

        if not product_sale.get_by_id(product_sale_id):
            return self.response(False, {'msg': 'product sale not found'}, 200)

        product_sale.delete(product_sale_id)
        return self.response(True, {'msg': 'product sale successfully deleted'}, 200)

    # GET BY ID
    def get_by_id(self, product_sale_id: int):
        product_sale: dict = ProductSaleRepository().get_by_id(product_sale_id)

        if not product_sale:
            return self.response(False, {'msg': 'product sale not found'}, 200)

        return self.response(True, product_sale, 200)

    # GET ALL
    def get_all(self, page: int, per_page: int) -> dict:
        product_sales: dict = ProductSaleRepository().get_all(page=page, per_page=per_page)
        return self.response(True, product_sales, 200)
