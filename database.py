import csv
import mysql.connector as sql
from mysql.connector import Error

# Establish a connection with database
# If connection fails, then throw an exception

try:
    db = sql.connect(host='coffeeshop-etl-datanase.cluster-cpphpy87raq7.ap-southeast-1.rds.amazonaws.com', user='admin',
                     password='sinh1996')
    if db.is_connected():
        print("Database connection is successful")

except Error as e:
    print("Connection Error", e)


# Each method realizes ETL operations by reading csv sources and inserting related data to database

def insert_sales_receipts(data):
    data_csv = csv.reader(open(data))
    cursor = db.cursor()
    print("Database insertion started...")
    header = next(data_csv)

    for row in data_csv:
        cursor.execute(
            "INSERT INTO coffee-shop-etl.Sales_Receipts (transaction_id,transaction_date,transaction_time,sales_outlet_id,staff_id,customer_id,instore_yn,order_num,line_item_id,product_id,quantity,line_item_amount,unit_price,promo_item_yn) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            row)

    db.commit()
    cursor.close()
    print("Sales Receipts insertion completed...")


def insert_customer(data):
    data_csv = csv.reader(open(data))
    cursor = db.cursor()
    print("Database insertion started...")
    header = next(data_csv)

    for row in data_csv:
        cursor.execute(
            "INSERT INTO coffee-shop-etl.Customer (customer_id,home_store,customer_first_name,customer_email,customer_since,loyalty_card_number,birthdate,gender,birth_year) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            row)

    db.commit()
    cursor.close()
    print("Customer insertion completed...")


def insert_product(data):
    data_csv = csv.reader(open(data))
    cursor = db.cursor()
    print("Database insertion started...")
    header = next(data_csv)

    for row in data_csv:
        cursor.execute(
            "INSERT INTO coffeeShopEtl.Product (product_id,product_group,product_category,product_type,product,product_description,unit_of_measure,current_wholesale_price,current_retail_price,tax_exempt_yn,promo_yn,new_product_yn) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            row)

    db.commit()
    cursor.close()
    print("Product insertion completed...")


def insert_pastry_inventory(data):
    data_csv = csv.reader(open(data))
    cursor = db.cursor()
    print("Database insertion started...")
    header = next(data_csv)

    for row in data_csv:
        cursor.execute(
            "INSERT INTO coffee-shop-etl.Pastry_Inventory (sales_outlet_id,transaction_date,product_id,start_of_day,quantity_sold,waste,waste_percent) VALUES(%s,%s,%s,%s,%s,%s,%s)",
            row)

    db.commit()
    cursor.close()
    print("Pastry Inventory insertion completed...")


def insert_sales_outlet(data):
    data_csv = csv.reader(open(data))
    cursor = db.cursor()
    print("Database insertion started...")
    header = next(data_csv)

    for row in data_csv:

        #If there are empty manager row, fill it with -1
        if (row[10] == ''):
            row[10] = -1

        cursor.execute(
            "INSERT INTO coffee-shop-etl.Sales_Outlet (sales_outlet_id,sales_outlet_type,sales_square_feet,store_address,store_city,store_state_province,store_telephone,store_postal_code,store_longitude,store_latitude,manager,Neighorhood) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            row)

    db.commit()
    cursor.close()
    print("Sales Outlet insertion completed...")


def insert_staff(data):

    data_csv = csv.reader(open(data))
    cursor = db.cursor()
    print("Database insertion started...")
    header = next(data_csv)

    for row in data_csv:

        #Take only non-empty columns
        transf_row = [None]*6
        for i in range(len(row)-2):
            transf_row[i] = row[i]

        cursor.execute(
            "INSERT INTO \"coffee-shop-etl\".Staff (staff_id,first_name,last_name,positions,start_date,location) VALUES(%s,%s,%s,%s,%s,%s)",
            transf_row)

    db.commit()
    cursor.close()
    print("Staff insertion completed...")
