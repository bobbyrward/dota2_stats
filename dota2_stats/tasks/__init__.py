from dota2_stats.tasks.common import celery
from dota2_stats.tasks.updates import update_match_details
from dota2_stats.tasks.updates import update_player_details
from dota2_stats.tasks.updates import update_recent_matches


@celery.task
def add(x, y):
    return x + y
