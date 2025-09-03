import types
import os
import platform
import sys
import shared_args
from pathlib import Path

system = platform.system()

# _____ URLS _____ #

URL_MARKET_ENGINE = "http://localhost:3000"
URL_MARKET_ENGINE_UPDATE_ITEMS = URL_MARKET_ENGINE + "/api/update_items"
URL_MARKET_ENGINE_FETCH_ITEMS = URL_MARKET_ENGINE + "/api/fetch_items"
URL_MARKET_ENGINE_FETCH_SERVER_STATUS = URL_MARKET_ENGINE + "/api/fetch_status"
URL_CSFLOAT_API_GET_LISTINGS = "https://csfloat.com/api/v1/listings"
URL_SKINPORT_GET_ITEMS = "https://api.skinport.com/v1/sales/history"
URL_MARKET_ENGINE_REPO = "https://github.com/1FIL0/Market-Engine-Client"
URL_1FIL0_YOUTUBE = "https://www.youtube.com/@1FIL0-f7f"
URL_1FIL0_DISCORD = "/"
URL_1FIL0_GITHUB = "https://github.com/1FIL0"


# __ CONFIGS / DATA __ #

PATH_DATA_CLIENT: Path = Path()
PATH_DATA_API: Path = Path()
PATH_CONFIG_CLIENT: Path = Path()
PATH_CONFIG_API: Path = Path()

# OS-specific base paths
if system == "Windows":
    APPDATA = Path(os.environ['APPDATA'])
    LOCALAPPDATA = Path(os.environ.get('LOCALAPPDATA', os.environ['APPDATA']))
    PATH_CONFIG_CLIENT = APPDATA / 'market_engine_client'
    PATH_CONFIG_API = APPDATA / 'market_engine_api'
    PATH_DATA_CLIENT = LOCALAPPDATA / 'market_engine_client'
    PATH_DATA_API = LOCALAPPDATA / 'market_engine_api'

elif system == "Linux":
    HOME = Path(os.environ['HOME'])
    PATH_CONFIG_CLIENT = HOME / '.config' / 'market_engine_client'
    PATH_CONFIG_API = HOME / '.config' / 'market_engine_api'
    PATH_DATA_CLIENT = HOME / '.local' / 'share' / 'market_engine_client'
    PATH_DATA_API = HOME / '.local' / 'share' / 'market_engine_api'

# Client config files
PATH_CONFIG_CLIENT_SONAR = PATH_CONFIG_CLIENT / "sonar.json"
PATH_CONFIG_CLIENT_TRADEUP_ENGINE = PATH_CONFIG_CLIENT / "tradeup_engine.json"
PATH_CONFIG_CLIENT_ITEM_LIBRARY = PATH_CONFIG_CLIENT / "item_library.json"
PATH_CONFIG_CLIENT_UI = PATH_CONFIG_CLIENT / "ui.json"
PATH_CONFIG_CLIENT_SERVER = PATH_CONFIG_CLIENT / "server.json"

# API config files
PATH_CONFIG_API_SONAR = PATH_CONFIG_API / "sonar.json"

# Client data files
PATH_DATA_CLIENT_READY_ITEMS = PATH_DATA_CLIENT / "ready_items.json"
PATH_DATA_CLIENT_PROFITABLE_TRADEUPS = PATH_DATA_CLIENT / "profitable_tradeups.json"
PATH_DATA_CLIENT_MODIFIED_ITEMS = PATH_DATA_CLIENT / "modified_items.json"

# API data files
PATH_DATA_API_BYMYKEL_CSGO_API_ITEMS = PATH_DATA_API / "bymykel_csgo_api_items.json"
PATH_DATA_API_STEAM_WEB_API_ITEMS = PATH_DATA_API / "steam_web_api_items.json"
PATH_DATA_API_CSFLOAT_ITEMS = PATH_DATA_API / "csfloat_items.json"
PATH_DATA_API_SKINPORT_ITEMS = PATH_DATA_API / "skinport_items.json"
PATH_DATA_API_READY_ITEMS = PATH_DATA_API / "ready_items.json"
PATH_DATA_API_SCRAPED_ITEMS = PATH_DATA_API / "scraped_items.json"
PATH_DATA_API_SCRAPED_PAGES = PATH_DATA_API / "scraped_pages.json"

# __ DIST / BINARIES __ #

PATH_SHARE_HERE = Path(__file__).resolve().parent
PATH_MEIPASS = Path(getattr(sys, "_MEIPASS", Path(".").resolve()))
PATH_BINARY = Path(sys.executable).parent
currentDir = PATH_BINARY
while currentDir.name != "bin" and currentDir.parent != currentDir:
    currentDir = currentDir.parent
PATH_DIST_BIN = currentDir
PATH_BINARY_DIRNAME = PATH_BINARY.name

