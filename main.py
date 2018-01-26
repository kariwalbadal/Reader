import imaplib
import email

def read(username, password):
    # Login to INBOX
    imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    imap.login(username, password)
    imap.select('INBOX')

    # Use search(), not status()
    status, response = imap.search(None, '(UNSEEN)')
    unread_msg_nums = response[0].split()

    # Print the count of all unread messages
    print(len(unread_msg_nums))
    data_list = []
    for e_id in unread_msg_nums:
        _, response = imap.uid('fetch', e_id, '(RFC822)')
        try:
            html = response[0][1].decode('utf-8') # if this fails that means that there is no readable data
            #print "gya"
            email_message = email.message_from_string(html)
            #print "here"
            data_dict = {}
            data_dict['mail_to'] = email_message['To']
            data_dict['mail_subject'] = email_message['Subject']
            data_dict['mail_from'] = email.utils.parseaddr(email_message['From'])
            if email_message.is_multipart():
                abc = ""
                for item in email_message.get_payload():
                    if item.get_content_maintype() == 'text':
                        abc+=(item.get_payload())
            else:
                abc+=(email_message.get_payload())
            data_dict['body'] = abc

            data_list.append(data_dict)
        except Exception as e:
            #announce that this mail has no readable data
            print(str(e))
    with open("result.txt", "w") as filename:
        for item in data_list:
            filename.write(str(item['body']))

    # Mark them as seen
    #for e_id in unread_msg_nums:
    #    imap.store(e_id, '+FLAGS', '\Seen')
def main(username, password):
    read(username, password)