# MongoDB
import pymongo
import sys

connection=pymongo.MongoClient("mongdb://localhost")
db=connection.school
students=db.students

def remove_lowest_homework_score(scores):
	homework_scores=[score for score in scores if score[u"type"]==u"homework"]
	lowest=min([score[u"score"] for score in homework_scores])
	return [score for score in scores \
	        if(score[u"type"]!=u"homework")\
	        or(score[u"type"]==u"homework" and score[u"score"!=lowest])
def update_scores(coll,doc_id,new_scores):
	try:
		coll.update({"_id":doc_id},{"$set":{"scores":new_scores}})
    except:
    	print "Unexpected error while updating:",sys.exc_info[0]

def main(argv):
	try:
		cursor=students.find({'scores.type':'homework'})
    except:
    	print "Unexpected error while finding:",sys.exc_info()[0]
    for doc in cursor:
    	id=doc["_id"]
    	scores=doc["scores"]
    	updated_scores=remove_lowest_homework_score(scores)
    	update_scores(students,id,updated_scores)
    	print "updated doc %s:\n  scores:%s\nnew scores:%s" %( id,scores,updated_scores)

if __name__=="__main__":
	main(sys.argv[1:])
