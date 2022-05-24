from src import api
from .ProductSaleController import ProductSaleController

api.add_resource(ProductSaleController, "/api/product_sale")
