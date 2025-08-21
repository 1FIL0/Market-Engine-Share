#include "definitions.hpp"

USE_NAMESPACE_SHARE

std::string DEFINITIONS::gradeToString(const int grade)
{
    switch(grade) {
        case GRADE_CONSUMER:  return GRADE_CONSUMER_STR; break;
        case GRADE_INDUSTRIAL: return GRADE_INDUSTRIAL_STR; break;
        case GRADE_MILSPEC: return GRADE_MILSPEC_STR; break;
        case GRADE_RESTRICTED: return GRADE_RESTRICTED_STR; break;
        case GRADE_CLASSIFIED: return GRADE_CLASSIFIED_STR; break;
        case GRADE_COVERT: return GRADE_COVERT_STR; break;
        case GRADE_CONTRABAND: return GRADE_CONTRABAND_STR; break;
    }
    return "?";
}

std::string DEFINITIONS::categoryToString(const int category)
{
    switch (category) {
        case CATEGORY_NORMAL: return CATEGORY_NORMAL_STR; break;
        case CATEGORY_STAT_TRAK: return CATEGORY_STAT_TRAK_STR; break;
        case CATEGORY_SOUVENIR: return CATEGORY_SOUVENIR_STR; break;
    }
    return "?";
}

std::string DEFINITIONS::wearToString(const int wear)
{
    switch (wear) {
        case WEAR_FACTORY_NEW: return WEAR_FACTORY_NEW_STR; break;
        case WEAR_MINIMAL_WEAR: return WEAR_MINIMAL_WEAR_STR; break;
        case WEAR_FIELD_TESTED: return WEAR_FIELD_TESTED_STR; break;
        case WEAR_WELL_WORN: return WEAR_WELL_WORN_STR; break;
        case WEAR_BATTLE_SCARRED: return WEAR_BATTLE_SCARRED_STR; break;
    }
    return "?";
}

int DEFINITIONS::gradeToInt(const std::string &grade)
{
    if (grade == GRADE_CONSUMER_STR) {return GRADE_CONSUMER;}
    if (grade == GRADE_INDUSTRIAL_STR) {return GRADE_INDUSTRIAL;}
    if (grade == GRADE_MILSPEC_STR) {return GRADE_MILSPEC;}
    if (grade == GRADE_RESTRICTED_STR) {return GRADE_RESTRICTED;}
    if (grade == GRADE_CLASSIFIED_STR) {return GRADE_CLASSIFIED;}
    if (grade == GRADE_COVERT_STR) {return GRADE_COVERT;}
    if (grade == GRADE_CONTRABAND_STR) {return GRADE_CONTRABAND;}
    return -1;
}

int DEFINITIONS::categoryToInt(const std::string &category)
{
    if (category == CATEGORY_NORMAL_STR) {return CATEGORY_NORMAL;}
    if (category == CATEGORY_STAT_TRAK_STR) {return CATEGORY_STAT_TRAK;}
    if (category == CATEGORY_SOUVENIR_STR) {return CATEGORY_SOUVENIR;}
    return -1;
}

int DEFINITIONS::wearToInt(const std::string &wear)
{
    if (wear == WEAR_FACTORY_NEW_STR) {return WEAR_FACTORY_NEW;}
    if (wear == WEAR_MINIMAL_WEAR_STR) {return WEAR_MINIMAL_WEAR;}
    if (wear == WEAR_FIELD_TESTED_STR) {return WEAR_FIELD_TESTED;}
    if (wear == WEAR_WELL_WORN_STR) {return WEAR_WELL_WORN;}
    if (wear == WEAR_BATTLE_SCARRED_STR) {return WEAR_BATTLE_SCARRED;}
    return -1;
}

