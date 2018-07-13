from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Chief Sergei",           # 1
        "KeA",                    # 2
        "Zeit",                   # 3
        "Cecil",                  # 4
        "Koppe",                  # 5
        "キャットフード",         # 6
        "Grace's Voice",          # 7
        "食器",                   # 8
        "食器",                   # 9
        "食器",                   # 10
        "食器",                   # 11
        "食器",                   # 12
        "食器",                   # 13
        "食器",                   # 14
        "食器",                   # 15
        "食器",                   # 16
        "食器",                   # 17
        "食器",                   # 18
        "食器",                   # 19
        "食器",                   # 20
        "食器",                   # 21
        "食器",                   # 22
        "食器",                   # 23
        "食器",                   # 24
        "食器",                   # 25
        "食器",                   # 26
        "椅子",                   # 27
        "椅子",                   # 28
        "椅子",                   # 29
        "椅子",                   # 30
        "椅子",                   # 31
        "椅子",                   # 32
        "椅子",                   # 33
        "椅子",                   # 34
        "幻獣調査レポート",       # 35
        "Dummy",                  # 36
        "Doll",                   # 37
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
        "Function_6_2983",         # 06, 6
        "Function_7_34C0",         # 07, 7
        "Function_8_4048",         # 08, 8
        "Function_9_41C0",         # 09, 9
        "Function_10_4401",        # 0A, 10
        "Function_11_48B9",        # 0B, 11
        "Function_12_4903",        # 0C, 12
        "Function_13_494F",        # 0D, 13
        "Function_14_4A21",        # 0E, 14
        "Function_15_4AF3",        # 0F, 15
        "Function_16_4B62",        # 10, 16
        "Function_17_4E4F",        # 11, 17
        "Function_18_5161",        # 12, 18
        "Function_19_5CDA",        # 13, 19
        "Function_20_606B",        # 14, 20
        "Function_21_61F8",        # 15, 21
        "Function_22_6DBF",        # 16, 22
        "Function_23_7B24",        # 17, 23
        "Function_24_864B",        # 18, 24
        "Function_25_A1B4",        # 19, 25
        "Function_26_A1D8",        # 1A, 26
        "Function_27_AC6B",        # 1B, 27
        "Function_28_AFA2",        # 1C, 28
        "Function_29_CE30",        # 1D, 29
        "Function_30_D97B",        # 1E, 30
        "Function_31_E4D2",        # 1F, 31
        "Function_32_100A7",       # 20, 32
        "Function_33_105E8",       # 21, 33
        "Function_34_11C85",       # 22, 34
        "Function_35_11D14",       # 23, 35
        "Function_36_126AB",       # 24, 36
        "Function_37_126E8",       # 25, 37
        "Function_38_13586",       # 26, 38
        "Function_39_13DC3",       # 27, 39
        "Function_40_14291",       # 28, 40
        "Function_41_15FCA",       # 29, 41
        "Function_42_16396",       # 2A, 42
        "Function_43_18379",       # 2B, 43
        "Function_44_1942D",       # 2C, 44
        "Function_45_19B2E",       # 2D, 45
        "Function_46_1BA97",       # 2E, 46
        "Function_47_1BAE1",       # 2F, 47
        "Function_48_1BB36",       # 30, 48
        "Function_49_1BB6D",       # 31, 49
        "Function_50_1BBB1",       # 32, 50
        "Function_51_1BBF5",       # 33, 51
        "Function_52_1BC2D",       # 34, 52
        "Function_53_1BC5D",       # 35, 53
        "Function_54_1CD9F",       # 36, 54
        "Function_55_1CDF0",       # 37, 55
        "Function_56_1D8FA",       # 38, 56
        "Function_57_1D96C",       # 39, 57
        "Function_58_1EA10",       # 3A, 58
        "Function_59_1EA94",       # 3B, 59
        "Function_60_1EAD1",       # 3C, 60
        "Function_61_1EB0E",       # 3D, 61
        "Function_62_1EB70",       # 3E, 62
        "Function_63_1EC9E",       # 3F, 63
        "Function_64_1F6D3",       # 40, 64
        "Function_65_1F746",       # 41, 65
        "Function_66_1F7B9",       # 42, 66
        "Function_67_1F82C",       # 43, 67
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
    Jump("loc_297F")

    label("loc_13A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_164E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A2")

    ChrTalk(
        0x8,
        (
            "#01000FNoｱl, regarding your reinstatement to the CGF,\x01",
            "I will prepare the necessary papers.\x02\x03",
            "Due to the influence of the raid incident,\x01",
            "support requests will probably come in from\x01",
            "every place. If you have time, deal with those.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, today I'll do them\x01",
            "putting everything I've got.\x02\x03",
            "#10103F...Chief Sergei, thank you very\x01",
            "much for everything you've done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004FEh eh, I don't need any thanks.\x02\x03",
            "#01002FJust focus on your last jobs\x01",
            "so to not have any regrets.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1649")

    label("loc_15A2")


    ChrTalk(
        0x8,
        (
            "#01000FNoｱl, regarding your reinstatement to the CGF,\x01",
            "I will prepare the necessary papers.\x02\x03",
            "#01004FTonight I will treat you to eating\x01",
            "out, so come back for that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1649")

    Jump("loc_297F")

    label("loc_164E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_17F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175C")

    ChrTalk(
        0x8,
        (
            "#01003FYou finally caught traces of Randy, eh?\x02\x03",
            "#01002FEh eh, with this, it means that you're\x01",
            "finally prepared to take him back.\x02\x03",
            "#01001FIf you've got that resolve, then don't dawdle.\x01",
            "You all, go bring that fool back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes...!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_17EF")

    label("loc_175C")


    ChrTalk(
        0x8,
        (
            "#01003FThe CGF is currently reassembling\x01",
            "reinforcements.\x02\x03",
            "#01001FIf you've got that resolve, then don't dawdle.\x01",
            "You all, go bring Randy back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17EF")

    Jump("loc_297F")

    label("loc_17F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_19DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191C")

    ChrTalk(
        0x8,
        (
            "#01000FBecause of the Mainz region occupation incident\x01",
            "influence, support requests aren't coming in.\x02\x03",
            "#01003FYou can devote yourselves to\x01",
            "find out where that Randy is.\x02\x03",
            "#01001FGo, and be very careful. If I find\x01",
            "out something, I'll contact you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FSir...!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_19D6")

    label("loc_191C")


    ChrTalk(
        0x8,
        (
            "#01003FToday there're no support requests,\x01",
            "so you can devote yourselves to\x01",
            "find out where that Randy is.\x02\x03",
            "#01001FGo, and be very careful. If I find\x01",
            "out something, I'll contact you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D6")

    Jump("loc_297F")

    label("loc_19DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B34")

    ChrTalk(
        0x8,
        (
            "#01003FSection Two and the CGF are\x01",
            "investigating about Wald Wales\x01",
            "and the Gnosis case.\x02\x03",
            "#01000FNow that the transcontinental railway restoration\x01",
            "is over, you don't have to be in a hurry anymore.\x02\x03",
            "About the Bracers' case, if you have the\x01",
            "time and occasion while on your jobs,\x01",
            "you can show your faces at the Guild.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1C1A")

    label("loc_1B34")


    ChrTalk(
        0x8,
        (
            "#01000FNow that the transcontinental railway restoration\x01",
            "is over, you don't have to be in a hurry anymore.\x02\x03",
            "About the Bracers' case, if you have the\x01",
            "time and occasion while on your jobs,\x01",
            "you can show your faces at the Guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C1A")

    Jump("loc_297F")

    label("loc_1C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1DF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D22")

    ChrTalk(
        0x8,
        (
            "#01000F...You're back.\x01",
            "You got a call from Fran, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, we're now going\x01",
            "to the incident scene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003FI see, got it.\x02\x03",
            "#01000FI'll hear your report about the Doll Studio later.\x01",
            "You too, go do what you can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1DF3")

    label("loc_1D22")


    ChrTalk(
        0x8,
        (
            "#01000FThose from Section Two and Sonya and\x01",
            "her CGF should be heading to the incident\x01",
            "scene on West Crossbell Highway too.\x02\x03",
            "I'll hear your report about the Doll Studio later.\x01",
            "You too, go do what you can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DF3")

    Jump("loc_297F")

    label("loc_1DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2032")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F68")

    ChrTalk(
        0x8,
        (
            "#01006FWith the matter of the local referendum\x01",
            "for the national independence, many \x01",
            "official papers are coming in.\x02\x03",
            "#01002FThere're some subjects I'm worried about, but...\x01",
            "Well, we'll leave them to the other sections.\x02\x03",
            "#01000FFor the present, crisis management comes first.\x01",
            "Not just the Doll Studio inquiry,\x01",
            "cover support requests too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_202D")

    label("loc_1F68")


    ChrTalk(
        0x8,
        (
            "#01004FAh, if you're looking for KeA, it seems\x01",
            "she just went out to shop for dinner.\x02\x03",
            "#01002FShe said she was dropping by the\x01",
            "library for a bit... Well, if\x01",
            "you're worried go check yourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_202D")

    Jump("loc_297F")

    label("loc_2032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_21ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2135")

    ChrTalk(
        0x8,
        (
            "#01000FHey, I just came back\x01",
            "from the hospital too.\x02\x03",
            "#01003FYou continue with your job, proceed\x01",
            "with the "Cryptid" investigation.\x02\x03",
            "#01002FWhile the "Divine Blade of Wind" can't act,\x01",
            "you can increase your achievements by a lot.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_21E8")

    label("loc_2135")


    ChrTalk(
        0x8,
        (
            "#01003FYou continue with your job, proceed\x01",
            "with the "Cryptid" investigation.\x02\x03",
            "#01002FWhile the "Divine Blade of Wind" can't act,\x01",
            "you can increase your achievements by a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E8")

    Jump("loc_297F")

    label("loc_21ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_21FB")
    Jump("loc_297F")

    label("loc_21FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2376")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22EC")

    ChrTalk(
        0x8,
        (
            "#01000FI'll contact the mayor and che CGFs\x01",
            "about terrorists information.\x02\x03",
            "Dudley, I leave to you to\x01",
            "keep my guys safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FYes, please leave them to me.\x02\x03",
            "#00601F...Come now, let's go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FSir!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2371")

    label("loc_22EC")


    ChrTalk(
        0x8,
        (
            "#01000FI don't know if something's\x01",
            "happened in the Geofront,\x01",
            "but be very careful.\x02\x03",
            "Dudley, I leave to you to\x01",
            "keep my guys safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2371")

    Jump("loc_297F")

    label("loc_2376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_25B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24CA")

    ChrTalk(
        0x8,
        (
            "#01000FThat girl you came across\x01",
            "too, Shirley, she showed\x01",
            "up for a reason for sure.\x02\x03",
            "#01003FIt's true that the "Red Constellation" actions\x01",
            "are a concern, but even if we caught sight of\x01",
            "them there would be nothing we can do.\x02\x03",
            "#01000FWell, I'll continue leaving things to you.\x01",
            "Go do what you can at your pace.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_25AE")

    label("loc_24CA")


    ChrTalk(
        0x8,
        (
            "#01003FIt's true that the "Red Constellation" actions\x01",
            "are a concern, but even if we caught sight of\x01",
            "them there would be nothing we can do.\x02\x03",
            "#01000FWell, I'll continue leaving things to you.\x01",
            "Go do what you can at your pace.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25AE")

    Jump("loc_297F")

    label("loc_25B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2739")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26B8")

    ChrTalk(
        0x8,
        (
            "#01003FToday I'm going to stay here on standby.\x02\x03",
            "#01000FI'll keep in contact with Section One\x01",
            "and proceed with the final preparations\x01",
            "for tomorrow Trade Conference.\x02\x03",
            "I'll call you if something happens,\x01",
            "so go out without reserve.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2734")

    label("loc_26B8")


    ChrTalk(
        0x8,
        (
            "#01003FToday I'm going to stay here on standby.\x02\x03",
            "#01000FI'll call you if something happens,\x01",
            "so go out without reserve.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2734")

    Jump("loc_297F")

    label("loc_2739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2747")
    Jump("loc_297F")

    label("loc_2747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2976")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28BC")

    ChrTalk(
        0x8,
        (
            "#01002FResponding to various requests keeping\x01",
            "in mind the citizens' safety as priority...\x01",
            "That's what the Special Support Section is.\x02\x03",
            "#01003FThose Cao and Lechter can't be dealt\x01",
            "with ordinary means, so for now leave \x01",
            "the investigation to Section One.\x02\x03",
            "#01000FDo not lose sight of\x01",
            "your actual duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, please leave it to us.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2971")

    label("loc_28BC")


    ChrTalk(
        0x8,
        (
            "#01000FResponding to various requests keeping\x01",
            "in mind the citizens' safety as priority...\x01",
            "That's what the Special Support Section is.\x02\x03",
            "Do not lose sight of\x01",
            "your actual duties.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2971")

    Jump("loc_297F")

    label("loc_2976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_297F")

    label("loc_297F")

    TalkEnd(0x8)
    Return()

    # Function_5_1397 end

    def Function_6_2983(): pass

    label("Function_6_2983")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2BDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B88")

    ChrTalk(
        0x9,
        (
            "#01108FEveryone, uhm...sorry.\x02\x03",
            "#01103FI suddenly did such a thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FDon't worry about it, KeA...\x02\x03",
            "#00004FConsidering the situatio we're in, it\x01",
            "can't be helped that you feel uneasy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FStopping that uneasiness is\x01",
            "your guardians...our role.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIf something happens,\x01",
            "don't hesitate to come\x01",
            "to us from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHa ha, it would make us happy\x01",
            "too if you could rely on us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01108FYes...thank you.\x02\x03",
            "#01100FBe careful...\x01",
            "KeA will wait for you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 6)
    Jump("loc_2BD6")

    label("loc_2B88")


    ChrTalk(
        0x9,
        (
            "#01108FEveryone, thank you.\x02\x03",
            "#01100FBe careful...\x01",
            "KeA will wait for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BD6")

    Jump("loc_34BC")

    label("loc_2BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2BE9")
    Jump("loc_34BC")

    label("loc_2BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2D84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D1F")

    ChrTalk(
        0x9,
        (
            "#01103FRandy... I hope you\x01",
            "find him safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWe will, for sure. You don't\x01",
            "have to worry, KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FSenior Randy is cruel though.\x01",
            "Making little KeA worry so much...\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. When we find him,\x01",
            "we'll have to scold him a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01109FYes, that's right.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2D7F")

    label("loc_2D1F")


    ChrTalk(
        0x9,
        (
            "#01109FWhen Randy comes home,\x01",
            "KeA too will scold him!\x02\x03",
            "#01100FEveryone...\x01",
            "Be very careful!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D7F")

    Jump("loc_34BC")

    label("loc_2D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2F30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EC5")

    ChrTalk(
        0x9,
        (
            "#01109FEhehe, actually, during yesterday\x01",
            "I went out and bought many ingredients.\x02\x03",
            "It was raining, but \x01",
            "I had to go shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, that's our KeA.\x02\x03",
            "#00000FWe'll put them into today's hot pot, so\x01",
            "be a good kid and watch the house, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01109FYes, Lloyd, guys, be careful!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2F2B")

    label("loc_2EC5")


    ChrTalk(
        0x9,
        (
            "#01100FKeA will prepare the hot pot\x01",
            "today too and wait for you.\x02\x03",
            "#01109FLloyd, guys, be careful!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F2B")

    Jump("loc_34BC")

    label("loc_2F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2F3E")
    Jump("loc_34BC")

    label("loc_2F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F4C")
    Jump("loc_34BC")

    label("loc_2F4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2F5A")
    Jump("loc_34BC")

    label("loc_2F5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2F68")
    Jump("loc_34BC")

    label("loc_2F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3131")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30C2")

    ChrTalk(
        0x9,
        (
            "#01100FEveryone, have a safe trip!\x02\x03",
            "#01109FEhehe, you be careful too, Dudley, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00603FI told you to not address me so casually...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01105FUhm?\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10A,
        (
            "#00606F...Damn, whatever!\x01",
            "You guys, let's go at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Hmm, as expected, not even\x01",
            "Mr. Dudley is a match for KeA.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_312C")

    label("loc_30C2")


    ChrTalk(
        0x9,
        (
            "#01109FEveryone, have a safe trip!\x02\x03",
            "Ehehe, you be careful too, Dudley, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00603F(Honestly...)\x02",
    )

    CloseMessageWindow()

    label("loc_312C")

    Jump("loc_34BC")

    label("loc_3131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_END)), "loc_325C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3201")

    ChrTalk(
        0x9,
        (
            "#01105FThat Sieg was\x01",
            "very cool, right?\x02\x03",
            "#01109FAlso, he's so smart.\x01",
            "KeA would like to meet him again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(The white falcon crest\x01",
            "stamped on the memo...\x01",
            "I-Impossible.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3257")

    label("loc_3201")


    ChrTalk(
        0x9,
        (
            "#01105FThat Sieg was\x01",
            "very cool, right?\x02\x03",
            "#01109FKeA would like to meet him again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3257")

    Jump("loc_34BC")

    label("loc_325C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_346D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33E3")

    ChrTalk(
        0x9,
        (
            "#01102FThe maple muffins will be\x01",
            "alright until tomorrow.\x02\x03",
            "#01109FEat them as lunch if you get\x01",
            "hungry during your job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thank you, KeA.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, they were very good,\x01",
            "I'm looking forward to get hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01102FEhehe, KeA will make them again.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 1)), scpexpr(EXPR_END)), "loc_33DB")

    ChrTalk(
        0x101,
        (
            "#00002F(Ha ha, thank goodness...\x01",
            "it looks like she's cheerful again.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33DB")

    SetScenarioFlags(0x0, 3)
    Jump("loc_3468")

    label("loc_33E3")


    ChrTalk(
        0x9,
        (
            "#01104FHumhuhuum♪\x01",
            "I have to finish laundry quickly.\x02\x03",
            "#01100FEat the maple muffins\x01",
            "for lunch if you get\x01",
            "hungry during your job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3468")

    Jump("loc_34BC")

    label("loc_346D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_347B")
    Jump("loc_34BC")

    label("loc_347B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3489")
    Jump("loc_34BC")

    label("loc_3489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3497")
    Jump("loc_34BC")

    label("loc_3497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_34A5")
    Jump("loc_34BC")

    label("loc_34A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_34B3")
    Jump("loc_34BC")

    label("loc_34B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_34BC")

    label("loc_34BC")

    TalkEnd(0xFE)
    Return()

    # Function_6_2983 end

    def Function_7_34C0(): pass

    label("Function_7_34C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_35DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35C0")

    ChrTalk(
        0xA,
        "#01200FGrrrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FZeit...\x01",
            "He's worked up about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FBecause of the situation, his\x01",
            "weariness is probably even higher.\x02\x03",
            "#00001FZeit, please take care\x01",
            "of KeA and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01200FWoof!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_35D9")

    label("loc_35C0")


    ChrTalk(
        0xA,
        "#01200FGrrrrrowl...\x02",
    )

    CloseMessageWindow()

    label("loc_35D9")

    Jump("loc_4044")

    label("loc_35DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_35EC")
    Jump("loc_4044")

    label("loc_35EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_3714")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F3")

    ChrTalk(
        0xA,
        "#01200FGrrrowl...woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F"Jaegers are used to fields.\x01",
            "Be extremely careful when\x01",
            "entering their territory."\x02\x03",
            "...so he says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThank you, Zeit. I'll\x01",
            "treasure your advice.\x02\x03",
            "We mustn't take on the\x01",
            "jaegers directly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_370F")

    label("loc_36F3")


    ChrTalk(
        0xA,
        "#01200FGrrrowl...woof.\x02",
    )

    CloseMessageWindow()

    label("loc_370F")

    Jump("loc_4044")

    label("loc_3714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_37E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37C6")

    ChrTalk(
        0xA,
        "#01200FGrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...You're right. \x01",
            "Mr. Randy is a big idiot.\x02\x03",
            "#00200FWe'll bring him back\x01",
            "at any cost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah...of course!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_37DD")

    label("loc_37C6")


    ChrTalk(
        0xA,
        "#01200FGrrrowl...\x02",
    )

    CloseMessageWindow()

    label("loc_37DD")

    Jump("loc_4044")

    label("loc_37E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_381A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37FD")
    Call(0, 8)
    Jump("loc_3815")

    label("loc_37FD")


    ChrTalk(
        0xA,
        "#01203FGrrrrowl...\x02",
    )

    CloseMessageWindow()

    label("loc_3815")

    Jump("loc_4044")

    label("loc_381A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_390B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E4")

    ChrTalk(
        0xA,
        "#01200FGrrrowl...woof, woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt seems that even Zeit is feeling\x01",
            "that something serious has happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYeah...let's be careful and go to the scene.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3906")

    label("loc_38E4")


    ChrTalk(
        0xA,
        "#01200FGrrrowl...woof, woof.\x02",
    )

    CloseMessageWindow()

    label("loc_3906")

    Jump("loc_4044")

    label("loc_390B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3932")

    ChrTalk(
        0xA,
        "#01203F...Grrowl...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4044")

    label("loc_3932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3A52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A32")

    ChrTalk(
        0xA,
        "#01200FGrrowl...woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F"Go, and be careful"\x01",
            "...so he says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIt seems it'll be quite dangerous\x01",
            "when we'll fight the Cryptids...\x02\x03",
            "#00000FThank you, Zeit.\x01",
            "If things get dangerous,\x01",
            "give us your help again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3A4D")

    label("loc_3A32")


    ChrTalk(
        0xA,
        "#01200FGrrowl...woof.\x02",
    )

    CloseMessageWindow()

    label("loc_3A4D")

    Jump("loc_4044")

    label("loc_3A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3A60")
    Jump("loc_4044")

    label("loc_3A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3D23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D02")

    ChrTalk(
        0xA,
        "#01200FGrrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FHmph, a self-important wolf as always.\x02\x03",
            "#00600FStill, since you're treated like a police dog,\x01",
            "there're times when we need your help.\x01",
            "Be prepared to sortie at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01200F...Woof.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B88")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_3B88")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BBC")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_3BBC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BF0")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_3BF0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C24")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_3C24")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C58")
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_3C58")

    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00306F(How can he call self-\x01",
            "important others, right...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(*giggle*, we can't do anything about it,\x01",
            "since it's Mr. Dudley way to encourage.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3D1E")

    label("loc_3D02")


    ChrTalk(
        0xA,
        "#01200FGrrrowl...woof.\x02",
    )

    CloseMessageWindow()

    label("loc_3D1E")

    Jump("loc_4044")

    label("loc_3D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_3D4D")

    ChrTalk(
        0xA,
        "#01200FGrrrowl...woof.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4044")

    label("loc_3D4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E7D")

    ChrTalk(
        0xA,
        "#01200FGrrrowl...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E78")

    ChrTalk(
        0x101,
        (
            "#00005FOh, right, Zeit...\x01",
            "You watched the inauguration of\x01",
            "Orchis Tower with KeA, right?\x02\x03",
            "Somehow KeA looks down.\x01",
            "Has anything happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01200FGrrrowl...woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FUhhm, with Tio not around, we don't\x01",
            "understand him, as you'd expect.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_3E78")

    Jump("loc_4044")

    label("loc_3E7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F54")

    ChrTalk(
        0xA,
        "#01200FGrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHey, Zeit.\x02\x03",
            "#00309FHa ha, thanks for guidin' us\x01",
            "back then at the old mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHa ha, please help us from now on too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01200FGrrowl...woof.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3F6F")

    label("loc_3F54")


    ChrTalk(
        0xA,
        "#01200FGrrowl...woof.\x02",
    )

    CloseMessageWindow()

    label("loc_3F6F")

    Jump("loc_4044")

    label("loc_3F74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_403B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4021")

    ChrTalk(
        0xA,
        "#01203FGrrrowl...woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOn rainy days, even\x01",
            "Zeit looks bored.\x02\x03",
            "Well, watch over the house\x01",
            "quietly today too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01200F...Woof.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4036")

    label("loc_4021")


    ChrTalk(
        0xA,
        "#01200F...Woof.\x02",
    )

    CloseMessageWindow()

    label("loc_4036")

    Jump("loc_4044")

    label("loc_403B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4044")

    label("loc_4044")

    TalkEnd(0xFE)
    Return()

    # Function_7_34C0 end

    def Function_8_4048(): pass

    label("Function_8_4048")

    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xA,
        "#01200FGrrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Nyaa～～[I'm hungry]\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt looks like that both Zeit\x01",
            "and Koppe are looking\x01",
            "forward to tonight hot pot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FEh? But don't cats have\x01",
            "what is called "cat tongue"...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FDon't animals of the dog\x01",
            "family have it too?\x01",
            "Hu hu, what a strange way of saying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F...I'll cool it down for them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01200FWoof.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 4)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_8_4048 end

    def Function_9_41C0(): pass

    label("Function_9_41C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_41D1")
    Jump("loc_43FD")

    label("loc_41D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4337")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_431D")

    ChrTalk(
        0xFE,
        "Nyanyayayaa～㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, he's really eating it nicely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt seems he was missing\x01",
            "the cat food flavor.\x02\x03",
            "It appears that when we\x01",
            "were not around he went out\x01",
            "to catch his food himself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FEeeh, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, unexpectedly Koppe\x01",
            "has an indomitable side.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4332")

    label("loc_431D")


    ChrTalk(
        0xFE,
        "Nyanyayayaa～㈱\x02",
    )

    CloseMessageWindow()

    label("loc_4332")

    Jump("loc_43FD")

    label("loc_4337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4345")
    Jump("loc_43FD")

    label("loc_4345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_43CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4360")
    Call(0, 8)
    Jump("loc_43CA")

    label("loc_4360")


    ChrTalk(
        0xFE,
        "Nyaa～～[I'm hungry]\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F(There's KeA at home, so there's\x01",
            "no need for us to feed him today.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43CA")

    Jump("loc_43FD")

    label("loc_43CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_43DD")
    Jump("loc_43FD")

    label("loc_43DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_43FD")

    ChrTalk(
        0xFE,
        "Nya～～go.[Hello]\x02",
    )

    CloseMessageWindow()

    label("loc_43FD")

    TalkEnd(0xFE)
    Return()

    # Function_9_41C0 end

    def Function_10_4401(): pass

    label("Function_10_4401")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4740")

    ChrTalk(
        0xB,
        (
            "#05928FThe reason Mr. Arios had Shizuku\x01",
            "discharged forcibly... I didn't \x01",
            "know it was such a serious one.\x02\x03",
            "#05923FI think that nothing can be done,\x01",
            "if we consider Shizuku's safety...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, that's right...\x02\x03",
            "#00005F...By the way, sister Cecil.\x01",
            "How's the situation at St. Ursula?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, I'm concerned about the hospitalized\x01",
            "policemen and about Miss Ilya's condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05920FThe hospital is in confusion,\x01",
            "but the dealing with patients\x01",
            "is being performed normally.\x02\x03",
            "#05924FMiss Fran has been recovering well and\x01",
            "was transferred to the general ward...\x02\x03",
            "#05920FMr. Donovan has just regained\x01",
            "consciousness not so long ago.\x02\x03",
            "#05928F...Although Ilya is still\x01",
            "not waking up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FI hope she gets back\x01",
            "on her feet fast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#05924FYes... I really hope so too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 1)
    Jump("loc_48B5")

    label("loc_4740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_483F")

    ChrTalk(
        0xB,
        (
            "#05920FThe hospital is in confusion,\x01",
            "but the dealing with patients\x01",
            "is being performed normally.\x02\x03",
            "#05923FAt any rate...\x01",
            "I will watch over the\x01",
            "place with KeA.\x02\x03",
            "#05920FThe situation seems pretty serious...\x01",
            "So, please, be very careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_48B5")

    label("loc_483F")


    ChrTalk(
        0xB,
        (
            "#05920FI will watch over the\x01",
            "place with KeA.\x02\x03",
            "The situation seems pretty serious...\x01",
            "So, please, be very careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48B5")

    TalkEnd(0xFE)
    Return()

    # Function_10_4401 end

    def Function_11_48B9(): pass

    label("Function_11_48B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48CB")
    Call(0, 16)
    Jump("loc_4902")

    label("loc_48CB")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThis is Tio's room.\x01",
            "Let's not enter.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_4902")

    Return()

    # Function_11_48B9 end

    def Function_12_4903(): pass

    label("Function_12_4903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4915")
    Call(0, 17)
    Jump("loc_494E")

    label("loc_4915")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThis is Randy's room.\x01",
            "Let's not enter.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_494E")

    Return()

    # Function_12_4903 end

    def Function_13_494F(): pass

    label("Function_13_494F")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F...Now that I think about it, KeA said\x01",
            "she was going to Sunday School.\x02\x03",
            "Chief has gone out too, maybe it\x01",
            "would be better going out together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, let's ask her.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 800, 0, 1890, 0)
    EventEnd(0x4)
    Return()

    # Function_13_494F end

    def Function_14_4A21(): pass

    label("Function_14_4A21")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F...Now that I think about it, KeA said\x01",
            "she was going to Sunday School.\x02\x03",
            "Chief has gone out too, maybe it\x01",
            "would be better going out together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, let's ask her.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_14_4A21 end

    def Function_15_4AF3(): pass

    label("Function_15_4AF3")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FKeA is going to Sunday School.\x01",
            "Let's use the back entrance as a shortcut.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -1330, 0, 71380, 268)
    EventEnd(0x4)
    Return()

    # Function_15_4AF3 end

    def Function_16_4B62(): pass

    label("Function_16_4B62")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4BFC")
    SetChrPos(0x1A5, 169520, 0, 61730, 0)

    label("loc_4BFC")

    OP_0D()

    ChrTalk(
        0x102,
        "#6P#00100FThis is Tio's room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FShe's currently on a business trip in\x01",
            "the autonomous state of Leman, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, she went with Jona\x01",
            "to the Epstein Foundation\x01",
            "research lab.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWith the state laws revised, even\x01",
            "the orbal net spreading has been\x01",
            "proceeding. They are helping with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10103FI don't understand complicated things, but...\x01",
            "They seem to have it hard too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DFA")

    ChrTalk(
        0x1A5,
        "#12P#01100FI hope Tio comes home fast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E37")

    label("loc_4DFA")


    ChrTalk(
        0x101,
        (
            "#00000FYeah, it would be nice if\x01",
            "she came back quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E37")

    OP_5A()
    SetChrPos(0x0, 169990, 0, 63110, 180)
    SetScenarioFlags(0x13B, 3)
    EventEnd(0x5)
    Return()

    # Function_16_4B62 end

    def Function_17_4E4F(): pass

    label("Function_17_4E4F")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4EE9")
    SetChrPos(0x1A5, 13500, 0, 61420, 0)

    label("loc_4EE9")

    OP_0D()

    ChrTalk(
        0x101,
        "#12P#00000FThis is Randy's room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FRandy is currently in the midst\x01",
            "of rehabilitation training at\x01",
            "Tangram Gate with the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FAh, if I remember correctly, during the Cult\x01",
            "incident they were served that drug, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103FYes...\x01",
            "Severe after-effects\x01",
            "didn't remain though.\x02\x03",
            "#10108FTo regain stamina and their senses\x01",
            "it seems it will take some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FI see...\x01",
            "I hope the CGF recover quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5109")

    ChrTalk(
        0x1A5,
        "#12P#01100FI wish Randy too came back home fast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5149")

    label("loc_5109")


    ChrTalk(
        0x102,
        (
            "#00100FRight, I'd like for Randy too\x01",
            "to come home quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5149")

    OP_5A()
    SetChrPos(0x0, 14040, 0, 63300, 180)
    SetScenarioFlags(0x13B, 4)
    EventEnd(0x5)
    Return()

    # Function_17_4E4F end

    def Function_18_5161(): pass

    label("Function_18_5161")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5188")
    Call(0, 21)
    Return()

    label("loc_5188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_51D9")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The terminal orbal power is failing.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    label("loc_51D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5344")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The terminal orbal power is failing.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5340")

    ChrTalk(
        0x101,
        (
            "#00003F...It looks like the orbal\x01",
            "power is not reaching it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FFor now I am happy that\x01",
            "it looks like it hasn't\x01",
            "got anything broken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, if we have to use a terminal, \x01",
            "let's do it at the Merkaba.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYou're right, let's\x01",
            "leave this one be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CC, 5)

    label("loc_5340")

    TalkEnd(0xFF)
    Return()

    label("loc_5344")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_535E")
    OP_C9(0x0, 0x4)
    OP_C9(0x0, 0x100)

    label("loc_535E")

    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5377")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AC4")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_53B0"),
        (1, "loc_556C"),
        (2, "loc_5AAF"),
        (3, "loc_5AB7"),
        (SWITCH_DEFAULT, "loc_5ABF"),
    )


    label("loc_53B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_53C3")
    OP_2B(0x94, 0xFFFF)
    Jump("loc_5567")

    label("loc_53C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_53DE")
    OP_2B(0x8E, 0x8F, 0x90, 0x91, 0x92, 0xFFFF)
    Jump("loc_5567")

    label("loc_53DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5441")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Currently there are no support requests.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_5567")

    label("loc_5441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_545C")
    OP_2B(0x8B, 0x8C, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_5567")

    label("loc_545C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5497")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5485")
    OP_2B(0x85, 0x86, 0x87, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_5492")

    label("loc_5485")

    OP_2B(0x85, 0x86, 0x88, 0x80, 0x83, 0xFFFF)

    label("loc_5492")

    Jump("loc_5567")

    label("loc_5497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_54B0")
    OP_2B(0x80, 0x81, 0x82, 0x83, 0xFFFF)
    Jump("loc_5567")

    label("loc_54B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_54BE")
    Jump("loc_5567")

    label("loc_54BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_54DB")
    OP_2B(0x79, 0x7A, 0x7B, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_5567")

    label("loc_54DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_END)), "loc_54F8")
    OP_2B(0x74, 0x75, 0x76, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_5567")

    label("loc_54F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5511")
    OP_2B(0x6F, 0x70, 0x71, 0x72, 0xFFFF)
    Jump("loc_5567")

    label("loc_5511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5545")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_5535")
    OP_2B(0x6A, 0x6B, 0x6C, 0x6D, 0x67, 0xFFFF)
    Jump("loc_5540")

    label("loc_5535")

    OP_2B(0x6A, 0x6B, 0x6C, 0x67, 0xFFFF)

    label("loc_5540")

    Jump("loc_5567")

    label("loc_5545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 7)), scpexpr(EXPR_END)), "loc_555C")
    OP_2B(0x65, 0x66, 0x67, 0xFFFF)
    Jump("loc_5567")

    label("loc_555C")

    OP_2B(0x65, 0x66, 0x67, 0x68, 0xFFFF)

    label("loc_5567")

    Jump("loc_5ABF")

    label("loc_556C")

    SetMapFlags(0x40000000)
    OP_E5(0x7)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5661")
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        "This is Crossbell Police.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_5639")

    AnonymousTalk(
        0xFF,
        "I will receive your report.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        (
            "Report processing, complete.\x01",
            "Thank you for your hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_565C")

    label("loc_5639")


    AnonymousTalk(
        0xFF,
        "There no reportable requests.\x02",
    )

    CloseMessageWindow()

    label("loc_565C")

    Jump("loc_5AA1")

    label("loc_5661")

    SetChrName("Receptionist Fran")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_56B8")
    Sound(3062, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Yes, this is Crossbell Poliiice!\x02",
    )

    CloseMessageWindow()
    Jump("loc_56ED")

    label("loc_56B8")

    Sound(3061, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Everyone, thank you for your hard wooork.\x02",
    )

    CloseMessageWindow()

    label("loc_56ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_598B")
    Sound(3067, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        "Then, I'll receive your report, okaaay?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58FE")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_576E"),
        (13, "loc_57BC"),
        (12, "loc_5807"),
        (SWITCH_DEFAULT, "loc_584B"),
    )


    label("loc_576E")

    Sound(3075, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Rank 1st...\x01",
            "That's too amazing, Mr. Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_584B")

    label("loc_57BC")

    Sound(3074, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Rank 2nd──\x01",
            "That's amazing, Mr. Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_584B")

    label("loc_5807")

    Sound(3073, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Rank 3rd──\x01",
            "You did, Mr. Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_584B")

    label("loc_584B")

    Sound(3076, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "I will immediately send you\x01",
            "the special article you gaaained!\x02",
        )
    )

    CloseMessageWindow()
    Sound(3077, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Thank you for your hard wooork!\x01",
            "I hope to be working with you agaaain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5983")

    label("loc_58FE")

    Sound(3078, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        "The report is oveeer.\x02",
    )

    CloseMessageWindow()
    Sound(3079, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Then, please contact me again the\x01",
            "next time you complete a requeeest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5983")

    SetScenarioFlags(0x0, 1)
    Jump("loc_5AA1")

    label("loc_598B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5A18")
    Sound(3063, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Oh...\x01",
            "Haven't you just made a report?\x02",
        )
    )

    CloseMessageWindow()
    Sound(3064, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Please do it again when you complete a request.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AA1")

    label("loc_5A18")

    Sound(3065, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Oh...it seems you don't have\x01",
            "any request you can repooort.\x02",
        )
    )

    CloseMessageWindow()
    Sound(3066, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        "Please, let's work together agaaain.\x02",
    )

    CloseMessageWindow()

    label("loc_5AA1")

    OP_57(0x0)
    OP_E5(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_5ABF")

    label("loc_5AAF")

    Call(0, 20)
    Jump("loc_5ABF")

    label("loc_5AB7")

    Call(0, 19)
    Jump("loc_5ABF")

    label("loc_5ABF")

    Jump("loc_5377")

    label("loc_5AC4")

    OP_E5(0x6)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x68, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B0A")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 24)
    Return()

    label("loc_5B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B42")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 27)
    Return()

    label("loc_5B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B81")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 32)
    Return()

    label("loc_5B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BB9")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 39)
    Return()

    label("loc_5BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C46")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5C10")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C0B")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 41)
    Return()

    label("loc_5C0B")

    Jump("loc_5C41")

    label("loc_5C10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C41")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 41)
    Return()

    label("loc_5C41")

    Jump("loc_5CC7")

    label("loc_5C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C5F")
    SetScenarioFlags(0x168, 2)
    Call(0, 67)
    Jump("loc_5CC7")

    label("loc_5C5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x92, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C9E")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 44)
    Return()

    label("loc_5C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_5CB5")
    ClearScenarioFlags(0x22, 3)
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    label("loc_5CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_5CC7")
    ClearScenarioFlags(0x22, 6)
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    label("loc_5CC7")

    FadeToBright(300, 0)
    OP_0D()
    OP_E5(0xB)
    Call(0, 67)
    TalkEnd(0xFF)
    Return()

    # Function_18_5161 end

    def Function_19_5CDA(): pass

    label("Function_19_5CDA")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5D08")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x94, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_5D03")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D03")

    Jump("loc_6018")

    label("loc_5D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5D48")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x92, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D43")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D43")

    Jump("loc_6018")

    label("loc_5D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5D60")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6018")

    label("loc_5D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5DA0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D9B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D9B")

    Jump("loc_6018")

    label("loc_5DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5E2A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5DF3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DEE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DEE")

    Jump("loc_5E25")

    label("loc_5DF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E25")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E25")

    Jump("loc_6018")

    label("loc_5E2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5E63")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E5E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E5E")

    Jump("loc_6018")

    label("loc_5E63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_5E7B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6018")

    label("loc_5E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5EC2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EBD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5EBD")

    Jump("loc_6018")

    label("loc_5EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_END)), "loc_5F09")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F04")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F04")

    Jump("loc_6018")

    label("loc_5F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5F42")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F3D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F3D")

    Jump("loc_6018")

    label("loc_5F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5FBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_5F8B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6D, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F86")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F86")

    Jump("loc_5FB6")

    label("loc_5F8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FB6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5FB6")

    Jump("loc_6018")

    label("loc_5FBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 7)), scpexpr(EXPR_END)), "loc_5FED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FE8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5FE8")

    Jump("loc_6018")

    label("loc_5FED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x68, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6018")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6018")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_606A")
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

    label("loc_606A")

    Return()

    # Function_19_5CDA end

    def Function_20_606B(): pass

    label("Function_20_606B")

    OP_E5(0x6)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 3)), scpexpr(EXPR_END)), "loc_608D")
    SetScenarioFlags(0x2A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_608D")
    ClearScenarioFlags(0x2A, 0)

    label("loc_608D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_END)), "loc_60AA")
    SetScenarioFlags(0x2A, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60AA")
    ClearScenarioFlags(0x2A, 1)

    label("loc_60AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_END)), "loc_60C7")
    SetScenarioFlags(0x2A, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60C7")
    ClearScenarioFlags(0x2A, 2)

    label("loc_60C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 6)), scpexpr(EXPR_END)), "loc_60E4")
    SetScenarioFlags(0x2A, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60E4")
    ClearScenarioFlags(0x2A, 3)

    label("loc_60E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_END)), "loc_6101")
    SetScenarioFlags(0x2A, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6101")
    ClearScenarioFlags(0x2A, 4)

    label("loc_6101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_END)), "loc_611E")
    SetScenarioFlags(0x2A, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_611E")
    ClearScenarioFlags(0x2A, 5)

    label("loc_611E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_END)), "loc_612A")
    SetScenarioFlags(0x2A, 6)

    label("loc_612A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_617C")
    RunExpression(0x6, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopBGM(0x0)
    Jump("loc_61F7")

    label("loc_617C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_61CE")
    OP_24(0x80)
    RunExpression(0x6, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()
    Sound(128, 1, 50, 0)
    Jump("loc_61F7")

    label("loc_61CE")

    RunExpression(0x6, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()

    label("loc_61F7")

    Return()

    # Function_20_606B end

    def Function_21_61F8(): pass

    label("Function_21_61F8")

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
            "#6P#00004FAccording to Chief Roberts,\x01",
            "we have to install this Memory\x01",
            "Quartz into the terminal, right?\x02\x03",
            "#00000FSo...\x01",
            "Elie, if you please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FYes, let's give it a try.\x02",
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
            "Elie installed "Pom!" beta\x01",
            "version in the terminal.\x07\x00\x02",
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
            "#12P#00104FDone, and...\x02\x03",
            "#00100FI also input the account\x01",
            "Chief Roberts gave us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FEeeh, you're really skillful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FReally. Miss Elie knows\x01",
            "very well a lot of things.\x02\x03",
            "#10100FShe also seems very knowledgeable\x01",
            "even about politics and law.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#11P#00102F*giggle*, in regard to this,\x01",
            "I only watched Tio doing it.\x01\x02\x03",
            "#00104FThere was an instruction\x01",
            "manual too and when I read\x01",
            "it well, it wasn't that difficult.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00002FBut still, you're truly a big help.\x02\x03",
            "#00006FFor instance, I've just finally got\x01",
            "used to the terminal keyboard.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#00109F*giggle*, you're welcome.\x02\x03",
            "#00100FThen...is it alright to\x01",
            "contact Chief Roberts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00000FYeah, let's do it at once.\x02",
    )

    CloseMessageWindow()

    def lambda_66DE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_66DE)
    Sleep(50)

    def lambda_66EE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_66EE)
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
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──Hi, Lloyd. I guess you've\x01",
            "installed it successfully?\x07\x00\x02",
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
            "#00000FYeah, everything went fine.\x01",
            "What should we do next?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Then, would you try\x01",
            "a match against me?\x02\x03",
            "Try starting "Pom!"\x01",
            "from the terminal.\x02\x03",
            "My account should be displayed\x01",
            "over there. If you select that,\x01",
            "you can challenge me.\x02\x03",
            "...Oh, right, since we're here, why\x01",
            "don't you, the Support Section\x01",
            "leader, challenge me?\x07\x00\x02",
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
            "#00005F???\x01",
            "Yes, I understand.\x07\x00\x02",
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
        "#12P#00100FThen, I'll leave you the seat.\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x14, 0x1F4)

    def lambda_69DA():
        OP_9B(0x1, 0xFE, 0xB4, 0x5DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_69DA)
    Sleep(200)

    def lambda_69F2():
        OP_95(0xFE, 15970, 850, 9800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_69F2)

    def lambda_6A0C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6A0C)
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
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hu hu, can you win against\x01",
            "me, its developer...?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4SAre you the man I can entrust little Tio to...?\x01",
            "Let me find it out for sure!#3S\x07\x00\x02",
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
            "#6P#10112F...Somehow it seems we could\x01",
            "hear his true intentions...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10309FAhaha, he seems to be\x01",
            "quite the doting parent, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FEhm, was that the reason why you\x01",
            "asked the Support Section...?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ahaha, no, no...\x01",
            "Since we're having a match,\x01",
            "I thought to fired me up a little.\x02\x03",
            "Then, let's start\x01",
            "the game at once!\x07\x00\x02",
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

    label("loc_6D13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D9B")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D4B")
    Call(0, 20)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D96")

    label("loc_6D4B")


    AnonymousTalk(
        0x101,
        (
            "#0000FChief Roberts is waiting, so\x01",
            "let's try launching "Pom!" now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6D96")

    Jump("loc_6D13")

    label("loc_6D9B")

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

    # Function_21_61F8 end

    def Function_22_6DBF(): pass

    label("Function_22_6DBF")

    EventBegin(0x0)
    SoundLoad(803)
    SoundLoad(128)
    Sound(128, 2, 50, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E43")
    OP_2C(0x6C, 0x1)

    ChrTalk(
        0x101,
        (
            "#6P#00009FAlright, I won somehow...!\x02\x03",
            "#00004F(Uhhm, it was quite fun...)\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6C, 0x1, 0x2)
    Jump("loc_6E99")

    label("loc_6E43")


    ChrTalk(
        0x101,
        (
            "#6P#00006F...I lost, eh?\x02\x03",
            "#00001F(Uhhm, somehow\x01",
            "it's really mortifying...)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6C, 0x1, 0x3)

    label("loc_6E99")


    ChrTalk(
        0x102,
        (
            "#12P#00109F*giggle*, somehow you\x01",
            "looked quite hooked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105F...Excuse me, this is an impression I had\x01",
            "from looking at it as an outsider, but...\x02\x03",
            "#10106FChief Roberts... Could\x01",
            "it be that he's weak?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FRight, although he's the developer, as\x01",
            "far as strength goes, he's not much\x01",
            "different from you, a beginner, eh?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00012FW-Well...\x01",
            "As you'd expect, he was\x01",
            "going easy on me, right?\x02\x03",
            "#00003FThis wouldn't amount as a test that\x01",
            "much if he didn't match his level\x01",
            "to mine to a certain degree...\x02",
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
        "#6P#00000FYes, Special Support Section spea──\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──Myyy, that was a good match!\x01\x02\x03",
            "A do-or-die game that will go down \x01",
            "in history! I'm still excited!!\x07\x00\x02",
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
            "#6P#00006F(It seems he wanted\x01",
            "to play in earnest...)\x02\x03",
            "#00012FS-So... How were\x01",
            "the test results?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ah, they were perfect!\x02\x03",
            "Inside the city there was no\x01",
            "prominent lag and the transmission\x01",
            "signal was satisfactory.\x02\x03",
            "I can surely say that it was a great success.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#6P#00000FIs that so...?\x01",
            "I'm glad for you.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "That was a beta version you installed,\x01",
            "but I will update it to a release version\x01",
            "before long.\x02\x03",
            "When the program distribution will commence,\x01",
            "the people you can challenge will increase too.\x02\x03",
            "I'd be happy if you exchanged the account with\x01",
            "many people and played to your heart's content.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75A6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7539")
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Of course, I too intend to\x01",
            "get my revenge one day!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_75A6")

    label("loc_7539")

    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Of course, I'll take you on whenever\x01",
            "you want to get revenge for today!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_75A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7612")
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Of course, I too intend to\x01",
            "get my revenge one day!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_767F")

    label("loc_7612")

    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Of course, I'll take you on whenever\x01",
            "you want to get revenge for today!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_767F")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00012FH-Ha ha...\x01",
            "Please go easy on me.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, thank you very much\x01",
            "for your cooperation.\x02\x03",
            "I have other work to attend to,\x01",
            "so I'll excuse myself now.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYou're welcome.\x01",
            "Please contact whenever you want\x01",
            "if something else happens.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes, I'll do that.\x01",
            "──Bye then!\x07\x00\x02",
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
            "#00004F*sigh*... Somehow it\x01",
            "seems it went well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100F*giggle*, thank you for your hard work.\x02\x03",
            "#00104FHow should I put it, it really seemed a\x01",
            "request that Chief Roberts would made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FHa ha, right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FIn any case, it appears that we will be\x01",
            "able to enjoy this game from now on.\x02\x03",
            "#10309FAnd so, what about trying\x01",
            "to aim to become a Pom!\x01",
            "master in Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, as you'd expect I'd never\x01",
            "be a match for Tio at all...\x02\x03",
            "#00000FStill, I could practice\x01",
            "while taking a breather\x01",
            "among jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100F*giggle*, you're right.\x02",
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
            "Quest [Beta Test Participation]\x07\x00",
            " completed!\x02",
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

    # Function_22_6DBF end

    def Function_23_7B24(): pass

    label("Function_23_7B24")

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
            "#00104F──Yes.\x01",
            "A few came in.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        "#10100FThese are...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10302FThe "support requests" you deal with\x01",
            "at the Special Support Section, then?\x02",
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
            "#00004FYeah, basically they're sent\x01",
            "to us together once per day.\x02\x03",
            "#00000FIt's left to our discretion\x01",
            "how many to do, but...\x02\x03",
            "Those with "urgent" written\x01",
            "should be done without fail.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10304FIndeed, it's reasonable.\x02\x03",
            "#10300FDoes it mean that if they take too long\x01",
            "you can resume them the next day?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00000FYeah, I guess that will happen.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00104FAt any rate, if we check them every day,\x01",
            "even the displayed period will change.\x02\x03",
            "#00100FAlso, if we check the "Detective Notebook",\x01",
            "we can check their status.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        "#10105FThe Detective Notebook...\x02",
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
            "#12P#10100FIs it the black notebook you now\x01",
            "and then write in it, right, Miss Elie?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        "#5P#00100FYes, this one.\x02",
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
            "#00003FBasically, we write in it when there are some\x01",
            "developments in investigations and requests.\x02\x03",
            "By doing that, it's possible to\x01",
            "keep an eye on multiple cases.\x02\x03",
            "#00000FAlso, the Tactical Orbments──\x01",
            "it can even be used as a manual\x01",
            "regarding the "ENIGMA".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10305FEeh, it's rather useful, right?\x02\x03",
            "#10304FAlthough I have the feeling that one day\x01",
            "even that kind of notebook will be orbalized.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00102FYou're right...\x01",
            "I heard once from Tio they\x01",
            "are researching into that.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10112FUhmm, somehow I'd be against\x01",
            "orbalizing it that much...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00002FReally, I agree that pen and\x01",
            "paper are a better match.\x02",
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
            "#00004F#5P──Well then, this how we do things in the \x01",
            "Support Section, roughly explained.\x02\x03",
            "#00000FFirst, let's check at the terminal the\x01",
            "support requests that we received.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10102FRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10309FHu hu, I look forward to see them.\x02",
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
            "※By inspecting the terminal at the Support Section and\x01",
            "pressing the ○ button, selecting [Check Requests] from\x01",
            "the list in the tab will display the job requests\x01",
            "(Quests) for Lloyd and the others.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※Among the support requests, there are some highly\x01",
            "urgent that need to be carried out absolutely.\x01",
            "Those of that type are marked "urgent" and\x01",
            "completing them will advance the story.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※There is no need to complete the other\x01",
            "support requests at all, but clearing them\x01",
            "will earn you DP and mira. Also, please be\x01",
            "careful if you take too long; they will expire.\x02",
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
    AddItemNumber(0x5, 1)
    AddItemNumber(0x6, 1)
    OP_C9(0x0, 0x1000)
    OP_C9(0x0, 0x200000)
    EventEnd(0x5)
    Return()

    # Function_23_7B24 end

    def Function_24_864B(): pass

    label("Function_24_864B")

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
            "#6P#10103FTwo urgent cases and\x01",
            "two Wanted Monsters...\x02\x03",
            "#10101FSetting aside the ENIGMA II one,\x01",
            "the other seems pretty unique.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PYes, I didn't know that man called Lechter\x01",
            "had come to Crossbell again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FThat young man playing the fool\x01",
            "at the "Schwarz Auktion", right?\x02\x03",
            "#10300FNo matter how he acted, I didn't\x01",
            "think he was an ordinary person.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)

    AnonymousTalk(
        0x101,
        (
            "#00003F...When I trained at Crime Investigations\x01",
            "Section One, I read a file about him.\x02\x03",
            "#00001FSpecial Captain Lechter Arundel, affiliated\x01",
            "to the Imperial Army Intelligence.\x02\x03",
            "It also seems that he has the degree of\x01",
            "Second Secretary of the Imperial government.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        "#10108FSomeone from the secret intelligence...?\x02",
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
            "#00103F#11PHe seems to be an intelligence officer\x01",
            "who is able at political maneuverings. \x02\x03",
            "#00101FSomeone subtle, and perhaps\x01",
            "possessing advanced hidden skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FOr more likely, he's got a lot of potential.\x02\x03",
            "#10302FAt any rate, being an Imperial government\x01",
            "secretary and attached to the army intelligence...\x02\x03",
            "Could mean that he's the confidant of\x01",
            "that famous "Blood and Iron Chancellor"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006F(How can he even know\x01",
            "that circumstance...?)\x02\x03",
            "#00001F──Yeah, according to Section One intel,\x01",
            "he's Chancellor Osborne right-hand man.\x02\x03",
            "It has been confirmed that last year, he came\x01",
            "to visit Crossbell with the Chancellor and they\x01",
            "had informal talks with Chairman Hartmann.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PHe himself said so. \x02\x03",
            "#00106FHe seemed like he was joking, but\x01",
            "who could've thought it was true...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FNo matter how I consider him, he seems a\x01",
            "person that can't be dealt via normal means...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FHu hu, isn't this interesting?\x02\x03",
            "#10300FThat said, our first priority seem to be\x01",
            "support activities inside the city, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00000FYeah, for one Wanted Monster\x01",
            "we'll have to search on a highway,\x01",
            "but let's leave that for later.\x02\x03",
            "#00003F...It's been some months\x01",
            "since Revache's annihilation.\x02\x03",
            "#00001FIt seems certain that some new\x01",
            "movements are taking place steadily\x01",
            "in the underground society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PThe "Heiyue" movements...\x01",
            "And then, the Imperial government actions.\x02\x03",
            "#00101FEven the "Trade Conference" taking place at the\x01",
            "end of the month will have a lot of effects...\x02",
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
        "#6P#10105FThe "Trade Conference"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FIt's an international conference called by the new\x01",
            "mayor where the executive class will gather.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00102F#11PYes──\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)

    AnonymousTalk(
        0x102,
        (
            "#00104FThe new mayor, Dieter Crois.\x02\x03",
            "An international conference related to economy\x01",
            "where he, the sponsor, and heads of state from the\x01",
            "Empire, Republic, Liberl and Remiferia will meet.\x02\x03",
            "#00100FIts official name is "West\x01",
            "Zemuria Trade Conference".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00004FI'd never thought that, immediately after his\x01",
            "assumption of office, he would've called such a\x01",
            "large-scale international conference meeting...\x02\x03",
            "#00000FMaybe it's really just something that\x01",
            "only the President of IBC could do.\x02",
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
            "#6P#10109FI've never met him in person, but\x01",
            "he sounds amazingly capable.\x02\x03",
            "#10102FBy the way, I think you have\x01",
            "met him already, right, Wazy?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#6P#10304FYeah, when I got the letter of recommendation.\x02\x03",
            "#10302FAlthough I was in an independent gang of\x01",
            "youths, to think he gave a juvenile delinquent\x01",
            "a letter of recommendation for a police post...\x02\x03",
            "#10309FHu hu, it shouldn't be me saying it,\x01",
            "but he's too generous of a man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00006FIt's no laughing matter, you know,\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00111F#11P"Uncle" was saying his usual\x01",
            ""Hah hah hah, what an\x01",
            "interesting kid!" and so on...\x02",
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
        "Chief's Voice",
        "Ooh, you're hard at it, eh?\x02",
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

    def lambda_96B6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_96B6)

    def lambda_96C7():
        OP_95(0xFE, 17000, 850, 4000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_96C7)
    SetChrSubChip(0x105, 0x0)
    Sleep(300)
    SetChrSubChip(0x102, 0x1)
    WaitChrThread(0x8, 1)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005FChief Sergei...\x02",
    )

    CloseMessageWindow()
    OP_68(12600, 1850, 6600, 4000)
    MoveCamera(35, 17, 0, 4000)
    OP_92(0x8, 0x39D0, 0x20D0, 0x1F4)
    BeginChrThread(0x101, 3, 0, 25)

    def lambda_974F():
        OP_95(0xFE, 14900, 850, 8400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_974F)
    WaitChrThread(0x8, 1)

    def lambda_976D():
        OP_95(0xFE, 12700, 850, 8400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_976D)
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
            "#01003F#5PAah, relax.\x02\x03",
            "#01000FFundamentally the Support Section is\x01",
            "run with the principle of laissez-faire.\x02\x03",
            "You can do things how you want to\x01",
            "because I won't meddle in them unless\x01",
            "the matters are really serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FI-I see...\x02",
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
            "#6P#10309FAhaha. You're an\x01",
            "understanding boss, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00012F...Uhhmm...\x01",
            "I don't think you can say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00111FIn Chief's case, half the motive\x01",
            "is that it's a bother, right...?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#01004F#5PEh eh, you know me well.\x02\x03",
            "#01002FHowever, today, you'll get an\x01",
            "order from me, exceptionally.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#11PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#11PF-From you Chief...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003F#5PYeah, although it's something that can wait\x01",
            "after you'll be over with support requests.\x02\x03",
            "#01000FI'll have you come to the Police Academy.\x02",
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
        "#00005F#11PTo the Police Academy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FThe place that has even maneuvering grounds,\x01",
            "located midway on the West Crossbell Highway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#5PFor you and Lloyd it's a\x01",
            "well familiar place, right?\x02\x03",
            "#01000FWhen I've taken care of preparations on\x01",
            "my side, I'll contact you via the ENIGMA.\x02\x03",
            "Until then, you can keep patrolling the\x01",
            "city and take care of support requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PUhm...understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F#11PStill, what is it all about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01002F#5PEh eh, you'll have to look forward\x01",
            "to that after you've come.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x8, 0x2328, 0x2648, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#01006F#11PSee you, then.\x01",
            "I'll get in touch with you later.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(10600, 1850, 6600, 3000)

    def lambda_9E1C():
        OP_95(0xFE, 9000, 850, 9800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9E1C)
    WaitChrThread(0x8, 1)

    def lambda_9E3A():
        OP_95(0xFE, 2000, 850, 9800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9E3A)
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
        "#6P#10105FEeehm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PMiss Noｱl...\x01",
            "I feel terribly sorry, but this\x01",
            "is the Support Section style.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FWell, thinking about it favorably,\x01",
            "it fosters our independence\x01",
            "and discernment, but still...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10109FI-Indeed! I could expect nothing \x01",
            "less from Chief Sergei!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHu hu, it's not what you say, but how you say it.\x02\x03",
            "#10302FSo?\x01",
            "Do we hit the city at once?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00004FYeah, let's do that.\x02\x03",
            "#00005F...By the way, KeA said she\x01",
            "was leaving for Sunday School.\x02\x03",
            "#00000FChief has gone out too. Maybe it\x01",
            "would be better going out together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#11PRight, let's go to 3F\x01",
            "and speak to KeA.\x02",
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

    # Function_24_864B end

    def Function_25_A1B4(): pass

    label("Function_25_A1B4")

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

    # Function_25_A1B4 end

    def Function_26_A1D8(): pass

    label("Function_26_A1D8")

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
            "#01006F#5PIt looks like it's going\x01",
            "to drizzle all day long.\x02\x03",
            "#01000FSeems it's going to be a little stormy tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIs that so...?\x02\x03",
            "#00000FBecause we have been granted an\x01",
            "orbal car, I thought to try taking it\x01",
            "for a brief patrol in the outskirts too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWell, it doesn't feel like\x01",
            "driving weather for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FUuh...what a pity.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PBy the way...isn't there a follow\x01",
            "up report on the person we met\x01",
            "yesterday on the highway yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003F#5PYeah, it appears that not even Section\x01",
            "One was capable to check on him.\x02\x03",
            "#01001FCao, that guy named Lechter... All folks\x01",
            "you can't deal with in an ordinary way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FYes...\x02\x03",
            "#00006F...The man we met yesterday was clad\x01",
            "in an extremely dangerous air.\x02\x03",
            "#00001FHe was calm, but, how should I say it, he\x01",
            "had a mysterious ferociousness in him...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10103FTruly... He had the air\x01",
            "like that of a tiger.\x02\x03",
            "#10101FHe looked like that if he had wanted he could\x01",
            "have attacked and eaten us in an instant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12PIt's not a pleasant metaphor,\x01",
            "but the air he had was really that.\x02\x03",
            "#00108FA terrorist, or maybe a jaeger...\x01",
            "Both are likely possibilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10308FHmm...\x02\x03",
            "#10304FIn that case, it could be good collecting\x01",
            "intelligence in the Downtown area.\x02\x03",
            "#10300FI feel like the female owner of "Neinvalli"\x01",
            "could know many things.\x02",
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
            "#00005F#11PMiss Ashley from the exchange shop?\x02\x03",
            "#00001FBeing a weapons dealer it appears she knows\x01",
            "many things about the underground world...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#11PTrue, in that regard it seems it\x01",
            "will be worthy paying her a visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#5PWell, best of luck to you.\x02\x03",
            "#01000FHowever, don't forget about\x01",
            "your support requests.\x02\x03",
            "If you strain your mind too much on\x01",
            "counterespionage, you'll lose sight\x01",
            "of your own duties, you know?\x02",
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
        "#00005FU-Understood.\x02",
    )

    CloseMessageWindow()
    OP_92(0x8, 0x39D0, 0x20D0, 0x1F4)
    OP_68(14900, 1850, 6600, 3000)

    def lambda_AA70():
        OP_95(0xFE, 14900, 850, 8400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AA70)
    WaitChrThread(0x8, 1)

    def lambda_AA8E():
        OP_95(0xFE, 18000, 850, 4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AA8E)
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

    def lambda_AAE7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AAE7)

    def lambda_AAF8():
        OP_95(0xFE, 19500, 850, 4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AAF8)
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
            "#5P#00006F...For now, let's check the support\x01",
            "requests at the terminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, let's.\x02",
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

    # Function_26_A1D8 end

    def Function_27_AC6B(): pass

    label("Function_27_AC6B")

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
            "#00000F#6PThe urgent requests are\x01",
            "all inside Crossbell City.\x02\x03",
            "#00004FSince there're this many, it should\x01",
            "be good to take care of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12PThe Foundation request could\x01",
            "be related to Tio...\x02\x03",
            "#00102FIf possible, I'd also would like to\x01",
            "hear about little Momo's request too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10100FThen, let's visit the exchange shop in Downtown\x01",
            "while taking care of the urgent requests, alright?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AE9F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AE9F)
    Sleep(100)

    def lambda_AEAF():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AEAF)
    Sleep(50)

    def lambda_AEBF():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AEBF)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00002F#5PYeah, let's do like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, it's also raining outside,\x01",
            "so let's do them taking our time.\x02",
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

    # Function_27_AC6B end

    def Function_28_AFA2(): pass

    label("Function_28_AFA2")

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
            "#00003F#5PThe very urgent ones came from\x01",
            "the CGF and St. Ursula...\x02\x03",
            "#00002FStill, to be called from\x01",
            "that Instructor Douglas...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#00105F#11PInstructor Douglas?\x01",
            "He has become the CGF Vice Commander, right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B23C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B23C)
    Sleep(100)

    def lambda_B24C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B24C)
    Sleep(50)

    def lambda_B25C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B25C)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x101,
        (
            "#00004F#5PYeah, before becoming Vice Commander\x01",
            "he was an instructor at the Police Academy.\x02\x03",
            "#00000FHe strictly drilled into me hand to hand\x01",
            "combat for physical fitness and\x01",
            "suppression techniques with tonfas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FOriginally, he was someone they put lot\x01",
            "of expectations on, as the CGF hope.\x02\x03",
            "#10106FHowever, he was adverse to the former CGF\x01",
            "Commander and he was given a do-nothing job...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FHe took care of my practice too.\x01",
            "He's an absurdly tough guy.\x02\x03",
            "#00302FFor fightin' strength, I guess\x01",
            "he could be the CGF's No. 1?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B48F():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B48F)
    Sleep(50)

    def lambda_B49F():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B49F)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x102,
        (
            "#00104F#11PI see...\x01",
            "He seems a very amazing person.\x02\x03",
            "#00100FThinking about his relationship with\x01",
            "the CGF I'd like to meet him once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PYeah, let's go greet him with the occasion.\x02\x03",
            "#00003FThen, this is from a new appointed\x01",
            "professor at St. Ursula...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FThe one who inherited both the pharmacology\x01",
            "and neurology departments in Joachim's stead...\x02\x03",
            "#00301FWell, no matter what, I'd be vigilant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FStill, this "Seiland"... It's like\x01",
            "I heard the name somewhere.\x02\x03",
            "#10300FIf I remember correctly, isn't it\x01",
            "a famous name in Remiferia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#11PThere's a place called "Seiland Corporation", a\x01",
            "medical treatments manufacturer of Remiferia.\x02\x03",
            "It's a distinguished family with ties even to the\x01",
            "Archduke's one. Someone related to, maybe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PUhhm, if that's the case then it seems\x01",
            "someone not that much suspicious...\x02\x03",
            "#00001F──Oh, well.\x01",
            "We have to go to St. Ursula since it appears\x01",
            "this person wants to talk about that drug too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10309FHu hu, it also seems there will\x01",
            "be the "sister" you look up to.\x02\x03",
            "#10302FThe girl to whom the nurse uniform\x01",
            "suits her so amazingly that she\x01",
            "looks like a holy saint, right...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_B95A():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B95A)
    Sleep(250)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00005F#5PWha...!?\x02\x03",
            "#00012FW-Well, I've been indebted to\x01",
            "sister Cecil since long ago and...\x02\x03",
            "#00011F──Wait, Wazy!? You never\x01",
            "met her, how can you know!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00309FMy bad, my bad, I told 'im.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00013F#5PKh, Randy...you!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00111F#11P(...Lloyd. He's a little too\x01",
            "much disturbed about it.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112F(Looks quite the case...)\x02\x03",
            "#10102F(Although, she's an amazing\x01",
            "person, so I can understand him...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P......*cough*.\x01",
            "Well, leaving that aside.\x02\x03",
            "#00000FBefore meeting with that professor,\x01",
            "I'd like to speak with sister Cecil.\x02\x03",
            "#00008F...Because of the damage Joachim left, I'm worried\x01",
            "about if the hospital is regaining its footing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PYou're right...\x02\x03",
            "#00100FAh, but isn't Shizuku coming\x01",
            "to the city today?\x02\x03",
            "A while ago KeA went to\x01",
            "visit her at the Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PYeah, she said she would've\x01",
            "played all day with Shizuku\x01",
            "and went out in high spirits.\x02\x03",
            "#00002FSince they should be at the Guild,\x01",
            "let's go there if we have time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#11PYes, let's do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10305F"Shizuku" is the daughter of that\x01",
            ""Divine Blade of Wind", right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FYeah, she's almost right\x01",
            "the same age of KeA.\x02\x03",
            "#00302FYou wouldn't believe how nice a kid\x01",
            "the daughter of that stuffy ol' man is.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_BEC8")

    ChrTalk(
        0x109,
        (
            "#6P#10109FHu hu...\x01",
            "Shizuku is adorable.\x02\x03",
            "#10102FFran has met her too,\x01",
            "she was really excited.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF47")

    label("loc_BEC8")


    ChrTalk(
        0x109,
        (
            "#6P#10109FI heard rumors about her. It\x01",
            "seems she's an adorable kid.\x02\x03",
            "#10102FFran has met her too,\x01",
            "she was really excited.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF47")


    ChrTalk(
        0x105,
        (
            "#12P#10300FHu hu, I see.\x02\x03",
            "#10304FIn that case, today we can go greet her with the \x01",
            "occasion of going around every place in Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#11P#10302F──While looking for some movements from\x01",
            "the "Red Constellation" bunch too.\x02",
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

    def lambda_C08F():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C08F)
    Sleep(50)

    def lambda_C09F():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C09F)
    Sleep(50)

    def lambda_C0AF():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C0AF)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00013F#5PWazy...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10101FY-You...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306F...Oh, don't mind it.\x01",
            "The guy's right.\x02\x03",
            "#00303FAlthough they're my relatives, I can\x01",
            "honestly say those guys are no joke.\x02\x03",
            "#00301FIt's also very possible that they were the ones who\x01",
            "rigged the old abandoned mine with explosives.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C1F2():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C1F2)
    Sleep(50)

    def lambda_C202():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C202)
    Sleep(50)

    def lambda_C212():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C212)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00005F#5PRandy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PYou see, you don't have to\x01",
            "take them to task so much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FUncle and Shirley──\x01",
            "I know those two very well.\x02\x03",
            "#00308FI can't really say it for certain, but...\x01",
            "It's likely they tested the Support Section ability.\x02\x03",
            "#00301FHow much capable is the place I, who\x01",
            "abandoned my former home, drifted to, is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#11P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10108FA-And just for that, they...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10303FThey have no malice, then.\x02\x03",
            "#10300FThey're guys who can do such\x01",
            "a thing just out of mere curiosity?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FYeah. That level of traps for\x01",
            "them are at a greetin' level.\x02\x03",
            "#00301FIn that sense, even if I've just come back maybe\x01",
            "I should've looked into their actions alo──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P──All the more, then.\x02\x03",
            "#00008FThe "Red Constellation" are people\x01",
            "we can't leave alone at all.\x02\x03",
            "One day we'll need to ascertain their motive\x01",
            "for coming to visit Crossbell, or their\x01",
            "relationship with the Imperial government.\x02\x03",
            "#00001FHowever...\x01",
            "Only as the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305FLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PWe need you Randy, and we've got\x01",
            "no intention of leaving you alone.\x02\x03",
            "#00001FActing alone, Randy, you stand no\x01",
            "chance of accomplishing something.\x02\x03",
            "And so...\x01",
            "Don't say stuff like you'll act on your own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00308F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10309FHu hu, quite the great\x01",
            "chat-up lines, as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10101FB-But he's right!\x02\x03",
            "Joining strengths together in such times is\x01",
            "what the Special Support Section do, right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#11PYes, of course.\x02\x03",
            "#00100FEven that Cult incident... We joined all\x01",
            "our strengths together and faced it.\x02\x03",
            "Randy, isn't it this time like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304F...Ha ha.\x02\x03",
            "#00302FSorry, seems I've blurted\x01",
            "out some nonsense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah, totally.\x02\x03",
            "#00000FAnyway, we even got a car so,\x01",
            "today let's patrol the outskirts\x01",
            "while dealing with support requests.\x02\x03",
            "Maybe it would be good stretching our legs\x01",
            "even to Tangram Gate and Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C9CD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C9CD)
    Sleep(50)

    def lambda_C9DD():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C9DD)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#00104F#11PYou're right, it's been some time...\x02\x03",
            "#00105FBy the way, Commander Sonya\x01",
            "is at Bellguard Gate, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FYes, she should be.\x02\x03",
            "Although I think she's being busy dealing\x01",
            "with the future Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FMireille should also be there,\x01",
            "it could be nice goin' to say hi.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu...\x01",
            "Then, should we go out?\x02",
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
            "When the party has more than 4 people,\x01",
            "the extra persons are recorded as\x01",
            ""Support Members".\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""Support Members" are on standby outside the battlefield\x01",
            "and occasionally appears in the AT Bar. When their turn\x01",
            "comes, they perform many support actions.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When the enemy ambush you from behind, the formation,\x01",
            ""Support Members" included, is disrupted.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Let's not neglect to prepare equipments\x01",
            "for "Support Members" too!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Switching party members can be performed\x01",
            "from the [TACTICS] option in the camp menu.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Moreover, from the [STATUS] option in\x01",
            "the camp menu you can select the use\x01",
            "of Support Crafts to be ON or OFF.\x07\x00\x02",
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

    # Function_28_AFA2 end

    def Function_29_CE30(): pass

    label("Function_29_CE30")

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

    def lambda_CF13():
        OP_97(0x109, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_CF13)
    Sleep(200)

    def lambda_CF30():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CF30)
    Sleep(200)

    def lambda_CF4D():
        OP_97(0x105, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_CF4D)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    VolumeBGM(0x50, 0x3E8)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_CF88():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_CF88)
    Sleep(400)

    def lambda_CF9C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CF9C)

    def lambda_CFAD():
        OP_96(0xFE, 0x3E8, 0xA, 0x1F4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CFAD)
    Sleep(400)

    def lambda_CFCA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_CFCA)

    def lambda_CFDB():
        OP_96(0xFE, 0x3E8, 0xA, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CFDB)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#00003F#5P──Say, Randy.\x02",
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
        "Uhm? What, Lloyd.\x02",
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
            "#00008F#5PYou know...\x01",
            "About your father...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#12P#00306FAh, that...\x01\x02\x03",
            "#00300FI don't particularly mind it, you know?\x01",
            "It's no rare story in that kind of world.\x02\x03",
            "Also, when I broke away from the group,\x01",
            "I severed ties with my ol' man.\x02\x03",
            "#00304FIt doesn't mean I didn't feel anything, but...\x01",
            "Well, I felt relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P...I see.\x02\x03",
            "#00001FHowever, when you feel like it,\x01",
            "you can tell me everything, okay?\x02\x03",
            "After all, as the leader\x01",
            "there could be things I\x01",
            "can you advice on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00305F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#5PAh, sorry.\x01",
            "Was I a bit impertinent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00304FHa ha, no, no.\x02\x03",
            "#00302FAll things considered, I\x01",
            "thought you've grown up too.\x02\x03",
            "#00309FHmm, your big bro here is deeply moved.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_D5BB")

    ChrTalk(
        0x101,
        "#00006F#5PHey now...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00008F#5P...It's just...that I'd want to be\x01",
            "of help to you in such moments.\x02\x03",
            "#00000FMaybe I'm not so reliable, but that's\x01",
            "what means to be "buddies", right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00305FLloyd...\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    Sleep(300)
    SetCameraDistance(22000, 1000)

    def lambda_D4BC():
        OP_96(0xFE, 0x3E8, 0x0, 0x4E2, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D4BC)
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
            "#12P#00302F...Alright, got it. Maybe one\x01",
            "day I'll tell you everything.\x02\x03",
            "#00309FI'll count on you when that time comes──buddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PYeah...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_D655")

    label("loc_D5BB")


    ChrTalk(
        0x101,
        "#00006F#5PHey now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00304F...Well, if I feel like it I\x01",
            "could ask you for advice.\x02\x03",
            "#00300FI'll count on you, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PYeah...!\x02",
    )

    CloseMessageWindow()

    label("loc_D655")

    SetChrPos(0x102, 1500, -1000, -4000, 180)
    SetChrPos(0x105, 500, -1000, -4000, 180)

    NpcTalk(
        0x105,
        "Wazy's Voice",
        "#1P#2SOh, what're you doing?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x102,
        "Elie's Voice",
        "#1P#2SDid you forget something?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_D75D")
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

    def lambda_D744():
        OP_96(0xFE, 0x3E8, 0x0, 0x2EE, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D744)
    WaitChrThread(0x104, 1)

    label("loc_D75D")


    def lambda_D762():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D762)

    ChrTalk(
        0x101,
        "#00011F#5PSorry, we'll be there immediately!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00304FAlright then, let's begin our\x01",
            "work in a nice and relaxed way.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x3E8)

    def lambda_D7F4():
        OP_97(0x104, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D7F4)
    Sleep(100)

    def lambda_D811():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D811)
    FadeToDark(1000, 0, -1)
    Sleep(400)

    def lambda_D838():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D838)
    Sleep(400)

    def lambda_D84C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D84C)
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
            "You are now able to move everywhere\x01",
            "in Crossbell via orbal car.\x02\x03",
            "It is parked at the Special Support Section back\x01",
            "entrance facing West Street. Please try using it.\x07\x00\x02",
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

    # Function_29_CE30 end

    def Function_30_D97B(): pass

    label("Function_30_D97B")

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

    def lambda_DA5E():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DA5E)
    Sleep(200)

    def lambda_DA7B():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_DA7B)
    Sleep(200)

    def lambda_DA98():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_DA98)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    VolumeBGM(0x50, 0x3E8)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_DAD3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_DAD3)
    Sleep(400)

    def lambda_DAE7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DAE7)
    Sleep(400)

    def lambda_DAFB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_DAFB)

    def lambda_DB0C():
        OP_96(0xFE, 0xFFFFF448, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DB0C)
    Sleep(300)

    def lambda_DB29():
        OP_96(0xFE, 0xFFFFFA24, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DB29)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00003F#11P──Say, Randy.\x02",
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
        "Uhm? What, Lloyd.\x02",
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
            "#00008F#11PYou know...\x01",
            "About your father...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00306FAh, that...\x01\x02\x03",
            "#00300FI don't particularly mind it, you know?\x01",
            "It's no rare story in that kind of world.\x02\x03",
            "Also, when I broke away from the group,\x01",
            "I severed ties with my ol' man.\x02\x03",
            "#00304FIt doesn't mean I didn't feel anything, but...\x01",
            "Well, I felt relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P...I see.\x02\x03",
            "#00001FHowever, when you feel like it,\x01",
            "you can tell me everything, okay?\x02\x03",
            "After all, as the leader\x01",
            "there could be things I\x01",
            "can you advice on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#11PAh, sorry.\x01",
            "Was I a bit impertinent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FHa ha, no, no.\x02\x03",
            "#00302FAll things considered, I\x01",
            "thought you've grown up too.\x02\x03",
            "#00309FHmm, your big bro here is deeply moved.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_E10F")

    ChrTalk(
        0x101,
        "#00006F#11PHey now...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00008F#11P...It's just...that I'd want to be\x01",
            "of help to you in such moments.\x02\x03",
            "#00000FMaybe I'm not so reliable, but that's\x01",
            "what means to be "buddies", right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305FLloyd...\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    SetCameraDistance(22000, 1000)

    def lambda_E010():
        OP_96(0xFE, 0xFFFFF736, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E010)
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
            "#6P#00302F...Alright, got it. Maybe one\x01",
            "day I'll tell you everything.\x02\x03",
            "#00309FI'll count on you when that time comes──buddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11PYeah...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E1AA")

    label("loc_E10F")


    ChrTalk(
        0x101,
        "#00006F#11PHey now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304F...Well, if I feel like it I\x01",
            "could ask you for advice.\x02\x03",
            "#00300FI'll count on you, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PYeah...!\x02",
    )

    CloseMessageWindow()

    label("loc_E1AA")

    SetChrPos(0x102, -7000, -2000, 68300, 270)
    SetChrPos(0x105, -7000, -2000, 67300, 270)

    NpcTalk(
        0x105,
        "Wazy's Voice",
        "#2P#2SOh, what're you doing?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x102,
        "Elie's Voice",
        "#2P#2SDid you forget something?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_E2B2")
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

    def lambda_E299():
        OP_96(0xFE, 0xFFFFF542, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E299)
    WaitChrThread(0x104, 1)

    label("loc_E2B2")


    def lambda_E2B7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E2B7)

    ChrTalk(
        0x101,
        "#00011F#11PSorry, we'll be there immediately!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00304FAlright then, let's begin our\x01",
            "work in a nice and relaxed way.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x3E8)

    def lambda_E34B():
        OP_97(0x104, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E34B)
    Sleep(100)

    def lambda_E368():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E368)
    FadeToDark(1000, 0, -1)
    Sleep(400)

    def lambda_E38F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E38F)
    Sleep(400)

    def lambda_E3A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E3A3)
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
            "You are now able to move everywhere\x01",
            "in Crossbell via orbal car.\x02\x03",
            "It is parked at the Special Support Section back\x01",
            "entrance facing West Street. Please try using it.\x07\x00\x02",
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

    # Function_30_D97B end

    def Function_31_E4D2(): pass

    label("Function_31_E4D2")

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
            "#00003F──I see, the Trade Conference is\x01",
            "going to start in earnest tomorrow.\x02",
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
            "#5P#01003FYeah, for the day there're going to be all\x01",
            "sort of informal talks at luncheon meetings.\x02\x03",
            "#01002FIt appears that in the evening, in\x01",
            "addition to a dinner party, they're\x01",
            "going to the Arc-en-ciel theater.\x02\x03",
            "By the way, all heads of state are planned\x01",
            "to spend the night at Michelam guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FFor guest house you mean the former\x01",
            "Chairman, Hartmann's mansion, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305FEeh, that ridiculously huge mansion\x01",
            "is bein' used like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01006FWell, the absurd sum of the fine\x01",
            "to Hartmann for his corruptions and\x01",
            "illegal dealings amounted to its value.\x02\x03",
            "#01000FSo it was confiscated as compensation\x01",
            "and it's been used as a guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FUhhm... Well, I guess\x01",
            "he reaped what he sowed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FSo, it goes without saying that\x01",
            "Michelam area is sealed, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01003FYeah, for the Trade Conference duration even\x01",
            "the hotel and theme park are temporarily closed.\x02\x03",
            "#01002FThe CGF has been stationed\x01",
            "there, so no need to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PI understand.\x02\x03",
            "#00000FWe will focus on support activities\x01",
            "continuing from yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01004FWell, I don't mind.\x02\x03",
            "#01000FAfter the dinner party it's likely\x01",
            "there will be some among the invitees\x01",
            "who want to visit Crossbell.\x02\x03",
            "Some trouble could arise, so you\x01",
            "should probably help in that regard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FAt any rate, those invitees really\x01",
            "didn't have a normal aura at all.\x02\x03",
            "#00301FEspecially the "Blood and Iron Chancellor"...\x01",
            "That one was no ordinary man, I tell you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah, even that Captain Lechter\x01",
            "drew my attention, but...\x02\x03",
            "#00008FThe Chancellor himself had\x01",
            "a further overwhelming air.\x02\x03",
            "#00001FPresident Rocksmith of the Republic\x01",
            "had a friendly air, though...\x02\x03",
            "#00005F...However, immediately next to\x01",
            "him there was that Miss Kilika.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)

    ChrTalk(
        0x102,
        (
            "#00103FSomeone from the "Rocksmith Agency",\x01",
            "Calvard's secret intelligence organization...\x02\x03",
            "#00108FA President well known among the common\x01",
            "people faction...we can't deal with him normally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10102FHowever, Princess Klaudia of Liberl had\x01",
            "really an aura of dignity around her.\x02\x03",
            "#10109FAnd Captain Julia who was accompanying\x01",
            "her was amazingly cool!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#6P#10305FOh, that female captain of the Liberl\x01",
            "Kingdom Royal Guards, right?\x02\x03",
            "#10302FIt seems that due to her status and\x01",
            "looks she's got some zealous fans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10112FY-Yes...so it seems.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FAhaha...\x01",
            "I'm a bit of a fan too.\x02",
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
        "#5P#00005FEeh, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FWhat, what?\x01",
            "Milady, do you have those kind of tastes?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#00102FNot at all, however...\x02\x03",
            "#00104FYou see, when I sojourned in Liberl\x01",
            "before, I saw the Royal Guards parade...\x02\x03",
            "#00100FAfter they even published a photo album, \x01",
            "I ended up buying it unconsciously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00012FI-I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10101FPlease, show it to me later!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#00109FAhaha...\x01",
            "Yes, okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FOh boy, what a pity.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHu hu, a belle disguised as\x01",
            "a man is a type of fantasy.\x02\x03",
            "#10302FAs for me, I was quite interested into\x01",
            "the Imperial Highness, Prince Olivert.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F#11PPrince Olivert, eh...?\x01",
            "A name you hear often, as of late.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)

    ChrTalk(
        0x102,
        (
            "#00104FHe's a famous person because he had\x01",
            "a role in solving Liberl's incident.\x02\x03",
            "#00100FAfter that he attended many meetings\x01",
            "and it seems he became popular...\x02\x03",
            "If I remember correctly, he doesn't have the\x01",
            "right of succession to the imperial throne.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5P#00001FReally...?\x02\x03",
            "#00005FOh, if he had a role in solving\x01",
            "Liberl's incident, could it mean...\x02\x03",
            "#00000FThat he's Estelle and\x01",
            "Joshua's acquaintance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FYes, now that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FThose two know a lot of\x01",
            "people, so it could be.\x02",
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
        "KeA's Voice",
        "#3605V#30W#12AWe're hooome.\x02",
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

    def lambda_F9B6():
        OP_96(0xFE, 0x3E8, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F9B6)

    def lambda_F9D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_F9D0)
    Sleep(1000)

    def lambda_F9E4():
        OP_96(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F9E4)

    def lambda_F9FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F9FE)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)

    def lambda_FA17():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_FA17)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x5A, 0x1F4)
    SetChrSubChip(0xA, 0x5)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00002FKeA, Zeit, welcome back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6P#01200FWoof.\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)

    def lambda_FA76():
        OP_96(0xFE, 0x3E8, 0x352, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_FA76)
    Sleep(1000)
    Fade(1000)
    OP_68(10600, 1850, 6600, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    OP_68(12600, 1850, 6600, 3000)
    EndChrThread(0x9, 0x1)
    SetChrPos(0x9, 5000, 850, 8900, 90)

    def lambda_FAEC():
        OP_96(0xFE, 0x2AF8, 0x352, 0x22C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_FAEC)
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
            "#00105FOh, weren't you\x01",
            "with Shizuku?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01106F#5PAh, yes, she went back to\x01",
            "the hospital with her father.\x02\x03",
            "#01110FBut we saw the building\x01",
            "inauguration together!\x02\x03",
            "#01109FIt was amazing!\x01",
            "You saw it too from nearby, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, honestly it was too\x01",
            "big that I'm not so sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300F#NWell, what we're sure of is that it's\x01",
            "too much of an amazing place.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#6P#10109FHu hu, it's possible that\x01",
            "KeA saw it perfectly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01109F#5PYes!\x01",
            "It was super cool!\x02\x03",
            "#01110FFireworks...were they?\x01",
            "Those too were super pretty!\x02\x03",
            "#01102FBut...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)

    ChrTalk(
        0x101,
        "#00005FHm? What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01104F#5PAh, no, it's nothing.\x02\x03",
            "#01100FAre you going out for\x01",
            "work again now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I think we're going to be back in the evening.\x02\x03",
            "Chief, what about you?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5P#01003FToday, I'll remain here on standby.\x02\x03",
            "#01002FIf something happens I'll call you,\x01",
            "so go out without worrying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004FYes, we'll take up on your kind offer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FLet's go out after we\x01",
            "check the terminal.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1009C")
    Jump("loc_100A1")

    label("loc_1009C")

    OP_29(0x73, 0x4, 0x40)

    label("loc_100A1")

    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_31_E4D2 end

    def Function_32_100A7(): pass

    label("Function_32_100A7")

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
            "#00001F#5PMany came in...\x01",
            "And all worry me.\x02\x03",
            "#00006FAlthough I don't quite understand\x01",
            "this "Search for Musician" one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FWeeell, who would've thought to receive\x01",
            "a request from the Bracer ladies, huh?\x02\x03",
            "#00302FThere's nothing sexy about trainin',\x01",
            "but I'd like to drop by if time allows it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10104FHu hu, it could be a nice opportunity.\x02\x03",
            "#10100FAnd this search for a cat seems\x01",
            "to come from that family...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10308():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10308)

    def lambda_10315():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_10315)
    Sleep(50)

    def lambda_10325():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10325)

    def lambda_10332():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_10332)
    WaitChrThread(0x101, 2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_103F5")

    ChrTalk(
        0x101,
        (
            "#00002F#5PYeah, it's from Mr. Bond's place.\x01",
            "They moved to East Street.\x02\x03",
            "#00004FWe have a connection with that cat too, so...\x01",
            "If possible, I'd want to help them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1048B")

    label("loc_103F5")


    ChrTalk(
        0x101,
        (
            "#00002F#5PYeah, it's from Mr. Bond's place.\x01",
            "They moved to East Street.\x02\x03",
            "#00003FIt seems they have it hard...\x01",
            "If possible, I'd want to help them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1048B")


    ChrTalk(
        0x102,
        (
            "#00104F#11PRight, I agree with you.\x02\x03",
            "#00100FIt seems they're counting on us,\x01",
            "so let's not forget to visit them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHu hu, it appears that the city\x01",
            "is enlivened due to the tower \x01",
            "inauguration and the VIPs visit.\x02\x03",
            "#10302FGoing around many\x01",
            "places could be fun.\x02",
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

    # Function_32_100A7 end

    def Function_33_105E8(): pass

    label("Function_33_105E8")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10719")
    OP_68(1300, 1850, 11800, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    OP_90(0x101, 1700, 4850, 14100, 180)
    OP_90(0x102, 600, 4850, 14400, 180)
    OP_90(0x104, 1700, 4850, 15400, 180)
    OP_90(0x109, 600, 4850, 15700, 180)
    OP_90(0x105, 1700, 4850, 16700, 180)
    Jump("loc_1079C")

    label("loc_10719")

    OP_68(1000, 1000, 700, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x101, 300, 0, -1600, 0)
    SetChrPos(0x102, 1400, 0, -1900, 0)
    SetChrPos(0x104, 300, 0, -2900, 0)
    SetChrPos(0x109, 1400, 0, -3200, 0)
    SetChrPos(0x105, 300, 0, -4200, 0)

    label("loc_1079C")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10839")
    OP_68(1300, 1850, 9800, 3500)
    BeginChrThread(0x101, 3, 0, 34)
    Jump("loc_108D8")

    label("loc_10839")

    OP_68(1000, 1000, 2700, 3500)

    def lambda_1084F():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1084F)
    Sleep(200)

    def lambda_1086C():
        OP_97(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1086C)
    Sleep(200)

    def lambda_10889():
        OP_97(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10889)
    Sleep(200)

    def lambda_108A6():
        OP_97(0x109, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_108A6)
    Sleep(200)

    def lambda_108C3():
        OP_97(0x105, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_108C3)

    label("loc_108D8")

    FadeToBright(1000, 0)

    def lambda_108E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_108E6)
    Sleep(400)

    def lambda_108FA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_108FA)
    Sleep(600)

    def lambda_1090E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1090E)
    Sleep(400)

    def lambda_10922():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_10922)
    Sleep(600)

    def lambda_10936():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_10936)
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A34")

    ChrTalk(
        0x101,
        "#5P#00002FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00109FMy...\x01",
            "What a great aroma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10302FYes, it seems to\x01",
            "be maple syrup.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10AA4")

    label("loc_10A34")


    ChrTalk(
        0x101,
        "#00002F#5POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#11PMy...\x01",
            "What a great aroma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FYes, it seems to\x01",
            "be maple syrup.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10AA4")

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

    def lambda_10AE8():
        OP_95(0xFE, 10810, 850, 11410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10AE8)

    def lambda_10B02():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_10B02)
    WaitChrThread(0x9, 1)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10BAB")
    SetChrPos(0x101, 1700, -850, 9100, 180)
    SetChrPos(0x102, 600, -850, 9400, 180)
    SetChrPos(0x104, 1700, -850, 10400, 180)
    SetChrPos(0x109, 600, -850, 10700, 180)
    SetChrPos(0x105, 1700, -850, 11700, 180)

    label("loc_10BAB")


    def lambda_10BB0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_10BB0)
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
            "#3606V#30WAh, Lloyd, guys, you really\x01",
            "came back as I thought.\x02",
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
            "#00009FYeah, to rest a little.\x02\x03",
            "#00000FBy the way...\x01",
            "Were you baking muffins?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D53")

    ChrTalk(
        0x9,
        (
            "#01104F#11PEhehe...somehow I had a hunch\x01",
            "you would've come back home...\x02\x03",
            "#01110FThey're maple muffins.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DBE")

    label("loc_10D53")


    ChrTalk(
        0x9,
        (
            "#01104F#5PEhehe...somehow I had a hunch\x01",
            "you would've come back home...\x02\x03",
            "#01110FThey're maple muffins.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10DBE")


    ChrTalk(
        0x104,
        (
            "#00305FOoh... Keddo, ain't\x01",
            "you considerate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FHu hu, how pleasant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FSince we're here,\x01",
            "let's pour some tea.\x02",
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
            "#5P#01005F──I see.\x01",
            "You came across them in such a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PYes, it didn't seem they had\x01",
            "anything in mind, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F...Are there no "Red Constellation"\x01",
            "movements as usual?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01004FIf something happens, Section\x01",
            "One will contact us here.\x02\x03",
            "#01002FIt's not that I don't get how you feel,\x01",
            "but, well, don't be so impatient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00304FHa ha...got it.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#11PWell, I'm not only concerned\x01",
            "about the "Red Constellation".\x02\x03",
            "#00001FAt any rate, let's patrol paying attention\x01",
            "if there're any kind of signs or not.\x02",
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
            "#6P#00108FRight...\x01",
            "With the VIPs visiting it would\x01",
            "be awful if something happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FIf we have the time, let's patrol\x01",
            "the outskirts too with the car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#01105FGuys, are you leaving again?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)

    ChrTalk(
        0x101,
        (
            "#00004F#11PYeah, we're returning to work.\x02\x03",
            "#00002FThank you for the muffins.\x01",
            "They were really delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00109F*giggle*, you have become more\x01",
            "skilled at cooking than any of us.\x02\x03",
            "#00102FDid you perhaps learn how to\x01",
            "make them from Mr. Oscar?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)
    Sleep(150)

    ChrTalk(
        0x9,
        "#6P#01109FEhehe, exactly.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#6P#01110FOh, there're still some left,\x01",
            "eat them if you please.\x02\x03",
            "I think they'll still be\x01",
            "good until tomorrow.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x20F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x5 received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x20F, 5)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        "#10302FEeh, you're thoughtful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FKuuuuh...\x01",
            "Your father is gonna cry!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#5P...Wait right there.\x02\x03",
            "#00013FNo matter if it's you Randy, I won't \x01",
            "hand you KeA's father role to you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#00302FHmph, how interesting.\x01",
            "Wanna rival with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#01105FHoee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106F*sigh*...\x01",
            "What're you rivaling for...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10112FAhaha... \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FThere're some serious\x01",
            "doting parents in this place.\x02",
        )
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

    # Function_33_105E8 end

    def Function_34_11C85(): pass

    label("Function_34_11C85")


    def lambda_11C8A():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11C8A)
    Sleep(200)

    def lambda_11CA7():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_11CA7)
    Sleep(200)

    def lambda_11CC4():
        OP_97(0x104, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_11CC4)
    Sleep(200)

    def lambda_11CE1():
        OP_97(0x109, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_11CE1)
    Sleep(200)

    def lambda_11CFE():
        OP_97(0x105, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_11CFE)
    Return()

    # Function_34_11C85 end

    def Function_35_11D14(): pass

    label("Function_35_11D14")

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

    def lambda_11E83():
        OP_95(0xFE, 11000, 850, 12300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11E83)

    def lambda_11E9D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_11E9D)
    WaitChrThread(0x9, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(300)

    def lambda_11ECE():
        OP_95(0xFE, 14100, 850, 12300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11ECE)
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
            "#01110F#3607V#30WUhm...hallo?\x02\x03",
            "#01109F#3608VThis is Crossbell Police,\x01",
            "Special Support Sectiooon.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE18)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ah...is it you, KeA?\x02",
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
            "#01105FOh, it's Tio!\x02\x03",
            "#01109FYou called again.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Eh eh, although it's via normal\x01",
            "orbal phone unlike yesterday.\x02\x03",
            "...Could it be that\x01",
            "no one is there?\x02",
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
            "#01100FYes, even Chief has\x01",
            "gone out some time ago.\x02\x03",
            "Although Zeit is here.\x02",
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
            "#01200FWoof.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hm, I see.\x02\x03",
            "...Actually, I can't connect to\x01",
            "Mr. Lloyd and the others' ENIGMAs.\x02\x03",
            "And so I contacted the\x01",
            "Support Section directly.\x02",
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
            "#01105FEeeh, is that so.\x02\x03",
            "#01111FLloyd and the others seem\x01",
            "to have been called by a pure\x01",
            "white falcon and went out.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A pure white falcon...?\x02",
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
            "#01110FYes, he said his name is\x01",
            "Sieg and talks like Zeit.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...Somehow it appears that\x01",
            "many things are going on.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(801, 0, 50, 0)
    Sleep(1300)
    SetMessageWindowPos(250, 0, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#1S#40W...everyone.\x01",
            "Sorry for the long wait.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#1S#40WNow...for...\x01",
            "Leman...\x02",
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
            "#01105F???\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──It seems it is time to go.\x02\x03",
            "KeA, I will call you later.\x01",
            "Please tell Mr. Lloyd, the others\x01",
            "and Chief that I said hi.\x02",
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
            "#01109FYes, later!\x02",
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
            "#01200FWoof.\x02",
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
        "Sergei's Voice",
        "Hey, I'm back.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1253D():

        label("loc_1253D")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1253D")

    QueueWorkItem2(0x9, 2, lambda_1253D)
    OP_68(1960, 1750, 2650, 2500)
    MoveCamera(40, 17, 0, 2500)
    Sleep(2000)

    def lambda_1256E():
        OP_95(0xFE, 1000, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1256E)

    def lambda_12588():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_12588)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x2D, 0x1F4)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#01101F#12PAh, Chief.\x02\x03",
            "#01106FIf you had come back faster,\x01",
            "you could've spoken to Tio!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01005F#6POh, did she call?\x02\x03",
            "#01002FSo, what did she say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01110F#12PWell, you see...\x02",
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

    # Function_35_11D14 end

    def Function_36_126AB(): pass

    label("Function_36_126AB")


    def lambda_126B0():
        OP_95(0xFE, 1000, 850, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_126B0)
    WaitChrThread(0x8, 1)

    def lambda_126CE():
        OP_95(0xFE, 10000, 850, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_126CE)
    WaitChrThread(0x8, 1)
    Return()

    # Function_36_126AB end

    def Function_37_126E8(): pass

    label("Function_37_126E8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetScenarioFlags(0x141, 5)
    OP_29(0xA3, 0x1, 0x14)
    OP_29(0xA3, 0x1, 0x15)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_12714")
    Jump("loc_12719")

    label("loc_12714")

    OP_29(0x75, 0x4, 0x40)

    label("loc_12719")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1272A")
    Jump("loc_1272F")

    label("loc_1272A")

    OP_29(0x76, 0x4, 0x40)

    label("loc_1272F")

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
            "#6P#00003F...As expected, some\x01",
            "new ones have arrived.\x02\x03",
            "#00001FHmm, they all\x01",
            "worry me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00104FIf we have the time,\x01",
            "let's stop by.\x02\x03",
            "#00100FIt appears that we can\x01",
            "act freely in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FAnd if we use the car, we\x01",
            "can move to the outskirts too.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12A39():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_12A39)
    WaitChrThread(0x103, 2)
    Sleep(150)

    ChrTalk(
        0x103,
        (
            "#00204F#5PCar...?\x01",
            "I'm looking forward to it.\x02\x03",
            "#00202FIt seems it's a model\x01",
            "developed by ZCF?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FYeah, it's a new model that seems it can\x01",
            "even put to shame that of Section One.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FBut still, Tio, you just arrived\x01",
            "yesterday, are you alright moving\x01",
            "since early in the morning?\x02\x03",
            "#00000FIf you want, you could take\x01",
            "it easy during the morning──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#5P*glare*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006FSorry, it wasn't on purpose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#5P...Honestly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FHa ha, somehow it really\x01",
            "feels that peTiote is back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00109F*giggle*...right.\x02\x03",
            "#00102FI really feel that Tio\x01",
            "is a better match\x01",
            "for the terminal.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12CCA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_12CCA)
    Sleep(50)

    def lambda_12CDA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_12CDA)
    WaitChrThread(0x109, 2)

    ChrTalk(
        0x109,
        (
            "#12P#10109FHu hu, everyone,\x01",
            "you really are in sync.\x02\x03",
            "#10102FFor the time being...\x01",
            "These are all the members of the\x01",
            "rebirthed Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PHu hu, aren't you deeply\x01",
            "moved as the leader?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FYeah...that's right.\x02\x03",
            "#00002F──At any rate, Tio, it's\x01",
            "nice to work with you again.\x02\x03",
            "And also, thank you for having come back\x01",
            "on purpose to help us in our time of need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#5PYes, on my end too it is nice\x01",
            "to be working with you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FHa ha, somehow \x01",
            "we're all excited, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#01004F#5PEh eh... What's important\x01",
            "is that you're into gear.\x02\x03",
            "#01002FWell, with that energy you\x01",
            "won't get beaten down by\x01",
            "the Trade Conference mood.\x02\x03",
            "Just be useful to the police by\x01",
            "doing things in your own way.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12FE2():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12FE2)
    Sleep(50)

    def lambda_12FF2():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_12FF2)
    Sleep(50)

    def lambda_13002():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_13002)
    Sleep(50)

    def lambda_13012():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_13012)
    Sleep(50)

    def lambda_13022():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_13022)
    Sleep(50)

    def lambda_13032():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_13032)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    def lambda_13057():

        label("loc_13057")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_13057")

    QueueWorkItem2(0x101, 2, lambda_13057)

    def lambda_13069():

        label("loc_13069")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_13069")

    QueueWorkItem2(0x102, 2, lambda_13069)

    def lambda_1307B():

        label("loc_1307B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1307B")

    QueueWorkItem2(0x103, 2, lambda_1307B)

    def lambda_1308D():

        label("loc_1308D")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1308D")

    QueueWorkItem2(0x104, 2, lambda_1308D)

    def lambda_1309F():

        label("loc_1309F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1309F")

    QueueWorkItem2(0x109, 2, lambda_1309F)

    def lambda_130B1():

        label("loc_130B1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_130B1")

    QueueWorkItem2(0x105, 2, lambda_130B1)

    ChrTalk(
        0x101,
        "#12P#00000FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FChief, are you going to be on\x01",
            "standby at police HQ from now on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01006F#5PYeah. They pushed on me negotiation\x01",
            "talks from all quarters, after all.\x02\x03",
            "#01000FI'll be around as backup, but\x01",
            "I won't directly join the police\x01",
            "at Orchis Tower.\x02\x03",
            "However, if something happens\x01",
            "I'll contact you too without fail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003F...Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FIt's nice to work with you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01002F#5PYeah, then I'll go on ahead.\x02",
    )

    CloseMessageWindow()
    OP_92(0x8, 0x2DB4, 0x2AF8, 0x1F4)

    def lambda_132A3():
        OP_95(0xFE, 11700, 850, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_132A3)
    WaitChrThread(0x8, 1)
    OP_68(12900, 1750, 9800, 3000)

    def lambda_132D2():
        OP_95(0xFE, 5700, 850, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_132D2)
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
            "#5P#00005FBy the way...\x01",
            "Has KeA gone to the library?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1339C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1339C)
    Sleep(100)

    def lambda_133AC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_133AC)

    def lambda_133B9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_133B9)
    Sleep(50)

    def lambda_133C9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_133C9)

    def lambda_133D6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_133D6)
    WaitChrThread(0x102, 2)

    ChrTalk(
        0x102,
        (
            "#12P#00104FYes, she went out\x01",
            "first thing in the morning.\x02\x03",
            "#00100FAlthough it seems she'll be back by noon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00002FI see...\x01",
            "Then, everything will be fine, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FAlright, then let's\x01",
            "get out too!\x02",
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
            "Tio has joined the party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can add her to the attack members\x01",
            "from [TACTICS] under the camp menu.\x07\x00\x02",
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

    # Function_37_126E8 end

    def Function_38_13586(): pass

    label("Function_38_13586")

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
    AddItemNumber(0x2FC, 1)
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
            "#11P#00003FThe sandbank at St. Ursula Byroad and\x01",
            "the outskirts of East Crossbell Highway...\x02\x03",
            "#00001FWe didn't stop by both\x01",
            "frequently, as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FIt looks like there's no one like the huge\x01",
            "one at the old abandoned mine, but...\x02\x03",
            "#00301FIt appears it'd better to\x01",
            "be totally prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FAlso...what's specifically\x01",
            "causing them, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PYes...\x02\x03",
            "#00101FIt appears there're also reports saying\x01",
            "that the three higher elements of time,\x01",
            "space and mirage are at work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FRegarding the three higher elements,\x01",
            "I think I will be able to perceive them.\x02\x03",
            "#00208FHowever, as for the "cause"...\x01",
            "It could be a little hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FRight, it appears that the cause regarding\x01",
            "the "Tower" and "Temple" hasn't been figured...\x02\x03",
            "#10305FNow that I think about it, even the "Fort of\x01",
            "Sun" at the Ancient Battlefield was like that?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00006FYeah, when we entered it\x01",
            "was like that for sure, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#5PIt's just that after we solved the incident, they\x01",
            "say that anything abnormal happened anymore.\x02\x03",
            "#00108FThe cause doesn't even seem to be a\x01",
            ""bell" like that one at the "Temple"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FWhen it is so, it appears that locating\x01",
            "what's causing it is going to be hard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FWell, at any rate, \x01",
            "let's get going.\x02\x03",
            "#00300FAfter all, we could've received\x01",
            "some other jobs.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#11P#00003FRight...\x02\x03",
            "#00000FAlright, let's depart after we\x01",
            "check the support requests.\x02",
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

    # Function_38_13586 end

    def Function_39_13DC3(): pass

    label("Function_39_13DC3")

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

    def lambda_13EA2():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_13EA2)
    Sleep(100)

    def lambda_13EB2():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_13EB2)
    Sleep(100)

    def lambda_13EC2():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_13EC2)
    Sleep(100)

    def lambda_13ED2():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_13ED2)
    Sleep(100)

    def lambda_13EE2():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_13EE2)
    Sleep(100)

    def lambda_13EF2():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_13EF2)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00003F#5PAs we thought, quite\x01",
            "a number came in...\x02\x03",
            "#00008FI don't think it's because\x01",
            "Mr. Arios can't move...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11P...Right...\x02\x03",
            "#00108FIt seems that today Chief went\x01",
            "to pay a visit at the hospital...\x02\x03",
            "#00101FIt would be nice to pay a\x01",
            "visit too when we're nearby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FI know, right?\x01",
            "It seems Keddo went yesterday.\x02\x03",
            "#00308F...She was quite down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FYes...\x01",
            "I am a little worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FUsing the car, it won't take that\x01",
            "much going to the hospital...\x02\x03",
            "#10100FIf we have time, let's\x01",
            "go pay a visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PYeah, let's.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FBut still...eye surgery...?\x02\x03",
            "#10301FDon't they say it's \x01",
            "yet a difficult field?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5P...You're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PIt also seems that\x01",
            "this surgery wasn't a\x01",
            "complete failure, however...\x02",
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

    # Function_39_13DC3 end

    def Function_40_14291(): pass

    label("Function_40_14291")

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
            "#5P#01006F──I see. The flowers that became\x01",
            "the raw ingredient for that drug, eh?\x02\x03",
            "#01001FIn this case, it's become something\x01",
            "that even the police can't ignore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11PI was thinking about keeping up\x01",
            "the cooperation with the Guild...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FCould there be other matters\x01",
            "that are bothering you?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#11P#01003FIf I have to say, there're, but, well,\x01",
            "leave those to the other sections.\x02\x03",
            "#01000FIn any case, with the local referendum \x01",
            "for the national independence, a certain \x01",
            "degree of confusion can't be avoided.\x02\x03",
            "Now, washing away anxieties\x01",
            "should be a priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106F...It's really the case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F#12PIn other words, it's crisis management.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FBut in that case...\x01",
            "What should we do about today's plans?\x02\x03",
            "#00200FEven the Cryptids investigation...\x01",
            "We were in charge of it just yesterday.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#00302F#11PWell, we could go help\x01",
            "the Guild's Bracers, no?\x02",
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
        "#6P#00105F...Is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305F#12PIs something on your mind?\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00003F#11PWell...I was just thinking...\x02\x03",
            "#00001FWhy don't we try to visit\x01",
            "the "Rosenberg Studio"?\x02",
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
        "#6P#00101FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10101FThe one said to be tied to the "Society"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PI see...\x01",
            "I totally forgot.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_150AF")

    ChrTalk(
        0x101,
        (
            "#00003F#11PNaturally without a search warrant we\x01",
            "can't perform a compulsory search.\x02\x03",
            "#00001FHowever...that old man said\x01",
            "something like this before:\x02",
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
            "However, now I don't have anything\x01",
            "in particular to tell you.\x02\x03",
            "If you have other business,\x01",
            "you can come visit again.\x02\x03",
            "I'll at least hear what you have to\x01",
            "say out of deference for Renne.\x07\x00\x02",
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
    Jump("loc_1525F")

    label("loc_150AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_151AE")

    ChrTalk(
        0x101,
        (
            "#00006F#11PNaturally without a search warrant we\x01",
            "can't perform a compulsory search.\x02\x03",
            "#00001FBased on what Renne told us, he didn't\x01",
            "look like someone you can't reason with.\x02\x03",
            "And due to Mrs. Imelda's request,\x01",
            "we more or less know him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1525F")

    label("loc_151AE")


    ChrTalk(
        0x101,
        (
            "#00006F#11PNaturally without a search warrant we\x01",
            "can't perform a compulsory search.\x02\x03",
            "#00001FBased on what Renne told us, he didn't\x01",
            "look like someone you can't reason with.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1525F")


    ChrTalk(
        0x103,
        (
            "#6P#00203F...Maybe it could be worth\x01",
            "paying him a visit.\x02\x03",
            "#00201FAlthough it could be risky.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_1536D")

    ChrTalk(
        0x105,
        (
            "#10304F#12PIndeed. I'd like to get an understanding of\x01",
            "that bizarre young boy's objectives, though.\x02\x03",
            "#10302FIt could be that he's\x01",
            "staying at the studio.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1540B")

    label("loc_1536D")


    ChrTalk(
        0x105,
        (
            "#10304F#12PIndeed. I'd like to get an understanding of\x01",
            "that bizarre young boy's objectives, though.\x02\x03",
            "#10302FIt could be that he's\x01",
            "staying at the studio.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1540B")


    ChrTalk(
        0x109,
        (
            "#6P#10100FI-I agree!\x02\x03",
            "#10106FIn addition, this situation in which a dangerous\x01",
            "group of foreigners is gaining power...\x02\x03",
            "#10101FWe can't leave a suspicious\x01",
            "group like that alone anymore!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FYou have a point...\x02\x03",
            "#00101FIs it okay to go first of all\x01",
            "to the studio directly?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(250)

    ChrTalk(
        0x101,
        (
            "#00000F#11PYeah, let's go probe the situation.\x02\x03",
            "#00003F...According to the circumstances, we\x01",
            "could need to get us a search warrant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PRight...\x02\x03",
            "#00300FAlright, then let's\x01",
            "go out at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01105F#6PHey, hey everyone.\x02\x03",
            "Are you going out for work?\x02",
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
            "#00005F#11PYeah, we plan to do that.\x02\x03",
            "#00000FKeA, today...\x01",
            "You were going to the library?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01103FHmm...maybe I'll search a\x01",
            "braille book for Shizuku...\x02\x03",
            "#01110FOn the way back I'll shop for groceries, is\x01",
            "there anything you want to eat for dinner?\x02",
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
            "#5P#00105FShopping for groceries...\x01",
            "Will you be alright, KeA?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00205FIt is true that you are always\x01",
            "cooking for us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01104FYes, I always buy from Momo's\x01",
            "father and from Oscar too.\x02\x03",
            "#01110FI'm also friends with the old lady\x01",
            "at the department general store...\x02",
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
        "#00012F#11PW-When did you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#11PHa ha, well, it's Keddo after all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01004FIn that case...\x01",
            "It's becoming a little colder, maybe\x01",
            "something for a hot pot would be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FAh, that's nice.\x01",
            "It will enliven everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PHot pot...so, it has to\x01",
            "be Eastern style, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00100FKeA, will you be alright?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01103FHmm, I think I'll manage.\x02\x03",
            "#01101FI want to make the broth properly, so I'll\x01",
            "have to stop by the East Street stalls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#11POoh, you're goin' all out for it, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FNow I can't wait for when\x01",
            "we will be returning home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#11PThank you, KeA.\x02\x03",
            "#00002FToday, we'll try our best to\x01",
            "not come back home late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#01109FEhehe...alright!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15F7C")
    Jump("loc_15F81")

    label("loc_15F7C")

    OP_29(0x81, 0x4, 0x40)

    label("loc_15F81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15F92")
    Jump("loc_15F97")

    label("loc_15F92")

    OP_29(0x82, 0x4, 0x40)

    label("loc_15F97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15FA8")
    Jump("loc_15FAD")

    label("loc_15FA8")

    OP_29(0x84, 0x4, 0x40)

    label("loc_15FAD")

    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    Call(0, 67)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_40_14291 end

    def Function_41_15FCA(): pass

    label("Function_41_15FCA")

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

    def lambda_160A9():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_160A9)
    Sleep(100)

    def lambda_160B9():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_160B9)
    Sleep(100)

    def lambda_160C9():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_160C9)
    Sleep(100)

    def lambda_160D9():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_160D9)
    Sleep(100)

    def lambda_160E9():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_160E9)
    Sleep(100)

    def lambda_160F9():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_160F9)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x105,
        "#11P#10300FA few new ones have arrived.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00300FWhat do we do?\x01",
            "It'd be nice to deal with them after\x01",
            "we've gone to the Doll Studio first.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#5PNo, we don't know what will\x01",
            "happen based on our inquiry.\x02\x03",
            "#00001FI think it's better to first clear\x01",
            "the urgent support requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FYou're right...\x01",
            "We could also need to perform\x01",
            "a compulsory search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#11PThen, let's go to the mountain path\x01",
            "Doll Studio after we have prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203F(I am really looking forward\x01",
            "to the Theme Park side job...)\x02",
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

    # Function_41_15FCA end

    def Function_42_16396(): pass

    label("Function_42_16396")

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
        "#00004F#11P──*phew*, thank you for the food.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#11PMyyy, hodgepodge is so\x01",
            "nice for the chilled body.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(200)

    ChrTalk(
        0x102,
        (
            "#5P#00102F*giggle*, indeed. There were also\x01",
            "eggs and chicken meat in it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x1)
    Sleep(100)

    ChrTalk(
        0x109,
        "#12P#10109FThank you for the food, KeA.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(100)

    ChrTalk(
        0x103,
        "#6P#00202FIt was very good.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x2)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#6P#01104FEhehe, I only used the ingredients\x01",
            "from yesterday's hot pot.\x02\x03",
            "#01110FWazy, are you full?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x2)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10304F#11P...Yeah. \x01",
            "It tasted rich and delicious.\x02\x03",
            "#10302FThank you for the food, KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#01109FEhehe, I'm glad.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5P#01004FHm...you finally feel relieved.\x02\x03",
            "#01000FAbout Wald Wales' case...\x01",
            "The CGF is continuing the search.\x02\x03",
            "Don't brood over it that much.\x02",
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
        "#10304F#12P...Ha ha, you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#11PHowever, it's no doubt\x01",
            "that Wald obtained the\x01",
            ""Gnosis" somewhere.\x02\x03",
            "We have to investigate\x01",
            "that route no matter what...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01003FSection Two is already\x01",
            "investigating about that.\x02\x03",
            "I also heard that Section One is taking part\x01",
            "in the investigation about those foreigners.\x02\x03",
            "#01000FWell, don't be too impatient about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11P...Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FIn the end, were they able to restore\x01",
            "the derailment place yesterday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01005FYeah, until yesterday evening,\x01",
            "only one track could be used, but\x01",
            "at night it was completely restored.\x02\x03",
            "#01004FIt ended without being a great deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106F*sigh*...thank goodness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FThe transcontinental railway is an important\x01",
            "traffic route... If it was still halted, \x01",
            "by now a big chaos would've arisen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PIf that had happened, it would've become\x01",
            "even more material for the Empire and \x01",
            "Republic arm twistin'.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00003F#5PYeah...no doubt.\x02\x03",
            "#00001F...So, should we check\x01",
            "the support requests?\x02\x03",
            "It should be time for today's\x01",
            "share to have come in.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(150)

    ChrTalk(
        0x102,
        "#6P#00100FYes, let's check.\x02",
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
        "#6P#01105FThe phone is ringing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PYeah, I'll take it.\x02",
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

    def lambda_171FF():
        OP_95(0xFE, 14100, 850, 12300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_171FF)
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
            "#00001FYes, this is Crossbell Police,\x01",
            "Special Support Section...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...Morning. It's Michel,\x01",
            "the Guild receptionist.\x02",
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
            "#00005FAh, good morning.\x02\x03",
            "#00001FDid you have a look at\x01",
            "the "Society" report?\x02",
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
            "Yes...frankly, it was really helpful.\x02\x03",
            "Currently, I contacted Leman Headquarters\x01",
            "and they're analyzing the information...\x02\x03",
            "Well, since they're a mysterious\x01",
            "group I honestly don't know how\x01",
            "much they will be able to do.\x02",
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
            "#00006F...I see.\x02\x03",
            "#00005FUhm, did you call to tell us that?\x02",
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
            "Ah, no.\x01",
            "It's not for that.\x02\x03",
            "I'd like to ask you something...\x01",
            "Don't you happen to have seen\x01",
            "our Ling and Eolia...?\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 2)), scpexpr(EXPR_END)), "loc_1759A")
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001FUhhm, we met them yesterday\x01",
            "at the hospital...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_175F2")

    label("loc_1759A")

    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FUhhm, we met them the day before\x01",
            "yesterday at Orchis Tower...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_175F2")

    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Michel's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I see...I see.\x02\x03",
            "...Honestly, I wonder what\x01",
            "those two are doing.\x02",
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
            "#00013FUhm...\x01",
            "You can't contact them?\x02",
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
            "Yes, I haven't been able to go through\x01",
            "their ENIGMAs since last night.\x02\x03",
            "Well, it's not a rare occurrence, so\x01",
            "I'm not really worried about them.\x02",
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
            "#00003FIs that so...?\x02",
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
            "Well, don't mind it.\x01",
            "You're busy too.\x02\x03",
            "That juvenile delinquents' leader, was it?\x01",
            "You have it hard too, don't you?\x02",
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
            "#00008F...Yes, well.\x02",
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
            "If you happen to catch sight of those two,\x01",
            "please tell them to contact me immediately.\x02\x03",
            "Well then, do your best too㈱\x02",
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
            "#00004FYes, thank you very much.\x02",
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
            "#01000FSeemed it was from the Guild.\x01",
            "Has anything happened?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        "#00001F#5PAh, yes...\x02",
    )

    CloseMessageWindow()
    OP_68(12920, 1850, 6140, 2000)
    MoveCamera(35, 17, 0, 2000)

    def lambda_179B2():
        OP_96(0xFE, 0x319C, 0x352, 0x20D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_179B2)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that Bracers Ling and Eolia\x01",
            "cannot be contacted since last night.\x07\x00\x02",
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
        "#6P#00101FThose women...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#12PThey're those two very\x01",
            "skilled ladies, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PYeah, especially Miss Eolia.\x01",
            "She's my type after Miss Cecil.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(150)

    ChrTalk(
        0x103,
        "#6P#00211FI think no one cares about that...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_17C6F")

    ChrTalk(
        0x109,
        (
            "#12P#10106F#NHowever, it worries me a little.\x02\x03",
            "#10108FThey seemed to be managing\x01",
            "their schedule very firmly.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#5P#00006FRight...\x01",
            "Even when we fought them before, I felt\x01",
            "they were calculating every single action.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17D1B")

    label("loc_17C6F")


    ChrTalk(
        0x109,
        (
            "#12P#10106F#NHowever, it worries me a little.\x02\x03",
            "#10101FThey seemed to be managing\x01",
            "their schedule very firmly.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#5P#00003FRight...\x01",
            "Mr. Arios too seems like that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D1B")


    ChrTalk(
        0x8,
        (
            "#01003F#11PWell, if you have time you can go\x01",
            "show up at the Guild during your jobs.\x02\x03",
            "#01002FIn times like this we're all equal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00000FYes, I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01105FLloyd, guys, are you\x01",
            "leaving now?\x02\x03",
            "#01102FWill hot pot be ok today?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17E14():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17E14)
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
            "#5P#00002FYeah, today we'll be back\x01",
            "home earlier than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00106FSorry, KeA.\x02\x03",
            "#00108FAlthough you went out of your way to\x01",
            "prepare it, yesterday we couldn't eat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01121FNo, don't be. Everyone is\x01",
            "doing their best, right?\x02\x03",
            "#01109FSo, KeA too has to do\x01",
            "hers and help out.\x02",
        )
    )

    CloseMessageWindow()
    Sound(822, 0, 100, 0)
    OP_63(0x9, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#00002FKeA...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#11PHa ha...\x01",
            "She overkilled you with that.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)

    ChrTalk(
        0x103,
        (
            "#6P#00204FAccording to the weather forecast,\x01",
            "it should stop raining in the afternoon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#11PLet's take care of work properly\x01",
            "and be back home quickly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10102F#NYes...!\x02",
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
    SubItemNumber(0x330, 1)
    SubItemNumber(0x331, 1)
    SubItemNumber(0x332, 1)
    SubItemNumber(0x33A, 1)
    Call(0, 67)
    ReplaceBGM("ed7150", -1)
    ReplaceBGM("ed7101", "ed7562")
    ReplaceBGM("ed7116", "ed7562")
    OP_24(0x350)
    PlayBGM("ed7150", 0)
    EventEnd(0x5)
    Return()

    # Function_42_16396 end

    def Function_43_18379(): pass

    label("Function_43_18379")

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
        "#01003F──I see, you're going back.\x02",
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
            "#10106F#11PYes... Actually, I wanted to have you let me\x01",
            "stay here to learn for half a year, but...\x02\x03",
            "#10101FThinking about many things──\x01",
            "I decided to go back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006F...I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00106F...It's understandable.\x02\x03",
            "#00108FIn this incident even the CGF\x01",
            "suffered heavy damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FWell, they probably would want badly\x01",
            "an excellent young member like you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#11PAhaha...\x01",
            "Although I doubt about that "excellent".\x02\x03",
            "#10108F...I'm sorry.\x01",
            "Setting aside restoration work\x01",
            "and going back to my duties is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FNo...don't let it bother you.\x02\x03",
            "#00002FConsidering the situation in which\x01",
            "Crossbell is, the CGF has a big role.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PWe will miss you, but...\x01",
            "We can only accept how things are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01108F#11PNoｱl...\x01",
            "Are you going away...?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x1)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10112F#5PAhaha...yes.\x02\x03",
            "I'll be incredibly sad not being\x01",
            "able to see you, KeA...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01106F#11P...I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F#5PBut I'll come to\x01",
            "see you again...!\x02\x03",
            "#10100F#30WAnd with Fran too...\x02\x01",
            "#10108F#45W............\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x109)

    ChrTalk(
        0x9,
        "#01112F#11PNoｱl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#11PMiss Noｱl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10301F...They say that your sister won't be\x01",
            "able to leave hospital for a while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#5PYes...the surgery succeeded and\x01",
            "since she regained consciousness\x01",
            "there's nothing to be worried about...\x02\x03",
            "#10113FBut her physical strength\x01",
            "isn't coming back at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00103F...I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00308F............\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10112F#11PAhaha...senior, please\x01",
            "don't do such a face.\x02\x03",
            "#10104FShe's a police officer too, she was\x01",
            "ready for some degree of danger.\x02\x03",
            "#10100FIf you're thinking that it's your fault...\x01",
            "It's not, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00304F...Ha ha, alright.\x02\x03",
            "#00302FAt any rate, if things are like this, then\x01",
            "today is Noｱl's last day workin' with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#11PYes, today I'll do\x01",
            "my very best!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10102F#11PIt's nice to be working with you, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00004FYeah...likewise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00102FMiss Noｱl...\x01",
            "It's nice to work with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#01003F──I'll prepare all the papers.\x01\x02\x03",
            "#01002FAlso, it's been some time since\x01",
            "we had dinner outside.\x02\x03",
            "Being it a special occasion, it'll be on me.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(100)
    SetChrSubChip(0x9, 0x0)

    ChrTalk(
        0x109,
        "#10105F#11PChief Sergei...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FHa ha, that's nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11PHow generous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FHu hu, should we go to\x01",
            "my friend's host club?\x02\x03",
            "#10302FI'll call well-dressed men and ready\x01",
            "a magnificent farewell party.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0x109, 0x1)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10111F#5PEeeh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00305FOh, that could do.\x02\x03",
            "#00309FAlthough I'd be happier with a\x01",
            "places with beautiful babes.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#11P#00111F*sigh*...\x01",
            "That's not the problem, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#11PThen, what about the meat restaurant at M.W.L.\x01",
            "where they do the Michey show? (*sparkling eyes*)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)

    ChrTalk(
        0x9,
        "#01105F#5PIs there such a restaurant?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#01006FBefore that, guys...\x01",
            "Think about my wallet content.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10112F#11PAhaha...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00012FIn any case, today we have\x01",
            "to finish our work by night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01203F#5P#NGrrowl...woof.\x02",
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

    # Function_43_18379 end

    def Function_44_1942D(): pass

    label("Function_44_1942D")

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

    def lambda_1950C():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1950C)
    Sleep(100)

    def lambda_1951C():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1951C)
    Sleep(100)

    def lambda_1952C():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1952C)
    Sleep(100)

    def lambda_1953C():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1953C)
    Sleep(100)

    def lambda_1954C():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1954C)
    Sleep(100)

    def lambda_1955C():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1955C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        "#00108F#11PAs expected, there're many...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FHowever, it looks like no\x01",
            "urgent ones came in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FRight. Even that one from Abbas\x01",
            "seems to be not so urgent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FWell, let's keep doin' our rounds\x01",
            "and take care of them little by little.\x02",
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
            "#00003F#5P──Listen, everyone.\x02\x03",
            "#00002FIt would be ok during a break too...\x01",
            "Why don't we go to St. Ursula Hospital?\x02",
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

    def lambda_197A2():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_197A2)
    Sleep(50)

    def lambda_197B2():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_197B2)
    Sleep(50)

    def lambda_197C2():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_197C2)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x109,
        "#12P#10105FWhat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#11PYou're right... I think it'd be nice.\x02\x03",
            "#00104FWe've been so busy for the last week\x01",
            "that we didn't go to check on her conditions...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FAgreed.\x02\x03",
            "#00302FSince sweet Fran has regained consciousness,\x01",
            "we have to absolutely go pay her a sick visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10108FB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FIndeed, not being able to\x01",
            "hear her lively voice at the\x01",
            "terminal is simply sad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201FYes...\x01",
            "I would like to at least hear her voice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PNoｱl, don't hold back.\x02\x03",
            "#00000FEven for us, Fran has an\x01",
            "important support role.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_19A1A():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_19A1A)
    Sleep(50)

    def lambda_19A2A():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_19A2A)
    Sleep(50)

    def lambda_19A3A():
        TurnDirection(0x104, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_19A3A)
    Sleep(50)

    def lambda_19A4A():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_19A4A)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        (
            "#12P#10104FEveryone...\x01",
            "Thank you very much.\x02\x03",
            "#10102FThen, when we take a break,\x01",
            "let's go to St. Ursula Hospital.\x02",
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

    # Function_44_1942D end

    def Function_45_19B2E(): pass

    label("Function_45_19B2E")

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
            "#30W　　　　　 Two days later──\x02\x03",
            "The referendum to question the propriety\x01",
            "of Crossbell state independence was held.\x02\x03",
            "Its result would have been announced the same day...\x02\x03",
            "One week after that──\x01",
            "Crossbell headed to its "fateful day".\x02",
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
    AddItemNumber(0x2E9, 1)
    Sleep(1500)
    Sound(18, 0, 100, 0)
    UseItem(0x2EA, 0xFF)
    AddItemNumber(0x2EA, 1)
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
        "#5P#00013F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F...Well, it's become\x01",
            "a serious matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00106FYes...\x01",
            "I honestly didn't think about\x01",
            "such a quick development.\x02\x03",
            "#00108F...I thought to check about it\x01",
            "with "uncle", but I haven't been\x01",
            "able to reach him since yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206FThe Chief too went out to HQ first thing\x01",
            "in the morning and isn't back yet...\x02\x03",
            "#00201FCould he have gone to check on\x01",
            "that "State Guard" organization?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FYeah...\x01",
            "Frankly, it was a bolt from the blue.\x02\x03",
            "#00001FNot only for us, but probably\x01",
            "for the police brass too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FHey now...\x01",
            "Wouldn't that be strange?\x02\x03",
            "#00301FWhat about Noｱl, Mireille\x01",
            "and the others?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#6P#00208FAt present, the CGF\x01",
            "can't be reached.\x02\x03",
            "I think that maybe the inquiries are so many\x01",
            "that they are having an information shut off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00103F...I don't blame them for that.\x02\x03",
            "#00101FRegarding this assets freeze...\x01",
            "There's no way the Empire and\x01",
            "Republic are going to remain silent.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)

    ChrTalk(
        0x101,
        (
            "#5P#00008F"We are already prepared for the use of force"...\x01",
            "I'm worried about the national borders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#01108F#30W............\x02",
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
            "#5P#00002FSorry...\x01",
            "Did we scare you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#01121F...No.\x01",
            "KeA too understands that\x01",
            "something serious is happening.\x02\x03",
            "#01105FBy the way, Wazy hasn't\x01",
            "been here since morning...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00005FYes, now that you mention it...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#12P#00205FAh, Mr. Wazy said he had some minor\x01",
            "business to attend to and went out.\x02\x03",
            "#00200FI think it was just after the Chief left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00001FReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00106FConsidering how late it is,\x01",
            "I'm not very happy about it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)

    ChrTalk(
        0x104,
        "#00308FHm...\x02",
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
        "#00105FAt such a time...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301FWho is it...?\x02",
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

    def lambda_1A64D():
        OP_95(0xFE, 3500, 0, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A64D)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xE1, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00001F──Yes!\x01",
            "Who is it!?\x02",
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
        "Woman's Voice",
        (
            "#1P#2SThank goodness...\x01",
            "You are in.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Woman's Voice",
        "#1P#2SIt is me, Cecil.\x07\x00\x02",
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
        "#00011FSister Cecil!?\x02",
    )

    CloseMessageWindow()

    def lambda_1A7BC():
        OP_95(0xFE, 1000, 0, 2500, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A7BC)
    WaitChrThread(0x101, 1)

    def lambda_1A7DA():
        OP_95(0xFE, 1000, 0, 1000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A7DA)
    WaitChrThread(0x101, 1)
    Sound(806, 0, 80, 0)
    Sleep(300)
    Sound(103, 0, 100, 0)

    def lambda_1A807():
        OP_96(0xFE, 0x3E8, 0x0, 0xAF0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A807)
    Sleep(500)
    SetChrPos(0xB, 1000, 0, -1500, 0)

    def lambda_1A835():
        OP_96(0xFE, 0x3E8, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1A835)

    def lambda_1A84F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1A84F)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x9,
        "#12P#01110FAh, it's Cecil.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x102, 3, 0, 46)
    Sleep(250)
    OP_68(4500, 1100, 3300, 2000)
    OP_93(0x101, 0x2D, 0x1F4)

    def lambda_1A8A9():
        OP_95(0xFE, 2000, 0, 3800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A8A9)
    Sleep(500)

    def lambda_1A8C6():
        OP_95(0xFE, 2000, 0, 2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1A8C6)
    WaitChrThread(0x101, 1)

    def lambda_1A8E4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A8E4)
    WaitChrThread(0xB, 1)

    def lambda_1A8F5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1A8F5)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#5P#00105FMiss Cecil...\x01",
            "Has something happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FIt's rare for you\x01",
            "to come here.\x02",
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
            "I am sorry for visiting\x01",
            "all of a sudden.\x02\x03",
            "Uhm... Didn't Mr. Arios\x01",
            "come here, perhaps?\x02",
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
        "#00005F#5P...Mr. Arios?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00205FNo, he didn't...\x01",
            "What is going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#05926F...Well...\x02\x03",
            "#05928FLast night he came at the hospital\x01",
            "very late and took Shizuku with him.\x02\x03",
            "He did the discharge procedure\x01",
            "papers on the spot...\x02",
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
        "#00005F#5PHUH!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00101FWhat...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#01112FShizuku...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#05926FSo, I went to the Guild to\x01",
            "ascertain the reason, but...\x02\x03",
            "It seems that even Mr. Michel\x01",
            "doesn't have a clue at all.\x02\x03",
            "#05921FAnd so, just in case I came\x01",
            "to visit your place too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#5PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FThat ol' man...\x01",
            "Why did he do such a thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FI think even the fact that it happened \x01",
            "late at night it is not normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#01108F............\x02",
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

    def lambda_1AE47():
        TurnDirection(0x101, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1AE47)
    Sleep(50)

    def lambda_1AE57():
        TurnDirection(0x102, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1AE57)
    Sleep(50)

    def lambda_1AE67():
        TurnDirection(0xB, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1AE67)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xB, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00011FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FSince it's not the ENIGMA,\x01",
            "maybe it won't be the Chief...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FCould it be Mr. Arios?\x02",
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
            "#11P#00001FYes, Crossbell Police,\x01",
            "Special Support Secti──\x02",
        )
    )

    WaitChrThread(0xB, 3)
    CloseMessageWindow()
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    NpcTalk(
        0xE,
        "Woman's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S#5PThank goodness!\x01",
            "You're there, Lloyd!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00011FWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FIt seems the phone was\x01",
            "in speaker mode.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FThis voice... Miss Grace?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00300FSeems so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FUhmm...\x01",
            "Miss Grace, is something wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5POf course something is!\x01",
            "I thought to tell you too!\x02\x03",
            "Just now an unbelievable notification\x01",
            "came in from Orchis Tower!\x02\x03",
            "It appears that Mayor Dieter has\x01",
            "become the first President of the \x01",
            ""Independent State of Crossbell"!\x07\x00\x02",
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
        "#11P#00007FWha──\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00205FThe first President...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00107FPresident...\x01",
            ""U-Uncle" has!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FHey now...\x01",
            "What kind of joke is this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5PI-I thought it was\x01",
            "a joke too, at first!\x02\x03",
            "However, that notice was brought\x01",
            "by a soldier in a white uniform...\x02\x03",
            "He said he was from the just formed\x01",
            ""State Guard", you know!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00013FR-Really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FA soldier...don't tell me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5PYes, probably a member\x01",
            "of the CGF, but...\x02\x03",
            "A-Also...don't freak out, ok?\x02\x03",
            "Immediately after President Dieter took his post,\x01",
            "he nominated the "Secretary of Defence".\x02\x03",
            "And he's──#350W─\x01",
            "#20Wthat Mr. Arios.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(250)

    ChrTalk(
        0x101,
        "#11P#00005F──What.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105F#30W...Then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00303F#30WHmmm...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00208F#30WMr. ...Arios?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#6P#05925F#30W............\x02",
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
    SetChrName("Everyone")
    Fade(500)
    SetCameraDistance(24500, 1000)
    OP_82(0x1F4, 0x0, 0xBB8, 0x3E8)

    AnonymousTalk(
        0xFF,
        "#5S#16AWHAAAAAAAAAAT!?\x02",
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
            "#5PIt appears that the President inaugural\x01",
            "speech is beginning right now!\x02\x03",
            "It seems it's going to be broadcasted even\x01",
            "via orbal net, so watch it if you want!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Youth's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P#1S...Senior Grace!\x01",
            "Somehow we got permission to collect data!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5P#2SWay to go!\x01",
            "Well done, Reins!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5P#3S──Sorry!\x01",
            "I'm off to get data about the speech!\x02\x03",
            "Bye then!\x07\x00\x02",
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
        "#6P#05928FWas it...real?\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00006FI-I don't know, but...\x02\x03",
            "#00013FThat Mr. Arios the\x01",
            ""Secretary of Defence"...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00107FThe Secretary means that...\x01",
            "he's the "State Guard" top...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00310FN-No way...\x01",
            "What about his title of Bracer!?\x02\x03",
            "#00306FAlso, ol' man Dieter being the\x01",
            ""President"...it's too sudden...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201F...In any case, let's watch the\x01",
            "inaugural speech at the terminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007FYeah...!\x02",
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

    # Function_45_19B2E end

    def Function_46_1BA97(): pass

    label("Function_46_1BA97")

    Fade(250)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 6050, 30, 5500, 180)
    OP_0D()

    def lambda_1BAC0():
        OP_95(0xFE, 4750, 30, 5500, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BAC0)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0xE1, 0x1F4)
    Return()

    # Function_46_1BA97 end

    def Function_47_1BAE1(): pass

    label("Function_47_1BAE1")

    SetChrPos(0x101, 4100, 850, 10800, 90)

    def lambda_1BAF7():
        OP_96(0xFE, 0x3138, 0x352, 0x2A30, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BAF7)
    WaitChrThread(0x101, 1)

    def lambda_1BB15():
        OP_95(0xFE, 14100, 850, 12300, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BB15)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_47_1BAE1 end

    def Function_48_1BB36(): pass

    label("Function_48_1BB36")

    SetChrPos(0x102, 4300, 850, 10200, 90)

    def lambda_1BB4C():
        OP_96(0xFE, 0x37DC, 0x352, 0x27D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BB4C)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_48_1BB36 end

    def Function_49_1BB6D(): pass

    label("Function_49_1BB6D")

    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 2650, 850, 9600, 90)

    def lambda_1BB90():
        OP_96(0xFE, 0x316A, 0x352, 0x2580, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1BB90)
    WaitChrThread(0x104, 1)
    TurnDirection(0x104, 0x101, 500)
    Return()

    # Function_49_1BB6D end

    def Function_50_1BBB1(): pass

    label("Function_50_1BBB1")

    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 2200, 850, 11000, 90)

    def lambda_1BBD4():
        OP_96(0xFE, 0x2FA8, 0x352, 0x2AF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1BBD4)
    WaitChrThread(0x103, 1)
    TurnDirection(0x103, 0x101, 500)
    Return()

    # Function_50_1BBB1 end

    def Function_51_1BBF5(): pass

    label("Function_51_1BBF5")

    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 800, 850, 10300, 90)

    def lambda_1BC13():
        OP_96(0xFE, 0x2A30, 0x352, 0x283C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1BC13)
    WaitChrThread(0x9, 1)
    Return()

    # Function_51_1BBF5 end

    def Function_52_1BC2D(): pass

    label("Function_52_1BC2D")

    SetChrPos(0xB, 800, 850, 11500, 90)

    def lambda_1BC43():
        OP_96(0xFE, 0x2A30, 0x352, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1BC43)
    WaitChrThread(0xB, 1)
    Return()

    # Function_52_1BC2D end

    def Function_53_1BC5D(): pass

    label("Function_53_1BC5D")

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
        "#6P#00008F............\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1BE39():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1BE39)
    Sleep(50)

    def lambda_1BE49():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1BE49)
    Sleep(50)

    def lambda_1BE59():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1BE59)
    Sleep(50)

    def lambda_1BE69():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1BE69)
    Sleep(50)

    def lambda_1BE79():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1BE79)
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
            "#00007FYes, Lloyd speaking...!\x02",
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
            "...Hey, it's me.\x02",
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
            "#00010FChief!\x01",
            "The inaugural speech just now──\x02",
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
            "...I saw it, of course.\x02\x03",
            "Well, aside if it's right or wrong,\x01",
            "the CGF seems to have been\x01",
            "reorganized into the "State Guard".\x02\x03",
            "The police too was decided to\x01",
            "be included in that as a part.\x02",
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
            "#00006FN-No way...\x02\x03",
            "#00013FEven Commander Sonya...\x01\x02",
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
            "She was in the video, right?\x01",
            "Well── I guess she acknowledged.\x02\x03",
            "I don't know what'll happen, but...\x01",
            "For now, don't get close\x01",
            "to Orchis Tower.\x02\x03",
            "The State Guard "soldiers" are\x01",
            "likely to be strictly guarding it.\x02",
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
            "#00010FSh...understood.\x02",
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
            "──I'll call again. Don't do\x01",
            "anything rash, alright?\x07\x00\x02",
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
        "#12P#00108F...What did the Chief say?\x02",
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
        "#5P#00006FYes, about the State Guard...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained what you heard from Sergei to the others.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#12P#00106FSo...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PDamn, Commander Sonya\x01",
            "went to their side...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00206FWell, considering her position\x01",
            "I think she didn't have a choice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05923F#5P...Mr. Arios.\x01",
            "The reason why he took away\x01",
            "Shizuku with him was this, then.\x02",
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

    def lambda_1C4AD():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C4AD)
    Sleep(50)

    def lambda_1C4BD():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1C4BD)
    Sleep(50)

    def lambda_1C4CD():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1C4CD)
    Sleep(50)

    def lambda_1C4DD():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1C4DD)
    Sleep(50)

    def lambda_1C4ED():
        TurnDirection(0x9, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1C4ED)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0x101,
        "#12P#00005FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FYou're right...\x01",
            "Being on such a position could\x01",
            "have an influence on Shizuku...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PShe could be targeted by\x01",
            "opposin' factions, right...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00208F...In such a situation, I can't\x01",
            "assert the chances are zero.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01108F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FKeA...it's alright.\x02\x03",
            "#00000FMr. Arios is thinking in order to\x01",
            "have no danger come to Shizuku.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1C6A3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1C6A3)
    Sleep(50)
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(200)

    ChrTalk(
        0x9,
        (
            "#01121F#5PYes...it's like that.\x02\x03",
            "#01122F...Ehehe.\x01",
            "I'm a bit worried though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5P#05921FKeA...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00008F...Sister Cecil, I'm sorry but, could\x01",
            "you watch the house for a little?\x02",
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

    def lambda_1C7F9():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1C7F9)
    Sleep(50)

    def lambda_1C809():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1C809)
    Sleep(50)

    def lambda_1C819():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1C819)
    Sleep(50)

    def lambda_1C829():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1C829)
    Sleep(50)
    WaitChrThread(0xB, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x9,
        "#01105F#5PLloyd...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05925F#5PYes, if it is until evening\x01",
            "I don't have any problem...\x02\x03",
            "#05921FAre you going somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FYeah──\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00001FListen, everyone.\x02\x03",
            "For now...\x01",
            "Why don't we go to the Guild?\x02",
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
        "#12P#00101FY-Yes, why not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00201FIt is true that I would like to ask \x01",
            "about Mr. Arios' circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12PI know, right?\x01",
            "It was really out of the blue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05923F#5P...I understand.\x01",
            "I will stay here and watch the\x01",
            "house together with KeA.\x02\x03",
            "#05920FThe situation looks serious,\x01",
            "so be very careful.\x02\x03",
            "Don't do anything crazy.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1CAE6():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1CAE6)
    Sleep(50)

    def lambda_1CAF6():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1CAF6)
    Sleep(50)

    def lambda_1CB06():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1CB06)
    Sleep(50)

    def lambda_1CB16():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1CB16)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x101,
        "#12P#00002FYeah, I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#12PThanks, Miss Cecil!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00104FThen, we leave it to you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00202FKeA, please be a good girl and\x01",
            "watch the place with Miss Cecil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01112F#5PAh...\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_68(12900, 1750, 9800, 3000)

    def lambda_1CC1D():

        label("loc_1CC1D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1CC1D")

    QueueWorkItem2(0xB, 2, lambda_1CC1D)

    def lambda_1CC2F():

        label("loc_1CC2F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1CC2F")

    QueueWorkItem2(0x9, 2, lambda_1CC2F)
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
        "#11P#01101F............\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1CCFA():

        label("loc_1CCFA")

        TurnDirection(0xB, 0x9, 500)
        Yield()
        Jump("loc_1CCFA")

    QueueWorkItem2(0xB, 2, lambda_1CCFA)

    ChrTalk(
        0xB,
        "#05925F#5PKeA?\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    SetCameraDistance(24500, 2000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)

    def lambda_1CD39():
        OP_95(0xFE, 900, 850, 9700, 5500, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1CD39)
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

    # Function_53_1BC5D end

    def Function_54_1CD9F(): pass

    label("Function_54_1CD9F")

    OP_95(0xFE, 15150, 850, 8450, 4500, 0x1)
    OP_95(0xFE, 10150, 850, 8950, 4500, 0x1)
    OP_95(0xFE, 5150, 850, 9450, 4500, 0x1)
    OP_95(0xFE, 150, 850, 9450, 4500, 0x1)
    Return()

    # Function_54_1CD9F end

    def Function_55_1CDF0(): pass

    label("Function_55_1CDF0")

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

    def lambda_1CEEB():
        OP_95(0xFE, -300, 0, 5300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1CEEB)
    WaitChrThread(0xB, 1)
    Sleep(500)
    OP_93(0xB, 0x5A, 0x1F4)

    def lambda_1CF13():
        OP_95(0xFE, 2300, 0, 5300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1CF13)
    WaitChrThread(0xB, 1)
    Sleep(500)
    OP_93(0xB, 0x10E, 0x1F4)

    def lambda_1CF3B():
        OP_95(0xFE, 1000, 0, 5300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1CF3B)
    WaitChrThread(0xB, 1)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "#1PSister Cecil!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_68(1000, 1000, 4100, 1500)
    SetChrPos(0x101, 300, 0, -1600, 0)
    BeginChrThread(0x101, 3, 0, 56)

    def lambda_1CFDF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1CFDF)
    Sleep(250)

    def lambda_1CFF3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1CFF3)
    Sleep(350)

    def lambda_1D007():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1D007)
    Sleep(450)

    def lambda_1D01B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1D01B)
    OP_93(0xB, 0xB4, 0x1F4)

    ChrTalk(
        0xB,
        "#05921F#5PLloyd...!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#12P#00007FWhat about KeA!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FYou said she was taken\x01",
            "away by Mr. Arios...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05926F#5PYes, Mr. Arios came alone,\x01",
            "wearing that white uniform...\x02\x03",
            "#05921FHe said "I've come to pick you up",\x01",
            "and KeA nodded to him...\x02",
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
        "#12P#00011FWhat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FYou mean that Keddo has\x01",
            "followed him willingly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05923F#5PYes...to me, it appeared like that.\x02\x03",
            "#05921FHowever, I tried to stopped her\x01",
            "since I thought it was strange\x01",
            "she didn't have your permission...\x02\x03",
            "#05926FBut KeA told me\x01",
            ""It's fine"...\x02\x03",
            "Also, Zeit, who was agitated,\x01",
            "calmed down too...\x02",
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
            "#12P#00208FBy the way...\x01",
            "Zeit is not around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05926F#5PAfter those two left,\x01",
            "he wandered off.\x02\x03",
            "#05928FMaybe he followed them...\x01\x02",
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

    def lambda_1D3CC():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D3CC)
    Sleep(100)

    def lambda_1D3DC():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D3DC)
    Sleep(100)

    def lambda_1D3EC():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1D3EC)
    Sleep(100)

    def lambda_1D3FC():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D3FC)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    Sleep(150)

    ChrTalk(
        0x101,
        "#5P#00008F...What's going on here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FCould she had made a\x01",
            "promise to Shizuku...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05923F#5PI thought that too, but\x01",
            "it didn't seem so...\x02\x03",
            "#05921FMr. Arios said something like\x01",
            "they were going to Michelam.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1D549():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D549)
    Sleep(50)

    def lambda_1D559():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D559)
    Sleep(50)

    def lambda_1D569():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1D569)
    Sleep(50)

    def lambda_1D579():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D579)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#12P#00005FMichelam...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05923F#5PYes, he said that the\x01",
            "boat was ready...\x02\x03",
            "#05921FIt means they intend to\x01",
            "go to Michelam, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#00103F...In the last few days, business was\x01",
            "completely halted in the Michelam area.\x02\x03",
            "#00101FThey went to such a place on purpose...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#00310FTsk...\x01",
            "It really isn't normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00201FLet's follow after them, Mr. Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003FYeah...\x01",
            "Let's find a boat in some way.\x02\x03",
            "#00007FSister Cecil, thank you!\x01",
            "At any rate, we'll try chasing after them.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D7A2():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D7A2)
    Sleep(50)

    def lambda_1D7B2():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D7B2)
    Sleep(50)

    def lambda_1D7C2():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1D7C2)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0xB,
        (
            "#05923F#5PYes, be careful.\x02\x03",
            "#05928F...Both Mr. Arios and KeA\x01",
            "had unusual serious eyes.\x02\x03",
            "#05921FI think the circumstances are really grave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00013FUnderstood...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107FIn any case we'll follow them\x01",
            "and ask about what's going on...!\x02",
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

    # Function_55_1CDF0 end

    def Function_56_1D8FA(): pass

    label("Function_56_1D8FA")


    def lambda_1D8FF():
        OP_97(0x101, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D8FF)
    Sleep(200)

    def lambda_1D91C():
        OP_97(0x102, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D91C)
    Sleep(200)

    def lambda_1D939():
        OP_97(0x103, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1D939)
    Sleep(200)

    def lambda_1D956():
        OP_97(0x104, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D956)
    Return()

    # Function_56_1D8FA end

    def Function_57_1D96C(): pass

    label("Function_57_1D96C")

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

    def lambda_1DB2A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1DB2A)
    Sleep(400)

    def lambda_1DB3E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1DB3E)
    Sleep(600)

    def lambda_1DB52():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1DB52)
    Sleep(400)

    def lambda_1DB66():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1DB66)
    Sleep(600)

    def lambda_1DB7A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_1DB7A)
    Sleep(400)

    def lambda_1DB8E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_1DB8E)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_1DBA4():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1DBA4)
    WaitChrThread(0x102, 1)

    def lambda_1DBB5():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1DBB5)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 1)

    def lambda_1DBCE():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_1DBCE)
    WaitChrThread(0xF5, 1)

    def lambda_1DBDF():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_1DBDF)
    OP_6F(0x79)
    OP_68(2640, 1300, 3150, 2000)
    MoveCamera(55, 15, 0, 2000)
    SetCameraDistance(29000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#6P#00001F#30W...The Special Support Section...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108F#30WWe're back...eh?\x02",
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
            "#4126V#25A#30WAh, you're back!\x02\x03",
            "#4127V#4S#30A#30WWelcome baaack!\x07\x00\x02",
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
            "#4S#20AI'm oooff!\x07\x00\x02",
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
            "#20A#30W──Alright, then.\x01",
            "Let's start on the hot pot.\x02\x03",
            "#20A#30WAfter KeA prepared, there is plenty\x01",
            "of meat, fish and vegetables.\x02\x03",
            "#20A#30WEat a lot, go to bed early...\x01",
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
            "#4S#20ABon appetiiit!\x07\x00\x02",
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
        "#6P#00008F#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00304F#30W...Ha ha.\x01",
            "Somehow it's too nostalgic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00208FYes...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E003")

    ChrTalk(
        0x109,
        (
            "#12P#10106FIt's hasn't been\x01",
            "even one month...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E003")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E040")

    ChrTalk(
        0x105,
        (
            "#12P#10404FHu hu...\x01",
            "It's really moving.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E040")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E0ED")

    ChrTalk(
        0x106,
        (
            "#12P#10708FHowever, it hasn't been damaged\x01",
            "as much as I thought it would...\x02\x03",
            "#10710FI thought it had been searched \x01",
            "thoroughly by the State Guard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E188")

    label("loc_1E0ED")


    ChrTalk(
        0x102,
        (
            "#5P#00104FHowever, it hasn't been damaged\x01",
            "as much as I thought it would, eh?\x02\x03",
            "#00100FI thought it had been searched \x01",
            "thoroughly by the State Guard...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E188")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E2D7")

    ChrTalk(
        0x10A,
        (
            "#12P#00606FIt appears they were considerate\x01",
            "towards that kid.\x02\x03",
            "#00602FFor the President side, she's\x01",
            "quite an important existence.\x02\x03",
            "They probably didn't want to offend her\x01",
            "by ravaging a place she holds very dear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000F...Indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00204FYou were too blunt, but...\x01",
            "I am happy it didn't change.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E405")

    label("loc_1E2D7")


    ChrTalk(
        0x101,
        (
            "#6P#00004FPerhaps they were considerate\x01",
            "towards KeA.\x02\x03",
            "#00000FFor the president side, she's\x01",
            "quite an important existence.\x02\x03",
            "They probably didn't want to offend her\x01",
            "by ravaging a place she hed very dear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00305F...Indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00204FYou were too blunt, but...\x01",
            "I'm happy it didn't change.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E405")

    Sound(953, 0, 100, 0)
    Sleep(300)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    OP_90(0xC, 1500, 3000, 15000, 180)

    def lambda_1E433():
        OP_96(0xFE, 0x5DC, 0x0, 0x1838, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1E433)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1E4C2():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1E4C2)
    Sleep(50)

    def lambda_1E4D2():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1E4D2)
    Sleep(50)

    def lambda_1E4E2():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1E4E2)
    Sleep(50)

    def lambda_1E4F2():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1E4F2)
    Sleep(50)

    def lambda_1E502():
        TurnDirection(0xF4, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1E502)
    Sleep(50)

    def lambda_1E512():
        TurnDirection(0xF5, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1E512)
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
        "#12P#00005FKoppe...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FI see...\x01",
            "You're safe.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 3, 0, 61)

    def lambda_1E5D1():
        OP_97(0x101, 0x0, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1E5D1)
    Sleep(100)

    def lambda_1E5EE():
        OP_97(0x102, 0x0, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1E5EE)
    Sleep(100)

    def lambda_1E60B():
        OP_97(0x104, 0x0, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1E60B)
    Sleep(100)

    def lambda_1E628():
        OP_97(0xF4, 0xFFFFFDA8, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1E628)
    Sleep(100)

    def lambda_1E645():
        OP_97(0xF5, 0xFFFFFDA8, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1E645)
    WaitChrThread(0x104, 0)

    def lambda_1E663():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1E663)
    WaitChrThread(0xF5, 0)
    WaitChrThread(0x103, 3)

    ChrTalk(
        0xC,
        "#11PNyaago.[It's been a while. How have you been?]\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PNyau, nyan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F...I see, thank you.\x02\x03",
            "#00202FYes, yes...\x01",
            "We will be away for a little.\x02\x03",
            "#00204FWe will be back again...for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FWhat did he say?\x02",
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
            "#00206F#5PIt seems he has been living\x01",
            "here since then...\x02\x03",
            "#00202FIt also appears he was worried\x01",
            "about us "housemates".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FHa ha, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F*giggle*, how unusually\x01",
            "faithful for a cat.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E8A4")

    ChrTalk(
        0x109,
        (
            "#12P#10102FSince we're here,\x01",
            "should we give him \x01",
            "some cat food?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E935")

    label("loc_1E8A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E8F9")

    ChrTalk(
        0x105,
        (
            "#12P#10402FSince we're here, should\x01",
            "we give him some food?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E935")

    label("loc_1E8F9")


    ChrTalk(
        0x104,
        (
            "#00304FSince we're here, should\x01",
            "we give 'im some food?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E935")

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

    # Function_57_1D96C end

    def Function_58_1EA10(): pass

    label("Function_58_1EA10")


    def lambda_1EA15():
        OP_98(0xFE, 0x0, 0x0, 0x1324, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EA15)
    Sleep(200)

    def lambda_1EA32():
        OP_98(0xFE, 0x0, 0x0, 0x1324, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1EA32)
    Sleep(200)
    BeginChrThread(0x103, 0, 0, 59)
    Sleep(200)
    BeginChrThread(0x104, 0, 0, 60)
    Sleep(200)

    def lambda_1EA61():
        OP_98(0xFE, 0x0, 0x0, 0x13EC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1EA61)
    Sleep(200)

    def lambda_1EA7E():
        OP_98(0xFE, 0x0, 0x0, 0x13EC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1EA7E)
    Return()

    # Function_58_1EA10 end

    def Function_59_1EA94(): pass

    label("Function_59_1EA94")


    def lambda_1EA99():
        OP_98(0xFE, 0x0, 0x0, 0x1194, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1EA99)
    WaitChrThread(0x103, 1)

    def lambda_1EAB7():
        OP_97(0xFE, 0x1F4, 0x0, 0x1F4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1EAB7)
    WaitChrThread(0x103, 1)
    Return()

    # Function_59_1EA94 end

    def Function_60_1EAD1(): pass

    label("Function_60_1EAD1")


    def lambda_1EAD6():
        OP_98(0xFE, 0x0, 0x0, 0x1194, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1EAD6)
    WaitChrThread(0x104, 1)

    def lambda_1EAF4():
        OP_97(0xFE, 0x1F4, 0x0, 0x1F4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1EAF4)
    WaitChrThread(0x104, 1)
    Return()

    # Function_60_1EAD1 end

    def Function_61_1EB0E(): pass

    label("Function_61_1EB0E")

    Sleep(200)

    def lambda_1EB16():
        OP_95(0xFE, -400, 0, 4100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1EB16)
    WaitChrThread(0x103, 1)

    def lambda_1EB34():
        OP_95(0xFE, 300, 0, 6100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1EB34)
    WaitChrThread(0x103, 1)
    TurnDirection(0x103, 0xC, 500)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    TurnDirection(0xC, 0x103, 500)
    Return()

    # Function_61_1EB0E end

    def Function_62_1EB70(): pass

    label("Function_62_1EB70")

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

    # Function_62_1EB70 end

    def Function_63_1EC9E(): pass

    label("Function_63_1EC9E")

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
            "#00000FIt seems that Chief Sergei's\x01",
            "old nickname was\x01",
            ""Sergei The Rear"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FIn that case, the Chief's chair\x01",
            "would correspond to "where\x01",
            "the rear commander sits".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FLet's search nearby it...\x02",
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
            "#00005F...There seems to be something\x01",
            "under the Chief's desk.\x02\x03",
            "#00000FI'll try taking it out.\x02",
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
            "#12P#00305FIsn't this thing...\x01",
            "a trunk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FIt also looks like the one\x01",
            "KeA was inside at that\x01",
            ""Black Auction".\x02\x03",
            "#10304FHu hu, choosing here as\x01",
            "the starting place could\x01",
            "be seen as a taunt too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FI-Indeed. It even caught\x01",
            "hold of Chief's nickname...\x02\x03",
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
            "On the reverse side of the trunk\x01",
            "there was a card attached.\x07\x00\x02",
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
            "The second cell is outside the city.\x01",
            "Find "The place the villagers\x01",
            "inherited along the old road".\x07\x00\x02",
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
            "#00200FAn antique doll from\x01",
            "the Rosenberg Studio...\x01",
            "No doubt about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FYes, I saw it too once.\x02\x03",
            "#00104FI think it was a doll Bell\x01",
            "loved and called "Canan".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FHu hu, giving a doll a name, even \x01",
            "Miss Mariabell has some cute sides.\x02\x03",
            "#10106FAlthough it's a bit unexpected\x01",
            "to find something stolen put\x01",
            "inside such a trunk on purpose...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FPhantom Thief B...\x01",
            "It could be that he's having some\x01",
            "proper manners towards a work of art.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FAlso, the second card...\x01",
            "The place is "outside the city", eh?\x02\x03",
            "#10306FOh boy, our search scope\x01",
            "has widen up, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FAlso, the parts that seem important are\x01",
            ""old road" and "the villagers inherited".\x02\x03",
            "#00103FThey're all words conveying a historic\x01",
            "feeling, but speaking of such places in\x01",
            "Crossbell that is a modern city...hmm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FAt any rate, let's get this thing and\x01",
            "try to go search for the next one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah, let's.\x02",
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
            "#16IRosenberg Doll C\x07\x00",
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x335, 1)
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

    # Function_63_1EC9E end

    def Function_64_1F6D3(): pass

    label("Function_64_1F6D3")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's first check the support requests,\x01",
            "and then decide our course of action.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    EventEnd(0x4)
    Return()

    # Function_64_1F6D3 end

    def Function_65_1F746(): pass

    label("Function_65_1F746")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's first check the support requests,\x01",
            "and then decide our course of action.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 11000, 850, 11350, 180)
    EventEnd(0x4)
    Return()

    # Function_65_1F746 end

    def Function_66_1F7B9(): pass

    label("Function_66_1F7B9")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's first check the support requests,\x01",
            "and then decide our course of action.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 17000, 850, 4000, 270)
    EventEnd(0x4)
    Return()

    # Function_66_1F7B9 end

    def Function_67_1F82C(): pass

    label("Function_67_1F82C")

    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F858")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1F858")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F875")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1F875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F892")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1F892")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F8AF")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1F8AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F8CC")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1F8CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F8E9")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1F8E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F906")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1F906")

    Return()

    # Function_67_1F82C end

    SaveToFile()

Try(main)
