import requests
import html
import json
import ast
import datetime
import string
#p = f"https://na1.api.riotgames.com//lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}?api_key=RGAPI-5076519d-5d50-4e91-aa45-56d9c1573eb4"
#reqs = requests.get(p)
#champion_mastery = reqs.json()
#print(champion_mastery)
today = datetime.date.today()
print(today)
uppercase = string.ascii_letters
with open("./id2champ.txt","r") as c:
	champdata=ast.literal_eval(c.read())
#UPDATE APIKEY
class Summoner():
	def __init__(self,summonerName,api_key):
		self.ign,self.key = summonerName,api_key
		i=f"https://na1.api.riotgames.com//lol/summoner/v4/summoners/by-name/{self.ign}?api_key={self.key}"
		req = requests.get(i)
		summonerdata = req.json()
		#print(summonerdata)
		self.lvl = summonerdata['summonerLevel']
		self.accID = summonerdata['accountId']
		self.encryptedID = summonerdata['id']
	def update_key(self,newkey):
		self.key = newkey
	def top5(self):
		result = f"{self.ign}'s most played champions are:\n"
		i = f"https://na1.api.riotgames.com//lol/champion-mastery/v4/champion-masteries/by-summoner/{self.encryptedID}?api_key={self.key}"
		req = requests.get(i)
		self.champsplayed = req.json()
		#print(champion_mastery)
		for i in range(8):
			key = (self.champsplayed[i]['championId'])
			name = champdata[str(key)]
			points = self.champsplayed[i]['championPoints']
			masterylevel = self.champsplayed[i]['championLevel']
			result+=f"{i+1}) {name}: Mastery Level {masterylevel}, with {points} mastery points\n"
		return result
	def rankdata(self):
		i = f'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{self.encryptedID}?api_key={self.key}'
		req = requests.get(i)
		self.rankdata = (req.json())[0]
		print(self.rankdata)
		que=self.rankdata['queueType']
		queuetype = que.replace('_',' ')
		self.winrate = self.rankdata['wins']/(self.rankdata['wins']+self.rankdata['losses'])
		self.rank = f"{(self.rankdata['tier']).title()} {self.rankdata['rank']}"
		rank = f"{self.ign} is {(self.rankdata['tier']).title()} {self.rankdata['rank']} in {queuetype.title()}"
		return rank
	def freeweek(self):
		i = f"https://na1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={self.key}"
		req = requests.get(i)
		self.freerotdata = req.json()
		if self.lvl>10:
			rotation = self.freerotdata['freeChampionIds']
			champrot = [champdata[str(i)] for i in rotation]
			return "These are the champions that are free to play this week: "+', '.join(champrot)+"."
		else:
			rotation = self.freerotdata['freeChampionIdsForNewPlayers']
			champrot = [champdata[str(i)] for i in rotation]
			return "These are the champions that are free to play this week: "+', '.join(champrot)+"."
api_key ="RGAPI-69cb14ee-6af8-4a2f-91b0-90d630889575"
Vinh = Summoner("Vinhabust",api_key)
print(Vinh.top5())
Vinh.rankdata()
print(Vinh.winrate)
yohan = Summoner("Y0H0N3Y",api_key)
print(yohan.top5())
'''
Nolan = Summoner("nowin REE",api_key)
print(Nolan.mastery())

Carl = Summoner("ReaperDreams",api_key)
print(Carl.mastery())

KevinN = Summoner("Kaeeede",api_key)
print(KevinN.mastery())

Sushi = Summoner("DUCK FONALD",api_key)
print(Sushi.mastery())

Manny = Summoner("Manny810",api_key)
print(Manny.mastery())
'''