std::string DEFINITIONS::collectionToString(const int collection)
{
    switch(collection) {
        case COLLECTION_OVERPASS_2024: {return COLLECTION_OVERPASS_2024_STR; break;}
        case COLLECTION_GALLERY: {return COLLECTION_GALLERY_STR; break;}
        case COLLECTION_GRAPHIC_DESIGN: {return COLLECTION_GRAPHIC_DESIGN_STR; break;}
        case COLLECTION_LIMITED_EDITION_ITEM: {return COLLECTION_LIMITED_EDITION_ITEM_STR; break;}
        case COLLECTION_SPORT_AND_FIELD: {return COLLECTION_SPORT_AND_FIELD_STR; break;}
        case COLLECTION_KILOWATT: {return COLLECTION_KILOWATT_STR; break;}
        case COLLECTION_ANUBIS: {return COLLECTION_ANUBIS_STR; break;}
        case COLLECTION_REVOLUTION: {return COLLECTION_REVOLUTION_STR; break;}
        case COLLECTION_RECOIL: {return COLLECTION_RECOIL_STR; break;}
        case COLLECTION_DREAMS_AND_NIGHTMARES: {return COLLECTION_DREAMS_AND_NIGHTMARES_STR; break;}
        case COLLECTION_TRAIN_2021: {return COLLECTION_TRAIN_2021_STR; break;}
        case COLLECTION_DUST2_2O21: {return COLLECTION_DUST2_2O21_STR; break;}
        case COLLECTION_MIRAGE_2021: {return COLLECTION_MIRAGE_2021_STR; break;}
        case COLLECTION_VERTIGO_2021: {return COLLECTION_VERTIGO_2021_STR; break;}
        case COLLECTION_RIPTIDE: {return COLLECTION_RIPTIDE_STR; break;}
        case COLLECTION_SNAKEBITE: {return COLLECTION_SNAKEBITE_STR; break;}
        case COLLECTION_BROKEN_FANG: {return COLLECTION_BROKEN_FANG_STR; break;}
        case COLLECTION_CONTROL: {return COLLECTION_CONTROL_STR; break;}
        case COLLECTION_ANCIENT: {return COLLECTION_ANCIENT_STR; break;}
        case COLLECTION_HAVOC: {return COLLECTION_HAVOC_STR; break;}
        case COLLECTION_FRACTURE: {return COLLECTION_FRACTURE_STR; break;}
        case COLLECTION_PRISMA2: {return COLLECTION_PRISMA2_STR; break;}
        case COLLECTION_CANALS: {return COLLECTION_CANALS_STR; break;}
        case COLLECTION_ST_MARC: {return COLLECTION_ST_MARC_STR; break;}
        case COLLECTION_NORSE: {return COLLECTION_NORSE_STR; break;}
        case COLLECTION_SHATTERED_WEB: {return COLLECTION_SHATTERED_WEB_STR; break;}
        case COLLECTION_CS20: {return COLLECTION_CS20_STR; break;}
        case COLLECTION_XRAY: {return COLLECTION_XRAY_STR; break;}
        case COLLECTION_PRISMA: {return COLLECTION_PRISMA_STR; break;}
        case COLLECTION_CLUTCH: {return COLLECTION_CLUTCH_STR; break;}
        case COLLECTION_BLACKSITE: {return COLLECTION_BLACKSITE_STR; break;}
        case COLLECTION_DANGER_ZONE: {return COLLECTION_DANGER_ZONE_STR; break;}
        case COLLECTION_NUKE_2018: {return COLLECTION_NUKE_2018_STR; break;}
        case COLLECTION_INFERNO_2018: {return COLLECTION_INFERNO_2018_STR; break;}
        case COLLECTION_HORIZON: {return COLLECTION_HORIZON_STR; break;}
        case COLLECTION_SPECTRUM_2: {return COLLECTION_SPECTRUM_2_STR; break;}
        case COLLECTION_HYDRA: {return COLLECTION_HYDRA_STR; break;}
        case COLLECTION_SPECTRUM: {return COLLECTION_SPECTRUM_STR; break;}
        case COLLECTION_GLOVE: {return COLLECTION_GLOVE_STR; break;}
        case COLLECTION_GAMMA2: {return COLLECTION_GAMMA2_STR; break;}
        case COLLECTION_GAMMA: {return COLLECTION_GAMMA_STR; break;}
        case COLLECTION_CHROMA3: {return COLLECTION_CHROMA3_STR; break;}
        case COLLECTION_WILDFIRE: {return COLLECTION_WILDFIRE_STR; break;}
        case COLLECTION_REVOLVER_CASE: {return COLLECTION_REVOLVER_CASE_STR; break;}
        case COLLECTION_SHADOW: {return COLLECTION_SHADOW_STR; break;}
        case COLLECTION_RISING_SUN: {return COLLECTION_RISING_SUN_STR; break;}
        case COLLECTION_GODS_AND_MONSTERS: {return COLLECTION_GODS_AND_MONSTERS_STR; break;}
        case COLLECTION_CHOP_SHOP: {return COLLECTION_CHOP_SHOP_STR; break;}
        case COLLECTION_FALCHION: {return COLLECTION_FALCHION_STR; break;}
        case COLLECTION_CHROMA2: {return COLLECTION_CHROMA2_STR; break;}
        case COLLECTION_CHROMA: {return COLLECTION_CHROMA_STR; break;}
        case COLLECTION_VANGUARD: {return COLLECTION_VANGUARD_STR; break;}
        case COLLECTION_CACHE: {return COLLECTION_CACHE_STR; break;}
        case COLLECTION_ESPORTS_2014_SUMMER: {return COLLECTION_ESPORTS_2014_SUMMER_STR; break;}
        case COLLECTION_BREAKOUT: {return COLLECTION_BREAKOUT_STR; break;}
        case COLLECTION_BAGGAGE: {return COLLECTION_BAGGAGE_STR; break;}
        case COLLECTION_OVERPASS: {return COLLECTION_OVERPASS_STR; break;}
        case COLLECTION_COBBLESTONE: {return COLLECTION_COBBLESTONE_STR; break;}
        case COLLECTION_BANK: {return COLLECTION_BANK_STR; break;}
        case COLLECTION_HUNTSMAN: {return COLLECTION_HUNTSMAN_STR; break;}
        case COLLECTION_PHEONIX: {return COLLECTION_PHEONIX_STR; break;}
        case COLLECTION_ARMS_DEAL_3: {return COLLECTION_ARMS_DEAL_3_STR; break;}
        case COLLECTION_ESPORTS_2013_WINTER: {return COLLECTION_ESPORTS_2013_WINTER_STR; break;}
        case COLLECTION_WINTER_OFFENSIVE: {return COLLECTION_WINTER_OFFENSIVE_STR; break;}
        case COLLECTION_ITALY: {return COLLECTION_ITALY_STR; break;}
        case COLLECTION_MIRAGE: {return COLLECTION_MIRAGE_STR; break;}
        case COLLECTION_SAFEHOUSE: {return COLLECTION_SAFEHOUSE_STR; break;}
        case COLLECTION_DUST2: {return COLLECTION_DUST2_STR; break;}
        case COLLECTION_LAKE: {return COLLECTION_LAKE_STR; break;}
        case COLLECTION_TRAIN: {return COLLECTION_TRAIN_STR; break;}
        case COLLECTION_ARMS_DEAL_2: {return COLLECTION_ARMS_DEAL_2_STR; break;}
        case COLLECTION_ALPHA: {return COLLECTION_ALPHA_STR; break;}
        case COLLECTION_BRAVO: {return COLLECTION_BRAVO_STR; break;}
        case COLLECTION_ASSAULT: {return COLLECTION_ASSAULT_STR; break;}
        case COLLECTION_DUST: {return COLLECTION_DUST_STR; break;}
        case COLLECTION_OFFICE: {return COLLECTION_OFFICE_STR; break;}
        case COLLECTION_NUKE: {return COLLECTION_NUKE_STR; break;}
        case COLLECTION_AZTEC: {return COLLECTION_AZTEC_STR; break;}
        case COLLECTION_INFERNO: {return COLLECTION_INFERNO_STR; break;}
        case COLLECTION_ARMS_DEAL: {return COLLECTION_ARMS_DEAL_STR; break;}
        case COLLECTION_MILITIA: {return COLLECTION_MILITIA_STR; break;}
        case COLLECTION_VERTIGO: {return COLLECTION_VERTIGO_STR; break;}
        case COLLECTION_ESPORTS_2013: {return COLLECTION_ESPORTS_2013_STR; break;}
        case COLLECTION_TRAIN_2O25: {return COLLECTION_TRAIN_STR; break;}
        case COLLECTION_RADIANT: {return COLLECTION_RADIANT_STR; break;}
        case COLLECTION_BOREAL: {return COLLECTION_BOREAL_STR; break;}
        case COLLECTION_ASCENT: {return COLLECTION_ASCENT_STR; break;}
        case COLLECTION_FEVER: {return COLLECTION_FEVER_STR; break;}
    }
    
    return "?";
}

