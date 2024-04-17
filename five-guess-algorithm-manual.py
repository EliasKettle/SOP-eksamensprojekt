import random

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
    print("Velkommen til Mastermind.")
    print("Farver er tal i dette spil. Skriv et 4-cifret tal, f.eks. 1436. Tal kan godt gentages.")
    secret_number = input("Skriv din kode: ")

    if not secret_number.isdigit() or len(secret_number) != 4 or not all(
            '1' <= digit <= '6' for digit in secret_number):
        print("For mange/få cifre. Skriv et 4-cifret tal med tallene 1-6.")
        return

    possible_solutions = generate_possible_solutions()
    guess_count = 0

    while True:
        guess = make_guess(possible_solutions, guess_count)
        print("Jeg gætter:", guess)

        correct_input = input("Hvor mange tal er korrekt placeret?: ")
        misplaced_input = input("Hvor mange tal er rigtige men sidder forkert?: ")

        try:
            correct_digits = int(correct_input)
            misplaced_digits = int(misplaced_input)
        except ValueError:
            print("Ugyldigt input. Skriv heltal.")
            break

        if correct_digits < 0 or correct_digits > 4 or misplaced_digits < 0 or misplaced_digits > 4 or correct_digits + misplaced_digits > 4:
            print("For højt tal. Summen af korrekte og forkerte placeret tal kan ikke være større end 4.")
            break

        guess_count += 1

        if correct_digits == 4:
            print("Jeg gættede din kode", secret_number, "på", guess_count, "gæt!")
            break


        if guess_count == 6:
            print("Jeg gættede ikke din kode")
            break

        remove_impossible_solutions(possible_solutions, guess, (correct_digits, misplaced_digits))


if __name__ == "__main__":
    main()
