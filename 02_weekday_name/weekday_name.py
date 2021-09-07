def weekday_name(day_of_week):
    """Return name of weekday.

        >>> weekday_name(1)
        'Sunday'

        >>> weekday_name(7)
        'Saturday'

    For days not between 1 and 7, return None

        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    days = ["Sunday", "Monday", "Tuesday",
            "Wedenesday", "Thursday", "Friday", "Saturday"]
    nums = list(range(1, 8))
    if day_of_week not in nums:
        print("Please enter a valid number")
        return
    else:
        print(days[day_of_week])


weekday_name(6)
