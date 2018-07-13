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
        "Function_8_1E17",         # 08, 8
        "Function_9_2642",         # 09, 9
        "Function_10_3344",        # 0A, 10
        "Function_11_3995",        # 0B, 11
        "Function_12_3AB6",        # 0C, 12
        "Function_13_3BD6",        # 0D, 13
        "Function_14_3C5B",        # 0E, 14
        "Function_15_3D0D",        # 0F, 15
        "Function_16_3DAE",        # 10, 16
        "Function_17_3FB4",        # 11, 17
        "Function_18_420F",        # 12, 18
        "Function_19_4495",        # 13, 19
        "Function_20_487F",        # 14, 20
        "Function_21_49E8",        # 15, 21
        "Function_22_4C0F",        # 16, 22
        "Function_23_4E71",        # 17, 23
        "Function_24_4F4E",        # 18, 24
        "Function_25_505C",        # 19, 25
        "Function_26_5A58",        # 1A, 26
        "Function_27_5ABE",        # 1B, 27
        "Function_28_5B5A",        # 1C, 28
        "Function_29_7205",        # 1D, 29
        "Function_30_7253",        # 1E, 30
        "Function_31_776C",        # 1F, 31
        "Function_32_8634",        # 20, 32
        "Function_33_8B26",        # 21, 33
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E13")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Rest\x01",      # 2
            "Quit\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B51")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_B51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B70")
    OP_AF(0x5F)
    Jump("loc_B92")

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B80")
    OP_AF(0x5E)
    Jump("loc_B92")

    label("loc_B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B90")
    OP_AF(0x5D)
    Jump("loc_B92")

    label("loc_B90")

    OP_AF(0x5C)

    label("loc_B92")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E0E")

    label("loc_BA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC1")
    OP_AF(0x5A)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E0E")

    label("loc_BC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD5")
    Jump("loc_1E0E")

    label("loc_BD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E0E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_DB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_CA9")

    ChrTalk(
        0x8,
        (
            "Uh uh, my well boiled stew\x01",
            "was the best, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's popular among the patients and the\x01",
            "outside visitors who say it gives them energy.\x01",
            "Come eat it again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DAB")

    label("loc_CA9")


    ChrTalk(
        0x8,
        (
            "My recommended dish\x01",
            "needs to take quite\x01",
            "some time to boil.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D52")

    ChrTalk(
        0x8,
        (
            "It'll be ready in \x01",
            "about two days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When that time comes,\x01",
            "don't forget to visit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DAB")

    label("loc_D52")


    ChrTalk(
        0x8,
        "It'll be ready tomorrow.\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since it's close to be ready,\x01",
            "don't forget to visit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DAB")

    Jump("loc_1E0E")

    label("loc_DB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_FDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF3")

    ChrTalk(
        0x8,
        (
            "I got a call from Mr. Harold.\x01",
            "It seems he'll come to the hospital later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I asked him to bring me a lot of\x01",
            "vegetables from Armorica so it seems \x01",
            "I'll finally be able to make proper meals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A rich meal is the most important thing.\x01",
            "With this, even the patients\x01",
            "will probably cheer up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FD5")

    label("loc_EF3")


    ChrTalk(
        0x8,
        (
            "I asked Mr. Harold  to bring me a lot of\x01",
            "vegetables from Armorica so it seems \x01",
            "I'll finally be able to make proper meals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A rich meal is the most important thing.\x01",
            "With this, even the patients\x01",
            "will probably cheer up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD5")

    Jump("loc_1E0E")

    label("loc_FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_107E")

    ChrTalk(
        0x8,
        (
            "The stress seems to be \x01",
            "gradually increasing for the\x01",
            "visitors staying here too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd like we could send them\x01",
            "back to Crossbell City quick...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E0E")

    label("loc_107E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1279")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B2")

    ChrTalk(
        0x8,
        (
            "Provisions are supplied\x01",
            "from the city, but basically\x01",
            "a lot is preserved food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh boy, the nutritional balance\x01",
            "is simply going to worsen in\x01",
            "the hospital meals too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Somehow the patients and visitors'\x01",
            "facial expressions are gloomy...\x01",
            "I'd like to do something about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1274")

    label("loc_11B2")


    ChrTalk(
        0x8,
        (
            "Only with the provisions supplied\x01",
            "from the city, the nutritional \x01",
            "balance is simply going to worsen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How I wish I could stock\x01",
            "up on fresh vegetables from\x01",
            "Armorica Village like before.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1274")

    Jump("loc_1E0E")

    label("loc_1279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1443")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1385")

    ChrTalk(
        0x8,
        (
            "The city kids over there\x01",
            "seem to be Arc-en-ciel fans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They came to visit Ilya but after the independence \x01",
            "declaration they stayed at the hospital and have\x01",
            "been helping with many things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Uh uh, there're some kind kids too, eh?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_143E")

    label("loc_1385")


    ChrTalk(
        0x8,
        (
            "Those kids are Ilya's fans and after the\x01",
            "independence declaration they stayed at the \x01",
            "hospital and have been helping with many things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Uh uh, there're some kind kids too, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_143E")

    Jump("loc_1E0E")

    label("loc_1443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_15EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1556")

    ChrTalk(
        0x8,
        (
            "I'm also in charge of the\x01",
            "hospital meals menu, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Among the recently newly hospitalised\x01",
            "patients, there're many injured persons\x01",
            "who can't even eat anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Food is tied to energy.\x01",
            "I wish they could become\x01",
            "able to eat something.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15EA")

    label("loc_1556")


    ChrTalk(
        0x8,
        (
            "For now, they're getting nutrients\x01",
            "from intravenous drips, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Food is tied to energy.\x01",
            "I wish they could become\x01",
            "able to eat something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15EA")

    Jump("loc_1E0E")

    label("loc_15EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_17F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1765")

    ChrTalk(
        0x8,
        (
            "Yesterday ambulances were repeatedly coming and\x01",
            "going and I was thinking about what could've happened \x01",
            "but...to think it was a train derailment accident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There was a mad rush to get some kind of\x01",
            "compensation from the railway company,\x01",
            "but I was really glad that there were no dead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even so...\x01",
            "What in the world could the cause be?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17EC")

    label("loc_1765")


    ChrTalk(
        0x8,
        (
            "What in the world could the cause\x01",
            "of the train derailment accident be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm glad there were\x01",
            "no dead, but I'm\x01",
            "worried somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17EC")

    Jump("loc_1E0E")

    label("loc_17F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_18D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1890")

    ChrTalk(
        0x8,
        (
            "Mr. Arios?\x01",
            "He went back to the Guild last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's a difficult time for Shizuku, but\x01",
            "as expected, he seems a busy man.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18CE")

    label("loc_1890")


    ChrTalk(
        0x8,
        (
            "Well then, what shoud I\x01",
            "cook for the boarders tonight...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18CE")

    Jump("loc_1E0E")

    label("loc_18D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1AA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E9")

    ChrTalk(
        0x8,
        (
            "Because of Shizuku's surgery,\x01",
            "Mr. Arios had been sojourning\x01",
            "here for some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Being attended to by a\x01",
            "great father, Shizuku too\x01",
            "must've been reassured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, they say the surgery\x01",
            "had disappointing results.\x01",
            "*sigh*...that's too much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AA1")

    label("loc_19E9")


    ChrTalk(
        0x8,
        (
            "Mr. Arios sojourned here for \x01",
            "some time to attend to Shizuku.\x01",
            "I'm sure she felt reassured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, they say the surgery\x01",
            "had disappointing results.\x01",
            "*sigh*...that's too much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA1")

    Jump("loc_1E0E")

    label("loc_1AA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1BFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B75")

    ChrTalk(
        0x8,
        (
            "Today, it seems that Miss Eolia,\x01",
            "the Bracer, came for a job, so\x01",
            "I gave her a lunch for free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The hospital is greatly \x01",
            "indebted to those kids.\x01",
            "It was a minimal thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BF8")

    label("loc_1B75")


    ChrTalk(
        0x8,
        (
            "The hospital is greatly \x01",
            "indebted to the Bracers too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Every now and then, I have to\x01",
            "at least give them a lunch for free.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BF8")

    Jump("loc_1E0E")

    label("loc_1BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1CAA")

    ChrTalk(
        0x8,
        (
            "Archduke Albert...\x01",
            "Although young, he's the\x01",
            "head of state of Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They say he's beloved by his citizens too...\x01",
            "I'm sure he's an excellent man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E0E")

    label("loc_1CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1E0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DAE")

    ChrTalk(
        0x8,
        (
            "It seems there's a new medical\x01",
            "intern in the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Look, he's that kid over there, Micheau.\x01",
            "It seems he self-studied in Crossbell City.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I really love hard workers, you know.\x01",
            "I have to give him lots of free stuff.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E0E")

    label("loc_1DAE")


    ChrTalk(
        0x8,
        "I really love hard workers, you know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I have to give the newcomer\x01",
            "lots of free stuff.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E0E")

    Jump("loc_AF2")

    label("loc_1E13")

    TalkEnd(0x8)
    Return()

    # Function_7_AA0 end

    def Function_8_1E17(): pass

    label("Function_8_1E17")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1E9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E35")
    Call(0, 9)
    Jump("loc_1E96")

    label("loc_1E35")


    ChrTalk(
        0x9,
        "Eat a lot, Micheau.\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hey hey, if you don't eat slowly,\x01",
            "it'll get stuck in your throat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E96")

    Jump("loc_263E")

    label("loc_1E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1F1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EB6")
    Call(0, 9)
    Jump("loc_1F1A")

    label("loc_1EB6")


    ChrTalk(
        0x9,
        (
            "...At any rate, we can't do\x01",
            "anything about that...\x01",
            "Let's focus on the hospital things for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F1A")

    Jump("loc_263E")

    label("loc_1F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1FCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3A")
    Call(0, 9)
    Jump("loc_1FC6")

    label("loc_1F3A")


    ChrTalk(
        0x9,
        (
            "Micheau too, you've\x01",
            "got used to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although before you were complaining\x01",
            "that you couldn't eat while we were\x01",
            "reading such a book.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC6")

    Jump("loc_263E")

    label("loc_1FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_20A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FE6")
    Call(0, 9)
    Jump("loc_20A4")

    label("loc_1FE6")


    ChrTalk(
        0x9,
        (
            "Constantly studying is important.\x01",
            "It takes three days to get back\x01",
            "one day of slacking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You may be worried about the city, but it's \x01",
            "something that you must do properly.\x01",
            "...Got it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A4")

    Jump("loc_263E")

    label("loc_20A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2113")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20C4")
    Call(0, 9)
    Jump("loc_210E")

    label("loc_20C4")


    ChrTalk(
        0x9,
        (
            "...Now Micheau, sit down.\x01",
            "We have to eat well for the afternoon too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_210E")

    Jump("loc_263E")

    label("loc_2113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_21E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_212E")
    Call(0, 9)
    Jump("loc_21DF")

    label("loc_212E")


    ChrTalk(
        0x9,
        (
            "Well, evaluation is something\x01",
            "that is going to follow later...\x01",
            "Whether one likes it or not, work increases.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For now, I have to be happy \x01",
            "that the patients were saved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21DF")

    Jump("loc_263E")

    label("loc_21E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2284")

    ChrTalk(
        0x9,
        (
            "Well then, I have a little time\x01",
            "until today's lecture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Micheau is not here yet, I guess I'll do\x01",
            "some self-study while having breakfast.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_263E")

    label("loc_2284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2381")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_229F")
    Call(0, 9)
    Jump("loc_237C")

    label("loc_229F")


    ChrTalk(
        0x9,
        (
            "Lytton has been doing desperate efforts since\x01",
            "the time of his previous coaching teacher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it's in studying I don't lose too, but\x01",
            "it wouldn't be strange he didn't grow up\x01",
            "after doing that much efforts on site.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_237C")

    Jump("loc_263E")

    label("loc_2381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2467")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_239C")
    Call(0, 9)
    Jump("loc_2462")

    label("loc_239C")


    ChrTalk(
        0x9,
        (
            "*munch munch*...\x01",
            "Well, it's a path everyone goes through\x01",
            "when you're a medical intern, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You can't always avoid lunch\x01",
            "from now on too, you know?\x01",
            "Uh uh, you'll get used to it soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2462")

    Jump("loc_263E")

    label("loc_2467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_24FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2482")
    Call(0, 9)
    Jump("loc_24F6")

    label("loc_2482")


    ChrTalk(
        0x9,
        (
            "Micheau, so it will be your first\x01",
            "time seeing a surgery live...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Uh uh...well, let's see what you've got.\x02",
    )

    CloseMessageWindow()

    label("loc_24F6")

    Jump("loc_263E")

    label("loc_24FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_263E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D3")

    ChrTalk(
        0x9,
        (
            "I was entrusted to coach\x01",
            "a newcomer, Micheau.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Uhhm, my studying hours\x01",
            "will get reduced, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, this is studying too.\x01",
            "Since this is an opportunity, I'll do it severely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_263E")

    label("loc_25D3")


    ChrTalk(
        0x9,
        (
            "Well, coaching a cute junior\x01",
            "is studying too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Since this is an opportunity, I'll do it severely.\x02",
    )

    CloseMessageWindow()

    label("loc_263E")

    TalkEnd(0x9)
    Return()

    # Function_8_1E17 end

    def Function_9_2642(): pass

    label("Function_9_2642")

    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_274E")

    ChrTalk(
        0x9,
        (
            "Micheau, because many\x01",
            "patients have come,\x01",
            "eat plenty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll have you work hardly\x01",
            "on site too tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Y-Yes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Alright, I'll do it!!\x01",
            "*chomp chomp chomp chomp*...!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ahaha, if you don't eat slowly\x01",
            "it'll get stuck in your throat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_333C")

    label("loc_274E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_28E6")

    ChrTalk(
        0x9,
        (
            "The independent state declaration of invalidity, eh ...?\x01",
            "I wonder what's going to happen from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At any rate, I'm worried about the\x01",
            "people of the Downtown apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems that even the applications to go back \x01",
            "to the city won't be accepted for a while...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...At any rate, we can't do\x01",
            "anything about that...\x01",
            "Let's focus on the hospital things for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "...Right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_333C")

    label("loc_28E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2A58")

    ChrTalk(
        0x9,
        (
            "*munch munch*...\x01",
            "And so, about the human organs\x01",
            "like these illustrated here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*chomp chomp*...\x01",
            "Hm, I see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Uh uh, even so,\x01",
            "you've got used\x01",
            "to it too, Micheau.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although before you were complaining\x01",
            "that you couldn't eat while we were\x01",
            "reading such a book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*munch munch*...\x01",
            "Ha ha, this too is the result\x01",
            "of your training, senior.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_333C")

    label("loc_2A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2B8B")

    ChrTalk(
        0x9,
        (
            "Micheau, are you studying\x01",
            "properly as of late?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well...\x01",
            "I'm in no mood for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Crossbell is in such a state and I'm worried\x01",
            "about the people of the apartment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I see...\x01",
            "Well, I think it can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, when you calm down,\x01",
            "you must study properly.\x01",
            "...Got it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_333C")

    label("loc_2B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2CEC")

    ChrTalk(
        0xA,
        (
            "Among the injured persons of the raid incident, there\x01",
            "was someone who couldn't be saved no matter what...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Senior...it's like...my heart is breaking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I know how you feel.\x01",
            "However, let's leave the complaints\x01",
            "after everything is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you have such free time,\x01",
            "you can save even one more person.\x01",
            "That's our job.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    Jump("loc_333C")

    label("loc_2CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E96")

    ChrTalk(
        0x9,
        "*sigh*, we can finally take a breather.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Nevertheless, it seems you\x01",
            "were doing quite your best \x01",
            "and helping out too, Micheau.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "W-Well...\x01",
            "I've still got a long way to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even if you say I was helping out,\x01",
            "I was just doing odd jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't be modest.\x01",
            "Even odd jobs are important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems that lately, even if you\x01",
            "see blood, you've become calm...\x01",
            "Didn't you grow up a little?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_333C")

    label("loc_2E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2FF6")

    ChrTalk(
        0xA,
        (
            "Senior Lytton often helps\x01",
            "with surgeries and does\x01",
            "frequent hospital rounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*sigh*, as expected\x01",
            "he's on a different level\x01",
            "than a newbie like me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lytton has been doing desperate efforts since\x01",
            "the time of his previous coaching teacher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, don't be impatient, don't be.\x01",
            "If you want to grow, study and study!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_333C")

    label("loc_2FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_31D4")

    ChrTalk(
        0x9,
        "*chomp chomp munch munch"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...What's wrong, Micheau?\x01",
            "Why don't you order something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "W-Well, you see...\x01",
            "Didn't we have an on-the-job practical\x01",
            "surgical operation this morning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Seeing a real surgery for the first time,\x01",
            "you know, somehow I don't have any appetite...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Aah, as I thought, that's it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*chomp chomp*...\x01",
            "Well, it's a path everyone goes through,\x01",
            "so you'll get used to it in time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...*burp*...\x01",
            "I-I hope it's like you say.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_333C")

    label("loc_31D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_333C")

    ChrTalk(
        0x9,
        (
            "By the way, Micheau, tomorrow\x01",
            "there's a training surgery\x01",
            "with Professor Gary, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think that it's going to be the\x01",
            "first time you see a real surgery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Man, I feel like I'm genuinely\x01",
            "beginning my doctor studies.\x01",
            "I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Uh uh...how high-spirited you're.\x01",
            "Well, I hope you'll do your best.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)

    label("loc_333C")

    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_2642 end

    def Function_10_3344(): pass

    label("Function_10_3344")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_339E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3362")
    Call(0, 9)
    Jump("loc_3399")

    label("loc_3362")


    ChrTalk(
        0xA,
        (
            "*chomp chomp chomp chomp*...!!\x01",
            "*cough cough*...!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3399")

    Jump("loc_3991")

    label("loc_339E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3458")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33B9")
    Call(0, 9)
    Jump("loc_3453")

    label("loc_33B9")


    ChrTalk(
        0xA,
        (
            "You're right...we're in a situation where\x01",
            "we can even go back to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It would be nice if the situation\x01",
            "changed a little for the better...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3453")

    Jump("loc_3991")

    label("loc_3458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_34C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3473")
    Call(0, 9)
    Jump("loc_34C1")

    label("loc_3473")


    ChrTalk(
        0xA,
        (
            "*munch munch*...\x01",
            "Ha ha, this too is the result\x01",
            "of your training, senior.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34C1")

    Jump("loc_3991")

    label("loc_34C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3574")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34E1")
    Call(0, 9)
    Jump("loc_356F")

    label("loc_34E1")


    ChrTalk(
        0xA,
        (
            "Right...\x01",
            "I'm worried about the people of the apartment too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If I didn't study for that reason,\x01",
            "it would be lacking self-reliance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_356F")

    Jump("loc_3991")

    label("loc_3574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3606")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_358F")
    Call(0, 9)
    Jump("loc_3601")

    label("loc_358F")


    ChrTalk(
        0xA,
        "...It's like you say, senior...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At any rate, now I must \x01",
            "think about saving even\x01",
            "just one more patient.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3601")

    Jump("loc_3991")

    label("loc_3606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3682")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3621")
    Call(0, 9)
    Jump("loc_367D")

    label("loc_3621")


    ChrTalk(
        0xA,
        (
            "Uhhm, I too must reach the point to be entrusted\x01",
            "with important jobs, not only chores.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_367D")

    Jump("loc_3991")

    label("loc_3682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3690")
    Jump("loc_3991")

    label("loc_3690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3752")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36AB")
    Call(0, 9)
    Jump("loc_374D")

    label("loc_36AB")


    ChrTalk(
        0xA,
        (
            "I see... It's true that it'll never\x01",
            "begin even if I'm impatient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...Even so, senior, don't you\x01",
            "think that reading an anatomy\x01",
            "book during mealtime is...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_374D")

    Jump("loc_3991")

    label("loc_3752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_37EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_376D")
    Call(0, 9)
    Jump("loc_37E5")

    label("loc_376D")


    ChrTalk(
        0xA,
        (
            "Uuh, after that surgery,\x01",
            "senior can eat that\x01",
            "meat dish...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Uuh, when I remember it, I feel like throwing up...\x02",
    )

    CloseMessageWindow()

    label("loc_37E5")

    Jump("loc_3991")

    label("loc_37EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_386D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3805")
    Call(0, 9)
    Jump("loc_3868")

    label("loc_3805")


    ChrTalk(
        0xA,
        "Ha ha, please leave it to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll study hard so to not bring\x01",
            "disgrace upon you, senior!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3868")

    Jump("loc_3991")

    label("loc_386D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3991")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3932")

    ChrTalk(
        0xA,
        (
            "Senior Flora is a bit strict,\x01",
            "but her teaching methods\x01",
            "are good, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Her knowledge is quite profound too...\x01",
            "Really, I'm glad I came across\x01",
            "a good senior.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3991")

    label("loc_3932")


    ChrTalk(
        0xA,
        (
            "Senior Flora, can't you do something\x01",
            "about opening the anatomy book\x01",
            "even during mealtime?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3991")

    TalkEnd(0xA)
    Return()

    # Function_10_3344 end

    def Function_11_3995(): pass

    label("Function_11_3995")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3AB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A7D")

    ChrTalk(
        0xFE,
        (
            "Our son was severely injured\x01",
            "in that raid incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He survived, but he's in\x01",
            "the intensive care unit...\x01",
            "I could only see him for a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aah, venerable Goddess...\x01",
            "Please save my son...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3AB2")

    label("loc_3A7D")


    ChrTalk(
        0xFE,
        (
            "Aah, venerable Goddess...\x01",
            "Please save my son...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AB2")

    TalkEnd(0xFE)
    Return()

    # Function_11_3995 end

    def Function_12_3AB6(): pass

    label("Function_12_3AB6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3BD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B78")

    ChrTalk(
        0xFE,
        (
            "My son is one of the CGF members\x01",
            "who fought against the armed group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...If I had known this would've\x01",
            "happened, I should've opposed\x01",
            "him to join the CGF...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3BD2")

    label("loc_3B78")


    ChrTalk(
        0xFE,
        (
            "...If I had known this would've\x01",
            "happened, I should've opposed\x01",
            "him to join the CGF...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BD2")

    TalkEnd(0xFE)
    Return()

    # Function_12_3AB6 end

    def Function_13_3BD6(): pass

    label("Function_13_3BD6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3C57")

    ChrTalk(
        0xFE,
        (
            "Somehow papa and mama have \x01",
            "been looking sad all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Big brother...\x01",
            "I wonder what's happened to him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C57")

    TalkEnd(0xFE)
    Return()

    # Function_13_3BD6 end

    def Function_14_3C5B(): pass

    label("Function_14_3C5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3D09")

    ChrTalk(
        0xFE,
        (
            "My son's family have been hospitalised\x01",
            "here since the raid incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now I could confirm their safety, but...\x01",
            "I can't really calm down my feelings.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D09")

    TalkEnd(0xFE)
    Return()

    # Function_14_3C5B end

    def Function_15_3D0D(): pass

    label("Function_15_3D0D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3DAA")

    ChrTalk(
        0xFE,
        (
            "Such an incident happened and even the police \x01",
            "and the CGF received severe damage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what will be of\x01",
            "Crossbell from now on...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DAA")

    TalkEnd(0xFE)
    Return()

    # Function_15_3D0D end

    def Function_16_3DAE(): pass

    label("Function_16_3DAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3DBF")
    Jump("loc_3FB0")

    label("loc_3DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3E5D")

    ChrTalk(
        0x10,
        (
            "It was decided that we have to bring\x01",
            "the hospital meals to Lady Ilya...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "W-What do I do...\x01",
            "What should I talk about when I meet her!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FB0")

    label("loc_3E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3F06")

    ChrTalk(
        0x10,
        (
            "The truth is that I'd like to scream Lady\x01",
            "Ilya's name so it reaches her room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "However, this is a hospital...\x01",
            "As expected, I must contain myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FB0")

    label("loc_3F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3FB0")

    ChrTalk(
        0x10,
        (
            "I'm really glad Lady Ilya's\x01",
            "regained consciousness!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "It was worth it not going back to the city and\x01",
            "staying here all the time praying for her recovery!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FB0")

    TalkEnd(0xFE)
    Return()

    # Function_16_3DAE end

    def Function_17_3FB4(): pass

    label("Function_17_3FB4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3FC5")
    Jump("loc_420B")

    label("loc_3FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4089")

    ChrTalk(
        0x11,
        (
            "C-Calm down, Police...\x01",
            "We have to bring the meals to\x01",
            "the other hospitalised patients too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "What if fretting out you\x01",
            "spilled even Lady Ilya's share?\x01",
            "Stay calm, stay calm...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_420B")

    label("loc_4089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_415A")

    ChrTalk(
        0x11,
        (
            "While helping out I'm also praying that\x01",
            "Lady Ilya recovers even just one day faster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "That superintendent is a slave driver, but...\x01",
            "When I think it's for Lady Ilya's sake, I don't care!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_420B")

    label("loc_415A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_420B")

    ChrTalk(
        0x11,
        (
            "We're in a hard time, so\x01",
            "we must endure to go\x01",
            "pay a visit to Lady Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "That being the case, we have to help in\x01",
            "the hospital and be useful at least a little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_420B")

    TalkEnd(0xFE)
    Return()

    # Function_17_3FB4 end

    def Function_18_420F(): pass

    label("Function_18_420F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_4220")
    Jump("loc_4491")

    label("loc_4220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_422E")
    Jump("loc_4491")

    label("loc_422E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_423C")
    Jump("loc_4491")

    label("loc_423C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_424A")
    Jump("loc_4491")

    label("loc_424A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4491")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_426D")
    Call(0, 19)
    TalkEnd(0xFE)
    SetChrSubChip(0x15, 0x1)
    Return()

    label("loc_426D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43D5")

    ChrTalk(
        0x15,
        (
            "#01300FWhen I am together with Zeit,\x01",
            "it is very relaxing.\x02\x03",
            "#01304FAlthough I haven't met him that many times,\x01",
            "somehow I am so at ease with him...\x02\x03",
            "#01300FIt is like we had been friends since a long time,\x01",
            "I feel such nostalgia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10400FAhaha, it's as if you\x01",
            "were a pair of lovers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F(I could be a little jealous of that...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4489")

    label("loc_43D5")


    ChrTalk(
        0x15,
        (
            "#01300FWhen I am together with Zeit,\x01",
            "it is very relaxing.\x02\x03",
            "#01304FSomehow I am so at ease with him...\x01",
            "It is like we had been friends since a long time,\x01",
            "I feel such nostalgia.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4489")

    TalkEnd(0xFE)
    SetChrSubChip(0x15, 0x1)
    Return()

    label("loc_4491")

    TalkEnd(0xFE)
    Return()

    # Function_18_420F end

    def Function_19_4495(): pass

    label("Function_19_4495")

    OP_4B(0x16, 0xFF)

    ChrTalk(
        0x15,
        (
            "#01300FNow that I think about it, Zeit, I haven't\x01",
            "seen you since the President's speech.\x02\x03",
            "#01303FYou chased after KeA who\x01",
            "was taken away by Mr. Arios \x01",
            "and I didn't know where you were...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#3C#01200FHm, I did pursue them, but...\x01",
            "When that "Divine Blade" reached the lake,\x01",
            "I was completely shaken off.\x02\x03",
            "I felt sorry for Lloyd and the others,\x01",
            "but I went back to my subordinates to\x01",
            "make preparations.\x02\x03",
            "#01203FCome to think of it, I caused you,\x01",
            "who were there, some needless worries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#01302F*chuckle*, I am fine.\x01",
            "More importantly, I am glad\x01",
            "that you are safe, Zeit.\x02\x03",
            "#01300FAlso, you are helping with all your \x01",
            "might Lloyd and Wazy even now.\x02\x03",
            "#01304FUh uh, thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Cecil gently stroked Zeit's head.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x16, 0xFFFFFDA8, 2100, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        "#3C#01200F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#01303FWhen I am together with you, Zeit,\x01",
            "for some reason I feel a lot at ease.\x02\x03",
            "#01305FAh... I am sorry.\x01",
            "Did I offend you by stroking\x01",
            "you so friendly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#3C#01200F...Hu hu, no.\x01",
            "It wasn't a bad feeling.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 1)
    ClearChrFlags(0x15, 0x10)
    OP_4C(0x16, 0xFF)
    Return()

    # Function_19_4495 end

    def Function_20_487F(): pass

    label("Function_20_487F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_49E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_489D")
    Call(0, 19)
    Jump("loc_49E4")

    label("loc_489D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_496D")

    ChrTalk(
        0x16,
        "#3C#01203F......Hu hu............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(I...wonder what's wrong with Zeit?\x01",
            "He sank into silence...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(Maybe he is feeling awkward after\x01",
            "he was stroked by Miss Cecil?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_49E4")

    label("loc_496D")


    ChrTalk(
        0x16,
        (
            "#3C#01200F...To not throw the hospital into confusion,\x01",
            "I'll be waiting for you here.\x02\x03",
            "You can go pay your visits.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49E4")

    TalkEnd(0xFE)
    Return()

    # Function_20_487F end

    def Function_21_49E8(): pass

    label("Function_21_49E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4C0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B55")

    ChrTalk(
        0xFE,
        (
            "Some time ago, my husband had spasm for his chronic disease.\x01",
            "We came here in a rush with the ambulance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm glad the application was accepted somehow, but...\x01",
            "Since the inspection was so strict, I was on\x01",
            "pin and needles about what if it was rejected...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... Maybe staying like this\x01",
            "in the hospital is not that safe.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4C0B")

    label("loc_4B55")


    ChrTalk(
        0xFE,
        (
            "Some time ago, my husband had spasm for his chronic disease.\x01",
            "We came here in a rush with the ambulance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... Maybe staying like this\x01",
            "in the hospital is not that safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C0B")

    TalkEnd(0xFE)
    Return()

    # Function_21_49E8 end

    def Function_22_4C0F(): pass

    label("Function_22_4C0F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4E6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D73")

    ChrTalk(
        0xFE,
        (
            "Because I couldn't commute to the hospital\x01",
            "I ran out of medicine for my chronic disease\x01",
            "and I had some spasm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The movements restrictions on the highway\x01",
            "is indeed a pain that I'll remember it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To go back to the city we need to wait\x01",
            "the next time the State Guard comes...\x01",
            "I guess I'll take it slowly for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_4E6D")

    label("loc_4D73")


    ChrTalk(
        0xFE,
        (
            "Getting carried to the hospital is indeed \x01",
            "a pain due to the movements restriction\x01",
            "on the highway that I'll remember it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To go back to the city we need to wait\x01",
            "the next time the State Guard comes...\x01",
            "I guess I'll take it slowly for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E6D")

    TalkEnd(0xFE)
    Return()

    # Function_22_4C0F end

    def Function_23_4E71(): pass

    label("Function_23_4E71")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4F4A")

    ChrTalk(
        0xFE,
        (
            "I planned to go back to the city today...\x01",
            "What's going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know anything about a declaration\x01",
            "of invalidity, but even if they took just me to\x01",
            "the city, they probably wouldn't be punished.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F4A")

    TalkEnd(0xFE)
    Return()

    # Function_23_4E71 end

    def Function_24_4F4E(): pass

    label("Function_24_4F4E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4F5F")
    Jump("loc_5058")

    label("loc_4F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5058")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F7A")
    Call(0, 30)
    Jump("loc_5058")

    label("loc_4F7A")


    ChrTalk(
        0xFE,
        (
            "We have to go to the St. Ursula sandbank\x01",
            "in order to investigate the nexus between the\x01",
            ""Azure Flowers" and the Cryptids that you reported.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, no need to worry about us.\x01",
            "You should just focus\x01",
            "on your own jobs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5058")

    TalkEnd(0xFE)
    Return()

    # Function_24_4F4E end

    def Function_25_505C(): pass

    label("Function_25_505C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_506D")
    Jump("loc_5A54")

    label("loc_506D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_52B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5088")
    Call(0, 30)
    Jump("loc_52AD")

    label("loc_5088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51F5")

    ChrTalk(
        0xFE,
        (
            "*cough*, by the way,\x01",
            "about those Azure Flowers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "According to your written report,\x01",
            "it seems they were ingredients\x01",
            "for that "Gnosis".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that the ringleader, Joachim\x01",
            "Gｸnther, manufactured a great amount\x01",
            "of that drug during the Cult incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder where he was stocking up on\x01",
            ""Pleroma Grass", the needed ingredient.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_52AD")

    label("loc_51F5")


    ChrTalk(
        0xFE,
        (
            "It seems that Joachim Gｸnther \x01",
            "manufactured a great amount of\x01",
            "Gnosis during the Cult incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder where he was stocking up on\x01",
            ""Pleroma Grass", the needed ingredient.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52AD")

    Jump("loc_5A54")

    label("loc_52B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_52C0")
    Jump("loc_5A54")

    label("loc_52C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5A54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5671")

    ChrTalk(
        0x101,
        "#00005FOh, Miss Eol──\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_539C")
    Jump("loc_53E6")

    label("loc_539C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_53BC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_53E6")

    label("loc_53BC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53DC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_53E6")

    label("loc_53DC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_53E6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "#4SLittle T-Tio...\x01",
            "You've finally come back!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F...Good morning, it has been a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aah...\x01",
            "How many times did I dream of this day!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come here, little Tio!\x01",
            "Big sister will kiss you all over!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F...I firmly refuse to.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*ahn*, it's been some time I felt this too...㈱\x02",
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
            "#00211F(...I don't know why but I feel like she's\x01",
            "become a more formidable foe than before.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(H-Ha ha... In the time she hasn't seen you,\x01",
            "her feelings probably have piled up.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetScenarioFlags(0x1C0, 7)
    Jump("loc_5A54")

    label("loc_5671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58D1")
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x103, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_570C")
    Jump("loc_5756")

    label("loc_570C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_572C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5756")

    label("loc_572C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_574C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5756")

    label("loc_574C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5756")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "To be able to meet little Tio for coming\x01",
            "to deliver a package due to a request is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Honestly, couldn't this be fate!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211FIt is not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*ahn*...a swift response......㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FMiss Eolia, in that case,\x01",
            "I could be a replacem...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhhm, I don't want you㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F*gasp*...\x01",
            "I got a swift response too!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_5A50")

    label("loc_58D1")

    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x103, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5962")
    Jump("loc_59AC")

    label("loc_5962")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5982")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_59AC")

    label("loc_5982")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59A2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_59AC")

    label("loc_59A2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_59AC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Uh uh, little Tio.\x01",
            "Let me have some skinship next time too, ok?㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F(Of course, I'll need to be careful...yes.)\x02",
    )

    CloseMessageWindow()

    label("loc_5A50")

    SetChrSubChip(0xFE, 0x0)

    label("loc_5A54")

    TalkEnd(0xFE)
    Return()

    # Function_25_505C end

    def Function_26_5A58(): pass

    label("Function_26_5A58")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "3F: Female Dormitory→\x01\x01",
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

    # Function_26_5A58 end

    def Function_27_5ABE(): pass

    label("Function_27_5ABE")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　Accomodation for Visitors and Outpatients　\x01",
            "※In case you need one, please ask the superintendent.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_5ABE end

    def Function_28_5B5A(): pass

    label("Function_28_5B5A")

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
        "#00206F#5P...So such things have...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#06406F#5PS-Somehow it's too grand\x01",
            "that I can't understand it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#01303F#5PThe Crossbell where we live...\x02\x03",
            "#01308FThere were some sequence of events and...\x01",
            "Now I understand some things.\x02\x03",
            "#01301FAbout the situation we are in, and about KeA too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#12P...Yeah.\x02\x03",
            "#00003FI only wish for two things.\x02\x03",
            "To ascertain with my own eyes\x01",
            "the truth that I don't know yet──\x02\x03",
            "#00013FAnd to free everyone,\x01",
            "and get KeA back.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x105, 0x1)
    Sleep(150)

    ChrTalk(
        0x105,
        (
            "#10409F#12PHu hu, although you can say they're only two,\x01",
            "they seem they'll be absurdly difficult to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01203F#11P#3CWell, they suit him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#5PUh uh...\x01",
            "That's who Mr. Lloyd is.\x02\x03",
            "#00204F──My feelings are the\x01",
            "same as Mr. Lloyd's.\x02\x03",
            "#00203FAs an SSS member...\x02\x03",
            "#00201FAnd even more, as one of KeA's guardians...\x01",
            "Please, take me along with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PThank you, Tio.\x01",
            "I'll count on you without reserve.\x02\x03",
            "#00005FHowever, why were you\x01",
            "brought here, Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#5P...Maybe Miss Mariabell ordered\x01",
            "Mr. Arios to do it.\x02\x03",
            "#00208FThey are observing the divided SSS\x01",
            "members, each one in a different place...\x02\x03",
            "#00201FI believe they think that if they had poorly\x01",
            "left us all in the same place, we could\x01",
            "have influenced KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PI see...\x02\x03",
            "#00008FAnd that means Elie and Randy too\x01",
            "seem to be in different places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PUhhm, if they're in Crossbell City,\x01",
            "it would be impossible to free them...\x02\x03",
            "#10402FThe fact that Tio was here means that\x01",
            "it's very likely they can be outside the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#01306F#5PRight... It seems they are trying to not\x01",
            "make you four get close to KeA.\x02",
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

    def lambda_636B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_636B)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x19,
        (
            "#06403F#5PE-Excuse me...!\x02\x03",
            "#06401FCould you take\x01",
            "me with you too!?\x02",
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
        "#01305F#5PMiss Fran?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#06406F#5PI-I can't fight like\x01",
            "all of you, but...\x02\x03",
            "#06403FEven so, I think I could do\x01",
            "all right as an operator!\x02\x03",
            "#06401FIt seems you're moving with\x01",
            "Mr. Wazy's airship, so...\x02\x03",
            "Please...!\x01",
            "I want to help you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PFran... \x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x103, 0x0)
    Sleep(150)

    ChrTalk(
        0x103,
        "#00208F#5PMr. Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#12PUhhm, it's true that the "Merkabah" is short\x01",
            "of hands so you could be of help...\x02\x03",
            "#10400FI'll have to let Lloyd\x01",
            "decide on this one.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00006F#6P...Right.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00003F#6PFran──your big sister is currently\x01",
            "working for the State Guard.\x02\x03",
            "#00008FComing with us means\x01",
            "to fight against Noｱl...\x02\x03",
            "#00001FDo you understand that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#06406F#5P...Y-Yes...!\x02\x03",
            "#06408FOf course I don't want to\x01",
            "pick a fight with big sis, but...\x02\x03",
            "#06401FNevertheless... Even I am\x01",
            "a Crossbell Police officer!\x02\x03",
            "I can't leave alone...\x01",
            "Such a dangerous situation!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PI see...\x02\x03",
            "#00002F──All right.\x01",
            "Thank you for your cooperation.\x02",
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
            "#00202F#5PMiss Fran...\x01",
            "I am happy for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#12PHu hu, I guess that Abbas' work\x01",
            "is going to become a little easier too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#01309F#5PUh uh...\x01",
            "It seems it is settled.\x02",
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
            "#00000F#12PYeah...\x01",
            "It's time to go, sister Cecil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#01304F#5PYes, please be extremely careful.\x02\x03",
            "#01303FI can't help you all\x01",
            "directly, however...\x02\x03",
            "#01302FI will pray for you while\x01",
            "I am working here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#12PThanks.\x01",
            "...That's really enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#5P...Miss Cecil.\x01",
            "Thank you for everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#06411F#11PS-Someone like me...\x01",
            "I owe you so much.\x02\x03",
            "#06406F#30W*sob*...uuuh...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x15, 0x1)
    Sleep(150)

    ChrTalk(
        0x15,
        (
            "#01309F#5PUh uh, you are going to mess your cute face, no?\x02\x03",
            "#01305FBy the way Miss Fran, is it\x01",
            "all right not packing your things?\x02\x03",
            "#01302FWouldn't it be better to take with you\x01",
            "at least one change of clothes...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x19,
        "#06405F#11PI-I have to pack my things!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x101, 500)

    ChrTalk(
        0x19,
        (
            "#06412F#5PP-Please wait just\x01",
            "a little while!\x02",
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
        "#00002F#12PHa ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#11P#3CHm, it seems that things\x01",
            "are going to become lively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#12PIt seems it'll become a little\x01",
            "cheerful even inside the Merkabah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#01304F#5PUh uh...\x02",
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
            "#00005F#12PWhat......!?\x01",
            "Could it be that they...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#01304F#5PYes, they have regained consciousness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#5PMiss Ilya can't\x01",
            "walk yet, but...\x02\x03",
            "#00202FIt seems that Inspector Donovan\x01",
            "is recovering well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#12PI see...thank goodness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#12PJust waiting for Fran would be...you know...\x01",
            "Why don't we try to visit them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#12PYeah, let's do like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5PI will come with you too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#11P#3CHm, since I would throw the patients into\x01",
            "confusion, I'll be waiting here for you.\x02",
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
            "Zeit left the party temporarily.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tio has joined the party.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71C0")
    SetChrFlags(0x15, 0x10)

    label("loc_71C0")

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

    # Function_28_5B5A end

    def Function_29_7205(): pass

    label("Function_29_7205")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x8000)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xFA0, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x138, 0x3E80, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x10B, 0x1F40, 0x1388, 0x1)
    Return()

    # Function_29_7205 end

    def Function_30_7253(): pass

    label("Function_30_7253")

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
            "#11P#00000FMiss Ling, Miss Eolia...\x01",
            "You came to St. Ursula Hospital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00100FDid you have some kind of request?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#6PWell, because we're going to investigate that\x01",
            "Cryptid now, we're making some preparations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#6PWe're now going to the St. Ursula Byroad sandbank\x01",
            "where you exterminated that Cryptid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#6PIt's to search for a connection between the\x01",
            ""Azure Flowers" and the Cryptid that your reported.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#5PIncidentally, Mr. Arios who just came\x01",
            "back is dealing with the extermination of\x01",
            "the remaining Cryptid that was spotted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10105FIs that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#00300FSomethin' we can help with?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#5PUhhm, no, we're fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#5PWell, if I could get some skinship with\x01",
            "little Tio when I come back, I think I\x01",
            "could do my best no matter what㈱\x02",
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
        "#5P*ahn*, no waaay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FAhaha, you never change.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#6PWell, it means you have no need to worry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#6PYou do the things\x01",
            "only you can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FYes, understood.\x01",
            "Please do your best too.\x02",
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

    # Function_30_7253 end

    def Function_31_776C(): pass

    label("Function_31_776C")

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
            "#5P#01300F...Then, Tio is not\x01",
            "coming back for\x01",
            "some more time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYeah. It seems she's\x01",
            "busy with many things.\x02\x03",
            "#00002FI guess that she's doing her best in the\x01",
            "autonomous state of Leman right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5P#01304FI see...\x01",
            "Then, I can't wait to see her.\x02\x03",
            "#01309FUh uh, when she comes back,\x01",
            "I will have to ask her all kind of stories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FHa ha...right.\x02\x03",
            "#00000FI'm sure that Tio too will be\x01",
            "delighted to see you, sister Cecil.\x02",
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
        "#6P#10105FEeh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10304FUhmm...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        "#12P#00005FW-What's with you two?\x02",
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
            "#6P#10109FW-Well...\x01",
            "I had heard the rumors,\x01",
            "but you really get along well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10302FI was being a little jealous\x01",
            "since I couldn't cut in...\x02",
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
            "#6P#00306FTch, this guy is\x01",
            "always like this.\x02\x03",
            "#00301FHe's such a lucky dog even just\x01",
            "for havin' been acquainted with\x01",
            "such a miss since he was a kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00106FReally, it's as you say...\x02\x03",
            "#00111FIf he thinks she's granted,\x01",
            "one day he'll be punished for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FI-I don't get what you mean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#5P#01309FUh uh...\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x15,
        (
            "#5P#01305FAh, by the way, I was unconsciously\x01",
            "taken by the conversation, but...\x02\x03",
            "#01300FDid you come to the hospital\x01",
            "for some business today?\x02",
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
            "#12P#00005FAh...yes, we did.\x02\x03",
            "#00000F...*cough*, actually...\x01",
            "A request came to the SSS from\x01",
            "a certain "Professor Seiland".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FIf I remember correctly, this person\x01",
            "came here as the pharmacology and\x01",
            "neurology successor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5P#01302FYes, that's true.\x02\x03",
            "#01303FWhen it was publically announced that Doctor\x01",
            "Joachim was manufacturing a mysterious drug,\x01",
            "the hospital went in an uproar temporarily.\x02\x03",
            "#01308FThe professors did efforts\x01",
            "for the after care while doing\x01",
            "their jobs for a while, but...\x02\x03",
            "#01300FThey finally got back the \x01",
            "patients' trust only recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FWell...\x01",
            "It must've been hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5P#01309FUh uh...\x01",
            "Thank goodness the situation settled.\x02\x03",
            "#01300FThe scars from that incident healed too,\x01",
            "and finally St. Ursula Hospital made\x01",
            "new steps forward.\x02\x03",
            "As part of those, \x01",
            "Professor Seiland was newly\x01",
            "called from Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00100FA person related to the Seiland Corporation, the\x01",
            "famous medical equipment manufacturer...right?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x2)

    ChrTalk(
        0x15,
        (
            "#11P#01300FYes, that person should be\x01",
            "a relative of the founder.\x02\x03",
            "#01304FShe's a woman, but she\x01",
            "has a commanding air to\x01",
            "her and she's very cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FOoh, a female doctor!\x01",
            "Man, I really look forward to it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FS-Setting aside her air...\x02\x03",
            "#00000FI see, this time the\x01",
            "references are\x01",
            "completely assured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10300FHm, she's a professor,\x01",
            "but are her skills real?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#01300FIt seems she's a famous pharmacology and\x01",
            "neurology researcher in Remiferia too.\x02\x03",
            "#01304FJust recently she was perfectly successful\x01",
            "in the surgery for Mihail who had been\x01",
            "hospitalised here with a severe illness.\x02\x03",
            "#01300FNow she's advancing the preparations\x01",
            "for Shizuku's surgery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00105FShizuku's...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FI see...\x01",
            "She really seems an amazing doctor...\x02\x03",
            "Do you know where that\x01",
            "Professor Seiland is now?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x15,
        (
            "#5P#01300FYes, she's usually holed up in\x01",
            "the lab in the research building.\x02\x03",
            "If you ask Miss Sera at the reception,\x01",
            "I think you could be announced.\x02\x03",
            "#01309FUh uh, since I am here,\x01",
            "I will go there with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah, thank you.\x01",
            "...Let's go then.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t1530", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_776C end

    def Function_32_8634(): pass

    label("Function_32_8634")

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
            "My, welcome.\x01",
            "Came to eat something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, we're from the\x01",
            "Special Support Section...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that you came to collect data\x01",
            "for the "gourmet recommendations".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Aah, the Gourmet Guide thing, right?\x01",
            "I've heard from a C.N.S. person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...Still, that's a problem.\x02",
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
            "My recommended dish needs\x01",
            "to boil for quite some time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I just ran out of it.\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm sorry, but now I'm\x01",
            "not prepared to treat\x01",
            "you to that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303FHmm, can't be helped then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FHow much will it take\x01",
            "until it is ready?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89B9")

    ChrTalk(
        0x8,
        (
            "Let's see, I just began\x01",
            "preparing it last night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It'll take two days to be ready,\x01",
            "so the day after tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A18")

    label("loc_89B9")


    ChrTalk(
        0x8,
        (
            "Let's see, I began preparing\x01",
            "it the day before yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "It'll be ready tomorrow.\x02",
    )

    CloseMessageWindow()

    label("loc_8A18")


    ChrTalk(
        0x109,
        "#10105FI-It boils even for three days...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, I'm sure the taste will be rich.\x01",
            "I'll look forward to its completion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, it'll be tasty for sure.\x01",
            "Don't forget to come when it's ready.\x02",
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

    # Function_32_8634 end

    def Function_33_8B26(): pass

    label("Function_33_8B26")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 1)), scpexpr(EXPR_END)), "loc_8D14")

    ChrTalk(
        0x8,
        (
            "Aah, you guys.\x01",
            "It seems you didn't forget and came.\x02",
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
        "#00005FT-Then that means...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, my recommended dish,\x01",
            "the "Three-Day Stew",\x01",
            "is finally ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Wanna eat it at once?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EBD")

    label("loc_8D14")


    ChrTalk(
        0x8,
        (
            "My, welcome.\x01",
            "Came to eat something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, we're from the\x01",
            "Special Support Section...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that you came to collect data\x01",
            "for the "gourmet recommendations".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Aah, the Gourmet Guide thing, right?\x01",
            "I've heard from a C.N.S. person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, you've come just at the right time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just moments ago, my recommended\x01",
            "dish, the "Three-Day Stew",\x01",
            "was completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Wanna eat it at once?\x02",
    )

    CloseMessageWindow()

    label("loc_8EBD")


    ChrTalk(
        0x103,
        "#00200FYes, by all means.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, wait a moment.\x01",
            "I'll serve for each one of you.\x02",
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
            "Lloyd and the others ate the Three-Day Stew.\x07\x00\x02",
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
        "#10105F#4S...D-Delicious...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FYeah...it incredibly melts in your mouth\x01",
            "and the taste is absurdly rich.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 1)), scpexpr(EXPR_END)), "loc_90B4")

    ChrTalk(
        0x105,
        "#10302FHu hu, it was worth the wait.\x02",
    )

    CloseMessageWindow()
    Jump("loc_90FF")

    label("loc_90B4")


    ChrTalk(
        0x105,
        (
            "#10302FHu hu, on such a rainy day,\x01",
            "it could be the best dish to have.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90FF")


    ChrTalk(
        0x102,
        (
            "#00100FYes, really...\x01",
            "It could be the first time in my life\x01",
            "that I ate such a delicious stew...!\x02\x03",
            "#00103FIt warms your body, it's full of nutrients...\x01",
            "I think it's really good for your body.\x02\x03",
            "#00109FEven the people who are ill seem they could\x01",
            "feel better at once just by eating this.\x02",
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
        "#00009FYou have a very happy face...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)

    ChrTalk(
        0x8,
        "Ahaha, you're exaggerating.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    ChrTalk(
        0x103,
        (
            "#00200FIt seems Miss Elie liked it a lot...\x01",
            "It would seem good to leave \x01",
            "the article about this to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, you're right.\x01",
            "Elie, can I count on you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#00100FYes, by all means, please leave it to me.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x173, 1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_93C5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_93C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_93E2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_93E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_93F5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_93F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_9408")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_9425")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_9438")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_9455")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_9468")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_9485")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_9498")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_94B5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_94B5")

    OP_29(0x80, 0x1, 0xA)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_95DD")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Finished to collect data from six food places!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_95D4")

    AnonymousTalk(
        0x101,
        (
            "#00003FIt seems we could go report\x01",
            "to Miss Grace immediately, but...\x02\x03",
            "#00000FWe haven't found all six members'\x01",
            "favourites yet, so why don't we\x01",
            "try our best a little more?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_95D4")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_95DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_96C1")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found the entire SSS\x01",
            "members' favourites!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this, we found all\x01",
            "six members' favourites.\x02\x03",
            "We have plenty of data now.\x01",
            "Let's go now to the News Service to report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_96C1")

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

    # Function_33_8B26 end

    SaveToFile()

Try(main)
