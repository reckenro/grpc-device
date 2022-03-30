# -*- coding: utf-8 -*-
# This file is generated from NI-SCOPE API metadata version 20.5.0d7
functions = {
    'StartTracing': {
        'cname': 'nispy_StartSpying',
        'parameters': [
            {
                'direction': 'in',
                'name': 'logFileSetting',
                'type': 'eNiSpyLogFileSetting',
                'supports_standard_copy_convert': True,
            },
            {
                'direction': 'in',
                'name': 'filePathString',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'name': 'fileWriteMode',
                'type': 'eNiSpyAPIFileWriteMode',
                'supports_standard_copy_convert': True
            }
        ],
        'returns': 'int32_t'
    },
}
