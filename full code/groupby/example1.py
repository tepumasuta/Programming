from itertools import groupby
things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"),
          ("vehicle", "speed boat"), ("vehicle", "school bus")]
for key, group in groupby(things, lambda x: x[0]):
    for thing in group:
        print(f"A {thing[1]} is a {key}.")
    print()

# A bear is a animal.
# A duck is a animal.

# A cactus is a plant.

# A speed boat is a vehicle.
# A school bus is a vehicle.