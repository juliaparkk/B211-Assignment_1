import os
import random
import string
import time
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

#Memorable Password Generator
def generate_memorable_password(num_words, case_type, word_list):
    """
    num_words: number of words to include
    case_type: 'lower', 'upper', or 'title'
    word_list: list of available words
    """
    chosen_words = random.sample(word_list, num_words)
    processed_words = []

    for w in chosen_words:
        if case_type == "upper":
            w = w.upper()
        elif case_type == "title":
            w = w.title()
        #lower is default

        w = f"{w}{random.randint(0,9)}"
        processed_words.append(w)

    return "-".join(processed_words)

#Random Password Generator
def generate_random_password(length, include_punct=True, banned_chars=""):
    """
    length: number of characters
    include_punct: include punctuation symbols
    banned_chars: characters NOT allowed
    """
    allowed_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    if include_punct:
        allowed_chars += string.punctuation

    #Remove banned characters
    allowed_chars = "".join([c for c in allowed_chars if c not in banned_chars])

    return "".join(random.choice(allowed_chars) for _ in range(length))

#Logging Function
def log_password(password, folder_name):
    ensure_directory(folder_name)
    file_path = os.path.join(folder_name, "Generated_Passwords.txt")

    timestamp = time.ctime(time.time())
    with open(file_path, "a") as f:
        f.write(f"{password} | Created: {timestamp}\n")

#Main Generator Function
def password_generator():
    password_type = input("Choose password type (memorable/random): ").strip().lower()

    if password_type == "memorable":
        num_words = int(input("How many words? "))
        case_type = input("Case type (lower/upper/title): ").strip().lower()

        #Load word list
        with open("top_english_nouns_lower_100000.txt", "r") as f:
            words = [line.strip() for line in f.readlines()]

        pw = generate_memorable_password(num_words, case_type, words)
        log_password(pw, "Memorable")
        print("Generated memorable password:", pw)

    elif password_type == "random":
        length = int(input("Password length: "))
        include_punct = input("Include punctuation? (y/n): ").strip().lower() == "y"
        banned = input("Characters to exclude (optional): ")

        pw = generate_random_password(length, include_punct, banned)
        log_password(pw, "Random")
        print("Generated random password:", pw)

    else:
        print("Invalid type selected.")

#Bulk Test: Generate 1000 random-type passwords
def generate_1000_test():
    with open("top_english_nouns_lower_100000.txt", "r") as f:
        words = [line.strip() for line in f.readlines()]

    for _ in range(1000):
        pw_type = random.choice(["memorable", "random"])

        if pw_type == "memorable":
            pw = generate_memorable_password(
                num_words=random.randint(2, 4),
                case_type=random.choice(["lower", "upper", "title"]),
                word_list=words
            )
            log_password(pw, "Memorable")

        else:
            pw = generate_random_password(
                length=random.randint(8, 16),
                include_punct=random.choice([True, False]),
                banned_chars=""
            )
            log_password(pw, "Random")

    print("Generated 1000 mixed passwords successfully.")
#Run main program
if __name__ == "__main__":
    generate_1000_test()
    #Uncomment to run interactive generator:
    #password_generator()

    #Uncomment to run 1000-password test:
    #generate_1000_test()