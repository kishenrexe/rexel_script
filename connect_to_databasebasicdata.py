import pyodbc
import pypyodbc as odbc
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import pandas as pd


#def query(file):
#    engine = connect_to_database()
#    sql= sql_statement(file)
#    records = pd.read_sql_query(sql,engine)
#    return records

def connect_to_databasebasicdata(file):
    connection_string = f"""Driver={{ODBC Driver 17 for SQL Server}};
    Server=10.182.1.54;
    Database=Artklas6_PRD;
    Trusted_Connection=yes;"""


    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
    engine = create_engine(connection_url,module=odbc)
    
    sql_statement = f"""Select 
[bestelnummer]	 = [AL].[Bestelnummer leverancier],
[Etim class] = [Al].[_Etimcode],
[Merk] = A.[fabrikaat],
[Serie] = A.[Serie/programma],
[rexelsearch] = [AL].[_Rexelsearch],
[orginele leveranciers] = [Al].[Art omschrijving leverancier],
[chunk] = [AL].[_chunk]
from ProductenPortal_Rexel_PRD.dbo.[Art_lev] AS AL 
INNER JOIN ProductenPortal_Rexel_PRD.dbo.[Artikel] AS A
ON [AL].[Relatiecode fabrikant] = [A].[Relatiecode fabrikant]
AND  [AL].[Artikelnummer fabrikant] = [A].[Artikelnummer fabrikant]
where _chunk IS NOT NULL  AND _Etimcode ='{file}'
"""
    
    df = pd.read_sql_query(sql_statement,engine)
    
    df.to_excel(f"""{file}.xlsx""")
    return df

    