"""Import the Account class from the Account.py file."""
import Account as acct


# Define a function for the Savings Account
def create_savings_account(balance: float, interest_rate: float, months: int):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    initial_interest: float = 0.00
    savings_account = acct.Account(balance, initial_interest)

    # Calculate interest earned
    interest_earned = balance * (interest_rate/100 * months/12)

    # Update the savings account balance by adding the interest earned
    updated_balance = savings_account.balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    savings_account.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    savings_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return updated_balance, interest_earned
