import psycopg2


class Database:

    def __init__(self):
        self.connect_details = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="Zahrafl96",
            port='5432')

        self.cursor = self.connect_details.cursor()

    def migrate(self):
        self.create_movie_table()
        self.create_person_table()
        self.create_pivot_table()

    def create_movie_table(self):
        table_movies = '''
            CREATE TABLE movie (
            id SERIAL PRIMARY KEY,
            name_movie TEXT NOT NULL,
            date_create DATE NOT NULL,
            country TEXT NOT NULL
                       )
                       '''

        self.cursor.execute(table_movies)

    def create_person_table(self):
        table_people = '''
            CREATE TABLE people ( 
            id SERIAL PRIMARY KEY,
            first_name CHAR(20) NOT NULL,
            last_name TEXT NOT NULL,
            date_birth DATE NOT NULL,
            sex CHAR(1) NOT NULL,
            job TEXT NOT NULL 
            )
        '''

        self.cursor.execute(table_people)

    def create_pivot_table(self):
        table_pivot = '''
            CREATE TABLE pivot_people_movies (
            id SERIAL PRIMARY KEY,
            peaple_id INTEGER,
            movie_id INTEGER

             )
        '''
        self.cursor.execute(table_pivot)


database = Database()
database.migrate()

    #
    #
    #
    #
    #
    # connect_details.commit()
    # cursor.close()
    # connect_details.close()


