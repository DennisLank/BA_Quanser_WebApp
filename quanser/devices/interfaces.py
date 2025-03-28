import sys
import os
import struct

from cffi import FFI

from quanser.devices import LCDAccess, RangingDistance, RangingMeasurementMode, RangingMeasurements, DeviceError

def add_common_path():
    if (sys.version_info[0] > 3) or ((sys.version_info[0] == 3) and (sys.version_info[1] >= 8)):
        common_dir = os.getenv("CommonProgramFiles") # TODO: will not work when 32-bit python being run on 64-bit Windows!
        if common_dir != None:
            bin_dir = os.path.join(common_dir, "Quanser", "bin")
            if os.path.isdir(bin_dir):
                os.add_dll_directory(bin_dir)

# region Setup


ffi = FFI()
ffi.cdef("""
    /* Type Definitions */
    
    typedef unsigned char   t_ubyte;    /* must always be 8 bits */
    typedef t_ubyte         t_uint8;
    typedef t_uint8         t_boolean;
    typedef unsigned short  t_uint16;   /* must always be 16 bits */
    typedef signed int      t_int;      /* must always be 32 bits */
    typedef unsigned int    t_uint;     /* must always be 32 bits */
    typedef t_uint          t_uint32;
    typedef t_int           t_error;
    typedef double          t_double;
    typedef float           t_single;
    typedef unsigned char   t_ubyte;

    typedef struct tag_game_controller * t_game_controller;
    typedef struct tag_ranging_sensor * t_ranging_sensor;
    typedef struct tag_st7032 * t_st7032;
    typedef struct tag_st7066u * t_st7066u;
    typedef struct tag_ws0010*  t_ws0010;
    typedef struct tag_ls012b7dd01* t_ls012b7dd01;
    typedef struct tag_ls027b7dh01* t_ls027b7dh01;
    typedef struct tag_aaaf5050_mc_k12* t_aaaf5050_mc_k12;

    typedef enum tag_ranging_sensor_type
    {
        RANGING_SENSOR_TYPE_INVALID,        /* Invalid sensor type */
        RANGING_SENSOR_TYPE_VL53L0,         /* ST Microelectronics VL53L0 time-of-flight sensor */
        RANGING_SENSOR_TYPE_VL53L1,         /* ST Microelectronics VL53L1 time-of-flight sensor */
        RANGING_SENSOR_TYPE_RPLIDAR,        /* Slamtec RPLidar 2D LIDAR sensor */
        RANGING_SENSOR_TYPE_YDLIDAR,        /* YDLIDAR 2D LIDAR sensor */
        RANGING_SENSOR_TYPE_MS10,           /* Leishen MS10 LIDAR sensor */
        RANGING_SENSOR_TYPE_M10P,           /* Leishen M10P LIDAR sensor */

        NUMBER_OF_RANGING_SENSOR_TYPES = RANGING_SENSOR_TYPE_M10P
    } t_ranging_sensor_type;

    typedef enum tag_ranging_distance
    {
        RANGING_DISTANCE_SHORT,
        RANGING_DISTANCE_MEDIUM,
        RANGING_DISTANCE_LONG,
    
        NUMBER_OF_RANGING_DISTANCES
    } t_ranging_distance;
    
    typedef enum tag_ranging_measurement_mode
    {
        RANGING_MEASUREMENT_MODE_NORMAL,        /* return actual measurement data. Number of measurements will vary and angles will not be consistent between scans. Angles will start close to zero. */
        RANGING_MEASUREMENT_MODE_INTERPOLATED,  /* returns the number of measurements, N, requested. Angles will start at zero and be 360/N apart. Raw measurements will be interpolated to estimate distance at each angle */
        
        NUMBER_OF_RANGING_MEASUREMENT_MODES
    } t_ranging_measurement_mode;
    
    typedef struct tag_ranging_measurement
    {
        t_double distance;          /* the distance in metres */
        t_double distance_sigma;    /* an estimate of the standard deviation in the current distance measurement */
        t_double heading;           /* the heading in radians (will be zero for 1D ranging sensors) */
        t_uint8 quality;            /* an indication of the quality of the measurement (0 to 100%) */
    } t_ranging_measurement;
    
    typedef struct tag_game_controller_states
    {
        t_single x;                 /* x-coordinate as a percentage of the range. Spans -1.0 to 1.0 */
        t_single y;                 /* y-coordinate as a percentage of the range. Spans -1.0 to 1.0 */
        t_single z;                 /* z-coordinate as a percentage of the range. Spans -1.0 to 1.0 */
        t_single rx;                /* rx-coordinate as a percentage of the range. Spans -1.0 to 1.0 */
        t_single ry;                /* ry-coordinate as a percentage of the range. Spans -1.0 to 1.0 */
        t_single rz;                /* rz-coordinate as a percentage of the range. Spans -1.0 to 1.0 */
        t_single sliders[2];        /* sliders as a percentage of the range. Spans 0.0 to 1.0 */
        t_single point_of_views[4]; /* point-of-view positions (in positive radians or -1 = centred). */
        t_uint32 buttons;           /* state of each of 32 buttons. If the bit corresponding to the button is 0 the button is released. If it is 1 then the button is pressed */
    } t_game_controller_states;

    typedef enum tag_lcd_access
    {
        LCD_ACCESS_SHARED,              /* multiple processes can access the LCD at the same time but hold a global mutex while actually writing to the display. Waits for mutex to be released */
        LCD_ACCESS_ASYNCHRONOUS,        /* multiple processes can access the LCD at the same time but hold a global mutex while actually writing to the display. Skips write if mutex already held by another process */
        LCD_ACCESS_EXCLUSIVE            /* only one process can access the LCD at a time (global mutex is held as long as the LCD is open) */
    } t_lcd_access;

    typedef struct tag_led_color
    {
        t_uint8 red;
        t_uint8 green;
        t_uint8 blue;
    } t_led_color;

    /* LIDAR Methods */
    
    t_error rplidar_open(const char * uri, t_ranging_distance range, t_ranging_sensor * sensor);
    
    t_int rplidar_read(t_ranging_sensor sensor, t_ranging_measurement_mode mode, t_double maximum_interpolated_distance,
                       t_double maximum_interpolated_angle, t_ranging_measurement * measurements, t_uint num_measurements);

    t_error rplidar_close(t_ranging_sensor sensor);

    /* YDLIDAR 2D LIDAR Sensors */

    t_error ydlidar_open(const char* uri, t_uint samples_per_scan, t_ranging_sensor* sensor);

    t_int ydlidar_read(t_ranging_sensor sensor, t_ranging_measurement_mode mode, t_double maximum_interpolated_distance, t_double maximum_interpolated_angle,
        t_ranging_measurement* measurements, t_uint num_measurements);

    t_error ydlidar_close(t_ranging_sensor sensor);

    /* Leishen MS10 2D LIDAR Sensors */

    t_error leishen_ms10_open(const char* uri, t_uint samples_per_scan, t_ranging_sensor* sensor);

    t_int leishen_ms10_read(t_ranging_sensor sensor, t_ranging_measurement_mode mode, t_double maximum_interpolated_distance, t_double maximum_interpolated_angle,
        t_ranging_measurement* measurements, t_uint num_measurements);

    t_error leishen_ms10_close(t_ranging_sensor sensor);

    /* Leishen M10P 2D LIDAR Sensors */

    t_error leishen_m10p_open(const char* uri, t_uint samples_per_scan, t_ranging_sensor* sensor);

    t_int leishen_m10p_read(t_ranging_sensor sensor, t_ranging_measurement_mode mode, t_double maximum_interpolated_distance, t_double maximum_interpolated_angle,
    t_ranging_measurement* measurements, t_uint num_measurements);

    t_error leishen_m10p_close(t_ranging_sensor sensor);

    /* LCD ST7032Display Methods */
    
    t_error st7032_open(const char * uri, t_st7032 * display);

    t_error st7032_close(t_st7032 display);

    t_int st7032_print(t_st7032 display, t_uint line, t_uint column, const char * message, size_t length);

    t_error st7032_set_character(t_st7032 display, t_int code, const t_uint8 pattern[8]);

    /* LCD ST7066UDisplay Methods */
    
    t_error st7066u_open(const char * uri, t_st7066u * display);

    t_error st7066u_close(t_st7066u display);

    t_int st7066u_print(t_st7066u display, t_uint line, t_uint column, const char * message, size_t length);

    t_error st7066u_set_character(t_st7066u display, t_int code, const t_uint8 pattern[8]);
    
    /* LCD Sharp LS012B7DD01 */

    t_error ls012b7dd01_open(const char* uri, t_ls012b7dd01* display);

    t_int ls012b7dd01_print(t_ls012b7dd01 display, t_uint line, t_uint column, const char* message, size_t length);

    t_int ls012b7dd01_wprint(t_ls012b7dd01 display, t_uint line, t_uint column, const wchar_t* message, size_t length);

    t_error ls012b7dd01_set_character(t_ls012b7dd01 display, t_int code, const t_uint16 pattern[16]);

    t_error ls012b7dd01_set_inversion(t_ls012b7dd01 display, t_boolean invert);

    t_error ls012b7dd01_set_rotation(t_ls012b7dd01 display, t_boolean rotation);

    t_error ls012b7dd01_draw_image(t_ls012b7dd01 display, t_int pixel_row, t_int pixel_column, t_uint image_width, t_uint image_height, const t_uint8* image);

    t_error ls012b7dd01_close(t_ls012b7dd01 display);

    /* LCD Sharp LS027B7DH01 */

    t_error ls027b7dh01_open(const char* uri, t_lcd_access access, t_ls027b7dh01* display);

    t_error ls027b7dh01_begin_draw(t_ls027b7dh01 display);

    t_error ls027b7dh01_end_draw(t_ls027b7dh01 display);

    t_int ls027b7dh01_print(t_ls027b7dh01 display, t_uint line, t_uint column, const char* message, size_t length);

    t_int ls027b7dh01_wprint(t_ls027b7dh01 display, t_uint line, t_uint column, const wchar_t* message, size_t length);

    t_error ls027b7dh01_set_character(t_ls027b7dh01 display, t_int code, const t_uint16 pattern[20]);

    t_error ls027b7dh01_set_inversion(t_ls027b7dh01 display, t_boolean invert);

    t_error ls027b7dh01_set_rotation(t_ls027b7dh01 display, t_boolean rotate);

    t_error ls027b7dh01_draw_image(t_ls027b7dh01 display, t_int pixel_row, t_int pixel_column, t_uint image_width, t_uint image_height, const t_uint8* image);

    t_error ls027b7dh01_save_display(t_ls027b7dh01 display, const char* filename);

    t_error ls027b7dh01_close(t_ls027b7dh01 display);

    /* LCD WS0010Display Methods */
    
    t_error ws0010_open(const char * uri, t_ws0010 * display);

    t_error ws0010_close(t_ws0010 display);

    t_int ws0010_print(t_ws0010 display, t_uint line, t_uint column, const char * message, size_t length);

    t_error ws0010_set_character(t_ws0010 display, t_int code, const t_uint8 pattern[8]);

    /* Game Controller methods */

    /* If max_force_feedback_effects == 0 then not f/f. */
    t_error game_controller_open(t_uint8 controller_number, t_uint16 buffer_size, t_double deadzone[6], t_double saturation[6], t_boolean auto_center,
                                 t_uint16 max_force_feedback_effects, t_double force_feedback_gain, t_game_controller * game_controller);
    t_error game_controller_poll(t_game_controller controller, t_game_controller_states * state, t_boolean * is_new);
    t_error game_controller_close(t_game_controller controller); 

    /* LED strip */
    t_error aaaf5050_mc_k12_open(const char* uri, t_uint max_leds, t_aaaf5050_mc_k12* led_handle);
    t_int aaaf5050_mc_k12_write(t_aaaf5050_mc_k12 led_handle, const t_led_color* colors, t_uint num_leds);
    t_error aaaf5050_mc_k12_close(t_aaaf5050_mc_k12 led_handle);

""")

