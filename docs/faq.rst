.. FAQ

FAQ
===================================================================

Frequently asked questions about the WebAPI:

How do I get the replay from the information in GetMatchDetails?
Replays are formed from the following URL:
Code:

http://replay<cluster>.valve.net/570/<match_id>_<replay_salt>.dem.bz2

The cluster, match_id and replay_salt are available from the fields in GetMatchDetails. For the curious, cluster is the server data center the game was played at.

Are match history and details going to be available for private matches?
These are not available at this time. We'll are looking at a possible OATUH based authentication system that will allow players to retrieve their match history securely and allow third party sites to get that information they grant access to. We hope to have more details soon.

How do I find out what hero_id and item values translate into?
These values can be found in files that are in your Dota 2 install directory.
For heroes:
Steam/steamapps/common/dota 2 beta/gamedota/scripts/npc/npc_heroes.txt
For items:
Steam/steamapps/common/dota 2 beta/gamedota/scripts/npc/items.txt

Is there a WebAPI for current games in progress?
Not yet! But this is a excellent suggestion.

Are there limits on how many API calls?
Not presently, but you may get a 503 Error if the matchmaking server is busy or you exceed limits. Please wait 30 seconds and try again. A good rule of thumb is limit your requests to about one per second.

Update From the Dota 2 Development Team
As some of you have noticed, the WebAPI is currently inaccessible. What happened was that we were seeing such an overwhelming demand from people for this information that our servers were getting completely bogged down servicing all of these requests. None of the behavior we saw was malicious, there was just way too much demand and unfortunately it really started impacting the experience of general DOTA players and therefore we had to disable it for now. This is of course super interesting information and we want to make it as available to as many people as we possibly can and we are working on a couple of solutions to help greatly improve the situation so we can handle more requests, but can’t give any definitive time frame for when these will be brought online. We will keep you posted as things develop, but hopefully our solutions will let us have our cake and eat it too (after all not all cakes are a lie).

As a side note though, if people are developing against this API, make sure to implement rate limiting within your systems. We don’t have any numbers at this point, but we of course need to prevent individual accounts from submitting thousands of requests in a small window so that we can make sure that we can handle a reasonable number of users. Also if people have specific queries that they are running in large quantities that don’t naturally fit into the existing API let us know so that if it is a common request people have that the system can efficiently handle those requests. o

FAQ

Are match history and details going to be available for private matches?
These are not available at this time. We are looking at a possible OATUH based authentication system that will allow players to retrieve their private match history securely and allow third party sites to get that information they grant access to. We hope to have more details soon.

Is there a WebAPI for current games in progress?
Not yet! But this is a excellent suggestion.

Are there limits on how many API calls?

    You must manually limit your requests to one request per second in order to reduce the strain on the servers
    If you get a 503 Error: the matchmaking server is busy or you exceed limits. Please wait 30 seconds and try again.
    Please note that as written in the WebAPI T&C's, you are limited to 100,000 API calls per day.


Can I persist the data in a database or similar?
YES! In fact, it is recommended in order to reduce the strain on the server.

What is this "Unix time"/"UTC seconds since..."?
http://en.wikipedia.org/wiki/Unix_time

How do I get a player's 32- or 64-bit SteamID?
See SteamIDs above!

I want to start developing, should I jump right into grabbing data using the API?
Short answer; no. You should not.
Whilst you are developing your application, it will be rather silly and inconsiderate to slam the API with calls for data you just throw away.
In stead, consider one of two alternatives:
1) (preferred) Manually make a few calls to the API and save the results to your hard drive, then use these to test from until you're confident your application does what it's supposed to.
2) If you are developing your actual dynamic API calls, (first make sure you have implemented a suitable request limit as above) consider using the Dota2 Beta TEST API, which works identically to the Dota2 Beta API, except its urls are different:
Code:

Replace "IDOTA2Match_570" with "IDOTA2Match_205790"


