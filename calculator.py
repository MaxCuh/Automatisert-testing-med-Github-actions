def add(a, b): 
    """Legg sammen to tall""" 
    return a + b 
 
def subtract(a, b): 
    """Trekk fra to tall""" 
    return a - b 
 
def multiply(a, b): 
    """Multipliser to tall""" 
    return a * b 
 
def divide(a, b): 
    """Divider to tall""" 
    if b == 0: 
        raise ValueError("Kan ikke dividere med null") 
    return a / b 
    