import requests

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

response = requests.get(url)
data = response.json()

if data['success'] and 'data' in data:
    user_data = data['data']
    user_name = user_data['login']['username']
    country = user_data['location']['country']
    print(f'User Name is: {user_name}\n Country: {country}')
else:
    raise Exception ('failed to fetch user data!')