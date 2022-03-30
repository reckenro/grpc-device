#include <gmock/gmock.h>
#include <gtest/gtest.h>
#include <iotrace/iotrace_client.h>

#include <algorithm>
#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>

#include "device_server.h"
#include "enumerate_devices.h"
#include "niRFSAErrors.h"
#include "nirfsa/nirfsa_client.h"
#include "niscope/niscope_client.h"
#include "nitclk/nitclk_client.h"

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
  // Pre-requisite for test, start the IO Trace application

  std::string path = "C:\\Users\\reckenro\\Documents\\text-output.txt";
  auto start_tracing_response = client::start_tracing(stub(), 1, path, 1);

  EXPECT_EQ(0, start_tracing_response.status());
}

TEST_F(IOTraceApiTests, IOTraceIsStarted_StartTracingWithInvalidArgs_InvalidArgsResponse)
{
  // Pre-requisite for test, start the IO Trace application

  std::string path = "";  // Empty string not allowed for file path.
  auto start_tracing_response = client::start_tracing(stub(), 1, path, 1);

  EXPECT_EQ(-303204, start_tracing_response.status());
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
