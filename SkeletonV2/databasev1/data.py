import sqlite3
import os

#conn = sqlite3.connect('Timeline_select.db')

conn = os.path.join(os.path.dirname(__file__), "databasev1", "Timeline_select.db")


def get_connection():
    os.makedirs(os.path.dirname(conn), exist_ok=True)
    return sqlite3.connect(conn)

cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS engineer (ID INTEGER PRIMARY KEY AUTOINCREMENT, StepName TEXT,  Description TEXT)')
cursor.execute("""INSERT INTO engineer (StepName, Description) VALUES
    ('Timeline','
    TIMELINE
    Age	    Stage
    15–16,	Year 11 (Level 1).

    16–17,	Year 12 (Level 2).

    17–18,	Year 13 (Level 3).

    18–22,	Bachelor of Engineering (Honours) or Navy/Apprenticeship.

    22–25,	Graduate Engineer.'),

    ('Year 11', 'Year 11 (NCEA Level 1)
1. Choose the right subjects

Aim to take:
    ✅ Mathematics
    ✅ Science
    ✅ English
    ✅ Digital Technologies (helpful)
    ✅ Engineering/MMT/Woodwork (very helpful)

If your school offers them:
    Physics (if available)
    Electronics
    Design & Visual Communication

2. Get good grades
Try to achieve:
    - Merit or Excellence where possible
    - Strong literacy and numeracy credits
    These make Level 2 and university easier.

3. Start building experience
Examples:
    - Robotics club
    - Coding
    - Engineering competitions
    - Maker projects
    - 3D printing
    - Woodworking
    - Metalworking'), 

    ('Year 12', 
'Year 12 (NCEA Level 2)
This is probably the most important year.
Take:
    ✅ Calculus/Advanced Maths
    ✅ Physics
    ✅ English

Helpful:
    - Chemistry
    - Digital Technologies
    - Engineering
    - Aim for University Entrance (UE)

You need:
    - 14 credits in three approved subjects
    - Literacy requirement
    - Numeracy requirement

Universities look closely at your Level 2 results.'), 

    ('Year 13', 'D'), 

    ('University Entrence', 'E'), 

    ('Bachelor of Engineering (Honours)', 'F')

    ('Practical Experience', 'G')

    ('Graduating', 'H')

    ('Becoming a Professional Engineer', 'I')

    ('Career Opportunities', 'J')
""")
conn.commit()

cursor.execute('SELECT * FROM engineer')
result = cursor.fetchall()

for row in result:
    print("StepName: ", row[1], "Description:", row [2])



cursor.execute('SELECT Description FROM engineer WHERE StepName= "Timeline"')
result = cursor.fetchone()
print(result[0])
cursor.execute('SELECT Description FROM engineer WHERE StepName= "Year 11"')
result = cursor.fetchone()
print(result[0])
cursor.execute('SELECT Description FROM engineer WHERE StepName= "Year 12"')
result = cursor.fetchone()
print(result[0])
cursor.execute('SELECT Description FROM engineer WHERE StepName= "Year 13"')
result = cursor.fetchone()
print(result[0])
cursor.execute('SELECT Description FROM engineer WHERE StepName= "University Entrence"')
result = cursor.fetchone()
print(result[0])
cursor.execute('SELECT Description FROM engineer WHERE StepName= "Bachelor of Engineering (Honours)"')
result = cursor.fetchone()
print(result[0])
cursor.execute('SELECT Description FROM engineer WHERE StepName= "Practical Experience"')
result = cursor.fetchone()
print(result[0])
cursor.execute('SELECT Description FROM engineer WHERE StepName= "Graduating"')
result = cursor.fetchone()
print(result[0])
cursor.execute('SELECT Description FROM engineer WHERE StepName= "Becoming a Professional Engineer"')
result = cursor.fetchone()
print(result[0])
cursor.execute('SELECT Description FROM engineer WHERE StepName= "Career Opportunities"')
result = cursor.fetchone()
print(result[0])
conn.close()