from queue import SimpleQueue

from ..utils.manifest import Manifest
from ..utils.configuration import Configuration
from ..utils.message import get_message_formatter
from ..connection import get_messagebroker_host, get_creds_provider, get_algorithm_manager_host
from ..reporter.reporter_factory import get_preprocess_reporter
from ..reporter.reporter import Reporter

import os
import logging

host = get_messagebroker_host()
algorithm_manager_host = get_algorithm_manager_host()
creds_provider = get_creds_provider()
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)
configuration = Configuration.get_configuration()
manifest = Manifest.get_manifest()
queue = SimpleQueue()
thread = None
message_formatter = get_message_formatter()
reporter = get_preprocess_reporter(algorithm_manager_host, logger, None)

def open_reporter() -> Reporter:
    """Get a reporter instance for reporting status updates to the Algorithm Manager"""
    return reporter

def get_logger(logging_level=logging.INFO) -> logging.Logger:
    return EPAlgorithmLogger(__name__, level=logging_level)

class EPAlgorithmLogger(logging.Logger):
    def __init__(self, name, level=logging.NOTSET):
        logging.Logger.__init__(self, name, level)
        self._reporter = reporter.open()

    def _log(self, level, msg, args, exc_info=None, extra=None, stack_info=False,
             stacklevel=1):
        self._reporter.report(msg)

    def __del__(self):
        self._reporter.close()