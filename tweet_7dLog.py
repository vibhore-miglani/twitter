import urllib
import json
from datetime import date,timedelta 

def search_twitter():			
	'''FUNCTION TO FETCH TWEETS OF THE USER SCREEN_NAME SPECIFIED'''
	name = raw_input("\n enter user screen_name whoose 7 day log is required: ")
	url = "https://api.twitter.com/1/statuses/user_timeline.json?screen_name=" + name +"&count=200"
	print "url=",url
	
	#get url response from twitter api
	response = urllib.urlopen(url).read()
	data = json.loads(response)
	
	#if some errors are present in respponse, again create and send new URL(mAx 3 times)
	
	if ("error" in data) or ("errors" in data) :
		print "invalid user name"
		return 1
		
	return data	

	
def monthStrToInt(m):
	'''to convert month value in string form to integer form'''
	if m == 'Jan':
		m=1
	elif m == 'Feb':
		m=2
	elif m == 'Mar':
		m=3
	elif m == 'Apr':
		m=4
	elif m == 'May':
		m=5
	elif m == 'Jun':
		m=6
	elif m == 'Jul':
		m=7
	elif m == 'Aug':
		m=8
	elif m == 'Sep':
		m=9
	elif m == 'Oct':
		m=10
	elif m == 'Nov':
		m=11
	elif m == 'Dec':
		m=12
	return m
	

def print_tweets(tweets):
	'''function to print tweets'''
	
	try:
		print tweets[0]['user']['name'] + ': '
	except:
		print "invalid response"
		return
	
	i=0
	today= date.today()
	td=timedelta(7)
	threshold =  today-td
	
	for tweet in tweets:
		try:
			created_at=tweet['created_at']
		except:
			print "created_at filed"
			pass
		dateStr=created_at.split(" ")
		d=int (dateStr[2])
		m=dateStr[1]
		y=int (dateStr[5])
		m = monthStrToInt(m)		
		tweetDate = date(y,m,d)
		print "date: ", tweetDate
		if tweetDate > threshold :	
			try :
				print "_" * 50 + 3*'\n' , i , ' ::: ' + tweet['created_at']+ "---->" + tweet['text'] + '\n'
			
			except:	
				pass
		else :
			break
		i=i+1
	print ("\n" + "_"* 100)*3  +"\n NO of tweets user has done in last 7 days =", i

		
if 	__name__ == "__main__" :
	count = 0
	while (count < 3):
		results = search_twitter()
		if results == 1 :
			count= count + 1
		else :
			break
		
	id = print_tweets(results)
	
#https://api.twitter.com/1/statuses/user_timeline.json?screen_name=priyankachopra&count=200