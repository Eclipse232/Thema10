import pymssql

conn = pymssql.connect(host='nickketelaarsserver.database.windows.net', port=1433, database='Thema10', user='nickketelaars@nickketelaarsserver', password='nick0001')

cursor = conn.cursor()
cursor.execute('SELECT * FROM TEST')
row = cursor.fetchone()
while row:
    #doe iets met deze rows
    print(str(row[0]) + str(row[1]))
    row = cursor.fetchone()
    
conn.commit()
conn.close()