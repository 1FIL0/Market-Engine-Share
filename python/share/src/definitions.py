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

import types
import os
import platform
import sys
import shared_args
from pathlib import Path

SYSTEM = platform.system()
SYSTEM_WINDOWS = "Windows"
SYSTEM_LINUX = "Linux"

# _____ URLS _____ #

URL_MARKET_ENGINE = "https://marketengine.onefil.dev"
URL_MARKET_ENGINE_DOWNLOADS = URL_MARKET_ENGINE + "/downloads"
URL_MARKET_ENGINE_DOCS = URL_MARKET_ENGINE + "/docs"
URL_MARKET_ENGINE_UPDATE_ITEMS = URL_MARKET_ENGINE + "/api/update_items"
URL_MARKET_ENGINE_FETCH_ITEMS = URL_MARKET_ENGINE + "/api/fetch_items"
URL_MARKET_ENGINE_FETCH_SERVER_STATUS = URL_MARKET_ENGINE + "/api/fetch_status"
URL_CSFLOAT_API_GET_LISTINGS = "https://csfloat.com/api/v1/listings"
URL_SKINPORT_GET_ITEMS = "https://api.skinport.com/v1/sales/history"
URL_MARKET_ENGINE_REPO = "https://github.com/1FIL0/Market-Engine-Client"
URL_1FIL0_YOUTUBE = "https://www.youtube.com/@1FIL0-f7f"
URL_1FIL0_DISCORD = "https://discord.gg/tM53kbYVa6"
URL_1FIL0_GITHUB = "https://github.com/1FIL0"

# _____ CONFIGS / DATA _____ #

PATH_DATA_CLIENT: Path = Path()
PATH_DATA_API: Path = Path()
PATH_CONFIG_CLIENT: Path = Path()
PATH_CONFIG_API: Path = Path()

if SYSTEM == "Windows":
    APPDATA = Path(os.environ['APPDATA'])
    LOCALAPPDATA = Path(os.environ.get('LOCALAPPDATA', os.environ['APPDATA']))
    PATH_CONFIG_CLIENT = APPDATA / 'market_engine_client'
    PATH_CONFIG_API = APPDATA / 'market_engine_api'
    PATH_DATA_CLIENT = LOCALAPPDATA / 'market_engine_client'
    PATH_DATA_API = LOCALAPPDATA / 'market_engine_api'

elif SYSTEM == "Linux":
    HOME = Path(os.environ['HOME'])
    PATH_CONFIG_CLIENT = HOME / '.config' / 'market_engine_client'
    PATH_CONFIG_API = HOME / '.config' / 'market_engine_api'
    PATH_DATA_CLIENT = HOME / '.local' / 'share' / 'market_engine_client'
    PATH_DATA_API = HOME / '.local' / 'share' / 'market_engine_api'

# _____ CLIENT CONFIGS _____ #
PATH_CONFIG_CLIENT_SONAR = PATH_CONFIG_CLIENT / "sonar.json"
PATH_CONFIG_CLIENT_TRADEUP_ENGINE = PATH_CONFIG_CLIENT / "tradeup_engine.json"
PATH_CONFIG_CLIENT_ITEM_LIBRARY = PATH_CONFIG_CLIENT / "item_library.json"
PATH_CONFIG_CLIENT_UI = PATH_CONFIG_CLIENT / "ui.json"
PATH_CONFIG_CLIENT_SERVER = PATH_CONFIG_CLIENT / "server.json"

# _____ API CONFIGS _____ #
PATH_CONFIG_API_SONAR = PATH_CONFIG_API / "sonar.json"

# _____ CLIENT DATA _____ #
PATH_DATA_CLIENT_READY_ITEMS = PATH_DATA_CLIENT / "ready_items.json"
PATH_DATA_CLIENT_PROFITABLE_TRADEUPS = PATH_DATA_CLIENT / "profitable_tradeups.json"
PATH_DATA_CLIENT_MODIFIED_ITEMS = PATH_DATA_CLIENT / "modified_items.json"
PATH_DATA_CLIENT_CACHE_DIR = PATH_DATA_CLIENT / "cache"

# _____ API DATA _____ #
PATH_DATA_API_BYMYKEL_CSGO_API_ITEMS = PATH_DATA_API / "bymykel_csgo_api_items.json"
PATH_DATA_API_STEAM_WEB_API_ITEMS = PATH_DATA_API / "steam_web_api_items.json"
PATH_DATA_API_CSFLOAT_ITEMS = PATH_DATA_API / "csfloat_items.json"
PATH_DATA_API_SKINPORT_ITEMS = PATH_DATA_API / "skinport_items.json"
PATH_DATA_API_READY_ITEMS = PATH_DATA_API / "ready_items.json"
PATH_DATA_API_SCRAPED_ITEMS = PATH_DATA_API / "scraped_items.json"
PATH_DATA_API_SCRAPED_PAGES = PATH_DATA_API / "scraped_pages.json"

# _____ DIST / BINARIES _____ #

PATH_SHARE_HERE = Path(__file__).resolve().parent
PATH_MEIPASS = Path(getattr(sys, "_MEIPASS", Path(".").resolve()))
PATH_BINARY_DIR = Path(sys.executable).parent

# Find bin directory from executable. WARNING - Must check in this specific order in case some proper mong tries to exploit into creating a fake bin/ directory.
PATH_DIST_BIN = Path()
for candidate in [PATH_BINARY_DIR, PATH_BINARY_DIR / "bin", PATH_BINARY_DIR.parent]:
    if candidate.is_dir() and candidate.name == "bin":
        PATH_DIST_BIN = candidate
        break

# Same thing but for bundled .dll/.so.
PATH_LIB = Path()
for candidate in [PATH_BINARY_DIR / "usr" / "lib", PATH_BINARY_DIR.parent / "usr" / "lib", PATH_BINARY_DIR.parent.parent / "usr" / "lib"]:
    if candidate.is_dir():
        PATH_LIB = candidate
        break

PATH_DIST_ASSETS: Path = Path()
PATH_DIST_CLIENT_APP_BINARY: Path = Path()
PATH_DIST_CLIENT_SONAR_BINARY: Path = Path()
PATH_DIST_CLIENT_TRADEUP_ENGINE_BINARY: Path = Path()
PATH_DIST_API_APP_BINARY: Path = Path()
PATH_DIST_API_SONAR_BINARY: Path = Path()
PATH_DIST_DRIVERS: Path = Path()
PATH_DIST_DRIVER_GECKODRIVER_PATH: Path = Path()
PATH_MARKET_ENGINE_SOURCE: Path = Path()

# _____ DEV / RELEASE _____ #
if shared_args.argDist == "dev":
    PATH_MARKET_ENGINE_SOURCE = PATH_SHARE_HERE.parents[3]
    PATH_MARKET_ENGINE_ASSETS = PATH_MARKET_ENGINE_SOURCE / "market_engine_assets"
    PATH_MARKET_ENGINE_ASSETS_SKINS = PATH_MARKET_ENGINE_ASSETS / "skins"
    PATH_MARKET_ENGINE_FONTS = PATH_MARKET_ENGINE_ASSETS / "fonts"
    PATH_MARKET_ENGINE_CLIENT = PATH_MARKET_ENGINE_SOURCE / "market_engine_client"
    PATH_MARKET_ENGINE_API = PATH_MARKET_ENGINE_SOURCE / "market_engine_api"
    PATH_MARKET_ENGINE_DRIVERS = PATH_MARKET_ENGINE_SOURCE / "drivers"
    PATH_CLIENT_APPLICATION = PATH_MARKET_ENGINE_CLIENT / "python" / "application"
    PATH_CLIENT_SONAR = PATH_MARKET_ENGINE_CLIENT / "python" / "sonar"
    PATH_CLIENT_TRADEUP_ENGINE = PATH_MARKET_ENGINE_CLIENT / "cpp" / "tradeup_engine"
    PATH_API_APPLICATION = PATH_MARKET_ENGINE_API / "python" / "application"
    PATH_API_SONAR = PATH_MARKET_ENGINE_API / "python" / "sonar"

    PATH_DIST_CLIENT_APP_BINARY = PATH_CLIENT_APPLICATION / "src" / "main.py"
    PATH_DIST_CLIENT_SONAR_BINARY = PATH_CLIENT_SONAR / "src" / "main.py"
    PATH_DIST_API_APP_BINARY = PATH_API_APPLICATION / "src" / "main.py"
    PATH_DIST_API_SONAR_BINARY = PATH_API_SONAR / "src" / "main.py"

    PATH_DIST_ASSETS = PATH_MARKET_ENGINE_ASSETS
    PATH_DIST_DRIVERS = PATH_MARKET_ENGINE_DRIVERS

    if SYSTEM == "Linux":
        PATH_DIST_CLIENT_TRADEUP_ENGINE_BINARY = PATH_CLIENT_TRADEUP_ENGINE / "build" / "build_linux64" / "engine"
    elif SYSTEM == "Windows":
        PATH_DIST_CLIENT_TRADEUP_ENGINE_BINARY = PATH_CLIENT_TRADEUP_ENGINE / "build" / "build_win64" / "engine"

elif shared_args.argDist == "release":
    if SYSTEM == "Linux":
        PATH_DIST_CLIENT_APP_BINARY = PATH_DIST_BIN / "application" / "application"
        PATH_DIST_CLIENT_SONAR_BINARY = PATH_DIST_BIN / "sonar" / "sonar"
        PATH_DIST_CLIENT_TRADEUP_ENGINE_BINARY = PATH_DIST_BIN / "engine"
        PATH_DIST_API_SONAR_BINARY = PATH_DIST_BIN / "sonar" / "sonar"
    elif SYSTEM == "Windows":
        PATH_DIST_CLIENT_APP_BINARY = PATH_DIST_BIN / "application" / "application.exe"
        PATH_DIST_CLIENT_SONAR_BINARY = PATH_DIST_BIN / "sonar" / "sonar.exe"
        PATH_DIST_CLIENT_TRADEUP_ENGINE_BINARY = PATH_DIST_BIN / "engine.exe"
        PATH_DIST_API_SONAR_BINARY = PATH_DIST_BIN / "sonar" / "sonar.exe"

    PATH_DIST_ASSETS = PATH_MEIPASS / "market_engine_assets"
    PATH_DIST_DRIVERS = PATH_MEIPASS / "drivers"

# NOT IN USE ANYMORE BUT MIGHT BE IN THE FUTURE
if SYSTEM == "Windows":
    PATH_DIST_DRIVER_GECKODRIVER_PATH = PATH_DIST_DRIVERS / "geckodriver_win32.exe"
elif SYSTEM == "Linux":
    PATH_DIST_DRIVER_GECKODRIVER_PATH = PATH_DIST_DRIVERS / "geckodriver_linux64"

# _____ FUCK WINDOWS ______ #

PYTHON_CMD_CLIENT = Path()
PYTHON_CMD_API = Path()

if SYSTEM == "Windows":
    PYTHON_CMD_CLIENT = PATH_MARKET_ENGINE_SOURCE / "venvs" / "windows_x86_64" / "client_venv" / "Scripts" / "python.exe" 
    PYTHON_CMD_API = PATH_MARKET_ENGINE_SOURCE / "venvs" / "windows_x86_64" / "api_venv" / "Scripts" / "python.exe" 

