#pragma once

#include "namespace.hpp"
#include <string>
#include <cstdlib>

// FILES

#if defined(_WIN32)
    const std::string PATH_HERE = __FILE__;
    const std::string DIR_HERE = {PATH_HERE.substr(0, PATH_HERE.rfind("/"))};
    #define SYSTEM_NAME                                 "Linux"
    #define ENV_HOME                                    std::getenv("HOME")
    #define PATH_CONFIG_CLIENT                          std::string(std::getenv("APPDATA")) + "\\market_engine_client"
    #define PATH_DATA_CLIENT                            std::string(std::getenv("LOCALAPPDATA")) + "\\market_engine_client"
    #define DIR_MARKET_ENGINE                           std::string(DIR_HERE) + "\\..\\..\\..\\..\\.."
    #define DIR_MARKET_ENGINE_CLIENT                    std::string(DIR_MARKET_ENGINE) + "\\market_engine_client"
    #define DIR_MARKET_ENGINE_APPLICATION               std::string(DIR_MARKET_ENGINE_CLIENT) + "\\python\\application"
    #define DIR_MARKET_ENGINE_SONAR                     std::string(DIR_MARKET_ENGINE_CLIENT) + "\\python\\sonar"
    #define DIR_MARKET_ENGINE_CALCULATOR                std::string(DIR_MARKET_ENGINE_CLIENT) + "\\cpp\\calculator"
    #define DIR_MARKET_ENGINE_GPU_KERNEL_PATH           std::string(DIR_MARKET_ENGINE_CALCULATOR) + "\\src\\gpu_kernel_embedded"
    #define PATH_CONFIG_CLIENT_TRADEUP_ENGINE       std::string(PATH_CONFIG_CLIENT) + "\\tradeup_engine.json"
    #define PATH_DATA_CLIENT_READY_ITEMS                std::string(PATH_DATA_CLIENT) + "\\ready_items.json"
    #define PATH_DATA_CLIENT_MODIFIED_ITEMS             std::string(PATH_DATA_CLIENT) + "\\modified_items.json"
    #define PATH_DATA_CLIENT_PROFITABLE_TRADEUPS        std::string(PATH_DATA_CLIENT) + "\\profitable_tradeups.json"
    #define PATH_DATA_CLIENT_PROFITABLE_TRADEUPS_TEMP   std::string(PATH_DATA_CLIENT) + "\\profitable_tradeups.json.temp"

#elif defined(__linux__)
    const std::string PATH_HERE = __FILE__;
    const std::string DIR_HERE = {PATH_HERE.substr(0, PATH_HERE.rfind("/"))};
    #define SYSTEM_NAME                                 "Linux"
    #define ENV_HOME                                    std::getenv("HOME")
    #define PATH_CONFIG_CLIENT                          std::string(ENV_HOME) + "/.config/market_engine_client"
    #define PATH_DATA_CLIENT                            std::string(ENV_HOME) + "/.local/share/market_engine_client"
    #define DIR_MARKET_ENGINE                           std::string(DIR_HERE) + "/../../../../.."
    #define DIR_MARKET_ENGINE_CLIENT                    std::string(DIR_MARKET_ENGINE) + "/market_engine_client"
    #define DIR_MARKET_ENGINE_APPLICATION               std::string(DIR_MARKET_ENGINE_CLIENT) + "/python/application"
    #define DIR_MARKET_ENGINE_SONAR                     std::string(DIR_MARKET_ENGINE_CLIENT) + "/python/sonar"
    #define DIR_MARKET_ENGINE_CALCULATOR                std::string(DIR_MARKET_ENGINE_CLIENT) + "/cpp/calculator"
    #define DIR_MARKET_ENGINE_GPU_KERNEL_PATH           std::string(DIR_MARKET_ENGINE_CALCULATOR) + "/src/gpu_kernel_embedded"
    #define PATH_CONFIG_CLIENT_TRADEUP_ENGINE       std::string(PATH_CONFIG_CLIENT) + "/tradeup_engine.json"
    #define PATH_DATA_CLIENT_READY_ITEMS                std::string(PATH_DATA_CLIENT) + "/ready_items.json"
    #define PATH_DATA_CLIENT_MODIFIED_ITEMS             std::string(PATH_DATA_CLIENT) + "/modified_items.json"
    #define PATH_DATA_CLIENT_PROFITABLE_TRADEUPS        std::string(PATH_DATA_CLIENT) + "/profitable_tradeups.json"
    #define PATH_DATA_CLIENT_PROFITABLE_TRADEUPS_TEMP   std::string(PATH_DATA_CLIENT) + "/profitable_tradeups.json.temp"
#endif

START_SHARE_NAMESPACE_MULTI(DEFINITIONS)

// GRADE

