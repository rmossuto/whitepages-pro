import urllib2
import urllib
# Specify the url
url = 'https://proapi.whitepages.com/2.0/person.json?name=Jane+Smith&api_key=60994ffaf2b89f76b1bd54c33c530403'
# Package Request
request = urllib2.Request(url)
# Send the request and retrieve the response
response = urllib2.urlopen(request)
# Extract the response
html = response.read()
# Display response
print html
