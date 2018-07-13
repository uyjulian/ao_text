from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0400.bin",                # FileName
        "c0400",                    # MapName
        "c0400",                    # Location
        0x0022,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("c0400", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 34, 0, 5, 0, 6],
    )

    BuildStringList((
        "c0400",                  # 0
        "Polise",                 # 1
        "Tap",                    # 2
        "Tello",                  # 3
        "Barker Pim",             # 4
        "Sophille",               # 5
        "Lamanda",                # 6
        "Bunny Girl",             # 7
        "Tourist",                # 8
        "Tourist",                # 9
        "Patrol Officer Kate",    # 10
        "Policeman",              # 11
        "Patrol Car",             # 12
        "Mary",                   # 13
        "車",                     # 14
        "Black Transport",        # 15
        "Central Square",         # 16
        "West Street",            # 17
        "Governmental District",  # 18
        "Residential Street",     # 19
        "Entertainment District", # 20
        "East Street",            # 21
        "Downtown",               # 22
        "Waterfront Area",        # 23
        "IBC",                    # 24
        "Station Street",         # 25
        "Back Street",            # 26
        "St. Ursula Byroad",      # 27
        "East Crossbell Highway", # 28
        "West Crossbell HIghway", # 29
        "Mainz Mountain Road",    # 30
        "Orchis Tower",           # 31
    ))

    AddCharChip((
        "chr/ch36300.itc",                   # 00
        "chr/ch24400.itc",                   # 01
        "chr/ch20400.itc",                   # 02
        "chr/ch25900.itc",                   # 03
        "chr/ch34500.itc",                   # 04
        "chr/ch21900.itc",                   # 05
        "chr/ch27100.itc",                   # 06
        "chr/ch33200.itc",                   # 07
        "chr/ch32300.itc",                   # 08
        "chr/ch30600.itc",                   # 09
        "chr/ch49100.itc",                   # 0A
        "chr/ch49200.itc",                   # 0B
        "chr/ch48900.itc",                   # 0C
        "chr/ch30000.itc",                   # 0D
    ))

    DeclNpc(379,     1769,    28049,   315,  261,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(1830,    1769,    27899,   315,  261,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(15439,   0,       10340,   45,   261,  0x0, 0,   2,   0,   0,   4,   0,   14,  255,  0)
    DeclNpc(4360,    0,       4294956336, 310,  261,  0x0, 0,   3,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(4294956546, 1759,    24469,   175,  261,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4294917296, 9,       12069,   220,  257,  0x0, 0,   5,   0,   0,   2,   0,   13,  255,  0)
    DeclNpc(4294945247, 0,       12489,   175,  261,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4294965456, 1990,    19209,   0,    385,  0x0, 0,   7,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294964056, 1990,    19010,   0,    385,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(13630,   0,       1000,    270,  389,  0x0, 0,   9,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294956727, 1759,    15760,   180,  389,  0x0, 0,   13,  0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 40,  -2.0,                  35.0,                  1.0,                   25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   0.3999999761581421,    -17.5,                 -0.19999998807907104,  1.0])

    PlaceName(90.5999984741211, 0.0, -111.88999938964844, 0x0000, 0x0000, "Central Square")
    PlaceName(-19.209999084472656, 0.0, -104.37999725341797, 0x0000, 0x0000, "West Street")
    PlaceName(135.69000244140625, 0.0, 36.7400016784668, 0x0000, 0x0000, "Governmental District")
    PlaceName(-121.08000183105469, 0.0, 20.040000915527344, 0x0000, 0x0000, "Residential Street")
    PlaceName(0.8399999737739563, 0.0, 6.679999828338623, 0x0000, 0x0000, "Entertainment District")
    PlaceName(226.2899932861328, 0.0, -150.3000030517578, 0x0000, 0x0000, "East Street")
    PlaceName(285.57000732421875, 0.0, -242.14999389648438, 0x0000, 0x0000, "Downtown")
    PlaceName(273.04998779296875, 0.0, -40.08000183105469, 0x0000, 0x0000, "Waterfront Area")
    PlaceName(229.6300048828125, 0.0, 116.9000015258789, 0x0000, 0x0000, "IBC")
    PlaceName(109.38999938964844, 0.0, -227.1199951171875, 0x0000, 0x0000, "Station Street")
    PlaceName(30.899999618530273, 0.0, -53.439998626708984, 0x0000, 0x0000, "Back Street")
    PlaceName(104.37999725341797, 0.0, -278.8900146484375, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(316.4700012207031, 0.0, -126.91999816894531, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-104.37999725341797, 0.0, -106.87999725341797, 0x0000, 0x0000, "West Crossbell HIghway")
    PlaceName(-94.36000061035156, 0.0, 60.119998931884766, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(124.0, 0.0, 255.0, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(53.86000061035156, 0.0, -135.27000427246094, 0x0000, 0x0051, "")
    PlaceName(143.6199951171875, 0.0, -91.8499984741211, 0x0000, 0x0054, "")
    PlaceName(94.7699966430664, 0.0, -148.6300048828125, 0x0000, 0x0057, "")
    PlaceName(52.61000061035156, 0.0, -86.83999633789062, 0x0000, 0x0053, "")
    PlaceName(86.83999633789062, 0.0, -46.7599983215332, 0x0000, 0x0053, "")
    PlaceName(2.0899999141693115, 0.0, -95.19000244140625, 0x0000, 0x0053, "")
    PlaceName(-14.199999809265137, 0.0, -60.119998931884766, 0x0000, 0x0053, "")
    PlaceName(25.889999389648438, 0.0, -6.679999828338623, 0x0000, 0x0052, "")
    PlaceName(33.81999969482422, 0.0, -28.389999389648438, 0x0000, 0x0053, "")
    PlaceName(48.43000030517578, 0.0, -42.59000015258789, 0x0000, 0x0053, "")
    PlaceName(96.02999877929688, 0.0, 75.98999786376953, 0x0000, 0x0051, "")
    PlaceName(283.07000732421875, 0.0, -150.3000030517578, 0x0000, 0x0052, "")
    PlaceName(254.67999267578125, 0.0, -301.44000244140625, 0x0000, 0x0053, "")
    PlaceName(232.97000122070312, 0.0, -270.5400085449219, 0x0000, 0x0053, "")

    ChipFrameInfo(1488, 0)                                       # 0

    ScpFunction((
        "Function_0_5D0",          # 00, 0
        "Function_1_680",          # 01, 1
        "Function_2_6AB",          # 02, 2
        "Function_3_838",          # 03, 3
        "Function_4_989",          # 04, 4
        "Function_5_A90",          # 05, 5
        "Function_6_F3A",          # 06, 6
        "Function_7_12B7",         # 07, 7
        "Function_8_15C3",         # 08, 8
        "Function_9_1803",         # 09, 9
        "Function_10_286F",        # 0A, 10
        "Function_11_31DD",        # 0B, 11
        "Function_12_3C20",        # 0C, 12
        "Function_13_4483",        # 0D, 13
        "Function_14_50E0",        # 0E, 14
        "Function_15_5B79",        # 0F, 15
        "Function_16_678D",        # 10, 16
        "Function_17_682E",        # 11, 17
        "Function_18_691A",        # 12, 18
        "Function_19_6B0D",        # 13, 19
        "Function_20_6B48",        # 14, 20
        "Function_21_6D25",        # 15, 21
        "Function_22_6D8A",        # 16, 22
        "Function_23_71E8",        # 17, 23
        "Function_24_7285",        # 18, 24
        "Function_25_72BC",        # 19, 25
        "Function_26_72E9",        # 1A, 26
        "Function_27_7323",        # 1B, 27
        "Function_28_7345",        # 1C, 28
        "Function_29_737F",        # 1D, 29
        "Function_30_73BA",        # 1E, 30
        "Function_31_7411",        # 1F, 31
        "Function_32_74B7",        # 20, 32
        "Function_33_879B",        # 21, 33
        "Function_34_8930",        # 22, 34
        "Function_35_8E66",        # 23, 35
        "Function_36_8FC0",        # 24, 36
        "Function_37_A816",        # 25, 37
        "Function_38_B4F9",        # 26, 38
        "Function_39_B526",        # 27, 39
        "Function_40_C10E",        # 28, 40
        "Function_41_C53D",        # 29, 41
    ))


    def Function_0_5D0(): pass

    label("Function_0_5D0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_608"),
        (1, "loc_614"),
        (2, "loc_620"),
        (3, "loc_62C"),
        (4, "loc_638"),
        (5, "loc_644"),
        (6, "loc_650"),
        (SWITCH_DEFAULT, "loc_65C"),
    )


    label("loc_608")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_668")

    label("loc_614")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_668")

    label("loc_620")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_668")

    label("loc_62C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_668")

    label("loc_638")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_668")

    label("loc_644")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_668")

    label("loc_650")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_668")

    label("loc_65C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_668")

    label("loc_668")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_67F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_668")

    label("loc_67F")

    Return()

    # Function_0_5D0 end

    def Function_1_680(): pass

    label("Function_1_680")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6AA")
    OP_94(0xFE, 0xED8, 0xFFFFEC96, 0x1AE0, 0xFFFFDE22, 0x3E8)
    Sleep(300)
    Jump("Function_1_680")

    label("loc_6AA")

    Return()

    # Function_1_680 end

    def Function_2_6AB(): pass

    label("Function_2_6AB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_837")
    SetChrPos(0xFE, -50000, 10, 12070, 220)
    OP_95(0xFE, -18740, 10, 10280, 1500, 0x0)
    OP_95(0xFE, -2040, 1770, 9880, 1500, 0x0)
    OP_95(0xFE, 30970, 0, 12150, 1500, 0x0)
    Sleep(1500)
    SetChrPos(0xFE, 30210, 0, 8600, 270)
    OP_95(0xFE, 17210, 0, 8600, 1500, 0x0)
    OP_95(0xFE, 15010, 0, 6790, 1500, 0x0)
    OP_95(0xFE, 10210, 0, -960, 1500, 0x0)
    OP_95(0xFE, 8450, 0, -7690, 1500, 0x0)
    OP_95(0xFE, 10100, 0, -11960, 1500, 0x0)
    OP_95(0xFE, 28170, 0, -38880, 1500, 0x0)
    Sleep(1500)
    SetChrPos(0xFE, 28170, 0, -38880, 315)
    OP_95(0xFE, 9370, 0, -17000, 1500, 0x0)
    OP_95(0xFE, 4280, 0, -11560, 1500, 0x0)
    OP_95(0xFE, -4810, 0, -3900, 1500, 0x0)
    OP_95(0xFE, -13140, 0, 1410, 1500, 0x0)
    OP_95(0xFE, -21060, 0, 5360, 1500, 0x0)
    OP_95(0xFE, -26790, 0, 8090, 1500, 0x0)
    OP_95(0xFE, -50000, 10, 12070, 1500, 0x0)
    Sleep(1500)
    Jump("Function_2_6AB")

    label("loc_837")

    Return()

    # Function_2_6AB end

    def Function_3_838(): pass

    label("Function_3_838")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_988")
    SetChrPos(0xFE, 28170, 0, -38880, 315)
    OP_95(0xFE, 9370, 0, -17000, 1500, 0x0)
    OP_95(0xFE, 4280, 0, -11560, 1500, 0x0)
    OP_95(0xFE, -4810, 0, -3900, 1500, 0x0)
    OP_95(0xFE, -13140, 0, 1410, 1500, 0x0)
    OP_95(0xFE, -21060, 0, 5360, 1500, 0x0)
    OP_95(0xFE, -26790, 0, 8090, 1500, 0x0)
    OP_95(0xFE, -50000, 10, 12070, 1500, 0x0)
    Sleep(1500)
    SetChrPos(0xFE, -50000, 10, 12070, 220)
    OP_95(0xFE, -50000, 10, 12070, 1500, 0x0)
    OP_95(0xFE, -26790, 0, 8090, 1500, 0x0)
    OP_95(0xFE, -21060, 0, 5360, 1500, 0x0)
    OP_95(0xFE, -13140, 0, 1410, 1500, 0x0)
    OP_95(0xFE, -4810, 0, -3900, 1500, 0x0)
    OP_95(0xFE, 4280, 0, -11560, 1500, 0x0)
    OP_95(0xFE, 9370, 0, -17000, 1500, 0x0)
    Sleep(1500)
    Jump("Function_3_838")

    label("loc_988")

    Return()

    # Function_3_838 end

    def Function_4_989(): pass

    label("Function_4_989")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A8F")
    OP_95(0xFE, 8780, 0, 6460, 1000, 0x0)
    OP_95(0xFE, 2270, 0, 3060, 1000, 0x0)
    OP_95(0xFE, -5460, 0, 2360, 1000, 0x0)
    OP_95(0xFE, -14070, 0, 5650, 1000, 0x0)
    OP_95(0xFE, -19800, 0, 8020, 1000, 0x0)
    OP_95(0xFE, -26870, 0, 10100, 1000, 0x0)
    Sleep(1500)
    OP_95(0xFE, -19800, 0, 8020, 1000, 0x0)
    OP_95(0xFE, -14070, 0, 5650, 1000, 0x0)
    OP_95(0xFE, -5460, 0, 2360, 1000, 0x0)
    OP_95(0xFE, 2270, 0, 3060, 1000, 0x0)
    OP_95(0xFE, 8780, 0, 6460, 1000, 0x0)
    OP_95(0xFE, 11400, 0, 7650, 1000, 0x0)
    Sleep(1500)
    Jump("Function_4_989")

    label("loc_A8F")

    Return()

    # Function_4_989 end

    def Function_5_A90(): pass

    label("Function_5_A90")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCB")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B6D")
    SetChrPos(0x0, 21040, 0, 11840, 270)
    SetChrPos(0x1, 21040, 0, 11840, 270)
    SetChrPos(0x2, 21040, 0, 11840, 270)
    SetChrPos(0x3, 21040, 0, 11840, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B40")
    SetChrPos(0x4, 21040, 0, 11840, 270)
    SetChrPos(0x5, 21040, 0, 11840, 270)
    Jump("loc_B5F")

    label("loc_B40")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B5F")
    SetChrPos(0x4, 21040, 0, 11840, 270)

    label("loc_B5F")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CCB")

    label("loc_B6D")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C2A")
    SetChrPos(0x0, -39280, 0, 12420, 90)
    SetChrPos(0x1, -39280, 0, 12420, 90)
    SetChrPos(0x2, -39280, 0, 12420, 90)
    SetChrPos(0x3, -39280, 0, 12420, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFD")
    SetChrPos(0x4, -39280, 0, 12420, 90)
    SetChrPos(0x5, -39280, 0, 12420, 90)
    Jump("loc_C1C")

    label("loc_BFD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C1C")
    SetChrPos(0x4, -39280, 0, 12420, 90)

    label("loc_C1C")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CCB")

    label("loc_C2A")

    SetChrPos(0x0, 13270, 0, -19100, 315)
    SetChrPos(0x1, 13270, 0, -19100, 315)
    SetChrPos(0x2, 13270, 0, -19100, 315)
    SetChrPos(0x3, 13270, 0, -19100, 315)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA3")
    SetChrPos(0x4, 13270, 0, -19100, 315)
    SetChrPos(0x5, 13270, 0, -19100, 315)
    Jump("loc_CC2")

    label("loc_CA3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC2")
    SetChrPos(0x4, 13270, 0, -19100, 315)

    label("loc_CC2")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CCB")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CE2")
    Jump("loc_E16")

    label("loc_CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CF0")
    Jump("loc_E16")

    label("loc_CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CFE")
    Jump("loc_E16")

    label("loc_CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D38")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xA, 0xC)
    SetChrPos(0xE, -25880, 160, 14850, 175)
    SetChrChipByIndex(0x8, 0xA)
    SetChrChipByIndex(0x9, 0xB)
    Jump("loc_E16")

    label("loc_D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D46")
    Jump("loc_E16")

    label("loc_D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D60")
    TurnDirection(0x9, 0x8, 0)
    SetChrFlags(0x9, 0x10)
    Jump("loc_E16")

    label("loc_D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D7C")
    BeginChrThread(0xD, 0, 0, 3)
    Jump("loc_E16")

    label("loc_D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D8A")
    Jump("loc_E16")

    label("loc_D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D9D")
    ClearChrFlags(0x12, 0x80)
    Jump("loc_E16")

    label("loc_D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_DB0")
    ClearChrFlags(0x12, 0x80)
    Jump("loc_E16")

    label("loc_DB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DC3")
    ClearChrFlags(0x12, 0x80)
    Jump("loc_E16")

    label("loc_DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_DFD")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xA, 0xC)
    SetChrPos(0xE, -25880, 160, 14850, 175)
    SetChrChipByIndex(0x8, 0xA)
    SetChrChipByIndex(0x9, 0xB)
    Jump("loc_E16")

    label("loc_DFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_E16")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    BeginChrThread(0xD, 0, 0, 3)

    label("loc_E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E47")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E47")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 13630, 0, 1000, 270)

    label("loc_E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E5B")
    ClearScenarioFlags(0x22, 0)
    Event(0, 18)
    Jump("loc_EBF")

    label("loc_E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_E6F")
    ClearScenarioFlags(0x22, 1)
    Event(0, 20)
    Jump("loc_EBF")

    label("loc_E6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_E88")
    ClearScenarioFlags(0x22, 2)
    SetChrFlags(0x11, 0x80)
    Event(0, 22)
    Jump("loc_EBF")

    label("loc_E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_E9F")
    ClearScenarioFlags(0x22, 3)
    SetScenarioFlags(0x1, 2)
    Event(0, 33)
    Jump("loc_EBF")

    label("loc_E9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_EB0")
    ClearScenarioFlags(0x22, 4)
    Jump("loc_EBF")

    label("loc_EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_EBF")
    ClearScenarioFlags(0x22, 6)
    Event(0, 41)

    label("loc_EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ED8")
    Event(0, 32)

    label("loc_ED8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F0E")
    SetMapFlags(0x10000000)
    Event(0, 37)

    label("loc_F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F39")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_F39")

    Return()

    # Function_5_A90 end

    def Function_6_F3A(): pass

    label("Function_6_F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F56")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x232), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FD4")

    label("loc_F56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F72")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FD4")

    label("loc_F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F85")
    Jump("loc_FD4")

    label("loc_F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FA1")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FD4")

    label("loc_FA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FBD")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FD4")

    label("loc_FBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FD4")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_FE9")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 2)

    label("loc_FE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_FF7")
    Jump("loc_1034")

    label("loc_FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1011")
    SetMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    Jump("loc_1034")

    label("loc_1011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_101F")
    Jump("loc_1034")

    label("loc_101F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1034")
    SetMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x2)

    label("loc_1034")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_104D")
    ClearMapObjFlags(0x6, 0x4)
    Jump("loc_1053")

    label("loc_104D")

    SetMapObjFlags(0x6, 0x4)

    label("loc_1053")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1108")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x7D, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_1108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_116E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_116E")
    OP_78(0x7, 0x13)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13630, 0, 3500, 270)
    OP_D5(0x13, 0x0, 0x41EB0, 0x0, 0x0)

    label("loc_116E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11C7")
    OP_78(0x9, 0x16)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12000, 0, 3500, 270)
    OP_D5(0x16, 0x0, 0x41EB0, 0x0, 0x0)

    label("loc_11C7")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_11DA")
    Jump("loc_12B6")

    label("loc_11DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_11E8")
    Jump("loc_12B6")

    label("loc_11E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_11F6")
    Jump("loc_12B6")

    label("loc_11F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1204")
    Jump("loc_12B6")

    label("loc_1204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1220")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 5)), scpexpr(EXPR_END)), "loc_121B")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_121B")

    Jump("loc_12B6")

    label("loc_1220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_123C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 5)), scpexpr(EXPR_END)), "loc_1237")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1237")

    Jump("loc_12B6")

    label("loc_123C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_124A")
    Jump("loc_12B6")

    label("loc_124A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1258")
    Jump("loc_12B6")

    label("loc_1258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1283")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1279")
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_127E")

    label("loc_1279")

    ModifyEventFlags(1, 0, 0x80)

    label("loc_127E")

    Jump("loc_12B6")

    label("loc_1283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1291")
    Jump("loc_12B6")

    label("loc_1291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_12AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 0)), scpexpr(EXPR_END)), "loc_12A8")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_12A8")

    Jump("loc_12B6")

    label("loc_12AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_12B6")

    label("loc_12B6")

    Return()

    # Function_6_F3A end

    def Function_7_12B7(): pass

    label("Function_7_12B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12E1")
    Call(0, 34)
    Return()

    label("loc_12E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1543")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "My, it's Lloyd and the others...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard the rumors...so the Special\x01",
            "Support Section has restarted, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes. We got some\x01",
            "new members, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FEven so, isn't it strange for\x01",
            "Miss Kate to be working in\x01",
            "Entertainment District?\x02\x03",
            "#00100FI feel like you're always\x01",
            "in Central Square...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, but actually, I've\x01",
            "been on stakeout here since lately\x01",
            "we've been looking for an orbal car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That aside, I'm looking\x01",
            "forward to seeing your\x01",
            "accomplishments even more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's all do our\x01",
            "best from here on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, thank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 4)
    Jump("loc_15BF")

    label("loc_1543")


    ChrTalk(
        0xFE,
        (
            "Uh uh, I heard the rumors...so the Special\x01",
            "Support Section has restarted, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's all do our\x01",
            "best from here on!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15BF")

    TalkEnd(0xFE)
    Return()

    # Function_7_12B7 end

    def Function_8_15C3(): pass

    label("Function_8_15C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1695")

    ChrTalk(
        0xFE,
        (
            "In addition to terrorists, the actions\x01",
            "of the "Red Constellation" and the\x01",
            ""Heiyue" are both odd as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For whom and for what reason do they act?\x01",
            "...We can't take our eyes off them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17FF")

    label("loc_1695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_173D")

    ChrTalk(
        0xFE,
        (
            "Though the unveiling ceremony ended without\x01",
            "incident, our security duties have only just begun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We have to concentrate\x01",
            "for the next three days.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17FF")

    label("loc_173D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_17FF")

    ChrTalk(
        0xFE,
        (
            "We're getting ready for the\x01",
            "Arc-en-ciel performances before\x01",
            "and after the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank goodness it seems there're fewer\x01",
            "people coming and going through this plaza.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17FF")

    TalkEnd(0xFE)
    Return()

    # Function_8_15C3 end

    def Function_9_1803(): pass

    label("Function_9_1803")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_183A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_183A")
    Call(0, 39)
    Return()

    label("loc_183A")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1847")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_286B")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1897")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1897")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18B7")
    OP_AF(0x7E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2866")

    label("loc_18B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18CB")
    Jump("loc_2866")

    label("loc_18CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2866")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_1946")

    ChrTalk(
        0xC,
        "Ehehe, I am glad you like it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I look forward to your\x01",
            "continued patronage!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2866")

    label("loc_1946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_19CA")

    ChrTalk(
        0xC,
        "Really, what an amazing clamor...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Somehow I feel that the ice creams\x01",
            "will melt due to all the enthusiasm...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2866")

    label("loc_19CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1AF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A8E")

    ChrTalk(
        0xC,
        "Miss Ilya...I'm really worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My only merit is to\x01",
            "sell ice creams, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I intend to continue my business here\x01",
            "while waiting for Miss Ilya's comeback.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AF2")

    label("loc_1A8E")


    ChrTalk(
        0xC,
        "Ice creams, do you want an ice cream?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's pleasantly cool, refreshing\x01",
            "and very gooood...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AF2")

    Jump("loc_2866")

    label("loc_1AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1C37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA3")

    ChrTalk(
        0xC,
        (
            "Welcome! Would you\x01",
            "like some ice cream!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Today is the long-awaited opening\x01",
            "of the renewal performance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I hope everyone enjoys it!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C32")

    label("loc_1BA3")


    ChrTalk(
        0xC,
        (
            "Mainz should be fine...\x01",
            "Our CGF will do something\x01",
            "about it for sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Anyway, I'll cheer on\x01",
            "Arc-en-ciel and sell\x01",
            "ice cream as usual!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C32")

    Jump("loc_2866")

    label("loc_1C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C45")
    Jump("loc_2866")

    label("loc_1C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1D78")

    ChrTalk(
        0xC,
        "Ice creams, do you want an ice cream?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Have you all had lunch? Ice cream\x01",
            "is great after lunch, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D73")

    ChrTalk(
        0x101,
        (
            "#00008F(I think we can get coverage for\x01",
            "the gourmet guide here, but...)\x02\x03",
            "#00003F(Now's not the time. Let's\x01",
            "not forget to stop by later.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D73")

    Jump("loc_2866")

    label("loc_1D78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1E1A")

    ChrTalk(
        0xC,
        (
            "The Arc-en-ciel performance is finally\x01",
            "opening the day after tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'll have more customers again, right?\x01",
            "Uhuhu, I'll be filthy rich.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2866")

    label("loc_1E1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1F77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EED")

    ChrTalk(
        0xC,
        "Ice creams, do you want an ice cream?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you need help deciding, I'd be happy\x01",
            "to offer you a sample of any flavor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'll give you a taste with\x01",
            "these special mini-spoons.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F72")

    label("loc_1EED")


    ChrTalk(
        0xC,
        (
            "My ice cream sampling service\x01",
            "is popular, and sales are up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Of course, this cart was No.1\x01",
            "in sales this month too. Viva!☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F72")

    Jump("loc_2866")

    label("loc_1F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2078")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2004")

    ChrTalk(
        0xC,
        (
            "Arc-en-ciel will be\x01",
            "on vacation soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm, my sales will plummet. \x01",
            "I'll need to deal with that somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2073")

    label("loc_2004")


    ChrTalk(
        0xC,
        (
            "Hmm. At this rate, \x01",
            "I'll lose my spot as\x01",
            "the No.1 selling cart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I'll need to deal with this somehow.\x02",
    )

    CloseMessageWindow()

    label("loc_2073")

    Jump("loc_2866")

    label("loc_2078")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_258A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_214C")

    ChrTalk(
        0xFE,
        (
            "If you're looking for that redheaded customer of mine\x01",
            "from just now, he went towards Residential Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though he was wearing a nice suit, \x01",
            "he looked out of place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2585")

    label("loc_214C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23B3")

    ChrTalk(
        0xFE,
        (
            "Just now, a cheerful redheaded\x01",
            "man asked me to make a\x01",
            ""10-scoop Cone" for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That was the first order I ever\x01",
            "got for a cone that tall. And he\x01",
            "finished it off in one go, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though he was wearing a nice suit, \x01",
            "he looked out of place.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10106F(M-Mr. Lloyd. \x01",
            "Most likely, it's him...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FU-Umm... \x01",
            "Which way did he go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He was holding his head due to brain\x01",
            "freeze and went to Residential Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Alright... \x01",
            "Let's follow him.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1C7, 2)
    Jump("loc_2585")

    label("loc_23B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2503")

    ChrTalk(
        0xC,
        "There sure was a lot of noise this morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Not just due to the VIPs\x01",
            "passing through, but all\x01",
            "the pedestrians as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I had great sales due to the\x01",
            "people passing through after\x01",
            "the inauguration ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Uhuhu, with this, I'll have secured the award\x01",
            "for top-selling food cart three months running!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2585")

    label("loc_2503")


    ChrTalk(
        0xC,
        (
            "Thanks to that, it looks like\x01",
            "I'll sell out early today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That means you've got\x01",
            "to buy now or you\x01",
            "might regret it later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2585")

    Jump("loc_2866")

    label("loc_258A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2713")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2695")

    ChrTalk(
        0xC,
        (
            "Regular ice cream or\x01",
            "sherbert. Which do\x01",
            "all of you prefer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By the way, Miss Ilya likes sherbert\x01",
            "and Miss Pliｳ likes ice cream. \x01",
            "Both come here often, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh, and Miss Rixia \x01",
            "often gets sherbert,\x01",
            "same as Miss Ilya does.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_270E")

    label("loc_2695")


    ChrTalk(
        0xC,
        (
            "And Mr. Eugene \x01",
            "likes ice cream, while\x01",
            "Mr. Theodore...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...It seems he dislikes sweets\x01",
            "and doesn't buy from me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_270E")

    Jump("loc_2866")

    label("loc_2713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2721")
    Jump("loc_2866")

    label("loc_2721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2866")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27CD")

    ChrTalk(
        0xC,
        "Ice creams, do you want an ice cream?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We have a variety\x01",
            "of flavors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The next time you\x01",
            "come, please look for\x01",
            "your favorite flavor.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2866")

    label("loc_27CD")


    ChrTalk(
        0xC,
        (
            "If you'd like to\x01",
            "blend flavors,\x01",
            "please, just ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Though, if you disregard my advice and it tastes\x01",
            "bad, I won't be responsible for the result.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2866")

    Jump("loc_1847")

    label("loc_286B")

    TalkEnd(0xFE)
    Return()

    # Function_9_1803 end

    def Function_10_286F(): pass

    label("Function_10_286F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_28F3")

    ChrTalk(
        0xFE,
        (
            "Dear me...somehow the\x01",
            "situation is going crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In any case, I just wish for\x01",
            "troubles to leave me alone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D9")

    label("loc_28F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_297F")

    ChrTalk(
        0xFE,
        (
            "Heh heh heh, don't you want\x01",
            "to come drink at our store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'll be able to learn a lot\x01",
            "due to our "charity service".\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D9")

    label("loc_297F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2A07")

    ChrTalk(
        0xFE,
        (
            "Hmm, dangerous things have\x01",
            "been occurring lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Normally, quarrels\x01",
            "like that are part of\x01",
            "Back Street's charm.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D9")

    label("loc_2A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2A15")
    Jump("loc_31D9")

    label("loc_2A15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2B14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AA9")

    ChrTalk(
        0xFE,
        (
            "*sigh*, aren't\x01",
            "there any rich\x01",
            "suckers around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whoops, hehehe, I accidently let\x01",
            "out what I was really thinking.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B0F")

    label("loc_2AA9")


    ChrTalk(
        0xFE,
        (
            "Hehehe, I accidently let out\x01",
            "what I was really thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's proof that I was too relaxed.\x02",
    )

    CloseMessageWindow()

    label("loc_2B0F")

    Jump("loc_31D9")

    label("loc_2B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B84")

    ChrTalk(
        0xFE,
        (
            "Now then, I've got to do\x01",
            "my best at work today too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We will show you a world of dreams.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31D9")

    label("loc_2B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2CFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C8C")

    ChrTalk(
        0xFE,
        (
            "Man, Arc-en-ciel is blessed\x01",
            "with a newcomer after the other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say Sully will be appearing\x01",
            "in the role of a new princess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It hasn't even been a year since\x01",
            "they took on dear Rixia. I wish\x01",
            "they'd share the love a little.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2CF5")

    label("loc_2C8C")


    ChrTalk(
        0xFE,
        (
            "Even so, all the\x01",
            "Arc-en-ciel artists\x01",
            "are lovely cuties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wish they'd share the love a little.\x02",
    )

    CloseMessageWindow()

    label("loc_2CF5")

    Jump("loc_31D9")

    label("loc_2CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2DB0")

    ChrTalk(
        0xFE,
        (
            "For people like us, there's\x01",
            "nothing interesting about\x01",
            "the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lately we've gotten fewer\x01",
            "congressmen who come to\x01",
            "merrymake, so business is down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D9")

    label("loc_2DB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2E51")

    ChrTalk(
        0xFE,
        (
            "There's a lot of foot traffic today, but\x01",
            "they're all citizens and no tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How should I say this...\x01",
            "I miss the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D9")

    label("loc_2E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2EC9")

    ChrTalk(
        0xFE,
        (
            "Ah, those policemen are\x01",
            "keeping their eyes on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of it, it seems\x01",
            "I can't be too pushy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D9")

    label("loc_2EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2ED7")
    Jump("loc_31D9")

    label("loc_2ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_31D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3161")

    ChrTalk(
        0xFE,
        (
            "Hehehe, if you've got\x01",
            "some free time, come\x01",
            "have a drink inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If all four of you are coming, we\x01",
            "have a special group discount.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FWow, how much is it?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FB9")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_2FB9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FDC")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_2FDC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FFF")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_2FFF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_301F")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_301F")

    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Let's see, it's normally\x01",
            "500 mira per person...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)

    ChrTalk(
        0x109,
        "#10101FW-Wazy...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FUmm, we're working you\x01",
            "see, so we can't really...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm? Man, don't\x01",
            "tease me like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then shoo, shoo! You're\x01",
            "getting in the way of sales.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FS-Sorry...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 2)
    Jump("loc_31D9")

    label("loc_3161")


    ChrTalk(
        0xFE,
        (
            "If you're just going to tease\x01",
            "me, then please, just don't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll get angry if you're\x01",
            "too persistent, you hear?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31D9")

    TalkEnd(0xFE)
    Return()

    # Function_10_286F end

    def Function_11_31DD(): pass

    label("Function_11_31DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_327D")

    ChrTalk(
        0xFE,
        (
            "Who hurt Lady Ilya must've\x01",
            "been the Empire, for sure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why...I won't forgive the Empire...!\x01",
            "As if I'll ever change my mind!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C1C")

    label("loc_327D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3322")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32D7")

    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Lady Ilya...\x01",
            "Why did such a thing...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_331D")

    label("loc_32D7")


    ChrTalk(
        0xFE,
        (
            "I won't forgive...the culprits...\x01",
            "...I'll never forgive them...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_331D")

    Jump("loc_3C1C")

    label("loc_3322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_33C3")

    ChrTalk(
        0xFE,
        (
            "Finally... Finally the renewal \x01",
            "performance is tonight...!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "L-a-d-y I-ly-aaa! We pray \x01",
            "for the success of your\x01",
            "performance from heeere!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C1C")

    label("loc_33C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_352C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34A3")

    ChrTalk(
        0xFE,
        (
            "Tomorrow... At last...\x01",
            "Tomorrow... Finally, it's tomorrow!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lady Ilya, it's too bad I won't be able to\x01",
            "see your opening night, but... There's no\x01",
            "way Polise will be able to sleep tonight!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3527")

    label("loc_34A3")


    ChrTalk(
        0xFE,
        (
            "Lady Ilya, it's too bad I won't be able to\x01",
            "see your opening night, but... There's no\x01",
            "way Polise will be able to sleep tonight!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3527")

    Jump("loc_3C1C")

    label("loc_352C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_357F")

    ChrTalk(
        0xFE,
        "Lady Ilya, Lady Ilyaaa!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please do your best at practice!!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C1C")

    label("loc_357F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_36E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_365E")

    ChrTalk(
        0xFE,
        (
            "The day after tomorrow...\x01",
            "At last, it's the day after tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what the connection between\x01",
            "Lady Ilya and little Sully is!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*drool*... Guhuhu...\x01",
            "I can't help but imagine!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_36DD")

    label("loc_365E")


    ChrTalk(
        0xFE,
        (
            "I wonder what the connection between\x01",
            "Lady Ilya and little Sully is!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*drool*... Guhuhu...\x01",
            "I can't help but imagine!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36DD")

    Jump("loc_3C1C")

    label("loc_36E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3766")

    ChrTalk(
        0xFE,
        (
            "In three days...\x01",
            "Finally, in three days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The opening night of the renewal\x01",
            "performance... Oh, I can't wait!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C1C")

    label("loc_3766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_38ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_385C")

    ChrTalk(
        0xFE,
        (
            "Even on days without a performance, \x01",
            "Lady Ilya should be coming to the theater!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In other words, this is my chance\x01",
            "to take even more photos of her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I still come here\x01",
            "even during their time off!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38E8")

    label("loc_385C")


    ChrTalk(
        0xFE,
        (
            "Lady Ilya should be coming to the\x01",
            "theater for practice from here on out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I still come here\x01",
            "even during their time off!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38E8")

    Jump("loc_3C1C")

    label("loc_38ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_397E")

    ChrTalk(
        0xFE,
        (
            "This evening, it seems the heads of\x01",
            "state will see Arc-en-ciel perform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ooh... How unfair! \x01",
            "I wanted an invitation too!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C1C")

    label("loc_397E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3B40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A76")

    ChrTalk(
        0xFE,
        "#4SMrgrrr...!!!#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, way too many people\x01",
            "wanted tickets for the opening night\x01",
            "and I couldn't get one!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What I ended up getting is a\x01",
            "B seat one week after the opening\x01",
            "night. I'm happy...yet sad!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B3B")

    label("loc_3A76")


    ChrTalk(
        0xFE,
        (
            "As expected, way too many people\x01",
            "wanted tickets for the opening night\x01",
            "and I couldn't get one!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What I ended up getting is a\x01",
            "B seat one week after the opening\x01",
            "night. I'm happy...yet sad!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B3B")

    Jump("loc_3C1C")

    label("loc_3B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3B94")

    ChrTalk(
        0xFE,
        "L-a-d-y I-ly-aaa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Polise won't lose to something like rain!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C1C")

    label("loc_3B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3C1C")

    ChrTalk(
        0xFE,
        (
            "Lady Ilya has been spotted\x01",
            "quite often lately with\x01",
            "that new girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ooh, what's with her...?\x01",
            "What is she to Lady Ilya?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C1C")

    TalkEnd(0xFE)
    Return()

    # Function_11_31DD end

    def Function_12_3C20(): pass

    label("Function_12_3C20")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3C70")

    ChrTalk(
        0xFE,
        (
            "Uwooooh...\x01",
            "Well said, President!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Now we'll be free!!\x02",
    )

    CloseMessageWindow()
    Jump("loc_447F")

    label("loc_3C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3CDA")

    ChrTalk(
        0xFE,
        (
            "Lady Ilya...\x01",
            "They say she's still in a coma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Shit, what a really\x01",
            "absurd thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_447F")

    label("loc_3CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3D6A")

    ChrTalk(
        0xFE,
        (
            "Alright, I think I'll\x01",
            "cheer for them all day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#4SEveryone at Arc-en-cieeel!\x01",
            "Us fans are always\x01",
            "watching over youuu!!#3S\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_447F")

    label("loc_3D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3DEA")

    ChrTalk(
        0xFE,
        (
            "Hehe, I bet they're\x01",
            "rehearsing inside around now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#4SArc-en-ciel, viva!! Renewal\x01",
            "performance, viva!!#3S\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_447F")

    label("loc_3DEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3E7E")

    ChrTalk(
        0xFE,
        (
            "Lady Ilya, Miss Rixia,\x01",
            "little Sully, and also Miss\x01",
            "Pliｳ and Miss Celine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#4SI really love each and every one of youuu!#3S\x02",
    )

    CloseMessageWindow()
    Jump("loc_447F")

    label("loc_3E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3ECE")

    ChrTalk(
        0xFE,
        (
            "Hey Polise, you're drooling...\x01",
            "And that expression is scary.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_447F")

    label("loc_3ECE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F83")

    ChrTalk(
        0xFE,
        (
            "Lady Ilya, Miss Rixia and\x01",
            "little Sully are cast as the\x01",
            "three princesses, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I managed to get a ticket\x01",
            "this time... And I'm really\x01",
            "looking forward to it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_447F")

    label("loc_3F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4068")

    ChrTalk(
        0xFE,
        (
            "To prepare for the renewal\x01",
            "performance, Arc-en-ciel will be\x01",
            "taking a break soon, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "During that time, they'll be practicing\x01",
            "their dancing inside the theater...\x01",
            "I want to see it so bad, I could die!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_447F")

    label("loc_4068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_40D7")

    ChrTalk(
        0xFE,
        (
            "That's right... Even if they're\x01",
            "heads of state, this is better\x01",
            "treatment than they deserve!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_447F")

    label("loc_40D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4192")

    ChrTalk(
        0xFE,
        (
            "That Polise, she's saying\x01",
            "all that but it's me who\x01",
            "lent her mira for the ticket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, I guess it's fine.\x01",
            "As fellow die-hard fans, we\x01",
            "have to help each other out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_447F")

    label("loc_4192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4238")

    ChrTalk(
        0xFE,
        (
            "Hehe, it's days like this that\x01",
            "gives us a chance to separate\x01",
            "from other die-hard fan groups!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#4SLady Ilyaaa, Miss Rixiaaa!\x01",
            "We love youuu!!#3S\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_447F")

    label("loc_4238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_447F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4326")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "Oh, you guys are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys are the policemen\x01",
            "who were going in and out\x01",
            "of the theater awhile back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Must be nice to be an officer.\x01",
            "You can enter the theater for work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_447F")

    label("loc_4326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43F3")

    ChrTalk(
        0xFE,
        (
            "Maybe I'll enter Police Academy\x01",
            "and become an officer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that, I'll use patrolling as an\x01",
            "excuse to visit Arc-en-ciel daily...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(Well, I think that's impossible.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_447F")

    label("loc_43F3")


    ChrTalk(
        0xFE,
        (
            "Maybe I'll enter Police Academy\x01",
            "and become an officer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that, I'll use patrolling as an\x01",
            "excuse to visit Arc-en-ciel daily...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_447F")

    TalkEnd(0xFE)
    Return()

    # Function_12_3C20 end

    def Function_13_4483(): pass

    label("Function_13_4483")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_457D")

    ChrTalk(
        0xFE,
        (
            "There were some kind of rumors, but\x01",
            "to think the two major powers would\x01",
            "do such cowardly things...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I completely agree with the President's claim.\x01",
            "If we don't stand up against them now,\x01",
            "the same tragedies will be repeated!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50DC")

    label("loc_457D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4647")

    ChrTalk(
        0xFE,
        (
            "The Arc-en-ciel play...\x01",
            "The truth is that I was supposed\x01",
            "to see it today, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With what has happened,\x01",
            "there's nothing I can do about it...\x01",
            "I wonder if Lady Ilya is all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50DC")

    label("loc_4647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_46BF")

    ChrTalk(
        0xFE,
        (
            "That Mainz incident...\x01",
            "It must be truly frightening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want those CGF to do\x01",
            "something about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50DC")

    label("loc_46BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_46CD")
    Jump("loc_50DC")

    label("loc_46CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_473E")

    ChrTalk(
        0xFE,
        (
            "Central Square\x01",
            "seems noisy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't really get it, but maybe\x01",
            "it's some kind of accident?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50DC")

    label("loc_473E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4893")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4825")

    ChrTalk(
        0xFE,
        (
            "The renewal performance's opening\x01",
            "night is the day after tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though I of course couldn't' get\x01",
            "tickets for opening night, I plan\x01",
            "to go see it a week after that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhuhu, I'm so excited.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_488E")

    label("loc_4825")


    ChrTalk(
        0xFE,
        (
            "I plan to see the renewal performance\x01",
            "one week after the opening night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhuhu, I'm so excited.\x02",
    )

    CloseMessageWindow()

    label("loc_488E")

    Jump("loc_50DC")

    label("loc_4893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_49F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49B6")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        (
            "My, it's you, Wazy.\x01",
            "Thanks for the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, thanks to you, \x01",
            "I had a dream-like hour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, same here. \x01",
            "I'm glad to hear you say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(That Wazy... Just\x01",
            "when is he doing\x01",
            "his shrewd host job?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_49F4")

    label("loc_49B6")

    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        (
            "Uh uh, Wazy. Let's see each\x01",
            "other again sometime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49F4")

    Jump("loc_50DC")

    label("loc_49F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4B90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AF6")

    ChrTalk(
        0xFE,
        (
            "I was just thinking that\x01",
            "former Chairman Hartmann\x01",
            "is in a cell right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He was such a big-shot and he's\x01",
            "already disappeared from the topics\x01",
            "of everyday conversations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "People can be pretty heartless sometimes.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4B8B")

    label("loc_4AF6")


    ChrTalk(
        0xFE,
        (
            "Former Chairman Hartmann has \x01",
            "completely disappeared from the \x01",
            "topics of everyday conversations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "People can be pretty heartless sometimes.\x02",
    )

    CloseMessageWindow()

    label("loc_4B8B")

    Jump("loc_50DC")

    label("loc_4B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4C0C")

    ChrTalk(
        0xFE,
        (
            "Orchis Tower... So its\x01",
            "form was finally revealed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh. Who knew buildings\x01",
            "could be this exciting?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50DC")

    label("loc_4C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4CF7")

    ChrTalk(
        0xFE,
        (
            "The high-class club "Neue-Blanc"... \x01",
            "According to rumor, they recently opened after\x01",
            "remodeling...I'd like to go there myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But they have a membership\x01",
            "system... I wonder if I can\x01",
            "get someone to take me there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50DC")

    label("loc_4CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4D05")
    Jump("loc_50DC")

    label("loc_4D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_50DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_502C")
    TurnDirection(0xFE, 0x105, 0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "My, you are... Aren't\x01",
            "you Wazy, the host?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FOh, do you know me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard for a long time\x01",
            "there was a handsome host\x01",
            "in this neighborhood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhuhu, you're as sexy as the rumors say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, thanks.\x02\x03",
            "#10302FYou can come to where I work, if you want.\x01",
            "There, we can take our time to a nice chat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhuhu. Next time, I'd love to.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EC2")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4EC2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EE8")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4EE8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F0E")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4F0E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F34")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4F34")

    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00106F(T-That's Wazy for you. He sure\x01",
            "is known by a lot of people.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Maybe you should focus on the fact that he's\x01",
            "conducting business brazenly right in front of us.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F(Honestly... \x01",
            "I'll reprimand him later.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 1)
    Jump("loc_50DC")

    label("loc_502C")


    ChrTalk(
        0xFE,
        (
            "I heard for a long time there was a \x01",
            "handsome host in this neighborhood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu. Next time,\x01",
            "I'll come to your store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHu hu, I'll be looking forward to it.\x02",
    )

    CloseMessageWindow()

    label("loc_50DC")

    TalkEnd(0xFE)
    Return()

    # Function_13_4483 end

    def Function_14_50E0(): pass

    label("Function_14_50E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_518D")

    ChrTalk(
        0xFE,
        (
            "The "Independent State of Crossbell", eh...?\x01",
            "Hehe, it doesn't sound bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It means that from now on we'll be\x01",
            "the citizens of an independent state.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B75")

    label("loc_518D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_52F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B7")

    ChrTalk(
        0xFE,
        (
            "Lately things have finally calmed down,\x01",
            "but since there was that raid, somehow\x01",
            "it's like the entire city is in a gloom mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, that's why I think that...\x01",
            "Because the situation is like this, I must revitalize\x01",
            "the economy by partying even more than usual.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_52EB")

    label("loc_52B7")


    ChrTalk(
        0xFE,
        "And so, for that reason, I'll party today too.\x02",
    )

    CloseMessageWindow()

    label("loc_52EB")

    Jump("loc_5B75")

    label("loc_52F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_543D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53BE")

    ChrTalk(
        0xFE,
        (
            "Somehow things seem terrible in Mainz.\x01",
            "Even if we panic, there's nothing we can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And so, I plan to play here in Entertainment\x01",
            "District 'til I drop, like I always do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5438")

    label("loc_53BE")


    ChrTalk(
        0xFE,
        (
            "Oh yeah, today is opening day\x01",
            "for that renewal performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. I'm jealous of those\x01",
            "who are seeing it first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5438")

    Jump("loc_5B75")

    label("loc_543D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_54BE")

    ChrTalk(
        0xFE,
        (
            "Now then, which bar\x01",
            "shall I go to today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. Today's not a bad day for\x01",
            "getting smashed drinking alone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B75")

    label("loc_54BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_556C")

    ChrTalk(
        0xFE,
        "I was playing slots at the casino, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, it's no good. Luck\x01",
            "has abandoned me today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "On a day like today, I think I'll go home and rest.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B75")

    label("loc_556C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5601")

    ChrTalk(
        0xFE,
        (
            "I wonder if there's any\x01",
            "strategy to the casino's slots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like there's machines that\x01",
            "pay out and machines that don't...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B75")

    label("loc_5601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5712")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5694")

    ChrTalk(
        0xFE,
        "Now then, time to go all-out playing today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As for today's money... This is\x01",
            "bad. I'll have to replenish soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_570D")

    label("loc_5694")


    ChrTalk(
        0xFE,
        "I've had a string of losses recently.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can't help it then, I guess I'll ask \x01",
            "my parents for pocket money again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_570D")

    Jump("loc_5B75")

    label("loc_5712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_57DB")

    ChrTalk(
        0xFE,
        (
            "After their next performance,\x01",
            "Arc-en-ciel is going to be on\x01",
            "break for awhile, they said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They said they'll start preparing\x01",
            "for the renewal performance in\x01",
            "earnest. I can't wait.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B75")

    label("loc_57DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_58F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58A0")

    ChrTalk(
        0xFE,
        (
            "As expected, I couldn't see it from up close, \x01",
            "but I did see the inauguration ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Orchis Tower sure is amazing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. This city is\x01",
            "really something.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_58ED")

    label("loc_58A0")


    ChrTalk(
        0xFE,
        "Orchis Tower sure is amazing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. This city is\x01",
            "really something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58ED")

    Jump("loc_5B75")

    label("loc_58F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5A55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59E6")

    ChrTalk(
        0xFE,
        (
            "Ah, there are officers\x01",
            "patrolling everywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it's because the Trade\x01",
            "Conference starts tomorrow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand where they're coming from, \x01",
            "but I wish the officers around \x01",
            "here'd give me a break.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5A50")

    label("loc_59E6")


    ChrTalk(
        0xFE,
        (
            "I haven't done anything\x01",
            "wrong, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's somehow hard to play when\x01",
            "there're officers around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A50")

    Jump("loc_5B75")

    label("loc_5A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5AF7")

    ChrTalk(
        0xFE,
        (
            "Hehe. Those who hole up at home\x01",
            "because it's raining can't call\x01",
            "themselves true gamblers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now then, I'm going to\x01",
            "play my heart out today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B75")

    label("loc_5AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5B75")

    ChrTalk(
        0xFE,
        "Alright! Today, I'll play 'til I drop!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "First up is to choose\x01",
            "which slot machine I'll\x01",
            "try my luck on today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B75")

    TalkEnd(0xFE)
    Return()

    # Function_14_50E0 end

    def Function_15_5B79(): pass

    label("Function_15_5B79")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5C75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C14")

    ChrTalk(
        0xFE,
        "Hello, how're you doooing☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Casino House "Barca" is\x01",
            "in high spirits today too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyone, come and have fuuun.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5C70")

    label("loc_5C14")


    ChrTalk(
        0xFE,
        (
            "Casino House "Barca" is\x01",
            "in high spirits today too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyone, come and have fuuun.\x02",
    )

    CloseMessageWindow()

    label("loc_5C70")

    Jump("loc_6789")

    label("loc_5C75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5CE2")

    ChrTalk(
        0xFE,
        "Hello, how're you doooing☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Won't you come to bring some cheerfulness to the casino?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6789")

    label("loc_5CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5DF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D85")

    ChrTalk(
        0xFE,
        "Hello, how're you doooing☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, finally, the\x01",
            "renewal performance\x01",
            "day has come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyone, you must look aliiive, seee?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5DEC")

    label("loc_5D85")


    ChrTalk(
        0xFE,
        (
            "Uhuhu, finally, the\x01",
            "renewal performance\x01",
            "day has come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyone, you must look aliiive, seee?\x02",
    )

    CloseMessageWindow()

    label("loc_5DEC")

    Jump("loc_6789")

    label("loc_5DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5E66")

    ChrTalk(
        0xFE,
        "Hello, how're you doooing☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why don't you come inside to\x01",
            "shelter from the rain, if you want?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6789")

    label("loc_5E66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5EE5")

    ChrTalk(
        0xFE,
        "Hello, how're you doooing☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, if you want to leave a tip,\x01",
            "you're always very welcome to do that㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6789")

    label("loc_5EE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5F4D")

    ChrTalk(
        0xFE,
        "Hello, how're you doooing☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, today too we'll\x01",
            "give you plenty of service㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6789")

    label("loc_5F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_609C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6010")

    ChrTalk(
        0xFE,
        "Hello, how're you doooing☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not that I always wear\x01",
            "these clothes, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, if my boyfriend asked it,\x01",
            "I could wear them in private, though㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6097")

    label("loc_6010")


    ChrTalk(
        0xFE,
        (
            "It's not that I always wear\x01",
            "these clothes, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, if my boyfriend asked it,\x01",
            "I could wear them in private, though㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6097")

    Jump("loc_6789")

    label("loc_609C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_619F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6139")

    ChrTalk(
        0xFE,
        "Hello, how're you doooing☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, today too the\x01",
            "rays of sun are strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, tan marks\x01",
            "will come out㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_619A")

    label("loc_6139")


    ChrTalk(
        0xFE,
        (
            "Even so, today too the\x01",
            "rays of sun are strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, tan marks\x01",
            "will come out㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_619A")

    Jump("loc_6789")

    label("loc_619F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_62EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6262")

    ChrTalk(
        0xFE,
        "Hello, how're you doooing☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say that today VIPs\x01",
            "are going to see the\x01",
            "Arc-en-ciel play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, I wonder if, with the\x01",
            "occasion, won't they stop here?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_62E9")

    label("loc_6262")


    ChrTalk(
        0xFE,
        (
            "They say that today VIPs\x01",
            "are going to see the\x01",
            "Arc-en-ciel play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, I wonder if, with the\x01",
            "occasion, won't they stop here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62E9")

    Jump("loc_6789")

    label("loc_62EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_657B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_651C")

    ChrTalk(
        0xFE,
        (
            "Oh, if it isn't Mr. Randy.\x01",
            "You didn't show up in a long time,\x01",
            "what have you been doing, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FYeah, sorry.\x01",
            "Had some minor business to do.\x02\x03",
            "#00300FI'll treat you next time, won't you forgive me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, forgiving you or not,\x01",
            "I can't accept your proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you think you're sorry about it,\x01",
            "then go lose some mira at our place☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FHa ha, good at business as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F(Rather, senior Randy...\x01",
            "He seems used to this.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Yeah, well, this place is\x01",
            "akin to a home to Randy.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 4)
    Jump("loc_6576")

    label("loc_651C")


    ChrTalk(
        0xFE,
        (
            "Mr. Randy,\x01",
            "If you think you're sorry about it,\x01",
            "then go lose some mira at our place☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6576")

    Jump("loc_6789")

    label("loc_657B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6609")

    ChrTalk(
        0xFE,
        "Hello, how're you doooing☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On such a day, I recommend\x01",
            "to come to our store to spend\x01",
            "the time having a ton of fuuun㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6789")

    label("loc_6609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6789")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6738")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66E0")

    ChrTalk(
        0xFE,
        "Hello, how're you doooing☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eh, has a redheaded man\x01",
            "come here, you ask?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you a friend of him?\x01",
            "If you're looking for him,\x01",
            "he has just come to the store㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6733")

    label("loc_66E0")


    ChrTalk(
        0xFE,
        "Hello, how're you doooing☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A redheaded man?\x01",
            "He just came to the store㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6733")

    Jump("loc_6789")

    label("loc_6738")


    ChrTalk(
        0xFE,
        "Hello, how're you doooing☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, go have a \x01",
            "looot of fun today too㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6789")

    TalkEnd(0xFE)
    Return()

    # Function_15_5B79 end

    def Function_16_678D(): pass

    label("Function_16_678D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "So this is the famed\x01",
            ""Arc-en-ciel"...\x01",
            "Uh uh, I've finally arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I already got my tickets\x01",
            "before, so I just need to\x01",
            "wait for the performance.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_678D end

    def Function_17_682E(): pass

    label("Function_17_682E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Their greatest masterpiece is called\x01",
            ""Golden Sun, Silver Moon", huh.\x01",
            "I can't help but look forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, it looks like the doors don't open\x01",
            "until just before the show. Now where\x01",
            "should I kill some time, I wonder.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_682E end

    def Function_18_691A(): pass

    label("Function_18_691A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SoundLoad(468)
    ClearChrFlags(0x13, 0x80)
    OP_78(0x5, 0x13)
    OP_49()
    SetChrPos(0x13, 13050, 0, -18750, 225)
    OP_D5(0x13, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x79, 0xB4, 0x1, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFE, 0xCB, 0xC0, 0x2C, 0x9D, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A8F")
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x8000)
    EndChrThread(0xB, 0xFF)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xB, 9390, 0, -4600, 180)
    EndChrThread(0xD, 0xFF)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrPos(0xD, 11820, 0, -12540, 270)

    def lambda_6A45():
        OP_96(0xFE, 0xFFFFE0D4, 0x0, 0xE88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6A45)
    EndChrThread(0xA, 0xFF)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0xA, 14040, 0, 11290, 90)

    def lambda_6A7A():
        OP_95(0xFE, 37920, 0, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6A7A)

    label("loc_6A8F")

    FadeToBright(1000, 0)
    Sound(468, 2, 100, 0)
    Sound(457, 0, 100, 0)
    BeginChrThread(0x13, 3, 0, 19)
    OP_68(-8900, 2000, 2110, 0)
    MoveCamera(60, 6, 0, 0)
    OP_6E(720, 0)
    SetCameraDistance(30000, 0)
    OP_68(-8900, 4000, 2110, 7500)
    OP_6F(0x79)
    OP_0D()
    StopSound(468, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 0)
    NewScene("c0300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_691A end

    def Function_19_6B0D(): pass

    label("Function_19_6B0D")

    SetChrPos(0xFE, 13050, 0, -18750, 225)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -8000, 0, -600)
    OP_9F(0x1, -24250, 0, 8350)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_19_6B0D end

    def Function_20_6B48(): pass

    label("Function_20_6B48")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrFlags(0x153, 0x8)
    SoundLoad(468)
    ClearChrFlags(0x13, 0x80)
    OP_78(0x5, 0x13)
    OP_49()
    SetChrPos(0x13, -24950, 0, 8900, 0)
    OP_D5(0x13, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x79, 0xB4, 0x1, 0x20)
    OP_7D(0xBB, 0x9B, 0xB9, 0x0, 0x0)
    OP_11(0xBB, 0xA1, 0xBF, 0x54, 0x9D, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6CA3")
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x8000)
    EndChrThread(0xB, 0xFF)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xB, 10750, 0, -5630, 270)
    EndChrThread(0xD, 0xFF)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrPos(0xD, 2520, 0, -5710, 90)

    def lambda_6C73():
        OP_96(0xFE, 0x3F15, 0x0, 0xFFFFAF42, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6C73)
    EndChrThread(0xA, 0xFF)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0xA, -3100, 1760, 9570, 180)

    label("loc_6CA3")

    FadeToBright(1000, 0)
    Sound(468, 2, 100, 0)
    Sound(458, 0, 100, 0)
    BeginChrThread(0x13, 3, 0, 21)
    OP_68(-8900, 8000, 2110, 0)
    MoveCamera(60, 6, 0, 0)
    OP_6E(720, 0)
    SetCameraDistance(30000, 0)
    OP_68(-8900, 4000, 2110, 10000)
    Sleep(7000)
    StopSound(468, 2000, 100)
    Sleep(2000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 0)
    NewScene("c120B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_6B48 end

    def Function_21_6D25(): pass

    label("Function_21_6D25")

    SetChrPos(0xFE, -24950, 0, 8900, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -10800, 0, 1900)
    OP_9F(0x1, 4150, 0, -2750)
    OP_9F(0x1, 10500, 0, 5450)
    OP_9F(0x1, 22600, 0, 11200)
    OP_9F(0x1, 38350, 0, 11900)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_21_6D25 end

    def Function_22_6D8A(): pass

    label("Function_22_6D8A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x102, -2570, 50, -5500, 225)
    SetChrPos(0x109, -2570, 50, -5500, 225)
    SetChrPos(0x104, -2570, 50, -5500, 225)
    SetChrPos(0x101, -1120, 50, -3330, 45)
    SetChrPos(0x105, -1120, 50, -3330, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x13, 0x80)
    OP_78(0x5, 0x13)
    OP_49()
    SetChrPos(0x13, -35000, 0, 11000, 0)
    OP_D5(0x13, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x79, 0xB4, 0x1, 0x20)
    BeginChrThread(0x13, 3, 0, 23)
    OP_68(-18410, 3350, 8480, 0)
    MoveCamera(9, 14, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(22130, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_68(-1860, 2550, -4600, 7000)
    MoveCamera(31, 21, 0, 7000)
    OP_6E(800, 7000)
    SetCameraDistance(18000, 7000)
    Sleep(2500)
    Sound(459, 0, 80, 0)
    OP_6F(0x79)
    OP_68(290, 650, -5500, 0)
    MoveCamera(71, 19, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14500, 0)
    Fade(500)
    OP_0D()
    WaitChrThread(0x13, 3)
    Sound(462, 0, 100, 0)
    OP_71(0x5, 0x1, 0x1E, 0x0, 0x0)
    MoveCamera(78, 20, 0, 3000)
    SetCameraDistance(13090, 3000)
    Sleep(1000)
    BeginChrThread(0x104, 0, 0, 24)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        "#00311F#5P............\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 0, 0, 25)
    BeginChrThread(0x101, 0, 0, 26)
    BeginChrThread(0x102, 0, 0, 28)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x101,
        "#00007F#5PRandy...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#6PLet's go after him!\x02",
    )

    CloseMessageWindow()
    MoveCamera(90, 10, 0, 5500)
    BeginChrThread(0x105, 0, 0, 30)
    BeginChrThread(0x109, 0, 0, 31)
    BeginChrThread(0x101, 0, 0, 27)
    BeginChrThread(0x102, 0, 0, 29)
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(800)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Burst Gauge has been deactivated.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※After the climax of each chapter of the story,\x01",
            "  the Burst Gauge will be temporarily unusable.\x02\x03",
            "※However, when the story again approaches\x01",
            "  a climax, it will be usable once again.\x02\x03",
            "※When that happens, the Burst Gauge will\x01",
            "  appear on the upper right of the screen once\x01",
            "  again, so be sure to take notice of it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)
    EndChrThread(0x104, 0x0)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x105, 0x0)
    EndChrThread(0x102, 0x0)
    EndChrThread(0x109, 0x0)
    EndChrThread(0x104, 0x0)
    OP_32(0xFF, 0xF9, 0x0)
    RemoveParty(0x3, 0xFF)
    SetScenarioFlags(0x12A, 4)
    OP_29(0xA2, 0x1, 0x4)
    OP_C9(0x0, 0x1000)
    EventEnd(0x5)
    NewScene("c0500", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_22_6D8A end

    def Function_23_71E8(): pass

    label("Function_23_71E8")

    SetChrPos(0xFE, -35000, 0, 11000, 0)
    Sound(458, 0, 80, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -23250, 0, 7500)
    OP_9F(0x1, -8000, 0, 0)
    OP_9F(0x1, -4500, 0, -2500)
    OP_9F(0x2, 0xFE, 5000, 0x6)
    OP_9B(0x0, 0xFE, 0x0, 0x320, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x320, 0xBB8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x320, 0x7D0, 0x1)
    Sound(492, 0, 60, 0)
    OP_71(0x5, 0x5B, 0x78, 0x1, 0x8)
    OP_9B(0x0, 0xFE, 0x0, 0x320, 0x3E8, 0x1)
    Return()

    # Function_23_71E8 end

    def Function_24_7285(): pass

    label("Function_24_7285")


    def lambda_728A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_728A)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_24_7285 end

    def Function_25_72BC(): pass

    label("Function_25_72BC")

    Sleep(300)
    OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    OP_9B(0x1, 0xFE, 0x162, 0x5DC0, 0x1388, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_25_72BC end

    def Function_26_72E9(): pass

    label("Function_26_72E9")

    Sleep(200)

    def lambda_72F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_72F1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x5DC, 0x0)
    OP_9B(0x1, 0xFE, 0x2D, 0xABE, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_26_72E9 end

    def Function_27_7323(): pass

    label("Function_27_7323")

    TurnDirection(0xFE, 0x104, 500)
    OP_9B(0x1, 0xFE, 0x0, 0x6978, 0x1770, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_27_7323 end

    def Function_28_7345(): pass

    label("Function_28_7345")

    Sleep(800)

    def lambda_734D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_734D)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x5DC, 0x0)
    OP_9B(0x1, 0xFE, 0x159, 0x190, 0x7D0, 0x1)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_28_7345 end

    def Function_29_737F(): pass

    label("Function_29_737F")

    Sleep(100)
    OP_93(0xFE, 0x7D, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    TurnDirection(0xFE, 0x104, 500)
    OP_9B(0x1, 0xFE, 0x0, 0x5DC0, 0x1388, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_29_737F end

    def Function_30_73BA(): pass

    label("Function_30_73BA")

    Sleep(100)

    def lambda_73C2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_73C2)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    OP_9B(0x1, 0xFE, 0x1E, 0x1F4, 0x7D0, 0x1)
    TurnDirection(0xFE, 0x104, 500)
    Sleep(100)
    OP_9B(0x1, 0xFE, 0x0, 0x6978, 0x1388, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_30_73BA end

    def Function_31_7411(): pass

    label("Function_31_7411")

    Sleep(500)

    def lambda_7419():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7419)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x1E, 0x1F4)
    Sound(461, 0, 100, 0)
    OP_71(0x5, 0x1F, 0x3C, 0x0, 0x0)
    Sleep(600)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x19)
    Sleep(300)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x7D, 0x1F4)
    Sleep(100)
    OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    TurnDirection(0xFE, 0x104, 500)
    OP_9B(0x1, 0xFE, 0x0, 0x5DC0, 0x1388, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_31_7411 end

    def Function_32_74B7(): pass

    label("Function_32_74B7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(803)
    SoundLoad(894)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(-27000, 1100, 12100, 0)
    MoveCamera(30, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18200, 0)
    SetChrPos(0x101, -27000, 0, 13400, 180)
    SetChrPos(0x102, -27600, 0, 11200, 0)
    SetChrPos(0x103, -28300, 0, 12100, 90)
    SetChrPos(0x109, -25700, 0, 12500, 270)
    SetChrPos(0x105, -26500, 0, 11200, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0xA, 0x80)
    OP_4B(0xA, 0x0)
    SetChrFlags(0xD, 0x80)
    OP_4B(0xD, 0x0)
    MoveCamera(40, 23, 0, 3000)
    SetCameraDistance(15200, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#12P#00101F...We've gotten a good idea of Randy's actions\x01",
            "between yesterday evening and this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00003FYeah, let's try piecing them together.\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_7675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7994")
    SetScenarioFlags(0x0, 0)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhere did Randy go first?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Exchange Shop "Neinvalli"\x01",            # 0
            "Repair Shop "Guillaume Factory"\x01",      # 1
            "Casino/Bar "Barca"\x01",                   # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7730")
    ClearScenarioFlags(0x0, 0)

    label("loc_7730")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhere did Randy go next?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Exchange Shop "Neinvalli"\x01",            # 0
            "Repair Shop "Guillaume Factory"\x01",      # 1
            "Casino/Bar "Barca"\x01",                   # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77C9")
    ClearScenarioFlags(0x0, 0)

    label("loc_77C9")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhere did Randy go last?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Exchange Shop "Neinvalli"\x01",            # 0
            "Repair Shop "Guillaume Factory"\x01",      # 1
            "Casino/Bar "Barca"\x01",                   # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_786B")
    ClearScenarioFlags(0x0, 0)

    label("loc_786B")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78FA")

    ChrTalk(
        0x101,
        (
            "#5P#00003F(No... \x01",
            "This isn't the order.)\x02\x03",
            "#00001F(I'll try sorting them out again.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78F5")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_78F5")

    Jump("loc_798F")

    label("loc_78FA")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_790A"),
        (SWITCH_DEFAULT, "loc_7957"),
    )


    label("loc_790A")

    OP_2C(0xAA, 0x1)

    ChrTalk(
        0x101,
        "#5P#00000F(There's no mistake. This is definitely the order.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_798F")

    label("loc_7957")


    ChrTalk(
        0x101,
        "#5P#00003F(...This is the most likely order.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_798F")

    label("loc_798F")

    Jump("loc_7675")

    label("loc_7994")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Between 3 and 4AM "Barca", between\x01",
            "5 and 6 "Guillaume Factory",\x01",
            "and around 6 "Neinvalli".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#00006F──He most likely first went\x01",
            "to Owner Drake to pick up\x01",
            "the trunk he left with him.\x02\x03",
            "#00008FIt's content... Randy's special\x01",
            "weapon from when he was a jaeger.\x02\x03",
            "#00001FIt's most likely a kind of\x01",
            "high-power orbal rifle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FOrbal rifles are normally\x01",
            "transported disassembled.\x02\x03",
            "#00201FBecause it hasn't been used in\x01",
            "two years, Randy brought it to\x01",
            "the repair factory to be serviced...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F#11P──Yes, no doubt about it.\x02\x03",
            "#10108FHaving a well-maintained weapon is a\x01",
            "matter of life and death on a battlefield.\x02\x03",
            "#10101FSenior Randy would definitely\x01",
            "have it checked carefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FFinally, he stopped by the\x01",
            "exchange shop to stock up.\x02\x03",
            "#10301FHe bought gunpowder ammo too.\x01",
            "It means he has quite the special rifle, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FI've heard the Reinford Corporation have\x01",
            "models that can change between orbal\x01",
            "and gunpowder operation but...\x02\x03",
            "#00101FRegardless, it probably has a\x01",
            "number of special improvements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FYeah. The Red Constellation \x01",
            "jaegers too used huge rifles\x01",
            "I had never seen before.\x02\x03",
            "#00013F──Alright, I think we've gotten a\x01",
            "handle on Randy's situation, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FIt was past 6AM when Mr. \x01",
            "Randy left the exchange shop...\x02\x03",
            "#00208FIt's around 10AM now, so\x01",
            "around 4 hours have passed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#11PIt seems difficult to\x01",
            "track senior now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003F...No. Even if it's Randy,\x01",
            "his toughness has a limit.\x02\x03",
            "#00001FAnd if he's going up against the "Red\x01",
            "Constellation", he'd rest before doing so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FOn top of that, he'll use the terrain to\x01",
            "his advantage, attacking suddenly\x01",
            "and finishing it once and for all.\x02\x03",
            "#10302FWell, if he's not planning\x01",
            "on a suicide attack,\x01",
            "that's how he'd do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101F...In any case we don't\x01",
            "have much time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00013FYeah. Without evidence, we have\x01",
            "no choice but to go towards Mainz──\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    def lambda_819F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_819F)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_81C4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_81C4)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(802, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#5P#00011FNo way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00205FIs it from Mr. Randy?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x7)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00007F──Special Support Section,\x01",
            "Lloyd Bannings speaking!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hey there, Mr. Lloyd.\x02\x03",
            "...Hu hu, it seems you thought\x01",
            "I was someone else.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FT-This voice is...\x02\x03",
            "#00013F...Why do you have this number?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hu hu, I told you before.\x01",
            "I am a huge fan of you guys.\x02\x03",
            "──The Times department store.\x02\x03",
            "If you are free, please\x01",
            "come to the roof.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 70, 0)
    Sleep(400)
    Sound(894, 2, 100, 0)
    Sleep(1200)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    OP_24(0x37E)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#6P#00201F...Mr. Lloyd.\x01",
            "That call...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108FW-Who was it?\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#00003F...Cao from the "Heiyue".\x02\x03",
            "#00013FIt seems he's waiting for us on the roof\x01",
            "of the Central Square department store.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10111F#11PHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10301FAt a time like this...\x01",
            "What could he be planning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FI don't know. \x01",
            "What I do know is, he wouldn't\x01",
            "contact us without a reason.\x02\x03",
            "#00001FLet's stop by before heading\x01",
            "to the mountain path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101FU-Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00201FAnyway, let's hurry.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xA, 0x80)
    OP_4C(0xA, 0x0)
    ClearChrFlags(0xD, 0x80)
    OP_4C(0xD, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, -27000, 0, 13400, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x166, 1)
    OP_29(0xAA, 0x1, 0x4)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    OP_24(0x323)
    OP_24(0x37E)
    EventEnd(0x5)
    Return()

    # Function_32_74B7 end

    def Function_33_879B(): pass

    label("Function_33_879B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(821)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetMapObjFlags(0x4, 0x1000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFE, 0xCB, 0xC0, 0x2C, 0x9D, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    OP_68(-28080, 1950, 8970, 0)
    MoveCamera(343, 18, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(20060, 0)
    OP_68(16750, 2150, 8910, 10000)
    MoveCamera(37, 10, 0, 10000)
    OP_6E(800, 10000)
    SetCameraDistance(35660, 10000)
    Sound(821, 2, 50, 0)
    PlayBGM("ed7576", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x240), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    VolumeBGM(0x1E, 0x64)
    Sleep(100)
    VolumeBGM(0x3C, 0xFA0)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(-2580, 10570, 29050, 0)
    MoveCamera(0, 5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(36500, 0)
    OP_68(-2580, 10570, 29050, 8000)
    MoveCamera(0, -10, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(30500, 8000)
    Sleep(7000)
    StopSound(821, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("e3600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_879B end

    def Function_34_8930(): pass

    label("Function_34_8930")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(10850, 1950, -100, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10250, 0)
    OP_78(0x7, 0x13)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13630, 0, 3500, 270)
    OP_D5(0x13, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrPos(0x101, 11400, 0, 1350, 90)
    SetChrPos(0x102, 11400, 0, 80, 90)
    SetChrPos(0x109, 10060, 0, 1820, 90)
    SetChrPos(0x105, 10120, 0, 440, 90)
    OP_4B(0x11, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DCA")

    ChrTalk(
        0x11,
        (
            "Thank you for coming,\x01",
            "Special Support Section!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOfficer Kate, thank you\x01",
            "for your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FYou want us to help\x01",
            "with that reckless\x01",
            "driving incident...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FCan you give us\x01",
            "the details?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes, I'll explain\x01",
            "it right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Recently, someone has been\x01",
            "driving a car recklessly\x01",
            "throughout the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It seems they enjoy the thrill of grazing\x01",
            "people and things, and we've gotten\x01",
            "complaints from all over the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIndeed. That did seem like\x01",
            "reckless driving just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FI've heard about this.\x02\x03",
            "Because they're using the horn\x01",
            "indiscriminately, the noise\x01",
            "is becoming a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FWe don't know who they're, but\x01",
            "they're certainly bothering people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes, this is a problem the District Crime\x01",
            "Prevention Section want to solve ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "And so, I'd like the Special\x01",
            "Support Section's help in putting\x01",
            "a stop to the reckless vehicle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "So, can I ask you to do it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E47")

    label("loc_8DCA")


    ChrTalk(
        0x11,
        (
            "I'd like the Special Support\x01",
            "Section's help in putting a\x01",
            "stop to the reckless vehicle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "So, can I ask you to do it?\x02",
    )

    CloseMessageWindow()

    label("loc_8E47")

    Call(0, 35)
    OP_4C(0x11, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 11050, 0, 540, 225)
    EventEnd(0x5)
    Return()

    # Function_34_8930 end

    def Function_35_8E66(): pass

    label("Function_35_8E66")

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
            "[Accept]\x01",      # 0
            "[Quit]\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EC7")
    Call(0, 36)
    Jump("loc_8FBF")

    label("loc_8EC7")


    ChrTalk(
        0x101,
        (
            "#00006FWe'd very much like to help, but...\x01",
            "There's another case we\x01",
            "have to deal with right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Hmm, I see. You have work\x01",
            "to do too, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Thanks for listening. \x01",
            "For now, we'll try to deal with the\x01",
            "problem ourselves somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x130, 6)

    label("loc_8FBF")

    Return()

    # Function_35_8E66 end

    def Function_36_8FC0(): pass

    label("Function_36_8FC0")


    ChrTalk(
        0x101,
        (
            "#00000FUnderstood. \x01",
            "We'll do everything\x01",
            "we can to help.\x02\x03",
            "#00009FHa ha, after all, you helped\x01",
            "me so much back at the police\x01",
            "academy, senior Kate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Thanks, this is a huge help!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Runaway Vehicle Crackdown]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x69, 0x4, 0x2)

    ChrTalk(
        0x11,
        (
            "*ahem*, then first, let me tell\x01",
            "you about the criminals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "The reckless drivers appear to be a group\x01",
            "of three young men from the Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "They were spotted in Crossbell\x01",
            "City just the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "They've been running around the state\x01",
            "from their base in Waterfront park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It looks like they've recently started using the \x01",
            "Mainz Mountain Path as a driving route too..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FEven on the highway...? \x01",
            "That might impact \x01",
            "bus service too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FAh, but...\x02\x03",
            "#00000FIf their highway route is\x01",
            "shutdown, it doesn't seem\x01",
            "that hard to stop them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FSeems that way.\x02\x03",
            "#10103FIf you used your patrols\x01",
            "cars, you could have them\x01",
            "surrounded without a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Hmm, I don't think\x01",
            "that's an option.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "If we don't pursue carefully, \x01",
            "I'm sure they'll break through our\x01",
            "formation out of desperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "If we're too reckless, a traffic\x01",
            "accident will occur, and that'll\x01",
            "attract a lot of attention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Sounds tough.\x02\x03",
            "#00001FIf that were to happen, surely the\x01",
            "police would bear responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "And so, I'd like you guys\x01",
            "to lend us your wisdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "We need a smart way to put\x01",
            "a stop to that car without\x01",
            "bothering the citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see... I understand\x01",
            "the situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00000FI think there's two\x01",
            "important points.\x02\x03",
            "#00003FFirst, the "method" to stop\x01",
            "that recklessly driven car...\x02\x03",
            "#00000FAnd, a "place" where we can use that\x01",
            "method without bothering the citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FIndeed. If either of those\x01",
            "are lacking, I don't think\x01",
            "we'll be able to catch them.\x02\x03",
            "#00100FIn that case, let's first\x01",
            "think about the "method."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHmm, I can think of\x01",
            "several ways, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FI assume the best method will be\x01",
            "the one with the least chance of\x01",
            "an accident occurring?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes, of course. I want to\x01",
            "minimize the probability\x01",
            "of involving any citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Think about a "method"\x01",
            "that can achieve that...\x01",
            "Do you have any good ideas?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FHmm...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KA method to safely stop the recklessly driven car?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Block Route with Patrol Cars\x01",      # 0
            "Deploy Traps on the Road\x01",          # 1
            "Lure Them Into a Dead End\x01",         # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99D4")
    OP_2C(0x69, 0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLuring them into a dead end...\x01",
            "How about that?\x02\x03",
            "If we do that, the\x01",
            "reckless car will have\x01",
            "no choice but to stop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CDF")

    label("loc_99D4")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_99EA"),
        (1, "loc_9B19"),
        (SWITCH_DEFAULT, "loc_9C35"),
    )


    label("loc_99EA")


    ChrTalk(
        0x101,
        (
            "#00000FBlock their route with patrol cars...\x01",
            "How about that?\x02\x03",
            "If we make the cars into a wall, they'll have\x01",
            "to stop no matter how reckless they are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FH-Hmm... \x01",
            "I think that's being a\x01",
            "little too overbearing.\x02\x03",
            "#10101FIf their brakes are\x01",
            "damaged, they'll collide\x01",
            "with the patrol cars.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C35")

    label("loc_9B19")


    ChrTalk(
        0x101,
        (
            "#00000FPutting traps on the road...\x01",
            "How about that?\x02\x03",
            "If we puncture their tires\x01",
            "with sharp objects...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FH-Hmm...\x01",
            "I've heard about things\x01",
            "like that too, but...\x02\x03",
            "#10101FIf we were to use something like\x01",
            "that in Crossbell City, there'd\x01",
            "be a serious accident for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C35")

    label("loc_9C35")


    ChrTalk(
        0x101,
        "#00006FI-I see...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000F...Then, how about luring\x01",
            "them into a dead end?\x02\x03",
            "If we do that, the\x01",
            "reckless car will have\x01",
            "no choice but to stop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CDF")


    ChrTalk(
        0x11,
        (
            "I see... That would\x01",
            "be a safe way of\x01",
            "stopping the car!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FBut, a dead end...\x01",
            "No suitable places\x01",
            "come to mind.\x02\x03",
            "#00100FWe won't be able to use the new City Hall\x01",
            "or the IBC building for obvious reasons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FHmm, that's right...\x01",
            "I thought that was a good idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, in that case...\x01",
            "Why don't we make one?\x02\x03",
            "#10300FWe can make a barricade with sandbags\x01",
            "like those used at construction sites.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x11,
        "Yeah, good idea!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "If we use those, we can stop\x01",
            "them wherever we please!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FUh uh, very skillfully thought.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, you're welcome.\x02\x03",
            "#10300FThen, the next problem is the\x01",
            ""place" where to stop them.\x02\x03",
            "Does the District Crime Prevention Section\x01",
            "have an idea as to the car's route?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Yes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "The route the car's taking\x01",
            "looks like a big lap\x01",
            "around Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Entertaintment District -> Governmental District ->\x01",
            "Waterfront Area -> East Street -> Central Square ->\x01",
            "Back Street...then back to the Entertainment District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWe should be able to lure\x01",
            "them into a dead end in\x01",
            "any of those six areas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I'm looking for a place with\x01",
            "few pedestrians and where the\x01",
            "citizens won't be bothered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Is there any place like\x01",
            "that along the car's route?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FLet's see...\x02",
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A427")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhere is the appropriate place to stop the car?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        180,
        0,
        (
            "Entertainment District\x01",      # 0
            "Governmental District\x01",       # 1
            "Waterfront Area\x01",             # 2
            "East Street\x01",                 # 3
            "Central Square\x01",              # 4
            "Back Street\x01",                 # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A38F")

    ChrTalk(
        0x101,
        (
            "#00000FI think the only place that matches those\x01",
            "conditions is the Governmental District.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A38A")
    OP_2C(0x69, 0x1)

    label("loc_A38A")

    Jump("loc_A422")

    label("loc_A38F")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00003F(...No, I think that\x01",
            "place won't work.)\x02\x03",
            "(A place with few pedestrians\x01",
            "and that won't bother the\x01",
            "citizens. That place is...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A422")

    Jump("loc_A222")

    label("loc_A427")


    ChrTalk(
        0x105,
        (
            "#10300FGovernmental District...\x01",
            "The City Meeting Hall, library\x01",
            "and police HQ are all there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIt's true there're few\x01",
            "pedestrians there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes. Even if an accident does occur, \x01",
            "I think damage will be kept to a minimum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Additionally, police HQ is nearby.\x01",
            "It's the perfect strategy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "...Hmm, I think this\x01",
            "is going to work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Uh uh, that's our Special Support Section!\x01",
            "You guys came up with that plan in a flash.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009FHa ha, we're just glad we could help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Next, to lure them in,\x01",
            "we're going to need\x01",
            "several patrol cars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Alright! I'll notify everyone\x01",
            "in my section, and we'll begin\x01",
            "the operation right away!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Special Support Section, please take\x01",
            "care of constructing the barricade!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FAlright, we'll help you out with that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FHu hu, this is getting interesting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FSince we're going to do this,\x01",
            "let's give it our all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes! We'll definitely catch\x01",
            "that reckless driven car!!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x206), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 4)
    NewScene("c1200", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_36_8FC0 end

    def Function_37_A816(): pass

    label("Function_37_A816")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch39000.itc", 0x1E)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -16970, 0, 10380, 90)
    OP_68(-16340, 1950, 10050, 0)
    MoveCamera(34, 51, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8590, 0)
    SetChrPos(0x101, -35010, 0, 11220, 90)
    SetChrPos(0x102, -36140, 0, 9520, 90)
    SetChrPos(0x1A3, -36060, 0, 12520, 90)
    SetChrPos(0x104, -37510, 0, 12020, 90)
    SetChrPos(0x109, -37260, 0, 10020, 90)
    SetChrPos(0x105, -38010, 0, 10820, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)

    def lambda_A911():
        OP_95(0xFE, -8119, 1770, 11630, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A911)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(-12110, 1950, 11440, 4000)
    MoveCamera(34, 51, 0, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(11450, 4000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-37440, 1950, 9730, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9160, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#00005F...There she is!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#00100FWe'll need to be a little\x01",
            "more careful from here on.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00003FRight. Let's circle around so she\x01",
            "doesn't escape to any other districts.\x02\x03",
            "#00000FElie and I will handle the\x01",
            "Governmental District. \x01",
            "Noｱl, Wazy, you take Back Street.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        "#6P#10100FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FJa.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A3, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FRandy, Shirley, you take\x01",
            "Residential Street.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A3, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        "#6P#00303F...Got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        "#5P#04609FAhaha, a pincer attack, eh?♪\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x3)
    OP_68(1290, 3710, 10770, 0)
    MoveCamera(43, 30, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9860, 0)
    SetChrPos(0x14, 2490, 1760, 11180, 90)
    SetChrPos(0x101, 15020, 0, 5200, 0)
    SetChrPos(0x102, 15000, 0, 2900, 0)

    def lambda_AC31():
        OP_95(0xFE, 13360, 0, 10870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_AC31)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_68(13490, 1950, 10070, 5000)
    MoveCamera(42, 30, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(9450, 5000)

    def lambda_AC86():
        OP_95(0xFE, 15810, 0, 11410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AC86)
    Sleep(50)

    def lambda_ACA3():
        OP_95(0xFE, 15710, 0, 10230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ACA3)
    WaitChrThread(0x101, 1)

    def lambda_ACC1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ACC1)
    WaitChrThread(0x102, 1)

    def lambda_ACD2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ACD2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00000FHere Mary.\x01",
            "Come 'ere!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FDon't worry. \x01",
            "We'll take you home.\x02",
        )
    )

    CloseMessageWindow()
    Sound(953, 0, 100, 0)

    def lambda_AD38():
        OP_95(0xFE, 9930, 0, 4040, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_AD38)
    Sleep(50)

    def lambda_AD55():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD55)
    Sleep(50)

    def lambda_AD65():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AD65)
    Sleep(1000)
    EndChrThread(0x14, 0x1)
    Fade(500)
    OP_68(6630, 1950, -13390, 0)
    MoveCamera(82, 19, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(7810, 0)
    SetChrPos(0x14, 7930, 0, -7640, 180)
    SetChrPos(0x109, 12080, 0, -15670, 315)
    SetChrPos(0x105, 11030, 0, -17020, 315)

    def lambda_ADDF():
        OP_95(0xFE, 7970, 0, -12520, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_ADDF)
    Sleep(50)

    def lambda_ADFC():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ADFC)
    Sleep(50)

    def lambda_AE14():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AE14)
    OP_0D()
    WaitChrThread(0x14, 1)
    OP_93(0x14, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10100FDon't be scared, Mary.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, resign yourself and\x01",
            "come quietly with us, won't you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AEA3():
        OP_95(0xFE, 440, 0, -6930, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_AEA3)
    Sleep(1000)
    EndChrThread(0x14, 0x1)
    Fade(500)
    OP_68(-34190, 1950, 7420, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(7870, 0)
    SetChrPos(0x14, -22150, 0, 7980, 270)
    SetChrPos(0x104, -35990, 0, 9690, 90)
    SetChrPos(0x1A3, -35970, 0, 11380, 90)

    def lambda_AF2A():
        OP_95(0xFE, -28830, 0, 10230, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_AF2A)
    Sleep(50)

    def lambda_AF47():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AF47)
    Sleep(50)

    def lambda_AF5F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_AF5F)
    OP_0D()
    WaitChrThread(0x14, 1)

    ChrTalk(
        0x1A3,
        "#04602FSee? I won't hurt you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(...Man. That part of her\x01",
            "hasn't changed a bit.)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AFDB():
        OP_95(0xFE, -8119, 1770, 11630, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_AFDB)
    Sleep(1000)
    EndChrThread(0x14, 0x1)
    Fade(500)
    SetChrPos(0x8, 380, 1770, 28050, 225)
    SetChrPos(0x9, 1830, 1770, 27900, 225)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(-4450, 3860, 22900, 0)
    MoveCamera(43, 24, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12000, 0)
    SetChrPos(0x14, -1970, 1990, 23280, 180)
    SetChrPos(0x101, 4560, 1760, 24610, 270)
    SetChrPos(0x102, 2580, 1990, 21200, 315)
    SetChrPos(0x109, -1130, 1990, 19400, 0)
    SetChrPos(0x105, -2530, 1990, 19200, 0)
    SetChrPos(0x104, -6130, 1990, 20650, 45)
    SetChrPos(0x1A3, -7940, 1760, 23860, 90)
    SetCameraDistance(9520, 4000)
    OP_0D()

    def lambda_B0DA():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B0DA)
    Sleep(50)

    def lambda_B0F2():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B0F2)
    Sleep(50)

    def lambda_B10A():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B10A)
    Sleep(50)

    def lambda_B122():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B122)
    Sleep(50)

    def lambda_B13A():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B13A)
    Sleep(50)

    def lambda_B152():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_B152)
    OP_63(0x14, 0x0, 1200, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    def lambda_B17C():
        OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_B17C)
    WaitChrThread(0x14, 1)
    OP_6F(0x10)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Oh a cat! How super cuuute!㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt's still a kitty.\x01",
            "Adorable!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x14)
    TurnDirection(0x14, 0x8, 500)
    OP_63(0x14, 0x0, 1200, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x14, 0x0, 1200, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x14, 1, 0, 38)
    Sleep(1000)
    OP_9B(0x1, 0x101, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(50)

    ChrTalk(
        0x101,
        "#11P#N#00011FCrap──\x02",
    )

    CloseMessageWindow()
    OP_5A()
    EndChrThread(0x14, 0x1)
    OP_64(0x14)

    def lambda_B280():

        label("loc_B280")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_B280")

    QueueWorkItem2(0x101, 1, lambda_B280)

    def lambda_B292():

        label("loc_B292")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_B292")

    QueueWorkItem2(0x104, 1, lambda_B292)

    def lambda_B2A4():

        label("loc_B2A4")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_B2A4")

    QueueWorkItem2(0x102, 1, lambda_B2A4)

    def lambda_B2B6():

        label("loc_B2B6")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_B2B6")

    QueueWorkItem2(0x109, 1, lambda_B2B6)

    def lambda_B2C8():

        label("loc_B2C8")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_B2C8")

    QueueWorkItem2(0x105, 1, lambda_B2C8)

    def lambda_B2DA():

        label("loc_B2DA")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_B2DA")

    QueueWorkItem2(0x1A3, 1, lambda_B2DA)

    def lambda_B2EC():

        label("loc_B2EC")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_B2EC")

    QueueWorkItem2(0x8, 1, lambda_B2EC)

    def lambda_B2FE():

        label("loc_B2FE")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_B2FE")

    QueueWorkItem2(0x9, 1, lambda_B2FE)
    Sound(953, 0, 100, 0)

    def lambda_B316():
        OP_95(0xFE, -2110, 2660, 36590, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_B316)
    Sleep(1500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x1A3, 0x1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)

    def lambda_B353():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_B353)
    WaitChrThread(0x14, 1)
    SetChrFlags(0x14, 0x80)
    OP_0D()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1A3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#N#00005FAh...!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#11P#00105FInto Arc-en-ciel...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#11P#10106FS-She's super fast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306F*sigh*... Anyway, we\x01",
            "should go there too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#6P#04609FYeah! She's just like\x01",
            "a rat in a trap!♪\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0410", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_37_A816 end

    def Function_38_B4F9(): pass

    label("Function_38_B4F9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B525")
    OP_93(0xFE, 0x0, 0x190)
    OP_93(0xFE, 0x5A, 0x190)
    OP_93(0xFE, 0xB4, 0x190)
    OP_93(0xFE, 0x10E, 0x190)
    Jump("Function_38_B4F9")

    label("loc_B525")

    Return()

    # Function_38_B4F9 end

    def Function_39_B526(): pass

    label("Function_39_B526")

    EventBegin(0x0)
    Fade(500)
    OP_68(-11770, 3710, 22190, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(11400, 0)
    SetChrPos(0x101, -10150, 1760, 22970, 0)
    SetChrPos(0x102, -11350, 1760, 22970, 0)
    SetChrPos(0x103, -10150, 1760, 21770, 0)
    SetChrPos(0x109, -11350, 1760, 21770, 0)
    SetChrPos(0x105, -10150, 1760, 20570, 0)
    SetChrPos(0x104, -11350, 1760, 20570, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xC, 0xFF)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "Welcome! Would you\x01",
            "like some ice cream?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, we're from the\x01",
            "Special Support Section...\x02",
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
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "Ah, so you're them. I heard\x01",
            "from the News Service people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Alright then. It's sudden, but I'd\x01",
            "like to recommend my "Sherbert\x01",
            ""Seven Colors" right away!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FWow, looks\x01",
            "quite delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's my new gelato that brings\x01",
            "together various flavors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I've added candy chips that\x01",
            "burst in your mouth, giving\x01",
            "it a unique texture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAlright then.\x01",
            "Let's try it out.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others ate the Sherbert "Seven Colors".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x109, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)

    ChrTalk(
        0x109,
        (
            "#10103F*chomp*.\x02\x03",
            "#10109F...Hmm, it's cold\x01",
            "and delicious!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        (
            "#00102FI agree. It's cute too, and I\x01",
            "feel it bursting in my mouth.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, our womenfolk\x01",
            "loves stuff like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x104,
        (
            "#00305FHuh? What's wrong,\x01",
            "peTiote? Brain freeze?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BA7D():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BA7D)

    def lambda_BA8A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BA8A)

    def lambda_BA97():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BA97)

    def lambda_BAA4():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BAA4)

    def lambda_BAB1():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BAB1)
    Sleep(1000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#00204FNo... Excuse me.\x02\x03",
            "#00200FIt was so shocking, \x01",
            "I lost myself for a moment.\x02",
        )
    )

    CloseMessageWindow()
    Sound(822, 0, 100, 0)
    OP_63(0x103, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1500)

    ChrTalk(
        0x103,
        (
            "#00204FWith the thrill of that bursting candy,\x01",
            "its freshness goes without saying...\x02\x03",
            "The seven flavors don't clash\x01",
            "and harmonize on the tongue.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        "#00201F#4SThis is truly a gelato revolution...!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0x103)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00206F...Sorry, I got\x01",
            "carried away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHa ha... Looks like you\x01",
            "like it. We'll have you\x01",
            "introduce this one, Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FYes, I think I will be able\x01",
            "to write a good comment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Ehehe, I am glad you like it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I look forward to your\x01",
            "continued patronage!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 4)
    SetScenarioFlags(0x172, 1)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_BDE2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BDE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_BDFF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BDFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_BE12")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BE12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_BE25")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BE25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_BE42")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BE42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_BE55")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BE55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_BE72")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BE72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_BE85")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BE85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_BEA2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BEA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_BEB5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BEB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_BED2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BED2")

    OP_29(0x80, 0x1, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BFFA")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BFF1")

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

    label("loc_BFF1")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_BFFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C0DE")
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

    label("loc_C0DE")

    OP_4C(0xC, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -10150, 1760, 22970, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_39_B526 end

    def Function_40_C10E(): pass

    label("Function_40_C10E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C11C")
    Jump("loc_C53C")

    label("loc_C11C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C12A")
    Jump("loc_C53C")

    label("loc_C12A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C138")
    Jump("loc_C53C")

    label("loc_C138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C146")
    Jump("loc_C53C")

    label("loc_C146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C1BA")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLooks like they're\x01",
            "busy rehearsing. \x01",
            "Let's refrain from entering.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_C53C")

    label("loc_C1BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C22E")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLooks like they're\x01",
            "busy rehearsing. \x01",
            "Let's refrain from entering.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_C53C")

    label("loc_C22E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C23C")
    Jump("loc_C53C")

    label("loc_C23C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C24A")
    Jump("loc_C53C")

    label("loc_C24A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C4AC")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C33A")

    ChrTalk(
        0x101,
        (
            "#00000FThat's right, they said the heads of\x01",
            "state were attending the theater today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWe'd be bothering them,\x01",
            "so let's put off our visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FYeah, that sounds like a good plan.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_C3A2")

    label("loc_C33A")


    ChrTalk(
        0x101,
        (
            "#00000FThey said the heads of state were\x01",
            "attending the theater today.\x01",
            "Let's refrain from entering.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3A2")

    Jump("loc_C491")

    label("loc_C3A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C445")

    ChrTalk(
        0x101,
        (
            "#00003F...There was a lot\x01",
            "of noise just now.\x02\x03",
            "#00000FThey've got to prepare to\x01",
            "receive the heads of state.\x01",
            "Let's hold off on entering.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_C491")

    label("loc_C445")


    ChrTalk(
        0x101,
        (
            "#00000FThere was a lot of noise just now. \x01",
            "Let's hold off on entering.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C491")

    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_C53C")

    label("loc_C4AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C4BA")
    Jump("loc_C53C")

    label("loc_C4BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C533")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLooks like Arc-en-ciel\x01",
            "is busy preparing. \x01",
            "Let's hold off on entering.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_C53C")

    label("loc_C533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C53C")

    label("loc_C53C")

    Return()

    # Function_40_C10E end

    def Function_41_C53D(): pass

    label("Function_41_C53D")

    EventBegin(0x0)
    Fade(500)
    OP_68(-2110, 4610, 31550, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x0, -2110, 2660, 31550, 180)
    SetChrPos(0x1, -2110, 2660, 31550, 180)
    SetChrPos(0x2, -2110, 2660, 31550, 180)
    SetChrPos(0x3, -2110, 2660, 31550, 180)
    ModifyEventFlags(1, 2, 0x80)
    EventEnd(0x5)
    Return()

    # Function_41_C53D end

    SaveToFile()

Try(main)
