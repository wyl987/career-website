from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://admin:aWfRDVV4WNOSoaOQ8uQ7@career-website.czame0giewij.ap-southeast-2.rds.amazonaws.com/careerwebsite?charset=utf8mb4")

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      row_dict = row._asdict()
      jobs.append(row_dict)
  
  return jobs