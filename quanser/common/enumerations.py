class ErrorCode:
    """Used as symbolic names for Quanser error codes."""
    __slots__ = ()

    OUT_OF_MEMORY = 1
    """Not enough memory to perform the operation."""

    OUT_OF_RESOURCES = 2
    """Not enough system resources are available to perform the operation."""

    OUT_OF_RANGE = 3
    """A value is outside the valid range."""

    INVALID_ARGUMENT = 4
    """One of the arguments is invalid."""

    PAGE_FAULT = 5
    """A page fault occurred accessing one of the arguments."""

    NOT_SUPPORTED = 6
    """The specified option or operation is not supported. It may be supported on other platforms. Please check the documentation."""

    DEADLOCK = 7
    """A deadlock situation would have occurred."""

    BUSY = 8
    """An operation is already in progress."""

    OBJECT_NOT_FOUND = 9
    """The object could not be found."""

    FILE_NOT_FOUND = 10
    """The file could not be found."""

    NO_PERMISSION = 11
    """The process lacks the appropriate privileges to perform the operation. If you are downloading a model then the model may be loaded on the target. Stop the model and download the code again. If you are uploading a MAT file then the host and target are likely the same machine and the operation would overwrite the MAT file with itself."""

    TOO_MANY_PROCESSES = 12
    """Too many processes are accessing an RTDLL."""

    UNRECOGNIZED_ERROR = 13
    """An operating system function returned an unrecognized error."""

    TIMED_OUT = 14
    """The operation timed out."""

    LIBRARY_NOT_FOUND = 15
    """Unable to locate the dynamic link library or shared object."""

    LIBRARY_NOT_CLOSED = 16
    """Failed to close dynamic link library or shared object."""

    STRING_TOO_SMALL = 17
    """The string buffer is too small to hold the result."""

    STRING_NOT_TERMINATED = 18
    """The string is not null-terminated within the given size."""

    INVALID_URI = 19
    """The absolute URI is not valid."""

    URI_OPTION_TOO_LONG = 20
    """The option name for a URI is too long. Option names must not be longer than URI_MAX_OPTION_LENGTH."""

    MISSING_URI_OPTION_VALUE = 21
    """The option for a URI is present but there is no associated value, as expected."""

    INVALID_URI_OPTION_VALUE = 22
    """The option for a URI is present but the value is invalid."""

    INVALID_URI_PORT_VALUE = 23
    """The port for a URI is present but the value is invalid."""

    MISSING_FUNCTION = 24
    """A required function is missing from a driver."""

    INVALID_CONNECTION = 25
    """The connection is not valid. A connection cannot be used after it has been closed."""

    NON_BLOCKING_NOT_SUPPORTED = 26
    """Non-blocking mode is not supported for the given protocol."""

    CANNOT_INITIALIZE_SOCKETS = 27
    """It was not possible to initialize the socket library."""

    NAGLE_NOT_SUPPORTED = 28
    """The Nagle algorithm is not supported for the given communication subsystem."""

    INVALID_BUFFER_SIZE = 29
    """The specified buffer size is not valid. It may be out of an acceptable range."""

    SOCKET_NOT_REUSABLE = 30
    """The socket address could not be made reusable."""

    CANNOT_BIND_SOCKET = 31
    """It was not possible to bind the socket to the given port. Check that the port number is valid and not in use."""

    CANNOT_LISTEN = 32
    """It was not possible to listen on the specified connection."""

    CANNOT_CONNECT = 33
    """It was not possible to connect to the specified URI."""

    WOULD_BLOCK = 34
    """A non-blocking operation would have blocked."""

    INTERRUPTED = 35
    """A blocking operation was interrupted by a signal."""

    HOST_NOT_FOUND = 36
    """The specified host could not be found."""

    INVALID_SOCKET = 37
    """Socket is not valid. It may have been closed already or never created successfully."""

    CANNOT_LINGER = 38
    """Unable to set the linker options for a connection."""

    CANNOT_ACCEPT_CONNECTION = 39
    """The listening socket was unable to accept a client connection."""

    CANNOT_SEND = 40
    """Unable to send data over a connection."""

    CANNOT_RECEIVE = 41
    """Unable to receive data over a connection."""

    CANNOT_POLL = 42
    """Unable to poll a connection."""

    CANNOT_SHUTDOWN = 43
    """Unable to shut down send and/or receives on the connection."""

    CONNECTION_SHUTDOWN = 44
    """The connection has been shut down."""

    CANNOT_CLOSE = 45
    """Unable to close the connection."""

    CANNOT_GET_TIME = 46
    """Unable to get the current high-resolution time."""

    CANNOT_SUBTRACT_TIMEOUTS = 47
    """The timeouts cannot be subtracted because the left-hand side is relative and the right hand side is absolute."""

    CANNOT_ADD_TIMEOUTS = 48
    """The timeouts cannot be added because both sides are absolute timeouts."""

    CANNOT_OBTAIN_LOCK = 49
    """Cannot obtain a lock to gain exclusive access to a critical section of code."""

    INVALID_RECONFIGURATION = 50
    """Reconfiguration instance is not valid. It may have been closed already or never opened successfully."""

    BEGIN_CONTROL_NOT_CALLED = 51
    """The reconfiguration_begin_control function has not been called."""

    CANNOT_SWITCH = 52
    """An attempt to switch models failed due to a communication failure."""

    INVALID_BASE = 53
    """The given base is invalid and cannot be used to convert the integer to a string."""

    INVALID_TIMER_EVENT = 54
    """The timer event passed as an argument is invalid."""

    INVALID_TIMER_NOTIFICATION = 55
    """The timer notification structure is invalid."""

    INVALID_TIMER_RESOLUTION = 56
    """The specified timer resolution is invalid."""

    INVALID_TIMER_PERIOD = 57
    """The specified timer period is invalid."""

    INVALID_TIMER = 58
    """The timer passed as an argument is invalid."""

    CANNOT_GET_RESOLUTION = 59
    """The timer resolution could not be retrieved. Stack or memory corruption is likely."""

    CANNOT_SET_RESOLUTION = 60
    """The timer resolution could not be set. The user does not have permission."""

    BEGIN_RESOLUTION_NOT_CALLED = 61
    """The qtimer_begin_resolution function has not been called successfully."""

    STATE_INCOMPATIBLE = 62
    """The state information is not compatible. Reconfiguration states must have the same data type and size."""

    INVALID_STATE = 63
    """The state is invalid. It may have already been unregistered."""

    INVALID_STREAM = 64
    """The stream is not valid. A stream cannot be used after it has been closed."""

    STREAM_BUFFER_TOO_SMALL = 65
    """The stream buffer is too small to send or receive units of the given size."""

    INVALID_DPC = 66
    """The DPC object is not valid. A DPC object cannot be used after it has been closed."""

    INVALID_METHOD = 67
    """The method code received is not valid. The DPC object should be closed."""

    INVALID_INTERFACE = 68
    """The interface code received is not valid. The DPC object should be closed."""

    DPC_DISCONNECTED = 69
    """The DPC connection has been closed at the peer."""

    INVALID_LOG = 70
    """The log object is not valid. A log object cannot be used after it has been closed."""

    INVALID_SEMAPHORE = 71
    """The semaphore is not valid. A semaphore cannot be used after it has been destroyed."""

    INVALID_MUTEX = 72
    """The mutex is not valid. A mutex cannot be used after it has been destroyed."""

    ARGUMENT_LIST_TOO_BIG = 73
    """The argument list for the model is too big."""

    FILE_NOT_EXECUTABLE = 74
    """The model specified is not executable."""

    TOO_MANY_LINKS = 75
    """Too many symbolic links or prefixes."""

    NAME_TOO_LONG = 76
    """The length of a path or pathname component exceeds the limit."""

    NOT_DIRECTORY = 77
    """A component of the path isn't a directory."""

    NAME_CONFLICT = 78
    """A different kind of object with the same name appears in the global namespace."""

    INVALID_ESCAPE_SEQUENCE = 79
    """An escape sequence in a quoted string is invalid."""

    INVALID_STOP_BITS = 80
    """Stop bits option has an invalid value. It must be "1", "1.5" or "2"."""

    INVALID_FLOW_CONTROL = 81
    """Invalid flow control option. Supported values are "none", "hw", "sw"."""

    INVALID_PARITY = 82
    """Invalid parity option. Supported values are "none", "even", "odd", "mark", "space"."""

    NOT_SOCK_STREAM = 83
    """The operation is not supported because the socket is not a SOCK_STREAM socket."""

    CANNOT_FIND_SOCKET_DRIVER = 84
    """The operation failed because the socket manager/driver could not be found."""

    NETWORK_FAILED = 85
    """The network subsystem has failed."""

    SOCKETS_NOT_INITIALIZED = 86
    """The socket library has not been initialized."""

    OPERATION_IN_PROGRESS = 87
    """A blocking socket operation is currently in progress."""

    INVALID_CARD_HANDLE = 88
    """The given t_card handle is not a valid card. In some Simulink versions, this error can arise when a HIL Initialize block is not in the same subsystem as a HIL Timebase block, due to Simulink incorrectly determining the execution order. In this case, try putting the two HIL blocks in the same subsystem."""

    VERSION_ARGUMENT_IS_NULL = 89
    """The version object passed as a parameter is NULL."""

    INVALID_VERSION_ARGUMENT = 90
    """The version structure does not have the right length."""

    DRIVER_MISSING_OPEN_OR_CLOSE = 91
    """A hardware driver is missing the open and/or close function."""

    CARD_ARGUMENT_IS_NULL = 92
    """The card argument to hil_open is NULL."""

    CARD_TYPE_ARGUMENT_IS_NULL = 93
    """The card type argument to hil_open is NULL."""

    FUNCTION_NOT_SUPPORTED = 94
    """The function is not supported."""

    MISSING_ANALOG_INPUTS = 95
    """No analog input channels were specified even though the number of analog inputs is nonzero."""

    MISSING_ANALOG_OUTPUTS = 96
    """No analog output channels were specified even though the number of analog outputs is nonzero."""

    MISSING_ENCODER_INPUTS = 97
    """No encoder input channels were specified even though the number of encoder inputs is nonzero."""

    MISSING_PWM_OUTPUTS = 98
    """No PWM output channels were specified even though the number of PWM outputs is nonzero."""

    MISSING_DIGITAL_INPUTS = 99
    """No digital input channels were specified even though the number of digital inputs is nonzero."""

    MISSING_DIGITAL_OUTPUTS = 100
    """No digital outputs were specified even though the number of digital outputs is nonzero."""

    MISSING_OTHER_INPUTS = 101
    """No other input channels were specified even though the number of other inputs is nonzero."""

    MISSING_OTHER_OUTPUTS = 102
    """No other output channels were specified even though the number of other outputs is nonzero."""

    MISSING_CLOCK_INPUTS = 103
    """No clocks were specified even though the number of clocks is nonzero."""

    TASK_ARGUMENT_IS_NULL = 104
    """The task argument to a HIL function is NULL."""

    INVALID_TASK_HANDLE = 105
    """An invalid task handle was passed as an argument to a HIL function."""

    BOARD_ARGUMENT_IS_NULL = 106
    """The board argument passed to the board-specific HIL driver is NULL. This situation should never occur unless the user is calling the board-specific driver directly or memory has been corrupted."""

    UNABLE_TO_OPEN_DRIVER = 107
    """An operating system specific kernel-level driver for the card was found but could not be loaded. There may be a device conflict, hardware problem, or the driver may not be correctly installed."""

    BOARD_NOT_FOUND = 108
    """An operating system specific kernel-level driver for the specified card could not be found. The card or driver may not be installed. The kernel-level driver is the driver that gets installed when the operating system detects the hardware. Check Device Manager to see if the card is present or recognized by the operating system. Also verify that you have selected the correct card in the HIL Initialize block or hil_open function."""

    BOARD_IN_USE = 109
    """The board is in use by another process and the board-specific driver does not support multi-process access to the card."""

    UNABLE_TO_LOCK_DEVICE = 110
    """It was not possible to get exclusive access to the device. The operation has been aborted."""

    BUFFER_OVERFLOW = 111
    """For a read operation, the buffer has overflowed. For a write operation, there is no more data left in the buffer. The sampling frequency is too fast for the rate at which data is being read from or written to the buffer. For HIL Timebase blocks or HIL tasks, oversampling has occurred. For Stream blocks, the hardware FIFO overflowed."""

    UNABLE_TO_CLOSE_DRIVER = 112
    """It was not possible to close the operating system specific kernel-level driver. The driver handle may be invalid. For example, the device may have already been closed or memory may have been corrupted."""

    INVALID_BOARD_HANDLE = 113
    """An invalid board handle was passed as an argument to the board-specific HIL driver. Once a card has been closed using hil_close the board handle is invalid."""

    OUT_OF_REQUIRED_SYSTEM_RESOURCES = 114
    """There are not enough system resources to perform the requested operation. Try rebooting, requesting fewer samples, or adding more memory to your machine."""

    DRIVER_INCOMPATIBLE_WITH_BOARD_DLL = 115
    """The board-specific HIL driver passed an invalid parameter to the operating system specific kernel-level driver for the board. The board-specific HIL driver is likely not compatible with the operating system specific kernel-level driver for the board. Make sure both are up-to-date and compatible versions."""

    INTERNAL_BUFFER_TOO_SMALL = 116
    """The board-specific HIL driver used an internal buffer that was too small for the operating system specific kernel-level driver for the board. The board-specific HIL driver is likely not compatible with the operating system specific kernel-level driver for the board. Make sure both are up-to-date and compatible versions."""

    ANALOG_RESOURCE_IN_USE = 117
    """The analog-to-digital converter on the HIL board is currently in use by another operation."""

    INVALID_BUFFER_HANDLE = 118
    """An invalid buffer handle was passed to a board-specific HIL driver function."""

    ANALOG_INPUT_CHANNELS_NOT_SUPPORTED = 119
    """Analog input channels are not supported by this board."""

    TOO_MANY_ANALOG_INPUT_CHANNELS = 120
    """Too many analog input channels were specified."""

    INVALID_ANALOG_INPUT_CHANNEL = 121
    """One of the analog input channels that was specified is not a valid channel number. Channel numbers typically range from 0 to one less than the number of channels."""

    ENCODER_INPUT_CHANNELS_NOT_SUPPORTED = 122
    """Counter input channels are not supported by this board."""

    TOO_MANY_ENCODER_INPUT_CHANNELS = 123
    """Too many encoder input channels were specified."""

    INVALID_ENCODER_INPUT_CHANNEL = 124
    """One of the encoder input channels that was specified is not a valid channel number. Channel numbers typically range from 0 to one less than the number of channels."""

    DIGITAL_INPUT_CHANNELS_NOT_SUPPORTED = 125
    """Digital input channels are not supported by this board."""

    TOO_MANY_DIGITAL_INPUT_CHANNELS = 126
    """Too many digital input channels were specified."""

    INVALID_DIGITAL_INPUT_CHANNEL = 127
    """One of the digital input channels that was specified is not a valid channel number. Channel numbers typically range from 0 to one less than the number of channels."""

    OTHER_INPUT_CHANNELS_NOT_SUPPORTED = 128
    """Other input channels are not supported by this board."""

    TOO_MANY_OTHER_INPUT_CHANNELS = 129
    """Too many other input channels were specified."""

    INVALID_OTHER_INPUT_CHANNEL = 130
    """One of the other input channels that was specified is not a valid channel number. Channel numbers are typically divided into ranges according to functionality. Refer to the documentation for your card."""

    ANALOG_OUTPUT_CHANNELS_NOT_SUPPORTED = 131
    """Analog output channels are not supported by this board."""

    TOO_MANY_ANALOG_OUTPUT_CHANNELS = 132
    """Too many analog output channels were specified."""

    INVALID_ANALOG_OUTPUT_CHANNEL = 133
    """One of the analog output channels that was specified is not a valid channel number. Channel numbers typically range from 0 to one less than the number of channels."""

    PWM_OUTPUT_CHANNELS_NOT_SUPPORTED = 134
    """PWM output channels are not supported by this board."""

    TOO_MANY_PWM_OUTPUT_CHANNELS = 135
    """Too many PWM output channels were specified."""

    INVALID_PWM_OUTPUT_CHANNEL = 136
    """One of the PWM output channels that was specified is not a valid channel number. Channel numbers typically range from 0 to one less than the number of channels."""

    DIGITAL_OUTPUT_CHANNELS_NOT_SUPPORTED = 137
    """Digital output channels are not supported by this board."""

    TOO_MANY_DIGITAL_OUTPUT_CHANNELS = 138
    """Too many digital output channels were specified."""

    INVALID_DIGITAL_OUTPUT_CHANNEL = 139
    """One of the digital output channels that was specified is not a valid channel number. Channel numbers typically range from 0 to one less than the number of channels."""

    OTHER_OUTPUT_CHANNELS_NOT_SUPPORTED = 140
    """Other output channels are not supported by this board."""

    TOO_MANY_OTHER_OUTPUT_CHANNELS = 141
    """Too many other output channels were specified."""

    INVALID_OTHER_OUTPUT_CHANNEL = 142
    """One of the other output channels that was specified is not a valid channel number. Channel numbers are typically divided into ranges according to functionality. Refer to the documentation for your card."""

    CONFLICTING_DIGITAL_DIRECTIONS = 143
    """A digital channel was specified as both an input and an output. Digital channels cannot be programmed as an input and an output at the same time."""

    CLOCK_NOT_SUPPORTED = 144
    """The specified clock is not supported by the board-specific HIL driver for this board."""

    HARDWARE_CLOCK_IN_USE = 145
    """The specified hardware clock is already in use for another operation and the board-specific HIL driver for this board does not permit sharing of the hardware clock."""

    TOO_MANY_CLOCKS = 146
    """Too many clocks were specified."""

    CLOCK_MODE_NOT_SUPPORTED = 147
    """The specified clock mode is not supported by this board."""

    PWM_MODE_NOT_SUPPORTED = 148
    """The specified PWM mode is not supported by this board."""

    CLOCK_FREQUENCY_NOT_POSITIVE = 149
    """The clock frequency specified is negative or zero. The clock frequency must be positive."""

    CLOCK_FREQUENCY_TOO_HIGH = 150
    """The clock frequency is too high for the specified clock. Try using a different clock. Hardware clocks are generally faster than the system clocks."""

    CLOCK_FREQUENCY_TOO_LOW = 151
    """The clock frequency is too low for the specified clock. Try using a different clock. System clocks are preferable for low frequencies so that hardware clocks remain available for higher frequency operations."""

    CLOCK_FREQUENCY_INVALID = 152
    """The clock frequency is invalid for the specified clock, or the clock may be unavailable. Try using a different clock frequency (usually slower) or a different clock."""

    DUTY_CYCLE_NOT_POSITIVE = 153
    """The specified duty cycle is negative and negative duty cycles are not supported by this board."""

    DUTY_CYCLE_TOO_HIGH = 154
    """The specified duty cycle is more than 100% (i.e. greater than 1.0)."""

    WRONG_CLOCK_MODE = 155
    """The specified clock is multipurpose and is in the wrong mode for this operation."""

    INVALID_OPERATION_HANDLE = 156
    """An invalid operation handle was passed as an argument to the board-specific HIL driver. Once a task has been deleted using hil_task_delete the operation handle is invalid."""

    OPERATION_ARGUMENT_IS_NULL = 157
    """The operation argument to a board-specific HIL driver is NULL. This situation should never occur unless the user is calling the board-specific driver directly or memory has been corrupted."""

    INTERRUPT_VECTOR_IN_USE = 158
    """The interrupt vector required by the board is in use by another device and the board-specific HIL driver does not support sharing of the interrupt vector."""

    TOO_MANY_SAMPLES_FOR_BUFFER = 159
    """The number of samples requested in the read or write operation is more than the number of samples being buffered by the task. Increase the buffer size for the task or read or write fewer samples."""

    MISSING_ANALOG_INPUT_BUFFER = 160
    """Analog input channels have been specified but not enough buffer space has been provided for the read operation."""

    MISSING_ENCODER_INPUT_BUFFER = 161
    """Encoder input channels have been specified but not enough buffer space has been provided for the read operation."""

    MISSING_DIGITAL_INPUT_BUFFER = 162
    """Digital input channels have been specified but not enough buffer space has been provided for the read operation."""

    MISSING_OTHER_INPUT_BUFFER = 163
    """Other input channels have been specified but not enough buffer space has been provided for the read operation."""

    MISSING_ANALOG_OUTPUT_BUFFER = 164
    """Analog output channels have been specified but not enough values have been provided for the write operation."""

    MISSING_PWM_OUTPUT_BUFFER = 165
    """PWM output channels have been specified but not enough values have been provided for the write operation."""

    MISSING_DIGITAL_OUTPUT_BUFFER = 166
    """Digital output channels have been specified but not enough values have has been provided for the write operation."""

    MISSING_OTHER_OUTPUT_BUFFER = 167
    """Other output channels have been specified but not enough values have been provided for the write operation."""

    READING_FROM_WRITE_ONLY_TASK = 168
    """An attempt was made to read from a write-only task."""

    WRITING_TO_READ_ONLY_TASK = 169
    """An attempt was made to write to a read-only task."""

    PROCESS_NOT_FOUND = 170
    """The specified model process could not be found."""

    PROCESS_CANNOT_BE_STOPPED = 171
    """The specified model process could not be stopped."""

    ERROR_MESSAGE_NOT_FOUND = 172
    """An error message corresponding to the given error code could not be found."""

    PORT_IN_USE = 173
    """Unable to listen on the specified port. The port is already in use."""

    HOST_BUSY = 174
    """The host is too busy to accept a connection at this point in time. Try again later."""

    HOST_SHUTDOWN = 175
    """The host was shut down during the operation."""

    CONNECTION_RESET = 176
    """The connection was reset. The remote peer may have exited without closing the connection."""

    CHANNEL_NOT_LISTENING = 177
    """The channel is not a listening channel so it cannot be used to accept connections."""

    CHANNEL_IS_LISTENING = 178
    """The channel is a listening channel so it cannot be used to send and receive data."""

    UNRECOGNIZED_BOARD_TYPE = 179
    """The specified board type is not recognized. Please install the board-specific HIL driver for this board type."""

    INVALID_PREFERENCES_ROOT = 180
    """The root node specified for preferences was invalid."""

    PREFERENCES_NODE_NOT_FOUND = 181
    """The specified preference node could not be found."""

    CANNOT_ENUMERATE_VALUES = 182
    """The values of a preferences node could not be enumerated."""

    PREFERENCES_NODE_TOO_LONG = 183
    """The path for the preferences node is too long."""

    URI_NOT_FOUND = 184
    """The specified URI could not be found."""

    CANNOT_SET_PREFERENCES_VALUE = 185
    """The preferences value could not be set. You may not have sufficient privileges."""

    CANNOT_DELETE_PREFERENCES_VALUE = 186
    """The preferences value could not be deleted. It may not exist, or you may not have sufficient privileges."""

    REMOVING_LAST_URI = 187
    """An attempt has been made to remove the last URI upon which the target is serving. To avoid leaving no means to connect to the target, the last URI may not be removed. The target must serve on at least one URI."""

    REMOVING_URI_IN_USE = 188
    """It is not possible to remove the URI associated with the current connection to the target."""

    OPERATION_PENDING = 189
    """The operation is not complete. It is still pending. This error should never be returned by any function to the user."""

    OVERSAMPLING_DETECTED = 190
    """Oversampling has been detected. The sampling rate is too fast and cannot be maintained."""

    TIMEBASE_ALREADY_REGISTERED = 191
    """A Timebase block has already been registered. Only one Timebase block may be present in the model."""

    TIMEBASE_NOT_REGISTERED = 192
    """A Timebase block has not been registered."""

    CANNOT_GET_PREFERENCES_VALUE = 193
    """The preferences value could not be retrieved. You may not have sufficient privileges."""

    INVALID_LICENSE = 194
    """The Quanser product does not have a valid license for the requested operation. For example, you may be trying to run more than one model at a time when you are only licensed for one, or your license may have expired. Run qc_get_loaded_models to see the models currently loaded and qc_stop_model to stop a model. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product. Contact Quanser if you think your license may have expired or it does not suit your current needs."""

    MISSING_LICENSE_FILE = 195
    """The license file is missing. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    ETHERCAT_MASTER_NOT_FOUND = 196
    """The corresponding EtherCAT Master could not be found. Make sure that an EtherCAT Master block is present in the model."""

    CANNOT_OPEN_ETHERCAT = 197
    """Unable to open the EtherCAT device specified. Make sure the XML configuration and IP address specified are correct"""

    ETHERCAT_DEVICE_IS_NULL = 198
    """A null pointer was specified instead of a valid EtherCAT device."""

    ETHERCAT_SYNC_CLIENT_IS_NULL = 199
    """The EtherCAT device does not have a synchronization client."""

    INVALID_XML_COMMENT = 200
    """An invalid comment was specified in the XML file."""

    INVALID_XML = 201
    """Malformed XML in the XML file."""

    INVALID_XML_DOCUMENT_TYPE = 202
    """Missing document type declaration <!DOCTYPE ...> in the XML file."""

    SPACE_PRECEDES_XML_DECLARATION = 203
    """Whitespace may not precede the <?xml ...> declaration in the XML file."""

    MULTIPLE_XML_ROOTS = 204
    """The XML file has more than one root element."""

    UNTERMINATED_XML_COMMENT = 205
    """A comment in the XML file was not terminated."""

    MISSING_XML_VERSION = 206
    """The version information in the <?xml ...> XML declaration is missing."""

    INVALID_XML_VERSION = 207
    """The specified XML version is not supported by this XML parser."""

    INVALID_XML_ENCODING = 208
    """The encoding information in the <?xml ...> XML declaration is not specified properly."""

    INVALID_XML_STANDALONE = 209
    """The standalone option in the <?xml ...> XML declaration is not specified properly."""

    INVALID_XML_DECLARATION = 210
    """The <?xml ...?> XML declaration is not formed correctly."""

    INVALID_XML_DECLARATION_END = 211
    """The <?xml ...?> XML declaration is not terminated correctly."""

    UNSUPPORTED_XML_MARKUP = 212
    """Markup that is currently unsupported was found in the XML file."""

    MISSING_URI_PATH = 213
    """The path component of the URI is missing."""

    INVALID_FILE_MODE = 214
    """The mode option specified for a file URI is invalid."""

    INVALID_FILE_SHARE_MODE = 215
    """The share mode option specified for a file URI is invalid."""

    NO_FILE_SIZE = 216
    """The end of the file could not be determined."""

    CHANGE_NOTIFICATIONS_NOT_SUPPORTED = 217
    """Change notifications are not supported on the specified file system."""

    WRITING_TO_READ_ONLY_STREAM = 218
    """An attempt was made to write to a read-only stream."""

    READING_FROM_WRITE_ONLY_STREAM = 219
    """An attempt was made to read from a write-only stream."""

    INVALID_STREAM_FORMAT = 220
    """The character format specified for the stream is out of range."""

    ILLEGAL_UTF8_CHARACTER = 221
    """An illegal UTF-8 character was encountered in the stream."""

    ILLEGAL_UTF16_CHARACTER = 222
    """An illegal UTF-16 character was encountered in the stream."""

    ILLEGAL_UTF32_CHARACTER = 223
    """An illegal UTF-32 character was encountered in the stream."""

    XML_DECLARATION_NOT_FIRST = 224
    """An <?xml ...> declaration appears but it is not the first tag in the XML stream."""

    XML_DOCTYPE_ALREADY_PARSED = 225
    """The <!DOCTYPE ...> declaration has already appeared in the XML stream."""

    INVALID_PI_TARGET_NAME = 226
    """The name of the XML processing instruction target is invalid."""

    INVALID_XML_PROCESSING_INSTRUCTION = 227
    """The XML processing instruction was invalid."""

    INVALID_XML_EXTERNAL_ID = 228
    """The external identifier in the document type declaration is invalid."""

    INVALID_DOCTYPE_NAME = 229
    """The name of the document type is invalid."""

    INVALID_XML_SYSTEM_LITERAL = 230
    """The system literal associated with the external identifier in the document type declaration is invalid."""

    INVALID_DOCTYPE_NOT_TERMINATED = 231
    """The document type definition is not terminated properly."""

    INVALID_XML_ELEMENT_NAME = 232
    """The name of the XML element is invalid. Names must begin with a letter, underscore or colon."""

    INVALID_XML_ELEMENT = 233
    """An XML element is invalid. An attribute name may be invalid or it is not terminated correctly."""

    MISSING_XML_ATTRIBUTE_VALUE = 234
    """An attribute appears in an XML element tag but there is no associated value."""

    TAG_IN_XML_ATTRIBUTE_VALUES = 235
    """Tags are not allowed within attribute values. Use &lt; to put a '<' in an attribute value."""

    INVALID_XML_ENTITY_REFERENCE = 236
    """Invalid XML entity reference. Escape ampersands using &amp; to put ampersands in values."""

    INVALID_XML_CHAR_REFERENCE = 237
    """The value of the character reference is not a valid character for XML."""

    UNTERMINATED_XML_ATTRIBUTE_VALUE = 238
    """An XML attribute value string is not terminated."""

    CDATA_TERMINATOR_IN_CHAR_DATA = 239
    """The CDATA termination sequence ']]>' is not allowed within XML content."""

    INVALID_XML_TAG = 240
    """An XML tag is invalid."""

    INVALID_XML_CDATA_TAG = 241
    """The XML <![CDATA[ ...]]> tag was invalid."""

    INVALID_XML_CDATA = 242
    """The contents of a CDATA section were invalid. An invalid character was detected."""

    UNTERMINATED_XML_ELEMENT = 243
    """An XML element was not terminated properly."""

    INVALID_DOM_NODE = 244
    """The DOM node is NULL or otherwise invalid."""

    INVALID_DOM_NODE_LIST = 245
    """The DOM node list is null or otherwise invalid."""

    ITEM_NOT_IN_LIST = 246
    """An attempt was made to access a node in a list to which it did not belong, or the node does not belong to a list."""

    STRING_IS_NULL = 247
    """The string buffer passed as an argument is NULL."""

    MISMATCHED_XML_ELEMENT_TAG = 248
    """An XML end tag does not match the corresponding start tag."""

    INVALID_DOM_NAMED_NODE_MAP = 249
    """The DOM named node map is null or otherwise invalid."""

    ITEM_NOT_IN_MAP = 250
    """An attempt was made to access a node in a map to which it did not belong, or the node does not belong to a map."""

    DUPLICATE_XML_ATTRIBUTE = 251
    """An XML element has more than one attribute with the same name."""

    ILLEGAL_UTF8_LEAD_CHAR = 252
    """The UTF-8 code unit is not a valid lead byte. It is a code unit that is only valid in the middle of a UTF-8 character."""

    TRUNCATED_UTF8_CHAR = 253
    """The UTF-8 character may be valid but the given length is too small to contain it."""

    ILLEGAL_UTF16_LEAD_CHAR = 254
    """The UTF-16 code unit is not a valid lead byte. It is a code unit that is only valid as a surrogate code unit."""

    TRUNCATED_UTF16_CHAR = 255
    """The UTF-16 character may be valid but the given length is too small to contain it."""

    CANNOT_START_LICENSE_MANAGER = 256
    """The Quanser license manager could not be started."""

    CANNOT_STOP_LICENSE_MANAGER = 257
    """The Quanser license manager could not be stopped."""

    TRUNCATED_UTF32_CHAR = 258
    """The UTF-32 character may be valid but the given length is too small to contain it."""

    INVALID_THREAD_AFFINITY = 259
    """The thread was assigned an affinity that does not correspond to an existing CPU or a CPU in the process affinity."""

    INVALID_PROCESS_AFFINITY = 260
    """The process was assigned an affinity that does not correspond to an existing CPU."""

    CANNOT_GET_PROCESS_AFFINITY = 261
    """The process affinity could not be determined."""

    THREAD_AFFINITY_UNAVAILABLE = 262
    """Setting the thread CPU affinity is not currently available on this platform."""

    INCOMPLETE_WRITE = 263
    """This error should never be returned. It is used internally by the Quanser Stream API."""

    PRINT_NUM_WRITTEN_IS_NULL = 264
    """The "number written" argument to a stream_print function is NULL. It must point to an appropriately-sized integer."""

    STREAM_FORMAT_NOT_DEDUCED = 265
    """The character format of the stream can only be deduced from the first bytes in the stream."""

    MISMATCHED_STREAM_FORMAT = 266
    """The character format set for the stream does not match the format indicated by the byte order mark (BOM) in the stream itself."""

    DIRECTX_NOT_INSTALLED = 267
    """Unable to use DirectX. Make sure DirectX 10.0 or above is installed."""

    NO_GAME_CONTROLLERS_ATTACHED = 268
    """There are no game controllers currently attached to the system."""

    CANNOT_ACCESS_GAME_CONTROLLER = 269
    """Unable to access game controller."""

    CANNOT_SET_GAME_CONTROLLER_FORMAT = 270
    """Unable to set data format of game controller."""

    CANNOT_POLL_GAME_CONTROLLER = 271
    """Unable to poll the game controller."""

    CANNOT_GET_GAME_CONTROLLER_STATE = 272
    """Unable to get the state of the game controller."""

    CANNOT_GET_MOUSE_STATE = 273
    """Unable to get the state of the mouse."""

    ETHERCAT_INVALID_BYTE_SIZE = 274
    """Invalid ByteSize field specified for EtherCAT process image."""

    INVALID_ETHERCAT_SOURCE = 275
    """Invalid Source Mac address field for the EtherCAT device."""

    INVALID_ETHERCAT_INITIALIZATION_DATA = 276
    """Invalid Data field in an initialization command for an EtherCAT device."""

    INVALID_ETHERCAT_DATA_LENGTH = 277
    """Invalid DataLength field in an initialization or cyclic command for an EtherCAT device."""

    CANNOT_GET_BUFFER_SIZE = 278
    """It was not possible to get the buffer size."""

    CANNOT_GET_PACKET_SIZE = 279
    """It was not possible to get the maximum packet size."""

    DATAGRAM_TOO_LARGE = 280
    """The datagram received was too large for the buffer provided in the receive operation."""

    NO_DESIGNATED_PEER = 281
    """An attempt was made to send data when no connection has been established with a particular peer. For connectionless protocols like UDP the server-side must receive data from a peer before sending any data in order to establish a "connection"."""

    CANNOT_INDICATE_CLOSURE = 282
    """It was not possible to indicate closure of the connection to the remote peer."""

    INVALID_PEER_OPTION = 283
    """Invalid "peer" option was specified. Valid values for the "peer" option are "one", "any", "broadcast" or "manual"."""

    CANNOT_BROADCAST = 284
    """The communication protocol, such as UDP, could not be configured for broadcasting."""

    ETHERCAT_VALIDATE_DATA_WRONG_LENGTH = 285
    """The Validate/Data field in an initialization command for an EtherCAT device contains data of a different size than the Data or DataLength field."""

    INVALID_ETHERCAT_VALIDATION_DATA = 286
    """Invalid Validate/Data field in an initialization command for an EtherCAT device."""

    ETHERCAT_VALIDATE_MASK_WRONG_LENGTH = 287
    """The Validate/DataMask field in an initialization command for an EtherCAT device contains data of a different size than the Data or DataLength field."""

    INVALID_ETHERCAT_VALIDATION_MASK = 288
    """Invalid Validate/DataMask field in an initialization command for an EtherCAT device."""

    INVALID_ETHERCAT_TIMEOUT = 289
    """Invalid Validate/Timeout field in an initialization command for an EtherCAT device."""

    INVALID_ETHERCAT_BEFORE_SLAVE = 290
    """Invalid BeforeSlave field in an initialization command for an EtherCAT device."""

    INVALID_ETHERCAT_TRANSITION = 291
    """Invalid Transition field in an initialization command for an EtherCAT device."""

    INVALID_ETHERCAT_REQUIRES_FIELD = 292
    """Invalid Requires field in an initialization command for an EtherCAT device."""

    INVALID_ETHERCAT_COMMAND = 293
    """Invalid Cmd field in an initialization or cyclic command for an EtherCAT device."""

    INVALID_ETHERCAT_LOGICAL_ADDRESS = 294
    """Invalid Addr field (logical address) in an initialization or cyclic command for EtherCAT device."""

    INVALID_ETHERCAT_ADDRESS_PAGE = 295
    """Invalid Adp field (physical address page) in an initialization or cyclic command for an EtherCAT device."""

    INVALID_ETHERCAT_ADDRESS_OFFSET = 296
    """Invalid Ado field (physical address offset) in an initialization or cyclic command for an EtherCAT device."""

    INVALID_ETHERCAT_COUNT = 297
    """Invalid Cnt field (working counter value) in an initialization command for an EtherCAT device."""

    INVALID_ETHERCAT_RETRIES = 298
    """Invalid Retries field in an initialization command for an EtherCAT device."""

    INVALID_ETHERCAT_START_ADDRESS = 299
    """Invalid StartAddr field in the mailbox states description for an EtherCAT master."""

    INVALID_ETHERCAT_MAILBOX_SIZE = 300
    """Invalid Count field in the mailbox states description for EtherCAT master."""

    INVALID_ETHERCAT_SLAVE_ADDRESS = 301
    """Invalid PhysAddr field (physical address) in the information section (Info) for an EtherCAT slave."""

    INVALID_ETHERCAT_STATE = 302
    """Invalid State field (slave state) in the cyclic commands for an EtherCAT device."""

    INVALID_ETHERCAT_INPUT_OFFSET = 303
    """Invalid InputOffs field (offset at which a cyclic command reads from the process image) in the cyclic commands for an EtherCAT device."""

    INVALID_ETHERCAT_OUTPUT_OFFSET = 304
    """Invalid OutputOffs field (offset at which a cyclic command writes to the process image) in the cyclic commands for an EtherCAT device."""

    OUT_OF_BAND_DATA_NOT_SUPPORTED = 305
    """The socket does not support receiving out-of-band data in the normal stream."""

    NO_CORRESPONDING_INTERNET_ADDRESS = 306
    """There is no corresponding Internet address for the given MAC address."""

    CANNOT_SET_DESCRIPTOR_FLAGS = 307
    """Unable to set the flags of a file descriptor or socket."""

    NO_ACCESS_TO_SHARED_MEMORY = 308
    """The process does not have permission to create global shared memory. On Vista and later operating systems, creation of global shared memory requires SeCreateGlobalPrivilege. This privilege is only enabled by default for administrators, services and the local system account. Try adding the local=yes option to the URI e.g. "shmem://mymem:1?local=yes"."""

    SEMAPHORE_NOT_FOUND = 309
    """The named semaphore could not be found."""

    SEMAPHORE_ALREADY_EXISTS = 310
    """The named semaphore already exists."""

    NO_CORRESPONDING_NETWORK_CARD = 311
    """There is no corresponding network card for the given MAC address."""

    PATH_IN_URI = 312
    """The given protocol does not support paths in the URI. Separate options from the hostname and port using a '?' rather than a '/', much like an HTTP query."""

    UNSUPPORTED_BAUD_RATE = 313
    """The given serial baud rate is not supported."""

    ETHERCAT_MASTER_ALREADY_RUNNING = 314
    """An EtherCAT master is already running on the given MAC address. Stop the existing EtherCAT master first."""

    MISSING_CLOCK_MODES = 315
    """Clocks have been specified but not enough clock modes have been provided."""

    MISSING_ENCODER_COUNTS = 316
    """Encoder input channels have been specified but not enough encoder counts have been provided."""

    MISSING_PWM_MODES = 317
    """PWM output channels have been specified but not enough PWM modes have been provided."""

    MISSING_PWM_FREQUENCIES = 318
    """PWM output channels have been specified but not enough PWM frequencies have been provided."""

    MISSING_PWM_DUTY_CYCLES = 319
    """PWM output channels have been specified but not enough PWM duty cycles have been provided."""

    INVALID_NUMBER_OF_SAMPLES_IN_BUFFER = 320
    """The number of samples in the task buffer must be greater than zero."""

    INVALID_NUMBER_OF_SAMPLES = 321
    """The number of samples requested in the read or write operation must be greater than zero."""

    ETHERCAT_DATAGRAM_TOO_LARGE = 322
    """The EtherCAT datagram to be sent is too large. Check the XML description."""

    NO_MORE_ETHERCAT_PACKETS = 323
    """The EtherCAT master puts a limit on the number of packets which may be queued for transmission. This limit has been exceeded so no more packets are available."""

    INVALID_ETHERCAT_CYCLIC_COMMAND = 324
    """The EtherCAT process image either could not be created or is not large enough for one of the cyclic command specified in the XML."""

    AUTOPILOT_ARGUMENT_IS_NULL = 325
    """The autopilot argument to val_open is NULL."""

    AUTOPILOT_TYPE_ARGUMENT_IS_NULL = 326
    """The autopilot type argument to val_open is NULL."""

    INVALID_AUTOPILOT_HANDLE = 327
    """The given t_autopilot handle is not a valid autopilot."""

    URI_HOSTNAME_TOO_LONG = 328
    """The hostname specified in the URI is too long."""

    URI_SCHEME_TOO_LONG = 329
    """The scheme specified in the URI is too long."""

    INVALID_CHANNEL = 330
    """The given t_channel handle is not valid."""

    ARCNET_NODE_ID_OUT_OF_BOUNDS = 331
    """The given ARCNET node ID is out of bounds (0-255)."""

    ARCNET_CANNOT_OPEN = 332
    """Cannot open and initialize the ARCNET board."""

    ARCNET_TARGET_NODE_DNE = 333
    """The ARCNET message cannot be sent because there is no node on the network with the given target node ID."""

    ARCNET_EXCESSIVE_NAKS = 334
    """The ARCNET transmission failed due to excessive NAKs."""

    ETHERCAT_PACKET_LOST = 335
    """An EtherCAT packet that was sent was lost and never returned. The slave device was not ready."""

    ETHERCAT_TELEGRAM_LOST = 336
    """An EtherCAT telegram that was sent within a packet was not present in the packet when the packet returned. Data corruption has occurred!"""

    INVALID_ETHERCAT_FRAME_LENGTH = 337
    """The telegrams within an EtherCAT packet do not fit within the EtherCAT frame. Packet is corrupted!"""

    ETHERCAT_COMMAND_TIMED_OUT = 338
    """An EtherCAT slave did not respond as expected within the timeout interval."""

    INVALID_ETHERCAT_TELEGRAM_LENGTH = 339
    """An EtherCAT telegram received from a slave was a different size than the telegram originally sent. Telegram is corrupted!"""

    INVALID_ETHERCAT_MASTER_STATE = 340
    """EtherCAT master cannot be set to the state requested. The state is not valid for the master."""

    INVALID_THREAD = 341
    """The given thread handle is not valid."""

    CANNOT_INITIALIZE_PA10 = 342
    """The PA10 cannot be properly initialized due to an error."""

    CANNOT_CLOSE_PA10 = 343
    """An error occurred while attempting to stop and close the PA10."""

    PGR_CANNOT_INITIALIZE_CAMERA = 344
    """An error occurred while attempting to initialize the PGR camera."""

    PGR_CANNOT_GRAB_IMAGE = 345
    """An error occurred while attempting to grab an image using the PGR camera."""

    PGR_GRAB_IMAGE_TIMEOUT = 346
    """A timeout occurred while attempting to grab an image using the PGR camera."""

    PGR_CANNOT_CLOSE = 347
    """An error occurred while attempting to close the PGR camera."""

    PGR_INVALID_CUSTOM_IMAGE_SIZE = 348
    """Starting the camera failed because the custom image size is invalid."""

    PGR_INVALID_IMAGE_DIMS = 349
    """The dimensions of the image are not valid. The image must have 3 dimensions."""

    IMAGE_CANNOT_CONVERT = 350
    """An error occurred attempting to convert the source image."""

    MISSING_ETHERCAT_COMMAND = 351
    """Missing Cmd node within an InitCmd in EtherCAT XML configuration file. The Cmd node identifies the EtherCAT command and is a required field."""

    MISSING_ETHERCAT_LOGICAL_ADDRESS = 352
    """Missing Addr node within an InitCmd in EtherCAT XML configuration file. The Addr node identifies the logical address and is a required field when a LRD, LWR or LRW command is used."""

    MISSING_ETHERCAT_ADDRESS_PAGE = 353
    """Missing Adp node within an InitCmd in EtherCAT XML configuration file. The Adp node identifies the address page and is a required field when a command other than LRD, LWR or LRW is used."""

    MISSING_ETHERCAT_ADDRESS_OFFSET = 354
    """Missing Ado node within an InitCmd in EtherCAT XML configuration file. The Ado node identifies the address offset and is a required field when a command other than LRD, LWR or LRW is used."""

    MISSING_ETHERCAT_COMMENT = 355
    """Missing Comment node within an InitCmd in EtherCAT XML configuration file. The Comments node provides information about the command and is a required field."""

    MISSING_ETHERCAT_DATA = 356
    """Missing Data or DataLength node within an InitCmd in EtherCAT XML configuration file. Either the Data node or the DataLength node is required because they provide the data for the command."""

    MISSING_ETHERCAT_VALIDATE_DATA = 357
    """Missing Data node within the Validate section of an InitCmd in EtherCAT XML configuration file. The Data node provides the data used to validate the response from the slaves and is a required field in the Validate section."""

    MISSING_ETHERCAT_TRANSITION = 358
    """Missing Transition node within an InitCmd in EtherCAT XML configuration file. The Transition nodes indicate the state transitions forward to the command should be executed and is a required field."""

    MISSING_ETHERCAT_RETRIES = 359
    """Missing Retries node within an InitCmd in EtherCAT XML configuration file. The Retries node indicates how many times the EtherCAT stack attempts to resend the command and is a required field."""

    MISSING_ETHERCAT_SLAVE_INFO = 360
    """Missing Info node within a Slave in EtherCAT XML configuration file. The Info node includes information about the slave and is a required field."""

    MISSING_ETHERCAT_SLAVE_COMMANDS = 361
    """Missing InitCmds section within a Slave in EtherCAT XML configuration file. The InitCmds section includes all the EtherCAT initialization commands for the slave and is required."""

    MISSING_ETHERCAT_SLAVE_COMMAND = 362
    """Missing InitCmd node within a Slave in EtherCAT XML configuration file. The InitCmd node identifies an EtherCAT initialization command for a slave and is required."""

    MISSING_ETHERCAT_SLAVE_NAME = 363
    """Missing Name node within a Slave in EtherCAT XML configuration file. The Name node identifies the name of the slave and is required."""

    MISSING_ETHERCAT_CYCLIC_STATE = 364
    """Missing State node within a cyclic Cmd node in EtherCAT XML configuration file. The State nodes identify the states in which the cyclic command should be sent and one is required."""

    MISSING_ETHERCAT_MASTER_INFO = 365
    """Missing Info node within the Master section of an EtherCAT XML configuration file. The Info node includes information about the master and is a required field."""

    MISSING_ETHERCAT_MASTER_SOURCE = 366
    """Missing Source node within the Master section of an EtherCAT XML configuration file. The Source node identifies the Mac address to be used by the master and is a required field."""

    MISSING_ETHERCAT_MASTER_COMMANDS = 367
    """Missing InitCmds section within the Master section of an EtherCAT XML configuration file. The InitCmds section includes all the EtherCAT initialization commands for the master and is required."""

    MISSING_ETHERCAT_MASTER_COMMAND = 368
    """Missing InitCmd node within the Master section of an EtherCAT XML configuration file. The InitCmd node identifies an EtherCAT initialization command for the master and is required."""

    MISSING_ETHERCAT_MAILBOX_START_ADDRESS = 369
    """Missing StartAddr node within the MailboxStates section of an EtherCAT XML configuration file. The StartAddr node identifies the starting address of the mailbox and is required."""

    MISSING_ETHERCAT_MAILBOX_COUNT = 370
    """Missing Count node within the MailboxStates section of an EtherCAT XML configuration file. The Count node identifies the length of the mailbox and is required."""

    MISSING_ETHERCAT_CONFIGURATION = 371
    """Missing Config node within the EtherCAT XML configuration file. The Config node identifies the EtherCAT configuration and is required."""

    MISSING_ETHERCAT_SLAVE = 372
    """Missing Slave node within the EtherCAT XML configuration file. The Slave node identifies an EtherCAT Slave and at least one is required."""

    MISSING_ETHERCAT_MASTER = 373
    """Missing Master node within the EtherCAT XML configuration file. The Master node identifies the EtherCAT master and is required."""

    MISSING_ETHERCAT_PROCESS_IMAGE = 374
    """Missing ProcessImage node within the EtherCAT XML configuration file. The ProcessImage node describes the EtherCAT process image configuration and is required."""

    MISSING_ETHERCAT_PROCESS_INPUTS = 375
    """Missing Inputs node within the ProcessImage section of the EtherCAT XML configuration file. The Inputs node describes the EtherCAT input process image and is required."""

    MISSING_ETHERCAT_PROCESS_INPUTS_SIZE = 376
    """Missing ByteSize node within the ProcessImage/Inputs section of the EtherCAT XML configuration file. The ByteSize node describes the size of the EtherCAT input process image and is required."""

    MISSING_ETHERCAT_PROCESS_OUTPUTS = 377
    """Missing Outputs node within the ProcessImage section of the EtherCAT XML configuration file. The Outputs node describes the EtherCAT output process image and is required."""

    MISSING_ETHERCAT_PROCESS_OUTPUTS_SIZE = 378
    """Missing ByteSize node within the ProcessImage/Outputs section of the EtherCAT XML configuration file. The ByteSize node describes the size of the EtherCAT output process image and is required."""

    NO_DYNAMIC_RECONFIGURATION_LICENSE = 379
    """You do not have a valid license for the Dynamic Reconfiguration blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    NO_COMMUNICATIONS_LICENSE = 380
    """You do not have a valid license for the Quanser Communications blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    NO_ETHERCAT_LICENSE = 381
    """You do not have a valid license for the EtherCAT blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    CANNOT_OPEN_LICENSE_FILE = 382
    """Unable to open license file. Make sure that the file exists and you have permission to read the license file. Mapped network drives are not accessible with elevated privileges. Use the full UNC path, such as "\\server\licenses\john-doe.qlic", instead."""

    INVALID_LICENSE_FILE = 383
    """The license file is invalid. Choose a different license file."""

    CANNOT_CREATE_PREFERENCES_NODE = 384
    """It was not possible to create the preferences node. You may not have sufficient privileges."""

    MISSING_ANALOG_MINIMUMS = 385
    """No analog minimums were specified when setting the analog ranges, even though the number of channels indicated was non-zero."""

    MISSING_ANALOG_MAXIMUMS = 386
    """No analog maximums were specified when setting the analog ranges, even though the number of channels indicated was non-zero."""

    CANNOT_READ_SCHUNK_GRIPPER = 387
    """An error occurred while attempting to read the state of the SCHUNK gripper."""

    SCHUNK_CANNOT_INIT = 388
    """An error occurred initializing the SCHUNK gripper device."""

    SCHUNK_CANNOT_HALT = 389
    """Cannot halt the SCHUNK gripper device."""

    SCHUNK_CANNOT_CLOSE = 390
    """An error occurred while attempting to close the SCHUNK gripper device."""

    SCHUNK_CANNOT_MOVE_POS = 391
    """An error occurred attempting to issue a move command to the SCHUNK gripper device."""

    SCHUNK_CANNOT_MOVE_VEL = 392
    """An error occurred attempting to issue a velocity command to the SCHUNK gripper device."""

    SCHUNK_CANNOT_MOVE_CUR = 393
    """An error occurred attempting to issue a current command to the SCHUNK gripper device."""

    SCHUNK_CANNOT_HOME = 394
    """Cannot home the SCHUNK gripper device."""

    SCHUNK_INVALID_CONTROL_MODE = 395
    """The specified control mode for the Schunk gripper is invalid."""

    SCHUNK_EXT_MODE_NOT_CONNECTED = 396
    """The 'mode' input signal must be connected when the Control mode external parameter is set."""

    INVALID_ANALOG_INPUT_RANGE = 397
    """One of the ranges specified for an analog input channel is not valid for the selected hardware."""

    INVALID_ANALOG_OUTPUT_RANGE = 398
    """One of the ranges specified for an analog output channel is not valid for the selected hardware."""

    CARD_IDENTIFIER_ARGUMENT_IS_NULL = 399
    """The card identifier argument to hil_open is NULL."""

    BOARD_IDENTIFIER_ARGUMENT_IS_NULL = 400
    """The board identifier argument passed to the board-specific HIL driver is NULL. This situation should never occur unless the user is calling the board-specific driver directly or memory has been corrupted."""

    INVALID_BOARD_IDENTIFIER = 401
    """The board identifier is not valid. The zero-based index of the board is typically used as the board identifier, although NI boards may also be identified by their name in MAX."""

    INVALID_DEVICE_HANDLE = 402
    """The handle to the device is invalid."""

    CANNOT_OPEN_DRIVER_DIRECTORY = 403
    """An attempt to get the driver directory failed."""

    WIIMOTE_WRITE_REPORT_FAILED = 404
    """An attempt to write the wiimote report failed."""

    WIIMOTE_CANNOT_CALIBRATE = 405
    """Failed to read calibration information from the wiimote. Make sure the wiimote is on and connected to the receiving device."""

    WIIMOTE_CANNOT_OPEN = 406
    """Failed to open a connection to the wiimote."""

    WIIMOTE_READ_FAILED = 407
    """A wiimote read request failed."""

    WIIMOTE_NOT_FOUND = 408
    """Unable to find the wiimote with the specified wiimote number. Make sure the wiimote number is valid and that the wiimote is powered on and connected."""

    INVALID_WIIMOTE_DEVICE_HANDLE = 409
    """Unable to open a handle to the wiimote device. The wiimote is possibly already opened by another process."""

    DAQMX_CANNOT_CLEAR_TASK = 410
    """DAQmx was unable to clear or release a National Instruments task. Try restarting MATLAB."""

    DAQMX_CANNOT_CREATE_TASK = 411
    """DAQmx was unable to create a new task. The resource may already be in use by another block."""

    DAQMX_CANNOT_ATTACH_ADC_TO_TASK = 412
    """DAQmx was unable to attach the specified analog input to the analog input task."""

    DAQMX_CANNOT_START_TASK = 413
    """DAQmx was unable to start the National Instruments device task. Make sure the device is not already open. If no devices are open, try restarting MATLAB."""

    DAQMX_ERROR_SAMPLING_ADC = 414
    """DAQmx failed to execute the National Instruments analog input task."""

    DAQMX_ERROR_RESETTING_DEVICE = 415
    """DAQmx failed to reset the device."""

    DAQMX_CANNOT_ATTACH_DAC_TO_TASK = 416
    """DAQmx was unable to attach the specified analog output to the National Instruments analog output task."""

    DAQMX_ERROR_WRITING_DAC = 417
    """DAQmx failed to output the requested analog value."""

    ANALOG_OUTPUT_RANGE_DIFF = 418
    """All analog output channels must have the same output range for this board."""

    ANALOG_INPUT_RANGE_DIFF = 419
    """All analog input channels must have the same input range for this board."""

    DAQMX_CANNOT_SET_HARDWARE_CLOCK_RATE = 420
    """Error setting the hardware timing for the time-base block."""

    DAQMX_CLOCK_ERROR_WAITING_FOR_SAMPLE = 421
    """Either the configuration is invalid, or a sample edge was missed before executing the wait."""

    DAQMX_CANNOT_ATTACH_ENCODER_TO_TASK = 422
    """DAQmx was unable to attach the specified channel to the National Instruments encoder input task."""

    DAQMX_ERROR_SAMPLING_ENCODER = 423
    """DAQmx failed to execute the National Instruments encoder input task."""

    DAQMX_ERROR_CHANGING_ENC_DIR_SRC = 424
    """DAQmx failed to change the source for the encoder count direction."""

    DAQMX_CANNOT_ATTACH_DIGITAL_TO_TASK = 425
    """DAQmx was unable to attach the specified digital lines to the National Instruments task."""

    DAQMX_ERROR_SAMPLING_DIGITAL = 426
    """DAQmx failed to execute the digital read task."""

    DAQMX_ERROR_WRITING_DIGITAL = 427
    """DAQmx failed to output the requested digital values."""

    JR3PCI_CANNOT_INIT = 428
    """Cannot initialize the JR3 PCI force torque sensor."""

    BUFFER_IS_NULL = 429
    """The buffer argument is NULL. It should be a valid pointer."""

    DIGITAL_OUTPUT_LOCKED = 430
    """The requested digital output is locked.  If you need access to this line, use the generic version of this driver."""

    ANALOG_OUTPUT_LOCKED = 431
    """The requested analog output is locked.  If you need access to this channel, use the generic version of this driver."""

    PWM_OUTPUT_LOCKED = 432
    """The requested PWM output is locked.  If you need access to this channel, use the generic version of this driver."""

    MISSING_URI_OPTION_NAME = 433
    """No option name was found even though a value was specified."""

    ENCODER_QUADRATURE_MODE_NOT_SUPPORTED = 434
    """The selected quadrature decoding is not available for this board."""

    MISSING_ENCODER_QUADRATURE_MODES = 435
    """Encoder input channels have been specified but not enough encoder quadrature modes have been provided."""

    INVALID_ENCODER_QUADRATURE_MODE = 436
    """One of the encoder quadrature modes specified was not a valid mode. Valid modes are 0, 1, 2 or 4."""

    MISSING_ENCODER_FILTER_FREQUENCIES = 437
    """Encoder input channels have been specified but not enough encoder filter frequencies have been provided."""

    INVALID_ENCODER_FILTER_FREQUENCY = 438
    """One of the encoder filter frequencies specified was not a valid frequency. The frequency is out of range or negative."""

    HIL_READ_NOT_SUPPORTED = 439
    """The hil_read function in C or MATLAB and HIL Read block in QUARC are not supported by this particular card."""

    HIL_READ_ANALOG_NOT_SUPPORTED = 440
    """The hil_read_analog function in C or MATLAB and HIL Read Analog block in QUARC are not supported by this particular card."""

    HIL_READ_ANALOG_BUFFER_NOT_SUPPORTED = 441
    """The hil_read_analog_buffer function and HIL Read Analog Buffer block are not supported by this particular card."""

    HIL_READ_ANALOG_CODES_NOT_SUPPORTED = 442
    """The hil_read_analog_codes function and HIL Read Analog Codes block are not supported by this particular card."""

    HIL_READ_ANALOG_WRITE_ANALOG_NOT_SUPPORTED = 443
    """The hil_read_analog_write_analog function and HIL Read Analog Write Analog block are not supported by this particular card."""

    HIL_READ_ANALOG_WRITE_ANALOG_BUFFER_NOT_SUPPORTED = 444
    """The hil_read_analog_write_analog_buffer function and HIL Read Analog Write Analog Buffer block are not supported by this particular card."""

    HIL_READ_BUFFER_NOT_SUPPORTED = 445
    """The hil_read_buffer function and HIL Read Buffer block are not supported by this particular card."""

    HIL_READ_DIGITAL_NOT_SUPPORTED = 446
    """The hil_read_digital function in C or MATLAB and HIL Read Digital block in QUARC are not supported by this particular card."""

    HIL_READ_DIGITAL_BUFFER_NOT_SUPPORTED = 447
    """The hil_read_digital_buffer function and HIL Read Digital Buffer block are not supported by this particular card."""

    HIL_READ_DIGITAL_WRITE_DIGITAL_NOT_SUPPORTED = 448
    """The hil_read_digital_write_digital function and HIL Read Digital Write Digital block are not supported by this particular card."""

    HIL_READ_DIGITAL_WRITE_DIGITAL_BUFFER_NOT_SUPPORTED = 449
    """The hil_read_digital_write_digital_buffer function and HIL Read Digital Write Digital Buffer block are not supported by this particular card."""

    HIL_READ_ENCODER_NOT_SUPPORTED = 450
    """The hil_read_encoder function in C or MATLAB and HIL Read Encoder block in QUARC are not supported by this particular card."""

    HIL_READ_ENCODER_BUFFER_NOT_SUPPORTED = 451
    """The hil_read_encoder_buffer function and HIL Read Encoder Buffer block are not supported by this particular card."""

    HIL_READ_ENCODER_WRITE_PWM_NOT_SUPPORTED = 452
    """The hil_read_encoder_write_pwm function and HIL Read Encoder Write PWM block are not supported by this particular card."""

    HIL_READ_ENCODER_WRITE_PWM_BUFFER_NOT_SUPPORTED = 453
    """The hil_read_encoder_write_pwm_buffer function and HIL Read Encoder Write PWM Buffer block are not supported by this particular card."""

    HIL_READ_OTHER_NOT_SUPPORTED = 454
    """The hil_read_other function in C or MATLAB and HIL Read Other block in QUARC are not supported by this particular card."""

    HIL_READ_OTHER_BUFFER_NOT_SUPPORTED = 455
    """The hil_read_other_buffer function and HIL Read Other Buffer block are not supported by this particular card."""

    HIL_READ_OTHER_WRITE_OTHER_NOT_SUPPORTED = 456
    """The hil_read_other_write_other function and HIL Read Write Other block are not supported by this particular card."""

    HIL_READ_OTHER_WRITE_OTHER_BUFFER_NOT_SUPPORTED = 457
    """The hil_read_other_write_other_buffer function and HIL Read Other Write Other Buffer block are not supported by this particular card."""

    HIL_READ_WRITE_NOT_SUPPORTED = 458
    """The hil_read_write function and HIL Read Write block are not supported by this particular card. Try using a more specific function or block."""

    HIL_READ_WRITE_BUFFER_NOT_SUPPORTED = 459
    """The hil_read_write_buffer function and HIL Read Write Buffer block are not supported by this particular card. Try using a more specific function or block."""

    HIL_SET_ANALOG_INPUT_RANGES_NOT_SUPPORTED = 460
    """The hil_set_analog_input_ranges function is not supported by this particular card. It may be necessary to uncheck the two "Set analog input parameters..." options in the HIL Initialize block."""

    HIL_SET_ANALOG_OUTPUT_RANGES_NOT_SUPPORTED = 461
    """The hil_set_analog_output_ranges function is not supported by this particular card. It may be necessary to uncheck the two "Set analog output parameters..." options in the HIL Initialize block."""

    HIL_SET_CARD_SPECIFIC_OPTIONS_NOT_SUPPORTED = 462
    """The hil_set_card_specific_options function is not supported by this particular card. It may be necessary to uncheck the two "Set clock parameters..." options in the HIL Initialize block."""

    HIL_SET_CLOCK_MODE_NOT_SUPPORTED = 463
    """The hil_set_clock_mode function is not supported by this particular card."""

    HIL_SET_DIGITAL_DIRECTIONS_NOT_SUPPORTED = 464
    """The hil_set_digital_directions function is not supported by this particular card. Set the "Digital input channels" and "Digital output channels" parameters in the HIL Initialize block to empty matrices: []."""

    HIL_SET_ENCODER_COUNTS_NOT_SUPPORTED = 465
    """The hil_set_encoder_counts function and HIL Set Encoder Counts block are not supported by this particular card. It may be necessary to uncheck the two "Set initial encoder counts..." options in the HIL Initialize block."""

    HIL_SET_ENCODER_FILTER_FREQUENCY_NOT_SUPPORTED = 466
    """The hil_set_encoder_filter_frequency function is not supported by this particular card. It may be necessary to set the "Encoder filter frequency" parameter in the HIL Initialize block to an empty matrix: []."""

    HIL_SET_ENCODER_QUADRATURE_MODE_NOT_SUPPORTED = 467
    """The hil_set_encoder_quadrature_mode function is not supported by this particular card. It may be necessary to set the "Encoder quadrature" parameter in the HIL Initialize block to an empty matrix: []."""

    HIL_SET_PWM_DUTY_CYCLE_NOT_SUPPORTED = 468
    """The hil_set_pwm_duty_cycle function is not supported by this particular card. It may be necessary to uncheck the two "Set PWM output parameters..." options in the HIL Initialize block."""

    HIL_SET_PWM_FREQUENCY_NOT_SUPPORTED = 469
    """The hil_set_pwm_frequency function is not supported by this particular card. It may be necessary to uncheck the two "Set PWM output parameters..." options in the HIL Initialize block."""

    HIL_SET_PWM_MODE_NOT_SUPPORTED = 470
    """The hil_set_pwm_mode function is not supported by this particular card. It may be necessary to uncheck the two "Set PWM output parameters..." options in the HIL Initialize block."""

    HIL_TASK_CREATE_ANALOG_READER_NOT_SUPPORTED = 471
    """The hil_task_create_analog_reader function and HIL Read Analog Timebase block are not supported by this particular card."""

    HIL_TASK_CREATE_ANALOG_READER_ANALOG_WRITER_NOT_SUPPORTED = 472
    """The hil_task_create_analog_reader_analog_writer function and HIL Read Analog Write Analog Timebase block are not supported by this particular card."""

    HIL_TASK_CREATE_DIGITAL_READER_NOT_SUPPORTED = 473
    """The hil_task_create_digital_reader function and HIL Read Digital Timebase block are not supported by this particular card."""

    HIL_TASK_CREATE_DIGITAL_READER_DIGITAL_WRITER_NOT_SUPPORTED = 474
    """The hil_task_create_digital_reader_digital_writer function and HIL Read Digital Write Digital Timebase block are not supported by this particular card."""

    HIL_TASK_CREATE_DIGITAL_WRITER_NOT_SUPPORTED = 475
    """The hil_task_create_digital_writer function that HIL Write Digital Timebase block are not supported by this particular card."""

    HIL_TASK_CREATE_ENCODER_READER_NOT_SUPPORTED = 476
    """The hil_task_create_encoder_reader function and HIL Read Encoder Timebase block are not supported by this particular card."""

    HIL_TASK_CREATE_ENCODER_READER_PWM_WRITER_NOT_SUPPORTED = 477
    """The hil_task_create_encoder_reader_pwm_writer function and HIL Read Encoder Write PWM Timebase block are not supported by this particular card."""

    HIL_TASK_CREATE_OTHER_READER_NOT_SUPPORTED = 478
    """The hil_task_create_other_reader function and HIL Read Other Timebase block are not supported by this particular card."""

    HIL_TASK_CREATE_OTHER_READER_OTHER_WRITER_NOT_SUPPORTED = 479
    """The hil_task_create_other_reader_other_writer function and HIL Read Other Write Other Timebase block are not supported by this particular card."""

    HIL_TASK_CREATE_OTHER_WRITER_NOT_SUPPORTED = 480
    """The hil_task_create_other_writer function and HIL Write Other Timebase block are not supported by this particular card."""

    HIL_TASK_CREATE_PWM_WRITER_NOT_SUPPORTED = 481
    """The hil_task_create_pwm_writer function and HIL Write PWM Timebase block are not supported by this particular card."""

    HIL_TASK_CREATE_READER_NOT_SUPPORTED = 482
    """The hil_task_create_reader function and HIL Read Timebase block are not supported by this particular card. Try one of the more specific functions or blocks."""

    HIL_TASK_CREATE_READER_WRITER_NOT_SUPPORTED = 483
    """The hil_task_create_reader_writer function and HIL Read Write Timebase block are not supported by this particular card. Try one of the more specific functions or blocks."""

    HIL_TASK_CREATE_WRITER_NOT_SUPPORTED = 484
    """The hil_task_create_writer function and HIL Write Timebase block are not supported by this particular card. Try one of the more specific functions or blocks."""

    HIL_TASK_DELETE_NOT_SUPPORTED = 485
    """The hil_task_delete function is not supported by this particular card. If one of the hil_task_create... functions is supported then the hil_task_delete function MUST be supported! In this case, contact the driver manufacturer."""

    HIL_TASK_FLUSH_NOT_SUPPORTED = 486
    """The hil_task_flush function is not supported by this particular card. If one of the hil_task_write... functions is supported then the hil_task_flush function MUST be supported! In this case, contact the driver manufacturer."""

    HIL_TASK_READ_NOT_SUPPORTED = 487
    """The hil_task_read function is not supported by this particular card. Try one of the more specific functions."""

    HIL_TASK_READ_ANALOG_NOT_SUPPORTED = 488
    """The hil_task_read_analog function is not supported by this particular card."""

    HIL_TASK_READ_ANALOG_WRITE_ANALOG_NOT_SUPPORTED = 489
    """The hil_task_read_analog_write_analog function is not supported by this particular card."""

    HIL_TASK_READ_DIGITAL_NOT_SUPPORTED = 490
    """The hil_task_read_digital function is not supported by this particular card."""

    HIL_TASK_READ_DIGITAL_WRITE_DIGITAL_NOT_SUPPORTED = 491
    """The hil_task_read_digital_write_digital function is not supported by this particular card."""

    HIL_TASK_READ_ENCODER_NOT_SUPPORTED = 492
    """The hil_task_read_encoder function is not supported by this particular card."""

    HIL_TASK_READ_ENCODER_WRITE_PWM_NOT_SUPPORTED = 493
    """The hil_task_read_encoder_write_pwm function is not supported by this particular card."""

    HIL_TASK_READ_OTHER_NOT_SUPPORTED = 494
    """The hil_task_read_other function is not supported by this particular card."""

    HIL_TASK_READ_OTHER_WRITE_OTHER_NOT_SUPPORTED = 495
    """The hil_task_read_other_write_other function is not supported by this particular card."""

    HIL_TASK_READ_WRITE_NOT_SUPPORTED = 496
    """The hil_task_read_write function is not supported by this particular card. Try one of the more specific functions."""

    HIL_TASK_START_NOT_SUPPORTED = 497
    """The hil_task_start function is not supported by this particular card. If one of the hil_task_create... functions is supported then the hil_task_start function MUST be supported! In this case, contact the driver manufacturer."""

    HIL_TASK_STOP_NOT_SUPPORTED = 498
    """The hil_task_stop function is not supported by this particular card. If one of the hil_task_create... functions is supported then the hil_task_stop function MUST be supported! In this case, contact the driver manufacturer."""

    HIL_TASK_WRITE_NOT_SUPPORTED = 499
    """The hil_task_write function is not supported by this particular card. Try one of the more specific functions."""

    HIL_TASK_WRITE_ANALOG_NOT_SUPPORTED = 500
    """The hil_task_write_analog function is not supported by this particular card."""

    HIL_TASK_WRITE_DIGITAL_NOT_SUPPORTED = 501
    """The hil_task_write_digital function is not supported by this particular card."""

    HIL_TASK_WRITE_OTHER_NOT_SUPPORTED = 502
    """The hil_task_write_other function is not supported by this particular card."""

    HIL_TASK_WRITE_PWM_NOT_SUPPORTED = 503
    """The hil_task_write_pwm function is not supported by this particular card."""

    HIL_WRITE_NOT_SUPPORTED = 504
    """The hil_write function in C or MATLAB and HIL Write block in QUARC are not supported by this particular card."""

    HIL_WRITE_ANALOG_NOT_SUPPORTED = 505
    """The hil_write_analog function in C or MATLAB and HIL Write Analog block in QUARC are not supported by this particular card. You might need to change a board specific option to enable it."""

    HIL_WRITE_ANALOG_BUFFER_NOT_SUPPORTED = 506
    """The hil_write_analog_buffer function and HIL Write Analog Buffer block are not supported by this particular card."""

    HIL_WRITE_ANALOG_CODES_NOT_SUPPORTED = 507
    """The hil_write_analog_codes function and HIL Write Analog Codes block are not supported by this particular card."""

    HIL_WRITE_BUFFER_NOT_SUPPORTED = 508
    """The hil_write_buffer function and HIL Write Buffer block are not supported by this particular card. Try using one of the more specific functions or blocks."""

    HIL_WRITE_DIGITAL_NOT_SUPPORTED = 509
    """The hil_write_digital function in C or MATLAB and HIL Write Digital block in QUARC are not supported by this particular card."""

    HIL_WRITE_DIGITAL_BUFFER_NOT_SUPPORTED = 510
    """The hil_write_digital_buffer function and HIL Write Digital Buffer block are not supported by this particular card."""

    HIL_WRITE_OTHER_NOT_SUPPORTED = 511
    """The hil_write_other function in C or MATLAB and HIL Write Other block in QUARC are not supported by this particular card."""

    HIL_WRITE_OTHER_BUFFER_NOT_SUPPORTED = 512
    """The hil_write_other_buffer function and HIL Write Other Buffer block are not supported by this particular card."""

    HIL_WRITE_PWM_NOT_SUPPORTED = 513
    """The hil_write_pwm function in C or MATLAB and HIL Write PWM block in QUARC are not supported by this particular card. You might need to change a board specific option to enable it."""

    HIL_WRITE_PWM_BUFFER_NOT_SUPPORTED = 514
    """The hil_write_pwm_buffer function and HIL Write PWM Buffer block are not supported by this particular card."""

    Q3_CONTROLPAQ_FW_CANNOT_OPEN_BOARD = 515
    """The specified Q3 ControlPaQ-FW board could not be opened. Check that the board is powered and properly connected and that the board number is correct."""

    CANNOT_CREATE_GAME_CONTROLLER_WINDOW = 516
    """Unable to create a window for the force feedback game controller."""

    CANNOT_SET_GAME_CONTROLLER_COOPERATIVE_LEVEL = 517
    """Unable to set the cooperation level of the force feedback game controller."""

    CONNECTION_NOT_BOUND = 518
    """The connection has not been bound. This error typically occurs with UDP client sockets whenever a receive operation is attempted prior to the first send operation. UDP client sockets are implicitly bound to the UDP port by the first send operation. Hence, a send must always be done first after a UDP client connection is established."""

    NO_SIMULINK_DEVELOPMENT_LICENSE = 519
    """You do not have a valid license for the QUARC Simulink Development Environment. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    INVALID_CIRCULAR_BUFFER = 520
    """The circular buffer is invalid. A circular buffer may not be used after it has been closed."""

    READ_TOO_LONG = 521
    """The amount of data requested in a read operation is too long. For example, you cannot read more bytes from a circular buffer than are contained in the buffer."""

    WRITE_TOO_LONG = 522
    """The amount of data provided in a write operation is too long. For example, you cannot write more bytes to a circular buffer than can be contained in the buffer."""

    TOO_MANY_FORCE_FEEDBACK_EFFECTS = 523
    """It is not possible to add another force feedback effect because the maximum number of force feedback effects has already been reached. Change the maximum number of force feedback effects in the Host Force Feedback Game Controller block."""

    INVALID_FORCE_FEEDBACK_AXIS = 524
    """An invalid axis number was specified for a force feedback effect. Axes numbers must range from 0 to 5, corresponding to x, y, z, Rx, Ry and Rz axes respectively."""

    CANNOT_CREATE_FORCE_FEEDBACK_EFFECT = 525
    """Unable to create a force feedback effect. The device may be out of memory for effects or the effect is not supported."""

    CANNOT_START_FORCE_FEEDBACK_EFFECT = 526
    """Unable to download or start a force feedback effect. The device may be out of memory."""

    CANNOT_STOP_FORCE_FEEDBACK_EFFECT = 527
    """Unable to stop a force feedback effect."""

    CANNOT_SET_FORCE_FEEDBACK_EFFECT_PARAMETERS = 528
    """Unable to set the parameters of a force feedback effect. The parameters may be incorrect or unsupported by the device."""

    INVALID_FORCE_FEEDBACK_EFFECT = 529
    """The given force feedback effect is invalid and does not belong to the game controller specified. The effect may not be supported by the game controller. Also, once an effect has been removed it cannot be used."""

    INVALID_GAME_CONTROLLER = 530
    """The specified game controller is invalid."""

    GAME_CONTROLLER_NOT_FOUND = 531
    """The specified game controller could not be found. A Host Force Feedback Game Controller block for the game controller is required in the same diagram to use the other Force Feedback blocks. There should only be one Host Force Feedback Game Controller block per game controller. Also ensure that the Host Force Feedback Game Controller block comes before the other Force Feedback blocks in the sorted (execution) order."""

    CANNOT_START_TARGET_MANAGER = 532
    """The QUARC Target Manager could not be started."""

    CANNOT_STOP_TARGET_MANAGER = 533
    """The QUARC Target Manager could not be stopped."""

    PEER_IGNORING_SHUTDOWN = 534
    """The peer is not responding to the connection being shut down. The receive operation has timed out."""

    INVALID_PERIODIC_EFFECT_TYPE = 535
    """An invalid periodic effect type was passed to the game_controller_add_periodic_force_effect function."""

    INVALID_CONDITION_EFFECT_TYPE = 536
    """An invalid condition effect type was passed to the game_controller_add_condition_force_effect function."""

    TOO_MANY_GAME_CONTROLLER_AXES = 537
    """No more than six axes may be specified for a game controller force effect."""

    INVALID_NUMBER_OF_CONDITIONS = 538
    """Invalid number of conditions for a condition force effect. There may be one condition for all axes or one condition for each axis."""

    INCOMPLETE_READ = 539
    """This error should never be returned. It is used internally by the Quanser Stream API."""

    EXCLUSIVE_ACCESS_ALREADY_GRANTED = 540
    """Exclusive access to this card has already been granted to another process. Only one process may have exclusive access to the card at one time. Try again later."""

    EXCLUSIVE_ACCESS_NOT_GRANTED = 541
    """Exclusive access to this card was not granted to the process which is attempting to release it. Exclusive access can only be released by the process with exclusive access, and only from the same open handle."""

    CARD_LOCATION_IS_NULL = 542
    """The card location pointer passed as an argument is NULL. A valid pointer to a t_card_location object must be passed to the hil_get_exclusive_access and hil_release_exclusive_access functions."""

    HIL_ACQUIRE_EXCLUSIVE_ACCESS_NOT_SUPPORTED = 543
    """The hil_acquire_exclusive_access function and Exclusive access to device option on the HIL Initialize block are not supported by this particular card."""

    HIL_RELEASE_EXCLUSIVE_ACCESS_NOT_SUPPORTED = 544
    """The hil_release_exclusive_access function and Exclusive access to device option on the HIL Initialize block are not supported by this particular card."""

    DRIVER_MISSING_GET_OR_RELEASE_ACCESS = 545
    """The hil_get_exclusive_access or hil_release_exclusive_access function is present in the driver while the other one is not. These functions are optional, but if one is included in the driver then both must be included."""

    CIRCULAR_BUFFER_NOT_FOUND = 546
    """The corresponding Circular Buffer Initialize could not be found. Make sure that a Circular Buffer Initialize block is present in the model."""

    INCOMPATIBLE_PIPE = 547
    """An attempt was made to create a named pipe for a pipe that already exists and the properties of the pipe are incompatible. Be aware that under the Windows target, the pipe name "localhost" is already used by the system."""

    SENSORAY_TOO_MANY_BOARDS = 548
    """The Sensoray driver supports a maximum of 16 boards."""

    SENSORAY_ILLEGAL_PARAM = 549
    """An illegal parameter was passed to the Sensoray driver."""

    SENSORAY_EEPROM_ERROR = 550
    """The Sensoray board failed to access its EEPROM during initialization.  Try unregistering the board and re-registering it.  If the error persists, then the problem is likely a hardware fault."""

    SENSORAY_UNSPECIFIED_ERROR = 551
    """The Sensoray board has experienced an unspecified fault."""

    KERNEL_CANNOT_REGISTER_BOARD = 552
    """The kernel-mode driver can't register the board.  This is usually caused by applications that fail to unlink from the system dll, or if the kernel model driver is improperly installed or registered."""

    DMA_BUFFER_LOCK = 553
    """A DMA buffer lock failed."""

    CANNOT_START_INTERRUPT_THREAD = 554
    """Failed to launch an interrupt thread"""

    DAC_COMM_TIMEOUT = 555
    """Cannot communicate with analog output."""

    COUNTER_RESOURCE_CONFLICT = 556
    """Counter parameter is illegal in current operation mode.  The counter may already be in use by another operation such as providing a timebase."""

    STREAM_NOT_CONNECTED = 557
    """The non-blocking stream is in the process of connecting but is not yet connected. The stream_poll function or Stream Poll block must be invoked with the connect flag to complete the connection."""

    LIBRARY_LOAD_ERROR = 558
    """The dynamic link library was found, but an error occurred while loading it."""

    PHANTOM_OMNI_CANNOT_OPEN_BOARD = 559
    """The specified PHANTOM Omni board could not be opened. Check that the device is powered and properly connected and that the board number is correct."""

    JR3PCI_CANNOT_SET_FULL_SCALES = 560
    """An error occurred attempting to set the full scales for the JR3 sensor."""

    ALTIA_ARGUMENT_IS_NULL = 561
    """The altia argument to altia_open is NULL."""

    INVALID_ALTIA = 562
    """An invalid Altia handle was passed as an argument. Once an Altia connection has been closed using altia_close the Altia handle is invalid."""

    ALTIA_INPUT_IS_NULL = 563
    """The altia_input argument to altia_register_input is NULL."""

    ALTIA_OUTPUT_IS_NULL = 564
    """The altia_output argument to altia_register_output is NULL."""

    INVALID_ALTIA_EVENT_NAME = 565
    """An invalid event name was passed to an altia function."""

    INVALID_ALTIA_INPUT = 566
    """An invalid t_altia_input handle was passed as an argument."""

    INVALID_ALTIA_OUTPUT = 567
    """An invalid t_altia_output handle was passed as an argument."""

    BEEP_ARGUMENT_IS_NULL = 568
    """The beep argument to beep_open is NULL."""

    INVALID_BEEP = 569
    """An invalid beep handle was passed as an argument. Once an beep handle has been closed using beep_close the beep handle is invalid."""

    BEEP_FAILED = 570
    """A beep was attempted but it failed for some reason. It is possible that permission was denied."""

    BEEP_FREQUENCY_OUT_OF_RANGE = 571
    """The specified beep frequency is out of the acceptable range. See the documentation for valid beep frequencies."""

    SCAN_VALUE_IS_NULL = 572
    """An argument passed to a stream_scan function to store a value scanned is NULL. Arguments must contain the address of appropriately typed quantities."""

    CARD_SPECIFIC_OPTION_NOT_RECOGNIZED = 573
    """The card specific option specified is not recognized."""

    CARD_SPECIFIC_OPTION_VALUE_NOT_RECOGNIZED = 574
    """The value of a card specific option specified is not recognized."""

    CARD_SPECIFIC_OPTION_NOT_SUPPORTED = 575
    """The card specific option specified is recognized, but is not supported by this board."""

    INVALID_ROOMBA = 576
    """The Roomba object is not valid. A Roomba object cannot be used after it has been closed."""

    INVALID_ROOMBA_SENSOR_ID = 577
    """The Roomba sensor id is not valid. It must be a value between 7 and 42 inclusive."""

    VISION_CAMERA_NOT_FOUND = 578
    """The camera could not be found or is not valid for image capture."""

    INVALID_IPLIMAGE = 579
    """Invalid IplImage structure."""

    SAVE_IMAGE = 580
    """Failed to save IplImage using."""

    INIT_V4L2_DEVICE = 581
    """Failed to initialize v4l2 video input."""

    GRAB_V4L2_IMAGE = 582
    """Failed to grab image from v4l2 video input."""

    NO_RPC_SERVER_FOR_BEEP = 583
    """The RPC server is unavailable so the beep cannot be sounded. This problem has been seen on laptops running Vista."""

    MISMATCHED_CHARACTER = 584
    """A character in the input stream did not match the character sequence described in the format string when scanning the stream."""

    EMPTY_SCAN = 585
    """The stream was closed before the first character was read. This error is used internally and should never be returned to the user."""

    URI_MISSING_HOST = 586
    """The hostname is missing from the URI. Although a hostname is not required for all URIs, the fact that you are getting this message indicates that it is required in this circumstance."""

    PATH_IN_PIPE_URI = 587
    """The form of the pipe URI must be pipe:name or pipe://server/name. The name cannot contain forward or backward slashes."""

    HOST_IN_PIPE_URI = 588
    """The pipe URI contains a hostname. Specifying a hostname is not supported on this target, because pipes may not be used to communicate between computers on the selected target."""

    HIQ_UNKNOWN_REPORT_TYPE = 589
    """The specified HiQ report type is unknown. Ensure that the selected HiQ report or mode is valid."""

    HIQ_RECEIVE_BLOCKED = 590
    """The HiQ thread failed to receive any data from the HiQ board."""

    HIL_WATCHDOG_SET_ANALOG_EXPIRATION_STATE_NOT_SUPPORTED = 591
    """The hil_watchdog_set_analog_expiration_state function is not supported by this particular card."""

    HIL_WATCHDOG_SET_DIGITAL_EXPIRATION_STATE_NOT_SUPPORTED = 592
    """The hil_watchdog_set_digital_expiration_state function is not supported by this particular card."""

    HIL_WATCHDOG_SET_PWM_EXPIRATION_STATE_NOT_SUPPORTED = 593
    """The hil_watchdog_set_pwm_expiration_state function is not supported by this particular card."""

    HIL_WATCHDOG_SET_OTHER_EXPIRATION_STATE_NOT_SUPPORTED = 594
    """The hil_watchdog_set_other_expiration_state function is not supported by this particular card."""

    HIL_WATCHDOG_START = 595
    """The hil_watchdog_start function is not supported by this particular card."""

    HIL_WATCHDOG_STOP = 596
    """The hil_watchdog_stop function is not supported by this particular card."""

    HIL_WATCHDOG_RELOAD = 597
    """The hil_watchdog_reload function is not supported by this particular card."""

    HIL_WATCHDOG_IS_EXPIRED = 598
    """The hil_watchdog_is_expired function is not supported by this particular card."""

    HIL_WATCHDOG_CLEAR = 599
    """The hil_watchdog_clear function is not supported by this particular card."""

    HIL_INVALID_DIGITAL_STATE = 600
    """One of the digital states specified was not a valid state. Valid modes are 0 (low), 1 (high), 2 (tristate) or 3 (no change)."""

    ANALOG_EXPIRATION_STATE_NOT_ZERO = 601
    """This board only supports resetting the analog outputs to zero when the watchdog expires."""

    DIGITAL_EXPIRATION_STATE_NOT_TRISTATE = 602
    """This board only supports resetting the digital outputs to tri-state when the watchdog expires."""

    CLOCK_NOT_WATCHDOG = 603
    """The specified clock is not a watchdog timer on this board."""

    ANALOG_EXPIRATIONS_NOT_CONFIGURED = 604
    """Some of the analog output expiration states have not been configured. This board requires that if any of the expiration states have been configured then all the states must be configured, and the "Set analog outputs when a watchdog timer expires" must be enabled."""

    DIGITAL_EXPIRATIONS_NOT_CONFIGURED = 605
    """Some of the digital output expiration states have not been configured. This board requires that if any of the expiration states have been configured then all the states must be configured, and the "Set digital outputs when a watchdog timer expires" must be enabled."""

    CLOCK_PERIOD_TOO_HIGH = 606
    """The clock period is too high for the specified clock. Try using a different clock. Hardware clocks are generally faster than the system clocks."""

    CLOCK_PERIOD_TOO_LOW = 607
    """The clock period is too low for the specified clock. Try using a different clock. System clocks are preferable for long periods so that hardware clocks remain available for operations requiring a shorter period."""

    HIL_TASK_CREATE_ANALOG_WRITER_NOT_SUPPORTED = 608
    """The hil_task_create_analog_writer function and HIL Write Analog Timebase block are not supported by this particular card."""

    FALCON_FAILED_TO_INITIALIZE = 609
    """The Novint Falcon failed to initialize.  Make sure the Falcon is plugged in and powered."""

    FALCON_COULD_NOT_OPEN_DEVICE = 610
    """Could not open the Novint Falcon device."""

    FALCON_COULD_NOT_START_DEVICE = 611
    """Could not start the Novint Falcon control loop."""

    FALCON_COULD_NOT_CREATE_CALLBACK = 612
    """Could not create a callback for the Novint Falcon."""

    FALCON_COULD_NOT_MAKE_CURRENT = 613
    """Novint Falcon error."""

    Q8_SERIES_EXPIRATIONS_NOT_CONFIGURED = 614
    """Some of the analog or digital output expiration states have not been configured. The Q8-series of boards requires that all analog and digital output channels be configured to be reset on watchdog expiration, not just some of the channels."""

    CONNECTION_ABORTED = 615
    """An incoming connection was indicated, but was subsequently terminated by the remote peer prior to accepting the call."""

    INVALID_ROOMBA_SONG_NUMBER = 616
    """Roomba song number must be 0 to 15."""

    INVALID_ROOMBA_SONG_LENGTH = 617
    """Roomba song length must be 1 to 16."""

    INVALID_ROOMBA_NOTE_NUMBER = 618
    """The note number of Roomba song must be 31 to 127."""

    INVALID_ROOMBA_DIGITAL_OUTPUT = 619
    """Roomba digital output must be 0 to 7."""

    INVALID_ROOMBA_EVENT_NO = 620
    """Roomba event no must be 1 to 22."""

    INVALID_ROOMBA_MODE = 621
    """Roomba mode number must be 1 to 3."""

    INVALID_ROOMBA_DEMO = 622
    """Roomba demo number must be 1 to 11."""

    INVALID_ROOMBA_LED_BITS = 623
    """Roomba LED bits must be 0 to 10."""

    INVALID_ROOMBA_SCRIPT_LENGTH = 624
    """Data length mismatches according to the script length defined in the first byte."""

    PREFERENCES_VALUE_CONTAINS_ENVIRONMENT_VARIABLES = 625
    """The preferences value contains environment variable references, which cannot be expanded."""

    INVALID_TYPE_OF_PREFERENCES_VALUE = 626
    """The preferences value is not a string."""

    INVALID_ROOMBA_STREAM_STATE = 627
    """Roomba stream state must be 0 to 1."""

    INVALID_ROOMBA_DRIVER_BITS = 628
    """Roomba low side driver number must be 0 to 7."""

    INVALID_ROOMBA_DUTY_CYCLE = 629
    """Roomba duty cycle must be 0 to 128."""

    INVALID_ROOMBA_PACKET_NUMBER = 630
    """The number of Roomba sensor packets requested must be 0 to 43"""

    INVALID_ROOMBA_STREAM_HEADER = 631
    """Roomba stream header must be 19."""

    CORRUPTED_ROOMBA_STREAM = 632
    """Roomba stream is corrupted."""

    INVALID_ROOMBA_STREAM_SIZE = 633
    """Roomba stream size must be (number of packets + number of data bytes + 3)"""

    INVALID_IMAGE_DIMENSION = 634
    """Invalid dimension for image data"""

    INVALID_SERACCEL = 635
    """The SerAccel object is not valid. A SerAccel object cannot be used after it has been closed."""

    SERACCEL_COULD_NOT_OPEN_DEVICE = 636
    """The SerAccel could not be opened. Make sure the SerAccel is connected and set to binary mode."""

    SERACCEL_COULD_NOT_START_DEVICE = 637
    """The SerAccel could not be started."""

    SERACCEL_COULD_NOT_READ_DEVICE = 638
    """The SerAccel could not be read."""

    NO_ALTIA_LICENSE = 639
    """You do not have a valid license for the Altia blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    NO_IROBOT_ROOMBA_LICENSE = 640
    """You do not have a valid license for the IRobot Roomba blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    NO_JR3_FORCE_TORQUE_LICENSE = 641
    """You do not have a valid license for the JR3 Force/Torque Sensor blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    NO_MITSUBISHI_PA10_LICENSE = 642
    """You do not have a valid license for the Mitsubishi PA-10 blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    NO_NINTENDO_WIIMOTE_LICENSE = 643
    """You do not have a valid license for the Nintendo Wiimote blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    NO_NOVINT_FALCON_LICENSE = 644
    """You do not have a valid license for the Novint Falcon blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    NO_POINTGREY_CAMERAS_LICENSE = 645
    """You do not have a valid license for the Point Grey Research Cameras blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    NO_SCHUNK_GRIPPER_LICENSE = 646
    """You do not have a valid license for the Schunk Gripper blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    NO_SENSABLE_OMNI_LICENSE = 647
    """You do not have a valid license for the SensAble Omni blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    INVALID_IMAGE_NAME = 648
    """The specified image does not exist."""

    NO_INTERNAL_USE_LICENSE = 649
    """The "Active during normal simulation" feature is not available. Did you intend to run in real-time using the "Monitor & Tune" button? Due to safety and liability concerns, accessing physical hardare in normal simulation rather than real-time is not enabled."""

    DRAGANFLY_X6_CRC_FAILED = 650
    """The Draganfly X6 autopilot message failed the CRC check."""

    CANPCI_NOT_FOUND = 651
    """The specified CANPCI could not be found."""

    CANPCI_INIT_FAILED = 652
    """Initialization of the CANPCI driver failed."""

    CANPCI_INVALID_PARAMETERS = 653
    """Parameters supplied to a CANPCI driver function are invalid."""

    CANPCI_SEND_MESSAGE_FAILED = 654
    """The CANPCI device failed to send a CAN message."""

    CANPCI_GET_MESSAGE_FAILED = 655
    """The CANPCI device failed to receive a CAN message."""

    CANPCI_INVALID_CHANNEL = 656
    """The CANPCI channel specified is invalid."""

    CANPCI_START_FAILED = 657
    """Failed to start the CANPCI card(s)."""

    INVALID_UBLOX = 658
    """The Ublox object is not valid. A Ublox object cannot be used after it has been closed."""

    NO_UBLOX_MSG = 659
    """No Ublox message"""

    INVALID_UBLOX_MSG = 660
    """Invalid Ublox message"""

    INVALID_UBLOX_IDENTIFIERS = 661
    """Invalid Ublox identifiers"""

    INVALID_UBLOX_CHECKSUM = 662
    """Invalid Ublox checksum"""

    INVALID_NMEA_MSG = 663
    """Invalid NMEA message"""

    INVALID_NMEA_CHECKSUM = 664
    """Invalid NMEA checksum"""

    INVALID_UBLOX_DATA = 665
    """Invalid Ublox data"""

    UNSUPPORTED_GPS_DATA_FIELD = 666
    """Unsupported Ublox GPS data field"""

    ROBOSTIX_INVALID_PROGRAM_VERSION = 667
    """The program on the robostix has an invalid version information (i.e., is either too old or too new)."""

    SPI_TRANSMIT = 668
    """A transmit error occured using the Serial Peripheral Interface (SPI) protocol."""

    SPI_RECEIVE = 669
    """A receive error occured using the Serial Peripheral Interface (SPI) protocol."""

    NO_SUCH_DEVICE = 670
    """No such device or address"""

    INTIME_NOT_RUNNING = 671
    """A real-time object could not be created. The INtime real-time kernel may not be running. Use the INtime Status icon in the system tray to start the INtime kernel."""

    CANNOT_CONNECT_TO_LICENSE_MANAGER = 672
    """It was not possible to connect to the license manager."""

    MISSING_PROPERTIES = 673
    """No properties were specified even though the number of properties is nonzero."""

    MISSING_PROPERTIES_BUFFER = 674
    """Properties have been specified but no values have been provided for the operation."""

    HIL_GET_INTEGER_PROPERTY_NOT_SUPPORTED = 675
    """The hil_get_integer_property function and HIL Get Property block are not supported by this particular card."""

    HIL_GET_DOUBLE_PROPERTY_NOT_SUPPORTED = 676
    """The hil_get_double_property function and HIL Get Property block are not supported by this particular card."""

    HIL_GET_STRING_PROPERTY_NOT_SUPPORTED = 677
    """The hil_get_string_property function and HIL Get Property block are not supported by this particular card."""

    HIL_SET_INTEGER_PROPERTY_NOT_SUPPORTED = 678
    """The hil_set_integer_property function and HIL Set Property block are not supported by this particular card."""

    HIL_SET_DOUBLE_PROPERTY_NOT_SUPPORTED = 679
    """The hil_set_double_property function and HIL Set Property block are not supported by this particular card."""

    HIL_SET_STRING_PROPERTY_NOT_SUPPORTED = 680
    """The hil_set_string_property function and HIL Set Property block are not supported by this particular card."""

    PROPERTY_NOT_RECOGNIZED = 681
    """One or more of the specified properties were not recognized by the board-specific driver."""

    GUMSTIX_WATCHDOG_CLOCK_PERIOD_TOO_HIGH = 682
    """The watchdog timer period (a.k.a., timeout interval) is too high. The gumstix watchdog timer may be programmed with any integer value between 1 and 255 seconds."""

    GUMSTIX_WATCHDOG_CLOCK_PERIOD_TOO_LOW = 683
    """The watchdog timer period (a.k.a., timeout interval) is too low. The gumstix watchdog timer may be programmed with any integer value between 1 and 255 seconds."""

    DIGITAL_INPUTS_NOT_INITIALIZED = 684
    """The specified digital input channels are not initialized. This board requires that all the channels which will be used for digital inputs should be configured on the HIL Initialize block's "Digital Inputs" tab. Set the "Digital input channels" field to all the digital channels that will be used as digital inputs on the board."""

    DIGITAL_OUTPUTS_NOT_INITIALIZED = 685
    """The specified digital output channels are not initialized. This board requires that all the channels which will be used for digital outputs should be configured on the HIL Initialize block's "Digital Outputs" tab. Set the "Digital output channels" field to all the digital channels that will be used as digital outputs on the board."""

    FILTER_PROTOCOLS_REQUIRE_URI = 686
    """Missing "uri" option. Filter protocols require a "uri" option in their URI to identify the underlying communication protocol."""

    CONFLICTING_COUNTER_MODES = 687
    """The specified counter is used as both an encoder and a PWM output channel."""

    DAQMX_ERROR_CHANGING_PWM_OUT_TERM = 688
    """DAQmx failed to change the counter output terminal."""

    DAQMX_ERROR_WRITING_PWM = 689
    """DAQmx failed to output the requested PWM values."""

    DAQMX_CANNOT_ATTACH_PWM_TO_TASK = 690
    """DAQmx was unable to attach the specified counter channel to the PWM output task."""

    DAQMX_ERROR_SETTING_IMPLICIT_TIMING = 691
    """DAQmx was unable to configure implicit timing for the PWM output task."""

    DAQMX_CANNOT_GET_PWM_CHANNEL_NAME = 692
    """DAQmx was unable to obtain the name of the PWM channel attached to the PWM output task."""

    NI_DUTY_CYCLE_OUT_OF_RANGE = 693
    """The specified PWM duty cycle is out of range. For National Instruments cards, the duty cycle should fall within the range between a minimum value of 0.1 % (0.001) and a maximum value of 99.9 % (0.999)."""

    NI_FREQUENCY_OUT_OF_RANGE = 694
    """The specified PWM frequency is out of range. For National Instruments cards, the frequency must satisfy the following inequality: (Maximum Counter Output Frequency/Max Number of Counts) <= frequency <= (Maximum Counter Output Frequency/4)."""

    DAQMX_ERROR_CHANGING_TIMEBASE_RATE = 695
    """DAQmx was unable to set the counter timebase rate."""

    INVALID_DSR_CONTROL = 696
    """Invalid dsr option. Supported values are "off", "on" or "handshake"."""

    OPTITRACK_RIGID_BODY_INIT_ERROR = 697
    """Unable to initialize the OptiTrack Rigid Body API. Make sure the proper software is installed and the path variable is set."""

    OPTITRACK_POINT_CLOUD_INIT_ERROR = 698
    """Unable to initialize the OptiTrack Point Cloud API. Make sure the proper software is installed and the path variable is set."""

    OPTITRACK_RIGID_BODY_ID_INVALID = 699
    """The rigid body ID is invalid or not found in the rigid body definition file. Valid IDs are integers ranging from 1 to 1024."""

    OPTITRACK_ERROR_STARTING_CAMERAS = 700
    """An error occurred starting the OptiTrack camera system. Make sure they are properly connected."""

    OPTITRACK_ERROR_STOPPING_CAMERAS = 701
    """An error occurred stopping the OptiTrack camera system."""

    OPTITRACK_INVALID_CALIBRATION_FILE = 702
    """Unable to load OptiTrack calibration file. Make sure the file path is correct or the calibration file is compatible with the Motive software version that you have installed."""

    OPTITRACK_INVALID_RIGID_BODY_FILE = 703
    """Unable to load OptiTrack rigid body definition file. Make sure the file path is correct."""

    OPTITRACK_TOO_MANY_RIGID_BODIES = 704
    """The number of specified OptiTrack rigid bodies exceeds the number of objects in the rigid body definition file."""

    VISION_INVALID_PARAMETER = 705
    """Invalid parameter for OpenCV functions"""

    VISION_INVALID_NO_OF_CHANNELS = 706
    """Invalid number of color planes of the input image"""

    NO_CANCELLATION_HANDLER = 707
    """An attempt was made to pop a cancellation handler when no cancellation handler was pushed on the stack!"""

    VISION_INVALID_INPUT = 708
    """Invalid input for OpenCV functions"""

    PORT_UNREACHABLE = 709
    """The port is unreachable. For UDP datagrams, a previous send operation resulted in an ICMP Port Unreachable message, indicating that there is likely no server listening on the UDP port."""

    CANNOT_SET_PORT_UNREACHABLE = 710
    """Cannot set the port unreachable option to disable reporting ICMP Port Unreachable messages for UDP datagrams"""

    MUST_BE_ADMINISTRATOR = 711
    """The process lacks the appropriate privileges to perform the operation. Administrator privileges are required. Log in as an Administrator or run as Administrator."""

    MISMATCHED_ENCODER_FILTER_FREQUENCY = 712
    """One of the encoder filter frequencies specified does not match the filter frequency of the other channels. This card only allows one filter frequency to be set for all encoder channels."""

    MISMATCHED_CLOCK_FREQUENCY = 713
    """One of the clock frequencies specified does not match the frequency of another channel which shares the same clock resources."""

    UNABLE_TO_OPEN_DIALOG = 714
    """The underlying operating system could not open the dialog."""

    HIL_SET_DIGITAL_OUTPUT_CONFIGURATION_NOT_SUPPORTED = 715
    """The hil_set_digital_output_configuration function is not supported by this particular card."""

    HIL_SET_PWM_CONFIGURATION_NOT_SUPPORTED = 716
    """The hil_set_pwm_configuration function is not supported by this particular card."""

    HIL_SET_PWM_DEADBAND_NOT_SUPPORTED = 717
    """The hil_set_pwm_deadband function is not supported by this particular card."""

    MISSING_DIGITAL_CONFIGURATIONS = 718
    """Digital output channels have been specified but not enough digital output configurations have been provided."""

    MISSING_PWM_CONFIGURATIONS = 719
    """PWM output channels have been specified but not enough PWM configurations have been provided."""

    MISSING_PWM_ALIGNMENTS = 720
    """PWM output channels have been specified but not enough PWM alignments have been provided."""

    MISSING_PWM_POLARITIES = 721
    """PWM output channels have been specified but not enough PWM polarities have been provided."""

    MISSING_PWM_DEADBANDS = 722
    """PWM output channels have been specified but not enough PWM high-to-low or low-to-high deadband values have been provided."""

    INVALID_PWM_CONFIGURATION = 723
    """One of the PWM output configurations specified is not a valid configuration. Configurations must be in the range from 0 to 2 inclusive (0=independent, 1=complementary, 2=bipolar)"""

    INVALID_PWM_ALIGNMENT = 724
    """One of the PWM output alignments specified is not a valid configuration. Configurations must be 0 (leading-edge-aligned), 1 (trailing-edge-aligned) or 2 (center-aligned)"""

    INVALID_PWM_POLARITY = 725
    """One of the PWM output polarities specified is not a valid configuration. Configurations must be 1 (active high) or 0 (active low)"""

    PWM_CONFIGURATION_NOT_SUPPORTED = 726
    """One of the PWM output channels specified does not support the given PWM output configuration. For example, channel 7 of the QPID cannot be used in the complementary configuration as the primary channel because it is the last PWM channel. Alternatively, the given configuration may not be supported by the card at all."""

    INVALID_PWM_DEADBAND = 727
    """One of the PWM deadbands specified is negative. Deadband values must be non-negative."""

    BIPOLAR_PWM_ON_EVEN_CHANNELS_ONLY = 728
    """The bipolar PWM configuration may only be configured on the even PWM channels for this card. See the card's documentation for details."""

    GPS_READ_FAILED = 729
    """A read of the GPS device failed."""

    PWM_ALIGNMENT_NOT_SUPPORTED = 730
    """One of the PWM output channels specified does not support the given PWM alignment."""

    PWM_POLARITY_NOT_SUPPORTED = 731
    """One of the PWM output channels specified does not support the given PWM polarity."""

    PWM_DEADBAND_NOT_SUPPORTED = 732
    """One of the PWM output channels specified does not support the given PWM deadband."""

    INVALID_CHANNEL_ORDER_FOR_BIPOLAR_PWM = 733
    """The PWM output channels are not ordered correctly for the bipolar PWM output. Bipolar PWM outputs require that both the primary and secondary channel be written at the same time, and that the secondary channel be specified in the channel order immediately after the primary channel."""

    SUM_OF_PWM_DEADBANDS_EXCEEDS_PERIOD = 734
    """The sum of the leading and trailing deadbands exceeds the PWM period. The deadbands cannot be so large that they exceed the PWM period."""

    PWM_MODES_NOT_ONE_SHOT = 735
    """At least one PWM channel is in one-shot mode, while others are not. The current card requires that all PWM channels be configured in one-shot mode, if this mode is used, not just some of the channels."""

    PWM_EXPIRATIONS_NOT_CONFIGURED = 736
    """Some of the PWM output expiration states have not been configured. This board requires that if any of the expiration states have been configured then all the states must be configured, and the "Set PWM outputs when a watchdog timer expires" must be enabled."""

    PHANTOM_CANNOT_INITIALIZE = 737
    """Phantom block cannot initialize the device."""

    PHANTOM_SCHEDULER_ERROR = 738
    """Phantom block cannot start the Phantom API scheduler."""

    PHANTOM_SCHEDULER_RATE_ERROR = 739
    """Phantom API scheduler rate error."""

    PHANTOM_READ_FAILED = 740
    """Phantom block cannot read the outputs of the device."""

    PHANTOM_WRITE_FAILED = 741
    """Phantom block cannot write to inputs of the device."""

    PHANTOM_CANNOT_CLOSE = 742
    """Phantom block cannot close the device."""

    NO_PHANTOM_OMNI_LICENSE = 743
    """You do not have a valid license for the Phantom Omni blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    NO_PHANTOM_DESKTOP_LICENSE = 744
    """You do not have a valid license for the Phantom Desktop blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    NO_PHANTOM_PREMIUM_LICENSE = 745
    """You do not have a valid license for the Phantom Premium blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    NO_PHANTOM_PREMIUM_6DOF_LICENSE = 746
    """You do not have a valid license for the Phantom Premium 6DOF blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    VAL_QBOT_OPEN_FAILED = 747
    """Failed to open the Qbot VAL driver."""

    INVALID_KR5_SIXX_R850 = 748
    """Invalid object. A KUKA robot object cannot be used after it has been closed."""

    KR5_SIXX_R850_COULD_NOT_OPEN_DEVICE = 749
    """The KUKA robot device could not be opened. Make sure a 6-DOF KUKA robot is connected."""

    NO_KUKA_KR5_SIXX_R850_LICENSE = 750
    """You do not have a valid license for the KUKA RSI blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    VISION_INVALID_IMAGE_SIZE = 751
    """Invalid image dimension."""

    INVALID_HYMOTION_11000 = 752
    """Invalid object. A HyMotion-11000 object cannot be used after it has been closed."""

    HYMOTION_11000_COULD_NOT_OPEN_DEVICE = 753
    """The HyMotion-11000 could not be opened. Make sure the Rexroth HyMotion-11000 Motion System is connected."""

    NO_REXROTH_HYMOTION_11000_LICENSE = 754
    """You do not have a valid license for the Rexroth HyMotion-11000 blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    INVALID_SHMEM_SCOPE = 755
    """The shmem protocol is designed for communicating between a real-time model and a foreground application. To use it for communicating between two Windows applications, the "local=true" option is required on the shmem URI. For example, "shmem://mymem:1?local=true"."""

    NO_NATURALPOINT_OPTITRACK_LICENSE = 756
    """You do not have a valid license for the NaturalPoint OptiTrack blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    NO_VISUALIZATION_LICENSE = 757
    """You do not have a valid license for the Visualization blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    NO_GPS_LICENSE = 758
    """You do not have a valid license for the GPS blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    INVALID_CIGI_HOST = 759
    """Invalid object. A CIGI host object cannot be used after it has been closed."""

    CIGI_HOST_COULD_NOT_OPEN_DEVICE = 760
    """The CIGI Host could not be opened."""

    INVALID_DEFLATE_MODE = 761
    """The mode option specified for a deflate URI is invalid."""

    STATE_IS_NULL = 762
    """The state argument is NULL. It should be a valid pointer."""

    WRONG_NUM_BYTES_POKED = 763
    """The wrong number of bytes have been sent to a persistent stream. Verify that the number of bytes configured when the stream was created matches the number of bytes sent."""

    WRONG_NUM_BYTES_PEEKED = 764
    """The wrong number of bytes have been received from a persistent stream. Verify that the number of bytes configured when the stream was created matches the number of bytes received."""

    NO_QBOT_LICENSE = 765
    """You do not have a valid license for the Qbot vehicle. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    NO_UAV_LICENSE = 766
    """You do not have a valid license for the UAV components. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    PHANTOM_LIBRARY_OPEN_FAILED = 767
    """The SensAble PHANToM library failed to open. Make sure you have the OpenHaptics and PHANToM Device Driver software installed and the system PATH is set correctly."""

    WRONG_NUMBER_OF_INITIAL_VALUES = 768
    """The wrong number of initial values were passed to visualization_open for the variables given."""

    INVALID_NEES = 769
    """Invalid object. A NEES object cannot be used after it has been closed."""

    NEES_COULD_NOT_INITIALIZE = 770
    """The NEES block could not be initialized."""

    NEES_COULD_NOT_COMMUNICATE = 771
    """Could not communicate with the NEES daemon."""

    NEES_INVALID_DATA_FROM_DAEMON = 772
    """Received invalid data from the NEES daemon."""

    NEES_COULD_NOT_CLOSE = 773
    """Could not close the NEES block."""

    TCP_KEEPALIVES_NOT_SUPPORTED = 774
    """TCP/IP keep alive packets on individual socket connections does not appear to be supported."""

    CANNOT_SELECT_VARIABLE = 775
    """Variables cannot be selected after a visualization task has already been started."""

    INVALID_VARIABLE_NAME = 776
    """The variable indicated could not be found in the scene."""

    VARIABLE_ALREADY_SELECTED = 777
    """The variable has already been selected in the scene. Variables cannot be selected more than once."""

    INVALID_VARIABLE_DATATYPE = 778
    """The wrong data type is being used to set the value of the given variable."""

    QERR_CANNOT_SET_VARIABLE = 779
    """Variable values cannot be set until the visualization task has been started. Use the Visualization Start Task VI to start the task."""

    VARIABLE_NOT_SELECTED = 780
    """The given variable has not been selected for animation. Use the Visualization Select Variable VI to select the variable for animation prior to starting the visualization task."""

    VISUALIZATION_ALREADY_STARTED = 781
    """The visualization task has already been started."""

    UNABLE_TO_START_VIEWER = 782
    """The Quanser 3D Viewer could not be started."""

    INVALID_VISUALIZATION_HANDLE = 783
    """An invalid visualization handle was passed to a Visualization VI or function."""

    VIEWER_MAY_NOT_HAVE_EXITED = 784
    """The Quanser 3D Viewer may not have exited. An unexpected error may have occurred."""

    PCAN_CANNOT_INITIALIZE = 785
    """The Peak CAN device failed to initialize. Make sure the device is connected properly and the drivers and API have been installed."""

    WIIMOTION_PLUS_ACTIVATE_FAILED = 786
    """The WiiMotion Plus extension failed to activate. Make sure the WiiMotion Plus extension is properly connected to the Wiimote."""

    WIIMOTION_PLUS_NOT_DETECTED = 787
    """The WiiMotion Plus extension was not detected. Make sure it is properly connected to the Wiimote."""

    WIIMOTE_EXT_CONTROLLER_CHECK_FAILED = 788
    """Failed to read report for Wiimote extension controllers. Make sure your Wiimote is properly connected."""

    SOFTWARE_ALREADY_INSTALLED = 789
    """Another version of the software is already installed. Please uninstall the other version first."""

    NO_SPACE_ON_FILE_SYSTEM = 790
    """There is no space left on the file system."""

    FILE_SYSTEM_ERROR = 791
    """A physical I/O error occurred trying to access the file system."""

    INVALID_SETUP_OPERATION = 792
    """An invalid operation was detected in the installation database. The installation database appears to be corrupt."""

    PREMATURE_END_OF_FILE = 793
    """The end of the file was encountered prematurely. The file is corrupt."""

    PARTITION_NOT_FOUND = 794
    """The specified partition could not be found. Make sure you have created the partition and have enabled the appropriate scheduler."""

    PARTITIONING_SCHEDULER_NOT_RUNNING = 795
    """The partitioning scheduler is not running. Be sure to set up your system to run the partitioning scheduler before attempting to use it."""

    JOINING_PARTITION_DENIED = 796
    """It was not possible to join the partition. Security constraints set up for partitioning do not allow it."""

    DIGITAL_EXPIRATION_STATE_TRISTATE_INVALID = 797
    """This board does not support tristating the digital outputs when the watchdog expires. The digital outputs may only be set high or low on watchdog expiration."""

    INVALID_LICENSE_FOR_BUILDFILE = 798
    """The Configure Licensing tool can only generate a build file snippet for a network client license. Specify the -c option but not the -m option (client not server/manager) when configuring the license."""

    URI_OPTION_NOT_RECOGNIZED = 799
    """An option specified in the URI was not recognized as a valid option."""

    HIL_CONFLICTING_DIGITAL_OUTPUTS = 800
    """Two or more digital outputs were specified with output values that conflict with one another. Refer to the device documentation for limitations."""

    DENSO_READ_TIMEOUT = 801
    """The Denso Read block has timed out since no data was received. Check that the IP settings of your PC are correct and that the PC is connected to the Denso controller."""

    NO_ROOM_IN_RECEIVE_BUFFER = 802
    """A communication protocol is being used that sends and receives data at the same time, such as SPI, and there is no room in the stream's receive buffer for the data that will be received during the send/flush operation."""

    NO_DATA_IN_RECEIVE_BUFFER = 803
    """A communication protocol is being used that sends and receives data at the same time, such as SPI, and there is no data in the stream's receive buffer to receive. A send/flush operation should be done first. The send/flush will receive data at the same time as data is sent and fill the receive buffer so that data can be received."""

    SPI_WRONG_BYTES_TO_SEND_AND_RECEIVE = 804
    """The number of bytes being sent or received is not an integer multiple of the natural word size (1 bytes for 1-8 bits, 2 bytes for 9-16 bits and 4 bytes for 17-32 bit word lengths)."""

    NO_SUCH_SPI_CHANNEL = 805
    """The SPI port specified in the URI is not available."""

    ONLY_SPI_MASTER_MODE_SUPPORTED = 806
    """Only the SPI master mode is supported by the device being used for SPI communications. Different hardware is required for slave mode."""

    ONLY_SPI_MSB_FIRST_SUPPORTED = 807
    """The SPI device specified in the URI only supports sending and receiving the most-significant bit first."""

    NO_DENSO_LICENSE = 808
    """You do not have a valid license for the Denso blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    NO_PTI_VISUALEYEZ_LICENSE = 809
    """You do not have a valid license for the PTI VisualEyez blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    PTI_VZSOFT_FAILED_TO_INITIALIZE = 810
    """The VZSoft device failed to initialize. Make sure the system is setup properly and the VZSoft software is installed."""

    PTI_VZANALYZER_FAILED_TO_INITIALIZE = 811
    """The VZAnalyzer device failed to initialize. Make sure the VZAnalyzer software is installed."""

    PWM_MODES_NOT_COMPATIBLE = 812
    """At least one PWM channel is in a mode that is incompatible with the other PWM channels. The current card has restrictions on the PWM modes. For example, the card may share the PWM period among all the channels so using duty cycle or time mode along with frequency or period mode is not permitted. See the card's documentation for details."""

    NP_TRACK_IR_OPEN_FAILED = 813
    """The TrackIR head tracker failed to initialize. Make sure that TrackIR is running and the Quanser Device ID is registered. Make sure the PATH environment variable is set correctly."""

    CANNOT_SET_POSITION = 814
    """The position of the stream cannot be set."""

    SEMAPHORE_COUNT_EXCEEDED = 815
    """A semaphore's maximum count has been reached. The semaphore cannot be signaled."""

    CONNECTION_REFUSED = 816
    """The remote peer refused the connection, most likely because no server application was listening for connections"""

    MISSING_INTERRUPT_SOURCES = 817
    """No interrupt sources were specified even though the number of interrupt sources is nonzero."""

    MISSING_INTERRUPT_OCCURRED_BUFFER = 818
    """Interrupt sources have been specified but not enough buffer space has been provided for the poll operation."""

    HIL_POLL_INTERRUPT_NOT_SUPPORTED = 819
    """The hil_poll_interrupt function and HIL Poll Interrupt block are not supported by this particular card."""

    MONITOR_ARGUMENT_IS_NULL = 820
    """The monitor argument to a HIL function is NULL."""

    INVALID_MONITOR_HANDLE = 821
    """An invalid monitor handle was passed as an argument to a HIL function."""

    HIL_MONITOR_CREATE_INTERRUPT_READER_NOT_SUPPORTED = 822
    """The hil_monitor_create_interrupt_reader function and HIL Interrupt block are not supported by this particular card."""

    HIL_MONITOR_START_NOT_SUPPORTED = 823
    """The hil_monitor_start function is not supported by this particular card. If the hil_monitor_create_interrupt_reader function is supported then the hil_monitor_stop function MUST be supported. Contact the device manufacturer."""

    HIL_MONITOR_STOP_NOT_SUPPORTED = 824
    """The hil_monitor_stop function is not supported by this particular card. If the hil_monitor_create_interrupt_reader function is supported then the hil_monitor_stop function MUST be supported. Contact the device manufacturer."""

    HIL_MONITOR_DELETE_NOT_SUPPORTED = 825
    """The hil_monitor_delete function is not supported by this particular card. If the hil_monitor_create_interrupt_reader function is supported then the hil_monitor_stop function MUST be supported. Contact the device manufacturer."""

    HIL_MONITOR_READ_INTERRUPT_NOT_SUPPORTED = 826
    """The hil_monitor_read_interrupt function is not supported by this particular card."""

    INVALID_INTERRUPT_SOURCE = 827
    """One of the interrupt sources that was specified is not a valid interrupt source. Interrupt sources are typically divided into ranges according to functionality. Refer to the documentation for your card."""

    INVALID_INTERRUPT_OPERATION_HANDLE = 828
    """An invalid interrupt operation handle was passed as an argument to the board-specific HIL driver. Once a monitor has been deleted using hil_monitor_delete the interrupt operation handle is invalid."""

    INTERRUPT_OPERATION_ARGUMENT_IS_NULL = 829
    """The interrupt operation argument to a board-specific HIL driver is NULL. This situation should never occur unless the user is calling the board-specific driver directly or memory has been corrupted."""

    OPTITRACK_INVALID_LICENSE = 830
    """The license for the Optitrack tools being used is invalid or missing. Make sure you have configured your license."""

    OPTITRACK_FRAME_UPDATE_FAILED = 831
    """An attempt to process frames from Optitrack failed. See the QUARC console for additional information."""

    TOO_MANY_INTERRUPT_SOURCES = 832
    """Too many interrupt sources were specified."""

    HIL_SET_CLOCK_FREQUENCY_NOT_SUPPORTED = 833
    """The hil_set_clock_frequency function is not supported by this particular card."""

    VICON_CANNOT_CONNECT = 834
    """Cannot connect to the Vicon DataStream server. Check that the host name is correct and that the Tracker software is running."""

    VICON_FAILED_TO_SET_STREAM_MODE = 835
    """The Vicon system failed to set the specified stream mode. Ensure the stream mode is valid and the Tracker software is running."""

    VICON_ENABLE_UNLABELED_MARKER_DATA_FAILED = 836
    """The Vicon system failed to enable the unlabeled marker data stream. Make sure your system is connected and the Tracker software is running."""

    VICON_ENABLE_MARKER_DATA_FAILED = 837
    """The Vicon system failed to enable the marker data stream. Make sure your system is connected and the Tracker software is running."""

    VICON_ENABLE_SEGMENT_DATA_FAILED = 838
    """The Vicon system failed to enable the segment data stream. Make sure your system is connected and the Tracker software is running."""

    NO_VICON_LICENSE = 839
    """You do not have a valid license for the Vicon blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    DAQMX_ONLY_DEVICE_NAMES_SUPPORTED = 840
    """Using a numeric board identifier for NI cards is not supported on this system. Please use the device name instead."""

    HIQ_BUILD_NUMBER_MISMATCH = 841
    """The HiQ firmware build number does not match the HiQ driver build number. Make sure your HiQ driver version is compatible with the HiQ hardware."""

    INVALID_HOST_PACKET = 842
    """A Host block appears to be incompatible with the current version of QUARC because it has sent invalid data. It may be necessary to rebuild the model."""

    DRIVER_TIMED_OUT = 843
    """The HIL driver timed out trying to communicate with the card. The card may not be working or the version of the driver may not be compatible with the version of the card."""

    V4L2_VIDIOC_QBUF_FAILED = 844
    """Failed to enqueue a buffer with the video driver's incoming queue."""

    V4L2_COULD_NOT_CLOSE = 845
    """Failed to close the video driver."""

    V4L2_DEVICE_MISSING = 846
    """The specified video device could not be found."""

    V4L2_QUERY_FAILED = 847
    """Unable to query the video driver for its status."""

    V4L2_NOT_CAP_DEVICE = 848
    """The device does not support video capture."""

    V4L2_NOT_STREAMING_DEVICE = 849
    """The device does not support video streaming."""

    V4L2_FORMAT_NOT_VALID = 850
    """The image format is not valid for the device."""

    V4L2_VIDIOC_REQBUFS_FAILED = 851
    """Failed to initiate memory-mapped or user-pointer I/O for the video device."""

    V4L2_VIDIOC_STREAM_FAILED = 852
    """Failed to start or stop video capture or streaming."""

    CASPA_CAPTURE_FAILED = 853
    """Failed to capture video."""

    CARD_NOT_ACTIVE = 854
    """The card is not valid. It may not have been made active during normal simulation in the HIL Initialize block and thus may be uninitialized."""

    AUTOPILOT_NOT_ACTIVE = 855
    """The autopilot is not valid. It may not have been made active during normal simulation in the VAL Initialize block and thus may be uninitialized."""

    PCAN_INVALID_CHANNEL = 856
    """The channel number specified for the Peak CAN device is not valid. Make sure the correct device type is selected and the channel number is valid."""

    PCAN_SET_MESSAGE_FILTER_FAILED = 857
    """The Peak CAN device failed to set the message filter. Make sure the message IDs requested are valid."""

    INCOMPATIBLE_TARGET_TYPE = 858
    """The code being downloaded or run is not compatible with the type of target referenced by the target URI. For example, 32-bit code cannot be downloaded to a 64-bit target or vice versa. In Simulink, make sure the system target file selected in the model's active configuration is compatible with the target referred to by the target URI."""

    PCAN_WRITE_FAILED = 859
    """The Peak CAN device failed to write a message. Make sure you are connected to a CAN network with proper CAN bus termination resistance and that your baud rate is correct."""

    JACO_INVALID_JOINT = 860
    """The joint specified for the Jaco device is outside the valid range."""

    JACO_JOINT_INITIALIZATION_FAILED = 861
    """Unable to initialize one of the Jaco joints. Make sure that the Jaco cables are properly connected, the emergency stop is released, and the Jaco power is on."""

    JACO_ACK_NOT_RECEIVED = 862
    """Jaco did not send an acknowledge message when one was expected."""

    SHARING_VIOLATION = 863
    """The process cannot access the file or object because it is being used by another process."""

    JACO_READ_FAILED = 864
    """Failed to read CANbus for the Jaco. Check that the CAN cables are properly connected, the emergency stop is released, and the Jaco power is on."""

    JACO_JOINT_ADDRESS_INVALID = 865
    """The Jaco joint address is invalid."""

    NO_ROBOTICS_LICENSE = 866
    """You do not have a valid license for the Robotics blockset you are using. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    INVALID_HOST = 867
    """The host passed as an argument is invalid. It is likely NULL, indicating the host may not be not connected or listening."""

    JACO_READ_TIMEOUT = 868
    """A JACO read timeout expired."""

    JACO_SHUTDOWN = 869
    """Unable to complete the operation because the JACO is shutting down."""

    PERIPHERAL_NOT_FOUND = 870
    """A peripheral device could not be found. It is possible the device is unplugged or otherwise inoperable."""

    ENVIRONMENT_VARIABLE_NOT_FOUND = 871
    """The environment variable could not be found."""

    VIS_CANNOT_CREATE_FRAME_TIMER = 872
    """An error occured creating the frame-rate timer."""

    VIS_CANNOT_CREATE_VISUALIZATION_WINDOW = 873
    """An error occured creating the visualization window."""

    VIS_CANNOT_REGISTER_WINDOW = 874
    """An error occured while attempting to register the windows class.  Windows error code %d."""

    VIS_CANNOT_GET_WINDOW_DC = 875
    """Cannot create device context.  Windows error %d."""

    VIS_FAILED_TO_SWITCH_TO_FULL_SCREEN = 876
    """Could not switch to requested fullscreen mode."""

    VIS_CANNOT_FIND_SUITABLE_PIXEL_FORMAT = 877
    """Cannot find suitable OpenGL pixel format."""

    VIS_CANNOT_SET_PIXEL_FORMAT = 878
    """Cannot set OpenGL pixel format."""

    VIS_CANNOT_CREATE_OPENGL_CONTEXT = 879
    """Cannot create OpenGL context."""

    VIS_CANNOT_CREATE_EXTENDED_OPENGL_CONTEXT = 880
    """Could not create a rendering context for the requested OpenGL version (%1.1f).  A different OpenGL version or updating your video drivers may resolve the issue."""

    VIS_CANNOT_MAKE_OPENGL_CONTEXT = 881
    """Cannot make the specified OpenGL context the current context."""

    VIS_CANNOT_MAKE_EXTENDED_OPENGL_CONTEXT = 882
    """Could not make the specified OpenGL context the current context for the requested OpenGL version (%1.1f). A different OpenGL version or updating your video drivers may resolve the issue."""

    VIS_UNABLE_TO_SWAP_GRAPHICS_BUFFERS = 883
    """Unable to swap graphics buffers."""

    VIS_TOO_MANY_LIGHTS_IN_SCENE = 884
    """Too many lights in scene. A maximum of %d lights are supported by OpenGL."""

    VIS_CANNOT_FIND_VALID_X3D_MESH = 885
    """Cannot find a valid X3D mesh in %s."""

    VIS_CANNOT_FIND_SPECIFIED_SHAPE_IN_X3D_MESH = 886
    """Shape %d could not be found in %s."""

    VIS_CANNOT_FIND_SPECIFIED_ATTRIBUTE_IN_X3D_MESH = 887
    """Attribute %s could not be found in %s."""

    VIS_INVALID_SCENE_FILE_FORMAT = 888
    """Invalid XML scene file."""

    VIS_INVALID_MESH_FILE_FORMAT = 889
    """Invalid mesh file."""

    VIS_UNSUPPORTED_TEXTURE_FORMAT = 890
    """The selected texture file %s is not a supported file type."""

    VIS_TEXTURE_NOT_POWER_OF_2 = 891
    """To improve rendering efficiency, only textures with dimensions that are a power of 2 are supported (eg 512, 1024, 2048, etc).  Rectangular bitmaps are acceptable though (eg 512 x 1024)."""

    VIS_TEXTURE_FILE_FORMAT_INVALID = 892
    """The texture file is recognized, but the file is not in an expected format"""

    VIS_TEXTURE_FILE_INVALID_COLOR_DEPTH = 893
    """The texture file appears to be valid, but the color depth specified in this file is not supported."""

    VIS_TEXTURE_FILE_INVALID_COMPRESSION = 894
    """The texture file appears to be valid, but the compression scheme used is not supported."""

    VIS_OPENGL_REQUIRED_EXTENSION_NOT_FOUND = 895
    """A necessary extension was not found for the requested OpenGL version (%1.1f).  Updating your video drivers may solve the issue."""

    VIS_MESH_INVALID_SHAPE_REFERENCE = 896
    """The shape parameter specified for the mesh %s in the scene file must be greater or equal to zero."""

    VIS_MESH_INVALID_FACE_COUNT = 897
    """The face parameter specified for the mesh %s in the scene file must be an integer."""

    VIS_MESH_INVALID_STRIDE = 898
    """The stride parameter specified for the mesh %s, attribute %s in the scene file must be greater than zero."""

    VIS_MESH_INVALID_NUMBER_OF_ATTRIBUTE_ELEMENTS = 899
    """The number of attribute elements was not the expected stride."""

    VIS_MESH_INVALID_NUMBER_OF_INDICES = 900
    """The indices are expected to be a group of 4 numbers for each face."""

    VIS_MESH_INVALID_NUMBER_OF_NORMALS = 901
    """The normals are expected to be a group of 3 numbers for each vertex."""

    VIS_MESH_INVALID_NUMBER_OF_TEXTURE_COORDINATES = 902
    """The texture coordinates are expected to be a group of 2 numbers for each vertex."""

    VIS_MESH_INVALID_NUMBER_OF_VERTICES = 903
    """The vertices are expected to be in groups of 3 numbers."""

    VIS_MESH_INVALID_INDICES_INDEX = 904
    """An index references a vertex that is outside of the expected range."""

    VIS_MESH_ATTRIBUTE_NOT_EQUAL_TO_OTHER_VERTICES = 905
    """The attribute %s in mesh %s has %d elements which does not match the %d elements found in other attributes or the vertices count in the scene file.  If the mesh is marked as a flexible mesh, try rescanning the mesh file to recount the vertices or uncheck the flexible mesh property."""

    VIS_SHADER_VERTEX_NOT_SET = 906
    """The vertex shader has not been specified for %s."""

    VIS_SHADER_FRAGMENT_NOT_SET = 907
    """The fragment shader has not been specified for %s."""

    VIS_SHADER_VERTEX_COMPILE_FAILED = 908
    """Failed to compile the vertex shader file %s."""

    VIS_SHADER_FRAGMENT_COMPILE_FAILED = 909
    """Failed to compile the fragment shader file %s."""

    VIS_SHADER_NOT_COMPILED = 910
    """Internal error.  The graphics engine has attempted to use a shader that has not yet been successfully compiled."""

    VIS_OLD_SCENE_FILE_VERSION = 911
    """The scene file appears to be valid, but the version (%2.2f) is not compatible with the installed version of QUARC.  Version %2.2f was expected.  Please regenerate the scene file from your diagram."""

    VIS_UNRECOGNIZED_SCENE_FILE_VERSION = 912
    """The scene file appears to be valid, but the version (%2.2f) is from a newer version of QUARC.  Please upgrade this viewer to the most recent version.  If this viewer is being used independently of QUARC, an installer for just the viewer is available on the QUARC DVD."""

    VIS_SCENE_BACKGROUND_COLOR_INVALID = 913
    """Invalid background color in the scene file."""

    VIS_SCENE_AMBIENT_COLOR_INVALID = 914
    """Invalid ambient color specified in the scene file."""

    VIS_SCENE_FRAMERATE_INVALID = 915
    """Invalid frame rate specified in scene file."""

    VIS_SCENE_WIDTH_INVALID = 916
    """Invalid screen width specified in scene file."""

    VIS_SCENE_HEIGHT_INVALID = 917
    """Invalid screen height specified in scene file."""

    VIS_SCENE_MESH_ID_DUPLICATE = 918
    """A duplicate mesh ID %s was found.  All mesh ID's must be unique."""

    VIS_SCENE_MESH_ATTRIBUTE_ID_DUPLICATE = 919
    """A duplicate mesh attribute ID %s was found was found in mesh %s.  All mesh attribute ID's must be unique."""

    VIS_SCENE_TEXTURE_ID_DUPLICATE = 920
    """A duplicate texture ID %s was found.  All mesh ID's must be unique."""

    VIS_SCENE_SHADER_ID_DUPLICATE = 921
    """A duplicate shader ID %s was found.  All shader ID's must be unique."""

    VIS_SCENE_SHADER_VARIABLE_ID_DUPLICATE = 922
    """A duplicate shader variable ID %s was found in shader %s.  Shader variable ID's must be unique within each shader."""

    VIS_SCENE_SHADER_ATTRIBUTE_ID_DUPLICATE = 923
    """A duplicate shader attribute ID %s was found in shader %s.  Shader attribute ID's must be unique within each shader."""

    VIS_SCENE_NEAR_CLIPPING_INVALID = 924
    """Near clipping plane must greater than or equal to 0."""

    VIS_SCENE_FAR_CLIPPING_INVALID = 925
    """Near clipping plane must greater than 0."""

    VIS_SCENE_NEAR_FAR_COMBINATION_INVALID = 926
    """Far clipping plane must be greater than the near clipping plane."""

    VIS_SCENE_VIEW_ANGLE_INVALID = 927
    """Camera viewing angle must greater than 0."""

    VIS_SCENE_KEYBOARD_CAMERA_CONTROL_KEY_INVALID = 928
    """Unrecognized camera control key."""

    VIS_SCENE_MOUSE_CAMERA_CONTROL_KEY_INVALID = 929
    """Unrecognized mouse button."""

    VIS_SCENE_GESTURE_CAMERA_CONTROL_KEY_INVALID = 930
    """Unrecognized gesture control."""

    VIS_SCENE_FOG_MODE_INVALID = 931
    """The fog mode must be either linear, exp, or exp2."""

    VIS_SCENE_FOG_DENSITY_INVALID = 932
    """The fog density must defined and greater or equal to 0."""

    VIS_SCENE_FOG_COLOR_INVALID = 933
    """Invalid fog color."""

    VIS_SCENE_FOG_START_INVALID = 934
    """The fog start must greater or equal to 0."""

    VIS_SCENE_FOG_END_INVALID = 935
    """The fog end must greater than fog start."""

    VIS_SCENE_FOG_START_OR_END_UNDEFINED = 936
    """If linear fog is used, the start and end distances must be defined."""

    VIS_SCENE_OPENGL_VERSION_INVALID = 937
    """The requested OpenGL version number must greater or equal to 1.0."""

    VIS_SCENE_OBJECT_REFERENCES_UNKNOWN_MESH_ID = 938
    """Object %s references an unknown mesh ID %s."""

    VIS_SCENE_OBJECT_REFERENCES_UNKNOWN_TEXTURE_ID = 939
    """Object %s references an unknown texture ID %s."""

    VIS_SCENE_OBJECT_ID_DUPLICATE = 940
    """A duplicate object ID %s was found.  All object ID's must be unique."""

    VIS_SCENE_ACTOR_REFERENCES_UNKNOWN_MESH_ID = 941
    """Actor %s references an unknown mesh ID %s."""

    VIS_SCENE_ACTOR_REFERENCES_UNKNOWN_TEXTURE_ID = 942
    """Actor %s references an unknown texture ID %s."""

    VIS_SCENE_ACTOR_REFERENCES_UNKNOWN_OBJECT_ID = 943
    """Actor %s references an unknown object ID %s."""

    VIS_SCENE_ACTOR_REFERENCES_UNKNOWN_SHADER_ID = 944
    """Actor %s references an unknown shader ID %s."""

    VIS_SCENE_ACTOR_REFERENCES_UNKNOWN_SHADER_VARIABLE_ID = 945
    """Actor %s references an unknown shader variable ID %s in shader %s."""

    VIS_SCENE_ACTOR_MISSING_SHADER_ID = 946
    """Actor %s is missing a Shader reference."""

    VIS_SCENE_ACTOR_ID_DUPLICATE = 947
    """A duplicate actor ID %s was found.  All actor ID's must be unique."""

    VIS_SCENE_ACTOR_TYPE_UNKNOWN = 948
    """Actor type %s not recognized."""

    VIS_SCENE_ACTOR_POSITION_INVALID = 949
    """Actor %s's position invalid."""

    VIS_SCENE_ACTOR_SCALE_INVALID = 950
    """Actor %s's scale invalid."""

    VIS_SCENE_ACTOR_FOG_INVALID = 951
    """Actor %s's fog override must be true or false."""

    VIS_SCENE_ACTOR_ORIENTATION_INVALID = 952
    """Actor %s's orientation invalid."""

    VIS_SCENE_ACTOR_CHILD_AND_SIBLING_PROCESSING_ERROR = 953
    """An internal error has occured processing the actor relationships.  Please report this error to Quanser."""

    VIS_SCENE_ACTOR_INHERITANCE_INVALID = 954
    """Actor %s's inheritance must be true or false."""

    VIS_SCENE_ACTOR_COLOR_INVALID = 955
    """Actor %s's color invalid."""

    VIS_SCENE_ACTOR_EMISSIVE_INVALID = 956
    """Actor %s's emissivity value invalid."""

    VIS_SCENE_ACTOR_SPECULAR_INVALID = 957
    """Actor %s's specularity invalid."""

    VIS_SCENE_ACTOR_SHININESS_INVALID = 958
    """Actor shininess invalid."""

    VIS_SCENE_ACTOR_ID_NOT_FOUND = 959
    """Actor ID not found."""

    VIS_ACTOR_MESH_POOL_NOT_INITIALIZED = 960
    """Internal error.  Failed attempted to attach a mesh to an actor because the mesh pool is not initialized."""

    VIS_ACTOR_TEXTURE_POOL_NOT_INITIALIZED = 961
    """Internal error.  Failed attempted to attach a mesh to an actor because the texture pool is not initialized."""

    VIS_ACTOR_MESH_OUTSIDE_OF_MESH_POOL_BOUNDS = 962
    """Attempted to attach a mesh that is outside of the array bounds of loaded meshes."""

    VIS_ACTOR_TEXTURE_OUTSIDE_OF_TEXTURE_POOL_BOUNDS = 963
    """Attempted to attach a texture that is outside of the array bounds of loaded textures."""

    VIS_WRONG_MAGIC_NUMBER = 964
    """The connection was successful, but the received data was not in the expected format."""

    VIS_COMM_ACTOR_REFERENCE_NOT_VALID = 965
    """The communications stream refers to more actors than exist in the scene file."""

    VIS_COMM_ACTOR_PARAMETER_NOT_VALID = 966
    """The communications stream refers to an invalid actor parameter."""

    VIS_COMM_DATA_STREAM_PAYLOAD_NOT_OF_EXPECTED_SIZE = 967
    """Data stream payload is an unexpected size."""

    VIS_COMM_RECEIVE_BUFFER_TOO_SMALL = 968
    """The receive buffer is too small for the volume of data needed each frame.  Increase the receive buffer size then retry communications."""

    VIS_COMM_RECEIVE_BUFFER_SIZE_INVALID = 969
    """The receive buffer size is invalid"""

    VIS_COMM_SEND_BUFFER_SIZE_INVALID = 970
    """The send buffer size is invalid"""

    VIS_COMM_CONFIGURATION_PAYLOAD_NOT_OF_EXPECTED_SIZE = 971
    """Configuration payload is an unexpected size."""

    VIS_OLDER_QUARC_VERSION = 972
    """The connection was successful, but the model was compiled with an older version of QUARC that is incompatible. Rebuild the model to make it compatible with the current version."""

    MULTISAMPLE_OPERATION_NOT_SUPPORTED_DURING_DECIMATED_SAMPLING = 973
    """Multiple samples for the selected task operation are not supported with decimated sampling by this board.  Either set the decimation or the number of samples to 1."""

    HIL_SET_ANALOG_TERMINATION_STATE_NOT_SUPPORTED = 974
    """The hil_set_analog_termination_state function is not supported by this particular card."""

    HIL_SET_DIGITAL_TERMINATION_STATE_NOT_SUPPORTED = 975
    """The hil_set_digital_termination_state function is not supported by this particular card."""

    HIL_SET_PWM_TERMINATION_STATE_NOT_SUPPORTED = 976
    """The hil_set_pwm_termination_state function is not supported by this particular card."""

    HIL_SET_OTHER_TERMINATION_STATE_NOT_SUPPORTED = 977
    """The hil_set_other_termination_state function is not supported by this particular card."""

    HIL_AT_LEAST_ONE_CHANNEL_REQUIRED = 978
    """The HIL function requires at least one channel to be specified."""

    HIL_INVALID_DIGITAL_DIRECTIONS = 979
    """The combination of directions specified for the digital channels are not compatible with the capabilities of this particular card. Some cards have digital channels organized into ports for which all channels in a port must have the same direction. Check the documentation for the card."""

    HIL_WRITE_TERMINATION_STATES_NOT_SUPPORTED = 980
    """The hil_write_termination_states function is not supported by this particular card."""

    RCP_INVALID_SMOOTH_GEN_FREQUENCY = 981
    """The Smooth Signal Generator does not support the frequency entered."""

    RCP_INVALID_SMOOTH_GEN_AMPLITUDE = 982
    """The Smooth Signal Generator does not support the amplitude entered."""

    RCP_INVALID_SMOOTH_GEN_INPUT_SIZE = 983
    """The input array sizes should be equal and non-zero for the Smooth Signal Generator."""

    RCP_INVALID_SIGMOID_SAMPLE_TIME = 984
    """The sample time is not valid for the Sigmoid VI."""

    MISMATCHED_SCHEDULING_POLICY = 985
    """The scheduling policy for the thread must match the system scheduling policy on this target operating system."""

    HIL_DRIVER_NOT_FOUND = 986
    """Support for the given board type does not appear to be installed. Verify that you have selected the correct card in the HIL Initialize block or hil_open function."""

    HIL_UNABLE_TO_READ_BITFILE = 987
    """The FPGA bitfile could not be read. Make sure the FPGA bitfile is actually installed on the target."""

    HIL_INVALID_FPGA_SIGNATURE = 988
    """The specified signature does not match the signature of the bitfile. If the bitfile has been recompiled, regenerate the C API and rebuild the application."""

    HIL_INVALID_RESOURCE_NAME = 989
    """Either the supplied resource name is invalid as a RIO resource name, or the device was not found. Use MAX to find the proper resource name for the intended device."""

    FORCE_DIMENSION_OPEN_FAILED = 990
    """An attempt to open a Force Dimension haptic device failed. Ensure that the Force Dimension device is powered on and has been calibrated."""

    FORCE_DIMENSION_READ_FAILED = 991
    """An attempt to read from the Force Dimension haptic device failed."""

    FORCE_DIMENSION_WRITE_FAILED = 992
    """An attempt to write to the Force Dimension haptic device failed."""

    FORCE_DIMENSION_CLOSE_FAILED = 993
    """An attempt to close a Force Dimension haptic device failed."""

    FORCE_DIMENSION_NOT_CALIBRATED = 994
    """The Force Dimension haptic device has not been calibrated. Ensure that the device is properly calibrated before use."""

    NO_FORCE_DIMENSION_LICENSE = 995
    """You do not have a valid license for the Force Dimension blockset. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    RCP_CHASSIS_NOT_FOUND = 996
    """The driver could not determine the chassis attached to the real-time controller."""

    RCP_CHASSIS_NOT_SUPPORTED = 997
    """The NI chassis currently in use is not supported by this particular driver. Check the documentation to ensure a compatible chassis is in use."""

    RCP_INCORRECT_MODULE = 998
    """One or more of the modules in the NI chassis do not match the hardware configuration selected in the HIL Initialize. Be sure the correct modules are being used. Please correct the hardware configuration or select the proper configuration in the HIL Initialize block."""

    RCP_MODULE_IO_ERROR = 999
    """One or more of the modules in the NI chassis is causing an error which prevents I/O from being performed."""

    FPGA_ALREADY_RUNNING = 1000
    """The FPGA is already running."""

    RESOURCE_NOT_INITIALIZED = 1001
    """A required resource was not initialized."""

    CORRUPT_FPGA_BITFILE = 1002
    """The specified bitfile is invalid or corrupt."""

    FPGA_BUSY = 1003
    """Operation could not be performed because the FPGA is busy. Stop all the activities on the FPGA before requesting this operation."""

    FPGA_BUSY_C_API = 1004
    """Operation could not be performed because the FPGA is busy operating in FPGA Interface C API mode. Stop all the activities on the FPGA before requesting this operation."""

    FPGA_BUSY_SCAN_INTERFACE = 1005
    """The chassis is in Scan Interface programming mode. In order to run FPGA VIs, you must go to the chassis properties page, select FPGA programming mode, and deploy settings."""

    FPGA_BUSY_FPGA_INTERFACE = 1006
    """Operation could not be performed because the FPGA is busy operating in FPGA Interface mode. Stop all the activities on the FPGA before requesting this operation."""

    FPGA_BUSY_INTERACTIVE = 1007
    """Operation could not be performed because the FPGA is busy operating in Interactive mode. Stop all the activities on the FPGA before requesting this operation."""

    FPGA_BUSY_EMULATION = 1008
    """Operation could not be performed because the FPGA is busy operating in Emulation mode. Stop all the activities on the FPGA before requesting this operation."""

    QBUS_NO_MODULES_FOUND = 1009
    """No QBus modules could be detected."""

    QBUS_UNRECOGNIZED_MODULE = 1010
    """An unrecognized QBus module was found."""

    SPI_INSUFFICIENT_BYTES_TO_SEND_AND_RECEIVE = 1011
    """The given buffer is too small to do a single send or receive for this protocol. The protocol uses a word length larger than the number of bytes supplied."""

    PARITY_NOT_SUPPORTED = 1012
    """The selected serial port does not support parity checking. Set the parity option on the URI to 'none'."""

    HARDWARE_FLOW_CONTROL_NOT_SUPPORTED = 1013
    """The selected serial port does not support hardware flow control. Set the flow option on the URI to 'none' or 'software' (if supported)."""

    SOFTWARE_FLOW_CONTROL_NOT_SUPPORTED = 1014
    """The selected serial port does not support software flow control. Set the flow option on the URI to 'none' or 'hardware' (if supported)."""

    DTR_DSR_NOT_SUPPORTED = 1015
    """The selected serial port does not support the data-terminal-ready (DTR) and data-set-ready (DSR) lines. Set the dsr option on the URI to 'off'."""

    PARITY_VALUE_NOT_SUPPORTED = 1016
    """The value specified for the parity is not supported by the given serial port. Use a different parity setting if possible or select 'none' for no parity checking."""

    STOP_BITS_VALUE_NOT_SUPPORTED = 1017
    """The value specified for the stop bits is not supported by the given serial port. Use a different number of stop bits if possible. A value of 1 is recommended."""

    WORD_LENGTH_VALUE_NOT_SUPPORTED = 1018
    """The value specified for the word length is not supported by the given serial port. Use a different word length if possible. A value of 8 is recommended."""

    NO_DATA_TO_SEND = 1019
    """There is no data to send. It is not possible to send zero-length arrays. If data will never be sent then configure the send options to not send data at all. Setting the enable input to false is not enough because the enable input is only intended to temporarily enable or disable transmission. If the stream is configured to send data then a valid data type must be connected even if the enable input is false."""

    RCP_MISSING_MODULE = 1020
    """One or more of the modules in the NI chassis that is required by the hardware configuration selected in the HIL Initialize is missing. Please correct the hardware configuration or select the proper configuration in the HIL Initialize block."""

    RCP_MISSING_ANALOG_INPUT_MODULE = 1021
    """The module in the NI chassis required for the selected channels of analog input is missing."""

    RCP_MISSING_ANALOG_OUTPUT_MODULE = 1022
    """The module in the NI chassis required for the selected channels of analog output is missing. Make sure these channels are not being written by the HIL Initialize block by unchecking the Initial and Final output fields of the Analog Outputs tab."""

    RCP_MISSING_ENCODER_INPUT_MODULE = 1023
    """The module in the NI chassis required for the selected channels of encoder input is missing."""

    RCP_MISSING_PWM_OUTPUT_MODULE = 1024
    """The module in the NI chassis required for the selected channels of PWM output is missing. Make sure these channels are not being written by the HIL Initialize block by unchecking the Initial and Final output fields of the PWM Outputs tab."""

    RCP_MISSING_DIGITAL_INPUT_MODULE = 1025
    """The module in the NI chassis required for the selected channels of digital input is missing."""

    RCP_MISSING_DIGITAL_OUTPUT_MODULE = 1026
    """The module in the NI chassis required for the selected channels of digital output is missing. Make sure these channels are not being written by the HIL Initialize block by unchecking the Initial and Final output fields of the Digital I/O tab."""

    RCP_MISSING_OTHER_INPUT_MODULE = 1027
    """The module in the NI chassis required for the selected channels of other input is missing."""

    RCP_MISSING_OTHER_OUTPUT_MODULE = 1028
    """The module in the NI chassis required for the selected channels of other output is missing. Make sure these channels are not being written by the HIL Initialize block by unchecking the Initial and Final output fields of the Other Outputs tab."""

    DEVICE_NOT_CONNECTED = 1029
    """The device is not connected. If the device was connected then somehow that connection has been lost."""

    TOO_MANY_PROPERTIES = 1030
    """Too many properties were specified."""

    PSTREAM_NOT_VARIABLE_SIZE = 1031
    """The persistent stream has not been configured for variable-size signals in the direction attempted."""

    PSTREAM_VARIABLE_SIZE = 1032
    """The persistent stream has been configured for variable-size signals in the direction attempted."""

    INVALID_DIMENSIONS = 1033
    """The dimensions exceed the maximum dimensions specified."""

    LEAPMOTION_NOT_FOUND = 1034
    """The Leap Motion device cannot be found on the system."""

    CANNOT_RESET_ENCODER_TO_NONZERO_VALUE = 1035
    """The encoder cannot be reset to a non-zero value on this device."""

    ENCODER_INPUT_ERROR = 1036
    """An error has occurred reading an encoder input. Make sure the encoder is connected reliably, there are no ground loops and signal noise is minimized."""

    STALL_OCCURRED = 1037
    """A stall condition was detected. Please ensure that your device is free to move and is functioning properly."""

    ONLY_I2C_MASTER_MODE_SUPPORTED = 1038
    """Only the I2C master mode is supported by the device being used for I2C communications. Different hardware is required for slave mode."""

    NO_DEVICE_ADDRESS = 1039
    """No device address was specified. See the options for the communications protocol."""

    NO_ACKNOWLEDGEMENT = 1040
    """Device did not send an acknowledgement. Device may not be present or an error may have occurred."""

    NO_KINECT_SENSOR = 1041
    """No Kinect sensor was detected with the given index or identifier."""

    INVALID_KINECT = 1042
    """Invalid Kinect sensor."""

    KINECT_NOT_FOUND = 1043
    """The corresponding Kinect Initialize could not be found. Make sure that a Kinect Initialize block is present in the model."""

    KINECT_FEATURE_NOT_ENABLED = 1044
    """The Kinect has been initialized without at least one of the requested features. Some of the features will not be available."""

    KINECT_NOT_INITIALIZED = 1045
    """The Kinect sensor has not been initialized."""

    KINECT_ALREADY_INITIALIZED = 1046
    """The Kinect sensor is already initialized so the requested settings can no longer be configured. Set options before calling the kinect_initialize function."""

    RESOLUTION_NOT_SUPPORTED = 1047
    """The selected image resolution is not supported."""

    NO_SPI_CHIP_SELECT = 1048
    """No SPI chip select signal was chosen using the frame or slave options of the URI. The current hardware requires that a chip select be used."""

    MULTIPLE_SPI_CHIP_SELECTS = 1049
    """More than one SPI chip select signal was chosen by setting both the frame and slave options of the URI. The current hardware does not support both at the same time. Choose one or the other."""

    UNSUPPORTED_I2C_OPERATION = 1050
    """The I2C protocol for the selected target only supports combined write-read messages. Other combinations of read and write operations are not supported in exclusive mode."""

    DIGITAL_EXPIRATION_STATE_NOT_ZERO = 1051
    """This board only supports resetting the digital outputs to zero when the watchdog expires."""

    PWM_EXPIRATION_STATE_NOT_ZERO = 1052
    """This board only supports resetting the PWM outputs to zero when the watchdog expires."""

    OTHER_EXPIRATION_STATE_NOT_ZERO = 1053
    """This board only supports resetting the other outputs to zero when the watchdog expires."""

    KINECT_NOT_SUPPORTED = 1054
    """The type of Kinect selected is not currently supported on this target."""

    INVALID_MICO = 1055
    """Invalid object. A Kinova MICO robot object cannot be used after it has been closed."""

    MICO_INVALID_JOINT = 1056
    """The joint specified for the Kinova MICO device is outside the valid range."""

    MICO_MESSAGE_INVALID = 1057
    """The Kinova MICO serial link message is invalid."""

    MICO_FIRMWARE_VERSION_NOT_READ = 1058
    """The Kinova MICO firmware version could not be read. Ensure the robot arm is powered up and properly connected to the external computer."""

    MICO_FIRMWARE_VERSION_NOT_SUPPORTED = 1059
    """The Kinova MICO joint and/or finger firmware version number is not supported."""

    MICO_ERROR = 1060
    """Error from the Kinova MICO device."""

    MICO_ERROR_CANNOT_READ = 1061
    """Error from the Kinova MICO device: cannot perform the read operation."""

    MICO_ERROR_CANNOT_WRITE = 1062
    """Error from the Kinova MICO device: cannot perform the write operation."""

    INVALID_ROS = 1063
    """The ROS property object is not valid. A ROS property object cannot be used after it has been closed."""

    ROS_ERROR = 1064
    """The ROS system is inaccessible."""

    INVALID_ROS_TOPIC = 1065
    """The ROS topic is not recognized."""

    ROS_SHUTDOWN = 1066
    """The ROS system is shutdown."""

    ROS_INIT_ERROR = 1067
    """There was a problem initializing ROS."""

    INVALID_BOARD_VERSION = 1068
    """Version information retrieved from the HIL board does not match the driver. It may be necessary to update the QUARC software to get the latest drivers."""

    UNABLE_TO_PROGRAM_FIRMWARE = 1069
    """Unable to program firmware."""

    WRONG_NUMBER_OF_BYTES_RECEIVED = 1070
    """The wrong number of bytes was received from a device or peer. This mismatch may indicate a driver or protocol incompatibility."""

    INCOMPATIBLE_HARDWARE_VERSION = 1071
    """The hardware version is incompatible with the firmware being flashed. No changes were made to the firmware."""

    INCOMPATIBLE_FIRMWARE_IMAGE = 1072
    """The version of the firmware image is not compatible with the driver. No changes were made."""

    BOARD_ALREADY_OPEN = 1073
    """The HIL board is already opened by another process. The board does not support access from more than one process at the same time."""

    UNSUPPORTED_VIDEO_FORMAT = 1074
    """The video format is not supported. This may be due to the frame rate, frame size or native video formats of the device or source."""

    INVALID_PACKET = 1075
    """The packet format is invalid."""

    INVALID_CHECKSUM = 1076
    """The checksum is invalid. The data may have been corrupted."""

    NEWER_VERSION_INSTALLED = 1077
    """A newer version is installed. No changes have been made."""

    INVALID_ALIGNMENT_TYPE = 1078
    """The alignment type is invalid."""

    INVALID_ALLOCATION_CHUNK = 1079
    """The maximum allocation chunk is invalid."""

    INVALID_BUFFER_MODE = 1080
    """The buffer mode is invalid."""

    INVALID_COMPONENT_ID = 1081
    """The component ID is invalid."""

    INVALID_CROP_REQUEST = 1082
    """The crop request is invalid."""

    DCT_COEFFICIENT_OUT_OF_RANGE = 1083
    """The DCT coefficient out of range."""

    IDCT_SIZE_NOT_SUPPORTED = 1084
    """The specified IDCT output block size is not supported."""

    MISMATCHED_SAMPLING_RATIO = 1085
    """The sampling ratio is mismatched."""

    INVALID_HUFFMAN_TABLE = 1086
    """The Huffman table definition is invalid."""

    INVALID_INPUT_COLORSPACE = 1087
    """The input colorspace is invalid."""

    INVALID_JPEG_COLORSPACE = 1088
    """The JPEG colorspace is invalid."""

    INVALID_MARKER_LENGTH = 1089
    """The marker length is invalid."""

    INVALID_MCU_SIZE = 1090
    """The sampling factors are too large for an interleaved scan."""

    INVALID_POOL_ID = 1091
    """The memory pool code is invalid."""

    INVALID_PRECISION = 1092
    """The specified data precision is not supported."""

    INVALID_PROGRESSION = 1093
    """The progressive image parameters are invalid."""

    INVALID_PROGRESSIVE_SCRIPT = 1094
    """The progressive image parameters at the scan script entry are invalid."""

    INVALID_SAMPLING = 1095
    """The sampling factors are invalid."""

    INVALID_SCAN_SCRIPT = 1096
    """The scan script is invalid."""

    INVALID_LIBRARY_STATE = 1097
    """A library call was made when the library is not in the proper state. Call sequence is likely invalid."""

    INVALID_STRUCT_SIZE = 1098
    """The structure size was invalid. The library may not be the same version as the caller."""

    INVALID_VIRTUAL_ACCESS = 1099
    """The virtual array access was invalid."""

    CANNOT_SUSPEND = 1100
    """Suspension is not allowed at this point."""

    CCIR601_NOT_IMPLEMENTED = 1101
    """CCIR601 sampling is not implemented yet."""

    COLOR_COMPONENT_COUNT = 1102
    """There are too many color components."""

    COLOR_CONVERSION_NOT_IMPLEMENTED = 1103
    """The specified color conversion is not supported."""

    INVALID_DAC_INDEX = 1104
    """Invalid DAC index."""

    INVALID_DAC_VALUE = 1105
    """Invalid DAC value."""

    INVALID_DHT_INDEX = 1106
    """Invalid DHT index."""

    INVALID_DQT_INDEX = 1107
    """Invalid DQT index."""

    EMPTY_IMAGE = 1108
    """The image is empty. Empty images are not currently supported."""

    EMS_READ_FAILED = 1109
    """A read from the EMS failed."""

    EMS_WRITE_FAILED = 1110
    """A write to the EMS failed."""

    END_OF_INPUT_EXPECTED = 1111
    """The end of the input was expected. There is too much input data."""

    FILE_READ_FAILED = 1112
    """An error occurred reading from a file."""

    FILE_WRITE_FAILED = 1113
    """An error occurred writing to a file. There may not be enough disk space."""

    FRACTIONAL_SAMPLING_NOT_IMPLEMENTED = 1114
    """Fractional sampling is not implemented yet."""

    HUFFMAN_TABLE_OVERFLOW = 1115
    """The Huffman code size table overflowed."""

    HUFFMAN_MISSING_CODE = 1116
    """A Huffman code table entry was missing."""

    IMAGE_TOO_BIG = 1117
    """The image was too big."""

    MISMATCHED_QUANTIZATION_TABLE = 1118
    """It is not possible to transcode due to multiple uses of the quantization table."""

    MISSING_SCAN_DATA = 1119
    """The scan script does not transmit all data."""

    COLOR_MODE_CHANGE_INVALID = 1120
    """The color quantization mode change was invalid."""

    FEATURE_NOT_COMPILED = 1121
    """The requested feature was omitted at compile time."""

    NO_ARITHMETIC_TABLE = 1122
    """An arithmetic table was not defined."""

    BACKING_STORE_NOT_SUPPORTED = 1123
    """A backing store is not supported."""

    NO_HUFFMAN_TABLE = 1124
    """A Huffman table was not defined."""

    NO_QUANTIZATION_TABLE = 1125
    """A quantization table was not defined."""

    INVALID_FILE_TYPE = 1126
    """The file type is wrong."""

    TOO_MANY_QUANTIZATION_COMPONENTS = 1127
    """There were too many color components to quantize."""

    CANNOT_QUANTIZE_TO_FEW_COLORS = 1128
    """It is not possible to quantize to so few colors."""

    CANNOT_QUANTIZE_TO_MANY_COLORS = 1129
    """It is not possible to quantize to so many colors."""

    SOF_DUPLICATE = 1130
    """There are too many SOF markers. The file structure is invalid."""

    NO_SOS_MARKER = 1131
    """The SOS marker is missing. The file structure is invalid."""

    SOF_NOT_SUPPORTED = 1132
    """The SOF marker type is not supported."""

    SOI_DUPLICATE = 1133
    """There are too many SOI markers. The file structure is invalid."""

    SOS_BEFORE_SOF = 1134
    """An SOS marker occurred before an SOF marker. The file structure is invalid."""

    CANNOT_CREATE_TEMPORARY_FILE = 1135
    """Failed to create a temporary file."""

    CANNOT_READ_TEMPORARY_FILE = 1136
    """Failed to read a temporary file."""

    CANNOT_SEEK_TEMPORARY_FILE = 1137
    """Failed to seek on a temporary file."""

    CANNOT_WRITE_TEMPORARY_FILE = 1138
    """Failed to write to a temporary file. There may not be enough disk space."""

    TOO_LITTLE_DATA = 1139
    """Not enough data was supplied."""

    MARKER_NOT_SUPPORTED = 1140
    """The marker type is not supported."""

    VIRTUAL_ARRAY_BUG = 1141
    """The virtual array controller is confused."""

    IMAGE_TOO_WIDE = 1142
    """The image is too wide for this implementation."""

    XMS_READ_FAILED = 1143
    """A read from the XMS failed."""

    XMS_WRITE_FAILED = 1144
    """A write to the XMS failed."""

    NO_DESTINATION_SET = 1145
    """The operation cannot be performed because no destination has been configured for the operation."""

    COMPRESSED_IMAGE_TOO_LARGE = 1146
    """The compressed image is too large to fit in the destination. If you are using the Image Compress block then make the output dimension larger."""

    HIL_NAME_NOT_ASSIGNED = 1147
    """The specified virtual name for the HIL card has not been assigned to an actual device."""

    HIL_SET_ANALOG_INPUT_CONFIGURATION_NOT_SUPPORTED = 1148
    """The hil_set_analog_input_configuration function is not supported by this particular card."""

    MISSING_ANALOG_INPUT_CONFIGURATION = 1149
    """No configurations were specified when setting the analog input configuration, even though the number of channels indicated was non-zero."""

    INVALID_ANALOG_INPUT_CONFIGURATION = 1150
    """One of the configurations specified for an analog input channel is not valid for the selected hardware."""

    INCOMPATIBLE_HARDWARE = 1151
    """The hardware appears to be incompatible with the board type selected."""

    BAUD_RATE_EXCEEDS_MAXIMUM = 1152
    """The baud rate exceeds the maximum baud rate set when the stream was created."""

    MISMATCHED_PWM_PERIOD_IN_BANK = 1153
    """One of the PWM periods specified does not match the period of the other channels. This card only allows one PWM period to be set for all PWM channels in a bank."""

    CALIBRATION_FAILED = 1154
    """Sensor calibration failed for some reason. Try running the model again."""

    INVALID_I2C_STATE = 1155
    """The I2C channel has entered an unexpected state."""

    PARITY_ERROR = 1156
    """A parity error occurred"""

    FRAMING_ERROR = 1157
    """A framing error occurred"""

    FILE_TOO_LARGE = 1158
    """The file has become too large for the given file format."""

    INVALID_MEDIA_TYPE = 1159
    """The media type is not supported, either because parameters such as the frame rate are invalid or there is no codec for that media type."""

    DEVICE_DISCONNECTED = 1160
    """Device was disconnected, this can be caused by outside intervention, by internal firmware error or due to insufficient power."""

    OS_ERROR = 1161
    """Error was returned from the underlying OS-specific layer."""

    WRONG_CALL_SEQUENCE = 1162
    """Function precondition was violated. Functions were called in the wrong order."""

    DEVICE_RECOVERING = 1163
    """Device is in recovery mode and might require firmware update."""

    DEVICE_IO_ERROR = 1164
    """I/O device failure."""

    PROPERTY_IS_READ_ONLY = 1165
    """The property is read-only. It cannot be set."""

    IMAGE_STREAM_NOT_FOUND = 1166
    """The specified image stream could not be found. The stream type may not be supported by the camera or the stream index is too large."""

    MISSING_REALSENSE = 1167
    """The RealSense 2 library is not installed."""

    EMITTER_CANNOT_BE_DISABLED = 1168
    """The laser emitter on the depth camera cannot be disabled."""

    INVALID_CAMERA_PROPERTY_VALUE = 1169
    """The property value specified is not supported by the camera. Check that the value corresponds with the camera selected."""

    INVALID_STRIDE = 1170
    """The image stride was either too small or is not a multiple of the pixel size."""

    INVALID_FILE_HANDLE = 1171
    """The file handle is not valid. An attempt was made to use a file that is not open."""

    BAROMETER_NOT_RESPONDING = 1172
    """The barometer is not responding. The device may have been damaged."""

    MAGNETOMETER_NOT_RESPONDING = 1173
    """The magnetometer is not responding. The device may have been damaged."""

    CONFLICTING_DIGITAL_MODES = 1174
    """The specified digital IO is configured for a special purpose (e.g. PWM, Encoder, SPI, I2C, UART). Therefore it cannot be used as the specified function. Refer to the device documentation for precedents and limitations of the generic digital IO."""

    ELVISIII_TOP_BOARD_NO_POWER = 1175
    """The NI ELVIS III top board is not powered, the top board must be powered before this board can be used."""

    ELVISIII_EEPROM_ERROR = 1176
    """Failed to access the NI ELVIS III top board EEPROM during initialization.  Try power cycle the ELVIS III.  If the error persists, then the problem is likely a hardware fault."""

    ELVISIII_TOP_BOARD_INCOMPATIBLE = 1177
    """The top board attached to the NI ELVIS III is not compatbile with the driver, make sure the correct top board is attached that matches the board type as selected in HIL Initialize."""

    NO_ELVISIII_LICENSE = 1178
    """You do not have a valid license for the NI ELVIS III you are using. Make sure you install QUARC with a license file that has NI ELVIS III support, and then run NI MAX to install QUARC on the NI ELVIS III."""

    NO_RIO_GENERIC_LICENSE = 1179
    """You do not have a valid license for the myRIO or generic NI ELVIS III board. Make sure you install QUARC with a license file that has myRIO or generic NI ELVIS III board support, and then run NI MAX to install QUARC on the myRIO or NI ELVIS III."""

    BORDER_TYPE_NOT_SUPPORTED = 1180
    """The border type selected for the operation is not supported by the current operation."""

    FILTER_MASK_SIZE_NOT_SUPPORTED = 1181
    """The mask size specified for the filter is not supported. Many filter operations only support 3x3 or 5x5 mask sizes. The mask should also be smaller than the image."""

    INVALID_ALGORITHM_HINT = 1182
    """The specified algorithm hint is not supported."""

    INVALID_ROUNDING_MODE = 1183
    """The specified rounding mode is not supported."""

    INVALID_DATA_TYPE = 1184
    """The specified data type is not supported."""

    CANNOT_AUTODETECT_DSM_EXTERNAL = 1185
    """The type of DSM protocol cannot be auto-detected for external remotes."""

    PROPERTY_NOT_SUPPORTED = 1186
    """The specified property is not supported."""

    CANNOT_INITIALIZE_OPENVR = 1187
    """The OpenVR cannot be properly initialized due to an error."""

    HIL_TASK_SET_BUFFER_OVERFLOW_MODE_NOT_SUPPORTED = 1188
    """The hil_task_set_buffer_overflow_mode function is not supported by this particular card."""

    HIL_TASK_GET_BUFFER_OVERFLOWS_NOT_SUPPORTED = 1189
    """The hil_task_get_buffer_overflows function is not supported by this particular card."""

    MACRO_NOT_TERMINATED = 1190
    """A macro was missing the closing parenthesis."""

    INVALID_MACRO_NAME = 1191
    """The macro does not match any of the standard macro names or the name of an environment variable."""

    UNSUPPORTED_IMAGE_CONVERSION = 1192
    """Conversion between the two image formats selected is not currently supported."""

    CANNOT_CONVERT_CHARACTER = 1193
    """A character was encountered that cannot be converted."""

    NO_DEVICE = 1194
    """The device is not available. Check that the device is plugged in or has not been reset."""

    PROTOCOL_BUFFER_TOO_SMALL = 1195
    """The buffer for the underlying communication protocol is too small to send or receive the data requested. Try using the sndsize, rcvsize, bufsize or memsize options of the URI to increase the requisite buffer size."""

    INVALID_CALIBRATION = 1196
    """The calibration data appears to be invalid."""

    RANGING_SENSOR_ERROR = 1197
    """The ranging sensor could not detect the range due to an error."""

    IO_ERROR = 1198
    """An I/O error occurred."""

    DIVISION_BY_ZERO = 1199
    """A division by zero occurred."""

    DEVICE_INITIALIZATION_FAILED = 1200
    """Device initialization failed."""

    DEVICE_DRIVER_INCOMPATIBLE = 1201
    """The device driver appears to be incompatible with the device."""

    HARDWARE_FAILURE = 1202
    """The hardware appears to have failed. It is either not responding, or not responding as expected. Try powering down and back up."""

    SCALING_LOSES_ASPECT_RATIO = 1203
    """The scaling of the width and height is not the same. The aspect ratio will be changed, which is not currently supported."""

    SCALE_FACTOR_NOT_SUPPORTED = 1204
    """The given scale factor is not currently supported."""

    BUFFER_TOO_SMALL = 1205
    """The supplied buffer is too small for the data requested."""

    INVALID_REALSENSE_VERSION = 1206
    """The version of the Intel RealSense API expected does not match the version that is installed. The versions must match exactly."""

    INVALID_JSON = 1207
    """The JSON is invalid. JSON values must be objects, arrays, numbers, strings, true, false or null."""

    NO_CODEC_FOUND = 1208
    """No suitable codec was found to encode or decode the content."""

    CANNOT_START_XMLRPC_SERVER = 1209
    """The XMLRPC server cannot be started."""

    CANNOT_START_XMLRPC_CLIENT = 1210
    """The XMLRPC client cannot be started."""

    CANNOT_TALK_TO_ROS_MASTER = 1211
    """The XMLRPC client cannot establish communication with ROS master."""

    INVALID_ROS_MASTER_RESPONSE = 1212
    """The ROS master has responded with invalid response."""

    ROS_MASTER_CALLER_ERROR = 1213
    """The ROS master indicates that the ROS master API was called with caller error. In general, this means that the master/slave did not attempt to execute the action."""

    ROS_MASTER_CALLER_FAILURE = 1214
    """The ROS master indicates that the ROS master API failed to complete completely.  In general, this means that the master/slave attempted the action and failed, and there may have been side-effects as a result."""

    INVALID_ROS_SLAVE_REQUEST = 1215
    """The ROS slave API request is invalid."""

    UNSUPPORTED_ROS_PROTOCOL = 1216
    """The requested ROS protocol is not supported. Currently this node only supports TCPROS and UDPROS protocols."""

    ROS_NOT_ACTIVE = 1217
    """The ROS node is not valid. It may not have been made active during normal simulation in the ROS Initialize block and thus may be uninitialized."""

    CAMERA_IN_USE = 1218
    """The camera is already in use by another application."""

    MUTEX_ALREADY_EXISTS = 1219
    """The named mutex already exists."""

    MUTEX_ABANDONED = 1220
    """The mutex was owned by another thread but that thread terminated while the lock was still held so the mutex has been abandoned. The caller now owns the mutex but should check for consistency of the shared resource."""

    MUTEX_NOT_FOUND = 1221
    """The named mutex could not be found."""

    IMAGE_DATA_TYPE_NOT_SUPPORTED = 1222
    """The data type selected is not currently supported by the chosen image format."""

    PROTOCOL_DRIVER_NOT_FOUND = 1223
    """Support for the given protocol type does not appear to be installed. Verify that you have entered the correct URI for the Stream blocks or stream_connect/stream_listen functions."""

    CPU_GPIO_IN_USE = 1224
    """A GPIO is in use by another application. Some applications on Linux-based systems use the old sysfs (/sys/class/gpio) file system for GPIO. If a GPIO is exported it cannot be used by QUARC. Try rebooting the target."""

    OPTITRACK_LIBRARY_OPEN_FAILED = 1225
    """The Motive library failed to open. Make sure you have the Motive software installed and the appropriate environment variables (refer to the device help page) set correctly."""

    OPTITRACK_UNSUPPORTED_API_FUNCTION = 1226
    """The required Motive API is not available. Make sure you have the correct version of the Motive software installed. E.g. older Motive software does not support loading of user profile (.xml or .motive) file and must use trackable (.tra) file for rigid bodies definitions."""

    OPTITRACK_UNSUPPORTED_RIGID_BODY_DEF_FILE = 1227
    """The specified rigid body definition is not supported. Currently only .xml, .motive, and .tra files are supported."""

    OPTITRACK_INVALID_PROFILE_FILE = 1228
    """Unable to load Motive user profile file. Make sure the file path is correct."""

    UNABLE_TO_LOAD_CUDA_KERNEL = 1229
    """Unable to load CUDA kernel. The installed CUDA version may be incompatible with the CUDA code."""

    UNABLE_TO_GET_CUDA_FUNCTION = 1230
    """Unable to get CUDA function from kernel. The mangled function name is likely incorrect."""

    CAN_BUS_IDENTIFIER_TOO_LARGE = 1231
    """The CAN bus identifier is too large for the standard frame format. Use the flexible=1 option on the URI to allow extended CAN FD frames if your CAN device supports it."""

    INVALID_IPV6_ADDRESS = 1232
    """The IPv6 address is invalid or incomplete. On Linux systems, the zone identifier must be used by clients to identify the network interface (e.g. eth0) through which a link local address is connecting e.g. tcpip6://[fe80::abcd:beef:1234:5678%eth0]:18000"""

    CANNOT_GET_CAMERA_PROPERTIES = 1233
    """Unable to get the properties of the camera. This may indicate a hardware issue."""

    INVALID_CUDA_CONTEXT = 1234
    """The CUDA context has not been initialized. This may indicate version mismatches."""

    MAP_FAILED = 1235
    """Failed to perform a mapping or register operation."""

    RESOURCE_IN_USE = 1236
    """The desired resource is already in use for another operation."""

    CUDA_CONTEXT_IN_USE = 1237
    """The CUDA context passed to an API call is already in use by another thread."""

    CUDA_COMPILATION_FAILED = 1238
    """Compilation of CUDA PTX code failed. The CUDA PTX source is invalid or the JIT PTX compilation library was not found."""

    INVALID_GRAPHICS_CONTEXT = 1239
    """The OpenGL or DirectX graphics context is invalid."""

    UNRECOVERABLE_ERROR = 1240
    """An unrecoverable error occurred. The application will need to be re-run."""

    INCOMPATIBLE_TEXTURING_MODE = 1241
    """The CUDA kernel launched using an incompatible texturing mode."""

    INVALID_PEER_ACCESS = 1242
    """The peer access was invalid. It may not be enabled or may have already been enabled."""

    OBJECT_ALREADY_INITIALIZED = 1243
    """The object was already initialized and cannot be re-initialized."""

    TOO_MANY_CUDA_BLOCKS = 1244
    """Too many CUDA blocks were used with a cooperative kernel."""

    MISSING_FGLOVE = 1245
    """The 5DT Data Glove SDK does not appear to be installed or is not in the PATH. See the help for the FDT Data Glove block for the installation requirements. Note that a reboot may be required after installing the SDK."""

    MISSING_FORCE_DIMENSION = 1246
    """The Force Dimension SDK does not appear to be installed or is not in the PATH. See the help for the Force Dimension Write block for the installation requirements. Note that a reboot may be required after installing the SDK."""

    MISSING_FLY_CAPTURE = 1247
    """The FlyCapture SDK does not appear to be installed or is not in the PATH. See the help for the PGR Grab Image block for the installation requirements. Note that a reboot may be required after installing the SDK."""

    MISSING_PCAN = 1248
    """The PCAN-Basic API does not appear to be installed or is not in the PATH. See the help for the Peak CAN block for the installation requirements. Note that a reboot may be required after installing the SDK."""

    MISSING_VICON = 1249
    """The Vicon DataStream SDK does not appear to be installed or is not in the PATH. See the help for the Vicon block for the installation requirements. Note that a reboot may be required after installing the SDK."""

    MISSING_LEAPMOTION = 1250
    """The Leap SDK does not appear to be installed or is not in the PATH. See the help for the Leap Motion block for the installation requirements. Note that a reboot may be required after installing the SDK."""

    MISSING_CANPCI = 1251
    """The CANPCI SDK does not appear to be installed or is not in the PATH. See the help for the CANPCI block for the installation requirements. Note that a reboot may be required after installing the SDK."""

    MISSING_SCHUNK = 1252
    """The Schunk PowerCube software does not appear to be installed or is not in the PATH. See the help for the Schunk Gripper block for the installation requirements. Note that a reboot may be required after installing the SDK."""

    MISSING_FALCON = 1253
    """The HDAL software does not appear to be installed or is not in the PATH. See the help for the Novint Falcon block for the installation requirements. Note that a reboot may be required after installing the SDK."""

    NO_THREAD_CANCELLATION_STATE = 1254
    """The calling thread does not support setting the cancellation state of the thread. The thread was not created with qthread_create."""

    MISSING_OPENVR = 1255
    """The OpenVR SDK software does not appear to be installed or is not in the PATH. See the help for the Tracker block for the installation requirements. Note that a reboot may be required after installing the SDK."""

    UNSUPPORTED_AUDIO_FORMAT = 1256
    """The audio format is not supported. This may be due to a missing audio codec on some targets."""

    CORRUPT_FILE = 1257
    """The file is corrupt or is not the expected format."""

    WRONG_MODE_FOR_TRIGGERING = 1258
    """The session is in the wrong mode for triggering."""

    CAMERA_NAME_NOT_ASSIGNED = 1259
    """The specified virtual name for the camera has not been assigned to an actual device."""

    NOT_HIL_PROXY = 1260
    """The server to which a connection was attempted is not a HIL proxy server or HIL simulation."""

    NOT_VIDEO3D_PROXY = 1261
    """The server to which a connection was attempted is not a Video3D proxy server or Video3D simulation."""

    NO_DEVICE_SIMULATION_LICENSE = 1262
    """You do not have a valid license for using third-party devices in normal simulation. To configure licensing use the Configure License utility found under Start Menu/All Programs/Quanser for your product."""

    NO_HIL_PROXY = 1263
    """The connection to the HIL simulation or HIL Proxy Server was refused. If using a simulated device, make sure the simulation is running."""

    PRODUCT_NOT_IN_LICENSE_FILE = 1264
    """The product code specified could not be found in the license file."""

    BUFFER_MODE_NOT_SUPPORTED = 1265
    """The specified buffer mode is not supported."""

    MISSING_FORMAT_SPECIFIER = 1266
    """A format specifier is missing in the option template."""

    INVALID_FORMAT_RESTRICTION = 1267
    """An invalid restriction on a format specifier was specified."""

    INVALID_TIMER_SEMAPHORE = 1268
    """The timer semaphore passed as an argument is invalid."""

    NOT_VIDEO_PROXY = 1269
    """The server to which a connection was attempted is not a Video proxy server or Video simulation."""

    SAMPLES_LOST = 1270
    """Samples were lost or corrupted because the device cannot keep up. The sampling frequency is too fast or too many samples have been requested. Try fewer samples or a slower sampling frequency."""

    QARM_COMM_FAILURE_J0 = 1271
    """Communication to the Yaw motor has been lost or corrupted. Please power cycle the arm and contact your local Quanser support team if the issue continues."""

    QARM_COMM_FAILURE_J1_MASTER = 1272
    """Communication to the Master Shoulder motor has been lost or corrupted. Please power cycle the arm and contact your local Quanser support team if the issue continues."""

    QARM_COMM_FAILURE_J1_SLAVE = 1273
    """Communication to the Slave Shoulder motor has been lost or corrupted. Please power cycle the arm and contact your local Quanser support team if the issue continues."""

    QARM_COMM_FAILURE_J2 = 1274
    """Communication to the Elbow motor has been lost or corrupted. Please power cycle the arm and contact your local Quanser support team if the issue continues."""

    QARM_COMM_FAILURE_J3 = 1275
    """Communication to the Wrist motor has been lost or corrupted. Please power cycle the arm and contact your local Quanser support team if the issue continues."""

    QARM_COMM_FAILURE_END_EFFECTOR = 1276
    """Communication to the End Effector board has been lost or corrupted. Please turn off the arm device and check the cable connection."""

    QARM_COMM_FAILURE_GRIPPER = 1277
    """Communication to the Gripper motor has been lost or corrupted. Please turn off the arm device and check the motor's cable connection."""

    QARM_OVERHEATING_J0 = 1278
    """Internal temperature of the Yaw motor has exceeded the configured operating temperature. Please turn off the arm and allow the motor to cool for at least 20 minutes."""

    QARM_OVERHEATING_J1_MASTER = 1279
    """Internal temperature of the Master Shoulder motor has exceeded the configured operating temperature. Please turn off the arm and allow the motor to cool for at least 20 minutes."""

    QARM_OVERHEATING_J1_SLAVE = 1280
    """Internal temperature of the Slave Shoulder motor has exceeded the configured operating temperature. Please turn off the arm and allow the motor to cool for at least 20 minutes."""

    QARM_OVERHEATING_J2 = 1281
    """Internal temperature of the Elbow motor has exceeded the configured operating temperature. Please turn off the arm and allow the motor to cool for at least 20 minutes."""

    QARM_OVERHEATING_J3 = 1282
    """Internal temperature of the Wrist motor has exceeded the configured operating temperature. Please turn off the arm and allow the motor to cool for at least 20 minutes."""

    QARM_OVERHEATING_GRIPPER = 1283
    """Internal temperature of the Gripper motor has exceeded the configured operating temperature. Please turn off the arm and allow the motor to cool for at least 20 minutes."""

    QARM_OVERLOAD_J0 = 1284
    """Detected a persistent load that exceeded the maximum output rating of the Yaw motor. Please turn off the arm and apply a lighter load to the motor."""

    QARM_OVERLOAD_J1_MASTER = 1285
    """Detected a persistent load that exceeded the maximum output rating of the Master Shoulder motor. Please turn off the arm and apply a lighter load to the motor."""

    QARM_OVERLOAD_J1_SLAVE = 1286
    """Detected a persistent load that exceeded the maximum output rating of the Slave Shoulder motor. Please turn off the arm and apply a lighter load to the motor."""

    QARM_OVERLOAD_J2 = 1287
    """Detected a persistent load that exceeded the maximum output rating of the Elbow motor. Please turn off the arm and apply a lighter load to the motor."""

    QARM_OVERLOAD_J3 = 1288
    """Detected a persistent load that exceeded the maximum output rating of the Wrist motor. Please turn off the arm and apply a lighter load to the motor."""

    QARM_OVERLOAD_GRIPPER = 1289
    """Detected a persistent load that exceeded the maximum output rating of the Gripper motor. Please turn off the arm and apply a lighter load to the motor."""

    QARM_MOTOR_ENCODER_J0 = 1290
    """Detected a malfunction of the Yaw motor's encoder. Please contact your local Quanser support team."""

    QARM_MOTOR_ENCODER_J1_MASTER = 1291
    """Detected a malfunction of the Master Shoulder motor's encoder. Please contact your local Quanser support team."""

    QARM_MOTOR_ENCODER_J1_SLAVE = 1292
    """Detected a malfunction of the Slave Shoulder motor's encoder. Please contact your local Quanser support team."""

    QARM_MOTOR_ENCODER_J2 = 1293
    """Detected a malfunction of the Elbow motor's encoder. Please contact your local Quanser support team."""

    QARM_MOTOR_ENCODER_J3 = 1294
    """Detected a malfunction of the Wrist motor's encoder. Please contact your local Quanser support team."""

    QARM_MOTOR_ENCODER_GRIPPER = 1295
    """Detected a malfunction of the Gripper motor's encoder. Please contact your local Quanser support team."""

    QARM_ELECTRICAL_SHOCK_J0 = 1296
    """Detected an electrical shock on the Yaw motor's circuit or insufficient power to operate the motor. Please power cycle the arm and contact your local Quanser support team if the issue continues."""

    QARM_ELECTRICAL_SHOCK_J1_MASTER = 1297
    """Detected an electrical shock on the Master Shoulder motor's circuit or insufficient power to operate the motor. Please power cycle the arm and contact your local Quanser support team if the issue continues."""

    QARM_ELECTRICAL_SHOCK_J1_SLAVE = 1298
    """Detected an electrical shock on the Slave Shoulder motor's circuit or insufficient power to operate the motor. Please power cycle the arm and contact your local Quanser support team if the issue continues."""

    QARM_ELECTRICAL_SHOCK_J2 = 1299
    """Detected an electrical shock on the Elbow motor's circuit or insufficient power to operate the motor. Please power cycle the arm and contact your local Quanser support team if the issue continues."""

    QARM_ELECTRICAL_SHOCK_J3 = 1300
    """Detected an electrical shock on the Wrist motor's circuit or insufficient power to operate the motor. Please power cycle the arm and contact your local Quanser support team if the issue continues."""

    QARM_ELECTRICAL_SHOCK_GRIPPER = 1301
    """Detected an electrical shock on the Gripper motor's circuit or insufficient power to operate the motor. Please power cycle the arm and contact your local Quanser support team if the issue continues."""

    QARM_INPUT_VOLTAGE_J0 = 1302
    """Input voltage of the Yaw motor exceeded the configured operating voltage. Please power cycle the arm and contact your local Quanser support team if the issue continues."""

    QARM_INPUT_VOLTAGE_J1_MASTER = 1303
    """Input voltage of the Master Shoulder motor exceeded the configured operating voltage. Please power cycle the arm and contact your local Quanser support team if the issue continues."""

    QARM_INPUT_VOLTAGE_J1_SLAVE = 1304
    """Input voltage of the Slave Shoulder motor exceeded the configured operating voltage. Please power cycle the arm and contact your local Quanser support team if the issue continues."""

    QARM_INPUT_VOLTAGE_J2 = 1305
    """Input voltage of the Elbow motor exceeded the configured operating voltage. Please power cycle the arm and contact your local Quanser support team if the issue continues."""

    QARM_INPUT_VOLTAGE_J3 = 1306
    """Input voltage of the Wrist motor exceeded the configured operating voltage. Please power cycle the arm and contact your local Quanser support team if the issue continues."""

    QARM_INPUT_VOLTAGE_GRIPPER = 1307
    """Input voltage of the Gripper motor exceeded the configured operating voltage. Please power cycle the arm and contact your local Quanser support team if the issue continues."""

    PDU_SIZE_TOO_SMALL = 1308
    """The protocol data unit (PDU) is too small to handle the data required."""

    CANNOT_NEGOTIATE_PDU = 1309
    """Unable to negotiate protocol data unit (PDU) size."""

    JOB_PENDING = 1310
    """A job is already pending."""

    TOO_MANY_VARIABLES = 1311
    """There are too may items (>20) in multivariable read/write."""

    PDU_TOO_SMALL = 1312
    """The total data exceeds the PDU size."""

    INVALID_PLC_ANSWER = 1313
    """The PLC returned an invalid answer."""

    CANNOT_START_PLC = 1314
    """The PLC could not be started."""

    PLC_ALREADY_RUN = 1315
    """The PLC is already running."""

    CANNOT_STOP_PLC = 1316
    """The PLC canot be stopped."""

    CANNOT_COPY_RAM_TO_ROM = 1317
    """Cannot copy RAM to ROM."""

    CANNOT_COMPRESS = 1318
    """Cannot compress."""

    PLC_ALREADY_STOPPED = 1319
    """The PLC has already been stopped."""

    UPLOAD_FAILED = 1320
    """The upload sequence failed."""

    INVALID_DATA_SIZE_RECEIVED = 1321
    """Invalid data size received."""

    INVALID_BLOCK_TYPE = 1322
    """Invalid block type."""

    INVALID_BLOCK_NUMBER = 1323
    """Invalid block number."""

    INVALID_BLOCK_SIZE = 1324
    """Invalid block size."""

    DOWNLOAD_FAILED = 1325
    """Download sequence failed."""

    BLOCK_INSERT_REFUSED = 1326
    """Block insert refused."""

    BLOCK_DELETE_REFUSED = 1327
    """Block delete refused."""

    INVALID_PASSWORD = 1328
    """Invalid password."""

    NO_PASSWORD_TO_SET_OR_CLEAR = 1329
    """No password to set or clear."""

    FUNCTION_REFUSED = 1330
    """Function refused by CPU (Unknown error)."""

    DESTROYING_OBJECT = 1331
    """Cannot perform the operation. Object is being destroyed."""

    CANNOT_CHANGE_PARAMETER = 1332
    """The parameter cannot be changed at the present time."""

    ILLEGAL_MULTIBYTE_CHARACTER = 1333
    """An illegal multi-byte character was encountered in the stream."""

    ILLEGAL_SURROGATE_CHARACTER = 1334
    """An illegal surrogate character was encountered in the stream."""

    ILLEGAL_CONTROL_CHARACTER = 1335
    """An illegal control character was encountered in the stream."""

    ILLEGAL_NON_CHARACTER = 1336
    """An illegal non-character was encountered in the stream."""

    MISSING_END_TAG_NAME = 1337
    """Missing end tag name e.g. </>."""

    UNEXPECTED_NULL_CHARACTER = 1338
    """Unexpected null character in the input stream."""

    UNEXPECTED_QUESTION_MARK = 1339
    """Unexpected question mark in the input stream."""

    END_BEFORE_TAG = 1340
    """End of input stream encountered before tag name."""

    END_IN_TAG = 1341
    """End of input stream encountered within tag name."""

    INVALID_FIRST_CHARACTER_OF_NAME = 1342
    """Invalid first character of tag name."""

    INVALID_ARRAY_ELEMENT_SEPARATOR = 1343
    """Invalid array element separator when parsing."""

    FAILED_TO_PARSE_INTEGER = 1344
    """Failed to parse an integer value in a string. Format is incorrect."""

    FAILED_TO_PARSE_REAL_NUMBER = 1345
    """Failed to parse a real value in a string. Format is incorrect."""

    MATRIX_NOT_INVERTIBLE = 1346
    """The matrix is not invertible."""

    FORCE_TORQUE_SENSOR_DISCONNECTED = 1347
    """The force/torque sensor appears to be disconnected."""

    END_QUOTE_EXPECTED = 1348
    """The ending quote for a string was expected."""

    TEXT_MATRICES_NOT_SUPPORTED = 1349
    """Text matrices are not currently supported."""

    SPARSE_MATRICES_NOT_SUPPORTED = 1350
    """Sparse matrices are not currently supported."""

    MATRIX_TYPE_NOT_RECOGNIZED = 1351
    """The matrix type of the MAT-file was not recognized. File may be corrupt."""

    VARIABLE_NOT_FOUND = 1352
    """The requested variable could not be found."""

    COMPLEX_NUMBERS_NOT_SUPPORTED = 1353
    """Complex numbers are not currently supported."""

    BYTE_ORDER_NOT_SUPPORTED = 1354
    """The specified byte order is not supported. For example, VAX and Cray byte ordering is not supported."""

    NUMBER_OF_ROWS_TOO_SMALL = 1355
    """The number of rows of the matrix in the file is too small for the total rows implied by the parameters."""

    NUMBER_OF_COLUMNS_TOO_SMALL = 1356
    """The number of columns of the matrix in the file is too small for the total columns implied by the parameters."""

    INVALID_I2C_TIMING_CONFIG = 1357
    """Could not configure the I2C timing registers to the specified clock frequency. Please try using a different I2C clock frequency."""

    IMU_HARDWARE_ERROR = 1358
    """The IMU is not responding properly. Please check the hardware. If necessary, the IMU may be disabled in the card-specific options, in which case the IMU outputs will be zero."""

    CONFLICTING_DIGITAL_FUNCTIONS = 1359
    """The special purpose function (e.g. PWM, Encoder, SPI, I2C, UART) pins are already configured for Digital I/O. Please remove the appropriate Digital I/O channels inside the HIL Initialize block in order to use the specified function. Refer to the device help page for pinout diagrams."""

    ANALOG_OUTPUT_IS_NAN = 1360
    """An attempt was made to write an analog output value that is Not-a-Number (NaN)."""

    PWM_OUTPUT_IS_NAN = 1361
    """An attempt was made to write a PWM output value that is Not-a-Number (NaN)."""

    OTHER_OUTPUT_IS_NAN = 1362
    """An attempt was made to write an other output value that is Not-a-Number (NaN)."""

    DOUBLE_PROPERTY_IS_NAN = 1363
    """An attempt was made to set a double property to a value that is Not-a-Number (NaN)."""

    PWM_FREQUENCY_IS_NAN = 1364
    """An attempt was made to set the PWM frequency to a value that is Not-a-Number (NaN)."""

    PWM_DUTY_CYCLE_IS_NAN = 1365
    """An attempt was made to set the PWM duty cycle to a value that is Not-a-Number (NaN)."""

    PWM_DEADBAND_IS_NAN = 1366
    """An attempt was made to set the PWM deadband to a value that is Not-a-Number (NaN)."""

    CLOCK_FREQUENCY_IS_NAN = 1367
    """An attempt was made to set the clock frequency to a value that is Not-a-Number (NaN)."""

    ENCODER_FILTER_FREQUENCY_IS_NAN = 1368
    """An attempt was made to set the encoder filter frequency to a value that is Not-a-Number (NaN)."""

    TOO_MANY_POINTS = 1369
    """There are too many points specified for the algorithm to process. Resource or computation limits would be exceeded."""

    STACK_OVERFLOW = 1370
    """An internal stack overflowed."""

    STACK_UNDERFLOW = 1371
    """An internal stack underflowed."""

    NO_REFERENCE_SCAN = 1372
    """No reference scan has been set. A scan match cannot be performed."""

    INVALID_SCAN = 1373
    """No valid points were found in the scan."""

    THEME_INCOMPATIBLE_WITH_DECOLORIZATION = 1374
    """The selected colorization theme is incompatible with decolorization. Please choose a different theme."""

    DYNAMIXEL_FAILED_TO_INITIALIZE = 1375
    """The Dynamixel OpenManipulator X failed to initialize.  Make sure the Dynamixel OpenManipulator X is plugged in and powered."""

    DYNAMIXEL_COMMUNICATION_ERROR = 1376
    """Could not communicate with Dynamixel OpenManipulator X."""

    DYNAMIXEL_COULD_NOT_OPEN_DEVICE = 1377
    """Could not open the Dynamixel OpenManipulator X device."""

    DYNAMIXEL_COULD_NOT_START_DEVICE = 1378
    """Could not start the Dynamixel OpenManipulator X control loop."""

    DYNAMIXEL_COULD_NOT_CREATE_READ_GROUP = 1379
    """Could not create a read group for the Dynamixel OpenManipulator X."""

    DYNAMIXEL_COULD_NOT_CREATE_WRITE_GROUP = 1380
    """Could not create a write group for the Dynamixel OpenManipulator X."""

    DYNAMIXEL_COULD_NOT_CHANGE_WRITE_GROUP = 1381
    """Could not change parameters of a write group for the Dynamixel OpenManipulator X."""

    DYNAMIXEL_INVALID_GOAL_PWM = 1382
    """The goal PWM for the Dynamixel OpenManipulator X device is out of range."""

    DYNAMIXEL_INVALID_GOAL_POSITION = 1383
    """The goal Position for the Dynamixel OpenManipulator X device is out of range."""

    DYNAMIXEL_INVALID_GAINS = 1384
    """The position PID or feedforward gains for the Dynamixel OpenManipulator X device is out of range."""

    DYNAMIXEL_INVALID_PROFILE_PARAMS = 1385
    """The profile velocity or acceleration parameters for the Dynamixel OpenManipulator X device is out of range."""

    CANNOT_CONNECT_TO_PLC = 1386
    """It was not possible to connect to the specified PLC. It is likely unreachable."""

    FILE_ALREADY_EXISTS = 1387
    """The file already exists and cannot be overwritten. Delete the file first."""

    TOO_MANY_TELEMETRY = 1388
    """There are too many telemetry bits set in DSHOT commands. When multiple ESC channels share a single telemetry line, only one channel may perform a telemetry request at one time."""

    DIGITAL_EXPIRATION_STATE_NOT_UNCHANGED = 1389
    """This board does not support setting the expiration state of all digital outputs. Set digital outputs which are not controlled by the watchdog to 2 (no change)."""

    VARIABLE_STEP_SOLVERS_NOT_SUPPORTED = 1390
    """Variable-step solvers are not supported by this block."""

    INVALID_NEWLINE_SEPARATED_STRING = 1391
    """The initialization string is invalid. A single string containing items separated by newlines (\n) is expected."""

    SENSOR_TYPE_NOT_SUPPORTED = 1392
    """The specified sensor type is not currently supported."""

    MISSING_SPINNAKER = 1393
    """The Spinnaker SDK does not appear to be installed or is not in the PATH. See the help for the GenICam capture block for the installation requirements. Note that a reboot may be required after installing the SDK."""

    GENICAM_CANNOT_INITIALIZE_CAMERA = 1394
    """An error occurred while attempting to initialize the GenICam camera."""

    GENICAM_CANNOT_GET_FEATURES = 1395
    """An error occurred while attempting to get features from the GenICam camera."""

    GENICAM_CANNOT_READ_NODE = 1396
    """An error occurred while attempting to read nodes from the GenICam camera."""

    GENICAM_CANNOT_WRITE_NODE = 1397
    """An error occurred while attempting to write nodes to the GenICam camera."""

    GENICAM_CANNOT_FIND_CAMERA = 1398
    """The requested GenICam camera cannot be found."""

    GENICAM_CANNOT_GET_CAMERA_NODE = 1399
    """The requested GenICam camera nodemap cannot be acquired."""

    GENICAM_CANNOT_SET_IMAGE_SIZE = 1400
    """Cannot set GenICam camera image to the desired size."""

    GENICAM_CANNOT_SET_PIXEL_FORMAT = 1401
    """Cannot set GenICam camera image to the desired pixel format."""

    GENICAM_CANNOT_SET_ANALOG_CONTROL = 1402
    """Cannot set GenICam camera analog controls to desired value."""

    GENICAM_CANNOT_SET_ACQUISITION_NODE = 1403
    """Cannot set GenICam camera acquisition mode."""

    GENICAM_CANNOT_GRAB_IMAGE = 1404
    """An error occurred while attempting to grab an image using the GenICam camera."""

    GENICAM_GRAB_IMAGE_TIMEOUT = 1405
    """A timeout occurred while attempting to grab an image using the GenICam camera."""

    GENICAM_CANNOT_CLOSE = 1406
    """An error occurred while attempting to close the GenICam camera."""

    CONTINUOUS_THRESHOLD_EXCEEDS_PEEK = 1407
    """The specified continuous threshold exceeds the peak threshold."""

    PEER_CLOSED_CONNECTION = 1408
    """The connection was closed by the peer. The stream should be closed."""

