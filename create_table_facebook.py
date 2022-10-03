edt_historical_report_entrfacebook = ''' create table edt_historical_report_entrfacebook(
       page_name text, 
       user_name text,
       facebook_dd numeric, 
       page_category text,
       page_admin_top_country text, 
       page_description text, 
       page_created Date,
       likes_at_posting numeric, 
       followers_at_posting numeric, 
       post_created text,
       post_created_date Date, 
       post_created_time Date, 
       type text, 
       total_interactions numeric,
       likes numeric,
       comments numeric,
       shares numeric,
       love numeric,
       wow numeric,
       haha numeric,
       sad numeric,
       angry numeric,
       care numeric,
       video_share_status text,
       is_video_owner text,
       post_views numeric,
       total_views numeric,
       total_views_for_all_crossposts numeric, 
       video_length time, 
       url text,
       message text, 
       link text, 
       final_link text, 
       image_text text, 
       link_text text,
       description text , 
       sponsor_id numeric,
       sponsor_name text, 
       sponsor_category text,
       overperforming_score numeric );'''

#copy the csv data into the table we created with separation of delimiter
copy_sql_facebook = """
           COPY edt_historical_report_entrfacebook FROM stdin WITH CSV HEADER
           DELIMITER as ','
           """

sponsor_details = ''' create table sponsor_details as (SELECT page_name,facebook_id, ARRAY_AGG(distinct(sponsor_name)) AS sponsor_name,
                      ARRAY_AGG(distinct(sponsor_category)) AS sponsor_category,count(distinct(sponsor_category)) as count_sponsors_category,
                      count(distinct(sponsor_name)) as count_sponsors_name FROM video_status 
                     WHERE sponsor_name is not null GROUP BY page_name,facebook_id ORDER BY page_name);'''

video_length_details = ''' select sum(likes) as likes ,page_name ,min(video_length) as video_length,total_interactions,post_views from video_status where video_length <='00:00:50'  
                          group by page_name ,video_length,total_interactions,post_views order by likes desc'''