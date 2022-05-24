# EXPENSE SCHEMA
expense_schema = {
    "type": "object",
    "properties": {
        "expense_type": { "type": "string", "minLength": 2},
        "description": {"type": "string", "minLength": 5, "maxLength": 120},
        "price": {"type": "number"},
        "firm_id": {"type": "number"}
    },
    "required": ["expense_type", "price", "firm_id"]
}
