import psycopg2

conn_details = psycopg2.connect(
   host="localhost",
   database="postgres",
   user="postgres",
   password="Zahrafl96",
   port='5432'
)

cursor = conn_details.cursor()


print("id")
id = input()
print("enter birth")
an = input()
print("enter crm")
crm = str(input())
print("enter date")
date = input()


Table_creation = f'''
   INSERT INTO zahra (id, birth_date, crm, date_joined)
   VALUES ('{id}', '{an}', '{crm}', '{date}');

'''
cursor.execute(Table_creation)

conn_details.commit()
cursor.close()
conn_details.close()