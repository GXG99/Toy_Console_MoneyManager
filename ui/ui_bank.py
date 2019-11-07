def print_menu():
    '''
    Function that prints the menu
    INPUT: -
    OUTPUT: Menu text
    '''
    print(
        ''' Welcome to this banking account managing application
    Possible managing commands:
    1. Transaction tools:
        ADD - To add a new transaction 
        UPDATE - To update a specific transaction
        D_ATDAY - To delete all transactions on a specific day
        D_TT - To delete all transactions of a specific type
    2. Searching Tools:
        PT_ALL - Prints all transactions
        PT_BIGGER - Prints all transactions bigger than a given sum
        PT_UNTILDAY_BIGGER - Prints all transactions made until the given date with the sum larger than the given number.
        PT_TYPE - Prints all transactions of a given type
    3. Statistics Tools:
        ST - Total sum of transactions of a given type
        BALLANCE - Account Ballance at a given date
        T_ORDER - All transactions of a given type, ordered by sum
    4. Filter:
        E_TYPE - Eliminate all transactions of a given type
        E_LST - Eliminate all transactions with a lowwer sum and of  a given type
    UNDO - Undos the last operation that modified the transactions list.
    ''')


def create_menu():
    pass


def display_ui():
    print_menu()
    menu = create_menu()


def run_ui():
    display_ui()
