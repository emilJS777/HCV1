from .config import app, db, logger, api
from .__general.utils import context_initializer

from .Auth import AuthRoutes
from .Client import ClientRoutes
from .ClientUser import ClientUserRoutes
from .Email import EmailRoutes
from .Firm import FirmRoutes

from .Permission import PermissionRoutes
from .User import UserRoutes

from .Information import InformationRoutes
from .InformationFirm import InformationFirmRoutes

from .Position import PositionRoutes
from .UserPosition import UserPositionRoutes
from .PermissionCategory import PermissionCategoryRoutes

from .Storage import StorageRoutes
from .Product import ProductRoutes
from .ProductSale import ProductSaleRoutes
from .Expense import ExpenseRoutes

from .UserPermission import UserPermissionRoutes
from .Income import IncomeRoutes


