# math_operations.py

def divide_numbers(a, b):
    """Divides two numbers and returns the result."""
    if b == 0:
        print('Cannot divide by 0')
        return None
    return a / b  # Potential division by zero error

def extra_credit():
    print('I want extra credit like jesus wants love, I want extra credit like how the thirsty being wants water, I want extra credit because I bombed the first quiz and this class is my Only B')

if __name__ == "__main__":
    x = 10
    y = 0
    result = divide_numbers(x, y)
    print(f"The result of division is: {result}")
    extra_credit()