PATH_DIST_ASSETS: Path = Path()
PATH_DIST_ASSETS_SKINS: Path = Path()
PATH_DIST_CLIENT_APP_BINARY: Path = Path()
PATH_DIST_CLIENT_SONAR_BINARY: Path = Path()
PATH_DIST_CLIENT_TRADEUP_ENGINE_BINARY: Path = Path()
PATH_DIST_API_APP_BINARY: Path = Path()
PATH_DIST_API_SONAR_BINARY: Path = Path()
PATH_DIST_DRIVERS: Path = Path()
PATH_DIST_DRIVER_GECKODRIVER_PATH: Path = Path()

# Handle developer or release distribution
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
    PATH_DIST_ASSETS_SKINS = PATH_MARKET_ENGINE_ASSETS_SKINS
    PATH_DIST_DRIVERS = PATH_MARKET_ENGINE_DRIVERS

    if system == "Linux":
        PATH_DIST_CLIENT_TRADEUP_ENGINE_BINARY = PATH_CLIENT_TRADEUP_ENGINE / "build" / "build_linux64" / "engine"
    elif system == "Windows":
        PATH_DIST_CLIENT_TRADEUP_ENGINE_BINARY = PATH_CLIENT_TRADEUP_ENGINE / "build" / "build_win64" / "engine"

elif shared_args.argDist == "release":
    if system == "Linux":
        PATH_DIST_CLIENT_APP_BINARY = PATH_DIST_BIN / "application" / "application"
        PATH_DIST_CLIENT_SONAR_BINARY = PATH_DIST_BIN / "sonar" / "sonar"
        PATH_DIST_CLIENT_TRADEUP_ENGINE_BINARY = PATH_DIST_BIN / "engine"
        PATH_DIST_API_SONAR_BINARY = PATH_DIST_BIN / "sonar" / "sonar"
    elif system == "Windows":
        PATH_DIST_CLIENT_APP_BINARY = PATH_DIST_BIN / "application" / "application.exe"
        PATH_DIST_CLIENT_SONAR_BINARY = PATH_DIST_BIN / "sonar" / "sonar.exe"
        PATH_DIST_CLIENT_TRADEUP_ENGINE_BINARY = PATH_DIST_BIN / "engine.exe"
        PATH_DIST_API_SONAR_BINARY = PATH_DIST_BIN / "sonar" / "sonar.exe"

    PATH_DIST_ASSETS = PATH_MEIPASS / "market_engine_assets"
    PATH_DIST_ASSETS_SKINS = PATH_DIST_ASSETS / "skins"
    PATH_DIST_DRIVERS = PATH_MEIPASS / "drivers"

# Drivers
if system == "Windows":
    PATH_DIST_DRIVER_GECKODRIVER_PATH = PATH_DIST_DRIVERS / "geckodriver_win32.exe"
elif system == "Linux":
    PATH_DIST_DRIVER_GECKODRIVER_PATH = PATH_DIST_DRIVERS / "geckodriver_linux64"


consts = types.SimpleNamespace()

# _____ GRADES ______ #

consts.GRADE_CONSUMER = 0; consts.GRADE_CONSUMER_STR = "Consumer"
consts.GRADE_INDUSTRIAL = 1; consts.GRADE_INDUSTRIAL_STR = "Industrial"
consts.GRADE_MILSPEC = 2; consts.GRADE_MILSPEC_STR = "Milspec"
consts.GRADE_RESTRICTED = 3; consts.GRADE_RESTRICTED_STR = "Restricted"
consts.GRADE_CLASSIFIED = 4; consts.GRADE_CLASSIFIED_STR = "Classified"
consts.GRADE_COVERT = 5; consts.GRADE_COVERT_STR = "Covert"
consts.GRADE_CONTRABAND = 6; consts.GRADE_CONTRABAND_STR = "Contraband"
consts.GRADE_MAX = 7
consts.GRADE_CONSUMER_RGB_STR = "204, 204, 204"
consts.GRADE_INDUSTRIAL_RGB_STR = "75, 105, 255"
consts.GRADE_MILSPEC_RGB_STR = "0, 100, 255"
consts.GRADE_RESTRICTED_RGB_STR = "136, 71, 255"
consts.GRADE_CLASSIFIED_RGB_STR = "211, 44, 230"
consts.GRADE_COVERT_RGB_STR = "235, 75, 75"
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
consts.WEAR_MAX = 5

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
consts.COLLECTION_MAX = 88

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
    return -1

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
        case _: return -1

def gradeToRGBString(grade: int) -> str:
    match grade:
        case consts.GRADE_CONSUMER: return consts.GRADE_CONSUMER_RGB_STR 
        case consts.GRADE_INDUSTRIAL: return consts.GRADE_INDUSTRIAL_RGB_STR 
        case consts.GRADE_MILSPEC: return consts.GRADE_MILSPEC_RGB_STR 
        case consts.GRADE_RESTRICTED: return consts.GRADE_RESTRICTED_RGB_STR
        case consts.GRADE_CLASSIFIED: return consts.GRADE_CLASSIFIED_RGB_STR
        case consts.GRADE_COVERT: return consts.GRADE_COVERT_RGB_STR 
        case consts.GRADE_CONTRABAND: return consts.GRADE_CONTRABAND_RGB_STR 
        case _: return "0, 0, 0"