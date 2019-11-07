'''
Created on Nov 7, 2019

@author: George
'''

from template.template_transaction import create_transaction, get_day, get_sum, get_type, get_id, modify_transaction
from validators.v_transaction import validate_transaction
from repo.repo_transaction import repo_add_transaction
from service.srv_transaction import srv_add_transaction, srv_modify_transaction
from utils.utils_transaction import dt_at_day, dt_at_period, dt_of_type, pt_all,\
    pt_bigger, pt_untilday_bigger


def test_add_transaction():
    '''
    Function that tests if a transaction can be added
    INPUT: -
    OUTPUT: Assertion error if test fails
    '''

    t = create_transaction(21, 5, 1500, "INCOME")

    assert get_id(t) == 21
    assert get_day(t) == 5
    assert get_sum(t) == 1500
    assert get_type(t) == "INCOME"

    modify_transaction(t, 13, 1000, "OUTCOME")

    assert get_id(t) == 21
    assert get_day(t) == 13
    assert get_sum(t) == 1000
    assert get_type(t) == "OUTCOME"


def test_validate_transaction():
    '''
    Function that tests if a transaction is valid
    INPUT: - 
    OUTPUT: Assertion error if test fails
    '''
    t = create_transaction(21, 5, 1500, "INCOME")
    validate_transaction(t)
    t = create_transaction(-21, -978, -15, "INC")
    try:
        validate_transaction(t)
        assert False
    except Exception as ex:
        assert (str(ex) == "Invalid ID!\nInvalid Day!\nInvalid Sum!\nInvalid Type!\n")

    t = create_transaction(21, -978, -15, "INC")
    try:
        validate_transaction(t)
        assert False
    except Exception as ex:
        assert (str(ex) == "Invalid Day!\nInvalid Sum!\nInvalid Type!\n")

    t = create_transaction(21, 978, -15, "INC")
    try:
        validate_transaction(t)
        assert False
    except Exception as ex:
        assert (str(ex) == "Invalid Sum!\nInvalid Type!\n")


def test_add_transaction_to_list():
    '''
    Function that tests if a transaction is added to the list
    INPUT: -
    OUTPUT: Assertion error if test fails
    '''
    l = []
    t = create_transaction(21, 5, 1500, "INCOME")
    repo_add_transaction(l, t)
    assert(len(l) == 1)
    assert(l == [t])

    t2 = create_transaction(21, 5, 2500, "OUTCOME")
    try:
        repo_add_transaction(l, t2)
        assert False
    except Exception as ex:
        assert(str(ex) == "ID already exists!\n")


def test_modify_transaction():
    '''
    Function that tests if a transaction can be modified
    INPUT:
    OUTPUT:
    '''
    l = []
    srv_add_transaction(l, 42, 5, 1500, "INCOME")
    srv_modify_transaction(l, 42, 6, 1000, "OUTCOME")
    assert (get_day(l[0]) == 6)
    assert (get_sum(l[0]) == 1000)
    assert (get_type(l[0]) == "OUTCOME")


def test_srv_add_transaction():
    '''
    Function that test if srv_add_transaction adds a transaction to the transaction list correctly
    INPUT: -
    OUTPUT: Assertion error if test fails
    '''
    l = []
    srv_add_transaction(l, 23, 5, 1500, "INCOME")
    assert len(l) == 1
    assert get_id(l[0]) == 23
    assert get_day(l[0]) == 5
    assert get_sum(l[0]) == 1500
    assert get_type(l[0]) == "INCOME"

    srv_add_transaction(l, 22, 6, 500, "OUTCOME")
    assert len(l) == 2
    assert get_id(l[1]) == 22
    assert get_day(l[1]) == 6
    assert get_sum(l[1]) == 500
    assert get_type(l[1]) == "OUTCOME"

    try:
        srv_add_transaction(l, -2, 23, 1500, "INCOME")
        assert False
    except Exception as ex:
        assert(str(ex) == "Invalid ID!\n")


def test_delete_functions():
    '''
    Function that
    '''
    l = []
    srv_add_transaction(l, 42, 5, 1500, "OUTCOME")
    srv_add_transaction(l, 43, 2, 500, "INCOME")
    srv_add_transaction(l, 44, 64, 1200, "OUTCOME")
    srv_add_transaction(l, 45, 21, 5400, "INCOME")
    srv_add_transaction(l, 46, 5, 7800, "OUTCOME")
    srv_add_transaction(l, 47, 42, 200, "INCOME")
    dt_at_day(l, 5)

    assert len(l) == 4

    for x in l:
        assert get_day(x) != 5

    l.clear()

    srv_add_transaction(l, 42, 5, 1500, "OUTCOME")
    srv_add_transaction(l, 43, 2, 500, "INCOME")
    srv_add_transaction(l, 44, 64, 1200, "OUTCOME")
    srv_add_transaction(l, 45, 21, 5400, "INCOME")
    srv_add_transaction(l, 46, 6, 7800, "OUTCOME")
    srv_add_transaction(l, 47, 42, 200, "INCOME")

    dt_at_period(l, 5, 42)

    assert len(l) == 2

    for x in l:
        assert (get_day(x) <= 5 or get_day(x) >= 42)

    l.clear()

    srv_add_transaction(l, 42, 5, 1500, "OUTCOME")
    srv_add_transaction(l, 43, 2, 500, "INCOME")
    srv_add_transaction(l, 44, 64, 8200, "OUTCOME")
    srv_add_transaction(l, 45, 21, 5400, "INCOME")
    srv_add_transaction(l, 46, 6, 7800, "OUTCOME")
    srv_add_transaction(l, 47, 42, 200, "INCOME")

    dt_of_type(l, "INCOME")

    assert len(l) == 3

    for x in l:
        assert (get_type(x) != "INCOME")


def run_all_tests():
    test_add_transaction()
    test_validate_transaction()
    test_add_transaction_to_list()
    test_srv_add_transaction()
    test_modify_transaction()
    test_delete_functions()
