from sqlalchemy import types

sql_types = {'page_name': types.VARCHAR,
        'user_name':types.VARCHAR,
        'facebook_id':types.BigInteger,
        'page_category':types.VARCHAR,
        'page_admin_top_country':types.VARCHAR,
        'page_description':types.VARCHAR,
        'page_created':types.DateTime(),
        'likes_at_posting':types.NUMERIC,
        'followers_at_posting':types.NUMERIC,
        'post_created':types.DateTime(),
       'post_created_date':types.DateTime(),
        'post_created_time':types.Time,
        'type':types.VARCHAR,
        'total_interactions':types.NUMERIC,
       'likes':types.NUMERIC,
        'comments':types.NUMERIC,
        'shares':types.NUMERIC,
        'love':types.NUMERIC,
        'wow':types.NUMERIC,
        'haha':types.NUMERIC,
        'sad':types.NUMERIC,
        'angry':types.NUMERIC,
       'care':types.NUMERIC,
        'video_share_status':types.VARCHAR,
        'is_video_owner':types.VARCHAR,
        'post_views':types.NUMERIC,
       'total_views':types.NUMERIC,
        'total_views_for_all_crossposts':types.NUMERIC,
        'video_length':types.Time,
        'url':types.VARCHAR,
       'message':types.VARCHAR,
        'link':types.VARCHAR,
        'final_link':types.VARCHAR,
        'image_text':types.VARCHAR,
        'link_text':types.VARCHAR,
       'description':types.VARCHAR,
        'sponsor_id':types.NUMERIC,
        'sponsor_name':types.VARCHAR,
         'sponsor_category':types.VARCHAR,
        'overperforming_score':types.FLOAT}
