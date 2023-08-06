from pythonav.plane cimport Plane
from pythonav.video.format cimport VideoFormatComponent


cdef class VideoPlane(Plane):

    cdef readonly size_t buffer_size
    cdef readonly unsigned int width, height
