from types import ModuleType
from typing import List
import sys
import traceback

def error_message_details(error: Exception, error_detail: ModuleType = sys) -> str:
    """
    Return a formatted error message containing file and line number from the traceback.
    Pass the 'sys' module (default) or any module providing exc_info().
    """
    exc_type, exc_value, exc_tb = error_detail.exc_info()
    # Walk to the last traceback frame that belongs to user code
    tb = exc_tb
    while tb and tb.tb_next:
        tb = tb.tb_next
    file_name = tb.tb_frame.f_code.co_filename if tb else "<unknown>"
    line_no = tb.tb_lineno if tb else 0
    return f"Error occurred in python script name [{file_name}] line number [{line_no}] error message [{error}]"

class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: ModuleType = sys):
        # build a detailed message immediately so it's available on the exception
        detailed = error_message_details(error_message, error_detail)
        super().__init__(detailed)
        self.error_message = error_message
        self.error_detail = error_detail
        self.detailed_message = detailed

    def __str__(self) -> str:
        return self.detailed_message