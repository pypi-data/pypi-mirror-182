cimport libav as lib

from pythonav.filter.filter cimport Filter
from pythonav.filter.graph cimport Graph


cdef class FilterContext(object):

    cdef lib.AVFilterContext *ptr
    cdef readonly Graph graph
    cdef readonly Filter filter

    cdef object _inputs
    cdef object _outputs

    cdef bint inited


cdef FilterContext wrap_filter_context(Graph graph, Filter filter, lib.AVFilterContext *ptr)
