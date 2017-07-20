from ScenarioHelper import *

def main():
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
        "Camille",               # 1
        "Elkin",               # 2
        "pulley",               # 3
        "Stephane",             # 4
        "Derrick",               # 5
        "Minnes",               # 6
        "Aretha",                 # 7
        "Sofia",               # 8
        "Choline",                 # 9
        "Mushroute Scott",         # 10
        "bus",                   # 11
        "Special support vehicle",             # 12
        "Mercapa machine",         # 13
        "Mercapa optical camouflage",       # 14
        "Mercapa shadow",             # 15
        "Keith",                 # 16
        "Zookoist Rin",             # 17
        "Friend Aolia",         # 18
        "Angers",               # 19
        "Gofan",             # 20
        "Cry",               # 21
        "Mayor of Torta",             # 22
        "Pete",                 # 23
        "Harold",               # 24
        "Cat type devil",               # 25
        "Cat type devil",               # 26
        "Cat type devil",               # 27
        "Cat type devil",               # 28
        "Cat type devil",               # 29
        "Black truck",             # 30
        "Almu",                 # 31
        "Airy",               # 32
        "SE control",                 # 33
        "bt0000",                 # 34
        "bt0000",                 # 35
        "Almorica ancient road",         # 36
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

    PlaceName(28.0, 0.0, -40.0, 0x0000, 0x0000, "Almorica ancient road")
    PlaceName(-25.0, 0.0, 20.0, 0x0000, 0x0053, "")
    PlaceName(20.399999618530273, 0.0, 25.25, 0x0000, 0x0052, "")
    PlaceName(-2.0, 0.0, -14.699999809265137, 0x0000, 0x0055, "")

    ChipFrameInfo(2404, 0)                                       # 0

    ScpFunction((
        "Function_0_964",          # 00, 0
        "Function_1_A1C",          # 01, 1
        "Function_2_12CF",         # 02, 2
        "Function_3_175B",         # 03, 3
        "Function_4_184B",         # 04, 4
        "Function_5_195E",         # 05, 5
        "Function_6_1994",         # 06, 6
        "Function_7_19E5",         # 07, 7
        "Function_8_1A79",         # 08, 8
        "Function_9_3054",         # 09, 9
        "Function_10_3B50",        # 0A, 10
        "Function_11_3DE6",        # 0B, 11
        "Function_12_447D",        # 0C, 12
        "Function_13_4C7D",        # 0D, 13
        "Function_14_5401",        # 0E, 14
        "Function_15_5521",        # 0F, 15
        "Function_16_55F9",        # 10, 16
        "Function_17_5786",        # 11, 17
        "Function_18_584E",        # 12, 18
        "Function_19_5900",        # 13, 19
        "Function_20_5C89",        # 14, 20
        "Function_21_5DCC",        # 15, 21
        "Function_22_5EC9",        # 16, 22
        "Function_23_620C",        # 17, 23
        "Function_24_6258",        # 18, 24
        "Function_25_632C",        # 19, 25
        "Function_26_656E",        # 1A, 26
        "Function_27_78A4",        # 1B, 27
        "Function_28_8D98",        # 1C, 28
        "Function_29_8F64",        # 1D, 29
        "Function_30_BAF6",        # 1E, 30
        "Function_31_BC0A",        # 1F, 31
        "Function_32_BC27",        # 20, 32
        "Function_33_C0F7",        # 21, 33
        "Function_34_CB66",        # 22, 34
        "Function_35_12DA0",       # 23, 35
        "Function_36_12DD4",       # 24, 36
        "Function_37_12E08",       # 25, 37
        "Function_38_12E3C",       # 26, 38
        "Function_39_12E70",       # 27, 39
        "Function_40_12EA4",       # 28, 40
        "Function_41_12ED8",       # 29, 41
        "Function_42_12F0C",       # 2A, 42
        "Function_43_12F40",       # 2B, 43
        "Function_44_12F74",       # 2C, 44
        "Function_45_12FA8",       # 2D, 45
        "Function_46_12FDC",       # 2E, 46
        "Function_47_13010",       # 2F, 47
        "Function_48_13044",       # 30, 48
        "Function_49_13078",       # 31, 49
        "Function_50_130AC",       # 32, 50
        "Function_51_130D4",       # 33, 51
        "Function_52_130F7",       # 34, 52
        "Function_53_1316C",       # 35, 53
        "Function_54_131F5",       # 36, 54
        "Function_55_1326A",       # 37, 55
        "Function_56_132F3",       # 38, 56
        "Function_57_13368",       # 39, 57
        "Function_58_133B3",       # 3A, 58
        "Function_59_133FE",       # 3B, 59
        "Function_60_13449",       # 3C, 60
        "Function_61_13494",       # 3D, 61
        "Function_62_134DF",       # 3E, 62
        "Function_63_1353E",       # 3F, 63
        "Function_64_13558",       # 40, 64
        "Function_65_1383B",       # 41, 65
        "Function_66_13D12",       # 42, 66
        "Function_67_14347",       # 43, 67
        "Function_68_14375",       # 44, 68
        "Function_69_143B7",       # 45, 69
        "Function_70_143F9",       # 46, 70
        "Function_71_1443B",       # 47, 71
        "Function_72_1447D",       # 48, 72
        "Function_73_144BF",       # 49, 73
        "Function_74_14501",       # 4A, 74
        "Function_75_14C04",       # 4B, 75
        "Function_76_14C46",       # 4C, 76
        "Function_77_15D0A",       # 4D, 77
        "Function_78_162BE",       # 4E, 78
        "Function_79_16303",       # 4F, 79
        "Function_80_16351",       # 50, 80
        "Function_81_163B6",       # 51, 81
        "Function_82_1669D",       # 52, 82
        "Function_83_166C8",       # 53, 83
        "Function_84_166F3",       # 54, 84
        "Function_85_1671E",       # 55, 85
        "Function_86_1674D",       # 56, 86
        "Function_87_174B7",       # 57, 87
        "Function_88_17598",       # 58, 88
        "Function_89_175AE",       # 59, 89
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
            "#1KThere is a bus stop.\x01",
            "Do you want to move by bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City East Exit\x01",      # 0
            "Tangram Gate\x01",          # 1
            "Stop (three-way street)\x01",      # 2
            "quit\x01",                # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17FE")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1843")

    label("loc_17FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1823")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1843")

    label("loc_1823")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1843")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_1843")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_3_175B end

    def Function_4_184B(): pass

    label("Function_4_184B")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_195A")
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

    label("loc_195A")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_4_184B end

    def Function_5_195E(): pass

    label("Function_5_195E")

    OP_95(0x12, 10630, 0, -20520, 4000, 0x0)
    OP_9E(0x12, 0x1770, 0xFFFF987C, 0xFFFF0DD0, 0xFA0, 0x1)
    OP_71(0x7, 0x5B, 0x78, 0x0, 0x0)
    Return()

    # Function_5_195E end

    def Function_6_1994(): pass

    label("Function_6_1994")

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

    # Function_6_1994 end

    def Function_7_19E5(): pass

    label("Function_7_19E5")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1A40")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A35")
    Sound(2502, 255, 100, 0)
    Jump("loc_1A3B")

    label("loc_1A35")

    Sound(2503, 255, 100, 0)

    label("loc_1A3B")

    Jump("loc_1A64")

    label("loc_1A40")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A5E")
    Sound(3347, 255, 100, 0)
    Jump("loc_1A64")

    label("loc_1A5E")

    Sound(3348, 255, 100, 0)

    label("loc_1A64")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_19E5 end

    def Function_8_1A79(): pass

    label("Function_8_1A79")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1BDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B56")

    ChrTalk(
        0x9,
        (
            "Oh, you pissed me off … …\x01",
            "What is that big tree! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Suddenly that such things appear,\x01",
            "Whatever you think about it is not normal …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "On days when you can drive happily\x01",
            "Is it no longer able to return …?! Is it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BDA")

    label("loc_1B56")


    ChrTalk(
        0x9,
        (
            "Suddenly that such things appear,\x01",
            "What about the crossbell … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "On days when you can drive happily\x01",
            "Is it no longer able to return …?! Is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDA")

    Jump("loc_3050")

    label("loc_1BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1D71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC4")

    ChrTalk(
        0x9,
        (
            "The invalid declaration of an independent country\x01",
            "I heard that it was issued?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In fact, you can enjoy the drive as it is\x01",
            "The original crossbell is better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I was not sure about independence,\x01",
            "Everything as it is\x01",
            "I hope to return to the original.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D6C")

    label("loc_1CC4")


    ChrTalk(
        0x9,
        (
            "From an independent country,\x01",
            "You can enjoy the drive as it is\x01",
            "The original crossbell is better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems that invalid declaration was also issued,\x01",
            "Everything as it is\x01",
            "I hope to return to the original.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D6C")

    Jump("loc_3050")

    label("loc_1D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1F1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E7B")

    ChrTalk(
        0x9,
        (
            "Under the movement regulations of the highway\x01",
            "Buses and cars almost do not come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Armored cars of the defense army who come to the village occasionally also\x01",
            "I think it's cool, but ….\x01",
            "To tell the truth, I got tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because \"something else\" comes out\x01",
            "I can not drive it as it is … …\x01",
            "This state, how long will it last? Is it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F17")

    label("loc_1E7B")


    ChrTalk(
        0x9,
        (
            "With the movement regulation of the highway,\x01",
            "In the village the defense armored armored car\x01",
            "It occasionally comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because \"something else\" comes out\x01",
            "I can not drive it ……\x01",
            "This state, how long will it last? Is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F17")

    Jump("loc_3050")

    label("loc_1F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1FAA")

    ChrTalk(
        0xFE,
        (
            "There was such a raid incident,\x01",
            "I am afraid to go out on the highway, though ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In such a case, we\x01",
            "I have to protect the village.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3050")

    label("loc_1FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1FB8")
    Jump("loc_3050")

    label("loc_1FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_230A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_205E")

    ChrTalk(
        0xFE,
        (
            "Derrick and Minnes' plan is\x01",
            "It seems that it has come quite clearly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How is this village\x01",
            "Will it evolve … ….\x01",
            "Hehe, I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2305")

    label("loc_205E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A6")

    ChrTalk(
        0xFE,
        (
            "Ha, but Mr. Minneshima\x01",
            "It was a cheat … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish you guys from him\x01",
            "This guided car that I bought … ….\x01",
            "What do you think I should do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FIndeed, about 500,000 mirrors\x01",
            "The power track of the market,\x01",
            "It was a story that I bought it at 50,000 mirrors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNo……\x01",
            "It certainly is a subtle problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FOnce handed over to the police\x01",
            "Who leaves the judgment\x01",
            "It might be nice.\x02\x03",
            "#00104FSince it was traded by an official deal,\x01",
            "I think that it will probably be refunded soon ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FWell, there is no illegality in the car itself\x01",
            "Whether it would be better to do so in the sense that it should be examined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's right.\x01",
            "Well, I guess I'll contact the police.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16F, 7)
    Jump("loc_2305")

    label("loc_22A6")


    ChrTalk(
        0xFE,
        (
            "A new truck from a con artist\x01",
            "I bought it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, I guess I'll contact the police.\x02",
    )

    CloseMessageWindow()

    label("loc_2305")

    Jump("loc_3050")

    label("loc_230A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2573")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_243E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E7")

    ChrTalk(
        0xFE,
        (
            "If it is Derrick,\x01",
            "In order to meet Mineness\x01",
            "It remained in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By around this time, at the hotel of the entertainment district\x01",
            "I guess they are talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Well, then,\x01",
            "It is the newest type of time.\x01",
            "I need to maintain it well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2439")

    label("loc_23E7")


    ChrTalk(
        0xFE,
        (
            "If it is a derrick,\x01",
            "Mr. Minnes at the hotel of the entertainment district\x01",
            "I guess they are talking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2439")

    Jump("loc_256E")

    label("loc_243E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24FD")

    ChrTalk(
        0xFE,
        (
            "Mr. Minnes\x01",
            "It is a really fat person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, a major confectionery company\x01",
            "To Quincy\x01",
            "I just have to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The plan with Derrick, too,\x01",
            "I would like to support you all means\x01",
            "Where are you?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_256E")

    label("loc_24FD")


    ChrTalk(
        0xFE,
        (
            "Mr. Minnes\x01",
            "It is a really fat person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, a major confectionery company\x01",
            "To Quincy\x01",
            "I just have to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_256E")

    Jump("loc_3050")

    label("loc_2573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_293E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 2)), scpexpr(EXPR_END)), "loc_2745")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2650")

    ChrTalk(
        0xFE,
        (
            "eh……\x01",
            "The key to private estate was opened! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, I see.\x01",
            "Even those who do annoying things\x01",
            "I thought you were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank you for telling me.\x01",
            "Later on the truck\x01",
            "I will go on closing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2740")

    label("loc_2650")


    ChrTalk(
        0xFE,
        (
            "Key of private property ……\x01",
            "Later on the truck\x01",
            "I hope to close it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… In fact, to tell the truth\x01",
            "Recently the track has come into play.\x01",
            "It is depressed to drive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But buy a new driving truck\x01",
            "There is no budget in the village … …\x01",
            "I must manage it somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2740")

    Jump("loc_2939")

    label("loc_2745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2859")

    ChrTalk(
        0xFE,
        (
            "In the middle of Almorica's ancient road,\x01",
            "There is a private property managed in the village.\x01",
            "I just came back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are agricultural tools and materials\x01",
            "Because it is a storage place,\x01",
            "You must not go unnoticed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, normally I wear a lock\x01",
            "I'm trying not to put it in\x01",
            "I think it's all right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2939")

    label("loc_2859")


    ChrTalk(
        0xFE,
        (
            "In the middle of Almorica's ancient road,\x01",
            "There is a private property managed in the village.\x01",
            "I just came back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, to foreigners in the village\x01",
            "It seems that customers are coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if this black truck is also for him?\x01",
            "It looks like a pretty luxury car, though ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2939")

    Jump("loc_3050")

    label("loc_293E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2BD3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2A5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29E0")

    ChrTalk(
        0x9,
        (
            "I was watching a special lesson,\x01",
            "A little earlier\x01",
            "It was a great technique.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, the match and nice as before\x01",
            "It is truly a hitter fighter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A5A")

    label("loc_29E0")


    ChrTalk(
        0x9,
        (
            "Oh, look at the previous meeting\x01",
            "The excitement is still insufficient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huhu, and also with the hit prisoner\x01",
            "Please let me see the match.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A5A")

    Jump("loc_2BCE")

    label("loc_2A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B6F")

    ChrTalk(
        0x9,
        (
            "I am excited,\x01",
            "I get a little accent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because it does not seem like young people of this time\x01",
            "I would like to fix it if possible, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After consulting Miria's sister,\x01",
            "I do not have to worry about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought it was someone else's … …\x01",
            "This is a redneck full name.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BCE")

    label("loc_2B6F")


    ChrTalk(
        0xFE,
        (
            "My older sister, my accent\x01",
            "You do not have to worry about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I thought it was someone else's … …\x02",
    )

    CloseMessageWindow()

    label("loc_2BCE")

    Jump("loc_3050")

    label("loc_2BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3050")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DAB")

    ChrTalk(
        0x9,
        "Hi, welcome to Almorika village.\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x87, 0x1F4)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "You …\x01",
            "What, that guidance car! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even made by Verne\x01",
            "It is not made by Rheinfault Co., Ltd. …\x01",
            "Such a car, I saw it for the first time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FHehe, that car is made by ZCF.\x02\x03",
            "#10102FThanks to the new engine installed\x01",
            "The maximum speed is 1500 Serge\x01",
            "It's got to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well yeah yeah … ….\x01",
            "Well that's fine, I wish! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(Noel, I'm proudly proud … …)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 5)
    Jump("loc_2F1B")

    label("loc_2DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E91")

    ChrTalk(
        0x9,
        (
            "Maximum speed 1500 Serge …\x01",
            "ZCF also Nikui\x01",
            "I thought I made it … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh no, I do not mind!\x01",
            "Ora also has new trucks\x01",
            "I'm getting wanted!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Kohon.\x01",
            "No, I got excited and caught up\x01",
            "I got an accent.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F1B")

    label("loc_2E91")


    ChrTalk(
        0x9,
        (
            "Speaking of which, the suspicious people during this time\x01",
            "What was it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, whatever you want, I do not care.\x01",
            "If there is no obstacle to my guide car life.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F1B")

    Jump("loc_3050")

    label("loc_2F20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC6")

    ChrTalk(
        0x9,
        "Hi, welcome to Almorika village.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In this village beekeeping, agriculture,\x01",
            "I am doing livestock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The view is nice and it is okay\x01",
            "What do you say if you go slowly?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3050")

    label("loc_2FC6")


    ChrTalk(
        0x9,
        (
            "Speaking of which, the suspicious people during this time\x01",
            "What was it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, whatever you want, I do not care.\x01",
            "If there is no obstacle to my guide car life.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3050")

    TalkEnd(0xFE)
    Return()

    # Function_8_1A79 end

    def Function_9_3054(): pass

    label("Function_9_3054")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3169")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30EC")

    ChrTalk(
        0x8,
        (
            "Adults were making noise, but …\x01",
            "That tree, it's really awesome ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you climb trees with such huge trees\x01",
            "It looks really fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3164")

    label("loc_30EC")


    ChrTalk(
        0x8,
        (
            "If you climb trees with such huge trees\x01",
            "It looks really fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huge beetle and so on\x01",
            "I guess they will stop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3164")

    Jump("loc_3B4C")

    label("loc_3169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_32E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_324D")

    ChrTalk(
        0x8,
        (
            "Okay, then, today\x01",
            "Even with a can kake!\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0x10,
        (
            "#03805FRan Koori\x01",
            "What is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, I do not know about canning! Is it?\x01",
            "I guess …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, basically\x01",
            "It's hide-and-see, but ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0x10, 0xFF)
    Jump("loc_32DC")

    label("loc_324D")


    ChrTalk(
        0x8,
        (
            "Suddenly, while there is no oni\x01",
            "This can ……\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0x10,
        (
            "#03809FI know that ~, crush it\x01",
            "Is not it garbage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "So, that is why ~.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)

    label("loc_32DC")

    Jump("loc_3B4C")

    label("loc_32E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3416")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33A9")

    ChrTalk(
        0x8,
        (
            "Hello, my uncle Harold\x01",
            "I brought a cuddly to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if my brother got it\x01",
            "I wonder what it is like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As an older, firmly\x01",
            "I have to watch Mendo!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3411")

    label("loc_33A9")


    ChrTalk(
        0x8,
        (
            "Harold uncle, too,\x01",
            "I wish I could move to the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then Colin, too\x01",
            "I can always play this way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3411")

    Jump("loc_3B4C")

    label("loc_3416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3576")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34FD")

    ChrTalk(
        0x8,
        (
            "Something, in this time in Crossbell City\x01",
            "It seems that the Koei went around rampage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because this village is boring,\x01",
            "I wonder if any incident will happen\x01",
            "I was thinking well … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Truly, what about a raid incident\x01",
            "I'm sorry completely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3571")

    label("loc_34FD")


    ChrTalk(
        0x8,
        (
            "This village is too peaceful and bored\x01",
            "I always thought that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Could it be,\x01",
            "I wonder if it was pretty zetaku.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3571")

    Jump("loc_3B4C")

    label("loc_3576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3584")
    Jump("loc_3B4C")

    label("loc_3584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3760")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35FA")

    ChrTalk(
        0x8,
        "Oh, today I am bored.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I feel like waking up here\x01",
            "I wonder if it will happen even in a major incident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_375B")

    label("loc_35FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36D8")

    ChrTalk(
        0x8,
        (
            "I guess it was awesome a while ago!\x01",
            "A huge cat is coming out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Perhaps, that uncle\x01",
            "At some circus\x01",
            "I wonder if you are going to use animal beasts, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wow, even with a sign\x01",
            "It was nice to hear it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_375B")

    label("loc_36D8")


    ChrTalk(
        0x8,
        (
            "Perhaps, that uncle\x01",
            "At some circus\x01",
            "I wonder if you are going to use animal beasts, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wow, even with a sign\x01",
            "It was nice to hear it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_375B")

    Jump("loc_3B4C")

    label("loc_3760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_38E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_383D")

    ChrTalk(
        0x8,
        (
            "By the way, I often came to the village\x01",
            "A foreigner's uncle\x01",
            "You gave me sweets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've done something chic\x01",
            "I thought I was getting angry ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wow, in the world\x01",
            "I have a kind person.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38E4")

    label("loc_383D")


    ChrTalk(
        0x8,
        (
            "To a foreigner's uncle\x01",
            "I've done something sexy, but,\x01",
            "She gave me sweets, not to be angry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "… … Then again, to my mother\x01",
            "I was scolded overfully though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38E4")

    Jump("loc_3B4C")

    label("loc_38E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_398B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3904")
    Call(0, 10)
    Jump("loc_3986")

    label("loc_3904")


    ChrTalk(
        0x8,
        (
            "Well, same Takaoni\x01",
            "It seems that rules are slightly different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, today is Stefan's\x01",
            "Let's make it cross-bell type Takaoni!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3986")

    Jump("loc_3B4C")

    label("loc_398B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_39FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39A6")
    Call(0, 10)
    Jump("loc_39F9")

    label("loc_39A6")


    ChrTalk(
        0x8,
        (
            "That's right.\x01",
            "Well, the building is like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I'd like to explore once.\x02",
    )

    CloseMessageWindow()

    label("loc_39F9")

    Jump("loc_3B4C")

    label("loc_39FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3B4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD3")

    ChrTalk(
        0x8,
        (
            "Chie, this village is\x01",
            "It's too peaceful and boring ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Speaking of recent news,\x01",
            "\"Cattle in the ranch gave birth to a cod\" or\x01",
            "It is only such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, something major incident\x01",
            "I wonder if it will happen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B4C")

    label("loc_3AD3")


    ChrTalk(
        0x8,
        (
            "Well, indeed the cow's codomo\x01",
            "I was cute, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The big incident I'm seeking,\x01",
            "It is such a peaceful thing\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B4C")

    TalkEnd(0xFE)
    Return()

    # Function_9_3054 end

    def Function_10_3B50(): pass

    label("Function_10_3B50")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3C95")

    ChrTalk(
        0x8,
        (
            "Okay.\x01",
            "Takaoni, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The oni is absolutely high\x01",
            "You should not go up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Pulley, Mr. Oni is good!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Huh? Within 3 seconds\x01",
            "Even if you are in a high place\x01",
            "Is not it okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……what is that.\x01",
            "I heard it for the first time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hey hey hey!\x01",
            "Pulley, Mr. Oni is good!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    Jump("loc_3DD6")

    label("loc_3C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3DD6")

    ChrTalk(
        0xB,
        (
            "By the way, today,\x01",
            "The unveiling ceremony of Orkis Tower in town\x01",
            "I guess I was doing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Orchis Tower?\x01",
            "What is it, do you eat it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "No, no, no.\x01",
            "It's a very big building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Rumor, from the top\x01",
            "Crossbell inside\x01",
            "I can say that I can look around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, great!\x01",
            "I want to go once.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)

    label("loc_3DD6")

    SetScenarioFlags(0x0, 7)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_10_3B50 end

    def Function_11_3DE6(): pass

    label("Function_11_3DE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E6E")

    ChrTalk(
        0xA,
        (
            "Choline,\x01",
            "With Harold Oychan\x01",
            "I got back to town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please come and visit again\x01",
            "I was yak sucking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4479")

    label("loc_3E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4023")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F81")

    ChrTalk(
        0xA,
        (
            "Older brother\x01",
            "Choline Kun all the way\x01",
            "I was boring, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Mother, pulley better\x01",
            "Because I am sister\x01",
            "Let's do a little gaman.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "Pulley, I will endure.\x01",
            "…… Because, sister is ♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_401E")

    label("loc_3F81")


    ChrTalk(
        0xA,
        (
            "Pulley is more than Colin\x01",
            "I'm a little sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even if you are taking pictures\x01",
            "I will endure it.\x01",
            "…… Because, sister is ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_401E")

    Jump("loc_4479")

    label("loc_4023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_40B3")

    ChrTalk(
        0xA,
        (
            "Older brother,\x01",
            "Recently, only Choline\x01",
            "I am caught ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Older brother\x01",
            "Even though she is a pulley's guy ……\x01",
            "Cunning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4479")

    label("loc_40B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_41AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4127")

    ChrTalk(
        0xA,
        (
            "Stephan, in the village earlier\x01",
            "I saw that it came back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I wonder if it will come soon.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_41AA")

    label("loc_4127")


    ChrTalk(
        0xA,
        (
            "For the most part,\x01",
            "With two little brothers and two\x01",
            "I was playing it ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But, after all, Stefan\x01",
            "It would be fun to stay there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41AA")

    Jump("loc_4479")

    label("loc_41AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_41BD")
    Jump("loc_4479")

    label("loc_41BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_42A6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41FF")

    ChrTalk(
        0xA,
        (
            "pulley,\x01",
            "I played a hushster!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42A1")

    label("loc_41FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4268")

    ChrTalk(
        0xA,
        (
            "Nya-nya.\x01",
            "It was a big cat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I was surprised and not cute.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_42A1")

    label("loc_4268")


    ChrTalk(
        0xA,
        (
            "After all the pulley,\x01",
            "I like a little cat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42A1")

    Jump("loc_4479")

    label("loc_42A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4336")

    ChrTalk(
        0xA,
        (
            "Older brother, the other day\x01",
            "To your mother\x01",
            "I was stuck in a butt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Puff.\x01",
            "An ass is like an apple\x01",
            "I was getting scared.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4479")

    label("loc_4336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4381")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4351")
    Call(0, 10)
    Jump("loc_437C")

    label("loc_4351")


    ChrTalk(
        0xA,
        (
            "pulley,\x01",
            "Mr. Onya! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_437C")

    Jump("loc_4479")

    label("loc_4381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_43E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_439C")
    Call(0, 10)
    Jump("loc_43E2")

    label("loc_439C")


    ChrTalk(
        0xA,
        (
            "To your boy\x01",
            "To get him to be swept away,\x01",
            "Which one is expensive?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43E2")

    Jump("loc_4479")

    label("loc_43E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4479")

    ChrTalk(
        0xA,
        (
            "Pulley,\x01",
            "Because there is an old boy\x01",
            "I'm not bored at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "She also has Stephan\x01",
            "It's fun to play.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4479")

    TalkEnd(0xFE)
    Return()

    # Function_11_3DE6 end

    def Function_12_447D(): pass

    label("Function_12_447D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_45FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4561")

    ChrTalk(
        0xB,
        (
            "Well, what mind is tremendous\x01",
            "I think it is a major incident ….\x01",
            "I wonder if you can do such a non-key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, this is the\x01",
            "It is also a nice place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Because of something happening,\x01",
            "I only have to be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_45F8")

    label("loc_4561")


    ChrTalk(
        0xB,
        (
            "Whenever these two people are nothing nonetheless\x01",
            "It's a nice place, though ….\x01",
            "It is a tremendous incidents for running water.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Because of something happening,\x01",
            "I only have to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45F8")

    Jump("loc_4C79")

    label("loc_45FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_471C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46BC")

    ChrTalk(
        0xB,
        (
            "Colin kun, hey\x01",
            "There is a dangerous place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As before, that blued flower is beautiful\x01",
            "I was going out towards the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "We have to look closely well.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4717")

    label("loc_46BC")


    ChrTalk(
        0xB,
        (
            "Colin kun, hey\x01",
            "There is a dangerous place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "We have to look closely well.\x02",
    )

    CloseMessageWindow()

    label("loc_4717")

    Jump("loc_4C79")

    label("loc_471C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_47CB")

    ChrTalk(
        0xB,
        (
            "Harolds, for a while\x01",
            "I'm staying at \"Tonelico Tei\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Also when my mother and I came\x01",
            "It was taken care of in various ways,\x01",
            "People in this village really have a big heart.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C79")

    label("loc_47CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_47D9")
    Jump("loc_4C79")

    label("loc_47D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_47E7")
    Jump("loc_4C79")

    label("loc_47E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_491D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4841")

    ChrTalk(
        0xB,
        (
            "Already, like a prison wrestler\x01",
            "I'm getting bored, but I wish …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4918")

    label("loc_4841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48CA")

    ChrTalk(
        0xB,
        (
            "That uncle, after all\x01",
            "It was a bad guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "No way in the village\x01",
            "To release a demonic beast ……\x01",
            "I thought that I could eat it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4918")

    label("loc_48CA")


    ChrTalk(
        0xB,
        (
            "Even so, to the monster\x01",
            "I was about to be attacked,\x01",
            "This brother and sister is non-ki ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4918")

    Jump("loc_4C79")

    label("loc_491D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_49A6")

    ChrTalk(
        0xB,
        (
            "That old man,\x01",
            "I'm kinda nigga.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You surely smile\x01",
            "It looks kind, but,\x01",
            "Is not my eyes smiling?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C79")

    label("loc_49A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4A4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49C1")
    Call(0, 10)
    Jump("loc_4A48")

    label("loc_49C1")


    ChrTalk(
        0xB,
        (
            "In Crosbell City,\x01",
            "Oni is up to 3 seconds high\x01",
            "It was supposed to be a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Certainly, like this\x01",
            "I say local rule.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A48")

    Jump("loc_4C79")

    label("loc_4A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4B07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A68")
    Call(0, 10)
    Jump("loc_4B02")

    label("loc_4A68")


    ChrTalk(
        0xB,
        (
            "Well, I see.\x01",
            "A big curtain has been lowered until now\x01",
            "Even if I do not know it is not he …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If that curtain took off,\x01",
            "The city is soooooooo\x01",
            "It must have been exciting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B02")

    Jump("loc_4C79")

    label("loc_4B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4C79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BFA")

    ChrTalk(
        0xB,
        (
            "Before, with my mum\x01",
            "In Crossbell City\x01",
            "I lived there … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In Almorika village\x01",
            "Since it began to spend,\x01",
            "Every day is fresh somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Why was that at first\x01",
            "Were they hated?\x01",
            "I do not quite understand myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    SetChrFlags(0xB, 0x10)
    OP_93(0xB, 0x6B, 0x0)
    Jump("loc_4C79")

    label("loc_4BFA")


    ChrTalk(
        0xB,
        (
            "Cow delivery\x01",
            "What is happening in the near future\x01",
            "I think that it is amazing enough ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If I lived in a village\x01",
            "I wonder if it will be natural.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C79")

    TalkEnd(0xFE)
    Return()

    # Function_12_447D end

    def Function_13_4C7D(): pass

    label("Function_13_4C7D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4C8E")
    Jump("loc_53FD")

    label("loc_4C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4DDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D6B")

    ChrTalk(
        0xC,
        (
            "Invalid declaration of independent country … ….\x01",
            "In this village which was originally far away\x01",
            "It will have little effect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "However, due to the sudden change of the situation\x01",
            "Not a few villagers feel uneasy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As I thought, one house in the village\x01",
            "I have to keep it around.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4DD9")

    label("loc_4D6B")


    ChrTalk(
        0xC,
        (
            "To the sudden change of the situation\x01",
            "Not a few villagers feel uneasy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As I thought, one house in the village\x01",
            "I have to keep it around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DD9")

    Jump("loc_53FD")

    label("loc_4DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4F5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EC1")

    ChrTalk(
        0xC,
        (
            "That creepy blue flower ……\x01",
            "A while ago, in the astragalus field\x01",
            "It began to bloom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It seems that it has an influence on flower growth\x01",
            "I'd rather weed out … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Damn, it grows no matter how many times I pulled out.\x01",
            "For now I'm upset.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4F5A")

    label("loc_4EC1")


    ChrTalk(
        0xC,
        (
            "This astragalus field,\x01",
            "Because it is the most important place for the village,\x01",
            "I want to manage that blue flower … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Damn, it grows no matter how many times I pulled out.\x01",
            "For now I'm upset.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F5A")

    Jump("loc_53FD")

    label("loc_4F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_50C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_504F")

    ChrTalk(
        0xC,
        (
            "Since the street attacks,\x01",
            "Look around the village\x01",
            "I started to take turns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As I had such a thing,\x01",
            "No matter where and what happens\x01",
            "It is not strange … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Anyway, to protect the safety of the village\x01",
            "I have to do as much as I can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_50BD")

    label("loc_504F")


    ChrTalk(
        0xC,
        (
            "Look around the village\x01",
            "I started to take turns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To protect the safety of the village\x01",
            "I have to do as much as I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50BD")

    Jump("loc_53FD")

    label("loc_50C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_50D0")
    Jump("loc_53FD")

    label("loc_50D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_50DE")
    Jump("loc_53FD")

    label("loc_50DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_50EC")
    Jump("loc_53FD")

    label("loc_50EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_50FA")
    Jump("loc_53FD")

    label("loc_50FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5282")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51EF")

    ChrTalk(
        0xC,
        (
            "Because of the survival of Almorika village,\x01",
            "Yesterday a variety of reform plans\x01",
            "I suggested to the mayor …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "All were dismissed\x01",
            "After all, the last is as usual\x01",
            "I have quarreled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My father …… The village head,\x01",
            "Current situation in Almorika village\x01",
            "Do not you feel the crisis?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_527D")

    label("loc_51EF")


    ChrTalk(
        0xC,
        (
            "Yesterday a variety of reform plans\x01",
            "I suggested it … …\x01",
            "The village mayor did not acknowledge one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My father …… The village head,\x01",
            "Current situation in Almorika village\x01",
            "Do not you feel the crisis?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_527D")

    Jump("loc_53FD")

    label("loc_5282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_53FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_536A")

    ChrTalk(
        0xC,
        (
            "Recently, both agriculture and pastoralism\x01",
            "I can not say that it is good.\x01",
            "The village's financial situation is tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But the father … … the village mayor,\x01",
            "Still conservative thoughts\x01",
            "I will not try to change it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "… As a next village head,\x01",
            "I have to manage somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_53FD")

    label("loc_536A")


    ChrTalk(
        0xC,
        (
            "For the survival of Almorika village,\x01",
            "It is bound by tradition etc.\x01",
            "Just do not keep it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "… As a next village head,\x01",
            "I have to manage somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53FD")

    TalkEnd(0xFE)
    Return()

    # Function_13_4C7D end

    def Function_14_5401(): pass

    label("Function_14_5401")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_551D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54B4")

    NpcTalk(
        0xD,
        "A good man",
        (
            "This is Armorika Village ……\x01",
            "As you have heard,\x01",
            "It is quite a nice village.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "A good man",
        (
            "Huhu, I will work quickly\x01",
            "Shall I take it for you?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_551D")

    label("loc_54B4")


    NpcTalk(
        0xD,
        "A good man",
        (
            "To work quickly\x01",
            "Let's say you're about to start.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "A good man",
        "Well, the house of the village chief is … …\x02",
    )

    CloseMessageWindow()

    label("loc_551D")

    TalkEnd(0xFE)
    Return()

    # Function_14_5401 end

    def Function_15_5521(): pass

    label("Function_15_5521")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5532")
    Jump("loc_55F5")

    label("loc_5532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_55EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_554D")
    Call(0, 16)
    Jump("loc_55E7")

    label("loc_554D")


    ChrTalk(
        0xE,
        (
            "Huhu, Sophia's sister\x01",
            "When it comes to Choline\x01",
            "It really makes me worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "But it's okay, children\x01",
            "While injured slightly\x01",
            "Because it grows.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55E7")

    Jump("loc_55F5")

    label("loc_55EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_55F5")

    label("loc_55F5")

    TalkEnd(0xFE)
    Return()

    # Function_15_5521 end

    def Function_16_55F9(): pass

    label("Function_16_55F9")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xF,
        "#03708FCollin, I wonder if it is okay … (fidget)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hehe, Sophia.\x01",
            "You do not have to worry about that so be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Stefan,\x01",
            "At first it was a bean sprout\x01",
            "I was worried … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Because children are strong,\x01",
            "A bit of a banging play\x01",
            "I think you should do better.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 500)

    ChrTalk(
        0xF,
        (
            "#03700FThat's right.\x01",
            "If I am overprotective,\x01",
            "I will not be able to enjoy Collin … …\x02",
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

    # Function_16_55F9 end

    def Function_17_5786(): pass

    label("Function_17_5786")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5797")
    Jump("loc_584A")

    label("loc_5797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5833")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57B2")
    Call(0, 16)
    Jump("loc_582E")

    label("loc_57B2")


    ChrTalk(
        0xF,
        (
            "#03700F…… I am too well protected\x01",
            "It may not be good.\x02\x03",
            "#03709FBecause Colin, so much\x01",
            "It looks like fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_582E")

    Jump("loc_584A")

    label("loc_5833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_5841")
    Jump("loc_584A")

    label("loc_5841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_584A")

    label("loc_584A")

    TalkEnd(0xFE)
    Return()

    # Function_17_5786 end

    def Function_18_584E(): pass

    label("Function_18_584E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_585F")
    Jump("loc_58FC")

    label("loc_585F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_58E5")

    ChrTalk(
        0x10,
        (
            "#03800FWith lots of friends\x01",
            "It's fun to play!\x02\x03",
            "#03809FNext time Sanaita also\x01",
            "Should I bring you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58FC")

    label("loc_58E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_58F3")
    Jump("loc_58FC")

    label("loc_58F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_58FC")

    label("loc_58FC")

    TalkEnd(0xFE)
    Return()

    # Function_18_584E end

    def Function_19_5900(): pass

    label("Function_19_5900")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BD9")

    ChrTalk(
        0xFE,
        (
            "This \"a prelima grass\" of the astragalus field\x01",
            "I'm looking for a way to do something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that it grows soon even if it is pulled out … …\x01",
            "I hope I managed to eradicate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI agree……\x01",
            "It will cause the appearance of \"Phantom beast\"\x01",
            "It seems better to deal with the top priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, I will try various things for the time being.\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "That's right, by all means to you,\x01",
            "There is something I want you to hear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… In fact, next time, with my fiancé pearl\x01",
            "Make a wedding ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because this is the situation, in Pearl\x01",
            "I still do not keep it … …\x01",
            "I have just started making arrangements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102Foh dear……\x01",
            "Congratulations, Huhu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, this is the time\x01",
            "Trying to have something to protect\x01",
            "Please think again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once the date for the formula is decided\x01",
            "Because you also invite,\x01",
            "Come by all means.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BB, 1)
    Jump("loc_5C85")

    label("loc_5BD9")


    ChrTalk(
        0xFE,
        (
            "Let me wait long in Pearl\x01",
            "I'm sorry, but …\x01",
            "I decided to name my wedding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order to protect her,\x01",
            "As a Crossbell hypocrite\x01",
            "I hope to further improve.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C85")

    TalkEnd(0xFE)
    Return()

    # Function_19_5900 end

    def Function_20_5C89(): pass

    label("Function_20_5C89")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D54")

    ChrTalk(
        0x26,
        (
            "For a while\x01",
            "After sightseeing here\x01",
            "Let's go back to Libert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "No matter how much you say a thank you guys\x01",
            "That's enough to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Things that made me reunite with my father,\x01",
            "Thank you again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_5DC8")

    label("loc_5D54")


    ChrTalk(
        0x26,
        (
            "No matter how much you say a thank you guys\x01",
            "That's enough to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Things that made me reunite with my father,\x01",
            "Thank you again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DC8")

    TalkEnd(0xFE)
    Return()

    # Function_20_5C89 end

    def Function_21_5DCC(): pass

    label("Function_21_5DCC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E63")

    ChrTalk(
        0xFE,
        (
            "Uhufu, too, Armin\x01",
            "Meet your father\x01",
            "I'm really happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ouchi\x01",
            "I'm glad you made it.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "baby",
        "Happy.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_5EC5")

    label("loc_5E63")


    ChrTalk(
        0xFE,
        (
            "O toyoshi, to your father in the future\x01",
            "Let's go to a greeting again ~ Ne\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "baby",
        "Happy.\x02",
    )

    CloseMessageWindow()

    label("loc_5EC5")

    TalkEnd(0xFE)
    Return()

    # Function_21_5DCC end

    def Function_22_5EC9(): pass

    label("Function_22_5EC9")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EFB")
    SetScenarioFlags(0x31, 2)

    label("loc_5EFB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_5F3B")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F30")
    Sound(2499, 255, 100, 0)
    Jump("loc_5F36")

    label("loc_5F30")

    Sound(3537, 255, 100, 0)

    label("loc_5F36")

    Jump("loc_5F41")

    label("loc_5F3B")

    Sound(3344, 255, 100, 0)

    label("loc_5F41")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_5FBA")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Mercapa")
    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5F9A"),
        (SWITCH_DEFAULT, "loc_5FAB"),
    )


    label("loc_5F9A")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_5FB5")

    label("loc_5FAB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5FB5")

    Jump("loc_61F9")

    label("loc_5FBA")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Travel with a driving car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_5FEE")
    MenuCmd(1, 0, "Take a break with a driving car")

    label("loc_5FEE")

    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6022"),
        (1, "loc_6126"),
        (2, "loc_61B7"),
        (SWITCH_DEFAULT, "loc_61EF"),
    )


    label("loc_6022")

    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_6053")
    OP_70(0x8, 0x12C)
    OP_71(0x8, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_6063")

    label("loc_6053")

    OP_70(0x8, 0xF0)
    OP_71(0x8, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_6063")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60B9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60B9")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60DC")
    Sound(461, 0, 100, 0)

    label("loc_60DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_60FC")
    OP_70(0x8, 0x14A)
    OP_71(0x8, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_610C")

    label("loc_60FC")

    OP_70(0x8, 0x10E)
    OP_71(0x8, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_610C")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x8, "light", 0x1, 0x1)
    OP_70(0x8, 0x0)
    Jump("loc_5F41")

    label("loc_6126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_6198")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_615B")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_6173")

    label("loc_615B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_616E")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_6173")

    label("loc_616E")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_6173")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61B2")

    label("loc_6198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_61A8")
    OP_AF(0xFB)
    Jump("loc_61B2")

    label("loc_61A8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_61B2")

    Jump("loc_61F9")

    label("loc_61B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61D0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61EA")

    label("loc_61D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_61E0")
    OP_AF(0xFB)
    Jump("loc_61EA")

    label("loc_61E0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_61EA")

    Jump("loc_61F9")

    label("loc_61EF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_61F9")

    Jump("loc_5F41")

    label("loc_61FE")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_22_5EC9 end

    def Function_23_620C(): pass

    label("Function_23_620C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6254")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The guiding bus seems to be out of service.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_6254")

    Call(0, 3)
    Return()

    # Function_23_620C end

    def Function_24_6258(): pass

    label("Function_24_6258")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FI'm going to catch you here.\x02",
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
            "Do you fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "To fish\x01",      # 0
            "quit\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6327")
    OP_E2(0x2)
    MiniGame(0x6, 0x1B, 0x300C, 0x0, 0x1478, 0xB4, 0x2A8A, 0xFFFFFA56, 0x4BA)

    label("loc_6327")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_24_6258 end

    def Function_25_632C(): pass

    label("Function_25_632C")

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

    # Function_25_632C end

    def Function_26_656E(): pass

    label("Function_26_656E")

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
            "#6P#00005FEven so ……\x01",
            "You have a pretty gallery.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_67BC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_67BC)
    Sleep(50)

    def lambda_67CC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_67CC)

    def lambda_67D9():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_67D9)
    Sleep(50)

    def lambda_67E9():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_67E9)

    def lambda_67F6():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_67F6)
    Sleep(50)

    def lambda_6806():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6806)
    Sleep(300)

    ChrTalk(
        0x18,
        (
            "#12POh, apparently\x01",
            "It seems that the story has spread.\x02",
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
        "#5PHello, you're invincible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PPolice station,\x01",
            "I do not know what to call.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    ChrTalk(
        0xA,
        (
            "#11PChicho?\x01",
            "Wait a minute, what is it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    ChrTalk(
        0xB,
        (
            "#5PWell, that is\x01",
            "I mean you will not be a partner.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x96, 0x1F4)

    ChrTalk(
        0xB,
        (
            "#5PBut how about you?\x01",
            "Older brothers of mission support department\x01",
            "I think it will do quite a bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x96, 0x1F4)

    ChrTalk(
        0x9,
        "#5PHuh, Bari Bali Come on fire!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x1D, 500)

    ChrTalk(
        0x9,
        (
            "#11PHey, the village mayor\x01",
            "Which do you think I have a minute?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#5PHmm, that's right ……\x01",
            "From both of usual\x01",
            "Because I am indebted to you.\x02",
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
        "#12P#00106FWell, to the mayor …\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x19,
        (
            "#12PI mean,\x01",
            "The story of the meeting is only for the village mayor\x01",
            "I did not do that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FWho should be called the countryside?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FOh, the surroundings of information is horribly early.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112FHaha ……\x01",
            "I am getting nervous again in a different way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#12PHehuu, well sometimes\x01",
            "Is not this something good too?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0xEE, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x18,
        (
            "#11PWell, immediately\x01",
            "I'd like to go and get together.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6C01():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C01)
    Sleep(50)

    def lambda_6C11():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C11)

    def lambda_6C1E():
        OP_93(0xFE, 0xEE, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6C1E)
    Sleep(50)

    def lambda_6C2E():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C2E)
    Sleep(50)

    def lambda_6C3E():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6C3E)
    Sleep(50)

    def lambda_6C4E():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6C4E)
    Sleep(300)

    ChrTalk(
        0x18,
        "#11PFirst we have to decide the format.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PWell, the pattern is\x01",
            "I think that there are various things … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PAs I thought it was a pair of two people#8RTwo Mansell#-\x01",
            "It's a 2: 2 battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#5POh, me too\x01",
            "I want to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PIs that okay there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FYes, it is the request of the two of you,\x01",
            "There is no problem, but …\x02\x03",
            "#00000FWho is going out?\x01",
            "Is it OK to decide here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11POh, I'll leave it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PHowever Lloyd,\x01",
            "Only you are determined and asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FHuh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell, so much\x01",
            "It is not surprising, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PApart from us\x01",
            "Only personal physical ability\x01",
            "I do not want to see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PCentering on Lloyd\x01",
            "Unity of Support Office Division … …\x01",
            "I want you to show it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Oh yes, but\x01",
            "There is no critical leader\x01",
            "There is no point?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FHaha …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FDamn, Lloyd's guy …!\x02\x03",
            "From such a wonderful older sister\x01",
            "What is required as well …! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHuh, I see.\x01",
            "This is the rumor brother noblemen.\x02",
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
            "#6P#00006FSomehow, an unfair comment\x01",
            "I think I heard it ….\x01",
            "whatever.\x02\x03",
            "#00000FTentatively,\x01",
            "I understand that kind of thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWell then,\x01",
            "Who is Lloyd's Partner\x01",
            "I wonder if you choose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FOh, I see. …\x02",
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
            "Fight with Ellie\x01",        # 0
            "Fight with Randy\x01",      # 1
            "Fight with Noel\x01",        # 2
            "Fight with Wadi\x01",          # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_726B")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x1)
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#5P#00000FErie, may I ask you a favor?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#00104FHehe, of course.\x02\x03",
            "#00102FOur combination ……\x01",
            "Let 's see two people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74C9")

    label("loc_726B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_732D")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x2)
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#5P#00000FRandy, can you ask me?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#12P#00309FOh yes, of course!\x02\x03",
            "#00300FOur collaboration skills ……\x01",
            "Let 's hit the elder sister.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74C9")

    label("loc_732D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73F7")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x3)
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#00000FNoel, can I ask you a favor?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10109FYes, of course!\x02\x03",
            "#10100FOur Combi Craft ……\x01",
            "Let's hit each other!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74C9")

    label("loc_73F7")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x75, 0x1, 0x4)
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#00000FWadi, will you fight with me?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#6P#10304FHuh, I'd be happy if you asked for it.\x02\x03",
            "#10302FOur cooperation#4Rduet#So, your older sisters\x01",
            "Let me show you what I am saying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74C9")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_32(0xFF, 0xFA, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7502")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_755A")

    label("loc_7502")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7526")
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_755A")

    label("loc_7526")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_754A")
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_755A")

    label("loc_754A")

    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_755A")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(8610, 1700, -21420, 0)
    MoveCamera(4, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12790, 0)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75FB")
    SetChrPos(0x104, 13650, 0, -14300, 225)
    SetChrPos(0x109, 14800, 0, -14550, 225)
    SetChrPos(0x105, 13100, 0, -12850, 225)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_76EF")

    label("loc_75FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7653")
    SetChrPos(0x102, 13650, 0, -14300, 225)
    SetChrPos(0x109, 14800, 0, -14550, 225)
    SetChrPos(0x105, 13100, 0, -12850, 225)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_76EF")

    label("loc_7653")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76AB")
    SetChrPos(0x102, 13650, 0, -14300, 225)
    SetChrPos(0x104, 14800, 0, -14550, 225)
    SetChrPos(0x105, 13100, 0, -12850, 225)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_76EF")

    label("loc_76AB")

    SetChrPos(0x102, 13650, 0, -14300, 225)
    SetChrPos(0x104, 14800, 0, -14550, 225)
    SetChrPos(0x109, 13100, 0, -12850, 225)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_76EF")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x19,
        "#11PI have decided!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PBoth of them hold their weapons.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(10960, 1000)
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_776D")
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_77B3")

    label("loc_776D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7789")
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x0)
    Jump("loc_77B3")

    label("loc_7789")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77AB")
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_77B3")

    label("loc_77AB")

    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)

    label("loc_77B3")

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
        "#4S#11PWell, let's go!\x02",
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7820")
    SetChrBattleFlags(0x104, 0x8)
    SetChrBattleFlags(0x109, 0x8)
    SetChrBattleFlags(0x105, 0x8)
    Jump("loc_7875")

    label("loc_7820")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7843")
    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x109, 0x8)
    SetChrBattleFlags(0x105, 0x8)
    Jump("loc_7875")

    label("loc_7843")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7866")
    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x104, 0x8)
    SetChrBattleFlags(0x105, 0x8)
    Jump("loc_7875")

    label("loc_7866")

    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x104, 0x8)
    SetChrBattleFlags(0x109, 0x8)

    label("loc_7875")

    Battle("BattleInfo_774", 0x30200011, 0x0, 0x0, 0xE, 0xFF)
    FadeToDark(0, 0, -1)
    ClearChrBattleFlags(0x102, 0x8)
    ClearChrBattleFlags(0x104, 0x8)
    ClearChrBattleFlags(0x109, 0x8)
    ClearChrBattleFlags(0x105, 0x8)
    Return()

    # Function_26_656E end

    def Function_27_78A4(): pass

    label("Function_27_78A4")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F14")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x3)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AA9")
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrSubChip(0x102, 0x3)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_7BB5")

    label("loc_7AA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B09")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x3)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_7BB5")

    label("loc_7B09")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B69")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrSubChip(0x109, 0x3)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_7BB5")

    label("loc_7B69")

    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x105, 0x3)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_7BB5")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#00006FHa Ha … … no dame! Is it?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C34")

    ChrTalk(
        0x102,
        (
            "#6P#00106FSomething like that …\x01",
            "I was not serious … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF8")

    label("loc_7C34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C83")

    ChrTalk(
        0x104,
        (
            "#6P#00306FOh, the other side\x01",
            "Even if I do not mind full power … ….!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF8")

    label("loc_7C83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CCE")

    ChrTalk(
        0x109,
        (
            "#6P#10106FCut … … perfectly\x01",
            "I misplaced himself … …!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF8")

    label("loc_7CCE")


    ChrTalk(
        0x105,
        "#6P#10306FWhew … … you guarded … …\x02",
    )

    CloseMessageWindow()

    label("loc_7CF8")


    ChrTalk(
        0x18,
        (
            "#11PHow about this degree … No.\x01",
            "It is a bit drastic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PWell, a little more\x01",
            "I thought you would do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell, the combat experience in the combination\x01",
            "Is not it still shallow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell, next time the team\x01",
            "I'm going to be headed by the whole.\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E93")
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Jump("loc_7F0F")

    label("loc_7E93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EC3")
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    Jump("loc_7F0F")

    label("loc_7EC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EF3")
    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    Jump("loc_7F0F")

    label("loc_7EF3")

    Fade(500)
    Sound(802, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    label("loc_7F0F")

    Jump("loc_8541")

    label("loc_7F14")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F8D")
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_8099")

    label("loc_7F8D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FED")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_8099")

    label("loc_7FED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_804D")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_8099")

    label("loc_804D")

    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_8099")

    SetChrChipByIndex(0x18, 0x30)
    SetChrSubChip(0x18, 0x3)
    SetChrChipByIndex(0x19, 0x31)
    SetChrSubChip(0x19, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#00000FHave you done it …?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_813A")

    ChrTalk(
        0x102,
        (
            "#6P#00102FYeah …\x01",
            "He was handling over there\x01",
            "It looks like it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_8247")

    label("loc_813A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8197")

    ChrTalk(
        0x104,
        (
            "#6P#00304FWell, over there\x01",
            "It seems not to be my best effort,\x01",
            "It's like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_8247")

    label("loc_8197")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81FE")

    ChrTalk(
        0x109,
        (
            "#6P#10104FYes, but …\x01",
            "The two of you were hand-dropping\x01",
            "It looks like it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_8247")

    label("loc_81FE")


    ChrTalk(
        0x105,
        (
            "#6P#10304FOh, but\x01",
            "The two were not serious\x01",
            "It looks like it.\x02",
        )
    )

    OP_57(0x0)
    OP_5A()
    CloseMessageWindow()

    label("loc_8247")

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
            "#11PHehe, I was surprised.\x01",
            "You do quite well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PYeah yeah, more than I thought\x01",
            "I was surprised to see my breath in breath.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00012FHaha … … I can afford it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PHuhu, it is true that I pulled out my hand\x01",
            "I can not afford that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell, anyway\x01",
            "I got a good one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FWell … with this\x01",
            "Is it okay to finish training?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PHehe, well so\x01",
            "Do not be impatient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11POh yeah, this is\x01",
            "Lloyd, are you indigestion too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FWell, there is not such a thing ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PHey, what are you refraining from.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PThat's right, next time we\x01",
            "Two people and the Special Affairs Support Division,\x01",
            "I will ask you for this confrontation.\x02",
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

    label("loc_8541")


    def lambda_8546():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8546)
    Sleep(50)

    def lambda_8556():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8556)
    Sleep(50)

    def lambda_8566():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8566)
    Sleep(50)

    def lambda_8576():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8576)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00005FOh, are we with five people?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FAs expected, all of us are lonesided\x01",
            "Is it a hard work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PHuhu, that's why\x01",
            "You're going to be training!\x02",
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
        "#11P#4SBreach#2RIs#It is!\x02",
    )

    CloseMessageWindow()
    Sound(620, 0, 100, 0)
    Sound(832, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 9600, 0, -18150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(
        0x102,
        "#6P#00105FAmazing … … the power is#2RBleak#I have it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FWhat is \"Qigong\" in Oriental martial arts?\x02\x03",
            "#00301F…… It sounds awkward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PWell, it is truly familiar.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11P- Eolia!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#11Proger that!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_8770():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8770)
    Sleep(50)

    def lambda_8780():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8780)
    Sleep(50)

    def lambda_8790():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8790)
    Sleep(50)

    def lambda_87A0():
        OP_93(0xFE, 0x3A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_87A0)
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
        "#6P#10105Fthis is……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHuhu, everyone in this\x01",
            "It is a perfect recovery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PCan you fight this without heart?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PNow, you guys!\x01",
            "Do not wait and do not stand!\x02",
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
        "#6P#00300FYou seem to have no choice but to do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FLloyd …\x01",
            "Who is going to support?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FAh……\x02",
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
            "Turn Ellie into support\x01",        # 0
            "Turn Randy into support\x01",      # 1
            "Turn Noel into support\x01",        # 2
            "Turning Wadi into support\x01",          # 3
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A05")
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_8A5D")

    label("loc_8A05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A29")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_8A5D")

    label("loc_8A29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A4D")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    Jump("loc_8A5D")

    label("loc_8A4D")

    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_8A5D")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AF8")
    SetChrPos(0x104, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrPos(0x102, 8330, 0, -21320, 58)
    Jump("loc_8BEC")

    label("loc_8AF8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B50")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x109, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrPos(0x104, 8330, 0, -21320, 58)
    Jump("loc_8BEC")

    label("loc_8B50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BA8")
    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x105, 4019, 0, -22360, 55)
    SetChrPos(0x109, 8330, 0, -21320, 58)
    Jump("loc_8BEC")

    label("loc_8BA8")

    SetChrPos(0x102, 4190, 0, -20390, 55)
    SetChrPos(0x104, 5920, 0, -22950, 55)
    SetChrPos(0x109, 4019, 0, -22360, 55)
    SetChrPos(0x105, 8330, 0, -21320, 58)

    label("loc_8BEC")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C50")

    ChrTalk(
        0x101,
        "#6P#00000FEly, ask for support!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FYeah, OK!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D5E")

    label("loc_8C50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CB8")

    ChrTalk(
        0x101,
        "#6P#00000FRandy, please go to support!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00300FIt is an intervention that is perfectly conscious!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D5E")

    label("loc_8CB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D18")

    ChrTalk(
        0x101,
        "#6P#00000FNoel, I left the support to you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FYes, sir!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D5E")

    label("loc_8D18")


    ChrTalk(
        0x101,
        "#6P#00000FWadi, I will leave the support!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FHuh, okay!\x02",
    )

    CloseMessageWindow()

    label("loc_8D5E")


    ChrTalk(
        0x18,
        "#4S#11P--will go!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_7B8", 0x30200011, 0x0, 0x100, 0xE, 0xFF)
    FadeToDark(0, 0, -1)
    StopEffect(0x0, 0x0)
    Return()

    # Function_27_78A4 end

    def Function_28_8D98(): pass

    label("Function_28_8D98")

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

    # Function_28_8D98 end

    def Function_29_8F64(): pass

    label("Function_29_8F64")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96C4")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x3)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_917E")
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
    Jump("loc_92D2")

    label("loc_917E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91F6")
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
    Jump("loc_92D2")

    label("loc_91F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_926E")
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
    Jump("loc_92D2")

    label("loc_926E")

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

    label("loc_92D2")

    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#00006FHaa, Haa, Haa ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FHow rude …… No way\x01",
            "Going with everyone and being an enemy is … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10108FIt is our complete defeat ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PFuu … As expected\x01",
            "This time as well this time\x01",
            "I thought it was dull.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PYeah, somehow\x01",
            "I got the winners picked up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#11PIs this also a single experience difference?\x02",
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
        "#6P#00002FAh……\x02",
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
            "#6P#00105FThe damage until a while ago\x01",
            "It is completely gone ……\x02\x03",
            "#00102FIt's a really amazing recovery technology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FBut on top of being killed\x01",
            "I had you recover …\x02\x03",
            "#00306FHaha, I can not feel compassion as a man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PI'm sorry.\x01",
            "I wonder if it was unnecessary care?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00309FWell, there's no tedemo!\x02\x03",
            "#00300FMr. Eoria's\x01",
            "I do not want to be caught by warm arts\x01",
            "Such a happiness, there is no other!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FLa, Randy-senior … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHaha, until a while ago\x01",
            "Where are you going to pride?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FHaa, exactly ….\x01",
            "I am lacking in tension\x01",
            "What?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CE3")

    label("loc_96C4")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 6950, 0, -19870, 58)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9755")
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
    Jump("loc_98A9")

    label("loc_9755")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97CD")
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
    Jump("loc_98A9")

    label("loc_97CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9845")
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
    Jump("loc_98A9")

    label("loc_9845")

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

    label("loc_98A9")

    SetChrChipByIndex(0x18, 0x30)
    SetChrSubChip(0x18, 0x3)
    SetChrChipByIndex(0x19, 0x31)
    SetChrSubChip(0x19, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#00006FHaa, Haa ……\x01",
            "Did you finish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FOh, somehow.\x02\x03",
            "#00302FHowever, against these five people\x01",
            "So far,\x01",
            "Even tons can not be totally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104FYeah, really … ….\x01",
            "I did not miss it until the end.\x02",
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
        (
            "#11PFuu …\x01",
            "Was it inevitable?\x02",
        )
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
            "#11PIf you do well, a little more\x01",
            "I thought I could go on … but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PWell, whatever you say\x01",
            "Afterwards, there is no use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PYou were really strong.\x01",
            "This time it is our perfection.\x02",
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
        "#6P#00005FAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102Fgreat……\x02\x03",
            "The damage until a while ago\x01",
            "It's gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FTo Eolia's recovery arts\x01",
            "It is taken twice a day … …\x01",
            "It is just a comfort rising in the sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#11PThank you, Randy.\x02",
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
            "#11PWell then, to be able to handle it for the third time\x01",
            "Would you try attacking again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FWell, that's the only thing I can do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHuff, this time in the real sense\x01",
            "You may ascend to heaven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FWow, Wazi ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#6P#00106FHaa, exactly ….\x01",
            "I am lacking in tension\x01",
            "What?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    OP_0D()

    label("loc_9CE3")


    ChrTalk(
        0x18,
        (
            "#11PHaha, you are the best for you.\x01",
            "I do not get tired of watching it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00012FWell, thanks.\x02",
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
            "#12PYeah yeah, the meeting is\x01",
            "This is the end.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x1D, 500)
    Sleep(300)

    ChrTalk(
        0x19,
        (
            "#12POh yeah, even if you wait any longer\x01",
            "I can not see interesting things.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9E0F():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9E0F)
    Sleep(50)

    def lambda_9E1F():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9E1F)
    Sleep(50)

    def lambda_9E2F():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9E2F)
    Sleep(50)

    def lambda_9E3F():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9E3F)
    Sleep(50)

    def lambda_9E4F():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9E4F)
    Sleep(300)

    ChrTalk(
        0x1D,
        (
            "#5PHmm, if that's the case\x01",
            "We will dissolve here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#5PEveryone has work.\x01",
            "Well, the break is over.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1D, 500)
    Sleep(300)

    ChrTalk(
        0x1B,
        "#11PHaha, that's understand.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x1A,
        "#11PLook, everyone will go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PIndeed, it was a good fight!\x02",
    )

    CloseMessageWindow()
    OP_68(7360, 1500, -16890, 5000)
    MoveCamera(20, 25, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(16070, 5000)

    def lambda_9F75():
        OP_95(0xFE, 8600, 0, -6460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9F75)
    Sleep(50)

    def lambda_9F92():
        OP_95(0xFE, -2960, 0, -6890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_9F92)
    Sleep(50)

    def lambda_9FAF():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_9FAF)
    Sleep(1000)

    def lambda_9FCC():
        OP_95(0xFE, 1980, 0, -8140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_9FCC)
    Sleep(50)

    def lambda_9FE9():
        OP_95(0xFE, -470, 0, -11050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9FE9)
    Sleep(50)

    def lambda_A006():
        OP_95(0xFE, 280, 0, -10190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A006)
    Sleep(50)

    def lambda_A023():
        OP_95(0xFE, 1220, 0, -9620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A023)
    Sleep(1200)

    def lambda_A040():
        OP_95(0xFE, 3110, 0, -9910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_A040)
    WaitChrThread(0x9, 1)

    def lambda_A05E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A05E)
    WaitChrThread(0x8, 1)

    def lambda_A06F():
        OP_95(0xFE, -5810, 0, -6140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A06F)
    WaitChrThread(0xA, 1)

    def lambda_A08D():
        OP_95(0xFE, -5250, 0, -4930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A08D)
    WaitChrThread(0xB, 1)

    def lambda_A0AB():
        OP_95(0xFE, -4680, 0, -3550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A0AB)
    WaitChrThread(0x1A, 1)

    def lambda_A0C9():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_A0C9)
    WaitChrThread(0x1B, 1)

    def lambda_A0E7():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_A0E7)
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
            "#12POh, that and the village chief.\x01",
            "Have the place to use\x01",
            "Thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#12PThanks to that, it was a good training.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#5PNo,\x01",
            "If it says that, that's it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#5PI will take care of you for you,\x01",
            "Also say anything any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "#5PWell then.\x02",
    )

    CloseMessageWindow()

    def lambda_A225():
        OP_95(0xFE, -5310, 0, -1160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A225)
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
            "#6P#00009FHaha.\x01",
            "It is said that I will be pleased so much\x01",
            "I did not think.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x18, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00005FBut, Mr. Lynn ……\x01",
            "The content of the essential meeting is\x01",
            "how was it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A31A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A31A)
    Sleep(50)

    def lambda_A32A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_A32A)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A383")

    def lambda_A346():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A346)
    Sleep(50)

    def lambda_A356():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A356)
    Sleep(50)

    def lambda_A366():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A366)
    Sleep(50)

    def lambda_A376():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A376)
    Jump("loc_A462")

    label("loc_A383")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3D4")

    def lambda_A397():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A397)
    Sleep(50)

    def lambda_A3A7():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A3A7)
    Sleep(50)

    def lambda_A3B7():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A3B7)
    Sleep(50)

    def lambda_A3C7():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A3C7)
    Jump("loc_A462")

    label("loc_A3D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A425")

    def lambda_A3E8():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A3E8)
    Sleep(50)

    def lambda_A3F8():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A3F8)
    Sleep(50)

    def lambda_A408():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A408)
    Sleep(50)

    def lambda_A418():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A418)
    Jump("loc_A462")

    label("loc_A425")


    def lambda_A42A():
        OP_93(0xFE, 0x10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A42A)
    Sleep(50)

    def lambda_A43A():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A43A)
    Sleep(50)

    def lambda_A44A():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A44A)
    Sleep(50)

    def lambda_A45A():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A45A)

    label("loc_A462")

    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A5C9")
    OP_2C(0x75, 0x2)
    OP_29(0x75, 0x1, 0x5)

    ChrTalk(
        0x18,
        (
            "#11POh, everyone\x01",
            "Being more tougher than I thought\x01",
            "I was surprised to surprise you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PIs the result of training a great part, either?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PHuhu, but neither of us\x01",
            "Because leaving the defeat is not a hobby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PAlso someday\x01",
            "I will get revenge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes, if there is an opportunity\x01",
            "Please do come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00309FEvery time I am OK\x02",
    )

    CloseMessageWindow()
    Jump("loc_A764")

    label("loc_A5C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A6B3")
    OP_29(0x75, 0x1, 0x6)

    ChrTalk(
        0x18,
        (
            "#11PThat's right.\x01",
            "It got even better training … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PWell, hey\x01",
            "It might be enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006FTherefore, it is not a face.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PWell, there were still results.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A764")

    label("loc_A6B3")

    OP_2C(0x75, 0x1)
    OP_29(0x75, 0x1, 0x7)

    ChrTalk(
        0x18,
        (
            "#11POh, everyone did it well\x01",
            "It is enough for training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PYeah yeah, if I had the chance\x01",
            "I want to ask you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYeah, certainly please when that happens.\x02",
    )

    CloseMessageWindow()

    label("loc_A764")

    OP_29(0x75, 0x1, 0x8)

    ChrTalk(
        0x18,
        (
            "#11PAfter all,\x01",
            "Each battle style is near at hand\x01",
            "I wonder if what was seen was harvest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PEspecially Lloyd.\x01",
            "For me, your thtonfer technique\x01",
            "It was quite interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PI am teaching at the police.\x01",
            "Is it kind of suppression technique?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes, you know well.\x02\x03",
            "#00005FBut what is interesting … …?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x18, 500)

    ChrTalk(
        0x104,
        (
            "#6P#00304FOh no, I do not like Tonfa,\x01",
            "Originally it was transmitted from the east.\x02\x03",
            "#00305FYou can also handle Lin's?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PWell, as it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11POther rings#6REnglish prince#And the three tribe club -\x01",
            "What is called Oriental armor\x01",
            "I handled it all in one's school days ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PFrom that point of view I say\x01",
            "Lloyd, your rotation skill is\x01",
            "Perhaps it could be.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00005FI mean to break … technique\x01",
            "Does that mean it will be more powerful?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PWell, it's possibilities to the last.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PAs long as you are good,\x01",
            "You can do it on this occasion ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PWhat would you like to try?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00002FYes, if you can tell me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#11POkay, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PRin says things to people,\x01",
            "It is seldom a thing.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x19, 500)

    ChrTalk(
        0x104,
        (
            "#6P#00309FI am Mr. Eoria\x01",
            "I want to have various guides.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#11PWhy, pass?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FHiking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FRandy senpai, you do not understand.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00006FEveryone, sorry ….\x02\x03",
            "#00000FThat's what it is,\x01",
            "May I take some time?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ACA2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ACA2)
    Sleep(50)

    def lambda_ACB2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ACB2)
    Sleep(50)

    def lambda_ACC2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ACC2)
    Sleep(50)

    def lambda_ACD2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ACD2)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#00100FWell, it's a great opportunity,\x01",
            "You should not tell me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHuh, then we are\x01",
            "I wonder if you will see the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FGood luck, Mr. Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00300FOh, please put it in for me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00012FOh, ah ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell then, at that point\x01",
            "Shall we start?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00000FPlease!\x02",
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
            "#6P#00000FWell, now\x01",
            "Was it nice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11POh, it is enough to pass.\x02",
    )

    CloseMessageWindow()
    OP_68(7310, 1400, -21350, 2000)
    MoveCamera(12, 19, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(14340, 2000)

    def lambda_AFDD():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_AFDD)
    Sleep(50)

    def lambda_AFF5():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AFF5)
    Sleep(50)

    def lambda_B00D():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_B00D)

    def lambda_B022():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B022)
    Sleep(50)

    def lambda_B03A():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B03A)
    Sleep(50)

    def lambda_B052():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B052)
    WaitChrThread(0x105, 1)
    OP_6F(0x10)

    ChrTalk(
        0x18,
        (
            "#11PAfterwards if you use it in actual battle,\x01",
            "You can do things quickly.\x02",
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
            "#6P#00000FWell, it was good …\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FHuh, you did it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FMr. Lloyd, cheers for good work.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x101, 0xFA, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#00000FOh, thank you.\x02\x03",
            "#00003FBut it is amazing …\x01",
            "One type, so much\x01",
            "Is it a way to change the way power is transmitted?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PHuhu, I taught you now\x01",
            "To a type commonly called \"helix\"\x01",
            "It is one of the standing categories.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x3A, 0x1F4)

    ChrTalk(
        0x18,
        (
            "#11PUsed by Arios\x01",
            "It is also adopted as \"Hachiba 1 sword flow\"\x01",
            "It is, so to speak, a form of martial arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PIt is all basic and applied as well\x01",
            "The technique derived from this type,\x01",
            "There are as many stars as that … but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PThose who control \"helix\" and who do \"no\"\x01",
            "Ultimate of all martial arts to reach point,\x01",
            "It is said that it leads to \"a reason\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FNothing in the spiral, is it \"logical\" … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell, as you know this area\x01",
            "It is not understood,\x01",
            "I will keep this lecture as far as I can … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PClosing place, \"What is it\"\x01",
            "Even if it takes a lifetime for an ordinary man, he can not reach\x01",
            "It's like the master of a guru.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PThose who have reached that point\x01",
            "If there are only a few people on the continent\x01",
            "It is being told.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FA few people on the continent …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FAlthough I have heard about rumors,\x01",
            "It's really ridiculous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11PHaha, indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell, I will not tell you to \"fantasy\"\x01",
            "It is to continue to devote from the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FYeah, I got it!\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x18,
        (
            "#11POops, while doing it\x01",
            "The next time came close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PYeah, a bit to each other\x01",
            "I feel bad if I do not hurry.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B60C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B60C)
    Sleep(50)

    def lambda_B61C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B61C)
    Sleep(300)

    ChrTalk(
        0x102,
        "#6P#00100FAfter all I am very busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11POh, especially now at the commerce meeting\x01",
            "Thanks a lot and tight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PThat's why Michelle\x01",
            "Shift is important, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#11PNow it's in minutes\x01",
            "I'm carved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FWell, that is outrageous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PHehuu, though\x01",
            "Although I am resting moderately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell then we will be rude,\x01",
            "Everyone should keep going for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#11PSee you again, Lloyd guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes, thankyou\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16340, 3000)

    def lambda_B80D():
        OP_95(0xFE, 17370, 0, -27500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_B80D)
    Sleep(50)

    def lambda_B82A():
        OP_95(0xFE, 17370, 0, -27500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_B82A)

    def lambda_B844():

        label("loc_B844")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B844")

    QueueWorkItem2(0x101, 1, lambda_B844)
    Sleep(50)

    def lambda_B859():

        label("loc_B859")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B859")

    QueueWorkItem2(0x102, 1, lambda_B859)
    Sleep(50)

    def lambda_B86E():

        label("loc_B86E")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B86E")

    QueueWorkItem2(0x104, 1, lambda_B86E)
    Sleep(50)

    def lambda_B883():

        label("loc_B883")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B883")

    QueueWorkItem2(0x109, 1, lambda_B883)
    Sleep(50)

    def lambda_B898():

        label("loc_B898")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B898")

    QueueWorkItem2(0x105, 1, lambda_B898)
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
            "Lloyd is\x01",
            "I mastered the ranging spin.\x07\x00\x02",
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
            "Lloyd's craft \"Axelush\"\x01",
            "It was strengthened as \"Raging Spin\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In addition to increased attack power, involve a wider range of enemies,\x01",
            "It is possible to draw further to one place.\x07\x00\x02",
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
            "Quest 【Request for participation in hypocritical person training】\x07\x00",
            "Achieved!\x02",
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

    # Function_29_8F64 end

    def Function_30_BAF6(): pass

    label("Function_30_BAF6")

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

    def lambda_BBD9():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x2EE, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BBD9)
    BeginChrThread(0x101, 0, 0, 31)
    WaitChrThread(0x101, 1)
    StopEffect(0x5, 0x2)
    ClearScenarioFlags(0x1, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_30_BAF6 end

    def Function_31_BC0A(): pass

    label("Function_31_BC0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_BC26")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_31_BC0A")

    label("loc_BC26")

    Return()

    # Function_31_BC0A end

    def Function_32_BC27(): pass

    label("Function_32_BC27")

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
            "#00003FI tried listening all the way … ….\x01",
            "I got information in various ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FThe name is \"Minnesh\" …\x01",
            "Apparently some sort of merchant\x01",
            "It seems to be seen.\x02\x03",
            "#00101FAlso what?\x01",
            "It was a surprisingly good impression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FPolite, children friendly ……\x01",
            "That was such an impression.\x02\x03",
            "#10304FHuh, when you come here\x01",
            "On the contrary it comes to be suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FWell, indeed …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FActually, the purpose is not so good\x01",
            "I do not see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FWith the village manager's son,\x01",
            "What I'm talking about\x01",
            "It is an interesting place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAh……\x01",
            "A little more listening\x01",
            "It seems better to continue.\x02\x03",
            "#00005FEr …\x02",
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

    def lambda_BFA3():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BFA3)

    def lambda_BFB0():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BFB0)

    def lambda_BFBD():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BFBD)

    def lambda_BFCA():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BFCA)

    def lambda_BFD7():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BFD7)
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
            "#00005FThat person … … By any chance,\x01",
            "With Derrick\x01",
            "I guess it was a person who went to the town.\x02\x03",
            "#00003FIn the village last time\x01",
            "It seems they came back … …\x01",
            "Do you want to ask the story?\x02",
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

    # Function_32_BC27 end

    def Function_33_C0F7(): pass

    label("Function_33_C0F7")

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
        "Fun Fun - … ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse me.\x01",
            "Is it Elkin?\x02\x03",
            "What I want to ask you a little\x01",
            "I do have …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        "What's it for you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Perhaps, this\x01",
            "About new type conductivity track\x01",
            "Is there something I want to hear?\x02",
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
        (
            "#00012FNo, no …\x01",
            "That's why.\x01",
            "I do not have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Whether it is different.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Inspire Mr. Minnesh\x01",
            "I gave it cheaply\x01",
            "Even though it is the latest version of Verne ……\x02",
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
            "#00105Feh……?\x02\x03",
            "#00101FMr. Minneshi said,\x01",
            "I have recently come to this village\x01",
            "Foreigners … …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FOr, cheaply handed over … …\x01",
            "How much is it! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hehe, it is …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "How, only 50 thousand mila\x01",
            "You got it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FOk, fifty thousand! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FA new car with such a price\x01",
            "I can not buy it ……\x01",
            "Good, hey ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FCome on, envious\x01",
            "It will not be a tough one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112FWell, it was … right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FKohon … Anyway.\x02\x03",
            "#00200FAs a new car also\x01",
            "It should be equivalent to 500,000 mirrors,\x01",
            "It can be said that it is the price of disqualification.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FIt's just 9 discounts.\x01",
            "No, really\x01",
            "He looks like a heavy person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Our work is\x01",
            "In order to be smooth,\x01",
            "It cheaply handed over to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "With a variety of derricks\x01",
            "He seems to be progressing the plan … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huhu, to Mr. Minnesu\x01",
            "I have no head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305Fplan……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oops.\x01",
            "This is a derrick\x01",
            "It was spun out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well anyway … …\x01",
            "People like Mr. Minnes\x01",
            "I think he is a trustworthy person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see……\x02\x03",
            "#00005F… … That, that's right.\x01",
            "Is Elkin alone?\x02\x03",
            "From the village manager, with Derrick\x01",
            "I heard that I headed to the city … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, if it's a derrick\x01",
            "I will return by bus later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anything, at the hotel of the entertainment district\x01",
            "It seems there is a purpose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Apparently, with Mr. Minnes\x01",
            "It seems they are making promises to meet.\x02",
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
        "#00101FHey Lloyd, this is … …\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FOh, maybe\x01",
            "You may be able to hear a direct talk.\x02\x03",
            "#00001FIt will be worth while going.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        (
            "#00000FThanks for your cooperation.\x01",
            "Thanks to that, I got a lot of reference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "No problem, you are welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I do not quite understand it, but\x01",
            "Do your best.\x02",
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

    # Function_33_C0F7 end

    def Function_34_CB66(): pass

    label("Function_34_CB66")

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
            "#N#1P#00010FOops……\x01",
            "Have you already closed the transaction …?! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)

    def lambda_CEC4():
        OP_95(0xFE, 3850, 0, 19250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_CEC4)
    Sleep(100)

    def lambda_CEE1():
        OP_95(0xFE, 4270, 0, 18270, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_CEE1)
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

    def lambda_CF8C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_CF8C)
    Sleep(100)

    def lambda_CF9C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_CF9C)
    Sleep(300)

    ChrTalk(
        0xD,
        "Hey, you are …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "The Special Affairs Support Division ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FMr. Derrick, Mr. Minnes … …\x01",
            "What kind of transaction did you do today?\x01",
            "Could you please?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Whether it is his father's deposit ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Huhuu, is not it nice\x01",
            "Mr. Derrick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Our plan is no longer\x01",
            "I started it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FWhat does that mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "── Actually, I heard that Mr. Derrick\x01",
            "Please do the last transaction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Using the land borrowed from everyone in the village,\x01",
            "It is necessary to undertake expansion of the astragalus field\x01",
            "We have decided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "And, management of the astragalus field itself\x01",
            "At our \"Quincy Company\"\x01",
            "I decided to take over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FBecome\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F…… If this is the case,\x01",
            "Most of the village farm\x01",
            "I talk about transferring … ….\x02\x03",
            "#10300FMr. Derrick,\x01",
            "Is it really good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "……What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To the last, management\x01",
            "I will just leave it to you.\x02",
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
            "By harvesting honey in our company\x01",
            "Confectionery business more efficiently\x01",
            "It will be able to operate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "For that purpose,\x01",
            "It is better to transfer the rights to our company\x01",
            "Efficiency is good in various ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F(Chick ……\x01",
            "He is a good bastard. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F(The plan is almost final stage\x01",
            "You seem to be coming. )\x02\x03",
            "#00208F(Then, after that … …)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "Huhu, then Derrick.\x01",
            "I will use this contract\x01",
            "We will deliver it to our head office.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "I will give you a good message tomorrow\x01",
            "I think that I can do it,\x01",
            "Please look forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Well, I am waiting.\x02",
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
        "#10101F(Ro, Mr. Lloyd … …!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Ah……\x01",
            "I can not let you escape here! )\x02\x03",
            "#00001F── Mr. Minnes, before that ……\x01",
            "I have something to ask.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_D641():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_D641)
    Sleep(100)

    def lambda_D651():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D651)
    Sleep(300)

    ChrTalk(
        0xD,
        "How is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "What do you want to ask?\x01",
            "Is it all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, that is ……\x01",
            "It depends on you\x01",
            "There is a suspicion about it.\x02\x03",
            "#00001Fso……\x01",
            "It is said that he is working fraud\x01",
            "Suspicion.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        "Become Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, please do it!\x01",
            "It will be rude to Mr. Minnes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hehe … … well so so,\x01",
            "Please calm down Mr. Derrick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Mr. Minnes …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Indeed, with the mission support section\x01",
            "Did you say that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Why you, me\x01",
            "Do you suspect it as a crook … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Of course, there are things to explain\x01",
            "Is it possible?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F……of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "interesting……\x01",
            "So let me tell you\x01",
            "let's do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But before that ……\x01",
            "That I am an empire\x01",
            "Do not forget.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If you make me a cheater\x01",
            "When there is no clear basis …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Even if it is a police officer,\x01",
            "Let me put it out\x01",
            "We will accept your approval as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F… … It would be nice.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00101FLloyd …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(……Should be fine.)\x02\x03",
            "(From the information obtained in the investigation,\x01",
            "Minnes worked fraud\x01",
            "It is obvious that there are … …)\x02\x03",
            "#00001F(Hold on suspicion\x01",
            "Reveal the identity of Minnes,\x01",
            "Wake up Mr. Derrick! )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hehe, please …\x01",
            "If there is so much preparedness,\x01",
            "Let's answer anything.\x02",
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
            "…… Then, what kind of story is first\x01",
            "Can you do it?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F── First of all, your\x01",
            "Behavior in crossbell …\x02\x03",
            "#00001FAbout the contradiction point\x01",
            "I would like to ask you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Contradiction, even …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "…… Since I came to Crosbell,\x01",
            "Always with Derrick\x01",
            "I have advanced this plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In Almorika village my \"Quincy Company\"\x01",
            "Start a subsidiary … …\x01",
            "\"Almorica · Honey company\" plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Confectionery business using quality village honey,\x01",
            "If you make the best use of our know-how\x01",
            "It will surely bear fruit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It has already been officially licensed to the city,\x01",
            "I am about to start now\x01",
            "In this project …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Where the contradiction arises\x01",
            "Are you saying that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNo, you talked right now\x01",
            "Story of \"plan\" …\x02\x03",
            "#00001FWhat we have is information\x01",
            "There are clearly conflicting points.\x02\x03",
            "#00003FYes, that contradiction point …\x02",
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
            "#1KAbout Minnes' plan\x01",
            "What is contradictory point?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Have know-how of confectionery\x01",      # 0
            "Plan is in progress\x01",        # 1
            "There is a prospect in the plan\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF3B")
    OP_2C(0x87, 0x1)

    ChrTalk(
        0x101,
        (
            "#00003FInformation we got at IBC and\x01",
            "When I compare it\x01",
            "You will see one contradiction point.\x02\x03",
            "#00001FYou say \"plan\" … …\x02\x03",
            "To tell the truth, I have it at all\x01",
            "It should not be progressing.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x6)
    Jump("loc_E2E9")

    label("loc_DF3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E08F")

    ChrTalk(
        0x101,
        (
            "#00003FYou say \"plan\" … …\x02\x03",
            "#00001FActually make it progress\x01",
            "Know how,\x01",
            "You should not be there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "How is it?\x01",
            "It is an interesting opinion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But how to do it\x01",
            "Are you going to prove it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F…… Well, well … that's …\x02\x03",
            "#00006F(Oops……\x01",
            "To confront suspicion\x01",
            "I have to think about arrangements. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1D8")

    label("loc_E08F")


    ChrTalk(
        0x101,
        (
            "#00003FYou say \"plan\" … …\x02\x03",
            "#00001FActually, that\x01",
            "I do not expect to succeed\x01",
            "There should be almost nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "How is it?\x01",
            "Although it is an interesting opinion,\x01",
            "Somewhat rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Doing something with what you have\x01",
            "Are you saying that,\x01",
            "I would like you to prove it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F…… Well, well … that's …\x02\x03",
            "#00006F(Oops……\x01",
            "Was it a bit different? )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E1D8")


    ChrTalk(
        0x102,
        (
            "#00105FOh … it may have been understood.\x02\x03",
            "#00100FInformation we got at IBC and\x01",
            "When you compare it, there are contradictions\x01",
            "I wonder if it will come into view.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F……Really……!\x02\x03",
            "#00001FMr. Minnes …\x01",
            "Your \"plan\" is …\x01",
            "Actually, is not it not progressing?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x7)

    label("loc_E2E9")

    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "…………!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "IBC ……?\x01",
            "Well, what do you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003Fplease think about it.\x01",
            "\"Quincy company\" is the previous\x01",
            "If I plan to proceed … …\x02\x03",
            "#00001FFor the establishment of subsidiaries and the construction of factories,\x01",
            "IBC loan is required.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "…… Yes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "To that end, we notified the city of the establishment of the company,\x01",
            "Properly set up an account for a corporation …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F─ ─ prepared, just \".\x01",
            "Is not it so?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIn the account of \"Honey company\"\x01",
            "Only the minimum number of mirrors necessary for opening\x01",
            "It seems that it was not included.\x02\x03",
            "I do not know the detailed price,\x01",
            "About tens of thousands of mirrors that had been deposited … …\x02\x03",
            "#00001FWell, at such Mira\x01",
            "The factory construction etc.\x01",
            "Is it possible …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "…… to IBC's account\x01",
            "I do not mean that you are investigating … …\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "Mi, Minnes san …\x01",
            "No way …! Is it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "Oh, do not get me wrong.\x01",
            "Separately they say\x01",
            "I did not admit it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "However, if it is too outrageous\x01",
            "I just thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FBut,\x01",
            "In fact, Mira in the account\x01",
            "It's almost not included! Is it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "What, as a company officer\x01",
            "I had no choice but to move a bit carefully\x01",
            "That's it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Anyway, venerable\x01",
            "In the name of \"Quincy Company\"\x01",
            "Because I receive a loan … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Of course, as soon as the permission of the head office goes down\x01",
            "To IBC for loan consultation\x01",
            "I thought about going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Ho … … it is, is not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F(… … It was well dodged.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Disagreeable……\x01",
            "Mineness is also quite inner\x01",
            "You should be ashamed. )\x02\x03",
            "#00001F(As if to fold here\x01",
            "Prompt proof …! )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "…… The face is still something\x01",
            "It seems there is something you want to hear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FYes, of course.\x02\x03",
            "#00004FAny suspicion of Mr. Minnesh\x01",
            "That's not all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        "It has not reached this period yet … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "No no, it's okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "That person\x01",
            "Even for Mr. Derrick\x01",
            "You will be safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F…… I'd like to ask …\x01",
            "Mr. Minnes's\x01",
            "About the profile.\x02\x03",
            "#00003FMr. Minnes, you\x01",
            "Officer of \"Quincy Company\"\x01",
            "You are saying that … ….\x02\x03",
            "#00013FIs that a sure thing?\x02",
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
            "wait……\x01",
            "What do you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Mr. Minnes\x01",
            "\"Quincy Company\"\x01",
            "Are not you human beings?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, we are\x01",
            "That is so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Kuku …… Ha ha ha!\x01",
            "If you think what you are saying ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Whatever your business card or employee ID card\x01",
            "Shall I show you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F…… If such knowledge is\x01",
            "How much can you forge?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWe overturn that evidence\x01",
            "I have examined the evidence.\x02\x03",
            "#00000FThat is … nothing else,\x01",
            "It is a brochure by Quincy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Quincy's brochure ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FHe was in his lady's room ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FIndeed, in the investigation notebook\x01",
            "You were memorizing the main points.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSince it was ordered from the head office,\x01",
            "The reliability of written information\x01",
            "It can be said that it is guaranteed.\x02\x03",
            "#00003FAnd what was written in the document …\x01",
            "That is what Mr. Minnes said yesterday\x01",
            "It is clearly contradictory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Wow, that's my story …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYesterday's story of Minnes\x01",
            "With the title of \"officer\"\x01",
            "What contradicts is that … …\x02",
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
            "#1KTalk with Minnes yesterday\x01",
            "What is the point where the facts of the material conflict?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Establishment plan of subsidiary\x01",      # 0
            "Sales department career\x01",          # 1
            "I am not good at sweets\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F4B2")
    OP_2C(0x87, 0x1)

    ChrTalk(
        0x101,
        (
            "#00003F── Mr. Minnes.\x01",
            "Yesterday you said:\x02\x03",
            "\"While entering the positions of officers\x01",
            "Actually I'm not good at sweet things \"……\x02\x03",
            "#00013FThere is no mistake in this word, are not you?\x02",
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

    def lambda_F0F9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F0F9)
    Sleep(50)

    def lambda_F109():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F109)
    Sleep(50)

    def lambda_F119():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F119)
    Sleep(50)

    def lambda_F129():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F129)
    Sleep(50)

    def lambda_F139():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F139)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00105FB, Lloyd …?\x01",
            "Er, well meaning ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "…… Certainly, I am not good at sweets.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Huh, but that is it\x01",
            "What's the matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "\"People who are not good at sweet things\x01",
            "It can not be an executive in a confectionery company \"\x01",
            "Are you going to say …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FThat's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "What is the word …!\x01",
            "You as embarrassing as the police ─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F── Quincy's brochure contains the following information:\x01",
            "It was written like this.\x02\x03",
            "#00003F\"At Quincy,\x01",
            "Officers taste products under development themselves,\x01",
            "We will strictly judge whether we can sell … \"\x02\x03",
            "#00013FTo tell the truth, it is such content.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F372():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F372)
    Sleep(50)

    def lambda_F382():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F382)
    Sleep(50)

    def lambda_F392():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F392)
    Sleep(50)

    def lambda_F3A2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F3A2)
    Sleep(50)

    def lambda_F3B2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F3B2)
    Sleep(300)

    ChrTalk(
        0xD,
        "…………………………! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "What is it all about …?\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0xC,
        "#4S……………………Ah! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… A company called Quincy\x01",
            "Mr. Minnes who \"is not good at sweet things\"\x01",
            "It is unnatural to be an official.\x02\x03",
            "#00013F……Is it wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x8)
    Jump("loc_FB4D")

    label("loc_F4B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F53F")

    ChrTalk(
        0x101,
        (
            "#00003F── Mr. Minnes.\x01",
            "Yesterday you said.\x02\x03",
            "\"Building a subsidiary in Almorika village\"\x01",
            "About that plan, that … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5C1")

    label("loc_F53F")


    ChrTalk(
        0x101,
        (
            "#00003F── Mr. Minnes.\x01",
            "Yesterday you said.\x02\x03",
            "\"Thanks to being active in the sales direction\x01",
            "Forgiving power,\x01",
            "I got on my present position \"……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F5C1")


    ChrTalk(
        0xD,
        (
            "…… I said certainly\x01",
            "Is that what it is all about?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00011F(Well, it was ……\x01",
            "I do not see any words to return!\x01",
            "Was the idea wrong …? )\x02\x03",
            "#00012FWell, it is.\x01",
            "It is a bit different now …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F─ ─ um I see.\x01",
            "I finally remembered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh.\x02",
    )

    CloseMessageWindow()

    def lambda_F6EB():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F6EB)
    Sleep(50)

    def lambda_F6FB():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F6FB)
    Sleep(50)

    def lambda_F70B():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F70B)
    Sleep(50)

    def lambda_F71B():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F71B)
    Sleep(50)

    def lambda_F72B():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F72B)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10304F\"While entering the positions of officers\x01",
            "Actually I'm not good at sweet things \"……\x02\x03",
            "#10302FMr. Minnes,\x01",
            "Yesterday you said so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FWow, you fuck …?\x01",
            "Er, well meaning ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "…… Certainly, I am not good at sweets.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Huh, but that is it\x01",
            "What's the matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "\"People who are not good at sweet things\x01",
            "It can not be an executive in a confectionery company \"\x01",
            "Are you going to say …?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F898():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F898)
    Sleep(300)

    ChrTalk(
        0x103,
        "#00203F……That's right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        "#10309FHuhu, you seem to have noticed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "What is the word …!\x01",
            "You, embarrassing as a police officer ----\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F── Quincy's brochure contains the following information:\x01",
            "It was written like this.\x02\x03",
            "\"At Quincy,\x01",
            "Officers taste products under development themselves,\x01",
            "We will strictly judge whether we can sell … \"\x02\x03",
            "#10302FTo tell the truth, that kind of thing.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FA1A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FA1A)
    Sleep(50)

    def lambda_FA2A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FA2A)
    Sleep(50)

    def lambda_FA3A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FA3A)
    Sleep(50)

    def lambda_FA4A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FA4A)
    Sleep(300)

    ChrTalk(
        0xD,
        "…………………………! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "What is it all about …?\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0xC,
        "#4S……………………Ah! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F…… A company called Quincy\x01",
            "Mr. Minnes who \"is not good at sweet things\"\x01",
            "It can be said that it is unnatural to be an officer.\x02\x03",
            "#00201F……Is it wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x9)

    label("loc_FB4D")


    ChrTalk(
        0xD,
        (
            "… …. Well, that is ……\x01",
            "In mere memory mistake ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIt will not pass.\x02\x03",
            "#00001F…… You just arrived\x01",
            "\"I am not good at sweet things\"\x01",
            "You should have recognized it clearly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "So …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIf so\x01",
            "Why are you \"Quincy Company\"\x01",
            "Did you falsify it as an officer?\x02\x03",
            "#00001FIt is ──\x01",
            "To make you a fraud,\x01",
            "To make Derrick trust you.\x02\x03",
            "#00003FFrom the evidence so far,\x01",
            "I can only think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FI used Armorican honey\x01",
            "Confectionery business ……\x02\x03",
            "#00101FTo make it trust\x01",
            "The name \"Quincy Inc.\"\x01",
            "That is why it was convenient.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "Mi, Minnes san …\x01",
            "This is,\x01",
            "what do you mean! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Again …\x01",
            "You were tricking me! Is it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "… …. Kuku ……\x01",
            "Mr. Derrick, you are\x01",
            "They should not be deceived …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FOh, with you?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        "Hehe … … is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I came to Almorika village,\x01",
            "Plan of \"Honey company\"\x01",
            "To have it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If you hand over a hundred steps and have other purposes,\x01",
            "If you say you fooled Derrick … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Well, what is the purpose! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "To you who can not prove it,\x01",
            "I should not qualify to call me a cheat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIs it proof of purpose …?\x01",
            "Certainly it was.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003FYour purpose ----\x01",
            "There is one thing just to be noticed.\x02",
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

    def lambda_100D7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_100D7)
    Sleep(50)

    def lambda_100E7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_100E7)
    Sleep(50)

    def lambda_100F7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_100F7)
    Sleep(50)

    def lambda_10107():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10107)
    Sleep(50)

    def lambda_10117():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10117)
    Sleep(50)

    def lambda_10127():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_10127)
    Sleep(300)

    ChrTalk(
        0xD,
        "What … … what! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F(Lloyd, are you okay … …!?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Yeah, I have no idea at all\x01",
            "I do not have it … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(No … indeed there are.\x02\x03",
            "(Immediately before coming here,\x01",
            "\"That person\" has searched for it\x01",
            "\"That testimony\" … …)\x02\x03",
            "(#00001FYes, Minnes's\x01",
            "The last clues to reveal the purpose …! )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "What are you saying!\x01",
            "… …. Now, explain!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYou are in this village\x01",
            "I did a fraud, the real reason.\x01",
            "that is……\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_102F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1051C")
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
            "#1KMinnes is in Armorika village\x01",
            "What is the real purpose of trying to work a fraud?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Stealing the land\x01",        # 0
            "Monopoly of honey sales\x01",      # 1
            "Sales of fake guided vehicles\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1043C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_103CC")
    OP_2C(0x87, 0x1)

    label("loc_103CC")


    ChrTalk(
        0x101,
        (
            "#00003FYour true purpose, that is ……\x02\x03",
            "#00013FOwned by this Almorika village\x01",
            "\"Land\" It was it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10517")

    label("loc_1043C")


    ChrTalk(
        0x101,
        (
            "#00006F(No … different.\x01",
            "Small of such scale\x01",
            "Not a story. )\x02\x03",
            "#00001F(Take that much time and effort\x01",
            "I was preparing … ….\x01",
            "There must be a bigger aim. )\x02\x03",
            "#00003F(The real purpose of Minnes,\x01",
            "that is……)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_10517")

    Jump("loc_102F3")

    label("loc_1051C")


    ChrTalk(
        0xD,
        "… … … Ah ……! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FA trader who is Mr. Harold,\x01",
            "Listen to you about you\x01",
            "I gave it.\x02\x03",
            "#00000FMr. Minnes, you are … …\x01",
            "Immediately after entering the crossbell,\x01",
            "You seem to have been looking at land prices in various places?\x02\x03",
            "#00003FOfficer of \"Quincy Company\"\x01",
            "To bring new business\x01",
            "There is no need to do such a thing.\x02\x03",
            "Then why …?\x01",
            "One possible possibility is one.\x02\x03",
            "#00013FYou pre-empt this land\x01",
            "Because it was aiming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FIs it true? Is it?\x01",
            "Nah, I do not have a rush\x01",
            "Like an idea.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00004FNo, it is not so.\x02\x03",
            "#00002FAs you can see, Almorika village\x01",
            "Surrounded by rich nature,\x01",
            "The location is preeminent.\x02\x03",
            "#00004FFor example, manage a high-end villa\x01",
            "If you were to sell it to a third party ……\x01",
            "How much value would you expect?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FThat's it ……\x01",
            "Even with tens of millions of mirrors\x01",
            "There seems to be a person who wants to win a bid.\x02\x03",
            "#00101FWhat does the villagers agree with?\x01",
            "I do not think at all … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FOh, that's why\x01",
            "Take this trouble\x01",
            "You probably worked a fraud.\x02\x03",
            "#00001FIf the land itself\x01",
            "Assuming the purpose … …\x01",
            "I can explain his behavior.\x02\x03",
            "Including a vast astragalus field\x01",
            "Many farms, and\x01",
            "Get the rights document of private property ……\x02\x03",
            "In the name of returning to the head office\x01",
            "From Crossbell\x01",
            "It disappears.\x02\x03",
            "#00003FAnd prepared\x01",
            "Land rights book on sales route\x01",
            "For sale, get a lot of mira … …\x02\x03",
            "#00013FThat is what Mr. Minnes … …\x01",
            "It was your true purpose.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10A23():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10A23)
    Sleep(50)

    def lambda_10A33():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10A33)
    Sleep(50)

    def lambda_10A43():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10A43)
    Sleep(50)

    def lambda_10A53():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10A53)
    Sleep(50)

    def lambda_10A63():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10A63)
    Sleep(300)

    ChrTalk(
        0xD,
        "… …. ugh …\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "Mineness …… Mr. …\x01",
            "Something like that ….\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x1F, -1730, 390, 7230, 225)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)

    NpcTalk(
        0x1F,
        "Male voice",
        "── Mr. Lloyd …!\x02",
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

    def lambda_10BA0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10BA0)
    Sleep(50)

    def lambda_10BB0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10BB0)
    Sleep(50)

    def lambda_10BC0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10BC0)
    Sleep(50)

    def lambda_10BD0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10BD0)
    Sleep(50)

    def lambda_10BE0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10BE0)
    Sleep(50)

    def lambda_10BF0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10BF0)
    Sleep(50)

    def lambda_10C00():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_10C00)
    Sleep(50)

    def lambda_10C10():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_10C10)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00000FThis voice ……\x02",
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
        "#03600FIt looks good, you seemed to make it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "Derrick ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Mr. Harold to the father ……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FBesides,\x01",
            "Certainly … of the law firm ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Professor Ian's assistant\x01",
            "It is called Pete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Originally the teacher was supposed to come,\x01",
            "Because of the draft constitution draft\x01",
            "Because I had to go out by all means …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FEvidence ……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#03603FYes, the teacher said earlier\x01",
            "It seems to be \"evidence of pushing\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "Everyone, please look at this.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Pete took out a picture,\x01",
            "I held it so that I could check with everyone on the spot.\x02\x03",
            "In the picture, I faced the same face as Minnes\x01",
            "A man with a merchant style is shown.\x07\x00\x02",
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
        "#00005FThat reflected in that picture ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Why, why ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Why are you,\x01",
            "I have such a picture! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "This photo shows how Professor Ian\x01",
            "Long ago, from reporters of acquaintances of the empire\x01",
            "It was acquired as a document.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "But, the name of the man in the picture is ……\x01",
            "Not \"Minnesh\"\x01",
            "It seems that it was \"Lidnar\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FRidnor …?\x01",
            "That name, recently somewhere\x01",
            "I feel like hearing it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F……Ah!\x01",
            "Surely that … …\x02\x03",
            "#00101FProfessor Ian was talking,\x01",
            "I robbed the baroness of the empire\x01",
            "It's a man's name …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Damn it …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FOh, it was such a name.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#03601FYeah …… Mr. Ian also\x01",
            "I have heard a new story again,\x01",
            "I think there is no mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHmm …. Then,\x01",
            "Fascinating facts are pretty\x01",
            "It looks like you can see it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10302FLloyd, he … … on Minnes\x01",
            "Do not push it.\x02\x03",
            "#10304FThe meaning of this picture, is not it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F… Ah, I understand.\x02",
    )

    CloseMessageWindow()
    OP_68(2020, 1500, 16370, 3000)

    def lambda_113DC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_113DC)
    Sleep(50)

    def lambda_113EC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_113EC)
    Sleep(50)

    def lambda_113FC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_113FC)
    Sleep(50)

    def lambda_1140C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1140C)
    Sleep(50)

    def lambda_1141C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1141C)
    Sleep(50)

    def lambda_1142C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1142C)
    Sleep(50)

    def lambda_1143C():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1143C)
    Sleep(50)

    def lambda_1144C():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1144C)
    Sleep(300)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00001FPeople in this picture \"Lidner\" and\x01",
            "Now \"Minnesh\" in this place\x01",
            "The reason for having the same face, that is ……\x02",
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
            "#1KPhoto with Lidner\x01",
            "Why is Minnes having the same face?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "twins\x01",          # 0
            "disguise\x01",          # 1
            "same person\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_115FD")
    OP_2C(0x87, 0x1)

    ChrTalk(
        0x101,
        (
            "#00003FMinnes and Lidner are the same person ……\x01",
            "I can only think so.\x02\x03",
            "#00013FThe fraud method was very similar,\x01",
            "Because it was the same person, that is why.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11885")

    label("loc_115FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1165B")

    ChrTalk(
        0x101,
        (
            "#00003FMinnes and Lidner … … twin brothers.\x01",
            "I can only think so.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1169F")

    label("loc_1165B")


    ChrTalk(
        0x101,
        (
            "#00003FMinnes …… Lydner's disguise.\x01",
            "I can only think so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1169F")

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
            "#10306F…… Indeed it is\x01",
            "I guess it's over reading too much?\x02\x03",
            "#10302FWhatever you think,\x01",
            "Minnes and Lidner\x01",
            "I think that it is the same person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Well, I thought it was too difficult … …)\x02\x03",
            "#00013FKohon, if so, …\x01",
            "The fraud method was very similar,\x01",
            "Because it was the same person, that is why.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11885")


    ChrTalk(
        0x1D,
        "Mr. Ian also said that ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Perhaps it is\x01",
            "This guy is the most specialty\x01",
            "It is a fraud trick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F\"Scammers\" ── Minnes.\x01",
            "Your fraudulent charges are obvious.\x02\x03",
            "#00013FMoreover, with suspects who worked in fraud in the empire\x01",
            "It is also likely to be the same person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FAs much as you can\x01",
            "Do not dust like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FCome and talk more\x01",
            "Let me tell you.\x01",
            "…… In the interrogation room of the police headquarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "… ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Dude ……\x01",
            "By yeah yeah yeah … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I … … a perfect job\x01",
            "This creed I believe … …\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0xD,
        "#4SSuch … … Bewitch! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Mi, Minnes san …\x02",
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
            "…… Hung, good mind\x01",
            "Shall we not have it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It's bad, but with this\x01",
            "I am going to capture\x01",
            "Because it is not a hairy head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005Fwhat……! Is it?\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xD,
        "─ ─ Come, animals!\x02",
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
        "Uwaaaa! Is it?\x02",
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
        "#00010FWait … … monsters! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FAnd pretty\x01",
            "It seems to be trained …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F(These guys, you can not … …!?)\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0xC, 0xB4, 0x3E8, 0x3E8, 0x0)
    Sleep(100)

    ChrTalk(
        0xC,
        "No …\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x1D, 0x0, 0x1F4, 0x1388, 0x0)
    OP_93(0x1D, 0x5A, 0x0)
    Sleep(300)

    ChrTalk(
        0x1D,
        "De, Derrick! It is!\x02",
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x87, 0x3E8)
    Sleep(300)

    ChrTalk(
        0x1F,
        "#03605FThat's right, the village mayor is in danger …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107Fyou are……\x01",
            "What is he doing?\x01",
            "Do you understand! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Yes, I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Oh, if you make a mistake, I will fight\x01",
            "Do not think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "To Derrick and the villagers\x01",
            "I do not want to hurt the spring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010FDamn\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Come now, leave the way.\x02",
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

    def lambda_12319():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12319)

    def lambda_12326():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12326)

    def lambda_12333():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12333)

    def lambda_12340():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12340)

    def lambda_1234D():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1234D)

    def lambda_1235A():
        OP_93(0xFE, 0x87, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1235A)

    def lambda_12367():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12367)

    def lambda_12374():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_12374)

    def lambda_12381():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_12381)
    WaitChrThread(0x105, 1)

    def lambda_12392():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12392)
    Sleep(50)

    def lambda_123AA():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_123AA)
    Sleep(50)

    def lambda_123C2():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_123C2)
    Sleep(50)

    def lambda_123DA():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_123DA)
    Sleep(50)

    def lambda_123F2():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_123F2)
    Sleep(50)

    def lambda_1240A():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1240A)
    Sleep(50)

    def lambda_12422():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12422)
    Sleep(50)

    def lambda_1243A():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1243A)
    Sleep(50)

    def lambda_12452():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_12452)
    Sleep(50)

    def lambda_1246A():
        OP_95(0xFE, -1910, 0, 11190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1246A)
    WaitChrThread(0x1F, 1)

    def lambda_12488():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12488)
    WaitChrThread(0x1D, 1)

    def lambda_12499():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_12499)
    WaitChrThread(0x1E, 1)

    def lambda_124AA():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_124AA)
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

    def lambda_12509():

        label("loc_12509")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12509")

    QueueWorkItem2(0x101, 1, lambda_12509)
    Sleep(50)

    def lambda_1251E():

        label("loc_1251E")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_1251E")

    QueueWorkItem2(0x102, 1, lambda_1251E)
    Sleep(50)

    def lambda_12533():

        label("loc_12533")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12533")

    QueueWorkItem2(0x103, 1, lambda_12533)
    Sleep(50)

    def lambda_12548():

        label("loc_12548")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12548")

    QueueWorkItem2(0x104, 1, lambda_12548)
    Sleep(50)

    def lambda_1255D():

        label("loc_1255D")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_1255D")

    QueueWorkItem2(0x105, 1, lambda_1255D)
    Sleep(50)

    def lambda_12572():

        label("loc_12572")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12572")

    QueueWorkItem2(0xC, 1, lambda_12572)
    Sleep(50)

    def lambda_12587():

        label("loc_12587")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_12587")

    QueueWorkItem2(0x1D, 1, lambda_12587)
    Sleep(50)

    def lambda_1259C():

        label("loc_1259C")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_1259C")

    QueueWorkItem2(0x1F, 1, lambda_1259C)
    Sleep(50)

    def lambda_125B1():

        label("loc_125B1")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_125B1")

    QueueWorkItem2(0x1E, 1, lambda_125B1)
    Sleep(100)

    def lambda_125C6():

        label("loc_125C6")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_125C6")

    QueueWorkItem2(0x109, 1, lambda_125C6)
    Sleep(50)

    def lambda_125DB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_125DB)
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

    def lambda_12627():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12627)
    Sleep(50)

    def lambda_1263F():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1263F)
    Sleep(50)

    def lambda_12657():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_12657)
    Sleep(500)

    ChrTalk(
        0xD,
        "Huhu, then it's OK.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I will never meet again.\x02",
    )

    CloseMessageWindow()

    def lambda_126B3():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_126B3)
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
        "De, Derrick ……!\x02",
    )

    CloseMessageWindow()

    def lambda_1280A():
        OP_95(0xFE, 5240, 0, 18260, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1280A)
    Sleep(100)

    def lambda_12827():
        OP_95(0xFE, 3790, 0, 19250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_12827)
    Sleep(100)

    def lambda_12844():
        OP_95(0xFE, 3560, 0, 17530, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12844)
    WaitChrThread(0x1D, 1)

    def lambda_12862():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_12862)
    WaitChrThread(0x1F, 1)

    def lambda_12873():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12873)
    WaitChrThread(0x1E, 1)

    def lambda_12884():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_12884)
    WaitChrThread(0x1E, 1)

    ChrTalk(
        0xC,
        "UU……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007FDamn it, let's escape …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201Flet's go……!\x02",
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

    def lambda_12917():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12917)
    Sleep(100)

    def lambda_12934():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12934)
    Sleep(100)

    def lambda_12951():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12951)
    Sleep(100)

    def lambda_1296E():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1296E)
    Sleep(100)

    def lambda_1298B():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1298B)
    Sleep(100)

    def lambda_129A8():
        OP_95(0xFE, -1710, 190, 9240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_129A8)
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
        "#00105FAhh ……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FI was able to escape\x01",
            "I have it …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FUu … … It is frustrating!\x01",
            "Such a cowardly son\x01",
            "I will not miss it …!\x02",
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
            "#00006F…… For the time being the villagers\x01",
            "I am glad that there was no damage.\x02\x03",
            "#00000FAnyway just that\x01",
            "I have to do it well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FWhew, to catch a guy\x01",
            "It is a translation for fun this time.\x02\x03",
            "#10300FAnyway, join the village mayors\x01",
            "Shall I report a case?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F(…………………………)\x02",
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

    # Function_34_CB66 end

    def Function_35_12DA0(): pass

    label("Function_35_12DA0")

    OP_97(0x101, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 2060, 0, 16660, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_35_12DA0 end

    def Function_36_12DD4(): pass

    label("Function_36_12DD4")

    OP_97(0x102, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 1450, 0, 17650, 2000, 0x0)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_36_12DD4 end

    def Function_37_12E08(): pass

    label("Function_37_12E08")

    OP_97(0x103, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 2050, 0, 15310, 2000, 0x0)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_37_12E08 end

    def Function_38_12E3C(): pass

    label("Function_38_12E3C")

    OP_97(0x104, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 420, 0, 18380, 2000, 0x0)
    OP_93(0x104, 0x5A, 0x1F4)
    Return()

    # Function_38_12E3C end

    def Function_39_12E70(): pass

    label("Function_39_12E70")

    OP_97(0x109, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 870, 0, 16059, 2000, 0x0)
    OP_93(0x109, 0x5A, 0x1F4)
    Return()

    # Function_39_12E70 end

    def Function_40_12EA4(): pass

    label("Function_40_12EA4")

    OP_97(0x105, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 170, 0, 17060, 2000, 0x0)
    OP_93(0x105, 0x5A, 0x1F4)
    Return()

    # Function_40_12EA4 end

    def Function_41_12ED8(): pass

    label("Function_41_12ED8")

    OP_97(0x101, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 7230, 0, -14950, 3500, 0x0)
    OP_93(0x101, 0x87, 0x1F4)
    Return()

    # Function_41_12ED8 end

    def Function_42_12F0C(): pass

    label("Function_42_12F0C")

    OP_97(0x102, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 5740, 0, -15440, 3500, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_42_12F0C end

    def Function_43_12F40(): pass

    label("Function_43_12F40")

    OP_97(0x103, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 7140, 0, -13390, 3500, 0x0)
    OP_93(0x103, 0x87, 0x1F4)
    Return()

    # Function_43_12F40 end

    def Function_44_12F74(): pass

    label("Function_44_12F74")

    OP_97(0x104, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 5860, 0, -14270, 3500, 0x0)
    OP_93(0x104, 0x87, 0x1F4)
    Return()

    # Function_44_12F74 end

    def Function_45_12FA8(): pass

    label("Function_45_12FA8")

    OP_97(0x109, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 5870, 0, -12970, 3500, 0x0)
    OP_93(0x109, 0x87, 0x1F4)
    Return()

    # Function_45_12FA8 end

    def Function_46_12FDC(): pass

    label("Function_46_12FDC")

    OP_97(0x105, 0x0, 0x0, 0xFFFFF448, 0xDAC, 0x0)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 4340, 0, -14470, 3500, 0x0)
    OP_93(0x105, 0x87, 0x1F4)
    Return()

    # Function_46_12FDC end

    def Function_47_13010(): pass

    label("Function_47_13010")

    OP_97(0x1D, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x1D, 1)
    OP_95(0x1D, -1530, 0, 11680, 2000, 0x0)
    OP_93(0x1D, 0x2D, 0x1F4)
    Return()

    # Function_47_13010 end

    def Function_48_13044(): pass

    label("Function_48_13044")

    OP_97(0x1F, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x1F, 1)
    OP_95(0x1F, -2380, 0, 13280, 2000, 0x0)
    OP_93(0x1F, 0x2D, 0x1F4)
    Return()

    # Function_48_13044 end

    def Function_49_13078(): pass

    label("Function_49_13078")

    OP_97(0x1E, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    WaitChrThread(0x1E, 1)
    OP_95(0x1E, -720, 0, 12970, 2000, 0x0)
    OP_93(0x1E, 0x2D, 0x1F4)
    Return()

    # Function_49_13078 end

    def Function_50_130AC(): pass

    label("Function_50_130AC")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_130B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_130D3")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("loc_130B7")

    label("loc_130D3")

    Return()

    # Function_50_130AC end

    def Function_51_130D4(): pass

    label("Function_51_130D4")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_130DF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_130F6")
    OP_A0(0xFE, 1200, 0x0, 0x5)
    Jump("loc_130DF")

    label("loc_130F6")

    Return()

    # Function_51_130D4 end

    def Function_52_130F7(): pass

    label("Function_52_130F7")


    def lambda_130FC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_130FC)

    def lambda_1310D():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1310D)
    WaitChrThread(0x20, 1)
    BeginChrThread(0x20, 0, 0, 51)
    OP_95(0x20, 4710, 0, -15670, 6000, 0x0)
    OP_95(0x20, -2120, 0, -1730, 6000, 0x0)
    OP_95(0x20, -2120, 0, 14270, 6000, 0x0)
    Return()

    # Function_52_130F7 end

    def Function_53_1316C(): pass

    label("Function_53_1316C")


    def lambda_13171():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_13171)

    def lambda_13182():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_13182)
    WaitChrThread(0x21, 1)
    BeginChrThread(0x21, 0, 0, 51)
    OP_95(0x21, 6990, 0, -13880, 7000, 0x0)
    OP_95(0x21, 830, 0, -10410, 7000, 0x0)
    OP_95(0x21, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x21, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_53_1316C end

    def Function_54_131F5(): pass

    label("Function_54_131F5")


    def lambda_131FA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_131FA)

    def lambda_1320B():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_1320B)
    WaitChrThread(0x22, 1)
    BeginChrThread(0x22, 0, 0, 51)
    OP_95(0x22, 4710, 0, -15670, 7000, 0x0)
    OP_95(0x22, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x22, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_54_131F5 end

    def Function_55_1326A(): pass

    label("Function_55_1326A")


    def lambda_1326F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_1326F)

    def lambda_13280():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_13280)
    WaitChrThread(0x23, 1)
    BeginChrThread(0x23, 0, 0, 51)
    OP_95(0x23, 6990, 0, -13880, 7000, 0x0)
    OP_95(0x23, 830, 0, -10410, 7000, 0x0)
    OP_95(0x23, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x23, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_55_1326A end

    def Function_56_132F3(): pass

    label("Function_56_132F3")


    def lambda_132F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_132F8)

    def lambda_13309():
        OP_9D(0xFE, 0x2ADA, 0x0, 0xFFFFBC8A, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_13309)
    WaitChrThread(0x24, 1)
    BeginChrThread(0x24, 0, 0, 51)
    OP_95(0x24, 4710, 0, -15670, 7000, 0x0)
    OP_95(0x24, -2120, 0, -1730, 7000, 0x0)
    OP_95(0x24, -2120, 0, 14270, 7000, 0x0)
    Return()

    # Function_56_132F3 end

    def Function_57_13368(): pass

    label("Function_57_13368")

    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    BeginChrThread(0x20, 0, 0, 51)
    OP_95(0xFE, -6100, 0, 14940, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_57_13368 end

    def Function_58_133B3(): pass

    label("Function_58_133B3")

    SetChrChipByIndex(0x21, 0x2E)
    SetChrSubChip(0x21, 0x0)
    BeginChrThread(0x21, 0, 0, 51)
    OP_95(0xFE, -6100, 0, 14940, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_58_133B3 end

    def Function_59_133FE(): pass

    label("Function_59_133FE")

    SetChrChipByIndex(0x22, 0x2E)
    SetChrSubChip(0x22, 0x0)
    BeginChrThread(0x22, 0, 0, 51)
    OP_95(0xFE, -6100, 0, 14940, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_59_133FE end

    def Function_60_13449(): pass

    label("Function_60_13449")

    SetChrChipByIndex(0x23, 0x2E)
    SetChrSubChip(0x23, 0x0)
    BeginChrThread(0x23, 0, 0, 51)
    OP_95(0xFE, 3670, 0, 15480, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_60_13449 end

    def Function_61_13494(): pass

    label("Function_61_13494")

    SetChrChipByIndex(0x24, 0x2E)
    SetChrSubChip(0x24, 0x0)
    BeginChrThread(0x24, 0, 0, 51)
    OP_95(0xFE, 3670, 0, 15480, 7000, 0x0)
    OP_95(0xFE, -1910, 0, 11190, 7000, 0x0)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1B58, 0x0)
    Return()

    # Function_61_13494 end

    def Function_62_134DF(): pass

    label("Function_62_134DF")

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

    # Function_62_134DF end

    def Function_63_1353E(): pass

    label("Function_63_1353E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13557")
    Sound(845, 0, 80, 0)
    Sleep(350)
    Jump("Function_63_1353E")

    label("loc_13557")

    Return()

    # Function_63_1353E end

    def Function_64_13558(): pass

    label("Function_64_13558")

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

    def lambda_13612():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13612)
    Sleep(50)

    def lambda_1362A():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1362A)
    Sleep(50)

    def lambda_13642():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13642)
    Sleep(50)

    def lambda_1365A():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1365A)
    Sleep(50)

    def lambda_13672():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13672)
    Sleep(50)

    def lambda_1368A():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1368A)
    OP_68(1050, 1500, -9540, 3000)
    SetCameraDistance(17450, 3000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_136C3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_136C3)
    WaitChrThread(0x101, 1)

    def lambda_136D4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_136D4)
    WaitChrThread(0x102, 1)

    def lambda_136E5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_136E5)
    WaitChrThread(0x103, 1)

    def lambda_136F6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_136F6)
    WaitChrThread(0x104, 1)

    def lambda_13707():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13707)
    WaitChrThread(0x109, 1)

    def lambda_13718():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_13718)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00000FI went to Almorica village ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FMr. Gebal somewhere in this village …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FAnyway, a dubious place\x01",
            "When you look for it, it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FEven people in the village who heard the story\x01",
            "It might be nice.\x02",
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

    # Function_64_13558 end

    def Function_65_1383B(): pass

    label("Function_65_1383B")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lock on the door.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1395C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_END)), "loc_138DA")

    ChrTalk(
        0x101,
        (
            "#00000F…… Let's consult with the mayor once.\x01",
            "You might know something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13958")

    label("loc_138DA")


    ChrTalk(
        0x101,
        (
            "#00003FThere is a sign that some people are inside … …\x02\x03",
            "#00000FAnyway keep listening.\x01",
            "If you live in a village\x01",
            "You may understand something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13958")

    TalkEnd(0xFF)
    Return()

    label("loc_1395C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1396E")
    TalkEnd(0xFF)
    Jump("loc_13D11")

    label("loc_1396E")

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
        "#00105FLloyd, Here it is …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWhen I came before,\x01",
            "Did you get a key …?\x02",
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
        "#10105FThe sound of now ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F…… Looks like there are people inside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FYes, I think so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHuh, you are suspicious suspicious.\x02",
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_END)), "loc_13C51")

    ChrTalk(
        0x101,
        "#00003Fperhaps……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00001F…… Let's consult with the mayor once.\x01",
            "You might know something.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x90, 0x1, 0x6)
    Jump("loc_13CD8")

    label("loc_13C51")

    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F……Anyways,\x01",
            "Leave me here for a moment\x01",
            "Let's continue listening.\x02\x03",
            "#00001FIf you live in a village\x01",
            "You may understand something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13CD8")

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

    label("loc_13D11")

    Return()

    # Function_65_1383B end

    def Function_66_13D12(): pass

    label("Function_66_13D12")

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
            "…… It is Turta of the mayor.\x01",
            "Is it a little better?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I want to talk with you\x01",
            "Those are coming.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(330, 20, -1, -1)
    SetChrName("Middle-aged voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "…………!\x02\x03",
            "Or, to return\x01",
            "Could you please say that?\x02\x03",
            "We are sorry for the inconvenience,\x01",
            "I want to see anyone for a while\x01",
            "It is not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "… … Safety.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I mean I came to see you\x01",
            "You are not your son and couple.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Middle-aged voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Why is that … …! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FMr. Geval, can you hear it?\x02\x03",
            "#00000FCrossbell Police,\x01",
            "It is a person of the affairs support department.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Middle-aged voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If it's police …! Is it?\x02\x03",
            "Well, what for you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F… … Sorry to have heard of you suddenly.\x02\x03",
            "#00000FWe are from Alm\x01",
            "Upon receiving a request,\x01",
            "I was searching for you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Middle-aged voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Become Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FBut, like forcibly taking me\x01",
            "I will not do things,\x01",
            "I do not have that authority.\x02\x03",
            "#00004FIf you say absolutely\x01",
            "Talking to the alms about the situation,\x01",
            "You can have the request withdrawn.\x02\x03",
            "#00000FWhether you just talk\x01",
            "Would you mind telling me?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Middle-aged voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "………………………………\x02",
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
        "#00100FYou seem to have opened the key.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAh……\x01",
            "Well then, let's try entering.\x02",
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

    # Function_66_13D12 end

    def Function_67_14347(): pass

    label("Function_67_14347")

    OP_93(0x101, 0x0, 0x0)

    def lambda_14353():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14353)

    def lambda_14368():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14368)
    Return()

    # Function_67_14347 end

    def Function_68_14375(): pass

    label("Function_68_14375")

    OP_95(0x102, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x102, 0x0, 0x0)

    def lambda_14395():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14395)

    def lambda_143AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_143AA)
    Return()

    # Function_68_14375 end

    def Function_69_143B7(): pass

    label("Function_69_143B7")

    OP_95(0x103, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x103, 0x0, 0x0)

    def lambda_143D7():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_143D7)

    def lambda_143EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_143EC)
    Return()

    # Function_69_143B7 end

    def Function_70_143F9(): pass

    label("Function_70_143F9")

    OP_95(0x104, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x104, 0x0, 0x0)

    def lambda_14419():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14419)

    def lambda_1442E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1442E)
    Return()

    # Function_70_143F9 end

    def Function_71_1443B(): pass

    label("Function_71_1443B")

    OP_95(0x109, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x109, 0x0, 0x0)

    def lambda_1445B():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1445B)

    def lambda_14470():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_14470)
    Return()

    # Function_71_1443B end

    def Function_72_1447D(): pass

    label("Function_72_1447D")

    OP_95(0x105, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x105, 0x0, 0x0)

    def lambda_1449D():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1449D)

    def lambda_144B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_144B2)
    Return()

    # Function_72_1447D end

    def Function_73_144BF(): pass

    label("Function_73_144BF")

    OP_95(0x1D, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0x1D, 0x0, 0x0)

    def lambda_144DF():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_144DF)

    def lambda_144F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_144F4)
    Return()

    # Function_73_144BF end

    def Function_74_14501(): pass

    label("Function_74_14501")

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
        "Among them, there is a father, is not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, there is no mistake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FI will see you from now\x01",
            "I also have a promise.\x02",
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
            "To be honest, why in such a place\x01",
            "I do not know if it was hiding, but …\x01",
            "I was really saved.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    ChrTalk(
        0x27,
        (
            "Hehe, it was good Alum.\x01",
            "At last\x01",
            "I can meet your father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "I could not call on my wedding.\x01",
            "Including apologies, properly\x01",
            "I have to say hello.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    ChrTalk(
        0x26,
        (
            "Oh Airy ……\x01",
            "How come your heart so much\x01",
            "Beautiful?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "To your transparent mind like new snow,\x01",
            "My heart is nailed ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "Oh, Alm ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F#4SPlease go into the barn.\x02",
    )

    CloseMessageWindow()

    def lambda_1487E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_1487E)
    Sleep(50)

    def lambda_1488E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1488E)
    Sleep(300)

    ChrTalk(
        0x26,
        "Happy …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "Uhufu, I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Alo, also Almin.\x01",
            "I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x27,
        "baby",
        "Bubuu.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "You can be well done ~ ~.\x02",
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
        "#10106F(One, I'm tired, is not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Anyway\x01",
            "We are waiting for you by David.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FGiggle\x01",
            "Talk to your heart's content\x01",
            "Enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        "Oh, I will let you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    ChrTalk(
        0x26,
        "Let's go, Airy.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    ChrTalk(
        0x27,
        "Yeah, Alm.\x02",
    )

    CloseMessageWindow()

    def lambda_14AC2():
        OP_95(0xFE, 15770, 3500, 47280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_14AC2)
    Sleep(300)

    def lambda_14ADF():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_14ADF)

    def lambda_14AF4():

        label("loc_14AF4")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_14AF4")

    QueueWorkItem2(0x101, 1, lambda_14AF4)
    Sleep(50)

    def lambda_14B09():

        label("loc_14B09")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_14B09")

    QueueWorkItem2(0x102, 1, lambda_14B09)
    Sleep(50)

    def lambda_14B1E():

        label("loc_14B1E")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_14B1E")

    QueueWorkItem2(0x103, 1, lambda_14B1E)
    Sleep(50)

    def lambda_14B33():

        label("loc_14B33")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_14B33")

    QueueWorkItem2(0x104, 1, lambda_14B33)
    Sleep(50)

    def lambda_14B48():

        label("loc_14B48")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_14B48")

    QueueWorkItem2(0x109, 1, lambda_14B48)
    Sleep(50)

    def lambda_14B5D():

        label("loc_14B5D")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_14B5D")

    QueueWorkItem2(0x105, 1, lambda_14B5D)
    Sleep(50)

    def lambda_14B72():

        label("loc_14B72")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_14B72")

    QueueWorkItem2(0x1D, 1, lambda_14B72)
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

    # Function_74_14501 end

    def Function_75_14C04(): pass

    label("Function_75_14C04")

    OP_95(0xFE, 15770, 3500, 47280, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x0)

    def lambda_14C24():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14C24)

    def lambda_14C39():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14C39)
    Return()

    # Function_75_14C04 end

    def Function_76_14C46(): pass

    label("Function_76_14C46")

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
        "Everyone, thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Thanks also to see my father,\x01",
            "I was able to introduce Airy and Armin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Huhu, your father-in-law?\x01",
            "I was very happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, I'm glad I got used to power.\x02\x03",
            "#00005FEr, Mr. Gebal …\x01",
            "Are you still inside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Oh, something I want to think about\x01",
            "I'm going home later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "I suddenly turned to the back in the middle of talking,\x01",
            "You will not show me your face at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "I wonder what the heck is doing ……\x02",
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
        "HM……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FWell, that is ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00304FIt is also in the eyes of a lawmaker.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FIt is a surprise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FGiggle\x01",
            "Well, here it is softly\x01",
            "It is a man 's duty.\x02",
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
            "#00009FHaha, so surely it's okay\x01",
            "Please do not worry.\x02\x03",
            "#00000FWhat will the two of you do from now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Oh, with my father\x01",
            "I was able to meet again … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "From now on contact\x01",
            "Let's keep in touch\x01",
            "It was a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Because there are things about your mother\x01",
            "It may not be easy\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "Eventually to the Kingdom of Libert\x01",
            "I am planning to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FIs that so……\x01",
            "Huhu, I hope it will work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Dad also members\x01",
            "It seems I quit,\x01",
            "Surely it will be so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Yes … to us\x01",
            "A brilliant future is waiting!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    ChrTalk(
        0x26,
        "Oh, Airy!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    ChrTalk(
        0x27,
        "Yeah, Alm!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "When I first held this child,\x01",
            "I swore by two people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "From now on to Armin,\x01",
            "I got a lot of brothers and sisters ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "…… me and you, and\x01",
            "Lots of lovable children … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "Everyone builds a continental first family.\x01",
            "… That was right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        "Oh, I love you Airy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "Me too, Alm! It is!\x02",
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
            "#00006F(What are you going to hear so far?\x01",
            "I did not have it ….\x01",
            "Well, okay. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell then, for now\x01",
            "Is it possible to meet your request?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1557C():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_1557C)
    Sleep(50)

    def lambda_1558C():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1558C)
    Sleep(300)

    ChrTalk(
        0x26,
        (
            "Oh, really thank you.\x01",
            "No matter how much you say a thank you\x01",
            "It is about enough to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "If we do a little more\x01",
            "I will return to Libert.\x01",
            "Thank you so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FWell, please be careful.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x27, 500)
    Sleep(300)

    ChrTalk(
        0x26,
        (
            "Well then Airy,\x01",
            "It's been a long time, so for a while\x01",
            "Let's go sightseeing here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x26, 500)
    Sleep(300)

    ChrTalk(
        0x27,
        "Yeah Alm, let's do that.\x02",
    )

    CloseMessageWindow()
    OP_93(0x27, 0x87, 0x0)

    def lambda_156E4():
        OP_9B(0x1, 0xFE, 0xB4, 0x262, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_156E4)
    Sleep(100)

    def lambda_156FC():
        OP_95(0xFE, 13050, 3500, 45510, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_156FC)
    WaitChrThread(0x26, 1)
    OP_93(0x27, 0xE1, 0x1F4)
    Sleep(500)
    OP_68(12010, 5000, 41990, 4000)
    MoveCamera(340, 27, 0, 4000)
    OP_6E(600, 4000)

    def lambda_15749():
        OP_95(0xFE, 7890, 3500, 42250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_15749)

    def lambda_15763():
        OP_95(0xFE, 6900, 3500, 42860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_15763)

    def lambda_1577D():

        label("loc_1577D")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_1577D")

    QueueWorkItem2(0x101, 1, lambda_1577D)
    Sleep(50)

    def lambda_15792():

        label("loc_15792")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_15792")

    QueueWorkItem2(0x102, 1, lambda_15792)
    Sleep(50)

    def lambda_157A7():

        label("loc_157A7")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_157A7")

    QueueWorkItem2(0x103, 1, lambda_157A7)
    Sleep(50)

    def lambda_157BC():

        label("loc_157BC")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_157BC")

    QueueWorkItem2(0x104, 1, lambda_157BC)
    Sleep(50)

    def lambda_157D1():

        label("loc_157D1")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_157D1")

    QueueWorkItem2(0x109, 1, lambda_157D1)
    Sleep(50)

    def lambda_157E6():

        label("loc_157E6")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_157E6")

    QueueWorkItem2(0x105, 1, lambda_157E6)
    Sleep(50)

    def lambda_157FB():

        label("loc_157FB")

        TurnDirection(0xFE, 0x26, 500)
        Yield()
        Jump("loc_157FB")

    QueueWorkItem2(0x1D, 1, lambda_157FB)
    WaitChrThread(0x26, 1)
    WaitChrThread(0x27, 1)

    def lambda_15815():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_15815)

    def lambda_15822():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_15822)
    OP_6F(0x79)

    def lambda_15831():
        TurnDirection(0xFE, 0x27, 500)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_15831)

    def lambda_1583E():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1583E)
    Sleep(500)

    ChrTalk(
        0x26,
        "Haha, Airy spout\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "Uhufu, you spray\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x27,
        "baby",
        "Bubu ~.\x02",
    )

    CloseMessageWindow()

    def lambda_15893():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_15893)

    def lambda_158A0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_158A0)
    Sleep(300)

    def lambda_158B0():
        OP_95(0xFE, 4830, 2000, 38020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_158B0)

    def lambda_158CA():
        OP_95(0xFE, 4470, 2000, 39100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_158CA)
    Sleep(1000)
    OP_68(15240, 5000, 43490, 5000)
    MoveCamera(5, 29, 0, 5000)
    OP_6E(600, 5000)
    WaitChrThread(0x26, 1)

    def lambda_15910():
        OP_95(0xFE, 1480, 2000, 40200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_15910)
    Sleep(100)

    def lambda_1592D():
        OP_95(0xFE, 1940, 2000, 41000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1592D)
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
            "#00006F……from the beggining to the end,\x01",
            "It has a great impact\x01",
            "People …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHuhu, really.\x01",
            "As I go there\x01",
            "On the other hand I'm jealous … …\x02\x03",
            "#00104FI have been with my parents for the first time in a while\x01",
            "I wanted to see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FMr. Erie - san …\x02\x03",
            "#10109FHehe, it is.\x01",
            "I also had a lot of filial piety on my mother\x01",
            "I feel like wanting to do it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1D,
        (
            "Well, at the same time also\x01",
            "I would like to thank you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15AE6():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15AE6)
    Sleep(50)

    def lambda_15AF6():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15AF6)
    Sleep(50)

    def lambda_15B06():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_15B06)
    Sleep(50)

    def lambda_15B16():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_15B16)
    Sleep(50)

    def lambda_15B26():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_15B26)
    Sleep(50)

    def lambda_15B36():
        TurnDirection(0xFE, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_15B36)
    Sleep(300)

    ChrTalk(
        0x1D,
        (
            "Gabal is calm\x01",
            "Until we return to the city, neatly\x01",
            "I will take care of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYes, we cooperate in various ways\x01",
            "Thank you very much.\x02\x03",
            "#00000FLet's suppose that we are about to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, I understand.\x02",
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
            "Quest 【Searching for living fathers】\x07\x00",
            "Achieved!\x02",
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

    # Function_76_14C46 end

    def Function_77_15D0A(): pass

    label("Function_77_15D0A")

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

    def lambda_15E3F():
        OP_96(0xFE, 0xFFFF4C50, 0x1900, 0x15F90, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_15E3F)

    def lambda_15E59():
        OP_96(0xFE, 0xFFFF4C50, 0x1900, 0x15F90, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_15E59)
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

    def lambda_15FB7():
        OP_96(0xFE, 0xFFFF4C50, 0x6720, 0x15F90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_15FB7)

    def lambda_15FD1():
        OP_96(0xFE, 0xFFFF4C50, 0x6720, 0x15F90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_15FD1)
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
            "#10406F#6POk then we got here safely\x02\x03",
            "#10408F…… But here,\x01",
            "It is a village's astragalus field, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#6PAh……\x01",
            "Though the appearance has changed a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12P…… also Ka'a awaked this\x01",
            "It may be an influence.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-17020, 5600, 61730, 1000)
    TurnDirection(0x103, 0x107, 400)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        (
            "#00201F#5PZeit.\x01",
            "How about the eidolon?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1617E():
        TurnDirection(0x101, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1617E)
    Sleep(0)

    def lambda_1618E():
        TurnDirection(0x105, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1618E)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x107,
        (
            "#01203F#12P#3C#NHmm, for now\x01",
            "There is no indication of appearance.\x02\x03",
            "#01200FFor the time being, we\x01",
            "You can rely on it without problems.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#5PUnderstood\x02\x03",
            "#00001FFor the time being to the mayor of Torta\x01",
            "It seems better to say hello.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#11PYes.\x01",
            "Let's go.\x02",
        )
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

    # Function_77_15D0A end

    def Function_78_162BE(): pass

    label("Function_78_162BE")

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

    # Function_78_162BE end

    def Function_79_16303(): pass

    label("Function_79_16303")

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

    # Function_79_16303 end

    def Function_80_16351(): pass

    label("Function_80_16351")

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

    # Function_80_16351 end

    def Function_81_163B6(): pass

    label("Function_81_163B6")

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

    def lambda_164B8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_164B8)
    BeginChrThread(0x101, 1, 0, 82)
    Sleep(1000)

    def lambda_164D2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_164D2)
    BeginChrThread(0x103, 1, 0, 83)
    Sleep(1000)

    def lambda_164EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_164EC)
    BeginChrThread(0x105, 1, 0, 84)
    Sleep(1000)

    def lambda_16506():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_16506)
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
            "#10404F#12POk then\x02\x03",
            "#10400FWell then at the battlefield\x01",
            "Is it okay if I go to go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6POh, that resistance faction\x01",
            "I do not know who it is.\x02\x03",
            "#00001FPerhaps we both\x01",
            "It may be possible to collaborate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#5PI agree……\x01",
            "It is worth exploring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01200F#11P#3COk then let's head that way\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 17950, 0, 16250, 180)
    SetScenarioFlags(0x1A1, 5)
    OP_29(0xAF, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_81_163B6 end

    def Function_82_1669D(): pass

    label("Function_82_1669D")

    OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x101, 17500, 0, 14850, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_82_1669D end

    def Function_83_166C8(): pass

    label("Function_83_166C8")

    OP_9B(0x0, 0x103, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x103, 16900, 0, 16550, 2000, 0x0)
    OP_93(0x103, 0x87, 0x1F4)
    Return()

    # Function_83_166C8 end

    def Function_84_166F3(): pass

    label("Function_84_166F3")

    OP_9B(0x0, 0x105, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x105, 18950, 0, 16100, 2000, 0x0)
    OP_93(0x105, 0xE1, 0x1F4)
    Return()

    # Function_84_166F3 end

    def Function_85_1671E(): pass

    label("Function_85_1671E")

    OP_9B(0x0, 0x107, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_95(0x107, 18000, 0, 17750, 2000, 0x0)
    OP_93(0x107, 0xB4, 0x1F4)
    SetChrSubChip(0x107, 0x5)
    Return()

    # Function_85_1671E end

    def Function_86_1674D(): pass

    label("Function_86_1674D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    FadeToBright(1000, 0)
    Call(0, 87)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A0E")
    Fade(500)
    OP_68(15510, 1350, -23710, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16913")
    SetChrPos(0x101, 21180, 0, -27450, 315)
    SetChrPos(0x104, 22100, 0, -28790, 315)
    SetChrPos(0x105, 23130, 0, -30790, 315)
    SetChrPos(0x102, 20230, 0, -28520, 315)
    SetChrPos(0x103, 20790, 0, -30560, 315)
    SetChrPos(0x109, 22200, 0, -31420, 315)

    def lambda_1684A():
        OP_95(0xFE, 15110, 0, -21470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1684A)

    def lambda_16864():
        OP_95(0xFE, 16020, 0, -22930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16864)

    def lambda_1687E():
        OP_95(0xFE, 16930, 0, -24390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1687E)

    def lambda_16898():
        OP_95(0xFE, 13980, 0, -22200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16898)

    def lambda_168B2():
        OP_95(0xFE, 14940, 0, -23710, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_168B2)

    def lambda_168CC():
        OP_95(0xFE, 15900, 0, -25220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_168CC)
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
    Jump("loc_16A09")

    label("loc_16913")

    SetChrPos(0x101, 21180, 0, -27450, 315)
    SetChrPos(0x104, 22100, 0, -28790, 315)
    SetChrPos(0x102, 20230, 0, -28520, 315)
    SetChrPos(0x109, 21290, 0, -30060, 315)
    SetChrPos(0x105, 22810, 0, -31000, 315)

    def lambda_1696D():
        OP_95(0xFE, 15110, 0, -21470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1696D)

    def lambda_16987():
        OP_95(0xFE, 16020, 0, -22930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16987)

    def lambda_169A1():
        OP_95(0xFE, 13980, 0, -22200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_169A1)

    def lambda_169BB():
        OP_95(0xFE, 14940, 0, -23710, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_169BB)

    def lambda_169D5():
        OP_95(0xFE, 16410, 0, -24800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_169D5)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    label("loc_16A09")

    Jump("loc_16E7F")

    label("loc_16A0E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C63")
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

    def lambda_16ABD():
        OP_95(0xFE, 15110, 0, -21470, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_16ABD)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16BF5")
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
    Jump("loc_16C54")

    label("loc_16BF5")

    SetChrPos(0x101, 11870, 0, -18060, 315)
    SetChrPos(0x104, 12780, 0, -19520, 315)
    SetChrPos(0x102, 10840, 0, -18790, 315)
    SetChrPos(0x109, 11800, 0, -20300, 315)
    SetChrPos(0x105, 13220, 0, -21400, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_16C54")

    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_16E7F")

    label("loc_16C63")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16E16")
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
    Jump("loc_16E75")

    label("loc_16E16")

    SetChrPos(0x101, 1030, 0, -12060, 0)
    SetChrPos(0x104, 1940, 0, -13520, 0)
    SetChrPos(0x102, 0, 0, -12790, 0)
    SetChrPos(0x109, 960, 0, -14300, 0)
    SetChrPos(0x105, 2380, 0, -15400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_16E75")

    FadeToBright(1000, 0)
    OP_0D()

    label("loc_16E7F")


    ChrTalk(
        0x105,
        (
            "#12P#10302FOh, it is a scenic place.\x02\x03",
            "#10304FCertainly, was it \"Almorika village\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, I see.\x02\x03",
            "#00104FBeekeeping industry, agriculture, pastoralism\x01",
            "Village with main industry ……\x02\x03",
            "#00102FThe legend of \"God Wolf\" still remains\x01",
            "It is also a few places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004Fby the way……\x01",
            "The mission support section is the first\x01",
            "It was a place where I did activities outside the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FMafia's military dog incident ……\x01",
            "Hehe, it is nostalgic.\x02\x03",
            "#10103FAt that time, our survey\x01",
            "To delegate to the support department\x01",
            "It is becoming it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, that was also incompetent former commander\x01",
            "It was a cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FBoth Huhu and Zeit\x01",
            "I have a relationship since that incident.\x02\x03",
            "#00104FHelp me with the last big pinch,\x01",
            "I was able to solve the incident thanks to you.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_171AD")

    ChrTalk(
        0x101,
        (
            "#00009FFrom that time on to Zeit\x01",
            "I am being helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FYeah, not just battle\x01",
            "Support in various scenes\x01",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1722C")

    label("loc_171AD")


    ChrTalk(
        0x101,
        (
            "#00009FFrom that time on to Zeit\x01",
            "I am being helped.\x02\x03",
            "#00004FNot just battle\x01",
            "Support in various scenes\x01",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1722C")


    ChrTalk(
        0x105,
        (
            "#12P#10304FHuh, you can not help being something\x01",
            "I think that it is not limited to Zeito.\x02\x03",
            "#10309FRather, it is that you get a good place\x01",
            "The fate of the support department is a guy.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_172C1():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_172C1)

    def lambda_172CE():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_172CE)

    def lambda_172DB():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_172DB)

    def lambda_172E8():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_172E8)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17385")

    def lambda_17365():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_17365)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_17385")

    Sleep(1000)

    ChrTalk(
        0x109,
        "#6P#10106FWow, Wazi ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FI wish I could catch a painful place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, well ….\x01",
            "We are also growing up,\x01",
            "That is a future subject.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x14E, 7)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17452")
    SetChrPos(0x0, 15500, 0, -23930, 315)
    Jump("loc_17487")

    label("loc_17452")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17476")
    SetChrPos(0x0, 11350, 0, -18420, 315)
    Jump("loc_17487")

    label("loc_17476")

    SetChrPos(0x0, 890, 0, -13080, 315)

    label("loc_17487")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_174AB")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_174AB")

    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_86_1674D end

    def Function_87_174B7(): pass

    label("Function_87_174B7")

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

    # Function_87_174B7 end

    def Function_88_17598(): pass

    label("Function_88_17598")

    Sleep(500)
    Sound(459, 0, 100, 0)
    Sleep(1200)
    Sleep(1500)
    Sound(492, 0, 90, 0)
    Return()

    # Function_88_17598 end

    def Function_89_175AE(): pass

    label("Function_89_175AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178E7")
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

    def lambda_1769C():
        OP_93(0x107, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1769C)
    Sleep(0)

    def lambda_176AC():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_176AC)
    Sleep(0)

    def lambda_176BC():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_176BC)
    Sleep(0)

    def lambda_176CC():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_176CC)
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
            "#12P#00000FThis guided vehicle ……\x01",
            "It's Harold's car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FPassenger car made by Verne … …\x01",
            "I have once got on a ride,\x01",
            "I think there is no mistake.\x02\x03",
            "#00203FIn the story of the mayor, on the second floor of the hotel\x01",
            "Although it was that he was staying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10403FNow I want information at least even one.\x02\x03",
            "#10400FBefore going out to the highway\x01",
            "You may as well listen to the story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FOh, let's go.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1AD, 6)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 11950, 0, -17850, 0)
    EventEnd(0x5)
    Jump("loc_1795E")

    label("loc_178E7")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FHarold in the village\x01",
            "She seems to be staying.\x02\x03",
            "Before going out to the highway,\x01",
            "Let's visit the second floor of the inn.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 17090, 0, -25640, 321)
    EventEnd(0x4)

    label("loc_1795E")

    Return()

    # Function_89_175AE end

    SaveToFile()

Try(main)
