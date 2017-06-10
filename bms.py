import urllib2
from bs4 import BeautifulSoup
import time
import yagmail


book_my_show_url = "https://in.bookmyshow.com/buytickets/the-mummy-3d-chennai/movie-chen-ET00050002-MT/20170611"    #change this url according to your movie

sender_email = raw_input("Enter your email address to send mail : ")

email_password = raw_input("Enter your email password : ")

receiver_email = raw_input("Enter the email address you want to receive  mail : ")

theatre_name="PVR: Ampa"    #change the theatre name to your wish 


while True:
        
	requester = urllib2.Request(book_my_show_url, headers={'User-Agent': "Magic Browser"})

	connector = urllib2.urlopen(requester)

	connector_reader = connector.read()

	soup = BeautifulSoup(connector_reader, "lxml")

	text = soup.get_text()

	if theatre_name in text:
		print "Tickets Available"
		sender = yagmail.SMTP(sender_email, email_password)
		sender.send(receiver_email, "Tickets Available" , contents='Hey There ! Time to book your tickets at ' + theatre_name)
		print "Notification mail sent"
		break
	else:
		print "Nope not yet"
	time.sleep(300)
        
