#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

__version__ = '0.0.2'

try:
    from thumbor_text_filter.text import Filter  # NOQA
except ImportError:
    logging.exception('Could not import thumbor_text_filter. Probably due to setup.py installing it.')