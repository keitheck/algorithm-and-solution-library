def human_years_cat_years_dog_years(hy):
    """
    Write a function that returns human, cat, and dog years.  For each hunan
    year, cats age 15(first year), 9(second year) and 4 years
    (thereafter), and dogs age 15(first year), 9(second year)
    and 4 years (thereafter).
    """
    if type(hy) is not int:
        raise TypeError('Argument must be integer')
    else:
        if hy == 1:
            return [1, 15, 15]
        if hy == 2:
            return [2, 24, 24]
        cy, dy = 24, 24
        i = 2
        while i < hy:
            cy += 4
            dy += 5
            i += 1
        return [hy, cy, dy]
