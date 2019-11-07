def create_transaction(tid, day, s, tp):
    '''
    Function that creates a transaction.
    INPUT: day - integer, sum - integer, type - string
    OUTPUT: A transaction
    '''
    return {
        "id": tid,
        "day": day,
        "sum": s,
        "type": tp
    }


def get_day(t):
    return t["day"]


def get_sum(t):
    return t["sum"]


def get_type(t):
    return t["type"]


def get_id(t):
    return t["id"]


def set_day(t, day):
    t["day"] = day


def set_sum(t, s):
    t["sum"] = s


def set_type(t, tp):
    t["type"] = tp


def modify_transaction(t, day, s, tp):
    set_day(t, day)
    set_sum(t, s)
    set_type(t, tp)
