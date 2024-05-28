""" Defines a base Account class with setter methods."""


class Account:

    def __init__(self, balance, interest):
        """
        Initializes a new instance of the Account class.

        Parameters:
            balance (float): The initial balance of the account.
            interest (float): The interest rate for the account.
        """
        self.balance: float = balance
        self.interest: float = interest

    # This method sets the balance of the account.
    def set_balance(self, balance: float):
        """
        Set the balance of the account.

        Parameters:
            balance (float): The new balance for the account.

        Returns:
            None
        """
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest: float):
        """
        Set the interest gained for the account.

        Args:
            interest (float): The new interest rate for the account.

        Returns:
            None
        """
        self.interest = interest