int DEFINITIONS::collectionToInt(const std::string &collection)
{
    if (collection == COLLECTION_OVERPASS_2024_STR) {return COLLECTION_OVERPASS_2024;}
    if (collection == COLLECTION_GALLERY_STR) {return COLLECTION_GALLERY;}
    if (collection == COLLECTION_GRAPHIC_DESIGN_STR) {return COLLECTION_GRAPHIC_DESIGN;}
    if (collection == COLLECTION_LIMITED_EDITION_ITEM_STR) {return COLLECTION_LIMITED_EDITION_ITEM;}
    if (collection == COLLECTION_SPORT_AND_FIELD_STR) {return COLLECTION_SPORT_AND_FIELD;}
    if (collection == COLLECTION_KILOWATT_STR) {return COLLECTION_KILOWATT;}
    if (collection == COLLECTION_ANUBIS_STR) {return COLLECTION_ANUBIS;}
    if (collection == COLLECTION_REVOLUTION_STR) {return COLLECTION_REVOLUTION;}
    if (collection == COLLECTION_RECOIL_STR) {return COLLECTION_RECOIL;}
    if (collection == COLLECTION_DREAMS_AND_NIGHTMARES_STR) {return COLLECTION_DREAMS_AND_NIGHTMARES;}
    if (collection == COLLECTION_TRAIN_2021_STR) {return COLLECTION_TRAIN_2021;}
    if (collection == COLLECTION_DUST2_2O21_STR) {return COLLECTION_DUST2_2O21;}
    if (collection == COLLECTION_MIRAGE_2021_STR) {return COLLECTION_MIRAGE_2021;}
    if (collection == COLLECTION_VERTIGO_2021_STR) {return COLLECTION_VERTIGO_2021;}
    if (collection == COLLECTION_RIPTIDE_STR) {return COLLECTION_RIPTIDE;}
    if (collection == COLLECTION_SNAKEBITE_STR) {return COLLECTION_SNAKEBITE;}
    if (collection == COLLECTION_BROKEN_FANG_STR) {return COLLECTION_BROKEN_FANG;}
    if (collection == COLLECTION_CONTROL_STR) {return COLLECTION_CONTROL;}
    if (collection == COLLECTION_ANCIENT_STR) {return COLLECTION_ANCIENT;}
    if (collection == COLLECTION_HAVOC_STR) {return COLLECTION_HAVOC;}
    if (collection == COLLECTION_FRACTURE_STR) {return COLLECTION_FRACTURE;}
    if (collection == COLLECTION_PRISMA2_STR) {return COLLECTION_PRISMA2;}
    if (collection == COLLECTION_CANALS_STR) {return COLLECTION_CANALS;}
    if (collection == COLLECTION_ST_MARC_STR) {return COLLECTION_ST_MARC;}
    if (collection == COLLECTION_NORSE_STR) {return COLLECTION_NORSE;}
    if (collection == COLLECTION_SHATTERED_WEB_STR) {return COLLECTION_SHATTERED_WEB;}
    if (collection == COLLECTION_CS20_STR) {return COLLECTION_CS20;}
    if (collection == COLLECTION_XRAY_STR) {return COLLECTION_XRAY;}
    if (collection == COLLECTION_PRISMA_STR) {return COLLECTION_PRISMA;}
    if (collection == COLLECTION_CLUTCH_STR) {return COLLECTION_CLUTCH;}
    if (collection == COLLECTION_BLACKSITE_STR) {return COLLECTION_BLACKSITE;}
    if (collection == COLLECTION_DANGER_ZONE_STR) {return COLLECTION_DANGER_ZONE;}
    if (collection == COLLECTION_NUKE_2018_STR) {return COLLECTION_NUKE_2018;}
    if (collection == COLLECTION_INFERNO_2018_STR) {return COLLECTION_INFERNO_2018;}
    if (collection == COLLECTION_HORIZON_STR) {return COLLECTION_HORIZON;}
    if (collection == COLLECTION_SPECTRUM_2_STR) {return COLLECTION_SPECTRUM_2;}
    if (collection == COLLECTION_HYDRA_STR) {return COLLECTION_HYDRA;}
    if (collection == COLLECTION_SPECTRUM_STR) {return COLLECTION_SPECTRUM;}
    if (collection == COLLECTION_GLOVE_STR) {return COLLECTION_GLOVE;}
    if (collection == COLLECTION_GAMMA2_STR) {return COLLECTION_GAMMA2;}
    if (collection == COLLECTION_GAMMA_STR) {return COLLECTION_GAMMA;}
    if (collection == COLLECTION_CHROMA3_STR) {return COLLECTION_CHROMA3;}
    if (collection == COLLECTION_WILDFIRE_STR) {return COLLECTION_WILDFIRE;}
    if (collection == COLLECTION_REVOLVER_CASE_STR) {return COLLECTION_REVOLVER_CASE;}
    if (collection == COLLECTION_SHADOW_STR) {return COLLECTION_SHADOW;}
    if (collection == COLLECTION_RISING_SUN_STR) {return COLLECTION_RISING_SUN;}
    if (collection == COLLECTION_GODS_AND_MONSTERS_STR) {return COLLECTION_GODS_AND_MONSTERS;}
    if (collection == COLLECTION_CHOP_SHOP_STR) {return COLLECTION_CHOP_SHOP;}
    if (collection == COLLECTION_FALCHION_STR) {return COLLECTION_FALCHION;}
    if (collection == COLLECTION_CHROMA2_STR) {return COLLECTION_CHROMA2;}
    if (collection == COLLECTION_CHROMA_STR) {return COLLECTION_CHROMA;}
    if (collection == COLLECTION_VANGUARD_STR) {return COLLECTION_VANGUARD;}
    if (collection == COLLECTION_CACHE_STR) {return COLLECTION_CACHE;}
    if (collection == COLLECTION_ESPORTS_2014_SUMMER_STR) {return COLLECTION_ESPORTS_2014_SUMMER;}
    if (collection == COLLECTION_BREAKOUT_STR) {return COLLECTION_BREAKOUT;}
    if (collection == COLLECTION_BAGGAGE_STR) {return COLLECTION_BAGGAGE;}
    if (collection == COLLECTION_OVERPASS_STR) {return COLLECTION_OVERPASS;}
    if (collection == COLLECTION_COBBLESTONE_STR) {return COLLECTION_COBBLESTONE;}
    if (collection == COLLECTION_BANK_STR) {return COLLECTION_BANK;}
    if (collection == COLLECTION_HUNTSMAN_STR) {return COLLECTION_HUNTSMAN;}
    if (collection == COLLECTION_PHEONIX_STR) {return COLLECTION_PHEONIX;}
    if (collection == COLLECTION_ARMS_DEAL_3_STR) {return COLLECTION_ARMS_DEAL_3;}
    if (collection == COLLECTION_ESPORTS_2013_WINTER_STR) {return COLLECTION_ESPORTS_2013_WINTER;}
    if (collection == COLLECTION_WINTER_OFFENSIVE_STR) {return COLLECTION_WINTER_OFFENSIVE;}
    if (collection == COLLECTION_ITALY_STR) {return COLLECTION_ITALY;}
    if (collection == COLLECTION_MIRAGE_STR) {return COLLECTION_MIRAGE;}
    if (collection == COLLECTION_SAFEHOUSE_STR) {return COLLECTION_SAFEHOUSE;}
    if (collection == COLLECTION_DUST2_STR) {return COLLECTION_DUST2;}
    if (collection == COLLECTION_LAKE_STR) {return COLLECTION_LAKE;}
    if (collection == COLLECTION_TRAIN_STR) {return COLLECTION_TRAIN;}
    if (collection == COLLECTION_ARMS_DEAL_2_STR) {return COLLECTION_ARMS_DEAL_2;}
    if (collection == COLLECTION_ALPHA_STR) {return COLLECTION_ALPHA;}
    if (collection == COLLECTION_BRAVO_STR) {return COLLECTION_BRAVO;}
    if (collection == COLLECTION_ASSAULT_STR) {return COLLECTION_ASSAULT;}
    if (collection == COLLECTION_DUST_STR) {return COLLECTION_DUST;}
    if (collection == COLLECTION_OFFICE_STR) {return COLLECTION_OFFICE;}
    if (collection == COLLECTION_NUKE_STR) {return COLLECTION_NUKE;}
    if (collection == COLLECTION_AZTEC_STR) {return COLLECTION_AZTEC;}
    if (collection == COLLECTION_INFERNO_STR) {return COLLECTION_INFERNO;}
    if (collection == COLLECTION_ARMS_DEAL_STR) {return COLLECTION_ARMS_DEAL;}
    if (collection == COLLECTION_MILITIA_STR) {return COLLECTION_MILITIA;}
    if (collection == COLLECTION_VERTIGO_STR) {return COLLECTION_VERTIGO;}
    if (collection == COLLECTION_ESPORTS_2013_STR) {return COLLECTION_ESPORTS_2013;}
    if (collection == COLLECTION_TRAIN_2O25_STR) {return COLLECTION_TRAIN_2O25;}
    if (collection == COLLECTION_RADIANT_STR) {return COLLECTION_RADIANT;}
    if (collection == COLLECTION_BOREAL_STR) {return COLLECTION_BOREAL;}
    if (collection == COLLECTION_ASCENT_STR) {return COLLECTION_ASCENT;}
    if (collection == COLLECTION_FEVER_STR) {return COLLECTION_FEVER;}
    return -1;
}

