class game_Analisys(object):


	def __init__(self):
		self.home_team=[]
		self.away_team=[]
		self.head_to_head=[]
	'''
	we have no way of predicting if the home_team has more points than the away_team
	other than compare the names that come from the self arrays with the names that come in a_list
	a_list[a,13,b,14]
	home_team[a]
	away_team[b]
	'''
	def set_teams_points(self,a_list):
		if self.home_team[0]==a_list[0]:
			self.home_team.append(a_list[1])
			self.away_team.append(a_list[3])
		else:
			self.home_team.append(a_list[3])
			self.away_team.append(a_list[1])

	#	away_team.append(away_team)

	def print_team_stats(self):
		print (self.home_team)
		print (self.away_team)
		print (self.head_to_head)

	def set_team_names(self,ahome_team,aaway_team):
		self.home_team.append(ahome_team)
		self.away_team.append(aaway_team)

	def last_6_matches_percentage_home__team(self,alist):
		self.home_team+=alist

	def last_6_matches_percentage_away__team(self,alist):
		self.away_team+=alist

	def latest_home_matches(self,alist):
		self.home_team+=alist

	def latest_away_matches(self,alist):
		self.away_team+=alist

	def overall_stats_home(self,alist):
		self.home_team+=alist

	def overall_stats_away(self,alist):
		self.away_team+=alist

	def vs(self,alist):
		self.head_to_head+=alist
