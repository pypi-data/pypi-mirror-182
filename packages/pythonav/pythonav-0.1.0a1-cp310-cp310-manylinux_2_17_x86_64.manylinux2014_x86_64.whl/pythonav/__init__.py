import os
import sys


# Some Python versions distributed by Conda have a buggy `os.add_dll_directory`
# which prevents binary wheels from finding the FFmpeg DLLs in the `pythonav.libs`
# directory. We work around this by adding `pythonav.libs` to the PATH.
if (
    os.name == "nt"
    and sys.version_info[:2] in ((3, 8), (3, 9))
    and os.path.exists(os.path.join(sys.base_prefix, "conda-meta"))
):
    os.environ["PATH"] = (
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), os.pardir, "pythonav.libs")
        )
        + os.pathsep
        + os.environ["PATH"]
    )

# MUST import the core before anything else in order to initalize the underlying
# library that is being wrapped.
from ._core import library_versions, time_base

# For convenience, IMPORT ALL OF THE THINGS (that are constructable by the user).
from .about import __version__
from .audio.fifo import AudioFifo
from .audio.format import AudioFormat
from .audio.frame import AudioFrame
from .audio.layout import AudioLayout
from .audio.resampler import AudioResampler
from .codec.codec import Codec, codecs_available
from .codec.context import CodecContext
from .container import open
from .error import *  # noqa: F403; This is limited to exception types.
from .format import ContainerFormat, formats_available
from .packet import Packet
from .video.format import VideoFormat
from .video.frame import VideoFrame

# Capture logging (by importing it).
import pythonav.logging


# Backwards compatibility
AVError = FFmpegError  # noqa: F405
