from template.template_transaction import create_transaction, get_type,\
    modify_transaction, get_id
from validators.v_transaction import validate_transaction
from repo.repo_transaction import repo_add_transaction


def srv_add_transaction(l, tid, day, s, tp):
    '''
    Function that adds a valid transaction to the list
    INPUT:
        l - a list
        tid - transaction id / INTEGER
        day - transaction day / INTEGER
        s - transaction sum / INTEGER
        tp - transaction type / STRING
    '''
    t = create_transaction(tid, day, s, tp)
    validate_transaction(t)
    repo_add_transaction(l, t)


def srv_modify_transaction(l, tid, day, s, tp):
    for x in l:
        if get_id(x) == tid:
            modify_transaction(x, day, s, tp)
