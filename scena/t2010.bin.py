from ScenarioHelper import *

def main():
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
        "Connors",           # 1
        "SIG member",               # 2
        "Stella",                 # 3
        "Crescent squad",             # 4
        "Beyond",               # 5
        "tourist",                 # 6
        "tourist",                 # 7
        "tourist",                 # 8
        "girl",                 # 9
        "tourist",                 # 10
        "tourist",                 # 11
        "Romeo members",             # 12
        "Lieutenant Mireille",           # 13
        "Harold",               # 14
        "Mushroute Scott",         # 15
        "Wrestler Wenzel",     # 16
        "Guided car",                 # 17
        "Sonya Command",           # 18
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
        "Function_9_18FC",         # 09, 9
        "Function_10_229B",        # 0A, 10
        "Function_11_229F",        # 0B, 11
        "Function_12_2FF7",        # 0C, 12
        "Function_13_3C9C",        # 0D, 13
        "Function_14_3CA0",        # 0E, 14
        "Function_15_4B2C",        # 0F, 15
        "Function_16_4DDF",        # 10, 16
        "Function_17_5074",        # 11, 17
        "Function_18_5339",        # 12, 18
        "Function_19_542C",        # 13, 19
        "Function_20_557E",        # 14, 20
        "Function_21_576B",        # 15, 21
        "Function_22_599B",        # 16, 22
        "Function_23_5B3B",        # 17, 23
        "Function_24_6195",        # 18, 24
        "Function_25_6243",        # 19, 25
        "Function_26_63A3",        # 1A, 26
        "Function_27_65D3",        # 1B, 27
        "Function_28_6AFF",        # 1C, 28
        "Function_29_73AB",        # 1D, 29
        "Function_30_7DE7",        # 1E, 30
        "Function_31_80B2",        # 1F, 31
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBC")

    NpcTalk(
        0x8,
        "Soldier Connors",
        (
            "Crossing bridge over the border,\x01",
            "Although it still fell,\x01",
            "The vigilance to the imperial army is strict.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Connors",
        (
            "If they think that they will start an invasion,\x01",
            "Even soon as I fell a bridge\x01",
            "I will repair it.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Connors",
        (
            "Fortunately unfortunate, the empire is in civil war ……\x01",
            "In the meantime we also\x01",
            "You have to keep yourself in shape.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F80")

    label("loc_EBC")


    NpcTalk(
        0x8,
        "Soldier Connors",
        (
            "If the Imperial Army wants to start an invasion,\x01",
            "Even soon as I fell a bridge\x01",
            "I will repair it.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Connors",
        (
            "Fortunately unfortunate, the empire is in civil war ……\x01",
            "In the meantime we also\x01",
            "You have to keep yourself in shape.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F80")

    Jump("loc_18F8")

    label("loc_F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_102F")

    ChrTalk(
        0x8,
        (
            "Given the recent tension,\x01",
            "Foreigners leaving the crossbell also\x01",
            "It seems that it's not a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Not even that,\x01",
            "Because the noisy incident continued … …\x01",
            "Is there any choice?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18F8")

    label("loc_102F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_11D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_112D")

    ChrTalk(
        0x8,
        (
            "昨日、Lieutenant Mireilleの連れた部隊が\x01",
            "I heard that he saw a huge monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To vigilance of the gone escaped,\x01",
            "For a while it is one unit\x01",
            "It seems to patrol within autonomous state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Whew ……\x01",
            "While the state of tension is also continuing\x01",
            "Busyness is increasing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_11CB")

    label("loc_112D")


    ChrTalk(
        0x8,
        (
            "To vigilance of the gone escaped,\x01",
            "For a while it is one unit\x01",
            "It seems to patrol within autonomous state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Whew ……\x01",
            "While the state of tension is also continuing\x01",
            "Busyness is increasing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CB")

    Jump("loc_18F8")

    label("loc_11D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1271")

    ChrTalk(
        0x8,
        (
            "Imperial merchants who passed here earlier,\x01",
            "About cross-bell independence\x01",
            "It seems they were talking a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This topic, even by the Empire\x01",
            "It sounds like a controversy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18F8")

    label("loc_1271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1401")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1371")

    ChrTalk(
        0x8,
        (
            "Recently, inside the empire's fortress\x01",
            "This exercise is something like this\x01",
            "It seems to be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We guards ……\x01",
            "No, in this case to Mayor Dieter\x01",
            "I wonder if you are putting pressure on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just prior to the \"Treaty of the Treaty of November\"\x01",
            "It is cute compared to the state of tension.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_13FC")

    label("loc_1371")


    ChrTalk(
        0x8,
        (
            "Recently, inside the empire's fortress\x01",
            "This sort of exercise\x01",
            "It seems to be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just prior to the \"Treaty of the Treaty of November\"\x01",
            "It is cute compared to the state of tension.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FC")

    Jump("loc_18F8")

    label("loc_1401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_15BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_153F")

    ChrTalk(
        0x8,
        (
            "Because there was information on terrorists,\x01",
            "Make sure to check strictly\x01",
            "I have an order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If today's warning system,\x01",
            "Entry from overland\x01",
            "It should be impossible at first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also,\x01",
            "From special nearby facilities\x01",
            "I keep warning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even a security officer who can not deploy a flying boat,\x01",
            "I have to do as much as I can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_15B5")

    label("loc_153F")


    ChrTalk(
        0x8,
        (
            "The guard, according to the provisions of autonomous state law\x01",
            "The possession of a flying boat is not permitted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For empty security\x01",
            "I definitely want it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B5")

    Jump("loc_18F8")

    label("loc_15BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_17D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_171E")

    ChrTalk(
        0x8,
        (
            "The Osborne Prime Minister, who is at the trade meeting,\x01",
            "It is commonly referred to as \"the iron baseball president\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is because \"stability of the country is iron and blood,\x01",
            "Weapons and military forces \"\x01",
            "It is derived from his creed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Under this word,\x01",
            "He has several autonomous states\x01",
            "I am militarily annexed to the empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For cross-bell autonomous state,\x01",
            "One of the most cautious people\x01",
            "There must be no mistake.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17D0")

    label("loc_171E")


    ChrTalk(
        0x8,
        (
            "Empire has several autonomous states\x01",
            "We have been armed with military force, but to many of them\x01",
            "\"Chancellor of Iron Blood\" is involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For cross-bell autonomous state,\x01",
            "One of the most cautious people\x01",
            "There must be no mistake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D0")

    Jump("loc_18F8")

    label("loc_17D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_18F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188E")

    ChrTalk(
        0x8,
        (
            "After passing through the iron fence there,\x01",
            "Up to the \"Galleria Fortress\" of the Empire\x01",
            "It's in a flash.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please be careful if you plan to go.\x01",
            "Empire checks of immigrants\x01",
            "It's pretty strict.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18F8")

    label("loc_188E")


    ChrTalk(
        0x8,
        (
            "Empire checks of immigrants\x01",
            "It's pretty strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "\"Galleria Fortress\"\x01",
            "Please be careful if you plan to go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18F8")

    TalkEnd(0x8)
    Return()

    # Function_8_D7B end

    def Function_9_18FC(): pass

    label("Function_9_18FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A05")

    NpcTalk(
        0x9,
        "Soldier Sig",
        (
            "An independent invalid declaration was issued,\x01",
            "Defense Secretary is missing ……\x01",
            "I heard that the president was also detained.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Sig",
        (
            "We will continue to be a defense army\x01",
            "I wonder if I can work or not ….\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Sig",
        (
            "…… In such a situation,\x01",
            "No matter how much I think, hesitation will not be sunny.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1A95")

    label("loc_1A05")


    NpcTalk(
        0x9,
        "Soldier Sig",
        (
            "We will continue to be a defense army\x01",
            "I wonder if I can work or not ….\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Sig",
        (
            "…… In such a situation,\x01",
            "No matter how much I think, hesitation will not be sunny.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A95")

    Jump("loc_2297")

    label("loc_1A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B2E")

    ChrTalk(
        0xFE,
        (
            "Ahead, the empire\x01",
            "Whatever you try,\x01",
            "We will never yield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Death of fellows,\x01",
            "Never waste it.\x01",
            "…… Then, what will it be?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2297")

    label("loc_1B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1BD2")

    ChrTalk(
        0xFE,
        (
            "Fuu …\x01",
            "Tired of restoration work last night\x01",
            "It seems to be still there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Under this strained situation\x01",
            "I do not know what will happen,\x01",
            "I suppose I should take a nap during the moment … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2297")

    label("loc_1BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1D62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CCF")

    ChrTalk(
        0xFE,
        (
            "A survey of things that become \"phantom beasts\"\x01",
            "We want to undertake in the guard\x01",
            "Where was that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With independence advocated relationship\x01",
            "With tension going on\x01",
            "It can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "… … I left it, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FOh, too there\x01",
            "Please do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D5D")

    label("loc_1CCF")


    ChrTalk(
        0xFE,
        (
            "A survey of things that become \"phantom beasts\"\x01",
            "We want to undertake in the guard\x01",
            "Where was that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With independence advocated relationship\x01",
            "With tension going on\x01",
            "It can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D5D")

    Jump("loc_2297")

    label("loc_1D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1EAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E1E")

    ChrTalk(
        0xFE,
        (
            "In the meantime, Mireille warrant\x01",
            "I was promoted to three captains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With three lieutenants, in the army of another country\x01",
            "It is a class equivalent to a lieutenant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope your future success\x01",
            "It is a place I want you to expect.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1EA7")

    label("loc_1E1E")


    ChrTalk(
        0xFE,
        (
            "Given her ability,\x01",
            "This promotion is too late … …\x01",
            "Well, it is a happy thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope your future success\x01",
            "It is a place I want you to expect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EA7")

    Jump("loc_2297")

    label("loc_1EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1F22")

    ChrTalk(
        0xFE,
        (
            "There is no response to detectors.\x01",
            "… … There seems to be no dangerous goods on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just to be sure the bottom of the car body\x01",
            "I suppose I should check it … ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2297")

    label("loc_1F22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_20C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2037")

    ChrTalk(
        0xFE,
        (
            "Sonya Commandの指揮する\x01",
            "Security during trade conference,\x01",
            "It is truly reasonable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Personnel with appropriate abilities\x01",
            "By allocating it to the minimum necessary,\x01",
            "I also follow border guards well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is a big difference from the previous command.\x01",
            "After all, what is the person who should stand on a person\x01",
            "There should be some.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_20BD")

    label("loc_2037")


    ChrTalk(
        0xFE,
        (
            "Both of them have proven track record\x01",
            "I am planning to take over the commander … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sonya Commandの目の黒いうちは\x01",
            "I realized that it would be impossible at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20BD")

    Jump("loc_2297")

    label("loc_20C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2297")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E9")

    ChrTalk(
        0xFE,
        (
            "Former commander through Hartmann\x01",
            "Having connection with Joachim,\x01",
            "It was also used during the cult incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He was disciplinedly dismissed,\x01",
            "Sonja deputy command was commanded\x01",
            "It is quite natural.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, the organization called the guard will\x01",
            "It will be operated more properly.\x01",
            "It is a pleasing thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2297")

    label("loc_21E9")


    ChrTalk(
        0xFE,
        (
            "Because of the incompetence of the former commander,\x01",
            "Until now only to Mireille warrantee\x01",
            "It was a burden … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, the organization called the guard will\x01",
            "It will be operated more properly.\x01",
            "It is a pleasing thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2297")

    TalkEnd(0xFE)
    Return()

    # Function_9_18FC end

    def Function_10_229B(): pass

    label("Function_10_229B")

    Call(0, 11)
    Return()

    # Function_10_229B end

    def Function_11_229F(): pass

    label("Function_11_229F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22C8")
    Call(0, 28)
    Return()

    label("loc_22C8")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FF3")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2333")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2333")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2353")
    OP_AF(0x73)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FEE")

    label("loc_2353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2367")
    Jump("loc_2FEE")

    label("loc_2367")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FEE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_241C")

    ChrTalk(
        0xA,
        (
            "Bellegard gate guards of warranties\x01",
            "\"Fried pork pot\" was delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I often do a pot party,\x01",
            "It will be a fight against meat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FEE")

    label("loc_241C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_25A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24FF")

    ChrTalk(
        0xA,
        (
            "Everyone is anxious … …\x01",
            "I'm surely okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because Cres,\x01",
            "You absolutely protect me\x01",
            "He told me what he said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If so, I do what I can do\x01",
            "I have to share my energy with everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_259E")

    label("loc_24FF")


    ChrTalk(
        0xA,
        (
            "Huge trees that do not understand Wake,\x01",
            "It is a rumor of President's detention\x01",
            "Everyone seems uneasy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I do what I can do\x01",
            "I have to share my energy with everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_259E")

    Jump("loc_2FEE")

    label("loc_25A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2713")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_268B")

    ChrTalk(
        0xA,
        (
            "Tension condition with the empire …\x01",
            "Bye bye\x01",
            "I will remember before the conclusion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That empire 's \"train cannon\"\x01",
            "When it turned to this one,\x01",
            "I was really scared … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Also, such a thing\x01",
            "I do not have to happen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_270E")

    label("loc_268B")


    ChrTalk(
        0xA,
        (
            "Before the conclusion of the treaty,\x01",
            "Empire exercises \"train cannon\"\x01",
            "There was something I brought out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Also, such a thing\x01",
            "I do not have to happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_270E")

    Jump("loc_2FEE")

    label("loc_2713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2874")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27EC")

    ChrTalk(
        0xA,
        (
            "Rain of unfortunate today.\x01",
            "Members who are guarding outside do seem hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "On such a day,\x01",
            "You have good food that will warm your body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I gave it to Mr. Cres yesterday.\x01",
            "Application of spicy simmering\x01",
            "I might as well make it in a pot.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_286F")

    label("loc_27EC")


    ChrTalk(
        0xA,
        (
            "On such a rainy day,\x01",
            "You have good food that will warm your body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I gave it to Mr. Cres yesterday.\x01",
            "Application of spicy simmering\x01",
            "I might as well make it in a pot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_286F")

    Jump("loc_2FEE")

    label("loc_2874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_29F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_295B")

    ChrTalk(
        0xA,
        (
            "Recently Mr. Cres was missing out,\x01",
            "To awaken\x01",
            "I cooked a spicy stew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At first, a little bit hard\x01",
            "I thought that I made it too much ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm eating properly,\x01",
            "Huhu, it sounds okay.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_29ED")

    label("loc_295B")


    ChrTalk(
        0xA,
        (
            "Huhu, I'm so glad\x01",
            "When you eat it,\x01",
            "After all I am glad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm getting along with each other,\x01",
            "From now on too often\x01",
            "I am going to cook specially.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29ED")

    Jump("loc_2FEE")

    label("loc_29F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2B5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ACB")

    ChrTalk(
        0xA,
        (
            "Mr. Cres, recently\x01",
            "It looks like I'm out of my mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "OK, here is a trip\x01",
            "Even cooking that makes you feel comfortable\x01",
            "I wonder if I can make one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's still a trial Kalesh,\x01",
            "I have to do this much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2B56")

    label("loc_2ACB")


    ChrTalk(
        0xA,
        (
            "To I cress Mr.\x01",
            "Even cooking that makes you feel comfortable\x01",
            "I wonder if I can make one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's still a trial Kalesh,\x01",
            "I have to do this much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B56")

    Jump("loc_2FEE")

    label("loc_2B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2BF2")

    ChrTalk(
        0xA,
        (
            "Everything, terrorists\x01",
            "Invade the crossbell\x01",
            "There is a possibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even at the gate, alertness is rising,\x01",
            "I wonder if all the members are okay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FEE")

    label("loc_2BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2D86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF4")

    ChrTalk(
        0xA,
        (
            "Try with Cress\x01",
            "It is the first time for me to associate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But, because I'm dating you\x01",
            "Nothing else will come anyway … …\x01",
            "I wonder if it is such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "For men,\x01",
            "The fact itself is \"dating\"\x01",
            "It might be important.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2D81")

    label("loc_2CF4")


    ChrTalk(
        0xA,
        (
            "I have not had much experience either.\x01",
            "I do not quite understand it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "For men,\x01",
            "The fact itself is \"dating\"\x01",
            "It might be important.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D81")

    Jump("loc_2FEE")

    label("loc_2D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2FEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F6C")
    TurnDirection(0xA, 0x104, 0)

    ChrTalk(
        0xA,
        (
            "Oh, come around … ….\x01",
            "It is not Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Rehabilitation training\x01",
            "Was not it over already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FWell, I guess so ….\x01",
            "You cute\x01",
            "I feel like watching at first sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Haha, as usual\x01",
            "I'm just joking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Besides, if you ask me for the present\x01",
            "May Cress get angry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F…… Randy,\x01",
            "A member sitting in a seat\x01",
            "It's awesome ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F…… It certainly looks troublesome.\x01",
            "Let's bear in mind the liver.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2FEE")

    label("loc_2F6C")


    ChrTalk(
        0xA,
        (
            "Huhu, well Well anyway ……\x01",
            "Because it is a point, please eat something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As in rehabilitation training\x01",
            "I'm glad if you eat it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FEE")

    Jump("loc_22D5")

    label("loc_2FF3")

    TalkEnd(0xA)
    Return()

    # Function_11_229F end

    def Function_12_2FF7(): pass

    label("Function_12_2FF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3020")
    Call(0, 27)
    Return()

    label("loc_3020")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_318B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3109")

    NpcTalk(
        0xB,
        "Soldier cres",
        (
            "To be honest,\x01",
            "I do not know what to do.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier cres",
        (
            "But what is important\x01",
            "You have to protect with this hand.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier cres",
        (
            "OK, well …\x01",
            "For the time being I am eating!\x01",
            "I will eat it and power it! It is!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3186")

    label("loc_3109")


    NpcTalk(
        0xB,
        "Soldier cres",
        "You can not fight if your hungry goes down.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier cres",
        (
            "To protect important things ……\x01",
            "I am eating! I will eat it all! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3186")

    Jump("loc_3C98")

    label("loc_318B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3351")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3292")

    ChrTalk(
        0xFE,
        (
            "In the battle in Mainz during this time,\x01",
            "A lot of my friends have been killed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we are powerful tanks too,\x01",
            "The damage may have been suppressed more …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Stellaちゃんや大事な人々を\x01",
            "In order to protect it from now on,\x01",
            "You may need independence after all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_334C")

    label("loc_3292")


    ChrTalk(
        0xFE,
        (
            "If we are powerful tanks too,\x01",
            "The damage in Mainz\x01",
            "It may have been suppressed more …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Stellaちゃんや大事な人々を\x01",
            "In order to protect it from now on,\x01",
            "You may need independence after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_334C")

    Jump("loc_3C98")

    label("loc_3351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_34AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3415")

    ChrTalk(
        0xFE,
        (
            "昨日Stellaちゃんの\x01",
            "After eating spicy simmered,\x01",
            "Somehow my physical condition is good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Juffu\x01",
            "This is love 's power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… That spicy is already overkill.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_34A8")

    label("loc_3415")


    ChrTalk(
        0xFE,
        (
            "昨日Stellaちゃんの\x01",
            "After eating spicy simmered,\x01",
            "Somehow my physical condition is good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must thank her.\x01",
            "…… That spicy is already overkill.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A8")

    Jump("loc_3C98")

    label("loc_34AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_35EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3585")

    ChrTalk(
        0xFE,
        (
            "Ha ha ha ha ha ……\x01",
            "It is hard, spicy, too hot ……! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, no matter my sweet\x01",
            "They made it for me.\x01",
            "Herring with Florida ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "UoOo ~, greasy guy ……! It is!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_35E9")

    label("loc_3585")


    ChrTalk(
        0xFE,
        (
            "Ha ha ha ha ha ……\x01",
            "And, after all, it is painful …! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, I will eat it completely!\x01",
            "Gottatsu guats …! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35E9")

    Jump("loc_3C98")

    label("loc_35EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_36E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3694")

    ChrTalk(
        0xFE,
        (
            "Ha … … with recent tension\x01",
            "I can not get tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… No matter,\x01",
            "Stellaちゃんが見てるんだから\x01",
            "You have to kill it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_36E4")

    label("loc_3694")


    ChrTalk(
        0xFE,
        (
            "Recently I'm tired, but ….\x01",
            "Stellaちゃんが見てるんだ、\x01",
            "You have to kill it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36E4")

    Jump("loc_3C98")

    label("loc_36E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3785")

    ChrTalk(
        0xFE,
        (
            "Today I guard with the bicycle,\x01",
            "Stellaちゃんにいいトコ見せないとな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not know what it is like a terrorist,\x01",
            "You are going to come from anywhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C98")

    label("loc_3785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_389F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3854")

    ChrTalk(
        0xFE,
        (
            "折角Stellaちゃんと\x01",
            "Even though I started dating,\x01",
            "I have not even bought a date.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently in relation to trade meeting\x01",
            "Although I am busy,\x01",
            "In the first place I may not have a sense of being crowded ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_389A")

    label("loc_3854")


    ChrTalk(
        0xFE,
        (
            "Goshiko ~ ….\x01",
            "なんとかStellaちゃんと\x01",
            "I would like to make progress.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_389A")

    Jump("loc_3C98")

    label("loc_389F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3C98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_397D")

    ChrTalk(
        0xB,
        (
            "Hey … … a little\x01",
            "Even if you listen to the story\x01",
            "Is not it nice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Stellaちゃんのことなら、\x01",
            "I wish I could talk for hours!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FWell, senpai.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Listen!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_39BD")

    label("loc_397D")


    ChrTalk(
        0xB,
        (
            "Tiny\x01",
            "Stellaちゃんのことなら、\x01",
            "Even though I could talk for hours, …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39BD")

    Jump("loc_3C98")

    label("loc_39C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3A47")

    ChrTalk(
        0xFE,
        (
            "Randy ……\x01",
            "You, my my sweet … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FWell, calm down.\x01",
            "Do whatever you do from a guy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C98")

    label("loc_3A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BFE")

    ChrTalk(
        0xFE,
        (
            "フフ、Stellaちゃん……\x01",
            "My sweet ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(Well, · Sue ….)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FOh, that's seniors … …\x01",
            "この間からStellaと『お試し』で\x01",
            "I was saying you are going out with me.\x02\x03",
            "#00309FHaha, was it a little progress?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… Well, well.\x01",
            "That's it, I love you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eating meals here every day,\x01",
            "Stellaちゃんを眺めて……\x01",
            "Happy everyday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(…, that is, still\x01",
            "I have not made any progress … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3C98")

    label("loc_3BFE")


    ChrTalk(
        0xFE,
        (
            "ス、Stellaちゃんと俺は\x01",
            "It is coming now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ランディ、Stellaちゃんを\x01",
            "Do not speak from the side.\x01",
            "……please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F(No, it's useless.\x02",
    )

    CloseMessageWindow()

    label("loc_3C98")

    TalkEnd(0xFE)
    Return()

    # Function_12_2FF7 end

    def Function_13_3C9C(): pass

    label("Function_13_3C9C")

    Call(0, 14)
    Return()

    # Function_13_3C9C end

    def Function_14_3CA0(): pass

    label("Function_14_3CA0")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3CAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B28")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",        # 0
            "To take a break\x01",      # 1
            "quit\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D09")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3D09")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D29")
    OP_AF(0x74)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B23")

    label("loc_3D29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D3D")
    Jump("loc_4B23")

    label("loc_3D3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B23")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E1A")

    ChrTalk(
        0xC,
        (
            "In such a case\x01",
            "The load of the mind is particularly troublesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you take a break, take a rest,\x01",
            "You should calm your mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "…… However, I am also anxious.\x01",
            "I wonder if it will come back when it is peaceful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3E98")

    label("loc_3E1A")


    ChrTalk(
        0xC,
        (
            "If you take a break, take a rest,\x01",
            "You should calm your mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "…… However, I am also anxious.\x01",
            "I wonder if it will come back when it is peaceful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E98")

    Jump("loc_4B23")

    label("loc_3E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4070")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FBB")

    ChrTalk(
        0xC,
        (
            "Do whatever you want with Crossbell\x01",
            "The \"red constellation\" which went away somewhere,\x01",
            "He told me he had a flying boat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Moreover, even the anti-aircraft radar of the guard\x01",
            "I heard she did not catch on … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "…… To be honest, with financial strength\x01",
            "It should not be a technique to get it.\x01",
            "Who the hell are they … ….?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_406B")

    label("loc_3FBB")


    ChrTalk(
        0xC,
        (
            "A flying boat of \"red constellation\"\x01",
            "Also on the anti-aircraft radar of the guard\x01",
            "It seems they did not catch on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "…… To be honest, with financial strength\x01",
            "It should not be a technique to get it.\x01",
            "Who the hell are they … ….?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_406B")

    Jump("loc_4B23")

    label("loc_4070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4266")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41A3")

    ChrTalk(
        0xC,
        (
            "I heard about the accident yesterday,\x01",
            "Because of the huge creatures punching hard\x01",
            "It is said that a train accident happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That train is famous for weapon development\x01",
            "It is made by Empire Linefault.\x01",
            "There should be strength of the armored car … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I have not seen the figure directly,\x01",
            "I wonder how frightening it is\x01",
            "Somehow I do not understand.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4261")

    label("loc_41A3")


    ChrTalk(
        0xC,
        (
            "That train is famous for weapon development\x01",
            "Although it is made by Imperial Rheinfault,\x01",
            "Punching to make a train accident ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I have not seen the figure directly,\x01",
            "I wonder how frightening it is\x01",
            "Somehow I do not understand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4261")

    Jump("loc_4B23")

    label("loc_4266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4483")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43DD")

    ChrTalk(
        0xC,
        (
            "As the military of each country is becoming capitalized\x01",
            "In recent years, emphasis has been placed on air tactics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For example, in \"hundred day campaign\" 12 years ago,\x01",
            "With the overwhelming military power of the empire\x01",
            "I was invading Libert … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "At the end of the war, Libert\x01",
            "With the newly developed flying boat,\x01",
            "The battle station was overturned at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The reason why the guard does not allow the possession of a flying boat is that,\x01",
            "I guess there are circumstances around that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_447E")

    label("loc_43DD")


    ChrTalk(
        0xC,
        (
            "近年、As the military of each country is becoming capitalized\x01",
            "Air tactics have been regarded as important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Foreign guardian\x01",
            "When you become an army, by all means\x01",
            "I want you to deploy a flying boat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_447E")

    Jump("loc_4B23")

    label("loc_4483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_463C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4587")

    ChrTalk(
        0xC,
        (
            "Once the crossbell is independent,\x01",
            "The guard officially also as an army\x01",
            "It will be operated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Armor of the members are also more than ever\x01",
            "It will turn into a powerful one.\x01",
            "You have been deploying tanks as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, as a military geek\x01",
            "Do not be intrigued.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4637")

    label("loc_4587")


    ChrTalk(
        0xC,
        (
            "Crossbell is independent\x01",
            "If the guard officially becomes an army,\x01",
            "Equipment will also be more fulfilling now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even tanks are deployed … …\x01",
            "Well, as a military geek\x01",
            "Do not be intrigued.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4637")

    Jump("loc_4B23")

    label("loc_463C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_479E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4723")

    ChrTalk(
        0xC,
        (
            "Today is finally over,\x01",
            "It's a plenary session at the Orkis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Because of consideration to the empire and the republic,\x01",
            "The guards are outstanding guards\x01",
            "I do not think I can do it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It is an important international conference, even from under the edge\x01",
            "I want you to keep protecting somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4799")

    label("loc_4723")


    ChrTalk(
        0xC,
        (
            "Today is finally over,\x01",
            "It's a plenary session at the Orkis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It is an important international conference, even from under the edge\x01",
            "I want you to keep protecting somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4799")

    Jump("loc_4B23")

    label("loc_479E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_496D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48D3")

    ChrTalk(
        0xC,
        (
            "A new type armored car is officially deployed\x01",
            "It will be awhile … …\x01",
            "No, it is still nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "There is also a powerful missile pod,\x01",
            "Armor is also considerably strengthened.\x01",
            "It is no doubt that the guard is the best armed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Compared to other flying boats and tanks\x01",
            "Although it does not look worse,\x01",
            "I think there are things like functional beauty.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4968")

    label("loc_48D3")


    ChrTalk(
        0xC,
        (
            "A new type armored car, no doubt\x01",
            "It is the best army in the guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Compared to other flying boats and tanks\x01",
            "Although it does not look worse,\x01",
            "I think there are things like functional beauty.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4968")

    Jump("loc_4B23")

    label("loc_496D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4B23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A73")

    ChrTalk(
        0xC,
        (
            "I am a military gee ……\x01",
            "In short, it is Mirita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I love military affairs,\x01",
            "Working at this gate also\x01",
            "It is a feeling that my hobby is growing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, the Crossbell Guard\x01",
            "Strictly speaking, it is not an army … …\x01",
            "It's attractive enough for me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4B23")

    label("loc_4A73")


    ChrTalk(
        0xC,
        (
            "I am a fellow of Miriota.\x01",
            "Working at this gate also\x01",
            "It is a feeling that my hobby is growing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, the Crossbell Guard\x01",
            "Strictly speaking, it is not an army … …\x01",
            "It's attractive enough for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B23")

    Jump("loc_3CAD")

    label("loc_4B28")

    TalkEnd(0xC)
    Return()

    # Function_14_3CA0 end

    def Function_15_4B2C(): pass

    label("Function_15_4B2C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4B3D")
    Jump("loc_4DDB")

    label("loc_4B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4C4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BED")

    ChrTalk(
        0xFE,
        (
            "To yesterday's train accident\x01",
            "I was involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once it was done with minor injuries\x01",
            "Daughter had me pick you up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, when are you ……\x01",
            "It still hurts a little.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4C49")

    label("loc_4BED")


    ChrTalk(
        0xFE,
        (
            "Oh, when are you ……\x01",
            "It still hurts a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you let me in a little more hospital\x01",
            "It was good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C49")

    Jump("loc_4DDB")

    label("loc_4C4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4CDF")

    ChrTalk(
        0xFE,
        (
            "Crossbell will try to become independent … …\x01",
            "You should know the condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the Imperium,\x01",
            "It seems like a hand biting by a dog\x01",
            "It is a thought.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DDB")

    label("loc_4CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4CED")
    Jump("loc_4DDB")

    label("loc_4CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4D56")

    ChrTalk(
        0xFE,
        "The examination can not be completed quickly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is countermeasures against terrorism\x01",
            "It is troublesome.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DDB")

    label("loc_4D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4D64")
    Jump("loc_4DDB")

    label("loc_4D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4DDB")

    ChrTalk(
        0xFE,
        (
            "At the trade meeting, His Excellency\x01",
            "I'm sure we will have a useful arrangement for the Empire\x01",
            "I'm sure he will let you through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Huh, that's fine.\x02",
    )

    CloseMessageWindow()

    label("loc_4DDB")

    TalkEnd(0xFE)
    Return()

    # Function_15_4B2C end

    def Function_16_4DDF(): pass

    label("Function_16_4DDF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4E7A")

    ChrTalk(
        0xFE,
        (
            "I have hesitated since that raid incident … …\x01",
            "I decided to return home to my empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To such a thing, if it gets involved again\x01",
            "I do not want to get it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5070")

    label("loc_4E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4E88")
    Jump("loc_5070")

    label("loc_4E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4E96")
    Jump("loc_5070")

    label("loc_4E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4F0E")

    ChrTalk(
        0xFE,
        (
            "It is national independence,\x01",
            "Do not miss the illusion as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell for the Empire\x01",
            "I only need to be exploited.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5070")

    label("loc_4F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F1C")
    Jump("loc_5070")

    label("loc_4F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4FBD")

    ChrTalk(
        0xFE,
        (
            "Welcome, come quickly to see it\x01",
            "It will not be as good as anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the Orkis Tower\x01",
            "Because it was also talked about in the empire,\x01",
            "I also wanted to see it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5070")

    label("loc_4FBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5070")

    ChrTalk(
        0xFE,
        (
            "At the trade meeting, as the emperor's name\x01",
            "Topic Oliver's Prince\x01",
            "I'm talking about entering the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, as Emperor Majesty\x01",
            "I am of assistance for \"Chairman of Iron Blood\"\x01",
            "I guess it's appointed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5070")

    TalkEnd(0xFE)
    Return()

    # Function_16_4DDF end

    def Function_17_5074(): pass

    label("Function_17_5074")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_51FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_516D")

    ChrTalk(
        0xF,
        (
            "There is a civil war in the empire,\x01",
            "Still want to return to the motherland\x01",
            "It is where I came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "But the bridge is like that\x01",
            "I was totally dropped\x01",
            "I did not feel well …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "…… How can I do now?\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_51F6")

    label("loc_516D")


    ChrTalk(
        0xF,
        (
            "Your father \"From the balcony\x01",
            "I will see the fallen bridge from above \"\x01",
            "I went up the stairs, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "…… After all the empire\x01",
            "I wonder if I can not return.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51F6")

    Jump("loc_5335")

    label("loc_51FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5209")
    Jump("loc_5335")

    label("loc_5209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5217")
    Jump("loc_5335")

    label("loc_5217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_529B")

    ChrTalk(
        0xFE,
        (
            "Somehow, the guard people\x01",
            "Everyone is pretty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not want to stay long like this,\x01",
            "I'm going home quickly ~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5335")

    label("loc_529B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_52A9")
    Jump("loc_5335")

    label("loc_52A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_52B7")
    Jump("loc_5335")

    label("loc_52B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_532C")

    ChrTalk(
        0xFE,
        (
            "Rumored skyscraper,\x01",
            "Lace with the Orchis Tower\x01",
            "I came to see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what kind of building it is.\x01",
            "It will not be fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5335")

    label("loc_532C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5335")

    label("loc_5335")

    TalkEnd(0xFE)
    Return()

    # Function_17_5074 end

    def Function_18_5339(): pass

    label("Function_18_5339")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_53B0")

    ChrTalk(
        0xFE,
        (
            "A little more crossbell\x01",
            "I wanted to play but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently, it is somewhat cowardly.\x01",
            "It can not be helped …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5428")

    label("loc_53B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_53BE")
    Jump("loc_5428")

    label("loc_53BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_53CC")
    Jump("loc_5428")

    label("loc_53CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_53DA")
    Jump("loc_5428")

    label("loc_53DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5411")

    ChrTalk(
        0xFE,
        (
            "Ah,\x01",
            "I would like to go to the city as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5428")

    label("loc_5411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_541F")
    Jump("loc_5428")

    label("loc_541F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5428")

    label("loc_5428")

    TalkEnd(0xFE)
    Return()

    # Function_18_5339 end

    def Function_19_542C(): pass

    label("Function_19_542C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_543D")
    Jump("loc_557A")

    label("loc_543D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_54CF")

    ChrTalk(
        0xFE,
        (
            "Oh, it will rain ……\x01",
            "I wonder if I should have used the railroad after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is right after the accident,\x01",
            "I did not want to use it much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_557A")

    label("loc_54CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_54DD")
    Jump("loc_557A")

    label("loc_54DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_54EB")
    Jump("loc_557A")

    label("loc_54EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_54F9")
    Jump("loc_557A")

    label("loc_54F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5571")

    ChrTalk(
        0xFE,
        (
            "Traffic regulation this morning\x01",
            "The railroad was not available.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that special train\x01",
            "It can not be helped though because it passes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_557A")

    label("loc_5571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_557A")

    label("loc_557A")

    TalkEnd(0xFE)
    Return()

    # Function_19_542C end

    def Function_20_557E(): pass

    label("Function_20_557E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_568E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_562C")

    ChrTalk(
        0xFE,
        (
            "We are now transporting goods\x01",
            "I just came back … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even at Crossbell Station\x01",
            "It seems that the confusion is still continuing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This situation is unavoidable in this situation.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5689")

    label("loc_562C")


    ChrTalk(
        0xFE,
        (
            "Even at Crossbell Station\x01",
            "It seems that the confusion is still continuing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This situation is unavoidable in this situation.\x02",
    )

    CloseMessageWindow()

    label("loc_5689")

    Jump("loc_5767")

    label("loc_568E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5767")

    ChrTalk(
        0x13,
        (
            "In the basement of the gate is a railroad\x01",
            "The cargo line is passing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Now, after the inspection of the freight train is over,\x01",
            "I came back from Crossbell station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "…… Are you planning to get down to the basement?\x01",
            "I do not think there is any big monkey\x01",
            "Take care of the train.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5767")

    TalkEnd(0xFE)
    Return()

    # Function_20_557E end

    def Function_21_576B(): pass

    label("Function_21_576B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5964")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58CE")

    ChrTalk(
        0x104,
        (
            "#00301FMireille ……\x01",
            "It looks pretty busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#07901FYeah, on the Empire's Galleria Fortress\x01",
            "It seems there is some movement.\x02\x03",
            "#07903FTo be honest, it's nervous.\x01",
            "…… Before concluding a non-war treaty two years ago\x01",
            "It is comparable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FTo that extent ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F… … Be careful, Mireille.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#07902F…… Yeah, I know.\x01",
            "Please leave it here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_595F")

    label("loc_58CE")


    ChrTalk(
        0x14,
        (
            "#07903FAt the Galleria Fort of the Empire\x01",
            "There seems to be some movement.\x02\x03",
            "#07901FTo be honest, it's nervous.\x01",
            "…… Before concluding a non-war treaty two years ago\x01",
            "It is comparable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_595F")

    Jump("loc_5997")

    label("loc_5964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5972")
    Jump("loc_5997")

    label("loc_5972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5980")
    Jump("loc_5997")

    label("loc_5980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_598E")
    Jump("loc_5997")

    label("loc_598E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5997")

    label("loc_5997")

    TalkEnd(0xFE)
    Return()

    # Function_21_576B end

    def Function_22_599B(): pass

    label("Function_22_599B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5A27")

    ChrTalk(
        0xFE,
        (
            "In a week from the incident,\x01",
            "I wonder that this situation will get worse\x01",
            "I did not expect it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With my daughter as soon as possible\x01",
            "I have to leave the crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B37")

    label("loc_5A27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5A7A")

    ChrTalk(
        0xFE,
        "Dad, are you OK?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A bit in the cafeteria\x01",
            "Shall I take a break?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B37")

    label("loc_5A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5A88")
    Jump("loc_5B37")

    label("loc_5A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5B12")

    ChrTalk(
        0xFE,
        (
            "Anything, recently incomprehensible\x01",
            "It seems that demons are on the increase.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something is wrong …\x01",
            "Let's go back to the empire quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B37")

    label("loc_5B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5B20")
    Jump("loc_5B37")

    label("loc_5B20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5B2E")
    Jump("loc_5B37")

    label("loc_5B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5B37")

    label("loc_5B37")

    TalkEnd(0xFE)
    Return()

    # Function_22_599B end

    def Function_23_5B3B(): pass

    label("Function_23_5B3B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_601C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5D1B")

    ChrTalk(
        0x15,
        (
            "#03600FYesterday's incident in Almorika ……\x01",
            "I'm glad that I was able to solve it.\x02\x03",
            "#03603FIf you did not have it\x01",
            "What was going on ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FVice broker MINNESS ……\x01",
            "It was a tough man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FOnce, it was wanted and arranged\x01",
            "It is a matter of time to be caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, how about you?\x01",
            "A quite persistent face\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FCertainly, until you catch Hun\x01",
            "I heard that you can not rest assured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03608FI agree……\x01",
            "By then, another damage\x01",
            "I hope it does not go out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6014")

    label("loc_5D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_END)), "loc_5F05")

    ChrTalk(
        0x15,
        (
            "#03605FAw, everyone ….\x02\x03",
            "#03600FOh yeah, in an example Almorika village\x01",
            "It's a case of Minnes … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F… …. from the investigation on the way\x01",
            "I'm sorry I missed it.\x02\x03",
            "#00008FOther high priority work\x01",
            "Entering ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03600FNo no, it's unexpected.\x01",
            "In cooperation with Professor Ian\x01",
            "I managed to solve it … …\x02\x03",
            "#03604FAlso investigate yours until then\x01",
            "It was helpful enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIs that so …?\x01",
            "That was good.\x02\x03",
            "#00003F(After all, until the end\x01",
            "I should have done it. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6014")

    label("loc_5F05")


    ChrTalk(
        0x15,
        (
            "#03600FBecause the village chiefs have the honor\x01",
            "I can not say details, but ….\x02\x03",
            "#03603FYesterday in Almorika village\x01",
            "There was a serious incident.\x02\x03",
            "#03600FWithout Professor Ian,\x01",
            "To solve that incident\x01",
            "You did not have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(It sounds like a serious incident … …\x01",
            "I wish I could have helped something. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6014")

    SetScenarioFlags(0x17C, 1)
    Jump("loc_6191")

    label("loc_601C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6103")

    ChrTalk(
        0x15,
        (
            "#03600FToday we cross the West Crossbell Highway\x01",
            "I have been driving … ….\x02\x03",
            "#03603FWhen I think that it is the day after the derailment accident\x01",
            "I will be a little worried.\x02\x03",
            "#03600FA huge compound has come out\x01",
            "Rumors are also flowing,\x01",
            "You may as well be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_6191")

    label("loc_6103")


    ChrTalk(
        0x15,
        (
            "#03600FToday we cross the West Crossbell Highway\x01",
            "I have been driving … ….\x02\x03",
            "A huge compound has come out\x01",
            "Rumors are also flowing,\x01",
            "You may as well be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6191")

    TalkEnd(0xFE)
    Return()

    # Function_23_5B3B end

    def Function_24_6195(): pass

    label("Function_24_6195")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61AA")
    Call(0, 25)
    Jump("loc_623F")

    label("loc_61AA")


    ChrTalk(
        0xFE,
        (
            "Tension of this border ……\x01",
            "I hope nothing happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, for the safety of civilians\x01",
            "Even our guild people\x01",
            "I have to check the situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_623F")

    TalkEnd(0xFE)
    Return()

    # Function_24_6195 end

    def Function_25_6243(): pass

    label("Function_25_6243")

    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x17, 0x10)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)

    ChrTalk(
        0x16,
        (
            "…… Indeed, the border is\x01",
            "It seems to be in a state not to be plugged in and out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "At such times, both the guild of the empire\x01",
            "I hope we can cooperate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "…… The guild of the empire,\x01",
            "It fades with the pressure of the military.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "There are some people with bones … …\x01",
            "Now that the organization itself is such a situation,\x01",
            "I will not be able to rely too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "That's right … that can not be helped.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x16, 0x10)
    ClearChrFlags(0x17, 0x10)
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1, 4)
    Return()

    # Function_25_6243 end

    def Function_26_63A3(): pass

    label("Function_26_63A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6478")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63C1")
    Call(0, 25)
    Jump("loc_6473")

    label("loc_63C1")


    ChrTalk(
        0xFE,
        (
            "If you can cooperate with the guild of the empire,\x01",
            "From this neutral standpoint this tension state\x01",
            "Although it may have been relaxed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… The guild of the empire,\x01",
            "It fades with the pressure of the military.\x01",
            "I do not think I can do much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6473")

    Jump("loc_65CF")

    label("loc_6478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6551")

    ChrTalk(
        0xFE,
        (
            "Today is different from Scott.\x01",
            "I had exterminated the maid beasts in the vicinity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As soon as the Trade Council is started,\x01",
            "It will be quite busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before that, I requested at least one request\x01",
            "I have to do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_65CF")

    label("loc_6551")


    ChrTalk(
        0xFE,
        (
            "As soon as the Trade Council is started,\x01",
            "It will be quite busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before that, I requested at least one request\x01",
            "I have to do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65CF")

    TalkEnd(0xFE)
    Return()

    # Function_26_63A3 end

    def Function_27_65D3(): pass

    label("Function_27_65D3")

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
        "#12P#00309FWell, Cress senpai.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PHappy …… Randy! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PRehabilitation training\x01",
            "Even though it is over,\x01",
            "What are you doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FEr, actually …\x02",
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
    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xB,
        (
            "#5PInquiry chart … …. Ah!\x01",
            "I completely forgotten!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x1)

    ChrTalk(
        0xB,
        (
            "#5PWait a moment,\x01",
            "Certainly here ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xB,
        "#5PHuh, is not this?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '库雷斯队员的问诊表'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('库雷斯队员的问诊表', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#12P#00000FYes, indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PNo, it's bad.\x01",
            "Come to pick it up.\x01",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PI am too happy recently,\x01",
            "I completely forgotten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FHappiness ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PYes, that is, with me\x01",
            "Stellaちゃんのラブラブな──\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#6P#00304FAlright Lloyd,\x01",
            "I suppose I should go soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FWell, the purpose has also been done.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00012F…, it is.\x01",
            "(It is going to be long … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PHey, cola! Is it?\x01",
            "Do not you ask me … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FHaha … I'm sorry.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x152, 6)
    OP_29(0x70, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6ACC")

    AnonymousTalk(
        0x101,
        (
            "#00003FWith this, all the questionnaire charts\x01",
            "I finished collecting it.\x02\x03",
            "#00000FImmediately to Professor Seyland\x01",
            "Let's suppose that we will go reporting.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x70, 0x1, 0x5)

    label("loc_6ACC")

    SetChrPos(0xB, -97470, 150, -3950, 270)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -94400, 0, -3950, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_65D3 end

    def Function_28_6AFF(): pass

    label("Function_28_6AFF")

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
            "Oh, to Randy … …\x01",
            "I wonder if you were in the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309Fよっ、Stella。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, today I am at work\x01",
            "I came ….\x02",
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
        0xA,
        (
            "Oh, by the way, …\x01",
            "Even such a story came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well then, then\x01",
            "Bellegard gate guards of warranties\x01",
            "Do you even make \"a full-baked pozzer\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FOh, in our troops\x01",
            "There was such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FWell, then, I'm looking forward to working with you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yeah, let's count on the number of people\x01",
            "Wait a moment.\x02",
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
            "Lloyd 's ate a full grunge.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00100FMunching …\x01",
            "No, my body is getting warmer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FOh, the volume of meat is amazing,\x01",
            "A lot of wild vegetables are also included and it is full of nutrition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FWell, the guard is also hard exercises,\x01",
            "With this we need to work hard\x01",
            "I do not have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I often do a pot party,\x01",
            "It will be a fight against meat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When Randy was there something,\x01",
            "I take away from the dish taken by others\x01",
            "I was doing it messed up.\x02",
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
            "#00211F…… What are you doing?\x01",
            "Randy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x104,
        "#00309FHaha, you mean a weak meal?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x173, 2)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_70B7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_70D4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_70E7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_70FA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_7117")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_712A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_712A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_7147")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_715A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_715A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_7177")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7177")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_718A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_718A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_71A7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_71A7")

    OP_29(0x80, 0x1, 0xB)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72AA")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_72A1")

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

    label("loc_72A1")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_72AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_737B")
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

    label("loc_737B")

    OP_4C(0xA, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -103610, 0, 2100, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_6AFF end

    def Function_29_73AB(): pass

    label("Function_29_73AB")

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

    def lambda_7489():
        OP_95(0x101, 21060, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7489)
    Sleep(30)

    def lambda_74A6():
        OP_95(0x102, 21260, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_74A6)
    Sleep(40)

    def lambda_74C3():
        OP_95(0x104, 21260, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_74C3)
    Sleep(800)

    def lambda_74E0():
        OP_95(0x109, 23560, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_74E0)
    Sleep(30)

    def lambda_74FD():
        OP_95(0x103, 23360, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_74FD)
    Sleep(10)

    def lambda_751A():
        OP_95(0x105, 23360, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_751A)
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
            "#00001FWell, the black carrying cars\x01",
            "I guess you're supposed to be here …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_END)), "loc_765D")

    ChrTalk(
        0x103,
        (
            "#00203F…… Franz says,\x01",
            "Trucks towards the Republic\x01",
            "In the story that I headed …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FOh … that's what I said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FToward the Belgard gate\x01",
            "I have come …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76F5")

    label("loc_765D")


    ChrTalk(
        0x103,
        (
            "#00205F…… The car that seems like it\x01",
            "I have not found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWell,\x01",
            "If you ask someone of the crew members\x01",
            "I wonder if it is ok.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FThat's right……\x02",
    )

    CloseMessageWindow()

    label("loc_76F5")


    def lambda_76FA():
        OP_95(0xFE, 17460, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_76FA)
    Sleep(2000)
    OP_68(20630, 1000, -340, 3000)
    MoveCamera(306, 19, 0, 3000)
    OP_6E(470, 3000)
    SetCameraDistance(20760, 3000)
    WaitChrThread(0x14, 1)
    OP_6F(0x79)

    ChrTalk(
        0x14,
        "#07900FOh … you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FWell, Mireille.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100Fお疲れ様です、Lieutenant Mireille！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#07902FIs cheers for good work.\x02\x03",
            "#07906F… ….\x01",
            "What did you come for today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FI guess I'm getting tired somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#07901FYeah … to the direction of the empire\x01",
            "Because the state of tension is continuing.\x02\x03",
            "#07903FAt times like this, at the Tangram gate\x01",
            "It was said that there was a big noise … …\x02",
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
        "#00005FDid something happen at the Tangram gate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#07901FEverything an empire made black carrying car,\x01",
            "Forcibly with poor documentation\x01",
            "It seems they passed through the gate.\x02\x03",
            "#07903FOnce, the minimum check\x01",
            "Because I'm finished I have problems\x01",
            "I do not think so ….\x02\x03",
            "#07901FThe face of the guard gets rolled,\x01",
            "Absolutely …!\x02",
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
        "#07900F……What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FNo……\x02",
    )

    CloseMessageWindow()

    def lambda_7AF9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7AF9)
    Sleep(10)

    def lambda_7B09():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7B09)
    Sleep(50)

    def lambda_7B19():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7B19)
    Sleep(10)

    def lambda_7B29():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7B29)
    Sleep(30)

    def lambda_7B39():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7B39)
    Sleep(10)

    def lambda_7B49():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7B49)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x102,
        "#00101FHey, what are you talking about now …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F…… Oh, apparently we are\x01",
            "Wrong one\x01",
            "He seems to have searched.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FYou already fled to the Republic.\x01",
            "I do not seem to get out of hands anymore …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_END)), "loc_7CBC")

    ChrTalk(
        0x101,
        (
            "#00001FBilly or Ursula hospital\x01",
            "I'm sorry but ….\x01",
            "That seems to only report so.\x02\x03",
            "#00006FHaa …… Franz's story\x01",
            "Should I have listened properly?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D17")

    label("loc_7CBC")


    ChrTalk(
        0x101,
        (
            "#00006FBilly or Ursula hospital\x01",
            "I'm sorry but ….\x01",
            "That seems to only report so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D17")


    ChrTalk(
        0x14,
        "#07900FIs it? Is it? Is it?\x02",
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
            "Lloyd's told the story of things\x01",
            "Wait at Crossbell Airport\x01",
            "Tell Billy and Ricardo …\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, with Billy\x01",
            "Circumstances to Ursula Hospital\x01",
            "It was going to tell.\x02",
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

    # Function_29_73AB end

    def Function_30_7DE7(): pass

    label("Function_30_7DE7")

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
    SetChrName("McDowell")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WAnd, of such procedures\x01",
            "More than anything but legitimacy ……\x02\x03",
            "I would like to ask everyone\x01",
            "There is no other.\x02\x03",
            "Indeed this situation,\x01",
            "The current system, our way is,\x01",
            "Is it \"right\"?\x02\x03",
            "Just - that's it.\x07\x00\x02",
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

    # Function_30_7DE7 end

    def Function_31_80B2(): pass

    label("Function_31_80B2")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "In the meantime, the cargo line dedicated to the guard\x01",
            "Staff only\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_31_80B2 end

    SaveToFile()

Try(main)
