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
        "Function_5_1D85",         # 05, 5
        "Function_6_213C",         # 06, 6
        "Function_7_31F8",         # 07, 7
        "Function_8_3D1C",         # 08, 8
        "Function_9_42AD",         # 09, 9
        "Function_10_43EC",        # 0A, 10
        "Function_11_4519",        # 0B, 11
        "Function_12_4A84",        # 0C, 12
        "Function_13_4AE6",        # 0D, 13
        "Function_14_4BE0",        # 0E, 14
        "Function_15_4E21",        # 0F, 15
        "Function_16_5555",        # 10, 16
        "Function_17_5A55",        # 11, 17
        "Function_18_6244",        # 12, 18
        "Function_19_6366",        # 13, 19
        "Function_20_66B2",        # 14, 20
        "Function_21_69B5",        # 15, 21
        "Function_22_70ED",        # 16, 22
        "Function_23_852C",        # 17, 23
        "Function_24_8555",        # 18, 24
        "Function_25_8559",        # 19, 25
        "Function_26_91A1",        # 1A, 26
        "Function_27_9594",        # 1B, 27
        "Function_28_9AD0",        # 1C, 28
        "Function_29_9D4D",        # 1D, 29
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD6")

    ChrTalk(
        0xFE,
        (
            "Some time ago, policemen\x01",
            "came for an inquiry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ian doing such a monstrous\x01",
            "thing...? It's so absurd\x01",
            "that I can't believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYes, we feel the same too.\x02\x03",
            "#00003F(However, that's the truth. As\x01",
            "for his true motive, we can only\x01",
            "try asking the man himself.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_E65")

    label("loc_DD6")


    ChrTalk(
        0xFE,
        (
            "There's no way that Ian did such\x01",
            "a monstrous thing... It's so\x01",
            "absurd that I can't believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What could have ever\x01",
            "made him do that?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E65")

    Jump("loc_1D81")

    label("loc_E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_151B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B9")

    ChrTalk(
        0xFE,
        (
            "Just when that barrier\x01",
            "disappeared, the\x01",
            "unthinkable happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since the declaration of independence,\x01",
            "the amount of people coming to visit\x01",
            "their departed has decreased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can at least clean the\x01",
            "graves in a situation\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_14B4")
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)

    ChrTalk(
        0x101,
        (
            "#00003F...Excuse me.\x02\x03",
            "#00008FI was wondering whose\x01",
            "grave this is...\x02",
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
            "Well, I have no problem telling\x01",
            "you all. "He" too, seems to be\x01",
            "a gentle person, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FIs it anyone we know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The name the people\x01",
            "resting here share is...\x01",
            ""Grimwood".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In other words, they're\x01",
            "Mr. Ian Grimwood's\x01",
            "family.\x02",
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
        "...It's true.\x02",
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
            "On the weekends, he always\x01",
            "came to visit their grave\x01",
            "and remember his family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The gravestone has been damaged\x01",
            "by wind and rain, but he seems\x01",
            "to pray to it nonetheless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was asked to tidy it up\x01",
            "without actually repairing\x01",
            "it, so it ended up this way.\x02",
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
        (
            "#00308FThat lawyer has gone through\x01",
            "trials and tribulations of\x01",
            "his own too, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since the declaration, he\x01",
            "must've been busy and unable to\x01",
            "find the time to visit, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like, from now on, you\x01",
            "could come visit them as well. I'm\x01",
            "sure they too are lonely, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F............\x02\x03",
            "#00000F...Alright, I\x01",
            "understand.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 4)

    label("loc_14B4")

    Jump("loc_1516")

    label("loc_14B9")


    ChrTalk(
        0xFE,
        (
            "I can at least clean the\x01",
            "graves in a situation\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Be careful, everyone.\x02",
    )

    CloseMessageWindow()

    label("loc_1516")

    Jump("loc_1D81")

    label("loc_151B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1529")
    Jump("loc_1D81")

    label("loc_1529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_1740")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1679")

    ChrTalk(
        0xFE,
        (
            "Some time ago, Ian went\x01",
            "to the church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears he visited\x01",
            "the graves of Arios'\x01",
            "wife and Guy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0x101,
        (
            "#00005FUhhm... Is something\x01",
            "wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, nothing. It's not\x01",
            "important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems he's been busy lately,\x01",
            "so it'd be nice if this turned\x01",
            "out to be a good change of mood.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_173B")

    label("loc_1679")


    ChrTalk(
        0xFE,
        (
            "It appears that some time ago,\x01",
            "Mr. Ian went to visit the\x01",
            "graves of Arios' wife and Guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems he's been busy lately,\x01",
            "so it'd be nice if this turned\x01",
            "out to be a good change of mood.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_173B")

    Jump("loc_1D81")

    label("loc_1740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1905")
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
            "Naturally, pressure will\x01",
            "come from the Empire and\x01",
            "Republic, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want this independence to be\x01",
            "realized no matter what, for the\x01",
            "sake of the future young generation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1900")

    label("loc_1853")


    ChrTalk(
        0xFE,
        (
            "National independence\x01",
            "could be something\x01",
            "needed to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want this independence to be\x01",
            "realized no matter what, for the\x01",
            "sake of the future young generation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1900")

    Jump("loc_1D81")

    label("loc_1905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1913")
    Jump("loc_1D81")

    label("loc_1913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1921")
    Jump("loc_1D81")

    label("loc_1921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1AE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A3D")

    ChrTalk(
        0xFE,
        (
            "That madam who always comes to\x01",
            "visit a grave... It seems her\x01",
            "husband passed away in an accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It was a little before\x01",
            "hers, but I too lost my\x01",
            "family in an accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because the circumstances\x01",
            "are similar, it ended up\x01",
            "weighing on my mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1ADC")

    label("loc_1A3D")


    ChrTalk(
        0xFE,
        (
            "That madam's husband\x01",
            "seems to have passed\x01",
            "away in an accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, her family is abroad\x01",
            "and it seems they're living\x01",
            "happily... That's a relief.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ADC")

    Jump("loc_1D81")

    label("loc_1AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1AEF")
    Jump("loc_1D81")

    label("loc_1AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_1AFD")
    Jump("loc_1D81")

    label("loc_1AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_1CD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B18")
    Call(0, 5)
    Jump("loc_1CCB")

    label("loc_1B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C03")

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
            "He was quite the heavy drinker. I don't\x01",
            "know how many times I drank myself to\x01",
            "the point of nearly passing out\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CCB")

    label("loc_1C03")


    ChrTalk(
        0xFE,
        (
            "That Guy was quite the heavy drinker. I\x01",
            "don't know how many times I drank myself\x01",
            "to the point of nearly passing out\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "... One of my regrets is\x01",
            "that I wasn't able to\x01",
            "leave him under the table.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CCB")

    Jump("loc_1D81")

    label("loc_1CD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1D81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CEB")
    Call(0, 5)
    Jump("loc_1D81")

    label("loc_1CEB")


    ChrTalk(
        0xFE,
        (
            "I can usually be found\x01",
            "managing this graveyard.\x01",
            "Stop by whenever you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right, I'll remember\x01",
            "those times and tell you\x01",
            "stories about Guy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D81")

    TalkEnd(0xFE)
    Return()

    # Function_4_CA7 end

    def Function_5_1D85(): pass

    label("Function_5_1D85")

    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0x101, 0)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "Oh, Lloyd... Long time\x01",
            "no see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "When did you get back?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNot too long ago. It has\x01",
            "been a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FLloyd, who is this?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1E8B")

    ChrTalk(
        0x102,
        (
            "#00100FHaha. We became\x01",
            "acquainted through a\x01",
            "previous request.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E8B")


    ChrTalk(
        0x101,
        (
            "#00000FYeah... He's Mr. Quint, a drinking\x01",
            "buddy of my older brother's.\x02\x03",
            "#00004FHe's been good to me too. After the\x01",
            "cult incident, he told me many old\x01",
            "stories when we drank together.\x02",
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
            "But, since Lloyd can't drink\x01",
            "as much as Guy, it was a\x01",
            "little boring, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHaha... Sorry about\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHaha. We sat with you\x01",
            "both for that.\x02\x03",
            "#00109FBeing a minor though,\x01",
            "Tio had juice and looked\x01",
            "unhappy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe, I see.\x02\x03",
            "#10304FWell, please take good\x01",
            "care of us too from now\x01",
            "on, old man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes, your colleagues are\x01",
            "more than welcome to\x01",
            "join me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I can usually be found\x01",
            "managing this graveyard.\x01",
            "Stop by whenever you like.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x135, 4)
    Return()

    # Function_5_1D85 end

    def Function_6_213C(): pass

    label("Function_6_213C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2245")

    ChrTalk(
        0xFE,
        (
            "After those scary monsters in the\x01",
            "city disappeared, I was finally\x01",
            "able to visit this grave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was awfully uneasy, but\x01",
            "thinking about this deceased\x01",
            "man gave me courage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am sure you protected\x01",
            "me. Thank you, my\x01",
            "dear...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_22C7")

    label("loc_2245")


    ChrTalk(
        0xFE,
        (
            "Thinking about this\x01",
            "deceased man gave me\x01",
            "courage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am sure I'll be fine\x01",
            "whatever happens. I\x01",
            "can't lose, after all...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C7")

    Jump("loc_31F4")

    label("loc_22CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_22DA")
    Jump("loc_31F4")

    label("loc_22DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_243E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23A9")

    ChrTalk(
        0xFE,
        (
            "My son's family in\x01",
            "Remiferia was worried and\x01",
            "came for me this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They should have stayed\x01",
            "safe and left me\x01",
            "alone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, however... I\x01",
            "wonder why I'm so happy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2439")

    label("loc_23A9")


    ChrTalk(
        0xFE,
        (
            "My son's family in\x01",
            "Remiferia was worried and\x01",
            "came for me this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish they had stayed\x01",
            "safe, but... I wonder\x01",
            "why I'm so happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2439")

    Jump("loc_31F4")

    label("loc_243E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_25AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2510")

    ChrTalk(
        0xFE,
        (
            "The attack the other day\x01",
            "was frightening...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It reminded me of the\x01",
            "disputes 30 years ago\x01",
            "when I lost my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want to relive\x01",
            "that memory again...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)
    SetChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_25A7")

    label("loc_2510")


    ChrTalk(
        0xFE,
        (
            "In the attack the other day, I\x01",
            "was reminded of the disputes 30\x01",
            "years ago when I lost my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want to relive\x01",
            "that memory again...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25A7")

    Jump("loc_31F4")

    label("loc_25AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2627")

    ChrTalk(
        0xFE,
        (
            "To think such and\x01",
            "incident could happen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is just like during\x01",
            "the disputes. How\x01",
            "frightening...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F4")

    label("loc_2627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2635")
    Jump("loc_31F4")

    label("loc_2635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_26DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C6")

    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(It seems she's\x01",
            "fervently praying...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(We shouldn't disturb\x01",
            "her. Let's go.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_26D8")

    label("loc_26C6")


    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()

    label("loc_26D8")

    Jump("loc_31F4")

    label("loc_26DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_287E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27DE")

    ChrTalk(
        0xFE,
        (
            "It that bizarre monsters\x01",
            "have been spotted throughout\x01",
            "Crossbell recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems there have been calls\x01",
            "in the city not to recklessly\x01",
            "travel the highways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm really glad that the\x01",
            "graveyard is so near to\x01",
            "the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2879")

    label("loc_27DE")


    ChrTalk(
        0xFE,
        (
            "Even if it is outside the city,\x01",
            "the way to Crossbell Cathedral\x01",
            "is not so dangerous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm really glad that the\x01",
            "graveyard is so near to\x01",
            "the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2879")

    Jump("loc_31F4")

    label("loc_287E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_292B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28EB")

    ChrTalk(
        0xFE,
        "What a pretty sunset...\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x1F4)

    ChrTalk(
        0xFE,
        (
            "Haha. I'll come again\x01",
            "tomorrow, my dear.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2926")

    label("loc_28EB")


    ChrTalk(
        0xFE,
        (
            "It's already evening...\x01",
            "It is time for me to go\x01",
            "home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2926")

    Jump("loc_31F4")

    label("loc_292B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_2AF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A6E")

    ChrTalk(
        0xFE,
        (
            "Nowadays, as a modest hobby,\x01",
            "I have gotten into the habit\x01",
            "of reading before bed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The other day when I was buying\x01",
            "books, I ended up buying two\x01",
            "copies of the same one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Would you all like to\x01",
            "have one of them?\x02",
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
    Jump("loc_2AED")

    label("loc_2A6E")


    ChrTalk(
        0xFE,
        (
            "Lately I decided to pick\x01",
            "up an hobby, encouraged\x01",
            "by my son's family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. As I thought, you\x01",
            "need enjoyment in life.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AED")

    Jump("loc_31F4")

    label("loc_2AF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2CC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C19")

    ChrTalk(
        0xFE,
        (
            "Lately I received a\x01",
            "letter from my son's\x01",
            "family in Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was invited to come to\x01",
            "Remiferia since I live\x01",
            "alone here in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I cannot really\x01",
            "leave Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This place is packed with\x01",
            "important memories of my\x01",
            "late husband and I.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2CBB")

    label("loc_2C19")


    ChrTalk(
        0xFE,
        (
            "I was glad they invited me,\x01",
            "however... I have no intention\x01",
            "of leaving Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This place is packed with\x01",
            "important memories of my\x01",
            "late husband and I.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CBB")

    Jump("loc_31F4")

    label("loc_2CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2D5E")

    ChrTalk(
        0xFE,
        (
            "Princess Klaudia seems\x01",
            "to be a very kind\x01",
            "person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I saw Queen Alicia of Liberl\x01",
            "in a picture, and... Their\x01",
            "air is really quite similar.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F4")

    label("loc_2D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2E10")

    ChrTalk(
        0xFE,
        (
            "Orchis Tower, the building\x01",
            "that is the symbol of\x01",
            "Crossbell's new era...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If possible, I would have\x01",
            "liked to go see the unveiling\x01",
            "ceremony with my husband.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F4")

    label("loc_2E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2F9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F44")

    ChrTalk(
        0xFE,
        (
            "It seems the heads of state from\x01",
            "the Empire and Republic are coming\x01",
            "to the trade conference as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can feel that times have\x01",
            "changed, compared to when there\x01",
            "were nothing but disputes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope that a good era is\x01",
            "made, not with military\x01",
            "power, but through dialogue.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2F98")

    label("loc_2F44")


    ChrTalk(
        0xFE,
        (
            "I hope that a good era is\x01",
            "made, not with military\x01",
            "power, but through dialogue.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F98")

    Jump("loc_31F4")

    label("loc_2F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2FAB")
    Jump("loc_31F4")

    label("loc_2FAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_3096")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_303E")

    ChrTalk(
        0xFE,
        (
            "That sister over\x01",
            "there... Could she be\x01",
            "new?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha... She looks about the\x01",
            "age of my granddaughter in\x01",
            "Remiferia.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3091")

    label("loc_303E")


    ChrTalk(
        0xFE,
        (
            "I have a granddaughter in\x01",
            "Remiferia. I think she's\x01",
            "about that sister's age...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3091")

    Jump("loc_31F4")

    label("loc_3096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_30FD")

    ChrTalk(
        0xFE,
        (
            "My... The sun has gone\x01",
            "down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it is about time\x01",
            "I returned home as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F4")

    label("loc_30FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_31F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31AD")

    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "O-Oh, I am sorry. I\x01",
            "didn't notice you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was offering prayers\x01",
            "at my husband's grave...\x01",
            "Please, forgive me.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x0)
    SetScenarioFlags(0x0, 0)
    Jump("loc_31F4")

    label("loc_31AD")


    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F(...We shouldn't disturb\x01",
            "her. Let's go.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31F4")

    TalkEnd(0xFE)
    Return()

    # Function_6_213C end

    def Function_7_31F8(): pass

    label("Function_7_31F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3209")
    Jump("loc_3D18")

    label("loc_3209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3217")
    Jump("loc_3D18")

    label("loc_3217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3564")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34C5")

    ChrTalk(
        0xA,
        (
            "#04401FIt appears that jaegers\x01",
            "have deployed to an area\x01",
            "of the mountain path.\x02\x03",
            "#04403F...As a Gralsritter, I\x01",
            "can't act officially.\x02\x03",
            "#04408FI am terribly sorry, not\x01",
            "being able to assist you\x01",
            "in this terrible time...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3344")

    ChrTalk(
        0x103,
        (
            "#00200FBy the way, you're very\x01",
            "skilled, Ries.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3344")


    ChrTalk(
        0x102,
        (
            "#00108FIt's true that borrowing the\x01",
            "strength of a Gralsritter\x01",
            "would be reassuring, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301FWell, the jaegers on the\x01",
            "mountain path are probably\x01",
            "quite troublesome opponents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FRies, please wait here\x01",
            "in case something\x01",
            "happens.\x02\x03",
            "#00001FWe and the CGF will try\x01",
            "to do something about\x01",
            "Mainz matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04401F...I understand. Please,\x01",
            "be extremely careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_355F")

    label("loc_34C5")


    ChrTalk(
        0xA,
        (
            "#04401FIt appears that the jaegers\x01",
            "have deployed to an area of\x01",
            "the mountain path.\x02\x03",
            "#04403FAs a Gralsritter I can't\x01",
            "assist you... Please, be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_355F")

    Jump("loc_3D18")

    label("loc_3564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3572")
    Jump("loc_3D18")

    label("loc_3572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3667")

    ChrTalk(
        0xA,
        (
            "#04400FRegarding the "Pleroma Grass", I\x01",
            "intend to start an investigation as\x01",
            "well as soon as I contact the knights.\x02\x03",
            "#04403FI don't know how much I'll be able to\x01",
            "research alone, however... I'll\x01",
            "contact you if I learn anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D18")

    label("loc_3667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3A07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_398E")

    ChrTalk(
        0xA,
        "#04400FEveryone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FRies... So this is where\x01",
            "you were.\x02\x03",
            "#00004FThank you for the\x01",
            "valuable information you\x01",
            "gave us the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04404FDon't mention it. I'm\x01",
            "glad I could help.\x02\x03",
            "#04400FEveryone, where are you\x01",
            "heading now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, actually...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Elie explained that they\x01",
            "are going to the Doll\x01",
            "Studio.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#04405FRosenberg Studio...\x02\x03",
            "#04403FIf I recall, it's a place\x01",
            "recognised for having a\x01",
            "connection with Ouroboros.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FOh man, that's the\x01",
            "Gralsritter for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04403F...I heard that Jｶrg\x01",
            "Rosenberg is a man who knows\x01",
            "right from wrong, but...\x02\x03",
            "#04401FEven so, the fact remains\x01",
            "that he has ties to\x01",
            "Ouroboros.\x02\x03",
            "If you intend to meet him,\x01",
            "you should be very careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYes... That was the\x01",
            "plan. Thanks for the\x01",
            "warning.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16D, 2)
    Jump("loc_3A02")

    label("loc_398E")


    ChrTalk(
        0xA,
        (
            "#04400FIf you're going to the\x01",
            "Doll Studio, you should\x01",
            "prepare yourselves fully.\x02\x03",
            "#04403F...Please, be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A02")

    Jump("loc_3D18")

    label("loc_3A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_3A15")
    Jump("loc_3D18")

    label("loc_3A15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_3A23")
    Jump("loc_3D18")

    label("loc_3A23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3A31")
    Jump("loc_3D18")

    label("loc_3A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3A3F")
    Jump("loc_3D18")

    label("loc_3A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3A4D")
    Jump("loc_3D18")

    label("loc_3A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3A5B")
    Jump("loc_3D18")

    label("loc_3A5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3A69")
    Jump("loc_3D18")

    label("loc_3A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_3D01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A88")
    TalkEnd(0xFE)
    Call(0, 8)
    Return()

    label("loc_3A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C8C")

    ChrTalk(
        0xA,
        (
            "#13800FAfter I finish my worship at the\x01",
            "memorial monument, I must learn\x01",
            "my job duties from my seniors.\x02\x03",
            "#13804FIt seems there are many things\x01",
            "to do when you take up a new\x01",
            "post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FAh... Could it be that\x01",
            "we got in your way...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#13800FNo, not at all... I also\x01",
            "got to meet KeA.\x02\x03",
            "#13803F...More importantly, I've\x01",
            "gotten hungry for some\x01",
            "reason.\x02\x03",
            "#13802FI want to hurry back to\x01",
            "the dorm and eat the bread\x01",
            "I bought at the bakery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F(*giggle*, it seems\x01",
            "she's still a glutton.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3CFC")

    label("loc_3C8C")


    ChrTalk(
        0xA,
        (
            "#13800FI will be in the care of\x01",
            "this cathedral for a\x01",
            "little while.\x02\x03",
            "Please come visit me\x01",
            "anytime you need.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CFC")

    Jump("loc_3D18")

    label("loc_3D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_3D0F")
    Jump("loc_3D18")

    label("loc_3D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3D18")

    label("loc_3D18")

    TalkEnd(0xFE)
    Return()

    # Function_7_31F8 end

    def Function_8_3D1C(): pass

    label("Function_8_3D1C")

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
            "#11P#13800FAah, everyone... Thank\x01",
            "you for before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FRies. It seems you're\x01",
            "through with your\x01",
            "introductions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#13804FYes, I just finished\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x153, 500)

    ChrTalk(
        0xA,
        (
            "#11P#13800F...Is she the girl you\x01",
            "were talking about\x01",
            "before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes. This is KeA.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01105FMiss, could you be a new\x01",
            "sister?\x02\x03",
            "#01109FEhehe, hello!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        "#11P#13802F...How cute...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F*giggle*, I know, right?\x01",
            "Also, she's a very good\x01",
            "girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00009FShe often helps us\x01",
            "preparing meals... She's\x01",
            "really a great help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10306FMan. You'll even show\x01",
            "what doting parents you\x01",
            "are in this situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FAhaha... I understand\x01",
            "how they feel, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#12P#01111FHuuuh?\x02",
    )

    CloseMessageWindow()

    def lambda_40BA():
        TurnDirection(0x101, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_40BA)
    Sleep(50)

    def lambda_40CA():
        TurnDirection(0x105, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_40CA)
    Sleep(50)

    def lambda_40DA():
        TurnDirection(0x102, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_40DA)
    Sleep(50)

    def lambda_40EA():
        TurnDirection(0x109, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_40EA)
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
            "#11P#13803F(...I see, so this girl\x01",
            "is that cult's...)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_41A5():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_41A5)
    Sleep(50)

    def lambda_41B5():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_41B5)
    Sleep(50)

    def lambda_41C5():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_41C5)
    Sleep(50)

    def lambda_41D5():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_41D5)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        (
            "#00105FUmm, Ries? Is something\x01",
            "wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#13803F...No, it's nothing.\x02\x03",
            "#13802FNice to meet you, KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#12P#01109FYeah, nice to meet you\x01",
            "too!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x135, 5)
    SetChrPos(0x0, 0, 4000, 40000, 180)
    EventEnd(0x5)
    Return()

    # Function_8_3D1C end

    def Function_9_42AD(): pass

    label("Function_9_42AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_438C")

    ChrTalk(
        0xFE,
        (
            "Oh, you're... The Special Support\x01",
            "Section people who visited the\x01",
            "Arseille last night, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crown Princess Klaudia\x01",
            "and Captain Julia are\x01",
            "further ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please pass through, if\x01",
            "you like.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43E8")

    label("loc_438C")


    ChrTalk(
        0xFE,
        (
            "Crown Princess Klaudia\x01",
            "and Captain Julia are\x01",
            "further ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please, pass through.\x02",
    )

    CloseMessageWindow()

    label("loc_43E8")

    TalkEnd(0xFE)
    Return()

    # Function_9_42AD end

    def Function_10_43EC(): pass

    label("Function_10_43EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44A8")

    ChrTalk(
        0xFE,
        (
            "As expected, I think there wouldn't\x01",
            "be anyone trying to cause a ruckus\x01",
            "in a graveyard, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The unexpected can\x01",
            "happen. I must maintain\x01",
            "proper lookout.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4515")

    label("loc_44A8")


    ChrTalk(
        0xFE,
        (
            "We are her minimum\x01",
            "required guard... This is\x01",
            "a grave responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must keep a proper\x01",
            "lookout.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4515")

    TalkEnd(0xFE)
    Return()

    # Function_10_43EC end

    def Function_11_4519(): pass

    label("Function_11_4519")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49FB")

    ChrTalk(
        0xFE,
        (
            "...Oh, guys. What an\x01",
            "unexpected meeting.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47B2")

    ChrTalk(
        0x101,
        (
            "#00003FIt seems you were\x01",
            "visiting a grave.\x01",
            "...Please excuse us.\x02\x03",
            "#00000F...Could it be that the\x01",
            "one resting here is...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F1st Lt. Ozma Seeker... He's\x01",
            "Fran and I's dad. He passed\x01",
            "away about 10 years ago.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_465B")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_465B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_467E")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_467E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46A1")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_46A1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46C1")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_46C1")

    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105FNoｱl's father...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FI only heard stories\x01",
            "about him... It seems he\x01",
            "was an excellent officer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FWow, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He had a strong sense of justice\x01",
            "and was a strict man... It\x01",
            "happened in the line of duty.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4884")

    label("loc_47B2")


    ChrTalk(
        0x101,
        (
            "#00003FIt seems you were\x01",
            "visiting a grave.\x01",
            "...Please excuse us.\x02\x03",
            "#00008F...If I remember\x01",
            "correctly, the one\x01",
            "resting here is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F...Yes, he's Fran and\x01",
            "I's dad. He passed away\x01",
            "about 10 years ago.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4884")


    ChrTalk(
        0xFE,
        (
            "...Since his job was that of a CGF member, we\x01",
            "should have been prepared for it, but... As\x01",
            "you can expect, back then we couldn't bear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. It happened a long\x01",
            "time ago. Please don't\x01",
            "be so sad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...However, you all must\x01",
            "regard your lives as\x01",
            "precious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you were to pass\x01",
            "away, a great number of\x01",
            "people would feel sad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10104F...Yes, I know.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 3)
    Jump("loc_4A80")

    label("loc_49FB")


    ChrTalk(
        0xFE,
        (
            "...However, you all must\x01",
            "regard your lives as\x01",
            "precious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you were to pass\x01",
            "away, a great number of\x01",
            "people would feel sad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A80")

    TalkEnd(0xFE)
    Return()

    # Function_11_4519 end

    def Function_12_4A84(): pass

    label("Function_12_4A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4ADF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AAD")
    Call(0, 26)
    Return()

    label("loc_4AAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4AC4")
    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Jump("loc_4ADA")

    label("loc_4AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 6)), scpexpr(EXPR_END)), "loc_4AD6")
    Call(0, 29)
    Return()

    label("loc_4AD6")

    Call(0, 27)
    Return()

    label("loc_4ADA")

    Jump("loc_4AE5")

    label("loc_4ADF")

    TalkBegin(0xFE)
    TalkEnd(0xFE)

    label("loc_4AE5")

    Return()

    # Function_12_4A84 end

    def Function_13_4AE6(): pass

    label("Function_13_4AE6")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "O, lambs born beneath\x01",
            "the bell, please, sleep\x01",
            "peacefully.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "From pure white clouds, let the golden\x01",
            "shining sun become a straight path to the\x01",
            "clear blue sky, guiding souls to the Goddess.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_4AE6 end

    def Function_14_4BE0(): pass

    label("Function_14_4BE0")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "Ozma Seeker\x01",
            "Sleeps Here\x01",
            "───────────────\x01",
            "S1157 - S1194\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E1D")

    ChrTalk(
        0x101,
        (
            "#00005FSeeker, it says... Could\x01",
            "it be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F1st Lt. Ozma Seeker... He's\x01",
            "Fran and I's dad. He passed\x01",
            "away about 10 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FNoｱl's father...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FHmm, it's the first I've\x01",
            "heard of this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha, I'm not the type to talk\x01",
            "about this kind of thing.\x02\x03",
            "#10104F...Let's go, everyone. We'd\x01",
            "probably get scolded by my dad for\x01",
            "loitering in a place like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FI see. Let's go, then.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 2)

    label("loc_4E1D")

    TalkEnd(0xFF)
    Return()

    # Function_14_4BE0 end

    def Function_15_4E21(): pass

    label("Function_15_4E21")

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
            "        S1176 - S1201\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F77")

    ChrTalk(
        0x153,
        (
            "#01105F(...The man of this\x01",
            "grave...)\x02\x03",
            "#01103F...............\x02",
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
            "KeA joined her hand in\x01",
            "silence.\x07\x00\x02",
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
        "#00002FHaha...thanks.\x02",
    )

    CloseMessageWindow()

    label("loc_4F77")

    TalkEnd(0xFF)
    Return()

    label("loc_4F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_503E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 6)), scpexpr(EXPR_END)), "loc_4FD2")

    ChrTalk(
        0x101,
        (
            "#00000FThis bouquet... Arios\x01",
            "probably offered it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5036")

    label("loc_4FD2")


    ChrTalk(
        0x101,
        (
            "#00005FOh... It seems someone\x01",
            "offered a bouquet of\x01",
            "flowers.\x02\x03",
            "#00003FWho could it have\x01",
            "been...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5036")

    SetScenarioFlags(0x0, 6)
    Jump("loc_5073")

    label("loc_503E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_505D")
    TalkEnd(0xFF)
    Call(0, 17)
    Return()

    label("loc_505D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5073")
    TalkEnd(0xFF)
    Call(0, 16)
    Return()

    label("loc_5073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_548B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_541A")

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
            "#00000FHaha, well... Arios told me\x01",
            "about my big brother's last\x01",
            "moments...\x02\x03",
            "#00004FReally, he worried about me\x01",
            "and Cecil until the very\x01",
            "end...\x02\x03",
            "Furthermore, he didn't bear\x01",
            "the slightest grudge against\x01",
            "Arios and Lawyer Ian...\x02\x03",
            "#00000FHonestly, how softhearted a\x01",
            "person was he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F...Haha, rest assured.\x02\x03",
            "#00302FYou have plenty of that\x01",
            "side of him too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5267")

    ChrTalk(
        0x10A,
        "#00604FHmph... Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_52C7")

    label("loc_5267")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5299")

    ChrTalk(
        0x109,
        "#10102FHaha, certainly.\x02",
    )

    CloseMessageWindow()
    Jump("loc_52C7")

    label("loc_5299")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52C7")

    ChrTalk(
        0x105,
        "#10402FAhaha, of course.\x02",
    )

    CloseMessageWindow()

    label("loc_52C7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5303")

    ChrTalk(
        0x106,
        (
            "#10702F*chuckle chuckle*...\x01",
            "True.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5361")

    label("loc_5303")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_532D")

    ChrTalk(
        0x105,
        "#10404FWord up.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5361")

    label("loc_532D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5361")

    ChrTalk(
        0x109,
        "#10102FHaha, you can say that.\x02",
    )

    CloseMessageWindow()

    label("loc_5361")


    ChrTalk(
        0x101,
        (
            "#00012FH-Hey now. ...Haha, oh,\x01",
            "well.\x02\x03",
            "#00000FIn any case... All that\x01",
            "remains is to save KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, let's go, without\x01",
            "letting our guards down\x01",
            "until the very end.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 5)
    Jump("loc_5486")

    label("loc_541A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5486")

    ChrTalk(
        0x101,
        (
            "#00000F...What remains is only\x01",
            "to save KeA.\x02\x03",
            "#00004FBig brother, please...\x01",
            "Watch over me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_5486")

    Jump("loc_5551")

    label("loc_548B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_54AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54A5")
    TalkEnd(0xFF)
    Call(0, 21)
    Return()

    label("loc_54A5")

    Jump("loc_5551")

    label("loc_54AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5551")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5551")

    ChrTalk(
        0x101,
        (
            "#00000F(Big brother... I've come\x01",
            "back to Crossbell.)\x02\x03",
            "#00004F(I'm going to get back KeA\x01",
            "no matter what it takes.\x01",
            "Please, watch over me...!)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_5551")

    TalkEnd(0xFF)
    Return()

    # Function_15_4E21 end

    def Function_16_5555(): pass

    label("Function_16_5555")

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
            "#00003FGuy Bannings... My big\x01",
            "brother who died in the\x01",
            "line of duty 3 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FI heard he was a remarkable\x01",
            "detective, one of the best\x01",
            "among the police.\x02\x03",
            "#10104FEven in the CGF, they are\x01",
            "few who don't know his\x01",
            "name.\x02",
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
            "#00000FIt seems he was originally Chief\x01",
            "Sergei's subordinate and Arios'\x01",
            "partner...\x02\x03",
            "#00003FStuff happened and that group\x01",
            "disbanded. But even after that, he\x01",
            "was Dudley's rival in Section One.\x02\x03",
            "#00009FIf nothing else, he's certainly\x01",
            "well known since he poked his nose\x01",
            "into many different areas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104FThe more I learn about\x01",
            "him, the more amazing he\x01",
            "seems...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FA detective who faced many of\x01",
            "Crossbell's barriers with\x01",
            "unusual energy...\x02\x03",
            "#00008F...To think someone like that\x01",
            "was killed in the line of duty.\x01",
            "I could hardly believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FIn the end, that cult\x01",
            "didn't murder your\x01",
            "brother, did they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FNo... The truth is still\x01",
            "a mystery.\x02\x03",
            "#00003F(But one day, I'll seize\x01",
            "the truth with my own\x01",
            "two hands.)\x02\x03",
            "#00000F(It might take a while\x01",
            "longer though. Wait for\x01",
            "me, Guy.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -22640, 0, 23360, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x136, 0)
    EventEnd(0x5)
    Return()

    # Function_16_5555 end

    def Function_17_5A55(): pass

    label("Function_17_5A55")

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
            "#10305F#12P...That's right...\x02\x03",
            "#10303FI heard Lloyd's\x01",
            "brother's grave was\x01",
            "here, but...\x02\x03",
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
        (
            "#00305F#6PNow that you mention\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PThey're both already\x01",
            "gone, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00004F#11PYeah, 15 years ago.\x02\x03",
            "#00008FTo be honest, I don't remember them\x01",
            "that well because I was very young.\x02\x03",
            "#00000FI heard it was because of an accident\x01",
            "involving a newly commissioned orbal\x01",
            "airship they were on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PAn airship accident...\x01",
            "So that's what it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#6PAirships had just been\x01",
            "developed so they were\x01",
            "still unreliable...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PYeah. In the end, it fell\x01",
            "in a mountainous region and\x01",
            "no remains were found...\x02\x03",
            "#00008FIt looked like it was\x01",
            "really hard on my brother,\x01",
            "too.\x02\x03",
            "#00002FOn top of that, he still\x01",
            "had to support an annoying\x01",
            "younger brother...\x02\x03",
            "#00012F...Haha... Honestly, I'll\x01",
            "never be able to repay him.\x02",
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
            "#00304F#6PWell, your big bro probably\x01",
            "never thought of it that\x01",
            "way even once, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#12PRight...\x02\x03",
            "#00214FWhen he spoke about you,\x01",
            "he said you had a cute\x01",
            "and helpless aura...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PAhaha, I can understand\x01",
            "how he felt.\x02\x03",
            "#10309FA three-year-old Lloyd,\x01",
            "eh? You must've been\x01",
            "adorable㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#6PI-I can imagine...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#6PSo cute you'd just want\x01",
            "to hold him, maybe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#6PYeah, I can easily\x01",
            "imagine it!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_61A3")

    ChrTalk(
        0x101,
        (
            "#00011F#11PS-Stop teasing me.\x02\x03",
            "#00004F─Sorry to have wasted\x01",
            "our time. We've got to\x01",
            "go to Ries' place.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6215")

    label("loc_61A3")


    ChrTalk(
        0x101,
        (
            "#00011F#11PS-Stop teasing me.\x02\x03",
            "#00004F─Sorry to have wasted\x01",
            "our time. Anyway, let's\x01",
            "go to the cathedral.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6215")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -22640, 0, 23360, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x17C, 6)
    EventEnd(0x5)
    Return()

    # Function_17_5A55 end

    def Function_18_6244(): pass

    label("Function_18_6244")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6350")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_634B")

    ChrTalk(
        0x153,
        (
            "#01108FThis grave is...\x02\x03",
            "#01100FLloyd, let's pay our\x01",
            "respects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F...Yeah, that's right.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_634B")

    Jump("loc_6362")

    label("loc_6350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6362")
    Call(0, 19)

    label("loc_6362")

    TalkEnd(0xFF)
    Return()

    # Function_18_6244 end

    def Function_19_6366(): pass

    label("Function_19_6366")

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
            "#12P#10105FThe name on this\x01",
            "grave... I think I've\x01",
            "heard it somewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FThe Divine Blade of Wind,\x01",
            "Arios MacLaine.\x02\x03",
            "#00003FI've never heard it directly\x01",
            "from him, but I think this\x01",
            "is his wife's grave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FIf I remember correctly,\x01",
            "she died in an\x01",
            "accident...\x02\x03",
            "#00103FShizuku was with her and\x01",
            "escaped death, but ended\x01",
            "up losing her sight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, and then Arios\x01",
            "quit the police and\x01",
            "became a Bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FHmm, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FIt's almost too much to\x01",
            "bear...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F...There's still hope.\x02\x03",
            "#00004FIt may still be possible\x01",
            "to restore Shizuku's\x01",
            "sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FRight... I hope we can\x01",
            "pay her a visit before\x01",
            "long...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 20740, 0, 31990, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x135, 7)
    EventEnd(0x5)
    Return()

    # Function_19_6366 end

    def Function_20_66B2(): pass

    label("Function_20_66B2")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "...... ...\x01",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_689A")

    ChrTalk(
        0x101,
        (
            "#00001FIt's a completely ruined\x01",
            "grave. The letters are\x01",
            "weathered and worn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FWell, it seems it's\x01",
            "impossible to decipher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FDecipher... It's not a\x01",
            "coded puzzle, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FI don't know whose grave\x01",
            "it is, but... It seems\x01",
            "it's been well maintained.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FShould we pay our\x01",
            "respects?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x135, 6)

    label("loc_689A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 4)), scpexpr(EXPR_END)), "loc_69B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_691C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6917")

    ChrTalk(
        0x101,
        (
            "#00001F(This grave belongs to\x01",
            "Lawyer Ian's wife and\x01",
            "child...)\x02\x03",
            "#00003F(...Let's go now.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_6917")

    Jump("loc_69B1")

    label("loc_691C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_69B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69B1")

    ChrTalk(
        0x101,
        (
            "#00001F(This grave belongs to\x01",
            "Lawyer Ian's wife and\x01",
            "child...)\x02\x03",
            "#00008F(Lawyer Ian... He never\x01",
            "said anything even\x01",
            "once...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_69B1")

    TalkEnd(0xFF)
    Return()

    # Function_20_66B2 end

    def Function_21_69B5(): pass

    label("Function_21_69B5")

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
        "#00008F...............\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6AE3")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6AE3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B03")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6B03")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B23")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6B23")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B43")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6B43")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B63")
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6B63")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B83")
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6B83")

    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#12P#00108FYour older brother's tonfas...\x01",
            "They're so full of cuts that\x01",
            "somehow it's pitiful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FProbably stuff from when\x01",
            "he went at it with ol'\x01",
            "man Arios...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FYeah...\x02\x03",
            "#00000F...However, if you look carefully,\x01",
            "aside from those there're a lot of\x01",
            "smaller scratches.\x02\x03",
            "It also seems there're even traces\x01",
            "of repeated repairs.\x02\x03",
            "#00004FMy big brother who seeked the\x01",
            "truth without giving up, no matter\x01",
            "the Barriers he faced...\x02\x03",
            "The aspect of these tonfas is for\x01",
            "sure my big brother very own way\x01",
            "to live.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DC6")

    ChrTalk(
        0x10A,
        "#6P#00604F...It could be.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E25")

    label("loc_6DC6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DFC")

    ChrTalk(
        0x109,
        "#6P#10100F...That could be.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E25")

    label("loc_6DFC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E25")

    ChrTalk(
        0x105,
        "#6P#10400F...Maybe.\x02",
    )

    CloseMessageWindow()

    label("loc_6E25")

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
            "#00008FThis incident and also my big\x01",
            "brother's incident...\x02\x03",
            "#00001FTo reach that truth, we must\x01",
            "overcome Mr. Arios... And\x01",
            "Lawyer Ian too.\x02\x03",
            "#00004FI'll borrow these tonfas for a\x01",
            "little while. ...Big brother,\x01",
            "please, give us your strength.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6F78")

    ChrTalk(
        0x106,
        "#6P#10710FLloyd...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6FCD")

    label("loc_6F78")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6FA5")

    ChrTalk(
        0x105,
        "#6P#10400FLloyd...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6FCD")

    label("loc_6FA5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6FCD")

    ChrTalk(
        0x109,
        "#6P#10100FLloyd...\x02",
    )

    CloseMessageWindow()

    label("loc_6FCD")


    ChrTalk(
        0x103,
        (
            "#6P#00204FNaturally, we will help\x01",
            "you too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00309FHaha, that's for sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FEveryone, let's combine\x01",
            "our strengths... To take\x01",
            "back KeA.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5P#00000FYeah... Everyone, once\x01",
            "again, I'm counting on\x01",
            "you!\x02",
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

    # Function_21_69B5 end

    def Function_22_70ED(): pass

    label("Function_22_70ED")

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
            "#5P#07000FThat reminds me, Julia...\x02\x03",
            "It seems "she" was\x01",
            "appointed to this cathedral\x01",
            "a little while ago.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 500)

    ChrTalk(
        0x13,
        (
            "#12P#07100FYes. According to\x01",
            "another sister, she's\x01",
            "out today, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5P#07003FI see...\x02\x03",
            "#07008FShe was a great help to me\x01",
            "back then. I would have liked\x01",
            "to see her if possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#N#00005FYour Highness...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        "#12P#N#10105FAnd Captain Julia!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7398():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_7398)
    Sleep(50)

    def lambda_73A8():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_73A8)
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
        "#12P#07102FLooks like it's them.\x02",
    )

    CloseMessageWindow()
    OP_68(860, 5100, 39660, 3000)
    MoveCamera(320, 19, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14870, 3000)

    def lambda_742A():
        OP_95(0xFE, 380, 4000, 38790, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_742A)

    def lambda_7444():
        OP_95(0xFE, 2620, 4000, 38580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7444)

    def lambda_745E():
        OP_95(0xFE, -820, 4000, 37680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_745E)

    def lambda_7478():
        OP_95(0xFE, 2009, 4000, 36940, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7478)

    def lambda_7492():
        OP_95(0xFE, 560, 4000, 36330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7492)

    def lambda_74AC():
        OP_95(0xFE, -1060, 4000, 36090, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_74AC)
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
            "#11P#07002FEveryone... Haha, we\x01",
            "meet again.\x02\x03",
            "#07009FI thought you would be\x01",
            "coming around now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FHuh? You knew we were\x01",
            "coming?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11P#07102FAs we speak, Sieg is\x01",
            "circling the skies, keeping\x01",
            "watch over this area.\x02\x03",
            "He told us you would be\x01",
            "coming a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FHe's that white falcon\x01",
            "we met yesterday... Wow,\x01",
            "he's amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#11P#07004FHaha. Sieg is a\x01",
            "messenger of the Royal\x01",
            "Guard, you know.\x02\x03",
            "#07000FUmm, so... Why are you\x01",
            "all here?\x02\x03",
            "#07005FOh, and there's even\x01",
            "someone new today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FHello. I'm Tio Plato. I\x01",
            "returned to the Special\x01",
            "Support Section last night.\x02\x03",
            "#00204FIt is an honor meeting you\x01",
            "like this.\x02",
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
            "#6P#00300FWell, we were just\x01",
            "casually droppin' by,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHehe. I never thought\x01",
            "we'd see you again so\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYour Highness, are you\x01",
            "here to pray?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#11P#07000FYes...\x02\x03",
            "#07003FThe great number of people\x01",
            "who passed away in Crossbell\x01",
            "now rest in this graveyard.\x02\x03",
            "That's why I had to come\x01",
            "here in advance of the\x01",
            "conference.\x02\x03",
            "#07008FTo put an end to the\x01",
            "Crossbell Problem, once and\x01",
            "for all as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FThe Crossbell Problem...\x02\x03",
            "#00204FA general term for the dispute between\x01",
            "the Empire and Republic over which has\x01",
            "the right to control Crossbell, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FYes. Crossbell natives hardly ever use\x01",
            "the term, though.\x02\x03",
            "#00103FIt's because of this problem that\x01",
            "tensions escalated to the brink of war.\x02\x03",
            "#00108FAlthough because of the signing of the\x01",
            "Non-Aggression Pact two years ago, those\x01",
            "tensions calmed down on the surface...\x02",
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
            "#12P#00106FI-I'm sorry! I, of all\x01",
            "people, said something\x01",
            "impolite...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#11P#07003FNo... What you said is basically correct.\x02\x03",
            "#07000FThe treaty proposed by my grandmother, Queen\x01",
            "Alicia, was to prevent the major powers from\x01",
            "using military force.\x02\x03",
            "At the time, the extreme tension was\x01",
            "released, but...\x02\x03",
            "#07003FOn the other hand, unseen pressure from both\x01",
            "nations began to build, and even now,\x01",
            "Crossbell remains in a dangerous position...\x02\x03",
            "#07001FIn that sense, I can't say the treaty\x01",
            "fundamentally solved the Crossbell Problem.\x02",
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
            "#6P#10101FB-But... I don't think the non-aggression pact\x01",
            "was meaningless.\x02\x03",
            "#10103FI had just joined the CGF, and we were\x01",
            "intimidated by Imperial and Republican military\x01",
            "exercises being conducted near the borders...\x02\x03",
            "#10108FAnd we still can't forget the terror when the\x01",
            "Imperial Railway Cannons were pointed at\x01",
            "Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FYou've got a point there... If a\x01",
            "war had broken out, there would've\x01",
            "been enormous citizen casualties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FI guess it was a\x01",
            "valuable treaty on that\x01",
            "account alone.\x02\x03",
            "#10300FWell, it's nothing Your\x01",
            "Highness need worry\x01",
            "about, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FNow look here Wazy...\x01",
            "You're obviously being\x01",
            "way too honest with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#11P#07009FHaha... Of course, I mustn't be\x01",
            "pessimistic.\x02\x03",
            "#07004FI must do whatever it takes to turn\x01",
            "this trade conference into a chance\x01",
            "to discuss Crossbell's future.\x02\x03",
            "#07002FI came to this graveyard to\x01",
            "strengthen my resolve.\x02\x03",
            "#07003FAlthough I ended up making more\x01",
            "work for Julia and the other\x01",
            "guards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12P#07104FYour Highness... Don't\x01",
            "be ridiculous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FWhat can I say... I\x01",
            "should have known your\x01",
            "heart was this strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FYes... I'm really quite\x01",
            "jealous of Liberl\x01",
            "Kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#11P#07002FHaha, thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x13,
        (
            "#12P#07100F...Your Highness, it's\x01",
            "almost time.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x13, 500)

    ChrTalk(
        0x12,
        (
            "#5P#07005FAh, yes. It's about time\x01",
            "I headed for Orchis\x01",
            "Tower...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_82FA():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_82FA)
    TurnDirection(0x13, 0x101, 500)

    ChrTalk(
        0x12,
        (
            "#11P#07004FWell then, everyone.\x01",
            "Please excuse us.\x02\x03",
            "#07000FI heard you all were\x01",
            "participating in today's\x01",
            "security detail, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes, we'll do our very\x01",
            "best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#11P#07009FHaha. Then, I'll be\x01",
            "counting on all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11P#07102FLadies and gentlemen.\x01",
            "I'll see you next at\x01",
            "Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)

    def lambda_844C():

        label("loc_844C")

        TurnDirection(0x101, 0x12, 500)
        Yield()
        Jump("loc_844C")

    QueueWorkItem2(0x101, 2, lambda_844C)

    def lambda_845E():

        label("loc_845E")

        TurnDirection(0x102, 0x12, 500)
        Yield()
        Jump("loc_845E")

    QueueWorkItem2(0x102, 2, lambda_845E)

    def lambda_8470():

        label("loc_8470")

        TurnDirection(0x109, 0x12, 500)
        Yield()
        Jump("loc_8470")

    QueueWorkItem2(0x109, 2, lambda_8470)

    def lambda_8482():

        label("loc_8482")

        TurnDirection(0x105, 0x12, 500)
        Yield()
        Jump("loc_8482")

    QueueWorkItem2(0x105, 2, lambda_8482)

    def lambda_8494():

        label("loc_8494")

        TurnDirection(0x103, 0x12, 500)
        Yield()
        Jump("loc_8494")

    QueueWorkItem2(0x103, 2, lambda_8494)

    def lambda_84A6():

        label("loc_84A6")

        TurnDirection(0x104, 0x12, 500)
        Yield()
        Jump("loc_84A6")

    QueueWorkItem2(0x104, 2, lambda_84A6)
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

    # Function_22_70ED end

    def Function_23_852C(): pass

    label("Function_23_852C")

    OP_95(0xFE, -2330, 4000, 42280, 2000, 0x0)
    OP_95(0xFE, -3140, 4000, 36010, 2000, 0x0)
    Return()

    # Function_23_852C end

    def Function_24_8555(): pass

    label("Function_24_8555")

    Call(0, 25)
    Return()

    # Function_24_8555 end

    def Function_25_8559(): pass

    label("Function_25_8559")

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
        "#6P#00005FArios?\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xF, 0xB4, 0x1F4)

    ChrTalk(
        0xF,
        (
            "#11P#01400FYou guys, huh.\x02\x03",
            "#01404FHmph... Fancy meeting\x01",
            "you here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 7)), scpexpr(EXPR_END)), "loc_89E1")

    ChrTalk(
        0x101,
        (
            "#6P#00000FIt seems like Michel has\x01",
            "been looking for you for\x01",
            "some time.\x02\x03",
            "#00003FWe heard you were called\x01",
            "by the mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11P#01403F...I guess.\x02\x03",
            "#01400FThat mayor is conscientious.\x01",
            "I said I didn't need his\x01",
            "thanks, but he insisted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FBut, I think it's pretty amazing\x01",
            "that you defended Orchis Tower\x01",
            "from those jaegers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FYeah, Crossbell Times\x01",
            "featured it too. That\x01",
            "was really impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11P#01404FHehe. I had Dudley's\x01",
            "support back then as\x01",
            "well...\x02\x03",
            "#01400F...The meeting ended\x01",
            "more quickly than I\x01",
            "thought as well.\x02\x03",
            "I just thought I'd drop\x01",
            "by this place on my way\x01",
            "back.\x02\x03",
            "#01400FI'll apologize to Michel\x01",
            "later for my late\x01",
            "return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100F*giggle*, I think that\x01",
            "would be nice.\x02\x03",
            "#00105F...Umm, you seem to have\x01",
            "come today to visit a\x01",
            "grave...\x02\x03",
            "Could that grave be...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B99")

    label("loc_89E1")


    ChrTalk(
        0x101,
        (
            "#6P#00000FNow that you mention it... I read\x01",
            "about your efforts in front of\x01",
            "Orchis Tower in Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FIt said you challenged\x01",
            "the jaegers and it was a\x01",
            "fierce battle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00302FYeah, that was a big\x01",
            "deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11P#01404FHehe. I had Dudley's\x01",
            "support back then as\x01",
            "well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FHaha, there's no need to\x01",
            "be modest.\x02\x03",
            "#00105F...Umm, you seem to have\x01",
            "come today to visit a\x01",
            "grave...\x02\x03",
            "Could that grave be...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B99")

    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_93(0xF, 0x0, 0x1F4)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#11P#01403F...Saya MacLaine.\x02\x03",
            "#01408FShe passed away five years\x01",
            "ago in an accident... She\x01",
            "is Shizuku's mother.\x02",
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
            "#6P#00308FIf I remember correctly,\x01",
            "Shizuku lost her sight\x01",
            "in that accident...\x02",
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
        "#6P#10105FArios...?\x02",
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
            "#01400F──I've done what I can\x01",
            "for. It's time for me to\x01",
            "be going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FAh... Thank you for all\x01",
            "your hard work.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)

    def lambda_8E2C():

        label("loc_8E2C")

        TurnDirection(0x101, 0xF, 500)
        Yield()
        Jump("loc_8E2C")

    QueueWorkItem2(0x101, 2, lambda_8E2C)

    def lambda_8E3E():

        label("loc_8E3E")

        TurnDirection(0x102, 0xF, 500)
        Yield()
        Jump("loc_8E3E")

    QueueWorkItem2(0x102, 2, lambda_8E3E)

    def lambda_8E50():

        label("loc_8E50")

        TurnDirection(0x109, 0xF, 500)
        Yield()
        Jump("loc_8E50")

    QueueWorkItem2(0x109, 2, lambda_8E50)

    def lambda_8E62():

        label("loc_8E62")

        TurnDirection(0x105, 0xF, 500)
        Yield()
        Jump("loc_8E62")

    QueueWorkItem2(0x105, 2, lambda_8E62)

    def lambda_8E74():

        label("loc_8E74")

        TurnDirection(0x103, 0xF, 500)
        Yield()
        Jump("loc_8E74")

    QueueWorkItem2(0x103, 2, lambda_8E74)

    def lambda_8E86():

        label("loc_8E86")

        TurnDirection(0x104, 0xF, 500)
        Yield()
        Jump("loc_8E86")

    QueueWorkItem2(0x104, 2, lambda_8E86)
    OP_68(20680, 700, 30630, 1000)

    def lambda_8EA9():
        OP_95(0xFE, 23250, 0, 30200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_8EA9)
    WaitChrThread(0xF, 1)
    OP_4B(0xF, 0xFF)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#12P#01401F─In the future, Crossbell\x01",
            "will experience an\x01",
            "unprecedented situation.\x02\x03",
            "#01403FHowever, no matter the\x01",
            "situation and no matter\x01",
            "what trials may come...\x02\x03",
            "#01400FYou must never lose sight\x01",
            "of what is important to\x01",
            "you.\x02",
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

    def lambda_8FF6():
        OP_95(0xFE, 23250, 0, 16970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_8FF6)
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
        "#11P#00103F...There he went.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00305FWhat could that mean?\x02",
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
            "#6P#00203FI didn't really\x01",
            "understand, but... Maybe\x01",
            "it's some kind of warning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00001F(Arios...?)\x02",
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

    # Function_25_8559 end

    def Function_26_91A1(): pass

    label("Function_26_91A1")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_9274")

    ChrTalk(
        0x101,
        (
            "#00000F(This man... I think\x01",
            "he's...Nielsen?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9291")

    label("loc_9274")


    ChrTalk(
        0x101,
        "#00000F(This man is...)\x02",
    )

    CloseMessageWindow()

    label("loc_9291")

    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "Well then... Time to go\x01",
            "back, I guess.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "Hmm, are you all here to\x01",
            "visit a grave too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Good morning. I'll\x01",
            "excuse myself now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_933D():
        OP_95(0xFE, -20540, 0, 24610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_933D)
    Sleep(500)

    def lambda_935A():

        label("loc_935A")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_935A")

    QueueWorkItem2(0x101, 1, lambda_935A)
    Sleep(50)

    def lambda_936F():

        label("loc_936F")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_936F")

    QueueWorkItem2(0x102, 1, lambda_936F)
    Sleep(50)

    def lambda_9384():

        label("loc_9384")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_9384")

    QueueWorkItem2(0x103, 1, lambda_9384)
    Sleep(50)

    def lambda_9399():

        label("loc_9399")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_9399")

    QueueWorkItem2(0x104, 1, lambda_9399)
    WaitChrThread(0xE, 1)
    OP_95(0xE, -15310, 0, 19380, 2000, 0x0)
    SetChrFlags(0xE, 0x80)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)

    def lambda_93D8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_93D8)
    Sleep(100)

    def lambda_93E8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_93E8)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_94B7")

    ChrTalk(
        0x101,
        (
            "#00000FNielsen... He came to\x01",
            "visit my big brother's\x01",
            "grave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHe seemed he was earnestly\x01",
            "praying... Somehow like he\x01",
            "was making a report?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, I wonder.\x02",
    )

    CloseMessageWindow()
    Jump("loc_956E")

    label("loc_94B7")

    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#00100FLloyd, do you know that\x01",
            "man?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_94EC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_94EC)
    Sleep(50)

    def lambda_94FC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_94FC)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FNo... I have no idea.\x02\x03",
            "(If he came to visit\x01",
            "this grave, I wonder if\x01",
            "he knew my brother...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_956E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -21160, 0, 21930, 135)
    SetScenarioFlags(0x19D, 4)
    EventEnd(0x5)
    Return()

    # Function_26_91A1 end

    def Function_27_9594(): pass

    label("Function_27_9594")

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
        "#00005FNielsen...\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#5P...Hmm. Lloyd, right?\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00108F#6PThis is... Your\x01",
            "brother's grave...\x02",
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
            "#11PAlso, I had a few things\x01",
            "I wanted to say to Guy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FTo my big brother...?\x02",
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
            "#5PThe attack, the declaration of\x01",
            "independence and this morning's\x01",
            "Presidential speech...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PMy feelings are many,\x01",
            "but― The people have set\x01",
            "their course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PSo that's why I, conversely,\x01",
            "decided to ponder a certain\x01",
            ""darkness of the past".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F"Darkness of the\x01",
            "past"... ...Could you\x01",
            "mean...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PYes, it's the murder case\x01",
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
        "#00208F#6PGuy's...\x02",
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
            "#00006FBut why now? ...Maybe\x01",
            "it's precisely because\x01",
            "it is now.\x02\x03",
            "#00001FCould you have found\x01",
            "something, Nielsen...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PHmm...\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#11PLloyd, and the rest of\x01",
            "you as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PWould you all be inclined\x01",
            "to go somewhere else and\x01",
            "review his case with me?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 28)
    Return()

    # Function_27_9594 end

    def Function_28_9AD0(): pass

    label("Function_28_9AD0")

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
            "Join Nielsen's case review\x01",      # 0
            "Think about it for now\x01",          # 1
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
        (0, "loc_9B52"),
        (1, "loc_9C92"),
        (SWITCH_DEFAULT, "loc_9D4C"),
    )


    label("loc_9B52")


    ChrTalk(
        0x101,
        (
            "#00003F............\x02\x03",
            "#00001FUnderstood. By all\x01",
            "means, please let us\x01",
            "join you.\x02",
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
            "Here isn't good, so\x01",
            "let's return to the city\x01",
            "for now.\x02",
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
            "Quest [Guy Bannings\x01",
            "Murder Case Review]\x07\x00\x01",
            "started!\x02",
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
    Jump("loc_9D4C")

    label("loc_9C92")


    ChrTalk(
        0x101,
        (
            "#00003F...I'm sorry. Can I\x01",
            "think about it a little?\x02",
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
            "I'll be staying here for\x01",
            "a while, so please speak\x01",
            "to me if you like.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D44")
    OP_93(0xE, 0x0, 0x1F4)
    OP_4C(0xE, 0xFF)
    EventEnd(0x5)

    label("loc_9D44")

    SetScenarioFlags(0x19B, 6)
    Jump("loc_9D4C")

    label("loc_9D4C")

    Return()

    # Function_28_9AD0 end

    def Function_29_9D4D(): pass

    label("Function_29_9D4D")

    TalkBegin(0xE)

    ChrTalk(
        0xE,
        "...Lloyd, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Would you all be inclined\x01",
            "to go somewhere else and\x01",
            "review his case with me?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Call(0, 28)
    TalkEnd(0xE)
    Return()

    # Function_29_9D4D end

    SaveToFile()

Try(main)
