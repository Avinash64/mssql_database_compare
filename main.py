import pyodbc

# CONNECT TO SERVER

SERVER = 'localhost, 1433'
DATABASE = 'testDB1'
USERNAME = 'SA'
PASSWORD = 'Thisisastrongpassword1!'

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes;'
conn = pyodbc.connect(connectionString)

#create cursor
cursor = conn.cursor()



table_names = [x[2] for x in cursor.tables(tableType='TABLE')]
for i in table_names:
    if 'trace' not in i:
        print(i)
        cursor.execute(f'SELECT * FROM {i}')
        columns = [column for column in cursor.description]
        print(columns)
# print(table_names)  # ['customer', 'invoice', ...]

with open('names.txt', encoding='utf-8') as f:
    places = [place.strip() for place in f.readlines()]
print(places)
for i in places:
    cursor.execute(f"INSERT INTO city VALUES ('{i}');")


cursor.execute(f'SELECT * FROM city')
print(cursor.fetchall())
cursor.close()
conn.close()