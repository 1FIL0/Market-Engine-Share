#include "file_handler.hpp"
#include <filesystem>
#include <sstream>
#include <fstream>
#include <string>
#include <rapidjson/document.h>
#include <rapidjson/prettywriter.h>
#include <rapidjson/stringbuffer.h>

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