import string
import secrets

import haikunator

haikunator = haikunator.Haikunator()


def append_random_haiku(name):
    haiku = haikunator.haikunate(token_length=0, delimiter='')
    return "{}_{}".format(name,haiku)


def generate_random_token(size):
    # allow upper and lowercase alphanumerics
    characters = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(characters) for i in range(size))
    return token


def iterate_pod_number(course):
    total_pods = course.get_total_number_pods()
    if total_pods == 0:
        return 1 
    else:
        # iterate from last pod number
        return course.pods.order_by('-number')[0].number + 1 