cimport libav as lib

from pythonav.container.core cimport Container
from pythonav.stream cimport Stream


cdef class InputContainer(Container):

    cdef flush_buffers(self)
