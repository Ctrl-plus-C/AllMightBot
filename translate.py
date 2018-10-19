import requests

def translatefn(sentence):
	key = "key_placeholder"
	text = ' '.join(sentence[1:])
	url = "https://translate.yandex.net/api/v1.5/tr.json/translate?key="+key+"&text="+text+"&lang=en"
	response = requests.get(url)
	val = response.json()['lang'].upper()+", Translation: "
	ans = ' '.join(response.json()['text'])
	return(val+ans)