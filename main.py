import sys
from modules.emails import sender


if __name__ == "__main__":
    # chedk if an argument was parsed.
    if len(sys.argv) > 1:
        print(sys.argv[1])

    sender("Wahab", "me@gmail.com")
