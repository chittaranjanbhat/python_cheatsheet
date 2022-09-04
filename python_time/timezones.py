"""
Created on 9/3/22
@author: chittaranjanbhat
"""

import pytz

print('All available Timezones in the world..!')
for timeZone in pytz.all_timezones:
    print(timeZone)

#There is another attribute that returns a set of timezones instead of a list.
print('Timezones')
for timeZone in pytz.all_timezones_set:
    print(timeZone)

#Get Common Timezones
print('Most commonly used timezones')
for timeZone in pytz.common_timezones:
    print(timeZone)


print(len(pytz.common_timezones))

# Get Timezone of a Any Country

print('US TimeZones')
for timeZone in pytz.country_timezones['US']:
    print(timeZone)

print('print all country Names with Code')
for code, name in pytz.country_names.items():
    print(code, ':', name)

print('Country full name =', pytz.country_names['IN'])