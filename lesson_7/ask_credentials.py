import argparse
import hashlib
from getpass import getpass

HASH = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"

def ask_pass():
    clear_password = getpass()
    hashed_password = hashlib.sha256(clear_password.encode())
    return hashed_password.hexdigest()

def main():
    global HASH
    parser = argparse.ArgumentParser(description="Ask for login credentials")
    parser.add_argument("-u", "--user", help="User name to login with", type=str, default="root")
    parser_args = parser.parse_args()
    user = parser_args.user
    pass_hash = ask_pass()

    if pass_hash == HASH:
        print("Access granted for user: {}".format(user))
    else:
        print("Access denied for user: {}".format(user))

if __name__ == "__main__":
    main()
