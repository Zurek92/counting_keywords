#!/usr/bin/env python3
"""Production config."""
import os


class APP:
    IP = "0.0.0.0"
    PORT = os.environ.get('APP_PORT')
    DEBUG = False
