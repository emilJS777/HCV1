from .config import app, db, logger
from ._general.utils import context_initializer

from .auth import auth_routes
from .client import client_routes
from .client_user import client_user_routes
from .email import email_routes
from .firm import firm_routes
from .permission import permission_routes
from .user import user_routes
from .user_permission import user_permission_routes
from .category import category_routes
from .category_firm import category_firm_routes
from .firm_user import firm_user_routes
from .position import position_routes
from .user_position import user_position_routes
from .permission_category import permission_category_routes
