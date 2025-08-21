#include "time.hpp"
#include <chrono>
#include <iomanip>

USE_NAMESPACE_SHARE

std::string TIME::getCurrentDateTime(void) {
    auto now = std::chrono::system_clock::now();
    std::time_t now_time_t = std::chrono::system_clock::to_time_t(now);
    std::tm localTM = *std::localtime(&now_time_t);
    std::ostringstream oss;
    oss << std::put_time(&localTM, "%Y-%m-%d %H:%M:%S");  // Format: "YYYY-MM-DD HH:MM:SS"
    
    return oss.str();
}