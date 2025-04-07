users:list[dict] = [
    {'name': 'Emilia', 'location': 'Lublin', 'posts': 500, },
    {'name': 'Julia', 'location': 'Warszawa', 'posts': 1000, },
    {'name': 'Martyna', 'location': 'Ząbki', 'posts': 200, }
]

def get_user_info(users_data: list [dict])-> None:
    for user in users_data:
        print(f'Twój znajomy: {user["name"]} z {user["location"]} opublikował: {user["posts"]}')

get_user_info(users)