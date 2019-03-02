def computeDistance(height, index, bounces):
    total = 0
    for x in range(bounces):
        total += height
        height *= index
        total += height
    return total

def main():
    while True:
        print("1 Compute the total distance") 
        print("2 Quit the program\n")
        command = input("Enter a number: ")
        if not command in ("1", "2"):
            print("Error: unrecognized command")
        elif command == "1":
            height = float(input("\nEnter the initial height: "))
            index = float(input("Enter the bounciness index: "))
            bounces = int(input("Enter the number of bounces: "))
            distance = computeDistance(height, index, bounces)
            print("\nThe distance is", distance, "\n")
        else:
            break

main()

