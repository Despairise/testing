import psycopg2

try:
    connection = psycopg2.connect(
        host='127.0.0.1',
        user='postgres',
        password='12131415ee',
        dbname='ab_db'
    )

    cursor = connection.cursor()

    insert_query = """INSERT INTO mails (id, type, mail_address) VALUES 
            ('1','personal', 'euprececoilla-9977@yopmail.com'),
            ('2','work', 'prakigrabroitau-2682@yopmail.com'),
            ('3','work', 'troicrawoimexo-2067@yopmail.com'),
            ('4','personal','hugriyallemmau-2771@yopmail.com'),
            ('5','work', 'xefafouddeutra-5559@yopmail.com');"""

    cursor.execute(insert_query)
    connection.commit()


finally:
    if connection:
        connection.close()
