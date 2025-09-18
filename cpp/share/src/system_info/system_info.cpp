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

#include "system_info.hpp"
#include "namespace.hpp"
#include "system_info_block.hpp"
#ifdef _WIN32
#include <windows.h>
#elif __linux__
#include <sys/sysinfo.h>
#endif

USE_NAMESPACE_SHARE

SYSTEM::SystemInfoBlock SYSTEM::getSystemInfo(void)
{
    SYSTEM::SystemInfoBlock systemInfoBlock;

#ifdef _WIN32
    MEMORYSTATUSEX status;
    status.dwLength = sizeof(status);
    GlobalMemoryStatusEx(&status);
    systemInfoBlock.totalRamBytes = status.ullTotalPhys;
    systemInfoBlock.freeRamBytes = status.ullAvailPhys;

#else
    struct sysinfo info;
    sysinfo(&info);
    systemInfoBlock.totalRamBytes = info.totalram * info.mem_unit;
    systemInfoBlock.freeRamBytes = info.freeram * info.mem_unit;

#endif

    return systemInfoBlock;
}