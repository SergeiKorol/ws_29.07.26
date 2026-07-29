import requests


def add_delete_task_test():
    body = {"title": "SomeTask", "completed": False}
    # создать задачу
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    # удалить созданную задачу
    requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')

    # проверить что гет по удалённой задаче == 404
    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 404
