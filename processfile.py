from connect_to_databasealldata import connect_to_database_alldata
from connect_to_databasebasicdata import connect_to_databasebasicdata
from savedatainexcel import save_in_excel
import asyncio

def processfile(file):
#    records = connect_to_database_alldata(file)
    records = connect_to_databasebasicdata(file)
    

    


"""
cursor = conn.cursor()
    cursor.execute("select * from dbo.Art_klas")
    for x in cursor.fetchall():
        return x

   for x in cursor:
      print(x)
"""