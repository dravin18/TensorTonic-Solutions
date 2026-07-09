def rgb_to_grayscale(image):
    """
    Returns: 2D list of shape (H, W) with luma values rounded to 4 decimals
    """
    output = []
    for img in image:
        gray = []
        for cell in img:
                gray.append(cell[0] * 0.299 + cell[1] * 0.587 + cell[2] * 0.114)
        output.append(gray)
    return output