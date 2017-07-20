from ScenarioHelper import *

def main():
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
        "Otto",               # 2
        "Tajik",                 # 3
        "Police investigation",           # 4
        "Zeit",               # 5
        "tourist",                 # 6
        "tourist",                 # 7
        "Citizen",                   # 8
        "boy",                 # 9
        "Citizen",                   # 10
        "Citizen",                   # 11
        "Haas",                 # 12
        "Defense Forces soldier",             # 13
        "Defense Forces soldier",             # 14
        "Citizen",                   # 15
        "Citizen",                   # 16
        "Citizen",                   # 17
        "Citizen",                   # 18
        "Citizen",                   # 19
        "Citizen",                   # 20
        "Policeman",                   # 21
        "Policeman",                   # 22
        "Policeman",                   # 23
        "Citizen",                   # 24
        "tourist",                 # 25
        "tourist",                 # 26
        "peach",                   # 27
        "Ryu",                 # 28
        "Henry",                 # 29
        "Magician",                 # 30
        "Magician",                 # 31
        "Mushroute Scott",         # 32
        "Wrestler Wenzel",     # 33
        "Zookoist Rin",             # 34
        "Friend Aolia",         # 35
        "Event monster",   # 36
        "Event monster",   # 37
        "Event monster",   # 38
        "Kate policing",             # 39
        "Yuri",                 # 40
        "Sykes",               # 41
        "Reggie",                 # 42
        "Police car",               # 43
        "Police car",               # 44
        "Police car",               # 45
        "Police car",               # 46
        "Runaway vehicle",                 # 47
        "car",                     # 48
        "sandbag",                   # 49
        "Citizen 1",                 # 50
        "Citizen 2",                 # 51
        "Citizen 3",                 # 52
        "Citizen 4",                 # 53
        "Citizen 5",                 # 54
        "Citizen 6",                 # 55
        "Citizen 7",                 # 56
        "Citizen 8",                 # 57
        "Policeman",                   # 58
        "Policeman",                   # 59
        "Policeman",                   # 60
        "Policeman",                   # 61
        "Policeman",                   # 62
        "SE control",                 # 63
        "bc1100",                 # 64
        "Central square",               # 65
        "Nishi dori",                 # 66
        "Administrative district",                 # 67
        "Residential area",                 # 68
        "Entertainment district",                 # 69
        "East Street",                 # 70
        "old Town",                 # 71
        "Harbor district",                 # 72
        "IBC",                 # 73
        "Beside the station",               # 74
        "Back street",                 # 75
        "Ursula interchange",           # 76
        "East Crossbell Highway",       # 77
        "West Crossbell Highway",       # 78
        "Mainz Mountain Road",           # 79
        "Orchis Tower",         # 80
    ))

    ATBonus("ATBonus_BF0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_C52E", 8,   8,   8,   8,   11,  11,  11)

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
        "BattleInfo_CC0", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc1100", "Sepith_C52E", 60, 30, 10, 0,
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

    PlaceName(-31.530000686645508, 0.0, -107.9000015258789, 0x0000, 0x0000, "Central square")
    PlaceName(-117.0, 0.0, -102.05000305175781, 0x0000, 0x0000, "Nishi dori")
    PlaceName(3.5799999237060547, 0.0, 7.800000190734863, 0x0000, 0x0000, "Administrative district")
    PlaceName(-196.3000030517578, 0.0, -5.199999809265137, 0x0000, 0x0000, "Residential area")
    PlaceName(-101.4000015258789, 0.0, -15.600000381469727, 0x0000, 0x0000, "Entertainment district")
    PlaceName(74.0999984741211, 0.0, -137.8000030517578, 0x0000, 0x0000, "East Street")
    PlaceName(120.25, 0.0, -209.3000030517578, 0x0000, 0x0000, "old Town")
    PlaceName(110.5, 0.0, -52.0, 0x0000, 0x0000, "Harbor district")
    PlaceName(76.69999694824219, 0.0, 70.19999694824219, 0x0000, 0x0000, "IBC")
    PlaceName(-16.899999618530273, 0.0, -197.60000610351562, 0x0000, 0x0000, "Beside the station")
    PlaceName(-78.0, 0.0, -62.400001525878906, 0x0000, 0x0000, "Back street")
    PlaceName(-20.799999237060547, 0.0, -237.89999389648438, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(144.3000030517578, 0.0, -119.5999984741211, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-183.3000030517578, 0.0, -104.0, 0x0000, 0x0000, "West Crossbell Highway")
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
        "Function_10_31C0",        # 0A, 10
        "Function_11_3FFB",        # 0B, 11
        "Function_12_41FD",        # 0C, 12
        "Function_13_50A5",        # 0D, 13
        "Function_14_5375",        # 0E, 14
        "Function_15_578E",        # 0F, 15
        "Function_16_5798",        # 10, 16
        "Function_17_57A2",        # 11, 17
        "Function_18_57AC",        # 12, 18
        "Function_19_5C35",        # 13, 19
        "Function_20_5FFA",        # 14, 20
        "Function_21_61DF",        # 15, 21
        "Function_22_62CA",        # 16, 22
        "Function_23_63BD",        # 17, 23
        "Function_24_64B4",        # 18, 24
        "Function_25_657B",        # 19, 25
        "Function_26_65EB",        # 1A, 26
        "Function_27_66F5",        # 1B, 27
        "Function_28_67D1",        # 1C, 28
        "Function_29_6D94",        # 1D, 29
        "Function_30_70FF",        # 1E, 30
        "Function_31_71F3",        # 1F, 31
        "Function_32_72A4",        # 20, 32
        "Function_33_730A",        # 21, 33
        "Function_34_736C",        # 22, 34
        "Function_35_73E9",        # 23, 35
        "Function_36_7436",        # 24, 36
        "Function_37_747B",        # 25, 37
        "Function_38_74F0",        # 26, 38
        "Function_39_7526",        # 27, 39
        "Function_40_7678",        # 28, 40
        "Function_41_7F23",        # 29, 41
        "Function_42_8687",        # 2A, 42
        "Function_43_89EB",        # 2B, 43
        "Function_44_8A31",        # 2C, 44
        "Function_45_8E9E",        # 2D, 45
        "Function_46_8F55",        # 2E, 46
        "Function_47_8F9A",        # 2F, 47
        "Function_48_8FD5",        # 30, 48
        "Function_49_969F",        # 31, 49
        "Function_50_9764",        # 32, 50
        "Function_51_9845",        # 33, 51
        "Function_52_9874",        # 34, 52
        "Function_53_989D",        # 35, 53
        "Function_54_99B0",        # 36, 54
        "Function_55_9AAC",        # 37, 55
        "Function_56_9BCC",        # 38, 56
        "Function_57_9C31",        # 39, 57
        "Function_58_9C60",        # 3A, 58
        "Function_59_9C85",        # 3B, 59
        "Function_60_9D0A",        # 3C, 60
        "Function_61_A818",        # 3D, 61
        "Function_62_A938",        # 3E, 62
        "Function_63_A997",        # 3F, 63
        "Function_64_A9C7",        # 40, 64
        "Function_65_A9F7",        # 41, 65
        "Function_66_B7B1",        # 42, 66
        "Function_67_B819",        # 43, 67
        "Function_68_B891",        # 44, 68
        "Function_69_BAE2",        # 45, 69
        "Function_70_C38A",        # 46, 70
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31BC")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2288")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2288")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A8")
    OP_AF(0x80)
    Jump("loc_22AA")

    label("loc_22A8")

    OP_AF(0x81)

    label("loc_22AA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31B7")

    label("loc_22B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22CD")
    Jump("loc_31B7")

    label("loc_22CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31B7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_2380")

    ChrTalk(
        0xFE,
        (
            "Well, as for tomato soda\x01",
            "It looks like there is still room for improvement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Delicious juice that everyone can enjoy\x01",
            "I will not work hard to make it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B7")

    label("loc_2380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_24E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2450")

    ChrTalk(
        0xFE,
        "Everyone, thanks for your hard work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it is not original of our shop,\x01",
            "To the tired body, \"Sorrisitan X\"\x01",
            "It is recommended!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fill the energy perfectly\x01",
            "Good luck going!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24DE")

    label("loc_2450")


    ChrTalk(
        0xFE,
        (
            "I got in touch a while ago ……\x01",
            "Department store mom also\x01",
            "I was glad that it seemed to be safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, everyone\x01",
            "With the spiritual power\x01",
            "Let's get better!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24DE")

    Jump("loc_31B7")

    label("loc_24E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_24F1")
    Jump("loc_31B7")

    label("loc_24F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2544")

    ChrTalk(
        0xFE,
        (
            "Everyone, it is a terrible enthusiast … …\x01",
            "It may be a bit scary somewhat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B7")

    label("loc_2544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_26B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2614")

    ChrTalk(
        0xFE,
        "Everyone, thanks for your hard work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it is not original of our shop,\x01",
            "To the tired body, \"Sorrisitan X\"\x01",
            "It is recommended!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fill the energy perfectly\x01",
            "Good luck going!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_26AB")

    label("loc_2614")


    ChrTalk(
        0xFE,
        (
            "Although it is not original of our shop,\x01",
            "To the tired body, \"Sorrisitan X\"\x01",
            "It is recommended!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fill the energy perfectly\x01",
            "Good luck going!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26AB")

    Jump("loc_31B7")

    label("loc_26B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_281D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_278B")

    ChrTalk(
        0xFE,
        (
            "The occupation case of Mainz,\x01",
            "It's a terrible story, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do you accept it?\x01",
            "From this morning independent discussion also actively\x01",
            "It seems to be getting ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, how to judge\x01",
            "I do not know yet.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2818")

    label("loc_278B")


    ChrTalk(
        0xFE,
        (
            "After receiving the occupation case,\x01",
            "From this morning independent discussion also actively\x01",
            "It seems to be getting ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, how to judge\x01",
            "I do not know yet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2818")

    Jump("loc_31B7")

    label("loc_281D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_282B")
    Jump("loc_31B7")

    label("loc_282B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_294C")

    ChrTalk(
        0xFE,
        (
            "Police people from a little while ago\x01",
            "You seem to be in a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also in any incident\x01",
            "Did it happen …?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2947")

    ChrTalk(
        0x101,
        (
            "#00008F(The gourmet guide coverage here\x01",
            "It looks like it could be done … …)\x02\x03",
            "#00003F(It is not right now.\x01",
            "Let's not forget to come later. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2947")

    Jump("loc_31B7")

    label("loc_294C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A79")

    ChrTalk(
        0xFE,
        (
            "Start a juice shop\x01",
            "It's been about a year now,\x01",
            "Thanks to your sales, sales are going well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I gradually get recognition,\x01",
            "Recently I adopted \"limited time\"\x01",
            "Especially it seems that it was a success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, I am as well,\x01",
            "Why people are naming themselves\x01",
            "Is it weak?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2B02")

    label("loc_2A79")


    ChrTalk(
        0xFE,
        (
            "New menu\x01",
            "For the limited time to sell,\x01",
            "It was my mother's suggestion … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My mother is an innate businessman.\x01",
            "I have always been studied.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B02")

    Jump("loc_31B7")

    label("loc_2B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2CBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C11")

    ChrTalk(
        0xFE,
        (
            "welcome!\x01",
            "How about some fresh juice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, with the theme of national independence as the subject\x01",
            "I used only crossbell special products\x01",
            "There is also a limited menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell taste\x01",
            "The ultimate cup of condensed\x01",
            "Please do not miss it once!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2CBA")

    label("loc_2C11")


    ChrTalk(
        0xFE,
        (
            "Now, with the theme of national independence as the subject\x01",
            "I used only crossbell special products\x01",
            "There is also a limited menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A cup filled with the taste of autonomous state\x01",
            "Please do not miss it once!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CBA")

    Jump("loc_31B7")

    label("loc_2CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2E54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DAB")

    ChrTalk(
        0xFE,
        (
            "Today is only with plenary sessions,\x01",
            "Directions to Orkis Tower\x01",
            "It seems to be blocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Me too\x01",
            "In order to go to see the state\x01",
            "I regret that I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But well, considering safety\x01",
            "I guess it is natural.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2E4F")

    label("loc_2DAB")


    ChrTalk(
        0xFE,
        (
            "Today is only with plenary sessions,\x01",
            "Directions to Orkis Tower\x01",
            "It seems to be blocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Considering safety\x01",
            "It will be natural, but,\x01",
            "It is a pity as a citizen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E4F")

    Jump("loc_31B7")

    label("loc_2E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2F12")

    ChrTalk(
        0xFE,
        (
            "In the morning I will also go around here\x01",
            "It was a crowd with people,\x01",
            "It has finally calmed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, but thanks.\x01",
            "Today, already the usual sales\x01",
            "I asked you to exceed the average.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B7")

    label("loc_2F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2FAD")

    ChrTalk(
        0xFE,
        (
            "welcome!\x01",
            "How about some fresh juice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, from tomorrow\x01",
            "I imagined a trade meeting\x01",
            "We can also offer special menus.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B7")

    label("loc_2FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2FBB")
    Jump("loc_31B7")

    label("loc_2FBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_31B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3037")

    ChrTalk(
        0xFE,
        (
            "Is not it something?\x01",
            "It was a wonderful captor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, the police also everyone\x01",
            "You seem to be doing your best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B7")

    label("loc_3037")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_312F")

    ChrTalk(
        0xFE,
        (
            "welcome!\x01",
            "How about some fresh juice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, I used a variant of imported ingredients\x01",
            "There is also a limited-time menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you miss this opportunity and later\x01",
            "I can not taste the new flavor\x01",
            "Please do not miss it once!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_31B7")

    label("loc_312F")


    ChrTalk(
        0xFE,
        (
            "Now, I used a variant of imported ingredients\x01",
            "There is also a limited-time menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before sale ends\x01",
            "Please do not miss it once!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31B7")

    Jump("loc_222A")

    label("loc_31BC")

    TalkEnd(0xFE)
    Return()

    # Function_9_21E6 end

    def Function_10_31C0(): pass

    label("Function_10_31C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3309")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_329E")

    ChrTalk(
        0xFE,
        "Abnormal circumstances visited to Crossbell …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well,\x01",
            "This kind of time is the mind of citizens\x01",
            "We have to make it one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do not lose ~, crossbells!\x01",
            "Gambare ~, McDowell chair!\x01",
            "… …. Now, along with you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3304")

    label("loc_329E")


    ChrTalk(
        0xFE,
        (
            "Well …\x01",
            "Come on, come join us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do not lose ~, crossbells!\x01",
            "Gambare ~, McDowell chair!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3304")

    Jump("loc_3FF7")

    label("loc_3309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3317")
    Jump("loc_3FF7")

    label("loc_3317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3373")

    ChrTalk(
        0xFE,
        "President Dieter, Banzha ~ a! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do not forget the empire, and the Republic ~! It is!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FF7")

    label("loc_3373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_34F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3461")

    ChrTalk(
        0xFE,
        (
            "I still burn with my eyes ……\x01",
            "No way, Iria-sama like that … ….!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well … … Allowing militant group!\x01",
            "And you forgive, the Imperial Government! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this way, we firmly and independently\x01",
            "There is only thorough anti-war ……!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_34EB")

    label("loc_3461")


    ChrTalk(
        0xFE,
        (
            "Well … … Allowing militant group!\x01",
            "And you forgive, the Imperial Government! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this way, we firmly and independently\x01",
            "There is only thorough anti-war ……!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34EB")

    Jump("loc_3FF7")

    label("loc_34F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3621")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35B9")

    ChrTalk(
        0xFE,
        (
            "Hmm, it is a case in a mining town.\x01",
            "It will be totally unpleasant at such times …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Anyway, I waited for it today.\x01",
            "Renewal The stage for release of the stage!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am going to be entertained with a full eye!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_361C")

    label("loc_35B9")


    ChrTalk(
        0xFE,
        (
            "I waited for it tonight.\x01",
            "Renewal The stage for release of the stage!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am going to be entertained with a full eye!\x02",
    )

    CloseMessageWindow()

    label("loc_361C")

    Jump("loc_3FF7")

    label("loc_3621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3737")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36DD")

    ChrTalk(
        0xFE,
        (
            "At last, at last tomorrow\x01",
            "Renewal performances ……!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The excitement is suppressed and the clearer … ….\x01",
            "…… Hmm, this rain is\x01",
            "It is just right for the body that burned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am getting somehow kept calm.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3732")

    label("loc_36DD")


    ChrTalk(
        0xFE,
        (
            "…… Hmm, this rain is\x01",
            "It is just right for the body that burned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am getting somehow kept calm.\x02",
    )

    CloseMessageWindow()

    label("loc_3732")

    Jump("loc_3FF7")

    label("loc_3737")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_387C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_381E")

    ChrTalk(
        0xFE,
        (
            "\"Golden Sun, Silver Moon\"\x01",
            "Two more days until the renewal performance …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, how long will it be in time.\x01",
            "It's an evening show on that day … …\x01",
            "Is there certainty over 48 hours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nervous …\x01",
            "Well, I'm patriotic!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3877")

    label("loc_381E")


    ChrTalk(
        0xFE,
        (
            "Nervous …\x01",
            "I want you to become the day after tomorrow as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, I'm patriotic!\x02",
    )

    CloseMessageWindow()

    label("loc_3877")

    Jump("loc_3FF7")

    label("loc_387C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_38E7")

    ChrTalk(
        0xFE,
        (
            "\"Golden Sun, Silver Moon\"\x01",
            "Two more days until the renewal performance …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, be patient! It is!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FF7")

    label("loc_38E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3A52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39BC")

    ChrTalk(
        0xFE,
        (
            "Of alkane shell\x01",
            "Renewal performance is\x01",
            "Finally approached in 3 days!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And, in reality …\x01",
            "This time lucky tickets for the first performance\x01",
            "I got it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, I can not wait to have fun too! It is!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3A4D")

    label("loc_39BC")


    ChrTalk(
        0xFE,
        (
            "Even so, the cast of the other day\x01",
            "I was amazed at the additional announcement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shri · Atlaid …\x01",
            "Become a weak crown at age 13, as soon as you play a big role\x01",
            "I'm totally terrified of acting!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A4D")

    Jump("loc_3FF7")

    label("loc_3A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3BBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B5A")

    ChrTalk(
        0xFE,
        (
            "Was it from the afternoon?\x01",
            "Finally, at the Orkis Tower\x01",
            "The plenary session will be held!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, to become a better meeting\x01",
            "Let's send it with cheers as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#4SMayor Dieter … …!\x01",
            "We citizen\x01",
            "I support you from the bottom of my heart! It is!#3S\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BB9")

    label("loc_3B5A")


    ChrTalk(
        0xFE,
        "Which one … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#4SMcDaill chairman … …!\x01",
            "Good luck with the mayor! It is!#3S\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BB9")

    Jump("loc_3FF7")

    label("loc_3BBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3C86")

    ChrTalk(
        0xFE,
        (
            "Orchis Tower……!\x01",
            "What a graceful and magnificent! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "About this town\x01",
            "I will not like it more and more!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With this one again, on this crossbell\x01",
            "A new place is added!\x01",
            "That's fine, fine! It is!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FF7")

    label("loc_3C86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3DF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D7B")

    ChrTalk(
        0xFE,
        (
            "Hmm, the leaders of each country\x01",
            "What comes to this crossbell is\x01",
            "It is finally tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also tomorrow is the Orkis Tower\x01",
            "It is the day when the unveiling ceremony is held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, considering such a thing\x01",
            "I am excited and I can not sleep tonight!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3DED")

    label("loc_3D7B")


    ChrTalk(
        0xFE,
        (
            "Hmm, considering tomorrow\x01",
            "Excited tonight\x01",
            "I do not feel like sleeping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why do not you stay up all night?\x02",
    )

    CloseMessageWindow()

    label("loc_3DED")

    Jump("loc_3FF7")

    label("loc_3DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3E6D")

    ChrTalk(
        0xFE,
        (
            "Good morning, today it's raining today\x01",
            "Sometimes it is good to have such a day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, the crossbell is still the best!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FF7")

    label("loc_3E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3FF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F17")

    ChrTalk(
        0xFE,
        (
            "You guys, a little while ago\x01",
            "Dent working combining sandbags\x01",
            "It was quite good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What are you doing at first?\x01",
            "It was the one that tilted his head … …\x01",
            "Umm, it's upper! It is!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FF7")

    label("loc_3F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F86")

    ChrTalk(
        0xFE,
        "Good morning, it is a wonderful weather today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is exactly the best day for walks.\x01",
            "No, thanks a lot, fine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3FF7")

    label("loc_3F86")


    ChrTalk(
        0xFE,
        "I love the cross streets.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Often you will hear a story of noises,\x01",
            "Still I love this city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FF7")

    TalkEnd(0xFE)
    Return()

    # Function_10_31C0 end

    def Function_11_3FFB(): pass

    label("Function_11_3FFB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_41F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_408A")

    ChrTalk(
        0xFE,
        (
            "A crowded car of cars ……\x01",
            "It seemed quite high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, is it the latest version of Verne?\x01",
            "Because this is so rich …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41F9")

    label("loc_408A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4143")

    ChrTalk(
        0xFE,
        (
            "Since the case incident happened,\x01",
            "Congress has changed completely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We are busy with the Finance Division\x01",
            "As usual, compared to the past\x01",
            "I have my work done quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_41F9")

    label("loc_4143")


    ChrTalk(
        0xFE,
        (
            "More than anything, to the Empire and the Republic\x01",
            "Members who were immersed\x01",
            "It was great that I was wiped out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, the intentions of both countries\x01",
            "Although it can not be neglected … …\x01",
            "There is something wrong with this difference.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41F9")

    TalkEnd(0xFE)
    Return()

    # Function_11_3FFB end

    def Function_12_41FD(): pass

    label("Function_12_41FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4404")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4385")

    ChrTalk(
        0xFE,
        (
            "What on earth is that big tree …?\x01",
            "It looks like it is glowing pale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What I can not believe recently\x01",
            "I have kept it many times,\x01",
            "That is spooking loops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… you guys, really are you\x01",
            "Are you going to jump in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F……Ah.\x01",
            "I can not draw back now.\x02\x03",
            "#00000FThe city asked, Franz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, please leave it.\x01",
            "… … You also have to be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43FF")

    label("loc_4385")


    ChrTalk(
        0xFE,
        (
            "Now each person can do what they can\x01",
            "If it does not do it, it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, leave it here.\x01",
            "… … You also have to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43FF")

    Jump("loc_50A1")

    label("loc_4404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4412")
    Jump("loc_50A1")

    label("loc_4412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4420")
    Jump("loc_50A1")

    label("loc_4420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_442E")
    Jump("loc_50A1")

    label("loc_442E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_443C")
    Jump("loc_50A1")

    label("loc_443C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_45B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_451D")

    ChrTalk(
        0xFE,
        (
            "What is full restoration this morning ……\x01",
            "I will do the guard as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The same as the police guards recently\x01",
            "It tends to be underestimated,\x01",
            "Actually it's quite a big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yesterday, watching the worker working in the field\x01",
            "I got the courage to do it seriously.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_45B0")

    label("loc_451D")


    ChrTalk(
        0xFE,
        (
            "The same as the police guards recently\x01",
            "It tends to be underestimated,\x01",
            "Actually it's quite a big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yesterday, watching the worker working in the field\x01",
            "I got the courage to do it seriously.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45B0")

    Jump("loc_50A1")

    label("loc_45B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_45C3")
    Jump("loc_50A1")

    label("loc_45C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4658")

    ChrTalk(
        0xFE,
        (
            "Something recently, around the city\x01",
            "It seems that \"Phantom beast\" appears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you knock it down with Hood\x01",
            "I heard that it disappears … …\x01",
            "It is a story of disgust.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50A1")

    label("loc_4658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4ADD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A56")

    ChrTalk(
        0xFE,
        (
            "The terrorism of the Trade Council,\x01",
            "For Crossbell Police\x01",
            "It was really scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently some improvements were seen\x01",
            "The trust of the police as a whole also fails to restore … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is said that he is standing in the streets like this,\x01",
            "I guess it's true\x01",
            "I realize that it got stronger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, Lloyd's\x01",
            "The mission support department is separate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FAh, no way……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FHowever,\x01",
            "Is that so prominent …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tentatively, during the tour\x01",
            "The tone of a shameful bastard is\x01",
            "Obviously it is more than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "\"Wonderful hardship hardship meaningless\" or something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "\"Because you are incompetent\x01",
            "Two major powers will be added \".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can never deny it,\x01",
            "Being hit beyond necessity\x01",
            "I mean something to do ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FI see……\x01",
            "It is quite painful, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FWell, whatever you may think\x01",
            "We can do what we can do\x01",
            "You only have to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FYeah, to it\x01",
            "Even with small power\x01",
            "Whether there is or not there is not much difference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe, so much comment\x01",
            "There is nothing to worry about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha … … it certainly is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank you.\x01",
            "Something a little refreshing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 5)
    Jump("loc_4AD8")

    label("loc_4A56")


    ChrTalk(
        0xFE,
        (
            "We can do what we can do\x01",
            "There is no choice but to do it surely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is no choice but to rotten ……\x01",
            "I should cringe in and do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AD8")

    Jump("loc_50A1")

    label("loc_4ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4AEE")
    Call(0, 13)
    Jump("loc_50A1")

    label("loc_4AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4C5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD6")

    ChrTalk(
        0xFE,
        (
            "Well, Lloyd?\x01",
            "Today the open space is open to the public\x01",
            "Please do not hesitate to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, but, the unveiling ceremony\x01",
            "Even looking at it from here was amazing enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is it, human beings\x01",
            "Even being able to make such things\x01",
            "It's a great story.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C57")

    label("loc_4BD6")


    ChrTalk(
        0xFE,
        (
            "No, but, the unveiling ceremony\x01",
            "Even looking at it from here was amazing enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is it, human beings\x01",
            "Even being able to make such things\x01",
            "It's a great story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C57")

    Jump("loc_50A1")

    label("loc_4C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4E90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DF1")

    ChrTalk(
        0xFE,
        (
            "Yo, Lloyd.\x01",
            "It will be a commerce meeting from tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Security guards will soon be in strict command mode\x01",
            "I got nervous as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FCertainly, tomorrow\x01",
            "Leaders enter crossbell\x01",
            "That's why.\x02\x03",
            "#00000FIn addition, the Orkis Tower also\x01",
            "It's time to show off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fuu, what is it?\x01",
            "It feels like it is not possible in many ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, for three days from tomorrow,\x01",
            "Let's tighten each other carefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FOh, that's OK.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 4)
    Jump("loc_4E8B")

    label("loc_4DF1")


    ChrTalk(
        0xFE,
        (
            "An unprecedented international conference ……\x01",
            "The more you think about it again,\x01",
            "I'm feeling more and more nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, anyway,\x01",
            "Three days from tomorrow\x01",
            "I have to tighten my mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E8B")

    Jump("loc_50A1")

    label("loc_4E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4FD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EAB")
    Call(0, 14)
    Jump("loc_4FD0")

    label("loc_4EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4F6A")

    ChrTalk(
        0xFE,
        (
            "Certainly the investigators are longing for ……\x01",
            "Somehow I was caught in the ideal\x01",
            "I feel like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is it, more now?\x01",
            "I am a life-sized person\x01",
            "I decided to face each other.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 6)
    Jump("loc_4FD0")

    label("loc_4F6A")


    ChrTalk(
        0xFE,
        (
            "Although it is light rain,\x01",
            "Security on rainy days is not easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lloyd's also have a cold.\x01",
            "Take care not to draw.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FD0")

    Jump("loc_50A1")

    label("loc_4FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_50A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FF0")
    Call(0, 14)
    Jump("loc_50A1")

    label("loc_4FF0")


    ChrTalk(
        0xFE,
        (
            "Certainly the investigators are longing for ……\x01",
            "Somehow I was caught in the ideal\x01",
            "I feel like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is it, more now?\x01",
            "I am a life-sized person\x01",
            "I decided to face each other.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 6)

    label("loc_50A1")

    TalkEnd(0xFE)
    Return()

    # Function_12_41FD end

    def Function_13_50A5(): pass

    label("Function_13_50A5")

    OP_4B(0xB, 0xFF)
    OP_4B(0x1F, 0xFF)
    OP_4B(0x20, 0xFF)
    OP_4B(0x21, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5260")

    ChrTalk(
        0xB,
        (
            "I am sorry, too.\x01",
            "Today we will hold a plenary session\x01",
            "For the general public -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Hmm, but the square does not matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "That's right.\x01",
            "Because we came all the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Right, should I just have a little?\x01",
            "Ten minutes, no less than five minutes, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, er,\x01",
            "That's not a problem …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(Apparently, against the blockade of the plaza\x01",
            "You seem to be protesting. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Ah.\x01",
            "… Franz is hard too. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5364")

    label("loc_5260")


    ChrTalk(
        0x21,
        (
            "5 minutes, no more 3 minutes\x01",
            "Because it is good, please?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Oh yeah, we are\x01",
            "Just a little bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "No, in the first place the square\x01",
            "It should not be a problem if you let it through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, anyway\x01",
            "It is useless for useless things ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(When we pass,\x01",
            "Let's pass aside casually … …)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5364")

    OP_4C(0xB, 0xFF)
    OP_4C(0x1F, 0xFF)
    OP_4C(0x20, 0xFF)
    OP_4C(0x21, 0xFF)
    Return()

    # Function_13_50A5 end

    def Function_14_5375(): pass

    label("Function_14_5375")

    RunExpression(0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xB, 0x101, 0)

    ChrTalk(
        0xB,
        (
            "Yo, Lloyd.\x01",
            "Finally the training of the investigation section one finally\x01",
            "I heard it's over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And also Lloyd's title\x01",
            "Finally to a senior agent … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Huh, even though there is a synchronization of the police school\x01",
            "I went to a distant place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FNo, it's not like that anymore.\x02\x03",
            "#00000FBy the way, Franz is\x01",
            "How was the result of the investigator exam?\x02\x03",
            "Certainly, did you accept it a while ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Huh, if I could pass\x01",
            "I'm reporting to Lloyd the first time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The result was disastrous … …\x01",
            "Clearly saying to me that the investigator\x01",
            "I was told that I did not face it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008FWell, was that so ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Well, thanks, I was able to blow it out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Even the work of the current wide area crime prevention division,\x01",
            "There are enough challenges enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Separately to the investigator to that extent\x01",
            "I do not need to be insisted … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "From now on,\x01",
            "I am a life-sized person\x01",
            "I chose to face each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FFranz …\x02\x03",
            "#00002FReally.\x01",
            "Yeah, the thing that seems to me is more than anything.\x02\x03",
            "Then, from now on to each other\x01",
            "Let 's go for each way and go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Oh, of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F(Well, something\x01",
            "I feel like a man's friendship. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F(Yes, I feel a little jealous.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xB, 0x10)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x13E, 5)
    Return()

    # Function_14_5375 end

    def Function_15_578E(): pass

    label("Function_15_578E")

    TalkBegin(0xFE)
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    # Function_15_578E end

    def Function_16_5798(): pass

    label("Function_16_5798")

    TalkBegin(0xFE)
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    # Function_16_5798 end

    def Function_17_57A2(): pass

    label("Function_17_57A2")

    TalkBegin(0xFE)
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    # Function_17_57A2 end

    def Function_18_57AC(): pass

    label("Function_18_57AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_57BD")
    Jump("loc_5C31")

    label("loc_57BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5A5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59EB")

    ChrTalk(
        0xFE,
        "Oh, you guys at the support department.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, good tired.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FThe head office is still recovering, is not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, for the time being\x01",
            "Although it is in tidy up state … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, at the entrance\x01",
            "In a situation where the damage is terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order to restore the reception function,\x01",
            "It will take some time yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, regarding acceptance\x01",
            "The office work temporarily at the police school\x01",
            "I will do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also have Rebecca,\x01",
            "If there is something related to work related work\x01",
            "You should be able to deal with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FIndeed, it is consent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200Fthank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 4)
    Jump("loc_5A59")

    label("loc_59EB")


    ChrTalk(
        0xFE,
        (
            "Until the head office recovers\x01",
            "It will take a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there is any office work,\x01",
            "You should go to the police school.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A59")

    Jump("loc_5C31")

    label("loc_5A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5B28")

    ChrTalk(
        0xFE,
        (
            "Today is for the general public\x01",
            "Access to the Orkis Tower\x01",
            "I'm restricted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you can see, \"I have not heard of it\"\x01",
            "Many people protest, but … …\x01",
            "Anyway other than those involved, we will not pass it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C31")

    label("loc_5B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5BA7")

    ChrTalk(
        0xFE,
        (
            "The square in front of the tower,\x01",
            "Many citizens and\x01",
            "It is crowded with tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Immediately after the unveiling ceremony,\x01",
            "The street goes hand in hand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C31")

    label("loc_5BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5C1A")

    ChrTalk(
        0xFE,
        "Tomorrow is finally over …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Five years have passed since the construction of the new city hall building,\x01",
            "It is finally a feeling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C31")

    label("loc_5C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5C28")
    Jump("loc_5C31")

    label("loc_5C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5C31")

    label("loc_5C31")

    TalkEnd(0xFE)
    Return()

    # Function_18_57AC end

    def Function_19_5C35(): pass

    label("Function_19_5C35")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5DB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D2E")

    ChrTalk(
        0xFE,
        (
            "In the afternoon, the leaders also\x01",
            "We gathered at the Orkis Tower ……\x01",
            "And the plenary session begins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From the situation so far,\x01",
            "The possibility that nothing happens is\x01",
            "It will be quite low.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, today as well\x01",
            "Let's say you're going to raise your spirit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5DAD")

    label("loc_5D2E")


    ChrTalk(
        0xFE,
        (
            "Clearly,\x01",
            "The possibility that nothing happens is\x01",
            "It will be quite low.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, today as well\x01",
            "Let's say you're going to raise your spirit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DAD")

    Jump("loc_5FF6")

    label("loc_5DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5E57")

    ChrTalk(
        0xFE,
        (
            "Although it is not until the anniversary festival,\x01",
            "Today seems to have a lot of people running along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Abruptly for disturbance purposes\x01",
            "Terrorism may also occur.\x01",
            "I have to watch carefully.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FF6")

    label("loc_5E57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5FF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F5A")

    ChrTalk(
        0xFE,
        (
            "All the leaders tomorrow,\x01",
            "Through this block to the new city hall\x01",
            "It will be headed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This place has good prospects,\x01",
            "It is easy to execute a crime such as sniper\x01",
            "It's a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To enter the crossbell\x01",
            "When we welcome the leaders,\x01",
            "A particularly strict regime will be laid down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5FF6")

    label("loc_5F5A")


    ChrTalk(
        0xFE,
        (
            "This place has good prospects,\x01",
            "It is easy to execute a crime such as sniper\x01",
            "It's a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To enter the crossbell\x01",
            "When we welcome the leaders,\x01",
            "A particularly strict regime will be laid down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FF6")

    TalkEnd(0xFE)
    Return()

    # Function_19_5C35 end

    def Function_20_5FFA(): pass

    label("Function_20_5FFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_609A")

    ChrTalk(
        0xFE,
        (
            "Terrorist groups simultaneously\x01",
            "Why are 2 pairs coming along?\x01",
            "It's not a joke at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway … anything confusing\x01",
            "I have to stop it before I get up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61DB")

    label("loc_609A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6141")

    ChrTalk(
        0xFE,
        (
            "Damn, towards the Orkis Tower\x01",
            "If you are in charge of security, the leaders\x01",
            "You actually saw it with this eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I saw a smoke glass\x01",
            "Only the protected limo.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61DB")

    label("loc_6141")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_61DB")

    ChrTalk(
        0xFE,
        (
            "The leaders of the four neighboring countries\x01",
            "To meet them all together ……\x01",
            "To be honest, the scale is tremendous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Tense up to this point\x01",
            "It might be the first time for caution.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61DB")

    TalkEnd(0xFE)
    Return()

    # Function_20_5FFA end

    def Function_21_61DF(): pass

    label("Function_21_61DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62A7")

    ChrTalk(
        0xC,
        "#01200FGuru …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FMr. Zeit,\x01",
            "It was in such a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FWith Ka'a's accompanying\x01",
            "You seem to be coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FEven so,\x01",
            "I'm totally familiar with the city …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_62C6")

    label("loc_62A7")


    ChrTalk(
        0xC,
        "#01200FGuru …… Won.\x02",
    )

    CloseMessageWindow()

    label("loc_62C6")

    TalkEnd(0xFE)
    Return()

    # Function_21_61DF end

    def Function_22_62CA(): pass

    label("Function_22_62CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6346")

    ChrTalk(
        0xFE,
        "Come now, How about a balloon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even one, two or three,\x01",
            "Take as much as you can today.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_63B9")

    label("loc_6346")


    ChrTalk(
        0xFE,
        (
            "From the afternoon\x01",
            "Even balloon art classroom\x01",
            "It is scheduled to be held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are interested, please do\x01",
            "Please come and join us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63B9")

    TalkEnd(0xFE)
    Return()

    # Function_22_62CA end

    def Function_23_63BD(): pass

    label("Function_23_63BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_64B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6438")

    ChrTalk(
        0x22,
        (
            "Ka'a-chan, today\x01",
            "I was going to go to the library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "I wonder if there was something I was looking for ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_64B0")

    label("loc_6438")


    ChrTalk(
        0x22,
        (
            "Shin, who came yesterday,\x01",
            "She seems to come home today by train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "I feel somewhat lonely ……\x01",
            "You seemed to be a good friend.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64B0")

    TalkEnd(0xFE)
    Return()

    # Function_23_63BD end

    def Function_24_64B4(): pass

    label("Function_24_64B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6577")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_653E")

    ChrTalk(
        0x23,
        (
            "Kisso, if you do not want it\x01",
            "To say stingy things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Oh, somehow\x01",
            "I guess I can not get in.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6577")

    label("loc_653E")


    ChrTalk(
        0x23,
        (
            "Oh, I have to do it early.\x01",
            "A fun party will start!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6577")

    TalkEnd(0xFE)
    Return()

    # Function_24_64B4 end

    def Function_25_657B(): pass

    label("Function_25_657B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_65E7")

    ChrTalk(
        0x24,
        "Let's give up, Ryou ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "What is a trade meeting?\x01",
            "Separately it's a fun party\x01",
            "Because it is not?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65E7")

    TalkEnd(0xFE)
    Return()

    # Function_25_657B end

    def Function_26_65EB(): pass

    label("Function_26_65EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_663E")

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "Empire and republic, from anywhere\x01",
            "I'm getting into trouble!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66F1")

    label("loc_663E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_669F")

    ChrTalk(
        0xFE,
        (
            "Something in front of the tower today\x01",
            "I can not put it in the square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Huh, that's a pinch.\x02",
    )

    CloseMessageWindow()
    Jump("loc_66F1")

    label("loc_669F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_66AD")
    Jump("loc_66F1")

    label("loc_66AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_66F1")

    ChrTalk(
        0xFE,
        (
            "Haha, it's pretty cool.\x01",
            "Even if you see it from here, it's enough!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66F1")

    TalkEnd(0xFE)
    Return()

    # Function_26_65EB end

    def Function_27_66F5(): pass

    label("Function_27_66F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6746")

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "If Arios is Secretary of Defense,\x01",
            "You can rest assured even after independence!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67CD")

    label("loc_6746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_678D")

    ChrTalk(
        0xFE,
        (
            "Ah, like yesterday\x01",
            "I wanted to look up nearby.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67CD")

    label("loc_678D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_679B")
    Jump("loc_67CD")

    label("loc_679B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_67CD")

    ChrTalk(
        0xFE,
        (
            "You know.\x01",
            "Or, is not it too deck?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67CD")

    TalkEnd(0xFE)
    Return()

    # Function_27_66F5 end

    def Function_28_67D1(): pass

    label("Function_28_67D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_681F")

    ChrTalk(
        0xFE,
        (
            "Well, next time in our store\x01",
            "I wonder if I will do an independent memorial sale.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D90")

    label("loc_681F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6957")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68B1")

    ChrTalk(
        0xFE,
        (
            "Have you heard?\x01",
            "Apparently the attack incident during this time\x01",
            "It seems that it was a conspiracy by the empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really\x01",
            "The country of the empire can not forgive.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6952")

    label("loc_68B1")


    ChrTalk(
        0xFE,
        (
            "But I understood well about this time.\x01",
            "Where they followed the empire they are\x01",
            "It's hard to keep us … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why we want our independence\x01",
            "I have no choice but to push it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6952")

    Jump("loc_6D90")

    label("loc_6957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6A9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A22")

    ChrTalk(
        0xFE,
        (
            "No way ….\x01",
            "It is not like this happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The guard managed to do something\x01",
            "I do not mind ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Finally,\x01",
            "It is necessary to borrow the power of the two major powers\x01",
            "Is not it worth it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6A95")

    label("loc_6A22")


    ChrTalk(
        0xFE,
        (
            "However, due to the independent advocacy\x01",
            "The relationship with the two major powers is\x01",
            "It is said that it is deteriorating … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No …\x01",
            "What will happen in the future …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A95")

    Jump("loc_6D90")

    label("loc_6A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6AA8")
    Jump("loc_6D90")

    label("loc_6AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6B2F")

    ChrTalk(
        0xFE,
        (
            "By the way … Tomorrow\x01",
            "A citizen forum at the city hall\x01",
            "It was done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, even now\x01",
            "Let me ask you a question.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D90")

    label("loc_6B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6C00")

    ChrTalk(
        0xFE,
        (
            "Just for emotional things,\x01",
            "Of course, I agree with independence independently … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, from the threat of the two major powers\x01",
            "How to keep safety is a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope it will open the way for dialogue,\x01",
            "That's not a simple story so.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D90")

    label("loc_6C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6C59")

    ChrTalk(
        0xFE,
        (
            "Whether the crossbell should be independent …\x01",
            "Hmm, no matter how many times I think it's a difficult problem.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D90")

    label("loc_6C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6D02")

    ChrTalk(
        0xFE,
        (
            "Mayor Dieter and McDowell,\x01",
            "If these two people are present, the plenary session\x01",
            "It will surely be rich in fruits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, the crossbell economy\x01",
            "The future is even more bright.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D90")

    label("loc_6D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6D90")

    ChrTalk(
        0xFE,
        (
            "The unveiling ceremony is even from this place\x01",
            "I could enjoy it enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From anywhere on the crossbell\x01",
            "It is truly awesome to be seen\x01",
            "It's a scale building.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D90")

    TalkEnd(0xFE)
    Return()

    # Function_28_67D1 end

    def Function_29_6D94(): pass

    label("Function_29_6D94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6DA5")
    Jump("loc_70FB")

    label("loc_6DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6DF4")

    ChrTalk(
        0xFE,
        (
            "Doing terrible things to everyone … …\x01",
            "It is a bad guy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70FB")

    label("loc_6DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6E59")

    ChrTalk(
        0xFE,
        (
            "Dad, since yesterday forever\x01",
            "I am troubled with such a kanji.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I want you to show me the genki …\x02",
    )

    CloseMessageWindow()
    Jump("loc_70FB")

    label("loc_6E59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6E67")
    Jump("loc_70FB")

    label("loc_6E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6EEE")

    ChrTalk(
        0xFE,
        (
            "Come tomorrow, I will see you\x01",
            "About Dokitsu everyone together\x01",
            "I'm talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, something\x01",
            "Otona is cool.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70FB")

    label("loc_6EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6F83")

    ChrTalk(
        0xFE,
        (
            "Well, I do not really know.\x01",
            "Why are you with each other?\x01",
            "You probably can not do it, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This, too\x01",
            "Is not he a guy?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70FB")

    label("loc_6F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7003")

    ChrTalk(
        0xFE,
        (
            "When you do,\x01",
            "There are good things but bad things\x01",
            "I do not know why.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, I do not understand well.\x02",
    )

    CloseMessageWindow()
    Jump("loc_70FB")

    label("loc_7003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7078")

    ChrTalk(
        0xFE,
        "Today is a very good day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something, everyone gathering\x01",
            "It seems to talk about various things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70FB")

    label("loc_7078")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_70FB")

    ChrTalk(
        0xFE,
        (
            "Curtains are gonna shoot,\x01",
            "Then it's like Hanabi\x01",
            "Dodon rises … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It seemed like a festival somehow!\x02",
    )

    CloseMessageWindow()

    label("loc_70FB")

    TalkEnd(0xFE)
    Return()

    # Function_29_6D94 end

    def Function_30_70FF(): pass

    label("Function_30_70FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_713A")

    ChrTalk(
        0xFE,
        "Hello, today was a welcome day!\x02",
    )

    CloseMessageWindow()
    Jump("loc_71EF")

    label("loc_713A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_71EF")

    ChrTalk(
        0xFE,
        (
            "I am doing at the city hall now.\x01",
            "It's a charity event,\x01",
            "It's fun to have various events.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And more than anything, doing this\x01",
            "I think that enjoying will lead to reconstruction\x01",
            "The idea is wonderful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71EF")

    TalkEnd(0xFE)
    Return()

    # Function_30_70FF end

    def Function_31_71F3(): pass

    label("Function_31_71F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7204")
    Jump("loc_72A0")

    label("loc_7204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_72A0")

    ChrTalk(
        0xFE,
        (
            "The event planner\x01",
            "Cross Bell Chamber of Commerce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, every year at the anniversary festival\x01",
            "I think, people from the Chamber of Commerce\x01",
            "It's powerful exciting and powerful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72A0")

    TalkEnd(0xFE)
    Return()

    # Function_31_71F3 end

    def Function_32_72A4(): pass

    label("Function_32_72A4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "The citizens' enthusiasm is tremendous …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone wanted in the bottom of my heart\x01",
            "Maybe it was expansion.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_72A4 end

    def Function_33_730A(): pass

    label("Function_33_730A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "You can not keep up with this as it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Early screen car\x01",
            "It seems better to withdraw.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_730A end

    def Function_34_736C(): pass

    label("Function_34_736C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "President Dieter\x01",
            "I made a wonderful decision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Living in crossbell for many years,\x01",
            "There is no such glad thing.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_736C end

    def Function_35_73E9(): pass

    label("Function_35_73E9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, Goddess.\x01",
            "Cross Bell's future\x01",
            "Please watch over me ……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_73E9 end

    def Function_36_7436(): pass

    label("Function_36_7436")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Now, you also together.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Crossbell independent country, all year!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_7436 end

    def Function_37_747B(): pass

    label("Function_37_747B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "President's speech is\x01",
            "It was wonderful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell, more from now\x01",
            "It's going to be a nice place!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_747B end

    def Function_38_74F0(): pass

    label("Function_38_74F0")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Eh, everybody\x01",
            "I feel so happy.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_74F0 end

    def Function_39_7526(): pass

    label("Function_39_7526")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_75C8")

    ChrTalk(
        0xFE,
        (
            "On a rainy day,\x01",
            "It is fun to hear various sounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Water surface, umbrella and ground …\x01",
            "The sound changes depending on where you hit\x01",
            "I feel like a little orchestra.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7674")

    label("loc_75C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7674")

    ChrTalk(
        0xFE,
        (
            "I am crispy hair ….\x01",
            "On a rainy day I feel somewhat\x01",
            "My hair gathers together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, I like rainy days ……\x01",
            "Sorry for making a bad story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7674")

    TalkEnd(0xFE)
    Return()

    # Function_39_7526 end

    def Function_40_7678(): pass

    label("Function_40_7678")

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
        "That was a great speech …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#6PNo way Crossbell\x01",
            "To declare independence ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#6PThat also, the Empire and the Republic\x01",
            "It's like saying like that … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#12PI was talking about \"big fight\" of the two major countries, but …\x01",
            "Perhaps that accident happened a long time ago …?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Citizen",
        "#12PEmpire and the Republic … …! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#6P…… Until now, for crossbells\x01",
            "Did there be anyone to tell you over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Crossbell politicians,\x01",
            "Tame to the Empire and the Republic\x01",
            "It was only utilities ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "It seems like Mr. MacDowell\x01",
            "Although there was a fine person ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#6PThe power so far\x01",
            "People who make me feel\x01",
            "I certainly did not … …!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Citizen",
        (
            "#6PMoreover, the guardian god of crossbell\x01",
            "Arios is the Secretary of Defense!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PIt is a selection that does not have any more.\x01",
            "That person is at the top\x01",
            "If you protect the crossbell …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#12PYeah, there is nothing scary!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Crossbell independence, too,\x01",
            "Perhaps it is not a dream story …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#6PMayor Dieter, no, president ……\x01",
            "It is surely safe to leave it to him!\x02",
        )
    )

    CloseMessageWindow()
    OP_25(0x1BD, 0x3C)

    NpcTalk(
        0xD,
        "Citizen",
        (
            "#12POh, as long as he\x01",
            "I am not afraid of the empire and the republic … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#6PPresident Dieter … …!\x02",
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
        "#5SPresident Dieter, 10 years old!#3S\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Citizens")

    AnonymousTalk(
        0xFF,
        "#5SPresident Dieter, 10 years old! It is!#3S\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_25(0x1BD, 0x50)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0xF,
        "#5SCrossbell independent country, all year!#3S\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Citizens")

    AnonymousTalk(
        0xFF,
        "#5S#6PCrossbell independent country, all year! It is!#3S\x02",
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
        "#5SPresident Dieter, 10 years old! It is!#3S\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetChrName("Citizens")

    AnonymousTalk(
        0xFF,
        "#5SCrossbell independent country, all year! It is!#3S\x02",
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
        "#6P#00005F…… It's been awfully enthusiastic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FYeah … I understand your feelings.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201FIt's getting too hot\x01",
            "Will not trouble happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FWell, there are also soldiers of the Defense Forces\x01",
            "It will fit in then … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001F…… Anyhow, let's go.\x02",
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

    # Function_40_7678 end

    def Function_41_7F23(): pass

    label("Function_41_7F23")

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

    def lambda_805B():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_805B)
    Sleep(50)

    def lambda_806B():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_806B)
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
        "#5P#00005FOh, is the section chief?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FEven if it hangs around\x01",
            "It's strange time.\x02",
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
            "#00000FYes, Special Affairs Support Division,\x01",
            "It is Lloyd · Bannings.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ou, thanks.\x02\x03",
            "As I said in the morning, it will not be long\x01",
            "I will have you come to the police school.\x02\x03",
            "Do you know the place?\x02",
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
            "#00000FFrom the middle of the West Crossbell Highway\x01",
            "I'm in the gate.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, keep the gate open.\x02\x03",
            "by the way……\x01",
            "You should have walked around the street all the way.\x02\x03",
            "How frankly did you say?\x02",
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
            "#00011FAh……\x02",
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
            "#00003F……I agree.\x02\x03",
            "#00001FTo various queen smell situation\x01",
            "I feel like I'm getting started.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "That olfaction, more than ever\x01",
            "Sharpen it.\x02\x03",
            "Well then it will be waiting.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#00000FOK.\x02",
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
        "#12P#00100FAfter all I seem to have been the section chief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FSomething to worry about\x01",
            "I guess they were saying … ….?\x02",
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
            "#5P#00006FOh, the section chief is also various\x01",
            "It seems that I feel a change in the situation.\x02\x03",
            "#00001FBlack Month and Captain Rector\x01",
            "It seems better to report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00106FI see …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10300FSo, it is about time.\x01",
            "You go to the police school?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00000FOh, let's get out on the highway from the West Exit.\x02",
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
            "From the city map of Crossbell\x01",
            "\"West Crossbell Highway\"\x01",
            "You can now select.\x07\x00\x02",
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

    # Function_41_7F23 end

    def Function_42_8687(): pass

    label("Function_42_8687")

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

    # Function_42_8687 end

    def Function_43_89EB(): pass

    label("Function_43_89EB")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 17150, 2500, 450)
    OP_9F(0x1, 4400, 2500, 8350)
    OP_9F(0x1, -4000, 2500, 21250)
    OP_9F(0x1, -5850, 2500, 32500)
    OP_9F(0x2, 0xFE, 5500, 0x6)
    Return()

    # Function_43_89EB end

    def Function_44_8A31(): pass

    label("Function_44_8A31")

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
    SetChrName("McDowell")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W─ ─ Needless to say, about the current situation\x01",
            "There will be each person!\x02\x03",
            "But the current government is truly democratic\x01",
            "It is not established by procedure!\x02\x03",
            "Many autonomous state members are detained,\x01",
            "I myself, in captivity,\x01",
            "Crossbell's independence was declared!\x02\x03",
            "If this declaration is not approved by Congress\x01",
            "What was done by an individual's own duty\x01",
            "I would like to point out again.\x07\x00\x02",
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

    # Function_44_8A31 end

    def Function_45_8E9E(): pass

    label("Function_45_8E9E")

    Sleep(2000)

    def lambda_8EA6():
        OP_96(0xFE, 0xAF0, 0x9C4, 0x11F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_8EA6)
    Sleep(500)

    def lambda_8EC3():
        OP_96(0xFE, 0xFFFFFF38, 0x9C4, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_8EC3)
    Sleep(500)

    def lambda_8EE0():
        OP_96(0xFE, 0x384, 0x9C4, 0x1A2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x40, 1, lambda_8EE0)
    Sleep(500)

    def lambda_8EFD():
        OP_96(0xFE, 0x1194, 0x9C4, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_8EFD)
    WaitChrThread(0x3D, 1)
    OP_63(0x3D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x40, 1)
    OP_63(0x40, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x3E, 1)
    Return()

    # Function_45_8E9E end

    def Function_46_8F55(): pass

    label("Function_46_8F55")

    Sleep(8000)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_8F6F():
        OP_96(0xFE, 0x8FC, 0x9C4, 0x2AF8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8F6F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1100)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_46_8F55 end

    def Function_47_8F9A(): pass

    label("Function_47_8F9A")

    Sleep(8200)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_8FB4():
        OP_96(0xFE, 0x7D0, 0x9C4, 0x2FA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8FB4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_47_8F9A end

    def Function_48_8FD5(): pass

    label("Function_48_8FD5")

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
            "#1KSame day, 10: 30 -\x02",
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

    def lambda_93DA():
        OP_A6(0xFE, 0x0, 0x64, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_93DA)
    SetChrChipByIndex(0x26, 0x1F)
    SetChrSubChip(0x26, 0x0)
    OP_52(0x26, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_9406():
        OP_A6(0xFE, 0x0, 0x64, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_9406)
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

    def lambda_958E():

        label("loc_958E")

        TurnDirection(0xFE, 0x33, 500)
        Yield()
        Jump("loc_958E")

    QueueWorkItem2(0x2A, 2, lambda_958E)
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

    def lambda_95FB():
        OP_95(0xFE, -7500, 4700, 47500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_95FB)
    Sleep(50)
    ClearChrFlags(0x28, 0x4)

    def lambda_961D():
        OP_95(0xFE, -4500, 4700, 47500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_961D)
    Sleep(50)
    ClearChrFlags(0x27, 0x4)

    def lambda_963F():
        OP_95(0xFE, -4500, 4700, 47500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_963F)
    Sleep(50)
    ClearChrFlags(0x2A, 0x4)
    SetChrChipByIndex(0x2A, 0x1B)
    SetChrSubChip(0x2A, 0x0)

    def lambda_9669():
        OP_95(0xFE, -7500, 4700, 47500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9669)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    SetScenarioFlags(0x22, 7)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_48_8FD5 end

    def Function_49_969F(): pass

    label("Function_49_969F")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0x29, 0x17)
    SetChrSubChip(0x29, 0x0)

    def lambda_96BF():
        OP_96(0xFE, 0xFFFFE2B4, 0x9C4, 0x6978, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_96BF)

    ChrTalk(
        0x29,
        "#9AHa ha!\x02",
    )

    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x29, 0x19)
    SetChrSubChip(0x29, 0x2)
    Sound(251, 0, 60, 0)

    def lambda_96FF():
        OP_9D(0xFE, 0xFFFFE2B4, 0xDAC, 0x80E8, 0x5DC, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_96FF)
    WaitChrThread(0xFE, 1)
    Sound(815, 0, 100, 0)
    SetChrSubChip(0x29, 0x3)
    BeginChrThread(0x26, 3, 0, 54)
    Sleep(1000)
    SetChrSubChip(0x29, 0x4)

    def lambda_9737():
        OP_9D(0xFE, 0xFFFFE2B4, 0x9C4, 0x7D00, 0xC8, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9737)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x29, 0x16)
    SetChrSubChip(0x29, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_49_969F end

    def Function_50_9764(): pass

    label("Function_50_9764")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)

    def lambda_977C():
        OP_96(0xFE, 0xFFFFED40, 0x9C4, 0x6D60, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_977C)
    Sleep(500)

    ChrTalk(
        0x28,
        "#9AOh, oh!\x02",
    )

    WaitChrThread(0xFE, 1)
    Sound(844, 0, 70, 0)

    def lambda_97B9():
        OP_9D(0xFE, 0xFFFFED40, 0x9C4, 0x7DC8, 0x384, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_97B9)
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

    # Function_50_9764 end

    def Function_51_9845(): pass

    label("Function_51_9845")

    SetChrChipByIndex(0x2A, 0x1B)
    SetChrSubChip(0x2A, 0x0)

    def lambda_9852():
        OP_96(0xFE, 0xFFFFE0C0, 0x9C4, 0x7724, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9852)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x2A, 0x1A)
    SetChrSubChip(0x2A, 0x0)
    Return()

    # Function_51_9845 end

    def Function_52_9874(): pass

    label("Function_52_9874")


    def lambda_9879():
        OP_96(0xFE, 0xFFFFEE6C, 0x9C4, 0x7724, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9879)
    WaitChrThread(0xFE, 1)
    Sound(531, 0, 50, 0)
    SetChrSubChip(0xFE, 0x5)
    Return()

    # Function_52_9874 end

    def Function_53_989D(): pass

    label("Function_53_989D")

    OP_82(0xFA, 0xFA, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_98D7():
        OP_A6(0xFE, 0x0, 0x64, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_98D7)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1700, -500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x0, 0, 1700, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    PlayEffect(0x1, 0x1, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_999C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_999C)
    WaitChrThread(0xFE, 2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_53_989D end

    def Function_54_99B0(): pass

    label("Function_54_99B0")

    OP_82(0xFA, 0xFA, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(300)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(501, 0, 100, 0)

    def lambda_99F0():
        OP_A6(0xFE, 0x0, 0x64, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_99F0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x0, 0, 1700, -300, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    MoveCamera(43, 15, 5, 4000)
    SetCameraDistance(16000, 4000)
    Sound(985, 0, 100, 0)
    PlayEffect(0x1, 0x2, 0xFE, 0x1, 0, 1200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_9A98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9A98)
    WaitChrThread(0xFE, 2)
    StopEffect(0x2, 0x2)
    Return()

    # Function_54_99B0 end

    def Function_55_9AAC(): pass

    label("Function_55_9AAC")

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

    def lambda_9B2C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9B2C)
    Sound(501, 0, 50, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 2850, 200, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x0, 0, 2850, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x1D)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_55_9AAC end

    def Function_56_9BCC(): pass

    label("Function_56_9BCC")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 3100, 2500, 10400)
    OP_9F(0x1, -3900, 2500, 20900)
    OP_9F(0x1, -5600, 2500, 35700)
    OP_9F(0x2, 0xFE, 10000, 0x6)

    def lambda_9C08():
        OP_96(0xFE, 0xFFFFEA20, 0x1D4C, 0xED1C, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9C08)
    OP_D5(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1F4)
    Return()

    # Function_56_9BCC end

    def Function_57_9C31(): pass

    label("Function_57_9C31")

    Sleep(500)
    Sound(207, 0, 60, 0)
    Sleep(1000)

    label("loc_9C3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C5F")
    Sound(246, 0, 70, 0)
    Sleep(300)
    Sound(246, 0, 60, 0)
    Sleep(400)
    Jump("loc_9C3D")

    label("loc_9C5F")

    Return()

    # Function_57_9C31 end

    def Function_58_9C60(): pass

    label("Function_58_9C60")

    Sound(458, 0, 100, 0)
    Sound(486, 0, 100, 0)
    Sleep(2000)
    Sound(487, 0, 100, 0)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Return()

    # Function_58_9C60 end

    def Function_59_9C85(): pass

    label("Function_59_9C85")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FDirections to Orkis Tower\x01",
            "\"Defense Army\" is strict\x01",
            "It seems to be guarding.\x02\x03",
            "#00003F… … let's not go.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -5600, 2500, 34230, 180)
    EventEnd(0x4)
    Return()

    # Function_59_9C85 end

    def Function_60_9D0A(): pass

    label("Function_60_9D0A")

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
        "#10AWow! It is! Is it? Is it?\x02",
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
            "Come on, when I went by a while ago\x01",
            "There was not such a thing! Is it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Yuri")

    NpcTalk(
        0x36,
        "Yuri",
        "Chi, instant barricade ……\x02",
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

    def lambda_A122():
        OP_96(0xFE, 0x4DE4, 0x0, 0xFFFF6BE0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_A122)
    Sleep(1000)

    def lambda_A13F():
        OP_96(0xFE, 0x4DE4, 0x0, 0xFFFF4CA0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_A13F)
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
        "#N#10302FHuh, it's checkmate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#N#00000FOh, after that ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        "…… Now it's time to pursue!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        "Go down quietly!\x02",
    )

    CloseMessageWindow()
    SetChrName("Sykes")

    NpcTalk(
        0x36,
        "Sykes",
        "… Well, is not he?\x02",
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
            "Education\x01",
            "I'm going to Toko.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "Whew, incompetence becoming incompetent\x01",
            "Did you use your head?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2E, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x2E,
        (
            "Oh, you guys ……\x01",
            "A little color of reflection\x01",
            "Why do not you show it! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "To how many people we are\x01",
            "Are you bothering me …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "Yeah yeah, I understand.\x01",
            "I'm so excited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        (
            "When you get very angry\x01",
            "I will increase the number of fine wigs,\x01",
            "O Ba San.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x2E,
        "#4SOhhh ……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "Oh, with you guys\x01",
            "It will not change so much! Is it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x2E, 500)
    Sleep(100)

    ChrTalk(
        0xB,
        "Senpai, calm down … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "Look, anywhere quickly\x01",
            "Why do not you take it with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "Well, to give us penalties\x01",
            "I guess they can not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105Feh……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x2E, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00000F…… Kate Senpai.\x01",
            "Anyway now they\x01",
            "Let's take it to the headquarters.\x02\x03",
            "Forever here\x01",
            "Even as I park my car\x01",
            "I will not go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        "Cut … Yes.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2E, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x2E,
        (
            "Well then everyone in the support department,\x01",
            "Please help me with their children.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2E, 0xB, 500)
    Sleep(100)

    ChrTalk(
        0x2E,
        "Franz, please give me my best regards for the withdrawal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hah!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x2F, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00003F…………………………\x02",
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

    # Function_60_9D0A end

    def Function_61_A818(): pass

    label("Function_61_A818")

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

    # Function_61_A818 end

    def Function_62_A938(): pass

    label("Function_62_A938")

    OP_96(0x36, 0x4D12, 0x0, 0xFFFF7B58, 0x3A98, 0x0)
    OP_9F(0x0, 0x36)
    OP_9F(0x1, 19500, 390, -31390)
    OP_9F(0x1, 19420, 1410, -27710)
    OP_9F(0x1, 19800, 1410, -27710)
    OP_9F(0x2, 0x36, 15000, 0x6)
    OP_D5(0x36, 0xFFFFD8F0, 0xAFC8, 0xFFFFD8F0, 0x0)
    Return()

    # Function_62_A938 end

    def Function_63_A997(): pass

    label("Function_63_A997")

    OP_97(0x2E, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
    OP_95(0x2E, 18560, 10, -34510, 1000, 0x0)
    TurnDirection(0x2E, 0x101, 500)
    Return()

    # Function_63_A997 end

    def Function_64_A9C7(): pass

    label("Function_64_A9C7")

    OP_97(0xB, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
    OP_95(0xB, 21150, 0, -34360, 1000, 0x0)
    TurnDirection(0xB, 0x101, 500)
    Return()

    # Function_64_A9C7 end

    def Function_65_A9F7(): pass

    label("Function_65_A9F7")

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
            "Welcome.\x01",
            "How about juice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse me,\x01",
            "I am a person in the mission support department … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the interview with \"One push gourmet\"\x01",
            "I explained what came.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Oh, was that case?\x01",
            "I have heard a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well then, please.\x01",
            "New item of juice stand,\x01",
            "\"Nagasa tomato soda\" is!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_ADB4")

    ChrTalk(
        0x101,
        (
            "#00005FThis, indeed,\x01",
            "McDowell chairperson wit … …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, even after being chairman\x01",
            "Drink and drink without ever changing\x01",
            "We have received it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This means that that drink\x01",
            "It is an improved new product.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because we are softening bitterness with soda,\x01",
            "Everyone who is not good at tomatoes\x01",
            "It should be delicious and healthy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE7C")

    label("loc_ADB4")


    ChrTalk(
        0x101,
        "#00005FWell, tomatoes … … that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is a tomato juice\x01",
            "It is an improved new product.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because we are softening bitterness with soda,\x01",
            "Everyone who is not good at tomatoes\x01",
            "It should be delicious and healthy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE7C")


    ChrTalk(
        0x102,
        "#00109FI see, I see … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F(… … Hey Lloyd, are you going to drink it seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(And it's work, it can not be helped ……\x01",
            "Let's do our best and let's drink it. )\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd drank tomato soda.\x07\x00\x02",
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
            "Everyone's CP recovered 50.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00010F#4S…… ha ha ha ……! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FHooh, hey …!\x01",
            "Th-This is……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F…… It is bitterly bitter.\x02\x03",
            "#00211FOr, soda's Schwaszwa\x01",
            "I am trying to power it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, there is still room for improvement\x01",
            "It looks like it is …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Anyway, if you open your mouth\x01",
            "This classic drink,\x01",
            "\"Belverie juice\" please.\x02",
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
            "Lloyd drank Bellberry juice.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00102F(Kokoku …)\x01",
            "Oh, it is very tasty ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuff, as well as the reaction of the bitterness earlier\x01",
            "It seems likely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(When introducing by guide,\x01",
            "It might be better to recommend this one\x01",
            "I wish I could do it … …)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x172, 4)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_B4B3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B4B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_B4D0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B4D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_B4E3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B4E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_B4F6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B4F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_B513")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_B526")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_B543")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_B556")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_B573")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_B586")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_B5A3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B5A3")

    OP_29(0x80, 0x1, 0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B6A6")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I finished interviewing 6 dining places!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B69D")

    AnonymousTalk(
        0x101,
        (
            "#00003FMr. Grace right away\x01",
            "It seems I can go to the report … but …\x02\x03",
            "#00000FThe favorite of all six people still\x01",
            "It was not found.\x01",
            "Maybe I'll try harder?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_B69D")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_B6A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B777")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "All members of the Special Affairs Support Division\x01",
            "I found a favorite!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this all six people\x01",
            "I found a favorite.\x02\x03",
            "This is enough for the interview.\x01",
            "Let's go report to the airlines immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_B777")

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

    # Function_65_A9F7 end

    def Function_66_B7B1(): pass

    label("Function_66_B7B1")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ This place Orkis Tower ※\x01",
            "※ Staff only ※\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_66_B7B1 end

    def Function_67_B819(): pass

    label("Function_67_B819")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FNow preparing for tomorrow\x01",
            "The tower direction will be busy as well.\x02\x03",
            "Even though I do not have any business\x01",
            "Let's stop approaching.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -5600, 2500, 34230, 180)
    EventEnd(0x4)
    Return()

    # Function_67_B819 end

    def Function_68_B891(): pass

    label("Function_68_B891")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA68")
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
            "#12P#00101F…… Walking in front of the tower\x01",
            "I do not seem to get close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FAll right, I'm on the other guy over there\x01",
            "Once found, in no time\x01",
            "It seems that reinforcement will be called.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001F… Then, then\x01",
            "The effect on the strategy can not be avoided, either.\x02\x03",
            "#00003FLet's turn back inside unnoticed.\x02",
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
    Jump("loc_BAE1")

    label("loc_BA68")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The front of the tower is protected by magical soldiers.\x01",
            "It seems better to turn back.\x07\x00\x02",
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

    label("loc_BAE1")

    Return()

    # Function_68_B891 end

    def Function_69_BAE2(): pass

    label("Function_69_BAE2")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BAF3")
    Jump("loc_C386")

    label("loc_BAF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BDC5")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Charity event\x01",
            "\"~ Let's spread by everyone circle of reconstruction ~\"\x01",
            "In the case of\x01",
            "【Program Overview】\x01",
            "· Solo piano concert\x01",
            "· Miss · Crossbell Contest\x01",
            "· Mass gourmet contest\x01",
            "· Various art work classes\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Place: Crossbell Civic Center · Multipurpose Hall\x01",
            "Hall\x01",
            "Date: Today\x01",
            "Organizer: Cross Bell Chamber of Commerce / Crosbell City\x01",
            "In the case of\x01",
            "※ The participation fee of various events,\x01",
            "All will be used for funds for reconstruction assistance. In the case of\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_C386")

    label("loc_BDC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BFB6")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Civil Forum\x01",
            "\"~ Let's seriously think now,\x01",
            "Independence of national independence ~ \"\x01",
            "In the case of\x01",
            "【Program Overview】\x01",
            "· Independent national independence talked by experts\x01",
            "· Public discussion session by active autonomous state members\x01",
            "Place: Crossbell Civic Center · Multipurpose Hall\x01",
            "Date: Today\x01",
            "Organizer: Crossbell City / Crossbell Communication Company\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_C386")

    label("loc_BFB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C1A9")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Civil Forum\x01",
            "\"~ Let's seriously think now,\x01",
            "Independence of national independence ~ \"\x01",
            "In the case of\x01",
            "【Program Overview】\x01",
            "· Independent national independence talked by experts\x01",
            "· Public discussion session by active autonomous state members\x01",
            "Place: Crossbell Civic Center · Multipurpose Hall\x01",
            "Date: tomorrow\x01",
            "Organizer: Crossbell City / Crossbell Communication Company\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_C386")

    label("loc_C1A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C1B7")
    Jump("loc_C386")

    label("loc_C1B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C37D")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Investor seminar for beginners\x01",
            "\"- To understand the economy of tomorrow -\"\x01",
            "In the case of\x01",
            "Place: Crossbell Civic Center · Multipurpose Hall\x01",
            "Date: Today\x01",
            "Organizer: trade quotient rezero\x01",
            "※ Since there is room in the seat,\x01",
            "Join participation on the day\x01",
            "We are waiting for you by all means. In the case of\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_C386")

    label("loc_C37D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C386")

    label("loc_C386")

    TalkEnd(0xFF)
    Return()

    # Function_69_BAE2 end

    def Function_70_C38A(): pass

    label("Function_70_C38A")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked firmly.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C502")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C4A6")

    ChrTalk(
        0x101,
        (
            "#00003FPolice headquarters ……\x01",
            "There seems to be no one inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#00603F…… Since yesterday's martial law, this is\x01",
            "It is blocked by the Defense Forces.\x02\x03",
            "#00600F- Anyhow, I will hurry ahead now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYeah … It's okay.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C4FF")

    label("loc_C4A6")


    ChrTalk(
        0x101,
        (
            "#00003FPolice headquarters ……\x01",
            "There seems to be no one inside.\x02\x03",
            "#00001FAnyway, now let's hurry ahead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4FF")

    SetScenarioFlags(0x1, 5)

    label("loc_C502")

    TalkEnd(0xFF)
    Return()

    # Function_70_C38A end

    SaveToFile()

Try(main)
