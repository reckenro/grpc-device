#include <iotrace/iotrace_service.h>
#include <shellapi.h>

#include <fstream>
#include <iostream>
using namespace std::string_literals;

namespace iotrace_grpc {
//---------------------------------------------------------------------
//---------------------------------------------------------------------
// TODO: This is hacky. Make this proper (support Linux, validate correct way to launch IO Trace, etc.)
::grpc::Status IOTraceService::OpenIOTrace(::grpc::ServerContext* context, const OpenIOTraceRequest* request, OpenIOTraceResponse* response)
{
  if (context->IsCancelled()) {
    return ::grpc::Status::CANCELLED;
  }
  try {
    auto path_string_size = 256;
    std::string path_string(path_string_size - 1, '\0');
    auto status = library_->GetIOTracePath((char*)path_string.data(), path_string_size);
    response->set_status(status);
    if (status >= 0) {
      ShellExecute(NULL, "open", path_string.c_str(), NULL, NULL, SW_SHOWDEFAULT);
    }

    return ::grpc::Status::OK;
  }
  catch (nidevice_grpc::LibraryLoadException& ex) {
    return ::grpc::Status(::grpc::NOT_FOUND, ex.what());
  }
}

}  // namespace iotrace_grpc
