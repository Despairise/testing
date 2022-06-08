import os
import psycopg2
from datetime import date


DATABASE_URL = os.environ.get('DATABASE_URL')
connection = psycopg2.connect(DATABASE_URL)

cursor = connection.cursor()

insert_query = f"""INSERT INTO users (full_name, gender, b_day, address) VALUES 
        ('Ivanov Ivan Ivanovich', 'male', '{date(1976, 12, 14)}', 'Moscow'),
        ('Melnikova Kseniia Vitalevna', 'female', '{date(1986, 7, 12)}', 'Krasnoyarsk'),
        ('Pimenov Maksim Evgenevich', 'male', '{date(1994, 6, 20)}', 'Novosibirsk'),
        ('SHpak Angelina Eduardovna', 'female', '{date(1975, 5, 21)}', 'Moscow'),
        ('Bogoslovskii Artem Mikhailovich', 'male', '{date(1976, 9, 15)}', 'Samara');"""

cursor.execute(insert_query)
connection.commit()
connection.close()
