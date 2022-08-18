# -*- coding: utf-8 -*-
# This file is generated from NI-FAKE API metadata version 22.8.0d9999
functions = {
    'Abort': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'AcceptListOfDurationsInSeconds': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'count',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'delays',
                'size': {
                    'mechanism': 'len',
                    'value': 'count'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'AcceptViSessionArray': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'name': 'sessionArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'AcceptViUInt32Array': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'arrayLen',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'uInt32Array',
                'size': {
                    'mechanism': 'len',
                    'value': 'arrayLen'
                },
                'type': 'ViUInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'BoolArrayInputFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'anArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'ViBoolean[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'BoolArrayOutputFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'anArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'ViBoolean[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'CloseExtCal': {
        'codegen_method': 'public',
        'custom_close_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'action',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CommandWithReservedParam': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateConfigurationList': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'numberOfListAttributes',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'listAttributeIds',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfListAttributes'
                },
                'type': 'ViAttr[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'DoubleAllTheNums': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'numberCount',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'numbers',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberCount'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnumArrayOutputFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'enum': 'Turtle',
                'name': 'anArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'ViInt16[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnumInputFunctionWithDefaults': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'Turtle',
                'name': 'aTurtle',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationBuffer': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'sizeInBytes',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'configuration',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'sizeInBytes'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchWaveform': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'waveformData',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfSamples'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'name': 'actualNumberOfSamples',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetABoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'aBoolean',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetANumber': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'aNumber',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAStringOfFixedMaximumSize': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'aString',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAnIviDanceString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'aString',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAnIviDanceWithATwistArray': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'aString',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'arrayOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualSize'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'name': 'actualSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAnIviDanceWithATwistArrayOfCustomType': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated FakeCustomStruct',
                'name': 'arrayOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualSize'
                },
                'type': 'struct CustomStruct[]'
            },
            {
                'direction': 'out',
                'name': 'actualSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAnIviDanceWithATwistArrayWithInputArray': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'dataIn',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySizeIn'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeIn',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'arrayOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualSize'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'name': 'actualSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAnIviDanceWithATwistByteArray': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'arrayOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualSize'
                },
                'type': 'ViInt8[]'
            },
            {
                'direction': 'out',
                'name': 'actualSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAnIviDanceWithATwistString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'aString',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualSize'
                },
                'type': 'ViChar[]'
            },
            {
                'direction': 'out',
                'name': 'actualSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAnIviDanceWithATwistStringStrlenBug': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'stringOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'tags': [
                        'strlen-bug'
                    ],
                    'value': 'bufferSize',
                    'value_twist': 'actualSize'
                },
                'type': 'ViChar[]'
            },
            {
                'direction': 'out',
                'name': 'actualSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetArraySizeForCustomCode': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'sizeOut',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetArrayUsingIviDance': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'arrayOut',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetArrayViUInt8WithEnum': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'arrayLen',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'enum': 'Color',
                'name': 'uInt8EnumArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arrayLen'
                },
                'type': 'ViUInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetBitfieldAsEnumArray': {
        'codegen_method': 'public',
        'parameters': [
            {
                'bitfield_as_enum_array': 'Bitfield',
                'direction': 'out',
                'name': 'flags',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCalDateAndTime': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'calType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCalInterval': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'months',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCustomType': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'grpc_type': 'FakeCustomStruct',
                'name': 'cs',
                'type': 'struct CustomStruct'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCustomTypeArray': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated FakeCustomStruct',
                'name': 'cs',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'struct CustomStruct[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetEnumValue': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'aQuantity',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'enum': 'Turtle',
                'name': 'aTurtle',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'private',
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'description',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetViInt32Array': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'arrayLen',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'int32Array',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arrayLen'
                },
                'type': 'ViInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetViUInt32Array': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'arrayLen',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'uInt32Array',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arrayLen'
                },
                'type': 'ViUInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetViUInt8': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'aUint8Number',
                'type': 'ViUInt8'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationBuffer': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'sizeInBytes',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'configuration',
                'size': {
                    'mechanism': 'len',
                    'value': 'sizeInBytes'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitExtCal': {
        'codegen_method': 'public',
        'custom_close': 'CloseExtCal(id, 0)',
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'name': 'calibrationPassword',
                'type': 'ViString'
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitWithOptions': {
        'codegen_method': 'public',
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'optionString',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitWithVarArgs': {
        'codegen_method': 'public',
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'stringArg',
                'repeating_argument': True,
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'enum': 'Turtle',
                'include_in_proto': False,
                'name': 'turtle',
                'repeating_argument': True,
                'type': 'ViInt16'
            },
            {
                'direction': 'in',
                'grpc_type': 'repeated StringAndTurtle',
                'is_compound_type': True,
                'max_length': 3,
                'name': 'nameAndTurtle',
                'repeated_var_args': True,
                'type': 'None'
            }
        ],
        'returns': 'ViStatus'
    },
    'Initiate': {
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'MultipleArrayTypes': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'outputArraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'outputArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'outputArraySize'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'name': 'outputArrayOfFixedLength',
                'size': {
                    'mechanism': 'fixed',
                    'value': 3
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'inputArraySizes',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'inputArrayOfFloats',
                'size': {
                    'mechanism': 'len',
                    'value': 'inputArraySizes'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'inputArrayOfIntegers',
                'size': {
                    'mechanism': 'len',
                    'value': 'inputArraySizes'
                },
                'type': 'ViInt16[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'MultipleArraysSameSize': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'values1',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'values2',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'values3',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'values4',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'MultipleArraysSameSizeWithOptional': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'values1',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'values2',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'values3',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'values4',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'repeated FakeCustomStruct',
                'name': 'values5',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'size'
                },
                'type': 'struct CustomStruct[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'OneInputFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'aNumber',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ParametersAreMultipleTypes': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'aBoolean',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'anInt32',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'anInt64',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'enum': 'Turtle',
                'name': 'anIntEnum',
                'type': 'ViInt16'
            },
            {
                'direction': 'in',
                'name': 'aFloat',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'enum': 'FloatEnum',
                'name': 'aFloatEnum',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'stringSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'aString',
                'size': {
                    'mechanism': 'len',
                    'value': 'stringSize'
                },
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'PoorlyNamedSimpleFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Read': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'maximumTime',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'reading',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadDataWithInOutIviTwist': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'bufferSize'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'name': 'bufferSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadDataWithMultipleIviTwistParamSets': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'arrayOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualSize'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'name': 'actualSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'otherBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'otherArrayOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'otherBufferSize',
                    'value_twist': 'otherActualSize'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'name': 'otherActualSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadFromChannel': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'maximumTime',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'reading',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReturnANumberAndAString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'aNumber',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'name': 'aString',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReturnDurationInSeconds': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'timedelta',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReturnListOfDurationsInSeconds': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'timedeltas',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReturnMultipleTypes': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'aBoolean',
                'type': 'ViBoolean'
            },
            {
                'direction': 'out',
                'name': 'anInt32',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'anInt64',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'enum': 'Turtle',
                'name': 'anIntEnum',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'name': 'aFloat',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'enum': 'FloatEnum',
                'name': 'aFloatEnum',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'anArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'stringSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'aString',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'stringSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt64': {
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetCustomType': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'grpc_type': 'FakeCustomStruct',
                'name': 'cs',
                'type': 'struct CustomStruct'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetCustomTypeArray': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'grpc_type': 'repeated FakeCustomStruct',
                'name': 'cs',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfElements'
                },
                'type': 'struct CustomStruct[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'StringValuedEnumInputFunctionWithDefaults': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'MobileOSNames',
                'name': 'aMobileOSName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'TwoInputFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'aNumber',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'aString',
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Use64BitNumber': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'input',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'name': 'output',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'UseATwoDimensionParameter': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'array',
                'size': {
                    'mechanism': 'two-dimension',
                    'value': 'arrayLengths'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'in',
                'name': 'arrayLengths',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ViInt16ArrayInputFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'anArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfElements'
                },
                'type': 'ViInt16[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ViUInt8ArrayInputFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'anArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'ViUInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ViUInt8ArrayOutputFunction': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'anArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'ViUInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteWaveform': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'waveform',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'close': {
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'error_message': {
        'codegen_method': 'private',
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'self_test': {
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'name': 'selfTestMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    }
}
