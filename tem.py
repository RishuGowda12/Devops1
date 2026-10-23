
import random
from datetime import datetime

def run_experiment():
    print("Python Experiment Started!")
    print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    numbers = [random.randint(1, 100) for _ in range(10)]

    print("Generated numbers:", numbers)
    print("Minimum:", min(numbers))
    print("Maximum:", max(numbers))
    print("Average:", sum(numbers) / len(numbers))

if __name__ == "__main__":
    run_experiment()
