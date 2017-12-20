import csv

# import CSV data and save to a dictionary

def csv_to_dictionary(csv_file):

  with open(csv_file, newline='') as players_csv:
    player_reader = csv.reader(players_csv)
    players_list = list(player_reader) # list of lists
    players_list.pop(0) # remove description line 
    
    '''players_list conatins each player is a list with this information order:
    Name = player[0]
    Height (in inches) = player[1]
    Experience = player[2]
    Guardian name(s) = player[3]'''
  
    # create a dicitionary of players
    # the script assumes that there are no players with the same name
    player_dic = {}
    for player in players_list:
      player_information = [player[1], player[2], player[3]] # value for key:value pair of player data
      player_dic[player[0]] = player_information
    
    return player_dic


# sort players into three teams
# save teams to a text file


















if __name__ == "__main__":
    print(csv_to_dictionary("soccer_players.csv"))
