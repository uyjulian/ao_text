from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1530.bin",                # FileName
        "t1530",                    # MapName
        "t1530",                    # Location
        0x004F,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 79, 0, 4, 0, 5],
    )

    BuildStringList((
        "t1530",                  # 0
        "Receptionist Serra",             # 1
        "Clark Secretary General",         # 2
        "Nurse Run",             # 3
        "Professor Lago",             # 4
        "Trainee Litton",         # 5
        "Trainee Nguyen",           # 6
        "Professor Gary",           # 7
        "Director Ashra",         # 8
        "Trainer Sharuru",       # 9
        "Outpatient",               # 10
        "Outpatient",               # 11
        "Outpatient",               # 12
        "Outpatient",               # 13
        "Outpatient",               # 14
        "Outpatient",               # 15
        "Outpatient",               # 16
        "Outpatient",               # 17
        "patient",                   # 18
        "patient",                   # 19
        "patient",                   # 20
        "Nurse Ada",           # 21
        "Professor Seyland",         # 22
        "Security guard Tony",           # 23
        "Quinn old man",           # 24
        "Amisa",                 # 25
        "Arios",               # 26
        "Prince Albert",         # 27
        "Billy",                 # 28
        "patient",                   # 29
        "Friend Aolia",         # 30
        "Cecil",                 # 31
        "Female",                   # 32
    ))

    AddCharChip((
        "chr/ch28200.itc",                   # 00
        "chr/ch28000.itc",                   # 01
        "chr/ch29700.itc",                   # 02
        "chr/ch29202.itc",                   # 03
        "chr/ch29200.itc",                   # 04
        "chr/ch29402.itc",                   # 05
        "chr/ch29400.itc",                   # 06
        "chr/ch29500.itc",                   # 07
        "chr/ch32702.itc",                   # 08
        "chr/ch32700.itc",                   # 09
        "chr/ch32900.itc",                   # 0A
        "chr/ch32800.itc",                   # 0B
        "chr/ch20002.itc",                   # 0C
        "chr/ch23302.itc",                   # 0D
        "chr/ch21002.itc",                   # 0E
        "chr/ch21000.itc",                   # 0F
        "chr/ch20302.itc",                   # 10
        "chr/ch20402.itc",                   # 11
        "chr/ch44202.itc",                   # 12
        "chr/ch23002.itc",                   # 13
        "chr/ch23000.itc",                   # 14
        "chr/ch24702.itc",                   # 15
        "apl/ch50132.itc",                   # 16
        "apl/ch50138.itc",                   # 17
        "apl/ch50140.itc",                   # 18
        "chr/ch29800.itc",                   # 19
        "chr/ch44800.itc",                   # 1A
        "chr/ch28600.itc",                   # 1B
        "chr/ch24000.itc",                   # 1C
        "chr/ch21502.itc",                   # 1D
        "chr/ch21500.itc",                   # 1E
        "chr/ch02400.itc",                   # 1F
        "chr/ch11800.itc",                   # 20
        "chr/ch20402.itc",                   # 21
        "apl/ch51277.itc",                   # 22
        "chr/ch23600.itc",                   # 23
        "chr/ch44802.itc",                   # 24
        "chr/ch32100.itc",                   # 25
        "apl/ch51278.itc",                   # 26
    ))

    DeclNpc(17209,   0,       7429,    266,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(19739,   0,       4889,    180,  261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(10539,   0,       4294962807, 325,  261,  0x0, 0,   2,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(50979,   119,     59069,   300,  261,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(53970,   0,       51840,   135,  261,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(58849,   0,       58389,   0,    261,  0x0, 0,   7,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(49930,   119,     4294907956, 260,  261,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(56430,   0,       4294912026, 90,   261,  0x0, 0,   10,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(60270,   0,       4294910366, 90,   261,  0x0, 0,   11,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   12,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   13,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   15,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   16,  0,   255, 255, 0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   17,  0,   255, 255, 0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   18,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   20,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   21,  0,   255, 255, 0,   28,  255,  0)
    DeclNpc(59209,   699,     59900,   0,    469,  0x0, 0,   22,  0,   255, 255, 0,   29,  255,  0)
    DeclNpc(59209,   699,     54900,   0,    469,  0x0, 0,   23,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(56889,   800,     4294908796, 0,    469,  0x0, 0,   24,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   25,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   26,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   27,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   28,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   30,  0,   0,   0,   0,   38,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   31,  0,   0,   0,   0,   40,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   32,  0,   0,   0,   0,   41,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   35,  0,   0,   0,   0,   43,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   38,  0,   255, 255, 0,   42,  255,  0)
    DeclNpc(22510,   0,       1299,    225,  389,  0x0, 0,   37,  0,   0,   0,   0,   44,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   7,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(16000,   0,       7000,    2000,    17210,   1500,    7430,    0x007E, 0,  6,  0x0000)
    DeclActor(19680,   0,       3710,    2000,    19740,   1500,    4890,    0x007E, 0,  8,  0x0000)
    DeclActor(65800,   0,       2430,    1200,    65800,   1500,    2430,    0x007C, 0,  54, 0x0000)

    ChipFrameInfo(1540, 0)                                       # 0

    ScpFunction((
        "Function_0_604",          # 00, 0
        "Function_1_6B4",          # 01, 1
        "Function_2_765",          # 02, 2
        "Function_3_790",          # 03, 3
        "Function_4_7BB",          # 04, 4
        "Function_5_1398",         # 05, 5
        "Function_6_1474",         # 06, 6
        "Function_7_1478",         # 07, 7
        "Function_8_2878",         # 08, 8
        "Function_9_287C",         # 09, 9
        "Function_10_3D4C",        # 0A, 10
        "Function_11_4A79",        # 0B, 11
        "Function_12_582C",        # 0C, 12
        "Function_13_5F0B",        # 0D, 13
        "Function_14_6725",        # 0E, 14
        "Function_15_7176",        # 0F, 15
        "Function_16_7BF7",        # 10, 16
        "Function_17_7D07",        # 11, 17
        "Function_18_8B42",        # 12, 18
        "Function_19_8CDB",        # 13, 19
        "Function_20_9A71",        # 14, 20
        "Function_21_9DF7",        # 15, 21
        "Function_22_A14C",        # 16, 22
        "Function_23_A599",        # 17, 23
        "Function_24_A958",        # 18, 24
        "Function_25_A9F1",        # 19, 25
        "Function_26_AC1A",        # 1A, 26
        "Function_27_AF35",        # 1B, 27
        "Function_28_B0A5",        # 1C, 28
        "Function_29_B1E8",        # 1D, 29
        "Function_30_B269",        # 1E, 30
        "Function_31_B2B6",        # 1F, 31
        "Function_32_B328",        # 20, 32
        "Function_33_B3A4",        # 21, 33
        "Function_34_BDA2",        # 22, 34
        "Function_35_BE5B",        # 23, 35
        "Function_36_BF64",        # 24, 36
        "Function_37_BFFD",        # 25, 37
        "Function_38_C1DC",        # 26, 38
        "Function_39_C2CD",        # 27, 39
        "Function_40_C369",        # 28, 40
        "Function_41_C39F",        # 29, 41
        "Function_42_C442",        # 2A, 42
        "Function_43_C62A",        # 2B, 43
        "Function_44_C631",        # 2C, 44
        "Function_45_C910",        # 2D, 45
        "Function_46_C917",        # 2E, 46
        "Function_47_CBE8",        # 2F, 47
        "Function_48_D3A9",        # 30, 48
        "Function_49_F7AC",        # 31, 49
        "Function_50_1048E",       # 32, 50
        "Function_51_10870",       # 33, 51
        "Function_52_10871",       # 34, 52
        "Function_53_10DDE",       # 35, 53
        "Function_54_112F3",       # 36, 54
        "Function_55_1139C",       # 37, 55
        "Function_56_113F1",       # 38, 56
        "Function_57_11446",       # 39, 57
    ))


    def Function_0_604(): pass

    label("Function_0_604")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_63C"),
        (1, "loc_648"),
        (2, "loc_654"),
        (3, "loc_660"),
        (4, "loc_66C"),
        (5, "loc_678"),
        (6, "loc_684"),
        (SWITCH_DEFAULT, "loc_690"),
    )


    label("loc_63C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_69C")

    label("loc_648")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_69C")

    label("loc_654")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_69C")

    label("loc_660")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_69C")

    label("loc_66C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_69C")

    label("loc_678")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_69C")

    label("loc_684")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_69C")

    label("loc_690")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_69C")

    label("loc_69C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_69C")

    label("loc_6B3")

    Return()

    # Function_0_604 end

    def Function_1_6B4(): pass

    label("Function_1_6B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_764")
    OP_95(0xFE, 7400, 0, -1600, 1500, 0x0)
    OP_95(0xFE, 7400, 0, 1420, 1500, 0x0)
    OP_95(0xFE, 10380, 0, 4530, 1500, 0x0)
    OP_95(0xFE, 13330, 0, 4550, 1500, 0x0)
    OP_95(0xFE, 16420, 0, 1470, 1500, 0x0)
    OP_95(0xFE, 16420, 0, -1430, 1500, 0x0)
    OP_95(0xFE, 13440, 0, -4490, 1500, 0x0)
    OP_95(0xFE, 10540, 0, -4490, 1500, 0x0)
    Jump("Function_1_6B4")

    label("loc_764")

    Return()

    # Function_1_6B4 end

    def Function_2_765(): pass

    label("Function_2_765")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_78F")
    OP_94(0xFE, 0x1932, 0x148C, 0x1DBA, 0xDCA, 0x3E8)
    Sleep(400)
    Jump("Function_2_765")

    label("loc_78F")

    Return()

    # Function_2_765 end

    def Function_3_790(): pass

    label("Function_3_790")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7BA")
    OP_94(0xFE, 0x4556, 0xFFFFF1F0, 0x3E4E, 0xFFFFE926, 0x3E8)
    Sleep(400)
    Jump("Function_3_790")

    label("loc_7BA")

    Return()

    # Function_3_790 end

    def Function_4_7BB(): pass

    label("Function_4_7BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_958")
    SetChrPos(0xB, 55650, 0, 500, 180)
    SetChrPos(0xE, 55650, 0, -620, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FA")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xE, 0x10)

    label("loc_7FA")

    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 50980, 120, 59070, 300)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 21840, 120, -7220, 270)
    SetChrChipByIndex(0x11, 0xC)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 21840, 120, -8200, 270)
    SetChrChipByIndex(0x12, 0xD)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 16800, 120, -6890, 0)
    SetChrChipByIndex(0x14, 0x10)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 16950, 0, -5000, 0)
    BeginChrThread(0x17, 0, 0, 3)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 7680, 120, 6840, 180)
    SetChrChipByIndex(0x13, 0xE)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 6680, 120, 6840, 180)
    SetChrChipByIndex(0x18, 0x15)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 2000, 120, 4140, 90)
    SetChrChipByIndex(0x15, 0x11)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 7750, 120, 9800, 180)
    SetChrChipByIndex(0x16, 0x12)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    ClearChrFlags(0x25, 0x80)
    Jump("loc_132F")

    label("loc_958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9AA")
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xE, 0x8)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrPos(0xC, 50900, 0, 57650, 270)
    SetChrPos(0xD, 49700, 0, 57650, 90)
    Jump("loc_132F")

    label("loc_9AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_A04")
    SetChrPos(0xB, 55650, 0, 500, 180)
    SetChrPos(0xE, 55650, 0, -620, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E9")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xE, 0x10)

    label("loc_9E9")

    SetChrFlags(0xC, 0x80)
    SetChrPos(0xD, 51850, 0, 58000, 90)
    Jump("loc_132F")

    label("loc_A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A39")
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xE, 0x8)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrFlags(0xC, 0x80)
    Jump("loc_132F")

    label("loc_A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BDF")
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xE, 0x8)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 16800, 120, -6890, 0)
    SetChrChipByIndex(0x11, 0xC)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 21840, 120, -4430, 270)
    SetChrChipByIndex(0x12, 0xD)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 5100, 120, 4740, 90)
    SetChrFlags(0x13, 0x10)
    SetChrChipByIndex(0x13, 0xE)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 7400, 0, 3740, 270)
    BeginChrThread(0x17, 0, 0, 2)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 2000, 120, 7880, 90)
    SetChrChipByIndex(0x15, 0x11)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB1")
    ClearChrFlags(0x1E, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6A")
    SetChrFlags(0x1E, 0x10)

    label("loc_B6A")

    SetChrPos(0x1E, 55400, 0, 1000, 135)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 56600, 0, 0, 270)
    SetChrFlags(0x1D, 0x10)
    SetChrPos(0x9, 55400, 0, -1000, 45)
    SetChrFlags(0x9, 0x10)
    Jump("loc_BDA")

    label("loc_BB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BDA")
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 65800, 0, 1700, 180)

    label("loc_BDA")

    Jump("loc_132F")

    label("loc_BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D09")
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xE, 0x8)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 55650, 0, 500, 180)
    SetChrFlags(0x1D, 0x10)
    SetChrPos(0xC, 55650, 0, -620, 0)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 8160, 0, 400, 180)
    SetChrFlags(0x1C, 0x10)
    SetChrPos(0xA, 8160, 0, -630, 0)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 2000, 120, 4140, 90)
    SetChrChipByIndex(0x12, 0xD)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 18850, 120, -4310, 270)
    SetChrChipByIndex(0x13, 0xE)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 18850, 120, -5220, 270)
    SetChrChipByIndex(0x14, 0x10)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 7520, 120, 6840, 180)
    SetChrChipByIndex(0x16, 0x12)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jump("loc_132F")

    label("loc_D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_DC9")
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xE, 0x8)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0x10, 56280, 0, -56460, 45)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 7400, 120, 6850, 180)
    SetChrChipByIndex(0x11, 0xC)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 19660, 120, -9970, 0)
    SetChrChipByIndex(0x14, 0x10)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 16560, 120, -9980, 0)
    SetChrChipByIndex(0x18, 0x15)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    Jump("loc_132F")

    label("loc_DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F19")
    SetChrPos(0xB, 55650, 0, 500, 180)
    SetChrPos(0xE, 55650, 0, -620, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E08")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xE, 0x10)

    label("loc_E08")

    SetChrPos(0xC, 50980, 120, 59070, 300)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrSubChip(0xC, 0x1)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, 49270, 0, 59090, 90)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, 49900, 0, 58070, 45)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E73")
    SetChrFlags(0x1F, 0x10)
    SetChrFlags(0x20, 0x10)

    label("loc_E73")

    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 18910, 120, -5350, 270)
    SetChrChipByIndex(0x12, 0xD)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 2000, 120, 7510, 90)
    SetChrChipByIndex(0x13, 0xE)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 7750, 120, 9800, 180)
    SetChrChipByIndex(0x15, 0x11)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 16810, 120, -6920, 0)
    SetChrChipByIndex(0x16, 0x12)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jump("loc_132F")

    label("loc_F19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_101A")
    SetChrPos(0xB, 55650, 0, 500, 180)
    SetChrPos(0xE, 55650, 0, -620, 0)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F67")
    SetChrFlags(0x10, 0x10)

    label("loc_F67")

    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 16800, 120, -9960, 0)
    SetChrChipByIndex(0x11, 0xC)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 8340, 120, 9890, 180)
    SetChrChipByIndex(0x14, 0x10)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x10)
    SetChrSubChip(0x14, 0x2)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 7550, 120, 9800, 180)
    SetChrChipByIndex(0x18, 0x15)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x10)
    SetChrSubChip(0x18, 0x1)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 21840, 120, -4430, 270)
    SetChrChipByIndex(0x15, 0x11)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    Jump("loc_132F")

    label("loc_101A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_121C")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0xE, 59270, 0, -57930, 90)
    SetChrPos(0x10, 60270, 0, -57930, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1068")
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0xE, 0x10)

    label("loc_1068")

    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 5100, 120, 4740, 90)
    SetChrChipByIndex(0x12, 0xD)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 9940, 0, 1990, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B4")
    SetChrFlags(0x13, 0x10)

    label("loc_10B4")

    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 21840, 120, -7320, 270)
    SetChrChipByIndex(0x16, 0x12)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x10)
    SetChrSubChip(0x16, 0x1)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 21840, 120, -8100, 270)
    SetChrChipByIndex(0x17, 0x13)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x10)
    SetChrSubChip(0x17, 0x2)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 50980, 120, 59070, 300)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_END)), "loc_1217")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A9")
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, 48860, 0, 59410, 90)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 49210, 0, 57900, 0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 18850, 120, -3970, 270)
    SetChrChipByIndex(0x24, 0x21)
    SetChrSubChip(0x24, 0x0)
    EndChrThread(0x24, 0x0)
    SetChrBattleFlags(0x24, 0x4)
    Jump("loc_1217")

    label("loc_11A9")

    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 50980, 120, 59070, 300)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 56950, 0, 60000, 90)
    SetChrChipByIndex(0x24, 0x26)
    SetChrSubChip(0x24, 0x0)
    EndChrThread(0x24, 0x0)
    SetChrBattleFlags(0x24, 0x4)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 59210, 700, 59900, 270)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0x10, 0x10)

    label("loc_1217")

    Jump("loc_132F")

    label("loc_121C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_132F")
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xE, 0x8)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, 16050, 100, -6990, 0)
    SetChrChipByIndex(0x20, 0x1D)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    SetChrPos(0xC, 16050, 0, -5480, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1293")
    SetChrFlags(0x20, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_1293")

    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 4090, 120, 9890, 180)
    SetChrChipByIndex(0x11, 0xC)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 19730, 120, -9960, 0)
    SetChrChipByIndex(0x12, 0xD)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 5110, 120, 5170, 90)
    SetChrChipByIndex(0x14, 0x10)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 5110, 120, 4330, 90)
    SetChrChipByIndex(0x17, 0x13)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)

    label("loc_132F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1348")
    ClearScenarioFlags(0x22, 0)
    SetMapFlags(0x10000000)
    Event(0, 47)
    Jump("loc_137F")

    label("loc_1348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_135C")
    ClearScenarioFlags(0x22, 1)
    Event(0, 52)
    Jump("loc_137F")

    label("loc_135C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1370")
    ClearScenarioFlags(0x22, 2)
    Event(0, 53)
    Jump("loc_137F")

    label("loc_1370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_137F")
    ClearScenarioFlags(0x22, 3)
    Event(0, 49)

    label("loc_137F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1397")
    ClearScenarioFlags(0x25, 1)
    Call(0, 45)

    label("loc_1397")

    Return()

    # Function_4_7BB end

    def Function_5_1398(): pass

    label("Function_5_1398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_13AA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13AA")

    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_13E2")
    OP_52(0x24, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_140C")
    OP_65(0x1, 0x1)

    label("loc_140C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1448")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 30, 0)

    label("loc_1448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1460")
    OP_1B(0x2, 0x0, 0x37)
    OP_1B(0x1, 0x0, 0x38)

    label("loc_1460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1473")
    OP_1B(0x0, 0x0, 0x39)

    label("loc_1473")

    Return()

    # Function_5_1398 end

    def Function_6_1474(): pass

    label("Function_6_1474")

    Call(0, 7)
    Return()

    # Function_6_1474 end

    def Function_7_1478(): pass

    label("Function_7_1478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_148A")
    Call(0, 46)
    Return()

    label("loc_148A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14B3")
    Call(0, 50)
    Return()

    label("loc_14B3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1630")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_158E")

    ChrTalk(
        0x8,
        (
            "Outpatient being stopped,\x01",
            "It was finally possible to resume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is going to be busy for a while,\x01",
            "I was really relieved ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is also thanks to everyone.\x01",
            "thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_162B")

    label("loc_158E")


    ChrTalk(
        0x8,
        (
            "Outpatient being stopped,\x01",
            "It was finally possible to resume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is going to be busy for a while,\x01",
            "It is polite as a hospital staff member\x01",
            "It is a place I want to keep in mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_162B")

    Jump("loc_2874")

    label("loc_1630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_177B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FA")

    ChrTalk(
        0x8,
        (
            "According to rumors, receiving invalid declaration of matter\x01",
            "Some of the city's riots\x01",
            "It seems that it has happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems that the Defense Forces have quelled soon … …\x01",
            "I am worried whether injured people are out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1776")

    label("loc_16FA")


    ChrTalk(
        0x8,
        (
            "Receiving invalid declarations\x01",
            "Some of the city's riots\x01",
            "It seems that it has happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I am worried whether injured people are out ……\x02",
    )

    CloseMessageWindow()

    label("loc_1776")

    Jump("loc_2874")

    label("loc_177B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_18D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_184F")

    ChrTalk(
        0x8,
        (
            "以前、通院していたpatientさんに\x01",
            "To keep the prescribed medicine comfortable,\x01",
            "We are negotiating with the Defense Forces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, there are too many … …\x01",
            "It is not possible to make arrangements easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "…… It will not be left.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18CB")

    label("loc_184F")


    ChrTalk(
        0x8,
        (
            "As outpatient reception is stopped,\x01",
            "薬だけでも市内のpatientさんに\x01",
            "I'd like to deliver it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "…… It will not be left.\x02",
    )

    CloseMessageWindow()

    label("loc_18CB")

    Jump("loc_2874")

    label("loc_18D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1AA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A00")

    ChrTalk(
        0x8,
        (
            "In the hospital due to the occurrence of \"eidolon\"\x01",
            "I am stopping the outpatient reception.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "現在は、重病・重傷patientのみが\x01",
            "With an ambulance with escort of Defense Forces\x01",
            "With it being transported ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This system is traditional\x01",
            "Contrary to the significance of Ursula hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… More than anything,\x01",
            "市内のpatientさんがとても心配です。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AA1")

    label("loc_1A00")


    ChrTalk(
        0x8,
        (
            "In the hospital due to the occurrence of \"eidolon\"\x01",
            "I am stopping the outpatient reception.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Treat only serious illness · serious injury\x01",
            "I can not give up … ….\x01",
            "市内のpatientさんがとても心配です。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA1")

    Jump("loc_2874")

    label("loc_1AA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1ED5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DBA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1BE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B73")

    ChrTalk(
        0x8,
        (
            "Medical supplies arrived\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "While overwhelming, on behalf of the hospital\x01",
            "I will thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, really\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BDD")

    label("loc_1B73")


    ChrTalk(
        0x8,
        (
            "While overwhelming, on behalf of the hospital\x01",
            "I will thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, really\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDD")

    Jump("loc_1DB5")

    label("loc_1BE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1C8A")

    ChrTalk(
        0x8,
        (
            "Explaining the situation to Remiferia,\x01",
            "I will send medical supplies again\x01",
            "I arranged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although it will be delayed somewhat ……\x01",
            "It can not be helped that it is done.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB5")

    label("loc_1C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D41")

    ChrTalk(
        0x8,
        (
            "Tony, security guy,\x01",
            "I reported anything to the secretary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now in front of the examination room,\x01",
            "Professor Seylandと３人で\x01",
            "I seem to be consulting … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Is there something wrong?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DB5")

    label("loc_1D41")


    ChrTalk(
        0x8,
        (
            "Security guard Tony and the secretary general,\x01",
            "診察室前でProfessor Seylandと\x01",
            "It seems they are consulting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Is there something wrong?\x02",
    )

    CloseMessageWindow()

    label("loc_1DB5")

    Jump("loc_1ED0")

    label("loc_1DBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E6A")

    ChrTalk(
        0x8,
        (
            "Fran's sick room is\x01",
            "It is room # 301 on the third floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although it has stabilized for a long time,\x01",
            "My physical strength has not yet returned.\x01",
            "It seems like ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Cheer up please\x01",
            "Please give me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ED0")

    label("loc_1E6A")


    ChrTalk(
        0x8,
        (
            "Fran, just the other day\x01",
            "The consciousness was returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It was a serious injury … …\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ED0")

    Jump("loc_2874")

    label("loc_1ED5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_20B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_200C")

    ChrTalk(
        0x8,
        (
            "In a train accident yesterday,\x01",
            "外国人を含む多数のpatientが\x01",
            "It has been brought in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ursula Hospital is a foreigner's\x01",
            "Because the acceptance system is in place,\x01",
            "I was able to respond smoothly … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Medical is not yet developed\x01",
            "If an accident happens in another country\x01",
            "What was going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "If you think about it, it will be creepy.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20B4")

    label("loc_200C")


    ChrTalk(
        0x8,
        (
            "Medical is not yet developed\x01",
            "If an accident happens in another country\x01",
            "What was going on ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Most of them were minor injuries,\x01",
            "In that sense\x01",
            "You may have been lucky.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20B4")

    Jump("loc_2874")

    label("loc_20B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_229A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2188")

    ChrTalk(
        0x8,
        "That luggage was misdirected.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "One of the nurses\x01",
            "I made an order mistake soon\x01",
            "Martha 's chief was making noise … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyways,\x01",
            "Please visit the second floor once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F9")

    label("loc_2188")


    ChrTalk(
        0x8,
        (
            "Package safely\x01",
            "You seem to have been received.\x01",
            "Hehe, it was good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, please take care\x01",
            "Please come back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F9")

    Jump("loc_2295")

    label("loc_21FE")


    ChrTalk(
        0x8,
        (
            "Welcome to Ursula Hospital.\x01",
            "The reception of outpatient / visitation is here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Those who do re-examination are\x01",
            "As we accept reservations,\x01",
            "Please do use it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2295")

    Jump("loc_2874")

    label("loc_229A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_23BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2357")

    ChrTalk(
        0x8,
        (
            "…… You should not do it.\x01",
            "Somehow it fell to the whole staff\x01",
            "The mood is spreading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For the operation of Shizuoka\x01",
            "It was expecting,\x01",
            "Perhaps it can not be helped … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_23B9")

    label("loc_2357")


    ChrTalk(
        0x8,
        (
            "…… Our officials\x01",
            "You should not do this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Somehow depressed mood\x01",
            "I have to wipe it ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B9")

    Jump("loc_2874")

    label("loc_23BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_24F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_248F")

    ChrTalk(
        0x8,
        (
            "Mikhail's discharge from you\x01",
            "It seems that it was decided next week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because I was hospitalized for a long time,\x01",
            "It makes me somewhat lonely … …\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "On the day, everyone to see me off\x01",
            "I want to give it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24F3")

    label("loc_248F")


    ChrTalk(
        0x8,
        (
            "Mikhail was determined to be discharged from the hospital\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "On the day, everyone to see me off\x01",
            "I want to give it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F3")

    Jump("loc_2874")

    label("loc_24F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_26F2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_25BA")

    ChrTalk(
        0x8,
        (
            "Prince Albert閣下は街の方へ\x01",
            "You seem to have returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Huhu, thanks to everyone for your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "patientさんのほうは退院まで\x01",
            "I will treat you responsibly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26ED")

    label("loc_25BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_265A")

    ChrTalk(
        0x8,
        (
            "先ほど、Prince Albert閣下が\x01",
            "Ariosさんといらっしゃいました。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now I have finished the inspection as usual,\x01",
            "A sympathy for Shizuku-chan\x01",
            "It seems to be doing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26ED")

    label("loc_265A")


    ChrTalk(
        0x8,
        (
            "現在、Prince Albert閣下が\x01",
            "Ariosさんと一緒に\x01",
            "I am going to the medical examination room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As the inspection was finished,\x01",
            "You seem to be talking a bit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26ED")

    Jump("loc_2874")

    label("loc_26F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2874")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2775")

    ChrTalk(
        0x8,
        (
            "Everyone, collection of questionnaire\x01",
            "Thank you for your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there is something again\x01",
            "Come at anytime\x01",
            "Please do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2874")

    label("loc_2775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2810")

    ChrTalk(
        0x8,
        (
            "Professor Seylandは\x01",
            "To the laboratory of pharmacology · neurology\x01",
            "Welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since there is a research building when you go to the rooftop,\x01",
            "From there please head to the 4th floor.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2874")

    label("loc_2810")


    ChrTalk(
        0x8,
        (
            "Professor Seylandは\x01",
            "I will come to the laboratory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The laboratory of pharmacology / neurology,\x01",
            "It is the 4th floor of the research building.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2874")

    TalkEnd(0x8)
    Return()

    # Function_7_1478 end

    def Function_8_2878(): pass

    label("Function_8_2878")

    Call(0, 9)
    Return()

    # Function_8_2878 end

    def Function_9_287C(): pass

    label("Function_9_287C")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_296A")

    ChrTalk(
        0x9,
        (
            "The current state that medical supplies are limited,\x01",
            "I can not be optimistic at all … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In this way,\x01",
            "再開できただけでも、patientを救える\x01",
            "The possibilities are quite different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Our officials, too,\x01",
            "You must do your best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A24")

    label("loc_296A")


    ChrTalk(
        0x9,
        (
            "The current situation is difficult,\x01",
            "If we can cooperate with Remiperia again\x01",
            "We can also solve the problem of medical supplies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Finally the outpatient response\x01",
            "I got to be able to do … ….\x01",
            "You must do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A24")

    Jump("loc_3D48")

    label("loc_2A29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2BC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B24")

    ChrTalk(
        0x9,
        (
            "Current situation, Crossbell City direction\x01",
            "Any information\x01",
            "It has stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Probably due to the invalid declaration\x01",
            "Information intentionally\x01",
            "You are blocking it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When this happens, such as a sudden illness\x01",
            "We can not take action.\x01",
            "…… I am worried about everyone in the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BBE")

    label("loc_2B24")


    ChrTalk(
        0x9,
        (
            "Current situation, Crossbell City direction\x01",
            "Any information\x01",
            "It has stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When this happens, such as a sudden illness\x01",
            "We can not take action.\x01",
            "…… I am worried about everyone in the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BBE")

    Jump("loc_3D48")

    label("loc_2BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2D28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C9B")

    ChrTalk(
        0x9,
        (
            "Information restriction was done throughout the crossbell,\x01",
            "Information in the city is almost not included.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "ときどき救急patientの情報が\x01",
            "As much as it is sent,\x01",
            "Correspondence was also getting behind the back … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "It is a bad situation.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D23")

    label("loc_2C9B")


    ChrTalk(
        0x9,
        (
            "Information restriction was done throughout the crossbell,\x01",
            "Information in the city is almost not included.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Correspondence was also getting behind the back … ….\x01",
            "It is a bad situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D23")

    Jump("loc_3D48")

    label("loc_2D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2EF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E54")

    ChrTalk(
        0x9,
        (
            "To Mr. Tio,\x01",
            "Relating to the maintenance of the power net\x01",
            "Thank you for all the help you have given me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Accept the acceptance situation by any chance\x01",
            "In order to be thorough,\x01",
            "Because the power net is indispensable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Borrow this place, once again\x01",
            "I will thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FHuhu, no …\x01",
            "It is not a big deal.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2EF2")

    label("loc_2E54")


    ChrTalk(
        0x9,
        (
            "To Mr. Tio\x01",
            "Relating to the maintenance of the power net\x01",
            "Thank you for all the help you have given me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Nonetheless, this situation continues\x01",
            "It is very bad as a hospital.\x01",
            "I have to manage somehow … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EF2")

    Jump("loc_3D48")

    label("loc_2EF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3376")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_304B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FD6")

    ChrTalk(
        0x9,
        (
            "To Ricardo of the airport,\x01",
            "I will inform you again that goods have arrived\x01",
            "I contacted you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seemed safe over there,\x01",
            "I think that it was good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Already like this\x01",
            "It is something you want to do without.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3042")

    label("loc_2FD6")


    ChrTalk(
        0x9,
        (
            "Ricardo seemed to be relieved,\x01",
            "I think that it was good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Already like this\x01",
            "It is something you want to do without.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3042")

    TalkEnd(0x9)
    Return()

    label("loc_304B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_30E4")

    ChrTalk(
        0x9,
        (
            "The matter of this year is everyone's\x01",
            "Because it is not a fault,\x01",
            "Please do not be discouraged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway, the other side here\x01",
            "I will try it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    label("loc_30E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_318E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3107")
    Call(0, 35)
    Jump("loc_3189")

    label("loc_3107")


    ChrTalk(
        0x9,
        (
            "Maybe something about transportation\x01",
            "It may be an effect …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway, once again in each direction\x01",
            "Let's get in touch.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3189")

    Jump("loc_3371")

    label("loc_318E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32E1")

    ChrTalk(
        0x9,
        (
            "For a while, Ms. Iria\x01",
            "Those who say that they want to visit\x01",
            "A lot of people were coming … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because Iria is unconscious,\x01",
            "We refuse non-persons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Nevertheless, only the goods of the sympathy\x01",
            "Those who put in sweets etc.\x01",
            "It seems that we are going after all … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For Mr. Ilya residents\x01",
            "How big it was,\x01",
            "I feel it again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3371")

    label("loc_32E1")


    ChrTalk(
        0x9,
        (
            "To Mr. Ilya\x01",
            "Those who put in sweets etc.\x01",
            "I will not fail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For her residents\x01",
            "How big it was,\x01",
            "I feel it again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3371")

    Jump("loc_3D48")

    label("loc_3376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3505")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3479")

    ChrTalk(
        0x9,
        (
            "From yesterday, from the Empire and the Republic\x01",
            "From families of accident victims\x01",
            "Safety confirmation is one after another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "After all, when it comes to hospitalization in a foreign country\x01",
            "If you are worried\x01",
            "It seems to be a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even without it, crossbell\x01",
            "From independent advice of the other day\x01",
            "Because the state of tension is continuing … ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3500")

    label("loc_3479")


    ChrTalk(
        0x9,
        (
            "After all, when it comes to hospitalization in a foreign country\x01",
            "If you are worried\x01",
            "It seems to be a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In order to return home as soon as possible,\x01",
            "It is a place I want to correspond with sincerely sincerity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3500")

    Jump("loc_3D48")

    label("loc_3505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3673")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35F9")

    ChrTalk(
        0x9,
        (
            "Legal development of the power network\x01",
            "Thanks to the preparation, on the net\x01",
            "Recurring appointments have also increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If the crossbell is independent\x01",
            "Such useful bills too\x01",
            "I think it will be easier to get through … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In fact, the referendum\x01",
            "What will happen?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_366E")

    label("loc_35F9")


    ChrTalk(
        0x9,
        (
            "If the crossbell is independent\x01",
            "It will make it easier for useful bills to pass through\x01",
            "I think……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In fact, the referendum\x01",
            "What will happen?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_366E")

    Jump("loc_3D48")

    label("loc_3673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3835")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_378D")

    ChrTalk(
        0x9,
        (
            "In Shizuku's surgery the other day,\x01",
            "Professor Seylandの考案した\x01",
            "A revolutionary technique was given.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Interest from medical personnel is also high,\x01",
            "The trust that had been falling for a while\x01",
            "It can be said that it was completely recovered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… However, I am rejoiced by letting go.\x01",
            "I wanted it to succeed ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3830")

    label("loc_378D")


    ChrTalk(
        0x9,
        (
            "By trying a revolutionary surgery,\x01",
            "The trust that had been falling for a while\x01",
            "It can be said that it was completely recovered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… However, I am rejoiced by letting go.\x01",
            "I wanted it to succeed ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3830")

    Jump("loc_3D48")

    label("loc_3835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_39CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_393C")

    ChrTalk(
        0x9,
        (
            "in a few days,\x01",
            "Professor Seylandによって\x01",
            "A big surgery is done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "昨日のPrince Albertの視察で\x01",
            "From Remiferia as well\x01",
            "I was able to support you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Toward the Success of Surgery\x01",
            "I have to do as much as I can\x01",
            "You can not do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_39CA")

    label("loc_393C")


    ChrTalk(
        0x9,
        (
            "in a few days,\x01",
            "Professor Seylandによって\x01",
            "A big surgery is done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Toward the Success of Surgery\x01",
            "I have to do as much as I can\x01",
            "You can not do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39CA")

    Jump("loc_3D48")

    label("loc_39CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3B1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AA0")

    ChrTalk(
        0x9,
        (
            "Prince Albertから\x01",
            "Labor#2RNekira#I received the word of saying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To the grand priest who is also a hospital sponsor,\x01",
            "We have been strongly supporting from the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "All the staff are really encouraged.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3B17")

    label("loc_3AA0")


    ChrTalk(
        0x9,
        (
            "To the grand priest who is also a hospital sponsor,\x01",
            "We have been strongly supporting from the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "All the staff are really encouraged.\x02",
    )

    CloseMessageWindow()

    label("loc_3B17")

    Jump("loc_3D48")

    label("loc_3B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3D48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C8A")

    ChrTalk(
        0x9,
        (
            "In the scandal of \"Colon Case\"\x01",
            "The trust that the hospital has built up\x01",
            "It fell to the ground once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A hospital doctor uses medicine\x01",
            "It made me confused.\x01",
            "…… It will be an unreasonable story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By in-depth investigation by the police\x01",
            "Usually, the medicine he had prescribed is\x01",
            "Although it proved to be no problem … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "patientさんの中には、いまだに\x01",
            "There seems to be some people who can not ward off distrust.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3D48")

    label("loc_3C8A")


    ChrTalk(
        0x9,
        (
            "Although allegations were dispelled,\x01",
            "I still feel distrust of the hospital\x01",
            "There are also those who are holding it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "From now on, more open medical care\x01",
            "Aim and gradually regain trust\x01",
            "いかなければYou can not do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D48")

    TalkEnd(0x9)
    Return()

    # Function_9_287C end

    def Function_10_3D4C(): pass

    label("Function_10_3D4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3EED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E3D")

    ChrTalk(
        0xA,
        (
            "My brother you guys ……\x01",
            "It seems to be very hard,\x01",
            "You should never get beckoned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If everything is done and calm down\x01",
            "I'm sure to play together again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FOh, leave it to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHahaha I will do my best.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3EE8")

    label("loc_3E3D")


    ChrTalk(
        0xA,
        (
            "If everything is done and calm down\x01",
            "I'm sure to play together again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ada and Philia, Shillon to Meihua,\x01",
            "Also at this time Mr. Martha asked,\x01",
            "Let's take a part with everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EE8")

    Jump("loc_4A75")

    label("loc_3EED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4085")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FED")

    ChrTalk(
        0xA,
        (
            "I have to stay in the hospital\x01",
            "The stress of outpatient visitors,\x01",
            "I was gradually reaching the peak … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There was such a thing in town,\x01",
            "Maybe I can return home\x01",
            "It seems I started having hope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I do not know what will happen,\x01",
            "I hope you can return home really.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4080")

    label("loc_3FED")


    ChrTalk(
        0xA,
        (
            "There was such a thing in town,\x01",
            "I have to stay in the hospital\x01",
            "外来客もIt seems I started having hope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I do not know what will happen,\x01",
            "I hope you can return home really.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4080")

    Jump("loc_4A75")

    label("loc_4085")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4206")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4184")

    ChrTalk(
        0xA,
        (
            "Iria · Platier,\x01",
            "As of now, the prospect of recovery\x01",
            "It looks like it does not go on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "……but it's okay.\x01",
            "The teachers of our hospital are\x01",
            "Very outstanding things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It may take time,\x01",
            "If you are a teacher absolutely\x01",
            "It will cure Ilya.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4201")

    label("loc_4184")


    ChrTalk(
        0xA,
        (
            "The teachers of our hospital are\x01",
            "Very outstanding things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It may take time,\x01",
            "If you are a teacher absolutely\x01",
            "It will cure Ilya.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4201")

    Jump("loc_4A75")

    label("loc_4206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4382")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F4")

    ChrTalk(
        0xA,
        (
            "This is the situation ……\x01",
            "People in the hospital\x01",
            "It's unexpectedly positive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway, I was unconscious\x01",
            "Iria · Platier\x01",
            "I finally awoke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If so, we also\x01",
            "I think I have to work hard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_437D")

    label("loc_42F4")


    ChrTalk(
        0xA,
        (
            "Iria · Platier\x01",
            "To regain consciousness,\x01",
            "It's been a while since the beginning of the year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If so, we also\x01",
            "I think I have to work hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_437D")

    Jump("loc_4A75")

    label("loc_4382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4421")

    ChrTalk(
        0xA,
        (
            "Ha Ha, no matter how much\x01",
            "I'm getting tired …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "……ううん、patientさんたちは\x01",
            "I am feeling more painful.\x01",
            "I can not say whining.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A75")

    label("loc_4421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_44AC")

    ChrTalk(
        0xA,
        (
            "Because of the train accident yesterday\x01",
            "We are also busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can play for a while\x01",
            "It's not atmosphere either … ….\x01",
            "I have to work firmly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A75")

    label("loc_44AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4540")

    ChrTalk(
        0xA,
        (
            "To the strength of the core of Shizuoka\x01",
            "I'm always cheered by this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Our nurses also have hope\x01",
            "I have to support Shizuoka.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A75")

    label("loc_4540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_46A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_460C")

    ChrTalk(
        0xA,
        (
            "Shizuku, as ever\x01",
            "I have undergone surgery several times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But even the excellent hospital teachers\x01",
            "Always not going well ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "あの子も、Ariosさんも\x01",
            "I guess it really is uneasy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_469B")

    label("loc_460C")


    ChrTalk(
        0xA,
        (
            "Shizuku, as ever\x01",
            "Although I have undergone an operation several times,\x01",
            "Always not going well ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "あの子も、Ariosさんも\x01",
            "I guess it really is uneasy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_469B")

    Jump("loc_4A75")

    label("loc_46A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_47DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_476F")

    ChrTalk(
        0xA,
        (
            "噂じゃProfessor Seylandが、\x01",
            "Large surgery in the near future\x01",
            "I will tell you ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Such surgery in this hospital\x01",
            "Being necessary\x01",
            "You do not have anything other than \"that girl\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I hope it will heal.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_47D9")

    label("loc_476F")


    ChrTalk(
        0xA,
        (
            "A big surgery at this hospital\x01",
            "Being necessary\x01",
            "You do not have anything other than \"that girl\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I hope it will heal.\x02",
    )

    CloseMessageWindow()

    label("loc_47D9")

    Jump("loc_4A75")

    label("loc_47DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4915")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_489C")

    ChrTalk(
        0xA,
        (
            "今日はProfessor Lagoが\x01",
            "I do not have a business trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anything, to a foreign academic society\x01",
            "I am attending.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "代わりにProfessor Seylandが\x01",
            "I am in charge of internal medicine today.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4910")

    label("loc_489C")


    ChrTalk(
        0xA,
        (
            "今日はProfessor Lago、\x01",
            "I am on a business trip to a foreign conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even though the Grand priest is coming\x01",
            "I was mournful that I could not say hello.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4910")

    Jump("loc_4A75")

    label("loc_4915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4A75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A24")

    ChrTalk(
        0xA,
        (
            "That, to Randy\x01",
            "You are not my brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FRan-chan, it's been a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000Flong time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "by the way\x01",
            "It was a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because it's no problem\x01",
            "I would like to tell you more,\x01",
            "I am at work now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Please speak again next time.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 6)
    Jump("loc_4A75")

    label("loc_4A24")


    ChrTalk(
        0xA,
        (
            "I would like to tell you more,\x01",
            "I am at work now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Please speak again next time.\x02",
    )

    CloseMessageWindow()

    label("loc_4A75")

    TalkEnd(0xFE)
    Return()

    # Function_10_3D4C end

    def Function_11_4A79(): pass

    label("Function_11_4A79")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4B0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A97")
    Call(0, 12)
    Jump("loc_4B05")

    label("loc_4A97")


    ChrTalk(
        0xB,
        (
            "Whoopee, my favorite hands are\x01",
            "It must be this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "さあ、patientは待ってくれん。\x01",
            "Let's say you're about to start.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B05")

    Jump("loc_5828")

    label("loc_4B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4D13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C36")

    ChrTalk(
        0xB,
        (
            "With Seirando\x01",
            "I tried an old medical book … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "With medicinal herbs that are growing within the autonomous province,\x01",
            "Some medicines such as anesthesia\x01",
            "She seems to be able to mix it here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Diplomacy with Remiferia was cut off,\x01",
            "Although it does not change that medical supplies are missing … ….\x01",
            "It may have been only a little light.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4D0E")

    label("loc_4C36")


    ChrTalk(
        0xB,
        (
            "When examining with Seileland,\x01",
            "Some missing chemicals\x01",
            "It seems to be able to cover just with the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Diplomacy with Remiferia was cut off,\x01",
            "Although it does not change that medical supplies are missing … ….\x01",
            "It may have been only a little light.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D0E")

    Jump("loc_5828")

    label("loc_4D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4DD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D2E")
    Call(0, 12)
    Jump("loc_4DD4")

    label("loc_4D2E")


    ChrTalk(
        0xB,
        (
            "With worry of my wife and son\x01",
            "If you do not get anything,\x01",
            "I thought I should go home … but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hm, he is a professional doctor.\x01",
            "…… I do not want anything but an unnecessary worry\x01",
            "It seems to have been done.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DD4")

    Jump("loc_5828")

    label("loc_4DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4F72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ED6")

    ChrTalk(
        0xB,
        (
            "Cross Bell Cathedral,\x01",
            "With the city into the barrier\x01",
            "It is said that it was wrapped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Eldar Archbishop\x01",
            "I wanted to talk with various people … …\x01",
            "There is no way it can not be contacted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F(Archbishop Elderda ……\x01",
            "I wonder what he is doing now. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4F6D")

    label("loc_4ED6")


    ChrTalk(
        0xB,
        (
            "Eldar Archbishop\x01",
            "I wanted to talk with various people … …\x01",
            "There is no help for no contact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This is also a trial given by the goddess.\x01",
            "patient達の為にも尽力せねばな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F6D")

    Jump("loc_5828")

    label("loc_4F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_50CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5052")

    ChrTalk(
        0xB,
        (
            "The victim of the raid incident,\x01",
            "Those who are injured\x01",
            "Not only.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I was shocked by the incident,\x01",
            "It hurts the stomach in the original\x01",
            "There are many who do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The spirit and the body are very closely\x01",
            "It can be said that they are related.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_50C6")

    label("loc_5052")


    ChrTalk(
        0xB,
        (
            "By spiritual burden\x01",
            "Some people experience abnormalities in the body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The spirit and the body are very closely\x01",
            "It can be said that they are related.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50C6")

    Jump("loc_5828")

    label("loc_50CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_52B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51FF")

    ChrTalk(
        0xB,
        (
            "I used to put a scalpel on the human body before\x01",
            "Suspecting the act itself#4RThe latest#I felt something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But as the times advance and civilization develops\x01",
            "Many things can not be dealt with by internal medicine alone.\x01",
            "… … like a train accident this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Beyond working in a hospital,\x01",
            "Accepting a new form of medical treatment\x01",
            "I felt it was important once it was important.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_52AF")

    label("loc_51FF")


    ChrTalk(
        0xB,
        (
            "Put a scalpel on a person's body ……\x01",
            "It is old to refuse it,\x01",
            "It is probably a lacking flexibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Beyond working in a hospital,\x01",
            "Accepting a new form of medical treatment\x01",
            "I felt it was important once it was important.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52AF")

    Jump("loc_5828")

    label("loc_52B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_546E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53C5")

    ChrTalk(
        0xB,
        (
            "To the human body,\x01",
            "The ability to cure injuries and diseases\x01",
            "Originally equipped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Many of the medicines prescribed in internal medicine,\x01",
            "Promote this \"self healing power\"\x01",
            "It is to do treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The neighborhood in this area is in the church.\x01",
            "Based on that, our physicians\x01",
            "I am doing the operation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5469")

    label("loc_53C5")


    ChrTalk(
        0xB,
        (
            "To the human body,\x01",
            "Power to cure injuries and diseases ……\x01",
            "\"Self - healing power\" is equipped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Many of the medicines prescribed in internal medicine,\x01",
            "By promoting it\x01",
            "It is a natural treatment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5469")

    Jump("loc_5828")

    label("loc_546E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_54BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5489")
    Call(0, 12)
    Jump("loc_54BA")

    label("loc_5489")


    ChrTalk(
        0xB,
        (
            "…… Well, sorry\x01",
            "I have to cool my head.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54BA")

    Jump("loc_5828")

    label("loc_54BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_54F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54DA")
    Call(0, 12)
    Jump("loc_54F4")

    label("loc_54DA")


    ChrTalk(
        0xB,
        "This beard is okay …!\x02",
    )

    CloseMessageWindow()

    label("loc_54F4")

    Jump("loc_5828")

    label("loc_54F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5507")
    Jump("loc_5828")

    label("loc_5507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5828")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_579C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_56C1")
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "Oh, you surely\x01",
            "It was a police department special office support section.\x01",
            "No, I came to a good place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Actually, I was studying tomorrow.\x01",
            "A paper on 'Lupinas grass'\x01",
            "It is supposed to be announced at the conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I want to report to you as well.\x01",
            "It was where I was thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSpeaking of lupine grass … …\x01",
            "It was medicinal herbs that I used to handle at the request before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FCongratulations, Huhu.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, thanks to you guys.\x01",
            "I will reward you again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5794")

    label("loc_56C1")


    ChrTalk(
        0xB,
        (
            "Oh!\x01",
            "I am in charge of internal medicine\x01",
            "It is a person called Lago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Actually, I was studying tomorrow.\x01",
            "A medicinal paper called \"Lupinas grass\"\x01",
            "It is supposed to be announced at the conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Huh, I'm really honored.\x01",
            "I wish I should be in perfect condition.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5794")

    SetScenarioFlags(0x159, 7)
    Jump("loc_5828")

    label("loc_579C")


    ChrTalk(
        0xB,
        (
            "At a conference to be held in a foreign country tomorrow\x01",
            "We will publish the paper \"Lupine's Grass\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Actually, there are also important guests at the hospital … …\x01",
            "There is no coffee this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5828")

    TalkEnd(0xFE)
    Return()

    # Function_11_4A79 end

    def Function_12_582C(): pass

    label("Function_12_582C")

    OP_4B(0xB, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_59DF")

    ChrTalk(
        0xB,
        (
            "Professor Gary、君の手術は\x01",
            "I will have you act as an assistant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It was said that it was formulated freshly\x01",
            "Also prepare anesthetic medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "…… Huff.\x01",
            "Today it is also beyond the bald head\x01",
            "It seems to be shining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hun, that of you\x01",
            "There are dirty bearded surfaces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "What happened today, today\x01",
            "Like a \"dark doctor Glenn\"\x01",
            "I feel like dignity is seen.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)
    OP_64(0xE)

    ChrTalk(
        0xE,
        (
            "…… Huh, soon\x01",
            "Let's start surgery!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Umm!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EEC")

    label("loc_59DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_5BE0")

    ChrTalk(
        0xB,
        (
            "ウォッホン、Professor Gary。\x01",
            "…… That, what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Your wife and son are in Crosbell City\x01",
            "I heard he lives … ….\x01",
            "Are you getting in touch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "…… No, here's where.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I see … I'm worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "…… What did you say,\x01",
            "Negotiate with the Defense Forces\x01",
            "Why do not you go back to the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "No … … both my wife and Kentz,\x01",
            "You will be able to take care of yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "重傷patientがいつ運び込まれるか\x01",
            "Do not know, hospital\x01",
            "I can not leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "それはProfessor Lagoも同じでしょう？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "…… Umm, that's right.\x01",
            "It seems that he did not care about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EEC")

    label("loc_5BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5D5E")

    ChrTalk(
        0xB,
        (
            "Seiren's technique is\x01",
            "It is thought at the present time\x01",
            "It should have been the best one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "… … The cause of the failure of surgery,\x01",
            "Was not it your fault?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well … that you are,\x01",
            "Hand trembling in unfamiliar surgery\x01",
            "You made it mistake! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#4SWhat! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#4SDo it! Is it?\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)
    OP_64(0xE)

    ChrTalk(
        0xE,
        "…… Let's, this time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "… … That's right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EEC")

    label("loc_5D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5EEC")

    ChrTalk(
        0xB,
        (
            "Yesterday's conference,\x01",
            "My paper has been acclaimed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "No, you too\x01",
            "I wanted to see that brave figure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I also came to visit the hospital yesterday\x01",
            "Prince Albert直々に、\x01",
            "I received the words of encouragement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "\"The future development of surgical medicine\x01",
            "It's on your shoulder. \"\x01",
            "No, I really appreciate it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)
    OP_64(0xE)

    ChrTalk(
        0xB,
        "#4SDo not be in a state, this beard!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#4SThis line of words, this bald!\x02",
    )

    CloseMessageWindow()

    label("loc_5EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5EFF")
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xE, 0x10)

    label("loc_5EFF")

    SetScenarioFlags(0x2, 0)
    OP_4C(0xB, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_12_582C end

    def Function_13_5F0B(): pass

    label("Function_13_5F0B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_605D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FCA")

    ChrTalk(
        0xC,
        (
            "Because of the fear of this strange situation\x01",
            "There seems to be some people who are out of shape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In the hospital my field of mind is out of the field,\x01",
            "そういうpatientさんの相談にも\x01",
            "I have to ride as much as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6058")

    label("loc_5FCA")


    ChrTalk(
        0xC,
        "The field of mind is originally the field of church ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It depends so much on hospitals,\x01",
            "そういうpatientさんの相談にも\x01",
            "I have to ride as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6058")

    Jump("loc_6721")

    label("loc_605D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_611D")

    ChrTalk(
        0xC,
        (
            "With the help of the professors,\x01",
            "A sample of medicinal herbs kept in the research building\x01",
            "I pulled out as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's a tough time,\x01",
            "Rather than opportunistically doing nothing\x01",
            "I have to do what I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6721")

    label("loc_611D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_612B")
    Jump("loc_6721")

    label("loc_612B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6139")
    Jump("loc_6721")

    label("loc_6139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6147")
    Jump("loc_6721")

    label("loc_6147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6254")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61EF")

    ChrTalk(
        0xC,
        (
            "昨日、たくさんのpatientが\x01",
            "After working over, work through.\x01",
            "The physical strength is the limit soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "A little more\x01",
            "I'm going to take a nap for the dormitory.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_624F")

    label("loc_61EF")


    ChrTalk(
        0xC,
        (
            "Even so,\x01",
            "I have worked all the time\x01",
            "I wonder if the professor is tough …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I have to get more physical strength.\x02",
    )

    CloseMessageWindow()

    label("loc_624F")

    Jump("loc_6721")

    label("loc_6254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6262")
    Jump("loc_6721")

    label("loc_6262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_627D")
    Call(0, 37)
    Jump("loc_632F")

    label("loc_627D")


    ChrTalk(
        0xC,
        (
            "After having enjoyed the play and the stage,\x01",
            "After reexamination the disease cured …\x01",
            "I have heard such a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Maybe, recently\x01",
            "I had a good time with my grandchild\x01",
            "Perhaps it was good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_632F")

    Jump("loc_6721")

    label("loc_6334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6342")
    Jump("loc_6721")

    label("loc_6342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6681")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6536")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64A6")

    ChrTalk(
        0xC,
        (
            "Professor Joachim is in case of case\x01",
            "When I learned that it was a mastermind,\x01",
            "It's really shocking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Dr. Seyland\x01",
            "Even after I arrived as a new boss,\x01",
            "Although I was depressed for a while … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "『patientがいるかぎり、\x01",
            "There is no time to depress us. \"\x01",
            "… … so so taught me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Anyway, under the teacher's teaching\x01",
            "I intend to work hard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6531")

    label("loc_64A6")


    ChrTalk(
        0xC,
        (
            "Mr. Seyland,\x01",
            "I will work hard on me.\x01",
            "Thanks to that, I do not have time to feel depressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha, that severity also\x01",
            "It might be within the gentleness of the teacher.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6531")

    Jump("loc_667C")

    label("loc_6536")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_65E7")

    ChrTalk(
        0xC,
        (
            "The medicated medicine worked,\x01",
            "The condition has stabilized.\x01",
            "This is safe for the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even so,\x01",
            "It seems that knowledge of equivalent medicine is deep.\x01",
            "I want to learn.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_667C")

    label("loc_65E7")


    ChrTalk(
        0xC,
        (
            "大公閣下とProfessor Seyland、\x01",
            "It seems like I got acquainted from long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Professor Seylandが大公閣下に\x01",
            "Talking in the usual atmosphere,\x01",
            "Somehow I will be disappointed … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_667C")

    Jump("loc_6721")

    label("loc_6681")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6721")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_669C")
    Call(0, 39)
    Jump("loc_6721")

    label("loc_669C")


    ChrTalk(
        0xC,
        (
            "Mr. Quinn takes medicine\x01",
            "It began to drink,\x01",
            "I am also really happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "これも全て、Amisaちゃんが\x01",
            "Thanks for your hard work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6721")

    TalkEnd(0xFE)
    Return()

    # Function_13_5F0B end

    def Function_14_6725(): pass

    label("Function_14_6725")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_67CB")

    ChrTalk(
        0xD,
        (
            "patientさんがどっと入ってきて\x01",
            "I'm pretty busy, but … I will do it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Although it is still a long way now,\x01",
            "きっとProfessor Seylandみたいな\x01",
            "Because I'm going to be a female doctor!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7172")

    label("loc_67CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_684F")

    ChrTalk(
        0xD,
        (
            "Unexpectedly, the idea of folk remedies\x01",
            "It may be helpful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I should have placed it in the dormitory bookshelf\x01",
            "Let's look for it later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7172")

    label("loc_684F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_69E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6934")

    ChrTalk(
        0xD,
        (
            "Drugs provided by the Defense Force\x01",
            "I am sorting out … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Indeed, amateurs got it all together\x01",
            "It is a product line of feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In the meantime I will manage somehow,\x01",
            "難病のpatientさんがきたら\x01",
            "I can not deal with it …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_69E0")

    label("loc_6934")


    ChrTalk(
        0xD,
        (
            "Medicines that were provided by the Defense Force\x01",
            "Indeed, amateurs got it all together\x01",
            "It is a product line of feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In the meantime I will manage somehow,\x01",
            "難病のpatientさんがきたら\x01",
            "I can not deal with it …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69E0")

    Jump("loc_7172")

    label("loc_69E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6A68")

    ChrTalk(
        0xD,
        (
            "Although outpatient reception has ceased,\x01",
            "重病のpatientがいつ来るか分からないわ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Just keep preparations neat.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7172")

    label("loc_6A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6BFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B7B")

    ChrTalk(
        0xD,
        (
            "\"When the doctor is in such a situation\x01",
            "Do not show the sunken look … …. \"\x01",
            "Professor Lagoが教えてくれたの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I wish we had an uneasy face\x01",
            "patientにそれが伝染するものね。\x01",
            "You have to be careful……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "To say anxiety, in a sense\x01",
            "It might be something like a sickness\x01",
            "You do not.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6BF5")

    label("loc_6B7B")


    ChrTalk(
        0xD,
        (
            "\"When the doctor is in such a situation\x01",
            "Do not show the sunken look … …. \"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "…… I understand it with my head,\x01",
            "It might be difficult for me ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BF5")

    Jump("loc_7172")

    label("loc_6BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6D70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CEA")

    ChrTalk(
        0xD,
        (
            "If you hit the rain and get wet,\x01",
            "It's easy to catch a cold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "This is because the body will cool down\x01",
            "The immunity that I have\x01",
            "It seems to be the reason that it stops working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "When you return home,\x01",
            "Change your clothes properly\x01",
            "You must warm yourself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6D6B")

    label("loc_6CEA")


    ChrTalk(
        0xD,
        (
            "If you hit the rain and get wet,\x01",
            "It's easy to catch a cold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "When you return home,\x01",
            "Change your clothes properly\x01",
            "You must warm yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D6B")

    Jump("loc_7172")

    label("loc_6D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6E11")

    ChrTalk(
        0xD,
        (
            "Litton, somewhat recently\x01",
            "I often go to a roundtrip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Mumumu, I can not lose.\x01",
            "patientさんに信用してもらえる\x01",
            "Because I'm going to be a female doctor!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7172")

    label("loc_6E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6E1F")
    Jump("loc_7172")

    label("loc_6E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6F47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EE2")

    ChrTalk(
        0xD,
        (
            "Well, professors also\x01",
            "She seems to be fighting …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In such a case,\x01",
            "It is better not to enter the stop\x01",
            "It will end soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Even with organizing the medical record as of now\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6F42")

    label("loc_6EE2")


    ChrTalk(
        0xD,
        (
            "To the fight of the professors\x01",
            "I got used to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Even with organizing the medical record as of now\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F42")

    Jump("loc_7172")

    label("loc_6F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_701D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FCF")

    ChrTalk(
        0xD,
        (
            "After all the professor\x01",
            "That's amazing …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "…… It should not be,\x01",
            "Now what I can do\x01",
            "I have to do it properly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7018")

    label("loc_6FCF")


    ChrTalk(
        0xD,
        (
            "Even so,\x01",
            "I am merciful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I have to study more.\x02",
    )

    CloseMessageWindow()

    label("loc_7018")

    Jump("loc_7172")

    label("loc_701D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7172")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7102")

    ChrTalk(
        0xD,
        (
            "From this time, the flora of the same room in the dormitory\x01",
            "I'm looking after a rookie training doctor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I told you that Michao was … ….\x01",
            "When I was a newcomer somehow\x01",
            "I will remember.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, I am still studying\x01",
            "It does not change.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7172")

    label("loc_7102")


    ChrTalk(
        0xD,
        (
            "When I was watching Michao,\x01",
            "When I was a newcomer somehow\x01",
            "I will remember.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Well, I am still studying.\x02",
    )

    CloseMessageWindow()

    label("loc_7172")

    TalkEnd(0xFE)
    Return()

    # Function_14_6725 end

    def Function_15_7176(): pass

    label("Function_15_7176")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7214")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7194")
    Call(0, 12)
    Jump("loc_720F")

    label("loc_7194")


    ChrTalk(
        0xE,
        (
            "Professor Lagoなど嫌いだが、\x01",
            "Beyond his support\x01",
            "There is no reliable one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Huff, now any operation\x01",
            "Do not feel like doing this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_720F")

    Jump("loc_7BF3")

    label("loc_7214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_7362")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72D9")

    ChrTalk(
        0xE,
        (
            "Missing medical supplies\x01",
            "Department of Internal Medicine and Department of Neurology and Medicine\x01",
            "It seems that he is planning to try it somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "…… There is no surgery now,\x01",
            "In the intervals between the work of Asura\x01",
            "I suppose you are helping.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_735D")

    label("loc_72D9")


    ChrTalk(
        0xE,
        (
            "In the intervals between the work of Asura\x01",
            "I suppose you are helping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "When surgery can enter,\x01",
            "I have to prepare thoroughly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_735D")

    Jump("loc_7BF3")

    label("loc_7362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_7409")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_737D")
    Call(0, 12)
    Jump("loc_7404")

    label("loc_737D")


    ChrTalk(
        0xE,
        (
            "……Professor Lagoも、たまには\x01",
            "You can say something wishful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, my wife and Kenzuto\x01",
            "Surely it's okay,\x01",
            "I have not worried about you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7404")

    Jump("loc_7BF3")

    label("loc_7409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_7508")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_748D")

    ChrTalk(
        0xE,
        (
            "…… I left it in the town\x01",
            "My wife and Kenzuto\x01",
            "What is going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If you are not sick or something\x01",
            "I do not mind ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7503")

    label("loc_748D")


    ChrTalk(
        0xE,
        "…… Well, I do not care.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I have not been brought here,\x01",
            "Wife and Kenzuto must be healthy\x01",
            "There must be spending.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7503")

    Jump("loc_7BF3")

    label("loc_7508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7609")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75B8")

    ChrTalk(
        0xE,
        (
            "I have been working in a hospital for many years,\x01",
            "It's enough to fill the hospital room\x01",
            "入院patientが来たのは初めてだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It can not be said that this is an unprecedented situation.\x01",
            "I have to get over it somehow ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7604")

    label("loc_75B8")


    ChrTalk(
        0xE,
        (
            "This situation …\x01",
            "It can be said that this is an unprecedented situation.\x01",
            "I have to get over it somehow ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7604")

    Jump("loc_7BF3")

    label("loc_7609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7748")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76D3")

    ChrTalk(
        0xE,
        (
            "Fuu … …. In the past,\x01",
            "One operation has ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "何分、patientの数が多くてな。\x01",
            "The procedure took until morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "When the examination of today is over,\x01",
            "I want to sleep like mud.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7743")

    label("loc_76D3")


    ChrTalk(
        0xE,
        (
            "I was tired from surgery until morning … …\x01",
            "patientは待ってくれない。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Until today's examination is over\x01",
            "You have to be firm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7743")

    Jump("loc_7BF3")

    label("loc_7748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7897")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7819")

    ChrTalk(
        0xE,
        (
            "Recently, my son Keynts\x01",
            "It seems to be worrying about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Haha, I also have a job at the hospital\x01",
            "Anxiety runs out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "下手をすると、Professor Lagoに\x01",
            "To the treatment of stomach pain\x01",
            "Maybe it will be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7892")

    label("loc_7819")


    ChrTalk(
        0xE,
        (
            "Whew, both public and private\x01",
            "Anxiety runs out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "下手をすると、Professor Lagoに\x01",
            "To the treatment of stomach pain\x01",
            "Maybe it will be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7892")

    Jump("loc_7BF3")

    label("loc_7897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7948")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78B2")
    Call(0, 12)
    Jump("loc_7943")

    label("loc_78B2")


    ChrTalk(
        0xE,
        (
            "We also participated in surgery,\x01",
            "This time is just helplessness\x01",
            "I was made aware.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "この失敗にpatientが絶望してないか……\x01",
            "That's only a concern.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7943")

    Jump("loc_7BF3")

    label("loc_7948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_798A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7963")
    Call(0, 12)
    Jump("loc_7985")

    label("loc_7963")


    ChrTalk(
        0xE,
        "Do not get in well, do not you think?\x02",
    )

    CloseMessageWindow()

    label("loc_7985")

    Jump("loc_7BF3")

    label("loc_798A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7A9A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7A05")

    ChrTalk(
        0xE,
        "It seems that Daimyo has returned home … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Ha, well … well …\x01",
            "It is also troubling for Ella Asura.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A95")

    label("loc_7A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A17")
    Call(0, 16)
    Jump("loc_7A95")

    label("loc_7A17")


    ChrTalk(
        0xE,
        (
            "Even though Prince Dictionary is coming to visit,\x01",
            "What a pace … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "To Mr. Asura Make moxibustion moxa\x01",
            "Do not settle …!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A95")

    Jump("loc_7BF3")

    label("loc_7A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7BF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B7B")

    ChrTalk(
        0xE,
        (
            "Professor Lagoめ、どうも\x01",
            "It seems to be ecstatic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Every time I see him\x01",
            "Be proud of this in the way.\x01",
            "Totally, that bald head …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "… Well, indeed the research of\x01",
            "It is worthy of praise.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7BF3")

    label("loc_7B7B")


    ChrTalk(
        0xE,
        (
            "Professor Lagoの研究成果は\x01",
            "I will not admit it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The first eclipse of a guy does not hurt him … …\x01",
            "Hun, I will endure about this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BF3")

    TalkEnd(0xFE)
    Return()

    # Function_15_7176 end

    def Function_16_7BF7(): pass

    label("Function_16_7BF7")

    OP_4B(0xE, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xE,
        (
            "Sha, Mr. Charles,\x01",
            "Are you oversleeping ashura? Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Yeah, probably.\x01",
            "…… Yesterday late in my laboratory\x01",
            "It seems to be muzzled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Daiko to visit\x01",
            "Even though it is,\x01",
            "How sloppy ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Eee, anyhow\x01",
            "Beat up!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0x10, 0x10)
    OP_4C(0xE, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_16_7BF7 end

    def Function_17_7D07(): pass

    label("Function_17_7D07")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7E56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DB4")

    ChrTalk(
        0xF,
        (
            "A huge tree that appeared near the wetlands,\x01",
            "It's too amazing ~ …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Under what principle, for what purpose\x01",
            "Did it appear in that place …?\x01",
            "Scientific interest does not run out!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7E51")

    label("loc_7DB4")


    ChrTalk(
        0xF,
        (
            "…… Haah, it hurried out.\x01",
            "Sorry, at times like this …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "今はとにかく、patientさんの対応と\x01",
            "Maintenance of medical equipment\x01",
            "If you do not do it properly, is not it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E51")

    Jump("loc_8B3E")

    label("loc_7E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_7FB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F17")

    ChrTalk(
        0xF,
        "Frustratingly ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "When a new medical device is broken,\x01",
            "I am checking out old equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Fuaa ~ Ah … … I'm sleepy,\x01",
            "I have to do it properly … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7FAC")

    label("loc_7F17")


    ChrTalk(
        0xF,
        (
            "Frustratingly ……\x01",
            "Even so, it is old.\x01",
            "It is unexpectedly made sturdy ~ is not it ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Many of them are large and rugged,\x01",
            "I feel comfortable when I sleep on … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FAC")

    Jump("loc_8B3E")

    label("loc_7FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_813A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_809C")

    ChrTalk(
        0xF,
        (
            "Spare of deteriorated parts,\x01",
            "I managed to find it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "But it's a special part\x01",
            "Next time I must order from Remiferia\x01",
            "I do not get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Well, I'm in trouble.\x01",
            "If we do not use it carefully carefully …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8135")

    label("loc_809C")


    ChrTalk(
        0xF,
        (
            "The parts of the medical equipment used at the hospital\x01",
            "I have to order from Remiferia\x01",
            "I do not get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Well, I'm in trouble.\x01",
            "If we do not use it carefully carefully …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8135")

    Jump("loc_8B3E")

    label("loc_813A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_838F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82F9")
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xF,
        "Oh, Tio.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Now, maintenance of medical equipment\x01",
            "I'm doing it ….\x01",
            "What do you think of this number?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FHmm … … the durability is the prescribed value\x01",
            "It is slightly below it.\x02\x03",
            "#00203FPerhaps parts of the moving part\x01",
            "I wonder if it has deteriorated over time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I guess so!\x01",
            "Well, I was in trouble ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(While Tio is here,\x01",
            "She seems to be pretty familiar … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F(If it's in the field of fuhu, conducting equipment\x01",
            "You were pretty helpful, are not you? )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_838A")

    label("loc_82F9")


    ChrTalk(
        0xF,
        (
            "Well, I was in trouble.\x01",
            "I am made by Seirando\x01",
            "I can not get a new item ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "But, there is no choice but to do something.\x01",
            "Tentatively I will search for a spare.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_838A")

    Jump("loc_8B3E")

    label("loc_838F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_84BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_844A")

    ChrTalk(
        0xF,
        (
            "Well, later on in the research building\x01",
            "A round visit to the intensive care room … and.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Mr. Donovan's\x01",
            "Also for ventilator check\x01",
            "I have to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Work has increased at a stretch\x01",
            "I am really busy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_84B8")

    label("loc_844A")


    ChrTalk(
        0xF,
        (
            "Work has increased at a stretch\x01",
            "I am really busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I can return to the day of research pickling\x01",
            "It seems like the previous story ~ …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84B8")

    Jump("loc_8B3E")

    label("loc_84BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_85B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8563")

    ChrTalk(
        0xF,
        (
            "Yesterday medical devices for surgery\x01",
            "It was a great success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "From day to day Charles\x01",
            "Asking for maintenance,\x01",
            "It was really good ~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_85AD")

    label("loc_8563")


    ChrTalk(
        0xF,
        (
            "The resident doctors\x01",
            "Only good talented people,\x01",
            "I am helped too ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85AD")

    Jump("loc_8B3E")

    label("loc_85B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8743")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86C0")

    ChrTalk(
        0xF,
        (
            "Utsura, depressed … …\x01",
            "…… Oh yeah!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Applying the principle of photosensitive quartz\x01",
            "If you create a mechanism to send visual information to the brain\x01",
            "It may be possible to assist visual acuity pseudo …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "(Kata kata kata kata kata kata … …)\x01",
            "…… Well, after all not.\x01",
            "In this case it takes decades for development …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_873E")

    label("loc_86C0")


    ChrTalk(
        0xF,
        (
            "No …\x01",
            "After all it may be irritating to me ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "…… No, I will not give up.\x01",
            "Fight for Shizuku-chan, I!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_873E")

    Jump("loc_8B3E")

    label("loc_8743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_88AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8822")

    ChrTalk(
        0xF,
        (
            "For the operation of Shizuku,\x01",
            "Equipment that can be said to be the best in modern medicine\x01",
            "I felt after preparing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It will not fail …\x01",
            "Wow, I do not get convinced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "To Shizuku who believed in me\x01",
            "I'm sorry……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_88A7")

    label("loc_8822")


    ChrTalk(
        0xF,
        (
            "Science makes people happy …\x01",
            "For that I am in the Department of Medical Devices\x01",
            "I have continued my research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "To Shizuku who believed in me\x01",
            "I'm sorry……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88A7")

    Jump("loc_8B3E")

    label("loc_88AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_896C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88C7")
    Call(0, 18)
    Jump("loc_8967")

    label("loc_88C7")

    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xF,
        (
            "…… Yes, a good success!\x01",
            "It seems that this time it worked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Huhu, today is in this condition\x01",
            "I have to proceed to the durability test.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "(Will it be a penetration course today? …)\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)

    label("loc_8967")

    Jump("loc_8B3E")

    label("loc_896C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_897A")
    Jump("loc_8B3E")

    label("loc_897A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8B3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AA5")

    ChrTalk(
        0xF,
        (
            "Professor Seylandが\x01",
            "When I heard that I will be assigned to my place here,\x01",
            "It seemed like they were going to jump.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Professional design, leading medical equipment manufacturer\x01",
            "The name \"Seirando\" is\x01",
            "I saw it everyday, hey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "She seems to be the relatives of the president … …\x01",
            "Uhufu, the company's story behind\x01",
            "I hope you can tell me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8B3E")

    label("loc_8AA5")


    ChrTalk(
        0xF,
        (
            "でも、Professor Seylandって\x01",
            "It is kind of cool, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Story of Seyland\x01",
            "I'd like to ask you various things ….\x01",
            "Timing is hard to grasp.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B3E")

    TalkEnd(0xFE)
    Return()

    # Function_17_7D07 end

    def Function_18_8B42(): pass

    label("Function_18_8B42")

    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xF,
        (
            "Well, Charles.\x01",
            "Prepare to get ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Because I put a switch,\x01",
            "Please adjust the guide pressure.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    ChrTalk(
        0x10,
        (
            "It is okay.\x01",
            "…… I have to explode now\x01",
            "Sounds good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I do not mind ♪\x01",
            "Failure is a mother of success.\x02",
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
            "#00211F(… … It is not wrong,\x01",
            "It is dangerous. )\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x2, 2)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_93(0x10, 0x5A, 0x0)
    Return()

    # Function_18_8B42 end

    def Function_19_8CDB(): pass

    label("Function_19_8CDB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8E2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DAD")

    ChrTalk(
        0x10,
        (
            "The boss seemed to be sleepy for a while,\x01",
            "Since I saw the appearance of that tree\x01",
            "It's that tension forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If Oh, the boss will be three days and three nights\x01",
            "It will be full operation.\x01",
            "I have to keep going.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8E26")

    label("loc_8DAD")


    ChrTalk(
        0x10,
        (
            "Empire's civil war,\x01",
            "That pale big tree …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "There are various worries,\x01",
            "Now I am going to follow the leader\x01",
            "Let's concentrate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E26")

    Jump("loc_9A6D")

    label("loc_8E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_8F60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EF2")

    ChrTalk(
        0x10,
        (
            "Hmm, the performance is indeed low\x01",
            "When it comes to emergency, substitution seems to be good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Because there are a lot of overnight checks\x01",
            "I have become ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "… Well, because it's usual thing?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8F5B")

    label("loc_8EF2")


    ChrTalk(
        0x10,
        (
            "Because it was overnight check,\x01",
            "Director Ashraも眠そうだな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "… Well, because it's usual thing?\x02",
    )

    CloseMessageWindow()

    label("loc_8F5B")

    Jump("loc_9A6D")

    label("loc_8F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_901E")

    ChrTalk(
        0x10,
        (
            "Professor Garyも家族の心配は\x01",
            "There would be a hospital's job\x01",
            "It seems to be very concentrated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "…… I also believe in family safety,\x01",
            "今はDirector Ashraの手伝いに\x01",
            "I will decide to get in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A6D")

    label("loc_901E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_91B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_913B")

    ChrTalk(
        0x10,
        (
            "Just before Crossbell independence,\x01",
            "Although a notice of withdrawal came from the empire\x01",
            "I decided to stay here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I still have to learn\x01",
            "Although there is a thing, to my hometown\x01",
            "I can not go home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "…… But it happened in the empire\x01",
            "I am a bit worried about the civil war.\x01",
            "I hope my family is safe, but …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_91B1")

    label("loc_913B")


    ChrTalk(
        0x10,
        (
            "To the things that remained in the crossbell itself\x01",
            "I regret not at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "… But, I am worried about the empire's civil war.\x01",
            "I hope my family is safe, but …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91B1")

    Jump("loc_9A6D")

    label("loc_91B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9308")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_928F")

    ChrTalk(
        0x10,
        (
            "In this raid incident,\x01",
            "As a conspiracy by the Imperial government\x01",
            "I heard whispered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "A lot of people were brought into the hospital\x01",
            "That affair is the work of the empire …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I do not want to say badly about my hometown,\x01",
            "I will despise if true.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9303")

    label("loc_928F")


    ChrTalk(
        0x10,
        (
            "In the future, in the hometown empire\x01",
            "Although my goal was to start business … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If the Imperial government's plot is true,\x01",
            "I despise my hometown.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9303")

    Jump("loc_9A6D")

    label("loc_9308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_944C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93FB")

    ChrTalk(
        0x10,
        (
            "Medical equipment from daily\x01",
            "Fine maintenance\x01",
            "It is indispensable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If the medical device breaks down\x01",
            "patientになにかあったりしたら\x01",
            "It's toppled over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "またいつpatientが\x01",
            "As it is good to be carried,\x01",
            "I have to keep it properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9447")

    label("loc_93FB")


    ChrTalk(
        0x10,
        (
            "またいつpatientが\x01",
            "As it is good to be carried,\x01",
            "I have to keep it properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9447")

    Jump("loc_9A6D")

    label("loc_944C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_95D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_953F")

    ChrTalk(
        0x10,
        (
            "From the operation of Shizuku-chan\x01",
            "I am researching something with insomnia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Apparently, using a guide\x01",
            "How to cure Shizuku's eyes\x01",
            "She seems to be exploring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "After all the chief is amazing … …\x01",
            "I did not think about that either.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_95CB")

    label("loc_953F")


    ChrTalk(
        0x10,
        (
            "Do you recover your eyesight with a guiding … ….\x01",
            "I did not think about that either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "However, it also involves the field of neurology … …\x01",
            "Realization may be difficult.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95CB")

    Jump("loc_9A6D")

    label("loc_95D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9723")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96A6")

    ChrTalk(
        0x10,
        (
            "Regarding that surgery, the professors\x01",
            "I think that everyone did their best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Still it did not reach complete recovery\x01",
            "I'm obliged to say sorry, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Personally, do not get too depressed\x01",
            "It is a place I want.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_971E")

    label("loc_96A6")


    ChrTalk(
        0x10,
        (
            "Regarding that surgery, the professors\x01",
            "I think that everyone did their best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Personally, do not get too depressed\x01",
            "It is a place I want.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_971E")

    Jump("loc_9A6D")

    label("loc_9723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_97BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_973E")
    Call(0, 18)
    Jump("loc_97BA")

    label("loc_973E")


    ChrTalk(
        0x10,
        (
            "Director Ashraは\x01",
            "No matter how much I fail, I can not afford it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Respect as a researcher of medical equipment,\x01",
            "You may have to learn a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97BA")

    Jump("loc_9A6D")

    label("loc_97BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_98F1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9864")

    ChrTalk(
        0x10,
        (
            "結局Director Ashraは\x01",
            "I could not make it in time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Well, the boss who stayed up all night yesterday\x01",
            "To be in time for the tour,\x01",
            "I did not even think about this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98EC")

    label("loc_9864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9876")
    Call(0, 16)
    Jump("loc_98EC")

    label("loc_9876")


    ChrTalk(
        0x10,
        (
            "Director Ashraは、夜を徹して\x01",
            "I often encourage research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I'm still sleeping in the dormitory now\x01",
            "I guess they are in the middle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98EC")

    Jump("loc_9A6D")

    label("loc_98F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9A6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99F5")

    ChrTalk(
        0x10,
        (
            "Director Ashraは\x01",
            "It is a medical equipment expert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Formerly the boss's hometown\x01",
            "At the Epstein Foundation headquarters in Leman Autonomous Region\x01",
            "It seems that he was learning the basics of guiding equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I am under such a boss,\x01",
            "Research on various medical devices\x01",
            "I am helping you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9A6D")

    label("loc_99F5")


    ChrTalk(
        0x10,
        (
            "Medical equipment in modern medicine\x01",
            "It is indispensable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I believe this research\x01",
            "I believe it will open up the future of medicine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A6D")

    TalkEnd(0xFE)
    Return()

    # Function_19_8CDB end

    def Function_20_9A71(): pass

    label("Function_20_9A71")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9AEB")

    ChrTalk(
        0x11,
        "Zoei rest assured that outpatient reception will resume.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "The medicine that I got before was out\x01",
            "I thought of what to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DF3")

    label("loc_9AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9AF9")
    Jump("loc_9DF3")

    label("loc_9AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9B07")
    Jump("loc_9DF3")

    label("loc_9B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9BA7")

    ChrTalk(
        0x11,
        (
            "Hmm, when you look at the unlikely place called …\x01",
            "The examination seems to be rather stagnant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "There was such a raid incident,\x01",
            "Teachers are also pretty busy …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DF3")

    label("loc_9BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9BB5")
    Jump("loc_9DF3")

    label("loc_9BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9C30")

    ChrTalk(
        0x11,
        "I have a reservation today in the morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I used a conductivity net for my reservation,\x01",
            "It is still convenient.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DF3")

    label("loc_9C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9C3E")
    Jump("loc_9DF3")

    label("loc_9C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9D42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CE6")

    ChrTalk(
        0x11,
        (
            "In the unveiling ceremony yesterday\x01",
            "That Orkis Tower\x01",
            "I was looking up … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "The elongation of the back has passed.\x01",
            "I carelessly got a waist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Oh, okay …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9D3D")

    label("loc_9CE6")


    ChrTalk(
        0x11,
        (
            "Looking up at the Orchis Tower,\x01",
            "I carelessly got a waist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Oh, okay …\x02",
    )

    CloseMessageWindow()

    label("loc_9D3D")

    Jump("loc_9DF3")

    label("loc_9D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9D50")
    Jump("loc_9DF3")

    label("loc_9D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9DF3")

    ChrTalk(
        0x11,
        (
            "After the case incident,\x01",
            "The hospital conducts a prompt investigation\x01",
            "It proved that innocence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Thus with confidence\x01",
            "I was able to visit the hospital,\x01",
            "It is truly appreciated.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DF3")

    TalkEnd(0xFE)
    Return()

    # Function_20_9A71 end

    def Function_21_9DF7(): pass

    label("Function_21_9DF7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9E8F")

    ChrTalk(
        0x12,
        (
            "For us old people,\x01",
            "Whether there is an environment where you can go to the hospital\x01",
            "It is very important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "In this way it came to come,\x01",
            "It was really nice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A148")

    label("loc_9E8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9E9D")
    Jump("loc_A148")

    label("loc_9E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9EAB")
    Jump("loc_A148")

    label("loc_9EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9F0A")

    ChrTalk(
        0x12,
        (
            "Haa … … Crossbell\x01",
            "I wonder if it is okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "I can not sleep at night because I am anxious …\x02",
    )

    CloseMessageWindow()
    Jump("loc_A148")

    label("loc_9F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9F76")

    ChrTalk(
        0x12,
        (
            "It is a train accident ……\x01",
            "I was really surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Passengers everyone\x01",
            "I wonder if it was all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A148")

    label("loc_9F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9F84")
    Jump("loc_A148")

    label("loc_9F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A006")

    ChrTalk(
        0x12,
        (
            "Well, at this hospital\x01",
            "I have been in the hospital for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "The teachers are also good at surgery,\x01",
            "I'm guaranteed to get through you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A148")

    label("loc_A006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A014")
    Jump("loc_A148")

    label("loc_A014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A0A5")

    ChrTalk(
        0x12,
        (
            "My mentor Lago,\x01",
            "It seems to be a day off today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Professor Seyland\x01",
            "I am young as a professor,\x01",
            "I wonder if it's all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A148")

    label("loc_A0A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A148")

    ChrTalk(
        0x12,
        (
            "Mr. Joachim is a cheap\x01",
            "Too big incident happened,\x01",
            "I still can not believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Oh, scary scary ……\x01",
            "I do not know what people are thinking\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A148")

    TalkEnd(0xFE)
    Return()

    # Function_21_9DF7 end

    def Function_22_A14C(): pass

    label("Function_22_A14C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A221")

    ChrTalk(
        0x13,
        (
            "Before President Dieter was detained,\x01",
            "I am a little sick\x01",
            "I did not let you go to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "But children's illness for parents\x01",
            "It is a big deal if it is a cold.\x01",
            "He wanted compassion a bit more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A595")

    label("loc_A221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_A22F")
    Jump("loc_A595")

    label("loc_A22F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A23D")
    Jump("loc_A595")

    label("loc_A23D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A296")

    ChrTalk(
        0x13,
        "Look here … be quiet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "To others\x01",
            "Do not bother trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A595")

    label("loc_A296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A32F")

    ChrTalk(
        0x13,
        (
            "On the train we derailed\x01",
            "I was on a ride ……\x01",
            "Luckily good at minor injuries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I'm glad I could leave the hospital in a day,\x01",
            "I wonder what has become of the railroad since then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A595")

    label("loc_A32F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A33D")
    Jump("loc_A595")

    label("loc_A33D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A49E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A42F")

    ChrTalk(
        0x13,
        (
            "In the meantime, with a human dog\x01",
            "If you eat too much sweets\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "It is bad for your body if you keep it like this,\x01",
            "I am reviewing my lifestyle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "However, sweets are said\x01",
            "A little hand comes out.\x01",
            "You have to be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A499")

    label("loc_A42F")


    ChrTalk(
        0x13,
        (
            "Sweet things\x01",
            "A little hand comes out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "It's about my body,\x01",
            "You must be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A499")

    Jump("loc_A595")

    label("loc_A49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A4AC")
    Jump("loc_A595")

    label("loc_A4AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A58C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A525")

    ChrTalk(
        0x13,
        "Well, I smell good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "こういうのでpatientの気持ちを\x01",
            "I guess they are softening.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    ClearChrFlags(0x13, 0x10)
    Jump("loc_A587")

    label("loc_A525")


    ChrTalk(
        0x13,
        (
            "With your mum\x01",
            "I am in the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "There are many unusual items,\x01",
            "I guess I'll try exploring again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A587")

    Jump("loc_A595")

    label("loc_A58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A595")

    label("loc_A595")

    TalkEnd(0xFE)
    Return()

    # Function_22_A14C end

    def Function_23_A599(): pass

    label("Function_23_A599")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A620")

    ChrTalk(
        0x14,
        (
            "I finally came to the hospital,\x01",
            "It's very crowded …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Teachers are also serious,\x01",
            "Please let me do its best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A954")

    label("loc_A620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_A62E")
    Jump("loc_A954")

    label("loc_A62E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A63C")
    Jump("loc_A954")

    label("loc_A63C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A64A")
    Jump("loc_A954")

    label("loc_A64A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A6D7")

    ChrTalk(
        0x14,
        (
            "Even so,\x01",
            "It was a terrible accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "What happened with a sudden thing\x01",
            "I do not know … ….\x01",
            "What on earth was the cause?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A954")

    label("loc_A6D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A76E")

    ChrTalk(
        0x14,
        (
            "If you are doing housework\x01",
            "Please hurt your back.\x01",
            "I do not really want to get old.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "You should be careful too.\x01",
            "Because 30 and 40 are soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A954")

    label("loc_A76E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A77C")
    Jump("loc_A954")

    label("loc_A77C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A7F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A797")
    Call(0, 24)
    Jump("loc_A7ED")

    label("loc_A797")


    ChrTalk(
        0x14,
        (
            "Well, really.\x01",
            "I have a runny nose to stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Until the turn comes\x01",
            "Please keep still.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7ED")

    Jump("loc_A954")

    label("loc_A7F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A800")
    Jump("loc_A954")

    label("loc_A800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A954")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8D4")

    ChrTalk(
        0x14,
        (
            "Recently, explanation of medicine\x01",
            "It was more detailed than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "私たちpatientが安心できるようにって\x01",
            "I wonder why … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "To be honest, it is a component\x01",
            "To amateurs it is Ginza.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_A954")

    label("loc_A8D4")


    ChrTalk(
        0x14,
        (
            "Recently, explanation of medicine\x01",
            "It was more detailed than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "The contents are Ganban, but ……\x01",
            "Well I guess I can relieve him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A954")

    TalkEnd(0xFE)
    Return()

    # Function_23_A599 end

    def Function_24_A958(): pass

    label("Function_24_A958")


    ChrTalk(
        0x14,
        (
            "Well, I still have a fever,\x01",
            "A runny nose will not stop as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Look, my mum handkerchief\x01",
            "Try to be a teenager.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#4S… …. CHAN!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "… … It came out.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Return()

    # Function_24_A958 end

    def Function_25_A9F1(): pass

    label("Function_25_A9F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AA78")

    ChrTalk(
        0x15,
        (
            "To visit my hospitalized friend\x01",
            "Finally I was able to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "He was also a subtle one,\x01",
            "I want to chat variously.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC16")

    label("loc_AA78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_AA86")
    Jump("loc_AC16")

    label("loc_AA86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_AA94")
    Jump("loc_AC16")

    label("loc_AA94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_AB0E")

    ChrTalk(
        0x15,
        (
            "Even my nigga,\x01",
            "I was involved in an attack incident\x01",
            "I am in the hospital ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "I hope it will get better soon …\x02",
    )

    CloseMessageWindow()
    Jump("loc_AC16")

    label("loc_AB0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AB1C")
    Jump("loc_AC16")

    label("loc_AB1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_AB2A")
    Jump("loc_AC16")

    label("loc_AB2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_ABA4")

    ChrTalk(
        0x15,
        (
            "The initial examination is postponement.\x01",
            "It will be a while until the turn comes\x01",
            "It seems to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Oh, hospital is too bad.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AC16")

    label("loc_ABA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_ABFF")

    ChrTalk(
        0x15,
        "My stomach hurts …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Also think about nurse\x01",
            "To distract herself ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC16")

    label("loc_ABFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_AC0D")
    Jump("loc_AC16")

    label("loc_AC0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_AC16")

    label("loc_AC16")

    TalkEnd(0xFE)
    Return()

    # Function_25_A9F1 end

    def Function_26_AC1A(): pass

    label("Function_26_AC1A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_ACAB")

    ChrTalk(
        0x16,
        "I came to pick up a mother who is leaving the hospital today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "For a while from the hospital\x01",
            "It seems I could not get out,\x01",
            "I'd like to take him home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF31")

    label("loc_ACAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_ACB9")
    Jump("loc_AF31")

    label("loc_ACB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_ACC7")
    Jump("loc_AF31")

    label("loc_ACC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_ACD5")
    Jump("loc_AF31")

    label("loc_ACD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AE26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD7F")

    ChrTalk(
        0x16,
        (
            "I heard rumors in the city ….\x01",
            "When I get a train accident, my body can not be known.\x01",
            "It seems that a huge monster has appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Perhaps it is\x01",
            "I wonder if it was the cause of the accident ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_AE21")

    label("loc_AD7F")


    ChrTalk(
        0x16,
        (
            "I heard rumors in the city ….\x01",
            "When I get a train accident, my body can not be known.\x01",
            "It seems that a huge monster has appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "…… If such a thing comes out\x01",
            "To us common people\x01",
            "There is no way to deal with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE21")

    Jump("loc_AF31")

    label("loc_AE26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_AE34")
    Jump("loc_AF31")

    label("loc_AE34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AEC7")

    ChrTalk(
        0x16,
        (
            "Before the consultation room, somewhat\x01",
            "Teachers seem to be fighting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "If you look closely, people in the hospital will also\x01",
            "It feels kind of dark … …\x01",
            "I wonder what happened.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF31")

    label("loc_AEC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_AED5")
    Jump("loc_AF31")

    label("loc_AED5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_AF28")

    ChrTalk(
        0x16,
        "Alright, quietly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "My sister is behind\x01",
            "I will look it up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF31")

    label("loc_AF28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_AF31")

    label("loc_AF31")

    TalkEnd(0xFE)
    Return()

    # Function_26_AC1A end

    def Function_27_AF35(): pass

    label("Function_27_AF35")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AF6B")

    ChrTalk(
        0x17,
        (
            "Are you waiting?\x01",
            "I got tired.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0A1")

    label("loc_AF6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_AF79")
    Jump("loc_B0A1")

    label("loc_AF79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_AF87")
    Jump("loc_B0A1")

    label("loc_AF87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_AFD5")

    ChrTalk(
        0x17,
        "Ah, boring ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "I hope the order will come soon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0A1")

    label("loc_AFD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AFE3")
    Jump("loc_B0A1")

    label("loc_AFE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_AFF1")
    Jump("loc_B0A1")

    label("loc_AFF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AFFF")
    Jump("loc_B0A1")

    label("loc_AFFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B00D")
    Jump("loc_B0A1")

    label("loc_B00D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B05B")

    ChrTalk(
        0x17,
        "Oooh, I'm scared of injection! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "My house, frog ~ ~!\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0A1")

    label("loc_B05B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B0A1")

    ChrTalk(
        0x17,
        (
            "Fa\x01",
            "I got tired of waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Order still ~?\x02",
    )

    CloseMessageWindow()

    label("loc_B0A1")

    TalkEnd(0xFE)
    Return()

    # Function_27_AF35 end

    def Function_28_B0A5(): pass

    label("Function_28_B0A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B0E7")

    ChrTalk(
        0x18,
        (
            "Keigeni …\x01",
            "If it is a medicine doctor, it is unreasonable ~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1E4")

    label("loc_B0E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_B0F5")
    Jump("loc_B1E4")

    label("loc_B0F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B103")
    Jump("loc_B1E4")

    label("loc_B103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B111")
    Jump("loc_B1E4")

    label("loc_B111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B11F")
    Jump("loc_B1E4")

    label("loc_B11F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B17A")

    ChrTalk(
        0x18,
        (
            "Today, alone\x01",
            "I got on the bus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "Eh, are you choosy?\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1E4")

    label("loc_B17A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B188")
    Jump("loc_B1E4")

    label("loc_B188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B1CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1A3")
    Call(0, 24)
    Jump("loc_B1C8")

    label("loc_B1A3")


    ChrTalk(
        0x18,
        (
            "Rust\x01",
            "Hana is bound for … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1C8")

    Jump("loc_B1E4")

    label("loc_B1CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B1DB")
    Jump("loc_B1E4")

    label("loc_B1DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B1E4")

    label("loc_B1E4")

    TalkEnd(0xFE)
    Return()

    # Function_28_B0A5 end

    def Function_29_B1E8(): pass

    label("Function_29_B1E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B265")

    ChrTalk(
        0x19,
        (
            "The city ……\x01",
            "The city was burning …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "It was a terrible sight …\x01",
            "It's like a dispute several decades ago\x01",
            "You seem to remember … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B265")

    TalkEnd(0xFE)
    Return()

    # Function_29_B1E8 end

    def Function_30_B269(): pass

    label("Function_30_B269")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B2B2")

    ChrTalk(
        0x1A,
        "Uuu……\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems to have been hurt.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_B2B2")

    TalkEnd(0xFE)
    Return()

    # Function_30_B269 end

    def Function_31_B2B6(): pass

    label("Function_31_B2B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B324")

    ChrTalk(
        0x1B,
        (
            "Uu … … In that raid incident\x01",
            "Both legs broke fracture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Damn it …\x01",
            "Why did I look like this …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B324")

    TalkEnd(0xFE)
    Return()

    # Function_31_B2B6 end

    def Function_32_B328(): pass

    label("Function_32_B328")

    TalkBegin(0xFE)

    ChrTalk(
        0x1C,
        (
            "Well then,\x01",
            "そっちの共和国のpatientさんの\x01",
            "Please contact your family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "私はProfessor Seylandに\x01",
            "I will deliver the chart.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_B328 end

    def Function_33_B3A4(): pass

    label("Function_33_B3A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3D3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3D3")
    Call(0, 48)
    Return()

    label("loc_B3D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B637")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B57C")

    ChrTalk(
        0x1D,
        (
            "I heard it with rumors of the wind … …\x01",
            "The eye of Shizuku McClein\x01",
            "You heard it was being cured completely?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "As a former doctor\x01",
            "Perhaps it should be rejoiced … …\x01",
            "It is also a complex mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "As far as this series of cases is concerned,\x01",
            "There is something mysterious power in her eyes\x01",
            "It can be seen as being used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "As a person engaged in modern medicine,\x01",
            "To take a delay on such things\x01",
            "However, as long as it is frustrating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Sorry, forget it.\x01",
            "It is like a desperate nature.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_B632")

    label("loc_B57C")


    ChrTalk(
        0x1D,
        (
            "Sorry, forget it.\x01",
            "As a person engaged in modern medicine,\x01",
            "It is like a desperate nature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "The eye of Shizuku McClein\x01",
            "The fact that healed itself is a pleasure.\x01",
            "Let me be blessed obediently.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B632")

    Jump("loc_BD9E")

    label("loc_B637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_B645")
    Jump("loc_BD9E")

    label("loc_B645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_B653")
    Jump("loc_BD9E")

    label("loc_B653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B661")
    Jump("loc_BD9E")

    label("loc_B661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B8CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B8C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B68D")
    Call(0, 35)
    Jump("loc_B8C0")

    label("loc_B68D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B79D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B734")

    ChrTalk(
        0x1D,
        (
            "For now,\x01",
            "襲撃事件のpatientたちに\x01",
            "You will be able to respond adequately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Medical supplies you recovered\x01",
            "Let's say you want to make effective use.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_B798")

    label("loc_B734")


    ChrTalk(
        0x1D,
        (
            "Now……\x01",
            "そろそろ次のpatientの手術だ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Medical supplies you recovered\x01",
            "Let's make effective use.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B798")

    Jump("loc_B8C0")

    label("loc_B79D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_B833")

    ChrTalk(
        0x1D,
        (
            "Medical supplies in this situation\x01",
            "That it was stolen,\x01",
            "It certainly hurts … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I can not stop spiraling out.\x01",
            "There seems to be no choice but to manage somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B8C0")

    label("loc_B833")


    ChrTalk(
        0x1D,
        (
            "…… Medical supplies are not enough\x01",
            "This situation is hard to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "At times, explain the circumstances\x01",
            "I only have to send me alternative supplies\x01",
            "There must be no.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B8C0")

    Jump("loc_B8C5")

    label("loc_B8C5")

    Jump("loc_BD9E")

    label("loc_B8CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B9B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B97E")
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x1D,
        (
            "Litton,\x01",
            "次はpatientたちの回診に向かうぞ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "今回の事故はpatientが多い。\x01",
            "Saying that the operation is over\x01",
            "Do not get out of my mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Wait!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x1, 6)
    Jump("loc_B9B3")

    label("loc_B97E")


    ChrTalk(
        0x1D,
        (
            "今回の事故はpatientが多い。\x01",
            "Do not get out of my mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9B3")

    Jump("loc_BD9E")

    label("loc_B9B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B9C6")
    Jump("loc_BD9E")

    label("loc_B9C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B9D4")
    Jump("loc_BD9E")

    label("loc_B9D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B9E2")
    Jump("loc_BD9E")

    label("loc_B9E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_BD95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB25")

    ChrTalk(
        0x1D,
        (
            "Albert ……\x01",
            "After the visit is over\x01",
            "She seems to be here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Now refraining from plenary session to tomorrow,\x01",
            "Come to visit my site\x01",
            "The necessity would be low.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Whew ……\x01",
            "That man is as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(A, Albert ……\x01",
            "Are you going to forget it? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F(Are you acquainted or something ……)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_BB8E")

    label("loc_BB25")


    ChrTalk(
        0x1D,
        (
            "Albert,\x01",
            "After the visit is over\x01",
            "She seems to be here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Whew ……\x01",
            "That man is as usual.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_BD90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCD6")

    ChrTalk(
        0x1D,
        (
            "\"Riboten poisoning\" is foreign\x01",
            "As it is caused by mushrooms, itself\x01",
            "It is a case hard to occur in crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I thought about the possibilities in various ways,\x01",
            "Albert's knowledge which I gave in one word is\x01",
            "It can be said that it is considerably deep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "This time I have borrowed … …\x01",
            "It is a person who bundles Remiferia temporarily,\x01",
            "It must be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_BD90")

    label("loc_BCD6")


    ChrTalk(
        0x1D,
        (
            "\"Ribotene poisoning\"\x01",
            "Albert's knowledge which I gave in one word is\x01",
            "It can be said that it is considerably deep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "This time I have borrowed … …\x01",
            "It is a person who bundles Remiferia temporarily,\x01",
            "It must be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD90")

    Jump("loc_BD9E")

    label("loc_BD95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BD9E")

    label("loc_BD9E")

    TalkEnd(0xFE)
    Return()

    # Function_33_B3A4 end

    def Function_34_BDA2(): pass

    label("Function_34_BDA2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BE57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDD1")
    Call(0, 35)
    Jump("loc_BE52")

    label("loc_BDD1")


    ChrTalk(
        0x1E,
        (
            "Medical supplies delivered to the airport\x01",
            "\"Rhys Trucking\"\x01",
            "It is a way to carry me ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Well, something wrong\x01",
            "Was there something wrong?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE52")

    Jump("loc_BE57")

    label("loc_BE57")

    TalkEnd(0xFE)
    Return()

    # Function_34_BDA2 end

    def Function_35_BE5B(): pass

    label("Function_35_BE5B")

    OP_4B(0x1E, 0xFF)
    OP_4B(0x1D, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x1D,
        (
            "…… from Remiferia\x01",
            "I do not get medical supplies yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Yes, the expected arrival time of baggage\x01",
            "I am a long time ago ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even if something goes wrong\x01",
            "Was there something ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Hmm, in Remiferia or the airport\x01",
            "It may be something.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1E, 0x10)
    SetScenarioFlags(0x18F, 0)
    OP_4C(0x1E, 0xFF)
    OP_4C(0x1D, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_35_BE5B end

    def Function_36_BF64(): pass

    label("Function_36_BF64")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF79")
    Call(0, 37)
    Jump("loc_BFF9")

    label("loc_BF79")


    ChrTalk(
        0x1F,
        (
            "Honestly wondering what I should say,\x01",
            "I went to visit Yiya … …\x01",
            "I wonder what it will be like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "これも全てAmisaのおかげじゃ。\x02",
    )

    CloseMessageWindow()

    label("loc_BFF9")

    TalkEnd(0xFE)
    Return()

    # Function_36_BF64 end

    def Function_37_BFFD(): pass

    label("Function_37_BFFD")

    OP_4B(0x1F, 0xFF)
    OP_4B(0x20, 0xFF)

    ChrTalk(
        0xC,
        "Hmm, I was surprised at this … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Quine,\x01",
            "More than when I was in the hospital\x01",
            "The symptoms are getting better.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1F,
        "Well, is it true? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah, but of course\x01",
            "I do not need to see the progress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Just at least\x01",
            "There seems to be no need for hospitalization.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x20,
        "That's good, Grandpa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Your body is getting better!\x01",
            "You do not have to be hospitalized for it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Oh, oh … that's right.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1F, 0x10)
    ClearChrFlags(0x20, 0x10)
    SetScenarioFlags(0x2, 4)
    OP_4C(0x1F, 0xFF)
    OP_4C(0x20, 0xFF)
    Return()

    # Function_37_BFFD end

    def Function_38_C1DC(): pass

    label("Function_38_C1DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C270")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1FA")
    Call(0, 37)
    Jump("loc_C26B")

    label("loc_C1FA")


    ChrTalk(
        0x20,
        (
            "It was truly really good,\x01",
            "Grandpa!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Huhuu, after all\x01",
            "Have your medicine taken properly\x01",
            "It was a correct answer ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C26B")

    Jump("loc_C2C9")

    label("loc_C270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C2C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C28B")
    Call(0, 39)
    Jump("loc_C2C9")

    label("loc_C28B")


    ChrTalk(
        0x20,
        (
            "Today too\x01",
            "In the place of my grandfather\x01",
            "Take your medicine ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2C9")

    TalkEnd(0xFE)
    Return()

    # Function_38_C1DC end

    def Function_39_C2CD(): pass

    label("Function_39_C2CD")

    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "それじゃ、Amisaちゃん。\x01",
            "I always wrapped her medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Take care and take it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Well.\x01",
            "Thank you always, teacher.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x20, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x2, 3)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_39_C2CD end

    def Function_40_C369(): pass

    label("Function_40_C369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C398")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C398")
    Call(0, 48)
    Return()

    label("loc_C398")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_40_C369 end

    def Function_41_C39F(): pass

    label("Function_41_C39F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3BE")
    Call(0, 48)
    Return()

    label("loc_C3BE")

    TalkBegin(0xFE)

    ChrTalk(
        0x22,
        (
            "Noderia mushroom\x01",
            "I'm waiting to bring it.\x02\x03",
            "君たちとArios君なら\x01",
            "I'm sure you will achieve it.\x01",
            "Please, I beg you.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_C39F end

    def Function_42_C442(): pass

    label("Function_42_C442")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C59E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C516")

    ChrTalk(
        0x24,
        (
            "To foreign souvenirs\x01",
            "Mushrooms that I brought back,\x01",
            "It was really tasty ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "To be sure it was a poisonous mushroom,\x01",
            "It was careless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "In the future a bit more,\x01",
            "I should be careful …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C599")

    label("loc_C516")


    ChrTalk(
        0x24,
        (
            "To foreign souvenirs\x01",
            "Mushrooms that I brought back,\x01",
            "It was really tasty ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "In the future a bit more,\x01",
            "I should be careful …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C599")

    Jump("loc_C626")

    label("loc_C59E")


    ChrTalk(
        0x24,
        (
            "Uuu……\x01",
            "The stomachache has become somewhat hidden … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "After all, I ate with an airship.\x01",
            "I wish it was not good …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "Ugging ………………\x02",
    )

    CloseMessageWindow()

    label("loc_C626")

    TalkEnd(0xFE)
    Return()

    # Function_42_C442 end

    def Function_43_C62A(): pass

    label("Function_43_C62A")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_43_C62A end

    def Function_44_C631(): pass

    label("Function_44_C631")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C833")

    ChrTalk(
        0xFE,
        (
            "I could not go to the hospital by regulation\x01",
            "patientたちの搬送を手伝ってるの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since there are quite a few numbers,\x01",
            "How many round trips are there today?\x01",
            "I guess I should do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIt seems quite tough …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FPlease do not push yourself too much.\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Oh, from Tio\x01",
            "I can not accept such words …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though it is always a cool reaction,\x01",
            "I guess this is a rumorous couple! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00211F(… gradually with Roberts chief\x01",
            "It looks like a similar one. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BB, 2)
    Jump("loc_C90C")

    label("loc_C833")


    ChrTalk(
        0xFE,
        (
            "Okay … … From Tio\x01",
            "It was something I was cheering for,\x01",
            "Genki Genki, courage Rin Rin!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tio, when everything is over\x01",
            "Let me hug hug hung out\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F(… … Even after all is over,\x01",
            "I do not feel comfortable with that. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C90C")

    TalkEnd(0xFE)
    Return()

    # Function_44_C631 end

    def Function_45_C910(): pass

    label("Function_45_C910")

    Sound(160, 0, 100, 0)
    Return()

    # Function_45_C910 end

    def Function_46_C917(): pass

    label("Function_46_C917")

    EventBegin(0x0)
    Fade(500)
    OP_68(15440, 600, 7240, 0)
    MoveCamera(47, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21850, 0)
    SetChrPos(0x109, 14410, 0, 6710, 90)
    SetChrPos(0x101, 12500, 0, 6000, 90)
    SetChrPos(0x102, 12750, 0, 7400, 90)
    SetChrPos(0x104, 11750, 0, 7950, 90)
    SetChrPos(0x105, 11400, 0, 6600, 90)
    SetChrPos(0x103, 11500, 0, 5500, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#11POh, noel.\x01",
            "Everyone in the support department …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PTo Mr. Fran's warmth\x01",
            "Did you come in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#6PYes, now, is it okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PYes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P…… But it was good.\x01",
            "My sister 's consciousness is back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#6P……Yes.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CAFC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_CAFC)
    WaitChrThread(0x109, 3)
    Sleep(150)

    ChrTalk(
        0x109,
        (
            "#10102F#11Plet's go.\x01",
            "It is room # 301 on the third floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6POh, let me get in the way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#6PExcuse me, Sera.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 14000, 0, 6500, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x180, 6)
    OP_29(0xAC, 0x1, 0x3)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_1B(0x2, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x0, 0x0, 0x39)
    EventEnd(0x5)
    Return()

    # Function_46_C917 end

    def Function_47_CBE8(): pass

    label("Function_47_CBE8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05300.itc", 0x3C)
    SetChrPos(0x8, 20770, 0, 9100, 45)
    SetChrFlags(0xA, 0x80)
    EndChrThread(0xA, 0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(15920, 900, 7500, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27430, 0)
    SetChrChipByIndex(0x26, 0x3C)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 13850, 0, 8550, 90)
    SetChrPos(0x101, 13910, 0, 6710, 45)
    SetChrPos(0x102, 13790, 0, 5540, 45)
    SetChrPos(0x104, 13100, 0, 4120, 45)
    SetChrPos(0x109, 12280, 0, 6290, 45)
    SetChrPos(0x105, 12230, 0, 5090, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetCameraDistance(24940, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x8,
        "… … Yes … Yes, it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thank you.\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    OP_68(14190, 1000, 7310, 3000)
    MoveCamera(41, 21, 0, 3000)
    OP_6E(440, 3000)
    SetCameraDistance(20470, 3000)
    OP_95(0x8, 17210, 0, 7430, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x102, 0x5A, 0x0)
    OP_93(0x104, 0x2D, 0x0)
    OP_93(0x109, 0x5A, 0x0)
    OP_93(0x105, 0x5A, 0x0)
    OP_93(0x26, 0x87, 0x0)
    OP_0D()
    WaitChrThread(0x8, 1)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "Professor Seylandにも\x01",
            "I got a confirmation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Immediately, in the room of the research building\x01",
            "It is as if to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        "#01309FThank you, Sera.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FI am saved.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x101, 500)

    ChrTalk(
        0x26,
        (
            "#01300F… Well then everyone.\x01",
            "The break will end soon,\x01",
            "I will be rude with this.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CEAA():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CEAA)
    Sleep(50)

    def lambda_CEBA():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CEBA)
    Sleep(50)

    def lambda_CECA():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CECA)
    Sleep(50)

    def lambda_CEDA():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_CEDA)
    Sleep(50)

    def lambda_CEEA():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_CEEA)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x101,
        "#12P#00000FOh, thank you for everything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10102Fthank you for helping me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#01300FNo, you are welcome.\x02\x03",
            "#01309FWell then, from now on\x01",
            "I think it's hard to do a lot ……\x01",
            "Good luck, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00009FOh, too.\x02",
    )

    CloseMessageWindow()

    def lambda_CFDF():
        OP_95(0xFE, 12030, 0, 10760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_CFDF)
    Sleep(50)

    def lambda_CFFC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CFFC)
    Sleep(50)

    def lambda_D00C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D00C)
    WaitChrThread(0x26, 1)

    def lambda_D01D():
        OP_97(0xFE, 0x0, 0x564, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_D01D)
    Sleep(1000)

    def lambda_D03A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_D03A)
    WaitChrThread(0x26, 2)
    SetChrFlags(0x26, 0x80)
    OP_0D()
    OP_68(13870, 1000, 6330, 3000)
    OP_6F(0x1)

    ChrTalk(
        0x104,
        (
            "#12P#00310F…… Damn, constantly\x01",
            "You are a hated guy you!\x02\x03",
            "#00309F\"Good luck, Lloyd's firing\"\x01",
            "… … Even, that's it!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006FBesides, Heart mark is another\x01",
            "It was nothing …\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D124():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D124)
    Sleep(100)

    def lambda_D134():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D134)
    Sleep(500)

    ChrTalk(
        0x105,
        (
            "#6P#10300FHuh, tell me such a thing\x01",
            "Is not it a little disappointing?\x02\x03",
            "Feverishness of rumors - a hug#4Rhug#Also\x01",
            "It seems I could not see it this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FOh, remember that … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FWell, such a thing …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh, already!\x01",
            "Quickly because it's good\x01",
            "Let's go to the professor!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x3E8)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00001FThe research building from the roof of the hospital,\x01",
            "The pharmaceutical laboratory is the 4th floor of the research building!\x01",
            "Now, let's go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309F(Well, at the momentum\x01",
            "Well, it has not been cheated. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302F(Hehe, this is it\x01",
            "It is worth the effort. )\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00003F…… I can hear it, there!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x3C)
    SetScenarioFlags(0x152, 1)
    OP_29(0x70, 0x1, 0x0)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xA, 0x80)
    BeginChrThread(0xA, 0, 0, 1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 13200, 0, 5700, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_47_CBE8 end

    def Function_48_D3A9(): pass

    label("Function_48_D3A9")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x22, 0xB4, 0x0)
    OP_93(0x21, 0x87, 0x0)
    OP_4B(0x22, 0xFF)
    OP_4B(0x21, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_68(50330, 1000, 58210, 0)
    MoveCamera(69, 34, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20540, 0)
    SetChrPos(0x101, 50460, 0, 56980, 315)
    SetChrPos(0x102, 49370, 0, 56120, 0)
    SetChrPos(0x109, 50910, 0, 55870, 0)
    SetChrPos(0x105, 51820, 0, 56620, 315)
    SetChrPos(0x104, 52140, 0, 55580, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0xC, 49800, 0, 51590, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    SetChrSubChip(0x1D, 0x1)

    ChrTalk(
        0x1D,
        "Mum … … It seems like a guest.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCDA")

    ChrTalk(
        0x22,
        "Oh, you guys ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FLes, in the princess of Remiferia\x01",
            "Prince Albert閣下……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105Fそれに、Ariosさんまで……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#01405FHmm, that's a strange idea.\x02\x03",
            "#01400FYour experts, they talked about before\x01",
            "They are those of the \"Special Affairs Support Division\".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x22, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x22,
        "Oh, was that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "…… Hello, you guys at the support department.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "My name is Albert von Bartholomeus.\x01",
            "He is the head of State of Remifria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "From now on for the crossbell,\x01",
            "Please do your best hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000Fよ、Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Huh, you guys,\x01",
            "Arios君から聞いていてね。\x01",
            "I definitely wanted to see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Also, Ellie is the first time in a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHuhuu, it's been a long time.\x01",
            "His Excellency seems to be well … …\x02\x03",
            "#00103FBut just to the hospital\x01",
            "What was it that you were seeing?\x01",
            "I did not know.\x02\x03",
            "#00105FToday we came to visit\x01",
            "Really?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Well, the Prime Minister of Remifria is at this hospital\x01",
            "It's one of the sponsors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Also, the state of Seiren who you worked in\x01",
            "I wanted to see it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x22, 500)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "#01403FRegarding that, personally\x01",
            "Let me put a little more escort\x01",
            "It is a place I wanted to receive.\x02\x03",
            "#01400FOnly me and a driver of a limousine,\x01",
            "I wonder what it is like ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "フフ、Arios君のことを\x01",
            "Because it is trusted\x01",
            "Please think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Besides, for my visit\x01",
            "Take the escort and get the job of the hospital\x01",
            "I can not prevent it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1D, 0x0)
    Sleep(300)

    ChrTalk(
        0x1D,
        "Totally, it is trouble to bother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I have to visit again this time\x01",
            "It is not something I should not do ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "About this time at the trade meeting\x01",
            "What I should have focused on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Awareness of being a state guest\x01",
            "Should not we have more?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "Ha ha ha, Seirando\x01",
            "You are as heavy as ever.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00003F（Prince Albert……\x01",
            "Many friends seem to be wide people. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F（ええ、エリィさんやAriosさん……\x01",
            "  それにProfessor Seylandとも\x01",
            "I'd like to know acquainted from before. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Huh, even one country leader\x01",
            "I am afraid that kind of speech I am excited. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E073")

    label("loc_DCDA")


    ChrTalk(
        0x22,
        "Oh, you guys at the Special Affairs Support Division.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FPrince Albert閣下、\x01",
            "それにAriosさん。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAfter a sympathy with Shizuku,\x01",
            "You came here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#01400Fああ、今はProfessor Seylandに\x01",
            "I have been to a greeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Hehu, the state of Mr. Seyland who gave me a job\x01",
            "I wanted to see it by all means.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1D, 0x0)
    Sleep(300)

    ChrTalk(
        0x1D,
        "Totally, it is trouble to bother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I have to visit again this time\x01",
            "It is not something I should not do ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "About this time at the trade meeting\x01",
            "What I should have focused on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Awareness of being a state guest\x01",
            "Should not we have more?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "Ha ha ha, Seirando\x01",
            "You are as heavy as ever.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00003F（Prince Albert……\x01",
            "You really have a wide range of companionship. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F（ええ、Professor Seylandとも\x01",
            "You seem to know each other. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Huh, even one country leader\x01",
            "I am afraid that kind of speech I am excited. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E073")

    OP_82(0xC8, 0x0, 0xBB8, 0x320)
    SetMessageWindowPos(300, -1, -1, -1)
    SetChrName("voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5SOk, my teacher!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x21, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1D, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(51580, 1000, 57460, 3000)
    SetChrSubChip(0x1D, 0x1)

    def lambda_E178():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E178)
    Sleep(50)

    def lambda_E188():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E188)
    Sleep(50)

    def lambda_E198():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E198)
    Sleep(50)

    def lambda_E1A8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E1A8)
    Sleep(50)

    def lambda_E1B8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E1B8)
    Sleep(50)

    def lambda_E1C8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_E1C8)
    Sleep(50)

    def lambda_E1D8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_E1D8)
    OP_95(0xC, 53440, 0, 52820, 4000, 0x0)
    OP_95(0xC, 54100, 0, 55910, 4000, 0x0)
    OP_93(0xC, 0x13B, 0x0)
    OP_6F(0x1)

    ChrTalk(
        0x1D,
        "What's wrong, Litton.\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0xC,
        "Cure is sudden illness!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "ついさっき、ロビーにいたpatientが\x01",
            "It collapsed … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "It is an unconscious heavy body!\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1D, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x22,
        "Hmm, how is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "You, here at once\x01",
            "Bring it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Wait!\x02",
    )

    CloseMessageWindow()
    OP_64(0xC)
    OP_68(50330, 1000, 58210, 3000)
    OP_95(0xC, 53440, 0, 52820, 4000, 0x0)
    OP_95(0xC, 49800, 0, 51590, 4000, 0x0)
    OP_95(0xC, 49560, 0, 49150, 4000, 0x0)
    OP_6F(0x1)
    SetChrSubChip(0x1D, 0x1)

    def lambda_E444():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E444)
    Sleep(50)

    def lambda_E454():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E454)
    Sleep(50)

    def lambda_E464():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E464)
    Sleep(50)

    def lambda_E474():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E474)
    Sleep(50)

    def lambda_E484():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E484)
    Sleep(50)

    def lambda_E494():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_E494)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00000FAriosさん、俺たちは……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#01400FOh, it seems to be an obstacle to consultation\x01",
            "You'd better stay away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "No, please come with me.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1D, 0x0)
    TurnDirection(0x21, 0x22, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "Maybe you guys\x01",
            "It may be useful.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 59700, 0, 58450, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 58750, 0, 58400, 0)
    SetChrChipByIndex(0x24, 0x22)
    SetChrFlags(0x24, 0x10)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 59210, 700, 59900, 0)
    OP_68(58990, 1000, 59760, 0)
    MoveCamera(54, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(25400, 0)
    SetChrPos(0x22, 56950, 0, 60000, 90)
    SetChrPos(0x21, 56050, 0, 58600, 90)
    SetChrPos(0x101, 56950, 0, 56650, 0)
    SetChrPos(0x102, 57950, 0, 56650, 0)
    SetChrPos(0x109, 58950, 0, 56650, 0)
    SetChrPos(0x104, 55950, 0, 57500, 45)
    SetChrPos(0x105, 55700, 0, 56350, 45)
    OP_4B(0x1D, 0xFF)
    OP_4B(0xC, 0xFF)
    SetCameraDistance(21940, 3000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x24,
        "Shoot …………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "……HM……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005Fhow is it? Condition ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301FAlthough it seems to be suffering a lot ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "…… I am not that bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I tried various inspections,\x01",
            "There is no mistake in medical symptoms\x01",
            "No cause was detected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "If you find the disease name\x01",
            "I can prepare medicines … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "それまでpatientが持つかどうか、\x01",
            "It's pretty tough at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FIs that so heavy ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "How do you do …?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "─ ─ um.\x01",
            "A little better?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_E916():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E916)
    Sleep(50)

    def lambda_E926():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E926)
    Sleep(50)

    def lambda_E936():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E936)
    Sleep(50)

    def lambda_E946():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E946)
    Sleep(50)

    def lambda_E956():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E956)
    Sleep(50)

    def lambda_E966():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_E966)
    Sleep(50)

    def lambda_E976():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_E976)
    Sleep(50)

    def lambda_E986():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_E986)
    Sleep(300)

    ChrTalk(
        0x21,
        "#01405FWhat did you like to do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Mr. Seyland,\x01",
            "I thought while watching from the edge … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "This symptom is,\x01",
            "Is not \"Riboten poisoning\"?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1D,
        "…… Indeed, a cigarette addiction.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Although it is a case not in crossbell,\x01",
            "The possibility seems to be high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F\"Riboten poisoning\" …?\x01",
            "That's a name I have never heard.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "Native to the continental frontier\x01",
            "By uncommon poison mushroom\x01",
            "It is caused symptoms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "The poison, in the usual way\x01",
            "It's hard to detect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "However, the symptom itself\x01",
            "Is not it exactly like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "Oh, it is no doubt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Things brought in from outside\x01",
            "Maybe it was ingested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FDoes Professor sensei come with it?\x02\x03",
            "#00300FThat 's great, Grand Prince Sun.\x01",
            "With such a single shot\x01",
            "I do not mind seeing you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Haha, it is not a big deal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "However, you can not rest assured yet.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "Mr. Seyland,\x01",
            "Ribotenic addiction of a silver bullet\x01",
            "Are there stockpiles?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "…… Several materials\x01",
            "It has just run out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Even as soon as there is material\x01",
            "I can prepare it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10103FThat's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Hmm … if so.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        "Arios君、そして特務支援課の諸君。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "I will give you medication procurement from me\x01",
            "I would like to request urgent … …\x01",
            "Will you take over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#01400FHa ha … … as you said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FIt is an emergency, of course\x01",
            "I will underwrite it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FSo, if you get anything\x01",
            "Is it alright?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Well, let's explain the setup from now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "The specific effect of \"Riboten addiction\"\x01",
            "Mainly compounding with two materials.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "One is in the mountains of Mainz\x01",
            "Medicinal grass called \"Ante grass\" …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "And the other,\x01",
            "It is in forest area of Ursula intermittent way\x01",
            "It is a mushroom called \"Alma mushrooms\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F\"Alma mushroom\" in \"Ante grass\" … …\x01",
            "With the survival training of the guard\x01",
            "I feel I have seen it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Among these, for collection of \"ante grass\"\x01",
            "Arios君に向かってもらいたい。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "People's hands are not entered\x01",
            "If you are looking for medicinal herbs in mountainous areas,\x01",
            "You will be qualified as a prime minister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#01400FYes, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "And, \"Alma mushrooms\" but … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "This is me for the members of the Special Affairs Support Division\x01",
            "I would like to find it in a form to accompany it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FWell ……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FIs it with Daimo?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Well, because … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Mushrooms called \"Alma mushrooms\"\x01",
            "Places that live are similar in shape\x01",
            "There are also many other mushrooms inhabiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Because it is very easy to mistake,\x01",
            "You'd better accompany someone with knowledge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHmm, certainly together\x01",
            "You seemed better looking.\x02\x03",
            "#10300FAriosさんの護衛を\x01",
            "It will take over to us\x01",
            "If it is not anxiety, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FCertainly responsibility seems to be serious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#01401FBefore I even accepted your escort,\x01",
            "I can not help worrying a bit … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "このpatientを一刻も早く\x01",
            "If treatment is prioritized,\x01",
            "There will be no other way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "For those of the support department,\x01",
            "You also admit your ability?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "I will be careful enough\x01",
            "Do not worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "それに、Arios君が\x01",
            "If you come back in a hurry,\x01",
            "Is not there any problem?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#01404FFu … OK.\x02\x03",
            "#01400FWell then, I will immediately return to Mainz\x01",
            "I will head to the mountainous area.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "#01400FWhat about your Excellency\x01",
            "I'm counting on you, the Special Affairs Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FI will surely accomplish the escort.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Huh, then we also\x01",
            "Let's face the forested area of intermittent.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "Seiren guys,\x01",
            "patientの経過を見つつ調合の準備を\x01",
            "Please keep it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "Well, I knew.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "Everyone in the mission support department,\x01",
            "Please do your best!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Thus, Lloyd's\x01",
            "Prince Albertの緊急要請を引き受け……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ariosと二手に分かれて\x01",
            "I was going to procure materials for medicine.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Material procurement of antidote】\x07\x00",
            "I started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x78, 0x4, 0x2)
    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("r1580", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_48_D3A9 end

    def Function_49_F7AC(): pass

    label("Function_49_F7AC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(58000, 1000, 58480, 0)
    MoveCamera(58, 17, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21610, 0)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 59700, 0, 58450, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 58750, 0, 58400, 0)
    SetChrChipByIndex(0x24, 0x26)
    SetChrSubChip(0x24, 0x1)
    ClearChrFlags(0x24, 0x2)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 59210, 700, 59900, 270)
    OP_68(58990, 2000, 59760, 0)
    MoveCamera(54, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21940, 0)
    RemoveParty(0x76, 0xFF)
    SetChrPos(0x22, 56950, 0, 60000, 90)
    SetChrPos(0x21, 56050, 0, 58600, 90)
    SetChrPos(0x101, 56950, 0, 56650, 0)
    SetChrPos(0x102, 57950, 0, 56650, 0)
    SetChrPos(0x109, 58950, 0, 56650, 0)
    SetChrPos(0x104, 55950, 0, 57500, 45)
    SetChrPos(0x105, 55700, 0, 56350, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x21, 0xFF)
    OP_4B(0x22, 0xFF)
    OP_4B(0x1D, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_68(58990, 1000, 59760, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x24,
        (
            "#1PTo foreign souvenirs\x01",
            "Mushrooms that I brought back,\x01",
            "It was really tasty ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#1Pふう、To be sure it was a poisonous mushroom,\x01",
            "It was careless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Eating and delicious\x01",
            "Mushroom with \"Riboten poisoning\"\x01",
            "It is a dangerous property.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "From now on, we will do something like that\x01",
            "Do not talk to your mouth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "And even though I have taken the missed part\x01",
            "For a while in the ward in the research building\x01",
            "Because I will be hospitalized I will do that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#1PI understand.\x01",
            "Certainly if there is a sequelae\x01",
            "I am scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#1PHowever, thanks to it, I am much easier.\x01",
            "Thank you very much, teachers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "お礼なら、Prince Albert閣下と\x01",
            "Ariosさん、そして特務支援課の\x01",
            "Please tell people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He brought me the ingredients of medicine\x01",
            "Because they are not others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#1PAh … That's right.\x01",
            "皆さんもThank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#1PまさかあのPrince Albert閣下に\x01",
            "I can not help but …\x01",
            "It is somehow afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "No, no matter what I like\x01",
            "It was as much as I thought of mushrooms.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FCA1():
        TurnDirection(0x22, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FCA1)

    ChrTalk(
        0x22,
        (
            "やはり功績はArios君と\x01",
            "You are in the support department.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0x0)

    def lambda_FCEB():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_FCEB)
    Sleep(50)

    def lambda_FCFB():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FCFB)

    def lambda_FD08():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_FD08)
    Sleep(50)

    def lambda_FD18():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_FD18)

    def lambda_FD25():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_FD25)
    Sleep(50)

    def lambda_FD35():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FD35)
    Sleep(50)

    def lambda_FD45():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FD45)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "#01402FPlease humbly ……\x02\x03",
            "#01403FHis Experience with Mr. Seyland\x01",
            "Learn together and get a doctor's license\x01",
            "I heard that it took.\x02\x03",
            "#01400FIn all aspects of experience, technology etc.\x01",
            "To a physician active in one line\x01",
            "I wonder if she does not despair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FYeah … was it so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FStone is remembrania of medical advanced country\x01",
            "Did you say that the Grand priest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Haha, I am still keen to study.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "When Seyland was in Remiferia\x01",
            "I had him observe surgery often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Knowledge that we have cultivated,\x01",
            "It just happened to be useful this time … …\x01",
            "I will be embarrassed if you say so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "However, regarding this case\x01",
            "I have only spoken out from the side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Arios君と支援課の諸君、\x01",
            "And the cooperation of hospital staff\x01",
            "It has turned to treatment promptly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Well, it was a very meaningful inspection.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Whew ……\x01",
            "As usual it is argumentation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "In any case, the visit is now\x01",
            "Was it all over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Toward the commerce meeting tomorrow\x01",
            "Those who returned to preparation soon\x01",
            "Is not it good?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x22,
        (
            "Ha ha ha, you are really harsh.\x01",
            "But saying is always reasonable and certain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Well then,\x01",
            "I will get rude with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Arios君、帰りの護衛も\x01",
            "Can I ask you a favor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#01400FYes, of course.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "#01400F…… That's the special department.\x02\x03",
            "#01403FUntil tomorrow's trade council,\x01",
            "It is that I am out of my mind.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0x1)

    ChrTalk(
        0x101,
        (
            "#00000FOh, yes.\x01",
            "I will keep in mind the liver.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FThank you for your hard work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Many, from now on\x01",
            "Please do more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "I will cheer for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100Fふふ、Thank you very much.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Material procurement of antidote】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x78, 0x1, 0x1)
    OP_29(0x78, 0x1, 0x2)
    OP_29(0x78, 0x4, 0x10)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x24, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 50980, 120, 59070, 300)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 56950, 0, 60000, 90)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0x10, 0x10)
    SetChrChipByIndex(0x24, 0x26)
    SetChrSubChip(0x24, 0x0)
    EndChrThread(0x24, 0x0)
    SetChrBattleFlags(0x24, 0x4)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 59210, 700, 59900, 270)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 54710, 0, 55500, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_49_F7AC end

    def Function_50_1048E(): pass

    label("Function_50_1048E")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(14780, 1000, 6910, 0)
    MoveCamera(58, 31, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21660, 0)
    SetChrPos(0x101, 14490, 0, 7430, 90)
    SetChrPos(0x102, 15120, 0, 5850, 45)
    SetChrPos(0x103, 13530, 0, 8000, 90)
    SetChrPos(0x109, 12940, 0, 6840, 90)
    SetChrPos(0x104, 13810, 0, 6210, 45)
    SetChrPos(0x105, 13710, 0, 5020, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Everyone in the Support Division ……\x01",
            "Welcome to Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What day is it?\x01",
            "Is it a case?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUh, a little\x01",
            "What you want to ask\x01",
            "I was there ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd's luggage misallocation\x01",
            "I asked about what happened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Oh … that luggage\x01",
            "Was that something like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "One of the nurses\x01",
            "I made an order mistake soon\x01",
            "Martha 's chief was on a noise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FOrder mistake … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, some times ago\x01",
            "There is such a thing … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FHaha …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FWell then, the baggage is now\x01",
            "To the nurse station?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, to that\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Please visit the second floor once.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FThen, it will do so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FIf you get angry with wet clothes\x01",
            "Poor thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FThat's right.\x01",
            "Let's go quickly.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x175, 7)
    OP_29(0x85, 0x1, 0x2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 14410, 0, 7430, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_50_1048E end

    def Function_51_10870(): pass

    label("Function_51_10870")

    Return()

    # Function_51_10870 end

    def Function_52_10871(): pass

    label("Function_52_10871")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(8130, 1000, 530, 0)
    MoveCamera(65, 32, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24000, 0)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x8, 9100, 0, 1500, 270)
    SetChrPos(0x9, 9100, 0, 500, 270)
    SetChrPos(0x1E, 9100, 0, -500, 270)
    SetChrPos(0x1D, 9100, 0, -1500, 270)
    SetChrPos(0x23, 7140, 0, 2160, 135)
    SetChrPos(0x101, 6500, 0, 0, 90)
    SetChrPos(0x102, 6300, 0, 1000, 90)
    SetChrPos(0x104, 6300, 0, -1000, 90)
    SetChrPos(0x109, 4900, 0, 0, 90)
    SetChrPos(0x105, 5100, 0, 1000, 90)
    SetChrPos(0x103, 5100, 0, -1000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0x1E, 0xFF)
    OP_4B(0x1D, 0xFF)
    OP_4B(0x23, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "From Ricardo of the airport\x01",
            "I was surprised when there was contact … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you think that medical supplies do not arrive\x01",
            "No way, it was supposed to be such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "There is a bad guy … hey ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "でも、Medical supplies arrived\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "For now,\x01",
            "襲撃事件のpatientたちに\x01",
            "You will be able to respond adequately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Do not let anything help you guys.\x01",
            "Let me thank you once more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FNo, of course\x01",
            "Because I did it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FFire place like a thief\x01",
            "To forgive a sneaky bastard\x01",
            "I will not go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FWell this time in that armor\x01",
            "I have been saved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "Armor … What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FLet me see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F…… This is the story,\x01",
            "Please do not mind too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell then, if something happens again\x01",
            "Please contact us anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah ….\x01",
            "本当にThank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "I will also thank you from my side.\x01",
            "Thank you so much!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Search for medical supplies】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x93, 0x1, 0x7)
    OP_29(0x93, 0x1, 0x8)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_29(0x93, 0x4, 0x10)
    OP_2C(0x93, 0x2)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x8, 17210, 0, 7430, 266)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x9, 19740, 0, 4890, 180)
    ClearChrFlags(0x9, 0x10)
    OP_66(0x1, 0x1)
    OP_4C(0x1D, 0xFF)
    SetChrPos(0x1D, 65800, 0, 1700, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 5950, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_52_10871 end

    def Function_53_10DDE(): pass

    label("Function_53_10DDE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(8130, 1000, 530, 0)
    MoveCamera(65, 32, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24000, 0)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x8, 9100, 0, 1500, 270)
    SetChrPos(0x9, 9100, 0, 500, 270)
    SetChrPos(0x1E, 9100, 0, -500, 270)
    SetChrPos(0x1D, 9100, 0, -1500, 270)
    SetChrPos(0x23, 7140, 0, 2160, 135)
    SetChrPos(0x101, 6500, 0, 0, 90)
    SetChrPos(0x102, 6300, 0, 1000, 90)
    SetChrPos(0x104, 6300, 0, -1000, 90)
    SetChrPos(0x109, 4900, 0, 0, 90)
    SetChrPos(0x105, 5100, 0, 1000, 90)
    SetChrPos(0x103, 5100, 0, -1000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0x1E, 0xFF)
    OP_4B(0x1D, 0xFF)
    OP_4B(0x23, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "From Ricardo of the airport\x01",
            "I was surprised when there was contact … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you think that medical supplies do not arrive\x01",
            "No way, it was supposed to be such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "There is a bad guy … hey ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAbsolutely, really\x01",
            "I am sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FAbsolutely\x01",
            "I wanted to catch it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "I too, faster\x01",
            "If you go to pick up your luggage\x01",
            "To such a thing …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No, everyone's … …\x01",
            "Please do not be discouraged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway, the other side here\x01",
            "Because I will try it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Those that have been stolen\x01",
            "It is no use right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hurry to add extra supplies\x01",
            "I have to arrange for them to be sent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Until then, somehow,\x01",
            "I guess there is no choice but to devise it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FExcuse me……\x01",
            "後はThank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "(Ha, well, I've got my grandfather with my father.\x01",
            "I heard you are getting overwhelmed … …)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Search for medical supplies】\x07\x00",
            "I failed ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x93, 0x1, 0x9)
    OP_29(0x93, 0x4, 0x40)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x8, 17210, 0, 7430, 266)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x9, 19740, 0, 4890, 180)
    ClearChrFlags(0x9, 0x10)
    OP_66(0x1, 0x1)
    OP_4C(0x1D, 0xFF)
    SetChrPos(0x1D, 65800, 0, 1700, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 5950, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_53_10DDE end

    def Function_54_112F3(): pass

    label("Function_54_112F3")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ICU (intensive care unit)\x01",
            "Forbid access by those without permission.\x01",
            "※ Entrants must have level 2 or higher\x01",
            "Please perform sterilization treatment.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_54_112F3 end

    def Function_55_1139C(): pass

    label("Function_55_1139C")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's go to the reception first.\x01",
            "Then it is time to visit the hospital room.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 59460, 0, 3330, 225)
    EventEnd(0x4)
    Return()

    # Function_55_1139C end

    def Function_56_113F1(): pass

    label("Function_56_113F1")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's go to the reception first.\x01",
            "Then it is time to visit the hospital room.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11970, 0, 10190, 135)
    EventEnd(0x4)
    Return()

    # Function_56_113F1 end

    def Function_57_11446(): pass

    label("Function_57_11446")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FFran's room was room 301.\x01",
            "Let's go to see the situation as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 1120, 50, -440, 89)
    EventEnd(0x4)
    Return()

    # Function_57_11446 end

    SaveToFile()

Try(main)
