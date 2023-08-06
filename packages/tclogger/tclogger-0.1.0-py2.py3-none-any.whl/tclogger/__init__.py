import os
import re
import datetime
import logging

__version__ = "0.1.0"
__author__ = 'Benjamin Western'
"""
tc-logger

A wrapper for Python Logging module to simplify logging to a file and console with a timestamp.
"""


def setup_logging(operation: str = 'execution', directory: str = None, timestamp_format: str = '%Y-%m-%d_%H%M%S', regex: str = r'[^a-zA-Z0-9\s_]|_+|\s+', sub_directory: str = 'logs', joiner: str = '_', logging_level: int = 10, file_extension: str = '.log', log_to_file: bool = True, log_to_console: bool = True):
    """
    Set up a logger for a specific operation, with the option to specify a directory, timestamp format, a regex pattern to filter out certain characters from the operation name, a subdirectory for the logs, a string to use as a separator between the operation name and timestamp in the log file name, a logging level, and a file extension for the log file.
    This function creates a directory (if required and given directory path is valid) for the logs, and a log file with the name of the operation, a timestamp, and the file extension.

    Examples:
    >>> logger = setup_logging()
    >>> logger = setup_logging('my_operation', logging_level=logging.ERROR)
    >>> logger = setup_logging('my_operation', directory='/path/to/custom/directory', file_extension='.txt', timestamp_format='%Y%m%d%H%M%S')
    >>> logger = setup_logging('my operation with spaces and symbols!', regex=r'[^a-zA-Z0-9]', joiner='-')
    >>> logger = setup_logging('my operation with spaces and symbols!', logging_level=logging.INFO, log_to_file=False)

    Parameters:
    - operation (str): The name of the operation for which to set up the logger (default 'execution').
    - directory (str): The directory in which to create the log file (default None, which uses the current working directory).
    - timestamp_format (str): The format of the timestamp to include in the log file name (default '%Y-%m-%d_%H%M%S').
    - regex (str): A regex pattern to filter out certain characters from the operation name (default r'[^a-zA-Z0-9\s_]|_+|\s+'). For example, if the operation name is 'Create BQ Tables', the regex pattern will remove the spaces, symbols, hyphens and underscores, leaving the operation name as 'CreateBQTables'.
    - sub_directory (str): The subdirectory in which to create the log file (default 'logs').
    - joiner (str): A string to use as a separator between the operation name and timestamp in the log file name (default '_').
    - logging_level (int): The logging level to use for the logger (default 10) also known as logging.DEBUG from the logging module.
    - file_extension (str): The file extension to use for the log file (default '.log').
    - log_to_file (bool): Whether to log to a file (default True).
    - log_to_console (bool): Whether to log to the console (default True).
    
    Returns:
    - logger: The logger object that has been configured to log to the file and print to the console in the format of [%(asctime)s] %(message)s.
    """
    
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime(timestamp_format)

    # Apply the passed REGEX to the operation string to ensure it will work as a filename
    operation = re.sub(regex, '', operation)
    
    # Cast the operation string as lowercase
    operation = operation.lower()

    # Create a logger and configure it to log to the file
    logger = logging.getLogger(operation)
    logger.setLevel(logging_level)
    
    # Setup Formatter for message
    formatter = logging.Formatter('[%(asctime)s] %(message)s')
    # https://docs.python.org/3/library/logging.html#logrecord-attributes
    # formatter = logging.Formatter('[%(asctime)s] line_number: %(lineno)d file_name: %(filename)s  %(message)s')
    
    # Setup the directory for the logs
    if log_to_file:
        if directory:
            current_directory = directory
        else:
            current_directory = os.getcwd()

        # Setup the log file name
        log_file_name = f'{operation}{joiner}{timestamp}{file_extension}'
        
        # Setup the logs subdirectory
        logs_dir = os.path.join(current_directory, sub_directory)
        if not os.path.exists(logs_dir):
            try:
                os.makedirs(logs_dir)
            except Exception as e:
                print(e)
                exit(f'Unable to create directory: {logs_dir}')

        # Setup the log file full path
        log_file = os.path.join(logs_dir, log_file_name)

        # Setup File Handler for message
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    if log_to_console:
        # Setup Console statements for message
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if not log_to_file and not log_to_console:
        print('No loggers configured, please set log_to_file and/or log_to_console to True')
        exit()

    return logger

def log(logger: logging.Logger, message: str, level: int = 10):
    """
    Uses the logger to log the message at the appropriate level.

    Examples:
    >>> logger = setup_logging()
    >>> log(logger, "This is a default message, see the other types: critical, error, warning, ,debug, info")
    >>> log(logger, 'This is a debug message', logging.DEBUG) # logging.DEBUG = 10
    >>> log(logger, 'This is an info message', logging.INFO) # logging.INFO = 20
    >>> log(logger, 'This is a warning message', logging.WARNING) # logging.WARNING = 30
    >>> log(logger, 'This is an error message', logging.ERROR) # logging.ERROR = 40
    >>> log(logger, 'This is an critical message', logging.CRITICAL) # logging.CRITICAL = 50

    Parameters:
    - logger (logging.Logger): The logger object to use to log the message.
    - message (str): The message to log. 
    - logging_level (int): The logging level to use for the logger (default 10) also known as logging.DEBUG from the logging module.
    
    Returns:
    - None
    """
    # Set the log level of the logger
    logger.setLevel(level)
    # Use the logger to log the message at the appropriate level
    logger.log(level, message)

    return None


if __name__ == '__main__':

    # Setup Logger in the current directory
    logger = setup_logging('testing logging')

    # Log a message at default level which is debug
    log(logger, "This is a default message, see the other types: critical, error, warning, ,debug, info")