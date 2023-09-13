order_list_select = [
            "tb.okey",
            "tb.iogy", 
            "tb.itcd",
            "tb.idsc",
            "tb.ooqy",
            "tb.oqty", 
            "tb.dlqy", 
            "tb.foqy", 
            "tb.sunt", 
            "tb.pric",
            "tb.psdt", 
        ]
order_list_columns = ", ".join(order_list_select)
print(order_list_columns)