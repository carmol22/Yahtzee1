#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    from wsgiref.handlers import CGIHandler
    from app import app

    CGIHandler().run(app)

except Exception as e:
    import traceback
    print(traceback.format_exc())