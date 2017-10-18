#!/usr/bin/python2

import imaplib
import sys
import getpass
import email
from email.parser import HeaderParser
from email.header import decode_header
import datetime

imap_host = 'outlook.com'
imap_user = 'boon960727@hotmail.com'
imap_pass = 'password'

## connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host)

## login to server
imap.login(imap_user, imap_pass)


# select mailbox
imap.select('INBOX')

def get_mostnew_email(messages):
    """
    Getting in most recent emails using IMAP and Python
    :param messages:
    :return:
    """
    ids = messages[0]  # data is a list.
    id_list = ids.split()  # ids is a space separated string
    #latest_ten_email_id = id_list  # get all
    latest_ten_email_id = id_list[-10:]  # get the latest 10
    keys = map(int, latest_ten_email_id)
    news_keys = sorted(keys, reverse=True)
    str_keys = [str(e) for e in news_keys]
    return  str_keys

def process_mailbox(M):
    rv, data = M.search(None, "ALL")
    if rv != 'OK':
        print "No messages found!"
        return

    # retrive last 10 mails
    mails = sorted(data[0].split()[-5:], reverse=True)
    counter = 1

    for item in mails:
        rv, data = M.fetch(item, '(RFC822)')
        if rv != 'OK':
            print "ERROR getting message", item
            return

        # return message object
        # access as dictionary
        msg = email.message_from_string(data[0][1])
        decode_utf_8_header = decode_header(msg['Subject'])[0:8]
        default_charset = 'ASCII'
        ascii_header = ''.join([unicode(t[0], t[1] \
                                        or default_charset) for t in decode_utf_8_header])
        truncated_header = ' '.join(ascii_header.split(' ')[0:8])
        date_tuple = email.utils.parsedate_tz(msg['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(
                email.utils.mktime_tz(date_tuple))
            print local_date.strftime("%a, %d %b %Y") + ': '
        print '%s: %s ...' % (counter, truncated_header)
        counter += 1

process_mailbox(imap)

# unread
status, response = imap.status('INBOX', "(UNSEEN)")
unreadcount = int(response[0].split()[2].strip(').,]'))
print 'You have ' + str(unreadcount) + ' unread mails.'


# close and clean connection
imap.close()
imap.logout()
