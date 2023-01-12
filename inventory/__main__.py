# Erdőkár Nyilvántartó Rendszer

# Készítette: Lászlók András (2022-2023)

# Az applikáció egy MySQL adatbázishoz kapcsolódik, amelyben a segítségével lekérdezéseket, feltöltéseket végezhetünk

from inventory import connector_inventory

if __name__ == '__main__':
    connector_inventory.run()

