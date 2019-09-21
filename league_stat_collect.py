import requests
import html
import json
import ast
import datetime
import string

today = datetime.date.today()
print(today)
uppercase = string.ascii_letters
with open("./id2champ.txt","r") as c:
	champdata=ast.literal_eval(c.read())
api_key = "RGAPI-e188023e-20c7-4c6b-b536-bb3f594acb2b"
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
		#print(self.encryptedID,"e-id")
		### import json of summoners champion data
		j = f"https://na1.api.riotgames.com//lol/champion-mastery/v4/champion-masteries/by-summoner/{self.encryptedID}?api_key={self.key}"
		self.champjson = generate_json(j)
		print(f"Profile for {self.ign} created.")
		k = f'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{self.encryptedID}?api_key={self.key}'
		self.rankdata = generate_json(k)
		#print(self.rankdata)
	def whatfunctions(self):
		return {"champ":{'get_chest':'shows what champions you can get a chest from','topX':'displays input X number of top champions based on mastery', 'masteryup':'shows which champions from each mastery level are closest to leveling up'},'ranked':{'winr8':'winrate in the queue you selected','rank':'displays rank','other':'other stats'},'freeweek':'displays what champions are free to play this week'}


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
			print(self.champjson)
			### if i want to find stuff for a certain champ
			#for i in self.champjson:
			#	if champdata[str(i['championId'])]=="LeeSin":
			#		print(i)
			###
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



	def ranked(self,func=None,queuetype='solo'):
		def winr8(self):
			wr = round(rankdata['wins']*100/(rankdata['losses']+rankdata['wins']),2)
			return f"Your winrate in {queue} is {wr}% in {rankdata['wins']+rankdata['losses']}."
		def rank(self):
			rnk = f"{rankdata['tier'].title()} {rankdata['rank']} {rankdata['leaguePoints']} lp."
			return f"In {queue} you are {rnk}"
		def other(self):
			return f"Veteran: {rankdata['veteran']}\nInactive: {rankdata['inactive']}\nWinstreak: {rankdata['hotStreak']}\nFreshblood: {rankdata['freshBlood']}"
		for i in self.rankdata:
			if queuetype.upper() in i['queueType']: rankdata = i
		queue = rankdata['queueType'].replace('_',' ').title().replace("Sr","SR").replace("Tft","TFT")
		if func == 'winr8':
			return winr8(self)
		elif func == 'rank':
			return rank(self)
		elif func == 'other':
			return other(self)
		else:
			return rankdata


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
print(Vinh.ranked('winr8','solo'))


