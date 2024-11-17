import requests

BASE_URL = "http://127.0.0.1:5000"
ACCESS_TOKEN = None

def login(username, password):
    global ACCESS_TOKEN
    response = requests.post(f"{BASE_URL}/login", json={"username": username, "password": password})
    if response.status_code == 200:
        ACCESS_TOKEN = response.json().get("access_token")
    return response.json()

def get_headers():
    if ACCESS_TOKEN:
        return {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    return {}

def get_users():
    response = requests.get(f"{BASE_URL}/users", headers=get_headers())
    return response.json()

def create_user(name, email):
    data = {"name": name, "email": email}
    response = requests.post(f"{BASE_URL}/users", json=data, headers=get_headers())
    return response.json()

def update_user(user_id, name, email):
    data = {"name": name, "email": email}
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=data, headers=get_headers())
    return response.json()

def delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/users/{user_id}", headers=get_headers())
    return response.status_code

if __name__ == '__main__':
    print("Login:", login("admin", "password"))
    print("Créer un utilisateur :", create_user("Alice", "alice@example.com"))
    print("Tous les utilisateurs :", get_users())
    print("Mettre à jour un utilisateur :", update_user(1, "Alice Updated", "alice.new@example.com"))
    print("Supprimer un utilisateur :", delete_user(1))
