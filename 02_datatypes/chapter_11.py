import arrow


brewing_time = arrow.utcnow()
brewing_time.to("Europe/Rome")


from collections import namedtuple

chaiProfile = namedtuple("chaiProfile" , ["flavour" , "armoa"])


# to many datatypes are availbale are there so go on the web and try and enjoy 