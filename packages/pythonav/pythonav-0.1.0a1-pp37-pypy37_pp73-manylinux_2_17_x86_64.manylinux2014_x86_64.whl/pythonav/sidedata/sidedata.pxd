
cimport libav as lib

from pythonav.buffer cimport Buffer
from pythonav.dictionary cimport _Dictionary, wrap_dictionary
from pythonav.frame cimport Frame


cdef class SideData(Buffer):

    cdef Frame frame
    cdef lib.AVFrameSideData *ptr
    cdef _Dictionary metadata


cdef SideData wrap_side_data(Frame frame, int index)

cdef class _SideDataContainer(object):

    cdef Frame frame

    cdef list _by_index
    cdef dict _by_type
