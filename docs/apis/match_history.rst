.. Match History

Match History
===================================================================

Used to get a list of matches played::
    https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key=<key>

Available options:

* player_name=<name>		# Search matches with a player name, exact match only 
* hero_id=<id>			# Search for matches with a specific hero being played (hero ID, not name)
* skill=<skill>			# 0 for any, 1 for normal, 2 for high, 3 for very high skill (default is 0)
* date_min=<date>			# date in UTC seconds since Jan 1, 1970 (unix time format) 
* date_max=<date>			# date in UTC seconds since Jan 1, 1970 (unix time format)
* account_id=<id>			# A user's 32-bit steam ID
* league_id=<id>			# matches for a particular league
* start_at_match_id=<id> 		# Start the search at the indicated match id, descending
* matches_requested=<n> 		# Maximum is 25 matches (default is 25)

Examples:
-------------------------------------------------------------------
To get the latest 25 matches played by person with 32-bit ID "XXXXX"::
    https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key=<key>&account_id=XXXXX

To get the latest single match::
    https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key=<key>&matches_requested=1

Note, in order to go to the "next page" of results you need to do one of two things:

* Use the match_id of the last match returned by the query, and then use it as the start_at_match_id::
    https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key=<key>&start_at_match_id=<id>&<OTHER_OPTIONS>
* Use the starttime of the last match returned by the query, and ten use it as the date_max::
    https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key=<key>&date_max=<id>&<OTHER_OPTIONS>

Result Field Format:

* num_results - the number of results contained in this response
* total_results - the total number of results for this particular query [(total_results / num_results) = total_num_pages]
* results_remaining - the number of results left for this query [(results_remaining / num_results) = remaining_num_pages]
* matches - an array of num_results matches:
    * match_id - the numeric match ID
    * start_time - date in UTC seconds since Jan 1, 1970 (unix time format)
    * lobby_type - the type of lobby (0 for human matchmaking, 1 for co-op bot)
    * players - an array of players:
        * account_id - the player's 32-bit Steam ID
        * player_slot - an 8-bit number: if the left-most bit is set, the player was on dire. the two right-most bits represent the player slot (0-4)
        * hero_id - the numeric ID of the hero that the player used

Match History

A WebAPI for match history is now available on Dota 2. Web developers can now retrieve the match history and match details in JSON or XML format for use in their own applications.

First off get a dev key from here, http://steamcommunity.com/dev/apikey and login with your Steam account and you will get unique key. Please do not share this key as it identifies you when you make WebAPI requests.

There are two API calls for Dota 2's match history:

Retrieving match history:

Code:

https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key=<key>

Replace "<key>" with your personal WebAPI key. That call will return the latest 25 public matches in JSON format. You can request it in XML format
using:
Code:

https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?format=XML&key=<key>

A maximum of 25 matches are returned. To request the next 25, use the param "start_at_match_id" with one less than the last match number you received:

Code:

https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?start_at_match_id=27110133&key=<key>


The following additional parameters are available on GetMatchHistory:

Code:

player_name=<name> # Search matches with a player name, exact match only
hero_id=<id> # Search for matches with a specific hero being played, hero id's are in dota/scripts/npc/npc_heroes.txt in your Dota install directory
skill=<skill>  # 0 for any, 1 for normal, 2 for high, 3 for very high skill
date_min=<date> # date in UTC seconds since Jan 1, 1970 (unix time format)
date_max=<date> # date in UTC seconds since Jan 1, 1970 (unix time format)
account_id=<id> # Steam account id (this is not SteamID, its only the account number portion)
league_id=<id> # matches for a particular league
start_at_match_id=<id> # Start the search at the indicated match id, descending
matches_requested=<n> # Defaults is 25 matches, this can limit to less

For example, to retrieve the latest single match:

Code:

https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?matches_requested=1&key=<key>

Please explore this functionality. We can’t wait to see what people come up with using this information.

Please do be nice and not slam the WebAPI’s too heavily, however! Thanks!


