from src import logger
from colorama import Fore, Back, Style
from src.services_db import user_service_db, role_service_db, permission_service_db, \
    role_permission_service_db, user_role_service_db


class Initializer:
    user = {"name": "super_admin", "password": "super_admin123", "first_name": "super", "last_name": "admin"}
    role = {"name": "super_admin"}
    permissions = ["create_client", "get_client_by_id", "get_clients", "update_client", "delete_client",
                   "get_user_ids_by_client_id", "bind_client_user", "unbind_client_user",
                   "create_firm", "get_firm_by_id", "get_firms", "update_firm", "delete_firm",
                   "get_user_ids_by_firm_id", "bind_firm_user", "unbind_firm_user",
                   # "create_permission", "update_permission", "delete_permission",
                   "create_role", "get_role_by_id", "get_roles", "update_role", "delete_role",
                   "get_permission_ids_by_role_id", "bind_role_permission", "unbind_role_permission",
                   "create_user", "get_user_by_id", "get_users", "update_user", "delete_user",
                   "get_role_ids_by_user_id", "bind_user_role", "unbind_user_role",
                   "create_employee", "update_employee", "delete_employee", "get_employee_by_id", "get_employees"]

    def __init__(self):
        # CHECK OR CREATE FIRST ROLE
        role = self.init_first_role(role_name=self.role["name"])

        # CHECK OR CREATE PERMISSIONS AND CHECK OR BIND ROLE PERMISSION
        for permission_name in self.permissions:
            permission = self.init_permission(permission_name=permission_name)
            self.init_role_permission(role_id=role.id, permission_id=permission.id)

        # CHECK OR CREATE FIRST ADMIN
        user = self.init_first_admin(user_name=self.user["name"], user_password=self.user["password"],
                                     first_name=self.user["first_name"], last_name=self.user["last_name"])

        # CHECK OR CREATE BIND USER ROLE
        self.init_user_role(user_id=user.id, role_id=role.id)

    @staticmethod
    def init_first_admin(user_name, user_password, first_name, last_name):
        # CHECK OR CREATE FIRST ADMIN
        user = user_service_db.get_by_name(name=user_name) or \
               user_service_db.create(name=user_name, password=user_password,
                                      first_name=first_name, last_name=last_name, creator_id=0)
        logger.info(f"first user {Fore.BLUE + user.name + Fore.RESET} and him password "
                    f"{Fore.BLUE + user_password + Fore.RESET} created")
        return user

    @staticmethod
    def init_first_role(role_name):
        # CHECK OR CREATE FIRST ROLE
        role = role_service_db.get_by_name_creator_id(name=role_name, creator_id=0) or \
               role_service_db.create(name=role_name, creator_id=0)
        logger.info(f"first role {role.name} created")
        return role

    @staticmethod
    def init_user_role(user_id, role_id):
        # CHECK OR CREATE USER ROLE BIND
        user_role = user_role_service_db.get_by_user_id_role_id(user_id=user_id, role_id=role_id) or \
                    user_role_service_db.create_bind(user_id=user_id, role_id=role_id)
        return user_role

    @staticmethod
    def init_permission(permission_name):
        # CHECK OR CREATE PERMISSION
        permission = permission_service_db.get_by_name(permission_name=permission_name) or \
                     permission_service_db.create(permission_name=permission_name)
        logger.info(f"permission {permission.name} created")
        return permission

    @staticmethod
    def init_role_permission(role_id, permission_id):
        # CHECK OR CREATE ROLE PERMISSION BIND
        role_permission = role_permission_service_db.get_by_role_id_permission_id(role_id=role_id, permission_id=permission_id) or \
                          role_permission_service_db.create_bind(role_id=role_id, permission_id=permission_id)
        return role_permission
