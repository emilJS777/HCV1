# EMAIL SCHEMA
email_schema = {
    "type": "object",
    "properties": {
        "address": { "type": "string", "minLength": 6,  'pattern': "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"}
      },
    "required": ["address"]
}
