import errno
import logging
import threading

import pythonav.error
import pythonav.logging

from .common import TestCase


def do_log(message):
    pythonav.logging.log(pythonav.logging.INFO, "test", message)


class TestLogging(TestCase):
    def test_adapt_level(self):
        self.assertEqual(
            pythonav.logging.adapt_level(pythonav.logging.ERROR), logging.ERROR
        )
        self.assertEqual(
            pythonav.logging.adapt_level(pythonav.logging.WARNING), logging.WARNING
        )
        self.assertEqual(
            pythonav.logging.adapt_level(
                (pythonav.logging.WARNING + pythonav.logging.ERROR) // 2
            ),
            logging.WARNING,
        )

    def test_threaded_captures(self):

        with pythonav.logging.Capture(local=True) as logs:
            do_log("main")
            thread = threading.Thread(target=do_log, args=("thread",))
            thread.start()
            thread.join()

        self.assertIn((pythonav.logging.INFO, "test", "main"), logs)

    def test_global_captures(self):

        with pythonav.logging.Capture(local=False) as logs:
            do_log("main")
            thread = threading.Thread(target=do_log, args=("thread",))
            thread.start()
            thread.join()

        self.assertIn((pythonav.logging.INFO, "test", "main"), logs)
        self.assertIn((pythonav.logging.INFO, "test", "thread"), logs)

    def test_repeats(self):

        with pythonav.logging.Capture() as logs:
            do_log("foo")
            do_log("foo")
            do_log("bar")
            do_log("bar")
            do_log("bar")
            do_log("baz")

        logs = [log for log in logs if log[1] == "test"]

        self.assertEqual(
            logs,
            [
                (pythonav.logging.INFO, "test", "foo"),
                (pythonav.logging.INFO, "test", "foo"),
                (pythonav.logging.INFO, "test", "bar"),
                (pythonav.logging.INFO, "test", "bar (repeated 2 more times)"),
                (pythonav.logging.INFO, "test", "baz"),
            ],
        )

    def test_error(self):

        log = (pythonav.logging.ERROR, "test", "This is a test.")
        pythonav.logging.log(*log)
        try:
            pythonav.error.err_check(-errno.EPERM)
        except OSError as e:
            self.assertEqual(e.log, log)
        else:
            self.fail()
