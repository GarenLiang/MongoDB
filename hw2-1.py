# MongoDB
import pymongo
import sys



connection = pymongo.MongoClient("mongodb://localhost")
db = connection.students
grades = db.grades

try:
	cursor = grades.find( { "type": "homework" }) \
	               .sort( [ ("student_id", pymongo.ASCENDING), \
	               	        ( "score", pymongo.ASCENDING)])
except:
	print "Unexpected error:", sys.exc_info()[ 0]

previous_id = None
student_id = None

for doc in cursor:
 	student_id = doc[ 'student_id']
	if student_id != previous_id:
  		previous_id = student_id
  		print "Removing", doc
  		grades.remove( { '_id': doc[ '_id'] } )
