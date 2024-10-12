# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

distance = 10 * 1.6 * 1000 # m

time = 30 * 60 + 30 # seconds

speed = round((distance / time) * 3.6, 2)

print(f' Average Speed = {speed} km/h')