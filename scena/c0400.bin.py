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
        "Function_8_158B",         # 08, 8
        "Function_9_17A0",         # 09, 9
        "Function_10_27F8",        # 0A, 10
        "Function_11_311C",        # 0B, 11
        "Function_12_3B66",        # 0C, 12
        "Function_13_4387",        # 0D, 13
        "Function_14_4FB8",        # 0E, 14
        "Function_15_5A39",        # 0F, 15
        "Function_16_667F",        # 10, 16
        "Function_17_6716",        # 11, 17
        "Function_18_6802",        # 12, 18
        "Function_19_69F5",        # 13, 19
        "Function_20_6A30",        # 14, 20
        "Function_21_6C0D",        # 15, 21
        "Function_22_6C72",        # 16, 22
        "Function_23_70D2",        # 17, 23
        "Function_24_716F",        # 18, 24
        "Function_25_71A6",        # 19, 25
        "Function_26_71D3",        # 1A, 26
        "Function_27_720D",        # 1B, 27
        "Function_28_722F",        # 1C, 28
        "Function_29_7269",        # 1D, 29
        "Function_30_72A4",        # 1E, 30
        "Function_31_72FB",        # 1F, 31
        "Function_32_73A1",        # 20, 32
        "Function_33_864A",        # 21, 33
        "Function_34_87DF",        # 22, 34
        "Function_35_8CEC",        # 23, 35
        "Function_36_8E47",        # 24, 36
        "Function_37_A602",        # 25, 37
        "Function_38_B2BE",        # 26, 38
        "Function_39_B2EB",        # 27, 39
        "Function_40_BE9D",        # 28, 40
        "Function_41_C2CA",        # 29, 41
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_150A")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "My, it's all of you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard the rumors, but the\x01",
            "Special Support Section has\x01",
            "restarted, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes. We got some new\x01",
            "members, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FEven so, isn't it strange\x01",
            "for you to be working in\x01",
            "Entertainment District?\x02\x03",
            "#00100FI feel like you're always\x01",
            "in Central Square...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes. Lately, I've been\x01",
            "on the lookout for a\x01",
            "certain orbal car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That aside, I'm looking\x01",
            "forward to seeing your\x01",
            "accomplishments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's both do our best\x01",
            "from here on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 4)
    Jump("loc_1587")

    label("loc_150A")


    ChrTalk(
        0xFE,
        (
            "Haha, I heard the rumors,\x01",
            "but the Special Support\x01",
            "Section has restarted, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's both do our best\x01",
            "from here on!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1587")

    TalkEnd(0xFE)
    Return()

    # Function_7_12B7 end

    def Function_8_158B(): pass

    label("Function_8_158B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1650")

    ChrTalk(
        0xFE,
        (
            "In addition to the terrorists,\x01",
            "the actions of Red Constellation\x01",
            "and Heiyue are both odd as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For who and what reason\x01",
            "do they act? ...We can't\x01",
            "take our eyes off them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_179C")

    label("loc_1650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_16F8")

    ChrTalk(
        0xFE,
        (
            "Though the unveiling ceremony ended\x01",
            "without incident, our security\x01",
            "duties have only just begun.\x02",
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
    Jump("loc_179C")

    label("loc_16F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_179C")

    ChrTalk(
        0xFE,
        (
            "We're getting ready for the\x01",
            "Arc-en-Ciel performances before\x01",
            "and after the conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems there's fewer\x01",
            "people in this plaza\x01",
            "because of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179C")

    TalkEnd(0xFE)
    Return()

    # Function_8_158B end

    def Function_9_17A0(): pass

    label("Function_9_17A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17D7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17D7")
    Call(0, 39)
    Return()

    label("loc_17D7")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27F4")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1836")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1836")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1856")
    OP_AF(0x7E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_27EF")

    label("loc_1856")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_186A")
    Jump("loc_27EF")

    label("loc_186A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27EF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_18E4")

    ChrTalk(
        0xC,
        (
            "Ehehe, I'm glad you like\x01",
            "it.\x02",
        )
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
    Jump("loc_27EF")

    label("loc_18E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1969")

    ChrTalk(
        0xC,
        (
            "Really, what an amazing\x01",
            "uproar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Somehow, I feel like the\x01",
            "ice cream will melt due\x01",
            "to all this enthusiasm...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27EF")

    label("loc_1969")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A2B")

    ChrTalk(
        0xC,
        (
            "Ilya...I'm really\x01",
            "worried about her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My only talent is\x01",
            "selling ice cream,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I intend to continue my\x01",
            "business here while\x01",
            "waiting for Ilya's return.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A93")

    label("loc_1A2B")


    ChrTalk(
        0xC,
        (
            "Ice cream, would you\x01",
            "like some ice cream?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's pleasantly cool,\x01",
            "refreshing and very\x01",
            "gooood...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A93")

    Jump("loc_27EF")

    label("loc_1A98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1BDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B47")

    ChrTalk(
        0xC,
        (
            "Welcome! Would you like\x01",
            "some ice cream!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Tonight is the long-\x01",
            "awaited opening of the\x01",
            "renewal performance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I hope everyone enjoys\x01",
            "it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BD6")

    label("loc_1B47")


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
            "Arc-en-Ciel and sell ice\x01",
            "cream as usual!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD6")

    Jump("loc_27EF")

    label("loc_1BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1BE9")
    Jump("loc_27EF")

    label("loc_1BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1D20")

    ChrTalk(
        0xC,
        (
            "Ice cream, would you\x01",
            "like some ice cream?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Have you all had lunch?\x01",
            "Ice cream is great after\x01",
            "lunch, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D1B")

    ChrTalk(
        0x101,
        (
            "#00008F(I think we can get\x01",
            "coverage for the gourmet\x01",
            "guide here, but...)\x02\x03",
            "#00003F(Now's not the time.\x01",
            "Let's not forget to stop\x01",
            "by later.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D1B")

    Jump("loc_27EF")

    label("loc_1D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1DBE")

    ChrTalk(
        0xC,
        (
            "The Arc-en-Ciel\x01",
            "performance finally opens\x01",
            "the day after tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'll have more customers\x01",
            "again, right? Hahaha,\x01",
            "I'll be filthy rich.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27EF")

    label("loc_1DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1F1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E96")

    ChrTalk(
        0xC,
        (
            "Ice cream, would you\x01",
            "like some ice cream?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you need help deciding,\x01",
            "I'd be happy to offer you\x01",
            "a sample of any flavor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'll give you a taste\x01",
            "with these special mini-\x01",
            "spoons.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F18")

    label("loc_1E96")


    ChrTalk(
        0xC,
        (
            "My ice cream sampling\x01",
            "service is popular, and\x01",
            "sales are up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Of course, this cart was\x01",
            "No. 1 in sales this\x01",
            "month. Viva!☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F18")

    Jump("loc_27EF")

    label("loc_1F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_201D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA9")

    ChrTalk(
        0xC,
        (
            "Arc-en-Ciel will be on\x01",
            "vacation soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm, my sales will\x01",
            "plummet. I'll need to\x01",
            "deal with that somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2018")

    label("loc_1FA9")


    ChrTalk(
        0xC,
        (
            "Hmm. At this rate, I'll\x01",
            "lose my spot as the No.\x01",
            "1 selling cart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'll need to deal with\x01",
            "this somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2018")

    Jump("loc_27EF")

    label("loc_201D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2522")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20F1")

    ChrTalk(
        0xFE,
        (
            "If you're looking for that redheaded\x01",
            "customer of mine from just now, they\x01",
            "went toward Residential Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though he was\x01",
            "wearing a nice suit, he\x01",
            "looked out of place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251D")

    label("loc_20F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2343")

    ChrTalk(
        0xFE,
        (
            "Just now, a cheerful redheaded\x01",
            "man asked me to make a\x01",
            ""10-scoop cone" for him.\x02",
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
            "Even though he was\x01",
            "wearing a nice suit, he\x01",
            "looked out of place.\x02",
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
            "#10106F(L-Lloyd. Most likely,\x01",
            "it's him...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FU-Umm... Which way did\x01",
            "he go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He got some brain freeze\x01",
            "and headed toward\x01",
            "Residential Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Alright... Let's follow\x01",
            "him.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1C7, 2)
    Jump("loc_251D")

    label("loc_2343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_249B")

    ChrTalk(
        0xC,
        (
            "There sure was a lot of\x01",
            "noise this morning.\x02",
        )
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
            "the unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hahaha. With this, I'll have secured\x01",
            "the award for being the top-selling\x01",
            "food cart three months running!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_251D")

    label("loc_249B")


    ChrTalk(
        0xC,
        (
            "Thanks to that, it looks\x01",
            "like I'll sell out early\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That means you've got to\x01",
            "buy now or you might\x01",
            "regret it later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_251D")

    Jump("loc_27EF")

    label("loc_2522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2689")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2616")

    ChrTalk(
        0xC,
        (
            "Regular ice cream or\x01",
            "sherbert. Which do all\x01",
            "of you prefer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By the way, Ilya likes sherbert\x01",
            "and Pliｳ likes ice cream. Both\x01",
            "come here often, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh, and Rixia often gets\x01",
            "sherbert, the same as\x01",
            "Ilya.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2684")

    label("loc_2616")


    ChrTalk(
        0xC,
        (
            "And Eugene likes ice\x01",
            "cream, and Theodore...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...It seems he dislikes\x01",
            "sweets and doesn't buy\x01",
            "from me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2684")

    Jump("loc_27EF")

    label("loc_2689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2697")
    Jump("loc_27EF")

    label("loc_2697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_27EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2747")

    ChrTalk(
        0xC,
        (
            "Ice cream, would you\x01",
            "like some ice cream?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We have a variety of\x01",
            "flavors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The next time you come,\x01",
            "please look for your\x01",
            "favorite flavor.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27EF")

    label("loc_2747")


    ChrTalk(
        0xC,
        (
            "If you'd like to blend\x01",
            "flavors, please, just\x01",
            "ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Though, if you disregard my advice\x01",
            "and mix two incompatible flavors, I\x01",
            "won't be responsible for the result.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27EF")

    Jump("loc_17E4")

    label("loc_27F4")

    TalkEnd(0xFE)
    Return()

    # Function_9_17A0 end

    def Function_10_27F8(): pass

    label("Function_10_27F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_287C")

    ChrTalk(
        0xFE,
        (
            "Dear me... The situation\x01",
            "is going crazy somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In any case, I just wish\x01",
            "troubles would leave me\x01",
            "alone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3118")

    label("loc_287C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2908")

    ChrTalk(
        0xFE,
        (
            "Heh heh heh, don't you\x01",
            "want to come drink at\x01",
            "our store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'll be able to learn\x01",
            "a lot due to our\x01",
            ""charity service".\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3118")

    label("loc_2908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2990")

    ChrTalk(
        0xFE,
        (
            "Hmm, dangerous things\x01",
            "have been occurring\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Normally, quarrels like\x01",
            "that are part of Back\x01",
            "Street's charm.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3118")

    label("loc_2990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_299E")
    Jump("loc_3118")

    label("loc_299E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2A97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A2E")

    ChrTalk(
        0xFE,
        (
            "Ah, there aren't any\x01",
            "rich suckers around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whoops. Hehehe, I\x01",
            "accidently let out what\x01",
            "I was really thinking.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A92")

    label("loc_2A2E")


    ChrTalk(
        0xFE,
        (
            "Hehehe, I accidently let\x01",
            "out what I was really\x01",
            "thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's proof that I'm too\x01",
            "relaxed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A92")

    Jump("loc_3118")

    label("loc_2A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B01")

    ChrTalk(
        0xFE,
        (
            "Now then, I've got to do\x01",
            "my best at work today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll show you a world\x01",
            "of dreams.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3118")

    label("loc_2B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2C5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF3")

    ChrTalk(
        0xFE,
        (
            "Arc-en-Ciel is blessed\x01",
            "with newcomers, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say Sully will be\x01",
            "appearing in the role of\x01",
            "a new princess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It hasn't even been a year since\x01",
            "they took on Rixia. I wish\x01",
            "they'd share the love a little.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C55")

    label("loc_2BF3")


    ChrTalk(
        0xFE,
        (
            "Even so, all the Arc-en-\x01",
            "Ciel ladies are lovely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish they'd share the\x01",
            "love a little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C55")

    Jump("loc_3118")

    label("loc_2C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2CFA")

    ChrTalk(
        0xFE,
        (
            "For people like us, there's\x01",
            "nothing interesting about\x01",
            "the trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've gotten fewer\x01",
            "congressmen lately, so\x01",
            "business is down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3118")

    label("loc_2CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2D9B")

    ChrTalk(
        0xFE,
        (
            "There's a lot of foot traffic\x01",
            "today, but they're all\x01",
            "citizens and no tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How should I say this...\x01",
            "I miss the Anniversary\x01",
            "Festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3118")

    label("loc_2D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E0F")

    ChrTalk(
        0xFE,
        (
            "Ah, those police are\x01",
            "keeping their eye on us.\x02",
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
    Jump("loc_3118")

    label("loc_2E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2E1D")
    Jump("loc_3118")

    label("loc_2E1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3118")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A0")

    ChrTalk(
        0xFE,
        (
            "Hehehe, if you've some\x01",
            "free time, come have a\x01",
            "drink inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If all four of you are\x01",
            "coming, we have a\x01",
            "special group discount.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FWow, how much is it?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EFB")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_2EFB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F1E")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_2F1E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F41")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_2F41")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F61")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_2F61")

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
        "#10101FW-Wazy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FUmm, we're working you\x01",
            "see, so we can't\x01",
            "really...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm? Man, don't tease me\x01",
            "like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then shoo, shoo! You're\x01",
            "getting in the way of\x01",
            "sales.\x02",
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
    Jump("loc_3118")

    label("loc_30A0")


    ChrTalk(
        0xFE,
        (
            "If you're just going to\x01",
            "tease me, then please,\x01",
            "just don't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll get angry if you're\x01",
            "too persistent, you\x01",
            "hear?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3118")

    TalkEnd(0xFE)
    Return()

    # Function_10_27F8 end

    def Function_11_311C(): pass

    label("Function_11_311C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_31D0")

    ChrTalk(
        0xFE,
        (
            "It must've been the\x01",
            "Empire that hurt Lady\x01",
            "Ilya, for sure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why... I won't ever\x01",
            "forgive the Empire! Taking orders\x01",
            "from them!? Over my dead body!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B62")

    label("loc_31D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3270")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_322A")

    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Lady Ilya... Why did\x01",
            "this have to...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_326B")

    label("loc_322A")


    ChrTalk(
        0xFE,
        (
            "I won't forgive... the\x01",
            "culprits... I'll never\x01",
            "forgive them!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_326B")

    Jump("loc_3B62")

    label("loc_3270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3310")

    ChrTalk(
        0xFE,
        (
            "Sorry... It's just\x01",
            "that... the renewal\x01",
            "performance is tonight!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lady I-ly-a! From here,\x01",
            "I'll pray for the success\x01",
            "of your performance!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B62")

    label("loc_3310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3492")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_340A")

    ChrTalk(
        0xFE,
        (
            "Tomorrow... It's already tomorrow...\x01",
            "It's finally tomorrow... At last,\x01",
            "it's tomorrow!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lady Ilya, it's too bad I won't be able to\x01",
            "see you opening night, but... There's no\x01",
            "way Polise will be able to sleep tonight!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_348D")

    label("loc_340A")


    ChrTalk(
        0xFE,
        (
            "Lady Ilya, it's too bad I won't be able to\x01",
            "see you opening night, but... There's no\x01",
            "way Polise will be able to sleep tonight!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_348D")

    Jump("loc_3B62")

    label("loc_3492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_34E3")

    ChrTalk(
        0xFE,
        "Lady Ilya, Lady Ilya!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please do your best at\x01",
            "practice!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B62")

    label("loc_34E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_363C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35BD")

    ChrTalk(
        0xFE,
        (
            "The day after tomorrow...\x01",
            "At last, it's the day\x01",
            "after tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what the\x01",
            "connection between Lady\x01",
            "Ilya and Sully is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*drool*... Guhuhu...\x01",
            "Imagining it is\x01",
            "irresistable!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3637")

    label("loc_35BD")


    ChrTalk(
        0xFE,
        (
            "I wonder what the\x01",
            "connection between Lady\x01",
            "Ilya and Sully is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*drool*... Guhuhu...\x01",
            "Imagining it is\x01",
            "irresistable!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3637")

    Jump("loc_3B62")

    label("loc_363C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_36C6")

    ChrTalk(
        0xFE,
        (
            "In three days...\x01",
            "Finally, it's in just\x01",
            "three days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Opening night of the\x01",
            "renewal performance...\x01",
            "Oh, I can't wait!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B62")

    label("loc_36C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3849")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37B8")

    ChrTalk(
        0xFE,
        (
            "Even on days without a\x01",
            "performance, Lady Ilya should\x01",
            "be going to the theater!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In other words, this is\x01",
            "my chance to take even\x01",
            "more Ilya photos!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I still come\x01",
            "here even during their\x01",
            "time off!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3844")

    label("loc_37B8")


    ChrTalk(
        0xFE,
        (
            "Lady Ilya should be coming\x01",
            "to the theater for\x01",
            "practice from here on out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I still come\x01",
            "here even during their\x01",
            "time off!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3844")

    Jump("loc_3B62")

    label("loc_3849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_38D7")

    ChrTalk(
        0xFE,
        (
            "This evening, it seems\x01",
            "the heads of state will\x01",
            "see Arc-en-Ciel perform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ooh, how unfair! I\x01",
            "wanted an invitation\x01",
            "too!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B62")

    label("loc_38D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3A8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C9")

    ChrTalk(
        0xFE,
        "#4SThis sucks!!#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected, way too many people\x01",
            "wanted tickets for opening night\x01",
            "and I couldn't get one!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What I ended up getting was a\x01",
            "B seat one week after opening\x01",
            "night. I'm happy... yet sad!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3A88")

    label("loc_39C9")


    ChrTalk(
        0xFE,
        (
            "As expected, way too many people\x01",
            "wanted tickets for opening night\x01",
            "and I couldn't get one!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What I ended up getting was a\x01",
            "B seat one week after opening\x01",
            "night. I'm happy... yet sad!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A88")

    Jump("loc_3B62")

    label("loc_3A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3ADC")

    ChrTalk(
        0xFE,
        "Lady I-ly-a!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Polise won't lose to\x01",
            "something like rain!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B62")

    label("loc_3ADC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3B62")

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
            "Ooh, what is with her?\x01",
            "What is she to Lady\x01",
            "Ilya?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B62")

    TalkEnd(0xFE)
    Return()

    # Function_11_311C end

    def Function_12_3B66(): pass

    label("Function_12_3B66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3BB7")

    ChrTalk(
        0xFE,
        (
            "Ohhh... Well said, Mr.\x01",
            "President!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Now we'll be free!!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_3BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3C33")

    ChrTalk(
        0xFE,
        (
            "Lady Ilya... They say\x01",
            "she's still in a coma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Shit. Seriously, why\x01",
            "did it have to come to\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_3C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3CBF")

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
            "#4SEveryone at Arc-en-Ciel!\x01",
            "We fans are always\x01",
            "watching over you!!#3S\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_3CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D43")

    ChrTalk(
        0xFE,
        (
            "Hehe, I bet they're\x01",
            "rehearsing inside around\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#4SArc-en-Ciel, banzai!!\x01",
            "Renewal performance,\x01",
            "banzai!!#3S\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_3D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3DB8")

    ChrTalk(
        0xFE,
        (
            "Lady Ilya, Rixia, Sully,\x01",
            "and also Pliｳ and\x01",
            "Celine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#4SI love each and every\x01",
            "one of you!#3S\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_3DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3E08")

    ChrTalk(
        0xFE,
        (
            "Hey Polise, you're\x01",
            "drooling... And that\x01",
            "expression is scary.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_3E08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3EB1")

    ChrTalk(
        0xFE,
        (
            "Lady Ilya, Rixia and\x01",
            "Sully are cast as the\x01",
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
    Jump("loc_4383")

    label("loc_3EB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3F96")

    ChrTalk(
        0xFE,
        (
            "To prepare for the renewal\x01",
            "performance, Arc-en-Ciel will be\x01",
            "taking a break soon, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "During that time, they'll be practicing\x01",
            "their dancing inside the theater... I\x01",
            "want to see it so bad, I could die!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_3F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4005")

    ChrTalk(
        0xFE,
        (
            "That's right... Even if they're\x01",
            "heads of state, this is better\x01",
            "treatment than they deserve!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_4005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_40B6")

    ChrTalk(
        0xFE,
        (
            "That Polise. If she's so\x01",
            "set on it, maybe I should\x01",
            "give her my ticket?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, I guess it's fine. As\x01",
            "fellow die-hard fans, we\x01",
            "have to help each other out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_40B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_413E")

    ChrTalk(
        0xFE,
        (
            "Hehe, it's days like this\x01",
            "that separate us from\x01",
            "other die-hard fan groups!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#4SLady Ilya, Rixia! We\x01",
            "love youuu!!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_413E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4383")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_422C")
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
            "You guys are the police that\x01",
            "were going in and out of the\x01",
            "theater a while back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Must be nice to be an\x01",
            "officer. You can enter\x01",
            "the theater for work~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4383")

    label("loc_422C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F7")

    ChrTalk(
        0xFE,
        (
            "Maybe I'll enter police\x01",
            "academy and become an\x01",
            "officer~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that, I'd use\x01",
            "patrolling as an excuse to\x01",
            "visit Arc-en-Ciel daily...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Um, I think that's\x01",
            "impossible.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4383")

    label("loc_42F7")


    ChrTalk(
        0xFE,
        (
            "Maybe I'll enter police\x01",
            "academy and become an\x01",
            "officer~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that, I'd use\x01",
            "patrolling as an excuse to\x01",
            "visit Arc-en-Ciel daily...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4383")

    TalkEnd(0xFE)
    Return()

    # Function_12_3B66 end

    def Function_13_4387(): pass

    label("Function_13_4387")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_447A")

    ChrTalk(
        0xFE,
        (
            "There was some kind of rumor but\x01",
            "to think the two major powers\x01",
            "would do such a cowardly thing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I completely agree with the President's\x01",
            "claim. If we don't stand up against them\x01",
            "now, the same tragedy will be repeated!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB4")

    label("loc_447A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4544")

    ChrTalk(
        0xFE,
        (
            "The Arc-en-Ciel play... The\x01",
            "truth is that I was supposed\x01",
            "to see it today, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With what has happened, there's\x01",
            "nothing I can do about it... I\x01",
            "wonder if Lady Ilya is all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB4")

    label("loc_4544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_45BC")

    ChrTalk(
        0xFE,
        (
            "That Mainz incident...\x01",
            "It must be truly\x01",
            "frightening.\x02",
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
    Jump("loc_4FB4")

    label("loc_45BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_45CA")
    Jump("loc_4FB4")

    label("loc_45CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_463B")

    ChrTalk(
        0xFE,
        (
            "Central Square seems\x01",
            "noisy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't really get it,\x01",
            "but maybe it's some kind\x01",
            "of accident?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB4")

    label("loc_463B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_478A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4720")

    ChrTalk(
        0xFE,
        (
            "The renewal performance's\x01",
            "opening night is the day\x01",
            "after tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though I of course couldn't get\x01",
            "ticket for opening night, I plan\x01",
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
    Jump("loc_4785")

    label("loc_4720")


    ChrTalk(
        0xFE,
        (
            "I plan to see the renewal\x01",
            "performance one week\x01",
            "after opening night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhuhu, I'm so excited.\x02",
    )

    CloseMessageWindow()

    label("loc_4785")

    Jump("loc_4FB4")

    label("loc_478A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_48E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48A4")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        (
            "My, it's you, Wazy.\x01",
            "Thanks for the other\x01",
            "day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, thanks to you, I\x01",
            "had a dream-like hour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHehe, same here. I'm\x01",
            "glad to hear you say\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(That Wazy... Just when\x01",
            "did he sneak in a host\x01",
            "job?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_48E1")

    label("loc_48A4")

    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        (
            "Haha, Wazy. Let's see\x01",
            "each other again\x01",
            "sometime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48E1")

    Jump("loc_4FB4")

    label("loc_48E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4A66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49D6")

    ChrTalk(
        0xFE,
        (
            "I was just thinking that\x01",
            "Former Chairman Hartmann\x01",
            "is in a cell right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And he's already completely\x01",
            "disappeared from the topics\x01",
            "of everyday conversation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People can be pretty\x01",
            "heartless sometimes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4A61")

    label("loc_49D6")


    ChrTalk(
        0xFE,
        (
            "Chairman Hartmann has completely\x01",
            "disappeared from the topics of\x01",
            "everyday conversation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People can be pretty\x01",
            "heartless sometimes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A61")

    Jump("loc_4FB4")

    label("loc_4A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4AE1")

    ChrTalk(
        0xFE,
        (
            "Orchis Tower... So its\x01",
            "form was finally\x01",
            "revealed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Who knew buildings\x01",
            "could be this exciting?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB4")

    label("loc_4AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4BCB")

    ChrTalk(
        0xFE,
        (
            "The high-class club Neue-Blanc... According\x01",
            "to rumor they recently opened after\x01",
            "remodeling, but I'd like to go there myself.\x02",
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
    Jump("loc_4FB4")

    label("loc_4BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4BD9")
    Jump("loc_4FB4")

    label("loc_4BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4FB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EFE")
    TurnDirection(0xFE, 0x105, 0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "My, you are... Are you\x01",
            "Wazy, the host?\x02",
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
            "that there was a handsome\x01",
            "host in this neighborhood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, you're as sexy as\x01",
            "the rumors say, aren't\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHaha, thanks.\x02\x03",
            "#10302FI'll come to your store\x01",
            "if you like. There, we\x01",
            "can have a nice chat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu. Next time, I'd\x01",
            "love to.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D91")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4D91")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DB7")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4DB7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DDD")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4DDD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E03")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4E03")

    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00106F(T-That's Wazy for you.\x01",
            "He sure does know a lot\x01",
            "of people.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Maybe you should focus on the\x01",
            "fact that he's conducting business\x01",
            "brazenly right in front of us.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F(Enough of this... I'll\x01",
            "reprimand him later.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 1)
    Jump("loc_4FB4")

    label("loc_4EFE")


    ChrTalk(
        0xFE,
        (
            "I heard for a long time\x01",
            "that there was a handsome\x01",
            "host in this neighborhood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu. Next time, I'll\x01",
            "take you to our store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha, I'll be looking\x01",
            "forward to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FB4")

    TalkEnd(0xFE)
    Return()

    # Function_13_4387 end

    def Function_14_4FB8(): pass

    label("Function_14_4FB8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5062")

    ChrTalk(
        0xFE,
        (
            "The "Independent State of\x01",
            "Crossbell", eh? Hehe, that\x01",
            "doesn't sound too bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It means that from now\x01",
            "on we won't be citizens,\x01",
            "we'll be a nation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A35")

    label("loc_5062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_51BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5183")

    ChrTalk(
        0xFE,
        (
            "Things have finally calmed down lately,\x01",
            "but ever since that attack, it's like\x01",
            "the entire city is in a gloomy mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, that's just what I think... Because\x01",
            "the situation is like this, I must revitalize\x01",
            "the economy by partying even more than usual.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_51B7")

    label("loc_5183")


    ChrTalk(
        0xFE,
        (
            "And so, for that reason,\x01",
            "I'll party today too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51B7")

    Jump("loc_5A35")

    label("loc_51BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_52FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5280")

    ChrTalk(
        0xFE,
        (
            "It looks like Mainz is in a\x01",
            "pinch, but even if we panic,\x01",
            "there's nothing we can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I plan to enjoy\x01",
            "myself here in Entertainment\x01",
            "District 'til I drop.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_52FA")

    label("loc_5280")


    ChrTalk(
        0xFE,
        (
            "Oh yeah, today is\x01",
            "opening day for that\x01",
            "renewal performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. I'm jealous of\x01",
            "those who get to see it\x01",
            "first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52FA")

    Jump("loc_5A35")

    label("loc_52FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5382")

    ChrTalk(
        0xFE,
        (
            "Now then, which bar\x01",
            "shall I go to today~?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. Today's not a bad\x01",
            "day for getting smashed\x01",
            "drinking alone~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A35")

    label("loc_5382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5430")

    ChrTalk(
        0xFE,
        (
            "I was playing slots at\x01",
            "the casino, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, it's no good.\x01",
            "Luck has abandoned me\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On a day like today, I\x01",
            "think I'll go home and\x01",
            "rest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A35")

    label("loc_5430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_54C5")

    ChrTalk(
        0xFE,
        (
            "I wonder if there's any\x01",
            "strategy to the casino's\x01",
            "slots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like there's\x01",
            "machines that pay out and\x01",
            "machines that don't...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A35")

    label("loc_54C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_55C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5558")

    ChrTalk(
        0xFE,
        (
            "Now then, time to go\x01",
            "all-out playing today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As for today's money...\x01",
            "This is bad. I'll have\x01",
            "to replenish soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_55BF")

    label("loc_5558")


    ChrTalk(
        0xFE,
        (
            "I've had a string of\x01",
            "losses recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. Maybe I'll ask my\x01",
            "parents for pocket money\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55BF")

    Jump("loc_5A35")

    label("loc_55C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_568E")

    ChrTalk(
        0xFE,
        (
            "After their next performance,\x01",
            "Arc-en-Ciel is going to be on\x01",
            "break for a while, they said.\x02",
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
    Jump("loc_5A35")

    label("loc_568E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_57A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_574F")

    ChrTalk(
        0xFE,
        (
            "As expected, I couldn't see\x01",
            "it from up close, but I did\x01",
            "see the unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Orchis Tower sure is\x01",
            "amazing.\x02",
        )
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
    Jump("loc_579C")

    label("loc_574F")


    ChrTalk(
        0xFE,
        (
            "Orchis Tower sure is\x01",
            "amazing.\x02",
        )
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

    label("loc_579C")

    Jump("loc_5A35")

    label("loc_57A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5914")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5894")

    ChrTalk(
        0xFE,
        (
            "Ah, there are officers\x01",
            "patrolling everywhere~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it's because the\x01",
            "trade conference starts\x01",
            "tomorrow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand where they're coming\x01",
            "from, but I wish the officers\x01",
            "around here'd give me a break.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_590F")

    label("loc_5894")


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
            "It's hard to enjoy myself\x01",
            "when there are officers\x01",
            "around for some reason.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_590F")

    Jump("loc_5A35")

    label("loc_5914")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_59B7")

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
            "play my heart out\x01",
            "today~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A35")

    label("loc_59B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5A35")

    ChrTalk(
        0xFE,
        (
            "Alright! Today, I'll\x01",
            "play 'til I drop!\x02",
        )
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

    label("loc_5A35")

    TalkEnd(0xFE)
    Return()

    # Function_14_4FB8 end

    def Function_15_5A39(): pass

    label("Function_15_5A39")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5B3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AD7")

    ChrTalk(
        0xFE,
        (
            "Hello, how're you\x01",
            "doooing☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Casino House Barca is in\x01",
            "high spirits today too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, come and have\x01",
            "some fuuun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5B36")

    label("loc_5AD7")


    ChrTalk(
        0xFE,
        (
            "Casino House Barca is in\x01",
            "high spirits today too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, come and have\x01",
            "some fuuun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B36")

    Jump("loc_667B")

    label("loc_5B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5BA1")

    ChrTalk(
        0xFE,
        (
            "Hello, how're you\x01",
            "doooing☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why not come to the\x01",
            "casino for a shot of\x01",
            "energy~?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_667B")

    label("loc_5BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5CC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C4D")

    ChrTalk(
        0xFE,
        (
            "Hello, how're you\x01",
            "doooing☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu. The renewal\x01",
            "performance's opening\x01",
            "day has finally come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, you must look\x01",
            "aliiive, seee?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5CBD")

    label("loc_5C4D")


    ChrTalk(
        0xFE,
        (
            "Uhuhu. The renewal\x01",
            "performance's opening\x01",
            "day has finally come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, you must look\x01",
            "aliiive, seee?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CBD")

    Jump("loc_667B")

    label("loc_5CC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5D37")

    ChrTalk(
        0xFE,
        (
            "Hello, how're you\x01",
            "doooing☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why don't you come\x01",
            "inside to shelter from\x01",
            "the rain, if you want?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_667B")

    label("loc_5D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5DB0")

    ChrTalk(
        0xFE,
        (
            "Hello, how're you\x01",
            "doooing☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu. If you want to\x01",
            "leave a tip, you're\x01",
            "always more than welcome㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_667B")

    label("loc_5DB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5E19")

    ChrTalk(
        0xFE,
        (
            "Hello, how're you\x01",
            "doooing☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu. I'll give you\x01",
            "plenty of service again\x01",
            "today㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_667B")

    label("loc_5E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5F6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EDD")

    ChrTalk(
        0xFE,
        (
            "Hello, how're you\x01",
            "doooing☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not that I always\x01",
            "wear these clothes, you\x01",
            "know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu. If my boyfriend\x01",
            "wanted it, I could wear\x01",
            "them in private, though㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5F65")

    label("loc_5EDD")


    ChrTalk(
        0xFE,
        (
            "It's not that I always\x01",
            "wear these clothes, you\x01",
            "know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu. If my boyfriend\x01",
            "wanted it, I could wear\x01",
            "them in private, though㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F65")

    Jump("loc_667B")

    label("loc_5F6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6071")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6009")

    ChrTalk(
        0xFE,
        (
            "Hello, how're you\x01",
            "doooing☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, the sun's rays\x01",
            "are strong again today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, I'll get\x01",
            "tan lines again㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_606C")

    label("loc_6009")


    ChrTalk(
        0xFE,
        (
            "Even so, the sun's rays\x01",
            "are strong again today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, I'll get\x01",
            "tan lines again㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_606C")

    Jump("loc_667B")

    label("loc_6071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_61DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6142")

    ChrTalk(
        0xFE,
        (
            "Hello, how're you\x01",
            "doooing☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say the heads of state\x01",
            "are going to see the Arc-\x01",
            "en-Ciel play this evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu. With the\x01",
            "occasion, I wonder if\x01",
            "they'll stop here~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_61D7")

    label("loc_6142")


    ChrTalk(
        0xFE,
        (
            "They say the heads of state\x01",
            "are going to see the Arc-\x01",
            "en-Ciel play this evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu. With the\x01",
            "occasion, I wonder if\x01",
            "they'll stop here~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61D7")

    Jump("loc_667B")

    label("loc_61DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6478")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_641D")

    ChrTalk(
        0xFE,
        (
            "Oh, if it isn't Mr. Randy. You\x01",
            "haven't shown up in a long time.\x01",
            "I wonder what you've been up to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FYeah, sorry. I had some\x01",
            "minor business to attend\x01",
            "to.\x02\x03",
            "#00300FI'll treat you next\x01",
            "time, so won't you\x01",
            "forgive me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu. Whether I forgive\x01",
            "you or not, I can't\x01",
            "accept your proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're that sorry\x01",
            "about it, then come lose\x01",
            "some mira at our place☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, professional as\x01",
            "always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F(How to say this...\x01",
            "Randy seems used to\x01",
            "this.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Yeah, well to Randy,\x01",
            "this place is something\x01",
            "akin to a home.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 4)
    Jump("loc_6473")

    label("loc_641D")


    ChrTalk(
        0xFE,
        (
            "If you're that sorry about\x01",
            "it Mr. Randy, then come lose\x01",
            "some mira at our place☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6473")

    Jump("loc_667B")

    label("loc_6478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_64FD")

    ChrTalk(
        0xFE,
        (
            "Hello, how're you\x01",
            "doooing☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On a day like today, I\x01",
            "recommend coming to our store\x01",
            "and having a ton of fuuun㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_667B")

    label("loc_64FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_667B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6624")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65CC")

    ChrTalk(
        0xFE,
        (
            "Hello, how're you\x01",
            "doooing☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huh? Has a redheaded man\x01",
            "come here, you ask?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you his friend? If\x01",
            "you're looking for him, he\x01",
            "just came by our store㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_661F")

    label("loc_65CC")


    ChrTalk(
        0xFE,
        (
            "Hello, how're you\x01",
            "doooing☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A redheaded man? He just\x01",
            "came to our store㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_661F")

    Jump("loc_667B")

    label("loc_6624")


    ChrTalk(
        0xFE,
        (
            "Hello, how're you\x01",
            "doooing☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu. Go have a looot\x01",
            "of fun again today, ok?㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_667B")

    TalkEnd(0xFE)
    Return()

    # Function_15_5A39 end

    def Function_16_667F(): pass

    label("Function_16_667F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "So this is the famed\x01",
            "Arc-en-Ciel... Haha,\x01",
            "I've finally arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got my tickets earlier,\x01",
            "so I just need to wait\x01",
            "for the performance.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_667F end

    def Function_17_6716(): pass

    label("Function_17_6716")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Their greatest masterpiece is called\x01",
            ""Golden Sun, Silver Moon", huh. I\x01",
            "can't help but look forward to it.\x02",
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

    # Function_17_6716 end

    def Function_18_6802(): pass

    label("Function_18_6802")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6977")
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

    def lambda_692D():
        OP_96(0xFE, 0xFFFFE0D4, 0x0, 0xE88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_692D)
    EndChrThread(0xA, 0xFF)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0xA, 14040, 0, 11290, 90)

    def lambda_6962():
        OP_95(0xFE, 37920, 0, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6962)

    label("loc_6977")

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

    # Function_18_6802 end

    def Function_19_69F5(): pass

    label("Function_19_69F5")

    SetChrPos(0xFE, 13050, 0, -18750, 225)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -8000, 0, -600)
    OP_9F(0x1, -24250, 0, 8350)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_19_69F5 end

    def Function_20_6A30(): pass

    label("Function_20_6A30")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B8B")
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

    def lambda_6B5B():
        OP_96(0xFE, 0x3F15, 0x0, 0xFFFFAF42, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6B5B)
    EndChrThread(0xA, 0xFF)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0xA, -3100, 1760, 9570, 180)

    label("loc_6B8B")

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

    # Function_20_6A30 end

    def Function_21_6C0D(): pass

    label("Function_21_6C0D")

    SetChrPos(0xFE, -24950, 0, 8900, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -10800, 0, 1900)
    OP_9F(0x1, 4150, 0, -2750)
    OP_9F(0x1, 10500, 0, 5450)
    OP_9F(0x1, 22600, 0, 11200)
    OP_9F(0x1, 38350, 0, 11900)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_21_6C0D end

    def Function_22_6C72(): pass

    label("Function_22_6C72")

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
        "#00007F#5PRandy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#6PAfter him!\x02",
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
            "The Burst Gauge has been\x01",
            "deactivated.\x02",
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
            "※When the story of each chapter has\x01",
            "progressed to a certain point, the Burst\x01",
            "function may no longer be available.\x02\x03",
            "※However, during other critical parts of the\x01",
            "story, the Burst function will return.\x02\x03",
            "※When that happens, the Burst Gauge will\x01",
            "appear on the upper right of the screen once\x01",
            "again, so be sure to take notice of it.\x02",
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

    # Function_22_6C72 end

    def Function_23_70D2(): pass

    label("Function_23_70D2")

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

    # Function_23_70D2 end

    def Function_24_716F(): pass

    label("Function_24_716F")


    def lambda_7174():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7174)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_24_716F end

    def Function_25_71A6(): pass

    label("Function_25_71A6")

    Sleep(300)
    OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    OP_9B(0x1, 0xFE, 0x162, 0x5DC0, 0x1388, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_25_71A6 end

    def Function_26_71D3(): pass

    label("Function_26_71D3")

    Sleep(200)

    def lambda_71DB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_71DB)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x5DC, 0x0)
    OP_9B(0x1, 0xFE, 0x2D, 0xABE, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_26_71D3 end

    def Function_27_720D(): pass

    label("Function_27_720D")

    TurnDirection(0xFE, 0x104, 500)
    OP_9B(0x1, 0xFE, 0x0, 0x6978, 0x1770, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_27_720D end

    def Function_28_722F(): pass

    label("Function_28_722F")

    Sleep(800)

    def lambda_7237():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7237)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x5DC, 0x0)
    OP_9B(0x1, 0xFE, 0x159, 0x190, 0x7D0, 0x1)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_28_722F end

    def Function_29_7269(): pass

    label("Function_29_7269")

    Sleep(100)
    OP_93(0xFE, 0x7D, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    TurnDirection(0xFE, 0x104, 500)
    OP_9B(0x1, 0xFE, 0x0, 0x5DC0, 0x1388, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_29_7269 end

    def Function_30_72A4(): pass

    label("Function_30_72A4")

    Sleep(100)

    def lambda_72AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_72AC)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    OP_9B(0x1, 0xFE, 0x1E, 0x1F4, 0x7D0, 0x1)
    TurnDirection(0xFE, 0x104, 500)
    Sleep(100)
    OP_9B(0x1, 0xFE, 0x0, 0x6978, 0x1388, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_30_72A4 end

    def Function_31_72FB(): pass

    label("Function_31_72FB")

    Sleep(500)

    def lambda_7303():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7303)
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

    # Function_31_72FB end

    def Function_32_73A1(): pass

    label("Function_32_73A1")

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
            "#12P#00101F...We've gotten a good idea of\x01",
            "Randy's actions between yesterday\x01",
            "evening and this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FYeah, let's try piecing\x01",
            "it together.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_755D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_787E")
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
            "#1KWhere did Randy go\x01",
            "first?\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7618")
    ClearScenarioFlags(0x0, 0)

    label("loc_7618")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76B1")
    ClearScenarioFlags(0x0, 0)

    label("loc_76B1")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7753")
    ClearScenarioFlags(0x0, 0)

    label("loc_7753")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77E4")

    ChrTalk(
        0x101,
        (
            "#5P#00003F(No... This can't be the\x01",
            "order.)\x02\x03",
            "#00001F(I'll try sorting them\x01",
            "out again.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77DF")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_77DF")

    Jump("loc_7879")

    label("loc_77E4")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_77F4"),
        (SWITCH_DEFAULT, "loc_7841"),
    )


    label("loc_77F4")

    OP_2C(0xAA, 0x1)

    ChrTalk(
        0x101,
        (
            "#5P#00000F(There's no mistake.\x01",
            "This is definitely the\x01",
            "order.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7879")

    label("loc_7841")


    ChrTalk(
        0x101,
        (
            "#5P#00003F(...This is the most\x01",
            "likely order.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7879")

    label("loc_7879")

    Jump("loc_755D")

    label("loc_787E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Between 3 and 4AM Barca, between\x01",
            "5 and 6 Guillaume Factory, and\x01",
            "around 6 Neinvalli.\x07\x00\x02",
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
            "#5P#00006F─He most likely first went\x01",
            "to Owner Drake to pick up\x01",
            "the trunk he left with him.\x02\x03",
            "#00008FIt's contents... Randy's\x01",
            "special weapon from when he\x01",
            "was a jaeger.\x02\x03",
            "#00001FIt's most likely a kind of\x01",
            "high-power orbal rifle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FOrbal rifles are normally transported\x01",
            "disassembled.\x02\x03",
            "#00201FBecause it hasn't been used in two\x01",
            "years, Randy brought it to the\x01",
            "maintenance workshop to be serviced...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F#11P─Yeah. No doubt about it.\x02\x03",
            "#10108FHaving a well-maintained\x01",
            "weapon is a matter of life\x01",
            "and death on a battlefield.\x02\x03",
            "#10101FRandy would definitely have\x01",
            "it checked carefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FFinally, he stopped by the\x01",
            "Exchange Shop to stock up.\x02\x03",
            "#10301FHe bought gunpowder ammo\x01",
            "too. That means he has quite\x01",
            "the special rifle, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FI've heard the Reinford Company has\x01",
            "models that can change between orbal\x01",
            "and gunpowder operation but...\x02\x03",
            "#00101FRegardless, it probably has a number\x01",
            "of special improvements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FYeah. The Red Constellation\x01",
            "jaegers were using huge rifles\x01",
            "I'd never seen before as well.\x02\x03",
            "#00013F─Alright, I think we've gotten\x01",
            "a handle on Randy's situation,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FIt was past 6AM when\x01",
            "Randy left the exchange\x01",
            "shop...\x02\x03",
            "#00208FIt's around 10 AM now,\x01",
            "so around 4 hours have\x01",
            "passed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#11PIt seems difficult to\x01",
            "track him now, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003F...No. Even if it's Randy,\x01",
            "his toughness has a limit.\x02\x03",
            "#00001FAnd if he's going up\x01",
            "against Red Constellation,\x01",
            "he'd rest before doing so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FOn top of that, he's planning on using the\x01",
            "terrain to his advantage, attacking\x01",
            "suddenly and finishing it once and for all.\x02\x03",
            "#10302FWell, if he's not planning on a suicide\x01",
            "attack, that's how he'd do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FIn any case, we don't\x01",
            "have much time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00013FYeah. Without evidence,\x01",
            "we have no choice but to\x01",
            "go towards Mainz─\x02",
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

    def lambda_8083():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8083)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_80A8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_80A8)
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
        "#6P#00205FIs it from Randy?\x02",
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
            "#00007F─Lloyd Bannings, Special\x01",
            "Support Section!\x02",
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
            "Hey there, Lloyd.\x02\x03",
            "Haha, it seems you\x01",
            "thought I was someone\x01",
            "else.\x02",
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
            "#00013FWhy do you have this\x01",
            "number?\x02",
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
            "Haha, I told you before.\x01",
            "I'm a huge fan of you\x01",
            "guys.\x02\x03",
            "─The Times Department\x01",
            "Store.\x02\x03",
            "If you have time, please\x01",
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
        "#6P#00201FLloyd. That was...\x02",
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
            "#5P#00003F...Cao of Heiyue.\x02\x03",
            "#00013FHe says he's waiting for us\x01",
            "on the roof of the Central\x01",
            "Square department store.\x02",
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
            "#12P#10301FAt a time like this?\x01",
            "What could he be\x01",
            "planning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FI don't know. What I do know\x01",
            "is, he wouldn't contact us\x01",
            "without a reason.\x02\x03",
            "#00001FLet's stop by before heading\x01",
            "to the mountains.\x02",
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

    # Function_32_73A1 end

    def Function_33_864A(): pass

    label("Function_33_864A")

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

    # Function_33_864A end

    def Function_34_87DF(): pass

    label("Function_34_87DF")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C5A")

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
            "#00000FOfficer Kate, thanks for\x01",
            "your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FWe'd like to help you\x01",
            "with that reckless\x01",
            "driving incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FCan you give us the\x01",
            "details?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes, I'll explain it\x01",
            "right away.\x02",
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
            "#00003FIndeed. That did seem\x01",
            "like reckless driving\x01",
            "just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FI've heard about this.\x02\x03",
            "Because they're using the\x01",
            "horn indiscriminately, noise\x01",
            "is going to be a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FWe don't know who they\x01",
            "are, but they're certainly\x01",
            "bothering people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes, this is a problem\x01",
            "the Patrol Division\x01",
            "wants to solve ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "And so, I'd like the Special\x01",
            "Support Section's help in putting\x01",
            "a stop to the reckless driver.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "So, can you do it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8CCD")

    label("loc_8C5A")


    ChrTalk(
        0x11,
        (
            "I'd like the Special Support\x01",
            "Section's help in putting a\x01",
            "stop to the reckless driver.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "So, can you do it?\x02",
    )

    CloseMessageWindow()

    label("loc_8CCD")

    Call(0, 35)
    OP_4C(0x11, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 11050, 0, 540, 225)
    EventEnd(0x5)
    Return()

    # Function_34_87DF end

    def Function_35_8CEC(): pass

    label("Function_35_8CEC")

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
            "[Cancel]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D4F")
    Call(0, 36)
    Jump("loc_8E46")

    label("loc_8D4F")


    ChrTalk(
        0x101,
        (
            "#00006FWe've very much like to help\x01",
            "but... There's another case we\x01",
            "have to deal with right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Hmm, I see. You have\x01",
            "work to do too, I\x01",
            "suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Thanks for listening. For now,\x01",
            "we'll try to deal with the\x01",
            "problem ourselves somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x130, 6)

    label("loc_8E46")

    Return()

    # Function_35_8CEC end

    def Function_36_8E47(): pass

    label("Function_36_8E47")


    ChrTalk(
        0x101,
        (
            "#00000FUnderstood. We'll do\x01",
            "everything we can to\x01",
            "help.\x02\x03",
            "#00009FHaha, you helped me so\x01",
            "much back at the police\x01",
            "academy, Officer Kate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Thanks, this is a huge\x01",
            "help!\x02",
        )
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
            "Quest [Stopping a\x01",
            "Reckless Driver]\x07\x00\x01",
            "started!\x02",
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
            "Ahem, then first, let me\x01",
            "tell you about the\x01",
            "criminals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "The reckless drivers appear\x01",
            "to be a group of three young\x01",
            "men from the Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "They were spotted in\x01",
            "Crossbell City just the\x01",
            "other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "They've been running around\x01",
            "the state from their base\x01",
            "in Waterfront Park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It looks like they've\x01",
            "recently started using a\x01",
            "Mainz Mountain Path route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FEven on the highway...?\x01",
            "That might impact bus\x01",
            "service.\x02",
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
            "#10103FIf you used your patrol cars,\x01",
            "you could have them\x01",
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
            "If we don't pursue carefully, I'm\x01",
            "sure they'll break through our\x01",
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
            "#00003FSounds tough.\x02\x03",
            "#00001FIf that were to happen,\x01",
            "surely the police would\x01",
            "bear responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "And so, I'd like you\x01",
            "guys to lend us your\x01",
            "wisdom.\x02",
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
            "#00003FFirst, the method to stop\x01",
            "that recklessly driven\x01",
            "car...\x02\x03",
            "#00000FAnd, a place where we can\x01",
            "use the method without\x01",
            "bothering the citizens.\x02",
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
            "think about the method.\x02",
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
            "Think about a method that\x01",
            "can achieve that... Do\x01",
            "you have any good ideas?\x02",
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
            "#1KHow to safely stop the recklessly driven car?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Block route with patrol cars\x01",      # 0
            "Deploy traps on the road\x01",          # 1
            "Lure into a dead end\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_981E")
    OP_2C(0x69, 0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLuring them into a dead\x01",
            "end... How about that?\x02\x03",
            "If we do that, the\x01",
            "reckless driver will have\x01",
            "no choice but to stop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B27")

    label("loc_981E")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9834"),
        (1, "loc_9962"),
        (SWITCH_DEFAULT, "loc_9A7A"),
    )


    label("loc_9834")


    ChrTalk(
        0x101,
        (
            "#00000FBlock their route with patrol\x01",
            "cars... How about that?\x02\x03",
            "If we make the cars into a\x01",
            "wall, they'll have to stop no\x01",
            "matter how reckless they are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FH-Hmm... I think that's\x01",
            "being a little too\x01",
            "overbearing.\x02\x03",
            "#10101FIf their brakes are\x01",
            "damaged, they'll collide\x01",
            "with the patrol cars.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A7A")

    label("loc_9962")


    ChrTalk(
        0x101,
        (
            "#00000FPutting traps on the\x01",
            "road... How about that?\x02\x03",
            "If we puncture their\x01",
            "tires with sharp\x01",
            "objects...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FH-Hmm... I've heard about things\x01",
            "like that, but...\x02\x03",
            "#10101FIf we were to use something like\x01",
            "that in Crossbell City, there'd\x01",
            "be a serious accident for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A7A")

    label("loc_9A7A")


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
            "reckless driver will have\x01",
            "no choice but to stop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B27")


    ChrTalk(
        0x11,
        (
            "I see... That would be a\x01",
            "safe way of stopping the\x01",
            "car!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FBut, a dead end... No\x01",
            "suitable places come to mind.\x02\x03",
            "#00100FWe won't be able to use the\x01",
            "new city hall or the IBC\x01",
            "building for obvious reasons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FHmm, that's right... I\x01",
            "thought those were good\x01",
            "ideas, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FIn that case... Why don't\x01",
            "we make one?\x02\x03",
            "#10300FWe can make a barricade\x01",
            "with sandbags like those\x01",
            "used at construction sites.\x02",
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
            "If we use those, we can\x01",
            "stop them wherever we\x01",
            "please!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHaha, things are looking\x01",
            "up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHehe, you're welcome.\x02\x03",
            "#10300FThen, the next problem\x01",
            "is where to stop them.\x02\x03",
            "Does the Patrol Division\x01",
            "have an idea as to the\x01",
            "car's route?\x02",
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
            "Ent. District>Govt. District>Water.\x01",
            "Area>East Street>Central Sq.>Back\x01",
            "Street... and then back to Ent. District.\x02",
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
            "that along the car's\x01",
            "route?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FHmm...\x02",
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A015")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A223")
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
            "#1KWhere is the appropriate place to\x01",
            "stop the recklessly driven car?\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A190")

    ChrTalk(
        0x101,
        (
            "#00000FI think the only place that\x01",
            "matches those conditions is\x01",
            "Governmental District.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A18B")
    OP_2C(0x69, 0x1)

    label("loc_A18B")

    Jump("loc_A21E")

    label("loc_A190")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00003F(...No, I think that place\x01",
            "won't work.)\x02\x03",
            "(A place with few pedestrians\x01",
            "and won't bother the\x01",
            "citizens. That place is...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A21E")

    Jump("loc_A015")

    label("loc_A223")


    ChrTalk(
        0x105,
        (
            "#10300FGovernmental District... The\x01",
            "City Meeting Hall, library\x01",
            "and police HQ are all there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIt's true there are few\x01",
            "pedestrians there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes. Even if an accident\x01",
            "does occur, I think damage\x01",
            "will be kept to a minimum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Additionally, HQ is\x01",
            "nearby. It's the perfect\x01",
            "strategy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "...Hmm, I think this is\x01",
            "going to work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Haha, that's our Special\x01",
            "Support Section! You guys came\x01",
            "up with that plan in a flash.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, we're just glad we\x01",
            "could help.\x02",
        )
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
            "in my division, and we'll begin\x01",
            "the operation right away!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Special Support Section,\x01",
            "please take care of\x01",
            "constructing the barricade!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAlright, we'll help you\x01",
            "out with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHehe, this is getting\x01",
            "interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIf we're going to do\x01",
            "this, let's give it our\x01",
            "all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes! We'll definitely\x01",
            "catch that reckless\x01",
            "driver!!\x02",
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

    # Function_36_8E47 end

    def Function_37_A602(): pass

    label("Function_37_A602")

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

    def lambda_A6FD():
        OP_95(0xFE, -8119, 1770, 11630, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A6FD)
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
        "#5P#00005FThere she is!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#00100FWe'll need to be a\x01",
            "little more careful from\x01",
            "here on.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00003FRight. Let's circle around\x01",
            "so she doesn't escape to any\x01",
            "other districts.\x02\x03",
            "#00000FElie and I will handle\x01",
            "Governmental District. Noｱl,\x01",
            "Wazy, you take Back Street.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        "#6P#10100FRoger that.\x02",
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
        "#6P#00303FGot it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#5P#04609FAhaha, a pincer attack,\x01",
            "eh?♪\x02",
        )
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

    def lambda_AA12():
        OP_95(0xFE, 13360, 0, 10870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_AA12)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_68(13490, 1950, 10070, 5000)
    MoveCamera(42, 30, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(9450, 5000)

    def lambda_AA67():
        OP_95(0xFE, 15810, 0, 11410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AA67)
    Sleep(50)

    def lambda_AA84():
        OP_95(0xFE, 15710, 0, 10230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AA84)
    WaitChrThread(0x101, 1)

    def lambda_AAA2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AAA2)
    WaitChrThread(0x102, 1)

    def lambda_AAB3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AAB3)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00000FHere Mary. Come 'ere!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FDon't worry. We'll take\x01",
            "you home.\x02",
        )
    )

    CloseMessageWindow()
    Sound(953, 0, 100, 0)

    def lambda_AB18():
        OP_95(0xFE, 9930, 0, 4040, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_AB18)
    Sleep(50)

    def lambda_AB35():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB35)
    Sleep(50)

    def lambda_AB45():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AB45)
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

    def lambda_ABBF():
        OP_95(0xFE, 7970, 0, -12520, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_ABBF)
    Sleep(50)

    def lambda_ABDC():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ABDC)
    Sleep(50)

    def lambda_ABF4():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ABF4)
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
            "#10300FHehe. Resign yourself\x01",
            "and come with us.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AC6F():
        OP_95(0xFE, 440, 0, -6930, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_AC6F)
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

    def lambda_ACF6():
        OP_95(0xFE, -28830, 0, 10230, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_ACF6)
    Sleep(50)

    def lambda_AD13():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AD13)
    Sleep(50)

    def lambda_AD2B():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_AD2B)
    OP_0D()
    WaitChrThread(0x14, 1)

    ChrTalk(
        0x1A3,
        (
            "#04602FSee? We're not going to\x01",
            "hurt you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(...Man. That part of\x01",
            "her hasn't changed a\x01",
            "bit.)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ADB0():
        OP_95(0xFE, -8119, 1770, 11630, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_ADB0)
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

    def lambda_AEAF():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AEAF)
    Sleep(50)

    def lambda_AEC7():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AEC7)
    Sleep(50)

    def lambda_AEDF():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AEDF)
    Sleep(50)

    def lambda_AEF7():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AEF7)
    Sleep(50)

    def lambda_AF0F():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AF0F)
    Sleep(50)

    def lambda_AF27():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_AF27)
    OP_63(0x14, 0x0, 1200, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    def lambda_AF51():
        OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_AF51)
    WaitChrThread(0x14, 1)
    OP_6F(0x10)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Oh a cat! How cuuute!㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt's still a kitten.\x01",
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
        "#11P#N#00011FCrap!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    EndChrThread(0x14, 0x1)
    OP_64(0x14)

    def lambda_B04D():

        label("loc_B04D")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_B04D")

    QueueWorkItem2(0x101, 1, lambda_B04D)

    def lambda_B05F():

        label("loc_B05F")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_B05F")

    QueueWorkItem2(0x104, 1, lambda_B05F)

    def lambda_B071():

        label("loc_B071")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_B071")

    QueueWorkItem2(0x102, 1, lambda_B071)

    def lambda_B083():

        label("loc_B083")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_B083")

    QueueWorkItem2(0x109, 1, lambda_B083)

    def lambda_B095():

        label("loc_B095")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_B095")

    QueueWorkItem2(0x105, 1, lambda_B095)

    def lambda_B0A7():

        label("loc_B0A7")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_B0A7")

    QueueWorkItem2(0x1A3, 1, lambda_B0A7)

    def lambda_B0B9():

        label("loc_B0B9")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_B0B9")

    QueueWorkItem2(0x8, 1, lambda_B0B9)

    def lambda_B0CB():

        label("loc_B0CB")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_B0CB")

    QueueWorkItem2(0x9, 1, lambda_B0CB)
    Sound(953, 0, 100, 0)

    def lambda_B0E3():
        OP_95(0xFE, -2110, 2660, 36590, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_B0E3)
    Sleep(1500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x1A3, 0x1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)

    def lambda_B120():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_B120)
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
        "#11P#N#00005FAh!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#11P#00105FInto Arc-en-Ciel!?\x02",
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
            "#6P#04609FYeah! She's just like a\x01",
            "rat in a trap!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0410", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_37_A602 end

    def Function_38_B2BE(): pass

    label("Function_38_B2BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B2EA")
    OP_93(0xFE, 0x0, 0x190)
    OP_93(0xFE, 0x5A, 0x190)
    OP_93(0xFE, 0xB4, 0x190)
    OP_93(0xFE, 0x10E, 0x190)
    Jump("Function_38_B2BE")

    label("loc_B2EA")

    Return()

    # Function_38_B2BE end

    def Function_39_B2EB(): pass

    label("Function_39_B2EB")

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
            "Welcome! Would you like\x01",
            "some ice cream?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, we're from\x01",
            "the Special Support\x01",
            "Section...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that you came\x01",
            "for "gourmet\x01",
            "recommendations" coverage.\x07\x00\x02",
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
            "Ah, so you're them. I\x01",
            "heard from the Crossbell\x01",
            "News people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Alright then. It's sudden, but I'd\x01",
            "like to recommend my "Sherbert\x01",
            "<Seven Colors>" right away!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FWow, looks delicious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's my new gelato that\x01",
            "brings together various\x01",
            "flavors.\x02",
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
            "#00100FAlright then. Let's try\x01",
            "it out.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others ate\x01",
            "the Sherbert <Seven\x01",
            "Colors>.\x07\x00\x02",
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
            "#10103FMmm.\x02\x03",
            "#10109F...Hmm, it's cold and\x01",
            "delicious!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        (
            "#00102FI agree. It's cute too,\x01",
            "and I feel it bursting\x01",
            "in my mouth.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        (
            "#00000FHaha, our womenfolk just\x01",
            "love stuff like this.\x02",
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
            "PeTiote? Brain freeze?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B833():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B833)

    def lambda_B840():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B840)

    def lambda_B84D():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B84D)

    def lambda_B85A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B85A)

    def lambda_B867():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B867)
    Sleep(1000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#00204FNo... Excuse me.\x02\x03",
            "#00200FIt was so shocking, I\x01",
            "lost myself for a\x01",
            "moment.\x02",
        )
    )

    CloseMessageWindow()
    Sound(822, 0, 100, 0)
    OP_63(0x103, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1500)

    ChrTalk(
        0x103,
        (
            "#00204FWith the thrill of that\x01",
            "bursting candy, its freshness\x01",
            "goes without saying...\x02\x03",
            "The seven flavors don't clash\x01",
            "and harmonize on the tongue.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        (
            "#00201F#4SThis is a gelato\x01",
            "revolution!\x02",
        )
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
            "#00206F...Sorry, I got carried\x01",
            "away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHaha... Looks like you\x01",
            "like it. We'll have you\x01",
            "introduce this one, Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FHere, I think this will\x01",
            "make a good comment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Ehehe, I'm glad you like\x01",
            "it.\x02",
        )
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_BB84")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BB84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_BBA1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BBA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_BBB4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BBB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_BBC7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BBC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_BBE4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BBE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_BBF7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BBF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_BC14")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BC14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_BC27")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BC27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_BC44")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BC44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_BC57")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BC57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_BC74")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BC74")

    OP_29(0x80, 0x1, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BD7F")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Finished covering 6\x01",
            "restaurants!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BD76")

    AnonymousTalk(
        0x101,
        (
            "#00003FIt seems we could go report to\x01",
            "Grace immediately, but...\x02\x03",
            "#00000FWe haven't found all 6\x01",
            "members' favorites yet, so why\x01",
            "don't we try a little harder?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_BD76")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_BD7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE6D")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found all SSS members'\x01",
            "favorites!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this, we found all 6\x01",
            "members' favorites.\x02\x03",
            "We've got plenty of coverage with\x01",
            "this. Let's head to the news\x01",
            "agency right away and report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_BE6D")

    OP_4C(0xC, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -10150, 1760, 22970, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_39_B2EB end

    def Function_40_BE9D(): pass

    label("Function_40_BE9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BEAB")
    Jump("loc_C2C9")

    label("loc_BEAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BEB9")
    Jump("loc_C2C9")

    label("loc_BEB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BEC7")
    Jump("loc_C2C9")

    label("loc_BEC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BED5")
    Jump("loc_C2C9")

    label("loc_BED5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BF48")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLooks like they're busy\x01",
            "rehearsing. Let's\x01",
            "refrain from entering.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_C2C9")

    label("loc_BF48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BFBB")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLooks like they're busy\x01",
            "rehearsing. Let's\x01",
            "refrain from entering.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_C2C9")

    label("loc_BFBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BFC9")
    Jump("loc_C2C9")

    label("loc_BFC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_BFD7")
    Jump("loc_C2C9")

    label("loc_BFD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C237")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C133")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C0C6")

    ChrTalk(
        0x101,
        (
            "#00000FThat's right, they said the\x01",
            "heads of state were\x01",
            "attending the theater today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWe'd be bothering them,\x01",
            "so let's pass on\x01",
            "visiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah, that sounds like a\x01",
            "good plan.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_C12E")

    label("loc_C0C6")


    ChrTalk(
        0x101,
        (
            "#00000FThey said the heads of state were\x01",
            "attending the theater today.\x01",
            "Let's refrain from entering.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C12E")

    Jump("loc_C21C")

    label("loc_C133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1D1")

    ChrTalk(
        0x101,
        (
            "#00003F...There was a lot of noise\x01",
            "just now.\x02\x03",
            "#00000FThey've got to prepare to\x01",
            "receive the heads of state.\x01",
            "Let's hold off on entering.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_C21C")

    label("loc_C1D1")


    ChrTalk(
        0x101,
        (
            "#00000FThere was a lot of noise\x01",
            "just now. Let's hold off\x01",
            "on entering.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C21C")

    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_C2C9")

    label("loc_C237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C245")
    Jump("loc_C2C9")

    label("loc_C245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C2C0")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FIt looks like Arc-en-Ciel\x01",
            "is busy preparing. Let's\x01",
            "hold off on entering.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_C2C9")

    label("loc_C2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C2C9")

    label("loc_C2C9")

    Return()

    # Function_40_BE9D end

    def Function_41_C2CA(): pass

    label("Function_41_C2CA")

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

    # Function_41_C2CA end

    SaveToFile()

Try(main)
