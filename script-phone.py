import psycopg2

try:
    connection = psycopg2.connect(
        host='127.0.0.1',
        user='postgres',
        password='12131415ee',
        dbname='ab_db'
    )

    cursor = connection.cursor()

    insert_query = """INSERT INTO phones (id, type, number_phone) VALUES 
            ('1','city', '342-434-275'),
            ('2','mobile', '7-823-234-22-44'),
            ('3','mobile', '7-323-678-43-81'),
            ('4','mobile','7-967-434-21-78'),
            ('5','city', '222-432-221');"""

    cursor.execute(insert_query)
    connection.commit()


finally:
    if connection:
        connection.close()
