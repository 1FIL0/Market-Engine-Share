#pragma once

#include "namespace.hpp"
#include <rapidjson/document.h>
#include <string>

START_SHARE_NAMESPACE_MULTI(FILES)
    
std::string readFile(const std::string &path);
void writeFile(const std::string &path, const std::string &data, std::ios_base::openmode mode = std::ios_base::out);
void writeFileAtomic(const std::string &path, const std::string &pathTmp, const std::string &data);
void moveFile(const std::string &path, const std::string &newPath);
void clearFile(const std::string &path);
void parseDocSanitizeDataArray(const std::string &path, rapidjson::Document &doc);

END_SHARE_NAMESPACE