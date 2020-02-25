START_TRACKING_BINDING = ("control", "s")

with open("params.conf", "r") as config:
    for line in config:
        if line.startswith("#"):
            continue

        split = line.rstrip().split("=")
        lhs = split[0]
        rhs = split[1]

        if lhs == "start_tracking":
            keys = rhs.split("-")
            if len(keys) == 1:
                START_TRACKING_BINDING = rhs
            else:
                START_TRACKING_BINDING = tuple(keys)
