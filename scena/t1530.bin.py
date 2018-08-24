from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Receptionist Sera",      # 1
        "Manager Clark",          # 2
        "Nurse Ran",              # 3
        "Professor Ragot",        # 4
        "Medical Intern Lytton",  # 5
        "Medical Intern Gwen",    # 6
        "Professor Gary",         # 7
        "Chief Ashram",           # 8
        "Medical Intern Chaleur", # 9
        "Outpatient",             # 10
        "Outpatient",             # 11
        "Outpatient",             # 12
        "Outpatient",             # 13
        "Outpatient",             # 14
        "Outpatient",             # 15
        "Outpatient",             # 16
        "Outpatient",             # 17
        "Patient",                # 18
        "Patient",                # 19
        "Patient",                # 20
        "Nurse Ada",              # 21
        "Professor Seiland",      # 22
        "Guard Tony",             # 23
        "Old Man Quine",          # 24
        "Amisaah",                # 25
        "Arios",                  # 26
        "Archduke Albert",        # 27
        "Billy",                  # 28
        "Patient",                # 29
        "Bracer Eolia",           # 30
        "Cecil",                  # 31
        "Woman",                  # 32
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
        "Function_8_2C5F",         # 08, 8
        "Function_9_2C63",         # 09, 9
        "Function_10_43D4",        # 0A, 10
        "Function_11_5239",        # 0B, 11
        "Function_12_62D6",        # 0C, 12
        "Function_13_6AAA",        # 0D, 13
        "Function_14_747F",        # 0E, 14
        "Function_15_804A",        # 0F, 15
        "Function_16_8C88",        # 10, 16
        "Function_17_8DAC",        # 11, 17
        "Function_18_9DEC",        # 12, 18
        "Function_19_9FA2",        # 13, 19
        "Function_20_B023",        # 14, 20
        "Function_21_B465",        # 15, 21
        "Function_22_B7EA",        # 16, 22
        "Function_23_BCCA",        # 17, 23
        "Function_24_C10F",        # 18, 24
        "Function_25_C1B7",        # 19, 25
        "Function_26_C429",        # 1A, 26
        "Function_27_C7F6",        # 1B, 27
        "Function_28_C960",        # 1C, 28
        "Function_29_CAB9",        # 1D, 29
        "Function_30_CB45",        # 1E, 30
        "Function_31_CB94",        # 1F, 31
        "Function_32_CC09",        # 20, 32
        "Function_33_CC99",        # 21, 33
        "Function_34_D7E3",        # 22, 34
        "Function_35_D8BC",        # 23, 35
        "Function_36_D9E5",        # 24, 36
        "Function_37_DAAD",        # 25, 37
        "Function_38_DCA5",        # 26, 38
        "Function_39_DD8A",        # 27, 39
        "Function_40_DE37",        # 28, 40
        "Function_41_DE6D",        # 29, 41
        "Function_42_DF1F",        # 2A, 42
        "Function_43_E11E",        # 2B, 43
        "Function_44_E125",        # 2C, 44
        "Function_45_E472",        # 2D, 45
        "Function_46_E479",        # 2E, 46
        "Function_47_E715",        # 2F, 47
        "Function_48_EF38",        # 30, 48
        "Function_49_114CD",       # 31, 49
        "Function_50_12308",       # 32, 50
        "Function_51_12725",       # 33, 51
        "Function_52_12726",       # 34, 52
        "Function_53_12CAF",       # 35, 53
        "Function_54_1323A",       # 36, 54
        "Function_55_132FA",       # 37, 55
        "Function_56_1335F",       # 38, 56
        "Function_57_133C4",       # 39, 57
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_167C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A5")

    ChrTalk(
        0x8,
        (
            "We were finally able to\x01",
            "reopen the closed\x01",
            "outpatient ward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even though we're going\x01",
            "to be busy for a while,\x01",
            "I'm relieved...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is thanks to all\x01",
            "your help as well. Please\x01",
            "accept my sincere thanks.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1677")

    label("loc_15A5")


    ChrTalk(
        0x8,
        (
            "We were finally able to\x01",
            "reopen the closed\x01",
            "outpatient ward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though we're going to be busy for a while, as a\x01",
            "hospital employee, I'll be sure to be kind,\x01",
            "careful and thorough when dealing with patients.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1677")

    Jump("loc_2C5B")

    label("loc_167C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1842")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178E")

    ChrTalk(
        0x8,
        (
            "According to rumor, it seems that accepting\x01",
            "the declaration of invalidity has caused\x01",
            "something like a riot in parts of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They say the State Guard quickly\x01",
            "suppressed it, but... I'm worried that\x01",
            "there may have been injured people.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_183D")

    label("loc_178E")


    ChrTalk(
        0x8,
        (
            "It seems that accepting the declaration\x01",
            "of invalidity has caused something like\x01",
            "a riot in a part of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm worried that there\x01",
            "may have been injured\x01",
            "people...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_183D")

    Jump("loc_2C5B")

    label("loc_1842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_19E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1944")

    ChrTalk(
        0x8,
        (
            "We ask the State Guard to pay\x01",
            "attention to medicine for those who\x01",
            "were our regular outpatients before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But there's not enough of\x01",
            "them... In this situation, they\x01",
            "can't very well manage it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...It's beyond our\x01",
            "control.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19E1")

    label("loc_1944")


    ChrTalk(
        0x8,
        (
            "Since we've stopped receiving outpatients,\x01",
            "I'd like to at least send medicines to the\x01",
            "patients in the city. However...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...It's beyond our\x01",
            "control.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E1")

    Jump("loc_2C5B")

    label("loc_19E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1C58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B77")

    ChrTalk(
        0x8,
        (
            "Because of the influence of the\x01",
            "Cryptids, we've stopped accepting\x01",
            "outpatients at the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At present, only seriously ill or injured\x01",
            "patients are brought here by ambulances\x01",
            "escorted by the State Guard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Such a system goes against\x01",
            "the long-established intent\x01",
            "of St. Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Above all, I'm very\x01",
            "worried about our\x01",
            "patients within the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C53")

    label("loc_1B77")


    ChrTalk(
        0x8,
        (
            "Because of the influence of the\x01",
            "Cryptids, we've stopped accepting\x01",
            "outpatients at the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To think we're only able to treat\x01",
            "seriously ill or injured patients... I'm\x01",
            "worried about our patients in the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C53")

    Jump("loc_2C5B")

    label("loc_1C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2164")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_203C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1DDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D4D")

    ChrTalk(
        0x8,
        (
            "Thank goodness those\x01",
            "medical supplies\x01",
            "arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though it may be presumptuous of\x01",
            "me, allow me to thank you as a\x01",
            "representative of the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DD6")

    label("loc_1D4D")


    ChrTalk(
        0x8,
        (
            "Though it may be presumptuous of\x01",
            "me, allow me to thank you as a\x01",
            "representative of the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DD6")

    Jump("loc_2037")

    label("loc_1DDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1EA2")

    ChrTalk(
        0x8,
        (
            "We explained the situation to Remiferia,\x01",
            "and they're once again arranging a\x01",
            "delivery of medical supplies for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though it may be a\x01",
            "little too late...\x01",
            "What's done is done.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2037")

    label("loc_1EA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F9C")

    ChrTalk(
        0x8,
        (
            "Just now, Mr. Tony, the\x01",
            "guard, reported something\x01",
            "to the manager.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The two of them as well as Professor\x01",
            "Seiland seem to be discussing something\x01",
            "in front of the exam room right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder what could have\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2037")

    label("loc_1F9C")


    ChrTalk(
        0x8,
        (
            "Mr. Tony, the guard, and the manager\x01",
            "seem to be discussing something with\x01",
            "Professor Seiland in the exam room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder what could have\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2037")

    Jump("loc_215F")

    label("loc_203C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20ED")

    ChrTalk(
        0x8,
        (
            "Fran's room is No. 301\x01",
            "on 3F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She's in stable condition,\x01",
            "but it seems her strength\x01",
            "hasn't yet returned...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please, try to cheer her\x01",
            "up a little.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_215F")

    label("loc_20ED")


    ChrTalk(
        0x8,
        (
            "Fran regained\x01",
            "consciousness just the\x01",
            "other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Her wounds were\x01",
            "extremely serious... I'm\x01",
            "very relieved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_215F")

    Jump("loc_2C5B")

    label("loc_2164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_23C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22FA")

    ChrTalk(
        0x8,
        (
            "Due to yesterday's train accident, a\x01",
            "large number of patients, foreigners\x01",
            "included, were brought here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since St. Ursula Hospital is always\x01",
            "ready to accept foreigners, we\x01",
            "dealt with them smoothly, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If the accident occurred in a foreign\x01",
            "country without advanced medical care,\x01",
            "I wonder what would've happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I end up shivering\x01",
            "whenever I think about\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_23C3")

    label("loc_22FA")


    ChrTalk(
        0x8,
        (
            "If the accident occurred in a foreign\x01",
            "country without advanced medical care,\x01",
            "I wonder what would have happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Almost everyone had only\x01",
            "minor injuries. In that\x01",
            "sense, maybe we were lucky.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23C3")

    Jump("loc_2C5B")

    label("loc_23C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_260E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2542")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24C3")

    ChrTalk(
        0x8,
        (
            "That package was a\x01",
            "misdelivery, wasn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thinking that it was an ordering\x01",
            "mistake made by one of the nurses, Head\x01",
            "Nurse Martha got angry at her, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, for now, please\x01",
            "visit 2F.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_253D")

    label("loc_24C3")


    ChrTalk(
        0x8,
        (
            "It seems you were able\x01",
            "to accept the package.\x01",
            "Haha, that's great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, please be\x01",
            "careful on your way\x01",
            "back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_253D")

    Jump("loc_2609")

    label("loc_2542")


    ChrTalk(
        0x8,
        (
            "Welcome to St. Ursula Hospital.\x01",
            "This is the outpatient and\x01",
            "visitation desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We also accept appointments for follow-\x01",
            "up exams via orbal net, so please feel\x01",
            "free to make use of this service.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2609")

    Jump("loc_2C5B")

    label("loc_260E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_272E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26CD")

    ChrTalk(
        0x8,
        (
            "...This isn't good. A\x01",
            "depressed mood is spreading\x01",
            "amongst the staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There were great hopes for\x01",
            "Shizuku's surgery... I suppose\x01",
            "it can't be helped, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2729")

    label("loc_26CD")


    ChrTalk(
        0x8,
        (
            "...We staff can't be\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We must get out of this\x01",
            "depressed mood\x01",
            "somehow...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2729")

    Jump("loc_2C5B")

    label("loc_272E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_28B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2824")

    ChrTalk(
        0x8,
        (
            "It seems Mihail's\x01",
            "discharge is scheduled\x01",
            "for next week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He's had a long hospital stay,\x01",
            "so I'll miss him, but... I'm\x01",
            "really happy for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone wants to say\x01",
            "goodbye to him on the\x01",
            "day of his discharge.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_28AD")

    label("loc_2824")


    ChrTalk(
        0x8,
        (
            "I'm really happy that\x01",
            "Mihail's discharge has\x01",
            "been scheduled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone wants to say\x01",
            "goodbye to him on the\x01",
            "day of his discharge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28AD")

    Jump("loc_2C5B")

    label("loc_28B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2ACE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2981")

    ChrTalk(
        0x8,
        (
            "His Excellency Archduke\x01",
            "Albert headed back to\x01",
            "the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, you all did good\x01",
            "work as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Allow us to look after\x01",
            "the patient and treat him\x01",
            "until he is discharged.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AC9")

    label("loc_2981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A1F")

    ChrTalk(
        0x8,
        (
            "His Excellency Archduke\x01",
            "Albert was with Mr.\x01",
            "Arios just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "His inspection is finished,\x01",
            "and it seems he's visiting\x01",
            "Shizuku with him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AC9")

    label("loc_2A1F")


    ChrTalk(
        0x8,
        (
            "His Excellency Archduke Albert\x01",
            "went with Mr. Arios to the\x01",
            "internal medicine exam room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since his inspection is\x01",
            "finished, it seems they're\x01",
            "having a little chat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AC9")

    Jump("loc_2C5B")

    label("loc_2ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C5B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2B4D")

    ChrTalk(
        0x8,
        (
            "Good work collecting\x01",
            "those medical surveys,\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please come again\x01",
            "whenever you need.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C5B")

    label("loc_2B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BEA")

    ChrTalk(
        0x8,
        (
            "Professor Seiland is in\x01",
            "the pharmacology and\x01",
            "neurology lab.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The research building is\x01",
            "on the roof. From there,\x01",
            "please head to 4F.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2C5B")

    label("loc_2BEA")


    ChrTalk(
        0x8,
        (
            "Professor Seiland is in\x01",
            "the lab.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The pharmacology and\x01",
            "neurology lab is on 4F of\x01",
            "the research building.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C5B")

    TalkEnd(0x8)
    Return()

    # Function_7_1478 end

    def Function_8_2C5F(): pass

    label("Function_8_2C5F")

    Call(0, 9)
    Return()

    # Function_8_2C5F end

    def Function_9_2C63(): pass

    label("Function_9_2C63")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2E47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D5E")

    ChrTalk(
        0x9,
        (
            "I can't see a situation with\x01",
            "limited medical supplies as\x01",
            "positive, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because we're again accepting\x01",
            "outpatients, their chances of\x01",
            "survival have greatly improved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We staff must do our\x01",
            "very best as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E42")

    label("loc_2D5E")


    ChrTalk(
        0x9,
        (
            "The present situation may be difficult, but\x01",
            "if we could cooperate with Remiferia again,\x01",
            "we could solve our medical supplies shortage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We're finally able to treat\x01",
            "outpatients once again, so...\x01",
            "We must do our very best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E42")

    Jump("loc_43D0")

    label("loc_2E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3031")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F79")

    ChrTalk(
        0x9,
        (
            "Currently, all information\x01",
            "coming in from Crossbell\x01",
            "City has been cut off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The information restrictions are\x01",
            "most likely intentional due to\x01",
            "the declaration of invalidity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it's like this, we can't deal\x01",
            "with emergencies. ...I'm worried\x01",
            "about everyone in the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_302C")

    label("loc_2F79")


    ChrTalk(
        0x9,
        (
            "Currently, all information\x01",
            "coming in from Crossbell\x01",
            "City has been cut off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it's like this, we can't deal\x01",
            "with emergencies. ...I'm worried\x01",
            "about everyone in the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_302C")

    Jump("loc_43D0")

    label("loc_3031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3222")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3154")

    ChrTalk(
        0x9,
        (
            "The flow of information is restricted\x01",
            "throughout Crossbell. There's hardly\x01",
            "any coming from within the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We get notified of emergency cases\x01",
            "from time to time. With things like\x01",
            "this, we're going to be too late...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm, this isn't a good\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_321D")

    label("loc_3154")


    ChrTalk(
        0x9,
        (
            "The flow of information is restricted\x01",
            "throughout Crossbell. There's hardly\x01",
            "any coming from within the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We're going to be too late\x01",
            "responding to them... Hmm,\x01",
            "this isn't a good situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_321D")

    Jump("loc_43D0")

    label("loc_3222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3422")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_335D")

    ChrTalk(
        0x9,
        (
            "We're indebted to Tio\x01",
            "for the maintenance of\x01",
            "our orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the worst case scenario, we'll be\x01",
            "ready to receive patients because\x01",
            "the orbal net's still working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Allow me to take this\x01",
            "opportunity to thank you\x01",
            "once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FHaha, no... It wasn't\x01",
            "anything serious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_341D")

    label("loc_335D")


    ChrTalk(
        0x9,
        (
            "We're greatly indebted\x01",
            "to Tio for maintaining\x01",
            "our orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although it would be awful for the hospital\x01",
            "if this situation were to continue. I must\x01",
            "think of some way deal with it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_341D")

    Jump("loc_43D0")

    label("loc_3422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3855")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_355D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F1")

    ChrTalk(
        0x9,
        (
            "I called Ricardo at the\x01",
            "airport to inform him the\x01",
            "goods were delivered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He felt relieved too.\x01",
            "That's great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope nothing like this\x01",
            "ever happens again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3554")

    label("loc_34F1")


    ChrTalk(
        0x9,
        (
            "I'm glad Ricardo finally\x01",
            "felt relieved too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope nothing like this\x01",
            "ever happens again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3554")

    TalkEnd(0x9)
    Return()

    label("loc_355D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_35F2")

    ChrTalk(
        0x9,
        (
            "What happened in this\x01",
            "case isn't your fault,\x01",
            "don't lose heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At any rate, we'll try\x01",
            "to do something about it\x01",
            "on our end.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    label("loc_35F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3680")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3615")
    Call(0, 35)
    Jump("loc_367B")

    label("loc_3615")


    ChrTalk(
        0x9,
        (
            "Maybe something happened\x01",
            "to the transport...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I-In any case, I'll try\x01",
            "contacting them again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_367B")

    Jump("loc_3850")

    label("loc_3680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37BE")

    ChrTalk(
        0x9,
        (
            "For a time, a lot of\x01",
            "people came to visit\x01",
            "Ilya, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since she's still in a coma,\x01",
            "I turned down everyone\x01",
            "except people who know her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even so, the people\x01",
            "sending her gifts and\x01",
            "sweets are never ending...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It made me feel once again\x01",
            "that Ilya is a great\x01",
            "existence for the citizens.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3850")

    label("loc_37BE")


    ChrTalk(
        0x9,
        (
            "The people who send\x01",
            "sweets and such to Ilya\x01",
            "are never ending.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It made me feel once again\x01",
            "that she's a great\x01",
            "existence for the citizens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3850")

    Jump("loc_43D0")

    label("loc_3855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3A91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39DC")

    ChrTalk(
        0x9,
        (
            "Safety confirmations have been coming in from the\x01",
            "Empire and Republic from the families of the people\x01",
            "injured in the accident ever since yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As expected, it seems many\x01",
            "people get worried when\x01",
            "you're hospitalised abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "And if that wasn't enough, a state of\x01",
            "tension continues in Crossbell following\x01",
            "the independence proposal the other day...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3A8C")

    label("loc_39DC")


    ChrTalk(
        0x9,
        (
            "As expected, it seems many\x01",
            "people get worried when\x01",
            "you're hospitalised abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'd like us to focus on treating\x01",
            "them so they can return to their\x01",
            "home countries ASAP.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A8C")

    Jump("loc_43D0")

    label("loc_3A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3C2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B99")

    ChrTalk(
        0x9,
        (
            "Thanks to the orbal\x01",
            "network legislation, our\x01",
            "net-based re-exams are up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think useful bills like that will\x01",
            "be easier to pass if Crossbell\x01",
            "becomes independent, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder how the\x01",
            "referendum will turn out\x01",
            "in practice?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3C2A")

    label("loc_3B99")


    ChrTalk(
        0x9,
        (
            "I think useful bills be\x01",
            "easier to pass if Crossbell\x01",
            "becomes independent, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder how the\x01",
            "referendum will turn out\x01",
            "in practice?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C2A")

    Jump("loc_43D0")

    label("loc_3C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3E3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D7F")

    ChrTalk(
        0x9,
        (
            "In Shizuku's surgery yesterday, a\x01",
            "revolutionary surgical technique\x01",
            "devised by Professor Seiland was used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Interest from the medical staff was great\x01",
            "and I can say that the trust they\x01",
            "temporarily lost was completely restored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...However, we can't\x01",
            "openly rejoice. I wish it\x01",
            "had been successful...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3E3A")

    label("loc_3D7F")


    ChrTalk(
        0x9,
        (
            "I can say that by trying a revolutionary\x01",
            "surgery, the trust they temporarily lost\x01",
            "was completely restored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...However, we can't\x01",
            "openly rejoice. I wish it\x01",
            "had been successful...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E3A")

    Jump("loc_43D0")

    label("loc_3E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3FFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F6A")

    ChrTalk(
        0x9,
        (
            "A big operation will be\x01",
            "performed by Professor\x01",
            "Seiland before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the inspection by Archduke Albert the\x01",
            "other day, it was decided that we'll receive\x01",
            "Remiferia's full support regarding it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We have to do all we can\x01",
            "as well to make the\x01",
            "surgery a success.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3FF8")

    label("loc_3F6A")


    ChrTalk(
        0x9,
        (
            "A big operation will be\x01",
            "performed by Professor\x01",
            "Seiland before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We have to do all we can\x01",
            "as well to make the\x01",
            "surgery a success.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FF8")

    Jump("loc_43D0")

    label("loc_3FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4162")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40CF")

    ChrTalk(
        0x9,
        (
            "We were thanked by\x01",
            "Archduke Albert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We've received strong support\x01",
            "from the Archduke, a sponsor of\x01",
            "the hospital, for a long while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The entire staff was\x01",
            "very encouraged.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_415D")

    label("loc_40CF")


    ChrTalk(
        0x9,
        (
            "We've received strong support\x01",
            "from the Archduke, a sponsor of\x01",
            "the hospital, for a long while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The entire staff was\x01",
            "very encouraged.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_415D")

    Jump("loc_43D0")

    label("loc_4162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_43D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_431A")

    ChrTalk(
        0x9,
        (
            "Because of the "Cult Incident"\x01",
            "scandal, the trust the hospital had\x01",
            "established was instantly lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That's reasonable. After all, a\x01",
            "hospital doctor made use of drugs\x01",
            "and threw this land into confusion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A thorough police investigation\x01",
            "confirmed there are no problems with the\x01",
            "medicines prescribed normally, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even now, there are some\x01",
            "patients with a sense of\x01",
            "mistrust they can't wipe away.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_43D0")

    label("loc_431A")


    ChrTalk(
        0x9,
        (
            "Though we were cleared of\x01",
            "suspicion, there are still some\x01",
            "who distrust the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Going forward, we must recover\x01",
            "trust gradually, aiming at\x01",
            "even more open medical care.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43D0")

    TalkEnd(0x9)
    Return()

    # Function_9_2C63 end

    def Function_10_43D4(): pass

    label("Function_10_43D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_45BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44E9")

    ChrTalk(
        0xA,
        (
            "Little bro and friends... The\x01",
            "situation seems really terrible,\x01",
            "but we must never lose heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When everything is over\x01",
            "and settled, let's go have\x01",
            "fun together again, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FYeah, leave it to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHaha, I'll do my best.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_45B7")

    label("loc_44E9")


    ChrTalk(
        0xA,
        (
            "When everything is over\x01",
            "and settled, let's go have\x01",
            "fun together again, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ada and Filia, Xilun and Meihua... And\x01",
            "let's invite Head Nurse Martha too this\x01",
            "time... Let's have a blast with everyone!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45B7")

    Jump("loc_5235")

    label("loc_45BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_47BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46E6")

    ChrTalk(
        0xA,
        (
            "The stress of even the outpatients\x01",
            "who had to remain at the hospital\x01",
            "has gradually reached a peak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, it seems they have\x01",
            "started to hope they can return\x01",
            "after what's happened in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I don't know what will\x01",
            "happen, but I hope they\x01",
            "get to return.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_47BA")

    label("loc_46E6")


    ChrTalk(
        0xA,
        (
            "After what's happened in the city, it seems that\x01",
            "the outpatient visitors who had to remain at the\x01",
            "hospital have started get their hopes up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I don't know what will\x01",
            "happen, but I hope they\x01",
            "get to return.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47BA")

    Jump("loc_5235")

    label("loc_47BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_494E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C6")

    ChrTalk(
        0xA,
        (
            "As of yet, it seems there's\x01",
            "no chance of a full\x01",
            "recovery for Ilya Platiｲre.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...However, it's going\x01",
            "to be fine. We have\x01",
            "excellent doctors here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It may take some time, but\x01",
            "you'll see. The doctors\x01",
            "will definitely cure Ilya.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4949")

    label("loc_48C6")


    ChrTalk(
        0xA,
        (
            "After all, we have\x01",
            "excellent doctors here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It may take some time, but\x01",
            "you'll see. The doctors\x01",
            "will definitely cure Ilya.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4949")

    Jump("loc_5235")

    label("loc_494E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4AE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A4A")

    ChrTalk(
        0xA,
        (
            "The situation is like this,\x01",
            "but... The people in the hospital\x01",
            "are unexpectedly positive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "After all, Ilya Platiｲre\x01",
            "who was in a coma has\x01",
            "finally opened her eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If we think about that,\x01",
            "we must do our best too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4ADD")

    label("loc_4A4A")


    ChrTalk(
        0xA,
        (
            "The fact that Ilya Platiｲre\x01",
            "has regained consciousness is\x01",
            "the best news in a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If we think about that,\x01",
            "we must do our best too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4ADD")

    Jump("loc_5235")

    label("loc_4AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4B83")

    ChrTalk(
        0xA,
        (
            "*sigh*, say what you\x01",
            "like, but I'm starting\x01",
            "to feel tired...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...No, the patients are\x01",
            "experiencing even more\x01",
            "suffering. I can't complain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5235")

    label("loc_4B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4C29")

    ChrTalk(
        0xA,
        (
            "We're extremely busy\x01",
            "because of yesterday's\x01",
            "derailment accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I won't be in the mood to\x01",
            "party for a while... I have\x01",
            "to do my job properly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5235")

    label("loc_4C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4CA2")

    ChrTalk(
        0xA,
        (
            "Shizuku's mental\x01",
            "strength always cheers\x01",
            "us up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We nurses must have hope\x01",
            "too and support Shizuku.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5235")

    label("loc_4CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4E07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D79")

    ChrTalk(
        0xA,
        (
            "Until now, Shizuku has\x01",
            "undergone many eye\x01",
            "surgeries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, even though the\x01",
            "doctors here are excellent,\x01",
            "it never goes well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Both she and Arios are\x01",
            "probably very uneasy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4E02")

    label("loc_4D79")


    ChrTalk(
        0xA,
        (
            "Shizuku has undergone many\x01",
            "eye surgeries up until now,\x01",
            "but none have gone well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Both she and Arios are\x01",
            "probably very uneasy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E02")

    Jump("loc_5235")

    label("loc_4E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EDE")

    ChrTalk(
        0xA,
        (
            "Rumor has it that Professor\x01",
            "Seiland will be doing a\x01",
            "major surgery soon, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In this hospital, the\x01",
            "only one who needs such a\x01",
            "surgery is "that child".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I hope she is cured.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4F47")

    label("loc_4EDE")


    ChrTalk(
        0xA,
        (
            "In this hospital, the only\x01",
            "one who needs a major\x01",
            "surgery is "that child".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I hope she is cured.\x02",
    )

    CloseMessageWindow()

    label("loc_4F47")

    Jump("loc_5235")

    label("loc_4F4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_50AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5018")

    ChrTalk(
        0xA,
        (
            "Professor Ragot is\x01",
            "currently away on\x01",
            "business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He's attending an\x01",
            "academic meeting abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Professor Seiland is in\x01",
            "charge of internal medicine\x01",
            "today in his stead.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_50A8")

    label("loc_5018")


    ChrTalk(
        0xA,
        (
            "Today, Professor Ragot\x01",
            "away for an academic\x01",
            "meeting out of state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's too bad he couldn't\x01",
            "greet the the Archduke\x01",
            "now that he's here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50A8")

    Jump("loc_5235")

    label("loc_50AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5235")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51D2")

    ChrTalk(
        0xA,
        (
            "Oh, if it isn't Mr.\x01",
            "Randy and little bro.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FRan, it's been a while!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FLong time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now that you mention it,\x01",
            "it has been a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'd like to talk with\x01",
            "you more but I'm working\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please speak to me again\x01",
            "next time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 6)
    Jump("loc_5235")

    label("loc_51D2")


    ChrTalk(
        0xA,
        (
            "I'd like to talk with\x01",
            "you more, but I'm\x01",
            "working now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please speak to me again\x01",
            "next time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5235")

    TalkEnd(0xFE)
    Return()

    # Function_10_43D4 end

    def Function_11_5239(): pass

    label("Function_11_5239")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_52E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5257")
    Call(0, 12)
    Jump("loc_52DB")

    label("loc_5257")


    ChrTalk(
        0xB,
        (
            "*cough*, that's how my\x01",
            "worthy rival is supposed\x01",
            "to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Come now, we can't keep\x01",
            "the patients waiting.\x01",
            "Let's begin at once!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52DB")

    Jump("loc_62D2")

    label("loc_52E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5551")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_544B")

    ChrTalk(
        0xB,
        (
            "I tried to hit some old\x01",
            "medical books with\x01",
            "Seiland and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It seems possible to prepare some\x01",
            "medicines, such as anaesthetics, here\x01",
            "using Crossbell's native medicinal plants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Diplomatic ties with Remiferia were cut and we have\x01",
            "a constant shortage of medical supplies, but...\x01",
            "Maybe we can have a little hope for the future.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_554C")

    label("loc_544B")


    ChrTalk(
        0xB,
        (
            "I looked into it with Seiland and\x01",
            "it seems some medicines we lack\x01",
            "of can be produced in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Diplomatic ties with Remiferia were cut and we have\x01",
            "a constant shortage of medical supplies, but...\x01",
            "Maybe we can have a little hope for the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_554C")

    Jump("loc_62D2")

    label("loc_5551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_5654")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_556C")
    Call(0, 12)
    Jump("loc_564F")

    label("loc_556C")


    ChrTalk(
        0xB,
        (
            "Since I'm worried about my wife and son\x01",
            "I'm not in the mood to work and I was\x01",
            "thinking I'd rather go home, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmm, he's a professional doctor too.\x01",
            "...It seems I've caused some\x01",
            "unnecessary worry. It's not like me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_564F")

    Jump("loc_62D2")

    label("loc_5654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_585C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_577B")

    ChrTalk(
        0xB,
        (
            "It appears Crossbell\x01",
            "Cathedral is within the\x01",
            "city barrier as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wanted to consult with Archbishop Eralda\x01",
            "about several things, but... Since I can't\x01",
            "contact him, there's nothing I can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F(Archbishop Eralda,\x01",
            "huh...? I wonder how\x01",
            "he's doing.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5857")

    label("loc_577B")


    ChrTalk(
        0xB,
        (
            "I wanted to consult with Archbishop Eralda\x01",
            "about several things, but... Since I can't\x01",
            "contact him, there's nothing I can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Maybe this another test the\x01",
            "Goddess gave me. I must work\x01",
            "hard for my patients' sake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5857")

    Jump("loc_62D2")

    label("loc_585C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_59CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_593D")

    ChrTalk(
        0xB,
        (
            "It's not just the\x01",
            "wounded who were injured\x01",
            "in the attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "There are also many who\x01",
            "suffered shock and have\x01",
            "stomach pain and the like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "They say the mind and\x01",
            "body are closely\x01",
            "connected.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_59C5")

    label("loc_593D")


    ChrTalk(
        0xB,
        (
            "There are people who develop\x01",
            "health disorders due to\x01",
            "mental strain as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "They say the mind and\x01",
            "body are closely\x01",
            "connected.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59C5")

    Jump("loc_62D2")

    label("loc_59CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5BFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B30")

    ChrTalk(
        0xB,
        (
            "Before, I had my doubts about\x01",
            "the act itself of using a\x01",
            "scalpel on a person's body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, as civilization advances, there are\x01",
            "many things that can't be solved with internal\x01",
            "medicine alone. ...Like this train accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "By working in the hospital, I\x01",
            "once again feel it's important to\x01",
            "accept new medical treatments.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5BF7")

    label("loc_5B30")


    ChrTalk(
        0xB,
        (
            "Using a scalpel on a person's\x01",
            "body... Rejecting that was an old\x01",
            "idea that lacked flexibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "By working in the hospital, I\x01",
            "once again feel it's important to\x01",
            "accept new medical treatments.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BF7")

    Jump("loc_62D2")

    label("loc_5BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5E13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D3B")

    ChrTalk(
        0xB,
        (
            "The human body possesses the\x01",
            "power to heal injuries and\x01",
            "illnesses to begin with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Many of medicines prescribed in internal\x01",
            "medicine treat illnesses by accelerating\x01",
            "this "self-healing capacity".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This essential point is present\x01",
            "in the Church. We physicians\x01",
            "operate on that basis.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5E0E")

    label("loc_5D3B")


    ChrTalk(
        0xB,
        (
            "The human body has the power to\x01",
            "heal injuries and illnesses... It\x01",
            "has a "self-healing capacity".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Many of the medicines prescribed in\x01",
            "internal medicine act as a natural\x01",
            "treatments by accelerating that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E0E")

    Jump("loc_62D2")

    label("loc_5E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5E60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E2E")
    Call(0, 12)
    Jump("loc_5E5B")

    label("loc_5E2E")


    ChrTalk(
        0xB,
        (
            "...*sigh*, it's time I\x01",
            "cooled my anger.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E5B")

    Jump("loc_62D2")

    label("loc_5E60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5E96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E7B")
    Call(0, 12)
    Jump("loc_5E91")

    label("loc_5E7B")


    ChrTalk(
        0xB,
        "Damn beardy...!!\x02",
    )

    CloseMessageWindow()

    label("loc_5E91")

    Jump("loc_62D2")

    label("loc_5E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5EA4")
    Jump("loc_62D2")

    label("loc_5EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_62D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61EE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_60D6")
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "Oh, if I remember correctly, you're the\x01",
            "officers from the Special Support Section.\x01",
            "Well, you came at the right time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Actually, I'm going to announce at an\x01",
            "academic meeting tomorrow my thesis about\x01",
            "the "Lupinus Grass" I was researching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I was just thinking I'd\x01",
            "tell you all about it as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FLupinus Grass is that...\x01",
            "medical herb you handled for\x01",
            "me in a previous request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*,\x01",
            "congratulations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes, it's thanks all of\x01",
            "you. Allow me to thank\x01",
            "you once again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61E6")

    label("loc_60D6")


    ChrTalk(
        0xB,
        (
            "*cough*! My name is\x01",
            "Ragot, in charge of\x01",
            "internal medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Actually, I'm going to announce my thesis\x01",
            "regarding the "Lupinus Grass" I was researching\x01",
            "at an academic conference tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hehe, it's really a\x01",
            "privilege. I must be in\x01",
            "perfect physical condition.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61E6")

    SetScenarioFlags(0x159, 7)
    Jump("loc_62D2")

    label("loc_61EE")


    ChrTalk(
        0xB,
        (
            "Tomorrow, I'm going to announce\x01",
            "my "Lupinus Grass" thesis at an\x01",
            "academic conference out of state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Actually, there's going to be an important\x01",
            "visitor at the hospital too... However,\x01",
            "there's nothing I can do about that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62D2")

    TalkEnd(0xFE)
    Return()

    # Function_11_5239 end

    def Function_12_62D6(): pass

    label("Function_12_62D6")

    OP_4B(0xB, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6489")

    ChrTalk(
        0xB,
        (
            "Professor Gary, I'll\x01",
            "assist you with your\x01",
            "surgery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Please prepare fresh\x01",
            "anaesthetics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...Hehe. It seems something\x01",
            "other than your bald head\x01",
            "is shining today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmph, same goes for your\x01",
            "dirty bearded face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I don't know why, but I feel\x01",
            "you look dignified today,\x01",
            "like "Back-Alley Dr. Glenn".\x02",
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
            "...Hehe, then let's\x01",
            "begin the surgery!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Right!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A8B")

    label("loc_6489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_66D6")

    ChrTalk(
        0xB,
        (
            "*cough*, Professor Gary.\x01",
            "...Well, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It seems your wife and child\x01",
            "live in Crossbell City... Were\x01",
            "you been able to contact them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "...No, not lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I see... That's\x01",
            "worrisome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...If you like, why don't you\x01",
            "discuss a return to Crossbell\x01",
            "City with the State Guard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "No... My wife and Kientz\x01",
            "can look after\x01",
            "themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I can't leave the hospital in a\x01",
            "situation where we don't know when\x01",
            "heavily injured patients will arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's the same for you,\x01",
            "right, Professor Ragot?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Yes, that's true. It\x01",
            "seems my concern was\x01",
            "unnecessary.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A8B")

    label("loc_66D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6887")

    ChrTalk(
        0xB,
        (
            "Seiland's surgical technique\x01",
            "is probably the best that can\x01",
            "be thought of at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Could your ineptitude\x01",
            "be the reason for its\x01",
            "failure?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Wh... You too. Couldn't you have made\x01",
            "a mistake because your hands trembled\x01",
            "in a surgery you're not used to!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#4SWhat did you...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#4SWanna go at it!?\x02",
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
            "...Let's let it slide,\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...Right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A8B")

    label("loc_6887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6A8B")

    ChrTalk(
        0xB,
        (
            "At the academic conference\x01",
            "the other day, my thesis\x01",
            "was highly praised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Dear me, I would've liked\x01",
            "for you to see my gallant\x01",
            "figure there too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The other day, I received words of\x01",
            "encouragement directly from Archduke\x01",
            "Albert who came to inspect the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            ""The growth of future surgical treatments\x01",
            "rest upon your shoulders"... Man, I'm\x01",
            "really grateful for what he said.\x02",
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
        (
            "#4SDon't get elated, you\x01",
            "beardy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#4SThat's my line, you\x01",
            "baldy!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6A9E")
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xE, 0x10)

    label("loc_6A9E")

    SetScenarioFlags(0x2, 0)
    OP_4C(0xB, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_12_62D6 end

    def Function_13_6AAA(): pass

    label("Function_13_6AAA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6C74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BB7")

    ChrTalk(
        0xC,
        (
            "It seems there are people whose\x01",
            "health is worsening due to anxiety\x01",
            "regarding this abnormal situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The field of the mind is outside this\x01",
            "hospital's expertise, but I must be able to\x01",
            "give at least some advice to those patients.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6C6F")

    label("loc_6BB7")


    ChrTalk(
        0xC,
        (
            "By its very nature, the field\x01",
            "of the mind is the Church's\x01",
            "area of expertise...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "However, since they've come to\x01",
            "the hospital, I must be able to\x01",
            "give them at least some advice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C6F")

    Jump("loc_747B")

    label("loc_6C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_6D57")

    ChrTalk(
        0xC,
        (
            "With the professors' help, we removed\x01",
            "all samples of medicinal plants that\x01",
            "were stored in the research building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Times are hard for many different\x01",
            "reasons, but rather than waiting,\x01",
            "we must do something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_747B")

    label("loc_6D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_6D65")
    Jump("loc_747B")

    label("loc_6D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6D73")
    Jump("loc_747B")

    label("loc_6D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6D81")
    Jump("loc_747B")

    label("loc_6D81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6EC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E4C")

    ChrTalk(
        0xC,
        (
            "Because a lot of patients arrived\x01",
            "the other day, I've been working\x01",
            "non-stop. I'm almost at my limit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I guess I'll go take a\x01",
            "nap at the dorm after a\x01",
            "little more work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6EBB")

    label("loc_6E4C")


    ChrTalk(
        0xC,
        (
            "Even so, although she's\x01",
            "been working non-stop,\x01",
            "the professor is tough...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I must gain stamina\x01",
            "myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EBB")

    Jump("loc_747B")

    label("loc_6EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6ECE")
    Jump("loc_747B")

    label("loc_6ECE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6F9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EE9")
    Call(0, 37)
    Jump("loc_6F96")

    label("loc_6EE9")


    ChrTalk(
        0xC,
        (
            "I heard a story where a patient's\x01",
            "illness was cured after enjoying\x01",
            "theater and plays.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If it's really true, I'm\x01",
            "glad he's spending time\x01",
            "with his grandchild lately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F96")

    Jump("loc_747B")

    label("loc_6F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6FA9")
    Jump("loc_747B")

    label("loc_6FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_73EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_713B")

    ChrTalk(
        0xC,
        (
            "When I learned Dr. Joachim\x01",
            "was the mastermind behind\x01",
            "that incident, I was shocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even after Dr. Seiland took\x01",
            "her post as my new superior, I\x01",
            "felt down for a while, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            ""As long as there are patients, we\x01",
            "have no time to be feeling down."\x01",
            "...That's what she said to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For now anyway, I intend\x01",
            "to work diligently under\x01",
            "the doctor's tutelage.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_71E8")

    label("loc_713B")


    ChrTalk(
        0xC,
        (
            "Dr. Seiland is giving me one job\x01",
            "after the next. Thanks to that,\x01",
            "I have no time to feel down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha. That strictness\x01",
            "might be the doctor's\x01",
            "way of showing kindness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71E8")

    Jump("loc_73E5")

    label("loc_71ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7302")

    ChrTalk(
        0xC,
        (
            "After the prepared medicine took effect, the\x01",
            "patient's condition stabilised. With this, there's\x01",
            "nothing to worry about for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Nevertheless, His Excellency the Archduke\x01",
            "seems to have considerable medical\x01",
            "knowledge. I want to be like him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73E5")

    label("loc_7302")


    ChrTalk(
        0xC,
        (
            "It seems that His Excellency the\x01",
            "Archduke and Professor Seiland\x01",
            "have been friends for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Professor Seiland talking like she always\x01",
            "does to His Excellency the Archduke made\x01",
            "me feel nervous for some reason...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73E5")

    Jump("loc_747B")

    label("loc_73EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_747B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7405")
    Call(0, 39)
    Jump("loc_747B")

    label("loc_7405")


    ChrTalk(
        0xC,
        (
            "I'm also very happy that\x01",
            "Mr. Quine was able to\x01",
            "take his medicines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This is all thanks to\x01",
            "Amisaah's efforts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_747B")

    TalkEnd(0xFE)
    Return()

    # Function_13_6AAA end

    def Function_14_747F(): pass

    label("Function_14_747F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7536")

    ChrTalk(
        0xD,
        (
            "We're flooded with\x01",
            "patients and quite busy,\x01",
            "but... I'm gonna do it!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'm not there yet, but I'll be\x01",
            "a capable female doctor like\x01",
            "Professor Seiland someday!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8046")

    label("loc_7536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_75D3")

    ChrTalk(
        0xD,
        (
            "Unexpectedly, even folk\x01",
            "remedies could be useful\x01",
            "as reference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I think I left it on the\x01",
            "dorm bookshelves. I'll\x01",
            "go look for it later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8046")

    label("loc_75D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_780A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7711")

    ChrTalk(
        0xD,
        (
            "I'm arranging the medicines\x01",
            "that were provided by the\x01",
            "State Guard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Really though, it seems\x01",
            "like something a novice\x01",
            "put together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We'll be able to manage for the time being, but\x01",
            "if a patient with an incurable disease came, as\x01",
            "you can expect we wouldn't be able treat them...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7805")

    label("loc_7711")


    ChrTalk(
        0xD,
        (
            "The medicines the State Guard\x01",
            "provided really feel like\x01",
            "something a novice put together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We'll be able to manage for the time being, but\x01",
            "if a patient with an incurable disease came, as\x01",
            "you can expect we wouldn't be able treat them...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7805")

    Jump("loc_8046")

    label("loc_780A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_78B8")

    ChrTalk(
        0xD,
        (
            "Though we've stopped receiving\x01",
            "outpatients, we don't know when a patient\x01",
            "with a serious illness will come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We must at least make\x01",
            "proper preparations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8046")

    label("loc_78B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7A58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79C3")

    ChrTalk(
        0xD,
        (
            ""In times like these, a doctor\x01",
            "must not appear depressed..."\x01",
            "Professor Ragot taught me that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If there was worry on my face,\x01",
            "it would pass to the patient\x01",
            "as well. I must be careful...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Worry could be like an\x01",
            "illness, in a way.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7A53")

    label("loc_79C3")


    ChrTalk(
        0xD,
        (
            ""In times like this, a\x01",
            "doctor must not show\x01",
            "appear depressed..."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...I understand it with\x01",
            "my head, but it could be\x01",
            "difficult for me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A53")

    Jump("loc_8046")

    label("loc_7A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7C01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B61")

    ChrTalk(
        0xD,
        (
            "When you're hit by the\x01",
            "rain and soaking wet, it's\x01",
            "easy to catch a cold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The cause seems to be that\x01",
            "the body's immunity doesn't\x01",
            "work when we get cold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Make sure to change clothes\x01",
            "and warm up when you get\x01",
            "home too, you guys.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7BFC")

    label("loc_7B61")


    ChrTalk(
        0xD,
        (
            "When you're hit by the\x01",
            "rain and soaking wet, it's\x01",
            "easy to catch a cold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Make sure to change clothes\x01",
            "and warm up when you get\x01",
            "home too, you guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BFC")

    Jump("loc_8046")

    label("loc_7C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7CB2")

    ChrTalk(
        0xD,
        (
            "Lytton seems to be\x01",
            "making many hospital\x01",
            "rounds as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Mrgrgr, I won't lose either. I\x01",
            "will become a dependable female\x01",
            "doctor who patients can trust!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8046")

    label("loc_7CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7CC0")
    Jump("loc_8046")

    label("loc_7CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7E26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DB1")

    ChrTalk(
        0xD,
        (
            "Oh jeez, the professors\x01",
            "seem to be quarreling\x01",
            "again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "When they get like this, it's\x01",
            "quicker to let them finish\x01",
            "rather than ineptly intervene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I guess I'll sort out\x01",
            "the clinical records\x01",
            "while I can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7E21")

    label("loc_7DB1")


    ChrTalk(
        0xD,
        (
            "I'm already used to the\x01",
            "professors' quarrels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I guess I'll sort out\x01",
            "the clinical records\x01",
            "while I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E21")

    Jump("loc_8046")

    label("loc_7E26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7EDC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E9D")

    ChrTalk(
        0xD,
        (
            "The professor is really\x01",
            "great...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...No, I mustn't. I must\x01",
            "properly do what I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7ED7")

    label("loc_7E9D")


    ChrTalk(
        0xD,
        (
            "Even so, I'm so\x01",
            "pathetic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I have to study more.\x02",
    )

    CloseMessageWindow()

    label("loc_7ED7")

    Jump("loc_8046")

    label("loc_7EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8046")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FE3")

    ChrTalk(
        0xD,
        (
            "Recently, Flora, my roommate\x01",
            "at the dorm, is taking care\x01",
            "of a new intern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Micheau, I think his name was?\x01",
            "I'm reminded of the time when\x01",
            "I was new, for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, it doesn't change\x01",
            "the fact that I'm still\x01",
            "studying.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8046")

    label("loc_7FE3")


    ChrTalk(
        0xD,
        (
            "Looking at Micheau, I'm\x01",
            "reminded of the when I\x01",
            "was new.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, I'm still studying\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8046")

    TalkEnd(0xFE)
    Return()

    # Function_14_747F end

    def Function_15_804A(): pass

    label("Function_15_804A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_80F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8068")
    Call(0, 12)
    Jump("loc_80F2")

    label("loc_8068")


    ChrTalk(
        0xE,
        (
            "I don't like Professor Ragot,\x01",
            "but I can't rely on anyone\x01",
            "else's support but his.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hehe. I feel I can do\x01",
            "any kind of surgery now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80F2")

    Jump("loc_8C84")

    label("loc_80F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_8263")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81E9")

    ChrTalk(
        0xE,
        (
            "It seems they're trying to do something about\x01",
            "the lack of medical supplies in internal\x01",
            "medicine and neurology/pharmacology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...I can't operate now, so\x01",
            "while I'm not working I'm\x01",
            "helping Ashram and Chaleur.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_825E")

    label("loc_81E9")


    ChrTalk(
        0xE,
        (
            "While not working I'm\x01",
            "helping Ashram and\x01",
            "Chaleur.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Preparations must be\x01",
            "perfect so we can\x01",
            "operate any time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_825E")

    Jump("loc_8C84")

    label("loc_8263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_830D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_827E")
    Call(0, 12)
    Jump("loc_8308")

    label("loc_827E")


    ChrTalk(
        0xE,
        (
            "...Even Professor Ragot\x01",
            "says clever things,\x01",
            "occasionally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, since my wife and\x01",
            "Kientz surely fine,\x01",
            "there's no need to worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8308")

    Jump("loc_8C84")

    label("loc_830D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_8420")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8393")

    ChrTalk(
        0xE,
        (
            "...I wonder how my wife\x01",
            "and Kientz in the city\x01",
            "are doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I hope they're not sick\x01",
            "or anything...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_841B")

    label("loc_8393")


    ChrTalk(
        0xE,
        (
            "...*sigh*, I'll stop\x01",
            "worrying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "They haven't been taken here, so\x01",
            "there's no doubt that my wife\x01",
            "and Kientz are doing just fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_841B")

    Jump("loc_8C84")

    label("loc_8420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_858A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_851B")

    ChrTalk(
        0xE,
        (
            "I've worked at the hospital for many\x01",
            "years, but this is the first time we've\x01",
            "had enough inpatients to fill all rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "You could say it's truly an\x01",
            "unprecedented situation. We must\x01",
            "get through it somehow or other...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8585")

    label("loc_851B")


    ChrTalk(
        0xE,
        (
            "This situation... You could say\x01",
            "it's truly unprecedented. We must\x01",
            "get through it somehow or other...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8585")

    Jump("loc_8C84")

    label("loc_858A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8712")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8660")

    ChrTalk(
        0xE,
        (
            "Phew... I ended the\x01",
            "surgery moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Anyway, there's a lot of\x01",
            "patients. Treating them\x01",
            "all took until morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "After I finish today's\x01",
            "exams, I want to sleep\x01",
            "like a log.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_870D")

    label("loc_8660")


    ChrTalk(
        0xE,
        (
            "I'm tired due to surgeries that\x01",
            "took until morning, but... I\x01",
            "can't make the patients wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I have to do my job\x01",
            "properly until I'm through\x01",
            "with today's treatments.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_870D")

    Jump("loc_8C84")

    label("loc_8712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_88C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8827")

    ChrTalk(
        0xE,
        (
            "Recently, it seems that\x01",
            "my son, Kientz, is\x01",
            "worried about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "*sigh*, I'm busy with my\x01",
            "job at the hospital and\x01",
            "my worries never cease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If I'm careless, I could be stuck\x01",
            "getting stomach pains and being\x01",
            "treated by Professor Ragot.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_88C2")

    label("loc_8827")


    ChrTalk(
        0xE,
        (
            "Oh man, my public and\x01",
            "private worries never\x01",
            "cease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If I'm careless, I could be stuck\x01",
            "getting stomach pains and being\x01",
            "treated by Professor Ragot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88C2")

    Jump("loc_8C84")

    label("loc_88C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_899A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88E2")
    Call(0, 12)
    Jump("loc_8995")

    label("loc_88E2")


    ChrTalk(
        0xE,
        (
            "We participated in the surgery\x01",
            "too, but this time we were forced\x01",
            "to realize our helplessness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Will this failure throw\x01",
            "the patient in despair...?\x01",
            "That's my only concern.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8995")

    Jump("loc_8C84")

    label("loc_899A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_89E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89B5")
    Call(0, 12)
    Jump("loc_89DB")

    label("loc_89B5")


    ChrTalk(
        0xE,
        (
            "Don't get carried away,\x01",
            "baldyyy!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89DB")

    Jump("loc_8C84")

    label("loc_89E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8AFE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8A61")

    ChrTalk(
        0xE,
        (
            "It seems His Excellency\x01",
            "the Archduke has left...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "*sigh*, oh man...\x01",
            "Ashram's troublesome\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AF9")

    label("loc_8A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A73")
    Call(0, 16)
    Jump("loc_8AF9")

    label("loc_8A73")


    ChrTalk(
        0xE,
        (
            "His Excellency the Archduke\x01",
            "came to observe, and yet she's\x01",
            "doing things at her own pace...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I have to severely scold\x01",
            "Ashram!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AF9")

    Jump("loc_8C84")

    label("loc_8AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8C84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BE4")

    ChrTalk(
        0xE,
        (
            "Damn Professor Ragot,\x01",
            "he's always so full of\x01",
            "himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Every single time we meet,\x01",
            "he brags pretentiously.\x01",
            "Jeez, that damn baldy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...Well, it's true that\x01",
            "his research is worthy\x01",
            "of praise.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8C84")

    label("loc_8BE4")


    ChrTalk(
        0xE,
        (
            "I have no choice but to\x01",
            "acknowledge Professor\x01",
            "Ragot's research results.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "His pride gets on my nerves,\x01",
            "but... Hmph, I'll endure it,\x01",
            "but just this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C84")

    TalkEnd(0xFE)
    Return()

    # Function_15_804A end

    def Function_16_8C88(): pass

    label("Function_16_8C88")

    OP_4B(0xE, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xE,
        (
            "C-Chaleur, has Ashram\x01",
            "slept in!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Yes, most likely. ...It seems she\x01",
            "holed up in the research building\x01",
            "until late again yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "T-The Archduke is coming\x01",
            "to inspect, and yet\x01",
            "she... How slovenly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Damn, go get her out of\x01",
            "bed no matter what!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0x10, 0x10)
    OP_4C(0xE, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_16_8C88 end

    def Function_17_8DAC(): pass

    label("Function_17_8DAC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8F25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E84")

    ChrTalk(
        0xF,
        (
            "The huge tree that has\x01",
            "appeared near the\x01",
            "Marshlands is too cool...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Under what principles and for what\x01",
            "purpose did it appear there...? It's\x01",
            "not lacking for scientific interest!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8F20")

    label("loc_8E84")


    ChrTalk(
        0xF,
        (
            "...Ah, I got carried\x01",
            "away. I'm sorry, at a\x01",
            "time like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Anyhow, I've got to properly\x01",
            "maintain our medical instruments\x01",
            "for treating patients.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F20")

    Jump("loc_9DE8")

    label("loc_8F25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9080")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FE2")

    ChrTalk(
        0xF,
        "So sleepy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I'm checking our old\x01",
            "medical instruments for\x01",
            "when the newer ones break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "*yaaaaaaawn*... I'm\x01",
            "sleepy, but I've got to\x01",
            "do it properly...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_907B")

    label("loc_8FE2")


    ChrTalk(
        0xF,
        (
            "So sleepy... Nevertheless,\x01",
            "the old stuff is\x01",
            "surprisingly sturdy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Many are large and\x01",
            "unrefined... It seems it would\x01",
            "feel nice to lie on them...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_907B")

    Jump("loc_9DE8")

    label("loc_9080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_9224")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_917E")

    ChrTalk(
        0xF,
        (
            "I found a spare part\x01",
            "that had deteriorated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "However, because it's a unique part,\x01",
            "we won't be able to get a new one\x01",
            "unless we order it from Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "*sigh*, what a problem.\x01",
            "I must use it carefully,\x01",
            "carefully...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_921F")

    label("loc_917E")


    ChrTalk(
        0xF,
        (
            "Parts for our medical instruments\x01",
            "can't be obtained unless we order\x01",
            "them from Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "*sigh*, what a problem.\x01",
            "I must use it carefully,\x01",
            "carefully...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_921F")

    Jump("loc_9DE8")

    label("loc_9224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_94DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_942F")
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xF,
        "Ah, Tio.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I'm currently maintaining our\x01",
            "medical instruments... What do\x01",
            "you think about these values?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FHmm... The durability is\x01",
            "slightly less than the\x01",
            "minimum required value.\x02\x03",
            "#00203FI think the moving parts\x01",
            "are most likely\x01",
            "degrading due to aging.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "As I thought, then. Hmm,\x01",
            "how troublesome...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(In the time she's been\x01",
            "here, they seem to have\x01",
            "grown quite close...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F(Hehe. If it's the field of\x01",
            "orbal tools, I bet she's\x01",
            "been pretty useful here.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_94D6")

    label("loc_942F")


    ChrTalk(
        0xF,
        (
            "Hmm, how troublesome. They're\x01",
            "made by Seiland Corp., so we\x01",
            "can't order new ones...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "However, I'll have to do\x01",
            "something. For now, I'll\x01",
            "look around for spares.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94D6")

    Jump("loc_9DE8")

    label("loc_94DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9654")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95BA")

    ChrTalk(
        0xF,
        (
            "Hmm. I'll have make my\x01",
            "rounds in the research\x01",
            "building's ICU later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I must check on\x01",
            "Donovan's artificial\x01",
            "respirator too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "*sigh*. The work\x01",
            "increased all at once\x01",
            "and I'm really busy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_964F")

    label("loc_95BA")


    ChrTalk(
        0xF,
        (
            "*sigh*. The work\x01",
            "increased all at once\x01",
            "and I'm really busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It seems it'll be a long\x01",
            "time until I can go back to\x01",
            "my full days of research.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_964F")

    Jump("loc_9DE8")

    label("loc_9654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9756")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96FF")

    ChrTalk(
        0xF,
        (
            "Yesterday, the medical\x01",
            "instruments for surgery\x01",
            "were used an awful lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I'm really glad I asked\x01",
            "Chaleur to do the\x01",
            "regular maintenance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9751")

    label("loc_96FF")


    ChrTalk(
        0xF,
        (
            "The medical internals are\x01",
            "all excellent kids too, so\x01",
            "they help me out a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9751")

    Jump("loc_9DE8")

    label("loc_9756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9942")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98BF")

    ChrTalk(
        0xF,
        (
            "*drowsy, drowsy*...\x01",
            "...Oh, that's right!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "By applying the principles of the exposure quartz and\x01",
            "using a device that sends visual information to the brain,\x01",
            "it might be possible to enhance eyesight artificially...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "(*clakclak clakclak clakclak*...)\x01",
            "...Hmm, no good, as I feared. It would\x01",
            "take several decades to develop...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_993D")

    label("loc_98BF")


    ChrTalk(
        0xF,
        (
            "No uuuse... As I feared,\x01",
            "maybe it's impossible\x01",
            "for me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "...No, I can't give up.\x01",
            "Fight, me! For Shizuku's\x01",
            "sake too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_993D")

    Jump("loc_9DE8")

    label("loc_9942")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9AE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A3C")

    ChrTalk(
        0xF,
        (
            "For Shizuku's surgery, you could\x01",
            "say we prepared the world's most\x01",
            "advanced medical equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "That it would end up\x01",
            "failing is... Ugh, I\x01",
            "can't accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It's inexcusable towards\x01",
            "Shizuku who believed in\x01",
            "us...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9ADE")

    label("loc_9A3C")


    ChrTalk(
        0xF,
        (
            "Making people happy with science...\x01",
            "In order to do that, I kept\x01",
            "researching medical instruments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It's inexcusable towards\x01",
            "Shizuku who believed in\x01",
            "us...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9ADE")

    Jump("loc_9DE8")

    label("loc_9AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9BBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AFE")
    Call(0, 18)
    Jump("loc_9BB9")

    label("loc_9AFE")

    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xF,
        (
            "...Yes, good, good! It\x01",
            "it went well this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Haha. At this rate, I guess\x01",
            "I'll keep going until the\x01",
            "endurance tests today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "(The full course today\x01",
            "too, I guess...)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)

    label("loc_9BB9")

    Jump("loc_9DE8")

    label("loc_9BBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9BCC")
    Jump("loc_9DE8")

    label("loc_9BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9DE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D47")

    ChrTalk(
        0xF,
        (
            "When I heard Professor Seiland\x01",
            "had been appointed here, I felt\x01",
            "like I could jump for joy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Due to the nature of my job, I see the\x01",
            "name of Seiland Corp., the major\x01",
            "medical equipment manufacturer, daily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "She seems to be a relative of the president...\x01",
            "Uhuhu, it would be nice if I could get some\x01",
            "behind-the-scenes stories about the company.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9DE8")

    label("loc_9D47")


    ChrTalk(
        0xF,
        (
            "However, Professor\x01",
            "Seiland is scary\x01",
            "somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I'd like to ask her many stories\x01",
            "about Seiland Corporation, but... I\x01",
            "can't quite find the right timing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DE8")

    TalkEnd(0xFE)
    Return()

    # Function_17_8DAC end

    def Function_18_9DEC(): pass

    label("Function_18_9DEC")

    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xF,
        (
            "Alright, Chaleur. I'm\x01",
            "ready here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Please adjust the orbal\x01",
            "pressure after I switch\x01",
            "it on.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    ChrTalk(
        0x10,
        (
            "Roger. ...Let's hope it\x01",
            "doesn't explode this\x01",
            "time, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Don't mind it even if it\x01",
            "does♪ Mistakes are the mother\x01",
            "of success, after all.\x02",
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
            "#00211F(...She isn't wrong, but\x01",
            "that's dangerous.)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x2, 2)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_93(0x10, 0x5A, 0x0)
    Return()

    # Function_18_9DEC end

    def Function_19_9FA2(): pass

    label("Function_19_9FA2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A150")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0AC")

    ChrTalk(
        0x10,
        (
            "The chief had been sleepy for a\x01",
            "while, but after she saw that tree\x01",
            "appear, she's been excited like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "With the chief in that state, she'll\x01",
            "probably work for three days and three\x01",
            "nights straight. I have to keep up with her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A14B")

    label("loc_A0AC")


    ChrTalk(
        0x10,
        (
            "The civil war in the\x01",
            "Empire... That bluish\x01",
            "huge tree...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I'm worried about a lot of things,\x01",
            "but for now I have to focus on\x01",
            "keeping up with the chief.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A14B")

    Jump("loc_B01F")

    label("loc_A150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_A2B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A23E")

    ChrTalk(
        0x10,
        (
            "Hmm. Their efficiency is\x01",
            "rather low but it seems they\x01",
            "can be used in an emergency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Because there are a lot of\x01",
            "them, we ended up checking\x01",
            "them all night long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "...Well, this always\x01",
            "happens, so...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A2B2")

    label("loc_A23E")


    ChrTalk(
        0x10,
        (
            "After an checking them\x01",
            "all night long, Chief\x01",
            "Ashram looks sleepy too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "...Well, this always\x01",
            "happens, so...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2B2")

    Jump("loc_B01F")

    label("loc_A2B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_A39C")

    ChrTalk(
        0x10,
        (
            "Professor Gary is probably worried about\x01",
            "his family too, but he seems to be\x01",
            "concentrating on his job at the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "...I will believe in my family's\x01",
            "safety too and focus on helping\x01",
            "Chief Ashram for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B01F")

    label("loc_A39C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A58E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4E3")

    ChrTalk(
        0x10,
        (
            "A recall notice came from the Empire\x01",
            "right before Crossbell's independence,\x01",
            "but I decided to stay here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Since I still have many\x01",
            "things to learn, I can't\x01",
            "return to my home country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "...Still, the civil war that broke out\x01",
            "in the Empire is a little concerning.\x01",
            "I hope my family is safe...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A589")

    label("loc_A4E3")


    ChrTalk(
        0x10,
        (
            "At this late hour, I don't\x01",
            "have any regrets about\x01",
            "having stayed in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "...Still, the civil war in\x01",
            "the Empire worries me. I\x01",
            "hope my family is safe...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A589")

    Jump("loc_B01F")

    label("loc_A58E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A75A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6B5")

    ChrTalk(
        0x10,
        (
            "It's been rumored that\x01",
            "the attack was a plot by\x01",
            "the Imperial government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "That incident where a lot of\x01",
            "people were brought to the\x01",
            "hospital was the Empire's doing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I don't want to bad mouth my\x01",
            "home country, but if that's\x01",
            "true, I'll hold it in contempt.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A755")

    label("loc_A6B5")


    ChrTalk(
        0x10,
        (
            "My goal was to practice\x01",
            "in my home country, the\x01",
            "Empire, in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If it's really an Imperial\x01",
            "government plot, I'll hold\x01",
            "my homeland in contempt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A755")

    Jump("loc_B01F")

    label("loc_A75A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A8E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A88B")

    ChrTalk(
        0x10,
        (
            "For medical instruments,\x01",
            "habitual and detailed\x01",
            "maintenance is essential.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If something were to happen to a patient\x01",
            "due to the breakdown of a medical tool,\x01",
            "that would defeat its purpose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I must do proper maintenance\x01",
            "so they're ready for\x01",
            "whenever a patient arrives.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A8DE")

    label("loc_A88B")


    ChrTalk(
        0x10,
        (
            "I must do proper maintenance\x01",
            "so they're ready for\x01",
            "whenever a patient arrives.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8DE")

    Jump("loc_B01F")

    label("loc_A8E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_AABA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9FA")

    ChrTalk(
        0x10,
        (
            "After Shizuku's surgery, the\x01",
            "chief has been researching\x01",
            "something without rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "It seems she's looking for\x01",
            "a method to cure Shizuku's\x01",
            "eyes using orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "As I thought, the chief is\x01",
            "amazing... I didn't even\x01",
            "think of something like that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_AAB5")

    label("loc_A9FA")


    ChrTalk(
        0x10,
        (
            "Restoring eyesight using\x01",
            "orbments, huh...? I didn't even\x01",
            "think of something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "However, it's tied to the field\x01",
            "of neurology as well... It\x01",
            "might be difficult to realize.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAB5")

    Jump("loc_B01F")

    label("loc_AABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AC44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABB7")

    ChrTalk(
        0x10,
        (
            "Regarding the surgery, I\x01",
            "think that the professors\x01",
            "did their very best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Even so, I can't help but say\x01",
            "that it's a pity she didn't\x01",
            "completely recover, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Personally, I'd like it\x01",
            "if they weren't so\x01",
            "depressed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_AC3F")

    label("loc_ABB7")


    ChrTalk(
        0x10,
        (
            "Regarding the surgery, I\x01",
            "think that the professors\x01",
            "did their very best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Personally, I'd like it\x01",
            "if they weren't so\x01",
            "depressed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC3F")

    Jump("loc_B01F")

    label("loc_AC44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_ACFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC5F")
    Call(0, 18)
    Jump("loc_ACFA")

    label("loc_AC5F")


    ChrTalk(
        0x10,
        (
            "No matter how often she\x01",
            "fails, Chief Ashram\x01",
            "doesn't get discouraged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Maybe I should try to emulate\x01",
            "her guts as a medical\x01",
            "instruments researcher.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACFA")

    Jump("loc_B01F")

    label("loc_ACFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_AE80")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_ADE1")

    ChrTalk(
        0x10,
        (
            "In the end, Chief Ashram\x01",
            "didn't make it, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Well, chief pulled an all nighter the other day\x01",
            "as well, so I didn't think in the slightest that\x01",
            "she'd make it it in time for the inspection.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE7B")

    label("loc_ADE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADF3")
    Call(0, 16)
    Jump("loc_AE7B")

    label("loc_ADF3")


    ChrTalk(
        0x10,
        (
            "Chief Ashram often stays\x01",
            "up all night working\x01",
            "hard on her research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "She should be still\x01",
            "sleeping at the\x01",
            "dormitory around now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE7B")

    Jump("loc_B01F")

    label("loc_AE80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B01F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF8F")

    ChrTalk(
        0x10,
        (
            "Chief Ashram is an\x01",
            "expert on medical\x01",
            "instruments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "The chief studied the basics of orbal\x01",
            "equipment at Epstein Foundation HQ in\x01",
            "Lｳman State, where she's from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I'm helping out in\x01",
            "researching different medical\x01",
            "instruments under her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_B01F")

    label("loc_AF8F")


    ChrTalk(
        0x10,
        (
            "Medical instruments are\x01",
            "indispensable for modern\x01",
            "medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I believe this research\x01",
            "will open a path to the\x01",
            "future of medical science.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B01F")

    TalkEnd(0xFE)
    Return()

    # Function_19_9FA2 end

    def Function_20_B023(): pass

    label("Function_20_B023")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B0BA")

    ChrTalk(
        0x11,
        (
            "I'm relieved they've\x01",
            "started accepting\x01",
            "outpatients again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I ran out of the medicine\x01",
            "I was taking and I\x01",
            "wondered what to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B461")

    label("loc_B0BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_B0C8")
    Jump("loc_B461")

    label("loc_B0C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B0D6")
    Jump("loc_B461")

    label("loc_B0D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B18C")

    ChrTalk(
        0x11,
        (
            "Hmm, they're not calling for\x01",
            "me... I guess the medical\x01",
            "exams are greatly delayed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "There was that attack, so\x01",
            "the doctors are probably\x01",
            "quite busy themselves...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B461")

    label("loc_B18C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B19A")
    Jump("loc_B461")

    label("loc_B19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B24B")

    ChrTalk(
        0x11,
        (
            "I have an appointment\x01",
            "first thing this\x01",
            "morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I used the orbal net to make the\x01",
            "appointment. It was really convenient,\x01",
            "just like I thought it would be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B461")

    label("loc_B24B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B259")
    Jump("loc_B461")

    label("loc_B259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B39B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B327")

    ChrTalk(
        0x11,
        (
            "The other day, I looked up\x01",
            "at that Orchis Tower at the\x01",
            "unveiling ceremony and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I overstretched my back.\x01",
            "I inadvertently ended up\x01",
            "hurting my hips.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Oow ow ow ow...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B396")

    label("loc_B327")


    ChrTalk(
        0x11,
        (
            "I looked up at Orchis Tower\x01",
            "for too long and inadvertently\x01",
            "ended up hurting my hips.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Oow ow ow ow...\x02",
    )

    CloseMessageWindow()

    label("loc_B396")

    Jump("loc_B461")

    label("loc_B39B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B3A9")
    Jump("loc_B461")

    label("loc_B3A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B461")

    ChrTalk(
        0x11,
        (
            "After the cult incident, the\x01",
            "hospital did a prompt investigation\x01",
            "and proved their innocence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It's really a nice to be\x01",
            "able to commute to the\x01",
            "hospital without worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B461")

    TalkEnd(0xFE)
    Return()

    # Function_20_B023 end

    def Function_21_B465(): pass

    label("Function_21_B465")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B4F5")

    ChrTalk(
        0x12,
        (
            "To us elderly, it's very\x01",
            "important to have a\x01",
            "hospital we can go to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I'm really glad I'm able\x01",
            "to come here like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B7E6")

    label("loc_B4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_B503")
    Jump("loc_B7E6")

    label("loc_B503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B511")
    Jump("loc_B7E6")

    label("loc_B511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B587")

    ChrTalk(
        0x12,
        (
            "*sigh*... I wonder if\x01",
            "Crossbell is really all\x01",
            "right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I'm so worried I can't\x01",
            "sleep at night...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B7E6")

    label("loc_B587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B5ED")

    ChrTalk(
        0x12,
        (
            "A derailment... What a\x01",
            "shock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I wonder the passengers\x01",
            "are all safe and sound.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B7E6")

    label("loc_B5ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B5FB")
    Jump("loc_B7E6")

    label("loc_B5FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B692")

    ChrTalk(
        0x12,
        (
            "I've been coming to this\x01",
            "hospital for some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "The doctors are even skilled\x01",
            "surgeons... I have no\x01",
            "worries about coming here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B7E6")

    label("loc_B692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B6A0")
    Jump("loc_B7E6")

    label("loc_B6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B740")

    ChrTalk(
        0x12,
        (
            "It seems my doctor, Dr.\x01",
            "Ragot, is absent today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "That Dr. Seiland... She's young\x01",
            "for a doctor. I wonder if\x01",
            "everything will be all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B7E6")

    label("loc_B740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B7E6")

    ChrTalk(
        0x12,
        (
            "Even now I can't believe\x01",
            "that Dr. Joachim caused such\x01",
            "an outrageous incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Aah, scary, scary... You\x01",
            "really never know what\x01",
            "people are thinking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7E6")

    TalkEnd(0xFE)
    Return()

    # Function_21_B465 end

    def Function_22_B7EA(): pass

    label("Function_22_B7EA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B8F2")

    ChrTalk(
        0x13,
        (
            "Before President Dieter was arrested,\x01",
            "he wouldn't allow me to come to the\x01",
            "hospital for a minor illness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "However, to a parent, illnesses of their\x01",
            "children are important, even if it's a mere\x01",
            "cold. I wish he were a little more considerate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCC6")

    label("loc_B8F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_B900")
    Jump("loc_BCC6")

    label("loc_B900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B90E")
    Jump("loc_BCC6")

    label("loc_B90E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B95F")

    ChrTalk(
        0x13,
        "Hey... Quiet down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "You mustn't cause\x01",
            "trouble for others.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCC6")

    label("loc_B95F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BA2A")

    ChrTalk(
        0x13,
        (
            "We were on the train that\x01",
            "derailed. Luckily, we\x01",
            "suffered only minor injuries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I'm glad we'll be discharged in just\x01",
            "one day, but I wonder what happened\x01",
            "to the railroad after that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCC6")

    label("loc_BA2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BA38")
    Jump("loc_BCC6")

    label("loc_BA38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BBB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB42")

    ChrTalk(
        0x13,
        (
            "I was warned that I eat\x01",
            "too many sweets at a\x01",
            "recent medical check-up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "They say it'll be bad for\x01",
            "me at this rate, so I'm\x01",
            "reconsidering my lifestyle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Even so, I reach for sweet\x01",
            "things without thinking.\x01",
            "I've got to be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_BBAC")

    label("loc_BB42")


    ChrTalk(
        0x13,
        (
            "I reach for sweet things\x01",
            "without thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "My health is on the\x01",
            "line, so I've got to be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBAC")

    Jump("loc_BCC6")

    label("loc_BBB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_BBBF")
    Jump("loc_BCC6")

    label("loc_BBBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_BCBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC2F")

    ChrTalk(
        0x13,
        "Mmm, what a nice smell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Things like this make a\x01",
            "patient feel at ease.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    ClearChrFlags(0x13, 0x10)
    Jump("loc_BCB8")

    label("loc_BC2F")


    ChrTalk(
        0x13,
        (
            "I came to the hospital\x01",
            "to accompany my mother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "It seems there are many unique\x01",
            "things here, so I guess I'll\x01",
            "take a look around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCB8")

    Jump("loc_BCC6")

    label("loc_BCBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BCC6")

    label("loc_BCC6")

    TalkEnd(0xFE)
    Return()

    # Function_22_B7EA end

    def Function_23_BCCA(): pass

    label("Function_23_BCCA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BD71")

    ChrTalk(
        0x14,
        (
            "I finally made it to the\x01",
            "hospital, but it's\x01",
            "incredibly crowded...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "The doctors must be having\x01",
            "a hard time too. I hope\x01",
            "they'll do their best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C10B")

    label("loc_BD71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_BD7F")
    Jump("loc_C10B")

    label("loc_BD7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_BD8D")
    Jump("loc_C10B")

    label("loc_BD8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BD9B")
    Jump("loc_C10B")

    label("loc_BD9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BE32")

    ChrTalk(
        0x14,
        (
            "Even so, it was a scary\x01",
            "accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "It was sudden and I still don't\x01",
            "know what happened... I wonder\x01",
            "what the cause could've been.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C10B")

    label("loc_BE32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BED5")

    ChrTalk(
        0x14,
        (
            "I hurt my hips doing\x01",
            "housework. Really, I\x01",
            "hate getting older.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "You all should be careful\x01",
            "too. Your 30s and 40s are\x01",
            "right around the corner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C10B")

    label("loc_BED5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BEE3")
    Jump("loc_C10B")

    label("loc_BEE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_BF53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEFE")
    Call(0, 24)
    Jump("loc_BF4E")

    label("loc_BEFE")


    ChrTalk(
        0x14,
        (
            "Uhh, my runny nose just\x01",
            "won't stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Stay quiet until your\x01",
            "turn comes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF4E")

    Jump("loc_C10B")

    label("loc_BF53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_BF61")
    Jump("loc_C10B")

    label("loc_BF61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C10B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C059")

    ChrTalk(
        0x14,
        (
            "Lately, medicine\x01",
            "explanations have become\x01",
            "more detailed than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "It's probably so that we\x01",
            "patients can feel at\x01",
            "ease, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Honestly, to an amateur,\x01",
            "those ingredients might as\x01",
            "well be ancient Zemurian.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_C10B")

    label("loc_C059")


    ChrTalk(
        0x14,
        (
            "Lately, medicine\x01",
            "explanations have become\x01",
            "more detailed than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "The contents might as well be\x01",
            "ancient Zemurian, but... Since I\x01",
            "can trust them, I'm sure it's fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C10B")

    TalkEnd(0xFE)
    Return()

    # Function_23_BCCA end

    def Function_24_C10F(): pass

    label("Function_24_C10F")


    ChrTalk(
        0x14,
        (
            "Hmm, you still have a\x01",
            "fever and your runny\x01",
            "nose just won't stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Here, blow your nose in\x01",
            "my handkerchief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#4S...*snort*!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "...So much came out～.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Return()

    # Function_24_C10F end

    def Function_25_C1B7(): pass

    label("Function_25_C1B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C257")

    ChrTalk(
        0x15,
        (
            "At last I came to visit\x01",
            "a hospitalised friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "He's probably feeling lonely,\x01",
            "so I'd like us to chat about\x01",
            "a lot of different things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C425")

    label("loc_C257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_C265")
    Jump("loc_C425")

    label("loc_C265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_C273")
    Jump("loc_C425")

    label("loc_C273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C2E4")

    ChrTalk(
        0x15,
        (
            "My buddy was caught up\x01",
            "in the attack and was\x01",
            "hospitalised...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I hope he gets well\x01",
            "soon...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C425")

    label("loc_C2E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C2F2")
    Jump("loc_C425")

    label("loc_C2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C300")
    Jump("loc_C425")

    label("loc_C300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C39D")

    ChrTalk(
        0x15,
        (
            "The say the initial medical exams\x01",
            "have been postponed. It seems it'll\x01",
            "be some time until my turn comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Ahh, hospitals are\x01",
            "sluggish.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C425")

    label("loc_C39D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C40E")

    ChrTalk(
        0x15,
        (
            "*grgrgrowl", my stomach\x01",
            "hurts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I can only distract\x01",
            "myself thinking about\x01",
            "the nurses...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C425")

    label("loc_C40E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C41C")
    Jump("loc_C425")

    label("loc_C41C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C425")

    label("loc_C425")

    TalkEnd(0xFE)
    Return()

    # Function_25_C1B7 end

    def Function_26_C429(): pass

    label("Function_26_C429")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C4DE")

    ChrTalk(
        0x16,
        (
            "Today I came to pick up\x01",
            "my mother who is leaving\x01",
            "the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "It seems she couldn't leave the\x01",
            "hospital for a while, so I want\x01",
            "to get her back home soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7F2")

    label("loc_C4DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_C4EC")
    Jump("loc_C7F2")

    label("loc_C4EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_C4FA")
    Jump("loc_C7F2")

    label("loc_C4FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C508")
    Jump("loc_C7F2")

    label("loc_C508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C695")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C5C8")

    ChrTalk(
        0x16,
        (
            "I heard the rumors in the city... They\x01",
            "say a mysterious giant monster appeared\x01",
            "at the time of the derailment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Could it have been cause\x01",
            "of the accident...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_C690")

    label("loc_C5C8")


    ChrTalk(
        0x16,
        (
            "I heard the rumors in the city... They\x01",
            "say a mysterious giant monster appeared\x01",
            "at the time of the derailment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "...If something like that\x01",
            "showed up, us ordinary folk\x01",
            "could never deal with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C690")

    Jump("loc_C7F2")

    label("loc_C695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C6A3")
    Jump("loc_C7F2")

    label("loc_C6A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C784")

    ChrTalk(
        0x16,
        (
            "It seems the doctors are\x01",
            "quarreling in front of the\x01",
            "exam room for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "If you look carefully, the people of the\x01",
            "hospital are all depressed too for some\x01",
            "reason... Could something have happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7F2")

    label("loc_C784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C792")
    Jump("loc_C7F2")

    label("loc_C792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C7E9")

    ChrTalk(
        0x16,
        (
            "There there, quiet down,\x01",
            "ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Big sis will be right\x01",
            "behind you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7F2")

    label("loc_C7E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C7F2")

    label("loc_C7F2")

    TalkEnd(0xFE)
    Return()

    # Function_26_C429 end

    def Function_27_C7F6(): pass

    label("Function_27_C7F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C824")

    ChrTalk(
        0x17,
        "I'm tired of waitiiing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C95C")

    label("loc_C824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_C832")
    Jump("loc_C95C")

    label("loc_C832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_C840")
    Jump("loc_C95C")

    label("loc_C840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C88C")

    ChrTalk(
        0x17,
        "Aaah, so boring...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Why hasn't my turn come\x01",
            "already!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C95C")

    label("loc_C88C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C89A")
    Jump("loc_C95C")

    label("loc_C89A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C8A8")
    Jump("loc_C95C")

    label("loc_C8A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C8B6")
    Jump("loc_C95C")

    label("loc_C8B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C8C4")
    Jump("loc_C95C")

    label("loc_C8C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C913")

    ChrTalk(
        0x17,
        (
            "Waaahn, injections are\x01",
            "scaryyy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "I'm going back hooome!\x02",
    )

    CloseMessageWindow()
    Jump("loc_C95C")

    label("loc_C913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C95C")

    ChrTalk(
        0x17,
        (
            "*yawn*... I'm tired of\x01",
            "waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Isn't it my turn yet?\x02",
    )

    CloseMessageWindow()

    label("loc_C95C")

    TalkEnd(0xFE)
    Return()

    # Function_27_C7F6 end

    def Function_28_C960(): pass

    label("Function_28_C960")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C9B2")

    ChrTalk(
        0x18,
        (
            "*cough, cough*... If\x01",
            "it's bitter medicine, I\x01",
            "don't want it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAB5")

    label("loc_C9B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_C9C0")
    Jump("loc_CAB5")

    label("loc_C9C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_C9CE")
    Jump("loc_CAB5")

    label("loc_C9CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C9DC")
    Jump("loc_CAB5")

    label("loc_C9DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C9EA")
    Jump("loc_CAB5")

    label("loc_C9EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CA42")

    ChrTalk(
        0x18,
        (
            "I came alone on the bus\x01",
            "today, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "Ehehe, I'm good, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_CAB5")

    label("loc_CA42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CA50")
    Jump("loc_CAB5")

    label("loc_CA50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_CA9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA6B")
    Call(0, 24)
    Jump("loc_CA99")

    label("loc_CA6B")


    ChrTalk(
        0x18,
        (
            "*sniff*... My nose won't\x01",
            "stop running...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA99")

    Jump("loc_CAB5")

    label("loc_CA9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_CAAC")
    Jump("loc_CAB5")

    label("loc_CAAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_CAB5")

    label("loc_CAB5")

    TalkEnd(0xFE)
    Return()

    # Function_28_C960 end

    def Function_29_CAB9(): pass

    label("Function_29_CAB9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CB41")

    ChrTalk(
        0x19,
        (
            "The city... The city was\x01",
            "ablaze...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "What a scary scene it was...\x01",
            "It made me remember the\x01",
            "battles many decades ago.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB41")

    TalkEnd(0xFE)
    Return()

    # Function_29_CAB9 end

    def Function_30_CB45(): pass

    label("Function_30_CB45")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CB90")

    ChrTalk(
        0x1A,
        "U-Uuuh...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "She seems to be having a\x01",
            "nightmare.\x07\x02\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_CB90")

    TalkEnd(0xFE)
    Return()

    # Function_30_CB45 end

    def Function_31_CB94(): pass

    label("Function_31_CB94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CC05")

    ChrTalk(
        0x1B,
        (
            "Uugh... I broke both my\x01",
            "legs in that attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Damn it... Why'd this\x01",
            "have to happen to me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC05")

    TalkEnd(0xFE)
    Return()

    # Function_31_CB94 end

    def Function_32_CC09(): pass

    label("Function_32_CC09")

    TalkBegin(0xFE)

    ChrTalk(
        0x1C,
        (
            "Then, please contact the\x01",
            "family of that Calvardian\x01",
            "patient over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "I'll deliver their\x01",
            "medical record to\x01",
            "Professor Seiland.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_CC09 end

    def Function_33_CC99(): pass

    label("Function_33_CC99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CCC8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CCC8")
    Call(0, 48)
    Return()

    label("loc_CCC8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CF42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE8E")

    ChrTalk(
        0x1D,
        (
            "I heard a rumor... It seems\x01",
            "Shizuku MacLaine's eyes\x01",
            "were completely healed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I should rejoice as her\x01",
            "former doctor. However, I\x01",
            "have mixed feelings about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Considering this series of incidents, I\x01",
            "can say that some kind of mysterious\x01",
            "power has been used on her eyes as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "As a medical professional,\x01",
            "losing to something like\x01",
            "that is rather frustrating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "...I'm sorry, forget it.\x01",
            "I'm being stubborn.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_CF3D")

    label("loc_CE8E")


    ChrTalk(
        0x1D,
        (
            "...I'm sorry, forget it.\x01",
            "It's the stubbornness of\x01",
            "a medical professional.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "The fact that Shizuku MacLaine's\x01",
            "eyes were healed is delightful.\x01",
            "I honestly wish her well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF3D")

    Jump("loc_D7DF")

    label("loc_CF42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_CF50")
    Jump("loc_D7DF")

    label("loc_CF50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_CF5E")
    Jump("loc_D7DF")

    label("loc_CF5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_CF6C")
    Jump("loc_D7DF")

    label("loc_CF6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D231")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D22C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF98")
    Call(0, 35)
    Jump("loc_D227")

    label("loc_CF98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D0D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D045")

    ChrTalk(
        0x1D,
        (
            "With these we'll be able\x01",
            "to treat the attack\x01",
            "victims for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I'll make sure the medical\x01",
            "supplies you recovered are\x01",
            "put to good use.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_D0CD")

    label("loc_D045")


    ChrTalk(
        0x1D,
        (
            "Well then... It's time\x01",
            "to operate on the next\x01",
            "patient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I'll make sure the medical\x01",
            "supplies you recovered are\x01",
            "put to good use.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0CD")

    Jump("loc_D227")

    label("loc_D0D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_D175")

    ChrTalk(
        0x1D,
        (
            "It really hurts that our\x01",
            "medical supplies were stolen\x01",
            "in this situation, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "We can't whine about it.\x01",
            "We have to think of\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D227")

    label("loc_D175")


    ChrTalk(
        0x1D,
        (
            "...It's difficult to\x01",
            "overcome this situation with\x01",
            "a lack of medical supplies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "If it comes to it, I'll explain\x01",
            "the situation and have them\x01",
            "send us replacement supplies.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D227")

    Jump("loc_D22C")

    label("loc_D22C")

    Jump("loc_D7DF")

    label("loc_D231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D34E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2FF")
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x1D,
        (
            "Lytton, I'm leaving to\x01",
            "do my rounds after this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Due to the accident, there are a\x01",
            "lot of patients. Don't relax just\x01",
            "because the surgeries are over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "R-Right!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x1, 6)
    Jump("loc_D349")

    label("loc_D2FF")


    ChrTalk(
        0x1D,
        (
            "Due to this accident,\x01",
            "there are many patients.\x01",
            "Don't relax too much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D349")

    Jump("loc_D7DF")

    label("loc_D34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D35C")
    Jump("loc_D7DF")

    label("loc_D35C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D36A")
    Jump("loc_D7DF")

    label("loc_D36A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D378")
    Jump("loc_D7DF")

    label("loc_D378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D7D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D557")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4E4")

    ChrTalk(
        0x1D,
        (
            "Albert... It seems he\x01",
            "intends to come here after\x01",
            "his inspection is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "There's not much need to\x01",
            "come here with tomorrow's\x01",
            "conference this close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Oh brother... That man\x01",
            "never changes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(A-Albert she says... Is\x01",
            "she addressing him\x01",
            "informally?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F(Maybe they know each\x01",
            "other or something...?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_D557")

    label("loc_D4E4")


    ChrTalk(
        0x1D,
        (
            "It seems Albert intends\x01",
            "to come here after his\x01",
            "inspection is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Oh brother... That man\x01",
            "never changes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D557")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D7D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6F2")

    ChrTalk(
        0x1D,
        (
            "Since the cause of "Riboten Poisoning"\x01",
            "is a mushroom found out of state, it's\x01",
            "hard for cases to appear in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I thought about many different possibilities\x01",
            "myself, but all I can say is that Albert guessed\x01",
            "right. As expected, his knowledge is significant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I owe him one this time... Even if\x01",
            "it's temporary, he governs Remiferia.\x01",
            "I shouldn't have expected less.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_D7D1")

    label("loc_D6F2")


    ChrTalk(
        0x1D,
        (
            "Albert guessed it right when he said it\x01",
            "was "Riboten Poisoning". As expected,\x01",
            "his knowledge is significant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I owe him one this time... Even if\x01",
            "it's temporary, he governs Remiferia.\x01",
            "I shouldn't have expected less.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7D1")

    Jump("loc_D7DF")

    label("loc_D7D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D7DF")

    label("loc_D7DF")

    TalkEnd(0xFE)
    Return()

    # Function_33_CC99 end

    def Function_34_D7E3(): pass

    label("Function_34_D7E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D8B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D8B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D812")
    Call(0, 35)
    Jump("loc_D8B3")

    label("loc_D812")


    ChrTalk(
        0x1E,
        (
            "We had arranged with "Rhymes Shipping"\x01",
            "to bring us the medical supplies that\x01",
            "arrived at the airport, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Hmm, maybe there was\x01",
            "some kind of mistake?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8B3")

    Jump("loc_D8B8")

    label("loc_D8B8")

    TalkEnd(0xFE)
    Return()

    # Function_34_D7E3 end

    def Function_35_D8BC(): pass

    label("Function_35_D8BC")

    OP_4B(0x1E, 0xFF)
    OP_4B(0x1D, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x1D,
        (
            "...The medical supplies\x01",
            "from Remiferia haven't\x01",
            "arrived?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Yes. The shipment's\x01",
            "scheduled arrival passed a\x01",
            "long time ago, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder if there's been\x01",
            "some kind of trouble...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Hmm, something might've\x01",
            "happened in Remiferia or\x01",
            "at the airport.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1E, 0x10)
    SetScenarioFlags(0x18F, 0)
    OP_4C(0x1E, 0xFF)
    OP_4C(0x1D, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_35_D8BC end

    def Function_36_D9E5(): pass

    label("Function_36_D9E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9FA")
    Call(0, 37)
    Jump("loc_DAA9")

    label("loc_D9FA")


    ChrTalk(
        0x1F,
        (
            "Honestly, thinking about what they might say,\x01",
            "I was reluctant to come to the hospital... Who\x01",
            "could've thought this would be the result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "I owe everything to\x01",
            "Amisaah.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DAA9")

    TalkEnd(0xFE)
    Return()

    # Function_36_D9E5 end

    def Function_37_DAAD(): pass

    label("Function_37_DAAD")

    OP_4B(0x1F, 0xFF)
    OP_4B(0x20, 0xFF)

    ChrTalk(
        0xC,
        (
            "Hm, this is\x01",
            "surprising...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Mr. Quine, your condition\x01",
            "has improved since you\x01",
            "were hospitalised.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1F,
        "I-Is that true!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes, although we need to\x01",
            "observe your progress,\x01",
            "of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "However, at least\x01",
            "there's no need to\x01",
            "hospitalise you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x20,
        (
            "Aren't you happy,\x01",
            "grandpa?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "He says your health has\x01",
            "improved! And he says you\x01",
            "don't have to stay here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Y-Yeah... That's right.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1F, 0x10)
    ClearChrFlags(0x20, 0x10)
    SetScenarioFlags(0x2, 4)
    OP_4C(0x1F, 0xFF)
    OP_4C(0x20, 0xFF)
    Return()

    # Function_37_DAAD end

    def Function_38_DCA5(): pass

    label("Function_38_DCA5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DD39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCC3")
    Call(0, 37)
    Jump("loc_DD34")

    label("loc_DCC3")


    ChrTalk(
        0x20,
        (
            "I'm really, really happy\x01",
            "for you, grandpa!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Hahaha. I was right in\x01",
            "making you take your\x01",
            "medicine, huh♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD34")

    Jump("loc_DD86")

    label("loc_DD39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DD86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD54")
    Call(0, 39)
    Jump("loc_DD86")

    label("loc_DD54")


    ChrTalk(
        0x20,
        (
            "I'll bring your medicine\x01",
            "today too, grampa♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD86")

    TalkEnd(0xFE)
    Return()

    # Function_38_DCA5 end

    def Function_39_DD8A(): pass

    label("Function_39_DD8A")

    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "Alright then, Amisaah.\x01",
            "I've wrapped the usual\x01",
            "medicines for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Be careful and bring\x01",
            "them to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "I will. Thank you as\x01",
            "always, doctor.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x20, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x2, 3)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_39_DD8A end

    def Function_40_DE37(): pass

    label("Function_40_DE37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE66")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE66")
    Call(0, 48)
    Return()

    label("loc_DE66")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_40_DE37 end

    def Function_41_DE6D(): pass

    label("Function_41_DE6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE8C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE8C")
    Call(0, 48)
    Return()

    label("loc_DE8C")

    TalkBegin(0xFE)

    ChrTalk(
        0x22,
        (
            "I will wait for you to bring\x01",
            "the Naderia Mushroom.\x02\x03",
            "I am sure that Arios and you\x01",
            "all can accomplish this.\x01",
            "Please, I leave this to you.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_DE6D end

    def Function_42_DF1F(): pass

    label("Function_42_DF1F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E087")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DFF9")

    ChrTalk(
        0x24,
        (
            "The mushrooms I brought\x01",
            "home as souvenirs from\x01",
            "abroad tasted great, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "To think they were\x01",
            "poisonous. I was\x01",
            "careless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Next time, I'll have to\x01",
            "be a little more\x01",
            "careful...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E082")

    label("loc_DFF9")


    ChrTalk(
        0x24,
        (
            "The mushrooms I brought\x01",
            "home as souvenirs from\x01",
            "abroad tasted great, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Next time, I'll have to\x01",
            "be a little more\x01",
            "careful...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E082")

    Jump("loc_E11A")

    label("loc_E087")


    ChrTalk(
        0x24,
        (
            "U-Uuhg... My stomach\x01",
            "pain has gotten worse\x01",
            "for some reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "As I thought, maybe what\x01",
            "I ate on the airship\x01",
            "wasn't good...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "Ughgh...\x02",
    )

    CloseMessageWindow()

    label("loc_E11A")

    TalkEnd(0xFE)
    Return()

    # Function_42_DF1F end

    def Function_43_E11E(): pass

    label("Function_43_E11E")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_43_E11E end

    def Function_44_E125(): pass

    label("Function_44_E125")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E361")

    ChrTalk(
        0xFE,
        (
            "I'm helping transport the\x01",
            "patients who couldn't come\x01",
            "to the hospital regularly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you probably guessed, there\x01",
            "are a lot, so I'll have make\x01",
            "many trips throughout the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FThat seems pretty\x01",
            "tough...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FPlease, don't overdo it.\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Aaahn, to hear such\x01",
            "words from Tio is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Her reactions are always cool, and yet...\x01",
            "Could she be one of those characters who are\x01",
            "always calm and composed... A "kuudere"?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00211F(...She's starting to\x01",
            "sound like Chief\x01",
            "Roberts.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BB, 2)
    Jump("loc_E46E")

    label("loc_E361")


    ChrTalk(
        0xFE,
        (
            "Aaaalright... Since I Tio cheered me\x01",
            "up, my energy has jumped a hundred\x01",
            "fold, and I'm full of courage!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tio, let me give you a\x01",
            "tight big hug when all\x01",
            "of this is over, ok?㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F(...It looks like I won't\x01",
            "be able to relax even when\x01",
            "all of this is over.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E46E")

    TalkEnd(0xFE)
    Return()

    # Function_44_E125 end

    def Function_45_E472(): pass

    label("Function_45_E472")

    Sound(160, 0, 100, 0)
    Return()

    # Function_45_E472 end

    def Function_46_E479(): pass

    label("Function_46_E479")

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
            "#11POh, Noｱl. And the\x01",
            "Support Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAre you here to see\x01",
            "Fran?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#6PYes. Is now a good time?\x02",
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
            "#11P...Still, I'm glad your\x01",
            "sister has regained\x01",
            "consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#6P...Yes. Thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E63E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_E63E)
    WaitChrThread(0x109, 3)
    Sleep(150)

    ChrTalk(
        0x109,
        (
            "#10102F#11PLet's go. It's room no.\x01",
            "301 on 3F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PYeah, excuse us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#6PExcuse us, Sera.\x02",
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

    # Function_46_E479 end

    def Function_47_E715(): pass

    label("Function_47_E715")

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
        (
            "...Yes...yes, that's\x01",
            "right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...Then, please do.\x02",
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
            "I confirmed it with\x01",
            "Professor Seiland.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She said to come to her\x01",
            "room in the research\x01",
            "building immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        "#01309FThanks, Sera.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FThat really helps us\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x101, 500)

    ChrTalk(
        0x26,
        (
            "#01300F...See you later, everyone.\x01",
            "My break is almost over, so\x01",
            "I'll leave you here.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E9E2():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E9E2)
    Sleep(50)

    def lambda_E9F2():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E9F2)
    Sleep(50)

    def lambda_EA02():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_EA02)
    Sleep(50)

    def lambda_EA12():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_EA12)
    Sleep(50)

    def lambda_EA22():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_EA22)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah, thanks for\x01",
            "everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10102FThanks for helping us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#01300FOh, you're very welcome.\x02\x03",
            "#01309FI think you'll face many\x01",
            "hardships from now on,\x01",
            "but... Do your best, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00009FYeah, you too.\x02",
    )

    CloseMessageWindow()

    def lambda_EB1E():
        OP_95(0xFE, 12030, 0, 10760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_EB1E)
    Sleep(50)

    def lambda_EB3B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_EB3B)
    Sleep(50)

    def lambda_EB4B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EB4B)
    WaitChrThread(0x26, 1)

    def lambda_EB5C():
        OP_97(0xFE, 0x0, 0x564, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_EB5C)
    Sleep(1000)

    def lambda_EB79():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_EB79)
    WaitChrThread(0x26, 2)
    SetChrFlags(0x26, 0x80)
    OP_0D()
    OP_68(13870, 1000, 6330, 3000)
    OP_6F(0x1)

    ChrTalk(
        0x104,
        (
            "#12P#00310F......Gah, well aren't\x01",
            "you always such the\x01",
            "darling!\x02\x03",
            "#00309FDo your best, Lloyd㈱\x01",
            "...She really said that!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006FI don't think she\x01",
            "attached any heart mark,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EC6D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_EC6D)
    Sleep(100)

    def lambda_EC7D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EC7D)
    Sleep(500)

    ChrTalk(
        0x105,
        (
            "#6P#10300FHehe. You say that, but aren't you\x01",
            "a little disappointed? Hm?\x02\x03",
            "Looks like I'm not going to get to\x01",
            "see one of those rumored\x01",
            "passionate hugs this time, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FYes, now that you\x01",
            "mention it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FHuh? She did such a\x01",
            "thing!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAh, enough already!\x01",
            "We're going to the\x01",
            "professor's lab!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x3E8)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00001FThe research building is on the\x01",
            "roof, and the pharmacology lab is\x01",
            "on the 4th floor. We're going!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309F(Oh man. Forcefully\x01",
            "dodging the question,\x01",
            "huh?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302F(Hehe. That's why he's\x01",
            "so fun to tease.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00003FI can hear you!\x02",
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

    # Function_47_E715 end

    def Function_48_EF38(): pass

    label("Function_48_EF38")

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
        (
            "Hmm? It seems we have\x01",
            "guests.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F8A7")

    ChrTalk(
        0x22,
        "Oh, you all are...\x02",
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
            "#00005FArchduke Albert from the\x01",
            "Principality of\x01",
            "Remiferia!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FAnd Arios too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#01405FHmm, what a coincidence.\x02\x03",
            "#01400FYour Excellency, they are the\x01",
            ""Special Support Section" I\x01",
            "told you about previously.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x22, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x22,
        (
            "Oh, so that's who they\x01",
            "are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "...How do you do, ladies\x01",
            "and gentlemen of the\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "I am Albert von\x01",
            "Bartholomeus. I serve as\x01",
            "Remiferia's Head of State.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Please do your very best\x01",
            "for Crossbell from now\x01",
            "on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FP-Pleased to make your\x01",
            "acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "I heard about you all\x01",
            "from Arios. I really\x01",
            "wanted to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Also, Elie, it's been a\x01",
            "long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, it has. You\x01",
            "look well, Your Grace...\x02\x03",
            "#00103FHowever, I didn't know\x01",
            "you were visiting the\x01",
            "hospital.\x02\x03",
            "#00105FAre you here for an\x01",
            "inspection today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Yes. The Principality of\x01",
            "Remiferia is one of this\x01",
            "hospital's sponsors, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Also, I wanted to see\x01",
            "Dr. Seiland who has been\x01",
            "appointed here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x22, 500)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "#01403FRegarding that, the Archduke\x01",
            "asked me to escort him\x01",
            "personally a while longer.\x02\x03",
            "#01400FI wonder if it's alright\x01",
            "with just the driver and I,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Haha. It's because I\x01",
            "have such confidence in\x01",
            "you, Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "And, I can't exactly go disturbing\x01",
            "hospital operations with a swarm\x01",
            "of escorts, now can I?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1D, 0x0)
    Sleep(300)

    ChrTalk(
        0x1D,
        (
            "Honestly, why do you go\x01",
            "to such trouble?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "It's not like you had to\x01",
            "come for an inspection\x01",
            "now either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "It would have been fine\x01",
            "if you just focused on\x01",
            "the trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "As a state guest,\x01",
            "shouldn't you be a little\x01",
            "more conscientious?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "Ha ha ha, harsh as\x01",
            "always, eh, Seiland?\x02",
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
            "#00003F(Archduke Albert... He\x01",
            "knows a lot of people,\x01",
            "doesn't he.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F(Yes. Elie, Arios... and it\x01",
            "looks like he's known Professor\x01",
            "Seiland for a long time.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Hehe. Even for a head of\x01",
            "state, he has an interesting\x01",
            "way of talking.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC8C")

    label("loc_F8A7")


    ChrTalk(
        0x22,
        (
            "Oh, you're the Special\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYour Excellency,\x01",
            "Archduke Albert. And\x01",
            "Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FSo you came here after\x01",
            "visiting with Shizuku.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#01400FYes, I was just saying\x01",
            "hello to Professor\x01",
            "Seiland.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Haha. I wanted to see\x01",
            "Dr. Seiland who has been\x01",
            "appointed here.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1D, 0x0)
    Sleep(300)

    ChrTalk(
        0x1D,
        (
            "Honestly, why do you go\x01",
            "to such trouble?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "It's not like you had to\x01",
            "come for an inspection\x01",
            "now either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "It would have been fine\x01",
            "if you just focused on\x01",
            "the trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "As a state guest,\x01",
            "shouldn't you be a little\x01",
            "more conscientious?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "Ha ha ha, harsh as\x01",
            "always, eh, Seiland?\x02",
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
            "#00003F(Archduke Albert... He\x01",
            "knows a lot of people,\x01",
            "doesn't he.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F(Yes. Elie, Arios... And it\x01",
            "looks like he's known Professor\x01",
            "Seiland for a long time.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Hehe. Even for a head of\x01",
            "state, he has an interesting\x01",
            "way of talking.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FC8C")

    OP_82(0xC8, 0x0, 0xBB8, 0x320)
    SetMessageWindowPos(300, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5SD-Doctor!\x07\x00\x02",
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

    def lambda_FD91():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FD91)
    Sleep(50)

    def lambda_FDA1():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FDA1)
    Sleep(50)

    def lambda_FDB1():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FDB1)
    Sleep(50)

    def lambda_FDC1():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_FDC1)
    Sleep(50)

    def lambda_FDD1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FDD1)
    Sleep(50)

    def lambda_FDE1():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_FDE1)
    Sleep(50)

    def lambda_FDF1():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_FDF1)
    OP_95(0xC, 53440, 0, 52820, 4000, 0x0)
    OP_95(0xC, 54100, 0, 55910, 4000, 0x0)
    OP_93(0xC, 0x13B, 0x0)
    OP_6F(0x1)

    ChrTalk(
        0x1D,
        (
            "What's the problem,\x01",
            "Lytton?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0xC,
        "I-It's an emergency!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "A patient in the lobby\x01",
            "just collapsed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's serious. He's lost\x01",
            "consciousness!\x02",
        )
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
        "Hmm, that's not good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Bring him here now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Y-Yes ma'am!\x02",
    )

    CloseMessageWindow()
    OP_64(0xC)
    OP_68(50330, 1000, 58210, 3000)
    OP_95(0xC, 53440, 0, 52820, 4000, 0x0)
    OP_95(0xC, 49800, 0, 51590, 4000, 0x0)
    OP_95(0xC, 49560, 0, 49150, 4000, 0x0)
    OP_6F(0x1)
    SetChrSubChip(0x1D, 0x1)

    def lambda_10052():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10052)
    Sleep(50)

    def lambda_10062():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10062)
    Sleep(50)

    def lambda_10072():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10072)
    Sleep(50)

    def lambda_10082():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10082)
    Sleep(50)

    def lambda_10092():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10092)
    Sleep(50)

    def lambda_100A2():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_100A2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000FArios, I think we\x01",
            "should...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#01400FRight. We'll be in the\x01",
            "way for the exam. We\x01",
            "should leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "No, stay here.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1D, 0x0)
    TurnDirection(0x21, 0x22, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "It's possible you may be\x01",
            "of help.\x02",
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
        "...Uh...gh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "...Hm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHow is he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FLooks like he's\x01",
            "sufferin' a lot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "...The news isn't good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I tried various tests. While it's\x01",
            "certainly an internal medicine\x01",
            "case, I couldn't detect the cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "If I knew what he had I\x01",
            "could prepare medicine\x01",
            "for it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "It's hard to say if the\x01",
            "patient will hold out\x01",
            "that long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FI-Is it that serious...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "W-What should we do!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "─Hmm. May I have a\x01",
            "moment?\x02",
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

    def lambda_10500():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10500)
    Sleep(50)

    def lambda_10510():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10510)
    Sleep(50)

    def lambda_10520():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10520)
    Sleep(50)

    def lambda_10530():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10530)
    Sleep(50)

    def lambda_10540():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10540)
    Sleep(50)

    def lambda_10550():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_10550)
    Sleep(50)

    def lambda_10560():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_10560)
    Sleep(50)

    def lambda_10570():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_10570)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "#01405FYour Excellency, is\x01",
            "something wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "I've thought this from\x01",
            "the start, Dr. Seiland,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Could this disease be\x01",
            ""Riboten Poisoning"?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1D,
        (
            "...I see, Riboten\x01",
            "Poisoning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Though there have been\x01",
            "no cases in Crossbell,\x01",
            "that does seem likely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FRiboten Poisoning?\x01",
            "That's a name I've not\x01",
            "heard.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "It's caused by a rare poisonous\x01",
            "mushroom that grows in remote\x01",
            "regions on the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Its poison is difficult\x01",
            "to detect with normal\x01",
            "methods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "I was just thinking,\x01",
            "isn't this case just\x01",
            "like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Yes, there's no doubt\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Perhaps he ingested\x01",
            "something he brought with\x01",
            "him from out of state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FSigned, sealed and\x01",
            "delivered, huh.\x02\x03",
            "#00300FYou're amazin', Mr.\x01",
            "Archduke. You saw\x01",
            "through it immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Haha. It's nothing much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Still, we can't relax\x01",
            "just yet.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "Seiland, do you have the\x01",
            "medicine for Riboten\x01",
            "Poisoning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "...I just ran out of\x01",
            "some of the ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "If I had them, I could\x01",
            "prepare it immediately,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FThat doesn't sound\x01",
            "good...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Hmm... In that case.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "Arios. And ladies and\x01",
            "gentlemen of the Special\x01",
            "Support Section as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "I want all of you to gather the\x01",
            "medicine's ingredients. This is\x01",
            "urgent. Will you accept?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#01400FSir... As you wish.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FSeeing as how it's an\x01",
            "emergency, of course we\x01",
            "accept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FThen, what should we be\x01",
            "getting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Yes, I'll explain the\x01",
            "plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "The medicine for Riboten\x01",
            "Poisoning has two main\x01",
            "ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "One of them is "Ante Grass",\x01",
            "a medical herb that grows in\x01",
            "the mountains near Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "The other is the "Almashroom"\x01",
            "that grows in the forests of\x01",
            "St. Ursula Byroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FAnte Grass and Almashroom...\x01",
            "I feel like I saw them during\x01",
            "CGF survival training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Of these, I want Arios\x01",
            "to retrieve the Ante\x01",
            "Grass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "As a bracer, you are qualified to\x01",
            "search for a medical herb in a\x01",
            "mountainous area untouched by man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#01400FYes, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Then, as for the\x01",
            "Almashroom...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Although I will be handling it\x01",
            "personally, I would like the Special\x01",
            "Support Section to accompany me.\x02",
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
        "#00005FWhat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FWith Your Excellency?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Yes. This is because...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "In places Almashroom grows,\x01",
            "other mushrooms with a\x01",
            "similar shape grow as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "It's hard to tell them\x01",
            "apart, so it's best if you\x01",
            "have an expert with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHmm. That does seem like a\x01",
            "good idea.\x02\x03",
            "#10300FIf you're not worried about\x01",
            "us taking over Arios'\x01",
            "escort duty, that is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FIndeed. This is a heavy\x01",
            "responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#01401FAlthough I too worry about\x01",
            "you taking on His\x01",
            "Excellency's escort duty...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Prioritizing treatment of this\x01",
            "patient as quickly as possible,\x01",
            "there is likely no other way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "And, you recognize the\x01",
            "skills of the Support\x01",
            "Section too, do you not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "I will be plenty careful\x01",
            "myself, so there's no\x01",
            "need to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Also, if you hurry back,\x01",
            "there won't be a\x01",
            "problem, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#01404FHmph... Understood.\x02\x03",
            "#01400FThen, I'll head for the\x01",
            "mountains of Mainz.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "#01400FI'm counting on you to\x01",
            "escort His Excellency,\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWe'll be sure to keep\x01",
            "him safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Haha. In that case, let's\x01",
            "head for the forest of St.\x01",
            "Ursula Byroad ourselves.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "Seiland, Lytton. Continue to\x01",
            "monitor the patient and get\x01",
            "ready to prepare the medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "Yes, all right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "Special Support Section,\x01",
            "please do your best!\x02",
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
            "And so, Lloyd and the\x01",
            "others accepted Archduke\x01",
            "Albert's urgent request...\x07\x00\x02",
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
            "They split into two groups\x01",
            "and headed out to gather\x01",
            "the medicine's ingredients.\x07\x00\x02",
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
            "Quest [Antidote\x01",
            "Ingredients Supply]\x07\x00\x01",
            "started!\x02",
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

    # Function_48_EF38 end

    def Function_49_114CD(): pass

    label("Function_49_114CD")

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
            "#1PThe mushrooms I brought\x01",
            "home as souvenirs from\x01",
            "abroad tasted great, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#1P*sigh*, to think they\x01",
            "were poisonous. I was\x01",
            "careless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Although they are delicious, the fact\x01",
            "that they cause Riboten Poisoning is\x01",
            "one of their dangerous properties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Take care not to eat\x01",
            "such things so easily in\x01",
            "the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Also, although your life is not in\x01",
            "danger, I intend to keep a close eye on\x01",
            "you in the research building for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#1PI-I understand. It would\x01",
            "really be scary if there\x01",
            "were after-effects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#1PStill, I'm feeling much\x01",
            "better thanks to you. Thank\x01",
            "you very much, doctors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you want to thank someone,\x01",
            "make it Archduke Albert, Arios\x01",
            "and the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "After all, it was they who\x01",
            "collected the ingredients\x01",
            "for your medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#1PI-I see. Thank you very\x01",
            "much, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#1PTo think I was saved by\x01",
            "Your Excellency, Archduke\x01",
            "Albert... How awesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "No, no. In the end, I\x01",
            "only identified a\x01",
            "mushroom.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11A01():
        TurnDirection(0x22, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11A01)

    ChrTalk(
        0x22,
        (
            "Credit naturally belongs with Arios\x01",
            "and the ladies and gentlemen of the\x01",
            "Support Section in this case.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0x0)

    def lambda_11A7D():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_11A7D)
    Sleep(50)

    def lambda_11A8D():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11A8D)

    def lambda_11A9A():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_11A9A)
    Sleep(50)

    def lambda_11AAA():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11AAA)

    def lambda_11AB7():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_11AB7)
    Sleep(50)

    def lambda_11AC7():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11AC7)
    Sleep(50)

    def lambda_11AD7():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11AD7)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "#01402FYou're too modest...\x02\x03",
            "#01403FI heard Your Excellency studied\x01",
            "with Professor Seiland and you\x01",
            "have a physician's license.\x02\x03",
            "#01400FThey say your experience and\x01",
            "skills are on par with combat\x01",
            "medics on the front lines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FWow... So that's how it\x01",
            "is, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FShould I say I expected as much\x01",
            "from the Archduke of Remiferia,\x01",
            "known for its advanced medicine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Haha. Even so, I study\x01",
            "hard, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "When she was in Remiferia,\x01",
            "Seiland often allowed me\x01",
            "to observe her surgeries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "The knowlege I acquired then just happened\x01",
            "to be of use... Frankly, it's embarrassing\x01",
            "that you all would say that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "I did nothing more than\x01",
            "butt in in this case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Cooperation between Arios, the ladies and\x01",
            "gentlemen of the Support Section and the\x01",
            "hospital staff lead to a prompt treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Yes, this was a\x01",
            "worthwhile inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Oh brother... Always the\x01",
            "argumentative one,\x01",
            "aren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Anyway, I suppose this\x01",
            "wraps up your\x01",
            "inspection?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Shouldn't you be\x01",
            "preparing for tomorrow's\x01",
            "trade conference?\x02",
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
            "Hah hah hah, you really\x01",
            "are harsh. However, what\x01",
            "you say is always logical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Then, we'll excuse\x01",
            "ourselves here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Arios, can I count on\x01",
            "you for an escort on our\x01",
            "way back?\x02",
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
            "#01400F...Well then, Special\x01",
            "Support Section.\x02\x03",
            "#01403FDon't let your guard\x01",
            "down until tomorrow's\x01",
            "trade conference.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0x1)

    ChrTalk(
        0x101,
        (
            "#00000FAh... Yes sir. We'll\x01",
            "keep that in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FThank you very much!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Ladies and gentlemen,\x01",
            "stay focused on your work\x01",
            "even more from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "I'll be rooting for you\x01",
            "from behind the scenes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, thank you very\x01",
            "much.\x02",
        )
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
            "Quest [Antidote\x01",
            "Ingredients Supply]\x07\x00\x01",
            "completed!\x02",
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

    # Function_49_114CD end

    def Function_50_12308(): pass

    label("Function_50_12308")

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
            "The Special Support\x01",
            "Section... Welcome to\x01",
            "St. Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What business do you\x01",
            "have with us today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUhhm, we came because we\x01",
            "wanted to ask you\x01",
            "something...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd asked about the\x01",
            "misdelivered package.\x07\x02\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Ah... So that's what\x01",
            "that package was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thinking a nurse made an\x01",
            "ordering mistake, Head Nurse\x01",
            "Martha made a fuss about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FAn order mistake?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes. I'm told similar\x01",
            "things have happened\x01",
            "many times before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FAnd, is the package at\x01",
            "the nurse's station now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yes, it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For now, please try\x01",
            "going to 2F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FThen, that's just what\x01",
            "we'll do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FI feel sorry for the nurse\x01",
            "that got scolded on a\x01",
            "false accusation, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FY-Yeah... Let's get\x01",
            "going already.\x02",
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

    # Function_50_12308 end

    def Function_51_12725(): pass

    label("Function_51_12725")

    Return()

    # Function_51_12725 end

    def Function_52_12726(): pass

    label("Function_52_12726")

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
            "When I got the call from\x01",
            "Ricardo at the airport,\x01",
            "I was shocked...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I never expected to hear\x01",
            "that he couldn't deliver\x01",
            "the medical supplies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "There are some real\x01",
            "nasty guys out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, I'm really glad\x01",
            "the medical goods were\x01",
            "delivered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "With these we'll be able\x01",
            "to treat the attack\x01",
            "victims for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "You've been a big help.\x01",
            "Let me thank you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FNo, we just did what we\x01",
            "had to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FThere's no way we could\x01",
            "forgive some cowardly\x01",
            "opportunist, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FWell, that armored lady\x01",
            "helped us out, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        ""Armored lady"... What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FU-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...It's between us.\x01",
            "Please don't worry about\x01",
            "it too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThen, please let us know\x01",
            "if you ever need our\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We will... Really, thank\x01",
            "you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Let me thank you too.\x01",
            "Thanks, really!\x02",
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
            "Quest [Medical Supplies\x01",
            "Investigation]\x07\x00\x01",
            "completed!\x02",
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

    # Function_52_12726 end

    def Function_53_12CAF(): pass

    label("Function_53_12CAF")

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
            "When I got the call from\x01",
            "Ricardo at the airport,\x01",
            "I was shocked...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I never expected to hear\x01",
            "that he couldn't deliver\x01",
            "the medical supplies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "There are some real\x01",
            "nasty guys out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWe're sorry we couldn't\x01",
            "accomplish your request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FWe did everything we\x01",
            "could to catch him,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Me too. If only I had gone to\x01",
            "get the package sooner, this\x01",
            "would never have happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No, none of you are at\x01",
            "fault. Please, don't be\x01",
            "too hard on yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyhow, we'll try to\x01",
            "deal with this on our\x01",
            "end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Nothing more can be done\x01",
            "about the stolen goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I have to hurry and\x01",
            "arrange for additional\x01",
            "supplies to be sent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Until they arrive, we'll\x01",
            "have no choice but to\x01",
            "improvise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWe're sorry... And thank\x01",
            "you for taking care of\x01",
            "the rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "(*sigh*, I guess my old\x01",
            "man is going to sock me\x01",
            "a good one...)\x02",
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
            "Quest [Medical Supplies\x01",
            "Investigation]\x07\x00",
            " failed...\x02",
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

    # Function_53_12CAF end

    def Function_54_1323A(): pass

    label("Function_54_1323A")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            " ICU (Intensive Care Unit)\x01",
            "Authorized Personnel Only\x01",
            "※Those entering, please perform a level\x01",
            "  2 or higher sterilization treatment.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_54_1323A end

    def Function_55_132FA(): pass

    label("Function_55_132FA")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's go to the reception\x01",
            "desk first. We'll visit\x01",
            "her room later.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 59460, 0, 3330, 225)
    EventEnd(0x4)
    Return()

    # Function_55_132FA end

    def Function_56_1335F(): pass

    label("Function_56_1335F")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's go to the reception\x01",
            "desk first. We'll visit\x01",
            "her room later.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11970, 0, 10190, 135)
    EventEnd(0x4)
    Return()

    # Function_56_1335F end

    def Function_57_133C4(): pass

    label("Function_57_133C4")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FFran's room is no. 301,\x01",
            "right? Let's go see how\x01",
            "she's doing.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 1120, 50, -440, 89)
    EventEnd(0x4)
    Return()

    # Function_57_133C4 end

    SaveToFile()

Try(main)
