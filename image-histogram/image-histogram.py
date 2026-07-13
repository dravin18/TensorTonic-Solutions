def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    rows = len(image)
    cols = len(image[0])
    hist = [0] * 256
    for row in range(rows):
        for col in range(cols):
            hist[image[row][col]] += 1
    return hist