elif SYSTEM == "Linux":
    PYTHON_CMD_CLIENT = PATH_MARKET_ENGINE_SOURCE / "venvs" / "linux_x86_64" / "client_venv" / "bin" / "python3" 
    PYTHON_CMD_API = PATH_MARKET_ENGINE_SOURCE / "venvs" / "linux_x86_64" / "api_venv" / "bin" / "python3" 

consts = types.SimpleNamespace()

# _____ GRADES ______ #

consts.GRADE_CONSUMER = 0; consts.GRADE_CONSUMER_STR = "Consumer"
consts.GRADE_INDUSTRIAL = 1; consts.GRADE_INDUSTRIAL_STR = "Industrial"
consts.GRADE_MILSPEC = 2; consts.GRADE_MILSPEC_STR = "Milspec"
consts.GRADE_RESTRICTED = 3; consts.GRADE_RESTRICTED_STR = "Restricted"
consts.GRADE_CLASSIFIED = 4; consts.GRADE_CLASSIFIED_STR = "Classified"
consts.GRADE_COVERT = 5; consts.GRADE_COVERT_STR = "Covert"
consts.GRADE_STAR = 6; consts.GRADE_STAR_STR = "Star"
consts.GRADE_CONTRABAND = 7; consts.GRADE_CONTRABAND_STR = "Contraband"
consts.GRADE_MAX = 8
consts.GRADE_CONSUMER_RGB_STR = "204, 204, 204"
consts.GRADE_INDUSTRIAL_RGB_STR = "75, 105, 255"
consts.GRADE_MILSPEC_RGB_STR = "0, 100, 255"
consts.GRADE_RESTRICTED_RGB_STR = "136, 71, 255"
consts.GRADE_CLASSIFIED_RGB_STR = "211, 44, 230"
consts.GRADE_COVERT_RGB_STR = "235, 75, 75"
consts.GRADE_STAR_RGB_STR = "212, 175, 55"
consts.GRADE_CONTRABAND_RGB_STR = "228, 174, 57"

# _____ CATEGORIES ______ #

consts.CATEGORY_NORMAL = 0; consts.CATEGORY_NORMAL_STR = "Normal"
consts.CATEGORY_STAT_TRAK = 1; consts.CATEGORY_STAT_TRAK_STR = "StatTrak"
consts.CATEGORY_SOUVENIR = 2; consts.CATEGORY_SOUVENIR_STR = "Souvenir"
consts.CATEGORY_MAX = 3

# _____ WEARS ______ #

consts.WEAR_FACTORY_NEW = 0; consts.WEAR_FACTORY_NEW_STR = "Factory New"
consts.WEAR_MINIMAL_WEAR = 1; consts.WEAR_MINIMAL_WEAR_STR = "Minimal Wear"
consts.WEAR_FIELD_TESTED = 2; consts.WEAR_FIELD_TESTED_STR = "Field Tested"
consts.WEAR_WELL_WORN = 3; consts.WEAR_WELL_WORN_STR = "Well Worn"
consts.WEAR_BATTLE_SCARRED = 4; consts.WEAR_BATTLE_SCARRED_STR = "Battle Scarred"
consts.WEAR_NO_WEAR = 5; consts.WEAR_NO_WEAR_STR = "No Wear"
consts.WEAR_MAX = 6

# _____ PAGE ______ #

consts.PAGE_PRICE_ASCEND = 0; consts.PAGE_PRICE_ASCEND_STR = "Price Ascend"
consts.PAGE_PRICE_DESCEND = 1; consts.PAGE_PRICE_DESCEND_STR = "Price Descend"

# _____ COLLECTIONS ______ #

consts.COLLECTION_OVERPASS_2024 = 0
consts.COLLECTION_GALLERY = 1
consts.COLLECTION_GRAPHIC_DESIGN = 2
consts.COLLECTION_LIMITED_EDITION_ITEM = 3
consts.COLLECTION_SPORT_AND_FIELD = 4
consts.COLLECTION_KILOWATT = 5
consts.COLLECTION_ANUBIS = 6
consts.COLLECTION_REVOLUTION = 7
consts.COLLECTION_RECOIL = 8
consts.COLLECTION_DREAMS_AND_NIGHTMARES = 9
consts.COLLECTION_TRAIN_2021 = 10
consts.COLLECTION_DUST2_2021 = 11
consts.COLLECTION_MIRAGE_2021 = 12
consts.COLLECTION_VERTIGO_2021 = 13
consts.COLLECTION_RIPTIDE = 14
consts.COLLECTION_SNAKEBITE = 15
consts.COLLECTION_BROKEN_FANG = 16
consts.COLLECTION_CONTROL = 17
consts.COLLECTION_ANCIENT = 18
consts.COLLECTION_HAVOC = 19
consts.COLLECTION_FRACTURE = 20
consts.COLLECTION_PRISMA2 = 21
consts.COLLECTION_CANALS = 22
consts.COLLECTION_ST_MARC = 23
consts.COLLECTION_NORSE = 24
consts.COLLECTION_SHATTERED_WEB = 25
consts.COLLECTION_CS20 = 26
consts.COLLECTION_XRAY = 27
consts.COLLECTION_PRISMA = 28
consts.COLLECTION_CLUTCH = 29
consts.COLLECTION_BLACKSITE = 30
consts.COLLECTION_DANGER_ZONE = 31
consts.COLLECTION_NUKE_2018 = 32
consts.COLLECTION_INFERNO_2018 = 33
consts.COLLECTION_HORIZON = 34
consts.COLLECTION_SPECTRUM_2 = 35
consts.COLLECTION_HYDRA = 36
consts.COLLECTION_SPECTRUM = 37
consts.COLLECTION_GLOVE = 38
consts.COLLECTION_GAMMA2 = 39
consts.COLLECTION_GAMMA = 40
consts.COLLECTION_CHROMA3 = 41
consts.COLLECTION_WILDFIRE = 42
consts.COLLECTION_REVOLVER_CASE = 43
consts.COLLECTION_SHADOW = 44
consts.COLLECTION_RISING_SUN = 45
consts.COLLECTION_GODS_AND_MONSTERS = 46
consts.COLLECTION_CHOP_SHOP = 47
consts.COLLECTION_FALCHION = 48
consts.COLLECTION_CHROMA2 = 49
consts.COLLECTION_CHROMA = 50
consts.COLLECTION_VANGUARD = 51
consts.COLLECTION_CACHE = 52
consts.COLLECTION_ESPORTS_2014_SUMMER = 53
consts.COLLECTION_BREAKOUT = 54
consts.COLLECTION_BAGGAGE = 55
consts.COLLECTION_OVERPASS = 56
consts.COLLECTION_COBBLESTONE = 57
consts.COLLECTION_BANK = 58
consts.COLLECTION_HUNTSMAN = 59
consts.COLLECTION_PHEONIX = 60
consts.COLLECTION_ARMS_DEAL_3 = 61
consts.COLLECTION_ESPORTS_2013_WINTER = 62
consts.COLLECTION_WINTER_OFFENSIVE = 63
consts.COLLECTION_ITALY = 64
consts.COLLECTION_MIRAGE = 65
consts.COLLECTION_SAFEHOUSE = 66
consts.COLLECTION_DUST2 = 67
consts.COLLECTION_LAKE = 68
consts.COLLECTION_TRAIN = 69
consts.COLLECTION_ARMS_DEAL_2 = 70
consts.COLLECTION_ALPHA = 71
consts.COLLECTION_BRAVO = 72
consts.COLLECTION_ASSAULT = 73
consts.COLLECTION_DUST = 74
consts.COLLECTION_OFFICE = 75
consts.COLLECTION_NUKE = 76
consts.COLLECTION_AZTEC = 77
consts.COLLECTION_INFERNO = 78
consts.COLLECTION_ARMS_DEAL = 79
consts.COLLECTION_MILITIA = 80
consts.COLLECTION_VERTIGO = 81
consts.COLLECTION_ESPORTS_2013 = 82
consts.COLLECTION_TRAIN_2025 = 83
consts.COLLECTION_RADIANT = 84
consts.COLLECTION_BOREAL = 85
consts.COLLECTION_ASCENT = 86
consts.COLLECTION_FEVER = 87
consts.COLLECTION_GENESIS = 88
consts.COLLECTION_MAX = 89
consts.COLLECTION_UNKNOWN = -1

