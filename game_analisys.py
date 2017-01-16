class game_Analisys(object):


	def __init__(self):
		self.home_team=[]
		self.away_team=[]

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

	def set_team_names(self,ahome_team,aaway_team):
		self.home_team.append(ahome_team)
		self.away_team.append(aaway_team)
