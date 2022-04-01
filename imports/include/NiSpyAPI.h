/* NiSpyAPI.h                                                                */
/*                                                                           */
/* This file is the main include file for using the NI Spy Programmatic API. */
/*                                                                           */
/* Contained within this header are the functions to be called by a client   */
/* application as well as enumerations detailing parameters and error return */
/* values.                                                                   */

#if !defined(_NI_SPY_API_H_)
#define _NI_SPY_API_H_

#include <stddef.h>

#if defined(WIN32) || defined(_WIN32) || defined(_WIN64)
   #define NISPY_API_APITYPE   __stdcall
   #if defined(NISPY_EXPORT_CWRAPPER)
      #define NISPY_API_CWRAPPER __declspec(dllexport)
   #else
      #define NISPY_API_CWRAPPER __declspec(dllimport)
   #endif
   #define NISPY_API_CWRAPPER_END
#else
   #define NISPY_API_APITYPE
   #define NISPY_API_CWRAPPER
   #if defined(__MACH__)
      #define NISPY_API_CWRAPPER_END __attribute__((weak_import))
   #else
      #define NISPY_API_CWRAPPER_END
   #endif
#endif

/* This enum corresponds to the logFileSetting specified in nispy_StartSpying */
enum eNiSpyLogFileSetting
{
   klogFileSettingNoFile = -1,
   kLogFileSettingSpy,
   kLogFileSettingPlainText,
   kLogFileSettingCommaSeparated,
   kLogFileSettingXml
};

#if !defined(__cplusplus) && !defined(__cplusplus__)
typedef enum eNiSpyLogFileSetting eNiSpyLogFileSetting;
#endif

/* This enum represents the error codes returned by the Spy API calls */
enum eNiSpyAPICommandStatus
{
   kCommandSuccess                     = 0,
   kCommandFailedNoExecute             = -303200,
   kCommandFailedIncompatibleState     = -303201,
   kCommandFailedUnableToOpenLogFile   = -303202,
   kCommandFailedSpyGUIClosed          = -303203,
   kCommandFailedInvalidSettings       = -303204,
   kCommandFailedBadParameter          = -303205,
   kCommandFailedInternalFailure       = -303206,
   kCommandFailedInvalidFileExtension  = -303207,
   kCommandFailedBufferTooSmall        = -303208,
   kCommandFailedFileAlreadyExists     = -303209
};

#if !defined(__cplusplus) && !defined(__cplusplus__)
typedef enum eNiSpyAPICommandStatus eNiSpyAPICommandStatus;
#endif

/* This enum represents the valid write modes for the nispy_StartSpying call */
enum eNiSpyAPIFileWriteMode
{
   kCreateOnly = 0,
   kCreateOrAppend,
   kCreateOrOverwrite
};

#if !defined(__cplusplus) && !defined(__cplusplus__)
typedef enum eNiSpyAPIFileWriteMode eNiSpyAPIFileWriteMode;
#endif

/* Functions supported by the NI Spy Programmatic API begin here */
#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/* nispy_GetApplicationPath returns the path to the application for launch.
   It is the user's responsibility to actually launch the application. */
NISPY_API_CWRAPPER eNiSpyAPICommandStatus NISPY_API_APITYPE
   nispy_GetApplicationPath(char * pathString, size_t pathStringSize)
NISPY_API_CWRAPPER_END;

/* nispy_StartSpying initiates spying on calls.  This command will only succeed
   if NI Spy has been launched.  logFileSetting specifies how the log should be
   stored to file and filePathString is a path to the desired log file.
   For overwriteFile, zero is false (append) and any nonzero value is true. */
NISPY_API_CWRAPPER eNiSpyAPICommandStatus NISPY_API_APITYPE
   nispy_StartSpying(eNiSpyLogFileSetting logFileSetting, const char * filePathString, eNiSpyAPIFileWriteMode fileWriteMode )
NISPY_API_CWRAPPER_END;

/* nispy_StopSpying halts spying on calls. */
NISPY_API_CWRAPPER eNiSpyAPICommandStatus NISPY_API_APITYPE
   nispy_StopSpying(void)
NISPY_API_CWRAPPER_END;

/* nispy_WriteTextEntry places a debug message into the current Spy log.
   This message also gets exported to the log file if logging to a file. */
NISPY_API_CWRAPPER eNiSpyAPICommandStatus NISPY_API_APITYPE
   nispy_WriteTextEntry(const char * message)
NISPY_API_CWRAPPER_END;

/* nispy_CloseSpy closes the NI Spy application.  This implies that logging is halted
   and the program will need to be relaunched if more calls need to be logged. */
NISPY_API_CWRAPPER eNiSpyAPICommandStatus NISPY_API_APITYPE
   nispy_CloseSpy(void)
NISPY_API_CWRAPPER_END;

#if defined(__cplusplus) || defined(__cplusplus__)
}  /* extern "C" closing brace */
#endif

#endif
