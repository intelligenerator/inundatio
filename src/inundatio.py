import numpy as np
from skimage.morphology import flood


def get_houses(target_image: np.array) -> list:
    """Cut out houses from target data
        Parameters:
        target_image: np.array
            2 D Matrix with target values with values either 0 or 1

        Returns:
        coordiantes_list: list
            Each element represents a bounding box around a house
            (xmin, ymin, xmax, ymax)
    """
    # Clip target_image to values 0, 1
    target_image = np.clip(target_image, a_min=0, a_max=1)

    coordinates_list = []

    # Starting from the top left, search the image for a house
    for i in range(0, len(target_image)):
        for j in range(0, len(target_image[0])):
            if target_image[i][j] == 1:
                # Flood and overlay selected house
                seed_point = (i, j)
                mask = flood(target_image, seed_point)
                mask_int = mask.astype(int)

                # Find X,Y coordinates of all pixels with value 1
                coordinates = np.argwhere(mask_int == 1)
                print('Number of Pixels: ', len(coordinates))

                # Find min and max values for x and y
                y_min, x_min = np.min(coordinates, axis=0)
                y_max, x_max = np.max(coordinates, axis=0)

                # Remove flood filled building from original image
                target_image[mask] = 0

                # Only select larger houses
                if len(coordinates) > 50:
                    coordinates_list.append([(x_min, y_min), (x_max, y_max)])

    return coordinates_list