add_common_path()
devices_lib = ffi.dlopen("quanser_devices")

# endregion

# region Constants

_WOULD_BLOCK = 34

_CHAR_ARRAY = "char[]"
_UINT8_ARRAY = "t_uint8[]"
_UINT16_ARRAY = "t_uint16[]"

_RANGING_MEASUREMENT_ARRAY = "t_ranging_measurement[]"

# endregion

# region Device Classes


class RPLIDAR:
    """A Python wrapper for the Quanser Devices API interface to RPLIDAR ranging sensors.

    Example
    -------
    >>> from quanser.devices import RPLIDAR
    >>> lidar = RPLIDAR()

    """

    # region Life Cycle

    def __init__(self):
        self._lidar = None

    # endregion

    # region Implementation

    def close(self):
        """Closes the current open RPLIDAR device.

        Example
        -------

        >>> from quanser.devices import RPLIDAR, RangingDistance
        >>> lidar = RPLIDAR()
        >>> lidar.open("serial-cpu://localhost:2?baud='115200',word='8',parity='none',stop='1',flow='none',dsr='on'",
        ...            RangingDistance.SHORT)
        ... ...
        ...
        >>> lidar.close()

        """
        if self._lidar is None:
            return

        result = devices_lib.rplidar_close(self._lidar if self._lidar is not None else ffi.NULL)
        if result < 0:
            raise DeviceError(result)

        self._lidar = None

    def open(self, uri, ranging_distance):
        """Opens the specified RPLIDAR device with the given parameters.

        Parameters
        ----------
        uri : string
            A URI used for communicating with the device. Numerous URI parameters are available.
        ranging_distance : RangingDistance
            The type of ranging distance. Valid values are ``RangingDistance.SHORT``, ``RangingDistance.MEDIUM``, and
            ``RangingDistance.LONG``.

        Example
        -------

        >>> from quanser.devices import RPLIDAR, RangingDistance
        >>> lidar = RPLIDAR()
        >>> lidar.open("serial-cpu://localhost:2?baud='115200',word='8',parity='none',stop='1',flow='none',dsr='on'",
        ...            RangingDistance.LONG)
        ... ...
        ...
        >>> lidar.close()

        """
        if self._lidar is not None:
            self.close()

        lidar = ffi.new("t_ranging_sensor *")

        result = devices_lib.rplidar_open(uri.encode("UTF-8") if uri is not None else ffi.NULL,
                                          ranging_distance,
                                          lidar if lidar is not None else ffi.NULL)
        if result < 0:
            raise DeviceError(result)

        self._lidar = lidar[0]

    def read(self, mode, max_interpolated_distance, max_interpolated_angle, measurements):
        """Reads LIDAR data from the ranging sensor.

        Parameters
        ----------
        mode : RangingMeasurementMode
            The measurement mode, which determines how the scan data is returned.

            When the measurement mode is ``RangingMeasurementMode.NORMAL``, the "raw" sensor readings from the LIDAR are
            returned (but the values are scaled to the SI units expected). In this case, the number of measurements may
            vary and the angles may not be consistent between scans. Furthermore, while the angles will be in ascending
            order, the first angle may not be zero. It will, however, be close to zero. If the size of the
            `measurements` buffer provided is not large enough, then a ``-QERR_BUFFER_TOO_SMALL`` error will be raised.
            In this case, the function may be called again with a larger buffer.

            When the measurement mode is ``RangingMeasurementMode.INTERPOLATED``, the raw sensor readings from the LIDAR
            are not returned. Instead, the number of "measurements" requested will be returned, in which the angles are
            360/N degrees apart (in radians), where N is the number of measurements requested and the first angle is
            zero. The distances will be interpolated from the raw data, as will the standard deviation and quality.
            Interpolation is only performed between two consecutive valid readings. The advantage of this mode is that
            the angles are always consistent, as are the number of measurements, so the data is easier to process in
            Simulink.
        max_interpolated_distance : float
            In interpolation mode, this is the maximum difference between the distance measurement of contiguous samples
            for which interpolation will be used. Beyond this difference, the distance of the sample with the closest
            angle to the desired heading will be used.
        max_interpolated_angle : float
            In interpolation mode, this is the maximum difference between the angle measurement of contiguous samples
            for which interpolation will be used. Beyond this difference, the distance and quality will be set to zero.
        measurements : RangingMeasurements
            A buffer in which the actual measurement data is stored.

        Return Value
        ------------

        Returns the number of valid measurements. The result may be zero, indicating that no new measurements
        were available.

        Notes
        -----
        If the quality is zero, then it indicates an invalid measurement (no reflected laser pulse).
        
        To efficiently access an array using numpy, use the frombuffer function to wrap the array with
        a numpy array. For example:

        >>> buffer = array.array('i', [0]*7200))
        >>> numpy.frombuffer(buffer)

        Examples
        --------
        Continuously read 100 samples of 720 measurements in normal mode.

        >>> from quanser.devices import RPLIDAR, RangingMeasurements, RangingMeasurementMode
        >>> num_measurements = 720
        >>> measurements = RangingMeasurements(num_measurments)
        >>> lidar = RPLIDAR()
        >>> lidar.open("serial-cpu://localhost:2?baud='115200',word='8',parity='none',stop='1',flow='none',dsr='on'",
        ...            RangingDistance.LONG)
        >>> for i in range(100):
        ...     lidar.read(RangingMeasurementMode.NORMAL, 0.0, 0.0, measurements)
        ...     ...
        ...
        >>> lidar.close()

        Continuously read 100 samples, consisting of measurements every half degree, in interpolated mode.

        >>> from quanser.devices import RPLIDAR, RangingMeasurements, RangingMeasurementMode
        >>> num_measurements = 720
        >>> measurements = RangingMeasurements(num_measurements)
        >>> lidar = RPLIDAR()
        >>> lidar.open("serial-cpu://localhost:2?baud='115200',word='8',parity='none',stop='1',flow='none',dsr='on'",
        ...            RangingDistance.LONG)
        >>> for i in range(100):
        ...     lidar.read(RangingMeasurementMode.INTERPOLATED, 0.05, 0.1, measurements)
        ...     ...
        ...
        >>> lidar.close()

        """

        num_measurements = sys.maxsize
        if measurements.distance is not None:
            num_measurements = len(measurements.distance)
        if measurements.distance_sigma is not None:
            num_measurements = min(num_measurements, len(measurements.distance_sigma))
        if measurements.heading is not None:
            num_measurements = min(num_measurements, len(measurements.heading))
        if measurements.quality is not None:
            num_measurements = min(num_measurements, len(measurements.quality))
        if num_measurements == sys.maxsize:
            raise DeviceError(-4) # -QERR_INVALID_ARGUMENT

        measurement_buffer = ffi.new("t_ranging_measurement[%d]" % num_measurements)

        result = devices_lib.rplidar_read(self._lidar if self._lidar is not None else ffi.NULL,
                                          mode, max_interpolated_distance, max_interpolated_angle,
                                          measurement_buffer, num_measurements)
        if (result > 0):
            measurements.length = result;
            for i in range(0, result):
                if measurements.distance is not None:
                    measurements.distance[i] = measurement_buffer[i].distance
                if measurements.distance_sigma is not None:
                    measurements.distance_sigma[i] = measurement_buffer[i].distance_sigma
                if measurements.heading is not None:
                    measurements.heading[i] = measurement_buffer[i].heading
                if measurements.quality is not None:
                    measurements.quality[i] = measurement_buffer[i].quality

        if result == -34: # -QERR_WOULD_BLOCK
            result = 0 # indicate no data read
        elif result < 0:
            raise DeviceError(result)

        # Return number of measurements read. May be zero
        return result

    # endregion

