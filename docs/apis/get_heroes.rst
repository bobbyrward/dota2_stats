.. Heroes

Heroes
===================================================================

Used to get an UP-TO-DATE list of heroes.

Examples
-------------------------------------------------------------------

To get the list of heroes with english names:

https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/?key=<key>&language=en_us

Result Field Format:

* heroes - an array of the heroes:
    * name - the hero's in-game "code name"
    * id - the hero's numeric ID
    * localized_name - the hero's name in the specified language (field is absent if no language specified)
* count - the total number of heroes in the list

Images
-------------------------------------------------------------------

You use the method as in `items`_
OR you can get them from valve's servers:

For a full-size image::

    http://media.steampowered.com/apps/dota2/images/heroes/<name>_full.png

For a thumbnail-size image::

    http://media.steampowered.com/apps/dota2/images/heroes/<name>_sb.png

where <name> is the hero's "name" from GetHeros, without the "\npc_hero_dota_" at the start.

