import time
from prepare_consolidation import prepare_consolidation

print("\n" + "🔹" * 43)
print("\n" + "~" * 30 + " Source Code Consolidator " + "~" * 30)

while True:

    print("\n🔹 1 - To prepare consolidation")
    print("🔹 2 - Get some orientation")
    print("🔹 3 - Close program")

    user_choice = input("\n  🟡 Enter an option (1, 2, or 3): ")

    try:

        if user_choice == "1":
            prepare_consolidation()

        elif user_choice == "2":
            pass

        elif user_choice == "3":

            clock_icons = ["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"]
            print("")

            for clock in clock_icons:
                print(f"\r    🟢 Closing program... {clock} ", end="")
                time.sleep(0.2)

            print("")
            print("\n      🟢 Program Closed Successfully")
            print("\n" + "🔹" * 43)
            break

    except ValueError:
        print("\n    🔴 Invalid option. Enter a valid input (1, 2, or 3)")