class LeishenMS10:
    """A Python wrapper for the Quanser Devices API interface to Leishen MS10 ranging sensors.

    Example
    -------
    >>> from quanser.devices import LeishenMS10
    >>> lidar = LeishenMS10()

    """

    # region Life Cycle

    def __init__(self):
        self._lidar = None

    # endregion

    # region Implementation

    def close(self):
        """Closes the current open LeishenMS10 device.

        Example
        -------

        >>> from quanser.devices import LeishenMS10
        >>> lidar = LeishenMS10()
        >>> lidar.open("serial-cpu://localhost:2?baud='460800',word='8',parity='none',stop='1',flow='none'")
        ... ...
        ...
        >>> lidar.close()

        """
        if self._lidar is None:
            return

        result = devices_lib.leishen_ms10_close(self._lidar if self._lidar is not None else ffi.NULL)
        if result < 0:
            raise DeviceError(result)

        self._lidar = None

    def open(self, uri, samples_per_scan = 1008):
        """Opens the specified Leishen MS10 LIDAR with the given parameters.

        Parameters
        ----------
        uri : string
            A URI used for communicating with the device. Numerous URI parameters are available.
        samples_per_scan : int
            The number of samples per scan. This value defaults to 1008.

        Example
        -------

        >>> from quanser.devices import LeishenMS10
        >>> lidar = LeishenMS10()
        >>> lidar.open("serial-cpu://localhost:2?baud='460800',word='8',parity='none',stop='1',flow='none'")
        ... ...
        ...
        >>> lidar.close()

        """
        if self._lidar is not None:
            self.close()

        lidar = ffi.new("t_ranging_sensor *")

        result = devices_lib.leishen_ms10_open(uri.encode("UTF-8") if uri is not None else ffi.NULL,
                                          samples_per_scan,
                                          lidar if lidar is not None else ffi.NULL)
        if result < 0:
            raise DeviceError(result)

        self._lidar = lidar[0]

    def read(self, mode, max_interpolated_distance, max_interpolated_angle, measurements):
        """Reads LIDAR data from the ranging sensor.

        Parameters
        ----------
        mode : RangingMeasurementMode
            The measurement mode, which determines how the scan data is returned.

            When the measurement mode is ``RangingMeasurementMode.NORMAL``, the "raw" sensor readings from the LIDAR are
            returned (but the values are scaled to the SI units expected). In this case, the number of measurements may
            vary and the angles may not be consistent between scans. Furthermore, while the angles will be in ascending
            order, the first angle may not be zero. It will, however, be close to zero. If the size of the
            `measurements` buffer provided is not large enough, then a ``-QERR_BUFFER_TOO_SMALL`` error will be raised.
            In this case, the function may be called again with a larger buffer.

            When the measurement mode is ``RangingMeasurementMode.INTERPOLATED``, the raw sensor readings from the LIDAR
            are not returned. Instead, the number of "measurements" requested will be returned, in which the angles are
            360/N degrees apart (in radians), where N is the number of measurements requested and the first angle is
            zero. The distances will be interpolated from the raw data, as will the standard deviation and quality.
            Interpolation is only performed between two consecutive valid readings. The advantage of this mode is that
            the angles are always consistent, as are the number of measurements, so the data is easier to process in
            Simulink.
        max_interpolated_distance : float
            In interpolation mode, this is the maximum difference between the distance measurement of contiguous samples
            for which interpolation will be used. Beyond this difference, the distance of the sample with the closest
            angle to the desired heading will be used.
        max_interpolated_angle : float
            In interpolation mode, this is the maximum difference between the angle measurement of contiguous samples
            for which interpolation will be used. Beyond this difference, the distance and quality will be set to zero.
        measurements : RangingMeasurements
            A buffer in which the actual measurement data is stored.

        Return Value
        ------------

        Returns the number of valid measurements. The result may be zero, indicating that no new measurements
        were available.

        Notes
        -----
        If the quality is zero, then it indicates an invalid measurement (no reflected laser pulse).
        
        To efficiently access an array using numpy, use the frombuffer function to wrap the array with
        a numpy array. For example:

        >>> buffer = array.array('i', [0]*7200))
        >>> numpy.frombuffer(buffer)

        Examples
        --------
        Continuously read 100 samples of 720 measurements in normal mode.

        >>> from quanser.devices import LeishenMS10, RangingMeasurements, RangingMeasurementMode
        >>> num_measurements = 1008
        >>> measurements = RangingMeasurements(num_measurments)
        >>> lidar = LeishenMS10()
        >>> lidar.open("serial-cpu://localhost:2?baud='460800',word='8',parity='none',stop='1',flow='none'")
        >>> for i in range(100):
        ...     lidar.read(RangingMeasurementMode.NORMAL, 0.0, 0.0, measurements)
        ...     ...
        ...
        >>> lidar.close()

        Continuously read 100 samples, consisting of measurements every half degree, in interpolated mode.

        >>> from quanser.devices import LeishenMS10, RangingMeasurements, RangingMeasurementMode
        >>> num_measurements = 720
        >>> measurements = RangingMeasurements(num_measurements)
        >>> lidar = LeishenMS10()
        >>> lidar.open("serial-cpu://localhost:2?baud='460800',word='8',parity='none',stop='1',flow='none'")
        >>> for i in range(100):
        ...     lidar.read(RangingMeasurementMode.INTERPOLATED, 0.05, 0.1, measurements)
        ...     ...
        ...
        >>> lidar.close()

        """

        num_measurements = sys.maxsize
        if measurements.distance is not None:
            num_measurements = len(measurements.distance)
        if measurements.distance_sigma is not None:
            num_measurements = min(num_measurements, len(measurements.distance_sigma))
        if measurements.heading is not None:
            num_measurements = min(num_measurements, len(measurements.heading))
        if measurements.quality is not None:
            num_measurements = min(num_measurements, len(measurements.quality))
        if num_measurements == sys.maxsize:
            raise DeviceError(-4) # -QERR_INVALID_ARGUMENT

        measurement_buffer = ffi.new("t_ranging_measurement[%d]" % num_measurements)

        result = devices_lib.leishen_ms10_read(self._lidar if self._lidar is not None else ffi.NULL,
                                               mode, max_interpolated_distance, max_interpolated_angle,
                                               measurement_buffer, num_measurements)
        if (result > 0):
            measurements.length = result;
            for i in range(0, result):
                if measurements.distance is not None:
                    measurements.distance[i] = measurement_buffer[i].distance
                if measurements.distance_sigma is not None:
                    measurements.distance_sigma[i] = measurement_buffer[i].distance_sigma
                if measurements.heading is not None:
                    measurements.heading[i] = measurement_buffer[i].heading
                if measurements.quality is not None:
                    measurements.quality[i] = measurement_buffer[i].quality

        if result == -34: # -QERR_WOULD_BLOCK
            result = 0 # indicate no data read
        elif result < 0:
            raise DeviceError(result)

        # Return number of measurements read. May be zero
        return result

    # endregion

class LeishenM10P:
    """A Python wrapper for the Quanser Devices API interface to Leishen M10P ranging sensors.

    Example
    -------
    >>> from quanser.devices import LeishenM10P
    >>> lidar = LeishenM10P()

    """

    # region Life Cycle

    def __init__(self):
        self._lidar = None

    # endregion

    # region Implementation

    def close(self):
        """Closes the current open LeishenM10P device.

        Example
        -------

        >>> from quanser.devices import LeishenM10P
        >>> lidar = LeishenM10P()
        >>> lidar.open("serial://localhost:0?device='/dev/lidar',baud='512000',word='8',parity='none',stop='1',flow='none'")
        ... ...
        ...
        >>> lidar.close()

        """
        if self._lidar is None:
            return

        result = devices_lib.leishen_m10p_close(self._lidar if self._lidar is not None else ffi.NULL)
        if result < 0:
            raise DeviceError(result)

        self._lidar = None

    def open(self, uri, samples_per_scan = 1680):
        """Opens the specified Leishen M10P LIDAR with the given parameters.

        Parameters
        ----------
        uri : string
            A URI used for communicating with the device. Numerous URI parameters are available.
        samples_per_scan : int
            The number of samples per scan. This value defaults to 1680.

        Example
        -------

        >>> from quanser.devices import LeishenM10P
        >>> lidar = LeishenM10P()
        >>> lidar.open("serial://localhost:0?device='/dev/lidar',baud='512000',word='8',parity='none',stop='1',flow='none'")
        ... ...
        ...
        >>> lidar.close()

        """
        if self._lidar is not None:
            self.close()

        lidar = ffi.new("t_ranging_sensor *")

        result = devices_lib.leishen_m10p_open(uri.encode("UTF-8") if uri is not None else ffi.NULL,
                                          samples_per_scan,
                                          lidar if lidar is not None else ffi.NULL)
        if result < 0:
            raise DeviceError(result)

        self._lidar = lidar[0]

    def read(self, mode, max_interpolated_distance, max_interpolated_angle, measurements):
        """Reads LIDAR data from the ranging sensor.

        Parameters
        ----------
        mode : RangingMeasurementMode
            The measurement mode, which determines how the scan data is returned.

            When the measurement mode is ``RangingMeasurementMode.NORMAL``, the "raw" sensor readings from the LIDAR are
            returned (but the values are scaled to the SI units expected). In this case, the number of measurements may
            vary and the angles may not be consistent between scans. Furthermore, while the angles will be in ascending
            order, the first angle may not be zero. It will, however, be close to zero. If the size of the
            `measurements` buffer provided is not large enough, then a ``-QERR_BUFFER_TOO_SMALL`` error will be raised.
            In this case, the function may be called again with a larger buffer.

            When the measurement mode is ``RangingMeasurementMode.INTERPOLATED``, the raw sensor readings from the LIDAR
            are not returned. Instead, the number of "measurements" requested will be returned, in which the angles are
            360/N degrees apart (in radians), where N is the number of measurements requested and the first angle is
            zero. The distances will be interpolated from the raw data, as will the standard deviation and quality.
            Interpolation is only performed between two consecutive valid readings. The advantage of this mode is that
            the angles are always consistent, as are the number of measurements, so the data is easier to process in
            Simulink.
        max_interpolated_distance : float
            In interpolation mode, this is the maximum difference between the distance measurement of contiguous samples
            for which interpolation will be used. Beyond this difference, the distance of the sample with the closest
            angle to the desired heading will be used.
        max_interpolated_angle : float
            In interpolation mode, this is the maximum difference between the angle measurement of contiguous samples
            for which interpolation will be used. Beyond this difference, the distance and quality will be set to zero.
        measurements : RangingMeasurements
            A buffer in which the actual measurement data is stored.

        Return Value
        ------------

        Returns the number of valid measurements. The result may be zero, indicating that no new measurements
        were available.

        Notes
        -----
        If the quality is zero, then it indicates an invalid measurement (no reflected laser pulse).
        
        To efficiently access an array using numpy, use the frombuffer function to wrap the array with
        a numpy array. For example:

        >>> buffer = array.array('i', [0]*7200))
        >>> numpy.frombuffer(buffer)

        Examples
        --------
        Continuously read 100 samples of 1680 measurements in normal mode.

        >>> from quanser.devices import LeishenM10P, RangingMeasurements, RangingMeasurementMode
        >>> num_measurements = 1680
        >>> measurements = RangingMeasurements(num_measurments)
        >>> lidar = LeishenM10P()
        >>> lidar.open("serial://localhost:0?device='/dev/lidar',baud='512000',word='8',parity='none',stop='1',flow='none'")
        >>> for i in range(100):
        ...     lidar.read(RangingMeasurementMode.NORMAL, 0.0, 0.0, measurements)
        ...     ...
        ...
        >>> lidar.close()

        Continuously read 100 samples, consisting of measurements every half degree, in interpolated mode.

        >>> from quanser.devices import LeishenM10P, RangingMeasurements, RangingMeasurementMode
        >>> num_measurements = 720
        >>> measurements = RangingMeasurements(num_measurements)
        >>> lidar = LeishenM10P()
        >>> lidar.open("serial://localhost:0?device='/dev/lidar',baud='512000',word='8',parity='none',stop='1',flow='none'")
        >>> for i in range(100):
        ...     lidar.read(RangingMeasurementMode.INTERPOLATED, 0.05, 0.1, measurements)
        ...     ...
        ...
        >>> lidar.close()

        """

        num_measurements = sys.maxsize
        if measurements.distance is not None:
            num_measurements = len(measurements.distance)
        if measurements.distance_sigma is not None:
            num_measurements = min(num_measurements, len(measurements.distance_sigma))
        if measurements.heading is not None:
            num_measurements = min(num_measurements, len(measurements.heading))
        if measurements.quality is not None:
            num_measurements = min(num_measurements, len(measurements.quality))
        if num_measurements == sys.maxsize:
            raise DeviceError(-4) # -QERR_INVALID_ARGUMENT

        measurement_buffer = ffi.new("t_ranging_measurement[%d]" % num_measurements)

        result = devices_lib.leishen_m10p_read(self._lidar if self._lidar is not None else ffi.NULL,
                                               mode, max_interpolated_distance, max_interpolated_angle,
                                               measurement_buffer, num_measurements)
        if (result > 0):
            measurements.length = result;
            for i in range(0, result):
                if measurements.distance is not None:
                    measurements.distance[i] = measurement_buffer[i].distance
                if measurements.distance_sigma is not None:
                    measurements.distance_sigma[i] = measurement_buffer[i].distance_sigma
                if measurements.heading is not None:
                    measurements.heading[i] = measurement_buffer[i].heading
                if measurements.quality is not None:
                    measurements.quality[i] = measurement_buffer[i].quality

        if result == -34: # -QERR_WOULD_BLOCK
            result = 0 # indicate no data read
        elif result < 0:
            raise DeviceError(result)

        # Return number of measurements read. May be zero
        return result

    # endregion