consts.COLLECTION_OVERPASS_2024_STR = "The Overpass 2024 Collection"
consts.COLLECTION_GALLERY_STR = "The Gallery Collection"
consts.COLLECTION_GRAPHIC_DESIGN_STR = "The Graphic Design Collection"
consts.COLLECTION_LIMITED_EDITION_ITEM_STR = "Limited Edition Item"
consts.COLLECTION_SPORT_AND_FIELD_STR = "The Sport & Field Collection"
consts.COLLECTION_KILOWATT_STR = "The Kilowatt Collection"
consts.COLLECTION_ANUBIS_STR = "The Anubis Collection"
consts.COLLECTION_REVOLUTION_STR = "The Revolution Collection"
consts.COLLECTION_RECOIL_STR = "The Recoil Collection"
consts.COLLECTION_DREAMS_AND_NIGHTMARES_STR = "The Dreams & Nightmares Collection"
consts.COLLECTION_TRAIN_2021_STR = "The 2021 Train Collection"
consts.COLLECTION_DUST2_2021_STR = "The 2021 Dust 2 Collection"
consts.COLLECTION_MIRAGE_2021_STR = "The 2021 Mirage Collection"
consts.COLLECTION_VERTIGO_2021_STR = "The 2021 Vertigo Collection"
consts.COLLECTION_RIPTIDE_STR = "The Operation Riptide Collection"
consts.COLLECTION_SNAKEBITE_STR = "The Snakebite Collection"
consts.COLLECTION_BROKEN_FANG_STR = "The Operation Broken Fang Collection"
consts.COLLECTION_CONTROL_STR = "The Control Collection"
consts.COLLECTION_ANCIENT_STR = "The Ancient Collection"
consts.COLLECTION_HAVOC_STR = "The Havoc Collection"
consts.COLLECTION_FRACTURE_STR = "The Fracture Collection"
consts.COLLECTION_PRISMA2_STR = "The Prisma 2 Collection"
consts.COLLECTION_CANALS_STR = "The Canals Collection"
consts.COLLECTION_ST_MARC_STR = "The St. Marc Collection"
consts.COLLECTION_NORSE_STR = "The Norse Collection"
consts.COLLECTION_SHATTERED_WEB_STR = "The Shattered Web Collection"
consts.COLLECTION_CS20_STR = "The CS20 Collection"
consts.COLLECTION_XRAY_STR = "The X-Ray Collection"
consts.COLLECTION_PRISMA_STR = "The Prisma Collection"
consts.COLLECTION_CLUTCH_STR = "The Clutch Collection"
consts.COLLECTION_BLACKSITE_STR = "The Blacksite Collection"
consts.COLLECTION_DANGER_ZONE_STR = "The Danger Zone Collection"
consts.COLLECTION_NUKE_2018_STR = "The 2018 Nuke Collection"
consts.COLLECTION_INFERNO_2018_STR = "The 2018 Inferno Collection"
consts.COLLECTION_HORIZON_STR = "The Horizon Collection"
consts.COLLECTION_SPECTRUM_2_STR = "The Spectrum 2 Collection"
consts.COLLECTION_HYDRA_STR = "The Operation Hydra Collection"
consts.COLLECTION_SPECTRUM_STR = "The Spectrum Collection"
consts.COLLECTION_GLOVE_STR = "The Glove Collection"
consts.COLLECTION_GAMMA2_STR = "The Gamma 2 Collection"
consts.COLLECTION_GAMMA_STR = "The Gamma Collection"
consts.COLLECTION_CHROMA3_STR = "The Chroma 3 Collection"
consts.COLLECTION_WILDFIRE_STR = "The Wildfire Collection"
consts.COLLECTION_REVOLVER_CASE_STR = "The Revolver Case Collection"
consts.COLLECTION_SHADOW_STR = "The Shadow Collection"
consts.COLLECTION_RISING_SUN_STR = "The Rising Sun Collection"
consts.COLLECTION_GODS_AND_MONSTERS_STR = "The Gods and Monsters Collection"
consts.COLLECTION_CHOP_SHOP_STR = "The Chop Shop Collection"
consts.COLLECTION_FALCHION_STR = "The Falchion Collection"
consts.COLLECTION_CHROMA2_STR = "The Chroma 2 Collection"
consts.COLLECTION_CHROMA_STR = "The Chroma Collection"
consts.COLLECTION_VANGUARD_STR = "The Vanguard Collection"
consts.COLLECTION_CACHE_STR = "The Cache Collection"
consts.COLLECTION_ESPORTS_2014_SUMMER_STR = "The eSports 2014 Summer Collection"
consts.COLLECTION_BREAKOUT_STR = "The Breakout Collection"
consts.COLLECTION_BAGGAGE_STR = "The Baggage Collection"
consts.COLLECTION_OVERPASS_STR = "The Overpass Collection"
consts.COLLECTION_COBBLESTONE_STR = "The Cobblestone Collection"
consts.COLLECTION_BANK_STR = "The Bank Collection"
consts.COLLECTION_HUNTSMAN_STR = "The Huntsman Collection"
consts.COLLECTION_PHEONIX_STR = "The Phoenix Collection"
consts.COLLECTION_ARMS_DEAL_3_STR = "The Arms Deal 3 Collection"
consts.COLLECTION_ESPORTS_2013_WINTER_STR = "The eSports 2013 Winter Collection"
consts.COLLECTION_WINTER_OFFENSIVE_STR = "The Winter Offensive Collection"
consts.COLLECTION_ITALY_STR = "The Italy Collection"
consts.COLLECTION_MIRAGE_STR = "The Mirage Collection"
consts.COLLECTION_SAFEHOUSE_STR = "The Safehouse Collection"
consts.COLLECTION_DUST2_STR = "The Dust 2 Collection"
consts.COLLECTION_LAKE_STR = "The Lake Collection"
consts.COLLECTION_TRAIN_STR = "The Train Collection"
consts.COLLECTION_ARMS_DEAL_2_STR = "The Arms Deal 2 Collection"
consts.COLLECTION_ALPHA_STR = "The Alpha Collection"
consts.COLLECTION_BRAVO_STR = "The Bravo Collection"
consts.COLLECTION_ASSAULT_STR = "The Assault Collection"
consts.COLLECTION_DUST_STR = "The Dust Collection"
consts.COLLECTION_OFFICE_STR = "The Office Collection"
consts.COLLECTION_NUKE_STR = "The Nuke Collection"
consts.COLLECTION_AZTEC_STR = "The Aztec Collection"
consts.COLLECTION_INFERNO_STR = "The Inferno Collection"
consts.COLLECTION_ARMS_DEAL_STR = "The Arms Deal Collection"
consts.COLLECTION_MILITIA_STR = "The Militia Collection"
consts.COLLECTION_VERTIGO_STR = "The Vertigo Collection"
consts.COLLECTION_ESPORTS_2013_STR = "The eSports 2013 Collection"
consts.COLLECTION_TRAIN_2O25_STR = "The Train 2025 Collection"
consts.COLLECTION_RADIANT_STR = "The Radiant Collection"
consts.COLLECTION_BOREAL_STR = "The Boreal Collection"
consts.COLLECTION_ASCENT_STR = "The Ascent Collection"
consts.COLLECTION_FEVER_STR = "The Fever Collection"
consts.COLLECTION_GENESIS_STR = "The Genesis Collection"

# _____ CRATES ______ #

consts.CRATE_GENESIS = 0
consts.CRATE_FEVER = 1
consts.CRATE_GALLERY = 2
consts.CRATE_KILOWATT = 3
consts.CRATE_ANUBIS = 4
consts.CRATE_REVOLUTION = 5
consts.CRATE_RECOIL = 6
consts.CRATE_DREAMS_AND_NIGHTMARES = 7
consts.CRATE_RIPTIDE = 8
consts.CRATE_SNAKEBITE = 9
consts.CRATE_BROKEN_FANG = 10
consts.CRATE_FRACTURE = 11
consts.CRATE_PRISMA2 = 12
consts.CRATE_CS20 = 13
consts.CRATE_XRAY = 14
consts.CRATE_SHATTERED_WEB = 15
consts.CRATE_PRISMA = 16
consts.CRATE_DANGER_ZONE = 17
consts.CRATE_HORIZON = 18
consts.CRATE_CLUTCH = 19
consts.CRATE_SPECTRUM2 = 20
consts.CRATE_HYDRA = 21
consts.CRATE_SPECTRUM = 22
consts.CRATE_GLOVE = 23
consts.CRATE_GAMMA2 = 24
consts.CRATE_GAMMA = 25
consts.CRATE_CHROMA3 = 26
consts.CRATE_WILDFIRE = 27
consts.CRATE_REVOLVER = 28
consts.CRATE_SHADOW = 29
consts.CRATE_FALCHION = 30
consts.CRATE_CHROMA2 = 31
consts.CRATE_CHROMA = 32
consts.CRATE_VANGUARD = 33
consts.CRATE_ESPORTS_2014_SUMMER = 34
consts.CRATE_BREAKOUT = 35
consts.CRATE_HUNTSMAN = 36
consts.CRATE_PHEONIX = 37
consts.CRATE_WEAPON_CASE_3 = 38
consts.CRATE_WINTER_OFFENSIVE = 39
consts.CRATE_ESPORTS_2013_WINTER = 40
consts.CRATE_WEAPON_CASE_2 = 41
consts.CRATE_BRAVO = 42
consts.CRATE_ESPORTS_2013 = 43
consts.CRATE_WEAPON_CASE = 44
consts.CRATE_END = 45
consts.CRATE_UNKNOWN = -1

consts.CRATE_GENESIS_STR = "Sealed Genesis Terminal"
consts.CRATE_FEVER_STR = "Fever Case"
consts.CRATE_GALLERY_STR = "Gallery Case"
consts.CRATE_KILOWATT_STR = "Kilowatt Case"
consts.CRATE_ANUBIS_STR = "Anubis Collection Package"
consts.CRATE_REVOLUTION_STR = "Revolution Case"
consts.CRATE_RECOIL_STR = "Recoil Case"
consts.CRATE_DREAMS_AND_NIGHTMARES_STR = "Dreams & Nightmares Case"
consts.CRATE_RIPTIDE_STR = "Operation Riptide Case"
consts.CRATE_SNAKEBITE_STR = "Snakebite Case"
consts.CRATE_BROKEN_FANG_STR = "Operation Broken Fang Case"
consts.CRATE_FRACTURE_STR = "Fracture Case"
consts.CRATE_PRISMA2_STR = "Prisma 2 Case"
consts.CRATE_CS20_STR = "CS20 Case"
consts.CRATE_XRAY_STR = "X-Ray P250 Package"
consts.CRATE_SHATTERED_WEB_STR = "Shattered Web Case"
consts.CRATE_PRISMA_STR = "Prisma Case"
consts.CRATE_DANGER_ZONE_STR = "Danger Zone Case"
consts.CRATE_HORIZON_STR = "Horizon Case"
consts.CRATE_CLUTCH_STR = "Clutch Case"
consts.CRATE_SPECTRUM2_STR = "Spectrum 2 Case"
consts.CRATE_HYDRA_STR = "Operation Hydra Case"
consts.CRATE_SPECTRUM_STR = "Spectrum Case"
consts.CRATE_GLOVE_STR = "Glove Case"
consts.CRATE_GAMMA2_STR = "Gamma 2 Case"
consts.CRATE_GAMMA_STR = "Gamma Case"
consts.CRATE_CHROMA3_STR = "Chroma 3 Case"
consts.CRATE_WILDFIRE_STR = "Operation Wildfire Case"
consts.CRATE_REVOLVER_STR = "Revolver Case"
consts.CRATE_SHADOW_STR = "Shadow Case"
consts.CRATE_FALCHION_STR = "Falchion Case"
consts.CRATE_CHROMA2_STR = "Chroma 2 Case"
consts.CRATE_CHROMA_STR = "Chroma Case"
consts.CRATE_VANGUARD_STR = "Operation Vanguard Weapon Case"
consts.CRATE_ESPORTS_2014_SUMMER_STR = "eSports 2014 Summer Case"
consts.CRATE_BREAKOUT_STR = "Operation Breakout Weapon Case"
consts.CRATE_HUNTSMAN_STR = "Huntsman Weapon Case"
consts.CRATE_PHEONIX_STR = "Operation Pheonix Weapon Case"
consts.CRATE_WEAPON_CASE_3_STR = "CS:GO Weapon Case 3"
consts.CRATE_WINTER_OFFENSIVE_STR = "Winter Offensive Weapon Case"
consts.CRATE_ESPORTS_2013_WINTER_STR = "eSports 2013 Winter Case"
consts.CRATE_WEAPON_CASE_2_STR = "CS:GO Weapon Case 2"
consts.CRATE_BRAVO_STR = "Operation Bravo Case"
consts.CRATE_ESPORTS_2013_STR = "eSports 2013 Case"
consts.CRATE_WEAPON_CASE_STR = "CS:GO Weapon Case"

# FLOATS

consts.FLOAT_MIN_FACTORY_NEW = 0.00
consts.FLOAT_MIN_MINIMAL_WEAR = 0.071
consts.FLOAT_MIN_FIELD_TESTED = 0.151
consts.FLOAT_MIN_WELL_WORN = 0.381
consts.FLOAT_MIN_BATTLE_SCARRED = 0.451

consts.FLOAT_MAX_FACTORY_NEW = 0.07
consts.FLOAT_MAX_MINIMAL_WEAR = 0.15
consts.FLOAT_MAX_FIELD_TESTED = 0.38
consts.FLOAT_MAX_WELL_WORN = 0.45
consts.FLOAT_MAX_BATTLE_SCARRED = 1.0

