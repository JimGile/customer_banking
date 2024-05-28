# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account


def non_negative_input(prompt: str) -> float:
    """
    Prompt the user to enter a non-negative number.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        float: The non-negative number entered by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Please enter a valid number.")


def prompt_user_for_account_info(account_type: str):
    """
    Prompt the user to enter the account balance, interest rate, and length of months for the given account type.

    Parameters:
        account_type (str): The type of account (CD or Savings) for which the user is entering the information.

    Returns:
        dict: A dictionary containing the following keys with the corresponding values entered by the user:
        'balance': (float),
        'interest_rate': (float),
        'months': (int)
    """
    # Prompt the user to enter the account balance
    balance: float = non_negative_input(f"Enter the {account_type} account balance: ")

    # Prompt the user to enter the interest rate
    interest_rate: float = non_negative_input(f"Enter the {account_type} account APR: ")

    # Prompt the user to enter the length of months
    months: int = int(non_negative_input(f"Enter the {account_type} account maturity in months: "))

    return {'balance': balance, 'interest_rate': interest_rate, 'months': months}


def print_interest_and_balance(account_type: str, interest_earned: float, updated_balance: float, months: int):
    """
    Print out the interest earned and updated savings account balance with interest earned for the given months.

    Args:
        account_type (str): The type of account (Savings or CD).
        interest_earned (float): The amount of interest earned.
        updated_balance (float): The updated balance of the account with interest earned.
        months (int): The number of months for which the interest is earned.

    Returns:
        None
    """
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Interest earned: ${interest_earned:,.2f}")
    print(f"Updated {account_type} account balance with interest earned for {months} months: ${updated_balance:,.2f}")


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance,
    interest rate, and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    account_types = ["Savings", "CD"]
    for account_type in account_types:
        # Prompt the user to set the balance, interest rate, and months for the current account type.
        input_dict = prompt_user_for_account_info(account_type)

        # Call the appropriate create account function and pass the variables from the user.
        if account_type == "Savings":
            response_dict = create_savings_account(**input_dict)
        else:
            response_dict = create_cd_account(**input_dict)

        # Print out the interest earned and updated account balance with interest earned for the given months.
        print_interest_and_balance(**response_dict)


if __name__ == "__main__":
    # Call the main function.
    main()
