cimport libav as lib

from pythonav.frame cimport Frame
from pythonav.sidedata.sidedata cimport SideData


cdef class _MotionVectors(SideData):

    cdef dict _vectors
    cdef int _len


cdef class MotionVector(object):

    cdef _MotionVectors parent
    cdef lib.AVMotionVector *ptr
