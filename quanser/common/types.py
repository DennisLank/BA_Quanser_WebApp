import os
import math

from cffi import FFI

# region Setup

ffi = FFI()
ffi.cdef("""

/* Type Definitions */

typedef char                t_boolean;
typedef signed int          t_int;
typedef signed long long    t_long;
typedef double              t_double;

typedef t_int               t_int32;
typedef t_int               t_error;

typedef struct tag_timeout
{
    t_long    seconds;
    t_int     nanoseconds;
    t_boolean is_absolute;
} t_timeout;

t_timeout* timeout_get_timeout(t_timeout * timeout, double time_value);
t_boolean timeout_is_negative(const t_timeout * timeout);
t_boolean timeout_is_zero(const t_timeout * timeout);
t_boolean timeout_is_expired(const t_timeout * timeout);
t_error timeout_get_absolute(t_timeout * result, const t_timeout * timeout);
t_error timeout_get_relative(t_timeout * result, const t_timeout * timeout);
t_int timeout_compare(const t_timeout * left, const t_timeout * right);
t_error timeout_subtract(t_timeout * result, const t_timeout * left, const t_timeout * right);
t_error timeout_add(t_timeout * result, const t_timeout * left, const t_timeout * right);
t_error timeout_get_current_time(t_timeout * time);
t_error timeout_get_high_resolution_time(t_timeout * time);
t_error timeout_get_thread_cpu_time(t_timeout * time);
t_error timeout_get_process_cpu_time(t_timeout * time);
t_error timeout_get_milliseconds(t_int32 * milliseconds, const t_timeout * timeout);

""")

# Invoke set_source so this FFI can be included in another FFI
ffi.set_source("_main", "")

common_lib = ffi.dlopen("quanser_common")

# endregion

