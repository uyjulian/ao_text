from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0000.bin",                # FileName
        "t0000",                    # MapName
        "t0000",                    # Location
        0x0037,                     # MapIndex
        "ed7120",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x19,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 55, 0, 1, 0, 2],
    )

    BuildStringList((
        "t0000",                  # 0
        "Camille",                # 1
        "Elkin",                  # 2
        "Pooley",                 # 3
        "Stefan",                 # 4
        "Derrick",                # 5
        "Minneth",                # 6
        "Aretha",                 # 7
        "Sophia",                 # 8
        "Colin",                  # 9
        "Bracer Scott",           # 10
        "バス",                   # 11
        "Special Support Vehicle",# 12
        "メルカバ玖号機",         # 13
        "メルカバ光学迷彩",       # 14
        "メルカバ影",             # 15
        "Keith",                  # 16
        "Bracer Ling",            # 17
        "Bracer Eolia",           # 18
        "Ange",                   # 19
        "Gｷfan",                 # 20
        "Sealy",                  # 21
        "Village Chief Tolta",    # 22
        "Pete",                   # 23
        "Harold",                 # 24
        "猫型魔獣",               # 25
        "猫型魔獣",               # 26
        "猫型魔獣",               # 27
        "猫型魔獣",               # 28
        "猫型魔獣",               # 29
        "Black Transport",        # 30
        "Alm",                    # 31
        "Aerie",                  # 32
        "SE制御",                 # 33
        "bt0000",                 # 34
        "bt0000",                 # 35
        "Armorica Old Road",      # 36
    ))

    ATBonus("ATBonus_6B4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_6D4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6DC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6EC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6F0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_754", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_758", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_75C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_760", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_764", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_768", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_76C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_770", 5, 5, 45)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_774", 0x0062, 255, 6, 45, 3, 3, 30, 0, "bt0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms32000.dat", "ms32100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6D4", "MonsterBattlePostion_754", "ed7451", "ed7453", "ATBonus_6B4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7B8", 0x0062, 255, 6, 45, 3, 3, 30, 0, "bt0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms32001.dat", "ms32101.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6D4", "MonsterBattlePostion_754", "ed7452", "ed7453", "ATBonus_6B4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch24600.itc",                   # 00
        "chr/ch24400.itc",                   # 01
        "chr/ch24700.itc",                   # 02
        "chr/ch20600.itc",                   # 03
        "chr/ch32300.itc",                   # 04
        "chr/ch45200.itc",                   # 05
        "chr/ch22700.itc",                   # 06
        "chr/ch09400.itc",                   # 07
        "chr/ch07200.itc",                   # 08
        "chr/ch27200.itc",                   # 09
        "chr/ch46300.itc",                   # 0A
        "chr/ch46200.itc",                   # 0B
    ))

    DeclNpc(4294960427, 0,       24790,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(8409,    0,       4294954817, 17,   261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294961186, 0,       23270,   315,  261,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294959467, 0,       23860,   107,  261,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(12779,   3500,    40220,   298,  389,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294966796, 500,     6000,    90,   389,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(11369,   0,       19389,   280,  389,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(10010,   0,       19659,   280,  389,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4294958597, 0,       25250,   90,   389,  0x0, 0,   8,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(3170,    0,       14229,   135,  389,  0x0, 0,   10,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(2119,    0,       13670,   135,  389,  0x0, 0,   11,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0040, 0, 33,  8.40999984741211,      -12.479999542236328,   -1.0,                  6.25,                  [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   -1.6820000410079956,   2.496000051498413,     0.3333333432674408,    1.0])
    DeclEvent(0x0000, 0, 34,  -2.130000114440918,    12.520000457763672,    -1.100000023841858,    270.27362060546875,    [0.24330902099609375,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.1250000149011612,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333730697632,    0.0,                   0.5182482600212097,    -1.565000295639038,    0.366666704416275,     1.0])
    DeclEvent(0x0000, 0, 64,  0.5400000214576721,    -8.800000190734863,    -0.0,                  144.0,                 [0.16666655242443085,  0.10825320333242416,   -0.0,                  0.0,                   -0.2886752188205719,   0.06249995902180672,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   -2.6303420066833496,   0.49154290556907654,   -0.0,                  1.0])

    DeclActor(4294965296, 0,       4294952296, 1500,    4294965296, 1500,    4294952296, 0x007C, 0,  23, 0x0000)
    DeclActor(11740,   0,       3950,    1200,    10890,   4294965846, 1210,    0x007C, 0,  24, 0x0000)
    DeclActor(15990,   0,       4294947856, 1200,    15990,   2000,    4294947856, 0x007C, 0,  22, 0x0000)
    DeclActor(4294949996, 3500,    63700,   1500,    4294926296, 1000,    91000,   0x007C, 0,  22, 0x0000)
    DeclActor(15550,   3520,    47700,   1200,    15550,   4520,    47700,   0x007C, 0,  65, 0x0000)

    PlaceName(28.0, 0.0, -40.0, 0x0000, 0x0000, "Armorica Old Road")
    PlaceName(-25.0, 0.0, 20.0, 0x0000, 0x0053, "")
    PlaceName(20.399999618530273, 0.0, 25.25, 0x0000, 0x0052, "")
    PlaceName(-2.0, 0.0, -14.699999809265137, 0x0000, 0x0055, "")

    ChipFrameInfo(2404, 0)                                       # 0

    ScpFunction((
        "Function_0_964",          # 00, 0
        "Function_1_A1C",          # 01, 1
        "Function_2_12CF",         # 02, 2
        "Function_3_175B",         # 03, 3
        "Function_4_185D",         # 04, 4
        "Function_5_1970",         # 05, 5
        "Function_6_19A6",         # 06, 6
        "Function_7_19F7",         # 07, 7
        "Function_8_1A8B",         # 08, 8
        "Function_9_33D6",         # 09, 9
        "Function_10_3F25",        # 0A, 10
        "Function_11_41C5",        # 0B, 11
        "Function_12_477E",        # 0C, 12
        "Function_13_4FB4",        # 0D, 13
        "Function_14_588B",        # 0E, 14
        "Function_15_59A7",        # 0F, 15
        "Function_16_5A69",        # 10, 16
        "Function_17_5C23",        # 11, 17
        "Function_18_5CE4",        # 12, 18
        "Function_19_5D88",        # 13, 19
        "Function_20_6182",        # 14, 20
        "Function_21_62FE",        # 15, 21
        "Function_22_63F0",        # 16, 22
        "Function_23_672D",        # 17, 23
        "Function_24_6781",        # 18, 24
        "Function_25_6848",        # 19, 25
        "Function_26_6A8A",        # 1A, 26
        "Function_27_7D28",        # 1B, 27
        "Function_28_9247",        # 1C, 28
        "Function_29_9413",        # 1D, 29
        "Function_30_C0A3",        # 1E, 30
        "Function_31_C1B7",        # 1F, 31
        "Function_32_C1D4",        # 20, 32
        "Function_33_C693",        # 21, 33
        "Function_34_D038",        # 22, 34
        "Function_35_13395",       # 23, 35
        "Function_36_133C9",       # 24, 36
        "Function_37_133FD",       # 25, 37
        "Function_38_13431",       # 26, 38
        "Function_39_13465",       # 27, 39
        "Function_40_13499",       # 28, 40
        "Function_41_134CD",       # 29, 41
        "Function_42_13501",       # 2A, 42
        "Function_43_13535",       # 2B, 43
        "Function_44_13569",       # 2C, 44
        "Function_45_1359D",       # 2D, 45
        "Function_46_135D1",       # 2E, 46
        "Function_47_13605",       # 2F, 47
        "Function_48_13639",       # 30, 48
        "Function_49_1366D",       # 31, 49
        "Function_50_136A1",       # 32, 50
        "Function_51_136C9",       # 33, 51
        "Function_52_136EC",       # 34, 52
        "Function_53_13761",       # 35, 53
        "Function_54_137EA",       # 36, 54
        "Function_55_1385F",       # 37, 55
        "Function_56_138E8",       # 38, 56
        "Function_57_1395D",       # 39, 57
        "Function_58_139A8",       # 3A, 58
        "Function_59_139F3",       # 3B, 59
        "Function_60_13A3E",       # 3C, 60
        "Function_61_13A89",       # 3D, 61
        "Function_62_13AD4",       # 3E, 62
        "Function_63_13B33",       # 3F, 63
        "Function_64_13B4D",       # 40, 64
        "Function_65_13E4A",       # 41, 65
        "Function_66_14329",       # 42, 66
        "Function_67_14971",       # 43, 67
        "Function_68_1499F",       # 44, 68
        "Function_69_149E1",       # 45, 69
        "Function_70_14A23",       # 46, 70
        "Function_71_14A65",       # 47, 71
        "Function_72_14AA7",       # 48, 72
        "Function_73_14AE9",       # 49, 73
        "Function_74_14B2B",       # 4A, 74
        "Function_75_151E2",       # 4B, 75
        "Function_76_15224",       # 4C, 76
        "Function_77_162E4",       # 4D, 77
        "Function_78_16883",       # 4E, 78
        "Function_79_168C8",       # 4F, 79
        "Function_80_16916",       # 50, 80
        "Function_81_1697B",       # 51, 81
        "Function_82_16C7A",       # 52, 82
        "Function_83_16CA5",       # 53, 83
        "Function_84_16CD0",       # 54, 84
        "Function_85_16CFB",       # 55, 85
        "Function_86_16D2A",       # 56, 86
        "Function_87_17B42",       # 57, 87
        "Function_88_17C23",       # 58, 88
        "Function_89_17C39",       # 59, 89
    ))


    def Function_0_964(): pass

    label("Function_0_964")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_9A4"),
        (1, "loc_9B0"),
        (2, "loc_9BC"),
        (3, "loc_9C8"),
        (4, "loc_9D4"),
        (5, "loc_9E0"),
        (6, "loc_9EC"),
        (SWITCH_DEFAULT, "loc_9F8"),
    )


    label("loc_9A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_9F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_A04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A1B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A04")

    label("loc_A1B")

    Return()

    # Function_0_964 end

    def Function_1_A1C(): pass

    label("Function_1_A1C")

    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A5B")
    SetChrPos(0x9, 11050, 0, -22040, 180)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -19420, 3500, 60540, 330)
    Jump("loc_C7C")

    label("loc_A5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_ADA")
    SetChrPos(0x8, -7700, 0, 24530, 0)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0xA, -7700, 0, 25980, 180)
    SetChrPos(0xB, -6700, 0, 25250, 270)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 5850, 0, 15680, 175)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD5")
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xF, 0x10)

    label("loc_AD5")

    Jump("loc_C7C")

    label("loc_ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_AFE")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -18860, 3500, 52530, 240)
    Jump("loc_C7C")

    label("loc_AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B66")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 7300, 0, -11420, 135)
    TurnDirection(0x9, 0xC, 0)
    SetChrPos(0x8, -7700, 0, 24530, 0)
    SetChrPos(0xA, -7700, 0, 25980, 180)
    SetChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B61")
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)

    label("loc_B61")

    Jump("loc_C7C")

    label("loc_B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B74")
    Jump("loc_C7C")

    label("loc_B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B96")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_C7C")

    label("loc_B96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BA4")
    Jump("loc_C7C")

    label("loc_BA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 7)), scpexpr(EXPR_END)), "loc_BBB")
    SetChrFlags(0x9, 0x10)

    label("loc_BBB")

    Jump("loc_C7C")

    label("loc_BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BE2")
    SetChrFlags(0x9, 0x80)

    label("loc_BE2")

    SetChrFlags(0xB, 0x10)
    Jump("loc_C7C")

    label("loc_BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C13")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    Jump("loc_C7C")

    label("loc_C13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_C30")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_C7C")

    label("loc_C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C52")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_C7C")

    label("loc_C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C65")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_C7C")

    label("loc_C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C73")
    Jump("loc_C7C")

    label("loc_C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C7C")

    label("loc_C7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1120")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D09")
    SetScenarioFlags(0x38, 0)

    label("loc_D09")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1F")
    SetScenarioFlags(0x38, 1)

    label("loc_D1F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D35")
    SetScenarioFlags(0x38, 2)

    label("loc_D35")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4B")
    SetScenarioFlags(0x38, 3)

    label("loc_D4B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D61")
    SetScenarioFlags(0x38, 4)

    label("loc_D61")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D77")
    SetScenarioFlags(0x38, 5)

    label("loc_D77")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8D")
    SetScenarioFlags(0x38, 6)

    label("loc_D8D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA3")
    SetScenarioFlags(0x38, 7)

    label("loc_DA3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB9")
    SetScenarioFlags(0x39, 0)

    label("loc_DB9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCF")
    SetScenarioFlags(0x39, 1)

    label("loc_DCF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE5")
    SetScenarioFlags(0x39, 2)

    label("loc_DE5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFB")
    SetScenarioFlags(0x39, 3)

    label("loc_DFB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E11")
    SetScenarioFlags(0x39, 4)

    label("loc_E11")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E27")
    SetScenarioFlags(0x39, 5)

    label("loc_E27")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3D")
    SetScenarioFlags(0x39, 6)

    label("loc_E3D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E53")
    SetScenarioFlags(0x39, 7)

    label("loc_E53")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E69")
    SetScenarioFlags(0x3A, 0)

    label("loc_E69")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E7F")
    SetScenarioFlags(0x3A, 1)

    label("loc_E7F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E95")
    SetScenarioFlags(0x3A, 2)

    label("loc_E95")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EAB")
    SetScenarioFlags(0x3A, 3)

    label("loc_EAB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC1")
    SetScenarioFlags(0x3A, 4)

    label("loc_EC1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED7")
    SetScenarioFlags(0x3A, 5)

    label("loc_ED7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EED")
    SetScenarioFlags(0x3A, 6)

    label("loc_EED")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F03")
    SetScenarioFlags(0x3A, 7)

    label("loc_F03")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F19")
    SetScenarioFlags(0x3B, 0)

    label("loc_F19")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2F")
    SetScenarioFlags(0x3B, 1)

    label("loc_F2F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F45")
    SetScenarioFlags(0x3B, 2)

    label("loc_F45")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5B")
    SetScenarioFlags(0x3B, 3)

    label("loc_F5B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F71")
    SetScenarioFlags(0x3B, 4)

    label("loc_F71")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F87")
    SetScenarioFlags(0x3B, 5)

    label("loc_F87")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9D")
    SetScenarioFlags(0x3B, 6)

    label("loc_F9D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB3")
    SetScenarioFlags(0x3B, 7)

    label("loc_FB3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC9")
    SetScenarioFlags(0x3D, 5)

    label("loc_FC9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDF")
    SetScenarioFlags(0x3D, 6)

    label("loc_FDF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF5")
    SetScenarioFlags(0x3D, 7)

    label("loc_FF5")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1030")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1120")

    label("loc_1030")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1053")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1120")

    label("loc_1053")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1076")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1120")

    label("loc_1076")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1099")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1120")

    label("loc_1099")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10BC")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1120")

    label("loc_10BC")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DF")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1120")

    label("loc_10DF")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1102")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1120")

    label("loc_1102")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1120")
    SetScenarioFlags(0x3C, 7)

    label("loc_1120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1136")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_114C")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_114C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_117E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117E")
    SetChrPos(0x0, 15150, 0, -19900, 225)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 7)

    label("loc_117E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_11B1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B1")
    SetChrPos(0x0, -17300, 3500, 63700, 150)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_11B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_11DB")
    ClearScenarioFlags(0x3E, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11D8")
    Event(0, 86)
    Jump("loc_11DB")

    label("loc_11D8")

    Event(0, 6)

    label("loc_11DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_11F2")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x1, 4)
    Event(0, 25)
    Jump("loc_1232")

    label("loc_11F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1209")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x1, 4)
    Event(0, 66)
    Jump("loc_1232")

    label("loc_1209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1220")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x1, 4)
    Event(0, 74)
    Jump("loc_1232")

    label("loc_1220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1232")
    ClearScenarioFlags(0x22, 3)
    SetScenarioFlags(0x1, 4)
    Event(0, 76)

    label("loc_1232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1248")
    Event(0, 77)
    Jump("loc_12CE")

    label("loc_1248")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1267")
    Event(0, 81)
    Jump("loc_12CE")

    label("loc_1267")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_129C")
    Event(0, 32)
    Jump("loc_12CE")

    label("loc_129C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12CE")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12CE")
    SetMapFlags(0x10000000)
    Event(0, 86)

    label("loc_12CE")

    Return()

    # Function_1_A1C end

    def Function_2_12CF(): pass

    label("Function_2_12CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_12E1")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_12F5")
    OP_24(0x7B)
    ClearScenarioFlags(0x1, 4)
    Jump("loc_132B")

    label("loc_12F5")

    SoundDistance(0x7B, 0xFFFF9372, 0x1F4, 0x230A, 0x1388, 0x4E20, 0x64, 0x0)
    OP_E3(0x1B26, 0x1F4, 0x143C)
    OP_E3(0x7936, 0x1F4, 0xFFFFFD6C)

    label("loc_132B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1346")
    ClearMapObjFlags(0x3, 0x10)
    OP_70(0x3, 0x0)

    label("loc_1346")

    SetMapObjFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1366")
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    Jump("loc_14FA")

    label("loc_1366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1393")
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    Jump("loc_14FA")

    label("loc_1393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_13C0")
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    Jump("loc_14FA")

    label("loc_13C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_13D4")
    SetMapObjFlags(0x6, 0x4)
    Jump("loc_14FA")

    label("loc_13D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1454")
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_144F")
    ClearMapObjFlags(0xD, 0x4)
    OP_78(0xD, 0x25)
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    OP_74(0xD, 0x1E)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 13000, 0, -11540, 20)
    OP_D5(0x25, 0x0, 0x4E20, 0x0, 0x0)

    label("loc_144F")

    Jump("loc_14FA")

    label("loc_1454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1492")
    SetMapObjFlags(0x6, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_147A")
    ClearMapObjFlags(0xA, 0x4)

    label("loc_147A")

    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    Jump("loc_14FA")

    label("loc_1492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_14A6")
    ClearMapObjFlags(0xD, 0x4)
    Jump("loc_14FA")

    label("loc_14A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_14B4")
    Jump("loc_14FA")

    label("loc_14B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_14C2")
    Jump("loc_14FA")

    label("loc_14C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_14E3")
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    Jump("loc_14FA")

    label("loc_14E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_14F1")
    Jump("loc_14FA")

    label("loc_14F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_14FA")

    label("loc_14FA")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_151B")
    OP_66(0x4, 0x1)

    label("loc_151B")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_154A")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_154A")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_157C")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_157C")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15AB")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_15AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_162F")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x0, 0xBE, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_162F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1686")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0xFF, "flower00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "flower04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "p_kusa", 0x1, 0x1)
    SetMapObjFrame(0xFF, "point0_add", 0x1, 0x1)
    Jump("loc_16C6")

    label("loc_1686")

    SetMapObjFrame(0xFF, "flower00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "flower04", 0x0, 0x1)
    SetMapObjFrame(0xFF, "p_kusa", 0x0, 0x1)
    SetMapObjFrame(0xFF, "point0_add", 0x0, 0x1)

    label("loc_16C6")

    MiniGame(0x2F, 0x2, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x11, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_16FD")
    ClearMapObjFlags(0x11, 0x4)

    label("loc_16FD")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 10890, -1450, 1210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_175A")
    OP_1B(0x0, 0x0, 0x59)

    label("loc_175A")

    Return()

    # Function_2_12CF end

    def Function_3_175B(): pass

    label("Function_3_175B")

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
            "Crossbell City East Entrance\x01",      # 0
            "Tangram Gate\x01",                      # 1
            "Bus Stop (Fork in the Road)\x01",       # 2
            "Cancel\x01",                            # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1810")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1855")

    label("loc_1810")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1835")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1855")

    label("loc_1835")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1855")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_1855")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_3_175B end

    def Function_4_185D(): pass

    label("Function_4_185D")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_196C")
    Fade(500)
    OP_68(4100, 1500, -16270, 0)
    MoveCamera(0, 33, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(17000, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -400, 0, -15300, 135)
    SetChrPos(0x1, -1230, 0, -15500, 135)
    SetChrPos(0x2, -2000, 0, -15700, 135)
    SetChrPos(0x3, -2750, 0, -15900, 135)
    ClearChrFlags(0x12, 0x80)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x7, 0x2)
    OP_78(0x7, 0x12)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x12, 13270, 0, -22560, 0)
    OP_D5(0x12, 0x0, 0x1F4, 0x0, 0x0)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)
    BeginChrThread(0x12, 1, 0, 5)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x12, 1)
    OP_79(0x7)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_196C")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_4_185D end

    def Function_5_1970(): pass

    label("Function_5_1970")

    OP_95(0x12, 10630, 0, -20520, 4000, 0x0)
    OP_9E(0x12, 0x1770, 0xFFFF987C, 0xFFFF0DD0, 0xFA0, 0x1)
    OP_71(0x7, 0x5B, 0x78, 0x0, 0x0)
    Return()

    # Function_5_1970 end

    def Function_6_19A6(): pass

    label("Function_6_19A6")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -700, 0, -13900, 135)
    OP_31(0x1)
    OP_68(-690, 1500, -13900, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    EventEnd(0x5)
    Return()

    # Function_6_19A6 end

    def Function_7_19F7(): pass

    label("Function_7_19F7")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1A52")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A47")
    Sound(2502, 255, 100, 0)
    Jump("loc_1A4D")

    label("loc_1A47")

    Sound(2503, 255, 100, 0)

    label("loc_1A4D")

    Jump("loc_1A76")

    label("loc_1A52")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A70")
    Sound(3347, 255, 100, 0)
    Jump("loc_1A76")

    label("loc_1A70")

    Sound(3348, 255, 100, 0)

    label("loc_1A76")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_19F7 end

    def Function_8_1A8B(): pass

    label("Function_8_1A8B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1C52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B9D")

    ChrTalk(
        0x9,
        (
            "H-How shocking... Just\x01",
            "what is that huge tree!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No matter how I think about it, I\x01",
            "can't accept something like that\x01",
            "appearing all of a sudden as normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You mean to tell me my\x01",
            "enjoyable, peaceful days of\x01",
            "driving aren't back yet!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C4D")

    label("loc_1B9D")


    ChrTalk(
        0x9,
        (
            "If something like that appeared\x01",
            "all of a sudden, what's going\x01",
            "to happen to Crossbell...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You mean to tell me my\x01",
            "enjoyable, peaceful days of\x01",
            "driving aren't back yet!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C4D")

    Jump("loc_33D2")

    label("loc_1C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1E30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D66")

    ChrTalk(
        0x9,
        (
            "There was that\x01",
            "independence invalidity\x01",
            "declaration, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Honestly, the former\x01",
            "Crossbell in which I could\x01",
            "enjoy my drives was better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I don't understand things like\x01",
            "independence. I just want things\x01",
            "to go back to how they used to be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E2B")

    label("loc_1D66")


    ChrTalk(
        0x9,
        (
            "More than independence, I just\x01",
            "want the Crossbell in which I\x01",
            "can enjoy my drives back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Though there was that invalidity\x01",
            "declaration, I just want things to\x01",
            "go back to how they used to be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E2B")

    Jump("loc_33D2")

    label("loc_1E30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_203C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F77")

    ChrTalk(
        0x9,
        (
            "With the highway movement\x01",
            "restrictions, hardly any\x01",
            "buses or cars come by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think the State Guard armored cars\x01",
            "that sometimes come here are cool but...\x01",
            "Honestly, I'm tired of looking at them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because Cryptids have appeared,\x01",
            "I can't enjoy my drives... How\x01",
            "long is this going to go on!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2037")

    label("loc_1F77")


    ChrTalk(
        0x9,
        (
            "With the highway movement\x01",
            "restrictions, only State Guard armored\x01",
            "cars pass by every now and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Now that Cryptids have\x01",
            "appeared, I can't drive... How\x01",
            "long is this going to go on!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2037")

    Jump("loc_33D2")

    label("loc_203C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_20D9")

    ChrTalk(
        0xFE,
        (
            "There was that attack,\x01",
            "and I'm scared to go out\x01",
            "on the highway, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's in times like these\x01",
            "that we have to protect\x01",
            "the village.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D2")

    label("loc_20D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_20E7")
    Jump("loc_33D2")

    label("loc_20E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2499")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2198")

    ChrTalk(
        0xFE,
        (
            "It seems Derrick and\x01",
            "Minneth's plan is\x01",
            "building to a climax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just how will this village\x01",
            "develop? ...Haha, I'm looking\x01",
            "forward to seeing it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2494")

    label("loc_2198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_242A")

    ChrTalk(
        0xFE,
        (
            "Wow. To think Minneth\x01",
            "was a swindler...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Say, everyone. This truck\x01",
            "that I bought from him...\x01",
            "What should I do with it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FIf I recall, you said earlier you\x01",
            "bought this orbal truck for 50,000\x01",
            "mira and market price is 500,000.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FH-Hmm... This is a\x01",
            "tricky problem, isn't\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FFor now, it might be best to\x01",
            "hand it to the police and let\x01",
            "them decide.\x02\x03",
            "#00104FYou purchased it in an official\x01",
            "transaction, so I think it'll\x01",
            "be returned immediately, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThat's right. It's best if\x01",
            "they investigate whether the\x01",
            "vehicle itself is illegal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I see... Well, I guess\x01",
            "I'll contact the police,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16F, 7)
    Jump("loc_2494")

    label("loc_242A")


    ChrTalk(
        0xFE,
        (
            "So I bought this new\x01",
            "truck from a swindler,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I guess I'll\x01",
            "contact the police,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2494")

    Jump("loc_33D2")

    label("loc_2499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_27A2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_263F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25BC")

    ChrTalk(
        0xFE,
        (
            "If you are looking for\x01",
            "Derrick, he's still in the\x01",
            "city meeting with Minneth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They should be talking at\x01",
            "the Entertainment District\x01",
            "hotel around now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Now then, seeing as how I've\x01",
            "got the latest model, I've got\x01",
            "to maintain it properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_263A")

    label("loc_25BC")


    ChrTalk(
        0xFE,
        (
            "If you're looking for Derrick, I wonder\x01",
            "if he isn't talking with Derrick at the\x01",
            "Entertainment District hotel around now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_263A")

    Jump("loc_279D")

    label("loc_263F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2712")

    ChrTalk(
        0xFE,
        (
            "Minneth is really a very\x01",
            "generous man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected of one who works\x01",
            "for Quincy Company, one of the\x01",
            "largest confectionery makers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I support his and\x01",
            "Derrick's plan\x01",
            "wholeheartedly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_279D")

    label("loc_2712")


    ChrTalk(
        0xFE,
        (
            "Minneth is really a very\x01",
            "generous man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected of one who works\x01",
            "for Quincy Company, one of the\x01",
            "largest confectionery makers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_279D")

    Jump("loc_33D2")

    label("loc_27A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2C01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 2)), scpexpr(EXPR_END)), "loc_29B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28A6")

    ChrTalk(
        0xFE,
        (
            "Huh... The lock on our\x01",
            "private property was\x01",
            "open, you say!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wow... So there's someone\x01",
            "out there that would do\x01",
            "such a thing, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank you for telling me.\x01",
            "I'll head over there in my\x01",
            "truck later to lock it up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29AC")

    label("loc_28A6")


    ChrTalk(
        0xFE,
        (
            "I'll have to head over to\x01",
            "the private property later\x01",
            "in my truck and lock it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...*sigh*, the truck's been\x01",
            "showing its age lately.\x01",
            "Driving isn't fun anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But the village doesn't have\x01",
            "the budget for a new one...\x01",
            "I'll have to make do somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29AC")

    Jump("loc_2BFC")

    label("loc_29B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ADB")

    ChrTalk(
        0xFE,
        (
            "Midway down Armorica Old Path, there's a\x01",
            "private property managed by the village.\x01",
            "I actually just got back from there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got tools and supplies\x01",
            "there, so you can't go in\x01",
            "there whenever you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I think it'll be\x01",
            "fine. We have it locked\x01",
            "so no one goes in.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BFC")

    label("loc_2ADB")


    ChrTalk(
        0xFE,
        (
            "Midway down Armorica Old Path, there's a\x01",
            "private property managed by the village.\x01",
            "I actually just got back from there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Come to think of it,\x01",
            "there's a foreign\x01",
            "visitor in the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if this black transport\x01",
            "belongs to him. Looks like a\x01",
            "very expensive car, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BFC")

    Jump("loc_33D2")

    label("loc_2C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2EFA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CB9")

    ChrTalk(
        0x9,
        (
            "I saw the special training.\x01",
            "That move I just saw was\x01",
            "one amazing technique.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, any match with the\x01",
            "bracers is sure to be a\x01",
            "good one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D56")

    label("loc_2CB9")


    ChrTalk(
        0x9,
        (
            "Wow. I saw that match\x01",
            "earlier, and my excitement\x01",
            "still hasn't died down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha. I'd like to spectate\x01",
            "another match with the\x01",
            "bracers again sometime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D56")

    Jump("loc_2EF5")

    label("loc_2D5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E91")

    ChrTalk(
        0x9,
        (
            "When I get excited, my\x01",
            "accent comes out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm not a young man\x01",
            "anymore, so I'd like to\x01",
            "fix it if possible, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I consulted Miria\x01",
            "about it, she said\x01",
            ""Don't worry about it."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tch, don't act like it's none of\x01",
            "your business... At this rate,\x01",
            "I'll be exposed as a bumpkin.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2EF5")

    label("loc_2E91")


    ChrTalk(
        0xFE,
        (
            "Miria told me not to\x01",
            "worry about my accent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tch, acting like it's\x01",
            "none of her business...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EF5")

    Jump("loc_33D2")

    label("loc_2EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_33D2")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3271")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30DD")

    ChrTalk(
        0x9,
        (
            "Hey, welcome to Armorica\x01",
            "Village.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x87, 0x1F4)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "Hey... W-What's with\x01",
            "that orbal car!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's not a Verne or Reinford\x01",
            "model... It's the first time\x01",
            "I've ever seen anything like it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FHaha, this one was\x01",
            "manufactured by ZCF.\x02\x03",
            "#10102FBecause it's equipped with a\x01",
            "new engine, it's top speed\x01",
            "is 1,500 selge per hour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Whoooa... That's great.\x01",
            "Simply amazing!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Noｱl's really proud of\x01",
            "it...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 5)
    Jump("loc_326C")

    label("loc_30DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31BF")

    ChrTalk(
        0x9,
        (
            "A top speed of 1500 selge an\x01",
            "hour... So even ZCF can make\x01",
            "amazing things like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Good, good! It makes me\x01",
            "want a new orbal truck\x01",
            "myself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Ahem. Ah, I got\x01",
            "excited and my accent\x01",
            "slipped out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_326C")

    label("loc_31BF")


    ChrTalk(
        0x9,
        (
            "...That reminds me, I wonder\x01",
            "who those suspicious people\x01",
            "the other day were...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, I guess it doesn't\x01",
            "really matter. It won't affect\x01",
            "the life of my orbal truck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_326C")

    Jump("loc_33D2")

    label("loc_3271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3325")

    ChrTalk(
        0x9,
        (
            "Hey, welcome to Armorica\x01",
            "Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We raise bees, crops and\x01",
            "livestock in this\x01",
            "village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The views are scenic\x01",
            "too. If you like, why\x01",
            "not stay a while?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_33D2")

    label("loc_3325")


    ChrTalk(
        0x9,
        (
            "...That reminds me, I wonder\x01",
            "who those suspicious people\x01",
            "the other day were...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, I guess it doesn't\x01",
            "really matter. It won't affect\x01",
            "the life of my orbal truck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33D2")

    TalkEnd(0xFE)
    Return()

    # Function_8_1A8B end

    def Function_9_33D6(): pass

    label("Function_9_33D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3501")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_346F")

    ChrTalk(
        0x8,
        (
            "Those adults sure are\x01",
            "noisy... That tree\x01",
            "really is amazing~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Climbing a tree that big\x01",
            "would be super-fun, I\x01",
            "bet.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_34FC")

    label("loc_346F")


    ChrTalk(
        0x8,
        (
            "Climbing a tree that big\x01",
            "would be super-fun, I\x01",
            "bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder if there's huge\x01",
            "rhinoceros beetle or something\x01",
            "in its branches, too~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34FC")

    Jump("loc_3F21")

    label("loc_3501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_36BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35F1")

    ChrTalk(
        0x8,
        (
            "Alright, let's play\x01",
            ""kick-the-can" today!\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0x10,
        (
            "#03805FKick the can~? What's\x01",
            "that~?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huh, you don't know\x01",
            "kick-the-can!? It can't\x01",
            "be helped, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Umm, we normally play\x01",
            "hide-and-seek, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0x10, 0xFF)
    Jump("loc_36B9")

    label("loc_35F1")


    ChrTalk(
        0x8,
        (
            "You see, because there's no\x01",
            "one to be "it" so I've been\x01",
            "playing with this can...\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0x10,
        (
            "#03809FI know. You crush it and\x01",
            "throw it in the trash,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I-I'm telling you,\x01",
            "that's not it!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)

    label("loc_36B9")

    Jump("loc_3F21")

    label("loc_36BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_37EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3786")

    ChrTalk(
        0x8,
        (
            "Mr. Harold came with\x01",
            "this kid the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm. So this must be\x01",
            "what it's like to have a\x01",
            "little brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm older, so I've got\x01",
            "to look after him\x01",
            "properly!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37E9")

    label("loc_3786")


    ChrTalk(
        0x8,
        (
            "I hope Mr. Harold moves\x01",
            "here too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It he does, I'll be able\x01",
            "to play with Colin every\x01",
            "day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37E9")

    Jump("loc_3F21")

    label("loc_37EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3971")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E7")

    ChrTalk(
        0x8,
        (
            "I heard some scary guys\x01",
            "rampaged in Crossbell\x01",
            "City the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because it's boring in this village,\x01",
            "I often think it'd be better if some\x01",
            "incident happened, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I never wanted something\x01",
            "like an attack.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_396C")

    label("loc_38E7")


    ChrTalk(
        0x8,
        (
            "It's always thought it's\x01",
            "too peaceful and boring\x01",
            "in this village, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But, it's possible that\x01",
            "it's actually a\x01",
            "blessing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_396C")

    Jump("loc_3F21")

    label("loc_3971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_397F")
    Jump("loc_3F21")

    label("loc_397F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3B3E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A06")

    ChrTalk(
        0x8,
        "Aww, today's boooring.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder if some big\x01",
            "incident will happen to wake\x01",
            "everyone up around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B39")

    label("loc_3A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD1")

    ChrTalk(
        0x8,
        (
            "Hey, wasn't that amazing\x01",
            "back there! Those huge\x01",
            "kitties came out like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Maybe that man was a\x01",
            "tamer at some circus\x01",
            "somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wow! I should have\x01",
            "gotten his autograph!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B39")

    label("loc_3AD1")


    ChrTalk(
        0x8,
        (
            "Maybe that man was a\x01",
            "tamer at some circus\x01",
            "somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wow! I should have\x01",
            "gotten his autograph!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B39")

    Jump("loc_3F21")

    label("loc_3B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3C83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C1A")

    ChrTalk(
        0x8,
        (
            "Recently a foreigner\x01",
            "that often comes to our\x01",
            "village gave us sweets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because we weren't\x01",
            "polite, I thought he'd\x01",
            "get mad, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Man, there are kind\x01",
            "people in this world for\x01",
            "sure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C7E")

    label("loc_3C1A")


    ChrTalk(
        0x8,
        (
            "We were rude to the\x01",
            "foreigner but he gave us\x01",
            "candy instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My mom scolded us after\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C7E")

    Jump("loc_3F21")

    label("loc_3C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3D3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C9E")
    Call(0, 10)
    Jump("loc_3D38")

    label("loc_3C9E")


    ChrTalk(
        0x8,
        (
            "Hmm. It's the same kick-\x01",
            "the-can. It's fishy that\x01",
            "the rules are different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then today, it's going to\x01",
            "be Stefan's Crossbell-\x01",
            "style kick the can!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D38")

    Jump("loc_3F21")

    label("loc_3D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3DBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D58")
    Call(0, 10)
    Jump("loc_3DBA")

    label("loc_3D58")


    ChrTalk(
        0x8,
        (
            "That's right, there's\x01",
            "that huge building in\x01",
            "town, huh~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I want to explore it\x01",
            "sometime~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DBA")

    Jump("loc_3F21")

    label("loc_3DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EB2")

    ChrTalk(
        0x8,
        (
            "Tch, it's too peaceful\x01",
            "and boring in this\x01",
            "village~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you want hear about recent news,\x01",
            "it's nothing but "Our cow gave\x01",
            "birth", and other stuff like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Aww, I wonder if some\x01",
            "big incident will occur.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3F21")

    label("loc_3EB2")


    ChrTalk(
        0x8,
        (
            "Well, the cow's calf was\x01",
            "cute, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If the big incident I\x01",
            "want happens, it won't\x01",
            "be that peaceful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F21")

    TalkEnd(0xFE)
    Return()

    # Function_9_33D6 end

    def Function_10_3F25(): pass

    label("Function_10_3F25")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_407D")

    ChrTalk(
        0x8,
        (
            "Alright then, let's play\x01",
            "kick-the-can!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The demon absolutely\x01",
            "can't go to high places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Pooley, you should be\x01",
            "the demon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Huh? So you're fine\x01",
            "standing on a high spot\x01",
            "in less than 3 seconds?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...What are you saying?\x01",
            "That's the first I've\x01",
            "heard of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hey, hey, Pooley should\x01",
            "be the demon!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    Jump("loc_41B5")

    label("loc_407D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_41B5")

    ChrTalk(
        0xB,
        (
            "That reminds me, they had\x01",
            "the Orchis Tower\x01",
            "unveiling ceremony today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Orchis Tower? What's\x01",
            "that? Food?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "A snack?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "N-No, no. It's a really\x01",
            "huge building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "According to rumors, you\x01",
            "can see all of Crossbell\x01",
            "from its roof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wow, amazing! I want to\x01",
            "go there sometime.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)

    label("loc_41B5")

    SetScenarioFlags(0x0, 7)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_10_3F25 end

    def Function_11_41C5(): pass

    label("Function_11_41C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4232")

    ChrTalk(
        0xA,
        (
            "Colin left for the city\x01",
            "with Mr. Harold~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He promised he come play\x01",
            "with me again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_477A")

    label("loc_4232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_43C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_432A")

    ChrTalk(
        0xA,
        (
            "My brother only cares\x01",
            "about Colin. How boring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Mom says Pooley has to be\x01",
            "a little patient since\x01",
            "she's like a big sister.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "Pooley will have\x01",
            "patience. ...'Cause\x01",
            "she's a big sister♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43C4")

    label("loc_432A")


    ChrTalk(
        0xA,
        (
            "Pooley is a bit of a big\x01",
            "sister to Colin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even if he takes away bro's attention,\x01",
            "Pooley will have some patience.\x01",
            "...'Cause she's a big sister♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43C4")

    Jump("loc_477A")

    label("loc_43C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4431")

    ChrTalk(
        0xA,
        (
            "Lately, all my brother\x01",
            "cares about is Colin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But he's MY BROTHER...\x01",
            "How unfair.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_477A")

    label("loc_4431")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4520")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44A9")

    ChrTalk(
        0xA,
        (
            "Looks like Stefan\x01",
            "returned to the village\x01",
            "earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hope he comes to visit\x01",
            "soon~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_451B")

    label("loc_44A9")


    ChrTalk(
        0xA,
        (
            "Lately, I've been\x01",
            "playing this whole time\x01",
            "with my brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But, as expected, it's\x01",
            "more fun with Stefan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_451B")

    Jump("loc_477A")

    label("loc_4520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_452E")
    Jump("loc_477A")

    label("loc_452E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_45EB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4565")

    ChrTalk(
        0xA,
        "I want to play Bracer!\x02",
    )

    CloseMessageWindow()
    Jump("loc_45E6")

    label("loc_4565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45BE")

    ChrTalk(
        0xA,
        (
            "Meow, meow. What a huge\x01",
            "kitty~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It wasn't that cute,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_45E6")

    label("loc_45BE")


    ChrTalk(
        0xA,
        (
            "As expected, I like\x01",
            "small kitties.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45E6")

    Jump("loc_477A")

    label("loc_45EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4661")

    ChrTalk(
        0xA,
        (
            "My brother got a\x01",
            "spanking from my mom the\x01",
            "other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*shiver*. His butt was\x01",
            "red as an apple~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_477A")

    label("loc_4661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4696")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_467C")
    Call(0, 10)
    Jump("loc_4691")

    label("loc_467C")


    ChrTalk(
        0xA,
        "I love demons!!\x02",
    )

    CloseMessageWindow()

    label("loc_4691")

    Jump("loc_477A")

    label("loc_4696")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4706")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46B1")
    Call(0, 10)
    Jump("loc_4701")

    label("loc_46B1")


    ChrTalk(
        0xA,
        (
            "When my brother gives me a\x01",
            "piggyback ride, I wonder\x01",
            "which of us is taller?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4701")

    Jump("loc_477A")

    label("loc_4706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_477A")

    ChrTalk(
        0xA,
        (
            "It's not boring at all\x01",
            "when my brother's\x01",
            "around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Lately, it's been fun\x01",
            "playing with Stefan,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_477A")

    TalkEnd(0xFE)
    Return()

    # Function_11_41C5 end

    def Function_12_477E(): pass

    label("Function_12_477E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_492C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_487F")

    ChrTalk(
        0xB,
        (
            "Hmm. I think this is a major incident\x01",
            "for some reason, but... I wonder if\x01",
            "it's all right to be this carefree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, I guess this is\x01",
            "one of their redeeming\x01",
            "qualities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I've got to be ready, no\x01",
            "matter what happens.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4927")

    label("loc_487F")


    ChrTalk(
        0xB,
        (
            "Being always carefree is one of Camille\x01",
            "and Pooley's good points, but... As\x01",
            "expected, this is a major incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I've got to be ready, no\x01",
            "matter what happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4927")

    Jump("loc_4FB0")

    label("loc_492C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4A2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49E0")

    ChrTalk(
        0xB,
        (
            "Colin is a bit\x01",
            "irresponsible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Earlier, he went out on\x01",
            "the highway, saying those\x01",
            "blue flowers are pretty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We've got to watch him\x01",
            "properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4A29")

    label("loc_49E0")


    ChrTalk(
        0xB,
        (
            "Colin is a bit\x01",
            "irresponsible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We've got to watch him\x01",
            "properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A29")

    Jump("loc_4FB0")

    label("loc_4A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4AF4")

    ChrTalk(
        0xB,
        (
            "Mr. Harold and his family\x01",
            "have been staying at the\x01",
            "Ash Tree Inn for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "They helped me and my mom when we\x01",
            "moved here. The people of this\x01",
            "village are really openhearted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB0")

    label("loc_4AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4B02")
    Jump("loc_4FB0")

    label("loc_4B02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4B10")
    Jump("loc_4FB0")

    label("loc_4B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4C41")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B57")

    ChrTalk(
        0xB,
        (
            "I'm already tired of\x01",
            "playing Bracer...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C3C")

    label("loc_4B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BE0")

    ChrTalk(
        0xB,
        (
            "I knew that man was\x01",
            "rotten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I can't believe he'd release\x01",
            "monsters in town... I thought\x01",
            "I was gonna be eaten.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4C3C")

    label("loc_4BE0")


    ChrTalk(
        0xB,
        (
            "Even so, when they were about\x01",
            "to be attacked, that brother\x01",
            "and sister were carefree...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C3C")

    Jump("loc_4FB0")

    label("loc_4C41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4CC2")

    ChrTalk(
        0xB,
        (
            "That man doesn't sit\x01",
            "well with me for some\x01",
            "reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He smiles and is nice,\x01",
            "but his eyes aren't\x01",
            "smiling...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB0")

    label("loc_4CC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4D65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CDD")
    Call(0, 10)
    Jump("loc_4D60")

    label("loc_4CDD")


    ChrTalk(
        0xB,
        (
            "In Crossbell City it's fine\x01",
            "if the demon gets to a high\x01",
            "spot within 3 seconds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This must be what they\x01",
            "call a local rule.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D60")

    Jump("loc_4FB0")

    label("loc_4D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4E31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D80")
    Call(0, 10)
    Jump("loc_4E2C")

    label("loc_4D80")


    ChrTalk(
        0xB,
        (
            "Hmmm, I see. It's been under a\x01",
            "big curtain until now, so it's no\x01",
            "wonder you don't know about it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Now that that curtain\x01",
            "has come down, the whole\x01",
            "city's excited.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E2C")

    Jump("loc_4FB0")

    label("loc_4E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4FB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F2D")

    ChrTalk(
        0xB,
        (
            "Before, I lived with my\x01",
            "mom in Crossbell City,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Now that we're living in\x01",
            "Armorica Village, every\x01",
            "day seems fresh somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Even I don't understand\x01",
            "why I hated the idea of\x01",
            "coming here at first.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    SetChrFlags(0xB, 0x10)
    OP_93(0xB, 0x6B, 0x0)
    Jump("loc_4FB0")

    label("loc_4F2D")


    ChrTalk(
        0xB,
        (
            "I think it's pretty amazing\x01",
            "that a calf birth is seen\x01",
            "as no big deal, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I guess if you live\x01",
            "here, it seems natural.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FB0")

    TalkEnd(0xFE)
    Return()

    # Function_12_477E end

    def Function_13_4FB4(): pass

    label("Function_13_4FB4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4FC5")
    Jump("loc_5887")

    label("loc_4FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_515C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50E1")

    ChrTalk(
        0xC,
        (
            "The invalidity declaration... It's\x01",
            "unrelated to this village so I don't\x01",
            "think it will have much effect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But, there are no small number of\x01",
            "villagers who feel anxious about\x01",
            "sudden changes in the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I need to visit each\x01",
            "villager's home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5157")

    label("loc_50E1")


    ChrTalk(
        0xC,
        (
            "There are many of them\x01",
            "worried about sudden\x01",
            "changes in the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I need to visit each\x01",
            "villager's home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5157")

    Jump("loc_5887")

    label("loc_515C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_533D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_527E")

    ChrTalk(
        0xC,
        (
            "Those strange blue lotus flowers...\x01",
            "A little while ago, they started\x01",
            "blooming in the lotus fields.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The flowers have an effect\x01",
            "on their growth, so I want\x01",
            "to weed them out, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Damn. No matter how many\x01",
            "times I pull them out,\x01",
            "they grow right back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5338")

    label("loc_527E")


    ChrTalk(
        0xC,
        (
            "These lotus field are precious to the\x01",
            "village, so I want to do something\x01",
            "about those blue flowers, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Damn. No matter how many\x01",
            "times I pull them out,\x01",
            "they grow right back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5338")

    Jump("loc_5887")

    label("loc_533D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_54CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5453")

    ChrTalk(
        0xC,
        (
            "Ever since the attack on the\x01",
            "city, we've started\x01",
            "patrolling near the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Now that that has happened, it\x01",
            "wouldn't be strange for\x01",
            "something to occur elsewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Anyway, we have to do\x01",
            "everything we can for the\x01",
            "safety of the village.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_54C7")

    label("loc_5453")


    ChrTalk(
        0xC,
        (
            "We've started patrolling\x01",
            "near the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We have to do everything\x01",
            "we can for the safety of\x01",
            "the village.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54C7")

    Jump("loc_5887")

    label("loc_54CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_54DA")
    Jump("loc_5887")

    label("loc_54DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_54E8")
    Jump("loc_5887")

    label("loc_54E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_54F6")
    Jump("loc_5887")

    label("loc_54F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5504")
    Jump("loc_5887")

    label("loc_5504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_56CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5635")

    ChrTalk(
        0xC,
        (
            "For the continued existence of Armorica\x01",
            "Village, I gave the chief several\x01",
            "reform proposals yesterday, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In the end, they were all\x01",
            "rejected, and we had the\x01",
            "same usual arguments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My father, the chief...\x01",
            "Can't he sense the danger in\x01",
            "maintaining the status quo?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_56C5")

    label("loc_5635")


    ChrTalk(
        0xC,
        (
            "I offered several reform\x01",
            "proposals yesterday,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My father, the chief...\x01",
            "Can't he sense the danger in\x01",
            "maintaining the status quo?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56C5")

    Jump("loc_5887")

    label("loc_56CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5887")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57F3")

    ChrTalk(
        0xC,
        (
            "I can't say our agriculture and livestock\x01",
            "have been doing well lately. The\x01",
            "village's finances are in poor shape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But my father, the chief... He\x01",
            "hasn't yet changed his\x01",
            "conservative ways of thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...As the next chief,\x01",
            "I've got to do something\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5887")

    label("loc_57F3")


    ChrTalk(
        0xC,
        (
            "For the continued existence\x01",
            "of Armorica Village, we\x01",
            "can't be bound by tradition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...As the next chief,\x01",
            "I've got to do something\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5887")

    TalkEnd(0xFE)
    Return()

    # Function_13_4FB4 end

    def Function_14_588B(): pass

    label("Function_14_588B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_59A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5937")

    NpcTalk(
        0xD,
        "Well-Dressed Man",
        (
            "This is Armorica\x01",
            "Village... As I had heard,\x01",
            "it's a pretty nice place.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Well-Dressed Man",
        (
            "Haha. I'll begin work\x01",
            "ASAP.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_59A3")

    label("loc_5937")


    NpcTalk(
        0xD,
        "Well-Dressed Man",
        "I'll begin work ASAP.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Well-Dressed Man",
        (
            "Now then, the village\x01",
            "chief's house is...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59A3")

    TalkEnd(0xFE)
    Return()

    # Function_14_588B end

    def Function_15_59A7(): pass

    label("Function_15_59A7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_59B8")
    Jump("loc_5A65")

    label("loc_59B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5A5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59D3")
    Call(0, 16)
    Jump("loc_5A57")

    label("loc_59D3")


    ChrTalk(
        0xE,
        (
            "Haha. That Sophia really\x01",
            "does worry too much\x01",
            "about Colin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "But it's all right.\x01",
            "Children grow after each\x01",
            "injury, after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A57")

    Jump("loc_5A65")

    label("loc_5A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5A65")

    label("loc_5A65")

    TalkEnd(0xFE)
    Return()

    # Function_15_59A7 end

    def Function_16_5A69(): pass

    label("Function_16_5A69")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xF,
        (
            "#03708FColin, I wonder if he'll\x01",
            "be all right...\x01",
            "(*fidget*)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Haha, Sophia. It'll be\x01",
            "all right. You don't\x01",
            "have to worry so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "At first, I was worried\x01",
            "because my Stefan was a\x01",
            "weakling, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "In order for children to be\x01",
            "healthy, I think you have to let\x01",
            "them play mischievously a bit.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 500)

    ChrTalk(
        0xF,
        (
            "#03700FY-You're right. If I'm too\x01",
            "overprotective, Colin won't\x01",
            "be able to enjoy himself...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x10)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_93(0xF, 0x118, 0x0)
    Return()

    # Function_16_5A69 end

    def Function_17_5C23(): pass

    label("Function_17_5C23")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5C34")
    Jump("loc_5CE0")

    label("loc_5C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5CC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C4F")
    Call(0, 16)
    Jump("loc_5CC4")

    label("loc_5C4F")


    ChrTalk(
        0xF,
        (
            "#03700F...I feel the same. It's\x01",
            "not good if I'm too\x01",
            "overprotective.\x02\x03",
            "#03709FI mean, Colin's having\x01",
            "so much fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CC4")

    Jump("loc_5CE0")

    label("loc_5CC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_5CD7")
    Jump("loc_5CE0")

    label("loc_5CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5CE0")

    label("loc_5CE0")

    TalkEnd(0xFE)
    Return()

    # Function_17_5C23 end

    def Function_18_5CE4(): pass

    label("Function_18_5CE4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5CF5")
    Jump("loc_5D84")

    label("loc_5CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5D6D")

    ChrTalk(
        0x10,
        (
            "#03800FIt's fun playing with so\x01",
            "many friends!\x02\x03",
            "#03809FI wonder if we can take\x01",
            "Sunita here next time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D84")

    label("loc_5D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_5D7B")
    Jump("loc_5D84")

    label("loc_5D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5D84")

    label("loc_5D84")

    TalkEnd(0xFE)
    Return()

    # Function_18_5CE4 end

    def Function_19_5D88(): pass

    label("Function_19_5D88")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60C3")

    ChrTalk(
        0xFE,
        (
            "I'm looking for a way to do\x01",
            "something about the Pleroma\x01",
            "Grass in this lotus field.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you pull them out, they grow\x01",
            "back immediately... I'd like to\x01",
            "exterminate them somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see... They're the cause of\x01",
            "Cryptid appearances, so dealing\x01",
            "with them is a top priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well for now, I'll try\x01",
            "everything I can think\x01",
            "of.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "That's right, there's\x01",
            "something I'd like you\x01",
            "all to hear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I've decided to marry\x01",
            "my fiancｳe, Pearl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of the situation though,\x01",
            "please keep it a secret from Pearl...\x01",
            "I've already started the preparations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FMy... Haha,\x01",
            "congratulations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. It's precisely because\x01",
            "of this situation that I\x01",
            "wanted something to protect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I've decided on a date\x01",
            "for the ceremony, I'll invite\x01",
            "you all, so please come.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BB, 1)
    Jump("loc_617E")

    label("loc_60C3")


    ChrTalk(
        0xFE,
        (
            "I've kept Pearl waiting\x01",
            "long enough already... I'll\x01",
            "marry her before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To protect her as well, I've got to\x01",
            "focus more than ever on being the\x01",
            "best Crossbell Bracer I can be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_617E")

    TalkEnd(0xFE)
    Return()

    # Function_19_5D88 end

    def Function_20_6182(): pass

    label("Function_20_6182")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_626A")

    ChrTalk(
        0x26,
        (
            "We'll see the sights\x01",
            "here for a while, then\x01",
            "return to Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "No matter how many times\x01",
            "I thanked you guys, it\x01",
            "wouldn't be enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Allow me to thank you\x01",
            "once again for reuniting\x01",
            "me with my father.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_62FA")

    label("loc_626A")


    ChrTalk(
        0x26,
        (
            "No matter how many times\x01",
            "I thanked you guys, it\x01",
            "wouldn't be enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Allow me to thank you\x01",
            "once again for reuniting\x01",
            "me with my father.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62FA")

    TalkEnd(0xFE)
    Return()

    # Function_20_6182 end

    def Function_21_62FE(): pass

    label("Function_21_62FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_638F")

    ChrTalk(
        0xFE,
        (
            "Uhuhu, Almin seems happy\x01",
            "to see his father-in-law\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There, there. Isn't that\x01",
            "great, Almin㈱\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Baby",
        "Goo goo.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_63EC")

    label("loc_638F")


    ChrTalk(
        0xFE,
        (
            "There, there, let's go\x01",
            "say hello to grandfather\x01",
            "again later, hm～?㈱\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Baby",
        "Goo goo.\x02",
    )

    CloseMessageWindow()

    label("loc_63EC")

    TalkEnd(0xFE)
    Return()

    # Function_21_62FE end

    def Function_22_63F0(): pass

    label("Function_22_63F0")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6422")
    SetScenarioFlags(0x31, 2)

    label("loc_6422")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6468")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_6462")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6457")
    Sound(2499, 255, 100, 0)
    Jump("loc_645D")

    label("loc_6457")

    Sound(3537, 255, 100, 0)

    label("loc_645D")

    Jump("loc_6468")

    label("loc_6462")

    Sound(3344, 255, 100, 0)

    label("loc_6468")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_671F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_64DD")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_64BD"),
        (SWITCH_DEFAULT, "loc_64CE"),
    )


    label("loc_64BD")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_64D8")

    label("loc_64CE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_64D8")

    Jump("loc_671A")

    label("loc_64DD")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_650F")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_650F")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6543"),
        (1, "loc_6647"),
        (2, "loc_66D8"),
        (SWITCH_DEFAULT, "loc_6710"),
    )


    label("loc_6543")

    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_6574")
    OP_70(0x8, 0x12C)
    OP_71(0x8, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_6584")

    label("loc_6574")

    OP_70(0x8, 0xF0)
    OP_71(0x8, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_6584")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65DA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_65DA")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65FD")
    Sound(461, 0, 100, 0)

    label("loc_65FD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_661D")
    OP_70(0x8, 0x14A)
    OP_71(0x8, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_662D")

    label("loc_661D")

    OP_70(0x8, 0x10E)
    OP_71(0x8, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_662D")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x8, "light", 0x1, 0x1)
    OP_70(0x8, 0x0)
    Jump("loc_6468")

    label("loc_6647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_66B9")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_667C")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_6694")

    label("loc_667C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_668F")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_6694")

    label("loc_668F")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_6694")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_66D3")

    label("loc_66B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_66C9")
    OP_AF(0xFB)
    Jump("loc_66D3")

    label("loc_66C9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_66D3")

    Jump("loc_671A")

    label("loc_66D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66F1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_670B")

    label("loc_66F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_6701")
    OP_AF(0xFB)
    Jump("loc_670B")

    label("loc_6701")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_670B")

    Jump("loc_671A")

    label("loc_6710")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_671A")

    Jump("loc_6468")

    label("loc_671F")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_22_63F0 end

    def Function_23_672D(): pass

    label("Function_23_672D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_677D")
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

    label("loc_677D")

    Call(0, 3)
    Return()

    # Function_23_672D end

    def Function_24_6781(): pass

    label("Function_24_6781")

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
    OP_68(11620, 1500, 1410, 1500)
    MoveCamera(328, 26, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(16250, 1500)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6843")
    OP_E2(0x2)
    MiniGame(0x6, 0x1B, 0x300C, 0x0, 0x1478, 0xB4, 0x2A8A, 0xFFFFFA56, 0x4BA)

    label("loc_6843")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_24_6781 end

    def Function_25_6848(): pass

    label("Function_25_6848")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch32000.itc", 0x1E)
    LoadChrToIndex("chr/ch32100.itc", 0x1F)
    LoadChrToIndex("chr/ch24300.itc", 0x20)
    LoadChrToIndex("chr/ch25200.itc", 0x21)
    LoadChrToIndex("chr/ch24500.itc", 0x22)
    LoadChrToIndex("chr/ch24000.itc", 0x23)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    LoadChrToIndex("chr/ch00350.itc", 0x26)
    LoadChrToIndex("chr/ch02950.itc", 0x27)
    LoadChrToIndex("chr/ch03050.itc", 0x28)
    LoadChrToIndex("chr/ch32050.itc", 0x29)
    LoadChrToIndex("chr/ch32152.itc", 0x2A)
    Call(0, 26)
    LoadChrToIndex("chr/ch24300.itc", 0x20)
    LoadChrToIndex("chr/ch25200.itc", 0x21)
    LoadChrToIndex("chr/ch24500.itc", 0x22)
    LoadChrToIndex("chr/ch24000.itc", 0x23)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    LoadChrToIndex("chr/ch00350.itc", 0x26)
    LoadChrToIndex("chr/ch02950.itc", 0x27)
    LoadChrToIndex("chr/ch03050.itc", 0x28)
    LoadChrToIndex("chr/ch00053.itc", 0x2B)
    LoadChrToIndex("chr/ch00153.itc", 0x2C)
    LoadChrToIndex("chr/ch00353.itc", 0x2D)
    LoadChrToIndex("chr/ch02953.itc", 0x2E)
    LoadChrToIndex("chr/ch03053.itc", 0x2F)
    LoadChrToIndex("chr/ch32000.itc", 0x1E)
    LoadChrToIndex("chr/ch32100.itc", 0x1F)
    LoadChrToIndex("chr/ch32050.itc", 0x29)
    LoadChrToIndex("chr/ch32152.itc", 0x2A)
    LoadChrToIndex("chr/ch32053.itc", 0x30)
    LoadChrToIndex("chr/ch32153.itc", 0x31)
    LoadChrToIndex("chr/ch32154.itc", 0x32)
    LoadEffect(0x0, "event/ev12020.eff")
    LoadEffect(0x1, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\mgaria1.eff")
    LoadEffect(0x3, "battle\\mg130_00.eff")
    Call(0, 27)
    LoadChrToIndex("chr/ch24300.itc", 0x20)
    LoadChrToIndex("chr/ch25200.itc", 0x21)
    LoadChrToIndex("chr/ch24500.itc", 0x22)
    LoadChrToIndex("chr/ch24000.itc", 0x23)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    LoadChrToIndex("chr/ch00350.itc", 0x26)
    LoadChrToIndex("chr/ch02950.itc", 0x27)
    LoadChrToIndex("chr/ch03050.itc", 0x28)
    LoadChrToIndex("chr/ch00053.itc", 0x2B)
    LoadChrToIndex("chr/ch00153.itc", 0x2C)
    LoadChrToIndex("chr/ch00353.itc", 0x2D)
    LoadChrToIndex("chr/ch02953.itc", 0x2E)
    LoadChrToIndex("chr/ch03053.itc", 0x2F)
    LoadChrToIndex("chr/ch32000.itc", 0x1E)
    LoadChrToIndex("chr/ch32100.itc", 0x1F)
    LoadChrToIndex("chr/ch32050.itc", 0x29)
    LoadChrToIndex("chr/ch32152.itc", 0x2A)
    LoadChrToIndex("chr/ch32053.itc", 0x30)
    LoadChrToIndex("chr/ch32153.itc", 0x31)
    LoadChrToIndex("chr/ch32154.itc", 0x32)
    LoadChrToIndex("chr/ch00052.itc", 0x33)
    LoadChrToIndex("chr/ch00057.itc", 0x34)
    LoadEffect(0x1, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\mgaria1.eff")
    LoadEffect(0x3, "battle\\mg130_00.eff")
    LoadEffect(0x4, "battle\\cr000500.eff")
    LoadEffect(0x5, "battle\\cr000501.eff")
    LoadEffect(0x6, "battle\\cr000102.eff")
    Call(0, 29)
    Return()

    # Function_25_6848 end

    def Function_26_6A8A(): pass

    label("Function_26_6A8A")

    EventBegin(0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrPos(0x18, 9600, 0, -18150, 238)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrPos(0x19, 10650, 0, -19830, 238)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 1970, 0, -14340, 136)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 1700, 0, -12600, 136)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 490, 0, -13860, 136)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrPos(0x1A, 3250, 0, -13270, 150)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrPos(0x1B, 4380, 0, -9290, 136)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrPos(0x1C, 370, 0, -11950, 150)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 2550, 0, -10030, 150)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 5530, 0, -10320, 150)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrPos(0x1D, 4350, 0, -11650, 150)
    OP_68(7840, 2500, -21280, 0)
    MoveCamera(358, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16070, 0)
    SetChrPos(0x101, 7290, 0, -20490, 46)
    SetChrPos(0x102, 8520, 0, -22110, 46)
    SetChrPos(0x104, 8230, 0, -23660, 46)
    SetChrPos(0x109, 6700, 0, -22920, 46)
    SetChrPos(0x105, 6010, 0, -21490, 46)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(7840, 1200, -21280, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(1000)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00005FWow... Look at all the\x01",
            "spectators.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6CCB():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6CCB)
    Sleep(50)

    def lambda_6CDB():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_6CDB)

    def lambda_6CE8():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6CE8)
    Sleep(50)

    def lambda_6CF8():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6CF8)

    def lambda_6D05():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6D05)
    Sleep(50)

    def lambda_6D15():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6D15)
    Sleep(300)

    ChrTalk(
        0x18,
        (
            "#12PYeah, it seems word's\x01",
            "gotten around.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(4450, 1500, -14100, 3000)
    MoveCamera(7, 29, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(16620, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#5PHehe, bracers are\x01",
            "invincible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe police 'll be a\x01",
            "piece of cake.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    ChrTalk(
        0xA,
        (
            "#11PPiece of cake? What's\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    ChrTalk(
        0xB,
        (
            "#5PUh, basically they don't\x01",
            "stand a chance.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x96, 0x1F4)

    ChrTalk(
        0xB,
        (
            "#5PBut the SSS guys seem\x01",
            "pretty strong somehow.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x96, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#5PYeah, things are heating\x01",
            "up!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x1D, 500)

    ChrTalk(
        0x9,
        (
            "#11PSo who's your money on,\x01",
            "Chief?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#5PHmm, let me see... Both\x01",
            "of them have helped me\x01",
            "out in the past, you see.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x9, 0x96, 0x1F4)
    Fade(500)
    OP_68(7840, 1200, -21280, 0)
    MoveCamera(358, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16070, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#12P#00106FE-Even the chief's\x01",
            "here...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x19,
        (
            "#12PMaybe I should say that\x01",
            "I only told the chief\x01",
            "about our match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHaha, I'd expect no less\x01",
            "of a rural town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FYeah. Information\x01",
            "spreads terrifyingly\x01",
            "fast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112FAhaha... I'm getting\x01",
            "nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12PHaha. Well having an\x01",
            "audience is good every\x01",
            "once in a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0xEE, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x18,
        (
            "#11PAlright, I want to get\x01",
            "into our match.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_70F2():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_70F2)
    Sleep(50)

    def lambda_7102():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7102)

    def lambda_710F():
        OP_93(0xFE, 0xEE, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_710F)
    Sleep(50)

    def lambda_711F():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_711F)
    Sleep(50)

    def lambda_712F():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_712F)
    Sleep(50)

    def lambda_713F():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_713F)
    Sleep(300)

    ChrTalk(
        0x18,
        (
            "#11PFirst, we'll need to\x01",
            "pick the format.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PHmm... There are\x01",
            "different ways I can see\x01",
            "doing this, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PI think two-on-two is\x01",
            "best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#5PYeah, I was thinking\x01",
            "that too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PIs that ok with you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FWell you guys put in the\x01",
            "request, so I don't have\x01",
            "a problem with it.\x02\x03",
            "#00000FCan we pick who gets to\x01",
            "fight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PYeah, sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PBut you have to fight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PHaha, it's not that\x01",
            "surprising, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PIt's not like we wanted\x01",
            "to see your personal\x01",
            "strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PThe unity of the SSS that\x01",
            "you're the center of...\x01",
            "That's what we want to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Yeah, yeah! Without the\x01",
            "leader, there'd be no\x01",
            "point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FDamn, just look at this\x01",
            "guy!\x02\x03",
            "To have these lovely\x01",
            "ladies taken from me\x01",
            "like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHehe, I see. So this is\x01",
            "the rumored younger\x01",
            "brother complex.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FI felt like I heard some\x01",
            "improper comments,\x01",
            "but... Whatever.\x02\x03",
            "#00000FIf that's how it's going\x01",
            "to be, that's just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FThen, who's going to be\x01",
            "your partner, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FHmm, let me think...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Fight with Elie\x01",       # 0
            "Fight with Randy\x01",      # 1
            "Fight with Noｱl\x01",      # 2
            "Fight with Wazy\x01",       # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7710")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x1)
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#5P#00000FElie, will you do it?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#00104FYes, of course.\x02\x03",
            "#00102FLet's show them our\x01",
            "combined strength.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7949")

    label("loc_7710")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77CD")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x2)
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#5P#00000FRandy, can I ask you?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#12P#00309FYeah, 'course!\x02\x03",
            "#00300FOur combination\x01",
            "attack... Let's throw it\x01",
            "at these ladies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7949")

    label("loc_77CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7886")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x3)
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#00000FNoｱl, can I ask you?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10109FYes, of course!\x02\x03",
            "#10100FOur combination craft...\x01",
            "Let's throw it at those\x01",
            "two!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7949")

    label("loc_7886")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x4)
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FWazy, care to fight with\x01",
            "me?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#6P#10304FHehe. If it is your\x01",
            "wish, I would love to.\x02\x03",
            "#10302FLet's show those ladies\x01",
            "our duet for a surprise.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7949")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_32(0xFF, 0xFA, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7982")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_79DA")

    label("loc_7982")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79A6")
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_79DA")

    label("loc_79A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79CA")
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_79DA")

    label("loc_79CA")

    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_79DA")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(8610, 1700, -21420, 0)
    MoveCamera(4, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12790, 0)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A7B")
    SetChrPos(0x104, 13650, 0, -14300, 225)
    SetChrPos(0x109, 14800, 0, -14550, 225)
    SetChrPos(0x105, 13100, 0, -12850, 225)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_7B6F")

    label("loc_7A7B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AD3")
    SetChrPos(0x102, 13650, 0, -14300, 225)
    SetChrPos(0x109, 14800, 0, -14550, 225)
    SetChrPos(0x105, 13100, 0, -12850, 225)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_7B6F")

    label("loc_7AD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B2B")
    SetChrPos(0x102, 13650, 0, -14300, 225)
    SetChrPos(0x104, 14800, 0, -14550, 225)
    SetChrPos(0x105, 13100, 0, -12850, 225)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_7B6F")

    label("loc_7B2B")

    SetChrPos(0x102, 13650, 0, -14300, 225)
    SetChrPos(0x104, 14800, 0, -14550, 225)
    SetChrPos(0x109, 13100, 0, -12850, 225)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_7B6F")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x19,
        "#11PIt's decided!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PReady your weapons, you\x01",
            "two.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(10960, 1000)
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BF4")
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_7C3A")

    label("loc_7BF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C10")
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x0)
    Jump("loc_7C3A")

    label("loc_7C10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C32")
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_7C3A")

    label("loc_7C32")

    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)

    label("loc_7C3A")

    OP_0D()
    Fade(500)
    Sound(812, 0, 100, 0)
    Sound(859, 0, 50, 0)
    SetChrChipByIndex(0x18, 0x29)
    SetChrChipByIndex(0x19, 0x2A)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x1)
    OP_0D()

    ChrTalk(
        0x18,
        "#4S#11POk, here we go!\x02",
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CA4")
    SetChrBattleFlags(0x104, 0x8)
    SetChrBattleFlags(0x109, 0x8)
    SetChrBattleFlags(0x105, 0x8)
    Jump("loc_7CF9")

    label("loc_7CA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CC7")
    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x109, 0x8)
    SetChrBattleFlags(0x105, 0x8)
    Jump("loc_7CF9")

    label("loc_7CC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CEA")
    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x104, 0x8)
    SetChrBattleFlags(0x105, 0x8)
    Jump("loc_7CF9")

    label("loc_7CEA")

    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x104, 0x8)
    SetChrBattleFlags(0x109, 0x8)

    label("loc_7CF9")

    Battle("BattleInfo_774", 0x30200011, 0x0, 0x0, 0xE, 0xFF)
    FadeToDark(0, 0, -1)
    ClearChrBattleFlags(0x102, 0x8)
    ClearChrBattleFlags(0x104, 0x8)
    ClearChrBattleFlags(0x109, 0x8)
    ClearChrBattleFlags(0x105, 0x8)
    Return()

    # Function_26_6A8A end

    def Function_27_7D28(): pass

    label("Function_27_7D28")

    EventBegin(0x0)
    SoundLoad(832)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrPos(0x18, 9600, 0, -18150, 238)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrPos(0x19, 10650, 0, -19830, 238)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 1970, 0, -14340, 136)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 1700, 0, -12600, 136)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 490, 0, -13860, 136)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrPos(0x1A, 3250, 0, -13270, 150)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrPos(0x1B, 4380, 0, -9290, 136)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrPos(0x1C, 370, 0, -11950, 150)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 2550, 0, -10030, 150)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 5530, 0, -10320, 150)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrPos(0x1D, 4350, 0, -11650, 150)
    OP_68(7310, 1800, -22770, 0)
    MoveCamera(4, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13320, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83BF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x3)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F2D")
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrSubChip(0x102, 0x3)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_8039")

    label("loc_7F2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F8D")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x3)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_8039")

    label("loc_7F8D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FED")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrSubChip(0x109, 0x3)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_8039")

    label("loc_7FED")

    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x105, 0x3)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_8039")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#00006F*pant, pant*... It's no\x01",
            "good!?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80B6")

    ChrTalk(
        0x102,
        (
            "#6P#00106FNo way... They weren't\x01",
            "serious...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8180")

    label("loc_80B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8104")

    ChrTalk(
        0x104,
        (
            "#6P#00306FGuh, and that's not even\x01",
            "their full power!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8180")

    label("loc_8104")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_814F")

    ChrTalk(
        0x109,
        (
            "#6P#10106FGuh... They were hiding\x01",
            "their strength!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8180")

    label("loc_814F")


    ChrTalk(
        0x105,
        (
            "#6P#10306FOh brother... We were\x01",
            "careless...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8180")


    ChrTalk(
        0x18,
        (
            "#11P*sigh*, I can't believe\x01",
            "this is all you've got...\x01",
            "I'm a little disappointed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PHmm, I was thinking of\x01",
            "another round, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell, I'd say their\x01",
            "battle teamwork has a\x01",
            "long way to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell, fine. Next, we'll\x01",
            "face your whole team.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_833E")
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Jump("loc_83BA")

    label("loc_833E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_836E")
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    Jump("loc_83BA")

    label("loc_836E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_839E")
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    Jump("loc_83BA")

    label("loc_839E")

    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    label("loc_83BA")

    Jump("loc_89DF")

    label("loc_83BF")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8438")
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_8544")

    label("loc_8438")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8498")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_8544")

    label("loc_8498")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84F8")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_8544")

    label("loc_84F8")

    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_8544")

    SetChrChipByIndex(0x18, 0x30)
    SetChrSubChip(0x18, 0x3)
    SetChrChipByIndex(0x19, 0x31)
    SetChrSubChip(0x19, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#00000F*pant*... Did we do it?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85EE")

    ChrTalk(
        0x102,
        (
            "#6P#00102FI would say yes... But\x01",
            "it appears our opponents\x01",
            "were holding back.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_86F7")

    label("loc_85EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8658")

    ChrTalk(
        0x104,
        (
            "#6P#00304FWell, it looks like that\x01",
            "wasn't their full power.\x01",
            "Isn't that right.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_86F7")

    label("loc_8658")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86B5")

    ChrTalk(
        0x109,
        (
            "#6P#10104FYes... But it appears\x01",
            "our opponents were\x01",
            "holding back.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_86F7")

    label("loc_86B5")


    ChrTalk(
        0x105,
        (
            "#6P#10304FYeah, although it\x01",
            "appears they weren't\x01",
            "serious.\x02",
        )
    )

    OP_57(0x0)
    OP_5A()
    CloseMessageWindow()

    label("loc_86F7")

    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_0D()

    ChrTalk(
        0x18,
        (
            "#11PHaha, I'm surprised. You\x01",
            "guys are pretty good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PYeah, you guys had\x01",
            "better teamwork than I\x01",
            "thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FAhaha... It seems we\x01",
            "have a ways to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PHaha. While it's true I\x01",
            "was holding back, it\x01",
            "wasn't that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell anyway, that was a\x01",
            "good showing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FUmm... Is this the end\x01",
            "of the training, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PHaha. Not so fast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PYeah. That wasn't enough\x01",
            "for you guys either,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FT-That's not true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PHaha, don't hold back\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PI know! Next, I want to\x01",
            "try us versus the\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_89DF")


    def lambda_89E4():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_89E4)
    Sleep(50)

    def lambda_89F4():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_89F4)
    Sleep(50)

    def lambda_8A04():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8A04)
    Sleep(50)

    def lambda_8A14():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8A14)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00005FA-All five of us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FWon't it be tough with\x01",
            "just you two against all\x01",
            "of us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PHaha, that's exactly why\x01",
            "they call this training!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x18, 0x29)
    SetChrSubChip(0x18, 0x0)
    OP_0D()

    ChrTalk(
        0x18,
        "#11P#4SHaaa!!\x02",
    )

    CloseMessageWindow()
    Sound(620, 0, 100, 0)
    Sound(832, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 9600, 0, -18150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(
        0x102,
        (
            "#6P#00105FAmazing... She's\x01",
            "radiating energy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FAn art from the east\x01",
            "called "qi", I believe.\x02\x03",
            "#00301FShe'll be trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PYou're well informed,\x01",
            "aren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PEolia!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#11PUnderstood!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_8C12():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8C12)
    Sleep(50)

    def lambda_8C22():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8C22)
    Sleep(50)

    def lambda_8C32():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8C32)
    Sleep(50)

    def lambda_8C42():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8C42)
    Sleep(50)
    BeginChrThread(0x19, 3, 0, 28)
    WaitChrThread(0x19, 3)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_32(0xFF, 0xFA, 0x0)
    OP_0D()

    ChrTalk(
        0x109,
        "#6P#10105FThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHaha, so everyone has\x01",
            "made a full recovery,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PNow we can fight without\x01",
            "holding anything back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell don't just stand\x01",
            "there! Get ready!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(10960, 1000)
    Fade(500)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x19, 0x2A)
    SetChrSubChip(0x19, 0x1)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(859, 0, 50, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#6P#00300F*sigh*, looks like we\x01",
            "have no choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FLloyd... Who's on\x01",
            "support?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FRight...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Switch Elie to Support\x01",       # 0
            "Switch Randy to Support\x01",      # 1
            "Switch Noｱl to Support\x01",      # 2
            "Switch Wazy to Support\x01",       # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EBC")
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_8F14")

    label("loc_8EBC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EE0")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_8F14")

    label("loc_8EE0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F04")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    Jump("loc_8F14")

    label("loc_8F04")

    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_8F14")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FAF")
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_90A3")

    label("loc_8FAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9007")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_90A3")

    label("loc_9007")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_905F")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_90A3")

    label("loc_905F")

    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_90A3")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9109")

    ChrTalk(
        0x101,
        (
            "#6P#00000FElie, handle the\x01",
            "support!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FAlright, roger!\x02",
    )

    CloseMessageWindow()
    Jump("loc_920E")

    label("loc_9109")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9163")

    ChrTalk(
        0x101,
        (
            "#6P#00000FRandy, you're on\x01",
            "support!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00300FAcknowledged!\x02",
    )

    CloseMessageWindow()
    Jump("loc_920E")

    label("loc_9163")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91C5")

    ChrTalk(
        0x101,
        (
            "#6P#00000FNoｱl, I'm leaving the\x01",
            "support to you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FYes, sir!\x02",
    )

    CloseMessageWindow()
    Jump("loc_920E")

    label("loc_91C5")


    ChrTalk(
        0x101,
        "#6P#00000FWazy, you're on support!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FHaha, understood!\x02",
    )

    CloseMessageWindow()

    label("loc_920E")


    ChrTalk(
        0x18,
        "#4S#11PHere we go!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_7B8", 0x30200011, 0x0, 0x100, 0xE, 0xFF)
    FadeToDark(0, 0, -1)
    StopEffect(0x0, 0x0)
    Return()

    # Function_27_7D28 end

    def Function_28_9247(): pass

    label("Function_28_9247")

    SetChrChipByIndex(0x19, 0x32)
    SetChrSubChip(0x19, 0x0)
    Sound(357, 0, 80, 0)
    PlayEffect(0x1, 0x1, 0x19, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0x19, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x19, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x1, 0x2)
    Sound(280, 0, 30, 0)
    PlayEffect(0x2, 0x2, 0x19, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x19, 0x3)
    Sleep(500)
    Sound(226, 0, 80, 0)
    PlayEffect(0x3, 0xFF, 0x101, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x102, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x104, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x109, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x105, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x19, 0x4)
    Sleep(2000)
    StopEffect(0x3, 0x2)
    Return()

    # Function_28_9247 end

    def Function_29_9413(): pass

    label("Function_29_9413")

    EventBegin(0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrPos(0x18, 9600, 0, -18150, 238)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrPos(0x19, 10650, 0, -19830, 238)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 1970, 0, -14340, 136)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 1700, 0, -12600, 136)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 490, 0, -13860, 136)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrPos(0x1A, 3250, 0, -13270, 150)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrPos(0x1B, 4380, 0, -9290, 136)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrPos(0x1C, 370, 0, -11950, 150)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 2550, 0, -10030, 150)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 5530, 0, -10320, 150)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrPos(0x1D, 4350, 0, -11650, 150)
    OP_68(7310, 1800, -22770, 0)
    MoveCamera(4, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13320, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B72")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x3)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_962D")
    SetChrPos(0x102, 8370, 0, -22800, 16)
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x102, 0x3)
    SetChrSubChip(0x104, 0x3)
    SetChrSubChip(0x109, 0x3)
    SetChrSubChip(0x105, 0x3)
    Jump("loc_9781")

    label("loc_962D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96A5")
    SetChrPos(0x104, 8370, 0, -22800, 16)
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x102, 0x3)
    SetChrSubChip(0x104, 0x3)
    SetChrSubChip(0x109, 0x3)
    SetChrSubChip(0x105, 0x3)
    Jump("loc_9781")

    label("loc_96A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_971D")
    SetChrPos(0x109, 8370, 0, -22800, 16)
    SetChrPos(0x102, 5920, 0, -22950, 55)
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x102, 0x3)
    SetChrSubChip(0x104, 0x3)
    SetChrSubChip(0x109, 0x3)
    SetChrSubChip(0x105, 0x3)
    Jump("loc_9781")

    label("loc_971D")

    SetChrPos(0x105, 8370, 0, -22800, 16)
    SetChrPos(0x102, 5920, 0, -22950, 55)
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x102, 0x3)
    SetChrSubChip(0x104, 0x3)
    SetChrSubChip(0x109, 0x3)
    SetChrSubChip(0x105, 0x3)

    label("loc_9781")

    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#00006F*pant*, *pant*,\x01",
            "*pant*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FWhy us... I can't\x01",
            "believe even all of us\x01",
            "were no match for them..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10108FWe lost...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11P*sigh*... And I thought\x01",
            "we wouldn't pull it off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PYes. We picked up the\x01",
            "win, somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PMaybe it's a difference\x01",
            "in experience?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x19, 3, 0, 28)
    WaitChrThread(0x19, 3)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#00002FAh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_32(0xFF, 0xFA, 0x0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#6P#00105FThe damage I took\x01",
            "earlier is completely\x01",
            "gone...\x02\x03",
            "#00102FThat's an amazing\x01",
            "recovery technique.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FBut you beat us, and now\x01",
            "you're healing us...\x02\x03",
            "#00306F*sigh*, I'm a failure of\x01",
            "a man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PSorry. Don't say\x01",
            "anything unnecessary,\x01",
            "ok?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00309FAh, I wouldn't dream of it!\x02\x03",
            "#00300FTo be healed by Eolia's warm\x01",
            "arts like this... I wouldn't\x01",
            "have it any other way!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FR-Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHaha. Where did your\x01",
            "pride from earlier go, I\x01",
            "wonder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106F*sigh*, seriously...\x01",
            "Have you no shame?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1B6")

    label("loc_9B72")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C03")
    SetChrPos(0x102, 8370, 0, -22800, 16)
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    Jump("loc_9D57")

    label("loc_9C03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C7B")
    SetChrPos(0x104, 8370, 0, -22800, 16)
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    Jump("loc_9D57")

    label("loc_9C7B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CF3")
    SetChrPos(0x109, 8370, 0, -22800, 16)
    SetChrPos(0x102, 5920, 0, -22950, 55)
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    Jump("loc_9D57")

    label("loc_9CF3")

    SetChrPos(0x105, 8370, 0, -22800, 16)
    SetChrPos(0x102, 5920, 0, -22950, 55)
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)

    label("loc_9D57")

    SetChrChipByIndex(0x18, 0x30)
    SetChrSubChip(0x18, 0x3)
    SetChrChipByIndex(0x19, 0x31)
    SetChrSubChip(0x19, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#00006F*pant, pant*... I-Is it\x01",
            "over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FYeah, somehow.\x02\x03",
            "#00302FBut they lasted this long\x01",
            "against all five of us.\x01",
            "They're really something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104FYes, truly... They didn't\x01",
            "let down their guard\x01",
            "until the bitter end.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    OP_0D()

    ChrTalk(
        0x18,
        "#11P*sigh*... No good, huh.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_0D()

    ChrTalk(
        0x19,
        (
            "#11PIt would have gone a\x01",
            "little better if we did\x01",
            "things differently, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PNo matter what excuses\x01",
            "we make, a loss is a\x01",
            "loss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PYou guys are really\x01",
            "strong. You're the\x01",
            "winners, this time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x19, 3, 0, 28)
    WaitChrThread(0x19, 3)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_32(0xFF, 0xFA, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#00005FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102FAmazing...\x02\x03",
            "I feel like all the\x01",
            "damage from before is\x01",
            "gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FTo be healed by Eolia twice\x01",
            "in one day... It's like\x01",
            "I've gone to heaven...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#11PThanks, Randy.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(859, 0, 50, 0)
    SetChrChipByIndex(0x19, 0x2A)
    SetChrSubChip(0x19, 0x1)
    OP_0D()

    ChrTalk(
        0x19,
        (
            "#11PI'll heal you a third\x01",
            "time, too. Up for\x01",
            "another round?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FUgh, give me a break!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHehe. I thought I might\x01",
            "really go to heaven during\x01",
            "the match this time, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FW-Wazy...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#6P#00106F*sigh*, seriously...\x01",
            "Have you no shame?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_0D()

    label("loc_A1B6")


    ChrTalk(
        0x18,
        (
            "#11PHaha, you guys are the\x01",
            "best. I never get tired\x01",
            "of watching you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00012FT-Thanks.\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(5620, 1500, -16800, 3000)
    MoveCamera(9, 27, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(18740, 3000)
    TurnDirection(0x18, 0x1D, 500)
    Sleep(300)
    OP_6F(0x79)

    ChrTalk(
        0x18,
        (
            "#12PAlright, this concludes\x01",
            "our duel.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x1D, 500)
    Sleep(300)

    ChrTalk(
        0x19,
        (
            "#12PYeah. Nothing further to\x01",
            "see here, everyone.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A2D8():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A2D8)
    Sleep(50)

    def lambda_A2E8():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A2E8)
    Sleep(50)

    def lambda_A2F8():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A2F8)
    Sleep(50)

    def lambda_A308():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A308)
    Sleep(50)

    def lambda_A318():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A318)
    Sleep(300)

    ChrTalk(
        0x1D,
        (
            "#5PHmm, then I suppose it's\x01",
            "time to end this little\x01",
            "event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#5PThere's work to do,\x01",
            "everyone. C'mon, break\x01",
            "time's over.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1D, 500)
    Sleep(300)

    ChrTalk(
        0x1B,
        "#11PGot it, Chief.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x1A,
        "#11PC'mon everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PMan, that was a great\x01",
            "fight.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(7360, 1500, -16890, 5000)
    MoveCamera(20, 25, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(16070, 5000)

    def lambda_A441():
        OP_95(0xFE, 8600, 0, -6460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A441)
    Sleep(50)

    def lambda_A45E():
        OP_95(0xFE, -2960, 0, -6890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_A45E)
    Sleep(50)

    def lambda_A47B():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_A47B)
    Sleep(1000)

    def lambda_A498():
        OP_95(0xFE, 1980, 0, -8140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_A498)
    Sleep(50)

    def lambda_A4B5():
        OP_95(0xFE, -470, 0, -11050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A4B5)
    Sleep(50)

    def lambda_A4D2():
        OP_95(0xFE, 280, 0, -10190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A4D2)
    Sleep(50)

    def lambda_A4EF():
        OP_95(0xFE, 1220, 0, -9620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A4EF)
    Sleep(1200)

    def lambda_A50C():
        OP_95(0xFE, 3110, 0, -9910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_A50C)
    WaitChrThread(0x9, 1)

    def lambda_A52A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A52A)
    WaitChrThread(0x8, 1)

    def lambda_A53B():
        OP_95(0xFE, -5810, 0, -6140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A53B)
    WaitChrThread(0xA, 1)

    def lambda_A559():
        OP_95(0xFE, -5250, 0, -4930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A559)
    WaitChrThread(0xB, 1)

    def lambda_A577():
        OP_95(0xFE, -4680, 0, -3550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A577)
    WaitChrThread(0x1A, 1)

    def lambda_A595():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_A595)
    WaitChrThread(0x1B, 1)

    def lambda_A5B3():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_A5B3)
    WaitChrThread(0x1A, 1)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_6F(0x1)

    ChrTalk(
        0x18,
        (
            "#12PYeah, and Chief, thanks\x01",
            "for letting us use this\x01",
            "place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12PWithout it, this\x01",
            "training wouldn't have\x01",
            "been possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#5PWell, it's not like we\x01",
            "didn't also benefit from\x01",
            "your training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#5PYou two are always helping\x01",
            "us out. It's really the\x01",
            "least we could do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#5PGoodbye, then.\x02",
    )

    CloseMessageWindow()

    def lambda_A722():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A722)
    Sleep(2000)
    Fade(500)
    OP_68(7310, 1800, -22770, 0)
    MoveCamera(4, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13320, 0)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#6P#00009FHaha, to think they'd be\x01",
            "so happy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x18, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00005FBut Ling... What was\x01",
            "this duel even for,\x01",
            "anyway?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A7FB():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A7FB)
    Sleep(50)

    def lambda_A80B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_A80B)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A864")

    def lambda_A827():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A827)
    Sleep(50)

    def lambda_A837():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A837)
    Sleep(50)

    def lambda_A847():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A847)
    Sleep(50)

    def lambda_A857():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A857)
    Jump("loc_A943")

    label("loc_A864")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8B5")

    def lambda_A878():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A878)
    Sleep(50)

    def lambda_A888():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A888)
    Sleep(50)

    def lambda_A898():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A898)
    Sleep(50)

    def lambda_A8A8():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A8A8)
    Jump("loc_A943")

    label("loc_A8B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A906")

    def lambda_A8C9():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A8C9)
    Sleep(50)

    def lambda_A8D9():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A8D9)
    Sleep(50)

    def lambda_A8E9():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A8E9)
    Sleep(50)

    def lambda_A8F9():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A8F9)
    Jump("loc_A943")

    label("loc_A906")


    def lambda_A90B():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A90B)
    Sleep(50)

    def lambda_A91B():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A91B)
    Sleep(50)

    def lambda_A92B():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A92B)
    Sleep(50)

    def lambda_A93B():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A93B)

    label("loc_A943")

    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AACF")
    OP_2C(0x75, 0x2)
    OP_29(0x75, 0x1, 0x5)

    ChrTalk(
        0x18,
        (
            "#11PYou guys are stronger\x01",
            "than I thought. I'm\x01",
            "surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PI guess you could say\x01",
            "it's the result of all\x01",
            "your training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PHaha, but we're not\x01",
            "interested in losing\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PWe'll have our revenge\x01",
            "someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, I'd love to do\x01",
            "this again if there's\x01",
            "another opportunity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FAnytime's ok if you ask\x01",
            "me㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC9F")

    label("loc_AACF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ABD0")
    OP_29(0x75, 0x1, 0x6)

    ChrTalk(
        0x18,
        (
            "#11PThat's right. If you had held out\x01",
            "a little longer, I would have\x01",
            "wanted additional training, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PHmm. I'm a little\x01",
            "unsatisfied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006FI-I'm ashamed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell, that's one result,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC9F")

    label("loc_ABD0")

    OP_2C(0x75, 0x1)
    OP_29(0x75, 0x1, 0x7)

    ChrTalk(
        0x18,
        (
            "#11PYeah. You all did your\x01",
            "best, and that's\x01",
            "training enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PThat's right. If there's\x01",
            "a chance, I'd like to do\x01",
            "this again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes. We'd love to take\x01",
            "up your offer again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC9F")

    OP_29(0x75, 0x1, 0x8)

    ChrTalk(
        0x18,
        (
            "#11PWhat we need to do now is\x01",
            "integrate what we've seen of\x01",
            "your various combat styles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PEspecially yours, Lloyd.\x01",
            "I'm very interested in\x01",
            "your tonfa techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PDo the police teach\x01",
            "those disabling\x01",
            "techniques?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, I'm impressed you\x01",
            "knew.\x02\x03",
            "#00005FBut, what's so\x01",
            "interesting about it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x18, 500)

    ChrTalk(
        0x104,
        (
            "#6P#00304FWell Tonfa are\x01",
            "originally from the\x01",
            "East, right?\x02\x03",
            "#00305FCan you use them too,\x01",
            "Ling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PYeah, a little bit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWhen I was learning martial arts, I got a\x01",
            "feel for Eastern weapons including the\x01",
            "chakram and the three-section staff, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PFrom that point of view, Lloyd,\x01",
            "your rotation techniques might\x01",
            "be a little old.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00005FOld you say... Are you\x01",
            "saying you can make my\x01",
            "technique stronger?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell in the end, it's\x01",
            "just a possibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PIf you like, I can\x01",
            "instruct you here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PWant to try it out?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00002FYou'll teach me? Of\x01",
            "course!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#11PYou're lucky, Lloyd~\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PIt's rare for Ling to be\x01",
            "teaching anyone\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x19, 500)

    ChrTalk(
        0x104,
        (
            "#6P#00309FI'd like you to teach me\x01",
            "a few things, Eolia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#11PHmm? Pass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FUgh, shot down again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FYou never learn, do ya\x01",
            "Randy.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00006FSorry everyone...\x02\x03",
            "#00000FYou heard the lady. Do\x01",
            "you mind if I take a\x01",
            "little more of our time?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B1F7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B1F7)
    Sleep(50)

    def lambda_B207():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B207)
    Sleep(50)

    def lambda_B217():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B217)
    Sleep(50)

    def lambda_B227():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B227)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#00100FNot at all. You won't get\x01",
            "many chances like this.\x01",
            "You should take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHaha, allow us to watch\x01",
            "and learn, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FDo your best, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00300FYeah, give it your all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00012FS-Sure...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PHaha. Well then, I guess\x01",
            "we'll get started.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00000FPlease do!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x24)
    SetChrChipByIndex(0x18, 0x29)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x18, 0x0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(7680, 1400, -21510, 0)
    MoveCamera(7, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12760, 0)
    SetChrPos(0x101, 7680, 0, -20400, 45)
    SetChrPos(0x102, 3320, 0, -22300, 45)
    SetChrPos(0x104, 4550, 0, -24210, 45)
    SetChrPos(0x109, 2930, 0, -19450, 90)
    SetChrPos(0x105, 7610, 0, -25120, 0)
    SetChrPos(0x18, 10880, 0, -16800, 225)
    SetChrPos(0x19, 12130, 0, -18530, 225)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    Sleep(3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 30)
    WaitChrThread(0x101, 3)
    TurnDirection(0x101, 0x18, 0)
    Sleep(1000)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00000FI-It felt good that\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PYeah, you pass.\x02",
    )

    CloseMessageWindow()
    OP_68(7310, 1400, -21350, 2000)
    MoveCamera(12, 19, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(14340, 2000)

    def lambda_B50C():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_B50C)
    Sleep(50)

    def lambda_B524():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B524)
    Sleep(50)

    def lambda_B53C():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_B53C)

    def lambda_B551():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B551)
    Sleep(50)

    def lambda_B569():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B569)
    Sleep(50)

    def lambda_B581():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B581)
    WaitChrThread(0x105, 1)
    OP_6F(0x10)

    ChrTalk(
        0x18,
        (
            "#11PAfter this, if you just use\x01",
            "it in actual combat, you'll\x01",
            "be able to make it your own.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0x2D, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#00000F*sigh*, thank\x01",
            "goodness... Thanks for\x01",
            "teaching me, Ling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FHaha, that's great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FNice work, Lloyd.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x101, 0xFA, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#00000FYeah, thanks.\x02\x03",
            "#00003FBut it's amazing... To\x01",
            "think this one move could\x01",
            "deliver so much power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PHaha. The spin move I just\x01",
            "taught you is commonly known\x01",
            "as a "Screw"-type attack.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x3A, 0x1F4)

    ChrTalk(
        0x18,
        (
            "#11PIt's a form of the Eight\x01",
            "Leaves, One Blade style\x01",
            "Arios uses, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PThe number of moves you can derive\x01",
            "from those fundamentals is as\x01",
            "countless as the stars in the sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PHe who masters the Screw and additionally\x01",
            "the ultimate Nothingness technique is\x01",
            "said to have reached a state of Reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FFrom screw to\x01",
            "nothingness and then to\x01",
            "reason, you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell, that's as much as\x01",
            "I understand, so that's\x01",
            "all for the lecture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PIn short, Reason is something like a\x01",
            "state ordinary people cannot reach\x01",
            "even if they spend their whole lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PIt is said that only a handful\x01",
            "of people on the continent\x01",
            "have ever reached that state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FJ-Just a handful...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FI've heard rumors about\x01",
            "that sort of thing in\x01",
            "before. It's pretty crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PYeah, it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell I obviously won't tell you\x01",
            "to go all the way to Reason, but\x01",
            "you should keep working on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FYes, understood!\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x18,
        (
            "#11PWhoops. Now that we're\x01",
            "through with that, it's\x01",
            "about time for our next job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PYeah. Both of us have to\x01",
            "hurry.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BBC6():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BBC6)
    Sleep(50)

    def lambda_BBD6():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BBD6)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00100FI thought you two were\x01",
            "rather busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PYeah. Especially now with\x01",
            "the trade conference, we\x01",
            "have a tight schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PMichel's shifts are\x01",
            "critical but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PNow he has them cut up\x01",
            "in blocks of just a few\x01",
            "minutes each.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FT-That's ridiculous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PHaha, I say that, but\x01",
            "there is some time set\x01",
            "aside for rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell then, we'll be\x01",
            "going. Keep up the good\x01",
            "work, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#11PLater! And thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes, thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16340, 3000)

    def lambda_BDDC():
        OP_95(0xFE, 17370, 0, -27500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_BDDC)
    Sleep(50)

    def lambda_BDF9():
        OP_95(0xFE, 17370, 0, -27500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_BDF9)

    def lambda_BE13():

        label("loc_BE13")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_BE13")

    QueueWorkItem2(0x101, 1, lambda_BE13)
    Sleep(50)

    def lambda_BE28():

        label("loc_BE28")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_BE28")

    QueueWorkItem2(0x102, 1, lambda_BE28)
    Sleep(50)

    def lambda_BE3D():

        label("loc_BE3D")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_BE3D")

    QueueWorkItem2(0x104, 1, lambda_BE3D)
    Sleep(50)

    def lambda_BE52():

        label("loc_BE52")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_BE52")

    QueueWorkItem2(0x109, 1, lambda_BE52)
    Sleep(50)

    def lambda_BE67():

        label("loc_BE67")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_BE67")

    QueueWorkItem2(0x105, 1, lambda_BE67)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd learned [Raging\x01",
            "Spin].\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd's craft [Accel\x01",
            "Rush] was strengthened\x01",
            "and became [Raging Spin].\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Attack power and range have\x01",
            "been improved and a suction\x01",
            "effect has been added.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddCraft(0x0, 0x9B)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Training with the\x01",
            "Bracers]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x9, 8410, 0, -12480, 17)
    SetChrPos(0x8, -6870, 0, 24790, 180)
    SetChrPos(0xA, -6110, 0, 23270, 315)
    SetChrPos(0xB, -7830, 0, 23860, 107)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_D7(0x28)
    SetChrPos(0x0, 8140, 0, -18700, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_69(0xFF, 0x0)
    OP_29(0x75, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_29_9413 end

    def Function_30_C0A3(): pass

    label("Function_30_C0A3")

    SetChrChipByIndex(0x101, 0x34)
    SetChrSubChip(0x101, 0x0)
    Sound(257, 0, 40, 0)
    Sound(252, 0, 80, 0)
    PlayEffect(0x4, 0x4, 0x101, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x101, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x101, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x101, 0, 0, 0, 0)
    StopEffect(0x4, 0x2)
    Sleep(300)
    StopEffect(0x6, 0x2)
    Sleep(300)
    SetChrChipByIndex(0x101, 0x33)
    SetChrSubChip(0x101, 0x0)
    SetChrChip(0x0, 0xFE, 0xF, 0x12C)
    Sound(253, 0, 100, 0)
    PlayEffect(0x5, 0x5, 0x101, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x101, 0, 0, 0, 0)
    SetScenarioFlags(0x1, 1)

    def lambda_C186():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x2EE, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C186)
    BeginChrThread(0x101, 0, 0, 31)
    WaitChrThread(0x101, 1)
    StopEffect(0x5, 0x2)
    ClearScenarioFlags(0x1, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_30_C0A3 end

    def Function_31_C1B7(): pass

    label("Function_31_C1B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_C1D3")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_31_C1B7")

    label("loc_C1D3")

    Return()

    # Function_31_C1B7 end

    def Function_32_C1D4(): pass

    label("Function_32_C1D4")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-3060, 1800, 24920, 0)
    MoveCamera(311, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16950, 0)
    SetChrPos(0x101, -2630, 0, 25660, 180)
    SetChrPos(0x102, -820, 0, 25800, 225)
    SetChrPos(0x103, -360, 0, 23860, 270)
    SetChrPos(0x104, -3500, 0, 24030, 90)
    SetChrPos(0x109, -2890, 0, 22410, 0)
    SetChrPos(0x105, -970, 0, 22610, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-3060, 700, 24920, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#00003FWe talked to everyone...\x01",
            "And we got some good\x01",
            "info.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FHis name is "Minneth"...\x01",
            "And he appeared to be\x01",
            "some kind of merchant.\x02\x03",
            "#00101FAnd unexpectedly, he's\x01",
            "good-natured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FPolite, kind to\x01",
            "children... That sort of\x01",
            "thing.\x02\x03",
            "#10304FHaha, he doesn't seem\x01",
            "all that suspicious at\x01",
            "this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FAt present, his\x01",
            "objective is unknown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FI really want to know\x01",
            "what he talked with the\x01",
            "chief's son about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah... I think it's\x01",
            "best to continue these\x01",
            "interviews.\x02\x03",
            "#00005FUmm...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)
    ClearChrFlags(0x9, 0x80)
    Fade(500)
    OP_68(8510, 1500, -12620, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    SetCameraDistance(15000, 3000)
    OP_63(0x9, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(3000)

    def lambda_C542():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C542)

    def lambda_C54F():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C54F)

    def lambda_C55C():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C55C)

    def lambda_C569():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C569)

    def lambda_C576():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C576)
    OP_6F(0x10)
    Sleep(1000)
    Fade(500)
    OP_68(-3060, 700, 24920, 0)
    MoveCamera(311, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16950, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00005FHim... It's possible\x01",
            "he's the one Derrick\x01",
            "went to the city with.\x02\x03",
            "#00003FLooks like he just got\x01",
            "back... Let's have a\x01",
            "little chat with him.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ModifyEventFlags(1, 0, 0x80)
    SetScenarioFlags(0x174, 4)
    OP_29(0x82, 0x1, 0x4)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -2850, 0, 24480, 135)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_32_C1D4 end

    def Function_33_C693(): pass

    label("Function_33_C693")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(7300, 1800, -12910, 0)
    MoveCamera(349, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13740, 0)
    SetChrPos(0x101, 6500, 0, -11950, 135)
    SetChrPos(0x102, 6210, 0, -13080, 90)
    SetChrPos(0x103, 5100, 0, -12190, 90)
    SetChrPos(0x104, 5560, 0, -10540, 135)
    SetChrPos(0x109, 6300, 0, -9770, 135)
    SetChrPos(0x105, 4430, 0, -10630, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        "Hm, hm, hmm...♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse me, are you\x01",
            "Elkin?\x02\x03",
            "I'd like to ask you a\x01",
            "little something...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        "What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Maybe you wanted to ask\x01",
            "me about this new orbal\x01",
            "truck?\x02",
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

    ChrTalk(
        0x101,
        "#00012FN-No... That's not it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Oh, no?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I got it cheap from\x01",
            "Minneth, and it's Verne\x01",
            "Co.'s latest model...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FHuh?\x02\x03",
            "#00101FYou mean Minneth, the\x01",
            "foreigner who's been coming\x01",
            "to the village recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FC-Cheap, you said... How\x01",
            "much was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Haha, it was...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "A mere 50,000 mira!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F50,000 mira!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FBuying a new truck for\x01",
            "such a low price... I'm\x01",
            "jealous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWhoa, there. This is no\x01",
            "time to be jealous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112FI-I suppose you're\x01",
            "right. Sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FAhem, anyway.\x02\x03",
            "#00200FSetting aside the fact that it's\x01",
            "new, it should cost around 500,000\x01",
            "mira. That's exceptionally cheap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FSo 90% off. That's\x01",
            "exceptionally generous\x01",
            "of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Our work has been going\x01",
            "smoothly. I guess that's\x01",
            "why.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It looks like his plan with\x01",
            "Derrick is progressing in\x01",
            "many ways...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, I'm no match for\x01",
            "Minneth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FPlan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "W-Whoops. Derrick\x01",
            "forbade me to speak of\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well anyway... I think\x01",
            "Minneth is trustworthy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see...\x02\x03",
            "#00005F...Huh? Come to think of\x01",
            "it... You're alone?\x02\x03",
            "Chief said you headed to\x01",
            "the city with Derrick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yeah, Derrick said he\x01",
            "was coming back by bus\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seemed like he had\x01",
            "business at the Entertainment\x01",
            "District hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think he had an\x01",
            "appointment to meet with\x01",
            "Minneth.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00101FHey Lloyd, this is...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FYeah. We might be able\x01",
            "to ask Minneth directly.\x02\x03",
            "#00001FIt's worth checking out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        (
            "#00000FThanks for your\x01",
            "cooperation. That was\x01",
            "helpful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You're very welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I don't really get it,\x01",
            "but good luck.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x174, 5)
    OP_29(0x82, 0x1, 0x5)
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, 6100, 0, -11400, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x0, 0x0)
    EventEnd(0x5)
    Return()

    # Function_33_C693 end

    def Function_34_D038(): pass

    label("Function_34_D038")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-1470, 1500, 10410, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    LoadChrToIndex("chr/ch24000.itc", 0x1E)
    LoadChrToIndex("chr/ch09300.itc", 0x1F)
    LoadChrToIndex("chr/ch22200.itc", 0x20)
    LoadChrToIndex("monster/ch82050.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch00150.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00350.itc", 0x25)
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch03050.itc", 0x27)
    LoadChrToIndex("chr/ch00051.itc", 0x28)
    LoadChrToIndex("chr/ch00151.itc", 0x29)
    LoadChrToIndex("chr/ch00251.itc", 0x2A)
    LoadChrToIndex("chr/ch00351.itc", 0x2B)
    LoadChrToIndex("chr/ch02951.itc", 0x2C)
    LoadChrToIndex("chr/ch03051.itc", 0x2D)
    LoadChrToIndex("monster/ch82051.itc", 0x2E)
    LoadChrToIndex("monster/ch82052.itc", 0x2F)
    SoundLoad(325)
    SoundLoad(948)
    SoundLoad(809)
    SoundLoad(805)
    SoundLoad(531)
    SoundLoad(494)
    SoundLoad(487)
    SoundLoad(486)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0x21)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0x21)
    SetChrSubChip(0x23, 0x0)
    SetChrChipByIndex(0x24, 0x21)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x101, -1320, 0, 11720, 90)
    SetChrPos(0x102, -2330, 0, 11520, 90)
    SetChrPos(0x103, -1550, 0, 10520, 90)
    SetChrPos(0x104, -2360, 60, 10120, 90)
    SetChrPos(0x109, -1360, 200, 9200, 90)
    SetChrPos(0x105, -2510, 260, 8760, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x103, 0x1000)
    SetChrFlags(0x104, 0x1000)
    SetChrFlags(0x109, 0x1000)
    SetChrFlags(0x105, 0x1000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0x20, 0x4)
    ClearChrFlags(0x21, 0x4)
    ClearChrFlags(0x22, 0x4)
    ClearChrFlags(0x23, 0x4)
    ClearChrFlags(0x24, 0x4)
    SetChrPos(0xC, 12240, 0, 17850, 180)
    SetChrPos(0xD, 12050, 0, 16440, 0)
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    StopBGM(0xBB8)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)
    OP_68(12280, 1500, 16050, 5000)
    OP_6F(0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#N#1P#00010FDamn... Did he already\x01",
            "finish the deal!?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)

    def lambda_D393():
        OP_95(0xFE, 3850, 0, 19250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D393)
    Sleep(100)

    def lambda_D3B0():
        OP_95(0xFE, 4270, 0, 18270, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_D3B0)
    OP_68(3150, 1500, 17270, 5000)
    MoveCamera(293, 25, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(13200, 5000)
    BeginChrThread(0x101, 3, 0, 35)
    Sleep(200)
    BeginChrThread(0x102, 3, 0, 36)
    Sleep(200)
    BeginChrThread(0x103, 3, 0, 37)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 38)
    Sleep(200)
    BeginChrThread(0x109, 3, 0, 39)
    Sleep(200)
    BeginChrThread(0x105, 3, 0, 40)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_D45B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D45B)
    Sleep(100)

    def lambda_D46B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_D46B)
    Sleep(300)

    ChrTalk(
        0xD,
        "Oh, you guys are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The Special Support\x01",
            "Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FDerrick, Minneth... Can I\x01",
            "ask what kind of deal you\x01",
            "two were conducting today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmph, my father put you\x01",
            "up to this again, did\x01",
            "he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Haha, well why not,\x01",
            "Derrick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Our plan will begin very\x01",
            "soon, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FWhat do you mean by\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "─Just now, I concluded\x01",
            "my final deal with\x01",
            "Derrick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It's decided that work will start on\x01",
            "expansion of the lotus fields I\x01",
            "borrowed from everyone in the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Then, my Quincy Company\x01",
            "will take over their\x01",
            "management.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FWha...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FSo you basically handed over\x01",
            "almost all of the village's\x01",
            "agriculture to this guy...\x02\x03",
            "#10300FDerrick, are you really ok\x01",
            "with this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In the end, I'm just\x01",
            "transferring management\x01",
            "of the fields to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Yes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "With my company harvesting the\x01",
            "honey, we'll be able to operate the\x01",
            "confectionery business efficiently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "For that to happen, it's most\x01",
            "efficient to temporarily transfer\x01",
            "the rights to my company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F(Crap, this guy is\x01",
            "cunning.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F(It seems the plan has\x01",
            "entered its final\x01",
            "stage.)\x02\x03",
            "#00208F(If that's the case,\x01",
            "then...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "Haha, farewell Derrick. I'll\x01",
            "be delivering this contract\x01",
            "to the main office.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "I think I'll have some good\x01",
            "news for you tomorrow, so\x01",
            "please look forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Alright. I'll be\x01",
            "waiting.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10101F(L-Lloyd!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Yeah... We can't let\x01",
            "him get away!)\x02\x03",
            "#00001F─Minneth, before that...\x01",
            "We have a few more\x01",
            "questions for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_DB39():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_DB39)
    Sleep(100)

    def lambda_DB49():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_DB49)
    Sleep(300)

    ChrTalk(
        0xD,
        "Oh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "What might you want to\x01",
            "know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYes, you see... It's\x01",
            "about certain suspicions\x01",
            "surrounding you.\x02\x03",
            "#00001FThat's right... I'm\x01",
            "talking about suspicions\x01",
            "of fraud.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        "Wha...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Don't be ridiculous!\x01",
            "That's rude to Minneth!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Haha... Calm down,\x01",
            "Derrick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Minneth?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You said you were the\x01",
            "Special Support Section,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Why on earth would you\x01",
            "suspect me of being a\x01",
            "crook...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I can ask for that much,\x01",
            "can't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FYes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "How interesting... In\x01",
            "that case, lay it on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But before that... Don't\x01",
            "forget that I am an\x01",
            "Imperial citizen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In the case you have no\x01",
            "clear basis for calling\x01",
            "me a crook...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In that case, though you are\x01",
            "an officer, I'll do whatever\x01",
            "I must to obtain restitution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F...That's fine with me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00101FLloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(It's all right. I'll handle\x01",
            "this.)\x02\x03",
            "(Based on our investigation\x01",
            "results, it's obvious Minneth\x01",
            "is committing fraud...)\x02\x03",
            "#00001F(We'll expose Minneth's true\x01",
            "colors, and open Derrick's\x01",
            "eyes!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Haha, very well... If\x01",
            "you're that prepared, I'll\x01",
            "answer anything you like.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    ChrTalk(
        0xD,
        (
            "...So, what will we be\x01",
            "discussing first?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F─First, your actions in\x01",
            "Crossbell...\x02\x03",
            "#00001FI want to ask you about\x01",
            "a contradiction between\x01",
            "those and what you said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "A contradiction, you\x01",
            "say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Ever since I came to Crossbell,\x01",
            "I've been working with Derrick\x01",
            "on furthering this plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The plan to launch the "Armorica\x01",
            "Honey Company" here in Armorica\x01",
            "as a Quincy subsidiary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "For a confectionery business using this village's\x01",
            "quality honey, if you apply my company's know-\x01",
            "how, I'm sure it will be profitable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I've already registered with the\x01",
            "city, and our business is practically\x01",
            "in the process of starting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "What is so contradictory\x01",
            "about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWell, about that plan you\x01",
            "just mentioned...\x02\x03",
            "#00001FAccording to information\x01",
            "we've obtained, there's a\x01",
            "clear, contradictory point.\x02\x03",
            "#00003FYes, that contradictory\x01",
            "point is...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat is the suspicious point\x01",
            "with Minneth's "plan"?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Confectionery know-how\x01",       # 0
            "Moving the plan forward\x01",      # 1
            "Plan's prospects\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E4CA")
    OP_2C(0x87, 0x1)

    ChrTalk(
        0x101,
        (
            "#00003FWhen we checked what you told\x01",
            "us against IBC records, I could\x01",
            "see a contradictory point.\x02\x03",
            "#00001FThat plan you mentioned...\x02\x03",
            "In actuality, it hasn't\x01",
            "progressed at all.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x6)
    Jump("loc_E865")

    label("loc_E4CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E61B")

    ChrTalk(
        0x101,
        (
            "#00003FThat plan you mentioned...\x02\x03",
            "#00001FActually, you don't know a\x01",
            "single thing about how to\x01",
            "make confectioneries, do you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Oh? An interesting\x01",
            "opinion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But, what proof do you\x01",
            "have of that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F...U-Umm, that's...\x02\x03",
            "#00006F(Damn... Now that he's\x01",
            "challenged it, I'll have\x01",
            "to think of a way out.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E75F")

    label("loc_E61B")


    ChrTalk(
        0x101,
        (
            "#00003FThat plan you\x01",
            "mentioned...\x02\x03",
            "#00001FActually, there's almost\x01",
            "no possibility of\x01",
            "success, isn't there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Oh? An interesting\x01",
            "opinion, but a bit rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "And what do you have that\x01",
            "makes you say that? I'm\x01",
            "talking evidence here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F...U-Umm, that's...\x02\x03",
            "#00006F(Damn... I should have\x01",
            "changed my approach.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E75F")


    ChrTalk(
        0x102,
        (
            "#00105FUmm... I might know.\x02\x03",
            "#00100FWe checked IBC's\x01",
            "information and noticed\x01",
            "an inconsistency.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FThat's right!\x02\x03",
            "#00001FMinneth... That "plan" you\x01",
            "mentioned... In actuality, it hasn't\x01",
            "progressed at all. Isn't that right?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x7)

    label("loc_E865")

    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "IBC? W-What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThink about it. If Quincy\x01",
            "Company was intended to further\x01",
            "its plans in Crossbell...\x02\x03",
            "#00001FIt would need a loan from IBC\x01",
            "for factory construction and\x01",
            "subsidiary development.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Yes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "For registering the company\x01",
            "with the city, I needed a\x01",
            "proper corporate account...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F─You "just" needed the\x01",
            "account. Isn't that\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThe "Armorica Honey Company"\x01",
            "account had the minimum balance\x01",
            "needed to open an account.\x02\x03",
            "Though we didn't learn the exact\x01",
            "amount, it was on the level of tens\x01",
            "of thousands of mira...\x02\x03",
            "#00001FDo you really think you can\x01",
            "construct a factory and operate a\x01",
            "business starting with that amount?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You looked into my IBC\x01",
            "account...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "M-Minneth... Does this\x01",
            "mean...!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "Oh, don't misunderstand.\x01",
            "I'm not admitting they\x01",
            "have a point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Just think of it as an\x01",
            "impoliteness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FB-But... There was\x01",
            "hardly any money in the\x01",
            "account!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "As an employee, I have\x01",
            "to be careful with how I\x01",
            "throw money around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I can't take out a loan\x01",
            "in the name of the Quincy\x01",
            "Company, you see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Of course, I'll think about discussing\x01",
            "a loan from IBC once I've secured\x01",
            "permission from the main office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F(...A skillful dodge.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(No... I can sense that\x01",
            "he's flustered.)\x02\x03",
            "#00001F(Let's press the attack\x01",
            "and shove more evidence\x01",
            "in his face!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The look on your face\x01",
            "says you have something\x01",
            "else to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FYes, of course.\x02\x03",
            "#00004FThat's not the only\x01",
            "suspicious point about\x01",
            "you, Minneth.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        "This late in the game!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "No, no, it's fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I want to put you at\x01",
            "ease too Derrick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FI'd like to ask about\x01",
            "your profile, Minneth.\x02\x03",
            "#00003FYou called yourself a\x01",
            "Quincy employee, but...\x02\x03",
            "#00013FI'm not mistaken about\x01",
            "that, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "Wait... What do you\x01",
            "mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You're saying Minneth\x01",
            "isn't with the Quincy\x01",
            "Company?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYes, that's what we\x01",
            "believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hehe... Hahaha! What do\x01",
            "you think you're\x01",
            "saying...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In that case, why don't I\x01",
            "show you my business card\x01",
            "or employee ID card?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...Even if you have\x01",
            "them, you may have\x01",
            "forged them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWe found some evidence\x01",
            "that trumps either of\x01",
            "those.\x02\x03",
            "#00000FIt was in nothing other\x01",
            "than a Quincy Company\x01",
            "pamphlet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "A pamphlet...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FIt was in milady's\x01",
            "room...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FWe have its main points\x01",
            "written in our detective\x01",
            "notebook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIt was ordered directly from the Quincy Company\x01",
            "main office. There shouldn't be any doubt as to\x01",
            "the authenticity of its information.\x02\x03",
            "#00003FAnd, there was a clear difference between the\x01",
            "material and what you told us yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "W-What I told you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FA point you told us that\x01",
            "is contrary to you being\x01",
            "an "employee". That is...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThe contradiction between Minneth's\x01",
            "statements yesterday and the materials?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Creation of subsidiary\x01",      # 0
            "Sales career\x01",                # 1
            "Dislike of sweets\x01",           # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA0F")
    OP_2C(0x87, 0x1)

    ChrTalk(
        0x101,
        (
            "#00003F─Yesterday, you told us\x01",
            "this.\x02\x03",
            ""Although I am an\x01",
            "employee, I actually\x01",
            "dislike sweet things"...\x02\x03",
            "#00013FDo you deny it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0xC)
    OP_64(0xD)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_F660():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F660)
    Sleep(50)

    def lambda_F670():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F670)
    Sleep(50)

    def lambda_F680():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F680)
    Sleep(50)

    def lambda_F690():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F690)
    Sleep(50)

    def lambda_F6A0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F6A0)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00105FL-Lloyd? Umm, I don't\x01",
            "get it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It is true that I don't\x01",
            "like them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Haha, but what about it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            ""A man with a dislike of sweets can't possibly\x01",
            "be a confectionery company employee"... Is\x01",
            "that what you are trying to say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FActually, that's exactly\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "What are you on about? You'll\x01",
            "bring shame on the whole of\x01",
            "the Crossbell Police!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F─This was written in the Quincy Company\x01",
            "pamphlet.\x02\x03",
            "#00003F"At Quincy, employees themselves sample\x01",
            "developmental products, and impartially\x01",
            "judge whether they are worthy of sale."\x02\x03",
            "#00013FThat's basically what it said.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F906():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F906)
    Sleep(50)

    def lambda_F916():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F916)
    Sleep(50)

    def lambda_F926():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F926)
    Sleep(50)

    def lambda_F936():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F936)
    Sleep(50)

    def lambda_F946():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F946)
    Sleep(300)

    ChrTalk(
        0xD,
        "!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "What do you...\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0xC,
        "#4S...Ah!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIt's unusual for someone like\x01",
            "Minneth who "dislikes sweets"\x01",
            "to be employed at Quincy.\x02\x03",
            "#00013FAm I wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x8)
    Jump("loc_1006F")

    label("loc_FA0F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA94")

    ChrTalk(
        0x101,
        (
            "#00003F─Minneth. Yesterday, you\x01",
            "said this.\x02\x03",
            "I will create a\x01",
            "subsidiary in Armorica,\x01",
            "regarding your plan...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB22")

    label("loc_FA94")


    ChrTalk(
        0x101,
        (
            "#00003F─Minneth. Yesterday, you said\x01",
            "this.\x02\x03",
            ""Thanks to my efforts in sales,\x01",
            "I have been recognized and\x01",
            "achieved my current position"...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB22")


    ChrTalk(
        0xD,
        (
            "...I did say that, but\x01",
            "what of it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00011F(D-Damn... No retorts\x01",
            "come to mind! Did I make\x01",
            "a mistake...?)\x02\x03",
            "#00012FU-Umm. That just now was\x01",
            "a mistake...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F─I see. I finally\x01",
            "thought of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh.\x02",
    )

    CloseMessageWindow()

    def lambda_FC1E():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FC1E)
    Sleep(50)

    def lambda_FC2E():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FC2E)
    Sleep(50)

    def lambda_FC3E():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FC3E)
    Sleep(50)

    def lambda_FC4E():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FC4E)
    Sleep(50)

    def lambda_FC5E():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FC5E)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10304F"Although I am an\x01",
            "employee, I actually\x01",
            "dislike sweet things"...\x02\x03",
            "#10302FYou said that yesterday,\x01",
            "Minneth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FW-Wazy? Umm, I don't\x01",
            "get...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It is true that I don't\x01",
            "like them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Haha, but what about it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            ""A man with a dislike of sweets can't possibly\x01",
            "be a confectionery company employee"... Is\x01",
            "that what you are trying to say?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FDD2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FDD2)
    Sleep(300)

    ChrTalk(
        0x103,
        "#00203F...Exactly.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10309FHaha. I looks like\x01",
            "you've realized it too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "W-What are these false\x01",
            "accusations!? You all should be\x01",
            "ashamed to call yourselves police─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F─In the Quincy Company pamphlet, this\x01",
            "was written.\x02\x03",
            ""At Quincy, employees themselves sample\x01",
            "developmental products, and impartially\x01",
            "judge whether they are worthy of sale."\x02\x03",
            "#10302FThat's basically what it said.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FF7B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FF7B)
    Sleep(50)

    def lambda_FF8B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FF8B)
    Sleep(50)

    def lambda_FF9B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FF9B)
    Sleep(50)

    def lambda_FFAB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FFAB)
    Sleep(300)

    ChrTalk(
        0xD,
        "!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "What do you...\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0xC,
        "#4S...Ah!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FIt's unusual for someone like\x01",
            "Minneth who "dislikes sweets"\x01",
            "to be employed at Quincy.\x02\x03",
            "#00201FAm I wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x9)

    label("loc_1006F")


    ChrTalk(
        0xD,
        (
            "...T-That is... You're\x01",
            "misremembering...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThat's not going to\x01",
            "work.\x02\x03",
            "#00001FYou just now admitted\x01",
            "that you don't like\x01",
            "sweets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Ugh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIf that's the case, then tell\x01",
            "us. Why did you pretend to be\x01",
            "a Quincy employee?\x02\x03",
            "#00001FI'll tell you why─ It was to\x01",
            "gain Derrick's trust─ for the\x01",
            "purpose of defrauding him.\x02\x03",
            "#00003FBased on the evidence we\x01",
            "have, that's the only\x01",
            "possibility I can think of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FAnd the confectionery\x01",
            "business making use of\x01",
            "Armorica's honey...\x02\x03",
            "#00101FThe Quincy Company name was a\x01",
            "convenient one for using that\x01",
            "idea to gain Derrick's trust.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "M-Minneth... What is the\x01",
            "meaning of this!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As I thought... You\x01",
            "tricked me!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "...He...Hehe... Derrick, my\x01",
            "friend. You mustn't be\x01",
            "deceived by these people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FW-What now?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "Haha... So what if it is\x01",
            "true?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "As for me coming to Armorica\x01",
            "and suggesting this "Honey\x01",
            "Company" plan...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If I concede that I had an\x01",
            "ulterior motive to come\x01",
            "here and deceive Derrick...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "What exactly are you\x01",
            "saying that objective\x01",
            "was!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If you've no proof of\x01",
            "that, you've no right to\x01",
            "call me a crook!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FProof of objective...\x01",
            "That's indeed a problem.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003FYour objective... I\x01",
            "actually do have an idea\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_10640():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10640)
    Sleep(50)

    def lambda_10650():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10650)
    Sleep(50)

    def lambda_10660():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10660)
    Sleep(50)

    def lambda_10670():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10670)
    Sleep(50)

    def lambda_10680():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10680)
    Sleep(50)

    def lambda_10690():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_10690)
    Sleep(300)

    ChrTalk(
        0xD,
        "W-What!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F(L-Lloyd, are you\x01",
            "sure!?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(I-I have no idea at\x01",
            "all...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(No... I've definitely got\x01",
            "this.)\x02\x03",
            "(Just before we came here, a\x01",
            ""certain someone" gave us a\x01",
            ""certain piece of evidence"...)\x02\x03",
            "#00001F(Yes, the final clue as\x01",
            "to Minneth's objective!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "What are you mumbling\x01",
            "about!? Out with it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThe true reason you\x01",
            "committed fraud in this\x01",
            "village. That is...\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10842")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A50")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThe goal of Minneth's\x01",
            "Armorica Village fraud?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Seizing land\x01",                # 0
            "Monopolize honey sales\x01",      # 1
            "Sell fake orbal cars\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10980")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1091B")
    OP_2C(0x87, 0x1)

    label("loc_1091B")


    ChrTalk(
        0x101,
        (
            "#00003FYour true objective\x01",
            "is...\x02\x03",
            "#00013FOwnership of the land of\x01",
            "Armorica Village itself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A4B")

    label("loc_10980")


    ChrTalk(
        0x101,
        (
            "#00006F(No... that's wrong.\x01",
            "It's too small of a\x01",
            "scale, isn't it.)\x02\x03",
            "#00001F(He spent all this time\x01",
            "preparing... His aim has\x01",
            "to be something bigger.)\x02\x03",
            "#00003F(Minneth's true\x01",
            "objective, that is...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_10A4B")

    Jump("loc_10842")

    label("loc_10A50")


    ChrTalk(
        0xD,
        "...W...ha...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FHarold, a trader we know, got some\x01",
            "information for us.\x02\x03",
            "#00000FMinneth, right after you arrived in\x01",
            "Crossbell, it seems you were looking\x01",
            "into land prices across the state.\x02\x03",
            "#00003FIf you were a Quincy Company employee\x01",
            "looking for new business opportunities,\x01",
            "that would not be necessary.\x02\x03",
            "So why, then? There's only one\x01",
            "possibility I can think of.\x02\x03",
            "#00013FIt was because your objective is to\x01",
            "steal this land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FR-Really!? I would never\x01",
            "have expected that.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00004FAnd that's not all.\x02\x03",
            "#00002FJust look all around us. Armorica\x01",
            "village is surrounded by nature's\x01",
            "beauty. It's a prime location.\x02\x03",
            "#00004FSuppose you transferred it to a third\x01",
            "party for managing villas... How much\x01",
            "do you think you could get for it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FThere are people who would\x01",
            "pay tens of millions for\x01",
            "something like this.\x02\x03",
            "#00101FI don't think the villagers\x01",
            "have any idea what they\x01",
            "agreed to, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FYeah. That's exactly why he was\x01",
            "able to make this whole scheme\x01",
            "work.\x02\x03",
            "#00001FIf we assume your objective was\x01",
            "the land itself, it would\x01",
            "explain all of your actions.\x02\x03",
            "You'd obtain the deed for the\x01",
            "vast lotus farms and the\x01",
            "private property...\x02\x03",
            "And under the pretext of\x01",
            "returning to the main office,\x01",
            "you'd disappear from Crossbell.\x02\x03",
            "#00003FThen, you'd sell the deeds\x01",
            "through the black market and\x01",
            "make a huge sum of mira...\x02\x03",
            "#00013FThat is your true objective.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10FD2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10FD2)
    Sleep(50)

    def lambda_10FE2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10FE2)
    Sleep(50)

    def lambda_10FF2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10FF2)
    Sleep(50)

    def lambda_11002():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11002)
    Sleep(50)

    def lambda_11012():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11012)
    Sleep(300)

    ChrTalk(
        0xD,
        "...Ugh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        "Minneth... No way...\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x1F, -1730, 390, 7230, 225)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)

    NpcTalk(
        0x1F,
        "Man's Voice",
        "─Lloyd!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_11132():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11132)
    Sleep(50)

    def lambda_11142():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11142)
    Sleep(50)

    def lambda_11152():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11152)
    Sleep(50)

    def lambda_11162():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11162)
    Sleep(50)

    def lambda_11172():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11172)
    Sleep(50)

    def lambda_11182():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11182)
    Sleep(50)

    def lambda_11192():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_11192)
    Sleep(50)

    def lambda_111A2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_111A2)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00000FThat voice...\x02",
    )

    CloseMessageWindow()
    OP_68(2080, 1500, 14610, 3000)
    MoveCamera(288, 29, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(16200, 3000)
    SetChrPos(0x1D, -1100, 450, 5260, 45)
    SetChrPos(0x1F, -2810, 450, 5340, 45)
    SetChrPos(0x1E, -2009, 420, 6880, 45)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    OP_0D()
    BeginChrThread(0x1E, 3, 0, 49)
    BeginChrThread(0x1F, 3, 0, 48)
    Sleep(200)
    BeginChrThread(0x1D, 3, 0, 47)
    WaitChrThread(0x1E, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)

    ChrTalk(
        0x1F,
        (
            "#03600FThank goodness, it seems\x01",
            "we made it in time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "Derrick...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Father, Harold...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FAnd you... I think\x01",
            "you're from that law\x01",
            "firm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "I'm Ian's assistant\x01",
            "Pete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Normally Mr. Grimwood would come, but\x01",
            "he had to leave for something related\x01",
            "to the constitution drafting process...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FProof... you said?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#03603FYes. Mr. Grimwood called\x01",
            "it "insurance" earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Please take a look at\x01",
            "this, everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Pete produced a single\x01",
            "photograph and everyone\x01",
            "examined it.\x02\x03",
            "A man with the air of a trader,\x01",
            "and with the same face as\x01",
            "Minneth, was depicted therein.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FT-The man that appears\x01",
            "in that photo is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "W-Why...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "How do you guys even\x01",
            "have that photo!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Mr. Grimwood got this photo a\x01",
            "long time ago from a reporter\x01",
            "he knew in the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "But the name on the\x01",
            "photograph isn't\x01",
            "Minneth... It's Littner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FLittner? I think we\x01",
            "heard that name\x01",
            "somewhere recently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F...Ah! That's it!\x02\x03",
            "#00101FIt's the name of the man who\x01",
            "stole that Imperial baron's\x01",
            "family land Ian told us about!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Ugh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FOh yeah, that was his\x01",
            "name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#03601FYes... I asked Lawyer Ian\x01",
            "about it once again and he\x01",
            "said there's no mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHmm... If that's the case, then\x01",
            "it seems a pretty interesting\x01",
            "truth is now revealed to us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10302FLloyd, you do the\x01",
            "honors.\x02\x03",
            "#10304FThe meaning of this\x01",
            "photo, I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F...Yeah, got it.\x02",
    )

    CloseMessageWindow()
    OP_68(2020, 1500, 16370, 3000)

    def lambda_11988():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11988)
    Sleep(50)

    def lambda_11998():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11998)
    Sleep(50)

    def lambda_119A8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_119A8)
    Sleep(50)

    def lambda_119B8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_119B8)
    Sleep(50)

    def lambda_119C8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_119C8)
    Sleep(50)

    def lambda_119D8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_119D8)
    Sleep(50)

    def lambda_119E8():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_119E8)
    Sleep(50)

    def lambda_119F8():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_119F8)
    Sleep(300)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00001FThe reason that "Littner" in the\x01",
            "photo and "Minneth" standing before\x01",
            "us have the same face, that is...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThe reason Littner and\x01",
            "Minneth have the same face?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Twins\x01",            # 0
            "Disguise\x01",         # 1
            "Same person\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BD3")
    OP_2C(0x87, 0x1)

    ChrTalk(
        0x101,
        (
            "#00003FMinneth and Littner are the\x01",
            "same person... That's the\x01",
            "only possibility.\x02\x03",
            "#00013FThe modus operandi is the\x01",
            "same, so he must be the same\x01",
            "person. It's that simple.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11E87")

    label("loc_11BD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C43")

    ChrTalk(
        0x101,
        (
            "#00003FMinneth and Littner are...\x01",
            "twin brothers. That's the\x01",
            "only thing I can think of.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C8D")

    label("loc_11C43")


    ChrTalk(
        0x101,
        (
            "#00003FMinneth is... Littner in\x01",
            "disguise. That's all I\x01",
            "can think of.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C8D")

    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1E, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0xC)
    OP_64(0xD)
    OP_64(0x1D)
    OP_64(0x1F)
    OP_64(0x1E)

    ChrTalk(
        0x105,
        (
            "#10306F...Aren't you reading\x01",
            "too much into it?\x02\x03",
            "#10302FNo matter how you slice\x01",
            "it, Minneth and Littner\x01",
            "are the same person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(I-It was difficult and I\x01",
            "overthought it, huh...)\x02\x03",
            "#00013FAhem. If that's true... Because\x01",
            "the modus operandi was similar,\x01",
            "they're the same person, huh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E87")


    ChrTalk(
        0x1D,
        (
            "Lawyer Ian said as\x01",
            "much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Most likely, he's proud\x01",
            "of his fraud technique.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FA "crook". That's what you\x01",
            "are, Minneth. A charge of\x01",
            "fraud is obvious.\x02\x03",
            "#00013FOn top of that, it's likely\x01",
            "you're the same person who\x01",
            "committed fraud in the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FNow that you've been caught,\x01",
            "I don't think it's anything\x01",
            "to be proud of, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FWe'd love to hear the\x01",
            "details... in the Police\x01",
            "HQ interrogation room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "...Ugh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Y... You... Youuuu...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I... I did everything\x01",
            "perfectly...\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0xD,
        "#4SThese... THESE BRATS!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "M-Minneth...\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1194)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    Sleep(2000)
    OP_64(0xD)

    ChrTalk(
        0xD,
        (
            "...Hmph, well I wouldn't\x01",
            "be so full of myself if\x01",
            "I were you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Sorry, but I haven't the\x01",
            "slightest intention of being\x01",
            "caught over something like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWhat!?\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xD,
        "─Come, monsters!\x02",
    )

    CloseMessageWindow()
    Sound(325, 0, 70, 0)
    WaitBGM()
    PlayBGM("ed7561", 0)
    Sleep(500)
    Fade(500)
    OP_68(10120, 700, -16210, 0)
    MoveCamera(326, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    SetChrChipByIndex(0x21, 0x2E)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0x2E)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0x2E)
    SetChrSubChip(0x23, 0x0)
    SetChrChipByIndex(0x24, 0x2E)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x21, 0x20)
    SetChrFlags(0x22, 0x20)
    SetChrFlags(0x23, 0x20)
    SetChrFlags(0x24, 0x20)
    SetChrPos(0x20, 11900, 200, -14590, 180)
    SetChrPos(0x21, 11900, 200, -14590, 180)
    SetChrPos(0x22, 11900, 200, -14590, 180)
    SetChrPos(0x23, 11900, 200, -14590, 180)
    SetChrPos(0x24, 11900, 200, -14590, 180)
    OP_A7(0x20, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x21, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x22, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    OP_0D()
    OP_71(0xD, 0xF1, 0x10E, 0x0, 0x0)
    Sound(454, 0, 100, 0)
    OP_79(0xD)
    Sound(948, 0, 100, 0)
    Sleep(1000)
    Sleep(500)
    Sound(809, 0, 100, 0)
    BeginChrThread(0x20, 3, 0, 52)
    Sleep(700)
    BeginChrThread(0x28, 1, 0, 63)
    Sound(809, 0, 100, 0)
    BeginChrThread(0x21, 3, 0, 53)
    Sleep(700)
    Sound(809, 0, 100, 0)
    BeginChrThread(0x22, 3, 0, 54)
    Sleep(700)
    Sound(809, 0, 100, 0)
    BeginChrThread(0x23, 3, 0, 55)
    Sleep(700)
    Sound(809, 0, 100, 0)
    BeginChrThread(0x24, 3, 0, 56)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x28, 0x1)
    OP_68(620, 700, 17350, 0)
    MoveCamera(294, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17910, 0)
    SetChrPos(0xC, 4960, 0, 19520, 270)
    SetChrPos(0xD, 5370, 0, 18730, 225)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0x21)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0x21)
    SetChrSubChip(0x23, 0x0)
    SetChrChipByIndex(0x24, 0x21)
    SetChrSubChip(0x24, 0x0)
    OP_52(0x20, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x20, -6100, 0, 14940, 135)
    SetChrPos(0x21, -3890, 0, 18870, 135)
    SetChrPos(0x22, -620, 0, 21820, 180)
    SetChrPos(0x23, 3420, 0, 20140, 225)
    SetChrPos(0x24, 3620, 0, 23850, 180)
    BeginChrThread(0x20, 3, 0, 50)
    BeginChrThread(0x21, 3, 0, 50)
    BeginChrThread(0x22, 3, 0, 50)
    BeginChrThread(0x23, 3, 0, 50)
    BeginChrThread(0x24, 3, 0, 50)
    SetChrPos(0x101, 1560, 10, 17040, 0)
    SetChrPos(0x102, 2380, 0, 16239, 0)
    SetChrPos(0x103, 1370, 10, 15400, 0)
    SetChrPos(0x104, 60, 10, 17000, 315)
    SetChrPos(0x109, -290, 0, 15050, 315)
    SetChrPos(0x105, -1310, 10, 16350, 315)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1E, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1E,
        "W-Whaaaa!?\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x23)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x27)
    SetChrSubChip(0x105, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00010FM-Monsters!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FAnd they look well-\x01",
            "trained!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F(This guy, could he\x01",
            "have...!?)\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0xC, 0xB4, 0x3E8, 0x3E8, 0x0)
    Sleep(100)

    ChrTalk(
        0xC,
        "...Ugh... Ah...\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x1D, 0x0, 0x1F4, 0x1388, 0x0)
    OP_93(0x1D, 0x5A, 0x0)
    Sleep(300)

    ChrTalk(
        0x1D,
        "D-Derrick!!\x02",
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x87, 0x3E8)
    Sleep(300)

    ChrTalk(
        0x1F,
        "#03605FC-Chief, it's dangerous!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107FYou... Do you have any\x01",
            "idea what you're doing!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hah, I know exactly what\x01",
            "I'm doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I never thought it would\x01",
            "come to this, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I never wanted to harm\x01",
            "Derrick or the\x01",
            "villagers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010FUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, out of my way,\x01",
            "please.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-480, 1500, 13490, 5000)
    MoveCamera(333, 20, 0, 5000)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2A)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2C)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2D)
    SetChrSubChip(0x105, 0x0)

    def lambda_12926():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12926)

    def lambda_12933():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12933)

    def lambda_12940():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12940)

    def lambda_1294D():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1294D)

    def lambda_1295A():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1295A)

    def lambda_12967():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12967)

    def lambda_12974():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12974)

    def lambda_12981():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_12981)

    def lambda_1298E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_1298E)
    WaitChrThread(0x105, 1)

    def lambda_1299F():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1299F)
    Sleep(50)

    def lambda_129B7():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_129B7)
    Sleep(50)

    def lambda_129CF():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_129CF)
    Sleep(50)

    def lambda_129E7():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_129E7)
    Sleep(50)

    def lambda_129FF():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_129FF)
    Sleep(50)

    def lambda_12A17():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12A17)
    Sleep(50)

    def lambda_12A2F():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12A2F)
    Sleep(50)

    def lambda_12A47():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_12A47)
    Sleep(50)

    def lambda_12A5F():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_12A5F)
    Sleep(50)

    def lambda_12A77():
        OP_95(0xFE, -1910, 0, 11190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_12A77)
    WaitChrThread(0x1F, 1)

    def lambda_12A95():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12A95)
    WaitChrThread(0x1D, 1)

    def lambda_12AA6():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_12AA6)
    WaitChrThread(0x1E, 1)

    def lambda_12AB7():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_12AB7)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x102, 1)
    SetChrChipByIndex(0x102, 0x23)
    SetChrSubChip(0x102, 0x0)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    WaitChrThread(0x109, 1)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    WaitChrThread(0x105, 1)
    SetChrChipByIndex(0x105, 0x27)
    SetChrSubChip(0x105, 0x0)
    Sleep(2000)
    OP_93(0x23, 0xB4, 0x0)

    def lambda_12B16():

        label("loc_12B16")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12B16")

    QueueWorkItem2(0x101, 1, lambda_12B16)
    Sleep(50)

    def lambda_12B2B():

        label("loc_12B2B")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12B2B")

    QueueWorkItem2(0x102, 1, lambda_12B2B)
    Sleep(50)

    def lambda_12B40():

        label("loc_12B40")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12B40")

    QueueWorkItem2(0x103, 1, lambda_12B40)
    Sleep(50)

    def lambda_12B55():

        label("loc_12B55")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12B55")

    QueueWorkItem2(0x104, 1, lambda_12B55)
    Sleep(50)

    def lambda_12B6A():

        label("loc_12B6A")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12B6A")

    QueueWorkItem2(0x105, 1, lambda_12B6A)
    Sleep(50)

    def lambda_12B7F():

        label("loc_12B7F")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12B7F")

    QueueWorkItem2(0xC, 1, lambda_12B7F)
    Sleep(50)

    def lambda_12B94():

        label("loc_12B94")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12B94")

    QueueWorkItem2(0x1D, 1, lambda_12B94)
    Sleep(50)

    def lambda_12BA9():

        label("loc_12BA9")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12BA9")

    QueueWorkItem2(0x1F, 1, lambda_12BA9)
    Sleep(50)

    def lambda_12BBE():

        label("loc_12BBE")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12BBE")

    QueueWorkItem2(0x1E, 1, lambda_12BBE)
    Sleep(100)

    def lambda_12BD3():

        label("loc_12BD3")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12BD3")

    QueueWorkItem2(0x109, 1, lambda_12BD3)
    Sleep(50)

    def lambda_12BE8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12BE8)
    WaitChrThread(0xD, 1)
    OP_6F(0x79)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1E, 0x1)
    OP_93(0x1F, 0xB4, 0x0)
    OP_93(0xD, 0x0, 0x1F4)
    Sleep(300)

    def lambda_12C34():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12C34)
    Sleep(50)

    def lambda_12C4C():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_12C4C)
    Sleep(50)

    def lambda_12C64():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_12C64)
    Sleep(500)

    ChrTalk(
        0xD,
        "Haha, farewell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I don't think we'll meet\x01",
            "again, though.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12CBE():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_12CBE)
    Sleep(3000)
    BeginChrThread(0x28, 1, 0, 63)
    BeginChrThread(0x20, 3, 0, 57)
    Sleep(500)
    BeginChrThread(0x21, 3, 0, 58)
    Sleep(500)
    BeginChrThread(0x22, 3, 0, 59)
    Sleep(1000)
    BeginChrThread(0x23, 3, 0, 60)
    Sleep(300)
    BeginChrThread(0x24, 3, 0, 61)
    Sleep(3000)
    Fade(500)
    OP_68(1180, 1500, 16250, 0)
    MoveCamera(337, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17060, 0)
    SetChrPos(0x1D, -170, 0, 13620, 45)
    SetChrPos(0x1F, -880, 0, 12290, 45)
    SetChrPos(0x1E, -2560, 0, 13500, 45)
    SetChrPos(0x101, -2100, 0, 15860, 180)
    SetChrPos(0x102, -1230, 0, 16850, 180)
    SetChrPos(0x103, -600, 0, 18000, 180)
    SetChrPos(0x104, -3190, 0, 16370, 180)
    SetChrPos(0x109, -2640, 0, 17580, 180)
    SetChrPos(0x105, -1830, 0, 18600, 180)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    OP_0D()
    EndChrThread(0x28, 0x1)

    ChrTalk(
        0x1D,
        "D-Derrick!!\x02",
    )

    CloseMessageWindow()

    def lambda_12E0E():
        OP_95(0xFE, 5240, 0, 18260, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_12E0E)
    Sleep(100)

    def lambda_12E2B():
        OP_95(0xFE, 3790, 0, 19250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_12E2B)
    Sleep(100)

    def lambda_12E48():
        OP_95(0xFE, 3560, 0, 17530, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12E48)
    WaitChrThread(0x1D, 1)

    def lambda_12E66():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_12E66)
    WaitChrThread(0x1F, 1)

    def lambda_12E77():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12E77)
    WaitChrThread(0x1E, 1)

    def lambda_12E88():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_12E88)
    WaitChrThread(0x1E, 1)

    ChrTalk(
        0xC,
        "Ooh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007FDamn, he got away!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201FLet's go...!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2A)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2C)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2D)
    SetChrSubChip(0x105, 0x0)

    def lambda_12F0D():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12F0D)
    Sleep(100)

    def lambda_12F2A():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12F2A)
    Sleep(100)

    def lambda_12F47():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12F47)
    Sleep(100)

    def lambda_12F64():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12F64)
    Sleep(100)

    def lambda_12F81():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_12F81)
    Sleep(100)

    def lambda_12F9E():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12F9E)
    Sleep(500)
    Fade(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_68(8750, 1500, -17760, 0)
    MoveCamera(345, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16149, 0)
    SetChrPos(0x101, -1860, 0, -3290, 180)
    SetChrPos(0x102, -3230, 0, -2980, 180)
    SetChrPos(0x103, -930, 0, -2320, 180)
    SetChrPos(0x104, -2380, 0, -1730, 180)
    SetChrPos(0x109, -1370, 0, -940, 180)
    SetChrPos(0x105, -3640, 0, -1220, 180)
    OP_0D()
    OP_71(0xD, 0x10F, 0x12C, 0x0, 0x0)
    Sound(454, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 41)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 42)
    Sleep(100)
    BeginChrThread(0x103, 3, 0, 43)
    Sleep(100)
    BeginChrThread(0x104, 3, 0, 44)
    Sleep(100)
    BeginChrThread(0x109, 3, 0, 45)
    Sleep(100)
    BeginChrThread(0x105, 3, 0, 46)
    Sleep(500)
    OP_71(0xD, 0x3C, 0x5A, 0x0, 0x0)
    Sound(494, 0, 100, 0)
    Sleep(500)
    OP_68(6900, 1500, -19750, 3000)
    MoveCamera(345, 24, 0, 3000)
    BeginChrThread(0x25, 1, 0, 62)
    OP_71(0xD, 0x79, 0xB4, 0x1, 0x20)
    Sleep(800)
    OP_6F(0x79)
    OP_68(6820, 1500, -15790, 3000)
    SetCameraDistance(15150, 3000)
    WaitChrThread(0x101, 3)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x102, 3)
    SetChrChipByIndex(0x102, 0x23)
    SetChrSubChip(0x102, 0x0)
    WaitChrThread(0x103, 3)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    WaitChrThread(0x104, 3)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    WaitChrThread(0x109, 3)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    WaitChrThread(0x105, 3)
    SetChrChipByIndex(0x105, 0x27)
    SetChrSubChip(0x105, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00105FAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FIt seems like he got\x01",
            "away, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FOoh... This is so aggravating!\x01",
            "To think we couldn't catch a\x01",
            "coward like that...!\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
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
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00006FThank goodness the\x01",
            "villagers weren't\x01",
            "harmed.\x02\x03",
            "#00000FI think that's all we\x01",
            "can do, for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FMan. I guess we'll need\x01",
            "to look forward to\x01",
            "capturing him next time.\x02\x03",
            "#10300FFor now, let's meet with\x01",
            "the chief and report the\x01",
            "details of this incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, good idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F(......)\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 2)
    NewScene("t0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_D038 end

    def Function_35_13395(): pass

    label("Function_35_13395")

    OP_97(0x101, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 2060, 0, 16660, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_35_13395 end

    def Function_36_133C9(): pass

    label("Function_36_133C9")

    OP_97(0x102, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 1450, 0, 17650, 2000, 0x0)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_36_133C9 end

    def Function_37_133FD(): pass

    label("Function_37_133FD")

    OP_97(0x103, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 2050, 0, 15310, 2000, 0x0)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_37_133FD end

    def Function_38_13431(): pass

    label("Function_38_13431")

    OP_97(0x104, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 420, 0, 18380, 2000, 0x0)
    OP_93(0x104, 0x5A, 0x1F4)
    Return()

    # Function_38_13431 end

    def Function_39_13465(): pass

    label("Function_39_13465")

    OP_97(0x109, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 870, 0, 16059, 2000, 0x0)
    OP_93(0x109, 0x5A, 0x1F4)
    Return()

    # Function_39_13465 end

    def Function_40_13499(): pass

    label("Function_40_13499")

    OP_97(0x105, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 170, 0, 17060, 2000, 0x0)
    OP_93(0x105, 0x5A, 0x1F4)
    Return()

    # Function_40_13499 end

    def Function_41_134CD(): pass

    label("Function_41_134CD")

    OP_97(0x101, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 7230, 0, -14950, 3500, 0x0)
    OP_93(0x101, 0x87, 0x1F4)
    Return()

    # Function_41_134CD end

    def Function_42_13501(): pass

    label("Function_42_13501")

    OP_97(0x102, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 5740, 0, -15440, 3500, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_42_13501 end

    def Function_43_13535(): pass

    label("Function_43_13535")

    OP_97(0x103, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 7140, 0, -13390, 3500, 0x0)
    OP_93(0x103, 0x87, 0x1F4)
    Return()

    # Function_43_13535 end

    def Function_44_13569(): pass

    label("Function_44_13569")

    OP_97(0x104, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 5860, 0, -14270, 3500, 0x0)
    OP_93(0x104, 0x87, 0x1F4)
    Return()

    # Function_44_13569 end

    def Function_45_1359D(): pass

    label("Function_45_1359D")

    OP_97(0x109, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 5870, 0, -12970, 3500, 0x0)
    OP_93(0x109, 0x87, 0x1F4)
    Return()

    # Function_45_1359D end

    def Function_46_135D1(): pass

    label("Function_46_135D1")

    OP_97(0x105, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 4340, 0, -14470, 3500, 0x0)
    OP_93(0x105, 0x87, 0x1F4)
    Return()

    # Function_46_135D1 end

    def Function_47_13605(): pass

    label("Function_47_13605")

    OP_97(0x1D, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x1D, 1)
    OP_95(0x1D, -1530, 0, 11680, 2000, 0x0)
    OP_93(0x1D, 0x2D, 0x1F4)
    Return()

    # Function_47_13605 end

    def Function_48_13639(): pass

    label("Function_48_13639")

    OP_97(0x1F, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x1F, 1)
    OP_95(0x1F, -2380, 0, 13280, 2000, 0x0)
    OP_93(0x1F, 0x2D, 0x1F4)
    Return()

    # Function_48_13639 end

    def Function_49_1366D(): pass

    label("Function_49_1366D")

    OP_97(0x1E, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x1E, 1)
    OP_95(0x1E, -720, 0, 12970, 2000, 0x0)
    OP_93(0x1E, 0x2D, 0x1F4)
    Return()

    # Function_49_1366D end

    def Function_50_136A1(): pass

    label("Function_50_136A1")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_136AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_136C8")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("loc_136AC")

    label("loc_136C8")

    Return()

    # Function_50_136A1 end

    def Function_51_136C9(): pass

    label("Function_51_136C9")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_136D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_136EB")
    OP_A0(0xFE, 1200, 0x0, 0x5)
    Jump("loc_136D4")

    label("loc_136EB")

    Return()

    # Function_51_136C9 end

    def Function_52_136EC(): pass

    label("Function_52_136EC")


    def lambda_136F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_136F1)

    def lambda_13702():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_13702)
    WaitChrThread(0x20, 1)
    BeginChrThread(0x20, 0, 0, 51)
    OP_95(0x20, 4710, 0, -15670, 6000, 0x0)
    OP_95(0x20, -2120, 0, -1730, 6000, 0x0)
    OP_95(0x20, -2120, 0, 14270, 6000, 0x0)
    Return()

    # Function_52_136EC end

    def Function_53_13761(): pass

    label("Function_53_13761")


    def lambda_13766():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_13766)

    def lambda_13777():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_13777)
    WaitChrThread(0x21, 1)
    BeginChrThread(0x21, 0, 0, 51)
    OP_95(0x21, 6990, 0, -13880, 7000, 0x0)
    OP_95(0x21, 830, 0, -10410, 7000, 0x0)
    OP_95(0x21, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x21, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_53_13761 end

    def Function_54_137EA(): pass

    label("Function_54_137EA")


    def lambda_137EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_137EF)

    def lambda_13800():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_13800)
    WaitChrThread(0x22, 1)
    BeginChrThread(0x22, 0, 0, 51)
    OP_95(0x22, 4710, 0, -15670, 7000, 0x0)
    OP_95(0x22, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x22, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_54_137EA end

    def Function_55_1385F(): pass

    label("Function_55_1385F")


    def lambda_13864():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_13864)

    def lambda_13875():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_13875)
    WaitChrThread(0x23, 1)
    BeginChrThread(0x23, 0, 0, 51)
    OP_95(0x23, 6990, 0, -13880, 7000, 0x0)
    OP_95(0x23, 830, 0, -10410, 7000, 0x0)
    OP_95(0x23, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x23, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_55_1385F end

    def Function_56_138E8(): pass

    label("Function_56_138E8")


    def lambda_138ED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_138ED)

    def lambda_138FE():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_138FE)
    WaitChrThread(0x24, 1)
    BeginChrThread(0x24, 0, 0, 51)
    OP_95(0x24, 4710, 0, -15670, 7000, 0x0)
    OP_95(0x24, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x24, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_56_138E8 end

    def Function_57_1395D(): pass

    label("Function_57_1395D")

    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    BeginChrThread(0x20, 0, 0, 51)
    OP_95(0xFE, -6100, 0, 14940, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_57_1395D end

    def Function_58_139A8(): pass

    label("Function_58_139A8")

    SetChrChipByIndex(0x21, 0x2E)
    SetChrSubChip(0x21, 0x0)
    BeginChrThread(0x21, 0, 0, 51)
    OP_95(0xFE, -6100, 0, 14940, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_58_139A8 end

    def Function_59_139F3(): pass

    label("Function_59_139F3")

    SetChrChipByIndex(0x22, 0x2E)
    SetChrSubChip(0x22, 0x0)
    BeginChrThread(0x22, 0, 0, 51)
    OP_95(0xFE, -6100, 0, 14940, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_59_139F3 end

    def Function_60_13A3E(): pass

    label("Function_60_13A3E")

    SetChrChipByIndex(0x23, 0x2E)
    SetChrSubChip(0x23, 0x0)
    BeginChrThread(0x23, 0, 0, 51)
    OP_95(0xFE, 3670, 0, 15480, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_60_13A3E end

    def Function_61_13A89(): pass

    label("Function_61_13A89")

    SetChrChipByIndex(0x24, 0x2E)
    SetChrSubChip(0x24, 0x0)
    BeginChrThread(0x24, 0, 0, 51)
    OP_95(0xFE, 3670, 0, 15480, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_61_13A89 end

    def Function_62_13AD4(): pass

    label("Function_62_13AD4")

    OP_9E(0xFE, 0x316, 0xFFFFE642, 0xEA60, 0x1B58, 0x4)
    Sound(487, 0, 100, 0)
    Sleep(500)
    Sleep(200)
    Sound(486, 0, 100, 0)
    OP_9F(0x0, 0x25)
    OP_9F(0x1, 12190, 0, -23580)
    OP_9F(0x1, 16760, 0, -26550)
    OP_9F(0x1, 23260, 0, -32810)
    OP_9F(0x2, 0x25, 9000, 0x6)
    Return()

    # Function_62_13AD4 end

    def Function_63_13B33(): pass

    label("Function_63_13B33")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13B4C")
    Sound(845, 0, 80, 0)
    Sleep(350)
    Jump("Function_63_13B33")

    label("loc_13B4C")

    Return()

    # Function_63_13B33 end

    def Function_64_13B4D(): pass

    label("Function_64_13B4D")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(1720, 1500, -10600, 0)
    MoveCamera(344, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21210, 0)
    SetChrPos(0x101, 720, 0, -10290, 325)
    SetChrPos(0x102, 1980, 0, -9830, 325)
    SetChrPos(0x103, 740, 0, -11540, 325)
    SetChrPos(0x104, 2190, 0, -11320, 325)
    SetChrPos(0x109, 2210, 0, -12700, 325)
    SetChrPos(0x105, 3580, 0, -11240, 325)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_13C07():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13C07)
    Sleep(50)

    def lambda_13C1F():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13C1F)
    Sleep(50)

    def lambda_13C37():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13C37)
    Sleep(50)

    def lambda_13C4F():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13C4F)
    Sleep(50)

    def lambda_13C67():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13C67)
    Sleep(50)

    def lambda_13C7F():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_13C7F)
    OP_68(1050, 1500, -9540, 3000)
    SetCameraDistance(17450, 3000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_13CB8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13CB8)
    WaitChrThread(0x101, 1)

    def lambda_13CC9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13CC9)
    WaitChrThread(0x102, 1)

    def lambda_13CDA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13CDA)
    WaitChrThread(0x103, 1)

    def lambda_13CEB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13CEB)
    WaitChrThread(0x104, 1)

    def lambda_13CFC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13CFC)
    WaitChrThread(0x109, 1)

    def lambda_13D0D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_13D0D)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00000FWe arrived at Armorica\x01",
            "Village, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FWhere in this village\x01",
            "could Geval be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FAnyway, let's try\x01",
            "searching suspicious\x01",
            "places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt might be a good idea\x01",
            "to speak with the\x01",
            "villagers, too.\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x19D, 2)
    ModifyEventFlags(0, 2, 0x80)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -1810, 0, -3210, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_29(0x90, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_64_13B4D end

    def Function_65_13E4A(): pass

    label("Function_65_13E4A")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13F6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_END)), "loc_13EE5")

    ChrTalk(
        0x101,
        (
            "#00000F...Let's try speaking\x01",
            "with the chief. He may\x01",
            "know something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13F67")

    label("loc_13EE5")


    ChrTalk(
        0x101,
        (
            "#00003FThere's the presence of\x01",
            "someone inside...\x02\x03",
            "#00000FAnyway, let's keep asking\x01",
            "around. The villagers may\x01",
            "know something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F67")

    TalkEnd(0xFF)
    Return()

    label("loc_13F6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F7D")
    TalkEnd(0xFF)
    Jump("loc_14328")

    label("loc_13F7D")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(15660, 5000, 47180, 0)
    MoveCamera(313, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 15740, 3500, 47460, 0)
    SetChrPos(0x102, 15140, 3500, 46070, 0)
    SetChrPos(0x103, 16540, 3500, 46260, 0)
    SetChrPos(0x104, 15130, 3500, 44850, 0)
    SetChrPos(0x109, 16950, 3500, 45060, 0)
    SetChrPos(0x105, 16149, 3500, 43850, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#00105FLloyd, is this place...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI think it was locked\x01",
            "when we came here\x01",
            "before...?\x02",
        )
    )

    CloseMessageWindow()
    Sound(812, 0, 80, 0)
    Sleep(400)
    Sound(811, 0, 50, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105FThat sound just now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F...There's someone\x01",
            "inside. For sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FYes, I think so too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha. It's plainly\x01",
            "suspicious.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_END)), "loc_1427B")

    ChrTalk(
        0x101,
        "#00003FCould it be...\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00001F...Let's try speaking\x01",
            "with the chief. He may\x01",
            "know something.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x6)
    Jump("loc_142EF")

    label("loc_1427B")

    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F...Anyway, for now,\x01",
            "let's keep collecting\x01",
            "evidence.\x02\x03",
            "#00001FThe villagers may know\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142EF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x19B, 1)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 16100, 3500, 45380, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_14328")

    Return()

    # Function_65_13E4A end

    def Function_66_14329(): pass

    label("Function_66_14329")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(16250, 5000, 46160, 0)
    MoveCamera(318, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15440, 0)
    LoadChrToIndex("chr/ch24000.itc", 0x1E)
    SetChrChipByIndex(0x1D, 0x1E)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 15770, 3500, 47280, 0)
    SetChrPos(0x101, 16040, 3500, 45180, 0)
    SetChrPos(0x102, 15140, 3500, 44440, 0)
    SetChrPos(0x103, 17030, 3500, 44510, 0)
    SetChrPos(0x104, 16260, 3500, 43520, 0)
    SetChrPos(0x109, 15070, 3500, 42860, 0)
    SetChrPos(0x105, 17520, 3500, 43210, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1D,
        (
            "...This is Chief Tolta.\x01",
            "May I have a moment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "There are some people\x01",
            "here who want to speak\x01",
            "with you.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(330, 20, -1, -1)
    SetChrName("Middle-Aged Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "!!\x02\x03",
            "I-I asked you to go\x01",
            "away, didn't I?\x02\x03",
            "I realize I'm intruding,\x01",
            "but I just want to be\x01",
            "left alone for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "...Please relax.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "The ones who came to see\x01",
            "you are your son and his\x01",
            "wife.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Middle-Aged Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "W-What are you saying!?\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FGeval, can you hear me?\x02\x03",
            "#00000FWe are the Crossbell\x01",
            "Police, Special Support\x01",
            "Section.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Middle-Aged Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "P-Police!?\x02\x03",
            "W-What do you want with\x01",
            "me!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Sorry for showing up\x01",
            "all of a sudden.\x02\x03",
            "#00000FWe accepted a request\x01",
            "from Alm and Aerie, and\x01",
            "were looking for you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Middle-Aged Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wha...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FBut, you're not under arrest. We\x01",
            "don't have that authority.\x02\x03",
            "#00004FIf you won't see them no matter\x01",
            "what, we'll explain things to Alm\x01",
            "and Aerie and abandon the request.\x02\x03",
            "#00000FWhat do you say? Will you speak\x01",
            "with them?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Middle-Aged Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "............\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00100FIt looks like it's open.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah... Then, let's go\x01",
            "inside.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x5A, 0x1F4)
    OP_9B(0x1, 0x1D, 0xB4, 0x3E8, 0x7D0, 0x0)
    OP_95(0x101, 15770, 3500, 47280, 2000, 0x0)
    Sleep(500)
    ClearMapObjFlags(0x3, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x3, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x1)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 67)
    BeginChrThread(0x102, 3, 0, 68)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 69)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 70)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 71)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 72)
    WaitChrThread(0x105, 3)
    BeginChrThread(0x1D, 3, 0, 73)
    WaitChrThread(0x1D, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("t0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_66_14329 end

    def Function_67_14971(): pass

    label("Function_67_14971")

    OP_93(0x101, 0x0, 0x0)

    def lambda_1497D():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1497D)

    def lambda_14992():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14992)
    Return()

    # Function_67_14971 end

    def Function_68_1499F(): pass

    label("Function_68_1499F")

    OP_95(0x102, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x102, 0x0, 0x0)

    def lambda_149BF():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_149BF)

    def lambda_149D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_149D4)
    Return()

    # Function_68_1499F end

    def Function_69_149E1(): pass

    label("Function_69_149E1")

    OP_95(0x103, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x103, 0x0, 0x0)

    def lambda_14A01():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14A01)

    def lambda_14A16():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_14A16)
    Return()

    # Function_69_149E1 end

    def Function_70_14A23(): pass

    label("Function_70_14A23")

    OP_95(0x104, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x104, 0x0, 0x0)

    def lambda_14A43():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14A43)

    def lambda_14A58():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_14A58)
    Return()

    # Function_70_14A23 end

    def Function_71_14A65(): pass

    label("Function_71_14A65")

    OP_95(0x109, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x109, 0x0, 0x0)

    def lambda_14A85():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14A85)

    def lambda_14A9A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_14A9A)
    Return()

    # Function_71_14A65 end

    def Function_72_14AA7(): pass

    label("Function_72_14AA7")

    OP_95(0x105, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x105, 0x0, 0x0)

    def lambda_14AC7():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_14AC7)

    def lambda_14ADC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_14ADC)
    Return()

    # Function_72_14AA7 end

    def Function_73_14AE9(): pass

    label("Function_73_14AE9")

    OP_95(0x1D, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x1D, 0x0, 0x0)

    def lambda_14B09():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_14B09)

    def lambda_14B1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_14B1E)
    Return()

    # Function_73_14AE9 end

    def Function_74_14B2B(): pass

    label("Function_74_14B2B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(14750, 5000, 44740, 0)
    MoveCamera(315, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17430, 0)
    LoadChrToIndex("chr/ch24000.itc", 0x1E)
    SetChrChipByIndex(0x1D, 0x1E)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 13580, 3500, 43350, 0)
    SetChrChipByIndex(0x26, 0xA)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 13850, 3500, 46310, 135)
    SetChrChipByIndex(0x27, 0xB)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 13050, 3500, 45510, 135)
    OP_4B(0x26, 0xFF)
    OP_4B(0x27, 0xFF)
    SetChrPos(0x101, 15510, 3500, 44690, 315)
    SetChrPos(0x102, 14840, 3500, 43910, 315)
    SetChrPos(0x103, 16500, 3500, 44690, 315)
    SetChrPos(0x104, 15040, 3500, 42890, 315)
    SetChrPos(0x109, 15980, 3500, 42470, 315)
    SetChrPos(0x105, 16900, 3500, 43550, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetCameraDistance(15430, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x26,
        "My dad is in there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes. There's no mistake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHe even promised he'd\x01",
            "see both of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        "Oh, thank you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "I honestly don't know why he's\x01",
            "hiding in a place like this,\x01",
            "but... You guys really did it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    ChrTalk(
        0x27,
        (
            "Haha, that's great, Alm.\x01",
            "I'll finally get to meet\x01",
            "my father-in-law!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "We'll need to apologize\x01",
            "for not inviting him to\x01",
            "our wedding, too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    ChrTalk(
        0x26,
        (
            "Oh, Aerie... Why is your\x01",
            "heart so pure?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Your heart is clear as\x01",
            "fresh snow. That's why I\x01",
            "love you so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "Oh Alm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F#4SGet in the shed.\x02",
    )

    CloseMessageWindow()

    def lambda_14E90():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_14E90)
    Sleep(50)

    def lambda_14EA0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_14EA0)
    Sleep(300)

    ChrTalk(
        0x26,
        "Huh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "Uhuhu, sorry about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "You too, Almin. S-o-r-\x01",
            "r-y.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x27,
        "Baby",
        "Baa.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "Well done!\x02",
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
    OP_63(0x1D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10106F(T-This is tiring...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "A-Anyway, Geval's\x01",
            "waiting for you inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha... Please take as\x01",
            "long as you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Sure, we'll do just\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    ChrTalk(
        0x26,
        "Let's go Aerie.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    ChrTalk(
        0x27,
        "Ok, Alm.\x02",
    )

    CloseMessageWindow()

    def lambda_150A0():
        OP_95(0xFE, 15770, 3500, 47280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_150A0)
    Sleep(300)

    def lambda_150BD():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_150BD)

    def lambda_150D2():

        label("loc_150D2")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_150D2")

    QueueWorkItem2(0x101, 1, lambda_150D2)
    Sleep(50)

    def lambda_150E7():

        label("loc_150E7")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_150E7")

    QueueWorkItem2(0x102, 1, lambda_150E7)
    Sleep(50)

    def lambda_150FC():

        label("loc_150FC")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_150FC")

    QueueWorkItem2(0x103, 1, lambda_150FC)
    Sleep(50)

    def lambda_15111():

        label("loc_15111")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_15111")

    QueueWorkItem2(0x104, 1, lambda_15111)
    Sleep(50)

    def lambda_15126():

        label("loc_15126")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_15126")

    QueueWorkItem2(0x109, 1, lambda_15126)
    Sleep(50)

    def lambda_1513B():

        label("loc_1513B")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_1513B")

    QueueWorkItem2(0x105, 1, lambda_1513B)
    Sleep(50)

    def lambda_15150():

        label("loc_15150")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_15150")

    QueueWorkItem2(0x1D, 1, lambda_15150)
    WaitChrThread(0x26, 1)
    OP_93(0x26, 0x0, 0x1F4)
    Sleep(500)
    ClearMapObjFlags(0x3, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x3, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x1)
    Sleep(500)
    BeginChrThread(0x26, 3, 0, 75)
    Sleep(500)
    BeginChrThread(0x27, 3, 0, 75)
    Sleep(500)
    WaitChrThread(0x27, 3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x1D, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 4)
    NewScene("t0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_74_14B2B end

    def Function_75_151E2(): pass

    label("Function_75_151E2")

    OP_95(0xFE, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x0)

    def lambda_15202():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_15202)

    def lambda_15217():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_15217)
    Return()

    # Function_75_151E2 end

    def Function_76_15224(): pass

    label("Function_76_15224")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(14750, 5000, 44740, 0)
    MoveCamera(315, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15430, 0)
    LoadChrToIndex("chr/ch24000.itc", 0x1E)
    SetChrChipByIndex(0x1D, 0x1E)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 13580, 3500, 43350, 0)
    SetChrChipByIndex(0x26, 0xA)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x26, 0x4)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 13850, 3500, 46310, 135)
    SetChrChipByIndex(0x27, 0xB)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x27, 0x4)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 13050, 3500, 45510, 135)
    OP_4B(0x26, 0xFF)
    OP_4B(0x27, 0xFF)
    SetChrPos(0x101, 15510, 3500, 44690, 315)
    SetChrPos(0x102, 14840, 3500, 43910, 315)
    SetChrPos(0x103, 16500, 3500, 44690, 315)
    SetChrPos(0x104, 15040, 3500, 42890, 315)
    SetChrPos(0x109, 15980, 3500, 42470, 315)
    SetChrPos(0x105, 16900, 3500, 43550, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x26,
        "Thank you everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Thanks to you, I got to see my\x01",
            "father again. I got to introduce\x01",
            "Aerie and Almin to him, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Haha, Geval seemed happy\x01",
            "to see us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, we're just glad we\x01",
            "could help.\x02\x03",
            "#00005FUmm, about Geval... Is\x01",
            "he still in there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Yes, he said he had\x01",
            "something to think about\x01",
            "and will return home later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "When we were talking to him, he\x01",
            "turned away from us suddenly\x01",
            "and wouldn't show his face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "I wonder why though...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1D,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FT-That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FEven the eyes of a corrupt\x01",
            "congressman are capable of\x01",
            "crying, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FI'm surprised.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHehe... Well, this is a\x01",
            "hard moment for a man.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x26, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00009FWell I'm sure everything\x01",
            "will be all right. No\x01",
            "need to worry.\x02\x03",
            "#00000FWhat will you guys do\x01",
            "now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Since I was able to\x01",
            "reunite with dad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "I was going to speak\x01",
            "with him about how we\x01",
            "can keep in touch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Because of my mother-in-\x01",
            "law it might not be that\x01",
            "simple, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "I plan on having him\x01",
            "visit us in Liberl\x01",
            "someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FI see... I hope it goes\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "He quit being a\x01",
            "congressman, so I think\x01",
            "he'll eventually visit us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Yes... A bright future\x01",
            "is waiting for all of\x01",
            "us!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    ChrTalk(
        0x26,
        "Isn't that right, Aerie?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    ChrTalk(
        0x27,
        "Yes, Alm!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "When we first held this\x01",
            "child, both of us swore\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Let's give Almin here\x01",
            "lots of little brothers\x01",
            "and sisters, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "...You and I, and lots\x01",
            "of lovable children...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Together, we'll make the best\x01",
            "family on the continent.\x01",
            "...That's what it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        "I love you, Aerie!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "I do too, Alm!\x02",
    )

    CloseMessageWindow()
    OP_63(0x26, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_63(0x27, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
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
    OP_63(0x1D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(Really, we didn't need\x01",
            "to hear all of that,\x01",
            "but... Well, whatever.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FSo, request complete,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15B88():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_15B88)
    Sleep(50)

    def lambda_15B98():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_15B98)
    Sleep(300)

    ChrTalk(
        0x26,
        (
            "Yes, you really helped us\x01",
            "out this time. I don't know\x01",
            "how I can ever thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "We'll be returning home to\x01",
            "Liberl in a little while. Thank\x01",
            "you so much for all your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FOk, have a safe trip.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    ChrTalk(
        0x26,
        (
            "Aerie, since we're here,\x01",
            "why not go sightseeing?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    ChrTalk(
        0x27,
        "I agree, Alm. Let's.\x02",
    )

    CloseMessageWindow()
    OP_93(0x27, 0x87, 0x0)

    def lambda_15CE9():
        OP_9B(0x1, 0xFE, 0xB4, 0x262, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_15CE9)
    Sleep(100)

    def lambda_15D01():
        OP_95(0xFE, 13050, 3500, 45510, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_15D01)
    WaitChrThread(0x26, 1)
    OP_93(0x27, 0xE1, 0x1F4)
    Sleep(500)
    OP_68(12010, 5000, 41990, 4000)
    MoveCamera(340, 27, 0, 4000)
    OP_6E(600, 4000)

    def lambda_15D4E():
        OP_95(0xFE, 7890, 3500, 42250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_15D4E)

    def lambda_15D68():
        OP_95(0xFE, 6900, 3500, 42860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_15D68)

    def lambda_15D82():

        label("loc_15D82")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_15D82")

    QueueWorkItem2(0x101, 1, lambda_15D82)
    Sleep(50)

    def lambda_15D97():

        label("loc_15D97")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_15D97")

    QueueWorkItem2(0x102, 1, lambda_15D97)
    Sleep(50)

    def lambda_15DAC():

        label("loc_15DAC")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_15DAC")

    QueueWorkItem2(0x103, 1, lambda_15DAC)
    Sleep(50)

    def lambda_15DC1():

        label("loc_15DC1")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_15DC1")

    QueueWorkItem2(0x104, 1, lambda_15DC1)
    Sleep(50)

    def lambda_15DD6():

        label("loc_15DD6")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_15DD6")

    QueueWorkItem2(0x109, 1, lambda_15DD6)
    Sleep(50)

    def lambda_15DEB():

        label("loc_15DEB")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_15DEB")

    QueueWorkItem2(0x105, 1, lambda_15DEB)
    Sleep(50)

    def lambda_15E00():

        label("loc_15E00")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_15E00")

    QueueWorkItem2(0x1D, 1, lambda_15E00)
    WaitChrThread(0x26, 1)
    WaitChrThread(0x27, 1)

    def lambda_15E1A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_15E1A)

    def lambda_15E27():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_15E27)
    OP_6F(0x79)

    def lambda_15E36():
        TurnDirection(0xFE, 0x27, 500)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_15E36)

    def lambda_15E43():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_15E43)
    Sleep(500)

    ChrTalk(
        0x26,
        "Ahaha, Aerie.㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "Uhuhu, oh you.㈱\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x27,
        "Baby",
        "Babubu.\x02",
    )

    CloseMessageWindow()

    def lambda_15E90():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_15E90)

    def lambda_15E9D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_15E9D)
    Sleep(300)

    def lambda_15EAD():
        OP_95(0xFE, 4830, 2000, 38020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_15EAD)

    def lambda_15EC7():
        OP_95(0xFE, 4470, 2000, 39100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_15EC7)
    Sleep(1000)
    OP_68(15240, 5000, 43490, 5000)
    MoveCamera(5, 29, 0, 5000)
    OP_6E(600, 5000)
    WaitChrThread(0x26, 1)

    def lambda_15F0D():
        OP_95(0xFE, 1480, 2000, 40200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_15F0D)
    Sleep(100)

    def lambda_15F2A():
        OP_95(0xFE, 1940, 2000, 41000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_15F2A)
    Sleep(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x1D, 0x1)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F...They made a huge\x01",
            "impact from beginning to\x01",
            "end, didn't they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHaha, indeed. I didn't\x01",
            "expect to be jealous of\x01",
            "them, though.\x02\x03",
            "#00104FIt has been a while, and\x01",
            "I feel like I too want\x01",
            "to visit my parents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FElie...\x02\x03",
            "#10109FHaha, I know. I have a\x01",
            "lot of respect for my\x01",
            "mom.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1D,
        (
            "Please accept my thanks\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_160C5():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_160C5)
    Sleep(50)

    def lambda_160D5():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_160D5)
    Sleep(50)

    def lambda_160E5():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_160E5)
    Sleep(50)

    def lambda_160F5():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_160F5)
    Sleep(50)

    def lambda_16105():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16105)
    Sleep(50)

    def lambda_16115():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16115)
    Sleep(300)

    ChrTalk(
        0x1D,
        (
            "I'll look after Geval\x01",
            "until he makes it back\x01",
            "to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYes. Thanks for your\x01",
            "cooperation, as always.\x02\x03",
            "#00000FIt's time for us to be\x01",
            "going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHehe, roger.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Search for Long\x01",
            "Lost Father]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x90, 0x1, 0x7)
    OP_29(0x90, 0x1, 0x8)
    OP_29(0x90, 0x4, 0x10)
    SetChrFlags(0x1D, 0x80)
    OP_D7(0x1E)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x26, 0xFF)
    OP_4C(0x27, 0xFF)
    SetMapObjFlags(0x3, 0x10)
    OP_65(0x4, 0x1)
    SetChrPos(0x0, 15390, 3500, 43000, 315)
    SetChrPos(0x26, 3170, 0, 14230, 135)
    SetChrPos(0x27, 2120, 0, 13670, 135)
    OP_69(0xFF, 0x0)
    SoundDistance(0x7B, 0xFFFF9372, 0x1F4, 0x230A, 0x1388, 0x4E20, 0x64, 0x0)
    OP_E3(0x1B26, 0x1F4, 0x143C)
    OP_E3(0x7936, 0x1F4, 0xFFFFFD6C)
    EventEnd(0x5)
    Return()

    # Function_76_15224 end

    def Function_77_162E4(): pass

    label("Function_77_162E4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(497)
    SoundLoad(950)
    ClearChrFlags(0x14, 0x80)
    OP_78(0xE, 0x14)
    OP_49()
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    OP_75(0xE, 0x1, 0x0)
    OP_71(0xE, 0x1, 0x78, 0x0, 0x20)
    OP_FF(0xE, 0x2EE, 0x2EE, 0x2EE)
    ClearChrFlags(0x15, 0x80)
    OP_78(0xF, 0x15)
    OP_49()
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    OP_71(0xF, 0x65, 0xA0, 0x0, 0x20)
    OP_FF(0xF, 0x307, 0x307, 0x307)
    ClearChrFlags(0x16, 0x80)
    OP_78(0x10, 0x16)
    OP_49()
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x1000)
    OP_75(0x10, 0x1, 0x0)
    OP_FF(0x10, 0x2EE, 0x2EE, 0x2EE)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x14, -46000, 16400, 90000, 260)
    OP_D5(0x14, 0x0, 0x3F7A0, 0x0, 0x0)
    SetChrPos(0x15, -46000, 16400, 90000, 260)
    OP_D5(0x15, 0x0, 0x3F7A0, 0x0, 0x0)
    SetChrPos(0x16, -46000, 0, 90000, 260)
    OP_D5(0x16, 0x0, 0x3F7A0, 0x0, 0x0)

    def lambda_16419():
        OP_96(0xFE, 0xFFFF4C50, 0x1900, 0x15F90, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_16419)

    def lambda_16433():
        OP_96(0xFE, 0xFFFF4C50, 0x1900, 0x15F90, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_16433)
    OP_82(0x32, 0x32, 0xBB8, 0x1F40)
    BeginChrThread(0x14, 0, 0, 78)
    OP_68(-26000, 5600, 70000, 0)
    MoveCamera(330, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(80000, 0)
    OP_68(-46000, 6900, 90000, 10000)
    MoveCamera(330, 30, 0, 10000)
    OP_6E(600, 10000)
    SetCameraDistance(70000, 10000)
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x15, 0x1)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x101, -18430, 3500, 62180, 330)
    SetChrPos(0x103, -17200, 3500, 62670, 324)
    SetChrPos(0x105, -18600, 3500, 60920, 324)
    SetChrPos(0x107, -15340, 3500, 61450, 277)
    SetChrSubChip(0x107, 0x5)
    OP_68(-24740, 5600, 71790, 0)
    MoveCamera(324, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(24190, 0)
    OP_68(-18990, 5600, 64470, 5000)

    def lambda_16591():
        OP_96(0xFE, 0xFFFF4C50, 0x6720, 0x15F90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_16591)

    def lambda_165AB():
        OP_96(0xFE, 0xFFFF4C50, 0x6720, 0x15F90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_165AB)
    BeginChrThread(0x14, 0, 0, 80)
    BeginChrThread(0x15, 0, 0, 79)
    FadeToBright(1000, 0)
    OP_0D()
    StopSound(497, 3000, 90)
    OP_6F(0x79)
    Fade(500)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x15, 0x0)
    OP_68(-17780, 5600, 62410, 0)
    MoveCamera(323, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16850, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10406F#6PWe got down here safely,\x01",
            "but...\x02\x03",
            "#10408FIsn't this the village's\x01",
            "lotus fields?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#6PYeah... It looks very\x01",
            "different, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12PThis is probably due to\x01",
            "KeA's awakening as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-17020, 5600, 61730, 1000)
    TurnDirection(0x103, 0x107, 400)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        (
            "#00201F#5PZeit. Any sign of\x01",
            "cryptids?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16746():
        TurnDirection(0x101, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_16746)
    Sleep(0)

    def lambda_16756():
        TurnDirection(0x105, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_16756)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x107,
        (
            "#01203F#12P#3C#NHmm. I don't sense any\x01",
            "for now.\x02\x03",
            "#01200FIt doesn't seem like the\x01",
            "magic circle is in any\x01",
            "immediate danger.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#5PRoger.\x02\x03",
            "#00001FFor now, I think we\x01",
            "should meet with Chief\x01",
            "Tolta.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11PRoger. Let's go.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(17100, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1F1)
    OP_24(0x3B6)
    SetScenarioFlags(0x22, 0)
    NewScene("t0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_77_162E4 end

    def Function_78_16883(): pass

    label("Function_78_16883")

    Sleep(2000)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_71(0xF, 0x0, 0x32, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 2000, 40)
    OP_75(0xE, 0x2, 0x7D0)
    OP_75(0x10, 0x2, 0x7D0)
    Sleep(1000)
    OP_79(0xF)
    Return()

    # Function_78_16883 end

    def Function_79_168C8(): pass

    label("Function_79_168C8")

    OP_75(0xE, 0x1, 0x7D0)
    OP_75(0x10, 0x1, 0x7D0)
    Sleep(500)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_71(0xF, 0x33, 0x64, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 2000, 40)
    OP_79(0xF)
    OP_71(0xF, 0x65, 0xA0, 0x0, 0x20)
    Return()

    # Function_79_168C8 end

    def Function_80_16916(): pass

    label("Function_80_16916")

    OP_82(0x32, 0x32, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x28, 0x28, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x1E, 0x1E, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x14, 0x14, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0xA, 0xA, 0xBB8, 0x3E8)
    Sleep(1000)
    Return()

    # Function_80_16916 end

    def Function_81_1697B(): pass

    label("Function_81_1697B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 19200, 500, 21050, 200)
    SetChrPos(0x103, 19200, 500, 21050, 200)
    SetChrPos(0x105, 19200, 500, 21050, 200)
    SetChrPos(0x107, 19200, 500, 21050, 200)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(19200, 1500, 21050, 0)
    MoveCamera(330, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(17950, 1000, 16250, 4000)
    MoveCamera(315, 30, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(18000, 4000)

    def lambda_16A7D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_16A7D)
    BeginChrThread(0x101, 1, 0, 82)
    Sleep(1000)

    def lambda_16A97():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_16A97)
    BeginChrThread(0x103, 1, 0, 83)
    Sleep(1000)

    def lambda_16AB1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_16AB1)
    BeginChrThread(0x105, 1, 0, 84)
    Sleep(1000)

    def lambda_16ACB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_16ACB)
    BeginChrThread(0x107, 1, 0, 85)
    Sleep(1000)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x107, 1)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10404F#12PWell then─\x02\x03",
            "#10400FAre we going to the\x01",
            "Ancient Battlefield?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PYeah. Even though we\x01",
            "don't know who the rebel\x01",
            "force is.\x02\x03",
            "#00001FI'd like to cooperate\x01",
            "with them, if at all\x01",
            "possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#5PI agree... I think\x01",
            "there's value in looking\x01",
            "for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#11P#3CIn that case, let us\x01",
            "journey there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 17950, 0, 16250, 180)
    SetScenarioFlags(0x1A1, 5)
    OP_29(0xAF, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_81_1697B end

    def Function_82_16C7A(): pass

    label("Function_82_16C7A")

    OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x101, 17500, 0, 14850, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_82_16C7A end

    def Function_83_16CA5(): pass

    label("Function_83_16CA5")

    OP_9B(0x0, 0x103, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x103, 16900, 0, 16550, 2000, 0x0)
    OP_93(0x103, 0x87, 0x1F4)
    Return()

    # Function_83_16CA5 end

    def Function_84_16CD0(): pass

    label("Function_84_16CD0")

    OP_9B(0x0, 0x105, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x105, 18950, 0, 16100, 2000, 0x0)
    OP_93(0x105, 0xE1, 0x1F4)
    Return()

    # Function_84_16CD0 end

    def Function_85_16CFB(): pass

    label("Function_85_16CFB")

    OP_9B(0x0, 0x107, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x107, 18000, 0, 17750, 2000, 0x0)
    OP_93(0x107, 0xB4, 0x1F4)
    SetChrSubChip(0x107, 0x5)
    Return()

    # Function_85_16CFB end

    def Function_86_16D2A(): pass

    label("Function_86_16D2A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    FadeToBright(1000, 0)
    Call(0, 87)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16FEB")
    Fade(500)
    OP_68(15510, 1350, -23710, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16EF0")
    SetChrPos(0x101, 21180, 0, -27450, 315)
    SetChrPos(0x104, 22100, 0, -28790, 315)
    SetChrPos(0x105, 23130, 0, -30790, 315)
    SetChrPos(0x102, 20230, 0, -28520, 315)
    SetChrPos(0x103, 20790, 0, -30560, 315)
    SetChrPos(0x109, 22200, 0, -31420, 315)

    def lambda_16E27():
        OP_95(0xFE, 15110, 0, -21470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16E27)

    def lambda_16E41():
        OP_95(0xFE, 16020, 0, -22930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16E41)

    def lambda_16E5B():
        OP_95(0xFE, 16930, 0, -24390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16E5B)

    def lambda_16E75():
        OP_95(0xFE, 13980, 0, -22200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16E75)

    def lambda_16E8F():
        OP_95(0xFE, 14940, 0, -23710, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_16E8F)

    def lambda_16EA9():
        OP_95(0xFE, 15900, 0, -25220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16EA9)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x109, 1)
    Jump("loc_16FE6")

    label("loc_16EF0")

    SetChrPos(0x101, 21180, 0, -27450, 315)
    SetChrPos(0x104, 22100, 0, -28790, 315)
    SetChrPos(0x102, 20230, 0, -28520, 315)
    SetChrPos(0x109, 21290, 0, -30060, 315)
    SetChrPos(0x105, 22810, 0, -31000, 315)

    def lambda_16F4A():
        OP_95(0xFE, 15110, 0, -21470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16F4A)

    def lambda_16F64():
        OP_95(0xFE, 16020, 0, -22930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16F64)

    def lambda_16F7E():
        OP_95(0xFE, 13980, 0, -22200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16F7E)

    def lambda_16F98():
        OP_95(0xFE, 14940, 0, -23710, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16F98)

    def lambda_16FB2():
        OP_95(0xFE, 16410, 0, -24800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16FB2)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    label("loc_16FE6")

    Jump("loc_1745C")

    label("loc_16FEB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17240")
    Fade(500)
    OP_68(17090, 1500, -25640, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    ClearChrFlags(0x13, 0x80)
    OP_78(0x8, 0x13)
    OP_49()
    SetChrPos(0x13, 27180, 0, -35450, 315)
    OP_D5(0x13, 0x0, 0x4CE78, 0x0, 0x0)
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    OP_0D()
    OP_49()
    BeginChrThread(0x28, 1, 0, 88)
    SetMapObjFlags(0x8, 0x1000)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)

    def lambda_1709A():
        OP_95(0xFE, 15110, 0, -21470, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1709A)
    Sleep(3500)
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    EndChrThread(0x13, 0x1)
    SetChrPos(0x13, 16500, 0, -18100, 135)
    OP_D5(0x13, 0x0, 0x20F58, 0x0, 0x0)
    OP_71(0x8, 0x0, 0x0, 0x0, 0x0)
    OP_79(0x8)
    SetMapObjFlags(0x8, 0x2)
    OP_66(0x2, 0x1)
    OP_68(12290, 1200, -19990, 0)
    MoveCamera(7, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15300, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_171D2")
    SetChrPos(0x101, 11870, 0, -18060, 315)
    SetChrPos(0x104, 12780, 0, -19520, 315)
    SetChrPos(0x105, 13690, 0, -20980, 315)
    SetChrPos(0x102, 10840, 0, -18790, 315)
    SetChrPos(0x103, 11800, 0, -20300, 315)
    SetChrPos(0x109, 12760, 0, -21810, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_17231")

    label("loc_171D2")

    SetChrPos(0x101, 11870, 0, -18060, 315)
    SetChrPos(0x104, 12780, 0, -19520, 315)
    SetChrPos(0x102, 10840, 0, -18790, 315)
    SetChrPos(0x109, 11800, 0, -20300, 315)
    SetChrPos(0x105, 13220, 0, -21400, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_17231")

    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_1745C")

    label("loc_17240")

    Fade(500)
    OP_68(4100, 1500, -16270, 0)
    MoveCamera(0, 33, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(17000, 0)
    OP_E2(0x1)
    ClearChrFlags(0x12, 0x80)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x7, 0x2)
    OP_78(0x7, 0x12)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x12, 13270, 0, -22560, 0)
    OP_D5(0x12, 0x0, 0x1F4, 0x0, 0x0)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)
    BeginChrThread(0x12, 1, 0, 5)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x12, 1)
    OP_79(0x7)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetMapObjFlags(0x7, 0x4)
    OP_68(1610, 1500, -14250, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16110, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x101, 250, 0, -13500, 0)
    SetChrPos(0x102, 1250, 0, -13500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_173F3")
    SetChrPos(0x101, 1030, 0, -12060, 0)
    SetChrPos(0x104, 1940, 0, -13520, 0)
    SetChrPos(0x105, 2850, 0, -14980, 0)
    SetChrPos(0x102, 0, 0, -12790, 0)
    SetChrPos(0x103, 960, 0, -14300, 0)
    SetChrPos(0x109, 1920, 0, -15810, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_17452")

    label("loc_173F3")

    SetChrPos(0x101, 1030, 0, -12060, 0)
    SetChrPos(0x104, 1940, 0, -13520, 0)
    SetChrPos(0x102, 0, 0, -12790, 0)
    SetChrPos(0x109, 960, 0, -14300, 0)
    SetChrPos(0x105, 2380, 0, -15400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_17452")

    FadeToBright(1000, 0)
    OP_0D()

    label("loc_1745C")


    ChrTalk(
        0x105,
        (
            "#12P#10302FWow, what a scenic\x01",
            "village.\x02\x03",
            "#10304FThis is "Armorica\x01",
            "Village", right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, that's right.\x02\x03",
            "#00104FBeekeeping, agriculture\x01",
            "and livestock are the\x01",
            "main industries...\x02\x03",
            "#00102FEven now, a small number\x01",
            "of the legendary Divine\x01",
            "Wolves remain here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FThat's right... This was the place\x01",
            "we conducted our first activity\x01",
            "outside the city, wasn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FThe incident with the\x01",
            "mafia's military dogs... it\x01",
            "really takes me back.\x02\x03",
            "#10103FBack then, I remember our\x01",
            "investigation being handed\x01",
            "over to the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, that was also the\x01",
            "fault of that\x01",
            "incompetent commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHaha, and Zeit has been with us\x01",
            "ever since that incident.\x02\x03",
            "#00104FHe came to our aid when we were\x01",
            "in grave danger, and the incident\x01",
            "was resolved thanks to him.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1781E")

    ChrTalk(
        0x101,
        (
            "#00009FZeit has been saving us\x01",
            "ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FYes, and not just in combat.\x01",
            "He's supported us in various\x01",
            "situations, as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_178A4")

    label("loc_1781E")


    ChrTalk(
        0x101,
        (
            "#00009FZeit has been saving us ever\x01",
            "since.\x02\x03",
            "#00004FNot just in combat, either.\x01",
            "He's supported us in various\x01",
            "investigations, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_178A4")


    ChrTalk(
        0x105,
        (
            "#12P#10304FHaha, well I get the feeling\x01",
            "Zeit isn't the only one\x01",
            "who's been helping you guys.\x02\x03",
            "#10309FRather, isn't he always\x01",
            "stealing the Support\x01",
            "Section's thunder?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17953():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17953)

    def lambda_17960():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_17960)

    def lambda_1796D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1796D)

    def lambda_1797A():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1797A)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17A17")

    def lambda_179F7():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_179F7)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_17A17")

    Sleep(1000)

    ChrTalk(
        0x109,
        "#6P#10106FW-Wazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FDamn, you always gotta\x01",
            "stab our weak spots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FW-Well anyway... We've\x01",
            "grown, and we'll have to\x01",
            "work on that.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x14E, 7)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17ADD")
    SetChrPos(0x0, 15500, 0, -23930, 315)
    Jump("loc_17B12")

    label("loc_17ADD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B01")
    SetChrPos(0x0, 11350, 0, -18420, 315)
    Jump("loc_17B12")

    label("loc_17B01")

    SetChrPos(0x0, 890, 0, -13080, 315)

    label("loc_17B12")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17B36")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_17B36")

    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_86_16D2A end

    def Function_87_17B42(): pass

    label("Function_87_17B42")

    OP_68(-37350, 1500, 69780, 0)
    MoveCamera(338, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(53190, 0)
    OP_68(-21000, 1500, 74410, 12000)
    Sleep(9000)
    Fade(1000)
    OP_68(7400, 1500, 48380, 0)
    MoveCamera(323, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(37470, 0)
    OP_68(-12130, 1500, 35080, 12000)
    Sleep(9000)
    Fade(1000)
    OP_68(-1020, 5100, 4110, 0)
    MoveCamera(338, 8, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(44250, 0)
    PlaceName2(340, 40, "c_plac14", 0x0, 3000)
    OP_68(-1020, 2800, 4110, 7000)
    OP_6F(0x1)
    Return()

    # Function_87_17B42 end

    def Function_88_17C23(): pass

    label("Function_88_17C23")

    Sleep(500)
    Sound(459, 0, 100, 0)
    Sleep(1200)
    Sleep(1500)
    Sound(492, 0, 90, 0)
    Return()

    # Function_88_17C23 end

    def Function_89_17C39(): pass

    label("Function_89_17C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F76")
    EventBegin(0x0)
    Fade(1000)
    OP_68(16470, 1500, -26270, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x13, 12610, 0, -12660, 0)
    SetChrPos(0x101, 16690, 0, -26040, 135)
    SetChrPos(0x103, 17490, 0, -25240, 135)
    SetChrPos(0x105, 15690, 0, -25040, 135)
    SetChrPos(0x107, 16490, 0, -24240, 135)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_17D27():
        OP_93(0x107, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_17D27)
    Sleep(0)

    def lambda_17D37():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_17D37)
    Sleep(0)

    def lambda_17D47():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_17D47)
    Sleep(0)

    def lambda_17D57():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_17D57)
    Sleep(0)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    Sleep(1000)
    Fade(1000)
    OP_68(12070, 1100, -16020, 0)
    MoveCamera(359, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16149, 0)
    SetChrPos(0x101, 12450, 0, -17250, 0)
    SetChrPos(0x103, 11450, 0, -17250, 0)
    SetChrPos(0x105, 12950, 0, -18450, 0)
    SetChrPos(0x107, 10950, 0, -18450, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00000FThis orbal car... It's\x01",
            "Harold's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FIt's a Verne Co. model...\x01",
            "We've ridden in it before,\x01",
            "if I'm not mistaken.\x02\x03",
            "#00203FThe chief said they were\x01",
            "staying on 2F at the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10403FFor right now, we need\x01",
            "information.\x02\x03",
            "#10400FIt's best if we ask\x01",
            "around before heading\x01",
            "out on the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, let's give it a\x01",
            "try.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1AD, 6)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 11950, 0, -17850, 0)
    EventEnd(0x5)
    Jump("loc_17FF0")

    label("loc_17F76")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FIt looks like Harold is\x01",
            "staying here.\x02\x03",
            "Before heading out,\x01",
            "let's visit 2F at the\x01",
            "inn.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 17090, 0, -25640, 321)
    EventEnd(0x4)

    label("loc_17FF0")

    Return()

    # Function_89_17C39 end

    SaveToFile()

Try(main)
