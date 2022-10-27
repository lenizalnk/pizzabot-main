from peewee import Model, SqliteDatabase

database = SqliteDatabase('sqlite.db')


class BaseModel(Model):
    class Meta:
        database = database


from database.Users import UsersTable
from database.Pizza import PizzaTable
from database.Orders import OrdersTable
from database.Files import FileTable

UsersTable.create_table()
PizzaTable.create_table()
OrdersTable.create_table()
FileTable.create_table()

FileTable.check_files()

