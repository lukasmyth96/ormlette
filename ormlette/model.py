
from typing import Optional

from pydantic import BaseModel

from ormlette import connection
from ormlette.manager import Manager


def save(self: Optional[BaseModel] = None):
    col_name_to_value = self.dict(exclude_none=True)
    col_names = list(col_name_to_value)
    col_names_placeholder = ', '.join(col_names)
    col_values_placeholder = ', '.join([f'%({col})s' for col in col_names])
    command = f"""INSERT INTO {self.__table__} ({col_names_placeholder}) VALUES ({col_values_placeholder}) RETURNING *"""
    cursor = connection.cursor()
    cursor.execute(command, col_name_to_value)
    connection.commit()
    data = {col.name: val for col, val in zip(cursor.description, cursor.fetchone())}
    cursor.close()
    return data


class ModelMeta(type):
    def __new__(mcs, class_name, bases, attrs):
        # Add pydantic_model attribute.
        if class_name == 'Model':
            # returning type.__new__(...) instead of just type(...) allows the metaclass to be inherited.
            # See here https://stackoverflow.com/questions/37410692/inheritance-of-metaclass - haven't fully understood why one works and not the other yet.
            return type.__new__(mcs, class_name, bases, attrs)
        else:
            pydantic_model = type(f'Pydantic{class_name}', (BaseModel,), attrs)
            pydantic_model.__table__ = attrs['__table__']
            pydantic_model.objects = Manager(model=pydantic_model,
                                             table=attrs['__table__'])
            pydantic_model.save = save
            return pydantic_model


class Model(metaclass=ModelMeta):

    def __init__(self, **data):
        pass
