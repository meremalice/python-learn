rapper_name = input("Enter your rapper name: ")
concert_ticket_price = float(input("Enter the concert ticket price: "))
concert_ticket_sold = int(input("Enter the number of concert tickets sold: "))
merch_price = float(input("Enter the price of the merch: "))
merch_sold = int(input("Enter the number of merch sold: "))
total_revenue = (concert_ticket_price * concert_ticket_sold) + (merch_price * merch_sold)
amount_per_person = int(input("Enter the amount of people: "))
split_revenue = total_revenue / 2

print(f"{rapper_name} made ${total_revenue:.2f} in total, so each of the {amount_per_person} people gets ${split_revenue:.2f}")


