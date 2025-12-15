def count_zero_clicks(rotations):
    pos = 50
    zero_count = 0

    for rot in rotations:
        direction = rot[0]
        steps = int(rot[1:])

        if steps == 0:
            continue

        if direction == "R":
            # distance from current position to next 0 going right
            dist_to_zero = (100 - pos) % 100
        else:  # 'L'
            # distance from current position to next 0 going left
            dist_to_zero = pos % 100

        # If we reach 0 at least once
        if steps >= dist_to_zero + 1:
            remaining = steps - (dist_to_zero + 1)
            zero_count += 1  # first time hitting 0
            zero_count += remaining // 100  # full extra loops

        # Update position
        if direction == "R":
            pos = (pos + steps) % 100
        else:
            pos = (pos - steps) % 100

    return zero_count


# Read input
with open("./01_input.txt") as f:
    rotations = [line.strip() for line in f if line.strip()]

print(count_zero_clicks(rotations))
