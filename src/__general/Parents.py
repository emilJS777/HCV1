from flask_restful import Resource, request
from flask import make_response, jsonify
from src import db
from abc import ABC, abstractmethod


class Controller(Resource):
    def __init__(self):
        self.per_page = int(request.args.get('per_page') or 0)
        self.page = int(request.args.get('page') or 0)
        self.arguments = request.args
        self.request = request


class Service:
    def __init__(self):
        self.per_page = int(request.args.get('per_page') or 0)
        self.page = int(request.args.get('page') or 0)
        self.arguments = request.args
        self.request = request

    @staticmethod
    # RESPONSE ON SUCCESSFUL CONTROLLER EXECUTION
    def response(success, obj, status_code) -> make_response:
        return make_response(jsonify(success=success, obj=obj), status_code)


class Repository:

    @staticmethod
    def get_dict_items(obj):
        dict_item = {}

        if not obj:
            return obj

        for key, value in obj.__dict__.items():
            if not key == '_sa_instance_state' and not key == 'password_hash':
                dict_item[key] = value

        return dict_item

    @staticmethod
    def get_page_items(page):
        page_items: dict = {'total': page.total,
                            'page': page.page,
                            'pages': page.pages,
                            'per_page': page.per_page,
                            'items': []}

        for item in page.items:
            page_items['items'].append(Repository.get_dict_items(item))

        return page_items


class Model:
    id = db.Column(db.Integer, primary_key=True)

    # SAVE DB SELF
    def save_db(self):
        db.session.add(self)
        db.session.commit()

    # DELETE DB
    def delete_db(self):
        db.session.delete(self)
        db.session.commit()

    # UPDATE DATABASE
    @staticmethod
    def update_db():
        db.session.commit()


class IRepository(ABC):
    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, body: dict):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def get_by_id(self, model_id: int):
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int):
        pass
