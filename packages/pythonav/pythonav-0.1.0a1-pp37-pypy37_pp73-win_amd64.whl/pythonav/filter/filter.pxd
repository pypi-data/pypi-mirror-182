cimport libav as lib

from pythonav.descriptor cimport Descriptor


cdef class Filter(object):

    cdef const lib.AVFilter *ptr

    cdef object _inputs
    cdef object _outputs
    cdef Descriptor _descriptor


cdef Filter wrap_filter(const lib.AVFilter *ptr)
