#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.load_modules import __check_external_modules
from core.parse import load

if __name__ == "__main__" and __check_external_modules():
    load()
