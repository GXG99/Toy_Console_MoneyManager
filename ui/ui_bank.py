from service.srv_transaction import srv_add_transaction, srv_modify_transaction
from utils.utils_transaction import dt_at_day, dt_of_type, dt_at_period, pt_all,\
    pt_bigger, t_order, e_type, e_lst
from utils.utils_undo import update_undo
from binascii import hexlify


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
        D_ATPERIOD - To delete all transaction from a given period of time
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
    menu = {}
    menu["ADD"] = ui_add_transaction
    menu["UPDATE"] = srv_modify_transaction
    menu["D_ATDAY"] = dt_at_day
    menu["D_TT"] = dt_of_type
    menu["D_ATPERIOD"] = dt_at_period
    menu["PT_ALL"] = pt_all
    menu["PT_BIGGER"] = pt_bigger
    menu["T_ORDER"] = t_order
    menu["E_TYPE"] = e_type
    menu["E_LST"] = e_lst
    return menu


def read_numeric(msg, tip):
    x = input(msg)
    while True:
        try:
            x = tip(x)
            return x
        except ValueError:
            print("Insert a valid integer please: ")
            x = input()


def ui_add_transaction(l):
    tid = read_numeric("Insert transaction ID: ", int)
    day = read_numeric("Insert day: ", int)
    s = read_numeric("Insert sum: ", int)
    tp = input("Insert type: ")
    srv_add_transaction(l, tid, day, s, tp)


def display_ui():
    print_menu()
    l = []
    undol = []
    menu = create_menu()
    while True:
        cmd = input("Choose your command: ")
        if cmd == "exit":
            return
        if cmd in menu:
            try:
                menu[cmd](l)
                update_undo(l, undol)
            except Exception as ex:
                print(str(ex))
        else:
            print("Invalid command!\n")


def run_ui():
    display_ui()
