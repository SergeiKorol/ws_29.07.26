import requests


def add_edit_test():
    body = {"title": "SomeTask", "completed": False}
    # создать задачу
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    # Проставить отметку о выполнении
    body = {"title": "generated-1"}
    response = requests.patch(
        f'https://todo-app-sky.herokuapp.com/{id}',
        json=body
        )

    # проверить что completed == True
    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.json()["completed"] == 1
