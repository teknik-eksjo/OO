import pytest
from exercises.oo import BankAccount, MinimumBalanceAccount


def test_bank_account():
    account = BankAccount()
    assert hasattr(account, 'balance')
    assert account.balance == 0
    assert account.deposit(100) == 100
    assert account.withdraw(75) == 25
    assert account.withdraw(50) == -25


def test_minimum_balance_account():
    account = MinimumBalanceAccount(100)
    assert hasattr(account, 'balance')
    assert account.balance == 0
    assert account.deposit(25) == 25
    assert account.deposit(100) == 125
    assert account.withdraw(20) == 105

    with pytest.raises(ValueError):
        account.withdraw(10)
    assert account.balance == 105

    assert account.withdraw(5) == 100
    assert account.deposit(10) == 110

    with pytest.raises(ValueError):
        account.withdraw(11)
    assert account.balance == 110


def test_minimum_balance_account_is_subclass():
    assert issubclass(MinimumBalanceAccount, BankAccount)
