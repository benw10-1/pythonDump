import requests, random

i=0

url = 'https://docs.google.com/forms/d/e/1FAIpQLScCuulrjWT7sHPFS3447eiSCG8RO3R9GRidwUW8D3-OIBssoA/formResponse'

responsearray = ["Right", "Left"]

def choose():
	num = random.randint(0,152)
	if num > 35:
		return "Left"
	return "Right"

while i < 100:
	form_data = {"entry.2100771746" :   "I consent to be a part of this experiment",
				 'entry.1502617477'	:	choose(),
				 'entry.1158618060'	:	choose(),
				 'entry.152454226'	:	choose(),
				 'entry.1721566939'	:	choose()}
	user_agent ={
		'Referer':url,
		'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
		}
	r = requests.post(url, data=form_data, headers=user_agent)
	i=i+1
	if(i%3==0):
		print(r)
		print('\nTotal Count = ')
		print(i)
		print('\n')


