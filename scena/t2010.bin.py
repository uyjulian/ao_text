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
        "Function_9_1C1A",         # 09, 9
        "Function_10_289F",        # 0A, 10
        "Function_11_28A3",        # 0B, 11
        "Function_12_378D",        # 0C, 12
        "Function_13_454B",        # 0D, 13
        "Function_14_454F",        # 0E, 14
        "Function_15_57E4",        # 0F, 15
        "Function_16_5B54",        # 10, 16
        "Function_17_5E6D",        # 11, 17
        "Function_18_6195",        # 12, 18
        "Function_19_62AF",        # 13, 19
        "Function_20_6440",        # 14, 20
        "Function_21_66B2",        # 15, 21
        "Function_22_697A",        # 16, 22
        "Function_23_6B58",        # 17, 23
        "Function_24_7327",        # 18, 24
        "Function_25_73F5",        # 19, 25
        "Function_26_75AF",        # 1A, 26
        "Function_27_787E",        # 1B, 27
        "Function_28_7E35",        # 1C, 28
        "Function_29_87AB",        # 1D, 29
        "Function_30_92A3",        # 1E, 30
        "Function_31_9576",        # 1F, 31
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1007")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F0B")

    NpcTalk(
        0x8,
        "Soldier Connors",
        (
            "The bridge connecting the national\x01",
            "border is still fallen, but security\x01",
            "towards the Imperial Army is severe.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Connors",
        (
            "If they thought to begin invading,\x01",
            "they'll probably repair the\x01",
            "fallen bridge right away.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Connors",
        (
            "For good or for evil, the Empire is in a civil war...\x01",
            "Now that we can, we have to adjust our positions too.\x01\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1002")

    label("loc_F0B")


    NpcTalk(
        0x8,
        "Soldier Connors",
        (
            "If the Empire thought to begin invading, they'll\x01",
            "probably repair the fallen bridge right away.\x01\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Connors",
        (
            "For good or for evil, the Empire is in a civil war...\x01",
            "Now that we can, we have to adjust our positions too.\x01\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1002")

    Jump("loc_1C16")

    label("loc_1007")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_10ED")

    ChrTalk(
        0x8,
        (
            "In light of the recent state of tension,\x01",
            "it seems there're a considerable number\x01",
            "of foreigners who're leaving Crossbell.\x02",
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
    Jump("loc_1C16")

    label("loc_10ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1306")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1231")

    ChrTalk(
        0x8,
        (
            "Yesterday, the unit lead by 2nd Lt. Mireille\x01",
            "seems to have spotted a giant monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems that she will patrol the autonomous\x01",
            "state with a company unit for a while to\x01",
            "look out for the monster that ran away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh boy...\x01",
            "While in a continued state of tension\x01",
            "the busyness increases.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1301")

    label("loc_1231")


    ChrTalk(
        0x8,
        (
            "It seems that she will patrol the autonomous\x01",
            "state with a company unit for a while to\x01",
            "look out for the monster that ran away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh boy...\x01",
            "While in a continued state of tension\x01",
            "the busyness increases.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1301")

    Jump("loc_1C16")

    label("loc_1306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_13E1")

    ChrTalk(
        0x8,
        (
            "The Imperial trader who just passed\x01",
            "through here seemed he was talking about\x01",
            "many things regarding Crossbell independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems that this topic is arousing\x01",
            "criticism even in the Empire area.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C16")

    label("loc_13E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_160F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1537")

    ChrTalk(
        0x8,
        (
            "Recently, it seems that practice\x01",
            "is being performed just for show\x01",
            "inside the Empire fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is to put pressure on us CGF...\x01",
            "No, in this case it's probably to\x01",
            "put pressure on Mayor Dieter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although if compared to the state of tension just before\x01",
            "the "Non-Aggression Pact", it's a charming thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_160A")

    label("loc_1537")


    ChrTalk(
        0x8,
        (
            "Recently, it seems that practice\x01",
            "is being performed just for show\x01",
            "inside the Empire fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although if compared to the state of tension just before\x01",
            "the "Non-Aggression Pact", it's a charming thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_160A")

    Jump("loc_1C16")

    label("loc_160F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1819")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178C")

    ChrTalk(
        0x8,
        (
            "Because we received intel about\x01",
            "terrorists we were ordered to do\x01",
            "strict checks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With today security system it\x01",
            "should be almost impossible to\x01",
            "infiltrate from an overland route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, even for the air route\x01",
            "security continues from a\x01",
            "special facility nearby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even in the CGF where airships can't be deployed,\x01",
            "we must do all that we can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1814")

    label("loc_178C")


    ChrTalk(
        0x8,
        (
            "Due to the autonomous state regulation,\x01",
            "the CGF can't posses airships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although you'd really want them\x01",
            "for airspace security.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1814")

    Jump("loc_1C16")

    label("loc_1819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1AC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19EA")

    ChrTalk(
        0x8,
        (
            "Chancellor Osborne who's coming to the Trade Conference \x01",
            "is commonly called "The Blood and Iron Chancellor".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The origin of that seems to come from his creed\x01",
            "that "A nation stability has to come from blood \x01",
            "and iron, namely military might and weapons".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Under these words, he militarily\x01",
            "annexed many autonomous\x01",
            "states to the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's no doubt that for\x01",
            "Crossbell he's the number one\x01",
            "character to be careful about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AC4")

    label("loc_19EA")


    ChrTalk(
        0x8,
        (
            "The Empire militarily annexed many\x01",
            "autonomous states and in many of those,\x01",
            ""The Blood and Iron Chancellor" was involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's no doubt that for\x01",
            "Crossbell he's the number one\x01",
            "character to be careful about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC4")

    Jump("loc_1C16")

    label("loc_1AC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1C16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA7")

    ChrTalk(
        0x8,
        (
            "If you pass through that iron fence,\x01",
            "it's just a shot until you reach\x01",
            "the Empire "Garrelia Fortress".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you intend to go there, be warned.\x01",
            "The Empire immigrants\x01",
            "check is quite strict.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C16")

    label("loc_1BA7")


    ChrTalk(
        0x8,
        (
            "The Empire immigrants\x01",
            "check is quite strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you intend to go to\x01",
            ""Garrelia Fortress", be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C16")

    TalkEnd(0x8)
    Return()

    # Function_8_D7B end

    def Function_9_1C1A(): pass

    label("Function_9_1C1A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1E47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D8E")

    NpcTalk(
        0x9,
        "Soldier Sig",
        (
            "The independence declaration of invalidity,\x01",
            "the Secretary of Defense getting missing...\x01",
            "And I also heard that the President has been restrained.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Sig",
        (
            "Is it all right for us to keep working\x01",
            "as the State Guard from now on...?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Sig",
        (
            "...No matter what I think in such a situation,\x01",
            "I can't clear my doubts.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1E42")

    label("loc_1D8E")


    NpcTalk(
        0x9,
        "Soldier Sig",
        (
            "Is it all right for us to keep working\x01",
            "as the State Guard from now on...?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Sig",
        (
            "...No matter what I think in such a situation,\x01",
            "I can't clear my doubts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E42")

    Jump("loc_289B")

    label("loc_1E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1EEA")

    ChrTalk(
        0xFE,
        (
            "In the future, no matter what\x01",
            "tricks the Empire pulls, we\x01",
            "won't ever yield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I won't let in vain\x01",
            "my comrades' deaths.\x01",
            "...As if I'd do that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_289B")

    label("loc_1EEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1FC6")

    ChrTalk(
        0xFE,
        (
            "*sigh*...\x01",
            "It seems the fatigue of last night\x01",
            "repairing works is still in me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Under such a tense situation I\x01",
            "don't know if something will happen.\x01",
            "Maybe I should go take a nap now that I still can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_289B")

    label("loc_1FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_21A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F1")

    ChrTalk(
        0xFE,
        (
            "We were going to undertake\x01",
            "the investigation for those\x01",
            ""Cryptids" things, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It can't be helped that the\x01",
            "tension continues due to\x01",
            "the independence proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...I'll leave it to you then, Randy and guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah, you too, well,\x01",
            "break a leg, 'k?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_219C")

    label("loc_20F1")


    ChrTalk(
        0xFE,
        (
            "We were going to undertake\x01",
            "the investigation for those\x01",
            ""Cryptids" things, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It can't be helped that the\x01",
            "tension continues due to\x01",
            "the independence proposal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_219C")

    Jump("loc_289B")

    label("loc_21A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_232C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2286")

    ChrTalk(
        0xFE,
        (
            "The other day, Warrant-Officer Mireille\x01",
            "was promoted to 2nd Lt..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the other countries' armies, a 2nd Lt.\x01",
            "is a rank equal to an Ensign.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I expect great result from\x01",
            "her in the future too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2327")

    label("loc_2286")


    ChrTalk(
        0xFE,
        (
            "Thinking about her merits,\x01",
            "this promotion was too late, but...\x01",
            "Well, it's something to be happy for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I expect great result from\x01",
            "her in the future too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2327")

    Jump("loc_289B")

    label("loc_232C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_23C9")

    ChrTalk(
        0xFE,
        (
            "No response from the detector.\x01",
            "...It seems there're no dangerous objects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll check under the\x01",
            "car frame too just in case...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_289B")

    label("loc_23C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2617")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_255C")

    ChrTalk(
        0xFE,
        (
            "It indeed makes sense that security \x01",
            "during the Trade Conference is\x01",
            "directed by Commander Sonya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By assigning the minimum required personnel\x01",
            "with pertinent abilities, we're smoothly covering\x01",
            "the national border security too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a great difference compared to the former Commander.\x01",
            "As expected, that's what a person who\x01",
            "ought to be on top of others should be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2612")

    label("loc_255C")


    ChrTalk(
        0xFE,
        (
            "I too thought that I could, one day, take up the\x01",
            "commander post by piling up achievements, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I realized that's totally impossible as\x01",
            "long as Commander Sonya is alive.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2612")

    Jump("loc_289B")

    label("loc_2617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_289B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_279A")

    ChrTalk(
        0xFE,
        (
            "The former Commander had ties with\x01",
            "Joachim through Hartmann and was\x01",
            "used even in the Cult incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After he had a disciplinary dismissal, it was \x01",
            "entirely a matter of course that Vice Commander \x01",
            "Sonya would've become commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, the CGF organization is probably\x01",
            "going to be managed way more correctly.\x01",
            "It's really something joyous.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_289B")

    label("loc_279A")


    ChrTalk(
        0xFE,
        (
            "Because of the former Commander incompetence,\x01",
            "all the responsibilities fell on the shoulder of\x01",
            "Warrant-Officer Mireille until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, the CGF organization is probably\x01",
            "going to be managed way more correctly.\x01",
            "It's really something joyous.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_289B")

    TalkEnd(0xFE)
    Return()

    # Function_9_1C1A end

    def Function_10_289F(): pass

    label("Function_10_289F")

    Call(0, 11)
    Return()

    # Function_10_289F end

    def Function_11_28A3(): pass

    label("Function_11_28A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28CC")
    Call(0, 28)
    Return()

    label("loc_28CC")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3789")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2929")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2929")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2949")
    OP_AF(0x73)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3784")

    label("loc_2949")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_295D")
    Jump("loc_3784")

    label("loc_295D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3784")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2A24")

    ChrTalk(
        0xA,
        (
            "The "Satiating Hot Pot" I serve to the CGF \x01",
            "Bellguard Gate members is delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We often do hot pot parties and\x01",
            "they really turn into meat contests.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3784")

    label("loc_2A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2BB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B01")

    ChrTalk(
        0xA,
        (
            "Everyone is uneasy, but...\x01",
            "I'm sure it'll be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "After all, Mr. Cless\x01",
            "said he'll absolutely\x01",
            "protect me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That's why I have to rise everyone's\x01",
            "spirit by doing what I can do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2BAF")

    label("loc_2B01")


    ChrTalk(
        0xA,
        (
            "It seems that everyone is uneasy\x01",
            "due to an absurd giant tree and the\x01",
            "rumor of the President's restraint...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I have to rise everyone's\x01",
            "spirit by doing what I can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BAF")

    Jump("loc_3784")

    label("loc_2BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2D84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CD3")

    ChrTalk(
        0xA,
        (
            "The state of tension with the Empire...\x01",
            "It really makes you remember the time\x01",
            "before the Non-Aggression Pact signing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When those Empire "Railway Cannons"\x01",
            "were pointed at us, I was really scared...\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hope that such a thing\x01",
            "doesn't happen again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2D7F")

    label("loc_2CD3")


    ChrTalk(
        0xA,
        (
            "Before the Non-Aggression Pact signing,\x01",
            "it happened that the Empire took out\x01",
            "those "Railway Cannons" for practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hope that such a thing\x01",
            "doesn't happen again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D7F")

    Jump("loc_3784")

    label("loc_2D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2F8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EBE")

    ChrTalk(
        0xA,
        (
            "Unfortunately, today is raining.\x01",
            "Seems it'll be hard for the members guarding outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In such a day, a dish that\x01",
            "warms up the body is nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I guess I'll put to practical use the extraordinary \x01",
            "spicy stew I gave to Mr. Cless yesterday \x01",
            "and prepare a hot pot or something.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2F87")

    label("loc_2EBE")


    ChrTalk(
        0xA,
        (
            "In such a rainy day, a dish that\x01",
            "warms up the body is nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I guess I'll put to practical use the extraordinary \x01",
            "spicy stew I gave to Mr. Cless yesterday \x01",
            "and prepare a hot pot or something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F87")

    Jump("loc_3784")

    label("loc_2F8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3130")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_308E")

    ChrTalk(
        0xA,
        (
            "Because recently Mr. Cless looked spent,\x01",
            "I made him an extraordinary spicy stew to\x01",
            "wake him out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At first, I thought I had\x01",
            "made it a little too spicy, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He's actually eating it, so...\x01",
            "Uh uh, it seems it was ok.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_312B")

    label("loc_308E")


    ChrTalk(
        0xA,
        (
            "Uh uh, eating it\x01",
            "so happily makes\x01",
            "me really glad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Since we're going out, maybe from\x01",
            "now on I'll occasionally prepare \x01",
            "some special dishes for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_312B")

    Jump("loc_3784")

    label("loc_3130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3296")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31FC")

    ChrTalk(
        0xA,
        (
            "Mr. Cless looks\x01",
            "spent lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Alright, I guess I'll prepare \x01",
            "him a dish or something\x01",
            "to fire him up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He's still my "trial boyfriend",\x01",
            "so I must at least do this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3291")

    label("loc_31FC")


    ChrTalk(
        0xA,
        (
            "Well then, I guess I'll prepare\x01",
            "Mr. Cless a dish or something\x01",
            "to fire him up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He's still my "trial boyfriend",\x01",
            "so I must at least do this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3291")

    Jump("loc_3784")

    label("loc_3296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_335A")

    ChrTalk(
        0xA,
        (
            "They say that there's the\x01",
            "possibility that terrorists\x01",
            "will infiltrate in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Security at the gate has been increased,\x01",
            "but I wonder if the members will be all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3784")

    label("loc_335A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_350E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_347B")

    ChrTalk(
        0xA,
        (
            "It's been quite some time since I've\x01",
            "started to go out with Mr. Cless to try.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But even if we're "going out",\x01",
            "we aren't doing anything different...\x01",
            "Could it be all there is to it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To men, maybe it's the\x01",
            "fact itself of "going out"\x01",
            "that's important.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3509")

    label("loc_347B")


    ChrTalk(
        0xA,
        (
            "I don't have much experience too\x01",
            "so I don't get it well, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To men, maybe it's the\x01",
            "fact itself of "going out"\x01",
            "that's important.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3509")

    Jump("loc_3784")

    label("loc_350E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3784")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36ED")
    TurnDirection(0xA, 0x104, 0)

    ChrTalk(
        0xA,
        (
            "Oh, welco...\x01",
            "Wait, if it isn't Randy.\x02",
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
            "#00302FHa ha, well, that's right, but...\x01",
            "I wanted to take a look\x01",
            "at the cute you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ahaha, you keep\x01",
            "saying jokes as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Also, if you seduced me now,\x01",
            "I think Mr. Cless would be mad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FRandy, that CGF member\x01",
            "sat there is eyeing you\x01",
            "really badly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F...I-It's true that could be troublesome.\x01",
            "I'll keep it in mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3784")

    label("loc_36ED")


    ChrTalk(
        0xA,
        (
            "Uh uh, well, that aside...\x01",
            "Since you're here, eat something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It would make me happy if you ate tons\x01",
            "like during the rehabilitation training.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3784")

    Jump("loc_28D9")

    label("loc_3789")

    TalkEnd(0xA)
    Return()

    # Function_11_28A3 end

    def Function_12_378D(): pass

    label("Function_12_378D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37B6")
    Call(0, 27)
    Return()

    label("loc_37B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3961")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38C1")

    NpcTalk(
        0xB,
        "Soldier Cless",
        (
            "Honestly, I too don't\x01",
            "know what to do.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Cless",
        (
            "However, I must protect what's\x01",
            "important to me with these hands.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Cless",
        (
            "A-Alright...\x01",
            "For now, I'll eat!\x01",
            "I'll eat and eat and build up my strength!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_395C")

    label("loc_38C1")


    NpcTalk(
        0xB,
        "Soldier Cless",
        "You can't fight on an empty stomach, yes.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Cless",
        (
            "In order to protect what's important to me...\x01",
            "I'll eat! I'll eat and eat!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_395C")

    Jump("loc_4547")

    label("loc_3961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3B6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A9A")

    ChrTalk(
        0xFE,
        (
            "In the fight in the Mainz region the other day,\x01",
            "many of my comrades were taken out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we had had powerful tanks, the damage\x01",
            "would probably have been much lower...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To protect sweet Stella and the persons\x01",
            "important to me in the future, as\x01",
            "I thought, we need independence.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3B69")

    label("loc_3A9A")


    ChrTalk(
        0xFE,
        (
            "If we had had powerful tanks,\x01",
            "the damage in Mainz could've\x01",
            "been kept in check a lot more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To protect sweet Stella and the persons\x01",
            "important to me in the future, as\x01",
            "I thought, we need independence.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B69")

    Jump("loc_4547")

    label("loc_3B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C78")

    ChrTalk(
        0xFE,
        (
            "After I ate sweet Stella's extremely\x01",
            "spicy stew yesterday, somehow\x01",
            "my body's condition is good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hu hu hu...\x01",
            "This is exactly what they call the "power of love", I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Although I've already had enough of that spiciness.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3D2B")

    label("loc_3C78")


    ChrTalk(
        0xFE,
        (
            "After I ate sweet Stella's extremely\x01",
            "spicy stew yesterday, somehow\x01",
            "my body's condition is good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must thank her.\x01",
            "...Although I've already had enough of that spiciness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D2B")

    Jump("loc_4547")

    label("loc_3D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3E63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DF9")

    ChrTalk(
        0xFE,
        (
            "*huff huff*...\x01",
            "Eek, i-it's spicy, too spicy...!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "N-No, my sweet made\x01",
            "it especially for me.\x01",
            "A man can clean it if he licks it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uooooh, *eating greedily*...!!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3E5E")

    label("loc_3DF9")


    ChrTalk(
        0xFE,
        (
            "*huff huff*...\x01",
            "I-It's really spicy...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "B-but I'll finish all of it!\x01",
            "*eating greedily*...!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E5E")

    Jump("loc_4547")

    label("loc_3E63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F14")

    ChrTalk(
        0xFE,
        (
            "*sigh*, I can't help but being very\x01",
            "tired due to the recent state of tension.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...No, no, sweet Stella\x01",
            "is watching me, so I\x01",
            "must look sharp.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3F63")

    label("loc_3F14")


    ChrTalk(
        0xFE,
        (
            "Lately I'm tired, but...\x01",
            "Sweet Stella is watching, \x01",
            "so I must look sharp.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F63")

    Jump("loc_4547")

    label("loc_3F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4025")

    ChrTalk(
        0xFE,
        (
            "Today I must cleanly do my watch\x01",
            "and show sweet Stella my good points.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't care if you're a terrorist or whatever,\x01",
            "just try coming at me from wherever you want.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4547")

    label("loc_4025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_415D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_410F")

    ChrTalk(
        0xFE,
        (
            "I've finally started going out\x01",
            "with sweet Stella, but I can't\x01",
            "even invite her to a date.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lately I've been busy with stuff\x01",
            "related to the Trade Conference,\x01",
            "and to begin with, I'm not resourceful...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4158")

    label("loc_410F")


    ChrTalk(
        0xFE,
        (
            "Damn it...\x01",
            "Somehow I'd like to progress\x01",
            "things with sweet Stella...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4158")

    Jump("loc_4547")

    label("loc_415D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4547")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4295")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_424D")

    ChrTalk(
        0xB,
        (
            "Tch...it wouldn't hurt you\x01",
            "if you listened to me a\x01",
            "little, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If it's about sweet Stella,\x01",
            "I could talk for hours!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FBye then, senior.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I told you to listen!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4290")

    label("loc_424D")


    ChrTalk(
        0xB,
        (
            "Tch... \x01",
            "If it's about sweet Stella,\x01",
            "I could talk for hours...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4290")

    Jump("loc_4547")

    label("loc_4295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4317")

    ChrTalk(
        0xFE,
        (
            "Randyyyy....\x01",
            "What were you doing to my sweet...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FT-There, there, calm down.\x01",
            "I didn't do anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4547")

    label("loc_4317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44BF")

    ChrTalk(
        0xFE,
        (
            "Hu hu, Stella...\x01",
            "My sweet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F("M-My sweet"...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FOh, by the way, senior...\x01",
            "I heard some time ago that you're\x01",
            "going out with Stella "to try", huh?\x02\x03",
            "#00309FHa ha, done a little progress?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...M-More or less.\x01",
            "Well, we're lovey dovey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Every day I eat here\x01",
            "and gaze at sweet Stella...\x01",
            "Every day is happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(...In other words, there hasn't\x01",
            "been any progress yet...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4547")

    label("loc_44BF")


    ChrTalk(
        0xFE,
        (
            "S-Sweet Stella and I are\x01",
            "only getting started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Randy, don't cut in\x01",
            "and seduce her.\x01",
            "...I beg you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F(He's hopeless.)\x02",
    )

    CloseMessageWindow()

    label("loc_4547")

    TalkEnd(0xFE)
    Return()

    # Function_12_378D end

    def Function_13_454B(): pass

    label("Function_13_454B")

    Call(0, 14)
    Return()

    # Function_13_454B end

    def Function_14_454F(): pass

    label("Function_14_454F")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_455C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57E0")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Rest\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45AC")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_45AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45CC")
    OP_AF(0x74)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57DB")

    label("loc_45CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45E0")
    Jump("loc_57DB")

    label("loc_45E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57DB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_478C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46EA")

    ChrTalk(
        0xC,
        (
            "In such times, the mental\x01",
            "strain is especially bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you're taking a break, take your\x01",
            "time to rest and calm down your mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...That said, I'm uneasy too.\x01",
            "I wonder if peaceful times will come back?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4787")

    label("loc_46EA")


    ChrTalk(
        0xC,
        (
            "If you're taking a break, take your\x01",
            "time to rest and calm down your mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...That said, I'm uneasy too!\x01",
            "I wonder if peaceful times will come back?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4787")

    Jump("loc_57DB")

    label("loc_478C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_49DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48EF")

    ChrTalk(
        0xC,
        (
            "The "Red Constellation" that retreated\x01",
            "somewhere after doing what they please\x01",
            "in Crossbell, seem they had an airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Furthermore, it seems that che CGF\x01",
            "anti-aircraft radar didn't catch it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Honestly, if you have funds power,\x01",
            "there's no technology you can't get.\x01",
            "I wonder who in the world are those people...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_49D7")

    label("loc_48EF")


    ChrTalk(
        0xC,
        (
            "They say that the "Red Constellation"\x01",
            "airship didn't even got caught by the\x01",
            "CGF anti-aircraft radar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Honestly, if you have funds power,\x01",
            "there's no technology you can't get.\x01",
            "I wonder who in the world are those people...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49D7")

    Jump("loc_57DB")

    label("loc_49DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4C84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B87")

    ChrTalk(
        0xC,
        (
            "I heard about the story of an accident yesterday.\x01",
            "It seems that because a giant monster struck\x01",
            "with all its might, a derailment accident happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That train is made by the Reinford Corporation,\x01",
            "famous in the Empire for its weapons development.\x01",
            "It should've gotten at least a sturdy armor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I didn't see its shape in person,\x01",
            "but somehow I get how much\x01",
            "frightening a monster that was.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4C7F")

    label("loc_4B87")


    ChrTalk(
        0xC,
        (
            "That train is made by the Reinford Corporation,\x01",
            "famous in the Empire for its weapons development,\x01",
            "and yet it made it derail after striking it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I didn't see its shape in person,\x01",
            "but somehow I get how much\x01",
            "frightening a monster that was.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C7F")

    Jump("loc_57DB")

    label("loc_4C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4F6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E7C")

    ChrTalk(
        0xC,
        (
            "With the mechanization of each country's' army, what\x01",
            "has been highly regarded in recent years is air tactics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For instance, in the "Hundred Days War"\x01",
            "12 years ago, Liberl was invaded due to the\x01",
            "Empire overwhelming military strength, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In the final stage of the conflict, Liberl\x01",
            "overturned the state of the war at once\x01",
            "with the newly developed airships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The fact that the CGF isn't allowed possession\x01",
            "of airships is because of circumstances like those.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4F66")

    label("loc_4E7C")


    ChrTalk(
        0xC,
        (
            "In recent years, with the mechanization of each countries' \x01",
            "army, what has been highly regarded is air tactics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "When we'll be independent and the\x01",
            "CGF becomes an army, first of all I\x01",
            "absolutely want we get airships deployed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F66")

    Jump("loc_57DB")

    label("loc_4F6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5193")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50AB")

    ChrTalk(
        0xC,
        (
            "If Crossbell becomes independent,\x01",
            "even the CGF will be managed as\x01",
            "a regular army, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even the members' equipments will be changed to \x01",
            "something more powerful than what they had until now.\x01",
            "They'll even get tanks deployed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Uuh, it can be really appealing\x01",
            "to a military otaku.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_518E")

    label("loc_50AB")


    ChrTalk(
        0xC,
        (
            "After Crossbell becomes independent and\x01",
            "the CGF turns into a regular army, even the \x01",
            "armaments will be more satisfying than now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "They'll even get tanks deployed...\x01",
            "Uuh, it can be really appealing\x01",
            "to a military otaku.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_518E")

    Jump("loc_57DB")

    label("loc_5193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_536A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52C0")

    ChrTalk(
        0xC,
        (
            "Today, there's finally the\x01",
            "conference at Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Because there's concern towards\x01",
            "the Empire and Republic, I think the\x01",
            "CGF can't openly guard, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's an important international conference. \x01",
            "I wish they somehow protect it even from out of sight.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5365")

    label("loc_52C0")


    ChrTalk(
        0xC,
        (
            "Today, there's finally the\x01",
            "conference at Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's an important international conference. \x01",
            "I wish they somehow protect it even from out of sight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5365")

    Jump("loc_57DB")

    label("loc_536A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_55E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_550D")

    ChrTalk(
        0xC,
        (
            "It's passed a little while since the new type\x01",
            "of armored vehicle has been deployed, but...\x01",
            "Dear me, it really is great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's also got powerful missile pods and\x01",
            "the armor has been reinforced considerably.\x01",
            "It's the CGF best armament without a doubt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, it's unfair to compare it to other\x01",
            "countries' airships and tanks, but I believe\x01",
            "it combines simplicity with functionality.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_55E4")

    label("loc_550D")


    ChrTalk(
        0xC,
        (
            "The new type of armored vehicle is,\x01",
            "without a doubt, the CGF best armament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, it's unfair to compare it to other\x01",
            "countries' airships and tanks, but I believe\x01",
            "it combines simplicity with functionality.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55E4")

    Jump("loc_57DB")

    label("loc_55E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_57DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5711")

    ChrTalk(
        0xC,
        (
            "I'm a military otaku...\x01",
            "What they shorten as miliota.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I really love army related things,\x01",
            "so even working at this gate feels\x01",
            "like my hobby grows in intensity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, strictly speaking, the\x01",
            "Crossbell CGF is not an army, but...\x01",
            "To me, it's greatly charming.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_57DB")

    label("loc_5711")


    ChrTalk(
        0xC,
        (
            "I'm what they call a miliota.\x01",
            "Even working at this gate feels\x01",
            "like my hobby grows in intensity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, strictly speaking, the\x01",
            "Crossbell CGF is not an army, but...\x01",
            "To me, it's greatly charming.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57DB")

    Jump("loc_455C")

    label("loc_57E0")

    TalkEnd(0xC)
    Return()

    # Function_14_454F end

    def Function_15_57E4(): pass

    label("Function_15_57E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_57F5")
    Jump("loc_5B50")

    label("loc_57F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_594D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58D8")

    ChrTalk(
        0xFE,
        (
            "I got caught up in yesterday\x01",
            "train derailment accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, since I got out of it with light injuries,\x01",
            "I got my daughter to come pick me up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ooh, ow ow ow...\x01",
            "It still hurts a little.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5948")

    label("loc_58D8")


    ChrTalk(
        0xFE,
        (
            "Ooh, ow ow ow...\x01",
            "It still hurts a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should've stayed \x01",
            "hospitalised for a little longer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5948")

    Jump("loc_5B50")

    label("loc_594D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5A0A")

    ChrTalk(
        0xFE,
        (
            "Crossbell trying to be independent...\x01",
            "They should know their place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From the point of view of an\x01",
            "Empire citizen, it feels like being\x01",
            "betrayed by a trusted follower.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B50")

    label("loc_5A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5A18")
    Jump("loc_5B50")

    label("loc_5A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5A97")

    ChrTalk(
        0xFE,
        "Isn't the inspection over already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't care if it's an anti-terrorism\x01",
            "measure, it's just a bother.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B50")

    label("loc_5A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5AA5")
    Jump("loc_5B50")

    label("loc_5AA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5B50")

    ChrTalk(
        0xFE,
        (
            "There's no doubt that His Grace the Chancellor\x01",
            "will come through the Trade Conference with a\x01",
            "profitable agreement for the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hu hu, how wonderful.\x02",
    )

    CloseMessageWindow()

    label("loc_5B50")

    TalkEnd(0xFE)
    Return()

    # Function_15_57E4 end

    def Function_16_5B54(): pass

    label("Function_16_5B54")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5C12")

    ChrTalk(
        0xFE,
        (
            "I've been perplexed since that raid incident, but...\x01",
            "I decided to go back to my Empire fatherland.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It would be unbearable if I got\x01",
            "involved in such a thing again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E69")

    label("loc_5C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5C20")
    Jump("loc_5E69")

    label("loc_5C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5C2E")
    Jump("loc_5E69")

    label("loc_5C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5CAF")

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
            "Crossbell should stay exploited\x01",
            "for the sake of the Empire.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E69")

    label("loc_5CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5CBD")
    Jump("loc_5E69")

    label("loc_5CBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5D6B")

    ChrTalk(
        0xFE,
        (
            "Boy, it's probably not something\x01",
            "to come to see in a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, because the Orchis Tower\x01",
            "became a topic even in the Empire,\x01",
            "I too wanted to see it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E69")

    label("loc_5D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E69")

    ChrTalk(
        0xFE,
        (
            "The story goes that the rumored Prince Olivert\x01",
            "is going to come to Crossbell as the emperor\x01",
            "representative at the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, he was probably appointed as\x01",
            "help to the "Blood and Iron Chancellor"\x01",
            "by His Majesty the Emperor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E69")

    TalkEnd(0xFE)
    Return()

    # Function_16_5B54 end

    def Function_17_5E6D(): pass

    label("Function_17_5E6D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_601F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F74")

    ChrTalk(
        0xF,
        (
            "There's a civil war going on in\x01",
            "the Empire but even so I want \x01",
            "to return to my fatherland.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "However, I'd never have dreamed\x01",
            "about the bridge to completely\x01",
            "collapse like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "...I wonder what should\x01",
            "I do from now on.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_601A")

    label("loc_5F74")


    ChrTalk(
        0xF,
        (
            "Father said he was going to look\x01",
            "from above at the fallen bridge from\x01",
            "the balcony and went up the stairs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "...As I feared, we can't\x01",
            "go back to the Empire.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_601A")

    Jump("loc_6191")

    label("loc_601F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_602D")
    Jump("loc_6191")

    label("loc_602D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_603B")
    Jump("loc_6191")

    label("loc_603B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_60C8")

    ChrTalk(
        0xFE,
        (
            "Somehow the CGF people\x01",
            "are all tense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want to stay long in such a place,\x01",
            "so I think I'll go back home quick.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6191")

    label("loc_60C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_60D6")
    Jump("loc_6191")

    label("loc_60D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_60E4")
    Jump("loc_6191")

    label("loc_60E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6188")

    ChrTalk(
        0xFE,
        (
            "I came to see the rumored high-rise\x01",
            "building, the Orchis Tower or\x01",
            "whatever it's called.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what kind of building it is.\x01",
            "I can't wait.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6191")

    label("loc_6188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6191")

    label("loc_6191")

    TalkEnd(0xFE)
    Return()

    # Function_17_5E6D end

    def Function_18_6195(): pass

    label("Function_18_6195")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_622D")

    ChrTalk(
        0xFE,
        (
            "I would've liked to have had a\x01",
            "little more fun in Crossbell, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently, the place is scary.\x01",
            "It can't be helped then...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62AB")

    label("loc_622D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_623B")
    Jump("loc_62AB")

    label("loc_623B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6249")
    Jump("loc_62AB")

    label("loc_6249")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6257")
    Jump("loc_62AB")

    label("loc_6257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6294")

    ChrTalk(
        0xFE,
        (
            "*sigh*...\x01",
            "I want to go to the city quick.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62AB")

    label("loc_6294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_62A2")
    Jump("loc_62AB")

    label("loc_62A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_62AB")

    label("loc_62AB")

    TalkEnd(0xFE)
    Return()

    # Function_18_6195 end

    def Function_19_62AF(): pass

    label("Function_19_62AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_62C0")
    Jump("loc_643C")

    label("loc_62C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6367")

    ChrTalk(
        0xFE,
        (
            "Aah, to think it's raining...\x01",
            "Maybe I should've used the railway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because we're just after that accident,\x01",
            "I didn't wanted to use it very much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_643C")

    label("loc_6367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6375")
    Jump("loc_643C")

    label("loc_6375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6383")
    Jump("loc_643C")

    label("loc_6383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6391")
    Jump("loc_643C")

    label("loc_6391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6433")

    ChrTalk(
        0xFE,
        (
            "Due to traffic regulation, this morning\x01",
            "the railway couldn't be used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that private train is passing,\x01",
            "so I guess it can't be helped.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_643C")

    label("loc_6433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_643C")

    label("loc_643C")

    TalkEnd(0xFE)
    Return()

    # Function_19_62AF end

    def Function_20_6440(): pass

    label("Function_20_6440")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_65A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6518")

    ChrTalk(
        0xFE,
        (
            "I just came back with\x01",
            "the goods transport, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, it seems that chaos is\x01",
            "continuing at Crossbell Station too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I guess it can't be helped in such a situation.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_659B")

    label("loc_6518")


    ChrTalk(
        0xFE,
        (
            "As expected, it seems that chaos is\x01",
            "continuing at Crossbell Station too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I guess it can't be helped in such a situation.\x02",
    )

    CloseMessageWindow()

    label("loc_659B")

    Jump("loc_66AE")

    label("loc_65A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_66AE")

    ChrTalk(
        0x13,
        (
            "A railway freight line runs\x01",
            "underground the gate, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I just came back from Crossbell Station\x01",
            "after inspecting the freight train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "...Do you want to go down there?\x01",
            "I don't think there's any problem with that,\x01",
            "just be careful about the train.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66AE")

    TalkEnd(0xFE)
    Return()

    # Function_20_6440 end

    def Function_21_66B2(): pass

    label("Function_21_66B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6943")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_685A")

    ChrTalk(
        0x104,
        (
            "#00301FMireille...\x01",
            "You look quite busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#07901FYes, it seems there're some movements\x01",
            "at the Empire Garrelia Fortress.\x02\x03",
            "#07903FHonestly, we're in an unprecedented\x01",
            "state of tension. ...It's almost the\x01",
            "same as two years ago, before the\x01",
            "Non-Aggression Pact was concluded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIt's so bad...?\x02",
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
            "#07902F...Yes, I know.\x01",
            "Leave this place to me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_693E")

    label("loc_685A")


    ChrTalk(
        0x14,
        (
            "#07903FIt seems there're some movements\x01",
            "at the Empire Garrelia Fortress.\x02\x03",
            "#07901FHonestly, we're in an unprecedented\x01",
            "state of tension. ...It's almost the\x01",
            "same as two years ago, before the\x01",
            "Non-Aggression Pact was concluded.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_693E")

    Jump("loc_6976")

    label("loc_6943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6951")
    Jump("loc_6976")

    label("loc_6951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_695F")
    Jump("loc_6976")

    label("loc_695F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_696D")
    Jump("loc_6976")

    label("loc_696D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6976")

    label("loc_6976")

    TalkEnd(0xFE)
    Return()

    # Function_21_66B2 end

    def Function_22_697A(): pass

    label("Function_22_697A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6A2A")

    ChrTalk(
        0xFE,
        (
            "I would've never dreamed of the\x01",
            "state of things worsening this much\x01",
            "after one week since the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must leave Crossbell\x01",
            "with my daughter fast.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B54")

    label("loc_6A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6A89")

    ChrTalk(
        0xFE,
        "Father, are you all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's go to the mess\x01",
            "hall to rest a little.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B54")

    label("loc_6A89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6A97")
    Jump("loc_6B54")

    label("loc_6A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6B2F")

    ChrTalk(
        0xFE,
        (
            "They say that the number of mysterious\x01",
            "monsters have increased recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's alarming...\x01",
            "I'll go back to the Empire quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B54")

    label("loc_6B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6B3D")
    Jump("loc_6B54")

    label("loc_6B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6B4B")
    Jump("loc_6B54")

    label("loc_6B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6B54")

    label("loc_6B54")

    TalkEnd(0xFE)
    Return()

    # Function_22_697A end

    def Function_23_6B58(): pass

    label("Function_23_6B58")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7155")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6DB7")

    ChrTalk(
        0x15,
        (
            "#03600FYesterday incident at Armorica Village...\x01",
            "I'm really glad you solved it.\x02\x03",
            "#03603FIf you all hadn't been there,\x01",
            "I don't know what would've happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FMinneth, an unscrupulous trader...\x01",
            "He was formidable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FWell, he's been wanted, so I think it will be \x01",
            "only a matter of time until he's arrested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, I wonder.\x01",
            "He was making quite a\x01",
            "tenacious-looking face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FIndeed, it seems we won't be able to\x01",
            "stay safe until he's been caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03608FYou're right...\x01",
            "I hope that until that happens,\x01",
            "there won't be other damage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_714D")

    label("loc_6DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_END)), "loc_6FE1")

    ChrTalk(
        0x15,
        (
            "#03605FOh, everyone...\x02\x03",
            "#03600FRight, about the Minneth incident\x01",
            "at Armorica Village...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...We're sorry to have abandoned it after\x01",
            "we were in the middle of investigating.\x02\x03",
            "#00008FWe had another high\x01",
            "priority job and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03600FNo no, what're you saying.\x01",
            "We had Mr. Grimwood cooperation too\x01",
            "and somehow it was solved...\x02\x03",
            "#03604FAnd that's because the investigation\x01",
            "you all had done until then was really useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI-I see...\x01",
            "In that case, I'm glad.\x02\x03",
            "#00003F(As I thought, we should've\x01",
            "done it through the end.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_714D")

    label("loc_6FE1")


    ChrTalk(
        0x15,
        (
            "#03600FI can't tell you the details since\x01",
            "it involves the prestige of the\x01",
            "Village Chief and the others, but...\x02\x03",
            "#03603FYesterday, there was a very bad\x01",
            "incident at Armorica Village.\x02\x03",
            "#03600FWithout Mr. Grimwood,\x01",
            "probably that incident\x01",
            "wouldn't have been solved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(It seems it was a really bad incident...\x01",
            "I would've been happy to help out somehow.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_714D")

    SetScenarioFlags(0x17C, 1)
    Jump("loc_7323")

    label("loc_7155")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7278")

    ChrTalk(
        0x15,
        (
            "#03600FToday, I came driving through\x01",
            "the West Crossbell Highway...\x02\x03",
            "#03603FIf I think it's the next day of the train\x01",
            "derailment accident, I feel a little uneasy.\x02\x03",
            "#03600FThere's also a rumor going around about\x01",
            "the appearance of a giant monster...\x01",
            "I should be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7323")

    label("loc_7278")


    ChrTalk(
        0x15,
        (
            "#03600FToday, I came driving through\x01",
            "the West Crossbell Highway...\x02\x03",
            "There's also a rumor going around about\x01",
            "the appearance of a giant monster...\x01",
            "I should be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7323")

    TalkEnd(0xFE)
    Return()

    # Function_23_6B58 end

    def Function_24_7327(): pass

    label("Function_24_7327")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_733C")
    Call(0, 25)
    Jump("loc_73F1")

    label("loc_733C")


    ChrTalk(
        0xFE,
        (
            "This national border state of tension...\x01",
            "I hope nothing happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In any case, even us from the\x01",
            "Guild have to ascertain the situation\x01",
            "for the sake of the citizens' safety.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73F1")

    TalkEnd(0xFE)
    Return()

    # Function_24_7327 end

    def Function_25_73F5(): pass

    label("Function_25_73F5")

    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x17, 0x10)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)

    ChrTalk(
        0x16,
        (
            "...I see, it really seems that the\x01",
            "national border is in a sticky situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "At such a time it would be nice to\x01",
            "cooperate with the Empire Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "...Due to military authorities pressure, \x01",
            "the Empire Guild has declined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "They have many men of spirit, but...\x01",
            "Now that the organization itself is in such\x01",
            "a situation, we can't count on them at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "I see...nothing that can be done then.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x16, 0x10)
    ClearChrFlags(0x17, 0x10)
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1, 4)
    Return()

    # Function_25_73F5 end

    def Function_26_75AF(): pass

    label("Function_26_75AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_76BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75CD")
    Call(0, 25)
    Jump("loc_76B7")

    label("loc_75CD")


    ChrTalk(
        0xFE,
        (
            "If we had cooperated with the Empire Guild,\x01",
            "we could've mitigated this state of tension\x01",
            "from a neutral position, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Due to military authorities pressure, \x01",
            "the Empire Guild has declined.\x01",
            "We can't count on them at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76B7")

    Jump("loc_787A")

    label("loc_76BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77D5")

    ChrTalk(
        0xFE,
        (
            "Today Scott and I are acting independently.\x01",
            "He was exterminating a Wanted Monster near here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With the starting of the Trade Conference, we\x01",
            "Bracers too are going to become quite busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before that, we have to accomplish\x01",
            "as many requests as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_787A")

    label("loc_77D5")


    ChrTalk(
        0xFE,
        (
            "With the starting of the Trade Conference, we\x01",
            "Bracers too are going to become quite busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before that, we have to accomplish\x01",
            "as many requests as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_787A")

    TalkEnd(0xFE)
    Return()

    # Function_26_75AF end

    def Function_27_787E(): pass

    label("Function_27_787E")

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
        "#12P#00309FHi, senior Cless.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PHuh...Randy!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PThe rehabilitation training\x01",
            "is over and yet what have\x01",
            "you come to do here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FEhhm, actually...\x02",
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
    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xB,
        (
            "#5PMedical questionnaire...ah!\x01",
            "I had completely forgotten!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x1)

    ChrTalk(
        0xB,
        (
            "#5PWait a moment, I'm sure\x01",
            "it should be here...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xB,
        "#5PHere, it's this, right?\x02",
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
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x32F, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#12P#00000FYes, it truly is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PMan, sorry.\x01",
            "You came all the way here\x01",
            "on purpose to get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PI'm so happy recently that\x01",
            "I had completely forgotten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FHappy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PRight, I mean that Stella\x01",
            "and I are all lovey dovey and──\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#6P#00304FAlright, Lloyd,\x01",
            "time to go, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FWell, our purpose is done.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00012F...R-Right.\x01",
            "(Seems it would take long...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PH-Hey, HEY!?\x01",
            "Aren't you going to listen to me...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FAhaha...sorry.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x152, 6)
    OP_29(0x70, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E02")

    AnonymousTalk(
        0x101,
        (
            "#00003FNow we have finished to collect\x01",
            "all the medical questionnaires.\x02\x03",
            "#00000FLet's go deliver them to\x01",
            "Professor Seiland at once.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x70, 0x1, 0x5)

    label("loc_7E02")

    SetChrPos(0xB, -97470, 150, -3950, 270)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -94400, 0, -3950, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_787E end

    def Function_28_7E35(): pass

    label("Function_28_7E35")

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
            "My, Randy and everyone from...\x01",
            "The Support Section, I guess?\x02",
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
            "#00000FUhhm, today we\x01",
            "came for work...\x02",
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
        0xA,
        (
            "Ah, now that you mention it...\x01",
            "I heard about that, I think.\x02",
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
            "#10105FEeh, this unit has\x01",
            "something like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FThen, please.\x02",
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
            "Lloyd and the others ate the Satiating Hot Pot.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00100F*munch munch*...\x01",
            "Yes, my body has warmed up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FYeah, the quantity of meat is amazing\x01",
            "and there're a lot of edible wild\x01",
            "plants too. It's highly nourishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FWell, the CGF practice is hard,\x01",
            "so if they didn't get strength from\x01",
            "something like this, they wouldn't last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We often do hot pot parties and\x01",
            "they really turn into meat contests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At the time Randy was here, he was \x01",
            "snatching away from the small servings\x01",
            "others took and he was doing a mess.\x02",
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
            "were doing, Mr. Randy?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x104,
        "#00309FHa ha, "survival of the fittest", you know?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x173, 2)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_847F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_847F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_849C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_849C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_84AF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_84C2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_84DF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_84F2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_850F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_850F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_8522")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_853F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_853F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_8552")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_856F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_856F")

    OP_29(0x80, 0x1, 0xB)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8697")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_868E")

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

    label("loc_868E")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_8697")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_877B")
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

    label("loc_877B")

    OP_4C(0xA, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -103610, 0, 2100, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_7E35 end

    def Function_29_87AB(): pass

    label("Function_29_87AB")

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

    def lambda_8889():
        OP_95(0x101, 21060, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8889)
    Sleep(30)

    def lambda_88A6():
        OP_95(0x102, 21260, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_88A6)
    Sleep(40)

    def lambda_88C3():
        OP_95(0x104, 21260, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_88C3)
    Sleep(800)

    def lambda_88E0():
        OP_95(0x109, 23560, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_88E0)
    Sleep(30)

    def lambda_88FD():
        OP_95(0x103, 23360, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_88FD)
    Sleep(10)

    def lambda_891A():
        OP_95(0x105, 23360, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_891A)
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
            "#00001FWell then, the black truck in case\x01",
            "should be here, but...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_END)), "loc_8A73")

    ChrTalk(
        0x103,
        (
            "#00203F...According to Mr. Franz,\x01",
            "didn't he say that the truck\x01",
            "headed to the Republic region...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FAh...now that you mention it, he did.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FWe unconsciously came\x01",
            "to Bellgard Gate...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B05")

    label("loc_8A73")


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
            "#00100FUhhm, could it be good\x01",
            "asking some of the members?\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FYou're right too...\x02",
    )

    CloseMessageWindow()

    label("loc_8B05")


    def lambda_8B0A():
        OP_95(0xFE, 17460, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8B0A)
    Sleep(2000)
    OP_68(20630, 1000, -340, 3000)
    MoveCamera(306, 19, 0, 3000)
    OP_6E(470, 3000)
    SetCameraDistance(20760, 3000)
    WaitChrThread(0x14, 1)
    OP_6F(0x79)

    ChrTalk(
        0x14,
        "#07900FOh...you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FHi, Mireille.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FGood morning, 2nd Lt. Mireille!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#07902FGood morning.\x02\x03",
            "#07906F...*sigh*.\x01",
            "What is your business here today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FYou somehow look tired.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#07901FYes... Because the state of tension\x01",
            "with the Empire region continues.\x02\x03",
            "#07903FI heard that at such a time there was\x01",
            "some disturbance at Tangram Gate...\x02",
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
        "#00005FWhat's happened at Tangram Gate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#07901FIt seems that an Empire made\x01",
            "black truck went forcefully through\x01",
            "the gate with incomplete documents.\x02\x03",
            "#07903FI think there won't be any problem\x01",
            "since at least a minimum check\x01",
            "was finished, but...\x02\x03",
            "#07901FThe CGF honor is completely\x01",
            "ruined, honestly...!\x02",
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

    def lambda_8F54():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8F54)
    Sleep(10)

    def lambda_8F64():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8F64)
    Sleep(50)

    def lambda_8F74():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8F74)
    Sleep(10)

    def lambda_8F84():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8F84)
    Sleep(30)

    def lambda_8F94():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8F94)
    Sleep(10)

    def lambda_8FA4():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8FA4)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x102,
        "#00101FSay, could that be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F...Yeah, it seems we\x01",
            "ended up looking in\x01",
            "the wrong place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FIt's already run away to the Republic,\x01",
            "so it seems too late to do something...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_END)), "loc_9139")

    ChrTalk(
        0x101,
        (
            "#00001FIt's inexcusable towards Mr.\x01",
            "Billy and St. Ursula Hospital, but...\x01",
            "It seems we can only report that.\x02\x03",
            "#00006F*sigh*... If only we had properly\x01",
            "listened to Franz's story...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91AA")

    label("loc_9139")


    ChrTalk(
        0x101,
        (
            "#00006FIt's inexcusable towards Mr.\x01",
            "Billy and St. Ursula Hospital, but...\x01",
            "It seems we can only report that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91AA")


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
            "Lloyd and the others told the\x01",
            "facts to Billy and Ricardo who \x01",
            "were waiting at the airport...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, they went with\x01",
            "Billy to St. Ursula Hospital \x01",
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

    # Function_29_87AB end

    def Function_30_92A3(): pass

    label("Function_30_92A3")

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
            "#30WThen, more than the\x01",
            "legality of these papers...\x02\x03",
            "There's one and only thing\x01",
            "I want to ask to you all.\x02\x03",
            "This situation, the present\x01",
            "order, how we are...\x01",
            "Are they really "correct"?\x02\x03",
            "It's──just that.\x07\x00\x02",
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

    # Function_30_92A3 end

    def Function_31_9576(): pass

    label("Function_31_9576")

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

    # Function_31_9576 end

    SaveToFile()

Try(main)
