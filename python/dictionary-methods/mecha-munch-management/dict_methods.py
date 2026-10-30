"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """

    for item in items_to_add:
        if item not in current_cart:
            current_cart.setdefault(item, 1)
        else:
            current_cart[item] += 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """

    result = {}
    for note in notes:
        if note not in result:
            result[note] = 1
        else:
            result[note] += 1
    return result


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """

    for name, ingredients in recipe_updates:
        ideas[name] = ingredients

    return ideas


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """

    result = {}
    for key, value in cart.items():
        if key in aisle_mapping:
            result[key] = [value] + aisle_mapping[key]
    return dict(sorted(result.items(), reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order."""

    for key, value in fulfillment_cart.items():
        if key in store_inventory:
            ordered = value[0]
            available = store_inventory[key][0]

            if available > ordered:
                store_inventory[key][0] = available - ordered
            else:
                store_inventory[key][0] = 'Out of Stock'

    return store_inventory