def normalize_image(image, mean, std):
    """
    Returns: 3D list of shape (H, W, C), each value rounded to 4 decimals
    """
    out_img = []
    for img in image:
        new_img = []
        for cell in img:
            new_cell = []
            for col, mu, sigma in zip(cell, mean, std):
                new_cell.append((col - mu) / sigma)
            new_img.append(new_cell)
        out_img.append(new_img)
    return out_img
    
