class DarkOsintCopsError(Exception):
    """Base exception for DarkOsintCops errors."""
    pass

class EngineError(DarkOsintCopsError):
    """Exception raised for errors in search engines."""
    pass
