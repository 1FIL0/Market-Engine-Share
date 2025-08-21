#pragma once

#include "namespace.hpp"

START_SHARE_NAMESPACE_MULTI(RAND)

void init();
int getRandomInt(const int min, const int max);
float getRandomFloat(const float min, const float max);

END_SHARE_NAMESPACE