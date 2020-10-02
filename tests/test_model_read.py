from typing import Optional

def test_model_instantiation(monkeypatch, connection):
    monkeypatch.setattr('ormlette.connection', connection)
    from ormlette.model import Model

    class User(Model):
        __table__ = 'users'
        id: Optional[int] = None
        name: str
        age: int

    user = User.objects.get(id=1)

    assert user.dict() == {'id': 1, 'name': 'Luka', 'age': 24}