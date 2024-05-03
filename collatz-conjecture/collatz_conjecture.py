def steps(number, counter=0):
    
    if number > 0:   
        if number == 1:
            return counter
        elif number % 2 == 0:
            return steps(number / 2, counter + 1)
        else:
            return steps(number * 3 + 1, counter + 1)
    else:
        raise ValueError("Only positive integers are allowed")
