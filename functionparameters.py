def safarimidclass(name, age, gender):
    print(f"My name is {name} I am {age}"
          f"years old and I am {gender}")


safarimidclass("Kindo", 18, "female")
safarimidclass("Gift", 38, "trans")
safarimidclass("Lily", 8, "female")
safarimidclass("Nick", 22, "male")


def is_palindrome():
    word = input("Enter a word:")
    if word == word[::-1]:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")


is_palindrome()


def num_palindrome():
    number = int(input("Enter a number"))
    if number == number:
        print(f"{number} is a palindrome")
    else:
        print(f"{number} is not a palindrome")


num_palindrome()
