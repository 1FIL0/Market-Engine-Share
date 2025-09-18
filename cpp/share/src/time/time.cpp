/*
* Market Engine Share
* Copyright (C) 2025 OneFil (1FIL0) https://github.com/1FIL0
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with this program.  If not, see <http://www.gnu.org/licenses/>.
* See LICENCE file.
*/

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