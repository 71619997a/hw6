import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

q = '''
SELECT courses.id, name,  mark
FROM students, courses
WHERE courses.id = students.id
'''

students = {}
for record in c.execute(q):
    id = record[0]
    if id in students:
        students[record[0]]['grades'].append(record[2])  # add mark to grade list
    else:
        students[record[0]] = {'name': record[1], 'grades': [record[2]]}  # start list of grades
print 'name\t\tid\tgrade'
for id, student in students.iteritems():
    print student['name'] + '    \t', str(id) + '\t',
    print sum(student['grades']) / len(student['grades'])
