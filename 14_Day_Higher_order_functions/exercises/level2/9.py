#Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

def get_string_lists(lst):
    # The lambda checks each item individually
    return list(filter(lambda item: isinstance(item, str), lst))

# Example usage:
mixed_list = [1, 'hello', True, 3.14, 'world']
print(get_string_lists(mixed_list)) 

