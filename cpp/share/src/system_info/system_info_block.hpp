#pragma once

#include "namespace.hpp"
#include <cstdint>
#include <stdlib.h>

START_SHARE_NAMESPACE_MULTI(SYSTEM)

struct SystemInfoBlock {
    uint64_t totalRamBytes;
    uint64_t freeRamBytes;

    SystemInfoBlock();
};

END_SHARE_NAMESPACE