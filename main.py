import psycopg2
from queries import dwh_dl_facebook_post_insights
from queries import copy_sql
from queries import postgender

#establish a connection to the postgresql
connection = psycopg2.connect(host='localhost',
                              dbname='postgres',
                              user='postgres',
                              password='gautham1235',
                              port='5432')
cursor = connection.cursor()

#delete if table exists
delete_table_query = ''' drop table if exists dwh_dl_facebook_post_insights,
                          postgender'''
cursor.execute(delete_table_query)

# table creation from the queires
create_table_query = dwh_dl_facebook_post_insights

#create the post_gender table from dwh_dl_facebook_post_insights table
create_post_gender_query = postgender

cursor.execute(create_table_query)
cursor.execute(create_post_gender_query)

#path where the data has been downloaded
path = r'C:\Users\manas\Documents\Task\Junior DE Task\Junior DE Task\dwh_dl_facebook_post_insights.csv'

#copying the data from csv file into postgres database
with open(path, 'r') as f:
    cursor.copy_expert(sql=copy_sql, file=f)
    connection.commit()
    cursor.close()