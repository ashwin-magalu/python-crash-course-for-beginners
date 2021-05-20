def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()

def get_formatted_name2(first, middle, last):
    full_name = f"{first} {middle} {last}"
    return full_name.title()

""" Responding to a Failed Test
def get_formatted_name2(first, last, middle=''):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
 """