from prettytable import PrettyTable
table = PrettyTable()


table.add_column("Pokemon Name: ", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type: ", ["Electric", "Water", "Fire"])
table.add_column("Id:", [1, 2, 3])
# align the table left 
table.align = "l"
# Print the table
print(table)

# use add_row() when you want to add a complete record/ entry 
# use add_column() when you want to add a new category of data:
# row = i want to add a new person to my table
# column = i want to add a new piece of information about everyone

table2 = PrettyTable()
table2.field_names = ["Name", "Age", "City"]
table.add_row(["Alice", 25, "New York"])
table2.add_row(["Bob", 30, "Los Angeles"])

print(table2)