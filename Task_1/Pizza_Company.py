def calculate_order_price(num_items, requires_delivery, is_tuesday, uses_app):
    # Constants for pricing and discounts
    item_price = 12
    delivery_cost = 2.5
    discount_tuesday = 0.5
    discount_app = 0.25

    # Apply Tuesday discount if applicable
    if is_tuesday:
        item_price *= (1 - discount_tuesday)

    # Calculate total cost of items
    total_item_cost = num_items * item_price

    # Check if delivery is free (for five or more items)
    if requires_delivery and num_items >= 5:
        delivery_cost = 0

    # Add delivery cost only if it's required
    total_cost = total_item_cost + (delivery_cost if requires_delivery else 0)

    # Apply app discount if the app is used
    if uses_app:
        total_cost *= (1 - discount_app)

    return total_cost


def get_confirmation_input(prompt):
    while True:
        response = input(prompt).lower()
        if response == 'y' or response == 'n':
            return response == 'y'
        else:
            print("Please enter 'y' or 'n' only.")


def main():
    print("BPP Pizza Price Calculator")
    print("==========================\n")
    

    # Gather information about the order
    while True:
        try:
            # Get the number of items in the order
            num_items = int(input("Please enter the number of pizza in your order: "))
            if num_items > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Get user confirmation for delivery, Tuesday, and app usage
    requires_delivery = get_confirmation_input("Do you require delivery? (y/n): ")
    is_tuesday = get_confirmation_input("Is it Tuesday? (y/n): ")
    uses_app = get_confirmation_input("Are you using the App? (y/n): ")

    # Calculate and display the total price
    total_price = calculate_order_price(num_items, requires_delivery, is_tuesday, uses_app)
    print(f"Your total price is: £{total_price:.2f}")


if __name__ == "__main__":
    main()
