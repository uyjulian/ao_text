from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1510.bin",                # FileName
        "t1510",                    # MapName
        "t1510",                    # Location
        0x004E,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 78, 0, 4, 0, 5],
    )

    BuildStringList((
        "t1510",                  # 0
        "Dir Kirsch",           # 1
        "Trainee Flora",         # 2
        "Trainee Misho",         # 3
        "A visitor",               # 4
        "A visitor",               # 5
        "A visitor",               # 6
        "A visitor",               # 7
        "A visitor",               # 8
        "Police",                 # 9
        "Tap",                 # 10
        "A visitor",               # 11
        "male",                   # 12
        "A visitor",               # 13
        "Cecil",                 # 14
        "God wolf Zeit",           # 15
        "Zookoist Rin",             # 16
        "Friend Aolia",         # 17
        "Franc",                 # 18
    ))

    AddCharChip((
        "chr/ch05302.itc",                   # 00
        "chr/ch02710.itc",                   # 01
        "chr/ch24300.itc",                   # 02
        "chr/ch29502.itc",                   # 03
        "chr/ch45300.itc",                   # 04
        "chr/ch45302.itc",                   # 05
        "chr/ch21902.itc",                   # 06
        "chr/ch21800.itc",                   # 07
        "chr/ch23000.itc",                   # 08
        "chr/ch20800.itc",                   # 09
        "chr/ch20902.itc",                   # 0A
        "chr/ch21900.itc",                   # 0B
        "chr/ch21000.itc",                   # 0C
        "chr/ch36300.itc",                   # 0D
        "chr/ch24400.itc",                   # 0E
        "chr/ch02702.itc",                   # 0F
        "chr/ch32002.itc",                   # 10
        "chr/ch32100.itc",                   # 11
        "chr/ch32102.itc",                   # 12
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

    DeclNpc(4294962487, 0,       11600,   225,  261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294955227, 150,     14399,   180,  261,  0x0, 0,   3,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(4294956887, 0,       13079,   322,  261,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(59330,   300,     4294964217, 180,  389,  0x0, 0,   6,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(59630,   0,       4294963036, 0,    389,  0x0, 0,   7,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(55229,   0,       4294966496, 135,  389,  0x0, 0,   8,   0,   0,   1,   0,   13,  255,  0)
    DeclNpc(55909,   0,       53659,   225,  389,  0x0, 0,   9,   0,   0,   2,   0,   14,  255,  0)
    DeclNpc(51729,   600,     52340,   180,  389,  0x0, 0,   10,  0,   255, 255, 0,   15,  255,  0)
    DeclNpc(3480,    0,       8439,    180,  389,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(3500,    0,       6590,    0,    389,  0x0, 0,   14,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(55250,   0,       4294965257, 0,    389,  0x0, 0,   11,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(55250,   0,       4294966257, 180,  389,  0x0, 0,   12,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(56090,   0,       53569,   225,  389,  0x0, 0,   9,   0,   0,   3,   0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(4294955227, 0,       3589,    0,    389,  0x0, 0,   16,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(4294957717, 0,       7340,    45,   389,  0x0, 0,   17,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(4294961196, 0,       10440,   1000,    4294962486, 1500,    11600,   0x007E, 0,  6,  0x0000)
    DeclActor(4390,    3750,    16900,   1000,    4390,    5000,    16900,   0x007C, 0,  26, 0x0000)
    DeclActor(5830,    0,       11730,   1200,    5830,    1500,    11730,   0x007C, 0,  27, 0x0000)

    ChipFrameInfo(1016, 0)                                       # 0

    ScpFunction((
        "Function_0_3F8",          # 00, 0
        "Function_1_4A8",          # 01, 1
        "Function_2_4D3",          # 02, 2
        "Function_3_4FE",          # 03, 3
        "Function_4_529",          # 04, 4
        "Function_5_909",          # 05, 5
        "Function_6_A9C",          # 06, 6
        "Function_7_AA0",          # 07, 7
        "Function_8_1BC2",         # 08, 8
        "Function_9_22AD",         # 09, 9
        "Function_10_2DA0",        # 0A, 10
        "Function_11_32FA",        # 0B, 11
        "Function_12_3415",        # 0C, 12
        "Function_13_34FA",        # 0D, 13
        "Function_14_3568",        # 0E, 14
        "Function_15_35EE",        # 0F, 15
        "Function_16_3682",        # 10, 16
        "Function_17_3826",        # 11, 17
        "Function_18_3A11",        # 12, 18
        "Function_19_3C55",        # 13, 19
        "Function_20_4009",        # 14, 20
        "Function_21_415C",        # 15, 21
        "Function_22_42FC",        # 16, 22
        "Function_23_44B9",        # 17, 23
        "Function_24_456A",        # 18, 24
        "Function_25_4654",        # 19, 25
        "Function_26_4F5C",        # 1A, 26
        "Function_27_4FBC",        # 1B, 27
        "Function_28_503B",        # 1C, 28
        "Function_29_65D3",        # 1D, 29
        "Function_30_6621",        # 1E, 30
        "Function_31_6AD7",        # 1F, 31
        "Function_32_780B",        # 20, 32
        "Function_33_7CC1",        # 21, 33
    ))


    def Function_0_3F8(): pass

    label("Function_0_3F8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_430"),
        (1, "loc_43C"),
        (2, "loc_448"),
        (3, "loc_454"),
        (4, "loc_460"),
        (5, "loc_46C"),
        (6, "loc_478"),
        (SWITCH_DEFAULT, "loc_484"),
    )


    label("loc_430")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_43C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_448")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_454")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_460")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_46C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_478")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_484")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_490")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_490")

    label("loc_4A7")

    Return()

    # Function_0_3F8 end

    def Function_1_4A8(): pass

    label("Function_1_4A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D2")
    OP_94(0xFE, 0xDE12, 0x122, 0xD0C0, 0xFFFFF07E, 0x3E8)
    Sleep(300)
    Jump("Function_1_4A8")

    label("loc_4D2")

    Return()

    # Function_1_4A8 end

    def Function_2_4D3(): pass

    label("Function_2_4D3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4FD")
    OP_94(0xFE, 0xDFFC, 0xDC82, 0xD548, 0xC922, 0x3E8)
    Sleep(300)
    Jump("Function_2_4D3")

    label("loc_4FD")

    Return()

    # Function_2_4D3 end

    def Function_3_4FE(): pass

    label("Function_3_4FE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_528")
    OP_94(0xFE, 0xDFCA, 0xDB74, 0xD4DA, 0xC454, 0x3E8)
    Sleep(300)
    Jump("Function_3_4FE")

    label("loc_528")

    Return()

    # Function_3_4FE end

    def Function_4_529(): pass

    label("Function_4_529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_574")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xA, -12070, 150, 11000, 0)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    Jump("loc_8E0")

    label("loc_574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5B6")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_8E0")

    label("loc_5B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_60B")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xA, -12070, 150, 11000, 0)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_8E0")

    label("loc_60B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6A1")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -12040, 150, 6900, 180)
    SetChrChipByIndex(0x15, 0x0)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrSubChip(0x15, 0x1)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0xF)
    SetChrPos(0x16, -10490, 0, 6320, 315)
    SetChrFlags(0x16, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_692")
    SetChrFlags(0x15, 0x10)

    label("loc_692")

    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_8E0")

    label("loc_6A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_70F")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CF")
    SetChrFlags(0xA, 0x10)

    label("loc_6CF")

    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x6)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0xA)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    Jump("loc_8E0")

    label("loc_70F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_764")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0xA, -12070, 150, 11000, 0)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75F")
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_75F")

    Jump("loc_8E0")

    label("loc_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_788")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x80)
    Jump("loc_8E0")

    label("loc_788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7E9")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0x10)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -12040, 150, 6900, 180)
    SetChrChipByIndex(0x18, 0x12)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    Jump("loc_8E0")

    label("loc_7E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_81C")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_817")
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_817")

    Jump("loc_8E0")

    label("loc_81C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_893")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xA, -12070, 150, 11000, 0)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -12040, 150, 6900, 180)
    SetChrFlags(0x18, 0x10)
    SetChrChipByIndex(0x18, 0x12)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    Jump("loc_8E0")

    label("loc_893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8C6")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BC")
    SetChrFlags(0x9, 0x10)

    label("loc_8BC")

    SetChrFlags(0xA, 0x10)
    Jump("loc_8E0")

    label("loc_8C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8E0")
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)

    label("loc_8E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_8F4")
    ClearScenarioFlags(0x22, 0)
    Event(0, 28)
    Jump("loc_908")

    label("loc_8F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_908")
    ClearScenarioFlags(0x22, 1)
    SetMapFlags(0x10000000)
    Event(0, 31)

    label("loc_908")

    Return()

    # Function_4_529 end

    def Function_5_909(): pass

    label("Function_5_909")

    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_92D")
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0F")

    label("loc_92D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_93B")
    Jump("loc_A0F")

    label("loc_93B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_954")
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0F")

    label("loc_954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_96D")
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0F")

    label("loc_96D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_97B")
    Jump("loc_A0F")

    label("loc_97B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_994")
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0F")

    label("loc_994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9A2")
    Jump("loc_A0F")

    label("loc_9A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9C6")
    OP_52(0x17, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0F")

    label("loc_9C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9D4")
    Jump("loc_A0F")

    label("loc_9D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9F8")
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0F")

    label("loc_9F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A06")
    Jump("loc_A0F")

    label("loc_A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A0F")

    label("loc_A0F")

    OP_52(0x16, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_A42")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A52")
    ClearMapObjFlags(0x2, 0x10)

    label("loc_A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A5F")
    OP_65(0x2, 0x1)

    label("loc_A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9B")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_A9B")

    Return()

    # Function_5_909 end

    def Function_6_A9C(): pass

    label("Function_6_A9C")

    Call(0, 7)
    Return()

    # Function_6_A9C end

    def Function_7_AA0(): pass

    label("Function_7_AA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AD7")
    Call(0, 33)
    Return()

    label("loc_AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE5")
    Call(0, 32)
    Return()

    label("loc_AE5")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BBE")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "To take a break\x01",        # 2
            "quit\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B65")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_B65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B84")
    OP_AF(0x5F)
    Jump("loc_BA6")

    label("loc_B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B94")
    OP_AF(0x5E)
    Jump("loc_BA6")

    label("loc_B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BA4")
    OP_AF(0x5D)
    Jump("loc_BA6")

    label("loc_BA4")

    OP_AF(0x5C)

    label("loc_BA6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BB9")

    label("loc_BB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD5")
    OP_AF(0x5A)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BB9")

    label("loc_BD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE9")
    Jump("loc_1BB9")

    label("loc_BE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BB9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_D8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_C9C")

    ChrTalk(
        0x8,
        (
            "Huhu, stew stew stew\x01",
            "Was it the best?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also for patients and outpatients\x01",
            "It's a reputation that I'm fine.\x01",
            "Come back to eat again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D87")

    label("loc_C9C")


    ChrTalk(
        0x8,
        (
            "The recommended food of our place is\x01",
            "Quite a while,\x01",
            "I need to simmer.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D39")

    ChrTalk(
        0x8,
        (
            "What is completed\x01",
            "It's about two days later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When that time comes\x01",
            "Do not forget to come.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D87")

    label("loc_D39")


    ChrTalk(
        0x8,
        (
            "What is completed\x01",
            "It's about tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because it is soon,\x01",
            "Do not forget to come.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D87")

    Jump("loc_1BB9")

    label("loc_D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAC")

    ChrTalk(
        0x8,
        (
            "Harold has notified you.\x01",
            "She seems to come to the hospital later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Almorica vegetables\x01",
            "I asked to bring a lot,\x01",
            "Finally I can make a decent meal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Rich food is more important than anything.\x01",
            "Patients will now\x01",
            "I will be fine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F74")

    label("loc_EAC")


    ChrTalk(
        0x8,
        (
            "ハロルドさんにAlmorica vegetables\x01",
            "I asked to bring a lot,\x01",
            "Finally I can make a decent meal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Rich food is more important than anything.\x01",
            "Patients will now\x01",
            "I will be fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F74")

    Jump("loc_1BB9")

    label("loc_F79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1016")

    ChrTalk(
        0x8,
        (
            "I'm staying here.\x01",
            "Even outpatient clinics gradually\x01",
            "It looks like I'm tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As soon as Crossbell City\x01",
            "I hope I can return it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB9")

    label("loc_1016")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_11B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_110B")

    ChrTalk(
        0x8,
        (
            "Food from the city\x01",
            "I am paid,\x01",
            "Basically there are many preserved foods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, even to make a hospital meal\x01",
            "The balance of nutrition is definitely\x01",
            "It gets worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There is no heart or patient\x01",
            "The facial expression of the foreigners is also dark … …\x01",
            "I want to manage somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11B1")

    label("loc_110B")


    ChrTalk(
        0x8,
        (
            "Just food supplied from the city\x01",
            "The balance of nutrition is definitely\x01",
            "It gets worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As in the past Almorika village\x01",
            "To be able to purchase fresh vegetables\x01",
            "I hope I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B1")

    Jump("loc_1BB9")

    label("loc_11B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_131D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129A")

    ChrTalk(
        0x8,
        (
            "Children of the city who are on the street,\x01",
            "It is a fan of alkane shell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I came to visit Iria,\x01",
            "Remaining in the hospital from the declaration of independence\x01",
            "He helped me a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hehe, a kind children were also there.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1318")

    label("loc_129A")


    ChrTalk(
        0x8,
        (
            "The young fans of Iria,\x01",
            "Remaining in the hospital from the declaration of independence\x01",
            "He helped me a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hehe, a kind children were also there.\x02",
    )

    CloseMessageWindow()

    label("loc_1318")

    Jump("loc_1BB9")

    label("loc_131D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_148B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_140B")

    ChrTalk(
        0x8,
        (
            "A hospital food menu is also available\x01",
            "I am in charge … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To this hospitalized patient,\x01",
            "Not enough to eat rice\x01",
            "Many people are injured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Food leads to vitality.\x01",
            "To be able to eat somehow\x01",
            "I want you to become it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1486")

    label("loc_140B")


    ChrTalk(
        0x8,
        (
            "Once, drip with nutrition\x01",
            "I wonder what they are doing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Food leads to vitality.\x01",
            "To be able to eat somehow\x01",
            "I want you to become it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1486")

    Jump("loc_1BB9")

    label("loc_148B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1605")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1589")

    ChrTalk(
        0x8,
        (
            "An ambulance gets outta easily\x01",
            "I thought it was something yesterday,\x01",
            "No way is it a train derailment accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Compensation or something\x01",
            "Although the railroad corporation is also in a hurry,\x01",
            "It was really nice for people to die.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even so ……\x01",
            "I wonder what the cause was?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1600")

    label("loc_1589")


    ChrTalk(
        0x8,
        (
            "Train accident,\x01",
            "I wonder what the cause was?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The person did not die\x01",
            "More than that,\x01",
            "Somehow it is anxious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1600")

    Jump("loc_1BB9")

    label("loc_1605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_16DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_169E")

    ChrTalk(
        0x8,
        (
            "If Arios,\x01",
            "I went back to the guild yesterday night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When Shizuku is in trouble,\x01",
            "You seem to be busy people after all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16D5")

    label("loc_169E")


    ChrTalk(
        0x8,
        (
            "Well, the meal to be given to the dormitory student tonight\x01",
            "What shall I do … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D5")

    Jump("loc_1BB9")

    label("loc_16DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_189E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E7")

    ChrTalk(
        0x8,
        (
            "Arios says,\x01",
            "For the operation of Shizuoka\x01",
            "I stayed here for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A wonderful father\x01",
            "I was accompanying you,\x01",
            "Shizuoka would have been encouraging.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, surgery itself is disappointing\x01",
            "That's right.\x01",
            "Ha … … I can not do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1899")

    label("loc_17E7")


    ChrTalk(
        0x8,
        (
            "Mr. Arios, stay for a while\x01",
            "I was accompanied by Shizuoka.\x01",
            "Well, I guess you were encouraging.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, surgery itself is disappointing\x01",
            "That's right.\x01",
            "Ha … … I can not do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1899")

    Jump("loc_1BB9")

    label("loc_189E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_19D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1963")

    ChrTalk(
        0x8,
        (
            "Today Mr. Erior of the haste fighter\x01",
            "It seems they came at work,\x01",
            "I served lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The hospital told the children\x01",
            "Oita I am indebted to you.\x01",
            "Thank you for replying at least.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19CD")

    label("loc_1963")


    ChrTalk(
        0x8,
        (
            "The hospital is also a hypocrite\x01",
            "Oita I am indebted to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sometimes it's about lunch service\x01",
            "I have to do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19CD")

    Jump("loc_1BB9")

    label("loc_19D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A71")

    ChrTalk(
        0x8,
        (
            "Dr. Albert,\x01",
            "At that young age of Remyria\x01",
            "He is the head of state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems that the people are also appreciated by the people … …\x01",
            "I guess you are an excellent one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB9")

    label("loc_1A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1BB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B5E")

    ChrTalk(
        0x8,
        (
            "There is a new researcher at the hospital\x01",
            "It seems that it increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Here, I'm a child of Michao.\x01",
            "Anything, in Crossbell City\x01",
            "I was studying by myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I love my hard work.\x01",
            "I have to serve with Dokan.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BB9")

    label("loc_1B5E")


    ChrTalk(
        0x8,
        "Well, I love my hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For newcomer kun\x01",
            "I have to serve with Dokan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB9")

    Jump("loc_AF2")

    label("loc_1BBE")

    TalkEnd(0x8)
    Return()

    # Function_7_AA0 end

    def Function_8_1BC2(): pass

    label("Function_8_1BC2")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1C4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE0")
    Call(0, 9)
    Jump("loc_1C4A")

    label("loc_1BE0")


    ChrTalk(
        0x9,
        (
            "Michao, a lot\x01",
            "Please do when you stomach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hey Hey, calm down and eat\x01",
            "I'm clogging my throat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C4A")

    Jump("loc_22A9")

    label("loc_1C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1CC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C6A")
    Call(0, 9)
    Jump("loc_1CC4")

    label("loc_1C6A")


    ChrTalk(
        0x9,
        (
            "…… Anyway, to us\x01",
            "I can not do anything ……\x01",
            "Let's concentrate on the hospital now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC4")

    Jump("loc_22A9")

    label("loc_1CC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE4")
    Call(0, 9)
    Jump("loc_1D5B")

    label("loc_1CE4")


    ChrTalk(
        0x9,
        (
            "Mr. Michao also\x01",
            "You became a summer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "While reading this book\x01",
            "You can not eat meals,\x01",
            "Even though it was noisy in the front.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D5B")

    Jump("loc_22A9")

    label("loc_1D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1E0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D7B")
    Call(0, 9)
    Jump("loc_1E09")

    label("loc_1D7B")


    ChrTalk(
        0x9,
        (
            "Continuing studies is important.\x01",
            "I gotta pick it up when I skim one day\x01",
            "It takes 3 days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The town may be worried,\x01",
            "Keep it in order.\x01",
            "……Good?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E09")

    Jump("loc_22A9")

    label("loc_1E0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1E73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E29")
    Call(0, 9)
    Jump("loc_1E6E")

    label("loc_1E29")


    ChrTalk(
        0x9,
        (
            "…, Sis, Michao also sit down.\x01",
            "I have to prepare for the afternoon as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E6E")

    Jump("loc_22A9")

    label("loc_1E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1F20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E8E")
    Call(0, 9)
    Jump("loc_1F1B")

    label("loc_1E8E")


    ChrTalk(
        0x9,
        (
            "Well, for evaluation\x01",
            "I will come with it later ……\x01",
            "Even if you get hurt you can increase work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For the time being, patients\x01",
            "I should be pleased that I was saved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F1B")

    Jump("loc_22A9")

    label("loc_1F20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1FA8")

    ChrTalk(
        0x9,
        (
            "Well, until today's lecture\x01",
            "I have a little time ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Michao has not come yet,\x01",
            "Would you like to go to self-study while taking breakfast?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22A9")

    label("loc_1FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2067")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC3")
    Call(0, 9)
    Jump("loc_2062")

    label("loc_1FC3")


    ChrTalk(
        0x9,
        (
            "Litton, from the time of the previous teaching professor\x01",
            "Because I was trying hard at death.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although I will not be beaten if I study too,\x01",
            "If only I tried that on site\x01",
            "It is strange that it does not grow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2062")

    Jump("loc_22A9")

    label("loc_2067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_211B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2082")
    Call(0, 9)
    Jump("loc_2116")

    label("loc_2082")


    ChrTalk(
        0x9,
        (
            "Munching …\x01",
            "Well, if I got a resident doctor\x01",
            "It's a road that everyone passes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Long time no see for ahead\x01",
            "You can not pull out, right?\x01",
            "Hehuu, I'll get used to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2116")

    Jump("loc_22A9")

    label("loc_211B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_218C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2136")
    Call(0, 9)
    Jump("loc_2187")

    label("loc_2136")


    ChrTalk(
        0x9,
        (
            "Michao,\x01",
            "First time to see surgery raw ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Huh … … Well, you look handsome.\x02",
    )

    CloseMessageWindow()

    label("loc_2187")

    Jump("loc_22A9")

    label("loc_218C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_22A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2252")

    ChrTalk(
        0x9,
        (
            "My new Michao's\x01",
            "I was given the guidance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, time for study\x01",
            "I will get scraped off … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, this is also a part of studying.\x01",
            "You are going to have a lot of fun and I'll do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22A9")

    label("loc_2252")


    ChrTalk(
        0x9,
        (
            "Well, cute junior's guidance also\x01",
            "It depends on my study.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You are going to have a lot of fun and I'll do it.\x02",
    )

    CloseMessageWindow()

    label("loc_22A9")

    TalkEnd(0x9)
    Return()

    # Function_8_1BC2 end

    def Function_9_22AD(): pass

    label("Function_9_22AD")

    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_23B6")

    ChrTalk(
        0x9,
        (
            "Michao,\x01",
            "Because many patients came\x01",
            "Please do when you stomach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Today, you are on site too\x01",
            "You'll work hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Ha ha, yes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Alright, I'll do it! It is!\x01",
            "Munching mushrooms …! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, I have to calm down and eat\x01",
            "I'm clogging my throat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D98")

    label("loc_23B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_24E3")

    ChrTalk(
        0x9,
        (
            "Is it an invalid declaration of an independent country …?\x01",
            "I wonder what will happen from now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway, in the old city\x01",
            "People in the apartment are worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Application for returning to the city, for a while\x01",
            "It seems I can not accept it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Anyway, to us\x01",
            "I can not do anything ……\x01",
            "Let's concentrate on the hospital now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "……is not it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D98")

    label("loc_24E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2626")

    ChrTalk(
        0x9,
        (
            "Munching …\x01",
            "So, as you can see in this illustration\x01",
            "Human internal organs …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Pu …\x01",
            "Hmm, I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Huhu, even so\x01",
            "Mr. Michao also\x01",
            "You became a summer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "While reading this book\x01",
            "You can not eat meals,\x01",
            "Even though it was noisy in the front.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Munching …\x01",
            "Haha, this is also my senior\x01",
            "It is an educational one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D98")

    label("loc_2626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_273E")

    ChrTalk(
        0x9,
        (
            "Michao,\x01",
            "Have you studied properly recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "that is……\x01",
            "Just a little with my hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When the crossbell is like this,\x01",
            "People in the apartment are also worried … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Is that so……\x01",
            "Perhaps it can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But, if you calm down\x01",
            "Keep it in order.\x01",
            "……Good?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D98")

    label("loc_273E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_286A")

    ChrTalk(
        0xA,
        (
            "Among the victims of the attack incident,\x01",
            "Some people just can not help …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Senior …… I, my heart seems to kiss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… I understand your feelings.\x01",
            "But, what makes you whining\x01",
            "Let's do it all over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If I had such time,\x01",
            "Even one person will help many patients.\x01",
            "That is our job.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    Jump("loc_2D98")

    label("loc_286A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_29DB")

    ChrTalk(
        0x9,
        "Haha, I finally got a breath.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even so,\x01",
            "Michao got a good job too\x01",
            "You seem to have helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, no.\x01",
            "I do not have much more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even if I told you to help me,\x01",
            "It was like choreography.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I do not humble it.\x01",
            "Even chores will be an important job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even if I look at the blood recently\x01",
            "It seems I got it ……\x01",
            "Was not he growing up a bit?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_2D98")

    label("loc_29DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2AF9")

    ChrTalk(
        0xA,
        (
            "Litton seniors,\x01",
            "Well for surgical assistants or rounds\x01",
            "You are driving me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ha, after all\x01",
            "With a newcomer I\x01",
            "I do not think deki is different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Litton, from the time of the previous teaching professor\x01",
            "Because I was trying hard at death.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, do not rush, do not hesitate.\x01",
            "If you want to grow study study.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_2D98")

    label("loc_2AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2C64")

    ChrTalk(
        0x9,
        "Puaku, mushrooms ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The reconstituted in was …, Michaud you.\x01",
            "If the order anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "No, that … ….\x01",
            "This morning, practical training on surgery\x01",
            "Was not there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "For the first time see real surgery,\x01",
            "Does not she have some appetite …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Oh, did not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Munching …\x01",
            "Well, it's a way for everyone\x01",
            "I'll get used to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "… …. UP\x01",
            "I hope that's it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D98")

    label("loc_2C64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2D98")

    ChrTalk(
        0x9,
        (
            "By the way, Misho - kun,\x01",
            "Tomorrow's Professor Gary\x01",
            "Surgical surgery training right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sure, I see real surgery\x01",
            "It was my first time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Well, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Geez, doctor's study in earnest\x01",
            "I feel like it is starting ~ is not it ~.\x01",
            "I am looking forward to it now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huh … … You are prone.\x01",
            "Well, I hope you do best at best.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)

    label("loc_2D98")

    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_22AD end

    def Function_10_2DA0(): pass

    label("Function_10_2DA0")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2DFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DBE")
    Call(0, 9)
    Jump("loc_2DF5")

    label("loc_2DBE")


    ChrTalk(
        0xA,
        (
            "Munching mushrooms …! It is!\x01",
            "Burst, burden …! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DF5")

    Jump("loc_32F6")

    label("loc_2DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2E7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E15")
    Call(0, 9)
    Jump("loc_2E77")

    label("loc_2E15")


    ChrTalk(
        0xA,
        (
            "I guess …. I can not go back to the city\x01",
            "It is a situation that can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "A little better if the situation turns better\x01",
            "Is it okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E77")

    Jump("loc_32F6")

    label("loc_2E7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2ED8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E97")
    Call(0, 9)
    Jump("loc_2ED3")

    label("loc_2E97")


    ChrTalk(
        0xA,
        (
            "Munching …\x01",
            "Haha, this is also my senior\x01",
            "It is an educational one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ED3")

    Jump("loc_32F6")

    label("loc_2ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2F64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EF3")
    Call(0, 9)
    Jump("loc_2F5F")

    label("loc_2EF3")


    ChrTalk(
        0xA,
        (
            "I agree……\x01",
            "People in the apartment are also worried … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I do not study it because of that\x01",
            "It may be amenable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F5F")

    Jump("loc_32F6")

    label("loc_2F64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2FE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F7F")
    Call(0, 9)
    Jump("loc_2FE1")

    label("loc_2F7F")


    ChrTalk(
        0xA,
        "… … Senpai said that ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway, now,\x01",
            "Even a single patient\x01",
            "I have to think about helping.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FE1")

    Jump("loc_32F6")

    label("loc_2FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3053")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3001")
    Call(0, 9)
    Jump("loc_304E")

    label("loc_3001")


    ChrTalk(
        0xA,
        (
            "Well, I'm not only miscellaneous\x01",
            "I must be able to handle important work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_304E")

    Jump("loc_32F6")

    label("loc_3053")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3061")
    Jump("loc_32F6")

    label("loc_3061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_30FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_307C")
    Call(0, 9)
    Jump("loc_30F9")

    label("loc_307C")


    ChrTalk(
        0xA,
        (
            "I see.\x01",
            "Even if you get upset, it will not start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "…… Senpai, that's it,\x01",
            "Anatomical books at meal time\x01",
            "It is better to quit after all …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30F9")

    Jump("loc_32F6")

    label("loc_30FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_318C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3119")
    Call(0, 9)
    Jump("loc_3187")

    label("loc_3119")


    ChrTalk(
        0xA,
        (
            "Uu, seniors after surgery\x01",
            "Often such meat dishes\x01",
            "You can eat it …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Uh, nicely when I remember … …\x02",
    )

    CloseMessageWindow()

    label("loc_3187")

    Jump("loc_32F6")

    label("loc_318C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3207")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31A7")
    Call(0, 9)
    Jump("loc_3202")

    label("loc_31A7")


    ChrTalk(
        0xA,
        "Haha, please leave it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Do not paint drones on your senior's face,\x01",
            "I am studying hard!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3202")

    Jump("loc_32F6")

    label("loc_3207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_32F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A8")

    ChrTalk(
        0xA,
        (
            "Senior Flora\x01",
            "It's a bit tough,\x01",
            "The way of teaching is very good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Knowledge is also deep,\x01",
            "Truly, a good senior\x01",
            "It was nice meeting you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_32F6")

    label("loc_32A8")


    ChrTalk(
        0xA,
        (
            "Flora seniors until the meal\x01",
            "To open a dissection book is\x01",
            "I wonder if they manage somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F6")

    TalkEnd(0xA)
    Return()

    # Function_10_2DA0 end

    def Function_11_32FA(): pass

    label("Function_11_32FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3411")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33DC")

    ChrTalk(
        0xFE,
        (
            "Our son,\x01",
            "I got hurt seriously at that raid incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Life was saved,\x01",
            "I am in an intensive care room ……\x01",
            "I was able to visit only a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, Goddess … …\x01",
            "Please help my son ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3411")

    label("loc_33DC")


    ChrTalk(
        0xFE,
        (
            "Oh, Goddess … …\x01",
            "Please help my son ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3411")

    TalkEnd(0xFE)
    Return()

    # Function_11_32FA end

    def Function_12_3415(): pass

    label("Function_12_3415")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_34F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34AE")

    ChrTalk(
        0xFE,
        (
            "My son fought with an armed group\x01",
            "I'm one of the security guards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… If this is the case,\x01",
            "To enter the guard\x01",
            "I should have opposed it … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_34F6")

    label("loc_34AE")


    ChrTalk(
        0xFE,
        (
            "…… If this is the case,\x01",
            "To enter the guard\x01",
            "I should have opposed it … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34F6")

    TalkEnd(0xFE)
    Return()

    # Function_12_3415 end

    def Function_13_34FA(): pass

    label("Function_13_34FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3564")

    ChrTalk(
        0xFE,
        (
            "Dad and mama, what is it\x01",
            "It looks sad all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "brother……\x01",
            "What's wrong?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3564")

    TalkEnd(0xFE)
    Return()

    # Function_13_34FA end

    def Function_14_3568(): pass

    label("Function_14_3568")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_35EA")

    ChrTalk(
        0xFE,
        (
            "Since the raid incident, the son and couple\x01",
            "You are hospitalized here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was able to confirm safety for the time being ….\x01",
            "I still feel calm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35EA")

    TalkEnd(0xFE)
    Return()

    # Function_14_3568 end

    def Function_15_35EE(): pass

    label("Function_15_35EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_367E")

    ChrTalk(
        0xFE,
        (
            "Such a case has happened,\x01",
            "Both the police and the guard have brought terrible damage … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on,\x01",
            "What will happen ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_367E")

    TalkEnd(0xFE)
    Return()

    # Function_15_35EE end

    def Function_16_3682(): pass

    label("Function_16_3682")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3693")
    Jump("loc_3822")

    label("loc_3693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3711")

    ChrTalk(
        0x10,
        (
            "Hospital food in Iria-sick room\x01",
            "I got to deliver … ….!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "How are you doing …?\x01",
            "What should I talk about when I meet? Is it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3822")

    label("loc_3711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_37A1")

    ChrTalk(
        0x10,
        (
            "If it is true, to reach the hospital room\x01",
            "I would like to cry out her name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "But here is a hospital ……\x01",
            "You should not do it unless you gaman it, truly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3822")

    label("loc_37A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3822")

    ChrTalk(
        0x10,
        (
            "Iria-sama's consciousness is back\x01",
            "It was really nice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Do not go back to the city, always here\x01",
            "It was worth praying for recovery!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3822")

    TalkEnd(0xFE)
    Return()

    # Function_16_3682 end

    def Function_17_3826(): pass

    label("Function_17_3826")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3837")
    Jump("loc_3A0D")

    label("loc_3837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_38DB")

    ChrTalk(
        0x11,
        (
            "お、落ち着けPolice……\x01",
            "Other hospitalized patients also\x01",
            "I have to deliver it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Rushing up to Ilya-sama's minutes\x01",
            "I will try it when I spill it.\x01",
            "A normal heart, a normal heart … …!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A0D")

    label("loc_38DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3981")

    ChrTalk(
        0x11,
        (
            "Iria-sama to cure soon even one day,\x01",
            "I'm also helping with an invitation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "That dorm manager is rough, but ……\x01",
            "If you think for Ilia-sama, it's a fart's kappa!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A0D")

    label("loc_3981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3A0D")

    ChrTalk(
        0x11,
        (
            "It's a tough time now,\x01",
            "Iria-sama's going to visit is\x01",
            "I have to go without gamans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "That much, helping the hospital\x01",
            "It is useless even a little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A0D")

    TalkEnd(0xFE)
    Return()

    # Function_17_3826 end

    def Function_18_3A11(): pass

    label("Function_18_3A11")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_3A22")
    Jump("loc_3C51")

    label("loc_3A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3A30")
    Jump("loc_3C51")

    label("loc_3A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3A3E")
    Jump("loc_3C51")

    label("loc_3A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3A4C")
    Jump("loc_3C51")

    label("loc_3A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3C51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A6F")
    Call(0, 19)
    TalkEnd(0xFE)
    SetChrSubChip(0x15, 0x1)
    Return()

    label("loc_3A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BA8")

    ChrTalk(
        0x15,
        (
            "#01300FWhen you are with Zeit,\x01",
            "It is very calm.\x02\x03",
            "#01304FI have not seen so many times,\x01",
            "Is it somewhat cozy …?\x02\x03",
            "#01300FShe seems to have been a longtime friend,\x01",
            "I feel such a nostalgic feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10400FAhaha, as if\x01",
            "It seems like a fateful lover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F(Maybe a little jealous ……)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3C49")

    label("loc_3BA8")


    ChrTalk(
        0x15,
        (
            "#01300FWhen Zeit is nearby,\x01",
            "It is very calm.\x02\x03",
            "#01304FIs it somewhat cozy …?\x01",
            "She seems to have been a longtime friend,\x01",
            "I feel such a nostalgic feeling.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C49")

    TalkEnd(0xFE)
    SetChrSubChip(0x15, 0x1)
    Return()

    label("loc_3C51")

    TalkEnd(0xFE)
    Return()

    # Function_18_3A11 end

    def Function_19_3C55(): pass

    label("Function_19_3C55")

    OP_4B(0x16, 0xFF)

    ChrTalk(
        0x15,
        (
            "#01300FBy the way, with Zeit\x01",
            "It was the past since that presidential speech day.\x02\x03",
            "#01303FI was taken by Arios\x01",
            "Following Ka'aa,\x01",
            "I just did not know where to go ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#3C#01200FWell, I was pursuing … …\x01",
            "As that \"sword san\" entered the lake,\x01",
            "It has been completely shaken off.\x02\x03",
            "I thought it was bad for Lloyd's,\x01",
            "In order to prepare for once\x01",
            "He was returning to his men.\x02\x03",
            "#01203FIf I think about it, in the place I was in that place\x01",
            "I was worried about you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#01302FKusu, I will be fine.\x01",
            "Mr. Zeit is better than that\x01",
            "I am glad that it was safe.\x02\x03",
            "#01300FBesides, I still have Lloyd and Waz\x01",
            "You are helping us a lot, do not you?\x02\x03",
            "#01304FHehe, Thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Cecilはツァイトの頭を優しく撫でた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x16, 0xFFFFFDA8, 2100, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        "#3C#01200F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#01303FHuhu, when you are with Zeit,\x01",
            "何故だかIt is very calm.\x02\x03",
            "#01305FOh … I'm sorry.\x01",
            "I got stroked like this carelessly,\x01",
            "Did you feel bad?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#3C#01200F…… Huh, no.\x01",
            "I did not feel bad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 1)
    ClearChrFlags(0x15, 0x10)
    OP_4C(0x16, 0xFF)
    Return()

    # Function_19_3C55 end

    def Function_20_4009(): pass

    label("Function_20_4009")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4158")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4027")
    Call(0, 19)
    Jump("loc_4158")

    label("loc_4027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40E9")

    ChrTalk(
        0x16,
        "#3C#01203F… … Huff ……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Zeit, what's wrong?\x01",
            "I was silent, but …).\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F（Cecilさんに撫でられて\x01",
            "Is she embarrassed? )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4158")

    label("loc_40E9")


    ChrTalk(
        0x16,
        (
            "#3C#01200F…… In order not to confuse the sick person,\x01",
            "Let's say I am waiting here.\x02\x03",
            "You ought to come and see yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4158")

    TalkEnd(0xFE)
    Return()

    # Function_20_4009 end

    def Function_21_415C(): pass

    label("Function_21_415C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_42F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_426E")

    ChrTalk(
        0xFE,
        (
            "My husband suffered from a sickness before this.\x01",
            "I hurried to come here with an ambulance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was glad that my application was managed.\x01",
            "Because the examination was rather rigorous,\x01",
            "I did hiyahiya if it was not good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha … … who was in this hospital as it is\x01",
            "I'd rather be relieved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_42F8")

    label("loc_426E")


    ChrTalk(
        0xFE,
        (
            "My husband suffered from a sickness before this.\x01",
            "I hurried to come here with an ambulance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha … … who was in this hospital as it is\x01",
            "I'd rather be relieved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42F8")

    TalkEnd(0xFE)
    Return()

    # Function_21_415C end

    def Function_22_42FC(): pass

    label("Function_22_42FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_44B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4403")

    ChrTalk(
        0xFE,
        (
            "Because I could not visit the hospital,\x01",
            "I have a chronic disease medicine out,\x01",
            "Have a seizure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is something called movement restriction of the highway\x01",
            "I found out how hard it was to get through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next to return to the city, the defense army will come\x01",
            "I need to wait … ….\x01",
            "Should I take it easy for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_44B5")

    label("loc_4403")


    ChrTalk(
        0xFE,
        (
            "By being carried to the hospital this time,\x01",
            "There is something called movement restriction of the highway\x01",
            "I found out how hard it was to get through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next to return to the city, the defense army will come\x01",
            "I need to wait … ….\x01",
            "Should I take it easy for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44B5")

    TalkEnd(0xFE)
    Return()

    # Function_22_42FC end

    def Function_23_44B9(): pass

    label("Function_23_44B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4566")

    ChrTalk(
        0xFE,
        (
            "I planned to return to the town today ….\x01",
            "How the hell do you get together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I do not know what the invalid declaration is,\x01",
            "Eagle one took me to the town\x01",
            "The bee will not work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4566")

    TalkEnd(0xFE)
    Return()

    # Function_23_44B9 end

    def Function_24_456A(): pass

    label("Function_24_456A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_457B")
    Jump("loc_4650")

    label("loc_457B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4650")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4596")
    Call(0, 30)
    Jump("loc_4650")

    label("loc_4596")


    ChrTalk(
        0xFE,
        (
            "\"Blue flower\" with the report\x01",
            "To investigate the causal relationship with the eidolon,\x01",
            "I'm going to Nakasu on the Ursula interstate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, do not worry about us.\x01",
            "You guys are going to work for you\x01",
            "It is good to concentrate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4650")

    TalkEnd(0xFE)
    Return()

    # Function_24_456A end

    def Function_25_4654(): pass

    label("Function_25_4654")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4665")
    Jump("loc_4F58")

    label("loc_4665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_484E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4680")
    Call(0, 30)
    Jump("loc_4849")

    label("loc_4680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47B2")

    ChrTalk(
        0xFE,
        (
            "Kohon, that remembered,\x01",
            "It's that blue flower ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In your report,\x01",
            "To that \"Gnostic\" material\x01",
            "You seem to have been getting on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mastermind Joachim Günter\x01",
            "Lots of medicines in the cult incident\x01",
            "She seems to have been producing it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The material \"pre-prime weed\"\x01",
            "I wonder where they were buying.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_4849")

    label("loc_47B2")


    ChrTalk(
        0xFE,
        (
            "Joachim Günter\x01",
            "A large amount of Gnostic in a cult incident\x01",
            "She seems to have been producing it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The material \"pre-prime weed\"\x01",
            "I wonder where they were buying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4849")

    Jump("loc_4F58")

    label("loc_484E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_485C")
    Jump("loc_4F58")

    label("loc_485C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD0")

    ChrTalk(
        0x101,
        "#00005FThat, Aeolianness ──\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x103, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_493C")
    Jump("loc_4986")

    label("loc_493C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_495C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4986")

    label("loc_495C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_497C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4986")

    label("loc_497C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4986")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "#4STe, Tio Chan ……\x01",
            "You finally came home! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F… …. Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ahh ……\x01",
            "How many times have you dreamed of this day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come this way, Tio!\x01",
            "My sister tucks up! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F… … firm, refuse.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Huh, this feeling is also a long time … … spray\x02",
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
        0x103,
        (
            "#00211F(… …. why, than before\x01",
            "I feel I became a strong enemy. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Hahaha … while I could not meet you\x01",
            "I wonder if my feelings were piled up. )\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetScenarioFlags(0x1C0, 7)
    Jump("loc_4F58")

    label("loc_4BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DF2")
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x103, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C6B")
    Jump("loc_4CB5")

    label("loc_4C6B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C8B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CB5")

    label("loc_4C8B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CAB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CB5")

    label("loc_4CAB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4CB5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "At the request came to deliver the package\x01",
            "I can not wait to see Tio - chan …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I guess this is destiny! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211Fwrong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Answer ___ ___ 0\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FMr. Eoria,\x01",
            "Then, with me …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No, no needless spray\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FGokutama ……\x01",
            "Immediately here! Is it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_4F54")

    label("loc_4DF2")

    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x103, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E83")
    Jump("loc_4ECD")

    label("loc_4E83")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4EA3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4ECD")

    label("loc_4EA3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4EC3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4ECD")

    label("loc_4EC3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4ECD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Hehe, Tio.\x01",
            "Let me skin ship next time\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F(You still need attention …… and.)\x02",
    )

    CloseMessageWindow()

    label("loc_4F54")

    SetChrSubChip(0xFE, 0x0)

    label("loc_4F58")

    TalkEnd(0xFE)
    Return()

    # Function_25_4654 end

    def Function_26_4F5C(): pass

    label("Function_26_4F5C")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "3rd floor: female staff dormitory →\x01\x01",
            "←２階：male職員寮\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_4F5C end

    def Function_27_4FBC(): pass

    label("Function_27_4FBC")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "Outpatient · outpatient accommodation\x01",
            "※ Please tell the dormitory manager when you use\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_4FBC end

    def Function_28_503B(): pass

    label("Function_28_503B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch03102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch08500.itc", 0x21)
    LoadChrToIndex("chr/ch08502.itc", 0x22)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -13250, 100, 3800, 0)
    SetChrChipByIndex(0x105, 0x1F)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x105, -12250, 100, 3800, 0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, -13650, 100, 6800, 180)
    ClearChrFlags(0x15, 0x80)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, -12900, 100, 6800, 180)
    SetChrChipByIndex(0x19, 0x22)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -12150, 100, 6800, 180)
    SetChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x107, 0xF)
    SetChrSubChip(0x107, 0x0)
    SetChrPos(0x107, -10500, 0, 4500, 315)
    BeginChrThread(0x107, 3, 0, 0)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)
    OP_68(3690, 1500, 8400, 0)
    MoveCamera(36, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(26610, 0)
    FadeToBright(1000, 0)
    OP_68(-12150, 1500, 5120, 7000)
    MoveCamera(47, 28, 0, 7000)
    OP_6E(440, 7000)
    SetCameraDistance(26610, 7000)
    OP_6F(0x79)
    Fade(500)
    OP_68(-13080, 1500, 4550, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18910, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x103,
        "#00206F#5P…… Such a thing ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#06406F#5PSomething is too spectacular\x01",
            "I will not come with pins ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#01303F#5PWe live in Crossbell ……\x02\x03",
            "#01308FThere were various circumstances in the past\x01",
            "I knew that it is now.\x02\x03",
            "#01301FEven this situation, Ka'a-chan's thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#12P……Ah.\x02\x03",
            "#00003FI only have two things.\x02\x03",
            "The truth that has not been seen yet\x01",
            "To make sure with this eye ─\x02\x03",
            "#00013FAnd liberate everyone\x01",
            "It is to regain Ka'aa.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x105, 0x1)
    Sleep(150)

    ChrTalk(
        0x105,
        (
            "#10409F#12PJuff, saying only two\x01",
            "It seems to be terribly troublesome though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01203F#11P#3CWell, it seems.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#5PHehu ……\x01",
            "Because that is Lloyd.\x02\x03",
            "#00204F── My heart also\x01",
            "It is the same as Lloyd's.\x02\x03",
            "#00203FAs a member of the support department ……\x02\x03",
            "#00201FMore than anything as a guardian of Kea\x01",
            "Please take me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PThank you, Tio.\x01",
            "Do not hesitate to have the power to lend me.\x02\x03",
            "#00005FBut why is Tio\x01",
            "You brought me here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#5P… … Maybe, Mariavell?\x01",
            "I think that it is the direction of Mr. Arios.\x02\x03",
            "#00208FMembers of the support department divided\x01",
            "Monitor each in different places …\x02\x03",
            "#00201FIf you leave it poorly together\x01",
            "We might unite and encourage Ka'aa\x01",
            "It seemed to have been thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PI see……\x02\x03",
            "#00008FAnd Ellie and Randy also\x01",
            "They seem to be in different places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PWell, if I was in Crosbell City\x01",
            "It is impossible to release it ….\x02\x03",
            "#10402FTio's here and there,\x01",
            "It seems likely that you are out of town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#01306F#5PWell … … to four people Kia-chan\x01",
            "It seems like I try not to approach it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x19)
    Sleep(500)
    MoveCamera(34, 18, 0, 1000)
    Sound(812, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0x19, 0x21)
    SetChrPos(0x19, -12150, 0, 6400, 180)
    OP_0D()

    def lambda_5796():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_5796)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x19,
        (
            "#06403F#5PHey, hey …!\x02\x03",
            "#06401FI too\x01",
            "Will you take me with you! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(50)
    SetChrSubChip(0x15, 0x1)
    Sleep(50)
    SetChrSubChip(0x101, 0x2)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00005F#6PFranc……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#01305F#5PFrancさん？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#06406F#5PI, like you guys\x01",
            "I can not fight, but ……\x02\x03",
            "#06403FStill if the operator\x01",
            "I think I can do it so much!\x02\x03",
            "#06401FAnything with Mr. Wasi's flying boat\x01",
            "I heard he is traveling … and\x02\x03",
            "please……!\x01",
            "I want you to help me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PFranc……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x0)
    Sleep(150)

    ChrTalk(
        0x103,
        "#00208F#5PMr. Lloyd ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PWell, certainly \"Mercapa\"\x01",
            "I am saved because it is too much for me.\x02\x03",
            "#10400FAll this\x01",
            "I have to decide Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00006F#6P… … That's right.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00003F#6PFranc──君のお姉さんは\x01",
            "Currently I work at the Defense Forces.\x02\x03",
            "#00008FComing with us is\x01",
            "Girlfriend#4RNoel#To confront with … …\x02\x03",
            "#00001FDo you know that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#06406F#5P… …. Yes, …!\x02\x03",
            "#06408FOf course, with my sister\x01",
            "I do not want to fight … …\x02\x03",
            "#06401FStill … even me\x01",
            "Crossbell is a police officer of the police!\x02\x03",
            "Such a crisis situation …\x01",
            "I can not leave it alone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PReally……\x02\x03",
            "#00002F── I understood.\x01",
            "I'm begging for your cooperation.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x19,
        "#06409F#5POh, thank you!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(100)

    ChrTalk(
        0x103,
        (
            "#00202F#5PFrancさん……\x01",
            "It was good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#12PHuff, Abbas' work also\x01",
            "I guess it will be easier a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#01309F#5PHehu ……\x01",
            "The story seems to be settled.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    OP_93(0x19, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00000F#12PAh……\x01",
            "そろそろ行くよ、Cecil姉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#01304F#5PWell, be careful again.\x02\x03",
            "#01303FI, directly to the power of everyone\x01",
            "I can not do it, though …\x02\x03",
            "#01302FWhile working here\x01",
            "I pray for everyone's safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PThank you.\x01",
            "… That's enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#5P……Cecilさん。\x01",
            "Thank you for your kindness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#06411F#11PWow, I ….\x01",
            "I have been indebted to you for a long time.\x02\x03",
            "#06406F#30WGou … … Uu … …\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x15, 0x1)
    Sleep(150)

    ChrTalk(
        0x15,
        (
            "#01309F#5PHuh, you messed up a cute face?\x02\x03",
            "#01305FそういえばFrancさん、\x01",
            "Do not you have to pack your luggage?\x02\x03",
            "#01302FThe one who took about changing clothes\x01",
            "I wonder if it is okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x19,
        "#06405F#11PWell, I have to pack up in a hurry!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x101, 500)

    ChrTalk(
        0x19,
        (
            "#06412F#5PJust a bit.\x01",
            "Please wait!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    BeginChrThread(0x19, 0, 0, 29)
    OP_68(-12440, 1500, 5080, 3500)
    MoveCamera(62, 19, 0, 3500)
    OP_6E(440, 3500)
    SetCameraDistance(21000, 3500)
    Sleep(200)
    SetChrSubChip(0x105, 0x2)
    Sleep(200)
    SetChrSubChip(0x101, 0x2)
    Sleep(3800)
    OP_68(-13080, 1500, 4550, 3000)
    MoveCamera(39, 20, 0, 3000)
    OP_6E(440, 3000)
    SetCameraDistance(18910, 3000)
    Sleep(1000)
    SetChrSubChip(0x105, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    SetChrSubChip(0x15, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00002F#12Pmy mother……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#11P#3CHm, quite\x01",
            "It is going to be lively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#12PAlso in Mercapa\x01",
            "It looks a little glamorous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#01304F#5PHehu ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x15,
        (
            "#01305F#5Pby the way……\x02\x03",
            "#01300FWhile waiting for it,\x01",
            "To Iria and Donovan\x01",
            "Do you even greet?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#12PHuh……! Is it?\x01",
            "Perhaps both of us …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#01304F#5PWell, I woke up safely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#5PIf you are Iria\x01",
            "I do not seem to be able to walk yet ….\x02\x03",
            "#00202FIf you are a Donovan policeman\x01",
            "It seems to be recovering smoothly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#12PI see … it was good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#12PJust why are you waiting\x01",
            "Shall we disturb you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#12POh, let's do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5PI am going out with you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#11P#3CBecause it seems to confuse hum, sick people\x01",
            "Shall I wait here?\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19160, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Zeit withdrew from the party at once.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tio joined the party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_32(0xFF, 0xF9, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -12040, 150, 6900, 180)
    SetChrChipByIndex(0x15, 0x0)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrSubChip(0x15, 0x1)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0xF)
    SetChrPos(0x16, -10490, 0, 6320, 315)
    SetChrFlags(0x16, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_658E")
    SetChrFlags(0x15, 0x10)

    label("loc_658E")

    SetChrPos(0x0, -10000, 0, 2500, 90)
    OP_69(0xFF, 0x0)
    SetChrFlags(0x19, 0x80)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x8)
    OP_C9(0x1, 0x10000)
    OP_50(0x52, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x21, 5)
    SetScenarioFlags(0x1A0, 5)
    OP_29(0xAF, 0x1, 0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_28_503B end

    def Function_29_65D3(): pass

    label("Function_29_65D3")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x8000)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xFA0, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x138, 0x3E80, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x10B, 0x1F40, 0x1388, 0x1)
    Return()

    # Function_29_65D3 end

    def Function_30_6621(): pass

    label("Function_30_6621")

    EventBegin(0x0)
    Fade(500)
    OP_68(-10410, 1400, 5420, 0)
    MoveCamera(41, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18740, 0)
    SetChrPos(0x101, -9460, 0, 4970, 277)
    SetChrPos(0x102, -8430, 0, 6280, 277)
    SetChrPos(0x103, -9710, 0, 6350, 277)
    SetChrPos(0x104, -8540, 0, 5090, 277)
    SetChrPos(0x109, -9270, 0, 7610, 232)
    SetChrPos(0x105, -8750, 0, 3940, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x17, 0x2)
    SetChrSubChip(0x18, 0x1)
    OP_0D()

    ChrTalk(
        0x18,
        "#5POh, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FMr. Lin, Mr. Aoria … …\x01",
            "I was in Ursula hospital, did not he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00100FDid you have any requests?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#6PNo, I am going to investigate the eidolon from now,\x01",
            "I am preparing for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#6PFrom now on, you have got rid of the eidolon\x01",
            "I'm going to Nakasu on the Ursula interstate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#6P\"Blue flower\" with the report\x01",
            "To investigate the causal relationship with the eidolon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#5Pちなみに復帰したArios says,\x01",
            "The rest of the eyewitness witnessed\x01",
            "I'm getting rid of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10105FOh really……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#00300FIs there something I can help with?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#5PNo, I do not mind letting me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#5PBut yes, when I came back\x01",
            "If you can skin with Tio,\x01",
            "I think I can do as much as I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4S#11P#00203FWe refuse.\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x18,
        "#5PKyan, that kind of … ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FAhaha, as usual.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#6PWell, I do not need to worry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#6PYou guys are\x01",
            "Do what you can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FYes, I understand.\x01",
            "Please do your best also there.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x17A, 2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -9520, 0, 6040, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x17, 0x0)
    SetChrSubChip(0x18, 0x0)
    EventEnd(0x5)
    Return()

    # Function_30_6621 end

    def Function_31_6AD7(): pass

    label("Function_31_6AD7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch02902.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x1)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    OP_68(-12750, 2200, 5380, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x15, -11900, 200, 6850, 180)
    SetChrPos(0x105, -12800, 200, 6850, 180)
    SetChrPos(0x102, -13700, 200, 6850, 180)
    SetChrPos(0x101, -11900, 200, 3600, 0)
    SetChrPos(0x109, -12800, 200, 3600, 0)
    SetChrPos(0x104, -13700, 200, 3600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-12750, 1000, 5380, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(500)

    ChrTalk(
        0x15,
        (
            "#5P#01300F……Well then,\x01",
            "Tio is in a little while\x01",
            "You can not come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FOh, variety\x01",
            "It seems to be busy.\x02\x03",
            "#00002FSurely, around this time, in Les Autonomous states\x01",
            "I guess I'm doing my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5P#01304FI see……\x01",
            "Well then, I'm looking forward to seeing you.\x02\x03",
            "#01309FHuhu, when I return home\x01",
            "I have to tell you souvenir stories a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FHaha … That's right.\x02\x03",
            "#00000FTio also surely,\x01",
            "Cecil姉に会えたら喜ぶと思うよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x0)
    Sleep(100)
    SetChrSubChip(0x109, 0x2)
    OP_63(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x105)
    OP_64(0x109)

    ChrTalk(
        0x109,
        "#6P#10105FOh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10304FWell ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        "#12P#00005FWhat are you two, both of us.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)

    ChrTalk(
        0x109,
        (
            "#6P#10109FGood, gee …\x01",
            "I have heard rumors,\x01",
            "You really are on good terms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10302FIt's hard to get in there\x01",
            "I feel a little jealous.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00006FOh, that, …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FHey, Guys\x01",
            "Because it is this.\x02\x03",
            "#00301FNormally, with this older sister\x01",
            "Even if I only know people since I was a child\x01",
            "Tonna is lucky bastard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00106FReally, right.\x02\x03",
            "#00111FIf you think that it is natural\x01",
            "Someday my boss will fall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FWell, I do not understand the meaning ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#5P#01309FWhatching\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x15,
        (
            "#5P#01305FOh, that's right.\x01",
            "I talked to him a lot ……\x02\x03",
            "#01300FFor what purpose today to the hospital\x01",
            "I wonder if he came.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x109, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)

    ChrTalk(
        0x101,
        (
            "#12P#00005FAh … that was right.\x02\x03",
            "#00000F…… Kohon, in fact … …\x01",
            "From people like Professor Seyland\x01",
            "The request came to the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FCertainly, people succeeding pharmacology and neurology are\x01",
            "You were able to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5P#01302FWell, that's right.\x02\x03",
            "#01303FMr. Joachim may be acquainted\x01",
            "It was announced that I was making medicine,\x01",
            "The hospital was a bit noisy at one time.\x02\x03",
            "#01308FFor a while,\x01",
            "Besides work, after-care\x01",
            "I was busy … ….\x02\x03",
            "#01300FRecently, finally\x01",
            "I regained patient trust.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FAbsolutely …\x01",
            "It was hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5P#01309FWhatching\x01",
            "Thanks to you I managed to do something.\x02\x03",
            "#01300FThe scars of that incident have also healed,\x01",
            "Finally Ursula Hospital\x01",
            "I took a new step.\x02\x03",
            "As a part of it,\x01",
            "Newly from Remiferia\x01",
            "Professor Seyland was called.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00100FThat famous medical equipment maker,\x01",
            "Islamic concerned … … is not it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x2)

    ChrTalk(
        0x15,
        (
            "#11P#01300FYes, to relatives of the founder\x01",
            "You should be wearing it.\x02\x03",
            "#01304FI am a woman,\x01",
            "The atmosphere is dignified\x01",
            "It's so cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FOh, the female doctor Sensei!\x01",
            "This is great expectation!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FBesides the atmosphere ……\x02\x03",
            "#00000FI see, this time\x01",
            "Identity perfectly\x01",
            "That's guaranteed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10300FAs a hum, professor,\x01",
            "Are my arms certain?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#01300FEven in Remiferia\x01",
            "It seems to be a famous researcher in pharmacy and neurology.\x02\x03",
            "#01304FIn the meantime, too heavy illness\x01",
            "The operation of Mikhail who was hospitalized\x01",
            "You made it successful.\x02\x03",
            "#01300FToday, for the operation of Shizuku-chan\x01",
            "You are preparing for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00105FSuzuku's … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FReally……\x01",
            "It certainly sounds like a great teacher.\x02\x03",
            "That Professor Isale … …\x01",
            "Do you know where I am now?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x15,
        (
            "#5P#01300FYes, most of the research building\x01",
            "I'm in the laboratory.\x02\x03",
            "To Sera at the reception,\x01",
            "I think you can get involved.\x02\x03",
            "#01309FHuhu, that's so hard\x01",
            "Let's go there together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FOh, it will be saved.\x01",
            "… Well then let's go.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t1530", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_6AD7 end

    def Function_32_780B(): pass

    label("Function_32_780B")

    EventBegin(0x0)
    Fade(500)
    OP_68(-6500, 1000, 9690, 0)
    MoveCamera(72, 25, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -7150, 0, 9330, 45)
    SetChrPos(0x102, -8240, 0, 9720, 45)
    SetChrPos(0x103, -6600, 0, 8189, 45)
    SetChrPos(0x109, -8980, 0, 8720, 45)
    SetChrPos(0x105, -7760, 0, 7150, 45)
    SetChrPos(0x104, -7950, 0, 8280, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Come, please come.\x01",
            "Would you like to eat something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse me,\x01",
            "I am a person in the mission support department … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the interview with \"One push gourmet\"\x01",
            "I explained what came.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Oh, the story of the gourmet guide.\x01",
            "I heard from people of the communication company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "…… But I was in trouble.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FIs there something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "ウチのお勧め料理はQuite a while,\x01",
            "I need to boil it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Before this, just leaving that\x01",
            "It's gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's bad, but now\x01",
            "Ready to act on you\x01",
            "I do not have it in place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303FHmm, that's it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FBy the time it is completed\x01",
            "How long will it take?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B84")

    ChrTalk(
        0x8,
        (
            "That's right, since last night\x01",
            "It is the place where I started tying … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Two days after completion,\x01",
            "It will be the day after tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BD3")

    label("loc_7B84")


    ChrTalk(
        0x8,
        (
            "That's right, from the day before yesterday\x01",
            "It is the place where I started tying … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "It is tomorrow to complete.\x02",
    )

    CloseMessageWindow()

    label("loc_7BD3")


    ChrTalk(
        0x109,
        "#10105FMi, are you stewing for three days …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHuhu, it seems that the taste is stained.\x01",
            "I am looking forward to finishing this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, surely it should be delicious.\x01",
            "完成する頃になったらDo not forget to come.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    OP_29(0x80, 0x1, 0x9)
    SetScenarioFlags(0x179, 1)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -6960, 0, 9540, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_32_780B end

    def Function_33_7CC1(): pass

    label("Function_33_7CC1")

    EventBegin(0x0)
    Fade(500)
    OP_68(-6500, 1000, 9690, 0)
    MoveCamera(72, 25, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -7150, 0, 9330, 45)
    SetChrPos(0x102, -8240, 0, 9720, 45)
    SetChrPos(0x103, -6600, 0, 8189, 45)
    SetChrPos(0x109, -8980, 0, 8720, 45)
    SetChrPos(0x105, -7760, 0, 7150, 45)
    SetChrPos(0x104, -7950, 0, 8280, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 1)), scpexpr(EXPR_END)), "loc_7EA8")

    ChrTalk(
        0x8,
        (
            "Oh, you guys.\x01",
            "You seem to have not forgotten.\x02",
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
        0x101,
        "#00005FAnd, to say … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, our recommended cuisine\x01",
            "\"Three days simmered stew\"\x01",
            "It was finally completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Would you like to eat it immediately?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8014")

    label("loc_7EA8")


    ChrTalk(
        0x8,
        (
            "Come, please come.\x01",
            "Would you like to eat something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse me,\x01",
            "I am a person in the mission support department … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the interview with \"One push gourmet\"\x01",
            "I explained what came.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Oh, the story of the gourmet guide.\x01",
            "I heard from people of the communication company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "No, it came just right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "About a while ago, our recommended cuisine\x01",
            "\"Three days simmered stew\"\x01",
            "It was completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Would you like to eat it immediately?\x02",
    )

    CloseMessageWindow()

    label("loc_8014")


    ChrTalk(
        0x103,
        "#00200FYes, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well then, wait a moment.\x01",
            "I will give you a number of people now.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6E(380, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd 's ate stewed stew for three days.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x109,
        "#10105F#4S…… Oh, tasty … …! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FOh …… Small Trotoro,\x01",
            "The taste is messed up.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 1)), scpexpr(EXPR_END)), "loc_8215")

    ChrTalk(
        0x105,
        "#10302FHuh, it was worth the wait.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8253")

    label("loc_8215")


    ChrTalk(
        0x105,
        (
            "#10302FHuh, on such a rainy day\x01",
            "It might be the best meal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8253")


    ChrTalk(
        0x102,
        (
            "#00100FYeah, really … ….\x01",
            "Such a delicious stew,\x01",
            "It may be the first time in my life …!\x02\x03",
            "#00103FMy body also warms up and I have plenty of nutrition\x01",
            "I wonder if it's good for your body.\x02\x03",
            "#00109FEven sick people just eat this\x01",
            "It looks like she will get better soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(500)
    TurnDirection(0x101, 0x102, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00009FIt looks like a very happy face …\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)

    ChrTalk(
        0x8,
        "Haha, that is exaggerating.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    ChrTalk(
        0x103,
        (
            "#00200FEly is awesome\x01",
            "It seems I liked it … ….\x01",
            "I heard that you can leave the article here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, that's right.\x01",
            "Elly, can you ask?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#00100FYeah, please leave it to me.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x173, 1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_84C7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_84E4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_84F7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_850A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_850A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_8527")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_853A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_853A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_8557")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_856A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_856A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_8587")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_859A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_859A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_85B7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_85B7")

    OP_29(0x80, 0x1, 0xA)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86BA")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I finished interviewing 6 dining places!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_86B1")

    AnonymousTalk(
        0x101,
        (
            "#00003FMr. Grace right away\x01",
            "It seems I can go to the report … but …\x02\x03",
            "#00000FThe favorite of all six people still\x01",
            "It was not found.\x01",
            "Maybe I'll try harder?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_86B1")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_86BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_878B")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "All members of the Special Affairs Support Division\x01",
            "I found a favorite!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this all six people\x01",
            "I found a favorite.\x02\x03",
            "This is enough for the interview.\x01",
            "Let's go report to the airlines immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_878B")

    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0xE1, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -6960, 0, 9540, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_33_7CC1 end

    SaveToFile()

Try(main)
