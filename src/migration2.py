import psycopg2

class MovieService :
    def insert(self,id,name_movie,date_create,country) :
        values = ({id},{name_movie},{date_create},{country})
#باید کوئراش رو اضافه کنیم یعنی جوری ک دیتابیس بفهمه تو میخوای اضافه کنی


    def update (self,id,name_movie,date_create,country) :
        values = ( {id},{name_movie},{date_create},{country})

    def drop (self,id,name_movie,date_create,country) :
        values = f'({id}, {name_movie}, {date_create}, {country})'

    def get_by_id (self,id):
        values = ({id})

    def get_all (self) :
        values = f"select * from movie"

class PeopleService :
    def insert (self,id,first_name,last_name,date_brith,sex,job):
        values = ({id},{first_name},{last_name},{date_brith},{sex},{job})

    def update (self,id,first_name,last_name,date_brith,sex,job):
        values = ({id},{first_name},{last_name},{date_brith},{sex},{job})

    def drop (self,id,first_name,last_name,date_brith,sex,job):
        values = ({id},{first_name},{last_name},{date_brith},{sex},{job})

    def get_by_id (self , id):
        values = ({id})

    def get_all (self):
        values = f"select * from people"





