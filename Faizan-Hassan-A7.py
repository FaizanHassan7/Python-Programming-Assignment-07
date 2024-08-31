def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
   
    name = input("Enter your name: ")
    num1 = int(input("Enter your first favorite number: "))
    num2 = int(input("Enter your second favorite number: "))
    num3 = int(input("Enter your third favorite number: "))

   
    favorite_numbers = [num1, num2, num3]

   
    print(f"\nHello, {name}! Let's explore your favorite numbers:")

    
    even_odd_list = [(num, "even" if num % 2 == 0 else "odd") for num in favorite_numbers]
    for num, parity in even_odd_list:
        print(f"The number {num} is {parity}.")

   
    for num in favorite_numbers:
        square_tuple = (num, num**2)
        print(f"The number {num} and its square: {square_tuple}")

    
    total_sum = sum(favorite_numbers)
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

    
    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"The sum {total_sum} is not a prime number.")

if __name__ == "__main__":
    main()
