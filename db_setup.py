import pyodbc

# CONNECT TO SERVER

SERVER = 'localhost, 1433'
DATABASE = 'master'
USERNAME = 'SA'
PASSWORD = 'Thisisastrongpassword1!'

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes;'
conn = pyodbc.connect(connectionString, autocommit=True)

#create cursor
cursor = conn.cursor()
with open('create_db.sql', encoding='utf-8') as f:
    create_db = f.read()
with open('cleanup.sql', encoding='utf-8') as f:
    cleanup = f.read()
with open('example_databases_setup.sql', encoding='utf-8') as f:
    db_setup = f.read()
cursor.execute(cleanup)
cursor.execute(create_db)
cursor.execute(db_setup)
cursor.close()
conn.close()

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE=testDB1;UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes;'
conn = pyodbc.connect(connectionString)
cursor = conn.cursor()

table_names = [x[2] for x in cursor.tables(tableType='TABLE')]
for i in table_names:
    if 'trace' not in i:
        print(i)
        cursor.execute(f'SELECT * FROM {i}')
        columns = [column for column in cursor.description]
        print(columns)
# print(table_names)  # ['customer', 'invoice', ...]

# with open('names.txt', encoding='utf-8') as f:
#     places = [place.strip() for place in f.readlines()]
# print(places)
# for i in places:
#     cursor.execute(f"INSERT INTO city VALUES ('{i}');")
with open('example_databases_populate.sql', encoding='utf-8') as f:     
    cursor.execute(f.read())
    cursor.execute('USE testDB1\n' + f.read())
    cursor.commit()
        



cursor.execute(f'SELECT * FROM city')
print(cursor.fetchall())
cursor.close()
conn.close()