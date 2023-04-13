import sys
from dataclasses import dataclass

# Usage: python hostel.py < hostel-input.txt
# Where hostel.py is this file and hostel-input.txt contains the challenge's input

def main() -> None:
    data = sys.stdin.read().strip()

    groups = sorted([int(group) for group in data.split(" ")], reverse=True)

    rooms = []

    for group in groups:
        for room in rooms:
            if sum(room) + group <= 10:
                room.append(group)
                break
        else:
            rooms.append([group])

    for room in rooms:
        print(" ".join(str(group) for group in room))

if __name__ == "__main__":
    main()
