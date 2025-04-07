users:list[dict] = [
    {'name': 'Emilia', 'location': 'Lublin', 'posts': 500, },
    {'name': 'Julia', 'location': 'Warszawa', 'posts': 1000, },
    {'name': 'Martyna', 'location': 'Ząbki', 'posts': 200, }
]

for user in users:
    print(f'Twój znajomy: {user["name"]} z {user["location"]} opublikował: {user["posts"]}')
