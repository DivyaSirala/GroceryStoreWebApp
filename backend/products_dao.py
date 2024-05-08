from sql_connection import get_sql_connection

"""Function to get all the products from the MySQL DB using MySQL query and MySQL connector"""
def get_all_products(connection):
    cursor = connection.cursor()
    query = ("SELECT products.product_id, products.product_name, products.uom_id , products.price_per_unit, uom.uom_name "
             "FROM products INNER JOIN uom ON products.uom_id = uom.uom_id")
    cursor.execute(query)

    #The results are within this cursor so we need to iterate through this cursor
    response=[]
    for (product_id, product_name, uom_id, price_per_unit, uom_name) in cursor:  # () tuple
        response.append(
            {
                'product_id': product_id,
                'product_name': product_name,
                'unit_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            }
        )
    return response


"""Function to insert a new product into the DB using MySQL query"""
def insert_new_product(connection, product):
    cursor = connection.cursor()
    #Parameterized query
    query = ("INSERT INTO products "
             "(product_name, uom_id, price_per_unit)" 
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    #commits the changes into the DB
    connection.commit()
    #returns the row_id of the last inserted value
    return cursor.lastrowid


"""Function to delete the row or given product by using its product_name"""
def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products "
             "WHERE product_id = " + str(product_id))
    cursor.execute(query)
    connection.commit()


if __name__ == "__main__":
    connection = get_sql_connection()
    #print(get_all_products(connection))
    """
    print(insert_new_product(connection, {
        'product_name': 'cabbage',
        'uom_id': '1',
        'price_per_unit': '10'
    }))
    """
    #print(delete_product(connection, 7))