consts.FLOAT_AVG_FACTORY_NEW = 0.035
consts.FLOAT_AVG_MINIMAL_WEAR = 0.11
consts.FLOAT_AVG_FIELD_TESTED = 0.26
consts.FLOAT_AVG_WELL_WORN = 0.41
consts.FLOAT_AVG_BATTLE_SCARRED = 0.725

weapons = [
    "AK-47", "M4A4", "M4A1-S", "AWP", "SG 553", "FAMAS", "Galil AR", "M249", "Negev", 
    "CZ75-Auto", "Desert Eagle", "P250", "Five-SeveN", "Tec-9", "USP-S", "Glock-18", 
    "Dual Berettas", "MAC-10", "MP7", "MP9", "UMP-45", "PP-Bizon", "MAG-7", "Nova", 
    "Sawed-Off", "XM1014", "AUG", "Scout", "R8 Revolver", "P90", "G3SG1", "PP-Bizon",
    "P2000", "SSG 08", "MP5-SD", "SCAR-20",
    
    "Bayonet," "M9 Bayonet", "Bowie Knife", "Butterfly Knife", "Classic Knife",
    "Falchion Knife", "Flip Knife", "Gut Knife", "Huntsman Knife", "Karambit,"
    "Kukri Knife", "Navaja Knife", "Nomad Knife", "Paracord Knife", "Shadow Daggers",
    "Skeleton Knife", "Stiletto Knife", "Survival Knife", "Talon Knife", "Ursus Knife",

    "Zeus x27"
]

def gradeToString(grade: int) -> str:
    match grade:
        case consts.GRADE_CONSUMER:  return consts.GRADE_CONSUMER_STR
        case consts.GRADE_INDUSTRIAL: return consts.GRADE_INDUSTRIAL_STR 
        case consts.GRADE_MILSPEC: return consts.GRADE_MILSPEC_STR
        case consts.GRADE_RESTRICTED: return consts.GRADE_RESTRICTED_STR
        case consts.GRADE_CLASSIFIED: return consts.GRADE_CLASSIFIED_STR
        case consts.GRADE_COVERT: return consts.GRADE_COVERT_STR
        case consts.GRADE_STAR: return consts.GRADE_STAR_STR
        case consts.GRADE_CONTRABAND: return consts.GRADE_CONTRABAND_STR
        case _: return "?"

def categoryToString(category: int) -> str:
    match category:
        case consts.CATEGORY_NORMAL: return consts.CATEGORY_NORMAL_STR
        case consts.CATEGORY_STAT_TRAK: return consts.CATEGORY_STAT_TRAK_STR
        case consts.CATEGORY_SOUVENIR: return consts.CATEGORY_SOUVENIR_STR
        case _: return "?"

def wearToString(wear: int) -> str:
    match wear:
        case consts.WEAR_FACTORY_NEW: return consts.WEAR_FACTORY_NEW_STR
        case consts.WEAR_MINIMAL_WEAR: return consts.WEAR_MINIMAL_WEAR_STR
        case consts.WEAR_FIELD_TESTED: return consts.WEAR_FIELD_TESTED_STR
        case consts.WEAR_WELL_WORN: return consts.WEAR_WELL_WORN_STR
        case consts.WEAR_BATTLE_SCARRED: return consts.WEAR_BATTLE_SCARRED_STR
        case consts.WEAR_NO_WEAR: return consts.WEAR_NO_WEAR_STR
        case _: return "?"

def pageSortToString(sort: int) -> str:
    res = "?"
    match(sort):
        case consts.PAGE_PRICE_ASCEND: return consts.PAGE_PRICE_ASCEND_STR
        case consts.PAGE_PRICE_DESCEND: return consts.PAGE_PRICE_DESCEND_STR
        case _: pass
    return res

def gradeToInt(grade: str) -> int:
    if grade == consts.GRADE_CONSUMER_STR: return consts.GRADE_CONSUMER
    if grade == consts.GRADE_INDUSTRIAL_STR: return consts.GRADE_INDUSTRIAL
    if grade == consts.GRADE_MILSPEC_STR: return consts.GRADE_MILSPEC
    if grade == consts.GRADE_RESTRICTED_STR: return consts.GRADE_RESTRICTED
    if grade == consts.GRADE_CLASSIFIED_STR: return consts.GRADE_CLASSIFIED
    if grade == consts.GRADE_COVERT_STR: return consts.GRADE_COVERT
    if grade == consts.GRADE_STAR_STR: return consts.GRADE_STAR
    if grade == consts.GRADE_CONTRABAND_STR: return consts.GRADE_CONTRABAND
    return -1

def categoryToInt(category: str) -> int:
    if category == consts.CATEGORY_NORMAL_STR: return consts.CATEGORY_NORMAL
    if category == consts.CATEGORY_STAT_TRAK_STR: return consts.CATEGORY_STAT_TRAK
    if category == consts.CATEGORY_SOUVENIR_STR: return consts.CATEGORY_SOUVENIR
    return -1

def wearToInt(wear: str) -> int:
    if wear == consts.WEAR_FACTORY_NEW_STR: return consts.WEAR_FACTORY_NEW
    if wear == consts.WEAR_MINIMAL_WEAR_STR: return consts.WEAR_MINIMAL_WEAR
    if wear == consts.WEAR_FIELD_TESTED_STR: return consts.WEAR_FIELD_TESTED
    if wear == consts.WEAR_WELL_WORN_STR: return consts.WEAR_WELL_WORN
    if wear == consts.WEAR_BATTLE_SCARRED_STR: return consts.WEAR_BATTLE_SCARRED
    if wear == consts.WEAR_NO_WEAR_STR: return consts.WEAR_NO_WEAR
    return -1

def collectionToString(collection: int) -> str:
    match collection:
        case consts.COLLECTION_OVERPASS_2024: return consts.COLLECTION_OVERPASS_2024_STR
        case consts.COLLECTION_GALLERY: return consts.COLLECTION_GALLERY_STR
        case consts.COLLECTION_GRAPHIC_DESIGN: return consts.COLLECTION_GRAPHIC_DESIGN_STR
        case consts.COLLECTION_LIMITED_EDITION_ITEM: return consts.COLLECTION_LIMITED_EDITION_ITEM_STR
        case consts.COLLECTION_SPORT_AND_FIELD: return consts.COLLECTION_SPORT_AND_FIELD_STR
        case consts.COLLECTION_KILOWATT: return consts.COLLECTION_KILOWATT_STR
        case consts.COLLECTION_ANUBIS: return consts.COLLECTION_ANUBIS_STR
        case consts.COLLECTION_REVOLUTION: return consts.COLLECTION_REVOLUTION_STR
        case consts.COLLECTION_RECOIL: return consts.COLLECTION_RECOIL_STR
        case consts.COLLECTION_DREAMS_AND_NIGHTMARES: return consts.COLLECTION_DREAMS_AND_NIGHTMARES_STR
        case consts.COLLECTION_TRAIN_2021: return consts.COLLECTION_TRAIN_2021_STR
        case consts.COLLECTION_DUST2_2021: return consts.COLLECTION_DUST2_2021_STR
        case consts.COLLECTION_MIRAGE_2021: return consts.COLLECTION_MIRAGE_2021_STR
        case consts.COLLECTION_VERTIGO_2021: return consts.COLLECTION_VERTIGO_2021_STR
        case consts.COLLECTION_RIPTIDE: return consts.COLLECTION_RIPTIDE_STR
        case consts.COLLECTION_SNAKEBITE: return consts.COLLECTION_SNAKEBITE_STR
        case consts.COLLECTION_BROKEN_FANG: return consts.COLLECTION_BROKEN_FANG_STR
        case consts.COLLECTION_CONTROL: return consts.COLLECTION_CONTROL_STR
        case consts.COLLECTION_ANCIENT: return consts.COLLECTION_ANCIENT_STR
        case consts.COLLECTION_HAVOC: return consts.COLLECTION_HAVOC_STR
        case consts.COLLECTION_FRACTURE: return consts.COLLECTION_FRACTURE_STR
        case consts.COLLECTION_PRISMA2: return consts.COLLECTION_PRISMA2_STR
        case consts.COLLECTION_CANALS: return consts.COLLECTION_CANALS_STR
        case consts.COLLECTION_ST_MARC: return consts.COLLECTION_ST_MARC_STR
        case consts.COLLECTION_NORSE: return consts.COLLECTION_NORSE_STR
        case consts.COLLECTION_SHATTERED_WEB: return consts.COLLECTION_SHATTERED_WEB_STR
        case consts.COLLECTION_CS20: return consts.COLLECTION_CS20_STR
        case consts.COLLECTION_XRAY: return consts.COLLECTION_XRAY_STR
        case consts.COLLECTION_PRISMA: return consts.COLLECTION_PRISMA_STR
        case consts.COLLECTION_CLUTCH: return consts.COLLECTION_CLUTCH_STR
        case consts.COLLECTION_BLACKSITE: return consts.COLLECTION_BLACKSITE_STR
        case consts.COLLECTION_DANGER_ZONE: return consts.COLLECTION_DANGER_ZONE_STR
        case consts.COLLECTION_NUKE_2018: return consts.COLLECTION_NUKE_2018_STR
        case consts.COLLECTION_INFERNO_2018: return consts.COLLECTION_INFERNO_2018_STR
        case consts.COLLECTION_HORIZON: return consts.COLLECTION_HORIZON_STR
        case consts.COLLECTION_SPECTRUM_2: return consts.COLLECTION_SPECTRUM_2_STR
        case consts.COLLECTION_HYDRA: return consts.COLLECTION_HYDRA_STR
        case consts.COLLECTION_SPECTRUM: return consts.COLLECTION_SPECTRUM_STR
        case consts.COLLECTION_GLOVE: return consts.COLLECTION_GLOVE_STR
        case consts.COLLECTION_GAMMA2: return consts.COLLECTION_GAMMA2_STR
        case consts.COLLECTION_GAMMA: return consts.COLLECTION_GAMMA_STR
        case consts.COLLECTION_CHROMA3: return consts.COLLECTION_CHROMA3_STR
        case consts.COLLECTION_WILDFIRE: return consts.COLLECTION_WILDFIRE_STR
        case consts.COLLECTION_REVOLVER_CASE: return consts.COLLECTION_REVOLVER_CASE_STR
        case consts.COLLECTION_SHADOW: return consts.COLLECTION_SHADOW_STR
        case consts.COLLECTION_RISING_SUN: return consts.COLLECTION_RISING_SUN_STR
        case consts.COLLECTION_GODS_AND_MONSTERS: return consts.COLLECTION_GODS_AND_MONSTERS_STR
        case consts.COLLECTION_CHOP_SHOP: return consts.COLLECTION_CHOP_SHOP_STR
        case consts.COLLECTION_FALCHION: return consts.COLLECTION_FALCHION_STR
        case consts.COLLECTION_CHROMA2: return consts.COLLECTION_CHROMA2_STR
        case consts.COLLECTION_CHROMA: return consts.COLLECTION_CHROMA_STR
        case consts.COLLECTION_VANGUARD: return consts.COLLECTION_VANGUARD_STR
        case consts.COLLECTION_CACHE: return consts.COLLECTION_CACHE_STR
        case consts.COLLECTION_ESPORTS_2014_SUMMER: return consts.COLLECTION_ESPORTS_2014_SUMMER_STR
        case consts.COLLECTION_BREAKOUT: return consts.COLLECTION_BREAKOUT_STR
        case consts.COLLECTION_BAGGAGE: return consts.COLLECTION_BAGGAGE_STR
        case consts.COLLECTION_OVERPASS: return consts.COLLECTION_OVERPASS_STR
        case consts.COLLECTION_COBBLESTONE: return consts.COLLECTION_COBBLESTONE_STR
        case consts.COLLECTION_BANK: return consts.COLLECTION_BANK_STR
        case consts.COLLECTION_HUNTSMAN: return consts.COLLECTION_HUNTSMAN_STR
        case consts.COLLECTION_PHEONIX: return consts.COLLECTION_PHEONIX_STR
        case consts.COLLECTION_ARMS_DEAL_3: return consts.COLLECTION_ARMS_DEAL_3_STR
        case consts.COLLECTION_ESPORTS_2013_WINTER: return consts.COLLECTION_ESPORTS_2013_WINTER_STR
        case consts.COLLECTION_WINTER_OFFENSIVE: return consts.COLLECTION_WINTER_OFFENSIVE_STR
        case consts.COLLECTION_ITALY: return consts.COLLECTION_ITALY_STR
        case consts.COLLECTION_MIRAGE: return consts.COLLECTION_MIRAGE_STR
        case consts.COLLECTION_SAFEHOUSE: return consts.COLLECTION_SAFEHOUSE_STR
        case consts.COLLECTION_DUST2: return consts.COLLECTION_DUST2_STR
        case consts.COLLECTION_LAKE: return consts.COLLECTION_LAKE_STR
        case consts.COLLECTION_TRAIN: return consts.COLLECTION_TRAIN_STR
        case consts.COLLECTION_ARMS_DEAL_2: return consts.COLLECTION_ARMS_DEAL_2_STR
        case consts.COLLECTION_ALPHA: return consts.COLLECTION_ALPHA_STR
        case consts.COLLECTION_BRAVO: return consts.COLLECTION_BRAVO_STR
        case consts.COLLECTION_ASSAULT: return consts.COLLECTION_ASSAULT_STR
        case consts.COLLECTION_DUST: return consts.COLLECTION_DUST_STR
        case consts.COLLECTION_OFFICE: return consts.COLLECTION_OFFICE_STR
        case consts.COLLECTION_NUKE: return consts.COLLECTION_NUKE_STR
        case consts.COLLECTION_AZTEC: return consts.COLLECTION_AZTEC_STR
        case consts.COLLECTION_INFERNO: return consts.COLLECTION_INFERNO_STR
        case consts.COLLECTION_ARMS_DEAL: return consts.COLLECTION_ARMS_DEAL_STR
        case consts.COLLECTION_MILITIA: return consts.COLLECTION_MILITIA_STR
        case consts.COLLECTION_VERTIGO: return consts.COLLECTION_VERTIGO_STR
        case consts.COLLECTION_ESPORTS_2013: return consts.COLLECTION_ESPORTS_2013_STR
        case consts.COLLECTION_TRAIN_2025: return consts.COLLECTION_TRAIN_2O25_STR
        case consts.COLLECTION_RADIANT: return consts.COLLECTION_RADIANT_STR
        case consts.COLLECTION_BOREAL: return consts.COLLECTION_BOREAL_STR
        case consts.COLLECTION_ASCENT: return consts.COLLECTION_ASCENT_STR
        case consts.COLLECTION_FEVER: return consts.COLLECTION_FEVER_STR
        case consts.COLLECTION_GENESIS: return consts.COLLECTION_GENESIS_STR
        case _: return "?"

