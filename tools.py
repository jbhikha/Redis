import redis

r = redis.StrictRedis(host="localhost", port=6379, db=0)

DATA = {
    "US":"Washington DC",
    "India":"New Delhi",
    "Turkey":"Ankara",
    "Pakistan":"Islamabad",
    "Sri Lanka":"Colombo",
    "Bangladesh":"Dhaka",
    "UK":"London",
    "Ireland":"Dublin",
    "Australia":"Canberra",
    "France":"Paris",
}

for (key, value) in DATA.iteritems():
    r.set(key,value)

for (key, value) in DATA.iteritems():
    print "KEY is " + key + " and VALUE is " + r.get(key)
