#include "randomiser.hpp"
#include "namespace.hpp"
#include <random>
#include <chrono>
#include <utility>
#include "logger.hpp"

USE_NAMESPACE_SHARE

std::mt19937 rng;

void RAND::init()
{
    std::random_device rd;
    unsigned seed = rd() + static_cast<unsigned>(std::chrono::steady_clock::now().time_since_epoch().count());
    rng = std::mt19937(seed);
}

int RAND::getRandomInt(int min, int max)
{
    if (min > max) {
        LOGGER::sendMessage("Randomiser warning: min is bigger than max");
        std::swap(min, max);
    }
    std::uniform_int_distribution<int> uid(min, max);
    return uid(rng);
}

float RAND::getRandomFloat(float min, float max)
{
    if (min > max) {
        LOGGER::sendMessage("Randomiser warning: min is bigger than max");
        std::swap(min, max);
    }
    std::uniform_real_distribution<float> uid(min, max);
    return uid(rng);
}