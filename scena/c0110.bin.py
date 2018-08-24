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
        "Function_6_2835",         # 06, 6
        "Function_7_336B",         # 07, 7
        "Function_8_3F01",         # 08, 8
        "Function_9_4083",         # 09, 9
        "Function_10_42AB",        # 0A, 10
        "Function_11_4708",        # 0B, 11
        "Function_12_4752",        # 0C, 12
        "Function_13_479E",        # 0D, 13
        "Function_14_484F",        # 0E, 14
        "Function_15_4900",        # 0F, 15
        "Function_16_496F",        # 10, 16
        "Function_17_4C4C",        # 11, 17
        "Function_18_4F30",        # 12, 18
        "Function_19_5A8D",        # 13, 19
        "Function_20_5E1E",        # 14, 20
        "Function_21_5FAB",        # 15, 21
        "Function_22_6B14",        # 16, 22
        "Function_23_77C5",        # 17, 23
        "Function_24_8242",        # 18, 24
        "Function_25_9BC0",        # 19, 25
        "Function_26_9BE4",        # 1A, 26
        "Function_27_A5C5",        # 1B, 27
        "Function_28_A8BC",        # 1C, 28
        "Function_29_C5CE",        # 1D, 29
        "Function_30_D0C8",        # 1E, 30
        "Function_31_DBCE",        # 1F, 31
        "Function_32_F6B5",        # 20, 32
        "Function_33_FBEB",        # 21, 33
        "Function_34_11209",       # 22, 34
        "Function_35_11298",       # 23, 35
        "Function_36_11BE7",       # 24, 36
        "Function_37_11C24",       # 25, 37
        "Function_38_129FA",       # 26, 38
        "Function_39_131CE",       # 27, 39
        "Function_40_136BC",       # 28, 40
        "Function_41_15311",       # 29, 41
        "Function_42_156E4",       # 2A, 42
        "Function_43_17707",       # 2B, 43
        "Function_44_18801",       # 2C, 44
        "Function_45_18ED3",       # 2D, 45
        "Function_46_1AD56",       # 2E, 46
        "Function_47_1ADA0",       # 2F, 47
        "Function_48_1ADF5",       # 30, 48
        "Function_49_1AE2C",       # 31, 49
        "Function_50_1AE70",       # 32, 50
        "Function_51_1AEB4",       # 33, 51
        "Function_52_1AEEC",       # 34, 52
        "Function_53_1AF1C",       # 35, 53
        "Function_54_1BFBF",       # 36, 54
        "Function_55_1C010",       # 37, 55
        "Function_56_1CAEC",       # 38, 56
        "Function_57_1CB5E",       # 39, 57
        "Function_58_1DBE8",       # 3A, 58
        "Function_59_1DC6C",       # 3B, 59
        "Function_60_1DCA9",       # 3C, 60
        "Function_61_1DCE6",       # 3D, 61
        "Function_62_1DD48",       # 3E, 62
        "Function_63_1DE76",       # 3F, 63
        "Function_64_1E84D",       # 40, 64
        "Function_65_1E8BC",       # 41, 65
        "Function_66_1E92B",       # 42, 66
        "Function_67_1E99A",       # 43, 67
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
    Jump("loc_2831")

    label("loc_13A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1641")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_159B")

    ChrTalk(
        0x8,
        (
            "#01000FNoｱl, I'll prepare the necessary papers for\x01",
            "your reinstatement to the CGF.\x02\x03",
            "Because of the impact of the attack, support\x01",
            "requests will probably come in from all over\x01",
            "the city. Take care of them if you have time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, I'll do my very\x01",
            "best to take care of\x01",
            "them today.\x02\x03",
            "#10103F...Chief Sergei, thank\x01",
            "you for everything\x01",
            "you've done for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004FHehe, I don't need any\x01",
            "thanks.\x02\x03",
            "#01002FJust focus on your final\x01",
            "jobs so as to not have\x01",
            "any regrets.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_163C")

    label("loc_159B")


    ChrTalk(
        0x8,
        (
            "#01000FNoｱl, I'll prepare the\x01",
            "necessary papers for your\x01",
            "reinstatement to the CGF.\x02\x03",
            "#01004FDinner out tonight is my\x01",
            "treat, so make sure\x01",
            "you're back in time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_163C")

    Jump("loc_2831")

    label("loc_1641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_17C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1731")

    ChrTalk(
        0x8,
        (
            "#01003FYou finally caught Randy's\x01",
            "trail, eh?\x02\x03",
            "#01002FHehe. Now you're finally\x01",
            "prepared to bring him\x01",
            "back.\x02\x03",
            "#01001FIf your minds are made up\x01",
            "then don't dawdle. Go\x01",
            "bring that fool back here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FRight!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_17C2")

    label("loc_1731")


    ChrTalk(
        0x8,
        (
            "#01003FThe CGF is currently\x01",
            "assembling a\x01",
            "reinforcement unit.\x02\x03",
            "#01001FIf your minds are made\x01",
            "up then don't dawdle. Go\x01",
            "bring Randy back here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C2")

    Jump("loc_2831")

    label("loc_17C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_195F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C2")

    ChrTalk(
        0x8,
        (
            "#01000FBecause of the Mainz\x01",
            "occupation, support\x01",
            "requests aren't coming in.\x02\x03",
            "#01003FYou guys should focus on\x01",
            "tracking down Randy.\x02\x03",
            "#01001FGo, and be very careful.\x01",
            "I'll contact you if I\x01",
            "learn anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FRight!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_195A")

    label("loc_18C2")


    ChrTalk(
        0x8,
        (
            "#01003FThere're no support\x01",
            "requests today, so focus\x01",
            "on tracking down Randy.\x02\x03",
            "#01001FGo, and be very careful.\x01",
            "I'll contact you if I\x01",
            "learn anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_195A")

    Jump("loc_2831")

    label("loc_195F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1B94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AAE")

    ChrTalk(
        0x8,
        (
            "#01003FSection Two and the CGF are\x01",
            "investigating the Wald Wales and\x01",
            "Gnosis cases.\x02\x03",
            "#01000FNow that the transcontinental railway\x01",
            "restoration is finished, you don't\x01",
            "have to be in such a hurry.\x02\x03",
            "Regarding the matter of those bracers,\x01",
            "you can show your faces at the guild\x01",
            "if you have time during your jobs.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1B8F")

    label("loc_1AAE")


    ChrTalk(
        0x8,
        (
            "#01000FNow that the transcontinental railway\x01",
            "restoration is finished, you don't\x01",
            "have to be in such a hurry.\x02\x03",
            "Regarding the matter of those bracers,\x01",
            "you can show your faces at the guild\x01",
            "if you have time during your jobs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B8F")

    Jump("loc_2831")

    label("loc_1B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1D5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C94")

    ChrTalk(
        0x8,
        (
            "#01000F...You're back. You got\x01",
            "a call from Fran, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, we're heading to\x01",
            "the scene now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003FI see, got it.\x02\x03",
            "#01000FI'll hear your report about\x01",
            "the Doll Studio later. You\x01",
            "guys should do what you can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D56")

    label("loc_1C94")


    ChrTalk(
        0x8,
        (
            "#01000FSection Two, Sonya and the CGF\x01",
            "should be heading to the accident\x01",
            "site on West Crossbell Highway.\x02\x03",
            "I'll hear your report about the\x01",
            "Doll Studio later. You guys\x01",
            "should do what you can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D56")

    Jump("loc_2831")

    label("loc_1D5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1F83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EAA")

    ChrTalk(
        0x8,
        (
            "#01006FMany official papers are coming in\x01",
            "regarding the independence referendum.\x02\x03",
            "#01002FThere're some cases I'm worried about,\x01",
            "but... Well, we'll leave them to the\x01",
            "other sections.\x02\x03",
            "#01000FFor now, crisis management takes\x01",
            "priority. Cover not just the Doll Studio\x01",
            "inquiry, but your support requests too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F7E")

    label("loc_1EAA")


    ChrTalk(
        0x8,
        (
            "#01004FAh, if you're looking for KeA, it seems\x01",
            "she just went out to shop for dinner.\x02\x03",
            "#01002FShe said she was dropping by the library\x01",
            "for a bit... Well, if you're worried\x01",
            "about her, go check for yourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7E")

    Jump("loc_2831")

    label("loc_1F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_211F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2078")

    ChrTalk(
        0x8,
        (
            "#01000FHey, I just came back from the\x01",
            "hospital myself.\x02\x03",
            "#01003FContinue with the Cryptids\x01",
            "investigation.\x02\x03",
            "#01002FWhile the Divine Blade of Wind is\x01",
            "out of commission, increase your\x01",
            "achievements as much as you can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_211A")

    label("loc_2078")


    ChrTalk(
        0x8,
        (
            "#01003FContinue with the Cryptids\x01",
            "investigation.\x02\x03",
            "#01002FWhile the Divine Blade of Wind is\x01",
            "out of commission, increase your\x01",
            "achievements as much as you can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_211A")

    Jump("loc_2831")

    label("loc_211F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_212D")
    Jump("loc_2831")

    label("loc_212D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_22A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2215")

    ChrTalk(
        0x8,
        (
            "#01000FI'll inform the mayor\x01",
            "and CGF about the\x01",
            "terrorists.\x02\x03",
            "Dudley, I'm counting on\x01",
            "you to keep my guys\x01",
            "safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FYes, please leave it to\x01",
            "me.\x02\x03",
            "#00601F...C'mon, we're going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FRight!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_229F")

    label("loc_2215")


    ChrTalk(
        0x8,
        (
            "#01000FI don't know if something's\x01",
            "happened in the Geofront,\x01",
            "but be very careful.\x02\x03",
            "Dudley, I'm counting on you\x01",
            "to keep my guys safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_229F")

    Jump("loc_2831")

    label("loc_22A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_24A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23CD")

    ChrTalk(
        0x8,
        (
            "#01000FThat Shirley girl you ran into showed\x01",
            "up for a reason.\x02\x03",
            "#01003FI'm concerned about the actions of Red\x01",
            "Constellation, but even if we sighted\x01",
            "them there's nothing we could do.\x02\x03",
            "#01000FWell, I'll continue leaving things to\x01",
            "you. Go do what you can at your pace.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_249C")

    label("loc_23CD")


    ChrTalk(
        0x8,
        (
            "#01003FI'm concerned about the actions of Red\x01",
            "Constellation, but even if we sighted\x01",
            "them there's nothing we could do.\x02\x03",
            "#01000FWell, I'll continue leaving things to\x01",
            "you. Go do what you can at your pace.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_249C")

    Jump("loc_2831")

    label("loc_24A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_261D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25AA")

    ChrTalk(
        0x8,
        (
            "#01003FI'll be here on standby today.\x02\x03",
            "#01000FI'll keep in contact with Section One and\x01",
            "make the final preparations heading into\x01",
            "the trade conference's main event tomorrow.\x02\x03",
            "I'll contact you if anything happens, so no\x01",
            "need to worry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2618")

    label("loc_25AA")


    ChrTalk(
        0x8,
        (
            "#01003FI'll be here on standby\x01",
            "today.\x02\x03",
            "#01000FI'll contact you if\x01",
            "anything happens, so no\x01",
            "need to worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2618")

    Jump("loc_2831")

    label("loc_261D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_262B")
    Jump("loc_2831")

    label("loc_262B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2828")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_277D")

    ChrTalk(
        0x8,
        (
            "#01002FResponding to various requests with\x01",
            "citizen safety as top priority... That's\x01",
            "what the Special Support Section is.\x02\x03",
            "#01003FCao and Lechter can't be dealt with\x01",
            "ordinary means, so leave them to Section\x01",
            "One for now.\x02\x03",
            "#01000FDo not lose sight of your main duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, please leave it to\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2823")

    label("loc_277D")


    ChrTalk(
        0x8,
        (
            "#01000FResponding to various requests with\x01",
            "citizen safety as top priority... That's\x01",
            "what the Special Support Section is.\x02\x03",
            "Do not lose sight of your main duties.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2823")

    Jump("loc_2831")

    label("loc_2828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2831")

    label("loc_2831")

    TalkEnd(0x8)
    Return()

    # Function_5_1397 end

    def Function_6_2835(): pass

    label("Function_6_2835")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2AA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A47")

    ChrTalk(
        0x9,
        (
            "#01108FEveryone, uhm... sorry.\x02\x03",
            "#01103FI suddenly did what I\x01",
            "did...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FDon't worry about it,\x01",
            "KeA...\x02\x03",
            "#00004FConsidering the situation\x01",
            "we're in, it can't be\x01",
            "helped if you feel uneasy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FStopping that uneasiness\x01",
            "is our role... as  your\x01",
            "guardians.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIf anything happens,\x01",
            "don't hesitate to come\x01",
            "to us from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha. It'd make us happy\x01",
            "if you could rely on us\x01",
            "too, ya know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01108FYes... thank you.\x02\x03",
            "#01100FBe careful... KeA will\x01",
            "be waiting for you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 6)
    Jump("loc_2A9B")

    label("loc_2A47")


    ChrTalk(
        0x9,
        (
            "#01108FEveryone, thank you.\x02\x03",
            "#01100FBe careful... KeA will\x01",
            "be waiting for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A9B")

    Jump("loc_3367")

    label("loc_2AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2AAE")
    Jump("loc_3367")

    label("loc_2AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2C43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BDE")

    ChrTalk(
        0x9,
        (
            "#01103FRandy... I hope you find\x01",
            "him safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWe will, for sure. You\x01",
            "don't have to worry,\x01",
            "KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FRandy is cruel though.\x01",
            "Making KeA worry so\x01",
            "much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. When we find him,\x01",
            "we'll have to give him a\x01",
            "good scolding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01109FYes, that's right.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2C3E")

    label("loc_2BDE")


    ChrTalk(
        0x9,
        (
            "#01109FWhen Randy comes home,\x01",
            "KeA will scold him too!\x02\x03",
            "#01100FEveryone... Be very\x01",
            "careful!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C3E")

    Jump("loc_3367")

    label("loc_2C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2DE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D7E")

    ChrTalk(
        0x9,
        (
            "#01109FEhehe, actually, I went\x01",
            "out and bought a lot of\x01",
            "ingredients yesterday.\x02\x03",
            "It was raining, but I\x01",
            "had to go shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, that's our KeA.\x02\x03",
            "#00000FWe'll put them in today's\x01",
            "hot pot, so be a good kid\x01",
            "and watch the house, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01109FOkay! Lloyd, guys, be\x01",
            "careful!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2DE4")

    label("loc_2D7E")


    ChrTalk(
        0x9,
        (
            "#01100FKeA will prepare the hot\x01",
            "pot today too and wait\x01",
            "for you.\x02\x03",
            "#01109FLloyd, guys, be careful!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DE4")

    Jump("loc_3367")

    label("loc_2DE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2DF7")
    Jump("loc_3367")

    label("loc_2DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2E05")
    Jump("loc_3367")

    label("loc_2E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2E13")
    Jump("loc_3367")

    label("loc_2E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2E21")
    Jump("loc_3367")

    label("loc_2E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2FF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F83")

    ChrTalk(
        0x9,
        (
            "#01100FEveryone, have a safe\x01",
            "trip!\x02\x03",
            "#01109FEhehe, you be careful\x01",
            "too, ok Dudley?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FDidn't I tell you not to\x01",
            "address me so casually!?\x02",
        )
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
            "#00606F...Damn, whatever! Guys,\x01",
            "we're leaving, on the\x01",
            "double!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Hmm. As expected, not\x01",
            "even Dudley is a match\x01",
            "for KeA.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2FEC")

    label("loc_2F83")


    ChrTalk(
        0x9,
        (
            "#01109FEveryone, have a safe\x01",
            "trip!\x02\x03",
            "Ehehe, you be careful\x01",
            "too, ok Dudley?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00603F(Honestly...)\x02",
    )

    CloseMessageWindow()

    label("loc_2FEC")

    Jump("loc_3367")

    label("loc_2FF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_END)), "loc_3104")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B4")

    ChrTalk(
        0x9,
        (
            "#01105FThat Sieg was cool,\x01",
            "right?\x02\x03",
            "#01109FAnd he's so smart. KeA\x01",
            "wants to see him again.\x02",
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
    Jump("loc_30FF")

    label("loc_30B4")


    ChrTalk(
        0x9,
        (
            "#01105FThat Sieg was cool,\x01",
            "right?\x02\x03",
            "#01109FKeA wants to see him\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30FF")

    Jump("loc_3367")

    label("loc_3104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_3318")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3287")

    ChrTalk(
        0x9,
        (
            "#01102FThe maple muffins will\x01",
            "be good until tomorrow.\x02\x03",
            "#01109FEat them for lunch if\x01",
            "you get hungry during\x01",
            "your jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thanks KeA.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, they were very\x01",
            "good, I'm looking forward\x01",
            "to getting hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01102FEhehe, then KeA will\x01",
            "make them again.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 1)), scpexpr(EXPR_END)), "loc_327F")

    ChrTalk(
        0x101,
        (
            "#00002F(Haha, thank goodness...\x01",
            "Looks like she's cheered\x01",
            "up.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_327F")

    SetScenarioFlags(0x0, 3)
    Jump("loc_3313")

    label("loc_3287")


    ChrTalk(
        0x9,
        (
            "#01104FHumhuhuum♪ I have to\x01",
            "hurry and finish the\x01",
            "laundry.\x02\x03",
            "#01100FEat the maple muffins\x01",
            "for lunch if you get\x01",
            "hungry during your jobs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3313")

    Jump("loc_3367")

    label("loc_3318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3326")
    Jump("loc_3367")

    label("loc_3326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3334")
    Jump("loc_3367")

    label("loc_3334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3342")
    Jump("loc_3367")

    label("loc_3342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_3350")
    Jump("loc_3367")

    label("loc_3350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_335E")
    Jump("loc_3367")

    label("loc_335E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3367")

    label("loc_3367")

    TalkEnd(0xFE)
    Return()

    # Function_6_2835 end

    def Function_7_336B(): pass

    label("Function_7_336B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3488")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_346D")

    ChrTalk(
        0xA,
        "#01200FGrrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FZeit... He's worked up\x01",
            "about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FBecause of the situation,\x01",
            "his wariness is probably\x01",
            "higher than usual.\x02\x03",
            "#00001FZeit, please take care of\x01",
            "KeA and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01200FWoof!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3483")

    label("loc_346D")


    ChrTalk(
        0xA,
        "#01200FGrrrrr...\x02",
    )

    CloseMessageWindow()

    label("loc_3483")

    Jump("loc_3EFD")

    label("loc_3488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3496")
    Jump("loc_3EFD")

    label("loc_3496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_35C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A4")

    ChrTalk(
        0xA,
        "#01200FGrrrowl... Woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F"Jaegers are masters of the\x01",
            "battlefield. Be extremely careful\x01",
            "when entering their territory."\x02\x03",
            "...He says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThank you, Zeit. We'll\x01",
            "heed your advice.\x02\x03",
            "We mustn't take on the\x01",
            "jaegers directly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_35C1")

    label("loc_35A4")


    ChrTalk(
        0xA,
        "#01200FGrrrowl... Woof.\x02",
    )

    CloseMessageWindow()

    label("loc_35C1")

    Jump("loc_3EFD")

    label("loc_35C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_369F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3683")

    ChrTalk(
        0xA,
        "#01200FGrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...You're right. Randy\x01",
            "is a big idiot.\x02\x03",
            "#00200FWe'll do whatever's\x01",
            "necessary to bring him\x01",
            "back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah... Of course!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_369A")

    label("loc_3683")


    ChrTalk(
        0xA,
        "#01200FGrrrowl...\x02",
    )

    CloseMessageWindow()

    label("loc_369A")

    Jump("loc_3EFD")

    label("loc_369F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_36D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36BA")
    Call(0, 8)
    Jump("loc_36D2")

    label("loc_36BA")


    ChrTalk(
        0xA,
        "#01203FGrrrrowl...\x02",
    )

    CloseMessageWindow()

    label("loc_36D2")

    Jump("loc_3EFD")

    label("loc_36D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_37C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37A0")

    ChrTalk(
        0xA,
        "#01200FGrrrowl... Woof, woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt seems even Zeit is\x01",
            "feeling that something\x01",
            "serious has happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYeah... Let's be careful\x01",
            "and head to the scene.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_37C3")

    label("loc_37A0")


    ChrTalk(
        0xA,
        "#01200FGrrrowl... Woof, woof.\x02",
    )

    CloseMessageWindow()

    label("loc_37C3")

    Jump("loc_3EFD")

    label("loc_37C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_37EF")

    ChrTalk(
        0xA,
        "#01203F...Grrowl...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EFD")

    label("loc_37EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_390B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38EA")

    ChrTalk(
        0xA,
        "#01200FGrrowl... Woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F"Go, and be careful"\x01",
            "...he says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIt seems it'll be quite\x01",
            "dangerous when we fight\x01",
            "the Cryptids...\x02\x03",
            "#00000FThank you, Zeit. If\x01",
            "things get dangerous,\x01",
            "give us your help again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3906")

    label("loc_38EA")


    ChrTalk(
        0xA,
        "#01200FGrrowl... Woof.\x02",
    )

    CloseMessageWindow()

    label("loc_3906")

    Jump("loc_3EFD")

    label("loc_390B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3919")
    Jump("loc_3EFD")

    label("loc_3919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3BDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BB8")

    ChrTalk(
        0xA,
        "#01200FGrrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FHmph. A self-important wolf as always.\x02\x03",
            "#00600FStill, since you're treated like a police\x01",
            "dog, there will be times when we'll need your\x01",
            "help. Be prepared to sortie at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01200F...Woof.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A49")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_3A49")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A7D")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_3A7D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AB1")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_3AB1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AE5")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_3AE5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B19")
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_3B19")

    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00306F(How can he call others\x01",
            "self-important,\x01",
            "right...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Haha, It's Dudley's way of\x01",
            "encouraging him. There's\x01",
            "nothing we can do.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3BD5")

    label("loc_3BB8")


    ChrTalk(
        0xA,
        "#01200FGrrrowl... Woof.\x02",
    )

    CloseMessageWindow()

    label("loc_3BD5")

    Jump("loc_3EFD")

    label("loc_3BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_3C05")

    ChrTalk(
        0xA,
        "#01200FGrrrowl... Woof.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EFD")

    label("loc_3C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3D33")

    ChrTalk(
        0xA,
        "#01200FGrrrowl...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D2E")

    ChrTalk(
        0x101,
        (
            "#00005FOh, right, Zeit... You\x01",
            "watched the unveiling of\x01",
            "Orchis Tower with KeA, right?\x02\x03",
            "Somehow KeA looks down. Has\x01",
            "anything happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01200FGrrrowl... Woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FUhhm, with Tio not around,\x01",
            "we don't understand him,\x01",
            "as you'd expect.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_3D2E")

    Jump("loc_3EFD")

    label("loc_3D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3E25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E04")

    ChrTalk(
        0xA,
        "#01200FGrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHey, Zeit.\x02\x03",
            "#00309FHaha, thanks for guidin'\x01",
            "us back at the old mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, please help us\x01",
            "from now on too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01200FGrrowl... Woof.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3E20")

    label("loc_3E04")


    ChrTalk(
        0xA,
        "#01200FGrrowl... Woof.\x02",
    )

    CloseMessageWindow()

    label("loc_3E20")

    Jump("loc_3EFD")

    label("loc_3E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3EF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EDA")

    ChrTalk(
        0xA,
        "#01203FGrrrowl... Woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOn rainy days, even Zeit\x01",
            "looks bored.\x02\x03",
            "Well, watch over the\x01",
            "house quietly for us\x01",
            "today, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01200F...Woof.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3EEF")

    label("loc_3EDA")


    ChrTalk(
        0xA,
        "#01200F...Woof.\x02",
    )

    CloseMessageWindow()

    label("loc_3EEF")

    Jump("loc_3EFD")

    label("loc_3EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3EFD")

    label("loc_3EFD")

    TalkEnd(0xFE)
    Return()

    # Function_7_336B end

    def Function_8_3F01(): pass

    label("Function_8_3F01")

    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xA,
        "#01200FGrrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Nyaa~~ [I'm hungry]\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt looks like that both Zeit\x01",
            "and Koppe are looking forward\x01",
            "to tonight's hot pot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FHuh? But don't cats have\x01",
            ""cat tongue"? That is,\x01",
            "they hate hot food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FAren't animals of the dog\x01",
            "family the same? Hehe. What\x01",
            "a strange way to put it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...I'll cool it down for\x01",
            "them.\x02",
        )
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

    # Function_8_3F01 end

    def Function_9_4083(): pass

    label("Function_9_4083")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4094")
    Jump("loc_42A7")

    label("loc_4094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_41E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41C8")

    ChrTalk(
        0xFE,
        "Nyanyayayaa~㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, he's really\x01",
            "eating it nicely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt seems he misses the\x01",
            "cat food flavor.\x02\x03",
            "It appears that he went\x01",
            "out to catch his own food\x01",
            "when we weren't around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FWow, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha. Unexpectedly,\x01",
            "Koppe has a bold side.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_41DC")

    label("loc_41C8")


    ChrTalk(
        0xFE,
        "Nyanyayayaa~㈱\x02",
    )

    CloseMessageWindow()

    label("loc_41DC")

    Jump("loc_42A7")

    label("loc_41E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_41EF")
    Jump("loc_42A7")

    label("loc_41EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4278")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_420A")
    Call(0, 8)
    Jump("loc_4273")

    label("loc_420A")


    ChrTalk(
        0xFE,
        "Nyaa~~ [I'm hungry]\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F(There's KeA at home, so\x01",
            "there's no need for us\x01",
            "to feed him today.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4273")

    Jump("loc_42A7")

    label("loc_4278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4286")
    Jump("loc_42A7")

    label("loc_4286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_42A7")

    ChrTalk(
        0xFE,
        "Nya～～go. [Hello]\x02",
    )

    CloseMessageWindow()

    label("loc_42A7")

    TalkEnd(0xFE)
    Return()

    # Function_9_4083 end

    def Function_10_42AB(): pass

    label("Function_10_42AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45C5")

    ChrTalk(
        0xB,
        (
            "#05928FThe reason Arios had Shizuku\x01",
            "discharged forcibly... I didn't\x01",
            "know it was such a serious one.\x02\x03",
            "#05923FConsidering Shizuku's safety, I\x01",
            "don't think there's anything we\x01",
            "can do...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, that's right...\x02\x03",
            "#00005F...By the way Cecil.\x01",
            "How's the situation at\x01",
            "St. Ursula?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, I'm concerned about\x01",
            "the hospitalized policemen\x01",
            "and Ilya's condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05920FThere's confusion even at\x01",
            "the hospital, but patients\x01",
            "are being treated normally.\x02\x03",
            "#05924FFran has been recovering\x01",
            "well and was transferred to\x01",
            "the general ward...\x02\x03",
            "#05920FAnd Mr. Donovan regained\x01",
            "consciousness not long ago\x01",
            "as well.\x02\x03",
            "#05928F...Although Ilya still\x01",
            "won't wake up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FI hope she gets back on\x01",
            "her feet fast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#05924FYes... I hope so too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 1)
    Jump("loc_4704")

    label("loc_45C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46A5")

    ChrTalk(
        0xB,
        (
            "#05920FThere's confusion even at\x01",
            "the hospital, but patients\x01",
            "are being treated normally.\x02\x03",
            "#05923FAt any rate... I will watch\x01",
            "the place with KeA.\x02\x03",
            "#05920FThe situation looks\x01",
            "serious, so be very\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4704")

    label("loc_46A5")


    ChrTalk(
        0xB,
        (
            "#05920FI will watch the place\x01",
            "with KeA.\x02\x03",
            "The situation looks\x01",
            "serious, so be very\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4704")

    TalkEnd(0xFE)
    Return()

    # Function_10_42AB end

    def Function_11_4708(): pass

    label("Function_11_4708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_471A")
    Call(0, 16)
    Jump("loc_4751")

    label("loc_471A")

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

    label("loc_4751")

    Return()

    # Function_11_4708 end

    def Function_12_4752(): pass

    label("Function_12_4752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4764")
    Call(0, 17)
    Jump("loc_479D")

    label("loc_4764")

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

    label("loc_479D")

    Return()

    # Function_12_4752 end

    def Function_13_479E(): pass

    label("Function_13_479E")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F...Oh yeah, KeA said she\x01",
            "was leaving for Sunday\x01",
            "School.\x02\x03",
            "Chief is out, so maybe\x01",
            "we should leave\x01",
            "together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FRight, let's ask her.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 800, 0, 1890, 0)
    EventEnd(0x4)
    Return()

    # Function_13_479E end

    def Function_14_484F(): pass

    label("Function_14_484F")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F...Oh yeah, KeA said she\x01",
            "was leaving for Sunday\x01",
            "School.\x02\x03",
            "Chief is out, so maybe\x01",
            "we should leave\x01",
            "together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FRight, let's ask her.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_14_484F end

    def Function_15_4900(): pass

    label("Function_15_4900")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FKeA is going to Sunday\x01",
            "School. Let's use the rear\x01",
            "entrance as a shortcut.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -1330, 0, 71380, 268)
    EventEnd(0x4)
    Return()

    # Function_15_4900 end

    def Function_16_496F(): pass

    label("Function_16_496F")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A09")
    SetChrPos(0x1A5, 169520, 0, 61730, 0)

    label("loc_4A09")

    OP_0D()

    ChrTalk(
        0x102,
        "#6P#00100FThis is Tio's room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FShe's working in Lｳman\x01",
            "State, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, she went to the\x01",
            "Epstein Foundation\x01",
            "research lab with Jona.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWith recent revisions to state law, development\x01",
            "of the orbal net has been proceeding. I wonder\x01",
            "if their trip is related to helping with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10103FI don't understand complicated\x01",
            "things, but... They seem to\x01",
            "have it hard too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C06")

    ChrTalk(
        0x1A5,
        (
            "#12P#01100FI hope Tio comes home\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, seriously.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C34")

    label("loc_4C06")


    ChrTalk(
        0x101,
        (
            "#00000FYeah, I hope Tio comes\x01",
            "home soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C34")

    OP_5A()
    SetChrPos(0x0, 169990, 0, 63110, 180)
    SetScenarioFlags(0x13B, 3)
    EventEnd(0x5)
    Return()

    # Function_16_496F end

    def Function_17_4C4C(): pass

    label("Function_17_4C4C")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CE6")
    SetChrPos(0x1A5, 13500, 0, 61420, 0)

    label("loc_4CE6")

    OP_0D()

    ChrTalk(
        0x101,
        "#12P#00000FThis is Randy's room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FRandy is in the middle of\x01",
            "rehabilitation training at\x01",
            "Tangram Gate with the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FAh, they were dosed with\x01",
            "that drug in the cult\x01",
            "incident, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103FYes... There were no\x01",
            "severe aftereffects,\x01",
            "though.\x02\x03",
            "#10108FIt will take some time\x01",
            "for them to recover their\x01",
            "stamina and senses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FI see... I hope the CGF\x01",
            "recover quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4EE1")

    ChrTalk(
        0x1A5,
        (
            "#12P#01100FI hope Randy comes home\x01",
            "soon, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHaha, seriously.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F18")

    label("loc_4EE1")


    ChrTalk(
        0x102,
        (
            "#00100FYes. I hope Randy comes\x01",
            "home soon as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F18")

    OP_5A()
    SetChrPos(0x0, 14040, 0, 63300, 180)
    SetScenarioFlags(0x13B, 4)
    EventEnd(0x5)
    Return()

    # Function_17_4C4C end

    def Function_18_4F30(): pass

    label("Function_18_4F30")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F57")
    Call(0, 21)
    Return()

    label("loc_4F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4FAA")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The terminal's orbal\x01",
            "power is failing.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    label("loc_4FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5100")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The terminal's orbal\x01",
            "power is failing.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50FC")

    ChrTalk(
        0x101,
        (
            "#00003F...It looks like the\x01",
            "orbal power itself isn't\x01",
            "reaching it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FFor now, I'm just glad\x01",
            "it isn't broken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, if we need to use\x01",
            "a terminal, let's do it\x01",
            "at the Merkabah.\x02",
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

    label("loc_50FC")

    TalkEnd(0xFF)
    Return()

    label("loc_5100")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_511A")
    OP_C9(0x0, 0x4)
    OP_C9(0x0, 0x100)

    label("loc_511A")

    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5133")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5877")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_516C"),
        (1, "loc_5328"),
        (2, "loc_5862"),
        (3, "loc_586A"),
        (SWITCH_DEFAULT, "loc_5872"),
    )


    label("loc_516C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_517F")
    OP_2B(0x94, 0xFFFF)
    Jump("loc_5323")

    label("loc_517F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_519A")
    OP_2B(0x8E, 0x8F, 0x90, 0x91, 0x92, 0xFFFF)
    Jump("loc_5323")

    label("loc_519A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_51FD")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Currently there are no\x01",
            "support requests.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_5323")

    label("loc_51FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5218")
    OP_2B(0x8B, 0x8C, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_5323")

    label("loc_5218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5253")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5241")
    OP_2B(0x85, 0x86, 0x87, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_524E")

    label("loc_5241")

    OP_2B(0x85, 0x86, 0x88, 0x80, 0x83, 0xFFFF)

    label("loc_524E")

    Jump("loc_5323")

    label("loc_5253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_526C")
    OP_2B(0x80, 0x81, 0x82, 0x83, 0xFFFF)
    Jump("loc_5323")

    label("loc_526C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_527A")
    Jump("loc_5323")

    label("loc_527A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5297")
    OP_2B(0x79, 0x7A, 0x7B, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_5323")

    label("loc_5297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_END)), "loc_52B4")
    OP_2B(0x74, 0x75, 0x76, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_5323")

    label("loc_52B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_52CD")
    OP_2B(0x6F, 0x70, 0x71, 0x72, 0xFFFF)
    Jump("loc_5323")

    label("loc_52CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5301")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_52F1")
    OP_2B(0x6A, 0x6B, 0x6C, 0x6D, 0x67, 0xFFFF)
    Jump("loc_52FC")

    label("loc_52F1")

    OP_2B(0x6A, 0x6B, 0x6C, 0x67, 0xFFFF)

    label("loc_52FC")

    Jump("loc_5323")

    label("loc_5301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 7)), scpexpr(EXPR_END)), "loc_5318")
    OP_2B(0x65, 0x66, 0x67, 0xFFFF)
    Jump("loc_5323")

    label("loc_5318")

    OP_2B(0x65, 0x66, 0x67, 0x68, 0xFFFF)

    label("loc_5323")

    Jump("loc_5872")

    label("loc_5328")

    SetMapFlags(0x40000000)
    OP_E5(0x7)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_541D")
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        (
            "This is Crossbell\x01",
            "Police.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_53F5")

    AnonymousTalk(
        0xFF,
        (
            "I will receive your\x01",
            "report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        (
            "Report processing,\x01",
            "complete. Thank you for\x01",
            "your hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5418")

    label("loc_53F5")


    AnonymousTalk(
        0xFF,
        (
            "There no reportable\x01",
            "requests.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5418")

    Jump("loc_5854")

    label("loc_541D")

    SetChrName("Receptionist Fran")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5474")
    Sound(3062, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Yes, this is Crossbell\x01",
            "Poliiice!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54A9")

    label("loc_5474")

    Sound(3061, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Everyone, thank you for\x01",
            "your hard wooork.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_5744")
    Sound(3067, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Then, I'll receive your\x01",
            "report, okaaay?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56AA")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_552A"),
        (13, "loc_5577"),
        (12, "loc_55C0"),
        (SWITCH_DEFAULT, "loc_5605"),
    )


    label("loc_552A")

    Sound(3075, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "1st Class!── Lloyd,\x01",
            "you're too amazing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5605")

    label("loc_5577")

    Sound(3074, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "2nd Class!── Lloyd,\x01",
            "you're amazing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5605")

    label("loc_55C0")

    Sound(3073, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "3rd Class!── Lloyd, you\x01",
            "did it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5605")

    label("loc_5605")

    Sound(3076, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "I will immediately send\x01",
            "over your special item!\x02",
        )
    )

    CloseMessageWindow()
    Sound(3077, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Thank you for your hard\x01",
            "wooork! I hope to be\x01",
            "working with you agaaain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_573C")

    label("loc_56AA")

    Sound(3078, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "That's all for your\x01",
            "report, right?\x02",
        )
    )

    CloseMessageWindow()
    Sound(3079, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Then, please contact me\x01",
            "again the next time you\x01",
            "complete a requeeest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_573C")

    SetScenarioFlags(0x0, 1)
    Jump("loc_5854")

    label("loc_5744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_57C9")
    Sound(3063, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Oh... Didn't you just\x01",
            "report?\x02",
        )
    )

    CloseMessageWindow()
    Sound(3064, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Please do it again when\x01",
            "you complete a request.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5854")

    label("loc_57C9")

    Sound(3065, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Oh... It seems you don't\x01",
            "have any requests you\x01",
            "can repooort.\x02",
        )
    )

    CloseMessageWindow()
    Sound(3066, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Please, let's work\x01",
            "together agaaain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5854")

    OP_57(0x0)
    OP_E5(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_5872")

    label("loc_5862")

    Call(0, 20)
    Jump("loc_5872")

    label("loc_586A")

    Call(0, 19)
    Jump("loc_5872")

    label("loc_5872")

    Jump("loc_5133")

    label("loc_5877")

    OP_E5(0x6)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x68, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58BD")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 24)
    Return()

    label("loc_58BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58F5")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 27)
    Return()

    label("loc_58F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5934")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 32)
    Return()

    label("loc_5934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_596C")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 39)
    Return()

    label("loc_596C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59F9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_59C3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59BE")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 41)
    Return()

    label("loc_59BE")

    Jump("loc_59F4")

    label("loc_59C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59F4")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 41)
    Return()

    label("loc_59F4")

    Jump("loc_5A7A")

    label("loc_59F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A12")
    SetScenarioFlags(0x168, 2)
    Call(0, 67)
    Jump("loc_5A7A")

    label("loc_5A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x92, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A51")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 44)
    Return()

    label("loc_5A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_5A68")
    ClearScenarioFlags(0x22, 3)
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    label("loc_5A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_5A7A")
    ClearScenarioFlags(0x22, 6)
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    label("loc_5A7A")

    FadeToBright(300, 0)
    OP_0D()
    OP_E5(0xB)
    Call(0, 67)
    TalkEnd(0xFF)
    Return()

    # Function_18_4F30 end

    def Function_19_5A8D(): pass

    label("Function_19_5A8D")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5ABB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x94, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_5AB6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5AB6")

    Jump("loc_5DCB")

    label("loc_5ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5AFB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x92, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AF6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5AF6")

    Jump("loc_5DCB")

    label("loc_5AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5B13")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5DCB")

    label("loc_5B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5B53")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B4E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5B4E")

    Jump("loc_5DCB")

    label("loc_5B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5BDD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5BA6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BA1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5BA1")

    Jump("loc_5BD8")

    label("loc_5BA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BD8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5BD8")

    Jump("loc_5DCB")

    label("loc_5BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5C16")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C11")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C11")

    Jump("loc_5DCB")

    label("loc_5C16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_5C2E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5DCB")

    label("loc_5C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5C75")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C70")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C70")

    Jump("loc_5DCB")

    label("loc_5C75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_END)), "loc_5CBC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CB7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5CB7")

    Jump("loc_5DCB")

    label("loc_5CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5CF5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CF0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5CF0")

    Jump("loc_5DCB")

    label("loc_5CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5D6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_5D3E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6D, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D39")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D39")

    Jump("loc_5D69")

    label("loc_5D3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D69")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D69")

    Jump("loc_5DCB")

    label("loc_5D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 7)), scpexpr(EXPR_END)), "loc_5DA0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D9B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D9B")

    Jump("loc_5DCB")

    label("loc_5DA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x65, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x68, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DCB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DCB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E1D")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please check all support\x01",
            "requests.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_5E1D")

    Return()

    # Function_19_5A8D end

    def Function_20_5E1E(): pass

    label("Function_20_5E1E")

    OP_E5(0x6)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 3)), scpexpr(EXPR_END)), "loc_5E40")
    SetScenarioFlags(0x2A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E40")
    ClearScenarioFlags(0x2A, 0)

    label("loc_5E40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_END)), "loc_5E5D")
    SetScenarioFlags(0x2A, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E5D")
    ClearScenarioFlags(0x2A, 1)

    label("loc_5E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_END)), "loc_5E7A")
    SetScenarioFlags(0x2A, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E7A")
    ClearScenarioFlags(0x2A, 2)

    label("loc_5E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 6)), scpexpr(EXPR_END)), "loc_5E97")
    SetScenarioFlags(0x2A, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E97")
    ClearScenarioFlags(0x2A, 3)

    label("loc_5E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_END)), "loc_5EB4")
    SetScenarioFlags(0x2A, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EB4")
    ClearScenarioFlags(0x2A, 4)

    label("loc_5EB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_END)), "loc_5ED1")
    SetScenarioFlags(0x2A, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5ED1")
    ClearScenarioFlags(0x2A, 5)

    label("loc_5ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_END)), "loc_5EDD")
    SetScenarioFlags(0x2A, 6)

    label("loc_5EDD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F2F")
    RunExpression(0x6, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopBGM(0x0)
    Jump("loc_5FAA")

    label("loc_5F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5F81")
    OP_24(0x80)
    RunExpression(0x6, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()
    Sound(128, 1, 50, 0)
    Jump("loc_5FAA")

    label("loc_5F81")

    RunExpression(0x6, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()

    label("loc_5FAA")

    Return()

    # Function_20_5E1E end

    def Function_21_5FAB(): pass

    label("Function_21_5FAB")

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
            "#6P#00004FAccording to Chief Roberts, we\x01",
            "have to install this memory\x01",
            "quartz on the terminal, right?\x02\x03",
            "#00000FSo then... Elie, if you\x01",
            "please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FYes, I'll give it a try.\x02",
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
            "Elie installed "Pom!"\x01",
            "beta version on the\x01",
            "terminal.\x07\x00\x02",
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
            "#12P#00104FAnd there we go.\x02\x03",
            "#00100FI also input Chief\x01",
            "Roberts' account.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWow, you're pretty good\x01",
            "at that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FYou're good at a lot of\x01",
            "different things.\x02\x03",
            "#10100FYou even know a lot\x01",
            "about politics and law.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#11P#00102FHaha, well I can only do\x01",
            "this because I watched Tio\x01",
            "do it.\x02\x03",
            "#00104FThere's an instruction\x01",
            "manual too, and if you read\x01",
            "it, it's not that difficult.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00002FEven still, this really\x01",
            "helps us out.\x02\x03",
            "#00006FBecause I'm only now\x01",
            "getting used to the\x01",
            "terminal keyboard.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#00109FHaha, you're welcome.\x02\x03",
            "#00100FThen... Should we\x01",
            "contact Chief Roberts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00000FYeah, let's give him a\x01",
            "call.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_645F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_645F)
    Sleep(50)

    def lambda_646F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_646F)
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
            "─Hey Lloyd. The install\x01",
            "went well, I take it?\x07\x00\x02",
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
            "#00000FYeah, everything's fine.\x01",
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
            "Then, would you try a match\x01",
            "against me?\x02\x03",
            "Try starting "Pom!" from the\x01",
            "terminal.\x02\x03",
            "From there, my account should\x01",
            "display. You can challenge me by\x01",
            "selecting it.\x02\x03",
            "...That's right. Since you're the\x01",
            "leader, how about you challenge\x01",
            "me as the SSS's representative?\x07\x00\x02",
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
            "#00005F??? Uhhh, I guess.\x07\x00\x02",
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
        "#12P#00100FThen, you can sit here.\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x14, 0x1F4)

    def lambda_6744():
        OP_9B(0x1, 0xFE, 0xB4, 0x5DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6744)
    Sleep(200)

    def lambda_675C():
        OP_95(0xFE, 15970, 850, 9800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_675C)

    def lambda_6776():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6776)
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
            "Haha, can you win\x01",
            "against me, the\x01",
            "developer?\x07\x00\x02",
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
            "#4SCan I entrust Tio to\x01",
            "you? ...I'll find out\x01",
            "for sure this time!#3S\x07\x00\x02",
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
            "#6P#10112F...So that's what he\x01",
            "really thinks, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10309FAhaha, he seems to be\x01",
            "quite the doting parent,\x01",
            "eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FUmm, was that the reason\x01",
            "you specifically requested\x01",
            "the Support Section?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ahaha. No, no... Since we're\x01",
            "having a match, I wanted to\x01",
            "get fired up a little.\x02\x03",
            "Ok then, let the battle\x01",
            "begin!\x07\x00\x02",
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

    label("loc_6A62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6AF0")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A9A")
    Call(0, 20)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6AEB")

    label("loc_6A9A")


    AnonymousTalk(
        0x101,
        (
            "#0000FChief Roberts is waiting,\x01",
            "so I'll try launching\x01",
            ""Pom!" right away.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6AEB")

    Jump("loc_6A62")

    label("loc_6AF0")

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

    # Function_21_5FAB end

    def Function_22_6B14(): pass

    label("Function_22_6B14")

    EventBegin(0x0)
    SoundLoad(803)
    SoundLoad(128)
    Sound(128, 2, 50, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B99")
    OP_2C(0x6C, 0x1)

    ChrTalk(
        0x101,
        (
            "#6P#00009FAll right, I managed to\x01",
            "win!\x02\x03",
            "#00004F(Hmm. That was pretty\x01",
            "fun.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6C, 0x1, 0x2)
    Jump("loc_6BE5")

    label("loc_6B99")


    ChrTalk(
        0x101,
        (
            "#6P#00006F...I lost, huh.\x02\x03",
            "#00001F(Hmm. That was\x01",
            "frustrating...)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6C, 0x1, 0x3)

    label("loc_6BE5")


    ChrTalk(
        0x102,
        (
            "#12P#00109FHaha, you seemed quite\x01",
            "hooked somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105F...Umm, it's just my\x01",
            "impression from\x01",
            "spectating, but...\x02\x03",
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
            "#5P#00012FN-No... He was obviously\x01",
            "holding back, right?\x02\x03",
            "#00003FIf skill levels weren't\x01",
            "about the same, I don't\x01",
            "think it'd be a good test...\x02",
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
        (
            "#6P#00000FYes, Special Support\x01",
            "Sec─\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "─Wooow, what a great\x01",
            "match!\x02\x03",
            "A grand battle that will\x01",
            "go down in the history\x01",
            "books! I'm still excited!!\x07\x00\x02",
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
            "#6P#00006F(I guess that actually\x01",
            "was his best, huh...)\x02\x03",
            "#00012FS-So... How were the\x01",
            "test results?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, they were perfect!\x02\x03",
            "There was no noticeable issue\x01",
            "playing across the city, and\x01",
            "the connection was perfect.\x02\x03",
            "I can only say that it was a\x01",
            "great success.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#6P#00000FIs that so? Well good\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Soon, I'll update the beta\x01",
            "version you installed to the\x01",
            "release version.\x02\x03",
            "When the game is released,\x01",
            "the number of people you can\x01",
            "challenge will increase, too.\x02\x03",
            "I hope you exchange accounts\x01",
            "with many people, and enjoy\x01",
            "the game as much as you like.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_727A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_720D")
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Of course, I intend to\x01",
            "get my revenge too one\x01",
            "day!!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_727A")

    label("loc_720D")

    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Of course, I'll take you\x01",
            "on whenever you like to\x01",
            "get revenge for today!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_727A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72E7")
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Of course, I intend to\x01",
            "get my revenge too one\x01",
            "day!!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_7354")

    label("loc_72E7")

    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Of course, I'll take you\x01",
            "on whenever you like to\x01",
            "get revenge for today!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7354")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00012FHa-haha... Please go\x01",
            "easy on me.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, thank you very\x01",
            "much for your\x01",
            "cooperation.\x02\x03",
            "I have other work to\x01",
            "attend to, so allow me\x01",
            "to excuse myself.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYou're welcome. Please\x01",
            "let us know if you ever\x01",
            "need our help.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Alright, I'll do just\x01",
            "that. ...Bye then!\x07\x00\x02",
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
            "#00004F*sigh*... Looks like it\x01",
            "went well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FHaha, nice work.\x02\x03",
            "#00104FI'm not sure how to say it,\x01",
            "but I felt that request was\x01",
            "very like the chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FHaha, that's true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FAnyhow, it looks like we'll\x01",
            "be able to enjoy this game\x01",
            "from here on out.\x02\x03",
            "#10309FWell? How about aiming to\x01",
            "be the Pom! master of\x01",
            "Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell for starters, I\x01",
            "could never stand up to\x01",
            "Tio, but...\x02\x03",
            "#00000FStill, I could practice\x01",
            "while taking a breather\x01",
            "between jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FHaha, that's true.\x02",
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
            "Quest [Beta Test\x01",
            "Participation]\x07\x00\x01",
            "completed!\x02",
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

    # Function_22_6B14 end

    def Function_23_77C5(): pass

    label("Function_23_77C5")

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
        "#00104F...Yes. A few came in.\x02",
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
            "#10302FSo these are the "support\x01",
            "requests" the Special\x01",
            "Support Section handles.\x02",
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
            "#00004FYeah, they're usually\x01",
            "sent to us all together\x01",
            "once per day.\x02\x03",
            "#00000FIt's left to our\x01",
            "discretion how many to\x01",
            "do, but...\x02\x03",
            "Those marked "urgent"\x01",
            "absolutely must be done.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10304FI see. That's logical.\x02\x03",
            "#10300FAnd for the ones with a\x01",
            "deadline further out, it's\x01",
            "ok to do them the next day?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00000FYeah, exactly.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00104FAt any rate, if we check\x01",
            "them daily, the displayed\x01",
            "deadline will change.\x02\x03",
            "#00100FAnd we can check request\x01",
            "status from the Detective\x01",
            "Notebook, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10105FThe Detective\x01",
            "Notebook...\x02",
        )
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
            "#12P#10100FIt's that black notebook\x01",
            "you write in sometimes?\x02",
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
            "#00003FBasically, we write\x01",
            "developments in investigations\x01",
            "or support requests in it.\x02\x03",
            "By doing that, it's possible\x01",
            "to keep an eye on multiple\x01",
            "cases.\x02\x03",
            "#00000FAnd, it's also an operations\x01",
            "manual for our tactical\x01",
            "orbments─ the ENIGMA.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10305FHmm. It's rather useful,\x01",
            "then.\x02\x03",
            "#10304FAlthough I feel like even\x01",
            "this kind of notebook will\x01",
            "be orbalized someday.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00102FThat's right... I heard Tio\x01",
            "say they were researching\x01",
            "something like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10112FHmm. I think there'd be\x01",
            "resistance against orbalizing\x01",
            "things that much...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00002FI agree. Pen and paper\x01",
            "are better suited to\x01",
            "this kind of thing.\x02",
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
            "#00004F#5P─Well, that's the Special\x01",
            "Support Section's fundamental\x01",
            "style, roughly speaking.\x02\x03",
            "#00000FFirst, let's use the terminal\x01",
            "to check each of today's\x01",
            "support requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10102FRoger that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10309FHehe, I can't wait to\x01",
            "see them.\x02",
        )
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
            "Inspecting the Support Section terminal with ○ and\x01",
            "selecting [Check Support Requests] will display the\x01",
            "list of job requests (quests) for Lloyd and the others.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Some requests are urgent and must be done.\x01",
            "These are marked "Urgent" and completing\x01",
            "them will advance the main story.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Other requests need not be completed, although completing\x01",
            "them will earn DP and mira. Also, if the deadline expires,\x01",
            "they will disappear, so please be cautious of this.\x02",
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

    # Function_23_77C5 end

    def Function_24_8242(): pass

    label("Function_24_8242")

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
            "#6P#10103FTwo urgent cases and two\x01",
            "wanted monsters...\x02\x03",
            "#10101FSetting aside the ENIGMA\x01",
            "Ⅱ one, the other seems\x01",
            "pretty unique.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PYes, to think Lechter's\x01",
            "come to Crossbell\x01",
            "again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FHe was that guy playing\x01",
            "dumb during the Schwarz\x01",
            "Auction.\x02\x03",
            "#10300FHe's clearly no ordinary\x01",
            "man.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(800)

    AnonymousTalk(
        0x101,
        (
            "#00003F...When I trained at Section\x01",
            "One, I read a file on him.\x02\x03",
            "#00001FCaptain Lechter Arundel,\x01",
            "Imperial Intelligence\x01",
            "Division.\x02\x03",
            "It seems he has the title of\x01",
            "Second Secretary of the\x01",
            "Imperial government as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10108FAn intelligence officer,\x01",
            "huh...\x02",
        )
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
            "#00103F#11PHe seems to be skilled\x01",
            "in political\x01",
            "maneuverings as well.\x02\x03",
            "#00101FSomeone elusive, and\x01",
            "perhaps possessing\x01",
            "advanced hidden skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHe seems more like an\x01",
            "ordinary person than not,\x01",
            "though.\x02\x03",
            "#10302FBut, being an Imperial\x01",
            "secretary and in army\x01",
            "intelligence...\x02\x03",
            "Could it mean that he's a\x01",
            "confidant of that famous\x01",
            "Blood and Iron Chancellor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006F(How does he know something like that...?)\x02\x03",
            "#00001F...Yeah, according to Section One intel,\x01",
            "he's Chancellor Osborne's right-hand man.\x02\x03",
            "It's confirmed that he came to Crossbell\x01",
            "with the chancellor last year and they had\x01",
            "informal talks with Chairman Hartmann.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PHe himself said so.\x02\x03",
            "#00106FIt seemed like he was joking\x01",
            "at the time. Who would have\x01",
            "thought it was true...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FHe's clearly someone who\x01",
            "can't be dealt with via\x01",
            "normal means...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FHehe, well isn't this\x01",
            "interesting?\x02\x03",
            "#10300FThat said, our first priority\x01",
            "seems to be support activities\x01",
            "inside the city, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00000FYeah. For the wanted monster we'll\x01",
            "have to search on the highway, but\x01",
            "let's leave that one for later.\x02\x03",
            "#00003F...It's been several months since\x01",
            "Revache's annihilation.\x02\x03",
            "#00001FIt seems certain that new\x01",
            "movements are taking place in the\x01",
            "underworld.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PHeiyue's actions... And those of the\x01",
            "Imperial government as well.\x02\x03",
            "#00101FIt seems they will have a considerable\x01",
            "influence on the "trade conference" that\x01",
            "will be held at the end of this month, too.\x02",
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
        (
            "#6P#10105FThe "trade\x01",
            "conference"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FIt's an international conference\x01",
            "called by the new mayor where\x01",
            "heads of state will gather.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00102F#11PYes...\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)

    AnonymousTalk(
        0x102,
        (
            "#00104FThe new mayor, Dieter Crois.\x02\x03",
            "He's the sponsor. It's an economics-related\x01",
            "conference where the leaders of the Empire,\x01",
            "Republic, Liberl and Remiferia will meet.\x02\x03",
            "#00100FOfficially, it's called the "West Zemuria\x01",
            "Trade Conference".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00004FTo think he'd call such a big\x01",
            "conference immediately\x01",
            "following his inauguration...\x02\x03",
            "#00000FMaybe it's something you can\x01",
            "only do if you're both mayor\x01",
            "and the President of IBC.\x02",
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
            "#6P#10109FI've never met him in\x01",
            "person, but I've heard\x01",
            "he's amazingly capable.\x02\x03",
            "#10102FBy the way, I think\x01",
            "you've met him already,\x01",
            "right, Wazy?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#6P#10304FYeah, when I got the letter of\x01",
            "recommendation.\x02\x03",
            "#10302FI can't believe I got a recommendation\x01",
            "for a police post, even though I'm the\x01",
            "leader of a delinquent group.\x02\x03",
            "#10309FHehe. He's too generous a man, if I do\x01",
            "say so myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FIt's no laughing matter,\x01",
            "you know.\x02",
        )
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
        "Oh, you already started.\x02",
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

    def lambda_918E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_918E)

    def lambda_919F():
        OP_95(0xFE, 17000, 850, 4000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_919F)
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

    def lambda_9227():
        OP_95(0xFE, 14900, 850, 8400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9227)
    WaitChrThread(0x8, 1)

    def lambda_9245():
        OP_95(0xFE, 12700, 850, 8400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9245)
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
        "#6P#10101FGood morning, sir!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x109, 500)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#01003F#5PAt ease, soldier.\x02\x03",
            "#01000FWe're fundamentally hands\x01",
            "off here.\x02\x03",
            "You can do things how ya\x01",
            "want. I won't interfere\x01",
            "unless it's really serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FR-Right...\x02",
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
            "#6P#10309FAhaha. What an\x01",
            "understanding boss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00012F...Uhhmm... I'm not so\x01",
            "sure about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00111FIn Chief's case, half\x01",
            "the motive is that it's\x01",
            "a bother, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#01004F#5PHeh heh, you know me\x01",
            "well.\x02\x03",
            "#01002FBut today is different.\x01",
            "I have an order for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#11PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#11PF-From you, Chief...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003F#5PYeah, though it's something\x01",
            "that can wait 'til after you're\x01",
            "through with support requests.\x02\x03",
            "#01000FGo to the police academy.\x02",
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
        "#00005F#11PThe police academy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FIt's that place along West\x01",
            "Crossbell Highway with the\x01",
            "training grounds, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#5PIt should be familiar to\x01",
            "you and Lloyd.\x02\x03",
            "#01000FI'll contact you via ENIGMA\x01",
            "when I'm ready for you.\x02\x03",
            "Until then, keep patrolling\x01",
            "the city and take care of\x01",
            "your support requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PUhm... Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#11PStill, what is this all\x01",
            "about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01002F#5PHeh heh, that'll give y'all\x01",
            "something to look forward\x01",
            "to when you get there.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x8, 0x2328, 0x2648, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#01006F#11PSee you, then. I'll be\x01",
            "in touch.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(10600, 1850, 6600, 3000)

    def lambda_9858():
        OP_95(0xFE, 9000, 850, 9800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9858)
    WaitChrThread(0x8, 1)

    def lambda_9876():
        OP_95(0xFE, 2000, 850, 9800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9876)
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
        "#6P#10105FUhhhm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PSorry, Noｱl, but this is\x01",
            "how the Special Support\x01",
            "Section is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FOn the bright side, it fosters\x01",
            "our senses of independence and\x01",
            "judgment, but...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10109FI-I see! I expected\x01",
            "nothing less from Chief\x01",
            "Sergei!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHehe. It's not what you\x01",
            "say, but how you say it.\x02\x03",
            "#10302FSo? Should we head out\x01",
            "right away?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00004FYeah, let's.\x02\x03",
            "#00005F...Oh yeah, KeA said she\x01",
            "was leaving for Sunday\x01",
            "School.\x02\x03",
            "#00000FChief is out, so maybe\x01",
            "we should leave\x01",
            "together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#11PRight. Let's head to the\x01",
            "3rd floor and speak with\x01",
            "KeA.\x02",
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

    # Function_24_8242 end

    def Function_25_9BC0(): pass

    label("Function_25_9BC0")

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

    # Function_25_9BC0 end

    def Function_26_9BE4(): pass

    label("Function_26_9BE4")

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
            "#01006F#5PLooks like it's going to\x01",
            "be light rain all day.\x02\x03",
            "#01000FAnd there'll be a storm\x01",
            "tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see...\x02\x03",
            "#00000FSince we were issued the orbal\x01",
            "car, I wanted to patrol to\x01",
            "Crossbell's outskirts, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWell this sure doesn't\x01",
            "feel like driving\x01",
            "weather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FAww... Too bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PBy the way... Is there a follow-\x01",
            "up report regarding the man we\x01",
            "met on the highway yesterday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01003F#5PYeah, it looks like Section\x01",
            "One hasn't checked up on him\x01",
            "yet.\x02\x03",
            "#01001FThere's Cao and that Lechter\x01",
            "guy too─ All folks who\x01",
            "aren't so easy to deal with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FRight...\x02\x03",
            "#00006FAnd the guy we met yesterday\x01",
            "seemed even more dangerous\x01",
            "than either of them.\x02\x03",
            "#00001FHe was calm, but I'd say he\x01",
            "had a strange ferocity to\x01",
            "him...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10103FYeah, he did really seem\x01",
            "like a tiger.\x02\x03",
            "#10101FLike, if he felt like it,\x01",
            "he could've attacked and\x01",
            "eaten us in an instant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12PIt's not a pleasant\x01",
            "metaphor, but the atmosphere\x01",
            "really was just like that.\x02\x03",
            "#00108FA terrorist, or a jaeger...\x01",
            "Both are possibilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10308FHmm...\x02\x03",
            "#10304FIn that case, how about\x01",
            "we gather information\x01",
            "around Downtown.\x02\x03",
            "#10300FI feel like the owner of\x01",
            "Neinvalli knows some\x01",
            "things.\x02",
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
            "#00005F#11PAshley from the exchange\x01",
            "shop, right?\x02\x03",
            "#00001FBeing a weapons dealer,\x01",
            "she would know about the\x01",
            "underworld, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#11PThen, I think we should\x01",
            "pay her a visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#5PWell, do your best, guys.\x02\x03",
            "#01000FBut don't forget that you're the\x01",
            "Support Section.\x02\x03",
            "If you over-focus on\x01",
            "counterintelligence, you'll lose\x01",
            "sight of your usual duties.\x02",
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

    def lambda_A3BE():
        OP_95(0xFE, 14900, 850, 8400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A3BE)
    WaitChrThread(0x8, 1)

    def lambda_A3DC():
        OP_95(0xFE, 18000, 850, 4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A3DC)
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

    def lambda_A435():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A435)

    def lambda_A446():
        OP_95(0xFE, 19500, 850, 4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A446)
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
            "#5P#00006F...For now, let's check\x01",
            "the support requests\x01",
            "using the terminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FAlright, understood.\x02",
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

    # Function_26_9BE4 end

    def Function_27_A5C5(): pass

    label("Function_27_A5C5")

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
            "all inside Crossbell\x01",
            "City, huh.\x02\x03",
            "#00004FIf it's just this many,\x01",
            "I think we can handle\x01",
            "all of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12PThe foundation request\x01",
            "might be connected to\x01",
            "Tio...\x02\x03",
            "#00102FIf possible, I also want\x01",
            "to hear Momo's request.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#6P#10100FThen, we'll visit the exchange\x01",
            "shop in Downtown while taking\x01",
            "care of the urgent requests?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A7D7():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A7D7)
    Sleep(100)

    def lambda_A7E7():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A7E7)
    Sleep(50)

    def lambda_A7F7():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A7F7)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00002F#5PYeah, let's.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell it's raining, so\x01",
            "let's make steady\x01",
            "progress.\x02",
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

    # Function_27_A5C5 end

    def Function_28_A8BC(): pass

    label("Function_28_A8BC")

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
            "#00003F#5PSo the urgent requests\x01",
            "are from the CGF and St.\x01",
            "Ursula Hospital, huh...\x02\x03",
            "#00002FBut, I can't believe\x01",
            "Instructor Douglas is\x01",
            "asking for our help.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#00105F#11PInstructor Douglas? He's\x01",
            "the new CGF Vice\x01",
            "Commander, right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AB6C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AB6C)
    Sleep(100)

    def lambda_AB7C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AB7C)
    Sleep(50)

    def lambda_AB8C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AB8C)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x101,
        (
            "#00004F#5PYeah, before becoming Vice Commander he\x01",
            "was an instructor at the police academy.\x02\x03",
            "#00000FHe drilled everything into me, from basic\x01",
            "strength training to close combat training\x01",
            "and the tonfa disabling techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FOriginally, the CGF had placed\x01",
            "their hopes in him.\x02\x03",
            "#10106FHowever, the former CGF\x01",
            "commander ostracised him and he\x01",
            "was given a do-nothing job...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FHe handled my training\x01",
            "too. He's incredibly\x01",
            "tough.\x02\x03",
            "#00302FHe might be No. 1 in the\x01",
            "CGF in terms of combat\x01",
            "strength.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ADA2():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_ADA2)
    Sleep(50)

    def lambda_ADB2():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_ADB2)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x102,
        (
            "#00104F#11PI see... That's very\x01",
            "impressive.\x02\x03",
            "#00100FBut, thinking about our\x01",
            "relationship with the CGF, I'd\x01",
            "like to at least meet him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PYeah, let's go see him.\x02\x03",
            "#00003FAnd there's one from a newly\x01",
            "appointed professor at St.\x01",
            "Ursula Hospital, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FThey're taking over the\x01",
            "pharmacology and neurology\x01",
            "departments from Joachim...\x02\x03",
            "#00301FWell, we need to stay\x01",
            "vigilant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FStill, I feel like I've\x01",
            "heard this Dr. Seiland\x01",
            "name somewhere.\x02\x03",
            "#10300FIsn't it a famous name\x01",
            "in Remiferia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#11PThe Seiland Company, a\x01",
            "pharmaceutical manufacturer\x01",
            "based in Remiferia.\x02\x03",
            "They're a distinguished family\x01",
            "with ties to the Archduke.\x01",
            "It's possible she's related.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PHmm. In that case, she doesn't seem\x01",
            "all that suspicious a character,\x01",
            "but...\x02\x03",
            "#00001F...Well anyway, Dr. Seiland wants to\x01",
            "speak with us about that drug too,\x01",
            "so we have to go to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10309FHehe, well that sister of\x01",
            "yours that you so admire is\x01",
            "there too.\x02\x03",
            "#10302FThey say a nurse uniform looks\x01",
            "so good on her that she looks\x01",
            "like a holy saint, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_B216():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B216)
    Sleep(250)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00005F#5PWha!?\x02\x03",
            "#00012FT-That's not it. It's\x01",
            "just... Cecil's been looking\x01",
            "after me all this time.\x02\x03",
            "#00011FBut Wazy! You never met her,\x01",
            "how do you know that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00309FMy bad, I told 'im.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00013F#5PKh, Randy... You!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00111F#11P(Lloyd's a little too\x01",
            "worked up.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112F(Looks like Wazy was\x01",
            "right on the money.)\x02\x03",
            "#10102F(But she really is\x01",
            "beautiful, so I get\x01",
            "where he's coming from.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P...Ahem. Well anyway...\x02\x03",
            "#00000FBefore meeting the\x01",
            "professor, I'd like hear\x01",
            "what Cecil has to say.\x02\x03",
            "#00008FI'd like to make sure the\x01",
            "hospital's recovered from\x01",
            "the damage Joachim caused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PYou have a point...\x02\x03",
            "#00100FAh, but isn't Shizuku\x01",
            "coming to the city\x01",
            "today?\x02\x03",
            "KeA went to visit her at\x01",
            "the guild a little while\x01",
            "ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PYeah, she said she'd play\x01",
            "with Shizuku all day and left\x01",
            "with a huge grin on her face.\x02\x03",
            "#00002FThey should be at the guild,\x01",
            "so let's go there too if we\x01",
            "have extra time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#11PYes, let's.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10305FShizuku is the Divine\x01",
            "Blade of Wind's daughter\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FYeah, she's almost the same\x01",
            "age as KeA.\x02\x03",
            "#00302FShe's such a good girl,\x01",
            "you'd never guess she's that\x01",
            "stuffy old man's daughter.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_B752")

    ChrTalk(
        0x109,
        (
            "#6P#10109FHaha... Shizuku is\x01",
            "pretty cute, isn't she.\x02\x03",
            "#10102FFran thought so too when\x01",
            "she met her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B7B9")

    label("loc_B752")


    ChrTalk(
        0x109,
        (
            "#6P#10109FAll the rumors say she's\x01",
            "super cute, too.\x02\x03",
            "#10102FFran thought so too when\x01",
            "she met her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7B9")


    ChrTalk(
        0x105,
        (
            "#12P#10300FHehe, I see.\x02\x03",
            "#10304FSo we'll be introducing\x01",
            "ourselves to various people\x01",
            "as we patrol Crossbell today.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#11P#10302F─While looking for any info\x01",
            "on the actions of those Red\x01",
            "Constellation guys, too.\x02",
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

    def lambda_B8F2():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B8F2)
    Sleep(50)

    def lambda_B902():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B902)
    Sleep(50)

    def lambda_B912():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B912)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00013F#5PWazy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10101FY-You!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306F...It's fine. He likes\x01",
            "to joke around.\x02\x03",
            "#00303FThough they're my\x01",
            "relatives, those guys\x01",
            "are seriously no joke.\x02\x03",
            "#00301FThey're probably the\x01",
            "ones who rigged the Old\x01",
            "Mine with explosives.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BA24():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BA24)
    Sleep(50)

    def lambda_BA34():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BA34)
    Sleep(50)

    def lambda_BA44():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BA44)
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
            "#00108F#11PUmm, you don't have to\x01",
            "take them to task so\x01",
            "much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FUncle and Shirley... I\x01",
            "know those two very well.\x02\x03",
            "#00308FI can't say for sure,\x01",
            "but... They were probably\x01",
            "testing our abilities.\x02\x03",
            "#00301FAnd the abilities of the\x01",
            "place I drifted to after\x01",
            "abandoning my former home.\x02",
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
        "#5P#10108FJ-Just for that, they...\x02",
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
            "#11P#10303FThen they're not\x01",
            "necessarily malicious\x01",
            "toward us.\x02\x03",
            "#10300FAre they really folks who\x01",
            "would do something like\x01",
            "that out of mere curiosity?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FYeah, traps of that\x01",
            "level are just their way\x01",
            "of saying hello.\x02\x03",
            "#00301FSince I've returned,\x01",
            "maybe I should look into\x01",
            "their actions al─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P─All the more reason, then.\x02\x03",
            "#00008FRed Constellation is a group we\x01",
            "definitely can't ignore.\x02\x03",
            "Eventually, we'll need to ascertain their\x01",
            "motive for visiting Crossbell and their\x01",
            "connection with the Imperial government.\x02\x03",
            "#00001FHowever... Only as the Special Support\x01",
            "Section.\x02",
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
            "#00003F#5PWe need you Randy, and\x01",
            "we've no intention of\x01",
            "leaving you alone.\x02\x03",
            "#00001FEven if it's you, acting\x01",
            "alone, you have no chance\x01",
            "of succeeding, right?\x02\x03",
            "So... Don't say things\x01",
            "like "I'll act alone."\x02",
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
            "#11P#10309FHaha, quite the\x01",
            "persuasive lines, as\x01",
            "always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10101FB-But he's right!\x02\x03",
            "Combining our strength in times\x01",
            "like these is what the Special\x01",
            "Support Section does, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#11PYes, exactly.\x02\x03",
            "#00100FEven in that cult\x01",
            "incident... We joined forces\x01",
            "and faced it together.\x02\x03",
            "Randy, isn't this the same?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304F...Haha.\x02\x03",
            "#00302FSorry, looks like I said\x01",
            "something stupid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah, totally.\x02\x03",
            "#00000FAnyway, we have a car now, too, so let's\x01",
            "patrol Crossbell's outskirts today while\x01",
            "taking care of support requests.\x02\x03",
            "Stretching our legs at Tangram Gate or\x01",
            "Armorica Village might be good as well.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C1C6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C1C6)
    Sleep(50)

    def lambda_C1D6():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C1D6)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#00104F#11PYeah, it has been a\x01",
            "while...\x02\x03",
            "#00105FBy the way, Commander\x01",
            "Sonya is at Bellguard\x01",
            "Gate, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FYes, she should be.\x02\x03",
            "Though I think she's\x01",
            "busy dealing with trade\x01",
            "conference preparations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FMireille should be\x01",
            "there. Maybe we should\x01",
            "say hi to her, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHaha... Then, shall we\x01",
            "head out?\x02",
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
            "When the party has more\x01",
            "than 4 people, the extras\x01",
            "are [Support Members].\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "[Support Members] standby outside the battlefield\x01",
            "and appear in the AT turns. When their turn\x01",
            "comes, they perform various support actions.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When attacked from behind, the\x01",
            "formation, inclusive of [Support\x01",
            "Members], is disrupted.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Because of this, it's important\x01",
            "to keep [Support Members]\x01",
            "prepared for battle as well.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can change party\x01",
            "members from [TACTICS]\x01",
            "in the camp menu.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Also, you can decide which\x01",
            "support crafts to use under\x01",
            "[STATUS] in the camp menu.\x07\x00\x02",
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

    # Function_28_A8BC end

    def Function_29_C5CE(): pass

    label("Function_29_C5CE")

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

    def lambda_C6B1():
        OP_97(0x109, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C6B1)
    Sleep(200)

    def lambda_C6CE():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C6CE)
    Sleep(200)

    def lambda_C6EB():
        OP_97(0x105, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C6EB)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    VolumeBGM(0x50, 0x3E8)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_C726():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C726)
    Sleep(400)

    def lambda_C73A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C73A)

    def lambda_C74B():
        OP_96(0xFE, 0x3E8, 0xA, 0x1F4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C74B)
    Sleep(400)

    def lambda_C768():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C768)

    def lambda_C779():
        OP_96(0xFE, 0x3E8, 0xA, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C779)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#00003F#5P...Say, Randy.\x02",
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
        "Huh? What's up Lloyd.\x02",
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
            "#00008F#5PYou know... About your\x01",
            "father...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#12P#00306FOh, that...\x02\x03",
            "#00300FI don't particularly mind,\x01",
            "you know? It's not a rare\x01",
            "story in that world.\x02\x03",
            "And when I left the group,\x01",
            "I cut ties with my old\x01",
            "man.\x02\x03",
            "#00304FIt's not like I didn't\x01",
            "feel anything, but...\x01",
            "Well, I felt relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P...I see.\x02\x03",
            "#00001FBut if you do ever feel\x01",
            "like it, you can always\x01",
            "talk to me about it.\x02\x03",
            "As leader, I might be\x01",
            "able to advise you.\x02",
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
            "#00011F#5PAh, sorry. Was that too\x01",
            "pushy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00304FHaha, no, no.\x02\x03",
            "#00302FI was just thinking that\x01",
            "you've grown up too, all\x01",
            "things considered.\x02\x03",
            "#00309FHmm, your big bro here\x01",
            "is deeply moved.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_CD27")

    ChrTalk(
        0x101,
        "#00006F#5PNow look here...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00008F#5P...It's just, I want to\x01",
            "help you in times like\x01",
            "these.\x02\x03",
            "#00000FMaybe I'm not so reliable,\x01",
            "but that's what means to\x01",
            "be "buddies", right?\x02",
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

    def lambda_CC2C():
        OP_96(0xFE, 0x3E8, 0x0, 0x4E2, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CC2C)
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
            "#12P#00302F...Alright, got it.\x01",
            "Maybe one day I'll tell\x01",
            "you everything.\x02\x03",
            "#00309FI'll count on you when\x01",
            "that time comes─ buddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PYeah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CDC9")

    label("loc_CD27")


    ChrTalk(
        0x101,
        "#00006F#5PNow look here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00304F...Well, if I do feel\x01",
            "like it, I might ask for\x01",
            "advice.\x02\x03",
            "#00300FI'll be counting on you\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PYeah!\x02",
    )

    CloseMessageWindow()

    label("loc_CDC9")

    SetChrPos(0x102, 1500, -1000, -4000, 180)
    SetChrPos(0x105, 500, -1000, -4000, 180)

    NpcTalk(
        0x105,
        "Wazy's Voice",
        (
            "#1P#2SHuh, what are you guys\x01",
            "doing?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x102,
        "Elie's Voice",
        (
            "#1P#2SDid you forget\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_CED8")
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

    def lambda_CEBF():
        OP_96(0xFE, 0x3E8, 0x0, 0x2EE, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CEBF)
    WaitChrThread(0x104, 1)

    label("loc_CED8")


    def lambda_CEDD():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CEDD)

    ChrTalk(
        0x101,
        "#00011F#5PSorry, coming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00304FAlright then, let's make\x01",
            "steady progress.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x3E8)

    def lambda_CF47():
        OP_97(0x104, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CF47)
    Sleep(100)

    def lambda_CF64():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CF64)
    FadeToDark(1000, 0, -1)
    Sleep(400)

    def lambda_CF8B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CF8B)
    Sleep(400)

    def lambda_CF9F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CF9F)
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
            "You can now go anywhere in Crossbell\x01",
            "State via orbal car.\x02\x03",
            "It is parked at the Support Section's\x01",
            "rear entrance on West Street, so\x01",
            "please make good use of it.\x07\x00\x02",
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

    # Function_29_C5CE end

    def Function_30_D0C8(): pass

    label("Function_30_D0C8")

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

    def lambda_D1AB():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D1AB)
    Sleep(200)

    def lambda_D1C8():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D1C8)
    Sleep(200)

    def lambda_D1E5():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_D1E5)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    VolumeBGM(0x50, 0x3E8)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_D220():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D220)
    Sleep(400)

    def lambda_D234():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D234)
    Sleep(400)

    def lambda_D248():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_D248)

    def lambda_D259():
        OP_96(0xFE, 0xFFFFF448, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D259)
    Sleep(300)

    def lambda_D276():
        OP_96(0xFE, 0xFFFFFA24, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D276)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00003F#11P...Say, Randy.\x02",
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
        "Huh? What's up Lloyd.\x02",
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
            "#00008F#11PYou know... About your\x01",
            "father...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00306FOh, that...\x02\x03",
            "#00300FI don't particularly mind,\x01",
            "you know? It's not a rare\x01",
            "story in that world.\x02\x03",
            "And when I left the group,\x01",
            "I cut ties with my old\x01",
            "man.\x02\x03",
            "#00304FIt's not like I didn't\x01",
            "feel anything, but...\x01",
            "Well, I felt relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P...I see.\x02\x03",
            "#00001FBut if you do ever feel\x01",
            "like it, you can always\x01",
            "talk to me about it.\x02\x03",
            "As leader, I might be\x01",
            "able to advise you.\x02",
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
            "#00011F#11PAh, sorry. Was that too\x01",
            "pushy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FHaha, no, no.\x02\x03",
            "#00302FI was just thinking that\x01",
            "you've grown up too, all\x01",
            "things considered.\x02\x03",
            "#00309FHmm, your big bro here\x01",
            "is deeply moved.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_D82A")

    ChrTalk(
        0x101,
        "#00006F#11PNow look here...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00008F#11P...It's just, I want to\x01",
            "help you in times like\x01",
            "these.\x02\x03",
            "#00000FMaybe I'm not so reliable,\x01",
            "but that's what means to\x01",
            "be "buddies", right?\x02",
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

    def lambda_D72F():
        OP_96(0xFE, 0xFFFFF736, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D72F)
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
            "#6P#00302F...Alright, got it.\x01",
            "Maybe one day I'll tell\x01",
            "you everything.\x02\x03",
            "#00309FI'll count on you when\x01",
            "that time comes─ buddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11PYeah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_D8CD")

    label("loc_D82A")


    ChrTalk(
        0x101,
        "#00006F#11PNow look here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304F...Well, if I do feel\x01",
            "like it, I might ask for\x01",
            "advice.\x02\x03",
            "#00300FI'll be counting on you\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PYeah!\x02",
    )

    CloseMessageWindow()

    label("loc_D8CD")

    SetChrPos(0x102, -7000, -2000, 68300, 270)
    SetChrPos(0x105, -7000, -2000, 67300, 270)

    NpcTalk(
        0x105,
        "Wazy's Voice",
        (
            "#2P#2SHuh, what are you guys\x01",
            "doing?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x102,
        "Elie's Voice",
        (
            "#2P#2SDid you forget\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_D9DC")
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

    def lambda_D9C3():
        OP_96(0xFE, 0xFFFFF542, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D9C3)
    WaitChrThread(0x104, 1)

    label("loc_D9DC")


    def lambda_D9E1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D9E1)

    ChrTalk(
        0x101,
        "#00011F#11PSorry, coming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00304FAlright then, let's make\x01",
            "steady progress.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x3E8)

    def lambda_DA4D():
        OP_97(0x104, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_DA4D)
    Sleep(100)

    def lambda_DA6A():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DA6A)
    FadeToDark(1000, 0, -1)
    Sleep(400)

    def lambda_DA91():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_DA91)
    Sleep(400)

    def lambda_DAA5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DAA5)
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
            "You can now go anywhere in Crossbell\x01",
            "State via orbal car.\x02\x03",
            "It is parked at the Support Section's\x01",
            "rear entrance on West Street, so\x01",
            "please make good use of it.\x07\x00\x02",
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

    # Function_30_D0C8 end

    def Function_31_DBCE(): pass

    label("Function_31_DBCE")

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
            "#00003F─I see. So the trade\x01",
            "conference's main event\x01",
            "is tomorrow.\x02",
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
            "#5P#01003FYeah. They're just discussing\x01",
            "things informally at today's\x01",
            "luncheon.\x02\x03",
            "#01002FThey'll attend a dinner party\x01",
            "at the Arc-en-Ciel theater\x01",
            "tonight as well.\x02\x03",
            "Incidentally, the plan is for\x01",
            "the heads of state to stay at\x01",
            "the Michelam State Guest House.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThe state guest house is\x01",
            "former chairman Hartmann's\x01",
            "mansion, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305FWow, that stupidly huge\x01",
            "mansion is being used\x01",
            "for that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01006FWell, it's because Hartmann's fine\x01",
            "for corruption and illegal dealings\x01",
            "was an astonishing amount.\x02\x03",
            "#01000FTo pay it, he forfeited the\x01",
            "mansion, and it's now used as the\x01",
            "state guest house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FHmm... Well, you reap\x01",
            "what you sow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FSo the Michelam area is\x01",
            "sealed off, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01003FYeah. The hotel and theme park\x01",
            "are temporarily closed for the\x01",
            "duration of the conference.\x02\x03",
            "#01002FCGF are stationed there too,\x01",
            "so there's no need to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PUnderstood.\x02\x03",
            "#00000FAs for us, we'll continue\x01",
            "support activities like\x01",
            "we did yesterday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01004FWell I don't care.\x02\x03",
            "#01000FSome of the attendees will\x01",
            "take a tour of Crossbell\x01",
            "after the luncheon.\x02\x03",
            "There might be trouble, so\x01",
            "I'll need you to provide\x01",
            "backup in that case.\x02",
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
            "#6P#00306FBut, those invitees didn't have\x01",
            "a normal aura at all.\x02\x03",
            "#00301FEspecially that Blood and Iron\x01",
            "Chancellor... He's no one\x01",
            "ordinary. That's for damn sure.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah. The unassuming nature\x01",
            "of that Captain Lechter\x01",
            "interests me as well, but...\x02\x03",
            "#00008FThe Chancellor had an even\x01",
            "more overwhelming air about\x01",
            "him.\x02\x03",
            "#00001FPresident Rocksmith of the\x01",
            "Republic had a friendly air,\x01",
            "though...\x02\x03",
            "#00005F...However, that of Kilika\x01",
            "next to him was unassuming.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)

    ChrTalk(
        0x102,
        (
            "#00103FShe belongs to the Rocksmith\x01",
            "Agency, Calvard's intelligence\x01",
            "agency.\x02\x03",
            "#00108FEven though the President is known\x01",
            "as a populist, it seems dealing\x01",
            "with him won't be straightforward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10102FHowever, Princess\x01",
            "Klaudia of Liberl was\x01",
            "dignified.\x02\x03",
            "#10109FAnd Captain Julia with\x01",
            "her... She was super\x01",
            "cool!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#6P#10305FShe's the captain of the\x01",
            "Liberl Royal Guard,\x01",
            "right?\x02\x03",
            "#10302FI heard she has some\x01",
            "crazy fans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10112FW-Well, yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FAhaha... I'm a bit of a\x01",
            "fan myself.\x02",
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
        "#5P#00005FWow, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FWhat's this now? You're\x01",
            "into that sort of thing,\x01",
            "milady?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#00102FI wouldn't say "into",\x01",
            "but...\x02\x03",
            "#00104FBefore, when I was staying\x01",
            "in Liberl, I saw a parade\x01",
            "of the Royal Guard...\x02\x03",
            "#00100FWhen they put out a photo\x01",
            "album of it, I bought it\x01",
            "unconsciously.\x02",
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
        (
            "#5P#10101FPlease, show it to me\x01",
            "later!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(150)

    ChrTalk(
        0x102,
        "#00109FAhaha... Alright.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FMan, what a pity.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHaha. A beautiful woman\x01",
            "disguised as a man is a\x01",
            "kind of romance, you see.\x02\x03",
            "#10302FAs for me, I'm interested\x01",
            "in Imperial prince.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F#11PPrince Olivert, huh...\x01",
            "It's a name I've been\x01",
            "hearing more often lately.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)

    ChrTalk(
        0x102,
        (
            "#00104FHe's famous for having a role\x01",
            "in the resolution of that\x01",
            "phenomenon in Liberl.\x02\x03",
            "#00100FAfter that, it seems he\x01",
            "attended many social functions\x01",
            "and made a name for himself.\x02\x03",
            "If I remember correctly, he\x01",
            "has no right of succession to\x01",
            "the Imperial throne.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5P#00001FReally...?\x02\x03",
            "#00005FA role in resolving that\x01",
            "phenomenon in Liberl...\x01",
            "Then that means...\x02\x03",
            "#00000FHe's an acquaintance of\x01",
            "Estelle and Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FYes, now that you\x01",
            "mention it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FIt seems like those two\x01",
            "have a lot of friends,\x01",
            "so it's possible.\x02",
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

    def lambda_EFD9():
        OP_96(0xFE, 0x3E8, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_EFD9)

    def lambda_EFF3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_EFF3)
    Sleep(1000)

    def lambda_F007():
        OP_96(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F007)

    def lambda_F021():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F021)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)

    def lambda_F03A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_F03A)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x5A, 0x1F4)
    SetChrSubChip(0xA, 0x5)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00002FKeA, Zeit, welcome home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#6P#01200FWoof.\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)

    def lambda_F099():
        OP_96(0xFE, 0x3E8, 0x352, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F099)
    Sleep(1000)
    Fade(1000)
    OP_68(10600, 1850, 6600, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    OP_68(12600, 1850, 6600, 3000)
    EndChrThread(0x9, 0x1)
    SetChrPos(0x9, 5000, 850, 8900, 90)

    def lambda_F10F():
        OP_96(0xFE, 0x2AF8, 0x352, 0x22C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F10F)
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
            "#00105FOh, Shizuku's not with\x01",
            "you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01106F#5POh yeah, she went back\x01",
            "to the hospital with her\x01",
            "dad.\x02\x03",
            "#01110FBut, we saw the\x01",
            "unveiling of that\x01",
            "building together!\x02\x03",
            "#01109FThat was amaaazing! Did\x01",
            "you guys see it from up\x01",
            "close?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FYeah. Honestly, it's so\x01",
            "big that I'm actually\x01",
            "not too sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300F#NYeah, it really is an\x01",
            "unbelievable building.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#6P#10109FHaha. You might have\x01",
            "gotten a better view\x01",
            "than we did, KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01109F#5PYeah! It was super cool!\x02\x03",
            "#01110FThey're called...\x01",
            "fireworks? They were\x01",
            "super pretty too.\x02\x03",
            "#01102FBut...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)

    ChrTalk(
        0x101,
        "#00005FHm? What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01104F#5PAh, no, nevermind.\x02\x03",
            "#01100FAre you guys leaving for\x01",
            "work agaaain?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah. I think we'll be\x01",
            "back by evening.\x02\x03",
            "What about you, Chief?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5P#01003FI'll be here on standby\x01",
            "today.\x02\x03",
            "#01002FI'll contact you if\x01",
            "anything happens, so no\x01",
            "need to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FAlright, we'll take you\x01",
            "up on that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FLet's check the terminal\x01",
            "before we go.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F6AA")
    Jump("loc_F6AF")

    label("loc_F6AA")

    OP_29(0x73, 0x4, 0x40)

    label("loc_F6AF")

    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_31_DBCE end

    def Function_32_F6B5(): pass

    label("Function_32_F6B5")

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
            "#00001F#5PWe got several\x01",
            "requests... And all of\x01",
            "them worry me.\x02\x03",
            "#00006FI don't get this "search\x01",
            "for musician" one,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FMaaan, who'd've ever thunk\x01",
            "we'd get a request from\x01",
            "those bracer ladies, eh?\x02\x03",
            "#00302FThere's nothin' sexy about\x01",
            "trainin', but I'd like to\x01",
            "drop by if there's time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10104FHaha. It might be a good\x01",
            "opportunity.\x02\x03",
            "#10100FAnd it looks like this\x01",
            ""lost cat" one is from\x01",
            "that same family.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F919():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F919)

    def lambda_F926():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_F926)
    Sleep(50)

    def lambda_F936():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F936)

    def lambda_F943():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F943)
    WaitChrThread(0x101, 2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FA04")

    ChrTalk(
        0x101,
        (
            "#00002F#5PYeah, it's Mr. Bond's\x01",
            "place. He moved to East\x01",
            "Street recently.\x02\x03",
            "#00004FWe have a connection with\x01",
            "that cat too, so I'd like\x01",
            "to help them if possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FAA8")

    label("loc_FA04")


    ChrTalk(
        0x101,
        (
            "#00002F#5PYeah, it's Mr. Bond's\x01",
            "place. He moved to East\x01",
            "Street recently.\x02\x03",
            "#00003FIt looks like things are\x01",
            "tough for them... I'd like\x01",
            "to help them if possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FAA8")


    ChrTalk(
        0x102,
        (
            "#00104F#11PI agree.\x02\x03",
            "#00100FIt seems they're\x01",
            "counting on us, so let's\x01",
            "not forget to stop by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWith the unveiling of the tower\x01",
            "and the visiting VIPs, the\x01",
            "city's more lively than usual.\x02\x03",
            "#10302FVisiting various places might\x01",
            "be fun.\x02",
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

    # Function_32_F6B5 end

    def Function_33_FBEB(): pass

    label("Function_33_FBEB")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD1C")
    OP_68(1300, 1850, 11800, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    OP_90(0x101, 1700, 4850, 14100, 180)
    OP_90(0x102, 600, 4850, 14400, 180)
    OP_90(0x104, 1700, 4850, 15400, 180)
    OP_90(0x109, 600, 4850, 15700, 180)
    OP_90(0x105, 1700, 4850, 16700, 180)
    Jump("loc_FD9F")

    label("loc_FD1C")

    OP_68(1000, 1000, 700, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x101, 300, 0, -1600, 0)
    SetChrPos(0x102, 1400, 0, -1900, 0)
    SetChrPos(0x104, 300, 0, -2900, 0)
    SetChrPos(0x109, 1400, 0, -3200, 0)
    SetChrPos(0x105, 300, 0, -4200, 0)

    label("loc_FD9F")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE3C")
    OP_68(1300, 1850, 9800, 3500)
    BeginChrThread(0x101, 3, 0, 34)
    Jump("loc_FEDB")

    label("loc_FE3C")

    OP_68(1000, 1000, 2700, 3500)

    def lambda_FE52():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FE52)
    Sleep(200)

    def lambda_FE6F():
        OP_97(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FE6F)
    Sleep(200)

    def lambda_FE8C():
        OP_97(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FE8C)
    Sleep(200)

    def lambda_FEA9():
        OP_97(0x109, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_FEA9)
    Sleep(200)

    def lambda_FEC6():
        OP_97(0x105, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_FEC6)

    label("loc_FEDB")

    FadeToBright(1000, 0)

    def lambda_FEE9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FEE9)
    Sleep(400)

    def lambda_FEFD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FEFD)
    Sleep(600)

    def lambda_FF11():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_FF11)
    Sleep(400)

    def lambda_FF25():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_FF25)
    Sleep(600)

    def lambda_FF39():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_FF39)
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10036")

    ChrTalk(
        0x101,
        "#5P#00002FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00109FMy... What a lovely\x01",
            "smell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10302FHmm, smells like maple\x01",
            "syrup.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_100A5")

    label("loc_10036")


    ChrTalk(
        0x101,
        "#00002F#5PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#11PMy... What a lovely\x01",
            "smell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHmm, smells like maple\x01",
            "syrup.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100A5")

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

    def lambda_100E9():
        OP_95(0xFE, 10810, 850, 11410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_100E9)

    def lambda_10103():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_10103)
    WaitChrThread(0x9, 1)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_101AC")
    SetChrPos(0x101, 1700, -850, 9100, 180)
    SetChrPos(0x102, 600, -850, 9400, 180)
    SetChrPos(0x104, 1700, -850, 10400, 180)
    SetChrPos(0x109, 600, -850, 10700, 180)
    SetChrPos(0x105, 1700, -850, 11700, 180)

    label("loc_101AC")


    def lambda_101B1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_101B1)
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
        "#3606V#30WAh, guys. So you did come back.\x02",
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
            "#00009FYeah, for a little\x01",
            "break.\x02\x03",
            "#00000FBut... Were you baking\x01",
            "muffins?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10330")

    ChrTalk(
        0x9,
        (
            "#01104F#11PEhehe... I thought you\x01",
            "guys might be coming\x01",
            "home.\x02\x03",
            "#01110FThey're maple muffins.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10390")

    label("loc_10330")


    ChrTalk(
        0x9,
        (
            "#01104F#5PEhehe... I thought you\x01",
            "guys might be coming\x01",
            "home.\x02\x03",
            "#01110FThey're maple muffins.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10390")


    ChrTalk(
        0x104,
        (
            "#00305FOh, Keddo... How\x01",
            "thoughtful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FHaha, this is great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FWhy don't I make some\x01",
            "tea for everyone.\x02",
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
            "#5P#01005F─I see. So that's where\x01",
            "they were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PYes, it didn't seem like\x01",
            "they had anything in\x01",
            "mind, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F...How about Red\x01",
            "Constellation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01004FIf something happens, Section\x01",
            "One will contact us.\x02\x03",
            "#01002FIt's not like I don't\x01",
            "understand how you feel, but...\x01",
            "Don't be in such a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00304FHaha... Got it.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#11PWell, it's not just Red\x01",
            "Constellation we're\x01",
            "concerned about.\x02\x03",
            "#00001FAnyway, let's patrol\x01",
            "while looking for signs\x01",
            "of anything unusual.\x02",
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
            "#6P#00108FRight... With the VIPs\x01",
            "visiting, it would be awful\x01",
            "if anything happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FIf there's time, let's\x01",
            "patrol the outskirts too\x01",
            "with our car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01105FYou're leaving again,\x01",
            "guys?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)

    ChrTalk(
        0x101,
        (
            "#00004F#11PYeah. Back to work!\x02\x03",
            "#00002FThanks for those\x01",
            "muffins. They were\x01",
            "super-delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00109FHaha, you've become\x01",
            "better than any of us at\x01",
            "cooking.\x02\x03",
            "#00102FPerhaps Oscar showed you\x01",
            "how to make them?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#6P#01109FEhehe, something like\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)
    Sleep(150)

    ChrTalk(
        0x9,
        (
            "#6P#01110FThere's still some left,\x01",
            "so please have them if\x01",
            "you like.\x02\x03",
            "I think they'll still be\x01",
            "good tomorrow.\x02",
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
        "#10302FWow, how thoughtful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FOooh... Your papa's\x01",
            "gonna cry!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#5P...Wait a second.\x02\x03",
            "#00013FI know how awesome you are, Randy,\x01",
            "but I've no intention of handing\x01",
            "my fatherly duties to you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#00302FHmph, how interesting.\x01",
            "Wanna go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#01105FHuuuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106F*sigh*... What are you\x01",
            "arguing about this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10112FAhaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FIt's quite rare to have\x01",
            "this many doting\x01",
            "parents.\x02",
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

    # Function_33_FBEB end

    def Function_34_11209(): pass

    label("Function_34_11209")


    def lambda_1120E():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1120E)
    Sleep(200)

    def lambda_1122B():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1122B)
    Sleep(200)

    def lambda_11248():
        OP_97(0x104, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_11248)
    Sleep(200)

    def lambda_11265():
        OP_97(0x109, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_11265)
    Sleep(200)

    def lambda_11282():
        OP_97(0x105, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_11282)
    Return()

    # Function_34_11209 end

    def Function_35_11298(): pass

    label("Function_35_11298")

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

    def lambda_11407():
        OP_95(0xFE, 11000, 850, 12300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11407)

    def lambda_11421():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_11421)
    WaitChrThread(0x9, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(300)

    def lambda_11452():
        OP_95(0xFE, 14100, 850, 12300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11452)
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
            "#01110F#3607V#30WUmm, hello?\x02\x03",
            "#01109F#3608VThis is Crossbell\x01",
            "Police, Special Support\x01",
            "Sectiooon.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE18)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Young Girl's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ah... Is that you, KeA?\x02",
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
            "#01105FAh, it's Tio!\x02\x03",
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
            "Haha, it's just a\x01",
            "regular orbal call,\x01",
            "unlike yesterday.\x02\x03",
            "...Is anyone there?\x02",
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
            "#01100FNo. Even chief left a\x01",
            "little while ago.\x02\x03",
            "Zeit's here though.\x02",
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
            "Hmm, I see.\x02\x03",
            "Actually, I couldn't\x01",
            "contact Lloyd and the\x01",
            "others' ENIGMAs.\x02\x03",
            "And so, I called the\x01",
            "Support Section\x01",
            "directly, but...\x02",
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
            "#01105FHmm, really?\x02\x03",
            "#01111FA pure white falcon gave Lloyd\x01",
            "and the others an invitation,\x01",
            "and they went out.\x02",
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
            "A pure white falcon?\x02",
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
            "#01110FYeah. He said his name\x01",
            "was Sieg and he talks\x01",
            "like Zeit.\x02",
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
            "It sounds like quite a\x01",
            "bit is happening over\x01",
            "there.\x02",
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
            "#1S#40W...everyone. Thank you\x01",
            "for waiting.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#1S#40WLｳman... arriving...\x02",
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
            "─Looks like it's time.\x02\x03",
            "KeA, I'll call you\x01",
            "later. Say hi to\x01",
            "everyone for me.\x02",
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
            "#01109FSure! See you!\x02",
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
        "Oh, you're back.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_11A7B():

        label("loc_11A7B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_11A7B")

    QueueWorkItem2(0x9, 2, lambda_11A7B)
    OP_68(1960, 1750, 2650, 2500)
    MoveCamera(40, 17, 0, 2500)
    Sleep(2000)

    def lambda_11AAC():
        OP_95(0xFE, 1000, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11AAC)

    def lambda_11AC6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_11AC6)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x2D, 0x1F4)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#01101F#12PAh, Chief.\x02\x03",
            "#01106FIf you had come back\x01",
            "sooner, you could've\x01",
            "talked to Tio!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01005F#6POh, she called?\x02\x03",
            "#01002FAnd, what did she say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01110F#12PUmm, you see...\x02",
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

    # Function_35_11298 end

    def Function_36_11BE7(): pass

    label("Function_36_11BE7")


    def lambda_11BEC():
        OP_95(0xFE, 1000, 850, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11BEC)
    WaitChrThread(0x8, 1)

    def lambda_11C0A():
        OP_95(0xFE, 10000, 850, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11C0A)
    WaitChrThread(0x8, 1)
    Return()

    # Function_36_11BE7 end

    def Function_37_11C24(): pass

    label("Function_37_11C24")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetScenarioFlags(0x141, 5)
    OP_29(0xA3, 0x1, 0x14)
    OP_29(0xA3, 0x1, 0x15)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_11C50")
    Jump("loc_11C55")

    label("loc_11C50")

    OP_29(0x75, 0x4, 0x40)

    label("loc_11C55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_11C66")
    Jump("loc_11C6B")

    label("loc_11C66")

    OP_29(0x76, 0x4, 0x40)

    label("loc_11C6B")

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
            "#6P#00003F...As I thought, some\x01",
            "new ones came in.\x02\x03",
            "#00001FHmm, they all worry me,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00104FIf we have time, let's\x01",
            "take care of them.\x02\x03",
            "#00100FAfter all, we're free\x01",
            "this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FWe can go to the\x01",
            "outskirts using our car,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11F66():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_11F66)
    WaitChrThread(0x103, 2)
    Sleep(150)

    ChrTalk(
        0x103,
        (
            "#00204F#5PA car, huh. I'm looking\x01",
            "forward to it.\x02\x03",
            "#00202FAnd it was developed by\x01",
            "ZCF?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FYeah. It's a new model\x01",
            "that even those Section\x01",
            "One guys envy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FBut you just got back\x01",
            "yesterday, Tio. Are you\x01",
            "alright getting up so early?\x02\x03",
            "#00000FIf you like, you can take it\x01",
            "easy until this afterno─\x02",
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
        "#6P#00006FSorry, my bad.\x02",
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
            "#6P#00309FHaha, it really feels\x01",
            "like PeTiote's back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00109FHaha, that's right.\x02\x03",
            "#00102FIt feels more natural\x01",
            "with Tio in front of the\x01",
            "terminal.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_121AE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_121AE)
    Sleep(50)

    def lambda_121BE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_121BE)
    WaitChrThread(0x109, 2)

    ChrTalk(
        0x109,
        (
            "#12P#10109FHaha. You all are really in\x01",
            "sync.\x02\x03",
            "#10102FFor now... This is the full\x01",
            "membership of the reformed\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PHaha. As leader, aren't\x01",
            "you deeply moved?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FYeah... That's right.\x02\x03",
            "#00002F─Anyhow, Tio. It's good\x01",
            "to be working with you\x01",
            "again.\x02\x03",
            "And also, thanks for\x01",
            "coming to help us in our\x01",
            "time of need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#5POf course. And same\x01",
            "here- let's do our best\x01",
            "together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FHaha, the tension's\x01",
            "risen somehow, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#01004F#5PHehe... Most importantly, you\x01",
            "guys are in gear.\x02\x03",
            "#01002FWell with that energy, you\x01",
            "won't get swallowed up by the\x01",
            "trade conference atmosphere.\x02\x03",
            "Just be useful to security by\x01",
            "doing things in your own way.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12494():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12494)
    Sleep(50)

    def lambda_124A4():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_124A4)
    Sleep(50)

    def lambda_124B4():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_124B4)
    Sleep(50)

    def lambda_124C4():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_124C4)
    Sleep(50)

    def lambda_124D4():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_124D4)
    Sleep(50)

    def lambda_124E4():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_124E4)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    def lambda_12509():

        label("loc_12509")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_12509")

    QueueWorkItem2(0x101, 2, lambda_12509)

    def lambda_1251B():

        label("loc_1251B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1251B")

    QueueWorkItem2(0x102, 2, lambda_1251B)

    def lambda_1252D():

        label("loc_1252D")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1252D")

    QueueWorkItem2(0x103, 2, lambda_1252D)

    def lambda_1253F():

        label("loc_1253F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1253F")

    QueueWorkItem2(0x104, 2, lambda_1253F)

    def lambda_12551():

        label("loc_12551")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_12551")

    QueueWorkItem2(0x109, 2, lambda_12551)

    def lambda_12563():

        label("loc_12563")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_12563")

    QueueWorkItem2(0x105, 2, lambda_12563)

    ChrTalk(
        0x101,
        "#12P#00000FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FWill you be standing by\x01",
            "at HQ, Chief?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01006F#5PYeah. They all conspired\x01",
            "and forced it on me.\x02\x03",
            "#01000FI'll be around as backup,\x01",
            "but I won't get directly\x01",
            "involved in tower security.\x02\x03",
            "However, if something\x01",
            "happens, you absolutely\x01",
            "must contact me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F...Thanks for the\x01",
            "backup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FWe're counting on you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01002F#5PAlright then. I'm\x01",
            "heading out.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x8, 0x2DB4, 0x2AF8, 0x1F4)

    def lambda_12727():
        OP_95(0xFE, 11700, 850, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_12727)
    WaitChrThread(0x8, 1)
    OP_68(12900, 1750, 9800, 3000)

    def lambda_12756():
        OP_95(0xFE, 5700, 850, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_12756)
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
            "#5P#00005FCome to think of it, was\x01",
            "KeA at the library?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12822():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_12822)
    Sleep(100)

    def lambda_12832():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_12832)

    def lambda_1283F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1283F)
    Sleep(50)

    def lambda_1284F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1284F)

    def lambda_1285C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1285C)
    WaitChrThread(0x102, 2)

    ChrTalk(
        0x102,
        (
            "#12P#00104FYeah, she left first\x01",
            "thing this morning.\x02\x03",
            "#00100FIt seems she'll be back\x01",
            "by noon, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00002FI see. Everything'll be\x01",
            "fine, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FAlright, then let's head\x01",
            "out ourselves!\x02",
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
            "Tio has joined the\x01",
            "party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can change attack\x01",
            "members from [TACTICS]\x01",
            "under the camp menu.\x07\x00\x02",
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

    # Function_37_11C24 end

    def Function_38_129FA(): pass

    label("Function_38_129FA")

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
            "#11P#00003FThe sandbank along St. Ursula\x01",
            "Byroad and the outskirts of\x01",
            "East Crossbell Highway...\x02\x03",
            "#00001FWe haven't been to either\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FIt looks like neither\x01",
            "are huge like the one at\x01",
            "the old mine, but...\x02\x03",
            "#00301FI think it's best if\x01",
            "we're fully prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FAnd... Identify the\x01",
            ""cause", right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PYes...\x02\x03",
            "#00101FIt seems there's also reports\x01",
            "that the higher elements of time,\x01",
            "space and mirage are at work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FRegarding activity of the\x01",
            "higher elements, I think I\x01",
            "will be able to sense them.\x02\x03",
            "#00208FHowever, as for the\x01",
            ""cause"... It might be a\x01",
            "little hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FIf I recall, the cause of the\x01",
            "Tower and Temple events isn't\x01",
            "known...\x02\x03",
            "#10305FCome to think of it, wasn't\x01",
            "the Fort of Sun at the Ancient\x01",
            "Battlefield like that too?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00006FYeah. It was certainly\x01",
            "like that when we\x01",
            "entered, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#5PIt's just, after we solved\x01",
            "the incident, it seems the\x01",
            "anomalies disappeared.\x02\x03",
            "#00108FBells like the one at the\x01",
            "Temple don't seem to be\x01",
            "the cause either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FIf that's the case,\x01",
            "identifying the cause\x01",
            "seems difficult...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FAnyway, all we can do is\x01",
            "go there, so let's do\x01",
            "just that.\x02\x03",
            "#00300FI bet other jobs have\x01",
            "come in for us as well.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#11P#00003FRight...\x02\x03",
            "#00000FAlright, let's depart\x01",
            "after checking the\x01",
            "support requests.\x02",
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

    # Function_38_129FA end

    def Function_39_131CE(): pass

    label("Function_39_131CE")

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

    def lambda_132AD():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_132AD)
    Sleep(100)

    def lambda_132BD():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_132BD)
    Sleep(100)

    def lambda_132CD():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_132CD)
    Sleep(100)

    def lambda_132DD():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_132DD)
    Sleep(100)

    def lambda_132ED():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_132ED)
    Sleep(100)

    def lambda_132FD():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_132FD)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00003F#5PAs I thought, it seems\x01",
            "quite a few have come\x01",
            "in...\x02\x03",
            "#00008FI don't think it's\x01",
            "because Arios can't act\x01",
            "right now, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11P...Right...\x02\x03",
            "#00108FIt seems chief went to\x01",
            "the hospital to visit\x01",
            "someone today...\x02\x03",
            "#00101FIt might be a good idea\x01",
            "for us to visit as well\x01",
            "when we're nearby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FI know, right? Looks\x01",
            "like Keddo went\x01",
            "yesterday.\x02\x03",
            "#00308F...She was real\x01",
            "depressed, wasn't she.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FYes... I'm a little\x01",
            "worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FIf we use our car, it\x01",
            "won't take long to get\x01",
            "there...\x02\x03",
            "#10100FLet's go visit if we\x01",
            "have time.\x02",
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
            "#12P#10303FBut still... eyesight\x01",
            "recovery surgery...?\x02\x03",
            "#10301FIsn't that still a\x01",
            "difficult field?\x02",
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
            "#00108F#11PIt's not the case that\x01",
            "the surgery was a\x01",
            "complete failure, but...\x02",
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

    # Function_39_131CE end

    def Function_40_136BC(): pass

    label("Function_40_136BC")

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
            "#5P#01006F─I see. The flower that\x01",
            "was an ingredient in\x01",
            "that drug, eh?\x02\x03",
            "#01001FIf that's the case, even\x01",
            "the police can't ignore\x01",
            "it any longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11PYes, I was thinking about\x01",
            "continuing our cooperation\x01",
            "with the guild, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FHave any other\x01",
            "concerning cases come\x01",
            "in?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#11P#01003FYeah, but well, let the other\x01",
            "sections handle them.\x02\x03",
            "#01000FAnyhow, with the upcoming state\x01",
            "independence referendum, a certain\x01",
            "amount of confusion can't be avoided.\x02\x03",
            "Right now, eliminating uncertain\x01",
            "elements should be your top priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FRight, that's true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PIn other words, crisis\x01",
            "management.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FBut in that case... What\x01",
            "should we make today's\x01",
            "objective?\x02\x03",
            "#00200FWe finished our part of\x01",
            "the Cryptids investigation\x01",
            "yesterday as well.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#00302F#11PWell, we could go help\x01",
            "the guild's bracers, no?\x02",
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
        (
            "#10305F#12PAre you worried about\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00003F#11PWell... I was just\x01",
            "thinking...\x02\x03",
            "#00001FWhy don't we try\x01",
            "visiting Rosenberg\x01",
            "Studio?\x02",
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
        (
            "#6P#10101FThe one said to be\x01",
            "connected to\x01",
            "Ouroboros...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PI see... I totally\x01",
            "forgot.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_144A9")

    ChrTalk(
        0x101,
        (
            "#00003F#11POf course without a\x01",
            "search warrant, we can't\x01",
            "force our way inside.\x02\x03",
            "#00001FHowever... That old man\x01",
            "said something like this\x01",
            "before:\x02",
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
            "However, I don't have\x01",
            "anything in particular\x01",
            "to tell you right now.\x02\x03",
            "If you have other\x01",
            "business, you can come\x01",
            "visit again.\x02\x03",
            "I'll at least hear what\x01",
            "you have to say out of\x01",
            "deference for Renne.\x07\x00\x02",
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
    Jump("loc_14659")

    label("loc_144A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_145A8")

    ChrTalk(
        0x101,
        (
            "#00006F#11POf course without a search\x01",
            "warrant, we can't force our\x01",
            "way inside.\x02\x03",
            "#00001FBased on what Renne told us,\x01",
            "he doesn't seem like someone\x01",
            "who can't be reasoned with.\x02\x03",
            "And due to Mrs. Imelda's\x01",
            "request, we more or less\x01",
            "know him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14659")

    label("loc_145A8")


    ChrTalk(
        0x101,
        (
            "#00006F#11POf course without a search\x01",
            "warrant, we can't force our\x01",
            "way inside.\x02\x03",
            "#00001FBased on what Renne told us,\x01",
            "he doesn't seem like someone\x01",
            "who can't be reasoned with.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14659")


    ChrTalk(
        0x103,
        (
            "#6P#00203FIt may be worth paying\x01",
            "him a visit.\x02\x03",
            "#00201FIt may be dangerous,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_1473B")

    ChrTalk(
        0x105,
        (
            "#10304F#12PIndeed. I'd like to get\x01",
            "a handle on that strange\x01",
            "boy's objectives.\x02\x03",
            "#10302FHe may be staying at the\x01",
            "studio.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_147B7")

    label("loc_1473B")


    ChrTalk(
        0x105,
        (
            "#10304F#12PIndeed. I'd like to get\x01",
            "a handle on that strange\x01",
            "boy's objectives.\x02\x03",
            "#10302FHe may be staying at the\x01",
            "studio.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_147B7")


    ChrTalk(
        0x109,
        (
            "#6P#10100FI-I agree!\x02\x03",
            "#10106FAnd a dangerous foreign\x01",
            "power has reared their heads\x01",
            "in Crossbell as it is...\x02\x03",
            "#10101FWe can't leave such a\x01",
            "suspicious group alone any\x01",
            "longer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FRight...\x02\x03",
            "#00101FShould we visit the\x01",
            "studio directly?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(250)

    ChrTalk(
        0x101,
        (
            "#00000F#11PYeah, let's try checking\x01",
            "it out.\x02\x03",
            "#00003FDepending on the\x01",
            "situation, we might need\x01",
            "a search warrant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PRight...\x02\x03",
            "#00300FAlright, then let's go\x01",
            "already!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01105F#6PHey, hey everyone.\x02\x03",
            "Leaving already?\x02",
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
            "#00005F#11PYeah. That was the plan,\x01",
            "anyway.\x02\x03",
            "#00000FYou're going to the\x01",
            "library today, right\x01",
            "KeA?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01103FHmm... I think I'll look\x01",
            "for a braille book for\x01",
            "Shizuku.\x02\x03",
            "#01110FI'll get groceries on my\x01",
            "way back. Anything you\x01",
            "want for dinner?\x02",
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
            "#5P#00105FShopping for\x01",
            "groceries... Will you be\x01",
            "alright, KeA?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00205FIt's true that you're\x01",
            "always cooking for us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01104FYes, I always buy from\x01",
            "Momo's father and from\x01",
            "Oscar too.\x02\x03",
            "#01110FI'm also friends with the\x01",
            "old lady at the department\x01",
            "store's food corner...\x02",
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
        (
            "#00309F#11PHaha, well it's Keddo\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01004FIn that case... It's getting a\x01",
            "little colder, so maybe some\x01",
            "kind of hot pot would be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FAh, good idea. That'll\x01",
            "give us all energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PHot pot... So, it has to\x01",
            "be Eastern style, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00100FKeA, will you be\x01",
            "alright?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01103FHmm, I think I'll manage.\x02\x03",
            "#01101FI want to make the broth\x01",
            "properly, so I'll have to stop\x01",
            "by the East Street stalls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#11POh, you're goin' all out\x01",
            "for it, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FI'm looking forward to\x01",
            "when we get home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#11PThank you, KeA.\x02\x03",
            "#00002FWe'll try our best to\x01",
            "not come home late\x01",
            "tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#01109FEhehe... Alright!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_152C3")
    Jump("loc_152C8")

    label("loc_152C3")

    OP_29(0x81, 0x4, 0x40)

    label("loc_152C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_152D9")
    Jump("loc_152DE")

    label("loc_152D9")

    OP_29(0x82, 0x4, 0x40)

    label("loc_152DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_152EF")
    Jump("loc_152F4")

    label("loc_152EF")

    OP_29(0x84, 0x4, 0x40)

    label("loc_152F4")

    OP_C9(0x1, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    Call(0, 67)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_40_136BC end

    def Function_41_15311(): pass

    label("Function_41_15311")

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

    def lambda_153F0():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_153F0)
    Sleep(100)

    def lambda_15400():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_15400)
    Sleep(100)

    def lambda_15410():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_15410)
    Sleep(100)

    def lambda_15420():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_15420)
    Sleep(100)

    def lambda_15430():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_15430)
    Sleep(100)

    def lambda_15440():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_15440)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x105,
        (
            "#11P#10300FA few new ones have\x01",
            "arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00300FWhat do we do? Seems like it'll be all\x01",
            "right to to deal with them after we've\x01",
            "gone to the Doll Studio, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#5PWell, I wonder about\x01",
            "that. We don't know how\x01",
            "that visit will go.\x02\x03",
            "#00001FI think it's best to\x01",
            "clear the urgent support\x01",
            "requests first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FYou're right... We might\x01",
            "need to perform a\x01",
            "compulsory search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#11PThen, let's head to the\x01",
            "mountain path Doll\x01",
            "Studio once we're ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203F(I've very drawn to the\x01",
            "theme park side job...)\x02",
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

    # Function_41_15311 end

    def Function_42_156E4(): pass

    label("Function_42_156E4")

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
        (
            "#00004F#11P─Phew, thanks for the\x01",
            "food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#11PMaaan, hodgepodge does a\x01",
            "cold body good.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(200)

    ChrTalk(
        0x102,
        (
            "#5P#00102F*giggle*, indeed. There\x01",
            "were eggs and chicken in\x01",
            "it, too.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x1)
    Sleep(100)

    ChrTalk(
        0x109,
        (
            "#12P#10109FThanks for the food,\x01",
            "KeA.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(100)

    ChrTalk(
        0x103,
        "#6P#00202FIt was delicious.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x2)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#6P#01104FEhehe, I just used the\x01",
            "ingredients from\x01",
            "yesterday's hot pot.\x02\x03",
            "#01110FWazy, are you full?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x2)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10304F#11P...Yeah. It was rich and\x01",
            "delicious.\x02\x03",
            "#10302FThanks for the food,\x01",
            "KeA.\x02",
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
            "#5P#01004FHmph... You're finally\x01",
            "back to your senses.\x02\x03",
            "#01000FAbout Wald Wales'\x01",
            "case... The CGF is\x01",
            "continuing the search.\x02\x03",
            "Don't brood over it that\x01",
            "much.\x02",
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
        "#10304F#12P...Haha, you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#11PHowever, it's certain\x01",
            "Wald got his hands on\x01",
            "Gnosis somehow.\x02\x03",
            "We've got to do whatever\x01",
            "it takes to discover\x01",
            "how!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01003FSection Two is already\x01",
            "investigating that.\x02\x03",
            "I also heard Section One is\x01",
            "taking part in the investigation\x01",
            "concerning those foreign powers.\x02\x03",
            "#01000FWell, don't be so impatient is\x01",
            "what I'm trying to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11P...Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FIn the end, they were able\x01",
            "to fully repair the\x01",
            "derailment site yesterday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01005FYeah. Through yesterday evening only one side\x01",
            "could be used, but it seems they worked all\x01",
            "through the night to fully restore service.\x02\x03",
            "#01004FIt ended without any major consequences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106F*sigh*... Thank\x01",
            "goodness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FThe transcontinental railway is an\x01",
            "important route... If it was still offline,\x01",
            "there'd be chaos, no doubt about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PIf it did turn out like that, it\x01",
            "would've been even more material for\x01",
            "Imperial and Republican arm twistin'.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00003F#5PYeah... You said it.\x02\x03",
            "#00001F...So, should we check\x01",
            "the support requests?\x02\x03",
            "It's about time for them\x01",
            "to come in today.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(150)

    ChrTalk(
        0x102,
        "#6P#00100FYes, let's.\x02",
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
        "#6P#01105FThe phone's ringing?\x02",
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

    def lambda_1655B():
        OP_95(0xFE, 14100, 850, 12300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1655B)
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
            "#00001FYes, this is Crossbell\x01",
            "Police, Special Support\x01",
            "Section...\x02",
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
            "the guild receptionist.\x02",
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
            "our report on Ouroboros?\x02",
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
            "Yes... To be perfectly honest it\x01",
            "was quite helpful.\x02\x03",
            "I contacted Lｳman HQ and they're\x01",
            "analyzing the information at\x01",
            "present...\x02\x03",
            "Well, since they're a mysterious\x01",
            "group I honestly don't know how\x01",
            "much they'll be able to do, though.\x02",
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
            "#00006FI see.\x02\x03",
            "#00005FUmm, you called to tell\x01",
            "us that?\x02",
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
            "Ah, no. That's not it.\x02\x03",
            "I'd like to ask you a little\x01",
            "something... Did you happen\x01",
            "to see our Ling or Eolia?\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 2)), scpexpr(EXPR_END)), "loc_168FB")
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001FUmm, we saw them\x01",
            "yesterday at the\x01",
            "hospital, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_16952")

    label("loc_168FB")

    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FUmm, we saw them the day\x01",
            "before yesterday at\x01",
            "Orchis Tower...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_16952")

    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Michel's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I see... That's right.\x02\x03",
            "...Honestly, I wonder\x01",
            "what those ladies are\x01",
            "doing.\x02",
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
            "#00013FUmm... You can't contact\x01",
            "them?\x02",
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
            "Yes, I haven't been able\x01",
            "to contact their ENIGMAs\x01",
            "since last night.\x02\x03",
            "Well, it's not that\x01",
            "unusual, so I'm not that\x01",
            "worried about them.\x02",
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
            "#00003FI see...\x02",
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
            "Well, don't worry about\x01",
            "it. You guys are busy\x01",
            "too.\x02\x03",
            "That delinquent leader,\x01",
            "was it? You must have it\x01",
            "hard too, don't you?\x02",
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
            "If you happen to see either\x01",
            "of those two, tell them to\x01",
            "contact me immediately.\x02\x03",
            "Well then, do your best,\x01",
            "alright?㈱\x02",
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
            "#00004FWe will, thanks.\x02",
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
            "#01000FLooked like that was\x01",
            "from the Guild. What's\x01",
            "up?\x02",
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

    def lambda_16D04():
        OP_96(0xFE, 0x319C, 0x352, 0x20D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16D04)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained that bracers Ling\x01",
            "and Eolia haven't been able to be\x01",
            "contacted ever since last night.\x07\x00\x02",
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
        "#6P#00101FThose bracers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#12PThey're those two highly\x01",
            "skilled ladies, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PYeah, especially Eolia.\x01",
            "She's my type after\x01",
            "Cecil.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(150)

    ChrTalk(
        0x103,
        (
            "#6P#00211FI don't think anyone\x01",
            "cares about that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_16FC7")

    ChrTalk(
        0x109,
        (
            "#12P#10106F#NBut, I'm a little\x01",
            "worried.\x02\x03",
            "#10108FThey seemed to be\x01",
            "keeping a tight\x01",
            "schedule.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#5P#00006FRight... Even when we fought\x01",
            "them before, I felt they were\x01",
            "calculating every single action.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17078")

    label("loc_16FC7")


    ChrTalk(
        0x109,
        (
            "#12P#10106F#NBut, I'm a little\x01",
            "worried.\x02\x03",
            "#10101FAlthough they're bracers,\x01",
            "they seemed to be keeping\x01",
            "a tight schedule.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#5P#00003FRight... Arios seems\x01",
            "like that too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17078")


    ChrTalk(
        0x8,
        (
            "#01003F#11PWell if you have time,\x01",
            "feel free to show up at\x01",
            "the Guild during work.\x02\x03",
            "#01002FWe've got to support\x01",
            "each other in times like\x01",
            "these.\x02",
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
            "leaving already?\x02\x03",
            "#01102FWill hot pot be ok\x01",
            "today?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17183():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17183)
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
            "#5P#00002FYeah. We'll be home\x01",
            "earlier than usual\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00106FSorry, KeA.\x02\x03",
            "#00108FAlthough you went to the\x01",
            "trouble of making it for us\x01",
            "yesterday, we couldn't eat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01121FNo, don't be. You're all\x01",
            "doing your best, right?\x02\x03",
            "#01109FIn that case, KeA wants\x01",
            "to do her best to help\x01",
            "you too.\x02",
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
            "#10309F#11PHaha... She's got quite\x01",
            "the destructive force,\x01",
            "doesn't she.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)

    ChrTalk(
        0x103,
        (
            "#6P#00204FAccording to the weather\x01",
            "forecast, it should stop\x01",
            "raining this afternoon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#11PLet's take care of work\x01",
            "properly and be back\x01",
            "home quickly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10102F#NRoger!\x02",
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

    # Function_42_156E4 end

    def Function_43_17707(): pass

    label("Function_43_17707")

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
        (
            "#01003F─I see, you're going\x01",
            "back, eh?\x02",
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
        0x109,
        (
            "#10106F#11PYes... Originally, I\x01",
            "wanted to train here for\x01",
            "half a year, but...\x02\x03",
            "#10101FAfter thinking things\x01",
            "over─ I decided to go\x01",
            "back.\x02",
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
            "#5P#00106F...That's\x01",
            "understandable.\x02\x03",
            "#00108FThe CGF suffered heavy\x01",
            "damage in this incident\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FExcellent young members are\x01",
            "probably desperately needed\x01",
            "over there right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#11PAhaha... I don't know about the\x01",
            ""excellent" part, though.\x02\x03",
            "#10108F...I'm sorry. For making this decision\x01",
            "just when we're finishing up restoration\x01",
            "work and returning to our normal duties...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FNo... Don't worry about\x01",
            "it.\x02\x03",
            "#00002FWith the current situation\x01",
            "in Crossbell, the CGF has\x01",
            "a big role to play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PWe will miss you, but...\x01",
            "We'll have to accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01108F#11PNoｱl... Are you going\x01",
            "away...?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x1)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10112F#5PAhaha... Yeah.\x02\x03",
            "It'll be incredibly sad\x01",
            "not being able to see\x01",
            "you, KeA...\x02",
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
            "#10102F#5PBut I'll come see you\x01",
            "again sometime!\x02\x03",
            "#10100F#30WAnd Fran too...\x02\x01",
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
        "#00208F#11PNoｱl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10301F...They said your sister\x01",
            "will remain hospitalized\x01",
            "for some time, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#5PYes... Since her surgery succeeded\x01",
            "and she's regained consciousness,\x01",
            "there's nothing to worry about...\x02\x03",
            "#10113FBut her strength hasn't returned\x01",
            "at all...\x02",
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
            "#10112F#11PAhaha... Randy, please\x01",
            "don't make that face.\x02\x03",
            "#10104FShe's a police officer too.\x01",
            "She was prepared to accept\x01",
            "some degree of danger.\x02\x03",
            "#10100FIf you're thinking it's\x01",
            "your fault... It's not, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00304F...Haha, alright.\x02\x03",
            "#00302FAnyway, if that's how it\x01",
            "is, then this is your\x01",
            "last day workin' with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#11PYes, I'll do my very\x01",
            "best for the rest of the\x01",
            "day!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10102F#11PIt's nice to be working\x01",
            "with you, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00004FYeah... Likewise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00102FNoｱl... It's nice to be\x01",
            "working with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#01003F─I'll get your transfer\x01",
            "papers in order.\x02\x03",
            "#01002FAnd it's been a while\x01",
            "since we went out for\x01",
            "dinner.\x02\x03",
            "On account of the\x01",
            "special occasion, it'll\x01",
            "be on me.\x02",
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
        "#6P#00002FHaha, good idea.\x02",
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
            "#6P#10309FHehe. In that case, should we go\x01",
            "to my friend's host club?\x02\x03",
            "#10302FThey'll get some well-dressed men\x01",
            "together and have a magnificent\x01",
            "farewell party ready for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0x109, 0x1)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10111F#5PWhaaat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00305FOh, that's an option.\x02\x03",
            "#00309FAlthough I'd be happier\x01",
            "with a place with\x01",
            "beautiful babes.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#11P#00111F*sigh*... That's not the\x01",
            "issue here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#11PThen, what about the MWL\x01",
            "restaurant where they do the\x01",
            "Mishy show? (*sparkling eyes*)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)

    ChrTalk(
        0x9,
        (
            "#01105F#5PIs there a restaurant\x01",
            "like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#01006FBefore that, guys...\x01",
            "Think about of my\x01",
            "wallet, will ya?\x02",
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
            "#6P#00012FAnyway, we've got to\x01",
            "finish up today's work\x01",
            "by evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#01203F#5P#NGrrowl... Woof.\x02",
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

    # Function_43_17707 end

    def Function_44_18801(): pass

    label("Function_44_18801")

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

    def lambda_188E0():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_188E0)
    Sleep(100)

    def lambda_188F0():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_188F0)
    Sleep(100)

    def lambda_18900():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_18900)
    Sleep(100)

    def lambda_18910():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_18910)
    Sleep(100)

    def lambda_18920():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_18920)
    Sleep(100)

    def lambda_18930():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_18930)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        (
            "#00108F#11PAs expected, there's a\x01",
            "lot of them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FHowever, it looks like\x01",
            "no urgent ones have come\x01",
            "in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FRight. Even that one\x01",
            "from Abbas seems to be\x01",
            "not so urgent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FWell, let's keep doin'\x01",
            "our rounds and take care\x01",
            "of them little by little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FRight!\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#5P─Listen, everyone.\x02\x03",
            "#00002FWant to go to St. Ursula\x01",
            "Hospital during one of\x01",
            "our breaks?\x02",
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

    def lambda_18B72():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_18B72)
    Sleep(50)

    def lambda_18B82():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_18B82)
    Sleep(50)

    def lambda_18B92():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_18B92)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x109,
        "#12P#10105FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#11PThat's right... I think\x01",
            "that's a great idea.\x02\x03",
            "#00104FWe've been so busy this\x01",
            "past week that we haven't\x01",
            "gone to see her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FAgreed.\x02\x03",
            "#00302FSince Fran's regained\x01",
            "consciousness, we've\x01",
            "gotta go pay her a visit.\x02",
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
            "#12P#10304FIndeed, it's sad not\x01",
            "hearing her lively voice\x01",
            "through the terminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201FYes... I'd at least like\x01",
            "to hear her voice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PNoｱl, don't hold back.\x02\x03",
            "#00000FEven to us, Fran has an\x01",
            "important supporting\x01",
            "role.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_18DBC():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_18DBC)
    Sleep(50)

    def lambda_18DCC():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_18DCC)
    Sleep(50)

    def lambda_18DDC():
        TurnDirection(0x104, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_18DDC)
    Sleep(50)

    def lambda_18DEC():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_18DEC)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        (
            "#12P#10104FEveryone... Thank you\x01",
            "very much.\x02\x03",
            "#10102FThen, let's go to St.\x01",
            "Ursula Hospital during\x01",
            "one of our breaks.\x02",
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

    # Function_44_18801 end

    def Function_45_18ED3(): pass

    label("Function_45_18ED3")

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
            "#30WTwo days later──\x02\x03",
            "The referendum on the\x01",
            "question of Crossbell State\x01",
            "independence was held.\x02\x03",
            "The results were counted\x01",
            "the same day...\x02\x03",
            "One week later─ Crossbell\x01",
            "headed to its "fateful\x01",
            "day".\x02",
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
            "#00301F...With this, the\x01",
            "unthinkable has\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00106FYes... I honestly didn't think\x01",
            "it would happen this quickly.\x02\x03",
            "#00108FI was thinking of checking with\x01",
            ""uncle" but I haven't been able\x01",
            "to contact him since yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206FChief went to an early\x01",
            "morning meeting at HQ\x01",
            "and isn't back yet...\x02\x03",
            "#00201FCould he have gone to\x01",
            "check on that "State\x01",
            "Guard" organization?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FYeah... Honestly, I'm\x01",
            "shocked.\x02\x03",
            "#00001FIt's not just us, either.\x01",
            "Police management probably\x01",
            "feel the same way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FHey now... Isn't that\x01",
            "strange?\x02\x03",
            "#00301FWhat about Noｱl,\x01",
            "Mireille and the others?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#6P#00208FThe CGF can't be contacted\x01",
            "at present.\x02\x03",
            "They've most likely received\x01",
            "too many inquiries and shut\x01",
            "off the flow of information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00103F...That's understandable.\x02\x03",
            "#00101FRegarding the asset freeze...\x01",
            "There's no way the Empire and\x01",
            "Republic are going to remain silent.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)

    ChrTalk(
        0x101,
        (
            "#5P#00008F"We are prepared to use\x01",
            "force"... I'm worried\x01",
            "about the border regions.\x02",
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
            "#5P#00002FSorry... Did we scare\x01",
            "you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#01121F...No. KeA understands\x01",
            "that something serious\x01",
            "is happening too.\x02\x03",
            "#01105FBy the way, I haven't\x01",
            "seen Wazy this morning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00005FYes, now that you\x01",
            "mention it...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#12P#00205FAh, Wazy said he had\x01",
            "some minor business to\x01",
            "attend to and went out.\x02\x03",
            "#00200FI think it was just\x01",
            "after chief left.\x02",
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
            "#5P#00106FConsidering how late it\x01",
            "is, I'm not happy about\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)

    ChrTalk(
        0x104,
        "#00308FHmm...\x02",
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
        "#00105FAt a time like this?\x02",
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

    def lambda_1998C():
        OP_95(0xFE, 3500, 0, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1998C)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xE1, 0x1F4)

    ChrTalk(
        0x101,
        "#00001F─Yes, who is it?\x02",
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
            "#1P#2SThank goodness... You're\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Woman's Voice",
        "#1P#2SIt's me, Cecil.\x07\x00\x02",
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
        "#00011FCecil!?\x02",
    )

    CloseMessageWindow()

    def lambda_19AF2():
        OP_95(0xFE, 1000, 0, 2500, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19AF2)
    WaitChrThread(0x101, 1)

    def lambda_19B10():
        OP_95(0xFE, 1000, 0, 1000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19B10)
    WaitChrThread(0x101, 1)
    Sound(806, 0, 80, 0)
    Sleep(300)
    Sound(103, 0, 100, 0)

    def lambda_19B3D():
        OP_96(0xFE, 0x3E8, 0x0, 0xAF0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19B3D)
    Sleep(500)
    SetChrPos(0xB, 1000, 0, -1500, 0)

    def lambda_19B6B():
        OP_96(0xFE, 0x3E8, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_19B6B)

    def lambda_19B85():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_19B85)
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

    def lambda_19BDF():
        OP_95(0xFE, 2000, 0, 3800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19BDF)
    Sleep(500)

    def lambda_19BFC():
        OP_95(0xFE, 2000, 0, 2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_19BFC)
    WaitChrThread(0x101, 1)

    def lambda_19C1A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19C1A)
    WaitChrThread(0xB, 1)

    def lambda_19C2B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_19C2B)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#5P#00105FCecil... Has something\x01",
            "happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FDon't see your face too\x01",
            "often around here.\x02",
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
            "Sorry for visiting all of a sudden.\x02\x03",
            "Umm... Did Arios come here,\x01",
            "perhaps?\x02",
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
        "#00005F#5P...Arios?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00205FNo, he didn't... What's\x01",
            "going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#05926F...Well...\x02\x03",
            "#05928FHe came late last night\x01",
            "to the hospital and took\x01",
            "Shizuku with him.\x02\x03",
            "He completed her\x01",
            "discharge papers on the\x01",
            "spot...\x02",
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
        "#00005F#5PHuh!?\x02",
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
            "#6P#05926FAnd so, I went to the\x01",
            "guild to ascertain the\x01",
            "reason, but...\x02\x03",
            "Even Michel didn't have\x01",
            "a clue.\x02\x03",
            "#05921FAnd so, I came to visit\x01",
            "you all just in case.\x02",
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
            "#00301FThat ol' man... Why'd he\x01",
            "do somethin' like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FI feel the fact he did\x01",
            "it late at night isn't\x01",
            "normal, either.\x02",
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

    def lambda_1A147():
        TurnDirection(0x101, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A147)
    Sleep(50)

    def lambda_1A157():
        TurnDirection(0x102, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1A157)
    Sleep(50)

    def lambda_1A167():
        TurnDirection(0xB, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1A167)
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
            "#00301FIt's not an ENIGMA, so I\x01",
            "don't think it's\x01",
            "chief...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FCould it be someone\x01",
            "related to Arios?\x02",
        )
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
            "#4S#5PThank goodness! You're\x01",
            "there, Lloyd!\x07\x00\x02",
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
        "#12P#00105FThis voice... Grace?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00300FLooks that way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FUhmm... Grace, is\x01",
            "something wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5POf course there is! I wanted to\x01",
            "tell you guys!\x02\x03",
            "Just now, an unbelievable\x01",
            "notification came in from Orchis\x01",
            "Tower!\x02\x03",
            "It appears Mayor Dieter has\x01",
            "become the first President of the\x01",
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
            "#12P#00107FPresident... "U-Uncle"\x01",
            "has!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FHey now... What kind of\x01",
            "joke is this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5PI-I thought it was a\x01",
            "joke too, at first!\x02\x03",
            "However, that notice was\x01",
            "brought by a soldier in\x01",
            "a white uniform...\x02\x03",
            "He said he was from the\x01",
            "newly formed "State\x01",
            "Guard", you know!?\x07\x00\x02",
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
        (
            "#12P#00301FA soldier... Don't tell\x01",
            "me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5PYes, probably a member of the\x01",
            "CGF, but...\x02\x03",
            "A-Also... Don't freak out, ok?\x02\x03",
            "Immediately after President\x01",
            "Dieter took office, he nominated\x01",
            "the "Secretary of Defense".\x02\x03",
            "And he's─#350W─\x01",
            "#20WThat Arios.\x07\x00\x02",
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
        "#6P#00208F#30W...Arios?\x02",
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
            "#5PThe President's inaugural\x01",
            "speech is starting right\x01",
            "now!\x02\x03",
            "It'll even be broadcasted\x01",
            "via the orbal net, so\x01",
            "watch it if you want!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Youth's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2P#1S...Grace! I got\x01",
            "permission to cover this\x01",
            "somehow!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5P#2SWay to go! Well done,\x01",
            "Reins!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5P#3S─Sorry! I'm off to cover\x01",
            "the speech!\x02\x03",
            "Bye then～!\x07\x00\x02",
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
        "#6P#05928FWas that... real?\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00006FI-I don't know, but...\x02\x03",
            "#00013FThat Arios is the\x01",
            ""Secretary of\x01",
            "Defense"...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00107F"Secretary"... Then,\x01",
            "he's head of the "State\x01",
            "Guard"!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00310FN-No way... What about\x01",
            "his title of bracer!?\x02\x03",
            "#00306FAlso, ol' man Dieter\x01",
            "being the "President"...\x01",
            "it's too sudden...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201F...In any case, let's\x01",
            "watch the inaugural\x01",
            "address on the terminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007FRight!\x02",
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

    # Function_45_18ED3 end

    def Function_46_1AD56(): pass

    label("Function_46_1AD56")

    Fade(250)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 6050, 30, 5500, 180)
    OP_0D()

    def lambda_1AD7F():
        OP_95(0xFE, 4750, 30, 5500, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1AD7F)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0xE1, 0x1F4)
    Return()

    # Function_46_1AD56 end

    def Function_47_1ADA0(): pass

    label("Function_47_1ADA0")

    SetChrPos(0x101, 4100, 850, 10800, 90)

    def lambda_1ADB6():
        OP_96(0xFE, 0x3138, 0x352, 0x2A30, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1ADB6)
    WaitChrThread(0x101, 1)

    def lambda_1ADD4():
        OP_95(0xFE, 14100, 850, 12300, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1ADD4)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_47_1ADA0 end

    def Function_48_1ADF5(): pass

    label("Function_48_1ADF5")

    SetChrPos(0x102, 4300, 850, 10200, 90)

    def lambda_1AE0B():
        OP_96(0xFE, 0x37DC, 0x352, 0x27D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1AE0B)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_48_1ADF5 end

    def Function_49_1AE2C(): pass

    label("Function_49_1AE2C")

    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 2650, 850, 9600, 90)

    def lambda_1AE4F():
        OP_96(0xFE, 0x316A, 0x352, 0x2580, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1AE4F)
    WaitChrThread(0x104, 1)
    TurnDirection(0x104, 0x101, 500)
    Return()

    # Function_49_1AE2C end

    def Function_50_1AE70(): pass

    label("Function_50_1AE70")

    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 2200, 850, 11000, 90)

    def lambda_1AE93():
        OP_96(0xFE, 0x2FA8, 0x352, 0x2AF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1AE93)
    WaitChrThread(0x103, 1)
    TurnDirection(0x103, 0x101, 500)
    Return()

    # Function_50_1AE70 end

    def Function_51_1AEB4(): pass

    label("Function_51_1AEB4")

    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 800, 850, 10300, 90)

    def lambda_1AED2():
        OP_96(0xFE, 0x2A30, 0x352, 0x283C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1AED2)
    WaitChrThread(0x9, 1)
    Return()

    # Function_51_1AEB4 end

    def Function_52_1AEEC(): pass

    label("Function_52_1AEEC")

    SetChrPos(0xB, 800, 850, 11500, 90)

    def lambda_1AF02():
        OP_96(0xFE, 0x2A30, 0x352, 0x2CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1AF02)
    WaitChrThread(0xB, 1)
    Return()

    # Function_52_1AEEC end

    def Function_53_1AF1C(): pass

    label("Function_53_1AF1C")

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

    def lambda_1B0F8():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1B0F8)
    Sleep(50)

    def lambda_1B108():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1B108)
    Sleep(50)

    def lambda_1B118():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1B118)
    Sleep(50)

    def lambda_1B128():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1B128)
    Sleep(50)

    def lambda_1B138():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1B138)
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
            "#00007FYes, Lloyd speaking!\x02",
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
            "#00010FChief! The inaugural\x01",
            "speech just now─\x02",
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
            "Aside from whether it's right or\x01",
            "wrong, the CGF seems to have been\x01",
            "reorganized into the "State Guard".\x02\x03",
            "It's decided that we police will be\x01",
            "included as part of it as well.\x02",
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
            "#00013FEven Commander Sonya...\x02",
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
            "She was on the monitor,\x01",
            "right? Well── I guess she\x01",
            "accepts this.\x02\x03",
            "I don't know what'll happen,\x01",
            "but... For now, stay away\x01",
            "from Orchis Tower.\x02\x03",
            "The State Guard "soldiers"\x01",
            "are likely to be strictly\x01",
            "guarding it.\x02",
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
            "#00010FUgh... Understood.\x02",
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
            "─I'll call again. Don't\x01",
            "do anything rash,\x01",
            "alright?\x07\x00\x02",
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
        "#12P#00108F...What did chief say?\x02",
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
        (
            "#5P#00006FYes, about the State\x01",
            "Guard...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained what he\x01",
            "heard from Sergei.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#12P#00106FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PDamn, Commander Sonya\x01",
            "went to their side?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00206FWell considering her\x01",
            "position, I think she\x01",
            "had no choice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05923F#5P...Arios. So this is why\x01",
            "he took Shizuku with\x01",
            "him, then.\x02",
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

    def lambda_1B749():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B749)
    Sleep(50)

    def lambda_1B759():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1B759)
    Sleep(50)

    def lambda_1B769():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1B769)
    Sleep(50)

    def lambda_1B779():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1B779)
    Sleep(50)

    def lambda_1B789():
        TurnDirection(0x9, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1B789)
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
            "#12P#00108FRight... Having a\x01",
            "position like that could\x01",
            "affect Shizuku...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PShe could be targeted by\x01",
            "opposin' factions,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00208F...In this situation, I\x01",
            "can't say the chances\x01",
            "are zero.\x02",
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
            "#12P#00004FKeA... It's alright.\x02\x03",
            "#00000FArios is thinking of\x01",
            "Shizuku's safety.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B90B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1B90B)
    Sleep(50)
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(200)

    ChrTalk(
        0x9,
        (
            "#01121F#5PYeah... You're right.\x02\x03",
            "#01122F...Ehehe. I'm a little\x01",
            "worried though...\x02",
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
            "#12P#00008F...Cecil, I'm sorry but,\x01",
            "could you watch the\x01",
            "house for a little?\x02",
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

    def lambda_1BA5D():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1BA5D)
    Sleep(50)

    def lambda_1BA6D():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1BA6D)
    Sleep(50)

    def lambda_1BA7D():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1BA7D)
    Sleep(50)

    def lambda_1BA8D():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1BA8D)
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
            "#05925F#5PYes, I think it'll be\x01",
            "all right until evening,\x01",
            "but...\x02\x03",
            "#05921FAre you going somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FYeah─\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00001FListen, everyone.\x02\x03",
            "For now... Why don't we\x01",
            "go to the guild?\x02",
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
        "#12P#00101FA-Agreed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00201FIndeed. I want to ask\x01",
            "them about Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12PI know, right? This was\x01",
            "way too sudden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05923F#5P...Understood. I'll stay\x01",
            "here and watch the house\x01",
            "with KeA.\x02\x03",
            "#05920FThe situation looks\x01",
            "serious, so be very\x01",
            "careful.\x02\x03",
            "Don't do anything crazy.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1BD10():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1BD10)
    Sleep(50)

    def lambda_1BD20():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1BD20)
    Sleep(50)

    def lambda_1BD30():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1BD30)
    Sleep(50)

    def lambda_1BD40():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1BD40)
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
        "#00309F#12PThanks, Cecil!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00104FThen, we leave it to\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00202FKeA, please be a good\x01",
            "girl and watch the house\x01",
            "with Cecil.\x02",
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

    def lambda_1BE3D():

        label("loc_1BE3D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1BE3D")

    QueueWorkItem2(0xB, 2, lambda_1BE3D)

    def lambda_1BE4F():

        label("loc_1BE4F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1BE4F")

    QueueWorkItem2(0x9, 2, lambda_1BE4F)
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

    def lambda_1BF1A():

        label("loc_1BF1A")

        TurnDirection(0xB, 0x9, 500)
        Yield()
        Jump("loc_1BF1A")

    QueueWorkItem2(0xB, 2, lambda_1BF1A)

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

    def lambda_1BF59():
        OP_95(0xFE, 900, 850, 9700, 5500, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1BF59)
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

    # Function_53_1AF1C end

    def Function_54_1BFBF(): pass

    label("Function_54_1BFBF")

    OP_95(0xFE, 15150, 850, 8450, 4500, 0x1)
    OP_95(0xFE, 10150, 850, 8950, 4500, 0x1)
    OP_95(0xFE, 5150, 850, 9450, 4500, 0x1)
    OP_95(0xFE, 150, 850, 9450, 4500, 0x1)
    Return()

    # Function_54_1BFBF end

    def Function_55_1C010(): pass

    label("Function_55_1C010")

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

    def lambda_1C10B():
        OP_95(0xFE, -300, 0, 5300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1C10B)
    WaitChrThread(0xB, 1)
    Sleep(500)
    OP_93(0xB, 0x5A, 0x1F4)

    def lambda_1C133():
        OP_95(0xFE, 2300, 0, 5300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1C133)
    WaitChrThread(0xB, 1)
    Sleep(500)
    OP_93(0xB, 0x10E, 0x1F4)

    def lambda_1C15B():
        OP_95(0xFE, 1000, 0, 5300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1C15B)
    WaitChrThread(0xB, 1)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "#1PCecil!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_68(1000, 1000, 4100, 1500)
    SetChrPos(0x101, 300, 0, -1600, 0)
    BeginChrThread(0x101, 3, 0, 56)

    def lambda_1C1F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C1F8)
    Sleep(250)

    def lambda_1C20C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1C20C)
    Sleep(350)

    def lambda_1C220():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1C220)
    Sleep(450)

    def lambda_1C234():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1C234)
    OP_93(0xB, 0xB4, 0x1F4)

    ChrTalk(
        0xB,
        "#05921F#5PLloyd!\x02",
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
            "#00101FYou said Arios took\x01",
            "her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05926F#5PYes. He came alone,\x01",
            "wearing that white\x01",
            "uniform...\x02\x03",
            "#05921FHe said "I've come to\x01",
            "get you", and KeA nodded\x01",
            "to him...\x02",
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
            "#00305FYou mean that Keddo\x01",
            "followed him willingly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05923F#5PYes... That's how it looked to\x01",
            "me.\x02\x03",
            "#05921FI thought it was strange that\x01",
            "she didn't have your permission\x01",
            "so I tried to stop her, but...\x02\x03",
            "#05926FBut KeA told me "It's fine"...\x02\x03",
            "And, Zeit, who was agitated,\x01",
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
            "#12P#00208FNow that you mention\x01",
            "it... Zeit is nowhere to\x01",
            "be found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05926F#5PAfter those two left, he\x01",
            "wandered off.\x02\x03",
            "#05928FMaybe he followed\x01",
            "them...\x02",
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

    def lambda_1C5D0():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C5D0)
    Sleep(100)

    def lambda_1C5E0():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1C5E0)
    Sleep(100)

    def lambda_1C5F0():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1C5F0)
    Sleep(100)

    def lambda_1C600():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1C600)
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
            "promise to Shizuku?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05923F#5PI thought that too, but\x01",
            "it doesn't seem like\x01",
            "it...\x02\x03",
            "#05921FArios spoke as if they\x01",
            "were going to Michelam.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1C744():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C744)
    Sleep(50)

    def lambda_1C754():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1C754)
    Sleep(50)

    def lambda_1C764():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1C764)
    Sleep(50)

    def lambda_1C774():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1C774)
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
            "#05923F#5PYes, he said the boat\x01",
            "was ready...\x02\x03",
            "#05921FIn other words, they're\x01",
            "going to Michelam,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#00103F...Business has been completely\x01",
            "halted in the Michelam area for\x01",
            "the past few days.\x02\x03",
            "#00101FSo why there?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#00310FTch... I knew it. This\x01",
            "isn't normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FLet's follow them,\x01",
            "Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003FYeah... Let's try to get\x01",
            "ourselves a boat\x01",
            "somehow.\x02\x03",
            "#00007FCecil, thank you!\x01",
            "Anyhow, we'll try\x01",
            "chasing after them.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1C981():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1C981)
    Sleep(50)

    def lambda_1C991():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1C991)
    Sleep(50)

    def lambda_1C9A1():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1C9A1)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0xB,
        (
            "#05923F#5PAlright, be careful.\x02\x03",
            "#05928F...Both Arios and KeA had\x01",
            "unusually serious\x01",
            "expressions on their faces.\x02\x03",
            "#05921FI think there may be\x01",
            "something big going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00013FGot it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107FAnyway, we've got to\x01",
            "catch up with them and\x01",
            "ask what's going on!\x02",
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

    # Function_55_1C010 end

    def Function_56_1CAEC(): pass

    label("Function_56_1CAEC")


    def lambda_1CAF1():
        OP_97(0x101, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1CAF1)
    Sleep(200)

    def lambda_1CB0E():
        OP_97(0x102, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1CB0E)
    Sleep(200)

    def lambda_1CB2B():
        OP_97(0x103, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1CB2B)
    Sleep(200)

    def lambda_1CB48():
        OP_97(0x104, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1CB48)
    Return()

    # Function_56_1CAEC end

    def Function_57_1CB5E(): pass

    label("Function_57_1CB5E")

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

    def lambda_1CD1C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1CD1C)
    Sleep(400)

    def lambda_1CD30():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1CD30)
    Sleep(600)

    def lambda_1CD44():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1CD44)
    Sleep(400)

    def lambda_1CD58():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1CD58)
    Sleep(600)

    def lambda_1CD6C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_1CD6C)
    Sleep(400)

    def lambda_1CD80():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_1CD80)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_1CD96():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1CD96)
    WaitChrThread(0x102, 1)

    def lambda_1CDA7():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1CDA7)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 1)

    def lambda_1CDC0():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_1CDC0)
    WaitChrThread(0xF5, 1)

    def lambda_1CDD1():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_1CDD1)
    OP_6F(0x79)
    OP_68(2640, 1300, 3150, 2000)
    MoveCamera(55, 15, 0, 2000)
    SetCameraDistance(29000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#6P#00001F#30W...The Special Support\x01",
            "Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108F#30WWe're back... aren't we.\x02",
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
            "#20A#30W─Alright, then. Let's\x01",
            "start on the hot pot.\x02\x03",
            "#20A#30WKeA prepared it after all,\x01",
            "so there's plenty of meat,\x01",
            "fish and vegetables.\x02\x03",
            "#20A#30WEat a lot, go to bed\x01",
            "early... Let's prepare for\x01",
            "tomorrow!\x07\x00\x02",
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
            "#5P#00304F#30W...Haha. It's too\x01",
            "nostalgic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00208FRight...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D1FB")

    ChrTalk(
        0x109,
        (
            "#12P#10106FIt's hasn't even been a\x01",
            "month...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D1FB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D234")

    ChrTalk(
        0x105,
        "#12P#10404FHeh. It's really moving.\x02",
    )

    CloseMessageWindow()

    label("loc_1D234")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D2DC")

    ChrTalk(
        0x106,
        (
            "#12P#10708FHowever, it's not as\x01",
            "damaged as I thought it\x01",
            "would be...\x02\x03",
            "#10710FI thought would have\x01",
            "been searched thoroughly\x01",
            "by the State Guard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D36E")

    label("loc_1D2DC")


    ChrTalk(
        0x102,
        (
            "#5P#00104FHowever, it's not as\x01",
            "damaged as I thought it\x01",
            "would be...\x02\x03",
            "#00100FI thought would have\x01",
            "been searched thoroughly\x01",
            "by the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D36E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D4B7")

    ChrTalk(
        0x10A,
        (
            "#12P#00606FIt appears they're being\x01",
            "considerate towards that\x01",
            "kid.\x02\x03",
            "#00602FShe's extremely important\x01",
            "to the President's side.\x02\x03",
            "They probably didn't want\x01",
            "to offend her by ravaging a\x01",
            "place she holds very dear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000F...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00204FYou were too blunt,\x01",
            "but... I'm happy it\x01",
            "hasn't changed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D5E4")

    label("loc_1D4B7")


    ChrTalk(
        0x101,
        (
            "#6P#00004FPerhaps it was out of\x01",
            "consideration for KeA.\x02\x03",
            "#00000FShe's extremely important\x01",
            "to the President's side.\x02\x03",
            "They probably didn't want\x01",
            "to offend her by ravaging\x01",
            "a place she held dear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00305FSounds about right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00204FYou were too blunt,\x01",
            "but... I'm happy it\x01",
            "hasn't changed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D5E4")

    Sound(953, 0, 100, 0)
    Sleep(300)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    OP_90(0xC, 1500, 3000, 15000, 180)

    def lambda_1D612():
        OP_96(0xFE, 0x5DC, 0x0, 0x1838, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1D612)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1D6A1():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D6A1)
    Sleep(50)

    def lambda_1D6B1():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D6B1)
    Sleep(50)

    def lambda_1D6C1():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1D6C1)
    Sleep(50)

    def lambda_1D6D1():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D6D1)
    Sleep(50)

    def lambda_1D6E1():
        TurnDirection(0xF4, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1D6E1)
    Sleep(50)

    def lambda_1D6F1():
        TurnDirection(0xF5, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1D6F1)
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
        "#12P#00005FKoppe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FI see... You're safe.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 3, 0, 61)

    def lambda_1D7AD():
        OP_97(0x101, 0x0, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D7AD)
    Sleep(100)

    def lambda_1D7CA():
        OP_97(0x102, 0x0, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D7CA)
    Sleep(100)

    def lambda_1D7E7():
        OP_97(0x104, 0x0, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D7E7)
    Sleep(100)

    def lambda_1D804():
        OP_97(0xF4, 0xFFFFFDA8, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1D804)
    Sleep(100)

    def lambda_1D821():
        OP_97(0xF5, 0xFFFFFDA8, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1D821)
    WaitChrThread(0x104, 0)

    def lambda_1D83F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1D83F)
    WaitChrThread(0xF5, 0)
    WaitChrThread(0x103, 3)

    ChrTalk(
        0xC,
        (
            "#11PNyaago. [It's been a\x01",
            "while. How have you\x01",
            "been?]\x02",
        )
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
            "#00202FYes, yes... We'll be\x01",
            "away for a little while.\x02\x03",
            "#00204FWe'll be back again...\x01",
            "for sure.\x02",
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
            "#00206F#5PHe says he's been living\x01",
            "here since then...\x02\x03",
            "#00202FHe also seems to be\x01",
            "worried about us\x01",
            ""housemates".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FHaha, I see.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DA7C")

    ChrTalk(
        0x109,
        (
            "#12P#10102FSince we're here, should\x01",
            "we give him some cat\x01",
            "food?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB0D")

    label("loc_1DA7C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DAD1")

    ChrTalk(
        0x105,
        (
            "#12P#10402FSince we're here, should\x01",
            "we give him some food?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB0D")

    label("loc_1DAD1")


    ChrTalk(
        0x104,
        (
            "#00304FSince we're here, should\x01",
            "we give 'im some food?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB0D")

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

    # Function_57_1CB5E end

    def Function_58_1DBE8(): pass

    label("Function_58_1DBE8")


    def lambda_1DBED():
        OP_98(0xFE, 0x0, 0x0, 0x1324, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DBED)
    Sleep(200)

    def lambda_1DC0A():
        OP_98(0xFE, 0x0, 0x0, 0x1324, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1DC0A)
    Sleep(200)
    BeginChrThread(0x103, 0, 0, 59)
    Sleep(200)
    BeginChrThread(0x104, 0, 0, 60)
    Sleep(200)

    def lambda_1DC39():
        OP_98(0xFE, 0x0, 0x0, 0x13EC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1DC39)
    Sleep(200)

    def lambda_1DC56():
        OP_98(0xFE, 0x0, 0x0, 0x13EC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1DC56)
    Return()

    # Function_58_1DBE8 end

    def Function_59_1DC6C(): pass

    label("Function_59_1DC6C")


    def lambda_1DC71():
        OP_98(0xFE, 0x0, 0x0, 0x1194, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1DC71)
    WaitChrThread(0x103, 1)

    def lambda_1DC8F():
        OP_97(0xFE, 0x1F4, 0x0, 0x1F4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1DC8F)
    WaitChrThread(0x103, 1)
    Return()

    # Function_59_1DC6C end

    def Function_60_1DCA9(): pass

    label("Function_60_1DCA9")


    def lambda_1DCAE():
        OP_98(0xFE, 0x0, 0x0, 0x1194, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1DCAE)
    WaitChrThread(0x104, 1)

    def lambda_1DCCC():
        OP_97(0xFE, 0x1F4, 0x0, 0x1F4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1DCCC)
    WaitChrThread(0x104, 1)
    Return()

    # Function_60_1DCA9 end

    def Function_61_1DCE6(): pass

    label("Function_61_1DCE6")

    Sleep(200)

    def lambda_1DCEE():
        OP_95(0xFE, -400, 0, 4100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1DCEE)
    WaitChrThread(0x103, 1)

    def lambda_1DD0C():
        OP_95(0xFE, 300, 0, 6100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1DD0C)
    WaitChrThread(0x103, 1)
    TurnDirection(0x103, 0xC, 500)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    TurnDirection(0xC, 0x103, 500)
    Return()

    # Function_61_1DCE6 end

    def Function_62_1DD48(): pass

    label("Function_62_1DD48")

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

    # Function_62_1DD48 end

    def Function_63_1DE76(): pass

    label("Function_63_1DE76")

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
            "#00000FIt seems Chief Sergei's\x01",
            "old nickname was "Sergei\x01",
            "the Rear"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FIn that case, the chief's\x01",
            "chair is "where the rear\x01",
            "commander sits".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FLet's search nearby...\x02",
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
            "#00005F...There's something\x01",
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
        "#12P#00305FThis is... a trunk?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FIt looks like the one KeA\x01",
            "was in at that Black\x01",
            "Auction, too.\x02\x03",
            "#10304FHe chose this as the first\x01",
            "hiding place. Hehe, he must\x01",
            "be trying to provoke us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FI-Indeed. He even got\x01",
            "ahold of chief's\x01",
            "nickname.\x02\x03",
            "#00000FAnyhow, let's check it\x01",
            "out.\x02",
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
            "A card was affixed to\x01",
            "the back of the trunk.\x07\x00\x02",
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
            "The second cell is outside the\x01",
            "city. Find "the place the villagers\x01",
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
            "#00200FA Rosenberg antique\x01",
            "doll... No doubt about\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FYes. I've seen this one\x01",
            "before, too.\x02\x03",
            "#00104FI think Bell calls this\x01",
            "one "Canan" and loves it\x01",
            "dearly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FHaha, she even gives her dolls names.\x01",
            "Mariabell has a cute side, doesn't\x01",
            "she.\x02\x03",
            "#10106FHe went to all the trouble of putting\x01",
            "the dolls he stole in trunks. That's\x01",
            "a bit unexpected, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FPhantom Thief B... He could be\x01",
            "showing proper respect towards\x01",
            "the dolls as works of art.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FSo the next one is\x01",
            ""outside the city", huh.\x02\x03",
            "#10306FOh man. Our search\x01",
            "radius has gotten wider.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FThe important parts are "Old Road"\x01",
            "and "inherited by the villagers".\x02\x03",
            "#00103FEach of those parts sounds historic,\x01",
            "but is there really such a place in\x01",
            "Crossbell's modern cities?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FAnyhow, let's collect this\x01",
            "one and try searching for\x01",
            "the next one.\x02",
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

    # Function_63_1DE76 end

    def Function_64_1E84D(): pass

    label("Function_64_1E84D")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's first check the\x01",
            "support requests, then\x01",
            "decide our course of action.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 9350, 850, 10320, 89)
    EventEnd(0x4)
    Return()

    # Function_64_1E84D end

    def Function_65_1E8BC(): pass

    label("Function_65_1E8BC")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's first check the\x01",
            "support requests, then\x01",
            "decide our course of action.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 11000, 850, 11350, 180)
    EventEnd(0x4)
    Return()

    # Function_65_1E8BC end

    def Function_66_1E92B(): pass

    label("Function_66_1E92B")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's first check the\x01",
            "support requests, then\x01",
            "decide our course of action.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 17000, 850, 4000, 270)
    EventEnd(0x4)
    Return()

    # Function_66_1E92B end

    def Function_67_1E99A(): pass

    label("Function_67_1E99A")

    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E9C6")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1E9C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E9E3")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1E9E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EA00")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1EA00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EA1D")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1EA1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EA3A")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1EA3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EA57")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1EA57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EA74")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_1EA74")

    Return()

    # Function_67_1E99A end

    SaveToFile()

Try(main)
