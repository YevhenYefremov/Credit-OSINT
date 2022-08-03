import ccard
from bank_card import BankCard
from card_identifier.card_issuer import identify_card_issuer
from card_identifier.card_type import identify_card_type
from card_identifier.cardutils import validate_card
from payment_card_identifier import CardIdentifier

banner = '''

░█████╗░░░░░░░░█████╗░░██████╗██╗███╗░░██╗████████╗
██╔══██╗░░░░░░██╔══██╗██╔════╝██║████╗░██║╚══██╔══╝
██║░░╚═╝█████╗██║░░██║╚█████╗░██║██╔██╗██║░░░██║░░░
██║░░██╗╚════╝██║░░██║░╚═══██╗██║██║╚████║░░░██║░░░
╚█████╔╝░░░░░░╚█████╔╝██████╔╝██║██║░╚███║░░░██║░░░
░╚════╝░░░░░░░░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░░░╚═╝░░░

[+] Title   => C-OSINT [*]
[*] Coders  => Krd-Pentester (https://github.com/krdsploit/Credit-OSINT) [*] 
            => YevhenYefremov [*]
[*] Version => 0.1.1 [*] 


                '''


def menu():
    input_choice = 0

    while input_choice != 7:
        print("[1] Credit Card Validation")
        print("[2] Credit Card Type")
        print("[3] Credit Card Issuer")
        print("[4] Credit Card Generator")
        print("[5] BankCard")
        print("[6] Card Identify")
        print("[7] Exit")

        input_choice = int(input("Choose what to do => "))

        if input_choice == 1:
            valid()

        elif input_choice == 2:
            typer()

        elif input_choice == 3:
            issuer()

        elif input_choice == 4:
            credit_gene()

        elif input_choice == 5:
            BnkCard()

        elif input_choice == 6:
            identifier()


def valid():
    credit_card_number = input("Enter Your Credit Card Number => ").replace(' ', '')
    validate = validate_card(credit_card_number)
    print(validate)


def typer():
    credit_card_number = input("Enter Your Credit Card Number => ").replace(' ', '')
    validate = identify_card_type(credit_card_number)
    print(validate)


def issuer():
    credit_card_number = input("Enter Your Credit Card Number => ").replace(' ', '')
    validate = identify_card_issuer(credit_card_number)
    print(validate)


def credit_gene():
    print("[1] Master Card")
    print("[2] Visa Card")
    print("[3] Discover")
    print("[4] American Express")

    credit_type = int(input("What card type to generate? ==> "))

    if credit_type == 1:
        mst()

    elif credit_type == 2:
        vis()

    elif credit_type == 3:
        disc()

    elif credit_gene == 4:
        american()


def mst():
    x = ccard.mastercard()
    print(x)


def vis():
    y = ccard.visa()
    print(y)


def disc():
    z = ccard.discover()
    print(z)


def american():
    a = ccard.americanexpress()
    print(a)


def BnkCard():
    bank_card_number = input("Bank Card Number ==> ").replace(' ', '')
    bank_name = BankCard(bank_card_number)
    print(bank_name)


def identifier():
    bank_card_number = input("Bank Card Number ==> ").replace(' ', '')
    ya_card = CardIdentifier.from_numbers(bank_card_number)
    print(ya_card)


if __name__ == "__main__":
    menu()
