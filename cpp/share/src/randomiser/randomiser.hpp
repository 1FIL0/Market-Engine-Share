#pragma once

#include "namespace.hpp"

START_SHARE_NAMESPACE_MULTI(RAND)

void init();
int getRandomInt(int min, int max);
float getRandomFloat(float min, float max);

END_SHARE_NAMESPACE