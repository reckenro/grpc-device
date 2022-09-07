# -*- coding: utf-8 -*-
# This file is generated from NI-DMM API metadata version 22.8.0d9999
attributes = {
    1050002: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'RANGE_CHECK',
        'type': 'ViBoolean'
    },
    1050003: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'QUERY_INSTRUMENT_STATUS',
        'type': 'ViBoolean'
    },
    1050004: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'CACHE',
        'type': 'ViBoolean'
    },
    1050005: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'SIMULATE',
        'type': 'ViBoolean'
    },
    1050006: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'RECORD_COERCIONS',
        'type': 'ViBoolean'
    },
    1050007: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DRIVER_SETUP',
        'type': 'ViString'
    },
    1050021: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'INTERCHANGE_CHECK',
        'type': 'ViBoolean'
    },
    1050101: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'PRIMARY_ERROR',
        'type': 'ViInt32'
    },
    1050102: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SECONDARY_ERROR',
        'type': 'ViInt32'
    },
    1050103: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'ERROR_ELABORATION',
        'type': 'ViString'
    },
    1050203: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'CHANNEL_COUNT',
        'type': 'ViInt32'
    },
    1050302: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'type': 'ViString'
    },
    1050304: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'type': 'ViString'
    },
    1050305: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'LOGICAL_NAME',
        'type': 'ViString'
    },
    1050327: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'type': 'ViString'
    },
    1050401: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'GROUP_CAPABILITIES',
        'type': 'ViString'
    },
    1050501: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'ENGINE_MAJOR_VERSION',
        'type': 'ViInt32'
    },
    1050502: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'ENGINE_MINOR_VERSION',
        'type': 'ViInt32'
    },
    1050503: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SPECIFIC_DRIVER_MAJOR_VERSION',
        'type': 'ViInt32'
    },
    1050504: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SPECIFIC_DRIVER_MINOR_VERSION',
        'type': 'ViInt32'
    },
    1050510: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'type': 'ViString'
    },
    1050511: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_MANUFACTURER',
        'type': 'ViString'
    },
    1050512: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_MODEL',
        'type': 'ViString'
    },
    1050513: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'type': 'ViString'
    },
    1050514: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'type': 'ViString'
    },
    1050515: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'type': 'ViInt32'
    },
    1050516: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'type': 'ViInt32'
    },
    1050551: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'type': 'ViString'
    },
    1050553: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'ENGINE_REVISION',
        'type': 'ViString'
    },
    1150001: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'ID_QUERY_RESPONSE',
        'type': 'ViString'
    },
    1150002: {
        'codegen_method': 'public',
        'enum': 'MeasurementDestinationSlope',
        'grpc_type': 'sint32',
        'name': 'MEAS_DEST_SLOPE',
        'type': 'ViInt32'
    },
    1150003: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SHUNT_VALUE',
        'type': 'ViReal64'
    },
    1150010: {
        'codegen_method': 'public',
        'enum': 'SampleTrigSlope',
        'grpc_type': 'sint32',
        'name': 'SAMPLE_TRIGGER_SLOPE',
        'type': 'ViInt32'
    },
    1150014: {
        'codegen_method': 'public',
        'enum': 'OperationMode',
        'grpc_type': 'sint32',
        'name': 'OPERATION_MODE',
        'type': 'ViInt32'
    },
    1150018: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'WAVEFORM_RATE',
        'type': 'ViReal64'
    },
    1150019: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'WAVEFORM_POINTS',
        'type': 'ViInt32'
    },
    1150022: {
        'codegen_method': 'public',
        'enum': 'ADCCalibration',
        'grpc_type': 'sint32',
        'name': 'ADC_CALIBRATION',
        'type': 'ViInt32'
    },
    1150023: {
        'codegen_method': 'public',
        'enum': 'OffsetCompensatedOhms',
        'grpc_type': 'sint32',
        'name': 'OFFSET_COMP_OHMS',
        'type': 'ViInt32'
    },
    1150025: {
        'codegen_method': 'public',
        'enum': 'CurrentSource',
        'grpc_type': 'double',
        'name': 'CURRENT_SOURCE',
        'type': 'ViReal64'
    },
    1150026: {
        'codegen_method': 'public',
        'enum': 'DCNoiseRejection',
        'grpc_type': 'sint32',
        'name': 'DC_NOISE_REJECTION',
        'type': 'ViInt32'
    },
    1150027: {
        'codegen_method': 'public',
        'enum': 'WaveformCoupling',
        'grpc_type': 'sint32',
        'name': 'WAVEFORM_COUPLING',
        'type': 'ViInt32'
    },
    1150028: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SETTLE_TIME',
        'type': 'ViReal64'
    },
    1150029: {
        'codegen_method': 'public',
        'enum': 'InputResistance',
        'grpc_type': 'double',
        'name': 'INPUT_RESISTANCE',
        'type': 'ViReal64'
    },
    1150031: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SAMPLE_DELAY_MODE',
        'type': 'ViInt32'
    },
    1150032: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'NUMBER_OF_AVERAGES',
        'type': 'ViInt32'
    },
    1150034: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'LATENCY',
        'type': 'ViInt32'
    },
    1150037: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'BUFFER_SIZE',
        'type': 'ViInt32'
    },
    1150044: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'FREQ_VOLTAGE_AUTO_RANGE',
        'type': 'ViReal64'
    },
    1150045: {
        'codegen_method': 'public',
        'enum': 'CableCompensationType',
        'grpc_type': 'sint32',
        'name': 'CABLE_COMP_TYPE',
        'type': 'ViInt32'
    },
    1150046: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SHORT_CABLE_COMP_REACTANCE',
        'type': 'ViReal64'
    },
    1150047: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SHORT_CABLE_COMP_RESISTANCE',
        'type': 'ViReal64'
    },
    1150048: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OPEN_CABLE_COMP_SUSCEPTANCE',
        'type': 'ViReal64'
    },
    1150049: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OPEN_CABLE_COMP_CONDUCTANCE',
        'type': 'ViReal64'
    },
    1150052: {
        'codegen_method': 'public',
        'enum': 'LCCalculationModel',
        'grpc_type': 'sint32',
        'name': 'LC_CALCULATION_MODEL',
        'type': 'ViInt32'
    },
    1150053: {
        'codegen_method': 'public',
        'enum': 'DCBias',
        'grpc_type': 'sint32',
        'name': 'DC_BIAS',
        'type': 'ViInt32'
    },
    1150054: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SERIAL_NUMBER',
        'type': 'ViString'
    },
    1150055: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'LC_NUMBER_MEAS_TO_AVERAGE',
        'type': 'ViInt32'
    },
    1150061: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'INSTRUMENT_PRODUCT_ID',
        'type': 'ViInt32'
    },
    1150120: {
        'codegen_method': 'public',
        'enum': 'RTDType',
        'grpc_type': 'sint32',
        'name': 'TEMP_RTD_TYPE',
        'type': 'ViInt32'
    },
    1150121: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TEMP_RTD_A',
        'type': 'ViReal64'
    },
    1150122: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TEMP_RTD_B',
        'type': 'ViReal64'
    },
    1150123: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TEMP_RTD_C',
        'type': 'ViReal64'
    },
    1150124: {
        'codegen_method': 'public',
        'enum': 'ThermistorType',
        'grpc_type': 'sint32',
        'name': 'TEMP_THERMISTOR_TYPE',
        'type': 'ViInt32'
    },
    1150125: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TEMP_THERMISTOR_A',
        'type': 'ViReal64'
    },
    1150126: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TEMP_THERMISTOR_B',
        'type': 'ViReal64'
    },
    1150127: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TEMP_THERMISTOR_C',
        'type': 'ViReal64'
    },
    1250001: {
        'codegen_method': 'public',
        'enum': 'Function',
        'grpc_type': 'sint32',
        'name': 'FUNCTION',
        'type': 'ViInt32'
    },
    1250002: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'RANGE',
        'type': 'ViReal64'
    },
    1250003: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'RESOLUTION_DIGITS',
        'type': 'ViReal64'
    },
    1250004: {
        'codegen_method': 'public',
        'enum': 'TriggerSource',
        'grpc_type': 'sint32',
        'name': 'TRIGGER_SOURCE',
        'type': 'ViInt32'
    },
    1250005: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TRIGGER_DELAY',
        'type': 'ViReal64'
    },
    1250006: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'AC_MIN_FREQ',
        'type': 'ViReal64'
    },
    1250007: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'AC_MAX_FREQ',
        'type': 'ViReal64'
    },
    1250008: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'RESOLUTION_ABSOLUTE',
        'type': 'ViReal64'
    },
    1250101: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'FREQ_VOLTAGE_RANGE',
        'type': 'ViReal64'
    },
    1250201: {
        'codegen_method': 'public',
        'enum': 'TransducerType',
        'grpc_type': 'sint32',
        'name': 'TEMP_TRANSDUCER_TYPE',
        'type': 'ViInt32'
    },
    1250231: {
        'codegen_method': 'public',
        'enum': 'ThermocoupleType',
        'grpc_type': 'sint32',
        'name': 'TEMP_TC_TYPE',
        'type': 'ViInt32'
    },
    1250232: {
        'codegen_method': 'public',
        'enum': 'ThermocoupleReferenceJunctionType',
        'grpc_type': 'sint32',
        'name': 'TEMP_TC_REF_JUNC_TYPE',
        'type': 'ViInt32'
    },
    1250233: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TEMP_TC_FIXED_REF_JUNC',
        'type': 'ViReal64'
    },
    1250242: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TEMP_RTD_RES',
        'type': 'ViReal64'
    },
    1250301: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SAMPLE_COUNT',
        'type': 'ViInt32'
    },
    1250302: {
        'codegen_method': 'public',
        'enum': 'SampleTrigger',
        'grpc_type': 'sint32',
        'name': 'SAMPLE_TRIGGER',
        'type': 'ViInt32'
    },
    1250303: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SAMPLE_INTERVAL',
        'type': 'ViReal64'
    },
    1250304: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'TRIGGER_COUNT',
        'type': 'ViInt32'
    },
    1250305: {
        'codegen_method': 'public',
        'enum': 'MeasurementCompleteDest',
        'grpc_type': 'sint32',
        'name': 'MEAS_COMPLETE_DEST',
        'type': 'ViInt32'
    },
    1250321: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'APERTURE_TIME',
        'type': 'ViReal64'
    },
    1250322: {
        'codegen_method': 'public',
        'enum': 'ApertureTimeUnits',
        'grpc_type': 'sint32',
        'name': 'APERTURE_TIME_UNITS',
        'type': 'ViInt32'
    },
    1250331: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'AUTO_RANGE_VALUE',
        'type': 'ViReal64'
    },
    1250332: {
        'codegen_method': 'public',
        'enum': 'AutoZero',
        'grpc_type': 'sint32',
        'name': 'AUTO_ZERO',
        'type': 'ViInt32'
    },
    1250333: {
        'codegen_method': 'public',
        'enum': 'PowerlineFrequency',
        'grpc_type': 'double',
        'name': 'POWERLINE_FREQ',
        'type': 'ViReal64'
    },
    1250334: {
        'codegen_method': 'public',
        'enum': 'TriggerSlope',
        'grpc_type': 'sint32',
        'name': 'TRIGGER_SLOPE',
        'type': 'ViInt32'
    }
}
