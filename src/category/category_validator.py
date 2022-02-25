# CATEGORY SCHEMA
category_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 2, "maxLength": 30},
        "description": {"type": "string", "minLength": 2, "maxLength": 120},
      },
    "required": ["title", "description"]
}
