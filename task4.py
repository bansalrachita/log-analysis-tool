import json

def serialize_to_json(obj):
    """
    Serialize an object to a JSON string.

    Parameters:
    obj (any): The object to be serialized.

    Returns:
    str: The serialized JSON string of the object.
    """
    return json.dumps(obj)

# json_serialized = serialize_to_json("{{Output3}}")
# print(json_serialized)

def parse_logs(logs, participant_id):
    """
    Parse the logs to extract conversationSetupDiagnosticsData, eventTimestampBag, and rgParticipantId
    for the specified participantId.

    Parameters:
    logs (str): The JSON log string.
    participant_id (str): The participant ID to filter by.

    Returns:
    dict: A dictionary containing the extracted metadata, or None if not found.
    """
    try:
        log_data = json.loads(logs)
    except (ValueError, TypeError):
        return "No Logs available"
    
    # Iterate through the records to find the participant
    for record in log_data.get("records", []):
        rg_participant_id = record['extension'].get("rgParticipantId")
        if rg_participant_id == participant_id:
            return {
                "conversationSetupDiagnosticsData": record['extension'].get("conversationSetupDiagnosticsData"),
                "eventTimestampBag": record['extension'].get("eventTimestampBag"),
                "rgParticipantId": rg_participant_id
            }
    
    return None

participant_id = "{{participantId}}"
metadata = parse_logs("{{Output3}}", participant_id)
print(json.dumps(metadata, indent=4))    