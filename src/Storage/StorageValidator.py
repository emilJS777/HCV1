# STORAGE SCHEMA
storage_schema: dict = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 2, "maxLength": 50},
        "code": {"type": "string", "minLength": 1, "maxLength": 50},
        "address": {"type": "string", "minLength": 1, "maxLength": 80},
        "storekeeper": {"type": "string", "minLength": 1, "maxLength": 80},
        "firm_id": {"type": "number"},
    },
    "required": ["title", "code", "address", "storekeeper", "firm_id"]
}
