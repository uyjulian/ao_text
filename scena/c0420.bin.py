from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0420.bin",                # FileName
        "c0420",                    # MapName
        "c0420",                    # Location
        0x0023,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 35, 0, 4, 0, 5],
    )

    BuildStringList((
        "c0420",                  # 0
        "Ilya",                   # 1
        "Rixia",                  # 2
        "Sully",                  # 3
        "Troupe Chief Aban",      # 4
        "Heintz",                 # 5
        "Eugene",                 # 6
        "Theodore",               # 7
        "Nikol",                  # 8
        "Pliｳ",                  # 9
        "Celine",                 # 10
        "Karelia",                # 11
        "Mary",                   # 12
        "Elie",                   # 13
        "Wazy",                   # 14
        "シャンデリア",           # 15
    ))

    AddCharChip((
        "chr/ch05100.itc",                   # 00
        "chr/ch05200.itc",                   # 01
        "chr/ch10000.itc",                   # 02
        "chr/ch25800.itc",                   # 03
        "chr/ch27500.itc",                   # 04
        "chr/ch24200.itc",                   # 05
        "chr/ch28700.itc",                   # 06
        "chr/ch28800.itc",                   # 07
        "chr/ch28900.itc",                   # 08
        "chr/ch29000.itc",                   # 09
        "chr/ch29100.itc",                   # 0A
        "chr/ch36600.itc",                   # 0B
        "chr/ch36700.itc",                   # 0C
        "chr/ch36800.itc",                   # 0D
        "chr/ch09800.itc",                   # 0E
        "chr/ch36900.itc",                   # 0F
        "chr/ch14100.itc",                   # 10
        "chr/ch37000.itc",                   # 11
        "chr/ch09700.itc",                   # 12
        "chr/ch21900.itc",                   # 13
        "chr/ch10100.itc",                   # 14
    ))

    DeclNpc(0,       0,       15550,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(1000,    0,       13819,   0,    261,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294966296, 0,       13819,   0,    261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294965417, 9,       15239,   135,  261,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294900807, 0,       7329,    0,    261,  0x0, 0,   5,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(64750,   0,       3480,    135,  389,  0x0, 0,   6,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(4294964747, 1250,    19700,   0,    389,  0x0, 0,   7,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(64750,   0,       3480,    135,  261,  0x0, 0,   8,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(2250,    0,       14750,   270,  389,  0x0, 0,   9,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(4294899167, 0,       2140,    270,  389,  0x0, 0,   10,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(4294843496, 0,       4294965007, 180,  261,  0x0, 0,   19,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 27,  0.0,                   7.079999923706055,     0.0,                   14.0625,               [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.4000000059604645,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -2.8320000171661377,   -0.0,                  1.0])
    DeclEvent(0x0000, 0, 28,  -60.38999938964844,    3.0,                   -1.0,                  12.25,                 [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.2857142984867096,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   30.19499969482422,     -0.8571429252624512,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 31,  0.0,                   7.079999923706055,     0.0,                   14.0625,               [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.4000000059604645,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -2.8320000171661377,   -0.0,                  1.0])

    ChipFrameInfo(1176, 0)                                       # 0

    ScpFunction((
        "Function_0_498",          # 00, 0
        "Function_1_548",          # 01, 1
        "Function_2_573",          # 02, 2
        "Function_3_5C6",          # 03, 3
        "Function_4_5F1",          # 04, 4
        "Function_5_C67",          # 05, 5
        "Function_6_DDB",          # 06, 6
        "Function_7_1494",         # 07, 7
        "Function_8_18B2",         # 08, 8
        "Function_9_2A6A",         # 09, 9
        "Function_10_3110",        # 0A, 10
        "Function_11_318E",        # 0B, 11
        "Function_12_374C",        # 0C, 12
        "Function_13_422E",        # 0D, 13
        "Function_14_432D",        # 0E, 14
        "Function_15_450E",        # 0F, 15
        "Function_16_4733",        # 10, 16
        "Function_17_4DEE",        # 11, 17
        "Function_18_5B33",        # 12, 18
        "Function_19_5F64",        # 13, 19
        "Function_20_6010",        # 14, 20
        "Function_21_631D",        # 15, 21
        "Function_22_6714",        # 16, 22
        "Function_23_677A",        # 17, 23
        "Function_24_69CB",        # 18, 24
        "Function_25_6B6E",        # 19, 25
        "Function_26_6B75",        # 1A, 26
        "Function_27_6B9B",        # 1B, 27
        "Function_28_8CED",        # 1C, 28
        "Function_29_91ED",        # 1D, 29
        "Function_30_9278",        # 1E, 30
        "Function_31_A122",        # 1F, 31
        "Function_32_A686",        # 20, 32
        "Function_33_B087",        # 21, 33
        "Function_34_B512",        # 22, 34
        "Function_35_C9F6",        # 23, 35
        "Function_36_D3EE",        # 24, 36
        "Function_37_D9DA",        # 25, 37
        "Function_38_E0F3",        # 26, 38
        "Function_39_E13E",        # 27, 39
        "Function_40_E189",        # 28, 40
        "Function_41_E1C0",        # 29, 41
        "Function_42_E20B",        # 2A, 42
        "Function_43_E2A6",        # 2B, 43
        "Function_44_F155",        # 2C, 44
        "Function_45_F185",        # 2D, 45
        "Function_46_F1B5",        # 2E, 46
        "Function_47_F1E5",        # 2F, 47
        "Function_48_F254",        # 30, 48
        "Function_49_F271",        # 31, 49
        "Function_50_F657",        # 32, 50
        "Function_51_F67B",        # 33, 51
        "Function_52_F69F",        # 34, 52
        "Function_53_F6B4",        # 35, 53
        "Function_54_F6C2",        # 36, 54
        "Function_55_F6E1",        # 37, 55
        "Function_56_F700",        # 38, 56
        "Function_57_10424",       # 39, 57
        "Function_58_106F9",       # 3A, 58
    ))


    def Function_0_498(): pass

    label("Function_0_498")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_4D0"),
        (1, "loc_4DC"),
        (2, "loc_4E8"),
        (3, "loc_4F4"),
        (4, "loc_500"),
        (5, "loc_50C"),
        (6, "loc_518"),
        (SWITCH_DEFAULT, "loc_524"),
    )


    label("loc_4D0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_4DC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_4E8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_4F4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_500")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_50C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_518")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_524")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_530")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_547")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_547")

    Return()

    # Function_0_498 end

    def Function_1_548(): pass

    label("Function_1_548")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_572")
    OP_94(0xFE, 0xF4D8, 0x532, 0x1054A, 0x15AE, 0x3E8)
    Sleep(300)
    Jump("Function_1_548")

    label("loc_572")

    Return()

    # Function_1_548 end

    def Function_2_573(): pass

    label("Function_2_573")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C5")
    OP_95(0xFE, 61750, 0, 3480, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x2EE)
    Sleep(300)
    OP_95(0xFE, 66750, 0, 3480, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x2EE)
    Sleep(300)
    Jump("Function_2_573")

    label("loc_5C5")

    Return()

    # Function_2_573 end

    def Function_3_5C6(): pass

    label("Function_3_5C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F0")
    OP_94(0xFE, 0xFFFF9C32, 0x1C0C, 0xFFFF8F8A, 0x1108, 0x3E8)
    Sleep(300)
    Jump("Function_3_5C6")

    label("loc_5F0")

    Return()

    # Function_3_5C6 end

    def Function_4_5F1(): pass

    label("Function_4_5F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_670")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xD, 3520, 1250, 22730, 90)
    SetChrPos(0xE, 4800, 1250, 22730, 270)
    SetChrPos(0xA, 0, 1250, 27230, 0)
    SetChrChipByIndex(0xA, 0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64A")
    SetChrFlags(0xA, 0x10)

    label("loc_64A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_END)), "loc_657")
    SetChrChipByIndex(0xA, 0x2)

    label("loc_657")

    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_B95")

    label("loc_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6E7")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xB, 0, 0, 15300, 0)
    SetChrPos(0xD, 0, 1250, 27300, 180)
    SetChrPos(0xF, -1390, 1250, 26170, 90)
    SetChrPos(0x11, 1390, 1250, 26170, 270)
    SetChrChipByIndex(0xD, 0xB)
    SetChrChipByIndex(0xF, 0xD)
    SetChrChipByIndex(0x11, 0x11)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_B95")

    label("loc_6E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7C0")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xB, 0, 0, 15300, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xA, 0, 1250, 27300, 180)
    SetChrPos(0xF, -1390, 1250, 26170, 90)
    SetChrPos(0x11, 1390, 1250, 26170, 270)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x11, 0x10)
    SetChrChipByIndex(0xA, 0x10)
    SetChrChipByIndex(0xF, 0xD)
    SetChrChipByIndex(0x11, 0x11)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xD, 65610, 0, 4550, 225)
    SetChrPos(0xE, 65000, 0, 3000, 270)
    SetChrPos(0x10, 63670, 0, 3590, 90)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrChipByIndex(0xD, 0xB)
    SetChrChipByIndex(0xE, 0xC)
    SetChrChipByIndex(0x10, 0xF)
    Jump("loc_B95")

    label("loc_7C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_813")
    SetChrPos(0xB, -62780, 0, 3150, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E9")
    SetChrFlags(0xB, 0x10)

    label("loc_7E9")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0xC, -66490, 0, 7330, 0)
    Jump("loc_B95")

    label("loc_813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8BF")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xD, -1390, 1250, 25170, 90)
    SetChrPos(0xE, 1390, 1250, 25170, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_866")
    SetChrFlags(0xD, 0x10)

    label("loc_866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_875")
    SetChrFlags(0xE, 0x10)

    label("loc_875")

    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 64000, 0, 3000, 90)
    SetChrPos(0xF, 65000, 0, 3000, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AB")
    SetChrFlags(0x11, 0x10)

    label("loc_8AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BA")
    SetChrFlags(0xF, 0x10)

    label("loc_8BA")

    Jump("loc_B95")

    label("loc_8BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_93D")
    SetChrChipByIndex(0xA, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F4")
    SetChrPos(0xA, -50, 0, 15980, 180)
    SetChrFlags(0x8, 0x80)
    Jump("loc_924")

    label("loc_8F4")

    SetChrChipByIndex(0x8, 0x12)
    SetChrPos(0x8, -1390, 1250, 25170, 90)
    SetChrPos(0xA, 1390, 1250, 25170, 270)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_924")

    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_B95")

    label("loc_93D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_969")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_B95")

    label("loc_969")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_995")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_B95")

    label("loc_995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9F4")
    SetChrFlags(0xF, 0x80)
    SetChrPos(0xA, 1390, 1250, 26170, 270)
    SetChrPos(0x9, -1390, 1250, 26170, 90)
    SetChrPos(0xB, 80, 1250, 24110, 0)
    SetChrPos(0x8, -6130, 15200, -2810, 45)
    SetChrChipByIndex(0xA, 0x10)
    SetChrChipByIndex(0x9, 0xE)
    Jump("loc_B95")

    label("loc_9F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A87")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xD, -1390, 1250, 25170, 90)
    SetChrPos(0xE, 1390, 1250, 25170, 270)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 64000, 0, 3000, 90)
    SetChrPos(0xF, 65000, 0, 3000, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A73")
    SetChrFlags(0xA, 0x10)

    label("loc_A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A82")
    SetChrFlags(0xF, 0x10)

    label("loc_A82")

    Jump("loc_B95")

    label("loc_A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_AB3")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_B95")

    label("loc_AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B22")
    SetChrChipByIndex(0x8, 0x12)
    SetChrChipByIndex(0x9, 0xE)
    SetChrChipByIndex(0xF, 0xD)
    SetChrPos(0xA, 7570, 0, 17850, 315)
    SetChrPos(0xF, 67000, 0, 3000, 90)
    SetChrPos(0xB, 0, 1250, 30300, 180)
    SetChrPos(0x8, -1390, 1250, 29170, 90)
    SetChrPos(0x9, 1390, 1250, 29170, 270)
    Jump("loc_B95")

    label("loc_B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B53")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_B95")

    label("loc_B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B95")
    SetChrPos(0xB, -64489, 0, 7330, 270)
    OP_93(0xC, 0x5A, 0x0)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xF, 65000, 0, 3000, 180)
    BeginChrThread(0xF, 0, 0, 1)

    label("loc_B95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_BA4")
    ClearScenarioFlags(0x22, 0)
    Event(0, 43)

    label("loc_BA4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C0A")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD8")
    Event(0, 34)

    label("loc_BD8")

    Jump("loc_C05")

    label("loc_BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BF4")
    Event(0, 32)
    Jump("loc_C05")

    label("loc_BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C05")
    Event(0, 33)

    label("loc_C05")

    Jump("loc_C30")

    label("loc_C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C30")
    Event(0, 56)

    label("loc_C30")

    Jump("loc_C66")

    label("loc_C35")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C66")
    Event(0, 37)

    label("loc_C66")

    Return()

    # Function_4_5F1 end

    def Function_5_C67(): pass

    label("Function_5_C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C83")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C9A")

    label("loc_C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C9A")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CB7")
    Jump("loc_D6F")

    label("loc_CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CC5")
    Jump("loc_D6F")

    label("loc_CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDD")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_CDD")

    Jump("loc_D6F")

    label("loc_CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CF0")
    Jump("loc_D6F")

    label("loc_CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_CFE")
    Jump("loc_D6F")

    label("loc_CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D0C")
    Jump("loc_D6F")

    label("loc_D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D1F")
    ModifyEventFlags(1, 1, 0x80)
    Jump("loc_D6F")

    label("loc_D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D2D")
    Jump("loc_D6F")

    label("loc_D2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D3B")
    Jump("loc_D6F")

    label("loc_D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D49")
    Jump("loc_D6F")

    label("loc_D49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_D57")
    Jump("loc_D6F")

    label("loc_D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_D6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6F")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D8A")
    ModifyEventFlags(1, 2, 0x80)
    OP_1B(0x2, 0x0, 0x2A)

    label("loc_D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D9E")
    ClearMapObjFlags(0x1A, 0x4)

    label("loc_D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_DDA")
    ClearMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1C, 0x1000)
    ClearMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1B, 0x1000)
    SetMapObjFrame(0xFF, "curtain", 0x0, 0x1)
    SetMapObjFrame(0x1B, "kesu", 0x0, 0x1)

    label("loc_DDA")

    Return()

    # Function_5_C67 end

    def Function_6_DDB(): pass

    label("Function_6_DDB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1024")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4F")

    ChrTalk(
        0xFE,
        "How about it? Isn't their drive just amazing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now anyway, we are doing\x01",
            "our best to resume performances\x01",
            "as quickly as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard Ilya has awoken...\x01",
            "We must do our best to live up\x01",
            "to her expectations as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(No one in the\x01",
            "troupe knows\x01",
            "Rixia's location.)\x02\x03",
            "(I would have wanted to\x01",
            "show them her face, but...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101F")

    label("loc_F4F")


    ChrTalk(
        0xFE,
        (
            "As always, we will\x01",
            "be here working on\x01",
            "our performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lloyd and friends,\x01",
            "please take care\x01",
            "of Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, we understand.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_101F")

    ChrTalk(
        0x106,
        (
            "#10700FTroupe Chief...\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_101F")

    Jump("loc_1490")

    label("loc_1024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_108D")

    ChrTalk(
        0xFE,
        (
            "Everyone is really\x01",
            "doing their best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ilya, Rixia... \x01",
            "We will be waiting for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1490")

    label("loc_108D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1293")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1215")
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xB,
        "Oh, Lloyd...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FTroupe Chief...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yes... I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Thinking about various things,\x01",
            "I can't help but be worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "About Ilya. I believe\x01",
            "she will definitely\x01",
            "awaken, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FTroupe Chief...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*sigh*, but I mustn't\x01",
            "do nothing but mope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I... I have to get\x01",
            "myself together.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x18D, 0)
    Jump("loc_128E")

    label("loc_1215")


    ChrTalk(
        0xFE,
        (
            "*sigh*, it's time to\x01",
            "get myself together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If Ilya learns I was like this this\x01",
            "whole time, she'll be mad at me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_128E")

    Jump("loc_1490")

    label("loc_1293")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1316")

    ChrTalk(
        0xFE,
        "Sorry, Lloyd and friends.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's no time until the\x01",
            "performance. We want to finish\x01",
            "our final preparations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1490")

    label("loc_1316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1324")
    Jump("loc_1490")

    label("loc_1324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1332")
    Jump("loc_1490")

    label("loc_1332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1340")
    Jump("loc_1490")

    label("loc_1340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_134E")
    Jump("loc_1490")

    label("loc_134E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_135C")
    Jump("loc_1490")

    label("loc_135C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_136A")
    Jump("loc_1490")

    label("loc_136A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_13F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1385")
    Call(0, 8)
    Jump("loc_13F4")

    label("loc_1385")


    ChrTalk(
        0xFE,
        (
            "Goodness, Ilya\x01",
            "is so reliable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If she is like this, tomorrow's\x01",
            "performance will surely be a success.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F4")

    Jump("loc_1490")

    label("loc_13F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1407")
    Jump("loc_1490")

    label("loc_1407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1490")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1422")
    Call(0, 7)
    Jump("loc_1490")

    label("loc_1422")


    ChrTalk(
        0xFE,
        (
            "Maybe I'm asking too much,\x01",
            "but please, I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is to realize\x01",
            "Ilya's idea as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1490")

    TalkEnd(0xFE)
    Return()

    # Function_6_DDB end

    def Function_7_1494(): pass

    label("Function_7_1494")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176A")

    ChrTalk(
        0xB,
        (
            "So, Heintz.\x01",
            "Can you technically do it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well...\x01",
            "Of course I'll try, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1593")

    ChrTalk(
        0xB,
        "Oh, you guys are the Special Support Section.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Could it be that some\x01",
            "incident happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_162E")

    label("loc_1593")


    ChrTalk(
        0xB,
        "Oh, all of you are...\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 0)

    ChrTalk(
        0xB,
        (
            "Oh, you're Lloyd of the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Could it be that some\x01",
            "incident happened?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_162E")


    ChrTalk(
        0x101,
        (
            "#00000FNo, we're just patrolling\x01",
            "the city right now.\x02\x03",
            "We wanted to look in here just\x01",
            "as a precautionary measure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, I see. Thank\x01",
            "you for coming here\x01",
            "on your patrols.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, if anything does happen, please\x01",
            "don't hesitate to ask for our help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, thank you very much.\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x10E, 0x0)
    OP_93(0xC, 0x5A, 0x0)
    SetScenarioFlags(0x136, 4)
    Jump("loc_18A9")

    label("loc_176A")


    ChrTalk(
        0xC,
        "But, is it ok?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If we speed it up,\x01",
            "the timing will be that\x01",
            "much more strict...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yeah, Ilya is already\x01",
            "aware of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "For Ilya's idea, it's\x01",
            "absolutely necessary to\x01",
            "speed the entire scene up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It seems that she wants to test\x01",
            "herself to the very limit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I see... \x01",
            "Then, I'll give it a try.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x1, 3)

    label("loc_18A9")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_7_1494 end

    def Function_8_18B2(): pass

    label("Function_8_18B2")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xB, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x101, -900, 1250, 26340, 0)
    SetChrPos(0x102, 800, 1250, 26340, 0)
    SetChrPos(0x109, -1500, 1250, 25200, 0)
    SetChrPos(0x105, 0, 1250, 25400, 0)
    SetChrPos(0x104, 1500, 1250, 25200, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_93(0xB, 0xB4, 0x0)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    OP_68(-610, 2600, 26940, 0)
    MoveCamera(27, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15740, 0)
    OP_0D()

    ChrTalk(
        0xB,
        "Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#06105FMy, the younger brother and friends.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FHello. Sorry for interrupting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06202FEveryone, hello.\x02\x03",
            "#06209FUh uh, so you've finally\x01",
            "returned too, Mr. Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FOh, that's my dear Rixia for you. I'm\x01",
            "so happy you were worried about me.\x02\x03",
            "#00309FAh, but even so, to get to see you and\x01",
            "Miss Ilya in your costumes like this...\x02\x03",
            "I've seen them many times before, \x01",
            "but I seriously never get tired of it㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#06102FUh uh, thanks a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06204FH-Hearing you say this directly is\x01",
            "a little embarrassing, though...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x104, 500)

    ChrTalk(
        0x105,
        (
            "#6P#10304FHu hu, it's true that Randy's glances\x01",
            "are always lascivious.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#11P#00301FWhat was that for, Wazy? I was only\x01",
            "saying it out of my own pure heart―\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    ChrTalk(
        0x102,
        (
            "#11P#00106FAlright, we understand,\x01",
            "so let's just leave it at that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_1D1D():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D1D)
    Sleep(50)

    def lambda_1D2D():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1D2D)
    Sleep(50)

    def lambda_1D3D():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D3D)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x109,
        "#12P#10109FA-Ahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FSorry for making a fuss.\x02\x03",
            "#00000FBy the way,\x01",
            "are you practicing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06100FI guess. We're doing the\x01",
            "fine tuning for our\x01",
            "performance tomorrow night.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        (
            "#06202FUh uh, tomorrow's guests\x01",
            "aren't just simply guests,\x01",
            "and I'm feeling nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yeah, I can't believe the heads of\x01",
            "state are going to visit our theater.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FHeads of state...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FThat's right. That came up in our\x01",
            "planning meeting this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, well they've been invited\x01",
            "to Crossbell, after all.\x02\x03",
            "#10304FAnd Arc-en-ciel performances are\x01",
            "the best entertainment around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FYeah, that's probably\x01",
            "what they were thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FBut, I can see why you'd be nervous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06203FYes. It seems like the other\x01",
            "members are nervous too...\x02\x03",
            "#06209FThough, Miss Ilya is\x01",
            "the same as usual.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        (
            "#06103FWhat? I mean, worrying over every little\x01",
            "thing won't solve anything, you know.\x02\x03",
            "#06100FNo matter who's sitting in those seats,\x01",
            "all I can do is my best for them.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x8, 500)

    ChrTalk(
        0xB,
        (
            "#11PGoodness... We can always\x01",
            "rely on you, can't we.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PAnd with the renewal performance too.\x01",
            "Your energy amazes me every time.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FRenewal performance...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FNow that you mention it...\x01",
            ""Golden Sun, Silver Moon"\x01",
            "is getting a renewal, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FYeah, that's a rumor\x01",
            "that's going around.\x02\x03",
            "I think they're saying some\x01",
            "bold arrangement will be added?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2328():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2328)
    Sleep(50)
    OP_93(0xB, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#06109FYes, that's right.\x02\x03",
            "#06104FRevising something that was completed once\x01",
            "was, in a sense, a challenge, however...\x02\x03",
            "#06100FWe're aiming to bring the\x01",
            "script and direction to a whole\x01",
            "other level of perfection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06202FYes. Once the normal performance is over,\x01",
            "we plan to focus on training for the new\x01",
            "one for approximately one month.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 2)), scpexpr(EXPR_END)), "loc_25D2")

    ChrTalk(
        0x101,
        (
            "#12P#00000FI see. So when you said "looks like we're\x01",
            "going to be busy" when we met before,\x01",
            "you must have been talking about this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#06100FUh uh, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#12P#10100FBut to think you're going to train for\x01",
            "a whole month... It seems like you put\x01",
            "a lot of work into the new arrangement.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2629")

    label("loc_25D2")


    ChrTalk(
        0x109,
        (
            "#12P#10100FI see... It seems like\x01",
            "you put a lot of work\x01",
            "into the new arrangement.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2629")


    ChrTalk(
        0x104,
        (
            "#12P#00300FBut "Golden Sun, Silver Moon" is\x01",
            "already known as one of Arc-en-\x01",
            "ciel's best performances ever...\x02\x03",
            "#00304FIf you're goin' to improve it even more, I can't\x01",
            "even imagine how the final product will turn out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah, seriously.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06100FUh uh. Since I've decided to live for the stage, \x01",
            "I'm always searching for my best performance.\x02\x03",
            "#06104FIn order to show our guests the\x01",
            "time of their lives, we have to\x01",
            "create an amazing play...\x02\x03",
            "#06100FThat is the duty of\x01",
            "Arc-en-ciel, and\x01",
            "especially us artists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FAs expected from Miss Ilya...\x01",
            "You're second to none for\x01",
            "passion about the stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FHmm, I can't wait until\x01",
            "the renewal performance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06100FUh uh. It'll be officially announced\x01",
            "before too long, so please be patient.\x02\x03",
            "I'm sure even those who saw the old\x01",
            "version will be able to enjoy it.\x02\x03",
            "#06104FAnd there's a little\x01",
            "surprise in the cast... \x01",
            "I'm sure you'll be shocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FSurprise you say... \x01",
            "Ha ha, then I'll look forward\x01",
            "to seeing what it is.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x8, 0x5A, 0x0)
    OP_93(0x9, 0x10E, 0x0)
    OP_4C(0xB, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x0, 0, 1250, 27240, 180)
    SetScenarioFlags(0x14B, 6)
    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_8_18B2 end

    def Function_9_2A6A(): pass

    label("Function_9_2A6A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2A7B")
    Jump("loc_310C")

    label("loc_2A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2A89")
    Jump("loc_310C")

    label("loc_2A89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2B6F")
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x8,
        (
            "#01700FAlright, we'll now check the scene\x01",
            "where the "Moon Princess" appears\x01",
            "and pursues the other two princesses.\x02\x03",
            "Rixia, Sully, you ready?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01800FYes... Of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#04200FI'm ok here!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    Jump("loc_310C")

    label("loc_2B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2B80")
    Call(0, 10)
    Jump("loc_310C")

    label("loc_2B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2B8E")
    Jump("loc_310C")

    label("loc_2B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B9C")
    Jump("loc_310C")

    label("loc_2B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BB7")
    Call(0, 30)
    Jump("loc_2D05")

    label("loc_2BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C88")

    ChrTalk(
        0x8,
        (
            "#01709FUh uh, this reminds me\x01",
            "of things of my past.\x02\x03",
            "#01700FIf you like, come\x01",
            "see our renewal\x01",
            "performance too.\x02\x03",
            "Rixia and Sully there will\x01",
            "be in it too. It's sure to\x01",
            "be an amazing show.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D05")

    label("loc_2C88")


    ChrTalk(
        0x8,
        (
            "#01700FCome and see our\x01",
            "renewal performance.\x02\x03",
            "Rixia and Sully there will\x01",
            "be in it too. It's sure to\x01",
            "be an amazing show.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D05")

    Jump("loc_310C")

    label("loc_2D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2D18")
    Jump("loc_310C")

    label("loc_2D18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2D26")
    Jump("loc_310C")

    label("loc_2D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2F09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D41")
    Call(0, 8)
    Jump("loc_2F04")

    label("loc_2D41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E5E")

    ChrTalk(
        0x8,
        (
            "#06100FSince I've decided to live for the stage, \x01",
            "I'm always searching for my best performance.\x02\x03",
            "#06104FIn order to show our guests the\x01",
            "time of their lives, we have to\x01",
            "create an amazing play...\x02\x03",
            "#06102FThat is the duty of\x01",
            "Arc-en-ciel, and\x01",
            "especially us artists.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F04")

    label("loc_2E5E")


    ChrTalk(
        0x8,
        (
            "#06100FUh uh. It'll be officially\x01",
            "announced before too long,\x01",
            "so please be patient.\x02\x03",
            "#06104FI'm sure even those who saw the old\x01",
            "version will be able to enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F04")

    Jump("loc_310C")

    label("loc_2F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2F17")
    Jump("loc_310C")

    label("loc_2F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_310C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3095")

    ChrTalk(
        0x8,
        (
            "#01700FUh uh, I see some new faces. That must\x01",
            "mean you guys have finally restarted.\x02\x03",
            "#01700FI think Cecil is looking forward to seeing\x01",
            "you, younger brother, and you guys too.\x02\x03",
            "#01709FMaaan, how wonderful for you, eh? Eh?㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FH-Ha ha... Please\x01",
            "don't make fun of me.\x02\x03",
            "#00004F(She's right though. I should\x01",
            "visit sister Cecil before too long.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_310C")

    label("loc_3095")


    ChrTalk(
        0x8,
        (
            "#01700FUh uh, look forward to\x01",
            "what we're planning next.\x02\x03",
            "#01709FIt's still a secret, but\x01",
            "I'm sure you'll love it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_310C")

    TalkEnd(0xFE)
    Return()

    # Function_9_2A6A end

    def Function_10_3110(): pass

    label("Function_10_3110")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x8,
        (
            "#06100FSay, Sully. There's still\x01",
            "time before the performance.\x01",
            "Let's keep going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12201FR-Right...!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_10_3110 end

    def Function_11_318E(): pass

    label("Function_11_318E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_319F")
    Jump("loc_3748")

    label("loc_319F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_31AD")
    Jump("loc_3748")

    label("loc_31AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3241")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_321B")

    ChrTalk(
        0x9,
        "#01808F―I'm sorry. It's right before our performance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F(Rixia...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_323C")

    label("loc_321B")


    ChrTalk(
        0x9,
        "#01801FMiss Ilya... Please!\x02",
    )

    CloseMessageWindow()

    label("loc_323C")

    Jump("loc_3748")

    label("loc_3241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_324F")
    Jump("loc_3748")

    label("loc_324F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_325D")
    Jump("loc_3748")

    label("loc_325D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_326B")
    Jump("loc_3748")

    label("loc_326B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3279")
    Jump("loc_3748")

    label("loc_3279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3287")
    Jump("loc_3748")

    label("loc_3287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3295")
    Jump("loc_3748")

    label("loc_3295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_353E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32B0")
    Call(0, 8)
    Jump("loc_3539")

    label("loc_32B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34B6")

    ChrTalk(
        0x9,
        (
            "#06203FThe Trade Conference... So it's really true that all\x01",
            "different sorts of people have come to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYou're doing your best\x01",
            "too, right Rixia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#06208FYes, that's true, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FIs there something else you're worried about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06202FAh, well... It's no\x01",
            "big deal, so please\x01",
            "don't worry about it.\x02\x03",
            "#06204FAnd anyway, right\x01",
            "now I need to focus\x01",
            "on my performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FS-Sure...\x02\x03",
            "#00003F(Is Rixia worried about something\x01",
            "related to the Trade Conference?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14C, 0)
    Jump("loc_3539")

    label("loc_34B6")


    ChrTalk(
        0x9,
        (
            "#06206FI'm the type to worry about\x01",
            "unnecessary things, aren't I.\x02\x03",
            "#06201FAnyway, right now I need to\x01",
            "focus on my performance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3539")

    Jump("loc_3748")

    label("loc_353E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_354C")
    Jump("loc_3748")

    label("loc_354C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3748")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36A8")

    ChrTalk(
        0x9,
        (
            "#01802FYou've added new members and\x01",
            "restarted... I'll be cheering\x01",
            "for all of you from now on.\x02\x03",
            "Please, everyone... \x01",
            "Feel free to visit us any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSure. And please feel free to contact\x01",
            "us if you ever need anything.\x02\x03",
            "We'd be glad to help whenever needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01809FUh uh, I'll be counting on you then.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3748")

    label("loc_36A8")


    ChrTalk(
        0x9,
        (
            "#01802FYou've added new members and\x01",
            "restarted... I'll be cheering\x01",
            "for all of you from now on.\x02\x03",
            "#01809FPlease, everyone... \x01",
            "Feel free to visit us any time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3748")

    TalkEnd(0xFE)
    Return()

    # Function_11_318E end

    def Function_12_374C(): pass

    label("Function_12_374C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3772")
    Call(0, 58)
    Return()

    label("loc_3772")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3EA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3790")
    Call(0, 35)
    Jump("loc_3E9E")

    label("loc_3790")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_END)), "loc_3A8A")

    ChrTalk(
        0xA,
        (
            "#04200FOh, did you\x01",
            "guys already go\x01",
            "visit Miss Ilya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah. She showed us\x01",
            "her energetic spirit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04203FI see...\x02\x03",
            "#04200FUmm, how about you, sis Rixia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708FYeah... We didn't meet face-\x01",
            "to-face, but she spoke to me\x01",
            "from outside her room...\x02\x03",
            "#10702FI'm not sure how to say\x01",
            "this, but... Sorry, Sully.\x01",
            "Sorry for worrying you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04205FI wasn't particularly worried...\x02\x03",
            "#04204FBut... I feel\x01",
            "relieved somehow.\x02\x03",
            "#04202FWith this, finally, I can\x01",
            "rest easy knowing you're\x01",
            "not going anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10702FSully...\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#04206FSorry, sis Rixia.\x01",
            "That was impertinent.\x02\x03",
            "#04202FFor now, I'll \x01",
            "stand by here.\x02\x03",
            "#04209FAnyway, come back soon, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10702FUh uh... Sure, understood.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D54")

    label("loc_3A8A")


    ChrTalk(
        0xA,
        (
            "#14000FOh, did you\x01",
            "guys already go\x01",
            "visit Miss Ilya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah. She showed us\x01",
            "her energetic spirit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14003FI see...\x02\x03",
            "#14000FUmm, what about Rixia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708FYeah... We didn't meet face-\x01",
            "to-face, but she spoke to me\x01",
            "from outside her room...\x02\x03",
            "#10702FI'm not sure how to say\x01",
            "this, but... Sorry, Sully.\x01",
            "Sorry for worrying you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14005FI wasn't particularly worried...\x02\x03",
            "#14004FBut... I feel\x01",
            "relieved somehow.\x02\x03",
            "#14002FWith this, finally, I can\x01",
            "rest easy knowing you're\x01",
            "not going anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10702FSully...\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#14006FSorry, sis Rixia.\x01",
            "That was impertinent.\x02\x03",
            "#14002FFor now, I'll\x01",
            "stand by here.\x02\x03",
            "#14009FAnyway, come back soon, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10702FUh uh... Sure, understood.\x02",
    )

    CloseMessageWindow()

    label("loc_3D54")

    SetScenarioFlags(0x1CF, 7)
    Jump("loc_3E9E")

    label("loc_3D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_END)), "loc_3E04")

    ChrTalk(
        0xA,
        (
            "#04200FI don't know where you're\x01",
            "going, but be careful, ok?\x02\x03",
            "#04202FWe'll be restarting performances before\x01",
            "long. I definitely want you to see them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E9E")

    label("loc_3E04")


    ChrTalk(
        0xA,
        (
            "#14000FI don't know where you're\x01",
            "going, but be careful, ok?\x02\x03",
            "#14002FWe'll be restarting performances before\x01",
            "long. I definitely want you to see them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E9E")

    Jump("loc_422A")

    label("loc_3EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3F19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EBE")
    Call(0, 13)
    Jump("loc_3F14")

    label("loc_3EBE")


    ChrTalk(
        0xA,
        (
            "#12203F...First the music starts,\x01",
            "then I come out from the\x01",
            "stage wing dancing...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F14")

    Jump("loc_422A")

    label("loc_3F19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3F27")
    Jump("loc_422A")

    label("loc_3F27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3F5E")

    ChrTalk(
        0xA,
        (
            "#04201FMiss Ilya, I'm\x01",
            "always ready!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_422A")

    label("loc_3F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3F6F")
    Call(0, 10)
    Jump("loc_422A")

    label("loc_3F6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3F7D")
    Jump("loc_422A")

    label("loc_3F7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3F8B")
    Jump("loc_422A")

    label("loc_3F8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F99")
    Jump("loc_422A")

    label("loc_3F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_405A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FB4")
    Call(0, 14)
    Jump("loc_4055")

    label("loc_3FB4")


    ChrTalk(
        0xA,
        (
            "#04203FFocusing on what I have in front of me...\x01",
            "I see, that's what it means.\x02\x03",
            "#04201FA-Alright... I'll practice without\x01",
            "thinking about unnecessary things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4055")

    Jump("loc_422A")

    label("loc_405A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4068")
    Jump("loc_422A")

    label("loc_4068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4193")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40F5")

    ChrTalk(
        0xA,
        (
            "#04206FMiss Ilya and sis Rixia\x01",
            "sure are amazing.\x02\x03",
            "#04200FI wonder if I'll be able\x01",
            "to perform like they do...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_418E")

    label("loc_40F5")


    ChrTalk(
        0xA,
        (
            "#04205FWhoops, can't stand around daydreaming.\x01",
            "I've got to hurry and finish up the cleaning.\x02\x03",
            "#04203FI'll lose my practice\x01",
            "time if I'm not careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_418E")

    Jump("loc_422A")

    label("loc_4193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_41A1")
    Jump("loc_422A")

    label("loc_41A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_422A")

    ChrTalk(
        0xA,
        (
            "#04200FEven so... \x01",
            "How can she know that sis Rixia\x01",
            "improved the way she rests?\x02\x03",
            "#04204F...I knew it. Miss Ilya is amazing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_422A")

    TalkEnd(0xFE)
    Return()

    # Function_12_374C end

    def Function_13_422E(): pass

    label("Function_13_422E")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0x11,
        (
            "Then, Nikol, Sully. \x01",
            "Please continue on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Understood.\x01",
            "Let's go, Sully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12201FSure. First is the\x01",
            "step, then the jump.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Sully and all the others... \x01",
            "Looks like they're focused on their training.)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_13_422E end

    def Function_14_432D(): pass

    label("Function_14_432D")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xA,
        (
            "#04205FSay, Mr. Nikol.\x02\x03",
            "Why doesn't Miss Ilya and the\x01",
            "others give us the details of the\x01",
            "renewal performance already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Well, I don't have the answer, but don't\x01",
            "we have the final performance left?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "If they tell you before that's done, you won't\x01",
            "be able to focus and it'll be a problem...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "I think that's the most likely reason.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04203FO-Oh... I see.\x01",
            "You're smart, Mr. Nikol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "No, I believe it's the normal thing to think...\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 2)
    Return()

    # Function_14_432D end

    def Function_15_450E(): pass

    label("Function_15_450E")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xA,
        (
            "#04200FSay, Mr. Nikol. \x01",
            "About the change in that \x01",
            "turn we do in that scene...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Yeah, it connects with the other\x01",
            "move after a very short pause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "The timing is tight, but\x01",
            "that's why it's pretty smooth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#04201FI-I see. I'll try.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_469D")

    ChrTalk(
        0x101,
        (
            "#00000F(Sully... Looks like she's\x01",
            "doing her best with training.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Yes... Her enthusiasm\x01",
            "sure is infectious.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_471A")

    label("loc_469D")


    ChrTalk(
        0x101,
        (
            "#00005F(So she's Arc-en-ciel's\x01",
            "novice artist, huh...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(*giggle*, looks like she's\x01",
            "focused on her training.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_471A")

    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 2)
    Return()

    # Function_15_450E end

    def Function_16_4733(): pass

    label("Function_16_4733")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_475C")
    Call(0, 36)
    Return()

    label("loc_475C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_476D")
    Jump("loc_4DEA")

    label("loc_476D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_481C")

    ChrTalk(
        0xFE,
        (
            "Even so... Martial law\x01",
            "was too sudden that it\x01",
            "caused considerable confusion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, at any rate, all\x01",
            "those of us left here can\x01",
            "do is focus on training.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DEA")

    label("loc_481C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4875")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4837")
    Call(0, 13)
    Jump("loc_4870")

    label("loc_4837")


    ChrTalk(
        0xFE,
        (
            "First is to match Sully's\x01",
            "timing, and from there...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4870")

    Jump("loc_4DEA")

    label("loc_4875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4883")
    Jump("loc_4DEA")

    label("loc_4883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4948")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_489E")
    Call(0, 24)
    Jump("loc_4943")

    label("loc_489E")


    ChrTalk(
        0xFE,
        (
            "I-I don't really get it but it\x01",
            "seems like I stepped on something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, whatever... \x01",
            "Senior was saying this too, so I\x01",
            "have to hurry up and start training.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4943")

    Jump("loc_4DEA")

    label("loc_4948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4956")
    Jump("loc_4DEA")

    label("loc_4956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4964")
    Jump("loc_4DEA")

    label("loc_4964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4972")
    Jump("loc_4DEA")

    label("loc_4972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4980")
    Jump("loc_4DEA")

    label("loc_4980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_499B")
    Call(0, 14)
    Jump("loc_4A2D")

    label("loc_499B")


    ChrTalk(
        0xFE,
        "How to say this... Sully is very direct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, that's exactly why there's\x01",
            "so many things she has to learn. \x01",
            "I too have got to do better.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A2D")

    Jump("loc_4DEA")

    label("loc_4A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4A40")
    Jump("loc_4DEA")

    label("loc_4A40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4BA6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4ACB")

    ChrTalk(
        0xFE,
        (
            "Oops...\x01",
            "I'll begin training now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll leave the medical\x01",
            "questionnaire to you guys.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BA1")

    label("loc_4ACB")


    ChrTalk(
        0xFE,
        (
            "Although I'm worried about tomorrow's\x01",
            "performance, I can't help but be curious\x01",
            "about the renewal performance details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I mustn't think about\x01",
            "anything unnecessary.\x01",
            "For now, I've got only to practice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BA1")

    Jump("loc_4DEA")

    label("loc_4BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4BB4")
    Jump("loc_4DEA")

    label("loc_4BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4DEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D33")

    ChrTalk(
        0xFE,
        (
            "Sully is still an assistant, but... When she\x01",
            "participated in performance practice, the\x01",
            "swiftness of her movements was impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our troupe is composed of mostly\x01",
            "geniuses like that, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although, in addition to their talent,\x01",
            "they pile up an unusual amount of efforts.\x01",
            "I can't compare to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Anyway, all I can do is do my best.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_4DEA")

    label("loc_4D33")


    ChrTalk(
        0xFE,
        (
            "Though I may be inferior to all\x01",
            "those geniuses, lately I have come\x01",
            "to be accepted, little-by-little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was lost for a time, but... \x01",
            "Anyway, all I can do is do my very best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DEA")

    TalkEnd(0xFE)
    Return()

    # Function_16_4733 end

    def Function_17_4DEE(): pass

    label("Function_17_4DEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_503A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FA6")

    ChrTalk(
        0xC,
        "Hey, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Actually, we were\x01",
            "contacted by the\x01",
            "Meister just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He said he'd start on\x01",
            "automata production\x01",
            "right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWow... \x01",
            "That's great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yes, indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To begin with, the\x01",
            "Meister hardly ever\x01",
            "contacts us, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "There's no greater happiness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(So the Meister was really\x01",
            "worried about this place.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200F(Uh uh. I hope he finishes them quickly.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CF, 6)
    Jump("loc_5035")

    label("loc_4FA6")


    ChrTalk(
        0xC,
        (
            "To receive proactive\x01",
            "cooperation from the Meister...\x01",
            "There's no greater happiness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I've got to do better with\x01",
            "making the foundation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5035")

    Jump("loc_5B2F")

    label("loc_503A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5144")

    ChrTalk(
        0xFE,
        (
            "The stage preparation and automata\x01",
            "the Meister has been helping us with\x01",
            "would be impossible for me alone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, I'll do it somehow\x01",
            "until the stage is arranged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Meister is worried\x01",
            "about it too... I've got\x01",
            "to build it diligently.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B2F")

    label("loc_5144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5299")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_521F")

    ChrTalk(
        0xFE,
        (
            "Now that the stage is\x01",
            "clear of debris, we can\x01",
            "finally practice again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As for my work as the\x01",
            "prop master, the start\x01",
            "point is still far off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, I'll proceed\x01",
            "ahead steadily.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_5294")

    label("loc_521F")


    ChrTalk(
        0xFE,
        (
            "As for my work as the\x01",
            "prop master, the start\x01",
            "point is still far off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, I'll proceed\x01",
            "ahead steadily.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5294")

    Jump("loc_5B2F")

    label("loc_5299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_54A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5408")

    ChrTalk(
        0xFE,
        (
            "The props and automata\x01",
            "the Meister built for us\x01",
            "were all destroyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They were peerless works of art\x01",
            "the Meister and troupe members\x01",
            "poured their souls into...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To trample over them was really\x01",
            "an unforgivable act of violence...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, in the end they are just\x01",
            "works of art. They can be rebuilt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But Miss Ilya is...!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_549F")

    label("loc_5408")


    ChrTalk(
        0xFE,
        (
            "...Anyway, I'll rebuild\x01",
            "the Arc-en-ciel stage\x01",
            "any number of times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I let something like\x01",
            "this break me, I'd have\x01",
            "no excuses for Miss Ilya.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_549F")

    Jump("loc_5B2F")

    label("loc_54A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_55D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5565")

    ChrTalk(
        0xFE,
        (
            "Alright, with this, the\x01",
            "stage setting is perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And I finished rehearsing\x01",
            "the movements yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All that's left is to\x01",
            "wait for the performance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_55D1")

    label("loc_5565")


    ChrTalk(
        0xFE,
        (
            "Alright, with this, the\x01",
            "stage setting is perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All that's left is to\x01",
            "wait for the performance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55D1")

    Jump("loc_5B2F")

    label("loc_55D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_55E4")
    Jump("loc_5B2F")

    label("loc_55E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_55F2")
    Jump("loc_5B2F")

    label("loc_55F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5600")
    Jump("loc_5B2F")

    label("loc_5600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5801")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5753")

    ChrTalk(
        0xFE,
        (
            "The stage setting for the renewal performance I\x01",
            "asked to studio I'm acquainted with will finally\x01",
            "be completed tomorrow. So it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I might have asked for various\x01",
            "impossible things this time, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Meister always pulls\x01",
            "through for me in the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm looking forward to going to get it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_57FC")

    label("loc_5753")


    ChrTalk(
        0xFE,
        (
            "I might have asked for various\x01",
            "impossible things this time, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Meister always pulls through\x01",
            "for me in the end. I'm looking\x01",
            "forward to going to get it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57FC")

    Jump("loc_5B2F")

    label("loc_5801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_59D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_594D")

    ChrTalk(
        0xFE,
        (
            "The new stage setting plan is\x01",
            "complete, so I'm beginning\x01",
            "work on its exact shape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, I have to fit all those\x01",
            "details in between practice for\x01",
            "the renewal performance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In essence, there's only a month\x01",
            "until the performance opening day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I don't hurry, \x01",
            "I won't finish on time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_59CF")

    label("loc_594D")


    ChrTalk(
        0xFE,
        (
            "In essence, there's only \x01",
            "a month until the renewal\x01",
            "performance opening day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I don't hurry, \x01",
            "I won't finish on time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59CF")

    Jump("loc_5B2F")

    label("loc_59D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_59E2")
    Jump("loc_5B2F")

    label("loc_59E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5A96")

    ChrTalk(
        0xFE,
        (
            "To prepare for tomorrow's\x01",
            "performance, we're all on\x01",
            "break until 3PM.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since I have some free time, I was thinking\x01",
            "of going to see the inauguration ceremony.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B2F")

    label("loc_5A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5AA4")
    Jump("loc_5B2F")

    label("loc_5AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5B2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5ABF")
    Call(0, 7)
    Jump("loc_5B2F")

    label("loc_5ABF")


    ChrTalk(
        0xFE,
        "But, a 50% increase...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though of course I'm going to do my\x01",
            "very best, that's another crazy demand...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B2F")

    TalkEnd(0xFE)
    Return()

    # Function_17_4DEE end

    def Function_18_5B33(): pass

    label("Function_18_5B33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5BF4")

    ChrTalk(
        0xFE,
        (
            "It looks like there are supportive\x01",
            "fans in front of the theater even\x01",
            "in a situation like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Miss Ilya's cheering for us too...\x01",
            "Nothing could be more encouraging.\x01\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F60")

    label("loc_5BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5CBD")

    ChrTalk(
        0xFE,
        (
            "We can only perform― \x01",
            "And we're fortunate to have\x01",
            "fans who support us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, there's only one choice. \x01",
            "Even in a situation like this, \x01",
            "we'll train as we usually do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F60")

    label("loc_5CBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5D0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CD8")
    Call(0, 19)
    Jump("loc_5D08")

    label("loc_5CD8")


    ChrTalk(
        0xFE,
        (
            "Let's go, Theodore.\x01",
            "Let's get fired up...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D08")

    Jump("loc_5F60")

    label("loc_5D0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5D1B")
    Jump("loc_5F60")

    label("loc_5D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5DCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D36")
    Call(0, 20)
    Jump("loc_5DC5")

    label("loc_5D36")


    ChrTalk(
        0xFE,
        (
            "Well, having said that,\x01",
            "handling easily any kind of role\x01",
            "is show of my true worth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I must serve a role in accordance with our needs.\x02",
    )

    CloseMessageWindow()

    label("loc_5DC5")

    Jump("loc_5F60")

    label("loc_5DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5F60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EC1")

    ChrTalk(
        0xFE,
        (
            "But, as expected of\x01",
            "Liberl's Queen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Princess Klaudia is sweet too,\x01",
            "but assigning Captain Julia to her\x01",
            "guard is too much of a waste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With her swordplay, \x01",
            "she'd certainly be a star\x01",
            "if she were to join us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5F60")

    label("loc_5EC1")


    ChrTalk(
        0xFE,
        (
            "Captain Julia... With her\x01",
            "figure, it's a waste for\x01",
            "her to be in the military.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With her swordplay, \x01",
            "she'd certainly be a star\x01",
            "if she were to join us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F60")

    TalkEnd(0xFE)
    Return()

    # Function_18_5B33 end

    def Function_19_5F64(): pass

    label("Function_19_5F64")

    OP_4B(0xD, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xD,
        (
            "Alright, Miss Pliｳ.\x01",
            "Can you do your solo for us now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Understood. I'll do super great,\x01",
            "so get excited, you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "...Alright.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_19_5F64 end

    def Function_20_6010(): pass

    label("Function_20_6010")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xD,
        (
            "Alright, Theodore. Our climax\x01",
            "scene's coming up next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You, the altar's guardian, raise\x01",
            "swords against I, the fast liver prince...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Ugh, saying it makes me regretful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I wished this development too\x01",
            "would've been changed for the renewal.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "*sigh*... That's quite a thing\x01",
            "to say at this late date.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's fine. Just shut up and get\x01",
            "along with it, you stupiGene.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "Y-You. Did you just\x01",
            "call me stupiGene?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Then you're stupiDore!\x01",
            "Huh, you stupiDore!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...My bad, so anyway,\x01",
            "adjust to it now.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F(I-I didn't think they'd be like this\x01",
            "right before the performance.)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x10)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_20_6010 end

    def Function_21_631D(): pass

    label("Function_21_631D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_63D9")

    ChrTalk(
        0xFE,
        (
            "Hmm... I feel I'm\x01",
            "very lucky to be\x01",
            "a performer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I owe a lot of things to a lot of people... \x01",
            "I've got to train even harder to repay \x01",
            "each and every one of them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6710")

    label("loc_63D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_63E7")
    Jump("loc_6710")

    label("loc_63E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_644A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6402")
    Call(0, 19)
    Jump("loc_6445")

    label("loc_6402")


    ChrTalk(
        0xFE,
        (
            "Hear that, Eugene? I won't be\x01",
            "cast aside by the likes of you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6445")

    Jump("loc_6710")

    label("loc_644A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6458")
    Jump("loc_6710")

    label("loc_6458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_660A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6473")
    Call(0, 20)
    Jump("loc_6605")

    label("loc_6473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6563")

    ChrTalk(
        0xE,
        (
            "Since forever, Eugene has been agitated\x01",
            "and has had a bad habit of backtalk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I wish he'd give me\x01",
            "a break already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FR-Really?\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xD)

    ChrTalk(
        0xD,
        (
            "Hey, Theo. Don't go\x01",
            "spouting pointless things!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6605")

    label("loc_6563")


    ChrTalk(
        0xFE,
        (
            "Anyway... No matter what kind of performance\x01",
            "it is, the first performance is special.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there's time, I want to go over\x01",
            "the performance one more time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6605")

    Jump("loc_6710")

    label("loc_660A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6710")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66D4")

    ChrTalk(
        0xFE,
        "...Indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard Princess Klaudia has\x01",
            "experience is theater from\x01",
            "when she was a student.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure the majesty of\x01",
            "those two would come\x01",
            "through, even on stage.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6710")

    label("loc_66D4")


    ChrTalk(
        0xFE,
        (
            "Indeed... I'd love\x01",
            "to see those two\x01",
            "on stage sometime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6710")

    TalkEnd(0xFE)
    Return()

    # Function_21_631D end

    def Function_22_6714(): pass

    label("Function_22_6714")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6776")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6732")
    Call(0, 19)
    Jump("loc_6776")

    label("loc_6732")


    ChrTalk(
        0xFE,
        (
            "That's quite an expression you\x01",
            "guys have. I won't lose to you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6776")

    TalkEnd(0xFE)
    Return()

    # Function_22_6714 end

    def Function_23_677A(): pass

    label("Function_23_677A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_678B")
    Jump("loc_69C7")

    label("loc_678B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_68A0")

    ChrTalk(
        0xFE,
        (
            "To do something like that on stage at\x01",
            "a time like this... I have no words...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As for me, I strongly believe that\x01",
            "especially because of this situation\x01",
            "that entertainment is needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of despair, humans become\x01",
            "unable to enjoy amusements, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69C7")

    label("loc_68A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_68FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68BB")
    Call(0, 13)
    Jump("loc_68F8")

    label("loc_68BB")


    ChrTalk(
        0xFE,
        (
            "I'll make my performance more\x01",
            "nimble, more beautiful...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68F8")

    Jump("loc_69C7")

    label("loc_68FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_690B")
    Jump("loc_69C7")

    label("loc_690B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_69C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6926")
    Call(0, 24)
    Jump("loc_69C7")

    label("loc_6926")


    ChrTalk(
        0xFE,
        (
            "Goodness, that Nikol. He never lets down\x01",
            "his guard, and he has no weak points!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This must be a technique of docile\x01",
            "young men. I-I'll never forgive him!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69C7")

    TalkEnd(0xFE)
    Return()

    # Function_23_677A end

    def Function_24_69CB(): pass

    label("Function_24_69CB")

    OP_4B(0x11, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0x11,
        (
            "Now then... If I'm going\x01",
            "to be the foil, I'll be\x01",
            "the best foil I can be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Foil? \x01",
            "You're no foil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "You know I love your acting,\x01",
            "right, senior Celine?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x11)

    ChrTalk(
        0x11,
        (
            "W-W-What're you saying\x01",
            "all of a sudden?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "C-Cut the chatter\x01",
            "and get your acting\x01",
            "together, you idiot!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "...Umm, why such\x01",
            "foul language?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x1, 2)
    Return()

    # Function_24_69CB end

    def Function_25_6B6E(): pass

    label("Function_25_6B6E")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_25_6B6E end

    def Function_26_6B75(): pass

    label("Function_26_6B75")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B9A")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_26_6B75")

    label("loc_6B9A")

    Return()

    # Function_26_6B75 end

    def Function_27_6B9B(): pass

    label("Function_27_6B9B")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01700.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01800.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04200.itp")
    SetChrPos(0x101, 700, 1350, 7760, 0)
    SetChrPos(0x102, -700, 1350, 7760, 0)
    SetChrPos(0x109, 700, 1520, 6680, 0)
    SetChrPos(0x105, -700, 1520, 6680, 0)
    OP_68(-640, 1320, 14170, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13720, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#01702FYou know, if you...\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#12P#04211FC-Cut it out... And in\x01",
            "front of sis Rixia too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#01802FUh uh, Miss Ilya. \x01",
            "You're troubling Sully, right?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 26)
    BeginChrThread(0x9, 0, 0, 26)
    BeginChrThread(0xA, 0, 0, 26)
    OP_68(450, 1620, 11150, 3000)
    MoveCamera(46, 24, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(15050, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#12P#00000FHa ha. Things sure are lively here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100F*giggle*, looks like\x01",
            "they're taking a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FI-It's Ilya Platiｲre! The real Ilya Platiｲre!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FAnd the two near her are...\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x0)
    OP_64(0x8)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        "#01700FHmm...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#01705FAh, it's the younger brother!!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    OP_64(0x9)
    OP_64(0xA)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6F32():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6F32)
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0x9,
        "#5P#01802FOh... Everyone!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7038")
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
            "#1K◆ZnK quest [Stalker Inv. Request]? (Debug)\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No Change]\x01",          # 0
            "[Completed]\x01",          # 1
            "[Not Completed]\x01",      # 2
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
        (0, "loc_701F"),
        (1, "loc_7024"),
        (2, "loc_702E"),
        (SWITCH_DEFAULT, "loc_7038"),
    )


    label("loc_701F")

    Jump("loc_7038")

    label("loc_7024")

    OP_29(0x1D, 0x4, 0x10)
    Jump("loc_7038")

    label("loc_702E")

    OP_29(0x1D, 0x3, 0x10)
    Jump("loc_7038")

    label("loc_7038")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7060")

    ChrTalk(
        0xA,
        "#04200F...Hello.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7077")

    label("loc_7060")


    ChrTalk(
        0xA,
        "#04200F...Hey ya.\x02",
    )

    CloseMessageWindow()

    label("loc_7077")


    def lambda_707C():
        OP_95(0xFE, 700, 1450, 12200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_707C)

    def lambda_7096():
        OP_95(0xFE, -700, 1450, 11760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7096)

    def lambda_70B0():
        OP_95(0xFE, 700, 1450, 10980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_70B0)

    def lambda_70CA():
        OP_95(0xFE, -700, 1450, 10680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_70CA)
    OP_68(-820, 1620, 12730, 3000)
    MoveCamera(39, 26, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(13510, 3000)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#12P#00000FHa ha, it's been awhile.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FSorry, it looks like we\x01",
            "interrupted your break...\x02",
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
        0x8,
        (
            "Uh uh, not at all㈱\x02\x03",
            "It's been awhile and you came\x01",
            "to see us. Take it easy!\x02\x03",
            "Ah, but since you're here,\x01",
            "can I get a reunion hug\x01",
            "from the younger brother?\x02",
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
        "#12P#00012FN-No no, I'll pass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01702FAww, really? You don't have\x01",
            "to hold back, you know.\x02\x03",
            "#01709FUh uh, or possibly... \x01",
            "Might you prefer the feeling \x01",
            "of a hug from Rixia instead?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x9)

    def lambda_739F():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_739F)
    Sleep(50)

    def lambda_73AF():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_73AF)

    ChrTalk(
        0x101,
        "#12P#00011FU-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#01806FM-Miss Ilya...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12P#04200FDamn. Stop acting like a dirty old man.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 500)

    ChrTalk(
        0x102,
        (
            "#12P#00109F*giggle*... Looks like\x01",
            "you have it tough as\x01",
            "always, Miss Rixia.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "A-Ahaha...\x01",
            "It might be what\x01",
            "they call fate.\x02\x03",
            "But, I'm glad to see all\x01",
            "of you after so long.\x02\x03",
            "Uh uh. Please support\x01",
            "us again from here on.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x105,
        (
            "#12P#10304FHu hu. Miss Rixia, you're the artist that\x01",
            "made her debut at the Anniversary\x01",
            "Festival performance, right?\x02\x03",
            "#10302FYou live in a Downtown apartment,\x01",
            "if I remember correctly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#01802FY-Yes...\x02\x03",
            "#01805FUmm, and you are... \x01",
            "That delinquent group in Downtown's...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWazy Hemisphere. Hu hu, I'm\x01",
            "honored to make your acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01705FOh, you know him, Rixia?\x02\x03",
            "Now that you mention it, those\x01",
            "two weren't with you before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes. They're our\x01",
            "new members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FI-I'm Noｱl Seeker.\x01",
            "I transferred to the SSS\x01",
            "from the Guardian Force!\x02\x03",
            "#10109FUmm... My younger sister\x01",
            "Fran and I are always\x01",
            "cheering for you, Miss Ilya!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#01709FUh uh, thanks☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FTio and Randy\x01",
            "aren't back yet.\x02\x03",
            "#00100FIt'll be just the four\x01",
            "of us for awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01700FI see.\x02\x03",
            "#01709FUh uh, looks like you've got some\x01",
            "pretty eccentric faces there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FW-Well...\x01",
            "They couldn't rival you\x01",
            "though, Miss Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FYou artists are a lot\x01",
            "more straightforward\x01",
            "than I thought you'd be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FIndeed. And you're even\x01",
            "more beautiful in person\x01",
            "than in the magazines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01702FUh uh, thanks. But you\x01",
            "know flattery won't get\x01",
            "you anything, right?\x02\x03",
            "#01703FWell, that aside...\x02\x03",
            "#01709FHey. You've been quiet this whole time. \x01",
            "Give a proper greeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P#04205F...I-I know already.\x02",
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xA,
        (
            "I'm Sully Atraid, an\x01",
            "assistant in this troupe.\x02\x03",
            "Umm... Nice to meet you.\x02",
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
        0x109,
        "#12P#10100FUh uh, same here Sully.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8060")

    ChrTalk(
        0x101,
        "#12P#00000FHa ha. How have you been, Sully?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        (
            "#5P#04203FHmph, don't smile when you talk to me.\x02\x03",
            "#04201FLet me just say this. I haven't forgotten\x01",
            "what happened back then, you hear?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00006F(S-She's still angry about that, huh...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FUmm, back then...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01709FUmm, if I'm remembering it right, the younger\x01",
            "brother here grabbed her from behind and──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00011FN-No, it wasn't like that...\x02\x03",
            "#00006FAnyway, Sully was the cause of the \x01",
            "whole thing in the first place, right!?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#5P#04205FW-What!?\x02\x03",
            "#04208F...I-I may have been\x01",
            "in the wrong, but...\x02\x03",
            "#04201FHow dare you grab me\x01",
            "so tightly like that...!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7EAD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7EAD)
    Sleep(50)

    def lambda_7EBD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7EBD)
    Sleep(50)
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x109,
        "#12P#10105FG-Grab...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, sounds like\x01",
            "something fun went on.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#12P#00011FN-No! You see...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01709FOh, a battle! This doesn't happen\x01",
            "often, so I'm joining in too──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#01806FM-Miss Ilya... You're making\x01",
            "this more complicated.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006F(Ooh. The more I\x01",
            "deny it, the more\x01",
            "guilty I look...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_840F")

    label("loc_8060")


    ChrTalk(
        0x101,
        "#12P#00005FHuh? Now that I see Sully better...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00011F#4SS-She's a girl!?#3S\x02\x03",
            "#00003FO-Oh. I've come\x01",
            "here many times,\x01",
            "but never realized.\x02\x03",
            "#00000FYeah, taking a closer look at her, \x01",
            "she does have a cute face...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_81F1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_81F1)
    Sleep(50)

    def lambda_8201():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8201)
    Sleep(50)

    def lambda_8211():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8211)
    Sleep(50)

    def lambda_8221():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8221)
    Sleep(50)

    def lambda_8231():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8231)
    Sleep(50)
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        "#5P#04201FY-You jerk...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P#01806FM-Mr. Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00111F...As expected, that was rude.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#11P#00011FAh, sorry! Since you speak like\x01",
            "a boy I unconsciously thought...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#01709FAhaha, that's our younger brother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHmm, that could be a pattern for\x01",
            "an airhead gigolos to use, right?\x01",
            "I've learned something here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        "#5P#00011FN-No, it's not that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P#04203F...Hmph, I don't like him.\x02",
    )

    CloseMessageWindow()

    label("loc_840F")


    ChrTalk(
        0x9,
        (
            "#5P#01803FUh uh, but even so...\x01",
            "I'm glad you are are doing well.\x02\x03",
            "#01809FThe Support Section has done\x01",
            "so much for us already. \x01",
            "Please feel free to visit anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01700FYeah, I'll give you a warm welcome too.\x02\x03",
            "#01704FAnd besides, it's more fun watching\x01",
            "Rixia's training these days.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_85B9():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_85B9)
    Sleep(50)

    def lambda_85C9():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_85C9)
    Sleep(50)

    def lambda_85D9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_85D9)
    Sleep(50)

    def lambda_85E9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_85E9)
    Sleep(50)

    def lambda_85F9():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_85F9)
    Sleep(50)
    TurnDirection(0xA, 0x8, 500)

    ChrTalk(
        0x101,
        "#12P#00005FWow, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu. To be specific, it seems\x01",
            "like the jumps during her\x01",
            "performances are the highlights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FH-Hey now, Wazy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P#01802FA-Ahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01709FUh uh, there is that too, of course.\x02\x03",
            "#01704FLately, I feel there's a sharpness\x01",
            "even to her ordinary movements.\x02\x03",
            "#01702FI never get the feeling she's\x01",
            "tired either. I guess you've\x01",
            "improved the way you rest?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#11P#01809FU-Umm, well,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)

    ChrTalk(
        0xA,
        (
            "#6P#04205FSo that's it, huh.\x01",
            "I never realized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100F*giggle*, it looks like even Miss Ilya's\x01",
            "perception is on a whole other level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#01803F(...Indeed. Because I haven't\x01",
            "been "working" recently, I've\x01",
            "had more time for rest...)\x02\x03",
            "#01808F(If Miss Ilya can sense that just from the\x01",
            "way I move, she really is amazing...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FHa ha. You sure are a\x01",
            "hard worker, Rixia...\x02\x03",
            "Make sure you get proper rest and\x01",
            "take care of yourself from now on.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_89CC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_89CC)
    Sleep(50)
    TurnDirection(0xA, 0x102, 500)

    ChrTalk(
        0x9,
        "#5P#01802FI will. And thank you for your concern.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FBut, Arc-en-ciel always\x01",
            "seems so busy...\x02\x03",
            "#00100FWe might stop by\x01",
            "only so often that\x01",
            "it's not a bother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01702FUh uh. Rehearsals\x01",
            "aren't performances.\x01",
            "Stop by anytime.\x02\x03",
            "#01703FWell, it does look like we'll\x01",
            "be busy going forward, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(30)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(30)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#12P#10105FUmm... Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FAre you thinking of\x01",
            "something interesting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01709FUh uh, it's still a s-e-c-r-e-t㈱\x02\x03",
            "#01700FWell, look forward to what\x01",
            "we have planned, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FHa ha, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100F*giggle*, I'll have to\x01",
            "check up on that.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0x9, 0, 0, 0)
    BeginChrThread(0xA, 0, 0, 0)
    OP_93(0x9, 0x0, 0x0)
    OP_93(0xA, 0x0, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x137, 2)
    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_27_6B9B end

    def Function_28_8CED(): pass

    label("Function_28_8CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 6)), scpexpr(EXPR_END)), "loc_8CFA")
    Call(0, 29)
    Return()

    label("loc_8CFA")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, -60420, 0, 3700, 90)
    SetChrPos(0x102, -60920, 0, 2700, 90)
    SetChrPos(0x103, -61420, 0, 1700, 90)
    SetChrPos(0x104, -61390, 0, 3700, 90)
    SetChrPos(0x105, -62090, 0, 2700, 90)
    SetChrPos(0x109, -62390, 0, 1700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_68(-61380, 1500, 2260, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17600, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#5P#00000FRixia and Sully...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FSully, that's Sully's "Star\x01",
            "Princess" costume, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00202F...Pretty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305FBut that Sullboy...\x01",
            "Doesn't she look flustered?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(10, 2900, 24580, 0)
    MoveCamera(0, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    TurnDirection(0xA, 0xB, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#12206FHah hah hah...\x02\x03",
            "#12201FSay, Troupe Chief.\x01",
            "Isn't it just perfect?\x02\x03",
            "Miss Ilya will have no choice\x01",
            "but to acknowledge me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6PHmm. You pass\x01",
            "of course, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12206F*sigh*, that again?\x02\x03",
            "#12200FHey, sis Rixia. \x01",
            "What do you think?\x02\x03",
            "#12202FDid I make some mistake\x01",
            "in my movements?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#06203FHmm...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#06202F...Say, Sully.\x02\x03",
            "I wonder if you can put more\x01",
            "emotions into it next time.\x02\x03",
            "#06204FPicture "how you want\x01",
            "it to be"... I can't\x01",
            "explain it well.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#12201F"How I want it to be"... \x01",
            "S-Specifically, what should I do?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-61380, 1500, 2260, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17600, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#5P#00005F(Sully...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300F(Hmm. Seems like\x01",
            "we should leave.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103F(Yeah... \x01",
            "We can't interrupt.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetChrPos(0x0, -62880, 0, 2950, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x16D, 6)
    EventEnd(0x5)
    Return()

    # Function_28_8CED end

    def Function_29_91ED(): pass

    label("Function_29_91ED")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F(Rixia and Sully...\x01",
            "It seems they're\x01",
            "focuses on training.)\x02\x03",
            "#00003F(We shouldn't interrupt them now.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -62880, 0, 2950, 270)
    EventEnd(0x4)
    Return()

    # Function_29_91ED end

    def Function_30_9278(): pass

    label("Function_30_9278")

    EventBegin(0x0)
    Fade(500)
    OP_68(-6140, 16219, -4030, 0)
    MoveCamera(355, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17490, 0)
    SetChrPos(0x101, -5460, 15200, -4290, 315)
    SetChrPos(0x102, -6310, 15200, -5170, 0)
    SetChrPos(0x103, -7650, 15200, -4870, 45)
    SetChrPos(0x104, -4700, 15200, -5320, 315)
    SetChrPos(0x105, -8080, 15200, -6150, 45)
    SetChrPos(0x109, -3880, 15200, -6340, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x8, 0x2D, 0x0)
    OP_4B(0x8, 0xFF)
    OP_0D()

    ChrTalk(
        0x8,
        "#5P#01703F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FMiss Ilya... So this\x01",
            "is where you were.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x102, 500)

    ChrTalk(
        0x8,
        (
            "#5P#01705FAh, it's the younger brother and friends.\x02\x03",
            "#01709FUh uh. Did you come to encourage\x01",
            "us for the renewal performance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100F*giggle*, something like that.\x02\x03",
            "Miss Ilya, it looks like you're\x01",
            "watching Miss Rixia and\x01",
            "Sully training from here?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5P#01704FYes. I can get a good view of the\x01",
            "whole thing from these 2F seats.\x02\x03",
            "#01702FAh, but even so, it's\x01",
            "good to see those young\x01",
            "kids doing their best.\x02\x03",
            "Seeing them like that somehow\x01",
            "reminds me of when I was a newbie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FWhen you were a newbie, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00302FHa ha, that's kinda hard to imagine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHu hu, feel free to tell us about\x01",
            "back then, if you like.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)

    ChrTalk(
        0x8,
        (
            "#5P#01700FUh uh, I don't mind, but...\x01",
            "It's not that interesting anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FWow... Please, tell us about it!!\x02\x03",
            "#10100FIf I recall, all the magazines were\x01",
            "saying how great expectations for\x01",
            "you were when you debuted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00205FI see. So it was ever since your debut.\x02\x03",
            "#00202FBy the way... What was\x01",
            "your reason for wanting\x01",
            "to be an artist?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01703FHmm, that's right.\x02\x03",
            "#01700FI think it was because\x01",
            "I saw Arc-en-ciel\x01",
            "performances as a kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FI see, and you wanted to\x01",
            "emulate them── Is that it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01703FUmm, I think it wasn't that, exactly.\x02\x03",
            "#01700FAt that time, the productions were amazing\x01",
            "because of the artists' performances and\x01",
            "their elaborate sets, but...\x02\x03",
            "#01706FWhen they were over, I thought\x01",
            "there was something missing,\x01",
            "and I couldn't accept it.\x02",
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
        "#12P#00011FC-Couldn't accept it, you say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01700FBut just about everyone in the neighborhood\x01",
            "said how amazing they were. I thought it\x01",
            "must be some kind of huge mistake, but...\x02\x03",
            "#01703FI mean, even I could put\x01",
            "on a better performance!\x01",
            "That's what I thought.\x02\x03",
            "#01702FUh uh. That must've seemed\x01",
            "weird at the time, because I\x01",
            "was a total amateur back then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FWow, so even when you were little you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHmm, but because of that, when\x01",
            "you knocked at the Arc-en-ciel's doors,\x01",
            "you had many conflicts with them, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01706FWell, that's about it,\x01",
            "since me, an untalented newbie,\x01",
            "was constantly interfering.\x02\x03",
            "#01700FBut, I absolutely\x01",
            "believed my performances\x01",
            "could be even better.\x02\x03",
            "#01709FI believed that if I kept showing them that,\x01",
            "they would've naturally understood my point\x01",
            "and even frictions would've vanished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FI see... And so that is\x01",
            "how you came to be\x01",
            "who you are now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01704FUh uh. Although there's no play\x01",
            "I'm convinced it was perfect, yet.\x02\x03",
            "#01702FBut, since the promising raw materials\x01",
            "called Rixia and Sully came in...\x02\x03",
            "I was thinking of\x01",
            "making an ultimate\x01",
            "performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FHa ha. Should I say that\x01",
            "you're greedy, Miss Ilya....?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104F*giggle*. "There is no genius\x01",
            "that bests hard work"...\x02\x03",
            "#00109FAnd you're a genius at hard\x01",
            "work, Miss Ilya. There's really\x01",
            "no one who can compete with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00309FYeah, you could say that again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01709FUh uh. Looks like I told\x01",
            "you something boring.\x02\x03",
            "#01704FIf you like, come\x01",
            "see our renewal\x01",
            "performance too.\x02\x03",
            "#01700FRixia and Sully will be in it too... \x01",
            "It'll be our best performance yet.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FYes, of course.\x02\x03",
            "#00000FThe ultimate performance with the three\x01",
            "of you... We'll be looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0x2D, 0x0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x17C, 3)
    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -5420, 15200, -4850, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_30_9278 end

    def Function_31_A122(): pass

    label("Function_31_A122")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    SetChrPos(0x101, 700, 1350, 7760, 0)
    SetChrPos(0x102, -700, 1350, 7760, 0)
    SetChrPos(0x109, 700, 1520, 6680, 0)
    SetChrPos(0x105, -700, 1520, 6680, 0)
    SetChrPos(0x103, 700, 1620, 5680, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(0, 1320, 13820, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x0, 500)

    ChrTalk(
        0xB,
        "Oh, it's you all...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A250():
        TurnDirection(0x8, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A250)

    def lambda_A25D():
        TurnDirection(0x9, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A25D)
    TurnDirection(0xA, 0x0, 500)

    def lambda_A271():
        OP_95(0xFE, 700, 1450, 12200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A271)

    def lambda_A28B():
        OP_95(0xFE, -700, 1450, 11760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A28B)

    def lambda_A2A5():
        OP_95(0xFE, 700, 1450, 10980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A2A5)

    def lambda_A2BF():
        OP_95(0xFE, -700, 1450, 10680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A2BF)

    def lambda_A2D9():
        OP_95(0xFE, 700, 1450, 9980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A2D9)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x8,
        "#01705FMy, if it isn't the younger brother and friends.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#04205FW-What do you want?\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)

    ChrTalk(
        0x9,
        "#01808F.........\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)
    Sleep(1000)
    TurnDirection(0x102, 0x9, 500)

    ChrTalk(
        0x101,
        "#00003FRixia...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FMiss Rixia...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        (
            "#01705FWhat's this now? Is there something\x01",
            "between you and the younger brother, Rixia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01803F―No...\x02\x03",
            "#01801FMore importantly, Miss Ilya, there's not\x01",
            "much time until the performance.\x02\x03",
            "I want to check the choreography\x01",
            "of our duet one more time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 500)

    ChrTalk(
        0xA,
        (
            "#04200FYeah, Miss Ilya!\x02\x03",
            "I already have that\x01",
            "part down cold.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#01705FOh, right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        (
            "#01703FWell then guys, if you don't\x01",
            "need anything important,\x01",
            "can I ask you to leave us?\x02\x03",
            "#01700FI can't let our concentration\x01",
            "be broken now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A5E0():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A5E0)
    TurnDirection(0x102, 0x8, 500)

    ChrTalk(
        0x101,
        "#00003FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...We're very sorry \x01",
            "to have bothered you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0x0, 0x0)
    OP_93(0xA, 0x0, 0x0)
    OP_93(0xB, 0x87, 0x0)
    SetScenarioFlags(0x16D, 7)
    ModifyEventFlags(0, 2, 0x80)
    EventEnd(0x5)
    Return()

    # Function_31_A122 end

    def Function_32_A686(): pass

    label("Function_32_A686")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-3290, 3950, 17840, 0)
    MoveCamera(22, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15820, 0)
    LoadChrToIndex("chr/ch14150.itc", 0x37)
    LoadChrToIndex("chr/ch14151.itc", 0x38)
    LoadChrToIndex("chr/ch14152.itc", 0x39)
    LoadChrToIndex("chr/ch14153.itc", 0x3A)
    LoadChrToIndex("chr/ch14154.itc", 0x3B)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0xD, 0xB)
    SetChrChipByIndex(0xE, 0xC)
    SetChrChipByIndex(0xF, 0xD)
    SetChrChipByIndex(0x10, 0xF)
    SetChrChipByIndex(0x11, 0x11)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0xB, 170, 450, 11640, 0)
    SetChrPos(0xD, -390, 1250, 19660, 90)
    SetChrPos(0xE, 900, 1250, 20710, 180)
    SetChrPos(0xF, 2040, 1250, 20500, 225)
    SetChrPos(0x10, 280, 1250, 18560, 45)
    SetChrPos(0x11, 1940, 1250, 18990, 315)
    SetChrPos(0xC, -3110, 1250, 19110, 60)
    SetChrPos(0x12, -1810, 1250, 19900, 240)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0x101, -600, 2700, -4000, 0)
    SetChrPos(0x102, 600, 2700, -4100, 0)
    SetChrPos(0x103, -600, 2700, -4000, 0)
    SetChrPos(0x104, 600, 2700, -4100, 0)
    SetChrPos(0xF4, -600, 2700, -4000, 0)
    SetChrPos(0xF5, 600, 2700, -4100, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x37)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 2500, 1250, 25450, 0)
    BeginChrThread(0x0, 0, 0, 49)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_A8D6():
        OP_95(0xFE, -600, 2700, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A8D6)

    def lambda_A8F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A8F0)
    Sleep(100)

    def lambda_A904():
        OP_95(0xFE, 600, 2700, 900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A904)

    def lambda_A91E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A91E)
    Sleep(500)

    def lambda_A932():
        OP_95(0xFE, -750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A932)

    def lambda_A94C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A94C)
    Sleep(100)
    OP_68(-1660, 3950, 2020, 4000)
    MoveCamera(33, 8, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(15070, 4000)

    def lambda_A98E():
        OP_95(0xFE, 750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A98E)

    def lambda_A9A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A9A8)
    Sleep(500)

    def lambda_A9BC():
        OP_95(0xFE, -500, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_A9BC)

    def lambda_A9D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_A9D6)
    Sleep(100)

    def lambda_A9EA():
        OP_95(0xFE, 770, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_A9EA)

    def lambda_AA04():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_AA04)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00002FThat's...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAA1")

    ChrTalk(
        0x10A,
        (
            "#12P#00602FThe "Golden Sun, Silver Moon"\x01",
            "additional scene, huh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAE8")

    label("loc_AAA1")


    ChrTalk(
        0x109,
        (
            "#12P#10102FThe "Golden Sun, Silver Moon"\x01",
            "additional scene, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAE8")


    ChrTalk(
        0x103,
        "#12P#00202FMiss Sully is amazing...\x02",
    )

    CloseMessageWindow()
    OP_68(150, 4650, 13120, 3000)
    MoveCamera(0, 10, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(10510, 3000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(660, 820, 13410, 0)
    MoveCamera(33, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17510, 0)
    SetChrPos(0x101, -530, 1810, 5540, 0)
    SetChrPos(0x102, 480, 1800, 5350, 0)
    SetChrPos(0x103, -790, 2160, 4170, 0)
    SetChrPos(0x104, 730, 2240, 4050, 0)
    SetChrPos(0xF4, -400, 2240, 2900, 0)
    SetChrPos(0xF5, 680, 2240, 2900, 0)
    OP_0D()

    def lambda_ABE3():
        OP_95(0xFE, -550, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ABE3)

    def lambda_ABFD():
        OP_95(0xFE, 620, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ABFD)

    def lambda_AC17():
        OP_95(0xFE, -720, 1330, 8470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AC17)

    def lambda_AC31():
        OP_95(0xFE, 650, 1310, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AC31)

    def lambda_AC4B():
        OP_95(0xFE, -570, 1350, 7280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_AC4B)

    def lambda_AC65():
        OP_95(0xFE, 590, 1350, 7240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_AC65)
    Sleep(1000)
    OP_4B(0xB, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0xB,
        "#5POh, you all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FTroupe chief, it's been awhile.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FIt seems everyone is\x01",
            "concentrating on their training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PYes. It seems like the\x01",
            "performance with Sully at\x01",
            "the center is taking shape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PFor now anyway, we are doing our\x01",
            "best to restart performances as\x01",
            "soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PI heard Ilya has awoken...\x01",
            "We must do our best to live up\x01",
            "to her expectations as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FI see... So that's how it is.\x02\x03",
            "#00008F(Come to think of it, no\x01",
            "one in the troupe knows\x01",
            "Rixia's location.)\x02\x03",
            "#00003F(I would've wanted to\x01",
            "show them her face, but...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xA, 0x0)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xA, 0x3)
    EndChrThread(0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 10, 900, 9380, 0)
    SetScenarioFlags(0x1CF, 4)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AFE7")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xD, 3520, 1250, 22730, 90)
    SetChrPos(0xE, 4800, 1250, 22730, 270)
    SetChrPos(0xA, 0, 1250, 27230, 0)
    SetChrChipByIndex(0xA, 0x14)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrChipByIndex(0xD, 0xB)
    SetChrChipByIndex(0xE, 0xC)
    SetChrChipByIndex(0x10, 0xF)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_B075")

    label("loc_AFE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B075")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xB, 0, 0, 15300, 0)
    SetChrPos(0xD, 0, 1250, 27300, 180)
    SetChrPos(0xF, -1390, 1250, 26170, 90)
    SetChrPos(0x11, 1390, 1250, 26170, 270)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)

    label("loc_B075")

    Sleep(1000)
    EventEnd(0x5)
    SetScenarioFlags(0x22, 2)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_32_A686 end

    def Function_33_B087(): pass

    label("Function_33_B087")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(610, 1520, 13160, 0)
    MoveCamera(43, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17510, 0)
    LoadChrToIndex("chr/ch14150.itc", 0x37)
    LoadChrToIndex("chr/ch14151.itc", 0x38)
    LoadChrToIndex("chr/ch14152.itc", 0x39)
    LoadChrToIndex("chr/ch14153.itc", 0x3A)
    LoadChrToIndex("chr/ch14154.itc", 0x3B)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0xD, 0xB)
    SetChrChipByIndex(0xE, 0xC)
    SetChrChipByIndex(0xF, 0xD)
    SetChrChipByIndex(0x10, 0xF)
    SetChrChipByIndex(0x11, 0x11)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0xB, 170, 450, 11640, 0)
    SetChrPos(0xD, -390, 1250, 19660, 90)
    SetChrPos(0xE, 900, 1250, 20710, 180)
    SetChrPos(0xF, 2040, 1250, 20500, 225)
    SetChrPos(0x10, 280, 1250, 18560, 45)
    SetChrPos(0x11, 1940, 1250, 18990, 315)
    SetChrPos(0xC, -3110, 1250, 19110, 60)
    SetChrPos(0x12, -1810, 1250, 19900, 240)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0x101, -530, 1810, 5540, 0)
    SetChrPos(0x102, 480, 1800, 5350, 0)
    SetChrPos(0x103, -790, 2160, 4170, 0)
    SetChrPos(0x104, 730, 2240, 4050, 0)
    SetChrPos(0xF4, -400, 2240, 2900, 0)
    SetChrPos(0xF5, 680, 2240, 2900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x37)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 2500, 1250, 25450, 0)
    BeginChrThread(0x0, 0, 0, 49)

    def lambda_B28B():
        OP_95(0xFE, -550, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B28B)

    def lambda_B2A5():
        OP_95(0xFE, 620, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B2A5)

    def lambda_B2BF():
        OP_95(0xFE, -720, 1330, 8470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B2BF)

    def lambda_B2D9():
        OP_95(0xFE, 650, 1310, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B2D9)

    def lambda_B2F3():
        OP_95(0xFE, -570, 1350, 7280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_B2F3)

    def lambda_B30D():
        OP_95(0xFE, 590, 1350, 7240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_B30D)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_4B(0xB, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0xB,
        "#5PYou all...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PHow about it? Isn't their drive just amazing?\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#11PFor now anyway, we are doing\x01",
            "our best to resume performances\x01",
            "as quickly as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PI heard Ilya has awoken...\x01",
            "We must do our best to live up\x01",
            "to her expectations as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F(...No one in the\x01",
            "troupe knows\x01",
            "Rixia's location.)\x02\x03",
            "#00008F(I would've wanted to\x01",
            "show them her face, but...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    SetScenarioFlags(0x22, 2)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_33_B087 end

    def Function_34_B512(): pass

    label("Function_34_B512")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-3290, 3950, 17840, 0)
    MoveCamera(22, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15820, 0)
    LoadChrToIndex("chr/ch14150.itc", 0x37)
    LoadChrToIndex("chr/ch14151.itc", 0x38)
    LoadChrToIndex("chr/ch14152.itc", 0x39)
    LoadChrToIndex("chr/ch14153.itc", 0x3A)
    LoadChrToIndex("chr/ch14154.itc", 0x3B)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0xD, 0xB)
    SetChrChipByIndex(0xE, 0xC)
    SetChrChipByIndex(0xF, 0xD)
    SetChrChipByIndex(0x10, 0xF)
    SetChrChipByIndex(0x11, 0x11)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0xB, 170, 450, 11640, 0)
    SetChrPos(0xD, -390, 1250, 19660, 90)
    SetChrPos(0xE, 900, 1250, 20710, 180)
    SetChrPos(0xF, 2040, 1250, 20500, 225)
    SetChrPos(0x10, 280, 1250, 18560, 45)
    SetChrPos(0x11, 1940, 1250, 18990, 315)
    SetChrPos(0xC, -3110, 1250, 19110, 60)
    SetChrPos(0x12, -1810, 1250, 19900, 240)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0x101, -600, 2700, -4000, 0)
    SetChrPos(0x102, 600, 2700, -4100, 0)
    SetChrPos(0x103, -600, 2700, -4000, 0)
    SetChrPos(0x104, 600, 2700, -4100, 0)
    SetChrPos(0xF4, -600, 2700, -4000, 0)
    SetChrPos(0xF5, 600, 2700, -4100, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x37)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 2500, 1250, 25450, 0)
    BeginChrThread(0x0, 0, 0, 49)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_B762():
        OP_95(0xFE, -600, 2700, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B762)

    def lambda_B77C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B77C)
    Sleep(100)

    def lambda_B790():
        OP_95(0xFE, 600, 2700, 900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B790)

    def lambda_B7AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B7AA)
    Sleep(500)

    def lambda_B7BE():
        OP_95(0xFE, -750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B7BE)

    def lambda_B7D8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B7D8)
    Sleep(100)
    OP_68(-1660, 3950, 2020, 4000)
    MoveCamera(33, 8, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(15070, 4000)

    def lambda_B81A():
        OP_95(0xFE, 750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B81A)

    def lambda_B834():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B834)
    Sleep(500)

    def lambda_B848():
        OP_95(0xFE, -500, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_B848)

    def lambda_B862():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_B862)
    Sleep(100)

    def lambda_B876():
        OP_95(0xFE, 770, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_B876)

    def lambda_B890():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_B890)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA0F")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00000FThat's...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B937")

    ChrTalk(
        0x10A,
        (
            "#12P#00602FThe "Golden Sun, Silver Moon"\x01",
            "additional scene, huh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E1")

    label("loc_B937")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B993")

    ChrTalk(
        0x109,
        (
            "#12P#10102FThe "Golden Sun, Silver Moon"\x01",
            "additional scene, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E1")

    label("loc_B993")


    ChrTalk(
        0x105,
        (
            "#12P#10402FHu hu, the "Golden Sun, Silver\x01",
            "Moon" additional scene, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9E1")


    ChrTalk(
        0x103,
        "#12P#00202FMiss Sully is amazing...\x02",
    )

    CloseMessageWindow()
    Jump("loc_BA6E")

    label("loc_BA0F")


    ChrTalk(
        0x101,
        (
            "#12P#00000FLooks like everyone's\x01",
            "practicing hard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10702F...Sully, everyone...\x02",
    )

    CloseMessageWindow()

    label("loc_BA6E")

    OP_68(150, 4650, 13120, 3000)
    MoveCamera(0, 10, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(10510, 3000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(660, 820, 13410, 0)
    MoveCamera(33, 23, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17510, 0)
    SetChrPos(0x101, -530, 1810, 5540, 0)
    SetChrPos(0x102, 480, 1800, 5350, 0)
    SetChrPos(0x103, -790, 2160, 4170, 0)
    SetChrPos(0x104, 730, 2240, 4050, 0)
    SetChrPos(0xF4, -400, 2240, 2900, 0)
    SetChrPos(0xF5, 680, 2240, 2900, 0)
    OP_0D()

    def lambda_BB40():
        OP_95(0xFE, -550, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BB40)

    def lambda_BB5A():
        OP_95(0xFE, 620, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BB5A)

    def lambda_BB74():
        OP_95(0xFE, -720, 1330, 8470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BB74)

    def lambda_BB8E():
        OP_95(0xFE, 650, 1310, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BB8E)

    def lambda_BBA8():
        OP_95(0xFE, -570, 1350, 7280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_BBA8)

    def lambda_BBC2():
        OP_95(0xFE, 590, 1350, 7240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_BBC2)
    Sleep(1000)
    OP_4B(0xB, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC29")

    ChrTalk(
        0xB,
        "#5POh, it's you all...\x02",
    )

    CloseMessageWindow()
    Jump("loc_BC46")

    label("loc_BC29")


    ChrTalk(
        0xB,
        "#5PAh, it's you all...?\x02",
    )

    CloseMessageWindow()

    label("loc_BC46")

    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#5PRixia! \x01",
            "If it isn't Rixia!\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0xA, 0x0)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xA, 0x3)
    EndChrThread(0x0, 0x0)
    Fade(500)
    SetChrChipByIndex(0xA, 0x10)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -50, 1250, 25080, 0)
    OP_0D()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#5P#N#12211FSis Rixia...?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_4B(0xF, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_68(400, 1520, 13900, 2000)
    MoveCamera(34, 16, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(17510, 2000)

    def lambda_BD45():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BD45)
    Sleep(50)

    def lambda_BD55():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_BD55)
    Sleep(50)

    def lambda_BD65():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_BD65)
    Sleep(50)

    def lambda_BD75():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_BD75)
    Sleep(50)

    def lambda_BD85():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_BD85)
    Sleep(50)

    def lambda_BD95():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_BD95)
    Sleep(50)

    def lambda_BDA5():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BDA5)
    Sleep(50)

    def lambda_BDB5():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_BDB5)
    Sleep(100)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        "#5PIt's really you. It's really Rixia!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PHa ha, there's no mistake, is there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5P...There's no mistake. It's really her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PUh uh. Now our\x01",
            "last worry has gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#12P#10717F...Everyone...\x02\x03",
            "#10703F...Umm, I'm really sorry.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(10, 1670, 17720, 0)
    MoveCamera(46, 9, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14860, 0)
    SetChrPos(0xB, 650, 0, 15670, 225)
    SetChrPos(0xA, -730, 0, 15940, 180)
    SetChrPos(0x12, -1810, 1250, 19920, 180)
    SetChrPos(0xC, -3020, 1250, 19410, 180)
    SetChrPos(0xD, -1000, 1250, 18840, 180)
    SetChrPos(0xE, -590, 1250, 20230, 180)
    SetChrPos(0xF, 1170, 1250, 20400, 180)
    SetChrPos(0x101, 620, 0, 14370, 315)
    SetChrPos(0x106, -630, 0, 14440, 0)
    SetChrPos(0x102, -780, 450, 12770, 0)
    SetChrPos(0x103, 700, 450, 12660, 0)
    SetChrPos(0x104, -770, 450, 11500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C0BC")
    SetChrPos(0x10A, 680, 500, 11260, 0)
    Jump("loc_C0F3")

    label("loc_C0BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C0E2")
    SetChrPos(0x109, 680, 500, 11260, 0)
    Jump("loc_C0F3")

    label("loc_C0E2")

    SetChrPos(0x105, 680, 500, 11260, 0)

    label("loc_C0F3")

    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#5PThat's right, you're with the\x01",
            "Support Section right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#12P#10708FYes. I can't tell you\x01",
            "everything right now, but...\x02\x03",
            "#10710FWhen the time comes, I will take\x01",
            "responsibility for everything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PUh uh. Oh, Rixia.\x01",
            "Your expression says you're holding \x01",
            "back a lot of emotion, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#12P#10712FEh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PThat's right. No one's going\x01",
            "to be happy with that\x01",
            "expression on your face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PYeah, seriously. \x01",
            "And you're such a beauty, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#12P#10718FMiss Pliｳ... \x01",
            "Miss Celine, Mr. Nikol...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PAnyway... \x01",
            "Do what you have to\x01",
            "and return to us ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PSeriously. There's a performance\x01",
            "I too want to try with you, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10716FMr. Theodore, Mr. Eugene...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PUh uh. I'll get your costume\x01",
            "ready for you, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PAnd the set will be ready. You can be sure of that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10715FMiss Karelia, Mr. Heintz...\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(500)
    OP_68(-630, 1070, 15110, 2000)
    MoveCamera(56, 21, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(11060, 2000)
    OP_6F(0x79)
    OP_64(0xA)

    ChrTalk(
        0xA,
        "#12208F...Sis Rixia...\x02",
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#12P#10716FSully...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12206FThis is... Arc-en-ciel is...\x01",
            "...The place where you belong, sis Rixia.\x02\x03",
            "#12212FI don't know what kind of\x01",
            "burden you're carrying, but...\x02\x03",
            "#12210FThis is the place that sis\x01",
            "Rixia...and Miss Ilya and\x01",
            "I must return to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10718F...Sully...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12212FI... No matter what happens, \x01",
            "I'll protect this place... So please...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#12P#10715FYeah... Yeah...\x02\x03",
            "#10716F...I understand how you\x01",
            "feel very well, Sully.\x02\x03",
            "#10716FI'll return... It's a promise,\x01",
            "so please don't worry.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#12210FAlright, si Rixia, you promised.\x02\x03",
            "And painful things are done to liars, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10715FYeah... I got it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 500)

    ChrTalk(
        0x101,
        "#11P#00002FRixia... \x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x106,
        (
            "#6P#10715F...Mr. Lloyd.\x01",
            "We should be going.\x02\x03",
            "#10716FEveryone has practice to\x01",
            "attend to... And we should\x01",
            "hurry towards our objective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah... You're right.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, 13940, 0)
    SetScenarioFlags(0x1CF, 5)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    OP_4C(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C951")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xD, 3520, 1250, 22730, 90)
    SetChrPos(0xE, 4800, 1250, 22730, 270)
    SetChrPos(0xA, 0, 1250, 27230, 0)
    SetChrChipByIndex(0xA, 0x14)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrChipByIndex(0xD, 0xB)
    SetChrChipByIndex(0xE, 0xC)
    SetChrChipByIndex(0x10, 0xF)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_C9E4")

    label("loc_C951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C9E4")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xB, 0, 0, 15300, 0)
    SetChrPos(0xD, 0, 1250, 27300, 180)
    SetChrPos(0xF, -1390, 1250, 26170, 90)
    SetChrPos(0x11, 1390, 1250, 26170, 270)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)

    label("loc_C9E4")

    Sleep(1000)
    EventEnd(0x5)
    SetScenarioFlags(0x22, 2)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_34_B512 end

    def Function_35_C9F6(): pass

    label("Function_35_C9F6")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_68(-40, 3900, 28500, 0)
    MoveCamera(0, 2, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20350, 0)
    SetChrPos(0x101, -750, 1250, 25380, 0)
    SetChrPos(0x102, 690, 1250, 25060, 0)
    SetChrPos(0x103, -1940, 1250, 24700, 45)
    SetChrPos(0x104, 1760, 1250, 24400, 315)
    SetChrPos(0xF4, -1200, 1250, 23190, 0)
    SetChrPos(0xF5, 1000, 1250, 23100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_93(0xA, 0x0, 0x0)
    OP_68(-40, 3200, 28500, 3000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xA,
        "#12P#14003F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FWhat's wrong, Sully?\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(510, 2700, 24450, 0)
    MoveCamera(331, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16329, 0)
    Sleep(100)
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#11P#14000FY-Yeah... \x01",
            "It's just a little prayer.\x02\x03",
            "#14003FFor now, this is an altar.\x01",
            "...In the set, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302FHa ha, I see. But you don't\x01",
            "seem like the prayin' type.\x02\x03",
            "#00305FSo, what could you be prayin' for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FHey Randy! \x01",
            "Don't ask so directly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#14000FWell it's fine, right?\x02\x03",
            "#14003FOf course it's for Miss Ilya...\x02\x03",
            "But it's for all of you as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00205FUs, you said?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#14003F............\x02\x03",
            "#14001F...I don't know the details, \x01",
            "but you guys are going \x01",
            "after KeA, right?\x02\x03",
            "And, you guys are going somewhere\x01",
            "dangerous right now.\x02\x03",
            "#14003F............\x02\x03",
            "#14002FThat's why I pray for your\x01",
            "safety. For sis Rixia's too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CE7C")

    ChrTalk(
        0x106,
        (
            "#6P#10702FSully...\x01",
            "Uh uh, thanks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF11")

    label("loc_CE7C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CEBC")

    ChrTalk(
        0x109,
        (
            "#6P#10102FI see... \x01",
            "Thank you, Sully.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF11")

    label("loc_CEBC")


    ChrTalk(
        0x105,
        (
            "#6P#10302FHu hu, I see...\x01",
            "You're saying something nice\x01",
            "again to us, aren't you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF11")


    ChrTalk(
        0x101,
        (
            "#6P#00002FYeah, thank you for\x01",
            "thinking of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#14012FA-Anyway... KeA is a precious\x01",
            "friend to me, you see.\x02\x03",
            "#14001FDefinitely bring her back, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYeah, of course!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6F), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D390")

    ChrTalk(
        0xA,
        (
            "#11P#14000FOh yeah... There's\x01",
            "something I want you\x01",
            "guys to take with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FWith us... What\x01",
            "ever could it be?\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0xA, 0x0, 0x1F4, 0x5DC, 0x0)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Sully took off her cap and handed it to Lloyd.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x39D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x39D, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1DE, 1)
    OP_9B(0x1, 0xA, 0xB4, 0x1F4, 0x5DC, 0x0)

    ChrTalk(
        0x101,
        "#6P#00005FThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#04203FSince you guys are going\x01",
            "after KeA, I really want\x01",
            "to go with you, but...\x02\x03",
            "#04208FI know I can't do\x01",
            "such a thing.\x02\x03",
            "So instead, take my\x01",
            "favorite hat with you.\x02\x03",
            "#04201F...That's ok, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FSure, it's fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102FWe understand your\x01",
            "feelings, Sully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FYes. We will take\x01",
            "responsibility for it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D320")

    ChrTalk(
        0xA,
        (
            "#11P#04212FI-I see... \x01",
            "Well, good then.\x02\x03",
            "#04202FPlease be careful, \x01",
            "sis Rixia and\x01",
            "everyone too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#6P#10709FYes, understood.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_D390")

    label("loc_D320")


    ChrTalk(
        0xA,
        (
            "#11P#04212FI-I see... \x01",
            "Well, good then.\x02\x03",
            "#04202FSo, be very\x01",
            "careful, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYeah, understood.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_D390")

    SetScenarioFlags(0x1DE, 0)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x10)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 1250, 24400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D3EB")
    OP_E0(0x34, 0x0)

    label("loc_D3EB")

    EventEnd(0x5)
    Return()

    # Function_35_C9F6 end

    def Function_36_D3EE(): pass

    label("Function_36_D3EE")

    EventBegin(0x0)
    Fade(500)
    OP_68(65370, 1500, 2140, 0)
    MoveCamera(37, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15840, 0)
    SetChrPos(0xF, 67000, 0, 3000, 270)
    SetChrPos(0x101, 65670, 0, 3760, 90)
    SetChrPos(0x102, 65700, 0, 2440, 90)
    SetChrPos(0x104, 64000, 0, 3200, 90)
    SetChrPos(0x109, 64590, 0, 1760, 90)
    SetChrPos(0x105, 64610, 0, 4350, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xF, 0xFF)
    OP_0D()

    ChrTalk(
        0xF,
        "Oh, you guys are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FHello, Mr. Nikol.\x02\x03",
            "We'd like to ask you a little something.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained the professor's request and that\x01",
            "they were here to collect the medical questionnaire.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        "Oh, that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I've been having so much fun\x01",
            "practicing lately that I\x01",
            "totally forgot to return it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Hang on a second.\x01",
            "I'll go grab it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xF,
        "Here. Is this it?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x32D, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#6P#00000FYes, it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102F*giggle*, if you you're doing this well,\x01",
            "then it looks like you're no longer\x01",
            "under the influence of that drug.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Yeah, I received\x01",
            "proper treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I wonder why I even started\x01",
            "taking a drug like that in\x01",
            "the first place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Though I did want to\x01",
            "do something about\x01",
            "my lack of ability...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FThe drug slid right\x01",
            "into that gap in\x01",
            "your heart, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FWell, as long as you're aware of it,\x01",
            "we've got nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Right... I plan to\x01",
            "dedicate myself to Arc-\x01",
            "en-ciel more than ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FI'm looking forward to seeing the play.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x152, 4)
    OP_29(0x70, 0x1, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D9A8")

    AnonymousTalk(
        0x101,
        (
            "#00000FNow we have finished to collect\x01",
            "all the medical questionnaires.\x02\x03",
            "Let's go deliver them to\x01",
            "Professor Seiland at once.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x70, 0x1, 0x5)

    label("loc_D9A8")

    OP_93(0xF, 0x5A, 0x0)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 65000, 0, 3000, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_36_D3EE end

    def Function_37_D9DA(): pass

    label("Function_37_D9DA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch39000.itc", 0x1E)
    LoadChrToIndex("chr/ch00100.itc", 0x1F)
    LoadChrToIndex("chr/ch03000.itc", 0x20)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 1850, 15200, -8150, 270)
    OP_68(10290, 16450, -8390, 0)
    MoveCamera(48, 12, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16590, 0)
    SetChrPos(0x101, 13010, 15200, -8000, 270)
    SetChrPos(0x1A3, 13010, 15200, -8000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 38)
    Sleep(700)
    BeginChrThread(0x1A3, 3, 0, 39)
    WaitChrThread(0x1A3, 3)
    OP_0D()

    ChrTalk(
        0x101,
        "#11P#00000FWell then, I wonder if Mary's here...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#00005FAh!\x02",
    )

    CloseMessageWindow()
    OP_68(2530, 16850, -8580, 3000)
    MoveCamera(48, 12, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15720, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x1A3,
        "#11P#04600FUh uh, found her right away.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A3, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00000FAlright, leave\x01",
            "this to me.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A3, 0x101, 500)

    ChrTalk(
        0x1A3,
        (
            "#11P#04605FAww. Fine, whatever.\x02\x03",
            "#04602FShow me what you've got.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DBE4():
        OP_95(0xFE, 8590, 15200, -7600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DBE4)
    Sleep(50)

    def lambda_DC01():
        TurnDirection(0xFE, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_DC01)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#00002FC'mon Mary.\x01",
            "It's ok, come here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x101, 500)
    OP_63(0x13, 0x0, 1200, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x13)
    OP_63(0x13, 0x0, 1200, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x13)
    OP_68(5850, 16850, -7440, 3000)
    OP_9B(0x0, 0x13, 0x0, 0x7D0, 0x3E8, 0x0)
    OP_6F(0x1)
    Sleep(500)
    Fade(500)
    OP_68(-8010, 16850, -9130, 0)
    MoveCamera(326, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15880, 0)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    Sound(103, 0, 100, 0)
    SetChrPos(0x14, -13030, 15200, -8029, 90)
    SetChrPos(0x15, -13030, 15200, -8029, 90)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x14, 3, 0, 40)
    Sleep(700)
    BeginChrThread(0x15, 3, 0, 41)
    WaitChrThread(0x15, 3)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FAh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(5850, 16850, -7440, 0)
    MoveCamera(48, 12, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_0D()
    OP_63(0x13, 0x0, 1200, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(10750, 16850, -7200, 1500)
    Sound(953, 0, 100, 0)

    def lambda_DDC0():
        OP_95(0xFE, 13800, 15200, -8010, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_DDC0)
    Sleep(1000)

    def lambda_DDDD():
        TurnDirection(0xFE, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DDDD)
    Sleep(50)

    def lambda_DDED():

        label("loc_DDED")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_DDED")

    QueueWorkItem2(0x1A3, 1, lambda_DDED)
    Sleep(1000)

    def lambda_DE02():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_DE02)
    WaitChrThread(0x13, 1)
    SetChrFlags(0x13, 0x80)
    OP_6F(0x1)
    EndChrThread(0x1A3, 0x1)

    ChrTalk(
        0x1A3,
        "#04605FWhoa...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FI-I was careless...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04609FAhaha, Shirley was too.\x02\x03",
            "#04606FHmm, could it be\x01",
            "I still lack in training?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x14, 1770, 15200, -7960, 90)
    SetChrPos(0x15, 1770, 15200, -9370, 90)
    OP_68(6830, 16850, -8570, 4000)
    MoveCamera(46, 28, 0, 4000)
    OP_6E(500, 4000)
    SetCameraDistance(16250, 4000)

    def lambda_DEFF():
        OP_95(0xFE, 6590, 15200, -7960, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_DEFF)
    Sleep(50)

    def lambda_DF1C():
        OP_95(0xFE, 6590, 15200, -9370, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_DF1C)
    WaitChrThread(0x15, 1)
    OP_6F(0x79)

    ChrTalk(
        0x15,
        (
            "#6P#10300FHey. It seems we're\x01",
            "interrupting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#6P#00106FSorry. That looked like\x01",
            "a really good chance.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DFAA():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DFAA)
    Sleep(50)

    def lambda_DFBA():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_DFBA)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00004FNo, it's only because I didn't follow through.\x02\x03",
            "#00000FAnyway, let's go after her.\x02\x03",
            "Just in case, you guys head\x01",
            "for the opposite entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#6P#00100FAlright, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04609FUh uh. Alright\x01",
            "then, after her!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x155, 6)
    OP_29(0x74, 0x1, 0x7)
    ModifyEventFlags(1, 2, 0x80)
    OP_1B(0x2, 0x0, 0x2A)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 9130, 15200, -8100, 0)
    EventEnd(0x5)
    Return()

    # Function_37_D9DA end

    def Function_38_E0F3(): pass

    label("Function_38_E0F3")


    def lambda_E0F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E0F8)

    def lambda_E109():
        OP_95(0xFE, 11590, 15200, -7990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E109)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 10260, 15200, -7100, 2000, 0x0)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_38_E0F3 end

    def Function_39_E13E(): pass

    label("Function_39_E13E")


    def lambda_E143():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_E143)

    def lambda_E154():
        OP_95(0xFE, 11590, 15200, -7990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_E154)
    WaitChrThread(0x1A3, 1)
    OP_95(0x1A3, 10260, 15200, -9100, 2000, 0x0)
    OP_93(0x1A3, 0x10E, 0x1F4)
    Return()

    # Function_39_E13E end

    def Function_40_E189(): pass

    label("Function_40_E189")


    def lambda_E18E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_E18E)

    def lambda_E19F():
        OP_95(0xFE, -8770, 15200, -8150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_E19F)
    WaitChrThread(0x14, 1)
    OP_93(0x14, 0x5A, 0x1F4)
    Return()

    # Function_40_E189 end

    def Function_41_E1C0(): pass

    label("Function_41_E1C0")


    def lambda_E1C5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_E1C5)

    def lambda_E1D6():
        OP_95(0xFE, -11190, 15200, -8100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_E1D6)
    WaitChrThread(0x15, 1)
    OP_95(0x15, -10100, 15200, -9070, 2000, 0x0)
    OP_93(0x15, 0x5A, 0x1F4)
    Return()

    # Function_41_E1C0 end

    def Function_42_E20B(): pass

    label("Function_42_E20B")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's hurry and chase Mary.\x01",
            "She should still be close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04609FUh uh, we're not going to\x01",
            "let her get away this time!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -11130, 15200, -7980, 90)
    EventEnd(0x4)
    Return()

    # Function_42_E20B end

    def Function_43_E2A6(): pass

    label("Function_43_E2A6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch39000.itc", 0x1E)
    LoadChrToIndex("apl/ch50267.itc", 0x1F)
    LoadChrToIndex("apl/ch51226.itc", 0x20)
    LoadChrToIndex("apl/ch51228.itc", 0x21)
    LoadChrToIndex("apl/ch51229.itc", 0x22)
    LoadChrToIndex("chr/ch03401.itc", 0x23)
    SoundLoad(148)
    SetMapObjFrame(0xFF, "chandelier01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "chandelier02", 0x0, 0x1)
    OP_4C(0x9, 0x1)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x8000)
    OP_52(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x13, -1900, 0, -1900, 0)
    OP_78(0x19, 0x16)
    ClearMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x19, 0x1000)
    OP_74(0x19, 0x1E)
    ClearChrFlags(0x16, 0x80)
    OP_49()
    SetChrPos(0x16, 0, 1250, 25580, 0)
    OP_D5(0x16, 0x0, 0x0, 0x0, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0xE)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x4)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, 0, 0, 900, 180)
    OP_68(-2680, 4650, 17690, 0)
    MoveCamera(50, 37, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(9930, 0)
    SetChrPos(0x13, 350, 1250, 18040, 0)
    SetChrPos(0x9, -140, 2700, -5190, 0)
    SetChrPos(0x1A3, -140, 2700, -5190, 0)
    SetChrPos(0x101, -140, 2700, -5190, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x104, 0x80)
    SetCameraDistance(12670, 3000)

    def lambda_E46C():
        OP_95(0xFE, 110, 1250, 20620, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_E46C)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x13, 1)
    OP_6F(0x10)
    Fade(500)
    OP_68(-2450, 4650, -2450, 0)
    MoveCamera(49, 31, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    OP_68(-2880, 4650, 4170, 5000)
    MoveCamera(55, 31, 0, 5000)
    BeginChrThread(0x9, 3, 0, 46)
    Sleep(700)
    BeginChrThread(0x1A3, 3, 0, 45)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 44)
    WaitChrThread(0x101, 3)
    OP_6F(0x79)
    Sleep(700)
    Fade(500)
    OP_68(-1760, 4650, 21430, 0)
    MoveCamera(50, 37, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    Sound(844, 0, 50, 0)
    OP_9D(0x13, 0x15E, 0xDAC, 0x5AA0, 0xDAC, 0x1388)
    OP_D3(0x13, 0x19, "nullch")
    ClearChrFlags(0x13, 0x1)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Sound(143, 0, 70, 0)
    Sound(148, 2, 100, 0)

    def lambda_E582():
        OP_98(0xFE, 0x0, 0x2710, 0x0, 0x96, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_E582)
    Sleep(3000)
    Fade(500)
    OP_68(-3750, 4650, 3390, 0)
    MoveCamera(33, 16, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#10AWha...!?\x02",
    )

    Sleep(1500)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#06205F#10AThis is bad! Not the props!\x02\x03",
            "#10ABut, just who...!?\x02",
        )
    )

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    OP_68(-1560, 4350, 2450, 2000)
    MoveCamera(30, 20, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(11000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x1A3,
        "#11P#04611F#10AUh uh! This is nothing!\x02",
    )

    Sleep(1000)
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x1A3, 0x23)
    SetChrSubChip(0x1A3, 0x5)
    SetChrFlags(0x1A3, 0x1000)
    OP_6B(0x1A3)
    SetChrChip(0x0, 0x1A3, 0x1E, 0x12C)
    Sound(250, 0, 60, 0)
    OP_95(0x1A3, -910, 1350, 7510, 10000, 0x0)
    OP_95(0x1A3, 100, 0, 15520, 10000, 0x0)
    Sound(844, 0, 100, 0)
    OP_9D(0x1A3, 0x1CC, 0x4E2, 0x49A2, 0x9C4, 0x2710)
    OP_95(0x1A3, 4610, 1250, 21370, 10000, 0x0)
    Sound(251, 0, 50, 0)
    OP_9D(0x1A3, 0x1E28, 0x9C4, 0x5910, 0x9C4, 0x2710)
    OP_93(0x1A3, 0x10E, 0x0)
    OP_9D(0x1A3, 0x0, 0xED8, 0x5A32, 0xFA0, 0x1388)
    Sound(326, 0, 50, 0)
    OP_93(0x1A3, 0x10E, 0x0)
    SetChrChip(0x1, 0x1A3, 0x0, 0x0)
    OP_D3(0x1A3, 0x19, "nullch2")
    ClearChrFlags(0x1A3, 0x1)
    OP_52(0x1A3, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6B(0xFF)
    OP_6B(0x13)
    SetChrChipByIndex(0x1A3, 0xFF)
    SetChrSubChip(0x1A3, 0x0)
    Sound(879, 0, 70, 0)
    OP_74(0x19, 0x14)
    OP_71(0x19, 0x2B, 0x42, 0x0, 0x0)
    Sleep(1100)
    Sound(879, 0, 60, 0)
    OP_74(0x19, 0xA)
    OP_71(0x19, 0x2B, 0x3A, 0x0, 0x0)
    Sleep(1500)
    Sound(879, 0, 50, 0)
    OP_74(0x19, 0x7)
    OP_71(0x19, 0x3A, 0x32, 0x0, 0x0)
    OP_79(0x19)
    OP_74(0x19, 0x5)
    OP_71(0x19, 0x32, 0x39, 0x0, 0x0)
    OP_79(0x19)
    Sound(879, 0, 40, 0)
    OP_74(0x19, 0x2)
    OP_71(0x19, 0x39, 0x36, 0x0, 0x0)
    OP_79(0x19)
    TurnDirection(0x13, 0x1A3, 500)
    OP_6B(0xFF)
    OP_68(-400, 8390, 22760, 2000)
    MoveCamera(33, 16, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(11550, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    EndChrThread(0x16, 0x1)
    Fade(500)
    OP_68(-360, 1320, 15690, 0)
    MoveCamera(39, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13720, 0)
    SetChrPos(0x101, 900, 0, 15820, 0)
    SetChrPos(0x9, -900, 0, 15820, 0)
    OP_D3(0x1A3, 0x19, "nullch")
    ClearChrFlags(0x1A3, 0x1)
    OP_52(0x1A3, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x19, 0xB, 0xB, 0x0, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#00005FHuh...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#06205FA-Amazing...!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-790, 8810, 23640, 0)
    MoveCamera(3, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(12000, 0)
    SetChrFlags(0x13, 0x8)
    SetChrChipByIndex(0x1A3, 0x20)
    SetChrSubChip(0x1A3, 0x7)
    SetChrFlags(0x1A3, 0x2)
    SetChrPos(0x1A3, 250, 1250, 22960, 270)
    OP_0D()
    OP_6B(0x1A3)

    def lambda_E98A():
        OP_98(0xFE, 0x0, 0x1770, 0x0, 0x96, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_E98A)

    ChrTalk(
        0x13,
        "#6PN-Nya～n...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#11P#04606FHmm? It's not like\x01",
            "I'm gonna eat you.\x02\x03",
            "Settle down already.\x02\x03",
            "#04602FHere, how do you like this♪\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Shirley tickled\x01",
            "Mary's throat.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x1A3, 0x0, 1200, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A3)
    OP_63(0x1A3, 0x0, 1200, 0x8, 0x9, 0xFA, 0x1)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    Sound(953, 0, 100, 0)

    ChrTalk(
        0x13,
        "#6PN-Nya～n. \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#11P#04609FUh uh, not too bad, eh?\x02\x03",
            "#04600FAlright... Then how about this㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A3, 0x0, 1200, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x13,
        "#6PNyaun!\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A3, 0x0, 1200, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A3)
    OP_63(0x1A3, 0x0, 1200, 0xA, 0xB, 0xFA, 0x1)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x13,
        "#6P*purr, purr, purr*... unyan㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        "#11P#04609FAhaha, have you calmed down a bit?\x02",
    )

    CloseMessageWindow()
    OP_6B(0xFF)
    StopSound(148, 1000, 100)
    Fade(500)
    OP_68(-390, 1320, 17820, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13620, 0)
    SetChrPos(0x101, 900, 0, 15820, 0)
    SetChrPos(0x9, -900, 0, 15820, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#00000FHa ha, she's very good at that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#06204FYes. And she's so agile,\x01",
            "I can hardly believe it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#12P#06205FRight, I need to see who was\x01",
            "operating the equipment...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EndChrThread(0x16, 0x1)
    Fade(500)
    OP_68(290, 11070, 33130, 0)
    MoveCamera(7, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(26000, 0)
    SetChrPos(0x16, 0, 11250, 25580, 0)
    OP_D5(0x16, 0x0, 0x0, 0x0, 0x0)
    OP_0D()

    ChrTalk(
        0x1A3,
        (
            "#11P#04600FAlright then, let's\x01",
            "get down together.\x02\x03",
            "No more funny business, you hear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#6PNya～n♪\x02",
    )

    CloseMessageWindow()
    OP_68(290, 9970, 33130, 100)
    Sound(143, 0, 100, 0)
    OP_98(0x16, 0x0, 0xFFFFFA24, 0x0, 0x1F40, 0x0)
    OP_63(0x1A3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A3,
        "#11P#04605FWhat's this all of a sudden... Ah.\x02",
    )

    CloseMessageWindow()
    OP_68(3620, 6670, 29700, 500)
    MoveCamera(25, 17, 0, 500)
    OP_6E(500, 500)
    SetCameraDistance(28350, 500)
    Sound(879, 0, 100, 0)
    OP_74(0x19, 0x1E)
    OP_71(0x19, 0xB, 0x28, 0x0, 0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_98(0x16, 0x0, 0xFFFFF448, 0x0, 0x2710, 0x0)
    SetChrPos(0x13, 520, 8840, 23300, 90)
    SetChrChipByIndex(0x1A3, 0xFF)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x1A3, 0x5)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x8)
    SetChrFlags(0x1A3, 0x2)
    SetChrFlags(0x13, 0x2)
    Sound(809, 0, 100, 0)

    def lambda_EEB5():
        OP_9D(0xFE, 0x212, 0x2328, 0x4268, 0x7D0, 0x64)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_EEB5)
    OP_D3(0x13, 0xFF, "nullch")
    OP_93(0x1A3, 0xB4, 0x0)
    CancelBlur(500)
    Sleep(500)
    EndChrThread(0x13, 0x1)
    Fade(500)
    OP_68(-710, 1320, 19230, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 900, 0, 15820, 0)
    SetChrPos(0x9, -900, 0, 15820, 0)
    SetChrPos(0x13, 530, 10000, 22500, 90)
    OP_71(0x19, 0x28, 0x28, 0x0, 0x0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011FThis is bad...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#06201F...!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 47)
    Sleep(500)
    OP_68(3370, 4570, 23550, 800)
    MoveCamera(48, 23, 0, 800)
    OP_6E(500, 800)
    SetCameraDistance(20670, 800)
    Sound(834, 0, 50, 0)

    def lambda_F003():
        OP_9D(0xFE, 0x6D6, 0x1F40, 0x4A38, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_F003)
    Sleep(700)
    EndChrThread(0x13, 0x1)
    SetChrFlags(0x13, 0x8)
    OP_6F(0x79)
    WaitChrThread(0x9, 3)
    ClearScenarioFlags(0x1, 4)
    EndChrThread(0x9, 0x0)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x7)
    OP_0D()
    OP_68(4110, 4870, 24080, 1000)
    MoveCamera(48, 23, 0, 1000)
    OP_6E(500, 1000)
    SetCameraDistance(29060, 1000)
    SetCameraDistance(29060, 1000)
    TurnDirection(0x1A3, 0x101, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x1A3,
        "#04605FWhoa, nice catch!\x02",
    )

    CloseMessageWindow()
    OP_68(-2520, 5470, 16640, 5000)
    MoveCamera(48, 23, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(9920, 5000)
    SetChrPos(0x101, -4480, 1250, 20070, 90)
    OP_95(0x101, 1230, 1250, 20900, 2000, 0x0)
    TurnDirection(0x101, 0x9, 500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00000F*phew*... Looks like\x01",
            "you got her somehow.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("c0410", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_43_E2A6 end

    def Function_44_F155(): pass

    label("Function_44_F155")


    def lambda_F15A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F15A)

    def lambda_F16B():
        OP_95(0xFE, 0, 2250, 2940, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F16B)
    WaitChrThread(0x101, 1)
    Return()

    # Function_44_F155 end

    def Function_45_F185(): pass

    label("Function_45_F185")


    def lambda_F18A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_F18A)

    def lambda_F19B():
        OP_95(0xFE, 0, 1800, 5200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_F19B)
    WaitChrThread(0x1A3, 1)
    Return()

    # Function_45_F185 end

    def Function_46_F1B5(): pass

    label("Function_46_F1B5")


    def lambda_F1BA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_F1BA)

    def lambda_F1CB():
        OP_95(0xFE, 0, 1350, 7460, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F1CB)
    WaitChrThread(0x9, 1)
    Return()

    # Function_46_F1B5 end

    def Function_47_F1E5(): pass

    label("Function_47_F1E5")

    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x1)
    Sound(250, 0, 60, 0)
    OP_9D(0x9, 0x0, 0x4E2, 0x4BFA, 0xBB8, 0x1388)
    SetChrSubChip(0x9, 0x0)
    SetScenarioFlags(0x1, 4)
    Sound(637, 0, 100, 0)
    Sound(844, 0, 100, 0)
    BeginChrThread(0x9, 0, 0, 48)

    def lambda_F228():
        OP_9D(0xFE, 0x1086, 0x4E2, 0x517C, 0x1388, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F228)
    OP_A1(0x9, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0x9, 1)
    Sound(326, 0, 50, 0)
    Return()

    # Function_47_F1E5 end

    def Function_48_F254(): pass

    label("Function_48_F254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_F270")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_48_F254")

    label("loc_F270")

    Return()

    # Function_48_F254 end

    def Function_49_F271(): pass

    label("Function_49_F271")

    SetChrPos(0xA, 0, 1250, 25500, 270)

    label("loc_F282")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F656")
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    SetChrFlags(0xA, 0x1020)
    BeginChrThread(0xA, 1, 0, 51)

    def lambda_F2B3():
        OP_93(0xA, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F2B3)
    Sound(809, 0, 30, 0)
    OP_9D(0xA, 0x0, 0x4E2, 0x59D8, 0xBB8, 0x44C)
    Sound(50, 0, 70, 0)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    Sleep(200)

    def lambda_F2EE():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0xA96, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F2EE)
    OP_49()
    Sound(809, 0, 30, 0)
    BeginChrThread(0xA, 1, 0, 51)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x4E2)
    Sound(50, 0, 70, 0)
    Sound(809, 0, 30, 0)
    BeginChrThread(0xA, 1, 0, 51)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x4E2)
    Sound(50, 0, 70, 0)
    EndChrThread(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    Sleep(300)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x38)

    def lambda_F374():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1068, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F374)
    Sleep(250)

    def lambda_F392():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1450, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F392)
    Sleep(250)

    def lambda_F3B0():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1838, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F3B0)
    Sleep(250)

    def lambda_F3CE():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F3CE)
    OP_49()
    SetChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x3B)
    SetChrSubChip(0xA, 0x2)
    BeginChrThread(0xA, 1, 0, 54)
    Sleep(1000)

    def lambda_F400():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1C20, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F400)
    OP_49()
    Sound(844, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    Sound(50, 0, 50, 0)
    EndChrThread(0xA, 0x2)
    Sound(809, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x578)
    Sound(50, 0, 50, 0)

    def lambda_F466():
        OP_9E(0xA, 0x0, 0x636A, 0xFFF24460, 0x2A94, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F466)
    OP_49()
    Sound(844, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x514)
    Sound(50, 0, 50, 0)

    def lambda_F4A5():
        OP_93(0xA, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F4A5)
    BeginChrThread(0xA, 1, 0, 51)
    Sound(809, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x578)
    Sound(50, 0, 50, 0)
    BeginChrThread(0xA, 1, 0, 51)

    def lambda_F4E1():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1838, 0x2)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F4E1)
    OP_49()
    Sound(844, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0xAF)
    Sound(50, 0, 50, 0)
    EndChrThread(0xA, 0x2)
    OP_93(0xA, 0x10E, 0x0)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    Sleep(1000)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x37)
    OP_96(0xA, 0xBB8, 0x4E2, 0x61A8, 0x7D0, 0x0)
    Sleep(700)
    SetChrChipByIndex(0xA, 0x38)
    OP_96(0xA, 0x7D0, 0x4E2, 0x61A8, 0x1194, 0x0)
    BeginChrThread(0xA, 1, 0, 50)
    Sound(809, 0, 20, 0)
    OP_9D(0xA, 0x3E8, 0x4E2, 0x61A8, 0x3E8, 0xBB8)
    Sound(50, 0, 30, 0)
    SetChrChipByIndex(0xA, 0x3B)
    SetChrSubChip(0xA, 0x2)
    BeginChrThread(0xA, 1, 0, 55)
    Sound(809, 0, 20, 0)
    OP_9D(0xA, 0x0, 0x4E2, 0x61A8, 0x5DC, 0xBB8)
    Sound(50, 0, 30, 0)
    BeginChrThread(0xA, 1, 0, 54)
    Sound(809, 0, 20, 0)
    OP_9D(0xA, 0xFFFFF92A, 0x4E2, 0x61A8, 0x7D0, 0xBB8)
    Sound(50, 0, 30, 0)
    BeginChrThread(0xA, 1, 0, 51)

    def lambda_F5F7():
        OP_93(0xA, 0x5A, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F5F7)
    Sound(809, 0, 20, 0)
    OP_9D(0xA, 0xFFFFF060, 0x4E2, 0x61A8, 0xBB8, 0x578)
    Sound(50, 0, 30, 0)
    OP_93(0xA, 0x87, 0x0)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    Sleep(1000)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x37)
    OP_96(0xA, 0x0, 0x4E2, 0x61A8, 0x7D0, 0x0)
    Jump("loc_F282")

    label("loc_F656")

    Return()

    # Function_49_F271 end

    def Function_50_F657(): pass

    label("Function_50_F657")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_50_F657 end

    def Function_51_F67B(): pass

    label("Function_51_F67B")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0x7D0, 0x3, 0x0, 0x1, 0x2)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_51_F67B end

    def Function_52_F69F(): pass

    label("Function_52_F69F")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0x9C4, 0x2, 0x0, 0x1)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_52_F69F end

    def Function_53_F6B4(): pass

    label("Function_53_F6B4")

    SetChrChipByIndex(0xFE, 0x3B)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_53_F6B4 end

    def Function_54_F6C2(): pass

    label("Function_54_F6C2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F6E0")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    Jump("Function_54_F6C2")

    label("loc_F6E0")

    Return()

    # Function_54_F6C2 end

    def Function_55_F6E1(): pass

    label("Function_55_F6E1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F6FF")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(60)
    Jump("Function_55_F6E1")

    label("loc_F6FF")

    Return()

    # Function_55_F6E1 end

    def Function_56_F700(): pass

    label("Function_56_F700")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 2500, 25500, 0)
    MoveCamera(32, 5, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(24000, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 1250, 25500, 180)
    SetChrPos(0x101, 0, 2700, 500, 0)
    SetChrPos(0x102, 1200, 2700, 500, 0)
    SetChrPos(0x103, -1200, 2700, 500, 0)
    SetChrPos(0x104, 0, 2700, -700, 0)
    SetChrPos(0x105, 1200, 2700, -700, 0)
    SetChrPos(0x109, -1200, 2700, -700, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    LoadChrToIndex("chr/ch14150.itc", 0x37)
    LoadChrToIndex("chr/ch14151.itc", 0x38)
    LoadChrToIndex("chr/ch14152.itc", 0x39)
    LoadChrToIndex("chr/ch14153.itc", 0x3A)
    LoadChrToIndex("chr/ch14154.itc", 0x3B)
    SetChrChipByIndex(0xA, 0x37)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 2500, 1250, 25450, 0)
    BeginChrThread(0x0, 0, 0, 49)
    FadeToBright(1000, 0)
    OP_68(0, 4000, 25500, 10000)
    MoveCamera(14, 10, 0, 710000)
    Sleep(7000)
    Fade(500)
    OP_68(-1400, 4130, 3070, 0)
    MoveCamera(30, 14, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FLooks like she's\x01",
            "really going at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes. It's just as the manager said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FHow should I say it...\x01",
            "Looking at her like this is overwhelming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FSo that's that new scene\x01",
            "she's practicin', huh.\x02\x03",
            "#00304FThey said it was a pretty\x01",
            "important role, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FThe "Star Princess", right?\x02\x03",
            "I heard she has a big\x01",
            "scene in the second half.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, looks like she's ready for it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, but the pressure\x01",
            "must be incredible...\x02\x03",
            "#00000FLet's excuse ourselves\x01",
            "before we get in her way.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xA, 0x3)
    EndChrThread(0x0, 0x0)
    SetChrChipByIndex(0xA, 0x10)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -1500, 1250, 25450, 90)
    OP_68(-1500, 2500, 25500, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    OP_93(0xA, 0xB4, 0x258)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#12205FAh... You guys!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-1400, 4130, 3070, 0)
    MoveCamera(30, 14, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FWhoops...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FLooks like we were noticed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, since we're here,\x01",
            "let's at least say hello.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FC03():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FC03)
    Sleep(50)

    def lambda_FC20():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FC20)
    Sleep(50)

    def lambda_FC3D():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FC3D)
    Sleep(50)

    def lambda_FC5A():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FC5A)
    Sleep(50)

    def lambda_FC77():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FC77)
    Sleep(50)

    def lambda_FC94():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_FC94)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-50, 1320, 14180, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13000, 0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrPos(0x101, 0, 0, 14050, 0)
    SetChrPos(0x102, 1000, 0, 14150, 0)
    SetChrPos(0x103, -1000, 0, 14150, 0)
    SetChrPos(0x104, 0, 450, 12100, 0)
    SetChrPos(0x105, 1000, 450, 12000, 0)
    SetChrPos(0x109, -1000, 450, 12100, 0)
    SetChrPos(0xA, -1500, 1250, 22000, 180)
    FadeToBright(1000, 0)
    ClearChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x38)
    OP_96(0xA, 0x0, 0x4E2, 0x4696, 0x1388, 0x0)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    Sleep(200)
    Sound(809, 0, 50, 0)
    SetChrFlags(0xA, 0x1020)
    BeginChrThread(0xA, 1, 0, 50)
    OP_9D(0xA, 0xFFFFFFCE, 0x0, 0x3E6C, 0x3E8, 0x7D0)
    Sound(42, 0, 100, 0)
    Sound(326, 0, 20, 0)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    Sleep(200)
    Fade(500)
    SetChrChipByIndex(0xA, 0x10)
    SetChrSubChip(0xA, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FHey, Sully.\x01",
            "Sorry to interrupt your training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12203FH-Hmph, whatever...\x02\x03",
            "#12200FSo, did you need something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FNo. We were passing by and just\x01",
            "want to see what you all were up to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah. Sorry for interrupting you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12206FWell, I was thinking of\x01",
            "taking a break anyway.\x01",
            "It's fine, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FBut, this is the first time\x01",
            "I have seen you perform...\x02\x03",
            "#00202FYou have already mastered it. \x01",
            "No one would think you are a beginner.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#12205FR-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FYes, really. \x01",
            "I'm honestly surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah. It's like you're not\x01",
            "wasting a single movement.\x02\x03",
            "#00002FYou must be pretty close\x01",
            "to perfecting it, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12205FHuh...\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    ChrTalk(
        0x109,
        (
            "#10109FYeah, yeah. And that costume\x01",
            "looks really good on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105F...Sully?\x02",
    )

    CloseMessageWindow()
    OP_64(0xA)

    def lambda_10142():

        label("loc_10142")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_10142")

    QueueWorkItem2(0x102, 0, lambda_10142)

    def lambda_10154():

        label("loc_10154")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_10154")

    QueueWorkItem2(0x103, 0, lambda_10154)
    OP_99(0xA, 0x101, 0x3E8, 0x7D0, 0x0)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)

    ChrTalk(
        0xA,
        (
            "#12203F...Hey, you.\x02\x03",
            "#12200FWant to join me for\x01",
            "performance training?\x02\x03",
            "#12208FHow to say this... There's\x01",
            "something I want your opinion on.\x02",
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
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FYou want Lloyd to\x01",
            "join your training?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FW-Why me? And my\x01",
            "opinion about what...?\x02\x03",
            "#00003FI'm just a layman. \x01",
            "I don't know anything about\x01",
            "the performing arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12203FI'm telling you, I won't have you\x01",
            "do anything difficult, you know.\x02\x03",
            "#12208FAlso, I had just\x01",
            "something on my mind.\x02\x03",
            "#12200F...So how about it?\x01",
            "Are you joining me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FW-Well...\x02",
    )

    CloseMessageWindow()
    Call(0, 57)
    Return()

    # Function_56_F700 end

    def Function_57_10424(): pass

    label("Function_57_10424")

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
            "Join Sully's Training\x01",      # 0
            "Quit\x01",                       # 1
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
        (0, "loc_1048F"),
        (1, "loc_10573"),
        (SWITCH_DEFAULT, "loc_106F8"),
    )


    label("loc_1048F")


    ChrTalk(
        0x101,
        (
            "#00000FSure, if you're okay with me, that is.\x02\x03",
            "Are you sure it's no big deal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12200FYeah... Got it.\x02",
    )

    CloseMessageWindow()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Secret Acting Coach]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x8D, 0x4, 0x2)
    SetScenarioFlags(0x22, 1)
    NewScene("e3600", 0, 0, 0)
    IdleLoop()
    Jump("loc_106F8")

    label("loc_10573")


    ChrTalk(
        0x101,
        (
            "#00006F...Sorry. We have other\x01",
            "things to do now and\x01",
            "can't spare the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12206FI see. Fine then.\x01",
            "...Forget what I just said.\x02\x03",
            "#12208FThen, I'll keep practicing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FY-Yeah...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#00100F(Hey Lloyd. Can we\x01",
            "spare the time somehow?)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#00003F(R-Right...\x01",
            "Let me rethink this.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x178, 4)
    SetChrPos(0xA, -50, 0, 15980, 180)
    OP_4C(0xA, 0xFF)
    BeginChrThread(0xA, 3, 0, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, 14050, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Jump("loc_106F8")

    label("loc_106F8")

    Return()

    # Function_57_10424 end

    def Function_58_106F9(): pass

    label("Function_58_106F9")

    EventBegin(0x0)
    Fade(500)
    OP_68(-620, 1320, 14390, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13000, 0)
    SetChrPos(0x101, 0, 0, 14050, 0)
    SetChrPos(0x102, 1000, 0, 14150, 0)
    SetChrPos(0x103, -1000, 0, 14150, 0)
    SetChrPos(0x104, 0, 450, 12100, 0)
    SetChrPos(0x105, 1000, 450, 12000, 0)
    SetChrPos(0x109, -1000, 450, 12100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#12205FWhat, didn't you\x01",
            "have stuff to do?\x02\x03",
            "#12200FCould you possibly...\x01",
            "Want to join my training?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 57)
    Return()

    # Function_58_106F9 end

    SaveToFile()

Try(main)
