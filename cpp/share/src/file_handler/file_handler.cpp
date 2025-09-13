#include "file_handler.hpp"
#include <filesystem>
#include <sstream>
#include <fstream>
#include <string>
#include <rapidjson/document.h>
#include <rapidjson/prettywriter.h>
#include <rapidjson/stringbuffer.h>
#include "logger.hpp"
#ifdef _WIN32
#include <windows.h>
#elif __linux__
#include <cstdio>
#endif

USE_NAMESPACE_SHARE

std::string FILES::readFile(const std::string &path)
{
    std::ifstream file(path);
    std::stringstream buffer;
    buffer << file.rdbuf();
    file.close();
    return buffer.str();
}

void FILES::writeFile(const std::string &path, const std::string &data)
{
    std::ofstream outFile;
    outFile.open(path);
    outFile << data;
    outFile.close();
}

void FILES::writeFileAtomic(const std::string &path, const std::string &data)
{
    std::string tmpPath = path + ".tmp";

    std::ofstream tmpFile(tmpPath, std::ios::binary);
    if (!tmpFile) {
        LOGGER::sendMessage("Error, cannot open temp file");
        throw std::runtime_error("Failed to open temp file");
    }
    tmpFile << data;
    tmpFile.flush();
    tmpFile.close();

    #ifdef _WIN32
        if (!MoveFileExA(tmpPath.c_str(), path.c_str(), MOVEFILE_REPLACE_EXISTING)) {
            DWORD err = GetLastError();
            throw std::runtime_error("Failed to replace file atomically (Windows error " + std::to_string(err) + ")");
        }
    #elif __linux__
        if (std::rename(tmpPath.c_str(), path.c_str()) != 0) {
            throw std::runtime_error("Failed to rename temporary file to target");
        }
    #endif
}

void FILES::moveFile(const std::string &path, const std::string &newPath)
{
    std::filesystem::rename(path.c_str(), newPath.c_str());
}

void FILES::appendFile(const std::string &path, const std::string &data)
{
    std::ofstream outFile;
    outFile.open(path, std::ios::app);
    outFile << data;
    outFile.close();
}

void FILES::clearFile(const std::string &path)
{
    std::ofstream outFile;
    outFile.open(path);
    outFile << "";
    outFile.close(); 
}

void FILES::parseDocSanitizeDataArray(const std::string &path, rapidjson::Document &doc)
{
    doc.Parse(FILES::readFile(path).c_str());
    
    rapidjson::Document::AllocatorType &allocator = doc.GetAllocator();
    if (!doc.HasMember("DATA")) {
        doc.RemoveAllMembers();
        doc.SetObject();
        doc.AddMember("DATA", rapidjson::Value(rapidjson::kArrayType), allocator);
    }
}