
import subprocess

LOG_FILE = "logs/execution.log"

def execute_script(script_path):
    try:
        result = subprocess.run(["python3", script_path], capture_output=True, text=True)
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"Executing {script_path}:\n{result.stdout}\n")
            if result.returncode != 0:
                log_file.write(f"Error: {result.stderr}\n")
        if result.returncode != 0:
            print(f"Error detected in {script_path}: {result.stderr}")
        else:
            print(f"{script_path} executed successfully!")
    except Exception as e:
        print(f"Execution failed: {e}")

def main():
    attack_scripts = [
        "attack_categories/code_injection/sql_injection.py",
        "attack_categories/code_injection/command_injection.py",
    ]
    for attack in attack_scripts:
        execute_script(attack)

if __name__ == "__main__":
    main()
