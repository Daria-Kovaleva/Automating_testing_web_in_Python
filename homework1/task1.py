import yaml
import requests

with open("/Users/veles/PycharmProjects/web_python/homework_1/config.yaml", "r") as file:
    data = yaml.safe_load(file)


def test_1(login, find_id):
    result = requests.get(data["address"], headers={"X-Auth-Token": login})
    list_id = [i["id"] for i in result.json()["data"]]
    assert find_id in list_id, "test_1 failed"


def test_2(login, title, description, content, find_description):
    result_1 = requests.post(data["address"], params={"title": title, "description": description, "content": content},
                             headers={"X-Auth-Token": login})
    result_2 = requests.get(data["address"], params={"description": find_description}, headers={"X-Auth-Token": login})
    assert result_1 and result_2, "test_2 failed"