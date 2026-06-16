def ask_text(prompt):
    return input(prompt)

def ask_int(prompt):
    return int(input(prompt))

def build_bio(name, age, city, language, years):
    divider = "=" * 40
    return (
        f"\n{divider}\n"
        f"            ABOUT ME\n"
        f"{divider}\n"
        f"Name:      {name}\n"
        f"Age:       {age}\n"
        f"City:      {city}\n"
        f"Codes in:  {language}\n"
        f"Coding for {years} years.\n"
        f"{divider}"
    )

def main():
    name = ask_text("What is your name? ")
    age = ask_int("How old are you? ")
    city = ask_text("Which city are you from? ")
    language = ask_text("Favourite programming language? ")
    years = ask_int("How many years have you been coding? ")
    print(build_bio(name, age, city, language, years))

main()
