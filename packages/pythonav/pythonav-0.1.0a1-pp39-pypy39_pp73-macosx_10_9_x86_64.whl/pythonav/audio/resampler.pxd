from pythonav.audio.format cimport AudioFormat
from pythonav.audio.frame cimport AudioFrame
from pythonav.audio.layout cimport AudioLayout
from pythonav.filter.graph cimport Graph


cdef class AudioResampler(object):

    cdef readonly bint is_passthrough

    cdef AudioFrame template

    # Destination descriptors
    cdef readonly AudioFormat format
    cdef readonly AudioLayout layout
    cdef readonly int rate
    cdef readonly unsigned int frame_size

    cdef Graph graph

    cpdef resample(self, AudioFrame)
