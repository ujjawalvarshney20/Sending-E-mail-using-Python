import yagmail

sender_email = 'sender@gmail.com'
receiver_email = 'receiver@gmail.com'

subject = "Check THIS out"

sender_password = input(f'Please, enter the password for {sender_email}:\n')

yag = yagmail.SMTP(user=sender_email, password=sender_password)

contents = [
  "Hello My name is Ujjawal Varshney.",
  'C:\\Python\\practice\\college.jpg'

]

yag.send(to=receiver_email, subject=subject, contents=contents)