def collectionToInt(collection: str) -> int:
    if collection == consts.COLLECTION_OVERPASS_2024_STR: return consts.COLLECTION_OVERPASS_2024
    if collection == consts.COLLECTION_GALLERY_STR: return consts.COLLECTION_GALLERY
    if collection == consts.COLLECTION_GRAPHIC_DESIGN_STR: return consts.COLLECTION_GRAPHIC_DESIGN
    if collection == consts.COLLECTION_LIMITED_EDITION_ITEM_STR: return consts.COLLECTION_LIMITED_EDITION_ITEM
    if collection == consts.COLLECTION_SPORT_AND_FIELD_STR: return consts.COLLECTION_SPORT_AND_FIELD
    if collection == consts.COLLECTION_KILOWATT_STR: return consts.COLLECTION_KILOWATT
    if collection == consts.COLLECTION_ANUBIS_STR: return consts.COLLECTION_ANUBIS
    if collection == consts.COLLECTION_REVOLUTION_STR: return consts.COLLECTION_REVOLUTION
    if collection == consts.COLLECTION_RECOIL_STR: return consts.COLLECTION_RECOIL
    if collection == consts.COLLECTION_DREAMS_AND_NIGHTMARES_STR: return consts.COLLECTION_DREAMS_AND_NIGHTMARES
    if collection == consts.COLLECTION_TRAIN_2021_STR: return consts.COLLECTION_TRAIN_2021
    if collection == consts.COLLECTION_DUST2_2021_STR: return consts.COLLECTION_DUST2_2021
    if collection == consts.COLLECTION_MIRAGE_2021_STR: return consts.COLLECTION_MIRAGE_2021
    if collection == consts.COLLECTION_VERTIGO_2021_STR: return consts.COLLECTION_VERTIGO_2021
    if collection == consts.COLLECTION_RIPTIDE_STR: return consts.COLLECTION_RIPTIDE
    if collection == consts.COLLECTION_SNAKEBITE_STR: return consts.COLLECTION_SNAKEBITE
    if collection == consts.COLLECTION_BROKEN_FANG_STR: return consts.COLLECTION_BROKEN_FANG
    if collection == consts.COLLECTION_CONTROL_STR: return consts.COLLECTION_CONTROL
    if collection == consts.COLLECTION_ANCIENT_STR: return consts.COLLECTION_ANCIENT
    if collection == consts.COLLECTION_HAVOC_STR: return consts.COLLECTION_HAVOC
    if collection == consts.COLLECTION_FRACTURE_STR: return consts.COLLECTION_FRACTURE
    if collection == consts.COLLECTION_PRISMA2_STR: return consts.COLLECTION_PRISMA2
    if collection == consts.COLLECTION_CANALS_STR: return consts.COLLECTION_CANALS
    if collection == consts.COLLECTION_ST_MARC_STR: return consts.COLLECTION_ST_MARC
    if collection == consts.COLLECTION_NORSE_STR: return consts.COLLECTION_NORSE
    if collection == consts.COLLECTION_SHATTERED_WEB_STR: return consts.COLLECTION_SHATTERED_WEB
    if collection == consts.COLLECTION_CS20_STR: return consts.COLLECTION_CS20
    if collection == consts.COLLECTION_XRAY_STR: return consts.COLLECTION_XRAY
    if collection == consts.COLLECTION_PRISMA_STR: return consts.COLLECTION_PRISMA
    if collection == consts.COLLECTION_CLUTCH_STR: return consts.COLLECTION_CLUTCH
    if collection == consts.COLLECTION_BLACKSITE_STR: return consts.COLLECTION_BLACKSITE
    if collection == consts.COLLECTION_DANGER_ZONE_STR: return consts.COLLECTION_DANGER_ZONE
    if collection == consts.COLLECTION_NUKE_2018_STR: return consts.COLLECTION_NUKE_2018
    if collection == consts.COLLECTION_INFERNO_2018_STR: return consts.COLLECTION_INFERNO_2018
    if collection == consts.COLLECTION_HORIZON_STR: return consts.COLLECTION_HORIZON
    if collection == consts.COLLECTION_SPECTRUM_2_STR: return consts.COLLECTION_SPECTRUM_2
    if collection == consts.COLLECTION_HYDRA_STR: return consts.COLLECTION_HYDRA
    if collection == consts.COLLECTION_SPECTRUM_STR: return consts.COLLECTION_SPECTRUM
    if collection == consts.COLLECTION_GLOVE_STR: return consts.COLLECTION_GLOVE
    if collection == consts.COLLECTION_GAMMA2_STR: return consts.COLLECTION_GAMMA2
    if collection == consts.COLLECTION_GAMMA_STR: return consts.COLLECTION_GAMMA
    if collection == consts.COLLECTION_CHROMA3_STR: return consts.COLLECTION_CHROMA3
    if collection == consts.COLLECTION_WILDFIRE_STR: return consts.COLLECTION_WILDFIRE
    if collection == consts.COLLECTION_REVOLVER_CASE_STR: return consts.COLLECTION_REVOLVER_CASE
    if collection == consts.COLLECTION_SHADOW_STR: return consts.COLLECTION_SHADOW
    if collection == consts.COLLECTION_RISING_SUN_STR: return consts.COLLECTION_RISING_SUN
    if collection == consts.COLLECTION_GODS_AND_MONSTERS_STR: return consts.COLLECTION_GODS_AND_MONSTERS
    if collection == consts.COLLECTION_CHOP_SHOP_STR: return consts.COLLECTION_CHOP_SHOP
    if collection == consts.COLLECTION_FALCHION_STR: return consts.COLLECTION_FALCHION
    if collection == consts.COLLECTION_CHROMA2_STR: return consts.COLLECTION_CHROMA2
    if collection == consts.COLLECTION_CHROMA_STR: return consts.COLLECTION_CHROMA
    if collection == consts.COLLECTION_VANGUARD_STR: return consts.COLLECTION_VANGUARD
    if collection == consts.COLLECTION_CACHE_STR: return consts.COLLECTION_CACHE
    if collection == consts.COLLECTION_ESPORTS_2014_SUMMER_STR: return consts.COLLECTION_ESPORTS_2014_SUMMER
    if collection == consts.COLLECTION_BREAKOUT_STR: return consts.COLLECTION_BREAKOUT
    if collection == consts.COLLECTION_BAGGAGE_STR: return consts.COLLECTION_BAGGAGE
    if collection == consts.COLLECTION_OVERPASS_STR: return consts.COLLECTION_OVERPASS
    if collection == consts.COLLECTION_COBBLESTONE_STR: return consts.COLLECTION_COBBLESTONE
    if collection == consts.COLLECTION_BANK_STR: return consts.COLLECTION_BANK
    if collection == consts.COLLECTION_HUNTSMAN_STR: return consts.COLLECTION_HUNTSMAN
    if collection == consts.COLLECTION_PHEONIX_STR: return consts.COLLECTION_PHEONIX
    if collection == consts.COLLECTION_ARMS_DEAL_3_STR: return consts.COLLECTION_ARMS_DEAL_3
    if collection == consts.COLLECTION_ESPORTS_2013_WINTER_STR: return consts.COLLECTION_ESPORTS_2013_WINTER
    if collection == consts.COLLECTION_WINTER_OFFENSIVE_STR: return consts.COLLECTION_WINTER_OFFENSIVE
    if collection == consts.COLLECTION_ITALY_STR: return consts.COLLECTION_ITALY
    if collection == consts.COLLECTION_MIRAGE_STR: return consts.COLLECTION_MIRAGE
    if collection == consts.COLLECTION_SAFEHOUSE_STR: return consts.COLLECTION_SAFEHOUSE
    if collection == consts.COLLECTION_DUST2_STR: return consts.COLLECTION_DUST2
    if collection == consts.COLLECTION_LAKE_STR: return consts.COLLECTION_LAKE
    if collection == consts.COLLECTION_TRAIN_STR: return consts.COLLECTION_TRAIN
    if collection == consts.COLLECTION_ARMS_DEAL_2_STR: return consts.COLLECTION_ARMS_DEAL_2
    if collection == consts.COLLECTION_ALPHA_STR: return consts.COLLECTION_ALPHA
    if collection == consts.COLLECTION_BRAVO_STR: return consts.COLLECTION_BRAVO
    if collection == consts.COLLECTION_ASSAULT_STR: return consts.COLLECTION_ASSAULT
    if collection == consts.COLLECTION_DUST_STR: return consts.COLLECTION_DUST
    if collection == consts.COLLECTION_OFFICE_STR: return consts.COLLECTION_OFFICE
    if collection == consts.COLLECTION_NUKE_STR: return consts.COLLECTION_NUKE
    if collection == consts.COLLECTION_AZTEC_STR: return consts.COLLECTION_AZTEC
    if collection == consts.COLLECTION_INFERNO_STR: return consts.COLLECTION_INFERNO
    if collection == consts.COLLECTION_ARMS_DEAL_STR: return consts.COLLECTION_ARMS_DEAL
    if collection == consts.COLLECTION_MILITIA_STR: return consts.COLLECTION_MILITIA
    if collection == consts.COLLECTION_VERTIGO_STR: return consts.COLLECTION_VERTIGO
    if collection == consts.COLLECTION_ESPORTS_2013_STR: return consts.COLLECTION_ESPORTS_2013
    if collection == consts.COLLECTION_TRAIN_2O25_STR: return consts.COLLECTION_TRAIN_2025
    if collection == consts.COLLECTION_RADIANT_STR: return consts.COLLECTION_RADIANT
    if collection == consts.COLLECTION_BOREAL_STR: return consts.COLLECTION_BOREAL
    if collection == consts.COLLECTION_ASCENT_STR: return consts.COLLECTION_ASCENT
    if collection == consts.COLLECTION_FEVER_STR: return consts.COLLECTION_FEVER
    if collection == consts.COLLECTION_GENESIS_STR: return consts.COLLECTION_GENESIS
    return consts.COLLECTION_UNKNOWN

