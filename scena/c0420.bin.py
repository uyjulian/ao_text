from ScenarioHelper import *

def main():
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
        "Ilia",                 # 1
        "Lisha",               # 2
        "Shuri",                 # 3
        "Aban Theater Company Manager",           # 4
        "Heinz",               # 5
        "Eugene",             # 6
        "Theodore",             # 7
        "Nicole",                 # 8
        "Priure",                 # 9
        "Celine",               # 10
        "Karelia",               # 11
        "Mary",                 # 12
        "Erie",                 # 13
        "Waji",                   # 14
        "chandelier",           # 15
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
        "Function_7_149F",         # 07, 7
        "Function_8_18A5",         # 08, 8
        "Function_9_287B",         # 09, 9
        "Function_10_2F14",        # 0A, 10
        "Function_11_2F85",        # 0B, 11
        "Function_12_34EB",        # 0C, 12
        "Function_13_3FFA",        # 0D, 13
        "Function_14_40FE",        # 0E, 14
        "Function_15_42A8",        # 0F, 15
        "Function_16_44B6",        # 10, 16
        "Function_17_4A9E",        # 11, 17
        "Function_18_5846",        # 12, 18
        "Function_19_5C3A",        # 13, 19
        "Function_20_5CE4",        # 14, 20
        "Function_21_5F98",        # 15, 21
        "Function_22_635F",        # 16, 22
        "Function_23_63B6",        # 17, 23
        "Function_24_659B",        # 18, 24
        "Function_25_6776",        # 19, 25
        "Function_26_677D",        # 1A, 26
        "Function_27_67A3",        # 1B, 27
        "Function_28_8909",        # 1C, 28
        "Function_29_8E6A",        # 1D, 29
        "Function_30_8EF9",        # 1E, 30
        "Function_31_9C83",        # 1F, 31
        "Function_32_A1D8",        # 20, 32
        "Function_33_ABAF",        # 21, 33
        "Function_34_B029",        # 22, 34
        "Function_35_C4C5",        # 23, 35
        "Function_36_CF52",        # 24, 36
        "Function_37_D4BE",        # 25, 37
        "Function_38_DBE7",        # 26, 38
        "Function_39_DC32",        # 27, 39
        "Function_40_DC7D",        # 28, 40
        "Function_41_DCB4",        # 29, 41
        "Function_42_DCFF",        # 2A, 42
        "Function_43_DD93",        # 2B, 43
        "Function_44_EC51",        # 2C, 44
        "Function_45_EC81",        # 2D, 45
        "Function_46_ECB1",        # 2E, 46
        "Function_47_ECE1",        # 2F, 47
        "Function_48_ED50",        # 30, 48
        "Function_49_ED6D",        # 31, 49
        "Function_50_F153",        # 32, 50
        "Function_51_F177",        # 33, 51
        "Function_52_F19B",        # 34, 52
        "Function_53_F1B0",        # 35, 53
        "Function_54_F1BE",        # 36, 54
        "Function_55_F1DD",        # 37, 55
        "Function_56_F1FC",        # 38, 56
        "Function_57_FECA",        # 39, 57
        "Function_58_101BF",       # 3A, 58
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_102A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F3E")

    ChrTalk(
        0xFE,
        "How about you, is it such a wonderful anxiety?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone is now anyway,\x01",
            "To resume the performance as soon as possible\x01",
            "I'm doing my best with all my strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Iria also has eyes\x01",
            "I heard that he awoke … …\x01",
            "To meet her expectations as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(… … everyone in the theater company\x01",
            "Even Lisher's way\x01",
            "I do not know it. )\x02\x03",
            "(Even face alone\x01",
            "I want to show it, but … …)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1025")

    label("loc_F3E")


    ChrTalk(
        0xFE,
        (
            "As usual\x01",
            "While refining the stage here\x01",
            "I will keep you waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lloyd guys,\x01",
            "About Lisa's\x01",
            "I asked for your best regards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, I understand.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1025")

    ChrTalk(
        0x106,
        (
            "#10700FTheater company manager ……\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1025")

    Jump("loc_149B")

    label("loc_102A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_10AE")

    ChrTalk(
        0xFE,
        (
            "Everyone, really\x01",
            "I am doing my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Iria, and Lisha … …\x01",
            "We are waiting for you guys.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_149B")

    label("loc_10AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_12BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1249")
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xB,
        "Oh, Lloyd or something ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FTheater company manager ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Oh … sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Thinking a lot, everything\x01",
            "You have become uneasy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It is about that Iria.\x01",
            "When you surely wake up\x01",
            "I believe it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FTheater company manager ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, but not least\x01",
            "I can not keep it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Me too … a bit more,\x01",
            "You have to be shy.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x18D, 0)
    Jump("loc_12B7")

    label("loc_1249")


    ChrTalk(
        0xFE,
        (
            "Well, I 'm almost done.\x01",
            "I have to be shy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Forever this way,\x01",
            "Ilia will get angry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B7")

    Jump("loc_149B")

    label("loc_12BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1334")

    ChrTalk(
        0xFE,
        "Sorry, Lloyd guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not have time to go.\x01",
            "Everyone until the end\x01",
            "I want to prepare.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_149B")

    label("loc_1334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1342")
    Jump("loc_149B")

    label("loc_1342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1350")
    Jump("loc_149B")

    label("loc_1350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_135E")
    Jump("loc_149B")

    label("loc_135E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_136C")
    Jump("loc_149B")

    label("loc_136C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_137A")
    Jump("loc_149B")

    label("loc_137A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1388")
    Jump("loc_149B")

    label("loc_1388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1414")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A3")
    Call(0, 8)
    Jump("loc_140F")

    label("loc_13A3")


    ChrTalk(
        0xFE,
        (
            "Indeed,\x01",
            "Iria is really reliable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this situation, the stage for tomorrow too\x01",
            "It will surely make you succeed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_140F")

    Jump("loc_149B")

    label("loc_1414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1422")
    Jump("loc_149B")

    label("loc_1422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_149B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_143D")
    Call(0, 7)
    Jump("loc_149B")

    label("loc_143D")


    ChrTalk(
        0xFE,
        (
            "It seems to be impossible,\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is also the idea of you\x01",
            "Because it is for realization.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_149B")

    TalkEnd(0xFE)
    Return()

    # Function_6_DDB end

    def Function_7_149F(): pass

    label("Function_7_149F")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175D")

    ChrTalk(
        0xB,
        (
            "So, Heinz.\x01",
            "Is it technically possible?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I agree,\x01",
            "Of course I will try … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1596")

    ChrTalk(
        0xB,
        "Oh, you guys at the Special Affairs Support Division.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Perhaps,\x01",
            "Were there any incidents too?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1628")

    label("loc_1596")


    ChrTalk(
        0xB,
        "Oh you guys\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 0)

    ChrTalk(
        0xB,
        (
            "Oh, you are the Special Support Section\x01",
            "You are Lloyd, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Perhaps,\x01",
            "Were there any incidents too?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1628")


    ChrTalk(
        0x101,
        (
            "#00000FNo, now I am going to\x01",
            "Where are you going around?\x02\x03",
            "Just to be sure, also to this person\x01",
            "It was up to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmm, was that so?\x01",
            "If you guys patrol\x01",
            "This will be helpful too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, if there is something again\x01",
            "Will you feel free to call out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, thank you.\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x10E, 0x0)
    OP_93(0xC, 0x5A, 0x0)
    SetScenarioFlags(0x136, 4)
    Jump("loc_189C")

    label("loc_175D")


    ChrTalk(
        0xC,
        "Is it okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Increasing the speed,\x01",
            "The timing to adjust so much\x01",
            "It will be severe … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, that is\x01",
            "Iria knows well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To anything in this conception\x01",
            "Tempo up of the whole scene\x01",
            "It seems indispensable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Until the boundary limit,\x01",
            "It seems I want to try it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Is that so……\x01",
            "Anyway, let's see.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x1, 3)

    label("loc_189C")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_7_149F end

    def Function_8_18A5(): pass

    label("Function_8_18A5")

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
        "Gee\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#06105FOh it's little bro!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FThank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06202FHello everyone.\x02\x03",
            "#06209FHuhu, Randy also\x01",
            "It was finally restored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FOh, it is Lisa-chan.\x01",
            "It is nice to care.\x02\x03",
            "#00309FNo, but, even if it is, Iria\x01",
            "Lisa's costumes … …\x02\x03",
            "Even if I look at it many times it is Isis\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#06102FHehu, thanks a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06204FOh, once again said\x01",
            "It's a bit embarrassing though ….\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x104, 500)

    ChrTalk(
        0x105,
        (
            "#6P#10304FHuff, certainly Randy's\x01",
            "The line of sight is irresistible.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#11P#00301FWhat is it, Wadi.\x01",
            "I am a pure feeling -\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    ChrTalk(
        0x102,
        (
            "#11P#00106FYeah yeah, I know.\x01",
            "I wonder if that will be enough.\x02",
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

    def lambda_1C70():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1C70)
    Sleep(50)

    def lambda_1C80():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1C80)
    Sleep(50)

    def lambda_1C90():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1C90)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x109,
        "#12P#10109FOh, haha ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FSorry to be noisy.\x02\x03",
            "#00000FBy the way, now\x01",
            "I was practicing, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06100FWell.\x01",
            "Towards the stage of tomorrow night\x01",
            "I adjusted it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        (
            "#06202FHuhu, tomorrow is\x01",
            "Customers only for customers\x01",
            "I am nervous, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, people from various countries\x01",
            "It will not come to the theater.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FThe leaders …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FSpeaking of which, even at the countermeeting meeting this morning\x01",
            "It was on the agenda.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuh, whatever it takes\x01",
            "Invite them to crossbell.\x02\x03",
            "#10304FThe stage of the alkane shell\x01",
            "It will be the best honor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FWell, considering that,\x01",
            "Is there a good taste there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FBut it certainly gets nervous, is not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06203FYes, other members of the group\x01",
            "Somewhere I feel uneasy … …\x02\x03",
            "#06209FEven so, Iria\x01",
            "It does not change as usual.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        (
            "#06103FWell, because every one\x01",
            "There is no use in mind even if it is worrisome.\x02\x03",
            "#06100FWho seems to be sitting in the audience seats,\x01",
            "I just do my best.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x8, 500)

    ChrTalk(
        0xB,
        (
            "#11PYou at all … …\x01",
            "It is reliable enough to always be amazed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PIt is called the idea of this renewal performance,\x01",
            "I admire that energy every time.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FRenewal performance ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100Fby the way……\x01",
            "Next time \"gold sun, silver moon\"\x01",
            "It was renewed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FOh, already in the world\x01",
            "It is an exclusive rumor.\x02\x03",
            "Anything but a bold arrangement\x01",
            "I heard that it will be added?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_21F5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_21F5)
    Sleep(50)
    OP_93(0xB, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#06109FYeah, that's right.\x02\x03",
            "#06104FOnce it's done to adjust the completed one\x01",
            "In a sense, it was a challenge, but ….\x02\x03",
            "#06100FFrom the viewpoint of screenplay and production\x01",
            "It is likely to raise the perfection\x01",
            "Finally come with a prospect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06202FYes, and this next performance\x01",
            "When I finish, about 1 month for that special training\x01",
            "I'm planning to concentrate.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 2)), scpexpr(EXPR_END)), "loc_2429")

    ChrTalk(
        0x101,
        (
            "#12P#00000FIndeed, when we met before\x01",
            "It was said that \"I'm going to be busy\"\x01",
            "It was this thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#06100FHuh, that kind of thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#12P#10100FHowever, it is a special training for one month … …\x01",
            "Even though it is said to be an arrangement\x01",
            "It seems that there is power.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_247A")

    label("loc_2429")


    ChrTalk(
        0x109,
        (
            "#12P#10100FI see……\x01",
            "Even though it is said to be an arrangement\x01",
            "It seems that there is power.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_247A")


    ChrTalk(
        0x104,
        (
            "#12P#00300F\"Golden Sun, Silver Moon\"\x01",
            "In the stage of the alkane shell\x01",
            "Especially it is reputation that the degree of completion is high … …\x02\x03",
            "#00304FTo make that even better,\x01",
            "I can not imagine what kind of substitute it would be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FOh, it is true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06100FHuhu, beyond deciding to live on the stage,\x01",
            "You must always ask for the best one.\x02\x03",
            "#06104FTo visitors who come to see\x01",
            "I hope you have the best time,\x01",
            "To make a wonderful setting ……\x02\x03",
            "#06100FThat is Alcan shell,\x01",
            "And our artists\x01",
            "It's the biggest mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FBeyond the stage\x01",
            "Does not that there is anyone who goes to the right …?\x01",
            "Is not Iria sushin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FWell, renewal performance is\x01",
            "It has become amazingly fun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#06100FHuff, because the official announcement is in the vicinity\x01",
            "Please wait.\x02\x03",
            "Even those who watched the previous performances,\x01",
            "You should be able to have fun.\x02\x03",
            "#06104FI was a little bit cautious about it\x01",
            "I also have surprises ……\x01",
            "I'm sure you will be surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FIs it a surprise … ….\x01",
            "Haha, well then\x01",
            "I am looking forward to it.\x02",
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

    # Function_8_18A5 end

    def Function_9_287B(): pass

    label("Function_9_287B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_288C")
    Jump("loc_2F10")

    label("loc_288C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_289A")
    Jump("loc_2F10")

    label("loc_289A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2971")
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x8,
        (
            "#01700FThen from now, the two princess'\x01",
            "Following \"Princess of the month\" appears\x01",
            "I'll check the scene.\x02\x03",
            "Lisha, Shuri, are you ready?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01800FYes, please!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#04200FThis one is OK too!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    Jump("loc_2F10")

    label("loc_2971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2982")
    Call(0, 10)
    Jump("loc_2F10")

    label("loc_2982")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2990")
    Jump("loc_2F10")

    label("loc_2990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_299E")
    Jump("loc_2F10")

    label("loc_299E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2B3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B9")
    Call(0, 30)
    Jump("loc_2B38")

    label("loc_29B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AA6")

    ChrTalk(
        0x8,
        (
            "#01709FHehe, old things\x01",
            "I remembered for a long time.\x02\x03",
            "#01700FWell, if you like\x01",
            "Also this renewal performance\x01",
            "Please come and see.\x02\x03",
            "I am working hard over there\x01",
            "There are Lisha and Shri,\x01",
            "Because it surely will be a wonderful stage.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B38")

    label("loc_2AA6")


    ChrTalk(
        0x8,
        (
            "#01700FAlso this renewal performance\x01",
            "Please come and see.\x02\x03",
            "I am working hard over there\x01",
            "There are Lisha and Shri,\x01",
            "Because it surely will be a wonderful stage.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B38")

    Jump("loc_2F10")

    label("loc_2B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2B4B")
    Jump("loc_2F10")

    label("loc_2B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2B59")
    Jump("loc_2F10")

    label("loc_2B59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2D42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B74")
    Call(0, 8)
    Jump("loc_2D3D")

    label("loc_2B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C96")

    ChrTalk(
        0x8,
        (
            "#06100FBeyond deciding to live on the stage,\x01",
            "You must always ask for the best one.\x02\x03",
            "#06104FTo visitors who come to see\x01",
            "I hope you have the best time,\x01",
            "To create a wonderful setting ……\x02\x03",
            "#06102FThat is Alcan shell,\x01",
            "And our artists\x01",
            "It's the biggest mission.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D3D")

    label("loc_2C96")


    ChrTalk(
        0x8,
        (
            "#06100FAbout Huff, renewal performances\x01",
            "The official announcement is in the vicinity\x01",
            "Please wait.\x02\x03",
            "#06104FEven those who watched the previous performances,\x01",
            "You should be able to have fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D3D")

    Jump("loc_2F10")

    label("loc_2D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2D50")
    Jump("loc_2F10")

    label("loc_2D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2F10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E8C")

    ChrTalk(
        0x8,
        (
            "#01700FHuh, I also got a new look and younger brother you guys as well\x01",
            "It feels like restarting at last.\x02\x03",
            "#01700FCecil can also see you brothers\x01",
            "I guess I was looking forward to it.\x02\x03",
            "#01709FNo, Ikko Ikuno, this jet\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHahaha ……\x01",
            "Please do not tease.\x02\x03",
            "#00004F(But, close to Cecil's older sister\x01",
            "I hope to have a good greetings. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F10")

    label("loc_2E8C")


    ChrTalk(
        0x8,
        (
            "#01700FHuh, our future development also\x01",
            "Please look forward to it.\x02\x03",
            "#01709FIt's still a secret,\x01",
            "Surely it will be fun!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F10")

    TalkEnd(0xFE)
    Return()

    # Function_9_287B end

    def Function_10_2F14(): pass

    label("Function_10_2F14")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x8,
        (
            "#06100FNow, Shri.\x01",
            "There is no time to actual production,\x01",
            "I'm going to visit you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12201FOoh!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_10_2F14 end

    def Function_11_2F85(): pass

    label("Function_11_2F85")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2F96")
    Jump("loc_34E7")

    label("loc_2F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2FA4")
    Jump("loc_34E7")

    label("loc_2FA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3039")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_300B")

    ChrTalk(
        0x9,
        "#01808F- I'm sorry, it's in front of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F(Lisha ………)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3034")

    label("loc_300B")


    ChrTalk(
        0x9,
        "#01801FIria … … please!\x02",
    )

    CloseMessageWindow()

    label("loc_3034")

    Jump("loc_34E7")

    label("loc_3039")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3047")
    Jump("loc_34E7")

    label("loc_3047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3055")
    Jump("loc_34E7")

    label("loc_3055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3063")
    Jump("loc_34E7")

    label("loc_3063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3071")
    Jump("loc_34E7")

    label("loc_3071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_307F")
    Jump("loc_34E7")

    label("loc_307F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_308D")
    Jump("loc_34E7")

    label("loc_308D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_32F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A8")
    Call(0, 8)
    Jump("loc_32F1")

    label("loc_30A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3273")

    ChrTalk(
        0x9,
        (
            "#06203FTrade meeting …… Really many people\x01",
            "You are coming to this crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAfter all,\x01",
            "Are Lisa tense, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#06208FWell, there it is, though ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FDo you have anything else to worry about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#06202FOh my, apart\x01",
            "It's not a big deal\x01",
            "please do not worry.\x02\x03",
            "#06204FThat's right,\x01",
            "Anyway, now on stage\x01",
            "I only have to concentrate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh, ah ……\x02\x03",
            "#00003F(Lisa, at the Trade Council\x01",
            "Do you have something to worry about? )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14C, 0)
    Jump("loc_32F1")

    label("loc_3273")


    ChrTalk(
        0x9,
        (
            "#06206FI do quite well, something extra\x01",
            "It is an idea type.\x02\x03",
            "#06201FAnyway, now on the stage\x01",
            "I only have to concentrate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F1")

    Jump("loc_34E7")

    label("loc_32F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3304")
    Jump("loc_34E7")

    label("loc_3304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_34E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3446")

    ChrTalk(
        0x9,
        (
            "#01802FRestart with adding new members …\x01",
            "From now on, everyone's\x01",
            "I will support my success.\x02\x03",
            "If you do not mind, this one\x01",
            "Please come and visit us any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, if there is something like that again\x01",
            "Please come and talk to us anytime.\x02\x03",
            "I will be sure to lend you my strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01809FHehe he is counting on him.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_34E7")

    label("loc_3446")


    ChrTalk(
        0x9,
        (
            "#01802FRestart with adding new members …\x01",
            "From now on, everyone's\x01",
            "I will support my success.\x02\x03",
            "#01809FIf you do not mind, this one\x01",
            "Please come and visit us any time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34E7")

    TalkEnd(0xFE)
    Return()

    # Function_11_2F85 end

    def Function_12_34EB(): pass

    label("Function_12_34EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3511")
    Call(0, 58)
    Return()

    label("loc_3511")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3CAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_352F")
    Call(0, 35)
    Jump("loc_3CA8")

    label("loc_352F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_END)), "loc_3862")

    ChrTalk(
        0xA,
        (
            "#04200FOkay, you guys\x01",
            "Iria's place now\x01",
            "You went to visit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I'm fine.\x01",
            "I had you see it several times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04203FReally……\x02\x03",
            "#04200FEr, Lisa's older sister … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708FYeah … … still towards the face\x01",
            "I have not met him,\x01",
            "Hearing a call through the door of the hospital room ……\x02\x03",
            "#10702FWhat I should say …\x01",
            "Sorry, Shri-chan.\x01",
            "I'm getting a little worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04205FSomething like that, I have nothing else ……\x02\x03",
            "#04204FBut …\x01",
            "I feel I can feel secure at all.\x02\x03",
            "#04202FFinally,\x01",
            "Lisa's older sister can not go anywhere\x01",
            "Because I feel confident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10702FShri-chan ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#04206FSorry, Lisa's older sister.\x01",
            "Say something cheeky.\x02\x03",
            "#04202FAnyway, I\x01",
            "I've been waiting here forever.\x02\x03",
            "#04209FAnyway, come back soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10702FHehe … … Yes, I understand.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B6E")

    label("loc_3862")


    ChrTalk(
        0xA,
        (
            "#14000FOkay, you guys\x01",
            "Iria's place now\x01",
            "You went to visit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I'm fine.\x01",
            "I had you see it several times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14003FReally……\x02\x03",
            "#14000FEr, Lisa's older sister … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708FYeah … … still towards the face\x01",
            "I have not met him,\x01",
            "Hearing a call through the door of the hospital room ……\x02\x03",
            "#10702FWhat I should say …\x01",
            "Sorry, Shri-chan.\x01",
            "I'm getting a little worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#14005FSomething like that, I have nothing else ……\x02\x03",
            "#14004FBut …\x01",
            "I feel I can feel secure at all.\x02\x03",
            "#14002FFinally,\x01",
            "Lisa's older sister can not go anywhere\x01",
            "Because I feel confident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10702FShri-chan ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#14006FSorry, Lisa's older sister.\x01",
            "Say something cheeky.\x02\x03",
            "#14002FAnyway, I\x01",
            "I've been waiting here forever.\x02\x03",
            "#14009FAnyway, come back soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10702FHehe … … Yes, I understand.\x02",
    )

    CloseMessageWindow()

    label("loc_3B6E")

    SetScenarioFlags(0x1CF, 7)
    Jump("loc_3CA8")

    label("loc_3B76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_END)), "loc_3C16")

    ChrTalk(
        0xA,
        (
            "#04200FI do not know where I will go,\x01",
            "Please be careful.\x02\x03",
            "#04202FThe performance will also resume within a short distance.\x01",
            "I will have you come naturally at that time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA8")

    label("loc_3C16")


    ChrTalk(
        0xA,
        (
            "#14000FI do not know where I will go,\x01",
            "Please be careful.\x02\x03",
            "#14002FThe performance will also resume within a short distance.\x01",
            "I will have you come naturally at that time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CA8")

    Jump("loc_3FF6")

    label("loc_3CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3D22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CC8")
    Call(0, 13)
    Jump("loc_3D1D")

    label("loc_3CC8")


    ChrTalk(
        0xA,
        (
            "#12203F…… First the sound came,\x01",
            "Then to jump out of the stage sleeve\x01",
            "Take the step … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D1D")

    Jump("loc_3FF6")

    label("loc_3D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3D30")
    Jump("loc_3FF6")

    label("loc_3D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3D72")

    ChrTalk(
        0xA,
        (
            "#04201FMr. Ilya,\x01",
            "I will be fine anytime!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FF6")

    label("loc_3D72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D83")
    Call(0, 10)
    Jump("loc_3FF6")

    label("loc_3D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D91")
    Jump("loc_3FF6")

    label("loc_3D91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3D9F")
    Jump("loc_3FF6")

    label("loc_3D9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3DAD")
    Jump("loc_3FF6")

    label("loc_3DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3E43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DC8")
    Call(0, 14)
    Jump("loc_3E3E")

    label("loc_3DC8")


    ChrTalk(
        0xA,
        (
            "#04203FNow do it in front of me ……\x01",
            "That's what it is.\x02\x03",
            "#04201FOkay, good.\x01",
            "I will practice without thinking anything unnecessary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E3E")

    Jump("loc_3FF6")

    label("loc_3E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E51")
    Jump("loc_3FF6")

    label("loc_3E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ED6")

    ChrTalk(
        0xA,
        (
            "#04206FWell, Iria and Mr.\x01",
            "Lisa's older sister can not afford it.\x02\x03",
            "#04200FSomeday I\x01",
            "Acting like two people ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3F52")

    label("loc_3ED6")


    ChrTalk(
        0xA,
        (
            "#04205FOh, no.\x01",
            "I have to finish cleaning up early.\x02\x03",
            "#04203FI am lying,\x01",
            "I will run out of practice time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F52")

    Jump("loc_3FF6")

    label("loc_3F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3F65")
    Jump("loc_3FF6")

    label("loc_3F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3FF6")

    ChrTalk(
        0xA,
        (
            "#04200FEven so ……\x01",
            "Lisa's older sister learn how to take a rest\x01",
            "I understand why it improved.\x02\x03",
            "#04204F…… I guess Iria is awesome.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FF6")

    TalkEnd(0xFE)
    Return()

    # Function_12_34EB end

    def Function_13_3FFA(): pass

    label("Function_13_3FFA")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0x11,
        (
            "Then, Nicole, Shri.\x01",
            "As I will follow, please start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I understand.\x01",
            "Let's go, Shri.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12201FOh, first from the step\x01",
            "It is a jump.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Shuri and everyone else … ….\x01",
            "It seems they are concentrating on practice. )\x02",
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

    # Function_13_3FFA end

    def Function_14_40FE(): pass

    label("Function_14_40FE")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xA,
        (
            "#04205FHey, Nicole.\x02\x03",
            "What about the Iria\x01",
            "Detailed contents of the renewal performance\x01",
            "Will not you tell everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Oh, I do not know the real place,\x01",
            "Anyway, the final performance is still there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "While it is not over, please talk next time\x01",
            "It will not be easy to concentrate … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Perhaps it is such a reason?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04203FThat's right … I see.\x01",
            "Nicole is clever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "No, I think it is normal, but …\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 2)
    Return()

    # Function_14_40FE end

    def Function_15_42A8(): pass

    label("Function_15_42A8")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xA,
        (
            "#04200FHey, Nicole.\x01",
            "To the rotation that that scene is doing\x01",
            "I'm switching over, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Oh, that's a breath\x01",
            "I'm connecting at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "The timing is difficult,\x01",
            "That person is smooth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#04201FWell, I see.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_441F")

    ChrTalk(
        0x101,
        (
            "#00000F(Shuri … Good luck\x01",
            "I guess you are practicing. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Yeah, dedicated\x01",
            "It is transmitted. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_449D")

    label("loc_441F")


    ChrTalk(
        0x101,
        (
            "#00005F(This child is an alkane shell\x01",
            "A newcomer girl … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Huhu, in one girlfriend\x01",
            "You seem to be practicing. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_449D")

    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 2)
    Return()

    # Function_15_42A8 end

    def Function_16_44B6(): pass

    label("Function_16_44B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44DF")
    Call(0, 36)
    Return()

    label("loc_44DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_44F0")
    Jump("loc_4A9A")

    label("loc_44F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_458C")

    ChrTalk(
        0xFE,
        (
            "Even so ……\x01",
            "I do not want to go out\x01",
            "It suddenly passed and it was quite confusing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, anyway\x01",
            "More than what I left here is to practice\x01",
            "I just concentrate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A9A")

    label("loc_458C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_45E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45A7")
    Call(0, 13)
    Jump("loc_45DE")

    label("loc_45A7")


    ChrTalk(
        0xFE,
        (
            "At the beginning of Shri's timing\x01",
            "Together, then … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45DE")

    Jump("loc_4A9A")

    label("loc_45E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_45F1")
    Jump("loc_4A9A")

    label("loc_45F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4690")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_460C")
    Call(0, 24)
    Jump("loc_468B")

    label("loc_460C")


    ChrTalk(
        0xFE,
        (
            "Okay, I do not really know.\x01",
            "It sounds like I stepped on something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "whatever……\x01",
            "Seniors are also saying that,\x01",
            "I have to practice early.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_468B")

    Jump("loc_4A9A")

    label("loc_4690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_469E")
    Jump("loc_4A9A")

    label("loc_469E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_46AC")
    Jump("loc_4A9A")

    label("loc_46AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_46BA")
    Jump("loc_4A9A")

    label("loc_46BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_46C8")
    Jump("loc_4A9A")

    label("loc_46C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_475E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46E3")
    Call(0, 14)
    Jump("loc_4759")

    label("loc_46E3")


    ChrTalk(
        0xFE,
        "What is it, Shuri is obedient.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But that's why\x01",
            "There are many places to emulate.\x01",
            "I also have to work harder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4759")

    Jump("loc_4A9A")

    label("loc_475E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_476C")
    Jump("loc_4A9A")

    label("loc_476C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4895")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47EA")

    ChrTalk(
        0xFE,
        (
            "Yacht……\x01",
            "I'm going to practice again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "About the questionnaire table\x01",
            "I left it to you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4890")

    label("loc_47EA")


    ChrTalk(
        0xFE,
        (
            "I'm worried about the performance tomorrow,\x01",
            "Specific content of the renewal stage\x01",
            "It can not help being worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, even extra things\x01",
            "You should not think about it.\x01",
            "There is only practice now anyway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4890")

    Jump("loc_4A9A")

    label("loc_4895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_48A3")
    Jump("loc_4A9A")

    label("loc_48A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4A9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49F5")

    ChrTalk(
        0xFE,
        (
            "Shuri is still working downroad ……\x01",
            "When you participate in acting practice something,\x01",
            "There is no hint of movement of that movement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that most of us are members of Uchi,\x01",
            "I say that you are a genius.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though they are all talented\x01",
            "Even efforts that are not ordinary are repeated.\x01",
            "It is not to compare, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Anyway, I just do my best with me.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_4A9A")

    label("loc_49F5")


    ChrTalk(
        0xFE,
        (
            "With talent everyone\x01",
            "It may be inferior, but I am me\x01",
            "Recently I got accepted little by little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got into a maze for a while though ….\x01",
            "Anyway, I just do my best with me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A9A")

    TalkEnd(0xFE)
    Return()

    # Function_16_44B6 end

    def Function_17_4A9E(): pass

    label("Function_17_4A9E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4D43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CA7")

    ChrTalk(
        0xC,
        "Oh, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Actually,\x01",
            "Direct from here\x01",
            "Please contact me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "An automatic doll immediately#8RAutomata#To produce\x01",
            "To be able to work\x01",
            "It has become.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh\x01",
            "That was good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yeah, really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In the first place, from meister\x01",
            "I do not bother to contact you\x01",
            "Because it is rare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "There is nothing I'm happy about.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Meister, after all\x01",
            "You had a lot of trouble. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200F(Hehe, I hope it will be completed soon.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CF, 6)
    Jump("loc_4D3E")

    label("loc_4CA7")


    ChrTalk(
        0xC,
        (
            "Actively from the Meister\x01",
            "To cooperate,\x01",
            "There is nothing I'm happy about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I, too, to build a foundation\x01",
            "I have to work harder and more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D3E")

    Jump("loc_5842")

    label("loc_4D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4E4A")

    ChrTalk(
        0xFE,
        (
            "I was handled by Meister\x01",
            "Stage equipment and automatic dolls#8RAutomata#Restoration of\x01",
            "It is impossible for me to fluffy … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, somehow, the appearance of the stage\x01",
            "It has arrived before we can arrange it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Worry meister too\x01",
            "It is that it is being given … …\x01",
            "I will build it again and again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5842")

    label("loc_4E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4FC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F3A")

    ChrTalk(
        0xFE,
        (
            "We also removed debris from the stage,\x01",
            "Finally decent exercise\x01",
            "I became able to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My job in charge of the stage equipment\x01",
            "Even still at the starting point\x01",
            "It is far from it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still what you can do steadily\x01",
            "I will proceed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_4FBD")

    label("loc_4F3A")


    ChrTalk(
        0xFE,
        (
            "My job in charge of the stage equipment\x01",
            "Even still at the starting point\x01",
            "It is far from it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still what you can do steadily\x01",
            "I will proceed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FBD")

    Jump("loc_5842")

    label("loc_4FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_51D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5137")

    ChrTalk(
        0xFE,
        (
            "Have cooperation with me until now\x01",
            "Built-up stage equipment and automatic dolls#8RAutomata#Is\x01",
            "Everything was destroyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Meister breathes life,\x01",
            "And the members of the theater tell the soul\x01",
            "Works that I had never raised … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What I stumbled upon\x01",
            "It is certainly an unforgivable rage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, if it is a work ……\x01",
            "It can be rebuilt again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But Iria … …………!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_51D3")

    label("loc_5137")


    ChrTalk(
        0xFE,
        (
            "…… Anyway, I also\x01",
            "The stage of the alkane shells many times\x01",
            "I can build it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I had been frustrated with such a thing,\x01",
            "More than anything to Mr. Ilya\x01",
            "I am sorry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51D3")

    Jump("loc_5842")

    label("loc_51D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5313")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_529E")

    ChrTalk(
        0xFE,
        (
            "OK, this is the stage equipment\x01",
            "Is the setting perfect?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The direction of action is already yesterday\x01",
            "I have already confirmed the rehearsal … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that the real thing starts\x01",
            "I just wait for now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_530E")

    label("loc_529E")


    ChrTalk(
        0xFE,
        (
            "OK, this is the stage equipment\x01",
            "Is the setting perfect?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that the real thing starts\x01",
            "I just wait for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_530E")

    Jump("loc_5842")

    label("loc_5313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5321")
    Jump("loc_5842")

    label("loc_5321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_532F")
    Jump("loc_5842")

    label("loc_532F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_533D")
    Jump("loc_5842")

    label("loc_533D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_54F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5454")

    ChrTalk(
        0xFE,
        (
            "I was asking the acquaintance's studio\x01",
            "A stage device for renewal performances\x01",
            "I heard he will finish it tomorrow at last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This time it is impossible to say various things\x01",
            "I was annoyed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Meister is always at the end\x01",
            "You manage to do something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am looking forward to going to get it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_54EB")

    label("loc_5454")


    ChrTalk(
        0xFE,
        (
            "This time it is impossible to say various things\x01",
            "I was annoyed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Meister is always at the end\x01",
            "You manage to do something.\x01",
            "I am looking forward to going to get it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54EB")

    Jump("loc_5842")

    label("loc_54F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_56FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5659")

    ChrTalk(
        0xFE,
        (
            "The idea of a new stage device\x01",
            "It was almost settled, so now\x01",
            "It is a place to make it concrete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Regardless of the details,\x01",
            "Renewal according to the practice of the stage\x01",
            "There is also a need to pack up … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until the release date, it's actually just one month\x01",
            "There is only a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you do not do it as soon as possible,\x01",
            "I do not seem to be in time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_56FA")

    label("loc_5659")


    ChrTalk(
        0xFE,
        (
            "Until the release date of the renewal performance,\x01",
            "Only a little bit more than one month actually\x01",
            "I do not have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you do not do it as soon as possible,\x01",
            "I do not seem to be in time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56FA")

    Jump("loc_5842")

    label("loc_56FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_570D")
    Jump("loc_5842")

    label("loc_570D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_57BA")

    ChrTalk(
        0xFE,
        (
            "In preparation for the night performance tomorrow,\x01",
            "We had a break every time until 3 pm\x01",
            "I am supposed to take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a great free time.\x01",
            "Shall I go to see it even at the unveiling ceremony?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5842")

    label("loc_57BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_57C8")
    Jump("loc_5842")

    label("loc_57C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5842")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57E3")
    Call(0, 7)
    Jump("loc_5842")

    label("loc_57E3")


    ChrTalk(
        0xFE,
        "But is it 5 more extra … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course I do my best,\x01",
            "It is also an outrageous order.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5842")

    TalkEnd(0xFE)
    Return()

    # Function_17_4A9E end

    def Function_18_5846(): pass

    label("Function_18_5846")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5903")

    ChrTalk(
        0xFE,
        (
            "Despite this situation,\x01",
            "He sends cheers in front of the theater company\x01",
            "It looks like there are fans of children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yale that Ms. Iria gave\x01",
            "That's right, but …\x01",
            "I do not appreciate it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C36")

    label("loc_5903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_59C9")

    ChrTalk(
        0xFE,
        (
            "We have only the stage -\x01",
            "And fortunately still we still\x01",
            "There are people who support you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is decided what to do.\x01",
            "Even in the city like this\x01",
            "It just polishes skills as usual.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C36")

    label("loc_59C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5A18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59E4")
    Call(0, 19)
    Jump("loc_5A13")

    label("loc_59E4")


    ChrTalk(
        0xFE,
        (
            "Let's go, Theodore.\x01",
            "Put in your mouth …!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A13")

    Jump("loc_5C36")

    label("loc_5A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5A26")
    Jump("loc_5C36")

    label("loc_5A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5AAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A41")
    Call(0, 20)
    Jump("loc_5AA7")

    label("loc_5A41")


    ChrTalk(
        0xFE,
        (
            "Well, as I say it\x01",
            "It is good to handle any role\x01",
            "You are my true heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I will respond to requests exactly.\x02",
    )

    CloseMessageWindow()

    label("loc_5AA7")

    Jump("loc_5C36")

    label("loc_5AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5C36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BA4")

    ChrTalk(
        0xFE,
        (
            "However, as expected\x01",
            "Should I say Queen Libert ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Claudia Highness is also pretty,\x01",
            "Assistant Yulia is a soldier to keep\x01",
            "It is unnecessary, is not it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The skill of sword is also preeminent,\x01",
            "As soon as I enter Uchiha flower shaped actress\x01",
            "I think I can get it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5C36")

    label("loc_5BA4")


    ChrTalk(
        0xFE,
        (
            "Assistant Yulia ……\x01",
            "In that appearance is a soldier\x01",
            "It is unnecessary, is not it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The skill of sword is also preeminent,\x01",
            "As soon as I enter Uchiha flower shaped actress\x01",
            "I think I can get it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C36")

    TalkEnd(0xFE)
    Return()

    # Function_18_5846 end

    def Function_19_5C3A(): pass

    label("Function_19_5C3A")

    OP_4B(0xD, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xD,
        (
            "Well, Mr. Prerie.\x01",
            "Can I have a solo song at once?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "OK, okay, I will skip it.\x01",
            "Both of them should increase the tension.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "……I understand.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_19_5C3A end

    def Function_20_5CE4(): pass

    label("Function_20_5CE4")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xD,
        (
            "Come on, Theodore.\x01",
            "Next is our climax scene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You are the guardian knight altar of the altar\x01",
            "Prodigal prince Haru sword to me ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "It is getting frustrating to say that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In any case, the development here\x01",
            "I wanted you to renew.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "Ha\x01",
            "What is going to say about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Keep silent and get along well,\x01",
            "This foolish.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "Oh, you.\x01",
            "Now you got stupid! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Then you are a Baka Dor!\x01",
            "Hi, this Baka Dor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "… … Because it was bad,\x01",
            "Just match it sooner.\x02",
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
            "#00005F(Well, what is it before production?\x01",
            "It is an unexpected atmosphere. )\x02",
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

    # Function_20_5CE4 end

    def Function_21_5F98(): pass

    label("Function_21_5F98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6055")

    ChrTalk(
        0xFE,
        (
            "HM……\x01",
            "The person named the stage person continues\x01",
            "Do not make me feel like a happy person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Various incentives received from various people … …\x01",
            "I will return it many times someday\x01",
            "I hope to continue to devote more and more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_635B")

    label("loc_6055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6063")
    Jump("loc_635B")

    label("loc_6063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_60B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_607E")
    Call(0, 19)
    Jump("loc_60B3")

    label("loc_607E")


    ChrTalk(
        0xFE,
        (
            "Oh, Eugene.\x01",
            "Do not shake off you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60B3")

    Jump("loc_635B")

    label("loc_60B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_60C6")
    Jump("loc_635B")

    label("loc_60C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_624E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60E1")
    Call(0, 20)
    Jump("loc_6249")

    label("loc_60E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61DF")

    ChrTalk(
        0xE,
        (
            "… … Eugene has been upset since long ago\x01",
            "There is a habit that strikes a few drops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It seems ugly,\x01",
            "Please do it for revenge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWell, is that so …?\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xD)

    ChrTalk(
        0xD,
        (
            "Hey, Teo.\x01",
            "Do not blow me into extra things!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6249")

    label("loc_61DF")


    ChrTalk(
        0xFE,
        (
            "Anyway … any stage\x01",
            "Premiere is especially important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As long as there is time,\x01",
            "Do you want to review the acting?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6249")

    Jump("loc_635B")

    label("loc_624E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_635B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_631B")

    ChrTalk(
        0xFE,
        "…… Indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "His Highness Claudia was a student\x01",
            "Experience participating in theater also\x01",
            "It was a story that there was … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Surely, both of you\x01",
            "A figure that was dignified on the stage\x01",
            "It will be able to show off.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_635B")

    label("loc_631B")


    ChrTalk(
        0xFE,
        (
            "surely……\x01",
            "Where the two people stand on the stage\x01",
            "I definitely want to see it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_635B")

    TalkEnd(0xFE)
    Return()

    # Function_21_5F98 end

    def Function_22_635F(): pass

    label("Function_22_635F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_63B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_637D")
    Call(0, 19)
    Jump("loc_63B2")

    label("loc_637D")


    ChrTalk(
        0xFE,
        (
            "Both of you have a nice face.\x01",
            "I can not lose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63B2")

    TalkEnd(0xFE)
    Return()

    # Function_22_635F end

    def Function_23_63B6(): pass

    label("Function_23_63B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_63C7")
    Jump("loc_6597")

    label("loc_63C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_64A5")

    ChrTalk(
        0xFE,
        (
            "Such as the stage etc.\x01",
            "Some say that it is unscrupulous … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I,\x01",
            "Conversely because it is such a time\x01",
            "I strongly believe that entertainment is necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because even human beings' unfortunate thing,\x01",
            "You will not have time to enjoy entertainment?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6597")

    label("loc_64A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_64FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64C0")
    Call(0, 13)
    Jump("loc_64F9")

    label("loc_64C0")


    ChrTalk(
        0xFE,
        (
            "I will perform my performance\x01",
            "Better, more beautiful …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64F9")

    Jump("loc_6597")

    label("loc_64FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_650C")
    Jump("loc_6597")

    label("loc_650C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6597")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6527")
    Call(0, 24)
    Jump("loc_6597")

    label("loc_6527")


    ChrTalk(
        0xFE,
        (
            "Indeed, Nicole っ っ た ら\x01",
            "There is nothing to worry about!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is the method of herbivorous boys,\x01",
            "Yun, I can not forgive!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6597")

    TalkEnd(0xFE)
    Return()

    # Function_23_63B6 end

    def Function_24_659B(): pass

    label("Function_24_659B")

    OP_4B(0x11, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0x11,
        (
            "Well ……\x01",
            "Friendly person seems to be a companion\x01",
            "I will do my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "As a fighting speech,\x01",
            "It's not like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Besides, Celine's seniors\x01",
            "I really like acting?\x02",
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
            "Nana, if you listen quietly,\x01",
            "Suddenly, what are you saying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Mum, because it's okay\x01",
            "I will do the performance matching soon,\x01",
            "This ska tang!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "Well,\x01",
            "Why were they abused?\x02",
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

    # Function_24_659B end

    def Function_25_6776(): pass

    label("Function_25_6776")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_25_6776 end

    def Function_26_677D(): pass

    label("Function_26_677D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_67A2")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_26_677D")

    label("loc_67A2")

    Return()

    # Function_26_677D end

    def Function_27_67A3(): pass

    label("Function_27_67A3")

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
        "#01702FWell, if it shrivels -\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#12P#04211FOr, stop it … …\x01",
            "Besides Lisa's older sister!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#01802FHehe, Mr. Ilya.\x01",
            "Shri - chan is in trouble, is not it?\x02",
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
        "#12P#00000FHaha, it is rising somewhat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FHuhuu, I'm just taking a break now.\x01",
            "It looks like a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FHon, real Iria · Platier …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FAlso, the two in the side … …\x02",
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
        "#01700FHmm……?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#01705F… … ah, younger brother! It is!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    OP_64(0x9)
    OP_64(0xA)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6B3F():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6B3F)
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0x9,
        "#5P#01802FOh … everyone!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C5E")
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
            "#1K◆ Prequel quest \"Stalker's Investigation Request\"? (for test)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【It does not change】\x01",          # 0
            "【Achievement】\x01",        # 1
            "【Not achieved】\x01",      # 2
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
        (0, "loc_6C45"),
        (1, "loc_6C4A"),
        (2, "loc_6C54"),
        (SWITCH_DEFAULT, "loc_6C5E"),
    )


    label("loc_6C45")

    Jump("loc_6C5E")

    label("loc_6C4A")

    OP_29(0x1D, 0x4, 0x10)
    Jump("loc_6C5E")

    label("loc_6C54")

    OP_29(0x1D, 0x3, 0x10)
    Jump("loc_6C5E")

    label("loc_6C5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C87")

    ChrTalk(
        0xA,
        "#04200F… ….\x02",
    )

    CloseMessageWindow()
    Jump("loc_6CA0")

    label("loc_6C87")


    ChrTalk(
        0xA,
        "#04200F…… Chiten.\x02",
    )

    CloseMessageWindow()

    label("loc_6CA0")


    def lambda_6CA5():
        OP_95(0xFE, 700, 1450, 12200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6CA5)

    def lambda_6CBF():
        OP_95(0xFE, -700, 1450, 11760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6CBF)

    def lambda_6CD9():
        OP_95(0xFE, 700, 1450, 10980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6CD9)

    def lambda_6CF3():
        OP_95(0xFE, -700, 1450, 10680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6CF3)
    OP_68(-820, 1620, 12730, 3000)
    MoveCamera(39, 26, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(13510, 3000)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#12P#00000FHaha, it's been a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FSorry, break time\x01",
            "It seems like I got in the way … …\x02",
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
            "Huh, that is not such a spray\x02\x03",
            "It came to see me after a long absence,\x01",
            "Please slow down.\x02\x03",
            "Oh, because it's so hard, my younger brother\x01",
            "Do you get on with the hug of reunion with me?\x02",
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
        "#12P#00012FNo, no, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01702FEr, so?\x01",
            "You do not have to hold back.\x02\x03",
            "#01709FHuh, or just … ….\x01",
            "As expected after all it seems like it feels good\x01",
            "Do you want a hug with Lisha?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x9)

    def lambda_6FBB():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6FBB)
    Sleep(50)

    def lambda_6FCB():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6FCB)

    ChrTalk(
        0x101,
        "#12P#00011FLet me see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#01806FI, Iria san … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12P#04200FWell, do not mind my father too.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 500)

    ChrTalk(
        0x102,
        (
            "#12P#00109FWhatching\x01",
            "Lisha is as usual\x01",
            "It sounds like you are having trouble.\x02",
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
            "Oh, haha ….\x01",
            "All this is like a fate\x01",
            "It may be things though.\x02\x03",
            "But, I have not seen you everyone for a long time\x01",
            "I'm really happy.\x02\x03",
            "Hehe, from now on again\x01",
            "Thank you.\x02",
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
            "#12P#10304FMr. Hoff, Leisha\x01",
            "I made a debut at the performance at the memorial festival\x01",
            "I wonder if it was an artist.\x02\x03",
            "#10302FCertainly, in an apartment in the old city\x01",
            "Was not she living there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#01802FR-right\x02\x03",
            "#01805FWell, you mean,\x01",
            "A bad group in the old city … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWadi Hemisphere.\x01",
            "Huh, I'm honored to know you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01705FOh Lisha, are you a child you know?\x02\x03",
            "By the way, these children\x01",
            "It seems I had not been before … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes, two people\x01",
            "It is a new member.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FOh, I'm from the guard\x01",
            "I have been sent to the support department\x01",
            "It is called Noel Seeker!\x02\x03",
            "#10109FThat … … About Mr. Ilya\x01",
            "Together with his sister Fran,\x01",
            "I will always support you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#01709FHuh, thanks ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FTio and Randy are\x01",
            "I have not come back yet ……\x02\x03",
            "#00100FFor the time being with these 4 people\x01",
            "I am planning to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01700FI see~.\x02\x03",
            "#01709FHuh, quite eccentric\x01",
            "It seems they are gathered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FNo~……\x01",
            "Irian-san seems to be enemy\x01",
            "I do not have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FOr, the direction of the artist\x01",
            "More than I had imagined\x01",
            "Is not it Frank?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302Fsurely.\x01",
            "Besides, in the magazine\x01",
            "The degree of beauty is also remarkable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01702FHuh, thanks.\x01",
            "But I praised so much\x01",
            "There is nothing left?\x02\x03",
            "#01703FAnyway, anyway ……\x02\x03",
            "#01709FHey, did not shut up from a little while ago.\x01",
            "Please say hello.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P#04205F… Well, I understand.\x02",
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
            "I am working as a jackpot at a theatrical company\x01",
            "It's Shri · Atlaid.\x02\x03",
            "Er … OK, thanks.\x02",
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
        "#12P#10100FHuh, thank you Shuri.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7CBD")

    ChrTalk(
        0x101,
        "#12P#00000FHave you also been shrieking up?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        (
            "#5P#04203FHun, talk to her smiling.\x02\x03",
            "#04201F…… To be to say, I am still\x01",
            "That time#12R噵 噵 噵 噵 噵 噵#I have not forgotten.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00006F(Well, you still have it in the roots … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FUh, what was that time …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01709FWell, surely my younger brother\x01",
            "Shuri from behind gussily and ─\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00011FNo, no …\x02\x03",
            "#00006FOr rather, that one\x01",
            "The root cause is Shuri! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#5P#04205FWhat? Is it?\x02\x03",
            "#04208F… Well, well I guess\x01",
            "I was sorry but ….\x02\x03",
            "#04201FFeeling like that strongly hugging\x01",
            "Well it's fine and …!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7AD9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7AD9)
    Sleep(50)

    def lambda_7AE9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7AE9)
    Sleep(50)
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x109,
        "#12P#10105FBut, hug me …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FSomething that seems to be fun\x01",
            "It seems there was.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#12P#00011FOh no, no, so … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01709FHuh, somehow suddenly a scuffle!\x01",
            "Because I'm worried so I have participated too ─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#01806FMr. I, Mr. Ilya ……\x01",
            "It will be confusing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006F(Uh, on this matter\x01",
            "The more you refute it\x01",
            "I feel like getting caught in a mire … …)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_803F")

    label("loc_7CBD")


    ChrTalk(
        0x101,
        "#12P#00005FOh, Shuri \"chan\" …\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00011F#4SOh, you were a girl! Is it?#3S\x02\x03",
            "#00003FThat's right.\x01",
            "Although I saw it several times when I came here,\x01",
            "I did not notice it at all.\x02\x03",
            "#00000FYeah, surely looking carefully and having a cute face ……\x02",
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

    def lambda_7E4F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E4F)
    Sleep(50)

    def lambda_7E5F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7E5F)
    Sleep(50)

    def lambda_7E6F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7E6F)
    Sleep(50)

    def lambda_7E7F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7E7F)
    Sleep(50)

    def lambda_7E8F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7E8F)
    Sleep(50)
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        "#5P#04201FHere, this bastard …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P#01806FRo, Mr. Lloyd ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00111F…… I think that it is rude indeed.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#11P#00011FNo, that, sorry!\x01",
            "Because it was a male word … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#01709FHaha, it is truly my brother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHmm, like natural gigolo\x01",
            "Is this pattern also ant?\x01",
            "It is quite a learning experience.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        "#5P#00011FNo, no …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P#04203F…… Hun, I do not like him.\x02",
    )

    CloseMessageWindow()

    label("loc_803F")


    ChrTalk(
        0x9,
        (
            "#5P#01803FHuhu, even so … …\x01",
            "Everyone seems to be fine and what's more.\x02\x03",
            "#01809FTo the support department,\x01",
            "It was really well done ……\x01",
            "Please come and visit me anytime again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01700FYes, I'm also very welcome.\x02\x03",
            "#01704FBesides, the recent practice scene of Lisha\x01",
            "It's worth seeing even more than before.\x02",
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

    def lambda_81E4():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81E4)
    Sleep(50)

    def lambda_81F4():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_81F4)
    Sleep(50)

    def lambda_8204():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8204)
    Sleep(50)

    def lambda_8214():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8214)
    Sleep(50)

    def lambda_8224():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8224)
    Sleep(50)
    TurnDirection(0xA, 0x8, 500)

    ChrTalk(
        0x101,
        "#12P#00005FWell, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuff, surely she is\x01",
            "If I jumped on the stage\x01",
            "various#4R噵 噵#There seems to be something in there though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FHere, these are you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P#01802FOh, haha ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01709FHuh, of course there are, though.\x02\x03",
            "#01704FAround this time also a little work of daily life\x01",
            "You feel shimmering.\x02\x03",
            "#01702FI do not feel tired … …\x01",
            "Obviously, even when taking a rest\x01",
            "Did I improve it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#11P#01809F…… Eh, umo well,\x01",
            "Is it such a place?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)

    ChrTalk(
        0xA,
        (
            "#6P#04205FIs it so……\x01",
            "I did not notice at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FHehu, thanks to Irria\x01",
            "It seems like a difference in care level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#01803F(… indeed recently\x01",
            "\"Work\" is being closed,\x01",
            "I have a good rest … …)\x02\x03",
            "#01808F(To feel it with your skin,\x01",
            "After all Iria is amazing … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FHaha, well, Lisha\x01",
            "There is a place to work hard … ….\x02\x03",
            "From now on taking a good rest,\x01",
            "Be careful not to break your body.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_85DD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_85DD)
    Sleep(50)
    TurnDirection(0xA, 0x102, 500)

    ChrTalk(
        0x9,
        "#5P#01802FYes, thank you for your concern.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FBut, alkane shell\x01",
            "He always seems to be busy ……\x02\x03",
            "#00100FTo the extent that it does not get in the way\x01",
            "As much as I look out\x01",
            "It might be exactly right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01702FHehe, during rehearsal\x01",
            "Without a performance\x01",
            "You are always welcome.\x02\x03",
            "#01703FWell, from now on a bit\x01",
            "I'm getting busy.\x02",
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
        "#12P#10105FEr … Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FDo something funny\x01",
            "You seem to think about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01709FHuh, still hi · mt · spray\x02\x03",
            "#01700FWell, future development of our place\x01",
            "Please look forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FOkay, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FHuhu, firmly\x01",
            "You have to check it.\x02",
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

    # Function_27_67A3 end

    def Function_28_8909(): pass

    label("Function_28_8909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 6)), scpexpr(EXPR_END)), "loc_8916")
    Call(0, 29)
    Return()

    label("loc_8916")

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
        "#5P#00000FLisha, and shri ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FShri-chan,\x01",
            "You are wearing the costume of \"Princess of the Star\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00202F…… It is beautiful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305FBut, Shri Elephant …\x01",
            "Does not it seem something impatient?\x02",
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
            "#12206FHa ha ha ha …\x02\x03",
            "#12201FNama Theater company manager,\x01",
            "It was perfect now.\x02\x03",
            "If this is the case,\x01",
            "You will admit it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6PHmm, of course\x01",
            "It is a point of departure … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12206FHa, that is it again ……\x02\x03",
            "#12200FHey Lisa's older sister,\x01",
            "What do you think Lisa's older sister?\x02\x03",
            "#12202FI'm in the wrong move\x01",
            "You did not do it, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#06203FYeah, well … ….\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#06202F…… Hey, Shri-chan.\x02\x03",
            "Next thing is somewhat like an emotion\x01",
            "I wonder if I can put it in.\x02\x03",
            "#06204FI can think that \"I want to be like this\"\x01",
            "To image it … …\x01",
            "I can not explain it well ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#12201FMyself who seems to want \"like this\" …\x01",
            "Well, what do you need to do specifically?\x02",
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
        "#5P#00005F(Shuri …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300F(Hmm, apparently we are\x01",
            "It seems better to break away. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103F(Yup……\x01",
            "I can not get in the way. )\x02",
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

    # Function_28_8909 end

    def Function_29_8E6A(): pass

    label("Function_29_8E6A")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F(Shuri to Lisha … ….\x01",
            "Apparently to practice\x01",
            "It seems to be concentrated. )\x02\x03",
            "#00003F(Let 's not disturb now.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -62880, 0, 2950, 270)
    EventEnd(0x4)
    Return()

    # Function_29_8E6A end

    def Function_30_8EF9(): pass

    label("Function_30_8EF9")

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
        "#5P#01703F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FMr. Ilya ……\x01",
            "You were here.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x102, 500)

    ChrTalk(
        0x8,
        (
            "#5P#01705FOh, my brother, you guys.\x02\x03",
            "#01709FHuff, towards a renewal performance\x01",
            "Did he come to encourage me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FHehe, that is the place.\x02\x03",
            "Mr. Iria, from here\x01",
            "Lisa and Shri's\x01",
            "You seem to have watched practice?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5P#01704FYeah, from the second floor seat\x01",
            "I can see the whole thing well.\x02\x03",
            "#01702FWell, even so\x01",
            "The way young kids try their best\x01",
            "As expected after all.\x02\x03",
            "Somehow this way,\x01",
            "I remember when I was a newcomer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FIs it about when Iria was a newcomer …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00302FHaha, I do not think anything like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHuh, what was that story at the time\x01",
            "I'd like to ask.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)

    ChrTalk(
        0x8,
        (
            "#5P#01700FHehe, I do not mind … …\x01",
            "It's not that funny story, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FThank you, I would like to ask you a favor! It is!\x02\x03",
            "#10100FSurely, since debut\x01",
            "I thought it was \"a super large new expectant of expectation\"\x01",
            "It was dealt largely in magazines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00205FIndeed, from the debut.\x02\x03",
            "#00202FBy the way …\x01",
            "What motivated you to become an artist\x01",
            "What was it like?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01703FWell, well.\x02\x03",
            "#01700FAfter all, as a child\x01",
            "The stage of the alkane shell\x01",
            "I wonder if I watched it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FIndeed, I longed for it - ─\x01",
            "Feeling like it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01703FYeah, it's a bit different.\x02\x03",
            "#01700FSince that time, acting of artists\x01",
            "Production by elaborate stage equipment\x01",
            "It was wonderful ….\x02\x03",
            "#01706FWhen you finish\x01",
            "I wonder if something is unsatisfactory,\x01",
            "I did not agree.\x02",
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
        "#12P#00011FNo, I did not agree … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01700FIn fact, the audience and parents who were around\x01",
            "I was acclaimed and it was amazing\x01",
            "There should be no mistake … …\x02\x03",
            "#01703FI mean, if I were you\x01",
            "I can be on a better stage! To\x01",
            "You feel it.\x02\x03",
            "#01702FHuff, at that time yet\x01",
            "It was an amateur with no knowledge\x01",
            "It may be a strange story though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FWell, like that when I was a child … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHmm, but with that trend\x01",
            "When you hit the door of the alkane shell\x01",
            "Was not there a lot of collisions too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01706FWell, the new rice of paper\x01",
            "Because I'm going to pull out\x01",
            "Oh yeah, that is not so bad.\x02\x03",
            "#01700FBut, to me\x01",
            "I definitely will make it a better place now\x01",
            "There was a certain belief … …\x02\x03",
            "#01709FIf you continue to show it,\x01",
            "Nature and everyone understands,\x01",
            "Friction#4RVicious#It has gone away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FI see……\x01",
            "And now Irria's\x01",
            "Is that so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01704FHuff, I was still completely satisfied\x01",
            "There is almost no stage called though.\x02\x03",
            "#01702FBut, like Lischa or Sri\x01",
            "It is also that promising materials are coming in the future … …\x02\x03",
            "From now on Bang Bang,\x01",
            "In order to create the best stage\x01",
            "I wonder if I want to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FHaha, Iria really is\x01",
            "Greedy is … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104FHehe, it is said that there is no genius better than effort ….\x02\x03",
            "#00109FIria is a genius who strives hard.\x01",
            "It really feels like there is no enemy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00309FOh, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#01709FHuhu, boring story\x01",
            "I wonder if I let him.\x02\x03",
            "#01704FWell, if you like\x01",
            "Also this renewal performance\x01",
            "Please come and see.\x02\x03",
            "#01700FLisha and Sri also ……\x01",
            "Always make the best acting\x01",
            "Because it will show off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FYes, of course.\x02\x03",
            "#00000FThe best stage created by Iria … …\x01",
            "I will be looking forward to it.\x02",
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

    # Function_30_8EF9 end

    def Function_31_9C83(): pass

    label("Function_31_9C83")

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
        "Oh you guys\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9DB0():
        TurnDirection(0x8, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9DB0)

    def lambda_9DBD():
        TurnDirection(0x9, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9DBD)
    TurnDirection(0xA, 0x0, 500)

    def lambda_9DD1():
        OP_95(0xFE, 700, 1450, 12200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9DD1)

    def lambda_9DEB():
        OP_95(0xFE, -700, 1450, 11760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9DEB)

    def lambda_9E05():
        OP_95(0xFE, 700, 1450, 10980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9E05)

    def lambda_9E1F():
        OP_95(0xFE, -700, 1450, 10680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9E1F)

    def lambda_9E39():
        OP_95(0xFE, 700, 1450, 9980, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9E39)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x8,
        "#01705FOh it's little bro!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#04205FWhat do you want\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)

    ChrTalk(
        0x9,
        "#01808F…\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)
    Sleep(1000)
    TurnDirection(0x102, 0x9, 500)

    ChrTalk(
        0x101,
        "#00003FRixia…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FRixia…\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        (
            "#01705FWhat, Lisa.\x01",
            "My brother and something happened with you guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01803FNo\x02\x03",
            "#01801FIria-san, than that\x01",
            "I do not have time to go.\x02\x03",
            "The flow of the two people 's bargaining\x01",
            "I want to check it again.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 500)

    ChrTalk(
        0xA,
        (
            "#04200FThat's right Ilia\x02\x03",
            "Even me, the flow over there\x01",
            "I want to grasp it firmly.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#01705FOh right\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        (
            "#01703FThat's why my brothers,\x01",
            "If there seems to be no particular business\x01",
            "May I have it rounded up?\x02\x03",
            "#01700FNow I have a little concentration\x01",
            "I do not want to break it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A133():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A133)
    TurnDirection(0x102, 0x8, 500)

    ChrTalk(
        0x101,
        "#00003FR-right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FTo bother you\x01",
            "I am sorry.\x02",
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

    # Function_31_9C83 end

    def Function_32_A1D8(): pass

    label("Function_32_A1D8")

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

    def lambda_A428():
        OP_95(0xFE, -600, 2700, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A428)

    def lambda_A442():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A442)
    Sleep(100)

    def lambda_A456():
        OP_95(0xFE, 600, 2700, 900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A456)

    def lambda_A470():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A470)
    Sleep(500)

    def lambda_A484():
        OP_95(0xFE, -750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A484)

    def lambda_A49E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A49E)
    Sleep(100)
    OP_68(-1660, 3950, 2020, 4000)
    MoveCamera(33, 8, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(15070, 4000)

    def lambda_A4E0():
        OP_95(0xFE, 750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A4E0)

    def lambda_A4FA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A4FA)
    Sleep(500)

    def lambda_A50E():
        OP_95(0xFE, -500, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_A50E)

    def lambda_A528():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_A528)
    Sleep(100)

    def lambda_A53C():
        OP_95(0xFE, 770, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_A53C)

    def lambda_A556():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_A556)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00002Fthis is……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A5EF")

    ChrTalk(
        0x10A,
        (
            "#12P#00602F\"Golden Sun, Silver Moon\"\x01",
            "Someone called an additional scene ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A62B")

    label("loc_A5EF")


    ChrTalk(
        0x109,
        (
            "#12P#10102F\"Golden Sun, Silver Moon\"\x01",
            "It is an additional scene ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A62B")


    ChrTalk(
        0x103,
        "#12P#00202FShuri, it is amazing …\x02",
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

    def lambda_A726():
        OP_95(0xFE, -550, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A726)

    def lambda_A740():
        OP_95(0xFE, 620, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A740)

    def lambda_A75A():
        OP_95(0xFE, -720, 1330, 8470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A75A)

    def lambda_A774():
        OP_95(0xFE, 650, 1310, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A774)

    def lambda_A78E():
        OP_95(0xFE, -570, 1350, 7280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_A78E)

    def lambda_A7A8():
        OP_95(0xFE, 590, 1350, 7240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_A7A8)
    Sleep(1000)
    OP_4B(0xB, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0xB,
        "#5POh you guys\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FThe theater company manager, it is the first time in a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FEveryone, practicing unrepentantly\x01",
            "You seem to be working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5POh, with Shiri in the center\x01",
            "The stage composition that we reconsidered is also\x01",
            "You are likely to be shaped somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PAnyway, now,\x01",
            "To resume the performance as soon as possible\x01",
            "I'm doing my best with all my strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PIria also has eyes\x01",
            "I heard that he awoke … …\x01",
            "To meet her expectations as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FIndeed … was it so?\x02\x03",
            "#00008F(By the way, everyone at the theater company\x01",
            "Even Lisher's way\x01",
            "I do not know it. )\x02\x03",
            "#00003F(Even face alone\x01",
            "I want to show it, but … …)\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AB0F")
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
    Jump("loc_AB9D")

    label("loc_AB0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_AB9D")
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

    label("loc_AB9D")

    Sleep(1000)
    EventEnd(0x5)
    SetScenarioFlags(0x22, 2)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_32_A1D8 end

    def Function_33_ABAF(): pass

    label("Function_33_ABAF")

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

    def lambda_ADB3():
        OP_95(0xFE, -550, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ADB3)

    def lambda_ADCD():
        OP_95(0xFE, 620, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ADCD)

    def lambda_ADE7():
        OP_95(0xFE, -720, 1330, 8470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ADE7)

    def lambda_AE01():
        OP_95(0xFE, 650, 1310, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AE01)

    def lambda_AE1B():
        OP_95(0xFE, -570, 1350, 7280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_AE1B)

    def lambda_AE35():
        OP_95(0xFE, 590, 1350, 7240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_AE35)
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
        "#5PAre you guys ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PHow about you, is it such a wonderful anxiety?\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#11PEveryone is now anyway,\x01",
            "To resume the performance as soon as possible\x01",
            "I'm doing my best with all my strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PIria also has eyes\x01",
            "I heard that he awoke … …\x01",
            "To meet her expectations as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F(… … everyone in the theater company\x01",
            "Even Lisher's way\x01",
            "I do not know it. )\x02\x03",
            "#00008F(Even face alone\x01",
            "I want to show it, but … …)\x02",
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

    # Function_33_ABAF end

    def Function_34_B029(): pass

    label("Function_34_B029")

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

    def lambda_B279():
        OP_95(0xFE, -600, 2700, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B279)

    def lambda_B293():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B293)
    Sleep(100)

    def lambda_B2A7():
        OP_95(0xFE, 600, 2700, 900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B2A7)

    def lambda_B2C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B2C1)
    Sleep(500)

    def lambda_B2D5():
        OP_95(0xFE, -750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B2D5)

    def lambda_B2EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B2EF)
    Sleep(100)
    OP_68(-1660, 3950, 2020, 4000)
    MoveCamera(33, 8, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(15070, 4000)

    def lambda_B331():
        OP_95(0xFE, 750, 2700, -450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B331)

    def lambda_B34B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B34B)
    Sleep(500)

    def lambda_B35F():
        OP_95(0xFE, -500, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_B35F)

    def lambda_B379():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_B379)
    Sleep(100)

    def lambda_B38D():
        OP_95(0xFE, 770, 2700, -1550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_B38D)

    def lambda_B3A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_B3A7)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B507")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00000Fthis is……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B44A")

    ChrTalk(
        0x10A,
        (
            "#12P#00602F\"Golden Sun, Silver Moon\"\x01",
            "Someone called an additional scene ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4D9")

    label("loc_B44A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B49B")

    ChrTalk(
        0x109,
        (
            "#12P#10102F\"Golden Sun, Silver Moon\"\x01",
            "It is an additional scene ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4D9")

    label("loc_B49B")


    ChrTalk(
        0x105,
        (
            "#12P#10402FHuff, \"The Sun of Gold, The Moon of Silver\"\x01",
            "It is an additional scene.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4D9")


    ChrTalk(
        0x103,
        "#12P#00202FShuri, it is amazing …\x02",
    )

    CloseMessageWindow()
    Jump("loc_B576")

    label("loc_B507")


    ChrTalk(
        0x101,
        (
            "#12P#00000FEveryone, there is still a long way to go\x01",
            "He seems to be practicing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10702F… … Shri-chan, everyone …………\x02",
    )

    CloseMessageWindow()

    label("loc_B576")

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

    def lambda_B648():
        OP_95(0xFE, -550, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B648)

    def lambda_B662():
        OP_95(0xFE, 620, 900, 9770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B662)

    def lambda_B67C():
        OP_95(0xFE, -720, 1330, 8470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B67C)

    def lambda_B696():
        OP_95(0xFE, 650, 1310, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B696)

    def lambda_B6B0():
        OP_95(0xFE, -570, 1350, 7280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_B6B0)

    def lambda_B6CA():
        OP_95(0xFE, 590, 1350, 7240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_B6CA)
    Sleep(1000)
    OP_4B(0xB, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B730")

    ChrTalk(
        0xB,
        "#5POh you guys\x02",
    )

    CloseMessageWindow()
    Jump("loc_B74B")

    label("loc_B730")


    ChrTalk(
        0xB,
        "#5POh, you guys ……\x02",
    )

    CloseMessageWindow()

    label("loc_B74B")

    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#5PLisha -\x01",
            "Is not Risa?\x02",
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
        "#5P#N#12211FLisa's older sister …?\x02",
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

    def lambda_B858():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B858)
    Sleep(50)

    def lambda_B868():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B868)
    Sleep(50)

    def lambda_B878():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_B878)
    Sleep(50)

    def lambda_B888():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B888)
    Sleep(50)

    def lambda_B898():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B898)
    Sleep(50)

    def lambda_B8A8():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B8A8)
    Sleep(50)

    def lambda_B8B8():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_B8B8)
    Sleep(50)

    def lambda_B8C8():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_B8C8)
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
        "#5PTrue, it's Lisha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PHaha, it's not a mistake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5P…… There is no doubt, certainly Leisha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PHuhu, in this\x01",
            "The last feeling of mind has gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#12P#10717F……everyone…………\x02\x03",
            "#10703FAh, I'm really sorry.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBD6")
    SetChrPos(0x10A, 680, 500, 11260, 0)
    Jump("loc_BC0D")

    label("loc_BBD6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBFC")
    SetChrPos(0x109, 680, 500, 11260, 0)
    Jump("loc_BC0D")

    label("loc_BBFC")

    SetChrPos(0x105, 680, 500, 11260, 0)

    label("loc_BC0D")

    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#5PThat's right, now\x01",
            "Together with the support department ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#12P#10708FYes, now I still have everything\x01",
            "I can not tell you ….\x02\x03",
            "#10710FHowever, if you add a hint\x01",
            "At that time properly ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PHehe\x01",
            "I wonder what I've chased so much\x01",
            "Do you have a look?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#12P#10712FHuh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PThat's right, no one told you\x01",
            "Why did you do such a face\x01",
            "I have not asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5POh, really.\x01",
            "I'm messed up with such a beautiful woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#12P#10718FMr. Pree ……\x01",
            "Celine, Mr. Nicole … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PAnyways……\x01",
            "If you do things you do\x01",
            "Come back as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PYou know, I still have a lot with Lisha\x01",
            "There are activities that I'd like to try.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10716FMr. Theodore, Eugene san ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PHuhu, I also costume\x01",
            "I am preparing and waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PI prepared the stage equipment, did not he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10715FKarelia, Heinz san ……\x02",
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
        "#12208F…… Lisa older sister ………\x02",
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#12P#10716FShri-chan ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12206FHere … …. Alcane shell ……\x01",
            "…… Because Lisa's older sister's place.\x02\x03",
            "#12212FWhat Lisha's older sister has,\x01",
            "I do not know it ….\x02\x03",
            "#12210FThis is Lisa's older sister ……\x01",
            "And Iria and I\x01",
            "It is also a place to come back ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10718F… … Shri-chan ………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12212FI … this place no matter what happens\x01",
            "I always keep it … … so ………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#12P#10715FYes … … Yeah ….\x02\x03",
            "#10716F…… Shri's feelings\x01",
            "It was well transmitted.\x02\x03",
            "#10716FI will come back properly … ….\x01",
            "… … So do not worry, promise.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#12210FPromise …. It's true, Lisa's older sister.\x02\x03",
            "A liar is a thousand books!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10715FYeah … I know.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 500)

    ChrTalk(
        0x101,
        "#11P#00002FRixia…\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x106,
        (
            "#6P#10715F…… Lloyd.\x01",
            "Let's go soon.\x02\x03",
            "#10716FEveryone has practice … …\x01",
            "We also hurry\x01",
            "I have to go to the desired place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh … That's right.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C420")
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
    Jump("loc_C4B3")

    label("loc_C420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C4B3")
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

    label("loc_C4B3")

    Sleep(1000)
    EventEnd(0x5)
    SetScenarioFlags(0x22, 2)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_34_B029 end

    def Function_35_C4C5(): pass

    label("Function_35_C4C5")

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
        "#12P#14003F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FWhat's wrong, Shri?\x02",
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
            "#11P#14000FOh, ah ……\x01",
            "A little praying.\x02\x03",
            "#14003FBecause it is kore, it is an altar.\x01",
            "…. Although it's a set.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302FHaha, I see.\x01",
            "However, it seems surprisingly beneficial.\x02\x03",
            "#00305FSo what on earth were you praying for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FHey Randy,\x01",
            "That's what I hear easily ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#14000FOh, is it alright?\x02\x03",
            "#14003FOf course, one of Mr. Iria … …\x02\x03",
            "And the other one is about you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00005FHuh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00205FAre we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#14003F…………………………\x02\x03",
            "#14001F…… I do not know the details, but\x01",
            "You guys talk about Kea\x01",
            "Are you chasing?\x02\x03",
            "So, from now on\x01",
            "I am about to go to a dangerous place.\x02\x03",
            "#14003F…………………….\x02\x03",
            "#14002FThat's why safety prayers.\x01",
            "Lisa's older sister is with me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C96D")

    ChrTalk(
        0x106,
        (
            "#6P#10702FShri-chan ……\x01",
            "Hehe, Thank you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA0B")

    label("loc_C96D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C9B9")

    ChrTalk(
        0x109,
        (
            "#6P#10102FI see……\x01",
            "Shuri, thanks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA0B")

    label("loc_C9B9")


    ChrTalk(
        0x105,
        (
            "#6P#10302FHuh, indeed … …\x01",
            "This is another happy thing\x01",
            "Will not you tell me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA0B")


    ChrTalk(
        0x101,
        (
            "#6P#00002FOh, like that\x01",
            "I am thankful that you will think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#14012FAnd anyway … …\x01",
            "Because Ka'aa is my precious friend.\x02\x03",
            "#14001FAbsolutely get back to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FOh, of course!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6F), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CEF4")

    ChrTalk(
        0xA,
        (
            "#11P#14000FI see …\x01",
            "Take it to you\x01",
            "I had something I wanted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FTo us ……\x01",
            "What on earth?\x02",
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
            "Shri took the hat and handed it to Lloyd.\x07\x00\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '修利的帽子'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('修利的帽子', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1DE, 1)
    OP_9B(0x1, 0xA, 0xB4, 0x1F4, 0x5DC, 0x0)

    ChrTalk(
        0x101,
        "#6P#00005Fthis is……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#04203FYou and Ka\x01",
            "If you chase after all\x01",
            "I want to go with it … ….\x02\x03",
            "#04208FI can not do that\x01",
            "I know that.\x02\x03",
            "Instead of using my favorite hat\x01",
            "I wonder if you can take it.\x02\x03",
            "#04201F… … Is it okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FNo, that's not true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102FShri's feelings,\x01",
            "I certainly got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FYes, this is what we\x01",
            "I take responsibility and keep it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CE6D")

    ChrTalk(
        0xA,
        (
            "#11P#04212FThat's right.\x01",
            "Then I asked you to do it.\x02\x03",
            "#04202FWell then,\x01",
            "Lisha elder sister and everyone else\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#6P#10709FYes, I understand.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_CEF4")

    label("loc_CE6D")


    ChrTalk(
        0xA,
        (
            "#11P#04212FThat's right.\x01",
            "Then I asked you to do it.\x02\x03",
            "#04202FWell then,\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FOh, I understand.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_CEF4")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF4F")
    OP_E0(0x34, 0x0)

    label("loc_CF4F")

    EventEnd(0x5)
    Return()

    # Function_35_C4C5 end

    def Function_36_CF52(): pass

    label("Function_36_CF52")

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
        "Oh, you are … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FHello, Nicole.\x02\x03",
            "I'd like to ask you a bit ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "At the request of Professor Lloyd\x01",
            "I explained the circumstances of collecting the questionnaire table.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        "Oh, that questioning list?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Recently I enjoyed practicing,\x01",
            "Take it all\x01",
            "I forgot it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Please wait a moment.\x01",
            "I will bring it.\x02",
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
        "Yes, this is it?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '尼克鲁的问诊表'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('尼克鲁的问诊表', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#6P#00000FYes, indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00102FHuhu, that seems like\x01",
            "Most of the influence of medicine\x01",
            "It does not seem to be left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Oh, properly\x01",
            "I had you treat me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "…… Now thinking,\x01",
            "Why such a medicine\x01",
            "I guess I put out my hand …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Indeed at that time\x01",
            "To my own talent\x01",
            "I have rotten, but ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FIn such gaps of heart\x01",
            "It's cunning to take over\x01",
            "It's pretty fucking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FWell, that you realized that\x01",
            "There is nothing to worry about any more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Oh … from now on\x01",
            "For alkane shell\x01",
            "I intend to further pursue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FI am looking forward to the stage.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x152, 4)
    OP_29(0x70, 0x1, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D48C")

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this, all the questionnaire charts\x01",
            "I finished collecting it.\x02\x03",
            "Immediately to Professor Seyland\x01",
            "Let's suppose that we will go reporting.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x70, 0x1, 0x5)

    label("loc_D48C")

    OP_93(0xF, 0x5A, 0x0)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 65000, 0, 3000, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_36_CF52 end

    def Function_37_D4BE(): pass

    label("Function_37_D4BE")

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
        "#11P#00000FWell, I wonder if Marie is … …\x02",
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
        "#11P#04600FHuh, you found it at once.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A3, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00000FAll right, then\x01",
            "Leave this to me here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A3, 0x101, 500)

    ChrTalk(
        0x1A3,
        (
            "#11P#04605FWell, oh well.\x02\x03",
            "#04602FAh, you have a handsome look.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D6CD():
        OP_95(0xFE, 8590, 15200, -7600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D6CD)
    Sleep(50)

    def lambda_D6EA():
        TurnDirection(0xFE, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_D6EA)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#00002FCome on, Mary.\x01",
            "I am comfortable coming here.\x02",
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
        "#00005FAh……\x02",
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

    def lambda_D8B4():
        OP_95(0xFE, 13800, 15200, -8010, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_D8B4)
    Sleep(1000)

    def lambda_D8D1():
        TurnDirection(0xFE, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D8D1)
    Sleep(50)

    def lambda_D8E1():

        label("loc_D8E1")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_D8E1")

    QueueWorkItem2(0x1A3, 1, lambda_D8E1)
    Sleep(1000)

    def lambda_D8F6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_D8F6)
    WaitChrThread(0x13, 1)
    SetChrFlags(0x13, 0x80)
    OP_6F(0x1)
    EndChrThread(0x1A3, 0x1)

    ChrTalk(
        0x1A3,
        "#04605FWow Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FYu, I got hurt … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04609FHaha, that's Shirley too.\x02\x03",
            "#04606FYeah, there is still a long way to go\x01",
            "Is not it a lack of training?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x14, 1770, 15200, -7960, 90)
    SetChrPos(0x15, 1770, 15200, -9370, 90)
    OP_68(6830, 16850, -8570, 4000)
    MoveCamera(46, 28, 0, 4000)
    OP_6E(500, 4000)
    SetCameraDistance(16250, 4000)

    def lambda_D9F1():
        OP_95(0xFE, 6590, 15200, -7960, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_D9F1)
    Sleep(50)

    def lambda_DA0E():
        OP_95(0xFE, 6590, 15200, -9370, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_DA0E)
    WaitChrThread(0x15, 1)
    OP_6F(0x79)

    ChrTalk(
        0x15,
        (
            "#6P#10300FHi, apparently\x01",
            "You seem to have disturbed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#6P#00106FI'm sorry,\x01",
            "It looks like it was a nice place ……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DA9C():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DA9C)
    Sleep(50)

    def lambda_DAAC():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_DAAC)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00004FNo, my stuff just was sweet.\x02\x03",
            "#00000FAnyway, I'll follow you soon.\x02\x03",
            "Just to be sure, Elly from the other side\x01",
            "Take me to the entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#6P#00100FYes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04609FHuh, then\x01",
            "Shall we chase after a while!\x02",
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

    # Function_37_D4BE end

    def Function_38_DBE7(): pass

    label("Function_38_DBE7")


    def lambda_DBEC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DBEC)

    def lambda_DBFD():
        OP_95(0xFE, 11590, 15200, -7990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DBFD)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 10260, 15200, -7100, 2000, 0x0)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_38_DBE7 end

    def Function_39_DC32(): pass

    label("Function_39_DC32")


    def lambda_DC37():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_DC37)

    def lambda_DC48():
        OP_95(0xFE, 11590, 15200, -7990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_DC48)
    WaitChrThread(0x1A3, 1)
    OP_95(0x1A3, 10260, 15200, -9100, 2000, 0x0)
    OP_93(0x1A3, 0x10E, 0x1F4)
    Return()

    # Function_39_DC32 end

    def Function_40_DC7D(): pass

    label("Function_40_DC7D")


    def lambda_DC82():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_DC82)

    def lambda_DC93():
        OP_95(0xFE, -8770, 15200, -8150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_DC93)
    WaitChrThread(0x14, 1)
    OP_93(0x14, 0x5A, 0x1F4)
    Return()

    # Function_40_DC7D end

    def Function_41_DCB4(): pass

    label("Function_41_DCB4")


    def lambda_DCB9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_DCB9)

    def lambda_DCCA():
        OP_95(0xFE, -11190, 15200, -8100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_DCCA)
    WaitChrThread(0x15, 1)
    OP_95(0x15, -10100, 15200, -9070, 2000, 0x0)
    OP_93(0x15, 0x5A, 0x1F4)
    Return()

    # Function_41_DCB4 end

    def Function_42_DCFF(): pass

    label("Function_42_DCFF")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's chase Mary in a hurry.\x01",
            "It should still be near by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04609FHuhuu, this time do not let it escape.\x01",
            "I have to do it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -11130, 15200, -7980, 90)
    EventEnd(0x4)
    Return()

    # Function_42_DCFF end

    def Function_43_DD93(): pass

    label("Function_43_DD93")

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

    def lambda_DF59():
        OP_95(0xFE, 110, 1250, 20620, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_DF59)
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

    def lambda_E06F():
        OP_98(0xFE, 0x0, 0x2710, 0x0, 0x96, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_E06F)
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
        "#00011F#10AI mean …!\x02",
    )

    Sleep(1500)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#06205F#10ADont, the stage equipment!\x02\x03",
            "#10ABut who the hell …! Is it?\x02",
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
        "#11P#04611F#10AHuhun, this much!\x02",
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
        "#12P#00005FHuh……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#06205FThat's amazing …!\x02",
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

    def lambda_E474():
        OP_98(0xFE, 0x0, 0x1770, 0x0, 0x96, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_E474)

    ChrTalk(
        0x13,
        "#6PWell, guys …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#11P#04606FHmm, I can take nothing and eat it.\x01",
            "It is not because it is not.\x02\x03",
            "Do not worry so nice.\x02\x03",
            "#04602FHey, how is this guy ♪\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Shirley is Mary's\x01",
            "I tickled my throat.\x07\x00\x02",
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
        "#6PWell, yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#11P#04609FHehe, is not it bad?\x02\x03",
            "#04600FWell then … … next one is like this\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A3, 0x0, 1200, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x13,
        "#6PYay!\x02",
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
        "#6PPursuit …… U U\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        "#11P#04609FHaha, calm down a bit?\x02",
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
        "#12P#00000FHaha, they are vivid hands.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#06204FYeah, I believe it is incredible\x01",
            "It was a light body.\x02",
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
            "#12P#06205FThat's right, who\x01",
            "I have to check if I have moved …\x02",
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
            "#11P#04600FWell then,\x01",
            "I am going down together.\x02\x03",
            "You should not go on a rampage anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#6PPaternity ♪\x02",
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
        "#11P#04605FWhat is it, suddenly … ah.\x02",
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

    def lambda_E9A5():
        OP_9D(0xFE, 0x212, 0x2328, 0x4268, 0x7D0, 0x64)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_E9A5)
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
        "#00011FUnpalatable……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#06201F…… っ ………!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 47)
    Sleep(500)
    OP_68(3370, 4570, 23550, 800)
    MoveCamera(48, 23, 0, 800)
    OP_6E(500, 800)
    SetCameraDistance(20670, 800)
    Sound(834, 0, 50, 0)

    def lambda_EAFA():
        OP_9D(0xFE, 0x6D6, 0x1F40, 0x4A38, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_EAFA)
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
        "#04605FWow, nice catch!\x02",
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
            "#00000FFuu … apparently\x01",
            "It seems I managed to do something.\x02",
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

    # Function_43_DD93 end

    def Function_44_EC51(): pass

    label("Function_44_EC51")


    def lambda_EC56():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EC56)

    def lambda_EC67():
        OP_95(0xFE, 0, 2250, 2940, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EC67)
    WaitChrThread(0x101, 1)
    Return()

    # Function_44_EC51 end

    def Function_45_EC81(): pass

    label("Function_45_EC81")


    def lambda_EC86():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_EC86)

    def lambda_EC97():
        OP_95(0xFE, 0, 1800, 5200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_EC97)
    WaitChrThread(0x1A3, 1)
    Return()

    # Function_45_EC81 end

    def Function_46_ECB1(): pass

    label("Function_46_ECB1")


    def lambda_ECB6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_ECB6)

    def lambda_ECC7():
        OP_95(0xFE, 0, 1350, 7460, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_ECC7)
    WaitChrThread(0x9, 1)
    Return()

    # Function_46_ECB1 end

    def Function_47_ECE1(): pass

    label("Function_47_ECE1")

    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x1)
    Sound(250, 0, 60, 0)
    OP_9D(0x9, 0x0, 0x4E2, 0x4BFA, 0xBB8, 0x1388)
    SetChrSubChip(0x9, 0x0)
    SetScenarioFlags(0x1, 4)
    Sound(637, 0, 100, 0)
    Sound(844, 0, 100, 0)
    BeginChrThread(0x9, 0, 0, 48)

    def lambda_ED24():
        OP_9D(0xFE, 0x1086, 0x4E2, 0x517C, 0x1388, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_ED24)
    OP_A1(0x9, 0x5DC, 0x3, 0x1, 0x2, 0x3)
    WaitChrThread(0x9, 1)
    Sound(326, 0, 50, 0)
    Return()

    # Function_47_ECE1 end

    def Function_48_ED50(): pass

    label("Function_48_ED50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_ED6C")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_48_ED50")

    label("loc_ED6C")

    Return()

    # Function_48_ED50 end

    def Function_49_ED6D(): pass

    label("Function_49_ED6D")

    SetChrPos(0xA, 0, 1250, 25500, 270)

    label("loc_ED7E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F152")
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x2)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    SetChrFlags(0xA, 0x1020)
    BeginChrThread(0xA, 1, 0, 51)

    def lambda_EDAF():
        OP_93(0xA, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EDAF)
    Sound(809, 0, 30, 0)
    OP_9D(0xA, 0x0, 0x4E2, 0x59D8, 0xBB8, 0x44C)
    Sound(50, 0, 70, 0)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    Sleep(200)

    def lambda_EDEA():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0xA96, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EDEA)
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

    def lambda_EE70():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1068, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EE70)
    Sleep(250)

    def lambda_EE8E():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1450, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EE8E)
    Sleep(250)

    def lambda_EEAC():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1838, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EEAC)
    Sleep(250)

    def lambda_EECA():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EECA)
    OP_49()
    SetChrFlags(0xA, 0x1020)
    SetChrChipByIndex(0xA, 0x3B)
    SetChrSubChip(0xA, 0x2)
    BeginChrThread(0xA, 1, 0, 54)
    Sleep(1000)

    def lambda_EEFC():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1C20, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EEFC)
    OP_49()
    Sound(844, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    Sound(50, 0, 50, 0)
    EndChrThread(0xA, 0x2)
    Sound(809, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x578)
    Sound(50, 0, 50, 0)

    def lambda_EF62():
        OP_9E(0xA, 0x0, 0x636A, 0xFFF24460, 0x2A94, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EF62)
    OP_49()
    Sound(844, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x514)
    Sound(50, 0, 50, 0)

    def lambda_EFA1():
        OP_93(0xA, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EFA1)
    BeginChrThread(0xA, 1, 0, 51)
    Sound(809, 0, 30, 0)
    OP_9C(0xA, 0x0, 0x0, 0x0, 0xBB8, 0x578)
    Sound(50, 0, 50, 0)
    BeginChrThread(0xA, 1, 0, 51)

    def lambda_EFDD():
        OP_9E(0xA, 0x0, 0x636A, 0xDBBA0, 0x1838, 0x2)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EFDD)
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

    def lambda_F0F3():
        OP_93(0xA, 0x5A, 0xC8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F0F3)
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
    Jump("loc_ED7E")

    label("loc_F152")

    Return()

    # Function_49_ED6D end

    def Function_50_F153(): pass

    label("Function_50_F153")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_50_F153 end

    def Function_51_F177(): pass

    label("Function_51_F177")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0x7D0, 0x3, 0x0, 0x1, 0x2)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_51_F177 end

    def Function_52_F19B(): pass

    label("Function_52_F19B")

    SetChrChipByIndex(0xFE, 0x39)
    OP_A1(0xFE, 0x9C4, 0x2, 0x0, 0x1)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_52_F19B end

    def Function_53_F1B0(): pass

    label("Function_53_F1B0")

    SetChrChipByIndex(0xFE, 0x3B)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_53_F1B0 end

    def Function_54_F1BE(): pass

    label("Function_54_F1BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F1DC")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    Jump("Function_54_F1BE")

    label("loc_F1DC")

    Return()

    # Function_54_F1BE end

    def Function_55_F1DD(): pass

    label("Function_55_F1DD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F1FB")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(60)
    Jump("Function_55_F1DD")

    label("loc_F1FB")

    Return()

    # Function_55_F1DD end

    def Function_56_F1FC(): pass

    label("Function_56_F1FC")

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
            "#00000FVery enthusiastic\x01",
            "It seems that I am doing my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, as the manager told you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FWhat?\x01",
            "When you see it like this it is a masterpiece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FScene to be added newly\x01",
            "Is it practice?\x02\x03",
            "#00304FPretty important\x01",
            "It's a story, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, it's a \"star of princess\" role.\x02\x03",
            "Anything in the latter half of the stage\x01",
            "It seems there is a big showroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, that will make you feel well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh, so much pressure\x01",
            "It will be a considerable thing ……\x02\x03",
            "#00000FDo not interrupt this\x01",
            "It might be better to break away.\x02",
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
        "#12205FAh … … you guys!\x02",
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
        "#00005FOops ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FI was noticed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, it's no problem.\x01",
            "Let's just say a greeting.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F6D6():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F6D6)
    Sleep(50)

    def lambda_F6F3():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F6F3)
    Sleep(50)

    def lambda_F710():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F710)
    Sleep(50)

    def lambda_F72D():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F72D)
    Sleep(50)

    def lambda_F74A():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F74A)
    Sleep(50)

    def lambda_F767():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F767)
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
            "#00000FHey, Shuri.\x01",
            "I was in the way of practicing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12203FFufun, apart ……\x02\x03",
            "#12200FSo, was it also a business?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FNo, it was a bit strewn.\x01",
            "I was just letting you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, it was bad to let me interrupt you though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12206FWell, just a break\x01",
            "I was thinking about sandwiching.\x01",
            "Separately it is OK though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FBut Shuri's acting\x01",
            "I saw it for the first time, but ….\x02\x03",
            "#00202FI was in the temple very much\x01",
            "I do not think he is a very newcomer.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#12205FIs that so …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FYeah, really.\x01",
            "I was surprised honestly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, what is it?\x01",
            "I wonder if there is no waste in movement.\x02\x03",
            "#00002FAlmost little\x01",
            "Is not it close to perfection?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12205FHuh……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    ChrTalk(
        0x109,
        (
            "#10109FYeah yeah, and that costume too\x01",
            "You look good on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105F… … Shri-chan?\x02",
    )

    CloseMessageWindow()
    OP_64(0xA)

    def lambda_FBE8():

        label("loc_FBE8")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_FBE8")

    QueueWorkItem2(0x102, 0, lambda_FBE8)

    def lambda_FBFA():

        label("loc_FBFA")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_FBFA")

    QueueWorkItem2(0x103, 0, lambda_FBFA)
    OP_99(0xA, 0x101, 0x3E8, 0x7D0, 0x0)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)

    ChrTalk(
        0xA,
        (
            "#12203F…… Hey, you.\x02\x03",
            "#12200FIf you like, practice a bit for acting\x01",
            "Will you go out with me?\x02\x03",
            "#12208FAnd that …\x01",
            "There is something I want to ask.\x02",
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
            "#00105FLloyd is Shri's\x01",
            "For practicing acting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWell, why am I?\x01",
            "I want to ask it … …\x02\x03",
            "#00003FClearly I will tell you,\x01",
            "About the stage\x01",
            "You do not know anything, are you an amateur?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12203FWell, another difficult thing\x01",
            "I'm not letting it go.\x02\x03",
            "#12208Fin addition,\x01",
            "There is a place I think slightly.\x02\x03",
            "#12200F……, how is that.\x01",
            "Will you go out with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FThat's right.\x02",
    )

    CloseMessageWindow()
    Call(0, 57)
    Return()

    # Function_56_F1FC end

    def Function_57_FECA(): pass

    label("Function_57_FECA")

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
            "Going out to practice shuri\x01",      # 0
            "To give up\x01",                  # 1
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
        (0, "loc_FF3C"),
        (1, "loc_1001F"),
        (SWITCH_DEFAULT, "loc_101BE"),
    )


    label("loc_FF3C")


    ChrTalk(
        0x101,
        (
            "#00000FOh, I do not mind if it's OK with me.\x02\x03",
            "You can not do anything really serious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12200FOh … I understand.\x02",
    )

    CloseMessageWindow()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Secret acting guidance】\x07\x00",
            "I started!\x02",
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
    Jump("loc_101BE")

    label("loc_1001F")


    ChrTalk(
        0x101,
        (
            "#00006F……sorry.\x01",
            "Now I have other errands\x01",
            "I do not think I can take time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12206FIf so, then.\x01",
            "… … forget what you said now.\x02\x03",
            "#12208FWell, I have a continuation of practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, ah ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#00100F(Hey, Lloyd.\x01",
            "I wonder if I can take time somehow? )\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#00003F(Well, that's right ……\x01",
            "Do you think about it again? )\x02",
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
    Jump("loc_101BE")

    label("loc_101BE")

    Return()

    # Function_57_FECA end

    def Function_58_101BF(): pass

    label("Function_58_101BF")

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
            "#12205FWhat is it like?\x01",
            "Was not there something wrong?\x02\x03",
            "#12200FDid you mean ……\x01",
            "Will you go out for practicing?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 57)
    Return()

    # Function_58_101BF end

    SaveToFile()

Try(main)
