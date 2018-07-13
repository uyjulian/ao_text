from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Mrs. Mucha",             # 1
        "Old Man Quint",          # 2
        "Sister Ries",            # 3
        "Bodyguard Soldier",      # 4
        "Bodyguard Soldier",      # 5
        "Claris",                 # 6
        "Nielsen",                # 7
        "Arios",                  # 8
        "ガイ墓前の花",           # 9
        "アリオス家墓前の花",     # 10
        "Princess Klaudia",       # 11
        "Captain Julia",          # 12
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
        "Function_5_1D52",         # 05, 5
        "Function_6_2141",         # 06, 6
        "Function_7_32C5",         # 07, 7
        "Function_8_3E4C",         # 08, 8
        "Function_9_43EA",         # 09, 9
        "Function_10_4532",        # 0A, 10
        "Function_11_4669",        # 0B, 11
        "Function_12_4BCF",        # 0C, 12
        "Function_13_4C31",        # 0D, 13
        "Function_14_4D2B",        # 0E, 14
        "Function_15_4F8C",        # 0F, 15
        "Function_16_56CA",        # 10, 16
        "Function_17_5C11",        # 11, 17
        "Function_18_6485",        # 12, 18
        "Function_19_65A7",        # 13, 19
        "Function_20_6932",        # 14, 20
        "Function_21_6C36",        # 15, 21
        "Function_22_737B",        # 16, 22
        "Function_23_8963",        # 17, 23
        "Function_24_898C",        # 18, 24
        "Function_25_8990",        # 19, 25
        "Function_26_964D",        # 1A, 26
        "Function_27_9A50",        # 1B, 27
        "Function_28_9FCD",        # 1C, 28
        "Function_29_A253",        # 1D, 29
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE3")

    ChrTalk(
        0xFE,
        "Some time ago, policemen came for an inquiry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Ian doing such a monstrous thing...?\x01",
            "It's so absurd that I can't believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F...Yes, we feel the same too.\x02\x03",
            "#00003F(...However, that's the truth.\x01",
            "As for the true motive, we can\x01",
            "only try asking Lawyer Ian himself.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_E79")

    label("loc_DE3")


    ChrTalk(
        0xFE,
        (
            "There's no way that Mr. Ian\x01",
            "did such a monstrous thing...\x01",
            "It's so absurd that I can't believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What could have ever\x01",
            "made him do that...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E79")

    Jump("loc_1D4E")

    label("loc_E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_150F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A1")

    ChrTalk(
        0xFE,
        (
            "No sooner than that barrier\x01",
            "disappears, an absurd\x01",
            "thing happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since that independence declaration, the\x01",
            "people coming to visit graves have decreased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What I can do in such a situation\x01",
            "is at least cleaning the graves.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_149C")
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)

    ChrTalk(
        0x101,
        (
            "#00003F...Excuse me.\x02\x03",
            "#00008FI was wondering whose\x01",
            "this grave is...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "What, you don't know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Hm, well, since it's you guys,\x01",
            "I think there'll be no problems.\x01",
            ""He" too seems a gentle person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FEh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FIs it anyone we know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Hm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The surname of the people\x01",
            "resting here is "Grimwood"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In other words, they're\x01",
            "Mr. Ian Grimwood's family.\x02",
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
        "#00205FLawyer Ian's...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FI-Is that so...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...It's the unmistakable truth.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "About 15 years ago, his wife\x01",
            "and child lost their lives in\x01",
            "an unfortunate accident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the weekends he always came to visit\x01",
            "their grave to remember his family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The gravestone has been damaged by wind\x01",
            "and rain, but...he seems he prays to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was asked to maintain it without repairing it,\x01",
            "so it ended up like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00308FThat lawyer too has gone through a lot of things...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since that independence declaration, he too\x01",
            "must've been busy and didn't visit at all, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like, from now on\x01",
            "you could visit too.\x01",
            "...They feel lonely too, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F............\x02\x03",
            "#00000F...Yes, I understand.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 4)

    label("loc_149C")

    Jump("loc_150A")

    label("loc_14A1")


    ChrTalk(
        0xFE,
        (
            "What I can do in such a situation\x01",
            "is at least cleaning the graves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...You all too, be careful.\x02",
    )

    CloseMessageWindow()

    label("loc_150A")

    Jump("loc_1D4E")

    label("loc_150F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_151D")
    Jump("loc_1D4E")

    label("loc_151D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_1748")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_167C")

    ChrTalk(
        0xFE,
        "Some time ago, Mr. Ian went to the church.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears he visited the graves\x01",
            "of Guy and Arios' wife.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0x101,
        "#00005FUhhm...is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...No, nothing.\x01",
            "It's nothing important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems he's been busy lately, so it' would be\x01",
            "nice if this turned out to be a good change of mood.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1743")

    label("loc_167C")


    ChrTalk(
        0xFE,
        (
            "It appears that some time ago,\x01",
            "Mr. Ian went to visit the\x01",
            "graves of Guy and Arios' wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems he's been busy lately, so it' would be\x01",
            "nice if this turned out to be a good change of mood.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1743")

    Jump("loc_1D4E")

    label("loc_1748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_18FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1853")

    ChrTalk(
        0xFE,
        (
            "Like the mayor says,\x01",
            "Crossbell could need\x01",
            "national independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Naturally, pressure will come from\x01",
            "the Empire and Republic, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want this to be realized no matter what,\x01",
            "even for the sake of the future young generation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18F8")

    label("loc_1853")


    ChrTalk(
        0xFE,
        (
            "National independence could be\x01",
            "something needed to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want this to be realized no matter what,\x01",
            "even for the sake of the future young generation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18F8")

    Jump("loc_1D4E")

    label("loc_18FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_190B")
    Jump("loc_1D4E")

    label("loc_190B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1919")
    Jump("loc_1D4E")

    label("loc_1919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1ADF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A3C")

    ChrTalk(
        0xFE,
        (
            "That madam who always come to\x01",
            "visit a grave... It seems her\x01",
            "husband passed away in a dispute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It was on a time a little earlier, but\x01",
            "I too lost my family in another dispute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because the circumstances are similar,\x01",
            "it ended up weighing on my mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1ADA")

    label("loc_1A3C")


    ChrTalk(
        0xFE,
        (
            "That madam's husband seems to\x01",
            "have passed away in a dispute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, her family is abroad and\x01",
            "it seems they're living happily.\x01",
            "...That's a relief.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ADA")

    Jump("loc_1D4E")

    label("loc_1ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1AED")
    Jump("loc_1D4E")

    label("loc_1AED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_1AFB")
    Jump("loc_1D4E")

    label("loc_1AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_1CA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B16")
    Call(0, 5)
    Jump("loc_1CA0")

    label("loc_1B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF0")

    ChrTalk(
        0xFE,
        (
            "Guy often came to drink\x01",
            "sake at that shed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We often drank together\x01",
            "until the break of dawn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hu hu, he was quite the heavy drinker.\x01",
            "I don't know how many time I drank myself dead drunk.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CA0")

    label("loc_1BF0")


    ChrTalk(
        0xFE,
        (
            "That Guy was quite the heavy drinker.\x01",
            "I don't know how many time I drank myself dead drunk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...One of my regrets is that I wasn't \x01",
            "able to leave him under the table.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CA0")

    Jump("loc_1D4E")

    label("loc_1CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1D4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC0")
    Call(0, 5)
    Jump("loc_1D4E")

    label("loc_1CC0")


    ChrTalk(
        0xFE,
        (
            "I regularly manage\x01",
            "this graveyard.\x01",
            "Come whenever you feel like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right, I'll remember those times\x01",
            "and tell you stories about Guy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D4E")

    TalkEnd(0xFE)
    Return()

    # Function_4_CA7 end

    def Function_5_1D52(): pass

    label("Function_5_1D52")

    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0x101, 0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "Ooh, aren't you Lloyd...\x01",
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
            "#00000FWell, not so long ago.\x01",
            "It has been a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FMr. Lloyd, who is this person...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1E7E")

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, we became acquaintances\x01",
            "due to a previous request.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E7E")


    ChrTalk(
        0x101,
        (
            "#00000FYeah...\x01",
            "He's Mr. Quint. He was a drinking\x01",
            "buddy of my older brother.\x02\x03",
            "#00004FHe has been good to me too.\x01",
            "After the Cult incident, when we drank together\x01",
            "he told me many different old stories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I really enjoyed that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, since Lloyd didn't drink as much\x01",
            "as Guy, it was a little boring, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FHa ha...I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, we joined\x01",
            "too at that time.\x02\x03",
            "#00109FBeing a minor though, Tio had only\x01",
            "juice and it appears she was unhappy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, I see.\x02\x03",
            "#10304FWell, please take good care \x01",
            "of us too from now on, mister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hm, I greatly welcome Lloyd's colleagues.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I manage this graveyard regularly.\x01",
            "You can come whenever you feel like it.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x135, 4)
    Return()

    # Function_5_1D52 end

    def Function_6_2141(): pass

    label("Function_6_2141")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2264")

    ChrTalk(
        0xFE,
        (
            "After that scary event of monsters\x01",
            "appearing in the city passed, I was\x01",
            "finally able to visit the grave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was awfully uneasy, but thinking\x01",
            "about this person who is dead,\x01",
            "courage came out to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am sure you protected me.\x01",
            "Thank you, my dear...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_22F7")

    label("loc_2264")


    ChrTalk(
        0xFE,
        (
            "Thinking about this person who is dead,\x01",
            "courage came out to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am sure I will be fine whatever happens.\x01",
            "I cannot lose, after all...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22F7")

    Jump("loc_32C1")

    label("loc_22FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_230A")
    Jump("loc_32C1")

    label("loc_230A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2489")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23ED")

    ChrTalk(
        0xFE,
        (
            "This morning, my son's family came\x01",
            "worried about me from Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They should have stayed\x01",
            "in a safer place leaving\x01",
            "someone like me be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, however...\x01",
            "I wonder why I am so happy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2484")

    label("loc_23ED")


    ChrTalk(
        0xFE,
        (
            "This morning, my son's family came\x01",
            "worried about me from Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish they would be in a safe place, but...\x01",
            "I wonder why I am so happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2484")

    Jump("loc_32C1")

    label("loc_2489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_261C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2570")

    ChrTalk(
        0xFE,
        (
            "The other day's raid incident\x01",
            "was very frightening...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It reminded me of the disputes of 30\x01",
            "years ago when I lost my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I did not want to go through\x01",
            "such a memory again...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)
    SetChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_2617")

    label("loc_2570")


    ChrTalk(
        0xFE,
        (
            "In the other day's raid incident, I\x01",
            "was reminded of the disputes of 30\x01",
            "years ago when I lost my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I did not want to go through\x01",
            "such a memory again...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2617")

    Jump("loc_32C1")

    label("loc_261C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2695")

    ChrTalk(
        0xFE,
        (
            "To think such and\x01",
            "incident would happen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is just like the disputes time.\x01",
            "How frightening...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32C1")

    label("loc_2695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_26A3")
    Jump("loc_32C1")

    label("loc_26A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_274F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2738")

    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F(It seems she's fervently praying...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(It's bad disturbing her,\x01",
            "let's go away.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_274A")

    label("loc_2738")


    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()

    label("loc_274A")

    Jump("loc_32C1")

    label("loc_274F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_28F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_285A")

    ChrTalk(
        0xFE,
        (
            "It appears that lately bizarre monsters\x01",
            "have been spotted throughout the land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems there has been an appeal\x01",
            "in the city too to not go out on the\x01",
            "highways recklessly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am really glad that the\x01",
            "graveyard is near the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_28EE")

    label("loc_285A")


    ChrTalk(
        0xFE,
        (
            "Even if it is outside the city, it is not so\x01",
            "dangerous to go up to the Cathedral...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am really glad that the\x01",
            "graveyard is near the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28EE")

    Jump("loc_32C1")

    label("loc_28F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_29A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2963")

    ChrTalk(
        0xFE,
        "What a pretty sunset...\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x1F4)

    ChrTalk(
        0xFE,
        (
            "Uh uh, my dear.\x01",
            "I will come again tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_299F")

    label("loc_2963")


    ChrTalk(
        0xFE,
        (
            "It is already evening...\x01",
            "It is time for me to go home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_299F")

    Jump("loc_32C1")

    label("loc_29A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_2B73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AEC")

    ChrTalk(
        0xFE,
        (
            "Nowadays, as a modest hobby,\x01",
            "I have become used to read\x01",
            "before sleeping...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The other day, when I was buying a book, I ended up\x01",
            "choosing two copies of the same one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like, wouldn't you\x01",
            "want to have one copy?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F4, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 6)
    Jump("loc_2B6E")

    label("loc_2AEC")


    ChrTalk(
        0xFE,
        (
            "Lately I decided to pick up an hobby, \x01",
            "encouraged by my son's family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, as I thought, you \x01",
            "need enjoyment in life.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B6E")

    Jump("loc_32C1")

    label("loc_2B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA5")

    ChrTalk(
        0xFE,
        (
            "Lately I received a letter from my son's\x01",
            "family who they live in Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was invited to come to\x01",
            "Remiferia since I live\x01",
            "in Crossbell alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I cannot\x01",
            "really leave Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is a place packed with important\x01",
            "memories of my late husband and I.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2D51")

    label("loc_2CA5")


    ChrTalk(
        0xFE,
        (
            "I was glad they invited me, however...\x01",
            "I do not have any intention\x01",
            "of leaving Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is a place packed with important\x01",
            "memories of my late husband and I.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D51")

    Jump("loc_32C1")

    label("loc_2D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2DF2")

    ChrTalk(
        0xFE,
        (
            "Princess Klaudia seems\x01",
            "to be a very kind person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I saw Queen Alicia of Liberl\x01",
            "too in a picture, and...\x01",
            "Their air is really similar.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32C1")

    label("loc_2DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2EAF")

    ChrTalk(
        0xFE,
        (
            "Orchis Tower, the building that is\x01",
            "the symbol of Crossbell new era...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it had been possible, I would have liked to go \x01",
            "see the unveiling ceremony with my husband.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32C1")

    label("loc_2EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3056")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF3")

    ChrTalk(
        0xFE,
        (
            "It seems that at the Trade Conference are going\x01",
            "to come VIPs from the Empire and Republic too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can feel that the era has changed, compared to \x01",
            "the times when there were nothing but disputes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope that from now on a good era is made,\x01",
            "not with military power, but through dialog.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3051")

    label("loc_2FF3")


    ChrTalk(
        0xFE,
        (
            "I hope that from now on a good era is made,\x01",
            "not with military power, but through dialog.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3051")

    Jump("loc_32C1")

    label("loc_3056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3064")
    Jump("loc_32C1")

    label("loc_3064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_3162")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_310A")

    ChrTalk(
        0xFE,
        (
            "That person over there...\x01",
            "Could she be a new Sister?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh...she looks about the age of my\x01",
            "granddaughter who lives in Remiferia.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_315D")

    label("loc_310A")


    ChrTalk(
        0xFE,
        (
            "I have a granddaughter in Remiferia.\x01",
            "I think she's about that Sister's age...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_315D")

    Jump("loc_32C1")

    label("loc_3162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_31C3")

    ChrTalk(
        0xFE,
        (
            "My...\x01",
            "The sun has gone down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it is about time\x01",
            "I return home too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32C1")

    label("loc_31C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_32C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3274")

    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "O-Oh, I am sorry.\x01",
            "I did not notice you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was offering prayers\x01",
            "to my husband's grave...\x01",
            "Please, forgive me.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x0)
    SetScenarioFlags(0x0, 0)
    Jump("loc_32C1")

    label("loc_3274")


    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F(...It would be bad to\x01",
            "disturb her. Let's go.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32C1")

    TalkEnd(0xFE)
    Return()

    # Function_6_2141 end

    def Function_7_32C5(): pass

    label("Function_7_32C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_32D6")
    Jump("loc_3E48")

    label("loc_32D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_32E4")
    Jump("loc_3E48")

    label("loc_32E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_365A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A9")

    ChrTalk(
        0xA,
        (
            "#04401FIt appears that the Jaegers have deployed\x01",
            "on the area of the mountain path.\x02\x03",
            "#04403F...As a "Gralsritter",\x01",
            "I can't take official\x01",
            "actions.\x02\x03",
            "#04408FI am terribly sorry to not\x01",
            "being able to assist you\x01",
            "in this terrible time...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3427")

    ChrTalk(
        0x103,
        (
            "#00200FBy the way, you're a lot\x01",
            "skilled, Miss Ries.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3427")


    ChrTalk(
        0x102,
        (
            "#00108FIt's true that borrowing the strength of\x01",
            "a "Gralsritter" would be reassuring, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301FWell, those on the mountain path are\x01",
            "probably quite troublesome opponents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FMiss Ries, please\x01",
            "wait here in case\x01",
            "something happens.\x02\x03",
            "#00001FWe and the CGF will try to do\x01",
            "something about Mainz matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04401F...I understand.\x01",
            "Please, be extremely careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3655")

    label("loc_35A9")


    ChrTalk(
        0xA,
        (
            "#04401FIt appears that the Jaegers have deployed\x01",
            "on the area of the mountain path.\x02\x03",
            "#04403FDue to my status of "Gralsritter"\x01",
            "I can't assist you...\x01",
            "Please, be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3655")

    Jump("loc_3E48")

    label("loc_365A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3668")
    Jump("loc_3E48")

    label("loc_3668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3764")

    ChrTalk(
        0xA,
        (
            "#04400FAbout the "Pleroma Grass", as soon\x01",
            "as I have contacted the knights, I\x01",
            "intend to start an investigation too.\x02\x03",
            "#04403FI don't know how far I will able\x01",
            "to research alone, however...\x01",
            "As soon as I figure something, I'll report it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E48")

    label("loc_3764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3B0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A91")

    ChrTalk(
        0xA,
        "#04400FEveryone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMiss Ries...\x01",
            "You were here?\x02\x03",
            "#00004FThank you for the valuable information\x01",
            "you gave us the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04404FNot at all, I'm glad I could be of help.\x02\x03",
            "#04400FEveryone, where're you going now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FWell, actually...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Elie explained they are going to the Doll Studio.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#04405FThe Rosenberg Studio...\x02\x03",
            "#04403FI'm sure it's a place that was recognised\x01",
            "to have a connection with the "Society".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FOh boy, that's the\x01",
            "Gralsritter for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04403F...I heard that Jｶrg Rosenberg is a\x01",
            "man who knows right from wrong, but...\x02\x03",
            "#04401FEven so, the fact remains that\x01",
            "he has ties to the "Society".\x02\x03",
            "If you intend to meet him,\x01",
            "you should be very careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYes...that's our intention.\x01",
            "Thank you for your warning.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16D, 2)
    Jump("loc_3B05")

    label("loc_3A91")


    ChrTalk(
        0xA,
        (
            "#04400FIf you're going to the Doll Studio,\x01",
            "you should prepare yourselves fully.\x02\x03",
            "#04403F...Please, be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B05")

    Jump("loc_3E48")

    label("loc_3B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_3B18")
    Jump("loc_3E48")

    label("loc_3B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_3B26")
    Jump("loc_3E48")

    label("loc_3B26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3B34")
    Jump("loc_3E48")

    label("loc_3B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3B42")
    Jump("loc_3E48")

    label("loc_3B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3B50")
    Jump("loc_3E48")

    label("loc_3B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3B5E")
    Jump("loc_3E48")

    label("loc_3B5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3B6C")
    Jump("loc_3E48")

    label("loc_3B6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_3E31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B8B")
    TalkEnd(0xFE)
    Call(0, 8)
    Return()

    label("loc_3B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DA2")

    ChrTalk(
        0xA,
        (
            "#13800FAfter I finish to worship the memorial\x01",
            "monument, I will have to go to hear\x01",
            "from my seniors the content of my job.\x02\x03",
            "#13804FWhen you take up a new post, it\x01",
            "seems there are many things to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FAh...could it be that\x01",
            "we got in your way...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#13800FNo, not at all...\x01",
            "I could also meet KeA.\x02\x03",
            "#13803F...More importantly,\x01",
            "somehow I have\x01",
            "gotten hungry.\x02\x03",
            "#13802FI want to go back to the\x01",
            "dormitory fast and eat the\x01",
            "bread I bought at the bakery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F(*giggle*, she seems\x01",
            "to still be a glutton.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E2C")

    label("loc_3DA2")


    ChrTalk(
        0xA,
        (
            "#13800FI will be in the care\x01",
            "of this cathedral\x01",
            "for a little while.\x02\x03",
            "Please come to visit me anytime\x01",
            "you want, if you need something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E2C")

    Jump("loc_3E48")

    label("loc_3E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_3E3F")
    Jump("loc_3E48")

    label("loc_3E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3E48")

    label("loc_3E48")

    TalkEnd(0xFE)
    Return()

    # Function_7_32C5 end

    def Function_8_3E4C(): pass

    label("Function_8_3E4C")

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
            "#11P#13800FAah, everyone...\x01",
            "Thank you for before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FMiss Ries, it seems you are\x01",
            "over with your greetings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#13804FYes, I finished them with no problems.\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x153, 500)

    ChrTalk(
        0xA,
        (
            "#11P#13800F...Is she the child you were talking\x01",
            "about before...the one you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, she's KeA.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01105FMiss, could you\x01",
            "be a new Sister?\x02\x03",
            "#01109FEheheh, hello!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        "#11P#13802F...Cute...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F*giggle*, right?\x01",
            "Also, she's a\x01",
            "very good child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00009FShe often helps us\x01",
            "preparing meals...\x01",
            "She's really a great help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10306FOh boy, showing here too how\x01",
            "much of doting parents you're?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FAhaha...\x01",
            "I understand how they feel, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#01111FHoee?\x02",
    )

    CloseMessageWindow()

    def lambda_41F3():
        TurnDirection(0x101, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_41F3)
    Sleep(50)

    def lambda_4203():
        TurnDirection(0x105, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4203)
    Sleep(50)

    def lambda_4213():
        TurnDirection(0x102, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4213)
    Sleep(50)

    def lambda_4223():
        TurnDirection(0x109, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4223)
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
            "#11P#13803F(...I see, this child\x01",
            "is that Cult's...)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_42DC():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_42DC)
    Sleep(50)

    def lambda_42EC():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_42EC)
    Sleep(50)

    def lambda_42FC():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_42FC)
    Sleep(50)

    def lambda_430C():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_430C)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        (
            "#00105FEehm, Miss Ries,\x01",
            "is something wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#13803F...No, nothing.\x02\x03",
            "#13802FKeA, it is nice\x01",
            "to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#01109FYes, nice to meet you too!\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x135, 5)
    SetChrPos(0x0, 0, 4000, 40000, 180)
    EventEnd(0x5)
    Return()

    # Function_8_3E4C end

    def Function_9_43EA(): pass

    label("Function_9_43EA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44D2")

    ChrTalk(
        0xFE,
        (
            "Oh, you're...\x01",
            "The Special Support Section people who\x01",
            "last night visited the Arseille, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crown Princess Klaudia and \x01",
            "Captain Julia are further ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please pass through,\x01",
            "if you feel like it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_452E")

    label("loc_44D2")


    ChrTalk(
        0xFE,
        (
            "Crown Princess Klaudia and \x01",
            "Captain Julia are further ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please pass through.\x02",
    )

    CloseMessageWindow()

    label("loc_452E")

    TalkEnd(0xFE)
    Return()

    # Function_9_43EA end

    def Function_10_4532(): pass

    label("Function_10_4532")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45F7")

    ChrTalk(
        0xFE,
        (
            "As you can expect, I think there\x01",
            "wouldn't be anyone trying to cause\x01",
            "a ruckus in a graveyard, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The unexpected also happens.\x01",
            "I must properly be on watch out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4665")

    label("loc_45F7")


    ChrTalk(
        0xFE,
        (
            "It's the minimum required guarding...\x01",
            "The responsibility is grave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I must properly be on watch out.\x02",
    )

    CloseMessageWindow()

    label("loc_4665")

    TalkEnd(0xFE)
    Return()

    # Function_10_4532 end

    def Function_11_4669(): pass

    label("Function_11_4669")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B47")

    ChrTalk(
        0xFE,
        (
            "...Oh, guys. What an\x01",
            "unexpected meeting.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4900")

    ChrTalk(
        0x101,
        (
            "#00003FIt seems you were visiting a grave.\x01",
            "...Please excuse us.\x02\x03",
            "#00000F...Could it be that who\x01",
            "is resting here is...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F1st Lt. Ozma Seeker...\x01",
            "Fran and my dad, who passed \x01",
            "away about 10 years ago.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47A6")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_47A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47C9")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_47C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47EC")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_47EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_480C")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_480C")

    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105FMiss Noｱl's father...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FI only heard stories about him...\x01",
            "It seems he was an excellent officer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FEeh, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He had a strong sense of justice\x01",
            "and was a strict man...\x01",
            "It happened while on duty.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49CD")

    label("loc_4900")


    ChrTalk(
        0x101,
        (
            "#00003FIt seems you were visiting a grave.\x01",
            "...Please excuse us.\x02\x03",
            "#00008F...If I remember correctly,\x01",
            "who is resting here is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F...Yes,\x01",
            "Fran and my dad, who passed \x01",
            "away about 10 years ago.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49CD")


    ChrTalk(
        0xFE,
        (
            "...Since the job is that of the CGF member, \x01",
            "we should have been prepared, but...\x01",
            "As you can expect, at that time we couldn't bear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, it's a story from\x01",
            "the past, please don't\x01",
            "look so serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...However, you all too must\x01",
            "hold your lives precious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you were to pass away, a great\x01",
            "number of people would feel sad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10104F...Yes, I know.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 3)
    Jump("loc_4BCB")

    label("loc_4B47")


    ChrTalk(
        0xFE,
        (
            "...However, you all too must\x01",
            "hold your lives precious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you were to pass away, a great\x01",
            "number of people would feel sad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BCB")

    TalkEnd(0xFE)
    Return()

    # Function_11_4669 end

    def Function_12_4BCF(): pass

    label("Function_12_4BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C2A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BF8")
    Call(0, 26)
    Return()

    label("loc_4BF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4C0F")
    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Jump("loc_4C25")

    label("loc_4C0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 6)), scpexpr(EXPR_END)), "loc_4C21")
    Call(0, 29)
    Return()

    label("loc_4C21")

    Call(0, 27)
    Return()

    label("loc_4C25")

    Jump("loc_4C30")

    label("loc_4C2A")

    TalkBegin(0xFE)
    TalkEnd(0xFE)

    label("loc_4C30")

    Return()

    # Function_12_4BCF end

    def Function_13_4C31(): pass

    label("Function_13_4C31")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "O, lambs born beneath the bell,\x01",
            "please, sleep peacefully.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "From pure white clouds, let the golden shining sun\x01",
            "become a straight path to the clear blue sky,\x01",
            "guiding souls to the Goddess.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_4C31 end

    def Function_14_4D2B(): pass

    label("Function_14_4D2B")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　　 Ozma Seeker\x01",
            "            Sleeps Here\x01",
            "───────────────\x01",
            " S1157 - S1194\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F88")

    ChrTalk(
        0x101,
        (
            "#00005F"Seeker"...\x01",
            "Could he be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F1st Lt. Ozma Seeker...\x01",
            "Fran and my dad, who passed \x01",
            "away about 10 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FMiss Noｱl's father...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FUuhm, it's the first time I hear this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha, I'm not the \x01",
            "type to talk about these \x01",
            "kind of things.\x02\x03",
            "#10104F...Let's go, everyone.\x01",
            "We'd probably get scolded by my dad\x01",
            "for standing still in such a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F...Ha ha, is that so?\x01",
            "Then, let's go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 2)

    label("loc_4F88")

    TalkEnd(0xFF)
    Return()

    # Function_14_4D2B end

    def Function_15_4F8C(): pass

    label("Function_15_4F8C")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "       Guy Bannings\x01",
            "       Sleeps Here\x01",
            "───────────────\x01",
            " S1176 - S1201\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50D9")

    ChrTalk(
        0x153,
        (
            "#01105F(...The man of this grave...)\x02\x03",
            "#01103F............\x02",
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
            "KeA joined her hand in silence.\x07\x00\x02",
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
        "#00002FHa ha...thanks.\x02",
    )

    CloseMessageWindow()

    label("loc_50D9")

    TalkEnd(0xFF)
    Return()

    label("loc_50DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 6)), scpexpr(EXPR_END)), "loc_5138")

    ChrTalk(
        0x101,
        (
            "#00000FThis bouquet...\x01",
            "Mr. Arios probably\x01",
            "offered it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_519A")

    label("loc_5138")


    ChrTalk(
        0x101,
        (
            "#00005FOh... It seems someone \x01",
            "offered a bouquet of flowers.\x02\x03",
            "#00003FWho could have been...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_519A")

    SetScenarioFlags(0x0, 6)
    Jump("loc_51D7")

    label("loc_51A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51C1")
    TalkEnd(0xFF)
    Call(0, 17)
    Return()

    label("loc_51C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51D7")
    TalkEnd(0xFF)
    Call(0, 16)
    Return()

    label("loc_51D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_5608")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5599")

    ChrTalk(
        0x101,
        "#00008F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FLloyd...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, well...\x01",
            "Mr. Arios told me my\x01",
            "big brother's last moments...\x02\x03",
            "#00004FReally, until the very end,\x01",
            "he was always worried\x01",
            "about me and sister Cecil...\x02\x03",
            "Furthermore, he didn't even\x01",
            "cursed Mr. Arios and\x01",
            "Lawyer Ian even a little...\x02\x03",
            "#00000FHonestly, how much of a\x01",
            "softhearted person was he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FMr. Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F...Ha ha, rest assured.\x02\x03",
            "#00302FYou've taken over plenty\x01",
            "of that side of him too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53EE")

    ChrTalk(
        0x10A,
        "#00604FHmph...indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5449")

    label("loc_53EE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_541E")

    ChrTalk(
        0x109,
        "#10102FUh uh, indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5449")

    label("loc_541E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5449")

    ChrTalk(
        0x105,
        "#10402FAhaha, indeed.\x02",
    )

    CloseMessageWindow()

    label("loc_5449")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5484")

    ChrTalk(
        0x106,
        "#10702F*chuckle chuckle*...true.\x02",
    )

    CloseMessageWindow()
    Jump("loc_54E3")

    label("loc_5484")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_54AE")

    ChrTalk(
        0x105,
        "#10404FWord up.\x02",
    )

    CloseMessageWindow()
    Jump("loc_54E3")

    label("loc_54AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_54E3")

    ChrTalk(
        0x109,
        "#10102FUh uh, you can say that.\x02",
    )

    CloseMessageWindow()

    label("loc_54E3")


    ChrTalk(
        0x101,
        (
            "#00012FH-Hey now.\x01",
            "...Ha ha, oh, well.\x02\x03",
            "#00000FIn any case... What remains\x01",
            "is just to save KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, let's go, without letting\x01",
            "our guards down until the end.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 5)
    Jump("loc_5603")

    label("loc_5599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5603")

    ChrTalk(
        0x101,
        (
            "#00000F...What remains is only to save KeA.\x02\x03",
            "#00004FBig brother...please watch over me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_5603")

    Jump("loc_56C6")

    label("loc_5608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5627")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5622")
    TalkEnd(0xFF)
    Call(0, 21)
    Return()

    label("loc_5622")

    Jump("loc_56C6")

    label("loc_5627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_56C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56C6")

    ChrTalk(
        0x101,
        (
            "#00000F(Big brother...\x01",
            "I've come back to Crossbell.)\x02\x03",
            "#00004F(Now I'm going to get\x01",
            "back KeA at all costs.\x01",
            "Please watch over me...!)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_56C6")

    TalkEnd(0xFF)
    Return()

    # Function_15_4F8C end

    def Function_16_56CA(): pass

    label("Function_16_56CA")

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
        "#6P#00108FThis grave is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FGuy Bannings...\x01",
            "My big brother who died on duty 3 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FI heard he was a remarkable detective,\x01",
            "one of the best among the police.\x01\x02\x03",
            "#10104FEven in the CGF, they aren't\x01",
            "few those who know his name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10305FEeh, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIt seems he was originally\x01",
            "Chief Sergei's subordinate\x01",
            "and Mr. Arios' partner...\x02\x03",
            "#00003FMany things happened and even after\x01",
            "the party disbanded, it seems he was a\x01",
            "worthy rival of Mr. Dudley in Section One.\x02\x03",
            "#00009FWell, it's a sure fact that because\x01",
            "he poked his nose in many fields,\x01",
            "he was widely known.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104FThe more stories I hear about him, the more \x01",
            "he seems to have been an amazing person...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FA detective who faced many\x01",
            "of Crossbell "barriers" with\x01",
            "an unusual energy...\x02\x03",
            "#00008F...Being killed on duty...\x01",
            "I couldn't really believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FIn the end, who killed\x01",
            "your older brother wasn't\x01",
            "even that Cult, right...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FYeah...\x01",
            "The truth is still a mystery.\x02\x03",
            "#00003F(However... One day, I'll get\x01",
            "to the truth with these hands.)\x02\x03",
            "#00000F(It could be something a little\x01",
            "farther in the future, but...\x01",
            "Wait for me, big brother.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -22640, 0, 23360, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x136, 0)
    EventEnd(0x5)
    Return()

    # Function_16_56CA end

    def Function_17_5C11(): pass

    label("Function_17_5C11")

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
        "#00003F#5P#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F#12P#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#12P...By the way...\x02\x03",
            "#10303FI had heard that Lloyd's older\x01",
            "brother's grave is here, but...\x02\x03",
            "#10300FWhat about your parents?\x02",
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
        "#00305F#6PNow that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6P...They both passed\x01",
            "away too, am I right?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00004F#11PYeah, 15 years ago.\x02\x03",
            "#00008F...Honestly, because I was little\x01",
            "I don't remember too much.\x02\x03",
            "#00000FAlthough I heard that it was in an\x01",
            "orbal airship accident that had been\x01",
            "just gone into commission at the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#6PIn an airship accident...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#6PIt was still a period of insecurity because\x01",
            "airship had just been implemented.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PYeah. In the end, it fell in a mountainous region\x01",
            "and they didn't find any remains, so they say...\x02\x03",
            "#00008FIt seemed that big brother was having it hard too.\x02\x03",
            "#00002FAs a bonus, he had to maintain a difficult \x01",
            "childish little brother for a long time too...\x02\x03",
            "#00012F...Ha ha...\x01",
            "Really, I'll never be able to repay him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6PLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#6PWell, your big brother probably never\x01",
            "thought of that as a heavy load to bear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#12PRight...\x02\x03",
            "#00214FWhen he was speaking of Mr. Lloyd, he said\x01",
            "you were cute and had a helpless aura...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PAhaha, I can understand how he felt.\x02\x03",
            "#10309FA three years hold Lloyd, eh...?\x01",
            "I'm sure he must've been adorable㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#6PR-Really, if I picture him...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#6P...He could've been so lovely\x01",
            "you'd have wanted to hug him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#6POoh, I can easily imagine him!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_63DB")

    ChrTalk(
        0x101,
        (
            "#00011F#11PD-Don't make fun of me.\x02\x03",
            "#00004F──Sorry, I've took up your time.\x01",
            "We have to go to Miss Ries' place.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6456")

    label("loc_63DB")


    ChrTalk(
        0x101,
        (
            "#00011F#11PD-Don't make fun of me.\x02\x03",
            "#00004F──Sorry, I've took up your time.\x01",
            "At any rate, let's go the Cathedral.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6456")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -22640, 0, 23360, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x17C, 6)
    EventEnd(0x5)
    Return()

    # Function_17_5C11 end

    def Function_18_6485(): pass

    label("Function_18_6485")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "   Saya MacLaine\x01",
            "   Sleeps Here\x01",
            "───────────────\x01",
            " S1175 - S1199\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6591")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_658C")

    ChrTalk(
        0x153,
        (
            "#01108FThis grave is...\x02\x03",
            "#01100FLloyd, let's pay our respects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F...Yeah, you're right.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_658C")

    Jump("loc_65A3")

    label("loc_6591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65A3")
    Call(0, 19)

    label("loc_65A3")

    TalkEnd(0xFF)
    Return()

    # Function_18_6485 end

    def Function_19_65A7(): pass

    label("Function_19_65A7")

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
            "#12P#10105FThe name on this grave...\x01",
            "I think I've heard it somewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FThe "Divine Blade of Wind",\x01",
            "Arios MacLaine.\x02\x03",
            "#00003FI've never heard directly from him,\x01",
            "but I think this is his wife grave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FIf I remember correctly, she was caught up\x01",
            "in an accident and passed away...\x02\x03",
            "#00103FShizuku, who was with her,\x01",
            "escaped death but ended up\x01",
            "losing her sight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, and then Mr. Arios quit\x01",
            "the police and became a Bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FUuhm, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FSomehow it's an\x01",
            "unbearable story...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F...It's not that there's no hope.\x02\x03",
            "#00004FIt seems that it's possible\x01",
            "to get back the light for\x01",
            "Shizuku's eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FRight...\x01",
            "I hope we can go pay\x01",
            "her a visit before long...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 20740, 0, 31990, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x135, 7)
    EventEnd(0x5)
    Return()

    # Function_19_65A7 end

    def Function_20_6932(): pass

    label("Function_20_6932")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "...... ..  \x01",
            ".. ........\x01",
            "     Sl.... He..\x01",
            "───────────────......\x01",
            " S1... - S1.8. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B1B")

    ChrTalk(
        0x101,
        (
            "#00001FIt's an all ruined grave. The characters\x01",
            "too have weathered and are worn out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FWell, it seems they're\x01",
            "impossible to decipher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FDecipher...\x01",
            "That's not a coded puzzle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FI don't know whose grave it is, but...\x01",
            "It seems it's been maintained.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FShould we pay our respects?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x135, 6)

    label("loc_6B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 4)), scpexpr(EXPR_END)), "loc_6C32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6B9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B98")

    ChrTalk(
        0x101,
        (
            "#00001F(This grave belongs to\x01",
            "Lawyer Ian's wife and child...)\x02\x03",
            "#00003F(...Let's go now.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_6B98")

    Jump("loc_6C32")

    label("loc_6B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6C32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C32")

    ChrTalk(
        0x101,
        (
            "#00001F(This grave belongs to\x01",
            "Lawyer Ian's wife and child...)\x02\x03",
            "#00008F(Lawyer Ian...\x01",
            "He never said\x01",
            "anything even once...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_6C32")

    TalkEnd(0xFF)
    Return()

    # Function_20_6932 end

    def Function_21_6C36(): pass

    label("Function_21_6C36")

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
        "#00008F............\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D61")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6D61")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D81")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6D81")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DA1")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6DA1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DC1")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6DC1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DE1")
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6DE1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E01")
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6E01")

    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#12P#00108FYour older brother's tonfas...\x01",
            "They're so full of cuts that somehow it's pitiful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FProbably stuff from when he\x01",
            "went at it with ol' man Arios...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FYeah...\x02\x03",
            "#00000F...However, if you look carefully, aside from\x01",
            "those there're a lot of smaller scratches.\x02\x03",
            "It also seems there're even\x01",
            "traces of repeated repairs.\x02\x03",
            "#00004FMy big brother who seeked the truth without \x01",
            "giving up, no matter the "barriers" he was facing...\x02\x03",
            "The aspect of these tonfas is for sure\x01",
            "my big brother very own way to live.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_704C")

    ChrTalk(
        0x10A,
        "#6P#00604F...It could be.\x02",
    )

    CloseMessageWindow()
    Jump("loc_70AB")

    label("loc_704C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7082")

    ChrTalk(
        0x109,
        "#6P#10100F...That could be.\x02",
    )

    CloseMessageWindow()
    Jump("loc_70AB")

    label("loc_7082")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_70AB")

    ChrTalk(
        0x105,
        "#6P#10400F...Maybe.\x02",
    )

    CloseMessageWindow()

    label("loc_70AB")

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
            "#00008FThis incident and also my big brother's incident...\x02\x03",
            "#00001FTo reach that truth, we must\x01",
            "overcome Mr. Arios...\x01",
            "And Lawyer Ian too.\x02\x03",
            "#00004FI'll borrow these tonfas for a little while.\x01",
            "...Big brother, please, give us your strength.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7202")

    ChrTalk(
        0x106,
        "#6P#10710FMr. Lloyd...\x02",
    )

    CloseMessageWindow()
    Jump("loc_725B")

    label("loc_7202")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_722F")

    ChrTalk(
        0x105,
        "#6P#10400FLloyd...\x02",
    )

    CloseMessageWindow()
    Jump("loc_725B")

    label("loc_722F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_725B")

    ChrTalk(
        0x109,
        "#6P#10100FMr. Lloyd...\x02",
    )

    CloseMessageWindow()

    label("loc_725B")


    ChrTalk(
        0x103,
        "#6P#00204FNaturally, we will help you too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00309FHa ha, that's for sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FEveryone, let's combine our strengths...\x01",
            "To get back keA.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5P#00000FYeah...\x01",
            "Everyone, once again, I'm counting on you!\x02",
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

    # Function_21_6C36 end

    def Function_22_737B(): pass

    label("Function_22_737B")

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
            "#5P#07000FBy the way, Miss Julia...\x02\x03",
            "It seems that "she" has been newly appointed\x01",
            "to this Cathedral since a little while ago.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 500)

    ChrTalk(
        0x13,
        (
            "#12P#07100FYes. According to another Sister,\x01",
            "today she's on a business trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5P#07003FI see...\x02\x03",
            "#07008FI am indebted to her for back then, if\x01",
            "possible I would have liked to greet her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#N#00005FYour Highness Klaudia...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        "#12P#N#10105FAnd Captain Julia too!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_764F():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_764F)
    Sleep(50)

    def lambda_765F():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_765F)
    Sleep(50)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)

    ChrTalk(
        0x12,
        "#11P#07002FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#12P#07102FIt seems it's them.\x02",
    )

    CloseMessageWindow()
    OP_68(860, 5100, 39660, 3000)
    MoveCamera(320, 19, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14870, 3000)

    def lambda_76DF():
        OP_95(0xFE, 380, 4000, 38790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76DF)

    def lambda_76F9():
        OP_95(0xFE, 2620, 4000, 38580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_76F9)

    def lambda_7713():
        OP_95(0xFE, -820, 4000, 37680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7713)

    def lambda_772D():
        OP_95(0xFE, 2009, 4000, 36940, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_772D)

    def lambda_7747():
        OP_95(0xFE, 560, 4000, 36330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7747)

    def lambda_7761():
        OP_95(0xFE, -1060, 4000, 36090, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7761)
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
            "#11P#07002FEveryone...\x01",
            "*giggle*, we meet again.\x02\x03",
            "#07009FI thought it would be time for you to arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FEh, you knew that\x01",
            "we were coming?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11P#07102FAt present, Sieg is watching\x01",
            "the environs from up the sky.\x02\x03",
            "A little time ago he told\x01",
            "us you were coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYesterday's white falcon...\x01",
            "Ha ha, he's outstanding, as we thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#11P#07004F*giggle*, after all, Sieg is the information\x01",
            "carrier of the Royal Guards.\x02\x03",
            "#07000FUhhm, so...\x01",
            "What have you come to do here?\x02\x03",
            "#07005FOh, and today there is even a new person...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FNice to meet you... \x01",
            "My name is Tio Plato.\x01",
            "I came back to the SSS last night.\x02\x03",
            "#00204FIt is an honor meeting you like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#11P#07009FYes, likewise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FWell, we were somehow\x01",
            "droppin' by without a\x01",
            "real reason, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHu hu, we would've never imagined\x01",
            "to be able to meet again the princess\x01",
            "and the captain this early.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FDid you come to worship?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#11P#07000FYes...\x02\x03",
            "#07003FA great number of persons who passed away \x01",
            "in Crossbell until now rest in this graveyard.\x02\x03",
            "That is why, no matter what,\x01",
            "I wanted to stop by here today,\x01",
            "before the conference begins.\x02\x03",
            "#07008FEven for the sake to come to grips with the\x01",
            ""Crossbell Problem" in the real sense...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FThe Crossbell Problem...\x02\x03",
            "#00204FThe general term for the problem in which\x01",
            "the Empire and Republic argue and dispute \x01",
            "about whose Crossbell belongs to...right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FYes, although that is a word that the\x01",
            "people living in Crossbell hardly use.\x02\x03",
            "#00103FDue to this problem, tensions\x01",
            "raised until just before a\x01",
            "real war suddenly broke out.\x02\x03",
            "#00108FTwo years ago, at Liberl,\x01",
            "by signing the "Non-Aggression Pact",\x01",
            "they only calmed down on the surface...\x02",
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
            "#12P#00106FI-I'm sorry!\x01",
            "I, of all people, said something impolite...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#11P#07003FNo...\x01",
            "What you said, Miss Elie,\x01",
            "is practically correct.\x02\x03",
            "#07000FThe Non-Aggression Pact proposed by my\x01",
            "dear grandmother...by Queen Alicia, was for not\x01",
            "allowing the two major powers to use military force.\x02\x03",
            "Because that, the Crossbell of those times was\x01",
            "released from a state of tension at its limit...\x02\x03",
            "#07003FOn the other hand, unforeseen pressure\x01",
            "from both countries raised and\x01",
            "Crossbell position is still critical...\x02\x03",
            "#07001FIn that sense, the Non-Aggression\x01",
            "Pact can't be said to have solved\x01",
            "the Crossbell Problem radically.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 500)

    ChrTalk(
        0x13,
        "#12P#07108FYour Highness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FB-But...\x01",
            "I don't think the Non-Aggression \x01",
            "Pact has been meaningless.\x02\x03",
            "#10103FI had just joined the CGF and at that time\x01",
            "there was an intimidating air due to the\x01",
            "large-scale military drills the Empire and\x01",
            "Republic performed at the borders...\x02\x03",
            "#10108FThen, I can't yet forget the terror\x01",
            "when the Empire "Railway Cannons"\x01",
            "were aimed at Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FYou've got a point...\x01",
            "If a war had broken out, serious damage\x01",
            "would've befallen the citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FIt means that even for just having\x01",
            "avoided that, it has been a very\x01",
            "valuable pact, right?\x02\x03",
            "#10300FWell, it's nothing Her Highness\x01",
            "should fret about, am I not right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FWazy, listen...\x01",
            "Don't you think you're too frank?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#11P#07009F*giggle*... Naturally, I\x01",
            "can't turn my back too.\x02\x03",
            "#07004FOn this occasion, the Trade Conference,\x01",
            "I want to create at all costs an opportunity\x01",
            "to talk together about Crossbell future.\x02\x03",
            "#07002FI came to visit this graveyard to\x01",
            "make sure of my determination.\x02\x03",
            "#07003FAlthough I ended up causing additional\x01",
            "work for Miss Julia and the bodyguards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#12P#07104FYour Highness...do not even mention it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FWhat can I say...\x01",
            "Your heart's strength is wonderful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FYes... I've really come to\x01",
            "envy the Liberl Kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#11P#07002F*giggle*, thank you very much.\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x13,
        "#12P#07100F...Your Highness, it's about the appointed time.\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x13, 500)

    ChrTalk(
        0x12,
        (
            "#5P#07005FOh, you're right.\x01",
            "We must head to\x01",
            "Orchis Tower...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8711():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8711)
    TurnDirection(0x13, 0x101, 500)

    ChrTalk(
        0x12,
        (
            "#11P#07004FThen, everyone from the SSS.\x01",
            "We will excuse us now.\x02\x03",
            "#07000FI heard that you are going to be\x01",
            "on guard duty at the conference...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes, we'll work trying\x01",
            "our utmost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#11P#07009F*giggle*, then, I will\x01",
            "be counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11P#07102FThen, ladies and gentlemen.\x01",
            "We will see each other at Orchis Tower next.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)

    def lambda_8883():

        label("loc_8883")

        TurnDirection(0x101, 0x12, 500)
        Yield()
        Jump("loc_8883")

    QueueWorkItem2(0x101, 2, lambda_8883)

    def lambda_8895():

        label("loc_8895")

        TurnDirection(0x102, 0x12, 500)
        Yield()
        Jump("loc_8895")

    QueueWorkItem2(0x102, 2, lambda_8895)

    def lambda_88A7():

        label("loc_88A7")

        TurnDirection(0x109, 0x12, 500)
        Yield()
        Jump("loc_88A7")

    QueueWorkItem2(0x109, 2, lambda_88A7)

    def lambda_88B9():

        label("loc_88B9")

        TurnDirection(0x105, 0x12, 500)
        Yield()
        Jump("loc_88B9")

    QueueWorkItem2(0x105, 2, lambda_88B9)

    def lambda_88CB():

        label("loc_88CB")

        TurnDirection(0x103, 0x12, 500)
        Yield()
        Jump("loc_88CB")

    QueueWorkItem2(0x103, 2, lambda_88CB)

    def lambda_88DD():

        label("loc_88DD")

        TurnDirection(0x104, 0x12, 500)
        Yield()
        Jump("loc_88DD")

    QueueWorkItem2(0x104, 2, lambda_88DD)
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

    # Function_22_737B end

    def Function_23_8963(): pass

    label("Function_23_8963")

    OP_95(0xFE, -2330, 4000, 42280, 2000, 0x0)
    OP_95(0xFE, -3140, 4000, 36010, 2000, 0x0)
    Return()

    # Function_23_8963 end

    def Function_24_898C(): pass

    label("Function_24_898C")

    Call(0, 25)
    Return()

    # Function_24_898C end

    def Function_25_8990(): pass

    label("Function_25_8990")

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
        "#6P#00005FMr. Arios...?\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xF, 0xB4, 0x1F4)

    ChrTalk(
        0xF,
        (
            "#11P#01400F...It's you.\x02\x03",
            "#01404FHmph...to think we'd meet here...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 7)), scpexpr(EXPR_END)), "loc_8E6C")

    ChrTalk(
        0x101,
        (
            "#6P#00000FIt seems that Mr. Michel\x01",
            "was looking for you\x01",
            "some time ago...\x02\x03",
            "#00003FWe heard you had been\x01",
            "called by the mayor,\x01",
            "Mr. Arios. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11P#01403F...Yeah.\x02\x03",
            "#01400FThat mayor is conscientious.\x01",
            "I said I didn't need any thanks,\x01",
            "but he wanted to at any costs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FHowever, I think that defending \x01",
            "Orchis Tower from the jaegers \x01",
            "was awesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FYeah, it seems that Crossbell\x01",
            "Times featured it too, it was\x01",
            "really an impressive feat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11P#01404FHu hu, I also had Dudley's\x01",
            "support back then...\x02\x03",
            "#01400F...Well, that matter too was\x01",
            "finished faster than I thought.\x02\x03",
            "So, since I was going back to the Guild,\x01",
            "I took the opportunity to stop by here.\x02\x03",
            "#01400FI'll apologize to Michel later\x01",
            "for having come back late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100F*giggle*, I think that would be nice.\x02\x03",
            "#00105F...Uhhm, today you seem to\x01",
            "have come to visit a grave...\x02\x03",
            "Could that grave be...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9027")

    label("loc_8E6C")


    ChrTalk(
        0x101,
        (
            "#6P#00000FNow that you mention it...\x01",
            "I read about your deed in front of\x01",
            "Orchis Tower in Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FIt said you challenged the Jaegers,\x01",
            "it was like a furious battle and so on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00302FYeah, quite the feat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11P#01404FHu hu, I also had Dudley's\x01",
            "support back then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100F*giggle*, please, don't be modest.\x02\x03",
            "#00105F...Uhhm, today you seem to\x01",
            "have come to visit a grave...\x02\x03",
            "Could that grave be...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9027")

    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_93(0xF, 0x0, 0x1F4)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#11P#01403F...Saya MacLaine.\x02\x03",
            "#01408FShe passed away five years ago in an accident...\x01",
            "She was Shizuku's mother.\x02",
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
        "#6P#00200FShizuku's mother...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00308FIf I remember correctly, little Shizuku\x01",
            "lost her sight in that accident...\x02",
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
        "#6P#10105F...Mr. Arios?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10305FIs something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11P#01404F...No, it's nothing.\x02\x03",
            "#01400F──I finished what I came to do.\x01",
            "It's time for me to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FAh...thank you for all your hard work.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)

    def lambda_92C6():

        label("loc_92C6")

        TurnDirection(0x101, 0xF, 500)
        Yield()
        Jump("loc_92C6")

    QueueWorkItem2(0x101, 2, lambda_92C6)

    def lambda_92D8():

        label("loc_92D8")

        TurnDirection(0x102, 0xF, 500)
        Yield()
        Jump("loc_92D8")

    QueueWorkItem2(0x102, 2, lambda_92D8)

    def lambda_92EA():

        label("loc_92EA")

        TurnDirection(0x109, 0xF, 500)
        Yield()
        Jump("loc_92EA")

    QueueWorkItem2(0x109, 2, lambda_92EA)

    def lambda_92FC():

        label("loc_92FC")

        TurnDirection(0x105, 0xF, 500)
        Yield()
        Jump("loc_92FC")

    QueueWorkItem2(0x105, 2, lambda_92FC)

    def lambda_930E():

        label("loc_930E")

        TurnDirection(0x103, 0xF, 500)
        Yield()
        Jump("loc_930E")

    QueueWorkItem2(0x103, 2, lambda_930E)

    def lambda_9320():

        label("loc_9320")

        TurnDirection(0x104, 0xF, 500)
        Yield()
        Jump("loc_9320")

    QueueWorkItem2(0x104, 2, lambda_9320)
    OP_68(20680, 700, 30630, 1000)

    def lambda_9343():
        OP_95(0xFE, 23250, 0, 30200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_9343)
    WaitChrThread(0xF, 1)
    OP_4B(0xF, 0xFF)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#12P#01401F──In the future, Crossbell will\x01",
            "undergo an unprecedented situation.\x02\x03",
            "#01403FHowever, no matter what circumstances,\x01",
            "no matter what trials will come...\x02\x03",
            "#01400FYou mustn't absolutely lose sight\x01",
            "of what is important to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00005FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10305F...?\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)

    def lambda_949A():
        OP_95(0xFE, 23250, 0, 16970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_949A)
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
        "#11P#00103F...He went away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00305FWhat could he have meant?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FW-Who knows...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FI didn't really understand, but...\x01",
            "Some kind of warning, perhaps?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00001F(...Mr. Arios...?)\x02",
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

    # Function_25_8990 end

    def Function_26_964D(): pass

    label("Function_26_964D")

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
        "............\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_9720")

    ChrTalk(
        0x101,
        (
            "#00000F(This man...\x01",
            "I think he's...Nielsen?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_973A")

    label("loc_9720")


    ChrTalk(
        0x101,
        "#00000F(This man...)\x02",
    )

    CloseMessageWindow()

    label("loc_973A")

    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "Well then...\x01",
            "TIme to go back, I guess.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "Hm, are you all here\x01",
            "to visit a grave too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Good morning.\x01",
            "I'll excuse myself now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_97E5():
        OP_95(0xFE, -20540, 0, 24610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_97E5)
    Sleep(500)

    def lambda_9802():

        label("loc_9802")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_9802")

    QueueWorkItem2(0x101, 1, lambda_9802)
    Sleep(50)

    def lambda_9817():

        label("loc_9817")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_9817")

    QueueWorkItem2(0x102, 1, lambda_9817)
    Sleep(50)

    def lambda_982C():

        label("loc_982C")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_982C")

    QueueWorkItem2(0x103, 1, lambda_982C)
    Sleep(50)

    def lambda_9841():

        label("loc_9841")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_9841")

    QueueWorkItem2(0x104, 1, lambda_9841)
    WaitChrThread(0xE, 1)
    OP_95(0xE, -15310, 0, 19380, 2000, 0x0)
    SetChrFlags(0xE, 0x80)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)

    def lambda_9880():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9880)
    Sleep(100)

    def lambda_9890():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9890)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_9963")

    ChrTalk(
        0x101,
        (
            "#00000FMr. Nielsen...\x01",
            "He came to visit my big brother's grave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHe seemed he was zealously praying...\x01",
            "Somehow like he was making a report?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, I wonder.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9A2A")

    label("loc_9963")

    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#00100FLloyd, do you know that man?\x02",
    )

    CloseMessageWindow()

    def lambda_9998():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9998)
    Sleep(50)

    def lambda_99A8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_99A8)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FNo...I have no idea.\x02\x03",
            "(Since he was visiting his grave, could\x01",
            "he have been big brother's acquaintance...?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A2A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -21160, 0, 21930, 135)
    SetScenarioFlags(0x19D, 4)
    EventEnd(0x5)
    Return()

    # Function_26_964D end

    def Function_27_9A50(): pass

    label("Function_27_9A50")

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
        "#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FMr. Nielsen...\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#5P...Hm, Mr. Lloyd, right?\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00108F#6PThis is...\x01",
            "Lloyd's older brother's grave...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYou came to visit my big\x01",
            "brother's grave, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PYes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PAlso, I had some things I wanted\x01",
            "to talk about to Mr. Guy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FTalking to my big brother...?\x02",
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
            "#5PThe raid incident, the national independence\x01",
            "declaration and this morning President's speech...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PThe feelings are many, and...\x01",
            "People are heading in one\x01",
            "direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PSo that's why...\x01",
            "I, conversely, decided to ponder\x01",
            "about a certain "darkness of the past".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F"Darkness of the past"...\x01",
            "...Could you mean...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PYes, about the murder case\x01",
            "of Detective Guy Bannings,\x01",
            "your elder brother.\x02",
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
        "#00105F#6PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#6PMr. Guy's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#6PThat's serious...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FNow of all times...?\x01",
            "No, it's because it is now, right?\x02\x03",
            "#00001FCould it be that you have found\x01",
            "something, Mr. Nielsen...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PHm...\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xE,
        "#11PMr. Lloyd, everybody too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PIf you feel inclined, would you change\x01",
            "place and verify the case with me?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 28)
    Return()

    # Function_27_9A50 end

    def Function_28_9FCD(): pass

    label("Function_28_9FCD")

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
            "Join in Nielsen's Verification\x01",      # 0
            "Think About It For Now\x01",              # 1
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
        (0, "loc_A053"),
        (1, "loc_A198"),
        (SWITCH_DEFAULT, "loc_A252"),
    )


    label("loc_A053")


    ChrTalk(
        0x101,
        (
            "#00003F............\x02\x03",
            "#00001FUnderstood.\x01",
            "By all means, please let us join.\x02",
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
            "Here it's not a good place.\x01",
            "Let's go back to the city for now.\x02",
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
            "Quest [Guy Bannings Murder Case Review]\x07\x00",
            " started!\x02",
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
    Jump("loc_A252")

    label("loc_A198")


    ChrTalk(
        0x101,
        (
            "#00003F...I'm sorry.\x01",
            "Can I think about it a little?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Yes, I don't mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'll be staying here for a while,\x01",
            "so please speak to me if you want.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A24A")
    OP_93(0xE, 0x0, 0x1F4)
    OP_4C(0xE, 0xFF)
    EventEnd(0x5)

    label("loc_A24A")

    SetScenarioFlags(0x19B, 6)
    Jump("loc_A252")

    label("loc_A252")

    Return()

    # Function_28_9FCD end

    def Function_29_A253(): pass

    label("Function_29_A253")

    TalkBegin(0xE)

    ChrTalk(
        0xE,
        "...Mr. Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If you feel inclined, would you change\x01",
            "place and verify the case with me?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Call(0, 28)
    TalkEnd(0xE)
    Return()

    # Function_29_A253 end

    SaveToFile()

Try(main)
