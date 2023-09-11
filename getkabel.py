from sqlalchemy import URL, create_engine
import pypyodbc as odbc
import pandas as pd
from openpyxl import Workbook

def create_db_connection():
    connection_string = f"""Driver={{ODBC Driver 17 for SQL Server}};
    Server=10.182.1.54;
    Database=Artklas6_PRD;
    Trusted_Connection=yes;"""


    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
    engine = create_engine(connection_url,module=odbc)
    return engine


def getkabelfiles(filename):
    lines = []
    with open(f'{filename}.txt', 'r') as f_in:
        for line in f_in:
            modified_line = line.strip()[:-1]
            lines.append(modified_line)
    return lines



def loopfiles():
    etimklasse = getkabelfiles()
    return etimklasse

def savetoexcel(artikels):
    wb = Workbook()
    ws = wb.active
    for index, value in enumerate(artikels, start = 1):
        ws.cell(row=index, column=1, value = value)
    wb.save("test.xlsx")

def main():
    etim = getkabelfiles('EtimKlassedz')
    connection = create_db_connection()

    

    for i in range(len(etim)):
        sql = f"""Select 
[bestelnummer]	 = [AL].[Bestelnummer leverancier],
[Etim class] = [Al].[_Etimcode],
[rexelsearch] = [AL].[_Rexelsearch],
[orginele leveranciers] = [Al].[Art omschrijving leverancier],
[chunk] = [AL].[_chunk]
from ProductenPortal_Rexel_PRD.dbo.[Art_lev] AS AL 
where _chunk IS NOT NULL  AND _Etimcode ='{etim[i]}'"""
        df = pd.read_sql_query(sql,connection)
        df.to_excel(f"{etim[i]}.xlsx")
    


main()
