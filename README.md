League Helper
===============
<p>Be able to access data about your League of Legends account, through League's API, which returns a JSON based on the type of request. The code then parses the data and gets you the information you want based on the function that is ran.</p>

Summoner Class :
---------------
<p>Everything is currently done under the Summoner Class, where you generate an instance using your in-game username(IGN) and a valid api_key. From that point you can call upon class functions to get what you want.</p>
<p>The __init__ of the Summoner class generates a json when you just request with the summoner IGN and gets basic information about your account and saves it as class variables, such as Summoner Level, Account ID, Encrypted Account ID, Champion Data, Ranked Data. </p>

self.champ(self, func=None, x=5):
---------------
<p><strong>get_chest:</strong> Returns a string saying which champions you can play to earn a Hextech Chest(in-game rewards).</p>
<p><strong>topX:</strong> Takes a parameter x, x being the number of champions you want returned. It then returns your x-top played champions based on data which says how many points are earned for each champ.</p>
<p><strong>masteryup:</strong> For each mastery level, it will return a champion in that mastery level which is the closest to reaching the next level.</p>

self.ranked(self, func=None, queuetype='solo'):
---------------
<p><strong>winr8:</strong> Based on the queuetype, it will return the winrate as a percent and the amount of games played.</p>
<p><strong>rank:</strong> Based on queuetype, it will return the rank you are in that queue.</p>
<p><strong>other:</strong> Based on queuetype, returns additional info, e.g. whether or not you are a veteran in the queue, inactive in play, on a winstreak, or new to the rank you are in.</p>

self.freeweek(self):
---------------
Returns the champions that are free to play and tells you how many days there are until the next rotation comes out.
