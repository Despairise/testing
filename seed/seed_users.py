import psycopg2

try:
    connection = psycopg2.connect(
        host='127.0.0.1',
        user='postgres',
        password='12131415ee',
        dbname='ab_db'
    )

    cursor = connection.cursor()

    insert_query = """INSERT INTO users (id, full_name, gender, b_day, address) VALUES 
            ('1','Ivanov Ivan Ivanovich', 'male', '1976.14.02', 'Moscow'),
            ('2','Melnikova Kseniia Vitalevna', 'female', '1998.12.07', 'Krasnoyarsk'),
            ('3','Pimenov Maksim Evgenevich', 'male', '1986.20.06', 'Novosibirsk'),
            ('4','SHpak Angelina Eduardovna', 'female', '1970.21.05', 'Moscow'),
            ('5','Bogoslovskii Artem Mikhailovich', 'male', '2000.15.09', 'Samara');"""

    cursor.execute(insert_query)
    connection.commit()


finally:
    if connection:
        connection.close()
