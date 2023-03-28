import random


class Character:
    def __init__(self, name, power, hp):
        self.name = name
        self.power = power
        self.hp = hp
        self.magic_attack_count = 3

    def attack(self, monster):
        print(f"{self.name}의 공격!")
        damage = random.randint(self.power + 0, self.power + 6)
        monster.hp -= damage
        print(f"{monster.name}에게 {damage}의 데미지를 입혔습니다!")

    def magic_attack(self, monster):        
        # if self.magic_attack_count <= 0:
        #     print("마법 공격 횟수 소진! 지금부터 마법 공격 사용 시 피해만 입습니다!")
        #     return
        print(f"{self.name}의 마법 공격!")
        damage = random.randint(self.power - 5, self.power + 0) * 2
        monster.hp -= damage
        print(f"{monster.name}에게 {damage}의 마법 데미지를 입혔습니다!")
        self.magic_attack_count -= 1

    def show_status(self):
        print(f"{self.name} (체력: {self.hp}, 파워: {self.power}, 마법공격 가능 횟수: {self.magic_attack_count})")


class Monster:
    def __init__(self, name, power, hp):
        self.name = name
        self.power = power
        self.hp = hp

    def attack(self, player):
        print(f"{self.name}의 공격!")
        damage = random.randint(self.power + 1, self.power + 6)
        player.hp -= damage
        print(f"{player.name}에게 {damage}의 데미지를 입혔습니다!")

    def show_status(self):
        print(f"{self.name} (체력: {self.hp}, 파워: {self.power})")


# 플레이어 생성
player_name = input("플레이어 이름을 입력해주세요: ")
player_power = 10
player_hp = 200
player = Character(player_name, player_power, player_hp)

# 몬스터 생성
monster_name = "몬스터"
monster_power = 10
monster_hp = random.randint(190, 200)
monster = Monster(monster_name, monster_power, monster_hp)


# 전투 시작
print(f"{player.name} vs {monster.name}! 전투 시작!!")
while True:
    # 플레이어 턴
    print(f"== {player.name}의 차례 ==")
    if player.magic_attack_count <= 0:
        print("마법 공격 횟수 소진! 지금부터 마법 공격 사용 시 피해만 입습니다!")
    player.show_status()
    monster.show_status()
    attack_type = input("어떤 공격을 사용하시겠습니까? (1. 일반공격 / 2. 마법공격): ")
    if attack_type == "1":
        player.attack(monster)
    elif attack_type == "2":
        player.magic_attack(monster)
    else:
        print("잘못된 입력입니다. 다시 선택해주세요.")
        continue

    if monster.hp <= 0:
        print(f"{monster.name}를 물리쳤습니다! {player.name}의 승리!")
        break

    print('\n')

    # 몬스터 턴
    print(f"== {monster.name}의 차례 ==")
    player.show_status()
    monster.show_status()
    monster.attack(player)

    if player.hp <= 0:
        print(f"{player.name}가 쓰러졌습니다. {monster.name}의 승리!")
        break

    print('\n')
