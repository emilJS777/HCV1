from src import logger
from colorama import Fore
from src.User import UserServiceDb
from src.Permission import PermissionServiceDb
from src.Client import ClientServiceDb
from src.UserPermission import UserPermissionServiceDb
# from src.Auth import auth_service_db
# from src.Client import client_service_db
# from src.Email import email_service_db
# from src.ClientUser import client_user_service_db
# from src.Firm import firm_service_db
# from src.firm_user import firm_user_service_db


class Initializer:
    permissions = [{'name': 'client_get', 'title': 'get clients', 'firm': False}, {'name': 'client_edit', 'title': 'redactor Client', 'firm': False},
                   {'name': 'user_get', 'title': 'get User', 'firm': False}, {'name': 'user_edit', 'title': 'redactor User', 'firm': False},
                   {'name': 'firm_get', 'title': 'get Firm', 'firm': False}, {'name': 'firm_edit', 'title': 'redactor Firm', 'firm': False},
                   {'name': 'expense_get', 'title': 'get expense', 'firm': True}, {'name': 'expense_edit', 'title': 'edit expense', 'firm': True},
                   {'name': 'income_get', 'title': 'get incomes', 'firm': True}, {'name': 'income_edit', 'title': 'edit income', 'firm': True}]

    def __init__(self):
        client = self.client_initializer()
        user_ticket = self.first_ticket_initializer(client_id=client.id)

        for permission in self.permissions:
            if not PermissionServiceDb.get_by_name(permission['name'], client_id=client.id):
                init_permission = self.permission_initializer(permission=permission, client_id=client.id)

                UserPermissionServiceDb.create(
                    user_id=user_ticket.id,
                    permission_id=init_permission.id,
                    client_id=client.id,
                    firm_id=None
                )

    @staticmethod
    def client_initializer():
        client = ClientServiceDb.get_first_client()
        if not client:
            logger.info(f"first Client successfully created")
            return ClientServiceDb.create(
                name="Admin",
                description="Admin",
                max_count_firms=99,
                parent_id=None,
                creator_id=None
            )
        return client

    # PERMISSIONS INITIALIZER
    @staticmethod
    def permission_initializer(permission, client_id):
        permission_from_db = PermissionServiceDb.get_by_name(permission_name=permission['name'], client_id=client_id)

        if not permission_from_db:
            return PermissionServiceDb.create(permission_name=permission['name'],
                                              permission_title=permission['title'],
                                              client_id=client_id,
                                              firm=permission['firm'])
        return permission_from_db

    # FIRST TICKET INITIALIZER
    @staticmethod
    def first_ticket_initializer(client_id: int):
        ticket = UserServiceDb.get_first_by_creator_id(creator_id=None)
        if not ticket:
            new_ticket = UserServiceDb.create_ticket(creator_id=None, client_id=client_id, full_name="Admin")
            logger.info(f"first ticket {Fore.RED + new_ticket.ticket + Fore.RESET}")
            return new_ticket

        else:
            return ticket


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
#             Permission = self.init_permission(permission_name=permission_name)
#             self.init_role_permission(role_id=role.id, permission_id=Permission.id)
#
#         # CHECK OR CREATE FIRST ADMIN
#         User = self.init_first_admin()
#
#         # CHECK OR CREATE BIND USER ROLE
#         self.init_user_role(user_id=User.id, role_id=role.id)
#
#     @staticmethod
#     def init_first_admin():
#         # CHECK OR CREATE FIRST ADMIN
#         User = user_service_db.create_ticket(creator_id=None)
#         logger.info(f"first ticket {Fore.BLUE + User.ticket + Fore.RESET} created")
#         return User
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
#         Permission = permission_service_db.get_by_name(permission_name=permission_name) or \
#                      permission_service_db.create(permission_name=permission_name)
#         logger.info(f"Permission {Permission.name} created")
#         return Permission
#
#     @staticmethod
#     def init_role_permission(role_id, permission_id):
#         # CHECK OR CREATE ROLE PERMISSION BIND
#         role_permission = role_permission_service_db.get_by_role_id_permission_id(role_id=role_id, permission_id=permission_id) or \
#                           role_permission_service_db.create_bind(role_id=role_id, permission_id=permission_id)
#         return role_permission
