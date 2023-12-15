
import time
from colorama import Fore, Back, Style, init
# I imported colorama to improve text and user readability
init()

class VendingMachine:
    def __init__(self):
        self.menu = {  # The dictionary defining the menu items with their codes, names, and prices 
            '=====🥤 Soda 🥤=====': {
                'A1': {'item': 'Cola', 'price': 1.50},
                'A2': {'item': 'Sprite', 'price': 1.00},
                'A3': {'item': 'Fanta', 'price': 1.25},
                'A4': {'item': 'Ginger Ale', 'price': 1.75},
                'A5': {'item': 'Root Beer', 'price': 2.00},
            },
            '=====🍟 Chips 🍟=====': {
                'B1': {'item': 'Classic Potato Chips', 'price': 1.50},
                'B2': {'item': 'Tortilla Chips', 'price': 1.25},
                'B3': {'item': 'Barbecue Chips', 'price': 1.75},
                'B4': {'item': 'Sour Cream & Onion Chips', 'price': 2.00},
                'B5': {'item': 'Cheddar Cheese Chips', 'price': 1.90},
            },
            '====🍫 Chocolate 🍫====': {
                'C1': {'item': 'Milk Chocolate', 'price': 2.50},
                'C2': {'item': 'Dark Chocolate', 'price': 2.75},
                'C3': {'item': 'White Chocolate', 'price': 2.25},
            },
            '=====☕ Coffee ☕=====': {
                'D1': {'item': 'Black Coffee', 'price': 1.80},
                'D2': {'item': 'Latte', 'price': 2.20},
                'D3': {'item': 'Cappuccino', 'price': 2.50},
            },
            '=====🍵 Tea 🍵=====': {
                'E1': {'item': 'Green Tea', 'price': 1.50},
                'E2': {'item': 'Black Tea', 'price': 1.25},
                'E3': {'item': 'Chai Tea', 'price': 2.00},
            }
        }
            # The suggestion for selected items in the main category
        self.suggestions = {
            '=====🥤 Soda 🥤=====': {
                'Cola': 'How about trying a different soda next time?',
                'Sprite': 'Consider pairing it with some chips!',
                'Fanta': 'Try a chocolate bar for a sweet treat!'
            },
            '=====🍟 Chips 🍟=====': {
                'Classic Potato Chips': 'Pair it with your favorite soda!',
                'Barbecue Chips': 'Consider a sweet chocolate bar to balance the flavors!'
            },
            '====🍫 Chocolate 🍫====': {
                'Milk Chocolate': 'Enjoy it with a cup of coffee!',
                'Dark Chocolate': 'Pair it with a black tea for a delightful combination!'
            },
            '=====☕ Coffee ☕=====': {
                'Black Coffee': 'How about a chocolate bar for a sweet contrast?',
                'Cappuccino': 'Consider a chocolate bar for a rich experience!'
            },
            '=====🍵 Tea 🍵=====': {
                'Green Tea': 'Pair it with a light snack like chips!',
                'Black Tea': 'Consider trying a chocolate bar!',
                'Chai Tea': 'How about some chips to go with your tea?'
            }
        }
        self.balance = 0   #  The user's current balance and 
        self.total_change = 0 # Total change to be returned after a purchase

    def accept_money(self): # The method to accept user input for money and update the balance
        try:
            amount = float(input(f"{Fore.WHITE}{Style.BRIGHT}Please Insert Money:{Fore.GREEN}{Style.BRIGHT} $"))
            self.balance += amount
            print(f"Balance: ${self.balance:.2f}")
        except ValueError:
            print(f"{Fore.RED}{Style.BRIGHT}Invalid input. Please enter a valid amount.")
            self.accept_money()

    def display_menu(self): # The method to display the vending machine menu with categories, items, and prices
        print(f"{Fore.MAGENTA}╔════════════════════════════════════════════════════════╗")
        print(f"{Fore.MAGENTA}║                    {Fore.GREEN}{Style.BRIGHT} Vending Machine   {Fore.MAGENTA}                 ║")
        print(f"{Fore.MAGENTA}╠════════════════════════════════════════════════════════╣")
        for category, items in self.menu.items():
            print(f"{Fore.MAGENTA}║ {Fore.BLUE}{category:^40}{Style.BRIGHT}             {Fore.MAGENTA}║")
            for code, item_info in items.items():
                print(f"║   {Fore.YELLOW}{Style.BRIGHT}{code}:{Style.RESET_ALL} {Fore.WHITE}{item_info['item']:<32} {Fore.GREEN}${Style.BRIGHT}{Fore.RED}{item_info['price']:.2f}{Style.BRIGHT}{Fore.MAGENTA}           ║")
        print(f"{Fore.MAGENTA}╚════════════════════════════════════════════════════════╝")



    def select_item(self): # The method to prompt the user to enter the code for the item they want to purchase
        while True:
            code = input(f"Enter the item code you want to purchase:{Fore.YELLOW}{Style.BRIGHT} ")
            for category, items in self.menu.items():
                if code in items:
                    return code
            print(f"{Fore.RED}{Style.BRIGHT}Invalid code. Please enter a valid code.")

    def display_loading(self, duration=2): # The method to simulate a delay or loading before your purchase comes out
        print("\nProcessing your purchase...")
        time.sleep(duration)
        print("Purchase complete!\n")


    def calculate_change(self, code): # The method to calculate the change to be returned based on the selected item and user's balance
        for category, items in self.menu.items():
            if code in items:
                item_price = items[code]['price']
                if self.balance >= item_price:
                    return self.balance - item_price
                else:
                    print(f"{Fore.RED}{Style.BRIGHT}Transaction canceled. Insufficient funds.")
                    if self.balance < 1 or item_price - self.balance < 13:
                        self.accept_money()
                        return self.calculate_change(code)



    def return_change(self, change, duration=3): # The method for returning the user's change
        if change > 0:
            time.sleep(duration)
            print(f"{Fore.YELLOW}{Style.BRIGHT}Change:{Fore.GREEN}{Style.BRIGHT} ${change:.2f} {Fore.WHITE}{Style.BRIGHT}Thank you for using the vending machine!")

    def dispense_item(self, code, duration=3): # The method to simulate dispensing the selected item and provide suggestions
        for category, items in self.menu.items():
            if code in items:
                item_info = items[code]
                time.sleep(duration)
                print(f"\nDispensing {Fore.GREEN}{item_info['item']}{Style.RESET_ALL}{Fore.WHITE}{Style.BRIGHT}... Enjoy!")

                # Add suggestion based on the category and item
                category_suggestions = self.suggestions.get(category, {})
                item_suggestion = category_suggestions.get(item_info['item'], '')

                if item_suggestion:
                    print(f"{Fore.YELLOW}Purchase Suggestion:{Fore.BLUE}{Style.BRIGHT}{item_suggestion}")
                break



    def operate(self): # The main method of executing the vending machine code
        while True:
            self.accept_money()
            self.display_menu()

            selected_item = self.select_item()
            self.display_loading()

            change = self.calculate_change(selected_item)
            if change == 0:
                continue

            self.total_change = change
            self.balance += change

            self.return_change(change)
            self.dispense_item(selected_item)

            another_purchase = input(f"\n{Fore.WHITE}Do you want to make another purchase? ({Fore.GREEN}{Style.BRIGHT}y{Fore.WHITE}/{Fore.RED}{Style.BRIGHT}n{Fore.WHITE}): ").lower()
            if another_purchase != 'y':
                print(f"\n{Fore.WHITE}Total remaining change: {Fore.GREEN}{Style.BRIGHT}${self.total_change:.2f} {Fore.WHITE}Thank you for using the vending machine. Goodbye!")
                print(f"{Fore.MAGENTA}══════════════════════════════════════════════════════════════════════════════")
                break
            else:
                # Resets the balance and total_change for the next purchase
                self.balance = 0
                self.total_change = 0

# Example usage
if __name__ == "__main__":
    vending_machine = VendingMachine()
    print("Welcome To My Vending Machine!!!")
    vending_machine.operate()

