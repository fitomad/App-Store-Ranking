from enum import Enum, unique

#
# Genres codes for App Store
#
@unique
class AppStoreGenre(Enum):
    Business = 6000
    Weather = 6001
    Utilities = 6002
    Travel = 6003
    Sports = 6004
    SocialNetworking = 6005
    Reference = 6006
    Productivity = 6007
    PhotoVideo = 6008
    News = 6009
    Navigation = 6010
    Music = 6011
    Lifestyle = 6012
    Games_HealthFitness = 6013
    Games_Games = 6014
    Games_Games_Action = 7001
    Games_Games_Adventure = 7002
    Games_Arcade = 7003
    Games_Board = 7004
    Games_Card = 7005
    Games_Casino = 7006
    Games_Dice = 7007
    Games_Educational = 7008
    Games_Family = 7009
    Games_Kids = 7010
    Games_Music = 7011
    Games_Puzzle = 7012
    Games_Racing = 7013
    Games_RolePlaying = 7014
    Games_Simulation = 7015
    Games_Sports = 7016
    Games_Strategy = 7017
    Games_Trivia = 7018
    Games_Word = 7019
    Finance = 6015
    Entertainment = 6016
    Education = 6017
    Books = 6018
    Medical = 6020
    Newsstand = 6021
    NewsPolitics = 13001
    FashionStyle = 13002
    HomeGarden = 13003
    OutdoorsNature = 13004
    SportsLeisure = 13005
    Automotive = 13006
    ArtsPhotography = 13007
    BridesWeddings = 13008
    BusinessInvesting = 13009
    ChildrensMagazines = 13010
    ComputersInternet = 13011
    CookingFoodDrink = 13012
    CraftsHobbies = 13013
    ElectronicsAudio = 13014
    #Entertainment = 13015
    HealthMindBody = 13017
    History = 13018
    LiteraryMagazinesJournals = 13019
    MensInterest = 13020
    MoviesMusic = 13021
    ParentingFamily = 13023
    Pets = 13024
    ProfessionalTrade = 13025
    RegionalNews = 13026
    Science = 13027
    Teens = 13028
    TravelRegional = 13029
    WomensInterest = 13030
    Catalogs = 6022

@unique
class MacAppStoreGenre(Enum):
    Business = 2001
    Developer = 12002
    Education = 12003
    Entertainment = 12004
    Finance = 12005
    Games = 12006
    Game_Action = 12201
    Game_Adventure = 12202
    Game_Arcade = 12203
    Game_Board = 12204
    Game_Card = 12205
    Game_Casino = 12206
    Game_Dice = 12207
    Game_Educational = 12208
    Game_Family = 12209
    Game_Kids = 12210
    Game_Music = 12211
    Game_Puzzle = 12212
    Game_Racing = 12213
    Game_RolePlaying = 12214
    Game_Simulation = 12215
    Game_Sports = 12216
    Game_Strategy = 12217
    Game_Trivia = 12218
    Game_Word = 12219
    Health = 2007 
    Lifestyle = 12008
    Medical = 12010
    Music = 12011
    News = 12012
    Photography = 12013
    Productivity = 12014
    Reference = 12015
    Social = 12016
    Sports = 12017
    Travel = 12018
    Utilities = 12019
    Video = 12020
    Weather = 12021
    Design = 12022
