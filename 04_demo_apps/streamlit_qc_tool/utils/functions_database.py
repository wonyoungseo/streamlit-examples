import pandas as pd
import pymssql


def query_from_db(dbname, sql_query, username, password):
    # query to MSSQL DB
    server = "whosgooddb.japanwest.cloudapp.azure.com"
    conn = pymssql.connect(server, username, password, dbname)
    query_output = pd.read_sql(sql_query, conn)
    conn.close()
    return query_output


def insert_to_db(dataframe, dbname, tbname, username, password):
    server = "whosgooddb.japanwest.cloudapp.azure.com"
    conn = pymssql.connect(server, username, password, dbname)
    data = [tuple(x) for x in dataframe.values]
    for i in data:
        cur = conn.cursor()
        # If including NULL value in dataframe
        if 'nan' in str(i):
            i = str(i).replace('nan', 'NULL')
        SQL = 'INSERT INTO [' + dbname + '].[dbo].[' + tbname + '] VALUES ' + str(i) + ';'
        cur.execute(SQL)
        conn.commit()
    conn.close()


def execute_query(query, dbname, username, password):
    server = "whosgooddb.japanwest.cloudapp.azure.com"
    conn = pymssql.connect(server, username, password, dbname)
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    conn.close()