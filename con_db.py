import sys; sys.path.append('./mariadb_con')
from mariadb_con import connect_lib
from mariadb_con import insert_data

connection = connect_lib()
cursor = connection.cursor()

data = [
    [3, 'title1', 'link1'],
    [4, '2', '2']
]
insert_data(cursor, connection, data)
#
cursor.execute("select * from sample")
result = cursor.fetchall()
print( result )

#
cursor.close()
connection.close()