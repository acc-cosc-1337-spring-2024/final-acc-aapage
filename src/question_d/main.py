#add import

import question_d

while True:
    table = question_d.create_multiplication_table()
    response = input("""Menu:
    1 - Display Multiplication Table
    2 - Exit
""")
    while response == '1':
        question_d.display_multiplication_table(table)
        response = None
    
    while response == '2':
        exit()