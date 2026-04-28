def main():
    while True:
        print("1. Show data")
        print("2. Insert data")
        print("3. Delete data")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            print("Showing data...")
        elif choice == "2":
            print("Inserting...")
        elif choice == "3":
            print("Deleting...")
        elif choice == "4":
            break

if __name__ == "__main__":
    main()