int DEFINITIONS::getMaxCollectionGrade(const int collection)
{
    switch (collection) {
        case COLLECTION_OVERPASS_2024: {return GRADE_COVERT; break;}
        case COLLECTION_GALLERY: {return GRADE_COVERT; break;}
        case COLLECTION_GRAPHIC_DESIGN: {return GRADE_COVERT; break;}
        case COLLECTION_LIMITED_EDITION_ITEM: {return GRADE_CLASSIFIED; break;}
        case COLLECTION_SPORT_AND_FIELD: {return GRADE_COVERT; break;}
        case COLLECTION_KILOWATT: {return GRADE_COVERT; break;}
        case COLLECTION_ANUBIS: {return GRADE_COVERT; break;}
        case COLLECTION_REVOLUTION: {return GRADE_COVERT; break;}
        case COLLECTION_RECOIL: {return GRADE_COVERT; break;}
        case COLLECTION_DREAMS_AND_NIGHTMARES: {return GRADE_COVERT; break;}
        case COLLECTION_TRAIN_2021: {return GRADE_COVERT; break;}
        case COLLECTION_DUST2_2O21: {return GRADE_COVERT; break;}
        case COLLECTION_MIRAGE_2021: {return GRADE_COVERT; break;}
        case COLLECTION_VERTIGO_2021: {return GRADE_COVERT; break;}
        case COLLECTION_RIPTIDE: {return GRADE_COVERT; break;}
        case COLLECTION_SNAKEBITE: {return GRADE_COVERT; break;}
        case COLLECTION_BROKEN_FANG: {return GRADE_COVERT; break;}
        case COLLECTION_CONTROL: {return GRADE_COVERT; break;}
        case COLLECTION_ANCIENT: {return GRADE_COVERT; break;}
        case COLLECTION_HAVOC: {return GRADE_COVERT; break;}
        case COLLECTION_FRACTURE: {return GRADE_COVERT; break;}
        case COLLECTION_PRISMA2: {return GRADE_COVERT; break;}
        case COLLECTION_CANALS: {return GRADE_COVERT; break;}
        case COLLECTION_ST_MARC: {return GRADE_COVERT; break;}
        case COLLECTION_NORSE: {return GRADE_COVERT; break;}
        case COLLECTION_SHATTERED_WEB: {return GRADE_COVERT ; break;}
        case COLLECTION_CS20: {return GRADE_COVERT; break;}
        case COLLECTION_XRAY: {return GRADE_RESTRICTED; break;}
        case COLLECTION_PRISMA: {return GRADE_COVERT; break;}
        case COLLECTION_CLUTCH: {return GRADE_COVERT; break;}
        case COLLECTION_BLACKSITE: {return GRADE_RESTRICTED; break;}
        case COLLECTION_DANGER_ZONE: {return GRADE_COVERT; break;}
        case COLLECTION_NUKE_2018: {return GRADE_CLASSIFIED; break;}
        case COLLECTION_INFERNO_2018: {return GRADE_CLASSIFIED; break;}
        case COLLECTION_HORIZON: {return GRADE_COVERT; break;}
        case COLLECTION_SPECTRUM_2: {return GRADE_COVERT; break;}
        case COLLECTION_HYDRA: {return GRADE_COVERT; break;}
        case COLLECTION_SPECTRUM: {return GRADE_COVERT; break;}
        case COLLECTION_GLOVE: {return GRADE_COVERT; break;}
        case COLLECTION_GAMMA2: {return GRADE_COVERT; break;}
        case COLLECTION_GAMMA: {return GRADE_COVERT; break;}
        case COLLECTION_CHROMA3: {return GRADE_COVERT; break;}
        case COLLECTION_WILDFIRE: {return GRADE_COVERT; break;}
        case COLLECTION_REVOLVER_CASE: {return GRADE_COVERT; break;}
        case COLLECTION_SHADOW: {return GRADE_COVERT; break;}
        case COLLECTION_RISING_SUN: {return GRADE_COVERT; break;}
        case COLLECTION_GODS_AND_MONSTERS: {return GRADE_COVERT; break;}
        case COLLECTION_CHOP_SHOP: {return GRADE_CLASSIFIED; break;}
        case COLLECTION_FALCHION: {return GRADE_COVERT; break;}
        case COLLECTION_CHROMA2: {return GRADE_COVERT; break;}
        case COLLECTION_CHROMA: {return GRADE_COVERT; break;}
        case COLLECTION_VANGUARD: {return GRADE_COVERT; break;}
        case COLLECTION_CACHE: {return GRADE_RESTRICTED; break;}
        case COLLECTION_ESPORTS_2014_SUMMER: {return GRADE_COVERT; break;}
        case COLLECTION_BREAKOUT: {return GRADE_COVERT; break;}
        case COLLECTION_BAGGAGE: {return GRADE_CLASSIFIED; break;}
        case COLLECTION_OVERPASS: {return GRADE_CLASSIFIED; break;}
        case COLLECTION_COBBLESTONE: {return GRADE_COVERT; break;}
        case COLLECTION_BANK: {return GRADE_CLASSIFIED; break;}
        case COLLECTION_HUNTSMAN: {return GRADE_COVERT; break;}
        case COLLECTION_PHEONIX: {return GRADE_COVERT; break;}
        case COLLECTION_ARMS_DEAL_3: {return GRADE_COVERT; break;}
        case COLLECTION_ESPORTS_2013_WINTER: {return GRADE_COVERT; break;}
        case COLLECTION_WINTER_OFFENSIVE: {return GRADE_COVERT; break;}
        case COLLECTION_ITALY: {return GRADE_RESTRICTED; break;}
        case COLLECTION_MIRAGE: {return GRADE_RESTRICTED; break;}
        case COLLECTION_SAFEHOUSE: {return GRADE_RESTRICTED; break;}
        case COLLECTION_DUST2: {return GRADE_CLASSIFIED; break;}
        case COLLECTION_LAKE: {return GRADE_RESTRICTED; break;}
        case COLLECTION_TRAIN: {return GRADE_RESTRICTED; break;}
        case COLLECTION_ARMS_DEAL_2: {return GRADE_COVERT; break;}
        case COLLECTION_ALPHA: {return GRADE_RESTRICTED; break;}
        case COLLECTION_BRAVO: {return GRADE_COVERT; break;}
        case COLLECTION_ASSAULT: {return GRADE_RESTRICTED; break;}
        case COLLECTION_DUST: {return GRADE_RESTRICTED; break;}
        case COLLECTION_OFFICE: {return GRADE_MILSPEC; break;}
        case COLLECTION_NUKE: {return GRADE_RESTRICTED; break;}
        case COLLECTION_AZTEC: {return GRADE_MILSPEC; break;}
        case COLLECTION_INFERNO: {return GRADE_MILSPEC; break;}
        case COLLECTION_ARMS_DEAL: {return GRADE_COVERT; break;}
        case COLLECTION_MILITIA: {return GRADE_CLASSIFIED; break;}
        case COLLECTION_VERTIGO: {return GRADE_RESTRICTED; break;}
        case COLLECTION_ESPORTS_2013: {return GRADE_COVERT; break;}
        case COLLECTION_TRAIN_2O25: {return GRADE_COVERT; break;}
        case COLLECTION_RADIANT: {return GRADE_CLASSIFIED; break;}
        case COLLECTION_BOREAL: { return GRADE_CLASSIFIED; break;}
        case COLLECTION_ASCENT: { return GRADE_CLASSIFIED; break;}
        case COLLECTION_FEVER: {return GRADE_COVERT; break;}
    }
    return -1;
}

