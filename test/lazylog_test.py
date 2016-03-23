import unittest2
import sys
import os
import logging
import copy


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from mock import Mock, patch
from lazylog import LazyLogger

BASE_LOG_IMPORT = 'lazylog.lazylogger.logging.Logger.log'

class LazyLoggerTest(unittest2.TestCase):
    def setUp(self):
        self._logger = LazyLogger("testlog")
        self._logger.setLevel(logging.DEBUG)

    @patch(BASE_LOG_IMPORT)
    def test_calls_base_log_with_return_value(self, base_log):
        message = "I'm a lumberjack"
        func = lambda: message
        self._logger.log(logging.DEBUG, func)
        base_log.assert_called_with(self._logger, logging.DEBUG, message)

    @patch(BASE_LOG_IMPORT)
    def test_calls_base_log_with_bare_string(self, base_log):
        message = "I'm a lumberjack"
        self._logger.log(logging.DEBUG, message)
        base_log.assert_called_with(self._logger, logging.DEBUG, message)

    @patch(BASE_LOG_IMPORT)
    def test_wont_call_if_not_enabled(self, base_log):
        func = lambda: self.fail("But I'm not OK")
        self._logger.level = logging.WARN
        self._logger.log(logging.DEBUG, func)
        base_log.assert_not_called()

    def subtest_calls_with_level(self, expected_level, log_method, base_log):
        message = "I'm a lumberjack"
        func = lambda: message
        log_method(func)
        base_log.assert_called_with(self._logger, expected_level, message)
        base_log.reset_mock()
        self._logger.level = expected_level+1
        func = lambda: self.fail("But I'm not OK")
        log_method(func)
        base_log.assert_not_called()

    @patch(BASE_LOG_IMPORT)
    def test_calls_with_debug_level(self, base_log):
        self.subtest_calls_with_level(logging.DEBUG, self._logger.debug, base_log)

    @patch(BASE_LOG_IMPORT)
    def test_calls_with_info_level(self, base_log):
        self.subtest_calls_with_level(logging.INFO, self._logger.info, base_log)

    @patch(BASE_LOG_IMPORT)
    def test_calls_with_warning_level(self, base_log):
        self.subtest_calls_with_level(logging.WARNING, self._logger.warning, base_log)

    @patch(BASE_LOG_IMPORT)
    def test_calls_with_error_level(self, base_log):
        self.subtest_calls_with_level(logging.ERROR, self._logger.error, base_log)

    @patch(BASE_LOG_IMPORT)
    def test_calls_with_critical_level(self, base_log):
        self.subtest_calls_with_level(logging.CRITICAL, self._logger.critical, base_log)

if __name__ == '__main__':
    unittest2.main()

