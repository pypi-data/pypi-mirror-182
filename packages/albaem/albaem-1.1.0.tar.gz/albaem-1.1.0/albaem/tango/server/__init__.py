from .device import PyAlbaEm


def main():
    import sys
    import logging
    from tango.server import run
    args = ['PyAlbaEM'] + sys.argv[1:]
    fmt = '%(asctime)s %(threadName)s %(levelname)s %(name)s %(message)s'
    logging.basicConfig(level=logging.INFO, format=fmt)
    run((PyAlbaEm,), args=args)
