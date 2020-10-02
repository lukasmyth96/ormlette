
import pytest


@pytest.fixture()
def connection(postgresql):
    cur = postgresql.cursor()
    cur.execute("CREATE TABLE users (id serial PRIMARY KEY, name varchar, age integer);")
    cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Luka", 24))
    postgresql.commit()
    cur.close()
    return postgresql


