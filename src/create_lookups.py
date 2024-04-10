import json
from collections import namedtuple

import numpy as np

Coord = namedtuple("Coord", ["x", "y"])


def create_untransformed_matrix() -> np.ndarray:
    raster = np.empty(40000, dtype=object).reshape(200, 200)
    for x in range(1, 201):
        for y in range(1, 201):
            raster[x - 1][y - 1] = Coord(x=x, y=y)
    return raster


def create_lookups(
    untransformed: np.ndarray, transformed: np.ndarray
) -> tuple[dict, dict]:
    x_lookup = {}
    y_lookup = {}
    for x in range(200):
        for y in range(200):
            x_lookup[untransformed[x][y].x] = transformed[x][y].x
            y_lookup[untransformed[x][y].y] = transformed[x][y].y
    return x_lookup, y_lookup


if __name__ == "__main__":
    untransformed = create_untransformed_matrix()
    transformed = np.flip(np.rot90(untransformed, k=2), axis=1)

    x_lookup, y_lookup = create_lookups(untransformed, transformed)
    with open("../output/x_lookup.json", "w") as fp:
        json.dump(x_lookup, fp)
    with open("../output/y_lookup.json", "w") as fp:
        json.dump(y_lookup, fp)
