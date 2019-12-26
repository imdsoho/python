class cust_slice(object):
    """
    slice(stop)
    slice(start, stop[, step])

    Create a slice object.  This is used for extended slicing (e.g. a[0:10:2]).
    """

    def indices(self, len):  # real signature unknown; restored from __doc__
        """
        S.indices(len) -> (start, stop, stride)

        Assuming a sequence of length len, calculate the start and stop
        indices, and the stride length of the extended slice described by
        S. Out of bounds indices are clipped in a manner consistent with the
        handling of normal slices.
        """
        pass

    def __eq__(self, *args, **kwargs):  # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs):  # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs):  # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs):  # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, stop):  # real signature unknown; restored from __doc__
        print("__init__")
        pass

    def __le__(self, *args, **kwargs):  # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs):  # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        print("__new__")
        print(args)
        print(kwargs)
        pass

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs):  # real signature unknown
        """ Return state information for pickling. """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ Return repr(self). """
        pass

    start = property(lambda self: 0)
    """:type: int"""

    step = property(lambda self: 0)
    """:type: int"""

    stop = property(lambda self: 0)
    """:type: int"""

    __hash__ = None

sl = cust_slice(10)
print(sl)