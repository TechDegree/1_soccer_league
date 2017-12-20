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
    
    # create a list with each player as dictionary, making it order independent
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


def player_to_string(player_dic):
    # changes player into a string that can be saved to a text file
    # uses only the data required in instructions
    player_string = "{}, {}, {}". format(
        player_dic["name"], 
        player_dic["experience"], 
        player_dic["guardian_names"]        
    )
    return player_string


def main():
    PLAYER_DATA = "soccer_players.csv"
    TEAMS_NAMES = ["SHARKS", "DRAGONS", "RAPTORS"]
    TEAMS_NAMES = ["Sharks", "Dragons", "Raptors"]
    TEAMS_DATA = "teams.txt"
    TEAMS = {}
    
    # read and convert players data to pythonic format (list of dicts)
    list_of_players = csv_to_list_of_dicts(PLAYER_DATA)
    
    # sort players to two list of ex and inex using tuple unpacking 
    experience_tuple = experiance_level_lists(list_of_players)
    experienced_players, inexperienced_players = experience_tuple

    # shuffle each list and assign appropriate amount of players to each team
    team_number = len(TEAMS_NAMES)
    players_num = len(list_of_players)

    # the number of players has to be so to make equal number of players per team 
    # the number can be changed to anything, as long as the above constraint stays
    players_per_team = players_num / team_number

    # shuffle players in experience level lists
    # random.shuffle() shuffles in place, returns None
    random.shuffle(experienced_players)
    random.shuffle(inexperienced_players)

    # organize playrs
    for team_name in TEAMS_NAMES:
        # number of players that must be taken from each experience level
        players = []
        
        players_from_each = players_per_team / len(experience_tuple)

        while players_from_each > 0:
            # remove player from both experience levels and add to players for 
            # current team
            players.append(experienced_players.pop())    
            players.append(inexperienced_players.pop())    
            players_from_each -= 1
        
        TEAMS[team_name] = players

    print(TEAMS)





if __name__ == "__main__":
    main()

