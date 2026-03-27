def validate_bet(user_input, balance):
    try:
        bet = int(user_input)
    except ValueError:
        return False, "Invalid input ! Please enter whole number"
    
    if bet<= 0:
        return False, "Bte must be greater than zero!"
    
    if bet> balance:
        return False, f"You dont have enough money! Your balance is ${balance}"
    
    return True, bet

def validate_action(action):
    if action.lower() in ['h','s']:
        return True
    return False