__author__ = 'josebermudez'


def get_rolling_averages(array, n):
    if not array or n < 1 or len(array) < n:
        raise ValueError('error in parameters.')

    return [sum(array[x:x+n]) / n for x in xrange(len(array)-n+1)]
