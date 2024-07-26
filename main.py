import hashlib

def convertT(text):
    digest = hashlib.sha1(
        text.encode()
    ).hexdigest()

    return digest


def main():
    user_sha1 = input("Enter the SHA1 to crack: ")
    cleanedUserSHA1 = user_sha1.strip().lower()

    password_found = False

    with open('./passwords.txt') as f:
        for line in f:
            password = line.strip()
            convertedSHA1 = convertT(password)

            if cleanedUserSHA1 == convertedSHA1:
                print(f"password found: {password}")
                password_found = True
                break

    if not password_found:
        print("could not find password")

if __name__ == "__main__":
    main()