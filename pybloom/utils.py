import sys
try:
    import StringIO
    import cStringIO
except ImportError:
    from io import BytesIO

running_python_3 = sys.version_info[0] == 3


def range_fn(*args):
        return range(*args)


def is_string_io(instance):
       return isinstance(instance, BytesIO)
