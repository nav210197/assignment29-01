zander = float(input("Enter the length of the zander in centimeters: "))

size_limit = 42

if zander >= size_limit:
     print("Congratulations! You can keep the zander.")
else:
    below_limit = size_limit - zander
    print(
        f"Oops! The zander is too small. Release it back into the lake. It's {below_limit:.f} centimeters below the size limit.")