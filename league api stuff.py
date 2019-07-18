import requests
import html
import json
#p = f"https://na1.api.riotgames.com//lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}?api_key=RGAPI-5076519d-5d50-4e91-aa45-56d9c1573eb4"
#reqs = requests.get(p)
#champion_mastery = reqs.json()
#print(champion_mastery)
class Summoner():
	def __init__(self,summonerName,api_key):
		self.ign,self.key = summonerName,api_key
		i=f"https://na1.api.riotgames.com//lol/summoner/v4/summoners/by-name/{self.ign}?api_key={self.key}"
		req = requests.get(i)
		summonerdata = req.json()
		self.accID = summonerdata['accountId']
		self.encryptedID = summonerdata['id']
		#print(self.accID)
		#print(self.encryptedID)
	def update_key(self,newkey):
		self.key = newkey
	def mastery(self):
		i = f"https://na1.api.riotgames.com//lol/champion-mastery/v4/champion-masteries/by-summoner/{self.encryptedID}?api_key={self.key}"
		reqs = requests.get(i)
		champion_mastery = reqs.json()
summonerName = "VinhaBust"
api_key ="RGAPI-5076519d-5d50-4e91-aa45-56d9c1573eb4"
Vinh = Summoner(summonerName,api_key)
def getJSON(filePathAndName):
	dict={}
	with open(filePathAndName, encoding="utf8") as fp:
		data = json.load(fp)
		for i in data['data']:
			#print(i,data['data'][i]['key'])
			dict[data['data'][i]['key']]=i
	return dict
print(getJSON('./champinfo.json'))