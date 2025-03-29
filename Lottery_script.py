import random

def generate_lottery_numbers():
    """Generate 6 random numbers (1-6), replacing 0 with 1"""
    numbers = [random.randint(0, 6) for _ in range(6)]
    numbers = [num + 1 if num == 0 else num for num in numbers]  # Convert 0 to 1
    return numbers

# Store lottery history
lottery_history = []

# Run for multiple days (e.g., 10 days)
for day in range(10):
    new_numbers = generate_lottery_numbers()
    
    # Check matches with the previous day's numbers
    if lottery_history:
        last_day_numbers = lottery_history[-1]
        matched_numbers = set(new_numbers) & set(last_day_numbers)  # Find matches
    
        print(f"Day {day + 1}: {new_numbers} | Matched with previous day: {matched_numbers}")
    else:
        print(f"Day {day + 1}: {new_numbers} | First day, no previous match")
    
    # Store new numbers
    lottery_history.append(new_numbers)