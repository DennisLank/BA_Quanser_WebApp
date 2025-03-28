import os

from cffi import FFI

from quanser.common import ErrorCode, Timeout
from quanser.common.types import ffi as ffi_types
from quanser.communications import PollFlag, BooleanProperty, StreamError

# region Setup


ffi = FFI()
ffi.include(ffi_types)
ffi.cdef("""
    /* Type Definitions */
    
    typedef char                t_boolean;
    typedef signed char         t_byte;
    typedef signed short        t_short;
    typedef unsigned short      t_ushort;
    typedef signed int          t_int;
    typedef unsigned int        t_uint;
    typedef signed long long    t_long;
    typedef float               t_single;
    typedef double              t_double;

    typedef t_short             t_int16;
    typedef t_ushort            t_uint16;
    typedef t_int               t_int32;
    typedef t_uint              t_uint32;
    typedef t_int               t_error;
        
    typedef struct tag_stream * t_stream;
    
    typedef enum tag_stream_byte_order
    {
        STREAM_BYTE_ORDER_NATIVE_ENDIAN,
        STREAM_BYTE_ORDER_LITTLE_ENDIAN,
        STREAM_BYTE_ORDER_BIG_ENDIAN
    } t_stream_byte_order;

    typedef enum tag_qcomm_boolean_property
    {
        QCOMM_PROPERTY_IS_READ_ONLY,
        QCOMM_PROPERTY_IS_WRITE_ONLY,
        QCOMM_PROPERTY_IS_EXCLUSIVE,
        QCOMM_PROPERTY_NO_READ_AHEAD,
    
        QCOMM_PROPERTY_SERIAL_DTR,
        QCOMM_PROPERTY_SERIAL_RTS,
        QCOMM_PROPERTY_SERIAL_DSR,
        QCOMM_PROPERTY_SERIAL_CTS
    } t_qcomm_boolean_property;
    
    typedef enum tag_stream_boolean_property
    {
        STREAM_PROPERTY_IS_READ_ONLY  = QCOMM_PROPERTY_IS_READ_ONLY,
        STREAM_PROPERTY_IS_WRITE_ONLY = QCOMM_PROPERTY_IS_WRITE_ONLY,
        STREAM_PROPERTY_IS_EXCLUSIVE  = QCOMM_PROPERTY_IS_EXCLUSIVE,
        STREAM_PROPERTY_NO_READ_AHEAD = QCOMM_PROPERTY_NO_READ_AHEAD,
    
        STREAM_PROPERTY_SERIAL_DTR    = QCOMM_PROPERTY_SERIAL_DTR,
        STREAM_PROPERTY_SERIAL_RTS    = QCOMM_PROPERTY_SERIAL_RTS,
        STREAM_PROPERTY_SERIAL_DSR    = QCOMM_PROPERTY_SERIAL_DSR,
        STREAM_PROPERTY_SERIAL_CTS    = QCOMM_PROPERTY_SERIAL_CTS
    } t_stream_boolean_property;

    typedef struct tag_stream_poke_state
    {
        t_int bytes_poked;  /* number of bytes poked so far */
    } t_stream_poke_state;

    typedef struct tag_stream_peek_state
    {
        t_int bytes_peeked; /* number of bytes peeked so far */
    } t_stream_peek_state;

    /* Configuration Functions */
            
    t_error stream_listen(const char * uri, t_boolean non_blocking, t_stream * server_stream);

    t_error stream_connect(const char * uri, t_boolean non_blocking,
                           t_int send_buffer_size, t_int receive_buffer_size, 
                           t_stream * client_stream);

    t_error stream_accept(t_stream server_stream,
                          t_int send_buffer_size, t_int receive_buffer_size,
                          t_stream * client_stream);

    t_int stream_poll(t_stream stream, const t_timeout * timeout, t_uint flags);

    t_error stream_shutdown(t_stream stream);

    t_error stream_close(t_stream stream);

    t_error stream_close_all(void);
    
    t_error stream_get_swap_bytes(t_stream stream);
    t_error stream_set_swap_bytes(t_stream stream, t_boolean swap);
    t_error stream_set_byte_order(t_stream stream, t_stream_byte_order byte_order);

    t_error stream_get_boolean_property(t_stream stream,
                                        const t_stream_boolean_property properties[], t_uint num_properties,
                                        t_boolean buffer[]);
    
    t_error stream_set_boolean_property(t_stream stream,
                                        const t_stream_boolean_property properties[], t_uint num_properties,
                                        const t_boolean buffer[]);
    
    t_int stream_send(t_stream stream, const void * buffer, t_int buffer_size);
    t_int stream_send_byte(t_stream stream, t_byte value);
    t_int stream_send_bytes(t_stream stream, const t_byte* elements, t_uint num_elements);
    t_int stream_send_byte_array(t_stream stream, const t_byte* elements, t_uint num_elements);
    t_int stream_send_short(t_stream stream, t_short value);
    t_int stream_send_shorts(t_stream stream, const t_short* elements, t_uint num_elements);
    t_int stream_send_short_array(t_stream stream, const t_short* elements, t_uint num_elements);
    t_int stream_send_int(t_stream stream, t_int value);
    t_int stream_send_ints(t_stream stream, const t_int* elements, t_uint num_elements);
    t_int stream_send_int_array(t_stream stream, const t_int* elements, t_uint num_elements);
    t_int stream_send_long(t_stream stream, t_long value);
    t_int stream_send_longs(t_stream stream, const t_long* elements, t_uint num_elements);
    t_int stream_send_long_array(t_stream stream, const t_long* elements, t_uint num_elements);
    t_int stream_send_single(t_stream stream, t_single value);
    t_int stream_send_singles(t_stream stream, const t_single* elements, t_uint num_elements);
    t_int stream_send_single_array(t_stream stream, const t_single* elements, t_uint num_elements);
    t_int stream_send_double(t_stream stream, t_double value);
    t_int stream_send_doubles(t_stream stream, const t_double* elements, t_uint num_elements);
    t_int stream_send_double_array(t_stream stream, const t_double* elements, t_uint num_elements);
    
    t_int stream_receive(t_stream stream, void * buffer, t_int buffer_size);
    t_int stream_receive_bytes(t_stream stream, t_byte* elements, t_int num_elements);
    t_int stream_receive_byte_array(t_stream stream, t_byte* elements, t_int num_elements);
    t_int stream_receive_shorts(t_stream stream, t_short* elements, t_int num_elements);
    t_int stream_receive_short_array(t_stream stream, t_short* elements, t_int num_elements);
    t_int stream_receive_ints(t_stream stream, t_int* elements, t_int num_elements);
    t_int stream_receive_int_array(t_stream stream, t_int* elements, t_int num_elements);
    t_int stream_receive_longs(t_stream stream, t_long* elements, t_int num_elements);
    t_int stream_receive_long_array(t_stream stream, t_long* elements, t_int num_elements);
    t_int stream_receive_singles(t_stream stream, t_single* elements, t_int num_elements);
    t_int stream_receive_single_array(t_stream stream, t_single* elements, t_int num_elements);
    t_int stream_receive_doubles(t_stream stream, t_double* elements, t_int num_elements);
    t_int stream_receive_double_array(t_stream stream, t_double* elements, t_int num_elements);

    t_error stream_flush(t_stream stream);

    t_error stream_poke_begin(t_stream stream, t_stream_poke_state* state);
    t_int stream_poke_byte(t_stream stream, t_stream_poke_state* state, t_byte value);
    t_int stream_poke_byte_array(t_stream stream, t_stream_poke_state* state, const t_byte* elements, t_uint num_elements);
    t_int stream_poke_short(t_stream stream, t_stream_poke_state* state, t_short value);
    t_int stream_poke_short_array(t_stream stream, t_stream_poke_state* state, const t_short* elements, t_uint num_elements);
    t_int stream_poke_int(t_stream stream, t_stream_poke_state* state, t_int value);
    t_int stream_poke_int_array(t_stream stream, t_stream_poke_state* state, const t_int* elements, t_uint num_elements);
    t_int stream_poke_long(t_stream stream, t_stream_poke_state* state, t_long value);
    t_int stream_poke_long_array(t_stream stream, t_stream_poke_state* state, const t_long* elements, t_uint num_elements);
    t_int stream_poke_single(t_stream stream, t_stream_poke_state* state, t_single value);
    t_int stream_poke_single_array(t_stream stream, t_stream_poke_state* state, const t_single* elements, t_uint num_elements);
    t_int stream_poke_double(t_stream stream, t_stream_poke_state* state, t_double value);
    t_int stream_poke_double_array(t_stream stream, t_stream_poke_state* state, const t_double* elements, t_uint num_elements);
    t_error stream_poke_end(t_stream stream, t_stream_poke_state* state, t_error status);

    t_error stream_peek_begin(t_stream stream, t_stream_peek_state* state, t_int prefetch);
    t_int stream_peek_byte(t_stream stream, t_stream_peek_state* state, t_byte* value);
    t_int stream_peek_byte_array(t_stream stream, t_stream_peek_state* state, t_byte* elements, t_int num_elements);
    t_int stream_peek_short(t_stream stream, t_stream_peek_state* state, t_short* value);
    t_int stream_peek_short_array(t_stream stream, t_stream_peek_state* state, t_short* elements, t_int num_elements);
    t_int stream_peek_int(t_stream stream, t_stream_peek_state* state, t_int* value);
    t_int stream_peek_int_array(t_stream stream, t_stream_peek_state* state, t_int* elements, t_int num_elements);
    t_int stream_peek_long(t_stream stream, t_stream_peek_state* state, t_long* value);
    t_int stream_peek_long_array(t_stream stream, t_stream_peek_state* state, t_long* elements, t_int num_elements);
    t_int stream_peek_single(t_stream stream, t_stream_peek_state* state, t_single* value);
    t_int stream_peek_single_array(t_stream stream, t_stream_peek_state* state, t_single* elements, t_int num_elements);
    t_int stream_peek_double(t_stream stream, t_stream_peek_state* state, t_double* value);
    t_int stream_peek_double_array(t_stream stream, t_stream_peek_state* state, t_double* elements, t_int num_elements);
    t_error stream_peek_end(t_stream stream, t_stream_peek_state* state, t_error status);

""")

communications_lib = ffi.dlopen("quanser_communications")

# endregion

# region Constants

_BOOLEAN_ARRAY = "t_boolean[]"
_CHAR_ARRAY = "char[]"
_UINT_ARRAY = "t_uint[]"
_UINT32_ARRAY = "t_uint32[]"
_INT_ARRAY = "t_int[]"
_INT32_ARRAY = "t_int32[]"
_DOUBLE_ARRAY = "t_double[]"

_BOOLEAN_PROPERTY_ARRAY = "t_stream_boolean_property[]"

# endregion

# region Stream Classes


