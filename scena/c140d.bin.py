from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c140d.bin",                # FileName
        "c140d",                    # MapName
        "c140d",                    # Location
        0x002E,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\x1c\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 3, 0, 4],
    )

    BuildStringList((
        "c140d",                  # 0
        "Paola Lady",           # 1
        "Van",                 # 2
        "Ruze",                   # 3
        "Canon",                 # 4
        "Dino",               # 5
        "Tantos old man",           # 6
        "Bacchus",               # 7
        "Lima",                   # 8
        "Marsun",               # 9
        "Keen",               # 10
        "Besse",                 # 11
        "Abbas",               # 12
        "Huey",               # 13
        "Slash",             # 14
        "Liang",                 # 15
        "Azel",                 # 16
        "Wald",               # 17
        "Central square",               # 18
        "Nishi dori",                 # 19
        "Administrative district",                 # 20
        "Residential area",                 # 21
        "Entertainment district",                 # 22
        "East Street",                 # 23
        "old Town",                 # 24
        "Harbor district",                 # 25
        "IBC",                 # 26
        "Beside the station",               # 27
        "Back street",                 # 28
        "Ursula interchange",           # 29
        "East Crossbell Highway",       # 30
        "West Crossbell Highway",       # 31
        "Mainz Mountain Road",           # 32
        "Orchis Tower",         # 33
    ))

    AddCharChip((
        "chr/ch31800.itc",                   # 00
        "chr/ch30900.itc",                   # 01
        "chr/ch06700.itc",                   # 02
        "chr/ch23800.itc",                   # 03
        "chr/ch23300.itc",                   # 04
        "chr/ch23000.itc",                   # 05
        "chr/ch24700.itc",                   # 06
        "chr/ch06800.itc",                   # 07
        "chr/ch24000.itc",                   # 08
        "chr/ch23302.itc",                   # 09
        "chr/ch20700.itc",                   # 0A
        "chr/ch26200.itc",                   # 0B
        "chr/ch23400.itc",                   # 0C
        "apl/ch50375.itc",                   # 0D
        "chr/ch30800.itc",                   # 0E
        "chr/ch31700.itc",                   # 0F
    ))

    DeclNpc(15449,   100,     4294967277, 270,  261,  0x0, 0,   4,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(9640,    0,       850,     180,  261,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(10279,   0,       4294966746, 315,  261,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(34080,   4294960796, 4294929026, 45,   261,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(44880,   4294964796, 4294947206, 225,  261,  0x0, 0,   7,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4269,    0,       4294915137, 90,   389,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(32799,   4294960796, 4294930346, 315,  389,  0x0, 0,   12,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(10270,   3500,    11050,   135,  389,  0x0, 0,   10,  0,   0,   0,   0,   10,  255,  0)
    DeclNpc(9609,    3500,    13869,   135,  389,  0x0, 0,   11,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(18700,   4000,    4294959086, 315,  389,  0x0, 0,   15,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(1779,    0,       4294962036, 90,   389,  0x0, 0,   14,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   255, 255, 0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   13,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(27560,   4294965886, 4294951167, 1200,    27560,   4294966886, 4294951167, 0x007C, 0,  29, 0x0000)
    DeclActor(45450,   4294964796, 4294947346, 1200,    45450,   4294965796, 4294947346, 0x007C, 0,  30, 0x0000)
    DeclActor(11700,   4294960846, 4294934446, 1200,    11700,   4294961846, 4294934446, 0x007C, 0,  31, 0x0000)
    DeclActor(4294950846, 0,       4294957746, 1200,    4294950846, 1000,    4294957746, 0x007C, 0,  32, 0x0000)
    DeclActor(17410,   4294960796, 4294931536, 1200,    17410,   4294961796, 4294931536, 0x007C, 0,  33, 0x0000)
    DeclActor(4294950606, 4294964186, 4294940956, 1200,    4294951246, 4294965216, 4294941096, 0x007C, 0,  34, 0x0000)
    DeclActor(15480,   0,       310,     1200,    14350,   1000,    4294966746, 0x007C, 0,  35, 0x0000)
    DeclActor(37750,   4294960796, 4294928796, 1200,    37750,   4294961796, 4294928796, 0x007C, 0,  40, 0x0000)
    DeclActor(4294939946, 2800,    4294938796, 1200,    4294939946, 3800,    4294938796, 0x007C, 0,  41, 0x0000)
    DeclActor(48220,   200,     4294928876, 1200,    48220,   1200,    4294928876, 0x007C, 0,  42, 0x0000)
    DeclActor(4294965516, 4294962996, 4294935516, 1200,    4294965516, 4294963996, 4294935516, 0x007C, 0,  36, 0x0000)
    DeclActor(39750,   4294964796, 4294949766, 1200,    39750,   4294965796, 4294949766, 0x007C, 0,  37, 0x0000)
    DeclActor(8109,    0,       4294959076, 1200,    8109,    1000,    4294959076, 0x007C, 0,  38, 0x0000)
    DeclActor(42230,   4294964796, 4294942076, 1200,    42230,   4294965796, 4294942076, 0x007C, 0,  39, 0x0000)
    DeclActor(47720,   4294966196, 4294934136, 1200,    47720,   100,     4294934136, 0x007C, 0,  5,  0x0000)
    DeclActor(38560,   4294960796, 4294936136, 1200,    38560,   4294962396, 4294936136, 0x007C, 0,  6,  0x0000)

    PlaceName(-110.69000244140625, 0.0, 106.94999694824219, 0x0000, 0x0000, "Central square")
    PlaceName(-186.3000030517578, 0.0, 112.12999725341797, 0x0000, 0x0000, "Nishi dori")
    PlaceName(-79.63999938964844, 0.0, 209.3000030517578, 0x0000, 0x0000, "Administrative district")
    PlaceName(-256.45001220703125, 0.0, 197.8000030517578, 0x0000, 0x0000, "Residential area")
    PlaceName(-172.5, 0.0, 188.60000610351562, 0x0000, 0x0000, "Entertainment district")
    PlaceName(-17.25, 0.0, 80.5, 0x0000, 0x0000, "East Street")
    PlaceName(23.579999923706055, 0.0, 17.25, 0x0000, 0x0000, "old Town")
    PlaceName(14.949999809265137, 0.0, 156.39999389648438, 0x0000, 0x0000, "Harbor district")
    PlaceName(-14.949999809265137, 0.0, 264.5, 0x0000, 0x0000, "IBC")
    PlaceName(-97.75, 0.0, 27.600000381469727, 0x0000, 0x0000, "Beside the station")
    PlaceName(-151.8000030517578, 0.0, 147.1999969482422, 0x0000, 0x0000, "Back street")
    PlaceName(-101.19999694824219, 0.0, -8.050000190734863, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(44.849998474121094, 0.0, 96.5999984741211, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-244.9499969482422, 0.0, 110.4000015258789, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-238.0500030517578, 0.0, 225.39999389648438, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(-88.0, 0.0, 360.0, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(-135.99000549316406, 0.0, 90.8499984741211, 0x0000, 0x0051, "")
    PlaceName(-74.18000030517578, 0.0, 120.75, 0x0000, 0x0054, "")
    PlaceName(-107.80999755859375, 0.0, 81.6500015258789, 0x0000, 0x0057, "")
    PlaceName(-136.85000610351562, 0.0, 124.19999694824219, 0x0000, 0x0053, "")
    PlaceName(-113.27999877929688, 0.0, 151.8000030517578, 0x0000, 0x0053, "")
    PlaceName(-171.63999938964844, 0.0, 118.44999694824219, 0x0000, 0x0053, "")
    PlaceName(-182.85000610351562, 0.0, 142.60000610351562, 0x0000, 0x0053, "")
    PlaceName(-155.25, 0.0, 179.39999389648438, 0x0000, 0x0052, "")
    PlaceName(-149.7899932861328, 0.0, 164.4499969482422, 0x0000, 0x0053, "")
    PlaceName(-139.72999572753906, 0.0, 154.67999267578125, 0x0000, 0x0053, "")
    PlaceName(-106.94999694824219, 0.0, 236.3300018310547, 0x0000, 0x0051, "")
    PlaceName(21.850000381469727, 0.0, 80.5, 0x0000, 0x0052, "")
    PlaceName(2.299999952316284, 0.0, -23.579999923706055, 0x0000, 0x0053, "")
    PlaceName(-12.649999618530273, 0.0, -2.299999952316284, 0x0000, 0x0053, "")

    ChipFrameInfo(2308, 0)                                       # 0

    ScpFunction((
        "Function_0_904",          # 00, 0
        "Function_1_9B4",          # 01, 1
        "Function_2_9DF",          # 02, 2
        "Function_3_A0A",          # 03, 3
        "Function_4_D63",          # 04, 4
        "Function_5_F50",          # 05, 5
        "Function_6_10A1",         # 06, 6
        "Function_7_1154",         # 07, 7
        "Function_8_1401",         # 08, 8
        "Function_9_153B",         # 09, 9
        "Function_10_15FE",        # 0A, 10
        "Function_11_16C8",        # 0B, 11
        "Function_12_195C",        # 0C, 12
        "Function_13_1DC1",        # 0D, 13
        "Function_14_1FB9",        # 0E, 14
        "Function_15_2198",        # 0F, 15
        "Function_16_2321",        # 10, 16
        "Function_17_2699",        # 11, 17
        "Function_18_26A0",        # 12, 18
        "Function_19_2A1E",        # 13, 19
        "Function_20_2AF3",        # 14, 20
        "Function_21_2C98",        # 15, 21
        "Function_22_2D26",        # 16, 22
        "Function_23_2D8E",        # 17, 23
        "Function_24_2DFC",        # 18, 24
        "Function_25_2FEC",        # 19, 25
        "Function_26_4175",        # 1A, 26
        "Function_27_418B",        # 1B, 27
        "Function_28_46DC",        # 1C, 28
        "Function_29_52E4",        # 1D, 29
        "Function_30_533F",        # 1E, 30
        "Function_31_539A",        # 1F, 31
        "Function_32_53F5",        # 20, 32
        "Function_33_5450",        # 21, 33
        "Function_34_54AB",        # 22, 34
        "Function_35_5506",        # 23, 35
        "Function_36_5561",        # 24, 36
        "Function_37_55BC",        # 25, 37
        "Function_38_5617",        # 26, 38
        "Function_39_5672",        # 27, 39
        "Function_40_56CD",        # 28, 40
        "Function_41_5728",        # 29, 41
        "Function_42_5783",        # 2A, 42
        "Function_43_57DE",        # 2B, 43
        "Function_44_5B32",        # 2C, 44
        "Function_45_5F2F",        # 2D, 45
        "Function_46_68C6",        # 2E, 46
        "Function_47_68EF",        # 2F, 47
        "Function_48_692C",        # 30, 48
        "Function_49_6966",        # 31, 49
        "Function_50_69A0",        # 32, 50
    ))


    def Function_0_904(): pass

    label("Function_0_904")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_93C"),
        (1, "loc_948"),
        (2, "loc_954"),
        (3, "loc_960"),
        (4, "loc_96C"),
        (5, "loc_978"),
        (6, "loc_984"),
        (SWITCH_DEFAULT, "loc_990"),
    )


    label("loc_93C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_99C")

    label("loc_948")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_99C")

    label("loc_954")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_99C")

    label("loc_960")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_99C")

    label("loc_96C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_99C")

    label("loc_978")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_99C")

    label("loc_984")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_99C")

    label("loc_990")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_99C")

    label("loc_99C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9B3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_99C")

    label("loc_9B3")

    Return()

    # Function_0_904 end

    def Function_1_9B4(): pass

    label("Function_1_9B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9DE")
    OP_94(0xFE, 0xFFFF8C06, 0xFFFF9F48, 0xFFFF9552, 0xFFFF88E6, 0x3E8)
    Sleep(300)
    Jump("Function_1_9B4")

    label("loc_9DE")

    Return()

    # Function_1_9B4 end

    def Function_2_9DF(): pass

    label("Function_2_9DF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A09")
    OP_94(0xFE, 0x8D04, 0xFFFF6E7E, 0x7800, 0xFFFF612C, 0x3E8)
    Sleep(300)
    Jump("Function_2_9DF")

    label("loc_A09")

    Return()

    # Function_2_9DF end

    def Function_3_A0A(): pass

    label("Function_3_A0A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE7")
    SetChrPos(0x0, 2050, 0, 14590, 180)
    SetChrPos(0x1, 2050, 0, 14590, 180)
    SetChrPos(0x2, 2050, 0, 14590, 180)
    SetChrPos(0x3, 2050, 0, 14590, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A91")
    SetChrPos(0x4, 2050, 0, 14590, 180)
    SetChrPos(0x5, 2050, 0, 14590, 180)
    Jump("loc_AB0")

    label("loc_A91")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB0")
    SetChrPos(0x4, 2050, 0, 14590, 180)

    label("loc_AB0")

    OP_68(2050, 2000, 14590, 0)
    MoveCamera(45, 34, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AE7")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 0x9)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B79")
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 2800, 0, -4440, 270)
    BeginChrThread(0x16, 0, 0, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 1100, 0, -4440, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 590, 0, -6640, 135)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -28960, 2800, -28390, 315)
    BeginChrThread(0xE, 0, 0, 1)
    BeginChrThread(0xB, 0, 0, 2)
    Jump("loc_D26")

    label("loc_B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_BA0")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_D26")

    label("loc_BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BE7")
    SetChrPos(0xB, 8290, 0, -1190, 45)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0x9, 9640, 0, 850, 180)
    SetChrPos(0xA, 10280, 0, -550, 315)
    Jump("loc_D26")

    label("loc_BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D26")
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C64")
    SetChrPos(0x11, -200, 0, -8460, 180)
    SetChrPos(0x12, 30390, -2500, -21970, 0)
    SetChrPos(0x10, 6500, 0, 5410, 0)
    SetChrPos(0xF, 5490, 0, 5600, 0)
    Jump("loc_CD9")

    label("loc_C64")

    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 2520, -10, -4059, 225)
    SetChrPos(0x11, 2120, -10, -6060, 315)
    SetChrPos(0x12, 310, -10, -4250, 90)
    SetChrPos(0x17, 10930, 0, -3700, 90)
    SetChrPos(0x10, 6500, 0, 5410, 0)
    SetChrPos(0xF, 5490, 0, 5600, 0)
    SetChrFlags(0xF, 0x10)

    label("loc_CD9")

    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 34490, -6500, -37750, 315)
    SetChrPos(0xA, 34490, -6500, -38950, 315)
    SetChrPos(0xB, 34840, -2220, -19610, 0)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D26")
    SetChrFlags(0xB, 0x10)

    label("loc_D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_D3A")
    ClearScenarioFlags(0x22, 0)
    Event(0, 24)
    Jump("loc_D62")

    label("loc_D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_D4E")
    ClearScenarioFlags(0x22, 1)
    Event(0, 25)
    Jump("loc_D62")

    label("loc_D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_D62")
    ClearScenarioFlags(0x22, 2)
    SetMapFlags(0x10000000)
    Event(0, 45)

    label("loc_D62")

    Return()

    # Function_3_A0A end

    def Function_4_D63(): pass

    label("Function_4_D63")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    OP_65(0x8, 0x1)
    OP_65(0x9, 0x1)
    OP_65(0xA, 0x1)
    OP_65(0xB, 0x1)
    OP_65(0xC, 0x1)
    OP_65(0xD, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('金属探测器', 0x0)"), scpexpr(EXPR_END)), "loc_DDF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DDF")
    LoadEffect(0x7, "event/ev10016.eff")

    label("loc_DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DFA")
    ClearMapObjFlags(0x7, 0x4)

    label("loc_DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_E2F")
    SetMapObjFrame(0xFF, "koge2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kenzai", 0x1, 0x1)
    SetMapObjFrame(0xFF, "blue", 0x1, 0x1)
    Jump("loc_E8B")

    label("loc_E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_E64")
    SetMapObjFrame(0xFF, "koge2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kenzai", 0x1, 0x1)
    SetMapObjFrame(0xFF, "blue", 0x1, 0x1)
    Jump("loc_E8B")

    label("loc_E64")

    SetMapObjFrame(0xFF, "koge2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kenzai", 0x0, 0x1)
    SetMapObjFrame(0xFF, "blue", 0x0, 0x1)

    label("loc_E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F08")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x6E, 0x0)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_F08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F38")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x24, 0x8C, 0x0)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4B")
    OP_70(0x5, 0x0)
    Jump("loc_F4F")

    label("loc_F4B")

    OP_70(0x5, 0x1E)

    label("loc_F4F")

    Return()

    # Function_4_D63 end

    def Function_5_F50(): pass

    label("Function_5_F50")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1050")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('珊瑚戒指', 1)"), scpexpr(EXPR_END)), "loc_FD9")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '珊瑚戒指'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_104B")

    label("loc_FD9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '珊瑚戒指'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '珊瑚戒指'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_104B")

    Jump("loc_1095")

    label("loc_1050")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1095")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_F50 end

    def Function_6_10A1(): pass

    label("Function_6_10A1")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is \"authentic dish made with oven\".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_1150")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1150")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Stamina steak\"\x07\x00",
            "I learned the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_1150")

    TalkEnd(0xFF)
    Return()

    # Function_6_10A1 end

    def Function_7_1154(): pass

    label("Function_7_1154")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_12E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1256")

    ChrTalk(
        0xFE,
        (
            "Wow ~, Hick ……\x01",
            "After all the liquor is great …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Even if it is, what the hell\x01",
            "The funny treasure is … oh …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Oh, it's dangerous,\x01",
            "Drunk in a place like this … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F(Oh well, drinking and feeling also\x01",
            "You do not understand it. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_12E2")

    label("loc_1256")


    ChrTalk(
        0xFE,
        (
            "Wow ~, Hick ……\x01",
            "That fool in the fool,\x01",
            "Perhaps it is heaven ……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Surely delicious liquor and\x01",
            "Cute little sister\x01",
            "I wonder what is full ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E2")

    Jump("loc_13FD")

    label("loc_12E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_12F5")
    Jump("loc_13FD")

    label("loc_12F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1303")
    Jump("loc_13FD")

    label("loc_1303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_13FD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132B")
    Call(0, 8)
    Jump("loc_13A3")

    label("loc_132B")


    ChrTalk(
        0xFE,
        (
            "It seems that there are cooks,\x01",
            "It is not unusual work from daytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let me finish quickly,\x01",
            "I'm going to have a drink quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13A3")

    Jump("loc_13FD")

    label("loc_13A8")


    ChrTalk(
        0xFE,
        (
            "Trust me, the sun is\x01",
            "It's dazzling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It is poisonous for a night type man.\x02",
    )

    CloseMessageWindow()

    label("loc_13FD")

    TalkEnd(0xFE)
    Return()

    # Function_7_1154 end

    def Function_8_1401(): pass

    label("Function_8_1401")

    OP_4B(0x9, 0xFF)
    OP_4B(0xE, 0xFF)
    TurnDirection(0x9, 0x0, 0)

    ChrTalk(
        0x9,
        (
            "Caja Ha, O yasie's gossip,\x01",
            "I am unusually working from daytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Whatever you do with Hooko,\x01",
            "You kick out from the apartment.\x01",
            "She seems to have told the landlord.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xE, 0x9, 0)

    ChrTalk(
        0xE,
        (
            "Oh, Van.\x01",
            "You are not talking about extra things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Shut up and help your work.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    OP_93(0x9, 0x13B, 0x0)
    OP_93(0xE, 0x13B, 0x0)
    OP_4C(0x9, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_8_1401 end

    def Function_9_153B(): pass

    label("Function_9_153B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_159D")

    ChrTalk(
        0xFE,
        (
            "Well, today as well.\x01",
            "Would you like me to pick it up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "First, measure the dimensions, and …\x02",
    )

    CloseMessageWindow()
    Jump("loc_15FA")

    label("loc_159D")


    ChrTalk(
        0xFE,
        (
            "Well, I got a bit late but\x01",
            "I finally breathed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yoshito … I will try my best from the afternoon too!\x02",
    )

    CloseMessageWindow()

    label("loc_15FA")

    TalkEnd(0xFE)
    Return()

    # Function_9_153B end

    def Function_10_15FE(): pass

    label("Function_10_15FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165B")

    ChrTalk(
        0xFE,
        "Dad, I work for everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Very cool, ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_16C4")

    label("loc_165B")

    OP_4B(0x10, 0x0)
    SetChrName("Lima")

    ChrTalk(
        0xF,
        "Dad, this juice delicious ー ー ー ー ー ー ー.\x02",
    )

    CloseMessageWindow()
    SetChrName("Marsun")

    ChrTalk(
        0x10,
        (
            "Oh, it is true.\x01",
            "Daddy also gains power.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0x0)

    label("loc_16C4")

    TalkEnd(0xFE)
    Return()

    # Function_10_15FE end

    def Function_11_16C8(): pass

    label("Function_11_16C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1815")

    ChrTalk(
        0x13,
        (
            "#04100F… … That's right, because it's a big problem\x01",
            "I will hand this over to you.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Abbas account\"\x07\x00",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x28, 0)
    OP_E4(0x3)

    ChrTalk(
        0x101,
        (
            "#00005F\"Pomutto! Account …?\x01",
            "Are you also doing Abbas?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#04100FIt's only when time is available.\x02\x03",
            "I will do my partner if I feel like it,\x01",
            "You may apply for a match.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1958")

    label("loc_1815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F1")

    ChrTalk(
        0x13,
        (
            "#04100FSpecial Affairs Support Division ……\x01",
            "Today was really saved.\x02\x03",
            "Thanks to that, I heard that the work is going well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHehe, you are welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FAbbas are\x01",
            "Do your best even after this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#04100FOh, of course.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1958")

    label("loc_18F1")


    ChrTalk(
        0x13,
        (
            "#04100FWell, the necessary parts are also\x01",
            "Almost completed.\x02\x03",
            "Focus until the sunset\x01",
            "I'm doing my work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1958")

    TalkEnd(0xFE)
    Return()

    # Function_11_16C8 end

    def Function_12_195C(): pass

    label("Function_12_195C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1AB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A48")

    ChrTalk(
        0xFE,
        (
            "Somehow, ridiculous things\x01",
            "It has happened …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I saw that pale tree,\x01",
            "I also do something, what I can do\x01",
            "I think I have to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At the very least make the city as beautiful as possible,\x01",
            "I hope everyone is relieved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1AB2")

    label("loc_1A48")


    ChrTalk(
        0xFE,
        (
            "If you do so, try hard.\x01",
            "I have to clean up the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As long as you do your best,\x01",
            "Surely there are good things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AB2")

    Jump("loc_1DBD")

    label("loc_1AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1AC5")
    Jump("loc_1DBD")

    label("loc_1AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B0A")

    ChrTalk(
        0xFE,
        (
            "Well, it's a war … …\x01",
            "I can not do such a thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBD")

    label("loc_1B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1DBD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B46")
    Call(0, 27)
    Return()

    label("loc_1B46")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('废弃材料', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BD1")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "talk\x01",        # 0
            "Pass waste materials\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1BC0"),
        (1, "loc_1BC5"),
        (SWITCH_DEFAULT, "loc_1BD1"),
    )


    label("loc_1BC0")

    Jump("loc_1BD1")

    label("loc_1BC5")

    Call(0, 43)
    TalkEnd(0xB)
    Return()

    label("loc_1BD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C42")

    ChrTalk(
        0xFE,
        (
            "Gasagoso …\x01",
            "Well, this is … no good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then …\x01",
            "Well, this is too lazy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBD")

    label("loc_1C42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE4")

    ChrTalk(
        0xB,
        (
            "Onii-chan\x01",
            "Waste material containing metal\x01",
            "Can you please find me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I cleaned up all the way,\x01",
            "Things that have not been found yet\x01",
            "I think there is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D44")

    label("loc_1CE4")


    ChrTalk(
        0xFE,
        "Thank you, Onii-chan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The waste materials received\x01",
            "I am responsible\x01",
            "I will exchange money.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D44")

    Jump("loc_1DBD")

    label("loc_1D49")


    ChrTalk(
        0xFE,
        (
            "Well, stomach too\x01",
            "It's going to be full,\x01",
            "I will do my best again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Onii-chan\x01",
            "You helped me a lot\x01",
            "Thanks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DBD")

    TalkEnd(0xFE)
    Return()

    # Function_12_195C end

    def Function_13_1DC1(): pass

    label("Function_13_1DC1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1F21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E92")

    ChrTalk(
        0xFE,
        (
            "What is it?\x01",
            "That big and splendid tree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Glowing pale white ……\x01",
            "I do not think it's from this world\x01",
            "It is beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To us goddess\x01",
            "Will you take me along?\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_1F1C")

    label("loc_1E92")


    ChrTalk(
        0xFE,
        (
            "That big and splendid tree,\x01",
            "I do not think it's from this world\x01",
            "It is beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To us goddess\x01",
            "Will you take me along?\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F1C")

    Jump("loc_1FB5")

    label("loc_1F21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1F2F")
    Jump("loc_1FB5")

    label("loc_1F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1FB5")

    ChrTalk(
        0xFE,
        (
            "I do not really understand it,\x01",
            "It is in a serious situation\x01",
            "Looks like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People who have not left home for a while\x01",
            "Perhaps it might be good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FB5")

    TalkEnd(0xFE)
    Return()

    # Function_13_1DC1 end

    def Function_14_1FB9(): pass

    label("Function_14_1FB9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2044")

    ChrTalk(
        0xFE,
        (
            "A non-drunk man\x01",
            "Because it is too bad,\x01",
            "I bought some sake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… I've been drinking forever!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2194")

    label("loc_2044")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2052")
    Jump("loc_2194")

    label("loc_2052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_20C8")

    ChrTalk(
        0xFE,
        (
            "Hello, something about the street\x01",
            "I'm becoming a big trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Someone may become a war\x01",
            "I told you I do not know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2194")

    label("loc_20C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2194")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2128")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F0")
    Call(0, 8)
    Jump("loc_2123")

    label("loc_20F0")


    ChrTalk(
        0xFE,
        (
            "Caja Ha, O yasie's gossip,\x01",
            "It is as thoughtful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2123")

    Jump("loc_2194")

    label("loc_2128")


    ChrTalk(
        0xFE,
        (
            "Hello, today's cooked also\x01",
            "It was delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If such things are eating out every day,\x01",
            "You can do it all the time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2194")

    TalkEnd(0xFE)
    Return()

    # Function_14_1FB9 end

    def Function_15_2198(): pass

    label("Function_15_2198")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2230")

    ChrTalk(
        0xFE,
        (
            "Van from herself to her father\x01",
            "It is reasonable to give you alcohol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Couscous……\x01",
            "Decent Bacchus Uncle,\x01",
            "It was such a fun time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_231D")

    label("loc_2230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_223E")
    Jump("loc_231D")

    label("loc_223E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_227B")

    ChrTalk(
        0xFE,
        (
            "Couscous……\x01",
            "Is not that a bad idea?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_231D")

    label("loc_227B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_231D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D6")

    ChrTalk(
        0xFE,
        (
            "Couscous……\x01",
            "Van's father is\x01",
            "It is reliable on surprise.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_231D")

    label("loc_22D6")


    ChrTalk(
        0xFE,
        (
            "For cooking,\x01",
            "There is one more evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What next will you have to eat?\x02",
    )

    CloseMessageWindow()

    label("loc_231D")

    TalkEnd(0xFE)
    Return()

    # Function_15_2198 end

    def Function_16_2321(): pass

    label("Function_16_2321")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_245B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2415")

    ChrTalk(
        0xFE,
        (
            "Jed's finally finally\x01",
            "It was supposed to be power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Although such a thing happened,\x01",
            "For us, Waldo\x01",
            "After all it is an important leader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys …… somehow\x01",
            "Take me back to you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2456")

    label("loc_2415")


    ChrTalk(
        0xFE,
        (
            "You … … somehow Mr. Wald\x01",
            "Take me back to you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2456")

    Jump("loc_2695")

    label("loc_245B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2469")
    Jump("loc_2695")

    label("loc_2469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2695")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_261F")

    ChrTalk(
        0xFE,
        "Oh, the Special Affairs Support Division ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FMr. Dino ……\x01",
            "Er, other members are … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, oh, thanks.\x01",
            "The most serious seniors, Koki\x01",
            "I managed to regain consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Some other seniors also left the hospital\x01",
            "I am coming back to the old city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, to the stance, immediately to the team\x01",
            "I think it is difficult to return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But if you wait here,\x01",
            "You surely will show your face, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FMr. Dino ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008FReally……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 2)
    Jump("loc_2695")

    label("loc_261F")


    ChrTalk(
        0xFE,
        (
            "Even so ……\x01",
            "From the morning the streets are noisy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard about independence,\x01",
            "I want you to do more quietly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2695")

    TalkEnd(0xFE)
    Return()

    # Function_16_2321 end

    def Function_17_2699(): pass

    label("Function_17_2699")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_17_2699 end

    def Function_18_26A0(): pass

    label("Function_18_26A0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28A4")
    SetScenarioFlags(0x191, 6)

    ChrTalk(
        0x17,
        (
            "Oh, everyone in the support department.\x01",
            "Thank you very much for today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Because cooked pork juice was left over\x01",
            "Take it if you like.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 4)), scpexpr(EXPR_END)), "loc_277C")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '强壮苦番茄猪骨汤'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('强壮苦番茄猪骨汤', 6)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    Jump("loc_27CA")

    label("loc_277C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '暖心猪骨汤'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('暖心猪骨汤', 6)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()

    label("loc_27CA")


    ChrTalk(
        0x101,
        (
            "#00000FThank you,\x01",
            "I will appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FThis pork soup, really\x01",
            "It was delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYeah, I think you can get it again\x01",
            "I am happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Haha, if you say so\x01",
            "It is also worthwhile to make this one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A1A")

    label("loc_28A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2978")

    ChrTalk(
        0x17,
        (
            "Because pork juice is peculiar\x01",
            "My sister and Yuggott as well\x01",
            "I'd rather take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Oh, but this is a reconstruction work\x01",
            "Because it belongs to the person who helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Oh yeah, then\x01",
            "I wonder if they could help me with washing, too?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2A1A")

    label("loc_2978")


    ChrTalk(
        0x17,
        (
            "Because pork juice is peculiar\x01",
            "My sister and Yuggott as well\x01",
            "I'd rather take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Both of us seem to be free today,\x01",
            "I also have a little help\x01",
            "Maybe it is ant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A1A")

    TalkEnd(0xFE)
    Return()

    # Function_18_26A0 end

    def Function_19_2A1E(): pass

    label("Function_19_2A1E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A8B")

    ChrTalk(
        0xFE,
        (
            "Well, after all\x01",
            "Do not use physical strength on site work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But well, well this\x01",
            "It's a good training.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AEF")

    label("loc_2A8B")


    ChrTalk(
        0xFE,
        (
            "Well, from here\x01",
            "I feel even more heavy workers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so ……\x01",
            "Besse's guy, are you all right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AEF")

    TalkEnd(0xFE)
    Return()

    # Function_19_2A1E end

    def Function_20_2AF3(): pass

    label("Function_20_2AF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B98")

    ChrTalk(
        0x12,
        (
            "That's right.\x01",
            "In this apartment\x01",
            "The destruction is fantastic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Although it was good in a waste apartment,\x01",
            "I thought that there were people inside,\x01",
            "I'm horrified.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C94")

    label("loc_2B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C30")

    ChrTalk(
        0x12,
        "……burp.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Because you say you can do something ……\x01",
            "One day, I ate too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Ho houd\x01",
            "You should have stopped it ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C94")

    label("loc_2C30")


    ChrTalk(
        0x12,
        (
            "When you put your strength\x01",
            "It may flow backwards …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Ho houd\x01",
            "You should have stopped it ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C94")

    TalkEnd(0xFE)
    Return()

    # Function_20_2AF3 end

    def Function_21_2C98(): pass

    label("Function_21_2C98")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "With the Testament 's Blue Buddhists,\x01",
            "We are looking around in cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Happy, in the old city\x01",
            "If I have someone who is selfish\x01",
            "We'll make it bogo.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_2C98 end

    def Function_22_2D26(): pass

    label("Function_22_2D26")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "What to do, what should I do With that wood?\x01",
            "Will it show up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hiakha, meaning me seriously! It is!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_2D26 end

    def Function_23_2D8E(): pass

    label("Function_23_2D8E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "If you keep watch over each other's territory\x01",
            "It seems to be safe for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "OK, I guess I'll come around again.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_2D8E end

    def Function_24_2DFC(): pass

    label("Function_24_2DFC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, -200, 0, -8460, 180)
    SetChrPos(0x12, 30390, -2500, -21970, 0)
    SetChrPos(0x10, 6500, 0, 5410, 0)
    SetChrPos(0xF, 5490, 0, 5600, 0)
    SetChrPos(0x9, 34490, -6500, -37750, 315)
    SetChrPos(0xA, 34490, -6500, -38950, 315)
    SetChrPos(0xB, 34840, -2220, -19610, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    OP_68(32850, -500, -17050, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(13250, 0)
    MoveCamera(45, 25, 0, 7000)
    SetCameraDistance(25250, 7000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(32780, -3600, -36810, 0)
    MoveCamera(19, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22320, 0)
    OP_68(32780, -5600, -36810, 5000)
    Sleep(4000)
    Fade(500)
    OP_68(2750, 2000, 4750, 0)
    MoveCamera(55, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    OP_68(-2300, 2000, -8850, 8000)
    Sleep(6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 3)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_2DFC end

    def Function_25_2FEC(): pass

    label("Function_25_2FEC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02100.itc", 0x1E)
    LoadChrToIndex("chr/ch30950.itc", 0x20)
    LoadChrToIndex("chr/ch31850.itc", 0x21)
    LoadChrToIndex("apl/ch51601.itc", 0x22)
    LoadChrToIndex("apl/ch51602.itc", 0x23)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis269.itp")
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 17200, -6500, -37400, 0)
    OP_52(0x18, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 50000, -2100, -22700, 270)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    EndChrThread(0xC, 0xFF)
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 7300, 0, -4300, 180)
    EndChrThread(0x11, 0xFF)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 5900, 0, -3800, 180)
    EndChrThread(0x12, 0xFF)
    SetChrChipByIndex(0x16, 0x20)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 8700, 0, -3300, 180)
    EndChrThread(0x16, 0xFF)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 7300, 0, -2800, 180)
    EndChrThread(0x17, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 7300, 0, -4300, 180)
    EndChrThread(0x11, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    OP_63(0x18, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(-11350, 2000, -25280, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18590, 0)
    OP_68(7460, 2000, -46280, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_68(17200, -4500, -36400, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(18000, 1000)
    Sleep(1000)
    OP_64(0x18)
    Sleep(500)
    OP_92(0x18, 0x5334, 0xFFFF6DE8, 0x190)
    Sleep(300)

    def lambda_32B5():
        OP_95(0xFE, 20640, -6500, -36460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_32B5)
    WaitChrThread(0x18, 1)

    def lambda_32D3():
        OP_95(0xFE, 21800, -2500, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_32D3)
    Sleep(2500)
    Fade(500)
    OP_68(22060, -500, -22520, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    MoveCamera(45, 21, 0, 5000)
    SetCameraDistance(17000, 5000)
    WaitChrThread(0x18, 1)
    OP_93(0x18, 0x2D, 0x190)
    OP_6F(0x79)
    Sleep(300)
    OP_63(0x18, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x18)
    Sleep(500)
    OP_93(0x18, 0x5A, 0x190)

    def lambda_3369():
        OP_95(0xFE, 41800, -2500, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3369)
    Sleep(2500)
    Fade(500)
    OP_68(35300, -900, -22650, 0)
    MoveCamera(57, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(22000, 0)
    OP_68(45300, -900, -22650, 7500)
    MoveCamera(57, 13, 0, 7500)
    SetCameraDistance(19000, 7500)
    WaitChrThread(0x18, 1)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x18,
        "#01601F#30W#5P…\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x18, 0x22)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x18, 0x2)
    SetChrFlags(0x18, 0x20)
    Sleep(500)

    ChrTalk(
        0x18,
        "#01608F#30W#5PShit!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Voice of a boy",
        "#30W#2S#5PWald…\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x10)
    ClearChrFlags(0x18, 0x2)
    ClearChrFlags(0x18, 0x20)

    def lambda_34F9():
        OP_95(0xFE, 47600, -2100, -22700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_34F9)

    def lambda_3513():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_3513)
    WaitChrThread(0xC, 1)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x18,
        "#01605F#5PDino…. You\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PW-Wald!?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xC,
        "#4S#11PIt's really Wald!\x02",
    )

    CloseMessageWindow()
    OP_68(42200, -1100, -22700, 1500)
    MoveCamera(53, 20, 0, 1300)
    SetCameraDistance(17000, 1300)
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_35F7():
        OP_95(0xFE, 42600, -2100, -22700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_35F7)
    WaitChrThread(0xC, 1)
    Sound(812, 0, 50, 0)
    OP_6F(0x79)
    Sleep(300)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0xC,
        (
            "#2PWhere are you … …!!\x01",
            "I was really worried! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2PBut, well well, well ……\x01",
            "…… Uuuuuuu … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#5P#01601F#30W…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2PSeniors are\x01",
            "Everyone owed a big injury ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2PSome people were able to leave the hospital\x01",
            "You can not come back at all … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2PBut, it's okay!\x01",
            "I'm sure if there is Mr. Wald … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#5P#01608F…!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x18, 0x22)
    SetChrSubChip(0x18, 0x1)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x18, 0x2)
    SetChrFlags(0x18, 0x20)
    Sleep(500)
    SetChrSubChip(0x18, 0x2)
    OP_68(43040, -1100, -22830, 500)
    SetCameraDistance(16149, 500)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    Sound(815, 0, 50, 0)
    Sound(802, 0, 100, 0)
    BeginChrThread(0xC, 3, 0, 26)

    def lambda_380A():
        OP_9D(0xFE, 0xAB7C, 0xFFFFF7CC, 0xFFFFA754, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_380A)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    Sound(862, 0, 30, 0)

    ChrTalk(
        0xC,
        "#11PAh!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 3)

    def lambda_385A():
        OP_A6(0xFE, 0x0, 0x32, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_385A)
    Sleep(300)
    SetChrSubChip(0xC, 0x3)
    Sleep(100)
    SetChrSubChip(0xC, 0x4)

    ChrTalk(
        0xC,
        "#60W#2SWald?\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x10)
    ClearChrFlags(0x18, 0x2)
    ClearChrFlags(0x18, 0x20)
    OP_93(0x18, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x18,
        (
            "#11P#01603F#30WThe Saber Vipers are disbanded\x02\x03",
            "#01608FEven you twice ……\x01",
            "Do not chase my ass.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        "#50W#2SYou're… lying…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#50W#2SBecause Wald…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#50W#2S…… Mr. Wald always ……\x01",
            "With the best head you can count on … …\x02",
        )
    )

    CloseMessageWindow()
    OP_68(30200, -1100, -22700, 9000)
    MoveCamera(65, 11, 0, 9000)
    OP_6E(550, 9000)
    SetCameraDistance(19000, 9000)

    def lambda_3A0E():
        OP_95(0xFE, 17000, -2500, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3A0E)
    Sleep(500)
    SetChrSubChip(0xC, 0x5)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(230, 10, -1, -1)

    AnonymousTalk(
        0xC,
        (
            "#25A… … That demon ……\x01",
            "A monster who made everyone a mess\x01",
            "Mr. Waldo!\x02",
        )
    )

    Sleep(3000)
    OP_82(0xC8, 0x0, 0xBB8, 0x7D0)
    SetMessageWindowPos(230, 20, -1, -1)

    AnonymousTalk(
        0xC,
        "#20A#4SThat's a lie right!?\x02",
    )

    Sleep(2500)
    OP_57(0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x18, 0x1)
    OP_6F(0x79)
    Sleep(1000)
    SetChrFlags(0xC, 0x80)
    OP_68(9600, 1100, -13300, 0)
    MoveCamera(100, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    OP_90(0x18, 14100, -1000, -17800, 315)

    def lambda_3B3D():
        OP_95(0xFE, 9600, 0, -13300, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3B3D)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x18, 1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    NpcTalk(
        0x11,
        "Voice of a young man",
        "S-stop!\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(805, 0, 100, 0)
    Sound(318, 0, 40, 0)
    OP_68(7850, 1100, -6000, 2500)
    MoveCamera(35, 21, 0, 2500)
    SetCameraDistance(17000, 2500)

    def lambda_3BDD():
        OP_95(0xFE, 8400, 0, -8300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3BDD)
    WaitChrThread(0x18, 1)
    OP_6F(0x79)

    ChrTalk(
        0x11,
        (
            "#5PWaldo Vales!\x01",
            "Well, maybe you do not return … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PNo more, the Old Town\x01",
            "I will not let you love me ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#5PWe will stop you here\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11P#01600F…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P…… You are united,\x01",
            "What I wanted to do ……! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5POh, it turned into such a thing\x01",
            "Make this Old Town confusingly … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "I was pretty cute.\x01",
            "Like the minions … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PIt was too much!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11P#01604FHm\x02\x03",
            "#01602FThat's it.\x01",
            "What happened to Wazi and Baldo?\x02\x03",
            "Originally, I saw a lieutenant … …\x01",
            "Did you run away with a tail?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(250)
    OP_82(0x64, 0x0, 0xBB8, 0xFA)

    ChrTalk(
        0x11,
        "#5PDon't make fun of us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PIf that two people\x01",
            "It surely comes back …!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x18,
        "#11P#01605FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThere seems to be circumstances!\x01",
            "You have a mission to fulfill!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThat's why the city leaves\x01",
            "I will come back again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "I do not know what it is ….\x01",
            "We just believe in the two of us!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x18)
    Fade(250)
    SetChrChipByIndex(0x18, 0x22)
    SetChrSubChip(0x18, 0x3)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x18, 0x2)
    SetChrFlags(0x18, 0x20)
    OP_0D()

    def lambda_3F82():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3F82)
    WaitChrThread(0x18, 2)
    Sleep(500)

    def lambda_3FA2():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3FA2)
    WaitChrThread(0x18, 2)
    Sleep(500)

    ChrTalk(
        0x18,
        "#11P#01604F#50WHehe…Haha\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0x18,
        "#11P#01609F#5SAHHAHAAH!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(8189, 1200, -8180, 0)
    MoveCamera(166, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16370, 0)
    SetCameraDistance(15370, 1000)
    SetChrSubChip(0x18, 0x4)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x18,
        (
            "#5P#01604FI see… a 'mission'\x02\x03",
            "Apparently the continuation of that time\x01",
            "I do not think so … ….?\x02\x03",
            "#01602FIsn't that right?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    MoveCamera(166, 32, 0, 4000)
    SetCameraDistance(25500, 4000)
    SetChrSubChip(0x18, 0x5)
    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x7D0)

    ChrTalk(
        0x18,
        "#5P#5S#35W#25A#01607FWazy!!!!!\x02",
    )

    Sleep(1000)
    OP_57(0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 5)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_2FEC end

    def Function_26_4175(): pass

    label("Function_26_4175")

    Sleep(120)
    SetChrSubChip(0xC, 0x1)
    WaitChrThread(0xC, 1)
    SetChrSubChip(0xC, 0x2)
    Sound(811, 0, 100, 0)
    Return()

    # Function_26_4175 end

    def Function_27_418B(): pass

    label("Function_27_418B")

    EventBegin(0x0)
    Fade(500)
    OP_68(34400, -500, -21490, 0)
    MoveCamera(45, 38, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19700, 0)
    SetChrPos(0x101, 35030, -2500, -20920, 0)
    SetChrPos(0x102, 34200, -2500, -21240, 0)
    SetChrPos(0x103, 36000, -2500, -21200, 0)
    SetChrPos(0x104, 35080, -2500, -22190, 0)
    SetChrPos(0x105, 33890, -2500, -22230, 0)
    SetChrPos(0x109, 36510, -2500, -22110, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xB, 0xFF)
    OP_93(0xB, 0x0, 0x0)
    OP_0D()

    ChrTalk(
        0xB,
        "Er, this is …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "……Wrong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "This is also … different.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, I was troubled.\x01",
            "I will not finish this condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWhat are you doing?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "Yup……\x01",
            "Asked by Mr. Abbas,\x01",
            "I am sorting out waste materials.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If it contains metal,\x01",
            "As a junk item,\x01",
            "I can convert it to Mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FHaa ~, I see.\x02\x03",
            "#00304FResidents in the Old Town\x01",
            "How kind, it is warm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FIt is ordinary thing here.\x02\x03",
            "#10300FTo the inhabitants of the old city,\x01",
            "I will do my utmost to live\x01",
            "There is a belief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FBecause life is difficult,\x01",
            "Is that so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FWell, quite\x01",
            "I can not manage money …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FThat's what people here\x01",
            "It might be strength.\x02\x03",
            "#00100F…… Hey, something to us\x01",
            "Is there anything I can do for you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "You can help me … That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well then, in the old city\x01",
            "Waste material containing metal\x01",
            "Can you please find me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I cleaned up all the way,\x01",
            "Things that have not been found yet\x01",
            "I think there is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWaste material containing metal ……\x01",
            "Okay, leave it.\x02\x03",
            "#00003F(If you search efficiently\x01",
            "Things like metal detectors\x01",
            "I want a place you want … …)\x02\x03",
            "#00000F(If you are Guillaume mentor consultation\x01",
            "It may ride. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x196, 4)
    OP_29(0x8E, 0x1, 0x6)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    OP_93(0xB, 0x0, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 34840, -2500, -21110, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_418B end

    def Function_28_46DC(): pass

    label("Function_28_46DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_477B")
    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThose who recover the waste are all right now.\x02\x03",
            "The support was over as usual,\x01",
            "Are you going to report to Abbas?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_477B")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThose who recover the waste are all right now.\x02\x03",
            "Let's find out what else you can do.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_47CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_47F2")
    Return()

    label("loc_47F2")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE4E5A8), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48A4")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6BA8), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3F01), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48A4")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_48A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_493C")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xB18A), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4DEE), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_493C")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_493C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49D4")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2DB4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8052), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49D4")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_49D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A6D")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4042), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x254E), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A6D")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B05")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4402), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8BB0), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B05")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B9E")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4132), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x66E4), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B9E")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C36")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3C78), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x136), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C36")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CCE")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9376), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9664), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CCE")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D67")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6AD6), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6F54), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D67")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DFF")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xBC5C), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9614), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DFF")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E98")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6F4), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7C24), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E98")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F30")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9B46), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x447A), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F30")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FC8")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1FAD), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x201C), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FC8")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5060")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xA4F6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6284), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5060")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5060")

    SetMapFlags(0x80)
    OP_C7(0x0, 0x0)
    OP_49()
    Sleep(30)
    PlayEffect(0x7, 0x0, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(632, 0, 100, 0)
    Sleep(600)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51E8")
    TalkBegin(0xFF)
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_64(0x0)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_64(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (1, "loc_5162"),
        (2, "loc_516B"),
        (3, "loc_5174"),
        (4, "loc_517D"),
        (5, "loc_5186"),
        (6, "loc_518F"),
        (7, "loc_5198"),
        (8, "loc_51A1"),
        (9, "loc_51AA"),
        (10, "loc_51B3"),
        (11, "loc_51BC"),
        (12, "loc_51C5"),
        (13, "loc_51CE"),
        (14, "loc_51D7"),
        (SWITCH_DEFAULT, "loc_51E0"),
    )


    label("loc_5162")

    OP_66(0x0, 0x1)
    Jump("loc_51E0")

    label("loc_516B")

    OP_66(0x1, 0x1)
    Jump("loc_51E0")

    label("loc_5174")

    OP_66(0x2, 0x1)
    Jump("loc_51E0")

    label("loc_517D")

    OP_66(0x3, 0x1)
    Jump("loc_51E0")

    label("loc_5186")

    OP_66(0x4, 0x1)
    Jump("loc_51E0")

    label("loc_518F")

    OP_66(0x5, 0x1)
    Jump("loc_51E0")

    label("loc_5198")

    OP_66(0x6, 0x1)
    Jump("loc_51E0")

    label("loc_51A1")

    OP_66(0x7, 0x1)
    Jump("loc_51E0")

    label("loc_51AA")

    OP_66(0x8, 0x1)
    Jump("loc_51E0")

    label("loc_51B3")

    OP_66(0x9, 0x1)
    Jump("loc_51E0")

    label("loc_51BC")

    OP_66(0xA, 0x1)
    Jump("loc_51E0")

    label("loc_51C5")

    OP_66(0xB, 0x1)
    Jump("loc_51E0")

    label("loc_51CE")

    OP_66(0xC, 0x1)
    Jump("loc_51E0")

    label("loc_51D7")

    OP_66(0xD, 0x1)
    Jump("loc_51E0")

    label("loc_51E0")

    TalkEnd(0xFF)
    Jump("loc_52DD")

    label("loc_51E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_5243")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A reaction ant in close proximity!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_52DD")

    label("loc_5243")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x186A0), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_529A")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Reaction ant nearby.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_52DD")

    label("loc_529A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is no reaction.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_52DD")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_28_46DC end

    def Function_29_52E4(): pass

    label("Function_29_52E4")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '废弃材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('废弃材料', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x196, 6)
    TalkEnd(0xFF)
    Return()

    # Function_29_52E4 end

    def Function_30_533F(): pass

    label("Function_30_533F")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '废弃材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('废弃材料', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x1, 0x1)
    SetScenarioFlags(0x196, 7)
    TalkEnd(0xFF)
    Return()

    # Function_30_533F end

    def Function_31_539A(): pass

    label("Function_31_539A")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('Ｕ材料', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x2, 0x1)
    SetScenarioFlags(0x197, 0)
    TalkEnd(0xFF)
    Return()

    # Function_31_539A end

    def Function_32_53F5(): pass

    label("Function_32_53F5")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '废弃材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('废弃材料', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x3, 0x1)
    SetScenarioFlags(0x197, 1)
    TalkEnd(0xFF)
    Return()

    # Function_32_53F5 end

    def Function_33_5450(): pass

    label("Function_33_5450")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '废弃材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('废弃材料', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x4, 0x1)
    SetScenarioFlags(0x197, 2)
    TalkEnd(0xFF)
    Return()

    # Function_33_5450 end

    def Function_34_54AB(): pass

    label("Function_34_54AB")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '废弃材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('废弃材料', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x5, 0x1)
    SetScenarioFlags(0x197, 3)
    TalkEnd(0xFF)
    Return()

    # Function_34_54AB end

    def Function_35_5506(): pass

    label("Function_35_5506")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '废弃材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('废弃材料', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x6, 0x1)
    SetScenarioFlags(0x197, 4)
    TalkEnd(0xFF)
    Return()

    # Function_35_5506 end

    def Function_36_5561(): pass

    label("Function_36_5561")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '废弃材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('废弃材料', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0xA, 0x1)
    SetScenarioFlags(0x19C, 0)
    TalkEnd(0xFF)
    Return()

    # Function_36_5561 end

    def Function_37_55BC(): pass

    label("Function_37_55BC")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '废弃材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('废弃材料', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0xB, 0x1)
    SetScenarioFlags(0x19C, 1)
    TalkEnd(0xFF)
    Return()

    # Function_37_55BC end

    def Function_38_5617(): pass

    label("Function_38_5617")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '废弃材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('废弃材料', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0xC, 0x1)
    SetScenarioFlags(0x19C, 2)
    TalkEnd(0xFF)
    Return()

    # Function_38_5617 end

    def Function_39_5672(): pass

    label("Function_39_5672")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '废弃材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('废弃材料', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0xD, 0x1)
    SetScenarioFlags(0x19C, 3)
    TalkEnd(0xFF)
    Return()

    # Function_39_5672 end

    def Function_40_56CD(): pass

    label("Function_40_56CD")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('Ｕ材料', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x7, 0x1)
    SetScenarioFlags(0x197, 5)
    TalkEnd(0xFF)
    Return()

    # Function_40_56CD end

    def Function_41_5728(): pass

    label("Function_41_5728")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('Ｕ材料', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x8, 0x1)
    SetScenarioFlags(0x197, 6)
    TalkEnd(0xFF)
    Return()

    # Function_41_5728 end

    def Function_42_5783(): pass

    label("Function_42_5783")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('Ｕ材料', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x9, 0x1)
    SetScenarioFlags(0x197, 7)
    TalkEnd(0xFF)
    Return()

    # Function_42_5783 end

    def Function_43_57DE(): pass

    label("Function_43_57DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('废弃材料', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_588E")

    ChrTalk(
        0xB,
        (
            "Wow …\x01",
            "Waste material containing metal\x01",
            "Did you find it so much?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hehe, it is amazing.\x01",
            "If there is only this, it is hokkehoku.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well then this\x01",
            "Can I have it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A68")

    label("loc_588E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('废弃材料', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_592F")

    ChrTalk(
        0xB,
        (
            "Waste material containing metal\x01",
            "You found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hehe, Thank you.\x01",
            "This is enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well then this\x01",
            "Can I have it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A68")

    label("loc_592F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('废弃材料', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_59BC")

    ChrTalk(
        0xB,
        (
            "Waste material containing metal\x01",
            "You found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It seems that it got together quite well ….\x01",
            "Well then this\x01",
            "Can I have it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A68")

    label("loc_59BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('废弃材料', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5A68")

    ChrTalk(
        0xB,
        (
            "Waste material containing metal\x01",
            "You found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A bit small number, but ….\x01",
            "I am glad that you looked for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well then this\x01",
            "Can I have it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A68")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Pass waste materials\x01",          # 0
            "I still try to find it\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5AD2"),
        (1, "loc_5ADA"),
        (SWITCH_DEFAULT, "loc_5B31"),
    )


    label("loc_5AD2")

    Call(0, 44)
    Jump("loc_5B31")

    label("loc_5ADA")


    ChrTalk(
        0xB,
        "Oh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well then,\x01",
            "If you think you gathered\x01",
            "Please speak out again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B31")

    label("loc_5B31")

    Return()

    # Function_43_57DE end

    def Function_44_5B32(): pass

    label("Function_44_5B32")

    EventBegin(0x0)
    Fade(500)
    OP_68(34400, -500, -21490, 0)
    MoveCamera(45, 38, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19700, 0)
    SetChrPos(0x101, 35030, -2500, -20920, 0)
    SetChrPos(0x102, 34200, -2500, -21240, 0)
    SetChrPos(0x103, 36000, -2500, -21200, 0)
    SetChrPos(0x104, 35080, -2500, -22190, 0)
    SetChrPos(0x105, 33890, -2500, -22230, 0)
    SetChrPos(0x109, 36510, -2500, -22110, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xB, 0xFF)
    OP_93(0xB, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00000FOh, please accept it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got\x07\x02",
            "Scrap\x07\x00",
            ".\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    ChrTalk(
        0xB,
        "Hehe, thank you very much.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('废弃材料', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CA3")
    OP_2C(0x8E, 0x3)
    OP_29(0x8E, 0x1, 0x8)
    Jump("loc_5CFC")

    label("loc_5CA3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('废弃材料', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5CC4")
    OP_2C(0x8E, 0x2)
    OP_29(0x8E, 0x1, 0x9)
    Jump("loc_5CFC")

    label("loc_5CC4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('废弃材料', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5CE5")
    OP_2C(0x8E, 0x1)
    OP_29(0x8E, 0x1, 0xA)
    Jump("loc_5CFC")

    label("loc_5CE5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('废弃材料', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5CFC")
    OP_29(0x8E, 0x1, 0xB)

    label("loc_5CFC")

    SubItemNumber('废弃材料', 1)
    SubItemNumber('废弃材料', 1)
    SubItemNumber('废弃材料', 1)
    SubItemNumber('废弃材料', 1)
    SubItemNumber('废弃材料', 1)
    SubItemNumber('废弃材料', 1)
    SubItemNumber('废弃材料', 1)
    SubItemNumber('废弃材料', 1)
    SubItemNumber('废弃材料', 1)
    SubItemNumber('废弃材料', 1)

    ChrTalk(
        0xB,
        (
            "Once you can convert to Mira,\x01",
            "Let me use it for reconstruction of old city\x01",
            "I will get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah, if you do it\x01",
            "I'm glad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FIf you can recover quickly\x01",
            "Sounds good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FSuch children are also doing their best,\x01",
            "I wonder what will be done somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300F… … Huh, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FWell then,\x01",
            "Shall we go?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EC1")

    ChrTalk(
        0x101,
        (
            "#00000FOh, I helped one way,\x01",
            "Let's report to Abbas.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8E, 0x1, 0xC)
    Jump("loc_5EF5")

    label("loc_5EC1")


    ChrTalk(
        0x101,
        (
            "#00000FOh, I've got other places soon.\x01",
            "I have to turn around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EF5")

    SetScenarioFlags(0x198, 0)
    OP_4C(0xB, 0xFF)
    OP_93(0xB, 0x0, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 34840, -2500, -21110, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_44_5B32 end

    def Function_45_5F2F(): pass

    label("Function_45_5F2F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(7540, 6230, -5160, 0)
    MoveCamera(64, 37, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(18930, 0)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 11100, 0, -2800, 270)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 11100, 0, -3700, 270)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0xE, 9500, 0, -2800, 90)
    SetChrPos(0x9, 9500, 0, -3700, 90)
    SetChrPos(0xA, 8000, 0, -2800, 90)
    SetChrPos(0xB, 8000, 0, -3700, 90)
    SetChrPos(0x11, 7000, 0, -2800, 90)
    SetChrPos(0x12, 7000, 0, -3700, 90)
    SetChrPos(0x10, 6000, 0, -2800, 90)
    SetChrPos(0xF, 6000, 0, -3700, 90)
    SetChrPos(0x8, 5000, 0, -3700, 90)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 990, 0, -7830, 0)
    SetChrPos(0x101, 1590, 0, -6330, 180)
    SetChrPos(0x105, 440, 0, -6060, 180)
    SetChrPos(0x102, 2500, 0, -5450, 180)
    SetChrPos(0x103, -480, 0, -5480, 180)
    SetChrPos(0x104, 490, 0, -4700, 180)
    SetChrPos(0x109, 1580, 0, -4880, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x13, 0xFF)
    ClearMapObjFlags(0x7, 0x4)
    FadeToBright(1000, 0)
    OP_68(8690, 2100, -4190, 15000)
    MoveCamera(39, 44, 0, 15000)
    OP_6E(500, 15000)
    SetCameraDistance(17780, 15000)

    def lambda_6153():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6153)
    Sleep(100)

    def lambda_6170():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6170)
    Sleep(500)

    def lambda_618D():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_618D)
    Sleep(250)

    def lambda_61AA():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_61AA)

    def lambda_61C4():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_61C4)
    Sleep(350)
    OP_93(0x17, 0x5A, 0x1F4)

    def lambda_61E8():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_61E8)
    Sleep(150)
    OP_93(0xD, 0x5A, 0x1F4)

    def lambda_620C():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_620C)

    def lambda_6226():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6226)
    Sleep(250)

    def lambda_6243():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6243)
    Sleep(600)
    OP_93(0x17, 0x10E, 0x1F4)
    OP_93(0xD, 0x10E, 0x1F4)
    Sleep(600)
    EndChrThread(0xE, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x8, 0x1)
    BeginChrThread(0x9, 3, 0, 47)
    Sleep(100)
    BeginChrThread(0xE, 3, 0, 46)
    Sleep(1000)

    def lambda_62A7():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_62A7)
    Sleep(150)

    def lambda_62C4():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_62C4)

    def lambda_62DE():
        OP_97(0xFE, 0x44C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_62DE)
    Sleep(250)

    def lambda_62FB():
        OP_97(0xFE, 0x44C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_62FB)
    Sleep(50)

    def lambda_6318():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6318)

    def lambda_6332():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6332)
    Sleep(500)
    OP_93(0x17, 0x5A, 0x1F4)

    def lambda_6356():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6356)
    Sleep(500)
    OP_93(0xD, 0x5A, 0x1F4)
    Sleep(1000)
    OP_93(0x17, 0x10E, 0x1F4)
    OP_93(0xD, 0x10E, 0x1F4)
    Sleep(500)
    EndChrThread(0xE, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x8, 0x1)
    BeginChrThread(0xA, 3, 0, 48)
    Sleep(100)
    BeginChrThread(0xB, 3, 0, 49)
    Sleep(1000)

    def lambda_63C4():
        OP_97(0xFE, 0x44C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_63C4)
    Sleep(150)

    def lambda_63E1():
        OP_97(0xFE, 0x44C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_63E1)
    Sleep(50)

    def lambda_63FE():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_63FE)
    Sleep(150)

    def lambda_641B():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_641B)
    Sleep(200)

    def lambda_6438():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6438)
    Sleep(1000)
    OP_93(0x17, 0x5A, 0x1F4)
    Sleep(500)
    OP_93(0xD, 0x5A, 0x1F4)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_93(0x17, 0x10E, 0x1F4)
    OP_93(0xD, 0x10E, 0x1F4)
    OP_0D()
    OP_68(310, 2100, -7180, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16930, 0)
    EndChrThread(0xE, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0xE, 0x3)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xA, 0x3)
    EndChrThread(0xB, 0x3)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0x17, 10930, 0, -3700, 90)
    SetChrPos(0x10, 11070, 0, 660, 135)
    SetChrPos(0xF, 12030, 0, 630, 225)
    SetChrFlags(0xF, 0x10)
    ClearMapObjFlags(0x7, 0x4)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 34490, -6500, -37750, 315)
    SetChrPos(0xA, 34490, -6500, -38950, 315)
    SetChrPos(0xB, 34840, -2220, -19610, 0)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6597")
    SetChrFlags(0xB, 0x10)

    label("loc_6597")

    SetChrPos(0xE, 32800, -6500, -36950, 315)
    SetChrPos(0x11, 5770, 0, -8300, 270)
    SetChrPos(0x12, 4420, 0, -8080, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x13,
        (
            "#04100F… … It was a hard work, the Special Affairs Division.\x02\x03",
            "Thanks to everyone in the old city\x01",
            "It seems that I regained a little energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FI am fortunate if I gained power.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FStill, various problems\x01",
            "It seems to be left … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FWald's brothers and sisters also\x01",
            "I guess I'm getting depressed for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FInitially,\x01",
            "Most of the viper\x01",
            "I have been in the hospital.\x02\x03",
            "#10300FWell, that Dino is there\x01",
            "You will follow me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThat's the best way\x01",
            "I am interested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10103FYeah……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#04100FAnyway, this is the end of the request.\x02\x03",
            "If there is something again\x01",
            "Lend me your strength in the old town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I understand.\x01",
            "Please call me anytime again.\x02",
        )
    )

    CloseMessageWindow()
    SubItemNumber('苦西红柿酱', 1)
    SubItemNumber('金属探测器', 1)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Reconstruction assistance of old city】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x8E, 0x1, 0xD)
    OP_29(0x8E, 0x4, 0x10)
    OP_4C(0x13, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 990, 0, -6330, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_45_5F2F end

    def Function_46_68C6(): pass

    label("Function_46_68C6")

    EndChrThread(0xFE, 0x1)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 500)
    Sleep(500)
    BeginChrThread(0xFE, 1, 0, 50)
    Return()

    # Function_46_68C6 end

    def Function_47_68EF(): pass

    label("Function_47_68EF")

    EndChrThread(0xFE, 0x1)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
    OP_97(0xFE, 0x3E8, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xE, 500)
    Sleep(500)
    BeginChrThread(0xFE, 1, 0, 50)
    Return()

    # Function_47_68EF end

    def Function_48_692C(): pass

    label("Function_48_692C")

    EndChrThread(0xFE, 0x1)
    OP_97(0xFE, 0x0, 0x0, 0xFA0, 0xBB8, 0x0)
    OP_97(0xFE, 0x7D0, 0x0, 0x7D0, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xB, 500)
    BeginChrThread(0xFE, 1, 0, 50)
    Return()

    # Function_48_692C end

    def Function_49_6966(): pass

    label("Function_49_6966")

    EndChrThread(0xFE, 0x1)
    OP_97(0xFE, 0x0, 0x0, 0xFA0, 0xBB8, 0x0)
    OP_97(0xFE, 0x7D0, 0x0, 0x7D0, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xA, 500)
    BeginChrThread(0xFE, 1, 0, 50)
    Return()

    # Function_49_6966 end

    def Function_50_69A0(): pass

    label("Function_50_69A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6AB8")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_69E3"),
        (1, "loc_69FD"),
        (2, "loc_6A17"),
        (3, "loc_6A31"),
        (4, "loc_6A4B"),
        (5, "loc_6A65"),
        (6, "loc_6A7F"),
        (SWITCH_DEFAULT, "loc_6A99"),
    )


    label("loc_69E3")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6AB3")

    label("loc_69FD")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("loc_6AB3")

    label("loc_6A17")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    Jump("loc_6AB3")

    label("loc_6A31")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6AB3")

    label("loc_6A4B")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("loc_6AB3")

    label("loc_6A65")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_6AB3")

    label("loc_6A7F")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6AB3")

    label("loc_6A99")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6AB3")

    label("loc_6AB3")

    Jump("Function_50_69A0")

    label("loc_6AB8")

    Return()

    # Function_50_69A0 end

    SaveToFile()

Try(main)
