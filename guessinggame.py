import random

secret_number = random.randint(1, 100)
attempts = 0

print("🎯 Welcome to Number Guessing Game!")
print("👉 Main 1 se 100 ke beech ek number soch raha hoon")
print("👉 Tum guess karo 🙂")

while True:
    guess = input("Apna guess likho: ")

    if not guess.isdigit():
        print("❌ Sirf number likho!")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("📉 Chhota number hai")
    elif guess > secret_number:
        print("📈 Bada number hai")
    else:
        print(f"🎉 Mubarak ho! Tumne {attempts} attempts me sahi guess kiya")
        break
