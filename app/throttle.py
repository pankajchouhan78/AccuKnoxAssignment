from rest_framework.throttling import SimpleRateThrottle


class PersonRequestThrottle(SimpleRateThrottle):
    scope = "person"
