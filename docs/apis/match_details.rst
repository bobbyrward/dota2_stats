.. Match Details

Match Details
===================================================================

GetMatchDetails
Used to get detailed information about a specified match.

Available options:
Code:

match_id=<id> # the match's ID

Examples:
To get the details for match with ID "XXXXX":
Code:

https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?key=<key>&match_id=XXXXX

Result Field Format:

* players - an array of players:
    * account_id - the player's 32-bit Steam ID
    * player_slot - an 8-bit unsigned int: if the left-most bit is set, the player was on dire. the two right-most bits represent the player slot (0-4)
    * hero_id - the numeric ID of the hero that the player used
    * item_0 - the numeric ID of the item that player had in their top-left slot
    * item_1 - the numeric ID of the item that player had in their top-center slot
    * item_2 - the numeric ID of the item that player had in their top-right slot
    * item_3 - the numeric ID of the item that player had in their bottom-left slot
    * item_4 - the numeric ID of the item that player had in their bottom-center slot
    * item_5 - the numeric ID of the item that player had in their bottom-right slot
    * kills - the number of kills the player got
    * deaths - the number of times the player died
    * assists - the number of assists the player got
    * leaver_status - 0 if the player stayed in the match
    * gold - the amount of gold the player had left at the end of the match
    * last_hits - the number of times a player last-hit a creep
    * denies - the number of times a player denied a creep
    * gold_per_min - the player's total gold/min
    * xp_per_min - the player's total xp/min
    * gold_spent - the total amount of gold the player spent over the entire match
    * hero_damage - the amount of damage the player dealt to heroes
    * tower_damage - the amount of damage the player dealt to towers
    * hero_healing - the amount of damage the player healed
    * level - the player's final level
* season - ????????
* radiant_win - true if radiant won, false otherwise
* duration - the total time in seconds the match ran for
* starttime - date in UTC seconds since Jan 1, 1970 (unix time format)
* match_id - the numeric match ID
* tower_status_radiant - an 11-bit unsinged int: see THIS THREAD
* tower_status_dire - an 11-bit unsinged int: see THIS THREAD
* barracks_status_radiant - a 6-bit unsinged int: see THIS THREAD
* barracks_status_radiant - a 6-bit unsinged int: see THIS THREAD
* cluster - see REPLAYS below
* first_blood_time - the total time in seconds at which first blood occurred
* replay_salt - see REPLAYS below
* lobby_type - the type of lobby (0 for human matchmaking, 1 for co-op bot)
* human_players - the number of human players in the match
* leagueid - the leauge this match is from (see GetMatchHistory above)
* positive_votes - the number of thumbs up the game has received
* positive_votes - the number of thumbs up the game has received



To retrieve the specific details of a match, use this API:

Code:

https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?match_id=27110133&key=<key>


