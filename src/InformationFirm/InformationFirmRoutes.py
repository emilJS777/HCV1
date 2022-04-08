from src import app
from . import InformationFirmController


# BIND INFORMATION FIRM
app.add_url_rule("/api/information-firm",
                 view_func=InformationFirmController.bind_information_firm,
                 methods=["POST"])

# UNBIND INFORMATION FIRM
app.add_url_rule("/api/information-firm",
                 view_func=InformationFirmController.unbind_information_firm,
                 methods=["DELETE"])

# GET FIRM IDS BY INFORMATION ID
app.add_url_rule("/api/information-firm/<int:information_id>",
                 view_func=InformationFirmController.get_firm_ids_by_information_id,
                 methods=["GET"])
