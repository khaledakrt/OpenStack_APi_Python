# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:13:28 2024

@author: Khaled-pro
"""

import requests
import json


res = requests.get('http://192.168.XXXX.XXXX:XXXX/v2/images',
                    headers={'content-type': 'application/json',
                             'X-Auth-Token': 'here_your_token'
                             },
                   )

print(res.text)