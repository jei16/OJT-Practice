class SalesTable:
    def __init__(self):
        self.data = []
        self.header = (
            "CODE",
            "DESCRIPTION",
            "UNIT",
            "ORDERED",
            "REG",
            "OBC",
            "ALLO",
            "TOTAL",
            "AMOUNT",
        )

    def add_item(self, item):
        self.data.append(item)

    def generate_table(self):
        table = "┌" + "─" * 78 + "┐\n"
        table += "│DELIVERED TO  :                                     DATE          :  08/23/2023  │\n"
        table += "│CUSTOMER NAME :  HYPERMARKET MUNTINLUPA             PLAN DEL DATE :  10/11/2022  │\n"
        table += "│ADDRESS       :                                     ORDER NUMBER  :  RSO 1327    │\n"
        table += "│CUSTOMER CODE :  600483                             ORDER DATE    :  10/05/2022  │\n"
        table += "├" + "─" * 78 + "┤\n"
        table += "│{:<10}│{:<30}│{:<5}│{:<7}│{:<5}│{:<5}│{:<5}│{:<5}│{:<8}│\n".format(*self.header)
        table += "├" + "─" * 78 + "┤\n"
        
        for item in self.data:
            table += "│{:<10}│{:<30}│{:<5}│{:<7}│{:<5}│{:<5}│{:<5}│{:<5}│{:<8}│\n".format(*item)
        
        table += "└" + "─" * 78 + "┘"
        return table

# Example usage:
sales_table = SalesTable()
sales_table.add_item(("3160002", "1. Cathedral Window Singles", "pcs", 2, "", "", "", "", ""))
sales_table.add_item(("3100001", "2. Black Forest Cake", "pcs", 2, "", "", "", "", ""))
# Add more items as needed

table_output = sales_table.generate_table()
print(table_output)
