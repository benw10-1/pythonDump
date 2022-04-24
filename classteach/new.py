import requests, random
i=0;
responsearray = ["bruh", "nigga", "nigger", "penis"]
while True:
	#This is the link where the form data is posted. It is simple the formlink + '/formResponse'
	url = 'https://docs.google.com/forms/d/e/1FAIpQLScjDDsQ6clHXW-CzM4CE0pZJOBaRNlPEc3-S-5VlyXPKTngjQ/formResponse'

	form_data = {
        #so why u want promo
		'entry.366340186'	:	responsearray[random.choice(range(0,4))],
        #you realise blah
		'entry.205173177'	:	responsearray[random.choice(range(0,4))],
        #if you do soemthing
		'entry.1042024739'	:	responsearray[random.choice(range(0,4))],
        #req for admin promo
		'entry.1609119854'	:	'Nothing... let the problem sort it\'s self out.',
        #req for lowest
		'entry.1658586357'	:	responsearray[random.choice(range(0,4))],
        #if your
		'entry.856624116'	:	'yes.',
        #name
		'entry.1685866332'	:	responsearray[random.choice(range(0,4))] + responsearray[random.choice(range(0,4))],

		}
	user_agent ={
		'Referer':'https://docs.google.com/forms/d/e/1FAIpQLScEm6OKcAEuso9P955IlaohxmjrcN8dFXTgwRrhU20GXiTlZw/viewform',
		'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
		}
	r = requests.post(url, data=form_data, headers=user_agent)
	i=i+1
	if(i%3==0):
		print(r)
		print('\nTotal Count = ')
		print(i)
		print('\n')


