import re
import timeit

with open("2023/Day5/input.txt") as f:
    input = f.read().split("\n\n")


maps = [
    {
        "name": s.split("\n")[0],
        "maps": [
            {
                "destination start": int(key.split()[0]),
                "destination range": range(
                    int(key.split()[0]), int(key.split()[0]) + int(key.split()[2])
                ),
                "source start": int(key.split()[1]),
                "source range": range(
                    int(key.split()[1]), int(key.split()[1]) + int(key.split()[2])
                ),
            }
            for key in s.split("\n")[1:]
            if key != ""
        ],
    }
    for s in input
]

seeds = [int(x) for x in maps[0]["name"].split(":")[1].split()]
maps = maps[1:]

locations = []
for seed in seeds:
    initial_destination = seed
    values = [seed]
    for map in maps:
        print(f"Current destination: {initial_destination}")
        print(f"Map name: {map['name']}")
        count_of_matches = 0
        for line in map["maps"]:
            if initial_destination in line["source range"]:
                count_of_matches += 1
                assert count_of_matches <= 1
                destination = (
                    initial_destination
                    - line["source start"]
                    + line["destination start"]
                )

        if count_of_matches == 0:
            print(
                f"{destination} not found in map {map['name']}, destination unchanged"
            )
        else:
            print(
                f"{initial_destination} found in map {map['name']}, destination changed to {destination}"
            )
            initial_destination = destination
        values.append(destination)

    print(f"{values}")
    locations.append(values[-1])


print(min(locations))

new_seed_list = [
    range(seeds[x], seeds[x] + seeds[x + 1]) for x in range(0, len(seeds) - 1, 2)
]


location_maps = maps[-1]["maps"]


new_ranges_to_check = []
for location_map in location_maps:
    range_of_destinations = location_map["destination range"]
    new_ranges_to_check.append(location_map["source range"])

# check if second


def invert_map(map):
    new_map = []
    for line in map:
        new_map.append(
            {
                "destination start": line["source start"],
                "destination range": line["source range"],
                "source start": line["destination start"],
                "source range": line["destination range"],
            }
        )
    return new_map


def find_min_seeds(range_obj):
    locations = []
    for seed in range_obj:
        initial_destination = seed
        values = [seed]
        for map in maps:
            count_of_matches = 0
            for line in map["maps"]:
                if initial_destination in line["source range"]:
                    count_of_matches += 1
                    assert count_of_matches <= 1
                    destination = (
                        initial_destination
                        - line["source start"]
                        + line["destination start"]
                    )

            if count_of_matches == 0:
                pass
                # print(
                #     f"{destination} not found in map {map['name']}, destination unchanged"
                # )
            else:
                # print(
                #     f"{initial_destination} found in map {map['name']}, destination changed to {destination}"
                # )
                initial_destination = destination
            values.append(destination)

        # print(f"{values}")
        locations.append(values[-1])
    print(f"seed range {range_obj} has min location {min(locations)}")
    return min(locations)


mins = []
for seed_range in new_seed_list:
    mins.append(find_min_seeds(seed_range))

print(min(mins))
