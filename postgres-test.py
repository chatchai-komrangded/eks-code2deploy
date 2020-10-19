import os

import boto3
import psycopg2

HOST = os.getenv('HOST')
PORT = "5432"
USER = os.getenv('USER')
REGION = "ap-southeast-1"
DBNAME = os.getenv('DATABASE')
token = os.getenv('PASS')


session = boto3.Session()
client = boto3.client('rds', region_name=REGION)

#token = client.generate_db_auth_token(DBHostname=HOST, Port=PORT, DBUsername=USER, Region=REGION)

conn = None
try:
    conn = psycopg2.connect(host=HOST, port=PORT, database=DBNAME, user=USER, password=token, connect_timeout=10)
    cur = conn.cursor()
    cur.execute("""SELECT version()""")
    query_results = cur.fetchone()
    print(query_results)
    cur.close()
except Exception as e:
    print("Database connection failed due to {}".format(e))
finally:
    if conn is not None:
        conn.close()