def clip(value, lower, upper):
    """Clip a given value between a lower and upper bound.
    """
    return lower if value < lower else upper if value > upper else value


def pad_bbox(box, padding=20, max_width=512):
    """Pad a bounding box.

    box: `list [`tuple` [int, int], `tuple` [int, int]]
        Bounding box as a coordinate pair of top-left and bottom-right corner.
    padding: int, optional
        Amount of padding in pixels to apply. Default is 20.
    max_width: int, optional
        Maximum image width to clamp padded coordinate values. Default is 512.
    """
    tl, br = box
    xmin, ymin = tl
    xmax, ymax = br

    xmin = clip(xmin - padding, 0, max_width)
    ymin = clip(ymin - padding, 0, max_width)

    xmax = clip(xmax + padding, 0, max_width)
    ymax = clip(ymax + padding, 0, max_width)

    return [(xmin, ymin), (xmax, ymax)]
