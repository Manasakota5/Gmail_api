#download data from gmail and upload to postgres

Task 1: 

•	I was able to understand the task and would like to mention that I had previously worked on a similar task in the previous company. Back then, I was already given credentials of the Gmail and then asked to fetch the data. But now in this task, I must start from scratch.

•	I plan to make code automatic i.e., sending automatic Gmail and downloading into the respective folder. Keeping this in mind, I did some research on sending mail. I found the “smtplib” library which is popularly used to send mail and receive messages from the mail. 

•	But when I used “smtplib” I encountered an issue. Initially, I sent a mail with an attachment and the subject name “Your report is ready” to the mail account. Later I sent the second mail with the same subject name and verified whether I can get separate emails or not. I observed that I am not able to receive mail as a separate, but it was added to the queue of the first email I sent.
  “export_daily_reports_using_smtp” the file which sends the mail using smtp
  
•	But according to the task, I should send the attachments as a separate mail. Then I decided to try with mail API. I went to the official website of mail API and proceeded with the steps mentioned on the website and downloaded the credentials required to send the mail.

•	Initially, I tried an example method by attaching a photo, to confirm whether I can send mail separately. The code worked perfectly and then attached the report related to the task. The below screenshot shows the emails which are sent separately.
 
•	After successfully sending separate emails, my next task involves downloading the emails and my code should be able to download the reports ignoring other emails, that will be received. In the Gmail API documentation, there is a section related to “GMAIL SEARCH” which I explored and attempted to use some different search techniques, which I incorporated as queries in my code part, which exactly explains that data related to query, will be downloaded ignoring all other mails.

•	Search API consists of methods like “has attachment”, “subject”, “has: youtube” etc all these labels can be used to search and download the data required. For this purpose, I have used “Subject” as my query and provided the label 

•	I have provided the subject name as “Your report is ready”, so my code searches the mail inbox with the subject “Your report is ready” and downloads all the attachments related to it.

•	I have downloaded the data and saved the files in a folder and the data is in the directory “downloaded_data_from_gmail”.

•	Later I concatenated the data into a data frame and changed the column names to send the data to Postgres.  

Above image represents downloading data from the mail and saving into local folder. Initially I removed all the files available in the folder and replaces it with the new data which is going to be downloaded. This scenario will be helpful in the real time situations.
Postgres:

In PostgreSQL, I have set up my local server and created tables using Python scripts. 

I have predefined every table schema using Python. Loading data into a database can be done in two ways.

First Method:

•	Loading data into a data frame and then connecting to Postgres to send the data. I have opted for both techniques, each for task one i.e., once after downloading the data into the data frame and connecting to Postgres using “psycopg2”.

•	I have changed the columns using a dictionary and provided them while saving them into the table.

•	The table is created using Python script. I prefer predefining schema helps a lot to shape your data with some meaning.

 Second Method: 
•	The second is using Python and predefined scripts. I have written the scripts for table creation, querying, and deleting and constantly importing these scripts into the main file and making use of them according to my questions. This will be explained in detail with task2.

Continuing to the first task, once I have loaded the entire data to the table “edt_historical_report_entrfacebook” and derived tables like the below screenshot.  

•	From the table “edt_historical_report_entrfacebook” I have derived table sponsor_details, video_viral_details, video_status. From these 3 tables, we can derive more insights.

•	From the table sponsor_details, we can derive pages having more sponsors and to which category they belong and how many pages have more sponsors.

•	video_viral_details table: If a video goes viral and if we want to know the details like the video_length, does the video has any sponsors and how many views, likes and total_interactions, and how many shares got for the post, and the owner of the post and which country does it belong, etc. Such details can be derived from the table.

•	Video_status table: This table is derived to know about the video_length. Based on the video_length we can know, how people are interested like whether they are interested in short or long-length videos.

•	Some of the query results are attached, to be results for example. Tableau can be used to have a visualization view properly.

•	The above details of video_length having more likes and interactions.video_length_details.csv consists of data related to video_length having more interactions and likes.

 The above CSV files represent the data of sponsors.
Task 2:
•	I have used pandas and converted the dwh_dl_facebook_post_insights.csv file into a data frame to better understand the data.

•	I have derived the column names and got to know all the available columns are available in the JSON format of post_video_view_time_by_age_bucket_and_gender”.


•	After properly examining the data, I imported the CSV file into Postgres using Python script (this data frame can be exported directly using Postgres but I wanted to show the other approach which I am aware of). I wrote SQL scripts integrated with Python to extract the JSON column and then created tables such as “dwh_dl_facebook_post_insights” and “post_gender”.

Write a script for the sums per post for each gender. Additionally, create the sum for ages 18-34 of all genders.

To calculate sums for each gender per post, I have considered the post_id which is unique. Though other columns are available related to dwh_dl_facebook_post_insights.csv, I feel it represents a unique value. So I have added post_id along with the JSON columns of post_video_view_time_by_age_bucket_and_gender.I have written the SQL script which is mentioned in “queries.py” and the result is 
 
Post_id indicated 3 different posts, the age column represents the data of all genders between the age group 18-34, and the rest female, male, and unknown columns represent the sums per post of the genders.

Further ideas:
•	The data while downloading can be incorrect date and time format. Initially, we provide the file path name and extract part related to the date, and then replace the new file with the same format of the current day of the next day files we receive, which makes it automatic.

•	Maintaining everything as separate folders help to save the data, in real situations time we get data corrupted, and because of that, the data that existed will be corrupted. So, keeping this in mind, I have written scripts separately for sending mail, downloading emails, and loading them into Postgres. Everything is saved in different locations which helps us in debugging the data like in the earlier situation.

•	Spark or pyspark will be more beneficial while dealing with such data, first data is fetched, and then using pyspark SQL required columns will be selected from the fetched data and then exported into Postgres or batch systems.

•	Exporting to Postgres can be easier using sqoop.

Note:
I have not added the files related to the credentials of Gmail mail that are required to send or download the mail. And have also not added some files like token, and labels that involves my credentials.
 
I have given detailed explaination in [DW JUNIOR DATA ENGINEER.pdf](https://github.com/Manasakota5/Gmail_api/files/9699229/DW.JUNIOR.DATA.ENGINEER.pdf)
along with images.

References:
https://support.google.com/mail/answer/7190?hl=en&ref_topic=3394593
https://developers.google.com/gmail/api/quickstart/python
