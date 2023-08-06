import functools


def rhasattr(obj, attr):
    """Recursive `hasattr`.

    Args:
        obj: the class instance which may hold the attribute
        attr: the attribute that is to be checked, e.g. 'attribute1.attribute2'

    Returns:
        the attribute looked for
    """
    for a in attr.split("."):
        res = hasattr(obj, a)
        if res is False:
            return False
        obj = getattr(obj, a)
    return True


def rsetattr(obj, attr, val):
    """Recursive `setattr`, see https://stackoverflow.com/a/31174427.

    Args:
        obj: the class instance which holds the attribute
        attr: the attribute that is to be modified, e.g. 'attribute1.attribute2'
        val: the value to be set
    """
    pre, _, post = attr.rpartition(".")
    setattr(rgetattr(obj, pre) if pre else obj, post, val)


def rgetattr(obj, attr):
    """Recursive `getattr`.

    Args:
        obj: the class instance which holds the attribute
        attr: the attribute that is to be retrieved, e.g. 'attribute1.attribute2'

    Returns:
        the attribute looked for
    """

    def _getattr(obj, attr):
        return getattr(obj, attr)

    return functools.reduce(_getattr, [obj] + attr.split("."))


def rdelattr(obj, attr):
    """Recursive `delattr`.

    Args:
        obj: the class instance which holds the attribute
        attr: the attribute that is to be deleted, e.g. 'attribute1.attribute2'
    """
    pre, _, post = attr.rpartition(".")
    delattr(rgetattr(obj, pre) if pre else obj, post)
