.. Items

Items
===================================================================

Unfortunately, there currently is no API call for the item list.

IDs
-------------------------------------------------------------------

Item IDs can be found in/parsed from the following game file::

    <path to steam>/Steam/steamapps/common/dota 2 beta/game/dota/scripts/npc/items.txt

Images
-------------------------------------------------------------------

There are two choices for this, either get the full quality images direct from the game files:
See CyborgMatt's guide here to learn how to open a vpk file.
the images can be found in the file::

    <path to steam>/Steam/steamapps/common/dota 2 beta/dota/pak01_dir.vpk

Then inside this file, they can be found in::

    root\resource\flash3\images\

OR get lower-quality images from the steam servers::

    http://media.steampowered.com/apps/dota2/images/items/<name>_lg.png

where <name> is the item's "name" from the text file above, without the "item_" at the start.


Deprecated?
-------------------------------------------------------------------

http://api.steampowered.com/IEconItems_816/GetSchema/v0001/?language=en&key=<YOUR API KEY> provides a list of all the items/actions/couriers/etc. This raw information is also provided below.

