from . import ProductService, ProductValidator
from flask import request
from src.Auth import AuthMiddleware
from src.Client import ClientMiddleware
from flask_expects_json import expects_json
from src.Permission import PermissionMiddleware


# CREATE
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission('product_edit')
@expects_json(ProductValidator.product_schema)
def create_product() -> dict:
    req: dict = request.get_json()
    res: dict = ProductService.create(body=req)
    return res


# UPDATE
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission('product_edit')
@expects_json(ProductValidator.product_schema)
def update_product(product_id: int) -> dict:
    req: dict = request.get_json()
    res: dict = ProductService.update(
        product_id=product_id,
        body=req
    )
    return res


# DELETE
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission('product_edit')
def delete_product(product_id: int) -> dict:
    res: dict = ProductService.delete(product_id)
    return res


# GET BY ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission('product_get')
def get_by_id_product(product_id: int) -> dict:
    res: dict = ProductService.get_by_id(product_id)
    return res


# GET ALL
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission('product_get')
def get_all_product() -> dict:
    res: dict = ProductService.get_all(
        page=int(request.args.get('page')),
        per_page=int(request.args.get('per_page'))
    )
    return res


# GET ALL IDS BY STORAGE ID
@AuthMiddleware.check_authorize
@ClientMiddleware.check_client(required=True)
@PermissionMiddleware.check_permission('product_get')
def get_all_product_by_storage_id() -> dict:
    res: dict = ProductService.get_all_by_storage_id(
        storage_id=int(request.args.get('storage_id')),
        page=int(request.args.get('page')),
        per_page=int(request.args.get('per_page'))
    )
    return res
