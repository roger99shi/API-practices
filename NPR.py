
>>>>>>>>>>>>>>>>>>>>story
from urllib2 import urlopen
from json import load, dumps

url = 'http://api.npr.org/query?apiKey=' 
key = 'API_KEY'
url = url + key
url += '&numResults=1&format=json&id=1007&requiredAssets=text,image,audio' #1007 is science

response = urlopen(url)
json_obj = load(response)

# uncomment 3 lines below to see JSON output to file
f = open('output.json', 'w')
f.write(dumps(json_obj, indent=4))
f.close()

for story in json_obj['list']['story']:
	print "TITLE: " + story['title']['$text'] + "\n"
	print "DATE: " +story['storyDate']['$text']+ "\n"
	print "TEASER: " + story['teaser']['$text']+ "\n"
	if 'byline' in story:
	    print "BYLINE: " + story['byline'][0]['name']['$text']+ "\n"
	if 'show' in story:
	    print "PROGRAM: " + story['show'][0]['program']['$text']+ "\n"
	print "NPR URL: " + story['link'][0]['$text']+ "\n"   
	print "IMAGE: " + story['image'][0]['src']+ "\n"  
	if 'caption' in story:
	    print "IMAGE CAPTION: " + story['image'][0]['caption']['$text'] + "\n"
	if 'producer' in story:
	    print "IMAGE CREDIT: " +story['image'][0]['producer']['$text']+ "\n"
	print "MP3 AUDIO: "+story['audio'][0]['format']['mp3'][0]['$text']+'\n'
	for paragraph in story['textWithHtml']['paragraph']:
	    print paragraph['$text']+'\n'
>>>>>>>>>>>>>>podcast and RSS
from urllib2 import urlopen
from urllib import quote


key = "API_KEY"
url = 'http://api.npr.org/query?apiKey='
url += key
url+='&numResults=3&action=Or&requiredAssets=audio&format=Podcast'

npr_id=raw_input("Enter comma-separated NPR IDs or leave blank.")
search_string=raw_input( "Enter your search string or leave blank.")
feed_title =raw_input( "What's your feed title?")
if npr_id !='' or search_string!='':
    raw_input("Hit Enter to download your podcast.")
    if npr_id !='':
        url+='&id=%s'%(npr_id)
    if search_string!='':
        url+="&searchTerm=%s"%(quote(search_string))
    if feed_title!='':
        url+="&title=%s"%(quote(feed_title))
else:
    print "You must enter an NPR ID, a search term, or both."
>>>>>>>>>>>>>>>>transcript
from urllib2 import urlopen
from json import load

key = "API_KEY"

url="http://api.npr.org/transcript?apiKey="
url+=key
url+='&format=json&id=152248901'

response=urlopen(url)
j=load(response)
for paragraph in j["paragraph"]:
    print paragraph["$text"]+'\n'
>>>>>>>>>>>>>>>>>>>>>>>>>>>station
from urllib2 import urlopen
from json import load

key = "API_KEY"

def build_api_call(key):
    url='http://api.npr.org/stations?apiKey='
    url+=key
    url+='&format=json'
    zip_code=raw_input("Enter your zip code:")
    url+='&zip=%s'%(zip_code)
    return url

def call_station_api(url):
    response=urlopen(url)
    j=load(response)
    return j

def parse_station_json(json_obj):
    for station in json_obj['station']:
        print station['callLetters']['$text'] +": " +station['marketCity']['$text'] +", " +station['state']['$text']+"Frequency:"+station['frequency']['$text'] +station['band']['$text']
    if 'url' in station:
        print "MP3 Streams: "
        for link in station["url"]:
            if link["type"]=="Audio MP3 Stream":
                print "\t" + link["title"] + " - " + link["$text"]
    
url=build_api_call(key)
print 'URL :'+url

json_obj=call_station_api(url)
parse_station_json(json_obj)