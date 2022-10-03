# Import libraries
import glob
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import  types
from redefine_datatypes import  sql_types
import os

# Get CSV files list from a folder
path_to_save = r'C:/Users/manas/Documents/Task/Answers/api_download_data/daily_report'
path = r'C:/Users/manas/Documents/Task/Answers/Download_files_from_gmail/'

#delete all the files in the directory
file_path = glob.glob(path_to_save+"/*.csv")
for f in file_path:
    os.remove(f)

#get all the file in the directory
files = []
for file in glob.glob(path + "/*.csv"):
    files.append(file)

#read all the files from the directory
df_list = (pd.read_csv(file) for file in files)

# Concatenate all DataFrames
daily_export   = pd.concat(df_list, ignore_index=True)

dict = {'Page Name':'page_name',
        'User Name':'user_name',
        'Facebook Id':'facebook_id',
        'Page Category':'page_category',
       'Page Admin Top Country':'page_admin_top_country',
        'Page Description':'page_description',
        'Page Created':'page_created',
       'Likes at Posting':'likes_at_posting',
        'Followers at Posting':'followers_at_posting',
        'Post Created':'post_created',
       'Post Created Date':'post_created_date',
        'Post Created Time':'post_created_time',
        'Type':'type',
        'Total Interactions':'total_interactions',
       'Likes':'likes',
        'Comments':'comments',
        'Shares':'shares',
        'Love':'love',
        'Wow':'wow',
        'Haha':'haha',
        'Sad':'sad',
        'Angry':'angry',
       'Care':'care',
        'Video Share Status':'video_share_status',
        'Is Video Owner?':'is_video_owner',
        'Post Views':'post_views',
       'Total Views':'total_views',
        'Total Views For All Crossposts':'total_views_for_all_crossposts',
        'Video Length':'video_length',
        'URL':'url',
       'Message':'message',
        'Link':'link',
        'Final Link':'final_link',
        'Image Text':'image_text',
        'Link Text':'link_text',
       'Description':'description',
        'Sponsor Id':'sponsor_id',
        'Sponsor Name':'sponsor_name',
        'Sponsor Category':'sponsor_category',
        'Overperforming Score ':'overperforming_score'}

#rename the column names before saving into csv
daily_export.rename(columns=dict,inplace=True)

#save into csv file
daily_export.to_csv(path_to_save+'.csv',index=False)

#export into postgres
engine=create_engine("postgresql+psycopg2://postgres:passwordname@localhost:5432/postgres")

try:
    daily_export.to_sql('edt_historical_report_entrfacebook', engine, if_exists='replace', index=False)
except:
    print("connection failed")

finally:
    engine.dispose()
