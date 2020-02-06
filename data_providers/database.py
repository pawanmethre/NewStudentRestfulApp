import psycopg2

con = psycopg2.connect(database=df0a7s9k9i8bh9, user='postgres', password='108', port='5432', host='//wxnboxwerxwxab:62aa8bf63483e06b6abab99f56e52495d3d5ea5bf4adcb37965fb84ee54f88ae@ec2-184-72-236-57.compute-1.amazonaws.com')

cur = con.cursor()
create_stud_table = "CREATE TABLE students (rollno INT PRIMARY KEY NOT NULL, name TEXT NOT NULL, age INT NOT NULL, branch TEXT NOT NUll)"
cur.execute(create_stud_table)

create_user_table = "CREATE TABLE  users (username TEXT NOT NULL, password TEXT NOT NULL, email TEXT NOT NULL, role TEXT NOT NULL)"
cur.execute(create_user_table)


cur.close()
con.commit()
con.close()