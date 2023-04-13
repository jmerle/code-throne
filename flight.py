import sys
from dataclasses import dataclass
from queue import PriorityQueue
from typing import Optional

# Usage: python flight.py < flight-input.txt
# Where flight.py is this file and flight-input.txt contains the challenge's input

@dataclass
class Flight:
    destination: "City"
    price: int

@dataclass(order=True)
class City:
    total_price: int

    id: int
    flights: list[Flight]

    previous_city: Optional["City"] = None

def main() -> None:
    data = sys.stdin.read().strip()

    cities = [City(1e9, i + 1, []) for i in range(100)]
    for line in data.splitlines():
        a, b, price = map(int, line.split(" "))
        a, b = cities[a - 1], cities[b - 1]

        a.flights.append(Flight(b, price))
        b.flights.append(Flight(a, price))

    cities[0].total_price = 0

    queue = PriorityQueue()
    queue.put(cities[0])

    while not queue.empty():
        current_city = queue.get()

        if current_city.id == len(cities):
            break

        for flight in current_city.flights:
            new_price = current_city.total_price + flight.price
            if new_price < flight.destination.total_price:
                flight.destination.total_price = new_price
                flight.destination.previous_city = current_city
                queue.put(flight.destination)

    answer = []

    current_city = cities[-1]
    while current_city is not None:
        answer.append(current_city.id)
        current_city = current_city.previous_city

    print(" ".join(str(id) for id in reversed(answer)))

if __name__ == "__main__":
    main()
