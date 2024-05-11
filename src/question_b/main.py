import question_b

while True:
    response = input("""Menu:
    1 - Stock Purchase History
    2 - Exit
""")
    while response == '1':
        question_b.stock_purchase_history()
        response = None
    
    while response == '2':
        exit()