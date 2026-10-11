# ==========================================
# Python 49 - HTTP GET Request
# ==========================================

import requests

# ==========================================
# 1. Send GET Request
# ==========================================

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url, timeout=10)

# ==========================================
# 2. Check Response
# ==========================================

# print(f"Status Code: {response.status_code}")
# print(f"Response Type: {type(response)}")
# print(response.text)

# ==========================================
# 3. Parse JSON Response
# ==========================================

# user_data = response.json()

# print(f"Data Type: {type(user_data)}")
# print(f"User ID: {user_data['id']}")
# print(f"Name: {user_data['name']}")
# print(f"Email: {user_data['email']}")

# ==========================================
# 4. Extract Nested JSON Data
# ==========================================

user_data = response.json()

print(f"Username: {user_data['username']}")
print(f"City: {user_data['address']['city']}")
print(f"Company Name: {user_data['company']['name']}")
print(f"Latitude: {user_data['address']['geo']['lat']}")