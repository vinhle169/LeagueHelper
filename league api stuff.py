import requests
import html
summonerName = "VinhaBust"
r = f"https://na1.api.riotgames.com//lol/summoner/v4/summoners/by-name/{summonerName}?api_key=RGAPI-5076519d-5d50-4e91-aa45-56d9c1573eb4"
req = requests.get(r)
summoner =  req.json()
print(summoner)
print('\n'+summoner['name']+"'s level is "+str(summoner['summonerLevel']))
accountID=summoner['accountId']

encryptedSummonerId=summoner['id']
print(encryptedSummonerId)
p = f"https://na1.api.riotgames.com//lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}?api_key=RGAPI-5076519d-5d50-4e91-aa45-56d9c1573eb4"
reqs = requests.get(p)
champion_mastery = reqs.json()
print(champion_mastery)
class Summoner():
	def __init__(self,summonerName):
		#initiate access to player data
