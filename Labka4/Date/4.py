def date_difference_in_seconds(date1, date2):
    return abs((date2 - date1).total_seconds())

date1 = datetime(2024, 2, 1, 12, 0, 0)
date2 = datetime(2024, 2, 2, 14, 30, 0)
print("Difference in seconds:", date_difference_in_seconds(date1, date2))

