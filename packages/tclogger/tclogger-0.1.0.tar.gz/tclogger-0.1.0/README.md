# tclogger
Wrapper for Python Logging module to log to a file and to the console. TC comes from the TC Series protocol droids. The TC series also somewhat lacked the eccentric behavior the 3PO units were known to develop. With this, I hope to make logging a little more sane.

## Installation
`pip install tclogger`

## Usage
```python
from tclogger import log, setup_logging

logger = setup_logging('my_operation', logging_level=logging.INFO, file_extension='.txt', log_to_console=False)
log('This is a warning log message', logger=logger, level=logging.WARNING)

```

### Setup Logging Parameters
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

### Setup Logging Outputs
    - logger: The logger object that has been configured to log to the file and print to the console in the format of [%(asctime)s] %(message)s.

### Log Parameters
    - message (str): The message to log.
    - logger (logging.Logger): The logger object to use for logging (default None).
    - level (int): The logging level to use for the log message (default 20) also known as logging.INFO from the logging module.

### Log Outputs
    - None


