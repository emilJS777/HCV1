# PRODUCT SCHEMA

product_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 2, "maxLength": 50},
        "code": {"type": "string", "minLength": 1, "maxLength": 50},
        "wholesale_price": {"type": "number"},
        "retail_price": {"type": "number"},
        "unit_id": {"type": "number"},
        "storage_id": {"type": "number"},
        "count": {"type": "number"},
      },
    "required": ["title",
                 "code",
                 "unit_id",
                 "wholesale_price",
                 "retail_price",
                 "storage_id",
                 "count"]
}
