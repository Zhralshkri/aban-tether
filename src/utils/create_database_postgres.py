import psycopg2


class Connector:
    def connect_database(self):
        conn_details = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="Zahrafl96",
            port='5432'
        )
        cursor = conn_details.cursor()

    Table_creation = '''
       CREATE TABLE table_name (
           id SERIAL PRIMARY KEY,
           birth_date DATE NOT NULL,
           crm TEXT NOT NULL,
           date_joined DATE NOT NULL
       )
    '''
    cursor.execute(Table_creation)

    conn_details.commit()
    cursor.close()
    conn_details.close()
