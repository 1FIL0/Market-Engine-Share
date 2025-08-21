#include "randomiser.hpp"
#include "namespace.hpp"
#include <random>
#include <chrono>

USE_NAMESPACE_SHARE

std::mt19937 rng;

void RAND::init()
{
    std::random_device rd;
    unsigned seed = rd() + static_cast<unsigned>(std::chrono::steady_clock::now().time_since_epoch().count());
    rng = std::mt19937(seed);
}

int RAND::getRandomInt(const int min, const int max)
{
    std::uniform_int_distribution<int> uid(min, max);
    return uid(rng);
}

float RAND::getRandomFloat(const float min, const float max)
{
    std::uniform_real_distribution<float> uid(min, max);
    return uid(rng);
}