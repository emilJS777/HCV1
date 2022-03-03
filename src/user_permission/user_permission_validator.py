# USER PERMISSION SCHEMA
user_permission_schema = {
    "type": "object",
    "properties": {
        "user_id": {"type": "number"},
        "permission_id": {"type": "number"},
      },
    "required": ["user_id", "permission_id"]
}