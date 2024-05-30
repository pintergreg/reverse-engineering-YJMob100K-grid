import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from shapely import Polygon


def plot_heatmap(
    data: np.ndarray,
    figsize: tuple[int, int] = (8, 8),
    dpi: int = 100,
    cmap: str = "coolwarm_r",
) -> tuple[plt.Figure, plt.Axes]:
    fig = plt.figure(figsize=figsize, dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1], frameon=False, xticks=[], yticks=[])
    ax.imshow(data, cmap=cmap, aspect="equal")
    ax.margins(0)
    ax.axis("off")
    fig.patch.set_visible(False)
    return fig, ax


def to_matrix(
    data: pd.DataFrame, shape: tuple[int, int] = (200, 200), value: str = "count"
) -> np.ndarray:
    raster = np.zeros(shape[0] * shape[1]).reshape(shape)
    for r in data.itertuples():
        raster[r.x - 1][r.y - 1] = getattr(r, value)
    return raster


def transform(matrix: np.ndarray) -> np.ndarray:
    rotated = np.rot90(matrix, k=2)
    flipped = np.flip(rotated, axis=1)
    return flipped


def rotate_90_cc(matrix: np.ndarray) -> np.ndarray:
    rotated = np.rot90(matrix, k=1)
    return rotated


def generate_grid(
    minx: float,
    maxx: float,
    miny: float,
    maxy: float,
    stepx: float,
    stepy: float,
    crs: int = 23700,
) -> gpd.GeoDataFrame:
    records = []
    for idx, x in enumerate(np.arange(minx, maxx, stepx)):
        for idy, y in enumerate(np.arange(miny, maxy, stepy)):
            p = Polygon(
                [(x, y), (x + stepx, y), (x + stepx, y + stepy), (x, y + stepy)]
            )
            records.append([p, idx, idy])
    grid = pd.DataFrame.from_records(records, columns=["geometry", "x", "y"])
    grid = gpd.GeoDataFrame(grid, geometry="geometry", crs=crs)
    return grid


def calculate_image_size(
    area_bounds: tuple[float, float, float, float], rx: int, ry: int
) -> tuple[float, float]:
    """
    area_bounds: (minx, miny, maxx, maxy)
    """
    width = (area_bounds[2] - area_bounds[0]) / rx
    height = (area_bounds[3] - area_bounds[1]) / ry
    return width, height


def calculate_top_left_coordinates(area: Polygon, x: int, y: int, rx: int, ry: int):
    return area.bounds[0] + x * rx, area.bounds[3] - y * ry
