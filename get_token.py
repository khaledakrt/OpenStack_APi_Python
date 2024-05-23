import requests
import json

payload = {
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": "here_your_username",
                    "domain": {
                        "name": "Default"
                    },
                    "password": "here_your_password"}
            }
        },
        "scope": {
            "project": {
                "domain": {
                    "id": "default"
                },
                "name": "here_your_project_name"
            }
        }
    }
}

res = requests.post('http://here your_Identity_ip/v3/auth/tokens',
                    headers = {'content-type':'application/json'},
                    data=json.dumps(payload))

print(res.headers)