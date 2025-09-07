#include "hasher.hpp"
#include <string>
#include <openssl/sha.h>
#include <iostream>
#include <sstream>
#include <iomanip>

USE_NAMESPACE_SHARE

std::string HASHER::sha256(const std::string &input)
{
    unsigned char digest[SHA256_DIGEST_LENGTH];
    SHA256((const unsigned char *)input.data(), input.size(), digest);

    std::ostringstream out;
    for (unsigned char byte : digest)
        out << std::hex << std::setw(2) << std::setfill('0') << (int)byte;
    return out.str();
}