enum {
    GRADE_CONSUMER = 0, GRADE_INDUSTRIAL, GRADE_MILSPEC, GRADE_RESTRICTED,
    GRADE_CLASSIFIED, GRADE_COVERT, GRADE_CONTRABAND, GRADE_END
};

const std::string GRADE_CONSUMER_STR = "Consumer";
const std::string GRADE_INDUSTRIAL_STR = "Industrial";
const std::string GRADE_MILSPEC_STR = "Milspec";
const std::string GRADE_RESTRICTED_STR = "Restricted";
const std::string GRADE_CLASSIFIED_STR = "Classified";
const std::string GRADE_COVERT_STR = "Covert";
const std::string GRADE_CONTRABAND_STR = "Contraband";

// CATEGORY

enum {CATEGORY_NORMAL = 0, CATEGORY_STAT_TRAK = 1, CATEGORY_SOUVENIR = 2, CATEGORY_END};
const std::string CATEGORY_NORMAL_STR = "Normal";
const std::string CATEGORY_STAT_TRAK_STR = "StatTrak";
const std::string CATEGORY_SOUVENIR_STR = "Souvenir";

// WEAR

enum {
    WEAR_FACTORY_NEW = 0, WEAR_MINIMAL_WEAR = 1, WEAR_FIELD_TESTED = 2, 
    WEAR_WELL_WORN = 3, WEAR_BATTLE_SCARRED = 4, WEAR_END
};
const std::string WEAR_FACTORY_NEW_STR = "Factory New";
const std::string WEAR_MINIMAL_WEAR_STR = "Minimal Wear";
const std::string WEAR_FIELD_TESTED_STR = "Field Tested";
const std::string WEAR_WELL_WORN_STR = "Well Worn";
const std::string WEAR_BATTLE_SCARRED_STR = "Battle Scarred";

const double FLOAT_MIN_FACTORY_NEW = 0.00;
const double FLOAT_MIN_MINIMAL_WEAR = 0.071;
const double FLOAT_MIN_FIELD_TESTED = 0.151;
const double FLOAT_MIN_WELL_WORN = 0.381;
const double FLOAT_MIN_BATTLE_SCARRED = 0.451;

const double FLOAT_MAX_FACTORY_NEW = 0.07;
const double FLOAT_MAX_MINIMAL_WEAR = 0.15;
const double FLOAT_MAX_FIELD_TESTED = 0.38;
const double FLOAT_MAX_WELL_WORN = 0.45;
const double FLOAT_MAX_BATTLE_SCARRED = 1.0;

const double FLOAT_AVG_FACTORY_NEW = 0.035;
const double FLOAT_AVG_MINIMAL_WEAR = 0.11;
const double FLOAT_AVG_FIELD_TESTED = 0.26;
const double FLOAT_AVG_WELL_WORN = 0.41;
const double FLOAT_AVG_BATTLE_SCARRED = 0.725;

// COLLECTIONS

