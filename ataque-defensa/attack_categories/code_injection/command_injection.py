
import os

def perform_command_injection(user_input):
    os.system(f"ping -c 1 {user_input}")

perform_command_injection("localhost; echo 'Injected Command'")
