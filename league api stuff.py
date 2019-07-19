import requests
import html
import json
import ast
import datetime
#p = f"https://na1.api.riotgames.com//lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}?api_key=RGAPI-5076519d-5d50-4e91-aa45-56d9c1573eb4"
#reqs = requests.get(p)
#champion_mastery = reqs.json()
#print(champion_mastery)
with open("./id2champ.txt","r") as c:
	champdata=ast.literal_eval(c.read())
#add mastery level to top5 and add rank data and dont forget to update apikey
class Summoner():
	def __init__(self,summonerName,api_key):
		self.ign,self.key = summonerName,api_key
		i=f"https://na1.api.riotgames.com//lol/summoner/v4/summoners/by-name/{self.ign}?api_key={self.key}"
		req = requests.get(i)
		summonerdata = req.json()
		self.lvl = summonerdata['summonerLevel']
		self.accID = summonerdata['accountId']
		self.encryptedID = summonerdata['id']
		#print(self.accID)
		#print(self.encryptedID)
	def update_key(self,newkey):
		self.key = newkey
	def top5(self):
		result = f"{self.ign}'s most played champions are:\n"
		i = f"https://na1.api.riotgames.com//lol/champion-mastery/v4/champion-masteries/by-summoner/{self.encryptedID}?api_key={self.key}"
		req = requests.get(i)
		self.champsplayed = req.json()
		#print(champion_mastery)
		for i in range(5):
			key = (self.champsplayed[i]['championId'])
			name = champdata[str(key)]
			points = self.champsplayed[i]['championPoints']
			masterylevel = self.champsplayed[i]['championLevel']
			result+=f"{i+1}) {name}: Mastery Level {masterylevel}, with {points} mastery points\n"
		return result
	def freeweek(self):
		i = f"https://na1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={self.key}"
		req = requests.get(i)
		self.freerotdata = req.json()
		if self.lvl>10:
			rotation = self.freerotdata['freeChampionIds']
			champrot = [champdata[str(i)] for i in rotation]
			return "These are the champions that are free to play this week: "+', '.join(champrot)
		else:
			rotation = self.freerotdata['freeChampionIdsForNewPlayers']
api_key ="RGAPI-69cb14ee-6af8-4a2f-91b0-90d630889575"
Vinh = Summoner("Vinhabust",api_key)
print(Vinh.top5())
print(Vinh.freeweek())
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