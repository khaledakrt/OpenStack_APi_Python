import requests

res= requests.get("http://192.168.XXX.XXX:XXXX/v2.0/networks",
                     headers={'content-type': 'application/json',
                             'X-Auth-Token': 'here_your_token'
                             },
                  )

print(res.text)