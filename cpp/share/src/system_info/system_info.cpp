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