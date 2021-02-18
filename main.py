import os

def main():
    nickname = os.getenv("NICKNAME", "")
    
    if nickname == "":
      nickname = "John Doe"

    print("Hello, {0}!".format(nickname))

if __name__ == "__main__":
    main()