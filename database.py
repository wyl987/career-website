from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()
db_connection_string = os.getenv('DB_CONNECTION_STRING')

engine = create_engine(db_connection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      row_dict = row._asdict()
      jobs.append(row_dict)
  
  return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("select * from jobs where id = :val"),
      {"val": id}
      )
    row = result.fetchone()
    if row:
      job = row._asdict()
    else:
      job = None
  
  return job