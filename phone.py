import urllib2
import urllib
# Specify the url
url = 'https://proapi.whitepages.com/2.0/phone.json?phone_number=2069735100&api_key=INSERTKEY'
# Package Request
request = urllib2.Request(url)
# Send the request and retrieve the response
response = urllib2.urlopen(request)
# Extract the response
html = response.read()
# Display response
print html
