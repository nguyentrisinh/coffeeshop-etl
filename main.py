import database


#Main driver of the ETL pipeline.
#Each method is responsible for data extraction from csv files,
  #transformation to related format and loading to MySQL database

if __name__ == '__main__':
    # database.insert_product("datasources/product.csv")
    # database.insert_customer("datasources/customer.csv")
    # database.insert_staff("datasources/staff.csv")
    database.insert_sales_outlet("datasources/sales_outlet.csv")
    # database.insert_pastry_inventory("datasources/pastry_inventory.csv")
    # database.insert_sales_receipts("datasources/sales_reciepts.csv")