class Stream:
    """A Python wrapper for the Quanser Stream API.

    Example
    -------
    >>> from quanser.communications import Stream
    >>> stream = Stream()

    """

    # region Life Cycle

    def __init__(self):
        self._stream = None

    # endregion

    # region Implementation

    def connect(self, uri, non_blocking=False, send_buffer_size=1460, receive_buffer_size=1460):
        """Connects to a listening stream referenced by the given URI. The URI specifies the protocol, address, port,
        and options associated with the stream. The Stream API uses the protocol to load a protocol-specific driver.

        URI examples::

            tcpip://remotehost:17000                        - connect to remote host on port 17000 using TCP/IP
            shmem://mymemory:1?bufsize=8192                 - connect via an 8K shared memory buffer
            pipe:mypipe?bufsize=4096                        - connect via a 4K named pipe
            i2c://localhost:0?baud='100000';address='0x48'  - connect via I2C at a baud rate of 100000

        If the non_blocking flag is set to ``False``, then this function will block until the connection is made.
        If the non_blocking flag is set to ``True``, then this function will not block. If the connection is made
        then ``True`` (1) is returned. If the connection cannot be completed immediately, then ``False`` (0) is 
        returned. In this case, the connection may be completed using `poll` with the ``PollFlag.CONNECT`` flag. 
        If an error occurs then an exception is raised.

        Parameters
        ----------
        uri : string
            A URI indicating the listening stream to which to connect.

        non_blocking : boolean
            Set to ``True`` (1) to make the client connection non-blocking.

        send_buffer_size : int    
            The size of the buffer to use for sending data over the stream, in bytes
    
        receive_buffer_size : int
            The size of the buffer to use for receiving data over the stream, in bytes

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Returns
        -------
        bool
            ``True`` if connected; ``False`` if connection in progress.

        Example
        -------
        >>> from quanser.communications import Stream
        >>> stream = Stream()
        >>> try:
        >>>    is_connected = stream.connect("tcpip://localhost:5039", False, 64, 64)
        >>>    # ...
        ...    
        >>>    stream.shutdown()
        >>>    stream.close()
        >>> except:
        >>>    # An error occurred

        """
        if self._stream is not None:
            self.close()

        client_stream = ffi.new("t_stream *")
        
        result = communications_lib.stream_connect(uri.encode('utf-8'),
                                                   b'\x01' if non_blocking else b'\x00',
                                                   send_buffer_size,
                                                   receive_buffer_size,
                                                   client_stream)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        self._stream = client_stream[0]

        return result != -ErrorCode.WOULD_BLOCK

    def listen(self, uri, non_blocking=False):
        """Establishes a server stream which listens on the given URI. The URI specifies the protocol, address, port and
        options associated with the server stream. The Stream API uses the protocol to load a protocol-specific driver.
        For example:

        tcpip://localhost:17000             - listen on port 17000 using TCP/IP
        shmem://mymemory:1?bufsize=8192     - listen via shared memory buffer. Use 8K buffers by default.
        pipe:mypipe?bufsize=4096            - listen via a named pipe. Use 4K buffers for the pipe.

        Parameters
        ----------
        uri : string
            A URI indicating the stream on which to listen.

        non_blocking : bool
            Set to ``True`` (1) to prevent `accept` calls from blocking.

        Raises
        ------
        StreamError
            On non-zero return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------
        >>> from quanser.communications import Stream
        >>> stream = Stream()
        >>> stream.listen("tcpip://localhost:5039", False)
        >>> # ...
        ...
        >>> stream.shutdown()
        >>> stream.close()
        
        """
        server_stream = ffi.new("t_stream *")

        result = communications_lib.stream_listen(uri.encode('utf-8'),
                                                  b'\x01' if non_blocking else b'\x00',
                                                  server_stream)

        if result < 0:
            raise StreamError(result)

        self._stream = server_stream[0]

    def accept(self, send_buffer_size = 1460, receive_buffer_size = 1460):
        """Accepts a connection to a listening communication stream by a client. The client connects using
        `connect`.

        If `listen` was called with `non_blocking` set to ``False``, then this call will block until a client connects.
        The client stream returned will also be a blocking stream.

        If `listen` was called with non_blocking set to ``True``, then this call will not block. If there is no pending
        client connection, then it will raise `-ErrorCode.WOULD_BLOCK`. The `poll` function may be used with
        ``PollFlag.ACCEPT`` to determine when a client connection is pending. In this case, the client stream returned
        will also be a non-blocking stream.

        On POSIX systems this function should be interruptible by a signal so that arrival of a signal will cause a
        ``-ErrorCode.INTERRUPTED`` error to be returned.

        Parameters
        ----------
        send_buffer_size : int
            The size of the buffer to use for sending data over the stream, in bytes

        receive_buffer_size : int
            The size of the buffer to use for receiving data over the stream, in bytes

        Raises
        ------
        StreamError
            On non-zero return code. A suitable error message may be retrieved using `get_error_message`.    

        Returns
        -------
        Stream or None
            The client stream or ``None`` if there is no client stream.

        Example
        -------
        >>> from quanser.communications import Stream
        >>> uri = "tcpip://localhost:5000"
        >>> send_buffer_size = 64
        >>> receive_buffer_size = 64
        >>> server_stream = Stream()
        >>> client_stream = Stream()
        >>> server_stream.listen(uri, False)
        >>> client_stream.connect(uri, False, send_buffer_size, receive_buffer_size)
        >>> client_connection = server_stream.accept(send_buffer_size, receive_buffer_size)
        >>> # ...
        ...
        >>> client_connection.shutdown()
        >>> client_stream.shutdown()
        >>> client_connection.close()
        >>> client_stream.close()
        >>> server_stream.close()

        """
        client_stream = Stream()

        _client_stream = ffi.new("t_stream *")

        result = communications_lib.stream_accept(self._stream if self._stream is not None else ffi.NULL,
                                                  send_buffer_size,
                                                  receive_buffer_size,
                                                  _client_stream)

        if result == -ErrorCode.WOULD_BLOCK:
            return None

        if result < 0:
            raise StreamError(result)

        client_stream._stream = _client_stream[0]
        return client_stream

    def poll(self, timeout, flags):
        """Polls the stream to determine whether it is possible to send or receive or accept a connection without
        blocking. The flags argument determines the conditions for which to check. The return value indicates the
        conditions which occurred. This function returns after the given timeout with a value of 0 if none of the
        conditions occurs. If an error occurs, then it returns a negative error code. The function will return before
        the timeout if at least one of the conditions occurs prior to the timeout.

        Note that this function may return zero even if the timeout has not occurred, even when the timeout is infinite.
        This special case occurs when the `shutdown` method has been called on the stream. Once the stream is shut down,
        the timeout may be limited to the close timeout associated with the stream (for shmem, for instance). Hence,
        the stream may timeout in this  case and return 0 before the specified timeout, even if the timeout is infinite.

        Parameters
        ----------
        timeout : Timeout
            A timeout structure, or None for an infinite timeout.
        
        flags : int
            A bit mask indicating the conditions for which to check. Valid flags are:
            ``PollFlag.RECEIVE`` = on a listening stream, check for connections pending from clients. On a client
            stream, check whether there is any data available to receive.
            ``PollFlag.SEND`` = not valid on a listening stream. On a client stream, check whether there is space in
            the stream buffer to store any data.
            ``PollFlag.FLUSH` = not valid on a listening stream. On a client stream, check whether it is possible to
            flush any more data without blocking.
            ``PollFlag.ACCEPT`` = not valid on a client stream. On a listening stream, check whether there is a pending
            client connection.
            ``PollFlag.CONNECT`` = not valid on a listening stream. On a client stream, check whether the connection
            has completed.

        Returns
        -------
        int
            A bit mask containing the conditions which were satisfied. It has the same definition as the flags argument.
            If none of the specified conditions occurs before the timeout, then 0 is returned.

        Raises
        ------
        StreamError
            On non-zero return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------
        Poll a stream

        >>> from quanser.common import Timeout
        >>> from quanser.communications import Stream, PollFlag
        >>> timeout = Timeout(3)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   result = stream.poll(timeout, PollFlag.SEND | PollFlag.RECEIVE)
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        if timeout is not None:
            _timeout = timeout._timeout
        else:
            _timeout = ffi.NULL

        result = communications_lib.stream_poll(self._stream if self._stream is not None else ffi.NULL, _timeout, flags)
        if result < 0:
            raise StreamError(result)

        return result

    def shutdown(self):
        """Shuts down send and/or receives in preparation for closing the stream. Note that close still
        needs to be called to free resources.

        Raises
        ------
        StreamError
            On non-zero return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------
        >>> from quanser.communications import Stream
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_shutdown(self._stream if self._stream is not None else ffi.NULL)

        if result < 0:
            raise StreamError(result)

    def close(self):
        """Closes the stream. All resources associated with the stream are freed.

        Raises
        ------
        StreamError
            On non-zero return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------
        >>> from quanser.communications import Stream
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_close(self._stream if self._stream is not None else ffi.NULL)

        if result < 0:
            raise StreamError(result)

        self._stream = None

    @staticmethod
    def close_all():
        """Closes all streams established using stream_listen, stream_connect or stream_accept.

        Raises
        ------
        StreamError
            On non-zero return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------
        >>> from quanser.communications import Stream
        >>> uri = "tcpip://localhost:5000"
        >>> server = Stream()
        >>> client = Stream()
        >>> server.listen(uri, False)
        >>> client.connect(uri, False, 64, 64)
        >>> # ...
        ...
        >>> Stream.close_all()

        """
        result = communications_lib.stream_close_all()

        if result < 0:
            raise StreamError(result)

    def get_swap_bytes(self):
        """Returns whether the functions that send and receive shorts,
        t_utf16_chars, t_utf32_chars, integers, longs, singles, doubles or 
        arrays of them, swap the bytes in the individual values.

        Byte swapping is only necessary when communicating between processors that use
        a different endianness.  For example, Intel processors are little endian (LSB first)
        while Motorola processors tend to be big endian (MSB first). By default, no
        byte swapping takes place. Whether byte swapping is necessary may be determined
        simply by sending 0x1234 as a short and seeing if it arrives as the same number
        or 0x3421.

        This function returns ``True`` (1) if byte swapping is enabled and ``False`` (0) otherwise. 
        If the stream is invalid an exception is raised.

        Returns
        -------
        state : boolean
            Returns ``True`` (1) if byte swapping is enabled and ``False`` (0) otherwise.

        Raises
        ------
        StreamError
            On non-zero return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------
        Determine if the given stream swaps bytes.

        >>> from array import array
        >>> from quanser.communications import Stream
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   swapping = stream.get_swap_bytes()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_get_swap_bytes(self._stream if self._stream is not None else ffi.NULL)
        if result < 0:
            raise StreamError(result)

        return (result > 0)

    def set_swap_bytes(self, swap):
        """Configures whether the functions that send and receive shorts,
        t_utf16_chars, t_utf32_chars, integers, longs, singles, doubles or 
        arrays of them, should swap the bytes in the individual values.

        Byte swapping is only necessary when communicating between processors that use
        a different endianness.  For example, Intel processors are little endian (LSB first)
        while Motorola processors tend to be big endian (MSB first). By default, no
        byte swapping takes place. Whether byte swapping is necessary may be determined
        simply by sending 0x1234 as a short and seeing if it arrives as the same number
        or 0x3421.

        Pass ``True`` (1) to enable byte swapping and ``False`` (0) to disable it. 
        If the stream is invalid an exception is raised.

        Note that `set_swap_bytes` and `set_byte_order` override each other.
        The function most recently called will determine whether byte swapping occurs.

        Parameters
        ----------
        state : boolean
            Set to ``True`` (1) to enable byte swapping, and ``False`` (0) to disable byte swapping.

        Returns
        -------
        old_state : boolean
            Returns the previous byte swapping state. A return value of ``False`` (0) indicates 
            that byte swapping was not enabled prior to the call, and a return value of ``True`` (1)
            indicates that byte swapping was enabled prior to the call.

        Raises
        ------
        StreamError
            On non-zero return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------
        Configure the given stream to swap bytes in multi-byte data types.

        >>> from array import array
        >>> from quanser.communications import Stream
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   stream.set_swap_bytes(True)
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_set_swap_bytes(self._stream if self._stream is not None else ffi.NULL, 
                                                          b'\x01' if swap else b'\x00')
        if result < 0:
            raise StreamError(result)

        return (result > 0)

    def set_byte_order(self, order):
        """Configures whether the functions that send and receive shorts,
        t_utf16_chars, t_utf32_chars, integers, longs, singles, doubles or 
        arrays of them, should swap the bytes in the individual values.

        Byte swapping is only necessary when communicating between processors that use
        a different endianness. For example, Intel processors are little endian (LSB first)
        while Motorola processors tend to be big endian (MSB first). By default, no
        byte swapping takes place. This function compares the byte order given to the
        native byte ordering of the platform running the code and tells the stream to
        swap bytes if the byte orders are different.

        Note that `set_swap_bytes` and `set_byte_order` override each other.
        The function most recently called will determine whether byte swapping occurs.

        Parameters
        ----------
        order : ByteOrder
            The byte order to use from the `ByteOrder` enumeration.

        Returns
        -------
        result : int
            Returns 0 on success. Otherwise an exception is raised.

        Raises
        ------
        StreamError
            On non-zero return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------
        Configure the given stream to use little-endian byte order for multi-byte data types.

        >>> from array import array
        >>> from quanser.communications import Stream, ByteOrder
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   stream.set_byte_order(ByteOrder.LITTLE_ENDIAN)
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_set_byte_order(self._stream if self._stream is not None else ffi.NULL, order)
        if result < 0:
            raise StreamError(result)

        return result

    def get_boolean_property(self, properties, num_properties, buffer):
        """Returns the value of the specified boolean properties. This function is optional in a driver. If the driver
        does not provide it, then this function returns ``-ErrorCode.NOT_SUPPORTED``.

        Parameters
        ----------
        properties : array_like
            An array containing the properties to query.
        num_properties : int
            The number of properties in the `properties` array.
        buffer : array_like
            An array into which the property values are stored. It must have the same number of elements as the
            properties array.

        Raises
        ------
        StreamError
            On non-zero return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------
        Determine if the given stream is in exclusive write-only mode.

        >>> from array import array
        >>> from quanser.communications import Stream, BooleanProperty
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   properties = array('i', [BooleanProperty.IS_EXCLUSIVE, BooleanProperty.IS_WRITE_ONLY])
        >>>   num_properties = len(properties)
        >>>   buffer = array('b', [0] * num_properties)
        >>>   stream.get_boolean_property(properties, num_properties, buffer)
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_get_boolean_property(self._stream if self._stream is not None else ffi.NULL,
                                                                ffi.from_buffer(_BOOLEAN_PROPERTY_ARRAY, properties) if properties is not None else ffi.NULL,
                                                                num_properties,
                                                                ffi.from_buffer(_BOOLEAN_ARRAY, buffer) if buffer is not None else ffi.NULL)
        if result < 0:
            raise StreamError(result)

    def set_boolean_property(self, properties, num_properties, buffer):
        """Sets the value of the specified boolean properties. This function is optional in a driver. If the driver
        does not provide it, then this function returns ``-ErrorCode.NOT_SUPPORTED``.

        Parameters
        ----------
        properties : array_like
            An array containing the properties to query.
        num_properties : int
            The number of properties in the `properties` array.
        buffer : array_like
            An array into which the property values are stored. It must have the same number of elements as the
            properties array.

        Raises
        ------
        StreamError
            On non-zero return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------
        Set the stream to exclusive write-only mode.

        >>> from array import array
        >>> from quanser.communications import Stream, BooleanProperty
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   properties = array('i', [BooleanProperty.IS_EXCLUSIVE, BooleanProperty.IS_WRITE_ONLY])
        >>>   num_properties = len(properties)
        >>>   buffer = array('b', [0] * num_properties)
        >>>   stream.set_boolean_property(properties, num_properties, buffer)
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_set_boolean_property(self._stream if self._stream is not None else ffi.NULL,
                                                                ffi.from_buffer(_BOOLEAN_PROPERTY_ARRAY, properties) if properties is not None else ffi.NULL,
                                                                num_properties,
                                                                ffi.from_buffer(_BOOLEAN_ARRAY, buffer) if buffer is not None else ffi.NULL)

        if result < 0:
            raise StreamError(result)

    def send(self, buffer, buffer_size):
        """Writes data to the stream buffer. It attempts to store `buffer_size` bytes in the stream buffer. If there is
        enough room available in the stream buffer, then it stores the data in the buffer and returns immediately. The
        data is not written to the actual communication channel until the stream is flushed using `flush` or there is no
        more room available in the stream buffer. If an error occurs, then an exception is raised. If the connection is
        closed, it is considered an error condition.

        If `listen` or `connect` was called with the non-blocking flag set to ``False``, then this function may block
        attempting to flush the stream buffer. All the data will be consumed and the total number of bytes sent is
        returned. Some of the data may remain in the stream buffer and not be sent until the next time `flush` is called
        or there is no more room available in the stream buffer. If an error occurs, then an exception is raised and the
        stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True``, then this function does not
        block. It returns the number of bytes sent successfully, which will be between 1 and `buffer_size` (unless
        `buffer_size` is zero). If no bytes could be sent without blocking, then the function returns the error code
        ``-ErrorCode.WOULD_BLOCK``. If an error occurs, then an exception is raised and the stream should be closed.

        This function does not support two threads calling `send` or `flush` at the same time; however, `send` or
        `flush` may be called by another thread at the same time as `receive`.

        The semantics of this function are comparable to the BSD `send()` socket function.

        Parameters
        ----------
        buffer : array_like
            A buffer of at least `buffer_size` bytes containing the data to be sent.
        buffer_size : int
            The number of bytes to send from the buffer.

        Returns
        -------
        int
            The number of bytes sent, which may be less than `buffer_size` bytes for non-blocking streams. If an error
            occurs, then an exception is raised. A value of zero is only returned if `buffer_size` is zero.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------

        Send a text message immediately by writing it to the stream and then flushing the buffer.

        >>> from quanser.communications import Stream
        >>> message = "Hello".encode()
        >>> num_bytes = len(message)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   bytes_written = stream.send(message, num_bytes)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        Send 2 doubles immediately by writing them to the stream and then flushing the buffer.

        >>> import struct
        >>> from quanser.communications import Stream
        >>> data = bytearray(struct.pack("!dd", 1.2, 3.4))
        >>> num_bytes = len(data)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   bytes_written = stream.send(data, num_bytes)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_send(self._stream if self._stream is not None else ffi.NULL,
                                                ffi.from_buffer(buffer) if buffer is not None else ffi.NULL,
                                                buffer_size)

        if result < 0 and result != ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def send_byte(self, data):
        """Writes a single byte to the stream buffer. It is has the
        same semantics as the `send` function, except that it only sends
        a single byte.

        The semantics of this function are comparable to the BSD `send()` socket function.

        Parameters
        ----------
        data : char
            The byte to send.

        Returns
        -------
        int
            The number of bytes sent, which will always be 1 unless no data was sent in non-blocking I/O. If an error
            occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------

        Send one byte immediately by writing it to the stream and then flushing the buffer.

        >>> from quanser.communications import Stream
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   bytes_written = stream.send_byte(123)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_send_byte(self._stream if self._stream is not None else ffi.NULL,
                                                     data)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def send_bytes(self, elements, num_elements):
        """This function writes an array of bytes to the stream buffer. It is has the
        same semantics as the `send` function.

        Unlike the `send_byte_array` function, this function does not require that the
        stream send buffer be at least `num_elements` bytes in length. Hence, it
        allows smaller stream buffers to be used.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` bytes containing the data to be sent.
        num_elements : int
            The number of bytes to send from the buffer.

        Returns
        -------
        int
            The number of bytes sent, which may be less than `num_elements` bytes for non-blocking streams. If an error
            occurs, then an exception is raised. A value of zero is only returned if `num_elements` is zero.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------

        Send a text message immediately by writing it to the stream and then flushing the buffer.

        >>> from quanser.communications import Stream
        >>> message = "Hello".encode()
        >>> num_bytes = len(message)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   bytes_written = stream.send_bytes(message, num_bytes)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        Send 4 bytes immediately by writing them to the stream and then flushing the buffer.

        >>> import struct
        >>> from quanser.communications import Stream
        >>> elements = array("b", [1, 2, 3, 4])
        >>> num_elements = len(data)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   elements_written = stream.send_bytes(elements, num_elements)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_send_bytes(self._stream if self._stream is not None else ffi.NULL,
                                                      ffi.from_buffer(elements) if elements is not None else ffi.NULL,
                                                      num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def send_byte_array(self, elements, num_elements):
        """Writes an array of bytes to the stream buffer. It attempts
        to store the bytes in the stream buffer. It differs from the `send_bytes`
        function in that it treats the entire array as an atomic unit. It either writes
        all of the array or none of it. If there is enough room available in the stream
        buffer then it stores the data in the buffer and returns immediately. The data
        is not written to the actual communication channel until the stream is flushed
        using `flush` or there is no more room available in the stream buffer. If
        an error occurs, then it throws an exception. If the connection is
        closed it is considered an error condition.

        Unlike the `send_bytes` function, the size of the stream send buffer 
        must be at least as large as the number of bytes being sent.

        If `listen` or `connect` was called with the non-blocking flag set to false (0),
        then this function may block attempting to flush the stream buffer. All the data will be
        consumed and 1 is returned. Some of the data may remain in the stream buffer and not be
        sent until the next time `flush` is called or there is no more room available in
        the stream buffer. If an error occurs then an exception is raised and the stream
        should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to true (1),
        then this function does not block. It returns 1 if the array is sent successfully.
        If the array could not be sent without blocking, then it returns the
        error code ``-ErrorCode.WOULD_BLOCK``. If an error occurs then an exception is raised
        and the stream should be closed.

        This function does not support two threads sending or flushing data at the same time.
        However, data may be sent or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` bytes containing the data to be sent.
        num_elements : int
            The number of bytes to send from the buffer.

        Returns
        -------
        int
            Returns 1 on success. If an error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------

        Send 4 bytes atomically by writing them to the stream and then flushing the buffer.

        >>> import struct
        >>> from quanser.communications import Stream
        >>> elements = array("b", [1, 2, 3, 4])
        >>> num_elements = len(data)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   bytes_written = stream.send_byte_array(elements, num_elements)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_send_byte_array(self._stream if self._stream is not None else ffi.NULL,
                                                           ffi.from_buffer(elements) if elements is not None else ffi.NULL,
                                                           num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def send_short(self, data):
        """Writes a 16-bit short integer to the stream buffer. It attempts to
        store the short integer in the stream buffer. If there is enough room available in the
        stream buffer then it stores the data in the buffer and returns immediately. The
        data is not written to the actual communication channel until the stream is flushed
        using `flush` or there is no more room available in the stream buffer. If an
        error occurs, then it returns a negative error code.

        If the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within the short integer when it
        is sent.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer. All the data will be
        consumed and the total number of short integers sent is returned (1). Some of the data may
        remain in the stream buffer and not be sent until the next time `flush` is called or
        there is no more room available in the stream buffer. If an error occurs then an
        exception is raised and the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns the number of short integers sent successfully,
        which will be 1. If the short integer could not be sent without blocking, then
        ``-ErrorCode.WOULD_BLOCK`` is returned. If an error occurs then an exception is raised
        and the stream should be closed.

        This function does not support two threads sending or flushing data at the same time.
        However, data may be sent or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        data : short
            The short to send.

        Returns
        -------
        int
            The number of 16-bit integers sent, which will always be 1 unless no data was sent in non-blocking I/O. If an error
            occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------

        Send one 16-bit integer immediately by writing it to the stream and then flushing the buffer.

        >>> from quanser.communications import Stream
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   shorts_written = stream.send_short(123)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_send_short(self._stream if self._stream is not None else ffi.NULL,
                                                      data)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def send_shorts(self, elements, num_elements):
        """This function writes an array of 16-bit short integers to the stream buffer. It
        attempts to store the short integers in the stream buffer. If there is enough
        room available in the stream buffer then it stores the data in the buffer and
        returns immediately. The data is not written to the actual communication channel
        until the stream is flushed using `flush` or there is no more room available
        in the stream buffer. If an error occurs, then it returns a negative error code.
        Unlike the `send_short_array` function, this function does not require that the
        stream send buffer be at least `num_elements` 16-bit integers in length. Hence, it
        allows smaller stream buffers to be used.

        If the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within each short integer when they
        are sent.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer. All the data will be
        consumed and the total number of short integers sent is returned. Some of the data may
        remain in the stream buffer and not be sent until the next time `flush` is called or
        there is no more room available in the stream buffer. If an error occurs then the
        error code is returned and the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns the number of short integers sent successfully,
        which will be between 1 and `num_elements` (unless `num_elements` is zero). If no
        short integers could be sent without blocking, then ``-ErrorCode.WOULD_BLOCK`` is returned.
        If an error occurs then an exception is raised and the stream should be closed.

        This function does not support two threads sending or flushing data at the same time.
        However, data may be sent or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 16-bit integers containing the data to be sent.
        num_elements : int
            The number of 16-bit integers to send from the buffer.

        Returns
        -------
        int
            The number of 16-bit integers sent, which may be less than `num_elements` for non-blocking streams. If an error
            occurs, then an exception is raised. A value of zero is only returned if `num_elements` is zero.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------

        Send 4 16-bit integers immediately by writing them to the stream and then flushing the buffer.

        >>> import struct
        >>> from quanser.communications import Stream
        >>> elements = array("h", [1, 2, 3, 4])
        >>> num_elements = len(data)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   elements_written = stream.send_shorts(elements, num_elements)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_send_shorts(self._stream if self._stream is not None else ffi.NULL,
                                                       ffi.from_buffer("const t_short*", elements) if elements is not None else ffi.NULL,
                                                       num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def send_short_array(self, elements, num_elements):
        """Writes an array of 16-bit integers to the stream buffer. It attempts
        to store the integers in the stream buffer. It differs from the `send_shorts`
        function in that it treats the entire array as an atomic unit. It either writes
        all of the array or none of it. If there is enough room available in the stream
        buffer then it stores the data in the buffer and returns immediately. The data
        is not written to the actual communication channel until the stream is flushed
        using `flush` or there is no more room available in the stream buffer. If
        an error occurs, then it throws an exception.

        Unlike the `send_shorts` function, the size of the stream send buffer 
        must be at least as large as the number of bytes being sent.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer. All the data will be
        consumed and 1 is returned. Some of the data may remain in the stream buffer and not be
        sent until the next time `flush` is called or there is no more room available in
        the stream buffer. If an error occurs then an exception is raised and the stream
        should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns 1 if the array is sent successfully.
        If the array could not be sent without blocking, then it returns the
        error code ``-ErrorCode.WOULD_BLOCK``. If an error occurs then an exception is raised
        and the stream should be closed.

        This function does not support two threads sending or flushing data at the same time.
        However, data may be sent or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 16-bit integers containing the data to be sent.
        num_elements : int
            The number of 16-bit integers to send from the buffer.

        Returns
        -------
        int
            Returns 1 on success. If an error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------

        Send 4 16-bit integers atomically by writing them to the stream and then flushing the buffer.

        >>> import struct
        >>> from quanser.communications import Stream
        >>> elements = array("h", [1, 2, 3, 4])
        >>> num_elements = len(elements)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   elements_written = stream.send_short_array(elements, num_elements)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_send_short_array(self._stream if self._stream is not None else ffi.NULL,
                                                            ffi.from_buffer("const t_short*", elements) if elements is not None else ffi.NULL,
                                                            num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def send_int(self, data):
        """Writes a 32-bit integer to the stream buffer. It attempts to
        store the integer in the stream buffer. If there is enough room available in the
        stream buffer then it stores the data in the buffer and returns immediately. The
        data is not written to the actual communication channel until the stream is flushed
        using `flush` or there is no more room available in the stream buffer. If an
        error occurs, then it returns a negative error code.

        If the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within the 32-bit integer when it
        is sent.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer. All the data will be
        consumed and the total number of 32-bit integers sent is returned (1). Some of the data may
        remain in the stream buffer and not be sent until the next time `flush` is called or
        there is no more room available in the stream buffer. If an error occurs then an
        exception is raised and the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns the number of 32-bit integers sent successfully,
        which will be 1. If the 32-bit integer could not be sent without blocking, then
        ``-ErrorCode.WOULD_BLOCK`` is returned. If an error occurs then an exception is raised
        and the stream should be closed.

        This function does not support two threads sending or flushing data at the same time.
        However, data may be sent or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        data : int
            The 32-bit integer to send.

        Returns
        -------
        int
            The number of 32-bit integers sent, which will always be 1 unless no data was sent in non-blocking I/O. If an error
            occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------

        Send one 32-bit integer immediately by writing it to the stream and then flushing the buffer.

        >>> from quanser.communications import Stream
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   ints_written = stream.send_int(123456)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_send_int(self._stream if self._stream is not None else ffi.NULL,
                                                    data)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def send_ints(self, elements, num_elements):
        """This function writes an array of 32-bit integers to the stream buffer. It
        attempts to store the integers in the stream buffer. If there is enough
        room available in the stream buffer then it stores the data in the buffer and
        returns immediately. The data is not written to the actual communication channel
        until the stream is flushed using `flush` or there is no more room available
        in the stream buffer. If an error occurs, then it returns a negative error code.
        Unlike the `send_int_array` function, this function does not require that the
        stream send buffer be at least `num_elements` 32-bit integers in length. Hence, it
        allows smaller stream buffers to be used.

        If the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within each 32-bit integer when they
        are sent.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer. All the data will be
        consumed and the total number of 32-bit integers sent is returned. Some of the data may
        remain in the stream buffer and not be sent until the next time `flush` is called or
        there is no more room available in the stream buffer. If an error occurs then the
        error code is returned and the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns the number of 32-bit integers sent successfully,
        which will be between 1 and `num_elements` (unless `num_elements` is zero). If no
        32-bit integers could be sent without blocking, then ``-ErrorCode.WOULD_BLOCK`` is returned.
        If an error occurs then an exception is raised and the stream should be closed.

        This function does not support two threads sending or flushing data at the same time.
        However, data may be sent or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 32-bit integers containing the data to be sent.
        num_elements : int
            The number of 32-bit integers to send from the buffer.

        Returns
        -------
        int
            The number of 32-bit integers sent, which may be less than `num_elements` for non-blocking streams. If an error
            occurs, then an exception is raised. A value of zero is only returned if `num_elements` is zero.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------

        Send 4 32-bit integers immediately by writing them to the stream and then flushing the buffer.

        >>> import struct
        >>> from quanser.communications import Stream
        >>> elements = array("l", [1, 2, 3, 4])
        >>> num_elements = len(data)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   elements_written = stream.send_ints(elements, num_elements)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_send_ints(self._stream if self._stream is not None else ffi.NULL,
                                                     ffi.from_buffer("const t_int*", elements) if elements is not None else ffi.NULL,
                                                     num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def send_int_array(self, elements, num_elements):
        """Writes an array of 32-bit integers to the stream buffer. It attempts
        to store the integers in the stream buffer. It differs from the `send_ints`
        function in that it treats the entire array as an atomic unit. It either writes
        all of the array or none of it. If there is enough room available in the stream
        buffer then it stores the data in the buffer and returns immediately. The data
        is not written to the actual communication channel until the stream is flushed
        using `flush` or there is no more room available in the stream buffer. If
        an error occurs, then it throws an exception.

        Unlike the `send_ints` function, the size of the stream send buffer 
        must be at least as large as the number of bytes being sent.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer. All the data will be
        consumed and 1 is returned. Some of the data may remain in the stream buffer and not be
        sent until the next time `flush` is called or there is no more room available in
        the stream buffer. If an error occurs then an exception is raised and the stream
        should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns 1 if the array is sent successfully.
        If the array could not be sent without blocking, then it returns the
        error code ``-ErrorCode.WOULD_BLOCK``. If an error occurs then an exception is raised
        and the stream should be closed.

        This function does not support two threads sending or flushing data at the same time.
        However, data may be sent or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 32-bit integers containing the data to be sent.
        num_elements : int
            The number of 32-bit integers to send from the buffer.

        Returns
        -------
        int
            Returns 1 on success. If an error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------

        Send 4 32-bit integers atomically by writing them to the stream and then flushing the buffer.

        >>> import struct
        >>> from quanser.communications import Stream
        >>> elements = array("l", [1, 2, 3, 4])
        >>> num_elements = len(elements)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   elements_written = stream.send_int_array(elements, num_elements)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_send_int_array(self._stream if self._stream is not None else ffi.NULL,
                                                          ffi.from_buffer("const t_int*", elements) if elements is not None else ffi.NULL,
                                                          num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def send_long(self, data):
        """Writes a 64-bit long integer to the stream buffer. It attempts to
        store the long integer in the stream buffer. If there is enough room available in the
        stream buffer then it stores the data in the buffer and returns immediately. The
        data is not written to the actual communication channel until the stream is flushed
        using `flush` or there is no more room available in the stream buffer. If an
        error occurs, then it returns a negative error code.

        If the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within the long integer when it
        is sent.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer. All the data will be
        consumed and the total number of long integers sent is returned (1). Some of the data may
        remain in the stream buffer and not be sent until the next time `flush` is called or
        there is no more room available in the stream buffer. If an error occurs then an
        exception is raised and the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns the number of long integers sent successfully,
        which will be 1. If the long integer could not be sent without blocking, then
        ``-ErrorCode.WOULD_BLOCK`` is returned. If an error occurs then an exception is raised
        and the stream should be closed.

        This function does not support two threads sending or flushing data at the same time.
        However, data may be sent or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        data : long
            The long to send.

        Returns
        -------
        int
            The number of 64-bit integers sent, which will always be 1 unless no data was sent in non-blocking I/O. If an error
            occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------

        Send one 64-bit integer immediately by writing it to the stream and then flushing the buffer.

        >>> from quanser.communications import Stream
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   longs_written = stream.send_long(123)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_send_long(self._stream if self._stream is not None else ffi.NULL,
                                                     data)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def send_longs(self, elements, num_elements):
        """This function writes an array of 64-bit long integers to the stream buffer. It
        attempts to store the long integers in the stream buffer. If there is enough
        room available in the stream buffer then it stores the data in the buffer and
        returns immediately. The data is not written to the actual communication channel
        until the stream is flushed using `flush` or there is no more room available
        in the stream buffer. If an error occurs, then it returns a negative error code.
        Unlike the `send_long_array` function, this function does not require that the
        stream send buffer be at least `num_elements` 64-bit integers in length. Hence, it
        allows smaller stream buffers to be used.

        If the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within each long integer when they
        are sent.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer. All the data will be
        consumed and the total number of long integers sent is returned. Some of the data may
        remain in the stream buffer and not be sent until the next time `flush` is called or
        there is no more room available in the stream buffer. If an error occurs then the
        error code is returned and the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns the number of long integers sent successfully,
        which will be between 1 and `num_elements` (unless `num_elements` is zero). If no
        long integers could be sent without blocking, then ``-ErrorCode.WOULD_BLOCK`` is returned.
        If an error occurs then an exception is raised and the stream should be closed.

        This function does not support two threads sending or flushing data at the same time.
        However, data may be sent or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 64-bit integers containing the data to be sent.
        num_elements : int
            The number of 64-bit integers to send from the buffer.

        Returns
        -------
        int
            The number of 64-bit integers sent, which may be less than `num_elements` for non-blocking streams. If an error
            occurs, then an exception is raised. A value of zero is only returned if `num_elements` is zero.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------

        Send 4 64-bit integers immediately by writing them to the stream and then flushing the buffer.

        >>> import struct
        >>> from quanser.communications import Stream
        >>> elements = array("q", [1, 2, 3, 4])
        >>> num_elements = len(data)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   elements_written = stream.send_longs(elements, num_elements)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_send_longs(self._stream if self._stream is not None else ffi.NULL,
                                                      ffi.from_buffer("const t_long*", elements) if elements is not None else ffi.NULL,
                                                      num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def send_long_array(self, elements, num_elements):
        """Writes an array of 64-bit integers to the stream buffer. It attempts
        to store the integers in the stream buffer. It differs from the `send_longs`
        function in that it treats the entire array as an atomic unit. It either writes
        all of the array or none of it. If there is enough room available in the stream
        buffer then it stores the data in the buffer and returns immediately. The data
        is not written to the actual communication channel until the stream is flushed
        using `flush` or there is no more room available in the stream buffer. If
        an error occurs, then it throws an exception.

        Unlike the `send_longs` function, the size of the stream send buffer 
        must be at least as large as the number of bytes being sent.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer. All the data will be
        consumed and 1 is returned. Some of the data may remain in the stream buffer and not be
        sent until the next time `flush` is called or there is no more room available in
        the stream buffer. If an error occurs then an exception is raised and the stream
        should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns 1 if the array is sent successfully.
        If the array could not be sent without blocking, then it returns the
        error code ``-ErrorCode.WOULD_BLOCK``. If an error occurs then an exception is raised
        and the stream should be closed.

        This function does not support two threads sending or flushing data at the same time.
        However, data may be sent or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 64-bit integers containing the data to be sent.
        num_elements : int
            The number of 64-bit integers to send from the buffer.

        Returns
        -------
        int
            Returns 1 on success. If an error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------

        Send 4 64-bit integers atomically by writing them to the stream and then flushing the buffer.

        >>> import struct
        >>> from quanser.communications import Stream
        >>> elements = array("q", [1, 2, 3, 4])
        >>> num_elements = len(elements)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   elements_written = stream.send_long_array(elements, num_elements)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_send_long_array(self._stream if self._stream is not None else ffi.NULL,
                                                           ffi.from_buffer("const t_long*", elements) if elements is not None else ffi.NULL,
                                                           num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def send_single(self, data):
        """Writes a 32-bit single-precision float to the stream buffer. It attempts to
        store the single-precision float in the stream buffer. If there is enough room available in the
        stream buffer then it stores the data in the buffer and returns immediately. The
        data is not written to the actual communication channel until the stream is flushed
        using `flush` or there is no more room available in the stream buffer. If an
        error occurs, then it returns a negative error code.

        If the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within the single-precision float when it
        is sent.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer. All the data will be
        consumed and the total number of single-precision floats sent is returned (1). Some of the data may
        remain in the stream buffer and not be sent until the next time `flush` is called or
        there is no more room available in the stream buffer. If an error occurs then an
        exception is raised and the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns the number of single-precision floats sent successfully,
        which will be 1. If the single-precision float could not be sent without blocking, then
        ``-ErrorCode.WOULD_BLOCK`` is returned. If an error occurs then an exception is raised
        and the stream should be closed.

        This function does not support two threads sending or flushing data at the same time.
        However, data may be sent or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        data : float
            The single-precision float to send.

        Returns
        -------
        int
            The number of 32-bit single-precision floats sent, which will always be 1 unless no data was sent in non-blocking I/O. If an error
            occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------

        Send one 32-bit single-precision float immediately by writing it to the stream and then flushing the buffer.

        >>> from quanser.communications import Stream
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   singles_written = stream.send_single(3.14)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_send_single(self._stream if self._stream is not None else ffi.NULL,
                                                       data)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def send_singles(self, elements, num_elements):
        """This function writes an array of 32-bit single-precision floats to the stream buffer. It
        attempts to store the single-precision floats in the stream buffer. If there is enough
        room available in the stream buffer then it stores the data in the buffer and
        returns immediately. The data is not written to the actual communication channel
        until the stream is flushed using `flush` or there is no more room available
        in the stream buffer. If an error occurs, then it returns a negative error code.
        Unlike the `send_single_array` function, this function does not require that the
        stream send buffer be at least `num_elements` 32-bit single-precision floats in length. Hence, it
        allows smaller stream buffers to be used.

        If the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within each single-precision float when they
        are sent.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer. All the data will be
        consumed and the total number of single-precision floats sent is returned. Some of the data may
        remain in the stream buffer and not be sent until the next time `flush` is called or
        there is no more room available in the stream buffer. If an error occurs then the
        error code is returned and the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns the number of single-precision floats sent successfully,
        which will be between 1 and `num_elements` (unless `num_elements` is zero). If no
        single-precision floats could be sent without blocking, then ``-ErrorCode.WOULD_BLOCK`` is returned.
        If an error occurs then an exception is raised and the stream should be closed.

        This function does not support two threads sending or flushing data at the same time.
        However, data may be sent or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 32-bit single-precision floats containing the data to be sent.
        num_elements : int
            The number of 32-bit single-precision floats to send from the buffer.

        Returns
        -------
        int
            The number of 32-bit single-precision floats sent, which may be less than `num_elements` for non-blocking streams. If an error
            occurs, then an exception is raised. A value of zero is only returned if `num_elements` is zero.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------

        Send 4 32-bit single-precision floats immediately by writing them to the stream and then flushing the buffer.

        >>> import struct
        >>> from quanser.communications import Stream
        >>> elements = array("f", [1, 2, 3, 4])
        >>> num_elements = len(data)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   elements_written = stream.send_singles(elements, num_elements)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_send_singles(self._stream if self._stream is not None else ffi.NULL,
                                                        ffi.from_buffer("const t_single*", elements) if elements is not None else ffi.NULL,
                                                        num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def send_single_array(self, elements, num_elements):
        """Writes an array of 32-bit single-precision floats to the stream buffer. It attempts
        to store the single-precision floats in the stream buffer. It differs from the `send_singles`
        function in that it treats the entire array as an atomic unit. It either writes
        all of the array or none of it. If there is enough room available in the stream
        buffer then it stores the data in the buffer and returns immediately. The data
        is not written to the actual communication channel until the stream is flushed
        using `flush` or there is no more room available in the stream buffer. If
        an error occurs, then it throws an exception.

        Unlike the `send_singles` function, the size of the stream send buffer 
        must be at least as large as the number of bytes being sent.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer. All the data will be
        consumed and 1 is returned. Some of the data may remain in the stream buffer and not be
        sent until the next time `flush` is called or there is no more room available in
        the stream buffer. If an error occurs then an exception is raised and the stream
        should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns 1 if the array is sent successfully.
        If the array could not be sent without blocking, then it returns the
        error code ``-ErrorCode.WOULD_BLOCK``. If an error occurs then an exception is raised
        and the stream should be closed.

        This function does not support two threads sending or flushing data at the same time.
        However, data may be sent or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 32-bit single-precision floats containing the data to be sent.
        num_elements : int
            The number of 32-bit single-precision floats to send from the buffer.

        Returns
        -------
        int
            Returns 1 on success. If an error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------

        Send 4 32-bit single-precision floats atomically by writing them to the stream and then flushing the buffer.

        >>> import struct
        >>> from quanser.communications import Stream
        >>> elements = array("f", [1, 2, 3, 4])
        >>> num_elements = len(elements)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   elements_written = stream.send_single_array(elements, num_elements)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_send_single_array(self._stream if self._stream is not None else ffi.NULL,
                                                             ffi.from_buffer("const t_single*", elements) if elements is not None else ffi.NULL,
                                                             num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def send_double(self, data):
        """Writes a 64-bit double-precision float to the stream buffer. It attempts to
        store the double-precision float in the stream buffer. If there is enough room available in the
        stream buffer then it stores the data in the buffer and returns immediately. The
        data is not written to the actual communication channel until the stream is flushed
        using `flush` or there is no more room available in the stream buffer. If an
        error occurs, then it returns a negative error code.

        If the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within the double-precision float when it
        is sent.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer. All the data will be
        consumed and the total number of double-precision floats sent is returned (1). Some of the data may
        remain in the stream buffer and not be sent until the next time `flush` is called or
        there is no more room available in the stream buffer. If an error occurs then an
        exception is raised and the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns the number of double-precision floats sent successfully,
        which will be 1. If the double-precision float could not be sent without blocking, then
        ``-ErrorCode.WOULD_BLOCK`` is returned. If an error occurs then an exception is raised
        and the stream should be closed.

        This function does not support two threads sending or flushing data at the same time.
        However, data may be sent or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        data : float
            The double-precision float to send.

        Returns
        -------
        int
            The number of 64-bit double-precision floats sent, which will always be 1 unless no data was sent in non-blocking I/O. If an error
            occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------

        Send one 64-bit double-precision float immediately by writing it to the stream and then flushing the buffer.

        >>> from quanser.communications import Stream
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   doubles_written = stream.send_double(3.14)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_send_double(self._stream if self._stream is not None else ffi.NULL,
                                                       data)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def send_doubles(self, elements, num_elements):
        """This function writes an array of 64-bit double-precision floats to the stream buffer. It
        attempts to store the double-precision floats in the stream buffer. If there is enough
        room available in the stream buffer then it stores the data in the buffer and
        returns immediately. The data is not written to the actual communication channel
        until the stream is flushed using `flush` or there is no more room available
        in the stream buffer. If an error occurs, then it returns a negative error code.
        Unlike the `send_double_array` function, this function does not require that the
        stream send buffer be at least `num_elements` 64-bit double-precision floats in length. Hence, it
        allows smaller stream buffers to be used.

        If the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within each double-precision float when they
        are sent.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer. All the data will be
        consumed and the total number of double-precision floats sent is returned. Some of the data may
        remain in the stream buffer and not be sent until the next time `flush` is called or
        there is no more room available in the stream buffer. If an error occurs then the
        error code is returned and the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns the number of double-precision floats sent successfully,
        which will be between 1 and `num_elements` (unless `num_elements` is zero). If no
        double-precision floats could be sent without blocking, then ``-ErrorCode.WOULD_BLOCK`` is returned.
        If an error occurs then an exception is raised and the stream should be closed.

        This function does not support two threads sending or flushing data at the same time.
        However, data may be sent or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 64-bit double-precision floats containing the data to be sent.
        num_elements : int
            The number of 64-bit double-precision floats to send from the buffer.

        Returns
        -------
        int
            The number of 64-bit double-precision floats sent, which may be less than `num_elements` for non-blocking streams. If an error
            occurs, then an exception is raised. A value of zero is only returned if `num_elements` is zero.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------

        Send 4 64-bit double-precision floats immediately by writing them to the stream and then flushing the buffer.

        >>> import struct
        >>> from quanser.communications import Stream
        >>> elements = array("d", [1, 2, 3, 4])
        >>> num_elements = len(data)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   elements_written = stream.send_doubles(elements, num_elements)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_send_doubles(self._stream if self._stream is not None else ffi.NULL,
                                                        ffi.from_buffer("const t_double*", elements) if elements is not None else ffi.NULL,
                                                        num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def send_double_array(self, elements, num_elements):
        """Writes an array of 64-bit double-precision floats to the stream buffer. It attempts
        to store the double-precision floats in the stream buffer. It differs from the `send_doubles`
        function in that it treats the entire array as an atomic unit. It either writes
        all of the array or none of it. If there is enough room available in the stream
        buffer then it stores the data in the buffer and returns immediately. The data
        is not written to the actual communication channel until the stream is flushed
        using `flush` or there is no more room available in the stream buffer. If
        an error occurs, then it throws an exception.

        Unlike the `send_doubles` function, the size of the stream send buffer 
        must be at least as large as the number of bytes being sent.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer. All the data will be
        consumed and 1 is returned. Some of the data may remain in the stream buffer and not be
        sent until the next time `flush` is called or there is no more room available in
        the stream buffer. If an error occurs then an exception is raised and the stream
        should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns 1 if the array is sent successfully.
        If the array could not be sent without blocking, then it returns the
        error code ``-ErrorCode.WOULD_BLOCK``. If an error occurs then an exception is raised
        and the stream should be closed.

        This function does not support two threads sending or flushing data at the same time.
        However, data may be sent or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 64-bit double-precision floats containing the data to be sent.
        num_elements : int
            The number of 64-bit double-precision floats to send from the buffer.

        Returns
        -------
        int
            Returns 1 on success. If an error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------

        Send 4 64-bit double-precision floats atomically by writing them to the stream and then flushing the buffer.

        >>> import struct
        >>> from quanser.communications import Stream
        >>> elements = array("d", [1, 2, 3, 4])
        >>> num_elements = len(elements)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, 64, 64)
        >>> try:
        >>>   elements_written = stream.send_double_array(elements, num_elements)
        >>>   stream.flush()
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_send_double_array(self._stream if self._stream is not None else ffi.NULL,
                                                             ffi.from_buffer("const t_double*", elements) if elements is not None else ffi.NULL,
                                                             num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def receive(self, buffer, buffer_size):
        """Receives data over a client stream. It attempts to receive `buffer_size` bytes from the communication
        channel.

        If `listen` or `connect` was called with the non-blocking flag set to ``False``, then this function blocks until
        all the data is read. If the connection has been closed gracefully, then it returns 0 only once there is no more
        data to receive. Otherwise it returns the number of bytes read before the connection closed. Once all the data
        in the stream buffer is exhausted, it will return 0 to indicate the connection has been closed. If an error
        occurs, then it raises an exception.

        If `listen` or `connect` was called with the non-blocking flag set to ``True``, then this function does not
        block. If no data is available at all, then it returns `-ErrorCode.WOULD_BLOCK`. In this case, the `poll` function
        may be used with ``PollFlag.RECEIVE`` to determine when data becomes available; otherwise, it returns the number
        of bytes received.

        Unlike the `receive_byte_array` function, this function does not require that the stream receive buffer be at
        least `buffer_size` bytes in length. Hence, it allows smaller stream buffers to be used.

        This function does not support two threads calling `receive` at the same time; however, `send` or `flush` may be
        called by another thread at the same time as `receive`.

        The semantics of this function differ from the BSD `recv()` socket function because it receives `buffer_size`
        bytes in blocking mode rather than the number of bytes that were sent in a single `send()` call at the peer. The
        semantics differ because this function attempts to "read ahead" by keeping the stream buffer full, thereby
        minimizing the number of receive operations performed on the internal connection. Also, due to buffering of the
        `send` operation, the number of `send()` calls made at the peer may not correspond to the number expected.

        Parameters
        ----------
        buffer : array_like
            A buffer of at least `buffer_size` bytes in which the received data will be stored.
        buffer_size : int
            The number of bytes available in the buffer.

        Returns
        -------
        int
            The number of bytes received, which may be less than `buffer_size` bytes for non-blocking streams. If no
            more data is available and the connection has been closed gracefully, then 0 is returned. If not enough
            bytes are available and the method would block, then ``-ErrorCode.WOULD_BLOCK`` is returned for non-blocking
            streams. If an error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> buffer = bytearray(buffer_size)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   bytes_read = stream.receive(buffer, buffer_size)
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_receive(self._stream if self._stream is not None else ffi.NULL,
                                                   ffi.from_buffer(buffer) if buffer is not None else ffi.NULL,
                                                   buffer_size)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def receive_bytes(self, elements, num_elements):
        """Receives an array of bytes over a client stream. It has the same semantics as the `receive` function.

        Unlike the `receive_byte_array` function, this function does not require that the stream receive buffer be at
        least `num_elements` bytes in length. Hence, it allows smaller stream buffers to be used.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` bytes in which the received data will be stored.
        num_elements : int
            The number of bytes available in the buffer.

        Returns
        -------
        int
            The number of bytes received, which may be less than `num_elements` bytes for non-blocking streams. If no
            more data is available and the connection has been closed gracefully, then 0 is returned. If not enough
            bytes are available and the method would block, then ``-ErrorCode.WOULD_BLOCK`` is returned for non-blocking
            streams. If an error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> buffer = bytearray(buffer_size)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   bytes_read = stream.receive_bytes(buffer, buffer_size)
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_receive_bytes(self._stream if self._stream is not None else ffi.NULL,
                                                         ffi.from_buffer(elements) if elements is not None else ffi.NULL,
                                                         num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def receive_byte_array(self, elements, num_elements):
        """Receives an array of bytes over a client stream. It differs from
        the `receive_bytes` function in that it treats the entire array as an
        atomic unit. It either receives all of the array or none of it. It also requires
        that the stream receive buffer be at least as large as the array of bytes.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function blocks until all the data is read.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. If fewer bytes are available then the size of
        the entire array then it returns with the error code ``-ErrorCode.WOULD_BLOCK``. 
        In this case, the `poll` function may be used with the ``PollFlag.RECEIVE`` flag
        to determine when data becomes available. Otherwise it returns 1.

        If the connection has been closed gracefully then it returns 0 only if there are fewer
        bytes left to receive than the size of the entire array. Otherwise it returns 1. Once
        there are fewer bytes left to receive than the size of the entire array then it will
        return 0 to indicate the connection has been closed. Use `receive` to receive any
        remaining bytes if required. If an error occurs, then it raises an exception.

        This function does not support two threads receiving data at the same time. However,
        data may be sent or the stream flushed by another thread at the same time as data is being
        received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` bytes in which the received data will be stored.
        num_elements : int
            The number of bytes available in the buffer.

        Returns
        -------
        int
            Returns 1 on success. If no more data is available and the connection has been closed 
            gracefully, then 0 is returned. If not enough bytes are available and the method would 
            block, then ``-ErrorCode.WOULD_BLOCK`` is returned for non-blocking streams. If an 
            error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> buffer = bytearray(buffer_size)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   result = stream.receive_byte_array(buffer, buffer_size)
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_receive_byte_array(self._stream if self._stream is not None else ffi.NULL,
                                                              ffi.from_buffer(elements) if elements is not None else ffi.NULL,
                                                              num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def receive_shorts(self, elements, num_elements):
        """Receives an array of 16-bit integers over a client stream. If 
        the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within each short integer that it
        receives before storing them in the given buffer.

        Unlike the `receive_short_array` function, this function does not require that the
        stream receive buffer be at least `num_elements` 16-bit integers in length. Hence, it
        allows smaller stream buffers to be used.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function blocks until all the data is read.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. If fewer bytes are available then the size of
        a short integer then it returns ``-ErrorCode.WOULD_BLOCK``. In this case, the `poll`
        function may be used with the ``PollFlag.RECEIVE`` flag to determine when data becomes
        available. Otherwise it returns the number of short integers received.

        If the connection has been closed gracefully then it returns 0 only if there are fewer
        bytes left to receive than the size of a short integer. Otherwise it returns the number
        of short integers read before the connection closed. Once there are fewer bytes left to
        receive than the size of a short integer then it will return 0 to indicate the connection
        has been closed. Use `receive` to receive any remaining bytes if required. If an
        error occurs, then it returns a negative error code.

        This function does not support two threads receiving data at the same time. However,
        data may be sent or the stream flushed by another thread at the same time as data is being
        received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 16-bit integers in which the received data will be stored.
        num_elements : int
            The number of 16-bit integers available in the buffer.

        Returns
        -------
        int
            The number of 16-bit integers received, which may be less than `num_elements` integers for non-blocking streams. If no
            more data is available and the connection has been closed gracefully, then 0 is returned. If not enough
            16-bit inegers are available and the method would block, then ``-ErrorCode.WOULD_BLOCK`` is returned for non-blocking
            streams. If an error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> buffer = array("h", [0] * buffer_size)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   bytes_read = stream.receive_shorts(buffer, buffer_size)
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_receive_shorts(self._stream if self._stream is not None else ffi.NULL,
                                                          ffi.from_buffer("t_short*", elements) if elements is not None else ffi.NULL,
                                                          num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def receive_short_array(self, elements, num_elements):
        """Receives an array of 16-bit integers over a client stream. It differs from
        the `receive_shorts` function in that it treats the entire array as an
        atomic unit. It either receives all of the array or none of it. It also requires
        that the stream receive buffer be at least as large as the array of 16-bit integers.
        If the stream has been configured to swap bytes using `set_swap_bytes` then this function
        will swap the order of the bytes within each short integer that it receives before
        storing them in the given buffer.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function blocks until all the data is read.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. If fewer 16-bit integers are available then the size of
        the entire array then it returns with the error code ``-ErrorCode.WOULD_BLOCK``. 
        In this case, the `poll` function may be used with the ``PollFlag.RECEIVE`` flag
        to determine when data becomes available. Otherwise it returns 1.

        If the connection has been closed gracefully then it returns 0 only if there are fewer
        16-bit integers left to receive than the size of the entire array. Otherwise it returns 1. Once
        there are fewer 16-bit integers left to receive than the size of the entire array then it will
        return 0 to indicate the connection has been closed. Use `receive` to receive any
        remaining bytes if required. If an error occurs, then it raises an exception.

        This function does not support two threads receiving data at the same time. However,
        data may be sent or the stream flushed by another thread at the same time as data is being
        received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 16-bit integers in which the received data will be stored.
        num_elements : int
            The number of 16-bit integers available in the buffer.

        Returns
        -------
        int
            Returns 1 on success. If no more data is available and the connection has been closed 
            gracefully, then 0 is returned. If not enough 16-bit integers are available and the method would 
            block, then ``-ErrorCode.WOULD_BLOCK`` is returned for non-blocking streams. If an 
            error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> buffer = array("h", [0] * buffer_size)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   result = stream.receive_short_array(buffer, buffer_size)
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_receive_short_array(self._stream if self._stream is not None else ffi.NULL,
                                                               ffi.from_buffer("t_short*", elements) if elements is not None else ffi.NULL,
                                                               num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def receive_ints(self, elements, num_elements):
        """Receives an array of 32-bit integers over a client stream. If 
        the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within each integer that it
        receives before storing them in the given buffer.

        Unlike the `receive_int_array` function, this function does not require that the
        stream receive buffer be at least `num_elements` 32-bit integers in length. Hence, it
        allows smaller stream buffers to be used.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function blocks until all the data is read.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. If fewer bytes are available then the size of
        a integer then it returns ``-ErrorCode.WOULD_BLOCK``. In this case, the `poll`
        function may be used with the ``PollFlag.RECEIVE`` flag to determine when data becomes
        available. Otherwise it returns the number of integers received.

        If the connection has been closed gracefully then it returns 0 only if there are fewer
        bytes left to receive than the size of a integer. Otherwise it returns the number
        of integers read before the connection closed. Once there are fewer bytes left to
        receive than the size of a integer then it will return 0 to indicate the connection
        has been closed. Use `receive` to receive any remaining bytes if required. If an
        error occurs, then it returns a negative error code.

        This function does not support two threads receiving data at the same time. However,
        data may be sent or the stream flushed by another thread at the same time as data is being
        received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 32-bit integers in which the received data will be stored.
        num_elements : int
            The number of 32-bit integers available in the buffer.

        Returns
        -------
        int
            The number of 32-bit integers received, which may be less than `num_elements` integers for non-blocking streams. If no
            more data is available and the connection has been closed gracefully, then 0 is returned. If not enough
            32-bit inegers are available and the method would block, then ``-ErrorCode.WOULD_BLOCK`` is returned for non-blocking
            streams. If an error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> buffer = array("l", [0] * buffer_size)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   bytes_read = stream.receive_ints(buffer, buffer_size)
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_receive_ints(self._stream if self._stream is not None else ffi.NULL,
                                                        ffi.from_buffer("t_int*", elements) if elements is not None else ffi.NULL,
                                                        num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def receive_int_array(self, elements, num_elements):
        """Receives an array of 32-bit integers over a client stream. It differs from
        the `receive_ints` function in that it treats the entire array as an
        atomic unit. It either receives all of the array or none of it. It also requires
        that the stream receive buffer be at least as large as the array of 32-bit integers.
        If the stream has been configured to swap bytes using `set_swap_bytes` then this function
        will swap the order of the bytes within each integer that it receives before
        storing them in the given buffer.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function blocks until all the data is read.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. If fewer 32-bit integers are available then the size of
        the entire array then it returns with the error code ``-ErrorCode.WOULD_BLOCK``. 
        In this case, the `poll` function may be used with the ``PollFlag.RECEIVE`` flag
        to determine when data becomes available. Otherwise it returns 1.

        If the connection has been closed gracefully then it returns 0 only if there are fewer
        32-bit integers left to receive than the size of the entire array. Otherwise it returns 1. Once
        there are fewer 32-bit integers left to receive than the size of the entire array then it will
        return 0 to indicate the connection has been closed. Use `receive` to receive any
        remaining bytes if required. If an error occurs, then it raises an exception.

        This function does not support two threads receiving data at the same time. However,
        data may be sent or the stream flushed by another thread at the same time as data is being
        received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 32-bit integers in which the received data will be stored.
        num_elements : int
            The number of 32-bit integers available in the buffer.

        Returns
        -------
        int
            Returns 1 on success. If no more data is available and the connection has been closed 
            gracefully, then 0 is returned. If not enough 32-bit integers are available and the method would 
            block, then ``-ErrorCode.WOULD_BLOCK`` is returned for non-blocking streams. If an 
            error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> buffer = array("l", [0] * buffer_size)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   result = stream.receive_int_array(buffer, buffer_size)
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_receive_int_array(self._stream if self._stream is not None else ffi.NULL,
                                                             ffi.from_buffer("t_int*", elements) if elements is not None else ffi.NULL,
                                                             num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def receive_longs(self, elements, num_elements):
        """Receives an array of 64-bit integers over a client stream. If 
        the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within each long integer that it
        receives before storing them in the given buffer.

        Unlike the `receive_long_array` function, this function does not require that the
        stream receive buffer be at least `num_elements` 64-bit integers in length. Hence, it
        allows smaller stream buffers to be used.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function blocks until all the data is read.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. If fewer bytes are available then the size of
        a long integer then it returns ``-ErrorCode.WOULD_BLOCK``. In this case, the `poll`
        function may be used with the ``PollFlag.RECEIVE`` flag to determine when data becomes
        available. Otherwise it returns the number of long integers received.

        If the connection has been closed gracefully then it returns 0 only if there are fewer
        bytes left to receive than the size of a long integer. Otherwise it returns the number
        of long integers read before the connection closed. Once there are fewer bytes left to
        receive than the size of a long integer then it will return 0 to indicate the connection
        has been closed. Use `receive` to receive any remaining bytes if required. If an
        error occurs, then it returns a negative error code.

        This function does not support two threads receiving data at the same time. However,
        data may be sent or the stream flushed by another thread at the same time as data is being
        received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 64-bit integers in which the received data will be stored.
        num_elements : int
            The number of 64-bit integers available in the buffer.

        Returns
        -------
        int
            The number of 64-bit integers received, which may be less than `num_elements` integers for non-blocking streams. If no
            more data is available and the connection has been closed gracefully, then 0 is returned. If not enough
            64-bit inegers are available and the method would block, then ``-ErrorCode.WOULD_BLOCK`` is returned for non-blocking
            streams. If an error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> buffer = array("q", [0] * buffer_size)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   bytes_read = stream.receive_longs(buffer, buffer_size)
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_receive_longs(self._stream if self._stream is not None else ffi.NULL,
                                                         ffi.from_buffer("t_long*", elements) if elements is not None else ffi.NULL,
                                                         num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def receive_long_array(self, elements, num_elements):
        """Receives an array of 64-bit integers over a client stream. It differs from
        the `receive_longs` function in that it treats the entire array as an
        atomic unit. It either receives all of the array or none of it. It also requires
        that the stream receive buffer be at least as large as the array of 64-bit integers.
        If the stream has been configured to swap bytes using `set_swap_bytes` then this function
        will swap the order of the bytes within each long integer that it receives before
        storing them in the given buffer.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function blocks until all the data is read.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. If fewer 64-bit integers are available then the size of
        the entire array then it returns with the error code ``-ErrorCode.WOULD_BLOCK``. 
        In this case, the `poll` function may be used with the ``PollFlag.RECEIVE`` flag
        to determine when data becomes available. Otherwise it returns 1.

        If the connection has been closed gracefully then it returns 0 only if there are fewer
        64-bit integers left to receive than the size of the entire array. Otherwise it returns 1. Once
        there are fewer 64-bit integers left to receive than the size of the entire array then it will
        return 0 to indicate the connection has been closed. Use `receive` to receive any
        remaining bytes if required. If an error occurs, then it raises an exception.

        This function does not support two threads receiving data at the same time. However,
        data may be sent or the stream flushed by another thread at the same time as data is being
        received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 64-bit integers in which the received data will be stored.
        num_elements : int
            The number of 64-bit integers available in the buffer.

        Returns
        -------
        int
            Returns 1 on success. If no more data is available and the connection has been closed 
            gracefully, then 0 is returned. If not enough 64-bit integers are available and the method would 
            block, then ``-ErrorCode.WOULD_BLOCK`` is returned for non-blocking streams. If an 
            error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> buffer = array("q", [0] * buffer_size)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   result = stream.receive_long_array(buffer, buffer_size)
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_receive_long_array(self._stream if self._stream is not None else ffi.NULL,
                                                              ffi.from_buffer("t_long*", elements) if elements is not None else ffi.NULL,
                                                              num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def receive_singles(self, elements, num_elements):
        """Receives an array of 32-bit single-precision floats over a client stream. If 
        the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within each single-precision float that it
        receives before storing them in the given buffer.

        Unlike the `receive_single_array` function, this function does not require that the
        stream receive buffer be at least `num_elements` 32-bit single-precision floats in length. Hence, it
        allows smaller stream buffers to be used.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function blocks until all the data is read.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. If fewer bytes are available then the size of
        a single 32-bit single-precision float then it returns ``-ErrorCode.WOULD_BLOCK``. In this case, the `poll`
        function may be used with the ``PollFlag.RECEIVE`` flag to determine when data becomes
        available. Otherwise it returns the number of 32-bit single-precision floats received.

        If the connection has been closed gracefully then it returns 0 only if there are fewer
        bytes left to receive than the size of a 32-bit single-precision float. Otherwise it returns the number
        of 32-bit single-precision floats read before the connection closed. Once there are fewer bytes left to
        receive than the size of a 32-bit single-precision float then it will return 0 to indicate the connection
        has been closed. Use `receive` to receive any remaining bytes if required. If an
        error occurs, then it returns a negative error code.

        This function does not support two threads receiving data at the same time. However,
        data may be sent or the stream flushed by another thread at the same time as data is being
        received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 32-bit single-precision floats in which the received data will be stored.
        num_elements : int
            The number of 32-bit single-precision floats available in the buffer.

        Returns
        -------
        int
            The number of 32-bit single-precision floats received, which may be less than `num_elements` floats for non-blocking streams. If no
            more data is available and the connection has been closed gracefully, then 0 is returned. If not enough
            32-bit single-precision floats are available and the method would block, then ``-ErrorCode.WOULD_BLOCK`` is returned for non-blocking
            streams. If an error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> buffer = array("f", [0] * buffer_size)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   bytes_read = stream.receive_singles(buffer, buffer_size)
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_receive_singles(self._stream if self._stream is not None else ffi.NULL,
                                                          ffi.from_buffer("t_single*", elements) if elements is not None else ffi.NULL,
                                                          num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def receive_single_array(self, elements, num_elements):
        """Receives an array of 32-bit single-precision floats over a client stream. It differs from
        the `receive_singles` function in that it treats the entire array as an
        atomic unit. It either receives all of the array or none of it. It also requires
        that the stream receive buffer be at least as large as the array of 32-bit single-precision floats.
        If the stream has been configured to swap bytes using `set_swap_bytes` then this function
        will swap the order of the bytes within each 32-bit single-precision float that it receives before
        storing them in the given buffer.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function blocks until all the data is read.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. If fewer 32-bit single-precision floats are available then the size of
        the entire array then it returns with the error code ``-ErrorCode.WOULD_BLOCK``. 
        In this case, the `poll` function may be used with the ``PollFlag.RECEIVE`` flag
        to determine when data becomes available. Otherwise it returns 1.

        If the connection has been closed gracefully then it returns 0 only if there are fewer
        32-bit single-precision floats left to receive than the size of the entire array. Otherwise it returns 1. Once
        there are fewer 32-bit single-precision floats left to receive than the size of the entire array then it will
        return 0 to indicate the connection has been closed. Use `receive` to receive any
        remaining bytes if required. If an error occurs, then it raises an exception.

        This function does not support two threads receiving data at the same time. However,
        data may be sent or the stream flushed by another thread at the same time as data is being
        received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 32-bit single-precision floats in which the received data will be stored.
        num_elements : int
            The number of 32-bit single-precision floats available in the buffer.

        Returns
        -------
        int
            Returns 1 on success. If no more data is available and the connection has been closed 
            gracefully, then 0 is returned. If not enough 32-bit single-precision floats are available and the method would 
            block, then ``-ErrorCode.WOULD_BLOCK`` is returned for non-blocking streams. If an 
            error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> buffer = array("f", [0] * buffer_size)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   result = stream.receive_single_array(buffer, buffer_size)
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_receive_single_array(self._stream if self._stream is not None else ffi.NULL,
                                                                ffi.from_buffer("t_single*", elements) if elements is not None else ffi.NULL,
                                                                num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def receive_doubles(self, elements, num_elements):
        """Receives an array of 64-bit double-precision floats over a client stream. If 
        the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within each double-precision float that it
        receives before storing them in the given buffer.

        Unlike the `receive_double_array` function, this function does not require that the
        stream receive buffer be at least `num_elements` 64-bit double-precision floats in length. Hence, it
        allows smaller stream buffers to be used.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function blocks until all the data is read.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. If fewer bytes are available then the size of
        a double 64-bit double-precision float then it returns ``-ErrorCode.WOULD_BLOCK``. In this case, the `poll`
        function may be used with the ``PollFlag.RECEIVE`` flag to determine when data becomes
        available. Otherwise it returns the number of 64-bit double-precision floats received.

        If the connection has been closed gracefully then it returns 0 only if there are fewer
        bytes left to receive than the size of a 64-bit double-precision float. Otherwise it returns the number
        of 64-bit double-precision floats read before the connection closed. Once there are fewer bytes left to
        receive than the size of a 64-bit double-precision float then it will return 0 to indicate the connection
        has been closed. Use `receive` to receive any remaining bytes if required. If an
        error occurs, then it returns a negative error code.

        This function does not support two threads receiving data at the same time. However,
        data may be sent or the stream flushed by another thread at the same time as data is being
        received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 64-bit double-precision floats in which the received data will be stored.
        num_elements : int
            The number of 64-bit double-precision floats available in the buffer.

        Returns
        -------
        int
            The number of 64-bit double-precision floats received, which may be less than `num_elements` floats for non-blocking streams. If no
            more data is available and the connection has been closed gracefully, then 0 is returned. If not enough
            64-bit double-precision floats are available and the method would block, then ``-ErrorCode.WOULD_BLOCK`` is returned for non-blocking
            streams. If an error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> buffer = array("d", [0] * buffer_size)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   bytes_read = stream.receive_doubles(buffer, buffer_size)
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_receive_doubles(self._stream if self._stream is not None else ffi.NULL,
                                                          ffi.from_buffer("t_double*", elements) if elements is not None else ffi.NULL,
                                                          num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def receive_double_array(self, elements, num_elements):
        """Receives an array of 64-bit double-precision floats over a client stream. It differs from
        the `receive_doubles` function in that it treats the entire array as an
        atomic unit. It either receives all of the array or none of it. It also requires
        that the stream receive buffer be at least as large as the array of 64-bit double-precision floats.
        If the stream has been configured to swap bytes using `set_swap_bytes` then this function
        will swap the order of the bytes within each 64-bit double-precision float that it receives before
        storing them in the given buffer.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function blocks until all the data is read.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. If fewer 64-bit double-precision floats are available then the size of
        the entire array then it returns with the error code ``-ErrorCode.WOULD_BLOCK``. 
        In this case, the `poll` function may be used with the ``PollFlag.RECEIVE`` flag
        to determine when data becomes available. Otherwise it returns 1.

        If the connection has been closed gracefully then it returns 0 only if there are fewer
        64-bit double-precision floats left to receive than the size of the entire array. Otherwise it returns 1. Once
        there are fewer 64-bit double-precision floats left to receive than the size of the entire array then it will
        return 0 to indicate the connection has been closed. Use `receive` to receive any
        remaining bytes if required. If an error occurs, then it raises an exception.

        This function does not support two threads receiving data at the same time. However,
        data may be sent or the stream flushed by another thread at the same time as data is being
        received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        elements : array_like
            A buffer of at least `num_elements` 64-bit double-precision floats in which the received data will be stored.
        num_elements : int
            The number of 64-bit double-precision floats available in the buffer.

        Returns
        -------
        int
            Returns 1 on success. If no more data is available and the connection has been closed 
            gracefully, then 0 is returned. If not enough 64-bit double-precision floats are available and the method would 
            block, then ``-ErrorCode.WOULD_BLOCK`` is returned for non-blocking streams. If an 
            error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> buffer = array("d", [0] * buffer_size)
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   result = stream.receive_double_array(buffer, buffer_size)
        >>>   # ...
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_receive_double_array(self._stream if self._stream is not None else ffi.NULL,
                                                                ffi.from_buffer("t_double*", elements) if elements is not None else ffi.NULL,
                                                                num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def flush(self):
        """Flushes the stream buffer. It attempts to send the contents of the buffer over the communication channel. If
        an error occurs, then it raises an exception. If the connection is closed, it is considered an error condition.

        If `listen` or `connect` was called with the non-blocking flag set to ``False``, then this function blocks until
        all the data in the buffer is sent.

        If `listen` or `connect` was called with the non-blocking flag set to ``True``, then this function does not
        block. It attempts to send all the data remaining in the stream buffer. However, if this operation would block,
        then it returns ``-ErrorCode.WOULD_BLOCK``, even if it has already sent some of the data. In this case, the `poll`
        function may be used with ``PollFlag.FLUSH`` to determine when at least one more bytes may be flushed.

        This function does not support two threads calling `send` or `flush` at the same time; however, `send` or
        `flush` may be called by another thread at the same time as `receive`.

        Raises
        ------
        StreamError
            On non-zero return code. A suitable error message may be retrieved using `get_error_message`.

        Returns
        -------
        int
            Returns 1 on success. If no more data is available and the connection has been closed 
            gracefully, then 0 is returned. If the method would block, then ``-ErrorCode.WOULD_BLOCK`` 
            is returned for non-blocking streams. If an error occurs, then an exception is raised.

        Example
        -------
        Flush the send buffer in order to send a message that is smaller than the size of the buffer.

        >>> from quanser.communications import Stream
        >>> message = "Hello".encode()
        >>> num_bytes = len(message)
        >>> send_buffer_size = 64
        >>> receive_buffer_size = 64
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, send_buffer_size, receive_buffer_size)
        >>> try:
        >>>   bytes_written = stream.send(message, num_bytes)
        >>>   stream.flush()
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_flush(self._stream if self._stream is not None else ffi.NULL)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def peek_begin(self, prefetch = 0):
        """Prepares the `t_stream_peek_state` to begin peeking for data. "Peeking" involves
        reading ahead without removing the data from the stream buffer. It is particularly useful for
        parsing the input from the stream because it allows the next bytes to be tested without
        preventing the user from receiving those bytes later. It may also be used to read a sequence
        of data types as a single atomic unit, much like the `xxxx_array` functions. The "peek state" 
        is used to keep track of how far ahead the lookahead operations have reached so far.
 
        As an example of using the peek capabilities to read a sequence of data types as a single
        atomic unit using non-blocking I/O:

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> int_buf = array("i", [0])
        >>> double_buf = array("d", [0.0])
        >>> prefetch = 0
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", True, buffer_size, buffer_size)
        >>> try:
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.peek_begin(prefetch)
        >>>      if result > 0:
        >>>         result = stream.peek_int_array(state, int_buf, len(int_buf))
        >>>      if result > 0:
        >>>         result = stream.peek_double_array(state, double_buf, len(double_buf))
        >>>      result = stream.peek_end(state, result)
        >>>      if result >= 0:
        >>>         break
        >>>   
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        In this example, the code peeks ahead in the input stream for an integer and a double.
        If at any time the operation would block, then result is ``-ErrorCode.WOULD_BLOCK``.
        Since result is negative, `peek_end` will not advance the stream pointer and the data 
        is not removed from the input stream. Hence, the next time the code is called the same 
        data is read again.

        However, if the `peek_int` and `peek_double` succeed then `peek_end` does advance the
        stream pointer and returns 1. Hence, the data is removed from the input stream and 
        subsequent reads/peeks from the stream will return new data.

        Thus, the integer and double are read as one atomic unit from the input stream, because
        if not all the data is available, then nothing is removed from the input stream. Only
        if both quantities are read successfully is the data actually removed from the input
        stream.

        Note that the `peek_xxxx` functions may read data from the underlying communication
        channel, but the contents of the stream buffer are never overwritten until `peek_end`
        is called to indicate that the peeked data may be removed from the input stream.

        This function assumes that the stream is valid. If the prefetch is zero then it does
        not block because it does not access the underlying communication channel.

        However, if the prefetch is non-zero then it may access the underlying communication
        channel. Normally, the stream will read as much as it can on any receive operation
        and try to fill the stream's receive buffer. Hence, no prefetching of data is necessary
        because the stream will do so automatically on any receive operation. However, if
        read-ahead has been disabled by setting the ``BooleanProperty.NO_READ_AHEAD`` property then
        the stream only reads as much data as is required to satisfy the receive operation
        requested. Some protocols, like I2C, enforce this property and do not allow read-ahead.
        The prefetch parameter of `peek_begin` causes the stream to attempt to ensure that
        at least `prefetch` bytes are present in the stream receive buffer before the rest of
        the `peek_xxxx` operations are performed, thereby reducing the number of calls to
        the underlying stream to receive data when read-ahead has been disabled.

        If prefetch is not required (because read-ahead is enabled on the stream - the default
        situation) then the prefetch parameter may be zero. If prefetch is desired, then it
        should be set to *no more* than the number of bytes expected to be peeked in subsequent
        `peek_xxxx` calls.

        Parameters
        ----------
        prefetch : int
            The number of bytes to prefetch even if read-ahead is disabled.

        Returns
        -------
        result : int
            If the stream is closed gracefully during a prefetch operation and there are 
            not enough bytes left in the receive buffer for the prefetch specified then 
            it will return zero. It returns 1 on success.
        state : t_stream_peek_state
            The initialized peek state.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        Suppose the following binary structure is being received::

            struct {
                t_int8 temperature;
                t_uint8 status;
                t_int16 gyro_rates[3];
            }

        This structure is 1 + 1 + 3*2 = 8 bytes long. Hence, the code to read this structure
        as one atomic unit, while accounting for potential byte swapping due to byte order
        differences between server and client would be:

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> temperature = array("b", [0])
        >>> status = array("B", [0])
        >>> gyro_rates = array("h", [0 0 0])
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", True, buffer_size, buffer_size)
        >>> prefetch = len(temperature) + len(status) + len(gyro_rates)*2
        >>> try:
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.peek_begin(prefetch)
        >>>      if result > 0:
        >>>         result = stream.peek_byte_array(state, temperature, len(temperature))
        >>>      if result > 0:
        >>>         result = stream.peek_byte_array(state, status, len(status))
        >>>      if result > 0:
        >>>         result = stream.peek_short_array(state, gyro_rates, len(gyro_rates))
        >>>      result = stream.peek_end(state, result)
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        state = ffi.new("t_stream_peek_state*")
        result = communications_lib.stream_peek_begin(self._stream if self._stream is not None else ffi.NULL,
                                                      state, prefetch)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result, state

    def peek_end(self, state, status):
        """Finishes a "peek" operation by removing all peeked data from the input
        stream. It must be called after a sequence of `peek_xxxx` operations to complete
        the peek. If this function is not called before another `peek_begin` then the
        data is left in the stream buffer.

        This function assumes that the stream is valid. It does not block because it does not
        access the underlying communication channel.

        Parameters
        ----------
        state : t_stream_peek_state
            The "peek state" indicating how much data to remove from the input stream.
        status : int
            This value is typically the result from the last `peek_xxxx` operation.
            If it is greater than zero then the peek is completed and the stream pointer 
            advanced. If it is 0 because the stream closed before finishing the peek 
            operations then this function does not advance the stream pointer and
            returns 0. If it is negative then the stream pointer is not advanced and
            the status is returned as the result.

        Returns
        -------
        result : int
            If the result argument is less than or equal to zero then it simply returns result. Otherwise,
            it returns 1 to indicate the operation completed successfully. 

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_buf = array("b", [0 0 0])
        >>> short_buf = array("h", [0 0 0])
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", True, buffer_size, buffer_size)
        >>> try:
        >>>   prefetch = len(byte_buf) + 2 * len(short_buf)
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.peek_begin(prefetch)
        >>>      if result > 0:
        >>>         result = stream.peek_byte_array(state, byte_buf, len(byte_buf))
        >>>      if result > 0:
        >>>         result = stream.peek_short_array(state, short_buf, len(short_buf))
        >>>      result = stream.peek_end(state, result)
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        return communications_lib.stream_peek_end(self._stream if self._stream is not None else ffi.NULL, state, status)

    def peek_byte_array(self, state, elements, num_elements):
        """Peeks ahead in the input stream to read an array of bytes from a client 
        stream. It either peeks all of the array or none of it.

        The `peek_begin` function must be called to initialize the peek state. No data
        peeked will be removed from the input stream until `peek_end` is called. If
        `peek_end` is not called before the next `peek_begin` then the peeked
        data is read again.

        See the `peek_begin` function for more information and an example.

        The size of the stream receive buffer must be at least `num_elements` bytes in 
        length.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function blocks until all the data is peeked. Blocking may occur because 
        data may be read from the underlying communication channel. However, the contents of 
        the stream buffer are never overwritten until `peek_end` is called to indicate 
        that the peeked data may be removed from the input stream.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. If fewer bytes are available then the size of
        the entire array then it returns ``-ErrorCode.WOULD_BLOCK``. In this case, the `poll`
        function may be used with the ``PollFlag.RECEIVE`` flag to determine when data becomes
        available. Otherwise it returns 1.

        If the connection has been closed gracefully and there are fewer bytes left to 
        peek than the size of the entire array then it returns 0. Otherwise it returns 1.
        Once there are fewer bytes left to peek than the size of the entire array then it
        will return ``-ErrorCode.WOULD_BLOCK`` if the stream is non-blocking. If an error 
        occurs, then it raises an exception.

        This function does not support two threads peeking data at the same time. However,
        data may be sent or the stream flushed by another thread at the same time as data is being
        peeked.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        state : t_stream_peek_state
            The peek state.
        elements : array_like
            A buffer of at least `num_elements` bytes in which the received data will be stored.
        num_elements : int
            The number of bytes available in the buffer.

        Returns
        -------
        result : int
            Returns 1 on success. If no more data is available and the connection has been closed gracefully,
            then it returns 0. If the method would block then it returns ``-ErrorCode.WOULD_BLOCK`` if the
            stream is non-blocking. If an error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_buf = array("b", [0 0 0])
        >>> short_buf = array("h", [0 0 0])
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", True, buffer_size, buffer_size)
        >>> try:
        >>>   prefetch = len(byte_buf) + 2 * len(short_buf)
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.peek_begin(prefetch)
        >>>      if result > 0:
        >>>         result = stream.peek_byte_array(state, byte_buf, len(byte_buf))
        >>>      if result > 0:
        >>>         result = stream.peek_short_array(state, short_buf, len(short_buf))
        >>>      result = stream.peek_end(state, result)
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_peek_byte_array(self._stream if self._stream is not None else ffi.NULL, state,
                                                           ffi.from_buffer(elements) if elements is not None else ffi.NULL,
                                                           num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def peek_short_array(self, state, elements, num_elements):
        """This function peeks ahead in the input stream to read an array of short (16-bit) integers
        from a client stream. It either peeks all of the array or none of it. If the stream has 
        been configured to swap bytes using `set_swap_bytes` then this function will 
        swap the order of the bytes within each element that it peeks before storing them in the 
        given buffer.

        The `peek_begin` function must be called to initialize the peek state. No data
        peeked will be removed from the input stream until `peek_end` is called. If
        `peek_end` is not called before the next `peek_begin` then the peeked
        data is read again.

        See the `peek_begin` function for more information and an example.

        The size of the stream receive buffer must be at least `num_elements` 16-bit integers
        in length.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function blocks until all the data is peeked. Blocking may occur because 
        data may be read from the underlying communication channel. However, the contents of 
        the stream buffer are never overwritten until `peek_end` is called to indicate 
        that the peeked data may be removed from the input stream.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. If fewer bytes are available then the size of
        the entire array then it returns ``-ErrorCode.WOULD_BLOCK``. In this case, the `poll`
        function may be used with the ``PollFlag.RECEIVE`` flag to determine when data becomes
        available. Otherwise it returns 1.

        If the connection has been closed gracefully then it returns 0 only if there are fewer
        16-bit integers left to peek than the size of the entire array. Otherwise it returns 1. Once
        there are fewer bytes left to peek than the size of the entire array then it will
        return 0 to indicate the connection has been closed. If an error occurs, then it returns 
        a negative error code.

        This function does not support two threads peeking data at the same time. However,
        data may be sent or the stream flushed by another thread at the same time as data is being
        peeked.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        state : t_stream_peek_state
            The peek state.
        elements : array_like
            A buffer of at least `num_elements` 16-bit integers in which the received data will be stored.
        num_elements : int
            The number of 16-bit integers available in the buffer.

        Returns
        -------
        result : int
            Returns 1 on success. If no more data is available and the connection has been closed gracefully,
            then it returns 0. If the method would block then it returns ``-ErrorCode.WOULD_BLOCK`` if the
            stream is non-blocking. If an error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_buf = array("b", [0 0 0])
        >>> short_buf = array("h", [0 0 0])
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", True, buffer_size, buffer_size)
        >>> try:
        >>>   prefetch = len(byte_buf) + 2 * len(short_buf)
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.peek_begin(prefetch)
        >>>      if result > 0:
        >>>         result = stream.peek_byte_array(state, byte_buf, len(byte_buf))
        >>>      if result > 0:
        >>>         result = stream.peek_short_array(state, short_buf, len(short_buf))
        >>>      result = stream.peek_end(state, result)
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_peek_short_array(self._stream if self._stream is not None else ffi.NULL, state,
                                                            ffi.from_buffer("t_short*", elements) if elements is not None else ffi.NULL,
                                                            num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def peek_int_array(self, state, elements, num_elements):
        """This function peeks ahead in the input stream to read an array of 32-bit integers
        from a client stream. It either peeks all of the array or none of it. If the stream has 
        been configured to swap bytes using `set_swap_bytes` then this function will 
        swap the order of the bytes within each element that it peeks before storing them in the 
        given buffer.

        The `peek_begin` function must be called to initialize the peek state. No data
        peeked will be removed from the input stream until `peek_end` is called. If
        `peek_end` is not called before the next `peek_begin` then the peeked
        data is read again.

        See the `peek_begin` function for more information and an example.

        The size of the stream receive buffer must be at least `num_elements` 32-bit integers
        in length.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function blocks until all the data is peeked. Blocking may occur because 
        data may be read from the underlying communication channel. However, the contents of 
        the stream buffer are never overwritten until `peek_end` is called to indicate 
        that the peeked data may be removed from the input stream.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. If fewer bytes are available then the size of
        the entire array then it returns ``-ErrorCode.WOULD_BLOCK``. In this case, the `poll`
        function may be used with the ``PollFlag.RECEIVE`` flag to determine when data becomes
        available. Otherwise it returns 1.

        If the connection has been closed gracefully then it returns 0 only if there are fewer
        32-bit integers left to peek than the size of the entire array. Otherwise it returns 1. Once
        there are fewer bytes left to peek than the size of the entire array then it will
        return 0 to indicate the connection has been closed. If an error occurs, then it returns 
        a negative error code.

        This function does not support two threads peeking data at the same time. However,
        data may be sent or the stream flushed by another thread at the same time as data is being
        peeked.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        state : t_stream_peek_state
            The peek state.
        elements : array_like
            A buffer of at least `num_elements` 32-bit integers in which the received data will be stored.
        num_elements : int
            The number of 32-bit integers available in the buffer.

        Returns
        -------
        result : int
            Returns 1 on success. If no more data is available and the connection has been closed gracefully,
            then it returns 0. If the method would block then it returns ``-ErrorCode.WOULD_BLOCK`` if the
            stream is non-blocking. If an error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_buf = array("b", [0 0 0])
        >>> int_buf = array("l", [0 0 0])
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", True, buffer_size, buffer_size)
        >>> try:
        >>>   prefetch = len(byte_buf) + 2 * len(int_buf)
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.peek_begin(prefetch)
        >>>      if result > 0:
        >>>         result = stream.peek_byte_array(state, byte_buf, len(byte_buf))
        >>>      if result > 0:
        >>>         result = stream.peek_int_array(state, int_buf, len(int_buf))
        >>>      result = stream.peek_end(state, result)
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_peek_int_array(self._stream if self._stream is not None else ffi.NULL, state,
                                                            ffi.from_buffer("t_int*", elements) if elements is not None else ffi.NULL,
                                                            num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def peek_long_array(self, state, elements, num_elements):
        """This function peeks ahead in the input stream to read an array of long (64-bit) integers
        from a client stream. It either peeks all of the array or none of it. If the stream has 
        been configured to swap bytes using `set_swap_bytes` then this function will 
        swap the order of the bytes within each element that it peeks before storing them in the 
        given buffer.

        The `peek_begin` function must be called to initialize the peek state. No data
        peeked will be removed from the input stream until `peek_end` is called. If
        `peek_end` is not called before the next `peek_begin` then the peeked
        data is read again.

        See the `peek_begin` function for more information and an example.

        The size of the stream receive buffer must be at least `num_elements` 64-bit integers
        in length.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function blocks until all the data is peeked. Blocking may occur because 
        data may be read from the underlying communication channel. However, the contents of 
        the stream buffer are never overwritten until `peek_end` is called to indicate 
        that the peeked data may be removed from the input stream.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. If fewer bytes are available then the size of
        the entire array then it returns ``-ErrorCode.WOULD_BLOCK``. In this case, the `poll`
        function may be used with the ``PollFlag.RECEIVE`` flag to determine when data becomes
        available. Otherwise it returns 1.

        If the connection has been closed gracefully then it returns 0 only if there are fewer
        64-bit integers left to peek than the size of the entire array. Otherwise it returns 1. Once
        there are fewer bytes left to peek than the size of the entire array then it will
        return 0 to indicate the connection has been closed. If an error occurs, then it returns 
        a negative error code.

        This function does not support two threads peeking data at the same time. However,
        data may be sent or the stream flushed by another thread at the same time as data is being
        peeked.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        state : t_stream_peek_state
            The peek state.
        elements : array_like
            A buffer of at least `num_elements` 64-bit integers in which the received data will be stored.
        num_elements : int
            The number of 64-bit integers available in the buffer.

        Returns
        -------
        result : int
            Returns 1 on success. If no more data is available and the connection has been closed gracefully,
            then it returns 0. If the method would block then it returns ``-ErrorCode.WOULD_BLOCK`` if the
            stream is non-blocking. If an error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_buf = array("b", [0 0 0])
        >>> long_buf = array("q", [0 0 0])
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", True, buffer_size, buffer_size)
        >>> try:
        >>>   prefetch = len(byte_buf) + 2 * len(long_buf)
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.peek_begin(prefetch)
        >>>      if result > 0:
        >>>         result = stream.peek_byte_array(state, byte_buf, len(byte_buf))
        >>>      if result > 0:
        >>>         result = stream.peek_long_array(state, long_buf, len(long_buf))
        >>>      result = stream.peek_end(state, result)
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_peek_long_array(self._stream if self._stream is not None else ffi.NULL, state,
                                                            ffi.from_buffer("t_long*", elements) if elements is not None else ffi.NULL,
                                                            num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def peek_single_array(self, state, elements, num_elements):
        """This function peeks ahead in the input stream to read an array of single-precision (32-bit) floats
        from a client stream. It either peeks all of the array or none of it. If the stream has 
        been configured to swap bytes using `set_swap_bytes` then this function will 
        swap the order of the bytes within each element that it peeks before storing them in the 
        given buffer.

        The `peek_begin` function must be called to initialize the peek state. No data
        peeked will be removed from the input stream until `peek_end` is called. If
        `peek_end` is not called before the next `peek_begin` then the peeked
        data is read again.

        See the `peek_begin` function for more information and an example.

        The size of the stream receive buffer must be at least `num_elements` 32-bit single-precision floats
        in length.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function blocks until all the data is peeked. Blocking may occur because 
        data may be read from the underlying communication channel. However, the contents of 
        the stream buffer are never overwritten until `peek_end` is called to indicate 
        that the peeked data may be removed from the input stream.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. If fewer bytes are available then the size of
        the entire array then it returns ``-ErrorCode.WOULD_BLOCK``. In this case, the `poll`
        function may be used with the ``PollFlag.RECEIVE`` flag to determine when data becomes
        available. Otherwise it returns 1.

        If the connection has been closed gracefully then it returns 0 only if there are fewer
        32-bit single-precision floats left to peek than the size of the entire array. Otherwise it returns 1. Once
        there are fewer bytes left to peek than the size of the entire array then it will
        return 0 to indicate the connection has been closed. If an error occurs, then it returns 
        a negative error code.

        This function does not support two threads peeking data at the same time. However,
        data may be sent or the stream flushed by another thread at the same time as data is being
        peeked.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        state : t_stream_peek_state
            The peek state.
        elements : array_like
            A buffer of at least `num_elements` 32-bit single-precision floats in which the received data will be stored.
        num_elements : int
            The number of 32-bit single-precision floats available in the buffer.

        Returns
        -------
        result : int
            Returns 1 on success. If no more data is available and the connection has been closed gracefully,
            then it returns 0. If the method would block then it returns ``-ErrorCode.WOULD_BLOCK`` if the
            stream is non-blocking. If an error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_buf = array("b", [0 0 0])
        >>> single_buf = array("f", [0 0 0])
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", True, buffer_size, buffer_size)
        >>> try:
        >>>   prefetch = len(byte_buf) + 2 * len(single_buf)
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.peek_begin(prefetch)
        >>>      if result > 0:
        >>>         result = stream.peek_byte_array(state, byte_buf, len(byte_buf))
        >>>      if result > 0:
        >>>         result = stream.peek_single_array(state, single_buf, len(single_buf))
        >>>      result = stream.peek_end(state, result)
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_peek_single_array(self._stream if self._stream is not None else ffi.NULL, state,
                                                             ffi.from_buffer("t_single*", elements) if elements is not None else ffi.NULL,
                                                             num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def peek_double_array(self, state, elements, num_elements):
        """This function peeks ahead in the input stream to read an array of double-precision (64-bit) floats
        from a client stream. It either peeks all of the array or none of it. If the stream has 
        been configured to swap bytes using `set_swap_bytes` then this function will 
        swap the order of the bytes within each element that it peeks before storing them in the 
        given buffer.

        The `peek_begin` function must be called to initialize the peek state. No data
        peeked will be removed from the input stream until `peek_end` is called. If
        `peek_end` is not called before the next `peek_begin` then the peeked
        data is read again.

        See the `peek_begin` function for more information and an example.

        The size of the stream receive buffer must be at least `num_elements` 64-bit double-precision floats
        in length.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function blocks until all the data is peeked. Blocking may occur because 
        data may be read from the underlying communication channel. However, the contents of 
        the stream buffer are never overwritten until `peek_end` is called to indicate 
        that the peeked data may be removed from the input stream.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. If fewer bytes are available then the size of
        the entire array then it returns ``-ErrorCode.WOULD_BLOCK``. In this case, the `poll`
        function may be used with the ``PollFlag.RECEIVE`` flag to determine when data becomes
        available. Otherwise it returns 1.

        If the connection has been closed gracefully then it returns 0 only if there are fewer
        64-bit double-precision floats left to peek than the size of the entire array. Otherwise it returns 1. Once
        there are fewer bytes left to peek than the size of the entire array then it will
        return 0 to indicate the connection has been closed. If an error occurs, then it returns 
        a negative error code.

        This function does not support two threads peeking data at the same time. However,
        data may be sent or the stream flushed by another thread at the same time as data is being
        peeked.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        state : t_stream_peek_state
            The peek state.
        elements : array_like
            A buffer of at least `num_elements` 64-bit double-precision floats in which the received data will be stored.
        num_elements : int
            The number of 64-bit double-precision floats available in the buffer.

        Returns
        -------
        result : int
            Returns 1 on success. If no more data is available and the connection has been closed gracefully,
            then it returns 0. If the method would block then it returns ``-ErrorCode.WOULD_BLOCK`` if the
            stream is non-blocking. If an error occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_buf = array("b", [0 0 0])
        >>> double_buf = array("d", [0 0 0])
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", True, buffer_size, buffer_size)
        >>> try:
        >>>   prefetch = len(byte_buf) + 2 * len(double_buf)
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.peek_begin(prefetch)
        >>>      if result > 0:
        >>>         result = stream.peek_byte_array(state, byte_buf, len(byte_buf))
        >>>      if result > 0:
        >>>         result = stream.peek_double_array(state, double_buf, len(double_buf))
        >>>      result = stream.peek_end(state, result)
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_peek_double_array(self._stream if self._stream is not None else ffi.NULL, state,
                                                             ffi.from_buffer("t_double*", elements) if elements is not None else ffi.NULL,
                                                             num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def poke_begin(self):
        """Prepares the `t_stream_poke_state` to begin poking data to the stream. "Poking" involves
        writing to the stream buffer without writing to the underlying communication channel or updating
        the buffer pointers. It is particularly useful for writing "atomic" data to the stream whose
        length is not known in advance, such as characters being converted to the underlying character
        format of the stream. The "poke state" is used to keep track of how much data has been poked
        into the stream so far.
 
        As an example of using the poke capabilities to write a sequence of data types as a single
        atomic unit using non-blocking I/O:

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", True, buffer_size, buffer_size)
        >>> try:
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.poke_begin()
        >>>      if result >= 0:
        >>>         result = stream.poke_int(state, 5)
        >>>      if result > 0:
        >>>         result = stream.poke_double(state, 3.14)
        >>>      result = stream.poke_end(state, result)
        >>>      if result > 0:
        >>>         result = stream.flush()
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        In this example, the code pokes an integer and a double into the output stream. The data
        is not transmitted over the underlying communication channel but is maintained in the
        stream buffer. If at any time the operation would block because there is not enough space
        in the stream buffer, then an exception is raised with error code ``-ErrorCode.WOULD_BLOCK``. 
        In this case, `poke_end` would not advance the output stream and the poked data would be 
        discarded and not sent to the output stream. Hence, the next time the code 
        is called it may write the same data again without the peer receiving two copies.

        However, if the `poke_int_array` and `poke_double_array` succeed then when `poke_end`
        advances the stream pointer. Hence, the data will be sent to the output stream the 
        next time the stream is flushed and subsequent sends/pokes to the stream will send new 
        data. In this case, `poke_end` returns one.

        Thus, the integer and double are sent as one atomic unit to the output stream, because
        if not enough space is available in the stream buffer, then nothing is written to the
        output stream. Only if both quantities are written successfully is the data actually 
        sent to the output stream.

        Note that the `poke_xxxx` functions may send data to the underlying communication
        channel (that remained from previous send operations), but the data being poked is never 
        sent until `poke_end` is called to indicate that the poked data may be sent to the 
        output stream.

        This function assumes that the stream is valid. It does not block because it does not
        access the underlying communication channel.

        Returns
        -------
        result : int
            Returns 0 on success or ``-ErrorCode.WOULD_BLOCK`` if it cannot flush earlier data in
            the stream send buffer to make space.
        state : t_stream_poke_state
            The initialized poke state.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        Suppose the following binary structure is being sent::

            struct {
                t_int8 temperature;
                t_uint8 status;
                t_int16 gyro_rates[3];
            }

        The code to send this structure as one atomic unit, while accounting for potential byte swapping
        due to byte order differences between server and client would be:

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> temperature = 25
        >>> status = 1
        >>> gyro_rates = array("h", [7 30 2])
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", True, buffer_size, buffer_size)
        >>> try:
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.poke_begin()
        >>>      if result >= 0:
        >>>         result = stream.poke_byte(state, temperature)
        >>>      if result > 0:
        >>>         result = stream.poke_byte(state, status)
        >>>      if result > 0:
        >>>         result = stream.poke_short_array(state, gyro_rates, len(gyro_rates))
        >>>      result = stream.poke_end(state, result)
        >>>      if result > 0:
        >>>         result = stream.flush()
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        state = ffi.new("t_stream_poke_state*")
        result = communications_lib.stream_poke_begin(self._stream if self._stream is not None else ffi.NULL,
                                                      state)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result, state

    def poke_end(self, state, status):
        """Finishes a "poke" operation by updating the stream buffer pointer so that all
        poked date is now marked as written to the streamm. It must be called after a 
        sequence of `poke_xxxx` operations to complete the poke. If this function is not 
        called before another `poke_begin` then the poked data is discarded from the
        stream buffer.

        This function assumes that the stream is valid. It does not block because it does not
        access the underlying communication channel.

        Parameters
        ----------
        state : t_stream_poke_state
            The "poke state" indicating how much data to add to the input stream.

        Returns
        -------
        result : int
            If the stream is shutdown or closed, an exception is raised. Otherwise it returns 1
            to indicate that the data was successfully written.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_buf = array("b", [0 0 0])
        >>> short_buf = array("h", [0 0 0])
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.poke_begin()
        >>>      if result >= 0:
        >>>         result = stream.poke_byte_array(state, byte_buf, len(byte_buf))
        >>>      if result > 0:
        >>>         result = stream.poke_short_array(state, short_buf, len(short_buf))
        >>>      result = stream.poke_end(state, result)
        >>>      if result > 0:
        >>>         result = stream.flush()
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        return communications_lib.stream_poke_end(self._stream if self._stream is not None else ffi.NULL, state, status)

    def poke_byte(self, state, data):
        """Writes a byte to the stream buffer. It attempts to store the byte in 
        the stream buffer. If there is enough room available in the stream buffer then it stores the
        data in the buffer and returns immediately. However, the stream pointer is not
        advanced, so the data is not written to the actual communication channel. The data
        will only be written to the underlying communication channel if `poke_end` is
        called. If an error occurs, then it raises an exception.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer (to write out data
        previously sent and still waiting in the stream buffer). Once the byte is poked into the
        buffer then 1 is returned. If an error occurs then an exception is raised and the 
        stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns 1 if the data is poked successfully. 
        If the byte could not be poked without blocking, then it returns ``ErrorCode.WOULD_BLOCK``.
        If an error occurs then an exception is raised and the stream should be closed.

        This function does not support two threads poking or flushing data at the same time.
        However, data may be poked or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        state : t_stream_poke_state
            The poke state.
        data : char
            The value to be poked.

        Returns
        -------
        result : int
            The number of bytes sent, which will always be 1. If the method would block then
            ``ErrorCode.WOULD_BLOCK`` is returned if the stream is non-blocking. If an error 
            occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_val = 123
        >>> short_buf = array("h", [4 5 6])
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.poke_begin()
        >>>      if result >= 0:
        >>>         result = stream.poke_byte(state, byte_val)
        >>>      if result > 0:
        >>>         result = stream.poke_short_array(state, short_buf, len(short_buf))
        >>>      result = stream.poke_end(state, result)
        >>>      if result > 0:
        >>>         result = stream.flush()
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_poke_byte(self._stream if self._stream is not None else ffi.NULL, state, data)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def poke_byte_array(self, state, elements, num_elements):
        """writes an array of bytes to the stream buffer. It attempts to store the
        bytes in the stream buffer. It either writes all of the array or none of it. 
        If there is enough room available in the stream buffer then it stores the data 
        in the buffer and returns immediately. However, the stream pointer is not
        advanced, so the data is not written to the actual communication channel. The data
        will only be written to the underlying communication channel if `poke_end` is
        called. If an error occurs, then an exception is raised.

        The size of the stream send buffer must be at least as large as `num_elements`
        bytes.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer (to write out data
        previously sent and still waiting in the stream buffer). Once the entire array is poked 
        into the buffer then 1 is returned. If an error occurs then an exception is raised
        and the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns 1 on success. If the entire array could not be 
        poked without blocking, then it returns with the error code ``-ErrorCode.WOULD_BLOCK``.
        If an error occurs then an exception is raised and the stream should be closed.

        This function does not support two threads poking or flushing data at the same time.
        However, data may be poked or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        state : t_stream_poke_state
            The poke state.
        elements : array_like
            A buffer of at least `num_elements` bytes in which the received data will be stored.
        num_elements : int
            The number of bytes from the `elements` array to poke.

        Returns
        -------
        result : int
            The number of bytes sent. If the method would block then
            ``ErrorCode.WOULD_BLOCK`` is returned if the stream is non-blocking. If an error 
            occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_buf = array("b", [3 2 1])
        >>> short_buf = array("h", [4 5 6])
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.poke_begin()
        >>>      if result >= 0:
        >>>         result = stream.poke_byte_array(state, byte_buf, len(byte_buf))
        >>>      if result > 0:
        >>>         result = stream.poke_short_array(state, short_buf, len(short_buf))
        >>>      result = stream.poke_end(state, result)
        >>>      if result > 0:
        >>>         result = stream.flush()
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_poke_byte_array(self._stream if self._stream is not None else ffi.NULL, state,
                                                           ffi.from_buffer(elements) if elements is not None else ffi.NULL,
                                                           num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def poke_short(self, state, data):
        """Writes a short 16-bit integer to the stream buffer. It attempts to 
        store the short integer in the stream buffer. If there is enough room available in the 
        stream buffer then it stores the data in the buffer and returns immediately. However, 
        the stream pointer is not advanced, so the data is not written to the actual communication 
        channel. The data will only be written to the underlying communication channel if 
        `poke_end` is called. If an error occurs, then it returns a negative error code. 

        If the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within the short integer when they are poked.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer (to write out data
        previously sent and still waiting in the stream buffer). Once the short integer is poked 
        into the buffer then 1 is returned. If an error occurs then an exception is raised and
        the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns 1 if the data is poked successfully. 
        If the short integer could not be poked without blocking, then ``-ErrorCode.WOULD_BLOCK`` is 
        returned. If an error occurs then an exception is raised and the stream should be 
        closed.

        This function does not support two threads poking or flushing data at the same time.
        However, data may be poked or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.


        Parameters
        ----------
        state : t_stream_poke_state
            The poke state.
        data : short
            The value to be poked.

        Returns
        -------
        result : int
            The number of 16-bit integers sent, which will always be 1. If the method would block then
            ``ErrorCode.WOULD_BLOCK`` is returned if the stream is non-blocking. If an error 
            occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_val = 123
        >>> short_val = 32000
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.poke_begin()
        >>>      if result >= 0:
        >>>         result = stream.poke_byte(state, byte_val)
        >>>      if result > 0:
        >>>         result = stream.poke_short(state, short_val)
        >>>      result = stream.poke_end(state, result)
        >>>      if result > 0:
        >>>         result = stream.flush()
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_poke_short(self._stream if self._stream is not None else ffi.NULL, state, data)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def poke_short_array(self, state, elements, num_elements):
        """writes an array of short 16-bit integers to the stream buffer. It attempts to store the
        short integers in the stream buffer. It either writes all of the array or none of it. 
        If there is enough room available in the stream buffer then it stores the data 
        in the buffer and returns immediately. However, the stream pointer is not
        advanced, so the data is not written to the actual communication channel. The data
        will only be written to the underlying communication channel if `poke_end` is
        called. If an error occurs, then an exception is raised.

        The size of the stream send buffer must be at least as large as `num_elements`
        16-bit integers.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer (to write out data
        previously sent and still waiting in the stream buffer). Once the entire array is poked 
        into the buffer then 1 is returned. If an error occurs then an exception is raised
        and the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns 1 on success. If the entire array could not be 
        poked without blocking, then it returns with the error code ``-ErrorCode.WOULD_BLOCK``.
        If an error occurs then an exception is raised and the stream should be closed.

        This function does not support two threads poking or flushing data at the same time.
        However, data may be poked or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        state : t_stream_poke_state
            The poke state.
        elements : array_like
            A buffer of at least `num_elements` 16-bit integers in which the received data will be stored.
        num_elements : int
            The number of 16-bit integers from the `elements` array to poke.

        Returns
        -------
        result : int
            The number of 16-bit integers sent. If the method would block then
            ``ErrorCode.WOULD_BLOCK`` is returned if the stream is non-blocking. If an error 
            occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_buf = array("b", [3 2 1])
        >>> short_buf = array("h", [4 5 6])
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.poke_begin()
        >>>      if result >= 0:
        >>>         result = stream.poke_short_array(state, byte_buf, len(byte_buf))
        >>>      if result > 0:
        >>>         result = stream.poke_short_array(state, short_buf, len(short_buf))
        >>>      result = stream.poke_end(state, result)
        >>>      if result > 0:
        >>>         result = stream.flush()
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_poke_short_array(self._stream if self._stream is not None else ffi.NULL, state,
                                                            ffi.from_buffer("const t_short*", elements) if elements is not None else ffi.NULL,
                                                            num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def poke_int(self, state, data):
        """Writes a 32-bit integer to the stream buffer. It attempts to 
        store the integer in the stream buffer. If there is enough room available in the 
        stream buffer then it stores the data in the buffer and returns immediately. However, 
        the stream pointer is not advanced, so the data is not written to the actual communication 
        channel. The data will only be written to the underlying communication channel if 
        `poke_end` is called. If an error occurs, then it returns a negative error code. 

        If the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within the integer when they are poked.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer (to write out data
        previously sent and still waiting in the stream buffer). Once the integer is poked 
        into the buffer then 1 is returned. If an error occurs then an exception is raised and
        the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns 1 if the data is poked successfully. 
        If the integer could not be poked without blocking, then ``-ErrorCode.WOULD_BLOCK`` is 
        returned. If an error occurs then an exception is raised and the stream should be 
        closed.

        This function does not support two threads poking or flushing data at the same time.
        However, data may be poked or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.


        Parameters
        ----------
        state : t_stream_poke_state
            The poke state.
        data : int
            The value to be poked.

        Returns
        -------
        result : int
            The number of 32-bit integers sent, which will always be 1. If the method would block then
            ``ErrorCode.WOULD_BLOCK`` is returned if the stream is non-blocking. If an error 
            occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_val = 123
        >>> int_val = 32000
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.poke_begin()
        >>>      if result >= 0:
        >>>         result = stream.poke_byte(state, byte_val)
        >>>      if result > 0:
        >>>         result = stream.poke_int(state, int_val)
        >>>      result = stream.poke_end(state, result)
        >>>      if result > 0:
        >>>         result = stream.flush()
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_poke_int(self._stream if self._stream is not None else ffi.NULL, state, data)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def poke_int_array(self, state, elements, num_elements):
        """writes an array of 32-bit integers to the stream buffer. It attempts to store the
        integers in the stream buffer. It either writes all of the array or none of it. 
        If there is enough room available in the stream buffer then it stores the data 
        in the buffer and returns immediately. However, the stream pointer is not
        advanced, so the data is not written to the actual communication channel. The data
        will only be written to the underlying communication channel if `poke_end` is
        called. If an error occurs, then an exception is raised.

        The size of the stream send buffer must be at least as large as `num_elements`
        32-bit integers.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer (to write out data
        previously sent and still waiting in the stream buffer). Once the entire array is poked 
        into the buffer then 1 is returned. If an error occurs then an exception is raised
        and the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns 1 on success. If the entire array could not be 
        poked without blocking, then it returns with the error code ``-ErrorCode.WOULD_BLOCK``.
        If an error occurs then an exception is raised and the stream should be closed.

        This function does not support two threads poking or flushing data at the same time.
        However, data may be poked or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        state : t_stream_poke_state
            The poke state.
        elements : array_like
            A buffer of at least `num_elements` 32-bit integers in which the received data will be stored.
        num_elements : int
            The number of 32-bit integers from the `elements` array to poke.

        Returns
        -------
        result : int
            The number of 32-bit integers sent. If the method would block then
            ``ErrorCode.WOULD_BLOCK`` is returned if the stream is non-blocking. If an error 
            occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_buf = array("b", [3 2 1])
        >>> int_buf = array("l", [4 5 6])
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.poke_begin()
        >>>      if result >= 0:
        >>>         result = stream.poke_int_array(state, byte_buf, len(byte_buf))
        >>>      if result > 0:
        >>>         result = stream.poke_int_array(state, int_buf, len(int_buf))
        >>>      result = stream.poke_end(state, result)
        >>>      if result > 0:
        >>>         result = stream.flush()
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_poke_int_array(self._stream if self._stream is not None else ffi.NULL, state,
                                                          ffi.from_buffer("const t_int*", elements) if elements is not None else ffi.NULL,
                                                          num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def poke_long(self, state, data):
        """Writes a long 64-bit integer to the stream buffer. It attempts to 
        store the long integer in the stream buffer. If there is enough room available in the 
        stream buffer then it stores the data in the buffer and returns immediately. However, 
        the stream pointer is not advanced, so the data is not written to the actual communication 
        channel. The data will only be written to the underlying communication channel if 
        `poke_end` is called. If an error occurs, then it returns a negative error code. 

        If the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within the long integer when they are poked.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer (to write out data
        previously sent and still waiting in the stream buffer). Once the long integer is poked 
        into the buffer then 1 is returned. If an error occurs then an exception is raised and
        the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns 1 if the data is poked successfully. 
        If the long integer could not be poked without blocking, then ``-ErrorCode.WOULD_BLOCK`` is 
        returned. If an error occurs then an exception is raised and the stream should be 
        closed.

        This function does not support two threads poking or flushing data at the same time.
        However, data may be poked or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.


        Parameters
        ----------
        state : t_stream_poke_state
            The poke state.
        data : long
            The value to be poked.

        Returns
        -------
        result : int
            The number of 64-bit integers sent, which will always be 1. If the method would block then
            ``ErrorCode.WOULD_BLOCK`` is returned if the stream is non-blocking. If an error 
            occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_val = 123
        >>> long_val = 32000
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.poke_begin()
        >>>      if result >= 0:
        >>>         result = stream.poke_byte(state, byte_val)
        >>>      if result > 0:
        >>>         result = stream.poke_long(state, long_val)
        >>>      result = stream.poke_end(state, result)
        >>>      if result > 0:
        >>>         result = stream.flush()
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_poke_long(self._stream if self._stream is not None else ffi.NULL, state, data)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def poke_long_array(self, state, elements, num_elements):
        """writes an array of long 64-bit integers to the stream buffer. It attempts to store the
        long integers in the stream buffer. It either writes all of the array or none of it. 
        If there is enough room available in the stream buffer then it stores the data 
        in the buffer and returns immediately. However, the stream pointer is not
        advanced, so the data is not written to the actual communication channel. The data
        will only be written to the underlying communication channel if `poke_end` is
        called. If an error occurs, then an exception is raised.

        The size of the stream send buffer must be at least as large as `num_elements`
        64-bit integers.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer (to write out data
        previously sent and still waiting in the stream buffer). Once the entire array is poked 
        into the buffer then 1 is returned. If an error occurs then an exception is raised
        and the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns 1 on success. If the entire array could not be 
        poked without blocking, then it returns with the error code ``-ErrorCode.WOULD_BLOCK``.
        If an error occurs then an exception is raised and the stream should be closed.

        This function does not support two threads poking or flushing data at the same time.
        However, data may be poked or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        state : t_stream_poke_state
            The poke state.
        elements : array_like
            A buffer of at least `num_elements` 64-bit integers in which the received data will be stored.
        num_elements : int
            The number of 64-bit integers from the `elements` array to poke.

        Returns
        -------
        result : int
            The number of 64-bit integers sent. If the method would block then
            ``ErrorCode.WOULD_BLOCK`` is returned if the stream is non-blocking. If an error 
            occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_buf = array("b", [3 2 1])
        >>> long_buf = array("q", [4 5 6])
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.poke_begin()
        >>>      if result >= 0:
        >>>         result = stream.poke_long_array(state, byte_buf, len(byte_buf))
        >>>      if result > 0:
        >>>         result = stream.poke_long_array(state, long_buf, len(long_buf))
        >>>      result = stream.poke_end(state, result)
        >>>      if result > 0:
        >>>         result = stream.flush()
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_poke_long_array(self._stream if self._stream is not None else ffi.NULL, state,
                                                           ffi.from_buffer("const t_long*", elements) if elements is not None else ffi.NULL,
                                                           num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def poke_single(self, state, data):
        """Writes a single-precision 32-bit float to the stream buffer. It attempts to 
        store the single-precision float in the stream buffer. If there is enough room available in the 
        stream buffer then it stores the data in the buffer and returns immediately. However, 
        the stream pointer is not advanced, so the data is not written to the actual communication 
        channel. The data will only be written to the underlying communication channel if 
        `poke_end` is called. If an error occurs, then it returns a negative error code. 

        If the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within the single-precision float when they are poked.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer (to write out data
        previously sent and still waiting in the stream buffer). Once the single-precision float is poked 
        into the buffer then 1 is returned. If an error occurs then an exception is raised and
        the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns 1 if the data is poked successfully. 
        If the single-precision float could not be poked without blocking, then ``-ErrorCode.WOULD_BLOCK`` is 
        returned. If an error occurs then an exception is raised and the stream should be 
        closed.

        This function does not support two threads poking or flushing data at the same time.
        However, data may be poked or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.


        Parameters
        ----------
        state : t_stream_poke_state
            The poke state.
        data : float
            The value to be poked.

        Returns
        -------
        result : int
            The number of 32-bit single-precision floats sent, which will always be 1. If the method would block then
            ``ErrorCode.WOULD_BLOCK`` is returned if the stream is non-blocking. If an error 
            occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_val = 123
        >>> single_val = 3.14
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.poke_begin()
        >>>      if result >= 0:
        >>>         result = stream.poke_byte(state, byte_val)
        >>>      if result > 0:
        >>>         result = stream.poke_single(state, single_val)
        >>>      result = stream.poke_end(state, result)
        >>>      if result > 0:
        >>>         result = stream.flush()
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_poke_single(self._stream if self._stream is not None else ffi.NULL, state, data)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def poke_single_array(self, state, elements, num_elements):
        """writes an array of single-precision 32-bit floats to the stream buffer. It attempts to store the
        single-precision floats in the stream buffer. It either writes all of the array or none of it. 
        If there is enough room available in the stream buffer then it stores the data 
        in the buffer and returns immediately. However, the stream pointer is not
        advanced, so the data is not written to the actual communication channel. The data
        will only be written to the underlying communication channel if `poke_end` is
        called. If an error occurs, then an exception is raised.

        The size of the stream send buffer must be at least as large as `num_elements`
        32-bit single-precision floats.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer (to write out data
        previously sent and still waiting in the stream buffer). Once the entire array is poked 
        into the buffer then 1 is returned. If an error occurs then an exception is raised
        and the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns 1 on success. If the entire array could not be 
        poked without blocking, then it returns with the error code ``-ErrorCode.WOULD_BLOCK``.
        If an error occurs then an exception is raised and the stream should be closed.

        This function does not support two threads poking or flushing data at the same time.
        However, data may be poked or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        state : t_stream_poke_state
            The poke state.
        elements : array_like
            A buffer of at least `num_elements` 32-bit single-precision floats in which the received data will be stored.
        num_elements : int
            The number of 32-bit single-precision floats from the `elements` array to poke.

        Returns
        -------
        result : int
            The number of 32-bit single-precision floats sent. If the method would block then
            ``ErrorCode.WOULD_BLOCK`` is returned if the stream is non-blocking. If an error 
            occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_buf = array("b", [3 2 1])
        >>> single_buf = array("f", [4 5 6])
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.poke_begin()
        >>>      if result >= 0:
        >>>         result = stream.poke_single_array(state, byte_buf, len(byte_buf))
        >>>      if result > 0:
        >>>         result = stream.poke_single_array(state, single_buf, len(single_buf))
        >>>      result = stream.poke_end(state, result)
        >>>      if result > 0:
        >>>         result = stream.flush()
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_poke_single_array(self._stream if self._stream is not None else ffi.NULL, state,
                                                             ffi.from_buffer("const t_single*", elements) if elements is not None else ffi.NULL,
                                                             num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def poke_double(self, state, data):
        """Writes a double-precision 64-bit float to the stream buffer. It attempts to 
        store the double-precision float in the stream buffer. If there is enough room available in the 
        stream buffer then it stores the data in the buffer and returns immediately. However, 
        the stream pointer is not advanced, so the data is not written to the actual communication 
        channel. The data will only be written to the underlying communication channel if 
        `poke_end` is called. If an error occurs, then it returns a negative error code. 

        If the stream has been configured to swap bytes using `set_swap_bytes` then
        this function will swap the order of the bytes within the double-precision float when they are poked.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer (to write out data
        previously sent and still waiting in the stream buffer). Once the double-precision float is poked 
        into the buffer then 1 is returned. If an error occurs then an exception is raised and
        the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns 1 if the data is poked successfully. 
        If the double-precision float could not be poked without blocking, then ``-ErrorCode.WOULD_BLOCK`` is 
        returned. If an error occurs then an exception is raised and the stream should be 
        closed.

        This function does not support two threads poking or flushing data at the same time.
        However, data may be poked or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.


        Parameters
        ----------
        state : t_stream_poke_state
            The poke state.
        data : float
            The value to be poked.

        Returns
        -------
        result : int
            The number of 64-bit double-precision floats sent, which will always be 1. If the method would block then
            ``ErrorCode.WOULD_BLOCK`` is returned if the stream is non-blocking. If an error 
            occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_val = 123
        >>> double_val = 3.14
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.poke_begin()
        >>>      if result >= 0:
        >>>         result = stream.poke_byte(state, byte_val)
        >>>      if result > 0:
        >>>         result = stream.poke_double(state, double_val)
        >>>      result = stream.poke_end(state, result)
        >>>      if result > 0:
        >>>         result = stream.flush()
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_poke_double(self._stream if self._stream is not None else ffi.NULL, state, data)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    def poke_double_array(self, state, elements, num_elements):
        """writes an array of double-precision 64-bit floats to the stream buffer. It attempts to store the
        double-precision floats in the stream buffer. It either writes all of the array or none of it. 
        If there is enough room available in the stream buffer then it stores the data 
        in the buffer and returns immediately. However, the stream pointer is not
        advanced, so the data is not written to the actual communication channel. The data
        will only be written to the underlying communication channel if `poke_end` is
        called. If an error occurs, then an exception is raised.

        The size of the stream send buffer must be at least as large as `num_elements`
        64-bit double-precision floats.

        If `listen` or `connect` was called with the non-blocking flag set to ``False`` (0),
        then this function may block attempting to flush the stream buffer (to write out data
        previously sent and still waiting in the stream buffer). Once the entire array is poked 
        into the buffer then 1 is returned. If an error occurs then an exception is raised
        and the stream should be closed.

        If `listen` or `connect` was called with the non-blocking flag set to ``True`` (1),
        then this function does not block. It returns 1 on success. If the entire array could not be 
        poked without blocking, then it returns with the error code ``-ErrorCode.WOULD_BLOCK``.
        If an error occurs then an exception is raised and the stream should be closed.

        This function does not support two threads poking or flushing data at the same time.
        However, data may be poked or the stream flushed by another thread at the same time as
        data is being received.

        The BSD socket API has no equivalent to this function.

        Parameters
        ----------
        state : t_stream_poke_state
            The poke state.
        elements : array_like
            A buffer of at least `num_elements` 64-bit double-precision floats in which the received data will be stored.
        num_elements : int
            The number of 64-bit double-precision floats from the `elements` array to poke.

        Returns
        -------
        result : int
            The number of 64-bit double-precision floats sent. If the method would block then
            ``ErrorCode.WOULD_BLOCK`` is returned if the stream is non-blocking. If an error 
            occurs, then an exception is raised.

        Raises
        ------
        StreamError
            On a negative return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------

        >>> from quanser.communications import Stream
        >>> buffer_size = 64
        >>> byte_buf = array("b", [3 2 1])
        >>> double_buf = array("d", [4 5 6])
        >>> stream = Stream()
        >>> stream.connect("tcpip://localhost:5000", False, buffer_size, buffer_size)
        >>> try:
        >>>   while stream.poll(None, PollFlag.RECEIVE) > 0:
        >>>      result, state = stream.poke_begin()
        >>>      if result >= 0:
        >>>         result = stream.poke_double_array(state, byte_buf, len(byte_buf))
        >>>      if result > 0:
        >>>         result = stream.poke_double_array(state, double_buf, len(double_buf))
        >>>      result = stream.poke_end(state, result)
        >>>      if result > 0:
        >>>         result = stream.flush()
        >>>      if result >= 0:
        >>>         break
        ...
        >>>   stream.shutdown()
        >>> finally:
        >>>   stream.close()

        """
        result = communications_lib.stream_poke_double_array(self._stream if self._stream is not None else ffi.NULL, state,
                                                             ffi.from_buffer("const t_double*", elements) if elements is not None else ffi.NULL,
                                                             num_elements)

        if result < 0 and result != -ErrorCode.WOULD_BLOCK:
            raise StreamError(result)

        return result

    # endregion

# endregion
