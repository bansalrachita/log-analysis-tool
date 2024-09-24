import json

def json_to_readable_string(json_data):
    try:
        # Convert JSON to a readable string format
        readable_string = json.dumps(json_data, indent=4)
        return readable_string
    except (TypeError, ValueError) as e:
        return f"Error converting to JSON: {e}"

# Example JSON data
json_example = "{{Output6}}"

# Convert to readable string
readable_json = json_to_readable_string(json_example)
print(readable_json)