def getMaxCollectionGrade(collection: int) -> int:
    match collection:
        case consts.COLLECTION_OVERPASS_2024: return consts.GRADE_COVERT
        case consts.COLLECTION_GALLERY: return consts.GRADE_COVERT
        case consts.COLLECTION_GRAPHIC_DESIGN: return consts.GRADE_COVERT
        case consts.COLLECTION_LIMITED_EDITION_ITEM: return consts.GRADE_CLASSIFIED
        case consts.COLLECTION_SPORT_AND_FIELD: return consts.GRADE_COVERT
        case consts.COLLECTION_KILOWATT: return consts.GRADE_COVERT
        case consts.COLLECTION_ANUBIS: return consts.GRADE_COVERT
        case consts.COLLECTION_REVOLUTION: return consts.GRADE_COVERT
        case consts.COLLECTION_RECOIL: return consts.GRADE_COVERT
        case consts.COLLECTION_DREAMS_AND_NIGHTMARES: return consts.GRADE_COVERT
        case consts.COLLECTION_TRAIN_2021: return consts.GRADE_COVERT
        case consts.COLLECTION_DUST2_2021: return consts.GRADE_COVERT
        case consts.COLLECTION_MIRAGE_2021: return consts.GRADE_COVERT
        case consts.COLLECTION_VERTIGO_2021: return consts.GRADE_COVERT
        case consts.COLLECTION_RIPTIDE: return consts.GRADE_COVERT
        case consts.COLLECTION_SNAKEBITE: return consts.GRADE_COVERT
        case consts.COLLECTION_BROKEN_FANG: return consts.GRADE_COVERT
        case consts.COLLECTION_CONTROL: return consts.GRADE_COVERT
        case consts.COLLECTION_ANCIENT: return consts.GRADE_COVERT
        case consts.COLLECTION_HAVOC: return consts.GRADE_COVERT
        case consts.COLLECTION_FRACTURE: return consts.GRADE_COVERT
        case consts.COLLECTION_PRISMA2: return consts.GRADE_COVERT
        case consts.COLLECTION_CANALS: return consts.GRADE_COVERT
        case consts.COLLECTION_ST_MARC: return consts.GRADE_COVERT
        case consts.COLLECTION_NORSE: return consts.GRADE_COVERT
        case consts.COLLECTION_SHATTERED_WEB: return consts.GRADE_COVERT 
        case consts.COLLECTION_CS20: return consts.GRADE_COVERT
        case consts.COLLECTION_XRAY: return consts.GRADE_RESTRICTED
        case consts.COLLECTION_PRISMA: return consts.GRADE_COVERT
        case consts.COLLECTION_CLUTCH: return consts.GRADE_COVERT
        case consts.COLLECTION_BLACKSITE: return consts.GRADE_RESTRICTED
        case consts.COLLECTION_DANGER_ZONE: return consts.GRADE_COVERT
        case consts.COLLECTION_NUKE_2018: return consts.GRADE_CLASSIFIED
        case consts.COLLECTION_INFERNO_2018: return consts.GRADE_CLASSIFIED
        case consts.COLLECTION_HORIZON: return consts.GRADE_COVERT
        case consts.COLLECTION_SPECTRUM_2: return consts.GRADE_COVERT
        case consts.COLLECTION_HYDRA: return consts.GRADE_COVERT
        case consts.COLLECTION_SPECTRUM: return consts.GRADE_COVERT
        case consts.COLLECTION_GLOVE: return consts.GRADE_COVERT
        case consts.COLLECTION_GAMMA2: return consts.GRADE_COVERT
        case consts.COLLECTION_GAMMA: return consts.GRADE_COVERT
        case consts.COLLECTION_CHROMA3: return consts.GRADE_COVERT
        case consts.COLLECTION_WILDFIRE: return consts.GRADE_COVERT
        case consts.COLLECTION_REVOLVER_CASE: return consts.GRADE_COVERT
        case consts.COLLECTION_SHADOW: return consts.GRADE_COVERT
        case consts.COLLECTION_RISING_SUN: return consts.GRADE_COVERT
        case consts.COLLECTION_GODS_AND_MONSTERS: return consts.GRADE_COVERT
        case consts.COLLECTION_CHOP_SHOP: return consts.GRADE_CLASSIFIED
        case consts.COLLECTION_FALCHION: return consts.GRADE_COVERT
        case consts.COLLECTION_CHROMA2: return consts.GRADE_COVERT
        case consts.COLLECTION_CHROMA: return consts.GRADE_COVERT
        case consts.COLLECTION_VANGUARD: return consts.GRADE_COVERT
        case consts.COLLECTION_CACHE: return consts.GRADE_RESTRICTED
        case consts.COLLECTION_ESPORTS_2014_SUMMER: return consts.GRADE_COVERT
        case consts.COLLECTION_BREAKOUT: return consts.GRADE_COVERT
        case consts.COLLECTION_BAGGAGE: return consts.GRADE_CLASSIFIED
        case consts.COLLECTION_OVERPASS: return consts.GRADE_CLASSIFIED
        case consts.COLLECTION_COBBLESTONE: return consts.GRADE_COVERT
        case consts.COLLECTION_BANK: return consts.GRADE_CLASSIFIED
        case consts.COLLECTION_HUNTSMAN: return consts.GRADE_COVERT
        case consts.COLLECTION_PHEONIX: return consts.GRADE_COVERT
        case consts.COLLECTION_ARMS_DEAL_3: return consts.GRADE_COVERT
        case consts.COLLECTION_ESPORTS_2013_WINTER: return consts.GRADE_COVERT
        case consts.COLLECTION_WINTER_OFFENSIVE: return consts.GRADE_COVERT
        case consts.COLLECTION_ITALY: return consts.GRADE_RESTRICTED
        case consts.COLLECTION_MIRAGE: return consts.GRADE_RESTRICTED
        case consts.COLLECTION_SAFEHOUSE: return consts.GRADE_RESTRICTED
        case consts.COLLECTION_DUST2: return consts.GRADE_CLASSIFIED
        case consts.COLLECTION_LAKE: return consts.GRADE_RESTRICTED
        case consts.COLLECTION_TRAIN: return consts.GRADE_RESTRICTED
        case consts.COLLECTION_ARMS_DEAL_2: return consts.GRADE_COVERT
        case consts.COLLECTION_ALPHA: return consts.GRADE_RESTRICTED
        case consts.COLLECTION_BRAVO: return consts.GRADE_COVERT
        case consts.COLLECTION_ASSAULT: return consts.GRADE_RESTRICTED
        case consts.COLLECTION_DUST: return consts.GRADE_RESTRICTED
        case consts.COLLECTION_OFFICE: return consts.GRADE_MILSPEC
        case consts.COLLECTION_NUKE: return consts.GRADE_RESTRICTED
        case consts.COLLECTION_AZTEC: return consts.GRADE_MILSPEC
        case consts.COLLECTION_INFERNO: return consts.GRADE_MILSPEC
        case consts.COLLECTION_ARMS_DEAL: return consts.GRADE_COVERT
        case consts.COLLECTION_MILITIA: return consts.GRADE_CLASSIFIED
        case consts.COLLECTION_VERTIGO: return consts.GRADE_RESTRICTED
        case consts.COLLECTION_ESPORTS_2013: return consts.GRADE_COVERT
        case consts.COLLECTION_TRAIN_2025: return consts.GRADE_COVERT
        case consts.COLLECTION_RADIANT: return consts.GRADE_CLASSIFIED
        case consts.COLLECTION_BOREAL: return consts.GRADE_CLASSIFIED
        case consts.COLLECTION_ASCENT: return consts.GRADE_CLASSIFIED
        case consts.COLLECTION_FEVER: return consts.GRADE_COVERT
        case consts.COLLECTION_GENESIS: return consts.GRADE_COVERT
        case _: return -1

def validCollection(collection: int):
    return collection >= 0 and collection < consts.COLLECTION_MAX

