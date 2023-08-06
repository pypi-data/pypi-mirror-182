import errno
import traceback

import pythonav

from .common import TestCase, is_windows


class TestErrorBasics(TestCase):
    def test_stringify(self):

        for cls in (
            pythonav.ValueError,
            pythonav.FileNotFoundError,
            pythonav.DecoderNotFoundError,
        ):
            e = cls(1, "foo")
            self.assertEqual(str(e), "[Errno 1] foo")
            self.assertEqual(repr(e), "{}(1, 'foo')".format(cls.__name__))
            self.assertEqual(
                traceback.format_exception_only(cls, e)[-1],
                "{}{}: [Errno 1] foo\n".format(
                    "pythonav.error.",
                    cls.__name__,
                ),
            )

        for cls in (
            pythonav.ValueError,
            pythonav.FileNotFoundError,
            pythonav.DecoderNotFoundError,
        ):
            e = cls(1, "foo", "bar.txt")
            self.assertEqual(str(e), "[Errno 1] foo: 'bar.txt'")
            self.assertEqual(repr(e), "{}(1, 'foo', 'bar.txt')".format(cls.__name__))
            self.assertEqual(
                traceback.format_exception_only(cls, e)[-1],
                "{}{}: [Errno 1] foo: 'bar.txt'\n".format(
                    "pythonav.error.",
                    cls.__name__,
                ),
            )

    def test_bases(self):

        self.assertTrue(issubclass(pythonav.ValueError, ValueError))
        self.assertTrue(issubclass(pythonav.ValueError, pythonav.FFmpegError))

        self.assertTrue(issubclass(pythonav.FileNotFoundError, FileNotFoundError))
        self.assertTrue(issubclass(pythonav.FileNotFoundError, OSError))
        self.assertTrue(issubclass(pythonav.FileNotFoundError, pythonav.FFmpegError))

    def test_filenotfound(self):
        """Catch using builtin class on Python 3.3"""
        try:
            pythonav.open("does not exist")
        except FileNotFoundError as e:
            self.assertEqual(e.errno, errno.ENOENT)
            if is_windows:
                self.assertTrue(
                    e.strerror
                    in ["Error number -2 occurred", "No such file or directory"]
                )
            else:
                self.assertEqual(e.strerror, "No such file or directory")
            self.assertEqual(e.filename, "does not exist")
        else:
            self.fail("no exception raised")

    def test_buffertoosmall(self):
        """Throw an exception from an enum."""
        try:
            pythonav.error.err_check(-pythonav.error.BUFFER_TOO_SMALL.value)
        except pythonav.BufferTooSmallError as e:
            self.assertEqual(e.errno, pythonav.error.BUFFER_TOO_SMALL.value)
        else:
            self.fail("no exception raised")
