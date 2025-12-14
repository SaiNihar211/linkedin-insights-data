# linkedin-insights-server

📊 LinkedIn Insights Server (End-to-End Backend Project)

This project is a complete backend system that:
Page Name
Page url
id (the LinkedIn platform specific id)
Page Profile Picture
Description
Website
Page Industry
Total Followers
Head Count
Specialities
Any other fields you find useful or a good-to-have





Accepts a LinkedIn profile name or profile URL

Fetches LinkedIn post insights using Apify

Stores the data permanently in MySQL

Runs a FastAPI server (ready for cloud deployment)

This project is built slowly and correctly, following real industry practices.

🔥 Why This Project Exists

LinkedIn does not provide free public APIs for insights.
So we use:

Apify → to fetch LinkedIn post data

MySQL → to store data permanently

FastAPI → to expose a backend server

This simulates how real companies build data pipelines.

🧠 High-Level Architecture (VERY IMPORTANT)
User Input (Profile Name / URL)
            ↓
        Python Backend
            ↓
        Apify Scraper
            ↓
     LinkedIn Post Data
            ↓
        MySQL Database
            ↓
   Queries / API / Analytics

📁 Project Folder Structure
linkedin_project/
│
├── src/
│   ├── main.py               # FastAPI server
│   ├── apify_to_mysql.py     # Scraper + Database logic
│   ├── requirements.txt     # Python dependencies
│
└── README.md

⚙️ Technologies Used (WHY EACH ONE)
Technology	Why We Use It
Python	Simple, powerful backend language
Apify	Scrapes LinkedIn without cookies
MySQL	Reliable relational database
FastAPI	Fast backend server framework
GitHub	Version control & deployment
Render	Free cloud deployment
🔐 Environment Variables (SECURITY)

⚠️ Never put API keys in code

We use environment variables.

Set Apify Token (Local Machine)
export APIFY_TOKEN="apify_api_your_real_token"


Why?

GitHub blocks secrets

Industry best practice

Safer deployment

📦 Python Dependencies
requirements.txt
fastapi
uvicorn
apify-client
mysql-connector-python


Install all dependencies:

pip3 install -r requirements.txt

🗄️ MySQL — FULL EXPLANATION (IMPORTANT SECTION)
❓ What is MySQL?

MySQL is a relational database used to:

Store structured data (tables, rows, columns)

Persist data even after system restarts

Run queries to analyze data

In this project:

MySQL permanently stores LinkedIn post insights

🔧 Step 1: Start MySQL

Open Terminal:

mysql -u root -p


Enter your MySQL password.

You should see:

mysql>

🏗️ Step 2: Create Database
CREATE DATABASE linkedin_insights;


Select it:

USE linkedin_insights;

📊 Step 3: Create posts Table (VERY IMPORTANT)
CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    post_id VARCHAR(255),
    author_name VARCHAR(255),
    post_text TEXT,
    post_date VARCHAR(50),
    likes INT,
    comments INT,
    reposts INT,
    post_url TEXT,
    profile_source VARCHAR(255)
);

🔍 What Each Column Means
Column	Purpose
id	Auto-generated unique row ID
post_id	LinkedIn post unique ID
author_name	Author shown by LinkedIn
post_text	Full post content
post_date	When post was published
likes	Number of likes
comments	Number of comments
reposts	Number of reposts
post_url	Direct LinkedIn post link
profile_source	Which profile was scraped

👉 profile_source is CRITICAL
It tells which LinkedIn profile the data belongs to.

▶️ Run Scraper (Apify → MySQL)

From src folder:

python3 apify_to_mysql.py

Input examples
satyanadella


or

https://www.linkedin.com/in/

What happens internally?

User enters profile

Script builds LinkedIn URL

Apify fetches post data

Python processes JSON

Data is inserted into MySQL

🔍 Verify Data in MySQL (CRITICAL SKILL)
Check total rows
SELECT COUNT(*) FROM posts;

View latest inserted data
SELECT
  id,
  profile_source,
  post_url,
  likes
FROM posts
ORDER BY id DESC
LIMIT 10;

Check which profiles exist
SELECT DISTINCT profile_source FROM posts;

🧹 Clear Old Data (Optional)
TRUNCATE TABLE posts;


⚠️ This deletes all rows but keeps the table.

🌐 Run FastAPI Server (Local)
python3 -m uvicorn main:app --reload


Open browser:

http://127.0.0.1:8000


Expected response:

{
  "message": "LinkedIn Insights Server is running"
}

☁️ Cloud Deployment (Render)

Render settings:

Build command:

pip install -r requirements.txt


Start command:

uvicorn main:app --host 0.0.0.0 --port 10000


Environment Variable:

APIFY_TOKEN=apify_api_your_real_token

🛡️ Security Practices Followed

✅ No API keys in code

✅ Environment variables used

✅ GitHub push protection compliant

✅ Clean commit history

❗ Common MySQL Problems & Fixes
❌ No database selected
USE linkedin_insights;

❌ Data not visible

Use:

ORDER BY id DESC

❌ Same profile appears

Because old data still exists — use TRUNCATE
