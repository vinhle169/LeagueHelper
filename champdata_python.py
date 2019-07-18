def getJSON(filePathAndName):
	dict={}
	with open(filePathAndName, encoding="utf8") as fp:
		data = json.load(fp)
		for i in data['data']:
			#print(i,data['data'][i]['key'])
			dict[data['data'][i]['key']]=i
	return dict
print(getJSON('./champinfo.json'))