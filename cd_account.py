"""Import the Account class from the Account.py file."""
import Account as acct


def create_cd_account(balance: float, interest_rate: float, months: int):
    """
    Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        dict: A dictionary containing the account type, updated balance, interest earned, and months.
            - account_type (str): The type of account (CD).
            - updated_balance (float): The updated CD account balance after adding the interest earned.
            - interest_earned (float): The amount of interest earned.
            - months (int): The length of months for the CD.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    initial_interest: float = 0.00
    cd_account = acct.Account(balance, initial_interest)

    # Calculate interest earned
    interest_earned = balance * (interest_rate/100 * months/12)

    # Update the CD account balance by adding the interest earned
    updated_balance = cd_account.balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    cd_account.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    cd_account.set_interest(interest_earned)

    # Create a response dictionary with the account type, updated balance, interest earned, and months.
    response = {
        "account_type": "CD",
        "updated_balance": updated_balance,
        "interest_earned": interest_earned,
        "months": months
    }

    # Return the response dictionary.
    return response
