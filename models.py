import os
from peewee import *

db_name = os.environ.get('db_name', 'coffeeShopEtl')
db_host = os.environ.get('db_host', 'coffeeshop-etl-datanase.cluster-cpphpy87raq7.ap-southeast-1.rds.amazonaws.com')
db_username = os.environ.get('db_username', 'admin')
db_password = os.environ.get('db_password', 'sinh1996')

database = MySQLDatabase(db_name, **{'host': db_host, 'port': 3306, 'user': db_username, 'password': db_password})


class BaseModel(Model):
    class Meta:
        database = database


class Product(BaseModel):
    product_id = IntegerField(primary_key=True, unique=True, null=False)
    product_group = CharField(null=True, max_length=45)
    product_category = CharField(null=True, max_length=45)
    product_type = CharField(null=True, max_length=45)
    product = CharField(null=True, max_length=45) # product name
    product_description = CharField(null=True, max_length=200)
    unit_of_measure = CharField(null=True, max_length=45)
    current_wholesale_price = DecimalField(null=True, max_digits=10, decimal_places=2)
    current_retail_price = DecimalField(null=True, max_digits=10, decimal_places=2)
    tax_exempt_yn = CharField(null=True, max_length=5)
    promo_yn = CharField(null=True, max_length=5)
    new_product_yn = CharField(null=True, max_length=5)

    class Meta:
        db_table = 'Product'

    
class Customer(BaseModel):
    customer_id = IntegerField(primary_key=True, unique=True, null=False)
    home_store = IntegerField(null=True)
    customer_first_name = CharField(null=True, max_length=45)
    customer_email = CharField(null=True, max_length=45)
    customer_since = DateField(null=True)
    loyalty_card_number = CharField(null=True, max_length=45)
    birthdate = DateField(null=True)
    gender = CharField(null=True, max_length=5)
    birth_year = DateField(null=True)
    
    class Meta:
        db_table = 'Customer'


if __name__ == '__main__':
    database.connect()
    # database.create_tables([Product])
    database.create_tables([Customer])
