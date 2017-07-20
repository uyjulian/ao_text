from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1540.bin",                # FileName
        "c1540",                    # MapName
        "c1540",                    # Location
        0x00AF,                     # MapIndex
        "ed7151",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 175, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1540",                  # 0
        "Lector clerk",         # 1
        "Major Muller",           # 2
        "Assistant Julia",             # 3
        "Assistant Kirika",           # 4
        "Republican officer",           # 5
        "Imperial army officer",             # 6
        "Republican officer",           # 7
        "Imperial army officer",             # 8
        "Royal Friendly Corps Corps",         # 9
        "Public guard",             # 10
        "Public guard",             # 11
        "Butler",                   # 12
        "Butler",                   # 13
        "A maid",                 # 14
        "A maid",                 # 15
        "Arios",               # 16
        "City official staff",             # 17
        "Pierre deputy director",         # 18
        "Policeman",                   # 19
        "Policeman",                   # 20
        "Policeman",                   # 21
        "Mayor of Dieter",         # 22
        "Prime Minister Osborne",         # 23
        "Prince Oliver",       # 24
        "Claudia Hime",         # 25
        "Prince Albert",         # 26
        "President Lock Smith",     # 27
        "McDowell",         # 28
        "Ian lawyer",           # 29
        "Dudley investigator",         # 30
        "Imperial terrorist",       # 31
        "Imperial terrorist",       # 32
        "Imperial terrorist",       # 33
        "Imperial terrorist",       # 34
        "Imperial terrorist",       # 35
        "Imperial terrorist",       # 36
        "Imperial terrorist",       # 37
        "Imperial terrorist",       # 38
        "Republic-based terrorists",     # 39
        "Republic-based terrorists",     # 40
        "Republic-based terrorists",     # 41
        "Republic-based terrorists",     # 42
        "Republic-based terrorists",     # 43
        "Republic-based terrorists",     # 44
        "Republic-based terrorists",     # 45
        "Republic-based terrorists",     # 46
        "Policeman",                   # 47
        "Policeman",                   # 48
        "Policeman",                   # 49
        "Policeman",                   # 50
        "A security guard",               # 51
        "A security guard",               # 52
        "dummy",                 # 53
        "Grace",               # 54
        "Raines",               # 55
        "A reporter",                   # 56
        "A reporter",                   # 57
        "A reporter",                   # 58
        "A reporter",                   # 59
        "A reporter",                   # 60
        "Airborne",                 # 61
        "Airborne",                 # 62
        "Chair",                   # 63
        "Chair",                   # 64
        "laptop",         # 65
        "Event monster",   # 66
        "Event monster",   # 67
        "Event monster",   # 68
        "SE control",                 # 69
        "bc1560",                 # 70
    ))

    ATBonus("ATBonus_A70", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_B50", 8, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_B54", 5, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_B58", 11, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_B5C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B60", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B64", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B68", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B6C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B30", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_B34", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_B38", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_B3C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_B40", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_B44", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_B48", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4C", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_B70", 0x000A, 3, 6, 45, 3, 3, 30, 0, "bc1560", 0x00000000, 100, 0, 0, 0,
        (
            ("ms84101.dat", "ms84301.dat", "ms84201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B50", "MonsterBattlePostion_B30", "ed7544", "ed7453", "ATBonus_A70"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch30000.itc",                   # 00
        "chr/ch11300.itc",                   # 01
        "chr/ch11200.itc",                   # 02
        "chr/ch13300.itc",                   # 03
        "chr/ch12400.itc",                   # 04
        "chr/ch41200.itc",                   # 05
        "chr/ch41000.itc",                   # 06
        "chr/ch41600.itc",                   # 07
        "chr/ch28600.itc",                   # 08
        "chr/ch25900.itc",                   # 09
        "chr/ch25600.itc",                   # 0A
        "chr/ch02400.itc",                   # 0B
        "chr/ch25800.itc",                   # 0C
        "chr/ch27800.itc",                   # 0D
        "chr/ch28200.itc",                   # 0E
        "chr/ch06400.itc",                   # 0F
        "chr/ch13302.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   4,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(171350,  0,       74290,   270,  453,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(174860,  0,       72669,   270,  453,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(85529,   0,       80650,   135,  453,  0x0, 0,   3,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(88940,   0,       80209,   135,  453,  0x0, 0,   5,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(171059,  0,       78610,   270,  453,  0x0, 0,   6,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(87379,   0,       80379,   135,  389,  0x0, 0,   5,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(172130,  0,       77980,   270,  389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(175050,  0,       71419,   271,  389,  0x0, 0,   7,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(88099,   0,       72809,   89,   389,  0x0, 0,   8,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(88260,   0,       71559,   89,   389,  0x0, 0,   8,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(170720,  0,       82220,   270,  389,  0x0, 0,   9,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294915116, 0,       124000,  180,  389,  0x0, 0,   12,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(173529,  0,       74540,   0,    389,  0x0, 0,   10,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4294917837, 0,       112459,  89,   389,  0x0, 0,   10,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(86529,   0,       80650,   135,  389,  0x0, 0,   11,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294915296, 0,       120730,  0,    389,  0x0, 0,   14,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(4294925497, 0,       128199,  0,    389,  0x0, 0,   15,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    236,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 28,  86.02999877929688,     83.37000274658203,     -1.0,                  5184.0,                [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -7.169166564941406,    -6.947500228881836,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 29,  36.47999954223633,     0.0,                   -1.0,                  56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -12.15999984741211,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 133, 9.699999809265137,     3.5,                   -1.0,                  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -3.2333333492279053,   -1.75,                 0.20000001788139343,   1.0])
    DeclEvent(0x0000, 0, 134, 91.69999694824219,     76.5,                  -1.0,                  9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -45.849998474121094,   -25.5,                 0.20000001788139343,   1.0])

    DeclActor(80610,   0,       2930,    1000,    80610,   1500,    2930,    0x007C, 0,  132, 0x0000)
    DeclActor(86730,   0,       3250,    1000,    86730,   1500,    3250,    0x007C, 0,  132, 0x0000)

    ChipFrameInfo(3540, 0)                                       # 0

    ScpFunction((
        "Function_0_DD4",          # 00, 0
        "Function_1_E84",          # 01, 1
        "Function_2_ED7",          # 02, 2
        "Function_3_130D",         # 03, 3
        "Function_4_150C",         # 04, 4
        "Function_5_15AB",         # 05, 5
        "Function_6_169B",         # 06, 6
        "Function_7_1918",         # 07, 7
        "Function_8_199C",         # 08, 8
        "Function_9_1C7B",         # 09, 9
        "Function_10_1D1C",        # 0A, 10
        "Function_11_2065",        # 0B, 11
        "Function_12_21FE",        # 0C, 12
        "Function_13_226F",        # 0D, 13
        "Function_14_2319",        # 0E, 14
        "Function_15_23BA",        # 0F, 15
        "Function_16_249E",        # 10, 16
        "Function_17_24BC",        # 11, 17
        "Function_18_2548",        # 12, 18
        "Function_19_25D7",        # 13, 19
        "Function_20_2AAD",        # 14, 20
        "Function_21_2B44",        # 15, 21
        "Function_22_2C93",        # 16, 22
        "Function_23_2D23",        # 17, 23
        "Function_24_2E1D",        # 18, 24
        "Function_25_2E9C",        # 19, 25
        "Function_26_39AA",        # 1A, 26
        "Function_27_4125",        # 1B, 27
        "Function_28_4898",        # 1C, 28
        "Function_29_4E82",        # 1D, 29
        "Function_30_536C",        # 1E, 30
        "Function_31_5373",        # 1F, 31
        "Function_32_539C",        # 20, 32
        "Function_33_6163",        # 21, 33
        "Function_34_61FA",        # 22, 34
        "Function_35_624B",        # 23, 35
        "Function_36_628B",        # 24, 36
        "Function_37_707C",        # 25, 37
        "Function_38_730B",        # 26, 38
        "Function_39_759A",        # 27, 39
        "Function_40_79C9",        # 28, 40
        "Function_41_7A82",        # 29, 41
        "Function_42_8C3E",        # 2A, 42
        "Function_43_9903",        # 2B, 43
        "Function_44_AEB2",        # 2C, 44
        "Function_45_AF7F",        # 2D, 45
        "Function_46_B04C",        # 2E, 46
        "Function_47_B0A7",        # 2F, 47
        "Function_48_B123",        # 30, 48
        "Function_49_B181",        # 31, 49
        "Function_50_B24E",        # 32, 50
        "Function_51_B31E",        # 33, 51
        "Function_52_B398",        # 34, 52
        "Function_53_B40B",        # 35, 53
        "Function_54_B47E",        # 36, 54
        "Function_55_B4EA",        # 37, 55
        "Function_56_B53F",        # 38, 56
        "Function_57_B594",        # 39, 57
        "Function_58_B607",        # 3A, 58
        "Function_59_B788",        # 3B, 59
        "Function_60_D143",        # 3C, 60
        "Function_61_D1D4",        # 3D, 61
        "Function_62_D237",        # 3E, 62
        "Function_63_D2E7",        # 3F, 63
        "Function_64_D4E9",        # 40, 64
        "Function_65_D589",        # 41, 65
        "Function_66_D5C0",        # 42, 66
        "Function_67_D63B",        # 43, 67
        "Function_68_D672",        # 44, 68
        "Function_69_D6ED",        # 45, 69
        "Function_70_D931",        # 46, 70
        "Function_71_D9EC",        # 47, 71
        "Function_72_DC18",        # 48, 72
        "Function_73_DC5F",        # 49, 73
        "Function_74_DCA8",        # 4A, 74
        "Function_75_DCEB",        # 4B, 75
        "Function_76_DD45",        # 4C, 76
        "Function_77_DEA6",        # 4D, 77
        "Function_78_E158",        # 4E, 78
        "Function_79_E265",        # 4F, 79
        "Function_80_E2C4",        # 50, 80
        "Function_81_E30B",        # 51, 81
        "Function_82_E539",        # 52, 82
        "Function_83_E609",        # 53, 83
        "Function_84_E689",        # 54, 84
        "Function_85_E709",        # 55, 85
        "Function_86_E789",        # 56, 86
        "Function_87_E7ED",        # 57, 87
        "Function_88_E851",        # 58, 88
        "Function_89_E8A7",        # 59, 89
        "Function_90_E918",        # 5A, 90
        "Function_91_E937",        # 5B, 91
        "Function_92_E956",        # 5C, 92
        "Function_93_E975",        # 5D, 93
        "Function_94_E994",        # 5E, 94
        "Function_95_E9B3",        # 5F, 95
        "Function_96_E9D2",        # 60, 96
        "Function_97_EA08",        # 61, 97
        "Function_98_EA5C",        # 62, 98
        "Function_99_EAB0",        # 63, 99
        "Function_100_EACC",       # 64, 100
        "Function_101_EC63",       # 65, 101
        "Function_102_EDF4",       # 66, 102
        "Function_103_EE44",       # 67, 103
        "Function_104_EE87",       # 68, 104
        "Function_105_EEE3",       # 69, 105
        "Function_106_EF0A",       # 6A, 106
        "Function_107_EF31",       # 6B, 107
        "Function_108_EF58",       # 6C, 108
        "Function_109_EF7F",       # 6D, 109
        "Function_110_EFDD",       # 6E, 110
        "Function_111_F030",       # 6F, 111
        "Function_112_F097",       # 70, 112
        "Function_113_F0EE",       # 71, 113
        "Function_114_F159",       # 72, 114
        "Function_115_F1B0",       # 73, 115
        "Function_116_F1D2",       # 74, 116
        "Function_117_F219",       # 75, 117
        "Function_118_F256",       # 76, 118
        "Function_119_F27D",       # 77, 119
        "Function_120_F2A4",       # 78, 120
        "Function_121_F2CB",       # 79, 121
        "Function_122_F2F2",       # 7A, 122
        "Function_123_F30F",       # 7B, 123
        "Function_124_F329",       # 7C, 124
        "Function_125_F35B",       # 7D, 125
        "Function_126_10B44",      # 7E, 126
        "Function_127_10B5F",      # 7F, 127
        "Function_128_10B7B",      # 80, 128
        "Function_129_1147C",      # 81, 129
        "Function_130_12960",      # 82, 130
        "Function_131_12978",      # 83, 131
        "Function_132_129F1",      # 84, 132
        "Function_133_12CE1",      # 85, 133
        "Function_134_12D53",      # 86, 134
        "Function_135_12DBE",      # 87, 135
    ))


    def Function_0_DD4(): pass

    label("Function_0_DD4")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_E0C"),
        (1, "loc_E18"),
        (2, "loc_E24"),
        (3, "loc_E30"),
        (4, "loc_E3C"),
        (5, "loc_E48"),
        (6, "loc_E54"),
        (SWITCH_DEFAULT, "loc_E60"),
    )


    label("loc_E0C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E18")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E24")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E30")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E3C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E48")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E54")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E60")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E6C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E83")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E83")

    Return()

    # Function_0_DD4 end

    def Function_1_E84(): pass

    label("Function_1_E84")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ED6")
    OP_95(0xFE, -4530, 0, -2520, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 20720, 0, -2520, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    Jump("Function_1_E84")

    label("loc_ED6")

    Return()

    # Function_1_E84 end

    def Function_2_ED7(): pass

    label("Function_2_ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 4)), scpexpr(EXPR_END)), "loc_EE5")
    Jump("loc_11BA")

    label("loc_EE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_1068")
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, 11220, 0, 2300, 180)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 7990, 0, 2300, 180)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 20720, 0, -2520, 270)
    BeginChrThread(0x1C, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6C")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xD, 75530, 0, 2000, 0)
    SetChrPos(0xC, 73730, 0, 2000, 0)

    label("loc_F6C")

    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 170720, 0, 82220, 270)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 173530, 0, 74540, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0xB, 87380, 0, 84160, 180)
    SetChrChipByIndex(0xB, 0x10)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0x17, 89160, 0, 85000, 0)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -41800, 0, 128199, 0)
    SetChrFlags(0x19, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -52180, 0, 124000, 180)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -49460, 0, 112460, 89)
    SetChrFlags(0x16, 0x10)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -52000, 0, 120730, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_104D")
    Event(0, 26)

    label("loc_104D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1063")
    Event(0, 27)

    label("loc_1063")

    Jump("loc_11BA")

    label("loc_1068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_11BA")
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, 11220, 0, 2300, 180)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 7990, 0, 2300, 180)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 20720, 0, -2520, 270)
    BeginChrThread(0x1C, 0, 0, 1)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xA, 174860, 0, 72670, 270)
    SetChrPos(0x10, 175050, 0, 71420, 271)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x40)
    SetChrPos(0x9, 171350, 0, 74290, 270)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    SetChrPos(0xD, 171060, 0, 78610, 270)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 172130, 0, 77980, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 84390, 150, 84160, 180)
    SetChrChipByIndex(0xB, 0x10)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x40)
    SetChrPos(0xC, 88940, 0, 80210, 135)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 87380, 0, 80380, 135)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 88100, 0, 72810, 89)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 88260, 0, 71560, 89)

    label("loc_11BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11E4")
    ClearScenarioFlags(0x25, 1)
    Call(0, 30)

    label("loc_11E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_11F8")
    ClearScenarioFlags(0x22, 0)
    Event(0, 32)
    Jump("loc_12C7")

    label("loc_11F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_120F")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 36)
    Jump("loc_12C7")

    label("loc_120F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1226")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 0)
    Event(0, 39)
    Jump("loc_12C7")

    label("loc_1226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_123D")
    ClearScenarioFlags(0x22, 3)
    SetScenarioFlags(0x0, 0)
    Event(0, 41)
    Jump("loc_12C7")

    label("loc_123D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_1251")
    ClearScenarioFlags(0x22, 4)
    Event(0, 42)
    Jump("loc_12C7")

    label("loc_1251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_1265")
    ClearScenarioFlags(0x22, 5)
    Event(0, 43)
    Jump("loc_12C7")

    label("loc_1265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_1279")
    ClearScenarioFlags(0x22, 6)
    Event(0, 58)
    Jump("loc_12C7")

    label("loc_1279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_128D")
    ClearScenarioFlags(0x22, 7)
    Event(0, 59)
    Jump("loc_12C7")

    label("loc_128D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_12A1")
    ClearScenarioFlags(0x23, 0)
    Event(0, 125)
    Jump("loc_12C7")

    label("loc_12A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_12B8")
    ClearScenarioFlags(0x23, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 129)
    Jump("loc_12C7")

    label("loc_12B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_12C7")
    ClearScenarioFlags(0x23, 2)
    Event(0, 128)

    label("loc_12C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12E5")
    Event(0, 37)

    label("loc_12E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_130C")
    Event(0, 38)

    label("loc_130C")

    Return()

    # Function_2_ED7 end

    def Function_3_130D(): pass

    label("Function_3_130D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1322")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_1322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1336")
    VolumeBGM(0x46, 0xC8)

    label("loc_1336")

    OP_10(0x13, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_134D")
    OP_10(0x13, 0x1)
    OP_10(0x3, 0x0)

    label("loc_134D")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_136A")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_136A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_137D")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_137D")

    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13A9")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    OP_1B(0xD, 0x0, 0x87)
    Jump("loc_13AE")

    label("loc_13A9")

    OP_1B(0xD, 0xFF, 0xFFFF)

    label("loc_13AE")

    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFrame(0xFF, "paper", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1423")
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)

    label("loc_1423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1437")
    ClearMapObjFlags(0xE, 0x4)

    label("loc_1437")

    ClearMapObjFlags(0x9, 0x10)
    ClearMapObjFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_1464")
    ClearMapObjFlags(0x8, 0x10)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)

    label("loc_1464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_END)), "loc_148B")
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x10)
    ClearMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0xD, 0x4)

    label("loc_148B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14D0")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_14D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_150B")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)

    label("loc_150B")

    Return()

    # Function_3_130D end

    def Function_4_150C(): pass

    label("Function_4_150C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_155C")

    ChrTalk(
        0xFE,
        (
            "Half of the place to leave the plenary session … …\x01",
            "I hope that you will not be aware of it until the end.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15A7")

    label("loc_155C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_15A7")

    ChrTalk(
        0xFE,
        "We are in the middle of the plenary session.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Take a look at the inside in the corridor room.\x02",
    )

    CloseMessageWindow()

    label("loc_15A7")

    TalkEnd(0xFE)
    Return()

    # Function_4_150C end

    def Function_5_15AB(): pass

    label("Function_5_15AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_1622")

    ChrTalk(
        0xFE,
        (
            "Now the staff members\x01",
            "Reopen the conference hall\x01",
            "I am setting the setting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please help yourself.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1697")

    label("loc_1622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_1697")

    ChrTalk(
        0xFE,
        (
            "The end time of the first half of the meeting,\x01",
            "We are planning 15:00.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Depending on the circumstances it is somewhat around\x01",
            "I think that there is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1697")

    TalkEnd(0xFE)
    Return()

    # Function_5_15AB end

    def Function_6_169B(): pass

    label("Function_6_169B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_17CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175C")

    ChrTalk(
        0xFE,
        (
            "Not yet to the terrorists\x01",
            "It seems that you can not see movement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is no clearance for ants to crawl\x01",
            "To be able to break through this alert system\x01",
            "I do not think so ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can not take care of it until the end.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_17CA")

    label("loc_175C")


    ChrTalk(
        0xFE,
        (
            "There is no clearance for ants to crawl\x01",
            "To be able to break through this alert system\x01",
            "I do not think so ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can not take care of it until the end.\x02",
    )

    CloseMessageWindow()

    label("loc_17CA")

    Jump("loc_1914")

    label("loc_17CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_1914")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188F")

    ChrTalk(
        0xFE,
        "At last the meeting started.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What are the terrorists\x01",
            "I can not read whether I will aim for it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway we are\x01",
            "According to the instructions of the countermeasures office,\x01",
            "It just fulfills the given role.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1914")

    label("loc_188F")


    ChrTalk(
        0xFE,
        (
            "What are the terrorists\x01",
            "I can not read whether I will aim for it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway we are\x01",
            "According to the instructions of the countermeasures office,\x01",
            "It just fulfills the given role.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1914")

    TalkEnd(0xFE)
    Return()

    # Function_6_169B end

    def Function_7_1918(): pass

    label("Function_7_1918")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_192D")
    Call(0, 8)
    Jump("loc_1998")

    label("loc_192D")


    ChrTalk(
        0xA,
        (
            "#07103FLeave this place to us,\x01",
            "You guys are trying to watch out for surroundings.\x02\x03",
            "#07100FPlease take care of the goddess for you as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1998")

    TalkEnd(0xFE)
    Return()

    # Function_7_1918 end

    def Function_8_199C(): pass

    label("Function_8_199C")

    OP_4B(0x10, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x10, 0x0, 0)
    TurnDirection(0xA, 0x0, 0)

    ChrTalk(
        0x10,
        "Everyone, good work\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07102FOh, the SSS \x02\x03",
            "The floor near the conference center\x01",
            "I hear you are wary of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, somehow\x01",
            "I was able to get screwed in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuhu, but\x01",
            "This room has considerable strength\x01",
            "It seems to be complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, almost no matter what\x01",
            "Because he is an officer class man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes, even those who are here\x01",
            "You seem to be able to deal with the situation that is awful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FYeah yeah, more than anything\x01",
            "The sword of Yuria Assoc.\x01",
            "I listen that it is beautifully bursting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07104FHaha, you flatter me\x02\x03",
            "#07100F……Anyways,\x01",
            "Whatever person may appear\x01",
            "Do not touch your finger with your father.\x02\x03",
            "Leave this place to us,\x01",
            "You guys are trying to watch out for surroundings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FRight, got it\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0x10, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    SetScenarioFlags(0x1C3, 0)
    Call(0, 31)
    Return()

    # Function_8_199C end

    def Function_9_1C7B(): pass

    label("Function_9_1C7B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C90")
    Call(0, 8)
    Jump("loc_1D18")

    label("loc_1C90")


    ChrTalk(
        0xFE,
        (
            "Whatever happens to our royal guards\x01",
            "I will protect Prince Claudia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since we do not need to worry about the meeting place,\x01",
            "Everyone please keep on a patrol.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D18")

    TalkEnd(0xFE)
    Return()

    # Function_9_1C7B end

    def Function_10_1D1C(): pass

    label("Function_10_1D1C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FCA")

    ChrTalk(
        0x101,
        "#00000FOh hello Muller\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FNice to see you\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#07302FOh you guys\x02\x03",
            "#07303FHmm, I can not take care of it\x01",
            "Is it such a place as peaceful?\x02\x03",
            "The leaders also did not appear to ruff their voices,\x01",
            "The meeting itself seems to be doing well.\x02\x03",
            "#07308FIf it ends safely as it is,\x01",
            "The load on the shoulder of the prince also gets a little lighter … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FMulller?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FSeems like you have a lot on your mind\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#07302FHuh, well.\x01",
            "Even though it is said that he himself\x01",
            "It's because of the seeds ……\x02\x03",
            "#07303FSeems I'm saying too much\x02\x03",
            "Anyway, what I should do now\x01",
            "Only to fulfill the duty as an escort -\x02\x03",
            "#07300FYou guys are also you,\x01",
            "Fulfill their duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, roger that\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C3, 2)
    Call(0, 31)
    Jump("loc_2061")

    label("loc_1FCA")


    ChrTalk(
        0x9,
        (
            "#07303FThose in the conference only have to watch over\x01",
            "I can not but … the martial art seems like a military officer\x01",
            "Until it fulfills the duty of escort.\x02\x03",
            "#07300FYou guys are also you,\x01",
            "Fulfill their duties.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2061")

    TalkEnd(0xFE)
    Return()

    # Function_10_1D1C end

    def Function_11_2065(): pass

    label("Function_11_2065")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2076")
    Jump("loc_21FA")

    label("loc_2076")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_21FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_219C")

    ChrTalk(
        0xFE,
        (
            "Hmm, you guys\x01",
            "Is it a Special Affairs Division of Circle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… …. It is hard work for you.\x01",
            "As you can see,\x01",
            "There is nothing abnormal here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Know the room,\x01",
            "Do not wander indefinitely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FIs that … Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F(What is wrong, is not it.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F(Oh, there is nothing to catch on.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_21FA")

    label("loc_219C")


    ChrTalk(
        0xFE,
        (
            "As you can see,\x01",
            "There is nothing abnormal here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Know the room,\x01",
            "Do not wander indefinitely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21FA")

    TalkEnd(0xFE)
    Return()

    # Function_11_2065 end

    def Function_12_21FE(): pass

    label("Function_12_21FE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "… … When you make a noise,\x01",
            "Because it leaks to the meeting place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Repeatedly,\x01",
            "Please be quiet here.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_21FE end

    def Function_13_226F(): pass

    label("Function_13_226F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "In the opposite waiting room, Mr. Arios and\x01",
            "The president's aide adviser\x01",
            "It seems like you are talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently I heard from you,\x01",
            "What on earth is it like?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_226F end

    def Function_14_2319(): pass

    label("Function_14_2319")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "This is the empire and the kingdom\x01",
            "People of your aides will refrain\x01",
            "It is a room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "- Yes, that is, here\x01",
            "There was Assassin Yulia!\x01",
            "Just thinking about screaming things.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_2319 end

    def Function_15_23BA(): pass

    label("Function_15_23BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_23CB")
    Jump("loc_249A")

    label("loc_23CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_249A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23EA")
    TalkEnd(0xFE)
    Call(0, 25)
    Return()

    label("loc_23EA")


    ChrTalk(
        0xB,
        (
            "#12004FI think there is something I want to say ….\x01",
            "Now they are mutual\x01",
            "Let's watch over the course.\x02\x03",
            "#12000FIn terms of vigilance,\x01",
            "I and your standing position are also\x01",
            "That is unchanged.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_249A")

    TalkEnd(0xFE)
    Return()

    # Function_15_23BA end

    def Function_16_249E(): pass

    label("Function_16_249E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_24AF")
    Jump("loc_24B8")

    label("loc_24AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_24B8")

    label("loc_24B8")

    TalkEnd(0xFE)
    Return()

    # Function_16_249E end

    def Function_17_24BC(): pass

    label("Function_17_24BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_24CD")
    Jump("loc_2544")

    label("loc_24CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2544")

    ChrTalk(
        0xFE,
        (
            "Hmm, everyone\x01",
            "Is it a special department for patrols in charge?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank you for your hard work.\x01",
            "If you have something please tell me anytime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2544")

    TalkEnd(0xFE)
    Return()

    # Function_17_24BC end

    def Function_18_2548(): pass

    label("Function_18_2548")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Apparently the meeting seems to be doing fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Unlike Republic Parliament, opposition forces\x01",
            "There is no persistent pursuit, President His Excellency also\x01",
            "Is not it easy for me?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_2548 end

    def Function_19_25D7(): pass

    label("Function_19_25D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_297C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F4")

    ChrTalk(
        0xFE,
        "You are the Special Affairs Support Division …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yesterday, Dr. Albert's Excellency\x01",
            "I heard that you became indebted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, thank you for your help\x01",
            "Rather it is ours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah, to the expert's medical knowledge\x01",
            "It was truly helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, indeed Grand Court of Honorable\x01",
            "A very excellent person as a doctor\x01",
            "Because we came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway,\x01",
            "Your Excellency very much about you\x01",
            "You seem to like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this way you are actually seeing\x01",
            "I am also happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FWell, thanks for that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100Fthank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C3, 3)
    Jump("loc_2977")

    label("loc_27F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2907")

    ChrTalk(
        0xFE,
        (
            "By the way, apparently\x01",
            "The possibility of terrorists appearing\x01",
            "It seems there is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At such an international conference place\x01",
            "Although it is always supposed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the unlikely event, the leaders\x01",
            "I can not expose it to danger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Put each other up,\x01",
            "Let's do what we should do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2977")

    label("loc_2907")


    ChrTalk(
        0xFE,
        (
            "Information on terrorists\x01",
            "It reaches this ear too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Put each other up,\x01",
            "Let's do what we should do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2977")

    Jump("loc_2AA9")

    label("loc_297C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A39")

    ChrTalk(
        0xFE,
        (
            "You are a member of the Special Affairs Division.\x01",
            "Congratulations on your patrol work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Information on terrorists\x01",
            "It reaches this ear too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Put each other up,\x01",
            "Let's do what we should do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2AA9")

    label("loc_2A39")


    ChrTalk(
        0xFE,
        (
            "Information on terrorists\x01",
            "It reaches this ear too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Put each other up,\x01",
            "Let's do what we should do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AA9")

    TalkEnd(0xFE)
    Return()

    # Function_19_25D7 end

    def Function_20_2AAD(): pass

    label("Function_20_2AAD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "In this trade meeting,\x01",
            "For our Remiferia\x01",
            "It is a very useful meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For further development of the country,\x01",
            "To a fruitful achievement\x01",
            "I will be expecting by all means.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_2AAD end

    def Function_21_2B44(): pass

    label("Function_21_2B44")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2C86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C4A")

    ChrTalk(
        0xFE,
        "Hmm, but it's a big view.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No way, terrorists\x01",
            "To fly this sky is\x01",
            "I do not think so ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "……… Haha, that's nothing.\x01",
            "Is not there such a thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(… … something, it looks painfully behind.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2C81")

    label("loc_2C4A")


    ChrTalk(
        0xFE,
        (
            "Is not it … no …\x01",
            "Apparently I seem to be tired.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C81")

    Jump("loc_2C8F")

    label("loc_2C86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2C8F")

    label("loc_2C8F")

    TalkEnd(0xFE)
    Return()

    # Function_21_2B44 end

    def Function_22_2C93(): pass

    label("Function_22_2C93")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well, later\x01",
            "With this microphone tidied ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, but until recently\x01",
            "The heads were lined up behind this\x01",
            "I feel a little tense somewhat if I think.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_2C93 end

    def Function_23_2D23(): pass

    label("Function_23_2D23")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DEA")

    ChrTalk(
        0xFE,
        (
            "Wipe off ……\x01",
            "Yeah, it is fun.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0xFE,
        (
            "The latter half of the conference also\x01",
            "Comfortably room your room\x01",
            "Because it is when you do not use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm cleaning a lot of my heart!\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x59, 0x0)
    SetScenarioFlags(0x0, 6)
    Jump("loc_2E19")

    label("loc_2DEA")


    ChrTalk(
        0xFE,
        (
            "Wipe off ……\x01",
            "Yeah, it is fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E19")

    TalkEnd(0xFE)
    Return()

    # Function_23_2D23 end

    def Function_24_2E1D(): pass

    label("Function_24_2E1D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Deputy Director-General, in such a place\x01",
            "Did you mean something twilly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well it does not get in the way,\x01",
            "…… But something you care.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_2E1D end

    def Function_25_2E9C(): pass

    label("Function_25_2E9C")

    EventBegin(0x0)
    Fade(500)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12000.itp")
    OP_4B(0xC, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_68(83610, 1300, 82220, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15400, 0)
    SetChrPos(0x101, 84860, 0, 82570, 0)
    SetChrPos(0x102, 83260, 0, 81870, 0)
    SetChrPos(0x103, 84860, 0, 81470, 0)
    SetChrPos(0x104, 83060, 0, 80570, 0)
    SetChrPos(0x109, 85060, 0, 80570, 0)
    SetChrPos(0x105, 83460, 0, 79870, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_END)), "loc_30D3")

    ChrTalk(
        0xB,
        (
            "#5P#12000FOh, you guys.\x01",
            "Perhaps you are on guard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00001FKilika?\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xB,
        (
            "It seems like that, again something\x01",
            "I wonder if I grabbed new information.\x02\x03",
            "Apparently also in \"Arseille\"\x01",
            "It seems they were invited.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_34F5")

    label("loc_30D3")


    ChrTalk(
        0xB,
        (
            "#5P#12000Fyou……\x01",
            "Huh, it's been a long time.\x02\x03",
            "Perhaps you are on guard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FKilika?\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xB,
        (
            "Well, when I saw you before\x01",
            "The position is also different - again\x01",
            "Let me introduce myself.\x02\x03",
            "In the Republic of Calvert\x01",
            "He is presidential aide,\x01",
            "Kirika Lawran.\x02\x03",
            "I have other titles ….\x01",
            "Well it is not to talk daringly.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        "#00003F--I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FBy the way, I mentioned earlier\x01",
            "What is an entertainer producer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#12004FHuhu, it also\x01",
            "It is one of certain titles.\x02\x03",
            "#12002FNaturally even the office,\x01",
            "It exists in the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIndeed, on that side\x01",
            "There is not a blow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302F(Hehe, the face of the table\x01",
            "Is it a woman intelligence officer who uses more than one? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309F(Well, that kind of mysterious\x01",
            "Kirika may also be nice. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106F(Senpai, that remark to the drift\x01",
            "It seems like lack of tension … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#12002FHuhu, on my face\x01",
            "I wonder if something is attached?\x02\x03",
            "#12004FYes Yes--\x01",
            "By the way, you guys.\x02\x03",
            "#12000FAnything yesterday to \"Arseille\"\x01",
            "You seem to have been invited?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34F5")

    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#12P#00105FHuh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201FI'm not surprised somehow\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00306FYeah, seriously\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#12004FWuh, well Well itself\x01",
            "Though it is not a big deal.\x02\x03",
            "#12000FSo …\x01",
            "Did you hear interesting stories?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYes, just some advice\x02\x03",
            "#00001FHowever,\x01",
            "There are many things I do not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#12004FI see.\x02\x03",
            "Well, that is\x01",
            "This is also the same thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#12000FThis is just hypothetical\x02\x03",
            "If I had some scenario\x01",
            "As I was imagining -\x01",
            "It does not always come true.\x02\x03",
            "#12003FAs there are multiple speculations involved,\x01",
            "An uncertain element\x01",
            "Everyone holds the same thing.\x02\x03",
            "What will happen from now,\x01",
            "Or will not anything happen?\x02\x03",
            "#12000FAt this time, to anyone\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FI'm sure that's true but\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10304FHeh, you are quite right it seems\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#12004FAnyway, I want to say\x01",
            "That I am in the position to protect the President\x01",
            "That's no mistake.\x02\x03",
            "In other words, in that sense\x01",
            "The standing position is the same with you.\x02\x03",
            "#12000FIn short, each other's success\x01",
            "Let's watch over it.\x02\x03",
            "For more than that … …\x01",
            "I do not mean to speak here now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FI see…\x01",
            "No, it was helpful enough.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0xC, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x1C3, 4)
    Call(0, 31)
    EventEnd(0x5)
    Return()

    # Function_25_2E9C end

    def Function_26_39AA(): pass

    label("Function_26_39AA")

    EventBegin(0x0)
    Fade(500)
    OP_68(86650, 1400, 75180, 0)
    MoveCamera(33, 8, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21450, 0)
    SetChrPos(0x101, 87120, 0, 70000, 0)
    SetChrPos(0x102, 86120, 0, 70000, 0)
    SetChrPos(0x103, 87120, 0, 68500, 0)
    SetChrPos(0x104, 86120, 0, 68500, 0)
    SetChrPos(0x109, 87120, 0, 67000, 0)
    SetChrPos(0x105, 86120, 0, 67000, 0)
    OP_4B(0x17, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#00005F#12P(That is……\x01",
            "Arios and Mr. Kirika? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00105F#12P(Looks like, what kind of story are you talking about?\x01",
            "I wonder … ….? )\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(88320, 1500, 84360, 0)
    MoveCamera(38, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    OP_0D()

    ChrTalk(
        0x17,
        (
            "#6P#01403F#11P── It is almost a year since I left the guild.\x02\x03",
            "#01400FDid you get used to the new place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12004F#6P… as it is.\x02\x03",
            "#12000FWhen I was in the guild\x01",
            "It is not comparable\x01",
            "It is working though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#6P#01403F#11PIs that right…\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)
    SetChrSubChip(0xB, 0x1)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#12000F#6P…… Shizuku-chan\x01",
            "How are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#6P#01402F#11POh, it is too good to hear a bit\x01",
            "She always cheerful.\x02\x03",
            "#01404FRecently, I was blessed with encounter.\x01",
            "…… I began to laugh a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12004F#6PIs that so,\x01",
            "That is a good thing.\x02\x03",
            "#12003F….\x02\x03",
            "Saya passed away ……\x01",
            "Have you been five years already?\x02\x03",
            "#12000FI met you for the first time\x01",
            "It was six years ago … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11P#01404FSix years ago … That was right.\x02\x03",
            "At that time, I was surprised\x01",
            "You say that you were awkward\x01",
            "I met a friend Saya by accident in this town ……\x02\x03",
            "Do not be shy,\x01",
            "In the form that Saya's guy pulls forcibly\x01",
            "Were you staying at our house?\x02\x03",
            "#01402FThree years ago with you like that\x01",
            "When we meet again at the guild of Libert\x01",
            "I was surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12004F#6PHehe, it is.\x01",
            "Truly the margin of people is strange\x01",
            "It is thought.\x02\x03",
            "#12003F…… I'm that one bunch of meals\x01",
            "I will not forget your warmth all my life.\x02\x03",
            "#12001FAfter all, returning that benefit directly\x01",
            "I could not do it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11P#01404F… …. No, I think so\x01",
            "Just got it\x01",
            "Saya probably was pleased.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(86040, 1500, 67910, 0)
    MoveCamera(46, 20, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15440, 0)
    OP_4C(0x17, 0xFF)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00005F#11P(… … apparently, for two people\x01",
            "From before get acquainted with the guild\x01",
            "She seems to have some acquaintance. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12P(Yes, but no more\x01",
            "I want to eavesdrop\x01",
            "It feels bad. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00203F(That's fine, do not disturb me\x01",
            "Let's draw it. )\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 86960, 0, 68320, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x1C2, 6)
    EventEnd(0x5)
    Return()

    # Function_26_39AA end

    def Function_27_4125(): pass

    label("Function_27_4125")

    EventBegin(0x0)
    Fade(500)
    OP_68(89970, 1500, 79740, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 89590, 0, 78000, 315)
    SetChrPos(0x102, 90800, 0, 78000, 315)
    SetChrPos(0x103, 89590, 0, 76500, 315)
    SetChrPos(0x104, 90800, 0, 76500, 315)
    SetChrPos(0x109, 89590, 0, 75000, 315)
    SetChrPos(0x105, 90800, 0, 75000, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x17, 0xFF)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00005F(That is……\x01",
            "Arios and Mr. Kirika? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105F(Looks like, what kind of story are you talking about?\x01",
            "I wonder … ….? )\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(88320, 1500, 84360, 0)
    MoveCamera(38, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    OP_0D()

    ChrTalk(
        0x17,
        (
            "#6P#01403F#11P── It is almost a year since I left the guild.\x02\x03",
            "#01400FDid you get used to the new place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12004F#6P… as it is.\x02\x03",
            "#12000FWhen I was in the guild\x01",
            "It is not comparable\x01",
            "It is working though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#6P#01403F#11PIs that right…\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)
    SetChrSubChip(0xB, 0x1)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#12000F#6P…… Shizuku-chan\x01",
            "How are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#6P#01402F#11POh, it is too good to hear a bit\x01",
            "She always cheerful.\x02\x03",
            "#01404FRecently, I was blessed with encounter.\x01",
            "…… I began to laugh a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12004F#6PIs that so,\x01",
            "That is a good thing.\x02\x03",
            "#12003F….\x02\x03",
            "Saya passed away ……\x01",
            "Have you been five years already?\x02\x03",
            "#12000FI met you for the first time\x01",
            "It was six years ago … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11P#01404FSix years ago … That was right.\x02\x03",
            "At that time, I was surprised\x01",
            "You say that you were awkward\x01",
            "I met a friend Saya by accident in this town ……\x02\x03",
            "Do not be shy,\x01",
            "In the form that Saya's guy pulls forcibly\x01",
            "Were you staying at our house?\x02\x03",
            "#01402FThree years ago with you like that\x01",
            "When we meet again at the guild of Libert\x01",
            "I was surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12004F#6PHehe, it is.\x01",
            "Truly the margin of people is strange\x01",
            "It is thought.\x02\x03",
            "#12003F…… I'm that one bunch of meals\x01",
            "I will not forget your warmth all my life.\x02\x03",
            "#12001FAfter all, returning that benefit directly\x01",
            "I could not do it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11P#01404F… …. No, I think so\x01",
            "Just got it\x01",
            "Saya probably was pleased.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(90790, 1500, 76740, 0)
    MoveCamera(64, 26, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15480, 0)
    OP_4C(0x17, 0xFF)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00005F#11P(… … apparently, for two people\x01",
            "From before get acquainted with the guild\x01",
            "She seems to have some acquaintance. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00108F(Yes, but no more\x01",
            "I want to eavesdrop\x01",
            "It feels bad. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203F(That's fine, do not disturb me\x01",
            "Let's draw it. )\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 91210, 0, 76450, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x1C2, 6)
    EventEnd(0x5)
    Return()

    # Function_27_4125 end

    def Function_28_4898(): pass

    label("Function_28_4898")

    EventBegin(0x0)
    Fade(500)
    OP_68(88320, 1500, 84360, 0)
    MoveCamera(38, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    OP_4B(0x17, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CAE")

    ChrTalk(
        0x17,
        (
            "#11P#01404Fby the way……\x01",
            "Esther and Joshua\x01",
            "I wanted to see you.\x02\x03",
            "I heard that I met Rin at the memorial festival\x01",
            "Although I was very regretted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12004F#6PHehe, is that so?\x01",
            "It did a bad thing, did not he?\x02\x03",
            "If there is time to spare, of course\x01",
            "I wanted to see you too.\x02\x03",
            "#12002FHowever, with two crossbells\x01",
            "Of course he is listening to his success.\x02\x03",
            "I will tell you about that girls\x01",
            "I have been watching it since I was a newcomer … …\x01",
            "It was really misplaced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11P#01402FOh, I, too, to two people\x01",
            "I was saved a lot.\x02\x03",
            "#01404FMr. Casius' s style\x01",
            "Should I say children …?\x01",
            "I am looking forward to the future.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(86330, 1800, 73970, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(14890, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 87080, 0, 73540, 0)
    SetChrPos(0x102, 88890, 0, 73750, 0)
    SetChrPos(0x103, 86550, 0, 71830, 0)
    SetChrPos(0x104, 88500, 0, 72620, 0)
    SetChrPos(0x109, 89790, 0, 72690, 0)
    SetChrPos(0x105, 87790, 0, 71090, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00001F#11P(Mr. Kirika … ….\x01",
            "By the way, accept reception at Libert\x01",
            "I was talking about doing it. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#11P(Naturally,\x01",
            "Both of the eschat\x01",
            "You mean acquaintance? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#11P(Hehe, people are really\x01",
            "Where is it connected?\x01",
            "I do not know. )\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4E56")

    label("loc_4CAE")


    ChrTalk(
        0x17,
        (
            "#11P#01405FBy the way, even now with Jin,\x01",
            "You seem to be keeping in touch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12004F#6PWell, as it is.\x02\x03",
            "#12000FSince there is a mutual position,\x01",
            "I do not have a chance to meet so.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(86330, 1800, 73970, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(14890, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 87080, 0, 73540, 0)
    SetChrPos(0x102, 88890, 0, 73750, 0)
    SetChrPos(0x103, 86550, 0, 71830, 0)
    SetChrPos(0x104, 88500, 0, 72620, 0)
    SetChrPos(0x109, 89790, 0, 72690, 0)
    SetChrPos(0x105, 87790, 0, 71090, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003F#11P(I can not ever ever hear it.\x01",
            "Let's turn back to life. )\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_4E56")

    SetChrPos(0x0, 87080, 0, 73540, 315)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x17, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_28_4898 end

    def Function_29_4E82(): pass

    label("Function_29_4E82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52F4")
    EventBegin(0x0)
    Fade(500)
    OP_68(34230, 0, 320, 0)
    MoveCamera(58, 28, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18390, 0)
    SetChrPos(0x101, 33280, 0, -280, 90)
    SetChrPos(0x102, 33280, 0, -1680, 90)
    SetChrPos(0x103, 32970, 0, 720, 90)
    SetChrPos(0x104, 31670, 0, -670, 90)
    SetChrPos(0x109, 31080, 0, -1750, 99)
    SetChrPos(0x105, 31070, 0, 740, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FAh……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(73750, 1500, 1580, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    Sound(160, 0, 100, 0)
    OP_64(0xC)
    OP_64(0xD)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "…… Hmm, the elevator is\x01",
            "You seem to have arrived?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#6POh, ah …… you go first.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Oh, hey there\x01",
            "Please use it ahead of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Because I am not in a hurry any more.\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0xD, 500)

    ChrTalk(
        0xC,
        (
            "#6PNo, but I came later\x01",
            "I am the one … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(34230, 0, 320, 0)
    MoveCamera(58, 28, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18390, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#6P#00305FWhat's wrong, Lloyd?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00001FOh, the officers of the two major countries\x01",
            "I'm in front of the elevator ….\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)
    TurnDirection(0x103, 0x104, 500)

    ChrTalk(
        0x102,
        (
            "#00106FApparently, each other elevator\x01",
            "She seems to be giving up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10108F…… Something, I do not feel comfortable.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#6P#10302FHuh, what the hell am I supposed to do\x01",
            "I guess that is supposed to be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FTentatively,\x01",
            "Forcibly use the elevator\x01",
            "I do not think it's necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FThat's right.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 33280, 0, -280, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x1C2, 7)
    EventEnd(0x5)
    Return()

    label("loc_52F4")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F…… The officers are still\x01",
            "It seems to be in front of the elevator.\x02\x03",
            "#00003FLet us use the stairs.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 33280, 0, -280, 270)
    EventEnd(0x4)
    Return()

    # Function_29_4E82 end

    def Function_30_536C(): pass

    label("Function_30_536C")

    Sound(160, 0, 100, 0)
    Return()

    # Function_30_536C end

    def Function_31_5373(): pass

    label("Function_31_5373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_539B")
    SetScenarioFlags(0x146, 3)

    label("loc_539B")

    Return()

    # Function_31_5373 end

    def Function_32_539C(): pass

    label("Function_32_539C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    CreatePortrait(0, 230, 192, 742, 256, 0, 20, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis505.itp")
    OP_90(0x101, -51500, 0, 11300, 0)
    OP_90(0x102, -51500, 0, 10200, 0)
    OP_90(0x103, -51500, 0, 9100, 0)
    OP_90(0x104, -51500, 0, 8000, 0)
    OP_90(0x109, -51500, 0, 6900, 0)
    OP_90(0x105, -51500, 0, 5800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -51500, 0, 13500, 0)
    ClearMapObjFlags(0xB, 0x10)
    OP_70(0xB, 0x3C)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x3C)
    OP_68(-54000, 1100, 12700, 0)
    MoveCamera(49, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(2000, 0)
    BeginChrThread(0x1D, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 33)
    OP_0D()
    OP_68(-54000, 1100, -300, 8000)
    OP_6F(0x79)
    Sleep(500)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0xD, 0x10)
    OP_71(0xD, 0x0, 0x5, 0x0, 0x0)
    OP_79(0xD)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1D, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    OP_68(-12600, 1000, 0, 0)
    MoveCamera(47, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x1D, -10500, 0, 0, 90)
    SetChrPos(0x3C, -11600, -600, 0, 90)
    SetChrPos(0x101, -12600, 0, -800, 90)
    SetChrPos(0x102, -12600, 0, 700, 90)
    SetChrPos(0x103, -13800, 0, -400, 90)
    SetChrPos(0x104, -13800, 0, 1100, 90)
    SetChrPos(0x109, -15000, 0, -600, 90)
    SetChrPos(0x105, -15000, 0, 900, 90)
    OP_6B(0x3C)
    SetChrFlags(0x3C, 0x20)
    SetChrFlags(0x3C, 0x40)
    SetChrFlags(0x3C, 0x8)
    SetChrFlags(0x3C, 0x4)

    def lambda_562C():
        OP_97(0xFE, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_562C)

    def lambda_5646():
        OP_98(0xFE, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_5646)

    def lambda_5660():
        OP_97(0x101, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5660)
    Sleep(50)

    def lambda_567D():
        OP_97(0x102, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_567D)
    Sleep(50)

    def lambda_569A():
        OP_97(0x103, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_569A)
    Sleep(50)

    def lambda_56B7():
        OP_97(0x104, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_56B7)
    Sleep(50)

    def lambda_56D4():
        OP_97(0x109, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_56D4)
    Sleep(50)

    def lambda_56F1():
        OP_97(0x105, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_56F1)
    FadeToBright(1000, 0)
    MoveCamera(37, 21, 0, 8000)
    SetCameraDistance(18000, 8000)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    WaitChrThread(0x1D, 1)

    def lambda_575E():
        OP_93(0xFE, 0x110, 0x15E)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_575E)
    WaitChrThread(0x101, 0)

    def lambda_576F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_576F)
    Sleep(100)
    WaitChrThread(0x102, 0)

    def lambda_5783():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5783)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x101,
        "#6P#00001FAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#6PThat is\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_6B(0xFF)
    OP_68(10000, 1000, 3800, 2000)
    MoveCamera(0, 19, 0, 2000)
    SetCameraDistance(20000, 2000)

    def lambda_57F6():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_57F6)
    OP_6F(0x79)

    ChrTalk(
        0x1D,
        (
            "#6P#02804FHoff, done after this\x01",
            "Named ambassadorial\x01",
            "A#2RHala#The stage of the conversation … …\x02\x03",
            "#02800FThe Trade Conference Venue\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrPos(0x1D, -52000, 0, 101500, 0)
    SetChrPos(0x101, -51400, 0, 104200, 0)
    SetChrPos(0x102, -52600, 0, 104200, 0)
    SetChrPos(0x103, -50200, 0, 103400, 0)
    SetChrPos(0x104, -53800, 0, 103400, 0)
    SetChrPos(0x109, -51200, 0, 102600, 0)
    SetChrPos(0x105, -52900, 0, 102200, 0)
    OP_68(-52000, 5500, 118000, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20500, 0)
    OP_68(-52660, 3000, 105850, 6000)
    MoveCamera(23, 7, 0, 6000)
    OP_6E(700, 6000)
    SetCameraDistance(16500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1500)

    def lambda_596A():
        OP_97(0x101, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_596A)
    Sleep(50)

    def lambda_5987():
        OP_97(0x102, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5987)
    Sleep(50)

    def lambda_59A4():
        OP_97(0x103, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_59A4)
    Sleep(50)

    def lambda_59C1():
        OP_97(0x104, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_59C1)
    Sleep(50)

    def lambda_59DE():
        OP_97(0x109, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_59DE)
    Sleep(50)

    def lambda_59FB():
        OP_97(0x105, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_59FB)
    Sleep(500)

    def lambda_5A18():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_5A18)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00011F#11PThis is amazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#11PWhat an awesome view!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#5PThat the ceiling is so expensive\x01",
            "You have to make two floor punches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#02804F#11POh, so the top 36 F\x01",
            "It has a U-shaped configuration.\x02\x03",
            "#02800FBy the way, the rooms on both sides are\x01",
            "Stakeholders of the heads of state summoned\x01",
            "It is a waiting room.\x02\x03",
            "Escort officers and so on\x01",
            "I will be waiting.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5B8B():
        TurnDirection(0x101, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5B8B)
    Sleep(50)

    def lambda_5B9B():
        TurnDirection(0x109, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5B9B)
    Sleep(50)

    def lambda_5BAB():
        TurnDirection(0x102, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5BAB)
    Sleep(50)

    def lambda_5BBB():
        TurnDirection(0x105, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5BBB)
    Sleep(50)

    def lambda_5BCB():
        TurnDirection(0x103, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5BCB)
    Sleep(50)

    def lambda_5BDB():
        TurnDirection(0x104, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5BDB)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x109,
        "#10100F#5PI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PSurely that room\x01",
            "It will be necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#02804F#11PWell, on the last floor\x01",
            "Shall I introduce you?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    OP_68(13400, 900, 0, 0)
    MoveCamera(37, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x1D, 15500, 0, 0, 90)
    SetChrPos(0x3C, 13400, -600, 0, 90)
    SetChrPos(0x101, 13400, 0, -800, 90)
    SetChrPos(0x102, 13400, 0, 700, 90)
    SetChrPos(0x103, 12200, 0, -400, 90)
    SetChrPos(0x104, 12200, 0, 1100, 90)
    SetChrPos(0x109, 11000, 0, -600, 90)
    SetChrPos(0x105, 11000, 0, 900, 90)
    OP_6B(0x3C)
    SetChrFlags(0x3C, 0x20)
    SetChrFlags(0x3C, 0x40)
    SetChrFlags(0x3C, 0x8)
    SetChrFlags(0x3C, 0x4)
    MoveCamera(47, 21, 0, 10000)
    SetCameraDistance(19000, 10000)

    def lambda_5D85():
        OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_5D85)

    def lambda_5D9F():
        OP_98(0xFE, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_5D9F)

    def lambda_5DB9():
        OP_97(0x101, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5DB9)
    Sleep(50)

    def lambda_5DD6():
        OP_97(0x102, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5DD6)
    Sleep(50)

    def lambda_5DF3():
        OP_97(0x103, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5DF3)
    Sleep(50)

    def lambda_5E10():
        OP_97(0x104, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5E10)
    Sleep(50)

    def lambda_5E2D():
        OP_97(0x109, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5E2D)
    Sleep(50)

    def lambda_5E4A():
        OP_97(0x105, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5E4A)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(8000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x1D, 0xFF)
    EndChrThread(0x3C, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    OP_68(71900, 1000, 0, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x1D, 71900, 0, 0, 90)
    SetChrPos(0x3C, 71900, -500, 0, 90)
    SetChrPos(0x101, 70200, 0, -900, 90)
    SetChrPos(0x102, 70200, 0, 600, 90)
    SetChrPos(0x103, 69000, 0, -500, 90)
    SetChrPos(0x104, 69000, 0, 1000, 90)
    SetChrPos(0x109, 67800, 0, -700, 90)
    SetChrPos(0x105, 67800, 0, 800, 90)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    SetCameraDistance(20000, 7000)

    def lambda_5F7D():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_5F7D)
    BeginChrThread(0x3C, 3, 0, 35)
    Sleep(100)
    FadeToBright(1000, 0)

    def lambda_5FA9():
        OP_97(0x101, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5FA9)
    Sleep(50)

    def lambda_5FC6():
        OP_97(0x102, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5FC6)
    Sleep(50)

    def lambda_5FE3():
        OP_97(0x103, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5FE3)
    Sleep(50)

    def lambda_6000():
        OP_97(0x104, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6000)
    Sleep(50)

    def lambda_601D():
        OP_97(0x109, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_601D)
    Sleep(50)

    def lambda_603A():
        OP_97(0x105, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_603A)
    Sleep(100)

    def lambda_6057():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6057)
    Sleep(50)

    def lambda_606B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_606B)
    OP_0D()
    WaitChrThread(0x1D, 0)
    BeginChrThread(0x1D, 3, 0, 34)
    WaitChrThread(0x101, 0)
    BeginChrThread(0x101, 3, 0, 34)
    Sleep(900)
    WaitChrThread(0x102, 0)
    BeginChrThread(0x102, 3, 0, 34)
    Sleep(100)
    WaitChrThread(0x103, 0)
    BeginChrThread(0x103, 3, 0, 34)
    Sleep(900)
    WaitChrThread(0x104, 0)
    BeginChrThread(0x104, 3, 0, 34)
    Sleep(100)
    WaitChrThread(0x109, 0)
    BeginChrThread(0x109, 3, 0, 34)
    Sleep(900)
    WaitChrThread(0x105, 0)
    BeginChrThread(0x105, 3, 0, 34)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_71(0x6, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x6)
    OP_0D()
    EndChrThread(0x1D, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_539C end

    def Function_33_6163(): pass

    label("Function_33_6163")


    def lambda_6168():
        OP_95(0xFE, -51500, 0, 14000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6168)
    WaitChrThread(0xFE, 1)

    def lambda_6186():
        OP_95(0xFE, -55500, 0, 14000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6186)
    WaitChrThread(0xFE, 1)

    def lambda_61A4():
        OP_95(0xFE, -55500, 0, 1500, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61A4)
    WaitChrThread(0xFE, 1)

    def lambda_61C2():
        OP_95(0xFE, -53000, 0, -1000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61C2)
    WaitChrThread(0xFE, 1)

    def lambda_61E0():
        OP_95(0xFE, -48000, 0, -1000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61E0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_33_6163 end

    def Function_34_61FA(): pass

    label("Function_34_61FA")


    def lambda_61FF():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61FF)
    WaitChrThread(0xFE, 1)

    def lambda_621D():
        OP_95(0xFE, 81000, 0, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_621D)
    Sleep(700)

    def lambda_623A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_623A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_34_61FA end

    def Function_35_624B(): pass

    label("Function_35_624B")


    def lambda_6250():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_6250)
    WaitChrThread(0x3C, 1)

    def lambda_626E():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_626E)
    WaitChrThread(0xFE, 1)
    OP_6B(0xFF)
    Return()

    # Function_35_624B end

    def Function_36_628B(): pass

    label("Function_36_628B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10902.itc", 0x1E)
    LoadChrToIndex("chr/ch11102.itc", 0x1F)
    LoadChrToIndex("chr/ch11002.itc", 0x20)
    LoadChrToIndex("chr/ch11802.itc", 0x21)
    LoadChrToIndex("chr/ch11712.itc", 0x22)
    LoadChrToIndex("chr/ch05602.itc", 0x23)
    LoadChrToIndex("chr/ch05802.itc", 0x24)
    LoadChrToIndex("chr/ch05902.itc", 0x25)
    LoadChrToIndex("apl/ch51233.itc", 0x26)
    LoadChrToIndex("chr/ch05900.itc", 0x27)
    LoadChrToIndex("chr/ch05600.itc", 0x28)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02200.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01400.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02500.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02800.itp")
    CreatePortrait(4, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07200.itp")
    CreatePortrait(5, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07000.itp")
    CreatePortrait(6, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07500.itp")
    CreatePortrait(7, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07400.itp")
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -46450, 50, 120000, 270)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -46450, 50, 117100, 270)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -46450, 50, 114200, 270)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -57600, 50, 117100, 90)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -57600, 50, 120000, 90)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -53850, 50, 123900, 180)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -50100, 50, 123900, 180)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -40100, 50, 121250, 270)
    OP_4B(0x17, 0xFF)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -46900, 0, 126600, 180)
    SetMapObjFrame(0xFF, "paper", 0x1, 0x1)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1KSame day, 13: 00 ─\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x23,
        (
            "#02503F─ ─ So from this\x01",
            "\"Western Zemria Trade Council\"\x01",
            "We will start the plenary session.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7583", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x247), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-52000, 7500, 116000, 0)
    MoveCamera(45, 29, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(23000, 0)
    OP_68(-52000, 2500, 116000, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-46800, 1000, 119400, 0)
    MoveCamera(27, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_68(-46800, 1000, 114800, 4000)
    MoveCamera(43, 21, 0, 4000)
    SetCameraDistance(14500, 4000)
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(-57600, 900, 118600, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13000, 0)
    MoveCamera(333, 29, 0, 4000)
    SetCameraDistance(15000, 4000)
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(-52000, 900, 123900, 0)
    MoveCamera(0, 7, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(25000, 0)
    SetCameraDistance(14000, 3000)
    OP_6F(0x79)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x23,
        (
            "The proceeding progress is 僭 越#4RSensuousness#While\x01",
            "I, Henry MacDael\x01",
            "I will do it.\x02\x03",
            "Once the meeting is over,\x01",
            "We are planning about 5 hours.\x02\x03",
            "However, depending on progress\x01",
            "Because there is some extension\x01",
            "Thank you for your understanding.\x02\x03",
            "With it, ─ on the meeting\x01",
            "To two observers\x01",
            "I am asked to participate.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetChrSubChip(0x23, 0x1)
    SetChrSubChip(0x1D, 0x1)
    OP_68(-41100, 900, 121250, 2500)
    MoveCamera(90, 15, 0, 2500)
    SetCameraDistance(15000, 2500)
    OP_6F(0x79)
    SetChrSubChip(0x1E, 0x2)
    SetChrSubChip(0x1F, 0x2)
    SetChrSubChip(0x20, 0x2)
    Sleep(300)

    ChrTalk(
        0x23,
        (
            "#02503F#6P#NAttorney Ian Grimwood\x02\x03",
            "Not only in crossbell but in neighboring countries\x01",
            "It is a legal expert who is active.\x02\x03",
            "#02500FBecause I am also familiar with international law and customary law\x01",
            "I asked for participation in this plenary session.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x24, 0x27)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x24, -40100, 0, 120250, 270)
    OP_0D()
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x24,
        (
            "Nice to meet you……\x01",
            "It is Ian Grimwood.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x1F,
        (
            "#07200F#12P#NYou,\x01",
            "The famous \"bear beard teacher\"?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x21,
        (
            "Hmm, as well as human rights issues\x01",
            "Are you actively involved?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(100)

    ChrTalk(
        0x20,
        "#07002F#12P#NEhe, nice to meet you\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x24,
        (
            "#5P#02210FHaha … … sincerity sincerity,\x01",
            "I will serve you.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-46900, 900, 126600, 2500)
    MoveCamera(0, 15, 0, 2500)
    SetCameraDistance(15500, 2500)
    OP_6F(0x79)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x24, -40100, 50, 121250, 270)
    Sleep(300)

    ChrTalk(
        0x23,
        (
            "#6P#02503FBracer Arios MacClaine\x02\x03",
            "A great deal of achievement in neighboring countries\x01",
            "It is known for being raised.\x02\x03",
            "#02500FFrom a neutral standpoint of the Association of Association\x01",
            "In order to ensure the safety of the plenary session,\x01",
            "I asked for participation.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x17, 0x10)
    SetChrFlags(0x17, 0x2)
    SetChrSubChip(0x17, 0x8)
    Sleep(130)
    SetChrSubChip(0x17, 0x9)
    Sleep(130)
    SetChrSubChip(0x17, 0xA)
    Sleep(800)
    SetChrSubChip(0x17, 0x9)
    Sleep(130)
    SetChrSubChip(0x17, 0x8)
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Flippers Arios")

    AnonymousTalk(
        0xFF,
        (
            "It is Arios · McLaein.\x01",
            "An Opinion.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x22,
        (
            "#07509F#6P#NHah, the Divine Blade of Wind right?\x02\x03",
            "#07500FEven in the Republic\x01",
            "I have heard your name.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1E,
        (
            "#07404F#11P#12P#NWe hear of you in the Empire as well\x02\x03",
            "#07400FOn the crossbell land\x01",
            "Letting the wind \"Sword Saint\" With you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x17, 0x8)
    Sleep(130)
    SetChrSubChip(0x17, 0xC)
    Sleep(130)
    SetChrSubChip(0x17, 0xD)

    NpcTalk(
        0x17,
        "Flippers Arios",
        "#01404FI'm honored\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-52000, 1000, 120500, 0)
    MoveCamera(90, 11, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    ClearChrFlags(0x17, 0x10)
    ClearChrFlags(0x17, 0x2)
    SetChrSubChip(0x17, 0x0)
    SetChrSubChip(0x23, 0x0)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x23,
        (
            "#02503F#5PThen it will be quickly,\x01",
            "Let's review each bill.\x02\x03",
            "#02500FProponent, Mayor Dieter Crois.\x01",
            "Please explain and supplement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#6P#02804FRight\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    SetChrPos(0x1D, -54850, 50, 123900, 180)
    OP_0D()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x1D,
        (
            "First of all, the materials you have\x01",
            "At first there is a bill - ─\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetCameraDistance(22500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_36_628B end

    def Function_37_707C(): pass

    label("Function_37_707C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(73000, 1200, -1000, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 74500, 0, -1000, 270)
    SetChrPos(0x102, 73800, 0, 200, 225)
    SetChrPos(0x103, 73800, 0, -2200, 315)
    SetChrPos(0x104, 72200, 0, 200, 135)
    SetChrPos(0x109, 71500, 0, -1000, 90)
    SetChrPos(0x105, 72200, 0, -2200, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#00000FAlright ……\x01",
            "Was this one round?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FFor now\x01",
            "There seems to be no problem in particular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00302FOh, with this condition again,\x01",
            "Let's look around and see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FI see …\x02\x03",
            "#00108F…… For the conference\x01",
            "I wonder what's going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FThat's right, the mayor and the chairman\x01",
            "I think I am trying hard but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FThe problem is \"Chairman of Iron Blood\"\x01",
            "Is it Rock Smith President?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, at break time\x01",
            "Why do not you ask someone?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 39)
    Return()

    # Function_37_707C end

    def Function_38_730B(): pass

    label("Function_38_730B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-55500, 1200, -1500, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -54000, 0, -1500, 270)
    SetChrPos(0x102, -54700, 0, -300, 225)
    SetChrPos(0x103, -54700, 0, -2700, 315)
    SetChrPos(0x104, -56300, 0, -300, 135)
    SetChrPos(0x109, -57000, 0, -1500, 90)
    SetChrPos(0x105, -56300, 0, -2700, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#00000FAlright ……\x01",
            "Was this one round?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FFor now\x01",
            "There seems to be no problem in particular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00302FOh, with this condition again,\x01",
            "Let's look around and see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FI see …\x02\x03",
            "#00108F…… For the conference\x01",
            "I wonder what's going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FThat's right, the mayor and the chairman\x01",
            "I think I am trying hard but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FThe problem is \"Chairman of Iron Blood\"\x01",
            "Is it Rock Smith President?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, at break time\x01",
            "Why do not you ask someone?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 39)
    Return()

    # Function_38_730B end

    def Function_39_759A(): pass

    label("Function_39_759A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10900.itc", 0x1E)
    LoadChrToIndex("chr/ch11100.itc", 0x1F)
    LoadChrToIndex("chr/ch11000.itc", 0x20)
    LoadChrToIndex("chr/ch11800.itc", 0x21)
    LoadChrToIndex("chr/ch11700.itc", 0x22)
    LoadChrToIndex("chr/ch05600.itc", 0x23)
    LoadChrToIndex("chr/ch05800.itc", 0x24)
    LoadChrToIndex("chr/ch00900.itc", 0x25)
    LoadChrToIndex("chr/ch06000.itc", 0x26)
    LoadChrToIndex("chr/ch47900.itc", 0x27)
    LoadChrToIndex("apl/ch50314.itc", 0x28)
    LoadChrToIndex("chr/ch27400.itc", 0x29)
    LoadChrToIndex("chr/ch27800.itc", 0x2A)
    LoadChrToIndex("chr/ch27900.itc", 0x2B)
    LoadChrToIndex("chr/ch47500.itc", 0x2C)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SoundLoad(851)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -50800, 0, 125000, 180)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -49600, 0, 125000, 180)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -51900, 0, 125200, 180)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -54200, 0, 125000, 180)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -53100, 0, 125200, 180)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -48500, 0, 125200, 180)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -55300, 0, 125200, 180)
    SetChrChipByIndex(0x25, 0x25)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, -44300, 0, 122800, 225)
    SetChrChipByIndex(0x36, 0x0)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, -50040, 0, 120090, 180)
    SetChrChipByIndex(0x37, 0x0)
    SetChrSubChip(0x37, 0x0)
    ClearChrFlags(0x37, 0x80)
    SetChrFlags(0x37, 0x8000)
    SetChrPos(0x37, -54210, 0, 120370, 180)
    SetChrChipByIndex(0x3D, 0x26)
    SetChrSubChip(0x3D, 0x0)
    ClearChrFlags(0x3D, 0x80)
    SetChrFlags(0x3D, 0x8000)
    SetChrPos(0x3D, -52870, 0, 116730, 358)
    SetChrChipByIndex(0x3E, 0x28)
    SetChrSubChip(0x3E, 0x0)
    ClearChrFlags(0x3E, 0x80)
    SetChrFlags(0x3E, 0x8000)
    SetChrPos(0x3E, -53430, 0, 117400, 0)
    SetChrChipByIndex(0x3F, 0x27)
    SetChrSubChip(0x3F, 0x0)
    ClearChrFlags(0x3F, 0x80)
    SetChrFlags(0x3F, 0x8000)
    SetChrPos(0x3F, -51370, 0, 117370, 0)
    SetChrChipByIndex(0x40, 0x29)
    SetChrSubChip(0x40, 0x0)
    ClearChrFlags(0x40, 0x80)
    SetChrFlags(0x40, 0x8000)
    SetChrPos(0x40, -53630, 0, 115630, 0)
    SetChrChipByIndex(0x41, 0x2A)
    SetChrSubChip(0x41, 0x0)
    ClearChrFlags(0x41, 0x80)
    SetChrFlags(0x41, 0x8000)
    SetChrPos(0x41, -51990, 0, 116190, 0)
    SetChrChipByIndex(0x42, 0x2B)
    SetChrSubChip(0x42, 0x0)
    ClearChrFlags(0x42, 0x80)
    SetChrFlags(0x42, 0x8000)
    SetChrPos(0x42, -50340, 0, 116750, 0)
    SetChrChipByIndex(0x43, 0x2C)
    SetChrSubChip(0x43, 0x0)
    ClearChrFlags(0x43, 0x80)
    SetChrFlags(0x43, 0x8000)
    SetChrPos(0x43, -51300, 0, 115500, 348)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    ClearMapObjFlags(0xE, 0x4)
    OP_68(-52000, 1100, 120300, 0)
    MoveCamera(33, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1KSame day, 15:05\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Eventually the first half of the meeting ended,\x01",
            "Before entering the break time, by the press\x01",
            "A joint interview with the leaders of each country was held.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(40, 19, 0, 9000)
    SetCameraDistance(21500, 9000)
    BeginChrThread(0x3E, 0, 0, 40)
    PlayBGM("ed7111", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    Sleep(1000)
    Sound(851, 2, 100, 0)
    OP_0D()
    Sleep(5000)
    StopSound(851, 2000, 100)
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    EndChrThread(0x3E, 0x0)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x142, 1)
    OP_24(0x353)
    SetScenarioFlags(0x22, 2)
    NewScene("c1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_39_759A end

    def Function_40_79C9(): pass

    label("Function_40_79C9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7A81")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_79F7")
    Sleep(500)
    Jump("loc_7A3F")

    label("loc_79F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7A0E")
    Sleep(1000)
    Jump("loc_7A3F")

    label("loc_7A0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7A25")
    Sleep(1500)
    Jump("loc_7A3F")

    label("loc_7A25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7A3C")
    Sleep(2000)
    Jump("loc_7A3F")

    label("loc_7A3C")

    Sleep(2500)

    label("loc_7A3F")

    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 80, 0)
    Jump("Function_40_79C9")

    label("loc_7A81")

    Return()

    # Function_40_79C9 end

    def Function_41_7A82(): pass

    label("Function_41_7A82")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10902.itc", 0x1E)
    LoadChrToIndex("chr/ch11102.itc", 0x1F)
    LoadChrToIndex("chr/ch11002.itc", 0x20)
    LoadChrToIndex("chr/ch11802.itc", 0x21)
    LoadChrToIndex("chr/ch11712.itc", 0x22)
    LoadChrToIndex("chr/ch05602.itc", 0x23)
    LoadChrToIndex("chr/ch05802.itc", 0x24)
    LoadChrToIndex("chr/ch05902.itc", 0x25)
    LoadChrToIndex("apl/ch51233.itc", 0x26)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -46450, 50, 120000, 270)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -46450, 50, 117100, 270)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x2)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -46450, 50, 114200, 270)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -57600, 50, 117100, 90)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -57600, 50, 120000, 90)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -53850, 50, 123900, 180)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -50100, 50, 123900, 180)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -40100, 50, 121250, 270)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -46900, 0, 126600, 215)
    OP_4B(0x17, 0xFF)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetMapObjFrame(0xFF, "paper", 0x1, 0x1)
    SetMapObjFlags(0xE, 0x4)
    OP_68(-52580, 3500, 121120, 0)
    MoveCamera(104, 9, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18820, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1KSame day 16:30\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And the second half of the trade meeting\x01",
            "As Ian lawyers concern,\x01",
            "It began with the development of turbulence.\x02\x03",
            "From both the Empire and the Republic\x01",
            "On the security of the crossbell\x01",
            "Severe problems raised one after another … …\x02\x03",
            "Mayor of Dieter and McDaely\x01",
            "The facial expression gradually strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7583", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x247), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-52580, 1500, 121120, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_68(-53220, 1500, 119580, 100000)
    MoveCamera(81, 11, 0, 100000)

    ChrTalk(
        0x1E,
        (
            "#5P#07403F── The problem is that there is only one religious group\x01",
            "Oh too, the security was shaken indefinitely.\x02\x03",
            "#07401FIt also controls security organization, such as,\x01",
            "By unprecedented form.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1D,
        "#6P#02803F…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x23,
        (
            "#02500F#6P…… For details as well to everyone\x01",
            "I think that I have told you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1E,
        (
            "#5P#07403FDetails are not a problem.\x01",
            "The \"quality\" of crisis management is a problem.\x02\x03",
            "#07401FDuring the incident, the empire who stayed\x01",
            "There are facts that life and property were threatened.\x02\x03",
            "What do you think about that?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1F, 0x2)
    Sleep(300)

    ChrTalk(
        0x1F,
        (
            "#11P#07203FWait a moment, Chancellor\x02\x03",
            "#07201FRegarding damage compensation and compensation fee\x01",
            "Procedures should already be in place.\x02\x03",
            "To put further Mira on top is\x01",
            "The amount of my empire will be questioned.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x1)
    Sleep(300)

    ChrTalk(
        0x1E,
        (
            "#5P#07400FNo, Your Highness.\x01",
            "It is not such a problem.\x02\x03",
            "The problem is they ……\x01",
            "Crossbell Autonomous State Government How\x01",
            "It can guarantee various \"safety\".\x02\x03",
            "#07403FLife safety, property safety,\x01",
            "Safety of trust in trade and financial markets!\x02\x03",
            "#07401FBringing to political fighting, to suspicious girls\x01",
            "To those who are attached\x01",
            "Can you guarantee it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1F,
        "#11P#07208FUgh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#4P#NHowever, former Hartmann chairman has failed,\x01",
            "I hear that corruption is also being purged …\x02\x03",
            "In the future under a sound political system\x01",
            "A solid security framework\x01",
            "Is not it okay to build it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x22, 0x2)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "#6P#07500F#NNo, no douympress.\x01",
            "The thing is not so easy, right?\x02\x03",
            "Crossbell's political climate\x01",
            "Originally, it tends to rot.\x02\x03",
            "Mayor Dieter and McDaely\x01",
            "Although it is outstanding as a politician … …\x02\x03",
            "If something happens to them,\x01",
            "Is not it going to turn back?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0x21, 0x1)
    Sleep(300)

    ChrTalk(
        0x21,
        "#4P#NHmm\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x20,
        (
            "#11P#07003F… … Although it is a pessimistic story\x01",
            "Originally corruption is a politico.\x02\x03",
            "#07008FIt's not just crossbells,\x01",
            "Same as anywhere, including Japan …\x02\x03",
            "#07001FNow, now, during the term of office\x01",
            "Can we make a sound political regime\x01",
            "Should not I watch over you?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1E,
        (
            "#5P#07404F… … Excuse my Highness is young.\x01",
            "I also want to believe in hope.\x02\x03",
            "#07403FBut the crossbell is traditional\x01",
            "Give the royal family#2RPlease#It is different from Libert.\x02\x03",
            "Compliance#2RYo#In places without authority to become\x01",
            "Politics will easily weaken too easily … …\x02\x03",
            "#07401FThat has been proved in history\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x20,
        "#11P#07005FT-that is\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x22, 0x0)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "#6P#07503F#NHmm, there are no monarchs in our country,\x01",
            "There is an honorable republic charter.\x02\x03",
            "#07500FThis is the time of the revolution a hundred years ago,\x01",
            "Various powers and ethnic groups gathered\x01",
            "It was a miraculous thing that I made.\x02\x03",
            "Depending on that, the politics of our country\x01",
            "Even if it rots without losing pride\x01",
            "It can be said that it survived.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x23, 0x2)
    Sleep(300)
    SetChrSubChip(0x1E, 0x0)

    ChrTalk(
        0x23,
        (
            "#02503F#5P…. Words, but also to us\x01",
            "Proud autonomous state law exists.\x02\x03",
            "From historical circumstances, various deficiencies\x01",
            "It is certain that it is occurring … …\x02\x03",
            "#02500FStill little by little\x01",
            "It is certain that it can be improved.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1E, 0x2)
    Sleep(300)

    ChrTalk(
        0x1E,
        (
            "#11P#07400F……lawyer.\x01",
            "The Autonomous State Law which was done in the last ten years\x01",
            "What is the added / revised item?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x24,
        (
            "#5P#N#02205FThat's right.\x01",
            "Although there is no detailed document.\x02\x03",
            "#02203FProbably around 50 times\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x22,
        (
            "#6P#07505F#NOnly 50 in 10 years!\x01",
            "That is somewhat surprising!\x02\x03",
            "That's only 5 times per year!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1D, 0x2)
    Sleep(300)

    ChrTalk(
        0x1D,
        (
            "#5P#02803FNo, in recent years\x01",
            "There is a trend of increase.\x02\x03",
            "#02801FLast year certainly 12 items\x01",
            "Was it supposed to be added / revised?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x23,
        (
            "#02505F#5POh, with regard to finance and conductivity net\x01",
            "Many items are added, but …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1E,
        (
            "#11P#07403FIn any case, in that condition\x01",
            "A very meaningful security system\x01",
            "I can not think that it can be constructed quickly.\x02\x03",
            "#07401FAgainst the countermeasures based on the current situation\x01",
            "We should discuss it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x22,
        "#6P#07504F#NYes, I agree with that\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1E, 0x0)

    ChrTalk(
        0x1F,
        (
            "#11P#07206F…… Okay, you are\x01",
            "I did not expect to get along well so far.\x02\x03",
            "#07201FRegarding the problem of territory of the Nord Plateau\x01",
            "Can not we agree immediately?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x22,
        "#6P#07509F#NHaha yes I suppose that's true\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1E,
        (
            "#5P#07404FWell, about that\x01",
            "Let's discuss another occasion.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x20,
        "#11P#07008F….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x21,
        (
            "#4P#NHmm, time is regrettable.\x01",
            "I should shift the argument.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x23,
        (
            "#02503F#5P……I understand.\x01",
            "As the prosperity of His Excellency ──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(19320, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_41_7A82 end

    def Function_42_8C3E(): pass

    label("Function_42_8C3E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10902.itc", 0x1E)
    LoadChrToIndex("chr/ch11102.itc", 0x1F)
    LoadChrToIndex("chr/ch11002.itc", 0x20)
    LoadChrToIndex("chr/ch11802.itc", 0x21)
    LoadChrToIndex("chr/ch11712.itc", 0x22)
    LoadChrToIndex("chr/ch05602.itc", 0x23)
    LoadChrToIndex("chr/ch05800.itc", 0x24)
    LoadChrToIndex("chr/ch05902.itc", 0x25)
    LoadChrToIndex("apl/ch51233.itc", 0x26)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x2)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -46450, 50, 120000, 270)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x2)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -46450, 50, 117100, 270)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x2)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -46450, 50, 114200, 270)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -57600, 50, 117100, 90)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -57600, 50, 120000, 90)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x1)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -53850, 50, 123900, 180)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -49100, 50, 123900, 135)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -40100, 50, 121250, 270)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -46900, 0, 126600, 180)
    OP_4B(0x17, 0xFF)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetMapObjFrame(0xFF, "paper", 0x1, 0x1)
    SetMapObjFlags(0xE, 0x4)
    OP_68(-46970, 2000, 122960, 0)
    MoveCamera(53, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21890, 0)
    VolumeBGM(0x64, 0x3E8)
    OP_68(-46970, 1000, 122960, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x23,
        (
            "#02501F#5PHis Excellency ……\x01",
            "What were you saying now?\x02\x03",
            "I am sorry, but once again,\x01",
            "I would like to repeat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#07404F#11PHaha, as many times as you like.\x02\x03",
            "#07401FThe dismantling of Crossbell's Guard Force\x02\x03",
            "Furthermore, the security maintenance force of other countries\x01",
            "To make it resident in the crossbell …\x02\x03",
            "That is the the most realistic option.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#02501F#5PUgh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#6P#02801F#N…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x20,
        (
            "#5P#07007F#11P#NW-wait a minute!\x02\x03",
            "His Excellency has appointed the provisions of the Treaty of the\x01",
            "Did not you forget …?! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1E, 0x1)
    Sleep(300)

    ChrTalk(
        0x1E,
        (
            "#5P#07405FOh, cross-bell problem with military force\x01",
            "Are you trying not to solve it?\x02\x03",
            "#07404FBut to invade another\x01",
            "It does not mean that.\x02\x03",
            "#07402F── I fell into civilians\x01",
            "Military army ineffective organization etc.\x01",
            "It is said that it should be disassembled.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x20,
        "#5P#11P#N#07005F!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1E, 0x0)
    Sleep(300)

    ChrTalk(
        0x1E,
        (
            "#11P#07404FActually, Crossbell Guard etc.\x01",
            "Before the Imperial Army, or the Republican Army\x01",
            "It does not exist.\x02\x03",
            "Even with a high performance armored car\x01",
            "After all, in the presence of a tank it is as good as a piece of paper.\x02\x03",
            "#07400FIf you use high maintenance costs for such things\x01",
            "Leave security to other countries' forces ─\x02\x03",
            "#07402FAs it is \"autonomous state\"\x01",
            "It will be the most efficient way.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x21,
        (
            "#11PSomehow\x01",
            "Although it seems to be a rough opinion.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1F,
        (
            "#11P#07203FThat \"the strength of another country\" is\x01",
            "Where do you point it?\x02\x03",
            "#07200FNo doubt someone who would be Prince Minister\x01",
            "Confirm historical circumstances#4RTo go#Also give\x01",
            "You will not say the Imperial Army etc?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1E,
        (
            "#11P#07404FHaha, of course not\x02\x03",
            "#07402F── But, if necessary\x01",
            "Even with sinking in the past\x01",
            "We should provide the power of the Imperial Army.\x02\x03",
            "It is in the western part of the continent of Zemuria\x01",
            "If it leads to peace and development.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#02501F#5PUgh…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-52480, 1200, 120270, 0)
    MoveCamera(87, 9, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21890, 0)
    SetChrPos(0x17, -46900, 0, 126600, 225)
    OP_0D()

    ChrTalk(
        0x22,
        (
            "#6P#07506F…… Fairly good.\x01",
            "Everyone, do not get so hot.\x02\x03",
            "#07501FHis Excellency's suggestion\x01",
            "I feel a bit too forcible.\x02\x03",
            "#07504F─ ─ Well, just a guard and so on\x01",
            "A security organization that can not be used as an army\x01",
            "I understand that it is incomplete.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x0)
    Sleep(200)

    def lambda_9525():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_9525)
    SetChrSubChip(0x21, 0x1)
    Sleep(50)
    SetChrSubChip(0x1F, 0x0)
    Sleep(50)
    SetChrSubChip(0x1D, 0x2)
    Sleep(50)

    ChrTalk(
        0x1E,
        "#5P#07405FHmm, well then\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#6P#07502FSo there is a suggestion,\x01",
            "The guard sharply scales down … …\x02\x03",
            "Instead of the Imperial Army, the Belgard gate,\x01",
            "The Republican Army in the Tangram main gate\x01",
            "How about managing it?\x02\x03",
            "If you do so, Crossbell City's emergency\x01",
            "Let's get up soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#5P#02801FAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#11PPresident, that is\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#5P#07404FHa, coordination of forces\x02\x03",
            "#07400FAs expected, President His Excellency.\x01",
            "Handle thrust up of many opposition parties#2RMackerel#While going\x01",
            "There is only a government administration being managed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#6P#07509FNo, hold down the stubborn aristocratic power\x01",
            "Compared to the ex-honorable minister who is undergoing reform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#11P#07008FY-you both are!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#11P#07203F… … Have a nice idea.\x01",
            "This is not a meeting of only two countries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#5P#07405FOho, that was rude of me\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x2)
    Sleep(300)

    ChrTalk(
        0x1E,
        (
            "#11P#07404FAnyway, like that#4RSeemingly#In a direction\x01",
            "The discussion has flowed … …\x02\x03",
            "#07402FHow about your opinions\x02",
        )
    )

    CloseMessageWindow()

    def lambda_987A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_987A)
    Sleep(100)
    SetChrSubChip(0x1D, 0x0)
    Sleep(250)

    ChrTalk(
        0x23,
        "#02501F#6P…ugh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#6P#02803F….\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22390, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 3)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_8C3E end

    def Function_43_9903(): pass

    label("Function_43_9903")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10902.itc", 0x1E)
    LoadChrToIndex("chr/ch11102.itc", 0x1F)
    LoadChrToIndex("chr/ch11002.itc", 0x20)
    LoadChrToIndex("chr/ch11802.itc", 0x21)
    LoadChrToIndex("chr/ch11712.itc", 0x22)
    LoadChrToIndex("chr/ch05600.itc", 0x23)
    LoadChrToIndex("chr/ch05802.itc", 0x24)
    LoadChrToIndex("chr/ch05902.itc", 0x25)
    LoadChrToIndex("apl/ch51233.itc", 0x26)
    LoadChrToIndex("chr/ch00900.itc", 0x27)
    LoadChrToIndex("chr/ch10900.itc", 0x28)
    LoadChrToIndex("chr/ch11100.itc", 0x29)
    LoadChrToIndex("chr/ch11000.itc", 0x2A)
    LoadChrToIndex("chr/ch11800.itc", 0x2B)
    LoadChrToIndex("chr/ch11710.itc", 0x2C)
    LoadChrToIndex("chr/ch05800.itc", 0x2D)
    LoadChrToIndex("chr/ch05900.itc", 0x2E)
    LoadChrToIndex("chr/ch02400.itc", 0x2F)
    LoadEffect(0x1, "battle/sc008100.eff")
    LoadEffect(0x2, "event/ev12001.eff")
    SoundLoad(497)
    SoundLoad(865)
    SoundLoad(861)
    SoundLoad(825)
    SoundLoad(866)
    SoundLoad(4051)
    SoundLoad(3457)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -46450, 50, 120000, 270)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x2)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -46450, 50, 117100, 270)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x2)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -46450, 50, 114200, 270)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x1)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -57600, 50, 117100, 90)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x1)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -57600, 50, 120000, 90)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -54850, 50, 123900, 180)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x2)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -50100, 50, 123900, 180)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -40100, 50, 121250, 270)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -46900, 0, 126600, 180)
    OP_4B(0x17, 0xFF)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetMapObjFrame(0xFF, "paper", 0x1, 0x1)
    SetMapObjFlags(0xE, 0x4)
    SetChrChipByIndex(0x25, 0x27)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, -52000, 0, 99000, 0)
    OP_A7(0x25, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x44, 0x80)
    OP_78(0x12, 0x44)
    OP_49()
    SetChrPos(0x44, -42000, -18000, 144000, 190)
    OP_D5(0x44, 0x0, 0x2E630, 0x0, 0x0)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    OP_74(0x12, 0x1E)
    OP_70(0x12, 0x3D)
    OP_71(0x12, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x45, 0x80)
    OP_78(0x13, 0x45)
    OP_49()
    SetChrPos(0x45, -62000, -20000, 144000, 170)
    OP_D5(0x45, 0x0, 0x29810, 0x0, 0x0)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_74(0x13, 0x1E)
    OP_70(0x13, 0x3D)
    OP_71(0x13, 0x3D, 0x78, 0x0, 0x20)
    OP_68(-54240, 3000, 116060, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18860, 0)
    VolumeBGM(0x64, 0x3E8)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-54240, 2000, 116060, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(150)

    ChrTalk(
        0x1D,
        (
            "#5P#02803FIt is spoken in this place now\x01",
            "About the discussion of security ……\x02\x03",
            "#02800FOne from me\x01",
            "There is something I want you to suggest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#11P#07405FOh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#6P#07509FHa ha ha, from before\x01",
            "I thought it was quite adequate … …\x02\x03",
            "#07502FSo what are you planning to say\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#5P#02800FYes, that is\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrFlags(0x17, 0x20)
    OP_93(0x17, 0xE1, 0x320)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x17,
        "Flippers Arios",
        "#01407F#4051V#6P#4S#15A── people#4RObscure#Let's go down!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)

    def lambda_9DF2():
        OP_93(0xFE, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_9DF2)
    OP_68(-52000, 1000, 128500, 2000)
    Sleep(1000)
    Fade(500)
    OP_68(-52000, 0, 135000, 0)
    MoveCamera(0, 40, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(25000, 0)
    OP_68(-52000, 4000, 130000, 4000)
    MoveCamera(0, 13, 0, 4000)
    SetCameraDistance(30000, 4000)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    BeginChrThread(0x4C, 1, 0, 57)
    BeginChrThread(0x44, 3, 0, 44)
    BeginChrThread(0x45, 3, 0, 45)
    SetChrSubChip(0x1E, 0x2)

    def lambda_9E8D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_9E8D)
    WaitChrThread(0x44, 3)
    WaitChrThread(0x45, 3)
    OP_6F(0x79)
    OP_63(0x23, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1E, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x21, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x22, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x24, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7544", 0)
    ReplaceBGM("ed7151", "ed7544")
    ReplaceBGM("ed7550", "ed7544")
    ReplaceBGM("ed7300", "ed7561")

    ChrTalk(
        0x23,
        "#02507F#12P#NAh!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x20,
        "#07005F#12P#NWarships!?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sound(865, 2, 100, 0)
    Sound(861, 2, 100, 0)
    OP_87(0x1, 0x0, 0x13, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    OP_87(0x1, 0x1, 0x12, "Null_gun_l", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    OP_87(0x1, 0x2, 0x12, "Null_gun_r", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    PlayEffect(0x2, 0x3, 0xFF, 0x0, -44000, 3500, 129699, 0, 180, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x4, 0xFF, 0x0, -60000, 3500, 129699, 0, 180, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    OP_71(0x14, 0x0, 0x1D, 0x0, 0x0)
    OP_71(0x15, 0x0, 0x1D, 0x0, 0x0)
    SetCameraDistance(27000, 2000)
    OP_82(0x12C, 0x12C, 0xBB8, 0x1F40)
    Sleep(2000)
    Fade(500)
    SetChrPos(0x44, -40000, 1000, 144000, 0)
    SetChrPos(0x45, -60000, 1000, 144000, 0)
    SetChrChipByIndex(0x23, 0x2D)
    SetChrSubChip(0x23, 0x0)
    SetChrPos(0x23, -49100, 50, 123900, 0)
    OP_68(-44000, 5000, 130000, 0)
    MoveCamera(43, 5, -10, 0)
    OP_6E(700, 0)
    SetCameraDistance(21500, 0)
    OP_68(-56000, 5000, 130000, 6000)
    MoveCamera(33, 5, 10, 6000)
    SetCameraDistance(24500, 6000)
    OP_0D()
    OP_71(0x14, 0x1E, 0x31, 0x0, 0x0)
    OP_71(0x15, 0x1E, 0x31, 0x0, 0x0)
    OP_6F(0x79)
    StopSound(865, 300, 100)
    StopSound(861, 300, 100)
    Sound(866, 0, 100, 0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    StopEffect(0x4, 0x2)

    ChrTalk(
        0x21,
        "Ah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#07207FNo way ….\x01",
            "A terrorist! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#07401F….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "#07505F#5PDid you come here …?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#02807F#11PRelax!\x01",
            "Can withstand artillery\x01",
            "It is custom-made tempered glass!\x02\x03",
            "But just to be sure\x01",
            "Everyone, Please go down!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x17, 0x2F)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x20)
    BeginChrThread(0x1D, 3, 0, 46)
    BeginChrThread(0x17, 3, 0, 47)
    BeginChrThread(0x23, 3, 0, 48)
    Sound(865, 2, 100, 0)
    Sound(861, 2, 100, 0)
    OP_87(0x1, 0x0, 0x13, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    OP_87(0x1, 0x1, 0x12, "Null_gun_l", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    OP_87(0x1, 0x2, 0x12, "Null_gun_r", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    PlayEffect(0x2, 0x3, 0xFF, 0x0, -44000, 3500, 129699, 0, 180, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x4, 0xFF, 0x0, -60000, 3500, 129699, 0, 180, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_71(0x14, 0x32, 0x46, 0x0, 0x0)
    OP_71(0x15, 0x32, 0x46, 0x0, 0x0)
    OP_82(0x12C, 0x12C, 0xBB8, 0xBB8)
    Sleep(3000)
    StopSound(865, 300, 100)
    StopSound(861, 300, 100)
    Sound(866, 0, 100, 0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    StopEffect(0x4, 0x2)
    BeginChrThread(0x44, 3, 0, 49)
    BeginChrThread(0x45, 3, 0, 50)
    Sleep(400)
    StopSound(497, 4000, 60)
    StopSound(825, 4000, 50)
    WaitChrThread(0x44, 3)
    WaitChrThread(0x45, 3)
    Fade(500)
    OP_68(-38000, 1100, 110200, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    EndChrThread(0x1D, 0xFF)
    EndChrThread(0x17, 0xFF)
    EndChrThread(0x23, 0xFF)
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x40)
    SetChrPos(0xA, -36500, 0, 110200, 270)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x9, -36500, 0, 110200, 270)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x40)
    SetChrPos(0xD, -36500, 0, 110200, 270)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, -36500, 0, 110200, 270)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x40)
    SetChrPos(0xC, -67400, 0, 110200, 90)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x3)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x40)
    SetChrPos(0xB, -67400, 0, 110200, 90)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1E, 0x28)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x1E, -50700, 0, 106700, 0)
    SetChrChipByIndex(0x1F, 0x29)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -49500, 0, 106000, 0)
    SetChrChipByIndex(0x20, 0x2A)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -50000, 0, 104300, 0)
    SetChrChipByIndex(0x21, 0x2B)
    SetChrSubChip(0x21, 0x0)
    SetChrPos(0x21, -54000, 0, 104300, 0)
    SetChrChipByIndex(0x22, 0x2C)
    SetChrSubChip(0x22, 0x0)
    SetChrPos(0x22, -54900, 0, 105200, 0)
    SetChrChipByIndex(0x24, 0x2E)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x24, -48900, 0, 103000, 0)
    SetChrPos(0x1D, -53100, 0, 107000, 0)
    SetChrPos(0x23, -52700, 0, 105600, 0)
    SetChrPos(0x17, -51000, 0, 108300, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x3)
    OP_68(-52000, 1100, 105600, 4000)
    MoveCamera(38, 23, 0, 4000)
    SetCameraDistance(17000, 4000)
    BeginChrThread(0xA, 3, 0, 51)
    Sleep(600)
    BeginChrThread(0x9, 3, 0, 52)
    Sleep(600)
    BeginChrThread(0xD, 3, 0, 53)
    Sleep(600)
    BeginChrThread(0x8, 3, 0, 54)
    BeginChrThread(0xB, 3, 0, 55)
    Sleep(600)
    BeginChrThread(0xC, 3, 0, 56)
    WaitChrThread(0xA, 3)

    ChrTalk(
        0xA,
        "#07107F#11PYour Highness, are you OK!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#6P#07008FYes, somehow\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 3)
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#07301FThe current … …\x01",
            "Is it a line fault high speed boat?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x0, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x1F,
        "#12P#07201FYes, no doubt\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x0, 0x1F4)
    Sleep(150)

    ChrTalk(
        0xB,
        (
            "#12P#N#12001FThe other one is Verne\x01",
            "It's military gunship …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0xC, 0x0, 0x1F4)
    Sleep(150)

    ChrTalk(
        0xC,
        (
            "Yeah, what was robbed by them\x01",
            "It was in the report … ….!\x02",
        )
    )

    CloseMessageWindow()
    Sound(121, 0, 100, 0)
    Sound(811, 0, 50, 0)
    ClearChrFlags(0x25, 0x80)

    def lambda_A86D():
        OP_96(0xFE, 0xFFFF34E0, 0x0, 0x19258, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_A86D)

    def lambda_A887():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_A887)
    WaitChrThread(0x25, 1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x25,
        "#12P#00607F#3457V#30WEveryone, are you safe?\x02",
    )

    CloseMessageWindow()
    OP_24(0xD81)
    OP_C9(0x1, 0x80000000)

    def lambda_A8ED():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_A8ED)

    def lambda_A8FA():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_A8FA)
    Sleep(50)

    def lambda_A90A():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_A90A)

    def lambda_A917():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_A917)

    def lambda_A924():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_A924)
    Sleep(50)

    def lambda_A934():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_A934)

    def lambda_A941():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_A941)
    Sleep(50)

    def lambda_A951():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_A951)

    def lambda_A95E():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A95E)

    ChrTalk(
        0x23,
        "#02501F#5PYes, somehow\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#02801F#5PBut where did they go\x02",
    )

    CloseMessageWindow()
    Sound(867, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(60, 0, -1, -1)
    SetChrName("Voice of a man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "……HM.\x01",
            "You seem to be heard.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-52000, 1100, 106600, 1000)
    SetCameraDistance(18000, 1000)

    def lambda_AA10():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_AA10)

    def lambda_AA1D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_AA1D)
    Sleep(50)

    def lambda_AA2D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_AA2D)

    def lambda_AA3A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_AA3A)

    def lambda_AA47():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_AA47)
    Sleep(50)

    def lambda_AA57():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_AA57)

    def lambda_AA64():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_AA64)

    def lambda_AA71():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AA71)

    def lambda_AA7E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_AA7E)
    Sleep(50)

    def lambda_AA8E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_AA8E)

    def lambda_AA9B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_AA9B)

    def lambda_AAA8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_AAA8)

    def lambda_AAB5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_AAB5)
    OP_6F(0x79)
    SetMessageWindowPos(60, 0, -1, -1)
    SetChrName("Voice of a man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "── People attending the meeting.\x01",
            "We are the \"Empire Liberation Front\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(10, 60, -1, -1)
    SetChrName("Voice of a young man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "─ ─ also of Calvert\x01",
            "I stood up to protect the old tradition\x01",
            "He is a faction of \"anti-immigration policyist\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x21,
        "#12PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#12P#02205FI am active in the Empire and the Republic\x01",
            "Terrorist group …! Is it?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(60, 0, -1, -1)
    SetChrName("Voice of a man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "This time, we\x01",
            "Hatred villain#4RTemple#Because it is a cause\x01",
            "It coincided with cooperating with each other.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetChrName("Voice of a man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "─ ─ Prepare to be prepared!\x01",
            "\"Chief Iron Blood\" Gillius Osborne!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(10, 60, -1, -1)
    SetChrName("Voice of a young man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "President Rock Smith!\x01",
            "You will disappear here!\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "It was eroded by an abominable Easterner\x01",
            "To protect the tradition of Calvert\x01",
            "That much rough treatment is necessary!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x22,
        "#6P#07506FWhat fools\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#07403F#12PHmm, this wont do\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#N#11508FBut …\x01",
            "I heard that it is a bit masu.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x17,
        "Flippers Arios",
        "#11P#01401FYeah. They're coming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        "#12P#00610FAh!\x02",
    )

    CloseMessageWindow()
    OP_68(-52000, 1600, 106600, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_24(0x361)
    OP_24(0x35D)
    OP_24(0x1F1)
    OP_24(0x339)
    SetScenarioFlags(0x22, 2)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_43_9903 end

    def Function_44_AEB2(): pass

    label("Function_44_AEB2")


    def lambda_AEB7():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AEB7)
    Sleep(1500)

    def lambda_AED4():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AED4)
    Sleep(300)

    def lambda_AEF1():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AEF1)
    Sleep(300)

    def lambda_AF0E():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF0E)
    Sleep(300)

    def lambda_AF2B():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF2B)
    Sleep(300)

    def lambda_AF48():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF48)
    Sleep(300)

    def lambda_AF65():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF65)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_44_AEB2 end

    def Function_45_AF7F(): pass

    label("Function_45_AF7F")


    def lambda_AF84():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF84)
    Sleep(1500)

    def lambda_AFA1():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AFA1)
    Sleep(300)

    def lambda_AFBE():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AFBE)
    Sleep(300)

    def lambda_AFDB():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AFDB)
    Sleep(300)

    def lambda_AFF8():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AFF8)
    Sleep(300)

    def lambda_B015():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B015)
    Sleep(300)

    def lambda_B032():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B032)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_45_AF7F end

    def Function_46_B04C(): pass

    label("Function_46_B04C")


    def lambda_B051():
        OP_95(0xFE, -56700, 0, 123900, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B051)
    WaitChrThread(0x1D, 1)

    def lambda_B06F():
        OP_95(0xFE, -59000, 0, 120600, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B06F)
    WaitChrThread(0x1D, 1)

    def lambda_B08D():
        OP_95(0xFE, -59000, 0, 118600, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B08D)
    WaitChrThread(0x1D, 1)
    Return()

    # Function_46_B04C end

    def Function_47_B0A7(): pass

    label("Function_47_B0A7")


    def lambda_B0AC():
        OP_95(0xFE, -48000, 0, 124600, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_B0AC)
    WaitChrThread(0x17, 1)
    Sleep(500)

    def lambda_B0CD():
        OP_97(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_B0CD)
    WaitChrThread(0x17, 1)

    def lambda_B0EB():
        OP_97(0xFE, 0x7D0, 0x0, 0xFFFFF830, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_B0EB)
    WaitChrThread(0x17, 1)

    def lambda_B109():
        OP_97(0xFE, 0x7D0, 0x0, 0xFFFFEC78, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_B109)
    WaitChrThread(0x17, 1)
    Return()

    # Function_47_B0A7 end

    def Function_48_B123(): pass

    label("Function_48_B123")

    Sleep(1000)

    def lambda_B12B():
        OP_97(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_B12B)
    WaitChrThread(0x23, 1)

    def lambda_B149():
        OP_97(0xFE, 0x7D0, 0x0, 0xFFFFF830, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_B149)
    WaitChrThread(0x23, 1)

    def lambda_B167():
        OP_97(0xFE, 0x7D0, 0x0, 0xFFFFEC78, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_B167)
    WaitChrThread(0x23, 1)
    Return()

    # Function_48_B123 end

    def Function_49_B181(): pass

    label("Function_49_B181")


    def lambda_B186():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B186)
    Sleep(300)

    def lambda_B1A3():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B1A3)
    Sleep(300)

    def lambda_B1C0():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B1C0)
    Sleep(300)

    def lambda_B1DD():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B1DD)
    Sleep(300)

    def lambda_B1FA():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B1FA)
    Sleep(300)

    def lambda_B217():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B217)
    Sleep(300)

    def lambda_B234():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B234)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_49_B181 end

    def Function_50_B24E(): pass

    label("Function_50_B24E")

    Sleep(400)

    def lambda_B256():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B256)
    Sleep(300)

    def lambda_B273():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B273)
    Sleep(300)

    def lambda_B290():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B290)
    Sleep(300)

    def lambda_B2AD():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B2AD)
    Sleep(300)

    def lambda_B2CA():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B2CA)
    Sleep(300)

    def lambda_B2E7():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B2E7)
    Sleep(300)

    def lambda_B304():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B304)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_50_B24E end

    def Function_51_B31E(): pass

    label("Function_51_B31E")


    def lambda_B323():
        OP_95(0xFE, -39800, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B323)

    def lambda_B33D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B33D)
    WaitChrThread(0xFE, 1)

    def lambda_B352():
        OP_95(0xFE, -42500, 0, 108000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B352)
    WaitChrThread(0xFE, 1)

    def lambda_B370():
        OP_95(0xFE, -48800, 0, 104500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B370)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xA, 0x20, 500)
    TurnDirection(0x20, 0xA, 500)
    Return()

    # Function_51_B31E end

    def Function_52_B398(): pass

    label("Function_52_B398")


    def lambda_B39D():
        OP_95(0xFE, -39800, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B39D)

    def lambda_B3B7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B3B7)
    WaitChrThread(0xFE, 1)

    def lambda_B3CC():
        OP_95(0xFE, -42500, 0, 108000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B3CC)
    WaitChrThread(0xFE, 1)

    def lambda_B3EA():
        OP_95(0xFE, -48000, 0, 106500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B3EA)
    WaitChrThread(0xFE, 1)
    TurnDirection(0x1F, 0x9, 500)
    Return()

    # Function_52_B398 end

    def Function_53_B40B(): pass

    label("Function_53_B40B")


    def lambda_B410():
        OP_95(0xFE, -39800, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B410)

    def lambda_B42A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B42A)
    WaitChrThread(0xFE, 1)

    def lambda_B43F():
        OP_95(0xFE, -42500, 0, 108000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B43F)
    WaitChrThread(0xFE, 1)

    def lambda_B45D():
        OP_95(0xFE, -49200, 0, 108000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B45D)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x1E, 500)
    Return()

    # Function_53_B40B end

    def Function_54_B47E(): pass

    label("Function_54_B47E")


    def lambda_B483():
        OP_95(0xFE, -39800, 0, 110200, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B483)

    def lambda_B49D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B49D)
    WaitChrThread(0xFE, 1)

    def lambda_B4B2():
        OP_95(0xFE, -42500, 0, 108000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4B2)
    WaitChrThread(0xFE, 1)

    def lambda_B4D0():
        OP_95(0xFE, -48000, 0, 108000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4D0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_54_B47E end

    def Function_55_B4EA(): pass

    label("Function_55_B4EA")


    def lambda_B4EF():
        OP_95(0xFE, -64400, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4EF)

    def lambda_B509():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B509)
    WaitChrThread(0xFE, 1)

    def lambda_B51E():
        OP_95(0xFE, -55900, 0, 104400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B51E)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x22, 500)
    Return()

    # Function_55_B4EA end

    def Function_56_B53F(): pass

    label("Function_56_B53F")


    def lambda_B544():
        OP_95(0xFE, -64400, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B544)

    def lambda_B55E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B55E)
    WaitChrThread(0xFE, 1)

    def lambda_B573():
        OP_95(0xFE, -55600, 0, 106300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B573)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x22, 500)
    Return()

    # Function_56_B53F end

    def Function_57_B594(): pass

    label("Function_57_B594")

    Sound(497, 2, 10, 0)
    Sound(825, 2, 10, 0)
    Sleep(80)
    OP_25(0x1F1, 0xF)
    OP_25(0x339, 0xF)
    Sleep(80)
    OP_25(0x1F1, 0x14)
    OP_25(0x339, 0x14)
    Sleep(80)
    OP_25(0x1F1, 0x19)
    OP_25(0x339, 0x19)
    Sleep(80)
    OP_25(0x1F1, 0x1E)
    OP_25(0x339, 0x1E)
    Sleep(80)
    OP_25(0x1F1, 0x23)
    OP_25(0x339, 0x23)
    Sleep(80)
    OP_25(0x1F1, 0x28)
    OP_25(0x339, 0x28)
    Sleep(80)
    OP_25(0x1F1, 0x2D)
    OP_25(0x339, 0x2D)
    Sleep(80)
    OP_25(0x1F1, 0x32)
    OP_25(0x339, 0x32)
    Sleep(80)
    OP_25(0x1F1, 0x37)
    Sleep(80)
    OP_25(0x1F1, 0x3C)
    Return()

    # Function_57_B594 end

    def Function_58_B607(): pass

    label("Function_58_B607")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51258.itc", 0x1E)
    OP_68(-39500, 1000, 106000, 0)
    MoveCamera(49, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x25, 0x1E)
    SetChrSubChip(0x25, 0x1)
    SetChrFlags(0x25, 0x10)
    SetChrFlags(0x25, 0x20)
    SetChrFlags(0x25, 0x2)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, -39500, 0, 106000, 270)
    SetCameraDistance(15500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x25,
        (
            "#00607F#11P── here\x01",
            "He said he was going straight! Is it?\x02\x03",
            "#00606FUgh… so that's why they took the blueprints\x02\x03",
            "#00610FThe guard who had been waiting anyway\x01",
            "Let me hurry to this person - ─\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetCameraDistance(15000, 300)
    OP_82(0xC8, 0xC8, 0xBB8, 0x12C)

    ChrTalk(
        0x25,
        "#00607F#4S#11PWhat?!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_58_B607 end

    def Function_59_B788(): pass

    label("Function_59_B788")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02450.itc", 0x5)
    LoadChrToIndex("chr/ch02451.itc", 0x6)
    LoadChrToIndex("chr/ch00950.itc", 0x7)
    LoadChrToIndex("chr/ch00951.itc", 0x8)
    LoadChrToIndex("chr/ch00952.itc", 0x9)
    LoadChrToIndex("chr/ch00953.itc", 0xA)
    LoadChrToIndex("chr/ch42250.itc", 0xB)
    LoadChrToIndex("chr/ch42251.itc", 0xC)
    LoadChrToIndex("chr/ch42252.itc", 0xD)
    LoadChrToIndex("chr/ch42253.itc", 0xE)
    LoadChrToIndex("chr/ch42254.itc", 0xF)
    LoadChrToIndex("chr/ch42350.itc", 0x10)
    LoadChrToIndex("chr/ch42351.itc", 0x11)
    LoadChrToIndex("chr/ch42352.itc", 0x12)
    LoadChrToIndex("chr/ch42353.itc", 0x13)
    LoadChrToIndex("chr/ch42550.itc", 0x14)
    LoadChrToIndex("chr/ch42551.itc", 0x15)
    LoadChrToIndex("chr/ch42552.itc", 0x16)
    LoadChrToIndex("chr/ch42553.itc", 0x17)
    LoadChrToIndex("chr/ch42554.itc", 0x18)
    LoadChrToIndex("apl/ch51236.itc", 0x19)
    LoadChrToIndex("apl/ch51262.itc", 0x1A)
    LoadChrToIndex("apl/ch51263.itc", 0x1B)
    LoadChrToIndex("apl/ch51264.itc", 0x1C)
    LoadChrToIndex("apl/ch51237.itc", 0x1D)
    LoadChrToIndex("apl/ch51265.itc", 0x1E)
    LoadChrToIndex("apl/ch51238.itc", 0x1F)
    LoadChrToIndex("apl/ch51267.itc", 0x20)
    LoadChrToIndex("chr/ch02452.itc", 0x21)
    LoadChrToIndex("chr/ch02456.itc", 0x22)
    LoadChrToIndex("chr/ch00900.itc", 0x23)
    LoadChrToIndex("apl/ch51223.itc", 0x24)
    LoadChrToIndex("apl/ch51266.itc", 0x25)
    LoadChrToIndex("apl/ch51268.itc", 0x26)
    LoadChrToIndex("chr/ch00959.itc", 0x27)
    LoadEffect(0x0, "event/ev12013.eff")
    LoadEffect(0x1, "battle/btgun00.eff")
    LoadEffect(0x2, "event/ev606_00.eff")
    LoadEffect(0x3, "battle/cr425100.eff")
    LoadEffect(0x4, "event/ev12012.eff")
    LoadEffect(0x5, "event/eva01_01.eff")
    SoundLoad(860)
    SoundLoad(861)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x101, -15000, 0, 0, 90)
    SetChrPos(0x102, -15000, 0, 500, 90)
    SetChrPos(0x103, -15000, 0, 0, 90)
    SetChrPos(0x104, -15000, 0, 1000, 90)
    SetChrPos(0x109, -15000, 0, -1000, 90)
    SetChrPos(0x105, -15000, 0, -1000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    EndChrThread(0x17, 0xFF)
    SetChrChipByIndex(0x17, 0x5)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 12000, 0, 0, 270)
    EndChrThread(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 13000, 0, 0, 270)
    EndChrThread(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x1D)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 14000, 0, 0, 270)
    SetChrChipByIndex(0x25, 0x9)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 23700, 0, -800, 90)
    SetChrChipByIndex(0x36, 0x19)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, 23900, 0, 1000, 90)
    SetChrChipByIndex(0x37, 0x19)
    SetChrSubChip(0x37, 0x0)
    ClearChrFlags(0x37, 0x80)
    SetChrFlags(0x37, 0x8000)
    SetChrPos(0x37, 24400, 0, -1900, 90)
    SetChrChipByIndex(0x26, 0xC)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 81000, 0, 5500, 180)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x27, 0xC)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 80500, 0, 5500, 180)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x28, 0xC)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 81500, 0, 5500, 180)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x29, 0xC)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, 80500, 0, 5500, 180)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2A, 0xC)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, 81500, 0, 5500, 180)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2E, 0x15)
    SetChrSubChip(0x2E, 0x0)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x8000)
    SetChrPos(0x2E, 81000, 0, 5500, 180)
    OP_A7(0x2E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2F, 0x15)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 80500, 0, 5500, 180)
    OP_A7(0x2F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x30, 0x15)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x80)
    SetChrFlags(0x30, 0x8000)
    SetChrPos(0x30, 81500, 0, 5500, 180)
    OP_A7(0x30, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x31, 0x15)
    SetChrSubChip(0x31, 0x0)
    ClearChrFlags(0x31, 0x80)
    SetChrFlags(0x31, 0x8000)
    SetChrPos(0x31, 80500, 0, 5500, 180)
    OP_A7(0x31, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x32, 0x15)
    SetChrSubChip(0x32, 0x0)
    ClearChrFlags(0x32, 0x80)
    SetChrFlags(0x32, 0x8000)
    SetChrPos(0x32, 81500, 0, 5500, 180)
    OP_A7(0x32, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x4)
    OP_68(79000, 2500, 0, 0)
    MoveCamera(60, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_68(79000, 1500, 0, 3000)
    FadeToBright(2000, 0)
    Sleep(2500)
    Sound(160, 0, 100, 0)
    Sleep(300)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x6, 0x10)
    OP_71(0x6, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x6)
    OP_68(72000, 1500, 0, 4000)
    MoveCamera(53, 13, 0, 4000)
    SetCameraDistance(17000, 4000)
    BeginChrThread(0x2E, 3, 0, 83)
    Sleep(400)
    BeginChrThread(0x2F, 3, 0, 84)
    Sleep(200)
    Sound(937, 0, 100, 0)
    BeginChrThread(0x30, 3, 0, 85)
    Sleep(400)
    BeginChrThread(0x31, 3, 0, 84)
    Sleep(200)
    BeginChrThread(0x32, 3, 0, 85)
    Sleep(400)
    BeginChrThread(0x26, 3, 0, 83)
    Sleep(400)
    BeginChrThread(0x27, 3, 0, 84)
    Sleep(200)
    BeginChrThread(0x28, 3, 0, 85)
    Sleep(400)
    BeginChrThread(0x29, 3, 0, 84)
    Sleep(200)
    BeginChrThread(0x2A, 3, 0, 85)
    OP_6F(0x79)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A7(0x2E, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2F, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x30, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x31, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x32, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    EndChrThread(0x2E, 0xFF)
    EndChrThread(0x2F, 0xFF)
    EndChrThread(0x30, 0xFF)
    EndChrThread(0x31, 0xFF)
    EndChrThread(0x32, 0xFF)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    EndChrThread(0x26, 0xFF)
    EndChrThread(0x27, 0xFF)
    EndChrThread(0x28, 0xFF)
    EndChrThread(0x29, 0xFF)
    EndChrThread(0x2A, 0xFF)
    ClearChrFlags(0x46, 0x80)
    OP_78(0xF, 0x46)
    OP_49()
    SetChrPos(0x46, 25500, 0, 0, 0)
    OP_D5(0x46, 0x0, 0x13880, 0x0, 0x0)
    SetMapObjFlags(0xF, 0x1000)
    ClearMapObjFlags(0xF, 0x4)
    ClearChrFlags(0x47, 0x80)
    OP_78(0x10, 0x47)
    OP_49()
    SetChrPos(0x47, 25500, 0, 0, 0)
    OP_D5(0x47, 0x0, 0x13880, 0x0, 0x0)
    SetMapObjFlags(0x10, 0x1000)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFrame(0xFF, "kokeru00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kokeru01", 0x0, 0x1)
    SetChrChipByIndex(0x2E, 0x16)
    SetChrSubChip(0x2E, 0x3)
    SetChrChipByIndex(0x2F, 0x16)
    SetChrSubChip(0x2F, 0x3)
    SetChrChipByIndex(0x30, 0x16)
    SetChrSubChip(0x30, 0x3)
    SetChrChipByIndex(0x31, 0x16)
    SetChrSubChip(0x31, 0x3)
    SetChrChipByIndex(0x32, 0x16)
    SetChrSubChip(0x32, 0x3)
    SetChrPos(0x2E, 32800, 0, 1500, 270)
    SetChrPos(0x2F, 32200, 0, -100, 270)
    SetChrPos(0x30, 37500, 0, 300, 270)
    OP_A7(0x30, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x31, 37500, 0, -300, 270)
    OP_A7(0x31, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x32, 33700, 0, -2500, 270)
    OP_68(32900, 900, 0, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_68(29200, 900, 0, 4000)
    SetCameraDistance(17500, 4000)
    ClearScenarioFlags(0x0, 1)
    FadeToBright(1000, 0)
    BeginChrThread(0x2E, 3, 0, 101)
    BeginChrThread(0x36, 3, 0, 88)
    BeginChrThread(0x4C, 1, 0, 122)
    BeginChrThread(0x4C, 2, 0, 123)
    PlayEffect(0x3, 0x1, 0xFF, 0x0, 26000, 700, 700, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sound(860, 2, 80, 0)
    Sleep(100)
    BeginChrThread(0x2F, 3, 0, 100)
    BeginChrThread(0x37, 3, 0, 88)
    PlayEffect(0x3, 0x2, 0xFF, 0x0, 26400, 700, -1600, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    BeginChrThread(0x32, 3, 0, 101)
    BeginChrThread(0x25, 3, 0, 89)
    PlayEffect(0x3, 0x3, 0xFF, 0x0, 27500, 0, 0, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x101, 3, 0, 82)
    Sound(861, 2, 80, 0)
    OP_0D()
    Sleep(500)
    BeginChrThread(0x30, 3, 0, 86)
    Sleep(500)
    BeginChrThread(0x31, 3, 0, 87)
    Sound(2512, 255, 100, 0)
    Sleep(3000)
    Sound(2513, 255, 100, 0)
    OP_6F(0x79)
    OP_AD(0x1)
    EndChrThread(0x2F, 0x3)
    SetChrChipByIndex(0x2F, 0x18)
    SetChrSubChip(0x2F, 0x2)
    Sleep(100)
    SetChrSubChip(0x2F, 0x3)
    Sleep(200)
    SetChrSubChip(0x2F, 0x4)
    Sound(809, 0, 100, 0)
    Sound(250, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x2F, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x4C, 0x1)
    OP_68(24000, 500, 0, 500)
    MoveCamera(35, 25, 0, 500)
    SetCameraDistance(15500, 500)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    OP_82(0x12C, 0x12C, 0xBB8, 0x3E8)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 26000, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sound(200, 0, 100, 0)
    Sound(833, 0, 100, 0)
    ClearMapObjFlags(0x10, 0x4)
    OP_75(0xF, 0x1, 0x12C)
    OP_75(0x10, 0x2, 0x12C)
    EndChrThread(0x36, 0x3)
    BeginChrThread(0x36, 3, 0, 102)
    Sleep(50)
    EndChrThread(0x37, 0x3)
    BeginChrThread(0x37, 3, 0, 103)
    Sleep(50)
    EndChrThread(0x25, 0x3)
    BeginChrThread(0x25, 3, 0, 104)
    StopSound(860, 3000, 70)
    StopSound(861, 3000, 70)

    ChrTalk(
        0x36,
        "#13AOooh!\x02",
    )

    Sleep(50)

    ChrTalk(
        0x37,
        "#5P#13AAlright!\x02",
    )

    Sleep(50)

    ChrTalk(
        0x25,
        "#6P#00610F#13AAh!\x02",
    )

    WaitChrThread(0x25, 3)
    OP_6F(0x79)
    LoadEffect(0x0, "battle/cr024101.eff")
    LoadEffect(0x4, "battle/cr024100.eff")
    LoadEffect(0x6, "battle/cr024201.eff")
    LoadEffect(0x7, "battle/cr024401.eff")
    Fade(500)
    OP_68(34500, 700, 0, 0)
    MoveCamera(43, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_68(33500, 700, 0, 2000)
    SetCameraDistance(17500, 2000)
    StopEffect(0x3, 0x0)
    SetChrPos(0x2E, 32800, 0, 2500, 270)
    SetChrChipByIndex(0x2E, 0x14)
    SetChrSubChip(0x2E, 0x0)
    EndChrThread(0x2E, 0xFF)
    EndChrThread(0x4C, 0x2)
    SetChrPos(0x2F, 32200, 0, 900, 270)
    SetChrChipByIndex(0x2F, 0x14)
    SetChrSubChip(0x2F, 0x0)
    EndChrThread(0x2F, 0xFF)
    SetChrPos(0x30, 34200, 0, 1500, 270)
    SetChrChipByIndex(0x30, 0x14)
    SetChrSubChip(0x30, 0x0)
    EndChrThread(0x30, 0xFF)
    SetChrPos(0x31, 33400, 0, -1800, 270)
    SetChrChipByIndex(0x31, 0x14)
    SetChrSubChip(0x31, 0x0)
    EndChrThread(0x31, 0xFF)
    SetChrPos(0x32, 33700, 0, -3000, 270)
    SetChrChipByIndex(0x32, 0x14)
    SetChrSubChip(0x32, 0x0)
    EndChrThread(0x32, 0xFF)
    SetChrPos(0x26, 37700, 0, -300, 270)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x27, 38900, 0, -1000, 270)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x28, 38900, 0, 0, 270)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x29, 40200, 0, -650, 270)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x25, 19700, 0, -1500, 90)
    SetChrPos(0x36, 21100, 0, 2900, 135)
    SetChrPos(0x37, 21100, 0, -3300, 90)
    SetMapObjFlags(0xF, 0x4)
    SetChrChipByIndex(0x26, 0xC)
    SetChrSubChip(0x26, 0x0)

    def lambda_C3BC():
        OP_95(0xFE, 29700, 0, -300, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_C3BC)

    def lambda_C3D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_C3D6)
    Sleep(100)
    SetChrChipByIndex(0x27, 0xC)
    SetChrSubChip(0x27, 0x0)

    def lambda_C3F2():
        OP_95(0xFE, 30900, 0, -1000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_C3F2)

    def lambda_C40C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_C40C)
    Sleep(100)
    SetChrChipByIndex(0x28, 0xC)
    SetChrSubChip(0x28, 0x0)

    def lambda_C428():
        OP_95(0xFE, 30900, 0, 0, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_C428)

    def lambda_C442():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_C442)
    Sleep(100)
    SetChrChipByIndex(0x29, 0xC)
    SetChrSubChip(0x29, 0x0)

    def lambda_C45E():
        OP_95(0xFE, 32200, 0, -650, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_C45E)

    def lambda_C478():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_C478)
    WaitChrThread(0x26, 1)
    SetChrChipByIndex(0x26, 0xB)
    SetChrSubChip(0x26, 0x0)
    WaitChrThread(0x27, 1)
    SetChrChipByIndex(0x27, 0xB)
    SetChrSubChip(0x27, 0x0)
    WaitChrThread(0x28, 1)
    SetChrChipByIndex(0x28, 0xB)
    SetChrSubChip(0x28, 0x0)
    WaitChrThread(0x29, 1)
    SetChrChipByIndex(0x29, 0xB)
    SetChrSubChip(0x29, 0x0)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x26,
        "#11P#4SNOW!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x27,
        "#11P#4SGet the chancellor!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x26, 3, 0, 105)
    BeginChrThread(0x17, 3, 0, 81)
    Sleep(150)
    BeginChrThread(0x27, 3, 0, 106)
    Sleep(150)
    BeginChrThread(0x28, 3, 0, 107)
    Sleep(150)
    BeginChrThread(0x29, 3, 0, 108)
    Fade(250)
    OP_68(24000, 700, 0, 0)
    MoveCamera(43, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    MoveCamera(43, 25, -10, 1000)
    SetCameraDistance(16500, 1000)
    OP_0D()
    WaitChrThread(0x17, 3)

    ChrTalk(
        0x17,
        "#01401F#5PThis is as far as you go\x02",
    )

    CloseMessageWindow()

    def lambda_C5A9():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_C5A9)
    Sleep(500)

    def lambda_C5C5():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_C5C5)
    Sleep(300)
    SetChrSubChip(0x26, 0x1)
    Sleep(90)
    Sound(802, 0, 100, 0)
    Sound(531, 0, 30, 0)
    SetChrChipByIndex(0x26, 0xB)
    SetChrSubChip(0x26, 0x0)
    Sleep(300)
    SetChrSubChip(0x29, 0x2)
    Sleep(90)
    SetChrSubChip(0x29, 0x1)
    Sleep(90)
    Sound(802, 0, 100, 0)
    Sound(531, 0, 30, 0)
    SetChrChipByIndex(0x29, 0xB)
    SetChrSubChip(0x29, 0x0)

    ChrTalk(
        0x26,
        "#11PUgh, the Divine Blade of Wind…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#11PDo not worry!\x01",
            "I will set a wavy attack!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(23500, 900, 0, 2000)
    MoveCamera(50, 21, 0, 2000)
    SetCameraDistance(17000, 2000)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, 11700, 0, 2100, 90)
    SetChrPos(0x9, 11100, 0, 700, 90)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)

    def lambda_C6C5():
        OP_95(0xFE, 19400, 0, 1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C6C5)
    Sleep(200)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)

    def lambda_C6EA():
        OP_95(0xFE, 18900, 0, -300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C6EA)
    WaitChrThread(0xA, 1)
    Sound(318, 0, 100, 0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    WaitChrThread(0x9, 1)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x9, 0x1D)
    SetChrSubChip(0x9, 0x0)

    ChrTalk(
        0xA,
        "#07107F#5PWe'll cover you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#07307F#5PFall back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        "#00610F#6P#NWe won't budge!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x25, 3, 0, 62)
    Sleep(300)
    BeginChrThread(0x36, 3, 0, 60)

    ChrTalk(
        0x26,
        "#12PMuller Vander!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        "#12PFrom the Arnor family.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        "#11PAnd the captian of the Liberl guard?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        "#11PWho cares, let's do it!\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "event/ev12015.eff")
    LoadEffect(0x2, "event/ev12017.eff")
    LoadEffect(0x4, "event/ev12018.eff")
    LoadEffect(0x8, "event/ev12019.eff")
    LoadEffect(0x6, "battle/ms00001.eff")
    OP_68(29000, 700, 0, 5000)
    MoveCamera(45, 21, 0, 5000)
    SetCameraDistance(16500, 5000)
    SetChrChipByIndex(0x30, 0x16)
    SetChrSubChip(0x30, 0x3)
    BeginChrThread(0x30, 3, 0, 101)
    BeginChrThread(0x4C, 2, 0, 123)
    PlayEffect(0x3, 0x1, 0xFF, 0x0, 28000, 0, 0, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sound(860, 2, 80, 0)
    Sound(861, 2, 80, 0)
    Sleep(50)
    SetChrChipByIndex(0x2E, 0x16)
    SetChrSubChip(0x2E, 0x3)
    BeginChrThread(0x2E, 3, 0, 101)
    Sleep(50)
    SetChrChipByIndex(0x31, 0x16)
    SetChrSubChip(0x31, 0x3)
    BeginChrThread(0x31, 3, 0, 101)
    Sleep(50)
    SetChrChipByIndex(0x2F, 0x16)
    SetChrSubChip(0x2F, 0x3)
    BeginChrThread(0x2F, 3, 0, 101)
    Sleep(50)
    SetChrChipByIndex(0x32, 0x16)
    SetChrSubChip(0x32, 0x3)
    BeginChrThread(0x32, 3, 0, 101)
    Sleep(100)
    BeginChrThread(0x17, 0, 0, 74)
    Sleep(1500)
    BeginChrThread(0xA, 0, 0, 69)
    BeginChrThread(0x9, 0, 0, 63)
    Sleep(3300)
    EndChrThread(0x25, 0x3)
    BeginChrThread(0x25, 0, 0, 73)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    StopSound(860, 1000, 75)
    StopSound(861, 1000, 75)
    OP_0D()
    OP_49()
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    EndChrThread(0x17, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x25, 0xFF)
    EndChrThread(0x36, 0xFF)
    EndChrThread(0x37, 0xFF)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    EndChrThread(0x26, 0xFF)
    EndChrThread(0x27, 0xFF)
    EndChrThread(0x28, 0xFF)
    EndChrThread(0x29, 0xFF)
    EndChrThread(0x4C, 0x2)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    EndChrThread(0x2E, 0xFF)
    EndChrThread(0x2F, 0xFF)
    EndChrThread(0x30, 0xFF)
    EndChrThread(0x31, 0xFF)
    EndChrThread(0x32, 0xFF)
    LoadChrToIndex("chr/ch00050.itc", 0x5)
    LoadChrToIndex("chr/ch00150.itc", 0x6)
    LoadChrToIndex("chr/ch00250.itc", 0x7)
    LoadChrToIndex("chr/ch00350.itc", 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x9)
    LoadChrToIndex("chr/ch03050.itc", 0xA)
    LoadChrToIndex("monster/ch84150.itc", 0xB)
    LoadChrToIndex("monster/ch84250.itc", 0xC)
    LoadChrToIndex("monster/ch84350.itc", 0xD)
    SoundLoad(943)
    SoundLoad(863)
    SetChrChipByIndex(0x49, 0xB)
    SetChrSubChip(0x49, 0x0)
    SetChrFlags(0x49, 0x8000)
    SetChrPos(0x49, -17500, 0, 0, 90)
    OP_A7(0x49, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x4A, 0xC)
    SetChrSubChip(0x4A, 0x0)
    SetChrFlags(0x4A, 0x8000)
    SetChrPos(0x4A, -17500, 0, 0, 90)
    OP_A7(0x4A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x4B, 0xD)
    SetChrSubChip(0x4B, 0x0)
    SetChrFlags(0x4B, 0x8000)
    SetChrPos(0x4B, -17500, 0, 0, 90)
    OP_A7(0x4B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-6000, 1100, 0, 0)
    MoveCamera(39, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    OP_68(7000, 1100, 0, 5000)
    SetCameraDistance(18000, 5000)
    FadeToBright(1000, 0)
    Sound(863, 2, 60, 0)
    BeginChrThread(0x4C, 1, 0, 124)
    BeginChrThread(0x101, 3, 0, 90)
    Sleep(200)
    BeginChrThread(0x102, 3, 0, 91)
    Sleep(200)
    BeginChrThread(0x103, 3, 0, 92)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 93)
    BeginChrThread(0x105, 3, 0, 95)
    Sleep(200)
    BeginChrThread(0x109, 3, 0, 94)
    WaitChrThread(0x109, 3)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00011FAmazing…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FInsane…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#5PBut if they're there…\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 9500, 0, 5000, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(121, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x4)
    Sleep(150)
    OP_68(8500, 1300, 1500, 1200)

    def lambda_CC28():
        OP_96(0xFE, 0x251C, 0x0, 0xE10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CC28)

    def lambda_CC42():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_CC42)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xE1, 0x1F4)

    def lambda_CC5E():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CC5E)
    Sleep(50)

    def lambda_CC6E():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CC6E)
    Sleep(50)

    def lambda_CC7E():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CC7E)
    Sleep(50)

    def lambda_CC8E():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_CC8E)
    Sleep(50)

    def lambda_CC9E():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_CC9E)
    Sleep(50)

    def lambda_CCAE():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CCAE)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "#5P#11505FOh you're here\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#12P#00001FLechter…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FAll the participants\x01",
            "Is not it safe? Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#11503FYeah, for now\x02",
    )

    CloseMessageWindow()
    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 10500, 0, 5000, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_CDA2():
        OP_96(0xFE, 0x2904, 0x0, 0xDAC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_CDA2)

    def lambda_CDBC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_CDBC)
    WaitChrThread(0xB, 1)
    OP_93(0xB, 0xE1, 0x1F4)

    ChrTalk(
        0xB,
        (
            "#11P#12001F─ ─ After a while.\x01",
            "It will come from behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FHuh…\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_CE57():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CE57)
    Sleep(50)
    OP_93(0x105, 0x10E, 0x1F4)

    ChrTalk(
        0x103,
        "#11P#00201FReinforcements!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#11P#10301FSomehow they got through\x02",
    )

    CloseMessageWindow()

    def lambda_CEB4():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_CEB4)
    Sleep(50)

    def lambda_CEC4():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CEC4)
    Sleep(50)

    def lambda_CED4():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CED4)
    Sleep(50)

    def lambda_CEE4():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CEE4)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)

    def lambda_CF04():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_CF04)

    def lambda_CF11():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_CF11)
    Fade(500)
    OP_68(-13900, 900, 0, 0)
    MoveCamera(37, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_68(2100, 900, 0, 4500)
    MoveCamera(30, 23, 0, 4500)
    SetCameraDistance(18000, 4500)
    ClearChrFlags(0x49, 0x80)
    ClearChrFlags(0x4A, 0x80)
    ClearChrFlags(0x4B, 0x80)
    Sound(943, 2, 70, 0)
    BeginChrThread(0x49, 3, 0, 96)
    Sleep(600)
    BeginChrThread(0x4A, 3, 0, 97)
    Sleep(600)
    BeginChrThread(0x4B, 3, 0, 98)
    OP_6F(0x79)
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x5)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x6)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x7)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x8)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x9)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xA)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    ChrTalk(
        0x109,
        "#12P#10111FT-this is\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00307FHe was in the mafia's hide\x01",
            "Look at similar types!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007FAnyway, let's take them out!\x02",
    )

    CloseMessageWindow()
    StopSound(863, 500, 60)
    EndChrThread(0x4C, 0x1)
    Sound(943, 2, 70, 0)
    EndChrThread(0x49, 0x3)
    EndChrThread(0x4A, 0x3)
    EndChrThread(0x4B, 0x3)

    def lambda_D08F():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x49, 1, lambda_D08F)

    def lambda_D0A9():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x4A, 1, lambda_D0A9)

    def lambda_D0C3():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x4B, 1, lambda_D0C3)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(3100, 900, 0, 500)
    SetCameraDistance(16000, 500)
    Sleep(500)
    EndChrThread(0x49, 0xFF)
    EndChrThread(0x4A, 0xFF)
    EndChrThread(0x4B, 0xFF)
    OP_24(0x3AF)
    OP_24(0x35C)
    OP_24(0x35D)
    Battle("BattleInfo_B70", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x49, 0x80)
    SetChrFlags(0x4A, 0x80)
    SetChrFlags(0x4B, 0x80)
    Call(0, 125)
    Return()

    # Function_59_B788 end

    def Function_60_D143(): pass

    label("Function_60_D143")


    def lambda_D148():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D148)
    Sleep(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1B)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x0)
    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)

    def lambda_D187():
        OP_96(0xFE, 0x4844, 0x0, 0xB54, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D187)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_D1AF():
        OP_98(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D1AF)
    WaitChrThread(0xFE, 1)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_60_D143 end

    def Function_61_D1D4(): pass

    label("Function_61_D1D4")


    def lambda_D1D9():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D1D9)
    SetChrChipByIndex(0xFE, 0x1B)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_D212():
        OP_98(0xFE, 0xFFFFE4A8, 0x0, 0x320, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D212)
    WaitChrThread(0xFE, 1)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_61_D1D4 end

    def Function_62_D237(): pass

    label("Function_62_D237")


    def lambda_D23C():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D23C)
    SetChrChipByIndex(0xFE, 0x7)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D268():
        OP_95(0xFE, 21300, 0, -2500, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D268)
    WaitChrThread(0xFE, 1)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x7)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    BeginChrThread(0x37, 3, 0, 61)
    Sleep(1300)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_D2BE():
        OP_98(0xFE, 0xFFFFE4A8, 0x0, 0x320, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D2BE)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x7)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_62_D237 end

    def Function_63_D2E7(): pass

    label("Function_63_D2E7")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D2F7():
        OP_95(0xFE, 22000, 0, -2400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D2F7)
    WaitChrThread(0xFE, 1)
    Sound(288, 0, 100, 0)

    def lambda_D31B():
        OP_95(0xFE, 24000, 0, -2400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D31B)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x2)

    def lambda_D363():
        OP_9D(0xFE, 0x6E8C, 0x0, 0xFFFFF6A0, 0x514, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D363)
    Sleep(300)
    Sound(540, 0, 100, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(90)
    SetChrSubChip(0xFE, 0x6)
    BeginChrThread(0x27, 3, 0, 64)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x7)
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)
    Sleep(400)
    SetChrSubChip(0xFE, 0x8)

    def lambda_D3BA():
        OP_9D(0xFE, 0x66BC, 0x0, 0xFFFFF7CC, 0x1F4, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D3BA)
    WaitChrThread(0xFE, 1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x9)
    Sound(257, 0, 100, 0)
    PlayEffect(0x0, 0x2, 0xFE, 0x5, 300, 900, 1200, -20, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0xFE, 0x5, 300, 900, 1200, 10, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x31, 0x3)
    BeginChrThread(0x31, 3, 0, 65)
    EndChrThread(0x32, 0x3)
    BeginChrThread(0x32, 3, 0, 67)
    Sleep(2000)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    SetChrSubChip(0xFE, 0xA)
    Sleep(30)
    SetChrSubChip(0xFE, 0xC)
    Sleep(30)
    SetChrSubChip(0xFE, 0xE)
    Sleep(30)
    Sound(538, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    BeginChrThread(0x31, 3, 0, 66)
    BeginChrThread(0x32, 3, 0, 68)
    Sleep(90)
    SetChrSubChip(0xFE, 0x2)
    Sleep(90)
    SetChrSubChip(0xFE, 0x3)
    Sleep(300)
    Return()

    # Function_63_D2E7 end

    def Function_64_D4E9(): pass

    label("Function_64_D4E9")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_D53D():
        OP_93(0xFE, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_D53D)

    def lambda_D54A():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D54A)

    def lambda_D563():
        OP_9D(0xFE, 0x7BD4, 0x0, 0xFFFFF3E4, 0x514, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D563)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_64_D4E9 end

    def Function_65_D589(): pass

    label("Function_65_D589")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D5A6():
        OP_96(0xFE, 0x6DC4, 0x0, 0xFFFFF830, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D5A6)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_65_D589 end

    def Function_66_D5C0(): pass

    label("Function_66_D5C0")

    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_D5FC():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D5FC)

    def lambda_D615():
        OP_9D(0xFE, 0x7C9C, 0x0, 0xFFFFF8F8, 0x384, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D615)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_66_D5C0 end

    def Function_67_D63B(): pass

    label("Function_67_D63B")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D658():
        OP_96(0xFE, 0x6DC4, 0x0, 0xFFFFF4AC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D658)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_67_D63B end

    def Function_68_D672(): pass

    label("Function_68_D672")

    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_D6AE():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D6AE)

    def lambda_D6C7():
        OP_9D(0xFE, 0x7DC8, 0x0, 0xFFFFF254, 0x384, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D6C7)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_68_D672 end

    def Function_69_D6ED(): pass

    label("Function_69_D6ED")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D6FA():
        OP_95(0xFE, 22000, 0, 2400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D6FA)
    WaitChrThread(0xFE, 1)

    def lambda_D718():
        OP_95(0xFE, 24000, 0, 2400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D718)
    WaitChrThread(0xFE, 1)
    Sound(318, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x3)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x2)
    BeginChrThread(0x28, 3, 0, 70)
    Sleep(100)
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    Sound(329, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x3, 1000, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D7A1():
        OP_95(0xFE, 28000, 0, 2400, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D7A1)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x5)
    BeginChrThread(0x26, 3, 0, 71)
    Sleep(300)
    SetChrSubChip(0xFE, 0x3)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_D7DF():
        OP_9D(0xFE, 0x67E8, 0x0, 0x3E8, 0x2BC, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D7DF)
    WaitChrThread(0xFE, 1)

    def lambda_D800():
        OP_9D(0xFE, 0x6400, 0x0, 0x7D0, 0x2BC, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D800)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x0)
    Sleep(550)
    SetChrSubChip(0xFE, 0x6)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    Sound(329, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x3, 1000, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D881():
        OP_95(0xFE, 28600, 0, 2000, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D881)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)

    def lambda_D8AE():
        OP_9D(0xFE, 0x6978, 0x0, 0x7D0, 0x2BC, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D8AE)
    WaitChrThread(0xFE, 1)
    Sound(329, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x3, 1000, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D90C():
        OP_95(0xFE, 30300, 0, 2000, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D90C)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x5)
    Sleep(500)
    Return()

    # Function_69_D6ED end

    def Function_70_D931(): pass

    label("Function_70_D931")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D93E():
        OP_95(0xFE, 28200, 0, 2000, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D93E)
    WaitChrThread(0xFE, 1)
    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D9A0():
        TurnDirection(0xFE, 0xA, 0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_D9A0)

    def lambda_D9AD():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D9AD)

    def lambda_D9C6():
        OP_9D(0xFE, 0x7A44, 0x0, 0xCE4, 0x258, 0x2328)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D9C6)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_70_D931 end

    def Function_71_D9EC(): pass

    label("Function_71_D9EC")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D9F9():
        OP_95(0xFE, 29000, 0, 1400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D9F9)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xD)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)

    def lambda_DA2E():
        OP_95(0xFE, 28000, 0, 2000, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DA2E)
    SetChrSubChip(0xFE, 0x2)
    Sleep(70)
    SetChrSubChip(0xFE, 0x3)
    WaitChrThread(0xFE, 1)
    Sleep(400)
    SetChrSubChip(0xFE, 0x4)
    Sleep(90)
    SetChrChipByIndex(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    TurnDirection(0xFE, 0xA, 500)
    SetChrChipByIndex(0xFE, 0xD)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)

    def lambda_DA86():
        OP_95(0xFE, 26700, 0, 2000, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DA86)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 26500, 1000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_DADF():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DADF)

    def lambda_DAF8():
        OP_96(0xFE, 0x6F54, 0x0, 0x7D0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DAF8)
    WaitChrThread(0xFE, 1)
    Sleep(450)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28300, 1000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0xF)
    SetChrSubChip(0xFE, 0x3)

    def lambda_DB58():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DB58)

    def lambda_DB71():
        OP_96(0xFE, 0x79E0, 0x0, 0x7D0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DB71)
    WaitChrThread(0xFE, 1)
    Sleep(600)
    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_DBD1():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DBD1)

    def lambda_DBEA():
        OP_9D(0xFE, 0x8084, 0x0, 0x7D0, 0x258, 0x2328)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DBEA)
    Sleep(50)
    EndChrThread(0x2E, 0x3)
    BeginChrThread(0x2E, 3, 0, 72)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_71_D9EC end

    def Function_72_DC18(): pass

    label("Function_72_DC18")

    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_DC25():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DC25)

    def lambda_DC3E():
        OP_9D(0xFE, 0x86C4, 0x0, 0xBB8, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DC3E)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_72_DC18 end

    def Function_73_DC5F(): pass

    label("Function_73_DC5F")

    SetChrPos(0x25, 17000, 0, 1800, 90)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x0)

    def lambda_DC7D():
        OP_96(0xFE, 0x6400, 0x0, 0x514, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DC7D)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    BeginChrThread(0x25, 0, 0, 89)
    Return()

    # Function_73_DC5F end

    def Function_74_DCA8(): pass

    label("Function_74_DCA8")

    BeginChrThread(0x17, 3, 0, 75)
    BeginChrThread(0x17, 2, 0, 77)
    Sound(3987, 255, 100, 0)
    Sound(264, 0, 100, 0)
    Sound(833, 0, 70, 0)
    Sleep(1300)
    BeginChrThread(0x17, 3, 0, 75)
    BeginChrThread(0x17, 2, 0, 77)
    Sound(264, 0, 100, 0)
    Sound(833, 0, 70, 0)
    Sleep(1300)
    BeginChrThread(0x17, 3, 0, 76)
    Return()

    # Function_74_DCA8 end

    def Function_75_DCEB(): pass

    label("Function_75_DCEB")

    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x3)
    Sound(859, 0, 100, 0)
    Sound(534, 0, 100, 0)
    Sleep(100)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    Sleep(60)
    Sound(569, 0, 100, 0)
    Sound(540, 0, 70, 0)
    SetChrSubChip(0x17, 0x1)
    Sleep(120)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x2)
    Sleep(60)
    SetChrSubChip(0x17, 0x3)
    Sleep(180)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    Sleep(60)
    SetChrSubChip(0x17, 0x1)
    Sleep(700)
    Return()

    # Function_75_DCEB end

    def Function_76_DD45(): pass

    label("Function_76_DD45")

    Sleep(500)
    BeginChrThread(0x29, 3, 0, 78)

    def lambda_DD53():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DD53)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x2)
    Sleep(270)
    PlayEffect(0x8, 0xFF, 0xFE, 0x0, 0, 0, 0, 93, 0, 90, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x17, 0x3)
    Sleep(1200)

    def lambda_DDB8():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DDB8)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x3)
    Sleep(270)
    PlayEffect(0x8, 0xFF, 0xFE, 0x0, 0, 500, 0, 85, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    Sleep(90)
    SetChrSubChip(0x17, 0x1)
    Sleep(300)
    EndChrThread(0x2F, 0x3)
    BeginChrThread(0x2F, 3, 0, 79)
    Sleep(100)
    EndChrThread(0x30, 0x3)
    BeginChrThread(0x30, 3, 0, 80)
    StopEffect(0x1, 0x0)
    Sleep(1100)

    def lambda_DE45():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DE45)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x2)
    Sleep(270)
    PlayEffect(0x8, 0xFF, 0xFE, 0x0, 0, 0, 0, 95, 0, 90, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x17, 0x3)
    Sleep(1500)
    Return()

    # Function_76_DD45 end

    def Function_77_DEA6(): pass

    label("Function_77_DEA6")

    StopEffect(0x1, 0x0)
    PlayEffect(0x7, 0xFF, 0x17, 0x3, 0, 500, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x78)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28000, 1000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28500, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28000, 1000, -2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(180)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28000, 1500, -3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x78)
    Sleep(30)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28500, 1250, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28000, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(180)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28000, 2000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x78)
    Sleep(30)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28500, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28500, 1000, -2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x1, 0xFF, 0x0, 28000, 0, 0, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(180)
    Return()

    # Function_77_DEA6 end

    def Function_78_E158(): pass

    label("Function_78_E158")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E170():
        OP_96(0xFE, 0x701C, 0x0, 0xFFFFFC7C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E170)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E19B():
        OP_A6(0xFE, 0x0, 0x32, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E19B)

    def lambda_E1B4():
        OP_9D(0xFE, 0x89E4, 0x0, 0xFFFFFBB4, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E1B4)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E1FB():
        OP_96(0xFE, 0x701C, 0x0, 0xFFFFFC7C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E1FB)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E226():
        OP_A6(0xFE, 0x0, 0x32, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E226)

    def lambda_E23F():
        OP_9D(0xFE, 0x89E4, 0x0, 0xFFFFFBB4, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E23F)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_78_E158 end

    def Function_79_E265(): pass

    label("Function_79_E265")

    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E272():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E272)

    def lambda_E28B():
        OP_9C(0xFE, 0x1F4, 0x0, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E28B)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0x16)
    SetChrSubChip(0xFE, 0x3)
    BeginChrThread(0xFE, 3, 0, 101)
    Return()

    # Function_79_E265 end

    def Function_80_E2C4(): pass

    label("Function_80_E2C4")

    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E2D1():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E2D1)

    def lambda_E2EA():
        OP_9C(0xFE, 0x1F4, 0x0, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E2EA)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_80_E2C4 end

    def Function_81_E30B(): pass

    label("Function_81_E30B")

    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 13300, 0, 200, 90)
    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0x17, 0x1E, 0xC8)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x2)
    PlayEffect(0x0, 0x0, 0x17, 0x3, 250, 1200, 500, 45, -45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_E378():
        OP_9D(0xFE, 0x571C, 0x0, 0x0, 0xDAC, 0x514)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_E378)
    Sleep(500)
    Sound(844, 0, 70, 0)
    Sound(255, 0, 50, 0)
    Sound(3987, 255, 100, 0)
    WaitChrThread(0x17, 1)
    SetChrSubChip(0x17, 0x3)
    Sound(532, 0, 100, 0)
    OP_82(0x0, 0x1F4, 0xBB8, 0x1F4)
    StopEffect(0x0, 0x0)
    PlayEffect(0x4, 0xFF, 0x17, 0x3, 0, 0, 2000, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    Sound(332, 0, 100, 0)
    Sound(289, 0, 100, 0)
    Sound(833, 0, 100, 0)
    BeginChrThread(0x26, 3, 0, 109)
    Sleep(50)
    BeginChrThread(0x27, 3, 0, 111)
    BeginChrThread(0x28, 3, 0, 113)
    Sleep(50)
    BeginChrThread(0x29, 3, 0, 115)
    Sleep(700)
    OP_68(27000, 700, 0, 500)
    MoveCamera(55, 17, 0, 500)
    SetCameraDistance(16000, 500)
    Sound(534, 0, 100, 0)
    Sound(540, 0, 100, 0)
    Sound(3992, 255, 100, 0)
    SetChrFlags(0x17, 0x20)

    def lambda_E472():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_E472)
    WaitChrThread(0x17, 1)
    ClearChrFlags(0x17, 0x20)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    PlayEffect(0x6, 0xFF, 0x17, 0x3, 0, 500, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(264, 0, 100, 0)
    Sound(833, 0, 100, 0)
    BeginChrThread(0x26, 3, 0, 110)
    BeginChrThread(0x27, 3, 0, 112)
    BeginChrThread(0x28, 3, 0, 114)
    BeginChrThread(0x29, 3, 0, 116)
    Sleep(60)
    SetChrSubChip(0x17, 0x1)
    Sleep(1000)
    OP_6F(0x79)
    SetChrChip(0x1, 0x17, 0x0, 0x0)
    CancelBlur(0)
    SetChrSubChip(0x17, 0x2)
    Sleep(90)
    SetChrChipByIndex(0x17, 0x5)
    SetChrSubChip(0x17, 0x0)
    Return()

    # Function_81_E30B end

    def Function_82_E539(): pass

    label("Function_82_E539")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E608")
    OP_82(0x32, 0x32, 0xBB8, 0x4B0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 31500, 0, -1700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 30500, 0, -1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 31000, 0, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Jump("Function_82_E539")

    label("loc_E608")

    Return()

    # Function_82_E539 end

    def Function_83_E609(): pass

    label("Function_83_E609")


    def lambda_E60E():
        OP_95(0xFE, 81000, 0, 2200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E60E)

    def lambda_E628():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E628)
    WaitChrThread(0xFE, 1)

    def lambda_E63D():
        OP_95(0xFE, 75000, 0, 0, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E63D)
    WaitChrThread(0xFE, 1)

    def lambda_E65B():
        OP_95(0xFE, 65000, 0, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E65B)
    Sleep(1100)

    def lambda_E678():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E678)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_83_E609 end

    def Function_84_E689(): pass

    label("Function_84_E689")


    def lambda_E68E():
        OP_95(0xFE, 80500, 0, 2200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E68E)

    def lambda_E6A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E6A8)
    WaitChrThread(0xFE, 1)

    def lambda_E6BD():
        OP_95(0xFE, 75000, 0, -300, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E6BD)
    WaitChrThread(0xFE, 1)

    def lambda_E6DB():
        OP_95(0xFE, 65000, 0, -300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E6DB)
    Sleep(1100)

    def lambda_E6F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E6F8)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_84_E689 end

    def Function_85_E709(): pass

    label("Function_85_E709")


    def lambda_E70E():
        OP_95(0xFE, 81500, 0, 2200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E70E)

    def lambda_E728():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E728)
    WaitChrThread(0xFE, 1)

    def lambda_E73D():
        OP_95(0xFE, 75000, 0, 300, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E73D)
    WaitChrThread(0xFE, 1)

    def lambda_E75B():
        OP_95(0xFE, 65000, 0, 300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E75B)
    Sleep(1100)

    def lambda_E778():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E778)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_85_E709 end

    def Function_86_E789(): pass

    label("Function_86_E789")

    SetChrChipByIndex(0x30, 0x15)
    SetChrSubChip(0x30, 0x0)

    def lambda_E796():
        OP_96(0xFE, 0x88B8, 0x0, 0x12C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E796)

    def lambda_E7B0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E7B0)
    WaitChrThread(0xFE, 1)

    def lambda_E7C5():
        OP_96(0xFE, 0x8598, 0x0, 0x1F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E7C5)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x30, 0x16)
    SetChrSubChip(0x30, 0x3)
    BeginChrThread(0x30, 3, 0, 101)
    Return()

    # Function_86_E789 end

    def Function_87_E7ED(): pass

    label("Function_87_E7ED")

    SetChrChipByIndex(0x31, 0x15)
    SetChrSubChip(0x31, 0x0)

    def lambda_E7FA():
        OP_96(0xFE, 0x88B8, 0x0, 0xFFFFFED4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E7FA)

    def lambda_E814():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E814)
    WaitChrThread(0xFE, 1)

    def lambda_E829():
        OP_96(0xFE, 0x8278, 0x0, 0xFFFFFAEC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E829)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x31, 0x16)
    SetChrSubChip(0x31, 0x3)
    BeginChrThread(0x31, 3, 0, 101)
    Return()

    # Function_87_E7ED end

    def Function_88_E851(): pass

    label("Function_88_E851")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E8A6")
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)
    Jump("Function_88_E851")

    label("loc_E8A6")

    Return()

    # Function_88_E851 end

    def Function_89_E8A7(): pass

    label("Function_89_E8A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E917")
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 80, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)
    Jump("Function_89_E8A7")

    label("loc_E917")

    Return()

    # Function_89_E8A7 end

    def Function_90_E918(): pass

    label("Function_90_E918")


    def lambda_E91D():
        OP_96(0xFE, 0x1B58, 0x0, 0xFFFFFF38, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E91D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_90_E918 end

    def Function_91_E937(): pass

    label("Function_91_E937")


    def lambda_E93C():
        OP_96(0xFE, 0x1964, 0x0, 0x2BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E93C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_91_E937 end

    def Function_92_E956(): pass

    label("Function_92_E956")


    def lambda_E95B():
        OP_96(0xFE, 0x1450, 0x0, 0x64, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E95B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_92_E956 end

    def Function_93_E975(): pass

    label("Function_93_E975")


    def lambda_E97A():
        OP_96(0xFE, 0x125C, 0x0, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E97A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_93_E975 end

    def Function_94_E994(): pass

    label("Function_94_E994")


    def lambda_E999():
        OP_96(0xFE, 0x1324, 0x0, 0xFFFFFAEC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E999)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_94_E994 end

    def Function_95_E9B3(): pass

    label("Function_95_E9B3")


    def lambda_E9B8():
        OP_96(0xFE, 0x16A8, 0x0, 0xFFFFF8F8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E9B8)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_95_E9B3 end

    def Function_96_E9D2(): pass

    label("Function_96_E9D2")


    def lambda_E9D7():
        OP_96(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E9D7)

    def lambda_E9F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E9F1)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 3, 0, 99)
    Return()

    # Function_96_E9D2 end

    def Function_97_EA08(): pass

    label("Function_97_EA08")


    def lambda_EA0D():
        OP_96(0xFE, 0xFFFFE9BC, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EA0D)

    def lambda_EA27():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EA27)
    WaitChrThread(0xFE, 1)

    def lambda_EA3C():
        OP_96(0xFE, 0xFFFFF95C, 0x0, 0x514, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EA3C)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 3, 0, 99)
    Return()

    # Function_97_EA08 end

    def Function_98_EA5C(): pass

    label("Function_98_EA5C")


    def lambda_EA61():
        OP_96(0xFE, 0xFFFFE9BC, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EA61)

    def lambda_EA7B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EA7B)
    WaitChrThread(0xFE, 1)

    def lambda_EA90():
        OP_96(0xFE, 0xFFFFF95C, 0x0, 0xFFFFFAEC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EA90)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 3, 0, 99)
    Return()

    # Function_98_EA5C end

    def Function_99_EAB0(): pass

    label("Function_99_EAB0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EACB")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_99_EAB0")

    label("loc_EACB")

    Return()

    # Function_99_EAB0 end

    def Function_100_EACC(): pass

    label("Function_100_EACC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EC62")
    ClearScenarioFlags(0x0, 1)
    SetChrSubChip(0xFE, 0x4)

    def lambda_EAE3():
        OP_A6(0xFE, 0x0, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EAE3)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    SetScenarioFlags(0x0, 1)
    Sleep(500)
    Jump("Function_100_EACC")

    label("loc_EC62")

    Return()

    # Function_100_EACC end

    def Function_101_EC63(): pass

    label("Function_101_EC63")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EDF3")
    SetChrSubChip(0xFE, 0x4)

    def lambda_EC77():
        OP_A6(0xFE, 0x0, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EC77)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(500)
    Jump("Function_101_EC63")

    label("loc_EDF3")

    Return()

    # Function_101_EC63 end

    def Function_102_EDF4(): pass

    label("Function_102_EDF4")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1A)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_EE12():
        OP_9D(0xFE, 0x5654, 0x0, 0x76C, 0x3E8, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EE12)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x87, 0x0)
    Sound(811, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_102_EDF4 end

    def Function_103_EE44(): pass

    label("Function_103_EE44")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_EE5C():
        OP_9D(0xFE, 0x5654, 0x0, 0xFFFFF31C, 0x384, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EE5C)
    WaitChrThread(0xFE, 1)
    Sound(862, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_103_EE44 end

    def Function_104_EE87(): pass

    label("Function_104_EE87")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    Sound(250, 0, 100, 0)

    def lambda_EEA5():
        OP_9D(0xFE, 0x53FC, 0x0, 0xFFFFFCE0, 0x190, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EEA5)
    WaitChrThread(0xFE, 1)

    def lambda_EEC6():
        OP_A6(0xFE, 0x0, 0x32, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EEC6)
    SetChrSubChip(0xFE, 0x2)
    WaitChrThread(0x25, 2)
    Return()

    # Function_104_EE87 end

    def Function_105_EEE3(): pass

    label("Function_105_EEE3")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_EEF0():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EEF0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_105_EEE3 end

    def Function_106_EF0A(): pass

    label("Function_106_EF0A")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_EF17():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0xFFFFFF38, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EF17)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_106_EF0A end

    def Function_107_EF31(): pass

    label("Function_107_EF31")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_EF3E():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0xC8, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EF3E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_107_EF31 end

    def Function_108_EF58(): pass

    label("Function_108_EF58")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_EF65():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EF65)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_108_EF58 end

    def Function_109_EF7F(): pass

    label("Function_109_EF7F")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_EF9D():
        OP_9D(0xFE, 0x6978, 0x0, 0x12C, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EF9D)
    WaitChrThread(0xFE, 1)
    Sound(862, 0, 100, 0)

    def lambda_EFC4():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EFC4)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_109_EF7F end

    def Function_110_EFDD(): pass

    label("Function_110_EFDD")

    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_EFF0():
        OP_9D(0xFE, 0x7530, 0x0, 0x320, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EFF0)
    WaitChrThread(0xFE, 1)
    Sound(811, 0, 100, 0)

    def lambda_F017():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F017)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_110_EFDD end

    def Function_111_F030(): pass

    label("Function_111_F030")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_F048():
        OP_9D(0xFE, 0x6720, 0x0, 0xFFFFF768, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F048)
    WaitChrThread(0xFE, 1)

    def lambda_F069():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F069)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    Return()

    # Function_111_F030 end

    def Function_112_F097(): pass

    label("Function_112_F097")

    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xF)
    SetChrSubChip(0xFE, 0x3)

    def lambda_F0A9():
        TurnDirection(0xFE, 0x17, 500)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_F0A9)

    def lambda_F0B6():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F0B6)

    def lambda_F0CF():
        OP_96(0xFE, 0x72D8, 0x0, 0xFFFFF448, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F0CF)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_112_F097 end

    def Function_113_F0EE(): pass

    label("Function_113_F0EE")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_F106():
        OP_9D(0xFE, 0x6720, 0x0, 0x5DC, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F106)
    WaitChrThread(0xFE, 1)

    def lambda_F127():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F127)
    SetChrSubChip(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    Return()

    # Function_113_F0EE end

    def Function_114_F159(): pass

    label("Function_114_F159")

    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xF)
    SetChrSubChip(0xFE, 0x3)

    def lambda_F16B():
        TurnDirection(0xFE, 0x17, 500)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_F16B)

    def lambda_F178():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F178)

    def lambda_F191():
        OP_96(0xFE, 0x72D8, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F191)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_114_F159 end

    def Function_115_F1B0(): pass

    label("Function_115_F1B0")


    def lambda_F1B5():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F1B5)
    SetChrChipByIndex(0xFE, 0xF)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_115_F1B0 end

    def Function_116_F1D2(): pass

    label("Function_116_F1D2")

    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_F1DF():
        OP_9D(0xFE, 0x7A44, 0x0, 0xFFFFFB50, 0x2BC, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F1DF)
    WaitChrThread(0xFE, 1)

    def lambda_F200():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F200)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_116_F1D2 end

    def Function_117_F219(): pass

    label("Function_117_F219")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)

    def lambda_F231():
        OP_9C(0xFE, 0xFFFFE890, 0x0, 0x0, 0x1F4, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F231)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_117_F219 end

    def Function_118_F256(): pass

    label("Function_118_F256")


    def lambda_F25B():
        OP_96(0xFE, 0x7C9C, 0x0, 0x12C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F25B)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x17, 0xB)
    SetChrSubChip(0x17, 0x0)
    Return()

    # Function_118_F256 end

    def Function_119_F27D(): pass

    label("Function_119_F27D")


    def lambda_F282():
        OP_96(0xFE, 0x76C0, 0x0, 0x76C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F282)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x12)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_119_F27D end

    def Function_120_F2A4(): pass

    label("Function_120_F2A4")


    def lambda_F2A9():
        OP_96(0xFE, 0x76C0, 0x0, 0xFFFFF894, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F2A9)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_120_F2A4 end

    def Function_121_F2CB(): pass

    label("Function_121_F2CB")


    def lambda_F2D0():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFED4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F2D0)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0xD)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_121_F2CB end

    def Function_122_F2F2(): pass

    label("Function_122_F2F2")

    Sleep(1200)

    label("loc_F2F5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F30E")
    Sound(530, 0, 80, 0)
    Sleep(1200)
    Jump("loc_F2F5")

    label("loc_F30E")

    Return()

    # Function_122_F2F2 end

    def Function_123_F30F(): pass

    label("Function_123_F30F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F328")
    Sound(356, 0, 50, 0)
    Sleep(1100)
    Jump("Function_123_F30F")

    label("loc_F328")

    Return()

    # Function_123_F30F end

    def Function_124_F329(): pass

    label("Function_124_F329")

    Sleep(1000)

    label("loc_F32C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F35A")
    Sound(264, 0, 40, 0)
    Sound(833, 0, 30, 0)
    Sleep(1600)
    Sound(264, 0, 40, 0)
    Sound(833, 0, 30, 0)
    Sleep(3000)
    Jump("loc_F32C")

    label("loc_F35A")

    Return()

    # Function_124_F329 end

    def Function_125_F35B(): pass

    label("Function_125_F35B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x5)
    LoadChrToIndex("chr/ch00150.itc", 0x6)
    LoadChrToIndex("chr/ch00250.itc", 0x7)
    LoadChrToIndex("chr/ch00350.itc", 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x9)
    LoadChrToIndex("chr/ch03050.itc", 0xA)
    LoadChrToIndex("chr/ch02450.itc", 0xB)
    LoadChrToIndex("chr/ch02451.itc", 0xC)
    LoadChrToIndex("chr/ch00950.itc", 0xD)
    LoadChrToIndex("chr/ch00951.itc", 0xE)
    LoadChrToIndex("chr/ch00952.itc", 0xF)
    LoadChrToIndex("apl/ch51237.itc", 0x10)
    LoadChrToIndex("apl/ch51265.itc", 0x11)
    LoadChrToIndex("apl/ch51238.itc", 0x12)
    LoadChrToIndex("apl/ch51267.itc", 0x13)
    LoadChrToIndex("chr/ch42250.itc", 0x14)
    LoadChrToIndex("chr/ch42251.itc", 0x15)
    LoadChrToIndex("chr/ch02452.itc", 0x16)
    LoadChrToIndex("chr/ch42253.itc", 0x17)
    LoadChrToIndex("chr/ch42254.itc", 0x18)
    LoadChrToIndex("chr/ch42550.itc", 0x19)
    LoadChrToIndex("chr/ch42551.itc", 0x1A)
    LoadChrToIndex("chr/ch00952.itc", 0x1B)
    LoadChrToIndex("chr/ch42553.itc", 0x1C)
    LoadChrToIndex("chr/ch42554.itc", 0x1D)
    LoadChrToIndex("apl/ch51258.itc", 0x1E)
    LoadChrToIndex("apl/ch51235.itc", 0x1F)
    LoadChrToIndex("chr/ch02400.itc", 0x20)
    LoadChrToIndex("chr/ch00900.itc", 0x21)
    LoadChrToIndex("apl/ch51021.itc", 0x22)
    LoadEffect(0x1, "event/ev12010.eff")
    LoadEffect(0x2, "event/ev12011.eff")
    SoundLoad(938)
    SoundLoad(145)
    SoundLoad(803)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x101, 0x5)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x6)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x7)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x8)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x9)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xA)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, 7000, 0, -200, 270)
    SetChrPos(0x102, 6500, 0, 700, 270)
    SetChrPos(0x103, 5200, 0, 100, 270)
    SetChrPos(0x104, 4700, 0, 1000, 270)
    SetChrPos(0x109, 4900, 0, -1300, 270)
    SetChrPos(0x105, 5800, 0, -1800, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    EndChrThread(0x17, 0xFF)
    SetChrChipByIndex(0x17, 0x16)
    SetChrSubChip(0x17, 0x1)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 26900, 0, 300, 90)
    EndChrThread(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x12)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x2)
    ClearChrFlags(0xA, 0x20)
    SetChrPos(0xA, 25400, 0, 1900, 90)
    EndChrThread(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x10)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x20)
    SetChrPos(0x9, 25400, 0, -1900, 90)
    SetChrChipByIndex(0x25, 0x1B)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 24500, 0, -300, 90)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 9500, 0, 3600, 270)
    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 10500, 0, 3500, 270)
    SetChrChipByIndex(0x26, 0x18)
    SetChrSubChip(0x26, 0x3)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 33500, 0, 0, 270)
    SetChrChipByIndex(0x27, 0x18)
    SetChrSubChip(0x27, 0x3)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 33200, 0, 1700, 270)
    SetChrChipByIndex(0x28, 0x17)
    SetChrSubChip(0x28, 0x3)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 34700, 0, 1300, 270)
    SetChrChipByIndex(0x29, 0x17)
    SetChrSubChip(0x29, 0x3)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, 33700, 0, 3100, 270)
    SetChrChipByIndex(0x2A, 0x17)
    SetChrSubChip(0x2A, 0x2)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrChipByIndex(0x2E, 0x1D)
    SetChrSubChip(0x2E, 0x2)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x8000)
    SetChrPos(0x2E, 34000, 0, -1900, 270)
    SetChrChipByIndex(0x2F, 0x1C)
    SetChrSubChip(0x2F, 0x2)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 34900, 0, -200, 270)
    SetChrChipByIndex(0x30, 0x1C)
    SetChrSubChip(0x30, 0x3)
    ClearChrFlags(0x30, 0x80)
    SetChrFlags(0x30, 0x8000)
    SetChrPos(0x30, 35900, 0, -900, 270)
    SetChrChipByIndex(0x31, 0x1C)
    SetChrSubChip(0x31, 0x2)
    ClearChrFlags(0x31, 0x80)
    SetChrFlags(0x31, 0x8000)
    SetChrPos(0x31, 34000, 0, -3100, 270)
    SetChrChipByIndex(0x32, 0x1D)
    SetChrSubChip(0x32, 0x2)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x32, 0x8000)
    SetChrChipByIndex(0x33, 0x1D)
    SetChrSubChip(0x33, 0x2)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x33, 0x8000)
    ClearMapObjFlags(0x4, 0x10)
    OP_70(0x4, 0xA)
    ClearChrFlags(0x48, 0x80)
    OP_78(0x17, 0x48)
    OP_49()
    SetChrPos(0x48, 34300, 100, -1600, 0)
    OP_D5(0x48, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x17, 0x1000)
    SetMapObjFlags(0x17, 0x4)
    ClearChrFlags(0x47, 0x80)
    OP_78(0x10, 0x47)
    OP_49()
    SetChrPos(0x47, 25500, 0, 0, 0)
    OP_D5(0x47, 0x0, 0x13880, 0x0, 0x0)
    SetMapObjFlags(0x10, 0x1000)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFrame(0xFF, "kokeru00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kokeru01", 0x0, 0x1)
    OP_68(4600, 900, 930, 0)
    MoveCamera(30, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00010F#11PTch, they even had these?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12PProbably from the rooftop inside the tower\x01",
            "I think that it was released.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00301FBut now is \"association\"\x01",
            "Is not it a mon made?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10308FDid you get the flowing in the dark\x01",
            "Or …\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#6P#11508F…… I do not care,\x01",
            "Why do you think that Kerry will be there too?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(29500, 700, 0, 3000)
    MoveCamera(43, 23, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(18500, 3000)

    def lambda_FA1A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_FA1A)

    def lambda_FA27():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FA27)
    Sleep(50)

    def lambda_FA37():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FA37)
    Sleep(50)

    def lambda_FA47():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_FA47)
    Sleep(50)

    def lambda_FA57():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FA57)
    Sleep(50)

    def lambda_FA67():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_FA67)
    Sleep(50)

    def lambda_FA77():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_FA77)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x26,
        "#12PUgh… monsters\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "it can not be helped!\x01",
            "I will switch to the final plan!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x2E, 0x3)
    Sound(809, 0, 100, 0)
    Sleep(200)
    SetChrSubChip(0x2E, 0x4)
    PlayEffect(0x1, 0x0, 0x2E, 0x5, 0, 0, 0, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    BeginChrThread(0x4C, 1, 0, 127)

    ChrTalk(
        0x17,
        "#01401F#7A#5PUhg\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#07105F#8A#5PStun Grenade\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#07307F#5A#5PGet back!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 0x13)
    SetChrSubChip(0xA, 0x2)
    BeginChrThread(0xA, 3, 0, 117)
    Sound(250, 0, 80, 0)
    Sleep(50)
    SetChrChipByIndex(0x9, 0x11)
    SetChrSubChip(0x9, 0x2)
    BeginChrThread(0x9, 3, 0, 117)
    Sound(844, 0, 80, 0)
    Sleep(50)
    SetChrChipByIndex(0x17, 0xC)
    SetChrSubChip(0x17, 0x2)
    BeginChrThread(0x17, 3, 0, 117)
    Sleep(50)
    SetChrChipByIndex(0x25, 0x22)
    SetChrSubChip(0x25, 0x0)
    BeginChrThread(0x25, 3, 0, 117)
    Sleep(200)
    StopEffect(0x0, 0x0)
    PlayEffect(0x2, 0x0, 0xFF, 0x0, 29000, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sound(833, 0, 100, 0)
    Sound(200, 0, 100, 0)
    Sleep(100)
    Sound(174, 0, 100, 0)
    FadeToDark(500, 16777215, -1)
    OP_0D()
    Sleep(2000)
    OP_68(29500, 900, 0, 0)
    MoveCamera(43, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    EndChrThread(0x17, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x25, 0xFF)
    SetChrPos(0x17, 20900, 0, 300, 90)
    SetChrPos(0xA, 19400, 0, 1900, 90)
    SetChrPos(0x9, 19400, 0, -1900, 90)
    SetChrChipByIndex(0x25, 0xE)
    SetChrSubChip(0x25, 0x0)
    SetChrPos(0x25, 18500, 0, -300, 90)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x11, 0x10)
    ClearMapObjFlags(0x11, 0x1000)
    OP_70(0x11, 0x1E)
    OP_74(0x11, 0x3C)
    FadeToBright(2000, 16777215)
    Sound(145, 2, 100, 0)
    OP_71(0x11, 0x3C, 0x0, 0x0, 0x0)
    OP_79(0x11)
    Sound(143, 0, 100, 0)
    OP_24(0x91)
    OP_0D()
    OP_68(33500, 1000, 0, 2500)
    MoveCamera(43, 19, 0, 2500)
    SetCameraDistance(17500, 2500)
    BeginChrThread(0x17, 3, 0, 118)
    Sleep(50)
    BeginChrThread(0xA, 3, 0, 119)
    Sleep(50)
    BeginChrThread(0x9, 3, 0, 120)
    Sleep(50)
    BeginChrThread(0x25, 3, 0, 121)
    WaitChrThread(0x25, 3)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        "#6P#07301FTch…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#07101F#5PThat shutter is\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#01403F#5P…… Apparently easy\x01",
            "I do not seem to be able to break through.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00007F#6P#NEveryone!\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(28000, 1000, 0, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    OP_68(31000, 1000, 0, 3000)
    SetCameraDistance(16500, 3000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, 19500, 0, -300, 90)
    SetChrPos(0x102, 19500, 0, 1000, 90)
    SetChrPos(0x103, 18300, 0, -1700, 90)
    SetChrPos(0x104, 18300, 0, -400, 90)
    SetChrPos(0x109, 17100, 0, -1700, 90)
    SetChrPos(0x105, 17100, 0, -400, 90)
    SetChrPos(0x8, 17300, 0, 2100, 90)
    SetChrPos(0xB, 18400, 0, 2100, 90)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x25, 0x21)
    SetChrSubChip(0x25, 0x0)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x17, 33500, 0, 300, 270)
    SetChrPos(0x25, 31500, 0, 0, 270)
    SetChrPos(0xA, 32400, 0, 1700, 270)
    SetChrPos(0x9, 32600, 0, -1300, 270)

    def lambda_FFED():
        OP_97(0x101, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FFED)
    Sleep(100)

    def lambda_1000A():
        OP_97(0x102, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1000A)
    Sleep(100)

    def lambda_10027():
        OP_97(0x103, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10027)
    Sleep(100)

    def lambda_10044():
        OP_97(0x104, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10044)
    Sleep(100)

    def lambda_10061():
        OP_97(0x109, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10061)
    Sleep(100)

    def lambda_1007E():
        OP_97(0x105, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1007E)
    Sleep(100)

    def lambda_1009B():
        OP_97(0xB, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1009B)
    Sleep(100)

    def lambda_100B8():
        OP_97(0x8, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_100B8)
    WaitChrThread(0xB, 0)

    def lambda_100D6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_100D6)
    WaitChrThread(0x8, 0)

    def lambda_100E7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_100E7)

    ChrTalk(
        0x25,
        "#11P#00600FYou guys\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#6PApparently safe,\x01",
            "You seem to have been able to repulse?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11P#01403FOh, but as it is\x01",
            "It will escape.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#11P#00001F#5PTio, can you do it!?\x02",
    )

    CloseMessageWindow()

    def lambda_101B7():

        label("loc_101B7")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_101B7")

    QueueWorkItem2(0x101, 2, lambda_101B7)

    def lambda_101C9():

        label("loc_101C9")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_101C9")

    QueueWorkItem2(0x102, 2, lambda_101C9)

    def lambda_101DB():

        label("loc_101DB")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_101DB")

    QueueWorkItem2(0x109, 2, lambda_101DB)

    def lambda_101ED():

        label("loc_101ED")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_101ED")

    QueueWorkItem2(0x105, 2, lambda_101ED)

    def lambda_101FF():

        label("loc_101FF")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_101FF")

    QueueWorkItem2(0x104, 2, lambda_101FF)
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#6P#00201FI do not have confidence\x01",
            "I will try just as I do.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10251():
        OP_95(0xFE, 32800, 0, -2700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10251)
    Sleep(300)

    def lambda_1026E():

        label("loc_1026E")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_1026E")

    QueueWorkItem2(0x25, 2, lambda_1026E)
    Sleep(50)

    def lambda_10283():

        label("loc_10283")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_10283")

    QueueWorkItem2(0x17, 2, lambda_10283)
    Sleep(50)

    def lambda_10298():

        label("loc_10298")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_10298")

    QueueWorkItem2(0x9, 2, lambda_10298)
    Sleep(50)

    def lambda_102AD():

        label("loc_102AD")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_102AD")

    QueueWorkItem2(0xA, 2, lambda_102AD)
    WaitChrThread(0x103, 1)

    def lambda_102C3():
        OP_95(0xFE, 34200, 0, -2100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_102C3)
    WaitChrThread(0x103, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x25, 0x2)
    EndChrThread(0x17, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)
    OP_93(0x103, 0x0, 0x1F4)
    Fade(250)
    Sound(802, 0, 100, 0)
    Sound(71, 0, 70, 0)
    ClearMapObjFlags(0x17, 0x4)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    BeginChrThread(0x103, 3, 0, 126)
    Sound(938, 2, 100, 0)
    OP_0D()
    Sleep(2000)
    EndChrThread(0x103, 0x3)
    StopSound(938, 500, 100)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#11P#00206FAgain the security level\x01",
            "It has been raised to the maximum.\x02\x03",
            "#00208FEven if you use \"Aion\"\x01",
            "In this notebook type terminal ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00008FIs that right…\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x25, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_10415():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10415)

    def lambda_10422():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10422)

    def lambda_1042F():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1042F)
    Sleep(50)

    def lambda_1043F():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1043F)

    def lambda_1044C():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1044C)
    Sleep(50)

    def lambda_1045C():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1045C)

    def lambda_10469():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_10469)

    def lambda_10476():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_10476)
    SetChrSubChip(0x103, 0x3)
    Sleep(100)
    SetChrSubChip(0x103, 0x4)
    Sleep(800)
    OP_93(0x25, 0xB4, 0x1F4)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x25, 0x10)
    SetChrFlags(0x25, 0x2)
    SetChrFlags(0x25, 0x20)
    SetChrChipByIndex(0x25, 0x1E)
    SetChrSubChip(0x25, 0x6)
    Sleep(500)
    SetChrSubChip(0x25, 0x7)
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    Sleep(300)

    ChrTalk(
        0x25,
        (
            "#5P#00600FIt's me\x02\x03",
            "#00603FOh, somehow\x01",
            "Surpassing#2RShin#Hanging out … …\x02\x03",
            "…\x02\x03",
            "#00601FHuh!?\x02\x03",
            "They are elevators.\x01",
            "You are descending to the basement … …?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#6P#N#10113FWhy?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00105F#5PBy flying boat on the roof\x01",
            "Are you going to escape …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11503F#5PUgh, I did think of this\x02\x03",
            "#11501FConductive bombs loaded on flying boats\x01",
            "Is it supposed to make a suicide bomber?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_10752():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10752)

    def lambda_1075F():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1075F)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_1079F():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1079F)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_107F7():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_107F7)

    def lambda_10804():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_10804)

    def lambda_10811():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_10811)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_10839():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_10839)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_1085E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1085E)
    OP_63(0x25, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    ClearChrFlags(0x25, 0x10)
    ClearChrFlags(0x25, 0x2)
    ClearChrFlags(0x25, 0x20)
    SetChrChipByIndex(0x25, 0x21)
    SetChrSubChip(0x25, 0x0)
    Sound(802, 0, 100, 0)

    def lambda_108A0():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_108A0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#00007FAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#11P#01401FI see.. In that case\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#07307FThis prestigious official with this building\x01",
            "Is that why they are buried?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12003F#5PCertainly, if they are terrorists\x01",
            "I can do that far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#07101FTch, fools\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10306FThis is bad\x02",
    )

    CloseMessageWindow()
    OP_93(0x25, 0x5A, 0x1F4)

    ChrTalk(
        0x25,
        (
            "#5P#00610FWhen it comes to it\x01",
            "Even brute force this shutter!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    SetChrSubChip(0x103, 0x3)
    Sleep(100)
    SetChrSubChip(0x103, 0x2)

    ChrTalk(
        0x103,
        (
            "#11P#00204F#30WNo…\x02\x03",
            "#00202F#20WApparently somehow\x01",
            "It may become.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10A7C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10A7C)

    def lambda_10A89():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_10A89)

    def lambda_10A96():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_10A96)
    Sleep(50)

    def lambda_10AA6():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_10AA6)

    def lambda_10AB3():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_10AB3)

    def lambda_10AC0():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10AC0)
    Sleep(50)

    def lambda_10AD0():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10AD0)

    def lambda_10ADD():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_10ADD)

    def lambda_10AEA():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_10AEA)
    WaitChrThread(0x25, 2)

    ChrTalk(
        0x25,
        "#5P#00605FWhat?!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7352", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x160), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x91)
    OP_24(0x323)
    OP_24(0x3AA)
    SetScenarioFlags(0x22, 0)
    NewScene("e4820", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_125_F35B end

    def Function_126_10B44(): pass

    label("Function_126_10B44")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10B5E")
    OP_A1(0x103, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_126_10B44")

    label("loc_10B5E")

    Return()

    # Function_126_10B44 end

    def Function_127_10B5F(): pass

    label("Function_127_10B5F")

    Sleep(200)
    Sound(555, 0, 80, 0)
    Sleep(500)
    Sound(555, 0, 60, 0)
    Sleep(200)
    Sound(555, 0, 30, 0)
    Return()

    # Function_127_10B5F end

    def Function_128_10B7B(): pass

    label("Function_128_10B7B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x6)
    LoadChrToIndex("apl/ch51235.itc", 0x7)
    SoundLoad(938)
    SoundLoad(145)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x101, 29500, 0, -300, 90)
    SetChrPos(0x102, 29500, 0, 1000, 90)
    SetChrPos(0x103, 34200, 0, -2100, 0)
    SetChrPos(0x104, 28300, 0, -400, 90)
    SetChrPos(0x109, 27100, 0, -1700, 90)
    SetChrPos(0x105, 27100, 0, -400, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    EndChrThread(0x17, 0xFF)
    SetChrChipByIndex(0x17, 0xB)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 33500, 0, 300, 270)
    EndChrThread(0xA, 0xFF)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 32400, 0, 1700, 270)
    EndChrThread(0x9, 0xFF)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 32600, 0, -1300, 270)
    SetChrChipByIndex(0x25, 0x6)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 31500, 0, 0, 270)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 27300, 0, 2100, 135)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 28400, 0, 2100, 135)
    OP_4B(0xB, 0xFF)

    def lambda_10D03():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10D03)

    def lambda_10D10():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10D10)

    def lambda_10D1D():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_10D1D)

    def lambda_10D2A():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_10D2A)

    def lambda_10D37():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10D37)

    def lambda_10D44():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_10D44)

    def lambda_10D51():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_10D51)

    def lambda_10D5E():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_10D5E)

    def lambda_10D6B():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_10D6B)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x11, 0x10)
    ClearMapObjFlags(0x11, 0x1000)
    OP_70(0x11, 0x0)
    ClearChrFlags(0x48, 0x80)
    OP_78(0x17, 0x48)
    OP_49()
    SetChrPos(0x48, 34300, 100, -1600, 0)
    OP_D5(0x48, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x17, 0x1000)
    ClearChrFlags(0x47, 0x80)
    OP_78(0x10, 0x47)
    OP_49()
    SetChrPos(0x47, 25500, 0, 0, 0)
    OP_D5(0x47, 0x0, 0x13880, 0x0, 0x0)
    SetMapObjFlags(0x10, 0x1000)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFrame(0xFF, "kokeru00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kokeru01", 0x0, 0x1)
    ClearMapObjFlags(0x17, 0x4)
    SetChrChipByIndex(0x103, 0x7)
    SetChrSubChip(0x103, 0x0)
    BeginChrThread(0x103, 3, 0, 126)
    Sound(938, 2, 100, 0)
    OP_68(31000, 1000, 0, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#00002FJonah … ….\x01",
            "Did you come back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202F#11PYeah, apparently on today's flight\x01",
            "You seem to have returned.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1500)
    Sound(839, 0, 100, 0)
    EndChrThread(0x103, 0x3)
    StopSound(938, 500, 100)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#12P#00204F#11P── We did it.\x01",
            "Release the control of the tower.\x02",
        )
    )

    CloseMessageWindow()
    Sound(145, 2, 100, 0)
    OP_71(0x11, 0x0, 0x3C, 0x0, 0x0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_10F72():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10F72)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_10F97():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_10F97)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_10FBF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10FBF)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_10FE4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10FE4)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_1100C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1100C)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_11031():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_11031)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_11059():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_11059)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_1107E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1107E)
    OP_63(0x25, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_110A3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_110A3)
    Sleep(1000)
    OP_79(0x11)
    OP_24(0x91)
    Sound(143, 0, 100, 0)

    ChrTalk(
        0xA,
        "#5P#07102FYou did it!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x25, 0x103, 500)

    ChrTalk(
        0x25,
        "#5P#00602FCan we use the elevator?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetMapObjFlags(0x17, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    TurnDirection(0x103, 0x25, 500)

    ChrTalk(
        0x103,
        (
            "#12P#00202F#11PYes. I've released all locks\x02\x03",
            "#00206FTerrorists are in use\x01",
            "Although one unit can not be used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12004F#5PIn that case I'lll go to the roof\x02\x03",
            "#12000FIt was mounted on an airship\x01",
            "I will release the bombs.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 500)

    ChrTalk(
        0x101,
        "#12P#00005FKillika, can you do that?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12004F#5PYes, for people involved in the anti-piracy\x01",
            "Because it is the minimum skill.\x02\x03",
            "#12000FLector clerk.\x01",
            "Let's say you have to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11504FWell, no helping it\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xB, 500)

    ChrTalk(
        0x9,
        (
            "#11P#07303FWe will accompany you\x02\x03",
            "#07300FThe guards protect the puppet weapons\x01",
            "There seems to be possibility of leaving.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x25, 500)

    def lambda_11327():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11327)

    ChrTalk(
        0xA,
        (
            "#5P#07101F─ ─ How about there,\x01",
            "Pursuing the terrorists!\x02\x03",
            "Somehow now\x01",
            "You may be caught!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x101, 500)

    ChrTalk(
        0x17,
        "#11P#01400FUnderstood\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x25, 0x101, 500)

    ChrTalk(
        0x25,
        (
            "#11P#00601FBannings!\x01",
            "We are going to pursue!\x02\x03",
            "Two enemies ……\x01",
            "I need to organize!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00007FUnderstood!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#6PAye aye sir!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(16000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 1)
    NewScene("c1520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_128_10B7B end

    def Function_129_1147C(): pass

    label("Function_129_1147C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10902.itc", 0x1E)
    LoadChrToIndex("chr/ch11102.itc", 0x1F)
    LoadChrToIndex("chr/ch11002.itc", 0x20)
    LoadChrToIndex("chr/ch11802.itc", 0x21)
    LoadChrToIndex("chr/ch11712.itc", 0x22)
    LoadChrToIndex("chr/ch05600.itc", 0x23)
    LoadChrToIndex("chr/ch05802.itc", 0x24)
    LoadChrToIndex("chr/ch05902.itc", 0x25)
    LoadChrToIndex("chr/ch06000.itc", 0x26)
    LoadChrToIndex("chr/ch47900.itc", 0x27)
    LoadChrToIndex("chr/ch28100.itc", 0x28)
    LoadChrToIndex("apl/ch51259.itc", 0x29)
    LoadChrToIndex("apl/ch50123.itc", 0x2A)
    SetChrPos(0x0, 0, 0, 5500, 0)
    SetChrPos(0x1, 0, 0, 5500, 0)
    SetChrPos(0x2, 0, 0, 5500, 0)
    SetChrPos(0x3, 0, 0, 5500, 0)
    SetChrChipByIndex(0x36, 0x0)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, 8500, 0, 2500, 180)
    SetChrChipByIndex(0x37, 0x0)
    SetChrSubChip(0x37, 0x0)
    ClearChrFlags(0x37, 0x80)
    SetChrFlags(0x37, 0x8000)
    SetChrPos(0x37, 11500, 0, 2500, 180)
    SetChrChipByIndex(0x38, 0x0)
    SetChrSubChip(0x38, 0x0)
    ClearChrFlags(0x38, 0x80)
    SetChrFlags(0x38, 0x8000)
    SetChrFlags(0x38, 0x20)
    SetChrPos(0x38, 33800, 0, -550, 45)
    SetChrChipByIndex(0x39, 0x0)
    SetChrSubChip(0x39, 0x0)
    ClearChrFlags(0x39, 0x80)
    SetChrFlags(0x39, 0x8000)
    SetChrFlags(0x39, 0x20)
    SetChrPos(0x39, 33800, 0, 550, 135)
    SetChrChipByIndex(0x3A, 0x2A)
    SetChrSubChip(0x3A, 0x0)
    ClearChrFlags(0x3A, 0x80)
    SetChrFlags(0x3A, 0x8000)
    SetChrPos(0x3A, -5000, 0, -1000, 90)
    SetChrChipByIndex(0x3B, 0x2A)
    SetChrSubChip(0x3B, 0x0)
    ClearChrFlags(0x3B, 0x80)
    SetChrFlags(0x3B, 0x8000)
    SetChrPos(0x3B, 25000, 0, 1000, 270)
    SetChrChipByIndex(0x3D, 0x26)
    SetChrSubChip(0x3D, 0x0)
    ClearChrFlags(0x3D, 0x80)
    SetChrFlags(0x3D, 0x8000)
    SetChrFlags(0x3D, 0x20)
    SetChrPos(0x3D, 34000, 0, 0, 270)
    BeginChrThread(0x3D, 3, 0, 130)
    SetChrChipByIndex(0x3E, 0x28)
    SetChrSubChip(0x3E, 0x0)
    ClearChrFlags(0x3E, 0x80)
    SetChrFlags(0x3E, 0x8000)
    SetChrPos(0x3E, 34600, 50, -1300, 315)
    SetChrChipByIndex(0x3F, 0x27)
    SetChrSubChip(0x3F, 0x0)
    ClearChrFlags(0x3F, 0x80)
    SetChrFlags(0x3F, 0x8000)
    SetChrPos(0x3F, 35700, 50, 400, 270)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_11(0xFF, 0xC7, 0xBB, 0x12C, 0x384, 0x0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1KSame day, 18:00\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_68(0, 1000, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    PlayBGM("ed7151", 0)
    OP_68(10000, 1000, 0, 10000)
    MoveCamera(60, 13, 0, 10000)

    def lambda_11717():
        OP_96(0xFE, 0x61A8, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_11717)

    def lambda_11731():
        OP_96(0xFE, 0xFFFFEC78, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3B, 1, lambda_11731)
    FadeToBright(1000, 0)
    OP_63(0x38, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(50)
    OP_63(0x39, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(35000, 1000, 0, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    SetCameraDistance(18000, 5000)
    BeginChrThread(0x3D, 0, 0, 131)
    BeginChrThread(0x38, 0, 0, 131)
    BeginChrThread(0x39, 0, 0, 131)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_64(0x36)
    OP_64(0x37)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -46450, 50, 120000, 270)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x2)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -46450, 50, 117100, 270)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x2)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -46450, 50, 114200, 270)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x1)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -57600, 50, 117100, 90)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x1)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -57600, 50, 120000, 90)
    SetChrChipByIndex(0x1D, 0x29)
    SetChrSubChip(0x1D, 0x1)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1D, 0x2)
    SetChrFlags(0x1D, 0x10)
    SetChrPos(0x1D, -54850, 50, 123900, 270)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x2)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -50100, 50, 123900, 180)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -40100, 50, 121250, 270)
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -45100, 0, 115300, 270)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -45100, 0, 118200, 270)
    OP_4B(0xC, 0xFF)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -58800, 0, 120000, 90)
    OP_4B(0xD, 0xFF)
    SetChrChipByIndex(0xD, 0x6)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -44800, 0, 121300, 270)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -44400, 0, 120400, 270)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -58800, 0, 118600, 90)
    OP_4B(0x11, 0xFF)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -59300, 0, 115700, 90)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    OP_70(0x14, 0x46)
    OP_70(0x15, 0x46)
    OP_68(-54240, 2000, 113000, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18860, 0)
    OP_68(-54240, 2000, 117000, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-56210, 2000, 121490, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16170, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x1D,
        (
            "#02803F#11P#30WI see… Understood\x02\x03",
            "#02801F…… This is already safe.\x01",
            "Please rest assured.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1D, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x1D,
        "#02806F#11P#30W….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#11P#02500FWhat about the terrorists?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x1D, 0x2)
    ClearChrFlags(0x1D, 0x10)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    OP_93(0x1D, 0xB4, 0x1F4)
    Fade(500)
    OP_68(-54240, 2000, 116060, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18860, 0)
    OP_0D()

    ChrTalk(
        0x1D,
        (
            "#02803F#5PA group of republics, \"Black Month#4RHayuue#Is called\x01",
            "It seems that they were caught by employees of a trading company.\x02\x03",
            "#02801FEverything Republic Government arrest power of attorney\x01",
            "It was that I had it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#07005F#11P#NHuh!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x22,
        (
            "#6P#07502FOh, it overlaps#4RLantern#!\x02\x03",
            "#07509FThey are our friends.\x01",
            "I will assure you that I am relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12004F#6P#N…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1D,
        (
            "#02806FAnd the group from the Empire…\x02\x03",
            "#02801FUnder the power of attorney by the Imperial Government\x01",
            "To the hunting soldier \"Red constellation\"\x01",
            "It seems that almost all of them were executed.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x23, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x21, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x24, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x21,
        "#6PWhat in the world!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-49800, 2000, 116900, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(13860, 0)
    SetChrSubChip(0x23, 0x0)
    OP_0D()
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x1F,
        (
            "#07207F#11P── The Prime Minister!\x01",
            "What on earth are you going to do !? Is it?\x02\x03",
            "Imperial government under the name of execution etc\x01",
            "You have operated a hunter corps outside the country! Is it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x1)
    Sleep(300)

    ChrTalk(
        0x1E,
        (
            "#5P#07404FYes. To be absoultey certain\x02\x03",
            "#07401FIn any case, the crime aimed at Prince Prince\x01",
            "I can not help being said that he deserves death.\x02\x03",
            "To the fools behind\x01",
            "It will also be a good warning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "#07201FUgh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11508F#11P(He can really talk)\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x24,
        (
            "#02205F#11P#NYes, certainly autonomous state law\x01",
            "I have no choice but to admit ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x23, 0x1)

    ChrTalk(
        0x23,
        (
            "#5P#02507FBut this is \x02\x03",
            "Too much faithful\x01",
            "Is not it a way! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "#6P#07505F#NOh that's a misunderstanding\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-54240, 2000, 116060, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18860, 0)
    SetChrSubChip(0x22, 0x0)

    def lambda_12119():
        TurnDirection(0xFE, 0x22, 0)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_12119)
    SetChrSubChip(0x23, 0x2)
    SetChrSubChip(0x1F, 0x0)
    SetChrSubChip(0x1E, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "#6P#07504FMore people than that#4RObscure#… ….\x01",
            "You proved it without it?\x02\x03",
            "#07502FEven this degree of accident\x01",
            "To the crossbell autonomous state government\x01",
            "That it can not be solved by oneself.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x23, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x21, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x24, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x23,
        "#11P#02501F…!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#11P#07404FHmm, let me list the terrorists\x01",
            "Happiness close to meeting place ……\x02\x03",
            "It escapes indefinitely,\x01",
            "Ultimately by our consideration\x01",
            "Was it able to prevent escape?\x02\x03",
            "#07402FCertainly, the bill of the bill\x01",
            "It's a good example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#6P#07503FYeah, actually rude\x01",
            "For everyone who was aimed at life ……\x02\x03",
            "#07500FThe previous station plan,\x01",
            "I will no longer consider seriously\x01",
            "I wonder if I can not get it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x23, 0x0)
    Sleep(300)

    def lambda_12424():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_12424)
    WaitChrThread(0x23, 2)
    Sleep(500)

    ChrTalk(
        0x23,
        "#5P#02501FY-you both are!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#12PHow high handed…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#07008F#11P#NN-no way, for that purpose…?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1F,
        (
            "#07201F#11P…… to this end a bad mechanism\x01",
            "I do not mean to be prepared …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1D)
    OP_93(0x1D, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1D,
        (
            "#02803F#5P── Everyone.\x01",
            "The debate seems to derail.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrSubChip(0x23, 0x2)
    SetChrSubChip(0x22, 0x1)
    SetChrSubChip(0x1F, 0x2)
    OP_68(-54850, 1300, 122600, 0)
    MoveCamera(63, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_68(-55060, 1300, 123450, 20000)
    MoveCamera(49, 16, 0, 20000)
    OP_6E(500, 20000)
    SetCameraDistance(18000, 20000)
    Sleep(1000)

    ChrTalk(
        0x1D,
        (
            "#02800F#5P#30WHonorable Prime Minister and His Excellency\x01",
            "Despite worth listening to your opinion ……\x02\x03",
            "Before that, I was disturbed by the raid\x01",
            "I would like to resume my remarks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#11P#02505F#30WDieter..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#11P#N#07405F#30WOh\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x22,
        "#12P#N#07505F#30WHmm\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x21,
        "#30WSo what's your proposal\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#5P#02804F#30WNo, not a proposal\x01",
            "Should I call it a commitment to resolve?\x02\x03",
            "I also had some hesitation … …\x01",
            "The determination resolved in this incident.\x02\x03",
            "#02800FNow, borrow this place\x01",
            "I will advocate one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#11P#N#07401F#30W?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x22,
        "#12P#N#07501F#30WWhat?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(500)
    OP_6F(0x79)

    ChrTalk(
        0x1D,
        (
            "#5P#02803F#30WWe no longer want other countries to speculate\x01",
            "I can not be swayed.\x02\x03",
            "#02801FIn the surrounding area, the whole continent\x01",
            "Even for permanent peace and development ─\x02",
        )
    )

    CloseMessageWindow()
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-55060, 1300, 123450, 500)
    MoveCamera(49, 16, 0, 500)
    OP_6E(500, 500)
    SetCameraDistance(16500, 500)
    OP_6F(0x79)
    CancelBlur(0)
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x1D,
        (
            "#5P#02807F#4SI am here to citizens and continental countries,\x01",
            "We advocate \"Cross Bell's national independence\"!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 3000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    Sleep(500)
    SetScenarioFlags(0x22, 0)
    NewScene("m0401", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_129_1147C end

    def Function_130_12960(): pass

    label("Function_130_12960")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12977")
    OP_A0(0xFE, 2500, 0x0, 0xFB)
    Jump("Function_130_12960")

    label("loc_12977")

    Return()

    # Function_130_12960 end

    def Function_131_12978(): pass

    label("Function_131_12978")


    def lambda_1297D():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1297D)
    WaitChrThread(0xFE, 1)
    Sleep(1500)
    OP_63(0x3E, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    def lambda_129B6():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_129B6)
    WaitChrThread(0xFE, 1)
    Sleep(1500)

    def lambda_129D7():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_129D7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_131_12978 end

    def Function_132_129F1(): pass

    label("Function_132_129F1")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12C6E")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The shutter of the elevator\x01",
            "It is tightly closed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00005FBy the way, during the meeting\x01",
            "Apart from the elevator in front\x01",
            "Did not you use it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah, for security reasons\x01",
            "That was supposed to be the case.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_END)), "loc_12B8D")

    ChrTalk(
        0x103,
        (
            "#00200FLike the emergency staircase,\x01",
            "Also here by the power net\x01",
            "It seems to be controlled and managed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh, it seems so.\x02\x03",
            "#00000FWell, when you move\x01",
            "Let's use the front elevator.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C66")

    label("loc_12B8D")


    ChrTalk(
        0x103,
        (
            "#00200FBy the way, opening and closing of the lock\x01",
            "With the power net\x01",
            "It seems to be controlled and managed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh, Kusufusaki is Orkistor's\x01",
            "Security is a place.\x02\x03",
            "#00000FWell, when you move\x01",
            "Let's use the front elevator.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12C66")

    SetScenarioFlags(0x1C2, 2)
    Jump("loc_12CDD")

    label("loc_12C6E")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The shutter of the elevator\x01",
            "It is tightly closed.\x02\x03",
            "During the meeting, this elevator\x01",
            "It seems that it can not be used.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_12CDD")

    TalkEnd(0xFF)
    Return()

    # Function_132_129F1 end

    def Function_133_12CE1(): pass

    label("Function_133_12CE1")

    EventBegin(0x1)
    OP_4B(0x1A, 0xFF)
    TurnDirection(0x1A, 0x0, 500)
    Sleep(500)

    ChrTalk(
        0x1A,
        "We are in the middle of the plenary session.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Take a look at the inside in the corridor room.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 9780, 0, 1430, 180)
    OP_93(0x1A, 0xB4, 0x0)
    OP_4C(0x1A, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_133_12CE1 end

    def Function_134_12D53(): pass

    label("Function_134_12D53")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F…… I can not enter the conference hall.\x02\x03",
            "#00001FLet's get inside without being annoying.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 90250, 0, 76140, 270)
    EventEnd(0x4)
    Return()

    # Function_134_12D53 end

    def Function_135_12DBE(): pass

    label("Function_135_12DBE")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F…… I can not enter the conference hall.\x02\x03",
            "#00001FLet's get inside without being annoying.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 168870, 0, 76540, 90)
    EventEnd(0x4)
    Return()

    # Function_135_12DBE end

    SaveToFile()

Try(main)
