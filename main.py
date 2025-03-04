import pyodbc
from tablegen import gen_html, table
# CONNECT TO SERVER

SERVER = 'localhost, 1433'
DATABASE = 'testDB1'
USERNAME = 'SA'
PASSWORD = 'Thisisastrongpassword1!'

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes;'
conn = pyodbc.connect(connectionString)

cursor = conn.cursor()
table_names = [x[2] for x in cursor.tables(tableType='TABLE') if 'trace' not in x[2]]

# print(table_names)
data = []
for i in table_names:
    cursor.execute(f'SELECT * from {i}')
    records = cursor.fetchall()
    data.append(table(records))
    # print(records)
cursor.close()
conn.close()

print(gen_html('index.html','\n\n'.join(data)))
# print('\n\n'.join(data))