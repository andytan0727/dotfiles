#!/usr/bin/python
# vim: set fileencoding=UTF-8 :

import urllib
import codecs
from xml.dom import minidom

email = 'mail'   #your email here..feel free to ommit the '@...' suffix
passwd = 'password'  #your password here

url = 'https://%s:%s@mail.google.com/mail/feed/atom' % (email, passwd)

dom = minidom.parse(urllib.urlopen(url))

count = dom.getElementsByTagName('fullcount')[0].childNodes[0].nodeValue

# names = []
# sums = []

# for n in dom.getElementsByTagName('name'):
#     name = n.childNodes[0].nodeValue.encode("utf-8")
#     names.append(name)
#     print "Email from: " + name

counter = 0
whole_summary = dom.getElementsByTagName("summary")
print "Unread mails:"
for n in dom.getElementsByTagName('name'):
    if counter < 8:
        name = n.childNodes[0].nodeValue.encode("utf-8")
        summary = whole_summary[counter].childNodes[0].nodeValue.encode("utf-8")
        brief_summary = " ".join(summary.split(" ")[0:8])
        print str(counter + 1) + ": " + name + " - " + brief_summary + " ..."
    counter += 1

# for s in dom.getElementsByTagName('summary'):
#     summary = s.childNodes[0].nodeValue.encode("utf-8")
#     sums.append(summary)
#     print summary

print "You got " + count + " unread mails  \n "
# mail = dict(zip(names , sums))
# for k, v in mail.iteritems():
#     print "{:<13} {:<13}".format(k, v)
# for key, value in mail.items():
#     print key + value + '\n'
