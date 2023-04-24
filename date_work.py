def season_and_sign(month, day):
    if month == 1 or month == 2 or month == 12:
        season = 'Winter'
    elif month == 3 or month == 4 or month == 5:
        season = 'Sping'
    elif month == 6 or month == 7 or month == 8:
        season = 'Summer'
    elif month == 9 or month == 10 or month == 11:
        season = 'Autumn'
    else:
        print('Error')

    if month == 1:
        if day < 20:
            sign = "Capricorn"
        else:
            sign = "Aquarius"
    elif month == 2:
        if day < 19:
            sign = "Aquarius"
        else:
            sign = "Pisces"
    elif month == 3:
        if day < 21:
            sign = "Pisces"
        else:
            sign = "Aries"
    elif month == 4:
        if day < 20:
            sign = "Aries"
        else:
            sign = "Taurus"
    elif month == 5:
        if day < 21:
            sign = "Taurus"
        else:
            sign = "Gemini"
    elif month == 6:
        if day < 21:
            sign = "Gemini"
        else:
            sign = "Cancer"
    elif month == 7:
        if day < 23:
            sign = "Cancer"
        else:
            sign = "Leo"
    elif month == 8:
        if day < 23:
            sign = "Leo"
        else:
            sign = "Virgo"
    elif month == 9:
        if day < 23:
            sign = "Virgo"
        else:
            sign = "Libra"
    elif month == 10:
        if day < 23:
            sign = "Libra"
        else:
            sign = "Scorpio"
    elif month == 11:
        if day < 22:
            sign = "Scorpio"
        else:
            sign = "Sagittarius"
    else:
        if day < 22:
            sign = "Sagittarius"
        else:
            sign = "Capricorn"
    result = [season, sign]
    return result
