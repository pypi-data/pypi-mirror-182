
Codecs
======

Descriptors
-----------

.. currentmodule:: pythonav.codec
.. automodule:: pythonav.codec

.. autoclass:: Codec

.. automethod:: Codec.create

.. autoattribute:: Codec.is_decoder
.. autoattribute:: Codec.is_encoder

.. autoattribute:: Codec.descriptor
.. autoattribute:: Codec.name
.. autoattribute:: Codec.long_name
.. autoattribute:: Codec.type
.. autoattribute:: Codec.id

.. autoattribute:: Codec.frame_rates
.. autoattribute:: Codec.audio_rates
.. autoattribute:: Codec.video_formats
.. autoattribute:: Codec.audio_formats


Flags
~~~~~

.. autoattribute:: Codec.properties

.. autoclass:: Properties

    Wraps :ffmpeg:`AVCodecDescriptor.props` (``AV_CODEC_PROP_*``).

    .. enumtable:: pythonav.codec.codec.Properties
        :class: pythonav.codec.codec.Codec

.. autoattribute:: Codec.capabilities

.. autoclass:: Capabilities

    Wraps :ffmpeg:`AVCodec.capabilities` (``AV_CODEC_CAP_*``).

    Note that ``ffmpeg -codecs`` prefers the properties versions of
    ``INTRA_ONLY`` and ``LOSSLESS``.

    .. enumtable:: pythonav.codec.codec.Capabilities
        :class: pythonav.codec.codec.Codec


Contexts
--------

.. currentmodule:: pythonav.codec.context
.. automodule:: pythonav.codec.context

.. autoclass:: CodecContext

.. autoattribute:: CodecContext.codec
.. autoattribute:: CodecContext.options

.. automethod:: CodecContext.create
.. automethod:: CodecContext.open
.. automethod:: CodecContext.close

Attributes
~~~~~~~~~~

.. autoattribute:: CodecContext.is_open
.. autoattribute:: CodecContext.is_encoder
.. autoattribute:: CodecContext.is_decoder

.. autoattribute:: CodecContext.name
.. autoattribute:: CodecContext.type
.. autoattribute:: CodecContext.profile

.. autoattribute:: CodecContext.time_base
.. autoattribute:: CodecContext.ticks_per_frame

.. autoattribute:: CodecContext.bit_rate
.. autoattribute:: CodecContext.bit_rate_tolerance
.. autoattribute:: CodecContext.max_bit_rate

.. autoattribute:: CodecContext.thread_count
.. autoattribute:: CodecContext.thread_type
.. autoattribute:: CodecContext.skip_frame

.. autoattribute:: CodecContext.extradata
.. autoattribute:: CodecContext.extradata_size

Transcoding
~~~~~~~~~~~
.. automethod:: CodecContext.parse
.. automethod:: CodecContext.encode
.. automethod:: CodecContext.decode


Flags
~~~~~

.. autoattribute:: CodecContext.flags

.. autoclass:: pythonav.codec.context.Flags

    .. enumtable:: pythonav.codec.context:Flags
        :class: pythonav.codec.context:CodecContext

.. autoattribute:: CodecContext.flags2

.. autoclass:: pythonav.codec.context.Flags2

    .. enumtable:: pythonav.codec.context:Flags2
        :class: pythonav.codec.context:CodecContext


Enums
~~~~~

.. autoclass:: pythonav.codec.context.ThreadType

    Which multithreading methods to use.
    Use of FF_THREAD_FRAME will increase decoding delay by one frame per thread,
    so clients which cannot provide future frames should not use it.

    .. enumtable:: pythonav.codec.context.ThreadType

.. autoclass:: pythonav.codec.context.SkipType

    .. enumtable:: pythonav.codec.context.SkipType