class ST7032Display:
    """A Python wrapper for the Quanser Devices API interface to Sitronix ST7032 displays.

    Example
    -------
    >>> from quanser.devices import ST7032Display
    >>> display = ST7032Display()

    """
    # region Life Cycle

    def __init__(self):        
        self._display = None

    # endregion

    # region Implementation

    def open(self, uri):
        """Opens the ST7032 (or NewHaven NHD-C0216C0Z) display.

        Example
        -------

        >>> from quanser.devices import ST7032Display
        >>> display = ST7032Display()
        >>> display.open("i2c-cpu://localhost:8?address=0x3E,baud=400000")
        >>> ...
        ...
        >>> display.close()

        """
        display = ffi.new("t_st7032 *")
        result = devices_lib.st7032_open(uri.encode("UTF-8") if uri is not None else ffi.NULL, display)

        if result < 0:
            raise DeviceError(result)
            
        self._display = display[0]

    def close(self):
        """Close the display.

        Example
        -------

        >>> from quanser.devices import ST7032Display
        >>> display = ST7032Display()
        >>> display.open("i2c-cpu://localhost:8?address=0x3E,baud=400000")
        >>> ...
        ...        
        >>> display.close()

        """
        result = devices_lib.st7032_close(self._display if self._display is not None else ffi.NULL)

        if result < 0:
            raise DeviceError(result)

        self._display = None

    def printText(self, line, column, message, length):
        """Print to the display. 

        Parameters
        ----------
        line : int
            The line where the message will be displayed. Line 0 is the first line.
            
        column : int
            The column where the message will be displayed. Column 0 is the first column.
        
        message : string
            The message to display. Unrecognized characters are skipped. If more than 16 characters would be printed on 
            a line then the line is truncated. A newline will cause the characters to be displayed on the next line. 
            As there are only two lines on the display there should only be one newline in the format string. 
            Printing starts at the given line and column. Line 0 is the first line and column 0 is the first column. 

            The format string is UTF-8 and does support Unicode (particularly, Katakana characters).
                        
        length : int
            The length of the `message`.

        Example
        -------
        Print 'Hello, World!' to the top, left corner of the display.

        >>> from quanser.devices import ST7032Display
        >>> display = ST7032Display()
        >>> display.open("i2c-cpu://localhost:8?address=0x3E,baud=400000")
        >>> message = "Hello, world!"
        >>> display.printText(0, 0, message, len(message))
        >>> ...
        ...
        >>> display.close()

        """

        result = devices_lib.st7032_print(self._display if self._display is not None else ffi.NULL,
                                          line, column,
                                          message.encode("UTF-8") if message is not None else ffi.NULL,
                                          length)

        if result < 0:
            raise DeviceError(result)

    def setCharacter(self, code, pattern):
        """Defines the character associated with the given character code. 

        Parameters
        ----------
        code : int
            Defines the character associated with the given character code. 
            Valid character codes are 0x10 to 0x17 i.e., '\020' to '\027'. Using these characters will produce the bitmap 
            defined in the pattern for that character.
            
        pattern : bytes
            The pattern defines each line of the character being defined, with the five bits in each byte defining the pixels of that line.
            For example to define the letter T, the pattern would be:

            pattern = b'\x1F\x40\x40\x40\x40\x40\x40\x00'

            0b00011111 (\x1F)
            0b00000100 (\x40)
            0b00000100 (\x40)
            0b00000100 (\x40)
            0b00000100 (\x40)
            0b00000100 (\x40)
            0b00000100 (\x40)
            0b00000000 (\x00) <= should generally be zero to allow for cursor
            Note that only bits 0-4 are used. Bit 0 is the rightmost pixel and bit 4 is the leftmost pixel. 
        
        Examples
        --------
        Print a custom character with three lines along the top, middle and bottom. 

        >>> from quanser.devices import ST7032Display
        >>> display = ST7032Display()
        >>> display.open("i2c-cpu://localhost:8?address=0x3E,baud=400000")
        >>> character_code = 0o20
        >>> pattern = b'\x1F\x00\x00\x1F\x00\x00\x1F\x00'
        >>> display.setCharacter(character_code, pattern)
        >>> message = str(chr(character_code))
        >>> display.printText(0, 0, message, len(message))
        >>> ...
        ...
        >>> display.close()

        Print a pair of custom characters that give the appearance of a wifi signal strength indicator.

        >>> from quanser.devices import ST7032Display
        >>> display = ST7032Display()
        >>> display.open("i2c-cpu://localhost:8?address=0x3E,baud=400000")
        >>> character_code_left = 0o20
        >>> pattern_left = b'\x00\x00\x00\x01\x05\x15\x15\x15'
        >>> character_code_right = 0o21        
        >>> pattern_right = b'\x01\x05\x15\x15\x15\x15\x15\x15'
        >>> display.setCharacter(character_code_left, pattern_left)
        >>> display.setCharacter(character_code_right, pattern_right)
        >>> message = str(chr(character_code_left)) + str(chr(character_code_right))
        >>> display.printText(1, 1, message, len(message))
        >>> ...
        ...
        >>> display.close()

        """       
        result = devices_lib.st7032_set_character(self._display if self._display is not None else ffi.NULL,
                                                  code, pattern)
    
        if result < 0:
            raise DeviceError(result)

    # endregion

class ST7066UDisplay:
    """A Python wrapper for the Quanser Devices API interface to Sitronix ST7066U displays.

    Example
    -------
    >>> from quanser.devices import ST7066UDisplay
    >>> display = ST7066UDisplay()

    """
    # region Life Cycle

    def __init__(self):
        self._display = None

    # endregion

    # region Implementation

    def open(self, uri):
        """Opens the ST7066U (or NewHaven NHD-C0216C0Z) display.

        Example
        -------

        >>> from quanser.devices import ST7066UDisplay
        >>> display = ST7066UDisplay()
        >>> display.open("serial://qbot3:0?baud=115200,device='/dev/qbot3_lcd'")
        >>> ...
        ...
        >>> display.close()

        """
        display = ffi.new("t_st7066u *")
        result = devices_lib.st7066u_open(uri.encode("UTF-8") if uri is not None else ffi.NULL, display)

        if result < 0:
            raise DeviceError(result)
            
        self._display = display[0]

    def close(self):
        """Close the display.

        Example
        -------

        >>> from quanser.devices import ST7066UDisplay
        >>> display = ST7066UDisplay()
        >>> display.open("serial://qbot3:0?baud=115200,device='/dev/qbot3_lcd'")
        >>> ...
        ...        
        >>> display.close()

        """
        result = devices_lib.st7066u_close(self._display if self._display is not None else ffi.NULL)

        if result < 0:
            raise DeviceError(result)

        self._display = None

    def printText(self, line, column, message, length):
        """Print to the display. 

        Parameters
        ----------
        line : int
            The line where the message will be displayed. Line 0 is the first line.
            
        column : int
            The column where the message will be displayed. Column 0 is the first column.
        
        message : string
            The message to display. Unrecognized characters are skipped. If more than 16 characters would be printed on 
            a line then the line is truncated. A newline will cause the characters to be displayed on the next line. 
            As there are only two lines on the display there should only be one newline in the format string. 
            Printing starts at the given line and column. Line 0 is the first line and column 0 is the first column. 

            The format string is UTF-8 and does support Unicode (particularly, Katakana characters).
                        
        length : int
            The length of the `message`.

        Example
        -------
        Print 'Hello, World!' to the top, left corner of the display.

        >>> from quanser.devices import ST7066UDisplay
        >>> display = ST7066UDisplay()
        >>> display.open("serial://qbot3:0?baud=115200,device='/dev/qbot3_lcd'")
        >>> message = "Hello, world!"
        >>> display.printText(0, 0, message, len(message))
        >>> ...
        ...
        >>> display.close()

        """

        result = devices_lib.st7066u_print(self._display if self._display is not None else ffi.NULL,
                                          line, column,
                                          message.encode("UTF-8") if message is not None else ffi.NULL,
                                          length)

        if result < 0:
            raise DeviceError(result)

    def setCharacter(self, code, pattern):
        """Defines the character associated with the given character code. 

        Parameters
        ----------
        code : int
            Defines the character associated with the given character code. 
            Valid character codes are 0x10 to 0x17 i.e., '\020' to '\027'. Using these characters will produce the bitmap 
            defined in the pattern for that character.
            
        pattern : bytes
            The pattern defines each line of the character being defined, with the five bits in each byte defining the pixels of that line.
            For example to define the letter T, the pattern would be:

            pattern = b'\x1F\x40\x40\x40\x40\x40\x40\x00'

            0b00011111 (\x1F)
            0b00000100 (\x40)
            0b00000100 (\x40)
            0b00000100 (\x40)
            0b00000100 (\x40)
            0b00000100 (\x40)
            0b00000100 (\x40)
            0b00000000 (\x00) <= should generally be zero to allow for cursor

            Note that only bits 0-4 are used. Bit 0 is the rightmost pixel and bit 4 is the leftmost pixel. 
        
        Examples
        --------
        Print a custom character with three lines along the top, middle and bottom. 

        >>> from quanser.devices import ST7066UDisplay
        >>> display = ST7066UDisplay()
        >>> display.open("serial://qbot3:0?baud=115200,device='/dev/qbot3_lcd'")
        >>> character_code = 0o20
        >>> pattern = b'\x1F\x00\x00\x1F\x00\x00\x1F\x00'
        >>> display.setCharacter(character_code, pattern)
        >>> message = str(chr(character_code))
        >>> display.printText(0, 0, message, len(message))
        >>> ...
        ...
        >>> display.close()

        Print a pair of custom characters that give the appearance of a wifi signal strength indicator.

        >>> from quanser.devices import ST7066UDisplay
        >>> display = ST7066UDisplay()
        >>> display.open("serial://qbot3:0?baud=115200,device='/dev/qbot3_lcd'")
        >>> character_code_left = 0o20
        >>> pattern_left = b'\x00\x00\x00\x01\x05\x15\x15\x15'
        >>> character_code_right = 0o21        
        >>> pattern_right = b'\x01\x05\x15\x15\x15\x15\x15\x15'
        >>> display.setCharacter(character_code_left, pattern_left)
        >>> display.setCharacter(character_code_right, pattern_right)
        >>> message = str(chr(character_code_left)) + str(chr(character_code_right))
        >>> display.printText(1, 1, message, len(message))
        >>> ...
        ...
        >>> display.close()

        """
        result = devices_lib.st7066u_set_character(self._display if self._display is not None else ffi.NULL,
                                                  code, pattern)
    
        if result < 0:
            raise DeviceError(result)

    # endregion