def crateToString(crate: int):
    match crate:
        case consts.CRATE_GENESIS: return consts.CRATE_GENESIS_STR
        case consts.CRATE_FEVER: return consts.CRATE_FEVER_STR
        case consts.CRATE_GALLERY: return consts.CRATE_GALLERY_STR
        case consts.CRATE_KILOWATT: return consts.CRATE_KILOWATT_STR
        case consts.CRATE_ANUBIS: return consts.CRATE_ANUBIS_STR
        case consts.CRATE_REVOLUTION: return consts.CRATE_REVOLUTION_STR
        case consts.CRATE_RECOIL: return consts.CRATE_RECOIL_STR
        case consts.CRATE_DREAMS_AND_NIGHTMARES: return consts.CRATE_DREAMS_AND_NIGHTMARES_STR
        case consts.CRATE_RIPTIDE: return consts.CRATE_RIPTIDE_STR
        case consts.CRATE_SNAKEBITE: return consts.CRATE_SNAKEBITE_STR
        case consts.CRATE_BROKEN_FANG: return consts.CRATE_BROKEN_FANG_STR
        case consts.CRATE_FRACTURE: return consts.CRATE_FRACTURE_STR
        case consts.CRATE_PRISMA2: return consts.CRATE_PRISMA2_STR
        case consts.CRATE_CS20: return consts.CRATE_CS20_STR
        case consts.CRATE_XRAY: return consts.CRATE_XRAY_STR
        case consts.CRATE_SHATTERED_WEB: return consts.CRATE_SHATTERED_WEB_STR
        case consts.CRATE_PRISMA: return consts.CRATE_PRISMA_STR
        case consts.CRATE_DANGER_ZONE: return consts.CRATE_DANGER_ZONE_STR
        case consts.CRATE_HORIZON: return consts.CRATE_HORIZON_STR
        case consts.CRATE_CLUTCH: return consts.CRATE_CLUTCH_STR
        case consts.CRATE_SPECTRUM2: return consts.CRATE_SPECTRUM2_STR
        case consts.CRATE_HYDRA: return consts.CRATE_HYDRA_STR
        case consts.CRATE_SPECTRUM: return consts.CRATE_SPECTRUM_STR
        case consts.CRATE_GLOVE: return consts.CRATE_GLOVE_STR
        case consts.CRATE_GAMMA2: return consts.CRATE_GAMMA2_STR
        case consts.CRATE_GAMMA: return consts.CRATE_GAMMA_STR
        case consts.CRATE_CHROMA3: return consts.CRATE_CHROMA3_STR
        case consts.CRATE_WILDFIRE: return consts.CRATE_WILDFIRE_STR
        case consts.CRATE_REVOLVER: return consts.CRATE_REVOLVER_STR
        case consts.CRATE_SHADOW: return consts.CRATE_SHADOW_STR
        case consts.CRATE_FALCHION: return consts.CRATE_FALCHION_STR
        case consts.CRATE_CHROMA2: return consts.CRATE_CHROMA2_STR
        case consts.CRATE_CHROMA: return consts.CRATE_CHROMA_STR
        case consts.CRATE_VANGUARD: return consts.CRATE_VANGUARD_STR
        case consts.CRATE_ESPORTS_2014_SUMMER: return consts.CRATE_ESPORTS_2014_SUMMER_STR
        case consts.CRATE_BREAKOUT: return consts.CRATE_BREAKOUT_STR
        case consts.CRATE_HUNTSMAN: return consts.CRATE_HUNTSMAN_STR
        case consts.CRATE_PHEONIX: return consts.CRATE_PHEONIX_STR
        case consts.CRATE_WEAPON_CASE_3: return consts.CRATE_WEAPON_CASE_3_STR
        case consts.CRATE_WINTER_OFFENSIVE: return consts.CRATE_WINTER_OFFENSIVE_STR
        case consts.CRATE_ESPORTS_2013_WINTER: return consts.CRATE_ESPORTS_2013_WINTER_STR
        case consts.CRATE_WEAPON_CASE_2: return consts.CRATE_WEAPON_CASE_2_STR
        case consts.CRATE_BRAVO: return consts.CRATE_BRAVO_STR
        case consts.CRATE_ESPORTS_2013: return consts.CRATE_ESPORTS_2013_STR
        case consts.CRATE_WEAPON_CASE: return consts.CRATE_WEAPON_CASE_STR
        case _: return "?"

def crateToInt(crate: str):
    if crate == consts.CRATE_GENESIS_STR: return consts.CRATE_GENESIS
    if crate == consts.CRATE_FEVER_STR: return consts.CRATE_FEVER
    if crate == consts.CRATE_GALLERY_STR: return consts.CRATE_GALLERY
    if crate == consts.CRATE_KILOWATT_STR: return consts.CRATE_KILOWATT
    if crate == consts.CRATE_ANUBIS_STR: return consts.CRATE_ANUBIS
    if crate == consts.CRATE_REVOLUTION_STR: return consts.CRATE_REVOLUTION
    if crate == consts.CRATE_RECOIL_STR: return consts.CRATE_RECOIL
    if crate == consts.CRATE_DREAMS_AND_NIGHTMARES_STR: return consts.CRATE_DREAMS_AND_NIGHTMARES
    if crate == consts.CRATE_RIPTIDE_STR: return consts.CRATE_RIPTIDE
    if crate == consts.CRATE_SNAKEBITE_STR: return consts.CRATE_SNAKEBITE
    if crate == consts.CRATE_BROKEN_FANG_STR: return consts.CRATE_BROKEN_FANG
    if crate == consts.CRATE_FRACTURE_STR: return consts.CRATE_FRACTURE
    if crate == consts.CRATE_PRISMA2_STR: return consts.CRATE_PRISMA2
    if crate == consts.CRATE_CS20_STR: return consts.CRATE_CS20
    if crate == consts.CRATE_XRAY_STR: return consts.CRATE_XRAY
    if crate == consts.CRATE_SHATTERED_WEB_STR: return consts.CRATE_SHATTERED_WEB
    if crate == consts.CRATE_PRISMA_STR: return consts.CRATE_PRISMA
    if crate == consts.CRATE_DANGER_ZONE_STR: return consts.CRATE_DANGER_ZONE
    if crate == consts.CRATE_HORIZON_STR: return consts.CRATE_HORIZON
    if crate == consts.CRATE_CLUTCH_STR: return consts.CRATE_CLUTCH
    if crate == consts.CRATE_SPECTRUM2_STR: return consts.CRATE_SPECTRUM2
    if crate == consts.CRATE_HYDRA_STR: return consts.CRATE_HYDRA
    if crate == consts.CRATE_SPECTRUM_STR: return consts.CRATE_SPECTRUM
    if crate == consts.CRATE_GLOVE_STR: return consts.CRATE_GLOVE
    if crate == consts.CRATE_GAMMA2_STR: return consts.CRATE_GAMMA2
    if crate == consts.CRATE_GAMMA_STR: return consts.CRATE_GAMMA
    if crate == consts.CRATE_CHROMA3_STR: return consts.CRATE_CHROMA3
    if crate == consts.CRATE_WILDFIRE_STR: return consts.CRATE_WILDFIRE
    if crate == consts.CRATE_REVOLVER_STR: return consts.CRATE_REVOLVER
    if crate == consts.CRATE_SHADOW_STR: return consts.CRATE_SHADOW
    if crate == consts.CRATE_FALCHION_STR: return consts.CRATE_FALCHION
    if crate == consts.CRATE_CHROMA2_STR: return consts.CRATE_CHROMA2
    if crate == consts.CRATE_CHROMA_STR: return consts.CRATE_CHROMA
    if crate == consts.CRATE_VANGUARD_STR: return consts.CRATE_VANGUARD
    if crate == consts.CRATE_ESPORTS_2014_SUMMER_STR: return consts.CRATE_ESPORTS_2014_SUMMER
    if crate == consts.CRATE_BREAKOUT_STR: return consts.CRATE_BREAKOUT
    if crate == consts.CRATE_HUNTSMAN_STR: return consts.CRATE_HUNTSMAN
    if crate == consts.CRATE_PHEONIX_STR: return consts.CRATE_PHEONIX
    if crate == consts.CRATE_WEAPON_CASE_3_STR: return consts.CRATE_WEAPON_CASE_3
    if crate == consts.CRATE_WINTER_OFFENSIVE_STR: return consts.CRATE_WINTER_OFFENSIVE
    if crate == consts.CRATE_ESPORTS_2013_WINTER_STR: return consts.CRATE_ESPORTS_2013_WINTER
    if crate == consts.CRATE_WEAPON_CASE_2_STR: return consts.CRATE_WEAPON_CASE_2
    if crate == consts.CRATE_BRAVO_STR: return consts.CRATE_BRAVO
    if crate == consts.CRATE_ESPORTS_2013_STR: return consts.CRATE_ESPORTS_2013
    if crate == consts.CRATE_WEAPON_CASE_STR: return consts.CRATE_WEAPON_CASE
    return consts.CRATE_UNKNOWN

def getMaxCrateGrade(crate: int):
    match crate:
        case consts.CRATE_GENESIS: return consts.GRADE_COVERT
        case consts.CRATE_FEVER: return consts.GRADE_STAR
        case consts.CRATE_GALLERY: return consts.GRADE_STAR
        case consts.CRATE_KILOWATT: return consts.GRADE_STAR
        case consts.CRATE_ANUBIS: return consts.GRADE_COVERT
        case consts.CRATE_REVOLUTION: return consts.GRADE_STAR
        case consts.CRATE_RECOIL: return consts.GRADE_STAR
        case consts.CRATE_DREAMS_AND_NIGHTMARES: return consts.GRADE_STAR
        case consts.CRATE_RIPTIDE: return consts.GRADE_STAR
        case consts.CRATE_SNAKEBITE: return consts.GRADE_STAR
        case consts.CRATE_BROKEN_FANG: return consts.GRADE_STAR
        case consts.CRATE_FRACTURE: return consts.GRADE_STAR
        case consts.CRATE_PRISMA2: return consts.GRADE_STAR
        case consts.CRATE_CS20: return consts.GRADE_STAR
        case consts.CRATE_XRAY: return consts.GRADE_RESTRICTED
        case consts.CRATE_SHATTERED_WEB: return consts.GRADE_STAR
        case consts.CRATE_PRISMA: return consts.GRADE_STAR
        case consts.CRATE_DANGER_ZONE: return consts.GRADE_STAR
        case consts.CRATE_HORIZON: return consts.GRADE_STAR
        case consts.CRATE_CLUTCH: return consts.GRADE_STAR
        case consts.CRATE_SPECTRUM2: return consts.GRADE_STAR
        case consts.CRATE_HYDRA: return consts.GRADE_STAR
        case consts.CRATE_SPECTRUM: return consts.GRADE_STAR
        case consts.CRATE_GLOVE: return consts.GRADE_STAR
        case consts.CRATE_GAMMA2: return consts.GRADE_STAR
        case consts.CRATE_GAMMA: return consts.GRADE_STAR
        case consts.CRATE_CHROMA3: return consts.GRADE_STAR
        case consts.CRATE_WILDFIRE: return consts.GRADE_STAR
        case consts.CRATE_REVOLVER: return consts.GRADE_STAR
        case consts.CRATE_SHADOW: return consts.GRADE_STAR
        case consts.CRATE_FALCHION: return consts.GRADE_STAR
        case consts.CRATE_CHROMA2: return consts.GRADE_STAR
        case consts.CRATE_CHROMA: return consts.GRADE_STAR
        case consts.CRATE_VANGUARD: return consts.GRADE_STAR
        case consts.CRATE_ESPORTS_2014_SUMMER: return consts.GRADE_STAR
        case consts.CRATE_BREAKOUT: return consts.GRADE_STAR
        case consts.CRATE_HUNTSMAN: return consts.GRADE_STAR
        case consts.CRATE_PHEONIX: return consts.GRADE_STAR
        case consts.CRATE_WEAPON_CASE_3: return consts.GRADE_STAR
        case consts.CRATE_WINTER_OFFENSIVE: return consts.GRADE_STAR
        case consts.CRATE_ESPORTS_2013_WINTER: return consts.GRADE_STAR
        case consts.CRATE_WEAPON_CASE_2: return consts.GRADE_STAR
        case consts.CRATE_BRAVO: return consts.GRADE_STAR
        case consts.CRATE_ESPORTS_2013: return consts.GRADE_STAR
        case consts.CRATE_WEAPON_CASE: return consts.GRADE_STAR
        case _: return -1

