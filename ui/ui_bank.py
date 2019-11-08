from service.srv_transaction import srv_add_transaction, srv_modify_transaction
from utils.utils_transaction import dt_at_day, dt_of_type, dt_at_period, pt_all,\
    pt_bigger, t_order, e_type, e_lst
from utils.utils_undo import update_undo
from validators.v_command import convert_command


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
    menu["D_ATDAY"] = ui_dt_at_day
    menu["D_TT"] = dt_of_type
    menu["D_ATPERIOD"] = dt_at_period
    menu["PT_ALL"] = ui_pt_all
    menu["PT_BIGGER"] = pt_bigger
    menu["T_ORDER"] = t_order
    menu["E_TYPE"] = e_type
    menu["E_LST"] = e_lst
    return menu


def ui_dt_at_day(l, params):
    error = ""
    try:
        day = int(params[0])
        dt_at_day(l, day)
    except ValueError:
        error += "Please insert a valid integer"
        raise Exception(error)


def ui_pt_all(l, params):
    pt_all(l)


def ui_add_transaction(l, params):
    p = convert_command(params)
    tid = p[0]
    day = p[1]
    s = p[2]
    tp = p[3]
    srv_add_transaction(l, tid, day, s, tp)


def ui_get_params(command_text):
    params = []
    for x in command_text[1:]:
        params.append(x)
    return params


def display_ui():
    print_menu()
    l = []
    undol = []
    menu = create_menu()
    while True:
        command_text = input("Insert your command: ").split(" ")
        cmd = command_text[0]
        if cmd == "exit":
            return
        if cmd in menu:
            try:
                params = ui_get_params(command_text)
                menu[cmd](l, params)
            except Exception as ex:
                print(str(ex))
        else:
            print("Invalid command!\n")


def run_ui():
    display_ui()
