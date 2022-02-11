# EMPLOYEE SCHEMA
employee_schema = {
    "type": "object",
    "properties": {
        "first_name": {"type": "string", "minLength": 3, "maxLength": 20},
        "last_name": {"type": "string", "minLength": 3, "maxLength": 20},
        "date_birth": {"type": "string"},
        "passport_id": {"type": "string", "minLength": 5, "maxLength": 30}
      },
    "required": ["first_name", "last_name", "date_birth", "passport_id"]
}
