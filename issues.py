import requests
import json

# requests the information from the site.
#r = requests.get('https://api.github.com/repos/code-newbies/python-thursday-adventure/issues')
# By using the optional parameters, we can tell the github api we want only issues from a specific milestone.
payload = {'milestone':5}
r = requests.get('https://api.github.com/repos/KJMSystems/pyshownoter/issues', payload)
# This will grab the text of the response either as unicode(text)
# or bytes(content)
# It then deserializes the content into a useable python object using
# json.loads
data = json.loads(r.text or r.content) 

print ("Number of issues: %d" % len(data))

# each issue is an item in a list.
# using the for loop we can grab its index and call that item,
# it then acts like any normal JSON, which acts like a dict
# so we can call values using the keys.
for index in range(0, len(data)):
    
    print ("Title: {title}\nBody: {body}\nMilestone: {milestone}\n".format(title=data[index]['title'], 
                                                  body=data[index]['body'], milestone=data[index]['milestone']['title']))
    
