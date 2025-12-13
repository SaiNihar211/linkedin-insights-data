from apify_client import ApifyClient
import mysql.connector

# =======================
# APIFY CONFIG
# =======================
import os

APIFY_TOKEN = os.getenv("APIFY_TOKEN")


client = ApifyClient(APIFY_TOKEN)

# =======================
# USER INPUT (NO BACKEND CHANGE)
# =======================
user_input = input(
    "Enter LinkedIn PROFILE NAME or FULL PROFILE URL: "
).strip()

if user_input.startswith("http"):
    profile_url = user_input
    username = user_input.rstrip("/").split("/")[-1]
else:
    username = user_input
    profile_url = f"https://www.linkedin.com/in/{username}/"


print("▶ Using profile URL:", profile_url)

run_input = {
    "profileUrls": [profile_url],
    "username": username,   # 👈 FORCE CORRECT PROFILE
    "resultsLimit": 5
}


print("▶ Running Apify actor...")
run = client.actor("apimaestro/linkedin-profile-posts").call(run_input=run_input)

dataset_id = run["defaultDatasetId"]
print("▶ Dataset ID:", dataset_id)

posts = client.dataset(dataset_id).list_items().items
print(f"▶ Fetched {len(posts)} posts")



# =======================
# MYSQL CONFIG
# =======================
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="halloween",   # change if your password is different
    database="linkedin_insights"
)

cursor = conn.cursor()

# =======================
# INSERT DATA INTO MYSQL
# =======================
for post in posts:
    post_id = post.get("full_urn", "")

    author = post.get("author", {})
    author_name = f"{author.get('first_name', '')} {author.get('last_name', '')}"

    post_text = post.get("text", "")
    post_date = post.get("posted_at", {}).get("date", "")

    stats = post.get("stats", {})
    likes = stats.get("like", 0)
    comments = stats.get("comments", 0)
    reposts = stats.get("reposts", 0)

    post_url = post.get("url", "")

    cursor.execute("""
        INSERT INTO posts (
            post_id, author_name, post_text, post_date,
            likes, comments, reposts, post_url
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        post_id, author_name, post_text, post_date,
        likes, comments, reposts, post_url
    ))

conn.commit()
cursor.close()
conn.close()

print("✅ Data fetched from Apify and stored in MySQL successfully!")

