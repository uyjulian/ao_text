from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Grandma Paola",          # 1
        "Vaan",                   # 2
        "Roser",                  # 3
        "Kanon",                  # 4
        "Dino",                   # 5
        "Old Man Tantos",         # 6
        "Bacchus",                # 7
        "Rimah",                  # 8
        "Melson",                 # 9
        "Kientz",                 # 10
        "Veysset",                # 11
        "Abbas",                  # 12
        "Huey",                   # 13
        "Slash",                  # 14
        "Liang",                  # 15
        "Azel",                   # 16
        "Wald",                   # 17
        "Central Square",         # 18
        "West Street",            # 19
        "Governmental District",  # 20
        "Residential Street",     # 21
        "Entertainment District", # 22
        "East Street",            # 23
        "Downtown",               # 24
        "Waterfront Area",        # 25
        "IBC",                    # 26
        "Station Street",         # 27
        "Back Street",            # 28
        "St. Ursula Byroad",      # 29
        "East Crossbell Highway", # 30
        "West Crossbell HIghway", # 31
        "Mainz Mountain Road",    # 32
        "Orchis Tower",           # 33
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

    PlaceName(-110.69000244140625, 0.0, 106.94999694824219, 0x0000, 0x0000, "Central Square")
    PlaceName(-186.3000030517578, 0.0, 112.12999725341797, 0x0000, 0x0000, "West Street")
    PlaceName(-79.63999938964844, 0.0, 209.3000030517578, 0x0000, 0x0000, "Governmental District")
    PlaceName(-256.45001220703125, 0.0, 197.8000030517578, 0x0000, 0x0000, "Residential Street")
    PlaceName(-172.5, 0.0, 188.60000610351562, 0x0000, 0x0000, "Entertainment District")
    PlaceName(-17.25, 0.0, 80.5, 0x0000, 0x0000, "East Street")
    PlaceName(23.579999923706055, 0.0, 17.25, 0x0000, 0x0000, "Downtown")
    PlaceName(14.949999809265137, 0.0, 156.39999389648438, 0x0000, 0x0000, "Waterfront Area")
    PlaceName(-14.949999809265137, 0.0, 264.5, 0x0000, 0x0000, "IBC")
    PlaceName(-97.75, 0.0, 27.600000381469727, 0x0000, 0x0000, "Station Street")
    PlaceName(-151.8000030517578, 0.0, 147.1999969482422, 0x0000, 0x0000, "Back Street")
    PlaceName(-101.19999694824219, 0.0, -8.050000190734863, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(44.849998474121094, 0.0, 96.5999984741211, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-244.9499969482422, 0.0, 110.4000015258789, 0x0000, 0x0000, "West Crossbell HIghway")
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
        "Function_7_116D",         # 07, 7
        "Function_8_1426",         # 08, 8
        "Function_9_157A",         # 09, 9
        "Function_10_1647",        # 0A, 10
        "Function_11_1712",        # 0B, 11
        "Function_12_19A5",        # 0C, 12
        "Function_13_1DE8",        # 0D, 13
        "Function_14_2025",        # 0E, 14
        "Function_15_221E",        # 0F, 15
        "Function_16_23CB",        # 10, 16
        "Function_17_2747",        # 11, 17
        "Function_18_274E",        # 12, 18
        "Function_19_2AE6",        # 13, 19
        "Function_20_2BDA",        # 14, 20
        "Function_21_2D7C",        # 15, 21
        "Function_22_2E1B",        # 16, 22
        "Function_23_2E70",        # 17, 23
        "Function_24_2EE5",        # 18, 24
        "Function_25_30D5",        # 19, 25
        "Function_26_421F",        # 1A, 26
        "Function_27_4235",        # 1B, 27
        "Function_28_4748",        # 1C, 28
        "Function_29_53A2",        # 1D, 29
        "Function_30_53F9",        # 1E, 30
        "Function_31_5450",        # 1F, 31
        "Function_32_54A7",        # 20, 32
        "Function_33_54FE",        # 21, 33
        "Function_34_5555",        # 22, 34
        "Function_35_55AC",        # 23, 35
        "Function_36_5603",        # 24, 36
        "Function_37_565A",        # 25, 37
        "Function_38_56B1",        # 26, 38
        "Function_39_5708",        # 27, 39
        "Function_40_575F",        # 28, 40
        "Function_41_57B6",        # 29, 41
        "Function_42_580D",        # 2A, 42
        "Function_43_5864",        # 2B, 43
        "Function_44_5B9B",        # 2C, 44
        "Function_45_5FB9",        # 2D, 45
        "Function_46_699B",        # 2E, 46
        "Function_47_69C4",        # 2F, 47
        "Function_48_6A01",        # 30, 48
        "Function_49_6A3B",        # 31, 49
        "Function_50_6A75",        # 32, 50
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x375, 0x0)"), scpexpr(EXPR_END)), "loc_DDF")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104C")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x3D, 1)"), scpexpr(EXPR_END)), "loc_FD5")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1047")

    label("loc_FD5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many,\x01",
            "you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1047")

    Jump("loc_1095")

    label("loc_104C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the\x01",
            "chest.\x07\x00\x02",
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
            "The "Classic Dishes That\x01",
            "Can Be Made With The\x01",
            "Oven" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_1169")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1169")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Stamina\x01",
            "Steak"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_1169")

    TalkEnd(0xFF)
    Return()

    # Function_6_10A1 end

    def Function_7_116D(): pass

    label("Function_7_116D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1308")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_127C")

    ChrTalk(
        0xFE,
        (
            "Ughhh, *hic*...\x01",
            "Alcohol's the best,\x01",
            "really...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Even so, what's that\x01",
            "stupidly huge tree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(I-It's dangerous, being\x01",
            "drunk in a place like\x01",
            "this...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F(Well, it's not like we\x01",
            "can't understand why\x01",
            "he's drinking.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1303")

    label("loc_127C")


    ChrTalk(
        0xFE,
        (
            "Ughhh, *hic*... There's\x01",
            "that stupidly huge tree.\x01",
            "Am I in heaven?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure there's lots of\x01",
            "good alcohol and pretty\x01",
            "girls, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1303")

    Jump("loc_1422")

    label("loc_1308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1316")
    Jump("loc_1422")

    label("loc_1316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1324")
    Jump("loc_1422")

    label("loc_1324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1422")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_134C")
    Call(0, 8)
    Jump("loc_13CE")

    label("loc_134C")


    ChrTalk(
        0xFE,
        (
            "Man. Even though they're\x01",
            "feeding us, I can't work\x01",
            "for free in broad daylight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm gonna have a drink\x01",
            "when this is over.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13CE")

    Jump("loc_1422")

    label("loc_13D3")


    ChrTalk(
        0xFE,
        (
            "But, the sun's really\x01",
            "bright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's poison to night\x01",
            "owls like myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1422")

    TalkEnd(0xFE)
    Return()

    # Function_7_116D end

    def Function_8_1426(): pass

    label("Function_8_1426")

    OP_4B(0x9, 0xFF)
    OP_4B(0xE, 0xFF)
    TurnDirection(0x9, 0x0, 0)

    ChrTalk(
        0x9,
        (
            "Kyahaha, that old man!\x01",
            "It's rare for him to\x01",
            "work before noon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think the landlord drove him\x01",
            "out of his apartment and told him\x01",
            "to help with the reconstruction?\x02",
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
            "Ah, Vaan. Don't say\x01",
            "anything unnecessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Shut up and help me with\x01",
            "this, will ya?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    OP_93(0x9, 0x13B, 0x0)
    OP_93(0xE, 0x13B, 0x0)
    OP_4C(0x9, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_8_1426 end

    def Function_9_157A(): pass

    label("Function_9_157A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D4")

    ChrTalk(
        0xFE,
        (
            "Now then, gotta tidy up\x01",
            "quickly today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "First to measure...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_15D4")


    ChrTalk(
        0xFE,
        (
            "Phew. It's a bit late,\x01",
            "but I can finally take a\x01",
            "breather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alright... I'll do my\x01",
            "best this afternoon!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1643")

    TalkEnd(0xFE)
    Return()

    # Function_9_157A end

    def Function_10_1647(): pass

    label("Function_10_1647")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1692")

    ChrTalk(
        0xFE,
        (
            "Papa's working for\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He's so cool♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_170E")

    label("loc_1692")

    OP_4B(0x10, 0x0)
    SetChrName("Rimah")

    ChrTalk(
        0xF,
        (
            "Papa, this broth's\x01",
            "delicious.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Melson")

    ChrTalk(
        0x10,
        (
            "Yeah, really. Papa can\x01",
            "feel the power welling\x01",
            "up inside him.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0x0)

    label("loc_170E")

    TalkEnd(0xFE)
    Return()

    # Function_10_1647 end

    def Function_11_1712(): pass

    label("Function_11_1712")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_182B")

    ChrTalk(
        0x13,
        (
            "#04100F...That's right. Since\x01",
            "you're here, I'll give\x01",
            "you this.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "[Abbas' Account]\x07\x00\x01",
            "obtained.\x02",
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
            "#00005FA "Pom!" account? You\x01",
            "play too, Abbas?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#04100FOnly when I'm free.\x02\x03",
            "If you feel like taking\x01",
            "me on, send me a\x01",
            "challenge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A1")

    label("loc_182B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1932")

    ChrTalk(
        0x13,
        (
            "#04100FThe Special Support\x01",
            "Section... You were a\x01",
            "big help today.\x02\x03",
            "The reconstruction work\x01",
            "is going smoothly thanks\x01",
            "to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHaha, you're welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FDo your best for me from\x01",
            "here on out, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#04100FYeah, of course.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_19A1")

    label("loc_1932")


    ChrTalk(
        0x13,
        (
            "#04100FNow then. With this, the\x01",
            "needed components are in\x01",
            "order.\x02\x03",
            "We've got to focus on\x01",
            "work until sunset.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19A1")

    TalkEnd(0xFE)
    Return()

    # Function_11_1712 end

    def Function_12_19A5(): pass

    label("Function_12_19A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1B0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A8D")

    ChrTalk(
        0xFE,
        (
            "Somehow, an unthinkable\x01",
            "thing has happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I saw that blue tree, I\x01",
            "thought I have to do everything\x01",
            "I can for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone will be\x01",
            "relieved if the city's a\x01",
            "little neater.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1B07")

    label("loc_1A8D")


    ChrTalk(
        0xFE,
        (
            "Because of that, I have\x01",
            "to do my best with\x01",
            "cleaning it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I do my very best,\x01",
            "I'm sure good things\x01",
            "will happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B07")

    Jump("loc_1DE4")

    label("loc_1B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1B1A")
    Jump("loc_1DE4")

    label("loc_1B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B61")

    ChrTalk(
        0xFE,
        (
            "T-To think a war...\x01",
            "That's no good. No good\x01",
            "at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE4")

    label("loc_1B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1DE4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B9D")
    Call(0, 27)
    Return()

    label("loc_1B9D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C25")
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
            "Talk\x01",             # 0
            "Give scraps\x01",      # 1
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
        (0, "loc_1C14"),
        (1, "loc_1C19"),
        (SWITCH_DEFAULT, "loc_1C25"),
    )


    label("loc_1C14")

    Jump("loc_1C25")

    label("loc_1C19")

    Call(0, 43)
    TalkEnd(0xB)
    Return()

    label("loc_1C25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C95")

    ChrTalk(
        0xFE,
        (
            "*rustle*... Umm, this\x01",
            "is... No good, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then this one... Hmm,\x01",
            "this one's a miss too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE4")

    label("loc_1C95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D33")

    ChrTalk(
        0xB,
        (
            "Can you guys search for\x01",
            "metal-containing scrap\x01",
            "for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I found most of it but I\x01",
            "bet there's still some I\x01",
            "haven't found.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D7E")

    label("loc_1D33")


    ChrTalk(
        0xFE,
        "Thanks you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm gonna sell this\x01",
            "scrap you gave us\x01",
            "properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D7E")

    Jump("loc_1DE4")

    label("loc_1D83")


    ChrTalk(
        0xFE,
        (
            "And now that my\x01",
            "stomach's full, I can\x01",
            "work hard again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks for all your\x01",
            "help, guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE4")

    TalkEnd(0xFE)
    Return()

    # Function_12_19A5 end

    def Function_13_1DE8(): pass

    label("Function_13_1DE8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1F7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ED8")

    ChrTalk(
        0xFE,
        (
            "What indeed is up with\x01",
            "that large and imposing\x01",
            "tree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Its pale blue glow... Its\x01",
            "beauty is something that I\x01",
            "can't think is of this world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if it will take\x01",
            "all of us to be with the\x01",
            "Goddess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_1F7A")

    label("loc_1ED8")


    ChrTalk(
        0xFE,
        (
            "The beauty of that large and\x01",
            "imposing tree is something that\x01",
            "I can't think is of this world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if it will take\x01",
            "all of us to be with the\x01",
            "Goddess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7A")

    Jump("loc_2021")

    label("loc_1F7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1F8D")
    Jump("loc_2021")

    label("loc_1F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2021")

    ChrTalk(
        0xFE,
        (
            "I don't really get it, but\x01",
            "it seems to have become a\x01",
            "terrible situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps it's a good idea\x01",
            "not to leave home for a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2021")

    TalkEnd(0xFE)
    Return()

    # Function_13_1DE8 end

    def Function_14_2025(): pass

    label("Function_14_2025")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_20AC")

    ChrTalk(
        0xFE,
        (
            "It's weird for my old man\x01",
            "to be without alcohol, so\x01",
            "I got him some.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Just keep drinking,\x01",
            "useless old man!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_221A")

    label("loc_20AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_20BA")
    Jump("loc_221A")

    label("loc_20BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_212A")

    ChrTalk(
        0xFE,
        (
            "Hehe, somehow, the\x01",
            "city's in a huuuge\x01",
            "uproar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say we might go to\x01",
            "war with someone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_221A")

    label("loc_212A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_221A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2194")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2152")
    Call(0, 8)
    Jump("loc_218F")

    label("loc_2152")


    ChrTalk(
        0xFE,
        (
            "Kyahaha, that old man!\x01",
            "He's almost like a good\x01",
            "citizen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_218F")

    Jump("loc_221A")

    label("loc_2194")


    ChrTalk(
        0xFE,
        (
            "Hehe, today's emergency\x01",
            "food was good too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we can each stuff like that\x01",
            "every day, reconstruction 'll\x01",
            "be done in no time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_221A")

    TalkEnd(0xFE)
    Return()

    # Function_14_2025 end

    def Function_15_221E(): pass

    label("Function_15_221E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22C1")

    ChrTalk(
        0xFE,
        (
            "It's quite something\x01",
            "that Vaan brought some\x01",
            "alcohol to his father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*chuckle*... Seeing an\x01",
            "upright uncle Bacchus\x01",
            "was quite fun, you see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23C7")

    label("loc_22C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_22CF")
    Jump("loc_23C7")

    label("loc_22CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_230B")

    ChrTalk(
        0xFE,
        (
            "*chuckle*... Wouldn't\x01",
            "that be dangerous?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23C7")

    label("loc_230B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_23C7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2361")

    ChrTalk(
        0xFE,
        (
            "*chuckle*... Your dad is\x01",
            "unexpectedly reliable,\x01",
            "Vaan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23C7")

    label("loc_2361")


    ChrTalk(
        0xFE,
        (
            "There's going to be\x01",
            "another emergency\x01",
            "feeding come evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what it's going\x01",
            "to be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23C7")

    TalkEnd(0xFE)
    Return()

    # Function_15_221E end

    def Function_16_23CB(): pass

    label("Function_16_23CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_24D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A0")

    ChrTalk(
        0xFE,
        (
            "Jed and the others\x01",
            "finally decided to help\x01",
            "us out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Although that sort of\x01",
            "thing happened, to us, Wald\x01",
            "is our precious leader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Guys... Bring him back\x01",
            "for us, somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_24CD")

    label("loc_24A0")


    ChrTalk(
        0xFE,
        (
            "Guys... Bring Wald back\x01",
            "to us, somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24CD")

    Jump("loc_2743")

    label("loc_24D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_24E0")
    Jump("loc_2743")

    label("loc_24E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2743")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26BA")

    ChrTalk(
        0xFE,
        (
            "Ah, the Special Support\x01",
            "Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FDino... Umm, those other\x01",
            "members are...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah... Thanks to you guys,\x01",
            "even Kouki, the sickest one,\x01",
            "regained consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A lot of us were\x01",
            "hospitalized but we've\x01",
            "all returned to Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well as you might expect, I\x01",
            "think it's hard to return to\x01",
            "the group right away, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But if you wait here, I\x01",
            "guess they'll probably\x01",
            "turn up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FDino...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008FIs that so...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 2)
    Jump("loc_2743")

    label("loc_26BA")


    ChrTalk(
        0xFE,
        (
            "Even so... The city is\x01",
            "noisy this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard about the question\x01",
            "of independence, I just wish\x01",
            "they'd be a little quieter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2743")

    TalkEnd(0xFE)
    Return()

    # Function_16_23CB end

    def Function_17_2747(): pass

    label("Function_17_2747")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_17_2747 end

    def Function_18_274E(): pass

    label("Function_18_274E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2966")
    SetScenarioFlags(0x191, 6)

    ChrTalk(
        0x17,
        (
            "Ah, the Support Section.\x01",
            "Thanks for your help\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "There's some pork miso left over\x01",
            "from the emergency feeding. If\x01",
            "you like, please take some.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 4)), scpexpr(EXPR_END)), "loc_2851")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x21A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x21A, 6)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    Jump("loc_289B")

    label("loc_2851")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x21B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x21B, 6)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()

    label("loc_289B")


    ChrTalk(
        0x101,
        "#00000FThanks, we accept.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10104FThis pork miso was\x01",
            "really delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes. I'm happy we'll get\x01",
            "to have it again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Haha. If you like it\x01",
            "that much, then it was\x01",
            "worth making.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AE2")

    label("loc_2966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A48")

    ChrTalk(
        0x17,
        (
            "Since I made this pork\x01",
            "miso, I should bring some\x01",
            "to my sister and Hugott.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Ah, but this belongs to\x01",
            "the people doing the\x01",
            "reconstruction work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Oh yeah, then maybe they\x01",
            "could help with washing\x01",
            "up?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2AE2")

    label("loc_2A48")


    ChrTalk(
        0x17,
        (
            "Since I made this pork\x01",
            "miso, I should bring some\x01",
            "to my sister and Hugott.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "It looks like they're\x01",
            "free today, so maybe I'll\x01",
            "ask them to help out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AE2")

    TalkEnd(0xFE)
    Return()

    # Function_18_274E end

    def Function_19_2AE6(): pass

    label("Function_19_2AE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B5E")

    ChrTalk(
        0xFE,
        (
            "*sigh*, this scene work\x01",
            "really takes it out of\x01",
            "ya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, I guess it's good\x01",
            "training, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BD6")

    label("loc_2B5E")


    ChrTalk(
        0xFE,
        (
            "Now then, I feel like\x01",
            "there's still a lot more\x01",
            "manual labor to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so... Will that\x01",
            "Veysset be all right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BD6")

    TalkEnd(0xFE)
    Return()

    # Function_19_2AE6 end

    def Function_20_2BDA(): pass

    label("Function_20_2BDA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C95")

    ChrTalk(
        0x12,
        (
            "B-But even so... Seeing\x01",
            "this destroyed apartment...\x01",
            "H-How intense!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Thank goodness it was abandoned.\x01",
            "It would have been terrible if\x01",
            "there was anyone inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D78")

    label("loc_2C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D22")

    ChrTalk(
        0x12,
        "...*burp*.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Because they said there\x01",
            "were seconds... I went\x01",
            "and overate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I should have eaten in\x01",
            "moderation...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D78")

    label("loc_2D22")


    ChrTalk(
        0x12,
        (
            "I-If I strain myself, I\x01",
            "might vomit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I should have eaten in\x01",
            "moderation...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D78")

    TalkEnd(0xFE)
    Return()

    # Function_20_2BDA end

    def Function_21_2D7C(): pass

    label("Function_21_2D7C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Those Testament baldies\x01",
            "are making rounds\x01",
            "helping us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hah. If there are guys doing\x01",
            "whatever they like in Downtown,\x01",
            "we'll beat them senseless.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_2D7C end

    def Function_22_2E1B(): pass

    label("Function_22_2E1B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Just why did that huge\x01",
            "tree appear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hyaha, I totally don't\x01",
            "get it!!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_2E1B end

    def Function_23_2E70(): pass

    label("Function_23_2E70")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Our respective\x01",
            "territories are settled\x01",
            "for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alright then, let's make\x01",
            "another patrol.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_2E70 end

    def Function_24_2EE5(): pass

    label("Function_24_2EE5")

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

    # Function_24_2EE5 end

    def Function_25_30D5(): pass

    label("Function_25_30D5")

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

    def lambda_339E():
        OP_95(0xFE, 20640, -6500, -36460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_339E)
    WaitChrThread(0x18, 1)

    def lambda_33BC():
        OP_95(0xFE, 21800, -2500, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_33BC)
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

    def lambda_3452():
        OP_95(0xFE, 41800, -2500, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3452)
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
        "#01601F#30W#5P............\x02",
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
        "#01608F#30W#5P...Damn...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Young Man's Voice",
        "#30W#2S#5P...Wald...?\x02",
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

    def lambda_35C0():
        OP_95(0xFE, 47600, -2100, -22700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_35C0)

    def lambda_35DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_35DA)
    WaitChrThread(0xC, 1)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x18,
        "#01605F#5PDino... You...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PW-Wald!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xC,
        "#4S#11PWald, it's really you!!\x02",
    )

    CloseMessageWindow()
    OP_68(42200, -1100, -22700, 1500)
    MoveCamera(53, 20, 0, 1300)
    SetCameraDistance(17000, 1300)
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_36A8():
        OP_95(0xFE, 42600, -2100, -22700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_36A8)
    WaitChrThread(0xC, 1)
    Sound(812, 0, 50, 0)
    OP_6F(0x79)
    Sleep(300)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0xC,
        (
            "#2PWhere have you been!? We\x01",
            "were really worried\x01",
            "about you, you know!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2PB-But most importantly\x01",
            "your safe... Waaaaaah!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#5P#01601F#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2PE-Everyone was seriously\x01",
            "hurt...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2PAlthough they went to\x01",
            "the hospital, none of\x01",
            "them are back yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2PB-But it's all right! As\x01",
            "long as you're here,\x01",
            "Wald...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#5P#01608F...!\x02",
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

    def lambda_38B7():
        OP_9D(0xFE, 0xAB7C, 0xFFFFF7CC, 0xFFFFA754, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_38B7)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    Sound(862, 0, 30, 0)

    ChrTalk(
        0xC,
        "#11PUwah!?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 3)

    def lambda_38FF():
        OP_A6(0xFE, 0x0, 0x32, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_38FF)
    Sleep(300)
    SetChrSubChip(0xC, 0x3)
    Sleep(100)
    SetChrSubChip(0xC, 0x4)

    ChrTalk(
        0xC,
        "#60W#2SWald...?\x02",
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
            "#11P#01603F#30W...The Saber Vipers are\x01",
            "no more.\x02\x03",
            "#01608FI won't say it again...\x01",
            "Don't follow me.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        "#50W#2S...No... It can't be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#50W#2SI mean, you are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#50W#2S...You've always been...\x01",
            "the strong leader we've\x01",
            "relied on...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(30200, -1100, -22700, 9000)
    MoveCamera(65, 11, 0, 9000)
    OP_6E(550, 9000)
    SetCameraDistance(19000, 9000)

    def lambda_3A95():
        OP_95(0xFE, 17000, -2500, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3A95)
    Sleep(500)
    SetChrSubChip(0xC, 0x5)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(230, 10, -1, -1)

    AnonymousTalk(
        0xC,
        (
            "#25A...That demon... To think\x01",
            "that monster that hurt all\x01",
            "those people was Wald!\x02",
        )
    )

    Sleep(3000)
    OP_82(0xC8, 0x0, 0xBB8, 0x7D0)
    SetMessageWindowPos(230, 20, -1, -1)

    AnonymousTalk(
        0xC,
        (
            "#20A#4SThat can't be true, can\x01",
            "it!?\x02",
        )
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

    def lambda_3BC9():
        OP_95(0xFE, 9600, 0, -13300, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3BC9)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x18, 1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    NpcTalk(
        0x11,
        "Youth's Voice",
        "S-Stop!\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(805, 0, 100, 0)
    Sound(318, 0, 40, 0)
    OP_68(7850, 1100, -6000, 2500)
    MoveCamera(35, 21, 0, 2500)
    SetCameraDistance(17000, 2500)

    def lambda_3C63():
        OP_95(0xFE, 8400, 0, -8300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3C63)
    WaitChrThread(0x18, 1)
    OP_6F(0x79)

    ChrTalk(
        0x11,
        (
            "#5PWald Wales! I-I can't\x01",
            "believe you've\x01",
            "returned...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PI won't let you do\x01",
            "anything more to this\x01",
            "Downtown that you loved...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PI will do whatever I\x01",
            "must to stop you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11P#01600F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P...What the heck are you\x01",
            "trying to say!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PYou became that monster\x01",
            "and did this to\x01",
            "Downtown...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "On top of that, you hurt\x01",
            "the subordinates you\x01",
            "loved!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PIt's too terrible!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11P#01604FHmph...\x02\x03",
            "#01602F─And who cares what Wazy\x01",
            "and you baldies have to\x01",
            "say?\x02\x03",
            "You've been outsiders\x01",
            "from the start... Didn't\x01",
            "you turn tail and run?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(250)
    OP_82(0x64, 0x0, 0xBB8, 0xFA)

    ChrTalk(
        0x11,
        "#5PD-Don't make fun of us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PThose two will\x01",
            "definitely be back!\x02",
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
            "#5PT-There's a situation! A\x01",
            "duty they must fulfill!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAnd so, even if they're away\x01",
            "from the city, I'm telling\x01",
            "you, they'll return!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "We don't know what it\x01",
            "is, but... We believe in\x01",
            "them!\x02",
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

    def lambda_4043():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_4043)
    WaitChrThread(0x18, 2)
    Sleep(500)

    def lambda_4063():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_4063)
    WaitChrThread(0x18, 2)
    Sleep(500)

    ChrTalk(
        0x18,
        "#11P#01604F#50W...Hehe... Haha...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0x18,
        "#11P#01609F#5SHahahahahaha!!\x02",
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
            "#5P#01604FI see... A "duty", huh.\x02\x03",
            "It looks like we'll be\x01",
            "able to continue from\x01",
            "back then, huh?\x02\x03",
            "#01602F─Isn't that right!?\x02",
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
        "#5P#5S#35W#25A#01607FWAZYYYYYYY!\x02",
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

    # Function_25_30D5 end

    def Function_26_421F(): pass

    label("Function_26_421F")

    Sleep(120)
    SetChrSubChip(0xC, 0x1)
    WaitChrThread(0xC, 1)
    SetChrSubChip(0xC, 0x2)
    Sound(811, 0, 100, 0)
    Return()

    # Function_26_421F end

    def Function_27_4235(): pass

    label("Function_27_4235")

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
        "Umm, this is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...No.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "This too is... No good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmm, this is tough.\x01",
            "It'll never end at this\x01",
            "rate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHey, what are you up to?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "Yeah... I'm picking out\x01",
            "scrap material like\x01",
            "Abbas told me to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Metal stuff, junk or\x01",
            "stuff that can be sold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FOh, I see.\x02\x03",
            "#00304FYou Downtowners are\x01",
            "pretty tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FThis is pretty common\x01",
            "though.\x02\x03",
            "#10300FDowntown citizens\x01",
            "believe in living\x01",
            "through hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt's because life itself\x01",
            "is hard, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FHmm, I don't think I\x01",
            "could ever match them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FThat's the strength of\x01",
            "the people here.\x02\x03",
            "#00100F...Hey there, is there\x01",
            "anything we can help you\x01",
            "with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Help, you say... Sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Can you bring metal-\x01",
            "containing scrap throughout\x01",
            "Downtown here for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I found most of it but I\x01",
            "bet there's still some I\x01",
            "haven't found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FScrap metal, huh...\x01",
            "Alright, leave it to us.\x02\x03",
            "#00003F(For an efficient search,\x01",
            "I'd want a something like\x01",
            "a metal detector...)\x02\x03",
            "#00000F(Maybe we should ask\x01",
            "Master Guilliaume for\x01",
            "advice.)\x02",
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

    # Function_27_4235 end

    def Function_28_4748(): pass

    label("Function_28_4748")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4862")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47FE")
    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FWe're through with the\x01",
            "scrap collection.\x02\x03",
            "We've finished helping\x01",
            "everywhere, so shall we\x01",
            "go report to Abbas?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_47FE")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FWe're through with the\x01",
            "scrap collection.\x02\x03",
            "Let's look for other\x01",
            "ways we can help.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_4862")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4887")
    Return()

    label("loc_4887")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE4E5A8), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4939")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6BA8), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3F01), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4939")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49D1")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xB18A), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4DEE), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49D1")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_49D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A69")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2DB4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8052), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A69")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B02")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4042), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x254E), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B02")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B9A")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4402), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8BB0), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B9A")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C33")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4132), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x66E4), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C33")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CCB")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3C78), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x136), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CCB")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4CCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D63")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9376), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9664), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D63")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DFC")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6AD6), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6F54), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DFC")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x197, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E94")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xBC5C), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9614), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E94")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F2D")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6F4), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7C24), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F2D")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FC5")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x9B46), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x447A), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FC5")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_505D")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1FAD), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x201C), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_505D")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_505D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50F5")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xA4F6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6284), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_50F5")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50F5")

    SetMapFlags(0x80)
    OP_C7(0x0, 0x0)
    OP_49()
    Sleep(30)
    PlayEffect(0x7, 0x0, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(632, 0, 100, 0)
    Sleep(600)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_527D")
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
        (1, "loc_51F7"),
        (2, "loc_5200"),
        (3, "loc_5209"),
        (4, "loc_5212"),
        (5, "loc_521B"),
        (6, "loc_5224"),
        (7, "loc_522D"),
        (8, "loc_5236"),
        (9, "loc_523F"),
        (10, "loc_5248"),
        (11, "loc_5251"),
        (12, "loc_525A"),
        (13, "loc_5263"),
        (14, "loc_526C"),
        (SWITCH_DEFAULT, "loc_5275"),
    )


    label("loc_51F7")

    OP_66(0x0, 0x1)
    Jump("loc_5275")

    label("loc_5200")

    OP_66(0x1, 0x1)
    Jump("loc_5275")

    label("loc_5209")

    OP_66(0x2, 0x1)
    Jump("loc_5275")

    label("loc_5212")

    OP_66(0x3, 0x1)
    Jump("loc_5275")

    label("loc_521B")

    OP_66(0x4, 0x1)
    Jump("loc_5275")

    label("loc_5224")

    OP_66(0x5, 0x1)
    Jump("loc_5275")

    label("loc_522D")

    OP_66(0x6, 0x1)
    Jump("loc_5275")

    label("loc_5236")

    OP_66(0x7, 0x1)
    Jump("loc_5275")

    label("loc_523F")

    OP_66(0x8, 0x1)
    Jump("loc_5275")

    label("loc_5248")

    OP_66(0x9, 0x1)
    Jump("loc_5275")

    label("loc_5251")

    OP_66(0xA, 0x1)
    Jump("loc_5275")

    label("loc_525A")

    OP_66(0xB, 0x1)
    Jump("loc_5275")

    label("loc_5263")

    OP_66(0xC, 0x1)
    Jump("loc_5275")

    label("loc_526C")

    OP_66(0xD, 0x1)
    Jump("loc_5275")

    label("loc_5275")

    TalkEnd(0xFF)
    Jump("loc_539B")

    label("loc_527D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_52EA")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There's a reaction\x01",
            "extremely close by!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_539B")

    label("loc_52EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x186A0), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_5354")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There's a reaction in\x01",
            "the vicinity.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_539B")

    label("loc_5354")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There's no reaction.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_539B")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_28_4748 end

    def Function_29_53A2(): pass

    label("Function_29_53A2")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x196, 6)
    TalkEnd(0xFF)
    Return()

    # Function_29_53A2 end

    def Function_30_53F9(): pass

    label("Function_30_53F9")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x1, 0x1)
    SetScenarioFlags(0x196, 7)
    TalkEnd(0xFF)
    Return()

    # Function_30_53F9 end

    def Function_31_5450(): pass

    label("Function_31_5450")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x38E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x2, 0x1)
    SetScenarioFlags(0x197, 0)
    TalkEnd(0xFF)
    Return()

    # Function_31_5450 end

    def Function_32_54A7(): pass

    label("Function_32_54A7")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x3, 0x1)
    SetScenarioFlags(0x197, 1)
    TalkEnd(0xFF)
    Return()

    # Function_32_54A7 end

    def Function_33_54FE(): pass

    label("Function_33_54FE")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x4, 0x1)
    SetScenarioFlags(0x197, 2)
    TalkEnd(0xFF)
    Return()

    # Function_33_54FE end

    def Function_34_5555(): pass

    label("Function_34_5555")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x5, 0x1)
    SetScenarioFlags(0x197, 3)
    TalkEnd(0xFF)
    Return()

    # Function_34_5555 end

    def Function_35_55AC(): pass

    label("Function_35_55AC")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x6, 0x1)
    SetScenarioFlags(0x197, 4)
    TalkEnd(0xFF)
    Return()

    # Function_35_55AC end

    def Function_36_5603(): pass

    label("Function_36_5603")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0xA, 0x1)
    SetScenarioFlags(0x19C, 0)
    TalkEnd(0xFF)
    Return()

    # Function_36_5603 end

    def Function_37_565A(): pass

    label("Function_37_565A")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0xB, 0x1)
    SetScenarioFlags(0x19C, 1)
    TalkEnd(0xFF)
    Return()

    # Function_37_565A end

    def Function_38_56B1(): pass

    label("Function_38_56B1")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0xC, 0x1)
    SetScenarioFlags(0x19C, 2)
    TalkEnd(0xFF)
    Return()

    # Function_38_56B1 end

    def Function_39_5708(): pass

    label("Function_39_5708")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x328, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0xD, 0x1)
    SetScenarioFlags(0x19C, 3)
    TalkEnd(0xFF)
    Return()

    # Function_39_5708 end

    def Function_40_575F(): pass

    label("Function_40_575F")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x38E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x7, 0x1)
    SetScenarioFlags(0x197, 5)
    TalkEnd(0xFF)
    Return()

    # Function_40_575F end

    def Function_41_57B6(): pass

    label("Function_41_57B6")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x38E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x8, 0x1)
    SetScenarioFlags(0x197, 6)
    TalkEnd(0xFF)
    Return()

    # Function_41_57B6 end

    def Function_42_580D(): pass

    label("Function_42_580D")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x38E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_65(0x9, 0x1)
    SetScenarioFlags(0x197, 7)
    TalkEnd(0xFF)
    Return()

    # Function_42_580D end

    def Function_43_5864(): pass

    label("Function_43_5864")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5912")

    ChrTalk(
        0xB,
        (
            "Wow! You found this much\x01",
            "metal-containing scrap?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha, amazing. I can\x01",
            "definitely be satisfied\x01",
            "with these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "So, are you giving them\x01",
            "to me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AC5")

    label("loc_5912")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_59A3")

    ChrTalk(
        0xB,
        (
            "You found some scrap\x01",
            "metal, didn't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha, thanks. This\x01",
            "should be plenty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "So, are you giving them\x01",
            "to me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AC5")

    label("loc_59A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5A2B")

    ChrTalk(
        0xB,
        (
            "You found some scrap\x01",
            "metal, didn't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It looks like you got a\x01",
            "bunch. So... are you\x01",
            "giving them to me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AC5")

    label("loc_5A2B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5AC5")

    ChrTalk(
        0xB,
        (
            "You found some scrap\x01",
            "metal, didn't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Not too much, but...\x01",
            "It's the thought that\x01",
            "counts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "So, are you giving them\x01",
            "to me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AC5")

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
            "Give scraps\x01",               # 0
            "Search a little more\x01",      # 1
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
        (0, "loc_5B36"),
        (1, "loc_5B3E"),
        (SWITCH_DEFAULT, "loc_5B9A"),
    )


    label("loc_5B36")

    Call(0, 44)
    Jump("loc_5B9A")

    label("loc_5B3E")


    ChrTalk(
        0xB,
        "Oh, is that so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Alright then, come to\x01",
            "speak to me again once\x01",
            "you're through.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B9A")

    label("loc_5B9A")

    Return()

    # Function_43_5864 end

    def Function_44_5B9B(): pass

    label("Function_44_5B9B")

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
        "#00000FSure, here you go.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Handed over obtained\x01\x07\x02",
            "scrap\x07\x00",
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
        "Haha, thanks.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D00")
    OP_2C(0x8E, 0x3)
    OP_29(0x8E, 0x1, 0x8)
    Jump("loc_5D59")

    label("loc_5D00")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5D21")
    OP_2C(0x8E, 0x2)
    OP_29(0x8E, 0x1, 0x9)
    Jump("loc_5D59")

    label("loc_5D21")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5D42")
    OP_2C(0x8E, 0x1)
    OP_29(0x8E, 0x1, 0xA)
    Jump("loc_5D59")

    label("loc_5D42")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x328, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5D59")
    OP_29(0x8E, 0x1, 0xB)

    label("loc_5D59")

    SubItemNumber(0x328, 1)
    SubItemNumber(0x328, 1)
    SubItemNumber(0x328, 1)
    SubItemNumber(0x328, 1)
    SubItemNumber(0x328, 1)
    SubItemNumber(0x328, 1)
    SubItemNumber(0x328, 1)
    SubItemNumber(0x328, 1)
    SubItemNumber(0x328, 1)
    SubItemNumber(0x328, 1)

    ChrTalk(
        0xB,
        (
            "I'll sell them for money\x01",
            "for reconstructing\x01",
            "Downtown!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, thanks for your\x01",
            "help with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FI hope the\x01",
            "reconstruction's\x01",
            "completed soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FEven a child like this is\x01",
            "doing their best. It'll\x01",
            "happen sooner or later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHaha, that's true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FAlright then. It's time\x01",
            "for us to be going.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F3E")

    ChrTalk(
        0x101,
        (
            "#00000FYeah, we're done helping\x01",
            "everyone. Let's check in\x01",
            "with Abbas.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8E, 0x1, 0xC)
    Jump("loc_5F7F")

    label("loc_5F3E")


    ChrTalk(
        0x101,
        (
            "#00000FYeah, it's about time\x01",
            "for us to help somewhere\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F7F")

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

    # Function_44_5B9B end

    def Function_45_5FB9(): pass

    label("Function_45_5FB9")

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

    def lambda_61DD():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_61DD)
    Sleep(100)

    def lambda_61FA():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_61FA)
    Sleep(500)

    def lambda_6217():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6217)
    Sleep(250)

    def lambda_6234():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6234)

    def lambda_624E():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_624E)
    Sleep(350)
    OP_93(0x17, 0x5A, 0x1F4)

    def lambda_6272():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6272)
    Sleep(150)
    OP_93(0xD, 0x5A, 0x1F4)

    def lambda_6296():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6296)

    def lambda_62B0():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_62B0)
    Sleep(250)

    def lambda_62CD():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_62CD)
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

    def lambda_6331():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6331)
    Sleep(150)

    def lambda_634E():
        OP_97(0xFE, 0x5DC, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_634E)

    def lambda_6368():
        OP_97(0xFE, 0x44C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6368)
    Sleep(250)

    def lambda_6385():
        OP_97(0xFE, 0x44C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6385)
    Sleep(50)

    def lambda_63A2():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_63A2)

    def lambda_63BC():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_63BC)
    Sleep(500)
    OP_93(0x17, 0x5A, 0x1F4)

    def lambda_63E0():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_63E0)
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

    def lambda_644E():
        OP_97(0xFE, 0x44C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_644E)
    Sleep(150)

    def lambda_646B():
        OP_97(0xFE, 0x44C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_646B)
    Sleep(50)

    def lambda_6488():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6488)
    Sleep(150)

    def lambda_64A5():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_64A5)
    Sleep(200)

    def lambda_64C2():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_64C2)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6621")
    SetChrFlags(0xB, 0x10)

    label("loc_6621")

    SetChrPos(0xE, 32800, -6500, -36950, 315)
    SetChrPos(0x11, 5770, 0, -8300, 270)
    SetChrPos(0x12, 4420, 0, -8080, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x13,
        (
            "#04100F...Good work, Special\x01",
            "Support Section.\x02\x03",
            "Thanks to you, the people\x01",
            "of Downtown have regained\x01",
            "some of their spirit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI'm just happy we could\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FThere's still plenty of\x01",
            "problems left, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FWald's underlings will\x01",
            "probably be depressed\x01",
            "for quite a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FAlmost all the Vipers\x01",
            "were hospitalized to\x01",
            "begin with.\x02\x03",
            "#10300FThey'll probably all\x01",
            "follow Dino before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThat would be for the\x01",
            "best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10103FThat's right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#04100FAnyhow, with this our\x01",
            "request is complete.\x02\x03",
            "Please assist the people\x01",
            "of Downtown if they need\x01",
            "your help again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, of course. Please\x01",
            "call us anytime.\x02",
        )
    )

    CloseMessageWindow()
    SubItemNumber(0x340, 1)
    SubItemNumber(0x375, 1)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Downtown\x01",
            "Reconstruction: Help\x01",
            "Wanted]\x07\x00",
            " completed!\x02",
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

    # Function_45_5FB9 end

    def Function_46_699B(): pass

    label("Function_46_699B")

    EndChrThread(0xFE, 0x1)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 500)
    Sleep(500)
    BeginChrThread(0xFE, 1, 0, 50)
    Return()

    # Function_46_699B end

    def Function_47_69C4(): pass

    label("Function_47_69C4")

    EndChrThread(0xFE, 0x1)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
    OP_97(0xFE, 0x3E8, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xE, 500)
    Sleep(500)
    BeginChrThread(0xFE, 1, 0, 50)
    Return()

    # Function_47_69C4 end

    def Function_48_6A01(): pass

    label("Function_48_6A01")

    EndChrThread(0xFE, 0x1)
    OP_97(0xFE, 0x0, 0x0, 0xFA0, 0xBB8, 0x0)
    OP_97(0xFE, 0x7D0, 0x0, 0x7D0, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xB, 500)
    BeginChrThread(0xFE, 1, 0, 50)
    Return()

    # Function_48_6A01 end

    def Function_49_6A3B(): pass

    label("Function_49_6A3B")

    EndChrThread(0xFE, 0x1)
    OP_97(0xFE, 0x0, 0x0, 0xFA0, 0xBB8, 0x0)
    OP_97(0xFE, 0x7D0, 0x0, 0x7D0, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xA, 500)
    BeginChrThread(0xFE, 1, 0, 50)
    Return()

    # Function_49_6A3B end

    def Function_50_6A75(): pass

    label("Function_50_6A75")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B8D")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6AB8"),
        (1, "loc_6AD2"),
        (2, "loc_6AEC"),
        (3, "loc_6B06"),
        (4, "loc_6B20"),
        (5, "loc_6B3A"),
        (6, "loc_6B54"),
        (SWITCH_DEFAULT, "loc_6B6E"),
    )


    label("loc_6AB8")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6B88")

    label("loc_6AD2")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("loc_6B88")

    label("loc_6AEC")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    Jump("loc_6B88")

    label("loc_6B06")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6B88")

    label("loc_6B20")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("loc_6B88")

    label("loc_6B3A")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_6B88")

    label("loc_6B54")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6B88")

    label("loc_6B6E")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_6B88")

    label("loc_6B88")

    Jump("Function_50_6A75")

    label("loc_6B8D")

    Return()

    # Function_50_6A75 end

    SaveToFile()

Try(main)
