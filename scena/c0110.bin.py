from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0110.bin",                # FileName
        "c0110",                    # MapName
        "c0110",                    # Location
        0x0009,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 9, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0110",                  # 0
        "Sergey Manager",           # 1
        "Keya",                 # 2
        "Zeit",               # 3
        "Cecil",                 # 4
        "Coppe",                 # 5
        "Cat food",         # 6
        "Voice of Grace",           # 7
        "Dishes",                   # 8
        "Dishes",                   # 9
        "Dishes",                   # 10
        "Dishes",                   # 11
        "Dishes",                   # 12
        "Dishes",                   # 13
        "Dishes",                   # 14
        "Dishes",                   # 15
        "Dishes",                   # 16
        "Dishes",                   # 17
        "Dishes",                   # 18
        "Dishes",                   # 19
        "Dishes",                   # 20
        "Dishes",                   # 21
        "Dishes",                   # 22
        "Dishes",                   # 23
        "Dishes",                   # 24
        "Dishes",                   # 25
        "Dishes",                   # 26
        "Chair",                   # 27
        "Chair",                   # 28
        "Chair",                   # 29
        "Chair",                   # 30
        "Chair",                   # 31
        "Chair",                   # 32
        "Chair",                   # 33
        "Chair",                   # 34
        "Phantom Beast Investigation Report",       # 35
        "dummy",                 # 36
        "doll",                   # 37
    ))

    AddCharChip((
        "chr/ch02500.itc",                   # 00
        "chr/ch02502.itc",                   # 01
        "chr/ch08200.itc",                   # 02
        "chr/ch08202.itc",                   # 03
        "chr/ch02707.itc",                   # 04
        "chr/ch02708.itc",                   # 05
        "chr/ch02702.itc",                   # 06
        "chr/ch14300.itc",                   # 07
        "chr/ch39200.itc",                   # 08
        "apl/ch50092.itc",                   # 09
        "chr/ch14302.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
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

    DeclNpc(64000,   200,     11399,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(2710,    0,       2509,    225,  405,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    438,  0x0, 0,   9,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 13,  1.0,                   -0.5,                  -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.5,                  0.25,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 14,  -3.299999952316284,    68.0,                  -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.649999976158142,     -34.0,                 0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 64,  7.0,                   10.5,                  0.0,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -3.5,                  -2.0999999046325684,   -0.0,                  1.0])
    DeclEvent(0x0000, 0, 65,  11.0,                  13.5,                  0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -5.5,                  -6.75,                 -0.0,                  1.0])
    DeclEvent(0x0000, 0, 66,  19.0,                  4.0,                   0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -9.5,                  -2.0,                  -0.0,                  1.0])
    DeclEvent(0x0000, 0, 15,  1.0,                   71.5,                  0.0,                   9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -0.5,                  -23.83333396911621,    -0.0,                  1.0])

    DeclActor(16960,   850,     10840,   2000,    16960,   1300,    10840,   0x007C, 0,  18, 0x0000)
    DeclActor(13960,   0,       63640,   1500,    13960,   1500,    63640,   0x007C, 0,  12, 0x0000)
    DeclActor(170000,  0,       63560,   1500,    170000,  1500,    63560,   0x007C, 0,  11, 0x0000)
    DeclActor(64000,   30,      9800,    1500,    64000,   1500,    11400,   0x007E, 0,  4,  0x0000)
    DeclActor(63890,   30,      11070,   1500,    63890,   1000,    11070,   0x007C, 0,  63, 0x0000)

    ChipFrameInfo(2332, 0)                                       # 0

    ScpFunction((
        "Function_0_91C",          # 00, 0
        "Function_1_9CC",          # 01, 1
        "Function_2_9F7",          # 02, 2
        "Function_3_10A2",         # 03, 3
        "Function_4_1393",         # 04, 4
        "Function_5_1397",         # 05, 5
        "Function_6_2541",         # 06, 6
        "Function_7_3048",         # 07, 7
        "Function_8_3BAF",         # 08, 8
        "Function_9_3CF4",         # 09, 9
        "Function_10_3F1E",        # 0A, 10
        "Function_11_4363",        # 0B, 11
        "Function_12_43B6",        # 0C, 12
        "Function_13_440B",        # 0D, 13
        "Function_14_44C8",        # 0E, 14
        "Function_15_4585",        # 0F, 15
        "Function_16_45DC",        # 10, 16
        "Function_17_4898",        # 11, 17
        "Function_18_4B74",        # 12, 18
        "Function_19_5605",        # 13, 19
        "Function_20_5996",        # 14, 20
        "Function_21_5B23",        # 15, 21
        "Function_22_6678",        # 16, 22
        "Function_23_724F",        # 17, 23
        "Function_24_7C66",        # 18, 24
        "Function_25_935E",        # 19, 25
        "Function_26_9382",        # 1A, 26
        "Function_27_9CDC",        # 1B, 27
        "Function_28_9FB1",        # 1C, 28
        "Function_29_BAD6",        # 1D, 29
        "Function_30_C53E",        # 1E, 30
        "Function_31_CFB2",        # 1F, 31
        "Function_32_E928",        # 20, 32
        "Function_33_EDD2",        # 21, 33
        "Function_34_103B4",       # 22, 34
        "Function_35_10443",       # 23, 35
        "Function_36_10DBA",       # 24, 36
        "Function_37_10DF7",       # 25, 37
        "Function_38_11B65",       # 26, 38
        "Function_39_1226B",       # 27, 39
        "Function_40_12719",       # 28, 40
        "Function_41_14202",       # 29, 41
        "Function_42_1457F",       # 2A, 42
        "Function_43_16393",       # 2B, 43
        "Function_44_1735F",       # 2C, 44
        "Function_45_179D0",       # 2D, 45
        "Function_46_197E0",       # 2E, 46
        "Function_47_1982A",       # 2F, 47
        "Function_48_1987F",       # 30, 48
        "Function_49_198B6",       # 31, 49
        "Function_50_198FA",       # 32, 50
        "Function_51_1993E",       # 33, 51
        "Function_52_19976",       # 34, 52
        "Function_53_199A6",       # 35, 53
        "Function_54_1AA4A",       # 36, 54
        "Function_55_1AA9B",       # 37, 55
        "Function_56_1B580",       # 38, 56
        "Function_57_1B5F2",       # 39, 57
        "Function_58_1C605",       # 3A, 58
        "Function_59_1C689",       # 3B, 59
        "Function_60_1C6C6",       # 3C, 60
        "Function_61_1C703",       # 3D, 61
        "Function_62_1C765",       # 3E, 62
        "Function_63_1C893",       # 3F, 63
        "Function_64_1D22A",       # 40, 64
        "Function_65_1D285",       # 41, 65
        "Function_66_1D2E0",       # 42, 66
        "Function_67_1D33B",       # 43, 67
    ))


    def Function_0_91C(): pass

    label("Function_0_91C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_954"),
        (1, "loc_960"),
        (2, "loc_96C"),
        (3, "loc_978"),
        (4, "loc_984"),
        (5, "loc_990"),
        (6, "loc_99C"),
        (SWITCH_DEFAULT, "loc_9A8"),
    )


    label("loc_954")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_960")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_96C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_978")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_984")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_990")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_99C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_9A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_9B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9CB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9B4")

    label("loc_9CB")

    Return()

    # Function_0_91C end

    def Function_1_9CC(): pass

    label("Function_1_9CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9F6")
    OP_94(0xFE, 0x1D8DA, 0x1F18, 0x1E53C, 0x1360, 0x3E8)
    Sleep(300)
    Jump("Function_1_9CC")

    label("loc_9F6")

    Return()

    # Function_1_9CC end

    def Function_2_9F7(): pass

    label("Function_2_9F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD5")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A2F")
    Jump("loc_AD0")

    label("loc_A2F")

    SetChrPos(0x0, -2190, 0, 68010, 90)
    SetChrPos(0x1, -2190, 0, 68010, 90)
    SetChrPos(0x2, -2190, 0, 68010, 90)
    SetChrPos(0x3, -2190, 0, 68010, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AA8")
    SetChrPos(0x4, -2190, 0, 68010, 90)
    SetChrPos(0x5, -2190, 0, 68010, 90)
    Jump("loc_AC7")

    label("loc_AA8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC7")
    SetChrPos(0x4, -2190, 0, 68010, 90)

    label("loc_AC7")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AD0")

    Jump("loc_AD5")

    label("loc_AD5")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AF1")
    SetChrFlags(0x8, 0x80)
    Jump("loc_F3C")

    label("loc_AF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B35")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 122700, 0, 6000, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 121800, 0, 6000, 0)
    Jump("loc_F3C")

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B48")
    SetChrFlags(0x8, 0x80)
    Jump("loc_F3C")

    label("loc_B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BC3")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0x9, 5570, 150, 6230, 180)
    SetChrChipByIndex(0xA, 0x5)
    SetChrPos(0xA, 3470, 30, 6380, 180)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0xA)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, 5450, 150, 2100, 0)
    Jump("loc_F3C")

    label("loc_BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BE2")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_F3C")

    label("loc_BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_C17")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 3470, 30, 6380, 180)
    Jump("loc_F3C")

    label("loc_C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C73")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0x9, 5570, 150, 6230, 180)
    SetChrPos(0xA, 3470, 30, 6380, 180)
    Jump("loc_F3C")

    label("loc_C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CD4")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 117660, 30, 8100, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 119610, 30, 4470, 225)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 117430, 30, 4080, 90)
    Jump("loc_F3C")

    label("loc_CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D0D")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x5)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    Jump("loc_F3C")

    label("loc_D0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D42")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    Jump("loc_F3C")

    label("loc_D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D6B")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    Jump("loc_F3C")

    label("loc_D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D7E")
    SetChrFlags(0x8, 0x80)
    Jump("loc_F3C")

    label("loc_D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_DDA")
    SetChrPos(0x8, 14400, 850, 12500, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0x9, 5570, 150, 6230, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    Jump("loc_F3C")

    label("loc_DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_END)), "loc_E25")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 117660, 30, 8100, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 119610, 30, 4470, 225)
    Jump("loc_F3C")

    label("loc_E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_E70")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 123270, 0, 4980, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 119610, 30, 4470, 225)
    Jump("loc_F3C")

    label("loc_E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_EA5")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    Jump("loc_F3C")

    label("loc_EA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_EDD")
    SetChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ED8")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 65890, 0, 1800, 225)

    label("loc_ED8")

    Jump("loc_F3C")

    label("loc_EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_F2E")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 122060, 0, 5750, 45)
    BeginChrThread(0xC, 0, 0, 1)
    Jump("loc_F3C")

    label("loc_F2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_F3C")
    SetChrFlags(0x8, 0x80)

    label("loc_F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_F50")
    ClearScenarioFlags(0x22, 0)
    Event(0, 23)
    Jump("loc_1063")

    label("loc_F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_F61")
    ClearScenarioFlags(0x22, 1)
    Jump("loc_1063")

    label("loc_F61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_F75")
    ClearScenarioFlags(0x22, 2)
    Event(0, 26)
    Jump("loc_1063")

    label("loc_F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_F86")
    Event(0, 28)
    Jump("loc_1063")

    label("loc_F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_F9A")
    ClearScenarioFlags(0x22, 4)
    Event(0, 31)
    Jump("loc_1063")

    label("loc_F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_FB1")
    ClearScenarioFlags(0x22, 5)
    SetScenarioFlags(0x0, 7)
    Event(0, 35)
    Jump("loc_1063")

    label("loc_FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_FC2")
    Event(0, 37)
    Jump("loc_1063")

    label("loc_FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_FD9")
    ClearScenarioFlags(0x22, 7)
    SetScenarioFlags(0x0, 7)
    Event(0, 38)
    Jump("loc_1063")

    label("loc_FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_FED")
    ClearScenarioFlags(0x23, 0)
    Event(0, 40)
    Jump("loc_1063")

    label("loc_FED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_1001")
    ClearScenarioFlags(0x23, 1)
    Event(0, 42)
    Jump("loc_1063")

    label("loc_1001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_1012")
    ClearScenarioFlags(0x23, 2)
    Jump("loc_1063")

    label("loc_1012")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_1026")
    ClearScenarioFlags(0x23, 3)
    Event(0, 43)
    Jump("loc_1063")

    label("loc_1026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_103D")
    ClearScenarioFlags(0x23, 4)
    SetScenarioFlags(0x0, 7)
    Event(0, 45)
    Jump("loc_1063")

    label("loc_103D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 5)), scpexpr(EXPR_END)), "loc_1054")
    ClearScenarioFlags(0x23, 5)
    SetScenarioFlags(0x0, 7)
    Event(0, 53)
    Jump("loc_1063")

    label("loc_1054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 6)), scpexpr(EXPR_END)), "loc_1063")
    ClearScenarioFlags(0x23, 6)
    Event(0, 55)

    label("loc_1063")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_108B")
    SetMapFlags(0x10000000)
    Event(0, 33)

    label("loc_108B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10A1")
    SetMapFlags(0x10000000)
    Event(0, 57)

    label("loc_10A1")

    Return()

    # Function_2_9F7 end

    def Function_3_10A2(): pass

    label("Function_3_10A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_10B7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 7)

    label("loc_10B7")

    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F0")
    OP_1B(0x0, 0x0, 0x1D)
    OP_1B(0x8, 0x0, 0x1E)

    label("loc_10F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1144")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_1144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_118E")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)

    label("loc_118E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11AF")
    SetMapObjFrame(0xFF, "tanmatu_add", 0x0, 0x1)

    label("loc_11AF")

    SetMapObjFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_11D2")
    SetMapObjFrame(0xFF, "asihuki", 0x0, 0x1)
    Jump("loc_11E1")

    label("loc_11D2")

    SetMapObjFrame(0xFF, "asihuki", 0x1, 0x1)

    label("loc_11E1")

    ClearMapObjFlags(0x3, 0x10)
    ClearMapObjFlags(0x6, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1200")
    SetMapObjFlags(0x3, 0x10)
    OP_65(0x1, 0x1)

    label("loc_1200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1213")
    SetMapObjFlags(0x6, 0x10)
    OP_65(0x2, 0x1)

    label("loc_1213")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1225")
    Jump("loc_1328")

    label("loc_1225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1233")
    Jump("loc_1328")

    label("loc_1233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1245")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_1245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_1257")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_1257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1269")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_1269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_127B")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_127B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_128D")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_128D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_129F")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_129F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_12AD")
    Jump("loc_1328")

    label("loc_12AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_12BB")
    Jump("loc_1328")

    label("loc_12BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_12C9")
    Jump("loc_1328")

    label("loc_12C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_END)), "loc_12DB")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_12DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_12ED")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_12ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_12FF")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_12FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_130D")
    Jump("loc_1328")

    label("loc_130D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_131F")
    OP_66(0x3, 0x1)
    Jump("loc_1328")

    label("loc_131F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1328")

    label("loc_1328")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1355")
    OP_66(0x4, 0x1)

    label("loc_1355")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1377")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1377")

    ModifyEventFlags(0, 5, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_138F")
    ModifyEventFlags(1, 5, 0x80)

    label("loc_138F")

    Call(0, 67)
    Return()

    # Function_3_10A2 end

    def Function_4_1393(): pass

    label("Function_4_1393")

    Call(0, 5)
    Return()

    # Function_4_1393 end

    def Function_5_1397(): pass

    label("Function_5_1397")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_13A8")
    Jump("loc_253D")

    label("loc_13A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_15CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1536")

    ChrTalk(
        0x8,
        (
            "#01000FRegarding the return to Noel's guard,\x01",
            "I will do the necessary procedures.\x02\x03",
            "By the influence of the attack incident everywhere\x01",
            "Since there is supposed to be a support request,\x01",
            "If you can afford it please do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, one day today\x01",
            "We will work with full power.\x02\x03",
            "#10103F……Sergey Manager、\x01",
            "Thank you for what you have done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004FWell, thank you.\x02\x03",
            "#01002FAt least not to regret,\x01",
            "You should concentrate on paying work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_15C6")

    label("loc_1536")


    ChrTalk(
        0x8,
        (
            "#01000FRegarding Noel's return to the guard,\x01",
            "I will keep the necessary procedures.\x02\x03",
            "#01004FBecause I go out to eat at night with my delicacy,\x01",
            "By the time you come back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C6")

    Jump("loc_253D")

    label("loc_15CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_1747")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16BC")

    ChrTalk(
        0x8,
        (
            "#01003FFinally grabbed Randy's footsteps.\x02\x03",
            "#01002FKuku, finally take back with this\x01",
            "I think it's okay to have a good settlement.\x02\x03",
            "#01001FDo not go fucking if you decide so.\x01",
            "Come back with that idiot for everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYeah … …!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1742")

    label("loc_16BC")


    ChrTalk(
        0x8,
        (
            "#01003FThe guard is now also a reinforcement unit\x01",
            "It is probably a place to restructure.\x02\x03",
            "#01001FDo not go fucking if you decide so.\x01",
            "Come bring Randy back with everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1742")

    Jump("loc_253D")

    label("loc_1747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_18F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_184F")

    ChrTalk(
        0x8,
        (
            "#01000FUnder the influence of the occupation case of Mainz direction,\x01",
            "There is no state of support request coming in.\x02\x03",
            "#01003FYou guys, Randy 's guy\x01",
            "You should focus on finding out.\x02\x03",
            "#01001FPlease do not forget to take care.\x01",
            "If I also find something I will contact you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes……!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_18F4")

    label("loc_184F")


    ChrTalk(
        0x8,
        (
            "#01003FToday there is no support request,\x01",
            "You guys, Randy 's guy\x01",
            "You should focus on finding out.\x02\x03",
            "#01001FPlease do not forget to take care.\x01",
            "If I also find something I will contact you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18F4")

    Jump("loc_253D")

    label("loc_18F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1A94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F9")

    ChrTalk(
        0x8,
        (
            "#01003FWaldo Valles and\x01",
            "In the case of Gnostic, the second division and the guard\x01",
            "We are proceeding with the investigation.\x02\x03",
            "#01000FNow that the restoration of the crossing railway is over,\x01",
            "You will not be impatient.\x02\x03",
            "Regarding the matter of the prime minister,\x01",
            "If I can afford, I have a job\x01",
            "You put your face on the guild.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1A8F")

    label("loc_19F9")


    ChrTalk(
        0x8,
        (
            "#01000FNow that the restoration of the crossing railway is over,\x01",
            "You will not be impatient.\x02\x03",
            "Regarding the matter of the prime minister,\x01",
            "If I can afford, I have a job\x01",
            "You put your face on the guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A8F")

    Jump("loc_253D")

    label("loc_1A94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1C33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B88")

    ChrTalk(
        0x8,
        (
            "#01000F… … Have you returned?\x01",
            "You seem to have contacted from Franc?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, from now to the accident scene\x01",
            "It is a place to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003FI see, I understand.\x02\x03",
            "#01000Fdoll工房の調査報告は後で聞く。\x01",
            "You are going to do what you can do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1C2E")

    label("loc_1B88")


    ChrTalk(
        0x8,
        (
            "#01000FOn the accident site of the West Crossbell Highway,\x01",
            "The guys in section two and Sonja\x01",
            "The guard should also be heading.\x02\x03",
            "doll工房の調査報告は後で聞く。\x01",
            "You are going to do what you can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C2E")

    Jump("loc_253D")

    label("loc_1C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1DE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D47")

    ChrTalk(
        0x8,
        (
            "#01006FIn the case of national independence referendum,\x01",
            "Different papers are coming.\x02\x03",
            "#01002FI've got questions to worry about ……\x01",
            "Well, leave this to another section.\x02\x03",
            "#01000FFor now, crisis management is the first choice.\x01",
            "doll工房の聞き込みだけじゃなく、\x01",
            "You should also cover support requests.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1DDB")

    label("loc_1D47")


    ChrTalk(
        0x8,
        (
            "#01004Fああ、Keyaならついさっき\x01",
            "It seems that I went shopping for dinner.\x02\x03",
            "#01002FI was somewhat close to the library … …\x01",
            "Well, if you worry, go get to see the situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDB")

    Jump("loc_253D")

    label("loc_1DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1F36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EB1")

    ChrTalk(
        0x8,
        (
            "#01000FYeah, I also just arrived\x01",
            "I came back from the hospital.\x02\x03",
            "#01003FIf you continue,\x01",
            "Advance the investigation of \"Phantom beast\".\x02\x03",
            "#01002FBefore the \"sword of the wind\" moved\x01",
            "You should at the most improve your results.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F31")

    label("loc_1EB1")


    ChrTalk(
        0x8,
        (
            "#01003FIf you continue,\x01",
            "Advance the investigation of \"Phantom beast\".\x02\x03",
            "#01002FBefore the \"sword of the wind\" moved\x01",
            "You should at the most improve your results.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F31")

    Jump("loc_253D")

    label("loc_1F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1F44")
    Jump("loc_253D")

    label("loc_1F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_20A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2027")

    ChrTalk(
        0x8,
        (
            "#01000FI got information on terrorists\x01",
            "Contact the mayor and the guard.\x02\x03",
            "Dudley, our folks\x01",
            "I ordered a talisman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FWell, please leave it to me.\x02\x03",
            "#00601F… …. Come on, you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_209B")

    label("loc_2027")


    ChrTalk(
        0x8,
        (
            "#01000FAt the Geo Front\x01",
            "I do not know what happened,\x01",
            "At best, be careful.\x02\x03",
            "Dudley, our folks\x01",
            "I ordered a talisman.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_209B")

    Jump("loc_253D")

    label("loc_20A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_2259")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B3")

    ChrTalk(
        0x8,
        (
            "#01000FYou came across\x01",
            "She is also aiming at her daughter\x01",
            "It did not appear.\x02\x03",
            "#01003FCertainly the trend of \"red constellation\"\x01",
            "It is worrisome, but just that\x01",
            "It can not be helped even if it is caught.\x02\x03",
            "#01000FWill continue to leave it to you.\x01",
            "Come and do what you can do without being impatient.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2254")

    label("loc_21B3")


    ChrTalk(
        0x8,
        (
            "#01003FCertainly the trend of \"red constellation\"\x01",
            "It is worrisome, but just that\x01",
            "It can not be helped even if it is caught.\x02\x03",
            "#01000FWill continue to leave it to you.\x01",
            "Come and do what you can do without being impatient.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2254")

    Jump("loc_253D")

    label("loc_2259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2383")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2321")

    ChrTalk(
        0x8,
        (
            "#01003FToday I am on standby.\x02\x03",
            "#01000FBeing in touch with department 1,\x01",
            "Toward the production of the commerce meeting tomorrow\x01",
            "We will prepare for the final preparation.\x02\x03",
            "I will contact you if there is something\x01",
            "Please do not hesitate to leave.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_237E")

    label("loc_2321")


    ChrTalk(
        0x8,
        (
            "#01003FToday I am on standby.\x02\x03",
            "#01000FI will contact you if there is something\x01",
            "Please do not hesitate to leave.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_237E")

    Jump("loc_253D")

    label("loc_2383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2391")
    Jump("loc_253D")

    label("loc_2391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2534")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B1")

    ChrTalk(
        0x8,
        (
            "#01002FThinking civic safety first,\x01",
            "Respond to various requests …\x01",
            "That is the Special Support Section.\x02\x03",
            "#01003FThey are Tsao and Lecter\x01",
            "I guess it will not be easy,\x01",
            "Leave it to the investigation department for the moment.\x02\x03",
            "#01000FYour original role\x01",
            "You will not lose sight of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, please leave it to me.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_252F")

    label("loc_24B1")


    ChrTalk(
        0x8,
        (
            "#01000FThinking civic safety first,\x01",
            "Respond to various requests …\x01",
            "That is the Special Support Section.\x02\x03",
            "Your original role\x01",
            "You will not lose sight of you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_252F")

    Jump("loc_253D")

    label("loc_2534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_253D")

    label("loc_253D")

    TalkEnd(0x8)
    Return()

    # Function_5_1397 end

    def Function_6_2541(): pass

    label("Function_6_2541")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2766")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_270E")

    ChrTalk(
        0x9,
        (
            "#01108FEveryone, that … … sorry.\x02\x03",
            "#01103FSuddenly doing such a thing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F気にするな、Keya。\x02\x03",
            "#00004FIn this situation,\x01",
            "It can not be helped variously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FTo take it is\x01",
            "We are the role of parents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIf something happen,\x01",
            "From now on without hesitation\x01",
            "Please come in and jump in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, if you rely on me\x01",
            "We are also happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01108FYes, thank you.\x02\x03",
            "#01100Fbe careful……\x01",
            "Keya、待ってるから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 6)
    Jump("loc_2761")

    label("loc_270E")


    ChrTalk(
        0x9,
        (
            "#01108FThanks guys.\x02\x03",
            "#01100Fbe careful……\x01",
            "Keya、待ってるから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2761")

    Jump("loc_3044")

    label("loc_2766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2774")
    Jump("loc_3044")

    label("loc_2774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_290E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28A7")

    ChrTalk(
        0x9,
        (
            "#01103FRandy …\x01",
            "I hope you find it in Budi.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSurely found.\x01",
            "Keyaは何も心配しなくていい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FRandy is also a sinner.\x01",
            "Keyaちゃんにこんなに\x01",
            "I do not care to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah, if I find it\x01",
            "You have to scold me down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01109FWell, that's right.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2909")

    label("loc_28A7")


    ChrTalk(
        0x9,
        (
            "#01109FWhen Randy comes back,\x01",
            "Keyaも叱るー！\x02\x03",
            "#01100FEveryone……\x01",
            "Please be careful!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2909")

    Jump("loc_3044")

    label("loc_290E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2AA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A40")

    ChrTalk(
        0x9,
        (
            "#01109FIn fact, yesterday\x01",
            "I was buying a lot of materials.\x02\x03",
            "It rained, but,\x01",
            "I do not want to go shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009Fはは、さすがKeyaだ。\x02\x03",
            "#00000FToday I will join the pot,\x01",
            "He is a nice girl who is staying at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01109FWell, be careful of Lloyd's!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2A9D")

    label("loc_2A40")


    ChrTalk(
        0x9,
        (
            "#01100FKeya、今日も\x01",
            "I'm preparing a pot and waiting.\x02\x03",
            "#01109FPlease be careful of Lloyd's!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A9D")

    Jump("loc_3044")

    label("loc_2AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2AB0")
    Jump("loc_3044")

    label("loc_2AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2ABE")
    Jump("loc_3044")

    label("loc_2ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2ACC")
    Jump("loc_3044")

    label("loc_2ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2ADA")
    Jump("loc_3044")

    label("loc_2ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2C97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C28")

    ChrTalk(
        0x9,
        (
            "#01100FEveryone, please tell me.\x02\x03",
            "#01109FWell, please be careful of Dudley too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00603FSo let's stop byhand … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01105FHmm?\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10A,
        (
            "#00606F…… Yeah, that's enough!\x01",
            "You guys are going quickly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Well, truly Dadley also\x01",
            "  Keyaには敵わないか。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2C92")

    label("loc_2C28")


    ChrTalk(
        0x9,
        (
            "#01109FEveryone, please tell me.\x02\x03",
            "Well, please be careful of Dudley too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00603F(Exactly … …)\x02",
    )

    CloseMessageWindow()

    label("loc_2C92")

    Jump("loc_3044")

    label("loc_2C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_END)), "loc_2DE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D7B")

    ChrTalk(
        0x9,
        (
            "#01105FThat Sieg's child,\x01",
            "It was really cool.\x02\x03",
            "#01109FBesides, my head is sooo great.\x01",
            "Keya、また会いたいかもー。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(It was pressed in a memo\x01",
            "Emblem of white falcon ……\x01",
            "Well, no way. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2DDC")

    label("loc_2D7B")


    ChrTalk(
        0x9,
        (
            "#01105FThat Sieg's child,\x01",
            "It was really cool.\x02\x03",
            "#01109FKeya、また会いたいかもー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DDC")

    Jump("loc_3044")

    label("loc_2DE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_2FF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F67")

    ChrTalk(
        0x9,
        (
            "#01102FMaple Muffin\x01",
            "I will be fine until tomorrow.\x02\x03",
            "#01109FWhen I am hungry at work\x01",
            "Let's make a boxed lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000Fああ、ありがとうKeya。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHehe, it was very delicious,\x01",
            "I am looking forward to it being hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01102Fえへへ、Keyaまた作るからー。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 1)), scpexpr(EXPR_END)), "loc_2F5F")

    ChrTalk(
        0x101,
        (
            "#00002F(Well, good … ….\x01",
            "Apparently it seems I got better. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F5F")

    SetScenarioFlags(0x0, 3)
    Jump("loc_2FF0")

    label("loc_2F67")


    ChrTalk(
        0x9,
        (
            "#01104FPerfume\x01",
            "Let's do the washing quickly.\x02\x03",
            "#01100FMaple Muffin\x01",
            "When I am hungry at work\x01",
            "Let's make a boxed lunch.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FF0")

    Jump("loc_3044")

    label("loc_2FF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3003")
    Jump("loc_3044")

    label("loc_3003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3011")
    Jump("loc_3044")

    label("loc_3011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_301F")
    Jump("loc_3044")

    label("loc_301F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_302D")
    Jump("loc_3044")

    label("loc_302D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_303B")
    Jump("loc_3044")

    label("loc_303B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3044")

    label("loc_3044")

    TalkEnd(0xFE)
    Return()

    # Function_6_2541 end

    def Function_7_3048(): pass

    label("Function_7_3048")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_315C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_313A")

    ChrTalk(
        0xA,
        "#01200FGururururururu ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FZeit……\x01",
            "It is somehow interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FLook at this situation\x01",
            "I guess warning is rising.\x02\x03",
            "#00001FZeit、Keyaたちのこと\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01200Fwon!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3157")

    label("loc_313A")


    ChrTalk(
        0xA,
        "#01200FGururururururu ……\x02",
    )

    CloseMessageWindow()

    label("loc_3157")

    Jump("loc_3BAB")

    label("loc_315C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_316A")
    Jump("loc_3BAB")

    label("loc_316A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_32AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3284")

    ChrTalk(
        0xA,
        "#01200FGurururu …… won.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F\"The soldiers are used to the field.\x01",
            "As I enter the other territory,\x01",
            "Be careful enough. \"\x02\x03",
            "It seems that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FありがとうZeit。\x01",
            "Advice will be painful.\x02\x03",
            "In front of a hunter from the front\x01",
            "I have to make sure not to.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_32A5")

    label("loc_3284")


    ChrTalk(
        0xA,
        "#01200FGurururu …… won.\x02",
    )

    CloseMessageWindow()

    label("loc_32A5")

    Jump("loc_3BAB")

    label("loc_32AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3383")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3365")

    ChrTalk(
        0xA,
        "#01200FGurururu …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F……I agree.\x01",
            "Randy is big fool.\x02\x03",
            "#00200FAt any cost\x01",
            "Let's take back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh … Of course!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_337E")

    label("loc_3365")


    ChrTalk(
        0xA,
        "#01200FGurururu …\x02",
    )

    CloseMessageWindow()

    label("loc_337E")

    Jump("loc_3BAB")

    label("loc_3383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_33BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_339E")
    Call(0, 8)
    Jump("loc_33B9")

    label("loc_339E")


    ChrTalk(
        0xA,
        "#01203FGururururu …\x02",
    )

    CloseMessageWindow()

    label("loc_33B9")

    Jump("loc_3BAB")

    label("loc_33BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_34A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3473")

    ChrTalk(
        0xA,
        "#01200FGurururu …… won, won.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FZeitも大事が起こったのを\x01",
            "It seems to be feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FOh … … Be careful and head for the scene.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_349C")

    label("loc_3473")


    ChrTalk(
        0xA,
        "#01200FGurururu …… won, won.\x02",
    )

    CloseMessageWindow()

    label("loc_349C")

    Jump("loc_3BAB")

    label("loc_34A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_34CC")

    ChrTalk(
        0xA,
        "#01203F… …. Gurururu ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BAB")

    label("loc_34CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_35DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35B9")

    ChrTalk(
        0xA,
        "#01200FGuru …… Won.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F\"You better go take care.\"\x01",
            "It seems that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWhen it comes to fighting the eidolon\x01",
            "It looks pretty dangerous ……\x02\x03",
            "#00000Fありがとう、Zeit。\x01",
            "When it comes to danger\x01",
            "Please lend me your power again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_35D8")

    label("loc_35B9")


    ChrTalk(
        0xA,
        "#01200FGuru …… Won.\x02",
    )

    CloseMessageWindow()

    label("loc_35D8")

    Jump("loc_3BAB")

    label("loc_35DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_35EB")
    Jump("loc_3BAB")

    label("loc_35EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3877")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3851")

    ChrTalk(
        0xA,
        "#01200FGururururu …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FHun, it is as great a wolf as ever.\x02\x03",
            "#00600FBut above being a police dog\x01",
            "You may borrow that power.\x01",
            "Prepare to be ready at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01200F……won.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36F2")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_36F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3726")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_3726")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_375A")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_375A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_378E")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_378E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37C2")
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_37C2")

    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00306F(Might be great,\x01",
            "You can not tell anyone else … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Hehe, Mr. Dudley's\x01",
            "I guess it is a way of encouragement. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3872")

    label("loc_3851")


    ChrTalk(
        0xA,
        "#01200FGurururu …… won.\x02",
    )

    CloseMessageWindow()

    label("loc_3872")

    Jump("loc_3BAB")

    label("loc_3877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_38A6")

    ChrTalk(
        0xA,
        "#01200FGurururu …… won.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BAB")

    label("loc_38A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_39CD")

    ChrTalk(
        0xA,
        "#01200FGurururu …\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39C8")

    ChrTalk(
        0x101,
        (
            "#00005Fそうだ、Zeit……\x01",
            "The Orchest Tower's announcement\x01",
            "Keyaと一緒に見たんだよな。\x02\x03",
            "なんだかKeyaが元気ないけど\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01200FGurururu …… won.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FWell, if you do not have Tio\x01",
            "You do not know exactly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_39C8")

    Jump("loc_3BAB")

    label("loc_39CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3AD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AAE")

    ChrTalk(
        0xA,
        "#01200FGurururu …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FようZeit。\x02\x03",
            "#00309FHa ha, in the case of the old mine last time\x01",
            "Thank you for giving me directions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FI am counting on you from now on.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01200FGuru …… Won.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3ACD")

    label("loc_3AAE")


    ChrTalk(
        0xA,
        "#01200FGuru …… Won.\x02",
    )

    CloseMessageWindow()

    label("loc_3ACD")

    Jump("loc_3BAB")

    label("loc_3AD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3BA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B84")

    ChrTalk(
        0xA,
        "#01203FGurururu …… won.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F雨の日はZeitも\x01",
            "It looks boring.\x02\x03",
            "Well, today is also quiet\x01",
            "Please keep an answering machine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01200F……won.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3B9D")

    label("loc_3B84")


    ChrTalk(
        0xA,
        "#01200F……won.\x02",
    )

    CloseMessageWindow()

    label("loc_3B9D")

    Jump("loc_3BAB")

    label("loc_3BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3BAB")

    label("loc_3BAB")

    TalkEnd(0xFE)
    Return()

    # Function_7_3048 end

    def Function_8_3BAF(): pass

    label("Function_8_3BAF")

    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xA,
        "#01200FGururururu …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Anyway ~ ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FZeitとCoppeも\x01",
            "I am looking forward to the pot of dinner\x01",
            "Looks like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FWell, but cats\x01",
            "As its name suggests, it is a cat tongue …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FDog family animals too\x01",
            "Was not she a cat tongue?\x01",
            "Huff, it's a strange expression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F…… I will cool down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01200Fwon.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 4)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_8_3BAF end

    def Function_9_3CF4(): pass

    label("Function_9_3CF4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3D05")
    Jump("loc_3F1A")

    label("loc_3D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3E5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E42")

    ChrTalk(
        0xFE,
        "Nyanaya ~ spray\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHe seems to eat well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FCat foodの味が\x01",
            "It seems to be nostalgic.\x02\x03",
            "While we are away,\x01",
            "Take a food outside for yourself\x01",
            "It seems like I went out … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FWell, was that so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fはは、Coppeって意外と\x01",
            "There are lively places.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3E5A")

    label("loc_3E42")


    ChrTalk(
        0xFE,
        "Nyanaya ~ spray\x02",
    )

    CloseMessageWindow()

    label("loc_3E5A")

    Jump("loc_3F1A")

    label("loc_3E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3E6D")
    Jump("loc_3F1A")

    label("loc_3E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3EF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E88")
    Call(0, 8)
    Jump("loc_3EEC")

    label("loc_3E88")


    ChrTalk(
        0xFE,
        "Anyway ~ ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F（Keyaもいるし、今日は俺たちから\x01",
            "There is no need to feed me. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EEC")

    Jump("loc_3F1A")

    label("loc_3EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3EFF")
    Jump("loc_3F1A")

    label("loc_3EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3F1A")

    ChrTalk(
        0xFE,
        "Wow ~ ~.\x02",
    )

    CloseMessageWindow()

    label("loc_3F1A")

    TalkEnd(0xFE)
    Return()

    # Function_9_3CF4 end

    def Function_10_3F1E(): pass

    label("Function_10_3F1E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41FE")

    ChrTalk(
        0xB,
        (
            "#05928FArios gives Shizuku-chan\x01",
            "Reason why I forced my husband to discharge … …\x01",
            "It is connected to such importance.\x02\x03",
            "#05923FIf you think about the safety of Shizuoka\x01",
            "It may be useless … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh, I see. …\x02\x03",
            "#00005F……そういえばCecil姉。\x01",
            "What is the state of Ursula Hospital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWell, police officials who were hospitalized\x01",
            "I also care about Iria's condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05920FEven at the hospital there is confusion,\x01",
            "Response to patients\x01",
            "I'm going as usual.\x02\x03",
            "#05924FFran was recovering smoothly\x01",
            "I was transferred to the general ward … …\x02\x03",
            "#05920FDonovan also, during this time\x01",
            "I finally got consciousness back.\x02\x03",
            "#05928F…… As usual, Ilya\x01",
            "I will not wake up … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FAs soon as you get well\x01",
            "That's a good idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#05924FYes … really.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 1)
    Jump("loc_435F")

    label("loc_41FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42EA")

    ChrTalk(
        0xB,
        (
            "#05920FEven at the hospital there was confusion,\x01",
            "Response to patients\x01",
            "I'm going as usual.\x02\x03",
            "#05923Fanyway……\x01",
            "私はここでKeyaちゃんと\x01",
            "Because I am keeping an answering machine together.\x02\x03",
            "#05920FIt looks like a difficult situation ….\x01",
            "Be careful again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_435F")

    label("loc_42EA")


    ChrTalk(
        0xB,
        (
            "#05920F私はここでKeyaちゃんと\x01",
            "Because I am keeping an answering machine together.\x02\x03",
            "It looks like a difficult situation ….\x01",
            "Be careful again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_435F")

    TalkEnd(0xFE)
    Return()

    # Function_10_3F1E end

    def Function_11_4363(): pass

    label("Function_11_4363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4375")
    Call(0, 16)
    Jump("loc_43B5")

    label("loc_4375")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThis is the room of Tio.\x01",
            "Let's stop entering.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_43B5")

    Return()

    # Function_11_4363 end

    def Function_12_43B6(): pass

    label("Function_12_43B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43C8")
    Call(0, 17)
    Jump("loc_440A")

    label("loc_43C8")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThis is the room of Randy.\x01",
            "Let's stop entering.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_440A")

    Return()

    # Function_12_43B6 end

    def Function_13_440B(): pass

    label("Function_13_440B")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F……そういえば、Keyaが\x01",
            "I told you to go to Sunday school.\x02\x03",
            "The manager also went out,\x01",
            "You may as well go out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FWell, let's call out.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 800, 0, 1890, 0)
    EventEnd(0x4)
    Return()

    # Function_13_440B end

    def Function_14_44C8(): pass

    label("Function_14_44C8")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F……そういえば、Keyaが\x01",
            "I told you to go to Sunday school.\x02\x03",
            "The manager also went out,\x01",
            "You may as well go out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FWell, let's call out.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_14_44C8 end

    def Function_15_4585(): pass

    label("Function_15_4585")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FKeyaはこれから日曜学校だ。\x01",
            "The back door is a shortcut.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -1330, 0, 71380, 268)
    EventEnd(0x4)
    Return()

    # Function_15_4585 end

    def Function_16_45DC(): pass

    label("Function_16_45DC")

    EventBegin(0x0)
    Fade(500)
    OP_68(169990, 1000, 63110, 0)
    MoveCamera(43, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23860, 0)
    SetChrPos(0x101, 170800, 0, 62310, 315)
    SetChrPos(0x102, 168790, 0, 62190, 45)
    SetChrPos(0x109, 171240, 0, 63400, 270)
    SetChrPos(0x105, 168190, 0, 63200, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4676")
    SetChrPos(0x1A5, 169520, 0, 61730, 0)

    label("loc_4676")

    OP_0D()

    ChrTalk(
        0x102,
        "#6P#00100FThis is Tio's room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FSurely now, in Les Autonomous states\x01",
            "Are you on a business trip?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, with Jonah\x01",
            "Epstein Foundation's\x01",
            "I am going to the laboratory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWith the amendment of the Autonomous State Law, the power net also\x01",
            "Diffusion is proceeding,\x01",
            "I guess that helped the relationship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10103FI do not know the difficult thing ….\x01",
            "It seems quite tough.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_484A")

    ChrTalk(
        0x1A5,
        "#12P#01100FTio, I hope to get back soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4880")

    label("loc_484A")


    ChrTalk(
        0x101,
        (
            "#00000FOh, as soon as I return\x01",
            "I do not mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4880")

    OP_5A()
    SetChrPos(0x0, 169990, 0, 63110, 180)
    SetScenarioFlags(0x13B, 3)
    EventEnd(0x5)
    Return()

    # Function_16_45DC end

    def Function_17_4898(): pass

    label("Function_17_4898")

    EventBegin(0x0)
    Fade(500)
    OP_68(14040, 800, 63300, 0)
    MoveCamera(41, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23800, 0)
    SetChrPos(0x101, 12730, 0, 61720, 45)
    SetChrPos(0x102, 14330, 0, 61720, 315)
    SetChrPos(0x109, 11530, 0, 62750, 90)
    SetChrPos(0x105, 15130, 0, 62750, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4932")
    SetChrPos(0x1A5, 13500, 0, 61420, 0)

    label("loc_4932")

    OP_0D()

    ChrTalk(
        0x101,
        "#12P#00000FThis is Randy 's room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FRandy is now,\x01",
            "With the troops of the Belgard gate\x01",
            "It is in the midst of rehabilitation training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FOh, surely in a cult incident\x01",
            "Did you have the case of the example?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103FYup……\x01",
            "Something terrible as sequelae\x01",
            "I do not remember.\x02\x03",
            "#10108FTo regain physical strength and can\x01",
            "It looks like it will take some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FReally……\x01",
            "I want the guard to recover quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B1E")

    ChrTalk(
        0x1A5,
        "#12P#01100FI wonder if Randy will come back soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHehe, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B5C")

    label("loc_4B1E")


    ChrTalk(
        0x102,
        (
            "#00100FWell, Randy also\x01",
            "I want to get back soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B5C")

    OP_5A()
    SetChrPos(0x0, 14040, 0, 63300, 180)
    SetScenarioFlags(0x13B, 4)
    EventEnd(0x5)
    Return()

    # Function_17_4898 end

    def Function_18_4B74(): pass

    label("Function_18_4B74")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B9B")
    Call(0, 21)
    Return()

    label("loc_4B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4BE0")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The power of the terminal is declining.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    label("loc_4BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4D14")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The power of the terminal is declining.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D10")

    ChrTalk(
        0x101,
        (
            "#00003F… … apparently the power itself\x01",
            "It does not seem to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FTentatively,\x01",
            "There is nothing to be broken\x01",
            "I'm glad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, I gotta use the terminal\x01",
            "That's Merkaba.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI see.\x01",
            "Let's leave it here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CC, 5)

    label("loc_4D10")

    TalkEnd(0xFF)
    Return()

    label("loc_4D14")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4D2E")
    OP_C9(0x0, 0x4)
    OP_C9(0x0, 0x100)

    label("loc_4D2E")

    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53EF")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4D80"),
        (1, "loc_4F32"),
        (2, "loc_53DA"),
        (3, "loc_53E2"),
        (SWITCH_DEFAULT, "loc_53EA"),
    )


    label("loc_4D80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4D93")
    OP_2B(0x94, 0xFFFF)
    Jump("loc_4F2D")

    label("loc_4D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4DAE")
    OP_2B(0x8E, 0x8F, 0x90, 0x91, 0x92, 0xFFFF)
    Jump("loc_4F2D")

    label("loc_4DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4E07")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Automatic announcement")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Currently, there is no support request.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_4F2D")

    label("loc_4E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4E22")
    OP_2B(0x8B, 0x8C, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_4F2D")

    label("loc_4E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4E5D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4E4B")
    OP_2B(0x85, 0x86, 0x87, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_4E58")

    label("loc_4E4B")

    OP_2B(0x85, 0x86, 0x88, 0x80, 0x83, 0xFFFF)

    label("loc_4E58")

    Jump("loc_4F2D")

    label("loc_4E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4E76")
    OP_2B(0x80, 0x81, 0x82, 0x83, 0xFFFF)
    Jump("loc_4F2D")

    label("loc_4E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_4E84")
    Jump("loc_4F2D")

    label("loc_4E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4EA1")
    OP_2B(0x79, 0x7A, 0x7B, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_4F2D")

    label("loc_4EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_END)), "loc_4EBE")
    OP_2B(0x74, 0x75, 0x76, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_4F2D")

    label("loc_4EBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4ED7")
    OP_2B(0x6F, 0x70, 0x71, 0x72, 0xFFFF)
    Jump("loc_4F2D")

    label("loc_4ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4F0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_4EFB")
    OP_2B(0x6A, 0x6B, 0x6C, 0x6D, 0x67, 0xFFFF)
    Jump("loc_4F06")

    label("loc_4EFB")

    OP_2B(0x6A, 0x6B, 0x6C, 0x67, 0xFFFF)

    label("loc_4F06")

    Jump("loc_4F2D")

    label("loc_4F0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 7)), scpexpr(EXPR_END)), "loc_4F22")
    OP_2B(0x65, 0x66, 0x67, 0xFFFF)
    Jump("loc_4F2D")

    label("loc_4F22")

    OP_2B(0x65, 0x66, 0x67, 0x68, 0xFFFF)

    label("loc_4F2D")

    Jump("loc_53EA")

    label("loc_4F32")

    SetMapFlags(0x40000000)
    OP_E5(0x7)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_500F")
    SetChrName("Automatic announcement")

    AnonymousTalk(
        0xFF,
        "This is Crosbell Police.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_4FE8")

    AnonymousTalk(
        0xFF,
        "We will receive reports.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("Automatic announcement")

    AnonymousTalk(
        0xFF,
        (
            "Finish report processing.\x01",
            "Thank you for your hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_500A")

    label("loc_4FE8")


    AnonymousTalk(
        0xFF,
        "There are no reportable requests.\x02",
    )

    CloseMessageWindow()

    label("loc_500A")

    Jump("loc_53CC")

    label("loc_500F")

    SetChrName("Receptionist franc")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5063")
    Sound(3062, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Yes, here is the crossbell police ~!\x02",
    )

    CloseMessageWindow()
    Jump("loc_508F")

    label("loc_5063")

    Sound(3061, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Everyone, thank you very much.\x02",
    )

    CloseMessageWindow()

    label("loc_508F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_52D8")
    Sound(3067, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        "Well then we will receive a report ~.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5263")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_5100"),
        (13, "loc_514A"),
        (12, "loc_5192"),
        (SWITCH_DEFAULT, "loc_51DC"),
    )


    label("loc_5100")

    Sound(3075, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        (
            "Class 1st--\x01",
            "Mr. Lloyd is too amazing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51DC")

    label("loc_514A")

    Sound(3074, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        (
            "Class 2nd -\x01",
            "Mr. Lloyd is amazing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51DC")

    label("loc_5192")

    Sound(3073, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        (
            "Class 3rd\x01",
            "Mr. Lloyd, you did it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51DC")

    label("loc_51DC")

    Sound(3076, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        (
            "Items of award also soon\x01",
            "I will deliver to you ~!\x02",
        )
    )

    CloseMessageWindow()
    Sound(3077, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Congratulations ~!\x01",
            "Thank you again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52D0")

    label("loc_5263")

    Sound(3078, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        "The report is over.\x02",
    )

    CloseMessageWindow()
    Sound(3079, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Then, once you have reached the request\x01",
            "nice to meet you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52D0")

    SetScenarioFlags(0x0, 1)
    Jump("loc_53CC")

    label("loc_52D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_535D")
    Sound(3063, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        (
            "There …\x01",
            "It was just reported earlier?\x02",
        )
    )

    CloseMessageWindow()
    Sound(3064, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Also, I hope you will be able to fulfill your request.\x02",
    )

    CloseMessageWindow()
    Jump("loc_53CC")

    label("loc_535D")

    Sound(3065, 255, 100, 0)
    SetChrName("Receptionist franc")

    AnonymousTalk(
        0xFF,
        (
            "There, reportable\x01",
            "It seems there is no request for it ~.\x02",
        )
    )

    CloseMessageWindow()
    Sound(3066, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Thank you again.\x02",
    )

    CloseMessageWindow()

    label("loc_53CC")

    OP_57(0x0)
    OP_E5(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_53EA")

    label("loc_53DA")

    Call(0, 20)
    Jump("loc_53EA")

    label("loc_53E2")

    Call(0, 19)
    Jump("loc_53EA")

    label("loc_53EA")

    Jump("loc_4D47")

    label("loc_53EF")

    OP_E5(0x6)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x68, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5435")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 24)
    Return()

    label("loc_5435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_546D")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 27)
    Return()

    label("loc_546D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54AC")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 32)
    Return()

    label("loc_54AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54E4")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 39)
    Return()

    label("loc_54E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5571")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_553B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5536")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 41)
    Return()

    label("loc_5536")

    Jump("loc_556C")

    label("loc_553B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_556C")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 41)
    Return()

    label("loc_556C")

    Jump("loc_55F2")

    label("loc_5571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_558A")
    SetScenarioFlags(0x168, 2)
    Call(0, 67)
    Jump("loc_55F2")

    label("loc_558A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x92, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55C9")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 44)
    Return()

    label("loc_55C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_55E0")
    ClearScenarioFlags(0x22, 3)
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    label("loc_55E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_55F2")
    ClearScenarioFlags(0x22, 6)
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    label("loc_55F2")

    FadeToBright(300, 0)
    OP_0D()
    OP_E5(0xB)
    Call(0, 67)
    TalkEnd(0xFF)
    Return()

    # Function_18_4B74 end

    def Function_19_5605(): pass

    label("Function_19_5605")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5633")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x94, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_562E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_562E")

    Jump("loc_5943")

    label("loc_5633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5673")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x92, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_566E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_566E")

    Jump("loc_5943")

    label("loc_5673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_568B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5943")

    label("loc_568B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_56CB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56C6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_56C6")

    Jump("loc_5943")

    label("loc_56CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5755")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_571E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5719")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5719")

    Jump("loc_5750")

    label("loc_571E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5750")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5750")

    Jump("loc_5943")

    label("loc_5755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_578E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5789")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5789")

    Jump("loc_5943")

    label("loc_578E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_57A6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5943")

    label("loc_57A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_57ED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57E8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_57E8")

    Jump("loc_5943")

    label("loc_57ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_END)), "loc_5834")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_582F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_582F")

    Jump("loc_5943")

    label("loc_5834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_586D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5868")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5868")

    Jump("loc_5943")

    label("loc_586D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_58E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_58B6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6D, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58B1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_58B1")

    Jump("loc_58E1")

    label("loc_58B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58E1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_58E1")

    Jump("loc_5943")

    label("loc_58E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 7)), scpexpr(EXPR_END)), "loc_5918")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5913")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5913")

    Jump("loc_5943")

    label("loc_5918")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x68, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5943")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5943")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5995")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please check all support requests.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_5995")

    Return()

    # Function_19_5605 end

    def Function_20_5996(): pass

    label("Function_20_5996")

    OP_E5(0x6)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 3)), scpexpr(EXPR_END)), "loc_59B8")
    SetScenarioFlags(0x2A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59B8")
    ClearScenarioFlags(0x2A, 0)

    label("loc_59B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_END)), "loc_59D5")
    SetScenarioFlags(0x2A, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59D5")
    ClearScenarioFlags(0x2A, 1)

    label("loc_59D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_END)), "loc_59F2")
    SetScenarioFlags(0x2A, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59F2")
    ClearScenarioFlags(0x2A, 2)

    label("loc_59F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 6)), scpexpr(EXPR_END)), "loc_5A0F")
    SetScenarioFlags(0x2A, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A0F")
    ClearScenarioFlags(0x2A, 3)

    label("loc_5A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_END)), "loc_5A2C")
    SetScenarioFlags(0x2A, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A2C")
    ClearScenarioFlags(0x2A, 4)

    label("loc_5A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_END)), "loc_5A49")
    SetScenarioFlags(0x2A, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A49")
    ClearScenarioFlags(0x2A, 5)

    label("loc_5A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_END)), "loc_5A55")
    SetScenarioFlags(0x2A, 6)

    label("loc_5A55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AA7")
    RunExpression(0x6, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopBGM(0x0)
    Jump("loc_5B22")

    label("loc_5AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5AF9")
    OP_24(0x80)
    RunExpression(0x6, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()
    Sound(128, 1, 50, 0)
    Jump("loc_5B22")

    label("loc_5AF9")

    RunExpression(0x6, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()

    label("loc_5B22")

    Return()

    # Function_20_5996 end

    def Function_21_5B23(): pass

    label("Function_21_5B23")

    EventBegin(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    SoundLoad(939)
    OP_68(16740, 1750, 10380, 0)
    MoveCamera(44, 21, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(24570, 0)
    SetChrPos(0x101, 15000, 850, 10900, 90)
    SetChrPos(0x102, 15970, 850, 9800, 45)
    SetChrPos(0x109, 14390, 850, 9310, 90)
    SetChrPos(0x105, 16500, 850, 8270, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#00004FAccording to Roberts,\x01",
            "This memory crystal is placed in the terminal\x01",
            "I was going to install it.\x02\x03",
            "#00000FWell then……\x01",
            "I'm begging you, Eli.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FYeah, I'll try.\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Erie is a powerful terminal\x01",
            "\"Pomutto! I installed the beta version.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    Sound(836, 0, 100, 0)
    Sleep(1000)
    Sound(939, 2, 100, 0)
    Sleep(1000)
    OP_24(0x3AB)
    Sound(839, 0, 100, 0)
    Sleep(500)
    Sound(839, 0, 100, 0)

    ChrTalk(
        0x102,
        (
            "#12P#00104FWith this, okay ….\x02\x03",
            "#00100FRoberts' director who got it\x01",
            "I also entered an account.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FWell, it's quite handy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FHey, really,\x01",
            "It is familiar to many things.\x02\x03",
            "#10100FPolitics and laws as well\x01",
            "I also like to have plenty of knowledge.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#11P#00102FHuhu, regarding this\x01",
            "Tio's doing it\x01",
            "Because I was only watching.\x02\x03",
            "#00104FThere were also instructions,\x01",
            "Well if you read well\x01",
            "It was not difficult either.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00002FNo, but I will be saved honestly.\x02\x03",
            "#00006FI'm finally the terminal\x01",
            "I'm used to the keyboard.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#00109FHehe, you are welcome.\x02\x03",
            "#00100FSo … to Roberts\x01",
            "I wonder if I should contact you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00000FOh, I will try it at once.\x02",
    )

    CloseMessageWindow()

    def lambda_5FFB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5FFB)
    Sleep(50)

    def lambda_600B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_600B)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sound(823, 0, 100, 0)
    Sleep(2800)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "── Hey, Lloyd.\x01",
            "Have you successfully installed it?\x07\x00\x02",
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
            "#00000FYes, it's okay.\x01",
            "What next?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well then, one\x01",
            "Shall I play against me?\x02\x03",
            "From the terminal \"Pomto! \"\x01",
            "Start it up.\x02\x03",
            "There my account\x01",
            "Since it should be displayed,\x01",
            "You can play against it if you choose it.\x02\x03",
            "… … That's right, because it's a point\x01",
            "You are the leader of the support department\x01",
            "Will you play as a representative?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FIs it? Is it? Is it?\x01",
            "Yes, I understood.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)

    ChrTalk(
        0x102,
        "#12P#00100FWell then I will change my seat.\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x14, 0x1F4)

    def lambda_62D4():
        OP_9B(0x1, 0xFE, 0xB4, 0x5DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_62D4)
    Sleep(200)

    def lambda_62EC():
        OP_95(0xFE, 15970, 850, 9800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62EC)

    def lambda_6306():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6306)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x5)
    Sleep(500)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hehe, who is a developer\x01",
            "I wonder if I can win this … ….?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Roberts' voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4SA man who can trust Tio … …\x01",
            "I will let you make it over again!#3S\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#6P#10112F…… Honestly\x01",
            "It sounds like you heard … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10309FAhaha,\x01",
            "It sounds like a pretty parents stupid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FWell, to go to the support section\x01",
            "You asked me …?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Haha, no no …\x01",
            "It's a great game,\x01",
            "I just put a spirit into it.\x02\x03",
            "Well then, immediately\x01",
            "Let's start the game!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x27, 2)
    OP_29(0x6C, 0x1, 0x1)
    StopSound(128, 500, 40)
    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_49()

    label("loc_65C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6654")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65FD")
    Call(0, 20)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_664F")

    label("loc_65FD")


    AnonymousTalk(
        0x101,
        (
            "#0000FRoberts is waiting for you,\x01",
            "Right away \"Pomutto! Let's start it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_664F")

    Jump("loc_65C5")

    label("loc_6654")

    OP_E5(0x6)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    FadeToBright(300, 0)
    OP_0D()
    OP_E5(0xB)
    Call(0, 22)
    Return()

    # Function_21_5B23 end

    def Function_22_6678(): pass

    label("Function_22_6678")

    EventBegin(0x0)
    SoundLoad(803)
    SoundLoad(128)
    Sound(128, 2, 50, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_670B")
    OP_2C(0x6C, 0x1)

    ChrTalk(
        0x101,
        (
            "#6P#00009FOK, I managed to win …!\x02\x03",
            "#00004F(Well, fine.\x01",
            "It might be fun … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6C, 0x1, 0x2)
    Jump("loc_6769")

    label("loc_670B")


    ChrTalk(
        0x101,
        (
            "#6P#00006F… … Have you lost?\x02\x03",
            "#00001F(Hmm, what is it?\x01",
            "It is frustrating as it is … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6C, 0x1, 0x3)

    label("loc_6769")


    ChrTalk(
        0x102,
        (
            "#12P#00109FHuhu, quite enough\x01",
            "You seem to have gotten hooked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105F… …. Well, I was watching by the side\x01",
            "It's an impression ….\x02\x03",
            "#10106FRoberts chief,\x01",
            "Perhaps it is not strong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FThat's right, even a developer\x01",
            "Beginner with you in strength\x01",
            "Does not it change much?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00012FNo……\x01",
            "As expected\x01",
            "Did not you do it?\x02\x03",
            "#00003FIf you have to adjust the level to some extent\x01",
            "I heard that it will be a test … …\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(100)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#00000FYes, this special support ─ ─\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "── Gee,\x01",
            "It was a good game now!\x02\x03",
            "It is a big game that remains in history!\x01",
            "I am excited! It is!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FApparently I'm gonna be a serious game\x01",
            "It looks like it was … …)\x02\x03",
            "#00012FWell then … …\x01",
            "How was the result of the test?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, it's pat!\x02\x03",
            "For the city to do\x01",
            "There is no noticeable rug,\x01",
            "The communication state is also good.\x02\x03",
            "It can be said that it was a great success.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#6P#00000FIs that so……\x01",
            "それはI'm glad.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Installed beta version,\x01",
            "In the near future release version\x01",
            "I will update it.\x02\x03",
            "When the distribution of the program is started,\x01",
            "The number of people who can fight will also increase.\x02\x03",
            "Exchange various accounts with various people,\x01",
            "I am glad if you enjoy yourself.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D5C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D01")
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Of course, this servant also\x01",
            "I will revenge someday!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6D5C")

    label("loc_6D01")

    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Of course, today's revenge is also\x01",
            "I'll always accept it!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6D5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DCB")
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Of course, this servant also\x01",
            "I will revenge someday!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6E26")

    label("loc_6DCB")

    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Of course, today's revenge is also\x01",
            "I'll always accept it!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6E26")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00012FHahaha ……\x01",
            "Hand softly.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No, thank you for your cooperation\x01",
            "Thank you very much.\x02\x03",
            "Because I have another job\x01",
            "This will be rude.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYou are welcome.\x01",
            "If there is something again\x01",
            "Please contact me anytime.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, I will.\x01",
            "── That's it!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(150)
    TurnDirection(0x101, 0x102, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00004FFuu … somehow\x01",
            "It seems that it went well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FHehe, cheers for good work.\x02\x03",
            "#00104FI mean,\x01",
            "It was a request like a chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FHaha, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FAnyway, from now on\x01",
            "I think I can enjoy this game.\x02\x03",
            "#10309FAs this is the case,\x01",
            "Pomutto! Master\x01",
            "What do you aim for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FNo, as expected to Tio\x01",
            "It will not be an enemy absolutely ….\x02\x03",
            "#00000FBut, between work\x01",
            "About relaxation exercise\x01",
            "It might be okay to keep it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FHuh, you are right.\x02",
    )

    CloseMessageWindow()
    StopSound(128, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Request for participation in β test】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    OP_29(0x6C, 0x1, 0x4)
    OP_29(0x6C, 0x4, 0x10)
    OP_29(0xA1, 0x1, 0x11)
    SetChrPos(0x0, 14970, 850, 8800, 225)
    OP_24(0x323)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7562", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x232), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(128, 2, 50, 0)
    EventEnd(0x5)
    Return()

    # Function_22_6678 end

    def Function_23_724F(): pass

    label("Function_23_724F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis011.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis347.itp")
    OP_68(17000, 1650, 10500, 0)
    MoveCamera(19, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 15200, 850, 10900, 90)
    SetChrPos(0x102, 16300, 850, 10200, 45)
    SetChrPos(0x109, 17200, 850, 8000, 315)
    SetChrPos(0x105, 16200, 850, 7700, 0)
    SetCameraDistance(23500, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    Sound(836, 0, 100, 0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(72, 0, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    AnonymousTalk(
        0x102,
        (
            "#00104F─ ─ Yeah.\x01",
            "You are coming properly.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        "#10100FThis is……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10302FThe Special Affairs Support Division handles\x01",
            "That's why \"request for support\".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x101, 0x109, 0)
    Sleep(300)

    AnonymousTalk(
        0x101,
        (
            "#00004FOh, the basic is once a day,\x01",
            "It is a rule that will be sent together.\x02\x03",
            "#00000FWhere to go is\x01",
            "I am left to the discretion here ….\x02\x03",
            "What is written as \"emergency\"\x01",
            "You'd better do it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10304FIndeed, it is reasonable.\x02\x03",
            "#10300FThose whose period has been taken longer\x01",
            "Is it alright to go to the next day?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00000FOh, I wonder if that will happen.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00104FOnce, once you check it every day\x01",
            "Because the period presented will also change.\x02\x03",
            "#00100FAnd if you check \"Investigation notebook\"\x01",
            "You can check the situation around that.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        "#10105FWhen I say an investigation notebook … …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(24000, 0)
    FadeToBright(0, 0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)

    ChrTalk(
        0x109,
        (
            "#12P#10100FEllie sometimes wrote it\x01",
            "Is it a black notebook?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        "#5P#00100FYes, this is it.\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    AnonymousTalk(
        0x101,
        (
            "#00003FBasically, on investigation and support request\x01",
            "Write something if there is any progress.\x02\x03",
            "By doing so, you can\x01",
            "It will be possible to manage.\x02\x03",
            "#00000FAlso, tactical ornament -\x01",
            "Also describing \"Enigma\"\x01",
            "I follow you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10305FWell, it is rather convenient, is not it?\x02\x03",
            "#10304FWell, either one such a notebook\x01",
            "I feel like it will be more powerful.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00102FI see …\x01",
            "Such research from Tio also\x01",
            "I have heard that it is being done.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10112FWell, that's why it will be\x01",
            "It is somewhat resistant ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00002FCertainly, paper and pen are\x01",
            "I agree that you are comfortable.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        (
            "#00004F#5P─ ─ Well, if you explain roughly\x01",
            "This is the basic style of the support department.\x02\x03",
            "#00000FFirst of all, we request support request from the terminal\x01",
            "Let's check it all out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10102FOK!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10309FHuh, I'm looking forward to opening it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "* Check the terminal placed in the support section with ○ button\x01",
            "If you select [Confirm Assistance Request] from the item,\x01",
            "Requests for work to Lloyd's (quest) are listed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ There are high urgency in support request,\x01",
            "There are things that you must do.\x01",
            "These things are marked \"urgent\"\x01",
            "The main story progresses when you achieve it.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ Other support requests,\x01",
            "We do not necessarily need to achieve it\x01",
            "If you clear it you can earn DP and Mira.\x01",
            "Also, please be aware that it will disappear after the deadline.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 15000, 850, 8900, 45)
    SetScenarioFlags(0x126, 0)
    OP_29(0xA1, 0x4, 0x2)
    OP_29(0xA1, 0x1, 0x0)
    Call(0, 67)
    AddItemNumber('自治州地图', 1)
    AddItemNumber('克洛斯贝尔市的地图', 1)
    OP_C9(0x0, 0x1000)
    OP_C9(0x0, 0x200000)
    EventEnd(0x5)
    Return()

    # Function_23_724F end

    def Function_24_7C66(): pass

    label("Function_24_7C66")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis231.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis235.itp")
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch02902.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    OP_68(12600, 2350, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x2)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x109, 11300, 900, 6650, 90)
    SetChrPos(0x105, 11300, 900, 4600, 90)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 19000, 850, 4000, 270)
    OP_4B(0x8, 0xFF)
    OP_68(12600, 1850, 5600, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x109,
        (
            "#6P#10103FUrgent 2 cases,\x01",
            "Are there two cases of devil demons … ….\x02\x03",
            "#10101FRegardless of the matter of Enigma\x01",
            "The other one is pretty special.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PYeah, that Rector is a person\x01",
            "I also came to crossbell … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303F\"Black auctioneer#10RSchwarz Auction#\"It was at the time of\x01",
            "That brother you've run down with.\x02\x03",
            "#10300FWhatever you think is not a taddy\x01",
            "I thought.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)

    AnonymousTalk(
        0x101,
        (
            "#00003F…… When I trained at the investigation department\x01",
            "I browsed the file about him.\x02\x03",
            "#00001FImperial Army Information Department Affiliation,\x01",
            "Captain Rector Alain Dole.\x02\x03",
            "As a secretary of the Imperial Government\x01",
            "She seems to have a title too.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        "#10108FIs it a human in an intelligence field …?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00103F#11PIt is possible to do political work as well\x01",
            "It looks like an information officer.\x02\x03",
            "#00101FThere is no way to capture it\x01",
            "Advanced Levels#4RTokyo#Is it the technology?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FI feel more than half though.\x02\x03",
            "#10302FBut the Imperial Government clerk\x01",
            "What is the affiliation of the military intelligence office … …\x02\x03",
            "That famous \"Iron Blood Championship\"\x01",
            "Is it confusing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006F(Why until such a background\x01",
            "Do you understand well? …)\x02\x03",
            "#00001F── Oh, according to the information in section 1\x01",
            "It seems to be one of the chiefs of Prime Minister Osborne.\x02\x03",
            "Last year, visiting the crossbell with the Prime Minister\x01",
            "Informally with Chairman Hartmann\x01",
            "It has been confirmed that the meeting was held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PThat person himself said that.\x02\x03",
            "#00106FIt was a kid talking like a joke\x01",
            "No way it was true … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FEven though I think about it\x01",
            "It is a person who does not seem to go …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FHuh, it sounds interesting, is not it?\x02\x03",
            "#10300FIt will be the first time in the city\x01",
            "Is the support activity a priority?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00000FOh, one arrangement devil is arranged,\x01",
            "Although it is arranged in the highway\x01",
            "Let's keep it there.\x02\x03",
            "#00003F… … A few months after the annihilation of Rubathe.\x02\x03",
            "#00001FSoon there will be new moves in the back society\x01",
            "It seems certain that it is happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11P\"Black moon#4RHayuue#\"Movement ……\x01",
            "Then the movement of the Imperial government.\x02\x03",
            "#00101F\"Trade meeting\" held at the end of the month is also\x01",
            "It seems that it has considerable influence.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)
    SetChrSubChip(0x105, 0x0)
    Sleep(300)

    ChrTalk(
        0x109,
        "#6P#10105F\"Trade meeting\" is … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FThe new Mayor called for it\x01",
            "It is an international conference where summit classes gather.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00102F#11PYeah\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)

    AnonymousTalk(
        0x102,
        (
            "#00104FDieter · Crois New Mayor.\x02\x03",
            "He sponsors the Empire, the Republic,\x01",
            "Leber, the head of Remifferia\x01",
            "Economic related international conference to be united.\x02\x03",
            "#00100F\"Western Zemria Trade Council\"\x01",
            "It is the official name.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00004FImmediately after inauguration\x01",
            "Such a large international conference\x01",
            "I do not want to call for holding ……\x02\x03",
            "#00000FAs expected, IBC president\x01",
            "Is there anything that is only doubling?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10109FI have never met you directly.\x01",
            "It's a terrible guy.\x02\x03",
            "#10102FBy the way, Mr. Waji is a new mayor\x01",
            "Have you ever met one?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#6P#10304FOh, when I got a letter of recommendation.\x02\x03",
            "#10302FNo matter how much independent gig they are\x01",
            "A letter of recommendation to the police department\x01",
            "I never give a bad boy.\x02\x03",
            "#10309FHuh, I mean something\x01",
            "It is a generous odysan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00006FNo, it's not a laugh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00111F#11PMy uncle is unclean.\x01",
            "\"Ha ha ha ha, that's an interesting girl,\"\x01",
            "I was saying that … ….\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)
    Sleep(300)

    NpcTalk(
        0x8,
        "Voice of the section chief",
        "Oh, it looks like you're doing it.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(16000, 1850, 4000, 2000)
    MoveCamera(40, 19, 0, 2000)
    SetChrPos(0x8, 20000, 850, 4000, 270)

    def lambda_89A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_89A3)

    def lambda_89B4():
        OP_95(0xFE, 17000, 850, 4000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_89B4)
    SetChrSubChip(0x105, 0x0)
    Sleep(300)
    SetChrSubChip(0x102, 0x1)
    WaitChrThread(0x8, 1)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005FSergey Manager……\x02",
    )

    CloseMessageWindow()
    OP_68(12600, 1850, 6600, 4000)
    MoveCamera(35, 17, 0, 4000)
    OP_92(0x8, 0x39D0, 0x20D0, 0x1F4)
    BeginChrThread(0x101, 3, 0, 25)

    def lambda_8A3D():
        OP_95(0xFE, 14900, 850, 8400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8A3D)
    WaitChrThread(0x8, 1)

    def lambda_8A5B():
        OP_95(0xFE, 12700, 850, 8400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8A5B)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 3)
    OP_6F(0x79)
    Fade(250)
    SetChrPos(0x109, 11100, 850, 5750, 90)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Sound(812, 0, 100, 0)
    OP_0D()
    TurnDirection(0x109, 0x8, 500)

    ChrTalk(
        0x109,
        "#6P#10101FGood morning!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x109, 500)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#01003F#5POh, it is fine as it is.\x02\x03",
            "#01000FBasically the support section#6RUchi#It is a funeralism.\x02\x03",
            "As long as there is nothing extra\x01",
            "Because I will not speak out from me\x01",
            "You should do it properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FHaha …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrPos(0x109, 11300, 900, 6650, 90)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x1)
    Sound(812, 0, 100, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0x105,
        (
            "#6P#10309FHaha.\x01",
            "It is a boss with understanding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00012F… Well …\x01",
            "I can not say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00111FIn the case of the section chief, half of the reason\x01",
            "It is troublesome, is not it?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#01004F#5PI do not know, I guess.\x02\x03",
            "#01002FJust Well, today is exceptional\x01",
            "There is a command from me.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#11PWhat……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#11POr, from the section chief?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003F#5POh, I will ask your support request\x01",
            "You can do away with it.\x02\x03",
            "#01000FI will go to the police school.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#11PTo the police school ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FIt is on the way of West Crossbell Highway\x01",
            "Is it a place where there is a training ground?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#5PFor Lloyd and Noel\x01",
            "It was a familiar place.\x02\x03",
            "#01000FOnce this is ready\x01",
            "Contact at Enigma.\x02\x03",
            "Until then it turned around the city\x01",
            "You should do a request for assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PEr … OK, OK.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F#11PBut what on earth are you doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01002F#5PKuku, it's gone.\x01",
            "It is a pleasure to have fun.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x8, 0x2328, 0x2648, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#01006F#11PThat's it.\x01",
            "I will contact you later.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(10600, 1850, 6600, 3000)

    def lambda_8FFF():
        OP_95(0xFE, 9000, 850, 9800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8FFF)
    WaitChrThread(0x8, 1)

    def lambda_901D():
        OP_95(0xFE, 2000, 850, 9800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_901D)
    Sleep(300)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(12600, 1850, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x105, 0x1)
    OP_0D()

    ChrTalk(
        0x109,
        "#6P#10105FUm … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PNoel ……\x01",
            "I'm very sorry but\x01",
            "This is the style of the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FWell, if you think it favorably\x01",
            "Our autonomy and judgment\x01",
            "I guess they have raised … ….\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10109FI see, I see!\x01",
            "さすがはSergey Managerですね！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHuh, things say good.\x02\x03",
            "#10302Fso?\x01",
            "Are you going to the town right away?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00004FOh, let's do that.\x02\x03",
            "#00005F……そういえば、Keyaが\x01",
            "I told you to go to Sunday school.\x02\x03",
            "#00000FThe manager also went out,\x01",
            "You may as well go out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#11PWell, go up to 3rd floor\x01",
            "Keyaちゃんに声を掛けましょう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_49()
    OP_4C(0x8, 0xFF)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetScenarioFlags(0x126, 1)
    OP_29(0xA1, 0x1, 0x1)
    OP_32(0x6, 0x0, 0x32)
    OP_42(0x6, 0x3E9, 0xFF)
    Call(0, 67)
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    EventEnd(0x5)
    Return()

    # Function_24_7C66 end

    def Function_25_935E(): pass

    label("Function_25_935E")

    Sleep(1500)
    SetChrSubChip(0x109, 0x0)
    Sleep(700)
    SetChrSubChip(0x102, 0x2)
    Sleep(300)
    SetChrSubChip(0x105, 0x1)
    Sleep(500)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)
    SetChrSubChip(0x109, 0x1)
    Return()

    # Function_25_935E end

    def Function_26_9382(): pass

    label("Function_26_9382")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch02902.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    OP_68(12600, 2350, 6600, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 13900, 900, 6650, 270)
    SetChrPos(0x102, 13900, 900, 4600, 270)
    SetChrPos(0x109, 11300, 900, 6650, 90)
    SetChrPos(0x105, 11300, 900, 4600, 90)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 12700, 850, 8400, 180)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)
    OP_68(12600, 1850, 6600, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#01006F#5PApparently today is a day,\x01",
            "It looks like light rain continues.\x02\x03",
            "#01000FIt seems to be a little rough at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIs that so……\x02\x03",
            "#00000FBecause a power car was paid\x01",
            "Let's go around the suburbs as usual\x01",
            "I thought … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWell, it's a day for driving\x01",
            "It is certain that it is not a feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FWow …. I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PBy the way …. Yesterday we\x01",
            "About the person who encountered in the highway\x01",
            "I have not got a follow-up yet, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003F#5POh, even one lesson\x01",
            "It seems that we have not confirmed yet.\x02\x03",
            "#01001FTsao is good, Recta is good with him\x01",
            "They are not all straight lines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FYeah ………\x02\x03",
            "#00006F…… The man who met yesterday, more than that\x01",
            "I was dressed in a dangerous atmosphere.\x02\x03",
            "#00001FI am calm but I can not tell the strange thing\x01",
            "It is said that it is blurring the ferocity ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10103Fsurely……\x01",
            "There was a kind of atmosphere like a tiger.\x02\x03",
            "#10101FIf that comes to mind, in a flash\x01",
            "It seems I'm being attacked and eaten … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12PSnatching nonsense#2RAt once#But\x01",
            "It certainly was such an atmosphere.\x02\x03",
            "#00108FTerrorist or hunter … …\x01",
            "Either way it seems possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10308FHM……\x02\x03",
            "#10304FAnd it will be around the old city\x01",
            "It might be good to gather information.\x02\x03",
            "#10300FMistress of \"Nine valley\"\x01",
            "I feel like I knew various things.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(200)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#00005F#11PAshley in the exchange store?\x02\x03",
            "#00001FFormer weapon merchant, also in the back world\x01",
            "It seems to be detailed in various ways ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#11PCertainly, in that sense\x01",
            "It looks worth a visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#5PWell, at best, do your best.\x02\x03",
            "#01000FJust for you to the end\x01",
            "Do not forget that you are a support department.\x02\x03",
            "Counterbreak#4RFather#If you are too careful about the direction\x01",
            "I will lose sight of the original role?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x109, 0x1)
    Sleep(200)

    ChrTalk(
        0x101,
        "#00005FI understand.\x02",
    )

    CloseMessageWindow()
    OP_92(0x8, 0x39D0, 0x20D0, 0x1F4)
    OP_68(14900, 1850, 6600, 3000)

    def lambda_9AE8():
        OP_95(0xFE, 14900, 850, 8400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9AE8)
    WaitChrThread(0x8, 1)

    def lambda_9B06():
        OP_95(0xFE, 18000, 850, 4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9B06)
    SetChrSubChip(0x105, 0x0)
    Sleep(500)
    SetChrSubChip(0x109, 0x2)
    Sleep(700)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)
    SetChrSubChip(0x102, 0x1)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x5A, 0x1F4)
    ClearMapObjFlags(0x0, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x0)

    def lambda_9B5F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_9B5F)

    def lambda_9B70():
        OP_95(0xFE, 19500, 850, 4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9B70)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    Fade(500)
    OP_68(12600, 1850, 5600, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    OP_0D()
    SetChrSubChip(0x102, 0x2)
    Sleep(100)
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00006F…… for the time being Terminals\x01",
            "Let's check the support request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, I understand.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetScenarioFlags(0x128, 1)
    OP_29(0xA1, 0x1, 0xC)
    OP_C9(0x0, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    Call(0, 67)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_26_9382 end

    def Function_27_9CDC(): pass

    label("Function_27_9CDC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x109, 14100, 850, 9500, 45)
    SetChrPos(0x105, 15600, 850, 8000, 45)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00000F#6PEmergency requests that are out\x01",
            "It's all in Crossbell city.\x02\x03",
            "#00004FIf it was this level\x01",
            "It looks good to clean up all the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12PAlso requested by the foundation, Tio\x01",
            "It might be related … …\x02\x03",
            "#00102FMomo's request also\x01",
            "I would like to listen if possible.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10100FThen, while clearing up the urgent request\x01",
            "Are you visiting a trading shop in the old city?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9EC4():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9EC4)
    Sleep(100)

    def lambda_9ED4():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9ED4)
    Sleep(50)

    def lambda_9EE4():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9EE4)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00002F#5POh, let's do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, it is raining,\x01",
            "Shall I go get it?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetScenarioFlags(0x128, 2)
    OP_29(0xA1, 0x1, 0xD)
    Call(0, 67)
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7150", "ed7562")
    ReplaceBGM("ed7101", "ed7562")
    ReplaceBGM("ed7116", "ed7562")
    ReplaceBGM("ed7117", "ed7562")
    Sleep(500)
    PlayBGM("ed7562", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x232), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_27_9CDC end

    def Function_28_9FB1(): pass

    label("Function_28_9FB1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetScenarioFlags(0x140, 0)
    OP_29(0xA3, 0x4, 0x2)
    OP_29(0xA3, 0x1, 0x0)
    OP_C9(0x0, 0x1000)
    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    OP_32(0x6, 0x0, 0x3A)
    OP_42(0x6, 0x3EB, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 65890, 0, 1800, 225)
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x109, 14000, 850, 9400, 45)
    SetChrPos(0x105, 15500, 850, 7900, 45)
    SetChrPos(0x104, 14000, 850, 7900, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetCameraDistance(23500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 18)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15600, 1750, 9500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x109, 14000, 850, 9400, 45)
    SetChrPos(0x105, 15500, 850, 7900, 45)
    SetChrPos(0x104, 14000, 850, 7900, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#5PThe degree of urgency seems high\x01",
            "From the guard and Ursula hospital ……\x02\x03",
            "#00002FBut, from that Douglas instructor\x01",
            "I will be called.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#00105F#11PDouglas instructor?\x01",
            "You are the deputy commander of the guard, are not you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A237():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A237)
    Sleep(100)

    def lambda_A247():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A247)
    Sleep(50)

    def lambda_A257():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A257)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x101,
        (
            "#00004F#5POh, before being a deputy commander\x01",
            "I was an instructor at the police school.\x02\x03",
            "#00000FFrom improving basic physical strength to fighting training,\x01",
            "Temptation by Tonfa\x01",
            "I was completely knocked down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FOriginally as a guard hope\x01",
            "It was one who was expected.\x02\x03",
            "#10106FBut, it was spoiled by that former guard command\x01",
            "Leisure occupation#4RPerfection#It seems that it was turned to … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FI was taken care of by the exercise\x01",
            "It is terribly tough brother.\x02\x03",
            "#00302FPerhaps with fighting strength,\x01",
            "The guard No. 1 What is it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A42E():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A42E)
    Sleep(50)

    def lambda_A43E():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A43E)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x102,
        (
            "#00104F#11PI see……\x01",
            "That is a pretty awesome person.\x02\x03",
            "#00100FBut, considering the relationship with the guard\x01",
            "I want to see you once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5POh, let's go greetings.\x02\x03",
            "#00003FAlso at Ursula Hospital\x01",
            "From a newly appointed professor ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FOn behalf of Joachim Pharmacology and Neurology\x01",
            "Person to inherit both divisions …\x02\x03",
            "#00301FWell, do not be alarmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FBut, this island is\x01",
            "I have heard it somewhere.\x02\x03",
            "#10300FSurely it is around Remiferia\x01",
            "Was not it a famous name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#11PAt Remiferia's medical manufacturer\x01",
            "There is a place called Seyland.\x02\x03",
            "Although it is a famous family that is also related to the large public estate\x01",
            "It may be possible for those involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PWell, until then\x01",
            "It seems not to be a suspicious person … …\x02\x03",
            "#00001F── Oh well.\x01",
            "There seems to be a story about the example medicine,\x01",
            "I have to go to Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10309FHuff, your longing\x01",
            "It looks like there are some older sisters.\x02\x03",
            "#10302FThe nurse's clothes suits themselves\x01",
            "You are a human like a saint?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_A7F7():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A7F7)
    Sleep(250)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00005F#5PBecome Is it?\x02\x03",
            "#00012Fい、いや、Cecil姉は昔から\x01",
            "Just being indebted … …\x02\x03",
            "#00011F── I do not know. Is it?\x01",
            "I do not know anything but I know what!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00309FLadder, I talked.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00013F#5PCut, Randy … you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00111F#11P(… Lloyd.\x01",
            "It is a little upset. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112F(Fine, it looks like a planet … …)\x02\x03",
            "#10102F(Certainly it was a wonderful person\x01",
            "I think I can understand it … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P…… Kohon.\x01",
            "Well, as it is it.\x02\x03",
            "#00000Fその先生に会う前にCecil姉には\x01",
            "I wish to listen to the story.\x02\x03",
            "#00008F…… Scars left by Joachim#4Rdamage#From\x01",
            "I am worried that the hospital has recovered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PI see …\x02\x03",
            "#00100FOh, but Shizuku-chan\x01",
            "You are coming to town today, are not you?\x02\x03",
            "さっきKeyaちゃんが\x01",
            "I went to play in the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5POh, today is a day\x01",
            "You play with Shizuoka\x01",
            "I went out and went out.\x02\x03",
            "#00002FI will be in the guild\x01",
            "Let's go if there is time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#11PWell, let's do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10305FThe word shizuku is\x01",
            "Is that the daughter of that \"sword of the wind\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FOh, just with the keeper\x01",
            "Do not become like Toshi.\x02\x03",
            "#00302FWith that hard daughter of Osan\x01",
            "It's a good child I can not imagine.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_AD07")

    ChrTalk(
        0x109,
        (
            "#6P#10109FHehu ……\x01",
            "Shizuku-chan, it's cute.\x02\x03",
            "#10102FShe seems to have met Fran\x01",
            "It was really noisy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD88")

    label("loc_AD07")


    ChrTalk(
        0x109,
        (
            "#6P#10109FI have heard rumors\x01",
            "すごく可愛い子Looks like it.\x02\x03",
            "#10102FShe seems to have met Fran\x01",
            "It was really noisy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD88")


    ChrTalk(
        0x105,
        (
            "#12P#10300FHuh, I see.\x02\x03",
            "#10304FThen, I greeted you today.\x01",
            "It goes around the cross bells.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#11P#10302F─ ─ \"Red constellation\" is\x01",
            "While exploring trends.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_AE8F():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AE8F)
    Sleep(50)

    def lambda_AE9F():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AE9F)
    Sleep(50)

    def lambda_AEAF():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AEAF)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00013F#5PWadi …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10101FKimi, you …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306F… Ah, good.\x01",
            "There is also plenty of locking of the guy.\x02\x03",
            "#00303FFormer, what the family say\x01",
            "That guy will be honestly smart.\x02\x03",
            "#00301FPerhaps it was also to exploit an old mine\x01",
            "I guess the chances of those guys will be high.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AFD3():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AFD3)
    Sleep(50)

    def lambda_AFE3():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AFE3)
    Sleep(50)

    def lambda_AFF3():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AFF3)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00005F#5PRandy …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PThat way, like that\x01",
            "You do not need to brand ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FUncle Takashi and Charlie ─\x01",
            "I know well about the two of them.\x02\x03",
            "#00308FI can not affirm it … …\x01",
            "I tried the competence of the support department.\x02\x03",
            "#00301FI threw away the old nest and I got past it\x01",
            "How much can you do#6R噵 噵 噵#I wonder if it's a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#11P……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10108FThat's it … for that … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#5P…………………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10303FThere is no disturbance separately.\x02\x03",
            "#10300FWith just curiosity such a thing\x01",
            "Are those who can do it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FOh, the trap of that extent\x01",
            "They say that greeting is about to them.\x02\x03",
            "#00301FIn that sense, I went back all the way\x01",
            "I person who studied trends of the people alone by myself ─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P── It will be even more.\x02\x03",
            "#00008FCertainly \"Red constellation\" is\x01",
            "I guess they are not allowed to leave.\x02\x03",
            "Even for the purpose of visiting the crossbell\x01",
            "Even in relationship with the Imperial Government\x01",
            "It is necessary to keep track of which one.\x02\x03",
            "#00001FHowever, …\x01",
            "It is totally as a special affairs support section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305FLloyd …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PWe need Randy,\x01",
            "I do not plan to keep Randy alone.\x02\x03",
            "#00001FEven Randy, moving alone\x01",
            "There is no prospect of doing something?\x02\x03",
            "If it's the case\x01",
            "Do not tell me to move arbitrarily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00308F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10309FHuhu, as usual\x01",
            "That's a lot of complaint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10101FBut, it is true!\x02\x03",
            "It is time to adjust forces at such times\x01",
            "It is a mission support department! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#11PYes, of course.\x02\x03",
            "#00100FEven in that cult's case, we\x01",
            "We confronted each other with the power of all.\x02\x03",
            "Randy, are not they the same this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304F……my mother.\x02\x03",
            "#00302FBad, do not be bored\x01",
            "I tried to say it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5POh, it's totally.\x02\x03",
            "#00000FAnyway there is a car,\x01",
            "Today I was finding a support request\x01",
            "Let's go around the suburbs.\x02\x03",
            "Also in the Belgard and Armorika villages\x01",
            "You may extend your legs.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B6D6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B6D6)
    Sleep(50)

    def lambda_B6E6():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B6E6)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#00104F#11PWell, it's been a while ago ….\x02\x03",
            "#00105FBy the way, those who command Sogna\x01",
            "You are at the Belgard gate, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FYeah, it should.\x02\x03",
            "In response to the commerce meeting\x01",
            "I think that I have been busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FThere must be some Mireille guy,\x01",
            "It might be good to show your face there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FGiggle\x01",
            "Well then let's leave.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If the party exceeds 4 people,\x01",
            "The remaining staff is \"support member\"\x01",
            "It will be registered.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "\"Support member\" waits outside theater,\x01",
            "Sometimes it appears in order of the AT, and when the turn comes\x01",
            "It will take various support behaviors.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When it is taken behind with an attack encounter,\x01",
            "Collision including the \"support member\" is disturbed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Equipment of 'support member'\x01",
            "Let 's not forget to prepare.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Replacing party members\x01",
            "キャンプメニューの[TACTICS]から行えます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "また、キャンプメニューの[STATUS]で\x01",
            "Turn ON / OFF use of support craft\x01",
            "You can choose.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_1B(0x0, 0x0, 0x1D)
    OP_1B(0x8, 0x0, 0x1E)
    EventEnd(0x5)
    Return()

    # Function_28_9FB1 end

    def Function_29_BAD6(): pass

    label("Function_29_BAD6")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51275.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00300.itp")
    OP_68(1000, 1100, 1250, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 1000, 10, 3300, 180)
    SetChrPos(0x102, 1500, 10, 1500, 180)
    SetChrPos(0x104, 1500, 0, 2500, 180)
    SetChrPos(0x109, 500, 0, 1000, 180)
    SetChrPos(0x105, 500, 10, 2000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_BBB9():
        OP_97(0x109, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BBB9)
    Sleep(200)

    def lambda_BBD6():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BBD6)
    Sleep(200)

    def lambda_BBF3():
        OP_97(0x105, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BBF3)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    VolumeBGM(0x50, 0x3E8)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_BC2E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BC2E)
    Sleep(400)

    def lambda_BC42():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BC42)

    def lambda_BC53():
        OP_96(0xFE, 0x3E8, 0xA, 0x1F4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BC53)
    Sleep(400)

    def lambda_BC70():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_BC70)

    def lambda_BC81():
        OP_96(0xFE, 0x3E8, 0xA, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC81)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#00003F#5P── Hey, Randy.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x104, 0x101, 500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x104,
        "Hmm? What a Lloyd.\x02",
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
        (
            "#00008F#5PThat……\x01",
            "It's about your father.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#12P#00306FOh, that is ……\x02\x03",
            "#00300FSomething you do not mind separately?\x01",
            "It is not uncommon in that world.\x02\x03",
            "Besides, when I left the group\x01",
            "My father and I have broken hearts.\x02\x03",
            "#00304FI do not feel anything ……\x01",
            "Well, I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P……I see.\x02\x03",
            "#00001FBut, if you feel like it\x01",
            "Please let me know a variety of things?\x02\x03",
            "Once, as a leader\x01",
            "I may be able to ride consultation\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00305F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#5POh, sorry.\x01",
            "Was it a bit cheeky?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00304FHa ha, it is different.\x02\x03",
            "#00302FWhatever you say\x01",
            "I thought that you also grew.\x02\x03",
            "#00309FWell, my older brother is deeply impressed.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_C1DB")

    ChrTalk(
        0x101,
        "#00006F#5PYou know.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00008F#5P…… That time, like this\x01",
            "I want you to manage it somehow.\x02\x03",
            "#00000FAlthough it may not be reliable\x01",
            "Is not it \"buddy\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00305FLloyd …\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    Sleep(300)
    SetCameraDistance(22000, 1000)

    def lambda_C0FA():
        OP_96(0xFE, 0x3E8, 0x0, 0x4E2, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C0FA)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    Sleep(100)
    SetChrSubChip(0x104, 0x1)
    SetChrSubChip(0x101, 0x5)
    Sound(811, 0, 30, 0)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#12P#00302F… …. OK, which story\x01",
            "Perhaps it will be heard.\x02\x03",
            "#00309FThat time I will ask - ___ 0.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PAh……!\x02",
    )

    CloseMessageWindow()
    Jump("loc_C26C")

    label("loc_C1DB")


    ChrTalk(
        0x101,
        "#00006F#5PYou know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00304F… Well, if you feel like it\x01",
            "I might consult him.\x02\x03",
            "#00300FAt that time I will ask for your kindness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PAh……!\x02",
    )

    CloseMessageWindow()

    label("loc_C26C")

    SetChrPos(0x102, 1500, -1000, -4000, 180)
    SetChrPos(0x105, 500, -1000, -4000, 180)

    NpcTalk(
        0x105,
        "Voice of Wadi",
        "#1P#2SWhat are you doing?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x102,
        "Ely's voice",
        "#1P#2SBoth of them are lost articles?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_C363")
    SetCameraDistance(22500, 1000)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)

    def lambda_C34A():
        OP_96(0xFE, 0x3E8, 0x0, 0x2EE, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C34A)
    WaitChrThread(0x104, 1)

    label("loc_C363")


    def lambda_C368():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C368)

    ChrTalk(
        0x101,
        "#00011F#5PSorry, I will go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00304FWell then,\x01",
            "When you start working, it is all.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x3E8)

    def lambda_C3DA():
        OP_97(0x104, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C3DA)
    Sleep(100)

    def lambda_C3F7():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C3F7)
    FadeToDark(1000, 0, -1)
    Sleep(400)

    def lambda_C41E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C41E)
    Sleep(400)

    def lambda_C432():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C432)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "With a driving car, across the crossbell\x01",
            "It is now possible to move.\x02\x03",
            "At the back door of the Special Affairs Support Division on Nishi Dori\x01",
            "Please stop using it because it is stopped.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x140, 1)
    OP_C9(0x1, 0x1000)
    EventEnd(0x5)
    NewScene("c0100", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_29_BAD6 end

    def Function_30_C53E(): pass

    label("Function_30_C53E")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51275.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00300.itp")
    OP_68(-2250, 1100, 67800, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -2000, 10, 69500, 180)
    SetChrPos(0x102, -2000, 10, 68300, 270)
    SetChrPos(0x104, -1000, 0, 68300, 270)
    SetChrPos(0x109, -2500, 10, 67300, 270)
    SetChrPos(0x105, -1500, 10, 67300, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_C621():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C621)
    Sleep(200)

    def lambda_C63E():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C63E)
    Sleep(200)

    def lambda_C65B():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C65B)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    VolumeBGM(0x50, 0x3E8)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_C696():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C696)
    Sleep(400)

    def lambda_C6AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C6AA)
    Sleep(400)

    def lambda_C6BE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C6BE)

    def lambda_C6CF():
        OP_96(0xFE, 0xFFFFF448, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C6CF)
    Sleep(300)

    def lambda_C6EC():
        OP_96(0xFE, 0xFFFFFA24, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C6EC)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00003F#11P── Hey, Randy.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x104, 0x101, 500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x104,
        "Hmm? What a Lloyd.\x02",
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
        (
            "#00008F#11PThat……\x01",
            "It's about your father.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00306FOh, that is ……\x02\x03",
            "#00300FSomething you do not mind separately?\x01",
            "It is not uncommon in that world.\x02\x03",
            "Besides, when I left the group\x01",
            "My father and I have broken hearts.\x02\x03",
            "#00304FI do not feel anything ……\x01",
            "Well, I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P……I see.\x02\x03",
            "#00001FBut, if you feel like it\x01",
            "Please let me know a variety of things?\x02\x03",
            "Once, as a leader\x01",
            "I may be able to ride consultation\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#11POh, sorry.\x01",
            "Was it a bit cheeky?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FHa ha, it is different.\x02\x03",
            "#00302FWhatever you say\x01",
            "I thought that you also grew.\x02\x03",
            "#00309FWell, my older brother is deeply impressed.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_CC4C")

    ChrTalk(
        0x101,
        "#00006F#11PYou know.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00008F#11P…… That time, like this\x01",
            "I want you to manage it somehow.\x02\x03",
            "#00000FAlthough it may not be reliable\x01",
            "Is not it \"buddy\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305FLloyd …\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    SetCameraDistance(22000, 1000)

    def lambda_CB6B():
        OP_96(0xFE, 0xFFFFF736, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CB6B)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x2)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    Sleep(100)
    SetChrSubChip(0x104, 0x3)
    SetChrSubChip(0x101, 0x7)
    Sound(811, 0, 30, 0)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#6P#00302F… …. OK, which story\x01",
            "Perhaps it will be heard.\x02\x03",
            "#00309FThat time I will ask - ___ 0.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11PAh……!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CCDE")

    label("loc_CC4C")


    ChrTalk(
        0x101,
        "#00006F#11PYou know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304F… Well, if you feel like it\x01",
            "I might consult him.\x02\x03",
            "#00300FAt that time I will ask for your kindness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PAh……!\x02",
    )

    CloseMessageWindow()

    label("loc_CCDE")

    SetChrPos(0x102, -7000, -2000, 68300, 270)
    SetChrPos(0x105, -7000, -2000, 67300, 270)

    NpcTalk(
        0x105,
        "Voice of Wadi",
        "#2P#2SWhat are you doing?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x102,
        "Ely's voice",
        "#2P#2SBoth of them are lost articles?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_CDD5")
    SetCameraDistance(22500, 700)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)

    def lambda_CDBC():
        OP_96(0xFE, 0xFFFFF542, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CDBC)
    WaitChrThread(0x104, 1)

    label("loc_CDD5")


    def lambda_CDDA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CDDA)

    ChrTalk(
        0x101,
        "#00011F#11PSorry, I will go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00304FWell then,\x01",
            "When you start working, it is all.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x3E8)

    def lambda_CE4E():
        OP_97(0x104, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CE4E)
    Sleep(100)

    def lambda_CE6B():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CE6B)
    FadeToDark(1000, 0, -1)
    Sleep(400)

    def lambda_CE92():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CE92)
    Sleep(400)

    def lambda_CEA6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CEA6)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "With a driving car, across the crossbell\x01",
            "It is now possible to move.\x02\x03",
            "At the back door of the Special Affairs Support Division on Nishi Dori\x01",
            "Please stop using it because it is stopped.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x140, 1)
    OP_C9(0x1, 0x1000)
    EventEnd(0x5)
    NewScene("c0200", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_30_C53E end

    def Function_31_CFB2(): pass

    label("Function_31_CFB2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch02710.itc", 0x23)
    LoadChrToIndex("apl/ch50090.itc", 0x24)
    LoadChrToIndex("apl/ch50092.itc", 0x25)
    SoundLoad(3605)
    OP_68(12600, 2550, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x1)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 13900, 900, 4600, 270)
    SetChrPos(0x102, 13900, 900, 2550, 270)
    SetChrPos(0x104, 11300, 900, 2550, 90)
    SetChrPos(0x109, 11300, 900, 6650, 90)
    SetChrPos(0x105, 11300, 900, 4600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 13900, 900, 6650, 270)
    SetChrChipByIndex(0xF, 0x25)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 13000, 1450, 6600, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0xE)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 13400, 1300, 6600, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x25)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 12400, 1450, 6600, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0xE)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 12000, 1300, 6600, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x25)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13000, 1450, 4600, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0xE)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13400, 1300, 4600, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x25)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12400, 1450, 4600, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0xE)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12000, 1300, 4600, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x25)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 12400, 1450, 2600, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0xE)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 12000, 1300, 2600, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x25)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1450, 2600, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0xE)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13400, 1300, 2600, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x24)
    SetChrSubChip(0x1B, 0x7)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12700, 1400, 5500, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x7)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12700, 1400, 3500, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x25)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 16000, 750, 5500, 0)
    SetChrSubChip(0xF, 0x7)
    SetChrSubChip(0x11, 0x7)
    SetChrSubChip(0x13, 0x7)
    SetChrSubChip(0x15, 0x7)
    SetChrSubChip(0x17, 0x7)
    SetChrSubChip(0x19, 0x7)
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00003F─ ─ I see.\x01",
            "Is the real committee meeting going tomorrow?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(12600, 2050, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x8,
        (
            "#5P#01003FOh, for today\x01",
            "Various talks to the luncheon#4RFun#It is a meeting place.\x02\x03",
            "#01002FIn addition to the dinner party in the evening\x01",
            "It seems there is a theater of alkane shell.\x02\x03",
            "By the way, all the leaders,\x01",
            "Guest House in Michelin#6REconomic depression#I'm planning to stay at the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWhen we say guesthouse,\x01",
            "It is the mansion of former Hartmann chairman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305FOh, that idiot deca house,\x01",
            "Is it used like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01006FWell, about Hartmann\x01",
            "Fines for corruption and illegal transactions\x01",
            "It has become a tremendous amount.\x02\x03",
            "#01000FAs confiscated as confiscated\x01",
            "It was used as a guest guesthouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FWell …\x01",
            "Well, it is self-interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FWell, of course, toward Michelam\x01",
            "Is it a blockade?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01003FOh, during the trade meeting\x01",
            "Hotel and theme parks are temporarily closed.\x02\x03",
            "#01002FBecause the guard is stuffed up there\x01",
            "There is no need to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PI understand.\x02\x03",
            "#00000FFor us, following yesterday\x01",
            "I will concentrate on support activities, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01004FThat would be fine.\x02\x03",
            "#01000FAmong the invited guests, after the luncheon,\x01",
            "There seems to be some visitors to the crossbell.\x02\x03",
            "Because there may be some problems\x01",
            "You should follow up with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104FOK.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FHowever, as expected, invited guests\x01",
            "It was not the same aura.\x02\x03",
            "#00301FEspecially \"Chairman of Iron Blood\" … …\x01",
            "You are not Tadamon.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#5POh, that Captain Rector\x01",
            "I was worried that I was holding down … ….\x02\x03",
            "#00008FThe Prime Minister more than that\x01",
            "It was the owner of the overwhelming atmosphere.\x02\x03",
            "#00001FRepublic President Rock Smith\x01",
            "It was a friendly atmosphere, but ……\x02\x03",
            "#00005F…… But close by\x01",
            "That Kirica has refrained from you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)

    ChrTalk(
        0x102,
        (
            "#00103FCalvert's intelligence organization,\x01",
            "\"Rock Smith Institution\" human being … ….\x02\x03",
            "#00108FAlthough it is a president known for the common people\x01",
            "I guess it will not go on smoothly after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10102FBut Libert's Claudia princess\x01",
            "As you expected there was elegance.\x02\x03",
            "#10109FAssociate Yulia who was together also\x01",
            "It was very cool!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#6P#10305FOh, in the Liber Kingdom\x01",
            "Is it a women captain of the royal guard?\x02\x03",
            "#10302FAnything is that streak,\x01",
            "It seems there are enthusiastic fans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10112FWell, yeah … that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHaha ……\x01",
            "I am also a little fan.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(250)

    ChrTalk(
        0x101,
        "#5P#00005FOh, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FWhat is it ~?\x01",
            "Daughter, was that kind of hobby?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#00102FAlthough it is not a separate hobby, ….\x02\x03",
            "#00104FThat, when I stayed in Libert before,\x01",
            "Saw the parade of the royal guards … …\x02\x03",
            "#00100FSome photo books were out\x01",
            "I bought it without thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00012FI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10101FPlease, show me later!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#00109FHaha ……\x01",
            "Yes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FWhew, it is deplorable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHoff, a manly wrestler\x01",
            "Because it is a kind of romance.\x02\x03",
            "#10302FAs for me, your imperial Prince's Prince also\x01",
            "I was worried quite well though.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F#11POliver tomato ……\x01",
            "Recently I heard a name that I hear.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)

    ChrTalk(
        0x102,
        (
            "#00104FTo solve the incident of Libert\x01",
            "It is famous for playing a part.\x02\x03",
            "#00100FThen attend various events\x01",
            "It seems to be reputable ….\x02\x03",
            "Certainly the right to succeed to the throne\x01",
            "You do not have it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5P#00001FIs it so……\x02\x03",
            "#00005FWell, to resolve the incident of Libert\x01",
            "What I mean by playing a role ……\x02\x03",
            "#00000FWith Esther and Joshua\x01",
            "Are they acquainted?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FOh, remember that … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FThe two of them seemed to be wide\x01",
            "It might be possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x8000)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 1000, 0, -2000, 0)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xA, 0x8000)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, 1000, 0, -2000, 0)
    Sound(103, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x9,
        "Keyaの声",
        "#3605V#30W#12AI'm home.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(1000, 1100, 1500, 2000)
    MoveCamera(40, 23, 0, 2000)
    SetCameraDistance(22000, 2000)
    SetChrSubChip(0x102, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x104, 0x2)
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x105, 0x2)
    Sleep(1300)

    def lambda_E25F():
        OP_96(0xFE, 0x3E8, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E25F)

    def lambda_E279():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_E279)
    Sleep(1000)

    def lambda_E28D():
        OP_96(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E28D)

    def lambda_E2A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_E2A7)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)

    def lambda_E2C0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_E2C0)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x5A, 0x1F4)
    SetChrSubChip(0xA, 0x5)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00002FKeya、Zeit、お帰り。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6P#01200Fwon.\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)

    def lambda_E324():
        OP_96(0xFE, 0x3E8, 0x352, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E324)
    Sleep(1000)
    Fade(1000)
    OP_68(10600, 1850, 6600, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    OP_68(12600, 1850, 6600, 3000)
    EndChrThread(0x9, 0x1)
    SetChrPos(0x9, 5000, 850, 8900, 90)

    def lambda_E39A():
        OP_96(0xFE, 0x2AF8, 0x352, 0x22C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E39A)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x105, 0x1)
    SetChrSubChip(0x104, 0x1)
    OP_0D()
    WaitChrThread(0x9, 1)
    SetChrSubChip(0x8, 0x2)
    OP_93(0x9, 0xB4, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#00105FOh, Shizuku-chan\x01",
            "Were not you with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01106F#5POh, yeah, with my dad\x01",
            "I returned to the hospital.\x02\x03",
            "#01110FBut, the building's owner is\x01",
            "I saw it together.\x02\x03",
            "#01109FIt was amazing!\x01",
            "You saw Lloyd nearby, did not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FOh, honestly too big\x01",
            "I did not understand well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300F#NWell, what a ridiculous building is\x01",
            "I know as much as I can.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#6P#10109Fふふっ、Keyaちゃんの方が\x01",
            "Perhaps you could have seen it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01109F#5PWow!\x01",
            "It was sooo cool!\x02\x03",
            "#01110FHanabi … Is that it?\x01",
            "That was also pretty beautiful!\x02\x03",
            "#01102FBut …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)

    ChrTalk(
        0x101,
        "#00005FWhat's the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01104F#5POh, no, nothing.\x02\x03",
            "#01100FLloyd's coming now\x01",
            "Are you going to work again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I think I will be back in the evening.\x02\x03",
            "How is the section chief?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5P#01003FToday I am on standby.\x02\x03",
            "#01002FI will contact you if there is something\x01",
            "Please do not hesitate to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004FYes, with your words.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FAfter checking the terminal\x01",
            "Shall I go out?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    Sleep(500)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
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
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 64000, 200, 11400, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    OP_4C(0xA, 0xFF)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x140, 3)
    OP_29(0xA3, 0x1, 0x7)
    OP_29(0xA3, 0x1, 0x8)
    Call(0, 67)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E91D")
    Jump("loc_E922")

    label("loc_E91D")

    OP_29(0x73, 0x4, 0x40)

    label("loc_E922")

    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_31_CFB2 end

    def Function_32_E928(): pass

    label("Function_32_E928")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15600, 1750, 9500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x109, 14000, 850, 9400, 45)
    SetChrPos(0x105, 15500, 850, 7900, 45)
    SetChrPos(0x104, 14000, 850, 7900, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00001F#5PVarious things come … ….\x01",
            "Do not mind anything.\x02\x03",
            "#00006FThis performer's search is\x01",
            "I do not know for a moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FNo, but, no way.\x01",
            "It is not my sister's request.\x02\x03",
            "#00302FTraining is not sexy\x01",
            "I want to get lost if I have time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10104FHeh heh, it might be a good opportunity.\x02\x03",
            "#10100FSearching for a cat here\x01",
            "I'd like to be from that family, but …\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EB52():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EB52)

    def lambda_EB5F():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_EB5F)
    Sleep(50)

    def lambda_EB6F():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_EB6F)

    def lambda_EB7C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_EB7C)
    WaitChrThread(0x101, 2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_EC1A")

    ChrTalk(
        0x101,
        (
            "#00002F#5POh, I moved to Eastern Avenue\x01",
            "It's Bond's place.\x02\x03",
            "#00004FThat cat has an edge, too …\x01",
            "I want to become a force if possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC97")

    label("loc_EC1A")


    ChrTalk(
        0x101,
        (
            "#00002F#5POh, I moved to Eastern Avenue\x01",
            "It's Bond's place.\x02\x03",
            "#00003FIt looks like a lot of hardship … …\x01",
            "I want to become a force if possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC97")


    ChrTalk(
        0x102,
        (
            "#00104F#11PWell, I agree.\x02\x03",
            "#00100FIt seems that he relied on us,\x01",
            "Do not forget to visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHuff and tower announcement\x01",
            "With VIPs' visit\x01",
            "The town seems to stand up.\x02\x03",
            "#10302FAlso trying around various things\x01",
            "It might be fun.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x140, 4)
    OP_29(0xA3, 0x1, 0x9)
    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    Call(0, 67)
    EventEnd(0x5)
    Return()

    # Function_32_E928 end

    def Function_33_EDD2(): pass

    label("Function_33_EDD2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("apl/ch51090.itc", 0x23)
    LoadChrToIndex("apl/ch50092.itc", 0x24)
    LoadChrToIndex("apl/ch51210.itc", 0x25)
    SoundLoad(3606)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01102.itp")
    ClearMapFlags(0x10000000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF03")
    OP_68(1300, 1850, 11800, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    OP_90(0x101, 1700, 4850, 14100, 180)
    OP_90(0x102, 600, 4850, 14400, 180)
    OP_90(0x104, 1700, 4850, 15400, 180)
    OP_90(0x109, 600, 4850, 15700, 180)
    OP_90(0x105, 1700, 4850, 16700, 180)
    Jump("loc_EF86")

    label("loc_EF03")

    OP_68(1000, 1000, 700, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x101, 300, 0, -1600, 0)
    SetChrPos(0x102, 1400, 0, -1900, 0)
    SetChrPos(0x104, 300, 0, -2900, 0)
    SetChrPos(0x109, 1400, 0, -3200, 0)
    SetChrPos(0x105, 300, 0, -4200, 0)

    label("loc_EF86")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x25)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 11000, 850, 14000, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F023")
    OP_68(1300, 1850, 9800, 3500)
    BeginChrThread(0x101, 3, 0, 34)
    Jump("loc_F0C2")

    label("loc_F023")

    OP_68(1000, 1000, 2700, 3500)

    def lambda_F039():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F039)
    Sleep(200)

    def lambda_F056():
        OP_97(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F056)
    Sleep(200)

    def lambda_F073():
        OP_97(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F073)
    Sleep(200)

    def lambda_F090():
        OP_97(0x109, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F090)
    Sleep(200)

    def lambda_F0AD():
        OP_97(0x105, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F0AD)

    label("loc_F0C2")

    FadeToBright(1000, 0)

    def lambda_F0D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F0D0)
    Sleep(400)

    def lambda_F0E4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F0E4)
    Sleep(600)

    def lambda_F0F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F0F8)
    Sleep(400)

    def lambda_F10C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F10C)
    Sleep(600)

    def lambda_F120():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_F120)
    OP_0D()
    StopBGM(0xFA0)
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitChrThread(0x105, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F22E")

    ChrTalk(
        0x101,
        "#5P#00002Fthat……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00109FOh……\x01",
            "It smells really nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10302FOh, the maple syrup\x01",
            "It looks like a smell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F2AE")

    label("loc_F22E")


    ChrTalk(
        0x101,
        "#00002F#5Pthat……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#11POh……\x01",
            "It smells really nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FOh, the maple syrup\x01",
            "It looks like a smell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F2AE")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7105", 0)
    OP_68(11000, 1750, 10500, 2000)
    SetCameraDistance(26500, 2000)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)

    def lambda_F2F2():
        OP_95(0xFE, 10810, 850, 11410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F2F2)

    def lambda_F30C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_F30C)
    WaitChrThread(0x9, 1)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F3B5")
    SetChrPos(0x101, 1700, -850, 9100, 180)
    SetChrPos(0x102, 600, -850, 9400, 180)
    SetChrPos(0x104, 1700, -850, 10400, 180)
    SetChrPos(0x109, 600, -850, 10700, 180)
    SetChrPos(0x105, 1700, -850, 11700, 180)

    label("loc_F3B5")


    def lambda_F3BA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_F3BA)
    Sleep(150)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x9,
        (
            "#3606V#30WOh, Lloyd.\x01",
            "After all it came back.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE16)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        (
            "#00009FOh, for a short break.\x02\x03",
            "#00000FEven so ……\x01",
            "Did you bake the muffin?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F556")

    ChrTalk(
        0x9,
        (
            "#01104F#11PEh … … everyone else\x01",
            "I felt like I was about to return.\x02\x03",
            "#01110FIt's Maple Muffin.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5BE")

    label("loc_F556")


    ChrTalk(
        0x9,
        (
            "#01104F#5PEh … … everyone else\x01",
            "I felt like I was about to return.\x02\x03",
            "#01110FIt's Maple Muffin.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F5BE")


    ChrTalk(
        0x104,
        (
            "#00305FOh……\x01",
            "Kiyoshi, you are attentive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FHuh, I'm glad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FIt's no problem\x01",
            "Shall I make some tea?\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(27000, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_68(12600, 2650, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 13900, 900, 5400, 270)
    SetChrPos(0x102, 11300, 900, 6650, 90)
    SetChrPos(0x104, 13900, 900, 3800, 270)
    SetChrPos(0x109, 11300, 900, 2550, 90)
    SetChrPos(0x105, 13900, 900, 2200, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 13900, 900, 7000, 270)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x1)
    SetChrPos(0x9, 11300, 900, 4600, 90)
    SetChrChipByIndex(0xA, 0x6)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 16300, 850, 6400, 180)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x0, 0x1)
    ClearChrFlags(0x22, 0x80)
    OP_78(0xB, 0x22)
    ClearChrFlags(0x23, 0x80)
    OP_78(0xC, 0x23)
    ClearChrFlags(0x24, 0x80)
    OP_78(0xD, 0x24)
    ClearChrFlags(0x25, 0x80)
    OP_78(0xE, 0x25)
    ClearChrFlags(0x26, 0x80)
    OP_78(0xF, 0x26)
    ClearChrFlags(0x27, 0x80)
    OP_78(0x10, 0x27)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x11, 0x28)
    OP_49()
    SetChrPos(0x22, 14000, 0, 7000, 0)
    OP_D5(0x22, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x23, 14000, 0, 5400, 0)
    OP_D5(0x23, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x24, 14000, 0, 3800, 0)
    OP_D5(0x24, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x25, 14000, 0, 2200, 0)
    OP_D5(0x25, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x26, 11200, 0, 6650, 0)
    OP_D5(0x26, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x27, 11200, 0, 4600, 0)
    OP_D5(0x27, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x28, 11200, 0, 2550, 0)
    OP_D5(0x28, 0x0, 0x15F90, 0x0, 0x0)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 13000, 1400, 7100, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x2)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 13100, 1350, 6700, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 12400, 1400, 6600, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x2)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 12300, 1350, 7100, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13000, 1400, 5400, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x2)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13100, 1350, 5000, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12400, 1400, 4600, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x1)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12300, 1350, 5100, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 13000, 1400, 3800, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x2)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 13100, 1350, 3400, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x23)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1400, 2100, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x23)
    SetChrSubChip(0x1A, 0x2)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13100, 1350, 1700, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x23)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12400, 1400, 2600, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x23)
    SetChrSubChip(0x1C, 0x2)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12300, 1350, 3100, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 16300, 750, 5500, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    Sleep(500)
    OP_68(12600, 2150, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x8,
        (
            "#5P#01005F─ ─ I see.\x01",
            "Did you come across such a place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PYeah, something aimed\x01",
            "It seems not to be the translation that appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F…… towards \"Red constellation\"\x01",
            "Is there no movement as ever?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01004FIf there is something from one department\x01",
            "You should have a call here.\x02\x03",
            "#01002FI do not even know the feeling\x01",
            "Well, do not panic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00304FHaha … OK.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#11PWell, what's worrisome\x01",
            "Not only \"red constellation\".\x02\x03",
            "#00001FAnyway, there are no signs\x01",
            "Take care and turn around.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(200)
    SetChrSubChip(0x9, 0x0)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#6P#00108FI see …\x01",
            "In the situation where VIP is visited\x01",
            "It will be hard if something happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FIf you can afford it by car\x01",
            "Let's also go to the suburbs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#01105FLloyd, are you going out again?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)

    ChrTalk(
        0x101,
        (
            "#00004F#11POh, it is resuming work.\x02\x03",
            "#00002FMuffin, thank you.\x01",
            "It was very tasty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00109FHuh, than any of us\x01",
            "My cooking has gone well.\x02\x03",
            "#00102FPossibly to Mr. Oscar\x01",
            "Did you learn how to make it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)
    Sleep(150)

    ChrTalk(
        0x9,
        "#6P#01109FWell, sort of like that.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#6P#01110FOh, I still have a rest\x01",
            "If you like, eat it.\x02\x03",
            "If it is about tomorrow\x01",
            "I think it's all right.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '枫糖蛋糕'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got five pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('枫糖蛋糕', 5)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        "#10302FWell, it is a sharp look.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWow …\x01",
            "Dad, I will cry!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#5P……Wait a minute.\x02\x03",
            "#00013FEven Randy\x01",
            "Keyaの父親役は譲れないぞ？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#00302FHood, funny.\x01",
            "Let's get in touch with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#01105FBarking ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FFuu …\x01",
            "What are you talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10112FHaha ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FParent stupid, it's boring here.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_32(0xFF, 0xFE, 0x0)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    OP_4C(0x9, 0xFF)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 64000, 200, 11400, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 123270, 0, 4980, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 119610, 30, 4470, 225)
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
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrPos(0x22, 22900, 0, 12700, 0)
    SetChrPos(0x23, 22900, 0, 12700, 0)
    SetChrPos(0x24, 22900, 0, 12700, 0)
    SetChrPos(0x25, 22900, 0, 12700, 0)
    SetChrPos(0x26, 22900, 0, 12700, 0)
    SetChrPos(0x27, 22900, 0, 12700, 0)
    SetChrPos(0x28, 22900, 0, 12700, 0)
    SetMapObjFrame(0xFF, "isu00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x1, 0x1)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x140, 6)
    OP_29(0xA3, 0x1, 0x10)
    OP_C9(0x0, 0x1000)
    PlayBGM("ed7150", 0)
    EventEnd(0x5)
    Return()

    # Function_33_EDD2 end

    def Function_34_103B4(): pass

    label("Function_34_103B4")


    def lambda_103B9():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_103B9)
    Sleep(200)

    def lambda_103D6():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_103D6)
    Sleep(200)

    def lambda_103F3():
        OP_97(0x104, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_103F3)
    Sleep(200)

    def lambda_10410():
        OP_97(0x109, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10410)
    Sleep(200)

    def lambda_1042D():
        OP_97(0x105, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1042D)
    Return()

    # Function_34_103B4 end

    def Function_35_10443(): pass

    label("Function_35_10443")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(14100, 1750, 12300, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(22000, 0)
    SoundLoad(848)
    SoundLoad(3607)
    SoundLoad(3608)
    SetChrPos(0x101, 5000, 0, 15000, 0)
    SetChrPos(0x102, 5000, 0, 15000, 0)
    SetChrPos(0x104, 5000, 0, 15000, 0)
    SetChrPos(0x109, 5000, 0, 15000, 0)
    SetChrPos(0x105, 5000, 0, 15000, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 11000, 850, 14000, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 13100, 850, 9300, 0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    OP_70(0xA, 0x0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x14, 0x0, 0x20)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Sound(848, 2, 100, 0)
    Sleep(2000)
    PlayBGM("ed7102", 0)
    SetCameraDistance(24000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)

    def lambda_105B2():
        OP_95(0xFE, 11000, 850, 12300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_105B2)

    def lambda_105CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_105CC)
    WaitChrThread(0x9, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(300)

    def lambda_105FD():
        OP_95(0xFE, 14100, 850, 12300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_105FD)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0x0, 0x1F4)
    OP_79(0x1)
    ClearMapObjFlags(0x1, 0x10)
    Sound(838, 0, 100, 0)
    OP_24(0x350)
    ClearMapObjFlags(0xA, 0x20)
    OP_70(0xA, 0x32)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01110F#3607V#30WEr, Hello?\x02\x03",
            "#01109F#3608VCross Bell Police,\x01",
            "I will be in the Special Affairs Support Division.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE18)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Voice of a girl")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あ……Keyaですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01105FOh, Tio!\x02\x03",
            "#01109FIt also hung me again -.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Voice of Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hehe, unlike yesterday\x01",
            "Although it is ordinary power communication.\x02\x03",
            "Possibly\x01",
            "Is there anyone nearby?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01100FYeah, hey, hey\x01",
            "I just went out earlier.\x02\x03",
            "Zeitはそこにいるけどー。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(230, 190, -1, -1)

    AnonymousTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01200Fwon.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Voice of Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hmm, is that so?\x02\x03",
            "…… Actually, Mr. Lloyd's\x01",
            "Do not connect to Enigma.\x02\x03",
            "So directly to the support department,\x01",
            "I contacted you ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01105FHmmm, that's right.\x02\x03",
            "#01111FIf it were Lloyd's\x01",
            "Called by pale white falcons\x01",
            "It seems like I went out.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Voice of Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "False hayabusa ……?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01110FOh, say Sieg.\x01",
            "Zeitみたいに喋れるの。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Voice of Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "… … somewhat different\x01",
            "進展しているLooks like it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(801, 0, 50, 0)
    Sleep(1300)
    SetMessageWindowPos(250, 0, -1, -1)
    SetChrName("Female voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#1S#40WEveryone … ….\x01",
            "I have kept you waiting for a long time.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#1S#40WFrom this … … Leman ……\x01",
            "………I shall go……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01105FIs it? Is it? Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Voice of Tio")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──時間Looks like it.\x02\x03",
            "Keya、また後で。\x01",
            "Mr. Lloyd and the section chief\x01",
            "Please say hello to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01109FWell, see you again.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(230, 190, -1, -1)

    AnonymousTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01200Fwon.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(838, 0, 100, 0)
    SetMapObjFlags(0xA, 0x4)
    Sleep(500)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 1000, 0, -1500, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    Sleep(500)

    NpcTalk(
        0x8,
        "Sergei's voice",
        "Oh, I came back.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_10C47():

        label("loc_10C47")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_10C47")

    QueueWorkItem2(0x9, 2, lambda_10C47)
    OP_68(1960, 1750, 2650, 2500)
    MoveCamera(40, 17, 0, 2500)
    Sleep(2000)

    def lambda_10C78():
        OP_95(0xFE, 1000, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10C78)

    def lambda_10C92():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_10C92)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x2D, 0x1F4)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#01101F#12POh, dear.\x02\x03",
            "#01106FIf I come home earlier\x01",
            "I could talk with Tio!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01005F#6PWhat, was communication in?\x02\x03",
            "#01002FSo what did you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01110F#12PUm, he's that.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 36)
    Sleep(1000)
    OP_68(1960, 2250, 2650, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x8, 0xFF)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x350)
    SetScenarioFlags(0x22, 0)
    NewScene("e3210", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_35_10443 end

    def Function_36_10DBA(): pass

    label("Function_36_10DBA")


    def lambda_10DBF():
        OP_95(0xFE, 1000, 850, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10DBF)
    WaitChrThread(0x8, 1)

    def lambda_10DDD():
        OP_95(0xFE, 10000, 850, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10DDD)
    WaitChrThread(0x8, 1)
    Return()

    # Function_36_10DBA end

    def Function_37_10DF7(): pass

    label("Function_37_10DF7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetScenarioFlags(0x141, 5)
    OP_29(0xA3, 0x1, 0x14)
    OP_29(0xA3, 0x1, 0x15)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10E23")
    Jump("loc_10E28")

    label("loc_10E23")

    OP_29(0x75, 0x4, 0x40)

    label("loc_10E28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10E39")
    Jump("loc_10E3E")

    label("loc_10E39")

    OP_29(0x76, 0x4, 0x40)

    label("loc_10E3E")

    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x103, 16300, 850, 10200, 45)
    SetChrPos(0x101, 14600, 850, 9200, 45)
    SetChrPos(0x102, 15000, 850, 8200, 45)
    SetChrPos(0x104, 13400, 850, 9400, 90)
    SetChrPos(0x109, 15700, 850, 7400, 0)
    SetChrPos(0x105, 17000, 850, 7600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 14200, 850, 11900, 135)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)
    SetCameraDistance(23500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 18)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x103, 16300, 850, 10200, 45)
    SetChrPos(0x101, 14600, 850, 9200, 45)
    SetChrPos(0x102, 15000, 850, 8200, 45)
    SetChrPos(0x104, 13400, 850, 9400, 90)
    SetChrPos(0x109, 15700, 850, 7400, 0)
    SetChrPos(0x105, 17000, 850, 7600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 14200, 850, 11900, 135)
    ClearChrFlags(0x8, 0x80)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#6P#00003F…… after all some\x01",
            "Is the new one coming?\x02\x03",
            "#00001FWell, none are fine\x01",
            "I am interested, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00104FIf there is time to spare\x01",
            "Let's stop by.\x02\x03",
            "#00100FIf it's morning\x01",
            "I can move freely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FIf you use a car you can also go to the suburbs\x01",
            "You seem to be able to move.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1113B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1113B)
    WaitChrThread(0x103, 2)
    Sleep(150)

    ChrTalk(
        0x103,
        (
            "#00204F#5PIs it a car …?\x01",
            "It is a little fun.\x02\x03",
            "#00202FAnything ZCF\x01",
            "Is it a driven car you developed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FOh, one of the divisions also\x01",
            "It's a new model looking back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FBut Tio,\x01",
            "I just arrived yesterday\x01",
            "Do you move early in the morning?\x02\x03",
            "#00000FWhat is it in the morning?\x01",
            "Even if you do slowly - ─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#5PGirorot …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006FI'm sorry, but.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#5P…… Completely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FHaha, something Tio Sukei\x01",
            "I feel like I came back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00109FHehe … … That's right.\x02\x03",
            "#00102FAfter all, before the terminal\x01",
            "Those who have Tio\x01",
            "It feels like I'm coming.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11372():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11372)
    Sleep(50)

    def lambda_11382():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_11382)
    WaitChrThread(0x109, 2)

    ChrTalk(
        0x109,
        (
            "#12P#10109FHuh, after all, everyone,\x01",
            "You are in breath.\x02\x03",
            "#10102FTentatively …\x01",
            "With this, the new-generation /\x01",
            "It is a full member.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PAs Huff, as a leader\x01",
            "Is not she deeply embarrassed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FOh … That's right.\x02\x03",
            "#00002F── Anyway Tio.\x01",
            "I'm begging to ask you again.\x02\x03",
            "Take a trouble with it\x01",
            "Thank you for returning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#5PYes, this is new\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FHaha, something tension,\x01",
            "You came up.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#01004F#5PPowered by Translate\x01",
            "I am feeling well above all.\x02\x03",
            "#01002FWell, I'm fine.\x01",
            "To the air of the trade council\x01",
            "You do not have to be swallowed.\x02\x03",
            "In your way of doing\x01",
            "You should come and help us with security.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1161A():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1161A)
    Sleep(50)

    def lambda_1162A():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1162A)
    Sleep(50)

    def lambda_1163A():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1163A)
    Sleep(50)

    def lambda_1164A():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1164A)
    Sleep(50)

    def lambda_1165A():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1165A)
    Sleep(50)

    def lambda_1166A():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1166A)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    def lambda_1168F():

        label("loc_1168F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1168F")

    QueueWorkItem2(0x101, 2, lambda_1168F)

    def lambda_116A1():

        label("loc_116A1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_116A1")

    QueueWorkItem2(0x102, 2, lambda_116A1)

    def lambda_116B3():

        label("loc_116B3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_116B3")

    QueueWorkItem2(0x103, 2, lambda_116B3)

    def lambda_116C5():

        label("loc_116C5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_116C5")

    QueueWorkItem2(0x104, 2, lambda_116C5)

    def lambda_116D7():

        label("loc_116D7")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_116D7")

    QueueWorkItem2(0x109, 2, lambda_116D7)

    def lambda_116E9():

        label("loc_116E9")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_116E9")

    QueueWorkItem2(0x105, 2, lambda_116E9)

    ChrTalk(
        0x101,
        "#12P#00000FIt is okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FThe direction of the section chief is now\x01",
            "Were you waiting at the police headquarters?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01006F#5POh, negotiate with each direction\x01",
            "I was pressed.\x02\x03",
            "#01000FI turn around to backup\x01",
            "For the security of the Orchis Tower\x01",
            "I will not participate directly.\x02\x03",
            "However, if something happens\x01",
            "Be sure to contact you too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003F…… I am saved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FThank you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01002F#5POh, then let's go ahead.\x02",
    )

    CloseMessageWindow()
    OP_92(0x8, 0x2DB4, 0x2AF8, 0x1F4)

    def lambda_11896():
        OP_95(0xFE, 11700, 850, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11896)
    WaitChrThread(0x8, 1)
    OP_68(12900, 1750, 9800, 3000)

    def lambda_118C5():
        OP_95(0xFE, 5700, 850, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_118C5)
    WaitChrThread(0x8, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x8, 0x80)
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00005Fby the way……\x01",
            "Keyaは図書館だったか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1198C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1198C)
    Sleep(100)

    def lambda_1199C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1199C)

    def lambda_119A9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_119A9)
    Sleep(50)

    def lambda_119B9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_119B9)

    def lambda_119C6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_119C6)
    WaitChrThread(0x102, 2)

    ChrTalk(
        0x102,
        (
            "#12P#00104FYes, early in the morning\x01",
            "I went out and went.\x02\x03",
            "#00100FIt seems to be back by noon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00002FI see……\x01",
            "Would that be okay with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FOkay.\x01",
            "Even if we also go out!\x02",
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
            "Tio joined the party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "キャンプメニューの[TACTICS]で\x01",
            "You can add it to an attack member.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_37_10DF7 end

    def Function_38_11B65(): pass

    label("Function_38_11B65")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    OP_68(12600, 2450, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x102, 13900, 900, 6650, 270)
    SetChrPos(0x101, 13900, 900, 4600, 270)
    SetChrPos(0x103, 11300, 900, 6650, 90)
    SetChrPos(0x104, 11300, 900, 4600, 90)
    SetChrPos(0x109, 11300, 900, 2550, 90)
    SetChrPos(0x105, 13900, 900, 2550, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x2A, 0x80)
    OP_78(0x13, 0x2A)
    ClearMapObjFlags(0x13, 0x4)
    OP_49()
    SetChrPos(0x2A, 12700, 1650, 4600, 0)
    OP_D5(0x2A, 0x0, 0x15F90, 0x0, 0x0)
    Sleep(500)
    Sound(18, 0, 100, 0)
    UseItem(0x2FC, 0xFF)
    Sleep(500)
    AddItemNumber('幻兽调查报告书', 1)
    PlayBGM("ed7111", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(12600, 1950, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#11P#00003FUrasura and the middle Nakasu\x01",
            "It is a deviation from the East Crossbell Highway ……\x02\x03",
            "#00001FBoth recently,\x01",
            "I did not drop in too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FAs it appeared in the old mine\x01",
            "It looks like he's not deck … …\x02\x03",
            "#00301FPerfect preparation\x01",
            "It seems better to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FAlso …\x01",
            "Is the \"cause\" specific?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PYeah ….\x02\x03",
            "#00101FTime · sky · vision\x01",
            "The top three attributes are working\x01",
            "There seems to be reports.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FRegarding the function of the superordinate attribute\x01",
            "I think that I can perceive it.\x02\x03",
            "#00208FJust become a \"cause\" ……\x01",
            "It might be a bit difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FCertainly for the \"tower\" and \"monastery\"\x01",
            "It seems I do not know the cause … …\x02\x03",
            "#10305FBy the way it is in the battlefield\x01",
            "Is that the same as \"The Fort of the Sun\"?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00006FOh, when we got in\x01",
            "Sure it was, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#5PHowever, after the case is settled\x01",
            "It seems that no abnormality has occurred.\x02\x03",
            "#00108FIt seems like it was in \"monastery\"\x01",
            "\"Bell\" seems not to be the cause … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FThen the cause is really\x01",
            "It seems difficult to identify …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FWell, anyway\x01",
            "Let's go only as I go.\x02\x03",
            "#00300FAnything other work\x01",
            "I wonder if they are coming in.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#11P#00003FThat's right.\x02\x03",
            "#00000FOK, after checking the support request\x01",
            "Shall I leave?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
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
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetChrPos(0x2A, 25600, 1650, 9500, 0)
    SetChrFlags(0x2A, 0x80)
    SetMapObjFlags(0x13, 0x4)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x160, 0)
    OP_29(0xA6, 0x4, 0x2)
    OP_29(0xA6, 0x1, 0x0)
    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    OP_32(0x6, 0x0, 0x43)
    OP_42(0x6, 0x3ED, 0xFF)
    Call(0, 67)
    EventEnd(0x5)
    Return()

    # Function_38_11B65 end

    def Function_39_1226B(): pass

    label("Function_39_1226B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15600, 1750, 9500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x103, 13500, 850, 8500, 45)
    SetChrPos(0x104, 13700, 850, 9900, 90)
    SetChrPos(0x109, 14600, 850, 7400, 45)
    SetChrPos(0x105, 16000, 850, 7600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x2B, 15000, 850, 8900, 0)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    def lambda_1234A():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1234A)
    Sleep(100)

    def lambda_1235A():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1235A)
    Sleep(100)

    def lambda_1236A():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1236A)
    Sleep(100)

    def lambda_1237A():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1237A)
    Sleep(100)

    def lambda_1238A():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1238A)
    Sleep(100)

    def lambda_1239A():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1239A)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00003F#5PAfter all, a wonderful number\x01",
            "It seems that the request has come …\x02\x03",
            "#00008FBecause Arios can not move\x01",
            "I do not think it's … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11P… … Well ….\x02\x03",
            "#00108FToday the section chief visits the hospital\x01",
            "It seems to be going ….\x02\x03",
            "#00101FWe will soon\x01",
            "It seems better to have a face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FRight\x01",
            "She seems to have gone yesterday.\x02\x03",
            "#00308F… … It was quite depressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FYes……\x01",
            "I am a bit worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FIf you use a car you can go to the hospital\x01",
            "It does not cost so much ……\x02\x03",
            "#10100FIf I have time\x01",
            "Let's go for a visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5POh, would you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FBut the recovery procedure of the eye ……\x02\x03",
            "#10301FAs expected after all\x01",
            "It sounds like a difficult area, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5P… … That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PThis surgery also\x01",
            "It will never fail\x01",
            "It does not seem to be ….\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x2B, 22900, 0, 12700, 0)
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x160, 1)
    Call(0, 67)
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    EventEnd(0x5)
    Return()

    # Function_39_1226B end

    def Function_40_12719(): pass

    label("Function_40_12719")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    LoadChrToIndex("apl/ch50090.itc", 0x24)
    LoadChrToIndex("apl/ch50092.itc", 0x25)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis255.itp")
    OP_68(12600, 2550, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x2)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 13900, 900, 5400, 270)
    SetChrPos(0x102, 11300, 900, 7000, 90)
    SetChrPos(0x103, 11300, 900, 3800, 90)
    SetChrPos(0x104, 13900, 900, 3800, 270)
    SetChrPos(0x109, 11300, 900, 2200, 90)
    SetChrPos(0x105, 13900, 900, 2200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 13900, 900, 7000, 270)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 11300, 900, 5400, 90)
    SetChrChipByIndex(0xA, 0x6)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 16300, 850, 6400, 180)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x0, 0x1)
    ClearChrFlags(0x22, 0x80)
    OP_78(0xB, 0x22)
    ClearChrFlags(0x23, 0x80)
    OP_78(0xC, 0x23)
    ClearChrFlags(0x24, 0x80)
    OP_78(0xD, 0x24)
    ClearChrFlags(0x25, 0x80)
    OP_78(0xE, 0x25)
    ClearChrFlags(0x26, 0x80)
    OP_78(0xF, 0x26)
    ClearChrFlags(0x27, 0x80)
    OP_78(0x10, 0x27)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x11, 0x28)
    ClearChrFlags(0x29, 0x80)
    OP_78(0x12, 0x29)
    OP_49()
    SetChrPos(0x22, 14000, 0, 7000, 0)
    OP_D5(0x22, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x23, 14000, 0, 5400, 0)
    OP_D5(0x23, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x24, 14000, 0, 3800, 0)
    OP_D5(0x24, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x25, 14000, 0, 2200, 0)
    OP_D5(0x25, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x26, 11200, 0, 7000, 0)
    OP_D5(0x26, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x27, 11200, 0, 5400, 0)
    OP_D5(0x27, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x28, 11200, 0, 3800, 0)
    OP_D5(0x28, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x29, 11200, 0, 2200, 0)
    OP_D5(0x29, 0x0, 0x15F90, 0x0, 0x0)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 13000, 1450, 7100, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x18)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 13100, 1300, 6700, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 12350, 1450, 7100, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0x18)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 12300, 1300, 6700, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13000, 1450, 5400, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x18)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13100, 1300, 5000, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x24)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12350, 1450, 5400, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0x18)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12300, 1300, 5000, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 13000, 1450, 3800, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x18)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 13100, 1300, 3400, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1450, 2100, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0x18)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13100, 1300, 1700, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x24)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12350, 1450, 2100, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x18)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12300, 1300, 1700, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 12350, 1450, 3800, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x24)
    SetChrSubChip(0x1E, 0x18)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 12300, 1300, 3400, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x25)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 16300, 750, 5500, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrSubChip(0xF, 0xA)
    SetChrSubChip(0x11, 0xA)
    SetChrSubChip(0x13, 0xA)
    SetChrSubChip(0x15, 0xA)
    SetChrSubChip(0x17, 0xA)
    SetChrSubChip(0x19, 0xA)
    SetChrSubChip(0x1B, 0xA)
    SetChrSubChip(0x1D, 0xA)
    OP_68(12600, 2050, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x8,
        (
            "#5P#01006F─ ─ I see.\x01",
            "A flower that became a raw material of an example of?\x02\x03",
            "#01001FThen for the police\x01",
            "I'm getting out of other people's affairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11PYes, continue to work with the guild\x01",
            "I think I will investigate … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FBesides, the matter you care about is\x01",
            "Is something in it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#11P#01003FSpeaking of being contained in it\x01",
            "Well, leave it to another section.\x02\x03",
            "#01000FAnyway, in a national independence referendum\x01",
            "A certain degree of confusion can not be avoided.\x02\x03",
            "Now I am concerned about\x01",
            "The washout should be the first choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106F……indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F#12PWhat is called#4RSo-called#Crisis management is a guy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FBut then …\x01",
            "What shall we do for today's policy?\x02\x03",
            "#00200FWe are also in charge of investigating the eidolon\x01",
            "I have finished within yesterday.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#00302F#11PWell, guild fighters\x01",
            "Maybe Ali may be helping.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x102, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    SetChrSubChip(0x102, 0x2)
    OP_63(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    SetChrSubChip(0x104, 0x2)
    OP_63(0x105, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#00105F……What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305F#12PIs it also anxious?\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00003F#11PNo … but I thought.\x02\x03",
            "#00001FOnce, \"Rosenberg Studio\"\x01",
            "Why do not you visit?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#00101FAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10101FIt is related to \"association\" … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PReally……\x01",
            "I completely forgotten.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_1343F")

    ChrTalk(
        0x101,
        (
            "#00003F#11POf course there is no search warrant,\x01",
            "It can not be forced investigation.\x02\x03",
            "#00001FBut … that old man\x01",
            "I was saying like this before.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "But now, especially speaking\x01",
            "It is not necessarily certain.\x02\x03",
            "When I have something to do\x01",
            "You should visit again.\x02\x03",
            "Let's dispense with Len and listen to it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    VolumeBGM(0x64, 0x3E8)
    Jump("loc_135A9")

    label("loc_1343F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_13517")

    ChrTalk(
        0x101,
        (
            "#00006F#11POf course there is no search warrant,\x01",
            "It can not be forced investigation.\x02\x03",
            "#00001FHowever, as long as I heard a story from Len,\x01",
            "It seems not to be a person who does not understand the story.\x02\x03",
            "At the request of Imelda\x01",
            "We also have acquaintance for a moment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_135A9")

    label("loc_13517")


    ChrTalk(
        0x101,
        (
            "#00006F#11POf course there is no search warrant,\x01",
            "It can not be forced investigation.\x02\x03",
            "#00001FHowever, as long as I heard a story from Len,\x01",
            "It seems not to be a person who does not understand the story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_135A9")


    ChrTalk(
        0x103,
        (
            "#6P#00203F…… Worth a visit\x01",
            "There may be.\x02\x03",
            "#00201FAlthough danger may be involved.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_1369B")

    ChrTalk(
        0x105,
        (
            "#10304F#12PCertainly, that strange boy's\x01",
            "I'd like to grab the purpose as much as possible.\x02\x03",
            "#10302FMaybe at that workshop\x01",
            "It may be staying.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1371F")

    label("loc_1369B")


    ChrTalk(
        0x105,
        (
            "#10304F#12PCertainly, that strange boy's\x01",
            "I'd like to grab the purpose as much as possible.\x02\x03",
            "#10302FMaybe at that workshop\x01",
            "It may be staying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1371F")


    ChrTalk(
        0x109,
        (
            "#6P#10100FWell, I agree!\x02\x03",
            "#10106FEven just a dangerous foreign forces\x01",
            "This emerging situation … …\x02\x03",
            "#10101FNo more dubious forces\x01",
            "I can not leave it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FI see …\x02\x03",
            "#00101FFirst of all,\x01",
            "May I visit you, is not it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(250)

    ChrTalk(
        0x101,
        (
            "#00000F#11POh, let's see the situation.\x02\x03",
            "#00003F…… In some cases, a search warrant\x01",
            "You may need to arrange it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PRight\x02\x03",
            "#00300FAll right, sort of\x01",
            "I will finally get out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01105F#6PHey, everyone.\x02\x03",
            "Are you going out for work already?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00005F#11POh, I'm planning that.\x02\x03",
            "#00000FKeyaは今日は……\x01",
            "Were you going to the library?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01103FOh, for the sake of Shizuku\x01",
            "I wonder if I should look for Braille books.\x02\x03",
            "#01110FAlthough I go shopping and go home\x01",
            "Do you want to eat night Gohan?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#5P#00105FShopping … ….\x01",
            "Keyaちゃん、大丈夫なの？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00205FCertainly many times the dishes\x01",
            "I have been making it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01104FYeah, Momo's dad or something\x01",
            "I always bought it from Oscar.\x02\x03",
            "#01110FDepartment store food corner\x01",
            "Do you agree with my aunt?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012F#11PUntil when … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#11PHaha, well well keeper, I'm convinced.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01004FThen …\x01",
            "It has become somewhat cooler\x01",
            "A pot stick might be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FOh, is not it?\x01",
            "Everyone seems to be excited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PWhat is called a pot\x01",
            "I wonder if the wind is eastern?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00100FKeyaちゃん、大丈夫？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01103FHmm, I think that it will manage somehow.\x02\x03",
            "#01101FI'd like to take a moment\x01",
            "I should also stay in the street stall of east street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#11PHuh, it is authentic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FWhen I came back\x01",
            "You enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#11Pありがとう、Keya。\x02\x03",
            "#00002FToday as possible\x01",
            "I will return so as not to be late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#01109FErr …… Well!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 64000, 200, 11400, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 2880, 0, 1750, 225)
    OP_4C(0xA, 0xFF)
    OP_49()
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
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x103, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrPos(0x22, 22900, 0, 12700, 0)
    SetChrPos(0x23, 22900, 0, 12700, 0)
    SetChrPos(0x24, 22900, 0, 12700, 0)
    SetChrPos(0x25, 22900, 0, 12700, 0)
    SetChrPos(0x26, 22900, 0, 12700, 0)
    SetChrPos(0x27, 22900, 0, 12700, 0)
    SetChrPos(0x28, 22900, 0, 12700, 0)
    SetChrPos(0x29, 22900, 0, 12700, 0)
    SetMapObjFrame(0xFF, "isu00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x1, 0x1)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x162, 0)
    OP_29(0xA6, 0x1, 0x9)
    OP_29(0xA6, 0x4, 0x10)
    OP_29(0xA7, 0x4, 0x2)
    OP_29(0xA7, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_141B4")
    Jump("loc_141B9")

    label("loc_141B4")

    OP_29(0x81, 0x4, 0x40)

    label("loc_141B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_141CA")
    Jump("loc_141CF")

    label("loc_141CA")

    OP_29(0x82, 0x4, 0x40)

    label("loc_141CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_141E0")
    Jump("loc_141E5")

    label("loc_141E0")

    OP_29(0x84, 0x4, 0x40)

    label("loc_141E5")

    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    Call(0, 67)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_40_12719 end

    def Function_41_14202(): pass

    label("Function_41_14202")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15600, 1750, 9500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x103, 13500, 850, 8500, 45)
    SetChrPos(0x104, 13700, 850, 9900, 90)
    SetChrPos(0x109, 14600, 850, 7400, 45)
    SetChrPos(0x105, 16000, 850, 7600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x2B, 15000, 850, 8900, 0)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    def lambda_142E1():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_142E1)
    Sleep(100)

    def lambda_142F1():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_142F1)
    Sleep(100)

    def lambda_14301():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_14301)
    Sleep(100)

    def lambda_14311():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_14311)
    Sleep(100)

    def lambda_14321():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_14321)
    Sleep(100)

    def lambda_14331():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_14331)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x105,
        "#11P#10300FSeveral new things are coming, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00300Fwhat will you do?\x01",
            "先にdoll工房に行ってから\x01",
            "Although it seems good to clean up.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#5PNo, depending on listening\x01",
            "I do not know what will happen.\x02\x03",
            "#00001FHurrying support request is something\x01",
            "You had better clean up in advance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FI agree……\x01",
            "It may be necessary to conduct a compulsory investigation\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#11PThen, if you are ready\x01",
            "山道のdoll工房に行きましょう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203F(Part-time at theme park is\x01",
            "You will be attracted to your asexuality … …)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x2B, 22900, 0, 12700, 0)
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x162, 1)
    Call(0, 67)
    EventEnd(0x5)
    Return()

    # Function_41_14202 end

    def Function_42_1457F(): pass

    label("Function_42_1457F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    LoadChrToIndex("apl/ch50090.itc", 0x24)
    LoadChrToIndex("apl/ch50092.itc", 0x25)
    SoundLoad(128)
    SoundLoad(848)
    OP_68(12600, 2650, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 13900, 900, 5400, 270)
    SetChrPos(0x102, 11300, 900, 7000, 90)
    SetChrPos(0x103, 11300, 900, 3800, 90)
    SetChrPos(0x104, 13900, 900, 3800, 270)
    SetChrPos(0x109, 11300, 900, 2200, 90)
    SetChrPos(0x105, 13900, 900, 2200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 13900, 900, 7000, 270)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 11300, 900, 5400, 90)
    SetChrChipByIndex(0xA, 0x6)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 16300, 850, 6400, 180)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x0, 0x1)
    ClearChrFlags(0x22, 0x80)
    OP_78(0xB, 0x22)
    ClearChrFlags(0x23, 0x80)
    OP_78(0xC, 0x23)
    ClearChrFlags(0x24, 0x80)
    OP_78(0xD, 0x24)
    ClearChrFlags(0x25, 0x80)
    OP_78(0xE, 0x25)
    ClearChrFlags(0x26, 0x80)
    OP_78(0xF, 0x26)
    ClearChrFlags(0x27, 0x80)
    OP_78(0x10, 0x27)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x11, 0x28)
    ClearChrFlags(0x29, 0x80)
    OP_78(0x12, 0x29)
    OP_49()
    SetChrPos(0x22, 14000, 0, 7000, 0)
    OP_D5(0x22, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x23, 14000, 0, 5400, 0)
    OP_D5(0x23, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x24, 14000, 0, 3800, 0)
    OP_D5(0x24, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x25, 14000, 0, 2200, 0)
    OP_D5(0x25, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x26, 11200, 0, 7000, 0)
    OP_D5(0x26, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x27, 11200, 0, 5400, 0)
    OP_D5(0x27, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x28, 11200, 0, 3800, 0)
    OP_D5(0x28, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x29, 11200, 0, 2200, 0)
    OP_D5(0x29, 0x0, 0x15F90, 0x0, 0x0)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 13000, 1450, 7100, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x14)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 13100, 1350, 6800, 0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 12200, 1450, 7100, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0x11)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 12300, 1300, 6800, 0)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13000, 1450, 5200, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x14)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13100, 1350, 4900, 0)
    SetChrChipByIndex(0x15, 0x24)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12200, 1450, 5200, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0x11)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12300, 1300, 4900, 0)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 13000, 1450, 3800, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x14)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 13100, 1350, 3500, 0)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 13000, 1450, 2000, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0x14)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 13100, 1350, 1700, 0)
    SetChrChipByIndex(0x1B, 0x24)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 12200, 1450, 2000, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x11)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 12300, 1300, 1700, 0)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 12200, 1450, 3800, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x24)
    SetChrSubChip(0x1E, 0x11)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 12300, 1300, 3500, 0)
    SetChrChipByIndex(0x1F, 0x25)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 16300, 750, 5500, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrSubChip(0xF, 0x8)
    SetChrSubChip(0x11, 0x8)
    SetChrSubChip(0x13, 0x8)
    SetChrSubChip(0x15, 0x8)
    SetChrSubChip(0x17, 0x8)
    SetChrSubChip(0x19, 0x8)
    SetChrSubChip(0x1B, 0x8)
    SetChrSubChip(0x1D, 0x8)
    Sound(128, 2, 50, 0)
    OP_68(12600, 2150, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#00004F#11P─ ─ Like, Feast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#11PNo, ~ to the cold body\x01",
            "It is nice to cook rice cooking.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(200)

    ChrTalk(
        0x102,
        (
            "#5P#00102FHuh, you are right.\x01",
            "Eggs and poultry were also included.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x1)
    Sleep(100)

    ChrTalk(
        0x109,
        "#12P#10109Fご馳走さま、Keyaちゃん。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(100)

    ChrTalk(
        0x103,
        "#6P#00202FIt was very delicious.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x2)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#6P#01104FWell, yesterday's pot\x01",
            "I just used materials.\x02\x03",
            "#01110FWadi, I got hungry tonight?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x2)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10304F#11P……Ah.\x01",
            "It was a delicious taste.\x02\x03",
            "#10302Fご馳走さま、Keya。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#01109FWell, it was good.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5P#01004FFu … … You are comfortable with your comfort.\x02\x03",
            "#01000FIt's about Waldo Valles … …\x01",
            "The search is continued in the direction of the guard.\x02\x03",
            "You guess so little of it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    SetChrSubChip(0x102, 0x0)
    Sleep(100)
    SetChrSubChip(0x104, 0x2)

    ChrTalk(
        0x105,
        "#10304F#12P…… Ha ha, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#11PBut, Waldo\x01",
            "Somewhere \"Gnostic\"\x01",
            "There is no mistake that I got it.\x02\x03",
            "The route there\x01",
            "I have to unravel anything ……!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01003FAlso about it\x01",
            "It is already the situation that the second department is moving.\x02\x03",
            "Regarding the involvement of foreign forces in department 1\x01",
            "I have heard that it is in the investigation.\x02\x03",
            "#01000FWell, do not be so impatient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11P……Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FAfter all, yesterday's derailment site is\x01",
            "Were you able to recover all the way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01005FOh, by the evening of yesterday\x01",
            "After making it possible to pass one side\x01",
            "It seems that it was fully restored overnight.\x02\x03",
            "#01004FI did not take care of that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FFu … … what more than anything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FThe transcontinental railroad is in the aorta …\x01",
            "If I had stopped\x01",
            "I guess it was confusing now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PMore and more,\x01",
            "To the materials of gorp of empire and republic\x01",
            "It looks a little strange.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00003F#5POh … it's totally.\x02\x03",
            "#00001F…… For now I will ask for assistance\x01",
            "Will you check it?\x02\x03",
            "It's about time for today\x01",
            "It may have arrived.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(150)

    ChrTalk(
        0x102,
        "#6P#00100FWell, let's do that.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sound(848, 2, 100, 0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    OP_70(0xA, 0x0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x14, 0x0, 0x20)
    Sleep(800)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 0x2)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x9, 0x1)
    Sleep(200)

    ChrTalk(
        0x9,
        "#6P#01105FTsunshin, it is ringing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11POh, I'll come out.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 15000, 850, 5700, 270)
    Sound(812, 0, 100, 0)
    OP_0D()
    OP_92(0x101, 0x3714, 0x300C, 0x1F4)
    OP_68(14100, 1850, 12300, 2500)

    def lambda_1532B():
        OP_95(0xFE, 14100, 850, 12300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1532B)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    OP_6F(0x1)
    OP_24(0x350)
    Sound(838, 0, 100, 0)
    ClearMapObjFlags(0xA, 0x20)
    OP_70(0xA, 0x32)
    FadeToDark(500, 0, 100)
    OP_0D()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001FYes, here crossbar police,\x01",
            "It is a mission support section, but …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of a man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……good morning.\x01",
            "Michelle of the guild acceptance.\x02",
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
            "#00005FOh, good morning.\x02\x03",
            "#00001FA report on \"association\"\x01",
            "Did you see it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Michelle")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yeah … …. I was honestly sorry.\x02\x03",
            "Currently, please contact Leiman headquarters\x01",
            "I am analyzing the information ….\x02\x03",
            "Well, because they are incomprehensible people\x01",
            "How far is it really moving?\x01",
            "It may not be understood.\x02",
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
            "#00006F……Is that so.\x02\x03",
            "#00005FEr, to tell about that?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Michelle")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, no.\x01",
            "That's not it.\x02\x03",
            "I'd like to ask you something.\x01",
            "Our lynn and aeolia,\x01",
            "I wonder if I see you …?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 2)), scpexpr(EXPR_END)), "loc_1567E")
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001FUm, yesterday at the hospital\x01",
            "I just met, but ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_156D0")

    label("loc_1567E")

    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FWell, the day before yesterday at the Orkis Tower\x01",
            "It is clear that I have met … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_156D0")

    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Michelle")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I see … That's right.\x02\x03",
            "…… That kids,\x01",
            "I wonder what he is doing.\x02",
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
            "#00013FEr …\x01",
            "Can not you contact me?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Michelle")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes, from yesterday evening\x01",
            "Do not connect to Enigma.\x02\x03",
            "Well, it's not so rare\x01",
            "I do not worry so much.\x02",
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
            "#00003FIs that so……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Michelle")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, do not mind.\x01",
            "You guys are also busy.\x02\x03",
            "Is it a bad leader of the example?\x01",
            "Is not that bad, is not it?\x02",
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
            "#00008F… Well, well.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Michelle")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you see two people\x01",
            "Please tell me to contact you soon.\x02\x03",
            "Well then, please do your best too\x02",
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
            "#00004FYes, I appreciate your work.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(500, 0)
    OP_0D()
    Sound(838, 0, 100, 0)
    SetMapObjFlags(0xA, 0x4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x8,
        (
            "#01000FI'd like to be from the guild,\x01",
            "What happened?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        "#00001F#5POh, yes……\x02",
    )

    CloseMessageWindow()
    OP_68(12920, 1850, 6140, 2000)
    MoveCamera(35, 17, 0, 2000)

    def lambda_15A41():
        OP_96(0xFE, 0x319C, 0x352, 0x20D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15A41)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lost and stolen Lin and Eolia from last night\x01",
            "I informed you that the contact has stopped.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#00101FThat guy ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#12PBoth of considerable skill\x01",
            "You were older sisters, did not they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11POh, especially Eolia\x01",
            "Cecilさんに次ぐ俺のタイプだな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(150)

    ChrTalk(
        0x103,
        "#6P#00211FI do not care about that … …\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15CD5")

    ChrTalk(
        0x109,
        (
            "#12P#10106F#NBut, I am a bit worried.\x02\x03",
            "#10108FBoth of you schedule management\x01",
            "It is quite solidly so.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#5P#00006FThat's right.\x01",
            "Even when we made arrangements before\x01",
            "It was feeling moving in increments.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15D88")

    label("loc_15CD5")


    ChrTalk(
        0x109,
        (
            "#12P#10106F#NBut, I am a bit worried.\x02\x03",
            "#10101FAs a hackman and schedule management\x01",
            "It is quite solidly so.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#5P#00003FThat's right.\x01",
            "Arios seems that way too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D88")


    ChrTalk(
        0x8,
        (
            "#01003F#11Pま、If I can afford, I have a job\x01",
            "Put your face on the guild.\x02\x03",
            "#01002FThese times are mutually exclusive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00000FYes, I understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01105FLloyd's,\x01",
            "Are you going out?\x02\x03",
            "#01102FToday is a pot, is it okay so?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15E6E():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_15E6E)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#5P#00002FOh, today\x01",
            "It will definitely return soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00106Fごめんね、Keyaちゃん。\x02\x03",
            "#00108FHe gave me a lot of preparation\x01",
            "I can not eat yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01121FNo, that's all\x01",
            "You are doing your best, do not you?\x02\x03",
            "#01109FだったらKeyaも\x01",
            "I want to do my best and help you.\x02",
        )
    )

    CloseMessageWindow()
    Sound(822, 0, 100, 0)
    OP_63(0x9, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#00002FKeya……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#11PHa ha …\x01",
            "It's quite a destructive power.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)

    ChrTalk(
        0x103,
        (
            "#6P#00204FIn the weather forecast, in the afternoon\x01",
            "It looks like rain will stop ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#11PTidy job perfectly\x01",
            "I will finally be back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10102F#NYes……!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 64000, 200, 11400, 180)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 117660, 30, 8100, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 119610, 30, 4470, 225)
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
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x103, 0x4)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrPos(0x22, 22900, 0, 12700, 0)
    SetChrPos(0x23, 22900, 0, 12700, 0)
    SetChrPos(0x24, 22900, 0, 12700, 0)
    SetChrPos(0x25, 22900, 0, 12700, 0)
    SetChrPos(0x26, 22900, 0, 12700, 0)
    SetChrPos(0x27, 22900, 0, 12700, 0)
    SetChrPos(0x28, 22900, 0, 12700, 0)
    SetChrPos(0x29, 22900, 0, 12700, 0)
    SetMapObjFrame(0xFF, "isu00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x1, 0x1)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x164, 0)
    OP_29(0xA8, 0x1, 0xB)
    OP_29(0xA8, 0x1, 0xC)
    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    SubItemNumber('沉重货物', 1)
    SubItemNumber('易碎品的小包裹', 1)
    SubItemNumber('发往住宅街的送货单', 1)
    SubItemNumber('小箱子', 1)
    Call(0, 67)
    ReplaceBGM("ed7150", -1)
    ReplaceBGM("ed7101", "ed7562")
    ReplaceBGM("ed7116", "ed7562")
    OP_24(0x350)
    PlayBGM("ed7150", 0)
    EventEnd(0x5)
    Return()

    # Function_42_1457F end

    def Function_43_16393(): pass

    label("Function_43_16393")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    OP_68(12600, 2550, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x1)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 11300, 900, 3800, 90)
    SetChrPos(0x102, 13900, 900, 7000, 270)
    SetChrPos(0x103, 13900, 900, 2200, 270)
    SetChrPos(0x104, 11300, 900, 7000, 90)
    SetChrPos(0x109, 13900, 900, 5400, 270)
    SetChrPos(0x105, 11300, 900, 2200, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 11300, 900, 5400, 90)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 13900, 900, 3800, 270)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 14120, 850, 10500, 180)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x0, 0x1)
    ClearChrFlags(0x22, 0x80)
    OP_78(0xB, 0x22)
    ClearChrFlags(0x23, 0x80)
    OP_78(0xC, 0x23)
    ClearChrFlags(0x24, 0x80)
    OP_78(0xD, 0x24)
    ClearChrFlags(0x25, 0x80)
    OP_78(0xE, 0x25)
    ClearChrFlags(0x26, 0x80)
    OP_78(0xF, 0x26)
    ClearChrFlags(0x27, 0x80)
    OP_78(0x10, 0x27)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x11, 0x28)
    ClearChrFlags(0x29, 0x80)
    OP_78(0x12, 0x29)
    OP_49()
    SetChrPos(0x22, 14000, 0, 7000, 0)
    OP_D5(0x22, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x23, 14000, 0, 5400, 0)
    OP_D5(0x23, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x24, 14000, 0, 3800, 0)
    OP_D5(0x24, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x25, 14000, 0, 2200, 0)
    OP_D5(0x25, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x26, 11200, 0, 7000, 0)
    OP_D5(0x26, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x27, 11200, 0, 5400, 0)
    OP_D5(0x27, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x28, 11200, 0, 3800, 0)
    OP_D5(0x28, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x29, 11200, 0, 2200, 0)
    OP_D5(0x29, 0x0, 0x15F90, 0x0, 0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        "#01003F─ ─ Do you think so?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(12600, 2050, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x109,
        (
            "#10106F#11PYes … … If true, half a year\x01",
            "I intended to study, but …\x02\x03",
            "#10101FThinking a lot - ─\x01",
            "I decided to return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006F……I see………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00106F…… No wonder.\x02\x03",
            "#00108FIn this case the guard also\x01",
            "It only took considerable damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FWell, excellent young men\x01",
            "I want a hand out from his throat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#11PHaha ……\x01",
            "I doubt whether it is excellent or not.\x02\x03",
            "#10108F……Excuse me.\x01",
            "The reconstruction work has fallen to a point\x01",
            "At the bow that I could return to normal business …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FNo … … Do not mind.\x02\x03",
            "#00002FWith the current cross-bell situation\x01",
            "The role of the guard is great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PI will miss you ….\x01",
            "There is no choice but to convince.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01108F#11PNoel …\x01",
            "Are you gone?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x1)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10112F#5PHaha … yeah.\x02\x03",
            "Keyaちゃんに会えなくなるのは\x01",
            "I am very lonely … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01106F#11P……I see………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F#5PBut, any time\x01",
            "I will come to play … ….!\x02\x03",
            "#10100F#30WThat is with Fran …\x02\x01",
            "#10108F#45W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x109)

    ChrTalk(
        0x9,
        "#01112F#11PNoel ぅ ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#11PNoel ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10301F…… My sister, for a while\x01",
            "You do not seem to be able to leave the hospital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#5PYeah … surgery was successful\x01",
            "I also regained consciousness\x01",
            "I do not have any further worries … …\x02\x03",
            "#10113FAfter all the strength is not at all,\x01",
            "It seems I have not returned …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00103F……so………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00308F………………………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10112F#11PHaha … senpai,\x01",
            "Please do not look that way.\x02\x03",
            "#10104FEven that girl is a police officer\x01",
            "I was prepared for the corresponding danger.\x02\x03",
            "#10100FI am responsible for myself … …\x01",
            "Do not you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00304F…… Haha, I understand.\x02\x03",
            "#00302FBut then\x01",
            "Is today's payment for Noel 's work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#11PYes, one day today,\x01",
            "I will try my hardest.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10102F#11PThank you, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00004FOh … this is it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00102FNoel ……\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#01003F── Various procedures\x01",
            "Let me do it by myself.\x02\x03",
            "#01002FAlso, after a long while\x01",
            "Will it be somewhere out?\x02\x03",
            "I specially make it to my ogre.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(100)
    SetChrSubChip(0x9, 0x0)

    ChrTalk(
        0x109,
        "#10105F#11PSergey Manager……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FHaha, is not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11PIt is quite fat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FHuh, then I'm familiar\x01",
            "Are you going to the host club too?\x02\x03",
            "#10302FCollect beautiful places\x01",
            "I prepare a farewell farewell party.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0x109, 0x1)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10111F#5PWhat! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00305FOh, it may be ant.\x02\x03",
            "#00309FAs I am a beautiful older sister\x01",
            "The shop is more nice.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#11P#00111FFuu …\x01",
            "It is not such a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#11PThen, there is a mischievous show\x01",
            "Restaurant in MWL and so on … (Kirari)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)

    ChrTalk(
        0x9,
        "#01105F#5PIs there such a shop?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#01006FBefore that … you …\x01",
            "Think about the contents of my wallet.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10112F#11PHaha ……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00012FTentatively for the time being, by night\x01",
            "I have to finish my work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01203F#5P#NGuru …… Won.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    EndChrThread(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    OP_49()
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
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x103, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrPos(0x22, 22900, 0, 12700, 0)
    SetChrPos(0x23, 22900, 0, 12700, 0)
    SetChrPos(0x24, 22900, 0, 12700, 0)
    SetChrPos(0x25, 22900, 0, 12700, 0)
    SetChrPos(0x26, 22900, 0, 12700, 0)
    SetChrPos(0x27, 22900, 0, 12700, 0)
    SetChrPos(0x28, 22900, 0, 12700, 0)
    SetChrPos(0x29, 22900, 0, 12700, 0)
    SetMapObjFrame(0xFF, "isu00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x1, 0x1)
    SetChrPos(0x0, 12000, 850, 8700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x180, 2)
    Call(0, 67)
    OP_32(0x6, 0x0, 0x49)
    OP_42(0x6, 0x3EF, 0xFF)
    OP_C9(0x0, 0x4)
    OP_C9(0x0, 0x100)
    OP_29(0xAB, 0x1, 0x3)
    OP_29(0xAB, 0x4, 0x10)
    OP_29(0xAC, 0x4, 0x2)
    OP_29(0xAC, 0x1, 0x0)
    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C9(0x0, 0x10000)
    Sleep(1000)
    EventEnd(0x5)
    Return()

    # Function_43_16393 end

    def Function_44_1735F(): pass

    label("Function_44_1735F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(15600, 1750, 9500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x103, 13500, 850, 8500, 45)
    SetChrPos(0x104, 13700, 850, 9900, 90)
    SetChrPos(0x109, 14600, 850, 7400, 45)
    SetChrPos(0x105, 16000, 850, 7600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x2B, 15000, 850, 8900, 0)
    SetCameraDistance(24000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    def lambda_1743E():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1743E)
    Sleep(100)

    def lambda_1744E():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1744E)
    Sleep(100)

    def lambda_1745E():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1745E)
    Sleep(100)

    def lambda_1746E():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1746E)
    Sleep(100)

    def lambda_1747E():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1747E)
    Sleep(100)

    def lambda_1748E():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1748E)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        "#00108F#11PThere are a lot of them indeed …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FBut, what is highly urgent\x01",
            "It looks like he has not come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FThat's right, Abbas's\x01",
            "I feel like I can afford it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FWell, around the various regions\x01",
            "Let's go a step forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FYes!\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#5P── Come on, everyone.\x02\x03",
            "#00002FBecause it is good at work\x01",
            "Will not you go to Ursula Hospital?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)

    def lambda_1768D():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1768D)
    Sleep(50)

    def lambda_1769D():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1769D)
    Sleep(50)

    def lambda_176AD():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_176AD)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x109,
        "#12P#10105FHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#11PWell … I think it's good.\x02\x03",
            "#00104FAbout a week ago, I was too busy\x01",
            "I could not go to see the situation ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FI agree.\x02\x03",
            "#00302FIf Franan woke up\x01",
            "You do not have to visit by all means.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10108FBut,\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FCertainly at the terminal,\x01",
            "I can not hear that bustling voice\x01",
            "It makes me feel lonesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201FYes……\x01",
            "I would like to hear even the voice at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PNoel, do not hold back.\x02\x03",
            "#00000FFor us also Fran\x01",
            "It is an important support role.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_178BE():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_178BE)
    Sleep(50)

    def lambda_178CE():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_178CE)
    Sleep(50)

    def lambda_178DE():
        TurnDirection(0x104, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_178DE)
    Sleep(50)

    def lambda_178EE():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_178EE)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        (
            "#12P#10104Feveryone……\x01",
            "Thank you very much.\x02\x03",
            "#10102FWell then, with a section\x01",
            "Let's go to Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 15000, 850, 8900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x180, 3)
    OP_29(0xAC, 0x1, 0x1)
    Call(0, 67)
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7101", "ed7563")
    ReplaceBGM("ed7116", "ed7563")
    ReplaceBGM("ed7123", "ed7515")
    EventEnd(0x5)
    Return()

    # Function_44_1735F end

    def Function_45_179D0(): pass

    label("Function_45_179D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu05901.itp")
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50091.itc", 0x22)
    SoundLoad(848)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 4900, 130, 6250, 180)
    SetChrPos(0x102, 6050, 130, 6250, 180)
    SetChrPos(0x103, 4600, 130, 2200, 0)
    SetChrPos(0x104, 6400, 130, 2200, 0)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 5500, 130, 2200, 0)
    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -900, 0, 4100, 135)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x8)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 13800, 850, 13000, 0)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x1D)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 4900, 330, 4600, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x22)
    SetChrSubChip(0x10, 0x1D)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 6000, 330, 3900, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    Sleep(1000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30WTwo days later\x02\x03",
            "Ask about the national independence of Crossbell,\x01",
            "The referendum ballot was enforced.\x02\x03",
            "The result will be the same day being voted … ….\x02\x03",
            "A week after that ──\x01",
            "Crossbell celebrated the \"Day of Destiny\".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    Sleep(1000)
    Sound(18, 0, 100, 0)
    UseItem(0x2E9, 0xFF)
    AddItemNumber('克洛斯贝尔时代周刊⑨', 1)
    Sleep(1500)
    Sound(18, 0, 100, 0)
    UseItem(0x2EA, 0xFF)
    AddItemNumber('克洛斯贝尔时代周刊号外', 1)
    OP_68(6020, 3950, 4710, 0)
    MoveCamera(47, 18, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(22800, 0)
    PlayBGM("ed7251", 0)
    Sleep(1500)
    OP_68(6020, 950, 4710, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    SetCameraDistance(22000, 100000)
    MoveCamera(35, 18, 0, 100000)
    Sleep(500)

    ChrTalk(
        0x101,
        "#5P#00013F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F…… That's it,\x01",
            "It was a terrible thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00106FYeah ….\x01",
            "To be honest, unexpected\x01",
            "It's quick to deploy.\x02\x03",
            "#00108F…… Also on my grandfather\x01",
            "I thought about checking it\x01",
            "I can not get in touch from yesterday … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206FThe section chief also went to the headquarters early in the morning,\x01",
            "I do not come back …\x02\x03",
            "#00201FAbout the organization called \"Defense Army\"\x01",
            "Did you go check it out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FAh……\x01",
            "To be honest, it's water to your crib.\x02\x03",
            "#00001FNot just us\x01",
            "The upper part of the police seems to be the same, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FOoooi …\x01",
            "Well it sounds funny.\x02\x03",
            "#00301FFor Noel and Mireille\x01",
            "How are you doing?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#6P#00208FWhat is the current direction of the guard\x01",
            "I can not hear from you.\x02\x03",
            "Perhaps there are too many inquiries\x01",
            "I am blocking information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00103F…… No wonder.\x02\x03",
            "#00101FEven with this asset freeze …\x01",
            "Empire and Republic\x01",
            "It can not be silent.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)

    ChrTalk(
        0x101,
        (
            "#5P#00008F\"I will not quit my ability\" …\x01",
            "I am concerned about the border.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#01108F#30W………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(250)

    ChrTalk(
        0x101,
        (
            "#5P#00002FSorry ….\x01",
            "Have you made me uneasy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#01121F……No.\x01",
            "What is going to happen is that\x01",
            "Keyaにだって分かるし。\x02\x03",
            "#01105FMore than that,\x01",
            "I can not see it from the morning, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00005FOh, remember that … …\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#12P#00205FOh, if you are a wild man\x01",
            "I told you to go out.\x02\x03",
            "#00200FI think that it was after the section manager came out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00001FIs it so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00106FAlready, at this time\x01",
            "I do not admire it a bit.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)

    ChrTalk(
        0x104,
        "#00308FHM……\x02",
    )

    CloseMessageWindow()
    Sound(808, 0, 100, 0)
    Sleep(300)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)
    SetChrSubChip(0x9, 0x1)
    SetChrSubChip(0x103, 0x1)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    SetChrSubChip(0x101, 0x2)
    Sleep(250)
    MoveCamera(35, 18, 0, 2000)
    OP_68(2300, 950, 2300, 2000)
    SetCameraDistance(24000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00105FAt such time …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301FWho……?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 4900, 30, 5500, 180)
    OP_0D()
    OP_93(0x101, 0x10E, 0x1F4)

    def lambda_183D1():
        OP_95(0xFE, 3500, 0, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_183D1)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xE1, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00001F── Yes!\x01",
            "May I ask who's calling! Is it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xB, 1000, -1000, -2000, 0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    OP_4B(0xB, 0xFF)

    NpcTalk(
        0xB,
        "Female voice",
        (
            "#1P#2SWas good……\x01",
            "You seem to have been there.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Female voice",
        "#1P#2S私よ、Cecilだけど。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011FCecil姉！？\x02",
    )

    CloseMessageWindow()

    def lambda_18547():
        OP_95(0xFE, 1000, 0, 2500, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18547)
    WaitChrThread(0x101, 1)

    def lambda_18565():
        OP_95(0xFE, 1000, 0, 1000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18565)
    WaitChrThread(0x101, 1)
    Sound(806, 0, 80, 0)
    Sleep(300)
    Sound(103, 0, 100, 0)

    def lambda_18592():
        OP_96(0xFE, 0x3E8, 0x0, 0xAF0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18592)
    Sleep(500)
    SetChrPos(0xB, 1000, 0, -1500, 0)

    def lambda_185C0():
        OP_96(0xFE, 0x3E8, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_185C0)

    def lambda_185DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_185DA)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x9,
        "#12P#01110Fあ、Cecilだー。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x102, 3, 0, 46)
    Sleep(250)
    OP_68(4500, 1100, 3300, 2000)
    OP_93(0x101, 0x2D, 0x1F4)

    def lambda_18635():
        OP_95(0xFE, 2000, 0, 3800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18635)
    Sleep(500)

    def lambda_18652():
        OP_95(0xFE, 2000, 0, 2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_18652)
    WaitChrThread(0x101, 1)

    def lambda_18670():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18670)
    WaitChrThread(0xB, 1)

    def lambda_18681():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_18681)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#5P#00105FCecilさん……\x01",
            "What did you do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FI do not want you to come here\x01",
            "Is not it rare?\x02",
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
        0xB,
        (
            "I'm sorry.\x01",
            "Suddenly I visited.\x02\x03",
            "That … … Arios or something\x01",
            "You have not come here, do you?\x02",
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
        "#00005F#5P… … Arios?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00205FI have not come … ….\x01",
            "What do you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#05926F……that is………\x02\x03",
            "#05928FLast night, I came to the hospital late at night\x01",
            "I took Shizuku-chan.\x02\x03",
            "Also on-site discharge procedures\x01",
            "Have you done ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#5Peh! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00101Fthat's……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#01112FShizuku ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#05926FSo, what kind of circumstances is it\x01",
            "I came to check it … ….\x02\x03",
            "Guild Michelle also\x01",
            "There seems to be no idea at all.\x02\x03",
            "#05921FSo just to be sure\x01",
            "I tried visiting you also.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#5PIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FThat osan …\x01",
            "Everything like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FBecause it is late at night\x01",
            "I feel it is not normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#01108F………………………………\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    OP_70(0xA, 0x0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x14, 0x0, 0x20)
    Sound(848, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(14100, 1750, 12300, 3000)
    MoveCamera(40, 17, 0, 3000)
    SetCameraDistance(22500, 3000)
    SetChrSubChip(0x9, 0x2)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)

    def lambda_18BC6():
        TurnDirection(0x101, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18BC6)
    Sleep(50)

    def lambda_18BD6():
        TurnDirection(0x102, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_18BD6)
    Sleep(50)

    def lambda_18BE6():
        TurnDirection(0xB, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_18BE6)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xB, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00011FUh ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FWhat is not Enigma\x01",
            "It seems not to be the section chief … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FIs not it Aryos' relationship?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(24000, 5000)
    BeginChrThread(0x101, 3, 0, 47)
    Sleep(800)
    BeginChrThread(0x102, 3, 0, 48)
    Sleep(100)
    BeginChrThread(0x104, 3, 0, 49)
    Sleep(100)
    BeginChrThread(0x103, 3, 0, 50)
    Sleep(500)
    BeginChrThread(0x9, 3, 0, 51)
    Sleep(200)
    BeginChrThread(0xB, 3, 0, 52)
    WaitChrThread(0x101, 3)
    OP_6F(0x79)
    Sleep(300)
    OP_24(0x350)
    Sound(838, 0, 100, 0)
    ClearMapObjFlags(0xA, 0x20)
    OP_70(0xA, 0x32)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#11P#00001FYes, here crossbar police,\x01",
            "Special Affairs Support Division ──\x02",
        )
    )

    WaitChrThread(0xB, 3)
    CloseMessageWindow()
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    NpcTalk(
        0xE,
        "Female voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S#5PWas good!\x01",
            "Lloyd, you were there!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00011FWow\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FCall setting to speaker\x01",
            "なっていたLooks like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FThis voice …… Mr. Grace?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00300FSounds like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FEr …\x01",
            "Mr. Grace, what happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5PWhatever happens … …\x01",
            "I am thinking of teaching you too!\x02\x03",
            "From earlier, from the Orchise Tower\x01",
            "There was a terrible notice!\x02\x03",
            "Apparently the mayor of Dieter\x01",
            "\"Crossbell independent country\" of\x01",
            "It seems that he assumed office as the first President!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#11P#00007FI\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00205FFirst President ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00107FPresident ……\x01",
            "Old uncle! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FOoooi …\x01",
            "What a joke, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5POh, I know\x01",
            "At first I thought it was a joke!\x02\x03",
            "But I guess that's what I was doing\x01",
            "A soldier in a white military uniform ……\x02\x03",
            "Just announced\x01",
            "I called you \"defense army\"! Is it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00013FIs it true? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FWell, that's not a soldier … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5PYeah, maybe the guards\x01",
            "I guess they are members ….\x02\x03",
            "Well, do not be surprised with that …\x02\x03",
            "Immediately after he took office, President Dieter\x01",
            "I have appointed the Secretary of Defense.\x02\x03",
            "It also#350W─\x01",
            "#20WUm, to Arios#20R噵 噵 噵 噵 噵 噵 噵 噵 噵 噵#.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(250)

    ChrTalk(
        0x101,
        "#11P#00005F─ ─.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105F#30W……that's……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00303F#30W~ ~ Wha?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00208F#30WArios, Mr. …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#6P#05925F#30W………………………………\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 3000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xB)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Lloyd's")
    Fade(500)
    SetCameraDistance(24500, 1000)
    OP_82(0x1F4, 0x0, 0xBB8, 0x3E8)

    AnonymousTalk(
        0xFF,
        "#5S#16AEeeeeee! It is! Is it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_6F(0x79)
    CancelBlur(0)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5PJust now\x01",
            "The presidential inauguration speech seems to start!\x02\x03",
            "Because it seems to deliver it even on a power net\x01",
            "Please see if you like!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Voice of a young man",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P#1S…… Grace senior!\x01",
            "Somehow we got permission to interview!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5P#2S\"Alright!\x01",
            "Rain's, I did it!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5P#3SSorry!\x01",
            "I am going to cover the inauguration speech!\x02\x03",
            "see you later~!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(838, 0, 100, 0)
    SetMapObjFlags(0xA, 0x4)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xB)
    Sleep(500)

    ChrTalk(
        0xB,
        "#6P#05928FRight now … … is it true?\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00006FWell, I do not know ……\x02\x03",
            "#00013FThat Arios\x01",
            "\"Secretary of Defense\" … …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00107FWhat is the Secretary?\x01",
            "Top of \"Defense Army\" …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00310FOh, you do not have it …\x01",
            "How is the title of a hushster? Is it?\x02\x03",
            "#00306FDieter's Osan\x01",
            "President is too abrupt … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201F…… Anyway at the terminal\x01",
            "Let's look at the inaugural speech.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007FAh……!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(25000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x350)
    SetScenarioFlags(0x22, 4)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_45_179D0 end

    def Function_46_197E0(): pass

    label("Function_46_197E0")

    Fade(250)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 6050, 30, 5500, 180)
    OP_0D()

    def lambda_19809():
        OP_95(0xFE, 4750, 30, 5500, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_19809)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0xE1, 0x1F4)
    Return()

    # Function_46_197E0 end

    def Function_47_1982A(): pass

    label("Function_47_1982A")

    SetChrPos(0x101, 4100, 850, 10800, 90)

    def lambda_19840():
        OP_96(0xFE, 0x3138, 0x352, 0x2A30, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19840)
    WaitChrThread(0x101, 1)

    def lambda_1985E():
        OP_95(0xFE, 14100, 850, 12300, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1985E)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_47_1982A end

    def Function_48_1987F(): pass

    label("Function_48_1987F")

    SetChrPos(0x102, 4300, 850, 10200, 90)

    def lambda_19895():
        OP_96(0xFE, 0x37DC, 0x352, 0x27D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_19895)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_48_1987F end

    def Function_49_198B6(): pass

    label("Function_49_198B6")

    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 2650, 850, 9600, 90)

    def lambda_198D9():
        OP_96(0xFE, 0x316A, 0x352, 0x2580, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_198D9)
    WaitChrThread(0x104, 1)
    TurnDirection(0x104, 0x101, 500)
    Return()

    # Function_49_198B6 end

    def Function_50_198FA(): pass

    label("Function_50_198FA")

    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 2200, 850, 11000, 90)

    def lambda_1991D():
        OP_96(0xFE, 0x2FA8, 0x352, 0x2AF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1991D)
    WaitChrThread(0x103, 1)
    TurnDirection(0x103, 0x101, 500)
    Return()

    # Function_50_198FA end

    def Function_51_1993E(): pass

    label("Function_51_1993E")

    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 800, 850, 10300, 90)

    def lambda_1995C():
        OP_96(0xFE, 0x2A30, 0x352, 0x283C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1995C)
    WaitChrThread(0x9, 1)
    Return()

    # Function_51_1993E end

    def Function_52_19976(): pass

    label("Function_52_19976")

    SetChrPos(0xB, 800, 850, 11500, 90)

    def lambda_1998C():
        OP_96(0xFE, 0x2A30, 0x352, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1998C)
    WaitChrThread(0xB, 1)
    Return()

    # Function_52_19976 end

    def Function_53_199A6(): pass

    label("Function_53_199A6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    LoadChrToIndex("chr/ch08201.itc", 0x1F)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(15900, 2250, 9800, 0)
    MoveCamera(13, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x103, 16300, 850, 10200, 45)
    SetChrPos(0x101, 15150, 870, 8450, 45)
    SetChrPos(0x102, 16200, 850, 7400, 0)
    SetChrPos(0x104, 17200, 850, 7800, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 14500, 850, 10500, 90)
    OP_4B(0xB, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 13900, 850, 9700, 90)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    PlayBGM("ed7561", 0)
    OP_68(15900, 1750, 9800, 3000)
    FadeToBright(2000, 0)
    Sleep(2500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xB)
    OP_64(0x9)
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#00008F………………………………\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_19B8E():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_19B8E)
    Sleep(50)

    def lambda_19B9E():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_19B9E)
    Sleep(50)

    def lambda_19BAE():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_19BAE)
    Sleep(50)

    def lambda_19BBE():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_19BBE)
    Sleep(50)

    def lambda_19BCE():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_19BCE)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x101, 2)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00007FYes, it is Lloyd …!\x02",
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
            "…… Oh, it's me.\x02",
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
            "#00010FManager!\x01",
            "The current inauguration address is ──\x02",
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
            "…… Of course, I was watching.\x02\x03",
            "Well, anyway, anyway,\x01",
            "The guard as \"defense army\"\x01",
            "It seems that it was completely reorganized.\x02\x03",
            "We also police, as part of it\x01",
            "It is decided to be incorporated.\x02",
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
            "#00006FSounds like that … ….\x02\x03",
            "#00013FPossibly\x01",
            "Sonya Command ……\x02",
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
            "Did you see it in the movie?\x01",
            "Well … I guess you agreed.\x02\x03",
            "I do not know what will happen ….\x01",
            "Now for the Orkis Tower\x01",
            "Keep away from me.\x02\x03",
            "Defense forces 'soldiers'\x01",
            "It should be strictly guarded.\x02",
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
            "#00010FCome … OK.\x02",
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
            "── I will contact you again.\x01",
            "You are not going ahead, am I?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 70, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#12P#00108F… … What is the section chief?\x02",
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
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#5P#00006FOh, the defense army … …\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I explained the stories I heard from Sergei to Eli.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#12P#00106Fso……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PCow, Sonja command\x01",
            "Have you turned to the other side … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00206FWell, from the standpoint\x01",
            "Wondering if it can not be helped …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05923F#5P…… Arios.\x01",
            "I took Shizuku-chan\x01",
            "This was the cause.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1A18C():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A18C)
    Sleep(50)

    def lambda_1A19C():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1A19C)
    Sleep(50)

    def lambda_1A1AC():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1A1AC)
    Sleep(50)

    def lambda_1A1BC():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1A1BC)
    Sleep(50)

    def lambda_1A1CC():
        TurnDirection(0x9, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1A1CC)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0x101,
        "#12P#00005FAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FI agree……\x01",
            "If it got into such a position\x01",
            "It also affects Shizuoka … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PPossibility to be targeted by opponents\x01",
            "Maybe it will come out …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00208F…… In this situation\x01",
            "I wonder if it can not be said that there is nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01108F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FKeya……大丈夫だ。\x02\x03",
            "#00000FDo not risk danger to Shizuoka\x01",
            "Arios is supposed to be thinking as well.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A379():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1A379)
    Sleep(50)
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(200)

    ChrTalk(
        0x9,
        (
            "#01121F#5PYes, that's right.\x02\x03",
            "#01122F…… Hehe.\x01",
            "I am a bit worried ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5P#05921FKeyaちゃん……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00008F……Cecil姉、悪いんだけど\x01",
            "Can I ask a little an answering machine?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1A4C6():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1A4C6)
    Sleep(50)

    def lambda_1A4D6():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1A4D6)
    Sleep(50)

    def lambda_1A4E6():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1A4E6)
    Sleep(50)

    def lambda_1A4F6():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1A4F6)
    Sleep(50)
    WaitChrThread(0xB, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x9,
        "#01105F#5PLloyd …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05925F#5PYeah, until evening\x01",
            "I think it's okay ….\x02\x03",
            "#05921FAre you going out somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FAh\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00001FHey, everyone.\x02\x03",
            "Tentatively …\x01",
            "ギルドをWhy do not you visit?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#12P#00101FThat's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00201FCertainly Mr. Arios's case\x01",
            "I would like to ask the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12PRight\x01",
            "It's truly an awful sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05923F#5P……I got it.\x01",
            "Keyaちゃんと一緒に\x01",
            "I am keeping an answering machine here.\x02\x03",
            "#05920FIt looks like a difficult situation ….\x01",
            "Be careful again.\x02\x03",
            "Do not be unreasonable.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A77B():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A77B)
    Sleep(50)

    def lambda_1A78B():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1A78B)
    Sleep(50)

    def lambda_1A79B():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1A79B)
    Sleep(50)

    def lambda_1A7AB():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1A7AB)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x101,
        "#12P#00002FOh, I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#12PCecilさん、感謝ッス！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00104FWell then, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00202FKeya、Cecilさんと一緒に\x01",
            "Please stay home with a nice girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01112F#5PAh……\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_68(12900, 1750, 9800, 3000)

    def lambda_1A8B4():

        label("loc_1A8B4")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1A8B4")

    QueueWorkItem2(0xB, 2, lambda_1A8B4)

    def lambda_1A8C6():

        label("loc_1A8C6")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1A8C6")

    QueueWorkItem2(0x9, 2, lambda_1A8C6)
    BeginChrThread(0x101, 3, 0, 54)
    Sleep(200)
    BeginChrThread(0x102, 3, 0, 54)
    Sleep(350)
    BeginChrThread(0x103, 3, 0, 54)
    Sleep(400)
    BeginChrThread(0x104, 3, 0, 54)
    EndChrThread(0xB, 0x2)
    EndChrThread(0x9, 0x2)
    OP_6F(0x79)
    Fade(500)
    OP_68(14150, 1750, 10040, 0)
    MoveCamera(47, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21210, 0)
    SetChrPos(0xB, 14500, 850, 10700, 270)
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        "#11P#01101F………………………….\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1A99B():

        label("loc_1A99B")

        TurnDirection(0xB, 0x9, 500)
        Yield()
        Jump("loc_1A99B")

    QueueWorkItem2(0xB, 2, lambda_1A99B)

    ChrTalk(
        0xB,
        "#05925F#5PKeyaちゃん？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    SetCameraDistance(24500, 2000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)

    def lambda_1A9E4():
        OP_95(0xFE, 900, 850, 9700, 5500, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1A9E4)
    Sleep(200)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x9, 0xFF)
    EndChrThread(0xB, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x238), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x323)
    SetScenarioFlags(0x182, 1)
    SetScenarioFlags(0x23, 5)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_53_199A6 end

    def Function_54_1AA4A(): pass

    label("Function_54_1AA4A")

    OP_95(0xFE, 15150, 850, 8450, 4500, 0x1)
    OP_95(0xFE, 10150, 850, 8950, 4500, 0x1)
    OP_95(0xFE, 5150, 850, 9450, 4500, 0x1)
    OP_95(0xFE, 150, 850, 9450, 4500, 0x1)
    Return()

    # Function_54_1AA4A end

    def Function_55_1AA9B(): pass

    label("Function_55_1AA9B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1000, 1000, 5300, 0)
    MoveCamera(51, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 300, -1000, -1600, 0)
    SetChrPos(0x102, 1400, 0, -1900, 0)
    SetChrPos(0x103, 300, 0, -3000, 0)
    SetChrPos(0x104, 1400, 0, -3300, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x2B, 800, 0, 2000, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 2300, 0, 5300, 270)
    SetChrChipByIndex(0xB, 0x7)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetCameraDistance(22500, 5000)
    FadeToBright(2000, 0)

    def lambda_1AB96():
        OP_95(0xFE, -300, 0, 5300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1AB96)
    WaitChrThread(0xB, 1)
    Sleep(500)
    OP_93(0xB, 0x5A, 0x1F4)

    def lambda_1ABBE():
        OP_95(0xFE, 2300, 0, 5300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1ABBE)
    WaitChrThread(0xB, 1)
    Sleep(500)
    OP_93(0xB, 0x10E, 0x1F4)

    def lambda_1ABE6():
        OP_95(0xFE, 1000, 0, 5300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1ABE6)
    WaitChrThread(0xB, 1)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    NpcTalk(
        0x101,
        "Voice of Lloyd",
        "#1PCecil姉！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_68(1000, 1000, 4100, 1500)
    SetChrPos(0x101, 300, 0, -1600, 0)
    BeginChrThread(0x101, 3, 0, 56)

    def lambda_1AC84():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1AC84)
    Sleep(250)

    def lambda_1AC98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1AC98)
    Sleep(350)

    def lambda_1ACAC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1ACAC)
    Sleep(450)

    def lambda_1ACC0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1ACC0)
    OP_93(0xB, 0xB4, 0x1F4)

    ChrTalk(
        0xB,
        "#05921F#5PLloyd …!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#12P#00007Fそれで、Keyaは！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FTo Arios\x01",
            "I heard he was taken away ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05926F#5PYes, I put on that white uniform\x01",
            "Arios came alone … …\x02\x03",
            "#05921FI say \"I came to pick you up\"\x01",
            "Keyaちゃんも頷いて……\x02",
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
    Sleep(850)

    ChrTalk(
        0x101,
        "#12P#00011FHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FSo, Kiyoshi\x01",
            "Were you attached to me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05923F#5PYeah … that seemed to me.\x02\x03",
            "#05921FBut to you\x01",
            "Because it was strange to say without permission\x01",
            "I tried to stop it ….\x02\x03",
            "#05926F\"Because it's okay\"\x01",
            "Keyaちゃんに言われて……\x02\x03",
            "それで警戒してたZeit君も\x01",
            "I became matured … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0x103, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#12P#00208Fby the way……\x01",
            "Zeitがどこにもいません。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05926F#5PSince two people are gone\x01",
            "I went out with Flari.\x02\x03",
            "#05928FPerhaps two people\x01",
            "Maybe he chased me ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    def lambda_1B095():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B095)
    Sleep(100)

    def lambda_1B0A5():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1B0A5)
    Sleep(100)

    def lambda_1B0B5():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1B0B5)
    Sleep(100)

    def lambda_1B0C5():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1B0C5)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    Sleep(150)

    ChrTalk(
        0x101,
        "#5P#00008F……What does it mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FAbout Shizuku-chan\x01",
            "I wonder if it was also a promise …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05923F#5PI thought so, though\x01",
            "It seems that it is not so … …\x02\x03",
            "#05921FThings like going to Michelin\x01",
            "Arios said that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1B21A():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B21A)
    Sleep(50)

    def lambda_1B22A():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1B22A)
    Sleep(50)

    def lambda_1B23A():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1B23A)
    Sleep(50)

    def lambda_1B24A():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1B24A)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#12P#00005FMichelam … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05923F#5PYeah, boat preparation\x01",
            "It is done ……\x02\x03",
            "#05921FIn Michelam\x01",
            "You mean that you go?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#00103F…… In the past few days, toward Michelin\x01",
            "It should be totally suspended.\x02\x03",
            "#00101FTake the trouble … ….?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#00310FChit\x01",
            "As expected, it is not normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00201FLet's chase, Mr. Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003FAh……\x01",
            "Let's procure a boat somehow.\x02\x03",
            "#00007FCecil姉、ゴメン！\x01",
            "Anyway I will chase after that.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B435():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1B435)
    Sleep(50)

    def lambda_1B445():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1B445)
    Sleep(50)

    def lambda_1B455():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1B455)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0xB,
        (
            "#05923F#5PYeah, be careful.\x02\x03",
            "#05928F……アリオスさんもKeyaちゃんも\x01",
            "I had serious eyes at any time.\x02\x03",
            "#05921FPerhaps, I think there is a lot of circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00013FI understood……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107FAnyway catch up\x01",
            "I have to ask about that situation …!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    SetScenarioFlags(0x22, 2)
    NewScene("e4500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_55_1AA9B end

    def Function_56_1B580(): pass

    label("Function_56_1B580")


    def lambda_1B585():
        OP_97(0x101, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B585)
    Sleep(200)

    def lambda_1B5A2():
        OP_97(0x102, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1B5A2)
    Sleep(200)

    def lambda_1B5BF():
        OP_97(0x103, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1B5BF)
    Sleep(200)

    def lambda_1B5DC():
        OP_97(0x104, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1B5DC)
    Return()

    # Function_56_1B580 end

    def Function_57_1B5F2(): pass

    label("Function_57_1B5F2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51218.itc", 0x1E)
    OP_24(0x101E)
    OP_24(0x101F)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis287.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis288.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis289.itp")
    ClearMapFlags(0x10000000)
    OP_68(1000, 1000, 0, 0)
    MoveCamera(55, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27000, 0)
    SetChrPos(0x101, 300, 0, -1600, 0)
    SetChrPos(0x102, 1400, 0, -1900, 0)
    SetChrPos(0x103, 300, 0, -2900, 0)
    SetChrPos(0x104, 1400, 0, -3200, 0)
    SetChrPos(0xF4, 300, 0, -4200, 0)
    SetChrPos(0xF5, 1400, 0, -4500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    StopBGM(0x1388)
    OP_68(1000, 1000, 2000, 3500)
    BeginChrThread(0x101, 3, 0, 58)
    FadeToBright(1000, 0)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_1B7B0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B7B0)
    Sleep(400)

    def lambda_1B7C4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1B7C4)
    Sleep(600)

    def lambda_1B7D8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1B7D8)
    Sleep(400)

    def lambda_1B7EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1B7EC)
    Sleep(600)

    def lambda_1B800():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_1B800)
    Sleep(400)

    def lambda_1B814():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_1B814)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_1B82A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B82A)
    WaitChrThread(0x102, 1)

    def lambda_1B83B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1B83B)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 1)

    def lambda_1B854():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_1B854)
    WaitChrThread(0xF5, 1)

    def lambda_1B865():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_1B865)
    OP_6F(0x79)
    OP_68(2640, 1300, 3150, 2000)
    MoveCamera(55, 15, 0, 2000)
    SetCameraDistance(29000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#6P#00001F#30W…… Special Support Section ………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108F#30WI came back … Wow.\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)
    VolumeBGM(0x46, 0x64)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(110, 50, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#4126V#25A#30WOh, I came back!\x02\x03",
            "#4127V#4S#30A#30WWelcome back~!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    BeginChrThread(0x101, 3, 0, 62)
    SetMessageWindowPos(170, 25, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#4S#20AI'll be back!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(500)
    SetMessageWindowPos(180, 20, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#20A#30W── Okay.\x01",
            "Let's start a pot.\x02\x03",
            "#20A#30WKeyaが準備してくれたから\x01",
            "Meat, fish, vegetables ─ ─ Tuppery.\x02\x03",
            "#20A#30WEat lots, rest early … …\x01",
            "Let's prepare for tomorrow!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(800)
    BeginChrThread(0x101, 3, 0, 62)
    SetMessageWindowPos(145, 110, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#4S#20ALet us eat\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    FadeToDark(0, 16777215, -1)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x5DC, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    FadeToBright(1000, 16777215)
    VolumeBGM(0x64, 0x7D0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#00008F#30W………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00304F#30W…… Ha ha.\x01",
            "Somehow I am too old.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00208FYes……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BC77")

    ChrTalk(
        0x109,
        (
            "#12P#10106FIt's only about a month\x01",
            "I did not go through … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC77")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BCB5")

    ChrTalk(
        0x105,
        (
            "#12P#10404FGiggle\x01",
            "It is truly emotional.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BCB5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BD42")

    ChrTalk(
        0x106,
        (
            "#12P#10708FBut than I thought\x01",
            "It has not been devastated …\x02\x03",
            "#10710FClearly the search of the Defense Forces\x01",
            "I thought that it was in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDB9")

    label("loc_1BD42")


    ChrTalk(
        0x102,
        (
            "#5P#00104FBut than I thought\x01",
            "I have not been devastated …\x02\x03",
            "#00100FClearly the search of the Defense Forces\x01",
            "入っているかとI thought.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BEE4")

    ChrTalk(
        0x10A,
        (
            "#12P#00606FApparently that girl#6RKey#To\x01",
            "It seems that there is consideration.\x02\x03",
            "#00602FFor the president side\x01",
            "She is too important.\x02\x03",
            "Damn the place you cherished\x01",
            "I do not want to hurt the mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000F……I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00204FSomething is blatantly … …\x01",
            "I am glad that it has not changed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C005")

    label("loc_1BEE4")


    ChrTalk(
        0x101,
        (
            "#6P#00004Fひょっとして、Keyaへの\x01",
            "There may be consideration.\x02\x03",
            "#00000FFor the president side\x01",
            "That girl is too important.\x02\x03",
            "Damn the place you cherished\x01",
            "I do not want to hurt the mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00305F…… I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00204FSomething is blatantly … …\x01",
            "I am glad that it has not changed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C005")

    Sound(953, 0, 100, 0)
    Sleep(300)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    OP_90(0xC, 1500, 3000, 15000, 180)

    def lambda_1C033():
        OP_96(0xFE, 0x5DC, 0x0, 0x1838, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1C033)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1C0C2():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C0C2)
    Sleep(50)

    def lambda_1C0D2():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1C0D2)
    Sleep(50)

    def lambda_1C0E2():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1C0E2)
    Sleep(50)

    def lambda_1C0F2():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1C0F2)
    Sleep(50)

    def lambda_1C102():
        TurnDirection(0xF4, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1C102)
    Sleep(50)

    def lambda_1C112():
        TurnDirection(0xF5, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1C112)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Fade(500)
    OP_68(1000, 1750, 9000, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    OP_68(1000, 900, 5000, 3000)
    SetCameraDistance(23000, 3000)
    OP_0D()
    WaitChrThread(0xC, 1)
    OP_4B(0xC, 0xFF)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#12P#00005FCoppe……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102Fso……\x01",
            "You remained safe.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 3, 0, 61)

    def lambda_1C1DE():
        OP_97(0x101, 0x0, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C1DE)
    Sleep(100)

    def lambda_1C1FB():
        OP_97(0x102, 0x0, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1C1FB)
    Sleep(100)

    def lambda_1C218():
        OP_97(0x104, 0x0, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1C218)
    Sleep(100)

    def lambda_1C235():
        OP_97(0xF4, 0xFFFFFDA8, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1C235)
    Sleep(100)

    def lambda_1C252():
        OP_97(0xF5, 0xFFFFFDA8, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1C252)
    WaitChrThread(0x104, 0)

    def lambda_1C270():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1C270)
    WaitChrThread(0xF5, 0)
    WaitChrThread(0x103, 3)

    ChrTalk(
        0xC,
        "#11PNice to meet you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PNya, Nyan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F… … That's right, cheers for good work.\x02\x03",
            "#00202Fyeah yeah……\x01",
            "I was just a little away.\x02\x03",
            "#00204FIn addition … … I'm surely coming back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FWhat are you talking about?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#00206F#5PApparently, from that all the way\x01",
            "It seems I lived here …\x02\x03",
            "#00202FWe also say \"living together\"\x01",
            "It seems that it came to mind once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FHaha, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHaha, for cats\x01",
            "It is unusual as a rule.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C4AD")

    ChrTalk(
        0x109,
        (
            "#12P#10102FBecause it's no problem\x01",
            "Cat foodの用意を\x01",
            "Shall I do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C52A")

    label("loc_1C4AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C4F8")

    ChrTalk(
        0x105,
        (
            "#12P#10402FBecause it's no problem\x01",
            "Should I prepare for food?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C52A")

    label("loc_1C4F8")


    ChrTalk(
        0x104,
        (
            "#00304FBecause it's no problem\x01",
            "Will you also prepare for food?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C52A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(122400, 700, 6000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0xC, 122700, 0, 6000, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 121800, 0, 6000, 0)
    OP_4C(0xC, 0xFF)
    SetCameraDistance(21000, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x4)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, 10790, 850, 12360, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A5, 4)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    EventEnd(0x5)
    Return()

    # Function_57_1B5F2 end

    def Function_58_1C605(): pass

    label("Function_58_1C605")


    def lambda_1C60A():
        OP_98(0xFE, 0x0, 0x0, 0x1324, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C60A)
    Sleep(200)

    def lambda_1C627():
        OP_98(0xFE, 0x0, 0x0, 0x1324, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C627)
    Sleep(200)
    BeginChrThread(0x103, 0, 0, 59)
    Sleep(200)
    BeginChrThread(0x104, 0, 0, 60)
    Sleep(200)

    def lambda_1C656():
        OP_98(0xFE, 0x0, 0x0, 0x13EC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1C656)
    Sleep(200)

    def lambda_1C673():
        OP_98(0xFE, 0x0, 0x0, 0x13EC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1C673)
    Return()

    # Function_58_1C605 end

    def Function_59_1C689(): pass

    label("Function_59_1C689")


    def lambda_1C68E():
        OP_98(0xFE, 0x0, 0x0, 0x1194, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C68E)
    WaitChrThread(0x103, 1)

    def lambda_1C6AC():
        OP_97(0xFE, 0x1F4, 0x0, 0x1F4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C6AC)
    WaitChrThread(0x103, 1)
    Return()

    # Function_59_1C689 end

    def Function_60_1C6C6(): pass

    label("Function_60_1C6C6")


    def lambda_1C6CB():
        OP_98(0xFE, 0x0, 0x0, 0x1194, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C6CB)
    WaitChrThread(0x104, 1)

    def lambda_1C6E9():
        OP_97(0xFE, 0x1F4, 0x0, 0x1F4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C6E9)
    WaitChrThread(0x104, 1)
    Return()

    # Function_60_1C6C6 end

    def Function_61_1C703(): pass

    label("Function_61_1C703")

    Sleep(200)

    def lambda_1C70B():
        OP_95(0xFE, -400, 0, 4100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C70B)
    WaitChrThread(0x103, 1)

    def lambda_1C729():
        OP_95(0xFE, 300, 0, 6100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C729)
    WaitChrThread(0x103, 1)
    TurnDirection(0x103, 0xC, 500)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    TurnDirection(0xC, 0x103, 500)
    Return()

    # Function_61_1C703 end

    def Function_62_1C765(): pass

    label("Function_62_1C765")

    OP_CB(0x0, 0x0, 0x4B0, 0xFFFFFBB4, 0x1, 0x0)
    OP_CB(0x1, 0x0, 0x4B0, 0xFFFFFBB4, 0x1, 0x0)
    OP_CB(0x2, 0x0, 0x4B0, 0xFFFFFBB4, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x0, 0x0, 0xFFFFFAEC, 0x4B0, 0x1, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFFAEC, 0x4B0, 0x1, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFFAEC, 0x4B0, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x0, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x0, 0x0, 0x640, 0xFFFFFB50, 0x1, 0x0)
    OP_CB(0x1, 0x0, 0x640, 0xFFFFFB50, 0x1, 0x0)
    OP_CB(0x2, 0x0, 0x640, 0xFFFFFB50, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1, 0x0)
    OP_CC(0x0, 0xFF, 0x0)
    Return()

    # Function_62_1C765 end

    def Function_63_1C893(): pass

    label("Function_63_1C893")

    EventBegin(0x0)
    Fade(500)
    OP_68(64879, 1330, 10230, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24880, 0)
    SetChrPos(0x101, 65030, 30, 11420, 225)
    SetChrPos(0x102, 66810, 30, 10890, 270)
    SetChrPos(0x103, 66810, 30, 9740, 270)
    SetChrPos(0x104, 63390, 0, 8370, 0)
    SetChrPos(0x109, 65019, 0, 8370, 0)
    SetChrPos(0x105, 66270, 0, 8280, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FSergey Managerの昔の渾名は\x01",
            "\"搦#2RFrom#It was Sergei of Me\x01",
            "It seems to be ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100Fとすると、課長のChairが\x01",
            "『搦め手の指揮官が座するChair』に\x01",
            "That sounds true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FWould you like to investigate around … ….\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_64(0x101)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F… … under the desk of the section chief\x01",
            "It looks like you have something in it.\x02\x03",
            "#00000FLet's pull it out for a moment.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(63630, 1330, 6190, 0)
    MoveCamera(43, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24880, 0)
    ClearMapObjFlags(0x14, 0x4)
    SetChrPos(0x101, 64060, 30, 5280, 0)
    SetChrPos(0x102, 62990, 30, 5080, 0)
    SetChrPos(0x103, 65190, 30, 5080, 0)
    SetChrPos(0x104, 64060, 30, 4000, 0)
    SetChrPos(0x109, 62990, 30, 4000, 0)
    SetChrPos(0x105, 65190, 30, 4000, 0)
    LoadChrToIndex("apl/ch51099.itc", 0x1E)
    SetChrChipByIndex(0x2C, 0x1E)
    SetChrSubChip(0x2C, 0xC)
    SetChrPos(0x2C, 64040, 150, 7160, 0)
    OP_52(0x2C, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x2)
    SetChrFlags(0x2C, 0x10)
    SetChrFlags(0x2C, 0x20)
    OP_A7(0x2C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis348.itp")
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#12P#00305FThis guy……\x01",
            "Maybe a trunk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FAt the \"auctioneer\" in the example\x01",
            "Keyaが入れられていた物にも\x01",
            "It looks similar.\x02\x03",
            "#10304FHuff, in the first place\x01",
            "To choose here\x01",
            "Where the provocation is also good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FYes, certainly.\x01",
            "It seems that he grabbed the manager's full name … …\x02\x03",
            "#00000FAnyway, let's check it.\x02",
        )
    )

    CloseMessageWindow()
    Sound(1024, 0, 100, 0)
    OP_74(0x14, 0x1E)
    OP_71(0x14, 0x1, 0x14, 0x1, 0x8)
    OP_A7(0x2C, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_79(0x14)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "On the back of the trunk\x01",
            "There was a card attached.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The second cage is outside the city.\x01",
            "\"A villager at the old road\x01",
            "Search for a place to inherit \".\x07\x00\x02",
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
        0x103,
        (
            "#00200FMade by Rosenberg\x01",
            "Antique doll ……\x01",
            "I do not think he will make a mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FYeah, I have seen something.\x02\x03",
            "#00104FBell calls me \"Canaan\" by name\x01",
            "可愛がっていたdollだったと思う。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100Fふふ、dollに名前をつけるなんて\x01",
            "Mariavel also has pretty places.\x02\x03",
            "#10106FBother to steal\x01",
            "I do not think I'm in this trunk\x01",
            "It is a bit surprising but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FKaito B ……\x01",
            "Courtesy for art works\x01",
            "It might be that it is being done properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FThat and the second card …\x01",
            "Is the place \"out of town\"?\x02\x03",
            "#10306FWhew.\x01",
            "The search range has expanded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FAnd it seems important,\x01",
            "\"Old way\" and \"Murano is inherited\".\x02\x03",
            "#00103FBoth are words that make history feel,\x01",
            "In the modern city Crossbell\x01",
            "Speaking of such a place ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FAnyway, collect the guys\x01",
            "Let's go looking for the next one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FOh, let's do that.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#16Iローゼンベルクdoll・Ｃ\x07\x00",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('罗赞贝尔克人偶·Ｃ', 1)
    SetMapObjFlags(0x14, 0x4)
    SetChrFlags(0x2C, 0x80)
    OP_D7(0x1E)
    SetChrPos(0x0, 64050, 30, 5290, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_29(0x7A, 0x1, 0x2)
    SetScenarioFlags(0x157, 1)
    OP_65(0x4, 0x1)
    EventEnd(0x5)
    Return()

    # Function_63_1C893 end

    def Function_64_1D22A(): pass

    label("Function_64_1D22A")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FFirst let's confirm the support request.\x01",
            "It is from then on to act.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    EventEnd(0x4)
    Return()

    # Function_64_1D22A end

    def Function_65_1D285(): pass

    label("Function_65_1D285")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FFirst let's confirm the support request.\x01",
            "It is from then on to act.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 11000, 850, 11350, 180)
    EventEnd(0x4)
    Return()

    # Function_65_1D285 end

    def Function_66_1D2E0(): pass

    label("Function_66_1D2E0")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FFirst let's confirm the support request.\x01",
            "It is from then on to act.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 17000, 850, 4000, 270)
    EventEnd(0x4)
    Return()

    # Function_66_1D2E0 end

    def Function_67_1D33B(): pass

    label("Function_67_1D33B")

    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D367")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1D367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D384")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1D384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D3A1")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1D3A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D3BE")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1D3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D3DB")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1D3DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D3F8")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1D3F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D415")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1D415")

    Return()

    # Function_67_1D33B end

    SaveToFile()

Try(main)
