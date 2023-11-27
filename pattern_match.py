# -*- coding: transpyler -*-
def print_point(p: tuple[int, int]) -> None:
    match p:
        case (0, 0):
            print("origin")
        case (x, 0):
            print(f"point at x-axis {x}")
        case (0, y):
            print(f"point at y-axis {y}")
        case (x, y) if x == y:
            print(f"point at diagonal {x}")
        case (x, y):
            print(f"point at {x}, {y}")


print_point((0, 0))
print_point((10, 0))
print_point((0, 10))
print_point((10, 10))
print_point((10, 20))
