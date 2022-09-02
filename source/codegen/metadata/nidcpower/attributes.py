# -*- coding: utf-8 -*-
# This file is generated from NI-DCPower API metadata version 22.8.0d9999
attributes = {
    1050002: {
        'codegen_method': 'public',
        'name': 'RANGE_CHECK',
        'type': 'ViBoolean'
    },
    1050003: {
        'codegen_method': 'public',
        'name': 'QUERY_INSTRUMENT_STATUS',
        'type': 'ViBoolean'
    },
    1050004: {
        'codegen_method': 'public',
        'name': 'CACHE',
        'type': 'ViBoolean'
    },
    1050005: {
        'codegen_method': 'public',
        'name': 'SIMULATE',
        'type': 'ViBoolean'
    },
    1050006: {
        'codegen_method': 'public',
        'name': 'RECORD_COERCIONS',
        'type': 'ViBoolean'
    },
    1050007: {
        'codegen_method': 'public',
        'name': 'DRIVER_SETUP',
        'type': 'ViString'
    },
    1050021: {
        'codegen_method': 'public',
        'name': 'INTERCHANGE_CHECK',
        'type': 'ViBoolean'
    },
    1050203: {
        'codegen_method': 'public',
        'name': 'CHANNEL_COUNT',
        'type': 'ViInt32'
    },
    1050302: {
        'codegen_method': 'public',
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'type': 'ViString'
    },
    1050304: {
        'codegen_method': 'public',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'type': 'ViString'
    },
    1050305: {
        'codegen_method': 'public',
        'name': 'LOGICAL_NAME',
        'type': 'ViString'
    },
    1050327: {
        'codegen_method': 'public',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'type': 'ViString'
    },
    1050401: {
        'codegen_method': 'public',
        'name': 'GROUP_CAPABILITIES',
        'type': 'ViString'
    },
    1050510: {
        'codegen_method': 'public',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'type': 'ViString'
    },
    1050511: {
        'codegen_method': 'public',
        'name': 'INSTRUMENT_MANUFACTURER',
        'type': 'ViString'
    },
    1050512: {
        'codegen_method': 'public',
        'name': 'INSTRUMENT_MODEL',
        'type': 'ViString'
    },
    1050513: {
        'codegen_method': 'public',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'type': 'ViString'
    },
    1050514: {
        'codegen_method': 'public',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'type': 'ViString'
    },
    1050515: {
        'codegen_method': 'public',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'type': 'ViInt32'
    },
    1050516: {
        'codegen_method': 'public',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'type': 'ViInt32'
    },
    1050551: {
        'codegen_method': 'public',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'type': 'ViString'
    },
    1150000: {
        'codegen_method': 'public',
        'enum': 'PowerSource',
        'name': 'POWER_SOURCE',
        'type': 'ViInt32'
    },
    1150001: {
        'codegen_method': 'public',
        'enum': 'PowerSourceInUse',
        'name': 'POWER_SOURCE_IN_USE',
        'type': 'ViInt32'
    },
    1150002: {
        'codegen_method': 'public',
        'name': 'AUXILIARY_POWER_SOURCE_AVAILABLE',
        'type': 'ViBoolean'
    },
    1150003: {
        'codegen_method': 'public',
        'name': 'SAMPLES_TO_AVERAGE',
        'type': 'ViInt32'
    },
    1150004: {
        'codegen_method': 'public',
        'name': 'CURRENT_LIMIT_RANGE',
        'type': 'ViReal64'
    },
    1150005: {
        'codegen_method': 'public',
        'name': 'VOLTAGE_LEVEL_RANGE',
        'type': 'ViReal64'
    },
    1150006: {
        'codegen_method': 'public',
        'name': 'RESET_AVERAGE_BEFORE_MEASUREMENT',
        'type': 'ViBoolean'
    },
    1150007: {
        'codegen_method': 'public',
        'name': 'OVERRANGING_ENABLED',
        'type': 'ViBoolean'
    },
    1150008: {
        'codegen_method': 'public',
        'enum': 'OutputFunction',
        'name': 'OUTPUT_FUNCTION',
        'type': 'ViInt32'
    },
    1150009: {
        'codegen_method': 'public',
        'name': 'CURRENT_LEVEL',
        'type': 'ViReal64'
    },
    1150010: {
        'codegen_method': 'public',
        'name': 'VOLTAGE_LIMIT',
        'type': 'ViReal64'
    },
    1150011: {
        'codegen_method': 'public',
        'name': 'CURRENT_LEVEL_RANGE',
        'type': 'ViReal64'
    },
    1150012: {
        'codegen_method': 'public',
        'name': 'VOLTAGE_LIMIT_RANGE',
        'type': 'ViReal64'
    },
    1150013: {
        'codegen_method': 'public',
        'enum': 'Sense',
        'name': 'SENSE',
        'type': 'ViInt32'
    },
    1150014: {
        'codegen_method': 'public',
        'enum': 'OutputCapacitance',
        'name': 'OUTPUT_CAPACITANCE',
        'type': 'ViInt32'
    },
    1150015: {
        'codegen_method': 'public',
        'enum': 'VoltageLevelAutorange',
        'name': 'VOLTAGE_LEVEL_AUTORANGE',
        'type': 'ViInt32'
    },
    1150016: {
        'codegen_method': 'public',
        'enum': 'CurrentLimitAutorange',
        'name': 'CURRENT_LIMIT_AUTORANGE',
        'type': 'ViInt32'
    },
    1150017: {
        'codegen_method': 'public',
        'enum': 'CurrentLevelAutorange',
        'name': 'CURRENT_LEVEL_AUTORANGE',
        'type': 'ViInt32'
    },
    1150018: {
        'codegen_method': 'public',
        'enum': 'VoltageLimitAutorange',
        'name': 'VOLTAGE_LIMIT_AUTORANGE',
        'type': 'ViInt32'
    },
    1150020: {
        'codegen_method': 'public',
        'enum': 'PowerLineFrequency',
        'name': 'POWER_LINE_FREQUENCY',
        'type': 'ViReal64'
    },
    1150021: {
        'codegen_method': 'public',
        'enum': 'TriggerType',
        'name': 'START_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150022: {
        'codegen_method': 'public',
        'enum': 'DigitalEdge',
        'name': 'DIGITAL_EDGE_START_TRIGGER_EDGE',
        'type': 'ViInt32'
    },
    1150023: {
        'codegen_method': 'public',
        'name': 'DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL',
        'type': 'ViString'
    },
    1150024: {
        'codegen_method': 'public',
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150025: {
        'codegen_method': 'public',
        'name': 'SEQUENCE_LOOP_COUNT',
        'type': 'ViInt32'
    },
    1150026: {
        'codegen_method': 'public',
        'enum': 'TriggerType',
        'name': 'SEQUENCE_ADVANCE_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150027: {
        'codegen_method': 'public',
        'enum': 'DigitalEdge',
        'name': 'DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE',
        'type': 'ViInt32'
    },
    1150028: {
        'codegen_method': 'public',
        'name': 'DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL',
        'type': 'ViString'
    },
    1150029: {
        'codegen_method': 'public',
        'name': 'EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150030: {
        'codegen_method': 'public',
        'enum': 'TriggerType',
        'name': 'SOURCE_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150031: {
        'codegen_method': 'public',
        'enum': 'DigitalEdge',
        'name': 'DIGITAL_EDGE_SOURCE_TRIGGER_EDGE',
        'type': 'ViInt32'
    },
    1150032: {
        'codegen_method': 'public',
        'name': 'DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL',
        'type': 'ViString'
    },
    1150033: {
        'codegen_method': 'public',
        'name': 'EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150034: {
        'codegen_method': 'public',
        'enum': 'TriggerType',
        'name': 'MEASURE_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150035: {
        'codegen_method': 'public',
        'enum': 'DigitalEdge',
        'name': 'DIGITAL_EDGE_MEASURE_TRIGGER_EDGE',
        'type': 'ViInt32'
    },
    1150036: {
        'codegen_method': 'public',
        'name': 'DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL',
        'type': 'ViString'
    },
    1150037: {
        'codegen_method': 'public',
        'name': 'EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150038: {
        'codegen_method': 'public',
        'enum': 'Polarity',
        'name': 'SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY',
        'type': 'ViInt32'
    },
    1150039: {
        'codegen_method': 'public',
        'name': 'SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH',
        'type': 'ViReal64'
    },
    1150040: {
        'codegen_method': 'public',
        'name': 'SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150041: {
        'codegen_method': 'public',
        'enum': 'Polarity',
        'name': 'SOURCE_COMPLETE_EVENT_PULSE_POLARITY',
        'type': 'ViInt32'
    },
    1150042: {
        'codegen_method': 'public',
        'name': 'SOURCE_COMPLETE_EVENT_PULSE_WIDTH',
        'type': 'ViReal64'
    },
    1150043: {
        'codegen_method': 'public',
        'name': 'SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150044: {
        'codegen_method': 'public',
        'enum': 'Polarity',
        'name': 'MEASURE_COMPLETE_EVENT_PULSE_POLARITY',
        'type': 'ViInt32'
    },
    1150045: {
        'codegen_method': 'public',
        'name': 'MEASURE_COMPLETE_EVENT_PULSE_WIDTH',
        'type': 'ViReal64'
    },
    1150046: {
        'codegen_method': 'public',
        'name': 'MEASURE_COMPLETE_EVENT_DELAY',
        'type': 'ViReal64'
    },
    1150047: {
        'codegen_method': 'public',
        'name': 'MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150048: {
        'codegen_method': 'public',
        'enum': 'Polarity',
        'name': 'SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY',
        'type': 'ViInt32'
    },
    1150049: {
        'codegen_method': 'public',
        'name': 'SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH',
        'type': 'ViReal64'
    },
    1150050: {
        'codegen_method': 'public',
        'name': 'SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150051: {
        'codegen_method': 'public',
        'name': 'SOURCE_DELAY',
        'type': 'ViReal64'
    },
    1150054: {
        'codegen_method': 'public',
        'enum': 'SourceMode',
        'name': 'SOURCE_MODE',
        'type': 'ViInt32'
    },
    1150055: {
        'codegen_method': 'public',
        'enum': 'AutoZero',
        'name': 'AUTO_ZERO',
        'type': 'ViInt32'
    },
    1150056: {
        'codegen_method': 'public',
        'name': 'FETCH_BACKLOG',
        'type': 'ViInt32'
    },
    1150057: {
        'codegen_method': 'public',
        'enum': 'MeasureWhen',
        'name': 'MEASURE_WHEN',
        'type': 'ViInt32'
    },
    1150058: {
        'codegen_method': 'public',
        'name': 'APERTURE_TIME',
        'type': 'ViReal64'
    },
    1150059: {
        'codegen_method': 'public',
        'enum': 'ApertureTimeUnits',
        'name': 'APERTURE_TIME_UNITS',
        'type': 'ViInt32'
    },
    1150060: {
        'codegen_method': 'public',
        'name': 'OUTPUT_CONNECTED',
        'type': 'ViBoolean'
    },
    1150061: {
        'codegen_method': 'public',
        'name': 'OUTPUT_RESISTANCE',
        'type': 'ViReal64'
    },
    1150062: {
        'codegen_method': 'public',
        'enum': 'TransientResponse',
        'name': 'TRANSIENT_RESPONSE',
        'type': 'ViInt32'
    },
    1150063: {
        'codegen_method': 'public',
        'name': 'MEASURE_RECORD_LENGTH',
        'type': 'ViInt32'
    },
    1150064: {
        'codegen_method': 'public',
        'name': 'MEASURE_RECORD_LENGTH_IS_FINITE',
        'type': 'ViBoolean'
    },
    1150065: {
        'codegen_method': 'public',
        'name': 'MEASURE_RECORD_DELTA_TIME',
        'type': 'ViReal64'
    },
    1150066: {
        'codegen_method': 'public',
        'enum': 'DCNoiseRejection',
        'name': 'DC_NOISE_REJECTION',
        'type': 'ViInt32'
    },
    1150067: {
        'codegen_method': 'public',
        'name': 'VOLTAGE_GAIN_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150068: {
        'codegen_method': 'public',
        'name': 'VOLTAGE_COMPENSATION_FREQUENCY',
        'type': 'ViReal64'
    },
    1150069: {
        'codegen_method': 'public',
        'name': 'VOLTAGE_POLE_ZERO_RATIO',
        'type': 'ViReal64'
    },
    1150070: {
        'codegen_method': 'public',
        'name': 'CURRENT_GAIN_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150071: {
        'codegen_method': 'public',
        'name': 'CURRENT_COMPENSATION_FREQUENCY',
        'type': 'ViReal64'
    },
    1150072: {
        'codegen_method': 'public',
        'name': 'CURRENT_POLE_ZERO_RATIO',
        'type': 'ViReal64'
    },
    1150073: {
        'codegen_method': 'public',
        'enum': 'SelfCalibrationPersistence',
        'name': 'SELF_CALIBRATION_PERSISTENCE',
        'type': 'ViInt32'
    },
    1150074: {
        'codegen_method': 'public',
        'name': 'ACTIVE_ADVANCED_SEQUENCE',
        'type': 'ViString'
    },
    1150075: {
        'codegen_method': 'public',
        'name': 'ACTIVE_ADVANCED_SEQUENCE_STEP',
        'type': 'ViInt64'
    },
    1150077: {
        'codegen_method': 'public',
        'name': 'MEASURE_BUFFER_SIZE',
        'type': 'ViInt32'
    },
    1150078: {
        'codegen_method': 'public',
        'name': 'SEQUENCE_LOOP_COUNT_IS_FINITE',
        'type': 'ViBoolean'
    },
    1150079: {
        'codegen_method': 'public',
        'name': 'SUPPORT_OUTPUT_DMA',
        'type': 'bool'
    },
    1150080: {
        'codegen_method': 'public',
        'name': 'PULSE_VOLTAGE_LEVEL',
        'type': 'ViReal64'
    },
    1150081: {
        'codegen_method': 'public',
        'name': 'PULSE_CURRENT_LIMIT',
        'type': 'ViReal64'
    },
    1150082: {
        'codegen_method': 'public',
        'name': 'PULSE_BIAS_VOLTAGE_LEVEL',
        'type': 'ViReal64'
    },
    1150083: {
        'codegen_method': 'public',
        'name': 'PULSE_BIAS_CURRENT_LIMIT',
        'type': 'ViReal64'
    },
    1150084: {
        'codegen_method': 'public',
        'name': 'PULSE_VOLTAGE_LEVEL_RANGE',
        'type': 'ViReal64'
    },
    1150085: {
        'codegen_method': 'public',
        'name': 'PULSE_CURRENT_LIMIT_RANGE',
        'type': 'ViReal64'
    },
    1150086: {
        'codegen_method': 'public',
        'name': 'PULSE_CURRENT_LEVEL',
        'type': 'ViReal64'
    },
    1150087: {
        'codegen_method': 'public',
        'name': 'PULSE_VOLTAGE_LIMIT',
        'type': 'ViReal64'
    },
    1150088: {
        'codegen_method': 'public',
        'name': 'PULSE_BIAS_CURRENT_LEVEL',
        'type': 'ViReal64'
    },
    1150089: {
        'codegen_method': 'public',
        'name': 'PULSE_BIAS_VOLTAGE_LIMIT',
        'type': 'ViReal64'
    },
    1150090: {
        'codegen_method': 'public',
        'name': 'PULSE_CURRENT_LEVEL_RANGE',
        'type': 'ViReal64'
    },
    1150091: {
        'codegen_method': 'public',
        'name': 'PULSE_VOLTAGE_LIMIT_RANGE',
        'type': 'ViReal64'
    },
    1150092: {
        'codegen_method': 'public',
        'name': 'PULSE_BIAS_DELAY',
        'type': 'ViReal64'
    },
    1150093: {
        'codegen_method': 'public',
        'name': 'PULSE_ON_TIME',
        'type': 'ViReal64'
    },
    1150094: {
        'codegen_method': 'public',
        'name': 'PULSE_OFF_TIME',
        'type': 'ViReal64'
    },
    1150095: {
        'codegen_method': 'public',
        'enum': 'TriggerType',
        'name': 'PULSE_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150096: {
        'codegen_method': 'public',
        'enum': 'DigitalEdge',
        'name': 'DIGITAL_EDGE_PULSE_TRIGGER_EDGE',
        'type': 'ViInt32'
    },
    1150097: {
        'codegen_method': 'public',
        'name': 'DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL',
        'type': 'ViString'
    },
    1150098: {
        'codegen_method': 'public',
        'name': 'EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150099: {
        'codegen_method': 'public',
        'name': 'PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150100: {
        'codegen_method': 'public',
        'enum': 'Polarity',
        'name': 'PULSE_COMPLETE_EVENT_PULSE_POLARITY',
        'type': 'ViInt32'
    },
    1150101: {
        'codegen_method': 'public',
        'name': 'PULSE_COMPLETE_EVENT_PULSE_WIDTH',
        'type': 'ViReal64'
    },
    1150102: {
        'codegen_method': 'public',
        'name': 'READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150103: {
        'codegen_method': 'public',
        'enum': 'Polarity',
        'name': 'READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY',
        'type': 'ViInt32'
    },
    1150104: {
        'codegen_method': 'public',
        'name': 'READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH',
        'type': 'ViReal64'
    },
    1150105: {
        'codegen_method': 'public',
        'name': 'INTERLOCK_INPUT_OPEN',
        'type': 'ViBoolean'
    },
    1150110: {
        'codegen_method': 'public',
        'name': 'INSTRUMENT_API_SESSION_HANDLE',
        'type': 'ViInt64'
    },
    1150111: {
        'codegen_method': 'public',
        'name': 'WAS_SESSION_OPENED_BY_INITIALIZE_WITH_INDEPENDENT_CHANNELS',
        'type': 'bool'
    },
    1150152: {
        'codegen_method': 'public',
        'name': 'SERIAL_NUMBER',
        'type': 'ViString'
    },
    1150184: {
        'codegen_method': 'public',
        'name': 'COMPLIANCE_LIMIT_SYMMETRY',
        'type': 'ViInt32'
    },
    1150185: {
        'codegen_method': 'public',
        'name': 'VOLTAGE_LIMIT_HIGH',
        'type': 'ViReal64'
    },
    1150186: {
        'codegen_method': 'public',
        'name': 'VOLTAGE_LIMIT_LOW',
        'type': 'ViReal64'
    },
    1150187: {
        'codegen_method': 'public',
        'name': 'CURRENT_LIMIT_HIGH',
        'type': 'ViReal64'
    },
    1150188: {
        'codegen_method': 'public',
        'name': 'CURRENT_LIMIT_LOW',
        'type': 'ViReal64'
    },
    1150189: {
        'codegen_method': 'public',
        'name': 'PULSE_VOLTAGE_LIMIT_HIGH',
        'type': 'ViReal64'
    },
    1150190: {
        'codegen_method': 'public',
        'name': 'PULSE_VOLTAGE_LIMIT_LOW',
        'type': 'ViReal64'
    },
    1150191: {
        'codegen_method': 'public',
        'name': 'PULSE_BIAS_VOLTAGE_LIMIT_HIGH',
        'type': 'ViReal64'
    },
    1150192: {
        'codegen_method': 'public',
        'name': 'PULSE_BIAS_VOLTAGE_LIMIT_LOW',
        'type': 'ViReal64'
    },
    1150193: {
        'codegen_method': 'public',
        'name': 'PULSE_CURRENT_LIMIT_HIGH',
        'type': 'ViReal64'
    },
    1150194: {
        'codegen_method': 'public',
        'name': 'PULSE_CURRENT_LIMIT_LOW',
        'type': 'ViReal64'
    },
    1150195: {
        'codegen_method': 'public',
        'name': 'PULSE_BIAS_CURRENT_LIMIT_HIGH',
        'type': 'ViReal64'
    },
    1150196: {
        'codegen_method': 'public',
        'name': 'PULSE_BIAS_CURRENT_LIMIT_LOW',
        'type': 'ViReal64'
    },
    1150198: {
        'codegen_method': 'public',
        'name': 'SEQUENCE_STEP_DELTA_TIME',
        'type': 'ViReal64'
    },
    1150199: {
        'codegen_method': 'public',
        'name': 'SEQUENCE_STEP_DELTA_TIME_ENABLED',
        'type': 'ViBoolean'
    },
    1150200: {
        'codegen_method': 'public',
        'name': 'OCP_ERROR_PERCENTAGE',
        'type': 'ViReal64'
    },
    1150205: {
        'codegen_method': 'public',
        'name': 'ACTUAL_POWER_ALLOCATION',
        'type': 'ViReal64'
    },
    1150206: {
        'codegen_method': 'public',
        'name': 'REQUESTED_POWER_ALLOCATION',
        'type': 'ViReal64'
    },
    1150207: {
        'codegen_method': 'public',
        'enum': 'PowerAllocationMode',
        'name': 'POWER_ALLOCATION_MODE',
        'type': 'ViInt32'
    },
    1150208: {
        'codegen_method': 'public',
        'enum': 'InstrumentMode',
        'name': 'INSTRUMENT_MODE',
        'type': 'ViInt32'
    },
    1150209: {
        'codegen_method': 'public',
        'enum': 'LCRStimulusFunction',
        'name': 'LCR_STIMULUS_FUNCTION',
        'type': 'ViInt32'
    },
    1150210: {
        'codegen_method': 'public',
        'name': 'LCR_FREQUENCY',
        'type': 'ViReal64'
    },
    1150211: {
        'codegen_method': 'public',
        'name': 'LCR_VOLTAGE_AMPLITUDE',
        'type': 'ViReal64'
    },
    1150212: {
        'codegen_method': 'public',
        'name': 'LCR_CURRENT_AMPLITUDE',
        'type': 'ViReal64'
    },
    1150213: {
        'codegen_method': 'public',
        'enum': 'LCRDCBiasSource',
        'name': 'LCR_DC_BIAS_SOURCE',
        'type': 'ViInt32'
    },
    1150214: {
        'codegen_method': 'public',
        'name': 'LCR_DC_BIAS_VOLTAGE_LEVEL',
        'type': 'ViReal64'
    },
    1150215: {
        'codegen_method': 'public',
        'name': 'LCR_DC_BIAS_CURRENT_LEVEL',
        'type': 'ViReal64'
    },
    1150216: {
        'codegen_method': 'public',
        'enum': 'LCRImpedanceAutoRange',
        'name': 'LCR_IMPEDANCE_AUTO_RANGE',
        'type': 'ViInt32'
    },
    1150217: {
        'codegen_method': 'public',
        'name': 'LCR_IMPEDANCE_RANGE',
        'type': 'ViReal64'
    },
    1150218: {
        'codegen_method': 'public',
        'enum': 'LCRMeasurementTime',
        'name': 'LCR_MEASUREMENT_TIME',
        'type': 'ViInt32'
    },
    1150220: {
        'codegen_method': 'public',
        'name': 'LCR_OPEN_COMPENSATION_ENABLED',
        'type': 'ViBoolean'
    },
    1150221: {
        'codegen_method': 'public',
        'name': 'LCR_SHORT_COMPENSATION_ENABLED',
        'type': 'ViBoolean'
    },
    1150222: {
        'codegen_method': 'public',
        'name': 'LCR_LOAD_COMPENSATION_ENABLED',
        'type': 'ViBoolean'
    },
    1150223: {
        'codegen_method': 'public',
        'enum': 'LCROpenShortLoadCompensationDataSource',
        'name': 'LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE',
        'type': 'ViInt32'
    },
    1150235: {
        'codegen_method': 'public',
        'name': 'OUTPUT_CUTOFF_ENABLED',
        'type': 'ViBoolean'
    },
    1150236: {
        'codegen_method': 'public',
        'name': 'OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH',
        'type': 'ViReal64'
    },
    1150237: {
        'codegen_method': 'public',
        'name': 'OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH',
        'type': 'ViReal64'
    },
    1150238: {
        'codegen_method': 'public',
        'name': 'OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW',
        'type': 'ViReal64'
    },
    1150239: {
        'codegen_method': 'public',
        'name': 'OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW',
        'type': 'ViReal64'
    },
    1150240: {
        'codegen_method': 'public',
        'name': 'OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED',
        'type': 'ViBoolean'
    },
    1150244: {
        'codegen_method': 'public',
        'enum': 'Autorange',
        'name': 'AUTORANGE',
        'type': 'ViInt32'
    },
    1150245: {
        'codegen_method': 'public',
        'enum': 'AutorangeBehavior',
        'name': 'AUTORANGE_BEHAVIOR',
        'type': 'ViInt32'
    },
    1150246: {
        'codegen_method': 'public',
        'enum': 'AutorangeApertureTimeMode',
        'name': 'AUTORANGE_APERTURE_TIME_MODE',
        'type': 'ViInt32'
    },
    1150247: {
        'codegen_method': 'public',
        'name': 'AUTORANGE_MINIMUM_APERTURE_TIME',
        'type': 'ViReal64'
    },
    1150248: {
        'codegen_method': 'public',
        'enum': 'ApertureTimeUnits',
        'name': 'AUTORANGE_MINIMUM_APERTURE_TIME_UNITS',
        'type': 'ViInt32'
    },
    1150249: {
        'codegen_method': 'public',
        'name': 'MERGED_CHANNELS',
        'type': 'ViString'
    },
    1150255: {
        'codegen_method': 'public',
        'name': 'AUTORANGE_MINIMUM_CURRENT_RANGE',
        'type': 'ViReal64'
    },
    1150256: {
        'codegen_method': 'public',
        'name': 'AUTORANGE_MINIMUM_VOLTAGE_RANGE',
        'type': 'ViReal64'
    },
    1150257: {
        'codegen_method': 'public',
        'enum': 'AutorangeThresholdMode',
        'name': 'AUTORANGE_THRESHOLD_MODE',
        'type': 'ViInt32'
    },
    1150258: {
        'codegen_method': 'public',
        'name': 'LCR_CUSTOM_MEASUREMENT_TIME',
        'type': 'ViReal64'
    },
    1150259: {
        'codegen_method': 'public',
        'name': 'ACTUAL_VOLTAGE_RANGE_FOR_LAST_FETCH',
        'type': 'ViReal64'
    },
    1150260: {
        'codegen_method': 'public',
        'name': 'ACTUAL_CURRENT_RANGE_FOR_LAST_FETCH',
        'type': 'ViReal64'
    },
    1150261: {
        'codegen_method': 'public',
        'name': 'LCR_OPEN_CONDUCTANCE',
        'type': 'ViReal64'
    },
    1150262: {
        'codegen_method': 'public',
        'name': 'LCR_OPEN_SUSCEPTANCE',
        'type': 'ViReal64'
    },
    1150263: {
        'codegen_method': 'public',
        'name': 'LCR_SHORT_RESISTANCE',
        'type': 'ViReal64'
    },
    1150264: {
        'codegen_method': 'public',
        'name': 'LCR_SHORT_REACTANCE',
        'type': 'ViReal64'
    },
    1150265: {
        'codegen_method': 'public',
        'name': 'LCR_VOLTAGE_RANGE',
        'type': 'ViReal64'
    },
    1150266: {
        'codegen_method': 'public',
        'name': 'LCR_DC_BIAS_VOLTAGE_RANGE',
        'type': 'ViReal64'
    },
    1150267: {
        'codegen_method': 'public',
        'name': 'LCR_CURRENT_RANGE',
        'type': 'ViReal64'
    },
    1150268: {
        'codegen_method': 'public',
        'name': 'LCR_MEASURED_LOAD_RESISTANCE',
        'type': 'ViReal64'
    },
    1150269: {
        'codegen_method': 'public',
        'name': 'LCR_MEASURED_LOAD_REACTANCE',
        'type': 'ViReal64'
    },
    1150270: {
        'codegen_method': 'public',
        'name': 'LCR_ACTUAL_LOAD_RESISTANCE',
        'type': 'ViReal64'
    },
    1150271: {
        'codegen_method': 'public',
        'name': 'LCR_ACTUAL_LOAD_REACTANCE',
        'type': 'ViReal64'
    },
    1150274: {
        'codegen_method': 'public',
        'name': 'LCR_DC_BIAS_CURRENT_RANGE',
        'type': 'ViReal64'
    },
    1150275: {
        'codegen_method': 'public',
        'enum': 'TriggerType',
        'name': 'SHUTDOWN_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150276: {
        'codegen_method': 'public',
        'enum': 'DigitalEdge',
        'name': 'DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE',
        'type': 'ViInt32'
    },
    1150277: {
        'codegen_method': 'public',
        'name': 'DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL',
        'type': 'ViString'
    },
    1150278: {
        'codegen_method': 'public',
        'enum': 'CableLength',
        'name': 'CABLE_LENGTH',
        'type': 'ViInt32'
    },
    1150290: {
        'codegen_method': 'public',
        'enum': 'LCRAutomaticLevelControl',
        'name': 'LCR_AUTOMATIC_LEVEL_CONTROL',
        'type': 'ViInt32'
    },
    1150291: {
        'codegen_method': 'public',
        'enum': 'LCRAutomaticLevelControl',
        'name': 'LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL',
        'type': 'ViInt32'
    },
    1150292: {
        'codegen_method': 'public',
        'name': 'OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW',
        'type': 'ViReal64'
    },
    1150293: {
        'codegen_method': 'public',
        'name': 'OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW',
        'type': 'ViReal64'
    },
    1150294: {
        'codegen_method': 'public',
        'name': 'OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH',
        'type': 'ViReal64'
    },
    1150295: {
        'codegen_method': 'public',
        'name': 'OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH',
        'type': 'ViReal64'
    },
    1150299: {
        'codegen_method': 'public',
        'name': 'LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED',
        'type': 'ViBoolean'
    },
    1150300: {
        'codegen_method': 'public',
        'name': 'OUTPUT_CUTOFF_DELAY',
        'type': 'ViReal64'
    },
    1150302: {
        'codegen_method': 'public',
        'enum': 'IsolationState',
        'name': 'ISOLATION_STATE',
        'type': 'ViInt32'
    },
    1150314: {
        'codegen_method': 'public',
        'enum': 'ApertureTimeAutoMode',
        'name': 'APERTURE_TIME_AUTO_MODE',
        'type': 'ViInt32'
    },
    1150315: {
        'codegen_method': 'public',
        'enum': 'LCRSourceDelayMode',
        'name': 'LCR_SOURCE_DELAY_MODE',
        'type': 'ViInt32'
    },
    1150318: {
        'codegen_method': 'public',
        'name': 'LCR_LOAD_RESISTANCE',
        'type': 'ViReal64'
    },
    1150319: {
        'codegen_method': 'public',
        'name': 'LCR_LOAD_INDUCTANCE',
        'type': 'ViReal64'
    },
    1150320: {
        'codegen_method': 'public',
        'name': 'LCR_LOAD_CAPACITANCE',
        'type': 'ViReal64'
    },
    1150321: {
        'codegen_method': 'public',
        'enum': 'LCRImpedanceRangeSource',
        'name': 'LCR_IMPEDANCE_RANGE_SOURCE',
        'type': 'ViInt32'
    },
    1150322: {
        'codegen_method': 'public',
        'name': 'AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE',
        'type': 'ViReal64'
    },
    1250001: {
        'codegen_method': 'public',
        'name': 'VOLTAGE_LEVEL',
        'type': 'ViReal64'
    },
    1250002: {
        'codegen_method': 'public',
        'name': 'OVP_ENABLED',
        'type': 'ViBoolean'
    },
    1250003: {
        'codegen_method': 'public',
        'name': 'OVP_LIMIT',
        'type': 'ViReal64'
    },
    1250004: {
        'codegen_method': 'public',
        'name': 'CURRENT_LIMIT_BEHAVIOR',
        'type': 'ViInt32'
    },
    1250005: {
        'codegen_method': 'public',
        'name': 'CURRENT_LIMIT',
        'type': 'ViReal64'
    },
    1250006: {
        'codegen_method': 'public',
        'name': 'OUTPUT_ENABLED',
        'type': 'ViBoolean'
    }
}
