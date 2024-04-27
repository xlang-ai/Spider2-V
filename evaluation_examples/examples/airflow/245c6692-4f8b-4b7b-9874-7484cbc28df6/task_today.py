from airflow.decorators import task, dag
from pendulum import datetime
import requests

doc_md_doc = """

### Purpose of this task

This task **boldly** suggests a daily activity to occupy my time.

Weather today: https://wttr.in/HongKong

If I don't like the suggested activity I can always play some games instead.

Check steam for my game: https://store.steampowered.com/

Sports today: running
gear: |
    - running shoes
    - sports clothes
    - a healthy lung
I hate running

But I can watch some anime when running: https://www.bilibili.com/
"""

@dag(
    start_date=datetime(2024,4,1),
    schedule="@daily",
    catchup=False,
)

def task_today():

    @task(
    doc_md=doc_md_doc
    )

    def tell_me_what_to_do():
        response = requests.get("https://www.boredapi.com/api/activity")
        return response.json()["activity"]

    tell_me_what_to_do()

task_today()

