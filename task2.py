def generate_call_summary_url(call_id):
    base_url = "https://cfvapi-aks.cfvapi.skype.com/v2/api/events/"
    params = "?eventName=skypecosi_concore_native_callsignalingagent_conversation&extendedLoad=false"
    return f"{base_url}{call_id}{params}"

# Example usage
call_id = '{{callId}}'
url = generate_call_summary_url(call_id)
print(url) 