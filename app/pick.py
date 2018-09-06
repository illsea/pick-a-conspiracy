from app import how
from app import what
from app import who
import random

def pickacon():
    pickacon = (random.choice(who.who) + " using " + random.choice(how.how) + " to " + random.choice(what.what) + ".")
    return pickacon