import lxml
from lxml import html,etree
import requests

needsemail = False
i=0
p=0
j=0
txtids = []
multids=[]
elements = []
qnames = []
opnames = []
data = {}
url = input("Enter url: ")
page = requests.get(url)
tree = html.fromstring(page.content)
body = list(tree)[1]

for element in body.iter(tag=etree.Element):

    elements.append(element)
    if element.tag == "input":
        if element.get("type") == "text":
            if element.get("type") == "email":
                needsemail=True
            else:
                txtids.append(element.get("name"))

        if element.get("type") == "hidden" and elements[i-2].text != "Submit" and elements[i-1].tag == "span":
            multids.append(element.get("name"))
            p+=1
    if element.tag == "div":
        if element.get("role") == "listitem":
            if element.get("class") == "freebirdFormviewerViewItemsItemItem":
                q = True
            else:
                q = False
    if element.tag == "span":
        if element.get("dir") == "auto":
            #print(str(p)+"."+element.text)
            opnames.append(str(p)+"."+element.text)
    if element.tag == "textarea":
       txtids.append(element.get("name"))
    if element.text == "*":
        if q:
            qnames.append("mult."+elements[i-1].text)
        else:
            if elements[i-1].text.strip().lower() != "email address":
                qnames.append("txt."+elements[i-1].text)
        j+=1

    i+=1

if txtids:
    print(txtids)
#if multids:
#    print(multids)
#if needsemail:
#    print("yes")
#print (qnames)
url = url.replace("/viewForm", "/formResponse")
j=0
t=0
for a in qnames:
    templst = []
    if "txt." in a:

        data[txtids[t]] = input(a.strip("txt.")+": ")
        t+=1
    if "mult." in a:
        i = 1
        for m in opnames:
            if str(t)+"." in m:
                print(m.replace(str(t),str(i)))
                templst.append(m.strip(str(t)))
                j+=1
                i+=1
        while True:
            input1 = input("Choose number: ")
            try:
                data[multids[t]] = templst[int(input1)]
            except ValueError:
                print ("Please enter a number")
                continue
            except Exception as e:
                print("Error "+ str(e))
                continue
            break
print(data)

i=0
url1 = url.replace("viewform", "formResponse")
print(url1)
input("")
while True:
	user_agent ={
		'Referer':url,
		'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
		}
	r = requests.post(url1, data=data, headers=user_agent)
	i=i+1
	print(r)
	print('\nTotal Count = ' +str(i))