enum {
    COLLECTION_OVERPASS_2024 = 0, COLLECTION_GALLERY, COLLECTION_GRAPHIC_DESIGN, COLLECTION_LIMITED_EDITION_ITEM,
    COLLECTION_SPORT_AND_FIELD, COLLECTION_KILOWATT, COLLECTION_ANUBIS, COLLECTION_REVOLUTION, COLLECTION_RECOIL, COLLECTION_DREAMS_AND_NIGHTMARES,
    COLLECTION_TRAIN_2021, COLLECTION_DUST2_2O21, COLLECTION_MIRAGE_2021, COLLECTION_VERTIGO_2021, COLLECTION_RIPTIDE, COLLECTION_SNAKEBITE,
    COLLECTION_BROKEN_FANG, COLLECTION_CONTROL, COLLECTION_ANCIENT, COLLECTION_HAVOC, COLLECTION_FRACTURE, COLLECTION_PRISMA2,
    COLLECTION_CANALS, COLLECTION_ST_MARC, COLLECTION_NORSE, COLLECTION_SHATTERED_WEB, COLLECTION_CS20, COLLECTION_XRAY,
    COLLECTION_PRISMA, COLLECTION_CLUTCH, COLLECTION_BLACKSITE, COLLECTION_DANGER_ZONE, COLLECTION_NUKE_2018, COLLECTION_INFERNO_2018,
    COLLECTION_HORIZON, COLLECTION_SPECTRUM_2, COLLECTION_HYDRA, COLLECTION_SPECTRUM, COLLECTION_GLOVE, COLLECTION_GAMMA2,
    COLLECTION_GAMMA, COLLECTION_CHROMA3, COLLECTION_WILDFIRE, COLLECTION_REVOLVER_CASE, COLLECTION_SHADOW, COLLECTION_RISING_SUN,
    COLLECTION_GODS_AND_MONSTERS, COLLECTION_CHOP_SHOP, COLLECTION_FALCHION, COLLECTION_CHROMA2, COLLECTION_CHROMA, COLLECTION_VANGUARD,
    COLLECTION_CACHE, COLLECTION_ESPORTS_2014_SUMMER, COLLECTION_BREAKOUT, COLLECTION_BAGGAGE, COLLECTION_OVERPASS, COLLECTION_COBBLESTONE,
    COLLECTION_BANK, COLLECTION_HUNTSMAN, COLLECTION_PHEONIX, COLLECTION_ARMS_DEAL_3, COLLECTION_ESPORTS_2013_WINTER, COLLECTION_WINTER_OFFENSIVE,
    COLLECTION_ITALY, COLLECTION_MIRAGE, COLLECTION_SAFEHOUSE, COLLECTION_DUST2, COLLECTION_LAKE, COLLECTION_TRAIN,
    COLLECTION_ARMS_DEAL_2, COLLECTION_ALPHA, COLLECTION_BRAVO, COLLECTION_ASSAULT, COLLECTION_DUST, COLLECTION_OFFICE,
    COLLECTION_NUKE, COLLECTION_AZTEC, COLLECTION_INFERNO, COLLECTION_ARMS_DEAL, COLLECTION_MILITIA, COLLECTION_VERTIGO,
    COLLECTION_ESPORTS_2013, COLLECTION_TRAIN_2O25, COLLECTION_RADIANT, COLLECTION_BOREAL, COLLECTION_ASCENT, COLLECTION_FEVER, 
    COLLECTION_END
};
const std::string COLLECTION_OVERPASS_2024_STR = "The Overpass 2024 Collection";
const std::string COLLECTION_GALLERY_STR = "The Gallery Collection";
const std::string COLLECTION_GRAPHIC_DESIGN_STR = "The Graphic Design Collection";
const std::string COLLECTION_LIMITED_EDITION_ITEM_STR = "Limited Edition Item";
const std::string COLLECTION_SPORT_AND_FIELD_STR = "The Sport & Field Collection";
const std::string COLLECTION_KILOWATT_STR = "The Kilowatt Collection";
const std::string COLLECTION_ANUBIS_STR = "The Anubis Collection";
const std::string COLLECTION_REVOLUTION_STR = "The Revolution Collection";
const std::string COLLECTION_RECOIL_STR = "The Recoil Collection";
const std::string COLLECTION_DREAMS_AND_NIGHTMARES_STR = "The Dreams & Nightmares Collection";
const std::string COLLECTION_TRAIN_2021_STR = "The 2021 Train Collection";
const std::string COLLECTION_DUST2_2O21_STR = "The 2021 Dust 2 Collection";
const std::string COLLECTION_MIRAGE_2021_STR = "The 2021 Mirage Collection";
const std::string COLLECTION_VERTIGO_2021_STR = "The 2021 Vertigo Collection";
const std::string COLLECTION_RIPTIDE_STR = "The Operation Riptide Collection";
const std::string COLLECTION_SNAKEBITE_STR = "The Snakebite Collection";
const std::string COLLECTION_BROKEN_FANG_STR = "The Operation Broken Fang Collection";
const std::string COLLECTION_CONTROL_STR = "The Control Collection";
const std::string COLLECTION_ANCIENT_STR = "The Ancient Collection";
const std::string COLLECTION_HAVOC_STR = "The Havoc Collection";
const std::string COLLECTION_FRACTURE_STR = "The Fracture Collection";
const std::string COLLECTION_PRISMA2_STR = "The Prisma 2 Collection";
const std::string COLLECTION_CANALS_STR = "The Canals Collection";
const std::string COLLECTION_ST_MARC_STR = "The St. Marc Collection";
const std::string COLLECTION_NORSE_STR = "The Norse Collection";
const std::string COLLECTION_SHATTERED_WEB_STR = "The Shattered Web Collection";
const std::string COLLECTION_CS20_STR = "The CS20 Collection";
const std::string COLLECTION_XRAY_STR = "The X-Ray Collection";
const std::string COLLECTION_PRISMA_STR = "The Prisma Collection";
const std::string COLLECTION_CLUTCH_STR = "The Clutch Collection";
const std::string COLLECTION_BLACKSITE_STR = "The Blacksite Collection";
const std::string COLLECTION_DANGER_ZONE_STR = "The Danger Zone Collection";
const std::string COLLECTION_NUKE_2018_STR = "The 2018 Nuke Collection";
const std::string COLLECTION_INFERNO_2018_STR = "The 2018 Inferno Collection";
const std::string COLLECTION_HORIZON_STR = "The Horizon Collection";
const std::string COLLECTION_SPECTRUM_2_STR = "The Spectrum 2 Collection";
const std::string COLLECTION_HYDRA_STR = "The Operation Hydra Collection";
const std::string COLLECTION_SPECTRUM_STR = "The Spectrum Collection";
const std::string COLLECTION_GLOVE_STR = "The Glove Collection";
const std::string COLLECTION_GAMMA2_STR = "The Gamma 2 Collection";
const std::string COLLECTION_GAMMA_STR = "The Gamma Collection";
const std::string COLLECTION_CHROMA3_STR = "The Chroma 3 Collection";
const std::string COLLECTION_WILDFIRE_STR = "The Wildfire Collection";
const std::string COLLECTION_REVOLVER_CASE_STR = "The Revolver Case Collection";
const std::string COLLECTION_SHADOW_STR = "The Shadow Collection";
const std::string COLLECTION_RISING_SUN_STR = "The Rising Sun Collection";
const std::string COLLECTION_GODS_AND_MONSTERS_STR = "The Gods and Monsters Collection";
const std::string COLLECTION_CHOP_SHOP_STR = "The Chop Shop Collection";
const std::string COLLECTION_FALCHION_STR = "The Falchion Collection";
const std::string COLLECTION_CHROMA2_STR = "The Chroma 2 Collection";
const std::string COLLECTION_CHROMA_STR = "The Chroma Collection";
const std::string COLLECTION_VANGUARD_STR = "The Vanguard Collection";
const std::string COLLECTION_CACHE_STR = "The Cache Collection";
const std::string COLLECTION_ESPORTS_2014_SUMMER_STR = "The eSports 2014 Summer Collection";
const std::string COLLECTION_BREAKOUT_STR = "The Breakout Collection";
const std::string COLLECTION_BAGGAGE_STR = "The Baggage Collection";
const std::string COLLECTION_OVERPASS_STR = "The Overpass Collection";
const std::string COLLECTION_COBBLESTONE_STR = "The Cobblestone Collection";
const std::string COLLECTION_BANK_STR = "The Bank Collection";
const std::string COLLECTION_HUNTSMAN_STR = "The Huntsman Collection";
const std::string COLLECTION_PHEONIX_STR = "The Phoenix Collection";
const std::string COLLECTION_ARMS_DEAL_3_STR = "The Arms Deal 3 Collection";
const std::string COLLECTION_ESPORTS_2013_WINTER_STR = "The eSports 2013 Winter Collection";
const std::string COLLECTION_WINTER_OFFENSIVE_STR = "The Winter Offensive Collection";
const std::string COLLECTION_ITALY_STR = "The Italy Collection";
const std::string COLLECTION_MIRAGE_STR = "The Mirage Collection";
const std::string COLLECTION_SAFEHOUSE_STR = "The Safehouse Collection";
const std::string COLLECTION_DUST2_STR = "The Dust 2 Collection";
const std::string COLLECTION_LAKE_STR = "The Lake Collection";
const std::string COLLECTION_TRAIN_STR = "The Train Collection";
const std::string COLLECTION_ARMS_DEAL_2_STR = "The Arms Deal 2 Collection";
const std::string COLLECTION_ALPHA_STR = "The Alpha Collection";
const std::string COLLECTION_BRAVO_STR = "The Bravo Collection";
const std::string COLLECTION_ASSAULT_STR = "The Assault Collection";
const std::string COLLECTION_DUST_STR = "The Dust Collection";
const std::string COLLECTION_OFFICE_STR = "The Office Collection";
const std::string COLLECTION_NUKE_STR = "The Nuke Collection";
const std::string COLLECTION_AZTEC_STR = "The Aztec Collection";
const std::string COLLECTION_INFERNO_STR = "The Inferno Collection";
const std::string COLLECTION_ARMS_DEAL_STR = "The Arms Deal Collection";
const std::string COLLECTION_MILITIA_STR = "The Militia Collection";
const std::string COLLECTION_VERTIGO_STR = "The Vertigo Collection";
const std::string COLLECTION_ESPORTS_2013_STR = "The eSports 2013 Collection";
const std::string COLLECTION_TRAIN_2O25_STR = "The Train 2025 Collection";
const std::string COLLECTION_RADIANT_STR = "The Radiant Collection";
const std::string COLLECTION_BOREAL_STR = "The Boreal Collection";
const std::string COLLECTION_ASCENT_STR = "The Ascent Collection";
const std::string COLLECTION_FEVER_STR = "The Fever Collection";

// FUNC

std::string gradeToString(const int grade);
std::string categoryToString(const int category);
std::string wearToString(const int wear);
int gradeToInt(const std::string &grade);
int categoryToInt(const std::string &category);
int wearToInt(const std::string &wear);
float wearToMinFloat(const int wear);
float wearToMaxFloat(const int wear);
int floatToWear(const float itemFloat);
std::string collectionToString(const int collection);
int collectionToInt(const std::string &collection);
int getMaxCollectionGrade(const int collection);
float itemFloatValToInt(const float val);

END_SHARE_NAMESPACE