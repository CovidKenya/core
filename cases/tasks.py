from celery.task.schedules import crontab
from celery.decorators import periodic_task

from cases.services.get_cases import get_historical_data


# Run task every 30th minute of every hour divisible by three
@periodic_task(run_every=(crontab(minute=30, hour='*/12')), name="update_visuals_data", ignore_result=True)
def update_visuals_data():
    return get_historical_data()
