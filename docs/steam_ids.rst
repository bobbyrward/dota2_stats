.. Steam IDs

Steam IDs
===================================================================

The Dota2 API generally gives you people's SteamIDs as 32-bit numbers.

In order to convert from these 32-bit numbers to Steam Names, you must first convert between the 32-bit ID and 64-bit ID:

On a system that supports up to 64-bit numbers you can do the following:
    * STEAMID64 - 76561197960265728 = STEAMID32
    * STEAMID32 + 76561197960265728 = STEAMID64
OR
    * STEAMID32 = The right-most 32-bits of STEAMID64
    * STEAMID64 = concatenate("00000001000100000000000000000001", STEAMID32);

On a system that only supports up to 32-bit numbers - it's trickier. You have to rely on the language's built-in "big number" functions (i.e. PHP's gmp extension: see this post for details)

Once you have the 64-bit ID, then you can use the GetPlayerSummaries call to get their detail!


How to get someone's 64-bit ID to search with:

If you have their vanity URL, it should look like this:
Code:

http://steamcommunity.com/id/<vanity_name>/

Using ResolveVanityURL (see http://wiki.teamfortress.com/wiki/We...solveVanityURL for more info), you can get the 64-bit ID as follows:
[CODE]http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=<key>&vanityurl=<vanity_name>[CODE]

If you have an ID url:
Code:

http://steamcommunity.com/profiles/<id>/

Then the <id> is their 64-bit ID and you're done!

If you have just a Steam-Name:
You can use this to search the Dota2 API directly using the player_name option of GetMatchHistory
You can then find their 32-bit ID in the list and then convert it to a 64-bit ID as above.




