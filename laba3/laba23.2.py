orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]


def find_farthest_orbit(orbits):
    s = 0
    for orbit in orbits:
        if orbit[0] == orbit[1]:
            break

        r = 3.14 * orbit[0] * orbit[1]
        if r > s:
            s = r
            answer = orbit

    print(answer)


find_farthest_orbit(orbits)