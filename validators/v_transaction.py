from template.template_transaction import get_id, get_day, get_type, get_sum


def validate_transaction(t):
    '''
    Function that validates a transaction
    INPUT: A transaction
    RAISES: Exception if:
        tid < 0
        day < 0
        sum < 0
        type != "INCOME" / "OUTCOME
    '''
    errors = ""
    if get_id(t) < 0:
        errors += "Invalid ID!\n"
    if get_day(t) < 0:
        errors += "Invalid Day!\n"
    if get_sum(t) < 0:
        errors += "Invalid Sum!\n"
    if str(get_type(t)) != "INCOME":
        if str(get_type(t)) != "OUTCOME":
            errors += "Invalid Type!\n"
    if len(errors) > 0:
        raise Exception(errors)
