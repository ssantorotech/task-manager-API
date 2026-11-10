import itertools

TODOS_DB: dict[int, dict] = {}
USERS_DB: dict[int, dict] = {}
TODOS_ID = itertools.count(1)
USERS_ID = itertools.count(1)