class LS012B7DD01Display:
    """A Python wrapper for the Quanser Devices API interface to Sharp LS012B7DD01 displays.

    Example
    -------
    >>> from quanser.devices import LS012B7DD01Display
    >>> display = LS012B7DD01Display()

    """
    # region Life Cycle

    def __init__(self):
        self._display = None

    # endregion

    # region Implementation

    def open(self, uri):
        """Opens the Sharp LS012B7DD01 display.

        Example
        -------

        >>> from quanser.devices import LS012B7DD01Display
        >>> display = LS012B7DD01Display()
        >>> display.open("spi-cpu://localhost:2?word=8,baud=1000000,frame=1,memsize=990")
        >>> ...
        ...
        >>> display.close()

        """
        display = ffi.new("t_ls012b7dd01 *")
        result = devices_lib.ls012b7dd01_open(uri.encode("UTF-8") if uri is not None else ffi.NULL, display)

        if result < 0:
            raise DeviceError(result)
            
        self._display = display[0]

    def close(self):
        """Close the display.

        Example
        -------

        >>> from quanser.devices import LS012B7DD01Display
        >>> display = LS012B7DD01Display()
        >>> display.open("spi-cpu://localhost:2?word=8,baud=1000000,frame=1,memsize=990")
        >>> ...
        ...        
        >>> display.close()

        """
        result = devices_lib.ls012b7dd01_close(self._display if self._display is not None else ffi.NULL)

        if result < 0:
            raise DeviceError(result)

        self._display = None

    def printText(self, line, column, message, length):
        """Print to the display. 

        Parameters
        ----------
        line : int
            The line where the message will be displayed. Line 0 is the first line.
            
        column : int
            The column where the message will be displayed. Column 0 is the first column.
        
        message : string
            The message to display. Unrecognized characters are skipped. If more than 16 characters would be printed on 
            a line then the line is truncated. A newline will cause the characters to be displayed on the next line. 
            As there are only two lines on the display there should only be one newline in the format string. 
            Printing starts at the given line and column. Line 0 is the first line and column 0 is the first column. 

            The format string is UTF-8 and does support Unicode (particularly, Katakana characters).
                        
        length : int
            The length of the `message`.

        Example
        -------
        Print 'Hello, World!' to the top, left corner of the display.

        >>> from quanser.devices import LS012B7DD01Display
        >>> display = LS012B7DD01Display()
        >>> display.open("spi-cpu://localhost:2?word=8,baud=1000000,frame=1,memsize=990")
        >>> message = "Hello, world!"
        >>> display.printText(0, 0, message, len(message))
        >>> ...
        ...
        >>> display.close()

        """

        result = devices_lib.ls012b7dd01_print(self._display if self._display is not None else ffi.NULL,
                                               line, column,
                                               message.encode("UTF-8") if message is not None else ffi.NULL,
                                               length)

        if result < 0:
            raise DeviceError(result)

    def setCharacter(self, code, pattern):
        """Defines the character associated with the given character code. 

        Parameters
        ----------
        code : int
            Defines the character associated with the given character code. 
            Valid character codes are 0x10 to 0x17 i.e., '\020' to '\027'. Using these characters will produce the bitmap 
            defined in the pattern for that character.
            
        pattern : bytes
            The pattern defines each line of the character being defined, with the eleven bits in each word defining the pixels of that line.
            For example to define the letter T, the pattern would be:

            pattern = np.array([0x0000, 0x0000, 0x0000, 0x01FC, 0x0020, 0x0020, 0x0020, 0x0020, 0x0020, 0x0020, 0x0020, 0x0020, 0x0000, 0x0000, 0x0000, 0x0000], dtype=np.uint16)

            0b00000000000 (0x0000)
            0b00000000000 (0x0000)
            0b00000000000 (0x0000)
            0b00111111100 (0x01FC)
            0b00000100000 (0x0020)
            0b00000100000 (0x0020)
            0b00000100000 (0x0020)
            0b00000100000 (0x0020)
            0b00000100000 (0x0020)
            0b00000100000 (0x0020)
            0b00000100000 (0x0020)
            0b00000100000 (0x0020)
            0b00000000000 (0x0000)
            0b00000000000 (0x0000)
            0b00000000000 (0x0000)
            0b00000000000 (0x0000) <= should generally be zero to allow for cursor

            Note that only bits 0-10 are used. Bit 0 is the rightmost pixel and bit 10 is the leftmost pixel.
            The baseline is in pattern[11]. The top of a typical character is in pattern[3], although some
            characters go higher.
        
        Examples
        --------
        Print a custom character with three lines along the top, middle and bottom. 

        Using array:

        >>> from quanser.devices import LS012B7DD01Display
        >>> display = LS012B7DD01Display()
        >>> display.open("spi-cpu://localhost:2?word=8,baud=1000000,frame=1,memsize=990")
        >>> character_code = 0o20
        >>> pattern = array('H', [0x0000, 0x0000, 0x0000, 0x01FC, 0x0020, 0x0020, 0x0020, 0x0020, 0x0020, 0x0020, 0x0020, 0x0020, 0x0000, 0x0000, 0x0000, 0x0000])
        >>> display.setCharacter(character_code, pattern)
        >>> message = str(chr(character_code))
        >>> display.printText(0, 0, message, len(message))
        >>> ...
        ...
        >>> display.close()

        Using numpy:

        >>> from quanser.devices import LS012B7DD01Display
        >>> import numpy as np
        >>> display = LS012B7DD01Display()
        >>> display.open("spi-cpu://localhost:2?word=8,baud=1000000,frame=1,memsize=990")
        >>> character_code = 0o20
        >>> pattern = np.array([0x0000, 0x0000, 0x0000, 0x01FC, 0x0020, 0x0020, 0x0020, 0x0020, 0x0020, 0x0020, 0x0020, 0x0020, 0x0000, 0x0000, 0x0000, 0x0000], dtype = np.uint16)
        >>> display.setCharacter(character_code, pattern)
        >>> message = str(chr(character_code))
        >>> display.printText(0, 0, message, len(message))
        >>> ...
        ...
        >>> display.close()

        """
        result = devices_lib.ls012b7dd01_set_character(self._display if self._display is not None else ffi.NULL,
                                                       code, ffi.from_buffer(_UINT16_ARRAY, pattern) if pattern is not None else ffi.NULL)
    
        if result < 0:
            raise DeviceError(result)

    def setDarkMode(self, dark):
        """Determine whether to use dark mode for the display. 

        Parameters
        ----------
        dark : bool
            ``True`` to enable dark mode i.e., white text on a black background; 
            ``False`` to use normal mode i.e., black text on a white background.
            
        Examples
        --------
        Print "Hello, world!" in dark mode.

        >>> from quanser.devices import LS012B7DD01Display
        >>> display = LS012B7DD01Display()
        >>> display.open("spi-cpu://localhost:2?word=8,baud=1000000,frame=1,memsize=990")
        >>> display.setDarkMode(True)
        >>> message = "Hello, world!"
        >>> display.printText(0, 0, message, len(message))
        >>> ...
        ...
        >>> display.close()

        """
        result = devices_lib.ls012b7dd01_set_inversion(self._display if self._display is not None else ffi.NULL, dark)

        if result < 0:
            raise DeviceError(result)

    def setRotation(self, rotate):
        """Determine whether to rotate the display 180 degrees. 

        Parameters
        ----------
        rotate : bool
            ``True`` to rotate the display
            ``False`` to use the normal orientation
            
        Examples
        --------
        Print "Hello, world!" in the opposite orientation.

        >>> from quanser.devices import LS012B7DD01Display
        >>> display = LS012B7DD01Display()
        >>> display.open("spi-cpu://localhost:2?word=8,baud=1000000,frame=1,memsize=990")
        >>> display.setRotation(True)
        >>> message = "Hello, world!"
        >>> display.printText(0, 0, message, len(message))
        >>> ...
        ...
        >>> display.close()

        """
        result = devices_lib.ls012b7dd01_set_rotation(self._display if self._display is not None else ffi.NULL, rotate)

        if result < 0:
            raise DeviceError(result)

    def drawImage(self, pixel_row, pixel_column, image_size, image):
        """Draw an image on the display at the given pixel coordinates. The display
        is not cleared before drawing the image, so multiple images may be drawn
        at different locations on the display.

        Parameters
        ----------
        pixel_row : int
            The pixel row at which to place the top edge of the image. A value of 0 corresponds
            to the top of the display.
            
        pixel_column : int
            The pixel column at which to place the left edge of the image. A value of 0 corresponds
            to the left edge of the display.

        image_size : (int, int)
            A tuple containing the height and width of the image as (height, width).

        image : image
            The image to display as a 2D uint8 array that is image_height x image_width pixels
            and is stored in column-major order in memory. Each byte represents a single pixel
            in which a value less than or equal to 127 is either white or black, depending on
            whether dark mode is enabled, and a value greater than 127 is the opposite colour.

        Examples
        --------
        Draw a bitmap on the LCD display.
                
        >>> from quanser.devices import LS012B7DD01Display
        >>> import cv2
        >>> display = LS012B7DD01Display()
        >>> display.open("spi-cpu://localhost:2?word=8,baud=1000000,frame=1,memsize=990")
        >>> img = cv2.imread('Sample.png', cv2.IMREAD_GRAYSCALE)
        >>> # Transpose to convert row major to column major. Copy to make C-continuous.
        >>> img_col_major = img.transpose().copy()
        >>> display.drawImage(0, 0, img_col_major.shape, img_col_major)
        >>> ...
        ...
        >>> display.close()

        """
        result = devices_lib.ls012b7dd01_draw_image(self._display if self._display is not None else ffi.NULL,
                                                    pixel_row, 
                                                    pixel_column,
                                                    image_size[0],
                                                    image_size[1],
                                                    ffi.from_buffer(_UINT8_ARRAY, image) if image is not None else ffi.NULL)
    
        if result < 0:
            raise DeviceError(result)

    # endregion

