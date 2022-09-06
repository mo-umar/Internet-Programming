from db import do_command

def list_of_all_stores():
    return do_command("select * from store")

def list_of_all_films():
    return do_command("select * from film order by title")

def list_of_all_inventory():
    return do_command("select * from inventory")

def inventory_for_film(film_id):
    return do_command("select * from inventory where film_id = ?", [film_id])

def inventory_for_film_for_store(film_id, store_id):
    return do_command("select * from inventory where film_id = ? and store_id = ?", [film_id, store_id])

def count_rentals_for_film(film_id):
    invent = inventory_for_film(film_id)
    rentals = 0
    for inv in invent:
        rnt = do_command("select count(all) as cnt  from rental where inventory_id = ?", [inv['inventory_id']])
        rentals += rnt[0]['cnt']
    return rentals

allstores = list_of_all_stores()
print("-" * 100)
for row in allstores:
    print (row)
print("-" * 100)

allfilms = list_of_all_films()
print("-" * 100)
for row in allfilms:
    print (row)
print("-" * 100)

allinventory = list_of_all_inventory()
print("-" * 100)
for row in allinventory:
    print (row)
print("-" * 100)

inventoryforfilm = inventory_for_film(999)
print("-" * 100)
for row in inventoryforfilm:
    print (row)
print("-" * 100)

inventoryforfilmstore = inventory_for_film_for_store(999, 1)
print("-" * 100)
for row in inventoryforfilmstore:
    print (row)
print("-" * 100)

countforfilm = count_rentals_for_film(999)
print("-" * 100)
print(str(countforfilm) + " Rentals")
print("-" * 100)