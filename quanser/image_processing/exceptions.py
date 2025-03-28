from quanser.common import GenericError


class ImageProcessingError(GenericError):
    """A image processing exception derived from ``GenericError``.

    Example
    -------
    >>> from quanser.image_processing import Lidar2DMatchScansGrid, ImageProcessingError
    >>> match_scan = Lidar2DMatchScansGrid()
    >>> try:
    ...     match_scan.match(None, ...)  # match_scan matching with no reference, so raises an exception.
    ... except ImageProcessingError as e:
    ...     print(e.get_error_message())  # Handle media errors.
    ...

    """
    pass
