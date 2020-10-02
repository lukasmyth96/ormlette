
from typing import Optional

from ormlette.model import Model


def test_model_instantiation(monkeypatch, connection):
    monkeypatch.setattr('ormlette.connection', connection)

    class User(Model):
        __table__ = 'user'
        id: Optional[int] = None
        name: str
        age: int

    data = {
        'name': 'luka',
        'age': 24,
    }

    user = User(**data)

    assert user.dict() == {**data, 'id': None}
