import new_validate

my_payload = [
    {
        "m_id": "101",
        "timestamp": "2026-10-09T08:00:00",
        "temperature": "25",
        "exposure": "12",
        "focus_error": "2"
    },
    {
        "m_id": "102",
        "timestamp": "2026-10-09T08:05:00",
        "temperature": "19",
        "exposure": "1",
        "focus_error": "15"
    }
]

print(my_payload[1])

# result = new_validate.run_type_validation(my_payload)
# result2 = new_validate.run_complete_validation(my_payload)
print(result)