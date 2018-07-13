from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Secretary Lechter",      # 1
        "Major Mueller",          # 2
        "Captain Julia",          # 3
        "Aide Kilika",            # 4
        "Republican Army Officer",# 5
        "Imperial Army Officer",  # 6
        "Republican Army Officer",# 7
        "Imperial Army Officer",  # 8
        "Royal Guard Soldier",    # 9
        "Archduke House Guard",   # 10
        "Archduke House Guard",   # 11
        "Butler",                 # 12
        "Butler",                 # 13
        "Maid",                   # 14
        "Maid",                   # 15
        "Arios",                  # 16
        "City Hall Staffer",      # 17
        "Vice Chief Pierre",      # 18
        "Policeman",              # 19
        "Policeman",              # 20
        "Policeman",              # 21
        "Mayor Dieter",           # 22
        "Chancellor Osborne",     # 23
        "Prince Olivert",         # 24
        "Princess Klaudia",       # 25
        "Archduke Albert",        # 26
        "President Rocksmith",    # 27
        "Chairman MacDowell",     # 28
        "Lawyer Ian",             # 29
        "Detective Dudley",       # 30
        "Imperial Terrorist",     # 31
        "Imperial Terrorist",     # 32
        "Imperial Terrorist",     # 33
        "Imperial Terrorist",     # 34
        "Imperial Terrorist",     # 35
        "Imperial Terrorist",     # 36
        "Imperial Terrorist",     # 37
        "Imperial Terrorist",     # 38
        "Republican Terrorist",   # 39
        "Republican Terrorist",   # 40
        "Republican Terrorist",   # 41
        "Republican Terrorist",   # 42
        "Republican Terrorist",   # 43
        "Republican Terrorist",   # 44
        "Republican Terrorist",   # 45
        "Republican Terrorist",   # 46
        "Policeman",              # 47
        "Policeman",              # 48
        "Policeman",              # 49
        "Policeman",              # 50
        "CGF Member",             # 51
        "CGF Member",             # 52
        "Dummy",                  # 53
        "Grace",                  # 54
        "Reins",                  # 55
        "Reporter",               # 56
        "Reporter",               # 57
        "Reporter",               # 58
        "Reporter",               # 59
        "Reporter",               # 60
        "Airship",                # 61
        "Airship",                # 62
        "椅子",                   # 63
        "椅子",                   # 64
        "Laptop",                 # 65
        "イベント用モンスター",   # 66
        "イベント用モンスター",   # 67
        "イベント用モンスター",   # 68
        "SE制御",                 # 69
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
        "Function_5_15EA",         # 05, 5
        "Function_6_16E8",         # 06, 6
        "Function_7_19E1",         # 07, 7
        "Function_8_1A74",         # 08, 8
        "Function_9_1DAA",         # 09, 9
        "Function_10_1E76",        # 0A, 10
        "Function_11_2240",        # 0B, 11
        "Function_12_2445",        # 0C, 12
        "Function_13_24C5",        # 0D, 13
        "Function_14_256C",        # 0E, 14
        "Function_15_261C",        # 0F, 15
        "Function_16_2705",        # 10, 16
        "Function_17_2723",        # 11, 17
        "Function_18_27CE",        # 12, 18
        "Function_19_2898",        # 13, 19
        "Function_20_2DC2",        # 14, 20
        "Function_21_2E55",        # 15, 21
        "Function_22_2FB7",        # 16, 22
        "Function_23_305C",        # 17, 23
        "Function_24_3157",        # 18, 24
        "Function_25_31F7",        # 19, 25
        "Function_26_3DBB",        # 1A, 26
        "Function_27_45AE",        # 1B, 27
        "Function_28_4D99",        # 1C, 28
        "Function_29_5400",        # 1D, 29
        "Function_30_58E3",        # 1E, 30
        "Function_31_58EA",        # 1F, 31
        "Function_32_5913",        # 20, 32
        "Function_33_6708",        # 21, 33
        "Function_34_679F",        # 22, 34
        "Function_35_67F0",        # 23, 35
        "Function_36_6830",        # 24, 36
        "Function_37_76D6",        # 25, 37
        "Function_38_79A8",        # 26, 38
        "Function_39_7C7A",        # 27, 39
        "Function_40_80C8",        # 28, 40
        "Function_41_8181",        # 29, 41
        "Function_42_9633",        # 2A, 42
        "Function_43_A4A9",        # 2B, 43
        "Function_44_BAC9",        # 2C, 44
        "Function_45_BB96",        # 2D, 45
        "Function_46_BC63",        # 2E, 46
        "Function_47_BCBE",        # 2F, 47
        "Function_48_BD3A",        # 30, 48
        "Function_49_BD98",        # 31, 49
        "Function_50_BE65",        # 32, 50
        "Function_51_BF35",        # 33, 51
        "Function_52_BFAF",        # 34, 52
        "Function_53_C022",        # 35, 53
        "Function_54_C095",        # 36, 54
        "Function_55_C101",        # 37, 55
        "Function_56_C156",        # 38, 56
        "Function_57_C1AB",        # 39, 57
        "Function_58_C21E",        # 3A, 58
        "Function_59_C3A8",        # 3B, 59
        "Function_60_DD8C",        # 3C, 60
        "Function_61_DE1D",        # 3D, 61
        "Function_62_DE80",        # 3E, 62
        "Function_63_DF30",        # 3F, 63
        "Function_64_E132",        # 40, 64
        "Function_65_E1D2",        # 41, 65
        "Function_66_E209",        # 42, 66
        "Function_67_E284",        # 43, 67
        "Function_68_E2BB",        # 44, 68
        "Function_69_E336",        # 45, 69
        "Function_70_E57A",        # 46, 70
        "Function_71_E635",        # 47, 71
        "Function_72_E861",        # 48, 72
        "Function_73_E8A8",        # 49, 73
        "Function_74_E8F1",        # 4A, 74
        "Function_75_E934",        # 4B, 75
        "Function_76_E98E",        # 4C, 76
        "Function_77_EAEF",        # 4D, 77
        "Function_78_EDA1",        # 4E, 78
        "Function_79_EEAE",        # 4F, 79
        "Function_80_EF0D",        # 50, 80
        "Function_81_EF54",        # 51, 81
        "Function_82_F182",        # 52, 82
        "Function_83_F252",        # 53, 83
        "Function_84_F2D2",        # 54, 84
        "Function_85_F352",        # 55, 85
        "Function_86_F3D2",        # 56, 86
        "Function_87_F436",        # 57, 87
        "Function_88_F49A",        # 58, 88
        "Function_89_F4F0",        # 59, 89
        "Function_90_F561",        # 5A, 90
        "Function_91_F580",        # 5B, 91
        "Function_92_F59F",        # 5C, 92
        "Function_93_F5BE",        # 5D, 93
        "Function_94_F5DD",        # 5E, 94
        "Function_95_F5FC",        # 5F, 95
        "Function_96_F61B",        # 60, 96
        "Function_97_F651",        # 61, 97
        "Function_98_F6A5",        # 62, 98
        "Function_99_F6F9",        # 63, 99
        "Function_100_F715",       # 64, 100
        "Function_101_F8AC",       # 65, 101
        "Function_102_FA3D",       # 66, 102
        "Function_103_FA8D",       # 67, 103
        "Function_104_FAD0",       # 68, 104
        "Function_105_FB2C",       # 69, 105
        "Function_106_FB53",       # 6A, 106
        "Function_107_FB7A",       # 6B, 107
        "Function_108_FBA1",       # 6C, 108
        "Function_109_FBC8",       # 6D, 109
        "Function_110_FC26",       # 6E, 110
        "Function_111_FC79",       # 6F, 111
        "Function_112_FCE0",       # 70, 112
        "Function_113_FD37",       # 71, 113
        "Function_114_FDA2",       # 72, 114
        "Function_115_FDF9",       # 73, 115
        "Function_116_FE1B",       # 74, 116
        "Function_117_FE62",       # 75, 117
        "Function_118_FE9F",       # 76, 118
        "Function_119_FEC6",       # 77, 119
        "Function_120_FEED",       # 78, 120
        "Function_121_FF14",       # 79, 121
        "Function_122_FF3B",       # 7A, 122
        "Function_123_FF58",       # 7B, 123
        "Function_124_FF72",       # 7C, 124
        "Function_125_FFA4",       # 7D, 125
        "Function_126_117DF",      # 7E, 126
        "Function_127_117FA",      # 7F, 127
        "Function_128_11816",      # 80, 128
        "Function_129_12170",      # 81, 129
        "Function_130_13845",      # 82, 130
        "Function_131_1385D",      # 83, 131
        "Function_132_138D6",      # 84, 132
        "Function_133_13C1C",      # 85, 133
        "Function_134_13CBF",      # 86, 134
        "Function_135_13D3F",      # 87, 135
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_156A")

    ChrTalk(
        0xFE,
        (
            "Still the second half to go... \x01",
            "I've got to do my best until it's over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E6")

    label("loc_156A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_15E6")

    ChrTalk(
        0xFE,
        "We're just in the middle of the conference right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You can see how it's going from the gallery above.\x02",
    )

    CloseMessageWindow()

    label("loc_15E6")

    TalkEnd(0xFE)
    Return()

    # Function_4_150C end

    def Function_5_15EA(): pass

    label("Function_5_15EA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_1658")

    ChrTalk(
        0xFE,
        (
            "The staff members\x01",
            "are now resetting\x01",
            "the conference room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please feel free to pass.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16E4")

    label("loc_1658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_16E4")

    ChrTalk(
        0xFE,
        (
            "The conference first half is\x01",
            "scheduled to end at 15:00.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It will be a little earlier or\x01",
            "later depending on how things go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E4")

    TalkEnd(0xFE)
    Return()

    # Function_5_15EA end

    def Function_6_16E8(): pass

    label("Function_6_16E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_184F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C1")

    ChrTalk(
        0xFE,
        (
            "No terrorist activity\x01",
            "has been observed yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't think security's so\x01",
            "tight, not even an ant\x01",
            "could break through, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We can't let down our guard until the very end.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_184A")

    label("loc_17C1")


    ChrTalk(
        0xFE,
        (
            "I can't think security's so\x01",
            "tight, not even an ant\x01",
            "could break through, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We can't let down our guard until the very end.\x02",
    )

    CloseMessageWindow()

    label("loc_184A")

    Jump("loc_19DD")

    label("loc_184F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_19DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1938")

    ChrTalk(
        0xFE,
        "The conference has finally started.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can only guess what the\x01",
            "terrorists are after, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, we have to fulfill the roles\x01",
            "we've been given per direction of\x01",
            "the security planning room.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_19DD")

    label("loc_1938")


    ChrTalk(
        0xFE,
        (
            "We can only guess what the\x01",
            "terrorists are after, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, we have to fulfill the roles\x01",
            "we've been given per direction of\x01",
            "the security planning room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19DD")

    TalkEnd(0xFE)
    Return()

    # Function_6_16E8 end

    def Function_7_19E1(): pass

    label("Function_7_19E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F6")
    Call(0, 8)
    Jump("loc_1A70")

    label("loc_19F6")


    ChrTalk(
        0xA,
        (
            "#07103FLeave this area to us. Do your best\x01",
            "with securing the surrounding areas.\x02\x03",
            "#07100FMay the Goddess protect you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A70")

    TalkEnd(0xFE)
    Return()

    # Function_7_19E1 end

    def Function_8_1A74(): pass

    label("Function_8_1A74")

    OP_4B(0x10, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x10, 0x0, 0)
    TurnDirection(0xA, 0x0, 0)

    ChrTalk(
        0x10,
        "Thank you for your hard work, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07102FHm, the Support Section.\x02\x03",
            "It seems you've been securing\x01",
            "the conference floors for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes. We were able to work\x01",
            "our way in here somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, but you've\x01",
            "got all the big\x01",
            "guns in this room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah, almost everyone\x01",
            "is a commissioned officer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes. With the people here alone, you would\x01",
            "be able to deal with a sizable situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FYes, yes, and I heard Captain\x01",
            "Julia's swordsmanship is\x01",
            "both lovely and destructive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#07104FUh uh, that's a bit much.\x02\x03",
            "#07100F...Anyway, no matter who shows up,\x01",
            "I will not allow them to lay a\x01",
            "single finger on Her Highness.\x02\x03",
            "Leave this area to us. Do your best\x01",
            "with securing the surrounding areas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, understood.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0x10, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    SetScenarioFlags(0x1C3, 0)
    Call(0, 31)
    Return()

    # Function_8_1A74 end

    def Function_9_1DAA(): pass

    label("Function_9_1DAA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DBF")
    Call(0, 8)
    Jump("loc_1E72")

    label("loc_1DBF")


    ChrTalk(
        0xFE,
        (
            "We Royal Guard will protect Her Highness,\x01",
            "Princess Klaudia, no matter what happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's no need to worry about the conference\x01",
            "room, so please continue your patrols.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E72")

    TalkEnd(0xFE)
    Return()

    # Function_9_1DAA end

    def Function_10_1E76(): pass

    label("Function_10_1E76")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_217A")

    ChrTalk(
        0x101,
        "#00000FThank you for your hard work, Major Mueller.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FIs anything out of the ordinary?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#07302FOh, you guys.\x02\x03",
            "#07303FHmm. We can't let down our guard,\x01",
            "but things have been calm so far.\x02\x03",
            "The leaders haven't even raised their voices.\x01",
            "I'd say the conference is going smoothly so far.\x02\x03",
            "#07308FIf they keep going at this rate, it'll\x01",
            "be a load off the prince's shoulders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FMajor Mueller...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FIt seems like you have a lot on your mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#07302FHu hu, I guess. You could even\x01",
            "say everything's due to all the\x01",
            "seeds he scattered personally.\x02\x03",
            "#07303FHmm, it seems I've said too much.\x02\x03",
            "Anyway, for now, I need only\x01",
            "do my duty as his escort.\x02\x03",
            "#07300FYou all should serve\x01",
            "in your own way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, understood.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C3, 2)
    Call(0, 31)
    Jump("loc_223C")

    label("loc_217A")


    ChrTalk(
        0x9,
        (
            "#07303FI can only watch over the conference...\x01",
            "I will carry out my duty as an escort until\x01",
            "the end as a military officer would do.\x02\x03",
            "#07300FPlease carry out your own\x01",
            "duties in your own way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_223C")

    TalkEnd(0xFE)
    Return()

    # Function_10_1E76 end

    def Function_11_2240(): pass

    label("Function_11_2240")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2251")
    Jump("loc_2441")

    label("loc_2251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2441")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23BF")

    ChrTalk(
        0xFE,
        (
            "Hmm. You're the Special Support\x01",
            "Section on patrol duty, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Thank you for doing that.\x01",
            "As you can see, there's nothing\x01",
            "out of the ordinary here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you understand, please don't\x01",
            "wander aimlessly around this room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FS-Sure...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F(I feel like he's somehow blunt.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F(Yeah, he's unapproachable.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2441")

    label("loc_23BF")


    ChrTalk(
        0xFE,
        (
            "As you can see, nothing is\x01",
            "out of the ordinary here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you understand, please don't\x01",
            "wander aimlessly around this room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2441")

    TalkEnd(0xFE)
    Return()

    # Function_11_2240 end

    def Function_12_2445(): pass

    label("Function_12_2445")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "...When you make sounds, they\x01",
            "leak into the conference room, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please be as quiet as\x01",
            "possible around here.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_2445 end

    def Function_13_24C5(): pass

    label("Function_13_24C5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "It seems that you've\x01",
            "spoken to Mr. Arios\x01",
            "and the President's aide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems like you know them. Just what kind\x01",
            "of relationship do you have, I wonder.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_24C5 end

    def Function_14_256C(): pass

    label("Function_14_256C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "These are the waiting\x01",
            "rooms for the aides of\x01",
            "the Empire and Kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "―That's right! It means Captain\x01",
            "Julia was here! Just thinking\x01",
            "that could make me scream.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_256C end

    def Function_15_261C(): pass

    label("Function_15_261C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_262D")
    Jump("loc_2701")

    label("loc_262D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2701")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_264C")
    TalkEnd(0xFE)
    Call(0, 25)
    Return()

    label("loc_264C")


    ChrTalk(
        0xB,
        (
            "#12004FThere are things I want to tell\x01",
            "you, but... For now, let's both\x01",
            "watch the proceedings.\x02\x03",
            "#12000FFrom the standpoint of\x01",
            "security, our positions\x01",
            "aren't all that different.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2701")

    TalkEnd(0xFE)
    Return()

    # Function_15_261C end

    def Function_16_2705(): pass

    label("Function_16_2705")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2716")
    Jump("loc_271F")

    label("loc_2716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_271F")

    label("loc_271F")

    TalkEnd(0xFE)
    Return()

    # Function_16_2705 end

    def Function_17_2723(): pass

    label("Function_17_2723")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2734")
    Jump("loc_27CA")

    label("loc_2734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_27CA")

    ChrTalk(
        0xFE,
        (
            "Hmm, so you're the Support\x01",
            "Section on patrol duty, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank you for doing that. Please let\x01",
            "us know if there's anything you need.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27CA")

    TalkEnd(0xFE)
    Return()

    # Function_17_2723 end

    def Function_18_27CE(): pass

    label("Function_18_27CE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "It seems like the conference is going well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Differently from the Republican congress,\x01",
            "I wonder if his excellency the President is feeling\x01",
            "at ease without an obstinate opposition party.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_27CE end

    def Function_19_2898(): pass

    label("Function_19_2898")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2C84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB8")

    ChrTalk(
        0xFE,
        "You're the Special Support Section...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard you assisted his grace\x01",
            "Archduke Albert yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo. On the contrary, it\x01",
            "was he who assisted us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. The Archduke's medical\x01",
            "knowledge really was a big help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha ha. It is true that His Grace\x01",
            "the Archduke is an excellent\x01",
            "doctor in his own right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That aside, His Grace\x01",
            "seemed extremely pleased\x01",
            "with all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I too am glad to meet\x01",
            "you all like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FHa ha, well thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FThank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C3, 3)
    Jump("loc_2C7F")

    label("loc_2AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C0B")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, it\x01",
            "seems there's a possibility\x01",
            "terrorists will appear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's always a possibility at international\x01",
            "conferences like this, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the event it does happen, I don't want the\x01",
            "heads of state to be exposed to any danger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's both give this everything\x01",
            "we have, and do what we must.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2C7F")

    label("loc_2C0B")


    ChrTalk(
        0xFE,
        (
            "We've gotten information\x01",
            "on the terrorists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's both give this everything\x01",
            "we have, and do what we must.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C7F")

    Jump("loc_2DBE")

    label("loc_2C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D4A")

    ChrTalk(
        0xFE,
        (
            "The Special Support Section,\x01",
            "right? Thanks for patrolling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've gotten information\x01",
            "on the terrorists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's both give this everything\x01",
            "we have, and do what we must.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2DBE")

    label("loc_2D4A")


    ChrTalk(
        0xFE,
        (
            "We've gotten information\x01",
            "on the terrorists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's both give this everything\x01",
            "we have, and do what we must.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DBE")

    TalkEnd(0xFE)
    Return()

    # Function_19_2898 end

    def Function_20_2DC2(): pass

    label("Function_20_2DC2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Today's Trade Conference\x01",
            "is being very beneficial for\x01",
            "our Remiferia too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm looking forward to\x01",
            "even more productivity\x01",
            "back home.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_2DC2 end

    def Function_21_2E55(): pass

    label("Function_21_2E55")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2FAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F73")

    ChrTalk(
        0xFE,
        "Hmm, still, what a view.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't tell me that the\x01",
            "terrorists would come flying\x01",
            "through the sky, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "...Ha ha, no way.\x01",
            "As if something like that could happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(...Somehow, he looks afflicted from behind.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2FA5")

    label("loc_2F73")


    ChrTalk(
        0xFE,
        (
            "Ha ha, no way...\x01",
            "Looks like I'm being tired.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FA5")

    Jump("loc_2FB3")

    label("loc_2FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2FB3")

    label("loc_2FB3")

    TalkEnd(0xFE)
    Return()

    # Function_21_2E55 end

    def Function_22_2FB7(): pass

    label("Function_22_2FB7")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Now then, to straighten\x01",
            "up this mic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, when I think about the heads of\x01",
            "state who were all sat here just some\x01",
            "time ago, I get slightly nervous.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_2FB7 end

    def Function_23_305C(): pass

    label("Function_23_305C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_312F")

    ChrTalk(
        0xFE,
        (
            "*sweep, sweep*...\x01",
            "There we go.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0xFE,
        (
            "I have to give everyone a room\x01",
            "they can feel good about for\x01",
            "the conference's second half.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I put all my heart into my cleaning!\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x59, 0x0)
    SetScenarioFlags(0x0, 6)
    Jump("loc_3153")

    label("loc_312F")


    ChrTalk(
        0xFE,
        (
            "*sweep, sweep*...\x01",
            "There we go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3153")

    TalkEnd(0xFE)
    Return()

    # Function_23_305C end

    def Function_24_3157(): pass

    label("Function_24_3157")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The Vice Chief looks so melancholy standing\x01",
            "there. I wonder what happened to him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I won't bother him.\x01",
            "...But, I'm just worried, somehow.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_3157 end

    def Function_25_31F7(): pass

    label("Function_25_31F7")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_END)), "loc_343B")

    ChrTalk(
        0xB,
        (
            "#5P#12000FMy, it's you all.\x01",
            "How are your patrols?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00001FMiss Kilika...\x02",
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
            "By how you look, I guess you have\x01",
            "gotten some new intel again...?\x02\x03",
            "It seems all of you were even \x01",
            "invited to the "Arseille", right?\x02",
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
    Jump("loc_3886")

    label("loc_343B")


    ChrTalk(
        0xB,
        (
            "#5P#12000FYou all... \x01",
            "Uh uh, it's been awhile.\x02\x03",
            "How is the security going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FMiss Kilika...\x02",
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
            "That's right. The situation was\x01",
            "different last time we met. Allow\x01",
            "me to introduce myself once again.\x02\x03",
            "I am Kilika Rouran, aide\x01",
            "to the President of the\x01",
            "Republic of Calvard.\x02\x03",
            "I have other titles too, but...\x01",
            "Well, nothing to speak about.\x02",
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
        "#00003F―I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FSo why did you say you were an\x01",
            "entertainment producer last time, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#12004FUh uh, that is another\x01",
            "of my many titles.\x02\x03",
            "#12002FMy office is in the\x01",
            "Republic, naturally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI see. So you really\x01",
            "weren't lying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302F(Hu hu, a female spy who\x01",
            "properly uses many faces.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309F(Hmm, I love the mysterious\x01",
            "Miss Kilika too, I guess.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106F(That kind of comment isn't\x01",
            "what we need right now, senior...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#12002FUh uh. Is there\x01",
            "something on my face?\x02\x03",
            "#12004FOh yes― \x01",
            "By the way...\x02\x03",
            "#12000FI'm told you all were invited\x01",
            "aboard the "Arseille" yesterday?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3886")

    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#12P#00105FEh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F...Of course you would know that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00306FYeah, you're really well informed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#12004FUh uh, well that itself\x01",
            "is really no big deal.\x02\x03",
            "#12000FSo tell me... Did you hear\x01",
            "anything interesting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYes, but in the end it was just some advice.\x02\x03",
            "#00001FBut there's still plenty\x01",
            "we don't understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#12004FUh uh, is that right.\x02\x03",
            "It's the same for\x01",
            "me too, actually.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#12000FThis is just a hypothetical.\x02\x03",
            "No matter what kind of scenario\x01",
            "I come up with―― It's limited\x01",
            "to what can be realized.\x02\x03",
            "#12003FThere are several conflicting\x01",
            "motives and uncertain factors.\x01",
            "That's true for everyone.\x02\x03",
            "Will things happen starting\x01",
            "now? Or won't they?\x02\x03",
            "#12000FAt this point in time, you could\x01",
            "say that no one knows the answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FThat's certainly true, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10304FUh uh, I guess you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#12004FAnyway, what I want to say is\x01",
            "that there's no doubt that my\x01",
            "role is to protect the President.\x02\x03",
            "In that sense, my position\x01",
            "is the same as yours.\x02\x03",
            "#12000FIn short, let's watch over\x01",
            "the developments together.\x02\x03",
            "Regarding anything else... I'll simply say there's\x01",
            "nothing further I'll discuss at this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FI see... \x01",
            "Thank you for the information.\x02",
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

    # Function_25_31F7 end

    def Function_26_3DBB(): pass

    label("Function_26_3DBB")

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
            "#11P#00005F#12P(Those are... Mr. Arios\x01",
            "and Miss Kilika...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00105F#12P(Looks like it. I wonder\x01",
            "what they're talking about?)\x02",
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
            "#6P#01403F#11P──It's been almost a year\x01",
            "since you left the Guild...\x02\x03",
            "#01400FAre you getting used to your new place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12004F#6P...More or less.\x02\x03",
            "#12000FThough I'm working so hard,\x01",
            "it can't be compared to\x01",
            "when I was at the Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#6P#01403F#11PI see...\x02",
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
            "#12000F#6P...How is\x01",
            "Shizuku?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#6P#01402F#11PHer hearing is a little too good,\x01",
            "and she's always cheerful.\x02\x03",
            "#01404FI recently had a chance to see her...\x01",
            "...She's started to smile often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12004F#6PI see. \x01",
            "That's good, then.\x02\x03",
            "#12003F............\x02\x03",
            "It's been five years already...\x01",
            "Since Mrs. Saya died.\x02\x03",
            "#12000FIt was six years ago that\x01",
            "we first met, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11P#01404FSix years ago... That's right.\x02\x03",
            "At that time, when you were\x01",
            "wandering the continent, you met\x01",
            "Saya by chance in this city...\x02\x03",
            "You didn't want to, but\x01",
            "Saya forced you to stay\x01",
            "with our family, hm?\x02\x03",
            "#01402FI was surprised when I saw\x01",
            "you with the Liberl Guild\x01",
            "three years ago, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12004F#6PUh uh, that's right. It's true\x01",
            "that connections between people\x01",
            "are thought to be mysterious.\x02\x03",
            "#12003F...I will never forget the warmth of\x01",
            "that meal and bed as long as I live.\x02\x03",
            "#12001FIn the end, I couldn't return\x01",
            "the favor directly, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11P#01404F...No. I'm sure the fact\x01",
            "that you think that would be\x01",
            "more than enough for Saya.\x02",
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
            "#00005F#11P(It looks like those two have\x01",
            "been acquainted even before\x01",
            "meeting through the Guild.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12P(Yes. However, I feel\x01",
            "like we shouldn't\x01",
            "listen in any further.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00203F(Indeed. Let's leave\x01",
            "before we bother them.)\x02",
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

    # Function_26_3DBB end

    def Function_27_45AE(): pass

    label("Function_27_45AE")

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
            "#12P#00005F(Those are... Mr. Arios\x01",
            "and Miss Kilika...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105F(Looks like it. I wonder\x01",
            "what they're talking about?)\x02",
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
            "#6P#01403F#11P──It's been almost a year\x01",
            "since you left the Guild...\x02\x03",
            "#01400FAre you getting used to your new place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12004F#6P...More or less.\x02\x03",
            "#12000FThough I'm working so hard,\x01",
            "it can't be compared to\x01",
            "when I was at the Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#6P#01403F#11PI see...\x02",
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
            "#12000F#6P...How is\x01",
            "Shizuku?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#6P#01402F#11PHer hearing is a little too good,\x01",
            "and she's always cheerful.\x02\x03",
            "#01404FI recently had a chance to see her...\x01",
            "...She's started to smile often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12004F#6PI see. \x01",
            "That's good, then.\x02\x03",
            "#12003F............\x02\x03",
            "It's been five years already...\x01",
            "Since Mrs. Saya died.\x02\x03",
            "#12000FIt was six years ago that\x01",
            "we first met, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11P#01404FSix years ago... That's right.\x02\x03",
            "At that time, when you were\x01",
            "wandering the continent, you met\x01",
            "Saya by chance in this city...\x02\x03",
            "You didn't want to, but\x01",
            "Saya forced you to stay\x01",
            "with our family, hm?\x02\x03",
            "#01402FI was surprised when I saw\x01",
            "you with the Liberl Guild\x01",
            "three years ago, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12004F#6PUh uh, that's right. It's true\x01",
            "that connections between people\x01",
            "are thought to be mysterious.\x02\x03",
            "#12003F...I will never forget the warmth of\x01",
            "that meal and bed as long as I live.\x02\x03",
            "#12001FIn the end, I couldn't return\x01",
            "the favor directly, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11P#01404F...No. I'm sure the fact\x01",
            "that you think that would be\x01",
            "more than enough for Saya.\x02",
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
            "#00005F#11P(It looks like those two have\x01",
            "been acquainted even before\x01",
            "meeting through the Guild.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00108F(Yes. However, I feel\x01",
            "like we shouldn't\x01",
            "listen in any further.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203F(Indeed. Let's leave\x01",
            "before we bother them.)\x02",
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

    # Function_27_45AE end

    def Function_28_4D99(): pass

    label("Function_28_4D99")

    EventBegin(0x0)
    Fade(500)
    OP_68(88320, 1500, 84360, 0)
    MoveCamera(38, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    OP_4B(0x17, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5206")

    ChrTalk(
        0x17,
        (
            "#11P#01404FThat's right...\x01",
            "Estelle and Joshua\x01",
            "wanted to see you.\x02\x03",
            "They resented it when they heard Ling\x01",
            "met you during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12004F#6PUh uh, is that right. \x01",
            "I didn't mean to offend.\x02\x03",
            "If I had the time, I too would\x01",
            "have wanted to see them.\x02\x03",
            "#12002FHowever, I did hear about the\x01",
            "achievements of those two in Crossbell.\x02\x03",
            "I've been watching those kids\x01",
            "ever since they were rookies...\x01",
            "I hardly recognize them now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11P#01402FYeah, I too believe those\x01",
            "two were a big help.\x02\x03",
            "#01404FPerhaps I should have expected as much\x01",
            "from Mr. Cassius' kids... I'm looking\x01",
            "forward to what's to come for them.\x02",
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
            "#00001F#11P(Miss Kilika... Come to think\x01",
            "of it, I heard she worked as\x01",
            "a receptionist in Liberl.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#11P(Then, of course\x01",
            "she knows Estelle\x01",
            "and Joshua.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#11P(*giggle*. We don't know where\x01",
            "they met or how they're\x01",
            "connected, though.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x0, 7)
    Jump("loc_53D4")

    label("loc_5206")


    ChrTalk(
        0x17,
        (
            "#11P#01405FBy the way, it looks like you are\x01",
            "staying in contact with Mr. Zin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12004F#6PYes, in a manner of speaking.\x02\x03",
            "#12000FWe each have our own positions, and\x01",
            "rarely get the chance to meet, though.\x02",
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
            "#00003F#11P(We shouldn't eavesdrop any\x01",
            "further. Let's leave quietly.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_53D4")

    SetChrPos(0x0, 87080, 0, 73540, 315)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x17, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_28_4D99 end

    def Function_29_5400(): pass

    label("Function_29_5400")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5860")
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
        "#00005FAh...\x02",
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
            "...Hmm, it looks like\x01",
            "the elevator arrived?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#6POh, well... Please go ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Ah, no, I'd like you\x01",
            "to use it first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I'm in no particular hurry.\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0xD, 500)

    ChrTalk(
        0xC,
        (
            "#6PNo, but I'm the one who\x01",
            "came here after you...\x02",
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
        "#6P#00305FLloyd, what's wrong?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00001FYeah, those two officers\x01",
            "by the elevator...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)
    TurnDirection(0x103, 0x104, 500)

    ChrTalk(
        0x102,
        (
            "#00106FIt seems like they're trying to\x01",
            "compromise on use of the elevator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10108F...I-It looks awkward, somehow.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#6P#10302FHu hu. How bad did both of them have\x01",
            "to hold back for it to get like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...For now, I don't\x01",
            "think we need to\x01",
            "use the elevator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FRight...\x02",
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

    label("loc_5860")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F...It looks like the officers are\x01",
            "still in front of the elevator.\x02\x03",
            "#00003FLet's use the stairs.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 33280, 0, -280, 270)
    EventEnd(0x4)
    Return()

    # Function_29_5400 end

    def Function_30_58E3(): pass

    label("Function_30_58E3")

    Sound(160, 0, 100, 0)
    Return()

    # Function_30_58E3 end

    def Function_31_58EA(): pass

    label("Function_31_58EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5912")
    SetScenarioFlags(0x146, 3)

    label("loc_5912")

    Return()

    # Function_31_58EA end

    def Function_32_5913(): pass

    label("Function_32_5913")

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

    def lambda_5BA3():
        OP_97(0xFE, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_5BA3)

    def lambda_5BBD():
        OP_98(0xFE, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_5BBD)

    def lambda_5BD7():
        OP_97(0x101, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5BD7)
    Sleep(50)

    def lambda_5BF4():
        OP_97(0x102, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5BF4)
    Sleep(50)

    def lambda_5C11():
        OP_97(0x103, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5C11)
    Sleep(50)

    def lambda_5C2E():
        OP_97(0x104, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5C2E)
    Sleep(50)

    def lambda_5C4B():
        OP_97(0x109, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5C4B)
    Sleep(50)

    def lambda_5C68():
        OP_97(0x105, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5C68)
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

    def lambda_5CD5():
        OP_93(0xFE, 0x110, 0x15E)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_5CD5)
    WaitChrThread(0x101, 0)

    def lambda_5CE6():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5CE6)
    Sleep(100)
    WaitChrThread(0x102, 0)

    def lambda_5CFA():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5CFA)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x101,
        "#6P#00001FAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#6PThat is...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_6B(0xFF)
    OP_68(10000, 1000, 3800, 2000)
    MoveCamera(0, 19, 0, 2000)
    SetCameraDistance(20000, 2000)

    def lambda_5D69():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_5D69)
    OP_6F(0x79)

    ChrTalk(
        0x1D,
        (
            "#6P#02804FIn a little while, this will\x01",
            "be a stage upon which true\x01",
            "intentions are revealed...\x02\x03",
            "#02800FIt is the Trade Conference venue.\x02",
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

    def lambda_5EFA():
        OP_97(0x101, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5EFA)
    Sleep(50)

    def lambda_5F17():
        OP_97(0x102, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5F17)
    Sleep(50)

    def lambda_5F34():
        OP_97(0x103, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5F34)
    Sleep(50)

    def lambda_5F51():
        OP_97(0x104, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5F51)
    Sleep(50)

    def lambda_5F6E():
        OP_97(0x109, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5F6E)
    Sleep(50)

    def lambda_5F8B():
        OP_97(0x105, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5F8B)
    Sleep(500)

    def lambda_5FA8():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_5FA8)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00011F#11PThis is...amazing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#11PWhat an amazing view...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#5PFor a ceiling this high, you must've\x01",
            "removed part of two floors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#02804F#11PYes. 36F above has a U-shaped\x01",
            "design to accommodate it.\x02\x03",
            "#02800FBy the way, there are rooms\x01",
            "on both sides for the staffs\x01",
            "of the heads of state.\x02\x03",
            "Their security personnel\x01",
            "will stand by there.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_612E():
        TurnDirection(0x101, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_612E)
    Sleep(50)

    def lambda_613E():
        TurnDirection(0x109, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_613E)
    Sleep(50)

    def lambda_614E():
        TurnDirection(0x102, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_614E)
    Sleep(50)

    def lambda_615E():
        TurnDirection(0x105, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_615E)
    Sleep(50)

    def lambda_616E():
        TurnDirection(0x103, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_616E)
    Sleep(50)

    def lambda_617E():
        TurnDirection(0x104, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_617E)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x109,
        "#10100F#5PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PI guess you do need\x01",
            "rooms for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#02804F#11PNow then, it's time to\x01",
            "show you the last floor.\x02",
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

    def lambda_632A():
        OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_632A)

    def lambda_6344():
        OP_98(0xFE, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_6344)

    def lambda_635E():
        OP_97(0x101, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_635E)
    Sleep(50)

    def lambda_637B():
        OP_97(0x102, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_637B)
    Sleep(50)

    def lambda_6398():
        OP_97(0x103, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6398)
    Sleep(50)

    def lambda_63B5():
        OP_97(0x104, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_63B5)
    Sleep(50)

    def lambda_63D2():
        OP_97(0x109, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_63D2)
    Sleep(50)

    def lambda_63EF():
        OP_97(0x105, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_63EF)
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

    def lambda_6522():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_6522)
    BeginChrThread(0x3C, 3, 0, 35)
    Sleep(100)
    FadeToBright(1000, 0)

    def lambda_654E():
        OP_97(0x101, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_654E)
    Sleep(50)

    def lambda_656B():
        OP_97(0x102, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_656B)
    Sleep(50)

    def lambda_6588():
        OP_97(0x103, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6588)
    Sleep(50)

    def lambda_65A5():
        OP_97(0x104, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_65A5)
    Sleep(50)

    def lambda_65C2():
        OP_97(0x109, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_65C2)
    Sleep(50)

    def lambda_65DF():
        OP_97(0x105, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_65DF)
    Sleep(100)

    def lambda_65FC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_65FC)
    Sleep(50)

    def lambda_6610():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6610)
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

    # Function_32_5913 end

    def Function_33_6708(): pass

    label("Function_33_6708")


    def lambda_670D():
        OP_95(0xFE, -51500, 0, 14000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_670D)
    WaitChrThread(0xFE, 1)

    def lambda_672B():
        OP_95(0xFE, -55500, 0, 14000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_672B)
    WaitChrThread(0xFE, 1)

    def lambda_6749():
        OP_95(0xFE, -55500, 0, 1500, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6749)
    WaitChrThread(0xFE, 1)

    def lambda_6767():
        OP_95(0xFE, -53000, 0, -1000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6767)
    WaitChrThread(0xFE, 1)

    def lambda_6785():
        OP_95(0xFE, -48000, 0, -1000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6785)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_33_6708 end

    def Function_34_679F(): pass

    label("Function_34_679F")


    def lambda_67A4():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_67A4)
    WaitChrThread(0xFE, 1)

    def lambda_67C2():
        OP_95(0xFE, 81000, 0, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_67C2)
    Sleep(700)

    def lambda_67DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_67DF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_34_679F end

    def Function_35_67F0(): pass

    label("Function_35_67F0")


    def lambda_67F5():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_67F5)
    WaitChrThread(0x3C, 1)

    def lambda_6813():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6813)
    WaitChrThread(0xFE, 1)
    OP_6B(0xFF)
    Return()

    # Function_35_67F0 end

    def Function_36_6830(): pass

    label("Function_36_6830")

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
            "#1KSame day, 13:00──\x02",
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
            "#02503F──Well then, I hereby\x01",
            "open the "West Zemuria\x01",
            "Trade Conference".\x02",
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
            "If I may be so bold, I,\x01",
            "Henry MacDowell, will\x01",
            "conduct the proceedings.\x02\x03",
            "The conference is scheduled\x01",
            "for approximately five\x01",
            "hours, including breaks.\x02\x03",
            "However, depending on how\x01",
            "things go, I may entertain\x01",
            "a short extension.\x02\x03",
            "And──Two observers\x01",
            "will participate\x01",
            "in the meeting.\x02",
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
            "#02503F#6P#NLawyer Ian Grimwood.\x02\x03",
            "He practices in Crossbell as\x01",
            "well as the surrounding areas.\x02\x03",
            "#02500FI requested he participate due to his\x01",
            "expertise in international and common law.\x02",
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
            "How do you do.\x01",
            "Ian Grimwood, at your service.\x02",
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
            "#07200F#12P#NOh, so you're the famous\x01",
            ""Mr. Beardy-Bear".\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x21,
        (
            "Hmm, it seems you're primarily\x01",
            "concerned with human rights and such.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(100)

    ChrTalk(
        0x20,
        "#07002F#12P#N*giggle*, nice to meet you.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x24,
        (
            "#5P#02210FHa ha... I will serve with\x01",
            "sincerity and good faith.\x02",
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
            "#6P#02503FBracer Arios MacLaine.\x02\x03",
            "Surely you know him through his great\x01",
            "achievements in neighboring countries.\x02\x03",
            "#02500FI requested he participates from the\x01",
            "neutral standpoint of the Bracer Guild,\x01",
            "to ensure the safety of everyone here.\x02",
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
    SetChrName("Bracer Arios")

    AnonymousTalk(
        0xFF,
        (
            "I am Arios MacLaine. Pleased\x01",
            "to make your acquaintance.\x02",
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
            "#07509F#6P#NHa ha. The "Divine Blade of Wind", right?\x02\x03",
            "#07500FI've heard your name many\x01",
            "times, even in the Republic.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1E,
        (
            "#07404F#11P#12P#NI hear your name from time to time\x01",
            "in the Imperial capital as well.\x02\x03",
            "#07400FThe "Divine Bade" of Crossbell,\x01",
            "clad in wind, they say.\x02",
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
        "Bracer Arios",
        "#01404F...I'm honored.\x02",
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
            "#02503F#5PVery well then. Let's move to\x01",
            "considering each of the proposals.\x02\x03",
            "#02500FThe motioner is Mayor Dieter Crois.\x01",
            "Please explain your proposals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#6P#02804FRight.\x02",
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
            "First of all, regarding the first\x01",
            "proposal in your materials──\x02",
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

    # Function_36_6830 end

    def Function_37_76D6(): pass

    label("Function_37_76D6")

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
            "#11P#00000FAlright... \x01",
            "This completes our patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FIt seems there's nothing\x01",
            "particularly wrong at present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00302FWe should make\x01",
            "another loop around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FTrue...\x02\x03",
            "#00108FI wonder how the\x01",
            "conference is going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FYeah... I'm sure the Mayor and the\x01",
            "Chairman are doing their best, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FThe problem is the "Blood and Iron\x01",
            "Chancellor" and President Rocksmith, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, maybe we should ask someone\x01",
            "about it during the break.\x02",
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

    # Function_37_76D6 end

    def Function_38_79A8(): pass

    label("Function_38_79A8")

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
            "#11P#00000FAlright... \x01",
            "This completes our patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FIt seems there's nothing\x01",
            "particularly wrong at present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00302FWe should make\x01",
            "another loop around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FTrue...\x02\x03",
            "#00108FI wonder how the\x01",
            "conference is going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FYeah... I'm sure the Mayor and the\x01",
            "Chairman are doing their best, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FThe problem is the "Blood and Iron\x01",
            "Chancellor" and President Rocksmith, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, maybe we should ask someone\x01",
            "about it during the break.\x02",
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

    # Function_38_79A8 end

    def Function_39_7C7A(): pass

    label("Function_39_7C7A")

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
            "#1KSame day, 15:05──\x02",
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
            "Finally──the conference was halfway over.\x01",
            "Just before the break, the heads of state\x01",
            "were being interviewed by the press corps.\x07\x00\x02",
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

    # Function_39_7C7A end

    def Function_40_80C8(): pass

    label("Function_40_80C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8180")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_80F6")
    Sleep(500)
    Jump("loc_813E")

    label("loc_80F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_810D")
    Sleep(1000)
    Jump("loc_813E")

    label("loc_810D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8124")
    Sleep(1500)
    Jump("loc_813E")

    label("loc_8124")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_813B")
    Sleep(2000)
    Jump("loc_813E")

    label("loc_813B")

    Sleep(2500)

    label("loc_813E")

    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 80, 0)
    Jump("Function_40_80C8")

    label("loc_8180")

    Return()

    # Function_40_80C8 end

    def Function_41_8181(): pass

    label("Function_41_8181")

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
            "#1KSame day, 16:30──\x02",
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
            "There were disturbing developments\x01",
            "in the conference's second half,\x01",
            "just as Lawyer Ian had predicted.\x02\x03",
            "Both the Empire and Republic raised\x01",
            "harsh questions regarding Crossbell's\x01",
            "security, one after the next.\x02\x03",
            "The faces of Mayor Dieter and Chairman\x01",
            "MacDowell gradually stiffened.\x07\x00\x02",
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
            "#5P#07403F──The problem lies in the fact that public\x01",
            "order was shaken so much by that lone Cult.\x02\x03",
            "#07401FWhat's more, even your public security organization\x01",
            "was controlled by them. It's unprecedented.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1D,
        "#6P#02803F............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x23,
        (
            "#02500F#6P...I thought we covered\x01",
            "those details already.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1E,
        (
            "#5P#07403FThe details aren't the problem. The problem is the\x01",
            ""quality" of your crisis management structure.\x02\x03",
            "#07401FThe fact that the lives and property of visiting \x01",
            "Imperial citizens were threatened during the \x01",
            "incident is the absolute truth.\x02\x03",
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
            "#11P#07203F──One moment please, Chancellor.\x02\x03",
            "#07201FProcedures for damage recovery and reparations\x01",
            "are being performed as we speak.\x02\x03",
            "If we ask for any more mira on top of that, it will\x01",
            "call into question the generosity of the Empire.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x1)
    Sleep(300)

    ChrTalk(
        0x1E,
        (
            "#5P#07400FNo, Your Highness.\x01",
            "That's not the issue.\x02\x03",
            "The problem is... How will the autonomous\x01",
            "state of Crossbell government be able to\x01",
            "guarantee "safety"?\x02\x03",
            "#07403FThe safety of lives and property, and the\x01",
            "safety of faith in trade and financial markets!\x02\x03",
            "#07401FCan you guarantee that, while you're busy\x01",
            "with petty politics, that you won't be taken\x01",
            "advantage of by suspicious fellows?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1F,
        "#11P#07208F...Mrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#4P#NBut, I've heard former Chairman Hartmann \x01",
            "was overthrown, and corruption is being \x01",
            "cleaned up as well.\x02\x03",
            "If going forward, they develop a\x01",
            "security framework under a sound\x01",
            "political system, won't that suffice?\x02",
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
            "#6P#07500F#NNo, no, Your Grace Archduke. \x01",
            "Do you really think it's that easy?\x02\x03",
            "The political climate of Crossbell is\x01",
            "prone to corruption by its very nature.\x02\x03",
            "Mayor Dieter and Chairman MacDowell have\x01",
            "been outstanding statesmen, of course.\x02\x03",
            "But if something were to happen\x01",
            "to them, wouldn't things regress?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0x21, 0x1)
    Sleep(300)

    ChrTalk(
        0x21,
        "#4P#NHmm...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x20,
        (
            "#11P#07003FIt may be overly pessimistic to say so,\x01",
            "but corruption is a part of any government.\x02\x03",
            "#07008FAnd that's valid not only for Crossbell, \x01",
            "but for my country too...\x02\x03",
            "#07001FBecause of that, can't we watch during\x01",
            "the terms of these two persons, and see \x01",
            "if they can create a sound political system?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1E,
        (
            "#5P#07404F...Excuse my rudeness, Your Highness, but you are\x01",
            "young. I understand your desire to believe in hope.\x02\x03",
            "#07403FHowever, Crossbell is not a\x01",
            "traditional monarchy like Liberl.\x02\x03",
            "In places where there is no authority to\x01",
            "serve as a base, governments easily weaken...\x02\x03",
            "#07401FHistory has proven that.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x20,
        "#11P#07005FT-That's...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x22, 0x0)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "#6P#07503F#NHmm, my country does not have a monarch,\x01",
            "but rather an honorable constitution.\x02\x03",
            "#07500FDuring the revolution 100\x01",
            "years ago, various people and\x01",
            "powers gathered to create it.\x02\x03",
            "Therefore, even if my country's politics\x01",
            "were to become corrupt, we could\x01",
            "continue without losing our pride.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x23, 0x2)
    Sleep(300)
    SetChrSubChip(0x1E, 0x0)

    ChrTalk(
        0x23,
        (
            "#02503F#5PYou say that, but we also have an\x01",
            "honorable autonomous state law.\x02\x03",
            "Although it's true that, throughout history,\x01",
            "various imperfections have come to light...\x02\x03",
            "#02500FIt's also true that we have been\x01",
            "improving them, little-by-little.\x02",
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
            "#11P#07400FLawyer Ian. About how many additions\x01",
            "and amendments have there been to\x01",
            "autonomous state law in the past 10 years?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x24,
        (
            "#5P#N#02205FR-Right, I don't have\x01",
            "exact figures, however...\x02\x03",
            "#02203FProbably around fifty.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x22,
        (
            "#6P#07505F#NOnly fifty in 10 years!\x01",
            "That's a bit surprising!\x02\x03",
            "Only five per year!?\x02",
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
            "#5P#02803FNo, it's been increasing\x01",
            "in recent years.\x02\x03",
            "#02801FThere were twelve additions and/or\x01",
            "amendments last year, if I recall.\x02",
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
            "#02505F#5PThough many of the additions were\x01",
            "concerning finance and the orbal net...\x02",
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
            "#11P#07403FIn any case, at that pace, it seems we\x01",
            "cannot expect any meaningful security\x01",
            "framework to be stood up quickly.\x02\x03",
            "#07401FAs I thought. Given the current situation, it\x01",
            "seems we'll need to discuss interim solutions.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x22,
        "#6P#07504F#NYes, I agree.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1E, 0x0)

    ChrTalk(
        0x1F,
        (
            "#11P#07206FMy goodness, I didn't know\x01",
            "you two got along so well.\x02\x03",
            "#07201FCan you two immediately agree on the question\x01",
            "of possession of the Nord Highlands too?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x22,
        "#6P#07509F#NHa ha, I suppose you have a point.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1E,
        (
            "#5P#07404FWell, we'll have another\x01",
            "opportunity to discuss that issue.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x20,
        "#11P#07008F............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x21,
        (
            "#4P#NHmm, time is short. \x01",
            "We should move on other arguments.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x23,
        (
            "#02503F#5P...Understood. Then, as the\x01",
            "Chancellor has motioned──\x02",
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

    # Function_41_8181 end

    def Function_42_9633(): pass

    label("Function_42_9633")

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
            "#02501F#5PChancellor... \x01",
            "What did you just say!?\x02\x03",
            "I'm terribly sorry, but I'd\x01",
            "like you to repeat that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#07404F#11PHu hu, as many times as you like.\x02\x03",
            "#07401F──Disband Crossbell's Guardian Force.\x02\x03",
            "And station other countries'\x01",
            "security forces in Crossbell...\x02\x03",
            "That is the the most realistic option.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#02501F#5P...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#6P#02801F#N............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x20,
        (
            "#5P#07007F#11P#NP-Please, wait a minute!\x02\x03",
            "Chancellor, are you forgetting the\x01",
            "terms on the Non-Aggression Pact?\x02",
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
            "#5P#07405FWe agreed not to use force to\x01",
            "solve disputes in Crossbell.\x02\x03",
            "#07404FHowever, this is not\x01",
            "an invasion at all.\x02\x03",
            "#07402F──I am merely saying the useless\x01",
            "pseudo-military that caused citizens\x01",
            "to live in fear should be disbanded.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x20,
        "#5P#11P#N#07005F!!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1E, 0x0)
    Sleep(300)

    ChrTalk(
        0x1E,
        (
            "#11P#07404FIn practice, before the Imperial Army, or even\x01",
            "the Republican Army, the Crossbell Guardian\x01",
            "Force might as well not even exist.\x02\x03",
            "In front of tanks, their high-power armored\x01",
            "vehicles are nothing more than scraps of paper.\x02\x03",
            "#07400FBecause of the organization's high maintenance \x01",
            "costs, Crossbell's security can be left to other \x01",
            "countries' military forces──\x02\x03",
            "#07402FThat is the best and most efficient solution\x01",
            "for a mere "autonomous state".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x21,
        (
            "#11P...I think that's a\x01",
            "too violent option.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1F,
        (
            "#11P#07203FHow will you designate the\x01",
            ""other countries' military forces"?\x02\x03",
            "#07200FYou're not suggesting\x01",
            "it would be the\x01",
            "Imperial Army, are you?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1E,
        (
            "#11P#07404FHa ha, of course not.\x02\x03",
            "#07402F──However, if necessary, I'm willing\x01",
            "to forgive past transgressions and\x01",
            "offer the Imperial Army's assistance.\x02\x03",
            "That's for both the peace of West Zemuria\x01",
            "and the development of relations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#02501F#5PUgh...\x02",
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
            "#6P#07506F...Now, now, everyone. There's\x01",
            "no need to get so worked up.\x02\x03",
            "#07501FI too feel the Chancellor's\x01",
            "proposal is a bit overbearing.\x02\x03",
            "#07504F──But I also agree that the Guardian\x01",
            "Force is half baked and wholly\x01",
            "inadequate for public order security.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x0)
    Sleep(200)

    def lambda_A018():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_A018)
    SetChrSubChip(0x21, 0x1)
    Sleep(50)
    SetChrSubChip(0x1F, 0x0)
    Sleep(50)
    SetChrSubChip(0x1D, 0x2)
    Sleep(50)

    ChrTalk(
        0x1E,
        "#5P#07405FHm, what would you do, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#6P#07502FThis is just a suggestion, but I propose a\x01",
            "large reduction in Guardian Force troop levels.\x02\x03",
            "Instead, the Republic will assume\x01",
            "responsibility for Bellguard Gate, and the\x01",
            "Empire will do the same for Tangram Gate.\x02\x03",
            "If we do that, we'll be able to quickly respond\x01",
            "to emergencies even here in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#5P#02801F...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#11PMr. President, that's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#5P#07404FHmm, it's worth considering.\x02\x03",
            "#07400FAs expected from you, Mr. President.\x01",
            "You handle many opposition parties all\x01",
            "while running your government. And\x01",
            "you're a fine statesman on top of that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#6P#07509FNo, no, I can't compare to you, Chancellor. \x01",
            "You have a country to reform, all while \x01",
            "holding  back influence of those nobles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#11P#07008FA-All of you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#11P#07203FCease this horseplay. This is not a\x01",
            "conference of only two countries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#5P#07405FOh, excuse my rudeness.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x2)
    Sleep(300)

    ChrTalk(
        0x1E,
        (
            "#11P#07404FIn any case, let's continue\x01",
            "to hear the arguments.\x02\x03",
            "#07402FMay we have your opinions?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A43F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_A43F)
    Sleep(100)
    SetChrSubChip(0x1D, 0x0)
    Sleep(250)

    ChrTalk(
        0x23,
        "#02501F#6P...Ugh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#6P#02803F............\x02",
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

    # Function_42_9633 end

    def Function_43_A4A9(): pass

    label("Function_43_A4A9")

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
            "#5P#02803FNow, regarding the arguments\x01",
            "over the security measures...\x02\x03",
            "#02800FI would like to offer\x01",
            "my own suggestion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#11P#07405FOh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#6P#07509FHa ha ha, I thought you\x01",
            "were being awfully quiet...\x02\x03",
            "#07502FSo you were planning on speaking up, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#5P#02800FYes, you see──\x02",
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
        "Bracer Arios",
        "#01407F#4051V#6P#4S#15A──Everyone, get back!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)

    def lambda_A9A4():
        OP_93(0xFE, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_A9A4)
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

    def lambda_AA3F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_AA3F)
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
        "#02507F#12P#NWha──!?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x20,
        "#07005F#12P#NAirships...!?\x02",
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
        "Ugh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#07207FIt can't be...\x01",
            "Terrorists!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#07401F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "#07505F#5PThey came here, huh...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#02807F#11PDon't worry! It's special\x01",
            "tempered glass that can\x01",
            "withstand even explosions!\x02\x03",
            "But just in case, please\x01",
            "everyone, back away!\x02",
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
        "#07107F#11PYour Highness, are you safe!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#6P#07008FYes, somehow...!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 3)
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#07301FJust now... That was a high-\x01",
            "speed Reinford model airship.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x0, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x1F,
        "#12P#07201FYeah, no doubt about it.\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x0, 0x1F4)
    Sleep(150)

    ChrTalk(
        0xB,
        (
            "#12P#N#12001FThe other one was a Verne\x01",
            "Corp. military gunship.\x02",
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
            "Yes, there was a report\x01",
            "that one was stolen...\x02",
        )
    )

    CloseMessageWindow()
    Sound(121, 0, 100, 0)
    Sound(811, 0, 50, 0)
    ClearChrFlags(0x25, 0x80)

    def lambda_B44B():
        OP_96(0xFE, 0xFFFF34E0, 0x0, 0x19258, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_B44B)

    def lambda_B465():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_B465)
    WaitChrThread(0x25, 1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x25,
        "#12P#00607F#3457V#30WEveryone, are you safe!?\x02",
    )

    CloseMessageWindow()
    OP_24(0xD81)
    OP_C9(0x1, 0x80000000)

    def lambda_B4CD():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_B4CD)

    def lambda_B4DA():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_B4DA)
    Sleep(50)

    def lambda_B4EA():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_B4EA)

    def lambda_B4F7():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_B4F7)

    def lambda_B504():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_B504)
    Sleep(50)

    def lambda_B514():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_B514)

    def lambda_B521():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B521)
    Sleep(50)

    def lambda_B531():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_B531)

    def lambda_B53E():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B53E)

    ChrTalk(
        0x23,
        "#02501F#5PYes, somehow...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#02801F#5PBut where did they go?\x02",
    )

    CloseMessageWindow()
    Sound(867, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(60, 0, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Hmm. It seems\x01",
            "you can hear me.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-52000, 1100, 106600, 1000)
    SetCameraDistance(18000, 1000)

    def lambda_B5F0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_B5F0)

    def lambda_B5FD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_B5FD)
    Sleep(50)

    def lambda_B60D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_B60D)

    def lambda_B61A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_B61A)

    def lambda_B627():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_B627)
    Sleep(50)

    def lambda_B637():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_B637)

    def lambda_B644():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B644)

    def lambda_B651():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B651)

    def lambda_B65E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_B65E)
    Sleep(50)

    def lambda_B66E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_B66E)

    def lambda_B67B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B67B)

    def lambda_B688():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_B688)

    def lambda_B695():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_B695)
    OP_6F(0x79)
    SetMessageWindowPos(60, 0, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "──Meeting attendees. We're the\x01",
            ""Imperial Liberation Front".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(10, 60, -1, -1)
    SetChrName("Youth's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "──Likewise, we're a faction of the \x01",
            ""Anti-Immigration Policy League", seeking\x01",
            "to protect the ancient traditions of Calvard.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x21,
        "#12PWhat...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#12P#02205FThe two terrorist groups active\x01",
            "in the Empire and Republic!?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(60, 0, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "We've agreed to\x01",
            "cooperate to destroy\x01",
            "our respective enemies.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "──"Blood and Iron Chancellor", \x01",
            "Giliath Osborne! Prepare yourself!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(10, 60, -1, -1)
    SetChrName("Youth's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "President Rocksmith!\x01",
            "Your end is here!\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "To protect the traditions of Calvard which\x01",
            "were violated by the abominable Easterners,\x01",
            "drastic measures are needed!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x22,
        "#6P#07506F...How foolish.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#07403F#12PHmm, nonsense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#N#11508FHowever... \x01",
            "This situation looks bad.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x17,
        "Bracer Arios",
        "#11P#01401FYeah── Here they come.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        "#12P#00610FUgh...!\x02",
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

    # Function_43_A4A9 end

    def Function_44_BAC9(): pass

    label("Function_44_BAC9")


    def lambda_BACE():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BACE)
    Sleep(1500)

    def lambda_BAEB():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BAEB)
    Sleep(300)

    def lambda_BB08():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BB08)
    Sleep(300)

    def lambda_BB25():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BB25)
    Sleep(300)

    def lambda_BB42():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BB42)
    Sleep(300)

    def lambda_BB5F():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BB5F)
    Sleep(300)

    def lambda_BB7C():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BB7C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_44_BAC9 end

    def Function_45_BB96(): pass

    label("Function_45_BB96")


    def lambda_BB9B():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BB9B)
    Sleep(1500)

    def lambda_BBB8():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BBB8)
    Sleep(300)

    def lambda_BBD5():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BBD5)
    Sleep(300)

    def lambda_BBF2():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BBF2)
    Sleep(300)

    def lambda_BC0F():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BC0F)
    Sleep(300)

    def lambda_BC2C():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BC2C)
    Sleep(300)

    def lambda_BC49():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BC49)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_45_BB96 end

    def Function_46_BC63(): pass

    label("Function_46_BC63")


    def lambda_BC68():
        OP_95(0xFE, -56700, 0, 123900, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_BC68)
    WaitChrThread(0x1D, 1)

    def lambda_BC86():
        OP_95(0xFE, -59000, 0, 120600, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_BC86)
    WaitChrThread(0x1D, 1)

    def lambda_BCA4():
        OP_95(0xFE, -59000, 0, 118600, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_BCA4)
    WaitChrThread(0x1D, 1)
    Return()

    # Function_46_BC63 end

    def Function_47_BCBE(): pass

    label("Function_47_BCBE")


    def lambda_BCC3():
        OP_95(0xFE, -48000, 0, 124600, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_BCC3)
    WaitChrThread(0x17, 1)
    Sleep(500)

    def lambda_BCE4():
        OP_97(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_BCE4)
    WaitChrThread(0x17, 1)

    def lambda_BD02():
        OP_97(0xFE, 0x7D0, 0x0, 0xFFFFF830, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_BD02)
    WaitChrThread(0x17, 1)

    def lambda_BD20():
        OP_97(0xFE, 0x7D0, 0x0, 0xFFFFEC78, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_BD20)
    WaitChrThread(0x17, 1)
    Return()

    # Function_47_BCBE end

    def Function_48_BD3A(): pass

    label("Function_48_BD3A")

    Sleep(1000)

    def lambda_BD42():
        OP_97(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_BD42)
    WaitChrThread(0x23, 1)

    def lambda_BD60():
        OP_97(0xFE, 0x7D0, 0x0, 0xFFFFF830, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_BD60)
    WaitChrThread(0x23, 1)

    def lambda_BD7E():
        OP_97(0xFE, 0x7D0, 0x0, 0xFFFFEC78, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_BD7E)
    WaitChrThread(0x23, 1)
    Return()

    # Function_48_BD3A end

    def Function_49_BD98(): pass

    label("Function_49_BD98")


    def lambda_BD9D():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BD9D)
    Sleep(300)

    def lambda_BDBA():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BDBA)
    Sleep(300)

    def lambda_BDD7():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BDD7)
    Sleep(300)

    def lambda_BDF4():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BDF4)
    Sleep(300)

    def lambda_BE11():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BE11)
    Sleep(300)

    def lambda_BE2E():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BE2E)
    Sleep(300)

    def lambda_BE4B():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BE4B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_49_BD98 end

    def Function_50_BE65(): pass

    label("Function_50_BE65")

    Sleep(400)

    def lambda_BE6D():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BE6D)
    Sleep(300)

    def lambda_BE8A():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BE8A)
    Sleep(300)

    def lambda_BEA7():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BEA7)
    Sleep(300)

    def lambda_BEC4():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BEC4)
    Sleep(300)

    def lambda_BEE1():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BEE1)
    Sleep(300)

    def lambda_BEFE():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BEFE)
    Sleep(300)

    def lambda_BF1B():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BF1B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_50_BE65 end

    def Function_51_BF35(): pass

    label("Function_51_BF35")


    def lambda_BF3A():
        OP_95(0xFE, -39800, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BF3A)

    def lambda_BF54():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BF54)
    WaitChrThread(0xFE, 1)

    def lambda_BF69():
        OP_95(0xFE, -42500, 0, 108000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BF69)
    WaitChrThread(0xFE, 1)

    def lambda_BF87():
        OP_95(0xFE, -48800, 0, 104500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BF87)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xA, 0x20, 500)
    TurnDirection(0x20, 0xA, 500)
    Return()

    # Function_51_BF35 end

    def Function_52_BFAF(): pass

    label("Function_52_BFAF")


    def lambda_BFB4():
        OP_95(0xFE, -39800, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BFB4)

    def lambda_BFCE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BFCE)
    WaitChrThread(0xFE, 1)

    def lambda_BFE3():
        OP_95(0xFE, -42500, 0, 108000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BFE3)
    WaitChrThread(0xFE, 1)

    def lambda_C001():
        OP_95(0xFE, -48000, 0, 106500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C001)
    WaitChrThread(0xFE, 1)
    TurnDirection(0x1F, 0x9, 500)
    Return()

    # Function_52_BFAF end

    def Function_53_C022(): pass

    label("Function_53_C022")


    def lambda_C027():
        OP_95(0xFE, -39800, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C027)

    def lambda_C041():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C041)
    WaitChrThread(0xFE, 1)

    def lambda_C056():
        OP_95(0xFE, -42500, 0, 108000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C056)
    WaitChrThread(0xFE, 1)

    def lambda_C074():
        OP_95(0xFE, -49200, 0, 108000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C074)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x1E, 500)
    Return()

    # Function_53_C022 end

    def Function_54_C095(): pass

    label("Function_54_C095")


    def lambda_C09A():
        OP_95(0xFE, -39800, 0, 110200, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C09A)

    def lambda_C0B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C0B4)
    WaitChrThread(0xFE, 1)

    def lambda_C0C9():
        OP_95(0xFE, -42500, 0, 108000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C0C9)
    WaitChrThread(0xFE, 1)

    def lambda_C0E7():
        OP_95(0xFE, -48000, 0, 108000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C0E7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_54_C095 end

    def Function_55_C101(): pass

    label("Function_55_C101")


    def lambda_C106():
        OP_95(0xFE, -64400, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C106)

    def lambda_C120():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C120)
    WaitChrThread(0xFE, 1)

    def lambda_C135():
        OP_95(0xFE, -55900, 0, 104400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C135)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x22, 500)
    Return()

    # Function_55_C101 end

    def Function_56_C156(): pass

    label("Function_56_C156")


    def lambda_C15B():
        OP_95(0xFE, -64400, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C15B)

    def lambda_C175():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C175)
    WaitChrThread(0xFE, 1)

    def lambda_C18A():
        OP_95(0xFE, -55600, 0, 106300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C18A)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x22, 500)
    Return()

    # Function_56_C156 end

    def Function_57_C1AB(): pass

    label("Function_57_C1AB")

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

    # Function_57_C1AB end

    def Function_58_C21E(): pass

    label("Function_58_C21E")

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
            "#00607F#11P──They're coming here directly!?\x01\x02\x03",
            "#00606FUgh, so that's what those blueprints were for.\x02\x03",
            "#00610FAnyway, have the Guardian Force\x01",
            "that's on standby hurry here──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetCameraDistance(15000, 300)
    OP_82(0xC8, 0xC8, 0xBB8, 0x12C)

    ChrTalk(
        0x25,
        "#00607F#4S#11PWhat!?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_58_C21E end

    def Function_59_C3A8(): pass

    label("Function_59_C3A8")

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
        "#13AUwaaah!\x02",
    )

    Sleep(50)

    ChrTalk(
        0x37,
        "#5P#13AGyah!\x02",
    )

    Sleep(50)

    ChrTalk(
        0x25,
        "#6P#00610F#13AUgh...!\x02",
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

    def lambda_CFD1():
        OP_95(0xFE, 29700, 0, -300, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_CFD1)

    def lambda_CFEB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_CFEB)
    Sleep(100)
    SetChrChipByIndex(0x27, 0xC)
    SetChrSubChip(0x27, 0x0)

    def lambda_D007():
        OP_95(0xFE, 30900, 0, -1000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_D007)

    def lambda_D021():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_D021)
    Sleep(100)
    SetChrChipByIndex(0x28, 0xC)
    SetChrSubChip(0x28, 0x0)

    def lambda_D03D():
        OP_95(0xFE, 30900, 0, 0, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_D03D)

    def lambda_D057():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_D057)
    Sleep(100)
    SetChrChipByIndex(0x29, 0xC)
    SetChrSubChip(0x29, 0x0)

    def lambda_D073():
        OP_95(0xFE, 32200, 0, -650, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_D073)

    def lambda_D08D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_D08D)
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
        "#11P#4SNow...!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x27,
        "#11P#4STarget the Chancellor!\x02",
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
        "#01401F#5P──You shall not pass.\x02",
    )

    CloseMessageWindow()

    def lambda_D1C6():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_D1C6)
    Sleep(500)

    def lambda_D1E2():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_D1E2)
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
        "#11PGuh, the "Divine Blade of Wind"?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#11PStand firm!\x01",
            "Attack in waves!\x02",
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

    def lambda_D2E7():
        OP_95(0xFE, 19400, 0, 1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D2E7)
    Sleep(200)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)

    def lambda_D30C():
        OP_95(0xFE, 18900, 0, -300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D30C)
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
        "#07107F#5P──We'll cover you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#07307F#5PYou guys fall back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        "#00610F#6P#NWe're in your debt!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x25, 3, 0, 62)
    Sleep(300)
    BeginChrThread(0x36, 3, 0, 60)

    ChrTalk(
        0x26,
        "#12PMueller Vander!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        "#12PThe guardian of the Arnor family!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        "#11PAnd the Liberl Royal Guard...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        "#11PWho cares, let's get them!\x02",
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
        "#00011FAmazing...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FInsane...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#5PBut if it's them, then somehow...\x02",
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

    def lambda_D853():
        OP_96(0xFE, 0x251C, 0x0, 0xE10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D853)

    def lambda_D86D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_D86D)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xE1, 0x1F4)

    def lambda_D889():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D889)
    Sleep(50)

    def lambda_D899():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D899)
    Sleep(50)

    def lambda_D8A9():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D8A9)
    Sleep(50)

    def lambda_D8B9():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D8B9)
    Sleep(50)

    def lambda_D8C9():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_D8C9)
    Sleep(50)

    def lambda_D8D9():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D8D9)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "#5P#11505FOh, you're here.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#12P#00001FMr. Lechter...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FAre the guests\x01",
            "all right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#11503FYeah, for now, anyway.\x02",
    )

    CloseMessageWindow()
    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 10500, 0, 5000, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_D9C5():
        OP_96(0xFE, 0x2904, 0x0, 0xDAC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D9C5)

    def lambda_D9DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_D9DF)
    WaitChrThread(0xB, 1)
    OP_93(0xB, 0xE1, 0x1F4)

    ChrTalk(
        0xB,
        (
            "#11P#12001F──We'll talk later. They're\x01",
            "coming from behind, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FHuh...\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_DA8F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DA8F)
    Sleep(50)
    OP_93(0x105, 0x10E, 0x1F4)

    ChrTalk(
        0x103,
        "#11P#00201FReinforcements...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#11P#10301FIt looks like something's coming.\x02",
    )

    CloseMessageWindow()

    def lambda_DAFB():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DAFB)
    Sleep(50)

    def lambda_DB0B():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_DB0B)
    Sleep(50)

    def lambda_DB1B():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DB1B)
    Sleep(50)

    def lambda_DB2B():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_DB2B)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)

    def lambda_DB4B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_DB4B)

    def lambda_DB58():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_DB58)
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
        "#12P#10111FW-What're...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00307FThey look like those we\x01",
            "fought at the mafia's hideout!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007FAnyway, let's take 'em out!\x02",
    )

    CloseMessageWindow()
    StopSound(863, 500, 60)
    EndChrThread(0x4C, 0x1)
    Sound(943, 2, 70, 0)
    EndChrThread(0x49, 0x3)
    EndChrThread(0x4A, 0x3)
    EndChrThread(0x4B, 0x3)

    def lambda_DCD8():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x49, 1, lambda_DCD8)

    def lambda_DCF2():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x4A, 1, lambda_DCF2)

    def lambda_DD0C():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x4B, 1, lambda_DD0C)
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

    # Function_59_C3A8 end

    def Function_60_DD8C(): pass

    label("Function_60_DD8C")


    def lambda_DD91():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DD91)
    Sleep(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1B)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x0)
    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)

    def lambda_DDD0():
        OP_96(0xFE, 0x4844, 0x0, 0xB54, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DDD0)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_DDF8():
        OP_98(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DDF8)
    WaitChrThread(0xFE, 1)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_60_DD8C end

    def Function_61_DE1D(): pass

    label("Function_61_DE1D")


    def lambda_DE22():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DE22)
    SetChrChipByIndex(0xFE, 0x1B)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_DE5B():
        OP_98(0xFE, 0xFFFFE4A8, 0x0, 0x320, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DE5B)
    WaitChrThread(0xFE, 1)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_61_DE1D end

    def Function_62_DE80(): pass

    label("Function_62_DE80")


    def lambda_DE85():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DE85)
    SetChrChipByIndex(0xFE, 0x7)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x0)

    def lambda_DEB1():
        OP_95(0xFE, 21300, 0, -2500, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DEB1)
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

    def lambda_DF07():
        OP_98(0xFE, 0xFFFFE4A8, 0x0, 0x320, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DF07)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x7)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_62_DE80 end

    def Function_63_DF30(): pass

    label("Function_63_DF30")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)

    def lambda_DF40():
        OP_95(0xFE, 22000, 0, -2400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DF40)
    WaitChrThread(0xFE, 1)
    Sound(288, 0, 100, 0)

    def lambda_DF64():
        OP_95(0xFE, 24000, 0, -2400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DF64)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x2)

    def lambda_DFAC():
        OP_9D(0xFE, 0x6E8C, 0x0, 0xFFFFF6A0, 0x514, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DFAC)
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

    def lambda_E003():
        OP_9D(0xFE, 0x66BC, 0x0, 0xFFFFF7CC, 0x1F4, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E003)
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

    # Function_63_DF30 end

    def Function_64_E132(): pass

    label("Function_64_E132")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_E186():
        OP_93(0xFE, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_E186)

    def lambda_E193():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E193)

    def lambda_E1AC():
        OP_9D(0xFE, 0x7BD4, 0x0, 0xFFFFF3E4, 0x514, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E1AC)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_64_E132 end

    def Function_65_E1D2(): pass

    label("Function_65_E1D2")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E1EF():
        OP_96(0xFE, 0x6DC4, 0x0, 0xFFFFF830, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E1EF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_65_E1D2 end

    def Function_66_E209(): pass

    label("Function_66_E209")

    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_E245():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E245)

    def lambda_E25E():
        OP_9D(0xFE, 0x7C9C, 0x0, 0xFFFFF8F8, 0x384, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E25E)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_66_E209 end

    def Function_67_E284(): pass

    label("Function_67_E284")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E2A1():
        OP_96(0xFE, 0x6DC4, 0x0, 0xFFFFF4AC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E2A1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_67_E284 end

    def Function_68_E2BB(): pass

    label("Function_68_E2BB")

    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_E2F7():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E2F7)

    def lambda_E310():
        OP_9D(0xFE, 0x7DC8, 0x0, 0xFFFFF254, 0x384, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E310)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_68_E2BB end

    def Function_69_E336(): pass

    label("Function_69_E336")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E343():
        OP_95(0xFE, 22000, 0, 2400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E343)
    WaitChrThread(0xFE, 1)

    def lambda_E361():
        OP_95(0xFE, 24000, 0, 2400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E361)
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

    def lambda_E3EA():
        OP_95(0xFE, 28000, 0, 2400, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E3EA)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x5)
    BeginChrThread(0x26, 3, 0, 71)
    Sleep(300)
    SetChrSubChip(0xFE, 0x3)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_E428():
        OP_9D(0xFE, 0x67E8, 0x0, 0x3E8, 0x2BC, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E428)
    WaitChrThread(0xFE, 1)

    def lambda_E449():
        OP_9D(0xFE, 0x6400, 0x0, 0x7D0, 0x2BC, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E449)
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

    def lambda_E4CA():
        OP_95(0xFE, 28600, 0, 2000, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E4CA)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)

    def lambda_E4F7():
        OP_9D(0xFE, 0x6978, 0x0, 0x7D0, 0x2BC, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E4F7)
    WaitChrThread(0xFE, 1)
    Sound(329, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x3, 1000, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_E555():
        OP_95(0xFE, 30300, 0, 2000, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E555)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x5)
    Sleep(500)
    Return()

    # Function_69_E336 end

    def Function_70_E57A(): pass

    label("Function_70_E57A")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E587():
        OP_95(0xFE, 28200, 0, 2000, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E587)
    WaitChrThread(0xFE, 1)
    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E5E9():
        TurnDirection(0xFE, 0xA, 0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_E5E9)

    def lambda_E5F6():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E5F6)

    def lambda_E60F():
        OP_9D(0xFE, 0x7A44, 0x0, 0xCE4, 0x258, 0x2328)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E60F)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_70_E57A end

    def Function_71_E635(): pass

    label("Function_71_E635")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E642():
        OP_95(0xFE, 29000, 0, 1400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E642)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xD)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)

    def lambda_E677():
        OP_95(0xFE, 28000, 0, 2000, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E677)
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

    def lambda_E6CF():
        OP_95(0xFE, 26700, 0, 2000, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E6CF)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 26500, 1000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_E728():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E728)

    def lambda_E741():
        OP_96(0xFE, 0x6F54, 0x0, 0x7D0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E741)
    WaitChrThread(0xFE, 1)
    Sleep(450)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28300, 1000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0xF)
    SetChrSubChip(0xFE, 0x3)

    def lambda_E7A1():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E7A1)

    def lambda_E7BA():
        OP_96(0xFE, 0x79E0, 0x0, 0x7D0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E7BA)
    WaitChrThread(0xFE, 1)
    Sleep(600)
    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E81A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E81A)

    def lambda_E833():
        OP_9D(0xFE, 0x8084, 0x0, 0x7D0, 0x258, 0x2328)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E833)
    Sleep(50)
    EndChrThread(0x2E, 0x3)
    BeginChrThread(0x2E, 3, 0, 72)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_71_E635 end

    def Function_72_E861(): pass

    label("Function_72_E861")

    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E86E():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E86E)

    def lambda_E887():
        OP_9D(0xFE, 0x86C4, 0x0, 0xBB8, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E887)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_72_E861 end

    def Function_73_E8A8(): pass

    label("Function_73_E8A8")

    SetChrPos(0x25, 17000, 0, 1800, 90)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E8C6():
        OP_96(0xFE, 0x6400, 0x0, 0x514, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E8C6)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    BeginChrThread(0x25, 0, 0, 89)
    Return()

    # Function_73_E8A8 end

    def Function_74_E8F1(): pass

    label("Function_74_E8F1")

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

    # Function_74_E8F1 end

    def Function_75_E934(): pass

    label("Function_75_E934")

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

    # Function_75_E934 end

    def Function_76_E98E(): pass

    label("Function_76_E98E")

    Sleep(500)
    BeginChrThread(0x29, 3, 0, 78)

    def lambda_E99C():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E99C)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x2)
    Sleep(270)
    PlayEffect(0x8, 0xFF, 0xFE, 0x0, 0, 0, 0, 93, 0, 90, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x17, 0x3)
    Sleep(1200)

    def lambda_EA01():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EA01)
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

    def lambda_EA8E():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EA8E)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x2)
    Sleep(270)
    PlayEffect(0x8, 0xFF, 0xFE, 0x0, 0, 0, 0, 95, 0, 90, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x17, 0x3)
    Sleep(1500)
    Return()

    # Function_76_E98E end

    def Function_77_EAEF(): pass

    label("Function_77_EAEF")

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

    # Function_77_EAEF end

    def Function_78_EDA1(): pass

    label("Function_78_EDA1")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_EDB9():
        OP_96(0xFE, 0x701C, 0x0, 0xFFFFFC7C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EDB9)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_EDE4():
        OP_A6(0xFE, 0x0, 0x32, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EDE4)

    def lambda_EDFD():
        OP_9D(0xFE, 0x89E4, 0x0, 0xFFFFFBB4, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EDFD)
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

    def lambda_EE44():
        OP_96(0xFE, 0x701C, 0x0, 0xFFFFFC7C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EE44)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_EE6F():
        OP_A6(0xFE, 0x0, 0x32, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EE6F)

    def lambda_EE88():
        OP_9D(0xFE, 0x89E4, 0x0, 0xFFFFFBB4, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EE88)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_78_EDA1 end

    def Function_79_EEAE(): pass

    label("Function_79_EEAE")

    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_EEBB():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EEBB)

    def lambda_EED4():
        OP_9C(0xFE, 0x1F4, 0x0, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EED4)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0x16)
    SetChrSubChip(0xFE, 0x3)
    BeginChrThread(0xFE, 3, 0, 101)
    Return()

    # Function_79_EEAE end

    def Function_80_EF0D(): pass

    label("Function_80_EF0D")

    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_EF1A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EF1A)

    def lambda_EF33():
        OP_9C(0xFE, 0x1F4, 0x0, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EF33)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_80_EF0D end

    def Function_81_EF54(): pass

    label("Function_81_EF54")

    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 13300, 0, 200, 90)
    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0x17, 0x1E, 0xC8)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x2)
    PlayEffect(0x0, 0x0, 0x17, 0x3, 250, 1200, 500, 45, -45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_EFC1():
        OP_9D(0xFE, 0x571C, 0x0, 0x0, 0xDAC, 0x514)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_EFC1)
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

    def lambda_F0BB():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_F0BB)
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

    # Function_81_EF54 end

    def Function_82_F182(): pass

    label("Function_82_F182")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F251")
    OP_82(0x32, 0x32, 0xBB8, 0x4B0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 31500, 0, -1700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 30500, 0, -1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 31000, 0, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Jump("Function_82_F182")

    label("loc_F251")

    Return()

    # Function_82_F182 end

    def Function_83_F252(): pass

    label("Function_83_F252")


    def lambda_F257():
        OP_95(0xFE, 81000, 0, 2200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F257)

    def lambda_F271():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F271)
    WaitChrThread(0xFE, 1)

    def lambda_F286():
        OP_95(0xFE, 75000, 0, 0, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F286)
    WaitChrThread(0xFE, 1)

    def lambda_F2A4():
        OP_95(0xFE, 65000, 0, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F2A4)
    Sleep(1100)

    def lambda_F2C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F2C1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_83_F252 end

    def Function_84_F2D2(): pass

    label("Function_84_F2D2")


    def lambda_F2D7():
        OP_95(0xFE, 80500, 0, 2200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F2D7)

    def lambda_F2F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F2F1)
    WaitChrThread(0xFE, 1)

    def lambda_F306():
        OP_95(0xFE, 75000, 0, -300, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F306)
    WaitChrThread(0xFE, 1)

    def lambda_F324():
        OP_95(0xFE, 65000, 0, -300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F324)
    Sleep(1100)

    def lambda_F341():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F341)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_84_F2D2 end

    def Function_85_F352(): pass

    label("Function_85_F352")


    def lambda_F357():
        OP_95(0xFE, 81500, 0, 2200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F357)

    def lambda_F371():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F371)
    WaitChrThread(0xFE, 1)

    def lambda_F386():
        OP_95(0xFE, 75000, 0, 300, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F386)
    WaitChrThread(0xFE, 1)

    def lambda_F3A4():
        OP_95(0xFE, 65000, 0, 300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F3A4)
    Sleep(1100)

    def lambda_F3C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F3C1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_85_F352 end

    def Function_86_F3D2(): pass

    label("Function_86_F3D2")

    SetChrChipByIndex(0x30, 0x15)
    SetChrSubChip(0x30, 0x0)

    def lambda_F3DF():
        OP_96(0xFE, 0x88B8, 0x0, 0x12C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F3DF)

    def lambda_F3F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F3F9)
    WaitChrThread(0xFE, 1)

    def lambda_F40E():
        OP_96(0xFE, 0x8598, 0x0, 0x1F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F40E)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x30, 0x16)
    SetChrSubChip(0x30, 0x3)
    BeginChrThread(0x30, 3, 0, 101)
    Return()

    # Function_86_F3D2 end

    def Function_87_F436(): pass

    label("Function_87_F436")

    SetChrChipByIndex(0x31, 0x15)
    SetChrSubChip(0x31, 0x0)

    def lambda_F443():
        OP_96(0xFE, 0x88B8, 0x0, 0xFFFFFED4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F443)

    def lambda_F45D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F45D)
    WaitChrThread(0xFE, 1)

    def lambda_F472():
        OP_96(0xFE, 0x8278, 0x0, 0xFFFFFAEC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F472)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x31, 0x16)
    SetChrSubChip(0x31, 0x3)
    BeginChrThread(0x31, 3, 0, 101)
    Return()

    # Function_87_F436 end

    def Function_88_F49A(): pass

    label("Function_88_F49A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F4EF")
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)
    Jump("Function_88_F49A")

    label("loc_F4EF")

    Return()

    # Function_88_F49A end

    def Function_89_F4F0(): pass

    label("Function_89_F4F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F560")
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
    Jump("Function_89_F4F0")

    label("loc_F560")

    Return()

    # Function_89_F4F0 end

    def Function_90_F561(): pass

    label("Function_90_F561")


    def lambda_F566():
        OP_96(0xFE, 0x1B58, 0x0, 0xFFFFFF38, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F566)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_90_F561 end

    def Function_91_F580(): pass

    label("Function_91_F580")


    def lambda_F585():
        OP_96(0xFE, 0x1964, 0x0, 0x2BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F585)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_91_F580 end

    def Function_92_F59F(): pass

    label("Function_92_F59F")


    def lambda_F5A4():
        OP_96(0xFE, 0x1450, 0x0, 0x64, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F5A4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_92_F59F end

    def Function_93_F5BE(): pass

    label("Function_93_F5BE")


    def lambda_F5C3():
        OP_96(0xFE, 0x125C, 0x0, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F5C3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_93_F5BE end

    def Function_94_F5DD(): pass

    label("Function_94_F5DD")


    def lambda_F5E2():
        OP_96(0xFE, 0x1324, 0x0, 0xFFFFFAEC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F5E2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_94_F5DD end

    def Function_95_F5FC(): pass

    label("Function_95_F5FC")


    def lambda_F601():
        OP_96(0xFE, 0x16A8, 0x0, 0xFFFFF8F8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F601)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_95_F5FC end

    def Function_96_F61B(): pass

    label("Function_96_F61B")


    def lambda_F620():
        OP_96(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F620)

    def lambda_F63A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F63A)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 3, 0, 99)
    Return()

    # Function_96_F61B end

    def Function_97_F651(): pass

    label("Function_97_F651")


    def lambda_F656():
        OP_96(0xFE, 0xFFFFE9BC, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F656)

    def lambda_F670():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F670)
    WaitChrThread(0xFE, 1)

    def lambda_F685():
        OP_96(0xFE, 0xFFFFF95C, 0x0, 0x514, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F685)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 3, 0, 99)
    Return()

    # Function_97_F651 end

    def Function_98_F6A5(): pass

    label("Function_98_F6A5")


    def lambda_F6AA():
        OP_96(0xFE, 0xFFFFE9BC, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F6AA)

    def lambda_F6C4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F6C4)
    WaitChrThread(0xFE, 1)

    def lambda_F6D9():
        OP_96(0xFE, 0xFFFFF95C, 0x0, 0xFFFFFAEC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F6D9)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 3, 0, 99)
    Return()

    # Function_98_F6A5 end

    def Function_99_F6F9(): pass

    label("Function_99_F6F9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F714")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_99_F6F9")

    label("loc_F714")

    Return()

    # Function_99_F6F9 end

    def Function_100_F715(): pass

    label("Function_100_F715")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F8AB")
    ClearScenarioFlags(0x0, 1)
    SetChrSubChip(0xFE, 0x4)

    def lambda_F72C():
        OP_A6(0xFE, 0x0, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F72C)
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
    Jump("Function_100_F715")

    label("loc_F8AB")

    Return()

    # Function_100_F715 end

    def Function_101_F8AC(): pass

    label("Function_101_F8AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FA3C")
    SetChrSubChip(0xFE, 0x4)

    def lambda_F8C0():
        OP_A6(0xFE, 0x0, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F8C0)
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
    Jump("Function_101_F8AC")

    label("loc_FA3C")

    Return()

    # Function_101_F8AC end

    def Function_102_FA3D(): pass

    label("Function_102_FA3D")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1A)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_FA5B():
        OP_9D(0xFE, 0x5654, 0x0, 0x76C, 0x3E8, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FA5B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x87, 0x0)
    Sound(811, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_102_FA3D end

    def Function_103_FA8D(): pass

    label("Function_103_FA8D")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_FAA5():
        OP_9D(0xFE, 0x5654, 0x0, 0xFFFFF31C, 0x384, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FAA5)
    WaitChrThread(0xFE, 1)
    Sound(862, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_103_FA8D end

    def Function_104_FAD0(): pass

    label("Function_104_FAD0")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    Sound(250, 0, 100, 0)

    def lambda_FAEE():
        OP_9D(0xFE, 0x53FC, 0x0, 0xFFFFFCE0, 0x190, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FAEE)
    WaitChrThread(0xFE, 1)

    def lambda_FB0F():
        OP_A6(0xFE, 0x0, 0x32, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FB0F)
    SetChrSubChip(0xFE, 0x2)
    WaitChrThread(0x25, 2)
    Return()

    # Function_104_FAD0 end

    def Function_105_FB2C(): pass

    label("Function_105_FB2C")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_FB39():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FB39)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_105_FB2C end

    def Function_106_FB53(): pass

    label("Function_106_FB53")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_FB60():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0xFFFFFF38, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FB60)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_106_FB53 end

    def Function_107_FB7A(): pass

    label("Function_107_FB7A")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_FB87():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0xC8, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FB87)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_107_FB7A end

    def Function_108_FBA1(): pass

    label("Function_108_FBA1")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_FBAE():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FBAE)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_108_FBA1 end

    def Function_109_FBC8(): pass

    label("Function_109_FBC8")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_FBE6():
        OP_9D(0xFE, 0x6978, 0x0, 0x12C, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FBE6)
    WaitChrThread(0xFE, 1)
    Sound(862, 0, 100, 0)

    def lambda_FC0D():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FC0D)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_109_FBC8 end

    def Function_110_FC26(): pass

    label("Function_110_FC26")

    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_FC39():
        OP_9D(0xFE, 0x7530, 0x0, 0x320, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FC39)
    WaitChrThread(0xFE, 1)
    Sound(811, 0, 100, 0)

    def lambda_FC60():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FC60)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_110_FC26 end

    def Function_111_FC79(): pass

    label("Function_111_FC79")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_FC91():
        OP_9D(0xFE, 0x6720, 0x0, 0xFFFFF768, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FC91)
    WaitChrThread(0xFE, 1)

    def lambda_FCB2():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FCB2)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    Return()

    # Function_111_FC79 end

    def Function_112_FCE0(): pass

    label("Function_112_FCE0")

    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xF)
    SetChrSubChip(0xFE, 0x3)

    def lambda_FCF2():
        TurnDirection(0xFE, 0x17, 500)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_FCF2)

    def lambda_FCFF():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FCFF)

    def lambda_FD18():
        OP_96(0xFE, 0x72D8, 0x0, 0xFFFFF448, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FD18)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_112_FCE0 end

    def Function_113_FD37(): pass

    label("Function_113_FD37")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_FD4F():
        OP_9D(0xFE, 0x6720, 0x0, 0x5DC, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FD4F)
    WaitChrThread(0xFE, 1)

    def lambda_FD70():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FD70)
    SetChrSubChip(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    Return()

    # Function_113_FD37 end

    def Function_114_FDA2(): pass

    label("Function_114_FDA2")

    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xF)
    SetChrSubChip(0xFE, 0x3)

    def lambda_FDB4():
        TurnDirection(0xFE, 0x17, 500)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_FDB4)

    def lambda_FDC1():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FDC1)

    def lambda_FDDA():
        OP_96(0xFE, 0x72D8, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FDDA)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_114_FDA2 end

    def Function_115_FDF9(): pass

    label("Function_115_FDF9")


    def lambda_FDFE():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FDFE)
    SetChrChipByIndex(0xFE, 0xF)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_115_FDF9 end

    def Function_116_FE1B(): pass

    label("Function_116_FE1B")

    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_FE28():
        OP_9D(0xFE, 0x7A44, 0x0, 0xFFFFFB50, 0x2BC, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FE28)
    WaitChrThread(0xFE, 1)

    def lambda_FE49():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FE49)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_116_FE1B end

    def Function_117_FE62(): pass

    label("Function_117_FE62")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)

    def lambda_FE7A():
        OP_9C(0xFE, 0xFFFFE890, 0x0, 0x0, 0x1F4, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FE7A)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_117_FE62 end

    def Function_118_FE9F(): pass

    label("Function_118_FE9F")


    def lambda_FEA4():
        OP_96(0xFE, 0x7C9C, 0x0, 0x12C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FEA4)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x17, 0xB)
    SetChrSubChip(0x17, 0x0)
    Return()

    # Function_118_FE9F end

    def Function_119_FEC6(): pass

    label("Function_119_FEC6")


    def lambda_FECB():
        OP_96(0xFE, 0x76C0, 0x0, 0x76C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FECB)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x12)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_119_FEC6 end

    def Function_120_FEED(): pass

    label("Function_120_FEED")


    def lambda_FEF2():
        OP_96(0xFE, 0x76C0, 0x0, 0xFFFFF894, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FEF2)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_120_FEED end

    def Function_121_FF14(): pass

    label("Function_121_FF14")


    def lambda_FF19():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFED4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FF19)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0xD)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_121_FF14 end

    def Function_122_FF3B(): pass

    label("Function_122_FF3B")

    Sleep(1200)

    label("loc_FF3E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FF57")
    Sound(530, 0, 80, 0)
    Sleep(1200)
    Jump("loc_FF3E")

    label("loc_FF57")

    Return()

    # Function_122_FF3B end

    def Function_123_FF58(): pass

    label("Function_123_FF58")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FF71")
    Sound(356, 0, 50, 0)
    Sleep(1100)
    Jump("Function_123_FF58")

    label("loc_FF71")

    Return()

    # Function_123_FF58 end

    def Function_124_FF72(): pass

    label("Function_124_FF72")

    Sleep(1000)

    label("loc_FF75")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FFA3")
    Sound(264, 0, 40, 0)
    Sound(833, 0, 30, 0)
    Sleep(1600)
    Sound(264, 0, 40, 0)
    Sound(833, 0, 30, 0)
    Sleep(3000)
    Jump("loc_FF75")

    label("loc_FFA3")

    Return()

    # Function_124_FF72 end

    def Function_125_FFA4(): pass

    label("Function_125_FFA4")

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
        "#00010F#11PTch, they even had those?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12PThey probably came\x01",
            "in from the roof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00301FBut aren't those things\x01",
            "made by that "Society"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10308FThey must've gotten them\x01",
            "through the black market, or...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#6P#11508F...It doesn't matter. It seems\x01",
            "they've settled things there too.\x02",
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

    def lambda_10673():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_10673)

    def lambda_10680():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10680)
    Sleep(50)

    def lambda_10690():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10690)
    Sleep(50)

    def lambda_106A0():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_106A0)
    Sleep(50)

    def lambda_106B0():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_106B0)
    Sleep(50)

    def lambda_106C0():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_106C0)
    Sleep(50)

    def lambda_106D0():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_106D0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x26,
        "#12PUgh... Damn monsters!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "There's no choice! \x01",
            "Switch to the final plan!\x02",
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
        "#01401F#7A#5PMmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#07105F#8A#5PA stun grenade...!?\x02",
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
        "#6P#07301FTch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#07101F#5PThat shutter is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#01403F#5P...It seems we won't be able\x01",
            "to get through it easily.\x02",
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

    def lambda_10C53():
        OP_97(0x101, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10C53)
    Sleep(100)

    def lambda_10C70():
        OP_97(0x102, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10C70)
    Sleep(100)

    def lambda_10C8D():
        OP_97(0x103, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10C8D)
    Sleep(100)

    def lambda_10CAA():
        OP_97(0x104, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10CAA)
    Sleep(100)

    def lambda_10CC7():
        OP_97(0x109, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10CC7)
    Sleep(100)

    def lambda_10CE4():
        OP_97(0x105, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10CE4)
    Sleep(100)

    def lambda_10D01():
        OP_97(0xB, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_10D01)
    Sleep(100)

    def lambda_10D1E():
        OP_97(0x8, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_10D1E)
    WaitChrThread(0xB, 0)

    def lambda_10D3C():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_10D3C)
    WaitChrThread(0x8, 0)

    def lambda_10D4D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_10D4D)

    ChrTalk(
        0x25,
        "#11P#00600FYou guys, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#6PIt seems you were able\x01",
            "to push them back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11P#01403FYes, but they'll get\x01",
            "away at this rate.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#11P#00001F#5PTio, can you do it!?\x02",
    )

    CloseMessageWindow()

    def lambda_10E1B():

        label("loc_10E1B")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_10E1B")

    QueueWorkItem2(0x101, 2, lambda_10E1B)

    def lambda_10E2D():

        label("loc_10E2D")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_10E2D")

    QueueWorkItem2(0x102, 2, lambda_10E2D)

    def lambda_10E3F():

        label("loc_10E3F")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_10E3F")

    QueueWorkItem2(0x109, 2, lambda_10E3F)

    def lambda_10E51():

        label("loc_10E51")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_10E51")

    QueueWorkItem2(0x105, 2, lambda_10E51)

    def lambda_10E63():

        label("loc_10E63")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_10E63")

    QueueWorkItem2(0x104, 2, lambda_10E63)
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#6P#00201FI am not sure, but\x01",
            "I will give it a try\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10EB3():
        OP_95(0xFE, 32800, 0, -2700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10EB3)
    Sleep(300)

    def lambda_10ED0():

        label("loc_10ED0")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_10ED0")

    QueueWorkItem2(0x25, 2, lambda_10ED0)
    Sleep(50)

    def lambda_10EE5():

        label("loc_10EE5")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_10EE5")

    QueueWorkItem2(0x17, 2, lambda_10EE5)
    Sleep(50)

    def lambda_10EFA():

        label("loc_10EFA")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_10EFA")

    QueueWorkItem2(0x9, 2, lambda_10EFA)
    Sleep(50)

    def lambda_10F0F():

        label("loc_10F0F")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_10F0F")

    QueueWorkItem2(0xA, 2, lambda_10F0F)
    WaitChrThread(0x103, 1)

    def lambda_10F25():
        OP_95(0xFE, 34200, 0, -2100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10F25)
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
            "#11P#00206FAs I thought, the security level\x01",
            "has been increased to maximum.\x02\x03",
            "#00208FEven if I use "Aeon", with this\x01",
            "notebook-type terminal, I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00008FI see...\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x25, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_1108A():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1108A)

    def lambda_11097():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11097)

    def lambda_110A4():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_110A4)
    Sleep(50)

    def lambda_110B4():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_110B4)

    def lambda_110C1():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_110C1)
    Sleep(50)

    def lambda_110D1():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_110D1)

    def lambda_110DE():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_110DE)

    def lambda_110EB():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_110EB)
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
            "#5P#00600F──It's me.\x02\x03",
            "#00603FYeah, we were barely\x01",
            "able to hold out, but...\x02\x03",
            "............\x02\x03",
            "#00601F...What?\x02\x03",
            "They took the elevator\x01",
            "to the basement!?\x02",
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
        "#6P#N#10113FW-Why...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00105F#5PThey're not retreating using\x01",
            "the airships on the roof...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11503F#5PHmm. If you think about it...\x02\x03",
            "#11501FMaybe they're thinking of detonating the\x01",
            "airships with orbal bombs they placed onboard?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_113DC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_113DC)

    def lambda_113E9():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_113E9)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_11429():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11429)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_11481():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11481)

    def lambda_1148E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1148E)

    def lambda_1149B():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1149B)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_114C3():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_114C3)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_114E8():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_114E8)
    OP_63(0x25, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    ClearChrFlags(0x25, 0x10)
    ClearChrFlags(0x25, 0x2)
    ClearChrFlags(0x25, 0x20)
    SetChrChipByIndex(0x25, 0x21)
    SetChrSubChip(0x25, 0x0)
    Sound(802, 0, 100, 0)

    def lambda_1152A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_1152A)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#00007FWhat...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#11P#01401FI see, in that case...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#07307FEveryone in the building\x01",
            "would be taken out...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12003F#5PIf they're terrorists\x01",
            "they might go that far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#07101FTch, fools...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10306FThis is really bad...\x02",
    )

    CloseMessageWindow()
    OP_93(0x25, 0x5A, 0x1F4)

    ChrTalk(
        0x25,
        (
            "#5P#00610FTch, given the situation, then we have to break\x01",
            "through this shutter, even if it's with brute force!\x02",
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
            "#11P#00204F#30W...No...\x02\x03",
            "#00202F#20WI might be able to do\x01",
            "something about it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1171A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1171A)

    def lambda_11727():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_11727)

    def lambda_11734():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_11734)
    Sleep(50)

    def lambda_11744():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11744)

    def lambda_11751():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_11751)

    def lambda_1175E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1175E)
    Sleep(50)

    def lambda_1176E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1176E)

    def lambda_1177B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1177B)

    def lambda_11788():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_11788)
    WaitChrThread(0x25, 2)

    ChrTalk(
        0x25,
        "#5P#00605FWhat...!?\x02",
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

    # Function_125_FFA4 end

    def Function_126_117DF(): pass

    label("Function_126_117DF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_117F9")
    OP_A1(0x103, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_126_117DF")

    label("loc_117F9")

    Return()

    # Function_126_117DF end

    def Function_127_117FA(): pass

    label("Function_127_117FA")

    Sleep(200)
    Sound(555, 0, 80, 0)
    Sleep(500)
    Sound(555, 0, 60, 0)
    Sleep(200)
    Sound(555, 0, 30, 0)
    Return()

    # Function_127_117FA end

    def Function_128_11816(): pass

    label("Function_128_11816")

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

    def lambda_1199E():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1199E)

    def lambda_119AB():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_119AB)

    def lambda_119B8():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_119B8)

    def lambda_119C5():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_119C5)

    def lambda_119D2():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_119D2)

    def lambda_119DF():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_119DF)

    def lambda_119EC():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_119EC)

    def lambda_119F9():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_119F9)

    def lambda_11A06():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_11A06)
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
            "#5P#00002FJona...\x01",
            "Did he come back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202F#11PYes, it seems he returned\x01",
            "on today's flight.\x02",
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
            "#12P#00204F#11P──Done. \x01",
            "Releasing tower controls.\x02",
        )
    )

    CloseMessageWindow()
    Sound(145, 2, 100, 0)
    OP_71(0x11, 0x0, 0x3C, 0x0, 0x0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_11BFB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11BFB)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_11C20():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11C20)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_11C48():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11C48)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_11C6D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11C6D)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_11C95():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_11C95)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_11CBA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_11CBA)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_11CE2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_11CE2)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_11D07():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_11D07)
    OP_63(0x25, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_11D2C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_11D2C)
    Sleep(1000)
    OP_79(0x11)
    OP_24(0x91)
    Sound(143, 0, 100, 0)

    ChrTalk(
        0xA,
        "#5P#07102FYou did it...!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x25, 0x103, 500)

    ChrTalk(
        0x25,
        "#5P#00602FCan we use the elevators!?\x02",
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
            "#12P#00202F#11PYes. I released the locks.\x02\x03",
            "#00206FThough we can't control the\x01",
            "one the terrorists are using.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12004F#5PIn that case I'll go to the roof.\x02\x03",
            "#12000FI'll disarm the orbal bombs\x01",
            "onboard those airships.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 500)

    ChrTalk(
        0x101,
        "#12P#00005FYou can do that, Miss Kilika?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12004F#5PYes. It's an essential skill for\x01",
            "any counter-intelligence officer.\x02\x03",
            "#12000FSecretary Lechter. Let's divide\x01",
            "this task amongst ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11504FCan't be helped, I guess.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xB, 500)

    ChrTalk(
        0x9,
        (
            "#11P#07303FIn that case, we'll accompany you.\x02\x03",
            "#07300FIt's possible they've left\x01",
            "archaisms to protect the bombs.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x25, 500)

    def lambda_12016():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12016)

    ChrTalk(
        0xA,
        (
            "#5P#07101F──Please, go after\x01",
            "the terrorists!\x02\x03",
            "You might still have\x01",
            "time to catch them!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x101, 500)

    ChrTalk(
        0x17,
        "#11P#01400FUnderstood...!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x25, 0x101, 500)

    ChrTalk(
        0x25,
        (
            "#11P#00601FBannings! \x01",
            "We're going after them too!\x02\x03",
            "There's two enemy groups...\x01",
            "We'll need to split up.\x02",
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
        "#00307F#6PAye aye, sir!\x02",
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

    # Function_128_11816 end

    def Function_129_12170(): pass

    label("Function_129_12170")

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
            "#1KSame day, 18:00──\x02",
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

    def lambda_1240A():
        OP_96(0xFE, 0x61A8, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_1240A)

    def lambda_12424():
        OP_96(0xFE, 0xFFFFEC78, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3B, 1, lambda_12424)
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
            "#02803F#11P#30WI see... Understood.\x02\x03",
            "#02801F...We're safe here.\x01",
            "Please don't worry.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1D, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x1D,
        "#02806F#11P#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#11P#02500F...What happened to the terrorists?\x02",
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
            "#02803F#5PThe Republican terrorists were apprehended by\x01",
            "employees of the "Heiyue" Trade Company.\x02\x03",
            "#02801FApparently, they had authorization\x01",
            "from the Republican government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#07005F#11P#NEh!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x22,
        (
            "#6P#07502FOh, splendid!\x02\x03",
            "#07509FThey're my friends. I'll vouch\x01",
            "for them, so please don't worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12004F#6P#N............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1D,
        (
            "#02806FAnd as for the Imperial terrorists...\x02\x03",
            "#02801FIt seems that, with the permission of the\x01",
            "Imperial government, the "Red Constellation"\x01",
            "jaeger corps executed nearly all of them.\x02",
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
        "#6P...How could they...\x02",
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
            "#07207F#11P──Chancellor! \x01",
            "What're you planning!?\x02\x03",
            "Do you mean to say you used jaegers\x01",
            "in the name of an Imperial government\x01",
            "execution outside the country!?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x1)
    Sleep(300)

    ChrTalk(
        0x1E,
        (
            "#5P#07404FYes. To be absolutely certain.\x02\x03",
            "#07401FIn any case, I cannot think any punishment other \x01",
            "than certain death would be suitable for an attempt \x01",
            "on your life, Your Highness.\x02\x03",
            "I think it will serve as a good warning to\x01",
            "those fools who remained behind as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "#07201FKh......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11508F#11P(...Well said.)\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x24,
        (
            "#02205F#11P#NIt's certainly true that those actions\x01",
            "are permitted per autonomous state law.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x23, 0x1)

    ChrTalk(
        0x23,
        (
            "#5P#02507FBut, this is too──\x02\x03",
            "It's too great a\x01",
            "breach of trust!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "#6P#07505F#NOh, you misunderstand.\x02",
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

    def lambda_12EC1():
        TurnDirection(0xFE, 0x22, 0)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_12EC1)
    SetChrSubChip(0x23, 0x2)
    SetChrSubChip(0x1F, 0x0)
    SetChrSubChip(0x1E, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "#6P#07504FBut more importantly, isn't their\x01",
            "plan proof of what we were saying?\x02\x03",
            "#07502FThat the Crossbell autonomous state\x01",
            "government cannot deal with an\x01",
            "accident of this scale on its own?\x02",
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
        "#11P#02501F...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#11P#07404FYes. After the terrorists successfully\x01",
            "approached the conference venue...\x02\x03",
            "You failed to capture them, and in\x01",
            "the end it was due to our planning\x01",
            "that their escape was prevented.\x02\x03",
            "#07402FYou could call it an example of how the measure\x01",
            "we discussed earlier would work in practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#6P#07503FYes. While it may be rude, for the sake\x01",
            "of everyone whose life was in danger...\x02\x03",
            "#07500FIs it not now time to seriously\x01",
            "consider the stationed\x01",
            "troops proposal?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x23, 0x0)
    Sleep(300)

    def lambda_1325F():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_1325F)
    WaitChrThread(0x23, 2)
    Sleep(500)

    ChrTalk(
        0x23,
        "#5P#02501FH-How could you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#12P...How heavy-handed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#07008F#11P#NI-I don't believe it! So that's why...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1F,
        (
            "#07201F#11PBoth of you have employed some\x01",
            "crafty plans here, haven't you...\x02",
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
            "#02803F#5P──Everyone. It seems\x01",
            "we have digressed.\x02",
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
            "#02800F#5P#30WThe Chancellor and President's proposal\x01",
            "is worthy of consideration. However...\x02\x03",
            "Before that, allow me to restate my remarks\x01",
            "that were interrupted by the attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#11P#02505F#30WD-Dieter...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#11P#N#07405F#30WOh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x22,
        "#12P#N#07505F#30W...Hmm.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x21,
        "#30WAnd, what sort of proposal do you have in mind?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#5P#02804F#30WNo── It's not a proposal but\x01",
            "rather a declaration of intent.\x02\x03",
            "I have been hesitant about this...\x01",
            "But after this incident, my resolve is firm.\x02\x03",
            "#02800FI will make a single\x01",
            "declaration, here and now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#11P#N#07401F#30W...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x22,
        "#12P#N#07501F#30WWhat...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(500)
    OP_6F(0x79)

    ChrTalk(
        0x1D,
        (
            "#5P#02803F#30WWe will no longer be bandied about\x01",
            "according to the whims of other countries.\x02\x03",
            "#02801FFor the development of lasting peace in the\x01",
            "surrounding areas, and indeed, the whole continent─\x02",
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
            "#5P#02807F#4SI now advocate, to the citizens\x01",
            "and nations of the continent, the\x01",
            ""Independent State of Crossbell"!\x02",
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

    # Function_129_12170 end

    def Function_130_13845(): pass

    label("Function_130_13845")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1385C")
    OP_A0(0xFE, 2500, 0x0, 0xFB)
    Jump("Function_130_13845")

    label("loc_1385C")

    Return()

    # Function_130_13845 end

    def Function_131_1385D(): pass

    label("Function_131_1385D")


    def lambda_13862():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13862)
    WaitChrThread(0xFE, 1)
    Sleep(1500)
    OP_63(0x3E, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    def lambda_1389B():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1389B)
    WaitChrThread(0xFE, 1)
    Sleep(1500)

    def lambda_138BC():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_138BC)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_131_1385D end

    def Function_132_138D6(): pass

    label("Function_132_138D6")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13BA6")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The elevator's shutter\x01",
            "is firmly shut.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00005FThat's right. During the conference,\x01",
            "we can't use any elevators except\x01",
            "the ones in the front, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. It must be that way\x01",
            "for security reasons.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_END)), "loc_13AA4")

    ChrTalk(
        0x103,
        (
            "#00200FThe same as the emergency\x01",
            "stairs, it seems these too are\x01",
            "controlled via the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, looks that way.\x02\x03",
            "#00000FWhatever. When we need to move, \x01",
            "let's use the elevators in the front.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B9E")

    label("loc_13AA4")


    ChrTalk(
        0x103,
        (
            "#00200FBy the way, it seems the\x01",
            "lock mechanism is controlled\x01",
            "via the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, I should expect that much from\x01",
            "the Orchis Tower security system.\x02\x03",
            "#00000FWhatever. When we need to move, \x01",
            "let's use the elevator in the front.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B9E")

    SetScenarioFlags(0x1C2, 2)
    Jump("loc_13C18")

    label("loc_13BA6")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The elevator's shutter\x01",
            "is firmly shut.\x02\x03",
            "It seems you can't use this elevator\x01",
            "during the conference.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_13C18")

    TalkEnd(0xFF)
    Return()

    # Function_132_138D6 end

    def Function_133_13C1C(): pass

    label("Function_133_13C1C")

    EventBegin(0x1)
    OP_4B(0x1A, 0xFF)
    TurnDirection(0x1A, 0x0, 500)
    Sleep(500)

    ChrTalk(
        0x1A,
        "We're just in the middle of the conference right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "You can see how it's going from the gallery above.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 9780, 0, 1430, 180)
    OP_93(0x1A, 0xB4, 0x0)
    OP_4C(0x1A, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_133_13C1C end

    def Function_134_13CBF(): pass

    label("Function_134_13CBF")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F...It's not like we can enter the conference.\x02\x03",
            "#00001FLet's leave before we bother everyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 90250, 0, 76140, 270)
    EventEnd(0x4)
    Return()

    # Function_134_13CBF end

    def Function_135_13D3F(): pass

    label("Function_135_13D3F")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F...It's not like we can enter the conference.\x02\x03",
            "#00001FLet's leave before we bother everyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 168870, 0, 76540, 90)
    EventEnd(0x4)
    Return()

    # Function_135_13D3F end

    SaveToFile()

Try(main)