class Timeout :
    """A class for dealing with timeouts. Note that Timeouts support addition and subtraction,
    as well as comparisons There are also a number of class methods for creating Timeouts and
    three read-only properties: seconds, nanoseconds and is_absolute.

    Parameters
    ----------
    seconds : int
        The seconds portion of the timeout.
    nanoseconds : int
        The nanoseconds portion of the timeout.
    is_absolute : boolean
        Indicates whether the timeout is a relative timeout or an absolute timeout.

    Examples
    --------
    Create a 20-second timeout

    >>> from quanser.common import Timeout
    >>> timeout = Timeout(20)

    Create a 2000-nanosecond timeout

    >>> from quanser.common import Timeout
    >>> timeout = Timeout(nanoseconds = 2000)

    Create a 1.02 second absolute timeout

    >>> from quanser.common import Timeout
    >>> timeout = Timeout(1, 20000000, True)

    """
    def __init__(self, seconds = 0, nanoseconds = 0, is_absolute = False):
        if isinstance(seconds, ffi.CData):
            self._timeout = seconds
        else:
            if (seconds < 0 and nanoseconds > 0) or (seconds > 0 and nanoseconds < 0):
                nanoseconds = -nanoseconds  # nanoseconds should have same sign as seconds

            self._timeout = ffi.new("t_timeout *")
            self._timeout.seconds = seconds
            self._timeout.nanoseconds = nanoseconds
            self._timeout.is_absolute = b'\x01' if is_absolute else b'\x00'

    @classmethod
    def get_timeout(cls, interval):
        """
        Get a relative Timeout instance from a time interval in seconds (including fractional seconds). A negative
        interval will result in a zero Timeout.

        Parameters
        ----------
        interval : float
            A non-negative time interval in seconds (including fractional seconds) to be represented by the Timeout instance.

        Returns
        -------
        timeout : Timeout
            The relative Timeout instance representing the same number of seconds (including fractional seconds)

        Example
        -------
        Creating a relative Timeout of 1.5 seconds:

        >>> timeout = Timeout.get_timeout(1.5)
        """
        timeout = ffi.new("t_timeout*")
        common_lib.timeout_get_timeout(timeout, interval)
        return cls(timeout)

    @classmethod
    def get_current_time(cls):
        """
        Get the current time as an absolute Timeout instance. On some platforms, this function
        may not return as much resolution as Timeout.get_high_resolution_time().

        Raises
        ------
        GenericError
            An exception is raised if the current time cannot be obtained.

        Returns
        -------
        timeout : Timeout
            An absolute Timeout instance representing the current time.

        Example
        -------
        Getting the current time:

        >>> timeout = Timeout.get_current_time()
        """
        timeout = ffi.new("t_timeout*")
        result = common_lib.timeout_get_current_time(timeout)
        if result < 0:
            raise GenericError(result)
        return cls(timeout)

    @classmethod
    def get_high_resolution_time(cls):
        """
        Get the current time as an absolute Timeout instance with the highest resolution. On some platforms,
        this method may be more expensive than Timeout.get_current_time().

        Raises
        ------
        GenericError
            An exception is raised if the current high-resolution time cannot be obtained.

        Returns
        -------
        timeout : Timeout
            An absolute Timeout instance representing the current time with the highest resolution.

        Example
        -------
        Getting the current time as a high-resolution time:

        >>> timeout = Timeout.get_high_resolution_time()
        """
        timeout = ffi.new("t_timeout*")
        result = common_lib.timeout_get_high_resolution_time(timeout)
        if result < 0:
            raise GenericError(result)
        return cls(timeout)

    @classmethod
    def get_thread_cpu_time(cls):
        """
        Get the current thread CPU time as a relative Timeout instance.

        Raises
        ------
        GenericError
            An exception is raised if the thread CPU time cannot be obtained.

        Returns
        -------
        timeout : Timeout
            A relative Timeout instance representing the current thread CPU time.

        Example
        -------
        Getting the current thread CPU time:

        >>> timeout = Timeout.get_thread_cpu_time()
        """
        timeout = ffi.new("t_timeout*")
        result = common_lib.timeout_get_thread_cpu_time(timeout)
        if result < 0:
            raise GenericError(result)
        return cls(timeout)

    @classmethod
    def get_process_cpu_time(cls):
        """
        Get the current process CPU time as a relative Timeout instance.

        Raises
        ------
        GenericError
            An exception is raised if the process CPU time cannot be obtained.

        Returns
        -------
        timeout : Timeout
            A relative Timeout instance representing the current process CPU time.

        Example
        -------
        Getting the current process CPU time:

        >>> timeout = Timeout.get_process_cpu_time()
        """
        timeout = ffi.new("t_timeout*")
        result = common_lib.timeout_get_process_cpu_time(timeout)
        if result < 0:
            raise GenericError(result)
        return cls(timeout)

    def set_timeout(self, interval):
        """
        Set the value of this Timeout instance to a relative time representing the given time interval in seconds 
        (including fractional seconds).

        Parameters
        ----------
        interval : float
            The time interval in seconds (including fractional seconds) to be represented by the Timeout instance.

        Example
        -------
        Setting a relative Timeout of 1.5 seconds:

        >>> timeout = Timeout()
        >>> timeout.set_timeout(1.5)
        """
        common_lib.timeout_get_timeout(self._timeout, interval)

    def set_current_time(self):
        """
        Set the value of this Timeout instance to the current time as an absolute Timeout. On some platforms, this function
        may not return as much resolution as Timeout.set_high_resolution_time().

        Raises
        ------
        GenericError
            An exception is raised if the current time cannot be obtained.

        Example
        -------
        Setting the current time:

        >>> timeout = Timeout()
        >>> timeout.set_current_time()
        """
        result = common_lib.timeout_get_current_time(self._timeout)
        if result < 0:
            raise GenericError(result)

    def set_high_resolution_time(self):
        """
        Set the value of this Timeout instance as a relative Timeout representing the current time with the highest resolution. 
        On some platforms, this method may be more expensive than Timeout.set_current_time().

        Raises
        ------
        GenericError
            An exception is raised if the current high-resolution time cannot be obtained.

        Example
        -------
        Setting the current time as a high-resolution time:

        >>> timeout = Timeout()
        >>> timeout.get_high_resolution_time()
        """
        result = common_lib.timeout_get_high_resolution_time(self._timeout)
        if result < 0:
            raise GenericError(result)

    def set_thread_cpu_time(self):
        """
        Set the value of this Timeout as a relative Timeout respresenting the current thread CPU time.

        Raises
        ------
        GenericError
            An exception is raised if the thread CPU time cannot be obtained.

        Example
        -------
        Setting the current thread CPU time:

        >>> timeout = Timeout()
        >>> timeout.get_thread_cpu_time()
        """
        result = common_lib.timeout_get_thread_cpu_time(self._timeout)
        if result < 0:
            raise GenericError(result)

    def set_process_cpu_time(self):
        """
        Set the value of this Timeout as a relative Timeout respresenting the current process CPU time.

        Raises
        ------
        GenericError
            An exception is raised if the process CPU time cannot be obtained.

        Example
        -------
        Setting the current process CPU time:

        >>> timeout = Timeout()
        >>> timeout.get_process_cpu_time()
        """
        result = common_lib.timeout_get_process_cpu_time(self._timeout)
        if result < 0:
            raise GenericError(result)

    @property
    def seconds(self):
        """
        Get the number of seconds stored in the Timeout instance.

        Example
        -------
        Get the seconds portion of the Timeout.

        >>> timeout = Timeout.get_timeout(2.5)
        >>> secs = timeout.seconds    # secs = 2
        """
        return self._timeout.seconds

    @property
    def nanoseconds(self):
        """
        Get the number of nanoseconds stored in the Timeout instance.

        Example
        -------
        Get the nanoseconds portion of the Timeout.

        >>> timeout = Timeout.get_timeout(2.5)
        >>> nsecs = timeout.nanoseconds    # nsecs = 500000000
        """
        return self._timeout.nanoseconds

    @property
    def is_absolute(self):
        """
        Determine whether the Timeout is absolute or relative.

        Example
        -------
        See if the Timeout is absolute or not:

        >>> timeout = Timeout.get_timeout(2.5)
        >>> absolute = timeout.is_absolute    # absolute = False
        """
        return (self._timeout.is_absolute != b'\x00')

    def is_negative(self):
        """
        Indicates whether the Timeout is negative or not.

        Example
        -------
        See if the Timeout is negative or not:

        >>> timeout = Timeout.get_timeout(-2)
        >>> neg = timeout.is_negative()    # neg = True
        """
        return (common_lib.timeout_is_negative(self._timeout) != b'\x00')

    def is_zero(self):
        """
        Indicates whether the Timeout is zero or not.

        Example
        -------
        See if the Timeout is zero or not:

        >>> timeout = Timeout()
        >>> zero = timeout.is_zero()    # zero = True
        """
        return (common_lib.timeout_is_zero(self._timeout) != b'\x00')

    def is_expired(self):
        """
        Indicates whether the Timeout has already expired. Absolute timeouts are
        compared to the current time. Relative timeouts are expired if they are
        negative or zero.

        Example
        -------
        See if the Timeout has expired or not:

        >>> timeout = Timeout.get_current_time()
        >>> relative = Timeout(1)
        >>> timeout += relative
        >>> expired = timeout.is_expired()    # expired = False
        """
        return (common_lib.timeout_is_expired(self._timeout) != b'\x00')

    def get_absolute(self):
        """
        Gets an absolute Timeout from the given relative Timeout.

        Raises
        ------
        GenericError
            An exception is raised if the conversion cannot be performed.

        Example
        -------
        Get the absolute time five seconds from now:

        >>> timeout = Timeout(5)
        >>> abs_timeout = timeout.get_absolute()
        """
        abs_timeout = ffi.new("t_timeout*")
        result = common_lib.timeout_get_absolute(abs_timeout, self._timeout)
        if result < 0:
            raise GenericError(result)
        return Timeout(abs_timeout)

    def get_relative(self):
        """
        Gets a relative Timeout from the given absolute Timeout.

        Raises
        ------
        GenericError
            An exception is raised if the conversion cannot be performed.

        Example
        -------
        Get the relative time from the given absolute Timeout to the current time:

        >>> rel_timeout = abs_timeout.get_relative()
        """
        rel_timeout = ffi.new("t_timeout*")
        result = common_lib.timeout_get_relative(rel_timeout, self._timeout)
        if result < 0:
            raise GenericError(result)
        return Timeout(rel_timeout)

    def compare(self, rhs):
        """
        Compares two Timeouts and returns -1 if the left-hand side is less than the right-hand side,
        zero if the two Timeouts are equal and +1 if the left-hand side is greater than the rigt-hand
        side.

        Raises
        ------
        GenericError
            An exception is raised if the comparison cannot be performed.

        Example
        -------
        Compares two Timeouts:

        >>> timeout = Timeout.get_current_time()
        >>> interval = Timeout(5)
        >>> other_timeout = timeout + interval
        >>> cmp = timeout.compare(other_timeout) # cmp = -1
        """
        return common_lib.timeout_compare(self._timeout, rhs._timeout)

    def get_milliseconds(self):
        """
        Returns the total number of milliseconds represented by the Timeout as an integer.

        Raises
        ------
        GenericError
            An exception is raised if the number of milliseconds cannot be determined.

        Example
        -------
        Get the total number of milliseconds represented by the Timeout:

        >>> timeout = Timeout.get_timeout(1.5)
        >>> ms = timeout.get_milliseconds() # ms = 1500
        """
        milliseconds = ffi.new("t_int32*")
        result = common_lib.timeout_get_milliseconds(milliseconds, self._timeout)
        if result < 0:
            raise GenericError(result)
        return milliseconds[0]

    def __sub__(self, rhs):
        """
        Subtracts one Timeout from another as the subtraction operator.

        Raises
        ------
        GenericError
            An exception is raised if the subtraction cannot be performed.

        Example
        -------
        Get the time between two absolute Timeouts:

        >>> start = Timeout.get_current_time()
        >>> ...
        >>> stop = Timeout.get_current_time()
        >>> elapsed = stop - start
        """
        diff_timeout = ffi.new("t_timeout*")
        result = common_lib.timeout_subtract(diff_timeout, self._timeout, rhs._timeout)
        if result < 0:
            raise GenericError(result)
        return Timeout(diff_timeout)

    def __isub__(self, rhs):
        """
        Subtracts one Timeout from another in-place as the -= operator.

        Raises
        ------
        GenericError
            An exception is raised if the subtraction cannot be performed.

        Example
        -------
        Get the time between two absolute Timeouts:

        >>> start = Timeout.get_current_time()
        >>> ...
        >>> elapsed = Timeout.get_current_time()
        >>> elapsed -= start
        """
        result = common_lib.timeout_subtract(self._timeout, self._timeout, rhs._timeout)
        if result < 0:
            raise GenericError(result)
        return self

    def __add__(self, rhs):
        """
        Adds one Timeout to another as the addition operator.

        Raises
        ------
        GenericError
            An exception is raised if the subtraction cannot be performed.

        Example
        -------
        Add five seconds to the current time.

        >>> start = Timeout.get_current_time()
        >>> interval = Timeout(5)
        >>> stop = start + interval
        """
        sum_timeout = ffi.new("t_timeout*")
        result = common_lib.timeout_add(sum_timeout, self._timeout, rhs._timeout)
        if result < 0:
            raise GenericError(result)
        return Timeout(sum_timeout)

    def __iadd__(self, rhs):
        """
        Adds one Timeout to another in-place as the += operator.

        Raises
        ------
        GenericError
            An exception is raised if the subtraction cannot be performed.

        Example
        -------
        Add five seconds to the current time.

        >>> stop = Timeout.get_current_time()
        >>> interval = Timeout(5)
        >>> stop += interval
        """
        result = common_lib.timeout_add(self._timeout, self._timeout, rhs._timeout)
        if result < 0:
            raise GenericError(result)
        return self

    def __eq__(self, rhs):
        """
        Compares two Timeouts for equality.

        Raises
        ------
        GenericError
            An exception is raised if the subtraction cannot be performed.

        Example
        -------
        Compare two Timeouts:

        >>> start = Timeout.get_current_time()
        >>> stop = Timeout.get_current_time()
        >>> same = (start == stop)
        """
        return (self.compare(rhs) == 0)

    def __lt__(self, rhs):
        """
        Implements the less-than operator.

        Raises
        ------
        GenericError
            An exception is raised if the subtraction cannot be performed.

        Example
        -------
        Compare two Timeouts:

        >>> start = Timeout.get_current_time()
        >>> stop = Timeout.get_current_time()
        >>> same = (start < stop)
        """
        return (self.compare(rhs) < 0)

    def __le__(self, rhs):
        """
        Implements the less-than or equal-to operator.

        Raises
        ------
        GenericError
            An exception is raised if the subtraction cannot be performed.

        Example
        -------
        Compare two Timeouts:

        >>> start = Timeout.get_current_time()
        >>> stop = Timeout.get_current_time()
        >>> same = (start <= stop)
        """
        return (self.compare(rhs) <= 0)

    def __ge__(self, rhs):
        """
        Implements the greater-than or equal-to operator.

        Raises
        ------
        GenericError
            An exception is raised if the subtraction cannot be performed.

        Example
        -------
        Compare two Timeouts:

        >>> start = Timeout.get_current_time()
        >>> stop = Timeout.get_current_time()
        >>> same = (start >= stop)
        """
        return (self.compare(rhs) >= 0)

    def __gt__(self, rhs):
        """
        Implements the greater-than operator.

        Raises
        ------
        GenericError
            An exception is raised if the subtraction cannot be performed.

        Example
        -------
        Compare two Timeouts:

        >>> start = Timeout.get_current_time()
        >>> stop = Timeout.get_current_time()
        >>> same = (start > stop)
        """
        return (self.compare(rhs) > 0)

    def __str__(self):
        """
        Converts the Timeout to a string for printing. Absolute timeouts are prefixed with the '@' symbol.

        Raises
        ------
        GenericError
            An exception is raised if the subtraction cannot be performed.

        Example
        -------
        Print the value of the relative Timeout:

        >>> timeout = Timeout.get_timeout(1.5)
        >>> print("Timeout:", timeout) # Prints 1.500000000
        """
        if self._timeout.is_absolute != b'\x00':
            prefix = "@"
        else:
            prefix = ""

        if self.is_negative():
            return "{:s}-{:d}.{:09d}".format(prefix, -self._timeout.seconds, -self._timeout.nanoseconds)
        else:
            return "{:s}{:d}.{:09d}".format(prefix, self._timeout.seconds, self._timeout.nanoseconds)
