import os

from cffi import FFI

from quanser.image_processing import (ImageProcessingError)


# region Setup


ffi = FFI()
ffi.cdef("""
    /* Common Type Definitions */
    
    typedef char                t_boolean;
    typedef unsigned int        t_uint;
    typedef unsigned long long  t_ulong;
    typedef t_ulong             t_uint64;
    typedef signed int          t_int;
    typedef t_int               t_error;
    typedef float               t_single;
    typedef double              t_double;
 
    /* Lidar Type Definitions */
    
    typedef struct tag_lidar2d_scan_matcher* t_lidar2d_scan_matcher;
    typedef struct tag_range_single
    {
        t_single x;
        t_single y;
    } t_range_single;
    
    /* Lidar Functions */
    t_error lidar2d_match_scans_grid_open(t_lidar2d_scan_matcher* matcher, t_single resolution, t_single max_range);
    
    t_error lidar2d_match_scans_grid_match(t_lidar2d_scan_matcher matcher,
                                           const t_single* ref_ranges, const t_single* ref_angles, t_uint num_ref_points,
                                           const t_single* ranges, const t_single* angles, t_uint num_points,
                                           const t_single initial_pose[3], const t_range_single* translation_search_range, t_single rotation_search_range,
                                           t_single pose[3], t_single* score, t_single covariance[9]);
    
    t_error lidar2d_match_scans_grid_close(t_lidar2d_scan_matcher matcher);
""")

image_processing_lib = ffi.dlopen("quanser_image_processing")

# endregion

# region Constants

_BOOLEAN_ARRAY = "t_boolean[]"
_CHAR_ARRAY = "char[]"
_UINT_ARRAY = "t_uint[]"
_UINT32_ARRAY = "t_uint32[]"
_INT_ARRAY = "t_int[]"
_INT32_ARRAY = "t_int32[]"
_SINGLE_ARRAY = "t_single[]"
_SINGLE_ARRAY3 = "t_single[3]"
_SINGLE_ARRAY9 = "t_single[9]"
_DOUBLE_ARRAY = "t_double[]"

_RANGE_SINGLE_ARRAY = "t_range_single[]"

# endregion

# region Image Processing Classes