class LS027B7DSH01Display:
    """A Python wrapper for the Quanser Devices API interface to Sharp LS027B7DSH01 displays.

    Example
    -------
    >>> from quanser.devices import LS027B7DSH01Display
    >>> display = LS027B7DSH01Display()

    """
    # region Life Cycle

    def __init__(self):
        self._display = None

    # endregion

    # region Implementation

    def open(self, uri = "spi://localhost:1?word=8,baud=45000000,polarity=on,phase=on,memsize=8192,frame=0", access = LCDAccess.EXCLUSIVE):
        """Opens the Sharp LS027B7DSH01 display.

        Parameters
        ----------
        uri : string
            The URI indicating the communication channel with which to communicate with the display.
            For QCar 2's display, the URI should be "spi://localhost:1?word=8,baud=45000000,polarity=on,phase=on,memsize=8192,frame=0".
            If this parameter is not specified, the default URI is set for the QCar 2's LCD display.

        access : LCDAccess
            The access mode for the display, which determines whether the LCD can be shared or not. The
            default access is LCDAccess.EXCLUSIVE, which means the caller gets exclusive access to the display.

        Example
        -------

        >>> from quanser.devices import LS027B7DSH01Display
        >>> display = LS027B7DSH01Display()
        >>> display.open("spi://localhost:1?word=8,baud=45000000,polarity=on,phase=on,memsize=8192,frame=0")
        >>> ...
        ...
        >>> display.close()

        """
        display = ffi.new("t_ls027b7dh01 *")
        result = devices_lib.ls027b7dh01_open(uri.encode("UTF-8") if uri is not None else ffi.NULL, access, display)

        if result < 0:
            raise DeviceError(result)
            
        self._display = display[0]

    def close(self):
        """Close the display.

        Example
        -------

        >>> from quanser.devices import LS027B7DSH01Display
        >>> display = LS027B7DSH01Display()
        >>> display.open("spi://localhost:1?word=8,baud=45000000,polarity=on,phase=on,memsize=8192,frame=0")
        >>> ...
        ...        
        >>> display.close()

        """
        result = devices_lib.ls027b7dh01_close(self._display if self._display is not None else ffi.NULL)

        if result < 0:
            raise DeviceError(result)

        self._display = None

    def beginDraw(self):
        """Put the LCD display into drawing mode so that the display is not updated until
        endDraw is called. This allows both graphics and text to be mixed on the display 
        as an atomic update. If this function is not called then the LCD display updates
        immediately.

        Example
        -------
        Draw an image and then write text on top of it.

        >>> from quanser.devices import LS027B7DSH01Display
        >>> display = LS027B7DSH01Display()
        >>> display.open("spi://localhost:1?word=8,baud=45000000,polarity=on,phase=on,memsize=8192,frame=0")
        >>> display.beginDraw()
        >>> display.drawImage(0, 0, (240, 400), image)
        >>> message = "Hello, world!"
        >>> display.printText(5, 0, message, len(message))
        >>> display.endDraw()
        >>> ...
        ...
        >>> display.close()

        Redirect a QCar 2 camera to the LCD display and superimpose the frame rate on the image.

        >>> from quanser.devices import LS027B7DSH01Display
        >>> from quanser.multimedia import VideoCapture, ImageFormat, ImageDataType
        >>> import numpy as np
        >>> import time
        >>>
        >>> fps = 20.0
        >>> image_data = np.zeros((400, 240), dtype = np.uint8)
        >>>
        >>> period = 1.0 / fps
        >>>
        >>> capture = VideoCapture("video://localhost:0", fps, 400, 240, ImageFormat.COL_MAJOR_GREYSCALE, ImageDataType.UINT8, None, 0)
        >>>
        >>> display = LS027B7DSH01Display()
        >>> display.open("spi://localhost:1?word=8,baud=45000000,polarity=on,phase=on,memsize=8192,frame=0")
        >>> display.setDarkMode(True)
        >>> display.setRotation(True)
        >>>
        >>> capture.start()
        >>>
        >>> try :
        >>>     while True :
        >>>         capture.read(image_data)
        >>>
        >>>         display.beginDraw()
        >>>
        >>>         display.drawImage(0, 0, (400, 240), image_data)
        >>>
        >>>         message = "FPS: %.0f" % fps
        >>>         display.printText(11, 0, message, len(message))
        >>>
        >>>         display.endDraw()
        >>>         time.sleep(period)
        >>> finally:
        >>>     display.close()
        >>>     capture.stop()
        >>>     capture.close()

        """

        result = devices_lib.ls027b7dh01_begin_draw(self._display if self._display is not None else ffi.NULL)

        if result < 0:
            raise DeviceError(result)

    def endDraw(self):
        """Take the LCD display out of drawing mode. The display will be updated at
        this point.

        Example
        -------
        Draw an image and then write text on top of it.

        >>> from quanser.devices import LS027B7DSH01Display
        >>> display = LS027B7DSH01Display()
        >>> display.open("spi://localhost:1?word=8,baud=45000000,polarity=on,phase=on,memsize=8192,frame=0")
        >>> display.beginDraw()
        >>> display.drawImage(0, 0, (240,400), image)
        >>> message = "Hello, world!"
        >>> display.printText(5, 0, message, len(message))
        >>> display.endDraw()
        >>> ...
        ...
        >>> display.close()

        """

        result = devices_lib.ls027b7dh01_end_draw(self._display if self._display is not None else ffi.NULL)

        if result < 0:
            raise DeviceError(result)

    def printText(self, line, column, message, length):
        """Print to the display. 

        Parameters
        ----------
        line : int
            The line where the message will be displayed. Line 0 is the first line.
            
        column : int
            The column where the message will be displayed. Column 0 is the first column.
        
        message : string
            The message to display. Unrecognized characters are skipped. If more than 16 characters would be printed on 
            a line then the line is truncated. A newline will cause the characters to be displayed on the next line. 
            As there are only two lines on the display there should only be one newline in the format string. 
            Printing starts at the given line and column. Line 0 is the first line and column 0 is the first column. 

            The format string is UTF-8 and does support Unicode (particularly, Katakana characters).
                        
        length : int
            The length of the `message`.

        Example
        -------
        Print 'Hello, World!' to the top, left corner of the display.

        >>> from quanser.devices import LS027B7DSH01Display
        >>> display = LS027B7DSH01Display()
        >>> display.open("spi://localhost:1?word=8,baud=45000000,polarity=on,phase=on,memsize=8192,frame=0")
        >>> message = "Hello, world!"
        >>> display.printText(0, 0, message, len(message))
        >>> ...
        ...
        >>> display.close()

        """

        result = devices_lib.ls027b7dh01_print(self._display if self._display is not None else ffi.NULL,
                                               line, column,
                                               message.encode("UTF-8") if message is not None else ffi.NULL,
                                               length)

        if result < 0:
            raise DeviceError(result)

    def setCharacter(self, code, pattern):
        """Defines the character associated with the given character code. 

        Parameters
        ----------
        code : int
            Defines the character associated with the given character code. 
            Valid character codes are 0x10 to 0x17 i.e., '\020' to '\027'. Using these characters will produce the bitmap 
            defined in the pattern for that character.
            
        pattern : bytes
            The pattern defines each line of the character being defined, with the sixteen bits in each word defining the pixels of that line.
            For example to define the letter T, the pattern would be:

            pattern = np.array([0x0000, 0x0000, 0x0000, 0X1FF0, 0x0100, 0x0100, 0x0100, 0x0100, 0x0100, 0x0100, 0x0100, 0x0100,
                                0x0100, 0x0100, 0x0100, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000], dtype=np.uint16)

            0x0000,	/* 0b0000000000000000 */	/*                  */
            0x0000,	/* 0b0000000000000000 */	/*                  */
            0x0000,	/* 0b0000000000000000 */	/*                  */
            0x1ff0,	/* 0b0001111111110000 */	/*    .........     */
            0x0100,	/* 0b0000000100000000 */	/*        .         */
            0x0100,	/* 0b0000000100000000 */	/*        .         */
            0x0100,	/* 0b0000000100000000 */	/*        .         */
            0x0100,	/* 0b0000000100000000 */	/*        .         */
            0x0100,	/* 0b0000000100000000 */	/*        .         */
            0x0100,	/* 0b0000000100000000 */	/*        .         */
            0x0100,	/* 0b0000000100000000 */	/*        .         */
            0x0100,	/* 0b0000000100000000 */	/*        .         */
            0x0100,	/* 0b0000000100000000 */	/*        .         */
            0x0100,	/* 0b0000000100000000 */	/*        .         */
            0x0100,	/* 0b0000000100000000 */	/*        .         */
            0x0000,	/* 0b0000000000000000 */	/*                  */
            0x0000,	/* 0b0000000000000000 */	/*                  */
            0x0000,	/* 0b0000000000000000 */	/*                  */
            0x0000,	/* 0b0000000000000000 */	/*                  */
            0x0000	/* 0b0000000000000000 */	/*                  */

            Bit 0 is the rightmost pixel and bit 15 is the leftmost pixel. The baseline is in pattern[14]. The top of a typical character is in pattern[3], although some
            characters go higher.
        
        Examples
        --------
        Print a custom character. 

        Using array:

        >>> from quanser.devices import LS027B7DSH01Display
        >>> display = LS027B7DSH01Display()
        >>> display.open("spi://localhost:1?word=8,baud=45000000,polarity=on,phase=on,memsize=8192,frame=0")
        >>> character_code = 0o20
        >>> pattern = array('H', [0x0000, 0x0000, 0x0000, 0X1FF0, 0x0100, 0x0100, 0x0100, 0x0100, 0X1FF0, 0x0100, 0x0100, 0x0100, 0x0100, 0x0100, 0X1FF0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000])
        >>> display.setCharacter(character_code, pattern)
        >>> message = str(chr(character_code))
        >>> display.printText(0, 0, message, len(message))
        >>> ...
        ...
        >>> display.close()

        Using numpy:

        >>> from quanser.devices import LS027B7DSH01Display
        >>> import numpy as np
        >>> display = LS027B7DSH01Display()
        >>> display.open("spi://localhost:1?word=8,baud=45000000,polarity=on,phase=on,memsize=8192,frame=0")
        >>> character_code = 0o20
        >>> pattern = np.array([0x0000, 0x0000, 0x0000, 0X1FF0, 0x0100, 0x0100, 0x0100, 0x0100, 0X1FF0, 0x0100, 0x0100, 0x0100, 0x0100, 0x0100, 0X1FF0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000], dtype = np.uint16)
        >>> display.setCharacter(character_code, pattern)
        >>> message = str(chr(character_code))
        >>> display.printText(0, 0, message, len(message))
        >>> ...
        ...
        >>> display.close()

        """
        result = devices_lib.ls027b7dh01_set_character(self._display if self._display is not None else ffi.NULL,
                                                       code, ffi.from_buffer(_UINT16_ARRAY, pattern) if pattern is not None else ffi.NULL)
    
        if result < 0:
            raise DeviceError(result)

    def setDarkMode(self, dark):
        """Determine whether to use dark mode for the display. 

        Parameters
        ----------
        dark : bool
            ``True`` to enable dark mode i.e., white text on a black background; 
            ``False`` to use normal mode i.e., black text on a white background.
            
        Examples
        --------
        Print "Hello, world!" in dark mode.

        >>> from quanser.devices import LS027B7DSH01Display
        >>> display = LS027B7DSH01Display()
        >>> display.open("spi://localhost:1?word=8,baud=45000000,polarity=on,phase=on,memsize=8192,frame=0")
        >>> display.setDarkMode(True)
        >>> message = "Hello, world!"
        >>> display.printText(0, 0, message, len(message))
        >>> ...
        ...
        >>> display.close()

        """
        result = devices_lib.ls027b7dh01_set_inversion(self._display if self._display is not None else ffi.NULL, dark)

        if result < 0:
            raise DeviceError(result)

    def setRotation(self, rotate):
        """Determine whether to rotate the display 180 degrees. 

        Parameters
        ----------
        rotate : bool
            ``True`` to rotate the display
            ``False`` to use the normal orientation
            
        Examples
        --------
        Print "Hello, world!" in the opposite orientation.

        >>> from quanser.devices import LS027B7DSH01Display
        >>> display = LS027B7DSH01Display()
        >>> display.open("spi://localhost:1?word=8,baud=45000000,polarity=on,phase=on,memsize=8192,frame=0")
        >>> display.setRotation(True)
        >>> message = "Hello, world!"
        >>> display.printText(0, 0, message, len(message))
        >>> ...
        ...
        >>> display.close()

        """
        result = devices_lib.ls027b7dh01_set_rotation(self._display if self._display is not None else ffi.NULL, rotate)

        if result < 0:
            raise DeviceError(result)

    def drawImage(self, pixel_row, pixel_column, image_size, image):
        """Draw an image on the display at the given pixel coordinates. The display
        is not cleared before drawing the image, so multiple images may be drawn
        at different locations on the display.

        Parameters
        ----------
        pixel_row : int
            The pixel row at which to place the top edge of the image. A value of 0 corresponds
            to the top of the display.
            
        pixel_column : int
            The pixel column at which to place the left edge of the image. A value of 0 corresponds
            to the left edge of the display.

        image_size : (int, int)
            A tuple containing the height and width of the image as (height, width).

        image : image
            The image to display as a 2D uint8 array that is image_height x image_width pixels
            and is stored in column-major order in memory. Each byte represents a single pixel
            in which a value less than or equal to 127 is either white or black, depending on
            whether dark mode is enabled, and a value greater than 127 is the opposite colour.

        Examples
        --------
        Draw a bitmap on the LCD display.
                
        >>> from quanser.devices import LS027B7DSH01Display
        >>> import cv2
        >>> display = LS027B7DSH01Display()
        >>> display.open("spi://localhost:1?word=8,baud=45000000,polarity=on,phase=on,memsize=8192,frame=0")
        >>> img = cv2.imread('Sample.png', cv2.IMREAD_GRAYSCALE)
        >>> # Transpose to convert row major to column major. Copy to make C-continuous.
        >>> img_col_major = img.transpose().copy()
        >>> display.drawImage(0, 0, img_col_major.shape, img_col_major)
        >>> ...
        ...
        >>> display.close()

        """
        result = devices_lib.ls027b7dh01_draw_image(self._display if self._display is not None else ffi.NULL,
                                                    pixel_row, 
                                                    pixel_column,
                                                    image_size[0],
                                                    image_size[1],
                                                    ffi.from_buffer(_UINT8_ARRAY, image) if image is not None else ffi.NULL)
    
        if result < 0:
            raise DeviceError(result)

    def save(self, filename):
        """Save the current contents of the display to a PBM image file. The filename should
        have a .pbm extension.

        Parameters
        ----------
        filename : string
            The filename to which to write the display contents.

        Examples
        --------
        Save the current contents of the LCD display.
                
        >>> from quanser.devices import LS027B7DSH01Display
        >>> import cv2
        >>> display = LS027B7DSH01Display()
        >>> display.open("spi://localhost:1?word=8,baud=45000000,polarity=on,phase=on,memsize=8192,frame=0")
        >>> img = cv2.imread('Sample.png', cv2.IMREAD_GRAYSCALE)
        >>> # Transpose to convert row major to column major. Copy to make C-continuous.
        >>> img_col_major = img.transpose().copy()
        >>> display.drawImage(0, 0, img_col_major.shape, img_col_major)
        >>> display.save("lcd_display.pbm")
        ...
        >>> display.close()

        """
        result = devices_lib.ls027b7dh01_save_display(self._display if self._display is not None else ffi.NULL, 
            filename.encode("UTF-8") if filename is not None else ffi.NULL)

        if result < 0:
            raise DeviceError(result)

    # endregion

