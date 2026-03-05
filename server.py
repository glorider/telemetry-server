from fastapi import FastAPI, Request
<<<<<<< HEAD
=======
import psycopg2
import os
>>>>>>> a1dcf0c (up)

app = FastAPI()

# get database url from environment
DATABASE_URL = os.getenv("DATABASE_URL")

# connect to database
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# ---- CREATE TABLE WHEN SERVER STARTS ----
cursor.execute("""
CREATE TABLE IF NOT EXISTS telemetry (
    id SERIAL PRIMARY KEY,
    ip TEXT,
    hostname TEXT,
    os TEXT
)
""")

conn.commit()
# -----------------------------------------

@app.get("/")
def home():
    return {"status": "running"}

<<<<<<< HEAD
@app.post("/collect")
async def collect(request: Request):
    data = await request.json()
    print(data)
    return {"status": "received"}
=======

@app.post("/collect")
async def collect(request: Request):

    data = await request.json()
    client_ip = request.client.host

    hostname = data.get("hostname")
    os_name = data.get("os")

    cursor.execute(
        "INSERT INTO telemetry (ip, hostname, os) VALUES (%s, %s, %s)",
        (client_ip, hostname, os_name)
    )

    conn.commit()

    return {"status": "saved"}
>>>>>>> a1dcf0c (up)
