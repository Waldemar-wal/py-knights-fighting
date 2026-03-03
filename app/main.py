from app.knights.knight import Knight
from app.knights.knights_config import KNIGHTS
from app.battle.battle import Battle


dict_of_knights = {
    key: Knight(
        name=value.get("name"),
        power=value.get("power"),
        hp=value.get("hp"),
        armour=value.get("armour"),
        weapon=value.get("weapon"),
        potion=value.get("potion"),
    ) for key, value in KNIGHTS.items()
}


def battle(knights: dict) -> dict:
    battle_results = {}

    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot_vs_mordred = Battle(
        lancelot.prepare_battle(), mordred.prepare_battle()
    )
    battle_results.update(lancelot_vs_mordred.start_battle())

    # 2 Arthur vs Red Knight:
    arthur_vs_red_knight = Battle(
        arthur.prepare_battle(), red_knight.prepare_battle()
    )
    battle_results.update(arthur_vs_red_knight.start_battle())

    # Return battle results:
    return battle_results


print(battle(dict_of_knights))
