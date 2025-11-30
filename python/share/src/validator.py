#* Market Engine Share
#* Copyright (C) 2025 OneFil (1FIL0) https://github.com/1FIL0
#*
#* This program is free software: you can redistribute it and/or modify
#* it under the terms of the GNU General Public License as published by
#* the Free Software Foundation, either version 3 of the License, or
#* (at your option) any later version.
#*
#* This program is distributed in the hope that it will be useful,
#* but WITHOUT ANY WARRANTY; without even the implied warranty of
#* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#* GNU General Public License for more details.
#*
#* You should have received a copy of the GNU General Public License
#* along with this program.  If not, see <http://www.gnu.org/licenses/>.
#* See LICENCE file.

import os
import file_handler
import definitions
import logger

def validateFiles():
    logger.sendMessage("Validating Files")
    if not os.path.exists(definitions.PATH_CONFIG_CLIENT): file_handler.makeDir(definitions.PATH_CONFIG_CLIENT)
    if not os.path.exists(definitions.PATH_DATA_CLIENT): file_handler.makeDir(definitions.PATH_DATA_CLIENT)
    if not os.path.exists(definitions.PATH_DATA_CLIENT_CACHE_DIR): file_handler.makeDir(definitions.PATH_DATA_CLIENT_CACHE_DIR)
    if not os.path.exists(definitions.PATH_CONFIG_CLIENT_SONAR): file_handler.writeFile(definitions.PATH_CONFIG_CLIENT_SONAR, "{}")
    if not os.path.exists(definitions.PATH_CONFIG_CLIENT_TRADEUP_ENGINE): file_handler.writeFile(definitions.PATH_CONFIG_CLIENT_TRADEUP_ENGINE, "{}")
    if not os.path.exists(definitions.PATH_CONFIG_CLIENT_ITEM_LIBRARY): file_handler.writeFile(definitions.PATH_CONFIG_CLIENT_ITEM_LIBRARY, "{}")
    if not os.path.exists(definitions.PATH_CONFIG_CLIENT_UI): file_handler.writeFile(definitions.PATH_CONFIG_CLIENT_UI, "{}")
    if not os.path.exists(definitions.PATH_DATA_CLIENT_MASTER_ITEMS): file_handler.writeFile(definitions.PATH_DATA_CLIENT_MASTER_ITEMS, "{\"DATA\":[]}")
    if not os.path.exists(definitions.PATH_DATA_CLIENT_MARKET_ITEMS): file_handler.writeFile(definitions.PATH_DATA_CLIENT_MARKET_ITEMS, "{\"DATA\":[]}")
    if not os.path.exists(definitions.PATH_DATA_CLIENT_PROFITABLE_TRADEUPS): file_handler.writeFile(definitions.PATH_DATA_CLIENT_PROFITABLE_TRADEUPS, "{\"DATA\":[]}")
    if not os.path.exists(definitions.PATH_DATA_CLIENT_MODIFIED_ITEMS): file_handler.writeFile(definitions.PATH_DATA_CLIENT_MODIFIED_ITEMS, "{\"DATA\":[]}")
    if not os.path.exists(definitions.PATH_DATA_CLIENT_MODIFIED_ITEMS): file_handler.writeFile(definitions.PATH_DATA_CLIENT_MODIFIED_ITEMS, "{\"DATA\":[]}")

    if not os.path.exists(definitions.PATH_CONFIG_API): file_handler.makeDir(definitions.PATH_CONFIG_API)
    if not os.path.exists(definitions.PATH_DATA_API): file_handler.makeDir(definitions.PATH_DATA_API)
    if not os.path.exists(definitions.PATH_DATA_API_BYMYKEL_CSGO_API_ITEMS): file_handler.writeFile(definitions.PATH_DATA_API_BYMYKEL_CSGO_API_ITEMS, "{}")
    if not os.path.exists(definitions.PATH_DATA_API_STEAM_WEB_API_ITEMS): file_handler.writeFile(definitions.PATH_DATA_API_STEAM_WEB_API_ITEMS, "{}")
    if not os.path.exists(definitions.PATH_DATA_API_MARKET_ITEMS): file_handler.writeFile(definitions.PATH_DATA_API_MARKET_ITEMS, "{}")
    if not os.path.exists(definitions.PATH_DATA_API_MASTER_ITEMS): file_handler.writeFile(definitions.PATH_DATA_API_MASTER_ITEMS, "{}")
    if not os.path.exists(definitions.PATH_DATA_API_SCRAPED_PAGES): file_handler.writeFile(definitions.PATH_DATA_API_SCRAPED_PAGES, "{}")
    if not os.path.exists(definitions.PATH_DATA_API_SCRAPED_ITEMS): file_handler.writeFile(definitions.PATH_DATA_API_SCRAPED_ITEMS, "{}")
    logger.sendMessage("Validated files")