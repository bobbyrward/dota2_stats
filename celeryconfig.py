from datetime import timedelta


BROKER_URL = 'redis://'
CELERY_RESULT_BACKEND = 'redis://'
CELERY_IMPORTS = ('dota2_stats.tasks',)


CELERYBEAT_SCHEDULE = {
    'runs-every-5-minutes': {
      'task': 'dota2_stats.tasks.updates.update_recent_matches',
      'schedule': timedelta(minutes=5),
    },
}
