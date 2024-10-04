
import itertools

def password_bruteforce(charset, max_length, target_password):
    for length in range(1, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            attempt = ''.join(attempt)
            print(f"Trying password: {attempt}")
            if attempt == target_password:
                print(f"Password found: {attempt}")
                return

password_bruteforce("abc123", 6, "abc")
