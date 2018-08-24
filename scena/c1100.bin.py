from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1100.bin",                # FileName
        "c1100",                    # MapName
        "c1100",                    # Location
        0x0016,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("c1100", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x06',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 4210, 2500, 8930, 0, 0, 1, 22, 0, 7, 0, 8],
    )

    BuildStringList((
        "c1100",                  # 0
        "Chroma",                 # 1
        "Otto",                   # 2
        "Tajik",                  # 3
        "Patrol Officer Frantz",  # 4
        "Zeit",                   # 5
        "Tourist",                # 6
        "Tourist",                # 7
        "Citizen",                # 8
        "Boy",                    # 9
        "Citizen",                # 10
        "Citizen",                # 11
        "Haas",                   # 12
        "State Guard Soldier",    # 13
        "State Guard Soldier",    # 14
        "Citizen",                # 15
        "Citizen",                # 16
        "Citizen",                # 17
        "Citizen",                # 18
        "Citizen",                # 19
        "Citizen",                # 20
        "Policeman",              # 21
        "Policeman",              # 22
        "Policeman",              # 23
        "Citizen",                # 24
        "Tourist",                # 25
        "Tourist",                # 26
        "Momo",                   # 27
        "Ryｹ",                   # 28
        "Henri",                  # 29
        "Magic Soldier",          # 30
        "Magic Soldier",          # 31
        "Bracer Scott",           # 32
        "Bracer Wenzel",          # 33
        "Bracer Ling",            # 34
        "Bracer Eolia",           # 35
        "イベント用モンスター",   # 36
        "イベント用モンスター",   # 37
        "イベント用モンスター",   # 38
        "Patrol Officer Kate",    # 39
        "Yuri",                   # 40
        "Sykes",                  # 41
        "Reggie",                 # 42
        "Patrol Car",             # 43
        "Patrol Car",             # 44
        "Patrol Car",             # 45
        "Patrol Car",             # 46
        "暴走車",                 # 47
        "車",                     # 48
        "土嚢",                   # 49
        "市民１",                 # 50
        "市民２",                 # 51
        "市民３",                 # 52
        "市民４",                 # 53
        "市民５",                 # 54
        "市民６",                 # 55
        "市民７",                 # 56
        "市民８",                 # 57
        "Policeman",              # 58
        "Policeman",              # 59
        "Policeman",              # 60
        "Policeman",              # 61
        "Policeman",              # 62
        "SE制御",                 # 63
        "bc1100",                 # 64
        "Central Square",         # 65
        "West Street",            # 66
        "Governmental District",  # 67
        "Residential Street",     # 68
        "Entertainment District", # 69
        "East Street",            # 70
        "Downtown",               # 71
        "Waterfront Area",        # 72
        "IBC",                    # 73
        "Station Street",         # 74
        "Back Street",            # 75
        "St. Ursula Byroad",      # 76
        "East Crossbell Highway", # 77
        "West Crossbell HIghway", # 78
        "Mainz Mountain Road",    # 79
        "Orchis Tower",           # 80
    ))

    ATBonus("ATBonus_BF0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_CCA3", 8,   8,   8,   8,   11,  11,  11)

    MonsterBattlePostion("MonsterBattlePostion_C40", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_C44", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_C48", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_C50", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_C54", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_C58", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_C5C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_CA0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_CA4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_CA8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_CAC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_CB0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_CB4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_CB8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_CBC", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_C20", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_C24", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_C28", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_C2C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_C30", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_C34", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_C38", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_C3C", 2, 13, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_CC0", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc1100", "Sepith_CCA3", 60, 30, 10, 0,
        (
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C40", "MonsterBattlePostion_CA0", "ed7450", "ed7453", "ATBonus_BF0"),
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C20", "MonsterBattlePostion_CA0", "ed7450", "ed7453", "ATBonus_BF0"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_C40", "MonsterBattlePostion_CA0", "ed7450", "ed7453", "ATBonus_BF0"),
            (),
        )
    )

    AddCharChip((
        "chr/ch24900.itc",                   # 00
        "chr/ch20800.itc",                   # 01
        "chr/ch28100.itc",                   # 02
        "chr/ch30000.itc",                   # 03
        "chr/ch02707.itc",                   # 04
        "chr/ch24400.itc",                   # 05
        "chr/ch22100.itc",                   # 06
        "chr/ch21000.itc",                   # 07
        "chr/ch23800.itc",                   # 08
        "chr/ch20400.itc",                   # 09
        "chr/ch21300.itc",                   # 0A
        "chr/ch21002.itc",                   # 0B
        "chr/ch26000.itc",                   # 0C
        "chr/ch41400.itc",                   # 0D
        "chr/ch41500.itc",                   # 0E
        "chr/ch20000.itc",                   # 0F
        "monster/ch85150.itc",               # 10
        "monster/ch85151.itc",               # 11
        "chr/ch23300.itc",                   # 12
        "chr/ch21800.itc",                   # 13
        "chr/ch22700.itc",                   # 14
        "chr/ch21400.itc",                   # 15
        "chr/ch49400.itc",                   # 16
        "chr/ch48700.itc",                   # 17
        "chr/ch20700.itc",                   # 18
        "chr/ch20600.itc",                   # 19
        "chr/ch22200.itc",                   # 1A
        "chr/ch32300.itc",                   # 1B
        "chr/ch44200.itc",                   # 1C
    ))

    DeclNpc(6929,    2490,    4294960646, 225,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(8369,    2390,    4294952446, 90,   257,  0x0, 0,   1,   0,   0,   2,   0,   10,  255,  0)
    DeclNpc(4294958557, 2500,    6070,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294952246, 2500,    27399,   180,  389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(24299,   2500,    4294956687, 225,  405,  0x0, 0,   4,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(4294965956, 2390,    9340,    0,    389,  0x0, 0,   5,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(4294964957, 2390,    9340,    0,    389,  0x0, 0,   6,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(4294950337, 2500,    4294967167, 270,  389,  0x0, 0,   7,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(4294948737, 2500,    4294967077, 45,   385,  0x0, 0,   8,   0,   0,   4,   0,   29,  255,  0)
    DeclNpc(7389,    2500,    4294959116, 135,  389,  0x0, 0,   9,   0,   0,   0,   0,   30,  255,  0)
    DeclNpc(8489,    2390,    4294958616, 315,  389,  0x0, 0,   10,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(4294958906, 2390,    9329,    225,  389,  0x0, 0,   12,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(14510,   2410,    11399,   270,  389,  0x0, 0,   13,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(14670,   2500,    4420,    270,  389,  0x0, 0,   14,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(13210,   2500,    5900,    90,   389,  0x0, 0,   15,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(12989,   2500,    3599,    45,   389,  0x0, 0,   18,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(12050,   2500,    6840,    90,   389,  0x0, 0,   19,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(11510,   2410,    9470,    180,  389,  0x0, 0,   20,  0,   0,   0,   0,   37,  255,  0)
    DeclNpc(9710,    2410,    9939,    90,   389,  0x0, 0,   21,  0,   0,   0,   0,   38,  255,  0)
    DeclNpc(1500,    2500,    4294964096, 270,  389,  0x0, 0,   23,  0,   0,   0,   0,   39,  255,  0)
    DeclNpc(4294952246, 2500,    27399,   180,  385,  0x0, 0,   3,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(21909,   2500,    1659,    180,  385,  0x0, 0,   3,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(21530,   0,       4294918637, 0,    385,  0x0, 0,   3,   0,   0,   1,   0,   20,  255,  0)
    DeclNpc(4294962146, 2500,    26469,   45,   385,  0x0, 0,   19,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4294963457, 2500,    26950,   0,    385,  0x0, 0,   27,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294964336, 2500,    26680,   315,  385,  0x0, 0,   28,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4294961137, 2500,    27180,   0,    389,  0x0, 0,   24,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(4294961546, 2500,    28309,   0,    389,  0x0, 0,   25,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(4294960396, 2500,    28020,   90,   389,  0x0, 0,   26,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(4294962507, 2500,    34500,   180,  389,  0x0, 0,   16,  0,   0,   5,   255, 255, 255,  0)
    DeclNpc(4294959726, 2500,    34500,   180,  389,  0x0, 0,   16,  0,   0,   5,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(8740,    8280,    2490,    0x101010E,    "BattleInfo_CC0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294949736, 9920,    2500,    0x10100E1,    "BattleInfo_CC0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(14710,   4294954026, 2390,    0x10100E1,    "BattleInfo_CC0", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0040, 0, 40,  11.420000076293945,    7.010000228881836,     0.0,                   36.0,                  [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.9516667127609253,   -0.5841667056083679,   -0.0,                  1.0])
    DeclEvent(0x0040, 0, 68,  -6.340000152587891,    30.489999771118164,    2.5,                   25.0,                  [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.6340000033378601,    -3.0490000247955322,   -0.5,                  1.0])

    DeclActor(4294961756, 2500,    32280,   2000,    4294961756, 4000,    32280,   0x007C, 0,  66, 0x0000)
    DeclActor(16550,   2410,    10660,   1200,    16550,   3910,    10660,   0x007C, 0,  69, 0x0000)
    DeclActor(4294949316, 2500,    30520,   1200,    4294949316, 3700,    30520,   0x007C, 0,  70, 0x0000)

    PlaceName(-31.530000686645508, 0.0, -107.9000015258789, 0x0000, 0x0000, "Central Square")
    PlaceName(-117.0, 0.0, -102.05000305175781, 0x0000, 0x0000, "West Street")
    PlaceName(3.5799999237060547, 0.0, 7.800000190734863, 0x0000, 0x0000, "Governmental District")
    PlaceName(-196.3000030517578, 0.0, -5.199999809265137, 0x0000, 0x0000, "Residential Street")
    PlaceName(-101.4000015258789, 0.0, -15.600000381469727, 0x0000, 0x0000, "Entertainment District")
    PlaceName(74.0999984741211, 0.0, -137.8000030517578, 0x0000, 0x0000, "East Street")
    PlaceName(120.25, 0.0, -209.3000030517578, 0x0000, 0x0000, "Downtown")
    PlaceName(110.5, 0.0, -52.0, 0x0000, 0x0000, "Waterfront Area")
    PlaceName(76.69999694824219, 0.0, 70.19999694824219, 0x0000, 0x0000, "IBC")
    PlaceName(-16.899999618530273, 0.0, -197.60000610351562, 0x0000, 0x0000, "Station Street")
    PlaceName(-78.0, 0.0, -62.400001525878906, 0x0000, 0x0000, "Back Street")
    PlaceName(-20.799999237060547, 0.0, -237.89999389648438, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(144.3000030517578, 0.0, -119.5999984741211, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-183.3000030517578, 0.0, -104.0, 0x0000, 0x0000, "West Crossbell HIghway")
    PlaceName(-175.5, 0.0, 26.0, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(-5.0, 0.0, 178.0, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(-60.130001068115234, 0.0, -126.0999984741211, 0x0000, 0x0051, "")
    PlaceName(9.75, 0.0, -92.30000305175781, 0x0000, 0x0054, "")
    PlaceName(-28.280000686645508, 0.0, -136.5, 0x0000, 0x0057, "")
    PlaceName(-61.099998474121094, 0.0, -88.4000015258789, 0x0000, 0x0053, "")
    PlaceName(-34.45000076293945, 0.0, -57.20000076293945, 0x0000, 0x0053, "")
    PlaceName(-100.43000030517578, 0.0, -94.9000015258789, 0x0000, 0x0053, "")
    PlaceName(-113.0999984741211, 0.0, -67.5999984741211, 0x0000, 0x0053, "")
    PlaceName(-81.9000015258789, 0.0, -26.0, 0x0000, 0x0052, "")
    PlaceName(-75.7300033569336, 0.0, -42.900001525878906, 0x0000, 0x0053, "")
    PlaceName(-64.3499984741211, 0.0, -53.95000076293945, 0x0000, 0x0053, "")
    PlaceName(-27.299999237060547, 0.0, 38.349998474121094, 0x0000, 0x0051, "")
    PlaceName(118.30000305175781, 0.0, -137.8000030517578, 0x0000, 0x0052, "")
    PlaceName(96.19999694824219, 0.0, -255.4499969482422, 0x0000, 0x0053, "")
    PlaceName(79.30000305175781, 0.0, -231.39999389648438, 0x0000, 0x0053, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_E90",          # 00, 0
        "Function_1_F48",          # 01, 1
        "Function_2_F95",          # 02, 2
        "Function_3_106E",         # 03, 3
        "Function_4_1099",         # 04, 4
        "Function_5_10C4",         # 05, 5
        "Function_6_10E3",         # 06, 6
        "Function_7_11C8",         # 07, 7
        "Function_8_193F",         # 08, 8
        "Function_9_21E6",         # 09, 9
        "Function_10_3261",        # 0A, 10
        "Function_11_4284",        # 0B, 11
        "Function_12_44AB",        # 0C, 12
        "Function_13_5527",        # 0D, 13
        "Function_14_5856",        # 0E, 14
        "Function_15_5CE9",        # 0F, 15
        "Function_16_5CF3",        # 10, 16
        "Function_17_5CFD",        # 11, 17
        "Function_18_5D07",        # 12, 18
        "Function_19_6223",        # 13, 19
        "Function_20_6685",        # 14, 20
        "Function_21_68AD",        # 15, 21
        "Function_22_6991",        # 16, 22
        "Function_23_6A89",        # 17, 23
        "Function_24_6B9E",        # 18, 24
        "Function_25_6C63",        # 19, 25
        "Function_26_6CC0",        # 1A, 26
        "Function_27_6DD5",        # 1B, 27
        "Function_28_6ED4",        # 1C, 28
        "Function_29_75DB",        # 1D, 29
        "Function_30_7901",        # 1E, 30
        "Function_31_7A25",        # 1F, 31
        "Function_32_7B25",        # 20, 32
        "Function_33_7BAD",        # 21, 33
        "Function_34_7C08",        # 22, 34
        "Function_35_7C8D",        # 23, 35
        "Function_36_7CCE",        # 24, 36
        "Function_37_7D1A",        # 25, 37
        "Function_38_7D82",        # 26, 38
        "Function_39_7DAE",        # 27, 39
        "Function_40_7F41",        # 28, 40
        "Function_41_8855",        # 29, 41
        "Function_42_901C",        # 2A, 42
        "Function_43_9380",        # 2B, 43
        "Function_44_93C6",        # 2C, 44
        "Function_45_98A2",        # 2D, 45
        "Function_46_9959",        # 2E, 46
        "Function_47_999E",        # 2F, 47
        "Function_48_99D9",        # 30, 48
        "Function_49_A0A2",        # 31, 49
        "Function_50_A162",        # 32, 50
        "Function_51_A23C",        # 33, 51
        "Function_52_A26B",        # 34, 52
        "Function_53_A294",        # 35, 53
        "Function_54_A3A7",        # 36, 54
        "Function_55_A4A3",        # 37, 55
        "Function_56_A5C3",        # 38, 56
        "Function_57_A628",        # 39, 57
        "Function_58_A657",        # 3A, 58
        "Function_59_A67C",        # 3B, 59
        "Function_60_A706",        # 3C, 60
        "Function_61_B1BC",        # 3D, 61
        "Function_62_B2DC",        # 3E, 62
        "Function_63_B33B",        # 3F, 63
        "Function_64_B36B",        # 40, 64
        "Function_65_B39B",        # 41, 65
        "Function_66_C1D3",        # 42, 66
        "Function_67_C239",        # 43, 67
        "Function_68_C2ED",        # 44, 68
        "Function_69_C585",        # 45, 69
        "Function_70_CAF6",        # 46, 70
    ))


    def Function_0_E90(): pass

    label("Function_0_E90")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_ED0"),
        (1, "loc_EDC"),
        (2, "loc_EE8"),
        (3, "loc_EF4"),
        (4, "loc_F00"),
        (5, "loc_F0C"),
        (6, "loc_F18"),
        (SWITCH_DEFAULT, "loc_F24"),
    )


    label("loc_ED0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_F30")

    label("loc_EDC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_F30")

    label("loc_EE8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_F30")

    label("loc_EF4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_F30")

    label("loc_F00")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_F30")

    label("loc_F0C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_F30")

    label("loc_F18")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_F30")

    label("loc_F24")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_F30")

    label("loc_F30")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F47")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_F30")

    label("loc_F47")

    Return()

    # Function_0_E90 end

    def Function_1_F48(): pass

    label("Function_1_F48")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F94")
    OP_95(0xFE, 20950, 2490, -3000, 2000, 0x0)
    OP_95(0xFE, 44000, 2490, -2580, 2000, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 21530, 0, -48660, 0)
    Jump("Function_1_F48")

    label("loc_F94")

    Return()

    # Function_1_F48 end

    def Function_2_F95(): pass

    label("Function_2_F95")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_106D")
    OP_95(0xFE, 17250, 2500, -14850, 1000, 0x0)
    OP_95(0xFE, 17250, 2500, -70, 1000, 0x0)
    OP_95(0xFE, 3810, 2500, 8270, 1000, 0x0)
    OP_95(0xFE, -6210, 2500, 23860, 1000, 0x0)
    OP_95(0xFE, -18440, 2500, 23260, 1000, 0x0)
    OP_95(0xFE, -20840, 2450, 19170, 1000, 0x0)
    OP_95(0xFE, -18240, 2500, 6490, 1000, 0x0)
    OP_95(0xFE, -18430, 2500, -3620, 1000, 0x0)
    OP_95(0xFE, -7420, 2500, -14630, 1000, 0x0)
    OP_95(0xFE, 8370, 2390, -14850, 1000, 0x0)
    Jump("Function_2_F95")

    label("loc_106D")

    Return()

    # Function_2_F95 end

    def Function_3_106E(): pass

    label("Function_3_106E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1098")
    OP_94(0xFE, 0x1F72, 0xFFFFEAD4, 0x109A, 0xFFFFD8AA, 0x7D0)
    Sleep(200)
    Jump("Function_3_106E")

    label("loc_1098")

    Return()

    # Function_3_106E end

    def Function_4_1099(): pass

    label("Function_4_1099")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10C3")
    OP_94(0xFE, 0xFFFFB2BC, 0x8CA, 0xFFFFBAC8, 0xFFFFF204, 0x3E8)
    Sleep(300)
    Jump("Function_4_1099")

    label("loc_10C3")

    Return()

    # Function_4_1099 end

    def Function_5_10C4(): pass

    label("Function_5_10C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10E2")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_5_10C4")

    label("loc_10E2")

    Return()

    # Function_5_10C4 end

    def Function_6_10E3(): pass

    label("Function_6_10E3")

    SetMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0xF, 0x2000000)
    SetMapObjFlags(0x10, 0x2000000)
    SetMapObjFlags(0x13, 0x2000000)
    SetMapObjFlags(0x14, 0x2000000)
    SetMapObjFlags(0x15, 0x2000000)
    SetMapObjFlags(0x16, 0x2000000)
    SetMapObjFlags(0x17, 0x2000000)
    SetMapObjFlags(0x18, 0x2000000)
    SetMapObjFlags(0x19, 0x2000000)
    SetMapObjFlags(0x1A, 0x2000000)
    SetMapObjFlags(0x1B, 0x2000000)
    SetMapObjFlags(0x1C, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_11A6")
    SetMapObjFlags(0x5, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0x12, 0x2000000)
    ClearMapObjFlags(0xF, 0x2000000)
    ClearMapObjFlags(0x10, 0x2000000)
    ClearMapObjFlags(0x13, 0x2000000)
    ClearMapObjFlags(0x14, 0x2000000)
    ClearMapObjFlags(0x15, 0x2000000)
    ClearMapObjFlags(0x16, 0x2000000)
    ClearMapObjFlags(0x17, 0x2000000)
    ClearMapObjFlags(0x18, 0x2000000)
    ClearMapObjFlags(0x19, 0x2000000)
    ClearMapObjFlags(0x1A, 0x2000000)
    ClearMapObjFlags(0x1B, 0x2000000)
    ClearMapObjFlags(0x1C, 0x2000000)

    label("loc_11A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_11C7")
    ClearMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)

    label("loc_11C7")

    Return()

    # Function_6_10E3 end

    def Function_7_11C8(): pass

    label("Function_7_11C8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AE")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1293")
    SetChrPos(0x0, 30170, 2500, -90, 270)
    SetChrPos(0x1, 30170, 2500, -90, 270)
    SetChrPos(0x2, 30170, 2500, -90, 270)
    SetChrPos(0x3, 30170, 2500, -90, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1266")
    SetChrPos(0x4, 30170, 2500, -90, 270)
    SetChrPos(0x5, 30170, 2500, -90, 270)
    Jump("loc_1285")

    label("loc_1266")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1285")
    SetChrPos(0x4, 30170, 2500, -90, 270)

    label("loc_1285")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14AE")

    label("loc_1293")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1359")
    SetChrPos(0x0, -40390, 0, 24150, 90)
    SetChrPos(0x1, -40390, 0, 24150, 90)
    SetChrPos(0x2, -40390, 0, 24150, 90)
    SetChrPos(0x3, -40390, 0, 24150, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_132C")
    SetChrPos(0x4, -40390, 0, 24150, 90)
    SetChrPos(0x5, -40390, 0, 24150, 90)
    Jump("loc_134B")

    label("loc_132C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_134B")
    SetChrPos(0x4, -40390, 0, 24150, 90)

    label("loc_134B")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14AE")

    label("loc_1359")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_140D")
    SetChrPos(0x0, -5400, 2500, 35000, 180)
    SetChrPos(0x1, -5400, 2500, 35000, 180)
    SetChrPos(0x2, -5400, 2500, 35000, 180)
    SetChrPos(0x3, -5400, 2500, 35000, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13E0")
    SetChrPos(0x4, -5400, 2500, 35000, 180)
    SetChrPos(0x5, -5400, 2500, 35000, 180)
    Jump("loc_13FF")

    label("loc_13E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13FF")
    SetChrPos(0x4, -5400, 2500, 35000, 180)

    label("loc_13FF")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14AE")

    label("loc_140D")

    SetChrPos(0x0, 19940, 0, -37920, 0)
    SetChrPos(0x1, 19940, 0, -37920, 0)
    SetChrPos(0x2, 19940, 0, -37920, 0)
    SetChrPos(0x3, 19940, 0, -37920, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1486")
    SetChrPos(0x4, 19940, 0, -37920, 0)
    SetChrPos(0x5, 19940, 0, -37920, 0)
    Jump("loc_14A5")

    label("loc_1486")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14A5")
    SetChrPos(0x4, 19940, 0, -37920, 0)

    label("loc_14A5")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14AE")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_14CF")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_189F")

    label("loc_14CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_14F6")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    Jump("loc_189F")

    label("loc_14F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_15A0")
    SetChrPos(0x9, 9470, 2500, 5580, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 11770, 2500, 4330, 45)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 11440, 2410, 7980, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 9580, 2500, 7830, 90)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 13290, 2410, 9400, 90)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_189F")

    label("loc_15A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_15F9")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xF, -11910, 2490, 8950, 45)
    SetChrPos(0x10, -12830, 2500, 9870, 45)
    BeginChrThread(0x10, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1C, 0x80)
    Jump("loc_189F")

    label("loc_15F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1627")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xF, 0xB)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    Jump("loc_189F")

    label("loc_1627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_165A")
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x9, 0x16)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1655")
    ClearChrFlags(0xB, 0x80)

    label("loc_1655")

    Jump("loc_189F")

    label("loc_165A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1688")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xF, 0xB)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    Jump("loc_189F")

    label("loc_1688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_16BB")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xF, 0xB)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    Jump("loc_189F")

    label("loc_16BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_16EE")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xF, 0xB)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    Jump("loc_189F")

    label("loc_16EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1798")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x10)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xF, 0xB)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -3560, 2500, 28520, 180)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -9470, 2500, 29190, 180)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x1F, 0x10)
    SetChrFlags(0x20, 0x10)
    SetChrFlags(0x21, 0x10)
    Jump("loc_189F")

    label("loc_1798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1806")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xF, 0xB)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -3560, 2500, 28520, 180)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -9470, 2500, 29190, 180)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_189F")

    label("loc_1806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_184F")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -3560, 2500, 28520, 180)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -9470, 2500, 29190, 180)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_189F")

    label("loc_184F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1875")
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x9, 0x16)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_189F")

    label("loc_1875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_189F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189F")
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189F")
    SetChrFlags(0xB, 0x10)

    label("loc_189F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18BA")
    Event(0, 41)

    label("loc_18BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18E5")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_18E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_18F9")
    ClearScenarioFlags(0x22, 0)
    Event(0, 42)
    Jump("loc_193E")

    label("loc_18F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_190D")
    ClearScenarioFlags(0x22, 1)
    Event(0, 44)
    Jump("loc_193E")

    label("loc_190D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1927")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 3)
    Event(0, 48)
    Jump("loc_193E")

    label("loc_1927")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_193E")
    ClearScenarioFlags(0x22, 3)
    SetMapFlags(0x10000000)
    SetScenarioFlags(0x1, 3)
    Event(0, 60)

    label("loc_193E")

    Return()

    # Function_7_11C8 end

    def Function_8_193F(): pass

    label("Function_8_193F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1954")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 2)

    label("loc_1954")

    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1983")
    Jump("loc_1A10")

    label("loc_1983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1991")
    Jump("loc_1A10")

    label("loc_1991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_19AB")
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x2)
    Jump("loc_1A10")

    label("loc_19AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_19C5")
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x2)
    Jump("loc_1A10")

    label("loc_19C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_19D3")
    Jump("loc_1A10")

    label("loc_19D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_19ED")
    SetMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    Jump("loc_1A10")

    label("loc_19ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_19FB")
    Jump("loc_1A10")

    label("loc_19FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1A10")
    SetMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x2)

    label("loc_1A10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A3F")
    SetMapObjFrame(0xFF, "ibc_pano", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ibc_pano2", 0x1, 0x1)
    Jump("loc_1A60")

    label("loc_1A3F")

    SetMapObjFrame(0xFF, "ibc_pano", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ibc_pano2", 0x0, 0x1)

    label("loc_1A60")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A79")
    ClearMapObjFlags(0x6, 0x4)
    Jump("loc_1A7F")

    label("loc_1A79")

    SetMapObjFlags(0x6, 0x4)

    label("loc_1A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A97")
    ClearMapFlags(0x2000)
    Jump("loc_1A9E")

    label("loc_1A97")

    SetMapFlags(0x2000)
    OP_E2(0x1)

    label("loc_1A9E")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AC0")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1AC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ADB")
    OP_1B(0x8, 0x0, 0x3B)

    label("loc_1ADB")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -5540, 2500, 32280, 8000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B0F")
    SetMapObjFlags(0x5, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    OP_65(0x0, 0x1)

    label("loc_1B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B22")
    OP_1B(0x8, 0x0, 0x43)

    label("loc_1B22")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B3A")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1B3A")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B56")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_1B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B68")
    OP_65(0x1, 0x1)
    Jump("loc_1BCC")

    label("loc_1B68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B7C")
    ClearMapObjFlags(0x12, 0x4)
    Jump("loc_1BCC")

    label("loc_1B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1B8E")
    OP_65(0x1, 0x1)
    Jump("loc_1BCC")

    label("loc_1B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1BA2")
    ClearMapObjFlags(0x12, 0x4)
    Jump("loc_1BCC")

    label("loc_1BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1BB4")
    OP_65(0x1, 0x1)
    Jump("loc_1BCC")

    label("loc_1BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1BC8")
    ClearMapObjFlags(0x12, 0x4)
    Jump("loc_1BCC")

    label("loc_1BC8")

    OP_65(0x1, 0x1)

    label("loc_1BCC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1BEB")
    OP_10(0x2, 0x0)
    OP_10(0x9, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0xA, 0x1)
    Jump("loc_1BF7")

    label("loc_1BEB")

    OP_10(0x2, 0x1)
    OP_10(0x9, 0x0)
    OP_10(0x1, 0x1)
    OP_10(0xA, 0x0)

    label("loc_1BF7")

    OP_52(0x47, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x47, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x48, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x49, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20A4")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0xAF, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo_sd", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_20A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2153")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x190, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo_sd", 0x0, 0x1)

    label("loc_2153")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_21B5")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x2C, 0xAF, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo_sd", 0x0, 0x1)

    label("loc_21B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_21C9")
    OP_24(0x7B)
    ClearScenarioFlags(0x1, 3)
    Jump("loc_21E5")

    label("loc_21C9")

    SoundDistance(0x7B, 0xFFFFB32A, 0x99C, 0xFFFFC324, 0x2710, 0x186A0, 0x64, 0x0)

    label("loc_21E5")

    Return()

    # Function_8_193F end

    def Function_9_21E6(): pass

    label("Function_9_21E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_221D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_221D")
    Call(0, 65)
    Return()

    label("loc_221D")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_222A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_325D")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_227C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_227C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_229C")
    OP_AF(0x80)
    Jump("loc_229E")

    label("loc_229C")

    OP_AF(0x81)

    label("loc_229E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3258")

    label("loc_22AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22C1")
    Jump("loc_3258")

    label("loc_22C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3258")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_237E")

    ChrTalk(
        0xFE,
        (
            "Hmm, it seems my bitter\x01",
            "tomato soda has quite a bit\x01",
            "of room for improvement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to work hard to\x01",
            "create juice that\x01",
            "everyone can enjoy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3258")

    label("loc_237E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_24D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244D")

    ChrTalk(
        0xFE,
        "Good work, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it's not one of my\x01",
            "originals, I recommend\x01",
            ""Sporitan X" for tired bodies!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'll completely refill\x01",
            "your energy, so you can\x01",
            "do your best!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24D2")

    label("loc_244D")


    ChrTalk(
        0xFE,
        (
            "I got word earlier... Thank\x01",
            "goodness my mom in the\x01",
            "department store is safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "C'mon everyone! Cheer up\x01",
            "with Sporitan power!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24D2")

    Jump("loc_3258")

    label("loc_24D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_24E5")
    Jump("loc_3258")

    label("loc_24E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2534")

    ChrTalk(
        0xFE,
        (
            "Everyone's so\x01",
            "enthusiastic... Somehow,\x01",
            "it's a little scary.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3258")

    label("loc_2534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_26A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2603")

    ChrTalk(
        0xFE,
        "Good work, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it's not one of my\x01",
            "originals, I recommend\x01",
            ""Sporitan X" for tired bodies!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'll completely refill\x01",
            "your energy, so you can\x01",
            "do your best!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_269D")

    label("loc_2603")


    ChrTalk(
        0xFE,
        (
            "Although it's not one of my\x01",
            "originals, I recommend\x01",
            ""Sporitan X" for tired bodies!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'll completely refill\x01",
            "your energy, so you can\x01",
            "do your best!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_269D")

    Jump("loc_3258")

    label("loc_26A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2847")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2795")

    ChrTalk(
        0xFE,
        (
            "A Mainz occupation...\x01",
            "That's really scary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should we accept it? It looks like\x01",
            "people have been arguing about\x01",
            "that since early this morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, I'm not\x01",
            "yet sure what to make of\x01",
            "all this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2842")

    label("loc_2795")


    ChrTalk(
        0xFE,
        (
            "It looks like people have been arguing\x01",
            "about whether to accept the occupation\x01",
            "since early this morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, I'm not\x01",
            "yet sure what to make of\x01",
            "all this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2842")

    Jump("loc_3258")

    label("loc_2847")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2855")
    Jump("loc_3258")

    label("loc_2855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_297C")

    ChrTalk(
        0xFE,
        (
            "The police have been\x01",
            "looking panicked since\x01",
            "earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did some kind of\x01",
            "incident occur again?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2977")

    ChrTalk(
        0x101,
        (
            "#00008F(I think we can get\x01",
            "coverage for the gourmet\x01",
            "guide here, but...)\x02\x03",
            "#00003F(Now's not the time.\x01",
            "Let's not forget to stop\x01",
            "by later.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2977")

    Jump("loc_3258")

    label("loc_297C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ACA")

    ChrTalk(
        0xFE,
        (
            "It's been almost a year since I\x01",
            "opened my juice shop, but\x01",
            "thankfully my sales are doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People gradually began to notice my\x01",
            "place, and my recent "limited edition"\x01",
            "strategy has done especially well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Even if I say so myself,\x01",
            "people are weak to names to\x01",
            "which "limited" is attached.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2B60")

    label("loc_2ACA")


    ChrTalk(
        0xFE,
        (
            "Selling my new juice for\x01",
            "a limited time was my\x01",
            "mom's idea, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My mom's a merchant at her\x01",
            "core. I'm always learning\x01",
            "new things from her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B60")

    Jump("loc_3258")

    label("loc_2B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C83")

    ChrTalk(
        0xFE,
        (
            "Welcome! Would you like\x01",
            "my new, fresh juice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is a limited item made exclusively\x01",
            "with local Crossbell ingredients, with\x01",
            "the theme of Crossbell independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is filled with the condensed\x01",
            "deliciousness of Crossbell. You\x01",
            "just have to try it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2D54")

    label("loc_2C83")


    ChrTalk(
        0xFE,
        (
            "It is a limited item made exclusively\x01",
            "with local Crossbell ingredients, with\x01",
            "the theme of Crossbell independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is filled with the condensed\x01",
            "deliciousness of our state. You\x01",
            "just have to try it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D54")

    Jump("loc_3258")

    label("loc_2D59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2F04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E53")

    ChrTalk(
        0xFE,
        (
            "Because of today's main session,\x01",
            "it seems the area around Orchis\x01",
            "Tower is blockaded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Too bad. I was thinking\x01",
            "on checking on the\x01",
            "situation over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I suppose safety\x01",
            "is a natural thing to\x01",
            "think about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2EFF")

    label("loc_2E53")


    ChrTalk(
        0xFE,
        (
            "Because of today's main session,\x01",
            "it seems the area around Orchis\x01",
            "Tower is blockaded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though safety is a natural\x01",
            "thing to think about, as a\x01",
            "citizen, it's too bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EFF")

    Jump("loc_3258")

    label("loc_2F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2FAB")

    ChrTalk(
        0xFE,
        (
            "There were a lot of people\x01",
            "here this morning, but\x01",
            "it's finally calmed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, but thanks to\x01",
            "that, I'm already over\x01",
            "my daily sales average.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3258")

    label("loc_2FAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3049")

    ChrTalk(
        0xFE,
        (
            "Welcome! Would you like\x01",
            "my new, fresh juice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of the trade conference,\x01",
            "I'm going to offer a special\x01",
            "product starting tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3258")

    label("loc_3049")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3057")
    Jump("loc_3258")

    label("loc_3057")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3258")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30CD")

    ChrTalk(
        0xFE,
        (
            "T-That was an amazing\x01",
            "arrest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, it seems our\x01",
            "police are doing their\x01",
            "best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3258")

    label("loc_30CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31BE")

    ChrTalk(
        0xFE,
        (
            "Welcome! Would you like\x01",
            "my new, fresh juice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of the situation, I\x01",
            "made a limited-time product\x01",
            "using imported ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You won't be able to get it\x01",
            "if you miss this chance!\x01",
            "Please try my new flavor!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3258")

    label("loc_31BE")


    ChrTalk(
        0xFE,
        (
            "Because of the situation, I\x01",
            "made a limited-time product\x01",
            "using imported ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You should try it at\x01",
            "least once, before it's\x01",
            "gone for good!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3258")

    Jump("loc_222A")

    label("loc_325D")

    TalkEnd(0xFE)
    Return()

    # Function_9_21E6 end

    def Function_10_3261(): pass

    label("Function_10_3261")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_33B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3356")

    ChrTalk(
        0xFE,
        (
            "This abnormal situation\x01",
            "that has appeared in\x01",
            "Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho, it's in times like\x01",
            "these that we citizens\x01",
            "must unite as one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't lose, Crossbell! Go\x01",
            "for it, Chairman MacDowell!\x01",
            "...You guys as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_33B3")

    label("loc_3356")


    ChrTalk(
        0xFE,
        (
            "Hoho... Go for it, you\x01",
            "guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't lose, Crossbell!\x01",
            "Go for it, Chairman\x01",
            "MacDowell!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B3")

    Jump("loc_4280")

    label("loc_33B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_33C6")
    Jump("loc_4280")

    label("loc_33C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_342D")

    ChrTalk(
        0xFE,
        (
            "Hooray, President\x01",
            "Dieter!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll forgive neither the\x01",
            "Empire, nor the\x01",
            "Republic!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4280")

    label("loc_342D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_361B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_355E")

    ChrTalk(
        0xFE,
        (
            "Even now it is seared into my\x01",
            "eyes... To think that Lady Ilya\x01",
            "is in such a condition...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mrrgrgr...I'll never forgive\x01",
            "that armed group! And I'll never\x01",
            "forgive the Empire Government!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Given the situation, we can\x01",
            "only firmly become independent\x01",
            "and radically resist!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3616")

    label("loc_355E")


    ChrTalk(
        0xFE,
        (
            "Mrrgrgr...I'll never forgive\x01",
            "that armed group! And I'll never\x01",
            "forgive the Empire Government!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Given the situation, we can\x01",
            "only firmly become independent\x01",
            "and radically resist!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3616")

    Jump("loc_4280")

    label("loc_361B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3763")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F2")

    ChrTalk(
        0xFE,
        (
            "Hmm, an incident in the\x01",
            "mining town. I hate\x01",
            "times like these...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Anyway, today is opening\x01",
            "day for the long-awaited\x01",
            "renewal performance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I plan to enjoy it to\x01",
            "the fullest!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_375E")

    label("loc_36F2")


    ChrTalk(
        0xFE,
        (
            "Today is opening day for\x01",
            "the long-awaited renewal\x01",
            "performance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I plan to enjoy it to\x01",
            "the fullest!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_375E")

    Jump("loc_4280")

    label("loc_3763")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_38B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3846")

    ChrTalk(
        0xFE,
        (
            "Finally! The renewal\x01",
            "performance finally\x01",
            "opens tomorrow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't hold back my excitement!\x01",
            "Hmm, this rain is just perfect\x01",
            "for my burning body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll be able to\x01",
            "stay cool somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_38B2")

    label("loc_3846")


    ChrTalk(
        0xFE,
        (
            "...Hmm, this rain is\x01",
            "just perfect for my\x01",
            "burning body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll be able to\x01",
            "stay cool somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38B2")

    Jump("loc_4280")

    label("loc_38B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39BB")

    ChrTalk(
        0xFE,
        (
            "There's just two days until\x01",
            "the "Golden Sun, Silver\x01",
            "Moon" renewal performance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Umm, just when is the performance?\x01",
            "It's in the evening, so... There's\x01",
            "less than 48 hours to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*fidget*... Oh, I can't\x01",
            "bear this waiting!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3A1E")

    label("loc_39BB")


    ChrTalk(
        0xFE,
        (
            "*fidget*... I want the\x01",
            "day after tomorrow to\x01",
            "arrive ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, I can't bear this\x01",
            "waiting!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A1E")

    Jump("loc_4280")

    label("loc_3A23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3AAA")

    ChrTalk(
        0xFE,
        (
            "There's just two days until\x01",
            "the "Golden Sun, Silver\x01",
            "Moon" renewal performance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, I can't bear this\x01",
            "waiting!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4280")

    label("loc_3AAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3C27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B72")

    ChrTalk(
        0xFE,
        (
            "Arc-en-Ciel's renewal\x01",
            "performance will be here\x01",
            "in just three days!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And... I managed to get\x01",
            "tickets for opening\x01",
            "night!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, I can't help but be\x01",
            "extra excited!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3C22")

    label("loc_3B72")


    ChrTalk(
        0xFE,
        (
            "But even so, I was surprised\x01",
            "at their additional cast\x01",
            "announcement the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sully Atraid... I'm surprised\x01",
            "she's filling such a big role\x01",
            "at her young age of 13!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C22")

    Jump("loc_4280")

    label("loc_3C27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3DA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D37")

    ChrTalk(
        0xFE,
        (
            "It starts this afternoon, if I\x01",
            "recall. Finally, the main\x01",
            "session opens at Orchis Tower!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. For a better\x01",
            "conference, I think I'll\x01",
            "send my support there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#4SMayor Dieter! We citizens\x01",
            "support you from the\x01",
            "bottom of our hearts!!#3S\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3DA3")

    label("loc_3D37")


    ChrTalk(
        0xFE,
        "Hmm, one more time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#4SMayor Dieter! We citizens\x01",
            "support you from the\x01",
            "bottom of our hearts!!#3S\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DA3")

    Jump("loc_4280")

    label("loc_3DA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E63")

    ChrTalk(
        0xFE,
        (
            "Orchis Tower! How\x01",
            "magnificent!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm liking this city\x01",
            "more and more!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With this, Crossbell adds yet\x01",
            "another famous place to its\x01",
            "arsenal! Very good, very good!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4280")

    label("loc_3E63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_401C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F7D")

    ChrTalk(
        0xFE,
        (
            "Hmm, the heads of state are finally\x01",
            "coming to Crossbell from their\x01",
            "respective countries tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And the Orchis Tower\x01",
            "unveiling ceremony is\x01",
            "also tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, just thinking about it\x01",
            "makes me so excited, I won't\x01",
            "be able to sleep tonight!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4017")

    label("loc_3F7D")


    ChrTalk(
        0xFE,
        (
            "Hmm, just thinking about\x01",
            "tomorrow makes me so excited, I\x01",
            "won't be able to sleep tonight!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was going to have a\x01",
            "sleepless night sooner\x01",
            "or later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4017")

    Jump("loc_4280")

    label("loc_401C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_40C5")

    ChrTalk(
        0xFE,
        (
            "Good morning. Though unfortunately\x01",
            "it's raining today, days like this\x01",
            "are good every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I always knew\x01",
            "Crossbell was the best!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4280")

    label("loc_40C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4280")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4195")

    ChrTalk(
        0xFE,
        (
            "Your skill in setting up\x01",
            "those sandbags earlier was\x01",
            "nothing short of remarkable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wasn't sure what you were\x01",
            "doing at the start, but... Yes,\x01",
            "it turned out splendidly!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4280")

    label("loc_4195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_420D")

    ChrTalk(
        0xFE,
        (
            "Good morning. Nice\x01",
            "weather today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The perfect weather for\x01",
            "a walk. Ah, very good,\x01",
            "very good!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4280")

    label("loc_420D")


    ChrTalk(
        0xFE,
        (
            "I love the Crossbell\x01",
            "townscape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though I hear dangerous\x01",
            "stories all the time, even\x01",
            "so, I love this city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4280")

    TalkEnd(0xFE)
    Return()

    # Function_10_3261 end

    def Function_11_4284(): pass

    label("Function_11_4284")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_44A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_431F")

    ChrTalk(
        0xFE,
        (
            "That arrested guy's\x01",
            "car... It looked really\x01",
            "expensive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, is it Verne Co.'s\x01",
            "latest model? He must be\x01",
            "loaded...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44A7")

    label("loc_431F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43DB")

    ChrTalk(
        0xFE,
        (
            "Congress has completely\x01",
            "changed ever since the\x01",
            "cult incident, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though we in the Finance\x01",
            "Division are busy as usual, it's\x01",
            "easy work compared to before.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_44A7")

    label("loc_43DB")


    ChrTalk(
        0xFE,
        (
            "Above all, most of those\x01",
            "Imperial and Republican\x01",
            "congresspeople have been purged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the other hand, it's not the case\x01",
            "that we can ignore those countries'\x01",
            "ideas, but... The difference is clear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44A7")

    TalkEnd(0xFE)
    Return()

    # Function_11_4284 end

    def Function_12_44AB(): pass

    label("Function_12_44AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_46E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4663")

    ChrTalk(
        0xFE,
        (
            "Just what is that huge\x01",
            "tree? It looks like it's\x01",
            "glowing bluish-white.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A lot of unbelievable things have been\x01",
            "happening around here lately, but this\x01",
            "is weird beyond my wildest expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Are you guys really\x01",
            "planning on jumping into\x01",
            "that thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Yeah. We can't back\x01",
            "down now.\x02\x03",
            "#00000FThe city's counting on\x01",
            "you, Frantz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Y-Yeah, leave it to me.\x01",
            "...You guys be careful,\x01",
            "ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_46E0")

    label("loc_4663")


    ChrTalk(
        0xFE,
        (
            "Right now, all of us\x01",
            "have to do what we can,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, leave this place\x01",
            "to me. ...You guys be\x01",
            "careful, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46E0")

    Jump("loc_5523")

    label("loc_46E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_46F3")
    Jump("loc_5523")

    label("loc_46F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4701")
    Jump("loc_5523")

    label("loc_4701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_470F")
    Jump("loc_5523")

    label("loc_470F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_471D")
    Jump("loc_5523")

    label("loc_471D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_48FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4848")

    ChrTalk(
        0xFE,
        (
            "To think it was completely\x01",
            "restored as of this morning...\x01",
            "Those CGF guys are something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Like the police, I feel the CGF\x01",
            "are often undervalued lately, when\x01",
            "in actuality, they're a big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seeing them working at\x01",
            "the scene gave me some\x01",
            "serious courage.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_48F6")

    label("loc_4848")


    ChrTalk(
        0xFE,
        (
            "Like the police, I feel the CGF\x01",
            "are often undervalued lately, when\x01",
            "in actuality, they're a big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seeing them working at\x01",
            "the scene gave me some\x01",
            "serious courage.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48F6")

    Jump("loc_5523")

    label("loc_48FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4909")
    Jump("loc_5523")

    label("loc_4909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_49C7")

    ChrTalk(
        0xFE,
        (
            "Lately, things called Cryptids\x01",
            "have been appearing here and\x01",
            "there outside the city lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard they disappear with\x01",
            "a *poof* when you defeat\x01",
            "them. ...How strange.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5523")

    label("loc_49C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4ECA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E2F")

    ChrTalk(
        0xFE,
        (
            "The terrorist attack on the\x01",
            "trade conference was really\x01",
            "hard on the Crossbell police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Trust in the police was\x01",
            "improving but now it's\x01",
            "as low as ever...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Standing in the city like\x01",
            "this, I really feel that the\x01",
            "criticism has gotten stronger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though you and the\x01",
            "Special Support Section\x01",
            "are a different story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FAh, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FBut, criticism, you\x01",
            "said? Is it that bad?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For starters, the jeering\x01",
            "tones we get when on patrol\x01",
            "are clearly more than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            ""Thanks for your\x01",
            "meaningless vigilance"\x01",
            "and such.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            ""The two majors powers take\x01",
            "advantage of us because\x01",
            "you're useless" and such.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though I can't deny it, I wish\x01",
            "they wouldn't fan the flames\x01",
            "any more than necessary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FI see... They're quite\x01",
            "bitter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FWell, no matter what\x01",
            "anyone says, we can only\x01",
            "do what we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FYes. There's a big difference\x01",
            "between having a tiny bit of\x01",
            "power and having none at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha. But a little\x01",
            "rumor's nothing to get\x01",
            "excited about, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha... You're certainly\x01",
            "right about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks. I feel refreshed\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 5)
    Jump("loc_4EC5")

    label("loc_4E2F")


    ChrTalk(
        0xFE,
        (
            "All we can do is what we\x01",
            "can. That's definitely\x01",
            "true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It can't be helped if our\x01",
            "efforts are futile... We need\x01",
            "to do our best and try again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EC5")

    Jump("loc_5523")

    label("loc_4ECA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4EDB")
    Call(0, 13)
    Jump("loc_5523")

    label("loc_4EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_508C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FE9")

    ChrTalk(
        0xFE,
        (
            "Oh, Lloyd. The plaza is open\x01",
            "to the public today, so feel\x01",
            "free to pass through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, but just seeing the\x01",
            "unveiling ceremony from\x01",
            "here was plenty amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's amazing to think\x01",
            "something like that could\x01",
            "be built with human hands.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5087")

    label("loc_4FE9")


    ChrTalk(
        0xFE,
        (
            "Ah, but just seeing the\x01",
            "unveiling ceremony from\x01",
            "here was plenty amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's amazing to think\x01",
            "something like that could\x01",
            "be built with human hands.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5087")

    Jump("loc_5523")

    label("loc_508C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5329")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_525C")

    ChrTalk(
        0xFE,
        (
            "Hey Lloyd. The trade\x01",
            "conference finally\x01",
            "starts tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The CGF will be on guard\x01",
            "too. I'm already\x01",
            "nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FIt's because the heads of\x01",
            "state are coming to\x01",
            "Crossbell tomorrow.\x02\x03",
            "#00000FAdditionally, it'll be\x01",
            "the long-awaited Orchis\x01",
            "Tower unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*. All of this is\x01",
            "just so unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, for the next three\x01",
            "days starting tomorrow,\x01",
            "let's both brace ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FYeah, got it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 4)
    Jump("loc_5324")

    label("loc_525C")


    ChrTalk(
        0xFE,
        (
            "An international conference of\x01",
            "unprecedented scale... The more I think\x01",
            "about it, the more nervous I get.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well anyway, we've got to\x01",
            "brace ourselves for the next\x01",
            "three days starting tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5324")

    Jump("loc_5523")

    label("loc_5329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_546C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5344")
    Call(0, 14)
    Jump("loc_5467")

    label("loc_5344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_53EE")

    ChrTalk(
        0xFE,
        (
            "I admire the Support\x01",
            "Section... Somehow, I feel I\x01",
            "have to stick to your ideals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How to say it... I've\x01",
            "decided to be the best\x01",
            "me that I can be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 6)
    Jump("loc_5467")

    label("loc_53EE")


    ChrTalk(
        0xFE,
        (
            "Though it's only light\x01",
            "rain, policing on rainy\x01",
            "days isn't easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Take care that you guys\x01",
            "don't catch any colds.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5467")

    Jump("loc_5523")

    label("loc_546C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5523")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5487")
    Call(0, 14)
    Jump("loc_5523")

    label("loc_5487")


    ChrTalk(
        0xFE,
        (
            "I admire the Support\x01",
            "Section... Somehow, I feel I\x01",
            "have to stick to your ideals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How to say it... I've\x01",
            "decided to be the best\x01",
            "me that I can be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 6)

    label("loc_5523")

    TalkEnd(0xFE)
    Return()

    # Function_12_44AB end

    def Function_13_5527(): pass

    label("Function_13_5527")

    OP_4B(0xB, 0xFF)
    OP_4B(0x1F, 0xFF)
    OP_4B(0x20, 0xFF)
    OP_4B(0x21, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5709")

    ChrTalk(
        0xB,
        (
            "I-I'm terribly sorry. Because\x01",
            "of the main session today,\x01",
            "the general public is―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Hmm. But the plaza has\x01",
            "nothing to do with that,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Yeah, yeah! We're here\x01",
            "on vacation, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "So, can we go just for a\x01",
            "little? 10 minutes. No,\x01",
            "how about 5?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ah, umm, that's not the\x01",
            "issue here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(It looks like they're\x01",
            "complaining that the\x01",
            "plaza is blockaded.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Yeah. ...Looks like\x01",
            "Frantz is having a hard\x01",
            "time.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5845")

    label("loc_5709")


    ChrTalk(
        0x21,
        (
            "5 minutes, no, 3. Pretty\x01",
            "please?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Yeah, yeah! We'll be\x01",
            "there only a little\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Ah, well it shouldn't be\x01",
            "a problem to go through\x01",
            "the plaza to begin with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "U-Umm, anyway, things\x01",
            "that are off limits are\x01",
            "off limits...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(When it's time for us\x01",
            "to pass through, let's\x01",
            "do it nonchalantly...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5845")

    OP_4C(0xB, 0xFF)
    OP_4C(0x1F, 0xFF)
    OP_4C(0x20, 0xFF)
    OP_4C(0x21, 0xFF)
    Return()

    # Function_13_5527 end

    def Function_14_5856(): pass

    label("Function_14_5856")

    RunExpression(0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xB, 0x101, 0)

    ChrTalk(
        0xB,
        (
            "Hey Lloyd. So your\x01",
            "Section One training is\x01",
            "finally over, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "So now you're finally a\x01",
            "senior detective...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*sigh*. Even though we went to\x01",
            "police academy at the same time,\x01",
            "you're in a whole other league.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FDon't say that.\x02\x03",
            "#00000FBy the way, how did you\x01",
            "do on the detective\x01",
            "exam, Frantz?\x02\x03",
            "You took it a little\x01",
            "while ago, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*sigh*. If I had passed,\x01",
            "you'd be the first to\x01",
            "know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The result was crushing failure...\x01",
            "To be precise, it made me realize\x01",
            "I'm not cut out to be a detective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008FThat bad, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ah, but thanks to that,\x01",
            "I feel relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Right now, the work of the\x01",
            "Patrol Division is more than\x01",
            "important enough for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm trying to say I don't think\x01",
            "I have to stick to becoming a\x01",
            "detective that much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "From now on, I've\x01",
            "decided to be the best\x01",
            "me that I can be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FFrantz...\x02\x03",
            "#00002FOh. Now that I think about\x01",
            "it, that's the most\x01",
            "important thing.\x02\x03",
            "In that case, from now on,\x01",
            "let's each do our best on\x01",
            "our respective paths.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yeah, of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F(Hmm, this must be what\x01",
            "they call male bonding.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F(Yes, I'm a little\x01",
            "jealous.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xB, 0x10)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x13E, 5)
    Return()

    # Function_14_5856 end

    def Function_15_5CE9(): pass

    label("Function_15_5CE9")

    TalkBegin(0xFE)
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    # Function_15_5CE9 end

    def Function_16_5CF3(): pass

    label("Function_16_5CF3")

    TalkBegin(0xFE)
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    # Function_16_5CF3 end

    def Function_17_5CFD(): pass

    label("Function_17_5CFD")

    TalkBegin(0xFE)
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    # Function_17_5CFD end

    def Function_18_5D07(): pass

    label("Function_18_5D07")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5D18")
    Jump("loc_621F")

    label("loc_5D18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5FEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F6D")

    ChrTalk(
        0xFE,
        (
            "Oh, the Special Support\x01",
            "Section, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, thanks for your\x01",
            "hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHQ is still under\x01",
            "repair, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes. At present we've\x01",
            "put things in order,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In any case, the damage\x01",
            "to the entrance is\x01",
            "really awful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It will take quite a\x01",
            "while to restore the\x01",
            "reception functions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Incidentally, the reception\x01",
            "office work is temporarily being\x01",
            "performed at the police academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rebecca is there too, so if\x01",
            "you have job-related paperwork\x01",
            "you can do it there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FI see, we understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FThank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 4)
    Jump("loc_5FE6")

    label("loc_5F6D")


    ChrTalk(
        0xFE,
        (
            "It will be some time\x01",
            "until HQ is repaired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have job-related\x01",
            "paperwork you can go to\x01",
            "the police academy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FE6")

    Jump("loc_621F")

    label("loc_5FEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_60A7")

    ChrTalk(
        0xFE,
        (
            "Today, entry to the Orchis\x01",
            "Tower area is off limits\x01",
            "to the general public.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But as you can see, there's a\x01",
            "lot of people complaining\x01",
            "saying, "I hadn't heard that"...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_621F")

    label("loc_60A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_614E")

    ChrTalk(
        0xFE,
        (
            "Orchis Tower plaza is\x01",
            "crowded with a lot of\x01",
            "citizens and tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it's right after\x01",
            "the unveiling ceremony,\x01",
            "traffic will be incessant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_621F")

    label("loc_614E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6208")

    ChrTalk(
        0xFE,
        (
            "The unveiling ceremony\x01",
            "will finally be held\x01",
            "tomorrow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been five years since construction\x01",
            "on our new City Hall building was\x01",
            "started. It's finally complete.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_621F")

    label("loc_6208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6216")
    Jump("loc_621F")

    label("loc_6216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_621F")

    label("loc_621F")

    TalkEnd(0xFE)
    Return()

    # Function_18_5D07 end

    def Function_19_6223(): pass

    label("Function_19_6223")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_63A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_632A")

    ChrTalk(
        0xFE,
        (
            "The heads of state will gather at\x01",
            "Orchis Tower this afternoon...\x01",
            "Then, the main session will begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of the situation,\x01",
            "it's highly unlikely that\x01",
            "nothing will happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I'll raise my\x01",
            "fighting spirit today.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_63A2")

    label("loc_632A")


    ChrTalk(
        0xFE,
        (
            "To be precise, the\x01",
            "possibility nothing will\x01",
            "happen is quite low.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I'll raise my\x01",
            "fighting spirit today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63A2")

    Jump("loc_6681")

    label("loc_63A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6487")

    ChrTalk(
        0xFE,
        (
            "It's not as bad as the\x01",
            "anniversary festival, but I knew\x01",
            "the turnout today would be high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's a possibility that an unexpected\x01",
            "act of terror could create a\x01",
            "disturbance. We must cautiously observe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6681")

    label("loc_6487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6681")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65C1")

    ChrTalk(
        0xFE,
        (
            "Tomorrow, all the heads of\x01",
            "state will leave this district\x01",
            "and head for the new City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This place has an unobstructed\x01",
            "view, and it'd be easy for a\x01",
            "sniper to target them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We plan to deploy a strict security\x01",
            "structure to greet the heads of\x01",
            "state as they enter Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_6681")

    label("loc_65C1")


    ChrTalk(
        0xFE,
        (
            "This place has an unobstructed\x01",
            "view, and it'd be easy for a\x01",
            "sniper to target them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We plan to deploy a strict security\x01",
            "structure to greet the heads of\x01",
            "state as they enter Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6681")

    TalkEnd(0xFE)
    Return()

    # Function_19_6223 end

    def Function_20_6685(): pass

    label("Function_20_6685")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_672B")

    ChrTalk(
        0xFE,
        (
            "That two terrorist\x01",
            "organizations came at the\x01",
            "same time is no joke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway... We've got to\x01",
            "stop them at all costs,\x01",
            "before chaos breaks out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68A9")

    label("loc_672B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_67D0")

    ChrTalk(
        0xFE,
        (
            "Damn. If I was in charge of Orchis\x01",
            "Tower area security, I could've\x01",
            "seen the heads of state...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All I got to see were\x01",
            "smoked-glass limousines.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68A9")

    label("loc_67D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_68A9")

    ChrTalk(
        0xFE,
        (
            "To think the heads of state from all four\x01",
            "neighboring countries are going to meet...\x01",
            "To be honest, the scale is too amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...The tension of our guard\x01",
            "duties thus far might only\x01",
            "be the beginning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68A9")

    TalkEnd(0xFE)
    Return()

    # Function_20_6685 end

    def Function_21_68AD(): pass

    label("Function_21_68AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6971")

    ChrTalk(
        0xC,
        "#01200FGrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FSo that's where you\x01",
            "were, Zeit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FIt seems he came to\x01",
            "escort KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FEven so, he's really\x01",
            "gotten used to the city,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_698D")

    label("loc_6971")


    ChrTalk(
        0xC,
        "#01200FGrrowl... Woof.\x02",
    )

    CloseMessageWindow()

    label("loc_698D")

    TalkEnd(0xFE)
    Return()

    # Function_21_68AD end

    def Function_22_6991(): pass

    label("Function_22_6991")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A0A")

    ChrTalk(
        0xFE,
        (
            "Come now, who wants a\x01",
            "balloon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Be it 1, 2 or 3, you can\x01",
            "have however many you\x01",
            "want today.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6A85")

    label("loc_6A0A")


    ChrTalk(
        0xFE,
        (
            "I'm going to hold a\x01",
            "balloon art class this\x01",
            "afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I sincerely hope that\x01",
            "all who are interested\x01",
            "will attend~!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A85")

    TalkEnd(0xFE)
    Return()

    # Function_22_6991 end

    def Function_23_6A89(): pass

    label("Function_23_6A89")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6B9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B09")

    ChrTalk(
        0x22,
        (
            "KeA said she was going\x01",
            "to the library today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "I wonder if she's\x01",
            "looking for something...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6B9A")

    label("loc_6B09")


    ChrTalk(
        0x22,
        (
            "I heard Shing, who\x01",
            "stopped by yesterday, was\x01",
            "leaving on a train today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "I'm a little lonely...\x01",
            "It seemed like we could\x01",
            "be good friends.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B9A")

    TalkEnd(0xFE)
    Return()

    # Function_23_6A89 end

    def Function_24_6B9E(): pass

    label("Function_24_6B9E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6C5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C23")

    ChrTalk(
        0x23,
        (
            "Damn, they said I\x01",
            "couldn't enter. How\x01",
            "stingy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Aww, man. I wonder if we\x01",
            "can sneak in somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6C5F")

    label("loc_6C23")


    ChrTalk(
        0x23,
        (
            "Ah, if I don't hurry,\x01",
            "the party will start\x01",
            "without me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C5F")

    TalkEnd(0xFE)
    Return()

    # Function_24_6B9E end

    def Function_25_6C63(): pass

    label("Function_25_6C63")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6CBC")

    ChrTalk(
        0x24,
        "Give up already, Ryｹ.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "It's a trade conference,\x01",
            "not some fun party!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CBC")

    TalkEnd(0xFE)
    Return()

    # Function_25_6C63 end

    def Function_26_6CC0(): pass

    label("Function_26_6CC0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6D20")

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "That Empire and\x01",
            "Republic. They're coming\x01",
            "after us from all sides!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DD1")

    label("loc_6D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6D7F")

    ChrTalk(
        0xFE,
        (
            "They said we couldn't\x01",
            "enter the tower plaza\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*, how boring.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6DD1")

    label("loc_6D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_6D8D")
    Jump("loc_6DD1")

    label("loc_6D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6DD1")

    ChrTalk(
        0xFE,
        (
            "Wow, amazing. It's huge\x01",
            "even looking at it from\x01",
            "here!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DD1")

    TalkEnd(0xFE)
    Return()

    # Function_26_6CC0 end

    def Function_27_6DD5(): pass

    label("Function_27_6DD5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6E45")

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "If Arios is the Secretary of\x01",
            "Defense, we'll be safe even\x01",
            "after we're independent!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ED0")

    label("loc_6E45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6E8D")

    ChrTalk(
        0xFE,
        (
            "Aww. I wanted to look up\x01",
            "at it like I did\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ED0")

    label("loc_6E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_6E9B")
    Jump("loc_6ED0")

    label("loc_6E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6ED0")

    ChrTalk(
        0xFE,
        (
            "I know, right. Isn't it\x01",
            "just too huge?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6ED0")

    TalkEnd(0xFE)
    Return()

    # Function_27_6DD5 end

    def Function_28_6ED4(): pass

    label("Function_28_6ED4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6F38")

    ChrTalk(
        0xFE,
        (
            "Haha. I might do an\x01",
            "independence anniversary sale\x01",
            "at our store in the future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75D7")

    label("loc_6F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_70A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FD3")

    ChrTalk(
        0xFE,
        (
            "Did you hear about it too?\x01",
            "They say the attack the other\x01",
            "day was an Imperial plot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really can't forgive\x01",
            "the Empire.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_709F")

    label("loc_6FD3")


    ChrTalk(
        0xFE,
        (
            "Because of what happened, I finally understand...\x01",
            "Even if we went along with the Empire, they'd\x01",
            "have no intentions of protecting us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's exactly why we\x01",
            "can only carry out the\x01",
            "independence.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_709F")

    Jump("loc_75D7")

    label("loc_70A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_721C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_717E")

    ChrTalk(
        0xFE,
        (
            "No way... To think he\x01",
            "caused this whole\x01",
            "incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish the CGF would do\x01",
            "something about it,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Won't we have to worry\x01",
            "about the strength of the\x01",
            "major powers pretty soon?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7217")

    label("loc_717E")


    ChrTalk(
        0xFE,
        (
            "But because of the influence of the\x01",
            "independence proposal, relations\x01",
            "with major powers have soured...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm... Just what are we\x01",
            "going to do now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7217")

    Jump("loc_75D7")

    label("loc_721C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_722A")
    Jump("loc_75D7")

    label("loc_722A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_72C3")

    ChrTalk(
        0xFE,
        (
            "Come to think of it... A\x01",
            "citizen's forum will be held\x01",
            "at City Meeting Hall tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I think I'll go\x01",
            "there for information.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75D7")

    label("loc_72C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_73D5")

    ChrTalk(
        0xFE,
        (
            "It might be sentimental of\x01",
            "me to say, but I of course\x01",
            "support our independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, the problem is how\x01",
            "we can be safe against the\x01",
            "threat of the major powers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'd be nice if we could open\x01",
            "talks, but I don't think it's\x01",
            "going to be that easy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75D7")

    label("loc_73D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7451")

    ChrTalk(
        0xFE,
        (
            "Should Crossbell be independent or\x01",
            "not? No matter how many times I think\x01",
            "about it, it's a tough problem.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75D7")

    label("loc_7451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7525")

    ChrTalk(
        0xFE,
        (
            "Because Mayor Dieter and Chairman\x01",
            "MacDowell are at the main session, I'm\x01",
            "sure Crossbell will reap rewards from it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, the future of Crossbell's\x01",
            "economy is looking brighter\x01",
            "and brighter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75D7")

    label("loc_7525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_75D7")

    ChrTalk(
        0xFE,
        (
            "Even though I saw the\x01",
            "unveiling ceremony from\x01",
            "here, I enjoyed it plenty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter where you see it in\x01",
            "Crossbell, it's a building of\x01",
            "a truly impressive scale.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75D7")

    TalkEnd(0xFE)
    Return()

    # Function_28_6ED4 end

    def Function_29_75DB(): pass

    label("Function_29_75DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_75EC")
    Jump("loc_78FD")

    label("loc_75EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7641")

    ChrTalk(
        0xFE,
        (
            "He did bad things to\x01",
            "everyone... This "empire"\x01",
            "is a bad guy, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78FD")

    label("loc_7641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_769F")

    ChrTalk(
        0xFE,
        (
            "Papa's been like this\x01",
            "ever since yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want him to cheer\x01",
            "up...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78FD")

    label("loc_769F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_76AD")
    Jump("loc_78FD")

    label("loc_76AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7730")

    ChrTalk(
        0xFE,
        (
            "Tomorrow, everyone's going\x01",
            "to talk about independence\x01",
            "at City Meeting Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, adults are cool,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78FD")

    label("loc_7730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_77B1")

    ChrTalk(
        0xFE,
        (
            "Hmm~. I don't really get\x01",
            "it, but why can't our\x01",
            "neighbors get along?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is this one of those\x01",
            ""adult things"?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78FD")

    label("loc_77B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7827")

    ChrTalk(
        0xFE,
        (
            "They say there's a lot\x01",
            "of good and bad things\x01",
            "about independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I don't really get\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78FD")

    label("loc_7827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7893")

    ChrTalk(
        0xFE,
        (
            "Today is the main\x01",
            "session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think everyone's going\x01",
            "to gather and talk about\x01",
            "stuff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78FD")

    label("loc_7893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_78FD")

    ChrTalk(
        0xFE,
        (
            "The curtain went\x01",
            "*woosh*, and then the\x01",
            "fireworks went *bam*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It was like a festival!\x02",
    )

    CloseMessageWindow()

    label("loc_78FD")

    TalkEnd(0xFE)
    Return()

    # Function_29_75DB end

    def Function_30_7901(): pass

    label("Function_30_7901")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7933")

    ChrTalk(
        0xFE,
        (
            "Hehe. Today is a happy\x01",
            "day!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A21")

    label("loc_7933")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7A21")

    ChrTalk(
        0xFE,
        (
            "They're having a charity event at City\x01",
            "Meeting Hall, but there are a lot of\x01",
            "different events and it's a lot of fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And the best part is that enjoying myself\x01",
            "there will aid the reconstruction... The\x01",
            "concept is amazing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A21")

    TalkEnd(0xFE)
    Return()

    # Function_30_7901 end

    def Function_31_7A25(): pass

    label("Function_31_7A25")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7A36")
    Jump("loc_7B21")

    label("loc_7A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7B21")

    ChrTalk(
        0xFE,
        (
            "They say the Crossbell\x01",
            "Merchants Association\x01",
            "planned this event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. They even think about the Anniversary Festival\x01",
            "every year. The Merchants Association are good\x01",
            "people who make things exciting and full of vigor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B21")

    TalkEnd(0xFE)
    Return()

    # Function_31_7A25 end

    def Function_32_7B25(): pass

    label("Function_32_7B25")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The citizens' enthusiasm\x01",
            "is ridiculous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This might be a development\x01",
            "everyone wanted from the\x01",
            "bottom of their hearts.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_7B25 end

    def Function_33_7BAD(): pass

    label("Function_33_7BAD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Order won't be restored\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We should remove the\x01",
            "screen cars soon.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_7BAD end

    def Function_34_7C08(): pass

    label("Function_34_7C08")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "President Dieter made a\x01",
            "wonderful decision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is the happiest\x01",
            "thing to occur in all of\x01",
            "Crossbell's long history.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_7C08 end

    def Function_35_7C8D(): pass

    label("Function_35_7C8D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, Goddess. Please\x01",
            "watch over Crossbell's\x01",
            "future...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_7C8D end

    def Function_36_7CCE(): pass

    label("Function_36_7CCE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "C'mon. You guys too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell State\x01",
            "independence! Hooray!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_7CCE end

    def Function_37_7D1A(): pass

    label("Function_37_7D1A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The President's address\x01",
            "was wonderful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, Crossbell will\x01",
            "become even more\x01",
            "beautiful!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_7D1A end

    def Function_38_7D82(): pass

    label("Function_38_7D82")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Ehehe, everyone looks so\x01",
            "happy.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_7D82 end

    def Function_39_7DAE(): pass

    label("Function_39_7DAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7E89")

    ChrTalk(
        0xFE,
        (
            "You can enjoy all sorts\x01",
            "of sounds on rainy days,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On water, on umbrellas, on the ground...\x01",
            "Depending on where rain lands, the sound is\x01",
            "different. It's like it's own little orchestra.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F3D")

    label("loc_7E89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7F3D")

    ChrTalk(
        0xFE,
        (
            "I have frizzy hair, but... On\x01",
            "rainy days, it's a good feeling\x01",
            "having it settled down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I love rainy\x01",
            "days... Oh, sorry for this\x01",
            "pointless conversation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F3D")

    TalkEnd(0xFE)
    Return()

    # Function_39_7DAE end

    def Function_40_7F41(): pass

    label("Function_40_7F41")

    EventBegin(0x0)
    SoundLoad(445)
    Fade(500)
    OP_4B(0x9, 0xFF)
    OP_4B(0x14, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x16, 0xFF)
    OP_4B(0x17, 0xFF)
    OP_4B(0x18, 0xFF)
    OP_4B(0x19, 0xFF)
    OP_4B(0x1A, 0xFF)
    OP_68(10760, 4740, 5470, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10000, 0)
    OP_93(0xE, 0x5A, 0x0)
    OP_93(0x19, 0x5A, 0x0)
    SetChrPos(0x101, 5150, 2500, 9860, 90)
    SetChrPos(0x102, 4000, 2500, 11070, 90)
    SetChrPos(0x104, 4740, 2500, 7860, 90)
    SetChrPos(0x103, 3500, 2500, 9070, 90)
    OP_0D()
    Sound(445, 2, 40, 0)

    ChrTalk(
        0x11,
        (
            "T-That speech was\x01",
            "amazing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#6PTo think he'd declare\x01",
            "Crossbell's\x01",
            "independence...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#6PAnd, to think he'd talk\x01",
            "about the Empire and\x01",
            "Republic like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12PA "secret feud" between the\x01",
            "major powers? Could that\x01",
            "accident back then have been...?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Citizen",
        (
            "#12PThat Empire and\x01",
            "Republic!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#6P...Was there a person\x01",
            "who spoke like that for\x01",
            "Crossbell before now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Crossbell's politicians\x01",
            "were all domesticated\x01",
            "fools...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "If we had upstanding\x01",
            "people like Chairman\x01",
            "MacDowell though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#6PIndeed, there have been\x01",
            "none with this much\x01",
            "power!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Citizen",
        (
            "#6PAnd what's more, he said\x01",
            "Crossbell's guardian deity\x01",
            "Arios is Secretary of Defense!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PI can think of none better.\x01",
            "With him at the helm\x01",
            "protecting Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12PYes, we'll have nothing\x01",
            "to fear!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Crossbell independence\x01",
            "might not be a pipe\x01",
            "dream after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#6PMayor Dieter, no, President...\x01",
            "If we leave it to him, I'm\x01",
            "sure it'll be all right!\x02",
        )
    )

    CloseMessageWindow()
    OP_25(0x1BD, 0x3C)

    NpcTalk(
        0xD,
        "Citizen",
        (
            "#12PYeah, if we have him, we\x01",
            "needn't fear the Empire,\x01",
            "nor the Republic!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#6PPresident Dieter!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Citizen",
        "#6PPresident Dieter!\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x16,
        (
            "#5SPresident Dieter,\x01",
            "hooray!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Citizens")

    AnonymousTalk(
        0xFF,
        (
            "#5SPresident Dieter,\x01",
            "hooray!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_25(0x1BD, 0x50)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0xF,
        (
            "#5SPresident Dieter,\x01",
            "hooray!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Citizens")

    AnonymousTalk(
        0xFF,
        (
            "#5S#6PPresident Dieter,\x01",
            "hooray!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x14, 0xE1, 0x1F4)
    Sleep(50)
    OP_93(0x15, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x14, 0xB4, 0x1F4)
    Sleep(50)
    OP_93(0x15, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0x14, 0xE1, 0x1F4)
    Sleep(50)
    OP_93(0x15, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x14, 0xB4, 0x1F4)
    Sleep(50)
    OP_93(0x15, 0x0, 0x1F4)
    Sleep(300)
    OP_93(0x14, 0x10E, 0x1F4)
    Sleep(50)
    OP_93(0x15, 0x10E, 0x1F4)
    Sleep(100)
    OP_64(0x14)
    OP_64(0x15)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Citizens")

    AnonymousTalk(
        0xFF,
        (
            "#5SPresident Dieter,\x01",
            "hooray!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetChrName("Citizens")

    AnonymousTalk(
        0xFF,
        (
            "#5SPresident Dieter,\x01",
            "hooray!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(3730, 4740, 8080, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10000, 0)
    Fade(500)
    OP_0D()
    OP_25(0x1BD, 0x32)
    Sleep(500)
    OP_25(0x1BD, 0x1E)

    ChrTalk(
        0x101,
        (
            "#6P#00005F...They're really going\x01",
            "at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FYes... I understand how\x01",
            "they feel, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201FIf they get too fired\x01",
            "up, there could be\x01",
            "trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FWell, the State Guard is\x01",
            "here. They'll have it under\x01",
            "control before long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001F...Anyway, let's go.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    StopSound(445, 1000, 30)
    OP_93(0xE, 0x0, 0x0)
    OP_93(0x19, 0xB4, 0x0)
    SetChrPos(0x0, 6520, 2490, 7410, 90)
    OP_4C(0x9, 0xFF)
    OP_4C(0x14, 0xFF)
    OP_4C(0x15, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x16, 0xFF)
    OP_4C(0x17, 0xFF)
    OP_4C(0x18, 0xFF)
    OP_4C(0x19, 0xFF)
    OP_4C(0x1A, 0xFF)
    SetScenarioFlags(0x18E, 4)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_40_7F41 end

    def Function_41_8855(): pass

    label("Function_41_8855")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    SoundLoad(803)
    OP_68(-17770, 3700, 27070, 0)
    MoveCamera(33, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -18000, 2500, 27800, 180)
    SetChrPos(0x102, -18000, 2500, 25600, 0)
    SetChrPos(0x109, -19200, 2500, 26700, 90)
    SetChrPos(0x105, -16800, 2500, 26700, 270)
    EndChrThread(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetCameraDistance(17500, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(803, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_898D():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_898D)
    Sleep(50)

    def lambda_899D():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_899D)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(802, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#5P#00005FOh, is that chief?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FIt's about time he\x01",
            "called.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x7)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sound(2084, 255, 100, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00000FSpecial Support Section,\x01",
            "Lloyd Bannings speaking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hey, nice work.\x02\x03",
            "As we discussed this morning,\x01",
            "it's time for you to come to\x01",
            "the police academy.\x02\x03",
            "You know the place, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00004FYes, of course.\x02\x03",
            "#00000FIt's past the gate\x01",
            "halfway down West\x01",
            "Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh yeah, I left the gate\x01",
            "open for you.\x02\x03",
            "By the way... You've\x01",
            "finished patrolling the\x01",
            "city, right?\x02\x03",
            "Honestly, how do things\x01",
            "look?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011FAh...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003F...Right.\x02\x03",
            "#00001FFor various reasons, I\x01",
            "get the feeling\x01",
            "something will happen.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You should sharpen that\x01",
            "intuition of yours.\x01",
            "You'll need it.\x02\x03",
            "Well then, I'll be\x01",
            "waiting.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#00000FUnderstood.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(813, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x6)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#00100FSo it was chief after\x01",
            "all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FSounds like he said\x01",
            "something worrisome.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5P#00006FYeah. I think he's also\x01",
            "feeling the change in\x01",
            "the city.\x02\x03",
            "#00001FWe should report to him\x01",
            "about Heiyue and Lechter\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00106FRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10300FWell, are we going to\x01",
            "the police academy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00000FYeah. Let's leave via\x01",
            "the west entrance.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "West Crossbell Highway\x01",
            "can now be selected from\x01",
            "the Crossbell City Map.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, -18000, 2500, 27800, 180)
    OP_69(0xFF, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 8370, 2390, -14850, 90)
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    SetScenarioFlags(0x126, 5)
    OP_29(0xA1, 0x1, 0x4)
    OP_24(0x323)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_41_8855 end

    def Function_42_901C(): pass

    label("Function_42_901C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51231.itc", 0x1E)
    SoundLoad(835)
    SoundLoad(821)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0x41, 0x1E)
    SetChrSubChip(0x41, 0x0)
    ClearChrFlags(0x41, 0x80)
    SetChrFlags(0x41, 0x8000)
    SetChrChipByIndex(0x42, 0x1E)
    SetChrSubChip(0x42, 0x0)
    ClearChrFlags(0x42, 0x80)
    SetChrFlags(0x42, 0x8000)
    SetChrChipByIndex(0x43, 0x1E)
    SetChrSubChip(0x43, 0x0)
    ClearChrFlags(0x43, 0x80)
    SetChrFlags(0x43, 0x8000)
    SetChrChipByIndex(0x44, 0x1E)
    SetChrSubChip(0x44, 0x0)
    ClearChrFlags(0x44, 0x80)
    SetChrFlags(0x44, 0x8000)
    SetChrChipByIndex(0x45, 0x1E)
    SetChrSubChip(0x45, 0x0)
    ClearChrFlags(0x45, 0x80)
    SetChrFlags(0x45, 0x8000)
    ClearChrFlags(0x32, 0x80)
    OP_78(0x7, 0x32)
    OP_49()
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    ClearChrFlags(0x33, 0x80)
    OP_78(0x8, 0x33)
    OP_49()
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    ClearChrFlags(0x34, 0x80)
    OP_78(0x9, 0x34)
    OP_49()
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    ClearChrFlags(0x35, 0x80)
    OP_78(0xA, 0x35)
    OP_49()
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    ClearChrFlags(0x36, 0x80)
    OP_78(0xF, 0x36)
    OP_49()
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    SetMapObjFrame(0xF, "light", 0x0, 0x1)
    ClearChrFlags(0x37, 0x80)
    OP_78(0x10, 0x37)
    OP_49()
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x1000)
    SetMapObjFrame(0x10, "light", 0x0, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x41, 10700, 2460, 7850, 225)
    SetChrPos(0x42, 6400, 2500, 10900, 225)
    SetChrPos(0x43, 2950, 2490, 15000, 225)
    SetChrPos(0x44, 1300, 2500, 7350, 45)
    SetChrPos(0x45, 2900, 2500, 5750, 45)
    SetChrPos(0x32, 15000, 2400, 8750, 0)
    OP_D5(0x32, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x33, 4550, 2400, 1400, 315)
    OP_D5(0x33, 0x0, 0x4CE78, 0x0, 0x0)
    SetChrPos(0x34, -2850, 2400, 8850, 315)
    OP_D5(0x34, 0x0, 0x4CE78, 0x0, 0x0)
    SetChrPos(0x35, 22500, 2500, -350, 270)
    OP_D5(0x35, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x36, 32500, 2500, -350, 270)
    OP_D5(0x36, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x37, 45000, 2500, -350, 270)
    OP_D5(0x37, 0x0, 0x41EB0, 0x0, 0x0)
    BeginChrThread(0x35, 1, 0, 43)
    BeginChrThread(0x36, 1, 0, 43)
    BeginChrThread(0x37, 1, 0, 43)
    OP_68(6450, 4000, 6050, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18500, 0)
    OP_68(1350, 4000, 11150, 9000)
    MoveCamera(40, 20, 0, 9000)
    Sound(835, 2, 100, 0)
    Sound(821, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(458, 0, 100, 0)
    Sleep(4000)
    Sound(494, 0, 60, 0)
    Sleep(2000)
    StopSound(835, 1000, 100)
    StopSound(821, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_901C end

    def Function_43_9380(): pass

    label("Function_43_9380")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 17150, 2500, 450)
    OP_9F(0x1, 4400, 2500, 8350)
    OP_9F(0x1, -4000, 2500, 21250)
    OP_9F(0x1, -5850, 2500, 32500)
    OP_9F(0x2, 0xFE, 5500, 0x6)
    Return()

    # Function_43_9380 end

    def Function_44_93C6(): pass

    label("Function_44_93C6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28000.itc", 0x23)
    LoadChrToIndex("chr/ch27600.itc", 0x24)
    ClearChrFlags(0x32, 0x80)
    OP_78(0xE, 0x32)
    OP_49()
    SetChrPos(0x32, 6200, 2500, 12300, 315)
    OP_D5(0x32, 0x0, 0x4CE78, 0x0, 0x0)
    SetMapObjFlags(0xE, 0x1000)
    ClearMapObjFlags(0xE, 0x4)
    OP_74(0xE, 0x1E)
    OP_70(0xE, 0x6)
    SetChrPos(0x0, 21600, 2500, 5700, 0)
    SetChrPos(0x1, 21600, 2500, 5700, 0)
    SetChrPos(0x2, 21600, 2500, 5700, 0)
    SetChrPos(0x3, 21600, 2500, 5700, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x10)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    OP_4B(0x14, 0xFF)
    SetChrChipByIndex(0x14, 0xD)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -3700, 2500, 16900, 135)
    OP_4B(0x15, 0xFF)
    SetChrChipByIndex(0x15, 0xE)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -4000, 2500, 18100, 135)
    SetChrChipByIndex(0x39, 0x0)
    SetChrSubChip(0x39, 0x0)
    ClearChrFlags(0x39, 0x80)
    SetChrFlags(0x39, 0x8000)
    SetChrPos(0x39, 4200, 2500, 6700, 45)
    SetChrChipByIndex(0x3A, 0x1)
    SetChrSubChip(0x3A, 0x0)
    ClearChrFlags(0x3A, 0x80)
    SetChrFlags(0x3A, 0x8000)
    SetChrPos(0x3A, 3000, 2500, 6900, 45)
    SetChrChipByIndex(0x3B, 0x2)
    SetChrSubChip(0x3B, 0x0)
    ClearChrFlags(0x3B, 0x80)
    SetChrFlags(0x3B, 0x8000)
    SetChrPos(0x3B, 3000, 2500, 8500, 45)
    SetChrChipByIndex(0x3C, 0x23)
    SetChrSubChip(0x3C, 0x0)
    ClearChrFlags(0x3C, 0x80)
    SetChrFlags(0x3C, 0x8000)
    SetChrPos(0x3C, 2400, 2500, 9200, 45)
    SetChrChipByIndex(0x3D, 0x24)
    SetChrSubChip(0x3D, 0x0)
    ClearChrFlags(0x3D, 0x80)
    SetChrFlags(0x3D, 0x8000)
    SetChrPos(0x3D, 1200, 2500, -2400, 0)
    SetChrChipByIndex(0x3E, 0x9)
    SetChrSubChip(0x3E, 0x0)
    ClearChrFlags(0x3E, 0x80)
    SetChrFlags(0x3E, 0x8000)
    SetChrPos(0x3E, 2900, 2500, -2300, 0)
    SetChrChipByIndex(0x3F, 0xA)
    SetChrSubChip(0x3F, 0x0)
    ClearChrFlags(0x3F, 0x80)
    SetChrFlags(0x3F, 0x8000)
    SetChrPos(0x3F, -7200, 2500, 6400, 90)
    SetChrChipByIndex(0x40, 0xF)
    SetChrSubChip(0x40, 0x0)
    ClearChrFlags(0x40, 0x80)
    SetChrFlags(0x40, 0x8000)
    SetChrPos(0x40, -2400, 2500, 3400, 45)
    OP_68(6700, 4000, 11200, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    OP_68(5700, 3500, 10200, 10000)
    MoveCamera(45, 17, 0, 10000)
    SetCameraDistance(18000, 10000)
    BeginChrThread(0x32, 3, 0, 45)
    BeginChrThread(0x14, 3, 0, 46)
    BeginChrThread(0x15, 3, 0, 47)
    OP_63(0x39, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, 120, -1, -1)
    SetChrName("Chairman MacDowell")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W─Of course, each of you has your own opinion\x01",
            "on the legality of this situation!\x02\x03",
            "However, the fact that the current\x01",
            "government did not come to power via the\x01",
            "democratic process is the absolute truth!\x02\x03",
            "With many congresspeople and even myself\x01",
            "imprisoned, Crossbell independence was\x01",
            "declared!\x02\x03",
            "I would like to once again point out that\x01",
            "this declaration was made individually and\x01",
            "arbitrarily, without going through congress.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("c1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_93C6 end

    def Function_45_98A2(): pass

    label("Function_45_98A2")

    Sleep(2000)

    def lambda_98AA():
        OP_96(0xFE, 0xAF0, 0x9C4, 0x11F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_98AA)
    Sleep(500)

    def lambda_98C7():
        OP_96(0xFE, 0xFFFFFF38, 0x9C4, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_98C7)
    Sleep(500)

    def lambda_98E4():
        OP_96(0xFE, 0x384, 0x9C4, 0x1A2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x40, 1, lambda_98E4)
    Sleep(500)

    def lambda_9901():
        OP_96(0xFE, 0x1194, 0x9C4, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_9901)
    WaitChrThread(0x3D, 1)
    OP_63(0x3D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x40, 1)
    OP_63(0x40, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x3E, 1)
    Return()

    # Function_45_98A2 end

    def Function_46_9959(): pass

    label("Function_46_9959")

    Sleep(8000)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_9973():
        OP_96(0xFE, 0x8FC, 0x9C4, 0x2AF8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9973)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1100)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_46_9959 end

    def Function_47_999E(): pass

    label("Function_47_999E")

    Sleep(8200)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_99B8():
        OP_96(0xFE, 0x7D0, 0x9C4, 0x2FA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_99B8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_47_999E end

    def Function_48_99D9(): pass

    label("Function_48_99D9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    LoadChrToIndex("apl/ch51719.itc", 0x14)
    LoadChrToIndex("apl/ch51718.itc", 0x15)
    LoadChrToIndex("chr/ch32050.itc", 0x16)
    LoadChrToIndex("chr/ch32051.itc", 0x17)
    LoadChrToIndex("chr/ch32056.itc", 0x19)
    LoadChrToIndex("chr/ch32150.itc", 0x1A)
    LoadChrToIndex("chr/ch32151.itc", 0x1B)
    LoadChrToIndex("chr/ch32152.itc", 0x1C)
    LoadChrToIndex("monster/ch85150.itc", 0x1D)
    LoadChrToIndex("monster/ch85151.itc", 0x1E)
    LoadChrToIndex("monster/ch85153.itc", 0x1F)
    LoadEffect(0x0, "event/ev17034.eff")
    LoadEffect(0x1, "event/ev17061.eff")
    LoadEffect(0x2, "battle\\cr313000.eff")
    LoadEffect(0x3, "battle\\ms00001.eff")
    LoadEffect(0x4, "battle\\ms00000.eff")
    LoadEffect(0x5, "event/eva01_01.eff")
    LoadEffect(0x7, "battle\\mg042_00.eff")
    SoundLoad(123)
    SetChrPos(0x0, 21600, 2500, 5700, 0)
    SetChrPos(0x1, 21600, 2500, 5700, 0)
    SetChrPos(0x2, 21600, 2500, 5700, 0)
    SetChrPos(0x3, 21600, 2500, 5700, 0)
    SetChrChipByIndex(0x27, 0x14)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, -4500, 2500, 20500, 0)
    SetChrChipByIndex(0x28, 0x15)
    SetChrSubChip(0x28, 0x0)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, -4800, 2500, 20000, 0)
    SetChrChipByIndex(0x29, 0x16)
    SetChrSubChip(0x29, 0x0)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, -7500, 2500, 20000, 0)
    SetChrChipByIndex(0x2A, 0x1A)
    SetChrSubChip(0x2A, 0x0)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, -8000, 2500, 20500, 0)
    SetChrChipByIndex(0x25, 0x1D)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    OP_52(0x25, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x26, 0x1D)
    SetChrSubChip(0x26, 0x0)
    SetChrFlags(0x26, 0x8000)
    OP_52(0x26, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x32, 0x80)
    OP_78(0x7, 0x32)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x32, 18500, 2500, 700, 295)
    OP_D5(0x32, 0x0, 0x48058, 0x0, 0x0)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0xB5, 0xF0, 0x0, 0x20)
    ClearChrFlags(0x33, 0x80)
    OP_78(0x11, 0x33)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x33, 10700, 2500, 4300, 300)
    OP_D5(0x33, 0x0, 0x493E0, 0x0, 0x0)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x11, 0x1000)
    OP_74(0x11, 0x1E)
    OP_71(0x11, 0xB5, 0xF0, 0x0, 0x20)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1KThe same day, 10:30──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    PlayBGM("ed7573", 0)
    OP_68(8000, 5000, 10500, 0)
    MoveCamera(50, 3, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(40000, 0)
    OP_68(4000, 5000, 10500, 7000)
    MoveCamera(40, 5, 0, 7000)
    SetCameraDistance(43000, 7000)
    Sound(123, 2, 30, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    StopSound(123, 500, 40)
    Fade(500)
    OP_68(-6100, 4300, 34500, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16500, 0)
    SetCameraDistance(15500, 5000)
    OP_6F(0x79)
    StopBGM(0xFA0)
    OP_4B(0x25, 0xFF)
    BeginChrThread(0x25, 3, 0, 55)
    Sleep(400)
    OP_4B(0x26, 0xFF)
    BeginChrThread(0x26, 3, 0, 55)
    BeginChrThread(0x46, 1, 0, 57)
    Sound(825, 2, 40, 0)
    PlayEffect(0x7, 0x0, 0xFF, 0x0, -6100, 2500, 34500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1388)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    SetChrChipByIndex(0x25, 0x1F)
    SetChrSubChip(0x25, 0x0)
    OP_52(0x25, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_9DE1():
        OP_A6(0xFE, 0x0, 0x64, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_9DE1)
    SetChrChipByIndex(0x26, 0x1F)
    SetChrSubChip(0x26, 0x0)
    OP_52(0x26, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_9E0D():
        OP_A6(0xFE, 0x0, 0x64, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_9E0D)
    Sleep(4500)
    EndChrThread(0x46, 0x1)
    StopSound(825, 1500, 40)
    CancelBlur(500)
    Sleep(500)
    SetChrChipByIndex(0x25, 0x1D)
    SetChrSubChip(0x25, 0x0)
    OP_52(0x25, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x26, 0x1D)
    SetChrSubChip(0x26, 0x0)
    OP_52(0x26, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Fade(250)
    OP_68(-5500, 3500, 28500, 0)
    MoveCamera(35, 15, 10, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    OP_68(-5500, 3700, 34000, 2000)
    MoveCamera(43, 15, 10, 2000)
    SetCameraDistance(14500, 2000)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x28, 0x80)
    BeginChrThread(0x29, 3, 0, 49)
    Sleep(300)
    BeginChrThread(0x28, 3, 0, 50)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7544", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x220), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x29, 3)
    WaitChrThread(0x28, 3)
    WaitChrThread(0x25, 3)
    WaitChrThread(0x26, 3)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x27, 0x80)
    BeginChrThread(0x27, 3, 0, 52)
    Sleep(300)
    BeginChrThread(0x2A, 3, 0, 51)
    WaitChrThread(0x27, 3)
    OP_6F(0x79)

    ChrTalk(
        0x27,
        "Clear!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x2A, 3)
    OP_93(0x2A, 0x87, 0x1F4)

    ChrTalk(
        0x2A,
        "#5PNow!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-300, 4000, 13000, 0)
    MoveCamera(100, 31, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    SetChrPos(0x27, -3500, 2500, 30500, 0)
    SetChrPos(0x28, -3800, 2500, 32000, 0)

    def lambda_9F91():

        label("loc_9F91")

        TurnDirection(0xFE, 0x33, 500)
        Yield()
        Jump("loc_9F91")

    QueueWorkItem2(0x2A, 2, lambda_9F91)
    OP_68(-6100, 5000, 33000, 3700)
    MoveCamera(25, 21, 0, 3700)
    SetCameraDistance(15000, 3700)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    BeginChrThread(0x33, 3, 0, 56)
    Sleep(300)
    BeginChrThread(0x32, 3, 0, 56)
    BeginChrThread(0x46, 1, 0, 58)
    WaitChrThread(0x32, 3)
    EndChrThread(0x2A, 0x2)
    ClearChrFlags(0x29, 0x4)
    SetChrChipByIndex(0x29, 0x17)
    SetChrSubChip(0x29, 0x0)

    def lambda_9FFE():
        OP_95(0xFE, -7500, 4700, 47500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_9FFE)
    Sleep(50)
    ClearChrFlags(0x28, 0x4)

    def lambda_A020():
        OP_95(0xFE, -4500, 4700, 47500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_A020)
    Sleep(50)
    ClearChrFlags(0x27, 0x4)

    def lambda_A042():
        OP_95(0xFE, -4500, 4700, 47500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_A042)
    Sleep(50)
    ClearChrFlags(0x2A, 0x4)
    SetChrChipByIndex(0x2A, 0x1B)
    SetChrSubChip(0x2A, 0x0)

    def lambda_A06C():
        OP_95(0xFE, -7500, 4700, 47500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_A06C)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    SetScenarioFlags(0x22, 7)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_48_99D9 end

    def Function_49_A0A2(): pass

    label("Function_49_A0A2")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0x29, 0x17)
    SetChrSubChip(0x29, 0x0)

    def lambda_A0C2():
        OP_96(0xFE, 0xFFFFE2B4, 0x9C4, 0x6978, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A0C2)

    ChrTalk(
        0x29,
        "#9AHaaaaa!\x02",
    )

    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x29, 0x19)
    SetChrSubChip(0x29, 0x2)
    Sound(251, 0, 60, 0)

    def lambda_A0FD():
        OP_9D(0xFE, 0xFFFFE2B4, 0xDAC, 0x80E8, 0x5DC, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A0FD)
    WaitChrThread(0xFE, 1)
    Sound(815, 0, 100, 0)
    SetChrSubChip(0x29, 0x3)
    BeginChrThread(0x26, 3, 0, 54)
    Sleep(1000)
    SetChrSubChip(0x29, 0x4)

    def lambda_A135():
        OP_9D(0xFE, 0xFFFFE2B4, 0x9C4, 0x7D00, 0xC8, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A135)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x29, 0x16)
    SetChrSubChip(0x29, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_49_A0A2 end

    def Function_50_A162(): pass

    label("Function_50_A162")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)

    def lambda_A17A():
        OP_96(0xFE, 0xFFFFED40, 0x9C4, 0x6D60, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A17A)
    Sleep(500)

    ChrTalk(
        0x28,
        "#9AOooooo!\x02",
    )

    WaitChrThread(0xFE, 1)
    Sound(844, 0, 70, 0)

    def lambda_A1B0():
        OP_9D(0xFE, 0xFFFFED40, 0x9C4, 0x7DC8, 0x384, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A1B0)
    Sound(532, 0, 100, 0)
    SetChrSubChip(0xFE, 0x6)
    Sleep(500)
    Sound(538, 0, 50, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x3, 0, 0, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x7)
    WaitChrThread(0xFE, 1)
    Sound(246, 0, 100, 0)
    Sound(196, 0, 70, 0)
    BeginChrThread(0x25, 3, 0, 53)
    Sleep(1000)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrSubChip(0xFE, 0x5)
    Return()

    # Function_50_A162 end

    def Function_51_A23C(): pass

    label("Function_51_A23C")

    SetChrChipByIndex(0x2A, 0x1B)
    SetChrSubChip(0x2A, 0x0)

    def lambda_A249():
        OP_96(0xFE, 0xFFFFE0C0, 0x9C4, 0x7724, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A249)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x2A, 0x1A)
    SetChrSubChip(0x2A, 0x0)
    Return()

    # Function_51_A23C end

    def Function_52_A26B(): pass

    label("Function_52_A26B")


    def lambda_A270():
        OP_96(0xFE, 0xFFFFEE6C, 0x9C4, 0x7724, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A270)
    WaitChrThread(0xFE, 1)
    Sound(531, 0, 50, 0)
    SetChrSubChip(0xFE, 0x5)
    Return()

    # Function_52_A26B end

    def Function_53_A294(): pass

    label("Function_53_A294")

    OP_82(0xFA, 0xFA, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_A2CE():
        OP_A6(0xFE, 0x0, 0x64, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A2CE)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1700, -500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x0, 0, 1700, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    PlayEffect(0x1, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_A393():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A393)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_53_A294 end

    def Function_54_A3A7(): pass

    label("Function_54_A3A7")

    OP_82(0xFA, 0xFA, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(501, 0, 100, 0)

    def lambda_A3E7():
        OP_A6(0xFE, 0x0, 0x64, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A3E7)
    PlayEffect(0x4, 0xFF, 0xFE, 0x0, 0, 1700, -300, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    MoveCamera(43, 15, 5, 4000)
    SetCameraDistance(16000, 4000)
    Sound(985, 0, 100, 0)
    PlayEffect(0x1, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_A48F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A48F)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_54_A3A7 end

    def Function_55_A4A3(): pass

    label("Function_55_A4A3")

    Sound(530, 0, 50, 0)
    Sound(567, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 2850, -15000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_82(0xFA, 0xFA, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_A523():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A523)
    Sound(501, 0, 50, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 2850, 200, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x0, 0, 2850, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x1D)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_55_A4A3 end

    def Function_56_A5C3(): pass

    label("Function_56_A5C3")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 3100, 2500, 10400)
    OP_9F(0x1, -3900, 2500, 20900)
    OP_9F(0x1, -5600, 2500, 35700)
    OP_9F(0x2, 0xFE, 10000, 0x6)

    def lambda_A5FF():
        OP_96(0xFE, 0xFFFFEA20, 0x1D4C, 0xED1C, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A5FF)
    OP_D5(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1F4)
    Return()

    # Function_56_A5C3 end

    def Function_57_A628(): pass

    label("Function_57_A628")

    Sleep(500)
    Sound(207, 0, 60, 0)
    Sleep(1000)

    label("loc_A634")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A656")
    Sound(246, 0, 70, 0)
    Sleep(300)
    Sound(246, 0, 60, 0)
    Sleep(400)
    Jump("loc_A634")

    label("loc_A656")

    Return()

    # Function_57_A628 end

    def Function_58_A657(): pass

    label("Function_58_A657")

    Sound(458, 0, 100, 0)
    Sound(486, 0, 100, 0)
    Sleep(2000)
    Sound(487, 0, 100, 0)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Return()

    # Function_58_A657 end

    def Function_59_A67C(): pass

    label("Function_59_A67C")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FIt seems the "State Guard"\x01",
            "are fiercely guarding the\x01",
            "Orchis Tower area.\x02\x03",
            "#00003F...Let's not go there.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -5600, 2500, 34230, 180)
    EventEnd(0x4)
    Return()

    # Function_59_A67C end

    def Function_60_A706(): pass

    label("Function_60_A706")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch44100.itc", 0x14)
    LoadChrToIndex("chr/ch47500.itc", 0x15)
    LoadChrToIndex("chr/ch23600.itc", 0x16)
    LoadChrToIndex("chr/ch30600.itc", 0x17)
    LoadChrToIndex("chr/ch30000.itc", 0x18)
    LoadEffect(0x6, "event\\eva04_00.eff")
    SoundLoad(975)
    SetChrPos(0x101, 18940, 2500, -19860, 180)
    SetChrPos(0x102, 19960, 2500, -18870, 180)
    SetChrPos(0x109, 17860, 2500, -18930, 180)
    SetChrPos(0x105, 19210, 2500, -18160, 180)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0x38, 0x80)
    SetChrFlags(0x38, 0x8000)
    SetMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xC, 0x4)
    OP_78(0xC, 0x38)
    SetChrPos(0x38, 19670, 2500, -22660, 0)
    OP_D5(0x38, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    OP_49()
    SetChrPos(0x36, 19940, 0, -58340, 0)
    OP_D5(0x36, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x36, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    ClearMapObjFlags(0xB, 0x4)
    OP_74(0xB, 0x1E)
    OP_78(0xB, 0x36)
    OP_71(0xB, 0xB5, 0xF0, 0x1, 0x20)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    SetChrFlags(0x32, 0x8000)
    SetChrFlags(0x33, 0x8000)
    SetChrFlags(0x34, 0x8000)
    SetChrFlags(0x35, 0x8000)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFlags(0xA, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    OP_78(0x7, 0x32)
    OP_78(0x8, 0x33)
    OP_78(0x9, 0x34)
    OP_78(0xA, 0x35)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x32, 19940, 0, -58340, 0)
    SetChrPos(0x33, 19940, 0, -58340, 0)
    SetChrPos(0x34, 14330, 2500, -18280, 135)
    SetChrPos(0x35, 20420, 2500, -12820, 180)
    OP_A7(0x32, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x33, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_D5(0x32, 0x0, 0x0, 0x0, 0x0)
    OP_D5(0x33, 0x0, 0x0, 0x0, 0x0)
    OP_D5(0x34, 0x0, 0x20F58, 0x0, 0x0)
    OP_D5(0x35, 0x0, 0x2BF20, 0x0, 0x0)
    OP_68(18610, 2750, -45640, 0)
    MoveCamera(46, 34, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(493, 0, 100, 0)
    BeginChrThread(0x36, 1, 0, 62)
    Sleep(800)
    OP_68(19110, 2750, -26510, 1500)
    MoveCamera(46, 28, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(18000, 1500)
    OP_63(0x33, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(487, 0, 100, 0)
    BeginChrThread(0x36, 3, 0, 61)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(500)

    NpcTalk(
        0x36,
        "Reggie",
        "#10AUwah!!??\x02",
    )

    CloseMessageWindow()
    OP_71(0xB, 0x5B, 0x78, 0x0, 0x0)
    WaitChrThread(0x36, 1)
    OP_6F(0x79)
    OP_0D()

    NpcTalk(
        0x36,
        "Sykes",
        (
            "Hey, hey! This wasn't\x01",
            "here when we passed by\x01",
            "last time!\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Yuri")

    NpcTalk(
        0x36,
        "Yuri",
        (
            "Tch, an improvised\x01",
            "barricade, huh...\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(18610, 2750, -45640, 0)
    MoveCamera(46, 34, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    Sound(975, 2, 100, 0)
    Sound(459, 0, 100, 0)

    def lambda_AB1F():
        OP_96(0xFE, 0x4DE4, 0x0, 0xFFFF6BE0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_AB1F)
    Sleep(1000)

    def lambda_AB3C():
        OP_96(0xFE, 0x4DE4, 0x0, 0xFFFF4CA0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_AB3C)
    OP_68(18540, 2750, -38950, 3000)
    OP_71(0x7, 0x5B, 0x78, 0x0, 0x0)
    WaitChrThread(0x32, 1)
    StopSound(975, 1000, 100)
    Sound(492, 0, 100, 0)
    OP_71(0x8, 0x5B, 0x78, 0x0, 0x0)
    WaitChrThread(0x33, 1)
    OP_6F(0x1)
    Sound(462, 0, 100, 0)
    OP_71(0x7, 0x1, 0x1E, 0x0, 0x0)
    OP_79(0x7)
    Fade(500)
    SetChrChipByIndex(0x2E, 0x17)
    SetChrChipByIndex(0xB, 0x18)
    SetChrSubChip(0x2E, 0x0)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0x2E, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0x2E, 17650, 0, -37870, 270)
    Sleep(500)
    Fade(500)
    SetChrPos(0xB, 22130, 0, -37520, 90)
    WaitChrThread(0x2E, 1)
    WaitChrThread(0xB, 1)
    BeginChrThread(0x2E, 1, 0, 63)
    Sleep(500)
    BeginChrThread(0xB, 1, 0, 64)
    OP_68(18370, 2750, -32299, 3000)
    Sleep(1000)
    Sound(461, 0, 100, 0)
    OP_71(0x7, 0x1F, 0x3C, 0x0, 0x0)
    OP_79(0x7)
    WaitChrThread(0x2E, 1)
    WaitChrThread(0xB, 1)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x105,
        "#N#10302FHehe, checkmate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#N#00000FYeah, next is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "...Alright, we finally\x01",
            "caught you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        "Surrender peacefully!\x02",
    )

    CloseMessageWindow()
    SetChrName("Sykes")

    NpcTalk(
        0x36,
        "Sykes",
        "...Well, look at you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(17170, 2750, -33200, 0)
    MoveCamera(47, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14520, 0)
    SetChrChipByIndex(0x2F, 0x14)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 17930, 230, -31970, 180)
    SetChrChipByIndex(0x30, 0x15)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x80)
    SetChrFlags(0x30, 0x8000)
    SetChrPos(0x30, 17480, 680, -30340, 180)
    SetChrChipByIndex(0x31, 0x16)
    SetChrSubChip(0x31, 0x0)
    ClearChrFlags(0x31, 0x80)
    SetChrFlags(0x31, 0x8000)
    SetChrPos(0x31, 19560, 540, -30840, 180)
    SetChrPos(0x101, 21080, 70, -32549, 270)
    SetChrPos(0x102, 21550, 390, -31400, 270)
    SetChrPos(0x109, 22460, 820, -29860, 225)
    SetChrPos(0x105, 21200, 1010, -29170, 225)
    TurnDirection(0xB, 0x2F, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7518", 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x31,
        (
            "Yeah, yeah, we\x01",
            "surrender~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "Man, looks you incompetents\x01",
            "are finally using your\x01",
            "brains for something.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2E, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x2E,
        (
            "Y-You guys... How about\x01",
            "showing some remorse,\x01",
            "eh!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "Do you know how much\x01",
            "trouble you've caused!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "Yeah, yeah, we know.\x01",
            "Don't get all excited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        (
            "If you get that mad,\x01",
            "you'll get crow's feet,\x01",
            "old lady.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x2E,
        "#4SO-Old!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "Y-You guys never change,\x01",
            "do you!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x2E, 500)
    Sleep(100)

    ChrTalk(
        0xB,
        "K-Kate, calm down...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "Oh, didn't you arrest us\x01",
            "somewhere before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "Well, you can't give us\x01",
            "any punishment anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FWhat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F............\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x2E, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00000F...Officer Kate. Anyway,\x01",
            "let's take them to HQ\x01",
            "for now.\x02\x03",
            "We can't leave their car\x01",
            "here forever, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        "Tch... You're right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2E, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x2E,
        (
            "Alright then, Special\x01",
            "Support Section. Help me\x01",
            "drag these kids to HQ.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2E, 0xB, 500)
    Sleep(100)

    ChrTalk(
        0x2E,
        (
            "Frantz, get ready to\x01",
            "remove the vehicle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Right!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x2F, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00003F............\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 2)
    NewScene("c1150", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_60_A706 end

    def Function_61_B1BC(): pass

    label("Function_61_B1BC")

    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 19800, 1410, -25000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 19270, 1410, -25000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 19800, 1410, -30710, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 19270, 1410, -30710, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 19420, 1410, -30710, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_61_B1BC end

    def Function_62_B2DC(): pass

    label("Function_62_B2DC")

    OP_96(0x36, 0x4D12, 0x0, 0xFFFF7B58, 0x3A98, 0x0)
    OP_9F(0x0, 0x36)
    OP_9F(0x1, 19500, 390, -31390)
    OP_9F(0x1, 19420, 1410, -27710)
    OP_9F(0x1, 19800, 1410, -27710)
    OP_9F(0x2, 0x36, 15000, 0x6)
    OP_D5(0x36, 0xFFFFD8F0, 0xAFC8, 0xFFFFD8F0, 0x0)
    Return()

    # Function_62_B2DC end

    def Function_63_B33B(): pass

    label("Function_63_B33B")

    OP_97(0x2E, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
    OP_95(0x2E, 18560, 10, -34510, 1000, 0x0)
    TurnDirection(0x2E, 0x101, 500)
    Return()

    # Function_63_B33B end

    def Function_64_B36B(): pass

    label("Function_64_B36B")

    OP_97(0xB, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
    OP_95(0xB, 21150, 0, -34360, 1000, 0x0)
    TurnDirection(0xB, 0x101, 500)
    Return()

    # Function_64_B36B end

    def Function_65_B39B(): pass

    label("Function_65_B39B")

    EventBegin(0x0)
    Fade(500)
    LoadEffect(0x0, "battle/it002_00.eff")
    OP_68(5880, 4740, -10040, 0)
    MoveCamera(7, 27, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(12150, 0)
    SetChrPos(0x101, 5420, 2500, -7460, 45)
    SetChrPos(0x102, 6250, 2500, -8390, 45)
    SetChrPos(0x103, 4250, 2500, -8350, 45)
    SetChrPos(0x104, 5120, 2500, -9330, 45)
    SetChrPos(0x109, 3220, 2500, -9240, 45)
    SetChrPos(0x105, 3990, 2500, -10270, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Welcome. Would you like\x01",
            "some juice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, we're from\x01",
            "the Special Support\x01",
            "Section...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that you came\x01",
            "for "gourmet\x01",
            "recommendations" coverage.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Ah, that, huh? I heard\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How about this, then.\x01",
            "It's "Acerbic Tomado\x01",
            "Soda", my latest product!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B781")

    ChrTalk(
        0x101,
        (
            "#00005FT-This is... the one you\x01",
            "make for Chairman\x01",
            "MacDowell!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes. Even though he\x01",
            "became Chairman, he still\x01",
            "orders his usual drink...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is my latest\x01",
            "product, an improved\x01",
            "version of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because the bitterness is moderated by\x01",
            "the soda, even those who dislike acerbic\x01",
            "tomatoes can enjoy it and be healthy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B874")

    label("loc_B781")


    ChrTalk(
        0x101,
        (
            "#00005FA-Acerbic tomatoes... In\x01",
            "this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's my latest product,\x01",
            "an improved version of\x01",
            "my acerbic tomato juice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because the bitterness is moderated by\x01",
            "the soda, even those who dislike acerbic\x01",
            "tomatoes can enjoy it and be healthy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B874")


    ChrTalk(
        0x102,
        "#00109FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(...Hey Lloyd. Are we\x01",
            "seriously gonna drink\x01",
            "this?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(I-It's our job, so it\x01",
            "can't be helped... Let's do\x01",
            "our best to get it down.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others\x01",
            "drank the acerbic tomato\x01",
            "soda.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    PlayEffect(0x0, 0x0, 0x101, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x102, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x103, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x104, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x4, 0x109, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x5, 0x105, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_89(0x5, 0x0)
    Sound(235, 0, 100, 0)
    OP_32(0x0, 0xF7, 0x32)
    OP_32(0x1, 0xF7, 0x32)
    OP_32(0x2, 0xF7, 0x32)
    OP_32(0x3, 0xF7, 0x32)
    OP_32(0x8, 0xF7, 0x32)
    OP_32(0x4, 0xF7, 0x32)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Everyone recovered 50\x01",
            "CP.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00010F#4S...Aaahhh!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F*cough, cough*! T-This\x01",
            "is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F...It's plenty bitter.\x02\x03",
            "#00211FThe bubbliness gives it\x01",
            "a power up, maybe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, it seems there's a\x01",
            "lot of room for\x01",
            "improvement...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Anyway, to clean your\x01",
            "palettes, have this standard\x01",
            "drink, my "Bell Berry Juice".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others\x01",
            "drank the Bell Berry\x01",
            "Juice.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00102F(*glug, glug*...) Ah,\x01",
            "it's super delicious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha. It's a sharp\x01",
            "contrast to that\x01",
            "bitterness before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(I think this one might\x01",
            "be better to introduce\x01",
            "in the guide...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x172, 4)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_BEB0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BEB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_BECD")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_BEE0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BEE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_BEF3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BEF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_BF10")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_BF23")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_BF40")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_BF53")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_BF70")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_BF83")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_BFA0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BFA0")

    OP_29(0x80, 0x1, 0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C0AB")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Finished covering 6\x01",
            "restaurants!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C0A2")

    AnonymousTalk(
        0x101,
        (
            "#00003FIt seems we could go report to\x01",
            "Grace immediately, but...\x02\x03",
            "#00000FWe haven't found all 6\x01",
            "members' favorites yet, so why\x01",
            "don't we try a little harder?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_C0A2")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_C0AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C199")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found all SSS members'\x01",
            "favorites!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this, we found all 6\x01",
            "members' favorites.\x02\x03",
            "We've got plenty of coverage with\x01",
            "this. Let's head to the news\x01",
            "agency right away and report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_C199")

    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 5330, 2500, -8020, 56)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_65_B39B end

    def Function_66_C1D3(): pass

    label("Function_66_C1D3")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "   ※ Orchis Tower Ahead ※\x01",
            "※ Authorized Personnel Only ※\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_66_C1D3 end

    def Function_67_C239(): pass

    label("Function_67_C239")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FOrchis Tower plaza should\x01",
            "be very busy today due to\x01",
            "preparations for tomorrow.\x02\x03",
            "Since we don't have any\x01",
            "business there, let's not\x01",
            "get too close.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -5600, 2500, 34230, 180)
    EventEnd(0x4)
    Return()

    # Function_67_C239 end

    def Function_68_C2ED(): pass

    label("Function_68_C2ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4FC")
    EventBegin(0x0)
    Fade(500)
    OP_68(-4500, 3240, 25730, 0)
    MoveCamera(34, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16420, 0)
    OP_E2(0x3)
    SetChrPos(0x101, -3910, 2500, 21570, 315)
    SetChrPos(0x102, -2680, 2500, 20990, 315)
    SetChrPos(0x103, -5210, 2500, 19950, 315)
    SetChrPos(0x104, -3420, 2500, 19850, 315)
    SetChrPos(0xF4, -4620, 2500, 18200, 315)
    SetChrPos(0xF5, -1960, 2500, 19500, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#12P#00101F...As expected, it\x01",
            "doesn't seem like we can\x01",
            "approach the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FFor sure. If we're spotted by\x01",
            "those things, reinforcements\x01",
            "'ll be here in no time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001F...If that happened,\x01",
            "impact to our plan\x01",
            "couldn't be avoided.\x02\x03",
            "#00003FLet's turn around before\x01",
            "we're spotted.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_E2(0x2)
    SetScenarioFlags(0x1, 4)
    EventEnd(0x5)
    Jump("loc_C584")

    label("loc_C4FC")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The path to the tower is\x01",
            "defended by magic soldiers.\x01",
            "It seems best to turn back.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -7830, 2500, 22590, 21)
    EventEnd(0x4)

    label("loc_C584")

    Return()

    # Function_68_C2ED end

    def Function_69_C585(): pass

    label("Function_69_C585")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C596")
    Jump("loc_CAF2")

    label("loc_C596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C731")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Charity Event\x01",
            ""The Circle to Spread the\x01",
            " Reconstruction With Everyone"\x01",
            "[Program Outline]\x01",
            "・Solo Piano Concert\x01",
            "・Miss Crossbell Contest\x01",
            "・Public Gourmet Contest\x01",
            "・Various Art Classes\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Location: Crossbell City Meeting Hall -\x01",
            "Multipurpose Hall\x01",
            "Plaza in front of the hall\x01",
            "Date: Today\x01",
            "Sponsor: Crossbell Merchants Association/Crossbell City\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CAF2")

    label("loc_C731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C8B9")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Civic Forum\x01",
            ""～Now is the time to think seriously\x01",
            " about the question of State\x01",
            " independence～"\x01",
            "[Program Outline]\x01",
            "・The question of state independence explained\x01",
            "by an expert\x01",
            "・Open forum with active state congressmen\x01",
            "Location: Crossbell City Hall - Multipurpose Hall\x01",
            "Date: Today\x01",
            "Sponsor: Crossbell City/Crossbell News Agency\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CAF2")

    label("loc_C8B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CA41")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Civic Forum\x01",
            ""～Now is the time to think seriously\x01",
            " about the question of State\x01",
            " independence～"\x01",
            "[Program Outline]\x01",
            "・The question of state independence explained\x01",
            "by an expert\x01",
            "・Open forum with active state congressmen\x01",
            "Location: Crossbell City Hall - Multipurpose Hall\x01",
            "Date: Today\x01",
            "Sponsor: Crossbell City/Crossbell News Agency\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CAF2")

    label("loc_CA41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_CA4F")
    Jump("loc_CAF2")

    label("loc_CA4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_CAE9")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Investing Seminar For Beginners\x01",
            ""For Reading And Understanding The Economy Of Tomorrow"\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_CAF2")

    label("loc_CAE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_CAF2")

    label("loc_CAF2")

    TalkEnd(0xFF)
    Return()

    # Function_69_C585 end

    def Function_70_CAF6(): pass

    label("Function_70_CAF6")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is tightly\x01",
            "shut.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC77")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CC1E")

    ChrTalk(
        0x101,
        (
            "#00003FPolice HQ... It seems no\x01",
            "one is inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#00603F...This place was sealed off\x01",
            "by the State Guard following\x01",
            "yesterday's martial law.\x02\x03",
            "#00600F...In any case, let's hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes... Roger that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC74")

    label("loc_CC1E")


    ChrTalk(
        0x101,
        (
            "#00003FPolice HQ... It seems no\x01",
            "one is inside.\x02\x03",
            "#00001FIn any case, let's\x01",
            "hurry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC74")

    SetScenarioFlags(0x1, 5)

    label("loc_CC77")

    TalkEnd(0xFF)
    Return()

    # Function_70_CAF6 end

    SaveToFile()

Try(main)
