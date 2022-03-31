#include <gmock/gmock.h>
#include <gtest/gtest.h>
#include <iotrace/iotrace_client.h>

#include <algorithm>
#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>

#include "device_server.h"
#include "enumerate_devices.h"

using namespace iotrace_grpc;
namespace client = iotrace_grpc::experimental::client;
namespace pb = google::protobuf;
using namespace ::testing;
using nlohmann::json;
using namespace std::string_literals;  // for trailing ""s string literal syntax;

namespace ni {
namespace tests {
namespace system {
namespace {

class IOTraceApiTests : public ::testing::Test {
 protected:
  IOTraceApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        stub_(IOTrace::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }
  virtual ~IOTraceApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  template <typename TService>
  std::unique_ptr<typename TService::Stub> create_stub()
  {
    return TService::NewStub(device_server_->InProcessChannel());
  }

  std::unique_ptr<IOTrace::Stub>& stub()
  {
    return stub_;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<IOTrace::Stub> stub_;
};

TEST_F(IOTraceApiTests, IOTraceIsStarted_StartTracing_Success)
{
  // Pre-requisite for test, IO Trace application is running

  std::string path = "C:\\Users\\reckenro\\Documents\\text-output.txt";
  auto start_tracing_response = client::start_tracing(stub(), LOG_FILE_SETTING_PlainText, path, FILE_WRITE_MODE_CreateOrAppend);

  EXPECT_EQ(0, start_tracing_response.status());
}

TEST_F(IOTraceApiTests, IOTraceIsStarted_StartTracingWithInvalidArgs_InvalidArgsResponse)
{
  // Pre-requisite for test, IO Trace application is running

  std::string path = "";  // Empty string not allowed for file path.
  auto start_tracing_response = client::start_tracing(stub(), LOG_FILE_SETTING_PlainText, path, FILE_WRITE_MODE_CreateOrAppend);

  EXPECT_EQ(COMMAND_STATUS_InvalidSettings, start_tracing_response.status());
}

TEST_F(IOTraceApiTests, IOTraceIsStarted_StopTracing_Success)
{
  // Pre-requisite for test, IO Trace application is running

  auto stop_tracing_response = client::stop_tracing(stub());

  EXPECT_EQ(0, stop_tracing_response.status());
}

TEST_F(IOTraceApiTests, IOTraceIsStarted_CloseIOTrace_Success)
{
  // Pre-requisite for test, IO Trace application is running

  auto close_trace_response = client::close_io_trace(stub());

  EXPECT_EQ(0, close_trace_response.status());
}

TEST_F(IOTraceApiTests, IOTraceIsInstalled_GetIOTracePath_SuccessAndGetsAppPath)
{
  // Pre-requisite for test, IO Trace application is running

  auto io_trace_path_response = client::get_io_trace_path(stub());

  EXPECT_EQ(0, io_trace_path_response.status());
  EXPECT_STRNE("", io_trace_path_response.path_string().c_str());
}

TEST_F(IOTraceApiTests, IOTraceIsStarted_LogMessage_Success)
{
  // Pre-requisite for test, IO Trace application is running

  std::string message = "Hello World!";
  auto log_message_response = client::log_message(stub(), message);

  EXPECT_EQ(0, log_message_response.status());
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
