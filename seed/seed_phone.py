import os
import psycopg2


DATABASE_URL = os.environ.get('DATABASE_URL')
connection = psycopg2.connect(DATABASE_URL)

cursor = connection.cursor()

insert_query = """INSERT INTO phones (phone_type, number_phone, owner_id) VALUES 
        ('city', '3342434275', 1),
        ('mobile', '9232342244', 2),
        ('mobile', '9236784381', 3),
        ('mobile','9674342178', 4),
        ('city', '3222432221', 5);"""

cursor.execute(insert_query)
connection.commit()
connection.close()
