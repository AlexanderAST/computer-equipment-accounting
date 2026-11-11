equipment = []


def add_equipment(inventory_number, name, location, responsible):
    equipment.append({
        "inventory_number": inventory_number,
        "name": name,
        "location": location,
        "responsible": responsible,
        "status": "в эксплуатации",
    })


def find_equipment(inventory_number):
    for item in equipment:
        if item["inventory_number"] == inventory_number:
            return item
    return None


def show_all():
    for item in equipment:
        print(item["inventory_number"], item["name"], item["location"],
              item["responsible"], item["status"])


def write_off(inventory_number):
    item = find_equipment(inventory_number)
    if item is not None:
        item["status"] = "списано"
        

if __name__ == "__main__":
    add_equipment("ИНВ-0001", "Ноутбук Lenovo ThinkPad", "Кабинет 204", "Петров И. И.")
    add_equipment("ИНВ-0002", "Монитор Samsung 24", "Кабинет 204", "Петров И. И.")
    add_equipment("ИНВ-0003", "Принтер HP LaserJet", "Кабинет 101", "Сидорова А. В.")
    show_all()
    print(find_equipment("ИНВ-0002"))
    print("Завершено")