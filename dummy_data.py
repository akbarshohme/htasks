import requests
from collections import namedtuple

Person = namedtuple('Person', ['id', 'firstName', 'lastName', 'age', 'email'])

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def create_persons(users_data):
    if not users_data or 'users' not in users_data:
        print("Invalid user data")
        return []

    return [Person(id=user['id'], firstName=user['firstName'], lastName=user['lastName'], age=user['age'], email=user['email'])
            for user in users_data['users']]

def find_user_by_first_name(users, first_name):
    return next((user for user in users if user.firstName.lower() == first_name.lower()), None)

url = "https://dummyjson.com/users"
users_data = fetch_data(url)
users = create_persons(users_data)


