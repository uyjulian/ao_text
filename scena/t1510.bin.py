from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Dormitory Superintendent Kilsch",# 1
        "Medical Intern Flora",   # 2
        "Medical Intern Micheau", # 3
        "Visitor",                # 4
        "Visitor",                # 5
        "Visitor",                # 6
        "Visitor",                # 7
        "Visitor",                # 8
        "Polise",                 # 9
        "Tap",                    # 10
        "Visitor",                # 11
        "Young Man",              # 12
        "Visitor",                # 13
        "Cecil",                  # 14
        "Divine Wolf Zeit",       # 15
        "Bracer Ling",            # 16
        "Bracer Eolia",           # 17
        "Fran",                   # 18
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
        "Function_8_1DA8",         # 08, 8
        "Function_9_2581",         # 09, 9
        "Function_10_3203",        # 0A, 10
        "Function_11_381F",        # 0B, 11
        "Function_12_393F",        # 0C, 12
        "Function_13_3A5F",        # 0D, 13
        "Function_14_3AEC",        # 0E, 14
        "Function_15_3B8E",        # 0F, 15
        "Function_16_3C33",        # 10, 16
        "Function_17_3E34",        # 11, 17
        "Function_18_4079",        # 12, 18
        "Function_19_42EF",        # 13, 19
        "Function_20_46AF",        # 14, 20
        "Function_21_4819",        # 15, 21
        "Function_22_4A30",        # 16, 22
        "Function_23_4C8D",        # 17, 23
        "Function_24_4D66",        # 18, 24
        "Function_25_4E6B",        # 19, 25
        "Function_26_5801",        # 1A, 26
        "Function_27_5868",        # 1B, 27
        "Function_28_5902",        # 1C, 28
        "Function_29_6FA0",        # 1D, 29
        "Function_30_6FEE",        # 1E, 30
        "Function_31_74E0",        # 1F, 31
        "Function_32_82CF",        # 20, 32
        "Function_33_87C6",        # 21, 33
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DA4")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Rest\x01",        # 2
            "Cancel\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B53")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_B53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B72")
    OP_AF(0x5F)
    Jump("loc_B94")

    label("loc_B72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B82")
    OP_AF(0x5E)
    Jump("loc_B94")

    label("loc_B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B92")
    OP_AF(0x5D)
    Jump("loc_B94")

    label("loc_B92")

    OP_AF(0x5C)

    label("loc_B94")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D9F")

    label("loc_BA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC3")
    OP_AF(0x5A)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D9F")

    label("loc_BC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD7")
    Jump("loc_1D9F")

    label("loc_BD7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D9F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_D9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_CA9")

    ChrTalk(
        0x8,
        (
            "Haha, my well-boiled\x01",
            "stew was the best,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's popular among the patients and\x01",
            "visitors, who say it gives them\x01",
            "energy. Come have it again sometime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D97")

    label("loc_CA9")


    ChrTalk(
        0x8,
        (
            "My recommended dish\x01",
            "needs quite some time to\x01",
            "boil.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D47")

    ChrTalk(
        0x8,
        (
            "It'll be ready in about\x01",
            "two days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Don't forget to visit\x01",
            "when the time comes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D97")

    label("loc_D47")


    ChrTalk(
        0x8,
        "It'll be ready tomorrow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's almost ready, so\x01",
            "don't forget to visit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D97")

    Jump("loc_1D9F")

    label("loc_D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_FC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE1")

    ChrTalk(
        0x8,
        (
            "I got a call from Mr.\x01",
            "Harold. He said he'll come\x01",
            "to the hospital later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I asked him to bring me a lot of\x01",
            "vegetables from Armorica so it looks like\x01",
            "I'll finally be able to make proper meals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A rich meal is the most important\x01",
            "thing. With this, the patients\x01",
            "will probably cheer up too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FC0")

    label("loc_EE1")


    ChrTalk(
        0x8,
        (
            "I asked Mr. Harold to bring me a lot of\x01",
            "vegetables from Armorica so it seems I'll\x01",
            "finally be able to make proper meals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A rich meal is the most important\x01",
            "thing. With this, the patients\x01",
            "will probably cheer up too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FC0")

    Jump("loc_1D9F")

    label("loc_FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1059")

    ChrTalk(
        0x8,
        (
            "Stress on the visitors\x01",
            "staying here is gradually\x01",
            "increasing as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope we can send them\x01",
            "back to Crossbell City\x01",
            "soon...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D9F")

    label("loc_1059")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_123D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1186")

    ChrTalk(
        0x8,
        (
            "The city supplies us with\x01",
            "provisions, but basically\x01",
            "all of it is preserved food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh man. The nutritional\x01",
            "balance of the hospital\x01",
            "meals is going to worsen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The patients and visitors' facial\x01",
            "expressions are somewhat gloomy...\x01",
            "I'd like to do something about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1238")

    label("loc_1186")


    ChrTalk(
        0x8,
        (
            "With only the provisions from\x01",
            "the city, the nutritional\x01",
            "balance is just going to worsen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wish I could stock up on\x01",
            "fresh vegetables from\x01",
            "Armorica Village like before.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1238")

    Jump("loc_1D9F")

    label("loc_123D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_143C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_136D")

    ChrTalk(
        0x8,
        (
            "The city kids over there\x01",
            "seem to be Arc-en-Ciel\x01",
            "fans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They came to visit Ilya, but after the declaration of\x01",
            "independence, they've been staying at the hospital\x01",
            "and have been helping out with different things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. I guess there are\x01",
            "kind kids out there too,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1437")

    label("loc_136D")


    ChrTalk(
        0x8,
        (
            "Those kids fans of Ilya's. They stayed at the\x01",
            "hospital after the declaration of independence\x01",
            "and have been helping with different things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. I guess there are\x01",
            "kind kids out there too,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1437")

    Jump("loc_1D9F")

    label("loc_143C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_15BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1537")

    ChrTalk(
        0x8,
        (
            "I'm also in charge of\x01",
            "the hospital menu,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Among the recently hospitalised\x01",
            "patients, there's many injured\x01",
            "people who can't eat anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Food is tied to energy.\x01",
            "I hope they become able\x01",
            "to eat again soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15B6")

    label("loc_1537")


    ChrTalk(
        0x8,
        (
            "For now, they're getting\x01",
            "nutrients via IV, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Food is tied to energy.\x01",
            "I hope they become able\x01",
            "to eat again soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B6")

    Jump("loc_1D9F")

    label("loc_15BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_17BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1719")

    ChrTalk(
        0x8,
        (
            "There were a lot of ambulance trips\x01",
            "yesterday. I wondered what might've happened\x01",
            "but... to think it was a train derailment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There was a mad rush to get some kind of\x01",
            "compensation from the railway company, but I\x01",
            "was really glad that there were no fatalities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even so... What in the\x01",
            "world could the cause\x01",
            "be?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17B5")

    label("loc_1719")


    ChrTalk(
        0x8,
        (
            "What in the world could the\x01",
            "cause of the train derailment\x01",
            "accident have been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm glad there were no\x01",
            "fatalities, but I'm\x01",
            "worried for some reason.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17B5")

    Jump("loc_1D9F")

    label("loc_17BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_18A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1863")

    ChrTalk(
        0x8,
        (
            "Mr. Arios? He went back\x01",
            "to the Guild last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's a difficult time for\x01",
            "Shizuku, but as expected, it\x01",
            "seems like he's a busy man.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18A2")

    label("loc_1863")


    ChrTalk(
        0x8,
        (
            "Well then, what should I\x01",
            "cook for the boarders\x01",
            "tonight...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18A2")

    Jump("loc_1D9F")

    label("loc_18A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1A6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B1")

    ChrTalk(
        0x8,
        (
            "Because of Shizuku's\x01",
            "surgery, Mr. Arios\x01",
            "stayed here some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Shizuku too must've been\x01",
            "reassured by the company\x01",
            "of her great father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, they say the surgery\x01",
            "had disappointing results.\x01",
            "*sigh*... It's too much to bear.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A6A")

    label("loc_19B1")


    ChrTalk(
        0x8,
        (
            "Mr. Arios stayed here for\x01",
            "some time to be with Shizuku.\x01",
            "I'm sure she felt reassured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, they say the surgery\x01",
            "had disappointing results.\x01",
            "*sigh*... It's too much to bear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6A")

    Jump("loc_1D9F")

    label("loc_1A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1BAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B22")

    ChrTalk(
        0x8,
        (
            "Bracer Eolia came for a\x01",
            "job today, so I gave her\x01",
            "lunch for free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The hospital is greatly\x01",
            "indebted to those kids. It\x01",
            "was the least I could do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BA7")

    label("loc_1B22")


    ChrTalk(
        0x8,
        (
            "The hospital is greatly\x01",
            "indebted to the bracers\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I have to at least give\x01",
            "them a lunch for free\x01",
            "every now and then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA7")

    Jump("loc_1D9F")

    label("loc_1BAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1C52")

    ChrTalk(
        0x8,
        (
            "Archduke Albert... Though\x01",
            "young, he's Remiferia's\x01",
            "head of state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They say he's beloved by\x01",
            "his citizens too... I'm\x01",
            "sure he's an excellent man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D9F")

    label("loc_1C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1D9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D3F")

    ChrTalk(
        0x8,
        (
            "It seems we have a new\x01",
            "medical intern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He's that kid over there,\x01",
            "Micheau. He said he self-\x01",
            "studied in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I really love hard workers,\x01",
            "you know. I have to give\x01",
            "him lots of free stuff.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D9F")

    label("loc_1D3F")


    ChrTalk(
        0x8,
        (
            "I really love hard\x01",
            "workers, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I have to give our\x01",
            "newcomer lots of free\x01",
            "stuff.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D9F")

    Jump("loc_AF2")

    label("loc_1DA4")

    TalkEnd(0x8)
    Return()

    # Function_7_AA0 end

    def Function_8_1DA8(): pass

    label("Function_8_1DA8")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1E2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC6")
    Call(0, 9)
    Jump("loc_1E28")

    label("loc_1DC6")


    ChrTalk(
        0x9,
        "Eat a lot, Micheau.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hey now. If you eat it\x01",
            "too quickly, it'll get\x01",
            "stuck in your throat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E28")

    Jump("loc_257D")

    label("loc_1E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1EAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E48")
    Call(0, 9)
    Jump("loc_1EA5")

    label("loc_1E48")


    ChrTalk(
        0x9,
        (
            "...Anyway, there's nothing we\x01",
            "can do about that... Let's\x01",
            "focus on the hospital for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EA5")

    Jump("loc_257D")

    label("loc_1EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1F50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EC5")
    Call(0, 9)
    Jump("loc_1F4B")

    label("loc_1EC5")


    ChrTalk(
        0x9,
        (
            "Micheau, you've gotten\x01",
            "used to it too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although before you complained\x01",
            "that you couldn't eat while\x01",
            "reading a book like that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F4B")

    Jump("loc_257D")

    label("loc_1F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2024")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F6B")
    Call(0, 9)
    Jump("loc_201F")

    label("loc_1F6B")


    ChrTalk(
        0x9,
        (
            "Constant study is important.\x01",
            "It takes three days to recover\x01",
            "from one day of slacking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You may be worried about the\x01",
            "city, but you've got to study\x01",
            "properly. ...Understood?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_201F")

    Jump("loc_257D")

    label("loc_2024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_208E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_203F")
    Call(0, 9)
    Jump("loc_2089")

    label("loc_203F")


    ChrTalk(
        0x9,
        (
            "...Now Micheau, sit down.\x01",
            "We have to eat well for\x01",
            "the afternoon too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2089")

    Jump("loc_257D")

    label("loc_208E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2153")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20A9")
    Call(0, 9)
    Jump("loc_214E")

    label("loc_20A9")


    ChrTalk(
        0x9,
        (
            "Well, we'll do your evaluation\x01",
            "later... We're going to have more work\x01",
            "to do whether you like it or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For now, I have to be\x01",
            "happy we saved the\x01",
            "patients.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_214E")

    Jump("loc_257D")

    label("loc_2153")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_21F5")

    ChrTalk(
        0x9,
        (
            "Well then, I have a\x01",
            "little time until\x01",
            "today's lecture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Micheau isn't here yet, I guess\x01",
            "I'll do some self-studying\x01",
            "while having breakfast.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_257D")

    label("loc_21F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_22CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2210")
    Call(0, 9)
    Jump("loc_22C9")

    label("loc_2210")


    ChrTalk(
        0x9,
        (
            "Lytton has been working\x01",
            "hard since he had his\x01",
            "previous instructor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I don't lose to him in studying, but\x01",
            "it would be strange if he didn't grow\x01",
            "after working that hard on site.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C9")

    Jump("loc_257D")

    label("loc_22CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_23AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E9")
    Call(0, 9)
    Jump("loc_23A8")

    label("loc_22E9")


    ChrTalk(
        0x9,
        (
            "*munch munch*... Well, it's\x01",
            "something everyone goes through when\x01",
            "they're a medical intern, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You can't always skip out\x01",
            "on lunch, you know? Haha,\x01",
            "you'll get used to it soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23A8")

    Jump("loc_257D")

    label("loc_23AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2441")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C8")
    Call(0, 9)
    Jump("loc_243C")

    label("loc_23C8")


    ChrTalk(
        0x9,
        (
            "Micheau, will this be\x01",
            "your first time observing\x01",
            "live surgery...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha... Well, let's see\x01",
            "what you've got.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_243C")

    Jump("loc_257D")

    label("loc_2441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_257D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2513")

    ChrTalk(
        0x9,
        (
            "I was asked to coach\x01",
            "Micheau, a newcomer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm. I won't have as\x01",
            "much time to study,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, this is studying too.\x01",
            "Since this is an opportunity,\x01",
            "I'll be relentless.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_257D")

    label("loc_2513")


    ChrTalk(
        0x9,
        (
            "Well, coaching a cute\x01",
            "junior is studying too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since this is an\x01",
            "opportunity, I'll be\x01",
            "relentless.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_257D")

    TalkEnd(0x9)
    Return()

    # Function_8_1DA8 end

    def Function_9_2581(): pass

    label("Function_9_2581")

    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_269C")

    ChrTalk(
        0x9,
        (
            "Eat plenty, Micheau.\x01",
            "After all, we have a lot\x01",
            "patients to get to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll have you work hard\x01",
            "on the floor today as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "R-Right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Alright, I'll do it!!\x01",
            "*chomp chomp chomp\x01",
            "chomp*...!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ahaha. If you eat too\x01",
            "fast, it'll get stuck in\x01",
            "your throat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31FB")

    label("loc_269C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_280C")

    ChrTalk(
        0x9,
        (
            "The declaration of invalidity,\x01",
            "huh... I wonder what's going\x01",
            "to happen from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyhow, I'm worried\x01",
            "about the people of the\x01",
            "Downtown apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems that applications\x01",
            "to return to the city won't\x01",
            "be accepted for some time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Anyway, there's nothing we\x01",
            "can do about that... Let's\x01",
            "focus on the hospital for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "...Right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31FB")

    label("loc_280C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2970")

    ChrTalk(
        0x9,
        (
            "*munch munch*... And so,\x01",
            "about human organs like the\x01",
            "ones illustrated here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*chomp chomp*... Hmm, I\x01",
            "see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Haha. Even so, you've\x01",
            "got used to this,\x01",
            "Micheau.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although before you complained\x01",
            "that you couldn't eat while\x01",
            "reading a book like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*munch munch*... Haha,\x01",
            "this too is the result\x01",
            "of your training, Flora.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31FB")

    label("loc_2970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2AA9")

    ChrTalk(
        0x9,
        (
            "Micheau, have you been\x01",
            "studying properly\x01",
            "lately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well... I'm not in the\x01",
            "mood for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "With Crossbell like this,\x01",
            "I'm worried about the\x01",
            "people of the apartment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I see... Well, I suppose\x01",
            "it can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, when you calm\x01",
            "down, you must study\x01",
            "properly. ...Understood?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31FB")

    label("loc_2AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2BF2")

    ChrTalk(
        0xA,
        (
            "Among those injured in the\x01",
            "attack, there was someone\x01",
            "who couldn't be saved...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Flora... It's like... my\x01",
            "heart is breaking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I know how you feel. However,\x01",
            "let's leave the complaints until\x01",
            "after everything is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you have that much free\x01",
            "time, you can save someone\x01",
            "else. That's our job.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    Jump("loc_31FB")

    label("loc_2BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2D90")

    ChrTalk(
        0x9,
        (
            "*sigh*, we can finally\x01",
            "take a breather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Nevertheless, it seems\x01",
            "you were doing your best\x01",
            "and helping out, Micheau.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "W-Well... I've still got\x01",
            "a long way to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even if you say I was\x01",
            "helping out, I was just\x01",
            "doing odd jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't be modest. Even\x01",
            "odd jobs are important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lately, it seems like you're calm\x01",
            "even if you see blood... You've\x01",
            "grown a little, haven't you.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_31FB")

    label("loc_2D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2ECD")

    ChrTalk(
        0xA,
        (
            "Lytton often helps with\x01",
            "surgeries and does\x01",
            "frequent hospital rounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*sigh*. As expected, he's\x01",
            "on a whole different level\x01",
            "than a newbie like me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lytton has been working\x01",
            "hard since he had his\x01",
            "previous instructor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "C'mon, don't be in such\x01",
            "a hurry! If you want to\x01",
            "grow, study!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_31FB")

    label("loc_2ECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3096")

    ChrTalk(
        0x9,
        (
            "*chomp chomp munch\x01",
            "munch"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...What's wrong,\x01",
            "Micheau? Why don't you\x01",
            "order something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "W-Well, you see...\x01",
            "Didn't we have a surgery\x01",
            "practicum this morning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Seeing a real surgery for the\x01",
            "first time, you know, I've lost\x01",
            "my appetite for some reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Aah, I thought that\x01",
            "might be it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*chomp chomp*... Well, it's\x01",
            "something everyone goes through.\x01",
            "You'll get used to it in time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...*burp*... I-I hope\x01",
            "you're right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31FB")

    label("loc_3096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_31FB")

    ChrTalk(
        0x9,
        (
            "By the way Micheau, there's a\x01",
            "training surgery with Professor\x01",
            "Gary tomorrow, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think it's going to be\x01",
            "the first time you see a\x01",
            "real surgery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Man, I feel like I'm beginning\x01",
            "my doctor studies in earnest.\x01",
            "I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha... You're certainly\x01",
            "excited. Well, at least\x01",
            "do your best.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)

    label("loc_31FB")

    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_2581 end

    def Function_10_3203(): pass

    label("Function_10_3203")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_325D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3221")
    Call(0, 9)
    Jump("loc_3258")

    label("loc_3221")


    ChrTalk(
        0xA,
        (
            "*chomp chomp chomp\x01",
            "chomp*...!! *cough\x01",
            "cough*...!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3258")

    Jump("loc_381B")

    label("loc_325D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_32FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3278")
    Call(0, 9)
    Jump("loc_32F9")

    label("loc_3278")


    ChrTalk(
        0xA,
        (
            "You're right... We can't\x01",
            "even go back to the city\x01",
            "in this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hope the situation\x01",
            "gets a little better,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F9")

    Jump("loc_381B")

    label("loc_32FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_336A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3319")
    Call(0, 9)
    Jump("loc_3365")

    label("loc_3319")


    ChrTalk(
        0xA,
        (
            "*munch munch*... Haha,\x01",
            "this too is the result\x01",
            "of your training, Flora.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3365")

    Jump("loc_381B")

    label("loc_336A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_340A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3385")
    Call(0, 9)
    Jump("loc_3405")

    label("loc_3385")


    ChrTalk(
        0xA,
        (
            "Right... I'm worried\x01",
            "about the people of the\x01",
            "apartment too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It might be foolish of\x01",
            "me not to study for that\x01",
            "reason.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3405")

    Jump("loc_381B")

    label("loc_340A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_34A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3425")
    Call(0, 9)
    Jump("loc_34A3")

    label("loc_3425")


    ChrTalk(
        0xA,
        (
            "...It's like you say,\x01",
            "Flora...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyhow, I must now think about\x01",
            "how I can save even just a\x01",
            "single additional patient.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A3")

    Jump("loc_381B")

    label("loc_34A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_352B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34C3")
    Call(0, 9)
    Jump("loc_3526")

    label("loc_34C3")


    ChrTalk(
        0xA,
        (
            "Hmm. I've got to reach the point\x01",
            "where I can be trusted with\x01",
            "important jobs, not just chores.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3526")

    Jump("loc_381B")

    label("loc_352B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3539")
    Jump("loc_381B")

    label("loc_3539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_35EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3554")
    Call(0, 9)
    Jump("loc_35EA")

    label("loc_3554")


    ChrTalk(
        0xA,
        (
            "I see... Indeed, being\x01",
            "impatient won't do\x01",
            "anyone any good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...Even so, Flora, don't you\x01",
            "think reading an anatomy\x01",
            "book during mealtime is...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35EA")

    Jump("loc_381B")

    label("loc_35EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3689")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_360A")
    Call(0, 9)
    Jump("loc_3684")

    label("loc_360A")


    ChrTalk(
        0xA,
        (
            "Ooh, after that surgery,\x01",
            "Flora can eat that meat\x01",
            "dish...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ooh, when I think about\x01",
            "it, I feel like throwing\x01",
            "up...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3684")

    Jump("loc_381B")

    label("loc_3689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_370D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36A4")
    Call(0, 9)
    Jump("loc_3708")

    label("loc_36A4")


    ChrTalk(
        0xA,
        (
            "Haha, please leave it to\x01",
            "me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll study hard so as\x01",
            "not to bring disgrace\x01",
            "upon you, Flora!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3708")

    Jump("loc_381B")

    label("loc_370D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_381B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37C3")

    ChrTalk(
        0xA,
        (
            "Flora is a bit strict,\x01",
            "but her teaching methods\x01",
            "are good, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "She's very knowledgeable\x01",
            "too... Really, I'm glad I\x01",
            "met a good upperclassman.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_381B")

    label("loc_37C3")


    ChrTalk(
        0xA,
        (
            "Flora, can't you do something\x01",
            "about opening the anatomy\x01",
            "book even during mealtime?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_381B")

    TalkEnd(0xA)
    Return()

    # Function_10_3203 end

    def Function_11_381F(): pass

    label("Function_11_381F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_393B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3906")

    ChrTalk(
        0xFE,
        (
            "Our son was severely\x01",
            "injured in that attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He survived, but he's in the\x01",
            "intensive care unit... I could\x01",
            "only see him for a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aah, venerable\x01",
            "Goddess... Please save\x01",
            "my son...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_393B")

    label("loc_3906")


    ChrTalk(
        0xFE,
        (
            "Aah, venerable\x01",
            "Goddess... Please save\x01",
            "my son...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_393B")

    TalkEnd(0xFE)
    Return()

    # Function_11_381F end

    def Function_12_393F(): pass

    label("Function_12_393F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3A5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39FD")

    ChrTalk(
        0xFE,
        (
            "My son is one of the CGF\x01",
            "who fought against the\x01",
            "armed group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...If I had known this would've\x01",
            "happened, I would've been\x01",
            "against him joining the CGF...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3A5B")

    label("loc_39FD")


    ChrTalk(
        0xFE,
        (
            "...If I had known this would've\x01",
            "happened, I would've been\x01",
            "against him joining the CGF...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A5B")

    TalkEnd(0xFE)
    Return()

    # Function_12_393F end

    def Function_13_3A5F(): pass

    label("Function_13_3A5F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3AE8")

    ChrTalk(
        0xFE,
        (
            "Mom and dad have been\x01",
            "looking sad this whole\x01",
            "time for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Big brother... I wonder\x01",
            "what's happened to him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AE8")

    TalkEnd(0xFE)
    Return()

    # Function_13_3A5F end

    def Function_14_3AEC(): pass

    label("Function_14_3AEC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3B8A")

    ChrTalk(
        0xFE,
        (
            "My son's family has been\x01",
            "hospitalised here since\x01",
            "the attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I confirmed their safety\x01",
            "for now, but... My feelings\x01",
            "just won't calm down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B8A")

    TalkEnd(0xFE)
    Return()

    # Function_14_3AEC end

    def Function_15_3B8E(): pass

    label("Function_15_3B8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3C2F")

    ChrTalk(
        0xFE,
        (
            "An incident like that happened\x01",
            "and both the police and CGF\x01",
            "suffered severe damage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what will\x01",
            "happen to Crossbell from\x01",
            "now on...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C2F")

    TalkEnd(0xFE)
    Return()

    # Function_15_3B8E end

    def Function_16_3C33(): pass

    label("Function_16_3C33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C44")
    Jump("loc_3E30")

    label("loc_3C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3CDB")

    ChrTalk(
        0x10,
        (
            "It was decided that we\x01",
            "have to bring the hospital\x01",
            "meals to Lady Ilya...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "W-What do I do... What\x01",
            "should I say when I meet\x01",
            "her!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E30")

    label("loc_3CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3D84")

    ChrTalk(
        0x10,
        (
            "The truth is that I'd like\x01",
            "to scream Lady Ilya's name\x01",
            "so it reaches her room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "However, this is a\x01",
            "hospital... As expected,\x01",
            "I must contain myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E30")

    label("loc_3D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3E30")

    ChrTalk(
        0x10,
        (
            "I'm really glad Lady\x01",
            "Ilya's regained\x01",
            "consciousness!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "It was worth it not going back to\x01",
            "the city and staying here the whole\x01",
            "time praying for her recovery!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E30")

    TalkEnd(0xFE)
    Return()

    # Function_16_3C33 end

    def Function_17_3E34(): pass

    label("Function_17_3E34")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E45")
    Jump("loc_4075")

    label("loc_3E45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3EFA")

    ChrTalk(
        0x11,
        (
            "C-Calm down, Polise... We\x01",
            "have to bring the meals to\x01",
            "the other patients too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "What if, by freaking out you\x01",
            "spilled Lady Ilya's portion?\x01",
            "Stay calm, stay calm!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4075")

    label("loc_3EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3FD1")

    ChrTalk(
        0x11,
        (
            "While helping out I'm also\x01",
            "praying for Lady Ilya to recover\x01",
            "even just one day faster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "That superintendent is a slave\x01",
            "driver, but... When I think that it's\x01",
            "for Lady Ilya's sake, I don't care!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4075")

    label("loc_3FD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4075")

    ChrTalk(
        0x11,
        (
            "Times are hard, so we\x01",
            "must endure sick\x01",
            "visiting Lady Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "That being the case, we have\x01",
            "to help out at the hospital\x01",
            "and be of at least some use.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4075")

    TalkEnd(0xFE)
    Return()

    # Function_17_3E34 end

    def Function_18_4079(): pass

    label("Function_18_4079")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_408A")
    Jump("loc_42EB")

    label("loc_408A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4098")
    Jump("loc_42EB")

    label("loc_4098")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_40A6")
    Jump("loc_42EB")

    label("loc_40A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_40B4")
    Jump("loc_42EB")

    label("loc_40B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_42EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40D7")
    Call(0, 19)
    TalkEnd(0xFE)
    SetChrSubChip(0x15, 0x1)
    Return()

    label("loc_40D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4236")

    ChrTalk(
        0x15,
        (
            "#01300FWhen I'm with Zeit, it's very\x01",
            "relaxing.\x02\x03",
            "#01304FAlthough I haven't met him\x01",
            "that many times, I am at ease\x01",
            "with him for some reason...\x02\x03",
            "#01300FThere's this nostalgic\x01",
            "feeling, like we've been\x01",
            "friends for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10400FAhaha, it's like you're\x01",
            "a pair of lovers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(I might be a little\x01",
            "jealous of that...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_42E3")

    label("loc_4236")


    ChrTalk(
        0x15,
        (
            "#01300FWhen I'm with Zeit, it's very relaxing.\x02\x03",
            "#01304FI'm at ease with him for some reason...\x01",
            "There's this nostalgic feeling, like\x01",
            "we've been friends for a long time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42E3")

    TalkEnd(0xFE)
    SetChrSubChip(0x15, 0x1)
    Return()

    label("loc_42EB")

    TalkEnd(0xFE)
    Return()

    # Function_18_4079 end

    def Function_19_42EF(): pass

    label("Function_19_42EF")

    OP_4B(0x16, 0xFF)

    ChrTalk(
        0x15,
        (
            "#01300FCome to think of it Zeit, I\x01",
            "haven't seen you since the\x01",
            "President's speech.\x02\x03",
            "#01303FYou chased after KeA who was\x01",
            "taken away by Arios and I\x01",
            "didn't know where you were...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#3C#01200FYes, I did pursue them, but...\x01",
            "When that Divine Blade reached the\x01",
            "lake, I was completely shaken off.\x02\x03",
            "I felt sorry for Lloyd and the\x01",
            "others, but I went back to my\x01",
            "subordinates to make preparations.\x02\x03",
            "#01203FCome to think of it, I caused you,\x01",
            "who was there, to worry\x01",
            "needlessly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#01302F*chuckle*, I'm fine. More\x01",
            "importantly, I'm glad\x01",
            "that you're safe, Zeit.\x02\x03",
            "#01300FAlso, you're doing all\x01",
            "you can to help Lloyd and\x01",
            "Wazy even now.\x02\x03",
            "#01304FHaha, thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Cecil gently stroked\x01",
            "Zeit's head.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x16, 0xFFFFFDA8, 2100, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        "#3C#01200F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#01303FWhen I'm with you Zeit,\x01",
            "I feel at ease for some\x01",
            "reason.\x02\x03",
            "#01305FAh... I am sorry. Did I\x01",
            "offend you by petting\x01",
            "you like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#3C#01200F...Hehe, no. It wasn't a\x01",
            "bad feeling.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 1)
    ClearChrFlags(0x15, 0x10)
    OP_4C(0x16, 0xFF)
    Return()

    # Function_19_42EF end

    def Function_20_46AF(): pass

    label("Function_20_46AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4815")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46CD")
    Call(0, 19)
    Jump("loc_4815")

    label("loc_46CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4789")

    ChrTalk(
        0x16,
        "#3C#01203F...Hehe......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(I...wonder what's wrong\x01",
            "with Zeit? He's awfully\x01",
            "quiet...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(Maybe he's feeling\x01",
            "awkward after being\x01",
            "petted by Cecil?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4815")

    label("loc_4789")


    ChrTalk(
        0x16,
        (
            "#3C#01200F...So as not to throw the\x01",
            "hospital into confusion, I'll\x01",
            "be waiting for you here.\x02\x03",
            "You all should visit whomever\x01",
            "you need to.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4815")

    TalkEnd(0xFE)
    Return()

    # Function_20_46AF end

    def Function_21_4819(): pass

    label("Function_21_4819")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4A2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_497F")

    ChrTalk(
        0xFE,
        (
            "Some time ago, my husband had\x01",
            "spasm due to his chronic disease.\x01",
            "We rushed here in an ambulance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm glad the application was accepted somehow,\x01",
            "but... Since the inspection was so strict, I was on\x01",
            "pins and needles about whether it'd be accepted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... Maybe staying\x01",
            "at the hospital like\x01",
            "this isn't that safe.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4A2C")

    label("loc_497F")


    ChrTalk(
        0xFE,
        (
            "Some time ago, my husband had\x01",
            "spasm due to his chronic disease.\x01",
            "We rushed here in an ambulance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... Maybe staying\x01",
            "at the hospital like\x01",
            "this isn't that safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A2C")

    TalkEnd(0xFE)
    Return()

    # Function_21_4819 end

    def Function_22_4A30(): pass

    label("Function_22_4A30")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4C89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B99")

    ChrTalk(
        0xFE,
        (
            "Because I couldn't come to the\x01",
            "hospital, I ran out of medicine for\x01",
            "my chronic disease and I had a spasm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The movement restrictions on\x01",
            "the highway are such a pain.\x01",
            "I'll remember them next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To go back to the city we need to wait until\x01",
            "the next time the State Guard comes... I\x01",
            "guess I'll take it easy for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_4C89")

    label("loc_4B99")


    ChrTalk(
        0xFE,
        (
            "Getting taken to the hospital is such\x01",
            "a pain due to the highway movement\x01",
            "restrictions. I'll remember them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To go back to the city we need to wait until\x01",
            "the next time the State Guard comes... I\x01",
            "guess I'll take it easy for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C89")

    TalkEnd(0xFE)
    Return()

    # Function_22_4A30 end

    def Function_23_4C8D(): pass

    label("Function_23_4C8D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4D62")

    ChrTalk(
        0xFE,
        (
            "I planned to go back to\x01",
            "the city today... What's\x01",
            "going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know anything about a declaration of\x01",
            "invalidity, but if they took me alone to the\x01",
            "city, they probably wouldn't be punished.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D62")

    TalkEnd(0xFE)
    Return()

    # Function_23_4C8D end

    def Function_24_4D66(): pass

    label("Function_24_4D66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4D77")
    Jump("loc_4E67")

    label("loc_4D77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4E67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D92")
    Call(0, 30)
    Jump("loc_4E67")

    label("loc_4D92")


    ChrTalk(
        0xFE,
        (
            "We have to go to the St. Ursula sandbank in\x01",
            "order to investigate the nexus between the\x01",
            ""Azure Flowers" and cryptids that you reported.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, no need to worry\x01",
            "about us. You should\x01",
            "focus on your own jobs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E67")

    TalkEnd(0xFE)
    Return()

    # Function_24_4D66 end

    def Function_25_4E6B(): pass

    label("Function_25_4E6B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4E7C")
    Jump("loc_57FD")

    label("loc_4E7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_50A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E97")
    Call(0, 30)
    Jump("loc_509E")

    label("loc_4E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FF0")

    ChrTalk(
        0xFE,
        (
            "*cough*, by the way,\x01",
            "about those azure\x01",
            "flowers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "According to your report,\x01",
            "it seems they were\x01",
            "ingredients for Gnosis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that the ringleader, Joachim\x01",
            "Gｸnther, manufactured a great amount of\x01",
            "the drug during the cult incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder where got his\x01",
            "hands on Pleroma Grass,\x01",
            "the necessary ingredient.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_509E")

    label("loc_4FF0")


    ChrTalk(
        0xFE,
        (
            "It seems Joachim Gｸnther\x01",
            "manufactured a great amount of\x01",
            "Gnosis during the cult incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder where got his\x01",
            "hands on Pleroma Grass,\x01",
            "the necessary ingredient.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_509E")

    Jump("loc_57FD")

    label("loc_50A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_50B1")
    Jump("loc_57FD")

    label("loc_50B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_57FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5438")

    ChrTalk(
        0x101,
        "#00005FOh, Bracer Eol─\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_518D")
    Jump("loc_51D7")

    label("loc_518D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_51AD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_51D7")

    label("loc_51AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_51CD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_51D7")

    label("loc_51CD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_51D7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "#4ST-Tio... You're finally\x01",
            "back!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F...Hello, it's been a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aah... How many times\x01",
            "did I dream of this\x01",
            "day!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come here, Tio! Big\x01",
            "sister will kiss you all\x01",
            "over!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F...I firmly refuse.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*ahn*, it's been some\x01",
            "time I felt this too...㈱\x02",
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
        0x103,
        (
            "#00211F(...I don't know why but I\x01",
            "feel she's become a more\x01",
            "formidable foe than before.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(H-Haha... Her feelings have\x01",
            "probably piled up in the\x01",
            "time she hasn't seen you.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetScenarioFlags(0x1C0, 7)
    Jump("loc_57FD")

    label("loc_5438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_568A")
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x103, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_54D3")
    Jump("loc_551D")

    label("loc_54D3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_54F3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_551D")

    label("loc_54F3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5513")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_551D")

    label("loc_5513")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_551D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "To be able to meet Tio\x01",
            "for coming to deliver a\x01",
            "requested package is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, couldn't this\x01",
            "be fate!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211FIt isn't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*ahn*... Such a swift\x01",
            "response......㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FIn that case Eolia, I\x01",
            "could be her replacem...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ugh, I don't want you㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F*gasp*... I got a swift\x01",
            "response too!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_57F9")

    label("loc_568A")

    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x103, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_571B")
    Jump("loc_5765")

    label("loc_571B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_573B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5765")

    label("loc_573B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_575B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5765")

    label("loc_575B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5765")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Haha. Let me have some\x01",
            "skinship next time too,\x01",
            "ok Tio?㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(I still need to be\x01",
            "careful... Yes.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57F9")

    SetChrSubChip(0xFE, 0x0)

    label("loc_57FD")

    TalkEnd(0xFE)
    Return()

    # Function_25_4E6B end

    def Function_26_5801(): pass

    label("Function_26_5801")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "3F: Female Dormitory→\x01",
            " \x01",
            "←2F: Male Dormitory\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_5801 end

    def Function_27_5868(): pass

    label("Function_27_5868")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　Accomodation for Visitors and Outpatients\x01",
            "※In case you need one, please ask the superintendent.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_5868 end

    def Function_28_5902(): pass

    label("Function_28_5902")

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
        "#00206F#5PNo way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#06406F#5PI-It's almost too grand\x01",
            "a story for me to\x01",
            "believe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#01303F#5PCrossbell, our home...\x02\x03",
            "#01308FI understand the various\x01",
            "past events and how we\x01",
            "arrived at this point.\x02\x03",
            "#01301FAbout our current\x01",
            "situation and KeA too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#12P...Yeah.\x02\x03",
            "#00003FI only wish for two\x01",
            "things.\x02\x03",
            "To ascertain the unseen\x01",
            "truth with my own eyes─\x02\x03",
            "#00013FAnd to free everyone,\x01",
            "getting KeA back in the\x01",
            "process.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x105, 0x1)
    Sleep(150)

    ChrTalk(
        0x105,
        (
            "#10409F#12PHehe. Even though it's just two\x01",
            "things, it seems like they'll\x01",
            "be absurdly difficult to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01203F#11P#3CWell, that's how he is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#5PHaha... That's our Lloyd.\x02\x03",
            "#00204F─My feelings are the same\x01",
            "as his.\x02\x03",
            "#00203FAs a member of the Support\x01",
            "Section...\x02\x03",
            "#00201FAnd even more so, as one of\x01",
            "KeA's guardians... Please,\x01",
            "take me along with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PThank you, Tio. I'll be\x01",
            "counting on you.\x02\x03",
            "#00005FHowever, why were you\x01",
            "brought here, Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#5P...Probably, Mariabell ordered\x01",
            "Arios to do it.\x02\x03",
            "#00208FIn order to keep the Support\x01",
            "Section members separated and to\x01",
            "monitor each of us...\x02\x03",
            "#00201FMost likely, they believe we\x01",
            "could have influenced KeA if they\x01",
            "left us all in the same place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PI see...\x02\x03",
            "#00008FThen that would imply\x01",
            "that Elie and Randy are\x01",
            "each in different places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PHmm... Well, if they're in\x01",
            "Crossbell City, then freeing\x01",
            "them isn't an option.\x02\x03",
            "#10402FBut, the fact that Tio was\x01",
            "here means it's likely that\x01",
            "they're outside the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#01306F#5PRight... It seems they\x01",
            "are trying to not let you\x01",
            "four get close to KeA.\x02",
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

    def lambda_60E1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_60E1)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x19,
        (
            "#06403F#5PU-Umm...!\x02\x03",
            "#06401FCould you perhaps take\x01",
            "me with you as well!?\x02",
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
        "#00005F#6PFran...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#01305F#5PFran?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#06406F#5PI-I can't fight like all\x01",
            "of you, but...\x02\x03",
            "#06403FEven so, I think I would\x01",
            "do all right as an\x01",
            "operator!\x02\x03",
            "#06401FAnd it seems you'll be\x01",
            "moving around with\x01",
            "Wazy's airship, so...\x02\x03",
            "Please! I want to help\x01",
            "you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PFran...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x0)
    Sleep(150)

    ChrTalk(
        0x103,
        "#00208F#5PLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PHmm. It's true that the\x01",
            "Merkabah is short handed\x01",
            "so you could be of help...\x02\x03",
            "#10400FI'll have to let Lloyd\x01",
            "decide this one.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00006F#6P...You're right.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00003F#6PFran─ Your older sister\x01",
            "is currently working for\x01",
            "the State Guard.\x02\x03",
            "#00008FComing with us means\x01",
            "fighting against Noｱl...\x02\x03",
            "#00001FDo you understand that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#06406F#5P...Y-Yes!\x02\x03",
            "#06408FOf course I don't want to pick\x01",
            "a fight with big sis, but...\x02\x03",
            "#06401FNevertheless... Even I am a\x01",
            "Crossbell Police officer!\x02\x03",
            "With everyone tackling such a\x01",
            "dangerous situation... I can't\x01",
            "just sit here and do nothing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PIs that so...\x02\x03",
            "#00002F─Alright then. We'll\x01",
            "make use of your\x01",
            "abilities.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x19,
        "#06409F#5PT-Thank you very much!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)
    Sleep(100)

    ChrTalk(
        0x103,
        (
            "#00202F#5PFran... I'm happy for\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#12PHehe, I guess Abbas' workload\x01",
            "is going to get a little\x01",
            "lighter from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#01309F#5PHaha... Looks like it's\x01",
            "settled then.\x02",
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
            "#00000F#12PYeah... It's time to go,\x01",
            "Cecil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#01304F#5PYes, please take care.\x02\x03",
            "#01303FI can't help you all\x01",
            "directly. However...\x02\x03",
            "#01302FI will pray for you\x01",
            "while working here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PThanks. ...That will be\x01",
            "plenty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#5P...Cecil. Thank you for\x01",
            "everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#06411F#11PS-Someone like me... I\x01",
            "owe you so much.\x02\x03",
            "#06406F#30W*sob*... Uuuh...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x15, 0x1)
    Sleep(150)

    ChrTalk(
        0x15,
        (
            "#01309F#5PHaha. You're going to\x01",
            "mess up your cute face,\x01",
            "you know?\x02\x03",
            "#01305FBy the way Fran, is it\x01",
            "alright for you to just\x01",
            "leave your stuff here?\x02\x03",
            "#01302FWouldn't it be better to\x01",
            "take at least one change\x01",
            "of clothes with you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x19,
        (
            "#06405F#11P...I-I have to pack my\x01",
            "things!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x101, 500)

    ChrTalk(
        0x19,
        (
            "#06412F#5PP-Please wait just a\x01",
            "little while!\x02",
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
        "#00002F#12PHaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#11P#3CHmm, looks like things\x01",
            "are going to become much\x01",
            "more lively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#12PIt'll be a little more\x01",
            "cheerful even inside the\x01",
            "Merkabah, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#01304F#5PHaha...\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x15,
        (
            "#01305F#5PBy the way...\x02\x03",
            "#01300FIf you want, why don't you\x01",
            "go say hi to Ilya and Mr.\x01",
            "Donovan while you wait?\x02",
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
            "#00005F#12PWhat...!? Could it be\x01",
            "that they...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#01304F#5PYes, they've both\x01",
            "regained consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#5PIlya can't truly walk\x01",
            "around just yet, but...\x02\x03",
            "#00202FIt seems Inspector\x01",
            "Donovan is recovering\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#12PI see... Thank goodness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#12PSince we're waiting for\x01",
            "Fran, why don't we take\x01",
            "the time to visit them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#12PYeah, let's.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5PI will join you as well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#11P#3CHmm. Since I may cause the\x01",
            "patients to be unsettled,\x01",
            "I shall wait here for you.\x02",
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
            "Zeit left the party\x01",
            "temporarily.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tio has joined the\x01",
            "party.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F5B")
    SetChrFlags(0x15, 0x10)

    label("loc_6F5B")

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

    # Function_28_5902 end

    def Function_29_6FA0(): pass

    label("Function_29_6FA0")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x8000)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xFA0, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x138, 0x3E80, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x10B, 0x1F40, 0x1388, 0x1)
    Return()

    # Function_29_6FA0 end

    def Function_30_6FEE(): pass

    label("Function_30_6FEE")

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
        "#5POh, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FLing, Eolia... You came\x01",
            "to St. Ursula Hospital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FDid you have some kind\x01",
            "of request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#6PWell, we're getting\x01",
            "ready to go investigate\x01",
            "that Cryptid, see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#6PRight now we're headed to St.\x01",
            "Ursula Byroad sandbank where\x01",
            "you guys defeated that Cryptid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#6PIt's to investigate the possibility\x01",
            "that those "azure flowers" you\x01",
            "reported cause Cryptid appearances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#5PIncidentally, Arios just got back\x01",
            "and is handling extermination of the\x01",
            "remaining Cryptid that was spotted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10105FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00300FAnythin' we can help\x01",
            "with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#5PNah, we'll be fine\x01",
            "handling this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#5PWell, if I could get some skinship\x01",
            "with Tio when I get back, I think\x01",
            "I could do my best no matter what㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4S#11P#00203FI refuse.\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x18,
        "#5PAwww, no waaay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FAhaha, you never change.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#6PWell, it means you don't\x01",
            "have to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#6PYou guys should just do\x01",
            "what you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FYes, understood. Please\x01",
            "do your best too.\x02",
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

    # Function_30_6FEE end

    def Function_31_74E0(): pass

    label("Function_31_74E0")

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
            "#5P#01300F...Then, Tio won't be\x01",
            "coming back for a while\x01",
            "yet, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYeah. She seems super\x01",
            "busy.\x02\x03",
            "#00002FI suppose she's doing\x01",
            "her best in Lｳman State\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5P#01304FI see... Then, I look\x01",
            "forward to seeing her\x01",
            "again.\x02\x03",
            "#01309FHaha, when she gets\x01",
            "back, I'll have her tell\x01",
            "me all about her trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FHaha... right.\x02\x03",
            "#00000FI think Tio will be glad\x01",
            "to see you too, Cecil.\x02",
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
        "#6P#10105FWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10304FHmm...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        "#12P#00005FW-What is with you two?\x02",
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
            "#6P#10109FW-Well... I did hear\x01",
            "rumors, but you guys\x01",
            "really are very close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10302FI'm a little jealous\x01",
            "since I couldn't cut\x01",
            "in...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00006FH-Hey now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FTch, that's just how this guy\x01",
            "is.\x02\x03",
            "#00301FNormally, even just knowing a\x01",
            "girl like Cecil since childhood\x01",
            "would make a guy super lucky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00106FThat really is true...\x02\x03",
            "#00111FIf you take that for\x01",
            "granted, you'll pay for\x01",
            "it someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FI-I don't get what you\x01",
            "mean...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#5P#01309FHaha...\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x15,
        (
            "#5P#01305FOh, by the way, sorry\x01",
            "for getting caught up in\x01",
            "conversation, but...\x02\x03",
            "#01300FDid you have some\x01",
            "business at the hospital\x01",
            "today?\x02",
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
            "#12P#00005FOh, that's right.\x02\x03",
            "#00000F...Ahem, you see... We\x01",
            "came for Professor\x01",
            "Seiland's request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FShe took over as head of the\x01",
            "pharmacology and neurology\x01",
            "department, if I'm not mistaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5P#01302FYes, that's right.\x02\x03",
            "#01303FThere was a commotion at the hospital\x01",
            "when it was announced that Dr. Joachim\x01",
            "was manufacturing a mysterious drug here.\x02\x03",
            "#01308FThe professors had to deal with that for\x01",
            "a while in addition to their normal jobs,\x01",
            "but...\x02\x03",
            "#01300FRecently, they regained the trust of the\x01",
            "patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FThat must have been\x01",
            "tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5P#01309FHaha... Thanks to all of you, we\x01",
            "managed somehow.\x02\x03",
            "#01300FThe scars from that incident\x01",
            "healed too, and finally St. Ursula\x01",
            "Hospital took new steps forward.\x02\x03",
            "As part of that, we asked\x01",
            "Professor Seiland to come here\x01",
            "from Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00100FShe's related to the famed\x01",
            "medical equipment manufacturer,\x01",
            "Seiland Company, right?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x2)

    ChrTalk(
        0x15,
        (
            "#11P#01300FYes, she's a relative of\x01",
            "the founder.\x02\x03",
            "#01304FShe's a woman, but she\x01",
            "has a cold and cool air\x01",
            "to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FOh, a female doctor!\x01",
            "Man, I'm really looking\x01",
            "forward to this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FS-Setting aside her\x01",
            "air...\x02\x03",
            "#00000FI see. This verifies her\x01",
            "background.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10300FHmm. She's a professor,\x01",
            "so I assume she's quite\x01",
            "skilled?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#01300FIt seems she's a famous pharmacology\x01",
            "and neurology researcher in Remiferia\x01",
            "as well.\x02\x03",
            "#01304FJust the other day, her surgery for\x01",
            "Mihail, hospitalized due to a serious\x01",
            "illness, was a great success.\x02\x03",
            "#01300FShe's now preparing for Shizuku's\x01",
            "surgery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00105FShizuku's...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FI see... She really\x01",
            "seems like an amazing\x01",
            "doctor.\x02\x03",
            "Do you know where\x01",
            "Professor Seiland is\x01",
            "now?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x15,
        (
            "#5P#01300FShe's usually holed up\x01",
            "in the research\x01",
            "building's lab.\x02\x03",
            "I think she'll see you\x01",
            "if you ask Sera at the\x01",
            "reception desk.\x02\x03",
            "#01309FHaha, but since I'm\x01",
            "here, how about we go\x01",
            "there together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah, thanks. ...Let's\x01",
            "go then.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t1530", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_74E0 end

    def Function_32_82CF(): pass

    label("Function_32_82CF")

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
            "My, welcome. Would you\x01",
            "like something to eat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, we're from\x01",
            "the Special Support\x01",
            "Section...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that you came\x01",
            "for "gourmet\x01",
            "recommendations" coverage.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Ah, the Gourmet Guide\x01",
            "thing, right? I heard about\x01",
            "it from Crossbell News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Still, that's a\x01",
            "problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FIs something the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My recommended dish\x01",
            "needs to boil for quite\x01",
            "some time, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I just ran out of it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sorry, but I'm not\x01",
            "prepared to treat you to\x01",
            "it right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHmm, can't be helped\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FHow long until it's\x01",
            "ready?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8652")

    ChrTalk(
        0x8,
        (
            "Let's see, I just\x01",
            "started preparing it\x01",
            "last night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It'll be two days until\x01",
            "it's ready, so the day\x01",
            "after tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86B3")

    label("loc_8652")


    ChrTalk(
        0x8,
        (
            "Let's see, I started\x01",
            "preparing it the day\x01",
            "before yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "It'll be ready tomorrow.\x02",
    )

    CloseMessageWindow()

    label("loc_86B3")


    ChrTalk(
        0x109,
        (
            "#10105FI-It boils for three\x01",
            "whole days?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHehe. I'm sure it will have\x01",
            "a deep flavor. Let's look\x01",
            "forward to its completion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, it'll be tasty for\x01",
            "sure. Don't forget to\x01",
            "stop by once it's ready.\x02",
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

    # Function_32_82CF end

    def Function_33_87C6(): pass

    label("Function_33_87C6")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 1)), scpexpr(EXPR_END)), "loc_89B0")

    ChrTalk(
        0x8,
        (
            "Ah, you guys. It seems\x01",
            "you didn't forget and\x01",
            "came.\x02",
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
        "#00005FThen that means...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, my recommended\x01",
            "dish, "Three-Day Stew",\x01",
            "is finally ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Wanna eat it right away?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B5A")

    label("loc_89B0")


    ChrTalk(
        0x8,
        (
            "My, welcome. Would you\x01",
            "like something to eat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, we're from\x01",
            "the Special Support\x01",
            "Section...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that you came\x01",
            "for "gourmet\x01",
            "recommendations" coverage.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Ah, the Gourmet Guide\x01",
            "thing, right? I heard about\x01",
            "it from Crossbell News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, you've come just\x01",
            "at the right time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "My recommended dish,\x01",
            ""Three-Day Stew", was\x01",
            "completed just moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Wanna eat it right away?\x02",
    )

    CloseMessageWindow()

    label("loc_8B5A")


    ChrTalk(
        0x103,
        "#00200FYes, by all means.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, wait a moment.\x01",
            "I'll prepare a portion\x01",
            "for each of you.\x02",
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
            "Lloyd and the others ate\x01",
            "the Three-Day Stew.\x07\x00\x02",
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
        "#10105F#4S...D-Delicious!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FYeah... it's super thick\x01",
            "and the taste is\x01",
            "absurdly rich.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 1)), scpexpr(EXPR_END)), "loc_8D45")

    ChrTalk(
        0x105,
        (
            "#10302FHehe, it was worth the\x01",
            "wait.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D8F")

    label("loc_8D45")


    ChrTalk(
        0x105,
        (
            "#10302FHehe, this might be the\x01",
            "best dish for a rainy\x01",
            "day like today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D8F")


    ChrTalk(
        0x102,
        (
            "#00100FYes, really... It might be the\x01",
            "first time I've ever had such\x01",
            "a delicious stew!\x02\x03",
            "#00103FIt warms your body, it's full\x01",
            "of nutrients... I think it's\x01",
            "really good for you.\x02\x03",
            "#00109FIt seems like even sick people\x01",
            "would recover in an instant if\x01",
            "they just ate this.\x02",
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
        "#00009FWell you look happy...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)

    ChrTalk(
        0x8,
        (
            "Ahaha, you're\x01",
            "exaggerating.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    ChrTalk(
        0x103,
        (
            "#00200FIt seems Elie liked it a\x01",
            "lot... I think we can leave\x01",
            "this place's article to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, that's right.\x01",
            "Elie, can I count on\x01",
            "you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#00100FYes, I would love to.\x01",
            "Please leave it to me.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x173, 1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_902D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_902D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_904A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_904A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_905D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_905D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_9070")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_908D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_908D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_90A0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_90BD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_90D0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_90ED")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_9100")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_911D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_911D")

    OP_29(0x80, 0x1, 0xA)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9228")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Finished covering 6\x01",
            "restaurants!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_921F")

    AnonymousTalk(
        0x101,
        (
            "#00003FIt seems we could go report to\x01",
            "Grace immediately, but...\x02\x03",
            "#00000FWe haven't found all 6\x01",
            "members' favorites yet, so why\x01",
            "don't we try a little harder?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_921F")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_9228")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9316")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found all SSS members'\x01",
            "favorites!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this, we found all 6\x01",
            "members' favorites.\x02\x03",
            "We've got plenty of coverage with\x01",
            "this. Let's head to the news\x01",
            "agency right away and report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_9316")

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

    # Function_33_87C6 end

    SaveToFile()

Try(main)
