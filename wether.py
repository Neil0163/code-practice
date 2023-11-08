def as_sun_lover(temp):
    if (temp) > 25:
        return 'Great'
    else:
        return 'Not great'
    
def as_snow_lover(temp):
    if (temp) < 0:
        return "Great"
    else: 
        return "isnt good"

def report_wether(temp, preference_func):
    return preference_func(temp)
#test
print(report_wether(26, as_snow_lover))