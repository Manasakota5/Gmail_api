import psycopg2
from create_table_facebook import edt_historical_report_entrfacebook
from create_table_facebook import copy_sql_facebook
from redefine_datatypes import  sql_types

connection = psycopg2.connect(host='localhost',
                              dbname='postgres',
                              user='postgres',
                              password='gautham1235',
                              port='5432')

cursor = connection.cursor()

#delete if table exists
delete_table_query = ''' drop table if exists edt_historical_report_entrfacebook'''
cursor.execute(delete_table_query)

# table creation from the queires
create_table_query = edt_historical_report_entrfacebook
cursor.execute(create_table_query)

