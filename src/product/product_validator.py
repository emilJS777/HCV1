# PRODUCT SCHEMA

product_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 2, "maxLength": 50},
        "code": {"type": "string", "minLength": 1, "maxLength": 50},
        "unit_measurement": {"type": "string", "minLength": 1, "maxLength": 30},
        "group": {"type": "string", "minLength": 1, "maxLength": 30},
        "atgaa_classifier": {"type": "string", "minLength": 1, "maxLength": 30},
        "account": {"type": "string", "minLength": 1, "maxLength": 30},
        "wholesale_price": {"type": "number"},
        "retail_price": {"type": "number"},
        "other_currency": {"type": "string", "minLength": 1, "maxLength": 30},
        "wholesale_price_other_currency": {"type": "string", "minLength": 1, "maxLength": 30},
        "hcb_coefficient": {"type": "string", "minLength": 1, "maxLength": 30},
        "accounting_method": {"type": "string", "minLength": 1, "maxLength": 30},
        "storage_id": {"type": "number"},
      },
    "required": ["title",
                 "code",
                 "unit_measurement",
                 "group",
                 "account",
                 "wholesale_price",
                 "retail_price",
                 "other_currency",
                 "wholesale_price_other_currency",
                 "hcb_coefficient",
                 "accounting_method",
                 "storage_id"]
}
