import os
import psycopg2


DATABASE_URL = os.environ.get('DATABASE_URL')
connection = psycopg2.connect(DATABASE_URL)

cursor = connection.cursor()

insert_query = """INSERT INTO mails (mail_type, mail_address, owner_id) VALUES 
        ('personal', 'euprececoilla-9977@yopmail.com', 1),
        ('work', 'prakigrabroitau-2682@yopmail.com', 2),
        ('work', 'troicrawoimexo-2067@yopmail.com', 3),
        ('personal','hugriyallemmau-2771@yopmail.com', 4),
        ('work', 'xefafouddeutra-5559@yopmail.com', 5);"""

cursor.execute(insert_query)
connection.commit()
connection.close()
