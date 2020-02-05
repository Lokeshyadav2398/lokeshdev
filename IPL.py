import random
semi_final_teams = []
def sort_teams(tdata):
	return tdata[1]
def num_of_teams(n):
	matches = []
	count_teams = []
	teams = ["team"+str(i) for i in range(1,n+1)]
	print(teams)
	print("")
	for x in range(0,len(teams)):
		team1 = teams[x]
		for y in range(x+1,len(teams)):
			team2 = teams[y]
			matches.append((team1,team2))
	double = matches*2
	#print(double)
	for points in double:
		ran = random.randint(1,2) 
		rand_points = f"{points} : {points[ran-1]}"
		#print(rand_points)
		wteams = f"{points[ran-1]}"
		#print(wteams)
		count_teams.append(wteams)
	#print(count_teams)
	team_points = {}
	d = 0
	for i in range(1,n+1):
		data = f"team{str(i)}"
		team_points[data]= d
	#print(team_points)
	#print(count_teams)
	for i in count_teams:
		if i in team_points:
			team_points[i]+= 2
	print(f"LEAGUE_MATCHES_WITH_POINTS:{team_points}")
	print("")
	a = sorted(team_points.items(),key = lambda x:x[1])
	print(f"AFTER SORTING:{a}")
	print("")
	for semis in a[4:]:
		semi_final_teams.append(semis[0])
	playoffs = semi_final_teams
	print(f"PLAYOFF_TEAMS:{playoffs}")
	print("")
	
	
	top_two = tuple(playoffs[2:])
	a = random.randint(1,2)
	final_list = []
	final_team1 = f"{top_two[a-1]}"
	final_list.append(f"{final_team1}")
	print(f"playoff1:{top_two}")
	print(f"playoff1_winner:{final_team1}")
	print("")
	playoffs3 = []
	if final_team1 in top_two[0]:
		playoffs3.append(top_two[1])
	else:
		playoffs3.append(top_two[0])
	#print(playoffs3)
	
	last_two = tuple(playoffs[0:2])
	b = random.randint(1,2)
	last_team2 = f"{last_two[b-1]}"
	print(f"playoff2:{last_two}")
	print(f"playoff2_winner:{last_team2}")
	print("")
	playoffs3.append(f"{last_team2}")
	print(f"playoff3:{playoffs3}")
	
	eliminator = tuple(playoffs3[0:])
	c = random.randint(1,2)
	final_team2 = f"{eliminator[c-1]}"
	print(f"playoff3_winner:{final_team2}")
	print("")
	final_list.append(f"{final_team2}")
	print(f"final_teams:{final_list}") 
	
	final_match = ((final_team1,final_team2))
	#print(final_match)
	team = random.randint(1,2)
	ipl_winner = f"{final_match[team-1]}"
	print(f"IPL WINNER:{ipl_winner}")
	
	
def main():
	n = 8
	num_of_teams(n)
	
	
if(__name__=="__main__"):
	main()