class Lidar2DMatchScansGrid:
    """A Python wrapper for the Quanser LIDAR 2D Match Scans Grid API.

    Parameters
    ----------
    resolution : float
        The resolution.
    max_range : float
        The maximum range.

    Raises
    ------
    ImageProcessingError
        On non-zero return code. A suitable error message may be retrieved using `get_error_message`.

    Examples
    --------
    Construct a new 2D LIDAR scan matcher.

    >>> from quanser.image_processing import Lidar2DMatchScanGrid
    >>> lidar2d_match_scan = Lidar2DMatchScanGrid()
    >>> # ...
    ...
    >>> lidar2d_match_scan.close()

    """

    # region Life Cycle

    def __init__(self,
                 resolution=20.0, max_range=5.0):
        self._matcher = None

        self.open(resolution=20.0, max_range=5.0)

    # endregion

    # region Functions

    def open(resolution, max_range):
        """Opens a 2D LIDAR scan matcher.

        Parameters
        ----------
        resolution : float
            The resolution.
        max_range : float
            The maximum range.

        Raises
        ------
        ImageProcessingError
            On non-zero return code. A suitable error message may be retrieved using `get_error_message`.

        Examples
        --------
        Open the 2D LIDAR scan matcher with 13 grid cells per meter and any LIDAR scan data beyond 8 metre to be discarded.

        >>> from quanser.image_processing import Lidar2DMatchScanGrid
        >>> resolution = 13.0
        >>> max_range = 8.0
        >>> lidar2d_match_scan = Lidar2DMatchScanGrid()
        >>> lidar2d_match_scan.open(resolution, max_range)
        >>> # ...
        ...
        >>> lidar2d_match_scan.close()

        """
        if self._matcher is not None:
            self.close()

        matcher = ffi.new("t_lidar2d_scan_matcher *")

        result = image_processing_lib.lidar2d_match_scans_grid_open(matcher, resolution, max_range)

        if result < 0:
            raise ImageProcessingError(result)

        self._matcher = matcher[0]

    def close(self):
        """Closes the 2D LIDAR scan matcher and frees up resources allocated by the matcher. Scan matching can consume
        a significant amount of memory and system resources.

        Raises
        ------
        ImageProcessingError
            On non-zero return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------
        Close the 2D LIDAR scan matcher.

        >>> from quanser.image_processing import Lidar2DMatchScanGrid
        >>> resolution = 13.0
        >>> max_range = 8.0
        >>> lidar2d_match_scan = Lidar2DMatchScanGrid()
        >>> lidar2d_match_scan.open(resolution, max_range)
        >>> # ...
        ...
        >>> lidar2d_match_scan.close()

        """
        result = image_processing_lib.lidar2d_match_scans_grid_close(self._matcher if self._matcher is not None else ffi.NULL)
        if result < 0:
            raise ImageProcessingError(result)

        self._matcher = None

    def match(self,
              ref_ranges, ref_angles, num_ref_points,
              ranges, angles, num_points,
              initial_pose, translation_search_range, rotation_search_range,
              pose, score, covariance):
        """Match the current scan to the reference scan, returning the pose of the current scan relative to the reference
        scan. If the score and/or covariance outputs are non-NULL then it will return the confidence in the match as
        a scalar score and/or 3x3 covariance matrix. For the fastest results, an initial pose may be specified, that
        may be derived from IMU data, for instance. In that case, if a translation search range and/or rotation search
        range is indicated then it will limit the search to those ranges.

        If the translation_search_range is NULL then values of 4 meters will be used. If the rotation_search_range
        is zero then a search range of 2*PI will be used.

        Parameters
        ----------
        ref_ranges : array_like
            A vector of range values for the reference scan.
        ref_angles : array_like
            A vector of angles or heading values for the reference scan.
        num_ref_points : int
            The number of valid points in reference scan as specified in the "ref_ranges" and "ref_angles" array.
        ranges : array_like
            A vector of range values for the current scan.
        angles : array_like
            A vector of angle or heading values for the current scan.
        num_points : int
            The number of valid points in the current scan.
        initial_pose : array_like
            The initial pose as a 3-vector at which to start the grid search. The "translation_search_range" and
            "rotation_search_range" are relative to this initial pose. The pose consists of the elements [x, y, theta]
            where x and y denote the translation in meters and theta denotes the rotation in radians.
        translation_search_range : array_like
            The translation search range as a 2-vector [x,y] indicating the cartesian search range in meters.
        rotation_search_range : float
            The rotation search range as a scalar indicating the angular search range in radians.
        pose : array_like
            The pose as a 3-vector [x,y,theta] representing the transformation between the current scan and the
            reference scan. The (x,y) components are the translation and the theta component is the rotation.
        score : array_like
            A score representing the confidence in the match. Higher values denote higher confidence. The value
            is not normalized so it is highly dependent on the input scans and block parameters.
        covariance : array_like
            A 3x3 matrix representing an estimate of the covariance of the result. This output is currently set
            to zero but may be added in future revisions.

        Raises
        ------
        ImageProcessingError
            On non-zero return code. A suitable error message may be retrieved using `get_error_message`.

        Example
        -------
        Read the 2D LIDAR scan matcher.

        >>> from quanser.image_processing import Lidar2DMatchScanGrid
        >>> resolution = 13.0
        >>> max_range = 8.0
        >>> lidar2d_match_scan = Lidar2DMatchScanGrid()
        >>> lidar2d_match_scan.open(resolution, max_range)
        >>> # ...
        ...#TODO: <to be filled in>
        >>> lidar2d_match_scan.close()

        """
        result = image_processing_lib.lidar2d_match_scans_grid_match(self._matcher if self._matcher is not None else ffi.NULL,
                                                                     ffi.from_buffer(_SINGLE_ARRAY, ref_ranges) if ref_ranges is not None else ffi.NULL, ffi.from_buffer(_SINGLE_ARRAY, ref_angles) if ref_angles is not None else ffi.NULL, num_ref_points,
                                                                     ffi.from_buffer(_SINGLE_ARRAY, ranges) if ranges is not None else ffi.NULL, ffi.from_buffer(_SINGLE_ARRAY, angles) if angles is not None else ffi.NULL, num_points,
                                                                     ffi.from_buffer(_SINGLE_ARRAY3, initial_pose) if initial_pose is not None else ffi.NULL, ffi.from_buffer(_RANGE_SINGLE_ARRAY, translation_search_range) if translation_search_range is not None else ffi.NULL, rotation_search_range,
                                                                     ffi.from_buffer(_SINGLE_ARRAY3, pose) if pos is not None else ffi.NULL, ffi.from_buffer(_SINGLE_ARRAY, score) if score is not None else ffi.NULL, ffi.from_buffer(_SINGLE_ARRAY9, covariance) if covariance is not None else ffi.NULL)
        if result < 0:
            raise ImageProcessingError(result)

        return True if result else False

    # endregion

# endregion
