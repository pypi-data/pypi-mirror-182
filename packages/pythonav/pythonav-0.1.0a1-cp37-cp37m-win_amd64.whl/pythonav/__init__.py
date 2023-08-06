

""""""# start delvewheel patch
def _delvewheel_init_patch_1_1_4():
    import ctypes
    import os
    import platform
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'pythonav.libs'))
    is_pyinstaller = getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')
    is_conda_cpython = platform.python_implementation() == 'CPython' and (hasattr(ctypes.pythonapi, 'Anaconda_GetVersion') or 'packaged by conda-forge' in sys.version)
    if sys.version_info[:2] >= (3, 8) and not is_conda_cpython or sys.version_info[:2] >= (3, 10):
        if not is_pyinstaller or os.path.isdir(libs_dir):
            os.add_dll_directory(libs_dir)
    else:
        load_order_filepath = os.path.join(libs_dir, '.load-order-pythonav-0.1.0a1')
        if not is_pyinstaller or os.path.isfile(load_order_filepath):
            with open(os.path.join(libs_dir, '.load-order-pythonav-0.1.0a1')) as file:
                load_order = file.read().split()
            for lib in load_order:
                lib_path = os.path.join(os.path.join(libs_dir, lib))
                if not is_pyinstaller or os.path.isfile(lib_path):
                    ctypes.WinDLL(lib_path)


_delvewheel_init_patch_1_1_4()
del _delvewheel_init_patch_1_1_4
# end delvewheel patch

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
