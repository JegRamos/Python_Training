# functions
def flip_coin(guess) :
    from random import randint
    
    coin_sides = [ "heads", "tails" ]
    coin_result = coin_sides[randint(0, 1)]
    guess_result = None
    guess = guess.lower()
    
    if guess not in coin_sides :
        print("Invalid input!")
        return None
    elif guess == coin_result  :
        guess_result = "Winner"
    else : 
        guess_result = "Loser"
        
    result = (coin_result, guess_result)
    print_results(result)

def print_results(result) :
    coin_side = result[0]
    guess = result[1]
    print(f"It's {coin_side.capitalize()}! you are a {guess.upper()}!")

# main
flip_coin("tAiLs")


