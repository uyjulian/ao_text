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
        "Function_7_1821",         # 07, 7
        "Function_8_194E",         # 08, 8
        "Function_9_1975",         # 09, 9
        "Function_10_1A09",        # 0A, 10
        "Function_11_2E41",        # 0B, 11
        "Function_12_3C25",        # 0C, 12
        "Function_13_4450",        # 0D, 13
        "Function_14_45FD",        # 0E, 14
        "Function_15_4699",        # 0F, 15
        "Function_16_47AE",        # 10, 16
        "Function_17_4A7E",        # 11, 17
        "Function_18_4B1C",        # 12, 18
        "Function_19_4E59",        # 13, 19
        "Function_20_4EAD",        # 14, 20
        "Function_21_4F74",        # 15, 21
        "Function_22_5D3E",        # 16, 22
        "Function_23_5D4E",        # 17, 23
        "Function_24_5D61",        # 18, 24
        "Function_25_5D74",        # 19, 25
        "Function_26_5D87",        # 1A, 26
        "Function_27_5D9A",        # 1B, 27
        "Function_28_6646",        # 1C, 28
        "Function_29_672A",        # 1D, 29
        "Function_30_67E1",        # 1E, 30
        "Function_31_68A1",        # 1F, 31
        "Function_32_691D",        # 20, 32
        "Function_33_698C",        # 21, 33
        "Function_34_69C6",        # 22, 34
        "Function_35_6A15",        # 23, 35
        "Function_36_6A4F",        # 24, 36
        "Function_37_6A89",        # 25, 37
        "Function_38_6AD8",        # 26, 38
        "Function_39_6B12",        # 27, 39
        "Function_40_6B4C",        # 28, 40
        "Function_41_761D",        # 29, 41
        "Function_42_7732",        # 2A, 42
        "Function_43_77D0",        # 2B, 43
        "Function_44_77FC",        # 2C, 44
        "Function_45_7807",        # 2D, 45
        "Function_46_7FA0",        # 2E, 46
        "Function_47_7FC2",        # 2F, 47
        "Function_48_7FE7",        # 30, 48
        "Function_49_800C",        # 31, 49
        "Function_50_8024",        # 32, 50
        "Function_51_803C",        # 33, 51
        "Function_52_8054",        # 34, 52
        "Function_53_806C",        # 35, 53
        "Function_54_98CC",        # 36, 54
        "Function_55_98FB",        # 37, 55
        "Function_56_992F",        # 38, 56
        "Function_57_99BF",        # 39, 57
        "Function_58_9A0D",        # 3A, 58
        "Function_59_9A21",        # 3B, 59
        "Function_60_9A92",        # 3C, 60
        "Function_61_9AA1",        # 3D, 61
        "Function_62_9B2A",        # 3E, 62
        "Function_63_9B2F",        # 3F, 63
        "Function_64_9BD5",        # 40, 64
        "Function_65_9BDA",        # 41, 65
        "Function_66_9C5C",        # 42, 66
        "Function_67_9D03",        # 43, 67
        "Function_68_9D9A",        # 44, 68
        "Function_69_9DBF",        # 45, 69
        "Function_70_9DE4",        # 46, 70
        "Function_71_9E2F",        # 47, 71
        "Function_72_9E8C",        # 48, 72
        "Function_73_9EC6",        # 49, 73
        "Function_74_9ED6",        # 4A, 74
        "Function_75_9EE9",        # 4B, 75
        "Function_76_9F0D",        # 4C, 76
        "Function_77_9F31",        # 4D, 77
        "Function_78_9F55",        # 4E, 78
        "Function_79_9F79",        # 4F, 79
        "Function_80_A536",        # 50, 80
        "Function_81_A591",        # 51, 81
        "Function_82_A5AB",        # 52, 82
        "Function_83_A5C8",        # 53, 83
        "Function_84_A5E5",        # 54, 84
        "Function_85_A5FF",        # 55, 85
        "Function_86_A61C",        # 56, 86
        "Function_87_A659",        # 57, 87
        "Function_88_A65A",        # 58, 88
        "Function_89_A675",        # 59, 89
        "Function_90_A6A0",        # 5A, 90
        "Function_91_B372",        # 5B, 91
        "Function_92_B373",        # 5C, 92
        "Function_93_BBFF",        # 5D, 93
        "Function_94_BEED",        # 5E, 94
        "Function_95_C83E",        # 5F, 95
        "Function_96_D2C1",        # 60, 96
        "Function_97_DF5D",        # 61, 97
        "Function_98_E002",        # 62, 98
        "Function_99_E056",        # 63, 99
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
            "#1KIt's a bus stop. Ride the bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City South Entrance\x01",      # 0
            "Fork (Near Sandbank)\x01",               # 1
            "Cancel\x01",                             # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F9")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1819")

    label("loc_17F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1819")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()

    label("loc_1819")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_6_1757 end

    def Function_7_1821(): pass

    label("Function_7_1821")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_194A")
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

    def lambda_1901():
        OP_95(0xFE, -59000, 0, 500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1901)
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

    label("loc_194A")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_7_1821 end

    def Function_8_194E(): pass

    label("Function_8_194E")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -56560, 0, 4080, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_8_194E end

    def Function_9_1975(): pass

    label("Function_9_1975")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_19D0")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19C5")
    Sound(2502, 255, 100, 0)
    Jump("loc_19CB")

    label("loc_19C5")

    Sound(2503, 255, 100, 0)

    label("loc_19CB")

    Jump("loc_19F4")

    label("loc_19D0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19EE")
    Sound(3347, 255, 100, 0)
    Jump("loc_19F4")

    label("loc_19EE")

    Sound(3348, 255, 100, 0)

    label("loc_19F4")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_1975 end

    def Function_10_1A09(): pass

    label("Function_10_1A09")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1BDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B28")

    ChrTalk(
        0x8,
        (
            "Hey now... What in the\x01",
            "world is that huge tree\x01",
            "glowing with bluish light?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To think something like that appeared\x01",
            "all of a sudden... There's no way I\x01",
            "can understand something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I-In any case, I've got\x01",
            "to get myself fired up\x01",
            "and guard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BDA")

    label("loc_1B28")


    ChrTalk(
        0x8,
        (
            "To think something like that appeared\x01",
            "all of a sudden... There's no way I\x01",
            "can understand something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I-In any case, I've got\x01",
            "to get myself fired up\x01",
            "and guard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDA")

    Jump("loc_2E3D")

    label("loc_1BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1DA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC2")

    ChrTalk(
        0x8,
        (
            "Because of the state independence\x01",
            "declaration of invalidity, the State\x01",
            "Guard seems like it's in in chaos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ambulances and bus guard\x01",
            "services are continuing, but\x01",
            "there's a lot to worry about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D9B")

    label("loc_1CC2")


    ChrTalk(
        0x8,
        (
            "Because of the state independence\x01",
            "declaration of invalidity, the State\x01",
            "Guard seems like it's in in chaos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Without the State Guard's protection,\x01",
            "ambulances can't come and go, so\x01",
            "there's a lot to worry about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D9B")

    Jump("loc_2E3D")

    label("loc_1DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1FE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F0A")

    ChrTalk(
        0x8,
        (
            "Since ambulances can't come and go without\x01",
            "the State Guard's protection, it's not a\x01",
            "good situation to be perfectly honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The Cryptid that appeared on the highway and\x01",
            "the State Guard's movement restrictions...\x01",
            "Those are our two main problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd like them to at least\x01",
            "spare a few more people\x01",
            "for guarding the highway.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FE4")

    label("loc_1F0A")


    ChrTalk(
        0x8,
        (
            "Since ambulances can't come and go without\x01",
            "the State Guard's protection, it's not a\x01",
            "good situation to be perfectly honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd like the State Guard to at\x01",
            "least spare a few more people\x01",
            "for highway protection.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FE4")

    Jump("loc_2E3D")

    label("loc_1FE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2193")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E5")

    ChrTalk(
        0x8,
        (
            "Those State Guard guys were\x01",
            "looking for a fugitive who\x01",
            "escaped from prison, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It appears they quickly\x01",
            "withdrew for some reason.\x01",
            "I wonder what happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Oh, well. At any\x01",
            "rate, I must return to\x01",
            "my watch.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_218E")

    label("loc_20E5")


    ChrTalk(
        0x8,
        (
            "The State Guard came looking for a\x01",
            "fugitive who escaped from prison,\x01",
            "but they withdrew quickly, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Oh, well. At any\x01",
            "rate, I must return to\x01",
            "my watch.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_218E")

    Jump("loc_2E3D")

    label("loc_2193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2537")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23BB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_233A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A0")

    ChrTalk(
        0x8,
        (
            "Oh man, trying to swindle\x01",
            "medical supplies... What\x01",
            "an awful guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Still, thank goodness\x01",
            "you recovered them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If I said that to everyone\x01",
            "while they're doing their best,\x01",
            "they'd be sad, wouldn't they.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2335")

    label("loc_22A0")


    ChrTalk(
        0x8,
        (
            "Oh man, trying to swindle\x01",
            "medical supplies... What\x01",
            "an awful guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If I said that to everyone\x01",
            "while they're doing their\x01",
            "best, they'd be sad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2335")

    Jump("loc_23B6")

    label("loc_233A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_23B6")

    ChrTalk(
        0x8,
        (
            "Oh man, swindling\x01",
            "medical goods... What an\x01",
            "awful guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Doing that to people in\x01",
            "need... What scum.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23B6")

    label("loc_23B6")

    Jump("loc_2532")

    label("loc_23BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24AB")

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
            "to St. Ursula Medical\x01",
            "School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you're here for a\x01",
            "visit, please please\x01",
            "check in at the 1F lobby.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2532")

    label("loc_24AB")


    ChrTalk(
        0x8,
        (
            "Due to the recent attack,\x01",
            "there's been a sudden\x01",
            "increase in patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The doctors are crazy\x01",
            "busy. I must do my best\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2532")

    Jump("loc_2E3D")

    label("loc_2537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2706")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2654")

    ChrTalk(
        0x8,
        (
            "Maaan, it's raining today,\x01",
            "huh. Guarding is tough\x01",
            "when it's like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even so, many ambulances\x01",
            "came in yesterday. It\x01",
            "was terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems there's been a big accident.\x01",
            "The fact that there were no casualties\x01",
            "can only be said to be a miracle.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2701")

    label("loc_2654")


    ChrTalk(
        0x8,
        (
            "Yesterday many\x01",
            "ambulances came in. It\x01",
            "was terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems there's been a big accident.\x01",
            "The fact that there were no casualties\x01",
            "can only be said to be a miracle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2701")

    Jump("loc_2E3D")

    label("loc_2706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_27BF")

    ChrTalk(
        0x8,
        (
            "It appears that the\x01",
            "bracers are investigating\x01",
            "many different places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems there are also rumors\x01",
            "of large monsters appearing...\x01",
            "I must stay on guard as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E3D")

    label("loc_27BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_293D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28C4")

    ChrTalk(
        0x8,
        (
            "Hi, welcome to St.\x01",
            "Ursula Medical School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just before, Professor\x01",
            "Seiland walked to the\x01",
            "lounge area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems the professor has been spending\x01",
            "her break time there lately. ...She must\x01",
            "have a lot of things to think about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2938")

    label("loc_28C4")


    ChrTalk(
        0x8,
        (
            "Professor Seiland has\x01",
            "been going to the lounge\x01",
            "often lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...She must have many\x01",
            "things to think about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2938")

    Jump("loc_2E3D")

    label("loc_293D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_29FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2958")
    Call(0, 15)
    Jump("loc_29F7")

    label("loc_2958")


    ChrTalk(
        0x8,
        (
            "Oh. At the time, the cause seemed\x01",
            "to have been Xilun's mistake\x01",
            "filling out the order forms...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyhow, I don't think\x01",
            "there'll be a problem\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29F7")

    Jump("loc_2E3D")

    label("loc_29FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2C41")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2A9A")

    ChrTalk(
        0x8,
        (
            "Archduke Albert's\x01",
            "limousine left some time\x01",
            "ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Maaan. I was awfully tense,\x01",
            "but... I'm glad I could\x01",
            "welcome him properly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C3C")

    label("loc_2A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B8E")

    ChrTalk(
        0x8,
        (
            "Archduke Albert of\x01",
            "Remiferia is here for an\x01",
            "inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Maaan. I'd heard he would be\x01",
            "visiting, but when it came time to\x01",
            "welcome him, I was super tense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I mustn't do any\x01",
            "discourtesy to him until\x01",
            "he returns home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C3C")

    label("loc_2B8E")


    ChrTalk(
        0x8,
        (
            "Maaan. I'd heard he would be\x01",
            "visiting, but when it came time to\x01",
            "welcome him, I was super tense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I mustn't do any\x01",
            "discourtesy to the Archduke\x01",
            "until he returns home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C3C")

    Jump("loc_2E3D")

    label("loc_2C41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D62")

    ChrTalk(
        0x8,
        (
            "Hi, good morning. This\x01",
            "is St. Ursula Medical\x01",
            "School Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since it's long, a lot of people\x01",
            "shorten it to "St. Ursula Hospital"\x01",
            "or "St. Ursula Medical School".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, the reception desk for\x01",
            "medical exams and visits is\x01",
            "in the building in the back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E3D")

    label("loc_2D62")


    ChrTalk(
        0x8,
        (
            "Even the wound I suffered when I was shot\x01",
            "during the cult incident was completely\x01",
            "cured by one of the doctors here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Medical technology, the pride of\x01",
            "St. Ursula Medical School, is\x01",
            "truly great! ...Just kidding.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E3D")

    TalkEnd(0xFE)
    Return()

    # Function_10_1A09 end

    def Function_11_2E41(): pass

    label("Function_11_2E41")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3080")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FB3")

    ChrTalk(
        0x9,
        (
            "It seems the State Guard has assigned\x01",
            "people to escort the ambulances and\x01",
            "buses that travel the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The people who were injured in the attack on the\x01",
            "city and also those who haven't been able to come\x01",
            "for a while are now arriving in fair numbers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even Bracer Eolia came to\x01",
            "help us... The hospital\x01",
            "might be secure for now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_307B")

    label("loc_2FB3")


    ChrTalk(
        0x9,
        (
            "Even Bracer Eolia came to\x01",
            "help us... The hospital\x01",
            "might be secure for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, after that huge tree appeared,\x01",
            "anxiety is spreading amongst the\x01",
            "patients. I must do my very best as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_307B")

    Jump("loc_3C21")

    label("loc_3080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3221")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_318C")

    ChrTalk(
        0x9,
        (
            "The hospitalized patients\x01",
            "seem very worried about\x01",
            "their families in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since we can't easily communicate\x01",
            "with the outside, we can't do\x01",
            "anything about that, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We must relieve the\x01",
            "patients' worries\x01",
            "somehow or other.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_321C")

    label("loc_318C")


    ChrTalk(
        0x9,
        (
            "The hospitalized patients\x01",
            "seem very worried about\x01",
            "their families in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We must relieve the\x01",
            "patients' worries\x01",
            "somehow or other.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_321C")

    Jump("loc_3C21")

    label("loc_3221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3350")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32EF")

    ChrTalk(
        0x9,
        (
            "I hold the decisions of little bro\x01",
            "and friends in higher esteem than\x01",
            "either State Guard or the President.\x02",
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
            "Also, and don't worry\x01",
            "Cecil too much, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_334B")

    label("loc_32EF")


    ChrTalk(
        0x9,
        (
            "Please be safe, little\x01",
            "bro and friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Also, and don't worry\x01",
            "Cecil too much, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_334B")

    Jump("loc_3C21")

    label("loc_3350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3475")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_342D")

    ChrTalk(
        0x9,
        (
            "It seems you guys have\x01",
            "been fighting the State\x01",
            "Guard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...Uhh, no, don't worry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No matter what happens,\x01",
            "we will support you and\x01",
            "your friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F...Thank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3470")

    label("loc_342D")


    ChrTalk(
        0x9,
        (
            "No matter what happens,\x01",
            "we will support you and\x01",
            "your friends.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3470")

    Jump("loc_3C21")

    label("loc_3475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_354D")

    ChrTalk(
        0x9,
        (
            "Due to the incident, a\x01",
            "lot of patients were\x01",
            "brought here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We really can't keep up with their treatments...\x01",
            "The situation is such that a lot people who need\x01",
            "surgery are waiting for their turn.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C21")

    label("loc_354D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_355B")
    Jump("loc_3C21")

    label("loc_355B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_367B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_362E")

    ChrTalk(
        0x9,
        (
            "Shizuku seems to be\x01",
            "quite positive towards\x01",
            "her surgery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That child doesn't give\x01",
            "up, so we around her\x01",
            "mustn't be pessimistic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Yes, we have to\x01",
            "believe and do our best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3676")

    label("loc_362E")


    ChrTalk(
        0x9,
        (
            "We must do our best to\x01",
            "believe in Shizuku's\x01",
            "full recovery as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3676")

    Jump("loc_3C21")

    label("loc_367B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3797")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3742")

    ChrTalk(
        0x9,
        (
            "They say only Professor Seiland\x01",
            "could have done that complex\x01",
            "and operation. However...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Shizuku... Maybe she can't\x01",
            "be fully cured with current\x01",
            "medical technology.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3792")

    label("loc_3742")


    ChrTalk(
        0x9,
        (
            "Shizuku... Maybe she can't\x01",
            "be fully cured with current\x01",
            "medical technology.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3792")

    Jump("loc_3C21")

    label("loc_3797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_38D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3848")

    ChrTalk(
        0x9,
        (
            "It appears that the\x01",
            "trade conference will at\x01",
            "last be held today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder what kind of\x01",
            "conference it will be. I\x01",
            "have check it out properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38CF")

    label("loc_3848")


    ChrTalk(
        0x9,
        (
            "But both Filia and Ran\x01",
            "seem to be\x01",
            "uninterested...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder what kind of\x01",
            "conference it will be. I\x01",
            "have check it out properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38CF")

    Jump("loc_3C21")

    label("loc_38D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3A64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F3")

    ChrTalk(
        0x9,
        (
            "Earlier, Archduke Albert\x01",
            "came and personally\x01",
            "introduced himself to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Being the sovereign of a whole\x01",
            "country, I thought he might be a\x01",
            "prideful man for some reason, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If he would speak to a\x01",
            "nurse like me, he's an\x01",
            "unexpectedly friendly man.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A5F")

    label("loc_39F3")


    ChrTalk(
        0x9,
        (
            "Archduke Albert seems to\x01",
            "be an unexpectedly\x01",
            "friendly man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, it was a really\x01",
            "familiar feeling.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A5F")

    Jump("loc_3C21")

    label("loc_3A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3C21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BBD")

    ChrTalk(
        0x9,
        (
            "Oh, Randy and little\x01",
            "bro. Long time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F("Little bro", huh...\x01",
            "They really labeled me\x01",
            "with that...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHaha, how have you guys\x01",
            "been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Good. Filia and Ran are\x01",
            "the same as always too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You seem to have some\x01",
            "new members...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If we get the chance,\x01",
            "let's go have fun again\x01",
            "sometime.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 4)
    Jump("loc_3C21")

    label("loc_3BBD")


    ChrTalk(
        0x9,
        (
            "Haha, I'm happy to see\x01",
            "you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If we get the chance,\x01",
            "let's go have fun again\x01",
            "sometime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C21")

    TalkEnd(0xFE)
    Return()

    # Function_11_2E41 end

    def Function_12_3C25(): pass

    label("Function_12_3C25")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C36")
    Jump("loc_444C")

    label("loc_3C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3C44")
    Jump("loc_444C")

    label("loc_3C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3C52")
    Jump("loc_444C")

    label("loc_3C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3E45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D75")

    ChrTalk(
        0xA,
        (
            "Much of the equipment we use at\x01",
            "the hospital was purchased from\x01",
            "a merchant named Harold, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now we're entirely\x01",
            "relying on State Guard\x01",
            "supplies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't say they're good quality,\x01",
            "but the situation is what it is\x01",
            "and we can't do anything about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E40")

    label("loc_3D75")


    ChrTalk(
        0xA,
        (
            "We're relying on the State Guard\x01",
            "supplies for much of the\x01",
            "equipment we use at the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't say they're good quality,\x01",
            "but the situation is what it is\x01",
            "and we can't do anything about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E40")

    Jump("loc_444C")

    label("loc_3E45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4024")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F7A")

    ChrTalk(
        0xA,
        (
            "An attack on Crossbell\x01",
            "City... A really unthinkable\x01",
            "incident has happened, hmm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although it's been about a\x01",
            "week since, I still can't\x01",
            "wipe the shock from my mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although the reconstruction is\x01",
            "proceeding, I wonder if Crossbell\x01",
            "will be able to regain its footing...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_401F")

    label("loc_3F7A")


    ChrTalk(
        0xA,
        (
            "Although the reconstruction is\x01",
            "proceeding, I think the shock\x01",
            "from the attack was really great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wonder if Crossbell\x01",
            "will be able to regain\x01",
            "its footing...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_401F")

    Jump("loc_444C")

    label("loc_4024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4032")
    Jump("loc_444C")

    label("loc_4032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_40B2")

    ChrTalk(
        0xA,
        (
            "This container... There\x01",
            "are loads of spirit\x01",
            "warding dolls inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...Why are those things\x01",
            "are in there?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_444C")

    label("loc_40B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4209")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4197")

    ChrTalk(
        0xA,
        (
            "They say that the\x01",
            "independence proposal is\x01",
            "a hot topic in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In a way, it could be\x01",
            "said to be a Crossbell\x01",
            "citizen's greatest wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I am completely in favor\x01",
            "of independence myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4204")

    label("loc_4197")


    ChrTalk(
        0xA,
        (
            "I am completely in favor\x01",
            "of independence myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I must remember to\x01",
            "participate in the\x01",
            "referendum.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4204")

    Jump("loc_444C")

    label("loc_4209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4217")
    Jump("loc_444C")

    label("loc_4217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4443")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4363")

    ChrTalk(
        0xA,
        (
            "In the Principality of Remiferia, they\x01",
            "say the Archduke's family puts special\x01",
            "effort into the field of medical care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Remiferia, the country with\x01",
            "advanced medical care. You've\x01",
            "heard that too, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm. It would be nice to live\x01",
            "in a country like that and not\x01",
            "worry about illnesses so much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_443E")

    label("loc_4363")


    ChrTalk(
        0xA,
        (
            "In the Principality of Remiferia, they\x01",
            "say the Archduke's family puts special\x01",
            "effort into the field of medical care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm. It would be nice to live\x01",
            "in a country like that and not\x01",
            "worry about illnesses so much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_443E")

    Jump("loc_444C")

    label("loc_4443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_444C")

    label("loc_444C")

    TalkEnd(0xFE)
    Return()

    # Function_12_3C25 end

    def Function_13_4450(): pass

    label("Function_13_4450")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4597")

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
        (
            "...Ah, it's you all,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm sorry, but I'm busy\x01",
            "now. Could you leave me\x01",
            "alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F(As I thought, maybe\x01",
            "she's worried about\x01",
            "Shizuku's surgery...)\x02",
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
    Jump("loc_45F9")

    label("loc_4597")


    ChrTalk(
        0xB,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(It looks like she's\x01",
            "deep in thought. ...We\x01",
            "shouldn't disturb her.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45F9")

    TalkEnd(0xFE)
    Return()

    # Function_13_4450 end

    def Function_14_45FD(): pass

    label("Function_14_45FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4612")
    Call(0, 15)
    Jump("loc_4695")

    label("loc_4612")


    ChrTalk(
        0xC,
        (
            "#03605FBy the way... Are 30\x01",
            "sheets alright?\x02\x03",
            "#03600FBefore, you ordered 500\x01",
            "sheets instead of 50, so\x01",
            "I'd like to make sure...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4695")

    TalkEnd(0xFE)
    Return()

    # Function_14_45FD end

    def Function_15_4699(): pass

    label("Function_15_4699")

    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x8,
        (
            "Hey, if it isn't Harold.\x01",
            "Why are you here today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#03600FWell, I came to deliver\x01",
            "the sheets you ordered.\x02\x03",
            "I'd like to deliver them\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh. In that case, I\x01",
            "guess I'll help carry\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#03609FHaha. Thanks for your\x01",
            "help, as always.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_15_4699 end

    def Function_16_47AE(): pass

    label("Function_16_47AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4924")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4898")

    ChrTalk(
        0xFE,
        (
            "Thank goodness the\x01",
            "medical goods got here\x01",
            "safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so... To think there was\x01",
            "such a nasty guy in this time\x01",
            "of crisis for Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "T-Though I'm relieved\x01",
            "now that he's been\x01",
            "caught.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_491F")

    label("loc_4898")


    ChrTalk(
        0xFE,
        (
            "To think there was such a\x01",
            "nasty guy in this time of\x01",
            "crisis for Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "T-Though I'm relieved\x01",
            "now that he's been\x01",
            "caught.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_491F")

    Jump("loc_4A7A")

    label("loc_4924")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_4A7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A09")

    ChrTalk(
        0xFE,
        (
            "Crap, I couldn't deliver\x01",
            "the medical supplies in\x01",
            "this time of crisis...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, what's done is\x01",
            "done, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't worry about it,\x01",
            "guys. Change your way of\x01",
            "thinking and do your job.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4A7A")

    label("loc_4A09")


    ChrTalk(
        0xFE,
        (
            "What's done is done, I\x01",
            "guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't worry about it,\x01",
            "guys. Change your way of\x01",
            "thinking and do your job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A7A")

    TalkEnd(0xFE)
    Return()

    # Function_16_47AE end

    def Function_17_4A7E(): pass

    label("Function_17_4A7E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4B18")

    ChrTalk(
        0xF,
        (
            "This is Archduke\x01",
            "Albert's private\x01",
            "limousine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Mr. Arios is accompanying His\x01",
            "Excellency as a bodyguard, so\x01",
            "I have no reason to worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B18")

    TalkEnd(0xFE)
    Return()

    # Function_17_4A7E end

    def Function_18_4B1C(): pass

    label("Function_18_4B1C")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B4E")
    SetScenarioFlags(0x31, 2)

    label("loc_4B4E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_4B8E")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B83")
    Sound(2499, 255, 100, 0)
    Jump("loc_4B89")

    label("loc_4B83")

    Sound(3537, 255, 100, 0)

    label("loc_4B89")

    Jump("loc_4B94")

    label("loc_4B8E")

    Sound(3344, 255, 100, 0)

    label("loc_4B94")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_4C09")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4BE9"),
        (SWITCH_DEFAULT, "loc_4BFA"),
    )


    label("loc_4BE9")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_4C04")

    label("loc_4BFA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C04")

    Jump("loc_4E46")

    label("loc_4C09")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_4C3B")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_4C3B")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4C6F"),
        (1, "loc_4D73"),
        (2, "loc_4E04"),
        (SWITCH_DEFAULT, "loc_4E3C"),
    )


    label("loc_4C6F")

    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4CA0")
    OP_70(0x8, 0x12C)
    OP_71(0x8, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_4CB0")

    label("loc_4CA0")

    OP_70(0x8, 0xF0)
    OP_71(0x8, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_4CB0")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D06")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D06")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D29")
    Sound(461, 0, 100, 0)

    label("loc_4D29")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4D49")
    OP_70(0x8, 0x14A)
    OP_71(0x8, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_4D59")

    label("loc_4D49")

    OP_70(0x8, 0x10E)
    OP_71(0x8, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_4D59")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x8, "light", 0x1, 0x1)
    OP_70(0x8, 0x0)
    Jump("loc_4B94")

    label("loc_4D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_4DE5")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_4DA8")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_4DC0")

    label("loc_4DA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4DBB")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_4DC0")

    label("loc_4DBB")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_4DC0")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4DFF")

    label("loc_4DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4DF5")
    OP_AF(0xFB)
    Jump("loc_4DFF")

    label("loc_4DF5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4DFF")

    Jump("loc_4E46")

    label("loc_4E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E1D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E37")

    label("loc_4E1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4E2D")
    OP_AF(0xFB)
    Jump("loc_4E37")

    label("loc_4E2D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E37")

    Jump("loc_4E46")

    label("loc_4E3C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E46")

    Jump("loc_4B94")

    label("loc_4E4B")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_18_4B1C end

    def Function_19_4E59(): pass

    label("Function_19_4E59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4EA9")
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

    label("loc_4EA9")

    Call(0, 6)
    Return()

    # Function_19_4E59 end

    def Function_20_4EAD(): pass

    label("Function_20_4EAD")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FIt seems we can fish\x01",
            "here.\x02",
        )
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
            "Fish\x01",        # 0
            "Cancel\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F6F")
    OP_E2(0x2)
    MiniGame(0x6, 0x11, 0xFFFFBFBE, 0xFFFFFC18, 0xFFFF9A5C, 0xB4, 0xFFFFBCE4, 0xFFFFF830, 0xFFFF7FFE)

    label("loc_4F6F")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_20_4EAD end

    def Function_21_4F74(): pass

    label("Function_21_4F74")

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

    def lambda_50F5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_50F5)

    ChrTalk(
        0x102,
        (
            "#00105F#12PA call from another\x01",
            "department?\x02",
        )
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
            "#00000F#30WSpecial Support Section,\x01",
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
            "Hehehe...... Hey\x01",
            "darling, it's me.\x02\x03",
            "Do you know who I am?\x02",
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
            "#00012FMichel... Um, what's up?\x02",
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
            "Ahaha. You got me in one\x01",
            "shot! So skillful, you.\x02\x03",
            "Or was it love that led\x01",
            "you to my identity?\x02",
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
            "#00006FNo, it's just that you\x01",
            "were the only logical\x01",
            "choice to think of.\x02\x03",
            "#00000FBy any chance, is KeA\x01",
            "visiting you at the\x01",
            "Guild?\x02",
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
            "Oh, about that.\x02\x03",
            "That child actually went to\x01",
            "Waterfront Area to play with\x01",
            "Shizuku.\x02\x03",
            "Zeit... I think he's called? They're\x01",
            "traveling together with that police\x01",
            "dog, so I think they'll be fine.\x02",
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
            "#00002FYeah, if they're with\x01",
            "Zeit, there shouldn't be\x01",
            "anything to worry about.\x02",
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
            "Oh, really?\x02\x03",
            "I've heard about him, he\x01",
            "has such a strong\x01",
            "presence.\x02\x03",
            "As expected of the\x01",
            "legendary Divine Wolf,\x01",
            "wouldn't you say?\x02",
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
            "#00004FHaha... I think a\x01",
            "legendary wolf would be\x01",
            "quite different.\x02\x03",
            "#00005FSo, is this all you\x01",
            "wanted to tell us with\x01",
            "your call?\x02",
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
            "No, no, let me get to the\x01",
            "point.\x02\x03",
            "Actually, it sounds like\x01",
            "Arios wants to exchange\x01",
            "information with you guys.\x02\x03",
            "He'll be back by this\x01",
            "evening, so could you make\x01",
            "some time for him?\x02",
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
            "#00000FThis evening...? That\x01",
            "should be fine.\x02\x03",
            "About the information\x01",
            "exchange, it's about the\x01",
            "trade conference, right?\x02",
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
            "That's correct, but it's\x01",
            "also... more about Heiyue\x01",
            "and Red Constellation.\x02",
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
            "#00003F...Got it.\x02\x03",
            "#00001FWhen we're finished with\x01",
            "our tasks, we'll make\x01",
            "sure to stop by.\x02",
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
            "Great, I'll be waiting\x01",
            "for you.\x07\x00\x02",
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
            "#00100F#12PWas that Michel from the\x01",
            "Bracer Guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#11PSomethin' come up?\x02",
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
        (
            "#00006F#5PNo, they want to\x01",
            "exchange information\x01",
            "with us.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained Michel's\x01",
            "request to the other\x01",
            "members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00303F#11PHeiyue and Red Constellation?\x02\x03",
            "#00301FIt's true that someone like ol'\x01",
            "Arios could be well informed\x01",
            "about matters out of state too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PHehe, this could end up\x01",
            "helping us.\x02\x03",
            "#10300FSo, are we heading back\x01",
            "to Crossbell City now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#5PNo, Arios won't be back\x01",
            "until this evening.\x02\x03",
            "We should try to finish\x01",
            "up our requests before\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BE2")

    ChrTalk(
        0x102,
        (
            "#00104F#12PWe gathered some basic\x01",
            "information about Red\x01",
            "Constellation, but...\x02\x03",
            "#00102FSince we have a car, it\x01",
            "might be best to visit\x01",
            "some other places too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C8D")

    label("loc_5BE2")


    ChrTalk(
        0x102,
        (
            "#00103F#12PWe haven't gathered that\x01",
            "much information about\x01",
            "Red Constellation, but...\x02\x03",
            "#00100FSince we have a car, it\x01",
            "might be best to visit\x01",
            "several different places.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C8D")


    ChrTalk(
        0x109,
        (
            "#10100F#11PAlright, once we've finished our\x01",
            "business, let's head to the guild\x01",
            "branch office on East Street.\x02",
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

    # Function_21_4F74 end

    def Function_22_5D3E(): pass

    label("Function_22_5D3E")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_22_5D3E end

    def Function_23_5D4E(): pass

    label("Function_23_5D4E")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_23_5D4E end

    def Function_24_5D61(): pass

    label("Function_24_5D61")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_24_5D61 end

    def Function_25_5D74(): pass

    label("Function_25_5D74")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_25_5D74 end

    def Function_26_5D87(): pass

    label("Function_26_5D87")

    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_26_5D87 end

    def Function_27_5D9A(): pass

    label("Function_27_5D9A")

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
            "#00208F#6PAs I thought, there are\x01",
            "many more visitors than\x01",
            "usual...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_621E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_621E)
    Sleep(150)

    def lambda_622E():
        OP_93(0xFE, 0x10F, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_622E)
    Sleep(100)

    def lambda_623E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_623E)
    Sleep(50)

    def lambda_624E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_624E)
    Sleep(50)

    def lambda_625E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_625E)
    Sleep(50)

    def lambda_626E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_626E)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x102,
        (
            "#00106F#11PYes. After all, a large\x01",
            "number of people were\x01",
            "wounded in the city alone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11PInspector Donovan and\x01",
            "Ilya are hospitalized as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6PYes... They both still\x01",
            "seem to be comatose.\x02\x03",
            "#10108FInspector Donovan... It\x01",
            "seems he protected Fran\x01",
            "and the others.\x02\x03",
            "I think Fran's quick\x01",
            "recovery was thanks to\x01",
            "the inspector.\x02",
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
            "#00306F#5PQuite the largehearted\x01",
            "ol' man... Impressive.\x02\x03",
            "#00308FI'd like to visit both\x01",
            "of them if possible,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 4)), scpexpr(EXPR_END)), "loc_64D0")

    ChrTalk(
        0x102,
        (
            "#00103F#11PThat's right... It seems\x01",
            "Sully came to visit\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64E9")

    label("loc_64D0")


    ChrTalk(
        0x102,
        "#00103F#11PRight...\x02",
    )

    CloseMessageWindow()

    label("loc_64E9")


    def lambda_64EE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_64EE)
    Sleep(250)

    ChrTalk(
        0x105,
        (
            "#10300F#5PSo, which is your\x01",
            "sister's room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#6PAh, yes... It's No. 301.\x02\x03",
            "#10100FBefore going there, we\x01",
            "should check in with the\x01",
            "receptionist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PUnderstood, let's go.\x02\x03",
            "#00003F(...Cecil is probably\x01",
            "rather busy.)\x02",
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

    # Function_27_5D9A end

    def Function_28_6646(): pass

    label("Function_28_6646")

    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_6662():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6662)
    OP_95(0xFE, -22000, 0, -1750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, -3750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, -9000, 4000, 0x0)
    Sleep(500)
    BeginChrThread(0x1D, 1, 0, 31)
    OP_95(0xFE, -24000, 0, -3750, 4000, 0x0)
    OP_95(0xFE, -22000, 0, -1750, 4000, 0x0)
    OP_95(0xFE, 2000, 0, -1750, 4000, 0x0)

    def lambda_66F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_66F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_28_6646 end

    def Function_29_672A(): pass

    label("Function_29_672A")

    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_6746():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6746)
    OP_95(0xFE, -22000, 0, 1750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, 3750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, 11000, 4000, 0x0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x1)

    def lambda_67A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_67A8)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_64(0xFE)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_29_672A end

    def Function_30_67E1(): pass

    label("Function_30_67E1")

    Sleep(1000)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_6815():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6815)
    OP_95(0xFE, -24000, 0, 3500, 4000, 0x0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x8)
    OP_95(0xFE, -22000, 0, 1500, 4000, 0x0)
    OP_95(0xFE, 2000, 0, 1500, 4000, 0x0)

    def lambda_686E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_686E)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_64(0xFE)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0x1B, 1, 0, 29)
    Return()

    # Function_30_67E1 end

    def Function_31_68A1(): pass

    label("Function_31_68A1")

    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, -24000, 0, -3500, 4000, 0x0)
    OP_95(0xFE, -22000, 0, -1500, 4000, 0x0)
    OP_95(0xFE, 2000, 0, -1500, 4000, 0x0)

    def lambda_68F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_68F9)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_64(0xFE)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_31_68A1 end

    def Function_32_691D(): pass

    label("Function_32_691D")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x960, 0x0)
    OP_93(0xFE, 0x10E, 0x3E8)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x3E8)
    OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x960, 0x0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x2)

    def lambda_696B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_696B)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x9C4, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_32_691D end

    def Function_33_698C(): pass

    label("Function_33_698C")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0x6D6, 0x0)

    def lambda_69A5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_69A5)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x6D6, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_33_698C end

    def Function_34_69C6(): pass

    label("Function_34_69C6")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0x3E8, 0x0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x2)

    def lambda_69F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_69F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x3E8, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_34_69C6 end

    def Function_35_6A15(): pass

    label("Function_35_6A15")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x6F54, 0x3E8, 0x0)

    def lambda_6A2E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6A2E)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x3E8, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_35_6A15 end

    def Function_36_6A4F(): pass

    label("Function_36_6A4F")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x8CA0, 0x5DC, 0x0)

    def lambda_6A68():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6A68)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x5DC, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_36_6A4F end

    def Function_37_6A89(): pass

    label("Function_37_6A89")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x9858, 0x578, 0x0)

    def lambda_6AA2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6AA2)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x578, 0x0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_37_6A89 end

    def Function_38_6AD8(): pass

    label("Function_38_6AD8")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x9858, 0x44C, 0x0)

    def lambda_6AF1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6AF1)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x44C, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_38_6AD8 end

    def Function_39_6B12(): pass

    label("Function_39_6B12")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0xA028, 0x44C, 0x0)

    def lambda_6B2B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6B2B)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x4B0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_39_6B12 end

    def Function_40_6B4C(): pass

    label("Function_40_6B4C")

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

    def lambda_6C4E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C4E)
    Sleep(100)

    def lambda_6C66():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C66)
    Sleep(50)

    def lambda_6C7E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6C7E)
    Sleep(50)

    def lambda_6C96():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C96)
    Sleep(50)

    def lambda_6CAE():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6CAE)
    Sleep(50)

    def lambda_6CC6():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6CC6)
    OP_68(-48920, 1000, -570, 2700)
    SetCameraDistance(19720, 2700)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_6D20():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6D20)
    Sleep(300)

    def lambda_6D30():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6D30)
    Sleep(300)

    def lambda_6D40():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6D40)
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
            "#00005FSpecial Support Section,\x01",
            "Lloyd Bannings speaking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Young Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ah, there you are.\x02\x03",
            "Where're you now?\x02",
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
            "#00003FNow listen here... It's\x01",
            "polite to give your name when\x01",
            "calling someone, you know.\x02\x03",
            "#00000FSt. Ursula Hospital... What's\x01",
            "wrong, Jona?\x02",
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
            "You guys got back to\x01",
            "doing your support work\x01",
            "today, right?\x02\x03",
            "So I was wondering if\x01",
            "you'd listen to a little\x01",
            "request of mine.\x02",
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
            "#00006FWell, like I told you,\x01",
            "don't look at the police\x01",
            "database as you please...\x02\x03",
            "#00001FAlso, we're quite busy\x01",
            "too, so─\x02",
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
            "Hmmm. Say, who helped you\x01",
            "before with that missing\x01",
            "bracers investigation...?\x02\x03",
            "You said you'd return the\x01",
            "favor, didn't you.\x02",
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
            "#00013FUgh...\x02\x03",
            "#00006F...It can't be helped. I can't\x01",
            "promise we'll accept but we'll\x01",
            "at least hear you out.\x02\x03",
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
            "In that case, come to\x01",
            "the Waterfront Area\x01",
            "lighthouse.\x02\x03",
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
            "#00005FThe lighthouse? Why\x01",
            "there...?\x02",
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
            "Hehe. It'll be a\x01",
            "surprise.\x02\x03",
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
            "#00011F#2PAh... Seriously.\x02",
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
            "#00211F#11PHas Jona made another\x01",
            "selfish request again?\x02",
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
        "#00012F#6PAh, well...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained that they'd\x01",
            "been called to the lighthouse\x01",
            "on the Waterfront Area wharf.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00305F#5PHuh? Why there...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#11PThe Waterfront Area lighthouse...\x01",
            "It's rather close to the\x01",
            "destroyed Heiyue building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#5PIt's true that he helped\x01",
            "us with the search for\x01",
            "Ling and Eolia...\x02\x03",
            "#00100FI think we can at least\x01",
            "hear what he has to say,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#11PWhy don't we head there\x01",
            "on one of our breaks?\x02",
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
            "#00206F#11PWell, he asked such a\x01",
            "selfish thing without any\x01",
            "regard to our circumstances.\x02\x03",
            "#00211FIt won't be a problem if we\x01",
            "make him wait a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#5PHaha, that's certainly\x01",
            "true.\x02",
        )
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

    # Function_40_6B4C end

    def Function_41_761D(): pass

    label("Function_41_761D")

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
            "Bad timing, huh.)\x02",
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

    # Function_41_761D end

    def Function_42_7732(): pass

    label("Function_42_7732")

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

    # Function_42_7732 end

    def Function_43_77D0(): pass

    label("Function_43_77D0")

    OP_74(0xD, 0x1E)
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    SetMapObjFrame(0xD, "mark00", 0x0, 0x1)
    Return()

    # Function_43_77D0 end

    def Function_44_77FC(): pass

    label("Function_44_77FC")

    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    Return()

    # Function_44_77FC end

    def Function_45_7807(): pass

    label("Function_45_7807")

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
        "#5P*sigh*, how boring...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PGuarding a place like\x01",
            "this is just too boring.\x02",
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
            "#6PBannings from that\x01",
            "Support Section is still\x01",
            "on the run, you know.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x13, 500)
    Sleep(100)

    ChrTalk(
        0x12,
        (
            "#5PHa! As if a lone\x01",
            "detective could do\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PCouldn't he have fled\x01",
            "the state a long time\x01",
            "ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#12PStill, rumor has it that\x01",
            "he has an unbelievable\x01",
            "monster with him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#12PIs it true that the 4th\x01",
            "Regiment guys were eaten\x01",
            "by it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x14, 500)
    Sleep(100)

    ChrTalk(
        0x12,
        (
            "#5PHaha. That's probably\x01",
            "just a false rumor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PMore importantly, since\x01",
            "we're here, I'd like pay\x01",
            "my respects to Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PShe's still\x01",
            "hospitalized, right?\x02",
        )
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
            "#11PI hope she recovers\x01",
            "quickly and makes a\x01",
            "comeback, though.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "#11P─Agreed.\x02",
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

    def lambda_7CA6():
        OP_93(0x12, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_7CA6)
    Sleep(50)

    def lambda_7CB6():
        OP_93(0x13, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_7CB6)
    Sleep(50)

    def lambda_7CC6():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_7CC6)
    Sleep(50)

    def lambda_7CD6():
        OP_93(0x15, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_7CD6)
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
        (
            "#11PUgh, to think he'd\x01",
            "actually show up!\x02",
        )
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
            "#01203F#6P#3CGoodness. How rude,\x01",
            "calling me a monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#6PWell, considering your\x01",
            "original form, it can't\x01",
            "really be helped, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P─We have no quarrel with\x01",
            "you.\x02\x03",
            "#00007FHowever, if you stand in\x01",
            "our way, we'll crush you\x01",
            "without mercy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#11PHow impertinent!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11PThey're outnumbered!\x01",
            "Arrest them at once!\x02",
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

    # Function_45_7807 end

    def Function_46_7FA0(): pass

    label("Function_46_7FA0")

    SetChrFlags(0xFE, 0x1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_46_7FA0 end

    def Function_47_7FC2(): pass

    label("Function_47_7FC2")

    Sleep(50)
    SetChrFlags(0xFE, 0x1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_47_7FC2 end

    def Function_48_7FE7(): pass

    label("Function_48_7FE7")

    Sleep(100)
    SetChrFlags(0xFE, 0x1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_48_7FE7 end

    def Function_49_800C(): pass

    label("Function_49_800C")

    SetChrChipByIndex(0x12, 0x27)
    SetChrSubChip(0x12, 0x0)
    OP_9B(0x1, 0xFE, 0xA, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_49_800C end

    def Function_50_8024(): pass

    label("Function_50_8024")

    SetChrChipByIndex(0x13, 0x29)
    SetChrSubChip(0x13, 0x0)
    OP_9B(0x1, 0xFE, 0x15E, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_50_8024 end

    def Function_51_803C(): pass

    label("Function_51_803C")

    SetChrChipByIndex(0x14, 0x26)
    SetChrSubChip(0x14, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_51_803C end

    def Function_52_8054(): pass

    label("Function_52_8054")

    SetChrChipByIndex(0x15, 0x29)
    SetChrSubChip(0x15, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_52_8054 end

    def Function_53_806C(): pass

    label("Function_53_806C")

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
        "#40W#11P...Argh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#40W#11PS-So.. strong...\x02",
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
        (
            "#10404F#5PWell then─ I guess it's\x01",
            "my turn.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(-54200, 800, 860, 1200)
    MoveCamera(36, 25, 0, 1200)
    OP_6E(500, 1200)
    SetCameraDistance(20500, 1200)

    def lambda_845A():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_845A)
    OP_9B(0x0, 0x105, 0x0, 0x190, 0x3E8, 0x0)
    Sleep(300)
    BeginChrThread(0x105, 0, 0, 54)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00005F#12P(A Gralsritter\x01",
            "Medal...?)\x02",
        )
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
            "#10403F#30W#5P#30AO azure seal of mine\x01",
            "shining from the\x01",
            "abyss...\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x105, 0, 0, 56)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10401F#30W#5P#20AJoin with the silver\x01",
            "will and give them false\x01",
            "memories.\x02",
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
        "#50W#11P#2S............\x02",
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
            "#01203F#3C#6P(Hm, it appears to a\x01",
            "suggestive technique of\x01",
            "the Church.)\x02\x03",
            "#01200F(It seems to make use of\x01",
            "some kind of mysterious\x01",
            "power...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5P─Not too long ago, you confirmed a\x01",
            "large-scale Cryptid drawing near.\x02\x03",
            "Somehow you managed to repel it, but\x01",
            "since you all suffered injuries, you\x01",
            "decided to momentarily return to base.\x02\x03",
            "#10401FYou didn't catch sight of Bannings and\x01",
            "you've seen no sign of him for now.\x02",
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
        (
            "#50W#11P#2S......Have seen no sign\x01",
            "of him for now.\x02",
        )
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

    def lambda_8864():

        label("loc_8864")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_8864")

    QueueWorkItem2(0x105, 3, lambda_8864)
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
            "#01203F#12P#3CYou can't concretely manipulate\x01",
            "memories that much with a mere\x01",
            "suggestion technique.\x02\x03",
            "#01200FI suppose you drew power from\x01",
            "your 'Stigma'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#5PHaha... As expected from\x01",
            "a divine beast of\x01",
            "legend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#11PStigma...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5P...Well, it's a trivial old trauma I\x01",
            "suffered.\x02\x03",
            "#10408FAt any rate, since it's not perfect, the\x01",
            "suggestion will wear off in two or three\x01",
            "days.\x02\x03",
            "#10401FBecause the army will be on the lookout,\x01",
            "I want you to act as if this is the last\x01",
            "time I can use that technique.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#11PAlright... I understand.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x103,
        "Young Girl's Voice",
        "#6P#2686V#30W#20AWazy, Zeit...?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)

    def lambda_8BB5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8BB5)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-44070, 400, 120, 2000)
    MoveCamera(76, 17, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(19770, 2000)

    def lambda_8C2D():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8C2D)
    Sleep(50)

    def lambda_8C3D():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8C3D)
    Sleep(50)

    def lambda_8C4D():
        OP_93(0x107, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_8C4D)
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
        "#00005F#11P#12P#NTio!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x107,
        (
            "#01200F#2P#3C#6P#NHmm, looks like you're\x01",
            "ok.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        "#10404F#6P#NMan, that's a relief.\x02",
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
            "#00014F#6PThank goodness! Ever since I\x01",
            "heard you were at the hospital I\x01",
            "wondered how you were doing...\x02\x03",
            "#00002FAre you all right? Are you hurt?\x02",
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
        "#00213F#11P#2687V#50W#25A#2SLloyd....\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        "#00212F#11P#2688V#20W#4S#15A#4SLloyd!!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    BeginChrThread(0x103, 0, 0, 71)
    OP_68(-52640, 1200, -1760, 1800)
    MoveCamera(47, 20, 0, 1800)
    OP_6E(500, 1800)
    SetCameraDistance(17000, 1800)
    WaitChrThread(0x103, 0)

    def lambda_8F49():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8F49)

    def lambda_8F56():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_8F56)
    OP_6F(0x79)
    SetCameraDistance(15500, 40000)

    ChrTalk(
        0x101,
        (
            "#00011F#6PUrk... (H-Her\x01",
            "breastplate is...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x103,
        (
            "#00213F#11P#2689V#60W#25AW-Where have you been!?\x02\x03",
            "#00215F#2690V#25AI heard you were arrested\x01",
            "and jailed!\x02\x03",
            "#00212F#2691V#60AAnd then you escaped and\x01",
            "were pursued by the army...\x01",
            "I-I saw it on the orbal net!\x02\x03",
            "#00213F#2692V#50AI-I... *hic*... I've been\x01",
            "worried this whole time!\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00008F#6PTio...\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 0, 0, 78)
    BeginChrThread(0x103, 0, 0, 77)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x101,
        (
            "#00006F#6P...Sorry for worrying\x01",
            "you.\x02\x03",
            "#00002FBut it's all right now.\x02\x03",
            "Because of Wazy and\x01",
            "Zeit's help, I've\x01",
            "returned to Crossbell...\x02\x03",
            "#00004FSo... You don't have to\x01",
            "worry.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x103,
        "#00215F#11P#2693V#40W#25A...Uuuh... *sob*...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    NpcTalk(
        0x17,
        "Girl's Voice",
        (
            "#11P#2724V#30W#N#25AWhoa whoa... They're so\x01",
            "lovey dovey.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    NpcTalk(
        0x16,
        "Woman's Voice",
        (
            "#11P#N#20A#30WHaha. I feel a little\x01",
            "bad for interrupting\x01",
            "them, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-52280, 1200, -1700, 2500)
    SetCameraDistance(17000, 2500)

    def lambda_92C5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_92C5)

    def lambda_92D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_92D6)
    SetChrPos(0x16, -42500, 0, -1200, 270)
    SetChrPos(0x17, -42500, 0, 0, 270)
    BeginChrThread(0x17, 0, 0, 73)
    Sleep(100)
    BeginChrThread(0x16, 0, 0, 74)
    Sleep(1500)

    ChrTalk(
        0x101,
        "#00002F#6PCecil! And Fran!\x02",
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
        "#2725V#30WEhehe... Long time no see, Lloyd!\x02",
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
            "#30WI'm really glad you're safe...\x02\x03",
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
            "#00006F#6PSorry... For worrying\x01",
            "you all.\x02\x03",
            "#00002FBut Fran. It looks like\x01",
            "you've made a complete\x01",
            "recovery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#06409F#11PYes, my injuries were\x01",
            "healed a long time ago!\x02\x03",
            "#06406FWith Crossbell how it is,\x01",
            "though, I can't very well\x01",
            "return to my duties, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PI see... Still, I'm\x01",
            "really glad.\x02",
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
            "#00215F#11P#30WBy the way, what's with\x01",
            "Wazy's clothes?\x02\x03",
            "#00216FAnd Zeit, where have you\x01",
            "been...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10404F#6PHaha. A lot happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#6P#3CAt any rate, allow me to\x01",
            "explain the sequence of\x01",
            "events thus far.\x02",
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
        "#01305F#11PWhat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#06411F#11PThat just now was...\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#00205F#11P? What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PWell, "what's wrong" you\x01",
            "say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#6PHaha. Could it be that because\x01",
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
            "like a human!?\x02",
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

    # Function_53_806C end

    def Function_54_98CC(): pass

    label("Function_54_98CC")

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

    # Function_54_98CC end

    def Function_55_98FB(): pass

    label("Function_55_98FB")

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

    # Function_55_98FB end

    def Function_56_992F(): pass

    label("Function_56_992F")

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

    # Function_56_992F end

    def Function_57_99BF(): pass

    label("Function_57_99BF")

    Sleep(300)

    label("loc_99C2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9A0C")
    PlayEffect(0x0, 0xFF, 0x105, 0x3, 0, 1050, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_99C2")

    label("loc_9A0C")

    Return()

    # Function_57_99BF end

    def Function_58_9A0D(): pass

    label("Function_58_9A0D")

    EndChrThread(0xFE, 0x2)
    Sleep(300)
    StopEffect(0x2, 0x2)
    StopSound(852, 500, 90)
    Sleep(300)
    Return()

    # Function_58_9A0D end

    def Function_59_9A21(): pass

    label("Function_59_9A21")


    def lambda_9A26():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_9A26)
    Sleep(200)

    def lambda_9A42():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_9A42)
    Sleep(200)

    def lambda_9A5E():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_9A5E)
    Sleep(200)

    def lambda_9A7A():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_9A7A)
    Sleep(200)
    Return()

    # Function_59_9A21 end

    def Function_60_9A92(): pass

    label("Function_60_9A92")

    Sleep(250)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    Return()

    # Function_60_9A92 end

    def Function_61_9AA1(): pass

    label("Function_61_9AA1")

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

    # Function_61_9AA1 end

    def Function_62_9B2A(): pass

    label("Function_62_9B2A")

    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_62_9B2A end

    def Function_63_9B2F(): pass

    label("Function_63_9B2F")

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

    # Function_63_9B2F end

    def Function_64_9BD5(): pass

    label("Function_64_9BD5")

    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_64_9BD5 end

    def Function_65_9BDA(): pass

    label("Function_65_9BDA")

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

    # Function_65_9BDA end

    def Function_66_9C5C(): pass

    label("Function_66_9C5C")

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

    def lambda_9CDA():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x384, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9CDA)
    Sleep(300)
    Sound(463, 0, 100, 0)
    OP_71(0xD, 0x1F, 0x3C, 0x1, 0x8)
    OP_79(0xD)
    Return()

    # Function_66_9C5C end

    def Function_67_9D03(): pass

    label("Function_67_9D03")

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

    # Function_67_9D03 end

    def Function_68_9D9A(): pass

    label("Function_68_9D9A")


    def lambda_9D9F():

        label("loc_9D9F")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_9D9F")

    QueueWorkItem2(0xFE, 2, lambda_9D9F)
    Sleep(400)
    OP_9B(0x1, 0xFE, 0x5A, 0x6D6, 0x7D0, 0x0)
    Return()

    # Function_68_9D9A end

    def Function_69_9DBF(): pass

    label("Function_69_9DBF")


    def lambda_9DC4():

        label("loc_9DC4")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_9DC4")

    QueueWorkItem2(0xFE, 2, lambda_9DC4)
    Sleep(100)
    OP_9B(0x1, 0xFE, 0x5A, 0x4E2, 0x3E8, 0x0)
    Return()

    # Function_69_9DBF end

    def Function_70_9DE4(): pass

    label("Function_70_9DE4")

    Sleep(600)
    OP_9B(0x0, 0xFE, 0x5A, 0x1F4, 0x7D0, 0x1)
    OP_9D(0xFE, 0xFFFF259A, 0x0, 0xFFFFF7CC, 0x15E, 0x5DC)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)

    def lambda_9E21():

        label("loc_9E21")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_9E21")

    QueueWorkItem2(0xFE, 2, lambda_9E21)
    Return()

    # Function_70_9DE4 end

    def Function_71_9E2F(): pass

    label("Function_71_9E2F")

    OP_9B(0x0, 0xFE, 0x0, 0x2198, 0x1770, 0x0)
    BeginChrThread(0xFE, 3, 0, 75)
    Sound(811, 0, 50, 0)
    Sound(898, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 76)

    def lambda_9E5B():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9E5B)
    Sleep(100)

    def lambda_9E77():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9E77)
    Return()

    # Function_71_9E2F end

    def Function_72_9E8C(): pass

    label("Function_72_9E8C")

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

    # Function_72_9E8C end

    def Function_73_9EC6(): pass

    label("Function_73_9EC6")

    OP_9B(0x0, 0xFE, 0x163, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_73_9EC6 end

    def Function_74_9ED6(): pass

    label("Function_74_9ED6")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x163, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_74_9ED6 end

    def Function_75_9EE9(): pass

    label("Function_75_9EE9")

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

    # Function_75_9EE9 end

    def Function_76_9F0D(): pass

    label("Function_76_9F0D")

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

    # Function_76_9F0D end

    def Function_77_9F31(): pass

    label("Function_77_9F31")

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

    # Function_77_9F31 end

    def Function_78_9F55(): pass

    label("Function_78_9F55")

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

    # Function_78_9F55 end

    def Function_79_9F79(): pass

    label("Function_79_9F79")

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
            "After that, Lloyd and\x01",
            "the others met up with\x01",
            "Zeit...\x02\x03",
            "...bid Cecil farewell,\x01",
            "and left St. Ursula\x01",
            "Hospital.\x02",
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
            "─On the way back, Wazy found a\x01",
            ""gap" in the septium vein force\x01",
            "field in front of the hospital...\x02\x03",
            "By fixing it with a "magic circle",\x01",
            "it became possible to have the\x01",
            "Merkabah come pick them up.\x07\x00\x02",
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
            "Because Tio and Fran have joined, it is\x01",
            "now possible to accept wanted monster\x01",
            "requests from the Merkabah terminal.\x02\x03",
            "The cabin terminal is usable, so please\x01",
            "make use of it.\x07\x00\x02",
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

    # Function_79_9F79 end

    def Function_80_A536(): pass

    label("Function_80_A536")

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

    # Function_80_A536 end

    def Function_81_A591(): pass

    label("Function_81_A591")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_81_A591 end

    def Function_82_A5AB(): pass

    label("Function_82_A5AB")

    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(900)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_82_A5AB end

    def Function_83_A5C8(): pass

    label("Function_83_A5C8")

    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(800)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_83_A5C8 end

    def Function_84_A5E5(): pass

    label("Function_84_A5E5")

    Sleep(500)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_84_A5E5 end

    def Function_85_A5FF(): pass

    label("Function_85_A5FF")

    Sleep(400)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_85_A5FF end

    def Function_86_A61C(): pass

    label("Function_86_A61C")

    OP_96(0xFE, 0xFFFF4480, 0x251C, 0x4268, 0xBB8, 0x1)
    OP_96(0xFE, 0xFFFF4480, 0x2328, 0x4268, 0x7D0, 0x1)
    OP_96(0xFE, 0xFFFF4480, 0x2134, 0x4268, 0x3E8, 0x1)
    Return()

    # Function_86_A61C end

    def Function_87_A659(): pass

    label("Function_87_A659")

    Return()

    # Function_87_A659 end

    def Function_88_A65A(): pass

    label("Function_88_A65A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A674")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_88_A65A")

    label("loc_A674")

    Return()

    # Function_88_A65A end

    def Function_89_A675(): pass

    label("Function_89_A675")

    SetMapObjFrame(0xF, "Null_fream", 0x2, "start")
    Sleep(20000)
    SetMapObjFrame(0xF, "Null_fream", 0x2, "loop")
    Return()

    # Function_89_A675 end

    def Function_90_A6A0(): pass

    label("Function_90_A6A0")

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

    def lambda_A79C():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A79C)
    Sleep(50)

    def lambda_A7B9():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A7B9)
    Sleep(50)

    def lambda_A7D6():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A7D6)
    Sleep(50)

    def lambda_A7F3():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A7F3)
    Sleep(50)

    def lambda_A810():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A810)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    Sleep(500)

    NpcTalk(
        0x16,
        "Woman's Voice",
        "Lloyd!?\x02",
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
        "#00002FAh!\x02",
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

    def lambda_A936():
        OP_95(0xFE, -21270, 0, -10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_A936)
    Sleep(50)

    def lambda_A953():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A953)
    Sleep(50)

    def lambda_A970():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A970)
    Sleep(50)

    def lambda_A98D():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A98D)
    Sleep(50)

    def lambda_A9AA():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A9AA)
    Sleep(50)

    def lambda_A9C7():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A9C7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x16, 1)

    ChrTalk(
        0x101,
        (
            "#6P#00009FCecil... Haha, good to\x01",
            "see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#11P#01300FHaha... Welcome back,\x01",
            "Lloyd.\x02\x03",
            "#01309FElie, Randy and even\x01",
            "Noｱl. How have you all\x01",
            "been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FHaha, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00309FLong time no see, Cecil!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10109FHaha, it has been too long.\x02\x03",
            "#10100FI think the last time we met was\x01",
            "during the cult incident when\x01",
            "the hospital was assaulted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#11P#01309FHaha... That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FWow, so she's your\x01",
            "legendary big sister,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#11P#01305FMy, I don't think I've\x01",
            "met you before, but...\x02\x03",
            "#01300FCould you and Noｱl be\x01",
            "the new members I've\x01",
            "heard so much about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FI guess you could say\x01",
            "that.\x02\x03",
            "#10302FWazy Hemisphere. Pleased\x01",
            "to make your\x01",
            "acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#11P#01309FHaha, nice to meet you.\x02\x03",
            "#01300FThen... Allow me to\x01",
            "introduce myself as\x01",
            "well.\x02",
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
            "Ahem... I am Cecil Neues, a nurse\x01",
            "working at St. Ursula Hospital.\x02\x03",
            "Haha. Please take good care of my\x01",
            "adorable little brother Lloyd.\x02",
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
            "#6P#00006FC'mon Cecil... You know\x01",
            "we're not actually brother\x01",
            "and sister, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00000FAhem, ahh... Cecil has\x01",
            "been looking after ever\x01",
            "since I was little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#11P#01306FOh, Lloyd, you're always\x01",
            "so shy.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#00012FI-I am not!\x02",
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
            "#11P#01304FHmm, but even so... Both\x01",
            "Wazy and Noｱl are real\x01",
            "beauties.\x02\x03",
            "#01300FLloyd, have you finally\x01",
            "decided who you're going\x01",
            "to date?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10105FD-Date!?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FI told you before, Cecil...\x01",
            "The Support Section isn't\x01",
            "that kind of place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#11P#01305FOh... right. I'll need\x01",
            "to be more careful.\x02\x03",
            "#01303FIt's a bit unfair having\x01",
            "this conversation now,\x01",
            "when Tio isn't here.\x02\x03",
            "#01300FOnce Tio is back,\x01",
            "carefully choose your\x01",
            "partner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FI-I told you already...\x01",
            "Why does it have to be\x01",
            "like that!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109FHaha. Somehow, I feel at\x01",
            "ease when I see Cecil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FYeah. She's still going\x01",
            "strong with pretending\x01",
            "to be an airhead, I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00006FNot you guys too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#11P#01304FHaha... Even so, I missed\x01",
            "you because you were away\x01",
            "for so long.\x02\x03",
            "#01300FIt's right around my\x01",
            "break time too. Would you\x01",
            "like to have tea with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FWell, since we're\x01",
            "here...\x02\x03",
            "#00002FEveryone, should we\x01",
            "accept her offer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10109FYes! We gladly accept!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("t1510", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_90_A6A0 end

    def Function_91_B372(): pass

    label("Function_91_B372")

    Return()

    # Function_91_B372 end

    def Function_92_B373(): pass

    label("Function_92_B373")

    EventBegin(0x0)
    Fade(500)
    OP_68(-47260, 1700, -1110, 0)
    MoveCamera(44, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x106, -48500, 0, -230, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_B585")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x102, -46300, 0, -1330, 90)
    SetChrPos(0x103, -46300, 0, 870, 90)
    SetChrPos(0x104, -48400, 0, 1030, 90)

    def lambda_B40B():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B40B)

    def lambda_B425():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B425)

    def lambda_B43F():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B43F)

    def lambda_B459():
        OP_95(0xFE, -46400, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B459)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B4A9")
    SetChrPos(0x109, -48000, 0, -1070, 90)

    def lambda_B494():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B494)

    label("loc_B4A9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B4E4")
    SetChrPos(0x105, -48000, 0, -1070, 90)

    def lambda_B4CF():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B4CF)

    label("loc_B4E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B51F")
    SetChrPos(0x10A, -48000, 0, -1070, 90)

    def lambda_B50A():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_B50A)

    label("loc_B51F")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B558")
    WaitChrThread(0x109, 1)

    label("loc_B558")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B56C")
    WaitChrThread(0x105, 1)

    label("loc_B56C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B580")
    WaitChrThread(0x10A, 1)

    label("loc_B580")

    Jump("loc_B871")

    label("loc_B585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_B693")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x103, -46300, 0, -1330, 90)
    SetChrPos(0x104, -46300, 0, 870, 90)
    SetChrPos(0x105, -48400, 0, 1030, 90)
    SetChrPos(0x109, -48000, 0, -1070, 90)

    def lambda_B5E8():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5E8)

    def lambda_B602():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B602)

    def lambda_B61C():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B61C)

    def lambda_B636():
        OP_95(0xFE, -46400, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B636)

    def lambda_B650():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B650)
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
    Jump("loc_B871")

    label("loc_B693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_B7A1")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x103, -46300, 0, -1330, 90)
    SetChrPos(0x104, -46300, 0, 870, 90)
    SetChrPos(0x107, -48800, 0, 1030, 90)
    SetChrPos(0x105, -48300, 0, -1070, 90)

    def lambda_B6F6():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B6F6)

    def lambda_B710():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B710)

    def lambda_B72A():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B72A)

    def lambda_B744():
        OP_95(0xFE, -46800, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_B744)

    def lambda_B75E():
        OP_95(0xFE, -46300, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B75E)
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
    Jump("loc_B871")

    label("loc_B7A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_B871")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x103, -46300, 0, -1330, 90)
    SetChrPos(0x105, -46300, 0, 870, 90)
    SetChrPos(0x107, -48800, 0, 1030, 90)

    def lambda_B7F3():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B7F3)

    def lambda_B80D():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B80D)

    def lambda_B827():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B827)

    def lambda_B841():
        OP_95(0xFE, -46800, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_B841)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x107, 1)

    label("loc_B871")


    ChrTalk(
        0x106,
        (
            "#6P#10708FI'm sorry, I would like\x01",
            "to wait outside the\x01",
            "hospital.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_BA20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B933")

    def lambda_B8D4():
        TurnDirection(0x109, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B8D4)
    Sleep(50)

    def lambda_B8E4():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B8E4)
    Sleep(50)

    def lambda_B8F4():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B8F4)
    Sleep(50)

    def lambda_B904():
        TurnDirection(0x102, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B904)
    Sleep(50)

    def lambda_B914():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B914)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    label("loc_B933")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B9A7")

    def lambda_B948():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B948)
    Sleep(50)

    def lambda_B958():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B958)
    Sleep(50)

    def lambda_B968():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B968)
    Sleep(50)

    def lambda_B978():
        TurnDirection(0x102, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B978)
    Sleep(50)

    def lambda_B988():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B988)
    Sleep(50)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    label("loc_B9A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BA1B")

    def lambda_B9BC():
        TurnDirection(0x10A, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_B9BC)
    Sleep(50)

    def lambda_B9CC():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B9CC)
    Sleep(50)

    def lambda_B9DC():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B9DC)
    Sleep(50)

    def lambda_B9EC():
        TurnDirection(0x102, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B9EC)
    Sleep(50)

    def lambda_B9FC():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B9FC)
    Sleep(50)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    label("loc_BA1B")

    Jump("loc_BB5D")

    label("loc_BA20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_BA92")

    def lambda_BA2E():
        TurnDirection(0x109, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BA2E)
    Sleep(50)

    def lambda_BA3E():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BA3E)
    Sleep(50)

    def lambda_BA4E():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BA4E)
    Sleep(50)

    def lambda_BA5E():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BA5E)
    Sleep(50)

    def lambda_BA6E():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BA6E)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    Jump("loc_BB5D")

    label("loc_BA92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_BB04")

    def lambda_BAA0():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_BAA0)
    Sleep(50)

    def lambda_BAB0():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BAB0)
    Sleep(50)

    def lambda_BAC0():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BAC0)
    Sleep(50)

    def lambda_BAD0():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BAD0)
    Sleep(50)

    def lambda_BAE0():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BAE0)
    Sleep(50)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    Jump("loc_BB5D")

    label("loc_BB04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_BB5D")

    def lambda_BB12():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_BB12)
    Sleep(50)

    def lambda_BB22():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BB22)
    Sleep(50)

    def lambda_BB32():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BB32)
    Sleep(50)

    def lambda_BB42():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BB42)
    Sleep(50)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)

    label("loc_BB5D")


    ChrTalk(
        0x101,
        (
            "#11P#00003FYeah, understood. See\x01",
            "you later.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBCA")
    RemoveParty(0x6, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)

    label("loc_BBCA")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -44100, 0, -230, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_BBFC")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_BBFC")

    EventEnd(0x5)
    Return()

    # Function_92_B373 end

    def Function_93_BBFF(): pass

    label("Function_93_BBFF")

    EventBegin(0x0)
    Fade(500)
    OP_68(-49470, 1000, -560, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18720, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_BCF3")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x102, -46820, 0, -830, 270)
    SetChrPos(0x103, -46820, 0, 370, 270)
    SetChrPos(0x104, -45620, 0, -1030, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BCA2")
    SetChrPos(0x109, -45620, 0, 570, 270)

    label("loc_BCA2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BCC3")
    SetChrPos(0x105, -45620, 0, 570, 270)

    label("loc_BCC3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BCE4")
    SetChrPos(0x10A, -45620, 0, 570, 270)

    label("loc_BCE4")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_BE1A")

    label("loc_BCF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_BD60")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x103, -46820, 0, -830, 270)
    SetChrPos(0x104, -46820, 0, 370, 270)
    SetChrPos(0x109, -45620, 0, -1030, 270)
    SetChrPos(0x105, -45620, 0, 570, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_BE1A")

    label("loc_BD60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_BDCD")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x103, -46820, 0, -830, 270)
    SetChrPos(0x104, -46820, 0, 370, 270)
    SetChrPos(0x105, -45620, 0, 570, 270)
    SetChrPos(0x107, -45320, 0, -1230, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_BE1A")

    label("loc_BDCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_BE1A")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x103, -46820, 0, -830, 270)
    SetChrPos(0x105, -46820, 0, 370, 270)
    SetChrPos(0x107, -45320, 0, -1230, 270)

    label("loc_BE1A")

    OP_4B(0xD, 0xFF)
    OP_0D()

    ChrTalk(
        0xD,
        (
            "#6P#10702FWelcome back, everyone.\x01",
            "...Have you finished\x01",
            "what you had to do?\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_BEEA")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_BEEA")

    EventEnd(0x5)
    Return()

    # Function_93_BBFF end

    def Function_94_BEED(): pass

    label("Function_94_BEED")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BF98")
    SetChrPos(0x109, -51500, 0, -1420, 90)

    label("loc_BF98")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BFB9")
    SetChrPos(0x105, -51500, 0, -1420, 90)

    label("loc_BFB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BFDA")
    SetChrPos(0x10A, -51500, 0, -1420, 90)

    label("loc_BFDA")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_BFF3():
        OP_95(0xFE, -44520, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BFF3)
    Sleep(30)

    def lambda_C010():
        OP_95(0xFE, -44520, 0, 1110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C010)
    Sleep(30)

    def lambda_C02D():
        OP_95(0xFE, -44520, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C02D)
    Sleep(30)

    def lambda_C04A():
        OP_95(0xFE, -45820, 0, 1110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C04A)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C08C")

    def lambda_C077():
        OP_95(0xFE, -45820, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C077)

    label("loc_C08C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C0B6")

    def lambda_C0A1():
        OP_95(0xFE, -45820, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C0A1)

    label("loc_C0B6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C0E0")

    def lambda_C0CB():
        OP_95(0xFE, -45820, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_C0CB)

    label("loc_C0E0")

    Sleep(30)

    def lambda_C0E8():
        OP_95(0xFE, -48500, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_C0E8)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)

    ChrTalk(
        0x106,
        (
            "#6P#10703FThen, everyone. I'll\x01",
            "excuse myself here...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_C14C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C14C)

    def lambda_C159():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C159)

    def lambda_C166():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C166)

    def lambda_C173():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C173)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C198")

    def lambda_C190():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C190)

    label("loc_C198")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C1B5")

    def lambda_C1AD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C1AD)

    label("loc_C1B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C1D2")

    def lambda_C1CA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_C1CA)

    label("loc_C1D2")

    WaitChrThread(0x104, 1)
    Sleep(500)

    ChrTalk(
        0x102,
        "#11P#00105FRixia...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00303F*sigh*...it can't be\x01",
            "helped.\x02",
        )
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
            "hear Ilya's voice?\x02",
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
            "#11P#00003FYou won't meet with Ilya until\x01",
            "you've settled everything...\x02\x03",
            "I understand your feelings and\x01",
            "I want to respect them, but...\x02\x03",
            "#00000FWouldn't it be fine if you\x01",
            "just listened to Ilya talking\x01",
            "with us from outside her room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#6P#10705FAh...\x02\x03",
            "#10708F...............\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)

    ChrTalk(
        0x104,
        (
            "#5P#00302FHe's right, it would be\x01",
            "fine if you gave\x01",
            "yourself a small reward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00203FIt is very likely that\x01",
            "from now on many other\x01",
            "difficulties await us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FI think that hearing the voice\x01",
            "of a person important to you\x01",
            "would give you strength.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C5A6")

    ChrTalk(
        0x109,
        (
            "#11P#10105FThat's right, Rixia!\x02\x03",
            "#10101FWe'll do our best to not\x01",
            "let her notice you're\x01",
            "there!\x02\x03",
            "#10104FI mean, when I met Fran\x01",
            "too, I cheered up so\x01",
            "much...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5A6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C682")

    ChrTalk(
        0x105,
        (
            "#11P#10404FHehe, why not?\x02\x03",
            "#10400FIf you don't actually see or\x01",
            "talk to her, you'd be keeping\x01",
            "your vow.\x02\x03",
            "#10408F...If you're really never be\x01",
            "able to see her again, won't\x01",
            "it be too late at that point?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C682")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C73D")

    ChrTalk(
        0x10A,
        (
            "#11P#00603FYin─ No, Rixia Mao.\x02\x03",
            "#00600FA detective like me\x01",
            "shouldn't say it, but\x01",
            "we're in a time of crisis.\x02\x03",
            "#00602FIt would be good if you\x01",
            "didn't have any regrets.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C73D")

    Sleep(1500)
    OP_64(0x106)

    ChrTalk(
        0x106,
        (
            "#6P#10704F...Everyone. Thank you very\x01",
            "much.\x02\x03",
            "#10702F...I'll accept your kind\x01",
            "offer... Please let me come with\x01",
            "you to the door of her room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00002FSure!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00100FYes, of course!\x02",
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

    # Function_94_BEED end

    def Function_95_C83E(): pass

    label("Function_95_C83E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_D047")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C85C")
    Call(0, 96)
    Jump("loc_D042")

    label("loc_C85C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE63")

    ChrTalk(
        0x10,
        (
            "#01300FLloyd... It seems you've\x01",
            "beaten Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah. As expected, it was\x01",
            "close, but... I was able to do\x01",
            "it thanks to everyone's help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FArios was a worthy rival to boost our\x01",
            "abilities and also served as a\x01",
            "Barrier we had to get over...\x02\x03",
            "#00100FHonestly speaking, I think if we were\x01",
            "short even one person, we would've\x01",
            "never been able to match him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00304F...You said it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#01309FHaha. All together, you're the\x01",
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
            "#01304FI didn't speak with Arios too many\x01",
            "times. However...\x02\x03",
            "I feel something has been weighing\x01",
            "heavily on his heart for a long\x01",
            "time.\x02\x03",
            "#01308FHe has to bear the facts of\x01",
            "Shizuku, his wife and Guy too... I\x01",
            "would never be able to bear it.\x02\x03",
            "#01300FAnd because that man is incredibly\x01",
            "strong, I think he might not even\x01",
            "be able to rely on others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThe loneliness that comes\x01",
            "from strength... It might\x01",
            "really be like you say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#01302FHaha. But I'm sure that, having been defeated\x01",
            "after fighting his heart out against you all,\x01",
            "he's been released from that as well.\x02\x03",
            "#01304FI think Guy was worried about him too, so let\x01",
            "me thank you in his stead, as his fiancｳe.\x02\x03",
            "#01309FThank you for saving Arios, Guy's close\x01",
            "friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FHaha... You're welcome.\x02\x03",
            "#00000FAll that's left is to\x01",
            "take back KeA. Wait for\x01",
            "us, sister Cecil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#01300FYes, all right.\x02\x03",
            "#01303FLloyd, everyone... Be\x01",
            "careful until the very\x01",
            "end.\x02\x03",
            "#01302FI'll be here, praying\x01",
            "that you come back\x01",
            "smiling with KeA.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 5)
    Jump("loc_D042")

    label("loc_CE63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CFC8")

    ChrTalk(
        0x10,
        (
            "#01303FLloyd, everyone... Be\x01",
            "careful until the very\x01",
            "end.\x02\x03",
            "#01302FI'll be here, praying\x01",
            "that you come back\x01",
            "smiling with KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAlright, just wait for us.\x02\x03",
            "#00003F(...In any case, I've confirmed the\x01",
            "truth of Guy's case, but... I don't\x01",
            "think I should tell her now.)\x02\x03",
            "#00008F(I must formally ask Lawyer Ian\x01",
            "about it as well...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_D042")

    label("loc_CFC8")


    ChrTalk(
        0x10,
        (
            "#01303FLloyd, everyone... Be\x01",
            "careful until the very\x01",
            "end.\x02\x03",
            "I'll be here, praying\x01",
            "that you come back\x01",
            "smiling with KeA.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D042")

    Jump("loc_D2BD")

    label("loc_D047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D298")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D062")
    Call(0, 96)
    Jump("loc_D293")

    label("loc_D062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D20F")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D15A")
    TurnDirection(0x10, 0x106, 0)

    ChrTalk(
        0x10,
        (
            "#01300FRixia, please be careful\x01",
            "too.\x02\x03",
            "#01304FIlya didn't directly say\x01",
            "it, but I think you are\x01",
            "always on her mind.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D121")

    ChrTalk(
        0x106,
        "#10708F...I see...\x02",
    )

    CloseMessageWindow()
    Jump("loc_D155")

    label("loc_D121")


    ChrTalk(
        0x106,
        (
            "#10702FRight! I promise I'll\x01",
            "come back safely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D155")

    Jump("loc_D207")

    label("loc_D15A")


    ChrTalk(
        0x10,
        (
            "#01300FDon't forget the promise\x01",
            "to all come back with KeA\x01",
            "either... All right?\x02\x03",
            "#01304FAs long as you can promise\x01",
            "me that, I will be able to\x01",
            "stay here waiting for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D207")

    SetScenarioFlags(0x0, 7)
    Jump("loc_D293")

    label("loc_D20F")


    ChrTalk(
        0x10,
        (
            "#01300FI will stay here, waiting\x01",
            "for you all.\x02\x03",
            "#01304FMay the blessing of the\x01",
            "Goddess be upon all of\x01",
            "you, Lloyd and friends...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D293")

    Jump("loc_D2BD")

    label("loc_D298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_D2A6")
    Jump("loc_D2BD")

    label("loc_D2A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_D2B4")
    Jump("loc_D2BD")

    label("loc_D2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_D2BD")

    label("loc_D2BD")

    TalkEnd(0xFE)
    Return()

    # Function_95_C83E end

    def Function_96_D2C1(): pass

    label("Function_96_D2C1")

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
        (
            "#5P#00000FCecil... So this is\x01",
            "where you were.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x10, 0x101, 300)

    ChrTalk(
        0x10,
        (
            "#12P#01300FYes. I was shocked after\x01",
            "that thing appeared...\x02\x03",
            "#01304F...Still, what a\x01",
            "mysterious tree.\x02\x03",
            "Although it is clearly\x01",
            "alien, it is somehow\x01",
            "lovely...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108F(Bell said that the Huge\x01",
            "Tree is "KeA\x01",
            "herself"...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D50A")

    ChrTalk(
        0x105,
        (
            "#11P#10403F(It might not be so\x01",
            "strange for her to feel\x01",
            "this way.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D5BF")

    label("loc_D50A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D565")

    ChrTalk(
        0x109,
        (
            "#11P#10103F(Being Cecil, maybe it's\x01",
            "not odd she feels that\x01",
            "way.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D5BF")

    label("loc_D565")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D5BF")

    ChrTalk(
        0x106,
        (
            "#11P#10703F(Being Cecil, maybe it's\x01",
            "not strange she feels\x01",
            "that way.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D5BF")

    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)

    ChrTalk(
        0x10,
        (
            "#12P#01303FLloyd, everyone...\x02\x03",
            "#01301F...You are heading\x01",
            "there, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003F...Yeah.\x02\x03",
            "#00001FIn that Huge Tree, the\x01",
            "whole truth and KeA are\x01",
            "waiting for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00101FNo matter what dangers\x01",
            "await us, we have to go.\x02",
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
            "#12P#01303FIn truth, I don't want you\x01",
            "to face those dangers...\x02\x03",
            "#01308FI lost someone important to\x01",
            "me once. ...I don't ever\x01",
            "want to feel that way again.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D7BE")

    ChrTalk(
        0x106,
        "#11P#10705FCecil...\x02",
    )

    CloseMessageWindow()
    Jump("loc_D81D")

    label("loc_D7BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D7F0")

    ChrTalk(
        0x10A,
        "#11P#00608F............\x02",
    )

    CloseMessageWindow()
    Jump("loc_D81D")

    label("loc_D7F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D81D")

    ChrTalk(
        0x105,
        "#11P#10408F............\x02",
    )

    CloseMessageWindow()

    label("loc_D81D")


    ChrTalk(
        0x10,
        (
            "#12P#01303F...However, if Guy was alive...\x01",
            "I think he would try to do the\x01",
            "same thing you all are doing.\x02\x03",
            "#01302FI think he would have dashed to\x01",
            "protect the things important to\x01",
            "him no matter the dangers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00000FCecil...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#01304F...That is why, everyone,\x01",
            "please promise me just one\x01",
            "thing.\x02\x03",
            "#01300FThat you will all come\x01",
            "back safely, together with\x01",
            "KeA.\x02\x03",
            "#01309FAs long as you can promise\x01",
            "me that, I will be able to\x01",
            "stay here waiting for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00005FCecil...\x02\x03",
            "#00004F...All right. Wait for\x01",
            "us just a little longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00200FIt will be a very\x01",
            "difficult trial, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00102FYes, we'll absolutely\x01",
            "return after taking back\x01",
            "KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00309FWe've also gotta beat\x01",
            "some sense into ol' man\x01",
            "Arios.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB30")

    ChrTalk(
        0x10A,
        "#11P#00602FYeah, of course.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DB97")

    label("loc_DB30")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB63")

    ChrTalk(
        0x109,
        "#11P#10102FYes, I agree.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DB97")

    label("loc_DB63")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB97")

    ChrTalk(
        0x105,
        "#11P#10402FHehe, that's right.\x02",
    )

    CloseMessageWindow()

    label("loc_DB97")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6D), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DE73")

    ChrTalk(
        0x10,
        (
            "#12P#01304F...Haha. Thank you,\x01",
            "everyone. With this I\x01",
            "can finally relax.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)

    ChrTalk(
        0x10,
        (
            "#12P#01309FThen, as a symbol of our\x01",
            "promise, I think I will\x01",
            "give you this.\x02",
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
        "#5P#00005FThis is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#01300FIt's something Guy gave me when I\x01",
            "undertook the nursing exam.\x02\x03",
            "#01304FIf you grasp it tightly in tough times,\x01",
            "you mysteriously feel courage gushing\x01",
            "out... It's that kind of amulet.\x02\x03",
            "#01300FIt is very precious to me, so come back\x01",
            "safely and return it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00000F...Yeah, got it. We'll\x01",
            "borrow it with\x01",
            "gratitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#01309FHaha. May the blessing of\x01",
            "the Goddess be upon you\x01",
            "all, Lloyd and friends...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF11")

    label("loc_DE73")


    ChrTalk(
        0x10,
        (
            "#12P#01304F...Haha. Thank you,\x01",
            "everyone. With this I can\x01",
            "finally relax.\x02\x03",
            "#01309FMay the blessing of the\x01",
            "Goddess be upon all of\x01",
            "you, Lloyd and friends...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF11")

    OP_5A()
    SetScenarioFlags(0x1AC, 4)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -24090, -1000, -22920, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DF5A")
    OP_E0(0x34, 0x0)

    label("loc_DF5A")

    EventEnd(0x5)
    Return()

    # Function_96_D2C1 end

    def Function_97_DF5D(): pass

    label("Function_97_DF5D")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DFEB")

    ChrTalk(
        0x101,
        (
            "#00000FWe can't leave the\x01",
            "hospital until Fran's\x01",
            "ready.\x02\x03",
            "Let's pay a visit to\x01",
            "Ilya and Inspector\x01",
            "Donovan in the meantime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DFEB")

    Sleep(50)
    SetChrPos(0x0, -61000, 0, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_97_DF5D end

    def Function_98_E002(): pass

    label("Function_98_E002")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "St.Ursula Medical School\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_98_E002 end

    def Function_99_E056(): pass

    label("Function_99_E056")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Medical College ～Auberge\x01",
            ""Le Rekuche"～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_99_E056 end

    SaveToFile()

Try(main)
