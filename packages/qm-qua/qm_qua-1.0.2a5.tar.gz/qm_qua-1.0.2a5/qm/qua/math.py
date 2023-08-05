from qm._deprecated import deprecated
from qm.qua import Math


@deprecated("use Math.sin2pi instead", "0.6", "0.8")
def sin2pi(x):
    """
    Compute the sin of a 2*pi*x on hardware
    :param x: the angle in radians
    :return:
    """
    return Math.sin2pi(x)


@deprecated("use Math.cos2pi instead", "0.6", "0.8")
def cos2pi(x):
    """
    Compute the cos of a 2*pi*x on hardware
    :param x: the angle in radians
    :return:
    """
    return Math.cos2pi(x)


@deprecated("use Math.abs instead", "0.6", "0.8")
def abs(x):
    """
    Compute the absolute value of x on hardware
    :param x: a QUA variable
    :return:
    """
    return Math.abs(x)


@deprecated("use Math.sin instead", "0.6", "0.8")
def sin(x):
    """
    Compute the sin of a x on hardware
    :param x: the angle in radians
    :return:
    """
    return Math.sin(x)


@deprecated("use Math.cos instead", "0.6", "0.8")
def cos(x):
    """
    Compute the cos of a x on hardware
    :param x: the angle in radians
    :return:
    """
    return Math.cos(x)


@deprecated("use Math.sum instead", "0.6", "0.8")
def sum(x):
    """
    Compute sum of an array x on hardware
    :param x: a QUA array
    :return: sum of the array, has same type as x
    """
    return Math.sum(x)


@deprecated("use Math.max instead", "0.6", "0.8")
def max(x):
    """
    Compute max of an array x on hardware
    :param x: a QUA array
    :return: max value of the array, has same type as x
    """
    return Math.max(x)


@deprecated("use Math.min instead", "0.6", "0.8")
def min(x):
    """
    Compute min of an array x on hardware
    :param x: a QUA array
    :return: min value of the array, has same type as x
    """
    return Math.min(x)


@deprecated("use Math.argmax instead", "0.6", "0.8")
def argmax(x):
    """
    Return the index of the maximum of an array on hardware
    :param x: a QUA array
    :return: index of maximum value of array
    """
    return Math.argmax(x)


@deprecated("use Math.argmin instead", "0.6", "0.8")
def argmin(x):
    """
    Return the index of the minimum of an array on hardware
    :param x: a QUA array
    :return: index of minimum value of array
    """
    return Math.argmin(x)
