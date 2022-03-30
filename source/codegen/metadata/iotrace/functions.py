# -*- coding: utf-8 -*-
# This file is generated from NI-SCOPE API metadata version 20.5.0d7
functions = {
    'CloseIOTrace': {
        'cname': 'nispy_CloseSpy',
        'parameters': [
        ],
        'returns': 'int32_t'
    },
    'GetApplicationPath': {
        'cname': 'nispy_GetApplicationPath',
        'parameters': [
            {
                'direction': 'out',
                'name': 'pathString',
                'type': 'char[]',
                'size': {
                    'mechanism': 'fixed',
                    'value': '256'
                }
            },
            {
                'direction': 'in',
                'name': 'pathStringSize',
                'type': 'int32_t',
                'include_in_proto': False,
                'hardcoded_value': '256'
            }
        ],
        'returns': 'int32_t'
    },
    'LogMessage': {
        'cname': 'nispy_WriteTextEntry',
        'parameters': [
            {
                'direction': 'in',
                'name': 'message',
                'type': 'const char[]'
            }
        ],
        'returns': 'int32_t'
    },
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
    'StopTracing': {
        'cname': 'nispy_StopSpying',
        'parameters': [
        ],
        'returns': 'int32_t'
    },    
}
