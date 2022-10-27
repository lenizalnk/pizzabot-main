from database import BaseModel
from peewee import *


class PizzaTable(BaseModel):
    pizza_id = PrimaryKeyField(null=False)
    name = TextField()
    desc = TextField()
    price = IntegerField()

    @staticmethod
    def get_menu():
        return PizzaTable.select().execute()

    @staticmethod
    def get_menu_by_id(id):
        return PizzaTable.get(pizza_id=id)

    @staticmethod
    def get_pizza_by_id(id):
        return PizzaTable.select().where(PizzaTable.pizza_id == id).execute()
