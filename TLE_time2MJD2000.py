'''
Compute number of seconds since 2000-01-01 12:00:00 (J2000)
This function takes into account leap years, but not leap seconds

Created 2023-06-14 by Oana Nica
'''
def TLE_time2MJD2000(year_input,day_input,n_leap_sec):
    year = 2000 + year_input
    leap_years = range(2004, 2050, 4)
    leap_days = 0
    for leap_year in leap_years:
        if year > leap_year:
            leap_days += 1
        elif year == leap_year and day_input >= 59:
            leap_days += 1
    n_days_J2000 = (year - 2000) * 365 + leap_days + day_input # days since 2000-01-01
    n_s_J2000 = n_days_J2000 * 24 * 3600 - 12 * 3600 + n_leap_sec # seconds since 2000-01-01 12:00:00
    return n_s_J2000

def MJD20002GMST(n_s_J2000):
    # Assuming JD_
    T = n_s_J2000/36525 # number of centuries since year 2000
    