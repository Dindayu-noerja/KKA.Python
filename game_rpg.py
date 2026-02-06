
class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")


# ===== INHERITANCE =====
class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")

    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)
        else:
            print("Mana tidak cukup!")


# ===== ENCAPSULATION =====
class HeroSecure:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal

    def get_hp(self):
        return self.__hp

    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def diserang(self, damage):
        sisa = self.get_hp() - damage
        self.set_hp(sisa)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")


# ===== MAIN =====
if __name__ == "__main__":
    hero1 = Hero("Layla", 100, 15)
    hero2 = Hero("Zilong", 120, 20)

    hero1.info()
    hero2.info()

    print("\n--- PERTARUNGAN ---")
    hero1.serang(hero2)
    hero2.serang(hero1)

    print("\n--- MAGE ---")
    eudora = Mage("Eudora", 80, 30, 100)
    balmond = Hero("Balmond", 200, 10)
    eudora.skill_fireball(balmond)

    print("\n--- ENCAPSULATION ---")
    aman = HeroSecure("Layla", 100)
    aman.set_hp(-50)
    print(aman.get_hp())
