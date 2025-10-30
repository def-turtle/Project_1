import random
import string
import time

# Quick benchmark
chars = list(string.ascii_letters)
start = time.time()
attempts = 0

while time.time() - start < 2.0:  # Run for 2 seconds
    ''.join(random.choices(chars, k=4))
    attempts += 1

rate = attempts / 2.0
print(f"🐍 PyCharm Performance Test:")
print(f"📊 {rate:,.0f} guesses per second")
print(f"💻 This is your actual speed in PyCharm")