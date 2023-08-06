
Containers
==========


Generic
-------

.. currentmodule:: pythonav.container

.. automodule:: pythonav.container

.. autoclass:: Container

    .. attribute:: options
    .. attribute:: container_options
    .. attribute:: stream_options
    .. attribute:: metadata_encoding
    .. attribute:: metadata_errors
    .. attribute:: open_timeout
    .. attribute:: read_timeout


Flags
~~~~~

.. attribute:: pythonav.container.Container.flags

.. class:: pythonav.container.Flags

    Wraps :ffmpeg:`AVFormatContext.flags`.

    .. enumtable:: pythonav.container.core:Flags
        :class: pythonav.container.core:Container


Input Containers
----------------

.. autoclass:: InputContainer
    :members:


Output Containers
-----------------

.. autoclass:: OutputContainer
    :members:


Formats
-------

.. currentmodule:: pythonav.format

.. automodule:: pythonav.format

.. autoclass:: ContainerFormat

.. autoattribute:: ContainerFormat.name
.. autoattribute:: ContainerFormat.long_name

.. autoattribute:: ContainerFormat.options
.. autoattribute:: ContainerFormat.input
.. autoattribute:: ContainerFormat.output
.. autoattribute:: ContainerFormat.is_input
.. autoattribute:: ContainerFormat.is_output
.. autoattribute:: ContainerFormat.extensions

Flags
~~~~~

.. autoattribute:: ContainerFormat.flags

.. autoclass:: pythonav.format.Flags

    .. enumtable:: pythonav.format.Flags
        :class: pythonav.format.ContainerFormat

