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