"""
Created on 9/3/22
@author: chittaranjanbhat
"""

#https://pendulum.eustace.io/

import pendulum

now = pendulum.now("Europe/Paris")

# Changing timezone
now.in_timezone("US/Central")
now.in_timezone("UTC")

# Default support for common datetime formats
now.to_iso8601_string()

# Shifting
print(now.add(days=2))

dur = pendulum.duration(days=15)

# More properties
print(dur.weeks)
print(dur.hours)

# Handy methods
print(dur.in_hours())

# print(dur.in_words(locale="en_us"))

dt = pendulum.now()

# A period is the difference between 2 instances
period = dt - dt.subtract(days=3)

# period.in_weekdays()


# A period is iterable
for dt in period:
    print(dt)

