from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t4100.bin",                # FileName
        "t4100",                    # MapName
        "t4100",                    # Location
        0x005D,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1F,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 93, 0, 2, 0, 3],
    )

    BuildStringList((
        "t4100",                  # 0
        "Mrs. Mucha",           # 1
        "Quint old man",           # 2
        "Sister · Lease",       # 3
        "A gentleman",             # 4
        "A gentleman",             # 5
        "Claris",               # 6
        "Nielsen",             # 7
        "Arios",               # 8
        "Flowers in front of the guy",           # 9
        "Arios家墓前の花",     # 10
        "Claudia Hime",         # 11
        "Assistant Julia",             # 12
    ))

    AddCharChip((
        "chr/ch20100.itc",                   # 00
        "chr/ch20000.itc",                   # 01
        "chr/ch14000.itc",                   # 02
        "chr/ch10400.itc",                   # 03
        "chr/ch41600.itc",                   # 04
        "apl/ch50423.itc",                   # 05
        "chr/ch02400.itc",                   # 06
        "chr/ch11000.itc",                   # 07
        "chr/ch11200.itc",                   # 08
        "chr/ch45100.itc",                   # 09
        "chr/ch11500.itc",                   # 0A
    ))

    DeclNpc(8579,    2000,    25379,   0,    257,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294958427, 0,       11800,   0,    385,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294965606, 0,       10510,   180,  389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(1720,    0,       10880,   180,  389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4294959697, 2000,    25329,   0,    389,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294960827, 0,       12180,   135,  389,  0x0, 0,   9,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(20829,   0,       32299,   0,    389,  0x0, 0,   6,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(4294944296, 0,       25500,   0,    502,  0x0, 0,   5,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(20600,   0,       34000,   0,    502,  0x0, 0,   5,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(349,     4000,    42569,   0,    449,  0x0, 0,   7,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(2230,    4000,    42750,   180,  449,  0x0, 0,   8,   0,   0,   0,   255, 255, 255,  0)

    DeclEvent(0x0000, 0, 22,  -1.0,                  24.0,                  0.0,                   1764.0,                [0.0357142873108387,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.0357142873108387,    -8.0,                  -0.0,                  1.0])

    DeclActor(190,     4200,    45040,   1200,    190,     5700,    45040,   0x007C, 0,  13, 0x0000)
    DeclActor(4294944246, 0,       25770,   1200,    4294944676, 1500,    25860,   0x007C, 0,  15, 0x0000)
    DeclActor(20570,   0,       34830,   1500,    20570,   1500,    34830,   0x007C, 0,  18, 0x0000)
    DeclActor(12080,   4000,    37650,   1500,    12080,   5500,    37650,   0x007C, 0,  20, 0x0000)
    DeclActor(4294959276, 2000,    26550,   1500,    4294959276, 3500,    26550,   0x007C, 0,  14, 0x0000)

    ChipFrameInfo(924, 0)                                        # 0

    ScpFunction((
        "Function_0_39C",          # 00, 0
        "Function_1_44C",          # 01, 1
        "Function_2_8A9",          # 02, 2
        "Function_3_B2E",          # 03, 3
        "Function_4_CA7",          # 04, 4
        "Function_5_1B8C",         # 05, 5
        "Function_6_1F20",         # 06, 6
        "Function_7_2E69",         # 07, 7
        "Function_8_38BE",         # 08, 8
        "Function_9_3E6E",         # 09, 9
        "Function_10_3FA2",        # 0A, 10
        "Function_11_407F",        # 0B, 11
        "Function_12_4565",        # 0C, 12
        "Function_13_45C7",        # 0D, 13
        "Function_14_469C",        # 0E, 14
        "Function_15_490D",        # 0F, 15
        "Function_16_5057",        # 10, 16
        "Function_17_5504",        # 11, 17
        "Function_18_5C6C",        # 12, 18
        "Function_19_5DA3",        # 13, 19
        "Function_20_60E1",        # 14, 20
        "Function_21_640A",        # 15, 21
        "Function_22_6B0C",        # 16, 22
        "Function_23_7E84",        # 17, 23
        "Function_24_7EAD",        # 18, 24
        "Function_25_7EB1",        # 19, 25
        "Function_26_8A8D",        # 1A, 26
        "Function_27_8E86",        # 1B, 27
        "Function_28_93A2",        # 1C, 28
        "Function_29_960D",        # 1D, 29
    ))


    def Function_0_39C(): pass

    label("Function_0_39C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3D4"),
        (1, "loc_3E0"),
        (2, "loc_3EC"),
        (3, "loc_3F8"),
        (4, "loc_404"),
        (5, "loc_410"),
        (6, "loc_41C"),
        (SWITCH_DEFAULT, "loc_434"),
    )


    label("loc_3D4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_434")

    label("loc_3E0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_434")

    label("loc_3EC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_434")

    label("loc_3F8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_434")

    label("loc_404")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_434")

    label("loc_410")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_434")

    label("loc_41C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_434")

    label("loc_434")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_434")

    label("loc_44B")

    Return()

    # Function_0_39C end

    def Function_1_44C(): pass

    label("Function_1_44C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8A8")
    OP_95(0xFE, -8870, 0, 11800, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -16950, 0, 11340, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -19140, 0, 11340, 2000, 0x0)
    OP_95(0xFE, -19140, 0, 16070, 2000, 0x0)
    OP_95(0xFE, -21040, 0, 16090, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -16960, 0, 16090, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -1200, 0, 16090, 2000, 0x0)
    OP_95(0xFE, -1200, 2000, 25270, 2000, 0x0)
    OP_95(0xFE, -10990, 2000, 25270, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -4930, 2000, 25270, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -1200, 2000, 25270, 2000, 0x0)
    OP_95(0xFE, -1200, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, -8460, 4000, 35990, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -170, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, -50, 4200, 43970, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, -170, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, 12000, 4000, 35990, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 4970, 4000, 36140, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 1310, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, 1310, 0, 8039, 2000, 0x0)
    OP_95(0xFE, 15920, 0, 8039, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, 22720, 0, 8039, 2000, 0x0)
    OP_95(0xFE, 22720, 0, 13250, 2000, 0x0)
    OP_95(0xFE, 20500, 0, 13250, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 11500, 0, 13250, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 9240, 0, 13250, 2000, 0x0)
    OP_95(0xFE, 9240, 0, 16390, 2000, 0x0)
    OP_95(0xFE, 15980, 0, 19640, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, 23050, 0, 19550, 2000, 0x0)
    OP_95(0xFE, 23050, 0, 25610, 2000, 0x0)
    OP_95(0xFE, 21270, 0, 25620, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, 27500, 0, 25610, 2000, 0x0)
    OP_95(0xFE, 27500, 0, 31330, 2000, 0x0)
    OP_95(0xFE, 20470, 0, 33170, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x6A, 0x190)
    Sleep(100)
    OP_95(0xFE, 27500, 0, 31330, 2000, 0x0)
    OP_95(0xFE, 27500, 0, 25610, 2000, 0x0)
    OP_95(0xFE, 23050, 0, 19550, 2000, 0x0)
    OP_95(0xFE, 23050, 0, 6410, 2000, 0x0)
    OP_95(0xFE, 30, 0, 6690, 2000, 0x0)
    Jump("Function_1_44C")

    label("loc_8A8")

    Return()

    # Function_1_44C end

    def Function_2_8A9(): pass

    label("Function_2_8A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DC")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -22960, 0, 24620, 0)

    label("loc_8DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8F5")
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_B2D")

    label("loc_8F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_924")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 12160, 4000, 36150, 0)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_B2D")

    label("loc_924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_963")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_95E")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -22960, 0, 24620, 0)

    label("loc_95E")

    Jump("loc_B2D")

    label("loc_963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_980")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_985")

    label("loc_980")

    ClearChrFlags(0x11, 0x80)

    label("loc_985")

    ClearChrFlags(0x10, 0x80)
    SetScenarioFlags(0x0, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_99B")
    SetChrFlags(0x8, 0x10)

    label("loc_99B")

    Jump("loc_B2D")

    label("loc_9A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9C4")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 350, 4000, 42570, 0)
    Jump("loc_B2D")

    label("loc_9C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9D7")
    SetChrFlags(0x8, 0x80)
    Jump("loc_B2D")

    label("loc_9D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_A00")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 350, 4000, 42570, 0)
    SetChrFlags(0x8, 0x10)
    Jump("loc_B2D")

    label("loc_A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A24")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 350, 4000, 42570, 0)
    Jump("loc_B2D")

    label("loc_A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_A32")
    Jump("loc_B2D")

    label("loc_A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_A4B")
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_B2D")

    label("loc_A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A64")
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_B2D")

    label("loc_A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8B")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)

    label("loc_A8B")

    Jump("loc_B2D")

    label("loc_A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_AA3")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_B2D")

    label("loc_AA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_ABC")
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_B2D")

    label("loc_ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_ACF")
    SetChrFlags(0x8, 0x80)
    Jump("loc_B2D")

    label("loc_ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_AFB")
    SetChrChipByIndex(0xA, 0xA)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 350, 4000, 42570, 0)
    Jump("loc_B2D")

    label("loc_AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_B14")
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_B2D")

    label("loc_B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B2D")
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrFlags(0x8, 0x10)

    label("loc_B2D")

    Return()

    # Function_2_8A9 end

    def Function_3_B2E(): pass

    label("Function_3_B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BB2")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x0, 0x168, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_BC9")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_BC9")

    label("loc_BC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BF5")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x14, 0x190, 0x0)
    Jump("loc_C1C")

    label("loc_BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C1C")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x14, 0x190, 0x0)

    label("loc_C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C2E")
    OP_65(0x4, 0x1)

    label("loc_C2E")

    SoundDistance(0x84, 0xFFFFD878, 0xFA0, 0xDEA8, 0x2710, 0x186A0, 0x64, 0x0)
    OP_E3(0x6C2, 0xFA0, 0xDEA8)
    OP_E3(0x4F60, 0xFA0, 0xDEA8)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C81")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_C81")

    OP_66(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA6")
    OP_65(0x1, 0x1)

    label("loc_CA6")

    Return()

    # Function_3_B2E end

    def Function_4_CA7(): pass

    label("Function_4_CA7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD0")

    ChrTalk(
        0xFE,
        "A police officer came to check the situation earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No doubt, that Ian was in such a big way ……\x01",
            "I can not believe it though it is not very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F…… Yeah, we have the same feeling.\x02\x03",
            "#00003F(…, but it is true.\x01",
            "Ask your teacher yourself for real intention\x01",
            "I guess there is only one thing to see … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_E4D")

    label("loc_DD0")


    ChrTalk(
        0xFE,
        (
            "Ian dressed,\x01",
            "What was such a big deal ……\x01",
            "I can not believe it is not very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What on earth is he\x01",
            "Does that make it so …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4D")

    Jump("loc_1B88")

    label("loc_E52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1499")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1423")

    ChrTalk(
        0xFE,
        (
            "If I think that the barrier disappeared,\x01",
            "Outrageous thing\x01",
            "It happens to happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since that independence declaration,\x01",
            "The number of people who came to visit the grave decreased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this situation you can do whatever you want,\x01",
            "It is about cleaning the grave.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_141E")
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)

    ChrTalk(
        0x101,
        (
            "#00003F……that.\x02\x03",
            "#00008FThis tomb is united,\x01",
            "Who is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "What did not you know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Hmm, if anyhow\x01",
            "There is no particular problem.\x01",
            "He seems to be close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105Feh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FAre we a acquaintance?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The surname of those sleeping here\x01",
            "\"Grim wood\" …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That is, Ian Grimwood's\x01",
            "It's your family.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#00205FMr. Ian's …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FWell, that's right ……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… That is something we can not afford.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "About 15 years ago, in an unfortunate accident\x01",
            "My wife and my two children's life\x01",
            "You are lost …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Always came to visit a grave every weekend\x01",
            "I remembered my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The tombstone was hurt by the wind and rain … …\x01",
            "It seems that he is doing a wish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do not dare to repair until it is done\x01",
            "You are asked to take care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00308FShe seems to have various teachers … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since he declared that independence, is he also busy?\x01",
            "I have not readily visited … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you do not mind, from now on\x01",
            "You ought to go see yours.\x01",
            "…… Let's miss them too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F………………………………\x02\x03",
            "#00000F……Yes, I understand.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 4)

    label("loc_141E")

    Jump("loc_1494")

    label("loc_1423")


    ChrTalk(
        0xFE,
        (
            "In this situation you can do whatever you want,\x01",
            "It is about cleaning the grave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… You should be careful with your own nirvana.\x02",
    )

    CloseMessageWindow()

    label("loc_1494")

    Jump("loc_1B88")

    label("loc_1499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_14A7")
    Jump("loc_1B88")

    label("loc_14A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_1674")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15DC")

    ChrTalk(
        0xFE,
        "Ian was in the church a while ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ガイやAriosの妻の墓を\x01",
            "You seemed to have visited them.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0x101,
        "#00005FEr … What did you do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…, no, what.\x01",
            "It is not a big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I seem to have been busy lately,\x01",
            "I wish I had a good change.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_166F")

    label("loc_15DC")


    ChrTalk(
        0xFE,
        (
            "Ian recently\x01",
            "ガイやAriosの妻の墓を\x01",
            "You seemed to have visited them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I seem to have been busy lately,\x01",
            "I wish I had a good change.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_166F")

    Jump("loc_1B88")

    label("loc_1674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_17D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1753")

    ChrTalk(
        0xFE,
        (
            "As the mayor says,\x01",
            "Crossbell has national independence\x01",
            "It may be necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, the Empire and the Republic\x01",
            "I will put pressure on … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the future generation of young people,\x01",
            "What I want you to do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17CD")

    label("loc_1753")


    ChrTalk(
        0xFE,
        (
            "Crossbell has national independence\x01",
            "It may be necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the future generation of young people,\x01",
            "What I want you to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17CD")

    Jump("loc_1B88")

    label("loc_17D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_17E0")
    Jump("loc_1B88")

    label("loc_17E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_17EE")
    Jump("loc_1B88")

    label("loc_17EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1963")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D5")

    ChrTalk(
        0xFE,
        (
            "I always came to visit the grave\x01",
            "That wife, husband in conflict\x01",
            "I heard that he died.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… The times are a while ago,\x01",
            "I am also losing my family due to conflict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is similar circumstances,\x01",
            "It really cares.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_195E")

    label("loc_18D5")


    ChrTalk(
        0xFE,
        (
            "That wife, husband in conflict\x01",
            "I heard that he died.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, her family is foreign\x01",
            "He seems to live well.\x01",
            "…… That's salvation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_195E")

    Jump("loc_1B88")

    label("loc_1963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1971")
    Jump("loc_1B88")

    label("loc_1971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_197F")
    Jump("loc_1B88")

    label("loc_197F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_1AE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199A")
    Call(0, 5)
    Jump("loc_1ADB")

    label("loc_199A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A5B")

    ChrTalk(
        0xFE,
        (
            "Guy often goes to a cottage there\x01",
            "I'm coming to drinking alcohol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, until the day breaks\x01",
            "I bought a sake for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, he is quite a liquor.\x01",
            "I do not know how many times I got sick drunk.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1ADB")

    label("loc_1A5B")


    ChrTalk(
        0xFE,
        (
            "Guy guys are quite a liquor.\x01",
            "I do not know how many times I got sick drunk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… I could not beat him,\x01",
            "It is one relief.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ADB")

    Jump("loc_1B88")

    label("loc_1AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1B88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AFB")
    Call(0, 5)
    Jump("loc_1B88")

    label("loc_1AFB")


    ChrTalk(
        0xFE,
        (
            "Usually, I am\x01",
            "I manage the graveyard.\x01",
            "I will come whenever I feel well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's right, if I remember it at that time\x01",
            "I will do it even in the old tale of Guy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B88")

    TalkEnd(0xFE)
    Return()

    # Function_4_CA7 end

    def Function_5_1B8C(): pass

    label("Function_5_1B8C")

    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0x101, 0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "Oh, you are Lloyd ……\x01",
            "Long time no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "When did you come back?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, it is the last time.\x01",
            "I was out of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FMr. Lloyd, who is this …?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1C9A")

    ChrTalk(
        0x102,
        (
            "#00100FHuhuu, there was a request before\x01",
            "You got to know each other.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C9A")


    ChrTalk(
        0x101,
        (
            "#00000FAh……\x01",
            "I was drinking partner with my big brother.\x01",
            "Mr. Quinto.\x02\x03",
            "#00004FHe was doing well for my brother.\x01",
            "Even when we drank together after a cult incident\x01",
            "He tells us stories about various stories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I was having fun at that time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, Lloyd does not drink as much as Guy\x01",
            "It was a bit boring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FHaha … I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHuhuu, that time we also\x01",
            "I asked him to be present.\x02\x03",
            "#00109FMinor Tio-chan\x01",
            "I seemed dissatisfied with just juice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, I see.\x02\x03",
            "#10304FWell, from now on we both\x01",
            "Regards, old man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Well, Lloyd's colleagues are welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "普段、わしはI manage the graveyard.\x01",
            "I will come whenever I feel well.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x135, 4)
    Return()

    # Function_5_1B8C end

    def Function_6_1F20(): pass

    label("Function_6_1F20")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_20AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_202F")

    ChrTalk(
        0xFE,
        (
            "It is said that monsters get out of town\x01",
            "Beyond that scary event,\x01",
            "Finally I came to visit the grave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was uneasy and uneasy,\x01",
            "Thinking about this dead man\x01",
            "Courage has come about … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guarded me for sure.\x01",
            "Thank you, you …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20A5")

    label("loc_202F")


    ChrTalk(
        0xFE,
        (
            "Thinking about this dead man\x01",
            "Courage came … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what may happen, it's okay.\x01",
            "Because I will not lose … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A5")

    Jump("loc_2E65")

    label("loc_20AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_20B8")
    Jump("loc_2E65")

    label("loc_20B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_221C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218F")

    ChrTalk(
        0xFE,
        (
            "I was in Remyferia this morning.\x01",
            "My son and couple were worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Leave me alone,\x01",
            "Those who were in a safe place\x01",
            "Will it be nice … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, but ….\x01",
            "I wonder why I am very happy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2217")

    label("loc_218F")


    ChrTalk(
        0xFE,
        (
            "I was in Remyferia this morning.\x01",
            "My son and couple were worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want you to stay safe, but …\x01",
            "I wonder why I am very happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2217")

    Jump("loc_2E65")

    label("loc_221C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_237C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22EE")

    ChrTalk(
        0xFE,
        (
            "The other day 's raid incident,\x01",
            "I was terribly frightened … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Disputes 30 years ago when I lost my husband\x01",
            "I remembered it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Never again, such a thought\x01",
            "I did not want to do … …\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)
    SetChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_2377")

    label("loc_22EE")


    ChrTalk(
        0xFE,
        (
            "In the recent raid incident,\x01",
            "Disputes 30 years ago when I lost my husband\x01",
            "I remembered it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Never again, such a thought\x01",
            "I did not want to do … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2377")

    Jump("loc_2E65")

    label("loc_237C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_23E8")

    ChrTalk(
        0xFE,
        (
            "No way, this kind of incident\x01",
            "I wake up …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like an era of conflict.\x01",
            "It's horrible …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E65")

    label("loc_23E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_23F6")
    Jump("loc_2E65")

    label("loc_23F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_24B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2494")

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F(He seems to be eagerly praying … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(I do not want to disturb you,\x01",
            "Let's go. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24B2")

    label("loc_2494")


    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_24B2")

    Jump("loc_2E65")

    label("loc_24B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_25F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2582")

    ChrTalk(
        0xFE,
        (
            "Recently, strange objects in various places\x01",
            "It seems they have been witnessed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even in the city,\x01",
            "I try not to go out into the highway\x01",
            "It seems there was a call.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cemetery near the city\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25F2")

    label("loc_2582")


    ChrTalk(
        0xFE,
        (
            "Outside of the city, even to the cathedral\x01",
            "It will not be so dangerous … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cemetery near the city\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25F2")

    Jump("loc_2E65")

    label("loc_25F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_268E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2658")

    ChrTalk(
        0xFE,
        "Beautiful sunset …\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x1F4)

    ChrTalk(
        0xFE,
        (
            "Huhu, you.\x01",
            "I will come again tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2689")

    label("loc_2658")


    ChrTalk(
        0xFE,
        (
            "It's already evening ….\x01",
            "I have to go home soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2689")

    Jump("loc_2E65")

    label("loc_268E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_282B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27BA")

    ChrTalk(
        0xFE,
        (
            "Recently, as a small hobby\x01",
            "Like to read before going to bed\x01",
            "I was getting ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "During this time, when you buy a new book\x01",
            "I have chosen two books of the same book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you wish\x01",
            "Can you get one?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝７卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝７卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 6)
    Jump("loc_2826")

    label("loc_27BA")


    ChrTalk(
        0xFE,
        (
            "Recently, recommended by my son and couple\x01",
            "I decided to have a hobby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, after all life\x01",
            "You must have fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2826")

    Jump("loc_2E65")

    label("loc_282B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_29D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2943")

    ChrTalk(
        0xFE,
        (
            "I am in Remiferia during this time\x01",
            "A letter has arrived from my son and couple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To me who is alone in the crossbell\x01",
            "Would you like to come to Remiferia?\x01",
            "He invited me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But after all, crossbell\x01",
            "I can not get away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is where I and the dead master\x01",
            "Because it is a place full of important memories.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_29CC")

    label("loc_2943")


    ChrTalk(
        0xFE,
        (
            "I was delighted with the invitation ….\x01",
            "I will crossbell\x01",
            "I do not mean to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is where I and the dead master\x01",
            "Because it is a place full of important memories.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29CC")

    Jump("loc_2E65")

    label("loc_29D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A6C")

    ChrTalk(
        0xFE,
        (
            "Claudia Himeって、\x01",
            "It seems to be very kind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Queen Alicia of Libert also\x01",
            "I have seen it in the photo ….\x01",
            "After all the atmosphere is similar.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E65")

    label("loc_2A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2AF8")

    ChrTalk(
        0xFE,
        (
            "A new era of crossbells\x01",
            "Symbolic building, Orchis Tower ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, if you can, with your husband\x01",
            "I wanted to go see the unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E65")

    label("loc_2AF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD4")

    ChrTalk(
        0xFE,
        (
            "At the trade meeting, the empire and the republic\x01",
            "The leaders seem to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Compared with when only conflict occurred,\x01",
            "I feel the times have changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on discussion, not military force,\x01",
            "I want you to make a good time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2C19")

    label("loc_2BD4")


    ChrTalk(
        0xFE,
        (
            "From now on discussion, not military force,\x01",
            "I want you to make a good time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C19")

    Jump("loc_2E65")

    label("loc_2C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2C2C")
    Jump("loc_2E65")

    label("loc_2C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_2CF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CAD")

    ChrTalk(
        0xFE,
        (
            "That person …\x01",
            "I wonder if it is a new sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heh he … is in Remiferia\x01",
            "She seems to be about a granddaughter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2CF4")

    label("loc_2CAD")


    ChrTalk(
        0xFE,
        (
            "There is a granddaughter at Remiferia.\x01",
            "I wonder that year old is that Sister ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CF4")

    Jump("loc_2E65")

    label("loc_2CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_2D59")

    ChrTalk(
        0xFE,
        (
            "Oh……\x01",
            "The sun has set.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will soon,\x01",
            "Let's suppose to go home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E65")

    label("loc_2D59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2E65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E11")

    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "Oh, sorry.\x01",
            "I did not notice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Pray for the master's tomb\x01",
            "Because it is something I dedicated … ….\x01",
            "Please forgive me.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x0)
    SetScenarioFlags(0x0, 0)
    Jump("loc_2E65")

    label("loc_2E11")


    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F(… … It's wrong to get in the way.\x01",
            "let's go. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E65")

    TalkEnd(0xFE)
    Return()

    # Function_6_1F20 end

    def Function_7_2E69(): pass

    label("Function_7_2E69")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2E7A")
    Jump("loc_38BA")

    label("loc_2E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2E88")
    Jump("loc_38BA")

    label("loc_2E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_31A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_310C")

    ChrTalk(
        0xA,
        (
            "#04401FIn the direction of the mountain road hunters\x01",
            "It seems to be developing.\x02\x03",
            "#04403F…… As a \"star cup knight\"\x01",
            "I will show outstanding behavior\x01",
            "I can not take it.\x02\x03",
            "#04408FAt this difficult time\x01",
            "I can not help you,\x01",
            "It is very painful but …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2FB3")

    ChrTalk(
        0x103,
        (
            "#00200FBy the way, Mr. Lease\x01",
            "I have had a lot of arms.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FB3")


    ChrTalk(
        0x102,
        (
            "#00108FCertainly the power of the \"star cup knight\"\x01",
            "I am reassuring if I can borrow it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301FWell, what is in the mountain path\x01",
            "It will be a pretty awkward opponent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FMr. Lease,\x01",
            "Even for a moment's time\x01",
            "Please wait here.\x02\x03",
            "#00001FWe do not care about Mainz\x01",
            "I'll do it with a guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04401F……I understand.\x01",
            "Please be careful enough for everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_319F")

    label("loc_310C")


    ChrTalk(
        0xA,
        (
            "#04401FIn the direction of the mountain road hunters\x01",
            "It seems to be developing.\x02\x03",
            "#04403FOn the standpoint of \"Star Cup Knight\"\x01",
            "I can not help but …\x01",
            "Please take care.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_319F")

    Jump("loc_38BA")

    label("loc_31A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_31B2")
    Jump("loc_38BA")

    label("loc_31B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3278")

    ChrTalk(
        0xA,
        (
            "#04400FRegarding \"Pleroma grass\"\x01",
            "We will contact you as soon as we contact the Order\x01",
            "I will start the survey even here.\x02\x03",
            "#04403FHow far by me alone\x01",
            "I do not know if it can be determined ……\x01",
            "I will report as soon as I know something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BA")

    label("loc_3278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_35B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3548")

    ChrTalk(
        0xA,
        "#04400FEveryone……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMr. Lease ……\x01",
            "You were here.\x02\x03",
            "#00004FYesterday, valuable information\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04404FNo wonder if I could serve you.\x02\x03",
            "#04400FEveryone, which way are you going to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FWell, actually …\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ellie explained that going to the doll workshop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#04405FRosenberg Studio ……\x02\x03",
            "#04403FIt certainly has something to do with \"association\"\x01",
            "It is a place that is being touched.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FWell, as expected\x01",
            "Is it such as the Star Cup knight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04403F…… Jorg Rosenberg\x01",
            "I have heard of the person who was able to say … …\x02\x03",
            "#04401FStill a connection with \"association\"\x01",
            "There is something different.\x02\x03",
            "If you're planning to meet,\x01",
            "You should be careful enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah … that's what I meant.\x01",
            "Thank you for your advice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16D, 2)
    Jump("loc_35B1")

    label("loc_3548")


    ChrTalk(
        0xA,
        (
            "#04400FIf you go to the puppet factory,\x01",
            "You should prepare thoroughly.\x02\x03",
            "#04403F… … Please be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35B1")

    Jump("loc_38BA")

    label("loc_35B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_35C4")
    Jump("loc_38BA")

    label("loc_35C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_35D2")
    Jump("loc_38BA")

    label("loc_35D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_35E0")
    Jump("loc_38BA")

    label("loc_35E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_35EE")
    Jump("loc_38BA")

    label("loc_35EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_35FC")
    Jump("loc_38BA")

    label("loc_35FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_360A")
    Jump("loc_38BA")

    label("loc_360A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3618")
    Jump("loc_38BA")

    label("loc_3618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_38A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3637")
    TalkEnd(0xFE)
    Call(0, 8)
    Return()

    label("loc_3637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3820")

    ChrTalk(
        0xA,
        (
            "#13800FAfter finishing visiting the memorial monuments,\x01",
            "Later on to seniors the contents of work\x01",
            "I have to go check him.\x02\x03",
            "#13804FVariety in taking office\x01",
            "There seems to be a lot of things to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FAh … what?\x01",
            "Did it disturb you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#13800FNo, such a thing ……\x01",
            "I also met Kaoru.\x02\x03",
            "#13803F… More than that,\x01",
            "Somehow stomach\x01",
            "I'm fleeing.\x02\x03",
            "#13802FReturning to the dormitory as soon as possible,\x01",
            "Bread you bought at bakery\x01",
            "I want to eat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F(Hehe, I'm gluttonous\x01",
            "It looks as usual. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_389E")

    label("loc_3820")


    ChrTalk(
        0xA,
        (
            "#13800FFor a while,\x01",
            "At this Crossbell Cathedral\x01",
            "I think that it will be indebted.\x02\x03",
            "If there is something,\x01",
            "Please come and see me anytime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_389E")

    Jump("loc_38BA")

    label("loc_38A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_38B1")
    Jump("loc_38BA")

    label("loc_38B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_38BA")

    label("loc_38BA")

    TalkEnd(0xFE)
    Return()

    # Function_7_2E69 end

    def Function_8_38BE(): pass

    label("Function_8_38BE")

    EventBegin(0x0)
    Fade(500)
    OP_68(540, 5500, 39970, 0)
    MoveCamera(316, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14580, 0)
    SetChrPos(0x101, 0, 4000, 40000, 0)
    SetChrPos(0x102, -1600, 4000, 40700, 0)
    SetChrPos(0x109, -800, 4000, 39100, 0)
    SetChrPos(0x105, 1300, 4000, 39000, 0)
    SetChrPos(0x153, 1450, 4000, 40510, 0)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x101, 0xA, 0)
    TurnDirection(0x102, 0xA, 0)
    TurnDirection(0x109, 0xA, 0)
    TurnDirection(0x105, 0xA, 0)
    TurnDirection(0x153, 0xA, 0)
    OP_0D()
    Sleep(100)
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        (
            "#11P#13800FOh, everyone ……\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FMr. Lease, the greetings of his appointment\x01",
            "It looks like it was over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#13804FWell, it ended without any problems.\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x153, 500)

    ChrTalk(
        0xA,
        (
            "#11P#13800F…… That child was talking about a while ago,\x01",
            "Son of a acquaintance ……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYeah, this is Keia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01105Folder sister,\x01",
            "Maybe a new sister ~?\x02\x03",
            "#01109FHello, hello!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        "#11P#13802F……cute……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHehe, is that so?\x01",
            "Besides, it is very\x01",
            "He is a good boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00009FHelp me often with meals\x01",
            "I will do it … ….\x01",
            "I am saved very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10306FWhew, even this\x01",
            "Parental behavior is demonstrated?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FHaha ……\x01",
            "I understand your feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#01111FBarking?\x02",
    )

    CloseMessageWindow()

    def lambda_3C53():
        TurnDirection(0x101, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3C53)
    Sleep(50)

    def lambda_3C63():
        TurnDirection(0x105, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3C63)
    Sleep(50)

    def lambda_3C73():
        TurnDirection(0x102, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3C73)
    Sleep(50)

    def lambda_3C83():
        TurnDirection(0x109, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3C83)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x109, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#11P#13803F(…… I see, this girl\x01",
            "Examples of the cult … …)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D3F():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3D3F)
    Sleep(50)

    def lambda_3D4F():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3D4F)
    Sleep(50)

    def lambda_3D5F():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3D5F)
    Sleep(50)

    def lambda_3D6F():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3D6F)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        (
            "#00105FWell, Mr. Lease.\x01",
            "What's up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#13803F…… No, nothing.\x02\x03",
            "#13802FMr. Kea,\x01",
            "I hope to see you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#01109FOh, thanks!\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x135, 5)
    SetChrPos(0x0, 0, 4000, 40000, 180)
    EventEnd(0x5)
    Return()

    # Function_8_38BE end

    def Function_9_3E6E(): pass

    label("Function_9_3E6E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F3F")

    ChrTalk(
        0xFE,
        (
            "Oh, you are …\x01",
            "I was visiting Arseille last night.\x01",
            "Everyone in the mission support department?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Claudia Hime殿下とAssistant Juliaが\x01",
            "I will come to this destination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like, please.\x01",
            "Please do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F9E")

    label("loc_3F3F")


    ChrTalk(
        0xFE,
        (
            "Claudia Hime殿下とAssistant Juliaが\x01",
            "I will come to this destination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "どうぞ、Please do.\x02",
    )

    CloseMessageWindow()

    label("loc_3F9E")

    TalkEnd(0xFE)
    Return()

    # Function_9_3E6E end

    def Function_10_3FA2(): pass

    label("Function_10_3FA2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4032")

    ChrTalk(
        0xFE,
        (
            "As expected, in the cemetery\x01",
            "He is trying to make a noise\x01",
            "I do not think so … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are things that can happen by any chance.\x01",
            "I have to be vigilant.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_407B")

    label("loc_4032")


    ChrTalk(
        0xFE,
        (
            "Minimum security required ……\x01",
            "Responsibility is serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have to be vigilant.\x02",
    )

    CloseMessageWindow()

    label("loc_407B")

    TalkEnd(0xFE)
    Return()

    # Function_10_3FA2 end

    def Function_11_407F(): pass

    label("Function_11_407F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44F5")

    ChrTalk(
        0xFE,
        (
            "…… Oh, you guys.\x01",
            "It's strange in such a place.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42FD")

    ChrTalk(
        0x101,
        (
            "#00003FYou seem to have been visiting.\x01",
            "……Excuse me.\x02\x03",
            "#00000FDid you mean …\x01",
            "What are you asleep at here …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FOzma · seeker second l …\x01",
            "He died about ten years ago,\x01",
            "It is my father and father.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41BD")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_41BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41E0")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_41E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4203")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_4203")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4223")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_4223")

    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105FNoel's father ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FI have heard only the story …\x01",
            "I heard he was a pretty good officer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FOh, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, I feel strong justice\x01",
            "It was a strict person … ….\x01",
            "In the accident during the mission.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43B8")

    label("loc_42FD")


    ChrTalk(
        0x101,
        (
            "#00003FYou seem to have been visiting.\x01",
            "……Excuse me.\x02\x03",
            "#00008F…… Certainly,\x01",
            "What are you sleeping here … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F…… Yeah,\x01",
            "He died about ten years ago\x01",
            "It is my father and father.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43B8")


    ChrTalk(
        0xFE,
        (
            "…… Because it is a job called security guards,\x01",
            "I was only prepared for it … …\x01",
            "After all I could not resist that time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, it's an old story\x01",
            "Such a soul\x01",
            "Do not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… But you also\x01",
            "You must take care of your life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you are gone,\x01",
            "Because there are many people who grieve.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10104F… Yeah, I know.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 3)
    Jump("loc_4561")

    label("loc_44F5")


    ChrTalk(
        0xFE,
        (
            "You too\x01",
            "You must take care of your life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you are gone,\x01",
            "Because there are many people who grieve.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4561")

    TalkEnd(0xFE)
    Return()

    # Function_11_407F end

    def Function_12_4565(): pass

    label("Function_12_4565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45C0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_458E")
    Call(0, 26)
    Return()

    label("loc_458E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_45A5")
    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Jump("loc_45BB")

    label("loc_45A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 6)), scpexpr(EXPR_END)), "loc_45B7")
    Call(0, 29)
    Return()

    label("loc_45B7")

    Call(0, 27)
    Return()

    label("loc_45BB")

    Jump("loc_45C6")

    label("loc_45C0")

    TalkBegin(0xFE)
    TalkEnd(0xFE)

    label("loc_45C6")

    Return()

    # Function_12_4565 end

    def Function_13_45C7(): pass

    label("Function_13_45C7")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "Born from under the bells and lambs\x01",
            "Please sleep peacefully\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "The golden sunlight that pulls from the pure white clouds\x01",
            "Become a path that leads to the blue blue sky\x01",
            "Do not lead the soul to the goddess\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_45C7 end

    def Function_14_469C(): pass

    label("Function_14_469C")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "Ozzma · Seeker\x01",
            "I sleep here\x01",
            "─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─\x01",
            "S1157 to S1194\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4909")

    ChrTalk(
        0x101,
        (
            "#00005FWhat is \"seeker\" …?\x01",
            "Did you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FOzma · seeker second l …\x01",
            "He died about ten years ago,\x01",
            "It is my father and father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FNoel's father ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FWell, I hear it for the first time … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FHaha, I too much\x01",
            "Things like this from myself\x01",
            "Because it is a type not to talk.\x02\x03",
            "#10104F…… Ladies and gentlemen, let's go.\x01",
            "Stopping at such a place\x01",
            "My father seems to be scolded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIs that so?\x01",
            "Let's say we'll go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 2)

    label("loc_4909")

    TalkEnd(0xFF)
    Return()

    # Function_14_469C end

    def Function_15_490D(): pass

    label("Function_15_490D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "Guy Bannings\x01",
            "I sleep here\x01",
            "─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─\x01",
            "S 1176 to S 1201\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A83")

    ChrTalk(
        0x153,
        (
            "#01105F(… … the person in this grave … …)\x02\x03",
            "#01103F……………………………………\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "Ka'a quietly adjusted his hand.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0x0, 6)

    ChrTalk(
        0x101,
        "#00002FHaha … thanks.\x02",
    )

    CloseMessageWindow()

    label("loc_4A83")

    TalkEnd(0xFF)
    Return()

    label("loc_4A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 6)), scpexpr(EXPR_END)), "loc_4AEE")

    ChrTalk(
        0x101,
        (
            "#00000FThis bouquet …\x01",
            "多分、Ariosさんが\x01",
            "I wonder what he gave us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B37")

    label("loc_4AEE")


    ChrTalk(
        0x101,
        (
            "#00005Fthat……\x01",
            "It seems that a flower bouquet is provided.\x02\x03",
            "#00003FWho the hell …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B37")

    SetScenarioFlags(0x0, 6)
    Jump("loc_4B74")

    label("loc_4B3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B5E")
    TalkEnd(0xFF)
    Call(0, 17)
    Return()

    label("loc_4B5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B74")
    TalkEnd(0xFF)
    Call(0, 16)
    Return()

    label("loc_4B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_4F89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F21")

    ChrTalk(
        0x101,
        "#00008F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FLloyd …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha … no.\x01",
            "Ariosさんに兄貴の最期を\x01",
            "I heard it, but ……\x02\x03",
            "#00004FReally, until the very end\x01",
            "Only me and Cecil's older sister\x01",
            "I am worried ……\x02\x03",
            "しかも、Ariosさんや\x01",
            "Mr. Ian also\x01",
            "I did not hurt a bit … …\x02\x03",
            "#00000FExactly, how much\x01",
            "I thought that it was good-looking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FMr. Lloyd ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F…… Haha, do not worry.\x02\x03",
            "#00302FYou and me like that\x01",
            "Because it inherits sufficiently.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D83")

    ChrTalk(
        0x10A,
        "#00604FHut … … certainly.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DE2")

    label("loc_4D83")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DB5")

    ChrTalk(
        0x109,
        "#10102FHuh, sure.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DE2")

    label("loc_4DB5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DE2")

    ChrTalk(
        0x105,
        "#10402FAhaha, indeed.\x02",
    )

    CloseMessageWindow()

    label("loc_4DE2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E1C")

    ChrTalk(
        0x106,
        "#10702FGiggle … I can say that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E7F")

    label("loc_4E1C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E4C")

    ChrTalk(
        0x105,
        "#10404FI can say that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E7F")

    label("loc_4E4C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E7F")

    ChrTalk(
        0x109,
        "#10102FHuh, I can say it.\x02",
    )

    CloseMessageWindow()

    label("loc_4E7F")


    ChrTalk(
        0x101,
        (
            "#00012FOh, that one.\x01",
            "…… Well, well.\x02\x03",
            "#00000FAnyways……\x01",
            "After that it will only rescue Kia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FUh, until the end\x01",
            "Let 's go out without distracting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 5)
    Jump("loc_4F84")

    label("loc_4F21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F84")

    ChrTalk(
        0x101,
        (
            "#00000F……After that it will only rescue Kia.\x02\x03",
            "#00004FBrother … Please be watchful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4F84")

    Jump("loc_5053")

    label("loc_4F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4FA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FA3")
    TalkEnd(0xFF)
    Call(0, 21)
    Return()

    label("loc_4FA3")

    Jump("loc_5053")

    label("loc_4FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5053")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5053")

    ChrTalk(
        0x101,
        (
            "#00000F(Big brother……\x01",
            "I came back to Cros Bell City. )\x02\x03",
            "#00004F(Anything in the future\x01",
            "Take back Ka'aa.\x01",
            "Please be watchful … …! )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_5053")

    TalkEnd(0xFF)
    Return()

    # Function_15_490D end

    def Function_16_5057(): pass

    label("Function_16_5057")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-22240, 1300, 23760, 0)
    MoveCamera(332, 19, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(13720, 0)
    SetChrPos(0x101, -22900, 0, 24540, 0)
    SetChrPos(0x102, -22700, 0, 21640, 0)
    SetChrPos(0x109, -21150, 0, 22390, 315)
    SetChrPos(0x105, -23900, 0, 22740, 0)
    SetCameraDistance(13720, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#6P#00108FThis grave ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FGuy · Bannings …\x01",
            "My brother who died three years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FAnything, even the police\x01",
            "About to compete for 1 or 2\x01",
            "I heard he was a brilliant investigator.\x02\x03",
            "#10104FEven the guard, even its name\x01",
            "There are not many people who know it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10305FOh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOriginally the manager of Sergey manager,\x01",
            "あのAriosさんと\x01",
            "It seems they had organized a combination … …\x02\x03",
            "#00003FEven after there were various things and the group broke up,\x01",
            "Mr. Dudley with the investigation one section\x01",
            "It seems that they were equal each other.\x02\x03",
            "#00009FWell, in various directions\x01",
            "Because I wish I had thrust my neck\x01",
            "It is certain that the face was extraordinarily extensive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00104FIf you listen to the story you are so amazing hearing … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWith unusual behavioral power\x01",
            "On various \"walls\" of Crossbell\x01",
            "Investigator who was confronting … ….\x02\x03",
            "#00008F…… It is a duty to live,\x01",
            "I really could not believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FEventually, the cults of the example also\x01",
            "You are the culprit who murdered your older brother.\x01",
            "You did not have it … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FAh……\x01",
            "The truth is still a mystery.\x02\x03",
            "#00003F(But … someday,\x01",
            "I grab the truth with this hand. )\x02\x03",
            "#00000F(To a little while ago\x01",
            "Maybe it will be ……\x01",
            "Please wait, older brother. )\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -22640, 0, 23360, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x136, 0)
    EventEnd(0x5)
    Return()

    # Function_16_5057 end

    def Function_17_5504(): pass

    label("Function_17_5504")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-22240, 1300, 23760, 0)
    MoveCamera(332, 19, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(13720, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -22900, 0, 24540, 0)
    SetChrPos(0x102, -22700, 0, 21640, 0)
    SetChrPos(0x103, -21150, 0, 22390, 315)
    SetChrPos(0x104, -23900, 0, 22740, 0)
    SetChrPos(0x105, -20180, 0, 23320, 270)
    SetChrPos(0x109, -24250, 0, 21630, 0)
    SetCameraDistance(13720, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00003F#5P#30W………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F#12P#30W………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#12P……by the way……\x02\x03",
            "#10303FLloyd's brother's tomb is\x01",
            "I heard that it is here ….\x02\x03",
            "#10300FHow are your parents?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00305F#6PHey so ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6P…… Certainly both of you\x01",
            "You are dying, are not you?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00004F#11POh, 15 years ago.\x02\x03",
            "#00008F…… To be honest, it was small\x01",
            "I do not remember well.\x02\x03",
            "#00000FAt the time of the recently deployed airline\x01",
            "I heard that it was an accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#6PIn an airship accident … That was right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#6PThe airship has just been put into practical use\x01",
            "It was when I was unstable …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11POh, it fell to the mountains part after all\x01",
            "It seems that no body was found … …\x02\x03",
            "#00008FMy older brother seems to have had trouble with various things.\x02\x03",
            "#00002FBesides, it still takes a lot of trouble\x01",
            "Younger brother must also be fed … …\x02\x03",
            "#00012F……my mother……\x01",
            "True, my head will not rise for the rest of my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6PLloyd …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#6PWell, maybe your older brother does it\x01",
            "You never thought of a burden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#12PI agree……\x02\x03",
            "#00214FTalking about Mr. Lloyd's\x01",
            "It was a cute and unavoidable aura.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PHaha, I know the feeling.\x02\x03",
            "#10309FThree year old Lloyd … ….\x01",
            "I guess it was lovely\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#6PYes, certainly imagining … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#6P…… I want to hold you close\x01",
            "It might be pretty … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#6POh, I can easily imagine!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_5BD7")

    ChrTalk(
        0x101,
        (
            "#00011F#11PDo not make fun of it.\x02\x03",
            "#00004F── Sorry, I took time.\x01",
            "I have to go to Mr Lease.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5C3D")

    label("loc_5BD7")


    ChrTalk(
        0x101,
        (
            "#00011F#11PDo not make fun of it.\x02\x03",
            "#00004F── Sorry, I took time.\x01",
            "Anyway, let's go to the cathedral.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5C3D")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -22640, 0, 23360, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x17C, 6)
    EventEnd(0x5)
    Return()

    # Function_17_5504 end

    def Function_18_5C6C(): pass

    label("Function_18_5C6C")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "Saya · Mc Rain\x01",
            "I sleep here\x01",
            "─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─\x01",
            "S 1175 to S 1199\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D88")

    ChrTalk(
        0x153,
        (
            "#01108FThis grave ……\x02\x03",
            "#01100FLloyd, go on a praying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F… Ah, that's right.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_5D88")

    Jump("loc_5D9F")

    label("loc_5D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D9F")
    Call(0, 19)

    label("loc_5D9F")

    TalkEnd(0xFF)
    Return()

    # Function_18_5C6C end

    def Function_19_5DA3(): pass

    label("Function_19_5DA3")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(21300, 1500, 31700, 0)
    MoveCamera(318, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14830, 0)
    SetChrPos(0x101, 21140, 0, 32049, 0)
    SetChrPos(0x102, 19720, 0, 31850, 45)
    SetChrPos(0x109, 22920, 0, 31580, 315)
    SetChrPos(0x105, 21620, 0, 30560, 0)
    SetCameraDistance(12830, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x109,
        (
            "#12P#10105FThe name of this grave ……\x01",
            "Do not you hear somewhere ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F\"The sword of the wind\",\x01",
            "Arios・マクレイン。\x02\x03",
            "#00003FI have not heard it directly,\x01",
            "I guess he is his wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FCertainly, involved in an accident,\x01",
            "He died …\x02\x03",
            "#00103FShizuku who was together\x01",
            "I took a long-term deal,\x01",
            "I lost the light …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003Fああ、そしてAriosさんは\x01",
            "I quit the police and became a hawk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FWell, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FSomehow, I can not do it\x01",
            "It is a story, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F…… There is no hope.\x02\x03",
            "#00004FShizuku's eyes are\x01",
            "The possibility to regain light still\x01",
            "There seems to be one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FI see …\x01",
            "If I can go and see him in the near future\x01",
            "I do not mind ……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 20740, 0, 31990, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x135, 7)
    EventEnd(0x5)
    Return()

    # Function_19_5DA3 end

    def Function_20_60E1(): pass

    label("Function_20_60E1")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "……………… ……\x01",
            "…… ……………………\x01",
            "Th … … sleep …\x01",
            "─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─\x01",
            "S1 ……… ~ S1 … 8 …\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62DC")

    ChrTalk(
        0x101,
        (
            "#00001FIt is a tomb of a horrible.\x01",
            "The letter also weathered and it collapses … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHey this,\x01",
            "You can not decipher it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FCrying …\x01",
            "It's not a cryptic game.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FI do not know who the grave is ….\x01",
            "It looks like I'm being care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWould you like to visit once.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x135, 6)

    label("loc_62DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 4)), scpexpr(EXPR_END)), "loc_6406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6363")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_635E")

    ChrTalk(
        0x101,
        (
            "#00001F(This grave is Mr. Ian's\x01",
            "It was that of his wife and child … …)\x02\x03",
            "#00003F(… … let's suppose I will go now.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_635E")

    Jump("loc_6406")

    label("loc_6363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6406")

    ChrTalk(
        0x101,
        (
            "#00001F(This grave is Mr. Ian's\x01",
            "It was that of his wife and child … …)\x02\x03",
            "#00008F(Professor Ian … ….\x01",
            "Such a swing is once\x01",
            "I did not show it … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_6406")

    TalkEnd(0xFF)
    Return()

    # Function_20_60E1 end

    def Function_21_640A(): pass

    label("Function_21_640A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    OP_68(-22240, 1300, 23760, 0)
    MoveCamera(332, 19, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(15090, 0)
    SetChrPos(0x101, -22900, 0, 24540, 0)
    SetChrPos(0x102, -21100, 0, 24440, 270)
    SetChrPos(0x103, -22800, 0, 22460, 0)
    SetChrPos(0x104, -19980, 0, 23580, 270)
    SetChrPos(0xF4, -24290, 0, 23980, 45)
    SetChrPos(0xF5, -20900, 0, 22210, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetCameraDistance(13720, 2000)
    StopBGM(0xFA0)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00008F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7567", 0)
    Fade(500)
    Sound(805, 0, 70, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6545")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6545")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6565")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6565")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6585")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6585")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65A5")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_65A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65C5")
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_65C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65E5")
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_65E5")

    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#12P#00108FYour older brother ….\x01",
            "There are lots of scratches, it is somewhat painful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F多分、あのAriosのオッサンと\x01",
            "I wonder what it was like when fighting … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FAh……\x02\x03",
            "#00000F…… But if you look closely it will be\x01",
            "There are lots of fine scratches.\x02\x03",
            "Traces that have repeated repairs many times\x01",
            "There seems to be one.\x02\x03",
            "#00004FWithout giving up regardless of what \"wall\"\x01",
            "Brother who has been pursuing the truth ……\x02\x03",
            "As for this figure of toffers,\x01",
            "I bet he is the older brother's way of living.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67DE")

    ChrTalk(
        0x10A,
        "#6P#00604F… maybe so.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6855")

    label("loc_67DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_681D")

    ChrTalk(
        0x109,
        "#6P#10100F……That may be the case.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6855")

    label("loc_681D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6855")

    ChrTalk(
        0x105,
        "#6P#10400F… It may be so.\x02",
    )

    CloseMessageWindow()

    label("loc_6855")

    OP_5A()
    Fade(500)
    Sound(805, 0, 70, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(150)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00008FThis case, and brother's case ……\x02\x03",
            "#00001FIn order to reach that truth,\x01",
            "Ariosさんを……そしてイアン先生を\x01",
            "You have to get over it.\x02\x03",
            "#00004FI will borrow this tofa for a while.\x01",
            "…… Brother, please lend it to us.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_69A7")

    ChrTalk(
        0x106,
        "#6P#10710FMr. Lloyd ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A04")

    label("loc_69A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_69D6")

    ChrTalk(
        0x105,
        "#6P#10400FLloyd …\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A04")

    label("loc_69D6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A04")

    ChrTalk(
        0x109,
        "#6P#10100FMr. Lloyd ……\x02",
    )

    CloseMessageWindow()

    label("loc_6A04")


    ChrTalk(
        0x103,
        "#6P#00204FOf course, we also help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00309FHaha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FTo regain Ka'a-chan ……\x01",
            "Let's all work together.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5P#00000FAh……\x01",
            "Everyone, please give my best regards!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -22300, 0, 23050, 180)
    OP_69(0xFF, 0x0)
    OP_D7(0x1F)
    SetScenarioFlags(0x1CD, 6)
    EventEnd(0x5)
    Return()

    # Function_21_640A end

    def Function_22_6B0C(): pass

    label("Function_22_6B0C")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)
    SetChrPos(0x101, 380, 4000, 33790, 0)
    SetChrPos(0x102, 2620, 4000, 33580, 0)
    SetChrPos(0x103, -820, 4000, 32680, 0)
    SetChrPos(0x104, 2009, 4000, 31940, 0)
    SetChrPos(0x109, 560, 4000, 31330, 0)
    SetChrPos(0x105, -1060, 4000, 31090, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(2040, 5500, 41860, 0)
    MoveCamera(317, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14260, 0)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    FadeToBright(250, 0)
    OP_0D()
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x12)
    TurnDirection(0x12, 0x13, 500)

    ChrTalk(
        0x12,
        (
            "#5P#07000FBy the way, Ms. Julia - san …\x02\x03",
            "In this cathedral, from a while ago\x01",
            "I heard that \"she\" is taking office.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 500)

    ChrTalk(
        0x13,
        (
            "#12P#07100FYeah, according to other sisters\x01",
            "I heard that he is on a business trip today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5P#07003FOh really……\x02\x03",
            "#07008FI also have a gratitude for that time,\x01",
            "I would like to say hello if you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#N#00005FHighness Claudia ……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        "#12P#N#10105FそれにAssistant Juliaっ！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6DB5():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_6DB5)
    Sleep(50)

    def lambda_6DC5():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_6DC5)
    Sleep(50)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)

    ChrTalk(
        0x12,
        "#11P#07002FAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#12P#07102FThey seem like.\x02",
    )

    CloseMessageWindow()
    OP_68(860, 5100, 39660, 3000)
    MoveCamera(320, 19, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14870, 3000)

    def lambda_6E47():
        OP_95(0xFE, 380, 4000, 38790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6E47)

    def lambda_6E61():
        OP_95(0xFE, 2620, 4000, 38580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6E61)

    def lambda_6E7B():
        OP_95(0xFE, -820, 4000, 37680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6E7B)

    def lambda_6E95():
        OP_95(0xFE, 2009, 4000, 36940, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6E95)

    def lambda_6EAF():
        OP_95(0xFE, 560, 4000, 36330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6EAF)

    def lambda_6EC9():
        OP_95(0xFE, -1060, 4000, 36090, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6EC9)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x12, 0)
    TurnDirection(0x102, 0x12, 0)
    TurnDirection(0x109, 0x12, 0)
    TurnDirection(0x105, 0x12, 0)
    TurnDirection(0x103, 0x12, 0)
    TurnDirection(0x104, 0x12, 0)

    ChrTalk(
        0x12,
        (
            "#11P#07002FEveryone……\x01",
            "Huh, I saw you again.\x02\x03",
            "#07009FI thought it was about time to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FWell, we are coming\x01",
            "Did you notice it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11P#07102FNow, Sieg whirling over the sky\x01",
            "Keep an eye on the surroundings.\x02\x03",
            "So earlier, you guys came\x01",
            "It taught me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYesterday's white falcon ……\x01",
            "Haha, it is truly excellent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#11P#07004FHuhu, Sieg is the royal guard\x01",
            "It is an information transferring person.\x02\x03",
            "#07000FEr, so … …\x01",
            "What are you going to do here?\x02\x03",
            "#07005FOh, and today to the new one … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FThank you so much … last night\x01",
            "Returned to the Special Affairs Support Division,\x01",
            "It is called Tio Plateau.\x02\x03",
            "#00204FI am honored to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#11P#07009FYes, this is it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FWell, we somehow\x01",
            "I tried dropping in with Buri\x01",
            "Where there is something ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FMr. Huff, no doubt the princess and the assistant\x01",
            "I hope to see you again soon\x01",
            "I did not expect that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYour Highlights are going to visit here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#11P#07000FYeah ….\x02\x03",
            "#07003FIn this graveyard, until now you have crossbell\x01",
            "Many people who have died are asleep.\x02\x03",
            "Therefore,\x01",
            "Before today's plenary session by all means\x01",
            "I wanted to stop by.\x02\x03",
            "#07008F\"Cross Bell problem\" in a true sense\x01",
            "To accept it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FCrossbell problem ……\x02\x03",
            "#00204FEmpire and the Republic, Crossbell\x01",
            "Having conflicts over fighting attribution\x01",
            "It was a generic name for the problem ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FYeah, who lives in Crossbell\x01",
            "It's a word I do not use much.\x02\x03",
            "#00103FBecause of this problem,\x01",
            "Just before the war broke out\x01",
            "The tension was growing.\x02\x03",
            "#00108FTwo years ago at Libert\x01",
            "By concluding a \"non-war treaty\"\x01",
            "On the surface#6R噵 噵 噵#I calmed down ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_64(0x12)

    ChrTalk(
        0x102,
        (
            "#12P#00106FSorry, I'm sorry!\x01",
            "What you did with me is rude … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#11P#07003FHouse……\x01",
            "What Elly says\x01",
            "In fact, it is correct.\x02\x03",
            "#07000FGrandmother … … Queen Alicia proposed\x01",
            "The Treaty of the Battle is to exercise force on the two major powers\x01",
            "It was for not letting it go.\x02\x03",
            "By that the crossbell of those days\x01",
            "Although it was released from the extreme tension state … ….\x02\x03",
            "#07003FOn the other hand, from both countries\x01",
            "Invisible pressure rises,\x01",
            "Crosbell's position is still in danger … …\x02\x03",
            "#07001FIn that sense, the Treaty of the\x01",
            "Crossbell problem fundamentally\x01",
            "It can not be said that it was solved.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 500)

    ChrTalk(
        0x13,
        "#12P#07108FYour Highness ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FBut,\x01",
            "I am a non-war treaty\x01",
            "I do not think it was meaningless.\x02\x03",
            "#10103FI just entered the guard,\x01",
            "Empire of the time and Republic went on the border\x01",
            "Intimidation of large-scale military exercises … …\x02\x03",
            "#10108FAnd the empire 's \"train cannon\"\x01",
            "The fears directed to Crossbell City\x01",
            "I still can not forget it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303Fsurely……\x01",
            "If the war has begun, the residents\x01",
            "There must have been tremendous damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FEven just by removing it\x01",
            "It is worthy enough\x01",
            "Is it a treaty?\x02\x03",
            "#10300FWell, your Highness's need to be sick\x01",
            "Is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FWadi, your …\x01",
            "It is truly a frank too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#11P#07009FHuh … … Of course,\x01",
            "I can not go backwards either.\x02\x03",
            "#07004FAt this trade meeting,\x01",
            "The opportunity to discuss the future of Crossbell\x01",
            "I want to make it at all costs.\x02\x03",
            "#07002FTo this graveyard, its determination\x01",
            "I visited to make sure.\x02\x03",
            "#07003FTo Yuria and the Guards\x01",
            "I have increased my extra work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#12P#07104FYour Highness … … There is no ruin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FSomehow ……\x01",
            "Its strength is truly good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FYeah … … the country named Libert\x01",
            "I am really envious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#11P#07002FHuh, thank you.\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x13,
        "#12P#07100F…… Your Highness, it is about time we planned.\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x13, 500)

    ChrTalk(
        0x12,
        (
            "#5P#07005FOh, that's right.\x01",
            "It is almost time for the Orkis Tower\x01",
            "I have to head …\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7C45():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7C45)
    TurnDirection(0x13, 0x101, 500)

    ChrTalk(
        0x12,
        (
            "#11P#07004FThen, everyone at the Special Affairs Support Division.\x01",
            "We will excuse this.\x02\x03",
            "#07000FToday, everyone is in the plenary session\x01",
            "I have heard that it will be guarded … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, as far as power\x01",
            "I will work for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#11P#07009FHehuu, how about that?\x01",
            "Thank you for your consideration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11P#07102FWell, you guys.\x01",
            "I will see you next at the Orkis Tower.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)

    def lambda_7DA4():

        label("loc_7DA4")

        TurnDirection(0x101, 0x12, 500)
        Yield()
        Jump("loc_7DA4")

    QueueWorkItem2(0x101, 2, lambda_7DA4)

    def lambda_7DB6():

        label("loc_7DB6")

        TurnDirection(0x102, 0x12, 500)
        Yield()
        Jump("loc_7DB6")

    QueueWorkItem2(0x102, 2, lambda_7DB6)

    def lambda_7DC8():

        label("loc_7DC8")

        TurnDirection(0x109, 0x12, 500)
        Yield()
        Jump("loc_7DC8")

    QueueWorkItem2(0x109, 2, lambda_7DC8)

    def lambda_7DDA():

        label("loc_7DDA")

        TurnDirection(0x105, 0x12, 500)
        Yield()
        Jump("loc_7DDA")

    QueueWorkItem2(0x105, 2, lambda_7DDA)

    def lambda_7DEC():

        label("loc_7DEC")

        TurnDirection(0x103, 0x12, 500)
        Yield()
        Jump("loc_7DEC")

    QueueWorkItem2(0x103, 2, lambda_7DEC)

    def lambda_7DFE():

        label("loc_7DFE")

        TurnDirection(0x104, 0x12, 500)
        Yield()
        Jump("loc_7DFE")

    QueueWorkItem2(0x104, 2, lambda_7DFE)
    BeginChrThread(0x12, 3, 0, 23)
    Sleep(1000)
    BeginChrThread(0x13, 3, 0, 23)
    Sleep(3000)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 590, 4000, 39380, 180)
    SetScenarioFlags(0x14B, 1)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_22_6B0C end

    def Function_23_7E84(): pass

    label("Function_23_7E84")

    OP_95(0xFE, -2330, 4000, 42280, 2000, 0x0)
    OP_95(0xFE, -3140, 4000, 36010, 2000, 0x0)
    Return()

    # Function_23_7E84 end

    def Function_24_7EAD(): pass

    label("Function_24_7EAD")

    Call(0, 25)
    Return()

    # Function_24_7EAD end

    def Function_25_7EB1(): pass

    label("Function_25_7EB1")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xF, 0xFF)
    OP_68(20680, 1100, 30630, 0)
    MoveCamera(304, 32, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16850, 0)
    SetChrPos(0x101, 21500, 0, 30200, 0)
    SetChrPos(0x102, 20300, 0, 30200, 0)
    SetChrPos(0x103, 21800, 0, 29000, 0)
    SetChrPos(0x104, 19800, 0, 29500, 0)
    SetChrPos(0x109, 20300, 0, 28700, 0)
    SetChrPos(0x105, 19100, 0, 28700, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetCameraDistance(14850, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00005FAriosさん……？\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xF, 0xB4, 0x1F4)

    ChrTalk(
        0xF,
        (
            "#11P#01400F… …. you guys.\x02\x03",
            "#01404FFu …… I do not see you meeting in such a place.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 7)), scpexpr(EXPR_END)), "loc_834C")

    ChrTalk(
        0x101,
        (
            "#6P#00000FA little while ago, Mr. Michelle\x01",
            "Ariosさんを探してた\x01",
            "Looks like it?\x02\x03",
            "#00003F確かAriosさんは、\x01",
            "I was asked by the mayor\x01",
            "I was listening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11P#01403F… Well.\x02\x03",
            "#01400FThat mayor is also ruleful.\x01",
            "I told him I do not need bowing,\x01",
            "Do not say anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FBut I went to the Orchise Tower\x01",
            "I guarded from the hunting corps\x01",
            "I think that it is amazing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FOh, even at Crossbell Times\x01",
            "It seems to have been picked up,\x01",
            "Actually it's a huge monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11P#01404FHuhu, at that time Dudley's aid also\x01",
            "You must have been ……\x02\x03",
            "#01400F…… Well, that matter also thought\x01",
            "I'm done quickly.\x02\x03",
            "As I return to the guild\x01",
            "That's why I came here.\x02\x03",
            "#01400FWhat is delayed on the way home\x01",
            "Let's apologize to Michelle later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FHuhu, I think that is good.\x02\x03",
            "#00105FWell, today to a visit to a grave\x01",
            "It seems I was coming ….\x02\x03",
            "That grave ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84D3")

    label("loc_834C")


    ChrTalk(
        0x101,
        (
            "#6P#00000Fby the way……\x01",
            "Activity in front of the Orkis Tower,\x01",
            "I read it at the Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FTo oppose a hunting soldier,\x01",
            "I heard that it was the lion's fight fighting ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00302FOh, it's a huge monster.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11P#01404FHuhu, at that time Dudley's aid also\x01",
            "You must have been ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FHehe, please do not humble.\x02\x03",
            "#00105FWell, today to a visit to a grave\x01",
            "It seems I was coming ….\x02\x03",
            "That grave ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84D3")

    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_93(0xF, 0x0, 0x1F4)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#11P#01403F…… Saya Mc Rain.\x02\x03",
            "#01408FHe died in an accident five years ago …\x01",
            "It is the mother of Shizuku.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#6P#00200FShizuku's mother ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00308FCertainly, in that accident Shizuku-chan\x01",
            "I was losing the light …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xF)
    Sleep(1000)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0x109,
        "#6P#10105F……Ariosさん？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10305Fwhat's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11P#01404F…… No, nothing.\x02\x03",
            "#01400F─ ─ We finished doing.\x01",
            "Let me get away soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FAh … good tiredness.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)

    def lambda_873D():

        label("loc_873D")

        TurnDirection(0x101, 0xF, 500)
        Yield()
        Jump("loc_873D")

    QueueWorkItem2(0x101, 2, lambda_873D)

    def lambda_874F():

        label("loc_874F")

        TurnDirection(0x102, 0xF, 500)
        Yield()
        Jump("loc_874F")

    QueueWorkItem2(0x102, 2, lambda_874F)

    def lambda_8761():

        label("loc_8761")

        TurnDirection(0x109, 0xF, 500)
        Yield()
        Jump("loc_8761")

    QueueWorkItem2(0x109, 2, lambda_8761)

    def lambda_8773():

        label("loc_8773")

        TurnDirection(0x105, 0xF, 500)
        Yield()
        Jump("loc_8773")

    QueueWorkItem2(0x105, 2, lambda_8773)

    def lambda_8785():

        label("loc_8785")

        TurnDirection(0x103, 0xF, 500)
        Yield()
        Jump("loc_8785")

    QueueWorkItem2(0x103, 2, lambda_8785)

    def lambda_8797():

        label("loc_8797")

        TurnDirection(0x104, 0xF, 500)
        Yield()
        Jump("loc_8797")

    QueueWorkItem2(0x104, 2, lambda_8797)
    OP_68(20680, 700, 30630, 1000)

    def lambda_87BA():
        OP_95(0xFE, 23250, 0, 30200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_87BA)
    WaitChrThread(0xF, 1)
    OP_4B(0xF, 0xFF)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#12P#01401F── From now on,\x01",
            "You will be hit by an unprecedented situation.\x02\x03",
            "#01403FBut in whatever circumstances it is,\x01",
            "Whatever challenge comes … …\x02\x03",
            "#01400FAn important one never loses sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00005FHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10305F……?\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)

    def lambda_88DF():
        OP_95(0xFE, 23250, 0, 16970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_88DF)
    WaitChrThread(0xF, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xF)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    SetChrFlags(0xF, 0x80)

    ChrTalk(
        0x102,
        "#11P#00103F… … I have gone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00305FWhat do you mean by now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FCome on … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FI do not understand well ….\x01",
            "Any advice, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00001F（……Ariosさん……？）\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Sleep(50)
    SetScenarioFlags(0x18C, 6)
    EventEnd(0x5)
    Return()

    # Function_25_7EB1 end

    def Function_26_8A8D(): pass

    label("Function_26_8A8D")

    EventBegin(0x0)
    OP_4B(0xE, 0xFF)
    Fade(500)
    OP_68(-22550, 1500, 23420, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -23390, 0, 22950, 0)
    SetChrPos(0x102, -21870, 0, 22900, 0)
    SetChrPos(0x103, -21870, 0, 21360, 0)
    SetChrPos(0x104, -23390, 0, 21360, 0)
    OP_0D()

    ChrTalk(
        0xE,
        "…………………….\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_8B6C")

    ChrTalk(
        0x101,
        (
            "#00000F(this person is……\x01",
            "  確かNielsenだったな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B89")

    label("loc_8B6C")


    ChrTalk(
        0x101,
        "#00000F(this person is……)\x02",
    )

    CloseMessageWindow()

    label("loc_8B89")

    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "Well ……\x01",
            "Shall I go home soon?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "Hmm, you also\x01",
            "Is it a visit to a grave?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hello.\x01",
            "I am sorry for this.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8C2E():
        OP_95(0xFE, -20540, 0, 24610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8C2E)
    Sleep(500)

    def lambda_8C4B():

        label("loc_8C4B")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_8C4B")

    QueueWorkItem2(0x101, 1, lambda_8C4B)
    Sleep(50)

    def lambda_8C60():

        label("loc_8C60")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_8C60")

    QueueWorkItem2(0x102, 1, lambda_8C60)
    Sleep(50)

    def lambda_8C75():

        label("loc_8C75")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_8C75")

    QueueWorkItem2(0x103, 1, lambda_8C75)
    Sleep(50)

    def lambda_8C8A():

        label("loc_8C8A")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_8C8A")

    QueueWorkItem2(0x104, 1, lambda_8C8A)
    WaitChrThread(0xE, 1)
    OP_95(0xE, -15310, 0, 19380, 2000, 0x0)
    SetChrFlags(0xE, 0x80)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)

    def lambda_8CC9():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8CC9)
    Sleep(100)

    def lambda_8CD9():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8CD9)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_8DA8")

    ChrTalk(
        0x101,
        (
            "#00000FNielsenさん……\x01",
            "You came to visit my big brother's grave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIt seems they were eagerly worshiped ….\x01",
            "I wonder if he was doing something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, I wonder why.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E60")

    label("loc_8DA8")

    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#00100FLloyd, is he acquainted?\x02",
    )

    CloseMessageWindow()

    def lambda_8DDF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8DDF)
    Sleep(50)

    def lambda_8DEF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8DEF)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FNo … I do not think so.\x02\x03",
            "(It means that you are going through the grave\x01",
            "Is it your acquaintance with my brother … …)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E60")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -21160, 0, 21930, 135)
    SetScenarioFlags(0x19D, 4)
    EventEnd(0x5)
    Return()

    # Function_26_8A8D end

    def Function_27_8E86(): pass

    label("Function_27_8E86")

    EventBegin(0x0)
    OP_4B(0xE, 0xFF)
    Fade(500)
    OP_68(-22550, 1500, 23420, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19360, 0)
    SetChrPos(0x101, -23390, 0, 22950, 0)
    SetChrPos(0x102, -21870, 0, 22900, 0)
    SetChrPos(0x103, -21870, 0, 21360, 0)
    SetChrPos(0x104, -23390, 0, 21360, 0)
    OP_0D()

    ChrTalk(
        0xE,
        "#5P…………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FNielsenさん……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#5P…… Hmm, he is Mr. Lloyd.\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00108F#6Phere……\x01",
            "Lloyd's brother's grave ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FA visit to a grave for the elder brother\x01",
            "You did it, did not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PYeah ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PAnd a bit, Mr. Guy\x01",
            "Because I wanted to talk.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FTalking to your big brother, are you …?\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xE)
    OP_93(0xE, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#5PThe declaration of national independence in the raid incident,\x01",
            "And this morning's presidential address ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PThat feeling is various -\x01",
            "People are now equal\x01",
            "It faces in one direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PBut that's why ……\x01",
            "On the contrary, in the \"past darkness\"\x01",
            "I decided to make a mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F\"The past darkness\" …\x01",
            "… … Is it possibly …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PYeah, your older brother -\x01",
            "Guy · Bannings investigators\x01",
            "It is about the murder case.\x02",
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
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105F#6PHuh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#6PMr. Guy ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#6PHe is also ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FDare now ……\x01",
            "No, right now, is it?\x02\x03",
            "#00001FNielsenさんには、\x01",
            "Did you see something …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PHM……\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xE,
        "#11PMr. Lloyd, everyone too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PIf you do not mind, change the place\x01",
            "Why do not you validate the case with me?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 28)
    Return()

    # Function_27_8E86 end

    def Function_28_93A2(): pass

    label("Function_28_93A2")

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
            "Nielsenの検証に付き合う\x01",      # 0
            "I think once\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_941C"),
        (1, "loc_9562"),
        (SWITCH_DEFAULT, "loc_960C"),
    )


    label("loc_941C")


    ChrTalk(
        0x101,
        (
            "#00003F……………………………\x02\x03",
            "#00001FI understand.\x01",
            "Please join us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Because what is here\x01",
            "Let's once go back to town.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Verification of Murder of Guy Bannings】\x07\x00",
            "I started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x95, 0x4, 0x2)
    StopSound(132, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("c0570", 0, 0, 0)
    IdleLoop()
    Jump("loc_960C")

    label("loc_9562")


    ChrTalk(
        0x101,
        (
            "#00003F……Excuse me.\x01",
            "May I think a little?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Well, I do not mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Because I am here for a while,\x01",
            "Please speak to me if you do not mind.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9604")
    OP_93(0xE, 0x0, 0x1F4)
    OP_4C(0xE, 0xFF)
    EventEnd(0x5)

    label("loc_9604")

    SetScenarioFlags(0x19B, 6)
    Jump("loc_960C")

    label("loc_960C")

    Return()

    # Function_28_93A2 end

    def Function_29_960D(): pass

    label("Function_29_960D")

    TalkBegin(0xE)

    ChrTalk(
        0xE,
        "…… Mr. Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If you do not mind, change the place\x01",
            "Why do not you validate the case with me?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Call(0, 28)
    TalkEnd(0xE)
    Return()

    # Function_29_960D end

    SaveToFile()

Try(main)
