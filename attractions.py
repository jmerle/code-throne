import sys
from dataclasses import dataclass

# Usage: python attractions.py < attractions-input.txt
# Where attractions.py is this file and attractions-input.txt contains the challenge's input

@dataclass
class Artist:
    id: int
    minutes: int
    earnings: int

def main() -> None:
    data = sys.stdin.read().strip()

    artists = []
    for line in data.splitlines():
        id, duration, earnings = line.split(" ")
        id, earnings = int(id), int(earnings)

        hours, minutes = map(int, duration.split(":"))
        minutes += hours * 60

        artists.append(Artist(id, minutes, earnings))

    dp = [[0 for _ in range(751)] for _ in range(len(artists) + 1)]

    for y in range(len(artists) + 1):
        for x in range(751):
            if y == 0 or x == 0:
                continue

            artist = artists[y - 1]
            if artist.minutes > x:
                dp[y][x] = dp[y - 1][x]
            else:
                dp[y][x] = max(dp[y - 1][x], dp[y - 1][x - artist.minutes] + artist.earnings)

    answer = []

    minutes_left = 750
    for y in range(len(artists), 0, -1):
        if dp[y][minutes_left] > dp[y - 1][minutes_left]:
            artist = artists[y - 1]
            answer.append(artist)
            minutes_left -= artist.minutes

    print(" ".join(str(artist.id) for artist in reversed(answer)))

if __name__ == "__main__":
    main()