float DEFINITIONS::wearToMinFloat(const int wear)
{
    if (wear == WEAR_FACTORY_NEW) {return FLOAT_MIN_FACTORY_NEW;}
    if (wear == WEAR_MINIMAL_WEAR) {return FLOAT_MIN_MINIMAL_WEAR;}
    if (wear == WEAR_FIELD_TESTED) {return FLOAT_MIN_FIELD_TESTED;}
    if (wear == WEAR_WELL_WORN) {return FLOAT_MIN_WELL_WORN;}
    if (wear == WEAR_BATTLE_SCARRED) {return FLOAT_MIN_BATTLE_SCARRED;}
    return -1.0;
}

float DEFINITIONS::wearToMaxFloat(const int wear)
{
    if (wear == WEAR_FACTORY_NEW) {return FLOAT_MAX_FACTORY_NEW;}
    if (wear == WEAR_MINIMAL_WEAR) {return FLOAT_MAX_MINIMAL_WEAR;}
    if (wear == WEAR_FIELD_TESTED) {return FLOAT_MAX_FIELD_TESTED;}
    if (wear == WEAR_WELL_WORN) {return FLOAT_MAX_WELL_WORN;}
    if (wear == WEAR_BATTLE_SCARRED) {return FLOAT_MAX_BATTLE_SCARRED;}
    return -1.0;
}

