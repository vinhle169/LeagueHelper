import requests
import html
import json
import ast
import datetime
import string

#Overhaul rank data to include flex and tft
today = datetime.date.today()
print(today)
uppercase = string.ascii_letters
with open("./id2champ.txt","r") as c:
	champdata=ast.literal_eval(c.read())
api_key = "RGAPI-d0403c28-04bd-42c4-8ae2-4c010e75e29a"
#UPDATE APIKEY
def generate_json(url):
	req = requests.get(url)
	return req.json()
class Summoner():
	def __init__(self,summonerName,api_key):
		### import json of summoner info
		self.ign,self.key = summonerName,api_key
		i=f"https://na1.api.riotgames.com//lol/summoner/v4/summoners/by-name/{self.ign}?api_key={self.key}"
		self.summonerjson = generate_json(i)
		#print(summonerdata)
		### save some important variables
		self.lvl = self.summonerjson['summonerLevel']
		self.accID = self.summonerjson['accountId']
		self.encryptedID = self.summonerjson['id']
		print(self.encryptedID,"e-id")
		### import json of summoners champion data
		j = f"https://na1.api.riotgames.com//lol/champion-mastery/v4/champion-masteries/by-summoner/{self.encryptedID}?api_key={self.key}"
		self.champjson = generate_json(j)
		print(f"Profile for {self.ign} created.")
	def update_key(self,newkey):
		self.key = newkey
	def champ(self, func=None, x=5):	
		def get_chest(self):
			print(self.champjson)
			self.chestable = []
			for c in self.champjson:
				if c['chestGranted']!=True:
					self.chestable.append(champdata[str(c['championId'])])
			return self.ign+" can get a chest by playing as: " + ', '.join(self.chestable)
		###
		def topX(self,x):
			result = f"{self.ign}'s most played champions are:\n"
			for i in range(x):
				key = (self.champjson[i]['championId'])
				name = champdata[str(key)]
				points = self.champjson[i]['championPoints']
				masterylevel = self.champjson[i]['championLevel']
				result+=f"{i+1}) {name}: Mastery Level {masterylevel}, with {points} mastery points\n"
			return result
		###
		def masteryup(self):
			lvl = {1:[],2:[],3:[],4:[],5:[],6:[]}
			#print(self.champjson)
			toreturn=""
			smallest=[]
			small=[0,9999]
			for c in self.champjson:
				if c['championLevel']!=7: lvl[c['championLevel']].append([champdata[str(c['championId'])],c['championPointsUntilNextLevel'],c['championId'],c['tokensEarned']])
			for j in list(lvl.keys()):
				big=[-1]*4
				if j==5 or j==6:
					for i in lvl[j]:
						if i[3]>big[3]: big=i
					smallest.append(big)
					continue
				for i in lvl[j]:
					if i[1]<small[1]: small=i
				smallest.append(small)
				small=[0,9999]
			for i in range(6):
				if i<=3:
					toreturn+=f"The Mastery Level {i+1} champion closest to leveling up is {smallest[i][0]}. You need to get {smallest[i][1]} more mastery points.\n"
				else:
					if i==4: toreturn+=f"The Mastery Level {i+1} champion closest to leveling up is {smallest[i][0]}. You need {2-smallest[i][3]} more tokens.\n"
					else: toreturn+=f"The Mastery Level {i+1} champion closest to leveling up is {smallest[i][0]}. You need {3-smallest[i][3]} more tokens.\n"

			return toreturn+"You can earn about 500 points per game, Mastery 6 tokens are earned with at least an S-, Mastery 7 with at least an S."
		if func == "get_chest": return get_chest(self)
		elif func == "topX": return topX(self,x)
		elif func =="masteryup": return masteryup(self)
		else: return None 


	def rankdata(self,func=None):
		def winr8(self):
			numgames=self.rankdata['wins']+self.rankdata['losses']
			return str(self.winrate)+f"% in {numgames} games."
		def rank(self):
			return self.rank
		def other(self):
			returnstring = f"Veteran: {self.rankdata['veteran']} ||| Inactive: {self.rankdata['inactive']} ||| Just Arrived: {self.rankdata['freshBlood']} ||| Winstreak: {self.rankdata['hotStreak']}"
			return returnstring
		i = f'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{self.encryptedID}?api_key={self.key}'
		self.rankdata = (generate_json(i))[0]
		print(self.rankdata)
		#print(self.rankdata)
		que=self.rankdata['queueType']
		queuetype = que.replace('_',' ')
		self.winrate = round(self.rankdata['wins']*100/(self.rankdata['wins']+self.rankdata['losses']),2)
		self.rank = f"{(self.rankdata['tier']).title()} {self.rankdata['rank']} {self.rankdata['leaguePoints']} lp"
		if func == 'winr8':
			return winr8(self)
		elif func == 'rank':
			return rank(self)
		elif func == 'other':
			return other(self)
		else:
			rank = f"{self.ign} is {(self.rankdata['tier']).title()} {self.rankdata['rank']} in {queuetype.title()}"
			return rank	

	def freeweek(self):
		i = f"https://na1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={self.key}"
		self.freerotdata = generate_json(i)
		daysuntiltuesday = (1-today.weekday())%7
		if daysuntiltuesday==0: daysuntiltuesday = 7
		daysuntiltuesday = f"\nThere are {daysuntiltuesday} more days until a new rotation."
		if self.lvl>10:
			rotation = self.freerotdata['freeChampionIds']
			champrot = [champdata[str(i)] for i in rotation]
			return "These are the champions that are free to play this week: "+', '.join(champrot)+"."+daysuntiltuesday
		else:
			rotation = self.freerotdata['freeChampionIdsForNewPlayers']
			champrot = [champdata[str(i)] for i in rotation]
			return "These are the champions that are free to play this week: "+', '.join(champrot)+"."+daysuntiltuesday
Vinh = Summoner("Vinhabust",api_key)
#print(Vinh.champ("get_chest"))
print(Vinh.champ())
#print(Vinh.get_chest())
#print(Vinh.freeweek())
print(Vinh.rankdata())


