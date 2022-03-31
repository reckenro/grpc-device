# -*- coding: utf-8 -*-
# This file is generated from IO Trace API metadata version 18.2
config = {
    "api_version": "18.2",
    "c_header": "NiSpyAPI.h",
    "c_function_prefix": "nispy_",
    "service_class_prefix": "IOTrace",
    "java_package": "com.ni.grpc.iotrace",
    "csharp_namespace": "NationalInstruments.Grpc.IOTrace",
    "namespace_component": "iotrace",
    "close_function": "Doesn't matter, there isn't one",
    "resource_handle_type": "int32_t",  # Note: This api shouldn't have "sessions", this is just to appease the build temporarily.
    "custom_types": [],
    "type_to_grpc_type": {
        "char[]": "string",
        "int32_t": "int32",
        "int": "int32",
        "eNiSpyLogFileSetting": "LogFileSetting",
        "eNiSpyAPIFileWriteMode": "FileWriteMode",
        "eNiSpyAPICommandStatus": "CommandStatus",
    },
    "driver_name": "IO-TRACE",
    "status_ok": "status >= 0",
    "library_info": {
        "Linux": {"64bit": {"name": "libNiSpyLog", "type": "cdll"}},
        "Windows": {
            "32bit": {"name": "NiSpyLog.dll", "type": "windll"},
            "64bit": {"name": "NiSpyLog.dll", "type": "cdll"},
        },
    },
    "metadata_version": "2.0",
    "module_name": "iotrace",
}
