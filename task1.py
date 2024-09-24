import re
import json

# Input log messages
logs = '{{logs}}'

# Regex patterns
timestamp_pattern = r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z)'
log_level_pattern = r'(Inf|Warn|Err)'
cid_pattern = r'CID\[([0-9a-fA-F-]+)\]'
module_pattern = r'[\s\\t]+([^:\s]+):'  # Matches module until the first colon
call_id_pattern = r'callId=(\S+)'

# Store metadata results
metadata = []

# Process each line of logs
for line in logs.splitlines():
    if not line.strip():
        continue
    
    timestamp = re.search(timestamp_pattern, line)
    log_level = re.search(log_level_pattern, line, re.IGNORECASE)
    cid = re.search(cid_pattern, line)
    module = re.search(module_pattern, line)
    call_id = re.search(call_id_pattern, line)
    
    # Find the first colon after the first space or tab
    first_colon_index = re.search(r'[\s\t]+[^:]*:', line)
    if first_colon_index:
        message_start = first_colon_index.end()  # Get the index after the colon
        message = line[message_start:].strip()  # Get everything after the first colon
    else:
        message = ''

    # Clean the message by removing leading/trailing spaces
    message = message.strip()

    if timestamp and log_level and module:
        log_entry = {
            "timestamp": timestamp.group(1),
            "logLevel": log_level.group(1),
            "module": module.group(1).strip(),
            "cid": cid.group(1) if cid else None,  # Extract just the alphanumeric part
            "message": message
        }
        # Add callId only if present
        if call_id:
            log_entry["callId"] = call_id.group(1)
        
        metadata.append(log_entry)

# Sort the metadata by timestamp
metadata.sort(key=lambda x: x["timestamp"])

# Print the metadata in JSON format
print(json.dumps(metadata, indent=2))