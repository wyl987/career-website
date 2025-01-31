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

def add_application_to_db(job_id, data):
  try:
    with engine.connect() as conn:
      query = text("INSERT into applications (job_id, full_name, email, linkedin_url, resume_url ) VALUES (:job_id, :full_name, :email, :linkedin_url, :resume_url)")
      
      conn.execute(query,
                  {"job_id" : job_id,
                    "full_name": data["fullname"],
                    "email": data["email"],
                    "linkedin_url": data["linkedin_url"],
                    "resume_url": data["resume_url"]}
                  )
      conn.commit()
      
  except Exception as e:
      print(f"An error occurred: {e}")
  