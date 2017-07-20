from ScenarioHelper import *

def main():
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
        "Lid",                 # 1
        "Billy",                 # 2
        "Claris",               # 3
        "tourist",                 # 4
        "tourist",                 # 5
        "tourist",                 # 6
        "tourist",                 # 7
        "tourist",                 # 8
        "tourist",                 # 9
        "boy",                 # 10
        "girl",                 # 11
        "Policeman",                   # 12
        "Defense Forces soldier",             # 13
        "Mercy",               # 14
        "sepia",                 # 15
        "Ohna",                 # 16
        "car",                     # 17
        "Defense Forces soldier",             # 18
        "Defense Forces soldier",             # 19
        "Policeman",                   # 20
        "Policeman",                   # 21
        "Policeman",                   # 22
        "Policeman",                   # 23
        "Policeman",                   # 24
        "Policeman",                   # 25
        "train",                   # 26
        "SE control",                 # 27
        "Central square",               # 28
        "Nishi dori",                 # 29
        "Administrative district",                 # 30
        "Residential area",                 # 31
        "Entertainment district",                 # 32
        "East Street",                 # 33
        "old Town",                 # 34
        "Harbor district",                 # 35
        "IBC",                 # 36
        "Beside the station",               # 37
        "Back street",                 # 38
        "Ursula interchange",           # 39
        "East Crossbell Highway",       # 40
        "West Crossbell Highway",       # 41
        "Mainz Mountain Road",           # 42
        "Orchis Tower",         # 43
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

    PlaceName(-9.25, 0.0, 67.0, 0x0000, 0x0000, "Central square")
    PlaceName(-75.0, 0.0, 71.5, 0x0000, 0x0000, "Nishi dori")
    PlaceName(17.75, 0.0, 156.0, 0x0000, 0x0000, "Administrative district")
    PlaceName(-136.0, 0.0, 146.0, 0x0000, 0x0000, "Residential area")
    PlaceName(-63.0, 0.0, 138.0, 0x0000, 0x0000, "Entertainment district")
    PlaceName(72.0, 0.0, 44.0, 0x0000, 0x0000, "East Street")
    PlaceName(107.5, 0.0, -11.0, 0x0000, 0x0000, "old Town")
    PlaceName(100.0, 0.0, 110.0, 0x0000, 0x0000, "Harbor district")
    PlaceName(74.0, 0.0, 204.0, 0x0000, 0x0000, "IBC")
    PlaceName(2.0, 0.0, -2.0, 0x0000, 0x0000, "Beside the station")
    PlaceName(-45.0, 0.0, 102.0, 0x0000, 0x0000, "Back street")
    PlaceName(-1.0, 0.0, -33.0, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(126.0, 0.0, 58.0, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-126.0, 0.0, 70.0, 0x0000, 0x0000, "West Crossbell Highway")
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
        "Function_6_252F",         # 06, 6
        "Function_7_2CD8",         # 07, 7
        "Function_8_2F1B",         # 08, 8
        "Function_9_3136",         # 09, 9
        "Function_10_32F6",        # 0A, 10
        "Function_11_34BB",        # 0B, 11
        "Function_12_364C",        # 0C, 12
        "Function_13_37C4",        # 0D, 13
        "Function_14_38AD",        # 0E, 14
        "Function_15_3A57",        # 0F, 15
        "Function_16_3B8B",        # 10, 16
        "Function_17_3D7C",        # 11, 17
        "Function_18_3E11",        # 12, 18
        "Function_19_3E5B",        # 13, 19
        "Function_20_3EAB",        # 14, 20
        "Function_21_3F61",        # 15, 21
        "Function_22_42B5",        # 16, 22
        "Function_23_431A",        # 17, 23
        "Function_24_435B",        # 18, 24
        "Function_25_481A",        # 19, 25
        "Function_26_4E93",        # 1A, 26
        "Function_27_4EA5",        # 1B, 27
        "Function_28_4EBA",        # 1C, 28
        "Function_29_4ECF",        # 1D, 29
        "Function_30_4EDA",        # 1E, 30
        "Function_31_4EE5",        # 1F, 31
        "Function_32_4EF7",        # 20, 32
        "Function_33_52AD",        # 21, 33
        "Function_34_533A",        # 22, 34
        "Function_35_5350",        # 23, 35
        "Function_36_5559",        # 24, 36
        "Function_37_5857",        # 25, 37
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1584")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D5")

    ChrTalk(
        0xFE,
        (
            "Since that day of declaration of independence,\x01",
            "Transcontinental railway operates\x01",
            "I have stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even without it, in the empire\x01",
            "The civil war began, even in the Republic there was a depression\x01",
            "It seems to be happening ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, I can watch the train\x01",
            "I wonder if the peaceful era has ended.\x01",
            "There is no such thing as sadness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_157F")

    label("loc_14D5")


    ChrTalk(
        0xFE,
        (
            "Since that day of declaration of independence,\x01",
            "Transcontinental railway operates\x01",
            "I have stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, I can watch the train\x01",
            "I wonder if the peaceful era has ended.\x01",
            "There is no such thing as sadness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157F")

    Jump("loc_252B")

    label("loc_1584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1592")
    Jump("loc_252B")

    label("loc_1592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_16E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1652")

    ChrTalk(
        0xFE,
        (
            "Finally today,\x01",
            "Traveling across the continental railway for a while\x01",
            "It seems to stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wow, my worthwhile ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hurry up and resolve everything,\x01",
            "I would like you to resume early.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16E3")

    label("loc_1652")


    ChrTalk(
        0xFE,
        (
            "Uh, my worthworking\x01",
            "Transcontinental railway operation\x01",
            "I will not stop today …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hurry up and resolve everything,\x01",
            "I would like you to resume early.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E3")

    Jump("loc_252B")

    label("loc_16E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_18AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1804")

    ChrTalk(
        0xFE,
        (
            "Rumor, the incident of the recent incident\x01",
            "Is not it an empire's work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps it was happening recently\x01",
            "A derailment accident and occupation cases of Mainz also\x01",
            "Is it because of the empire …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is a country going the cutting edge of railway technology\x01",
            "I want to believe it is kind of damn ……\x01",
            "There is no doubt if it is doubtful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18AA")

    label("loc_1804")


    ChrTalk(
        0xFE,
        (
            "Perhaps,\x01",
            "The recent incident was\x01",
            "Is it because of the empire …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is a country going the cutting edge of railway technology\x01",
            "I want to believe it is kind of damn ……\x01",
            "There is no doubt if it is doubtful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18AA")

    Jump("loc_252B")

    label("loc_18AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_195D")

    ChrTalk(
        0xFE,
        (
            "From the train derailment accident\x01",
            "Even though it is not so long ago,\x01",
            "What does occupation happen …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It feels kind of unpleasant.\x01",
            "To have the incident go on so long,\x01",
            "Is it really a coincidence …?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_252B")

    label("loc_195D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1AA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A25")

    ChrTalk(
        0xFE,
        (
            "The transit railroad was able to recover in one night\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to everyone today\x01",
            "I can feel the train ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He took the work all night.\x01",
            "There is no word of gratitude to the guard!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A9F")

    label("loc_1A25")


    ChrTalk(
        0xFE,
        (
            "Thanks to everyone today\x01",
            "I can feel the train ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He took the work all night.\x01",
            "There is no word of gratitude to the guard!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A9F")

    Jump("loc_252B")

    label("loc_1AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1B2A")

    ChrTalk(
        0xFE,
        (
            "Wow, what a thing.\x01",
            "It's a derailment accident … …! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess the train is safe, too ….\x01",
            "I am worried about my heart.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_252B")

    label("loc_1B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1CC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C21")

    ChrTalk(
        0xFE,
        (
            "Anything yesterday, from the station's home\x01",
            "To jump on the roof of the train\x01",
            "It seems there was a case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand the feeling … ….\x01",
            "It is an unforgivable act as a railway enthusiast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Doing a crazy ride and hurting the train,\x01",
            "It is terrible to annoy the passengers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CBC")

    label("loc_1C21")


    ChrTalk(
        0xFE,
        (
            "Anything yesterday, from the station's home\x01",
            "To jump on the roof of the train\x01",
            "It seems there was a case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Doing a crazy ride and hurting the train,\x01",
            "It is terrible to annoy the passengers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CBC")

    Jump("loc_252B")

    label("loc_1CC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1E45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC0")

    ChrTalk(
        0xFE,
        (
            "To be independent\x01",
            "What merit is there?\x01",
            "Specifically, I do not quite understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For anything, the Empire and the Republic\x01",
            "Things like turning to enemies\x01",
            "I wish you would like to have a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that it is a transit railroad\x01",
            "After stopping,\x01",
            "I can not live.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E40")

    label("loc_1DC0")


    ChrTalk(
        0xFE,
        (
            "Empire and Republic\x01",
            "To turn to the enemy are\x01",
            "I want you to forgive me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Transit railway caused by independence\x01",
            "After stopping,\x01",
            "I can not live.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E40")

    Jump("loc_252B")

    label("loc_1E45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1F8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F04")

    ChrTalk(
        0xFE,
        (
            "The trade meeting in me,\x01",
            "\"Eisengraf issue\"\x01",
            "Just looking at it ended in eight percent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that the schedule is over\x01",
            "A figure of running away from the crossbell\x01",
            "It is enough if you can see it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F89")

    label("loc_1F04")


    ChrTalk(
        0xFE,
        (
            "The trade meeting within me,\x01",
            "Look at \"Eisengraf\"\x01",
            "It is over 80 finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, today I am at home and a book\x01",
            "I guess I should read it ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F89")

    Jump("loc_252B")

    label("loc_1F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_21A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F2")

    ChrTalk(
        0xFE,
        (
            "Ah ah …… That one, that is\x01",
            "Imperial government dedicated power train,\x01",
            "Is it \"Eisengruf\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, as if to show the mighty power of the empire,\x01",
            "Heavy design based on red like fire … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "\"Earl of Iron#8REisengraf#I am not ashamed of the name of\x01",
            "You can say it is a wonderful train!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For this day the camera\x01",
            "I wish I could have bought it …!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21A3")

    label("loc_20F2")


    ChrTalk(
        0xFE,
        (
            "The train exclusively for that imperial government,\x01",
            "\"Earl of Iron#8REisengraf#I am not ashamed of the name of\x01",
            "You can say it is a wonderful train!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, what a nice day.\x01",
            "You do not have to die anymore! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21A3")

    Jump("loc_252B")

    label("loc_21A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_233A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B0")

    ChrTalk(
        0xFE,
        (
            "Western Zemria Trade Council ……\x01",
            "I heard that the leaders of the empire will also come,\x01",
            "I can not miss as a railroad mania.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, the Imperial Government\x01",
            "I have a dedicated power train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a leader of the empire\x01",
            "Absolutely it should ride it ……\x01",
            "Well, I'm looking forward to it now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2335")

    label("loc_22B0")


    ChrTalk(
        0xFE,
        (
            "Imperial government is dedicated\x01",
            "I have a driving train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the unveiling ceremony of tomorrow, surely\x01",
            "It must be riding it.\x01",
            "Well, I'm looking forward to it now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2335")

    Jump("loc_252B")

    label("loc_233A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_23B9")

    ChrTalk(
        0xFE,
        "Weather has nothing to do with train mania activities.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The train which is wet in the rain is also good.\x01",
            "That is exactly how water drips too, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_252B")

    label("loc_23B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_252B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_249A")

    ChrTalk(
        0xFE,
        (
            "Today as well, the transcontinental railroad\x01",
            "It seems that it operates well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A truly luxurious form,\x01",
            "It looks like the Sokyu was reflected as it was\x01",
            "Beautiful coloring ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it is always great to see it.\x01",
            "It was nice to have done railway mania.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_252B")

    label("loc_249A")


    ChrTalk(
        0xFE,
        (
            "A truly luxurious form,\x01",
            "It looks like the Sokyu was reflected as it was\x01",
            "Beautiful coloring ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it is always great to see it.\x01",
            "It was nice to have done railway mania.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_252B")

    TalkEnd(0xFE)
    Return()

    # Function_5_138B end

    def Function_6_252F(): pass

    label("Function_6_252F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_26B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2618")

    ChrTalk(
        0xFE,
        (
            "Material left over in Crossbell City\x01",
            "I decided to go distribute to various places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now almost no foreign goods come in,\x01",
            "It will have its limit, though ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a shipper, what you can do first\x01",
            "I have to do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26AF")

    label("loc_2618")


    ChrTalk(
        0xFE,
        (
            "Now almost no foreign goods come in,\x01",
            "To distribute goods to various places\x01",
            "There will be a limit, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a shipper, what you can do first\x01",
            "I have to do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26AF")

    Jump("loc_2CD4")

    label("loc_26B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_26C2")
    Jump("loc_2CD4")

    label("loc_26C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_274A")

    ChrTalk(
        0xFE,
        (
            "Hey, what is it?\x01",
            "It became a serious thing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that the operation of the railroad is also stopped,\x01",
            "What about circulation with foreign countries?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD4")

    label("loc_274A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2758")
    Jump("loc_2CD4")

    label("loc_2758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_27EB")

    ChrTalk(
        0xFE,
        (
            "No way in the cross-bell autonomous province\x01",
            "Occupation cases are\x01",
            "I wake up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that the guard is also struggling,\x01",
            "What will it become ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD4")

    label("loc_27EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_27F9")
    Jump("loc_2CD4")

    label("loc_27F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2807")
    Jump("loc_2CD4")

    label("loc_2807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2898")

    ChrTalk(
        0xFE,
        (
            "You guys,\x01",
            "Misplaced luggage of Kapua Express\x01",
            "Did he report it back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, I was relieved.\x01",
            "As expected, the Special Affairs Division should not be counted on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD4")

    label("loc_2898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_294E")

    ChrTalk(
        0xFE,
        (
            "Because unknown monsters are out,\x01",
            "Be careful with the traffic of the highway\x01",
            "There was notice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The carriers like us are\x01",
            "Especially since there are many people coming and going,\x01",
            "After all I am concerned with demon animals.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD4")

    label("loc_294E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_29B5")

    ChrTalk(
        0xFE,
        "Well, I guess I will go to delivery soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you do not bring it with papa,\x01",
            "I'm getting scolded by my father.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CD4")

    label("loc_29B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2B65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AAC")

    ChrTalk(
        0xFE,
        (
            "Receive your baggage quickly\x01",
            "Even though I have to go to the delivery,\x01",
            "I am late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Loading of freight trains also quite strictly\x01",
            "I wonder what is being checked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A great man from the empire came,\x01",
            "Speaking of which it can not be helped, it can not be helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B60")

    label("loc_2AAC")


    ChrTalk(
        0xFE,
        (
            "Receive your baggage quickly\x01",
            "Even though I have to go to the delivery,\x01",
            "I am late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A great man from the empire came.\x01",
            "The check would have become tough as well,\x01",
            "Speaking of which it can not be helped, it can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B60")

    Jump("loc_2CD4")

    label("loc_2B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2B73")
    Jump("loc_2CD4")

    label("loc_2B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2B81")
    Jump("loc_2CD4")

    label("loc_2B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2CD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C68")

    ChrTalk(
        0xFE,
        (
            "My house says Rhys shipping\x01",
            "It is a privately operated transport company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oyaji is the president's young company,\x01",
            "With kindness, politeness and speedy motto\x01",
            "I am doing my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the case of your order,\x01",
            "Please contact me by all means.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CD4")

    label("loc_2C68")


    ChrTalk(
        0xFE,
        (
            "My house says Rhys shipping\x01",
            "It is a privately operated transport company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the case of your order,\x01",
            "Please contact me by all means.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD4")

    TalkEnd(0xFE)
    Return()

    # Function_6_252F end

    def Function_7_2CD8(): pass

    label("Function_7_2CD8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EA1")

    ChrTalk(
        0xFE,
        "Oh, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FAh … … Mother.\x01",
            "From now on to visit Franc?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, changing the francs\x01",
            "I'm going to deliver it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How was he / she was?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FYeah, still nothing\x01",
            "It looks tired, but ….\x01",
            "Tomorrow I'm fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, that was nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, until that child got better\x01",
            "I am planning to go to visit frequently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, leave it to me\x01",
            "You know your work\x01",
            "Do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYeah, I know.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 7)
    Jump("loc_2F17")

    label("loc_2EA1")


    ChrTalk(
        0xFE,
        (
            "Noel, your second division of support department\x01",
            "It is the end of today, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At least not to have regrets\x01",
            "Please work firmly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F17")

    TalkEnd(0xFE)
    Return()

    # Function_7_2CD8 end

    def Function_8_2F1B(): pass

    label("Function_8_2F1B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2FAA")

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "Absurd, if you miss today\x01",
            "If you can not return to the empire …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "Eh, what is the Defense Forces!\x01",
            "Just get rid of things that are selfish!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3132")

    label("loc_2FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3044")

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "No way Cross Bell City\x01",
            "I do not think that it will be in case of an attack or … …\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "What did we do …?\x01",
            "I'm sorry for such a thing anymore.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3132")

    label("loc_3044")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_30CB")

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "Is it state independent?\x01",
            "The day when such a thing is advocated\x01",
            "I will come … …\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Citizen",
        (
            "In any case, realize it\x01",
            "It is what you want.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3132")

    label("loc_30CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3132")

    ChrTalk(
        0xFE,
        (
            "Oh, how ……\x01",
            "What a splendid city skyline!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe\x01",
            "I was excited!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3132")

    TalkEnd(0xFE)
    Return()

    # Function_8_2F1B end

    def Function_9_3136(): pass

    label("Function_9_3136")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_31B0")

    NpcTalk(
        0xFE,
        "Foreigner",
        "Grandfather, please calm down … …\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "Anyway, get the tickets as soon as possible\x01",
            "Let's go buy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32F2")

    label("loc_31B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3201")

    ChrTalk(
        0xFE,
        (
            "A lot of ambulances passed … …\x01",
            "What on earth is it all about?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32F2")

    label("loc_3201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_326F")

    ChrTalk(
        0xFE,
        (
            "What is crossbell?\x01",
            "After all it is wide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even one of the tour guide\x01",
            "I should have bought it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32F2")

    label("loc_326F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_32F2")

    ChrTalk(
        0xFE,
        (
            "My grandfather is very pleased,\x01",
            "I am worried about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it's a crossbell\x01",
            "Is it called \"Mago\"?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F2")

    TalkEnd(0xFE)
    Return()

    # Function_9_3136 end

    def Function_10_32F6(): pass

    label("Function_10_32F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_33B0")

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "Losing the job at the crossbell hurts,\x01",
            "I'm better than going home.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "In this case, you do not have to sit down.\x01",
            "Before getting caught up in strange things\x01",
            "I should leave the crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34B7")

    label("loc_33B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3430")

    ChrTalk(
        0xFE,
        (
            "It is occupation by an armed group,\x01",
            "What on earth are these incidents ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if Mainz is safe,\x01",
            "I am worried ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34B7")

    label("loc_3430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34B7")

    ChrTalk(
        0xFE,
        (
            "Well, I made a reservation today.\x01",
            "Where is the hotel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got excited and made it to an accommodation in the red light district.\x01",
            "I hope to enjoy traveling abundantly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34B7")

    TalkEnd(0xFE)
    Return()

    # Function_10_32F6 end

    def Function_11_34BB(): pass

    label("Function_11_34BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3548")

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "In the meantime, from the empire\x01",
            "A notice of withdrawal has arrived ……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "Hello, life in Crossbell\x01",
            "I liked it ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3648")

    label("loc_3548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_35C8")

    ChrTalk(
        0xFE,
        (
            "I am an armed group\x01",
            "I am worried that he will not come to the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The guard will soon\x01",
            "I wonder if you manage somehow ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3648")

    label("loc_35C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3648")

    ChrTalk(
        0xFE,
        (
            "Huhu, if you got this kid\x01",
            "It's such awesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I feel I can understand.\x01",
            "Crossbell is amazing\x01",
            "It is a city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3648")

    TalkEnd(0xFE)
    Return()

    # Function_11_34BB end

    def Function_12_364C(): pass

    label("Function_12_364C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_36C7")

    ChrTalk(
        0xFE,
        (
            "From Crossbell\x01",
            "I am planning to leave quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Already in such a dangerous place\x01",
            "I do not want to stay even for one second.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37C0")

    label("loc_36C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3754")

    ChrTalk(
        0xFE,
        (
            "Even if I say independence,\x01",
            "What are you doing wrong?\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before the referendum day comes,\x01",
            "Let's investigate a bit … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37C0")

    label("loc_3754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_37C0")

    ChrTalk(
        0xFE,
        "The bustle of this morning was amazing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Transfer at such a luxurious limousine,\x01",
            "As expected, they are VIPs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37C0")

    TalkEnd(0xFE)
    Return()

    # Function_12_364C end

    def Function_13_37C4(): pass

    label("Function_13_37C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3847")

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "What should I do……\x01",
            "The campus is too busy to enter inside.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Foreigner",
        (
            "Uu, properly in the Republic\x01",
            "I wonder if I can go home …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38A9")

    label("loc_3847")


    ChrTalk(
        0xFE,
        (
            "Unveiling ceremony from the rooftop of department store\x01",
            "You saw it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, I'm sorry for having Yuria-sama's face\x01",
            "I wanted to see you directly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38A9")

    TalkEnd(0xFE)
    Return()

    # Function_13_37C4 end

    def Function_14_38AD(): pass

    label("Function_14_38AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3924")

    ChrTalk(
        0xFE,
        (
            "Hey, why to the Empire\x01",
            "You have to go home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A lot of my friends\x01",
            "I could have done it ~ ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A53")

    label("loc_3924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_398D")

    ChrTalk(
        0xFE,
        (
            "If you were playing at the station, to the station staff\x01",
            "I got scolded and got picked up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, it is stingy ~.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A53")

    label("loc_398D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_39FC")

    ChrTalk(
        0xFE,
        (
            "Well then, then then today\x01",
            "Shall I see a hide-and-seek in the station?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hello, initially Eura is oni ~.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A53")

    label("loc_39FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3A53")

    ChrTalk(
        0xFE,
        "Wow, this is Cross Bell ~! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hey, let's go soon Mom! It is!\x02",
    )

    CloseMessageWindow()

    label("loc_3A53")

    TalkEnd(0xFE)
    Return()

    # Function_14_38AD end

    def Function_15_3A57(): pass

    label("Function_15_3A57")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3AF9")

    ChrTalk(
        0xFE,
        (
            "I already have an older brother ……\x01",
            "So I told you to stop and say ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… But, the station staff\x01",
            "You seemed to be really busy right?\x01",
            "I wonder what happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B87")

    label("loc_3AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3B4B")

    ChrTalk(
        0xFE,
        "Well … let's stop it, Onii-chan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "People at the station will get angry ~.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B87")

    label("loc_3B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3B87")

    ChrTalk(
        0xFE,
        (
            "Both of us with my dad\x01",
            "I want to play at the casino.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B87")

    TalkEnd(0xFE)
    Return()

    # Function_15_3A57 end

    def Function_16_3B8B(): pass

    label("Function_16_3B8B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3C4C")

    ChrTalk(
        0xFE,
        (
            "Together, the terrorists\x01",
            "On what route do you crossbell\x01",
            "I guess you are about to enter … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There should be no blind spots ……\x01",
            "Anyway, as it stands now\x01",
            "There is no choice but to keep vigilant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D78")

    label("loc_3C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3CD6")

    ChrTalk(
        0xFE,
        (
            "The way the unveiling ceremony is finished somehow\x01",
            "It is a feeling that the load of the shoulder fell a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, it is still too much\x01",
            "I can not miss it though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D78")

    label("loc_3CD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3D78")

    ChrTalk(
        0xFE,
        (
            "Inside the station and the airport,\x01",
            "There are a considerable number of investigators in section two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Including other places, so far\x01",
            "It is a matter of putting a strong warning system\x01",
            "It is my first time in my memory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D78")

    TalkEnd(0xFE)
    Return()

    # Function_16_3B8B end

    def Function_17_3D7C(): pass

    label("Function_17_3D7C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DDE")

    ChrTalk(
        0xFE,
        (
            "A wife and a daughter who return to the empire\x01",
            "I came to see her off … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "However, it is a derailment accident … …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E0D")

    label("loc_3DDE")


    ChrTalk(
        0xFE,
        (
            "Even if my wife and daughter\x01",
            "After that train ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E0D")

    TalkEnd(0xFE)
    Return()

    # Function_17_3D7C end

    def Function_18_3E11(): pass

    label("Function_18_3E11")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "What a thing …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How much damage did you have?\x01",
            "I wonder why ….\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_3E11 end

    def Function_19_3E5B(): pass

    label("Function_19_3E5B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Is the train stopped?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then, also today\x01",
            "You will be with Dad!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_3E5B end

    def Function_20_3EAB(): pass

    label("Function_20_3EAB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Crosbell station, with today\x01",
            "The operation will be paused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, as for the schedule of resumption for now\x01",
            "It is undecided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For foreigners who wish to return home,\x01",
            "Please hurry.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_3EAB end

    def Function_21_3F61(): pass

    label("Function_21_3F61")

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

    def lambda_427E():
        OP_9B(0x1, 0xFE, 0x0, 0x30D40, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_427E)
    BeginChrThread(0x21, 0, 0, 22)
    Sleep(5000)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_3F61 end

    def Function_22_42B5(): pass

    label("Function_22_42B5")

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

    # Function_22_42B5 end

    def Function_23_431A(): pass

    label("Function_23_431A")

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

    # Function_23_431A end

    def Function_24_435B(): pass

    label("Function_24_435B")

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
            "── They have been working for many years,\x01",
            "This crossbell is our\x01",
            "I treated it as \"a province.\"\x02\x03",
            "No matter what they committed any crime\x01",
            "We do not have the right to pursue.\x02\x03",
            "And still ….\x01",
            "In a form to be stolen from rich tax revenue\x01",
            "We are exploited#4REarthquakes#It continues to be.\x02",
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
            "#4SAlthough it is ─ ─,\x01",
            "That's not all!\x02\x03",
            "#4SWe even risk the danger of life\x01",
            "It has been threatened …!\x02",
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

    # Function_24_435B end

    def Function_25_481A(): pass

    label("Function_25_481A")

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

    def lambda_48EE():
        OP_97(0x101, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_48EE)
    Sleep(100)

    def lambda_490B():
        OP_97(0x102, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_490B)
    Sleep(100)

    def lambda_4928():
        OP_97(0x103, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4928)
    Sleep(100)

    def lambda_4945():
        OP_97(0x104, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4945)
    Sleep(100)

    def lambda_4962():
        OP_97(0x105, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4962)
    Sleep(100)

    def lambda_497F():
        OP_97(0x109, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_497F)
    Sleep(100)

    def lambda_499C():
        OP_97(0x106, 0x0, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_499C)
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
            "#11P#00006FSomehow with the section chiefs\x01",
            "I want to get in touch, but …\x02\x03",
            "#00013Fwhat……?\x01",
            "What is this pale moya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108FIt's like a monastery or a tower\x01",
            "Like going out ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5PThere are also people …\x01",
            "There is not it at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#11P#10408FWell, outside the city\x01",
            "Because the battle is happening\x01",
            "I guess she is evacuating, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00205F#30W….\x02",
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

    def lambda_4BF7():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4BF7)
    Sleep(30)

    def lambda_4C07():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4C07)
    Sleep(30)

    def lambda_4C17():
        TurnDirection(0x106, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_4C17)
    Sleep(30)

    def lambda_4C27():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4C27)
    Sleep(30)

    def lambda_4C37():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4C37)
    Sleep(30)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x104,
        "#11P#00301FWhat's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203F…… From the central square\x01",
            "I hear a resonance tone.\x02\x03",
            "#00201FIt's the Great Bell!\x02",
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
        "#12P#10701FLet's go check!\x02",
    )

    CloseMessageWindow()

    def lambda_4D0E():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4D0E)
    Sleep(30)

    def lambda_4D1E():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4D1E)
    Sleep(30)

    def lambda_4D2E():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4D2E)
    Sleep(30)

    def lambda_4D3E():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4D3E)
    Sleep(30)

    def lambda_4D4E():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4D4E)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_68(500, 1200, 7500, 3000)
    MoveCamera(37, 21, 0, 3000)
    SetCameraDistance(20500, 3000)

    def lambda_4D97():
        OP_97(0x101, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4D97)
    Sleep(100)

    def lambda_4DB4():
        OP_97(0x102, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4DB4)
    Sleep(100)

    def lambda_4DD1():
        OP_97(0x103, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4DD1)
    Sleep(100)

    def lambda_4DEE():
        OP_97(0x104, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4DEE)
    Sleep(100)

    def lambda_4E0B():
        OP_97(0x105, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4E0B)
    Sleep(100)

    def lambda_4E28():
        OP_97(0x109, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4E28)
    Sleep(100)

    def lambda_4E45():
        OP_97(0x106, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_4E45)
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

    # Function_25_481A end

    def Function_26_4E93(): pass

    label("Function_26_4E93")

    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_26_4E93 end

    def Function_27_4EA5(): pass

    label("Function_27_4EA5")

    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1100)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_27_4EA5 end

    def Function_28_4EBA(): pass

    label("Function_28_4EBA")

    Sleep(500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_28_4EBA end

    def Function_29_4ECF(): pass

    label("Function_29_4ECF")

    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_29_4ECF end

    def Function_30_4EDA(): pass

    label("Function_30_4EDA")

    Sleep(500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_30_4EDA end

    def Function_31_4EE5(): pass

    label("Function_31_4EE5")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_31_4EE5 end

    def Function_32_4EF7(): pass

    label("Function_32_4EF7")

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
            "#00003F(… … Kirika's story\x01",
            "I do not know how long it will take. )\x02\x03",
            "#00001F(Before the strategy, errands are as usual\x01",
            "You'd better have done it. )\x02",
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
            "As we advance the event ahead\x01",
            "To start the operation of the Orkis Tower\x01",
            "You will not be able to act freely in the city.\x07\x00\x02",
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
            "Enter the station premises\x01",            # 0
            "Complete other errands\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_511A"),
        (1, "loc_527A"),
        (SWITCH_DEFAULT, "loc_52AC"),
    )


    label("loc_511A")

    OP_68(8400, 1900, -1900, 1500)
    MoveCamera(90, 13, 0, 1500)

    def lambda_513B():
        OP_96(0xFE, 0x2328, 0xFA, 0xFFFFF894, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_513B)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    SetCameraDistance(17500, 3000)

    def lambda_517F():
        OP_97(0x101, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_517F)
    Sleep(50)

    def lambda_519C():
        OP_97(0x103, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_519C)
    Sleep(50)

    def lambda_51B9():
        OP_97(0x102, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_51B9)
    Sleep(50)

    def lambda_51D6():
        OP_97(0x104, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_51D6)
    Sleep(50)

    def lambda_51F3():
        OP_97(0xF4, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_51F3)
    Sleep(50)

    def lambda_5210():
        OP_97(0xF5, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_5210)
    Sleep(300)
    FadeToDark(2000, 0, -1)

    def lambda_5237():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5237)
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
    Jump("loc_52AC")

    label("loc_527A")

    SetChrPos(0x0, 6500, 0, -2000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_E2(0x2)
    EventEnd(0x5)
    Jump("loc_52AC")

    label("loc_52AC")

    Return()

    # Function_32_4EF7 end

    def Function_33_52AD(): pass

    label("Function_33_52AD")

    TalkBegin(0x8)

    ChrTalk(
        0x8,
        (
            "A black carrying car made by Imperial earlier\x01",
            "I ran toward the central square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "… … Where have you been going?\x01",
            "I'm sorry, but I do not know for a moment.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_33_52AD end

    def Function_34_533A(): pass

    label("Function_34_533A")

    EventBegin(0x1)
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)
    Return()

    # Function_34_533A end

    def Function_35_5350(): pass

    label("Function_35_5350")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_53A2")

    ChrTalk(
        0x101,
        (
            "#00000FThis is Crossbell Station.\x01",
            "…… I do not have any errands anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5545")

    label("loc_53A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5483")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5400")
    Sound(807, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked firmly.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 5)
    Jump("loc_547B")

    label("loc_5400")


    ChrTalk(
        0x101,
        (
            "#00001F…… Apparently the station is\x01",
            "It seems to be blocked.\x02\x03",
            "#00003FWell, especially for errands\x01",
            "There is not it either,\x01",
            "Let's leave it here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_547B")

    SetScenarioFlags(0x1CE, 4)
    Jump("loc_5545")

    label("loc_5483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5506")

    ChrTalk(
        0x101,
        (
            "#00001F…… The campus is a foreigner returning home\x01",
            "It seems that it is considerably crowded.\x02\x03",
            "#00003FThose who have stopped entering\x01",
            "Looks nice.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    Jump("loc_5545")

    label("loc_5506")


    ChrTalk(
        0x101,
        (
            "#00000FThis is Crossbell Station.\x01",
            "…… There is no use now.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)

    label("loc_5545")

    SetChrPos(0x0, 5480, 0, -2680, 270)
    EventEnd(0x4)
    Return()

    # Function_35_5350 end

    def Function_36_5559(): pass

    label("Function_36_5559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5618")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55C9")

    ChrTalk(
        0x101,
        (
            "#00000FThe future is the South Exit of the city.\x02\x03",
            "I do not have any particular business,\x01",
            "Let's stop getting out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5605")

    label("loc_55C9")


    ChrTalk(
        0x101,
        (
            "#00000FThere is no business in this direction.\x01",
            "Let's stop getting out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5605")

    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_5618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56E7")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_568E")

    ChrTalk(
        0x101,
        (
            "#00001FThe future is the South Exit of the city.\x02\x03",
            "Right now,\x01",
            "Let's concentrate on the accident-related investigation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_56D4")

    label("loc_568E")


    ChrTalk(
        0x101,
        (
            "#00001FThere is no business in this direction.\x01",
            "Let 's concentrate on the accident - related investigation now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56D4")

    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_56E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_575D")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FAnyway now\x01",
            "I have to chase Randy -\x01",
            "It is not the case that it is on a side street.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_575D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57C2")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FIt is not the case that I am out of town right now.\x01",
            "Let's turn back to life.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_57C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5856")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FCome this far to the city\x01",
            "I can not leave.\x02\x03",
            "Operation into the Orkis Tower -\x01",
            "You must make it successful at all costs.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -230, 0, -17470, 0)
    EventEnd(0x4)

    label("loc_5856")

    Return()

    # Function_36_5559 end

    def Function_37_5857(): pass

    label("Function_37_5857")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lock on the door.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_37_5857 end

    SaveToFile()

Try(main)
