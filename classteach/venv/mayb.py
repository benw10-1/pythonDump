import requests, random, string
i=0;

file1 = open("names.txt", "r")
names = file1.readlines()
file2 = open("emails.txt", "w")
file2.write("\n")
while True:
	#This is the link where the form data is posted. It is simple the formlink + '/formResponse'
	url = 'https://mail.protonmail.com/create/new?language=en'
	username = names[random.choice(range(0,1000))].strip()+''.join(random.choice(string.hexdigits) for i in range(7))
	password = ''.join(random.choice(string.digits) for i in range(10))
	form_data = {
        #so why u want promo
		'username'	:	username,
        #you realise blah
		'password'	:	password,

		'passwordc' :   password

		}
	user_agent ={
		'Referer':'google.com',
		'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
		}
	r = requests.post(url, data=form_data, headers=user_agent)

	file2.writelines(username + ":"+password+"\n")
	print(username + ":" + password)
	i=i+1
	if(i%3==0):
		print(r)
		print('\nTotal Count = ')
		print(i)
		print('\n')
