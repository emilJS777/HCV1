# ROLE SCHEMA
role_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 3, "maxLength": 30}
      },
    "required": ["name"]
}