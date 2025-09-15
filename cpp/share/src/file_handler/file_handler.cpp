#include "file_handler.hpp"
#include <filesystem>
#include <ios>
#include <sstream>
#include <fstream>
#include <string>
#include <rapidjson/document.h>
#include <rapidjson/prettywriter.h>
#include <rapidjson/stringbuffer.h>
#include "logger.hpp"
#include <boost/interprocess/sync/file_lock.hpp>
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

void FILES::writeFile(const std::string &path, const std::string &data, std::ios_base::openmode mode)
{
    std::ofstream outFile;
    outFile.open(path, mode);
    outFile << data;
    outFile.flush();
    outFile.close();
}

void FILES::writeFileAtomic(const std::string &path, const std::string &pathTmp, const std::string &data)
{

    std::string lockPath = path + ".lock";
    boost::interprocess::file_lock lock(lockPath.c_str());
    lock.lock();

    writeFile(pathTmp, data, std::ios::binary);

    #ifdef _WIN32
        if (!MoveFileExA(pathTmp.c_str(), path.c_str(), MOVEFILE_REPLACE_EXISTING)) {
            DWORD err = GetLastError();
            throw std::runtime_error("Failed to replace file atomically (Windows error " + std::to_string(err) + ")");
        }
    #elif __linux__
        moveFile(pathTmp, path);
    #endif

    lock.unlock();
}

void FILES::moveFile(const std::string &path, const std::string &newPath)
{
    std::filesystem::rename(path.c_str(), newPath.c_str());
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