#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "1.0.9.2"

def main(**kwargs):
    """Main entry point.
    ykdl (legacy)
    """
    from .common import main
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted by Ctrl-C')
