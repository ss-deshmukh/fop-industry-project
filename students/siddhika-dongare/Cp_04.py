#problem1
def print_menu():
    print("=== Calculator Menu ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
Print_menu()

#problem2
def show_history(history):
    if len(history) == 0:
        print("No history yet.")
    else:
        print("--- Session History ---")
        i = 1
        while i <= len(history):
            print(f"[{i}] {history[i - 1]}")
            i += 1
history = [
    "Added 1 subject(s)",
    "Viewed report"
]

show_history(history)
