class RangingSensorType:
    """The sensor type."""
    INVALID = 0
    """Invalid sensor type."""

    VL53L1 = 1
    """ST Microelectronics VL31L1 time-of-flight sensor."""

    RPLIDAR = 2
    """Slamtec RPLidar 2D LIDAR sensor."""


class RangingDistance:
    """The ranging distance."""
    SHORT = 0
    """Short ranging distance. For the short range, use the `legacy` mode since it has 1/4 mm distance measurements or
    the `stability` mode. Give priority to the stability mode since it is newer and provides more data points."""

    MEDIUM = 1
    """Medium ranging distance. Uses the `express` mode, which has 16 m range and more data points (4000 sps)."""

    LONG = 2
    """Long ranging distance. Uses the `boost` or `sensitivity` scan modes, if available, since they have 28 m range.
    Gives priority to the `sensitivity` mode."""


class RangingMeasurementMode:
    """The ranging measurement mode."""
    NORMAL = 0
    """Return actual measurement data. Number of measurements will vary and angles will not be consistent between scans.
    Angles will start close to zero."""

    INTERPOLATED = 1
    """Returns the number of measurements, N, requested. Angles will start at zero and be 360/N apart. Raw measurements
    will be interpolated to estimate distance at each angle."""


class LCDAccess:
    """The LCD access mode."""
    SHARED = 0
    """Multiple processes can access the LCD at the same time but hold a global mutex while actually writing to the display. Waits for mutex to be released."""

    ASYNCHRONOUS = 1
    """Multiple processes can access the LCD at the same time but hold a global mutex while actually writing to the display. Skips write if mutex already held by another process."""

    EXCLUSIVE = 2
    """Only one process can access the LCD at a time (global mutex is held as long as the LCD is open)."""
