from db import do_command

customers = do_command("select ID, name, address from customer_list")
customer_rentals = do_command("select rental.rental_id, ID, name, address from customer_list inner join rental on rental.customer_id=ID")


for row in customers:
     print(row)

#for row in customer_rentals:
#    print(row)