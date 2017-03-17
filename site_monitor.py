from HTMLParser import HTMLParser
import requests
import time
url = raw_input("Enter Link(http://...): ")
start_tags = 0
end_tags = 0
data_ = 0
entities_ = 0
charrefs_ = 0
comments_ = 0
counter = 1	
class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		global start_tags 
		start_tags += 1
	def handle_endtag(self, tag):
		global end_tags
		end_tags += 1
	def handle_data(self, data):
		global data_
		data_ += 1
	def handle_entityref(self, name):
		global entities_
		entities_ += 1
	def handle_charref(self, name):
		global charrefs_
		charrefs_ += 1
	def handle_comment(self, data):
		global comments_
		comments_ += 1
while True:
	headers = {'User-Agent': 'Chrome/39.0.2171.95'}
	page_source = requests.get(url,headers=headers)
	parser = MyHTMLParser()
	parser.feed(page_source.text)
	print "--------------------"
	print "Check#: " + str(counter)
	print "--------------------"
	print "Start Tags: " + str(start_tags)
	print "End Tags: " + str(end_tags)
	print "Middle Stuff(Data): " + str(data_)
	print "Entities: " + str(entities_)
	print "Charrefs: " + str(charrefs_)
	print "Comments: " + str(comments_)
	counter += 1
	print "--------------------"
	start_tags = 0
	end_tags = 0
	data_ = 0
	entities_ = 0
	charrefs_ = 0
	comments_ = 0	
	time.sleep(4)