class WS0010Display:
    """A Python wrapper for the Quanser Devices API interface to Sitronix WS0010 displays.

    Example
    -------
    >>> from quanser.devices import WS0010Display
    >>> display = WS0010Display()

    """
    # region Life Cycle

    def __init__(self):
        self._display = None

    # endregion

    # region Implementation

    def open(self, uri):
        """Opens the WS0010 display.

        Example
        -------

        >>> from quanser.devices import WS0010Display
        >>> display = WS0010Display()
        >>> display.open("lcd://qbot_platform:1")
        >>> ...
        ...
        >>> display.close()

        """
        display = ffi.new("t_ws0010 *")
        result = devices_lib.ws0010_open(uri.encode("UTF-8") if uri is not None else ffi.NULL, display)

        if result < 0:
            raise DeviceError(result)
            
        self._display = display[0]

    def close(self):
        """Close the display.

        Example
        -------

        >>> from quanser.devices import WS0010Display
        >>> display = WS0010Display()
        >>> display.open("lcd://qbotplatform:1")
        >>> ...
        ...        
        >>> display.close()

        """
        result = devices_lib.ws0010_close(self._display if self._display is not None else ffi.NULL)

        if result < 0:
            raise DeviceError(result)

        self._display = None

    def printText(self, line, column, message, length):
        """Print to the display. 

        Parameters
        ----------
        line : int
            The line where the message will be displayed. Line 0 is the first line.
            
        column : int
            The column where the message will be displayed. Column 0 is the first column.
        
        message : string
            The message to display. Unrecognized characters are skipped. If more than 16 characters would be printed on 
            a line then the line is truncated. A newline will cause the characters to be displayed on the next line. 
            As there are only two lines on the display there should only be one newline in the format string. 
            Printing starts at the given line and column. Line 0 is the first line and column 0 is the first column. 

            The format string is UTF-8 and does support Unicode (particularly, Katakana characters).
                        
        length : int
            The length of the `message`.

        Example
        -------
        Print 'Hello, World!' to the top, left corner of the display.

        >>> from quanser.devices import WS0010Display
        >>> display = WS0010Display()
        >>> display.open("lcd://qbotplatform:1")
        >>> message = "Hello, world!"
        >>> display.printText(0, 0, message, len(message))
        >>> ...
        ...
        >>> display.close()

        """

        result = devices_lib.ws0010_print(self._display if self._display is not None else ffi.NULL,
                                          line, column,
                                          message.encode("UTF-8") if message is not None else ffi.NULL,
                                          length)

        if result < 0:
            raise DeviceError(result)

    def setCharacter(self, code, pattern):
        """Defines the character associated with the given character code. 

        Parameters
        ----------
        code : int
            Defines the character associated with the given character code. 
            Valid character codes are 0x10 to 0x17 i.e., '\020' to '\027'. Using these characters will produce the bitmap 
            defined in the pattern for that character.
            
        pattern : bytes
            The pattern defines each line of the character being defined, with the five bits in each byte defining the pixels of that line.
            For example to define the letter T, the pattern would be:

            pattern = b'\x1F\x40\x40\x40\x40\x40\x40\x00'

            0b00011111 (\x1F)
            0b00000100 (\x40)
            0b00000100 (\x40)
            0b00000100 (\x40)
            0b00000100 (\x40)
            0b00000100 (\x40)
            0b00000100 (\x40)
            0b00000000 (\x00) <= should generally be zero to allow for cursor

            Note that only bits 0-4 are used. Bit 0 is the rightmost pixel and bit 4 is the leftmost pixel. 
        
        Examples
        --------
        Print a custom character with three lines along the top, middle and bottom. 

        >>> from quanser.devices import WS0010Display
        >>> display = WS0010Display()
        >>> display.open("lcd://qbotplatform:1")
        >>> character_code = 0o20
        >>> pattern = b'\x1F\x00\x00\x1F\x00\x00\x1F\x00'
        >>> display.setCharacter(character_code, pattern)
        >>> message = str(chr(character_code))
        >>> display.printText(0, 0, message, len(message))
        >>> ...
        ...
        >>> display.close()

        Print a pair of custom characters that give the appearance of a wifi signal strength indicator.

        >>> from quanser.devices import WS0010Display
        >>> display = WS0010Display()
        >>> display.open("lcd://qbotplatform:1")
        >>> character_code_left = 0o20
        >>> pattern_left = b'\x00\x00\x00\x01\x05\x15\x15\x15'
        >>> character_code_right = 0o21        
        >>> pattern_right = b'\x01\x05\x15\x15\x15\x15\x15\x15'
        >>> display.setCharacter(character_code_left, pattern_left)
        >>> display.setCharacter(character_code_right, pattern_right)
        >>> message = str(chr(character_code_left)) + str(chr(character_code_right))
        >>> display.printText(1, 1, message, len(message))
        >>> ...
        ...
        >>> display.close()

        """
        result = devices_lib.ws0010_set_character(self._display if self._display is not None else ffi.NULL,
                                                  code, pattern)
    
        if result < 0:
            raise DeviceError(result)

    # endregion

