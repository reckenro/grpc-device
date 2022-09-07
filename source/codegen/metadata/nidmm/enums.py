# -*- coding: utf-8 -*-
# This file is generated from NI-DMM API metadata version 22.8.0d9999
enums = {
    'ADCCalibration': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'ADC_CALIBRATION_OFF',
                'value': 0
            },
            {
                'name': 'ADC_CALIBRATION_AUTO',
                'value': -1
            },
            {
                'name': 'ADC_CALIBRATION_ON',
                'value': 1
            }
        ]
    },
    'AcquisitionStatus': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'ACQUISITION_STATUS_RUNNING',
                'value': 0
            },
            {
                'name': 'ACQUISITION_STATUS_FINISHED_WITH_BACKLOG',
                'value': 1
            },
            {
                'name': 'ACQUISITION_STATUS_FINISHED_WITH_NO_BACKLOG',
                'value': 2
            },
            {
                'name': 'ACQUISITION_STATUS_PAUSED',
                'value': 3
            },
            {
                'name': 'ACQUISITION_STATUS_NO_ACQUISITION_IN_PROGRESS',
                'value': 4
            }
        ]
    },
    'ApertureTimeUnits': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'SECONDS',
                'value': 0
            },
            {
                'name': 'POWER_LINE_CYCLES',
                'value': 1
            }
        ]
    },
    'AutoZero': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'AUTO_ZERO_OFF',
                'value': 0
            },
            {
                'name': 'AUTO_ZERO_AUTO',
                'value': -1
            },
            {
                'name': 'AUTO_ZERO_ON',
                'value': 1
            },
            {
                'name': 'AUTO_ZERO_ONCE',
                'value': 2
            }
        ]
    },
    'CableCompensationType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'CABLE_COMP_NONE',
                'value': 0
            },
            {
                'name': 'CABLE_COMP_OPEN',
                'value': 1
            },
            {
                'name': 'CABLE_COMP_SHORT',
                'value': 2
            },
            {
                'name': 'CABLE_COMP_OPEN_AND_SHORT',
                'value': 3
            }
        ]
    },
    'CurrentSource': {
        'codegen_method': 'public',
        'generate-mappings': True,
        'values': [
            {
                'name': '1_MICROAMP',
                'value': 1e-06
            },
            {
                'name': '10_MICROAMP',
                'value': 1e-05
            },
            {
                'name': '100_MICROAMP',
                'value': 0.0001
            },
            {
                'name': '1_MILLIAMP',
                'value': 0.001
            }
        ]
    },
    'DCBias': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'DC_BIAS_OFF',
                'value': 0
            },
            {
                'name': 'DC_BIAS_ON',
                'value': 1
            }
        ]
    },
    'DCNoiseRejection': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'DCNR_NORMAL',
                'value': 0
            },
            {
                'name': 'DCNR_AUTO',
                'value': -1
            },
            {
                'name': 'DCNR_SECOND_ORDER',
                'value': 1
            },
            {
                'name': 'DCNR_HIGH_ORDER',
                'value': 2
            }
        ]
    },
    'Function': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'DC_VOLTS',
                'value': 1
            },
            {
                'name': 'AC_VOLTS',
                'value': 2
            },
            {
                'name': 'DC_CURRENT',
                'value': 3
            },
            {
                'name': 'AC_CURRENT',
                'value': 4
            },
            {
                'name': '2_WIRE_RES',
                'value': 5
            },
            {
                'name': '4_WIRE_RES',
                'value': 101
            },
            {
                'name': 'FREQ',
                'value': 104
            },
            {
                'name': 'PERIOD',
                'value': 105
            },
            {
                'name': 'TEMPERATURE',
                'value': 108
            },
            {
                'name': 'AC_VOLTS_DC_COUPLED',
                'value': 1001
            },
            {
                'name': 'DIODE',
                'value': 1002
            },
            {
                'name': 'WAVEFORM_VOLTAGE',
                'value': 1003
            },
            {
                'name': 'WAVEFORM_CURRENT',
                'value': 1004
            },
            {
                'name': 'CAPACITANCE',
                'value': 1005
            },
            {
                'name': 'INDUCTANCE',
                'value': 1006
            }
        ]
    },
    'InputResistance': {
        'codegen_method': 'public',
        'generate-mappings': True,
        'values': [
            {
                'name': '1_MEGAOHM',
                'value': 1000000.0
            },
            {
                'name': '10_MEGAOHM',
                'value': 10000000.0
            },
            {
                'name': 'GREATER_THAN_10_GIGAOHM',
                'value': 10000000000.0
            }
        ]
    },
    'LCCalculationModel': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'CALC_MODEL_SERIES',
                'value': 0
            },
            {
                'name': 'CALC_MODEL_AUTO',
                'value': -1
            },
            {
                'name': 'CALC_MODEL_PARALLEL',
                'value': 1
            }
        ]
    },
    'MeasurementCompleteDest': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NONE',
                'value': -1
            },
            {
                'name': 'EXTERNAL',
                'value': 2
            },
            {
                'name': 'PXI_TRIG0',
                'value': 111
            },
            {
                'name': 'PXI_TRIG1',
                'value': 112
            },
            {
                'name': 'PXI_TRIG2',
                'value': 113
            },
            {
                'name': 'PXI_TRIG3',
                'value': 114
            },
            {
                'name': 'PXI_TRIG4',
                'value': 115
            },
            {
                'name': 'PXI_TRIG5',
                'value': 116
            },
            {
                'name': 'PXI_TRIG6',
                'value': 117
            },
            {
                'name': 'PXI_TRIG7',
                'value': 118
            },
            {
                'name': 'LBR_TRIG0',
                'value': 1003
            }
        ]
    },
    'MeasurementDestinationSlope': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'POSITIVE',
                'value': 0
            },
            {
                'name': 'NEGATIVE',
                'value': 1
            }
        ]
    },
    'NiDmmInt32AttributeValues': {
        'enum-value-prefix': 'NIDMM_INT32',
        'generate-mappings': False,
        'values': [
            {
                'name': 'ADC_CALIBRATION_ADC_CALIBRATION_OFF',
                'value': 0
            },
            {
                'name': 'ADC_CALIBRATION_ADC_CALIBRATION_AUTO',
                'value': -1
            },
            {
                'name': 'ADC_CALIBRATION_ADC_CALIBRATION_ON',
                'value': 1
            },
            {
                'name': 'APERTURE_TIME_UNITS_SECONDS',
                'value': 0
            },
            {
                'name': 'APERTURE_TIME_UNITS_POWER_LINE_CYCLES',
                'value': 1
            },
            {
                'name': 'AUTO_ZERO_AUTO_ZERO_OFF',
                'value': 0
            },
            {
                'name': 'AUTO_ZERO_AUTO_ZERO_AUTO',
                'value': -1
            },
            {
                'name': 'AUTO_ZERO_AUTO_ZERO_ON',
                'value': 1
            },
            {
                'name': 'AUTO_ZERO_AUTO_ZERO_ONCE',
                'value': 2
            },
            {
                'name': 'CABLE_COMPENSATION_TYPE_CABLE_COMP_NONE',
                'value': 0
            },
            {
                'name': 'CABLE_COMPENSATION_TYPE_CABLE_COMP_OPEN',
                'value': 1
            },
            {
                'name': 'CABLE_COMPENSATION_TYPE_CABLE_COMP_SHORT',
                'value': 2
            },
            {
                'name': 'CABLE_COMPENSATION_TYPE_CABLE_COMP_OPEN_AND_SHORT',
                'value': 3
            },
            {
                'name': 'DC_BIAS_DC_BIAS_OFF',
                'value': 0
            },
            {
                'name': 'DC_BIAS_DC_BIAS_ON',
                'value': 1
            },
            {
                'name': 'DC_NOISE_REJECTION_DCNR_NORMAL',
                'value': 0
            },
            {
                'name': 'DC_NOISE_REJECTION_DCNR_AUTO',
                'value': -1
            },
            {
                'name': 'DC_NOISE_REJECTION_DCNR_SECOND_ORDER',
                'value': 1
            },
            {
                'name': 'DC_NOISE_REJECTION_DCNR_HIGH_ORDER',
                'value': 2
            },
            {
                'name': 'FUNCTION_DC_VOLTS',
                'value': 1
            },
            {
                'name': 'FUNCTION_AC_VOLTS',
                'value': 2
            },
            {
                'name': 'FUNCTION_DC_CURRENT',
                'value': 3
            },
            {
                'name': 'FUNCTION_AC_CURRENT',
                'value': 4
            },
            {
                'name': 'FUNCTION_2_WIRE_RES',
                'value': 5
            },
            {
                'name': 'FUNCTION_4_WIRE_RES',
                'value': 101
            },
            {
                'name': 'FUNCTION_FREQ',
                'value': 104
            },
            {
                'name': 'FUNCTION_PERIOD',
                'value': 105
            },
            {
                'name': 'FUNCTION_TEMPERATURE',
                'value': 108
            },
            {
                'name': 'FUNCTION_AC_VOLTS_DC_COUPLED',
                'value': 1001
            },
            {
                'name': 'FUNCTION_DIODE',
                'value': 1002
            },
            {
                'name': 'FUNCTION_WAVEFORM_VOLTAGE',
                'value': 1003
            },
            {
                'name': 'FUNCTION_WAVEFORM_CURRENT',
                'value': 1004
            },
            {
                'name': 'FUNCTION_CAPACITANCE',
                'value': 1005
            },
            {
                'name': 'FUNCTION_INDUCTANCE',
                'value': 1006
            },
            {
                'name': 'LC_CALCULATION_MODEL_CALC_MODEL_SERIES',
                'value': 0
            },
            {
                'name': 'LC_CALCULATION_MODEL_CALC_MODEL_AUTO',
                'value': -1
            },
            {
                'name': 'LC_CALCULATION_MODEL_CALC_MODEL_PARALLEL',
                'value': 1
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_NONE',
                'value': -1
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_EXTERNAL',
                'value': 2
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_PXI_TRIG0',
                'value': 111
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_PXI_TRIG1',
                'value': 112
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_PXI_TRIG2',
                'value': 113
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_PXI_TRIG3',
                'value': 114
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_PXI_TRIG4',
                'value': 115
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_PXI_TRIG5',
                'value': 116
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_PXI_TRIG6',
                'value': 117
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_PXI_TRIG7',
                'value': 118
            },
            {
                'name': 'MEASUREMENT_COMPLETE_DEST_LBR_TRIG0',
                'value': 1003
            },
            {
                'name': 'MEASUREMENT_DESTINATION_SLOPE_POSITIVE',
                'value': 0
            },
            {
                'name': 'MEASUREMENT_DESTINATION_SLOPE_NEGATIVE',
                'value': 1
            },
            {
                'name': 'OFFSET_COMPENSATED_OHMS_OFFSET_COMP_OHMS_OFF',
                'value': 0
            },
            {
                'name': 'OFFSET_COMPENSATED_OHMS_OFFSET_COMP_OHMS_ON',
                'value': 1
            },
            {
                'name': 'OPERATION_MODE_IVIDMM_MODE',
                'value': 0
            },
            {
                'name': 'OPERATION_MODE_WAVEFORM_MODE',
                'value': 1
            },
            {
                'name': 'RTD_TYPE_TEMP_RTD_CUSTOM',
                'value': 0
            },
            {
                'name': 'RTD_TYPE_TEMP_RTD_PT3750',
                'value': 1
            },
            {
                'name': 'RTD_TYPE_TEMP_RTD_PT3851',
                'value': 2
            },
            {
                'name': 'RTD_TYPE_TEMP_RTD_PT3911',
                'value': 3
            },
            {
                'name': 'RTD_TYPE_TEMP_RTD_PT3916',
                'value': 4
            },
            {
                'name': 'RTD_TYPE_TEMP_RTD_PT3920',
                'value': 5
            },
            {
                'name': 'RTD_TYPE_TEMP_RTD_PT3928',
                'value': 6
            },
            {
                'name': 'SAMPLE_TRIG_SLOPE_POSITIVE',
                'value': 0
            },
            {
                'name': 'SAMPLE_TRIG_SLOPE_NEGATIVE',
                'value': 1
            },
            {
                'name': 'SAMPLE_TRIGGER_IMMEDIATE',
                'value': 1
            },
            {
                'name': 'SAMPLE_TRIGGER_EXTERNAL',
                'value': 2
            },
            {
                'name': 'SAMPLE_TRIGGER_SOFTWARE_TRIG',
                'value': 3
            },
            {
                'name': 'SAMPLE_TRIGGER_INTERVAL',
                'value': 10
            },
            {
                'name': 'SAMPLE_TRIGGER_PXI_TRIG0',
                'value': 111
            },
            {
                'name': 'SAMPLE_TRIGGER_PXI_TRIG1',
                'value': 112
            },
            {
                'name': 'SAMPLE_TRIGGER_PXI_TRIG2',
                'value': 113
            },
            {
                'name': 'SAMPLE_TRIGGER_PXI_TRIG3',
                'value': 114
            },
            {
                'name': 'SAMPLE_TRIGGER_PXI_TRIG4',
                'value': 115
            },
            {
                'name': 'SAMPLE_TRIGGER_PXI_TRIG5',
                'value': 116
            },
            {
                'name': 'SAMPLE_TRIGGER_PXI_TRIG6',
                'value': 117
            },
            {
                'name': 'SAMPLE_TRIGGER_PXI_TRIG7',
                'value': 118
            },
            {
                'name': 'SAMPLE_TRIGGER_PXI_STAR',
                'value': 131
            },
            {
                'name': 'SAMPLE_TRIGGER_AUX_TRIG1',
                'value': 1001
            },
            {
                'name': 'SAMPLE_TRIGGER_LBR_TRIG1',
                'value': 1004
            },
            {
                'name': 'THERMISTOR_TYPE_TEMP_THERMISTOR_CUSTOM',
                'value': 0
            },
            {
                'name': 'THERMISTOR_TYPE_TEMP_THERMISTOR_44004',
                'value': 1
            },
            {
                'name': 'THERMISTOR_TYPE_TEMP_THERMISTOR_44006',
                'value': 2
            },
            {
                'name': 'THERMISTOR_TYPE_TEMP_THERMISTOR_44007',
                'value': 3
            },
            {
                'name': 'THERMOCOUPLE_REFERENCE_JUNCTION_TYPE_FIXED',
                'value': 2
            },
            {
                'name': 'THERMOCOUPLE_TYPE_TEMP_TC_B',
                'value': 1
            },
            {
                'name': 'THERMOCOUPLE_TYPE_TEMP_TC_E',
                'value': 4
            },
            {
                'name': 'THERMOCOUPLE_TYPE_TEMP_TC_J',
                'value': 6
            },
            {
                'name': 'THERMOCOUPLE_TYPE_TEMP_TC_K',
                'value': 7
            },
            {
                'name': 'THERMOCOUPLE_TYPE_TEMP_TC_N',
                'value': 8
            },
            {
                'name': 'THERMOCOUPLE_TYPE_TEMP_TC_R',
                'value': 9
            },
            {
                'name': 'THERMOCOUPLE_TYPE_TEMP_TC_S',
                'value': 10
            },
            {
                'name': 'THERMOCOUPLE_TYPE_TEMP_TC_T',
                'value': 11
            },
            {
                'name': 'TRANSDUCER_TYPE_THERMOCOUPLE',
                'value': 1
            },
            {
                'name': 'TRANSDUCER_TYPE_THERMISTOR',
                'value': 2
            },
            {
                'name': 'TRANSDUCER_TYPE_2_WIRE_RTD',
                'value': 3
            },
            {
                'name': 'TRANSDUCER_TYPE_4_WIRE_RTD',
                'value': 4
            },
            {
                'name': 'TRIGGER_SLOPE_POSITIVE',
                'value': 0
            },
            {
                'name': 'TRIGGER_SLOPE_NEGATIVE',
                'value': 1
            },
            {
                'name': 'TRIGGER_SOURCE_IMMEDIATE',
                'value': 1
            },
            {
                'name': 'TRIGGER_SOURCE_EXTERNAL',
                'value': 2
            },
            {
                'name': 'TRIGGER_SOURCE_SOFTWARE_TRIG',
                'value': 3
            },
            {
                'name': 'TRIGGER_SOURCE_PXI_TRIG0',
                'value': 111
            },
            {
                'name': 'TRIGGER_SOURCE_PXI_TRIG1',
                'value': 112
            },
            {
                'name': 'TRIGGER_SOURCE_PXI_TRIG2',
                'value': 113
            },
            {
                'name': 'TRIGGER_SOURCE_PXI_TRIG3',
                'value': 114
            },
            {
                'name': 'TRIGGER_SOURCE_PXI_TRIG4',
                'value': 115
            },
            {
                'name': 'TRIGGER_SOURCE_PXI_TRIG5',
                'value': 116
            },
            {
                'name': 'TRIGGER_SOURCE_PXI_TRIG6',
                'value': 117
            },
            {
                'name': 'TRIGGER_SOURCE_PXI_TRIG7',
                'value': 118
            },
            {
                'name': 'TRIGGER_SOURCE_PXI_STAR',
                'value': 131
            },
            {
                'name': 'TRIGGER_SOURCE_AUX_TRIG1',
                'value': 1001
            },
            {
                'name': 'TRIGGER_SOURCE_LBR_TRIG1',
                'value': 1004
            },
            {
                'name': 'WAVEFORM_COUPLING_WAVEFORM_COUPLING_AC',
                'value': 0
            },
            {
                'name': 'WAVEFORM_COUPLING_WAVEFORM_COUPLING_DC',
                'value': 1
            }
        ]
    },
    'NiDmmReal64AttributeValuesMapped': {
        'enum-value-prefix': 'NIDMM_REAL64',
        'generate-mappings': True,
        'values': [
            {
                'name': 'CURRENT_SOURCE_1_MICROAMP',
                'value': 1e-06
            },
            {
                'name': 'CURRENT_SOURCE_10_MICROAMP',
                'value': 1e-05
            },
            {
                'name': 'CURRENT_SOURCE_100_MICROAMP',
                'value': 0.0001
            },
            {
                'name': 'CURRENT_SOURCE_1_MILLIAMP',
                'value': 0.001
            },
            {
                'name': 'INPUT_RESISTANCE_1_MEGAOHM',
                'value': 1000000.0
            },
            {
                'name': 'INPUT_RESISTANCE_10_MEGAOHM',
                'value': 10000000.0
            },
            {
                'name': 'INPUT_RESISTANCE_GREATER_THAN_10_GIGAOHM',
                'value': 10000000000.0
            },
            {
                'name': 'POWERLINE_FREQUENCY_50_HERTZ',
                'value': 50.0
            },
            {
                'name': 'POWERLINE_FREQUENCY_60_HERTZ',
                'value': 60.0
            }
        ]
    },
    'OffsetCompensatedOhms': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'OFFSET_COMP_OHMS_OFF',
                'value': 0
            },
            {
                'name': 'OFFSET_COMP_OHMS_ON',
                'value': 1
            }
        ]
    },
    'OperationMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'IVIDMM_MODE',
                'value': 0
            },
            {
                'name': 'WAVEFORM_MODE',
                'value': 1
            }
        ]
    },
    'PowerlineFrequency': {
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
    'RTDType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'TEMP_RTD_CUSTOM',
                'value': 0
            },
            {
                'name': 'TEMP_RTD_PT3750',
                'value': 1
            },
            {
                'name': 'TEMP_RTD_PT3851',
                'value': 2
            },
            {
                'name': 'TEMP_RTD_PT3911',
                'value': 3
            },
            {
                'name': 'TEMP_RTD_PT3916',
                'value': 4
            },
            {
                'name': 'TEMP_RTD_PT3920',
                'value': 5
            },
            {
                'name': 'TEMP_RTD_PT3928',
                'value': 6
            }
        ]
    },
    'SampleTrigSlope': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'POSITIVE',
                'value': 0
            },
            {
                'name': 'NEGATIVE',
                'value': 1
            }
        ]
    },
    'SampleTrigger': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'IMMEDIATE',
                'value': 1
            },
            {
                'name': 'EXTERNAL',
                'value': 2
            },
            {
                'name': 'SOFTWARE_TRIG',
                'value': 3
            },
            {
                'name': 'INTERVAL',
                'value': 10
            },
            {
                'name': 'PXI_TRIG0',
                'value': 111
            },
            {
                'name': 'PXI_TRIG1',
                'value': 112
            },
            {
                'name': 'PXI_TRIG2',
                'value': 113
            },
            {
                'name': 'PXI_TRIG3',
                'value': 114
            },
            {
                'name': 'PXI_TRIG4',
                'value': 115
            },
            {
                'name': 'PXI_TRIG5',
                'value': 116
            },
            {
                'name': 'PXI_TRIG6',
                'value': 117
            },
            {
                'name': 'PXI_TRIG7',
                'value': 118
            },
            {
                'name': 'PXI_STAR',
                'value': 131
            },
            {
                'name': 'AUX_TRIG1',
                'value': 1001
            },
            {
                'name': 'LBR_TRIG1',
                'value': 1004
            }
        ]
    },
    'ThermistorType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'TEMP_THERMISTOR_CUSTOM',
                'value': 0
            },
            {
                'name': 'TEMP_THERMISTOR_44004',
                'value': 1
            },
            {
                'name': 'TEMP_THERMISTOR_44006',
                'value': 2
            },
            {
                'name': 'TEMP_THERMISTOR_44007',
                'value': 3
            }
        ]
    },
    'ThermocoupleReferenceJunctionType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'FIXED',
                'value': 2
            }
        ]
    },
    'ThermocoupleType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'TEMP_TC_B',
                'value': 1
            },
            {
                'name': 'TEMP_TC_E',
                'value': 4
            },
            {
                'name': 'TEMP_TC_J',
                'value': 6
            },
            {
                'name': 'TEMP_TC_K',
                'value': 7
            },
            {
                'name': 'TEMP_TC_N',
                'value': 8
            },
            {
                'name': 'TEMP_TC_R',
                'value': 9
            },
            {
                'name': 'TEMP_TC_S',
                'value': 10
            },
            {
                'name': 'TEMP_TC_T',
                'value': 11
            }
        ]
    },
    'TransducerType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'THERMOCOUPLE',
                'value': 1
            },
            {
                'name': 'THERMISTOR',
                'value': 2
            },
            {
                'name': '2_WIRE_RTD',
                'value': 3
            },
            {
                'name': '4_WIRE_RTD',
                'value': 4
            }
        ]
    },
    'TriggerSlope': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'POSITIVE',
                'value': 0
            },
            {
                'name': 'NEGATIVE',
                'value': 1
            }
        ]
    },
    'TriggerSource': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'IMMEDIATE',
                'value': 1
            },
            {
                'name': 'EXTERNAL',
                'value': 2
            },
            {
                'name': 'SOFTWARE_TRIG',
                'value': 3
            },
            {
                'name': 'PXI_TRIG0',
                'value': 111
            },
            {
                'name': 'PXI_TRIG1',
                'value': 112
            },
            {
                'name': 'PXI_TRIG2',
                'value': 113
            },
            {
                'name': 'PXI_TRIG3',
                'value': 114
            },
            {
                'name': 'PXI_TRIG4',
                'value': 115
            },
            {
                'name': 'PXI_TRIG5',
                'value': 116
            },
            {
                'name': 'PXI_TRIG6',
                'value': 117
            },
            {
                'name': 'PXI_TRIG7',
                'value': 118
            },
            {
                'name': 'PXI_STAR',
                'value': 131
            },
            {
                'name': 'AUX_TRIG1',
                'value': 1001
            },
            {
                'name': 'LBR_TRIG1',
                'value': 1004
            }
        ]
    },
    'WaveformCoupling': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'WAVEFORM_COUPLING_AC',
                'value': 0
            },
            {
                'name': 'WAVEFORM_COUPLING_DC',
                'value': 1
            }
        ]
    }
}
