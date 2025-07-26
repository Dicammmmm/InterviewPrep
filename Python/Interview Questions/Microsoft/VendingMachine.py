from typing import Tuple, Optional

# Create a vending machine class which will take in money and product code and then return the product and the change

# Define the class
class VendingMachine:
    def __init__(self) -> None:
        # When the class is initialized create a list of available products
        # Using a hash map (dictionary) we will have constant lookup time when checking the availability of items - O(1)
        self.products = {
            0:{'Product': 'Cookie', 'Price': 10},
            1:{'Product': 'Soda', 'Price': 5}
        }

    # Time complexity: O(1) - Lookup in the hashmap
    # Space complexity: O(1) - Space doesn't grow with the input size
    # We are taking in money (integer) and productCode (integer) and returning an immutable object Tuple for the answer
    def pay(self, money: int, productCode: int) -> Tuple[str, int]:
        # If the productCode is in the products hashmap we will proceed with the function
        if productCode in self.products:
            # Calculate the change which is money given - the price
            change = money - self.products[productCode]['Price']
            # Return the chosen product and the change in a tuple  
            return (self.products[productCode]['Product'], change)


    # Bonus points for edge case and error handling
    # Time complexity: O(1) - Lookup in the hashmap
    # Space complexity: O(1) - Space doesn't grow with the input size
    # We are taking in money (integer) and productCode (integer) and returning an immutable object Tuple for the answer
    def payBonus(self, money: int, productCode: int) -> Optional[Tuple[str, int]]:

        # If money or the product code are not an integer
        # If your IDE says this code is unreachable it could be due to type hints in the function
        # TYPE HINTS ARE NOT ENFORCED AT RUNTIME
        if not isinstance(money, int) or not isinstance(productCode, int):
            print('Invalid input')
            return None

        # Check if the product code is in the products hash map
        if productCode not in self.products:
            print('Product not available')
            return None

        # Check if the user deposited enough money
        if money < self.products[productCode]['Price']:
            print('Insufficient funds')
            return None
        
        # Calculate the change and return the tuple consisting of the product and the change
        change = money - self.products[productCode]['Price']
        return (self.products[productCode]['Product'], change)