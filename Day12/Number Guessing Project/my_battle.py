# variables globales
HERO_MAX_HP = 100
MONSTER_MAX_HP = 80
HERO_ATTACK_DAMAGE = 20
MONSTER_ATTACK_DAMAGE = 15

def initialize_battle():
    print("Welcome to the battle!")
    print(f"Hero initial HP: {HERO_MAX_HP}")
    print(f"Monster initial HP: {MONSTER_MAX_HP}")
    return HERO_MAX_HP, MONSTER_MAX_HP

def perform_attack(attacker_name, attacker_damage, defender_name, defender_hp):
    print(f"{attacker_name} attacks {defender_name} with {attacker_damage} attack damage.")
    remaining_hp = defender_hp - attacker_damage
    return remaining_hp


def run_battle():
    hero_current_hp, monster_current_hp = initialize_battle()

    while hero_current_hp > 0 and monster_current_hp > 0:
        monster_current_hp = perform_attack("Hero", HERO_ATTACK_DAMAGE, "Monster", monster_current_hp)
        print(f"Monster remaining HP is {monster_current_hp}")
        if monster_current_hp <= 0:
            print("Hero has won!")
            return
        hero_current_hp = perform_attack("Monster", MONSTER_ATTACK_DAMAGE, "Hero", hero_current_hp)
        print(f"Hero remaining HP is {hero_current_hp}")
        if hero_current_hp <= 0:
            print("Monster has won!")
            return

        print("\n--- End of Round ---")
        print(f"Hero's current HP: {hero_current_hp}")
        print(f"Monster's current HP: {monster_current_hp}")


if __name__ == "__main__":
    run_battle()