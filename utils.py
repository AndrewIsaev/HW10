import json

CANDIDATES_DATA = "candidates.json"


def load_candidates(filename: str):
    """`, которая загрузит данные из файла"""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def get_all():
    """`, которая покажет всех кандидатов"""
    pass


def get_by_pk(pk):
    """`, которая вернет кандидата по pk"""
    pass


def get_by_skill(skill_name):
    """`, которая вернет кандидатов по навыку"""
    pass
print(load_candidates(CANDIDATES_DATA))