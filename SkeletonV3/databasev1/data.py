import sqlite3

# Connect to database
conn = sqlite3.connect('Timeline_selectV2.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS engineer (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    StepName TEXT,
    Description TEXT
)
''')

# Insert information
cursor.execute("""
INSERT INTO engineer (StepName, Description) VALUES

('Timeline', '''
# Timeline

| Stage | Typical Age | Qualification/Outcome |
| Year 11 | 15–16     | NCEA Level 1 |
| Year 12 | 16–17 | NCEA Level 2 |
| Year 13 | 17–18 | NCEA Level 3 and University Entrance |
| University | 18–22 | Bachelor of Engineering (Honours) |
| Graduate Engineer | 22–25 | Professional work experience |
| Chartered Engineer (optional) | 25+ | Chartered Professional Engineer (CPEng) |
'''),

('Year 11', '''
## Year 11 (NCEA Level 1)

Year 11 is the foundation for an engineering career. Students should choose subjects that develop mathematical, scientific, and practical problem-solving skills.

### Recommended subjects:

-  Mathematics 
-  Science 
-  English 
-  Digital Technologies (recommended) 
-  Engineering, Technology, or Materials and Manufacturing Technology (MMT) 

### Goals:

-  Achieve NCEA Level 1. 
-  Develop strong literacy and numeracy skills. 
-  Begin building practical engineering experience through school projects, clubs, or competitions. 
'''),

('Year 12', '''
## Year 12 (NCEA Level 2)

Year 12 is one of the most important years for students planning to study engineering at university.

### Recommended subjects:

-  Mathematics (preferably Advanced Mathematics) 
-  Physics 
-  English 
-  Chemistry (recommended) 
-  Engineering or Digital Technologies 

### Goals:

-  Achieve NCEA Level 2. 
-  Earn strong grades, particularly in Mathematics and Physics. 
-  Meet the requirements for University Entrance (UE). 
'''),

('Year 13', '''
## Year 13 (NCEA Level 3)

Students continue studying subjects that prepare them for engineering degrees.

### Recommended subjects:

-  Calculus 
-  Physics 
-  English or another University Entrance approved subject 
-  Engineering or Technology (if available) 

### Goals:

-  Achieve NCEA Level 3. 
-  Gain University Entrance. 
-  Meet the specific entry requirements for a Bachelor of Engineering (Honours). 
'''),

('University Entrance', '''
# University Entrance Requirements

To study engineering at most New Zealand universities, students generally need:

-  NCEA Level 3 
-  University Entrance (UE) 
-  Strong achievement in Calculus and Physics 
-  Literacy and numeracy requirements 

Some universities may also have rank score requirements.
'''),

('Bachelor of Engineering (Honours)', '''
# Bachelor of Engineering (Honours)

After secondary school, students usually enrol in a **Bachelor of Engineering (Honours) (BE(Hons))**, which normally takes **four years** to complete.

### First Year

Students study common engineering subjects such as:

-  Engineering Mathematics 
-  Physics 
-  Programming 
-  Design 
-  Engineering Mechanics 
-  Professional Engineering Practice 

### Second to Fourth Year

Students specialise in an engineering discipline, such as:

-  Mechanical Engineering 
-  Civil Engineering 
-  Electrical Engineering 
-  Mechatronics Engineering 
-  Software Engineering 
-  Chemical Engineering 
-  Biomedical Engineering 

Throughout the degree, students complete laboratory work, group projects, design projects, and industry-related assignments.
'''),

('Practical Experience', '''
# Practical Experience

Engineering students are encouraged to complete internships or work placements during university holidays.

Practical experience allows students to:

-  Apply classroom knowledge. 
-  Develop workplace skills. 
-  Build professional connections. 
-  Improve employment opportunities after graduation. 

Many engineering programmes also require a period of supervised practical work before graduation.
'''),

('Graduating', '''
# Graduating

After successfully completing the four-year degree, students graduate with a **Bachelor of Engineering (Honours)**.

At this stage they are considered **graduate engineers** and can begin working in industry.
'''),

('Becoming a Professional Engineer', '''
# Becoming a Professional Engineer

Graduate engineers usually work under experienced engineers while gaining professional experience.

During this stage they continue developing skills in:

-  Engineering design 
-  Project management 
-  Communication 
-  Problem solving 
-  Professional responsibility 
'''),

('Becoming Chartered (Optional)', '''
# Becoming Chartered (Optional)

After several years of professional experience, engineers can apply to become a **Chartered Professional Engineer (CPEng)** through Engineering New Zealand.

To become chartered, engineers must demonstrate that they:

-  Meet professional competency standards. 
-  Have sufficient engineering experience. 
-  Follow professional and ethical practices. 
-  Continue developing their engineering knowledge. 

Chartered status is recognised throughout New Zealand and can improve career opportunities, particularly in senior engineering positions.
'''),

('Career Opportunities', '''
# Career Opportunities

Once qualified, engineers can work in many industries, including:

-  Construction 
-  Manufacturing 
-  Transport 
-  Energy 
-  Marine engineering 
-  Aerospace 
-  Electronics 
-  Robotics 
-  Software development 
-  Environmental engineering 

Engineers may also progress into management, research, consulting, or start their own engineering businesses.
''')
""")

# Save changes
conn.commit()


# ==========================
# Get individual information
# ==========================

cursor.execute('SELECT Description FROM engineer WHERE StepName = "Timeline"')
result = cursor.fetchone()
print(result[0])

cursor.execute('SELECT Description FROM engineer WHERE StepName = "Year 11"')
result = cursor.fetchone()
print(result[0])

cursor.execute('SELECT Description FROM engineer WHERE StepName = "Year 12"')
result = cursor.fetchone()
print(result[0])

cursor.execute('SELECT Description FROM engineer WHERE StepName = "Year 13"')
result = cursor.fetchone()
print(result[0])

cursor.execute('SELECT Description FROM engineer WHERE StepName = "University Entrance"')
result = cursor.fetchone()
print(result[0])

cursor.execute('SELECT Description FROM engineer WHERE StepName = "Bachelor of Engineering (Honours)"')
result = cursor.fetchone()
print(result[0])

cursor.execute('SELECT Description FROM engineer WHERE StepName = "Practical Experience"')
result = cursor.fetchone()
print(result[0])

cursor.execute('SELECT Description FROM engineer WHERE StepName = "Graduating"')
result = cursor.fetchone()
print(result[0])

cursor.execute('SELECT Description FROM engineer WHERE StepName = "Becoming a Professional Engineer"')
result = cursor.fetchone()
print(result[0])

cursor.execute('SELECT Description FROM engineer WHERE StepName = "Becoming Chartered (Optional)"')
result = cursor.fetchone()
print(result[0])

cursor.execute('SELECT Description FROM engineer WHERE StepName = "Career Opportunities"')
result = cursor.fetchone()
print(result[0])


# Close database
conn.close()