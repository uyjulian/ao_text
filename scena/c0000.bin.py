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
        "Function_6_28F1",         # 06, 6
        "Function_7_3145",         # 07, 7
        "Function_8_338D",         # 08, 8
        "Function_9_35FE",         # 09, 9
        "Function_10_37BC",        # 0A, 10
        "Function_11_39DA",        # 0B, 11
        "Function_12_3B8B",        # 0C, 12
        "Function_13_3D2D",        # 0D, 13
        "Function_14_3E58",        # 0E, 14
        "Function_15_4024",        # 0F, 15
        "Function_16_4164",        # 10, 16
        "Function_17_4387",        # 11, 17
        "Function_18_4455",        # 12, 18
        "Function_19_449A",        # 13, 19
        "Function_20_4506",        # 14, 20
        "Function_21_45F4",        # 15, 21
        "Function_22_4948",        # 16, 22
        "Function_23_49AD",        # 17, 23
        "Function_24_49EE",        # 18, 24
        "Function_25_4EB3",        # 19, 25
        "Function_26_5573",        # 1A, 26
        "Function_27_5585",        # 1B, 27
        "Function_28_559A",        # 1C, 28
        "Function_29_55AF",        # 1D, 29
        "Function_30_55BA",        # 1E, 30
        "Function_31_55C5",        # 1F, 31
        "Function_32_55D7",        # 20, 32
        "Function_33_59E7",        # 21, 33
        "Function_34_5A7F",        # 22, 34
        "Function_35_5A95",        # 23, 35
        "Function_36_5D09",        # 24, 36
        "Function_37_60BA",        # 25, 37
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_15D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_150A")

    ChrTalk(
        0xFE,
        (
            "Rail service has been\x01",
            "stopped ever since the day\x01",
            "independence was declared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As if that weren't enough, a civil\x01",
            "war has started in the Empire and\x01",
            "there's a panic in the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I guess the peaceful times when\x01",
            "I gazed at the railway are over, right?\x01",
            "There's nothing sadder than this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15D2")

    label("loc_150A")


    ChrTalk(
        0xFE,
        (
            "Rail service has been\x01",
            "stopped ever since the day\x01",
            "independence was declared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I guess the peaceful times when\x01",
            "I gazed at the railway are over, right?\x01",
            "There's nothing sadder than this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D2")

    Jump("loc_28ED")

    label("loc_15D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_15E5")
    Jump("loc_28ED")

    label("loc_15E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1761")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B9")

    ChrTalk(
        0xFE,
        (
            "It seems rail service will be\x01",
            "suspended for a while starting\x01",
            "at the end of the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ooh, my reason to\x01",
            "live...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope everything is\x01",
            "settled quickly so\x01",
            "service can resume.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_175C")

    label("loc_16B9")


    ChrTalk(
        0xFE,
        (
            "Ooh, the transcontinental rail\x01",
            "service, my reason to live, is\x01",
            "going to be suspended today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope everything is\x01",
            "settled quickly so\x01",
            "service can resume.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_175C")

    Jump("loc_28ED")

    label("loc_1761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1996")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C9")

    ChrTalk(
        0xFE,
        (
            "It's a rumor, but they say the\x01",
            "attack the other day may have\x01",
            "been perpetrated by the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What if the Empire's responsible\x01",
            "for the recent derailment and\x01",
            "the Mainz occupation as well...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's easy to believe since their nation has\x01",
            "the most advanced rail tech, but... If you\x01",
            "start to have doubts, there'll be no end.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1991")

    label("loc_18C9")


    ChrTalk(
        0xFE,
        (
            "What if the recent\x01",
            "incidents were all the\x01",
            "Empire's fault...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's easy to believe since their nation has\x01",
            "the most advanced rail tech, but... If you\x01",
            "start to have doubts, there'll be no end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1991")

    Jump("loc_28ED")

    label("loc_1996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1A8D")

    ChrTalk(
        0xFE,
        (
            "It hasn't been that long since the\x01",
            "derailment. To think an occupation\x01",
            "would happen this soon after that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have a bad feeling about this. Could\x01",
            "the fact these incidents occurred so\x01",
            "close together really be a coincidence?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28ED")

    label("loc_1A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B9B")

    ChrTalk(
        0xFE,
        (
            "I'm really glad they were able\x01",
            "to repair the transcontinental\x01",
            "railway in one night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to that, I'll be\x01",
            "able to see the trains\x01",
            "today, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The CGF worked all night to\x01",
            "make this possible. No words\x01",
            "are enough to thank them!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C35")

    label("loc_1B9B")


    ChrTalk(
        0xFE,
        (
            "Thanks to that, I'll be\x01",
            "able to see the trains\x01",
            "today, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The CGF worked all night to\x01",
            "make this possible. No words\x01",
            "are enough to thank them!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C35")

    Jump("loc_28ED")

    label("loc_1C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1CCC")

    ChrTalk(
        0xFE,
        (
            "Ooh, my Goddess. A\x01",
            "derailment of all\x01",
            "things!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if the train is\x01",
            "all right... I'm worried\x01",
            "and I can't stop shaking!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28ED")

    label("loc_1CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1ECC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E05")

    ChrTalk(
        0xFE,
        (
            "I'm told that yesterday,\x01",
            "someone jumped onto a moving\x01",
            "train from the platform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand how they feel,\x01",
            "but... As a railway maniac, I\x01",
            "can't condone their actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It would be awful if the train was\x01",
            "damaged due to their recklessness\x01",
            "and passengers were inconvenienced.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1EC7")

    label("loc_1E05")


    ChrTalk(
        0xFE,
        (
            "I'm told that yesterday,\x01",
            "someone jumped onto a moving\x01",
            "train from the platform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It would be awful if the train was\x01",
            "damaged due to their recklessness\x01",
            "and passengers were inconvenienced.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EC7")

    Jump("loc_28ED")

    label("loc_1ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2072")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FCF")

    ChrTalk(
        0xFE,
        (
            "I can't concretely\x01",
            "understand what the benefits\x01",
            "of being independent are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, I just hope the\x01",
            "Empire and Republic don't\x01",
            "become our enemies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If rail service were\x01",
            "suspended for that reason,\x01",
            "I couldn't go on living.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_206D")

    label("loc_1FCF")


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
            "If rail service were suspended\x01",
            "due to independence, I couldn't\x01",
            "go on living, you see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_206D")

    Jump("loc_28ED")

    label("loc_2072")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2201")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2153")

    ChrTalk(
        0xFE,
        (
            "I ended up being able to see the\x01",
            "Eisengraf in 80% of the trade\x01",
            "conferences I've attended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After the schedule is over, I'd\x01",
            "be satisfied if I could see its\x01",
            "figure running through Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21FC")

    label("loc_2153")


    ChrTalk(
        0xFE,
        (
            "I ended up being able to see the\x01",
            "Eisengraf in 80% of the trade\x01",
            "conferences I've attended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then, I wonder if I\x01",
            "should go home today and\x01",
            "read a book, or...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21FC")

    Jump("loc_28ED")

    label("loc_2201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_241E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2371")

    ChrTalk(
        0xFE,
        (
            "Aaaah... That... Could it really be the\x01",
            "Eisengraf, the orbal train for exclusive\x01",
            "use by the Imperial government...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's bold design uses\x01",
            "reddish tones to display the\x01",
            "Empire's mighty power...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a superb train. It truly\x01",
            "lives up to its name, Eisengraf,\x01",
            "which means iron count!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm so glad I bought a\x01",
            "camera for today!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2419")

    label("loc_2371")


    ChrTalk(
        0xFE,
        (
            "That train for exclusive use by the\x01",
            "Imperial government truly lives up\x01",
            "to its name, the Eisengraf!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aah, what a nice day\x01",
            "this is. I don't even\x01",
            "care if I die!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2419")

    Jump("loc_28ED")

    label("loc_241E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_263E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2586")

    ChrTalk(
        0xFE,
        (
            "The West Zemuria Trade Conference... When I\x01",
            "heard Imperial VIPs are coming, being the\x01",
            "railway maniac I am, I couldn't have missed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, the Imperial government\x01",
            "has a special orbal train for\x01",
            "their exclusive use, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since they're Imperial VIPs,\x01",
            "they'll definitely be coming\x01",
            "in it... Maaan, I can't wait.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2639")

    label("loc_2586")


    ChrTalk(
        0xFE,
        (
            "The Imperial government\x01",
            "has an orbal train for\x01",
            "their exclusive use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure that they're going to come\x01",
            "in on it for tomorrow's unveiling\x01",
            "ceremony. Maaan, I can't wait.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2639")

    Jump("loc_28ED")

    label("loc_263E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_26F0")

    ChrTalk(
        0xFE,
        (
            "Weather doesn't matter\x01",
            "for a railway maniac's\x01",
            "activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Trains wet by the rain are nice\x01",
            "too, actually. With water dripping\x01",
            "from them and such, you see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28ED")

    label("loc_26F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_28ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2822")

    ChrTalk(
        0xFE,
        (
            "The transcontinental\x01",
            "railway seems to be running\x01",
            "perfectly today, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The magnificent forms of the\x01",
            "trains, their beautiful coloring\x01",
            "seeming to reflect the blue sky...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, it's a great feeling no\x01",
            "matter how many times I see them.\x01",
            "I'm glad to be a railway maniac.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_28ED")

    label("loc_2822")


    ChrTalk(
        0xFE,
        (
            "The magnificent forms of the\x01",
            "trains, their beautiful coloring\x01",
            "seeming to reflect the blue sky...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, it's a great feeling no\x01",
            "matter how many times I see them.\x01",
            "I'm glad to be a railway maniac.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28ED")

    TalkEnd(0xFE)
    Return()

    # Function_5_138B end

    def Function_6_28F1(): pass

    label("Function_6_28F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29DD")

    ChrTalk(
        0xFE,
        (
            "I decided to distribute\x01",
            "our excess goods\x01",
            "throughout Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that we can hardly get\x01",
            "goods from abroad, there's a\x01",
            "limit to what I can do, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a carrier, I must do\x01",
            "what I can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A70")

    label("loc_29DD")


    ChrTalk(
        0xFE,
        (
            "Now that we can't hardly get goods\x01",
            "from abroad, there's a limit to\x01",
            "what goods sharing can do, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a carrier, I must do\x01",
            "what I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A70")

    Jump("loc_3141")

    label("loc_2A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2A83")
    Jump("loc_3141")

    label("loc_2A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2B2A")

    ChrTalk(
        0xFE,
        (
            "Whoa, the situation's\x01",
            "somehow gotten\x01",
            "serious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems like rail service is\x01",
            "suspended too... How am I going\x01",
            "to distribute foreign goods now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3141")

    label("loc_2B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B38")
    Jump("loc_3141")

    label("loc_2B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2BDE")

    ChrTalk(
        0xFE,
        (
            "Who could've thought an\x01",
            "occupation would happen\x01",
            "in Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The CGF seems to be having\x01",
            "a tough time... I wonder\x01",
            "how this is going to end...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3141")

    label("loc_2BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2BEC")
    Jump("loc_3141")

    label("loc_2BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2BFA")
    Jump("loc_3141")

    label("loc_2BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2C89")

    ChrTalk(
        0xFE,
        (
            "You guys delivered the\x01",
            "misdelivered goods for\x01",
            "Capua Express, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, what a relief. The\x01",
            "SSS always so\x01",
            "dependable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3141")

    label("loc_2C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D54")

    ChrTalk(
        0xFE,
        (
            "There was a notice about being careful\x01",
            "travelling the highways due to the\x01",
            "appearance of strange monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Couriers like us travel\x01",
            "them often, so we need to\x01",
            "be especially careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3141")

    label("loc_2D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2DE1")

    ChrTalk(
        0xFE,
        (
            "Well then, I guess it's\x01",
            "time to do the\x01",
            "deliveries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If if don't deliver them\x01",
            "quickly, I'll be scolded\x01",
            "by the old man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3141")

    label("loc_2DE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2F83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ED9")

    ChrTalk(
        0xFE,
        (
            "I need to accept the packages\x01",
            "for delivery right away, but\x01",
            "they're rather slow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The freight train's\x01",
            "cargo is probably being\x01",
            "strictly checked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it's because\x01",
            "those Imperial VIPs\x01",
            "came. What can you do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F7E")

    label("loc_2ED9")


    ChrTalk(
        0xFE,
        (
            "I need to accept the packages\x01",
            "for delivery right away, but\x01",
            "they're rather slow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those Imperial VIPs came,\x01",
            "so checks have gotten\x01",
            "stricter. What can you do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F7E")

    Jump("loc_3141")

    label("loc_2F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2F91")
    Jump("loc_3141")

    label("loc_2F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2F9F")
    Jump("loc_3141")

    label("loc_2F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3141")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30BB")

    ChrTalk(
        0xFE,
        (
            "We're Rhymes Shipping, a\x01",
            "privately managed\x01",
            "shipping company.\x02",
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
            "If you have an order,\x01",
            "please feel free to\x01",
            "contact us about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3141")

    label("loc_30BB")


    ChrTalk(
        0xFE,
        (
            "We're Rhymes Shipping, a\x01",
            "privately managed\x01",
            "shipping company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have an order,\x01",
            "please feel free to\x01",
            "contact us about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3141")

    TalkEnd(0xFE)
    Return()

    # Function_6_28F1 end

    def Function_7_3145(): pass

    label("Function_7_3145")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3307")

    ChrTalk(
        0xFE,
        "Oh, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FAh... Mom. Are you going\x01",
            "to visit Fran?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, I'm about to bring\x01",
            "her a change of clothes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How is she?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FWell, as you can imagine, it\x01",
            "she's still rather tired, but...\x01",
            "For right now, she's doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, that's good to\x01",
            "hear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, until she's\x01",
            "better, I plan to visit\x01",
            "her often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So leave her to me and\x01",
            "do your best with your\x01",
            "job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes, I know.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 7)
    Jump("loc_3389")

    label("loc_3307")


    ChrTalk(
        0xFE,
        (
            "Your temporary transfer\x01",
            "to the Support Section\x01",
            "ends today, right, Noｱl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Try to work hard so you\x01",
            "don't have any regrets.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3389")

    TalkEnd(0xFE)
    Return()

    # Function_7_3145 end

    def Function_8_338D(): pass

    label("Function_8_338D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_343A")

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "Mhrrrr, I can't go back\x01",
            "to the Empire until the\x01",
            "end of the day!?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "Tch, State Guard my ass!\x01",
            "They just spout whatever\x01",
            "they want!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35FA")

    label("loc_343A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_34E3")

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "Who would've ever thought\x01",
            "there'd be an attack on\x01",
            "Crossbell City...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "Did we do something...?\x01",
            "I've had enough of\x01",
            "things like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35FA")

    label("loc_34E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3591")

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "National independence, huh... To\x01",
            "think the day when something like\x01",
            "that was proposed would come...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "Anyhow, I hope it can be\x01",
            "realized.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35FA")

    label("loc_3591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_35FA")

    ChrTalk(
        0xFE,
        (
            "Oh, what a... What a\x01",
            "fine townscape!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I'm feeling so\x01",
            "excited in spite of my\x01",
            "age!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35FA")

    TalkEnd(0xFE)
    Return()

    # Function_8_338D end

    def Function_9_35FE(): pass

    label("Function_9_35FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3671")

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "Dear, please, calm\x01",
            "down...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "Anyway, let's hurry and\x01",
            "buy our tickets.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B8")

    label("loc_3671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_36CD")

    ChrTalk(
        0xFE,
        (
            "Several ambulances passed\x01",
            "by... W-What could all\x01",
            "the commotion be about?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B8")

    label("loc_36CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3733")

    ChrTalk(
        0xFE,
        (
            "Crossbell is a big\x01",
            "place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish I had bought at\x01",
            "least one sightseeing\x01",
            "guide.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B8")

    label("loc_3733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_37B8")

    ChrTalk(
        0xFE,
        (
            "My husband is enjoying\x01",
            "it very much, but I'm\x01",
            "worried somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, isn't\x01",
            "Crossbell called the\x01",
            ""Demon City"?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B8")

    TalkEnd(0xFE)
    Return()

    # Function_9_35FE end

    def Function_10_37BC(): pass

    label("Function_10_37BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_38AE")

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "Losing my job in Crossbell\x01",
            "hurts, but it's worse not being\x01",
            "able to return to my hometown.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "I can't sit still in this situation.\x01",
            "Before anything strange happens, I\x01",
            "have to get away from Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39D6")

    label("loc_38AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3934")

    ChrTalk(
        0xFE,
        (
            "Occupation by an armed\x01",
            "group... Why on earth\x01",
            "did such an incident...?\x02",
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
    Jump("loc_39D6")

    label("loc_3934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_39D6")

    ChrTalk(
        0xFE,
        (
            "Uhhhm, where's the hotel\x01",
            "I reserved for today...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I splurged on lodging in\x01",
            "Entertainment District. I've got\x01",
            "to enjoy this trip to the fullest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39D6")

    TalkEnd(0xFE)
    Return()

    # Function_10_37BC end

    def Function_11_39DA(): pass

    label("Function_11_39DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3A72")

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "I got a recall notice\x01",
            "from the Empire the\x01",
            "other day...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "*sigh*. I'd become fond\x01",
            "of living in\x01",
            "Crossbell...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B87")

    label("loc_3A72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3AF4")

    ChrTalk(
        0xFE,
        (
            "I'm worried that armed\x01",
            "group could come to\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Won't the CGF do\x01",
            "something about it\x01",
            "quickly for us?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B87")

    label("loc_3AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3B87")

    ChrTalk(
        0xFE,
        (
            "Haha. What am I going to\x01",
            "do with you, being in\x01",
            "such high spirits...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I feel I\x01",
            "understand. Crossbell is\x01",
            "an amazing city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B87")

    TalkEnd(0xFE)
    Return()

    # Function_11_39DA end

    def Function_12_3B8B(): pass

    label("Function_12_3B8B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3C12")

    ChrTalk(
        0xFE,
        (
            "I intend to leave\x01",
            "Crossbell at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want to remain in\x01",
            "such a dangerous place\x01",
            "even a second longer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D29")

    label("loc_3C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3C9F")

    ChrTalk(
        0xFE,
        (
            "They say "independence",\x01",
            "but I still don't quite\x01",
            "know what that is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll look into\x01",
            "it before election\x01",
            "day...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D29")

    label("loc_3C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3D29")

    ChrTalk(
        0xFE,
        (
            "This morning's crowds\x01",
            "were really something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All those gorgeous limousines\x01",
            "coming and going... Those are\x01",
            "VIPs for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D29")

    TalkEnd(0xFE)
    Return()

    # Function_12_3B8B end

    def Function_13_3D2D(): pass

    label("Function_13_3D2D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3DDD")

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "What should I do... The\x01",
            "grounds are too crowded\x01",
            "and I can't get inside.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "Ooh. Will I really be\x01",
            "able to return to the\x01",
            "Republic...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E54")

    label("loc_3DDD")


    ChrTalk(
        0xFE,
        (
            "I saw the unveiling\x01",
            "ceremony from the\x01",
            "department store rooftop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aah, I looked directly\x01",
            "at Lady Julia's face!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E54")

    TalkEnd(0xFE)
    Return()

    # Function_13_3D2D end

    def Function_14_3E58(): pass

    label("Function_14_3E58")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3ED1")

    ChrTalk(
        0xFE,
        (
            "Hey, hey, why do we have\x01",
            "to go home to the\x01",
            "Empire...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And just when I made so\x01",
            "many friends...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4020")

    label("loc_3ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3F59")

    ChrTalk(
        0xFE,
        (
            "When we played at the train station\x01",
            "I made the station attendant mad\x01",
            "and we were thrown out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Tch, party-pooper.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4020")

    label("loc_3F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3FCC")

    ChrTalk(
        0xFE,
        (
            "Alright, then let's play\x01",
            "hide and seek inside the\x01",
            "station today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. I'll be "it"\x01",
            "first.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4020")

    label("loc_3FCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4020")

    ChrTalk(
        0xFE,
        (
            "Wooow, so this is\x01",
            "Crossbell!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, hey, quick, let's\x01",
            "go mamaaa!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4020")

    TalkEnd(0xFE)
    Return()

    # Function_14_3E58 end

    def Function_15_4024(): pass

    label("Function_15_4024")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_40CF")

    ChrTalk(
        0xFE,
        (
            "Geez, big brother...\x01",
            "That's why I told you to\x01",
            "cut it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...However, the station\x01",
            "attendants really looked busy.\x01",
            "Could something have happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4160")

    label("loc_40CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4126")

    ChrTalk(
        0xFE,
        (
            "Eeeh, let's not, big\x01",
            "brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The station people will\x01",
            "get mad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4160")

    label("loc_4126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4160")

    ChrTalk(
        0xFE,
        (
            "I wanna play at the\x01",
            "casino with father too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4160")

    TalkEnd(0xFE)
    Return()

    # Function_15_4024 end

    def Function_16_4164(): pass

    label("Function_16_4164")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_420F")

    ChrTalk(
        0xFE,
        (
            "I wonder how the\x01",
            "terrorists will try to\x01",
            "enter Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There shouldn't be blind spots\x01",
            "but... Anyway, at present, we\x01",
            "can only stay vigilant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_420F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_429E")

    ChrTalk(
        0xFE,
        (
            "Phew, the unveiling ceremony\x01",
            "ended. I feel like a weight\x01",
            "has lifted off my shoulders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I can't relax\x01",
            "just yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_429E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4383")

    ChrTalk(
        0xFE,
        (
            "Inside the station and the airport\x01",
            "there are a considerable number of\x01",
            "detectives from Section Two on duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Including the rest of it, I can't\x01",
            "remember such a solid security\x01",
            "structure ever being deployed before.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4383")

    TalkEnd(0xFE)
    Return()

    # Function_16_4164 end

    def Function_17_4387(): pass

    label("Function_17_4387")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_441C")

    ChrTalk(
        0xFE,
        (
            "I came to see off my wife and\x01",
            "daughter who're returning\x01",
            "home to the Empire, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think, a derailment\x01",
            "accident...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4451")

    label("loc_441C")


    ChrTalk(
        0xFE,
        (
            "W-What if my wife and\x01",
            "daughter were on\x01",
            "board...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4451")

    TalkEnd(0xFE)
    Return()

    # Function_17_4387 end

    def Function_18_4455(): pass

    label("Function_18_4455")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "My Goddess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder how severe the\x01",
            "damage was...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_4455 end

    def Function_19_449A(): pass

    label("Function_19_449A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Are the trains not\x01",
            "running?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, this means that I\x01",
            "can stay together with\x01",
            "papa today too!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_449A end

    def Function_20_4506(): pass

    label("Function_20_4506")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Service at Crossbell\x01",
            "Station will be\x01",
            "suspended after today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, at present, the date\x01",
            "for resumption of service\x01",
            "has not been decided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Foreigners who wish to return\x01",
            "to their home countries are\x01",
            "asked to please hurry.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_4506 end

    def Function_21_45F4(): pass

    label("Function_21_45F4")

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

    def lambda_4911():
        OP_9B(0x1, 0xFE, 0x0, 0x30D40, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_4911)
    BeginChrThread(0x21, 0, 0, 22)
    Sleep(5000)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_45F4 end

    def Function_22_4948(): pass

    label("Function_22_4948")

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

    # Function_22_4948 end

    def Function_23_49AD(): pass

    label("Function_23_49AD")

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

    # Function_23_49AD end

    def Function_24_49EE(): pass

    label("Function_24_49EE")

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
            "─For too many years they have\x01",
            "treated Crossbell as their own\x01",
            ""province".\x02\x03",
            "No matter which crimes they\x01",
            "commit, we have no right to solve\x01",
            "them.\x02\x03",
            "And even now... We continue to be\x01",
            "exploited in ways which snatch\x01",
            "abundant revenues from us.\x02",
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
            "#4S─However, that is not\x01",
            "all!\x02\x03",
            "#4SWe've come to a point\x01",
            "where even our very\x01",
            "lives are threatened!\x02",
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

    # Function_24_49EE end

    def Function_25_4EB3(): pass

    label("Function_25_4EB3")

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

    def lambda_4F87():
        OP_97(0x101, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4F87)
    Sleep(100)

    def lambda_4FA4():
        OP_97(0x102, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4FA4)
    Sleep(100)

    def lambda_4FC1():
        OP_97(0x103, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4FC1)
    Sleep(100)

    def lambda_4FDE():
        OP_97(0x104, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4FDE)
    Sleep(100)

    def lambda_4FFB():
        OP_97(0x105, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4FFB)
    Sleep(100)

    def lambda_5018():
        OP_97(0x109, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5018)
    Sleep(100)

    def lambda_5035():
        OP_97(0x106, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5035)
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
            "#11P#00006FI'd like to get ahold of\x01",
            "chief and the others\x01",
            "somehow, but...\x02\x03",
            "#00013FWhat's this...? This\x01",
            "bluish mist?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108FIt looks like what\x01",
            "appeared at the temple\x01",
            "and tower...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5PThere's... no pedestrian\x01",
            "traffic at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10408FWell, because fighting is taking\x01",
            "place outside the city, they\x01",
            "might've taken refuge somewhere...\x02",
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

    def lambda_52CE():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_52CE)
    Sleep(30)

    def lambda_52DE():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_52DE)
    Sleep(30)

    def lambda_52EE():
        TurnDirection(0x106, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_52EE)
    Sleep(30)

    def lambda_52FE():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_52FE)
    Sleep(30)

    def lambda_530E():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_530E)
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
            "#12P#00203F...I hear a resonance\x01",
            "from Central Square.\x02\x03",
            "#00201FIt's that great bell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00007FWhat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10701FLet's go have a look.\x02",
    )

    CloseMessageWindow()

    def lambda_53EE():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_53EE)
    Sleep(30)

    def lambda_53FE():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_53FE)
    Sleep(30)

    def lambda_540E():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_540E)
    Sleep(30)

    def lambda_541E():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_541E)
    Sleep(30)

    def lambda_542E():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_542E)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_68(500, 1200, 7500, 3000)
    MoveCamera(37, 21, 0, 3000)
    SetCameraDistance(20500, 3000)

    def lambda_5477():
        OP_97(0x101, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5477)
    Sleep(100)

    def lambda_5494():
        OP_97(0x102, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5494)
    Sleep(100)

    def lambda_54B1():
        OP_97(0x103, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_54B1)
    Sleep(100)

    def lambda_54CE():
        OP_97(0x104, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_54CE)
    Sleep(100)

    def lambda_54EB():
        OP_97(0x105, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_54EB)
    Sleep(100)

    def lambda_5508():
        OP_97(0x109, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5508)
    Sleep(100)

    def lambda_5525():
        OP_97(0x106, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5525)
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

    # Function_25_4EB3 end

    def Function_26_5573(): pass

    label("Function_26_5573")

    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_26_5573 end

    def Function_27_5585(): pass

    label("Function_27_5585")

    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1100)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_27_5585 end

    def Function_28_559A(): pass

    label("Function_28_559A")

    Sleep(500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_28_559A end

    def Function_29_55AF(): pass

    label("Function_29_55AF")

    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_29_55AF end

    def Function_30_55BA(): pass

    label("Function_30_55BA")

    Sleep(500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_30_55BA end

    def Function_31_55C5(): pass

    label("Function_31_55C5")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_31_55C5 end

    def Function_32_55D7(): pass

    label("Function_32_55D7")

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
            "#00003F(...I don't know how much\x01",
            "time Kilika and Captain\x01",
            "Lechter's talk will take.)\x02\x03",
            "#00001F(It's before the operation.\x01",
            "If there's anything we need\x01",
            "to do, we should do it now.)\x02",
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
            "If you proceed with the events past this point,\x01",
            "you will infiltrate Orchis Tower and will no\x01",
            "longer be able to freely move about the city.\x07\x00\x02",
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
            "Enter the Station\x01",          # 0
            "Finish Other Business\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5854"),
        (1, "loc_59B4"),
        (SWITCH_DEFAULT, "loc_59E6"),
    )


    label("loc_5854")

    OP_68(8400, 1900, -1900, 1500)
    MoveCamera(90, 13, 0, 1500)

    def lambda_5875():
        OP_96(0xFE, 0x2328, 0xFA, 0xFFFFF894, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5875)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    SetCameraDistance(17500, 3000)

    def lambda_58B9():
        OP_97(0x101, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_58B9)
    Sleep(50)

    def lambda_58D6():
        OP_97(0x103, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_58D6)
    Sleep(50)

    def lambda_58F3():
        OP_97(0x102, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_58F3)
    Sleep(50)

    def lambda_5910():
        OP_97(0x104, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5910)
    Sleep(50)

    def lambda_592D():
        OP_97(0xF4, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_592D)
    Sleep(50)

    def lambda_594A():
        OP_97(0xF5, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_594A)
    Sleep(300)
    FadeToDark(2000, 0, -1)

    def lambda_5971():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5971)
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
    Jump("loc_59E6")

    label("loc_59B4")

    SetChrPos(0x0, 6500, 0, -2000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_E2(0x2)
    EventEnd(0x5)
    Jump("loc_59E6")

    label("loc_59E6")

    Return()

    # Function_32_55D7 end

    def Function_33_59E7(): pass

    label("Function_33_59E7")

    TalkBegin(0x8)

    ChrTalk(
        0x8,
        (
            "Just now, an Empire-made\x01",
            "black transport went\x01",
            "towards Central Square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Where did it go after\x01",
            "that, you ask? I'm\x01",
            "sorry, I don't know.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_33_59E7 end

    def Function_34_5A7F(): pass

    label("Function_34_5A7F")

    EventBegin(0x1)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)
    Return()

    # Function_34_5A7F end

    def Function_35_5A95(): pass

    label("Function_35_5A95")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5AFA")

    ChrTalk(
        0x101,
        (
            "#00000FThis is Crossbell Station.\x01",
            "...We don't have any\x01",
            "business here right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CF5")

    label("loc_5AFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5B56")
    Sound(807, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The doors are firmly\x01",
            "locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 5)
    Jump("loc_5BE6")

    label("loc_5B56")


    ChrTalk(
        0x101,
        (
            "#00001F...It appears the station\x01",
            "has been sealed off.\x02\x03",
            "#00003FWell, we don't have any\x01",
            "special business here, so\x01",
            "let's leave this place be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BE6")

    SetScenarioFlags(0x1CE, 4)
    Jump("loc_5CF5")

    label("loc_5BEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5C8F")

    ChrTalk(
        0x101,
        (
            "#00001F...The premises are packed\x01",
            "with foreigners returning\x01",
            "to their home countries.\x02\x03",
            "#00003FI think it's best if we\x01",
            "pass on going inside.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    Jump("loc_5CF5")

    label("loc_5C8F")


    ChrTalk(
        0x101,
        (
            "#00000FThis is Crossbell Station.\x01",
            "...I don't think we don't have\x01",
            "any business here right now.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)

    label("loc_5CF5")

    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)
    Return()

    # Function_35_5A95 end

    def Function_36_5D09(): pass

    label("Function_36_5D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DF3")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D94")

    ChrTalk(
        0x101,
        (
            "#00000FThe south exit is this\x01",
            "way.\x02\x03",
            "We don't have any\x01",
            "special business this\x01",
            "way, so let's not exit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5DE0")

    label("loc_5D94")


    ChrTalk(
        0x101,
        (
            "#00000FWe don't have any\x01",
            "special business this\x01",
            "way, so let's not exit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DE0")

    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_5DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F05")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E89")

    ChrTalk(
        0x101,
        (
            "#00001FThe south exit is this way.\x02\x03",
            "For now, let's focus on\x01",
            "accident investigation\x01",
            "without taking any detours.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5EF2")

    label("loc_5E89")


    ChrTalk(
        0x101,
        (
            "#00001FWe don't have any special\x01",
            "business this way. For now, let's\x01",
            "focus on accident investigation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EF2")

    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_5F05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F7E")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FWe've got to chase after\x01",
            "Randy... This is no time\x01",
            "to be wandering around.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_5F7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FE8")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FThis is no time to be\x01",
            "leaving the city. Let's\x01",
            "turn around.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_5FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60B9")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FWe've come this far. There's no way\x01",
            "we're leaving the city now.\x02\x03",
            "The Orchis Tower infiltration\x01",
            "operation... We have to do whatever\x01",
            "it takes to make it a success.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_60B9")

    Return()

    # Function_36_5D09 end

    def Function_37_60BA(): pass

    label("Function_37_60BA")

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

    # Function_37_60BA end

    SaveToFile()

Try(main)
