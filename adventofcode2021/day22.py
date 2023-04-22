with open("input/day22.txt") as f:
    input = [l.strip() for l in f.readlines()]
    region = ["x=-50..50,y=-50..50,z=-50..50"]

    def parse(input):
        directions = []
        if len(input) == 1:
            region = True
        else:
            region = False
        for line in input:
            adddirection = []
            if not region:
                onoff, bounds = line.split(" ")
                adddirection += [onoff]
            else:
                bounds = line
            bounds = bounds.split(",")
            for bound in bounds:
                axis, strlimits = bound.split("=")
                strlimits = strlimits.split("..")
                limits = []
                for i in strlimits:
                    limits += [int(i)]
                adddirection += [limits]
            directions += [adddirection]
        if not region:
            return directions
        else:
            return directions[0]

    def snip(directions, region):
        snipped = []
        for step in directions:
            current = step[1:]
            inrange = True
            for a, axis in enumerate(current):
                if axis[0] > region[a][1] or axis[1] < region[a][0]:
                    inrange = False
                else:
                    if axis[0] < region[a][0]:
                        current[a][0] = region[a][0]
                    if axis[1] > region[a][1]:
                        current[a][1] = region[a][1]
            if inrange:
                snipped += [[step[0], current[0], current[1], current[2]]]
        return snipped

    def intersection(cube1, cube2):
        minx = max(cube1[0][0], cube2[0][0])
        maxx = min(cube1[0][1], cube2[0][1])
        miny = max(cube1[1][0], cube2[1][0])
        maxy = min(cube1[1][1], cube2[1][1])
        minz = max(cube1[2][0], cube2[2][0])
        maxz = min(cube1[2][1], cube2[2][1])
        if minx > maxx or miny > maxy or minz > maxz:
            return False
        return [[minx, maxx], [miny, maxy], [minz, maxz]]

    def inclusivevolume(cube):
        x = cube[0][1] - cube[0][0] + 1
        y = cube[1][1] - cube[1][0] + 1
        z = cube[2][1] - cube[2][0] + 1
        volume = x * y * z
        return volume

    def reboot(directions, region=False):
        if region:
            directions = snip(parse(directions), parse(region))
        else:
            directions = parse(directions)
        on = 0
        directions.reverse()
        usedcubes = []
        for direction in directions:
            onoff, x, y, z = direction
            if onoff == "off":
                usedcubes += [[x, y, z]]
            elif onoff == "on":
                oncubes = []
                offcubes = []
                shadowcubes = []
                for cube in usedcubes:
                    i = intersection(cube, [x, y, z])
                    if i:
                        shadowcubes += [i]
                for shadow in shadowcubes:
                    addoncubes = []
                    addoffcubes = [shadow]
                    for cube in oncubes:
                        i = intersection(cube, shadow)
                        if i:
                            addoffcubes += [i]
                    for cube in offcubes:
                        i = intersection(cube, shadow)
                        if i:
                            addoncubes += [i]
                    oncubes += addoncubes
                    offcubes += addoffcubes
                oncubes += [[x, y, z]]
                for c in oncubes:
                    on += inclusivevolume(c)
                for c in offcubes:
                    on -= inclusivevolume(c)
                usedcubes += [[x, y, z]]
            else:
                raise Exception("not any onoff???")
        return on

        # reverse directions
        # make list of 'used cubes'
        # if off
        # just add it to the list of used cubes
        # if on
        # in a fresh on/off space
        # go through all the used cubes and see if it overlaps with any of them (keep a list)
        # for each overlapping cube/segments
        # add an off cube
        # add opposite cubes for any interactions
        # add the original on cube as a single on cube

        # SCORING
        # add all the ons as + and the offs as -

        # forget all these ons and offs
        # add the cube to the 'used cubes' list

    print("Task 1:", reboot(input, region))
    print("Task 2:", reboot(input))

# Task 1: 648023
# Task 2: 1285677377848549
