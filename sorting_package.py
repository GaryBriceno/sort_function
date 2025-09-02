def sort(width, height, length, mass):
    """
        Classifies a package as STANDARD, SPECIAL, or REJECTED
        based on its dimensions (cm) and mass (kg).
    """
    max_length = 150
    max_volume = 1_000_000
    max_mass = 20

    volume = width * height * length

    if (width >= max_length or height >= max_length or length >= max_length) or volume >= max_volume :
        if mass >= max_mass:
            return "REJECTED"
        else:
            return "SPECIAL"
    else:
        if mass >= max_mass:
            return "SPECIAL"

    return "STANDARD"

