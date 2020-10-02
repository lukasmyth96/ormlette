from typing import Optional

from ormlette.model import Model


class Test(Model):
    __table__ = 'test'
    id: Optional[int]
    num: int
    data: str


if __name__ == '__main__':

    # You can fetch rows from the 'test' table like so:
    fetched_instance = Test.objects.get(id='6')
    print(fetched_instance)

    # You can deserialize data into a Model and then save it to the database easily like this:
    data = {
        'num': 342532,
        'data': 'hey yooo'
    }
    created_instance = Test(**data)
    data = created_instance.save()
    print(data)