def crateToCollection(crate: int):
    match crate:
        case consts.CRATE_GENESIS: return consts.COLLECTION_GENESIS
        case consts.CRATE_FEVER: return consts.COLLECTION_FEVER
        case consts.CRATE_GALLERY: return consts.COLLECTION_GALLERY
        case consts.CRATE_KILOWATT: return consts.COLLECTION_KILOWATT
        case consts.CRATE_ANUBIS: return consts.COLLECTION_ANUBIS
        case consts.CRATE_REVOLUTION: return consts.COLLECTION_REVOLUTION
        case consts.CRATE_RECOIL: return consts.COLLECTION_RECOIL
        case consts.CRATE_DREAMS_AND_NIGHTMARES: return consts.COLLECTION_DREAMS_AND_NIGHTMARES
        case consts.CRATE_RIPTIDE: return consts.COLLECTION_RIPTIDE
        case consts.CRATE_SNAKEBITE: return consts.COLLECTION_SNAKEBITE
        case consts.CRATE_BROKEN_FANG: return consts.COLLECTION_BROKEN_FANG
        case consts.CRATE_FRACTURE: return consts.COLLECTION_FRACTURE
        case consts.CRATE_PRISMA2: return consts.COLLECTION_PRISMA2
        case consts.CRATE_CS20: return consts.COLLECTION_CS20
        case consts.CRATE_XRAY: return consts.COLLECTION_XRAY
        case consts.CRATE_SHATTERED_WEB: return consts.COLLECTION_SHATTERED_WEB
        case consts.CRATE_PRISMA: return consts.COLLECTION_PRISMA
        case consts.CRATE_DANGER_ZONE: return consts.COLLECTION_DANGER_ZONE
        case consts.CRATE_HORIZON: return consts.COLLECTION_HORIZON
        case consts.CRATE_CLUTCH: return consts.COLLECTION_CLUTCH
        case consts.CRATE_SPECTRUM2: return consts.COLLECTION_SPECTRUM_2
        case consts.CRATE_HYDRA: return consts.COLLECTION_HYDRA
        case consts.CRATE_SPECTRUM: return consts.COLLECTION_SPECTRUM
        case consts.CRATE_GLOVE: return consts.COLLECTION_GLOVE
        case consts.CRATE_GAMMA2: return consts.COLLECTION_GAMMA2
        case consts.CRATE_GAMMA: return consts.COLLECTION_GAMMA
        case consts.CRATE_CHROMA3: return consts.COLLECTION_CHROMA3
        case consts.CRATE_WILDFIRE: return consts.COLLECTION_WILDFIRE
        case consts.CRATE_REVOLVER: return consts.COLLECTION_REVOLVER_CASE
        case consts.CRATE_SHADOW: return consts.COLLECTION_SHADOW
        case consts.CRATE_FALCHION: return consts.COLLECTION_FALCHION
        case consts.CRATE_CHROMA2: return consts.COLLECTION_CHROMA2
        case consts.CRATE_CHROMA: return consts.COLLECTION_CHROMA
        case consts.CRATE_VANGUARD: return consts.COLLECTION_VANGUARD
        case consts.CRATE_ESPORTS_2014_SUMMER: return consts.COLLECTION_ESPORTS_2014_SUMMER
        case consts.CRATE_BREAKOUT: return consts.COLLECTION_BREAKOUT
        case consts.CRATE_HUNTSMAN: return consts.COLLECTION_HUNTSMAN
        case consts.CRATE_PHEONIX: return consts.COLLECTION_PHEONIX
        case consts.CRATE_WEAPON_CASE_3: return consts.COLLECTION_ARMS_DEAL_3
        case consts.CRATE_WINTER_OFFENSIVE: return consts.COLLECTION_WINTER_OFFENSIVE
        case consts.CRATE_ESPORTS_2013_WINTER: return consts.COLLECTION_ESPORTS_2013_WINTER
        case consts.CRATE_WEAPON_CASE_2: return consts.COLLECTION_ARMS_DEAL_2
        case consts.CRATE_BRAVO: return consts.COLLECTION_BRAVO
        case consts.CRATE_ESPORTS_2013: return consts.COLLECTION_ESPORTS_2013
        case consts.CRATE_WEAPON_CASE: return consts.COLLECTION_ARMS_DEAL
        case _: return consts.COLLECTION_UNKNOWN

def collectionToCrate(collection: int):
    match collection:
        case consts.COLLECTION_GENESIS: return consts.CRATE_GENESIS
        case consts.COLLECTION_FEVER: return consts.CRATE_FEVER
        case consts.COLLECTION_GALLERY: return consts.CRATE_GALLERY
        case consts.COLLECTION_KILOWATT: return consts.CRATE_KILOWATT
        case consts.COLLECTION_ANUBIS: return consts.CRATE_ANUBIS
        case consts.COLLECTION_REVOLUTION: return consts.CRATE_REVOLUTION
        case consts.COLLECTION_RECOIL: return consts.CRATE_RECOIL
        case consts.COLLECTION_DREAMS_AND_NIGHTMARES: return consts.CRATE_DREAMS_AND_NIGHTMARES
        case consts.COLLECTION_RIPTIDE: return consts.CRATE_RIPTIDE
        case consts.COLLECTION_SNAKEBITE: return consts.CRATE_SNAKEBITE
        case consts.COLLECTION_BROKEN_FANG: return consts.CRATE_BROKEN_FANG
        case consts.COLLECTION_FRACTURE: return consts.CRATE_FRACTURE
        case consts.COLLECTION_PRISMA2: return consts.CRATE_PRISMA2
        case consts.COLLECTION_CS20: return consts.CRATE_CS20
        case consts.COLLECTION_XRAY: return consts.CRATE_XRAY
        case consts.COLLECTION_SHATTERED_WEB: return consts.CRATE_SHATTERED_WEB
        case consts.COLLECTION_PRISMA: return consts.CRATE_PRISMA
        case consts.COLLECTION_DANGER_ZONE: return consts.CRATE_DANGER_ZONE
        case consts.COLLECTION_HORIZON: return consts.CRATE_HORIZON
        case consts.COLLECTION_CLUTCH: return consts.CRATE_CLUTCH
        case consts.COLLECTION_SPECTRUM_2: return consts.CRATE_SPECTRUM2
        case consts.COLLECTION_HYDRA: return consts.CRATE_HYDRA
        case consts.COLLECTION_SPECTRUM: return consts.CRATE_SPECTRUM
        case consts.COLLECTION_GLOVE: return consts.CRATE_GLOVE
        case consts.COLLECTION_GAMMA2: return consts.CRATE_GAMMA2
        case consts.COLLECTION_GAMMA: return consts.CRATE_GAMMA
        case consts.COLLECTION_CHROMA3: return consts.CRATE_CHROMA3
        case consts.COLLECTION_WILDFIRE: return consts.CRATE_WILDFIRE
        case consts.COLLECTION_REVOLVER_CASE: return consts.CRATE_REVOLVER
        case consts.COLLECTION_SHADOW: return consts.CRATE_SHADOW
        case consts.COLLECTION_FALCHION: return consts.CRATE_FALCHION
        case consts.COLLECTION_CHROMA2: return consts.CRATE_CHROMA2
        case consts.COLLECTION_CHROMA: return consts.CRATE_CHROMA
        case consts.COLLECTION_VANGUARD: return consts.CRATE_VANGUARD
        case consts.COLLECTION_ESPORTS_2014_SUMMER: return consts.CRATE_ESPORTS_2014_SUMMER
        case consts.COLLECTION_BREAKOUT: return consts.CRATE_BREAKOUT
        case consts.COLLECTION_HUNTSMAN: return consts.CRATE_HUNTSMAN
        case consts.COLLECTION_PHEONIX: return consts.CRATE_PHEONIX
        case consts.COLLECTION_ARMS_DEAL_3: return consts.CRATE_WEAPON_CASE_3
        case consts.COLLECTION_WINTER_OFFENSIVE: return consts.CRATE_WINTER_OFFENSIVE
        case consts.COLLECTION_ESPORTS_2013_WINTER: return consts.CRATE_ESPORTS_2013_WINTER
        case consts.COLLECTION_ARMS_DEAL_2: return consts.CRATE_WEAPON_CASE_2
        case consts.COLLECTION_BRAVO: return consts.CRATE_BRAVO
        case consts.COLLECTION_ESPORTS_2013: return consts.CRATE_ESPORTS_2013
        case consts.COLLECTION_ARMS_DEAL: return consts.CRATE_WEAPON_CASE
        case _: return consts.CRATE_UNKNOWN

def itemFloatValToInt(val: float) -> int:
    if val >= 0.0 and val <= consts.FLOAT_MAX_FACTORY_NEW: return consts.WEAR_FACTORY_NEW
    if val >= 0.0 and val <= consts.FLOAT_MAX_MINIMAL_WEAR: return consts.WEAR_MINIMAL_WEAR
    if val >= 0.0 and val <= consts.FLOAT_MAX_FIELD_TESTED: return consts.WEAR_FIELD_TESTED
    if val >= 0.0 and val <= consts.FLOAT_MAX_WELL_WORN: return consts.WEAR_WELL_WORN
    if val >= 0.0 and val <= consts.FLOAT_MAX_BATTLE_SCARRED: return consts.WEAR_BATTLE_SCARRED
    return -1.0

def gradeToRGBString(grade: int) -> str:
    match grade:
        case consts.GRADE_CONSUMER: return consts.GRADE_CONSUMER_RGB_STR 
        case consts.GRADE_INDUSTRIAL: return consts.GRADE_INDUSTRIAL_RGB_STR 
        case consts.GRADE_MILSPEC: return consts.GRADE_MILSPEC_RGB_STR 
        case consts.GRADE_RESTRICTED: return consts.GRADE_RESTRICTED_RGB_STR
        case consts.GRADE_CLASSIFIED: return consts.GRADE_CLASSIFIED_RGB_STR
        case consts.GRADE_COVERT: return consts.GRADE_COVERT_RGB_STR 
        case consts.GRADE_STAR: return consts.GRADE_STAR_RGB_STR
        case consts.GRADE_CONTRABAND: return consts.GRADE_CONTRABAND_RGB_STR 
        case _: return "0, 0, 0"