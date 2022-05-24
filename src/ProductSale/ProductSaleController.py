from .ProductSaleService import ProductSaleService
from src.__general.Parents import Controller
from src.Auth import AuthMiddleware
from src.Permission import PermissionMiddleware
from src.Client import ClientMiddleware


class ProductSaleController(Controller):

    def __init__(self):
        super().__init__()
        self.product_sale_service: ProductSaleService = ProductSaleService()

    # POST
    @AuthMiddleware.check_authorize
    @ClientMiddleware.check_client(required=True)
    def post(self) -> dict:
        req: dict = self.request.get_json()
        return self.product_sale_service.create(
            product_id=req['product_id'],
            count=req['count'],
            wholesale=req['wholesale'],
            income_type_id=req['income_type_id']
        )

    # GET
    @AuthMiddleware.check_authorize
    @ClientMiddleware.check_client(required=True)
    def get(self):
        if self.arguments.get('id'):
            return self.product_sale_service.get_by_id(self.arguments.get('id'))
        else:
            return self.product_sale_service.get_all(
                page=self.page,
                per_page=self.per_page
            )

    # DELETE
    @AuthMiddleware.check_authorize
    @ClientMiddleware.check_client(required=True)
    def delete(self):
        return self.product_sale_service.delete(self.arguments.get('id'))
