# -*- coding: utf-8 -*-
# This file is generated from NI-SCOPE API metadata version 20.5.0d7
enums = {
    'FileWriteMode': {
        'force-include': True,
        'values': [
            {
                'name': 'CreateOnly',
                'value': 0
            },
            {
                'name': 'CreateOrAppend',
                'value': 1
            },
            {
                'name': 'CreateOrOverwrite',
                'value': 2
            },
        ]
    },
    'LogFileSetting': {
        'force-include': True,
        'values': [
            {
                'name': 'NoFile',
                'value': -1
            },
            {
                'name': 'Spy',
                'value': 0
            },
            {
                'name': 'PlainText',
                'value': 1
            },
            {
                'name': 'CommaSeparated',
                'value': 2
            },
            {
                'name': 'SettingXml',
                'value': 3
            },
        ]
    },
    'CommandStatus': {
        'force-include': True,
        'values': [
            {
                'name': 'Success',
                'value': 0
            },
            {
                'name': 'NoExecute',
                'value': -303200
            },
            {
                'name': 'IncompatibleState',
                'value': -303201
            },
            {
                'name': 'UnableToOpenLogFile',
                'value': -303202
            },
            {
                'name': 'IOTraceClosed',
                'value': -303203
            },
            {
                'name': 'InvalidSettings',
                'value': -303204
            },
            {
                'name': 'BadParameter',
                'value': -303205
            },
            {
                'name': 'InternalFailure',
                'value': -303206
            },
            {
                'name': 'InvalidFileExtension',
                'value': -303207
            },
            {
                'name': 'BufferTooSmall',
                'value': -303208
            },
            {
                'name': 'FileAlreadyExists',
                'value': -303209
            },
        ]
    },
}
