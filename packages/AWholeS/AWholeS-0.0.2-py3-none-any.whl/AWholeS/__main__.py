import inquirer

from AWholeS.ec2 import show_all_regions, show_all_available_regions
from AWholeS.sts_calls import (
    get_current_arn,
    get_current_assumed_role,
    get_current_account_id,
)
from AWholeS.trusted_advisor_security import TrustedAdvisor


def menu() -> None:
    """
    Shows the menu with current options of the app.
    Each option should call a function besides exit.
    :return: None
    """
    last_choice = None
    while True:
        choice = inquirer.list_input(
            "What do you want to run?",
            choices=["EC2", "STS", "Trusted Advisor", "exit"],
            default=last_choice,
        )
        if choice == "EC2":
            print("Showing all regions:")
            show_all_regions()
            print("\n")
            print("Showing current available regions:")
            show_all_available_regions()
            print("\n")
        elif choice == "STS":
            print("Your current ARN is:")
            print(get_current_arn())
            print("\n")
            print("Your current AssumedRole is:")
            print(get_current_assumed_role())
            print("\n")
        elif choice == "Trusted Advisor":
            ta = TrustedAdvisor()
            print(f"Current Security failures for your account {get_current_account_id()}:")
            ta.show_failed_security_checks()
            print("\n")
        elif choice == "exit":
            return
        last_choice = choice


# If this doesn't find modules, use:
# export PYTHONPATH=$PYTHONPATH:.
# Ref: https://stackoverflow.com/questions/37233140/python-module-not-found
if __name__ == "__main__":
    print("Running AWholeS...")
    menu()
