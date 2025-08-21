#pragma once

#include "namespace.hpp"
#include <string>

START_SHARE_NAMESPACE_MULTI(LOGGER)

void sendMessage(const std::string msg);
void sendStatusMessage(const std::string msg);
void sendResultMessage(const bool success, const std::string rebound = "");

END_SHARE_NAMESPACE
