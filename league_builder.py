import csv
import random

# import CSV data and save to a dictionary
def csv_to_list_of_dicts(csv_file):

    with open(csv_file, newline='') as players_csv:
        player_reader = csv.reader(players_csv)
        players_list = list(player_reader) # list of lists
        players_list.pop(0) # remove description line 
        
        # players_list conatins each player is a list with this information order:
        # Name = player[0]
        # Height (in inches) = player[1]
        # Experience = player[2]
        # Guardian name(s) = player[3]
    
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


def player_to_string(player_dic):
    # changes player into a string that can be saved to a text file
    # uses only the data required in instructions
    player_string = "{}, {}, {}". format(
        player_dic["name"], 
        player_dic["experience"], 
        player_dic["guardian_names"]        
    )
    return player_string

# save teams to a text file
def save_to_file(file_name, teams_dic):
    # open file, with possible re-write, and creation if not there
    with open(file_name, "w") as file:

        for team_name, players in teams_dic.items():
            file.write(team_name + '\n') # save team name first
            # iterate over all players assigned to the team
            for player in players: 
                player_string = player_to_string(player)
                file.write(player_string + "\n")            
            file.write("\n") # add a new line after each team

def create_letter(player, team, start_hour="10:00 AM",
                  start_date="Tuesday, March 7",
                  location="Thorns Boys and Girls Club",
                  season_year="2018", 
                  head_coach="Michelle Gibregh"):
    # create name for the letter text file
    file_name = player["name"].lower().replace(" ", "_") + ".txt"
    letter_string = """Dear {}, \n
We would like to welcome {} to the {}. Our first practice will be at {} on {} at {}.
We are looking forward to having {} with us, and hope to celebrate a successful {} season together.\n
Best Regards,
{}
{}, Head Coach"""
    player_full_name = player["name"]
    player_first_name = player_full_name.split()[0] # split on space, take first name
    
    letter_text = letter_string.format(
        player["guardian_names"],
        player_full_name,
        team,
        start_hour,
        start_date,
        location,
        player_first_name,
        season_year,
        team,
        head_coach)

    # save data to file
    with open(file_name, "w") as file:
        file.write(letter_text)
        



def main():
    PLAYER_DATA = "soccer_players.csv"
    TEAMS_NAMES = {"Sharks": ["10:00 AM", "Monday, March 6", "Green Dragon Venue", "2018", "Juliana Yandar"],
                   "Dragons": ["11:20 AM", "Thursday, March 9", "Yellow Boats United", "2018", "Alina Marakash"],
                   "Raptors": ["09:15 AM", "Wednesday, March 2", "Orange Monsters University", "2018", "Dima Kailar"]
    }

    TEAMS_DATA = "teams.txt"
    TEAMS = {}
    
    # read and convert players data to pythonic format (list of dicts)
    list_of_players = csv_to_list_of_dicts(PLAYER_DATA)
    
    # sort players to two list of ex and inex using tuple unpacking 
    experience_tuple = experiance_level_lists(list_of_players)
    experienced_players, inexperienced_players = experience_tuple

    # shuffle each list and assign appropriate amount of players to each team:
    # the number of players has to be so to make equal number of players per team 
    # the number can be changed to anything, as long as the above constraint stays    
    team_number = len(TEAMS_NAMES)
    players_num = len(list_of_players)
    players_per_team = players_num / team_number

    # shuffle players in (in)experience level lists
    # random.shuffle() shuffles in place, returns None
    random.shuffle(experienced_players)
    random.shuffle(inexperienced_players)

    # organize players into teams
    for team_name, letter_details in TEAMS_NAMES.items():
        players = []

        # number of players that must be taken from each experience level
        players_from_each = players_per_team / len(experience_tuple)

        while players_from_each > 0:
            # remove player from both experience levels 
            # send letters to the players' guardians
            ex_player = experienced_players.pop()
            create_letter(ex_player, team_name, 
                  start_hour=letter_details[0],
                  start_date=letter_details[1],
                  location=letter_details[2],
                  season_year=letter_details[3],
                  head_coach=letter_details[4]
            )

            inex_player = inexperienced_players.pop()
            create_letter(inex_player, team_name, 
                  start_hour=letter_details[0],
                  start_date=letter_details[1],
                  location=letter_details[2],
                  season_year=letter_details[3],
                  head_coach=letter_details[4]
            )


            # and add to players for current team
            players.append(ex_player)
            players.append(inex_player)

            players_from_each -= 1
        
        # add all players to a team in a key:value (team:players) dic
        TEAMS[team_name] = players

    # save teams to a file
    save_to_file(TEAMS_DATA, TEAMS)

    # create letters to guardians of every player






if __name__ == "__main__":
    main()

