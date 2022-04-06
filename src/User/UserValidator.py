# USER SCHEMA
user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 6, "maxLength": 18},
        "password": {"type": "string", "minLength": 6, "maxLength": 32},
        "ticket": {"type": "string", "minLength": 30, "maxLength": 50},
      },
    "required": ["name", "password"]
}

# TICKET SCHEMA
user_ticket_schema = {
    "type": "object",
    "properties": {
        "full_name": {"type": "string", "minLength": 3, "maxLength": 40},
      },
    "required": ["full_name"]
}