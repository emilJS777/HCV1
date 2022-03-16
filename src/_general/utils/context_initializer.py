from src import logger
from colorama import Fore
from src.user import user_service_db
from src.permission import permission_service_db
from src.user_permission import user_permission_service_db
# from src.auth import auth_service_db
# from src.client import client_service_db
# from src.email import email_service_db
# from src.client_user import client_user_service_db
# from src.firm import firm_service_db
# from src.firm_user import firm_user_service_db


class Initializer:
    permissions = [{'name': 'client_get', 'title': 'get clients'}, {'name': 'client_edit', 'title': 'redactor client'},
                   {'name': 'user_get', 'title': 'get user'}, {'name': 'user_edit', 'title': 'redactor user'},
                   {'name': 'bind_user_client', 'title': 'link user to client'},
                   {'name': 'firm_get', 'title': 'get firm'}, {'name': 'firm_edit', 'title': 'redactor firm'},
                   {'name': 'bind_user_firm', 'title': 'link user to firm'},
                   {'name': 'position_edit', 'title': 'edit position'}]

    def __init__(self):
        user_ticket = self.first_ticket_initializer()
        for permission in self.permissions:
            init_permission = self.permission_initializer(permission=permission)
            self.ticket_permission_initializer(ticket=user_ticket, permission=init_permission)

    # PERMISSIONS INITIALIZER
    @staticmethod
    def permission_initializer(permission):
        permission_from_db = permission_service_db.get_by_name(permission_name=permission['name'])

        if not permission_from_db:
            return permission_service_db.create(permission_name=permission['name'],
                                                permission_title=permission['title'])

        if not permission_from_db.title == permission['title']:
            return permission_service_db.update(permission_id=permission_from_db.id,
                                                permission_name=permission_from_db.name,
                                                permission_title=permission['title'])
        return permission_from_db

    # FIRST TICKET INITIALIZER
    @staticmethod
    def first_ticket_initializer():
        ticket = user_service_db.get_first_by_creator_id(creator_id=None)
        if not ticket:
            new_ticket = user_service_db.create_ticket(creator_id=None)
            logger.info(f"first ticket {Fore.RED + new_ticket.ticket + Fore.RESET}")
            return new_ticket

        else:
            return ticket

    # TICKET AND PERMISSION INITIALIZER
    @staticmethod
    def ticket_permission_initializer(ticket, permission):
        if not user_permission_service_db.get_by_user_id_permission_id(user_id=ticket.id, permission_id=permission.id):
            user_permission_service_db.create_bind(user_id=ticket.id, permission_id=permission.id)
            logger.info(f"user or ticket by id {ticket.id} and permission by name {permission.name} bind!")


# v.0.1
# class Initializer:
#     role = {"name": "super_admin"}
#     permissions = ["create_client", "get_client_by_id", "get_clients", "update_client", "delete_client",
#                    "get_user_ids_by_client_id", "bind_client_user", "unbind_client_user",
#                    "create_firm", "get_firm_by_id", "get_firms", "update_firm", "delete_firm",
#                    "get_user_ids_by_firm_id", "bind_firm_user", "unbind_firm_user",
#                    # "create_permission", "update_permission", "delete_permission",
#                    "create_role", "get_role_by_id", "get_roles", "update_role", "delete_role",
#                    "get_permission_ids_by_role_id", "bind_role_permission", "unbind_role_permission",
#                    "create_user", "create_user_ticket", "get_user_by_id", "get_users", "update_user", "delete_user",
#                    "get_role_ids_by_user_id", "bind_user_role", "unbind_user_role",
#                    "create_employee", "update_employee", "delete_employee", "get_employee_by_id", "get_employees"]
#
#     def __init__(self):
#         # CHECK OR CREATE FIRST ROLE
#         role = self.init_first_role(role_name=self.role["name"])
#
#         # CHECK OR CREATE PERMISSIONS AND CHECK OR BIND ROLE PERMISSION
#         for permission_name in self.permissions:
#             permission = self.init_permission(permission_name=permission_name)
#             self.init_role_permission(role_id=role.id, permission_id=permission.id)
#
#         # CHECK OR CREATE FIRST ADMIN
#         user = self.init_first_admin()
#
#         # CHECK OR CREATE BIND USER ROLE
#         self.init_user_role(user_id=user.id, role_id=role.id)
#
#     @staticmethod
#     def init_first_admin():
#         # CHECK OR CREATE FIRST ADMIN
#         user = user_service_db.create_ticket(creator_id=None)
#         logger.info(f"first ticket {Fore.BLUE + user.ticket + Fore.RESET} created")
#         return user
#
#     @staticmethod
#     def init_first_role(role_name):
#         # CHECK OR CREATE FIRST ROLE
#         role = role_service_db.get_by_name(name=role_name) or \
#                role_service_db.create(name=role_name, creator_id=None)
#         logger.info(f"first role {role.name} created")
#         return role
#
#     @staticmethod
#     def init_user_role(user_id, role_id):
#         # CHECK OR CREATE USER ROLE BIND
#         user_role = user_role_service_db.get_by_user_id_role_id(user_id=user_id, role_id=role_id) or \
#                     user_role_service_db.create_bind(user_id=user_id, role_id=role_id)
#         return user_role
#
#     @staticmethod
#     def init_permission(permission_name):
#         # CHECK OR CREATE PERMISSION
#         permission = permission_service_db.get_by_name(permission_name=permission_name) or \
#                      permission_service_db.create(permission_name=permission_name)
#         logger.info(f"permission {permission.name} created")
#         return permission
#
#     @staticmethod
#     def init_role_permission(role_id, permission_id):
#         # CHECK OR CREATE ROLE PERMISSION BIND
#         role_permission = role_permission_service_db.get_by_role_id_permission_id(role_id=role_id, permission_id=permission_id) or \
#                           role_permission_service_db.create_bind(role_id=role_id, permission_id=permission_id)
#         return role_permission
