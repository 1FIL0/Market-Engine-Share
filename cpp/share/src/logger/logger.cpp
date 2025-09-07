#include "logger.hpp"
#include <iostream>

USE_NAMESPACE_SHARE

void LOGGER::sendMessage(const std::string msg)
{
    std::cout << "(Market Engine): " << msg << std::endl;
}

void LOGGER::sendStatusMessage(const std::string msg)
{
    std::cout << "(Market Engine): " << msg << " >>> " << std::flush;
}

void LOGGER::sendResultMessage(const bool success, const std::string rebound)
{
    std::string msg = (success) ? "[OK] " + rebound : "[FAILURE] " + rebound;
    std::cout << msg << std::endl;
}
