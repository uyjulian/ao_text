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
        "Function_8_2D0F",         # 08, 8
        "Function_9_2D13",         # 09, 9
        "Function_10_459F",        # 0A, 10
        "Function_11_54C4",        # 0B, 11
        "Function_12_65EB",        # 0C, 12
        "Function_13_6DE3",        # 0D, 13
        "Function_14_781C",        # 0E, 14
        "Function_15_8459",        # 0F, 15
        "Function_16_90BE",        # 10, 16
        "Function_17_91E7",        # 11, 17
        "Function_18_A2D3",        # 12, 18
        "Function_19_A486",        # 13, 19
        "Function_20_B59E",        # 14, 20
        "Function_21_BA08",        # 15, 21
        "Function_22_BDE0",        # 16, 22
        "Function_23_C2DB",        # 17, 23
        "Function_24_C730",        # 18, 24
        "Function_25_C7DD",        # 19, 25
        "Function_26_CA64",        # 1A, 26
        "Function_27_CE50",        # 1B, 27
        "Function_28_CFB7",        # 1C, 28
        "Function_29_D11C",        # 1D, 29
        "Function_30_D1B2",        # 1E, 30
        "Function_31_D201",        # 1F, 31
        "Function_32_D277",        # 20, 32
        "Function_33_D308",        # 21, 33
        "Function_34_DEC6",        # 22, 34
        "Function_35_DFA2",        # 23, 35
        "Function_36_E0C9",        # 24, 36
        "Function_37_E18A",        # 25, 37
        "Function_38_E39E",        # 26, 38
        "Function_39_E48F",        # 27, 39
        "Function_40_E530",        # 28, 40
        "Function_41_E566",        # 29, 41
        "Function_42_E618",        # 2A, 42
        "Function_43_E82C",        # 2B, 43
        "Function_44_E833",        # 2C, 44
        "Function_45_EB98",        # 2D, 45
        "Function_46_EB9F",        # 2E, 46
        "Function_47_EE74",        # 2F, 47
        "Function_48_F6A1",        # 30, 48
        "Function_49_11D91",       # 31, 49
        "Function_50_12C3A",       # 32, 50
        "Function_51_13059",       # 33, 51
        "Function_52_1305A",       # 34, 52
        "Function_53_135F8",       # 35, 53
        "Function_54_13B85",       # 36, 54
        "Function_55_13C46",       # 37, 55
        "Function_56_13CA6",       # 38, 56
        "Function_57_13D06",       # 39, 57
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_166B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1598")

    ChrTalk(
        0x8,
        (
            "We were even finally able to \x01",
            "accept outpatients again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though we're going to be busy\x01",
            "for awhile, I'm relieved...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This too is thanks to all your help.\x01",
            "Please accept my sincere thanks.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1666")

    label("loc_1598")


    ChrTalk(
        0x8,
        (
            "We were even finally able to \x01",
            "accept outpatients again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though we're going to be busy for awhile, as a\x01",
            "hospital employee, I'll be sure to be kind,\x01",
            "careful and thorough when dealing with patients.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1666")

    Jump("loc_2D0B")

    label("loc_166B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1834")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_177F")

    ChrTalk(
        0x8,
        (
            "According to rumor, it seems that accepting\x01",
            "the declaration of invalidity has caused \x01",
            "something like a riot in a part of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They say the State Guard quickly suppressed it, but...\x01",
            "I'm worried that there may have been injured people.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_182F")

    label("loc_177F")


    ChrTalk(
        0x8,
        (
            "It seems that accepting the\x01",
            "declaration of invalidity has caused \x01",
            "something like a riot in a part of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I'm worried that there may have been injured people...\x02",
    )

    CloseMessageWindow()

    label("loc_182F")

    Jump("loc_2D0B")

    label("loc_1834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_19EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1940")

    ChrTalk(
        0x8,
        (
            "We discussed with the State Guard to be prudent\x01",
            "with the prescribed medicines for the patients\x01",
            "who were commuting to the hospital before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But there're too few...\x01",
            "They can't arrange for all of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...It's beyond our control.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19E7")

    label("loc_1940")


    ChrTalk(
        0x8,
        (
            "Since reception of outpatients has been\x01",
            "stopped, I'd like at least to send medicines\x01",
            "to the patients within the city, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...It's beyond our control.\x02",
    )

    CloseMessageWindow()

    label("loc_19E7")

    Jump("loc_2D0B")

    label("loc_19EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1C73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B8B")

    ChrTalk(
        0x8,
        (
            "Because of the "Cryptids" outbreak effect,\x01",
            "we have stopped accepting outpatients at the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At present, only seriously ill or injured patients\x01",
            "are brought to the hospital by ambulances\x01",
            "escorted by the State Guard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Such a system goes against the long-\x01",
            "established St. Ursula Hospital's intent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Similarly, I'm very worried\x01",
            "about the patients within the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C6E")

    label("loc_1B8B")


    ChrTalk(
        0x8,
        (
            "Because of the "Cryptids" outbreak effect,\x01",
            "we have stopped accepting outpatients at the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To think we're only able to treat the\x01",
            "seriously ill or injured patients...\x01",
            "I'm worried about the patients in the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C6E")

    Jump("loc_2D0B")

    label("loc_1C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_21BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_207B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1E12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D76")

    ChrTalk(
        0x8,
        (
            "Thank goodness those\x01",
            "medical supplies arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though it may be presumptuous of me, allow me \x01",
            "to thank you as a representative of the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, please accept\x01",
            "our sincere thanks.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E0D")

    label("loc_1D76")


    ChrTalk(
        0x8,
        (
            "Though it may be presumptuous of me, allow me \x01",
            "to thank you as a representative of the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, please accept\x01",
            "our sincere thanks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E0D")

    Jump("loc_2076")

    label("loc_1E12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1EDA")

    ChrTalk(
        0x8,
        (
            "We explained our situation to Remiferia,\x01",
            "and they're once again arranging a \x01",
            "delivery of medical supplies for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though it may be a little too late...\x01",
            "What's done is done.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2076")

    label("loc_1EDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FDB")

    ChrTalk(
        0x8,
        (
            "Just now, Mr. Tony, the guard,\x01",
            "reported something to the manager.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The two of them as well as Professor Seiland\x01",
            "seem to be discussing something in front of\x01",
            "the examination room right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I wonder what might have happened.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2076")

    label("loc_1FDB")


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
        "I wonder what might have happened.\x02",
    )

    CloseMessageWindow()

    label("loc_2076")

    Jump("loc_21B8")

    label("loc_207B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2141")

    ChrTalk(
        0x8,
        (
            "Miss Fran's room is number\x01",
            "301 on the 3rd floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She is in stable condition,\x01",
            "but it seems her strength \x01",
            "hasn't yet returned...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please, try to cheer\x01",
            "her up a little.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21B8")

    label("loc_2141")


    ChrTalk(
        0x8,
        (
            "Miss Fran regained consciousness\x01",
            "just the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Her wounds were extremely serious...\x01",
            "I'm very relieved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21B8")

    Jump("loc_2D0B")

    label("loc_21BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2431")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2358")

    ChrTalk(
        0x8,
        (
            "Due to yesterday's train accident,\x01",
            "a great number of patients, foreigners\x01",
            "included, were brought here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since St. Ursula Hospital is always ready \x01",
            "to accept foreigners, we could deal with\x01",
            "them smoothly, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If the accident occurred in a foreign\x01",
            "country without advanced medical care,\x01",
            "I wonder what would have happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "When I think about it, I end up shivering.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_242C")

    label("loc_2358")


    ChrTalk(
        0x8,
        (
            "If the accident occurred in a foreign\x01",
            "country without advanced medical\x01",
            "care, I wonder what would have happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Nearly all patients had only minor\x01",
            "injuries. In a certain sense,\x01",
            "maybe they were lucky.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_242C")

    Jump("loc_2D0B")

    label("loc_2431")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2674")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_252C")

    ChrTalk(
        0x8,
        "That package was a misdelivery, wasn't it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thinking that it was a mis-order\x01",
            "by one of the nurses, Head Nurse\x01",
            "Martha made a fuss at her, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, for now,\x01",
            "please visit the 2nd floor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25AB")

    label("loc_252C")


    ChrTalk(
        0x8,
        (
            "It seems you were able\x01",
            "to get the package safely.\x01",
            "Uh uh, good for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, please be careful\x01",
            "on your way home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25AB")

    Jump("loc_266F")

    label("loc_25B0")


    ChrTalk(
        0x8,
        (
            "Welcome to St. Ursula Hospital.\x01",
            "This is the outpatient and visitation desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since we also accept appointments for\x01",
            "follow-up exams via orbal net,\x01",
            "please feel free to make use of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_266F")

    Jump("loc_2D0B")

    label("loc_2674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_279B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_273A")

    ChrTalk(
        0x8,
        (
            "...This isn't good.\x01",
            "Somehow a depressed mood\x01",
            "is spreading to all the staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There were great hopes for\x01",
            "Shizuku's surgery...\x01",
            "I suppose it can't be helped, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2796")

    label("loc_273A")


    ChrTalk(
        0x8,
        (
            "...We staff can't\x01",
            "be like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We must get out of this\x01",
            "depressed mood somehow...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2796")

    Jump("loc_2D0B")

    label("loc_279B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2929")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_289D")

    ChrTalk(
        0x8,
        (
            "It seems that Mihail's discharge\x01",
            "is scheduled for next week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He has had a long hospital stay,\x01",
            "so I will miss him, but...\x01",
            "I'm really happy for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone wants to say goodbye\x01",
            "to him on the day he'll be discharged.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2924")

    label("loc_289D")


    ChrTalk(
        0x8,
        (
            "I'm really happy that Mihail's\x01",
            "discharge was scheduled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone wants to say goodbye\x01",
            "to him on the day he'll be discharged.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2924")

    Jump("loc_2D0B")

    label("loc_2929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2B4E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2A02")

    ChrTalk(
        0x8,
        (
            "His Grace Archduke Albert seems\x01",
            "to have headed back to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Uh uh, you all did good work as well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Allow us to look after the patient and\x01",
            "treat him until he is discharged.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B49")

    label("loc_2A02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A9C")

    ChrTalk(
        0x8,
        (
            "His Grace, Archduke Albert\x01",
            "was with Mr. Arios just now.\x02",
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
    Jump("loc_2B49")

    label("loc_2A9C")


    ChrTalk(
        0x8,
        (
            "His Grace Archduke Albert went\x01",
            "with Mr. Arios to the internal\x01",
            "medicine examination room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since his inspection is finished, it\x01",
            "seems they are having a little chat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B49")

    Jump("loc_2D0B")

    label("loc_2B4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2D0B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2BE5")

    ChrTalk(
        0x8,
        (
            "Good work collecting those\x01",
            "medical surveys, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please come whenever\x01",
            "you want when you need\x01",
            "something again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D0B")

    label("loc_2BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C8F")

    ChrTalk(
        0x8,
        (
            "Professor Seiland is in the \x01",
            "pharmacology and neurology lab.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The research building is on the roof.\x01",
            "From there, please head to the 4th floor.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2D0B")

    label("loc_2C8F")


    ChrTalk(
        0x8,
        (
            "Professor Seiland\x01",
            "is in the lab.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The pharmacology and neurology lab is\x01",
            "on the 4th floor of the research building.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D0B")

    TalkEnd(0x8)
    Return()

    # Function_7_1478 end

    def Function_8_2D0F(): pass

    label("Function_8_2D0F")

    Call(0, 9)
    Return()

    # Function_8_2D0F end

    def Function_9_2D13(): pass

    label("Function_9_2D13")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2F01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E13")

    ChrTalk(
        0x9,
        (
            "I can't see a situation with limited\x01",
            "medical supplies as positive, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Just by having restarted accepting\x01",
            "outpatients, their chances of\x01",
            "survival have greatly improved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even us as staff must\x01",
            "do our very best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2EFC")

    label("loc_2E13")


    ChrTalk(
        0x9,
        (
            "The present situation may be difficult,\x01",
            "but if we could cooperate with Remiferia again,\x01",
            "even our medical supplies problem could be solved.\x02",
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

    label("loc_2EFC")

    Jump("loc_459B")

    label("loc_2F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_310B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3043")

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
            "The information restrictions\x01",
            "are most likely intentional due\x01",
            "to the declaration of invalidity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In a situation like this, we're not\x01",
            "able to deal with emergencies.\x01",
            "...I'm worried about everyone in the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3106")

    label("loc_3043")


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
            "In a situation like this, we're not\x01",
            "able to deal with emergencies.\x01",
            "...I'm worried about everyone in the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3106")

    Jump("loc_459B")

    label("loc_310B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_32EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3227")

    ChrTalk(
        0x9,
        (
            "The flow of information is restricted throughout\x01",
            "Crossbell. There's hardly any from within the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We get notified of emergency cases\x01",
            "from time to time. With things like this,\x01",
            "we're going to be too late...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hmm, this isn't a good situation.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_32E9")

    label("loc_3227")


    ChrTalk(
        0x9,
        (
            "The flow of information is restricted throughout\x01",
            "Crossbell. There's hardly any from within the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We're going to be too late responding to them...\x01",
            "Hmm, this isn't a good situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32E9")

    Jump("loc_459B")

    label("loc_32EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_34E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3424")

    ChrTalk(
        0x9,
        (
            "We're indebted to Miss\x01",
            "Tio for the orbal net\x01",
            "maintenance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the worst case scenario, we'll\x01",
            "be ready to receive patients because\x01",
            "the orbal net's still working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Allow me to take this opportunity\x01",
            "to thank you once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FUh uh, no...\x01",
            "It was nothing serious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_34E2")

    label("loc_3424")


    ChrTalk(
        0x9,
        (
            "We're greatly indebted to\x01",
            "Miss Tio for the orbal\x01",
            "net maintenance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although, such continuing situation\x01",
            "is terrible for the hospital.\x01",
            "I must think about something to deal with it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34E2")

    Jump("loc_459B")

    label("loc_34E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3971")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3630")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35B9")

    ChrTalk(
        0x9,
        (
            "I called Mr. Ricardo at\x01",
            "the airport to inform him the\x01",
            "goods were delivered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm glad he could\x01",
            "feel relieved too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I want such a thing to\x01",
            "never happen again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3627")

    label("loc_35B9")


    ChrTalk(
        0x9,
        (
            "I'm glad that Mr. Ricardo\x01",
            "can finally feel relieved too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I want such a thing to\x01",
            "never happen again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3627")

    TalkEnd(0x9)
    Return()

    label("loc_3630")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_36CA")

    ChrTalk(
        0x9,
        (
            "What happened in this case\x01",
            "is not your fault, so please,\x01",
            "keep up your spirits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At any rate, we'll try to\x01",
            "do something about it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    label("loc_36CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3766")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36ED")
    Call(0, 35)
    Jump("loc_3761")

    label("loc_36ED")


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
            "I-In any case, I'll try to contact\x01",
            "all places one more time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3761")

    Jump("loc_396C")

    label("loc_3766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38D1")

    ChrTalk(
        0x9,
        (
            "In a period of time a lot of persons\x01",
            "came saying that they had come\x01",
            "to visit Miss Ilya, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since Miss Ilya is still in a coma, I turn\x01",
            "down people except those authorised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even so, the people who\x01",
            "send her gifts and sweets\x01",
            "are never ending...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Once again, I felt that Miss\x01",
            "Ilya is indeed a great\x01",
            "existence for the citizens.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_396C")

    label("loc_38D1")


    ChrTalk(
        0x9,
        (
            "The people who send\x01",
            "sweets and the likes to\x01",
            "Miss Ilya are never ending.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Once again, I felt that\x01",
            "she's indeed a great\x01",
            "existence for the citizens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_396C")

    Jump("loc_459B")

    label("loc_3971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3BB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AF8")

    ChrTalk(
        0x9,
        (
            "Since yesterday, safety confirmations have been\x01",
            "coming from the Empire and Republic from the \x01",
            "families of the people who got injured in the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As expected, it seems that\x01",
            "many people get worried when\x01",
            "you're hospitalised abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As if that wasn't enough, a state of\x01",
            "tension continues in Crossbell after\x01",
            "the other day's independence proposal...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BB3")

    label("loc_3AF8")


    ChrTalk(
        0x9,
        (
            "As expected, it seems that\x01",
            "many people get worried when\x01",
            "you're hospitalised abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I want to deal with it with all my heart so\x01",
            "that they can return to their homes immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BB3")

    Jump("loc_459B")

    label("loc_3BB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3D8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CEE")

    ChrTalk(
        0x9,
        (
            "Thanks to the well-ordered orbal network\x01",
            "legislation, even the re-examination \x01",
            "reservations have increased too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think that if Crossbell becomes\x01",
            "independent, even useful bills\x01",
            "like that will pass easier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder how the local referendum\x01",
            "will turn out in practice?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3D8A")

    label("loc_3CEE")


    ChrTalk(
        0x9,
        (
            "I think that if Crossbell became\x01",
            "independent, even useful bills\x01",
            "would pass easier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder how the local referendum\x01",
            "will turn out in practice?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D8A")

    Jump("loc_459B")

    label("loc_3D8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3FA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EE1")

    ChrTalk(
        0x9,
        (
            "Yesterday, in Shizuku's surgery,\x01",
            "an epoch-making surgery method\x01",
            "devised by Professor Seiland was used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Interest from the medical personnel was great\x01",
            "and I can say that the trust they temporarily\x01",
            "lost was completely recovered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...However, we can't openly rejoice.\x01",
            "I wish it had been successful...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3F9D")

    label("loc_3EE1")


    ChrTalk(
        0x9,
        (
            "I can say that by trying an epoch-making\x01",
            "surgery, the trust they temporarily lost\x01",
            "was completely recovered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...However, we can't openly rejoice.\x01",
            "I wish it had been successful...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F9D")

    Jump("loc_459B")

    label("loc_3FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_414A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40B4")

    ChrTalk(
        0x9,
        (
            "Before long, a big surgery\x01",
            "is going to be performed\x01",
            "by Professor Seiland.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the other day inspection by\x01",
            "Archduke Albert, it was decided\x01",
            "a full backup from Remiferia too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We must also do as\x01",
            "much as possible for\x01",
            "the surgery success.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4145")

    label("loc_40B4")


    ChrTalk(
        0x9,
        (
            "Before long, a big surgery\x01",
            "is going to be performed\x01",
            "by Professor Seiland.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We must also do as\x01",
            "much as possible for\x01",
            "the surgery success.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4145")

    Jump("loc_459B")

    label("loc_414A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_42E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_423D")

    ChrTalk(
        0x9,
        (
            "I received words of thanks\x01",
            "from Archduke Albert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We have been receiving strong support since a while\x01",
            "from the Archduke who is a sponsor of the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "The entire staff personnel was very encouraged.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_42DF")

    label("loc_423D")


    ChrTalk(
        0x9,
        (
            "We have been receiving strong support since a while\x01",
            "from the Archduke who is a sponsor of the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "The entire staff personnel was very encouraged.\x02",
    )

    CloseMessageWindow()

    label("loc_42DF")

    Jump("loc_459B")

    label("loc_42E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_459B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44C8")

    ChrTalk(
        0x9,
        (
            "Because of the "Cult Incident" scandal,\x01",
            "the trust the hospital had established\x01",
            "was lost at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That's reasonable.\x01",
            "After all, a hospital doctor made use of drugs\x01",
            "and threw this land into confusion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By a thorough police investigation it\x01",
            "was confirmed that there're no problems\x01",
            "with the medicines he normally prescribed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, it seems that even now, among\x01",
            "the patients, there're those with a sense\x01",
            "of mistrust they can't wipe away.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_459B")

    label("loc_44C8")


    ChrTalk(
        0x9,
        (
            "Although suspicions were driven away,\x01",
            "there're still persons who hold a sense\x01",
            "of distrust towards the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "From now on, we must get back\x01",
            "trust gradually, aiming at an even\x01",
            "more open medical care.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_459B")

    TalkEnd(0x9)
    Return()

    # Function_9_2D13 end

    def Function_10_459F(): pass

    label("Function_10_459F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4791")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46BE")

    ChrTalk(
        0xA,
        (
            "The younger brother and friends...\x01",
            "The situation seems really terrible,\x01",
            "but we must never lose heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When everything is over and settled,\x01",
            "let's go have fun together again, ok?\x02",
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
        "#00000FHa ha, I'll do my best.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_478C")

    label("loc_46BE")


    ChrTalk(
        0xA,
        (
            "When everything is over and settled,\x01",
            "let's go have fun together again, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ada and Filia, Xilun and Meihua...\x01",
            "And let's invite Head Nurse Martha too this time...\x01",
            "Let's have a blast with everyone!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_478C")

    Jump("loc_54C0")

    label("loc_4791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_49A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48D2")

    ChrTalk(
        0xA,
        (
            "Even the stress of the outpatients visitors\x01",
            "who had to remain in the hospital has\x01",
            "gradually reached it's peak, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems they have started to have\x01",
            "hopes they can go back after\x01",
            "that happened in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I don't know what's going to happen,\x01",
            "but I hope they can go back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_49A4")

    label("loc_48D2")


    ChrTalk(
        0xA,
        (
            "After that happened in the city, it seems\x01",
            "that the outpatients visitors who had to remain\x01",
            "in the hospital started to have some hopes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I don't know what's going to happen,\x01",
            "but I hope they can go back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49A4")

    Jump("loc_54C0")

    label("loc_49A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_4B60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AC4")

    ChrTalk(
        0xA,
        (
            "As of yet, it seems there're\x01",
            "no chances of Ilya Platiｲre\x01",
            "complete recovery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...However, it's going to be fine.\x01",
            "The doctors at our hospital\x01",
            "are very excellent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It may take some time, but\x01",
            "you'll see that the doctors\x01",
            "will absolutely cure Ilya.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4B5B")

    label("loc_4AC4")


    ChrTalk(
        0xA,
        (
            "After all, the doctors at our\x01",
            "hospital are very excellent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It may take some time, but\x01",
            "you'll see that the doctors\x01",
            "will absolutely cure Ilya.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B5B")

    Jump("loc_54C0")

    label("loc_4B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4CF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C5C")

    ChrTalk(
        0xA,
        (
            "The situation is like this, but...\x01",
            "The people in the hospital are\x01",
            "unexpectedly positive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "After all, Ilya Platiｲre who\x01",
            "was in a coma has finally\x01",
            "opened her eyes.\x02",
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
    Jump("loc_4CED")

    label("loc_4C5C")


    ChrTalk(
        0xA,
        (
            "The fact that Ilya Platiｲre\x01",
            "has regained consciousness\x01",
            "is a good news in a long time.\x02",
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

    label("loc_4CED")

    Jump("loc_54C0")

    label("loc_4CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4D90")

    ChrTalk(
        0xA,
        (
            "*sigh*, say what you like,\x01",
            "but I started to feel tired...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...No, the patients are experiencing\x01",
            "even more suffering.\x01",
            "I can't complain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54C0")

    label("loc_4D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4E4E")

    ChrTalk(
        0xA,
        (
            "Due to the effects of yesterday's derailment\x01",
            "accident we're extremely busy too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I won't be in a mood to\x01",
            "be able to party for a while...\x01",
            "I have to do my job properly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54C0")

    label("loc_4E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4EC7")

    ChrTalk(
        0xA,
        (
            "Shizuku's mental strength\x01",
            "always cheers us up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We nurses must have hope too\x01",
            "and support Shizuku.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54C0")

    label("loc_4EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5047")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FAD")

    ChrTalk(
        0xA,
        (
            "Until now, Shizuku has gone\x01",
            "under many eye surgeries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, even if they're excellent \x01",
            "hospital doctors, it never goes well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Both that child and Mr. Arios\x01",
            "are probably really uneasy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5042")

    label("loc_4FAD")


    ChrTalk(
        0xA,
        (
            "Until now, Shizuku has gone\x01",
            "under many eye surgeries but\x01",
            "they never went well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Both that child and Mr. Arios\x01",
            "are probably really uneasy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5042")

    Jump("loc_54C0")

    label("loc_5047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_518F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_511F")

    ChrTalk(
        0xA,
        (
            "Rumor goes that Professor\x01",
            "Seiland is going to do a\x01",
            "major surgery soon, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In this hospital, the only\x01",
            "one who needs such a\x01",
            "surgery is "that child".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I hope she gets cured.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_518A")

    label("loc_511F")


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
        "I hope she gets cured.\x02",
    )

    CloseMessageWindow()

    label("loc_518A")

    Jump("loc_54C0")

    label("loc_518F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_531C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_526B")

    ChrTalk(
        0xA,
        (
            "Professor Ragot is currently\x01",
            "on a business trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems he's attending at\x01",
            "an academic meeting abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Professor Seiland is in charge of\x01",
            "today's internal medicine in his stead.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5317")

    label("loc_526B")


    ChrTalk(
        0xA,
        (
            "Today, Professor Ragot is on a business\x01",
            "trip for an academic meeting abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He was sighing that although the Archduke \x01",
            "was coming, he couldn't have greeted him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5317")

    Jump("loc_54C0")

    label("loc_531C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_54C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_545D")

    ChrTalk(
        0xA,
        (
            "Oh, if it isn't Mr. Randy\x01",
            "and the younger brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FDear Ran, been a while!\x02",
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
            "Since you're here, I'd\x01",
            "like to talk with you more\x01",
            "but I'm working now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Please speak to me again next time.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 6)
    Jump("loc_54C0")

    label("loc_545D")


    ChrTalk(
        0xA,
        (
            "I'd like to talk with you more,\x01",
            "but I'm working now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Please speak to me again next time.\x02",
    )

    CloseMessageWindow()

    label("loc_54C0")

    TalkEnd(0xFE)
    Return()

    # Function_10_459F end

    def Function_11_54C4(): pass

    label("Function_11_54C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5568")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54E2")
    Call(0, 12)
    Jump("loc_5563")

    label("loc_54E2")


    ChrTalk(
        0xB,
        (
            "*cough*, that's how my worthy\x01",
            "rival is supposed to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Come now, we can't make the patients wait.\x01",
            "Let's begin at once!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5563")

    Jump("loc_65E7")

    label("loc_5568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_57E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56DB")

    ChrTalk(
        0xB,
        (
            "I tried to hit some old medical\x01",
            "books with Seiland and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It seems possible to mix here some medicines\x01",
            "like anaesthetics and so on using the medical\x01",
            "plants growing in the autonomous state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Diplomatic ties with Remiferia were cut and\x01",
            "we have a constant lack of medical goods, but...\x01",
            "Maybe we can see a little hope for the future.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_57DB")

    label("loc_56DB")


    ChrTalk(
        0xB,
        (
            "I just searched with Seiland and it\x01",
            "seems some of the medicines we \x01",
            "lack of can be provided in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Diplomatic ties with Remiferia were cut and\x01",
            "we have a constant lack of medical goods, but...\x01",
            "Maybe we can see a little hope for the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57DB")

    Jump("loc_65E7")

    label("loc_57E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_58E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57FB")
    Call(0, 12)
    Jump("loc_58DB")

    label("loc_57FB")


    ChrTalk(
        0xB,
        (
            "Since being worried about my wife\x01",
            "and son I'm not in the mood to work\x01",
            "I was thinking I'd rather go home, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hm, he's a professional doctor too.\x01",
            "...It seems I've caused some\x01",
            "unnecessary worry. It's not like me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58DB")

    Jump("loc_65E7")

    label("loc_58E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5B09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A1E")

    ChrTalk(
        0xB,
        (
            "It appears that Crossbell Cathedral\x01",
            "too is enveloped inside the\x01",
            "barrier with the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wanted to consult with Archbishop\x01",
            "Eralda too about many things, but...\x01",
            "Since I can't contact him, there's nothing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F(Archbishop Eralda, eh...?\x01",
            "I wonder what is he doing now.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5B04")

    label("loc_5A1E")


    ChrTalk(
        0xB,
        (
            "I wanted to consult with Archbishop\x01",
            "Eralda too about many things, but...\x01",
            "Since I can't contact him, there's nothing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Maybe this too is a test the Goddess gave to me.\x01",
            "I must exert myself for the patients' sake too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B04")

    Jump("loc_65E7")

    label("loc_5B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5CC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C35")

    ChrTalk(
        0xB,
        (
            "The people injured in the raid\x01",
            "incidents are not only those who\x01",
            "suffered some physical injuries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "There're also many who were\x01",
            "shocked by the incident and due\x01",
            "to that their stomach hurts and so on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It can be said that mind and body\x01",
            "are very closely connected.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5CC4")

    label("loc_5C35")


    ChrTalk(
        0xB,
        (
            "There're people who develop health\x01",
            "disorders due to mental strain too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It can be said that mind and body\x01",
            "are very closely connected.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CC4")

    Jump("loc_65E7")

    label("loc_5CC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5F2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E54")

    ChrTalk(
        0xB,
        (
            "Before, I felt suspicious about the act itself\x01",
            "of using a scalpel on a person's body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, when the times advance and culture\x01",
            "progresses, there're many things that can't\x01",
            "be dealt with just internal medicine too.\x01",
            "...Like this train accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "By working in the hospital I once again\x01",
            "felt that it's important to accept new\x01",
            "forms of medical treatments.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5F28")

    label("loc_5E54")


    ChrTalk(
        0xB,
        (
            "Using a scalpel on a person's body...\x01",
            "Rejecting that was an old idea\x01",
            "that lacked flexibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "By working in the hospital I once again\x01",
            "felt that it's important to accept new\x01",
            "forms of medical treatments.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F28")

    Jump("loc_65E7")

    label("loc_5F2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_613A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6063")

    ChrTalk(
        0xB,
        (
            "The human body possesses\x01",
            "by nature the power to heal\x01",
            "injuries and illnesses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Many of the medicines prescribed in\x01",
            "internal medicine treat by accelerating\x01",
            "this "self-healing capacity".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This essential point is present in the Church.\x01",
            "We physicians operate on that basis.\x01\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6135")

    label("loc_6063")


    ChrTalk(
        0xB,
        (
            "The human body has the power\x01",
            "to heal injuries and illnesses...\x01",
            "I has a "self-healing capacity".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Many of the medicines prescribed in\x01",
            "internal medicine acts as a natural\x01",
            "treatment by accelerating that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6135")

    Jump("loc_65E7")

    label("loc_613A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_618A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6155")
    Call(0, 12)
    Jump("loc_6185")

    label("loc_6155")


    ChrTalk(
        0xB,
        (
            "...*sigh*, it's time I\x01",
            "cool down my anger.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6185")

    Jump("loc_65E7")

    label("loc_618A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_61C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61A5")
    Call(0, 12)
    Jump("loc_61BB")

    label("loc_61A5")


    ChrTalk(
        0xB,
        "Damn beardy...!!\x02",
    )

    CloseMessageWindow()

    label("loc_61BB")

    Jump("loc_65E7")

    label("loc_61C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_61CE")
    Jump("loc_65E7")

    label("loc_61CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_65E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6508")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_63F6")
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
            "Actually, tomorrow I'm going to announce \x01",
            "at an academic meeting a thesis about\x01",
            "the "Lupinus Grass" I was researching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I was just thinking to report\x01",
            "it to you all too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThe Lupinus Grass is that...\x01",
            "Medical grass we dealt with for a previous request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, congratulations.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes, it's thanks to you all.\x01",
            "Let me thank you once again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6500")

    label("loc_63F6")


    ChrTalk(
        0xB,
        (
            "*cough*!\x01",
            "My name is Ragot, in charge\x01",
            "of internal medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Actually, tomorrow I'm going to announce \x01",
            "at an academic meeting a thesis about\x01",
            "the "Lupinus Grass" I was researching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hu hu, it's really a privilege.\x01",
            "I must be in perfect physical condition.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6500")

    SetScenarioFlags(0x159, 7)
    Jump("loc_65E7")

    label("loc_6508")


    ChrTalk(
        0xB,
        (
            "Tomorrow, at an academic meeting abroad,\x01",
            "I'm going to announce my "Lupinus Grass" thesis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Actually, there's going to be an important\x01",
            "visitor at the hospital too... However, I can't\x01",
            "do anything about it this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65E7")

    TalkEnd(0xFE)
    Return()

    # Function_11_54C4 end

    def Function_12_65EB(): pass

    label("Function_12_65EB")

    OP_4B(0xB, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_67BF")

    ChrTalk(
        0xB,
        (
            "Professor Gary, I'll assist\x01",
            "you in your surgery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Please prepare the anaesthetics\x01",
            "they say you newly mixed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...Hu hu.\x01",
            "Today it seems that something else\x01",
            "aside from your bald head is shining too.\x02",
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
            "I don't know why, but today\x01",
            "I feel you look dignified like\x01",
            ""Back-Alley Dr. Glenn".\x02",
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
            "...Hu hu, then let's\x01",
            "begin the surgery!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hm!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6DC4")

    label("loc_67BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_6A1C")

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
            "live in Crossbell City...\x01",
            "Were you been able to contact them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "...No, lately not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I see...that's worrisome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...If it suits you then, why don't \x01",
            "you discuss with the State \x01",
            "Guard and go back to the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "No... My wife and Kientz too\x01",
            "can look after themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I can't leave the hospital in a situation\x01",
            "where we don't know when some heavy\x01",
            "injured patients will be carried in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "It's the same for you, right, Professor Ragot?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Hm, true. It seems I was\x01",
            "unnecessarily concerned.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DC4")

    label("loc_6A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6BC6")

    ChrTalk(
        0xB,
        (
            "Seiland's surgical technique is\x01",
            "probably the best that can be\x01",
            "thought at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Could the reason of its failure\x01",
            "be your ineptitude?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Wh...you too, couldn't you have made\x01",
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
        "...Let's this slide, this time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...Right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6DC4")

    label("loc_6BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6DC4")

    ChrTalk(
        0xB,
        (
            "At the other day's academic meeting,\x01",
            "my thesis was highly praised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Dear me, I would've liked for you\x01",
            "to see my gallant figure too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I too, the other day, received words of\x01",
            "encouragement directly from Archduke\x01",
            "Albert who came to observe the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            ""The growth of future surgical treatments\x01",
            "rest upon your shoulders"...\x01",
            "Man, I'm really grateful for what he said.\x02",
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
        "#4SDon't get elated, you beardy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#4SThat's my line, you baldy!\x02",
    )

    CloseMessageWindow()

    label("loc_6DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6DD7")
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xE, 0x10)

    label("loc_6DD7")

    SetScenarioFlags(0x2, 0)
    OP_4C(0xB, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_12_65EB end

    def Function_13_6DE3(): pass

    label("Function_13_6DE3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6FC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F05")

    ChrTalk(
        0xC,
        (
            "It seems there're also persons whose health is being\x01",
            "destroyed due to unrest towards this abnormal situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The mind field is outside the areas of expertise\x01",
            "in the hospital, but I must at least being able to\x01",
            "give some advice to those patients too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6FC2")

    label("loc_6F05")


    ChrTalk(
        0xC,
        "By nature, the mind field is the Church area of expertise...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "However, since they came on purpose\x01",
            "to the hospital, I must at least being\x01",
            "able to give advice to those patients too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FC2")

    Jump("loc_7818")

    label("loc_6FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_70C6")

    ChrTalk(
        0xC,
        (
            "With the help of the professors we\x01",
            "could take out all the medical grass\x01",
            "that were stored in the research building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's a hard time for many reasons, but\x01",
            "more than sitting on the fence without\x01",
            "doing anything, we must do something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7818")

    label("loc_70C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_70D4")
    Jump("loc_7818")

    label("loc_70D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_70E2")
    Jump("loc_7818")

    label("loc_70E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_70F0")
    Jump("loc_7818")

    label("loc_70F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_723D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71CC")

    ChrTalk(
        0xC,
        (
            "Because the other day a lot of patients were\x01",
            "carried in, I've been working all the time.\x01",
            "I'm almost at my limit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I guess I'll go take a nap at the dormitory\x01",
            "after a little more work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7238")

    label("loc_71CC")


    ChrTalk(
        0xC,
        (
            "Even so, although she's\x01",
            "kept working non-stop,\x01",
            "the professor is tough...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I too must gain stamina.\x02",
    )

    CloseMessageWindow()

    label("loc_7238")

    Jump("loc_7818")

    label("loc_723D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_724B")
    Jump("loc_7818")

    label("loc_724B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_732F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7266")
    Call(0, 37)
    Jump("loc_732A")

    label("loc_7266")


    ChrTalk(
        0xC,
        (
            "I happened to hear a story like\x01",
            "after enjoying theater and plays,\x01",
            "a patient's illness was cured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If that's the case, I'm glad he\x01",
            "happily passed time together\x01",
            "with his grandchild lately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_732A")

    Jump("loc_7818")

    label("loc_732F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_733D")
    Jump("loc_7818")

    label("loc_733D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_777C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7596")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74E0")

    ChrTalk(
        0xC,
        (
            "When I came to know that doctor\x01",
            "Joachim was the ringleader of\x01",
            "that incident, it was a shock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even after Doctor Seiland took\x01",
            "her post as my new superior, I \x01",
            "felt down for a while, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            ""As long as there're patients,\x01",
            "we have no time to be feeling down."\x01",
            "...That's what the doctor said to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "At any rate, now I intend to work\x01",
            "sedulously under the doctor's lead.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7591")

    label("loc_74E0")


    ChrTalk(
        0xC,
        (
            "Doctor Seiland is giving me\x01",
            "one job after the other.\x01",
            "Thanks to this, I have no time to feel down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Ha ha, that strictness too could be\x01",
            "a form of the doctor's kindness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7591")

    Jump("loc_7777")

    label("loc_7596")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_769F")

    ChrTalk(
        0xC,
        (
            "After the mixed medicine had effect,\x01",
            "the condition stabilised. With this, \x01",
            "there's nothing to worry for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Nevertheless, His Grace the Archduke seems\x01",
            "to have quite a deep medical knowledge.\x01",
            "I'd like to strive to be like him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7777")

    label("loc_769F")


    ChrTalk(
        0xC,
        (
            "It seems that His Grace the Archduke and Professor\x01",
            "Seiland have been friends since a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Professor Seiland talking like she \x01",
            "always does to His Grace the Archduke\x01",
            "somehow made me feel nervous...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7777")

    Jump("loc_7818")

    label("loc_777C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7818")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7797")
    Call(0, 39)
    Jump("loc_7818")

    label("loc_7797")


    ChrTalk(
        0xC,
        (
            "I'm really happy too that\x01",
            "Mr. Quine became able\x01",
            "to take his medicines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This is all thanks to little\x01",
            "Amisaah's efforts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7818")

    TalkEnd(0xFE)
    Return()

    # Function_13_6DE3 end

    def Function_14_781C(): pass

    label("Function_14_781C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_78CF")

    ChrTalk(
        0xD,
        (
            "We're flooded with patients and\x01",
            "quite busy, but... I'm gonna do it!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'm not yet there, but I'll\x01",
            "become a capable female\x01",
            "doctor like Professor Seiland!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8455")

    label("loc_78CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_797A")

    ChrTalk(
        0xD,
        (
            "Unexpectedly even the folk remedies\x01",
            "could become useful as reference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I should've left it on the dormitory bookshelves.\x01",
            "I'll go look for it later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8455")

    label("loc_797A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_7BC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AC0")

    ChrTalk(
        0xD,
        (
            "I'm arranging the medicines that\x01",
            "were provided by the State Guard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Really though, they all feel like\x01",
            "things a novice arranged out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We'll be able to manage for the time being,\x01",
            "but if a patient with an incurable disease came,\x01",
            "as you can expect we wouldn't be able to deal with him...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7BC0")

    label("loc_7AC0")


    ChrTalk(
        0xD,
        (
            "The medicines that the State Guard\x01",
            "provided really all feel like things\x01",
            "a novice arranged out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We'll be able to manage for the time being,\x01",
            "but if a patient with an incurable disease came,\x01",
            "as you can expect we wouldn't be able to deal with him...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BC0")

    Jump("loc_8455")

    label("loc_7BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_7C7A")

    ChrTalk(
        0xD,
        (
            "Although the reception of outpatients\x01",
            "has stopped, we don't know when a\x01",
            "patient with a serious illness will come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "We must make at least proper preparations.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8455")

    label("loc_7C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7E3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D9E")

    ChrTalk(
        0xD,
        (
            ""In times like this, a doctor must\x01",
            "not show his depressed expression..."\x01",
            "Professor Ragot taught me that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If even us did a worried face,\x01",
            "that would pass to the patient too.\x01",
            "I must be careful...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In a certain sense,\x01",
            "that worry could be\x01",
            "like an illness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7E36")

    label("loc_7D9E")


    ChrTalk(
        0xD,
        (
            ""In times like this, a doctor must\x01",
            "not show his depressed expression..."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...I understand it with my head,\x01",
            "but it could be difficult for me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E36")

    Jump("loc_8455")

    label("loc_7E3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7FE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F54")

    ChrTalk(
        0xD,
        (
            "Getting hit by the rain and soaked wet,\x01",
            "it's easy to catch a cold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The cause seems to be that by having the\x01",
            "body get cold, the immunity abilities\x01",
            "we have don't work anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You too, when you get home\x01",
            "you must properly change\x01",
            "and warm up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7FE2")

    label("loc_7F54")


    ChrTalk(
        0xD,
        (
            "Getting hit by the rain and soaked wet,\x01",
            "it's easy to catch a cold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You too, when you get home\x01",
            "you must properly change\x01",
            "and warm up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FE2")

    Jump("loc_8455")

    label("loc_7FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_80A7")

    ChrTalk(
        0xD,
        (
            "Somehow Lytton seems to be making\x01",
            "many hospital rounds as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Mrgrgr, I won't lose too.\x01",
            "I too will  become a dependable female \x01",
            "doctor who the patients can trust!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8455")

    label("loc_80A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_80B5")
    Jump("loc_8455")

    label("loc_80B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_821C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_819F")

    ChrTalk(
        0xD,
        (
            "Oh jeez, the professors seem\x01",
            "to be quarreling again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In times like this, it's\x01",
            "quicker to let them finish\x01",
            "than ineptly intervening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I guess I'll sort out the clinical\x01",
            "records now that I can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8217")

    label("loc_819F")


    ChrTalk(
        0xD,
        (
            "I've already got used to\x01",
            "the professors' quarrels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I guess I'll sort out the clinical\x01",
            "records now that I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8217")

    Jump("loc_8455")

    label("loc_821C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_82D8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8299")

    ChrTalk(
        0xD,
        (
            "The professor\x01",
            "is really great...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...No, I mustn't.\x01",
            "I must properly do\x01",
            "the things I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82D3")

    label("loc_8299")


    ChrTalk(
        0xD,
        (
            "Even so, I'm\x01",
            "so pathetic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I have to study more.\x02",
    )

    CloseMessageWindow()

    label("loc_82D3")

    Jump("loc_8455")

    label("loc_82D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8455")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83DF")

    ChrTalk(
        0xD,
        (
            "Recently, Flora, my roommate at the dormitory,\x01",
            "is taking care of a newcomer medical intern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Micheau...I guess...?\x01",
            "Somehow I got reminded of the\x01",
            "time when I was a newcomer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, it doesn't change\x01",
            "that I'm still studying.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8455")

    label("loc_83DF")


    ChrTalk(
        0xD,
        (
            "Looking at Micheau I got\x01",
            "reminded of the time\x01",
            "when I was a newcomer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Well, I too am still studying, though.\x02",
    )

    CloseMessageWindow()

    label("loc_8455")

    TalkEnd(0xFE)
    Return()

    # Function_14_781C end

    def Function_15_8459(): pass

    label("Function_15_8459")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_850F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8477")
    Call(0, 12)
    Jump("loc_850A")

    label("loc_8477")


    ChrTalk(
        0xE,
        (
            "I don't like Professor Ragot, but\x01",
            "I can't rely on anyone else's\x01",
            "support than his.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hu hu, I feel like now I\x01",
            "could do any kind of surgery.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_850A")

    Jump("loc_90BA")

    label("loc_850F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_8691")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_860F")

    ChrTalk(
        0xE,
        (
            "It seems that at the internal medicine and\x01",
            "neurology - pharmacology they intend to try\x01",
            "to do something for the lacking medical goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...I can't operate now, so while\x01",
            "I'm not working I'm helping out\x01",
            "Ashram and Chaleur.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_868C")

    label("loc_860F")


    ChrTalk(
        0xE,
        (
            "While I'm not working I'm helping\x01",
            "out Ashram and Chaleur.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Preparations must be perfect so\x01",
            "we can operate any time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_868C")

    Jump("loc_90BA")

    label("loc_8691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_8741")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86AC")
    Call(0, 12)
    Jump("loc_873C")

    label("loc_86AC")


    ChrTalk(
        0xE,
        (
            "...Even Professor Ragot can\x01",
            "say clever things, occasionally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, since my wife and\x01",
            "Kientz are fine for sure,\x01",
            "I don't need to worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_873C")

    Jump("loc_90BA")

    label("loc_8741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_885E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87D4")

    ChrTalk(
        0xE,
        (
            "...I wonder how my wife and\x01",
            "Kientz who remained in the\x01",
            "city are doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I hope they're not\x01",
            "sick or anything...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8859")

    label("loc_87D4")


    ChrTalk(
        0xE,
        "...*sigh*, I'll stop worrying.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "They haven't been carried here,\x01",
            "so there's no doubt that my wife\x01",
            "and Kientz are doing fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8859")

    Jump("loc_90BA")

    label("loc_885E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_89C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8957")

    ChrTalk(
        0xE,
        (
            "I've been working at the hospital for\x01",
            "many years, but it's the first time we\x01",
            "had in-patients to fill up the rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It can be said it's truly an unprecedented situation.\x01",
            "We must overcome it in a way or another...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_89C2")

    label("loc_8957")


    ChrTalk(
        0xE,
        (
            "This situation...\x01",
            "It can be said it's truly unprecedented.\x01",
            "We must overcome it in a way or another...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89C2")

    Jump("loc_90BA")

    label("loc_89C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8B51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AAB")

    ChrTalk(
        0xE,
        (
            "*phew*...I ended the surgeries\x01",
            "some moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Anyway, there're many patients.\x01",
            "Their treatment ended up until morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "After I finish today's examinations,\x01",
            "I want to sleep like a log.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8B4C")

    label("loc_8AAB")


    ChrTalk(
        0xE,
        (
            "I'm tired due to surgeries until the morning, but...\x01",
            "I can't make a patient wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I have to do my job properly until\x01",
            "I'm over with today's treatments.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B4C")

    Jump("loc_90BA")

    label("loc_8B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8D01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C62")

    ChrTalk(
        0xE,
        (
            "Recently, it seems that my son,\x01",
            "Kientz, is worried about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "*sigh*, I'm busy with the job at the hospital\x01",
            "and my worries never cease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If I'm careless, I could be stuck\x01",
            "with getting stomach pains\x01",
            "treated by Professor Ragot.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8CFC")

    label("loc_8C62")


    ChrTalk(
        0xE,
        (
            "Boy oh boy, my public and private\x01",
            "worries never cease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If I'm careless, I could be stuck\x01",
            "with getting stomach pains\x01",
            "treated by Professor Ragot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CFC")

    Jump("loc_90BA")

    label("loc_8D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8DD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D1C")
    Call(0, 12)
    Jump("loc_8DD1")

    label("loc_8D1C")


    ChrTalk(
        0xE,
        (
            "We took part in the surgery too, but\x01",
            "just this time we were forced to\x01",
            "realize our helplessness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Will this failure throw the patient in despair...?\x01",
            "That's my only concern.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DD1")

    Jump("loc_90BA")

    label("loc_8DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8E19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DF1")
    Call(0, 12)
    Jump("loc_8E14")

    label("loc_8DF1")


    ChrTalk(
        0xE,
        "Don't get elated, baldyyy...!\x02",
    )

    CloseMessageWindow()

    label("loc_8E14")

    Jump("loc_90BA")

    label("loc_8E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8F36")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8E9E")

    ChrTalk(
        0xE,
        "It seem His Grace the Archduke has gone back...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "*sigh*, oh boy...\x01",
            "How troublesome is Ashram too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F31")

    label("loc_8E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EB0")
    Call(0, 16)
    Jump("loc_8F31")

    label("loc_8EB0")


    ChrTalk(
        0xE,
        (
            "His Grace the Archduke came to observe,\x01",
            "and yet she's doing things at her own pace...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I must severely\x01",
            "scold Ashram...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F31")

    Jump("loc_90BA")

    label("loc_8F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_90BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_901B")

    ChrTalk(
        0xE,
        (
            "Damn Professor Ragot, \x01",
            "it seems he's in ruptures.\x02",
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
            "...Well, it's true that his research\x01",
            "is worth to be praised.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_90BA")

    label("loc_901B")


    ChrTalk(
        0xE,
        (
            "I have no choice but to acknowledge\x01",
            "Professor Ragot's research results.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "His ruptures get on my nerves, but...\x01",
            "Hmph, I'll endure, just for this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90BA")

    TalkEnd(0xFE)
    Return()

    # Function_15_8459 end

    def Function_16_90BE(): pass

    label("Function_16_90BE")

    OP_4B(0xE, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xE,
        (
            "C-Chaleur, has\x01",
            "Ashram slept in!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Yes, most likely.\x01",
            "...It seems that yesterday too she holed\x01",
            "up in the research building until late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "T-The Archduke is coming\x01",
            "to observe, and yet she...\x01",
            "How slovenly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Damn, go rouse her out\x01",
            "of bed no matter what!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0x10, 0x10)
    OP_4C(0xE, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_16_90BE end

    def Function_17_91E7(): pass

    label("Function_17_91E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9381")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92CA")

    ChrTalk(
        0xF,
        (
            "The giant tree that has appeared in\x01",
            "the Marshlands environs is too cool...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Under what principles and for what\x01",
            "purpose did it appear in that place...?\x01",
            "It doesn't lack scientific interest!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_937C")

    label("loc_92CA")


    ChrTalk(
        0xF,
        (
            "...Ah! I was unintentionally merry.\x01",
            "I'm sorry, in such a time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "At any rate, now I must properly\x01",
            "do the medical treatment tools\x01",
            "maintenance to deal with the patients.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_937C")

    Jump("loc_A2CF")

    label("loc_9381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_94F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9450")

    ChrTalk(
        0xF,
        "*drowsy drowsy*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I'm checking the old type tools for when\x01",
            "the new type of medical treatment tools break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "*yaaaaaaawn"... I'm sleepy, \x01",
            "but I must do it properly...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_94F2")

    label("loc_9450")


    ChrTalk(
        0xF,
        (
            "*drowsy drowsy*...\x01",
            "Nevertheless, the old stuff is\x01",
            "surprisingly sturdy made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Many are large and boorish...\x01",
            "It seems it would feel nice to lie on them...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94F2")

    Jump("loc_A2CF")

    label("loc_94F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_96C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9601")

    ChrTalk(
        0xF,
        (
            "Somehow I found a spare part\x01",
            "that had deteriorated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "However, because it's a unique part,\x01",
            "we won't be able to obtain a new one\x01",
            "unless we order it from Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "*sigh*, what a problem.\x01",
            "We must use it carefully, carefully...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_96C1")

    label("loc_9601")


    ChrTalk(
        0xF,
        (
            "The parts of the medical treatment tools\x01",
            "we use at the hospital can't be obtained\x01",
            "unless we order them from Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "*sigh*, what a problem.\x01",
            "We must use it carefully, carefully...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96C1")

    Jump("loc_A2CF")

    label("loc_96C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_9994")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98EB")
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xF,
        "Oh, Tio.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I'm currently doing the medical\x01",
            "treatment tools maintenance...\x01",
            "Who do you say about these values?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FHmm...the durability is slightly\x01",
            "lesser than the minimal required value.\x02\x03",
            "#00203FI think that probably the moving\x01",
            "parts are degrading due to aging.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "As I thought, then.\x01",
            "Hmm, how troublesome...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(In the time she's been here, Tio seems\x01",
            "to have gotten quite familiar with her...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F(Hu hu, if it's for the orbal tools field,\x01",
            "she's been pretty useful here, I bet?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_998F")

    label("loc_98EB")


    ChrTalk(
        0xF,
        (
            "Hmm, how troublesome.\x01",
            "They're Seiland Corp. made,\x01",
            "so we can't order new ones...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "However, I'll have to do something.\x01",
            "For now, I'll look around for spares.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_998F")

    Jump("loc_A2CF")

    label("loc_9994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9B12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A75")

    ChrTalk(
        0xF,
        (
            "Ehhm, later I'll have to do a round\x01",
            "to the research building ICU.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I must go check\x01",
            "Mr. Donovan's artificial\x01",
            "respirator too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "*phew*, the work increased all\x01",
            "at once and I'm really busy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9B0D")

    label("loc_9A75")


    ChrTalk(
        0xF,
        (
            "*phew*, the work increased all\x01",
            "at once and I'm really busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It seems it'll be a long way off until I\x01",
            "can go back to my days full of research.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B0D")

    Jump("loc_A2CF")

    label("loc_9B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9C13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BBD")

    ChrTalk(
        0xF,
        (
            "Yesterday, the medical treatment tools\x01",
            "for surgery were used a great lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I'm really glad I asked\x01",
            "Chaleur to do habitual\x01",
            "maintenance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9C0E")

    label("loc_9BBD")


    ChrTalk(
        0xF,
        (
            "All the medical interns are\x01",
            "nothing but excellent kids\x01",
            "so I get helped too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C0E")

    Jump("loc_A2CF")

    label("loc_9C13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9E04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D81")

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
            "By applying the principles of the exposure Quartz and\x01",
            "using a device that sends visual information to the brain, \x01",
            "it could be possible to enhance eyesight artificially...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "(*clakclakclakclakclakclak*...)\x01",
            "...Hmm, no good, as I feared.\x01",
            "It would take several tens of years to develop...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9DFF")

    label("loc_9D81")


    ChrTalk(
        0xF,
        (
            "No uuuse...\x01",
            "As I feared, maybe it's impossible for me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "...No, I can't give up.\x01",
            "Fight, me! For Shizuku's sake too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DFF")

    Jump("loc_A2CF")

    label("loc_9E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9FB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F09")

    ChrTalk(
        0xF,
        (
            "For Shizuku's surgery, what could be said \x01",
            "to be the most advanced modern medicine\x01",
            "equipment was prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "That would end up failing is...\x01",
            "Uugh, I can't accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It's inexcusable towards\x01",
            "Shizuku who believed in us...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9FAF")

    label("loc_9F09")


    ChrTalk(
        0xF,
        (
            "Making people happy with science...\x01",
            "In order to do that, I kept researching\x01",
            "medical treatment tools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It's inexcusable towards\x01",
            "Shizuku who believed in us...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FAF")

    Jump("loc_A2CF")

    label("loc_9FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A09C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FCF")
    Call(0, 18)
    Jump("loc_A097")

    label("loc_9FCF")

    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xF,
        (
            "...Yes, good, good!\x01",
            "It seems this time it went well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Uh uh, I guess that at this rate, today\x01",
            "I'll progress till the endurance tests too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "(The full course today too, I guess...)\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)

    label("loc_A097")

    Jump("loc_A2CF")

    label("loc_A09C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A0AA")
    Jump("loc_A2CF")

    label("loc_A0AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A2CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A22F")

    ChrTalk(
        0xF,
        (
            "When I've heard that Professor\x01",
            "Seiland had been appointed here,\x01",
            "I was almost jumping around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Due to the nature of my job, every day I\x01",
            "see the name "Seiland Corp.", the major\x01",
            "medical treatment tools manufacturer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "She seems to be a relative of the president...\x01",
            "Uhuhu, it would be nice if I could get some\x01",
            "behind the scene stories about the company.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_A2CF")

    label("loc_A22F")


    ChrTalk(
        0xF,
        (
            "However, Professor Seiland\x01",
            "is somehow scary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I'd like to ask many stories about\x01",
            "the Seiland Corporation, but...\x01",
            "I can't quite get the right timing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2CF")

    TalkEnd(0xFE)
    Return()

    # Function_17_91E7 end

    def Function_18_A2D3(): pass

    label("Function_18_A2D3")

    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xF,
        (
            "Alright, Chaleur.\x01",
            "I'm ready here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Please adjust the orbal pressure\x01",
            "after I switch it on.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    ChrTalk(
        0x10,
        (
            "Roger.\x01",
            "...Let's hope it doesn't\x01",
            "explode this time, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Don't mind it even if it does♪\x01",
            "Mistake is the mother of success, after all.\x02",
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
            "#00211F(...She isn't wrong,\x01",
            "but that's dangerous.)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x2, 2)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_93(0x10, 0x5A, 0x0)
    Return()

    # Function_18_A2D3 end

    def Function_19_A486(): pass

    label("Function_19_A486")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A62A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A58A")

    ChrTalk(
        0x10,
        (
            "The Chief had been sleepy for a while,\x01",
            "but after she saw that tree appearing,\x01",
            "she's been enthusiastic like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "With the Chief in that state, she'll probably\x01",
            "work for three days and three nights.\x01",
            "I have to keep up too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A625")

    label("loc_A58A")


    ChrTalk(
        0x10,
        (
            "The civil war in the Empire...\x01",
            "That bluish huge tree...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I'm worried about many things,\x01",
            "but for now I have to focus on\x01",
            "keeping up with the Chief.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A625")

    Jump("loc_B59A")

    label("loc_A62A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_A775")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A70B")

    ChrTalk(
        0x10,
        (
            "Hm, their efficiency seems very low but\x01",
            "it seems they can be used in an emergency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Because there're many, we ended up\x01",
            "checking them out all night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "...Well, it always happens, so...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A770")

    label("loc_A70B")


    ChrTalk(
        0x10,
        (
            "After an all night check,\x01",
            "Chief Ashram too looks sleepy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "...Well, it always happens, so...\x02",
    )

    CloseMessageWindow()

    label("loc_A770")

    Jump("loc_B59A")

    label("loc_A775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_A866")

    ChrTalk(
        0x10,
        (
            "Professor Gary too is probably worried about \x01",
            "his family, but he seems to be concentrating\x01",
            "a lot on his job at the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "...I too will believe in my family's\x01",
            "safety and put effort in helping\x01",
            "out Chief Ashram now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B59A")

    label("loc_A866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_AA58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9B0")

    ChrTalk(
        0x10,
        (
            "Right before Crossbell independence,\x01",
            "a leaving notice came from the Empire\x01",
            "but I decided to remain here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Since I still have many things\x01",
            "to learn, I can't return back\x01",
            "to my home country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "...Still, the civil war that outbroke\x01",
            "in the Empire concerns me a little.\x01",
            "I hope my family is safe...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_AA53")

    label("loc_A9B0")


    ChrTalk(
        0x10,
        (
            "Now at this late hour I don't have any\x01",
            "regret in having stayed back in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "...Still, the Empire civil war worries me.\x01",
            "I hope my family is safe...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA53")

    Jump("loc_B59A")

    label("loc_AA58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_AC24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB82")

    ChrTalk(
        0x10,
        (
            "It's been whispered that the\x01",
            "raid incident was a plot by\x01",
            "the Imperial government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "That incident where a lot of people were\x01",
            "carried to the hospital was the Empire deed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I don't want to bad mouth my home country,\x01",
            "but if that's true, I'll hold it in scorn.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_AC1F")

    label("loc_AB82")


    ChrTalk(
        0x10,
        (
            "My goal was to practice in my home\x01",
            "country, the Empire, in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If it's really an Imperial government plot,\x01",
            "I'll hold my homeland in scorn.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC1F")

    Jump("loc_B59A")

    label("loc_AC24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_ADCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD68")

    ChrTalk(
        0x10,
        (
            "For medical treatment tools,\x01",
            "an habitual and detailed\x01",
            "maintenance is essential.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If something were to happen to a patient\x01",
            "due to the breakdown of a medical tool,\x01",
            "it would defeat its purpose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I must do a proper maintenance\x01",
            "so that they're good for whenever\x01",
            "a patient gets carried in.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_ADC9")

    label("loc_AD68")


    ChrTalk(
        0x10,
        (
            "I must do a proper maintenance\x01",
            "so that they're good for whenever\x01",
            "a patient gets carried in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADC9")

    Jump("loc_B59A")

    label("loc_ADCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_AFAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AEEB")

    ChrTalk(
        0x10,
        (
            "After Shizuku's surgery, the Chief has\x01",
            "been researching something without rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "It seems she's groping for a\x01",
            "method to cure Shizuku's\x01",
            "eyes by using orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "As I thought, the Chief is amazing...\x01",
            "I didn't even think about something like that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_AFAA")

    label("loc_AEEB")


    ChrTalk(
        0x10,
        (
            "Recovering the eyesight using orbments, eh...?\x01",
            "I didn't even think about something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "However, it's entwined to the neurology field too...\x01",
            "It could be difficult to realize.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFAA")

    Jump("loc_B59A")

    label("loc_AFAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B143")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0B4")

    ChrTalk(
        0x10,
        (
            "Regarding that surgery, I think that\x01",
            "the professors did their very best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Even so, I can't help but say that it's a pity\x01",
            "she didn't have a complete recovery, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Personally, I'd want them to\x01",
            "not be so much depressed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_B13E")

    label("loc_B0B4")


    ChrTalk(
        0x10,
        (
            "Regarding that surgery, I think that\x01",
            "the professors did their very best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Personally, I'd want them to\x01",
            "not be so much depressed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B13E")

    Jump("loc_B59A")

    label("loc_B143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B203")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B15E")
    Call(0, 18)
    Jump("loc_B1FE")

    label("loc_B15E")


    ChrTalk(
        0x10,
        (
            "No matter how much she fails,\x01",
            "Chief Ashram doesn't get discouraged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Maybe I should greatly follow her temper\x01",
            "as a medical treatment tools researcher.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1FE")

    Jump("loc_B59A")

    label("loc_B203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B3A1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B2E7")

    ChrTalk(
        0x10,
        (
            "In the end, Chief Ashram\x01",
            "didn't make it, eh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Well, the other day too the Chief pulled out\x01",
            "an all nighter, so I didn't think in the slightest\x01",
            "she would've made it in time for the inspection.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B39C")

    label("loc_B2E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2F9")
    Call(0, 16)
    Jump("loc_B39C")

    label("loc_B2F9")


    ChrTalk(
        0x10,
        (
            "It happens many times that Chief Ashram stays up\x01",
            "all night working hard on her research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I guess that now she should be\x01",
            "still sleeping at the dormitory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B39C")

    Jump("loc_B59A")

    label("loc_B3A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B59A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4F8")

    ChrTalk(
        0x10,
        (
            "Chief Ashram is an expert of\x01",
            "medical treatment tools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "It seems that previously the Chief studied the\x01",
            "basis of orbal tools at the Epstein Foundation HQ\x01",
            "in the autonomous state of Leman, where she is from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I'm helping out on the research\x01",
            "about different medical treatment\x01",
            "tools under a chief like that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_B59A")

    label("loc_B4F8")


    ChrTalk(
        0x10,
        (
            "Medical tools are something indispensable\x01",
            "in modern medical treatments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I believe that this research will open a\x01",
            "path in the future of medical science.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B59A")

    TalkEnd(0xFE)
    Return()

    # Function_19_A486 end

    def Function_20_B59E(): pass

    label("Function_20_B59E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B647")

    ChrTalk(
        0x11,
        "I'm relieved they've started accepting outpatients again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I've run out of the medicine I was taking\x01",
            "and I was thinking what should I've done.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA04")

    label("loc_B647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_B655")
    Jump("loc_BA04")

    label("loc_B655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B663")
    Jump("loc_BA04")

    label("loc_B663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B72C")

    ChrTalk(
        0x11,
        (
            "Hmm, since they aren't calling at all...\x01",
            "I guess the medical examinations are really delayed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "There was a raid incident like that,\x01",
            "so the doctors too are probably quite busy...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA04")

    label("loc_B72C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B73A")
    Jump("loc_BA04")

    label("loc_B73A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B7E0")

    ChrTalk(
        0x11,
        "Today, I have an appointment first thing in the morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I used the orbal net for the appointment\x01",
            "and as I thought, it was really convenient.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA04")

    label("loc_B7E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B7EE")
    Jump("loc_BA04")

    label("loc_B7EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B930")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8C0")

    ChrTalk(
        0x11,
        (
            "The other day I was looking up\x01",
            "at that Orchis Tower at the\x01",
            "unveiling ceremony and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I overstretched my back.\x01",
            "I inadvertently ended up hurting my hips.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Oow ow ow ow...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B92B")

    label("loc_B8C0")


    ChrTalk(
        0x11,
        (
            "I looked up too much at Orchis Tower and\x01",
            "inadvertently ended up hurting my hips.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Oow ow ow ow...\x02",
    )

    CloseMessageWindow()

    label("loc_B92B")

    Jump("loc_BA04")

    label("loc_B930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B93E")
    Jump("loc_BA04")

    label("loc_B93E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BA04")

    ChrTalk(
        0x11,
        (
            "After the Cult incident, the\x01",
            "hospital did a prompt investigation\x01",
            "and proved their innocence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Thus, it's really a nice thing\x01",
            "to be able to commute to\x01",
            "the hospital without worries.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA04")

    TalkEnd(0xFE)
    Return()

    # Function_20_B59E end

    def Function_21_BA08(): pass

    label("Function_21_BA08")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BAA7")

    ChrTalk(
        0x12,
        (
            "To us elderly, it's something\x01",
            "very important to have a\x01",
            "hospital we can go to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I'm really glad that I'm\x01",
            "able to come here like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDDC")

    label("loc_BAA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_BAB5")
    Jump("loc_BDDC")

    label("loc_BAB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_BAC3")
    Jump("loc_BDDC")

    label("loc_BAC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BB39")

    ChrTalk(
        0x12,
        (
            "*sigh*... I wonder if\x01",
            "Crossbell is really fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "I can't even sleep at night for the unrest...\x02",
    )

    CloseMessageWindow()
    Jump("loc_BDDC")

    label("loc_BB39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BBBA")

    ChrTalk(
        0x12,
        (
            "A train derailment accident...\x01",
            "That really shocked me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I wonder if all the passenger\x01",
            "are safe and sound.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDDC")

    label("loc_BBBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BBC8")
    Jump("loc_BDDC")

    label("loc_BBC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BC66")

    ChrTalk(
        0x12,
        (
            "I've been commuting to this\x01",
            "hospital for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "The doctors are even skillful in surgeries...\x01",
            "I can come and go with peace of mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDDC")

    label("loc_BC66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_BC74")
    Jump("loc_BDDC")

    label("loc_BC74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_BD33")

    ChrTalk(
        0x12,
        (
            "Professor Ragot, my personal doctor,\x01",
            "seems to be on vacation today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "That doctor called Seiland...\x01",
            "She's young for being a doctor,\x01",
            "I wonder if everything will be fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDDC")

    label("loc_BD33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BDDC")

    ChrTalk(
        0x12,
        (
            "Even now I can't believe that\x01",
            "Doctor Joachim caused such\x01",
            "an outrageous incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Aah, scary, scary...\x01",
            "You can't really know\x01",
            "what people are thinking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDDC")

    TalkEnd(0xFE)
    Return()

    # Function_21_BA08 end

    def Function_22_BDE0(): pass

    label("Function_22_BDE0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BEE0")

    ChrTalk(
        0x13,
        (
            "Before President Dieter was arrested,\x01",
            "he didn't allow to come to the hospital\x01",
            "for small illnesses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "However, to a parent, the illness of his child \x01",
            "is important, even if it's a mere cold.\x01",
            "I wish he were a little more considerate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2D7")

    label("loc_BEE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_BEEE")
    Jump("loc_C2D7")

    label("loc_BEEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_BEFC")
    Jump("loc_C2D7")

    label("loc_BEFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BF56")

    ChrTalk(
        0x13,
        "Hey...quiet down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "You mustn't cause\x01",
            "trouble for the other people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2D7")

    label("loc_BF56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C025")

    ChrTalk(
        0x13,
        (
            "We were riding on the train\x01",
            "that derailed, however...\x01",
            "Luckily, we had minor injuries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I'm glad we can be discharged in one day,\x01",
            "but I wonder what happened to the railroad after that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2D7")

    label("loc_C025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C033")
    Jump("loc_C2D7")

    label("loc_C033")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C1C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C150")

    ChrTalk(
        0x13,
        (
            "Recently due to a medical \x01",
            "check-up I was warned that\x01",
            "I eat too much sweet things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I was said that at this rate it'll be bad for my body,\x01",
            "so I'm reconsidering my lifestyle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Even so, I unintentionally\x01",
            "reach for sweet things.\x01",
            "I must be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_C1BC")

    label("loc_C150")


    ChrTalk(
        0x13,
        (
            "I unintentionally reach\x01",
            "for sweet things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "It's my body we're talking about,\x01",
            "so I must be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1BC")

    Jump("loc_C2D7")

    label("loc_C1C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C1CF")
    Jump("loc_C2D7")

    label("loc_C1CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C2CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C245")

    ChrTalk(
        0x13,
        "Uuhm, what a nice smell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Something like this relieves\x01",
            "a patient's feelings.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    ClearChrFlags(0x13, 0x10)
    Jump("loc_C2C9")

    label("loc_C245")


    ChrTalk(
        0x13,
        (
            "I came to the hospital to\x01",
            "accompany my mother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "It seems there're many unique things here,\x01",
            "so I guess I'll explore around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2C9")

    Jump("loc_C2D7")

    label("loc_C2CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C2D7")

    label("loc_C2D7")

    TalkEnd(0xFE)
    Return()

    # Function_22_BDE0 end

    def Function_23_C2DB(): pass

    label("Function_23_C2DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C38A")

    ChrTalk(
        0x14,
        (
            "I was finally able to come to the hospital,\x01",
            "but it's incredibly crowded...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "The doctors must be having it hard too,\x01",
            "but I wish they'd do their best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C72C")

    label("loc_C38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_C398")
    Jump("loc_C72C")

    label("loc_C398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_C3A6")
    Jump("loc_C72C")

    label("loc_C3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C3B4")
    Jump("loc_C72C")

    label("loc_C3B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C44B")

    ChrTalk(
        0x14,
        (
            "Even so, it was a\x01",
            "scary incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "It was sudden and I still don't\x01",
            "know what happened...\x01",
            "I wonder what could've been the cause.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C72C")

    label("loc_C44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C4FA")

    ChrTalk(
        0x14,
        (
            "I hurt my hips when I\x01",
            "was doing housework.\x01",
            "Really, I don't want to get older.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "You all too, be careful.\x01",
            "The 30 or 40 are immediately around the corner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C72C")

    label("loc_C4FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C508")
    Jump("loc_C72C")

    label("loc_C508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C57F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C523")
    Call(0, 24)
    Jump("loc_C57A")

    label("loc_C523")


    ChrTalk(
        0x14,
        (
            "Uuhn, my running nose\x01",
            "doesn't really stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Stay quiet until\x01",
            "your turn comes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C57A")

    Jump("loc_C72C")

    label("loc_C57F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C58D")
    Jump("loc_C72C")

    label("loc_C58D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C72C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C67D")

    ChrTalk(
        0x14,
        (
            "Lately, medicine explanations have\x01",
            "become more detailed than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "It's probably consideration so we\x01",
            "patients can feel at ease, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Honestly, those ingredients are\x01",
            "all Zemurian for an amateur.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_C72C")

    label("loc_C67D")


    ChrTalk(
        0x14,
        (
            "Lately, medicine explanations have\x01",
            "become more detailed than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I don't really understand what's inside, but...\x01",
            "Well, since I can be reassured, it's all right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C72C")

    TalkEnd(0xFE)
    Return()

    # Function_23_C2DB end

    def Function_24_C730(): pass

    label("Function_24_C730")


    ChrTalk(
        0x14,
        (
            "Uhhm, you still have a fever and\x01",
            "the running nose too doesn't stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Here, blow your nose in\x01",
            "mama's handkerchief.\x02",
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
        "...So much came out.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Return()

    # Function_24_C730 end

    def Function_25_C7DD(): pass

    label("Function_25_C7DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C87A")

    ChrTalk(
        0x15,
        (
            "At last I was able to come to\x01",
            "visit a hospitalised friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "He's probably feeling lonely too,\x01",
            "so I want to chat about many things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA60")

    label("loc_C87A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_C888")
    Jump("loc_CA60")

    label("loc_C888")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_C896")
    Jump("loc_CA60")

    label("loc_C896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C913")

    ChrTalk(
        0x15,
        (
            "My buddy too was caught\x01",
            "up in the raid incident and\x01",
            "was hospitalised...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "I hope he gets well quick...\x02",
    )

    CloseMessageWindow()
    Jump("loc_CA60")

    label("loc_C913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C921")
    Jump("loc_CA60")

    label("loc_C921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C92F")
    Jump("loc_CA60")

    label("loc_C92F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C9D8")

    ChrTalk(
        0x15,
        (
            "The say the initial medical examinations\x01",
            "have been postponed. It seems it'll take\x01",
            "some time until my turn comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "*haah*, hospitals are sluggish.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CA60")

    label("loc_C9D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_CA49")

    ChrTalk(
        0x15,
        "*grgrgrowl", my stomach aches...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I can only distract myself\x01",
            "thinking about the nurses...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA60")

    label("loc_CA49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_CA57")
    Jump("loc_CA60")

    label("loc_CA57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_CA60")

    label("loc_CA60")

    TalkEnd(0xFE)
    Return()

    # Function_25_C7DD end

    def Function_26_CA64(): pass

    label("Function_26_CA64")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CB1A")

    ChrTalk(
        0x16,
        (
            "Today I came to pick up my mother\x01",
            "who is leaving the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "It seems she couldn't exit the\x01",
            "hospital for a while, so I want\x01",
            "to take her back home quick.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE4C")

    label("loc_CB1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_CB28")
    Jump("loc_CE4C")

    label("loc_CB28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_CB36")
    Jump("loc_CE4C")

    label("loc_CB36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CB44")
    Jump("loc_CE4C")

    label("loc_CB44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CD03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC15")

    ChrTalk(
        0x16,
        (
            "I heard the rumors in the city...\x01",
            "They say that at the time of the derailment accident,\x01",
            "a mysterious giant monster appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "What if that could be the\x01",
            "incident's cause...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_CCFE")

    label("loc_CC15")


    ChrTalk(
        0x16,
        (
            "I heard the rumors in the city...\x01",
            "They say that at the time of the derailment accident,\x01",
            "a mysterious giant monster appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "...If something like that showed up,\x01",
            "it would be impossible for us\x01",
            "common people to deal with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCFE")

    Jump("loc_CE4C")

    label("loc_CD03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CD11")
    Jump("loc_CE4C")

    label("loc_CD11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CDE5")

    ChrTalk(
        0x16,
        (
            "Somehow it seems the doctors are\x01",
            "quarreling in front of the examination room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "If I look carefully, somehow even the\x01",
            "people of the hospital are all gloomy...\x01",
            "Could something have happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE4C")

    label("loc_CDE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_CDF3")
    Jump("loc_CE4C")

    label("loc_CDF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_CE43")

    ChrTalk(
        0x16,
        "There there, quiet down, ok?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Big sis will be\x01",
            "there too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE4C")

    label("loc_CE43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_CE4C")

    label("loc_CE4C")

    TalkEnd(0xFE)
    Return()

    # Function_26_CA64 end

    def Function_27_CE50(): pass

    label("Function_27_CE50")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CE7E")

    ChrTalk(
        0x17,
        (
            "I'm tired of\x01",
            "waitiiing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFB3")

    label("loc_CE7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_CE8C")
    Jump("loc_CFB3")

    label("loc_CE8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_CE9A")
    Jump("loc_CFB3")

    label("loc_CE9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CEE8")

    ChrTalk(
        0x17,
        "Aaah, so boring...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Why the turn doesn't come already!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CFB3")

    label("loc_CEE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CEF6")
    Jump("loc_CFB3")

    label("loc_CEF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CF04")
    Jump("loc_CFB3")

    label("loc_CF04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CF12")
    Jump("loc_CFB3")

    label("loc_CF12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_CF20")
    Jump("loc_CFB3")

    label("loc_CF20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_CF6D")

    ChrTalk(
        0x17,
        "Waaahn, injections are scaryyy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "I'll go back hooome!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CFB3")

    label("loc_CF6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_CFB3")

    ChrTalk(
        0x17,
        (
            "*yawn*...\x01",
            "I'm tired of waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Isn't my turn yet?\x02",
    )

    CloseMessageWindow()

    label("loc_CFB3")

    TalkEnd(0xFE)
    Return()

    # Function_27_CE50 end

    def Function_28_CFB7(): pass

    label("Function_28_CFB7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D00B")

    ChrTalk(
        0x18,
        (
            "*cough, cough*...\x01",
            "If it's a bitter medicine, I don't want it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D118")

    label("loc_D00B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_D019")
    Jump("loc_D118")

    label("loc_D019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_D027")
    Jump("loc_D118")

    label("loc_D027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D035")
    Jump("loc_D118")

    label("loc_D035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D043")
    Jump("loc_D118")

    label("loc_D043")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D0A3")

    ChrTalk(
        0x18,
        (
            "Today you see, I came\x01",
            "riding on the bus alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "Eheheh, I'm good, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_D118")

    label("loc_D0A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D0B1")
    Jump("loc_D118")

    label("loc_D0B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D101")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0CC")
    Call(0, 24)
    Jump("loc_D0FC")

    label("loc_D0CC")


    ChrTalk(
        0x18,
        (
            "*sniff*...\x01",
            "My nose doesn't stop running...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0FC")

    Jump("loc_D118")

    label("loc_D101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D10F")
    Jump("loc_D118")

    label("loc_D10F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D118")

    label("loc_D118")

    TalkEnd(0xFE)
    Return()

    # Function_28_CFB7 end

    def Function_29_D11C(): pass

    label("Function_29_D11C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D1AE")

    ChrTalk(
        0x19,
        (
            "The city...\x01",
            "The city was ablaze...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "What a scary scene it was...\x01",
            "It made me remember the disputes\x01",
            "of many tens of years ago.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1AE")

    TalkEnd(0xFE)
    Return()

    # Function_29_D11C end

    def Function_30_D1B2(): pass

    label("Function_30_D1B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D1FD")

    ChrTalk(
        0x1A,
        "U-Uuuh...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems she is having a nightmare.\x07\x02\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D1FD")

    TalkEnd(0xFE)
    Return()

    # Function_30_D1B2 end

    def Function_31_D201(): pass

    label("Function_31_D201")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D273")

    ChrTalk(
        0x1B,
        (
            "Uugh...in that raid incident\x01",
            "I broke both of my legs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Damn it...\x01",
            "Why did it happen to me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D273")

    TalkEnd(0xFE)
    Return()

    # Function_31_D201 end

    def Function_32_D277(): pass

    label("Function_32_D277")

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
            "I'll go deliver the medical\x01",
            "record to Professor Seiland.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_D277 end

    def Function_33_D308(): pass

    label("Function_33_D308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D337")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D337")
    Call(0, 48)
    Return()

    label("loc_D337")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D60F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D526")

    ChrTalk(
        0x1D,
        (
            "I heard a rumor...\x01",
            "It seems that Shizuku MacLaine's\x01",
            "eyes were completely healed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I should rejoice as her former\x01",
            "doctor in charge, however...\x01",
            "I have mixed feelings about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Considering this series of incidents,\x01",
            "I can say that some kind of mysterious\x01",
            "power has been used for her eyes too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "As a person who takes part in\x01",
            "medical care, falling behind to\x01",
            "such a thing is just a lot vexing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "...I'm sorry, forget it.\x01",
            "It's like a stupid obstinacy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_D60A")

    label("loc_D526")


    ChrTalk(
        0x1D,
        (
            "...I'm sorry, forget it.\x01",
            "It's like a stupid obstinacy of a person \x01",
            "who takes part in modern medical care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "The fact in itself that Shizuku MacLaine's \x01",
            "eyes were healed is something delightful.\x01",
            "I honestly wish her well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D60A")

    Jump("loc_DEC2")

    label("loc_D60F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_D61D")
    Jump("loc_DEC2")

    label("loc_D61D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_D62B")
    Jump("loc_DEC2")

    label("loc_D62B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_D639")
    Jump("loc_DEC2")

    label("loc_D639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D8E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D8E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D665")
    Call(0, 35)
    Jump("loc_D8DC")

    label("loc_D665")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D79C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D71B")

    ChrTalk(
        0x1D,
        (
            "For now, with these we'll\x01",
            "be able to deal well with\x01",
            "the raid incident patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I'll put to an efficient use the\x01",
            "medical goods you recovered.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_D797")

    label("loc_D71B")


    ChrTalk(
        0x1D,
        (
            "Well then...\x01",
            "It's time to operate the next patient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I'll put to an efficient use the\x01",
            "medical goods you recovered.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D797")

    Jump("loc_D8DC")

    label("loc_D79C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_D836")

    ChrTalk(
        0x1D,
        (
            "It really hurts that in this\x01",
            "situation medical goods\x01",
            "were stolen, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "We can't whine about it.\x01",
            "We have to devise something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D8DC")

    label("loc_D836")


    ChrTalk(
        0x1D,
        (
            "...It's difficult to overcome this situation\x01",
            "where we lack medical goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Just in case, I'll explain the\x01",
            "situation and make me send\x01",
            "some replacement goods.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8DC")

    Jump("loc_D8E1")

    label("loc_D8E1")

    Jump("loc_DEC2")

    label("loc_D8E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D9F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9AB")
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x1D,
        (
            "Lytton, I'll go do my\x01",
            "hospital rounds next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Due to this accident, there're many patients.\x01",
            "Don't relax just because\x01",
            "the surgeries are over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Y-Yes!!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x1, 6)
    Jump("loc_D9F4")

    label("loc_D9AB")


    ChrTalk(
        0x1D,
        (
            "Due to this accident, there're many patients.\x01",
            "Don't relax too much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9F4")

    Jump("loc_DEC2")

    label("loc_D9F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_DA07")
    Jump("loc_DEC2")

    label("loc_DA07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DA15")
    Jump("loc_DEC2")

    label("loc_DA15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_DA23")
    Jump("loc_DEC2")

    label("loc_DA23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_DEB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBAE")

    ChrTalk(
        0x1D,
        (
            "Albert...\x01",
            "It seems he intends to come here\x01",
            "after his inspection is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Now that tomorrow's conference\x01",
            "draws close, the necessity to come\x01",
            "here in person to inspect is low.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Oh boy...\x01",
            "That man too is always the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(A-Albert she says...\x01",
            "Is she addressing him informally?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F(Maybe they're acquaintances or something...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_DC27")

    label("loc_DBAE")


    ChrTalk(
        0x1D,
        (
            "Albert seems to intend \x01",
            "to come here after his \x01",
            "inspection is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Oh boy...\x01",
            "That man too is always the same.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_DEB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDC7")

    ChrTalk(
        0x1D,
        (
            "Since the cause of "Riboten Poisoning"\x01",
            "is a mushroom found abroad, it's hard\x01",
            "for medical cases to appear in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I too have thought about many possibilities,\x01",
            "but I can only say that Albert guessed right.\x01",
            "As expected, his knowledge is very deep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "This time I owe him one...\x01",
            "He's someone who governs Remiferia, even\x01",
            "if temporarily, but I shouldn't have expected less.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_DEB4")

    label("loc_DDC7")


    ChrTalk(
        0x1D,
        (
            "Albert guessed it right when he\x01",
            "said it was "Riboten Poisoning". \x01",
            "As expected, his knowledge is very deep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "This time I owe him one...\x01",
            "He's someone who governs Remiferia, even\x01",
            "if temporarily, but I shouldn't have expected less.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DEB4")

    Jump("loc_DEC2")

    label("loc_DEB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DEC2")

    label("loc_DEC2")

    TalkEnd(0xFE)
    Return()

    # Function_33_D308 end

    def Function_34_DEC6(): pass

    label("Function_34_DEC6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_DF9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DF9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DEF5")
    Call(0, 35)
    Jump("loc_DF99")

    label("loc_DEF5")


    ChrTalk(
        0x1E,
        (
            "We have an arrangement with\x01",
            ""Rhymes Shipping" to brings us the\x01",
            "medical goods delivered at the airport, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Uhhm, maybe there was\x01",
            "some kind of blunder?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF99")

    Jump("loc_DF9E")

    label("loc_DF9E")

    TalkEnd(0xFE)
    Return()

    # Function_34_DEC6 end

    def Function_35_DFA2(): pass

    label("Function_35_DFA2")

    OP_4B(0x1E, 0xFF)
    OP_4B(0x1D, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x1D,
        (
            "...They say the can't deliver the\x01",
            "medical goods from Remiferia yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "Yes. The packages scheduled arrival\x01",
            "has long passed, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder if there has been\x01",
            "some kind of trouble...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Hm, something could've happened\x01",
            "at the Remiferia airport.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1E, 0x10)
    SetScenarioFlags(0x18F, 0)
    OP_4C(0x1E, 0xFF)
    OP_4C(0x1D, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_35_DFA2 end

    def Function_36_E0C9(): pass

    label("Function_36_E0C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E0DE")
    Call(0, 37)
    Jump("loc_E186")

    label("loc_E0DE")


    ChrTalk(
        0x1F,
        (
            "Honestly, thinking about what they could say,\x01",
            "I was reluctant to come to the hospital...\x01",
            "Who could've thought about this result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "I owe everything to Amisaah.\x02",
    )

    CloseMessageWindow()

    label("loc_E186")

    TalkEnd(0xFE)
    Return()

    # Function_36_E0C9 end

    def Function_37_E18A(): pass

    label("Function_37_E18A")

    OP_4B(0x1F, 0xFF)
    OP_4B(0x20, 0xFF)

    ChrTalk(
        0xC,
        "Hm, this is surprising...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Mr. Quine, your condition\x01",
            "has improved since the time\x01",
            "when you were hospitalised.\x02",
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
            "Yes, although of course we need\x01",
            "to observe its progress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "However, at least it seems there's\x01",
            "no need to hospitalise you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x20,
        "Aren't you happy, grandpa?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "He says your health has improved!\x01",
            "And also that's ok to not put you in a hospital!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Y-Yeah...that's right.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1F, 0x10)
    ClearChrFlags(0x20, 0x10)
    SetScenarioFlags(0x2, 4)
    OP_4C(0x1F, 0xFF)
    OP_4C(0x20, 0xFF)
    Return()

    # Function_37_E18A end

    def Function_38_E39E(): pass

    label("Function_38_E39E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E43C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3BC")
    Call(0, 37)
    Jump("loc_E437")

    label("loc_E3BC")


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
            "Uh uh uh, I was right\x01",
            "in making you properly\x01",
            "take the medicines, eh♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E437")

    Jump("loc_E48B")

    label("loc_E43C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_E48B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E457")
    Call(0, 39)
    Jump("loc_E48B")

    label("loc_E457")


    ChrTalk(
        0x20,
        (
            "Today too I'll\x01",
            "bring the medicines\x01",
            "to grampa♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E48B")

    TalkEnd(0xFE)
    Return()

    # Function_38_E39E end

    def Function_39_E48F(): pass

    label("Function_39_E48F")

    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "Then, Amisaah. I've wrapped\x01",
            "the usual medicines for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Be careful and take them to him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Yes.\x01",
            "Thank you as always, doctor.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x20, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x2, 3)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_39_E48F end

    def Function_40_E530(): pass

    label("Function_40_E530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E55F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E55F")
    Call(0, 48)
    Return()

    label("loc_E55F")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_40_E530 end

    def Function_41_E566(): pass

    label("Function_41_E566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E585")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E585")
    Call(0, 48)
    Return()

    label("loc_E585")

    TalkBegin(0xFE)

    ChrTalk(
        0x22,
        (
            "I will wait for you to bring\x01",
            "the Naderia Mushroom.\x02\x03",
            "I am sure that you all and\x01",
            "Arios can accomplish this.\x01",
            "Please, I leave this to you.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_E566 end

    def Function_42_E618(): pass

    label("Function_42_E618")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E79C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E706")

    ChrTalk(
        0x24,
        (
            "The mushrooms I brought home\x01",
            "as souvenirs from abroad \x01",
            "tasted really great, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Who would've thought they were poisonous.\x01",
            "I was careless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Next time, I'll have to be\x01",
            "a little more careful...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E797")

    label("loc_E706")


    ChrTalk(
        0x24,
        (
            "The mushrooms I brought home\x01",
            "as souvenirs from abroad \x01",
            "tasted really great, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Next time, I'll have to be\x01",
            "a little more careful...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E797")

    Jump("loc_E828")

    label("loc_E79C")


    ChrTalk(
        0x24,
        (
            "U-Uuhg...\x01",
            "Somehow my stomach pain has become acute...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "As I thought, maybe what I ate\x01",
            "on the airship was not good...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        "Ughgh...\x02",
    )

    CloseMessageWindow()

    label("loc_E828")

    TalkEnd(0xFE)
    Return()

    # Function_42_E618 end

    def Function_43_E82C(): pass

    label("Function_43_E82C")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_43_E82C end

    def Function_44_E833(): pass

    label("Function_44_E833")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA8C")

    ChrTalk(
        0xFE,
        (
            "I'm helping to carry the patients who\x01",
            "couldn't come to the hospital regularly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because there're many as expected,\x01",
            "it seems I'll have to do many rounds\x01",
            "throughout the entire day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIt seems pretty tough...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FPlease, don't overdo it too much.\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Aaahn, to be said such \x01",
            "words from little Tio is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Her reactions are always cool, and yet...\x01",
            "Could she be one of those characters who're\x01",
            "always calm and composed...a "kｹdere"?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00211F(...She has gradually become\x01",
            "similar to Chief Roberts.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BB, 2)
    Jump("loc_EB94")

    label("loc_EA8C")


    ChrTalk(
        0xFE,
        (
            "Aaaalright... I got cheered by little Tio,\x01",
            "my energy jumped a hundred fold,\x01",
            "and I'm full of bravery!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Little Tio, let me give you a tight big\x01",
            "hug when everything's over, ok?㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F(...Even if everything's over, it\x01",
            "seems I won't be able to relax.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB94")

    TalkEnd(0xFE)
    Return()

    # Function_44_E833 end

    def Function_45_EB98(): pass

    label("Function_45_EB98")

    Sound(160, 0, 100, 0)
    Return()

    # Function_45_EB98 end

    def Function_46_EB9F(): pass

    label("Function_46_EB9F")

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
            "#11POh, Miss Noｱl.\x01",
            "And the SSS members too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHave you come to pay\x01",
            "a visit to Miss Fran?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#6PYes. Is it all right now?\x02",
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
            "#11P...Still, I am glad that your younger\x01",
            "sister has regained consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104F#6P...Yes.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ED89():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_ED89)
    WaitChrThread(0x109, 3)
    Sleep(150)

    ChrTalk(
        0x109,
        (
            "#10102F#11PLet's go.\x01",
            "It's the 301 room on 3F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PYeah, excuse us for disturbing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#6PExcuse us, Miss Sera.\x02",
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

    # Function_46_EB9F end

    def Function_47_EE74(): pass

    label("Function_47_EE74")

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
        "...Yes...yes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...Then, please.\x01\x02",
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
            "She said to come to her room\x01",
            "at the research laboratory now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        "#01309FThank you, Miss Sera.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FThank you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x101, 500)

    ChrTalk(
        0x26,
        (
            "#01300F...Then, everyone, my break\x01",
            "is about to end, so I will\x01",
            "excuse myself here.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F130():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F130)
    Sleep(50)

    def lambda_F140():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F140)
    Sleep(50)

    def lambda_F150():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F150)
    Sleep(50)

    def lambda_F160():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F160)
    Sleep(50)

    def lambda_F170():
        TurnDirection(0xFE, 0x26, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_F170)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x101,
        "#12P#00000FYeah, thanks for everything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10102FWe're in your debt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#01300FNo, you're welcome.\x02\x03",
            "#01309FThen, I think you will face many\x01",
            "hardships from now on, but...\x01",
            "Do your best, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00009FYeah, you too.\x02",
    )

    CloseMessageWindow()

    def lambda_F26C():
        OP_95(0xFE, 12030, 0, 10760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_F26C)
    Sleep(50)

    def lambda_F289():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F289)
    Sleep(50)

    def lambda_F299():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F299)
    WaitChrThread(0x26, 1)

    def lambda_F2AA():
        OP_97(0xFE, 0x0, 0x564, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_F2AA)
    Sleep(1000)

    def lambda_F2C7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_F2C7)
    WaitChrThread(0x26, 2)
    SetChrFlags(0x26, 0x80)
    OP_0D()
    OP_68(13870, 1000, 6330, 3000)
    OP_6F(0x1)

    ChrTalk(
        0x104,
        (
            "#12P#00310F......Khhh, you're always\x01",
            "the hateful guy, huh!\x02\x03",
            "#00309F"Do your best, Lloyd㈱"\x01",
            "...She said that, she said!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006FS-She didn't attach any\x01",
            "heart mark at all, right...?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F3BC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F3BC)
    Sleep(100)

    def lambda_F3CC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F3CC)
    Sleep(500)

    ChrTalk(
        0x105,
        (
            "#6P#10300FHu hu, you said it like that but\x01",
            "aren't you a little disappointed? Hm?\x02\x03",
            "It also seems I couldn't see the rumored\x01",
            "passionate hug too, this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FYes, now that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FHuh, did such a thing...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAh, jeez!\x01",
            "Enough already, let's go\x01",
            "meet the professor, now!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x3E8)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00001FThe research building is on the hospital rooftop\x01",
            "and the pharmacology laboratory is on its 4F.\x01",
            "Come now, let's go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309F(Oh boy, he tends to end up\x01",
            "bein' manipulated, huh.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302F(Hu hu, that's exactly why\x01",
            "it's worth teasing him.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00003F...I can hear you!\x02",
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

    # Function_47_EE74 end

    def Function_48_F6A1(): pass

    label("Function_48_F6A1")

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
        "Hm...seems we have guests.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10067")

    ChrTalk(
        0x22,
        "Oh, you are...\x02",
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
            "#00005FH-His Grace Archduke Albert from\x01",
            "the Principality of Remiferia...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FAnd Mr. Arios too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#01405FHm, what a coincidence.\x02\x03",
            "#01400FYour Grace, they are the persons from the\x01",
            ""Special Support Section" I told you about before.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x22, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x22,
        "Ooh, are they?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "...Nice to meet you, Support Section ladies and gentlemen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "My name is Albert von Bartholomeus.\x01",
            "I serve as Remiferia's Head of State.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Please do your very best for\x01",
            "Crossbell's sake in the future too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FI-It is nice making your acquaintance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Hu hu, I heard about\x01",
            "you all from Arios.\x01",
            "I really wanted to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Also, Elie, it's been a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, yes it has.\x01",
            "You look well too, Your Grace...\x02\x03",
            "#00103FHowever, I didn't know\x01",
            "you had come to\x01",
            "visit the hospital.\x02\x03",
            "#00105FDid you come to\x01",
            "inspect it today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Hm, the Principality of Remiferia is\x01",
            "one of this hospital's sponsors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Also, I really wanted to see Seiland\x01",
            "who has been appointed here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x22, 500)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "#01403FIn regard to that,  I personally\x01",
            "was allowed to escort him a\x01",
            "little longer.\x02\x03",
            "#01400FI thought it wasn't good to come\x01",
            "here for just the driver and I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Hu hu, it's just because\x01",
            "I have confidence in\x01",
            "you, Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Also, I couldn't have brought with me a\x01",
            "group of guards in my inspection, or else \x01",
            "I would've disturbed the hospital work.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1D, 0x0)
    Sleep(300)

    ChrTalk(
        0x1D,
        "Honestly, what troublesome things you do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Even the inspection, it's not like\x01",
            "you had to come to do it now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "You should've just focused on the\x01",
            "Trade Conference this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Shouldn't you be a little more\x01",
            "self-conscious as a state guest?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "Hah hah hah, harsh as\x01",
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
            "#00003F(Archduke Albert...\x01",
            "He seems to really know many people.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F(Yes. Miss Elie, Mr. Arios...\x01",
            "And Professor Seiland too, he seems\x01",
            "to have known them since some time ago.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Hu hu, even if he's a country VIP,\x01",
            "I'm surprised by his way of talking.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1042B")

    label("loc_10067")


    ChrTalk(
        0x22,
        "Oh, you're the Special Support Section.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYour Grace Archduke Albert,\x01",
            "Mr. Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FSo after seeing Shizuku\x01",
            "you had come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#01400FYeah, I just came to greet\x01",
            "Professor Seiland.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Hu hu, I really wanted to see Seiland\x01",
            "who has been appointed here.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1D, 0x0)
    Sleep(300)

    ChrTalk(
        0x1D,
        "Honestly, what troublesome things you do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Even the inspection, it's not like\x01",
            "you had to come to do it now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "You should've just focused on the\x01",
            "Trade Conference this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Shouldn't you be a little more\x01",
            "self-conscious as a state guest?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "Hah hah hah, harsh as\x01",
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
            "#00003F(Archduke Albert...\x01",
            "He seems to really know many people.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F(Yes, it seems he's acquainted\x01",
            "with Professor Seiland too.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Hu hu, even if he's a country VIP,\x01",
            "I'm surprised by his way of talking.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1042B")

    OP_82(0xC8, 0x0, 0xBB8, 0x320)
    SetMessageWindowPos(300, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5SD-Doctor!\x07\x02\x02",
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

    def lambda_10530():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10530)
    Sleep(50)

    def lambda_10540():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10540)
    Sleep(50)

    def lambda_10550():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10550)
    Sleep(50)

    def lambda_10560():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10560)
    Sleep(50)

    def lambda_10570():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10570)
    Sleep(50)

    def lambda_10580():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_10580)
    Sleep(50)

    def lambda_10590():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_10590)
    OP_95(0xC, 53440, 0, 52820, 4000, 0x0)
    OP_95(0xC, 54100, 0, 55910, 4000, 0x0)
    OP_93(0xC, 0x13B, 0x0)
    OP_6F(0x1)

    ChrTalk(
        0x1D,
        "What's with the noise, Lytton?\x02",
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
            "A patient who was in the lobby\x01",
            "has just collapsed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "It's a serious condition, he lost consciousness!\x02",
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
        "Hm, that sounds bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Bring him here now.\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Y-Yes!\x02",
    )

    CloseMessageWindow()
    OP_64(0xC)
    OP_68(50330, 1000, 58210, 3000)
    OP_95(0xC, 53440, 0, 52820, 4000, 0x0)
    OP_95(0xC, 49800, 0, 51590, 4000, 0x0)
    OP_95(0xC, 49560, 0, 49150, 4000, 0x0)
    OP_6F(0x1)
    SetChrSubChip(0x1D, 0x1)

    def lambda_10804():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10804)
    Sleep(50)

    def lambda_10814():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10814)
    Sleep(50)

    def lambda_10824():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10824)
    Sleep(50)

    def lambda_10834():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10834)
    Sleep(50)

    def lambda_10844():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10844)
    Sleep(50)

    def lambda_10854():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_10854)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00000FMr. Arios, we...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#01400FYeah, it seems we would be in the way for\x01",
            "the examination, so it's better to leave.\x02",
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
            "In case, you could\x01",
            "be of help too.\x02",
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
        "#00005FHow is...his condition?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301FHe looks to be sufferin' a lot...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "...Looking blue.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "I tried examining many things and although\x01",
            "there's no doubt that it's an internal medicine\x01",
            "case, I couldn't determine the cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "If I ascertained the disease name,\x01",
            "I could prepare a medicine, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "At present, it's quite hard to say if the\x01",
            "patient will hold out until then, or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FI-Is it so serious...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "W-What should we...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "──Hm.\x01",
            "Can I say something?\x02",
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

    def lambda_10D05():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10D05)
    Sleep(50)

    def lambda_10D15():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10D15)
    Sleep(50)

    def lambda_10D25():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10D25)
    Sleep(50)

    def lambda_10D35():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10D35)
    Sleep(50)

    def lambda_10D45():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10D45)
    Sleep(50)

    def lambda_10D55():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_10D55)
    Sleep(50)

    def lambda_10D65():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_10D65)
    Sleep(50)

    def lambda_10D75():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_10D75)
    Sleep(300)

    ChrTalk(
        0x21,
        "#01405FYour Grace, is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Seiland, from the outset\x01",
            "I was thinking...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Could these symptoms \x01",
            "be "Riboten Poisoning"?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1D,
        "...I see, "Riboten Poisoning".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "There're no medical cases in Crossbell,\x01",
            "but it seems very likely to be that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F"Riboten Poisoning"?\x01",
            "It's a name I've never heard.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "It's a condition caused by a rare\x01",
            "poisonous mushroom native of the\x01",
            "continent's borderlands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "That poison is quite difficult to\x01",
            "detect with the usual methods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "However, isn't this case\x01",
            "exactly like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "Yeah, no doubt about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "He could've ingested something \x01",
            "he brought with him from abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FThe professor's black seal, then.\x02\x03",
            "#00300FYou're amazin', Mr. Archduke.\x01",
            "You saw through such a thing\x01",
            "at the first try.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Ha ha, it's nothing much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Still, we can't relax yet.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "Seiland, you have a specific\x01",
            "medicine for Riboten Poisoning \x01",
            "emergencies, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "...I just ran out of some\x01",
            "of the ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "If I had them, I could mix\x01",
            "the medicine immediately....\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10103FThat doesn't sound good...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Hm...in that case...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        "Arios, and SSS ladies and gentlemen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "I want to make an urgent request to\x01",
            "you to supply the medicine ingredients.\x01",
            "Can you accept it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#01400FSir...as you wish.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FIt's an emergency situation, so\x01",
            "of course we're accepting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FThen, what should\x01",
            "we get I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Hm, I'll explain the plan now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "The antidote for "Riboten Poisoning"\x01",
            "is mixed with two main ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "One is a medical plant called "Ante Grass"\x01",
            "found in the mountain areas of Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "And the other one is a mushroom\x01",
            "called "Almashroom" found in\x01",
            "St. Ursula wooded areas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F"Ante Grass" and "Almashroom"...\x01",
            "I feel like I saw them during\x01",
            "CGF survival training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Of these, I want you Arios to\x01",
            "head to retrieve the "Ante Grass".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "If we're searching for a medical plant\x01",
            "in a mountain area untouched by man,\x01",
            "you, who're a Bracer, should be suited.\x02",
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
        "Then, for the "Almashroom"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "I want to search for it myself and have\x01",
            "the Special Support Section accompany me.\x02",
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
        "#00005FEeh...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FTogether with Your Grace?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Hm, that's because...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "In the places where the "Almashroom"\x01",
            "grows, many other mushrooms with a\x01",
            "similar shape inhabit it too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Because they're very easy to mistake, it should be better\x01",
            "if you were accompanied by someone who knows about them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHm, it's true that looking for\x01",
            "it together would be better.\x02\x03",
            "#10300FIf you're not uncomfortable\x01",
            "with us taking over Arios'\x01",
            "guard duty, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FIndeed, the responsibility is heavy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#01401FI too can't help but being a little worried myself\x01",
            "about you taking on His Grace guard duty...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Prioritizing an immediate cure\x01",
            "for this patient there're probably\x01",
            "no other ways than this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "And regarding the Support Section's ladies and\x01",
            "gentlemen, didn't you recognise their skills too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "You don't have to worry, because\x01",
            "I'll be extra careful too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Also, if you came\x01",
            "back quick, there would\x01",
            "be nothing to worry, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#01404FHmph...understood.\x02\x03",
            "#01400FThen, I'll go immediately\x01",
            "to the Mainz mountain area.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "#01400FI leave His Grace escort to you, \x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FWe'll absolutely fulfill our guard duty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Hu hu, then, let's head to the\x01",
            "byroad wooded area too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x22, 0x1D, 500)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "Seiland, Lytton, keep monitoring\x01",
            "the patient's progress and ready\x01",
            "preparations for mixing the medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        "Hm, all right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "Everyone from the SSS too,\x01",
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
            "Thus, Lloyd and the others accepted\x01",
            "Archduke Albert's urgent request...\x07\x00\x02",
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
            "They splitted with Arios into two groups and\x01",
            "headed to procure the medicine ingredients.\x07\x00\x02",
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
            "Quest [Antidote Ingredients Supply]\x07\x00",
            " started!\x02",
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

    # Function_48_F6A1 end

    def Function_49_11D91(): pass

    label("Function_49_11D91")

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
            "#1PThe mushrooms I brought home\x01",
            "as souvenirs from abroad \x01",
            "tasted really great, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#1P*sigh*, who could've thought they were\x01",
            "poisonous mushrooms. I was careless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Although tasty when eaten, those\x01",
            "mushrooms have dangerous properties\x01",
            "which cause "Riboten Poisoning".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Don't eat such things\x01",
            "easily next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Also, although your life is not in peril,\x01",
            "I intend to hospitalise you in the ward\x01",
            "inside the research building for some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#1PI-I understand.\x01",
            "It would really be scary if\x01",
            "there were after-effects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#1PStill, thanks to you I feel considerably better.\x01",
            "Thank you very much, doctors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you want to thank someone, please\x01",
            "say those words to His Grace Archduke\x01",
            "Albert, Mr. Arios and the SSS people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "They're none other those who\x01",
            "brought the medicine ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#1POh...I-I see.\x01",
            "Thank you very much to you too, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#1PTo think I was saved by\x01",
            "His Grace Archduke Albert...\x01",
            "How awesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "No no, after all, what I did was\x01",
            "only confirming the mushroom.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_122F5():
        TurnDirection(0x22, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_122F5)

    ChrTalk(
        0x22,
        (
            "As you can expect, the merit goes to\x01",
            "Arios and the SSS ladies and gentlemen.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0x0)

    def lambda_12358():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_12358)
    Sleep(50)

    def lambda_12368():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12368)

    def lambda_12375():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12375)
    Sleep(50)

    def lambda_12385():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12385)

    def lambda_12392():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_12392)
    Sleep(50)

    def lambda_123A2():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_123A2)
    Sleep(50)

    def lambda_123B2():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_123B2)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "#01402FYou're too modest...\x02\x03",
            "#01403FI heard you studied with\x01",
            "Doctor Seiland and took the\x01",
            "medical license, Your Grace.\x02\x03",
            "#01400FI think you can evenly compare in every\x01",
            "respect like experience, skills and so on\x01",
            "with a doctor who serves on the front line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FEeh...is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FShould I say that's to be expected from the Archduke\x01",
            "of the medical care advanced country of Remiferia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Ha ha, it may appear like that, but I'm only studious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "When Seiland was in Remiferia, she often\x01",
            "allowed me to study surgeries by observation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "The knowledge I acquired like that has\x01",
            "only been useful by chance this time...\x01",
            "Being told those things embarrass me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "However, regarding this matter, \x01",
            "I did nothing more than butt in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Cooperation among Arios, the SSS\x01",
            "ladies and gentlemen and the hospital\x01",
            "staff lead to a prompt treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Hm, it was really a meaningful inspection.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Oh boy...\x01",
            "Always the argumentative one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "In any case, your inspection\x01",
            "is over with this, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Shouldn't it be better for you to\x01",
            "go back and start preparing for\x01",
            "tomorrow's Trade Conference?\x02",
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
            "Hah hah hah, you really are harsh.\x01",
            "However, it's true that what you say is always rational.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Then, we will excuse us now.\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Arios, can I count on you to\x01",
            "escort me on the way back too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#01400FYes, it goes without saying.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "#01400F...Then, Special Support Section.\x02\x03",
            "#01403FDo not let your guard down until\x01",
            "tomorrow's Trade Conference.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0x1)

    ChrTalk(
        0x101,
        (
            "#00000FAh...yes.\x01",
            "We'll bear it in mind.\x02",
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
            "Ladies and gentlemen, stay focused\x01",
            "on your job even more from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "I'll cheer for you behind the scenes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, thank you very much.\x02",
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
            "Quest [Antidote Ingredients Supply]\x07\x00",
            " completed!\x02",
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

    # Function_49_11D91 end

    def Function_50_12C3A(): pass

    label("Function_50_12C3A")

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
            "The Special Support Section...\x01",
            "Welcome to St. Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What business do\x01",
            "you have today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUhhm, we came because\x01",
            "we wanted to ask you\x01",
            "something...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd asked about the package\x01",
            "that was misdelivered.\x07\x02\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Ah...so that's what\x01",
            "that package was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Head Nurse Martha was making\x01",
            "a noise thinking if it hadn't been a\x01",
            "purchase order mistake from a nurse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FA purchase order...mistake?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, something like that\x01",
            "happened sometimes before...\x02",
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
            "#10100FSo, is the package at\x01",
            "the nurse center now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yes, that is the case.\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Please try visiting it at 2F.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FThen, let's do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FI'd be sorry if someone got scolded\x01",
            "due to some false accusations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FY-You're right...\x01",
            "Let's go now.\x02",
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

    # Function_50_12C3A end

    def Function_51_13059(): pass

    label("Function_51_13059")

    Return()

    # Function_51_13059 end

    def Function_52_1305A(): pass

    label("Function_52_1305A")

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
            "When I received the call from\x01",
            "Mr. Ricardo from the airport I was shocked...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I would've never thought to hear he\x01",
            "couldn't deliver the medical goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "There sure are some bad guys out there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, I am really glad the\x01",
            "medical goods were delivered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "For now, with these we'll\x01",
            "be able to deal well with\x01",
            "the raid incident patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "We've been helped by you.\x01",
            "Let me thank you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FNo, we just need\x01",
            "what we had to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FWe couldn't forgive\x01",
            "a cowardly bastard\x01",
            "like a looter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FWell, this time we were\x01",
            "helped by that armor, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        ""Armor"...what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FE-Eehm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...It is something among us,\x01",
            "please do not mind it too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThen, please consult with us whenever\x01",
            "something happens again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes...\x01",
            "Thank you very much.\x02",
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
            "Quest [Medical Supplies Investigation]\x07\x00",
            " completed!\x02",
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

    # Function_52_1305A end

    def Function_53_135F8(): pass

    label("Function_53_135F8")

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
            "When I received the call from\x01",
            "Mr. Ricardo from the airport I was shocked...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I would've never thought to hear he\x01",
            "couldn't deliver the medical goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "There sure are some bad guys out there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWe're terribly sorry to not have\x01",
            "been able to accomplish your request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FWe would've liked to catch\x01",
            "him at all cost, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Me too, if only I had\x01",
            "gone to get the package\x01",
            "faster, something like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No, it's not your fault, everyone...\x01",
            "Please, do not feel depressed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At any rate, we'll try\x01",
            "to do something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Nothing can't be done anymore\x01",
            "about the stolen goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I must quickly dispatch for\x01",
            "additional goods to be sent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "Until then, we'll only have to\x01",
            "keep coming up with something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI'm sorry...\x01",
            "We leave the rest to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "(*sigh*, I guess my old man is\x01",
            "going to sock me a good one...)\x02",
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
            "Quest [Medical Supplies Investigation]\x07\x00",
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

    # Function_53_135F8 end

    def Function_54_13B85(): pass

    label("Function_54_13B85")

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
            "※Those entering the room, please perform\x01",
            "sterilization treatment above level 2.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_54_13B85 end

    def Function_55_13C46(): pass

    label("Function_55_13C46")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's go to the reception first.\x01",
            "We'll visit her room later.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 59460, 0, 3330, 225)
    EventEnd(0x4)
    Return()

    # Function_55_13C46 end

    def Function_56_13CA6(): pass

    label("Function_56_13CA6")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's go to the reception first.\x01",
            "We'll visit her room later.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11970, 0, 10190, 135)
    EventEnd(0x4)
    Return()

    # Function_56_13CA6 end

    def Function_57_13D06(): pass

    label("Function_57_13D06")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FFran's room is the 301, right?\x01",
            "Let's go see how she's doing.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 1120, 50, -440, 89)
    EventEnd(0x4)
    Return()

    # Function_57_13D06 end

    SaveToFile()

Try(main)
