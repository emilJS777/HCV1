# CLIENT SCHEMA
client_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 3, "maxLength": 30},
        "description": {"type": "string", "minLength": 3, "maxLength": 120},
        "max_count_firms": {"type": "number"},
      },
    "required": ["name", "description", "max_count_firms"]
}
