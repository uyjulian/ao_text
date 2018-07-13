from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1500.bin",                # FileName
        "t1500",                    # MapName
        "t1500",                    # Location
        0x004D,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 77, 0, 4, 0, 5],
    )

    BuildStringList((
        "t1500",                  # 0
        "Guard Tony",             # 1
        "Nurse Ada",              # 2
        "Janitor Dyson",          # 3
        "Professor Seiland",      # 4
        "Harold",                 # 5
        "Rixia",                  # 6
        "Billy",                  # 7
        "Driver",                 # 8
        "Cecil",                  # 9
        "バス",                   # 10
        "State Guard Soldier",    # 11
        "State Guard Soldier",    # 12
        "State Guard Soldier",    # 13
        "State Guard Soldier",    # 14
        "Cecil",                  # 15
        "Fran",                   # 16
        "車",                     # 17
        "メルカバ玖号機",         # 18
        "Male Nurse A",           # 19
        "Male Nurse B",           # 20
        "Medical Intern A",       # 21
        "Medical Intern B",       # 22
        "Child",                  # 23
        "Old Man",                # 24
        "Elderly Man",            # 25
        "Elderly Woman",          # 26
        "Visitor A",              # 27
        "Visitor B",              # 28
        "Visitor C",              # 29
        "Visitor D",              # 30
        "SE制御",                 # 31
        "bt1510",                 # 32
        "St. Ursula Byroad",      # 33
    ))

    ATBonus("ATBonus_7E0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_8C0", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C8", 8, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_8CC", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D0", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8DC", 12, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8A0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_8A4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_8A8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_8AC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_8B0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_8B4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_8B8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8BC", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_8E0", 0x0002, 255, 6, 45, 3, 3, 30, 0, "bt1510", 0x00000000, 100, 0, 0, 0,
        (
            ("ms41501.dat", "ms41401.dat", "ms41401.dat", "ms41501.dat", 0, 0, 0, 0, "MonsterBattlePostion_8C0", "MonsterBattlePostion_8A0", "ed7452", "ed7453", "ATBonus_7E0"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch28600.itc",                   # 00
        "chr/ch29800.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch44800.itc",                   # 03
        "chr/ch09300.itc",                   # 04
        "chr/ch03200.itc",                   # 05
        "chr/ch23600.itc",                   # 06
        "chr/ch28300.itc",                   # 07
        "chr/ch05300.itc",                   # 08
    ))

    DeclNpc(4294919736, 0,       4000,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4294944256, 4294966296, 4294941387, 0,    257,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294937296, 4294966296, 4294946997, 246,  389,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294945317, 4294966296, 4294941266, 180,  389,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294918407, 0,       4000,    90,   389,  0x0, 0,   4,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4294917276, 0,       4294967066, 90,   389,  0x0, 0,   5,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(4294914817, 0,       13199,   180,  385,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294913206, 0,       11979,   180,  389,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4294943096, 4294966296, 4294942587, 180,  389,  0x0, 0,   8,   0,   0,   0,   0,   95,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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

    DeclEvent(0x0000, 0, 21,  -47.5,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   15.833333969116211,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 27,  -42.0,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   14.0,                  -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 40,  -47.5,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   15.833333969116211,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 90,  -42.5,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   14.166666984558105,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 92,  -44.75,                0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   14.916666984558105,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 93,  -47.5,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   15.833333969116211,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 94,  -43.75,                0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   14.583333969116211,    -0.0,                  0.20000000298023224,   1.0])

    DeclActor(4294909296, 0,       4000,    1500,    4294909296, 1500,    4000,    0x007C, 0,  19, 0x0000)
    DeclActor(4294950466, 4294966296, 4294939786, 1200,    4294950116, 4294965296, 4294934526, 0x007C, 0,  20, 0x0000)
    DeclActor(4294917886, 0,       16470,   1200,    4294917886, 2000,    16470,   0x007C, 0,  18, 0x0000)
    DeclActor(4294919296, 0,       17000,   1200,    4294919296, 2000,    17000,   0x007C, 0,  18, 0x0000)
    DeclActor(4294959416, 0,       6560,    1200,    4294959416, 1500,    6560,    0x007C, 0,  98, 0x0000)
    DeclActor(4294930436, 0,       14360,   1200,    4294930436, 1500,    14360,   0x007C, 0,  99, 0x0000)

    PlaceName(-69.0, 0.0, -8.0, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(-23.0, 0.0, 18.0, 0x0000, 0x0052, "")
    PlaceName(-57.900001525878906, 0.0, 4.199999809265137, 0x0000, 0x0055, "")

    ChipFrameInfo(2740, 0)                                       # 0

    ScpFunction((
        "Function_0_AB4",          # 00, 0
        "Function_1_B6C",          # 01, 1
        "Function_2_C24",          # 02, 2
        "Function_3_C85",          # 03, 3
        "Function_4_D00",          # 04, 4
        "Function_5_1432",         # 05, 5
        "Function_6_1757",         # 06, 6
        "Function_7_182A",         # 07, 7
        "Function_8_1957",         # 08, 8
        "Function_9_197E",         # 09, 9
        "Function_10_1A12",        # 0A, 10
        "Function_11_2DF9",        # 0B, 11
        "Function_12_3CCC",        # 0C, 12
        "Function_13_4508",        # 0D, 13
        "Function_14_46B4",        # 0E, 14
        "Function_15_4773",        # 0F, 15
        "Function_16_48A9",        # 10, 16
        "Function_17_4BA6",        # 11, 17
        "Function_18_4C3D",        # 12, 18
        "Function_19_4F76",        # 13, 19
        "Function_20_4FCA",        # 14, 20
        "Function_21_508F",        # 15, 21
        "Function_22_5E76",        # 16, 22
        "Function_23_5E86",        # 17, 23
        "Function_24_5E99",        # 18, 24
        "Function_25_5EAC",        # 19, 25
        "Function_26_5EBF",        # 1A, 26
        "Function_27_5ED2",        # 1B, 27
        "Function_28_67F9",        # 1C, 28
        "Function_29_68DD",        # 1D, 29
        "Function_30_6994",        # 1E, 30
        "Function_31_6A54",        # 1F, 31
        "Function_32_6AD0",        # 20, 32
        "Function_33_6B3F",        # 21, 33
        "Function_34_6B79",        # 22, 34
        "Function_35_6BC8",        # 23, 35
        "Function_36_6C02",        # 24, 36
        "Function_37_6C3C",        # 25, 37
        "Function_38_6C8B",        # 26, 38
        "Function_39_6CC5",        # 27, 39
        "Function_40_6CFF",        # 28, 40
        "Function_41_77F4",        # 29, 41
        "Function_42_790C",        # 2A, 42
        "Function_43_79AA",        # 2B, 43
        "Function_44_79D6",        # 2C, 44
        "Function_45_79E1",        # 2D, 45
        "Function_46_817D",        # 2E, 46
        "Function_47_819F",        # 2F, 47
        "Function_48_81C4",        # 30, 48
        "Function_49_81E9",        # 31, 49
        "Function_50_8201",        # 32, 50
        "Function_51_8219",        # 33, 51
        "Function_52_8231",        # 34, 52
        "Function_53_8249",        # 35, 53
        "Function_54_9AE8",        # 36, 54
        "Function_55_9B17",        # 37, 55
        "Function_56_9B4B",        # 38, 56
        "Function_57_9BDB",        # 39, 57
        "Function_58_9C29",        # 3A, 58
        "Function_59_9C3D",        # 3B, 59
        "Function_60_9CAE",        # 3C, 60
        "Function_61_9CBD",        # 3D, 61
        "Function_62_9D46",        # 3E, 62
        "Function_63_9D4B",        # 3F, 63
        "Function_64_9DF1",        # 40, 64
        "Function_65_9DF6",        # 41, 65
        "Function_66_9E78",        # 42, 66
        "Function_67_9F1F",        # 43, 67
        "Function_68_9FB6",        # 44, 68
        "Function_69_9FDB",        # 45, 69
        "Function_70_A000",        # 46, 70
        "Function_71_A04B",        # 47, 71
        "Function_72_A0A8",        # 48, 72
        "Function_73_A0E2",        # 49, 73
        "Function_74_A0F2",        # 4A, 74
        "Function_75_A105",        # 4B, 75
        "Function_76_A129",        # 4C, 76
        "Function_77_A14D",        # 4D, 77
        "Function_78_A171",        # 4E, 78
        "Function_79_A195",        # 4F, 79
        "Function_80_A774",        # 50, 80
        "Function_81_A7CF",        # 51, 81
        "Function_82_A7E9",        # 52, 82
        "Function_83_A806",        # 53, 83
        "Function_84_A823",        # 54, 84
        "Function_85_A83D",        # 55, 85
        "Function_86_A85A",        # 56, 86
        "Function_87_A897",        # 57, 87
        "Function_88_A898",        # 58, 88
        "Function_89_A8B3",        # 59, 89
        "Function_90_A8DE",        # 5A, 90
        "Function_91_B625",        # 5B, 91
        "Function_92_B626",        # 5C, 92
        "Function_93_BEB6",        # 5D, 93
        "Function_94_C1A4",        # 5E, 94
        "Function_95_CB16",        # 5F, 95
        "Function_96_D5C1",        # 60, 96
        "Function_97_E28E",        # 61, 97
        "Function_98_E333",        # 62, 98
        "Function_99_E389",        # 63, 99
    ))


    def Function_0_AB4(): pass

    label("Function_0_AB4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_AF4"),
        (1, "loc_B00"),
        (2, "loc_B0C"),
        (3, "loc_B18"),
        (4, "loc_B24"),
        (5, "loc_B30"),
        (6, "loc_B3C"),
        (SWITCH_DEFAULT, "loc_B48"),
    )


    label("loc_AF4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B00")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B0C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B18")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B24")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B30")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B3C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B48")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B54")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B6B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B6B")

    Return()

    # Function_0_AB4 end

    def Function_1_B6C(): pass

    label("Function_1_B6C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_BAC"),
        (1, "loc_BB8"),
        (2, "loc_BC4"),
        (3, "loc_BD0"),
        (4, "loc_BDC"),
        (5, "loc_BE8"),
        (6, "loc_BF4"),
        (SWITCH_DEFAULT, "loc_C00"),
    )


    label("loc_BAC")

    OP_A0(0xFE, 450, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_BB8")

    OP_A0(0xFE, 550, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_BC4")

    OP_A0(0xFE, 600, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_BD0")

    OP_A0(0xFE, 400, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_BDC")

    OP_A0(0xFE, 650, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_BE8")

    OP_A0(0xFE, 350, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_BF4")

    OP_A0(0xFE, 500, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_C00")

    OP_A0(0xFE, 500, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_C0C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C23")
    OP_A0(0xFE, 500, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_C23")

    Return()

    # Function_1_B6C end

    def Function_2_C24(): pass

    label("Function_2_C24")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C84")
    OP_95(0xFE, -23040, 0, -6950, 2000, 0x0)
    OP_95(0xFE, -24930, 0, -6950, 2000, 0x0)
    OP_95(0xFE, -24930, -1000, -23250, 2000, 0x0)
    OP_95(0xFE, -23040, -1000, -23250, 2000, 0x0)
    Jump("Function_2_C24")

    label("loc_C84")

    Return()

    # Function_2_C24 end

    def Function_3_C85(): pass

    label("Function_3_C85")

    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0x11, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CCC")
    ClearMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)
    SetMapObjFlags(0x8, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)

    label("loc_CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_CFF")
    ClearMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)
    SetMapObjFlags(0x8, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)

    label("loc_CFF")

    Return()

    # Function_3_C85 end

    def Function_4_D00(): pass

    label("Function_4_D00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D24")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x9, -20070, 0, -3580, 270)
    Jump("loc_E8E")

    label("loc_D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_D38")
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_E8E")

    label("loc_D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_D4C")
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_E8E")

    label("loc_D4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_D65")
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_E8E")

    label("loc_D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_DC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DA6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D9C")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_DA1")

    label("loc_D9C")

    SetChrFlags(0x8, 0x80)

    label("loc_DA1")

    Jump("loc_DAB")

    label("loc_DA6")

    SetChrFlags(0x8, 0x10)

    label("loc_DAB")

    SetChrPos(0x9, -23040, -1000, -25910, 180)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_E8E")

    label("loc_DC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DD9")
    SetChrFlags(0x9, 0x80)
    Jump("loc_E8E")

    label("loc_DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E03")
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -36570, 3000, 16290, 90)
    Jump("loc_E8E")

    label("loc_E03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E26")
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    Jump("loc_E8E")

    label("loc_E26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E49")
    SetChrFlags(0x8, 0x10)
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    Jump("loc_E8E")

    label("loc_E49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E74")
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6F")
    ClearChrFlags(0xF, 0x80)

    label("loc_E6F")

    Jump("loc_E8E")

    label("loc_E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_E8E")
    SetChrPos(0x9, -12330, -1000, -17370, 90)

    label("loc_E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 2)), scpexpr(EXPR_END)), "loc_E9C")
    ClearChrFlags(0xD, 0x80)

    label("loc_E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_EB0")
    ClearScenarioFlags(0x22, 0)
    Event(0, 41)
    Jump("loc_EED")

    label("loc_EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_EC7")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 45)
    Jump("loc_EED")

    label("loc_EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_EDE")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 0)
    Event(0, 53)
    Jump("loc_EED")

    label("loc_EDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_EED")
    ClearScenarioFlags(0x22, 3)
    Event(0, 79)

    label("loc_EED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1391")
    ClearScenarioFlags(0x38, 0)
    ClearScenarioFlags(0x38, 1)
    ClearScenarioFlags(0x38, 2)
    ClearScenarioFlags(0x38, 3)
    ClearScenarioFlags(0x38, 4)
    ClearScenarioFlags(0x38, 5)
    ClearScenarioFlags(0x38, 6)
    ClearScenarioFlags(0x38, 7)
    ClearScenarioFlags(0x39, 0)
    ClearScenarioFlags(0x39, 1)
    ClearScenarioFlags(0x39, 2)
    ClearScenarioFlags(0x39, 3)
    ClearScenarioFlags(0x39, 4)
    ClearScenarioFlags(0x39, 5)
    ClearScenarioFlags(0x39, 6)
    ClearScenarioFlags(0x39, 7)
    ClearScenarioFlags(0x3A, 0)
    ClearScenarioFlags(0x3A, 1)
    ClearScenarioFlags(0x3A, 2)
    ClearScenarioFlags(0x3A, 3)
    ClearScenarioFlags(0x3A, 4)
    ClearScenarioFlags(0x3A, 5)
    ClearScenarioFlags(0x3A, 6)
    ClearScenarioFlags(0x3A, 7)
    ClearScenarioFlags(0x3B, 0)
    ClearScenarioFlags(0x3B, 1)
    ClearScenarioFlags(0x3B, 2)
    ClearScenarioFlags(0x3B, 3)
    ClearScenarioFlags(0x3B, 4)
    ClearScenarioFlags(0x3B, 5)
    ClearScenarioFlags(0x3B, 6)
    ClearScenarioFlags(0x3B, 7)
    ClearScenarioFlags(0x3D, 5)
    ClearScenarioFlags(0x3D, 6)
    ClearScenarioFlags(0x3D, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7A")
    SetScenarioFlags(0x38, 0)

    label("loc_F7A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F90")
    SetScenarioFlags(0x38, 1)

    label("loc_F90")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA6")
    SetScenarioFlags(0x38, 2)

    label("loc_FA6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FBC")
    SetScenarioFlags(0x38, 3)

    label("loc_FBC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD2")
    SetScenarioFlags(0x38, 4)

    label("loc_FD2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE8")
    SetScenarioFlags(0x38, 5)

    label("loc_FE8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FFE")
    SetScenarioFlags(0x38, 6)

    label("loc_FFE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1014")
    SetScenarioFlags(0x38, 7)

    label("loc_1014")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102A")
    SetScenarioFlags(0x39, 0)

    label("loc_102A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1040")
    SetScenarioFlags(0x39, 1)

    label("loc_1040")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1056")
    SetScenarioFlags(0x39, 2)

    label("loc_1056")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_106C")
    SetScenarioFlags(0x39, 3)

    label("loc_106C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1082")
    SetScenarioFlags(0x39, 4)

    label("loc_1082")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1098")
    SetScenarioFlags(0x39, 5)

    label("loc_1098")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AE")
    SetScenarioFlags(0x39, 6)

    label("loc_10AE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C4")
    SetScenarioFlags(0x39, 7)

    label("loc_10C4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DA")
    SetScenarioFlags(0x3A, 0)

    label("loc_10DA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F0")
    SetScenarioFlags(0x3A, 1)

    label("loc_10F0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1106")
    SetScenarioFlags(0x3A, 2)

    label("loc_1106")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_111C")
    SetScenarioFlags(0x3A, 3)

    label("loc_111C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1132")
    SetScenarioFlags(0x3A, 4)

    label("loc_1132")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1148")
    SetScenarioFlags(0x3A, 5)

    label("loc_1148")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_115E")
    SetScenarioFlags(0x3A, 6)

    label("loc_115E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1174")
    SetScenarioFlags(0x3A, 7)

    label("loc_1174")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118A")
    SetScenarioFlags(0x3B, 0)

    label("loc_118A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A0")
    SetScenarioFlags(0x3B, 1)

    label("loc_11A0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B6")
    SetScenarioFlags(0x3B, 2)

    label("loc_11B6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11CC")
    SetScenarioFlags(0x3B, 3)

    label("loc_11CC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E2")
    SetScenarioFlags(0x3B, 4)

    label("loc_11E2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F8")
    SetScenarioFlags(0x3B, 5)

    label("loc_11F8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120E")
    SetScenarioFlags(0x3B, 6)

    label("loc_120E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1224")
    SetScenarioFlags(0x3B, 7)

    label("loc_1224")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123A")
    SetScenarioFlags(0x3D, 5)

    label("loc_123A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1250")
    SetScenarioFlags(0x3D, 6)

    label("loc_1250")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1266")
    SetScenarioFlags(0x3D, 7)

    label("loc_1266")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12A1")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1391")

    label("loc_12A1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C4")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1391")

    label("loc_12C4")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E7")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1391")

    label("loc_12E7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_130A")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1391")

    label("loc_130A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132D")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1391")

    label("loc_132D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1350")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1391")

    label("loc_1350")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1373")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1391")

    label("loc_1373")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1391")
    SetScenarioFlags(0x3C, 7)

    label("loc_1391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13A7")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13BD")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13EF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13EF")
    SetChrPos(0x0, -50230, 0, 16410, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 9)

    label("loc_13EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_1422")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1422")
    SetChrPos(0x0, -48000, 0, 17000, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_1422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_1431")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 8)

    label("loc_1431")

    Return()

    # Function_4_D00 end

    def Function_5_1432(): pass

    label("Function_5_1432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_144C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_145E")

    label("loc_144C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_145E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_145E")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1484")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1484")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_149C")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_149C")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14B4")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_14B4")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14DF")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_14DF")

    ModifyEventFlags(0, 4, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    ModifyEventFlags(0, 6, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_151B")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1516")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1516")
    ModifyEventFlags(1, 6, 0x80)

    label("loc_1516")

    Jump("loc_154C")

    label("loc_151B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_154C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 2)), scpexpr(EXPR_END)), "loc_1537")
    ModifyEventFlags(1, 5, 0x80)
    Jump("loc_154C")

    label("loc_1537")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_154C")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_154C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15D0")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x6E, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_15D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_15E7")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_15E7")

    label("loc_15E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_15F5")
    Jump("loc_1697")

    label("loc_15F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_162F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_162A")
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFrame(0xE, "light", 0x0, 0x1)
    SetMapObjFlags(0xE, 0x1000)

    label("loc_162A")

    Jump("loc_1697")

    label("loc_162F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_163D")
    Jump("loc_1697")

    label("loc_163D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_164B")
    Jump("loc_1697")

    label("loc_164B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1659")
    Jump("loc_1697")

    label("loc_1659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_166D")
    ClearMapObjFlags(0xB, 0x4)
    Jump("loc_1697")

    label("loc_166D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_168E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1689")
    ClearMapObjFlags(0xA, 0x4)

    label("loc_1689")

    Jump("loc_1697")

    label("loc_168E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1697")

    label("loc_1697")

    MiniGame(0x2F, 0x2, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x11, 0x80)
    SetMapObjFlags(0x7, 0x4)
    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, -17180, -2000, -32770, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1734")
    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)

    label("loc_1734")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_174C")
    OP_1B(0x0, 0x0, 0x61)

    label("loc_174C")

    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    Return()

    # Function_5_1432 end

    def Function_6_1757(): pass

    label("Function_6_1757")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThere is a bus stop.\x01",
            "Move by bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City South Exit\x01",             # 0
            "Crossroad Stop (Nearby Sandbank)\x01",      # 1
            "Quit\x01",                                  # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1802")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1822")

    label("loc_1802")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1822")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()

    label("loc_1822")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_6_1757 end

    def Function_7_182A(): pass

    label("Function_7_182A")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_1953")
    Fade(500)
    OP_68(-59000, 1000, 2200, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -56600, 0, 3800, 180)
    SetChrPos(0x1, -56600, 0, 4900, 180)
    SetChrPos(0x2, -56600, 0, 6000, 180)
    SetChrPos(0x3, -56600, 0, 7200, 180)
    SetMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    ClearChrFlags(0x11, 0x80)
    OP_78(0x7, 0x11)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x11, -71000, 0, 500, 90)
    OP_D5(0x11, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)

    def lambda_190A():
        OP_95(0xFE, -59000, 0, 500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_190A)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x11, 1)
    OP_71(0x7, 0x5B, 0x78, 0x1, 0x0)
    OP_79(0x7)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_1953")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_7_182A end

    def Function_8_1957(): pass

    label("Function_8_1957")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -56560, 0, 4080, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_8_1957 end

    def Function_9_197E(): pass

    label("Function_9_197E")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_19D9")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19CE")
    Sound(2502, 255, 100, 0)
    Jump("loc_19D4")

    label("loc_19CE")

    Sound(2503, 255, 100, 0)

    label("loc_19D4")

    Jump("loc_19FD")

    label("loc_19D9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19F7")
    Sound(3347, 255, 100, 0)
    Jump("loc_19FD")

    label("loc_19F7")

    Sound(3348, 255, 100, 0)

    label("loc_19FD")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_197E end

    def Function_10_1A12(): pass

    label("Function_10_1A12")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1B68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE7")

    ChrTalk(
        0x8,
        (
            "Hey now... What's that giant tree\x01",
            "emitting a bluish light?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Such a thing appearing suddenly...\x01",
            "That's absurd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I-In any case, I'll have to\x01",
            "get myself fired up and guard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B63")

    label("loc_1AE7")


    ChrTalk(
        0x8,
        (
            "Such a giant tree appearing suddenly...\x01",
            "That's absurd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I-In any case, I'll have to\x01",
            "get myself fired up and guard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B63")

    Jump("loc_2DF5")

    label("loc_1B68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1D29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C50")

    ChrTalk(
        0x8,
        (
            "Because of the declaration of invalidity about the state \x01",
            "independence, even the State Guard seems in chaos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ambulances and bus escorts\x01",
            "are being continued at present,\x01",
            "but there's much to worry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D24")

    label("loc_1C50")


    ChrTalk(
        0x8,
        (
            "Because of that declaration of invalidity about the state \x01",
            "independence, even the State Guard seems in chaos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Without the State Guard protection,\x01",
            "ambulances can't come and go,\x01",
            "so there's much to worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D24")

    Jump("loc_2DF5")

    label("loc_1D29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1F68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E8E")

    ChrTalk(
        0x8,
        (
            "Since without the State Guard protection\x01",
            "ambulances can't come and go, frankly\x01",
            "speaking it's not a good situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The "Cryptid" that appeared on the highway\x01",
            "and the mobility restriction by the State Guard...\x01",
            "These two are big problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At least, I'd like they to spare a little\x01",
            "more people for highway protection.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F63")

    label("loc_1E8E")


    ChrTalk(
        0x8,
        (
            "Since without the State Guard protection\x01",
            "ambulances can't come and go, frankly\x01",
            "speaking it's not a good situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At least I'd like the State Guard to spare\x01",
            "a little more people for highway protection.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F63")

    Jump("loc_2DF5")

    label("loc_1F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_210F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2060")

    ChrTalk(
        0x8,
        (
            "The State Guard guys were looking for\x01",
            "a fugitive criminal from the prison, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Somehow it appears that\x01",
            "they withdrew quickly.\x01",
            "I wonder what happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Oh, well.\x01",
            "At any rate, I must return to my watch.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_210A")

    label("loc_2060")


    ChrTalk(
        0x8,
        (
            "The State Guard came to look for\x01",
            "a fugitive criminal from the prison,\x01",
            "but they withdrew quickly, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Oh, well.\x01",
            "At any rate, I must return to my watch.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_210A")

    Jump("loc_2DF5")

    label("loc_210F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_24F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_234E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_22B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2215")

    ChrTalk(
        0x8,
        (
            "Oh man, trying to cheat\x01",
            "out medical goods...\x01",
            "What a bad guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Still, although it's nice\x01",
            "you took them back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If everyone knew about it\x01",
            "when they're doing their best,\x01",
            "they'd be said, you see.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22B0")

    label("loc_2215")


    ChrTalk(
        0x8,
        (
            "Oh man, trying to cheat\x01",
            "out medical goods...\x01",
            "What a bad guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If everyone knew about it\x01",
            "when they're doing their best,\x01",
            "they'd be said, you see...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22B0")

    Jump("loc_2349")

    label("loc_22B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_2349")

    ChrTalk(
        0x8,
        (
            "Oh man, cheating out\x01",
            "medical goods...\x01",
            "What a bad guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They're people in need\x01",
            "and yet he did such a thing...\x01",
            "What a scum.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2349")

    label("loc_2349")

    Jump("loc_24EF")

    label("loc_234E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244B")

    ChrTalk(
        0x8,
        (
            "That's weird, they\x01",
            "should've arrived\x01",
            "already, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0x8,
        (
            "Oh, excuse me, welcome\x01",
            "to St. Ursula Medical College.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you're here for a visit,\x01",
            "please fill the papers at\x01",
            "the lobby on the 1F ward.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_24EF")

    label("loc_244B")


    ChrTalk(
        0x8,
        (
            "Due to the recent raid incident, there has\x01",
            "been a sudden increase of patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The professors in the hospital\x01",
            "are crazily busy.\x01",
            "I too have to do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24EF")

    Jump("loc_2DF5")

    label("loc_24F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_26D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2617")

    ChrTalk(
        0x8,
        (
            "Maaan, today's raining, eh?\x01",
            "In times like this, guarding is tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even so, yesterday many\x01",
            "ambulances came in.\x01",
            "It was terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems there has been quite a big accident,\x01",
            "the fact there were no casualties can only be\x01",
            "said to have been a miracle.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26CE")

    label("loc_2617")


    ChrTalk(
        0x8,
        (
            "Yesterday many ambulances came in.\x01",
            "It was terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems there has been quite a big accident,\x01",
            "the fact there were no casualties can only be\x01",
            "said to have been a miracle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26CE")

    Jump("loc_2DF5")

    label("loc_26D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_277F")

    ChrTalk(
        0x8,
        (
            "It appears that the Bracers are\x01",
            "searching many places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems there're also rumors of\x01",
            "large-scale monsters appearing...\x01",
            "I must stay on guard too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF5")

    label("loc_277F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_28FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_287C")

    ChrTalk(
        0x8,
        "Hi, welcome to St. Ursula Medical College.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just before, Professor Seiland\x01",
            "walked to the lounge area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems that the professor \x01",
            "recently often loiters there.\x01",
            "...I wonder if she has many things to think about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28F6")

    label("loc_287C")


    ChrTalk(
        0x8,
        (
            "Lately, Professor Seiland often\x01",
            "goes out to the lounge area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...I wonder if she has many things to think about.\x02",
    )

    CloseMessageWindow()

    label("loc_28F6")

    Jump("loc_2DF5")

    label("loc_28FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_29BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2916")
    Call(0, 15)
    Jump("loc_29B6")

    label("loc_2916")


    ChrTalk(
        0x8,
        (
            "Ah, that time it seems the cause\x01",
            "was Xilun making a mistake in\x01",
            "filling the order papers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At any rate, I think there\x01",
            "won't be any problem this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29B6")

    Jump("loc_2DF5")

    label("loc_29BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2BFD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2A5A")

    ChrTalk(
        0x8,
        (
            "The Archduke Albert's limousine\x01",
            "went back some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Maaan, I was tense, but...\x01",
            "I'm glad I could welcome\x01",
            "him properly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF8")

    label("loc_2A5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B48")

    ChrTalk(
        0x8,
        (
            "Archduke Albert of Remiferia\x01",
            "is here to observe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Maaan, I had heard about this\x01",
            "in advance, but when it came to\x01",
            "welcome him, I was super tense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Until he goes back home, I mustn't\x01",
            "do any discourtesy to him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BF8")

    label("loc_2B48")


    ChrTalk(
        0x8,
        (
            "Maaan, I had heard about this\x01",
            "in advance, but when it came to\x01",
            "welcome him, I was super tense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Until the Archduke goes back home,\x01",
            "I mustn't do any discourtesy to him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BF8")

    Jump("loc_2DF5")

    label("loc_2BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2DF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D25")

    ChrTalk(
        0x8,
        (
            "Hi, good morning. This is the\x01",
            "Saint Ursula Medical College Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since it's long, many persons shortens it to\x01",
            ""St. Ursula Hospital" or "St. Ursula Medical College".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, the reception for medical examinations\x01",
            "or visits is in the building in the back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2DF5")

    label("loc_2D25")


    ChrTalk(
        0x8,
        (
            "Even the wound when I was shot during \x01",
            "the Cult incident was completely cured\x01",
            "by a doctor working here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The medical technology, pride of St. Ursula\x01",
            "Medical College, is truly great! ...Just kidding.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DF5")

    TalkEnd(0xFE)
    Return()

    # Function_10_1A12 end

    def Function_11_2DF9(): pass

    label("Function_11_2DF9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_305C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F89")

    ChrTalk(
        0x9,
        (
            "it seems that the State Guard has assigned\x01",
            "people to escort the ambulances and buses\x01",
            "that come and go on the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The people who got injured in the strife in the city\x01",
            "and those too who could not come to the hospital\x01",
            "for a while they're now considerably coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even Miss Eolia, the Bracer,\x01",
            "has come to help us... Maybe\x01",
            "for now the hospital is secure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3057")

    label("loc_2F89")


    ChrTalk(
        0x9,
        (
            "Even Miss Eolia, the Bracer,\x01",
            "has come to help us... Maybe\x01",
            "for now the hospital is secure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, after that giant tree appeared,\x01",
            "anxiety is spreading to the patients.\x01",
            "I too must do all my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3057")

    Jump("loc_3CC8")

    label("loc_305C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_321E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_317D")

    ChrTalk(
        0x9,
        (
            "The hospitalized patients seem very worried\x01",
            "about their families that are in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since we're in a situation we can't easily communicate \x01",
            "with the outside we can't do anything but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In a way or another we must\x01",
            "relieve the patients' worries.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3219")

    label("loc_317D")


    ChrTalk(
        0x9,
        (
            "The hospitalized patients seem very worried\x01",
            "about their families that are in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In a way or another we must\x01",
            "relieve the patients' worries.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3219")

    Jump("loc_3CC8")

    label("loc_321E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3374")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32FF")

    ChrTalk(
        0x9,
        (
            "I esteem the younger brother and his friends decisions \x01",
            "more than those of the State Guard and the President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Please be safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Also, don't cause too much\x01",
            "worries for senior Cecil, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_336F")

    label("loc_32FF")


    ChrTalk(
        0x9,
        (
            "Please be safe, younger\x01",
            "brother and friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Also, don't cause too much\x01",
            "worries for senior Cecil, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_336F")

    Jump("loc_3CC8")

    label("loc_3374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_34CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_347C")

    ChrTalk(
        0x9,
        (
            "It seems that the younger brother and his friends\x01",
            "have been fighting the State Guard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Uuhm, no,\x01",
            "don't worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No matter what happens, we support\x01",
            "the younger brother and his friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F...Thank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_34C9")

    label("loc_347C")


    ChrTalk(
        0x9,
        (
            "No matter what happens, we support\x01",
            "the younger brother and his friends.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34C9")

    Jump("loc_3CC8")

    label("loc_34CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_35B0")

    ChrTalk(
        0x9,
        (
            "Due to that incident, quite many\x01",
            "patients were brought in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We can't really keep up with the treatments...\x01",
            "We're in a situation where there're many people\x01",
            "who need surgery who're waiting for their turn.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CC8")

    label("loc_35B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_35BE")
    Jump("loc_3CC8")

    label("loc_35BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_36F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36AE")

    ChrTalk(
        0x9,
        (
            "Shizuku seems to be quite positive\x01",
            "towards that surgery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That child doesn't give up, so\x01",
            "we who are around her must\x01",
            "not be pessimistic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Yes, we too have to believe\x01",
            "in its success and do our best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_36F4")

    label("loc_36AE")


    ChrTalk(
        0x9,
        (
            "We too must believe in\x01",
            "Shizuku's full recovery \x01",
            "and do our best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36F4")

    Jump("loc_3CC8")

    label("loc_36F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3817")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37BE")

    ChrTalk(
        0x9,
        (
            "Because it's Professor Seiland,\x01",
            "they say she could do such a\x01",
            "surgery, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Shizuku...\x01",
            "Maybe with the current medical technology\x01",
            "she can't be fully cured.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3812")

    label("loc_37BE")


    ChrTalk(
        0x9,
        (
            "Shizuku...\x01",
            "Maybe with the current medical technology\x01",
            "she can't be fully cured.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3812")

    Jump("loc_3CC8")

    label("loc_3817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3958")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38CD")

    ChrTalk(
        0x9,
        (
            "It appears that the Trade Conference\x01",
            "is going to be held today, at last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What conference could it be, I wonder.\x01",
            "I have to properly check it out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3953")

    label("loc_38CD")


    ChrTalk(
        0x9,
        (
            "But both Filia and Ran\x01",
            "seem to not be interested...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What conference could it be, I wonder.\x01",
            "I have to properly check it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3953")

    Jump("loc_3CC8")

    label("loc_3958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3AEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A78")

    ChrTalk(
        0x9,
        (
            "Some time ago, Archduke Albert\x01",
            "came to greet me in person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Being the sovereign of a whole country,\x01",
            "I arbitrarily thought him to be a man \x01",
            "with a air of importance, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Speaking to a nurse like me,\x01",
            "he seems he's unexpectedly\x01",
            "a sociable person.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3AE7")

    label("loc_3A78")


    ChrTalk(
        0x9,
        (
            "Archduke Albert seems to\x01",
            "unexpectedly be a sociable person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Uh uh, I felt a strong\x01",
            "affinity raising.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AE7")

    Jump("loc_3CC8")

    label("loc_3AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3CC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C67")

    ChrTalk(
        0x9,
        (
            "Oh, Mr. Randy and the younger brother.\x01",
            "Long time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F("Younger brother", eh...?\x01",
            "They really labeled me like that...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHa ha, have dear Ada and\x01",
            "the others been well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes, Filia and Ran too\x01",
            "are the same as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You seem to have got\x01",
            "some new members...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If we get the chance, let's\x01",
            "go have some fun again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 4)
    Jump("loc_3CC8")

    label("loc_3C67")


    ChrTalk(
        0x9,
        "Uh uh, I'm happy to see you again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If we get the chance, let's\x01",
            "go have some fun again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CC8")

    TalkEnd(0xFE)
    Return()

    # Function_11_2DF9 end

    def Function_12_3CCC(): pass

    label("Function_12_3CCC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3CDD")
    Jump("loc_4504")

    label("loc_3CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3CEB")
    Jump("loc_4504")

    label("loc_3CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3CF9")
    Jump("loc_4504")

    label("loc_3CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3EF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E25")

    ChrTalk(
        0xA,
        (
            "Many of the equipments we use at\x01",
            "the hospital were mainly purchased\x01",
            "from a merchant called Harold, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now we're entirely relying\x01",
            "on the State Guard supplies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't say they're good quality, but the situation \x01",
            "is this and we can't do anything about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3EF1")

    label("loc_3E25")


    ChrTalk(
        0xA,
        (
            "For many of the equipments we're using at the hospital\x01",
            "we're relying on the State Guard supplies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't say they're good quality, but the situation \x01",
            "is this and we can't do anything about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EF1")

    Jump("loc_4504")

    label("loc_3EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_40CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_401F")

    ChrTalk(
        0xA,
        (
            "A raid in Crossbell City...\x01",
            "A really absurd incident\x01",
            "has happened, hm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although it's been about one week since then,\x01",
            "I still can't wipe out the shock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although the reconstruction is advancing,\x01",
            "I wonder if Crossbell will be able to\x01",
            "regain its footing...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_40C9")

    label("loc_401F")


    ChrTalk(
        0xA,
        (
            "Although the reconstruction is advancing,\x01",
            "I think the shock for the raid incident\x01",
            "is really great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wonder of Crossbell will be \x01",
            "able to regain its footing...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40C9")

    Jump("loc_4504")

    label("loc_40CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_40DC")
    Jump("loc_4504")

    label("loc_40DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4158")

    ChrTalk(
        0xA,
        (
            "This container...\x01",
            "Heaps of spirits warding dolls\x01",
            "come out from it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...Why such things\x01",
            "are in there?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4504")

    label("loc_4158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_42C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4248")

    ChrTalk(
        0xA,
        (
            "They say that the independence\x01",
            "proposal is the city hot topic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "For a Crossbell citizen,\x01",
            "it can be said to be his\x01",
            "dearest wish, in a certain sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I too am completely in favor\x01",
            "for the independence.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_42BD")

    label("loc_4248")


    ChrTalk(
        0xA,
        (
            "I too am completely in favor\x01",
            "for the independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I must remember to participate\x01",
            "at the local referendum.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42BD")

    Jump("loc_4504")

    label("loc_42C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_42D0")
    Jump("loc_4504")

    label("loc_42D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_44FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_441C")

    ChrTalk(
        0xA,
        (
            "It is said that in the Principality of\x01",
            "Remiferia the Archduke family puts\x01",
            "special effort in the medical care field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Remiferia, the medical care advanced country.\x01",
            "You too have heard about it, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Uhhm, it seems it would be nice\x01",
            "to live in such a country without\x01",
            "worrying about illnesses.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_44F6")

    label("loc_441C")


    ChrTalk(
        0xA,
        (
            "It is said that in the Principality of\x01",
            "Remiferia the Archduke family puts\x01",
            "special effort in the medical care field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Uhhm, it seems it would be nice\x01",
            "to live in such a country without\x01",
            "worrying about illnesses.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44F6")

    Jump("loc_4504")

    label("loc_44FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4504")

    label("loc_4504")

    TalkEnd(0xFE)
    Return()

    # Function_12_3CCC end

    def Function_13_4508(): pass

    label("Function_13_4508")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_464B")

    ChrTalk(
        0xB,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FProfessor Seiland...?\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x0, 500)

    ChrTalk(
        0xB,
        "...Ah, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm sorry, but now I'm busy.\x01",
            "Could you leave me alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F(As I thought, maybe she's\x01",
            "worried about Shizuku's surgery...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Yeah, she was the\x01",
            "operating surgeon...)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0xB4, 0x0)
    SetScenarioFlags(0x0, 4)
    Jump("loc_46B0")

    label("loc_464B")


    ChrTalk(
        0xB,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(It looks like she's deep in thought.\x01",
            "...Disturbing her would be bad.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46B0")

    TalkEnd(0xFE)
    Return()

    # Function_13_4508 end

    def Function_14_46B4(): pass

    label("Function_14_46B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46C9")
    Call(0, 15)
    Jump("loc_476F")

    label("loc_46C9")


    ChrTalk(
        0xC,
        (
            "#03605FBy the way...\x01",
            "Were you fine with a quantity\x01",
            "of 30 sheets this time?\x02\x03",
            "#03600FBefore, it happened that\x01",
            "I was ordered 500 instead\x01",
            "of 50, so, just in case...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_476F")

    TalkEnd(0xFE)
    Return()

    # Function_14_46B4 end

    def Function_15_4773(): pass

    label("Function_15_4773")

    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x8,
        (
            "Hey, if it isn't Harold.\x01",
            "What've you come for today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#03600FWell, I came to deliver\x01",
            "the sheets I was ordered.\x02\x03",
            "I'd like to deliver the goods immediately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, then I guess I'll give you a\x01",
            "little help with carrying them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#03609FHa ha, thank you for always helping me.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_15_4773 end

    def Function_16_48A9(): pass

    label("Function_16_48A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4A2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_499F")

    ChrTalk(
        0xFE,
        (
            "Thank goodness I could safely \x01",
            "deliver the medical goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so...\x01",
            "In such a time of crisis for Crossbell,\x01",
            "to think there was such a nasty guy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A-Although now that he's \x01",
            "caught I feel relieved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4A2A")

    label("loc_499F")


    ChrTalk(
        0xFE,
        (
            "In such a time of crisis for Crossbell,\x01",
            "to think there was such a nasty guy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A-Although now that he's \x01",
            "caught I feel relieved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A2A")

    Jump("loc_4BA2")

    label("loc_4A2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_4BA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B24")

    ChrTalk(
        0xFE,
        (
            "Shit, to not being able to deliver medical\x01",
            "goods in this time of crisis...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, no use in complaining\x01",
            "on what's been done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You all too, don't mind it, change your\x01",
            "way of thinking and do your job.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4BA2")

    label("loc_4B24")


    ChrTalk(
        0xFE,
        (
            "No use in complaining\x01",
            "on what's been done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You all too, don't mind it, change your\x01",
            "way of thinking and do your job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BA2")

    TalkEnd(0xFE)
    Return()

    # Function_16_48A9 end

    def Function_17_4BA6(): pass

    label("Function_17_4BA6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4C39")

    ChrTalk(
        0xF,
        (
            "This is Archduke Albert's\x01",
            "private limousine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Mr. Arios is accompanying\x01",
            "His Grace as a bodyguard,\x01",
            "so even I can stay assured.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C39")

    TalkEnd(0xFE)
    Return()

    # Function_17_4BA6 end

    def Function_18_4C3D(): pass

    label("Function_18_4C3D")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C6F")
    SetScenarioFlags(0x31, 2)

    label("loc_4C6F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4CB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_4CAF")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4CA4")
    Sound(2499, 255, 100, 0)
    Jump("loc_4CAA")

    label("loc_4CA4")

    Sound(3537, 255, 100, 0)

    label("loc_4CAA")

    Jump("loc_4CB5")

    label("loc_4CAF")

    Sound(3344, 255, 100, 0)

    label("loc_4CB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_4D28")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4D08"),
        (SWITCH_DEFAULT, "loc_4D19"),
    )


    label("loc_4D08")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_4D23")

    label("loc_4D19")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D23")

    Jump("loc_4F63")

    label("loc_4D28")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_4D5A")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_4D5A")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4D8C"),
        (1, "loc_4E90"),
        (2, "loc_4F21"),
        (SWITCH_DEFAULT, "loc_4F59"),
    )


    label("loc_4D8C")

    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4DBD")
    OP_70(0x8, 0x12C)
    OP_71(0x8, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_4DCD")

    label("loc_4DBD")

    OP_70(0x8, 0xF0)
    OP_71(0x8, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_4DCD")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E23")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E23")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E46")
    Sound(461, 0, 100, 0)

    label("loc_4E46")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4E66")
    OP_70(0x8, 0x14A)
    OP_71(0x8, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_4E76")

    label("loc_4E66")

    OP_70(0x8, 0x10E)
    OP_71(0x8, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_4E76")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x8, "light", 0x1, 0x1)
    OP_70(0x8, 0x0)
    Jump("loc_4CB5")

    label("loc_4E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_4F02")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_4EC5")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_4EDD")

    label("loc_4EC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4ED8")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_4EDD")

    label("loc_4ED8")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_4EDD")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F1C")

    label("loc_4F02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4F12")
    OP_AF(0xFB)
    Jump("loc_4F1C")

    label("loc_4F12")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F1C")

    Jump("loc_4F63")

    label("loc_4F21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F3A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F54")

    label("loc_4F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4F4A")
    OP_AF(0xFB)
    Jump("loc_4F54")

    label("loc_4F4A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F54")

    Jump("loc_4F63")

    label("loc_4F59")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F63")

    Jump("loc_4CB5")

    label("loc_4F68")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_18_4C3D end

    def Function_19_4F76(): pass

    label("Function_19_4F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4FC6")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems the orbal bus service is not running.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_4FC6")

    Call(0, 6)
    Return()

    # Function_19_4F76 end

    def Function_20_4FCA(): pass

    label("Function_20_4FCA")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FIt seems I can fish here.\x02",
    )

    CloseMessageWindow()
    OP_68(-17220, 0, -31290, 1500)
    MoveCamera(60, 36, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(22000, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish \x01",      # 0
            "Quit\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_508A")
    OP_E2(0x2)
    MiniGame(0x6, 0x11, 0xFFFFBFBE, 0xFFFFFC18, 0xFFFF9A5C, 0xB4, 0xFFFFBCE4, 0xFFFFF830, 0xFFFF7FFE)

    label("loc_508A")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_20_4FCA end

    def Function_21_508F(): pass

    label("Function_21_508F")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    SetChrPos(0x101, -47420, 0, 290, 270)
    SetChrPos(0x102, -46710, 0, -820, 270)
    SetChrPos(0x104, -46010, 0, 1050, 270)
    SetChrPos(0x105, -44880, 0, -1000, 270)
    SetChrPos(0x109, -44460, 0, 420, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-45000, 1000, 0, 0)
    MoveCamera(33, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21160, 0)
    OP_68(-54310, 1000, 260, 4500)
    BeginChrThread(0x101, 0, 0, 22)
    BeginChrThread(0x102, 0, 0, 23)
    BeginChrThread(0x104, 0, 0, 24)
    BeginChrThread(0x105, 0, 0, 25)
    BeginChrThread(0x109, 0, 0, 26)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3000)
    Sound(803, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitChrThread(0x101, 0)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005F#5POh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    def lambda_5210():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5210)

    ChrTalk(
        0x102,
        "#00105F#12PMaybe a call from another post?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
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
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000F#30WYes, Special Support Section,\x01",
            "Lloyd Bannings speaking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Husky Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Uhuhu...\x01",
            "It's me, me.\x02\x03",
            "Can you tell who I am?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00012FMr. Michel...\x01",
            "Ehhm, is something wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Michel's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Uhuhu, getting it right immediately...\x01",
            "Aren't you quite skillful?\x02\x03",
            "Or could it be none other than love?\x02",
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
            "#00006FNo, it's just that there's no other than you \x01",
            "Mr. Michel who could I've thought of.\x02\x03",
            "#00000FCould it be about KeA\x01",
            "who came there?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Michel's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, that's right.\x02\x03",
            "That child went to play at the\x01",
            "Waterfront Area with Shizuku.\x02\x03",
            "Zeit...I think he's called?\x01",
            "Since they're together with that\x01",
            "police dog, I think they're fine.\x02",
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
            "#00002FYeah, if Zeit is with them, I think\x01",
            "there's nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Michel's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "My, really?\x02\x03",
            "I heard stories about him,\x01",
            "he looks very dignified.\x02\x03",
            "Not for nothing it's said to be\x01",
            "a legendary "Divine Wolf", eh?\x02",
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
            "#00004FHa ha...as you'd expect, I think a\x01",
            "legendary wolf would be different.\x02\x03",
            "#00005FAh, did you call on purpose\x01",
            "to inform us about this?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Michel's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No, I'll tell you the main point now.\x02\x03",
            "Actually, it seems that Arios wants\x01",
            "to exchange information with you.\x02\x03",
            "He'll be back by evening, so\x01",
            "could you somehow have time?\x02",
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
            "#00000FEvening...?\x01",
            "I think it's fine.\x02\x03",
            "About the information exchange, does\x01",
            "he mean about the Trade Conference?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Michel's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "That too, but also...regarding the\x01",
            ""Heiyue" and the "Red Constellation".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003F...Understood.\x02\x03",
            "#00001FWhen we finish our business,\x01",
            "we'll come over there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Michel's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "All right, we'll be waiting.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)

    ChrTalk(
        0x102,
        (
            "#00100F#12PIt seemed from Mr. Michel\x01",
            "of the Bracer Guild, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#11PSomething happened?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        "#00006F#5PNo, it was an information exchange offer.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained to the other\x01",
            "members what Michel wanted.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00303F#11P"Heiyue" and the "Red Constellation"...?\x02\x03",
            "#00301FIt's true that someone like ol' man Arios could\x01",
            "be well informed about the autonomous state too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PUh uh, we could bite at the chance.\x02\x03",
            "#10300FSo then, should we go\x01",
            "back to Crossbell now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#5PNo, it seems that Mr. Arios\x01",
            "will be back in the evening.\x02\x03",
            "Until then, it should be fine\x01",
            "to finish our business.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D2A")

    ChrTalk(
        0x102,
        (
            "#00104F#12PWe could gather some information\x01",
            "about the "Red Constellation", but...\x02\x03",
            "#00102FSince we have a car, it seems it would\x01",
            "be better to go around some more places.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DDD")

    label("loc_5D2A")


    ChrTalk(
        0x102,
        (
            "#00103F#12PWe haven't gathered that much information\x01",
            "about the "Red Constellation"...\x02\x03",
            "#00100FSince we have a car, it seems it would\x01",
            "be better to go around some more places.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DDD")


    ChrTalk(
        0x109,
        (
            "#10100F#11PThen, let's go to the Guild in East\x01",
            "Street after we finish our business.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, -55000, 0, -250, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x140, 2)
    OP_29(0xA3, 0x1, 0x6)
    ModifyEventFlags(0, 0, 0x80)
    OP_24(0x323)
    EventEnd(0x5)
    Return()

    # Function_21_508F end

    def Function_22_5E76(): pass

    label("Function_22_5E76")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_22_5E76 end

    def Function_23_5E86(): pass

    label("Function_23_5E86")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_23_5E86 end

    def Function_24_5E99(): pass

    label("Function_24_5E99")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_24_5E99 end

    def Function_25_5EAC(): pass

    label("Function_25_5EAC")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_25_5EAC end

    def Function_26_5EBF(): pass

    label("Function_26_5EBF")

    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_26_5EBF end

    def Function_27_5ED2(): pass

    label("Function_27_5ED2")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch29700.itc", 0x1E)
    LoadChrToIndex("chr/ch29900.itc", 0x20)
    LoadChrToIndex("chr/ch29400.itc", 0x21)
    LoadChrToIndex("chr/ch32800.itc", 0x22)
    LoadChrToIndex("chr/ch23000.itc", 0x23)
    LoadChrToIndex("chr/ch21000.itc", 0x24)
    LoadChrToIndex("chr/ch20000.itc", 0x25)
    LoadChrToIndex("chr/ch23300.itc", 0x26)
    LoadChrToIndex("chr/ch20400.itc", 0x27)
    LoadChrToIndex("chr/ch21200.itc", 0x28)
    LoadChrToIndex("chr/ch20900.itc", 0x29)
    LoadChrToIndex("chr/ch20500.itc", 0x2A)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x20)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x21)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x22)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x23)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x24)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x25)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x26)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x27)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x28)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x24, 0x29)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x2A)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x2, 0x1000)
    OP_68(-18000, 6000, 1300, 0)
    MoveCamera(55, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(33000, 0)
    OP_68(-18000, 1000, 1300, 10000)
    MoveCamera(45, 25, 0, 10000)
    SetCameraDistance(35000, 10000)
    SetChrPos(0x1A, -5000, 1000, -1750, 270)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x1B, 5000, 1000, 1750, 270)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x1C, -24000, 0, 14000, 180)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x1D, -24000, 0, -7000, 180)
    SetChrPos(0x1E, -16500, 0, -500, 90)
    SetChrPos(0x1F, -17000, 0, 500, 90)
    SetChrPos(0x20, -22000, 0, 0, 90)
    SetChrPos(0x21, -25500, 0, -300, 90)
    SetChrPos(0x22, -34000, 0, 700, 90)
    SetChrPos(0x23, -38000, 0, -500, 90)
    SetChrPos(0x24, -37500, 0, 500, 90)
    SetChrPos(0x25, -40000, 0, -750, 90)
    BeginChrThread(0x1A, 1, 0, 28)
    BeginChrThread(0x1C, 1, 0, 30)
    BeginChrThread(0x1E, 1, 0, 32)
    BeginChrThread(0x1F, 1, 0, 33)
    BeginChrThread(0x20, 1, 0, 34)
    BeginChrThread(0x21, 1, 0, 35)
    BeginChrThread(0x22, 1, 0, 36)
    BeginChrThread(0x23, 1, 0, 37)
    BeginChrThread(0x24, 1, 0, 38)
    BeginChrThread(0x25, 1, 0, 39)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1C, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x21, 0x1)
    EndChrThread(0x22, 0x1)
    EndChrThread(0x23, 0x1)
    EndChrThread(0x24, 0x1)
    EndChrThread(0x25, 0x1)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    OP_64(0x1A)
    OP_64(0x1B)
    OP_64(0x1C)
    OP_64(0x1D)
    OP_71(0x1, 0x5, 0x5, 0x0, 0x8)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    OP_71(0x2, 0xA, 0xA, 0x0, 0x8)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    SetChrPos(0x101, -34900, 0, -950, 90)
    SetChrPos(0x102, -34900, 0, 450, 90)
    SetChrPos(0x103, -36500, 0, -1700, 90)
    SetChrPos(0x104, -36500, 0, 1200, 90)
    SetChrPos(0x109, -38100, 0, -1150, 90)
    SetChrPos(0x105, -38100, 0, 650, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-35310, 1100, -350, 0)
    MoveCamera(38, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_68(-36310, 1100, -350, 3000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x103,
        (
            "#00208F#6PAs expected, it seems there are many\x01",
            "more visitors than in normal times...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6368():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6368)
    Sleep(150)

    def lambda_6378():
        OP_93(0xFE, 0x10F, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6378)
    Sleep(100)

    def lambda_6388():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6388)
    Sleep(50)

    def lambda_6398():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6398)
    Sleep(50)

    def lambda_63A8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_63A8)
    Sleep(50)

    def lambda_63B8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_63B8)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x102,
        (
            "#00106F#11PYes, after all there have been many people\x01",
            "who were seriously injured in the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11P...Inspector Donovan and Miss\x01",
            "Ilya too are hospitalized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6PYes...they both seem to be\x01",
            "still in a comatose state.\x02\x03",
            "#10108FInspector Donovan...\x01",
            "It seems he protected Fran and the others.\x02\x03",
            "I think that the fact Fran's recovery was\x01",
            "quick has been thanks to the Inspector.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PQuite the largehearted ol' man...\x01",
            "Impressive.\x02\x03",
            "#00308FIf possible, it would be nice to go look\x01",
            "at his condition, and Miss Ilya's too...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 4)), scpexpr(EXPR_END)), "loc_6662")

    ChrTalk(
        0x102,
        (
            "#00103F#11PRight...\x01",
            "Today, it seems Sully\x01",
            "came to visit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_667B")

    label("loc_6662")


    ChrTalk(
        0x102,
        "#00103F#11PRight...\x02",
    )

    CloseMessageWindow()

    label("loc_667B")


    def lambda_6680():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_6680)
    Sleep(250)

    ChrTalk(
        0x105,
        (
            "#10300F#5PSo, where's your\x01",
            "younger sister's room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#6PAh, yes...it's 301.\x02\x03",
            "#10100FBefore we go there, it should be better\x01",
            "to say some words to the reception.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PUnderstood, let's go.\x02\x03",
            "#00003F(...Probably sister Cecil too\x01",
            "is considerably busy.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_D7(0x28)
    OP_D7(0x29)
    OP_D7(0x2A)
    SetChrPos(0x0, -38500, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x180, 5)
    OP_29(0xAC, 0x1, 0x2)
    ModifyEventFlags(0, 1, 0x80)
    EventEnd(0x5)
    Return()

    # Function_27_5ED2 end

    def Function_28_67F9(): pass

    label("Function_28_67F9")

    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_6815():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6815)
    OP_95(0xFE, -22000, 0, -1750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, -3750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, -9000, 4000, 0x0)
    Sleep(500)
    BeginChrThread(0x1D, 1, 0, 31)
    OP_95(0xFE, -24000, 0, -3750, 4000, 0x0)
    OP_95(0xFE, -22000, 0, -1750, 4000, 0x0)
    OP_95(0xFE, 2000, 0, -1750, 4000, 0x0)

    def lambda_68A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_68A7)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_28_67F9 end

    def Function_29_68DD(): pass

    label("Function_29_68DD")

    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_68F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_68F9)
    OP_95(0xFE, -22000, 0, 1750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, 3750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, 11000, 4000, 0x0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x1)

    def lambda_695B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_695B)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_64(0xFE)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_29_68DD end

    def Function_30_6994(): pass

    label("Function_30_6994")

    Sleep(1000)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_69C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_69C8)
    OP_95(0xFE, -24000, 0, 3500, 4000, 0x0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x8)
    OP_95(0xFE, -22000, 0, 1500, 4000, 0x0)
    OP_95(0xFE, 2000, 0, 1500, 4000, 0x0)

    def lambda_6A21():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6A21)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_64(0xFE)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0x1B, 1, 0, 29)
    Return()

    # Function_30_6994 end

    def Function_31_6A54(): pass

    label("Function_31_6A54")

    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, -24000, 0, -3500, 4000, 0x0)
    OP_95(0xFE, -22000, 0, -1500, 4000, 0x0)
    OP_95(0xFE, 2000, 0, -1500, 4000, 0x0)

    def lambda_6AAC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6AAC)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_64(0xFE)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_31_6A54 end

    def Function_32_6AD0(): pass

    label("Function_32_6AD0")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x960, 0x0)
    OP_93(0xFE, 0x10E, 0x3E8)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x3E8)
    OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x960, 0x0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x2)

    def lambda_6B1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6B1E)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x9C4, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_32_6AD0 end

    def Function_33_6B3F(): pass

    label("Function_33_6B3F")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0x6D6, 0x0)

    def lambda_6B58():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6B58)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x6D6, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_33_6B3F end

    def Function_34_6B79(): pass

    label("Function_34_6B79")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0x3E8, 0x0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x2)

    def lambda_6BA7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6BA7)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x3E8, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_34_6B79 end

    def Function_35_6BC8(): pass

    label("Function_35_6BC8")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x6F54, 0x3E8, 0x0)

    def lambda_6BE1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6BE1)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x3E8, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_35_6BC8 end

    def Function_36_6C02(): pass

    label("Function_36_6C02")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x8CA0, 0x5DC, 0x0)

    def lambda_6C1B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6C1B)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x5DC, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_36_6C02 end

    def Function_37_6C3C(): pass

    label("Function_37_6C3C")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x9858, 0x578, 0x0)

    def lambda_6C55():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6C55)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x578, 0x0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_37_6C3C end

    def Function_38_6C8B(): pass

    label("Function_38_6C8B")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x9858, 0x44C, 0x0)

    def lambda_6CA4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6CA4)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x44C, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_38_6C8B end

    def Function_39_6CC5(): pass

    label("Function_39_6CC5")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0xA028, 0x44C, 0x0)

    def lambda_6CDE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6CDE)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x4B0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_39_6CC5 end

    def Function_40_6CFF(): pass

    label("Function_40_6CFF")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(-46690, 1000, -40, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19720, 0)
    SetChrPos(0x101, -45000, 0, -700, 270)
    SetChrPos(0x102, -45000, 0, 700, 270)
    SetChrPos(0x103, -43500, 0, -700, 270)
    SetChrPos(0x104, -43500, 0, 700, 270)
    SetChrPos(0x109, -42000, 0, -700, 270)
    SetChrPos(0x105, -42000, 0, 700, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_6E01():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6E01)
    Sleep(100)

    def lambda_6E19():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6E19)
    Sleep(50)

    def lambda_6E31():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6E31)
    Sleep(50)

    def lambda_6E49():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6E49)
    Sleep(50)

    def lambda_6E61():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6E61)
    Sleep(50)

    def lambda_6E79():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6E79)
    OP_68(-48920, 1000, -570, 2700)
    SetCameraDistance(19720, 2700)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_6ED3():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6ED3)
    Sleep(300)

    def lambda_6EE3():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6EE3)
    Sleep(300)

    def lambda_6EF3():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6EF3)
    Sleep(300)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FYes, Special Support Section,\x01",
            "Lloyd Bannings speaking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Boy's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ah, there you're.\x02\x03",
            "We're you now?\x02",
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
            "#00003FListen...\x01",
            "In such a time, wouldn't it be courtesy\x01",
            "to properly give one's name?\x02\x03",
            "#00000FSt. Ursula Hospital...\x01",
            "What's wrong, Jona?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If I remember correctly, you got\x01",
            "back to the SSS today, right?\x02\x03",
            "So I thought if you couldn't listen\x01",
            "to one small request...?\x02",
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
            "#00006FWell, like I told you, don't peep into\x01",
            "the police database as you please...\x02\x03",
            "#00001FAlso, we're quite\x01",
            "busy too, so──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hhmm, say, who did help you\x01",
            "before with the missing\x01",
            "Bracers investigation...?\x02\x03",
            "You said you'd have returned the favor, huh?\x02",
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
            "#00013FUrgh...\x02\x03",
            "#00006F...It can't be helped.\x01",
            "We can't accept whatever you ask us,\x01",
            "but we'll at least hear you out.\x02\x03",
            "#00000FWhere should we go?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Then come in front of the lighthouse\x01",
            "at the Waterfront Area.\x02\x03",
            "I'll wait there for you♪\x02",
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
            "#00005FThe lighthouse?\x01",
            "Why at such a place...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hhmm, it's gonna be a surprise.\x02\x03",
            "Then, I'll be waiting.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(813, 0, 70, 0)
    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011F#2PAh...jeez.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00211F#11PHas Jona made a selfish\x01",
            "request again?\x02",
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
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(150)
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        "#00012F#6PNo, well...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd told them they were called in front of the \x01",
            "lighthouse at the Waterfront Area jetty.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00305F#5PHuh?\x01",
            "Why at such a place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#11PThe Waterfront Area lighthouse...\x01",
            "It's rather close to the\x01",
            "destroyed "Heiyue" building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#5PIt's true that he helped us with the\x01",
            "search for Miss Ling and Miss Eolia...\x02\x03",
            "#00100FI think it would be all right\x01",
            "at least hearing him out...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#11PWhy don't we go immediately\x01",
            "after taking our break?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYeah, let's.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PWell, he asked a selfish thing\x01",
            "without considering our position.\x02\x03",
            "#00211FEven if we make him wait a\x01",
            "little, it won't be a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#5PHa ha, you're right.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, -51000, 0, -700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x181, 2)
    OP_29(0xAC, 0x1, 0x7)
    ModifyEventFlags(0, 2, 0x80)
    OP_24(0x323)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_40_6CFF end

    def Function_41_77F4(): pass

    label("Function_41_77F4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    Call(0, 42)
    Call(0, 43)
    Call(0, 44)
    OP_68(-55000, 800, -300, 0)
    MoveCamera(71, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(32200, 0)
    FadeToBright(1000, 0)
    OP_68(-52000, 800, -300, 4000)
    MoveCamera(71, 19, 0, 4000)
    OP_6E(500, 4000)
    SetCameraDistance(26800, 4000)
    OP_0D()
    OP_6F(0x79)
    SetMessageWindowPos(14, 280, -1, 3)

    AnonymousTalk(
        0x101,
        "#00013F(A State Guard unit...)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10401F(Are they on guard...?\x01",
            "The timing was bad.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("r1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_41_77F4 end

    def Function_42_790C(): pass

    label("Function_42_790C")

    LoadChrToIndex("apl/ch51616.itc", 0x1E)
    LoadChrToIndex("apl/ch51617.itc", 0x1F)
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x12, -50960, 0, 750, 225)
    SetChrPos(0x13, -53240, 0, 680, 135)
    SetChrPos(0x14, -53040, 0, -1550, 43)
    SetChrPos(0x15, -51030, 0, -1630, 315)
    Return()

    # Function_42_790C end

    def Function_43_79AA(): pass

    label("Function_43_79AA")

    OP_74(0xD, 0x1E)
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    SetMapObjFrame(0xD, "mark00", 0x0, 0x1)
    Return()

    # Function_43_79AA end

    def Function_44_79D6(): pass

    label("Function_44_79D6")

    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    Return()

    # Function_44_79D6 end

    def Function_45_79E1(): pass

    label("Function_45_79E1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00051.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03151.itc", 0x23)
    LoadChrToIndex("chr/ch02750.itc", 0x24)
    LoadChrToIndex("chr/ch02751.itc", 0x25)
    LoadChrToIndex("chr/ch41450.itc", 0x26)
    LoadChrToIndex("chr/ch41451.itc", 0x27)
    LoadChrToIndex("chr/ch41550.itc", 0x28)
    LoadChrToIndex("chr/ch41551.itc", 0x29)
    Call(0, 42)
    Call(0, 43)
    Call(0, 44)
    SetChrPos(0x101, -67340, 0, -1250, 90)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x105, -67880, 0, 500, 90)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x107, -69900, 0, -550, 90)
    SetChrChipByIndex(0x107, 0x25)
    SetChrSubChip(0x107, 0x0)
    PlayBGM("ed7561", 0)
    OP_68(-52000, 2200, -300, 0)
    MoveCamera(71, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24150, 0)
    FadeToBright(1000, 0)
    OP_68(-52000, 1200, -300, 3000)
    MoveCamera(71, 24, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(23000, 3000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x12,
        "#5P*sigh*, so boring...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PStaying on guard in such\x01",
            "a place is too boring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#6PDon't complain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#6PThat Bannings from the SSS\x01",
            "is still on the run, you know.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x13, 500)
    Sleep(100)

    ChrTalk(
        0x12,
        (
            "#5PHa! As if a mere detective alone\x01",
            "could do something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PCouldn't he have fled abroad\x01",
            "a long time ago already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#12PStill, rumor goes that he has an\x01",
            "unbelievable monster with him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#12PIs it true that the 4th Regiment guys\x01",
            "have been eaten by that?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x14, 500)
    Sleep(100)

    ChrTalk(
        0x12,
        "#5PHa ha, that's probably just a false rumor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PMore importantly, since we're here,\x01",
            "I'd like to see Ilya's face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#5PShe's still hospitalized, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#11PYeah, she should be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11PI wish she gets treated\x01",
            "fast and recovers.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "#11P──I agree with you.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-59000, 800, -300, 1500)
    MoveCamera(36, 25, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(20500, 1500)

    def lambda_7E82():
        OP_93(0x12, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_7E82)
    Sleep(50)

    def lambda_7E92():
        OP_93(0x13, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_7E92)
    Sleep(50)

    def lambda_7EA2():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_7EA2)
    Sleep(50)

    def lambda_7EB2():
        OP_93(0x15, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_7EB2)
    Sleep(50)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x15, 0)
    Sleep(1000)
    BeginChrThread(0x101, 0, 0, 46)
    BeginChrThread(0x105, 0, 0, 47)
    BeginChrThread(0x107, 0, 0, 48)
    Sleep(1000)
    OP_68(-55500, 800, -300, 1300)
    MoveCamera(36, 25, 0, 1300)
    OP_6E(500, 1300)
    SetCameraDistance(20500, 1300)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x12,
        "#11PLloyd Bannings!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#11PKh, to think he'd actually show up!\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x14, 0x26)
    SetChrSubChip(0x14, 0x0)
    Sleep(150)
    SetChrChipByIndex(0x13, 0x28)
    SetChrSubChip(0x13, 0x0)
    Sleep(150)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0x12, 0x0)
    Sleep(150)
    SetChrChipByIndex(0x15, 0x28)
    SetChrSubChip(0x15, 0x0)
    Sleep(150)

    ChrTalk(
        0x107,
        (
            "#01203F#6P#3CGoodness.\x01",
            "How rude to call me a monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#6PWell, considering your original form, \x01",
            "it can't really be helped, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P──I don't want to fight.\x02\x03",
            "#00007FHowever, if you stand in our way,\x01",
            "we'll crush you without any mercy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#11PHow brazen...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11PThey're few!\x01",
            "Let's suppress them all at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#11PRoger!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetCameraDistance(19000, 500)
    BeginChrThread(0x12, 0, 0, 49)
    BeginChrThread(0x13, 0, 0, 50)
    BeginChrThread(0x14, 0, 0, 51)
    BeginChrThread(0x15, 0, 0, 52)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x15, 0)
    SetScenarioFlags(0x22, 2)
    Battle("BattleInfo_8E0", 0x30200011, 0x0, 0x0, 0x24, 0xFF)
    FadeToDark(0, 0, -1)
    ClearScenarioFlags(0x22, 2)
    Call(0, 53)
    Return()

    # Function_45_79E1 end

    def Function_46_817D(): pass

    label("Function_46_817D")

    SetChrFlags(0xFE, 0x1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_46_817D end

    def Function_47_819F(): pass

    label("Function_47_819F")

    Sleep(50)
    SetChrFlags(0xFE, 0x1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_47_819F end

    def Function_48_81C4(): pass

    label("Function_48_81C4")

    Sleep(100)
    SetChrFlags(0xFE, 0x1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_48_81C4 end

    def Function_49_81E9(): pass

    label("Function_49_81E9")

    SetChrChipByIndex(0x12, 0x27)
    SetChrSubChip(0x12, 0x0)
    OP_9B(0x1, 0xFE, 0xA, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_49_81E9 end

    def Function_50_8201(): pass

    label("Function_50_8201")

    SetChrChipByIndex(0x13, 0x29)
    SetChrSubChip(0x13, 0x0)
    OP_9B(0x1, 0xFE, 0x15E, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_50_8201 end

    def Function_51_8219(): pass

    label("Function_51_8219")

    SetChrChipByIndex(0x14, 0x26)
    SetChrSubChip(0x14, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_51_8219 end

    def Function_52_8231(): pass

    label("Function_52_8231")

    SetChrChipByIndex(0x15, 0x29)
    SetChrSubChip(0x15, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_52_8231 end

    def Function_53_8249(): pass

    label("Function_53_8249")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(2724)
    SoundLoad(2725)
    SoundLoad(2686)
    SoundLoad(2687)
    SoundLoad(2688)
    SoundLoad(2689)
    SoundLoad(2690)
    SoundLoad(2691)
    SoundLoad(2692)
    SoundLoad(2693)
    SoundLoad(2866)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00203.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06400.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01300.itp")
    AddParty(0x2, 0xFF, 0xFF)
    OP_32(0x2, 0x0, 0x52)
    OP_32(0x2, 0x5, 0x64)
    OP_42(0x2, 0x419, 0xFF)
    OP_42(0x2, 0x5ED, 0xFF)
    OP_42(0x2, 0x651, 0xFF)
    OP_38(0x2, 0x81, 0x2)
    OP_38(0x2, 0x82, 0x2)
    OP_38(0x2, 0x83, 0x2)
    OP_38(0x2, 0x86, 0x2)
    OP_42(0x2, 0xAF, 0x1)
    OP_42(0x2, 0x66, 0x2)
    OP_42(0x2, 0x7A, 0x3)
    OP_42(0x2, 0xA2, 0x6)
    ClearScenarioFlags(0x20, 3)
    LoadChrToIndex("chr/ch41400.itc", 0x1E)
    LoadChrToIndex("chr/ch41500.itc", 0x1F)
    LoadChrToIndex("chr/ch05300.itc", 0x20)
    LoadChrToIndex("chr/ch08500.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch03150.itc", 0x23)
    LoadChrToIndex("chr/ch02750.itc", 0x24)
    LoadChrToIndex("chr/ch41453.itc", 0x25)
    LoadChrToIndex("chr/ch41553.itc", 0x26)
    LoadChrToIndex("apl/ch51700.itc", 0x27)
    LoadChrToIndex("apl/ch51701.itc", 0x28)
    LoadEffect(0x0, "event/ev17027.eff")
    LoadEffect(0x3, "event/ev17004.eff")
    LoadEffect(0x4, "event/ev17005.eff")
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0x24)
    SetChrSubChip(0x107, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x101, -55340, 0, -1250, 90)
    SetChrPos(0x105, -55880, 0, 500, 90)
    SetChrPos(0x107, -57900, 0, -550, 90)
    SetChrPos(0x103, -44000, 0, 150, 270)
    SetChrPos(0x16, -44000, 0, -1200, 270)
    SetChrPos(0x17, -44000, 0, 0, 270)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x12, 0x25)
    SetChrSubChip(0x12, 0x2)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x26)
    SetChrSubChip(0x13, 0x2)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x2)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x26)
    SetChrSubChip(0x15, 0x2)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x12, -50370, 0, 640, 270)
    SetChrPos(0x13, -52240, 0, 580, 270)
    SetChrPos(0x14, -52040, 0, -1450, 270)
    SetChrPos(0x15, -50440, 0, -1520, 270)
    SetChrChipByIndex(0x16, 0x20)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    Call(0, 43)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -52000, 0, 4000, 268)
    OP_78(0xD, 0x18)
    Call(0, 44)
    OP_68(-54300, 800, -300, 0)
    MoveCamera(36, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(20500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x14,
        "#40W#11P...Ugh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#40W#11PS-Strong...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    Sleep(300)

    ChrTalk(
        0x105,
        "#10404F#5PWell then──I guess it's my turn.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(-54200, 800, 860, 1200)
    MoveCamera(36, 25, 0, 1200)
    OP_6E(500, 1200)
    SetCameraDistance(20500, 1200)

    def lambda_8632():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8632)
    OP_9B(0x0, 0x105, 0x0, 0x190, 0x3E8, 0x0)
    Sleep(300)
    BeginChrThread(0x105, 0, 0, 54)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005F#12P(A Grals medal...?)\x02",
    )

    CloseMessageWindow()
    PlayBGM("ed7304", 0)
    SetCameraDistance(20000, 20000)
    Sleep(1000)
    Sound(2866, 255, 50, 0)

    ChrTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10403F#30W#5P#30AO azure seal of mine \x01",
            "shining from the abyss...\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x105, 0, 0, 56)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10401F#30W#5P#20AJoin with the silver will and\x01",
            "give them false memories.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 59)
    Sleep(800)

    ChrTalk(
        0x13,
        "#50W#11P#2S.........Ah...\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x14,
        "#50W#11P#2S.............\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00011F#12P(This is...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#3C#6P(Hm, it seems a kind of suggestive\x01",
            "technique conveyed in the Church.)\x02\x03",
            "#01200F(It seems it uses some kind\x01",
            "of mysterious power...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5P──Just some time ago, you confirmed\x01",
            "a large-scale Cryptid drawing near.\x02\x03",
            "Somehow you managed to repel it,\x01",
            "but since you all suffered injuries, you\x01",
            "decided to momentarily return to base.\x02\x03",
            "#10401FYou didn't catch sight of Bannings and\x01",
            "there's no sign he could appear for now.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    BeginChrThread(0x13, 0, 0, 62)
    WaitChrThread(0x13, 0)
    Sleep(500)

    ChrTalk(
        0x13,
        "#50W#11P#2S............(*nod nod*)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    BeginChrThread(0x14, 0, 0, 64)
    WaitChrThread(0x14, 0)
    Sleep(500)

    ChrTalk(
        0x14,
        "#50W#11P#2S......No sign he could appear for now.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_68(-53350, 800, 2710, 3000)
    OP_52(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 0, 0, 61)
    BeginChrThread(0x13, 0, 0, 63)
    BeginChrThread(0x14, 0, 0, 65)
    BeginChrThread(0x15, 0, 0, 66)
    BeginChrThread(0x105, 0, 0, 55)

    def lambda_8A45():

        label("loc_8A45")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_8A45")

    QueueWorkItem2(0x105, 3, lambda_8A45)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x15, 0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    EndChrThread(0x105, 0x3)
    BeginChrThread(0x18, 0, 0, 67)
    BeginChrThread(0x101, 0, 0, 68)
    BeginChrThread(0x105, 0, 0, 69)
    BeginChrThread(0x107, 0, 0, 70)
    Sleep(1500)
    OP_68(-55360, 1500, -1970, 2000)
    MoveCamera(64, 37, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(19550, 2000)
    OP_6F(0x79)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x107, 0x2)
    WaitChrThread(0x18, 0)
    SetMapObjFlags(0xD, 0x4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00006F#11PA-Amazing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#12P#3CYou can't definitely manipulate them\x01",
            "that much with a mere suggestive technique.\x02\x03",
            "#01200FI presume you made use\x01",
            "of your "Stigma" power...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#5PHa ha...\x01",
            "As expected from a divine beast of legend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#11P"Stigma"...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5P...Well, it's a trivial \x01",
            "very old trauma.\x02\x03",
            "#10408FAt any rate, since it's not perfect,\x01",
            "the suggestion will wear off in two\x01",
            "or three days.\x02\x03",
            "#10401FBecause the army will be on the\x01",
            "lookout, I want you to think I\x01",
            "won't be able to use it next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#11PI see...roger.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x103,
        "Young Girl's Voice",
        "#6P#2686V#30W#20AMr. Wazy, Zeit...?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)

    def lambda_8D80():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8D80)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-44070, 400, 120, 2000)
    MoveCamera(76, 17, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(19770, 2000)

    def lambda_8DF8():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8DF8)
    Sleep(50)

    def lambda_8E08():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8E08)
    Sleep(50)

    def lambda_8E18():
        OP_93(0x107, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_8E18)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x103,
        "#40W............\x02",
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
        "#00005F#11P#12P#NTio...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x107,
        "#01200F#2P#3C#6P#NHm, you look fine.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        "#10404F#6P#NOh boy, what a relief.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x101, -53360, 0, -1680, 90)
    SetChrPos(0x105, -54080, 0, 130, 90)
    SetChrPos(0x107, -55410, 0, -1850, 90)
    SetChrSubChip(0x107, 0x5)
    TurnDirection(0x101, 0x103, 0)
    TurnDirection(0x103, 0x101, 0)
    OP_68(-49050, 1000, -1000, 0)
    MoveCamera(52, 11, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19080, 0)
    Fade(500)
    OP_0D()
    OP_9B(0x0, 0x101, 0x0, 0x190, 0x3E8, 0x0)

    ChrTalk(
        0x101,
        (
            "#00014F#6PThank goodness...!\x01",
            "Because I heard you were at the hospital\x01",
            "I thought what could've ever happened...\x02\x03",
            "#00002FAre you all right?\x01",
            "Are you injured...?\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x103,
        "#00213F#11P#2687V#50W#25A#2S...Mr....Lloyd...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        "#00212F#11P#2688V#20W#4S#15A#4SMr. Lloyd...!!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    BeginChrThread(0x103, 0, 0, 71)
    OP_68(-52640, 1200, -1760, 1800)
    MoveCamera(47, 20, 0, 1800)
    OP_6E(500, 1800)
    SetCameraDistance(17000, 1800)
    WaitChrThread(0x103, 0)

    def lambda_912D():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_912D)

    def lambda_913A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_913A)
    OP_6F(0x79)
    SetCameraDistance(15500, 40000)

    ChrTalk(
        0x101,
        (
            "#00011F#6PUgh...\x01",
            "(H-Her breastplate is...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x103,
        (
            "#00213F#11P#2689V#60W#25AW-Where have you been until now...!?\x02\x03",
            "#00215F#2690V#25AI heard you were put in prison...!\x02\x03",
            "#00212F#2691V#60A...Y-You escaped and were\x01",
            "chased by the army men...\x01",
            "I saw it on t-the orbal net...!\x02\x03",
            "#00213F#2692V#50AI-I...*hic*...\x01",
            "...Have been worried all the time...!\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00008F#6PTio... \x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 0, 0, 78)
    BeginChrThread(0x103, 0, 0, 77)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x101,
        (
            "#00006F#6P...I'm sorry.\x01",
            "It seems I've made you worry.\x02\x03",
            "#00002FBut it's fine now.\x02\x03",
            "I came back to Crossbell with\x01",
            "the help of Zeit and Wazy...\x02\x03",
            "#00004FSo...you can relax.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x103,
        "#00215F#11P#2693V#40W#25A...Uuuh...*sob*...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    NpcTalk(
        0x17,
        "Girl's Voice",
        (
            "#11P#2724V#30W#N#25AWhoa whoa...\x01",
            "They're so lovey dovey.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    NpcTalk(
        0x16,
        "Woman's Voice",
        (
            "#11P#N#20A#30WUh uh, I feel a little uneasy\x01",
            "to interrupt them, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-52280, 1200, -1700, 2500)
    SetCameraDistance(17000, 2500)

    def lambda_94B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_94B4)

    def lambda_94C5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_94C5)
    SetChrPos(0x16, -42500, 0, -1200, 270)
    SetChrPos(0x17, -42500, 0, 0, 270)
    BeginChrThread(0x17, 0, 0, 73)
    Sleep(100)
    BeginChrThread(0x16, 0, 0, 74)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00002F#6PSister Cecil!\x01",
            "And...Fran!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x17, 0)
    WaitChrThread(0x16, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x17,
        (
            "#2725V#30WEhehe...\x01",
            "Long time no see, Mr. Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xAA5)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x16,
        (
            "#30WI am really glad you are safe...\x02\x03",
            "...I was worried, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    ChrTalk(
        0x101,
        (
            "#00006F#6PI'm sorry...\x01",
            "I've made you all worry.\x02\x03",
            "#00002FBut Fran...\x01",
            "You look completely recovered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#06409F#11PYes, my injuries have been\x01",
            "healed a long time ago!\x02\x03",
            "#06406FWell, since Crossbell\x01",
            "is in that state, I can't\x01",
            "go back to my post, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PI see... \x01",
            "Still, I'm really glad.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(2277, 255, 80, 0)
    Sleep(300)
    BeginChrThread(0x103, 0, 0, 72)
    WaitChrThread(0x103, 0)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#00215F#11P#30W...By the way.\x01",
            "What's with Mr. Wazy's clothes?\x02\x03",
            "#00216FAnd Zeit, where have you been...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10404F#6PHu hu, many things have happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#6P#3CAt any rate, let's explain in general\x01",
            "the sequence of events up to now.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x16,
        "#01305F#11PWhat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#06411F#11PThat now was...\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#00205F#11P? What's wrong...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6PWell, "what's wrong" you say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#6PHa ha, could it be that because \x01",
            "you've always understood him,\x01",
            "you haven't noticed?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    Sleep(500)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        (
            "#00205F#11P#4SZ-Zeit!?\x02\x03",
            "#00207FWhy are you speaking\x01",
            "in human language──!?\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 2000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("t1510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_53_8249 end

    def Function_54_9AE8(): pass

    label("Function_54_9AE8")

    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x2)
    Sleep(100)
    Sound(531, 0, 50, 0)
    Sound(859, 0, 40, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    Return()

    # Function_54_9AE8 end

    def Function_55_9B17(): pass

    label("Function_55_9B17")

    Sleep(4000)
    BeginChrThread(0x105, 1, 0, 58)
    WaitChrThread(0x105, 1)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x2)
    Return()

    # Function_55_9B17 end

    def Function_56_9B4B(): pass

    label("Function_56_9B4B")

    Sound(895, 0, 100, 0)
    Sound(222, 0, 30, 0)
    Sound(852, 2, 100, 0)
    PlayEffect(0x3, 0x1, 0x105, 0x5, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x4, 0x2, 0x105, 0x1, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    StopEffect(0x1, 0x2)
    BeginChrThread(0xFE, 2, 0, 57)
    Return()

    # Function_56_9B4B end

    def Function_57_9BDB(): pass

    label("Function_57_9BDB")

    Sleep(300)

    label("loc_9BDE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C28")
    PlayEffect(0x0, 0xFF, 0x105, 0x3, 0, 1050, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_9BDE")

    label("loc_9C28")

    Return()

    # Function_57_9BDB end

    def Function_58_9C29(): pass

    label("Function_58_9C29")

    EndChrThread(0xFE, 0x2)
    Sleep(300)
    StopEffect(0x2, 0x2)
    StopSound(852, 500, 90)
    Sleep(300)
    Return()

    # Function_58_9C29 end

    def Function_59_9C3D(): pass

    label("Function_59_9C3D")


    def lambda_9C42():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_9C42)
    Sleep(200)

    def lambda_9C5E():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_9C5E)
    Sleep(200)

    def lambda_9C7A():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_9C7A)
    Sleep(200)

    def lambda_9C96():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_9C96)
    Sleep(200)
    Return()

    # Function_59_9C3D end

    def Function_60_9CAE(): pass

    label("Function_60_9CAE")

    Sleep(250)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    Return()

    # Function_60_9CAE end

    def Function_61_9CBD(): pass

    label("Function_61_9CBD")

    Sleep(900)
    SetChrSubChip(0x12, 0x1)
    Sleep(700)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    BeginChrThread(0xFE, 1, 0, 1)
    OP_93(0xFE, 0x0, 0x12C)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x384, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x60E, 0x384, 0x0)
    OP_9B(0x0, 0xFE, 0x2D, 0xFA, 0x384, 0x1)
    BeginChrThread(0xFE, 3, 0, 60)
    OP_9C(0xFE, 0x0, 0x1F4, 0x3E8, 0x226, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x384, 0x1)
    Return()

    # Function_61_9CBD end

    def Function_62_9D46(): pass

    label("Function_62_9D46")

    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_62_9D46 end

    def Function_63_9D4B(): pass

    label("Function_63_9D4B")

    Sleep(200)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    BeginChrThread(0xFE, 1, 0, 1)
    OP_93(0xFE, 0x0, 0x12C)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x384, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x28A, 0x384, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x64, 0x384, 0x0)
    Sound(464, 0, 100, 0)
    OP_71(0xD, 0x1, 0x1E, 0x1, 0x0)
    OP_79(0xD)
    OP_9B(0x0, 0xFE, 0x0, 0x96, 0x384, 0x1)
    BeginChrThread(0xFE, 3, 0, 60)
    OP_9C(0xFE, 0x0, 0x1F4, 0x3E8, 0x226, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x384, 0x1)
    Return()

    # Function_63_9D4B end

    def Function_64_9DF1(): pass

    label("Function_64_9DF1")

    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_64_9DF1 end

    def Function_65_9DF6(): pass

    label("Function_65_9DF6")

    Sleep(1200)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    BeginChrThread(0xFE, 1, 0, 1)
    OP_93(0xFE, 0x0, 0x12C)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x384, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2EE, 0x384, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x15E, 0x384, 0x0)
    BeginChrThread(0xFE, 3, 0, 60)
    OP_9C(0xFE, 0x0, 0x1F4, 0x3E8, 0x226, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x384, 0x1)
    Return()

    # Function_65_9DF6 end

    def Function_66_9E78(): pass

    label("Function_66_9E78")

    Sleep(1500)
    SetChrSubChip(0x15, 0x1)
    Sleep(700)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    BeginChrThread(0xFE, 1, 0, 1)
    OP_93(0xFE, 0x0, 0x12C)
    OP_9B(0x0, 0xFE, 0x0, 0x8CA, 0x384, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x60E, 0x384, 0x0)
    OP_9B(0x0, 0xFE, 0x2D, 0xFA, 0x384, 0x1)
    BeginChrThread(0xFE, 3, 0, 60)
    OP_9C(0xFE, 0x0, 0x1F4, 0x3E8, 0x226, 0x1F4)

    def lambda_9EF6():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x384, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9EF6)
    Sleep(300)
    Sound(463, 0, 100, 0)
    OP_71(0xD, 0x1F, 0x3C, 0x1, 0x8)
    OP_79(0xD)
    Return()

    # Function_66_9E78 end

    def Function_67_9F1F(): pass

    label("Function_67_9F1F")

    Sound(465, 0, 100, 0)
    SetMapObjFrame(0xD, "light", 0x1, 0x1)
    Sleep(500)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x167, 0xFA, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x167, 0xFA, 0xBB8, 0x1)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -53500, 0, 3700)
    OP_9F(0x1, -55000, 0, 2900)
    OP_9F(0x1, -57000, 0, 1600)
    OP_9F(0x1, -60000, 0, 500)
    OP_9F(0x1, -69000, 0, 0)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    Return()

    # Function_67_9F1F end

    def Function_68_9FB6(): pass

    label("Function_68_9FB6")


    def lambda_9FBB():

        label("loc_9FBB")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_9FBB")

    QueueWorkItem2(0xFE, 2, lambda_9FBB)
    Sleep(400)
    OP_9B(0x1, 0xFE, 0x5A, 0x6D6, 0x7D0, 0x0)
    Return()

    # Function_68_9FB6 end

    def Function_69_9FDB(): pass

    label("Function_69_9FDB")


    def lambda_9FE0():

        label("loc_9FE0")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_9FE0")

    QueueWorkItem2(0xFE, 2, lambda_9FE0)
    Sleep(100)
    OP_9B(0x1, 0xFE, 0x5A, 0x4E2, 0x3E8, 0x0)
    Return()

    # Function_69_9FDB end

    def Function_70_A000(): pass

    label("Function_70_A000")

    Sleep(600)
    OP_9B(0x0, 0xFE, 0x5A, 0x1F4, 0x7D0, 0x1)
    OP_9D(0xFE, 0xFFFF259A, 0x0, 0xFFFFF7CC, 0x15E, 0x5DC)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)

    def lambda_A03D():

        label("loc_A03D")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_A03D")

    QueueWorkItem2(0xFE, 2, lambda_A03D)
    Return()

    # Function_70_A000 end

    def Function_71_A04B(): pass

    label("Function_71_A04B")

    OP_9B(0x0, 0xFE, 0x0, 0x2198, 0x1770, 0x0)
    BeginChrThread(0xFE, 3, 0, 75)
    Sound(811, 0, 50, 0)
    Sound(898, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 76)

    def lambda_A077():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A077)
    Sleep(100)

    def lambda_A093():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A093)
    Return()

    # Function_71_A04B end

    def Function_72_A0A8(): pass

    label("Function_72_A0A8")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1000)
    Sound(812, 0, 100, 0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
    Return()

    # Function_72_A0A8 end

    def Function_73_A0E2(): pass

    label("Function_73_A0E2")

    OP_9B(0x0, 0xFE, 0x163, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_73_A0E2 end

    def Function_74_A0F2(): pass

    label("Function_74_A0F2")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x163, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_74_A0F2 end

    def Function_75_A105(): pass

    label("Function_75_A105")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1005)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    Return()

    # Function_75_A105 end

    def Function_76_A129(): pass

    label("Function_76_A129")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x8)
    Sleep(100)
    SetChrSubChip(0xFE, 0x9)
    Sleep(100)
    SetChrSubChip(0xFE, 0xA)
    Sleep(300)
    Return()

    # Function_76_A129 end

    def Function_77_A14D(): pass

    label("Function_77_A14D")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x4)
    Sleep(450)
    Return()

    # Function_77_A14D end

    def Function_78_A171(): pass

    label("Function_78_A171")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xA)
    Sleep(150)
    SetChrSubChip(0xFE, 0xB)
    Sleep(150)
    SetChrSubChip(0xFE, 0xC)
    Sleep(450)
    Return()

    # Function_78_A171 end

    def Function_79_A195(): pass

    label("Function_79_A195")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x6, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch05300.itc", 0x1E)
    LoadChrToIndex("chr/ch06900.itc", 0x1F)
    LoadChrToIndex("chr/ch03154.itc", 0x20)
    LoadEffect(0x0, "battle/mgaria0.eff")
    SoundLoad(497)
    SetChrPos(0x101, -10000, 0, 750, 90)
    SetChrPos(0x103, -10200, 0, -850, 90)
    SetChrPos(0x105, -11550, 0, 1350, 90)
    SetChrPos(0x17, -11700, 0, -1450, 90)
    SetChrPos(0x107, -12050, 0, 100, 90)
    SetChrSubChip(0x107, 0x5)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -6000, 1000, 0, 270)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x11, 0x19)
    OP_93(0x19, 0xB4, 0x0)
    OP_68(-10000, 3000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25000, 0)
    FadeToBright(1000, 0)
    OP_68(-10000, 1000, 0, 3000)
    MoveCamera(45, 23, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(25000, 3000)
    OP_6F(0x79)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and the others, together with Zeit...\x02\x03",
            "Said goodbye to Cecil and left St. Ursula Hospital.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(27000, 5000)
    BeginChrThread(0x101, 0, 0, 81)
    BeginChrThread(0x103, 0, 0, 82)
    BeginChrThread(0x105, 0, 0, 83)
    BeginChrThread(0x107, 0, 0, 84)
    BeginChrThread(0x17, 0, 0, 85)
    BeginChrThread(0x16, 0, 0, 87)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x103, 0x0)
    EndChrThread(0x105, 0x0)
    EndChrThread(0x107, 0x0)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrPos(0x105, -51000, 100, 17000, 90)
    SetChrPos(0x101, -51300, 0, 15600, 90)
    SetChrPos(0x103, -52380, 0, 17080, 90)
    SetChrPos(0x107, -51330, 0, 18780, 124)
    SetChrPos(0x17, -51810, 0, 14140, 51)
    SetChrSubChip(0x107, 0x5)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x1000)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x11, 0x1000)
    OP_71(0x11, 0x65, 0xA0, 0x0, 0x20)
    SetMapObjFlags(0x9, 0x4)
    OP_68(-50250, 1000, 17000, 0)
    MoveCamera(48, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20150, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Sound(357, 0, 50, 0)
    PlayEffect(0x0, 0x0, 0x105, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(-49850, 1000, 17000, 18000)
    SetCameraDistance(15000, 18000)
    BeginChrThread(0x105, 3, 0, 88)
    BeginChrThread(0x19, 1, 0, 89)
    Sleep(500)
    Sound(935, 0, 100, 0)
    Sleep(1500)
    StopEffect(0x0, 0x2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──While going back, Wazy found a "gap" in the\x01",
            "Septium vein force field in front of the hospital...\x02\x03",
            "By fixing it with a "magic circle",\x01",
            "it became possible to have the\x01",
            ""Merkabah" come pick them up.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x26, 1, 0, 80)
    Fade(500)
    OP_68(-49730, 1500, 16190, 0)
    MoveCamera(64, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(37770, 0)
    OP_68(-43790, 1000, 18370, 6000)
    MoveCamera(68, 48, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(60530, 6000)
    ClearMapObjFlags(0x11, 0x4)
    SetChrPos(0x19, -48000, 18250, 17000, 180)
    OP_D5(0x19, 0x0, 0x2BF20, 0x0, 0x0)
    BeginChrThread(0x19, 0, 0, 86)
    Sleep(4000)
    StopSound(497, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x19, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(814, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Because Tio and Fran joined, it became\x01",
            "possible to accept Wanted Monsters requests\x01",
            "and such at the terminal inside the Merkabah.\x02\x03",
            "Since you can use the terminal in the cabin,\x01",
            "please give it a try.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x22, 3)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_79_A195 end

    def Function_80_A774(): pass

    label("Function_80_A774")

    Sound(497, 2, 10, 0)
    Sleep(50)
    OP_25(0x1F1, 0xF)
    Sleep(50)
    OP_25(0x1F1, 0x14)
    Sleep(50)
    OP_25(0x1F1, 0x19)
    Sleep(50)
    OP_25(0x1F1, 0x1E)
    Sleep(50)
    OP_25(0x1F1, 0x23)
    Sleep(50)
    OP_25(0x1F1, 0x28)
    Sleep(50)
    OP_25(0x1F1, 0x2D)
    Sleep(50)
    OP_25(0x1F1, 0x32)
    Sleep(50)
    OP_25(0x1F1, 0x37)
    Sleep(50)
    OP_25(0x1F1, 0x3C)
    Sleep(50)
    OP_25(0x1F1, 0x41)
    Sleep(50)
    OP_25(0x1F1, 0x46)
    Return()

    # Function_80_A774 end

    def Function_81_A7CF(): pass

    label("Function_81_A7CF")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_81_A7CF end

    def Function_82_A7E9(): pass

    label("Function_82_A7E9")

    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(900)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_82_A7E9 end

    def Function_83_A806(): pass

    label("Function_83_A806")

    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(800)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_83_A806 end

    def Function_84_A823(): pass

    label("Function_84_A823")

    Sleep(500)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_84_A823 end

    def Function_85_A83D(): pass

    label("Function_85_A83D")

    Sleep(400)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_85_A83D end

    def Function_86_A85A(): pass

    label("Function_86_A85A")

    OP_96(0xFE, 0xFFFF4480, 0x251C, 0x4268, 0xBB8, 0x1)
    OP_96(0xFE, 0xFFFF4480, 0x2328, 0x4268, 0x7D0, 0x1)
    OP_96(0xFE, 0xFFFF4480, 0x2134, 0x4268, 0x3E8, 0x1)
    Return()

    # Function_86_A85A end

    def Function_87_A897(): pass

    label("Function_87_A897")

    Return()

    # Function_87_A897 end

    def Function_88_A898(): pass

    label("Function_88_A898")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A8B2")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_88_A898")

    label("loc_A8B2")

    Return()

    # Function_88_A898 end

    def Function_89_A8B3(): pass

    label("Function_89_A8B3")

    SetMapObjFrame(0xF, "Null_fream", 0x2, "start")
    Sleep(20000)
    SetMapObjFrame(0xF, "Null_fream", 0x2, "loop")
    Return()

    # Function_89_A8B3 end

    def Function_90_A8DE(): pass

    label("Function_90_A8DE")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch05300.itc", 0x1E)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrPos(0x16, -9000, 0, -500, 270)
    OP_68(-37710, 1000, 350, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19060, 0)
    SetChrPos(0x101, -41980, 0, 500, 90)
    SetChrPos(0x102, -42590, 0, -900, 90)
    SetChrPos(0x109, -42700, 0, 1300, 90)
    SetChrPos(0x105, -44040, 0, -1300, 90)
    SetChrPos(0x104, -43990, 0, 300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01300.itp")
    OP_0D()
    OP_68(-34660, 1000, -430, 5000)

    def lambda_A9DA():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A9DA)
    Sleep(50)

    def lambda_A9F7():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A9F7)
    Sleep(50)

    def lambda_AA14():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AA14)
    Sleep(50)

    def lambda_AA31():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AA31)
    Sleep(50)

    def lambda_AA4E():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AA4E)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    Sleep(500)

    NpcTalk(
        0x16,
        "Woman's Voice",
        "...Lloyd...!?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00002FAh...!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-9210, 1000, -500, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19060, 0)
    OP_0D()
    Sleep(800)
    OP_68(-23280, 1000, -240, 5000)
    MoveCamera(44, 25, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(17390, 5000)

    def lambda_AB7D():
        OP_95(0xFE, -21270, 0, -10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_AB7D)
    Sleep(50)

    def lambda_AB9A():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB9A)
    Sleep(50)

    def lambda_ABB7():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ABB7)
    Sleep(50)

    def lambda_ABD4():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ABD4)
    Sleep(50)

    def lambda_ABF1():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ABF1)
    Sleep(50)

    def lambda_AC0E():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AC0E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x16, 1)

    ChrTalk(
        0x101,
        (
            "#6P#00009FSister Cecil...\x01",
            "Ha ha, we meet all of a sudden, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#11P#01300FUh uh...welcome back, Lloyd.\x02\x03",
            "#01309FMiss Elie, Randy,\x01",
            "Miss Noｱl too...\x01",
            "Have you been well, everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100F*giggle*, long time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00309FBeen a long time, Miss Cecil!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10109FUh uh, it's really been a long time.\x02\x03",
            "#10100FI guess since we met when\x01",
            "the hospital was assaulted\x01",
            "during the Cult incident...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#11P#01309FUh uh...that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FEeh, is this woman the rumored sister?\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#11P#01305FMy, there's a child I don't know with you...\x02\x03",
            "#01300FCould you be a new member\x01",
            "like Miss Noｱl I heard about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHu hu, I guess I am.\x02\x03",
            "#10302FI am Wazy Hemisphere.\x01",
            "Nice to make your acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#11P#01309FUh uh, nice to meet you.\x02\x03",
            "#01300FThen... I will formally\x01",
            "introduce myself too.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x16,
        (
            "*cough*... My name is Cecil Neues,\x01",
            "I am a nurse in service\x01",
            "at St. Ursula Hospital.\x02\x03",
            "Uh uh, please take care of my\x01",
            "cute little brother, Lloyd.\x02",
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
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FCome on sister Cecil...\x01",
            "Strictly speaking, we aren't\x01",
            "brother and sister, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00000F*cough*, ehhm..\x01",
            "She's someone who took care\x01",
            "of me since I was a child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#11P#01306FOh, Lloyd, you're so shy.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#00012FI-I'm not.\x02",
    )

    CloseMessageWindow()
    OP_93(0x16, 0xE1, 0x1F4)
    Sleep(1000)
    OP_93(0x16, 0x13B, 0x1F4)
    Sleep(1000)
    OP_93(0x16, 0x10E, 0x1F4)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#11P#01304FUhhm, even so...\x01",
            "Wazy and Miss Noｱl too\x01",
            "are very beautiful.\x02\x03",
            "#01300FLloyd, I wonder if you\x01",
            "have finally decided\x01",
            "who to date?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10105FT-To date!?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FSister Cecil... I told you before too,\x01",
            "the SSS is not that kind of place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#11P#01305FAh...right. \x01",
            "I, of all people, have been inconsiderate.\x02\x03",
            "#01303FHaving such a conversation when\x01",
            "Tio is not even here now was unfair.\x02\x03",
            "#01300FWhen Tio comes back, please take\x01",
            "your time to choose your partner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FI-I told you already...\x01",
            "Why has to be like that!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109F*giggle*, somehow looking\x01",
            "at Miss Cecil relaxes me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00309FYeah, her airheadedness too seems to be doin' well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00006FAnd you around me retort too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#11P#01304F*giggle*... Nevertheless, it's been\x01",
            "so long since I saw you that I am\x01",
            "feeling quite nostalgic.\x02\x03",
            "#01300FIt's just right my break time too.\x01",
            "Would you like to have tea with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FThen, since we're here...\x02\x03",
            "#00002FEveryone, should\x01",
            "we accept her offer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10109FYes, please allow us to make you company!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("t1510", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_90_A8DE end

    def Function_91_B625(): pass

    label("Function_91_B625")

    Return()

    # Function_91_B625 end

    def Function_92_B626(): pass

    label("Function_92_B626")

    EventBegin(0x0)
    Fade(500)
    OP_68(-47260, 1700, -1110, 0)
    MoveCamera(44, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x106, -48500, 0, -230, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_B838")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x102, -46300, 0, -1330, 90)
    SetChrPos(0x103, -46300, 0, 870, 90)
    SetChrPos(0x104, -48400, 0, 1030, 90)

    def lambda_B6BE():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B6BE)

    def lambda_B6D8():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B6D8)

    def lambda_B6F2():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B6F2)

    def lambda_B70C():
        OP_95(0xFE, -46400, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B70C)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B75C")
    SetChrPos(0x109, -48000, 0, -1070, 90)

    def lambda_B747():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B747)

    label("loc_B75C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B797")
    SetChrPos(0x105, -48000, 0, -1070, 90)

    def lambda_B782():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B782)

    label("loc_B797")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B7D2")
    SetChrPos(0x10A, -48000, 0, -1070, 90)

    def lambda_B7BD():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_B7BD)

    label("loc_B7D2")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B80B")
    WaitChrThread(0x109, 1)

    label("loc_B80B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B81F")
    WaitChrThread(0x105, 1)

    label("loc_B81F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B833")
    WaitChrThread(0x10A, 1)

    label("loc_B833")

    Jump("loc_BB24")

    label("loc_B838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_B946")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x103, -46300, 0, -1330, 90)
    SetChrPos(0x104, -46300, 0, 870, 90)
    SetChrPos(0x105, -48400, 0, 1030, 90)
    SetChrPos(0x109, -48000, 0, -1070, 90)

    def lambda_B89B():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B89B)

    def lambda_B8B5():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B8B5)

    def lambda_B8CF():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B8CF)

    def lambda_B8E9():
        OP_95(0xFE, -46400, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B8E9)

    def lambda_B903():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B903)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x109, 1)
    Jump("loc_BB24")

    label("loc_B946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_BA54")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x103, -46300, 0, -1330, 90)
    SetChrPos(0x104, -46300, 0, 870, 90)
    SetChrPos(0x107, -48800, 0, 1030, 90)
    SetChrPos(0x105, -48300, 0, -1070, 90)

    def lambda_B9A9():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B9A9)

    def lambda_B9C3():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B9C3)

    def lambda_B9DD():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B9DD)

    def lambda_B9F7():
        OP_95(0xFE, -46800, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_B9F7)

    def lambda_BA11():
        OP_95(0xFE, -46300, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BA11)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x107, 1)
    WaitChrThread(0x105, 1)
    Jump("loc_BB24")

    label("loc_BA54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_BB24")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x103, -46300, 0, -1330, 90)
    SetChrPos(0x105, -46300, 0, 870, 90)
    SetChrPos(0x107, -48800, 0, 1030, 90)

    def lambda_BAA6():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BAA6)

    def lambda_BAC0():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BAC0)

    def lambda_BADA():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BADA)

    def lambda_BAF4():
        OP_95(0xFE, -46800, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_BAF4)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x107, 1)

    label("loc_BB24")


    ChrTalk(
        0x106,
        (
            "#6P#10708FI'm sorry, I'd like to wait\x01",
            "for you outside the hospital.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_BCD7")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBEA")

    def lambda_BB8B():
        TurnDirection(0x109, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BB8B)
    Sleep(50)

    def lambda_BB9B():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BB9B)
    Sleep(50)

    def lambda_BBAB():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BBAB)
    Sleep(50)

    def lambda_BBBB():
        TurnDirection(0x102, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BBBB)
    Sleep(50)

    def lambda_BBCB():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BBCB)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    label("loc_BBEA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC5E")

    def lambda_BBFF():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BBFF)
    Sleep(50)

    def lambda_BC0F():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BC0F)
    Sleep(50)

    def lambda_BC1F():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BC1F)
    Sleep(50)

    def lambda_BC2F():
        TurnDirection(0x102, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BC2F)
    Sleep(50)

    def lambda_BC3F():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BC3F)
    Sleep(50)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    label("loc_BC5E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BCD2")

    def lambda_BC73():
        TurnDirection(0x10A, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_BC73)
    Sleep(50)

    def lambda_BC83():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BC83)
    Sleep(50)

    def lambda_BC93():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BC93)
    Sleep(50)

    def lambda_BCA3():
        TurnDirection(0x102, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BCA3)
    Sleep(50)

    def lambda_BCB3():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BCB3)
    Sleep(50)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    label("loc_BCD2")

    Jump("loc_BE14")

    label("loc_BCD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_BD49")

    def lambda_BCE5():
        TurnDirection(0x109, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BCE5)
    Sleep(50)

    def lambda_BCF5():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BCF5)
    Sleep(50)

    def lambda_BD05():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BD05)
    Sleep(50)

    def lambda_BD15():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BD15)
    Sleep(50)

    def lambda_BD25():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BD25)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    Jump("loc_BE14")

    label("loc_BD49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_BDBB")

    def lambda_BD57():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_BD57)
    Sleep(50)

    def lambda_BD67():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BD67)
    Sleep(50)

    def lambda_BD77():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BD77)
    Sleep(50)

    def lambda_BD87():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BD87)
    Sleep(50)

    def lambda_BD97():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BD97)
    Sleep(50)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    Jump("loc_BE14")

    label("loc_BDBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_BE14")

    def lambda_BDC9():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_BDC9)
    Sleep(50)

    def lambda_BDD9():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BDD9)
    Sleep(50)

    def lambda_BDE9():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BDE9)
    Sleep(50)

    def lambda_BDF9():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BDF9)
    Sleep(50)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)

    label("loc_BE14")


    ChrTalk(
        0x101,
        (
            "#11P#00003FYeah, understood.\x01",
            "See you later.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_32(0xFF, 0xF9, 0x0)
    SetScenarioFlags(0x1AD, 2)
    RemoveParty(0x5, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    ModifyEventFlags(1, 5, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BE81")
    RemoveParty(0x6, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)

    label("loc_BE81")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -44100, 0, -230, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_BEB3")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_BEB3")

    EventEnd(0x5)
    Return()

    # Function_92_B626 end

    def Function_93_BEB6(): pass

    label("Function_93_BEB6")

    EventBegin(0x0)
    Fade(500)
    OP_68(-49470, 1000, -560, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18720, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_BFAA")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x102, -46820, 0, -830, 270)
    SetChrPos(0x103, -46820, 0, 370, 270)
    SetChrPos(0x104, -45620, 0, -1030, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BF59")
    SetChrPos(0x109, -45620, 0, 570, 270)

    label("loc_BF59")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BF7A")
    SetChrPos(0x105, -45620, 0, 570, 270)

    label("loc_BF7A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BF9B")
    SetChrPos(0x10A, -45620, 0, 570, 270)

    label("loc_BF9B")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_C0D1")

    label("loc_BFAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_C017")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x103, -46820, 0, -830, 270)
    SetChrPos(0x104, -46820, 0, 370, 270)
    SetChrPos(0x109, -45620, 0, -1030, 270)
    SetChrPos(0x105, -45620, 0, 570, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_C0D1")

    label("loc_C017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_C084")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x103, -46820, 0, -830, 270)
    SetChrPos(0x104, -46820, 0, 370, 270)
    SetChrPos(0x105, -45620, 0, 570, 270)
    SetChrPos(0x107, -45320, 0, -1230, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_C0D1")

    label("loc_C084")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_C0D1")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x103, -46820, 0, -830, 270)
    SetChrPos(0x105, -46820, 0, 370, 270)
    SetChrPos(0x107, -45320, 0, -1230, 270)

    label("loc_C0D1")

    OP_4B(0xD, 0xFF)
    OP_0D()

    ChrTalk(
        0xD,
        (
            "#6P#10702FWelcome back, everyone.\x01",
            "...Have you finished what you had to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00000FYeah, let's go.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearScenarioFlags(0x1AD, 2)
    ModifyEventFlags(1, 4, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    SetChrFlags(0xD, 0x80)
    AddParty(0x5, 0xFF, 0xFF)
    SetChrChipPat(0x5, 0x1, 0x20)
    LoadChrChipPat()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -48820, 0, -230, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_C1A1")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_C1A1")

    EventEnd(0x5)
    Return()

    # Function_93_BEB6 end

    def Function_94_C1A4(): pass

    label("Function_94_C1A4")

    EventBegin(0x0)
    Fade(500)
    OP_68(-46080, 1000, -230, 0)
    MoveCamera(51, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -50520, 0, -230, 90)
    SetChrPos(0x102, -50500, 0, 1110, 90)
    SetChrPos(0x103, -50500, 0, -1420, 90)
    SetChrPos(0x104, -51500, 0, 1110, 90)
    SetChrPos(0x106, -51500, 0, -230, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C24F")
    SetChrPos(0x109, -51500, 0, -1420, 90)

    label("loc_C24F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C270")
    SetChrPos(0x105, -51500, 0, -1420, 90)

    label("loc_C270")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C291")
    SetChrPos(0x10A, -51500, 0, -1420, 90)

    label("loc_C291")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_C2AA():
        OP_95(0xFE, -44520, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C2AA)
    Sleep(30)

    def lambda_C2C7():
        OP_95(0xFE, -44520, 0, 1110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C2C7)
    Sleep(30)

    def lambda_C2E4():
        OP_95(0xFE, -44520, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C2E4)
    Sleep(30)

    def lambda_C301():
        OP_95(0xFE, -45820, 0, 1110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C301)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C343")

    def lambda_C32E():
        OP_95(0xFE, -45820, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C32E)

    label("loc_C343")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C36D")

    def lambda_C358():
        OP_95(0xFE, -45820, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C358)

    label("loc_C36D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C397")

    def lambda_C382():
        OP_95(0xFE, -45820, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_C382)

    label("loc_C397")

    Sleep(30)

    def lambda_C39F():
        OP_95(0xFE, -48500, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_C39F)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)

    ChrTalk(
        0x106,
        (
            "#6P#10703FThen, everyone.\x01",
            "I'll excuse myself here...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_C403():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C403)

    def lambda_C410():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C410)

    def lambda_C41D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C41D)

    def lambda_C42A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C42A)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C44F")

    def lambda_C447():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C447)

    label("loc_C44F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C46C")

    def lambda_C464():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C464)

    label("loc_C46C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C489")

    def lambda_C481():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_C481)

    label("loc_C489")

    WaitChrThread(0x104, 1)
    Sleep(500)

    ChrTalk(
        0x102,
        "#11P#00105FMiss Rixia...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00303F*sigh*...it can't be helped.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#11P#00003F...Say, Rixia.\x02\x03",
            "#00000FWon't you go at least to\x01",
            "hear Miss Ilya's voice?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#6P#10705F......what......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003FYou won't meet with Miss Ilya\x01",
            "until you've settled everything...\x02\x03",
            "I understand your feelings and\x01",
            "I want to respect them, but...\x02\x03",
            "#00000FWouldn't it be fine if you just\x01",
            "listened to Miss Ilya talking\x01",
            "with us from outside her room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#6P#10705FOh.........\x02\x03",
            "#10708F............\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)

    ChrTalk(
        0x104,
        (
            "#5P#00302FHe's right, it would be fine if\x01",
            "you gave yourself a small reward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00203FIt is very likely that from now on\x01",
            "many other difficulties await us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FI think that hearing the voice of a person\x01",
            "important to you would give you strength,\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C879")

    ChrTalk(
        0x109,
        (
            "#11P#10105FThat's right, Miss Rixia!\x02\x03",
            "#10101FWe'll do our best to not let\x01",
            "her notice you're there!\x02\x03",
            "#10104FI mean, when I met Fran too,\x01",
            "I cheered up so much...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C879")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C953")

    ChrTalk(
        0x105,
        (
            "#11P#10404FHu hu, why not?\x02\x03",
            "#10400FIf you don't meet her in a real sense,\x01",
            "you'd be able to keep your vow.\x02\x03",
            "#10408F...If you'll never be able to see her again,\x01",
            "don't you think it would be too late?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C953")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CA12")

    ChrTalk(
        0x10A,
        (
            "#11P#00603F"Yin"──\x01",
            "No, Rixia Mao.\x02\x03",
            "#00600FA detective like me shouldn't say it,\x01",
            "but we're in a time of crisis.\x02\x03",
            "#00602FIt would be good if you\x01",
            "didn't have any regrets.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA12")

    Sleep(1500)
    OP_64(0x106)

    ChrTalk(
        0x106,
        (
            "#6P#10704F...Everyone.\x01",
            "Thank you very much.\x02\x03",
            "#10702F...I'll accept your kind offer...\x01",
            "Please let me come with you in front of her room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00002FYeah...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00100FYes, all right...!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1AD, 3)
    ModifyEventFlags(0, 6, 0x80)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -44520, 0, -230, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_94_C1A4 end

    def Function_95_CB16(): pass

    label("Function_95_CB16")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_D339")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB34")
    Call(0, 96)
    Jump("loc_D334")

    label("loc_CB34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D153")

    ChrTalk(
        0x10,
        (
            "#01300FLloyd... It seems you have\x01",
            "beaten Mr. Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah. As expected, it was a close game, but...\x01",
            "I could do it thanks to everyone's help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FMr. Arios was a worthy rival to \x01",
            "boost our abilities and a "barrier" \x01",
            "we had to get over too...\x02\x03",
            "#00100FFrankly speaking, I think that if we\x01",
            "had missed even one person, we would've\x01",
            "never been able to be a match for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00304F...I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#01309FUh uh, you all together are the\x01",
            ""Special Support Section", right?\x01",
            "I think you should be very proud.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)

    ChrTalk(
        0x10,
        (
            "#01304FI didn't speak with Mr. Arios\x01",
            "so many times, however...\x02\x03",
            "I felt like he's been bearing\x01",
            "a weight in his heart\x01",
            "since a long time.\x02\x03",
            "#01308FBearing alone the facts of Shizuku,\x01",
            "his wife and Guy too...\x01",
            "It was something unbearable to see.\x02\x03",
            "#01300FBecause that man is endlessly\x01",
            "strong, I think that maybe he\x01",
            "couldn't even count on others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThe loneliness that comes from strength...\x01",
            "It could be really like you say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#01302F*giggle*, but I am sure that having been defeated\x01",
            "after fighting with all his might against you all,\x01",
            "he's been released from that too.\x02\x03",
            "#01304FI think that Guy too was worried,\x01",
            "so let me thank you in his stead,\x01",
            "as his fianceｳ.\x02\x03",
            "#01309FThank you for having saved Mr. Arios,\x01",
            "Guy's close friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FHa ha...you're welcome.\x02\x03",
            "#00000FWhat remains is only to get KeA back.\x01",
            "Wait for us, sister Cecil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#01300FYes, all right.\x02\x03",
            "#01303FLloyd, everyone...\x01",
            "Be careful until the end.\x02\x03",
            "#01302FI'll be here praying that\x01",
            "you come back smiling\x01",
            "together with KeA.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 5)
    Jump("loc_D334")

    label("loc_D153")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2B7")

    ChrTalk(
        0x10,
        (
            "#01303FLloyd, everyone...\x01",
            "Be careful until the end.\x02\x03",
            "#01302FI'll be here praying that\x01",
            "you come back smiling\x01",
            "together with KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, wait for us.\x02\x03",
            "#00003F(...In any case, I even have confirmed\x01",
            "the truth of big brother's incident, but...\x01",
            "It seems I shouldn't tell her now.)\x02\x03",
            "#00008F(I must formally ask\x01",
            "Lawyer Ian too...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_D334")

    label("loc_D2B7")


    ChrTalk(
        0x10,
        (
            "#01303FLloyd, everyone...\x01",
            "Be careful until the end.\x02\x03",
            "I'll be here praying that\x01",
            "you come back smiling\x01",
            "together with KeA.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D334")

    Jump("loc_D5BD")

    label("loc_D339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D598")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D354")
    Call(0, 96)
    Jump("loc_D593")

    label("loc_D354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D51E")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D463")
    TurnDirection(0x10, 0x106, 0)

    ChrTalk(
        0x10,
        (
            "#01300FMiss Rixia, please\x01",
            "be careful too.\x02\x03",
            "#01304FIlya doesn't say it directly,\x01",
            "but I think that she always\x01",
            "weighs you on her mind.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D425")

    ChrTalk(
        0x106,
        "#10708F...I see...\x02",
    )

    CloseMessageWindow()
    Jump("loc_D45E")

    label("loc_D425")


    ChrTalk(
        0x106,
        (
            "#10702FYes...! I promise you\x01",
            "I'll come back safely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D45E")

    Jump("loc_D516")

    label("loc_D463")


    ChrTalk(
        0x10,
        (
            "#01300FDon't forget the promise to all\x01",
            "come back together with KeA...\x01",
            "All right?\x02\x03",
            "#01304FI think that until that promise\x01",
            "exists, I will be able to stay\x01",
            "here waiting for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D516")

    SetScenarioFlags(0x0, 7)
    Jump("loc_D593")

    label("loc_D51E")


    ChrTalk(
        0x10,
        (
            "#01300FI will stay here,\x01",
            "waiting for you all.\x02\x03",
            "#01304FMay the blessing of the Goddess\x01",
            "be with you all, Lloyd...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D593")

    Jump("loc_D5BD")

    label("loc_D598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_D5A6")
    Jump("loc_D5BD")

    label("loc_D5A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_D5B4")
    Jump("loc_D5BD")

    label("loc_D5B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_D5BD")

    label("loc_D5BD")

    TalkEnd(0xFE)
    Return()

    # Function_95_CB16 end

    def Function_96_D5C1(): pass

    label("Function_96_D5C1")

    EventBegin(0x0)
    Fade(500)
    OP_68(-24280, 400, -23490, 0)
    MoveCamera(32, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15570, 0)
    SetChrPos(0x101, -24090, -1000, -22920, 180)
    SetChrPos(0x102, -25290, -1000, -22000, 180)
    SetChrPos(0x103, -22850, -1000, -22000, 225)
    SetChrPos(0x104, -24260, -1000, -21430, 180)
    SetChrPos(0xF4, -22050, -1000, -22590, 225)
    SetChrPos(0xF5, -22790, -1000, -20810, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x10, 0x0)
    OP_93(0x10, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        "#5P#00000FSister Cecil...so you were here.\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x10, 0x101, 300)

    ChrTalk(
        0x10,
        (
            "#12P#01300FYes, of course after that thing\x01",
            "appeared I was shocked...\x02\x03",
            "#01304F...Still, what a mysterious tree.\x02\x03",
            "Although it is clearly an alien thing,\x01",
            "somehow it is lovely...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108F(Bell said that the\x01",
            ""huge tree" is\x01",
            ""KeA herself"...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D812")

    ChrTalk(
        0x105,
        (
            "#11P#10403F(Maybe it's not strange\x01",
            "she feels that way.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D8D0")

    label("loc_D812")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D872")

    ChrTalk(
        0x109,
        (
            "#11P#10103F(Being Miss Cecil, maybe it's not\x01",
            "odd she feels that way.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D8D0")

    label("loc_D872")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D8D0")

    ChrTalk(
        0x106,
        (
            "#11P#10703F(Being Miss Cecil, maybe it's not\x01",
            "stange she feels that way.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8D0")

    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)

    ChrTalk(
        0x10,
        (
            "#12P#01303FLloyd, everyone...\x02\x03",
            "#01301F...You are heading there, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003F...Yeah.\x02\x03",
            "#00001FIn that "huge tree" the whole truth and KeA...\x01",
            "Are waiting for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00101FNo matter what dangers await \x01",
            "us from now on, we have to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#12P#01308FI see...\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)

    ChrTalk(
        0x10,
        (
            "#12P#01303FThe truth is that I don't want\x01",
            "you to face such dangers...\x02\x03",
            "#01308FI lost an important person to me once.\x01",
            "...I don't want to taste that feeling anymore.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DAF0")

    ChrTalk(
        0x106,
        "#11P#10705FMiss Cecil...\x02",
    )

    CloseMessageWindow()
    Jump("loc_DB4F")

    label("loc_DAF0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB22")

    ChrTalk(
        0x10A,
        "#11P#00608F............\x02",
    )

    CloseMessageWindow()
    Jump("loc_DB4F")

    label("loc_DB22")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB4F")

    ChrTalk(
        0x105,
        "#11P#10408F............\x02",
    )

    CloseMessageWindow()

    label("loc_DB4F")


    ChrTalk(
        0x10,
        (
            "#12P#01303F...However, if Guy was alive...\x01",
            "I think he would try to do the\x01",
            "same thing you all are doing.\x02\x03",
            "#01302FI think he would have dashed to\x01",
            "protect the things important to\x01",
            "him no matter the dangers there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00000FSister Cecil... \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#01304F...That is why, everyone,\x01",
            "promise me just one thing.\x02\x03",
            "#01300FThat you will all come back safely,\x01",
            "together with KeA.\x02\x03",
            "#01309FI think that until that promise\x01",
            "exists, I will be able to stay\x01",
            "here waiting for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00005FSister Cecil...\x02\x03",
            "#00004F...All right.\x01",
            "Wait for us just a little longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00200FIt will be a really\x01",
            "severe trial, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00102FYes, we'll absolutely return\x01",
            "after taking KeA back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00309FWe must also beat some sense\x01",
            "into that ol' man Arios.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DE74")

    ChrTalk(
        0x10A,
        "#11P#00602FYeah, of course.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DEDA")

    label("loc_DE74")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DEAC")

    ChrTalk(
        0x109,
        "#11P#10102FYes, that's right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DEDA")

    label("loc_DEAC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DEDA")

    ChrTalk(
        0x105,
        "#11P#10402FHu hu, right.\x02",
    )

    CloseMessageWindow()

    label("loc_DEDA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6D), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E1B2")

    ChrTalk(
        0x10,
        (
            "#12P#01304F...Uh uh, thank you, everyone.\x01",
            "Now I can finally relax.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)

    ChrTalk(
        0x10,
        (
            "#12P#01309FThen, as a symbol of our promise,\x01",
            "I think I will give you this.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3A0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x3A0, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1DE, 2)

    ChrTalk(
        0x101,
        "#5P#00005FWhat is this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#01300FSomething that Guy gave me \x01",
            "when I undertook the nurse test.\x02\x03",
            "#01304FIf you grasp it tightly in tough times,\x01",
            "you mysteriously feel courage gushing out...\x01",
            "It is that kind of amulet.\x02\x03",
            "#01300FIt is something very precious to me,\x01",
            "so come back safely and hand it back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00000F...Yeah, got it.\x01",
            "We'll borrow it with gratitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#01309FUh uh, may the blessing\x01",
            "of the Goddess be upon\x01",
            "you all, Lloyd...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E242")

    label("loc_E1B2")


    ChrTalk(
        0x10,
        (
            "#12P#01304F...Uh uh, thank you, everyone.\x01",
            "With this I can finally relax.\x02\x03",
            "#01309FMay the blessing of the Goddess\x01",
            "be upon you all, Lloyd...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E242")

    OP_5A()
    SetScenarioFlags(0x1AC, 4)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -24090, -1000, -22920, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E28B")
    OP_E0(0x34, 0x0)

    label("loc_E28B")

    EventEnd(0x5)
    Return()

    # Function_96_D5C1 end

    def Function_97_E28E(): pass

    label("Function_97_E28E")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E31C")

    ChrTalk(
        0x101,
        (
            "#00000FUntil Fran has finished to prepare,\x01",
            "we can't leave the hospital.\x02\x03",
            "Let's go visit Miss Ilya\x01",
            "and Inspector Donovan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E31C")

    Sleep(50)
    SetChrPos(0x0, -61000, 0, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_97_E28E end

    def Function_98_E333(): pass

    label("Function_98_E333")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "St.Ursula \x01",
            "Medical College\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_98_E333 end

    def Function_99_E389(): pass

    label("Function_99_E389")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Medical College\x01",
            "～Auberge  "Le Rekuche"～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_99_E389 end

    SaveToFile()

Try(main)
