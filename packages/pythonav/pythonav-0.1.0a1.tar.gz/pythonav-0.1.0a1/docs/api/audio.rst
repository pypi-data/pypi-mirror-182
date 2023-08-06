
Audio
=====

Audio Streams
-------------

.. automodule:: pythonav.audio.stream

    .. autoclass:: AudioStream
        :members:

Audio Context
-------------

.. automodule:: pythonav.audio.codeccontext

    .. autoclass:: AudioCodecContext
        :members:
        :exclude-members: channel_layout, channels

Audio Formats
-------------

.. automodule:: pythonav.audio.format

    .. autoclass:: AudioFormat
        :members:

Audio Layouts
-------------

.. automodule:: pythonav.audio.layout

    .. autoclass:: AudioLayout
        :members:

    .. autoclass:: AudioChannel
        :members:

Audio Frames
------------

.. automodule:: pythonav.audio.frame

    .. autoclass:: AudioFrame
        :members:
        :exclude-members: to_nd_array

Audio FIFOs
-----------

.. automodule:: pythonav.audio.fifo

    .. autoclass:: AudioFifo
        :members:
        :exclude-members: write, read, read_many

        .. automethod:: write
        .. automethod:: read
        .. automethod:: read_many

Audio Resamplers
----------------

.. automodule:: pythonav.audio.resampler

    .. autoclass:: AudioResampler
        :members:
        :exclude-members: resample

        .. automethod:: resample
