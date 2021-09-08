default_row = ["⬛" for i in range(10)]
fields = {k:default_row.copy() for k in list("ABCDEFGHIJ")}

fields["A"][0] = "🔷"
fields["J"][9] = "🔶"

class Field:

    def __init__(self):
        pass

selected = "⬜"
friendly_capture = "🟦"
enemy_capture = "🟧"

fields["A"][1] = friendly_capture
fields["J"][8] = enemy_capture

def render_field(fields):

    print("     0 1 2 3 4 5 6 7 8 9\n")

    for colum_key in fields:
        colum = f"{colum_key}   "
        
        for field in fields[colum_key]:
            
            colum = f"{colum} {field}" 
        
        print(colum)

render_field(fields)