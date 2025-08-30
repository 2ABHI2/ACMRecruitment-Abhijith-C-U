def rotate_and_convert(binary_str, k, direction="left"):
    n = len(binary_str)
    k = k % n 
    if direction == "left":
        rotated = binary_str[k:] + binary_str[:k]
    else:
        rotated = binary_str[-k:] + binary_str[:-k]

    return int(rotated, 2)
#examples
print(rotate_and_convert("1011", 1, "left"))  
print(rotate_and_convert("1011", 2, "right")) 