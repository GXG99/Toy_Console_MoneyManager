from template.template_transaction import get_id


def repo_add_transaction(l, t):
    '''
    Function that adds a transaction to the list if the ID is not existent
    INPUT: l - a list, t - a transaction
    OUTPUT: Raises exception if ID is existent
    '''
    error = ""
    for tr in l:
        if get_id(tr) == get_id(t):
            error += "ID already exists!\n"
            raise Exception(error)
    l.append(t)
