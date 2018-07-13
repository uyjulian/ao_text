from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0000.bin",                # FileName
        "c0000",                    # MapName
        "c0000",                    # Location
        0x0002,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("c0000", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 2, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0000",                  # 0
        "Reed",                   # 1
        "Billy",                  # 2
        "Claris",                 # 3
        "Tourist",                # 4
        "Tourist",                # 5
        "Tourist",                # 6
        "Tourist",                # 7
        "Tourist",                # 8
        "Tourist",                # 9
        "Boy",                    # 10
        "Girl",                   # 11
        "Policeman",              # 12
        "State Guard Soldier",    # 13
        "Marcy",                  # 14
        "Sepia",                  # 15
        "Oonagh",                 # 16
        "車",                     # 17
        "State Guard Soldier",    # 18
        "State Guard Soldier",    # 19
        "Policeman",              # 20
        "Policeman",              # 21
        "Policeman",              # 22
        "Policeman",              # 23
        "Policeman",              # 24
        "Policeman",              # 25
        "列車",                   # 26
        "SE制御",                 # 27
        "Central Square",         # 28
        "West Street",            # 29
        "Governmental District",  # 30
        "Residential Street",     # 31
        "Entertainment District", # 32
        "East Street",            # 33
        "Downtown",               # 34
        "Waterfront Area",        # 35
        "IBC",                    # 36
        "Station Street",         # 37
        "Back Street",            # 38
        "St. Ursula Byroad",      # 39
        "East Crossbell Highway", # 40
        "West Crossbell HIghway", # 41
        "Mainz Mountain Road",    # 42
        "Orchis Tower",           # 43
    ))

    AddCharChip((
        "chr/ch20400.itc",                   # 00
        "chr/ch23600.itc",                   # 01
        "chr/ch21600.itc",                   # 02
        "chr/ch23300.itc",                   # 03
        "chr/ch20200.itc",                   # 04
        "chr/ch44000.itc",                   # 05
        "chr/ch44100.itc",                   # 06
        "chr/ch34300.itc",                   # 07
        "chr/ch34200.itc",                   # 08
        "chr/ch24700.itc",                   # 09
        "chr/ch10400.itc",                   # 0A
        "chr/ch48900.itc",                   # 0B
        "chr/ch30000.itc",                   # 0C
        "chr/ch21800.itc",                   # 0D
        "chr/ch33200.itc",                   # 0E
        "chr/ch22300.itc",                   # 0F
        "chr/ch41500.itc",                   # 10
    ))

    DeclNpc(4294965466, 0,       13000,   180,  261,  0x0, 0,   0,   0,   0,   1,   0,   5,   255,  0)
    DeclNpc(1490,    0,       4294956557, 180,  261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(3660,    29,      4294910697, 90,   389,  0x0, 0,   10,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4880,    0,       2930,    35,   389,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(5880,    0,       2930,    35,   389,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4880,    0,       2930,    35,   389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(5880,    0,       2930,    35,   389,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4880,    0,       2930,    35,   389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(5880,    0,       2930,    35,   389,  0x0, 0,   7,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(6880,    0,       2930,    35,   389,  0x0, 0,   8,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(6880,    0,       2930,    35,   389,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4000,    0,       4294960296, 270,  389,  0x0, 0,   12,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(6070,    0,       319,     270,  389,  0x0, 0,   16,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(5150,    0,       4294966076, 90,   389,  0x0, 0,   13,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4010,    0,       4294966796, 90,   389,  0x0, 0,   14,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(3809,    0,       4294965796, 90,   389,  0x0, 0,   15,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 35,  8.5,                   -2.0,                  -0.5,                  16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -4.25,                 0.5,                   0.10000000149011612,   1.0])

    DeclActor(9500,    360,     4294965296, 2000,    10000,   1360,    4294965296, 0x007C, 0,  32, 0x0000)
    DeclActor(4294944996, 4294962296, 20700,   2000,    4294945346, 4294963296, 21360,   0x007C, 0,  37, 0x0000)

    PlaceName(-9.25, 0.0, 67.0, 0x0000, 0x0000, "Central Square")
    PlaceName(-75.0, 0.0, 71.5, 0x0000, 0x0000, "West Street")
    PlaceName(17.75, 0.0, 156.0, 0x0000, 0x0000, "Governmental District")
    PlaceName(-136.0, 0.0, 146.0, 0x0000, 0x0000, "Residential Street")
    PlaceName(-63.0, 0.0, 138.0, 0x0000, 0x0000, "Entertainment District")
    PlaceName(72.0, 0.0, 44.0, 0x0000, 0x0000, "East Street")
    PlaceName(107.5, 0.0, -11.0, 0x0000, 0x0000, "Downtown")
    PlaceName(100.0, 0.0, 110.0, 0x0000, 0x0000, "Waterfront Area")
    PlaceName(74.0, 0.0, 204.0, 0x0000, 0x0000, "IBC")
    PlaceName(2.0, 0.0, -2.0, 0x0000, 0x0000, "Station Street")
    PlaceName(-45.0, 0.0, 102.0, 0x0000, 0x0000, "Back Street")
    PlaceName(-1.0, 0.0, -33.0, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(126.0, 0.0, 58.0, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-126.0, 0.0, 70.0, 0x0000, 0x0000, "West Crossbell HIghway")
    PlaceName(-120.0, 0.0, 170.0, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(11.0, 0.0, 286.0, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(-31.25, 0.0, 53.0, 0x0000, 0x0051, "")
    PlaceName(22.5, 0.0, 79.0, 0x0000, 0x0054, "")
    PlaceName(-6.75, 0.0, 45.0, 0x0000, 0x0057, "")
    PlaceName(-32.0, 0.0, 82.0, 0x0000, 0x0053, "")
    PlaceName(-11.5, 0.0, 106.0, 0x0000, 0x0053, "")
    PlaceName(-62.25, 0.0, 77.0, 0x0000, 0x0053, "")
    PlaceName(-72.0, 0.0, 98.0, 0x0000, 0x0053, "")
    PlaceName(-48.0, 0.0, 130.0, 0x0000, 0x0052, "")
    PlaceName(-43.25, 0.0, 117.0, 0x0000, 0x0053, "")
    PlaceName(-34.5, 0.0, 108.5, 0x0000, 0x0053, "")
    PlaceName(-6.0, 0.0, 179.5, 0x0000, 0x0051, "")
    PlaceName(106.0, 0.0, 44.0, 0x0000, 0x0052, "")
    PlaceName(89.0, 0.0, -46.5, 0x0000, 0x0053, "")
    PlaceName(76.0, 0.0, -28.0, 0x0000, 0x0053, "")

    ChipFrameInfo(2132, 0)                                       # 0

    ScpFunction((
        "Function_0_854",          # 00, 0
        "Function_1_904",          # 01, 1
        "Function_2_957",          # 02, 2
        "Function_3_990",          # 03, 3
        "Function_4_ED7",          # 04, 4
        "Function_5_138B",         # 05, 5
        "Function_6_2A6C",         # 06, 6
        "Function_7_3376",         # 07, 7
        "Function_8_35C5",         # 08, 8
        "Function_9_387A",         # 09, 9
        "Function_10_3A25",        # 0A, 10
        "Function_11_3C4C",        # 0B, 11
        "Function_12_3DEF",        # 0C, 12
        "Function_13_3F95",        # 0D, 13
        "Function_14_40C5",        # 0E, 14
        "Function_15_4292",        # 0F, 15
        "Function_16_43D5",        # 10, 16
        "Function_17_4646",        # 11, 17
        "Function_18_4729",        # 12, 18
        "Function_19_476C",        # 13, 19
        "Function_20_47D9",        # 14, 20
        "Function_21_48C8",        # 15, 21
        "Function_22_4C1C",        # 16, 22
        "Function_23_4C81",        # 17, 23
        "Function_24_4CC2",        # 18, 24
        "Function_25_518D",        # 19, 25
        "Function_26_5869",        # 1A, 26
        "Function_27_587B",        # 1B, 27
        "Function_28_5890",        # 1C, 28
        "Function_29_58A5",        # 1D, 29
        "Function_30_58B0",        # 1E, 30
        "Function_31_58BB",        # 1F, 31
        "Function_32_58CD",        # 20, 32
        "Function_33_5CE6",        # 21, 33
        "Function_34_5D77",        # 22, 34
        "Function_35_5D8D",        # 23, 35
        "Function_36_6013",        # 24, 36
        "Function_37_63C3",        # 25, 37
    ))


    def Function_0_854(): pass

    label("Function_0_854")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_88C"),
        (1, "loc_898"),
        (2, "loc_8A4"),
        (3, "loc_8B0"),
        (4, "loc_8BC"),
        (5, "loc_8C8"),
        (6, "loc_8D4"),
        (SWITCH_DEFAULT, "loc_8E0"),
    )


    label("loc_88C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_898")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_8EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_903")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8EC")

    label("loc_903")

    Return()

    # Function_0_854 end

    def Function_1_904(): pass

    label("Function_1_904")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_956")
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -1830, 0, -9000, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -1830, 0, 13000, 2000, 0x0)
    Sleep(300)
    Jump("Function_1_904")

    label("loc_956")

    Return()

    # Function_1_904 end

    def Function_2_957(): pass

    label("Function_2_957")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_98F")
    OP_95(0xFE, -1830, 0, -23430, 2000, 0x0)
    Sleep(800)
    SetChrPos(0xFE, -1830, 0, 25870, 180)
    Jump("Function_2_957")

    label("loc_98F")

    Return()

    # Function_2_957 end

    def Function_3_990(): pass

    label("Function_3_990")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3F")
    SetChrPos(0x0, 0, 0, 21840, 180)
    SetChrPos(0x1, 0, 0, 21840, 180)
    SetChrPos(0x2, 0, 0, 21840, 180)
    SetChrPos(0x3, 0, 0, 21840, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A17")
    SetChrPos(0x4, 0, 0, 21840, 180)
    SetChrPos(0x5, 0, 0, 21840, 180)
    Jump("loc_A36")

    label("loc_A17")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A36")
    SetChrPos(0x4, 0, 0, 21840, 180)

    label("loc_A36")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A3F")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A56")
    Jump("loc_E55")

    label("loc_A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_A6E")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_E55")

    label("loc_A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A86")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_E55")

    label("loc_A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B5B")
    SetChrPos(0x9, 2730, 0, -9140, 45)
    SetChrPos(0x8, -3650, 0, -1670, 270)
    BeginChrThread(0x8, 0, 0, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 6010, 0, -4070, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 3930, 0, 510, 135)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3230, 0, 1580, 135)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1830, 0, -4530, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 1830, 0, -6290, 360)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 170, 0, -5890, 90)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 2890, 0, -2500, 90)
    Jump("loc_E55")

    label("loc_B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BB9")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 2050, 0, 8850, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_END)), "loc_B99")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2840, 0, -530, 270)

    label("loc_B99")

    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2490, 0, 2350, 0)
    SetChrFlags(0x9, 0x80)
    Jump("loc_E55")

    label("loc_BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BF3")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 4720, 0, 2440, 270)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 3740, 0, 2940, 90)
    Jump("loc_E55")

    label("loc_BF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C21")
    SetChrChipByIndex(0x8, 0xB)
    SetChrPos(0x8, -3650, 0, -1670, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrFlags(0x9, 0x80)
    Jump("loc_E55")

    label("loc_C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C85")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 2050, 0, 8850, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 4720, 0, 2440, 270)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 3740, 0, 2940, 90)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_E55")

    label("loc_C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CF1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA0")
    SetChrFlags(0x9, 0x80)

    label("loc_CA0")

    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 2050, 0, 8850, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 4720, 0, 2440, 270)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 3740, 0, 2940, 90)
    SetChrFlags(0x12, 0x10)
    Jump("loc_E55")

    label("loc_CF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D2B")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 2490, 0, 2350, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2050, 0, 8850, 270)
    Jump("loc_E55")

    label("loc_D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D6A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 2490, 0, 2350, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 1490, 0, 2550, 0)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_E55")

    label("loc_D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_DA9")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2490, 0, 2350, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 1490, 0, 2550, 0)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_E55")

    label("loc_DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DED")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 2490, 0, 2350, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 1490, 0, 2550, 0)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_E55")

    label("loc_DED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_E1B")
    SetChrChipByIndex(0x8, 0xB)
    SetChrPos(0x8, -3650, 0, -1670, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrFlags(0x9, 0x80)
    Jump("loc_E55")

    label("loc_E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_E55")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 2490, 0, 2350, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 1490, 0, 2550, 0)
    SetChrFlags(0x11, 0x10)

    label("loc_E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E6D")
    ClearMapFlags(0x2000)
    Jump("loc_E74")

    label("loc_E6D")

    SetMapFlags(0x2000)
    OP_E2(0x1)

    label("loc_E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E88")
    ClearScenarioFlags(0x22, 0)
    Event(0, 21)
    Jump("loc_EAB")

    label("loc_E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_E9C")
    ClearScenarioFlags(0x22, 1)
    Event(0, 24)
    Jump("loc_EAB")

    label("loc_E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_EAB")
    ClearScenarioFlags(0x22, 3)
    Event(0, 25)

    label("loc_EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ED6")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_ED6")

    Return()

    # Function_3_990 end

    def Function_4_ED7(): pass

    label("Function_4_ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F8C")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x6E, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_F8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_102C")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x6E, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_102C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_107F")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x28, 0x78, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_107F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C8")
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    Jump("loc_10FE")

    label("loc_10C8")

    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)

    label("loc_10FE")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_111A")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_111A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1146")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1146")
    OP_1B(0x3, 0x0, 0x22)

    label("loc_1146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_115E")
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_11C1")

    label("loc_115E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_116C")
    Jump("loc_11C1")

    label("loc_116C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_117F")
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_11C1")

    label("loc_117F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_118D")
    Jump("loc_11C1")

    label("loc_118D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_11A0")
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_11C1")

    label("loc_11A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_11B3")
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_11C1")

    label("loc_11B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_11C1")
    ModifyEventFlags(0, 0, 0x80)

    label("loc_11C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11D4")
    OP_1B(0x3, 0x0, 0x24)

    label("loc_11D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11E7")
    OP_1B(0x3, 0x0, 0x24)

    label("loc_11E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11FA")
    OP_1B(0x3, 0x0, 0x24)

    label("loc_11FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_120D")
    OP_1B(0x3, 0x0, 0x24)

    label("loc_120D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1220")
    OP_1B(0x3, 0x0, 0x24)

    label("loc_1220")

    ClearMapObjFlags(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_124D")
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    SetMapObjFlags(0x11, 0x1000)
    Jump("loc_1384")

    label("loc_124D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_125B")
    Jump("loc_1384")

    label("loc_125B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1269")
    Jump("loc_1384")

    label("loc_1269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1277")
    Jump("loc_1384")

    label("loc_1277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_129E")
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    SetMapObjFlags(0x11, 0x1000)
    Jump("loc_1384")

    label("loc_129E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_12AC")
    Jump("loc_1384")

    label("loc_12AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_12D3")
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    SetMapObjFlags(0x11, 0x1000)
    Jump("loc_1384")

    label("loc_12D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1306")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1301")
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    SetMapObjFlags(0x11, 0x1000)

    label("loc_1301")

    Jump("loc_1384")

    label("loc_1306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_132D")
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    SetMapObjFlags(0x11, 0x1000)
    Jump("loc_1384")

    label("loc_132D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1354")
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    SetMapObjFlags(0x11, 0x1000)
    Jump("loc_1384")

    label("loc_1354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1362")
    Jump("loc_1384")

    label("loc_1362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1384")
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "light", 0x0, 0x1)
    SetMapObjFlags(0x11, 0x1000)

    label("loc_1384")

    SetMapObjFlags(0xB, 0x4)
    Return()

    # Function_4_ED7 end

    def Function_5_138B(): pass

    label("Function_5_138B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B9")
    Call(0, 33)
    Return()

    label("loc_13B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_15FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_151A")

    ChrTalk(
        0xFE,
        (
            "Since the declaration of independence day,\x01",
            "the transcontinental railway service has stopped.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And yet, it appears that a civil war\x01",
            "broke out in the Empire and the\x01",
            "Republic is in a panic too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*haah*, I guess the peaceful times when\x01",
            "I gazed at the railway are over, right?\x01",
            "There's no sadder thing than this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15F5")

    label("loc_151A")


    ChrTalk(
        0xFE,
        (
            "Since the declaration of independence day,\x01",
            "the transcontinental railway service has stopped.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*haah*, I guess the peaceful times when\x01",
            "I gazed at the railway are over, right?\x01",
            "There's no sadder thing than this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F5")

    Jump("loc_2A68")

    label("loc_15FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1608")
    Jump("loc_2A68")

    label("loc_1608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_17D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1709")

    ChrTalk(
        0xFE,
        (
            "It appears that by today's end,\x01",
            "the transcontinental railway\x01",
            "service is going to be stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uuh, my reason to live...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How I wish that everything got settled in the blink\x01",
            "of an eye and the service reopened quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17CB")

    label("loc_1709")


    ChrTalk(
        0xFE,
        (
            "Uuh, the transcontinental railway\x01",
            "service, my reason to live, is\x01",
            "going to stop today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How I wish that everything got settled in the blink\x01",
            "of an eye and the service reopened quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17CB")

    Jump("loc_2A68")

    label("loc_17D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1950")

    ChrTalk(
        0xFE,
        (
            "It's a rumor, but could the recent raid incident\x01",
            "have been perpetrated by the Empire?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What if the derailment accident and Mainz\x01",
            "occupation too which happened recently\x01",
            "were all the Empire fault...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's easy to believe that since they're the most\x01",
            "advanced nation for railway technology, but...\x01",
            "If you start to have doubts, there'll be no end.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A32")

    label("loc_1950")


    ChrTalk(
        0xFE,
        (
            "What if the recently occurred\x01",
            "incidents were all the Empire fault...?\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's easy to believe that since they're the most\x01",
            "advanced nation for railway technology, but...\x01",
            "If you start to have doubts, there'll be no end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A32")

    Jump("loc_2A68")

    label("loc_1A37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1B34")

    ChrTalk(
        0xFE,
        (
            "One day from when the train derailment\x01",
            "accident occurred has not even passed\x01",
            "that an occupation incident happens...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have a bad feeling about this.\x01",
            "Could it really be a coincidence for incidents\x01",
            "to happen in such succession...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A68")

    label("loc_1B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1CF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C4E")

    ChrTalk(
        0xFE,
        (
            "I'm really glad they were able to repair\x01",
            "the transcontinental railway in one night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to this, I'll be able to enjoy\x01",
            "trains to my heart's content today too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have not enough words of gratitude for\x01",
            "the CGF who worked all night long!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CF4")

    label("loc_1C4E")


    ChrTalk(
        0xFE,
        (
            "Thanks to this, I'll be able to enjoy\x01",
            "trains to my heart's content today too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have not enough words of gratitude for\x01",
            "the CGF who worked all night long!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CF4")

    Jump("loc_2A68")

    label("loc_1CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1DA8")

    ChrTalk(
        0xFE,
        (
            "Uuh, my Goddess.\x01",
            "A derailment accident of all things...!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The train is gonna be all right, huh...?\x01",
            "My heart can't settle down due to all the worrying!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A68")

    label("loc_1DA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2004")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F0E")

    ChrTalk(
        0xFE,
        (
            "It appears that yesterday there was an\x01",
            "incident of someone jumping on the train\x01",
            "roof from the station platform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can understand how it feels, but...\x01",
            "As a railway maniac, I can't condone the deed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nothing is worse than scratching the train\x01",
            "and causing trouble for the passengers by \x01",
            "boarding in an unreasonable way.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FFF")

    label("loc_1F0E")


    ChrTalk(
        0xFE,
        (
            "It appears that yesterday there was an\x01",
            "incident of someone jumping on the train\x01",
            "roof from the station platform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nothing is worse than scratching the train\x01",
            "and causing trouble for the passengers by \x01",
            "boarding in an unreasonable way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FFF")

    Jump("loc_2A68")

    label("loc_2004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2207")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2144")

    ChrTalk(
        0xFE,
        (
            "I can't concretely understand\x01",
            "what kind of benefit there is\x01",
            "in being independent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, I just hope something\x01",
            "like making the Empire and Republic\x01",
            "our enemies doesn't happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If that were the cause of the\x01",
            "transcontinental railway getting\x01",
            "stopped, I couldn't go on living.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2202")

    label("loc_2144")


    ChrTalk(
        0xFE,
        (
            "I just hope we don't\x01",
            "make enemies of the\x01",
            "Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the independence were the cause\x01",
            "of the transcontinental railway getting\x01",
            "stopped, I couldn't go on living, you see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2202")

    Jump("loc_2A68")

    label("loc_2207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_238B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E7")

    ChrTalk(
        0xFE,
        (
            "In 80% of the trade conferences\x01",
            "I attended, I ended up being\x01",
            "able to see the "Eisengraf".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After the schedule is over,\x01",
            "I'd be satisfied if I could see its\x01",
            "shape running through Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2386")

    label("loc_22E7")


    ChrTalk(
        0xFE,
        (
            "80% of the trade conferences\x01",
            "I attended ended with me being\x01",
            "able to see the "Eisengraf".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then, should I go home\x01",
            "for today and read a book or...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2386")

    Jump("loc_2A68")

    label("loc_238B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_25CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2514")

    ChrTalk(
        0xFE,
        (
            "Aaaah... That... Could that really be\x01",
            "the Imperial government exclusive\x01",
            "orbal train, the "Eisengraf"...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That composed design denoting the Empire extremely\x01",
            "strong power and the underlying red-like flames...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can say it's a superb train which lives\x01",
            "up to its name of "Eisengraf [Iron Count]"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm so glad I've bought\x01",
            "a camera for this day...!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25C6")

    label("loc_2514")


    ChrTalk(
        0xFE,
        (
            "That Imperial government exclusive\x01",
            "train is a train that can be said to \x01",
            "live up to its name of "Eisengraf"!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aah, what a nice day this is.\x01",
            "I don't even care if I die!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C6")

    Jump("loc_2A68")

    label("loc_25CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_27DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2729")

    ChrTalk(
        0xFE,
        (
            "The West Zemuria Trade Conference...\x01",
            "When I heard that Empire VIPs are coming too, \x01",
            "being a railway maniac I couldn't have missed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, the Imperial government has an\x01",
            "orbal train for exclusive use, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since they are Empire VIPs, they\x01",
            "should definitely come boarding it...\x01",
            "Myyy, I can't wait.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_27D6")

    label("loc_2729")


    ChrTalk(
        0xFE,
        (
            "The Imperial government has\x01",
            "an orbal train for exclusive use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure that they're going to come in\x01",
            "that on tomorrow's inauguration ceremony.\x01",
            "Myyy, I can't wait.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D6")

    Jump("loc_2A68")

    label("loc_27DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2888")

    ChrTalk(
        0xFE,
        "Weather doesn't matter in a railway maniac activities.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Trains wet by the rain actually are nice too.\x01",
            "The water dripping from them and all that, see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A68")

    label("loc_2888")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2A68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29AE")

    ChrTalk(
        0xFE,
        (
            "It seems that the transcontinental railway\x01",
            "is in perfect service today too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The trains magnificent forms,\x01",
            "the beautiful coloring like it \x01",
            "reflects the blue sky...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, every time I see them, what a great\x01",
            "feeling it is. I'm glad to be a railway maniac.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2A68")

    label("loc_29AE")


    ChrTalk(
        0xFE,
        (
            "The trains magnificent forms,\x01",
            "the beautiful coloring like it \x01",
            "reflects the blue sky...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, every time I see them, what a great\x01",
            "feeling it is. I'm glad to be a railway maniac.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A68")

    TalkEnd(0xFE)
    Return()

    # Function_5_138B end

    def Function_6_2A6C(): pass

    label("Function_6_2A6C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B67")

    ChrTalk(
        0xFE,
        (
            "I decided to go share to every place\x01",
            "in Crossbell City the goods in excess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that we can't get goods from abroad,\x01",
            "there should be a limit to that too, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a carrier, I must do\x01",
            "first what I can do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C0D")

    label("loc_2B67")


    ChrTalk(
        0xFE,
        (
            "Now that we can't get goods from abroad,\x01",
            "there should be a limit to sharing goods\x01",
            "with every place, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a carrier, I must do\x01",
            "first what I can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C0D")

    Jump("loc_3372")

    label("loc_2C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2C20")
    Jump("loc_3372")

    label("loc_2C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2CE9")

    ChrTalk(
        0xFE,
        (
            "Hey now, somehow the\x01",
            "situation has become serious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems the railway service has stopped too...\x01",
            "What's going to happen to the goods circulation\x01",
            "with the foreign countries?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3372")

    label("loc_2CE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2CF7")
    Jump("loc_3372")

    label("loc_2CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2DC5")

    ChrTalk(
        0xFE,
        (
            "Who could've thought something\x01",
            "like an occupation incident to happen\x01",
            "in the autonomous state of Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears the CGF is having a hard fight...\x01",
            "How is gonna end, I wonder...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3372")

    label("loc_2DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2DD3")
    Jump("loc_3372")

    label("loc_2DD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2DE1")
    Jump("loc_3372")

    label("loc_2DE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2E77")

    ChrTalk(
        0xFE,
        (
            "You guys delivered the\x01",
            "misdelivered goods for\x01",
            "the Capua Express, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, what a relief.\x01",
            "The SSS is dependable as always.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3372")

    label("loc_2E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2F61")

    ChrTalk(
        0xFE,
        (
            "There was a notification about being careful\x01",
            "going back and forth the highways due to\x01",
            "strange monsters having appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Carriers like us go back and\x01",
            "forth a lot, so we really need\x01",
            "to be careful about monsters.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3372")

    label("loc_2F61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2FE8")

    ChrTalk(
        0xFE,
        "Well then, I guess it's time to do deliveries.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If if don't carry them quickly,\x01",
            "I'll be scolded by the old man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3372")

    label("loc_2FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_31B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30E8")

    ChrTalk(
        0xFE,
        (
            "Although I have to receive the\x01",
            "packages and deliver them quickly,\x01",
            "they're really late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The freight train cargo is probably\x01",
            "being checked pretty strictly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess it can't be helped, since\x01",
            "Empire big-shots came by.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_31B1")

    label("loc_30E8")


    ChrTalk(
        0xFE,
        (
            "Although I have to receive the\x01",
            "packages and deliver them quickly,\x01",
            "they're really late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Having big-shots from the Empire come,\x01",
            "the checks have become stricter too.\x01",
            "I guess it can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31B1")

    Jump("loc_3372")

    label("loc_31B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_31C4")
    Jump("loc_3372")

    label("loc_31C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_31D2")
    Jump("loc_3372")

    label("loc_31D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3372")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32ED")

    ChrTalk(
        0xFE,
        (
            "We are a private management shipping\x01",
            "company called Rhymes Shipping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My old man is the president of our young\x01",
            "company, but we do our best with the\x01",
            "motto of being kind, polite and speedy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have an order, please\x01",
            "contact us by all means.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3372")

    label("loc_32ED")


    ChrTalk(
        0xFE,
        (
            "We are a private management shipping\x01",
            "company called Rhymes Shipping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have an order, please\x01",
            "contact us by all means.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3372")

    TalkEnd(0xFE)
    Return()

    # Function_6_2A6C end

    def Function_7_3376(): pass

    label("Function_7_3376")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3549")

    ChrTalk(
        0xFE,
        "Oh, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FAh... Mom.\x01",
            "Are you going to visit Fran now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, I'm about to go bring\x01",
            "Fran a change of clothes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How was she?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FWell, as you can imagine,\x01",
            "it seems she's still tired, but...\x01",
            "She looks well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*, that's good to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, until she's better in shape,\x01",
            "I plan to go visit her frequently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And so, leave her to me\x01",
            "and you do your best\x01",
            "with your job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes, I know.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 7)
    Jump("loc_35C1")

    label("loc_3549")


    ChrTalk(
        0xFE,
        (
            "Your transfer at the Support Section\x01",
            "ends today, right, Noｱl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Try to work diligently to\x01",
            "not have any regrets.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35C1")

    TalkEnd(0xFE)
    Return()

    # Function_7_3376 end

    def Function_8_35C5(): pass

    label("Function_8_35C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3675")

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "Mhrrrr, I can't go back to the Empire\x01",
            "until the end of the day...!?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "Tsk, State Guard my ass!\x01",
            "They just spout whatever they want!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3876")

    label("loc_3675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3744")

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "Who could've ever thought that an occupation\x01",
            "incident would've taken place in Crossbell City...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "Does it mean we did something...?\x01",
            "I can't take this situation anymore.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3876")

    label("loc_3744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_37FB")

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "National independence, huh...?\x01",
            "To think that the day when such a\x01",
            "thing was proposed would've come...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "In any case, I wish\x01",
            "it could be realized.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3876")

    label("loc_37FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3876")

    ChrTalk(
        0xFE,
        (
            "Ooh, what a... What a great\x01",
            "line up of stores and houses!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hu hu, I'm feeling so\x01",
            "excited despite my age!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3876")

    TalkEnd(0xFE)
    Return()

    # Function_8_35C5 end

    def Function_9_387A(): pass

    label("Function_9_387A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_38EA")

    NpcTalk(
        0xFE,
        "Tourist",
        "Dear, please, calm down...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Tourist",
        (
            "Anyway, let's go buy\x01",
            "the tickets quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A21")

    label("loc_38EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_393D")

    ChrTalk(
        0xFE,
        (
            "Many ambulances passed by...\x01",
            "W-What could all the commotion be?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A21")

    label("loc_393D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_399C")

    ChrTalk(
        0xFE,
        (
            "Crossbell is\x01",
            "really big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish I had bought at\x01",
            "least a tourist guide.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A21")

    label("loc_399C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3A21")

    ChrTalk(
        0xFE,
        (
            "My husband is enjoying it very much,\x01",
            "but I'm worried somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, isn't Crossbell\x01",
            "called the "Demon City"?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A21")

    TalkEnd(0xFE)
    Return()

    # Function_9_387A end

    def Function_10_3A25(): pass

    label("Function_10_3A25")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3B1C")

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "Losing my job in Crossbell hurts me, but it's\x01",
            "worse not being able to return to my home town.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "I can't sit still in this situation.\x01",
            "Before something strange happens,\x01",
            "I have to get away from Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C48")

    label("loc_3B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3BA2")

    ChrTalk(
        0xFE,
        (
            "Occupation by an armed group...\x01",
            "Why on earth did such an incident...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is Mainz safe, I wonder?\x01",
            "I'm worried...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C48")

    label("loc_3BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3C48")

    ChrTalk(
        0xFE,
        (
            "Uhhhm, where is the hotel\x01",
            "I reserved for today...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I treated myself to lodge in the Entertainment District.\x01",
            "I must enjoy this trip to the fullest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C48")

    TalkEnd(0xFE)
    Return()

    # Function_10_3A25 end

    def Function_11_3C4C(): pass

    label("Function_11_3C4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3CE6")

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "Lately I received a notice\x01",
            "from the Empire to leave...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "*haah*, I had become fond\x01",
            "of living in Crossbell...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DEB")

    label("loc_3CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3D5D")

    ChrTalk(
        0xFE,
        (
            "I'm worried that that armed group\x01",
            "could come to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Won't the CGF do\x01",
            "something fast...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DEB")

    label("loc_3D5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3DEB")

    ChrTalk(
        0xFE,
        (
            "Uh uh, what do I have to do with you,\x01",
            "being in such high spirits...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I can understand.\x01",
            "Crossbell is a great city.\x01\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DEB")

    TalkEnd(0xFE)
    Return()

    # Function_11_3C4C end

    def Function_12_3DEF(): pass

    label("Function_12_3DEF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3E7D")

    ChrTalk(
        0xFE,
        (
            "I intend to get away from\x01",
            "Crossbell on the double.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want to remain in such a\x01",
            "dangerous place a second more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F91")

    label("loc_3E7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F0F")

    ChrTalk(
        0xFE,
        (
            ""Independence" or whatever,\x01",
            "I don't really know what it is.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll look into it before\x01",
            "the referendum day comes...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F91")

    label("loc_3F0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3F91")

    ChrTalk(
        0xFE,
        "This morning's bustle was something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All those gorgeous limousines coming\x01",
            "and going... Those are VIPs for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F91")

    TalkEnd(0xFE)
    Return()

    # Function_12_3DEF end

    def Function_13_3F95(): pass

    label("Function_13_3F95")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4046")

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "What should I do... The grounds are\x01",
            "too crowded and I can't get inside.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "Uuh, will I really be able to\x01",
            "go back to the Republic...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40C1")

    label("loc_4046")


    ChrTalk(
        0xFE,
        (
            "I saw the inauguration ceremony from\x01",
            "the department store rooftop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aahn, I looked directly\x01",
            "at Lady Julia's face!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40C1")

    TalkEnd(0xFE)
    Return()

    # Function_13_3F95 end

    def Function_14_40C5(): pass

    label("Function_14_40C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4139")

    ChrTalk(
        0xFE,
        (
            "Hey, hey, why do we have to\x01",
            "go home to the Empire...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had just made so\x01",
            "many friends...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_428E")

    label("loc_4139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_41C1")

    ChrTalk(
        0xFE,
        (
            "When we played at the train station I made the\x01",
            "station attendant mad and we were thrown out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Tch, party-pooper.\x02",
    )

    CloseMessageWindow()
    Jump("loc_428E")

    label("loc_41C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_423B")

    ChrTalk(
        0xFE,
        (
            "Alright, then let's play hide and\x01",
            "seek inside the train station today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Eh eh, I'll be "it" first.\x02",
    )

    CloseMessageWindow()
    Jump("loc_428E")

    label("loc_423B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_428E")

    ChrTalk(
        0xFE,
        "Woow, so this is Crossbell!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hey, hey, quick, let's go mamaaa!!\x02",
    )

    CloseMessageWindow()

    label("loc_428E")

    TalkEnd(0xFE)
    Return()

    # Function_14_40C5 end

    def Function_15_4292(): pass

    label("Function_15_4292")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4340")

    ChrTalk(
        0xFE,
        (
            "Geez, big brother...\x01",
            "That's why I told you to quit it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...However, the station attendants\x01",
            "really looked to be busy.\x01",
            "Could something have happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D1")

    label("loc_4340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4397")

    ChrTalk(
        0xFE,
        "Eeeh, let's not, big brother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The station people will get mad.\x02",
    )

    CloseMessageWindow()
    Jump("loc_43D1")

    label("loc_4397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_43D1")

    ChrTalk(
        0xFE,
        (
            "I too wanna play at the\x01",
            "casino with father!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43D1")

    TalkEnd(0xFE)
    Return()

    # Function_15_4292 end

    def Function_16_43D5(): pass

    label("Function_16_43D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_44AF")

    ChrTalk(
        0xFE,
        (
            "I wonder through which route\x01",
            "the terrorists will try to enter\x01",
            "into Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There shouldn't be blind spots...\x01",
            "Anyway, in the present condition I can\x01",
            "only keep staying vigilant like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4642")

    label("loc_44AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4549")

    ChrTalk(
        0xFE,
        (
            "*phew*, somehow the inauguration ceremony ended.\x01",
            "I feel like a weight has gone off my mind a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Although I can't relax yet.\x01\x02",
    )

    CloseMessageWindow()
    Jump("loc_4642")

    label("loc_4549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4642")

    ChrTalk(
        0xFE,
        (
            "Inside the train station and the airport there're\x01",
            "quite a considerable number of detectives from\x01",
            "Section Two on duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Including the other places, it's the first\x01",
            "time I remember such a solid vigilance\x01",
            "system to have been deployed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4642")

    TalkEnd(0xFE)
    Return()

    # Function_16_43D5 end

    def Function_17_4646(): pass

    label("Function_17_4646")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46E2")

    ChrTalk(
        0xFE,
        (
            "I came to see off my wife and daughter\x01",
            "who're returning home to the Empire, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "S-Something like a derailment accident...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4725")

    label("loc_46E2")


    ChrTalk(
        0xFE,
        (
            "W-What if my wife and daughter\x01",
            "were on board of that train...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4725")

    TalkEnd(0xFE)
    Return()

    # Function_17_4646 end

    def Function_18_4729(): pass

    label("Function_18_4729")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "My Goddess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder how much\x01",
            "the damage was...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_4729 end

    def Function_19_476C(): pass

    label("Function_19_476C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Are the trains not running?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, this means that I can stay \x01",
            "together with papa today too!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_476C end

    def Function_20_47D9(): pass

    label("Function_20_47D9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "With today, Crossbell Station service\x01",
            "is scheduled to be stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, at present it is still not decided\x01",
            "when the service will resume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The foreigners who wish to return to their\x01",
            "countries are asked to please hurry.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_47D9 end

    def Function_21_48C8(): pass

    label("Function_21_48C8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51231.itc", 0x1E)
    SoundLoad(835)
    SoundLoad(825)
    SoundLoad(455)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x1B, 0xC)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0xC)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0xC)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0xC)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0xC)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0xC)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x80)
    OP_78(0x13, 0x21)
    OP_49()
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x1B, -3750, 0, -1250, 270)
    SetChrPos(0x1C, -3750, 0, -2750, 270)
    SetChrPos(0x1D, -2750, 0, 11000, 270)
    SetChrPos(0x1E, -2750, 0, 9500, 270)
    SetChrPos(0x1F, -2750, 0, 5500, 270)
    SetChrPos(0x20, -2750, 0, 4000, 270)
    SetChrPos(0x21, -37500, -11600, 7500, 90)
    OP_D5(0x21, 0x0, 0x15F90, 0x0, 0x0)
    OP_68(9150, 2700, -1950, 0)
    MoveCamera(48, 10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27850, 0)
    OP_68(-2750, 1000, 7000, 5000)
    MoveCamera(45, 25, 0, 5000)
    SetCameraDistance(16000, 5000)
    Sound(835, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x1F, 0x1E)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    SetCameraDistance(15750, 200)
    OP_0D()
    Sleep(500)
    Fade(1000)
    SetChrPos(0x1B, -8000, -10300, -1000, 0)
    SetChrPos(0x1C, -9500, -10300, -1000, 0)
    SetChrPos(0x1D, -11000, -10300, -1000, 0)
    SetChrPos(0x1E, -12500, -10300, -1000, 0)
    SetChrPos(0x1F, -14000, -10300, -1000, 0)
    SetChrPos(0x20, -15500, -10300, -1000, 0)
    OP_68(-20000, -8500, 7500, 0)
    MoveCamera(325, 10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(7000, 0)
    OP_68(0, -8500, 7500, 8000)
    MoveCamera(70, 15, 0, 8000)
    SetCameraDistance(32000, 8000)
    Sound(455, 0, 100, 0)
    BeginChrThread(0x22, 1, 0, 23)

    def lambda_4BE5():
        OP_9B(0x1, 0xFE, 0x0, 0x30D40, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_4BE5)
    BeginChrThread(0x21, 0, 0, 22)
    Sleep(5000)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_48C8 end

    def Function_22_4C1C(): pass

    label("Function_22_4C1C")

    OP_82(0x0, 0x32, 0x5DC, 0x2EE)
    Sleep(1500)
    OP_82(0x0, 0x32, 0x5DC, 0x2EE)
    Sleep(1500)
    OP_82(0x0, 0x32, 0x5DC, 0x2EE)
    Sleep(1500)
    OP_82(0x0, 0x32, 0x5DC, 0x2EE)
    Sleep(1500)
    OP_82(0x0, 0x32, 0x5DC, 0x2EE)
    Sleep(1500)
    Return()

    # Function_22_4C1C end

    def Function_23_4C81(): pass

    label("Function_23_4C81")

    Sound(825, 2, 10, 0)
    Sleep(100)
    OP_25(0x339, 0x14)
    Sleep(100)
    OP_25(0x339, 0x1E)
    Sleep(100)
    OP_25(0x339, 0x28)
    Sleep(100)
    OP_25(0x339, 0x32)
    Sleep(100)
    OP_25(0x339, 0x3C)
    Sleep(100)
    OP_25(0x339, 0x46)
    Sleep(100)
    OP_25(0x339, 0x50)
    Sleep(5300)
    StopSound(825, 2000, 80)
    Return()

    # Function_23_4C81 end

    def Function_24_4CC2(): pass

    label("Function_24_4CC2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41800.itc", 0x1E)
    LoadChrToIndex("chr/ch41500.itc", 0x1F)
    SetChrPos(0x0, 6500, 0, 8000, 0)
    SetChrPos(0x1, 6500, 0, 8000, 0)
    SetChrPos(0x2, 6500, 0, 8000, 0)
    SetChrPos(0x3, 6500, 0, 8000, 0)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x12, 0x18)
    OP_49()
    SetChrPos(0x18, 5000, 0, -1000, 0)
    OP_D5(0x18, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x12, 0x1000)
    ClearMapObjFlags(0x12, 0x4)
    OP_74(0x12, 0x1E)
    OP_70(0x12, 0x3)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 2500, 0, 100, 270)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 2500, 0, -4500, 270)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x2)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 200, 0, -3500, 90)
    OP_4B(0xC, 0xFF)
    SetChrChipByIndex(0xC, 0x3)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -1000, 0, -1800, 90)
    OP_4B(0xD, 0xFF)
    SetChrChipByIndex(0xD, 0x4)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -1000, 0, -3000, 90)
    OP_4B(0xE, 0xFF)
    SetChrChipByIndex(0xE, 0x5)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -1000, 0, 0, 135)
    OP_4B(0xF, 0xFF)
    SetChrChipByIndex(0xF, 0x6)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 100, 0, -4900, 45)
    OP_4B(0x10, 0xFF)
    SetChrChipByIndex(0x10, 0x7)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2400, 0, -2400, 90)
    OP_4B(0x11, 0xFF)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -1400, 0, -5400, 45)
    OP_4B(0x12, 0xFF)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 600, 0, 1000, 135)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(2200, 1200, -2000, 0)
    MoveCamera(39, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(19500, 0)
    MoveCamera(51, 23, 0, 13000)
    SetCameraDistance(16500, 13000)
    Sound(821, 2, 60, 0)
    Sound(835, 2, 80, 0)
    FadeToBright(1500, 0)
    OP_0D()
    SetMessageWindowPos(150, 100, -1, -1)
    SetChrName("President Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──For too many years they\x01",
            "have treated Crossbell as\x01",
            "their own "province".\x02\x03",
            "No matter which crimes they commit,\x01",
            "we have no right to solve them.\x02\x03",
            "And even now...\x01",
            "We keep being exploited in ways which\x01",
            "snatch away abundant revenues from us.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_70(0x12, 0x4)
    Sleep(300)
    SetMessageWindowPos(150, 110, -1, -1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetChrName("President Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S──However, it's\x01",
            "not only that!\x02\x03",
            "#4SWe've come to a point where\x01",
            "even our lives are threatened...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    StopSound(851, 1500, 60)
    StopSound(835, 1500, 80)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 4)
    NewScene("c040D", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_4CC2 end

    def Function_25_518D(): pass

    label("Function_25_518D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 300, 0, -24600, 0)
    SetChrPos(0x102, 1600, 0, -25000, 0)
    SetChrPos(0x103, 300, 0, -26000, 0)
    SetChrPos(0x104, 1600, 0, -26400, 0)
    SetChrPos(0x109, 900, 0, -27500, 0)
    SetChrPos(0x105, -1000, 0, -26400, 0)
    SetChrPos(0x106, -500, 0, -27500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    OP_68(0, 1200, -15300, 0)
    MoveCamera(40, 29, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(32500, 0)

    def lambda_5261():
        OP_97(0x101, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5261)
    Sleep(100)

    def lambda_527E():
        OP_97(0x102, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_527E)
    Sleep(100)

    def lambda_529B():
        OP_97(0x103, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_529B)
    Sleep(100)

    def lambda_52B8():
        OP_97(0x104, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_52B8)
    Sleep(100)

    def lambda_52D5():
        OP_97(0x105, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_52D5)
    Sleep(100)

    def lambda_52F2():
        OP_97(0x109, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_52F2)
    Sleep(100)

    def lambda_530F():
        OP_97(0x106, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_530F)
    OP_68(0, 1200, -5300, 3000)
    MoveCamera(50, 25, 0, 3000)
    SetCameraDistance(22500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(500, 1200, -1300, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetCameraDistance(16500, 2000)
    OP_0D()
    WaitChrThread(0x101, 0)
    BeginChrThread(0x101, 3, 0, 26)
    WaitChrThread(0x102, 0)
    BeginChrThread(0x102, 3, 0, 27)
    WaitChrThread(0x104, 0)
    BeginChrThread(0x104, 3, 0, 28)
    WaitChrThread(0x105, 0)
    BeginChrThread(0x105, 3, 0, 29)
    WaitChrThread(0x109, 0)
    BeginChrThread(0x109, 3, 0, 30)
    WaitChrThread(0x106, 0)
    BeginChrThread(0x106, 3, 0, 31)
    OP_6F(0x79)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#00006FI'd like to get hold of the Chief\x01",
            "and the others in some way, but...\x02\x03",
            "#00013FWhat's this...?\x01",
            "This bluish mist?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108FIt looks like what appeared\x01",
            "at the Temple and the Tower...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5PThere's...\x01",
            "No pedestrian traffic at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10408FWell, because outside the city\x01",
            "fightings are taking place, they\x01",
            "could've taken refuge somewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00205F#30W............\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x106, 3)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x103, 500)

    ChrTalk(
        0x102,
        "#5P#00105FTio?\x02",
    )

    CloseMessageWindow()

    def lambda_55B5():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_55B5)
    Sleep(30)

    def lambda_55C5():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_55C5)
    Sleep(30)

    def lambda_55D5():
        TurnDirection(0x106, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_55D5)
    Sleep(30)

    def lambda_55E5():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_55E5)
    Sleep(30)

    def lambda_55F5():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_55F5)
    Sleep(30)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x104,
        "#11P#00301FWhat, something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203F...I can hear a resonance\x01",
            "sound from Central Square.\x02\x03",
            "#00201FIt is that big bell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00007FWhat...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10701F...Let's go have a look.\x02",
    )

    CloseMessageWindow()

    def lambda_56E4():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_56E4)
    Sleep(30)

    def lambda_56F4():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_56F4)
    Sleep(30)

    def lambda_5704():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5704)
    Sleep(30)

    def lambda_5714():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5714)
    Sleep(30)

    def lambda_5724():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5724)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_68(500, 1200, 7500, 3000)
    MoveCamera(37, 21, 0, 3000)
    SetCameraDistance(20500, 3000)

    def lambda_576D():
        OP_97(0x101, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_576D)
    Sleep(100)

    def lambda_578A():
        OP_97(0x102, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_578A)
    Sleep(100)

    def lambda_57A7():
        OP_97(0x103, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_57A7)
    Sleep(100)

    def lambda_57C4():
        OP_97(0x104, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_57C4)
    Sleep(100)

    def lambda_57E1():
        OP_97(0x105, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_57E1)
    Sleep(100)

    def lambda_57FE():
        OP_97(0x109, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_57FE)
    Sleep(100)

    def lambda_581B():
        OP_97(0x106, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_581B)
    Sleep(1900)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    EndChrThread(0x106, 0xFF)
    SetScenarioFlags(0x24, 0)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_518D end

    def Function_26_5869(): pass

    label("Function_26_5869")

    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_26_5869 end

    def Function_27_587B(): pass

    label("Function_27_587B")

    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1100)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_27_587B end

    def Function_28_5890(): pass

    label("Function_28_5890")

    Sleep(500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_28_5890 end

    def Function_29_58A5(): pass

    label("Function_29_58A5")

    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_29_58A5 end

    def Function_30_58B0(): pass

    label("Function_30_58B0")

    Sleep(500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_30_58B0 end

    def Function_31_58BB(): pass

    label("Function_31_58BB")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_31_58BB end

    def Function_32_58CD(): pass

    label("Function_32_58CD")

    EventBegin(0x0)
    OP_E2(0x3)
    Fade(500)
    OP_68(6400, 1900, -1900, 0)
    MoveCamera(57, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15860, 0)
    SetChrPos(0x101, 6500, 0, -1900, 90)
    SetChrPos(0x102, 5900, 0, -1000, 90)
    SetChrPos(0x103, 5900, 0, -2800, 90)
    SetChrPos(0x104, 3900, 0, -1900, 90)
    SetChrPos(0xF4, 4300, 0, -3100, 90)
    SetChrPos(0xF5, 4300, 0, -700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F(...I don't know how much time Miss Kilika\x01",
            "and Captain Lechter's talk will take.)\x02\x03",
            "#00001F(We have time before the operation, so it\x01",
            "would be better to finish what we have to do.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you proceed with the events past this\x01",
            "point, you will break into Orchis Tower and\x01",
            "will not be able to freely move in the city.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Enter the Station Premises\x01",      # 0
            "Finish Other Business\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5B53"),
        (1, "loc_5CB3"),
        (SWITCH_DEFAULT, "loc_5CE5"),
    )


    label("loc_5B53")

    OP_68(8400, 1900, -1900, 1500)
    MoveCamera(90, 13, 0, 1500)

    def lambda_5B74():
        OP_96(0xFE, 0x2328, 0xFA, 0xFFFFF894, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B74)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    SetCameraDistance(17500, 3000)

    def lambda_5BB8():
        OP_97(0x101, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5BB8)
    Sleep(50)

    def lambda_5BD5():
        OP_97(0x103, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5BD5)
    Sleep(50)

    def lambda_5BF2():
        OP_97(0x102, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5BF2)
    Sleep(50)

    def lambda_5C0F():
        OP_97(0x104, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5C0F)
    Sleep(50)

    def lambda_5C2C():
        OP_97(0xF4, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_5C2C)
    Sleep(50)

    def lambda_5C49():
        OP_97(0xF5, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_5C49)
    Sleep(300)
    FadeToDark(2000, 0, -1)

    def lambda_5C70():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5C70)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x101, 0xFF)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0xF4, 0xFF)
    EndChrThread(0xF5, 0xFF)
    SetScenarioFlags(0x22, 0)
    NewScene("c0010", 0, 0, 0)
    IdleLoop()
    Jump("loc_5CE5")

    label("loc_5CB3")

    SetChrPos(0x0, 6500, 0, -2000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_E2(0x2)
    EventEnd(0x5)
    Jump("loc_5CE5")

    label("loc_5CE5")

    Return()

    # Function_32_58CD end

    def Function_33_5CE6(): pass

    label("Function_33_5CE6")

    TalkBegin(0x8)

    ChrTalk(
        0x8,
        (
            "Before, an Empire made black truck\x01",
            "ran towards Central Square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Where did it go after that, you ask?\x01",
            "I'm sorry, I don't know.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_33_5CE6 end

    def Function_34_5D77(): pass

    label("Function_34_5D77")

    EventBegin(0x1)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)
    Return()

    # Function_34_5D77 end

    def Function_35_5D8D(): pass

    label("Function_35_5D8D")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5DF2")

    ChrTalk(
        0x101,
        (
            "#00000FThis is Crossbell Station.\x01",
            "...We don't have any business here right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FFF")

    label("loc_5DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5E4E")
    Sound(807, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The doors are firmly locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 5)
    Jump("loc_5EE3")

    label("loc_5E4E")


    ChrTalk(
        0x101,
        (
            "#00001F...It appears the train\x01",
            "station was sealed.\x02\x03",
            "#00003FWell, it's not that we have\x01",
            "any special business here,\x01",
            "so let's leave this place be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EE3")

    SetScenarioFlags(0x1CE, 4)
    Jump("loc_5FFF")

    label("loc_5EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5FA5")

    ChrTalk(
        0x101,
        (
            "#00001F...It looks like that inside it's greatly congested\x01",
            "with foreigners returning to their countries.\x02\x03",
            "#00003FIt looks like it would be\x01",
            "better to not go inside.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    Jump("loc_5FFF")

    label("loc_5FA5")


    ChrTalk(
        0x101,
        (
            "#00000FThis is Crossbell Station.\x01",
            "...I guess we don't have any business here now.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)

    label("loc_5FFF")

    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)
    Return()

    # Function_35_5D8D end

    def Function_36_6013(): pass

    label("Function_36_6013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60F0")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6095")

    ChrTalk(
        0x101,
        (
            "#00000FThe south exit is this way.\x02\x03",
            "We don't have any special business,\x01",
            "so let's not exit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_60DD")

    label("loc_6095")


    ChrTalk(
        0x101,
        (
            "#00000FWe don't have any special business\x01",
            "here, so let's not exit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60DD")

    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_60F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6220")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6195")

    ChrTalk(
        0x101,
        (
            "#00001FThe south exit is this way.\x02\x03",
            "Let's focus on the investigation associated\x01",
            "with the incident without taking any detours.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_620D")

    label("loc_6195")


    ChrTalk(
        0x101,
        (
            "#00001FWe don't have any special business\x01",
            "here. Let's focus on the investigation\x01",
            "associated with the incident now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_620D")

    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_6220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6297")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FNow we have to chase Randy down...\x01",
            "It's not the time to wander around.\x01\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_6297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6311")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FNow it's not the time to go out the city.\x01",
            "Let's quietly retrace our steps.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_6311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_63C2")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FAfter coming here,\x01",
            "we can't leave the city.\x02\x03",
            "The operation to break into Orchis Tower...\x01",
            "We have to make it succeed at all costs.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_63C2")

    Return()

    # Function_36_6013 end

    def Function_37_63C3(): pass

    label("Function_37_63C3")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_37_63C3 end

    SaveToFile()

Try(main)
