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
        "Function_7_14AD",         # 07, 7
        "Function_8_18B1",         # 08, 8
        "Function_9_29ED",         # 09, 9
        "Function_10_306B",        # 0A, 10
        "Function_11_30E6",        # 0B, 11
        "Function_12_36AD",        # 0C, 12
        "Function_13_4187",        # 0D, 13
        "Function_14_429A",        # 0E, 14
        "Function_15_4463",        # 0F, 15
        "Function_16_4679",        # 10, 16
        "Function_17_4D29",        # 11, 17
        "Function_18_5A33",        # 12, 18
        "Function_19_5E27",        # 13, 19
        "Function_20_5ECC",        # 14, 20
        "Function_21_61F1",        # 15, 21
        "Function_22_65E6",        # 16, 22
        "Function_23_664C",        # 17, 23
        "Function_24_68A0",        # 18, 24
        "Function_25_6A33",        # 19, 25
        "Function_26_6A3A",        # 1A, 26
        "Function_27_6A60",        # 1B, 27
        "Function_28_8A86",        # 1C, 28
        "Function_29_8F77",        # 1D, 29
        "Function_30_9004",        # 1E, 30
        "Function_31_9DFB",        # 1F, 31
        "Function_32_A31D",        # 20, 32
        "Function_33_AD22",        # 21, 33
        "Function_34_B1B7",        # 22, 34
        "Function_35_C66A",        # 23, 35
        "Function_36_D027",        # 24, 36
        "Function_37_D604",        # 25, 37
        "Function_38_DD0B",        # 26, 38
        "Function_39_DD56",        # 27, 39
        "Function_40_DDA1",        # 28, 40
        "Function_41_DDD8",        # 29, 41
        "Function_42_DE23",        # 2A, 42
        "Function_43_DEBD",        # 2B, 43
        "Function_44_ED40",        # 2C, 44
        "Function_45_ED70",        # 2D, 45
        "Function_46_EDA0",        # 2E, 46
        "Function_47_EDD0",        # 2F, 47
        "Function_48_EE3F",        # 30, 48
        "Function_49_EE5C",        # 31, 49
        "Function_50_F242",        # 32, 50
        "Function_51_F266",        # 33, 51
        "Function_52_F28A",        # 34, 52
        "Function_53_F29F",        # 35, 53
        "Function_54_F2AD",        # 36, 54
        "Function_55_F2CC",        # 37, 55
        "Function_56_F2EB",        # 38, 56
        "Function_57_FF9D",        # 39, 57
        "Function_58_10267",       # 3A, 58
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1021")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4E")

    ChrTalk(
        0xFE,
        (
            "How about it? Isn't\x01",
            "their drive just\x01",
            "amazing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now anyway, we're doing our\x01",
            "best to resume performances as\x01",
            "quickly as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard Ilya has awoken... We\x01",
            "must do our best to live up\x01",
            "to her expectations as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(No one in the troupe\x01",
            "knows Rixia's location.)\x02\x03",
            "(I would have wanted to\x01",
            "show them her face,\x01",
            "but...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101C")

    label("loc_F4E")


    ChrTalk(
        0xFE,
        (
            "As always, we'll be here\x01",
            "working on our\x01",
            "performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lloyd and friends,\x01",
            "please take care of\x01",
            "Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, we understand.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_101C")

    ChrTalk(
        0x106,
        (
            "#10700FTroupe Chief... Thank\x01",
            "you very much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_101C")

    Jump("loc_14A9")

    label("loc_1021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_10A7")

    ChrTalk(
        0xFE,
        (
            "Everyone, you are really\x01",
            "doing your best for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ilya, Rixia... And all\x01",
            "of us here. We'll be\x01",
            "waiting for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A9")

    label("loc_10A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_12B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1233")
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xB,
        "Oh, Lloyd...\x02",
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
            "Thinking about various\x01",
            "things, I can't help but\x01",
            "be worried.\x02",
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
            "*sigh*, but I mustn't do\x01",
            "nothing but mope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I... I have to keep a\x01",
            "positive attitude.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x18D, 0)
    Jump("loc_12AE")

    label("loc_1233")


    ChrTalk(
        0xFE,
        (
            "*sigh*, I have to keep a\x01",
            "positive attitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If Ilya learns I was like\x01",
            "this this whole time,\x01",
            "she'll be mad at me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12AE")

    Jump("loc_14A9")

    label("loc_12B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1336")

    ChrTalk(
        0xFE,
        (
            "Sorry, Lloyd and\x01",
            "friends.\x02",
        )
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
    Jump("loc_14A9")

    label("loc_1336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1344")
    Jump("loc_14A9")

    label("loc_1344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1352")
    Jump("loc_14A9")

    label("loc_1352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1360")
    Jump("loc_14A9")

    label("loc_1360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_136E")
    Jump("loc_14A9")

    label("loc_136E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_137C")
    Jump("loc_14A9")

    label("loc_137C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_138A")
    Jump("loc_14A9")

    label("loc_138A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1418")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A5")
    Call(0, 8)
    Jump("loc_1413")

    label("loc_13A5")


    ChrTalk(
        0xFE,
        (
            "Goodness, Ilya is so\x01",
            "reliable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If she's like this,\x01",
            "tomorrow's performance\x01",
            "will surely be a success.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1413")

    Jump("loc_14A9")

    label("loc_1418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1426")
    Jump("loc_14A9")

    label("loc_1426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_14A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1441")
    Call(0, 7)
    Jump("loc_14A9")

    label("loc_1441")


    ChrTalk(
        0xFE,
        (
            "Though it might be a lot\x01",
            "to ask, I'm counting on\x01",
            "you.\x02",
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

    label("loc_14A9")

    TalkEnd(0xFE)
    Return()

    # Function_6_DDB end

    def Function_7_14AD(): pass

    label("Function_7_14AD")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176A")

    ChrTalk(
        0xB,
        (
            "So, Heintz. Technically,\x01",
            "can you do it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I tried, but...\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_159A")

    ChrTalk(
        0xB,
        (
            "Oh, you guys are the\x01",
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
    Jump("loc_1633")

    label("loc_159A")


    ChrTalk(
        0xB,
        "Oh, it's you all...\x02",
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

    label("loc_1633")


    ChrTalk(
        0x101,
        (
            "#00000FNo, we're just\x01",
            "patrolling the city\x01",
            "right now.\x02\x03",
            "We wanted to look in\x01",
            "here just as a\x01",
            "precautionary measure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, I see. Thank you for\x01",
            "coming here on your\x01",
            "patrols.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, if anything does\x01",
            "happen, please don't hesitate\x01",
            "to ask for our help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FAlright, and thanks.\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x10E, 0x0)
    OP_93(0xC, 0x5A, 0x0)
    SetScenarioFlags(0x136, 4)
    Jump("loc_18A8")

    label("loc_176A")


    ChrTalk(
        0xC,
        "But, is it ok?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If we speed it up, the\x01",
            "timing will be that much\x01",
            "more strict...\x02",
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
            "It seems that she wants\x01",
            "to test herself to the\x01",
            "very limit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I see... Then, I'll give\x01",
            "it a try.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x1, 3)

    label("loc_18A8")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_7_14AD end

    def Function_8_18B1(): pass

    label("Function_8_18B1")

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
        (
            "#06105FMy, if it isn't little\x01",
            "bro.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FHello. Sorry for\x01",
            "interrupting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06202FEveryone, hello.\x02\x03",
            "#06209FHaha, so you've finally\x01",
            "returned, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FOh, that's our Rixia for\x01",
            "you. I'm so happy you\x01",
            "were worried about me.\x02\x03",
            "#00309FAh~, but even so, to get\x01",
            "to see you and Ilya in\x01",
            "costume like this...\x02\x03",
            "I've seen them many times\x01",
            "before, but I seriously\x01",
            "never get tired of it.㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#06102FHaha, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06204FAh, hearing you say that\x01",
            "again is a little\x01",
            "embarrassing, though...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x104, 500)

    ChrTalk(
        0x105,
        (
            "#6P#10304FHehe. Randy's eyes are\x01",
            "always drawn to the most\x01",
            "lewd thing around, you see.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#11P#00301FWhat was that for, Wazy?\x01",
            "I was only saying it out\x01",
            "of my own pure heart―\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    ChrTalk(
        0x102,
        (
            "#11P#00106FAlright, we understand,\x01",
            "so let's just leave it\x01",
            "at that.\x02",
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

    def lambda_1D03():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D03)
    Sleep(50)

    def lambda_1D13():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1D13)
    Sleep(50)

    def lambda_1D23():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D23)
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
            "#00000FBy the way, are you\x01",
            "practicing?\x02",
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
            "#06202FHaha, tomorrow's guests\x01",
            "aren't just guests, and\x01",
            "I'm nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yeah, I can't believe the\x01",
            "heads of state are going\x01",
            "to visit our theater.\x02",
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
            "#12P#00105FThat's right. That came\x01",
            "up in our planning\x01",
            "meeting this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, they have been\x01",
            "invited to Crossbell,\x01",
            "after all.\x02\x03",
            "#10304FAnd Arc-en-Ciel\x01",
            "performances are the best\x01",
            "entertainment around.\x02",
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
        (
            "#12P#10100FBut, I can see why you'd\x01",
            "be nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06203FYes. It seems like the\x01",
            "other members are\x01",
            "nervous too...\x02\x03",
            "#06209FThough, Ilya's the same\x01",
            "as usual.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        (
            "#06103FWhat? I mean, worrying over\x01",
            "every little thing won't\x01",
            "solve anything, you know.\x02\x03",
            "#06100FNo matter who's sitting in\x01",
            "those seats, all I can do\x01",
            "is my best for them.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x8, 500)

    ChrTalk(
        0xB,
        (
            "#11PGoodness... We can\x01",
            "always rely on you,\x01",
            "can't we.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PAnd with the renewal\x01",
            "performance too. Your energy\x01",
            "amazes me every time.\x02",
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
            ""Golden Sun, Silver Moon" is\x01",
            "getting a renewal, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FYeah, that's a rumor\x01",
            "that's going around.\x02\x03",
            "I think they're saying\x01",
            "some bold arrangement\x01",
            "will be added?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_22F4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_22F4)
    Sleep(50)
    OP_93(0xB, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#06109FYes, that's right.\x02\x03",
            "#06104FIts revision is, in a way, a\x01",
            "challenge to ourselves, but...\x02\x03",
            "#06100FWe're aiming to bring the\x01",
            "script and direction to a whole\x01",
            "other level of perfection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06202FYes. Once tomorrow's performance is\x01",
            "over, we plan to focus on training\x01",
            "for it for approximately one month.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 2)), scpexpr(EXPR_END)), "loc_257C")

    ChrTalk(
        0x101,
        (
            "#12P#00000FI see. So when you said "looks like we're\x01",
            "going to be busy" when we met before, you\x01",
            "must have been talking about this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#06100FHaha, that's right.\x02",
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
    Jump("loc_25D3")

    label("loc_257C")


    ChrTalk(
        0x109,
        (
            "#12P#10100FI see... It seems like\x01",
            "you put a lot of work\x01",
            "into the new arrangement.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D3")


    ChrTalk(
        0x104,
        (
            "#12P#00300FBut "Golden Sun, Silver Moon" is\x01",
            "already known as one of Arc-en-\x01",
            "Ciel's best performances ever...\x02\x03",
            "#00304FIf you're going to improve it even\x01",
            "more, I can't even imagine how the\x01",
            "final product will turn out.\x02",
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
            "#06100FHaha, I live through dance. I'm\x01",
            "always searching for my best\x01",
            "performance.\x02\x03",
            "#06104FIn order to show our guests the\x01",
            "time of their lives, we have to\x01",
            "create an amazing performance...\x02\x03",
            "#06100FThat is the duty of Arc-en-Ciel,\x01",
            "and especially us artists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FI wouldn't have it any\x01",
            "other way... That's our\x01",
            "Ilya for you.\x02",
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
            "#06100FHaha. It'll be officially\x01",
            "announced before too long,\x01",
            "so please be patient.\x02\x03",
            "I'm sure even those who saw\x01",
            "the old version will be\x01",
            "able to enjoy it.\x02\x03",
            "#06104FAnd there's a little\x01",
            "surprise in the cast... I'm\x01",
            "sure you'll be shocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FSurprise you say... Haha,\x01",
            "then I'll look forward to\x01",
            "seeing what it is.\x02",
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

    # Function_8_18B1 end

    def Function_9_29ED(): pass

    label("Function_9_29ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_29FE")
    Jump("loc_3067")

    label("loc_29FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2A0C")
    Jump("loc_3067")

    label("loc_2A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2AF0")
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x8,
        (
            "#01700FAlright, we'll now check the scene\x01",
            "where the Moon Princess appears and\x01",
            "pursues the other two princesses.\x02\x03",
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
    Jump("loc_3067")

    label("loc_2AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2B01")
    Call(0, 10)
    Jump("loc_3067")

    label("loc_2B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2B0F")
    Jump("loc_3067")

    label("loc_2B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B1D")
    Jump("loc_3067")

    label("loc_2B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2C98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B38")
    Call(0, 30)
    Jump("loc_2C93")

    label("loc_2B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C16")

    ChrTalk(
        0x8,
        (
            "#01709FHaha. It's been a while\x01",
            "since I thought of my\x01",
            "past, you know.\x02\x03",
            "#01700FIf you like, come see our\x01",
            "renewal performance.\x02\x03",
            "Rixia and Sully there will\x01",
            "be in it too. It's sure to\x01",
            "be an amazing show.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C93")

    label("loc_2C16")


    ChrTalk(
        0x8,
        (
            "#01700FCome and see our renewal\x01",
            "performance.\x02\x03",
            "Rixia and Sully there will\x01",
            "be in it too. It's sure to\x01",
            "be an amazing show.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C93")

    Jump("loc_3067")

    label("loc_2C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2CA6")
    Jump("loc_3067")

    label("loc_2CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2CB4")
    Jump("loc_3067")

    label("loc_2CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CCF")
    Call(0, 8)
    Jump("loc_2E83")

    label("loc_2CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DDE")

    ChrTalk(
        0x8,
        (
            "#06100FI live through dance. I'm always\x01",
            "searching for my best\x01",
            "performance.\x02\x03",
            "#06104FIn order to show our guests the\x01",
            "time of their lives, we have to\x01",
            "create an amazing performance...\x02\x03",
            "#06102FThat is the duty of Arc-en-Ciel,\x01",
            "and especially us artists.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E83")

    label("loc_2DDE")


    ChrTalk(
        0x8,
        (
            "#06100FHaha. It'll be officially\x01",
            "announced before too long,\x01",
            "so please be patient.\x02\x03",
            "#06104FI'm sure even those who\x01",
            "saw the old version will\x01",
            "be able to enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E83")

    Jump("loc_3067")

    label("loc_2E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2E96")
    Jump("loc_3067")

    label("loc_2E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3067")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF1")

    ChrTalk(
        0x8,
        (
            "#01700FHaha, I see some new faces.\x01",
            "That must mean you guys\x01",
            "have finally restarted.\x02\x03",
            "#01700FI think Cecil is looking\x01",
            "forward to seeing you guys\x01",
            "too.\x02\x03",
            "#01709FMaaan, how wonderful for\x01",
            "you, eh? Eh?㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FH-Haha... Please don't\x01",
            "make fun of us.\x02\x03",
            "#00004F(She's right though. I\x01",
            "should visit Cecil\x01",
            "before too long.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3067")

    label("loc_2FF1")


    ChrTalk(
        0x8,
        (
            "#01700FHaha, look forward to\x01",
            "what we're planning\x01",
            "next.\x02\x03",
            "#01709FIt's still a secret, but\x01",
            "I'm sure you'll love it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3067")

    TalkEnd(0xFE)
    Return()

    # Function_9_29ED end

    def Function_10_306B(): pass

    label("Function_10_306B")

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
        "#12201FR-Right!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_10_306B end

    def Function_11_30E6(): pass

    label("Function_11_30E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_30F7")
    Jump("loc_36A9")

    label("loc_30F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3105")
    Jump("loc_36A9")

    label("loc_3105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_319D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_317C")

    ChrTalk(
        0x9,
        (
            "#01808F―Excuse me. It's right\x01",
            "before our performance,\x01",
            "you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F(Rixia...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3198")

    label("loc_317C")


    ChrTalk(
        0x9,
        "#01801FIlya... Please!\x02",
    )

    CloseMessageWindow()

    label("loc_3198")

    Jump("loc_36A9")

    label("loc_319D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_31AB")
    Jump("loc_36A9")

    label("loc_31AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_31B9")
    Jump("loc_36A9")

    label("loc_31B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_31C7")
    Jump("loc_36A9")

    label("loc_31C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_31D5")
    Jump("loc_36A9")

    label("loc_31D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_31E3")
    Jump("loc_36A9")

    label("loc_31E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_31F1")
    Jump("loc_36A9")

    label("loc_31F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_349C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_320C")
    Call(0, 8)
    Jump("loc_3497")

    label("loc_320C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3414")

    ChrTalk(
        0x9,
        (
            "#06203FThe trade conference... So it's really\x01",
            "true that all sorts of different\x01",
            "people are coming to Crossbell.\x02",
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
        (
            "#00105FIs there something else\x01",
            "you're worried about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06202FAh, well... It's no big\x01",
            "deal, so please don't\x01",
            "worry about it.\x02\x03",
            "#06204FAnd anyway, right now I\x01",
            "need to focus on my\x01",
            "performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FR-Right...\x02\x03",
            "#00003F(Is Rixia worried about\x01",
            "something related to the\x01",
            "trade conference?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14C, 0)
    Jump("loc_3497")

    label("loc_3414")


    ChrTalk(
        0x9,
        (
            "#06206FI'm the type to worry\x01",
            "about unnecessary\x01",
            "things, aren't I.\x02\x03",
            "#06201FAnyway, right now I need\x01",
            "to focus on my\x01",
            "performance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3497")

    Jump("loc_36A9")

    label("loc_349C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_34AA")
    Jump("loc_36A9")

    label("loc_34AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_36A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3607")

    ChrTalk(
        0x9,
        (
            "#01802FYou've added new members and\x01",
            "restarted... I'll be cheering\x01",
            "for all of you from now on, ok?\x02\x03",
            "Please, everyone... Feel free\x01",
            "to visit us anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSure. And please feel\x01",
            "free to contact us if\x01",
            "you ever need anything.\x02\x03",
            "We'd be glad to help\x01",
            "whenever needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01809FHaha, I'll be counting\x01",
            "on you then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_36A9")

    label("loc_3607")


    ChrTalk(
        0x9,
        (
            "#01802FYou've added new members and\x01",
            "restarted... I'll be cheering\x01",
            "for all of you from now on, ok?\x02\x03",
            "#01809FPlease, everyone... Feel free\x01",
            "to visit us anytime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36A9")

    TalkEnd(0xFE)
    Return()

    # Function_11_30E6 end

    def Function_12_36AD(): pass

    label("Function_12_36AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36D3")
    Call(0, 58)
    Return()

    label("loc_36D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F1")
    Call(0, 35)
    Jump("loc_3E04")

    label("loc_36F1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_END)), "loc_39E9")

    ChrTalk(
        0xA,
        (
            "#04200FOh, did you guys already\x01",
            "go visit Ilya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah. She showed us her\x01",
            "energetic spirit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04203FIs that so...\x02\x03",
            "#04200FUmm, how about you,\x01",
            "Rixia?\x02",
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
            "#04205FI wasn't particularly\x01",
            "worried...\x02\x03",
            "#04204FBut... I feel relieved\x01",
            "for some reason.\x02\x03",
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
            "#04206FSorry, Rixia. That was\x01",
            "impertinent.\x02\x03",
            "#04202FFor now, I'll stand by\x01",
            "here.\x02\x03",
            "#04209FAnyway, come back soon,\x01",
            "ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10702FHaha... Sure,\x01",
            "understood.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBA")

    label("loc_39E9")


    ChrTalk(
        0xA,
        (
            "#14000FOh, did you guys already\x01",
            "go visit Ilya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah. She showed us her\x01",
            "energetic spirit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14003FIs that so...\x02\x03",
            "#14000FUmm, how about you,\x01",
            "Rixia?\x02",
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
            "#14005FI wasn't particularly\x01",
            "worried...\x02\x03",
            "#14004FBut... I feel relieved\x01",
            "for some reason.\x02\x03",
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
            "#14006FSorry, Rixia. That was\x01",
            "impertinent.\x02\x03",
            "#14002FFor now, I'll stand by\x01",
            "here.\x02\x03",
            "#14009FAnyway, come back soon,\x01",
            "ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10702FHaha... Sure,\x01",
            "understood.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CBA")

    SetScenarioFlags(0x1CF, 7)
    Jump("loc_3E04")

    label("loc_3CC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_END)), "loc_3D6A")

    ChrTalk(
        0xA,
        (
            "#04200FI don't know where you're going,\x01",
            "but be careful, ok?\x02\x03",
            "#04202FWe'll be restarting performances\x01",
            "before long. I definitely want\x01",
            "you to see them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E04")

    label("loc_3D6A")


    ChrTalk(
        0xA,
        (
            "#14000FI don't know where you're going,\x01",
            "but be careful, ok?\x02\x03",
            "#14002FWe'll be restarting performances\x01",
            "before long. I definitely want\x01",
            "you to see them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E04")

    Jump("loc_4183")

    label("loc_3E09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3E7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E24")
    Call(0, 13)
    Jump("loc_3E7A")

    label("loc_3E24")


    ChrTalk(
        0xA,
        (
            "#12203F...First the music starts,\x01",
            "then I come out from the\x01",
            "stage wing dancing...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E7A")

    Jump("loc_4183")

    label("loc_3E7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3E8D")
    Jump("loc_4183")

    label("loc_3E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3EBF")

    ChrTalk(
        0xA,
        "#04201FIlya, I'm always ready!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4183")

    label("loc_3EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3ED0")
    Call(0, 10)
    Jump("loc_4183")

    label("loc_3ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3EDE")
    Jump("loc_4183")

    label("loc_3EDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3EEC")
    Jump("loc_4183")

    label("loc_3EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3EFA")
    Jump("loc_4183")

    label("loc_3EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3FBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F15")
    Call(0, 14)
    Jump("loc_3FB7")

    label("loc_3F15")


    ChrTalk(
        0xA,
        (
            "#04203FFocusing on the stage in\x01",
            "front of me... I see, so\x01",
            "that's what it means.\x02\x03",
            "#04201FA-Alright... I'll\x01",
            "practice without thinking\x01",
            "about unnecessary things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FB7")

    Jump("loc_4183")

    label("loc_3FBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3FCA")
    Jump("loc_4183")

    label("loc_3FCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_40EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_404E")

    ChrTalk(
        0xA,
        (
            "#04206FIlya and Rixia sure are\x01",
            "amazing.\x02\x03",
            "#04200FI wonder if I'll be able\x01",
            "to perform like they\x01",
            "do...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_40E9")

    label("loc_404E")


    ChrTalk(
        0xA,
        (
            "#04205FWhoops, I can't stand around\x01",
            "daydreaming. I've got to hurry\x01",
            "and finish up the cleaning.\x02\x03",
            "#04203FI'll lose my practice time if\x01",
            "I'm not careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40E9")

    Jump("loc_4183")

    label("loc_40EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_40FC")
    Jump("loc_4183")

    label("loc_40FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4183")

    ChrTalk(
        0xA,
        (
            "#04200FEven so... How does she\x01",
            "know that Rixia improved\x01",
            "the way she rests?\x02\x03",
            "#04204F...I knew it. Ilya\x01",
            "really is amazing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4183")

    TalkEnd(0xFE)
    Return()

    # Function_12_36AD end

    def Function_13_4187(): pass

    label("Function_13_4187")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0x11,
        (
            "Then, Nikol, Sully.\x01",
            "Please follow along as\x01",
            "it's my first time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Understood. Let's go,\x01",
            "Sully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12201FSure. First is the step,\x01",
            "then the jump.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Sully and everyone else...\x01",
            "Looks like they're focused\x01",
            "on their training.)\x02",
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

    # Function_13_4187 end

    def Function_14_429A(): pass

    label("Function_14_429A")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xA,
        (
            "#04205FSay, Nikol.\x02\x03",
            "Why won't Ilya and the others\x01",
            "give us the details of the\x01",
            "renewal performance already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Although I don't have the\x01",
            "answer, don't we have the\x01",
            "final performance left?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "If they tell you before that's\x01",
            "done, you won't be able to\x01",
            "focus and it'll be a problem...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I think that's the most\x01",
            "likely reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04203FO-Oh... I see. You're\x01",
            "smart, Nikol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Umm, I'm just thinking\x01",
            "normally, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 2)
    Return()

    # Function_14_429A end

    def Function_15_4463(): pass

    label("Function_15_4463")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xA,
        (
            "#04200FSay, Nikol. About the\x01",
            "change in that turn you\x01",
            "do in that scene...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Yeah, I was able to get\x01",
            "it down without much\x01",
            "trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "The timing is tight, but\x01",
            "otherwise it's pretty\x01",
            "smooth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#04201FI-I see. Nice work.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_45E7")

    ChrTalk(
        0x101,
        (
            "#00000F(Sully... Looks like\x01",
            "she's doing her best\x01",
            "with her training.)\x02",
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
    Jump("loc_4660")

    label("loc_45E7")


    ChrTalk(
        0x101,
        (
            "#00005F(So she's Arc-en-Ciel's\x01",
            "novice artist, huh...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Haha, looks like she's\x01",
            "focused on her\x01",
            "training.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4660")

    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 2)
    Return()

    # Function_15_4463 end

    def Function_16_4679(): pass

    label("Function_16_4679")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46A2")
    Call(0, 36)
    Return()

    label("loc_46A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_46B3")
    Jump("loc_4D25")

    label("loc_46B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4760")

    ChrTalk(
        0xFE,
        (
            "Even so... The martial law\x01",
            "was too sudden and caused\x01",
            "considerable confusion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well anyway, all those of\x01",
            "us left here can do is\x01",
            "focus on our training.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D25")

    label("loc_4760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_47B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_477B")
    Call(0, 13)
    Jump("loc_47B4")

    label("loc_477B")


    ChrTalk(
        0xFE,
        (
            "First is to match\x01",
            "Sully's timing, and from\x01",
            "there...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47B4")

    Jump("loc_4D25")

    label("loc_47B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_47C7")
    Jump("loc_4D25")

    label("loc_47C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_488D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47E2")
    Call(0, 24)
    Jump("loc_4888")

    label("loc_47E2")


    ChrTalk(
        0xFE,
        (
            "I-I don't really get it\x01",
            "but it seems like I\x01",
            "stepped on something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, whatever... Theodore was\x01",
            "saying this too, so I have to\x01",
            "hurry up and start training.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4888")

    Jump("loc_4D25")

    label("loc_488D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_489B")
    Jump("loc_4D25")

    label("loc_489B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_48A9")
    Jump("loc_4D25")

    label("loc_48A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_48B7")
    Jump("loc_4D25")

    label("loc_48B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_48C5")
    Jump("loc_4D25")

    label("loc_48C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4972")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48E0")
    Call(0, 14)
    Jump("loc_496D")

    label("loc_48E0")


    ChrTalk(
        0xFE,
        (
            "How to say this... Sully\x01",
            "is very direct.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, that's exactly why there\x01",
            "are so many things she has to\x01",
            "learn. I've got to do better.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_496D")

    Jump("loc_4D25")

    label("loc_4972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4980")
    Jump("loc_4D25")

    label("loc_4980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4B02")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A1E")

    ChrTalk(
        0xFE,
        (
            "Alright... I'll start\x01",
            "training again, starting\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll leave the medical\x01",
            "questionnaire to you\x01",
            "guys.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AFD")

    label("loc_4A1E")


    ChrTalk(
        0xFE,
        (
            "Although I'm worried about tomorrow's\x01",
            "performance, I can't help but be curious\x01",
            "about the details of the renewal performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But even so, I mustn't think\x01",
            "about anything unnecessary.\x01",
            "For now, I need only practice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AFD")

    Jump("loc_4D25")

    label("loc_4B02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4B10")
    Jump("loc_4D25")

    label("loc_4B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4D25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C73")

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
            "Our troupe is composed\x01",
            "of mostly geniuses like\x01",
            "that, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although, in addition to\x01",
            "talent, they practice hard\x01",
            "too. I can't compare to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, all I can do is\x01",
            "my best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_4D25")

    label("loc_4C73")


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
            "I was lost for a time\x01",
            "but... Anyway, all I can\x01",
            "do is my very best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D25")

    TalkEnd(0xFE)
    Return()

    # Function_16_4679 end

    def Function_17_4D29(): pass

    label("Function_17_4D29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4F7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EE5")

    ChrTalk(
        0xC,
        "Hey, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Actually, we were\x01",
            "contacted by the meister\x01",
            "just now.\x02",
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
        "#00000FWow... That's great.\x02",
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
            "meister hardly ever\x01",
            "contacts us, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "There is no greater\x01",
            "happiness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(I thought the meister\x01",
            "might be worried about\x01",
            "this place.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(Haha. I hope he\x01",
            "finishes them quickly.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CF, 6)
    Jump("loc_4F75")

    label("loc_4EE5")


    ChrTalk(
        0xC,
        (
            "To receive proactive\x01",
            "cooperation from the meister...\x01",
            "There is no greater happiness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I've got to do better\x01",
            "with making the\x01",
            "foundation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F75")

    Jump("loc_5A2F")

    label("loc_4F7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_507E")

    ChrTalk(
        0xFE,
        (
            "The stage preparation and automata\x01",
            "the meister is helping us with\x01",
            "would be impossible for me alone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, it's all I can\x01",
            "do to get the stage in\x01",
            "order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The meister is worried\x01",
            "about it too... I've got\x01",
            "to build it as best I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A2F")

    label("loc_507E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_51D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5159")

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
    Jump("loc_51CE")

    label("loc_5159")


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

    label("loc_51CE")

    Jump("loc_5A2F")

    label("loc_51D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_53DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_532F")

    ChrTalk(
        0xFE,
        (
            "The props and automata\x01",
            "the meister built for us\x01",
            "were all destroyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They were peerless works of art\x01",
            "the meister and troupe members\x01",
            "poured their souls into...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To trample over them is\x01",
            "unforgivable\x01",
            "recklessness...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, in the end they\x01",
            "are just works of art.\x01",
            "They can be rebuilt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But Ilya is...!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_53D8")

    label("loc_532F")


    ChrTalk(
        0xFE,
        (
            "...Anyway, I'll rebuild them\x01",
            "as many times as I have to for\x01",
            "the sake of our performances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I let something like\x01",
            "this break me, I'd have\x01",
            "no excuses for Ilya.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53D8")

    Jump("loc_5A2F")

    label("loc_53DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_550F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_549E")

    ChrTalk(
        0xFE,
        (
            "Alright, with this, the\x01",
            "stage setting is\x01",
            "perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And I finished\x01",
            "rehearsing the movements\x01",
            "yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All that's left is to\x01",
            "wait for the\x01",
            "performance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_550A")

    label("loc_549E")


    ChrTalk(
        0xFE,
        (
            "Alright, with this, the\x01",
            "stage setting is\x01",
            "perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All that's left is to\x01",
            "wait for the\x01",
            "performance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_550A")

    Jump("loc_5A2F")

    label("loc_550F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_551D")
    Jump("loc_5A2F")

    label("loc_551D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_552B")
    Jump("loc_5A2F")

    label("loc_552B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5539")
    Jump("loc_5A2F")

    label("loc_5539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_56FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_564D")

    ChrTalk(
        0xFE,
        (
            "The new stage setting I\x01",
            "asked for will finally\x01",
            "be completed tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I might have asked for\x01",
            "various impossible\x01",
            "things this time, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The meister always pulls\x01",
            "through for me in the\x01",
            "end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm looking forward to\x01",
            "going to get it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_56F6")

    label("loc_564D")


    ChrTalk(
        0xFE,
        (
            "I might have asked for\x01",
            "various impossible\x01",
            "things this time, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The meister always pulls through\x01",
            "for me in the end. I'm looking\x01",
            "forward to going to get it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56F6")

    Jump("loc_5A2F")

    label("loc_56FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_58BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5843")

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
            "details in between practices for\x01",
            "the renewal performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The reality of opening\x01",
            "day being a month away\x01",
            "hasn't sunk in yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I don't hurry, I\x01",
            "won't finish on time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_58B9")

    label("loc_5843")


    ChrTalk(
        0xFE,
        (
            "The reality of opening\x01",
            "day being a month away\x01",
            "hasn't sunk in yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I don't hurry, I\x01",
            "won't finish on time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58B9")

    Jump("loc_5A2F")

    label("loc_58BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_58CC")
    Jump("loc_5A2F")

    label("loc_58CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5987")

    ChrTalk(
        0xFE,
        (
            "Tomorrow, we're all on break\x01",
            "until 3PM to prepare for the\x01",
            "evening performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since I have some free time,\x01",
            "I was thinking of going to\x01",
            "see the unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A2F")

    label("loc_5987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5995")
    Jump("loc_5A2F")

    label("loc_5995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5A2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59B0")
    Call(0, 7)
    Jump("loc_5A2F")

    label("loc_59B0")


    ChrTalk(
        0xFE,
        (
            "But, a 50 percent\x01",
            "increase, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though I'm of course going\x01",
            "to do my very best, that's\x01",
            "another ridiculous request.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A2F")

    TalkEnd(0xFE)
    Return()

    # Function_17_4D29 end

    def Function_18_5A33(): pass

    label("Function_18_5A33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5AEE")

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
            "Ilya's cheering for us\x01",
            "too... Nothing could be\x01",
            "more encouraging.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E23")

    label("loc_5AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5BB4")

    ChrTalk(
        0xFE,
        (
            "We can only perform― And\x01",
            "we're fortunate to have\x01",
            "fans who support us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, there's only one\x01",
            "choice. Even in a situation like\x01",
            "this, we'll train as we usually do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E23")

    label("loc_5BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5C01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BCF")
    Call(0, 19)
    Jump("loc_5BFC")

    label("loc_5BCF")


    ChrTalk(
        0xFE,
        (
            "Let's go, Theodore.\x01",
            "Let's get fired up!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BFC")

    Jump("loc_5E23")

    label("loc_5C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5C0F")
    Jump("loc_5E23")

    label("loc_5C0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5C9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C2A")
    Call(0, 20)
    Jump("loc_5C96")

    label("loc_5C2A")


    ChrTalk(
        0xFE,
        (
            "Though I say that, I\x01",
            "would be good in any\x01",
            "role.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must serve a role in\x01",
            "accordance with our\x01",
            "needs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C96")

    Jump("loc_5E23")

    label("loc_5C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5E23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D89")

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
            "Princess Klaudia is sweet, but\x01",
            "assigning Lt. Julia to her\x01",
            "guard is too much of a waste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With her swordplay, she'd\x01",
            "certainly be a star if\x01",
            "she were to join us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5E23")

    label("loc_5D89")


    ChrTalk(
        0xFE,
        (
            "Lt. Julia... With her\x01",
            "figure, it's a waste for\x01",
            "her to be in the military.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With her swordplay, she'd\x01",
            "certainly be a star if\x01",
            "she were to join us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E23")

    TalkEnd(0xFE)
    Return()

    # Function_18_5A33 end

    def Function_19_5E27(): pass

    label("Function_19_5E27")

    OP_4B(0xD, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xD,
        (
            "Alright, Pliｳ. Is it\x01",
            "time for your solo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Understood. I'll be\x01",
            "right there, so get them\x01",
            "excited, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "...Understood.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_19_5E27 end

    def Function_20_5ECC(): pass

    label("Function_20_5ECC")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xD,
        (
            "Alright, Theodore. Our\x01",
            "climax scene is coming\x01",
            "up next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You, the altar's guardian knight\x01",
            "would raise swords against I,\x01",
            "the debaucherous prince...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Ugh. I feel regret when\x01",
            "I say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Since we're doing the\x01",
            "renewal, I would have wanted\x01",
            "this revised as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "*sigh*... That's quite a\x01",
            "thing to say at this\x01",
            "late date.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's fine. Just shut up\x01",
            "and go along with it you\x01",
            "stupiGene.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "Y-You. Did you just call\x01",
            "me stupiGene?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Then you're stupiDore!\x01",
            "Right, stupiDore!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...Sorry. Anyway, hurry\x01",
            "up and go along with it.\x02",
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
            "#00005F(I didn't think they'd\x01",
            "be like this right\x01",
            "before the performance.)\x02",
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

    # Function_20_5ECC end

    def Function_21_61F1(): pass

    label("Function_21_61F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_62AB")

    ChrTalk(
        0xFE,
        (
            "Hmm... I feel I'm very\x01",
            "lucky to be a performer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I owe a lot of things to a lot of\x01",
            "people... I've got to train even harder\x01",
            "to repay each and every one of them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65E2")

    label("loc_62AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_62B9")
    Jump("loc_65E2")

    label("loc_62B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_631C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62D4")
    Call(0, 19)
    Jump("loc_6317")

    label("loc_62D4")


    ChrTalk(
        0xFE,
        (
            "Hear that, Eugene? I\x01",
            "won't be cast aside by\x01",
            "the likes of you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6317")

    Jump("loc_65E2")

    label("loc_631C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_632A")
    Jump("loc_65E2")

    label("loc_632A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_64DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6345")
    Call(0, 20)
    Jump("loc_64D7")

    label("loc_6345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6435")

    ChrTalk(
        0xE,
        (
            "Since forever, Eugene has\x01",
            "been agitated and has had\x01",
            "a bad habit of backtalk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I wish he'd give me a\x01",
            "break already.\x02",
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
            "spouting pointless\x01",
            "things!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_64D7")

    label("loc_6435")


    ChrTalk(
        0xFE,
        (
            "Anyway... No matter what kind\x01",
            "of performance it is, the\x01",
            "first performance is special.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there's time, I want to\x01",
            "go over the performance\x01",
            "one more time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64D7")

    Jump("loc_65E2")

    label("loc_64DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_65E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65A6")

    ChrTalk(
        0xFE,
        "...Indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard Princess Klaudia has\x01",
            "experience in theater from\x01",
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
    Jump("loc_65E2")

    label("loc_65A6")


    ChrTalk(
        0xFE,
        (
            "Indeed... I'd love to\x01",
            "see those two on stage\x01",
            "sometime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65E2")

    TalkEnd(0xFE)
    Return()

    # Function_21_61F1 end

    def Function_22_65E6(): pass

    label("Function_22_65E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6648")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6604")
    Call(0, 19)
    Jump("loc_6648")

    label("loc_6604")


    ChrTalk(
        0xFE,
        (
            "That's quite an\x01",
            "expression you guys have.\x01",
            "I won't lose to you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6648")

    TalkEnd(0xFE)
    Return()

    # Function_22_65E6 end

    def Function_23_664C(): pass

    label("Function_23_664C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_665D")
    Jump("loc_689C")

    label("loc_665D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6777")

    ChrTalk(
        0xFE,
        (
            "To do something like that\x01",
            "on stage at a time like\x01",
            "this... I have no words...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As for me, I strongly believe that\x01",
            "entertainment is needed precisely\x01",
            "because of this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because when they despair,\x01",
            "people lose the ability to\x01",
            "enjoy amusement, correct?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_689C")

    label("loc_6777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_67D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6792")
    Call(0, 13)
    Jump("loc_67CF")

    label("loc_6792")


    ChrTalk(
        0xFE,
        (
            "I'll make my performance\x01",
            "more nimble, more\x01",
            "beautiful...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67CF")

    Jump("loc_689C")

    label("loc_67D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_67E2")
    Jump("loc_689C")

    label("loc_67E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_689C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67FD")
    Call(0, 24)
    Jump("loc_689C")

    label("loc_67FD")


    ChrTalk(
        0xFE,
        (
            "Goodness, that Nikol. He\x01",
            "never lets down his guard,\x01",
            "and he has no weak points!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This must be a technique\x01",
            "of docile young men.\x01",
            "I'll never forgive him!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_689C")

    TalkEnd(0xFE)
    Return()

    # Function_23_664C end

    def Function_24_68A0(): pass

    label("Function_24_68A0")

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
        "Foil? You're no foil.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "You know I love your\x01",
            "acting, right?\x02",
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
            "Wh-What are you saying\x01",
            "all of a sudden?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "C-Cut the chatter and\x01",
            "get your acting\x01",
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
            "...Umm, why such foul\x01",
            "language?\x02",
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

    # Function_24_68A0 end

    def Function_25_6A33(): pass

    label("Function_25_6A33")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_25_6A33 end

    def Function_26_6A3A(): pass

    label("Function_26_6A3A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A5F")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_26_6A3A")

    label("loc_6A5F")

    Return()

    # Function_26_6A3A end

    def Function_27_6A60(): pass

    label("Function_27_6A60")

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
            "front of Rixia too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#01802FHaha, Ilya. You're\x01",
            "troubling Sully, right?\x02",
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
        (
            "#12P#00000FHaha. Things sure are\x01",
            "lively in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FHaha. Looks like you're\x01",
            "taking a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FI-It's Ilya Platiere!\x01",
            "The real Ilya Platiere!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FAnd the two beside her\x01",
            "are...\x02",
        )
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
        "#01700FHmm?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#01705FAh, it's little bro!!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    OP_64(0x9)
    OP_64(0xA)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6DDF():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6DDF)
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0x9,
        "#5P#01802FAh... Everyone!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EE2")
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
            "#1K◆ZnK quest [Stalker Inv.\x01",
            "Request]? (debug)\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No Change]\x01",       # 0
            "[Completed]\x01",       # 1
            "[Incomplete]\x01",      # 2
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
        (0, "loc_6EC9"),
        (1, "loc_6ECE"),
        (2, "loc_6ED8"),
        (SWITCH_DEFAULT, "loc_6EE2"),
    )


    label("loc_6EC9")

    Jump("loc_6EE2")

    label("loc_6ECE")

    OP_29(0x1D, 0x4, 0x10)
    Jump("loc_6EE2")

    label("loc_6ED8")

    OP_29(0x1D, 0x3, 0x10)
    Jump("loc_6EE2")

    label("loc_6EE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F0A")

    ChrTalk(
        0xA,
        "#04200F...Hello.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F1F")

    label("loc_6F0A")


    ChrTalk(
        0xA,
        "#04200F...Hmph.\x02",
    )

    CloseMessageWindow()

    label("loc_6F1F")


    def lambda_6F24():
        OP_95(0xFE, 700, 1450, 12200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F24)

    def lambda_6F3E():
        OP_95(0xFE, -700, 1450, 11760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6F3E)

    def lambda_6F58():
        OP_95(0xFE, 700, 1450, 10980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6F58)

    def lambda_6F72():
        OP_95(0xFE, -700, 1450, 10680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6F72)
    OP_68(-820, 1620, 12730, 3000)
    MoveCamera(39, 26, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(13510, 3000)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#12P#00000FHaha, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FSorry, it looks like we\x01",
            "interrupted your\x01",
            "break...\x02",
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
            "Haha, not at all㈱\x02\x03",
            "It's been a while and you came to\x01",
            "see us. Take it easy!\x02\x03",
            "Ah, but since you're here, can I\x01",
            "get a reunion hug from little bro?\x02",
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
        "#12P#00012FN-No, I'll pass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01702FAww, really? You don't have\x01",
            "to hold back, you know.\x02\x03",
            "#01709FHaha, or possibly~... Might\x01",
            "you prefer the feeling of a\x01",
            "Rixia hug instead?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x9)

    def lambda_7234():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7234)
    Sleep(50)

    def lambda_7244():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7244)

    ChrTalk(
        0x101,
        "#12P#00011FU-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#01806FI-Ilya...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12P#04200FDamn. Stop acting like a\x01",
            "dirty old man.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 500)

    ChrTalk(
        0x102,
        (
            "#12P#00109FHaha... Looks like you\x01",
            "have it tough as always,\x01",
            "Rixia.\x02",
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
            "A-Ahaha... It might be what they\x01",
            "call fate.\x02\x03",
            "But, I am glad to see all of you\x01",
            "after so long.\x02\x03",
            "Haha. I really am glad to see you\x01",
            "again.\x02",
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
            "#12P#10304FHaha. Rixia, you're the artist that\x01",
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
            "#01805FUmm, and you are... That\x01",
            "delinquent group in\x01",
            "Downtown's...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWazy Hemisphere. Hehe,\x01",
            "I'm honored that you\x01",
            "know me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01705FOh, you know him, Rixia?\x02\x03",
            "Now that you mention it,\x01",
            "that girl wasn't with\x01",
            "you before, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes. They're our new\x01",
            "members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FNoｱl Seeker. I\x01",
            "transferred to the SSS\x01",
            "from the Guardian Force.\x02\x03",
            "#10109FUmm... My little sister\x01",
            "Fran and I are always\x01",
            "cheering for you guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#01709FHaha, thanks☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FTio and Randy aren't\x01",
            "back yet.\x02\x03",
            "#00100FIt'll be just the four\x01",
            "of us for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01700FI see~.\x02\x03",
            "#01709FHaha, looks like you've\x01",
            "got some pretty\x01",
            "interesting faces there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FU-Umm~... You seem\x01",
            "disappointed, though.\x02",
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
            "#5P#01702FHaha, thanks. But you\x01",
            "know flattery won't get\x01",
            "you anywhere, right?\x02\x03",
            "#01703FWell, that aside...\x02\x03",
            "#01709FHey. You've been quiet\x01",
            "this whole time. Give a\x01",
            "proper greeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P#04205F...O-Okay.\x02",
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
            "I'm Sully Atraid, an assistant with\x01",
            "this troupe.\x02\x03",
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
        "#12P#10100FHaha, same here Sully.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7E66")

    ChrTalk(
        0x101,
        (
            "#12P#00000FHaha. How have you been,\x01",
            "Sully?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        (
            "#5P#04203FHmph, don't smile when you\x01",
            "talk to me.\x02\x03",
            "#04201FLet me just say this. I\x01",
            "haven't forgotten what\x01",
            "happened back then, you hear?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006F(S-She's still angry\x01",
            "about that, huh...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FUmm, back then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01709FUmm, if I'm remembering it\x01",
            "right, little bro here\x01",
            "grabbed her from behind and─\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00011FI-I don't think...\x02\x03",
            "#00006FAnyway, Sully was the\x01",
            "cause of the whole\x01",
            "thing, right!?\x02",
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
            "#04208F...I-I may have been in\x01",
            "the wrong, but...\x02\x03",
            "#04201FHow dare you grab me so\x01",
            "tightly like that!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7CD5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7CD5)
    Sleep(50)

    def lambda_7CE5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7CE5)
    Sleep(50)
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x109,
        "#12P#10105FG-Grab!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FHaha, sounds fun.\x02",
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
            "#5P#01709FOh, a battle! This\x01",
            "doesn't happen often, so\x01",
            "I'm joining in too─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#01806FI-Ilya... You're making\x01",
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
            "#12P#00006F(Ugh. The more I deny\x01",
            "it, the more guilty I\x01",
            "look...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81E1")

    label("loc_7E66")


    ChrTalk(
        0x101,
        (
            "#12P#00005FHuh? Now that I see\x01",
            "Sully better...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00011F#4SS-She's a girl!?#3S\x02\x03",
            "#00003FO-Oh. I've come here\x01",
            "many times, but never\x01",
            "realized.\x02\x03",
            "#00000FYeah, taking a closer\x01",
            "look at her, she does\x01",
            "have a cute face...\x02",
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

    def lambda_7FF6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7FF6)
    Sleep(50)

    def lambda_8006():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8006)
    Sleep(50)

    def lambda_8016():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8016)
    Sleep(50)

    def lambda_8026():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8026)
    Sleep(50)

    def lambda_8036():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8036)
    Sleep(50)
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        "#5P#04201FY-You jerk...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P#01806FL-Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00111F...How rude.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#11P#00011FAh, sorry! Since you\x01",
            "speak like a boy I\x01",
            "thought...! Sorry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01709FAhaha, that's our little\x01",
            "bro.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHmm, could that be a pattern\x01",
            "for airhead gigolos use?\x01",
            "I've learned something here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        "#5P#00011FI-I don't think...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#04203F...Hmph, I don't like\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81E1")


    ChrTalk(
        0x9,
        (
            "#5P#01803FHaha, but even so... I'm glad\x01",
            "you're doing well.\x02\x03",
            "#01809FThe Support Section has done\x01",
            "so much for us already. Please\x01",
            "feel free to visit anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01700FYeah, we'll give you a\x01",
            "warm welcome.\x02\x03",
            "#01704FAnd besides, it's more\x01",
            "fun watching Rixia's\x01",
            "training these days.\x02",
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

    def lambda_8381():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8381)
    Sleep(50)

    def lambda_8391():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8391)
    Sleep(50)

    def lambda_83A1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_83A1)
    Sleep(50)

    def lambda_83B1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_83B1)
    Sleep(50)

    def lambda_83C1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_83C1)
    Sleep(50)
    TurnDirection(0xA, 0x8, 500)

    ChrTalk(
        0x101,
        "#12P#00005FWow, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHaha. To be specific, it seems\x01",
            "like the jumps during her\x01",
            "performances are the highlights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FW-Wazy!\x02",
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
            "#5P#01709FHaha, there is that, of\x01",
            "course.\x02\x03",
            "#01704FLately, I feel there's a\x01",
            "sharpness even to her\x01",
            "ordinary movements.\x02\x03",
            "#01702FI never get the feeling she's\x01",
            "tired either. I guess she's\x01",
            "improved the way she rests?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#11P#01809FU-Umm, well, I guess.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)

    ChrTalk(
        0xA,
        (
            "#6P#04205FSo that's it, huh. I\x01",
            "never realized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FHaha. It looks like even\x01",
            "Ilya's perception is on\x01",
            "a whole other level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#01803F(Indeed. Because I haven't\x01",
            "been "working" recently, I've\x01",
            "had more time for rest.)\x02\x03",
            "#01808F(If Ilya can sense that just\x01",
            "from the way I move, she\x01",
            "really is amazing...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FHaha. You sure are a\x01",
            "hard worker, Rixia.\x02\x03",
            "Make sure you get proper\x01",
            "rest and take care of\x01",
            "yourself from now on.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_876B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_876B)
    Sleep(50)
    TurnDirection(0xA, 0x102, 500)

    ChrTalk(
        0x9,
        (
            "#5P#01802FI will. And thank you\x01",
            "for your concern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FBut, Arc-en-Ciel always\x01",
            "seems so busy...\x02\x03",
            "#00100FWe might stop by only so\x01",
            "often that it's not a\x01",
            "bother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01702FHaha. Rehearsals aren't\x01",
            "performances. Stop by\x01",
            "anytime.\x02\x03",
            "#01703FWell, it does look like\x01",
            "we'll be busy going\x01",
            "forward, though.\x02",
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
            "#5P#01709FHaha, it's still a s-e-\x01",
            "c-r-e-t㈱\x02\x03",
            "#01700FWell, look forward to\x01",
            "what we have planned,\x01",
            "anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FHaha, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FHaha, I'll have to check\x01",
            "up on that.\x02",
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

    # Function_27_6A60 end

    def Function_28_8A86(): pass

    label("Function_28_8A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 6)), scpexpr(EXPR_END)), "loc_8A93")
    Call(0, 29)
    Return()

    label("loc_8A93")

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
            "#11P#00100FThat's Sully's Star\x01",
            "Princess costume, right?\x02",
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
            "Doesn't she look\x01",
            "flustered?\x02",
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
            "#12206F*pant, pant, pant*...\x02\x03",
            "#12201FSay, Troupe Chief.\x01",
            "Wasn't that just\x01",
            "perfect?\x02\x03",
            "Ilya will have no choice\x01",
            "but to acknowledge me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6PHmm. You pass of course,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12206F*sigh*, that again?\x02\x03",
            "#12200FHey Rixia, what do you\x01",
            "think?\x02\x03",
            "#12202FWas there some mistake\x01",
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
            "I wonder if you can put\x01",
            "more emotions into it\x01",
            "next time.\x02\x03",
            "#06204FPicture "how you want it\x01",
            "to be"... I can't\x01",
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
            "#12201F"How I want it to be"...\x01",
            "What should I do,\x01",
            "specifically?\x02",
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
            "#6P#10300F(Hmm. Seems like we\x01",
            "should leave.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103F(Yeah... We can't\x01",
            "interrupt.)\x02",
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

    # Function_28_8A86 end

    def Function_29_8F77(): pass

    label("Function_29_8F77")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F(Rixia and Sully...\x01",
            "Looks like they're\x01",
            "focused on practice.)\x02\x03",
            "#00003F(We shouldn't interrupt\x01",
            "them now.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -62880, 0, 2950, 270)
    EventEnd(0x4)
    Return()

    # Function_29_8F77 end

    def Function_30_9004(): pass

    label("Function_30_9004")

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
        "#5P#01703F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FIlya... So this is where\x01",
            "you were.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x102, 500)

    ChrTalk(
        0x8,
        (
            "#5P#01705FAh, it's little bro and\x01",
            "friends.\x02\x03",
            "#01709FHaha. Did you come to\x01",
            "encourage us for the\x01",
            "renewal performance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FSomething like that.\x02\x03",
            "It looks like you're\x01",
            "training with Rixia and\x01",
            "Sully?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5P#01704FYes. I can get a good\x01",
            "view of the whole thing\x01",
            "from these 2F seats.\x02\x03",
            "#01702FAh, but even so, it's\x01",
            "good to see those young\x01",
            "kids doing their best.\x02\x03",
            "Seeing them like this\x01",
            "reminds me of when I was\x01",
            "a newbie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FWhen you were a newbie,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302FHaha, that's kind of\x01",
            "hard to imagine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FFeel free to tell us\x01",
            "about back then, if you\x01",
            "like.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)

    ChrTalk(
        0x8,
        (
            "#5P#01700FHaha. I don't particularly\x01",
            "mind, but... It's not that\x01",
            "interesting, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FWawa... Please, tell us about it!!\x02\x03",
            "#10100FIf I recall, all the magazines\x01",
            "were saying how great expectations\x01",
            "were for you when you debuted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00205FI see. So it was ever\x01",
            "since your debut.\x02\x03",
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
            "#01700FI think it was because I\x01",
            "saw Arc-en-Ciel\x01",
            "performances as a kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FI see, and you wanted to\x01",
            "emulate them─ is that\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01703FMmm, I think it wasn't that, exactly.\x02\x03",
            "#01700FAt that time, the productions were amazing\x01",
            "because of the artists' performances and\x01",
            "their elaborate sets, but...\x02\x03",
            "#01706FWhen they were over, I thought there was\x01",
            "something missing, and I couldn't accept\x01",
            "it.\x02",
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
            "#12P#00011FC-Couldn't accept it,\x01",
            "you say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01700FBut just about everyone in the neighborhood\x01",
            "said how amazing they were. I thought it\x01",
            "must be some kind of huge mistake, but...\x02\x03",
            "#01703FI mean, even I could put on a better\x01",
            "performance! That's what I thought.\x02\x03",
            "#01702FHaha. That was a weird thing to say because\x01",
            "I was a total amateur back then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FWow, so even as a kid\x01",
            "you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHmm, but because of that, rather\x01",
            "than knock on the door of Arc-\x01",
            "en-Ciel, you crashed into it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01706FMaybe I was because I interfered\x01",
            "with the practice of the newbies.\x01",
            "But yeah, that's about it.\x02\x03",
            "#01700FBut, I absolutely believed my\x01",
            "performances could be even\x01",
            "better.\x02\x03",
            "#01709FIf I just kept believing it,\x01",
            "everyone would come to understand\x01",
            "it eventually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FI see... And so that's\x01",
            "how you came to be who\x01",
            "you are now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01704FHaha. I can't say my\x01",
            "performances are perfect\x01",
            "yet, but it's close.\x02\x03",
            "#01702FBut, since the promising\x01",
            "raw materials called Rixia\x01",
            "and Sully came in...\x02\x03",
            "I was thinking of making\x01",
            "an ultimate performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FHaha. You're so greedy,\x01",
            "Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104FHaha. "There is no genius\x01",
            "that bests hard work"...\x02\x03",
            "#00109FAnd you're a genius at hard\x01",
            "work, Ilya. There's really no\x01",
            "one who can compete with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FYeah, you can say that\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01709FHaha. Looks like I told\x01",
            "you something boring.\x02\x03",
            "#01704FIf you like, come see\x01",
            "our renewal performance.\x02\x03",
            "#01700FRixia and Sully will be\x01",
            "in it... It'll be our\x01",
            "best performance yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FYes, of course.\x02\x03",
            "#00000FThe ultimate performance with\x01",
            "the three of you... I'll be\x01",
            "looking forward to it.\x02",
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

    # Function_30_9004 end

    def Function_31_9DFB(): pass

    label("Function_31_9DFB")

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

    def lambda_9F29():
        TurnDirection(0x8, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9F29)

    def lambda_9F36():
        TurnDirection(0x9, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9F36)
    TurnDirection(0xA, 0x0, 500)

    def lambda_9F4A():
        OP_95(0xFE, 700, 1450, 12200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F4A)

    def lambda_9F64():
        OP_95(0xFE, -700, 1450, 11760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9F64)

    def lambda_9F7E():
        OP_95(0xFE, 700, 1450, 10980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9F7E)

    def lambda_9F98():
        OP_95(0xFE, -700, 1450, 10680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9F98)

    def lambda_9FB2():
        OP_95(0xFE, 700, 1450, 9980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9FB2)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x8,
        (
            "#01705FMy, if it isn't little\x01",
            "bro.\x02",
        )
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
        "#01808F............\x02",
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
        "#00108FRixia...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        (
            "#01705FWhat's this now? Is there\x01",
            "something between you and\x01",
            "little bro, Rixia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01803F―No...\x02\x03",
            "#01801FMore importantly, Ilya,\x01",
            "there's not much time\x01",
            "until the performance.\x02\x03",
            "I want to check the\x01",
            "choreography of our duet\x01",
            "one last time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 500)

    ChrTalk(
        0xA,
        (
            "#04200FYeah, Ilya!\x02\x03",
            "I already have that part\x01",
            "down cold.\x02",
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
            "have anything important,\x01",
            "we're pretty busy.\x02\x03",
            "#01700FI can't let my concentration\x01",
            "be broken now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A286():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A286)
    TurnDirection(0x102, 0x8, 500)

    ChrTalk(
        0x101,
        "#00003FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FSorry to have bothered\x01",
            "you.\x02",
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

    # Function_31_9DFB end

    def Function_32_A31D(): pass

    label("Function_32_A31D")

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

    def lambda_A56D():
        OP_95(0xFE, -600, 2700, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A56D)

    def lambda_A587():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A587)
    Sleep(100)

    def lambda_A59B():
        OP_95(0xFE, 600, 2700, 900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A59B)

    def lambda_A5B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A5B5)
    Sleep(500)

    def lambda_A5C9():
        OP_95(0xFE, -750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A5C9)

    def lambda_A5E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A5E3)
    Sleep(100)
    OP_68(-1660, 3950, 2020, 4000)
    MoveCamera(33, 8, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(15070, 4000)

    def lambda_A625():
        OP_95(0xFE, 750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A625)

    def lambda_A63F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A63F)
    Sleep(500)

    def lambda_A653():
        OP_95(0xFE, -500, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_A653)

    def lambda_A66D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_A66D)
    Sleep(100)

    def lambda_A681():
        OP_95(0xFE, 770, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_A681)

    def lambda_A69B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_A69B)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00002FThis is...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A739")

    ChrTalk(
        0x10A,
        (
            "#12P#00602FThe "Golden Sun, Silver\x01",
            "Moon" additional scene,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A780")

    label("loc_A739")


    ChrTalk(
        0x109,
        (
            "#12P#10102FThe "Golden Sun, Silver\x01",
            "Moon" additional scene,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A780")


    ChrTalk(
        0x103,
        "#12P#00202FSully is amazing...\x02",
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

    def lambda_A876():
        OP_95(0xFE, -550, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A876)

    def lambda_A890():
        OP_95(0xFE, 620, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A890)

    def lambda_A8AA():
        OP_95(0xFE, -720, 1330, 8470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A8AA)

    def lambda_A8C4():
        OP_95(0xFE, 650, 1310, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A8C4)

    def lambda_A8DE():
        OP_95(0xFE, -570, 1350, 7280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_A8DE)

    def lambda_A8F8():
        OP_95(0xFE, 590, 1350, 7240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_A8F8)
    Sleep(1000)
    OP_4B(0xB, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0xB,
        "#5POh, it's you all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FTroupe Chief, it's been\x01",
            "a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FIt seems everyone is\x01",
            "concentrating on their\x01",
            "training.\x02",
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
            "#5PI heard Ilya has awoken... We\x01",
            "must do our best to live up\x01",
            "to her expectations as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FI see... So that's how\x01",
            "it is.\x02\x03",
            "#00008F(Come to think of it, no\x01",
            "one in the troupe knows\x01",
            "Rixia's location.)\x02\x03",
            "#00003F(I would have wanted to\x01",
            "show them her face,\x01",
            "but...)\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AC82")
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
    Jump("loc_AD10")

    label("loc_AC82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_AD10")
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

    label("loc_AD10")

    Sleep(1000)
    EventEnd(0x5)
    SetScenarioFlags(0x22, 2)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_32_A31D end

    def Function_33_AD22(): pass

    label("Function_33_AD22")

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

    def lambda_AF26():
        OP_95(0xFE, -550, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF26)

    def lambda_AF40():
        OP_95(0xFE, 620, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AF40)

    def lambda_AF5A():
        OP_95(0xFE, -720, 1330, 8470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AF5A)

    def lambda_AF74():
        OP_95(0xFE, 650, 1310, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AF74)

    def lambda_AF8E():
        OP_95(0xFE, -570, 1350, 7280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_AF8E)

    def lambda_AFA8():
        OP_95(0xFE, 590, 1350, 7240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_AFA8)
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
        "#5PIt's all of you, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PHow about it? Isn't\x01",
            "their drive just\x01",
            "amazing?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#11PFor now anyway, we're doing our\x01",
            "best to resume performances as\x01",
            "quickly as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PI heard Ilya has awoken... We\x01",
            "must do our best to live up\x01",
            "to her expectations as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F(No one in the troupe\x01",
            "knows Rixia's location.)\x02\x03",
            "#00008F(I would have wanted to\x01",
            "show them her face,\x01",
            "but...)\x02",
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

    # Function_33_AD22 end

    def Function_34_B1B7(): pass

    label("Function_34_B1B7")

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

    def lambda_B407():
        OP_95(0xFE, -600, 2700, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B407)

    def lambda_B421():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B421)
    Sleep(100)

    def lambda_B435():
        OP_95(0xFE, 600, 2700, 900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B435)

    def lambda_B44F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B44F)
    Sleep(500)

    def lambda_B463():
        OP_95(0xFE, -750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B463)

    def lambda_B47D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B47D)
    Sleep(100)
    OP_68(-1660, 3950, 2020, 4000)
    MoveCamera(33, 8, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(15070, 4000)

    def lambda_B4BF():
        OP_95(0xFE, 750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B4BF)

    def lambda_B4D9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B4D9)
    Sleep(500)

    def lambda_B4ED():
        OP_95(0xFE, -500, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_B4ED)

    def lambda_B507():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_B507)
    Sleep(100)

    def lambda_B51B():
        OP_95(0xFE, 770, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_B51B)

    def lambda_B535():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_B535)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6B7")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00000FThis is...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B5DD")

    ChrTalk(
        0x10A,
        (
            "#12P#00602FThe "Golden Sun, Silver\x01",
            "Moon" additional scene,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B68E")

    label("loc_B5DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B639")

    ChrTalk(
        0x109,
        (
            "#12P#10102FThe "Golden Sun, Silver\x01",
            "Moon" additional scene,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B68E")

    label("loc_B639")


    ChrTalk(
        0x105,
        (
            "#12P#10402FHaha, this is the "Golden\x01",
            "Sun, Silver Moon"\x01",
            "additional scene, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B68E")


    ChrTalk(
        0x103,
        "#12P#00202FSully is amazing...\x02",
    )

    CloseMessageWindow()
    Jump("loc_B716")

    label("loc_B6B7")


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

    label("loc_B716")

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

    def lambda_B7E8():
        OP_95(0xFE, -550, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B7E8)

    def lambda_B802():
        OP_95(0xFE, 620, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B802)

    def lambda_B81C():
        OP_95(0xFE, -720, 1330, 8470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B81C)

    def lambda_B836():
        OP_95(0xFE, 650, 1310, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B836)

    def lambda_B850():
        OP_95(0xFE, -570, 1350, 7280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_B850)

    def lambda_B86A():
        OP_95(0xFE, 590, 1350, 7240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_B86A)
    Sleep(1000)
    OP_4B(0xB, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8D1")

    ChrTalk(
        0xB,
        "#5POh, it's you all...\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8ED")

    label("loc_B8D1")


    ChrTalk(
        0xB,
        "#5PAh, it's you all...\x02",
    )

    CloseMessageWindow()

    label("loc_B8ED")

    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#5PRixia! If it isn't\x01",
            "Rixia!\x02",
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
        "#5P#N#12211FRixia...?\x02",
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

    def lambda_B9E7():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B9E7)
    Sleep(50)

    def lambda_B9F7():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B9F7)
    Sleep(50)

    def lambda_BA07():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_BA07)
    Sleep(50)

    def lambda_BA17():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_BA17)
    Sleep(50)

    def lambda_BA27():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_BA27)
    Sleep(50)

    def lambda_BA37():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_BA37)
    Sleep(50)

    def lambda_BA47():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_BA47)
    Sleep(50)

    def lambda_BA57():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_BA57)
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
        (
            "#5PIt's really you. It's\x01",
            "really Rixia!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PHaha. There's no\x01",
            "mistake, is there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P...There's no mistake.\x01",
            "It's really her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PHaha. With this, looks\x01",
            "like there's no need to\x01",
            "worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#12P#10717FEveryone...\x02\x03",
            "#10703F...Umm, I'm really\x01",
            "sorry.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BD6C")
    SetChrPos(0x10A, 680, 500, 11260, 0)
    Jump("loc_BDA3")

    label("loc_BD6C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BD92")
    SetChrPos(0x109, 680, 500, 11260, 0)
    Jump("loc_BDA3")

    label("loc_BD92")

    SetChrPos(0x105, 680, 500, 11260, 0)

    label("loc_BDA3")

    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#5PThat's right, you're\x01",
            "with the Support Section\x01",
            "right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#12P#10708FYes. I can't tell you\x01",
            "everything right now,\x01",
            "but...\x02\x03",
            "#10710FWhen the time comes, I\x01",
            "will take responsibility\x01",
            "for everything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PHaha. Oh, Rixia. Your\x01",
            "expression says you're holding\x01",
            "back a lot of emotion, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#12P#10712FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PThat's right. No one's\x01",
            "going to be happy with that\x01",
            "expression on your face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PYeah, seriously. And\x01",
            "you're such a beauty,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10718FPliｳ... Celine, Nikol...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PAnyway... Do what you\x01",
            "have to, and return to\x01",
            "us ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PSeriously. There's a\x01",
            "performance I want to\x01",
            "try with you, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10716FTheodore, Eugene...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PHaha. I'll get your\x01",
            "costume ready for you,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PAnd the set will be\x01",
            "ready too. You can be\x01",
            "sure of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10715FKarelia, Heintz...\x02",
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
        "#12208F...Rixia...\x02",
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
            "#12206FThis is... Arc-en-Ciel\x01",
            "is... the place where\x01",
            "you belong, Rixia.\x02\x03",
            "#12212FI don't know what kind\x01",
            "of burden you're\x01",
            "carrying, but...\x02\x03",
            "#12210FThis is the place that\x01",
            "Rixia... and Ilya and I\x01",
            "must return to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10718FSully...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12212FI... No matter what\x01",
            "happens, I'll protect this\x01",
            "place... So please...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#12P#10715FYeah... Yeah...\x02\x03",
            "#10716F...I understand how you\x01",
            "feel, Sully.\x02\x03",
            "#10716FI'll return... It's a\x01",
            "promise, so please don't\x01",
            "worry.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#12210FAlright. You promised,\x01",
            "Rixia.\x02\x03",
            "I've got a porcupinefish\x01",
            "for you if it's a lie,\x01",
            "you hear!\x02",
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
        "#11P#00002FRixia...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x106,
        (
            "#6P#10715F...Lloyd. We should be\x01",
            "going.\x02\x03",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C5C5")
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
    Jump("loc_C658")

    label("loc_C5C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C658")
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

    label("loc_C658")

    Sleep(1000)
    EventEnd(0x5)
    SetScenarioFlags(0x22, 2)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_34_B1B7 end

    def Function_35_C66A(): pass

    label("Function_35_C66A")

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
            "#11P#14000FY-Yeah... It's just a\x01",
            "little prayer.\x02\x03",
            "#14003FFor now, this is an\x01",
            "altar, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302FHaha, I see. But you\x01",
            "don't seem like the\x01",
            "praying type.\x02\x03",
            "#00305FSo, what could you be\x01",
            "praying for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FRandy! Don't ask so\x01",
            "directly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#14000FWell it's fine, right?\x02\x03",
            "#14003FOf course it's for\x01",
            "Ilya...\x02\x03",
            "But it's for all of you\x01",
            "as well.\x02",
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
            "#14001F...I don't know the\x01",
            "details, but you guys are\x01",
            "going after KeA, right?\x02\x03",
            "And, you guys are going\x01",
            "somewhere dangerous right\x01",
            "after this.\x02\x03",
            "#14003F............\x02\x03",
            "#14002FThat's why I'm praying\x01",
            "for your safety. For\x01",
            "Rixia too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CAD7")

    ChrTalk(
        0x106,
        "#6P#10702FSully... Haha, thanks.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CB52")

    label("loc_CAD7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CB16")

    ChrTalk(
        0x109,
        (
            "#6P#10102FI see... Thank you,\x01",
            "Sully.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CB52")

    label("loc_CB16")


    ChrTalk(
        0x105,
        (
            "#6P#10302FHaha, I see... So you\x01",
            "can be nice sometimes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB52")


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
            "#11P#14012FA-Anyway... KeA is a\x01",
            "precious friend to me,\x01",
            "you see.\x02\x03",
            "#14001FDefinitely bring her\x01",
            "back for me, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYeah, of course!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6F), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CFC9")

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
            "#6P#00000FFor us... What ever\x01",
            "could it be?\x02",
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
            "Sully took off her cap\x01",
            "and handed it to Lloyd.\x07\x00\x02",
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
            "#04208FI understand I can't do\x01",
            "that.\x02\x03",
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
            "#6P#00202FYes. We'll take\x01",
            "responsibility for it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF59")

    ChrTalk(
        0xA,
        (
            "#11P#04212FI-I see... Well good\x01",
            "then.\x02\x03",
            "#04202FPlease be careful, Rixia\x01",
            "and everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#6P#10709FYeah, understood.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_CFC9")

    label("loc_CF59")


    ChrTalk(
        0xA,
        (
            "#11P#04212FI-I see... Well good\x01",
            "then.\x02\x03",
            "#04202FWell then, be careful,\x01",
            "ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYeah, understood.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_CFC9")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D024")
    OP_E0(0x34, 0x0)

    label("loc_D024")

    EventEnd(0x5)
    Return()

    # Function_35_C66A end

    def Function_36_D027(): pass

    label("Function_36_D027")

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
            "#6P#00000FHello, Nikol.\x02\x03",
            "We'd like to ask you a\x01",
            "little something.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained the professor's\x01",
            "request and that they were here to\x01",
            "collect the medical questionnaire.\x02",
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
            "Hang on a second. I'll\x01",
            "go grab it.\x02",
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
            "#6P#00102FHaha. If you you're doing this well,\x01",
            "then it looks like you're no longer\x01",
            "under the influence of that drug.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Yeah, I received proper\x01",
            "treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I wonder why I even started\x01",
            "taking a medicine like that\x01",
            "in the first place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Though I did want to do\x01",
            "something about my lack\x01",
            "of ability.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FThe drug slid right into\x01",
            "that gap in your heart,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FWell, as long as you're\x01",
            "aware of it, we've got to\x01",
            "nothin' to worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Right... I plan to\x01",
            "dedicate myself to Arc-\x01",
            "en-Ciel more than ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FI'm looking forward to\x01",
            "seeing the show!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x152, 4)
    OP_29(0x70, 0x1, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5D2")

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this, we've\x01",
            "collected all the\x01",
            "questionnaires.\x02\x03",
            "Let's deliver them to\x01",
            "Professor Seiland\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x70, 0x1, 0x5)

    label("loc_D5D2")

    OP_93(0xF, 0x5A, 0x0)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 65000, 0, 3000, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_36_D027 end

    def Function_37_D604(): pass

    label("Function_37_D604")

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
        (
            "#11P#00000FI wonder if Mary's\x01",
            "here...\x02",
        )
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
        (
            "#11P#04600FHaha, found her right\x01",
            "away.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A3, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00000FAlright, leave this to\x01",
            "me.\x02",
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

    def lambda_D802():
        OP_95(0xFE, 8590, 15200, -7600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D802)
    Sleep(50)

    def lambda_D81F():
        TurnDirection(0xFE, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_D81F)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#00002FC'mon Mary. It's ok.\x02",
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

    def lambda_D9D3():
        OP_95(0xFE, 13800, 15200, -8010, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_D9D3)
    Sleep(1000)

    def lambda_D9F0():
        TurnDirection(0xFE, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D9F0)
    Sleep(50)

    def lambda_DA00():

        label("loc_DA00")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_DA00")

    QueueWorkItem2(0x1A3, 1, lambda_DA00)
    Sleep(1000)

    def lambda_DA15():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_DA15)
    WaitChrThread(0x13, 1)
    SetChrFlags(0x13, 0x80)
    OP_6F(0x1)
    EndChrThread(0x1A3, 0x1)

    ChrTalk(
        0x1A3,
        "#04605FWhoa!\x02",
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
            "#04606FHmm, I wonder if you've\x01",
            "been keeping up with\x01",
            "your training?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x14, 1770, 15200, -7960, 90)
    SetChrPos(0x15, 1770, 15200, -9370, 90)
    OP_68(6830, 16850, -8570, 4000)
    MoveCamera(46, 28, 0, 4000)
    OP_6E(500, 4000)
    SetCameraDistance(16250, 4000)

    def lambda_DB1F():
        OP_95(0xFE, 6590, 15200, -7960, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_DB1F)
    Sleep(50)

    def lambda_DB3C():
        OP_95(0xFE, 6590, 15200, -9370, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_DB3C)
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

    def lambda_DBCA():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DBCA)
    Sleep(50)

    def lambda_DBDA():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_DBDA)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00004FNo, it's because I'm not\x01",
            "a good closer.\x02\x03",
            "#00000FAnyway, let's go after\x01",
            "her.\x02\x03",
            "Just in case, you guys\x01",
            "head for the opposite\x01",
            "entrance.\x02",
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
            "#04609FHaha. Alright then,\x01",
            "after her!\x02",
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

    # Function_37_D604 end

    def Function_38_DD0B(): pass

    label("Function_38_DD0B")


    def lambda_DD10():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DD10)

    def lambda_DD21():
        OP_95(0xFE, 11590, 15200, -7990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DD21)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 10260, 15200, -7100, 2000, 0x0)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_38_DD0B end

    def Function_39_DD56(): pass

    label("Function_39_DD56")


    def lambda_DD5B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_DD5B)

    def lambda_DD6C():
        OP_95(0xFE, 11590, 15200, -7990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_DD6C)
    WaitChrThread(0x1A3, 1)
    OP_95(0x1A3, 10260, 15200, -9100, 2000, 0x0)
    OP_93(0x1A3, 0x10E, 0x1F4)
    Return()

    # Function_39_DD56 end

    def Function_40_DDA1(): pass

    label("Function_40_DDA1")


    def lambda_DDA6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_DDA6)

    def lambda_DDB7():
        OP_95(0xFE, -8770, 15200, -8150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_DDB7)
    WaitChrThread(0x14, 1)
    OP_93(0x14, 0x5A, 0x1F4)
    Return()

    # Function_40_DDA1 end

    def Function_41_DDD8(): pass

    label("Function_41_DDD8")


    def lambda_DDDD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_DDDD)

    def lambda_DDEE():
        OP_95(0xFE, -11190, 15200, -8100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_DDEE)
    WaitChrThread(0x15, 1)
    OP_95(0x15, -10100, 15200, -9070, 2000, 0x0)
    OP_93(0x15, 0x5A, 0x1F4)
    Return()

    # Function_41_DDD8 end

    def Function_42_DE23(): pass

    label("Function_42_DE23")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's hurry and chase\x01",
            "Mary. She should still\x01",
            "be close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04609FHaha, we're not going to\x01",
            "let her get away this\x01",
            "time!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -11130, 15200, -7980, 90)
    EventEnd(0x4)
    Return()

    # Function_42_DE23 end

    def Function_43_DEBD(): pass

    label("Function_43_DEBD")

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

    def lambda_E083():
        OP_95(0xFE, 110, 1250, 20620, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_E083)
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

    def lambda_E199():
        OP_98(0xFE, 0x0, 0x2710, 0x0, 0x96, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_E199)
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
        "#00011F#10AWha!?\x02",
    )

    Sleep(1500)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#06205F#10AThis is bad! Not the\x01",
            "props!\x02\x03",
            "#10ABut, just who!?\x02",
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
        "#11P#04611F#10AHaha! This is nothing!\x02",
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
        "#12P#00005FHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#06205FA-Amazing!\x02",
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

    def lambda_E594():
        OP_98(0xFE, 0x0, 0x1770, 0x0, 0x96, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_E594)

    ChrTalk(
        0x13,
        "#6PMeow!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#11P#04606FHmm? It's not like I'm\x01",
            "gonna eat you.\x02\x03",
            "Settle down already.\x02\x03",
            "#04602FHere, how do you like\x01",
            "this♪\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Shirley tickled Mary.\x02",
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
        "#6PMeow, meow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#11P#04609FHaha, not too bad, eh?\x02\x03",
            "#04600FAlright... Then how\x01",
            "about this㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A3, 0x0, 1200, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x13,
        "#6PMeoow!!\x02",
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
        "#6PPurr, purr... meow㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#11P#04609FAhaha, have you calmed\x01",
            "down a bit?\x02",
        )
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
        (
            "#12P#00000FHaha, you're very good\x01",
            "at that.\x02",
        )
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
            "#12P#06205FThat's right, I need to\x01",
            "see who touched the\x01",
            "equipment...\x02",
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
            "#11P#04600FAlright then, let's get\x01",
            "down together.\x02\x03",
            "No more funny business,\x01",
            "you hear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#6PMeoow♪\x02",
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
        (
            "#11P#04605FWhat's this all of a\x01",
            "sudden... Ah.\x02",
        )
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

    def lambda_EAA5():
        OP_9D(0xFE, 0x212, 0x2328, 0x4268, 0x7D0, 0x64)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_EAA5)
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
        "#00011FThis is bad!\x02",
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

    def lambda_EBF0():
        OP_9D(0xFE, 0x6D6, 0x1F40, 0x4A38, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_EBF0)
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
            "#00000FPhew... Looks like you\x01",
            "got her somehow.\x02",
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

    # Function_43_DEBD end

    def Function_44_ED40(): pass

    label("Function_44_ED40")


    def lambda_ED45():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_ED45)

    def lambda_ED56():
        OP_95(0xFE, 0, 2250, 2940, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ED56)
    WaitChrThread(0x101, 1)
    Return()

    # Function_44_ED40 end

    def Function_45_ED70(): pass

    label("Function_45_ED70")


    def lambda_ED75():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_ED75)

    def lambda_ED86():
        OP_95(0xFE, 0, 1800, 5200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_ED86)
    WaitChrThread(0x1A3, 1)
    Return()

    # Function_45_ED70 end

    def Function_46_EDA0(): pass

    label("Function_46_EDA0")


    def lambda_EDA5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_EDA5)

    def lambda_EDB6():
        OP_95(0xFE, 0, 1350, 7460, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_EDB6)
    WaitChrThread(0x9, 1)
    Return()

    # Function_46_EDA0 end

    def Function_47_EDD0(): pass

    label("Function_47_EDD0")

    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x1)
    Sound(250, 0, 60, 0)
    OP_9D(0x9, 0x0, 0x4E2, 0x4BFA, 0xBB8, 0x1388)
    SetChrSubChip(0x9, 0x0)
    SetScenarioFlags(0x1, 4)
    Sound(637, 0, 100, 0)
    Sound(844, 0, 100, 0)
    BeginChrThread(0x9, 0, 0, 48)

    def lambda_EE13():
        OP_9D(0xFE, 0x1086, 0x4E2, 0x517C, 0x1388, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_EE13)
    OP_A1(0x9, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0x9, 1)
    Sound(326, 0, 50, 0)
    Return()

    # Function_47_EDD0 end

    def Function_48_EE3F(): pass

    label("Function_48_EE3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_EE5B")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_48_EE3F")

    label("loc_EE5B")

    Return()

    # Function_48_EE3F end

    def Function_49_EE5C(): pass

    label("Function_49_EE5C")

    SetChrPos(0xA, 0, 1250, 25500, 270)

    label("loc_EE6D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F241")
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    SetChrFlags(0xA, 0x1020)
    BeginChrThread(0xA, 1, 0, 51)

    def lambda_EE9E():
        OP_93(0xA, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EE9E)
    Sound(809, 0, 30, 0)
    OP_9D(0xA, 0x0, 0x4E2, 0x59D8, 0xBB8, 0x44C)
    Sound(50, 0, 70, 0)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    Sleep(200)

    def lambda_EED9():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0xA96, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EED9)
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

    def lambda_EF5F():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1068, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EF5F)
    Sleep(250)

    def lambda_EF7D():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1450, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EF7D)
    Sleep(250)

    def lambda_EF9B():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1838, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EF9B)
    Sleep(250)

    def lambda_EFB9():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EFB9)
    OP_49()
    SetChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x3B)
    SetChrSubChip(0xA, 0x2)
    BeginChrThread(0xA, 1, 0, 54)
    Sleep(1000)

    def lambda_EFEB():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1C20, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EFEB)
    OP_49()
    Sound(844, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    Sound(50, 0, 50, 0)
    EndChrThread(0xA, 0x2)
    Sound(809, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x578)
    Sound(50, 0, 50, 0)

    def lambda_F051():
        OP_9E(0xA, 0x0, 0x636A, 0xFFF24460, 0x2A94, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F051)
    OP_49()
    Sound(844, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x514)
    Sound(50, 0, 50, 0)

    def lambda_F090():
        OP_93(0xA, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F090)
    BeginChrThread(0xA, 1, 0, 51)
    Sound(809, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x578)
    Sound(50, 0, 50, 0)
    BeginChrThread(0xA, 1, 0, 51)

    def lambda_F0CC():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1838, 0x2)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F0CC)
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

    def lambda_F1E2():
        OP_93(0xA, 0x5A, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F1E2)
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
    Jump("loc_EE6D")

    label("loc_F241")

    Return()

    # Function_49_EE5C end

    def Function_50_F242(): pass

    label("Function_50_F242")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_50_F242 end

    def Function_51_F266(): pass

    label("Function_51_F266")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0x7D0, 0x3, 0x0, 0x1, 0x2)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_51_F266 end

    def Function_52_F28A(): pass

    label("Function_52_F28A")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0x9C4, 0x2, 0x0, 0x1)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_52_F28A end

    def Function_53_F29F(): pass

    label("Function_53_F29F")

    SetChrChipByIndex(0xFE, 0x3B)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_53_F29F end

    def Function_54_F2AD(): pass

    label("Function_54_F2AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F2CB")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    Jump("Function_54_F2AD")

    label("loc_F2CB")

    Return()

    # Function_54_F2AD end

    def Function_55_F2CC(): pass

    label("Function_55_F2CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F2EA")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(60)
    Jump("Function_55_F2CC")

    label("loc_F2EA")

    Return()

    # Function_55_F2CC end

    def Function_56_F2EB(): pass

    label("Function_56_F2EB")

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
            "#00000FLooks like she's really\x01",
            "going at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. It's just as the\x01",
            "manager said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FJust look at her. She's\x01",
            "amazing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FSo that's that new scene\x01",
            "she's practicin', huh.\x02\x03",
            "#00304FThey said it was a\x01",
            "pretty important role,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FThe "Star Princess",\x01",
            "right?\x02\x03",
            "I heard she has a big\x01",
            "scene in the second\x01",
            "half.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHaha, looks like she's\x01",
            "ready for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, but the pressure\x01",
            "must be incredible...\x02\x03",
            "#00000FLet's excuse ourselves\x01",
            "before we get in her\x01",
            "way.\x02",
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
        (
            "#00200FLooks like we were\x01",
            "noticed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FD-Damn. We've got to at\x01",
            "least say hello.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F7C4():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F7C4)
    Sleep(50)

    def lambda_F7E1():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F7E1)
    Sleep(50)

    def lambda_F7FE():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F7FE)
    Sleep(50)

    def lambda_F81B():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F81B)
    Sleep(50)

    def lambda_F838():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F838)
    Sleep(50)

    def lambda_F855():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F855)
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
        "#00000FHey, Sully.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12203FH-Hmph, whatever...\x02\x03",
            "#12200FSo, did you need\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FNo. We were passing by\x01",
            "and just wanted to see\x01",
            "what you were up to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah. Sorry for\x01",
            "interrupting you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12206FWell I was thinking of\x01",
            "taking a break anyway.\x01",
            "It's fine, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FBut, this is the first\x01",
            "time I've seen you\x01",
            "perform...\x02\x03",
            "#00202FYou've already mastered\x01",
            "it. No one would think\x01",
            "you're a beginner.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#12205FR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FYes, really. Honestly,\x01",
            "I'm surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah. It like you're not\x01",
            "wasting a single\x01",
            "movement.\x02\x03",
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
            "#10109FYeah, yeah. And that\x01",
            "costume looks really\x01",
            "good on you.\x02",
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

    def lambda_FCD3():

        label("loc_FCD3")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_FCD3")

    QueueWorkItem2(0x102, 0, lambda_FCD3)

    def lambda_FCE5():

        label("loc_FCE5")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_FCE5")

    QueueWorkItem2(0x103, 0, lambda_FCE5)
    OP_99(0xA, 0x101, 0x3E8, 0x7D0, 0x0)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)

    ChrTalk(
        0xA,
        (
            "#12203F...Hey, you.\x02\x03",
            "#12200FWant to join me for\x01",
            "performance training?\x02\x03",
            "#12208FHow to say this...\x01",
            "There's something I want\x01",
            "your opinion on.\x02",
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
            "#00105FYou want Lloyd to join\x01",
            "your training?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FW-Why me? What could this\x01",
            "be about?\x02\x03",
            "#00003FI'm just a layman. I\x01",
            "don't know anything about\x01",
            "the performing arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12203FI'm telling you, it's\x01",
            "nothing too difficult.\x02\x03",
            "#12208FIt's just something I\x01",
            "was thinking of, see?\x02\x03",
            "#12200FSo how 'bout it? Are you\x01",
            "joining me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FR-Right...\x02",
    )

    CloseMessageWindow()
    Call(0, 57)
    Return()

    # Function_56_F2EB end

    def Function_57_FF9D(): pass

    label("Function_57_FF9D")

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
            "Join Sully's training\x01",      # 0
            "Refuse\x01",                     # 1
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
        (0, "loc_1000A"),
        (1, "loc_100EE"),
        (SWITCH_DEFAULT, "loc_10266"),
    )


    label("loc_1000A")


    ChrTalk(
        0x101,
        (
            "#00000FSure, if you're okay\x01",
            "with me, that is.\x02\x03",
            "Are you sure it's no big\x01",
            "deal?\x02",
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
            "Quest [Secret Acting\x01",
            "Coach]\x07\x00",
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
    Jump("loc_10266")

    label("loc_100EE")


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
            "...Forget it.\x02\x03",
            "#12208FThen, I'll keep\x01",
            "practicing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FR-Right...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#00100F(Hey Lloyd. Can we spare\x01",
            "the time somehow?)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#00003F(R-Right... Let me\x01",
            "rethink this.)\x02",
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
    Jump("loc_10266")

    label("loc_10266")

    Return()

    # Function_57_FF9D end

    def Function_58_10267(): pass

    label("Function_58_10267")

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
            "#12205FWhat, don't you have\x01",
            "stuff to do?\x02\x03",
            "#12200FCould you possibly...\x01",
            "want to join my\x01",
            "practice?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 57)
    Return()

    # Function_58_10267 end

    SaveToFile()

Try(main)
