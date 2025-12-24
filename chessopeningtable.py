from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Chess Opening", ["Ruy Lopez","Sicilian","French"])
table.add_column("Pokemon Name", ["Major","Major","Major"])

print(table.align)
#table.align = "l"

print(table)
