import os
import file_handler
import definitions
import logger

def validateFiles():
    logger.sendMessage("Validating Files")
    if not os.path.exists(definitions.PATH_CONFIG_CLIENT): file_handler.makeDir(definitions.PATH_CONFIG_CLIENT)
    if not os.path.exists(definitions.PATH_DATA_CLIENT): file_handler.makeDir(definitions.PATH_DATA_CLIENT)
    if not os.path.exists(definitions.PATH_CONFIG_CLIENT_SONAR): file_handler.writeFile(definitions.PATH_CONFIG_CLIENT_SONAR, "{}")
    if not os.path.exists(definitions.PATH_CONFIG_CLIENT_TRADEUP_ENGINE): file_handler.writeFile(definitions.PATH_CONFIG_CLIENT_TRADEUP_ENGINE, "{}")
    if not os.path.exists(definitions.PATH_CONFIG_CLIENT_ITEM_LIBRARY): file_handler.writeFile(definitions.PATH_CONFIG_CLIENT_ITEM_LIBRARY, "{}")
    if not os.path.exists(definitions.PATH_CONFIG_CLIENT_UI): file_handler.writeFile(definitions.PATH_CONFIG_CLIENT_UI, "{}")
    if not os.path.exists(definitions.PATH_DATA_CLIENT_READY_ITEMS): file_handler.writeFile(definitions.PATH_DATA_CLIENT_READY_ITEMS, "{\"DATA\":[]}")
    if not os.path.exists(definitions.PATH_DATA_CLIENT_PROFITABLE_TRADEUPS): file_handler.writeFile(definitions.PATH_DATA_CLIENT_PROFITABLE_TRADEUPS, "{\"DATA\":[]}")
    if not os.path.exists(definitions.PATH_DATA_CLIENT_MODIFIED_ITEMS): file_handler.writeFile(definitions.PATH_DATA_CLIENT_MODIFIED_ITEMS, "{\"DATA\":[]}")
    if not os.path.exists(definitions.PATH_DATA_CLIENT_MODIFIED_ITEMS): file_handler.writeFile(definitions.PATH_DATA_CLIENT_MODIFIED_ITEMS, "{\"DATA\":[]}")

    if not os.path.exists(definitions.PATH_CONFIG_API): file_handler.makeDir(definitions.PATH_CONFIG_API)
    if not os.path.exists(definitions.PATH_DATA_API): file_handler.makeDir(definitions.PATH_DATA_API)
    if not os.path.exists(definitions.PATH_DATA_API_BYMYKEL_CSGO_API_ITEMS): file_handler.writeFile(definitions.PATH_DATA_API_BYMYKEL_CSGO_API_ITEMS, "{}")
    if not os.path.exists(definitions.PATH_DATA_API_STEAM_WEB_API_ITEMS): file_handler.writeFile(definitions.PATH_DATA_API_STEAM_WEB_API_ITEMS, "{}")
    if not os.path.exists(definitions.PATH_DATA_API_SCRAPED_PAGES): file_handler.writeFile(definitions.PATH_DATA_API_SCRAPED_PAGES, "{}")
    if not os.path.exists(definitions.PATH_DATA_API_SCRAPED_ITEMS): file_handler.writeFile(definitions.PATH_DATA_API_SCRAPED_ITEMS, "{}")
    logger.sendMessage("Validated files")