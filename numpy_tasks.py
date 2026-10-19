"""Заготовки задач на NumPy."""

import numpy as np
from grader_contracts.numpy_tasks import (
    BinarizeInput, ChessInput, EllipseInput, MatrixInput, MatrixStatistics,
    MatrixVectorBatchInput, OneHotInput, RandomMatrixInput, RectangleInput,
    TimeSeriesInput, TimeSeriesStatistics,
)

#1
def sum_prod(data: MatrixVectorBatchInput) -> np.ndarray:
    matrices, vectors = data.matrices, data.vectors
    matrices = np.asarray(matrices)
    vectors = np.asarray(vectors)
    # matrices: (p, n, n), vectors: (p, n, 1) -> products: (p, n, 1)
    products = np.matmul(matrices, vectors)
    return products.sum(axis=0)  # (n, 1)

#2
def binarize(data: BinarizeInput) -> np.ndarray:
    matrix, threshold = data.matrix, data.threshold
    matrix = np.asarray(matrix)
    return (matrix > threshold).astype(int)

#3
def unique_rows(data: MatrixInput) -> list[list[float]]:
    matrix = np.asarray(data.matrix)
    return [list(np.unique(row)) for row in matrix]


def unique_columns(data: MatrixInput) -> list[list[float]]:
    matrix = np.asarray(data.matrix)
    return [list(np.unique(col)) for col in matrix.T]

#4
def matrix_statistics(data: RandomMatrixInput) -> MatrixStatistics:
    rows, columns, mean, std, seed = data.rows, data.columns, data.mean, data.std, data.seed
    rng = np.random.default_rng(seed)
    matrix = rng.normal(loc=mean, scale=std, size=(rows, columns))
    return MatrixStatistics(
        matrix=matrix,
        row_means=matrix.mean(axis=1),
        column_means=matrix.mean(axis=0),
        row_variances=matrix.var(axis=1),
        column_variances=matrix.var(axis=0),
    )

#5
def chess(data: ChessInput) -> np.ndarray:
    rows, columns, first, second = data.rows, data.columns, data.first, data.second
    # i+j even -> first, odd -> second
    i = np.arange(rows)[:, None]
    j = np.arange(columns)[None, :]
    return np.where((i + j) % 2 == 0, first, second)

#6
def draw_rectangle(data: RectangleInput) -> np.ndarray:
    width, height = data.width, data.height
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color

    image = np.empty((image_height, image_width, 3), dtype=np.uint8)
    image[:] = np.asarray(background_color, dtype=np.uint8)

    # rectangle centered
    top = (image_height - height) // 2
    left = (image_width - width) // 2
    image[top:top + height, left:left + width] = np.asarray(shape_color, dtype=np.uint8)
    return image


def draw_ellipse(data: EllipseInput) -> np.ndarray:
    semi_axis_x, semi_axis_y = data.semi_axis_x, data.semi_axis_y
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color

    image = np.empty((image_height, image_width, 3), dtype=np.uint8)
    image[:] = np.asarray(background_color, dtype=np.uint8)

    y0 = (image_height - 1) / 2.0
    x0 = (image_width - 1) / 2.0
    ys, xs = np.mgrid[0:image_height, 0:image_width]
    mask = ((xs - x0) ** 2) / (semi_axis_x ** 2) + ((ys - y0) ** 2) / (semi_axis_y ** 2) <= 1.0
    image[mask] = np.asarray(shape_color, dtype=np.uint8)
    return image

#7
def analyze_time_series(data: TimeSeriesInput) -> TimeSeriesStatistics:
    values, window = np.asarray(data.values, dtype=float), data.window
    mean = float(values.mean())
    variance = float(values.var())
    std = float(values.std())

    if len(values) >= 3:
        local_max = np.where(
            (values[1:-1] > values[:-2]) & (values[1:-1] > values[2:])
        )[0] + 1
        local_min = np.where(
            (values[1:-1] < values[:-2]) & (values[1:-1] < values[2:])
        )[0] + 1
    else:
        local_max = np.array([], dtype=int)
        local_min = np.array([], dtype=int)

    moving_average = np.convolve(values, np.ones(window) / window, mode="valid")

    return TimeSeriesStatistics(
        mean=mean,
        variance=variance,
        std=std,
        local_maxima=local_max.tolist(),
        local_minima=local_min.tolist(),
        moving_average=moving_average,
    )

#8
def one_hot(data: OneHotInput) -> np.ndarray:
    labels = np.asarray(data.labels, dtype=int)
    class_count = data.class_count
    if class_count is None:
        class_count = int(labels.max()) + 1
    result = np.zeros((len(labels), class_count), dtype=int)
    result[np.arange(len(labels)), labels] = 1
    return result