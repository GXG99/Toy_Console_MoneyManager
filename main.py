'''
Created on Nov 7, 2019

@author: George
'''

from test.test_transaction import run_all_tests
from ui.ui_bank import run_ui


def run():
    run_all_tests()
    run_ui()


run()
