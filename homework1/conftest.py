import pytest
import requests
import yaml

with open("/Users/veles/PycharmProjects/web_python/homework_1/config.yaml", "r") as file:
    data = yaml.safe_load(file)


@pytest.fixture()
def login():
    res_1 = requests.post(data["address_1"], data={"username": data["username"], "password": data["password"]})
    return res_1.json()["token"]


@pytest.fixture()
def find_id():
    return 114977


@pytest.fixture()
def title():
    return "Привет мир"


@pytest.fixture()
def description():
    return "Hello world! Hello world! Hello world!"


@pytest.fixture()
def content():
    return "Hello, world!» — программа, результатом работы которой является вывод на экран или иное устройство фразы."


@pytest.fixture()
def find_description():
    return "Hello world!"