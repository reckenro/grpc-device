# -*- coding: utf-8 -*-
# This file is generated from NI-IO Trace API metadata version 18.2
config = {
    "api_version": "18.2",
    "c_header": "NiSpyAPI.h",
    "c_function_prefix": "nispy_",
    "service_class_prefix": "NiIOTrace",
    "java_package": "com.ni.grpc.iotrace",
    "csharp_namespace": "NationalInstruments.Grpc.IOTrace",
    "namespace_component": "niiotrace",
    "close_function": "Close",
    "custom_types": [],
    "type_to_grpc_type": {
        "char[]": "string",
        "int32_t": "int32",
        "int": "int32",
    },
    "driver_name": "NI-IOTRACE",
    "init_function": "InitWithOptions",
    "status_ok": "status >= 0",
    "library_info": {
        "Linux": {"64bit": {"name": "libNiSpyLog", "type": "cdll"}},
        "Windows": {
            "32bit": {"name": "NiSpyLog.dll", "type": "windll"},
            "64bit": {"name": "NiSpyLog.dll", "type": "cdll"},
        },
    },
    "metadata_version": "2.0",
    "module_name": "niiotrace",
}
