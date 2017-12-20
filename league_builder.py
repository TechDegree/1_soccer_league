import csv

# import CSV data and save to a dictionary

def csv_to_list_of_dicts(csv_file):

    with open(csv_file, newline='') as players_csv:
        player_reader = csv.reader(players_csv)
        players_list = list(player_reader) # list of lists
        players_list.pop(0) # remove description line 
        
        '''players_list conatins each player is a list with this information order:
        Name = player[0]
        Height (in inches) = player[1]
        Experience = player[2]
        Guardian name(s) = player[3]'''
    
    # create a list with each player as dicitionary
    list_player_dic = []
    for player in players_list:
        name, height, experience, guardian_names = player
        one_player_dict = {"name" : name,
                           "height" : height, 
	                       "experience" : experience,
		                   "guardian_names" : guardian_names}
        list_player_dic.append(one_player_dict)

    return list_player_dic


# sort players into three teams
# save teams to a text file


















if __name__ == "__main__":
    print(csv_to_dictionary("soccer_players.csv"))
