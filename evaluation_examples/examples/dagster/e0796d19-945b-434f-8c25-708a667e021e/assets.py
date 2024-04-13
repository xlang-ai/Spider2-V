import json
from dagster import asset, get_dagster_logger

@asset
def all_potions() -> None:
    with open("data/raw_potions.json") as f:
        raw_potions = json.load(f)
    potion_data = raw_potions['data']
    with open("data/potions.json", "w") as f:
        json.dump(potion_data, f)

@asset(deps=[all_potions])
def count_advanced_difficulty_potions() -> int:
    with open("data/potions.json") as f:
        potions = json.load(f)
    cnt = 0
    for potion in potions:
        cnt += (potion['attributes']['difficulty'] == 'Advanced')
    get_dagster_logger().info(cnt)
    
    return cnt