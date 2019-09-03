from json import load
from datetime import datetime

file_name = "services.json"
transaction = "transactions.txt"


def print_welcome_message():
    print(
        """
                         .--~~,__
            :-....,-------`~~'._.'
            `-,,,  ,_      ;'~U'
            _,-' ,'`-__; '--.
            (_/'~~      ''''(;
 WELCOME TO LUXURY DOG SERVICES!
    """
    )


def load_services(filename):
    with open(filename) as file:
        json_services = load(file)
    return json_services["services"]


def print_services(services):
    print("These are the services we offer:")
    for key, value in services.items():
        print(key, value["price"])


def get_service(keys):
    while True:
        choice = input("What will you be receiving today:  ").lower().strip()
        if choice in keys:
            return choice
        print(choice, "We do not offer that.")
        print("Our choices are ", keys)


def save_transaction(filename, services):
    data = f"{datetime.now()}, {services['name']}, {services['price']}"
    with open(filename, "a") as file:
        file.write(data)


def main():
    print_welcome_message()
    services = load_services(file_name)
    print_services(services)
    service_name = get_service(services.keys())
    print(service_name.title(), "Great choice!")
    print("Your total is: ${:.2f}".format(services[service_name]["price"]))
    save_transaction(transaction, services[service_name])
    print("Thank you, have a nice day!")


if __name__ == "__main__":
    main()
