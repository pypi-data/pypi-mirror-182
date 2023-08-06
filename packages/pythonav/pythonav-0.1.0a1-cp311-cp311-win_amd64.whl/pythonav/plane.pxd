from pythonav.buffer cimport Buffer
from pythonav.frame cimport Frame


cdef class Plane(Buffer):

    cdef Frame frame
    cdef int index

    cdef size_t _buffer_size(self)
    cdef void* _buffer_ptr(self)
