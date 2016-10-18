import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================

try:
    q = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)"
    c.execute(q)    #run SQL query

    q = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)"
    c.execute(q)
except sqlite3.OperationalError:
    print 'Tables already created, skipping'

with open('peeps.csv') as f:
    student_reader = csv.DictReader(f)
    for row in student_reader:
        name = repr(row['name'])
        age = row['age']
        id = row['id']
        q = 'INSERT INTO students VALUES(' + name + ',' +age+','+ id + ')'
        c.execute(q)
                
with open('courses.csv') as f:
    course_reader = csv.DictReader(f)
    for row in course_reader:
        code = repr(row['code'])
        mark = row['mark']
        id = row['id']
        q = 'INSERT INTO courses VALUES('+code+','+mark+','+id+')'
        c.execute(q)

def testdb():  # tester
    for i in c.execute('SELECT * FROM students'):
        print i
    print '\n'
    for i in c.execute('SELECT * FROM courses'):
        print i

# testdb()

#==========================================================
db.commit() #save changes
db.close()  #close database


