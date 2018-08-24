from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2010.bin",                # FileName
        "t2010",                    # MapName
        "t2010",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1C,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 89, 0, 5, 0, 6],
    )

    BuildStringList((
        "t2010",                  # 0
        "Connors ",               # 1
        "Sig",                    # 2
        "Stella",                 # 3
        "Cless ",                 # 4
        "Beyond",                 # 5
        "Tourist",                # 6
        "Tourist",                # 7
        "Tourist",                # 8
        "Girl",                   # 9
        "Tourist",                # 10
        "Tourist",                # 11
        "Romeo ",                 # 12
        "2nd Lt. Mireille",       # 13
        "Harold",                 # 14
        "Bracer Scott",           # 15
        "Bracer Wenzel",          # 16
        "導力車",                 # 17
        "Commander Sonya",        # 18
    ))

    AddCharChip((
        "chr/ch31202.itc",                   # 00
        "chr/ch24900.itc",                   # 01
        "chr/ch31200.itc",                   # 02
        "chr/ch24800.itc",                   # 03
        "chr/ch33000.itc",                   # 04
        "chr/ch33002.itc",                   # 05
        "chr/ch33100.itc",                   # 06
        "chr/ch33102.itc",                   # 07
        "chr/ch33302.itc",                   # 08
        "chr/ch34400.itc",                   # 09
        "chr/ch34402.itc",                   # 0A
        "chr/ch32400.itc",                   # 0B
        "chr/ch32402.itc",                   # 0C
        "chr/ch32600.itc",                   # 0D
        "chr/ch33200.itc",                   # 0E
        "chr/ch33202.itc",                   # 0F
        "chr/ch41400.itc",                   # 10
        "chr/ch41402.itc",                   # 11
        "chr/ch33300.itc",                   # 12
        "chr/ch09300.itc",                   # 13
        "chr/ch27202.itc",                   # 14
        "chr/ch27302.itc",                   # 15
    ))

    DeclNpc(4294960706, 0,       7079,    200,  261,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(16079,   0,       3700,    90,   261,  0x0, 0,   2,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(4294861796, 0,       2099,    90,   261,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294869826, 150,     4294963346, 270,  325,  0x0, 0,   0,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(4294805186, 0,       4294964796, 90,   261,  0x0, 0,   3,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4294872627, 150,     2319,    90,   453,  0x0, 0,   5,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(579,     0,       4179,    180,  389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294872627, 150,     2319,    90,   453,  0x0, 0,   8,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(4294964146, 0,       2960,    180,  389,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(4294963796, 0,       3180,    145,  389,  0x0, 0,   11,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(4294875167, 150,     4190,    270,  453,  0x0, 0,   15,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(3289,    0,       4294959057, 0,    389,  0x0, 0,   2,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   13,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(14180,   0,       4294961626, 135,  389,  0x0, 0,   19,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(4294865197, 150,     2230,    90,   452,  0x0, 0,   20,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(4294867847, 150,     2230,    270,  452,  0x0, 0,   21,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(4294960696, 0,       6140,    1000,    4294960706, 1500,    7080,    0x007E, 0,  7,  0x0000)
    DeclActor(4294863646, 0,       1450,    1000,    4294861796, 1500,    2100,    0x007E, 0,  10, 0x0000)
    DeclActor(4294806156, 0,       4294964596, 1000,    4294805186, 1500,    4294964796, 0x007E, 0,  13, 0x0000)
    DeclActor(3130,    0,       4294954796, 1000,    3130,    1500,    4294954796, 0x007C, 0,  31, 0x0000)

    ChipFrameInfo(1012, 0)                                       # 0

    ScpFunction((
        "Function_0_3F4",          # 00, 0
        "Function_1_4A4",          # 01, 1
        "Function_2_541",          # 02, 2
        "Function_3_5F2",          # 03, 3
        "Function_4_67B",          # 04, 4
        "Function_5_718",          # 05, 5
        "Function_6_ACA",          # 06, 6
        "Function_7_D77",          # 07, 7
        "Function_8_D7B",          # 08, 8
        "Function_9_1AE3",         # 09, 9
        "Function_10_2741",        # 0A, 10
        "Function_11_2745",        # 0B, 11
        "Function_12_35F3",        # 0C, 12
        "Function_13_4333",        # 0D, 13
        "Function_14_4337",        # 0E, 14
        "Function_15_54FD",        # 0F, 15
        "Function_16_5878",        # 10, 16
        "Function_17_5B91",        # 11, 17
        "Function_18_5E85",        # 12, 18
        "Function_19_5FA8",        # 13, 19
        "Function_20_6144",        # 14, 20
        "Function_21_63AC",        # 15, 21
        "Function_22_6659",        # 16, 22
        "Function_23_6830",        # 17, 23
        "Function_24_6FAF",        # 18, 24
        "Function_25_706B",        # 19, 25
        "Function_26_721D",        # 1A, 26
        "Function_27_74DF",        # 1B, 27
        "Function_28_7A3A",        # 1C, 28
        "Function_29_8382",        # 1D, 29
        "Function_30_8E14",        # 1E, 30
        "Function_31_913E",        # 1F, 31
    ))


    def Function_0_3F4(): pass

    label("Function_0_3F4")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_42C"),
        (1, "loc_438"),
        (2, "loc_444"),
        (3, "loc_450"),
        (4, "loc_45C"),
        (5, "loc_468"),
        (6, "loc_474"),
        (SWITCH_DEFAULT, "loc_480"),
    )


    label("loc_42C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_438")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_444")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_450")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_45C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_468")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_474")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_480")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_48C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_4A3")

    Return()

    # Function_0_3F4 end

    def Function_1_4A4(): pass

    label("Function_1_4A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_540")
    OP_95(0xFE, 16079, 0, 3700, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(100)
    OP_95(0xFE, 9170, 0, -4250, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -9020, 0, -3100, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(100)
    OP_95(0xFE, 8720, 0, 4400, 2000, 0x0)
    Jump("Function_1_4A4")

    label("loc_540")

    Return()

    # Function_1_4A4 end

    def Function_2_541(): pass

    label("Function_2_541")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F1")
    OP_95(0xFE, 16079, 0, 3700, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(100)
    OP_95(0xFE, 9170, 0, -4250, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -9020, 0, -3100, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(100)
    OP_95(0xFE, -4560, 0, 4400, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    Jump("Function_2_541")

    label("loc_5F1")

    Return()

    # Function_2_541 end

    def Function_3_5F2(): pass

    label("Function_3_5F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_67A")
    OP_95(0xFE, 16079, 0, 3700, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(100)
    OP_95(0xFE, 9170, 0, -4250, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 8720, 0, 4400, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    Jump("Function_3_5F2")

    label("loc_67A")

    Return()

    # Function_3_5F2 end

    def Function_4_67B(): pass

    label("Function_4_67B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_717")
    OP_95(0xFE, 16079, 0, 3700, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xE1, 0x190)
    Sleep(100)
    OP_95(0xFE, 9170, 0, -4250, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -9020, 0, -3100, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(100)
    OP_95(0xFE, 8720, 0, 4400, 2000, 0x0)
    Jump("Function_4_67B")

    label("loc_717")

    Return()

    # Function_4_67B end

    def Function_5_718(): pass

    label("Function_5_718")

    SetChrChipByIndex(0xB, 0x0)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xF, 0x8)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_78C")
    SetChrChipByIndex(0x8, 0x10)
    SetChrChipByIndex(0x9, 0x10)
    BeginChrThread(0x9, 0, 0, 2)
    SetChrChipByIndex(0xB, 0x11)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x12)
    ClearChrBattleFlags(0xF, 0x4)
    SetChrPos(0xF, -3840, 0, -130, 270)
    BeginChrThread(0xF, 0, 0, 0)
    Jump("loc_A9B")

    label("loc_78C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_889")
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0x14)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0x15)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7DA")
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x17, 0x10)

    label("loc_7DA")

    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x9, -3730, 0, -170, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0x9, 0x10)
    SetChrChipByIndex(0xB, 0x2)
    ClearChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, 14120, 0, 3660, 180)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 6110, 0, 5040, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -970, 0, 2740, 180)
    SetChrChipByIndex(0x12, 0xF)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -94700, 0, 4190, 90)
    SetChrChipByIndex(0x10, 0xA)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    Jump("loc_A9B")

    label("loc_889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_918")
    BeginChrThread(0x9, 0, 0, 3)
    SetChrChipByIndex(0xD, 0x4)
    SetChrPos(0xD, -1100, 0, 3450, 90)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrChipByIndex(0x12, 0xE)
    SetChrPos(0x12, 80, 0, 3450, 270)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x40)
    BeginChrThread(0x12, 0, 0, 0)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -94670, 150, 2320, 90)
    SetChrChipByIndex(0x11, 0xC)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_A9B")

    label("loc_918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_95D")
    BeginChrThread(0x9, 0, 0, 3)
    SetChrFlags(0xB, 0x10)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -2190, 400, 9210, 152)
    Jump("loc_A9B")

    label("loc_95D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_98C")
    BeginChrThread(0x9, 0, 0, 3)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x12, 0xF)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_A9B")

    label("loc_98C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A0F")
    SetChrPos(0x9, -3730, 0, -170, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0x9, 0x10)
    SetChrChipByIndex(0xD, 0x4)
    SetChrPos(0xD, -1670, 0, 2760, 225)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    BeginChrThread(0xD, 0, 0, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A0A")
    ClearChrFlags(0x13, 0x80)

    label("loc_A0A")

    Jump("loc_A9B")

    label("loc_A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A54")
    BeginChrThread(0x9, 0, 0, 3)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -92130, 150, 2320, 270)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_A9B")

    label("loc_A54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A9B")
    BeginChrThread(0x9, 0, 0, 3)
    TurnDirection(0xA, 0xB, 0)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0x15)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)

    label("loc_A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_AAA")
    ClearScenarioFlags(0x22, 0)
    Event(0, 30)

    label("loc_AAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC9")
    Event(0, 29)

    label("loc_AC9")

    Return()

    # Function_5_718 end

    def Function_6_ACA(): pass

    label("Function_6_ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE6")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AF8")

    label("loc_AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_AF8")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AF8")

    SetMapObjFrame(0x8, "chukin", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B42")
    ClearMapObjFlags(0x8, 0x4)
    OP_78(0x8, 0x18)
    SetChrPos(0x18, -760, 0, -150, 0)
    OP_D5(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    Jump("loc_C9D")

    label("loc_B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B7E")
    ClearMapObjFlags(0x7, 0x4)
    OP_78(0x7, 0x18)
    SetChrPos(0x18, -760, 0, -150, 0)
    OP_D5(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    Jump("loc_C9D")

    label("loc_B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BC6")
    ClearMapObjFlags(0x8, 0x4)
    OP_78(0x8, 0x18)
    SetChrPos(0x18, -760, 0, -150, 0)
    OP_D5(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    Jump("loc_C9D")

    label("loc_BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C02")
    ClearMapObjFlags(0x7, 0x4)
    OP_78(0x7, 0x18)
    SetChrPos(0x18, -760, 0, -150, 0)
    OP_D5(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    Jump("loc_C9D")

    label("loc_C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C3E")
    ClearMapObjFlags(0x8, 0x4)
    OP_78(0x8, 0x18)
    SetChrPos(0x18, -760, 100, -150, 0)
    OP_D5(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    Jump("loc_C9D")

    label("loc_C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C7A")
    ClearMapObjFlags(0x7, 0x4)
    OP_78(0x7, 0x18)
    SetChrPos(0x18, -760, 0, -150, 0)
    OP_D5(0x18, 0x0, 0x15F90, 0x0, 0x0)
    Jump("loc_C9D")

    label("loc_C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C8E")
    ClearMapObjFlags(0x8, 0x4)
    Jump("loc_C9D")

    label("loc_C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C9D")
    ClearMapObjFlags(0x7, 0x4)

    label("loc_C9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CBF")
    SetMapObjFlags(0x5, 0x4)

    label("loc_CBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE5")
    SetMapObjFlags(0x5, 0x4)

    label("loc_CE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D0B")
    SetMapObjFlags(0x5, 0x4)

    label("loc_D0B")

    OP_66(0x3, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D39")
    SetMapObjFlags(0xA, 0x4)
    OP_65(0x3, 0x1)

    label("loc_D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D4C")
    SetMapObjFlags(0xA, 0x4)
    OP_65(0x3, 0x1)

    label("loc_D4C")

    OP_70(0x5, 0x8C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D76")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_D76")

    Return()

    # Function_6_ACA end

    def Function_7_D77(): pass

    label("Function_7_D77")

    Call(0, 8)
    Return()

    # Function_7_D77 end

    def Function_8_D7B(): pass

    label("Function_8_D7B")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_FC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE9")

    NpcTalk(
        0x8,
        "Soldier Connors",
        (
            "The bridge connecting the national\x01",
            "border is still out, but security\x01",
            "towards the Imperial army is strict.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Connors",
        (
            "If they invade, they'll\x01",
            "probably repair the\x01",
            "fallen bridge right away.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Connors",
        (
            "The Empire is in a civil war, for\x01",
            "good or bad... We've got to adjust\x01",
            "our positions while we can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_FC0")

    label("loc_EE9")


    NpcTalk(
        0x8,
        "Soldier Connors",
        (
            "If the Empire invades,\x01",
            "they'd probably repair the\x01",
            "fallen bridge right away.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Connors",
        (
            "The Empire is in a civil war, for\x01",
            "good or bad... We've got to adjust\x01",
            "our positions while we can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FC0")

    Jump("loc_1ADF")

    label("loc_FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1097")

    ChrTalk(
        0x8,
        (
            "In light of recent tensions, it\x01",
            "seems there's a considerable number\x01",
            "of foreigners leaving Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even without that, dangerous\x01",
            "incidents are continuing...\x01",
            "I guess I can't blame them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ADF")

    label("loc_1097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_124F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A3")

    ChrTalk(
        0x8,
        (
            "Yesterday, the unit led\x01",
            "by 2nd Lt. Mireille\x01",
            "spotted a giant monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She'll patrol the state with\x01",
            "a company for a while to look\x01",
            "for the monster that escaped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh man... With these\x01",
            "continued tensions, we're\x01",
            "only getting busier.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_124A")

    label("loc_11A3")


    ChrTalk(
        0x8,
        (
            "She'll patrol the state with\x01",
            "a company for a while to look\x01",
            "for the monster that escaped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh man... With these\x01",
            "continued tensions, we're\x01",
            "only getting busier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_124A")

    Jump("loc_1ADF")

    label("loc_124F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1305")

    ChrTalk(
        0x8,
        (
            "The Imperial merchant who just\x01",
            "passed through said many things\x01",
            "about Crossbell's independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems this topic is\x01",
            "provoking criticism even\x01",
            "in the Empire.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ADF")

    label("loc_1305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_14F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_143C")

    ChrTalk(
        0x8,
        (
            "Recently, it seems exercises\x01",
            "are being held for show\x01",
            "inside the Imperial fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's to put pressure on we CGF...\x01",
            "No, in this case it's probably to\x01",
            "put pressure on Mayor Dieter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though it's cute compared to\x01",
            "the tensions before the "Non-\x01",
            "Aggression Pact" was signed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_14EB")

    label("loc_143C")


    ChrTalk(
        0x8,
        (
            "Recently, it exercises are\x01",
            "being held for show inside\x01",
            "the Imperial fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though it's cute compared to\x01",
            "the tensions before the "Non-\x01",
            "Aggression Pact" was signed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14EB")

    Jump("loc_1ADF")

    label("loc_14F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1671")

    ChrTalk(
        0x8,
        (
            "Because we received intel\x01",
            "about terrorists, we were\x01",
            "ordered to do strict checks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With the security today, it should\x01",
            "be almost impossible to infiltrate\x01",
            "from an overland route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, for the air route, security\x01",
            "measures are being taken at a\x01",
            "special facility nearby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even in the CGF where we\x01",
            "don't have airships, we\x01",
            "must do all that we can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_16E4")

    label("loc_1671")


    ChrTalk(
        0x8,
        (
            "Due to the state\x01",
            "regulations, the CGF\x01",
            "can't possess airships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ideally, you'd want them\x01",
            "for air security.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E4")

    Jump("loc_1ADF")

    label("loc_16E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1990")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18BC")

    ChrTalk(
        0x8,
        (
            "Chancellor Osborne, who's attending the\x01",
            "trade conference, is commonly known as\x01",
            "the Blood and Iron Chancellor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The origin of that name seems to come from his\x01",
            "creed that "A nation's stability must come from\x01",
            "blood and iron, namely military might and weapons."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Under those words, he\x01",
            "militarily annexed many\x01",
            "states into the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's no doubt that he's the\x01",
            "single character Crossbell should\x01",
            "be the most cautious about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_198B")

    label("loc_18BC")


    ChrTalk(
        0x8,
        (
            "The Empire militarily annexed many\x01",
            "states. In many of them, the Blood\x01",
            "and Iron Chancellor was involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's no doubt that he's the\x01",
            "single character Crossbell should\x01",
            "be the most cautious about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_198B")

    Jump("loc_1ADF")

    label("loc_1990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1ADF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A6C")

    ChrTalk(
        0x8,
        (
            "If you pass through that iron\x01",
            "fence, it's just a short distance\x01",
            "to the Empire's Garrelia Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you're going there, be\x01",
            "warned. The Imperial immigration\x01",
            "checks are quite strict.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1ADF")

    label("loc_1A6C")


    ChrTalk(
        0x8,
        (
            "The Imperial\x01",
            "immigrations checks are\x01",
            "quite strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you intend to go to\x01",
            "Garrelia Fortress, be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ADF")

    TalkEnd(0x8)
    Return()

    # Function_8_D7B end

    def Function_9_1AE3(): pass

    label("Function_9_1AE3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C4E")

    NpcTalk(
        0x9,
        "Soldier Sig",
        (
            "The independence declaration of invalidity,\x01",
            "the Secretary of Defense going missing... And\x01",
            "I also heard the President has been arrested.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Sig",
        (
            "Is it all right for us to\x01",
            "keep working as the State\x01",
            "Guard from now on...?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Sig",
        (
            "...No matter what I think\x01",
            "about the situation, I\x01",
            "can't clear my doubts.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D02")

    label("loc_1C4E")


    NpcTalk(
        0x9,
        "Soldier Sig",
        (
            "Is it all right for us to\x01",
            "keep working as the State\x01",
            "Guard from now on...?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Sig",
        (
            "...No matter what I think\x01",
            "about the situation, I\x01",
            "can't clear my doubts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D02")

    Jump("loc_273D")

    label("loc_1D07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1DBB")

    ChrTalk(
        0xFE,
        (
            "In the future, no matter\x01",
            "what tricks the Empire\x01",
            "pulls, we won't ever yield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I won't let my comrades'\x01",
            "deaths be in vain. ...As if\x01",
            "I'd ever actually do that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_273D")

    label("loc_1DBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1E94")

    ChrTalk(
        0xFE,
        (
            "*sigh*... It seems the\x01",
            "fatigue of last night's\x01",
            "repair work is still with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In a tense situation like this, I don't\x01",
            "know if something will happen. Maybe I\x01",
            "should take a nap while I still can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_273D")

    label("loc_1E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2064")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB8")

    ChrTalk(
        0xFE,
        (
            "We were going to take on\x01",
            "the investigation for those\x01",
            "Cryptid things, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The continued state of tension\x01",
            "due to the independence\x01",
            "proposal can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I'll leave it to you\x01",
            "then, Randy and friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah, you do your best\x01",
            "too, 'k?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_205F")

    label("loc_1FB8")


    ChrTalk(
        0xFE,
        (
            "We were going to take on\x01",
            "the investigation for those\x01",
            "Cryptid things, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The continued state of tension\x01",
            "due to the independence\x01",
            "proposal can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_205F")

    Jump("loc_273D")

    label("loc_2064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_21F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2149")

    ChrTalk(
        0xFE,
        (
            "The other day, Warrant\x01",
            "Officer Mireille was\x01",
            "promoted to 2nd Lt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the other countries'\x01",
            "armies, 2nd Lt. is a\x01",
            "rank equal to Ensign.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm expecting great\x01",
            "things from her in the\x01",
            "future, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_21F2")

    label("loc_2149")


    ChrTalk(
        0xFE,
        (
            "Thinking about her merit, this\x01",
            "promotion came too late, but... Well,\x01",
            "it's something to be happy about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm expecting great\x01",
            "things from her in the\x01",
            "future, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F2")

    Jump("loc_273D")

    label("loc_21F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2295")

    ChrTalk(
        0xFE,
        (
            "No response from the\x01",
            "detector. ...It seems there\x01",
            "are no dangerous objects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll check under\x01",
            "the car frame too just\x01",
            "in case...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_273D")

    label("loc_2295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_24B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_240A")

    ChrTalk(
        0xFE,
        (
            "It indeed makes sense that security\x01",
            "during the trade conference is under\x01",
            "the direction of Commander Sonya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By assigning the minimum required\x01",
            "personnel with pertinent abilities,\x01",
            "we're smoothly covering border security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a great difference compared to the\x01",
            "former commander. As expected, that's\x01",
            "what a leader of others should be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_24AC")

    label("loc_240A")


    ChrTalk(
        0xFE,
        (
            "I thought I could be the\x01",
            "commander one day by racking\x01",
            "up achievements, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I realized that's totally\x01",
            "impossible as long as\x01",
            "Commander Sonya is alive.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24AC")

    Jump("loc_273D")

    label("loc_24B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_273D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2626")

    ChrTalk(
        0xFE,
        (
            "The former commander had ties\x01",
            "to Joachim through Hartmann and\x01",
            "was used in the cult incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After his dishonorable discharge, it\x01",
            "was a matter of course that Vice\x01",
            "Commander Sonya would become commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, the CGF organization is probably\x01",
            "going to be managed much more correctly. It's\x01",
            "really something to be happy about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_273D")

    label("loc_2626")


    ChrTalk(
        0xFE,
        (
            "Because of the former commander's incompetence,\x01",
            "all the responsibilities have fallen on the\x01",
            "shoulders of Warrant Officer Mireille until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, the CGF organization is probably\x01",
            "going to be managed much more correctly. It's\x01",
            "really something to be happy about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_273D")

    TalkEnd(0xFE)
    Return()

    # Function_9_1AE3 end

    def Function_10_2741(): pass

    label("Function_10_2741")

    Call(0, 11)
    Return()

    # Function_10_2741 end

    def Function_11_2745(): pass

    label("Function_11_2745")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_276E")
    Call(0, 28)
    Return()

    label("loc_276E")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_277B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35EF")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27CD")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_27CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27ED")
    OP_AF(0x73)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_35EA")

    label("loc_27ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2801")
    Jump("loc_35EA")

    label("loc_2801")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35EA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_28C8")

    ChrTalk(
        0xA,
        (
            "The "Satiating Hot Pot" I\x01",
            "serve to the Bellguard Gate\x01",
            "CGF members is delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We often do hot pot\x01",
            "parties, but they really\x01",
            "turn into meat contests.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EA")

    label("loc_28C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29A5")

    ChrTalk(
        0xA,
        (
            "Everyone is uneasy,\x01",
            "but... I'm sure it'll be\x01",
            "all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "After all, Cless said\x01",
            "he'll absolutely protect\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That's why I've got to do\x01",
            "everything I can to raise\x01",
            "everyone's spirits.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2A54")

    label("loc_29A5")


    ChrTalk(
        0xA,
        (
            "It seems that everyone is uneasy due\x01",
            "to that ridiculous huge tree and the\x01",
            "rumor of the President's arrest...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I have to raise\x01",
            "everyone's spirits by\x01",
            "doing what I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A54")

    Jump("loc_35EA")

    label("loc_2A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2C2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B79")

    ChrTalk(
        0xA,
        (
            "This state of tension with the Empire...\x01",
            "It really makes you remember the time\x01",
            "before the Non-Aggression Pact was signed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When those Imperial Railway\x01",
            "Cannons were pointed at us,\x01",
            "I was really scared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hope nothing like that\x01",
            "ever happens again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2C26")

    label("loc_2B79")


    ChrTalk(
        0xA,
        (
            "Before the Non-Aggression Pact was signing,\x01",
            "the Empire sometimes deployed those Railway\x01",
            "Cannons for during exercises.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hope nothing like that\x01",
            "ever happens again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C26")

    Jump("loc_35EA")

    label("loc_2C2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D58")

    ChrTalk(
        0xA,
        (
            "Unfortunately, it's raining\x01",
            "today. It'll be hard for our\x01",
            "members guarding outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In such a day, a dish\x01",
            "that warms up the body\x01",
            "is nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I guess I'll put to the extraordinarily\x01",
            "spicy stew I gave Cless yesterday to good\x01",
            "use and prepare a hot pot or something.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2E1A")

    label("loc_2D58")


    ChrTalk(
        0xA,
        (
            "On rainy days like\x01",
            "these, a dish that warms\x01",
            "the body is nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I guess I'll put to the extraordinarily\x01",
            "spicy stew I gave Cless yesterday to good\x01",
            "use and prepare a hot pot or something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E1A")

    Jump("loc_35EA")

    label("loc_2E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2FB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F20")

    ChrTalk(
        0xA,
        (
            "Because Cless looked spent recently,\x01",
            "I made him an extraordinarily spicy\x01",
            "stew to snap him out of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At first, I thought I\x01",
            "made it a little too\x01",
            "spicy, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He's actually eating it,\x01",
            "so... Haha, it seems it\x01",
            "was ok.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2FAE")

    label("loc_2F20")


    ChrTalk(
        0xA,
        (
            "Haha, it makes me glad\x01",
            "he's eating it so\x01",
            "happily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Since we're going out, maybe\x01",
            "I'll make special dishes for\x01",
            "him every now and then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FAE")

    Jump("loc_35EA")

    label("loc_2FB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_311A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_307F")

    ChrTalk(
        0xA,
        (
            "Cless looks spent\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Alright, I think I'll\x01",
            "prepare him a dish or\x01",
            "something to fire him up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He's still my "trial\x01",
            "boyfriend", so I've got\x01",
            "to at least do this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3115")

    label("loc_307F")


    ChrTalk(
        0xA,
        (
            "Well then, I guess I'll\x01",
            "prepare Cless a dish or\x01",
            "something to fire him up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He's still my "trial\x01",
            "boyfriend", so I've got\x01",
            "to at least do this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3115")

    Jump("loc_35EA")

    label("loc_311A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_31CD")

    ChrTalk(
        0xA,
        (
            "They say that there's a\x01",
            "possibility terrorists\x01",
            "will infiltrate Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Gate security has been\x01",
            "increased, but I wonder if the\x01",
            "members will be all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EA")

    label("loc_31CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3387")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F1")

    ChrTalk(
        0xA,
        (
            "It's been quite some time\x01",
            "since I started going out\x01",
            "with Cless on a trial basis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But even if we're "going out", we're\x01",
            "not doing anything different...\x01",
            "Could that be all there is to it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To men, maybe the fact\x01",
            "of "going out" itself is\x01",
            "what's important.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3382")

    label("loc_32F1")


    ChrTalk(
        0xA,
        (
            "I don't have much\x01",
            "experience either so I\x01",
            "don't really get it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To men, maybe the fact\x01",
            "of "going out" itself is\x01",
            "what's important.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3382")

    Jump("loc_35EA")

    label("loc_3387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_35EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3554")
    TurnDirection(0xA, 0x104, 0)

    ChrTalk(
        0xA,
        (
            "Oh, welco... Wait, if it\x01",
            "isn't Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Did you already finish\x01",
            "rehabilitation training?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHaha, that's right,\x01",
            "but... I wanted have a\x01",
            "look at a cutie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ahaha, you're always\x01",
            "such a jokester.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Also, if you seduced me\x01",
            "now, I think Cless would\x01",
            "get mad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FRandy, that CGF member\x01",
            "there is eyeing you\x01",
            "pretty intensely...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F...I-It's true that\x01",
            "could be troublesome.\x01",
            "I'll keep that in mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_35EA")

    label("loc_3554")


    ChrTalk(
        0xA,
        (
            "Haha. Well, that\x01",
            "aside... Since you're\x01",
            "here, eat something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It would make me happy if\x01",
            "you ate tons like during the\x01",
            "rehabilitation training.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35EA")

    Jump("loc_277B")

    label("loc_35EF")

    TalkEnd(0xA)
    Return()

    # Function_11_2745 end

    def Function_12_35F3(): pass

    label("Function_12_35F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_361C")
    Call(0, 27)
    Return()

    label("loc_361C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_37CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_372B")

    NpcTalk(
        0xB,
        "Soldier Cless",
        (
            "Honestly, I don't know\x01",
            "what to do either.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Cless",
        (
            "However, I must protect\x01",
            "what's important to me\x01",
            "with my own hands.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Cless",
        (
            "A-Alright... For now, I'll\x01",
            "eat! I'll eat and eat and\x01",
            "build up my strength!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_37C6")

    label("loc_372B")


    NpcTalk(
        0xB,
        "Soldier Cless",
        (
            "You can't fight on an\x01",
            "empty stomach, yes.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Cless",
        (
            "In order to protect what's\x01",
            "important to me... I'll\x01",
            "eat! I'll eat and eat!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37C6")

    Jump("loc_432F")

    label("loc_37CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_399E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E9")

    ChrTalk(
        0xFE,
        (
            "In the fight in the Mainz\x01",
            "region the other day, many of\x01",
            "my comrades were taken out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we had had powerful\x01",
            "tanks, we'd probably have\x01",
            "suffered far less damage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To protect Stella and those\x01",
            "important to me, I always\x01",
            "knew we needed independence.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3999")

    label("loc_38E9")


    ChrTalk(
        0xFE,
        (
            "If we had had powerful tanks,\x01",
            "the damage in Mainz could've\x01",
            "been kept to a minimum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To protect Stella and those\x01",
            "important to me, I always\x01",
            "knew we needed independence.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3999")

    Jump("loc_432F")

    label("loc_399E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3B3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A90")

    ChrTalk(
        0xFE,
        (
            "I'm feeling good for some\x01",
            "reason after eating Stella's\x01",
            "extremely spicy stew yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe... Maybe this is\x01",
            "what they call the\x01",
            ""power of love".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Although I've had\x01",
            "enough of that spiciness\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3B3A")

    label("loc_3A90")


    ChrTalk(
        0xFE,
        (
            "I'm feeling good for some\x01",
            "reason after eating Stella's\x01",
            "extremely spicy stew yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must thank her.\x01",
            "...Although I've had enough\x01",
            "of that spiciness already.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B3A")

    Jump("loc_432F")

    label("loc_3B3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3C78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C0D")

    ChrTalk(
        0xFE,
        (
            "*huff huff*... Eek,\x01",
            "i-it's spicy, too\x01",
            "spicy...!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "N-No, my babe made it specially\x01",
            "for me. If I'm a man, I'll make\x01",
            "short work of it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uooooh, *eating\x01",
            "greedily*...!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3C73")

    label("loc_3C0D")


    ChrTalk(
        0xFE,
        (
            "*huff huff*... I-It's\x01",
            "really spicy...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "B-But, I'll finish all\x01",
            "of it! *eating\x01",
            "greedily*...!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C73")

    Jump("loc_432F")

    label("loc_3C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D21")

    ChrTalk(
        0xFE,
        (
            "*sigh*, I can't help but\x01",
            "feel tired due to the\x01",
            "recent state of tension.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...No, no, Stella's\x01",
            "watching me, so I've got\x01",
            "to look sharp.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3D74")

    label("loc_3D21")


    ChrTalk(
        0xFE,
        (
            "I've been tired lately,\x01",
            "but... Stella is watching,\x01",
            "so I've got to look sharp.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D74")

    Jump("loc_432F")

    label("loc_3D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3E28")

    ChrTalk(
        0xFE,
        (
            "I'll guard smartly today\x01",
            "and show Stella my good\x01",
            "points.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't care if you're a terrorist\x01",
            "or whatever, just try coming at me\x01",
            "from wherever you want.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_432F")

    label("loc_3E28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3F4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F05")

    ChrTalk(
        0xFE,
        (
            "I've finally started going\x01",
            "out with Stella, but I can't\x01",
            "even invite her on a date.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lately I've been busy with trade\x01",
            "conference stuff, and my abilities\x01",
            "aren't all that to begin with...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3F49")

    label("loc_3F05")


    ChrTalk(
        0xFE,
        (
            "Damn it... Somehow I'd\x01",
            "like to make progress\x01",
            "with my Stella...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F49")

    Jump("loc_432F")

    label("loc_3F4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_432F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_407B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_403A")

    ChrTalk(
        0xB,
        (
            "Tch... It wouldn't hurt\x01",
            "you if you listened to\x01",
            "me a little, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If it's about Stella, I\x01",
            "could talk for hours!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FLater then, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I told you to listen!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4076")

    label("loc_403A")


    ChrTalk(
        0xB,
        (
            "Tch... If it's about\x01",
            "Stella, I could talk for\x01",
            "hours...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4076")

    Jump("loc_432F")

    label("loc_407B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_40FC")

    ChrTalk(
        0xFE,
        (
            "Randyyyy.... What were\x01",
            "you doing to my\x01",
            "sweetheart...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FNow, now, calm down. I\x01",
            "didn't do anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_432F")

    label("loc_40FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42A9")

    ChrTalk(
        0xFE,
        (
            "Hehe, Stella... My\x01",
            "sweet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F("M-My sweet", he\x01",
            "says...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FOh, by the way Randy... I heard\x01",
            "some time ago that you're going\x01",
            "out with Stella as a "trial", huh?\x02\x03",
            "#00309FHaha, making progress?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...M-More or less. Well,\x01",
            "we're lovey dovey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Every day I eat here and\x01",
            "gaze at my sweet Stella...\x01",
            "Every day is happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(...In other words,\x01",
            "there hasn't been any\x01",
            "progress yet...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_432F")

    label("loc_42A9")


    ChrTalk(
        0xFE,
        (
            "Stella and I are just\x01",
            "getting started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't cut in and seduce\x01",
            "her, Randy. ...I'm\x01",
            "begging you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F(He's hopeless.)\x02",
    )

    CloseMessageWindow()

    label("loc_432F")

    TalkEnd(0xFE)
    Return()

    # Function_12_35F3 end

    def Function_13_4333(): pass

    label("Function_13_4333")

    Call(0, 14)
    Return()

    # Function_13_4333 end

    def Function_14_4337(): pass

    label("Function_14_4337")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4344")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54F9")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Rest\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4396")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4396")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43B6")
    OP_AF(0x74)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_54F4")

    label("loc_43B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43CA")
    Jump("loc_54F4")

    label("loc_43CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54F4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_456C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44D2")

    ChrTalk(
        0xC,
        (
            "In times like these, the\x01",
            "mental strain is\x01",
            "especially bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you're taking a\x01",
            "break, take time to rest\x01",
            "and calm your mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...That said, I'm uneasy\x01",
            "too. I wonder if peaceful\x01",
            "times will ever return.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4567")

    label("loc_44D2")


    ChrTalk(
        0xC,
        (
            "If you're taking a\x01",
            "break, take time to rest\x01",
            "and calm your mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...That said, I'm uneasy\x01",
            "too! I wonder if peaceful\x01",
            "times will ever return.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4567")

    Jump("loc_54F4")

    label("loc_456C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4793")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46BF")

    ChrTalk(
        0xC,
        (
            "It seems Red Constellation has an\x01",
            "airship. They did as they please in\x01",
            "Crossbell and then retreated somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Furthermore, it seems that\x01",
            "the CGF's anti-aircraft\x01",
            "radar didn't pick it up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Honestly, if you have the funds,\x01",
            "there's no tech you can't get. I wonder\x01",
            "who the hell those people are...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_478E")

    label("loc_46BF")


    ChrTalk(
        0xC,
        (
            "They say Red Constellation's\x01",
            "airship wasn't picked up on\x01",
            "the CGF's anti-aircraft radar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Honestly, if you have the funds,\x01",
            "there's no tech you can't get. I wonder\x01",
            "who the hell those people are...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_478E")

    Jump("loc_54F4")

    label("loc_4793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_49FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_490D")

    ChrTalk(
        0xC,
        (
            "I heard about the accident yesterday.\x01",
            "I heard the train derailed after\x01",
            "being struck hard by a giant monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That train was manufactured by Reinford Corporation,\x01",
            "famous in the Empire for its weapons development. It\x01",
            "should've at least had sturdy armor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I didn't see it myself, but I\x01",
            "feel I understand how\x01",
            "frightening that monster was.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_49FA")

    label("loc_490D")


    ChrTalk(
        0xC,
        (
            "That train was manufactured by Reinford Corporation,\x01",
            "famous in the Empire for its weapons development,\x01",
            "and yet it derailed after being struck...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I didn't see it myself, but I\x01",
            "feel I understand how\x01",
            "frightening that monster was.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49FA")

    Jump("loc_54F4")

    label("loc_49FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4CB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD8")

    ChrTalk(
        0xC,
        (
            "With the mechanization of each country's\x01",
            "army, great importance has been placed\x01",
            "on air tactics in recent years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For instance, in the Hundred Days War 12 years\x01",
            "ago, Liberl was invaded due to the Empire's\x01",
            "overwhelming military strength, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In the final stage of the conflict,\x01",
            "Liberl turned the situation around\x01",
            "with its newly developed airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The CGF isn't allowed to\x01",
            "possess airships is because\x01",
            "of situations like those.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4CAC")

    label("loc_4BD8")


    ChrTalk(
        0xC,
        (
            "With the recent mechanization of\x01",
            "national armies, great importance\x01",
            "has been placed on air tactics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "When we're independent and the CGF\x01",
            "becomes an army, I want to deploy\x01",
            "airships of our own, first thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CAC")

    Jump("loc_54F4")

    label("loc_4CB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4EA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DCA")

    ChrTalk(
        0xC,
        (
            "If Crossbell becomes\x01",
            "independent, the CGF will become\x01",
            "a regular army too, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The members' equipment will be\x01",
            "upgraded to be more powerful than what\x01",
            "it is now. They'll even deploy tanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm. that's probably\x01",
            "appealing to military\x01",
            "otaku.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4EA3")

    label("loc_4DCA")


    ChrTalk(
        0xC,
        (
            "After Crossbell becomes independent and the\x01",
            "CGF becomes a regular army, the weapons\x01",
            "will be more satisfying than they are now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "They'll even deploy tanks...\x01",
            "Hmm. That's probably\x01",
            "appealing to military otaku..\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EA3")

    Jump("loc_54F4")

    label("loc_4EA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5072")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FC6")

    ChrTalk(
        0xC,
        (
            "Today is finally the day\x01",
            "of the conference at\x01",
            "Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Out of concern towards the\x01",
            "Empire and Republic, the CGF\x01",
            "can't openly guard, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's an important international\x01",
            "conference. I hope they'll protect\x01",
            "even if they're out of sight.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_506D")

    label("loc_4FC6")


    ChrTalk(
        0xC,
        (
            "Today is finally the day\x01",
            "of the conference at\x01",
            "Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's an important international\x01",
            "conference. I hope they'll protect\x01",
            "even if they're out of sight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_506D")

    Jump("loc_54F4")

    label("loc_5072")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_52EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5211")

    ChrTalk(
        0xC,
        (
            "It's been a little while since the new\x01",
            "armored cars were deployed, but...\x01",
            "Dear me, they really are great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "They've also got powerful missile pods and the\x01",
            "armor has been considerably reinforced. They're\x01",
            "the CGF's best weapons without a doubt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, it's unfair to compare them to other\x01",
            "countries' airships and tanks, but I believe\x01",
            "they combine simplicity with functionality.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_52E9")

    label("loc_5211")


    ChrTalk(
        0xC,
        (
            "The new armored cars are,\x01",
            "without a doubt, the best\x01",
            "of the CGF's weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, it's unfair to compare them to other\x01",
            "countries' airships and tanks, but I believe\x01",
            "they combine simplicity with functionality.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52E9")

    Jump("loc_54F4")

    label("loc_52EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_54F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5420")

    ChrTalk(
        0xC,
        (
            "I'm a military otaku...\x01",
            "What they shorten as\x01",
            "miliota.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I really love army-related things, so I\x01",
            "feel like my hobby grows in intensity\x01",
            "even just working here at the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, strictly speaking, the\x01",
            "Crossbell CGF isn't an army, but...\x01",
            "To me, it's quite fascinating.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_54F4")

    label("loc_5420")


    ChrTalk(
        0xC,
        (
            "I'm what they call a miliota. I feel\x01",
            "like my hobby grows in intensity\x01",
            "even just working here at the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, strictly speaking, the\x01",
            "Crossbell CGF isn't an army, but...\x01",
            "To me, it's quite fascinating.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54F4")

    Jump("loc_4344")

    label("loc_54F9")

    TalkEnd(0xC)
    Return()

    # Function_14_4337 end

    def Function_15_54FD(): pass

    label("Function_15_54FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_550E")
    Jump("loc_5874")

    label("loc_550E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5668")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55F2")

    ChrTalk(
        0xFE,
        (
            "I got caught up in\x01",
            "yesterday's derailment\x01",
            "accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, since I got out of it\x01",
            "with only light injuries, I got\x01",
            "my daughter to come pick me up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ooh, ow ow ow... It\x01",
            "still hurts a little.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5663")

    label("loc_55F2")


    ChrTalk(
        0xFE,
        (
            "Ooh, ow ow ow... It\x01",
            "still hurts a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should've stayed\x01",
            "at the hospital for a\x01",
            "while longer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5663")

    Jump("loc_5874")

    label("loc_5668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5727")

    ChrTalk(
        0xFE,
        (
            "Crossbell trying to be\x01",
            "independent... They\x01",
            "should know their place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From the point of view of an Imperial\x01",
            "citizen, it feels like being betrayed\x01",
            "by a trusted follower.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5874")

    label("loc_5727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5735")
    Jump("loc_5874")

    label("loc_5735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_57B8")

    ChrTalk(
        0xFE,
        (
            "Isn't the inspection\x01",
            "over already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't care if it's an\x01",
            "anti-terror countermeasure,\x01",
            "it's just a bother.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5874")

    label("loc_57B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_57C6")
    Jump("loc_5874")

    label("loc_57C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5874")

    ChrTalk(
        0xFE,
        (
            "There's no doubt that His Excellency the\x01",
            "Chancellor will come out of the trade conference\x01",
            "with a profitable agreement for the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe, how wonderful.\x02",
    )

    CloseMessageWindow()

    label("loc_5874")

    TalkEnd(0xFE)
    Return()

    # Function_15_54FD end

    def Function_16_5878(): pass

    label("Function_16_5878")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_593E")

    ChrTalk(
        0xFE,
        (
            "I've been perplexed ever since that\x01",
            "attack, but... I've decided to\x01",
            "return to my home in the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It would be unbearable if\x01",
            "I got involved in\x01",
            "something like that again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B8D")

    label("loc_593E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_594C")
    Jump("loc_5B8D")

    label("loc_594C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_595A")
    Jump("loc_5B8D")

    label("loc_595A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_59D2")

    ChrTalk(
        0xFE,
        (
            "State independence...\x01",
            "That's a mere fantasy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell should sweat\x01",
            "for the sake of the\x01",
            "Empire.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B8D")

    label("loc_59D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_59E0")
    Jump("loc_5B8D")

    label("loc_59E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5A91")

    ChrTalk(
        0xFE,
        (
            "Man oh man. It's not\x01",
            "really something to\x01",
            "hurry to come see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, because Orchis Tower became\x01",
            "a topic even in the Empire, I\x01",
            "wanted to see it for myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B8D")

    label("loc_5A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5B8D")

    ChrTalk(
        0xFE,
        (
            "They say Prince Olivert, the talk of the Empire,\x01",
            "is coming to Crossbell to attend the trade\x01",
            "conference as the Emperor's representative.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, he was probably appointed to\x01",
            "aid the Blood and Iron Chancellor\x01",
            "by His Majesty the Emperor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B8D")

    TalkEnd(0xFE)
    Return()

    # Function_16_5878 end

    def Function_17_5B91(): pass

    label("Function_17_5B91")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5D1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C81")

    ChrTalk(
        0xF,
        (
            "There's a civil war going\x01",
            "on in the Empire but even\x01",
            "so, I want to return home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "However, I'd never have dreamed\x01",
            "the bridge would completely\x01",
            "collapse like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "...I wonder what I\x01",
            "should do now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5D16")

    label("loc_5C81")


    ChrTalk(
        0xF,
        (
            "Father said he was going to look\x01",
            "at the fallen bridge from the\x01",
            "balcony and went upstairs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "...As I feared, we can't\x01",
            "return to the Empire.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D16")

    Jump("loc_5E81")

    label("loc_5D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5D29")
    Jump("loc_5E81")

    label("loc_5D29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5D37")
    Jump("loc_5E81")

    label("loc_5D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5DC4")

    ChrTalk(
        0xFE,
        (
            "The CGF people are all\x01",
            "tense for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want to stay here\x01",
            "for long, so I think I'll\x01",
            "go back home soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E81")

    label("loc_5DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5DD2")
    Jump("loc_5E81")

    label("loc_5DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5DE0")
    Jump("loc_5E81")

    label("loc_5DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5E78")

    ChrTalk(
        0xFE,
        (
            "I came to see Orchis Tower\x01",
            "or whatever it's called,\x01",
            "the rumored skyscraper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what kind of\x01",
            "building it is. I can't\x01",
            "wait.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E81")

    label("loc_5E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E81")

    label("loc_5E81")

    TalkEnd(0xFE)
    Return()

    # Function_17_5B91 end

    def Function_18_5E85(): pass

    label("Function_18_5E85")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5F29")

    ChrTalk(
        0xFE,
        (
            "I would've liked to have\x01",
            "a little more fun in\x01",
            "Crossbell, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This place has gotten\x01",
            "scary recently. I guess\x01",
            "there's no choice, then...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FA4")

    label("loc_5F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5F37")
    Jump("loc_5FA4")

    label("loc_5F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5F45")
    Jump("loc_5FA4")

    label("loc_5F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5F53")
    Jump("loc_5FA4")

    label("loc_5F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5F8D")

    ChrTalk(
        0xFE,
        (
            "*sigh*... I want to\x01",
            "hurry to the city.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FA4")

    label("loc_5F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5F9B")
    Jump("loc_5FA4")

    label("loc_5F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5FA4")

    label("loc_5FA4")

    TalkEnd(0xFE)
    Return()

    # Function_18_5E85 end

    def Function_19_5FA8(): pass

    label("Function_19_5FA8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5FB9")
    Jump("loc_6140")

    label("loc_5FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6057")

    ChrTalk(
        0xFE,
        (
            "Ah, to think it's\x01",
            "raining... Maybe I\x01",
            "should've used the railway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because that accident\x01",
            "just happened, I really\x01",
            "didn't want to use it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6140")

    label("loc_6057")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6065")
    Jump("loc_6140")

    label("loc_6065")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6073")
    Jump("loc_6140")

    label("loc_6073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6081")
    Jump("loc_6140")

    label("loc_6081")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6137")

    ChrTalk(
        0xFE,
        (
            "Due to traffic regulations,\x01",
            "the railway couldn't be\x01",
            "used this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that private train was\x01",
            "passing through, so I guess\x01",
            "it couldn't have been helped.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6140")

    label("loc_6137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6140")

    label("loc_6140")

    TalkEnd(0xFE)
    Return()

    # Function_19_5FA8 end

    def Function_20_6144(): pass

    label("Function_20_6144")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_62A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_621C")

    ChrTalk(
        0xFE,
        (
            "I'm just coming back\x01",
            "from my goods delivery,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, it seems\x01",
            "chaos is continuing at\x01",
            "Crossbell Station as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this situation, I\x01",
            "guess it can't be\x01",
            "helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_629D")

    label("loc_621C")


    ChrTalk(
        0xFE,
        (
            "As expected, it seems\x01",
            "chaos is continuing at\x01",
            "Crossbell Station as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this situation, I\x01",
            "guess it can't be\x01",
            "helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_629D")

    Jump("loc_63A8")

    label("loc_62A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_63A8")

    ChrTalk(
        0x13,
        (
            "A freight railway line\x01",
            "runs beneath the gate,\x01",
            "you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I just got back from\x01",
            "Crossbell Station after\x01",
            "inspecting the freight train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "...Do you want to go down there? I\x01",
            "don't think there's any problem with\x01",
            "that, just be careful of the train.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63A8")

    TalkEnd(0xFE)
    Return()

    # Function_20_6144 end

    def Function_21_63AC(): pass

    label("Function_21_63AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6622")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6545")

    ChrTalk(
        0x104,
        (
            "#00301FMireille... You look\x01",
            "quite busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#07901FYes, it seems there's movement at the Empire's\x01",
            "Garrelia Fortress.\x02\x03",
            "#07903FHonestly, it's an unprecedented state of\x01",
            "tension. ...It's almost the same as two years\x01",
            "ago, before the Non-Aggression Pact was signed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FThat much...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F...Stay safe, Mireille.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#07902F...Yes, I know. Leave\x01",
            "this place to me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_661D")

    label("loc_6545")


    ChrTalk(
        0x14,
        (
            "#07903FIt seems there's movement at the Empire's\x01",
            "Garrelia Fortress.\x02\x03",
            "#07901FHonestly, it's an unprecedented state of\x01",
            "tension. ...It's almost the same as two years\x01",
            "ago, before the Non-Aggression Pact was signed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_661D")

    Jump("loc_6655")

    label("loc_6622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6630")
    Jump("loc_6655")

    label("loc_6630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_663E")
    Jump("loc_6655")

    label("loc_663E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_664C")
    Jump("loc_6655")

    label("loc_664C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6655")

    label("loc_6655")

    TalkEnd(0xFE)
    Return()

    # Function_21_63AC end

    def Function_22_6659(): pass

    label("Function_22_6659")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6706")

    ChrTalk(
        0xFE,
        (
            "I would've never dreamed things\x01",
            "would worsen this much just one\x01",
            "week after the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to get out of\x01",
            "Crossbell with my\x01",
            "daughter quick.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_682C")

    label("loc_6706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6768")

    ChrTalk(
        0xFE,
        (
            "Father, are you all\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's go to the mess\x01",
            "hall to rest for a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_682C")

    label("loc_6768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6776")
    Jump("loc_682C")

    label("loc_6776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6807")

    ChrTalk(
        0xFE,
        (
            "They say the number of\x01",
            "mysterious monsters has\x01",
            "increased recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's alarming... I'll\x01",
            "return to the Empire\x01",
            "quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_682C")

    label("loc_6807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6815")
    Jump("loc_682C")

    label("loc_6815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6823")
    Jump("loc_682C")

    label("loc_6823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_682C")

    label("loc_682C")

    TalkEnd(0xFE)
    Return()

    # Function_22_6659 end

    def Function_23_6830(): pass

    label("Function_23_6830")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E06")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6A64")

    ChrTalk(
        0x15,
        (
            "#03600FYesterday's incident at\x01",
            "Armorica Village... I'm\x01",
            "really glad you solved it.\x02\x03",
            "#03603FIf you all hadn't been\x01",
            "there, I don't know what\x01",
            "would've happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FMinneth, an unscrupulous\x01",
            "trader... He was\x01",
            "formidable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FWell, he's wanted, so I\x01",
            "think it's only a matter of\x01",
            "time before he's arrested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe, I wonder. He had\x01",
            "tenacity written all\x01",
            "over his face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FIndeed, it seems we\x01",
            "can't relax until he's\x01",
            "caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03608FYou're right... I hope\x01",
            "there won't be any more\x01",
            "damage before then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DFE")

    label("loc_6A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_END)), "loc_6C92")

    ChrTalk(
        0x15,
        (
            "#03605FOh, everyone...\x02\x03",
            "#03600FRight, about the Minneth\x01",
            "incident at Armorica\x01",
            "Village...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...We're sorry to give up\x01",
            "on it while we were in the\x01",
            "middle of investigating.\x02\x03",
            "#00008FWe had another high\x01",
            "priority job and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03600FNo no, what are you saying. We had\x01",
            "Mr. Grimwood's cooperation too and\x01",
            "we managed to solve it somehow...\x02\x03",
            "#03604FThat's because the investigation\x01",
            "you all had done until then was\x01",
            "really useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI-I see... In that case,\x01",
            "I'm glad.\x02\x03",
            "#00003F(As I thought, we\x01",
            "should've done it\x01",
            "through the end.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DFE")

    label("loc_6C92")


    ChrTalk(
        0x15,
        (
            "#03600FI can't tell you the details since\x01",
            "it involves the prestige of the\x01",
            "Village Chief and the others, but...\x02\x03",
            "#03603FYesterday, there was a very bad\x01",
            "incident at Armorica Village.\x02\x03",
            "#03600FWithout Mr. Grimwood, that incident\x01",
            "probably wouldn't have been solved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(It seems it was a really bad\x01",
            "incident... I would've liked\x01",
            "to help them out somehow.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DFE")

    SetScenarioFlags(0x17C, 1)
    Jump("loc_6FAB")

    label("loc_6E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F10")

    ChrTalk(
        0x15,
        (
            "#03600FI drove via West Crossbell\x01",
            "Highway today...\x02\x03",
            "#03603FI get a little worried when I\x01",
            "think it's the day after a\x01",
            "derailment accident.\x02\x03",
            "#03600FThere's also a rumor going around\x01",
            "about the appearance of a giant\x01",
            "monster... I should be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_6FAB")

    label("loc_6F10")


    ChrTalk(
        0x15,
        (
            "#03600FI drove via West Crossbell\x01",
            "Highway today...\x02\x03",
            "There's also a rumor going around\x01",
            "about the appearance of a giant\x01",
            "monster... I should be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FAB")

    TalkEnd(0xFE)
    Return()

    # Function_23_6830 end

    def Function_24_6FAF(): pass

    label("Function_24_6FAF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FC4")
    Call(0, 25)
    Jump("loc_7067")

    label("loc_6FC4")


    ChrTalk(
        0xFE,
        (
            "This state of tension at\x01",
            "the border... I hope\x01",
            "nothing happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In any case, even the guild has\x01",
            "to check on the situation for\x01",
            "the sake of citizen safety.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7067")

    TalkEnd(0xFE)
    Return()

    # Function_24_6FAF end

    def Function_25_706B(): pass

    label("Function_25_706B")

    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x17, 0x10)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)

    ChrTalk(
        0x16,
        (
            "...I see, it really seems\x01",
            "like the national border\x01",
            "is in a sticky situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "It'd be nice to cooperate\x01",
            "with the Imperial guild\x01",
            "at a time like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "...Due to pressure from\x01",
            "the military, the Imperial\x01",
            "guild has declined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "They have many men of spirit, but...\x01",
            "With their organization like that,\x01",
            "we can't count on their help at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I see... Nothing can be\x01",
            "done about that then.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x16, 0x10)
    ClearChrFlags(0x17, 0x10)
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1, 4)
    Return()

    # Function_25_706B end

    def Function_26_721D(): pass

    label("Function_26_721D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7323")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_723B")
    Call(0, 25)
    Jump("loc_731E")

    label("loc_723B")


    ChrTalk(
        0xFE,
        (
            "If we cooperated with the Imperial guild,\x01",
            "we could've mitigated this state of\x01",
            "tension from a neutral position, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Due to military pressure, the\x01",
            "Imperial guild has declined. We\x01",
            "can't count on their help at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_731E")

    Jump("loc_74DB")

    label("loc_7323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7435")

    ChrTalk(
        0xFE,
        (
            "Today Scott and I are acting\x01",
            "separately. He was exterminating\x01",
            "nearby wanted monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With the start of the trade\x01",
            "conference, we bracers are going\x01",
            "to become quite busy ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before that, we have to\x01",
            "complete as many\x01",
            "requests as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_74DB")

    label("loc_7435")


    ChrTalk(
        0xFE,
        (
            "With the start of the trade\x01",
            "conference, we bracers are going\x01",
            "to become quite busy ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before that, we have to\x01",
            "complete as many\x01",
            "requests as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74DB")

    TalkEnd(0xFE)
    Return()

    # Function_26_721D end

    def Function_27_74DF(): pass

    label("Function_27_74DF")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0xB, -97000, 150, -3950, 90)
    SetChrSubChip(0xB, 0x2)
    OP_68(-95990, 750, -3740, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26060, 0)
    SetChrPos(0x101, -95150, 0, -3250, 270)
    SetChrPos(0x104, -95210, 0, -4670, 270)
    SetChrPos(0x102, -93870, 0, -4040, 270)
    SetChrPos(0x109, -93620, 0, -2840, 270)
    SetChrPos(0x105, -93480, 0, -5210, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    ChrTalk(
        0x104,
        "#12P#00309FYo, Cless.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PHuh... Randy!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PYour rehab training's\x01",
            "over. What are you doing\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FUhh, actually...\x02",
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
    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xB,
        (
            "#5PMedical questionnaire...\x01",
            "Oh! I completely forgot!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x1)

    ChrTalk(
        0xB,
        (
            "#5POne second, it should be\x01",
            "here somewhere...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xB,
        "#5PThis is it, right?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x32F, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#12P#00000FYeah, it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PSorry about that. Making\x01",
            "you come all the way out\x01",
            "here to get it, I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PI've been so happy\x01",
            "lately, I totally\x01",
            "forgot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FHappy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PYeah, Stella and I are\x01",
            "in love!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#6P#00304FAlright Lloyd, how about\x01",
            "we get going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FWell, we got what we\x01",
            "came for.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00012FR-Right. (This could go\x01",
            "on forever...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PH-Hey! You won't listen\x01",
            "to me!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FAhaha... Sorry.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x152, 6)
    OP_29(0x70, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A07")

    AnonymousTalk(
        0x101,
        (
            "#00003FWith this, we've\x01",
            "collected all the\x01",
            "questionnaires.\x02\x03",
            "#00000FLet's deliver them to\x01",
            "Professor Seiland\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x70, 0x1, 0x5)

    label("loc_7A07")

    SetChrPos(0xB, -97470, 150, -3950, 270)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -94400, 0, -3950, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_74DF end

    def Function_28_7A3A(): pass

    label("Function_28_7A3A")

    EventBegin(0x0)
    Fade(500)
    OP_68(-105030, 750, 2240, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26060, 0)
    SetChrPos(0x101, -103240, 0, 2040, 270)
    SetChrPos(0x104, -103250, 0, 3150, 270)
    SetChrPos(0x102, -103260, 0, 880, 270)
    SetChrPos(0x109, -103100, 0, -280, 315)
    SetChrPos(0x103, -102080, 0, 700, 270)
    SetChrPos(0x105, -101780, 0, -540, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "My, Randy and... everyone\x01",
            "from the Support Section,\x01",
            "I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FHi, Stella.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUhhm, today we came for\x01",
            "work...\x02",
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
        0xA,
        (
            "Ah, now that you mention\x01",
            "it... I heard about\x01",
            "that, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Alright then, I'll prepare the\x01",
            ""Satiating Hot Pot" I serve to\x01",
            "the Bellguard Gate CGF members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FWow, this unit has\x01",
            "something like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FThen, if you please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, I'll prepare a\x01",
            "portion for everyone.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others ate\x01",
            "the Satiating Hot Pot.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00100F*munch munch*... Yes, my\x01",
            "body feels nice and\x01",
            "warm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FYeah, the quantity of meat is amazing\x01",
            "and there are a lot of edible wild\x01",
            "plants too. It's highly nourishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FWell, CGF practice is hard, so if they\x01",
            "didn't get strength from something\x01",
            "like this, they wouldn't last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHehe, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We often do hot pot\x01",
            "parties, but they really\x01",
            "turn into meat contests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When Randy was here, he snatched\x01",
            "away other people's servings and\x01",
            "made a huge mess of things.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x103, 0x104, 500)

    ChrTalk(
        0x103,
        (
            "#00211F...What do you think you\x01",
            "were doing, Randy?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x104,
        (
            "#00309FHaha. Survival of the\x01",
            "fittest, you know?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x173, 2)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_8069")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8069")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_8086")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_8099")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_80AC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_80AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_80C9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_80C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_80DC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_80DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_80F9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_80F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_810C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_810C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_8129")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_813C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_813C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_8159")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8159")

    OP_29(0x80, 0x1, 0xB)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8264")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_825B")

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

    label("loc_825B")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_8264")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8352")
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

    label("loc_8352")

    OP_4C(0xA, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -103610, 0, 2100, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_7A3A end

    def Function_29_8382(): pass

    label("Function_29_8382")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xB, 0x80)
    SetMapObjFlags(0x5, 0x4)
    OP_68(20630, 1000, -340, 0)
    MoveCamera(315, 32, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(20760, 0)
    SetChrPos(0x101, 28060, 0, 0, 270)
    SetChrPos(0x102, 28260, 0, -1200, 270)
    SetChrPos(0x104, 28260, 0, 1200, 270)
    SetChrPos(0x109, 29460, 0, 0, 270)
    SetChrPos(0x103, 29260, 0, -1200, 270)
    SetChrPos(0x105, 29260, 0, 1200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x14, 5870, 0, 0, 90)
    OP_4B(0x14, 0xFF)
    SetChrFlags(0x14, 0x8000)

    def lambda_8460():
        OP_95(0x101, 21060, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8460)
    Sleep(30)

    def lambda_847D():
        OP_95(0x102, 21260, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_847D)
    Sleep(40)

    def lambda_849A():
        OP_95(0x104, 21260, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_849A)
    Sleep(800)

    def lambda_84B7():
        OP_95(0x109, 23560, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_84B7)
    Sleep(30)

    def lambda_84D4():
        OP_95(0x103, 23360, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_84D4)
    Sleep(10)

    def lambda_84F1():
        OP_95(0x105, 23360, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_84F1)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x101,
        (
            "#00001FWell then, that black\x01",
            "transport should be\x01",
            "here, but...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_END)), "loc_8620")

    ChrTalk(
        0x103,
        (
            "#00203FDidn't Frantz say it was\x01",
            "heading to the Republic?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FAh... Now that you\x01",
            "mention it, he did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FWe unconsciously came to\x01",
            "Bellgard Gate...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86A5")

    label("loc_8620")


    ChrTalk(
        0x103,
        (
            "#00205F...I don't see any\x01",
            "vehicle like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FUmm, maybe we could ask\x01",
            "some of the guardsmen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FWe could...\x02",
    )

    CloseMessageWindow()

    label("loc_86A5")


    def lambda_86AA():
        OP_95(0xFE, 17460, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_86AA)
    Sleep(2000)
    OP_68(20630, 1000, -340, 3000)
    MoveCamera(306, 19, 0, 3000)
    OP_6E(470, 3000)
    SetCameraDistance(20760, 3000)
    WaitChrThread(0x14, 1)
    OP_6F(0x79)

    ChrTalk(
        0x14,
        "#07900FOh... You guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FHi Mireille.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FGood morning, 2nd Lt.\x01",
            "Mireille!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#07902FGood morning.\x02\x03",
            "#07906F...*sigh*. What is your\x01",
            "business here today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FYou look tired.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#07901FYes... It's because of\x01",
            "the continuing tensions\x01",
            "with the Empire.\x02\x03",
            "#07903FI heard there's been a\x01",
            "disturbance at Tangram\x01",
            "Gate...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FWhat's happened at\x01",
            "Tangram?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#07901FIt seems that an Imperial-make black\x01",
            "transport forced its way through the\x01",
            "gate with incomplete documents.\x02\x03",
            "#07903FI think there won't be any problem\x01",
            "since at least a minimum check was\x01",
            "finished, but...\x02\x03",
            "#07901FThe CGF's honor is completely\x01",
            "ruined, honestly!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x103)
    OP_64(0x105)
    OP_64(0x109)
    Sleep(500)
    OP_63(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x14,
        "#07900F...Is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FN-No...\x02",
    )

    CloseMessageWindow()

    def lambda_8AD1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8AD1)
    Sleep(10)

    def lambda_8AE1():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8AE1)
    Sleep(50)

    def lambda_8AF1():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8AF1)
    Sleep(10)

    def lambda_8B01():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8B01)
    Sleep(30)

    def lambda_8B11():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8B11)
    Sleep(10)

    def lambda_8B21():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8B21)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x102,
        (
            "#00101FSay, what she just\x01",
            "talked about...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F...Yeah, it seems we\x01",
            "ended up looking in the\x01",
            "wrong place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FHe's already fled to the\x01",
            "Republic so I don't think\x01",
            "there's anything we can do.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_END)), "loc_8CB5")

    ChrTalk(
        0x101,
        (
            "#00001FI feel sorry for Billy and St.\x01",
            "Ursula but... All we can do is\x01",
            "tell them what happened.\x02\x03",
            "#00006F*sigh*... If only we had\x01",
            "listened properly to Franz's\x01",
            "story...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D18")

    label("loc_8CB5")


    ChrTalk(
        0x101,
        (
            "#00006FI feel sorry for Billy and St.\x01",
            "Ursula but... All we can do is\x01",
            "tell them what happened.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D18")


    ChrTalk(
        0x14,
        "#07900F???\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others explained the\x01",
            "facts to Billy and Ricardo who\x01",
            "were waiting at the airport...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, they went with\x01",
            "Billy to St. Ursula Hospital\x01",
            "to tell them the situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x93, 0x1, 0x2)
    SetScenarioFlags(0x22, 2)
    NewScene("t1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_8382 end

    def Function_30_8E14(): pass

    label("Function_30_8E14")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41400.itc", 0x1E)
    LoadChrToIndex("chr/ch41500.itc", 0x1F)
    LoadChrToIndex("chr/ch41800.itc", 0x20)
    LoadChrToIndex("chr/ch41402.itc", 0x21)
    LoadChrToIndex("chr/ch41502.itc", 0x22)
    LoadChrToIndex("chr/ch12200.itc", 0x23)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -105500, 0, 2100, 45)
    OP_4B(0xD, 0xFF)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x1)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -101900, 50, 2200, 90)
    OP_4B(0xE, 0xFF)
    SetChrChipByIndex(0xE, 0x22)
    SetChrSubChip(0xE, 0x2)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -99600, 50, 2200, 270)
    OP_4B(0xF, 0xFF)
    SetChrChipByIndex(0xF, 0x21)
    SetChrSubChip(0xF, 0x2)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -99600, 50, 4000, 270)
    OP_4B(0x10, 0xFF)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -100200, 0, 400, 0)
    OP_4B(0x11, 0xFF)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -99200, 0, 700, 0)
    OP_4B(0x12, 0xFF)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -98100, 0, 2600, 315)
    SetChrChipByIndex(0x19, 0x23)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -103500, 0, -700, 45)
    OP_68(-101000, 2300, 3300, 0)
    MoveCamera(293, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_68(-101000, 1300, 3300, 10000)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(180, 120, -1, -1)
    SetChrName("Chairman MacDowell")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WAnd, more than the legitimacy of these legal\x01",
            "procedures...\x02\x03",
            "There is only one thing I want to ask to you\x01",
            "all.\x02\x03",
            "This situation we're all in, the structure of\x01",
            "our government at present, and how we citizens\x01",
            "ought to be... Are they truly "correct"?\x02\x03",
            "That is all─ That's all I wish to say.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m0302", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_8E14 end

    def Function_31_913E(): pass

    label("Function_31_913E")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "CGF Only Freight Line Ahead\x01",
            "Authorized Personnel Only\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_31_913E end

    SaveToFile()

Try(main)
