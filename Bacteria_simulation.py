import random
import time

def function():

    bacteria_number = 1
    i = 0

    while i < 20 and bacteria_number != 0:
        for j in range(bacteria_number):
            number = random.randint(0, 3)
            if number == 3:
                bacteria_number -= 1
            else:
                bacteria_number += number
        i += 1
    return bacteria_number


if __name__ == "__main__":
    time_start = time.time()
    i = 0
    number_extinct = 0
    iterations = 10000
    while i <= iterations:
        extinct = function()
        if extinct == 0:
            number_extinct += 1
        i += 1
    time_ended = round(time.time() - time_start, 2)
    probability = number_extinct/iterations
    error = round(abs(((probability - 0.411)/0.411))*100, 2)
    print(f'The probability is: {probability}, the simulation took {time_ended} seconds, and the error is: {error}%')

