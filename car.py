import sys
from dataclasses import dataclass

# Usage: python car.py < car-input.txt
# Where car.py is this file and car-input.txt contains the challenge's input

@dataclass
class Person:
    id: int
    start: int
    end: int
    days: set[int]

def main() -> None:
    data = sys.stdin.read().strip()

    persons = []
    for line in data.splitlines():
        id, start, end = map(int, line.split(" "))
        persons.append(Person(id, start, end, set(range(start, end + 1))))

    answer = []
    for person in sorted(persons, key=lambda person: -len(person.days)):
            if not any(len(person.days & other.days) > 0 for other in answer):
                answer.append(person)

    print(" ".join(str(id) for id in sorted(person.id for person in answer)))
    print(f"{sum(len(person.days) for person in answer)} days")

if __name__ == "__main__":
    main()
