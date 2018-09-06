from how import how
from what import what
from who import who
import random

def pickacon():
    pickacon = (random.choice(who) + " using " + random.choice(how) + " to " + random.choice(what) + ".")
    return pickacon