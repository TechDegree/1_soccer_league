import csv
import random

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
def experiance_level_lists(players):
    # players is a list of dictionaries
    experienced_players = []
    inexperienced_players = []
    
    for player in players:
        if player["experience"] == "YES":
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)
    
    # returns a tuple with both lists
    return (experienced_players, inexperienced_players)

def sort_players(levels_tuple_of_lists):
    pass
# save teams to a text file




def main():
    PLAYER_DATA = "soccer_players.csv"
    TEAMS_NAMES = ["SHARKS", "DRAGONS", "RAPTORS"]
    TEAMS_DATA = "teams.txt"

    # read and convert players data to pythonic format (list of dicts)
    list_of_players = csv_to_list_of_dicts(PLAYER_DATA)
    
    # sort players to two list of ex and inex using tuple unpacking 
    experienced_players, inexperienced_players = experiance_level_lists(list_of_players)

    # shuffle each list and assign appropriate amount of players to each team

    teams = {}
    team_number = len(TEAMS_NAMES)











if __name__ == "__main__":
    main()

