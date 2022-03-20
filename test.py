from datetime import datetime

import requests
from sqlalchemy import func

BASE = "http://127.0.0.1:5000/"

# response = requests.post(BASE + "/123", {'first_name': 'Marko', 'last_name': 'Bruinic', 'club': 'Bayern'})
# print(response.json())
#
# response = requests.post(BASE + "/121", {'first_name': 'Markoo', 'last_name': 'Bruinic', 'club': 'Bayern'})
# print(response.json())
#
# response = requests.get(BASE + "/123")
# print(response.json())

# response = requests.put(BASE + "/123", {'club':'BVB', 'nationality':'Bosnian'})
# print(response.json())
#
# response = requests.get(BASE + "/123")
# print(response.json())
#
#
# response = requests.get(BASE + "/123")
# print(response.json())

# response = requests.get(BASE + "/all")
# print(response.json())