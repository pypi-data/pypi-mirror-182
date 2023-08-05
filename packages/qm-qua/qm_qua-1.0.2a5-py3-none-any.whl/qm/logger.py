import logging


logger = logging.getLogger("qm")
logger.warning(
    "Directly importing the logger is deprecated and will not work in future versions. "
    "To change logging levels, you can either use the function `set_logging_level(...)` from `qm.logging_utils` "
    'or you can use python native `logging.getLogger("qm").setLevel(...)`.'
)
