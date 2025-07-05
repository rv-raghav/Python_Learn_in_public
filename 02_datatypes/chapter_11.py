import arrow

brewing_time = arrow.utcnow()
brewing_time.to("europe/rome")

from collections import namedtuple
chaiProfile = namedtuple("chaiProfile", ["flavour", "aroma"])