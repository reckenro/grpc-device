# -*- coding: utf-8 -*-
# This file is generated from NI-DCPower API metadata version 22.8.0d9999
enums = {
    'ApertureTimeAutoMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'APERTURE_TIME_AUTO_MODE_OFF',
                'value': 1135
            },
            {
                'name': 'APERTURE_TIME_AUTO_MODE_SHORT',
                'value': 1136
            },
            {
                'name': 'APERTURE_TIME_AUTO_MODE_NORMAL',
                'value': 1137
            },
            {
                'name': 'APERTURE_TIME_AUTO_MODE_LONG',
                'value': 1138
            }
        ]
    },
    'ApertureTimeUnits': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'SECONDS',
                'value': 1028
            },
            {
                'name': 'POWER_LINE_CYCLES',
                'value': 1029
            }
        ]
    },
    'AutoZero': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'OFF',
                'value': 0
            },
            {
                'name': 'ON',
                'value': 1
            },
            {
                'name': 'ONCE',
                'value': 1024
            }
        ]
    },
    'Autorange': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'OFF',
                'value': 0
            },
            {
                'name': 'ON',
                'value': 1
            }
        ]
    },
    'AutorangeApertureTimeMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'APERTURE_TIME_AUTO',
                'value': 1110
            },
            {
                'name': 'APERTURE_TIME_CUSTOM',
                'value': 1111
            }
        ]
    },
    'AutorangeBehavior': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'RANGE_UP_TO_LIMIT_THEN_DOWN',
                'value': 1107
            },
            {
                'name': 'RANGE_UP',
                'value': 1108
            },
            {
                'name': 'RANGE_UP_AND_DOWN',
                'value': 1109
            }
        ]
    },
    'AutorangeThresholdMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'THRESHOLD_MODE_NORMAL',
                'value': 1112
            },
            {
                'name': 'THRESHOLD_MODE_FAST_STEP',
                'value': 1113
            },
            {
                'name': 'THRESHOLD_MODE_HIGH_HYSTERESIS',
                'value': 1114
            },
            {
                'name': 'THRESHOLD_MODE_MEDIUM_HYSTERESIS',
                'value': 1115
            },
            {
                'name': 'THRESHOLD_MODE_HOLD',
                'value': 1116
            }
        ]
    },
    'CableLength': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'ZERO_M',
                'value': 1121
            },
            {
                'name': 'NI_STANDARD_1M',
                'value': 1122
            },
            {
                'name': 'NI_STANDARD_2M',
                'value': 1123
            },
            {
                'name': 'NI_STANDARD_4M',
                'value': 1124
            },
            {
                'name': 'CUSTOM_ONBOARD_STORAGE',
                'value': 1125
            },
            {
                'name': 'CUSTOM_AS_CONFIGURED',
                'value': 1126
            },
            {
                'name': 'NI_STANDARD_TRIAXIAL_1M',
                'value': 1139
            },
            {
                'name': 'NI_STANDARD_TRIAXIAL_2M',
                'value': 1140
            },
            {
                'name': 'NI_STANDARD_TRIAXIAL_4M',
                'value': 1141
            }
        ]
    },
    'CurrentLevelAutorange': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'OFF',
                'value': 0
            },
            {
                'name': 'ON',
                'value': 1
            }
        ]
    },
    'CurrentLimitAutorange': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'OFF',
                'value': 0
            },
            {
                'name': 'ON',
                'value': 1
            }
        ]
    },
    'DCNoiseRejection': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'DC_NOISE_REJECTION_SECOND_ORDER',
                'value': 1043
            },
            {
                'name': 'DC_NOISE_REJECTION_NORMAL',
                'value': 1044
            }
        ]
    },
    'DigitalEdge': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'RISING',
                'value': 1016
            },
            {
                'name': 'FALLING',
                'value': 1017
            }
        ]
    },
    'ExportSignal': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'SOURCE_COMPLETE_EVENT',
                'value': 1030
            },
            {
                'name': 'MEASURE_COMPLETE_EVENT',
                'value': 1031
            },
            {
                'name': 'SEQUENCE_ITERATION_COMPLETE_EVENT',
                'value': 1032
            },
            {
                'name': 'SEQUENCE_ENGINE_DONE_EVENT',
                'value': 1033
            },
            {
                'name': 'PULSE_COMPLETE_EVENT',
                'value': 1051
            },
            {
                'name': 'READY_FOR_PULSE_TRIGGER_EVENT',
                'value': 1052
            },
            {
                'name': 'START_TRIGGER',
                'value': 1034
            },
            {
                'name': 'SOURCE_TRIGGER',
                'value': 1035
            },
            {
                'name': 'MEASURE_TRIGGER',
                'value': 1036
            },
            {
                'name': 'SEQUENCE_ADVANCE_TRIGGER',
                'value': 1037
            },
            {
                'name': 'PULSE_TRIGGER',
                'value': 1053
            },
            {
                'name': 'SHUTDOWN_TRIGGER',
                'value': 1118
            }
        ]
    },
    'InstrumentMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'SMU_PS',
                'value': 1061
            },
            {
                'name': 'LCR',
                'value': 1062
            }
        ]
    },
    'IsolationState': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'ISOLATED',
                'value': 1128
            },
            {
                'name': 'NON_ISOLATED',
                'value': 1129
            }
        ]
    },
    'LCRAutomaticLevelControl': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'OFF',
                'value': 0
            },
            {
                'name': 'ON',
                'value': 1
            }
        ]
    },
    'LCRCompensationType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'OPEN_COMPENSATION',
                'value': 1130
            },
            {
                'name': 'SHORT_COMPENSATION',
                'value': 1131
            },
            {
                'name': 'LOAD_COMPENSATION',
                'value': 1132
            },
            {
                'name': 'OPEN_CUSTOM_CABLE_COMPENSATION',
                'value': 1133
            },
            {
                'name': 'SHORT_CUSTOM_CABLE_COMPENSATION',
                'value': 1134
            }
        ]
    },
    'LCRDCBiasSource': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'DC_BIAS_OFF',
                'value': 1065
            },
            {
                'name': 'DC_BIAS_VOLTAGE',
                'value': 1066
            },
            {
                'name': 'DC_BIAS_CURRENT',
                'value': 1067
            }
        ]
    },
    'LCRImpedanceAutoRange': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'AUTO_RANGE_OFF',
                'value': 1068
            },
            {
                'name': 'AUTO_RANGE_ON',
                'value': 1070
            }
        ]
    },
    'LCRImpedanceRangeSource': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'LCR_IMPEDANCE_RANGE',
                'value': 1142
            },
            {
                'name': 'LCR_LOAD_CONFIGURATION',
                'value': 1143
            }
        ]
    },
    'LCRMeasurementTime': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'MEASUREMENT_TIME_SHORT',
                'value': 1071
            },
            {
                'name': 'MEASUREMENT_TIME_MEDIUM',
                'value': 1072
            },
            {
                'name': 'MEASUREMENT_TIME_LONG',
                'value': 1073
            },
            {
                'name': 'MEASUREMENT_TIME_CUSTOM',
                'value': 1117
            }
        ]
    },
    'LCROpenShortLoadCompensationDataSource': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'ONBOARD_STORAGE',
                'value': 1074
            },
            {
                'name': 'AS_DEFINED',
                'value': 1075
            }
        ]
    },
    'LCRSourceDelayMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'LCR_SOURCE_DELAY_MODE_AUTOMATIC',
                'value': 1144
            },
            {
                'name': 'LCR_SOURCE_DELAY_MODE_MANUAL',
                'value': 1145
            }
        ]
    },
    'LCRStimulusFunction': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'AC_VOLTAGE',
                'value': 1063
            },
            {
                'name': 'AC_CURRENT',
                'value': 1064
            }
        ]
    },
    'MeasureWhen': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'AUTOMATICALLY_AFTER_SOURCE_COMPLETE',
                'value': 1025
            },
            {
                'name': 'ON_DEMAND',
                'value': 1026
            },
            {
                'name': 'ON_MEASURE_TRIGGER',
                'value': 1027
            }
        ]
    },
    'MeasurementTypes': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'MEASURE_CURRENT',
                'value': 0
            },
            {
                'name': 'MEASURE_VOLTAGE',
                'value': 1
            }
        ]
    },
    'NiDCPowerInt32AttributeValues': {
        'enum-value-prefix': 'NIDCPOWER_INT32',
        'generate-mappings': False,
        'values': [
            {
                'name': 'APERTURE_TIME_AUTO_MODE_APERTURE_TIME_AUTO_MODE_OFF',
                'value': 1135
            },
            {
                'name': 'APERTURE_TIME_AUTO_MODE_APERTURE_TIME_AUTO_MODE_SHORT',
                'value': 1136
            },
            {
                'name': 'APERTURE_TIME_AUTO_MODE_APERTURE_TIME_AUTO_MODE_NORMAL',
                'value': 1137
            },
            {
                'name': 'APERTURE_TIME_AUTO_MODE_APERTURE_TIME_AUTO_MODE_LONG',
                'value': 1138
            },
            {
                'name': 'APERTURE_TIME_UNITS_SECONDS',
                'value': 1028
            },
            {
                'name': 'APERTURE_TIME_UNITS_POWER_LINE_CYCLES',
                'value': 1029
            },
            {
                'name': 'AUTO_ZERO_OFF',
                'value': 0
            },
            {
                'name': 'AUTO_ZERO_ON',
                'value': 1
            },
            {
                'name': 'AUTO_ZERO_ONCE',
                'value': 1024
            },
            {
                'name': 'AUTORANGE_OFF',
                'value': 0
            },
            {
                'name': 'AUTORANGE_ON',
                'value': 1
            },
            {
                'name': 'AUTORANGE_APERTURE_TIME_MODE_APERTURE_TIME_AUTO',
                'value': 1110
            },
            {
                'name': 'AUTORANGE_APERTURE_TIME_MODE_APERTURE_TIME_CUSTOM',
                'value': 1111
            },
            {
                'name': 'AUTORANGE_BEHAVIOR_RANGE_UP_TO_LIMIT_THEN_DOWN',
                'value': 1107
            },
            {
                'name': 'AUTORANGE_BEHAVIOR_RANGE_UP',
                'value': 1108
            },
            {
                'name': 'AUTORANGE_BEHAVIOR_RANGE_UP_AND_DOWN',
                'value': 1109
            },
            {
                'name': 'AUTORANGE_THRESHOLD_MODE_THRESHOLD_MODE_NORMAL',
                'value': 1112
            },
            {
                'name': 'AUTORANGE_THRESHOLD_MODE_THRESHOLD_MODE_FAST_STEP',
                'value': 1113
            },
            {
                'name': 'AUTORANGE_THRESHOLD_MODE_THRESHOLD_MODE_HIGH_HYSTERESIS',
                'value': 1114
            },
            {
                'name': 'AUTORANGE_THRESHOLD_MODE_THRESHOLD_MODE_MEDIUM_HYSTERESIS',
                'value': 1115
            },
            {
                'name': 'AUTORANGE_THRESHOLD_MODE_THRESHOLD_MODE_HOLD',
                'value': 1116
            },
            {
                'name': 'CABLE_LENGTH_ZERO_M',
                'value': 1121
            },
            {
                'name': 'CABLE_LENGTH_NI_STANDARD_1M',
                'value': 1122
            },
            {
                'name': 'CABLE_LENGTH_NI_STANDARD_2M',
                'value': 1123
            },
            {
                'name': 'CABLE_LENGTH_NI_STANDARD_4M',
                'value': 1124
            },
            {
                'name': 'CABLE_LENGTH_CUSTOM_ONBOARD_STORAGE',
                'value': 1125
            },
            {
                'name': 'CABLE_LENGTH_CUSTOM_AS_CONFIGURED',
                'value': 1126
            },
            {
                'name': 'CABLE_LENGTH_NI_STANDARD_TRIAXIAL_1M',
                'value': 1139
            },
            {
                'name': 'CABLE_LENGTH_NI_STANDARD_TRIAXIAL_2M',
                'value': 1140
            },
            {
                'name': 'CABLE_LENGTH_NI_STANDARD_TRIAXIAL_4M',
                'value': 1141
            },
            {
                'name': 'CURRENT_LEVEL_AUTORANGE_OFF',
                'value': 0
            },
            {
                'name': 'CURRENT_LEVEL_AUTORANGE_ON',
                'value': 1
            },
            {
                'name': 'CURRENT_LIMIT_AUTORANGE_OFF',
                'value': 0
            },
            {
                'name': 'CURRENT_LIMIT_AUTORANGE_ON',
                'value': 1
            },
            {
                'name': 'DC_NOISE_REJECTION_DC_NOISE_REJECTION_SECOND_ORDER',
                'value': 1043
            },
            {
                'name': 'DC_NOISE_REJECTION_DC_NOISE_REJECTION_NORMAL',
                'value': 1044
            },
            {
                'name': 'DIGITAL_EDGE_RISING',
                'value': 1016
            },
            {
                'name': 'DIGITAL_EDGE_FALLING',
                'value': 1017
            },
            {
                'name': 'INSTRUMENT_MODE_SMU_PS',
                'value': 1061
            },
            {
                'name': 'INSTRUMENT_MODE_LCR',
                'value': 1062
            },
            {
                'name': 'ISOLATION_STATE_ISOLATED',
                'value': 1128
            },
            {
                'name': 'ISOLATION_STATE_NON_ISOLATED',
                'value': 1129
            },
            {
                'name': 'LCR_AUTOMATIC_LEVEL_CONTROL_OFF',
                'value': 0
            },
            {
                'name': 'LCR_AUTOMATIC_LEVEL_CONTROL_ON',
                'value': 1
            },
            {
                'name': 'LCRDC_BIAS_SOURCE_DC_BIAS_OFF',
                'value': 1065
            },
            {
                'name': 'LCRDC_BIAS_SOURCE_DC_BIAS_VOLTAGE',
                'value': 1066
            },
            {
                'name': 'LCRDC_BIAS_SOURCE_DC_BIAS_CURRENT',
                'value': 1067
            },
            {
                'name': 'LCR_IMPEDANCE_AUTO_RANGE_AUTO_RANGE_OFF',
                'value': 1068
            },
            {
                'name': 'LCR_IMPEDANCE_AUTO_RANGE_AUTO_RANGE_ON',
                'value': 1070
            },
            {
                'name': 'LCR_IMPEDANCE_RANGE_SOURCE_LCR_IMPEDANCE_RANGE',
                'value': 1142
            },
            {
                'name': 'LCR_IMPEDANCE_RANGE_SOURCE_LCR_LOAD_CONFIGURATION',
                'value': 1143
            },
            {
                'name': 'LCR_MEASUREMENT_TIME_MEASUREMENT_TIME_SHORT',
                'value': 1071
            },
            {
                'name': 'LCR_MEASUREMENT_TIME_MEASUREMENT_TIME_MEDIUM',
                'value': 1072
            },
            {
                'name': 'LCR_MEASUREMENT_TIME_MEASUREMENT_TIME_LONG',
                'value': 1073
            },
            {
                'name': 'LCR_MEASUREMENT_TIME_MEASUREMENT_TIME_CUSTOM',
                'value': 1117
            },
            {
                'name': 'LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE_ONBOARD_STORAGE',
                'value': 1074
            },
            {
                'name': 'LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE_AS_DEFINED',
                'value': 1075
            },
            {
                'name': 'LCR_SOURCE_DELAY_MODE_LCR_SOURCE_DELAY_MODE_AUTOMATIC',
                'value': 1144
            },
            {
                'name': 'LCR_SOURCE_DELAY_MODE_LCR_SOURCE_DELAY_MODE_MANUAL',
                'value': 1145
            },
            {
                'name': 'LCR_STIMULUS_FUNCTION_AC_VOLTAGE',
                'value': 1063
            },
            {
                'name': 'LCR_STIMULUS_FUNCTION_AC_CURRENT',
                'value': 1064
            },
            {
                'name': 'MEASURE_WHEN_AUTOMATICALLY_AFTER_SOURCE_COMPLETE',
                'value': 1025
            },
            {
                'name': 'MEASURE_WHEN_ON_DEMAND',
                'value': 1026
            },
            {
                'name': 'MEASURE_WHEN_ON_MEASURE_TRIGGER',
                'value': 1027
            },
            {
                'name': 'OUTPUT_CAPACITANCE_LOW',
                'value': 1010
            },
            {
                'name': 'OUTPUT_CAPACITANCE_HIGH',
                'value': 1011
            },
            {
                'name': 'OUTPUT_FUNCTION_DC_VOLTAGE',
                'value': 1006
            },
            {
                'name': 'OUTPUT_FUNCTION_DC_CURRENT',
                'value': 1007
            },
            {
                'name': 'OUTPUT_FUNCTION_PULSE_VOLTAGE',
                'value': 1049
            },
            {
                'name': 'OUTPUT_FUNCTION_PULSE_CURRENT',
                'value': 1050
            },
            {
                'name': 'POLARITY_ACTIVE_HIGH',
                'value': 1018
            },
            {
                'name': 'POLARITY_ACTIVE_LOW',
                'value': 1019
            },
            {
                'name': 'POWER_ALLOCATION_MODE_POWER_ALLOCATION_MODE_DISABLED',
                'value': 1058
            },
            {
                'name': 'POWER_ALLOCATION_MODE_POWER_ALLOCATION_MODE_AUTOMATIC',
                'value': 1059
            },
            {
                'name': 'POWER_ALLOCATION_MODE_POWER_ALLOCATION_MODE_MANUAL',
                'value': 1060
            },
            {
                'name': 'POWER_SOURCE_INTERNAL',
                'value': 1003
            },
            {
                'name': 'POWER_SOURCE_AUXILIARY',
                'value': 1004
            },
            {
                'name': 'POWER_SOURCE_AUTOMATIC',
                'value': 1005
            },
            {
                'name': 'POWER_SOURCE_IN_USE_INTERNAL',
                'value': 1003
            },
            {
                'name': 'POWER_SOURCE_IN_USE_AUXILIARY',
                'value': 1004
            },
            {
                'name': 'SELF_CALIBRATION_PERSISTENCE_KEEP_IN_MEMORY',
                'value': 1045
            },
            {
                'name': 'SELF_CALIBRATION_PERSISTENCE_WRITE_TO_EEPROM',
                'value': 1046
            },
            {
                'name': 'SENSE_LOCAL',
                'value': 1008
            },
            {
                'name': 'SENSE_REMOTE',
                'value': 1009
            },
            {
                'name': 'SOURCE_MODE_SINGLE_POINT',
                'value': 1020
            },
            {
                'name': 'SOURCE_MODE_SEQUENCE',
                'value': 1021
            },
            {
                'name': 'TRANSIENT_RESPONSE_NORMAL',
                'value': 1038
            },
            {
                'name': 'TRANSIENT_RESPONSE_FAST',
                'value': 1039
            },
            {
                'name': 'TRANSIENT_RESPONSE_SLOW',
                'value': 1041
            },
            {
                'name': 'TRANSIENT_RESPONSE_CUSTOM',
                'value': 1042
            },
            {
                'name': 'TRIGGER_TYPE_NONE',
                'value': 1012
            },
            {
                'name': 'TRIGGER_TYPE_DIGITAL_EDGE',
                'value': 1014
            },
            {
                'name': 'TRIGGER_TYPE_SOFTWARE_EDGE',
                'value': 1015
            },
            {
                'name': 'VOLTAGE_LEVEL_AUTORANGE_OFF',
                'value': 0
            },
            {
                'name': 'VOLTAGE_LEVEL_AUTORANGE_ON',
                'value': 1
            },
            {
                'name': 'VOLTAGE_LIMIT_AUTORANGE_OFF',
                'value': 0
            },
            {
                'name': 'VOLTAGE_LIMIT_AUTORANGE_ON',
                'value': 1
            }
        ]
    },
    'NiDCPowerReal64AttributeValuesMapped': {
        'enum-value-prefix': 'NIDCPOWER_REAL64',
        'generate-mappings': True,
        'values': [
            {
                'name': 'POWER_LINE_FREQUENCY_50_HERTZ',
                'value': 50.0
            },
            {
                'name': 'POWER_LINE_FREQUENCY_60_HERTZ',
                'value': 60.0
            }
        ]
    },
    'OutputCapacitance': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'LOW',
                'value': 1010
            },
            {
                'name': 'HIGH',
                'value': 1011
            }
        ]
    },
    'OutputCutoffReason': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'OUTPUT_CUTOFF_REASON_ALL',
                'value': -1
            },
            {
                'name': 'OUTPUT_CUTOFF_REASON_VOLTAGE_OUTPUT_HIGH',
                'value': 1
            },
            {
                'name': 'OUTPUT_CUTOFF_REASON_VOLTAGE_OUTPUT_LOW',
                'value': 2
            },
            {
                'name': 'OUTPUT_CUTOFF_REASON_CURRENT_MEASURE_HIGH',
                'value': 4
            },
            {
                'name': 'OUTPUT_CUTOFF_REASON_CURRENT_MEASURE_LOW',
                'value': 8
            },
            {
                'name': 'OUTPUT_CUTOFF_REASON_VOLTAGE_CHANGE_HIGH',
                'value': 16
            },
            {
                'name': 'OUTPUT_CUTOFF_REASON_VOLTAGE_CHANGE_LOW',
                'value': 32
            },
            {
                'name': 'OUTPUT_CUTOFF_REASON_CURRENT_CHANGE_HIGH',
                'value': 64
            },
            {
                'name': 'OUTPUT_CUTOFF_REASON_CURRENT_CHANGE_LOW',
                'value': 128
            }
        ]
    },
    'OutputFunction': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'DC_VOLTAGE',
                'value': 1006
            },
            {
                'name': 'DC_CURRENT',
                'value': 1007
            },
            {
                'name': 'PULSE_VOLTAGE',
                'value': 1049
            },
            {
                'name': 'PULSE_CURRENT',
                'value': 1050
            }
        ]
    },
    'OutputStates': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'OUTPUT_CONSTANT_VOLTAGE',
                'value': 0
            },
            {
                'name': 'OUTPUT_CONSTANT_CURRENT',
                'value': 1
            }
        ]
    },
    'Polarity': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'ACTIVE_HIGH',
                'value': 1018
            },
            {
                'name': 'ACTIVE_LOW',
                'value': 1019
            }
        ]
    },
    'PowerAllocationMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'POWER_ALLOCATION_MODE_DISABLED',
                'value': 1058
            },
            {
                'name': 'POWER_ALLOCATION_MODE_AUTOMATIC',
                'value': 1059
            },
            {
                'name': 'POWER_ALLOCATION_MODE_MANUAL',
                'value': 1060
            }
        ]
    },
    'PowerLineFrequency': {
        'codegen_method': 'public',
        'generate-mappings': True,
        'values': [
            {
                'name': '50_HERTZ',
                'value': 50.0
            },
            {
                'name': '60_HERTZ',
                'value': 60.0
            }
        ]
    },
    'PowerSource': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'INTERNAL',
                'value': 1003
            },
            {
                'name': 'AUXILIARY',
                'value': 1004
            },
            {
                'name': 'AUTOMATIC',
                'value': 1005
            }
        ]
    },
    'PowerSourceInUse': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'INTERNAL',
                'value': 1003
            },
            {
                'name': 'AUXILIARY',
                'value': 1004
            }
        ]
    },
    'SelfCalibrationPersistence': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'KEEP_IN_MEMORY',
                'value': 1045
            },
            {
                'name': 'WRITE_TO_EEPROM',
                'value': 1046
            }
        ]
    },
    'Sense': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'LOCAL',
                'value': 1008
            },
            {
                'name': 'REMOTE',
                'value': 1009
            }
        ]
    },
    'SourceMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'SINGLE_POINT',
                'value': 1020
            },
            {
                'name': 'SEQUENCE',
                'value': 1021
            }
        ]
    },
    'TransientResponse': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NORMAL',
                'value': 1038
            },
            {
                'name': 'FAST',
                'value': 1039
            },
            {
                'name': 'SLOW',
                'value': 1041
            },
            {
                'name': 'CUSTOM',
                'value': 1042
            }
        ]
    },
    'TriggerType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NONE',
                'value': 1012
            },
            {
                'name': 'DIGITAL_EDGE',
                'value': 1014
            },
            {
                'name': 'SOFTWARE_EDGE',
                'value': 1015
            }
        ]
    },
    'VoltageLevelAutorange': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'OFF',
                'value': 0
            },
            {
                'name': 'ON',
                'value': 1
            }
        ]
    },
    'VoltageLimitAutorange': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'OFF',
                'value': 0
            },
            {
                'name': 'ON',
                'value': 1
            }
        ]
    }
}
