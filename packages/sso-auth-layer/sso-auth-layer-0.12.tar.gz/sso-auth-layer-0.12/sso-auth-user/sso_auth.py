
import requests
from requests.adapters import HTTPAdapter, Retry

sso_x_api_key = "e77tz4T4nO3z4XphD7umT9LgIKXqM7db2cr5hDuY"
token_validation_url = "https://sso-stage.ventura1.com/auth/user/v3/valid_token"
# used to validate token from sso against client id
def validate_token(token, client_id ,session_id):
    headers = {
        "content-type": "application/json",
        "session_id": session_id,
        "x-api-key": sso_x_api_key,
        "Authorization": f'Bearer {token}'
    }
    request_body = {"client_id": client_id}
    s = requests.Session()
    retries = Retry(total=3,
                    backoff_factor=0.1,
                    status_forcelist=[429, 500, 502, 503, 504])

    s.mount('https://', HTTPAdapter(max_retries=retries))
    s.mount('http://', HTTPAdapter(max_retries=retries))
    
    response = s.request("POST", token_validation_url, headers=headers, json=request_body, timeout=5)
    if response.status_code == 200:
        resp = response.json()
        valid_token = resp.get("valid_token")
        if valid_token == "True":
            status = True
        else:
            status = False
    else:
        resp = response.json()
        status = False
    
    return resp, status