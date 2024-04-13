from dagster import materialize
from harry_potter_potions.assets import all_potions, count_advanced_difficulty_potions

def test_potions_assets():
    assets = [all_potions, count_advanced_difficulty_potions]
    result = materialize(assets)
    assert result.success
    cnt = result.output_for_node("count_advanced_difficulty_potions")
    assert cnt == 14