class GameController:
    """A Python wrapper for the Quanser Devices API interface to game controllers.

    Example
    -------
    >>> from quanser.devices import GameController
    >>> joystick = GameController()

    """
    # region Life Cycle

    def __init__(self):        
        self._controller = None

    # endregion

    # region Implementation

    def open(self, controller_number):
        """Opens a game controller.

        Example
        -------

        >>> from quanser.devices import GameController
        >>> joystick = GameController()
        >>> joystick.open(1)
        >>> ...
        ...
        >>> joystick.close()

        """
        controller = ffi.new("t_game_controller *")
        result = devices_lib.game_controller_open(controller_number, 64, ffi.NULL, ffi.NULL, 1, 0, 1.0, controller)

        if result < 0:
            raise DeviceError(result)
            
        self._controller = controller[0]

    def close(self):
        """Close the game controller.

        Example
        -------

        >>> from quanser.devices import GameController
        >>> joystick = GameController()
        >>> joystick.open(1)
        >>> ...
        ...
        >>> joystick.close()

        """
        result = devices_lib.game_controller_close(self._controller if self._controller is not None else ffi.NULL)

        if result < 0:
            raise DeviceError(result)

        self._controller = None

    def poll(self):
        """Poll the game controller state.

        The first return value contains the state of the game controller axes, sliders and buttons as an object. The properties of the object are:
                x : float
                    The x-coordinate as a percentage of the range. Spans -1.0 to +1.0.
                y : float
                    The y-coordinate as a percentage of the range. Spans -1.0 to +1.0.
                z : float
                    The z-coordinate as a percentage of the range. Spans -1.0 to +1.0.
                rx : float
                    The rx-coordinate as a percentage of the range. Spans -1.0 to +1.0.
                ry : float
                    The ry-coordinate as a percentage of the range. Spans -1.0 to +1.0.
                rz : float
                    The rz-coordinate as a percentage of the range. Spans -1.0 to +1.0.
                sliders : float[2]
                    The slider positions as a percentage of the range. Spans 0.0 to 1.0.
                point_of_views : float[4]
                    The point-of-view positions in positive radians or -1 (centred).
                buttons : uint32
                    The state of each of 32 buttons as a bitmask. A bit value of 0 indicates the button is released, while a value of 1 indicates the button is pressed.

        The second return value is a boolean indicating whether the state is new since the last time it was polled.

        Example
        -------
        Poll the state of the joystick.

        >>> from quanser.devices import GameController
        >>> joystick = GameController()
        >>> joystick.open(1)
        >>> state, is_new = joystick.poll()
        >>> print("new=%d x=%f y=%f z=%f" % (is_new, state.x, state.y, state.z))
        ...
        >>> joystick.close()

        """

        c_states = ffi.new("t_game_controller_states *")
        c_is_new = ffi.new("t_boolean *")

        result = devices_lib.game_controller_poll(self._controller if self._controller is not None else ffi.NULL, c_states, c_is_new)

        is_new = bool(c_is_new[0])
        if result == -34:
            is_new = False
        elif result < 0:
            raise DeviceError(result)

        return c_states[0], is_new

    # endregion

class Aaaf5050McK12LED :
    """A Python wrapper for the Quanser Devices API interface to the AAAF5050_MC_K12 LED strip on QCar 2.

    Example
    -------
    >>> from quanser.devices import Aaaf5050McK12LED
    >>> leds = Aaaf5050McK12LED()

    """
    # region Life Cycle

    def __init__(self):
        self._leds = None

    # endregion

    # region Implementation

    def open(self, uri, max_leds):
        """Opens the AAAF5050_MC_K12 LED strip.

        Parameters
        ----------
        uri : string
            A URI used for communicating with the device. Numerous URI parameters are available. For the Quanser QCar 2,
            a suitable URI is "spi://localhost:1?memsize=420,word=8,baud=3333333,lsb=off,frame=1".
        max_leds : int
            The maximum number of LEDs in the LED strip. For the Quanser QCar 2, this number should be 33.

        Example
        -------

        >>> from quanser.devices import Aaaf5050McK12LED
        >>> leds = Aaaf5050McK12LED()
        >>> leds.open("spi://localhost:1?memsize=420,word=8,baud=3333333,lsb=off,frame=1", 33)
        >>> ...
        ...
        >>> leds.close()

        """
        leds = ffi.new("t_aaaf5050_mc_k12 *")
        result = devices_lib.aaaf5050_mc_k12_open(uri.encode("UTF-8") if uri is not None else ffi.NULL, int(max_leds), leds)

        if result < 0:
            raise DeviceError(result)
            
        self._leds = leds[0]

    def close(self):
        """Close the LED strip.

        Example
        -------

        >>> from quanser.devices import Aaaf5050McK12LED
        >>> leds = Aaaf5050McK12LED()
        >>> leds.open("spi://localhost:1?memsize=420,word=8,baud=3333333,lsb=off,frame=1", 33)
        >>> ...
        ...
        >>> leds.close()

        """
        result = devices_lib.aaaf5050_mc_k12_close(self._leds if self._leds is not None else ffi.NULL)

        if result < 0:
            raise DeviceError(result)

        self._leds = None

    def writeColors(self, led_colors, num_leds):
        """Write colors to the LED strip. 

        Parameters
        ----------
        led_colors : array_like
            An Nx3 array of unsigned 8-bit integers containing the colors for each LED in the strip. 
            The three color components are red, green, and blue in that order and each component 
            ranges from 0 to 255. Alternatively, it may be an Nx3 list of lists, or list of (R, G, B) tuples
            or simply a single (R, G, B) tuple or [R, G, B] list or array.
            
        num_leds : int
            The number of LED colors from the led_colors argument to write to the LED strip. If this
            number exceeds the number of colors in the led_colors argument then the last element is
            used for the remaining LEDs.
        
        Example
        -------
        Make all the LEDs red.

        >>> from quanser.devices import Aaaf5050McK12LED
        >>> leds = Aaaf5050McK12LED()
        >>> num_leds = 33
        >>> leds.open("spi://localhost:1?memsize=420,word=8,baud=3333333,lsb=off,frame=1", num_leds)
        >>> leds.writeColors((255, 0, 0), num_leds)
        ...
        >>> leds.close()

        Make the first three LEDs red, green and blue and the rest magenta using a list of tuples.

        >>> from quanser.devices import Aaaf5050McK12LED
        >>> leds = Aaaf5050McK12LED()
        >>> num_leds = 33
        >>> leds.open("spi://localhost:1?memsize=420,word=8,baud=3333333,lsb=off,frame=1", num_leds)
        >>> leds.writeColors([(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255)], num_leds)
        ...
        >>> leds.close()

        Make the first three LEDs red, green and blue and the rest magenta using a list of lists.

        >>> from quanser.devices import Aaaf5050McK12LED
        >>> leds = Aaaf5050McK12LED()
        >>> num_leds = 33
        >>> leds.open("spi://localhost:1?memsize=420,word=8,baud=3333333,lsb=off,frame=1", num_leds)
        >>> leds.writeColors([[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 0, 255]], num_leds)
        ...
        >>> leds.close()

        Make the first LED red and the rest green using a list of arrays.

        >>> import array as arr
        >>> from quanser.devices import Aaaf5050McK12LED
        >>> leds = Aaaf5050McK12LED()
        >>> num_leds = 33
        >>> leds.open("spi://localhost:1?memsize=420,word=8,baud=3333333,lsb=off,frame=1", num_leds)
        >>> red = arr.array("B", [255, 0, 0]])
        >>> green = arr.array("B", [0, 255, 0]])
        >>> colors = [red, green]
        >>> leds.writeColors(colors, num_leds)
        ...
        >>> leds.close()

        Make the first three LEDs red, green and blue and the rest light magenta using floating-point.

        >>> import numpy as np
        >>> from quanser.devices import Aaaf5050McK12LED
        >>> leds = Aaaf5050McK12LED()
        >>> num_leds = 33
        >>> leds.open("spi://localhost:1?memsize=420,word=8,baud=3333333,lsb=off,frame=1", num_leds)
        >>> leds.writeColors([(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0), (0.5, 0.0, 0.5)], num_leds)
        ...
        >>> leds.close()

        Clear all the LEDs.

        >>> import numpy as np
        >>> from quanser.devices import Aaaf5050McK12LED
        >>> leds = Aaaf5050McK12LED()
        >>> num_leds = 33
        >>> leds.open("spi://localhost:1?memsize=420,word=8,baud=3333333,lsb=off,frame=1", num_leds)
        >>> leds.writeColors([], num_leds)
        ...
        >>> leds.close()

        """

        length = len(led_colors)
        if length > 0:
            # If the object's elements are not subscriptable then it is a tuple or array of values
            # so make it a list of such elements to make the code below easier.
            if not hasattr(led_colors[0], '__getitem__'):
                led_colors = [led_colors];
                length = 1

        if length > num_leds:
            length = num_leds

        colors = ffi.new("t_led_color[]", num_leds)
        
        # Initialize r,g,b to zero so that supplying an empty list clears all the LEDs
        r = 0
        g = 0
        b = 0

        for i in range(0, length):
            c = led_colors[i]

            if isinstance(c[0], float) or isinstance(c[1], float) or isinstance(c[2], float):
                r = int(255 * c[0])
                g = int(255 * c[1])
                b = int(255 * c[2])
            else:
                r = c[0]
                g = c[1]
                b = c[2]

            colors[i].red   = r
            colors[i].green = g
            colors[i].blue  = b

        for i in range(length, num_leds):
            colors[i].red   = r
            colors[i].green = g
            colors[i].blue  = b

        result = devices_lib.aaaf5050_mc_k12_write(self._leds if self._leds is not None else ffi.NULL,
                                          colors, num_leds)

        ffi.release(colors)

        if result < 0:
            raise DeviceError(result)

    # endregion

# endregion