int DEFINITIONS::floatToWear(const float itemFloat)
{
    if (itemFloat >= FLOAT_MIN_FACTORY_NEW && itemFloat <= FLOAT_MAX_FACTORY_NEW) {return WEAR_FACTORY_NEW;}
    if (itemFloat >= FLOAT_MIN_MINIMAL_WEAR && itemFloat <= FLOAT_MAX_MINIMAL_WEAR) {return WEAR_MINIMAL_WEAR;}
    if (itemFloat >= FLOAT_MIN_FIELD_TESTED && itemFloat <= FLOAT_MAX_FIELD_TESTED) {return WEAR_FIELD_TESTED;}
    if (itemFloat >= FLOAT_MIN_WELL_WORN && itemFloat <= FLOAT_MAX_WELL_WORN) {return WEAR_WELL_WORN;}
    if (itemFloat >= FLOAT_MIN_BATTLE_SCARRED && itemFloat <= FLOAT_MAX_BATTLE_SCARRED) {return WEAR_BATTLE_SCARRED;}
    return -1.0;
}

float DEFINITIONS::itemFloatValToInt(const float val)
{
    if (val >= 0.0 && val <= FLOAT_MAX_FACTORY_NEW) {return WEAR_FACTORY_NEW;}
    if (val >= 0.0 && val <= FLOAT_MAX_MINIMAL_WEAR) {return WEAR_MINIMAL_WEAR;}
    if (val >= 0.0 && val <= FLOAT_MAX_FIELD_TESTED) {return WEAR_FIELD_TESTED;}
    if (val >= 0.0 && val <= FLOAT_MAX_WELL_WORN) {return WEAR_WELL_WORN;}
    if (val >= 0.0 && val <= FLOAT_MAX_BATTLE_SCARRED) {return WEAR_BATTLE_SCARRED;}
    return -1.0;
}
