# INFORMATION SCHEMA
information_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 2, "maxLength": 30},
        "description": {"type": "string", "minLength": 2, "maxLength": 120},
        "unit_id": {"type": "number"}
      },
    "required": ["title", "description", "unit_id"]
}
