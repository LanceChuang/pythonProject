import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com" # gmail host
port = 587 # gmail port
username = "xxxx@gmail.com"
password = "xxxxx"
from_email = username
to_list = ["xxxxx@gmail.com"]


class MessageUser(object):
	user_details = []
	messages = []
	email_messages = []
	base_message = """Hi, {name}!

Thank you for the purchase on {date}.
We hope you are excited about using it. Just as
a reminder the purchase total was ${total}.
Have a great one!

Team Lance
"""		

	def add_user(self,name,amount, email=None):
		name = name[0].upper() + name[1:].lower() # adjust names
		amount = "%.2f" %(amount)
		detail = {
			"name": name,
			"amount": amount,
		}
		today = datetime.date.today()
		# print(today)
		date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
		detail['date'] = date_text
		if email is not None:
			detail ["email"] = email
		self.user_details.append(detail)

	def get_details(self):
		return self.user_details

	def make_messages(self):
		if len(self.user_details) > 0: # list not empty
			for detail in self.user_details:
				name = detail["name"]
				amount = detail["amount"] # already format in add user
				date = detail["date"]
				message = self.base_message
				new_msg = message. format(
					name = name,
					date = date,
					total = amount
				)
				user_email = detail.get("email") # if not get email then return None
				if user_email:
					user_data ={
						"email": user_email,
						"message": new_msg
					}
					self.email_messages.append(user_data)
				else:
					self.messages.append(new_msg)

			return self.messages
		return [] # if user empty	

	def send_email(self):
		self.make_messages()
		if len(self.email_messages) > 0:
			for detail in self.email_messages:
				user_email = detail["email"]
				user_message = detail["message"]
				# run email here
				try:
					email_conn = smtplib.SMTP(host,port)
					email_conn.starttls()
					email_conn.login(username,password)


					the_msg = MIMEMultipart("alternative") # call html message
					the_msg["Subject"] = "Hello there!"
					the_msg["From"] = from_email
					the_msg["To"] = user_email
					part_1 = MIMEText(user_message,'plain')
					the_msg.attach(part_1)
					# print(the_msg.as_string())
					email_conn.sendmail(from_email,[user_email],the_msg.as_string())
					email_conn.quit()
				except smtplib.SMTPException:
					print("error sending message")
			return True

		return False # empty in email_messages	

obj = MessageUser()
print(obj.make_messages())
obj.add_user("Lance", 100, email='xxxx@gmail.com')
obj.add_user("john", 80, email='xxxxx@usc.edu')
# obj.add_user("SeXy", 60)
# obj.add_user("PaUl", 50)
# obj.add_user("ViVIan", 87.66663)
print(obj.get_details())

obj.send_email()