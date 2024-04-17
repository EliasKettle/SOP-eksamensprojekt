import random


def generate_secret_number():
    return ''.join(str(random.randint(1, 6)) for _ in range(4))


def generate_possible_solutions():
    possible_solutions = []
    for i in range(1111, 6667):
        if all(digit in '123456' for digit in str(i)):
            possible_solutions.append(str(i).zfill(4))
    return possible_solutions


def evaluate_guess(secret, guess):
    correct_digits = sum(a == b for a, b in zip(secret, guess))
    misplaced_digits = sum(min(secret.count(digit), guess.count(digit)) for digit in '123456') - correct_digits
    return correct_digits, misplaced_digits


def remove_impossible_solutions(possible_solutions, guess, evaluation):
    possible_solutions[:] = [solution for solution in possible_solutions if
                             evaluate_guess(solution, guess) == evaluation]


def make_guess(possible_solutions, guess_count):
    if guess_count == 0:
        return '1122'
    else:
        return random.choice(possible_solutions)


def main():
    secret_number = generate_secret_number()
    print(secret_number)
    possible_solutions = generate_possible_solutions()
    guess_count = 0

    while True:
        guess = make_guess(possible_solutions, guess_count)
        print("Gæt:", guess)
        correct_digits, misplaced_digits = evaluate_guess(secret_number, guess)
        print("Korrekt placeret:", correct_digits)
        print("Forkert placeret:", misplaced_digits)
        guess_count += 1

        if correct_digits == 4:
            print("Korrekt", secret_number, "på", guess_count, "gæt")
            break

        if guess_count == 10:
            print("Ikke flere gæt")
            print("Hemmelige kode var", secret_number)
            break

        remove_impossible_solutions(possible_solutions, guess, (correct_digits, misplaced_digits))


if __name__ == "__main__":
    main()
