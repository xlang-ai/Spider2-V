from airflow.decorators import task, dag
from pendulum import datetime
import requests
import logging

@dag(
    start_date=datetime(2024, 4, 1),
    schedule="@daily",
    catchup=False,
    tags=['bored_api', 'daily_activity']
)
def activity_suggestion_dag():
    @task
    def fetch_activity():
        """Fetches an activity suggestion from the Bored API."""
        response = requests.get("https://www.boredapi.com/api/activity")
        if response.status_code == 200:
            return response.json()
        else:
            logging.error('Failed to fetch data from Bored API')
            return None
    
    @task
    def analyze_activity(activity):
        """Analyzes the accessibility of the fetched activity."""
        if activity and 'accessibility' in activity:
            accessibility_rating = activity['accessibility']
            logging.info(f"Accessibility of the activity is rated as: {accessibility_rating}")
            return {
                'accessibility': accessibility_rating,
                'description': f"Activity involves: {activity.get('activity')} with accessibility rating of {accessibility_rating}"
            }
        else:
            logging.error("No accessibility info available for analysis")
            return None

    @task
    def log_activity(activity):
        """Logs the activity or an error if no activity was fetched."""
        if activity:
            logging.info(f"Today's activity: {activity.get('activity')}")
        else:
            logging.error("No activity was fetched successfully")

    activity = fetch_activity()
    logged_activity = log_activity(activity)
    analyzed_activity = analyze_activity(activity)
    
    # Define task dependencies
    activity >> logged_activity >>  analyzed_activity 

activity_suggestion_dag()
