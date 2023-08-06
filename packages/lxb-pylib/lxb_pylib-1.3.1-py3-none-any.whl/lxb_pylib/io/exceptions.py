class DataExistsError(Exception):
    pass


class BadConversionError(Exception):
    """
    Unable to convert Python-based data type to SQL equivalent.
    """

    pass
