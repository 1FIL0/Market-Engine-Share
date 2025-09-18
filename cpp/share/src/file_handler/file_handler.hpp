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