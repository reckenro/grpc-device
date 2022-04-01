# -*- coding: utf-8 -*-
# This file is generated from NI-SCOPE API metadata version 20.5.0d7
functions = {
    'CloseIOTrace': {
        'cname': 'nispy_CloseSpy',
        'parameters': [
        ],
        'returns': 'eNiSpyAPICommandStatus'
    },
    'GetIOTracePath': {
        'cname': 'nispy_GetApplicationPath',
        'codegen_method': 'private',
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
        'returns': 'eNiSpyAPICommandStatus'
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
        'returns': 'eNiSpyAPICommandStatus'
    },
    'OpenIOTrace': {
        'codegen_method': 'CustomGrpcOnly',
        'parameters': [],
        'returns': 'eNiSpyAPICommandStatus'
    },
    'StartTracing': {
        'cname': 'nispy_StartSpying',
        'parameters': [
            {
                'direction': 'in',
                'name': 'logFileSetting',
                'type': 'eNiSpyLogFileSetting',
                'supports_standard_copy_convert': True,
                'actual_enum': True
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
                'supports_standard_copy_convert': True,
                'actual_enum': True
            },
        ],
        'returns': 'eNiSpyAPICommandStatus'
    },
    'StopTracing': {
        'cname': 'nispy_StopSpying',
        'parameters': [
        ],
        'returns': 'eNiSpyAPICommandStatus'
    },    
}
