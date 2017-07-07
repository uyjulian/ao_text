from ScenarioHelper import *

def main():
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
        "Police",                 # 1
        "Tap",                 # 2
        "Tejo",               # 3
        "Buddy Pim",             # 4
        "Sofeille",             # 5
        "Ramanda",               # 6
        "Bunny girl",           # 7
        "tourist",                 # 8
        "tourist",                 # 9
        "Kate policing",             # 10
        "Policeman",                   # 11
        "Police car",               # 12
        "Mary",                 # 13
        "car",                     # 14
        "黒い運搬car",             # 15
        "Central square",               # 16
        "Nishi dori",                 # 17
        "Administrative district",                 # 18
        "Residential area",                 # 19
        "Entertainment district",                 # 20
        "East Street",                 # 21
        "old Town",                 # 22
        "Harbor district",                 # 23
        "IBC",                 # 24
        "Beside the station",               # 25
        "Back street",                 # 26
        "Ursula interchange",           # 27
        "East Crossbell Highway",       # 28
        "West Crossbell Highway",       # 29
        "Mainz Mountain Road",           # 30
        "Orchis Tower",         # 31
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

    PlaceName(90.5999984741211, 0.0, -111.88999938964844, 0x0000, 0x0000, "Central square")
    PlaceName(-19.209999084472656, 0.0, -104.37999725341797, 0x0000, 0x0000, "Nishi dori")
    PlaceName(135.69000244140625, 0.0, 36.7400016784668, 0x0000, 0x0000, "Administrative district")
    PlaceName(-121.08000183105469, 0.0, 20.040000915527344, 0x0000, 0x0000, "Residential area")
    PlaceName(0.8399999737739563, 0.0, 6.679999828338623, 0x0000, 0x0000, "Entertainment district")
    PlaceName(226.2899932861328, 0.0, -150.3000030517578, 0x0000, 0x0000, "East Street")
    PlaceName(285.57000732421875, 0.0, -242.14999389648438, 0x0000, 0x0000, "old Town")
    PlaceName(273.04998779296875, 0.0, -40.08000183105469, 0x0000, 0x0000, "Harbor district")
    PlaceName(229.6300048828125, 0.0, 116.9000015258789, 0x0000, 0x0000, "IBC")
    PlaceName(109.38999938964844, 0.0, -227.1199951171875, 0x0000, 0x0000, "Beside the station")
    PlaceName(30.899999618530273, 0.0, -53.439998626708984, 0x0000, 0x0000, "Back street")
    PlaceName(104.37999725341797, 0.0, -278.8900146484375, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(316.4700012207031, 0.0, -126.91999816894531, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-104.37999725341797, 0.0, -106.87999725341797, 0x0000, 0x0000, "West Crossbell Highway")
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
        "Function_8_159F",         # 08, 8
        "Function_9_176B",         # 09, 9
        "Function_10_274B",        # 0A, 10
        "Function_11_3081",        # 0B, 11
        "Function_12_39C0",        # 0C, 12
        "Function_13_4156",        # 0D, 13
        "Function_14_4C26",        # 0E, 14
        "Function_15_5525",        # 0F, 15
        "Function_16_5FD1",        # 10, 16
        "Function_17_6062",        # 11, 17
        "Function_18_6105",        # 12, 18
        "Function_19_62F8",        # 13, 19
        "Function_20_6333",        # 14, 20
        "Function_21_6510",        # 15, 21
        "Function_22_6575",        # 16, 22
        "Function_23_69AE",        # 17, 23
        "Function_24_6A4B",        # 18, 24
        "Function_25_6A82",        # 19, 25
        "Function_26_6AAF",        # 1A, 26
        "Function_27_6AE9",        # 1B, 27
        "Function_28_6B0B",        # 1C, 28
        "Function_29_6B45",        # 1D, 29
        "Function_30_6B80",        # 1E, 30
        "Function_31_6BD7",        # 1F, 31
        "Function_32_6C7D",        # 20, 32
        "Function_33_7E3E",        # 21, 33
        "Function_34_7FD3",        # 22, 34
        "Function_35_84A4",        # 23, 35
        "Function_36_85F1",        # 24, 36
        "Function_37_9C50",        # 25, 37
        "Function_38_A937",        # 26, 38
        "Function_39_A964",        # 27, 39
        "Function_40_B4F9",        # 28, 40
        "Function_41_B8D4",        # 29, 41
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1523")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Oh, Lloyd's guys …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was listening to rumors,\x01",
            "The mission support department also restarts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, new members\x01",
            "Thank you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FEven so, Mr. Kate\x01",
            "Entertainment districtでお仕事というのも\x01",
            "Is not it rare?\x02\x03",
            "#00100FいつもはCentral squareにいる\x01",
            "It was an image ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, actually\x01",
            "目を付けている導力carがあって\x01",
            "I'm sticking here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well anyway,\x01",
            "To your success\x01",
            "I expect more and more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on,\x01",
            "Let's get better and try hard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 4)
    Jump("loc_159B")

    label("loc_1523")


    ChrTalk(
        0xFE,
        (
            "ふふ、I was listening to rumors,\x01",
            "The mission support department also restarts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on,\x01",
            "Let's get better and try hard!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_159B")

    TalkEnd(0xFE)
    Return()

    # Function_7_12B7 end

    def Function_8_159F(): pass

    label("Function_8_159F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1641")

    ChrTalk(
        0xFE,
        (
            "Even terrorists,\x01",
            "Trends of \"red constellation\" and \"black moon\"\x01",
            "It is creepy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who is trying to get things working?\x01",
            "I can not take my eyes off every move.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1767")

    label("loc_1641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_16CB")

    ChrTalk(
        0xFE,
        (
            "The unveiling ceremony ended successfully,\x01",
            "Vigilance has only just begun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Three days from today, concentrate\x01",
            "I have to try not to cut it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1767")

    label("loc_16CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1767")

    ChrTalk(
        0xFE,
        (
            "Before and after the Trade Council,\x01",
            "Alcan Shell has a general performance\x01",
            "I am supposed to refrain from it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to this, we can also go in and out of this square\x01",
            "It seems to be somewhat calm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1767")

    TalkEnd(0xFE)
    Return()

    # Function_8_159F end

    def Function_9_176B(): pass

    label("Function_9_176B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17A2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17A2")
    Call(0, 39)
    Return()

    label("loc_17A2")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2747")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_180D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_180D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_182D")
    OP_AF(0x7E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2742")

    label("loc_182D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1841")
    Jump("loc_2742")

    label("loc_1841")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2742")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_18BF")

    ChrTalk(
        0xC,
        "Well, I'm glad that you are pleased.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We will continue our shop\x01",
            "I'd like to ask your favorite.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2742")

    label("loc_18BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1928")

    ChrTalk(
        0xC,
        "It really is a terrible noise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I feel something hot and ice cream\x01",
            "I feel that it will melt.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2742")

    label("loc_1928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E3")

    ChrTalk(
        0xC,
        "Iria … … I am really worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Only to sell ice to me\x01",
            "I do not have the ability, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Continue to do business here,\x01",
            "I will wait for Mr. Iria to return.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A38")

    label("loc_19E3")


    ChrTalk(
        0xC,
        "Ice ~, how about ice cream?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Cool and refreshing,\x01",
            "It is very tasty ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A38")

    Jump("loc_2742")

    label("loc_1A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1B89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AEC")

    ChrTalk(
        0xC,
        (
            "Welcome~!\x01",
            "How about ice creams! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I waited for it tonight.\x01",
            "It is the release date of the renewal performance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Let's all go exciting!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B84")

    label("loc_1AEC")


    ChrTalk(
        0xC,
        (
            "If Mainz is okay ……\x01",
            "The guards people\x01",
            "It is supposed to do something!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Anyway, as always,\x01",
            "Support the alkane shell\x01",
            "Just sell ice! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B84")

    Jump("loc_2742")

    label("loc_1B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1B97")
    Jump("loc_2742")

    label("loc_1B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1CB1")

    ChrTalk(
        0xC,
        "Ice ~, how about ice cream?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Have the customers ate lunch?\x01",
            "Ice after eating is exquisite.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CAC")

    ChrTalk(
        0x101,
        (
            "#00008F(The gourmet guide coverage here\x01",
            "It looks like it could be done … …)\x02\x03",
            "#00003F(It is not right now.\x01",
            "Let's not forget to come later. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CAC")

    Jump("loc_2742")

    label("loc_1CB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1D51")

    ChrTalk(
        0xC,
        (
            "Renewal stage of alkane shell,\x01",
            "It is finally the day after tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The number of customers will also increase.\x01",
            "Hehuu, it seems to be troubled by too much prosperity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2742")

    label("loc_1D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1E83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E00")

    ChrTalk(
        0xC,
        "Ice ~, how about ice cream?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you worry about which to do,\x01",
            "Tasting is also okay, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "With this special mini spoon\x01",
            "Alright.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E7E")

    label("loc_1E00")


    ChrTalk(
        0xC,
        (
            "Ice's tasting service was popular\x01",
            "The sales are good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Of course, this month's stall MVP\x01",
            "I got it, ☆ Viva ☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E7E")

    Jump("loc_2742")

    label("loc_1E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1F9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F22")

    ChrTalk(
        0xC,
        (
            "Alcane shell, soon\x01",
            "I'm going to take a day off ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, it's a crisis of sales decline.\x01",
            "I have to manage somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F96")

    label("loc_1F22")


    ChrTalk(
        0xC,
        (
            "Well, at this level of crisis\x01",
            "You surrendered the top\x01",
            "It is a renowned stall MVP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I have to manage somehow.\x02",
    )

    CloseMessageWindow()

    label("loc_1F96")

    Jump("loc_2742")

    label("loc_1F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_245E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2047")

    ChrTalk(
        0xFE,
        (
            "If you are a redhead customer just now,\x01",
            "Residential areaの方に行っちゃいましたよー。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm deciding on a suit suit,\x01",
            "It was kind of a strange person.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2459")

    label("loc_2047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22C9")

    ChrTalk(
        0xFE,
        (
            "As of now, bright redheaded older brother\x01",
            "\"Please make 10 tiers of ice cream\"\x01",
            "I got ordered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I ordered ice of such height,\x01",
            "Eat at a stroke without knocking down\x01",
            "It is the first time for customers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm deciding on a suit suit,\x01",
            "It was kind of a strange person.\x02",
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
            "#10106F(B, Lloyd.\x01",
            "After all this is that person … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FLet me see……\x01",
            "Which is the man?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While holding the head in the coldness of ice,\x01",
            "Residential areaの方に行っちゃいましたよー。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Alright ……\x01",
            "Let's chase this way. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1C7, 2)
    Jump("loc_2459")

    label("loc_22C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23DA")

    ChrTalk(
        0xC,
        "Wow, it was a terrible fun in the morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In this area everyone at VIP\x01",
            "Because it is not a wake going through,\x01",
            "The pedestrian was as it was ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "After the unveiling ceremony is over\x01",
            "People are flowing at once in a while\x01",
            "It was a thriving prosperity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Fufu, this is\x01",
            "It is the ability of MVP for 3 consecutive months stalls.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2459")

    label("loc_23DA")


    ChrTalk(
        0xC,
        (
            "Thanks to you, today as early as\x01",
            "It seems to be sold out ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That's why,\x01",
            "Without regret by customers\x01",
            "Please buy it now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2459")

    Jump("loc_2742")

    label("loc_245E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_25F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_256F")

    ChrTalk(
        0xC,
        (
            "Sorbet based on milk series,\x01",
            "Which customers are you\x01",
            "Do you like ice cream?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By the way, Mr. Ilya\x01",
            "Sherbet type, Mr. Preiel is a milk type\x01",
            "I will often buy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Also, Mr. Lisha\x01",
            "Just like Iria\x01",
            "Are there many sherbets?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25F2")

    label("loc_256F")


    ChrTalk(
        0xC,
        (
            "In addition,\x01",
            "Eugene is a milk-based,\x01",
            "Mr. Theodore ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "…… Sweet things are so cool\x01",
            "I do not buy it ~!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25F2")

    Jump("loc_2742")

    label("loc_25F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2605")
    Jump("loc_2742")

    label("loc_2605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2742")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26B9")

    ChrTalk(
        0xC,
        "Ice ~, how about ice cream?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My ice cream\x01",
            "I am rich in variety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Pass many times,\x01",
            "Please make sure your favorite flavor\x01",
            "Please search.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2742")

    label("loc_26B9")


    ChrTalk(
        0xC,
        (
            "By the way,\x01",
            "You can also blend freely\x01",
            "I can do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even if you ignore the advice and become masu,\x01",
            "I can not take responsibility.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2742")

    Jump("loc_17AF")

    label("loc_2747")

    TalkEnd(0xFE)
    Return()

    # Function_9_176B end

    def Function_10_274B(): pass

    label("Function_10_274B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_27CE")

    ChrTalk(
        0xFE,
        (
            "No, no … what …\x01",
            "It is becoming ridiculous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, only troubleshooting\x01",
            "I want a cabbage, MON.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307D")

    label("loc_27CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_285A")

    ChrTalk(
        0xFE,
        (
            "Hello, hey, you\x01",
            "Would you like to drink it at our store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By doing charity service,\x01",
            "I will learn quite a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307D")

    label("loc_285A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_28F1")

    ChrTalk(
        0xFE,
        (
            "Something, recently\x01",
            "Something noisy happens often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ほ〜んと、これじゃBack streetで\x01",
            "Even a taming as it is happening\x01",
            "It will look cute.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307D")

    label("loc_28F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_28FF")
    Jump("loc_307D")

    label("loc_28FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_29F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2997")

    ChrTalk(
        0xFE,
        (
            "Oh, somewhere\x01",
            "It seems to be good for the swing\x01",
            "I do not have a duck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, hehehe,\x01",
            "I could not believe my heart's voice leaked out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_29EC")

    label("loc_2997")


    ChrTalk(
        0xFE,
        (
            "Heck Hether,\x01",
            "I could not believe my heart's voice leaked out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I feel loose evidence.\x02",
    )

    CloseMessageWindow()

    label("loc_29EC")

    Jump("loc_307D")

    label("loc_29F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2A58")

    ChrTalk(
        0xFE,
        (
            "Well, good luck with today.\x01",
            "Do you work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Tell them to the world of dreams.\x02",
    )

    CloseMessageWindow()
    Jump("loc_307D")

    label("loc_2A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2BC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B4F")

    ChrTalk(
        0xFE,
        (
            "Well, Alcan Shell too\x01",
            "I am blessed with a fresh rookie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next time I will debut with a new princess role\x01",
            "Did you shri - chan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That Lisa-chan came out\x01",
            "Even though it has not been a year yet.\x01",
            "I really want you to share it with me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BC1")

    label("loc_2B4F")


    ChrTalk(
        0xFE,
        (
            "even if,\x01",
            "The artists of alkane shell\x01",
            "Kawaiko is the only one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I really want you to share it with me.\x02",
    )

    CloseMessageWindow()

    label("loc_2BC1")

    Jump("loc_307D")

    label("loc_2BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2C72")

    ChrTalk(
        0xFE,
        (
            "Even if it is a trade meeting,\x01",
            "To Mong that seems like a chef\x01",
            "There is nothing interesting in anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently it will be a grand prix\x01",
            "Members of the lawmakers also decreased,\x01",
            "The business is expensive.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307D")

    label("loc_2C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2CF2")

    ChrTalk(
        0xFE,
        (
            "Today there are many passengers,\x01",
            "市民ばっかでtouristは少ないねー。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean,\x01",
            "I miss the founding memorial festival as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307D")

    label("loc_2CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2D68")

    ChrTalk(
        0xFE,
        (
            "Oh, the police people\x01",
            "I'm getting my eyes on my eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is not so much\x01",
            "It is aggressive, it looks like it can not be done.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307D")

    label("loc_2D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2D76")
    Jump("loc_307D")

    label("loc_2D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_307D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3011")

    ChrTalk(
        0xFE,
        (
            "Heck Hether,\x01",
            "If you do not have time\x01",
            "Would you like to drink at our store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For 4 people together at group discount\x01",
            "Will you let me service you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FOh, how much is that?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E54")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_2E54")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E77")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_2E77")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E9A")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_2E9A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EBA")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_2EBA")

    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "That's right, always\x01",
            "A place of 500 Mira per person ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)

    ChrTalk(
        0x109,
        "#10101FWow, you are …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FUm, because we are at work\x01",
            "A bit of that … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What?\x01",
            "Oh, was it a frenzy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, I will …\x01",
            "I wonder if you do not disturb business.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FSorry, something ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 2)
    Jump("loc_307D")

    label("loc_3011")


    ChrTalk(
        0xFE,
        (
            "Oh, if you are afraid\x01",
            "Please hold back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Too much persistent,\x01",
            "Older brother may get angry?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_307D")

    TalkEnd(0xFE)
    Return()

    # Function_10_274B end

    def Function_11_3081(): pass

    label("Function_11_3081")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3116")

    ChrTalk(
        0xFE,
        (
            "Irier-sama injured\x01",
            "It is certainly the work of the empire that we owe ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So … … Empire can not forgive ………!\x01",
            "Does not it fell underfill! It is!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39BC")

    label("loc_3116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_31C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3184")

    ChrTalk(
        0xFE,
        "…………………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Iria-sama ………\x01",
            "Why is this ………\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_31C1")

    label("loc_3184")


    ChrTalk(
        0xFE,
        (
            "The culprit Yatsura … I can not forgive … …\x01",
            "…… Absolutely unforgivable ………!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31C1")

    Jump("loc_39BC")

    label("loc_31C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3265")

    ChrTalk(
        0xFE,
        (
            "Finally … Finally this evening,\x01",
            "The renewal performance is open to the public … …! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lee A-sama ~ ~!\x01",
            "Policeはここで舞台の成功を\x01",
            "I prayed! It is!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39BC")

    label("loc_3265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_336E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_330F")

    ChrTalk(
        0xFE,
        (
            "Tomorrow … … tomorrow,\x01",
            "Finally tomorrow, at last it will be tomorrow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ilia-sama, unfortunately\x01",
            "I can not watch it on the first day … …\x01",
            "Policeは今夜眠れそうにありませんっ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3369")

    label("loc_330F")


    ChrTalk(
        0xFE,
        (
            "Ilia-sama, unfortunately\x01",
            "I can not watch it on the first day … …\x01",
            "Policeは今夜眠れそうにありませんっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3369")

    Jump("loc_39BC")

    label("loc_336E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_33C4")

    ChrTalk(
        0xFE,
        "Ilia-sama, Iria-sama! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please do your best at practice! It is!\x02",
    )

    CloseMessageWindow()
    Jump("loc_39BC")

    label("loc_33C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_34F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_347C")

    ChrTalk(
        0xFE,
        (
            "day after tomorrow……\x01",
            "At last it is the day after tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Iria and Shri-chan\x01",
            "I wonder how they get involved ……! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Juuuri … … ふ ふ ふ … …\x01",
            "I just can not imagine it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_34F2")

    label("loc_347C")


    ChrTalk(
        0xFE,
        (
            "Iria and Shri-chan\x01",
            "I wonder how they get involved ……! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Juuuri … … ふ ふ ふ … …\x01",
            "I just can not imagine it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34F2")

    Jump("loc_39BC")

    label("loc_34F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3565")

    ChrTalk(
        0xFE,
        (
            "Well, tomorrow ……\x01",
            "At last it will be tomorrow at a later date.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Release date of renewal performance ……\x01",
            "I wait too long! It is!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39BC")

    label("loc_3565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_36BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3641")

    ChrTalk(
        0xFE,
        (
            "Even though the performance is closed, Ilia says\x01",
            "It should come to the theater for practice …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In other words, this is iris-sama\x01",
            "Opportunity to take more pictures … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So while I am on holiday\x01",
            "I will keep going to the alkane shell!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_36B7")

    label("loc_3641")


    ChrTalk(
        0xFE,
        (
            "Ilia says for practice\x01",
            "I am supposed to come to the theater from now on …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So while I am on holiday\x01",
            "I will keep going to the alkane shell!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36B7")

    Jump("loc_39BC")

    label("loc_36BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3742")

    ChrTalk(
        0xFE,
        (
            "Today evening, the leaders\x01",
            "I heard that you will see an alkane shell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uoo …… Sullen ~ I!\x01",
            "Even I want you to invite me! It is!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39BC")

    label("loc_3742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_38E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_382F")

    ChrTalk(
        0xFE,
        "#4SMuy … …! It is!#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tickets for renewal performance,\x01",
            "Competition rate for the first day of public release\x01",
            "I was too expensive to get it! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Finally I got it\x01",
            "B seat one week after release ……\x01",
            "I'm happy ……… but I regret! It is!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38E3")

    label("loc_382F")


    ChrTalk(
        0xFE,
        (
            "Tickets for renewal performance,\x01",
            "Competition rate for the first day of public release\x01",
            "I was too expensive to get it! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Finally I got it\x01",
            "B seat one week after release ……\x01",
            "I'm happy ……… but I regret! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38E3")

    Jump("loc_39BC")

    label("loc_38E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_393A")

    ChrTalk(
        0xFE,
        "Lee · A · sama ~!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Policeは雨なんかに負けませんからー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_39BC")

    label("loc_393A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_39BC")

    ChrTalk(
        0xFE,
        (
            "Recently, Iria-sama\x01",
            "I am with a rookie girl\x01",
            "I see a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uu, what what, that child … ….\x01",
            "What is it all about like Iya?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39BC")

    TalkEnd(0xFE)
    Return()

    # Function_11_3081 end

    def Function_12_39C0(): pass

    label("Function_12_39C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3A26")

    ChrTalk(
        0xFE,
        (
            "Uooh ……\x01",
            "You said well, President!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We are now free now! It is!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3A90")

    ChrTalk(
        0xFE,
        (
            "Iria-sama ……\x01",
            "I do not wake up yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn it,\x01",
            "Seriously I do not understand well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3B37")

    ChrTalk(
        0xFE,
        (
            "Okay, today is the day\x01",
            "Would you let me send you a Yale!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#4SEveryone in the alkane shell!\x01",
            "We fans always\x01",
            "I'm watching you guys ~! It is!#3S\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3BCD")

    ChrTalk(
        0xFE,
        (
            "Hello, surely inside this time\x01",
            "I guess he's doing rehearsals as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#4SAlcane shell, Banza ~ a!\x01",
            "Renewal performance, Banza ~ a! It is!#3S\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3C55")

    ChrTalk(
        0xFE,
        (
            "Iliya, Lisha,\x01",
            "Shri-chan, and\x01",
            "Ms. Celeine …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#4SEveryone, I love everyone!#3S\x02",
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3C55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3C9C")

    ChrTalk(
        0xFE,
        (
            "おいPolice、よだれよだれ……\x01",
            "Besides, my expression is over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D38")

    ChrTalk(
        0xFE,
        (
            "To Ms. Ili, Mr. Lisha,\x01",
            "And Shri-chan plays\x01",
            "Three princesses, or …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also this time the ticket of your wish\x01",
            "I got it … ….\x01",
            "Seriously I am having too much fun!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3DEC")

    ChrTalk(
        0xFE,
        (
            "To prepare for the renewal performance,\x01",
            "The alkane shell\x01",
            "It seems that we will be on holiday soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Meanwhile, inside the theater\x01",
            "A secret stage practice ……\x01",
            "I want to see it as it may be dead!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3DEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E38")

    ChrTalk(
        0xFE,
        (
            "That's right ~ ….\x01",
            "How much are you from the leadership?\x01",
            "It is too favorable!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3EE4")

    ChrTalk(
        0xFE,
        (
            "Policeの奴、\x01",
            "Saying barely thoughts\x01",
            "I am the one who liberated the tickets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hello, is it okay?\x01",
            "Chasing friends with the same aspirations,\x01",
            "Because there is a mutual aid.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3F6F")

    ChrTalk(
        0xFE,
        (
            "Hello, this is the day\x01",
            "Differ other chase\x01",
            "It's a chance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#4SIria-sama, Leisha!\x01",
            "I love you ~ ~! It is!#3S\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4152")

    label("loc_3F6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4152")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_403D")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "Oh, you are …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A few times before to the theater\x01",
            "I saw places to go in and out,\x01",
            "It is certainly a police guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay ~, the police.\x01",
            "I'm going to enter the theater at work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4152")

    label("loc_403D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40E4")

    ChrTalk(
        0xFE,
        (
            "I also received a police school,\x01",
            "Policemanを目指すかな〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then hit the patrol\x01",
            "Every day to alkane shell … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(No, that is no good.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4152")

    label("loc_40E4")


    ChrTalk(
        0xFE,
        (
            "I also received a police school,\x01",
            "Policemanを目指すかな〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then hit the patrol\x01",
            "Every day to alkane shell … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4152")

    TalkEnd(0xFE)
    Return()

    # Function_12_39C0 end

    def Function_13_4156(): pass

    label("Function_13_4156")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4215")

    ChrTalk(
        0xFE,
        (
            "There was some rumor,\x01",
            "No two major powers like that\x01",
            "I was doing sneaky things …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I fully agree with the President 's assertion.\x01",
            "I have to stand up now.\x01",
            "Just repeat the same tragedy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C22")

    label("loc_4215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_42B1")

    ChrTalk(
        0xFE,
        (
            "The stage of the alkane shell,\x01",
            "If true, watch today\x01",
            "It was a schedule ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such a thing happened.\x01",
            "There is no choice but …\x01",
            "Ilia-sama, I wonder if it's okay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C22")

    label("loc_42B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_431D")

    ChrTalk(
        0xFE,
        (
            "Main case incident ……\x01",
            "It is a terrible story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the people of the guard as soon as possible\x01",
            "I want you to do something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C22")

    label("loc_431D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_432B")
    Jump("loc_4C22")

    label("loc_432B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_439B")

    ChrTalk(
        0xFE,
        (
            "何だか、Central squareの方が\x01",
            "It sounds noisy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not really understand it,\x01",
            "I wonder if it was also an accident?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C22")

    label("loc_439B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_44C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4469")

    ChrTalk(
        0xFE,
        (
            "Renewal The release date of the stage,\x01",
            "I approached the day after tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tickets on the first day of public release to the treasures\x01",
            "I did not get it,\x01",
            "I will be going to see it next week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhufu, I feel excited.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_44C0")

    label("loc_4469")


    ChrTalk(
        0xFE,
        (
            "Renewal stage,\x01",
            "I will be going to see it next week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhufu, I feel excited.\x02",
    )

    CloseMessageWindow()

    label("loc_44C0")

    Jump("loc_4C22")

    label("loc_44C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_462C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45F5")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        (
            "Oh, you crazy.\x01",
            "Thank you very much for this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehu, thanks.\x01",
            "I could spend a temporary dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHuh, this is it.\x01",
            "I am glad that you said so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Waji's guy ……\x01",
            "Before getting in touch\x01",
            "I am working as a host. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4627")

    label("loc_45F5")

    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        (
            "Huhu, you fucker.\x01",
            "I will go play again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4627")

    Jump("loc_4C22")

    label("loc_462C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4760")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46FD")

    ChrTalk(
        0xFE,
        (
            "Suddenly I thought,\x01",
            "Former Chairman Hartmann\x01",
            "I am in a detention center right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There was a person who was as big as that\x01",
            "Even for the topic of the public\x01",
            "You do not go up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "People are fine, are not you?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_475B")

    label("loc_46FD")


    ChrTalk(
        0xFE,
        (
            "Former Hartmann chairman,\x01",
            "Even the topics of the public\x01",
            "You do not go up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "People are fine, are not you?\x02",
    )

    CloseMessageWindow()

    label("loc_475B")

    Jump("loc_4C22")

    label("loc_4760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_47D6")

    ChrTalk(
        0xFE,
        (
            "Orchis Tower……\x01",
            "At last it revealed its appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, look at the building\x01",
            "Start off exciting so much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C22")

    label("loc_47D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4894")

    ChrTalk(
        0xFE,
        (
            "Exclusive club \"Neue-Bran\" … ….\x01",
            "It is rumored that we recently opened a new store\x01",
            "I definitely want to go there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, you're over there\x01",
            "It is certainly a full membership system …\x01",
            "I wonder if someone will take me there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C22")

    label("loc_4894")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_48A2")
    Jump("loc_4C22")

    label("loc_48A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4C22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B8D")
    TurnDirection(0xFE, 0x105, 0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Oh, you … … maybe\x01",
            "Are not you my host, Wazy?\x02",
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
            "In this neighborhood\x01",
            "You have a nice host\x01",
            "I heard it from a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhufu, you are a nice child as rumored.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHuh, that kind of.\x02\x03",
            "#10302FYou ought to come to the store if you like.\x01",
            "If so, I will talk slowly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhufu, you will have me go next time.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A5E")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4A5E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A84")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4A84")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AAA")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4AAA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AD0")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4AD0")

    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00106F(Well, as expected,\x01",
            "You know well the face. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(I mean,\x01",
            "Openly in business in front of us ……)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F(Altogether ……\x01",
            "Later is a strict attention. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 1)
    Jump("loc_4C22")

    label("loc_4B8D")


    ChrTalk(
        0xFE,
        (
            "この界隈にYou have a nice host\x01",
            "I heard it from a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, come on\x01",
            "I will let you go to the shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHuh, I'll be waiting.\x02",
    )

    CloseMessageWindow()

    label("loc_4C22")

    TalkEnd(0xFE)
    Return()

    # Function_13_4156 end

    def Function_14_4C26(): pass

    label("Function_14_4C26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4CA7")

    ChrTalk(
        0xFE,
        (
            "\"Crossbell independent country\"? …\x01",
            "Wow, that's not bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on,\x01",
            "It is a citizen rather than a citizen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5521")

    label("loc_4CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4DA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D76")

    ChrTalk(
        0xFE,
        (
            "Recently I finally calmed down,\x01",
            "Since that raid took place\x01",
            "I feel that the whole city is dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I think.\x01",
            "That's why I played extra than usual\x01",
            "It is said not to not activate the economy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4D9E")

    label("loc_4D76")


    ChrTalk(
        0xFE,
        "Well then, I will play today as well ~.\x02",
    )

    CloseMessageWindow()

    label("loc_4D9E")

    Jump("loc_5521")

    label("loc_4DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4EBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E48")

    ChrTalk(
        0xFE,
        (
            "Although something in Mainz is tough,\x01",
            "It can not be helped if we are in a panic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So I, as always\x01",
            "このEntertainment districtで遊び倒すつもりだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4EB6")

    label("loc_4E48")


    ChrTalk(
        0xFE,
        (
            "Oh yeah, today.\x01",
            "Renewal It is the release day of the stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hello from the first day\x01",
            "The guy who is seen is envious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EB6")

    Jump("loc_5521")

    label("loc_4EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4F3D")

    ChrTalk(
        0xFE,
        (
            "Well then, today\x01",
            "I wonder if I can enter any bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hello, this is my last day\x01",
            "It is not too bad to alone alone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5521")

    label("loc_4F3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4FD8")

    ChrTalk(
        0xFE,
        "I was slotting at the casino ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haa ~, it is useless.\x01",
            "Apparently, she seems to have been forsaken by luck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if I will go back to sleep this day.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5521")

    label("loc_4FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_505A")

    ChrTalk(
        0xFE,
        (
            "In the slot of the casino\x01",
            "I wonder if there is no winning rule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow the table goes well and the other stands out\x01",
            "I feel like it seems to be … ~ ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5521")

    label("loc_505A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_513A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50DA")

    ChrTalk(
        0xFE,
        "Well, let's play well today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today's hands are … and …\x01",
            "Okay, I do not supplement it soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5135")

    label("loc_50DA")


    ChrTalk(
        0xFE,
        "Recently, the defeat continued.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do not talk to your parents\x01",
            "I'd like to ask for money on sesame seeds.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5135")

    Jump("loc_5521")

    label("loc_513A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_51EC")

    ChrTalk(
        0xFE,
        (
            "Alkane shell,\x01",
            "At the end of the next scheduled performance\x01",
            "I'm off for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Renewal Preparing the stage\x01",
            "Although it is said that it will start in earnest,\x01",
            "I'm really looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5521")

    label("loc_51EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_52EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_529B")

    ChrTalk(
        0xFE,
        (
            "Although I could not see it close to drift,\x01",
            "I've been watching the unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Orchis Tower、すげえよなー。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hello\x01",
            "This town is truly a good economy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_52EA")

    label("loc_529B")


    ChrTalk(
        0xFE,
        "Orchis Tower、すげえよなー。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hello\x01",
            "This town is truly a good economy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52EA")

    Jump("loc_5521")

    label("loc_52EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5427")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53C2")

    ChrTalk(
        0xFE,
        (
            "Oh, somewhere else\x01",
            "Policemanがウロウロしてんな〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From a tomorrow I have a trade meeting\x01",
            "Is it starting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand the influence,\x01",
            "To be honest I am about to go around\x01",
            "It is a camben.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5422")

    label("loc_53C2")


    ChrTalk(
        0xFE,
        (
            "I, another bad thing\x01",
            "I should not be doing it though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Policemanがいると\x01",
            "Something's hard to play.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5422")

    Jump("loc_5521")

    label("loc_5427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_54AE")

    ChrTalk(
        0xFE,
        (
            "Hello, It's because it's raining.\x01",
            "I will stay in the house\x01",
            "I can not say it is a real playboy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, today as well.\x01",
            "It is supposed to be floating and standing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5521")

    label("loc_54AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5521")

    ChrTalk(
        0xFE,
        "Oh, I will beat you down today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At first somewhere casino\x01",
            "Even slots\x01",
            "I wonder if I will try even today's luck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5521")

    TalkEnd(0xFE)
    Return()

    # Function_14_4C26 end

    def Function_15_5525(): pass

    label("Function_15_5525")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_560C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55B2")

    ChrTalk(
        0xFE,
        "Hello, how come ☆ ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Casino House \"Barca\" is\x01",
            "Today too, Agave!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyone, please go playing.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5607")

    label("loc_55B2")


    ChrTalk(
        0xFE,
        (
            "Casino House \"Barca\" is\x01",
            "Today too, Agave!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyone, please go playing.\x02",
    )

    CloseMessageWindow()

    label("loc_5607")

    Jump("loc_5FCD")

    label("loc_560C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5658")

    ChrTalk(
        0xFE,
        "Hello, how come ☆ ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Can I inject cheaply at the casino?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FCD")

    label("loc_5658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_574E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56EB")

    ChrTalk(
        0xFE,
        "Hello, how come ☆ ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, finally\x01",
            "The day of the renewal performance is\x01",
            "You came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyone ought to be fine, ya ~ ~?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5749")

    label("loc_56EB")


    ChrTalk(
        0xFE,
        (
            "Uhufu, finally\x01",
            "The day of the renewal performance is\x01",
            "You came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Everyone ought to be fine, ya ~ ~?\x02",
    )

    CloseMessageWindow()

    label("loc_5749")

    Jump("loc_5FCD")

    label("loc_574E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_57A1")

    ChrTalk(
        0xFE,
        "Hello, how come ☆ ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you do not mind, please\x01",
            "Did you take shelter from rain?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FCD")

    label("loc_57A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_57F6")

    ChrTalk(
        0xFE,
        "Hello, how come ☆ ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, if it's a chip\x01",
            "You are welcome anytime ~ Erupt\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FCD")

    label("loc_57F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5851")

    ChrTalk(
        0xFE,
        "Hello, how come ☆ ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, plenty for today.\x01",
            "Serving chattering\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FCD")

    label("loc_5851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_598F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5908")

    ChrTalk(
        0xFE,
        "Hello, how come ☆ ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I always like this\x01",
            "I'm not dressed as a dress ~ ~?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ufufu, if asked by Kalesh\x01",
            "I can wear it in private, though ~\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_598A")

    label("loc_5908")


    ChrTalk(
        0xFE,
        (
            "I always like this\x01",
            "I'm not dressed as a dress ~ ~?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ufufu, if asked by Kalesh\x01",
            "I can wear it in private, though ~\x02",
        )
    )

    CloseMessageWindow()

    label("loc_598A")

    Jump("loc_5FCD")

    label("loc_598F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5A89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A24")

    ChrTalk(
        0xFE,
        "Hello, how come ☆ ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "それeven if,\x01",
            "The sun is strong today too ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this case,\x01",
            "I can make sunburn marks\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5A84")

    label("loc_5A24")


    ChrTalk(
        0xFE,
        (
            "それeven if,\x01",
            "The sun is strong today too ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this case,\x01",
            "I can make sunburn marks\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A84")

    Jump("loc_5FCD")

    label("loc_5A89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5BC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B3D")

    ChrTalk(
        0xFE,
        "Hello, how come ☆ ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today all the leaders\x01",
            "The stage of the alkane shell\x01",
            "You come to see ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, for the time being\x01",
            "I wonder if she will drop in?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5BBC")

    label("loc_5B3D")


    ChrTalk(
        0xFE,
        (
            "Today all the leaders\x01",
            "The stage of the alkane shell\x01",
            "You come to see ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, for the time being\x01",
            "I wonder if she will drop in?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BBC")

    Jump("loc_5FCD")

    label("loc_5BC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DB2")

    ChrTalk(
        0xFE,
        (
            "Oh, it is not Randy.\x01",
            "Do not give up on your face for a long time\x01",
            "What on earth were you doing ~?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FOh, bad.\x01",
            "It's for a little idle.\x02\x03",
            "#00300FWill you forgive me this time I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, forgive me nothing\x01",
            "I will not take that hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you think that it is bad\x01",
            "Please drop Mira with my place ~ ☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FYou are a good business as ever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F(What is Randy senior … ….\x01",
            "I am used to it. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Oh, well Well here for Randy\x01",
            "It seems to be like home. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 4)
    Jump("loc_5DFC")

    label("loc_5DB2")


    ChrTalk(
        0xFE,
        (
            "Randy,\x01",
            "If you think that it is bad\x01",
            "Please drop Mira with my place ~ ☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DFC")

    Jump("loc_5FCD")

    label("loc_5E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5E6F")

    ChrTalk(
        0xFE,
        "Hello, how come ☆ ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On a day like this\x01",
            "Light and fun to watch\x01",
            "It is recommended to spend time\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FCD")

    label("loc_5E6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5FCD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F28")

    ChrTalk(
        0xFE,
        "Hello, how come ☆ ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eh, a redhead man\x01",
            "Did not you come?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You, your friend ~?\x01",
            "If that person, last time\x01",
            "I just came to the shop.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5F7D")

    label("loc_5F28")


    ChrTalk(
        0xFE,
        "Hello, how come ☆ ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are a redhead man, last time\x01",
            "I just came to the shop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F7D")

    Jump("loc_5FCD")

    label("loc_5F82")


    ChrTalk(
        0xFE,
        "Hello, how come ☆ ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, today too\x01",
            "Have fun and have fun ~ spray\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FCD")

    TalkEnd(0xFE)
    Return()

    # Function_15_5525 end

    def Function_16_5FD1(): pass

    label("Function_16_5FD1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "This is famous\x01",
            "\"Alcane shell\" … …\x01",
            "Huhu, I finally came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also tickets in advance\x01",
            "I got it,\x01",
            "I only have to wait for the performance.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_5FD1 end

    def Function_17_6062(): pass

    label("Function_17_6062")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Call of the highest masterpiece high,\x01",
            "\"Golden sun, the moon of silver\"?\x01",
            "It can not be helped and can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But just before the play begins\x01",
            "It seems they are not opening.\x01",
            "Where will I kill time?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_6062 end

    def Function_18_6105(): pass

    label("Function_18_6105")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_627A")
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

    def lambda_6230():
        OP_96(0xFE, 0xFFFFE0D4, 0x0, 0xE88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6230)
    EndChrThread(0xA, 0xFF)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0xA, 14040, 0, 11290, 90)

    def lambda_6265():
        OP_95(0xFE, 37920, 0, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6265)

    label("loc_627A")

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

    # Function_18_6105 end

    def Function_19_62F8(): pass

    label("Function_19_62F8")

    SetChrPos(0xFE, 13050, 0, -18750, 225)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -8000, 0, -600)
    OP_9F(0x1, -24250, 0, 8350)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_19_62F8 end

    def Function_20_6333(): pass

    label("Function_20_6333")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_648E")
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

    def lambda_645E():
        OP_96(0xFE, 0x3F15, 0x0, 0xFFFFAF42, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_645E)
    EndChrThread(0xA, 0xFF)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0xA, -3100, 1760, 9570, 180)

    label("loc_648E")

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

    # Function_20_6333 end

    def Function_21_6510(): pass

    label("Function_21_6510")

    SetChrPos(0xFE, -24950, 0, 8900, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -10800, 0, 1900)
    OP_9F(0x1, 4150, 0, -2750)
    OP_9F(0x1, 10500, 0, 5450)
    OP_9F(0x1, 22600, 0, 11200)
    OP_9F(0x1, 38350, 0, 11900)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_21_6510 end

    def Function_22_6575(): pass

    label("Function_22_6575")

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
        "#00311F#5P………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 0, 0, 25)
    BeginChrThread(0x101, 0, 0, 26)
    BeginChrThread(0x102, 0, 0, 28)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x101,
        "#00007F#5PRandy …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#6PLet's chase!\x02",
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
            "Burst gauge has been lifted.\x02",
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
            "* When the story of each chapter passes past the fantasy\x01",
            "Once burst can not be used.\x02\x03",
            "※ However, the story of the next chapter will be on the brink of\x01",
            "When it comes, it will be able to be used again.\x02\x03",
            "* In that case, when entering the first battle,\x01",
            "Burst gauge at the upper right of the battle screen\x01",
            "It will appear again, so please be careful.\x02",
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

    # Function_22_6575 end

    def Function_23_69AE(): pass

    label("Function_23_69AE")

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

    # Function_23_69AE end

    def Function_24_6A4B(): pass

    label("Function_24_6A4B")


    def lambda_6A50():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6A50)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_24_6A4B end

    def Function_25_6A82(): pass

    label("Function_25_6A82")

    Sleep(300)
    OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    OP_9B(0x1, 0xFE, 0x162, 0x5DC0, 0x1388, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_25_6A82 end

    def Function_26_6AAF(): pass

    label("Function_26_6AAF")

    Sleep(200)

    def lambda_6AB7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6AB7)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x5DC, 0x0)
    OP_9B(0x1, 0xFE, 0x2D, 0xABE, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_26_6AAF end

    def Function_27_6AE9(): pass

    label("Function_27_6AE9")

    TurnDirection(0xFE, 0x104, 500)
    OP_9B(0x1, 0xFE, 0x0, 0x6978, 0x1770, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_27_6AE9 end

    def Function_28_6B0B(): pass

    label("Function_28_6B0B")

    Sleep(800)

    def lambda_6B13():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6B13)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x5DC, 0x0)
    OP_9B(0x1, 0xFE, 0x159, 0x190, 0x7D0, 0x1)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_28_6B0B end

    def Function_29_6B45(): pass

    label("Function_29_6B45")

    Sleep(100)
    OP_93(0xFE, 0x7D, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    TurnDirection(0xFE, 0x104, 500)
    OP_9B(0x1, 0xFE, 0x0, 0x5DC0, 0x1388, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_29_6B45 end

    def Function_30_6B80(): pass

    label("Function_30_6B80")

    Sleep(100)

    def lambda_6B88():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6B88)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    OP_9B(0x1, 0xFE, 0x1E, 0x1F4, 0x7D0, 0x1)
    TurnDirection(0xFE, 0x104, 500)
    Sleep(100)
    OP_9B(0x1, 0xFE, 0x0, 0x6978, 0x1388, 0x0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_30_6B80 end

    def Function_31_6BD7(): pass

    label("Function_31_6BD7")

    Sleep(500)

    def lambda_6BDF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6BDF)
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

    # Function_31_6BD7 end

    def Function_32_6C7D(): pass

    label("Function_32_6C7D")

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
            "#12P#00101F… from last night to this morning\x01",
            "Randy 's movements came into view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00003FOh, let's lightly organize.\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_6E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70FF")
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
            "#1KWas Randy first visited?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Exchange shop \"Ninevali\"\x01",      # 0
            "Repair shop \"Guillaume Studio\"\x01",      # 1
            "Casino Bar \"Barca\"\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6EC4")
    ClearScenarioFlags(0x0, 0)

    label("loc_6EC4")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThen Randy visited?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Exchange shop \"Ninevali\"\x01",      # 0
            "Repair shop \"Guillaume Studio\"\x01",      # 1
            "Casino Bar \"Barca\"\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F55")
    ClearScenarioFlags(0x0, 0)

    label("loc_6F55")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KLast time Randy visited?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Exchange shop \"Ninevali\"\x01",      # 0
            "Repair shop \"Guillaume Studio\"\x01",      # 1
            "Casino Bar \"Barca\"\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6FF1")
    ClearScenarioFlags(0x0, 0)

    label("loc_6FF1")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7083")

    ChrTalk(
        0x101,
        (
            "#5P#00003F(Disagreeable……\x01",
            "It should not be in this order. )\x02\x03",
            "#00001F(Let's organize it again.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_707E")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_707E")

    Jump("loc_70FA")

    label("loc_7083")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_7093"),
        (SWITCH_DEFAULT, "loc_70C9"),
    )


    label("loc_7093")

    OP_2C(0xAA, 0x1)

    ChrTalk(
        0x101,
        "#5P#00000F(No doubt, this is the order.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_70FA")

    label("loc_70C9")


    ChrTalk(
        0x101,
        "#5P#00003F(… … maybe, this is the turn.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_70FA")

    label("loc_70FA")

    Jump("loc_6E10")

    label("loc_70FF")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３時〜４時　Casino Bar \"Barca\"\x01",
            "５時〜６時　Repair shop \"Guillaume Studio\"\x01",
            "6 o'clock - change shop \"Ninevali\"\x07\x00\x02",
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
            "#5P#00006F─ ─ probably first\x01",
            "I had it with Drake owner\x01",
            "I guess I got a trunk.\x02\x03",
            "#00008FIt was in the trunk\x01",
            "Randy's hunting gifts … …\x02\x03",
            "#00001FProbably, boasts considerable offensive power\x01",
            "I guess it's a driving rifle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FUsually, such a rifle\x01",
            "You should carry it in a disassembled state.\x02\x03",
            "#00201FBecause I have not used it for about 2 years,\x01",
            "Randy declined the unit\x01",
            "I had them repair workshops ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F#11P─ ─ Yes, I think there is no mistake.\x02\x03",
            "#10108FMaintenance of arms, life and death on the battlefield\x01",
            "It is a thing to change … ….\x02\x03",
            "#10101FIf Randy-senpai, absolutely\x01",
            "It should have been carefully checked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FFinally, drop by the exchange shop\x01",
            "It seems that they purchased various things … ….\x02\x03",
            "#10301FI mean you bought gunpowder ammo\x01",
            "Is it a rather special rifle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FSome of Rheinfault\x01",
            "Switch between the power formula and the pyrotechnic formula\x01",
            "I heard there is also a lineup ……\x02\x03",
            "#00101FEither way, it's quite special\x01",
            "It will be an enhanced rifle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FOh, red constellation hunters also\x01",
            "A huge rifle that I have not seen\x01",
            "You used it.\x02\x03",
            "#00013F── Ok, by this,\x01",
            "I could grasp the situation of Randy ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FAt the end Randy says a replacement shop\x01",
            "It was 6 o'clock this morning that I visited … …\x02\x03",
            "#00208FIt's about 10 o'clock now\x01",
            "It's almost four hours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#11PFrom now on catching up to my legs is\x01",
            "It seems to be pretty difficult, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003F…… No, Randy said\x01",
            "There should be a limit no matter how much it is tough.\x02\x03",
            "#00001FIf you're on a \"red constellation\"\x01",
            "As expected it will take as much as a nap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FIn addition, utilizing the benefits of the topography\x01",
            "Tackle it at a stretch …\x02\x03",
            "#10302FWell, at the time of honorable resolution\x01",
            "I have to plan to do some special things\x01",
            "I think the area is reasonable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101F…… Anyway\x01",
            "I can not afford that much already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00013FOh, it will not work if this happens\x01",
            "Only going to Mainz direction ─\x02",
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

    def lambda_787C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_787C)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_78A1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_78A1)
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
        "#5P#00011FNo way ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00205FFrom Randy's … ….?\x02",
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
            "#00007F── Yes, the Special Affairs Support Division,\x01",
            "It is Lloyd · Bannings!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Male voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hi, Mr. Lloyd.\x02\x03",
            "…… Huh, apparently someone else\x01",
            "You seem to have made me wrong.\x02",
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
            "#00005FWell, that voice ……\x02\x03",
            "#00013F…… Why is this number?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Male voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Huh, I told you.\x01",
            "It is a fan of Lloyd's.\x02\x03",
            "── Times department store.\x02\x03",
            "If you are free,\x01",
            "Please come to the rooftop.\x07\x00\x02",
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
            "#6P#00201F…… Lloyd.\x01",
            "The current communication ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108FWell, who the hell were you?\x02",
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
            "#5P#00003F…… It is Tsao of \"Black moon\".\x02\x03",
            "#00013FCentral squareのデパートの\x01",
            "She seems to be waiting at the rooftop.\x02",
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
        "#10111F#11PWell ……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10301FAt such time …\x01",
            "What on earth are you going to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006F……I do not understand.\x01",
            "However, that man was meaningless\x01",
            "I do not think that I will contact him.\x02\x03",
            "#00001FBefore going out to the mountain path\x01",
            "Let's get close to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101FI knew.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00201FLet's hurry anyway.\x02",
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

    # Function_32_6C7D end

    def Function_33_7E3E(): pass

    label("Function_33_7E3E")

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

    # Function_33_7E3E end

    def Function_34_7FD3(): pass

    label("Function_34_7FD3")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_841B")

    ChrTalk(
        0x11,
        (
            "You came,\x01",
            "Everyone at the Special Affairs Support Division!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FKate Senpai,\x01",
            "Good morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F暴走carの件について\x01",
            "We want us to cooperate\x01",
            "I mean, but …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FBe sure to state the circumstances\x01",
            "I'd like to ask you a favor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well, then\x01",
            "I will explain it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "最近、危険運転をするcar……\x01",
            "いわゆる『暴走car』が、市内を\x01",
            "I run around freely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Sureles hitting people and things\x01",
            "It looks like he enjoys thrilling,\x01",
            "Complaints are coming from every direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FCertainly, the moment ago\x01",
            "It was quite a rough driving ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FI have heard of it.\x02\x03",
            "A horn, too\x01",
            "Because it sounds anywhere,\x01",
            "It seems that the noise is also a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FI do not know who this is,\x01",
            "There were some annoying people ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yeah, as a wide area security office\x01",
            "It is a problem I want to resolve promptly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "So, at your support department\x01",
            "あの暴走carを取り締まる\x01",
            "I wanted to help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "How can I do?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8485")

    label("loc_841B")


    ChrTalk(
        0x11,
        (
            "At your support department\x01",
            "あの暴走carを取り締まる\x01",
            "I would like to help out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "How can I do?\x02",
    )

    CloseMessageWindow()

    label("loc_8485")

    Call(0, 35)
    OP_4C(0x11, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 11050, 0, 540, 225)
    EventEnd(0x5)
    Return()

    # Function_34_7FD3 end

    def Function_35_84A4(): pass

    label("Function_35_84A4")

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
            "【undertake】\x01",      # 0
            "【quit】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_850F")
    Call(0, 36)
    Jump("loc_85F0")

    label("loc_850F")


    ChrTalk(
        0x101,
        (
            "#00006FI would like to help you\x01",
            "Yamaayama ….\x01",
            "Now there is a separate matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well, I see.\x01",
            "You have work as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Thank you for listening.\x01",
            "Tentatively, somehow\x01",
            "We will deal with it alone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x130, 6)

    label("loc_85F0")

    Return()

    # Function_35_84A4 end

    def Function_36_85F1(): pass

    label("Function_36_85F1")


    ChrTalk(
        0x101,
        (
            "#00000FI understand,\x01",
            "If you can cooperate with us\x01",
            "Please let me help as much as you can.\x02\x03",
            "#00009FHaha, to Kate Senpai\x01",
            "Since the police school days\x01",
            "I am indebted to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Thank you, I will save you!\x02",
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
            "クエスト【暴走carの取り締まり】\x07\x00",
            "I started!\x02",
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
            "Kohon, then, first of all\x01",
            "I will explain the criminals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "暴走carを運転しているのは、\x01",
            "Young people 3 people who are from the Republic … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "From this moment, in Crossbell City\x01",
            "Children who came to be witnessed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "彼らはHarbor districtの公園を拠点に\x01",
            "I run around in autonomous province.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "最近はMainz Mountain Roadなんかも\x01",
            "It seems that it is in the running route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FTo the highway ……\x01",
            "Also for bus service\x01",
            "There appears to be an impact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh, but …\x02\x03",
            "#00000FIf the driving route is broken\x01",
            "Crackdown on that\x01",
            "Is not it difficult?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105Findeed.\x02\x03",
            "#10103FPolice carを総動員すれば、\x01",
            "It is impossible to lay an encirclement network immediately\x01",
            "I think that I can do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well, that is\x01",
            "It does not work either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "If you chase it down,\x01",
            "I'm sure they are also raging\x01",
            "You will try to get through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Let me forcibly drive,\x01",
            "If raised in a traffic accident\x01",
            "I do not care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F… … It is troublesome.\x02\x03",
            "#00001FIf that happens\x01",
            "It is likely to be the responsibility of the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "So, to you\x01",
            "I want you to lend wisdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Do not bother the citizens,\x01",
            "スマートに暴走carを捕まえる……\x01",
            "Wisdom for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see……\x01",
            "I understood the circumstances as usual.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00000FAn important element is\x01",
            "I think there are two.\x02\x03",
            "#00003Fまず、走っている暴走carを\x01",
            "\"Method\" for stopping safely … …\x02\x03",
            "#00000FAnd even if you use that method\x01",
            "\"Place\" where citizens are not adversely affected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FCertainly, whichever is missing\x01",
            "安全に暴走carを取り締まることは\x01",
            "You will not be able to do it.\x02\x03",
            "#00100FWell then, first,\x01",
            "Let's think about from the \"method\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHmm, any number of ways\x01",
            "I think it can be thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FAgain, the top priority should be\x01",
            "The possibility of an accident is low,\x01",
            "Is it that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes, of course.\x01",
            "The probability of involving citizens is\x01",
            "I want to minimize it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "If so, to some extent\x01",
            "I think that the \"method\" will be narrowed down ….\x01",
            "I wonder if there are any good ideas?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FI agree……\x02",
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
            "#1K暴走carを安全に止める方法は？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Police carで進路を塞ぐ\x01",      # 0
            "Trap the road\x01",        # 1
            "Invite into a dead end\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F3D")
    OP_2C(0x69, 0x1)

    ChrTalk(
        0x101,
        (
            "#00000FInvite to the deadline …\x01",
            "How is that?\x02\x03",
            "それ以上、暴走carが\x01",
            "If it is in a state where it can not proceed,\x01",
            "You should not stop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9230")

    label("loc_8F3D")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8F53"),
        (1, "loc_9057"),
        (SWITCH_DEFAULT, "loc_9162"),
    )


    label("loc_8F53")


    ChrTalk(
        0x101,
        (
            "#00000FPolice carで進路を塞ぐ……\x01",
            "How is that?\x02\x03",
            "car両を壁にすれば、\x01",
            "いくら暴走carでも止まらざるを……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FWell, hmm … ….\x01",
            "That is a bit too overpowering\x01",
            "I think I do.\x02\x03",
            "#10101FDo not brake\x01",
            "Police carと衝突する\x01",
            "There is also possibility.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9162")

    label("loc_9057")


    ChrTalk(
        0x101,
        (
            "#00000FTrap on the road … …\x01",
            "How is that?\x02\x03",
            "With tires like a needle\x01",
            "If I let it puncture ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FWell, hmm … ….\x01",
            "It is said that there are such tools\x01",
            "I have heard of it … ….\x02\x03",
            "#10101FWhen I do it in Crosband city,\x01",
            "It seems to lead to a serious accident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9162")

    label("loc_9162")


    ChrTalk(
        0x101,
        "#00006FIs it true?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000F… … If it was, let's go to dead end\x01",
            "How about inviting?\x02\x03",
            "それ以上、暴走carが\x01",
            "If it is in a state where it can not proceed,\x01",
            "You should not stop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9230")


    ChrTalk(
        0x11,
        (
            "I see……\x01",
            "それなら安全に暴走carを\x01",
            "I think I can stop it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FBut it does not end …\x01",
            "A place where you can use it is cool\x01",
            "I do not think so.\x02\x03",
            "#00100F新市庁ビルやIBCの敷地なんかは\x01",
            "You will not be able to use it as expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWell, that's right ……\x01",
            "I thought it was a good idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHuh, if it is ……\x01",
            "Why do not you just create it?\x02\x03",
            "#10300FAs used at the construction site\x01",
            "I made barricades with sandbags.\x02",
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
        "Yeah, a good idea!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "If so, anywhere\x01",
            "I think I can make a dead end!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FHuh, it is awful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHuh, you are welcome.\x02\x03",
            "#10300FThen, the next problem is\x01",
            "It's a place to make a dead end.\x02\x03",
            "一応、暴走carのルートは\x01",
            "Are you grasping by the wide area crime prevention section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Yes, of course I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "暴走carが使っているルートは、\x01",
            "Basically cross-city\x01",
            "It seems like I have made a big round.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Entertainment district⇒Administrative district⇒Harbor district⇒\x01",
            "East Street⇒Central square⇒Back street……\x01",
            "そして再びEntertainment districtっていう具合ね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThen, in the six compartments\x01",
            "Setting a dead end somewhere,\x01",
            "It looks good to invite there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "There are relatively few people traffic,\x01",
            "It is hard for inconvenience to citizens\x01",
            "The location is desirable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "暴走carのルート上に、\x01",
            "I wonder if there was such a place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FI agree……\x02",
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98E1")
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
            "#1K暴走carを止めるのに相応しい場所は？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        180,
        0,
        (
            "Entertainment district\x01",        # 0
            "Administrative district\x01",        # 1
            "Harbor district\x01",        # 2
            "East Street\x01",        # 3
            "Central square\x01",      # 4
            "Back street\x01",        # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9830")

    ChrTalk(
        0x101,
        (
            "#00000FThat condition applies to\x01",
            "Administrative districtだけだと思います。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_982B")
    OP_2C(0x69, 0x1)

    label("loc_982B")

    Jump("loc_98DC")

    label("loc_9830")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00003F(… … no, that place is\x01",
            "You'd better stop doing it. )\x02\x03",
            "（There are relatively few people traffic,\x01",
            "Places where it is hard to inconvenience citizens.\x01",
            "Which applies to that condition … …)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98DC")

    Jump("loc_9727")

    label("loc_98E1")


    ChrTalk(
        0x105,
        (
            "#10300FAdministrative district……\x01",
            "Municipal hall and library,\x01",
            "The police headquarters is a block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FCertainly if over there\x01",
            "There are relatively few people on the street … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYeah, even if a traffic accident happens\x01",
            "It seems that damage can be minimized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "In addition, the police headquarters is close.\x01",
            "It's perfect for the strategy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "…. Yup, this is\x01",
            "I'm getting it somehow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Huhu, it is truly a special support department!\x01",
            "The strategy was decided in no time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009FI am honored to serve you, my senior.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "あとは、暴走carを行き止まりに\x01",
            "To invite,\x01",
            "何台かPolice carが要りそうね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well then, then\x01",
            "I informed everyone in the wide area crime prevention division,\x01",
            "Let's start a strategy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "To Lloyd's,\x01",
            "I asked for the preparation of the barricade!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, I will help you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FHuh, I'm getting interesting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FTo do it\x01",
            "Let's put in a spirit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100Fええ、絶対に暴走carを\x01",
            "Let's catch it! It is!\x02",
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

    # Function_36_85F1 end

    def Function_37_9C50(): pass

    label("Function_37_9C50")

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

    def lambda_9D4B():
        OP_95(0xFE, -8119, 1770, 11630, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_9D4B)
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
        "#5P#00005F… … It is!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#00100FFrom here, a bit\x01",
            "It seems better to be cautious.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00003FOh, no more in other blocks\x01",
            "Let's go around not to go.\x02\x03",
            "#00000FEri and I bypass around\x01",
            "Administrative district方面から近付くから、\x01",
            "ノエルとワジはBack street方面を。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        "#6P#10100FIt is okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302Froger that#4RYa#.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A3, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FRandy and you\x01",
            "このままResidential area方面から頼む。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A3, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        "#6P#00303F… Wow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        "#5P#04609FHaha, it's a siege battle ♪\x02",
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

    def lambda_A04B():
        OP_95(0xFE, 13360, 0, 10870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A04B)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_68(13490, 1950, 10070, 5000)
    MoveCamera(42, 30, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(9450, 5000)

    def lambda_A0A0():
        OP_95(0xFE, 15810, 0, 11410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A0A0)
    Sleep(50)

    def lambda_A0BD():
        OP_95(0xFE, 15710, 0, 10230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A0BD)
    WaitChrThread(0x101, 1)

    def lambda_A0DB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A0DB)
    WaitChrThread(0x102, 1)

    def lambda_A0EC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A0EC)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00000Fさあ、Mary。\x01",
            "come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYou do not have to worry.\x01",
            "Because we will bring it home.\x02",
        )
    )

    CloseMessageWindow()
    Sound(953, 0, 100, 0)

    def lambda_A173():
        OP_95(0xFE, 9930, 0, 4040, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A173)
    Sleep(50)

    def lambda_A190():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A190)
    Sleep(50)

    def lambda_A1A0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A1A0)
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

    def lambda_A21A():
        OP_95(0xFE, 7970, 0, -12520, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A21A)
    Sleep(50)

    def lambda_A237():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A237)
    Sleep(50)

    def lambda_A24F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A24F)
    OP_0D()
    WaitChrThread(0x14, 1)
    OP_93(0x14, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10100FMaryちゃん、怖がらないで。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHooh, Ideas\x01",
            "Will you be kind enough for me?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A2D0():
        OP_95(0xFE, 440, 0, -6930, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A2D0)
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

    def lambda_A357():
        OP_95(0xFE, -28830, 0, 10230, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A357)
    Sleep(50)

    def lambda_A374():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A374)
    Sleep(50)

    def lambda_A38C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_A38C)
    OP_0D()
    WaitChrThread(0x14, 1)

    ChrTalk(
        0x1A3,
        "#04602FHey Hey, do not do anything?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(……Geez.\x01",
            "This place has not changed. )\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A407():
        OP_95(0xFE, -8119, 1770, 11630, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A407)
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

    def lambda_A506():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A506)
    Sleep(50)

    def lambda_A51E():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A51E)
    Sleep(50)

    def lambda_A536():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A536)
    Sleep(50)

    def lambda_A54E():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A54E)
    Sleep(50)

    def lambda_A566():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A566)
    Sleep(50)

    def lambda_A57E():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_A57E)
    OP_63(0x14, 0x0, 1200, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    def lambda_A5A8():
        OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A5A8)
    WaitChrThread(0x14, 1)
    OP_6F(0x10)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Oh, it's a cat! Super cute - spray\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PMoreover, it is still a kitten.\x01",
            "Do not be healed ~.\x02",
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
        "#11P#N#00011FOops\x02",
    )

    CloseMessageWindow()
    OP_5A()
    EndChrThread(0x14, 0x1)
    OP_64(0x14)

    def lambda_A6B5():

        label("loc_A6B5")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_A6B5")

    QueueWorkItem2(0x101, 1, lambda_A6B5)

    def lambda_A6C7():

        label("loc_A6C7")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_A6C7")

    QueueWorkItem2(0x104, 1, lambda_A6C7)

    def lambda_A6D9():

        label("loc_A6D9")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_A6D9")

    QueueWorkItem2(0x102, 1, lambda_A6D9)

    def lambda_A6EB():

        label("loc_A6EB")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_A6EB")

    QueueWorkItem2(0x109, 1, lambda_A6EB)

    def lambda_A6FD():

        label("loc_A6FD")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_A6FD")

    QueueWorkItem2(0x105, 1, lambda_A6FD)

    def lambda_A70F():

        label("loc_A70F")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_A70F")

    QueueWorkItem2(0x1A3, 1, lambda_A70F)

    def lambda_A721():

        label("loc_A721")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_A721")

    QueueWorkItem2(0x8, 1, lambda_A721)

    def lambda_A733():

        label("loc_A733")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_A733")

    QueueWorkItem2(0x9, 1, lambda_A733)
    Sound(953, 0, 100, 0)

    def lambda_A74B():
        OP_95(0xFE, -2110, 2660, 36590, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A74B)
    Sleep(1500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x1A3, 0x1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)

    def lambda_A788():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_A788)
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
        "#11P#N#00005FAh……!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#11P#00105FTo alkane shell … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#11P#10106FWell, it was a terrible momentum.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FHaa … Anyway\x01",
            "We only have to get inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#6P#04609FYes.\x01",
            "It will already be a rat of a bag ♪\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0410", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_37_9C50 end

    def Function_38_A937(): pass

    label("Function_38_A937")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A963")
    OP_93(0xFE, 0x0, 0x190)
    OP_93(0xFE, 0x5A, 0x190)
    OP_93(0xFE, 0xB4, 0x190)
    OP_93(0xFE, 0x10E, 0x190)
    Jump("Function_38_A937")

    label("loc_A963")

    Return()

    # Function_38_A937 end

    def Function_39_A964(): pass

    label("Function_39_A964")

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
            "welcome.\x01",
            "How about ice cream?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse me,\x01",
            "I am a person in the mission support department … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the interview with \"One push gourmet\"\x01",
            "I explained what came.\x07\x00\x02",
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
            "Oh, did everyone do that?\x01",
            "I've heard stories from people of the telecommunications company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well then, I'm in a hurry … …\x01",
            "This is my recommended menu,\x01",
            "\"Frozen dessert≪ seven colors ≫!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FOh, quite\x01",
            "It looks delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Variegated taste attractive\x01",
            "It is a new gelato.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I can crackle into your mouth\x01",
            "Candy chips also joined,\x01",
            "You can enjoy a magical texture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWell then, let me sample it quickly\x01",
            "Let's get it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyds ate ice confections ≪seven colors≫.\x07\x00\x02",
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
            "#10103FPuff\x02\x03",
            "#10109F……Yup,\x01",
            "It is cold and tasty!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        (
            "#00102FYes, it looks cute,\x01",
            "I feel good to play in my mouth.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        (
            "#00000FThe women's team is especially\x01",
            "I heard that he likes such things.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x104,
        (
            "#00305FWhat's wrong, Tio.\x01",
            "Have you cooled down your belly?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AE9C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AE9C)

    def lambda_AEA9():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AEA9)

    def lambda_AEB6():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AEB6)

    def lambda_AEC3():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AEC3)

    def lambda_AED0():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AED0)
    Sleep(1000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#00204FNo … I'm sorry.\x02\x03",
            "#00200FFor a moment to shock a lot,\x01",
            "I have forgotten.\x02",
        )
    )

    CloseMessageWindow()
    Sound(822, 0, 100, 0)
    OP_63(0x103, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1500)

    ChrTalk(
        0x103,
        (
            "#00204FStimulus of bouncy candy,\x01",
            "While checking the freshness of this texture ……\x02\x03",
            "The colorful flavor of the seven colors do not contradict each other,\x01",
            "Harmoniously harmoniously on the tongue.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        "#00201F#4SThis is exactly the gelato revolution …!\x02",
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
            "#00206F……Excuse me,\x01",
            "I was excited very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012Fmy mother……\x01",
            "It seems that she liked it a lot,\x01",
            "Do you ask Tio for introduction here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FYes, here\x01",
            "I can write good comments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Well, I'm glad that you are pleased.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We will continue our shop\x01",
            "I'd like to ask your favorite.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 4)
    SetScenarioFlags(0x172, 1)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_B205")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_B222")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_B235")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_B248")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_B265")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_B278")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_B295")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_B2A8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_B2C5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B2C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_B2D8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B2D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_B2F5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B2F5")

    OP_29(0x80, 0x1, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3F8")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I finished interviewing 6 dining places!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B3EF")

    AnonymousTalk(
        0x101,
        (
            "#00003FMr. Grace right away\x01",
            "It seems I can go to the report … but …\x02\x03",
            "#00000FThe favorite of all six people still\x01",
            "It was not found.\x01",
            "Maybe I'll try harder?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_B3EF")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_B3F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B4C9")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "All members of the Special Affairs Support Division\x01",
            "I found a favorite!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this all six people\x01",
            "I found a favorite.\x02\x03",
            "This is enough for the interview.\x01",
            "Let's go report to the airlines immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_B4C9")

    OP_4C(0xC, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -10150, 1760, 22970, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_39_A964 end

    def Function_40_B4F9(): pass

    label("Function_40_B4F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B507")
    Jump("loc_B8D3")

    label("loc_B507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B515")
    Jump("loc_B8D3")

    label("loc_B515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B523")
    Jump("loc_B8D3")

    label("loc_B523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B531")
    Jump("loc_B8D3")

    label("loc_B531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B59C")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FNow we are rehearsing\x01",
            "It seems to be busy.\x01",
            "Let's stop entering.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_B8D3")

    label("loc_B59C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B607")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FNow we are rehearsing\x01",
            "It seems to be busy.\x01",
            "Let's stop entering.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_B8D3")

    label("loc_B607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B615")
    Jump("loc_B8D3")

    label("loc_B615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B623")
    Jump("loc_B8D3")

    label("loc_B623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B84B")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B75D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B705")

    ChrTalk(
        0x101,
        (
            "#00000FBy the way, today the leaders\x01",
            "It was a story that we planned to watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIt will be annoying if you interfere,\x01",
            "Shall I stop my visit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FOh, that seems better.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B758")

    label("loc_B705")


    ChrTalk(
        0x101,
        (
            "#00000FToday the leaders\x01",
            "It was a story that we planned to watch.\x01",
            "Let's stop entering.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B758")

    Jump("loc_B830")

    label("loc_B75D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7EE")

    ChrTalk(
        0x101,
        (
            "#00003F… … earlier\x01",
            "I just bothered you.\x02\x03",
            "#00000FSoon the leaders\x01",
            "We will need preparation to meet you,\x01",
            "Let's stop entering.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B830")

    label("loc_B7EE")


    ChrTalk(
        0x101,
        (
            "#00000FI just bothered the trouble.\x01",
            "Let's stop entering.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B830")

    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_B8D3")

    label("loc_B84B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B859")
    Jump("loc_B8D3")

    label("loc_B859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B8CA")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FThe alkane shell\x01",
            "準備でIt seems to be busy.\x01",
            "Let's stop entering.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Jump("loc_B8D3")

    label("loc_B8CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B8D3")

    label("loc_B8D3")

    Return()

    # Function_40_B4F9 end

    def Function_41_B8D4(): pass

    label("Function_41_B8D4")

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

    # Function_41_B8D4 end

    SaveToFile()

Try(main)
