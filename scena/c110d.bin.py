from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c110d.bin",                # FileName
        "c110d",                    # MapName
        "c110d",                    # Location
        0x0016,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 3, 0, 4],
    )

    BuildStringList((
        "c110d",                  # 0
        "Chroma",                 # 1
        "Otto",               # 2
        "Haas",                 # 3
        "Citizen",                   # 4
        "boy",                 # 5
        "Citizen",                   # 6
        "Citizen",                   # 7
        "Policeman",                   # 8
        "car",                     # 9
        "Defense Forces soldier",             # 10
        "Defense Forces soldier",             # 11
        "Citizen１",                 # 12
        "Citizen２",                 # 13
        "Citizen３",                 # 14
        "Citizen４",                 # 15
        "Citizen５",                 # 16
        "Citizen６",                 # 17
        "Citizen７",                 # 18
        "Citizen８",                 # 19
        "Central square",               # 20
        "Nishi dori",                 # 21
        "Administrative district",                 # 22
        "Residential area",                 # 23
        "Entertainment district",                 # 24
        "East Street",                 # 25
        "old Town",                 # 26
        "Harbor district",                 # 27
        "IBC",                 # 28
        "Beside the station",               # 29
        "Back street",                 # 30
        "Ursula interchange",           # 31
        "East Crossbell Highway",       # 32
        "West Crossbell Highway",       # 33
        "Mainz Mountain Road",           # 34
        "Orchis Tower",         # 35
    ))

    AddCharChip((
        "chr/ch24900.itc",                   # 00
        "chr/ch20800.itc",                   # 01
        "chr/ch26000.itc",                   # 02
        "chr/ch30000.itc",                   # 03
        "chr/ch21000.itc",                   # 04
        "chr/ch23800.itc",                   # 05
        "chr/ch20400.itc",                   # 06
        "chr/ch21300.itc",                   # 07
    ))

    DeclNpc(6929,    2490,    4294960646, 225,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(8369,    2390,    4294952446, 90,   257,  0x0, 0,   1,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(4294958906, 2390,    9329,    225,  261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294950337, 2500,    4294967167, 270,  389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4294948737, 2500,    4294967077, 45,   385,  0x0, 0,   5,   0,   0,   2,   0,   10,  255,  0)
    DeclNpc(7389,    2500,    4294959116, 135,  389,  0x0, 0,   6,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(8489,    2390,    4294958616, 315,  389,  0x0, 0,   7,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294952246, 2500,    27399,   180,  385,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(16550,   2410,    10660,   1200,    16550,   3910,    10660,   0x007C, 0,  16, 0x0000)

    PlaceName(-31.530000686645508, 0.0, -107.9000015258789, 0x0000, 0x0000, "Central square")
    PlaceName(-117.0, 0.0, -102.05000305175781, 0x0000, 0x0000, "Nishi dori")
    PlaceName(3.5799999237060547, 0.0, 7.800000190734863, 0x0000, 0x0000, "Administrative district")
    PlaceName(-196.3000030517578, 0.0, -5.199999809265137, 0x0000, 0x0000, "Residential area")
    PlaceName(-101.4000015258789, 0.0, -15.600000381469727, 0x0000, 0x0000, "Entertainment district")
    PlaceName(74.0999984741211, 0.0, -137.8000030517578, 0x0000, 0x0000, "East Street")
    PlaceName(120.25, 0.0, -209.3000030517578, 0x0000, 0x0000, "old Town")
    PlaceName(110.5, 0.0, -52.0, 0x0000, 0x0000, "Harbor district")
    PlaceName(76.69999694824219, 0.0, 70.19999694824219, 0x0000, 0x0000, "IBC")
    PlaceName(-16.899999618530273, 0.0, -197.60000610351562, 0x0000, 0x0000, "Beside the station")
    PlaceName(-78.0, 0.0, -62.400001525878906, 0x0000, 0x0000, "Back street")
    PlaceName(-20.799999237060547, 0.0, -237.89999389648438, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(144.3000030517578, 0.0, -119.5999984741211, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-183.3000030517578, 0.0, -104.0, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-175.5, 0.0, 26.0, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(-5.0, 0.0, 178.0, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(-60.130001068115234, 0.0, -126.0999984741211, 0x0000, 0x0051, "")
    PlaceName(9.75, 0.0, -92.30000305175781, 0x0000, 0x0054, "")
    PlaceName(-28.280000686645508, 0.0, -136.5, 0x0000, 0x0057, "")
    PlaceName(-61.099998474121094, 0.0, -88.4000015258789, 0x0000, 0x0053, "")
    PlaceName(-34.45000076293945, 0.0, -57.20000076293945, 0x0000, 0x0053, "")
    PlaceName(-100.43000030517578, 0.0, -94.9000015258789, 0x0000, 0x0053, "")
    PlaceName(-113.0999984741211, 0.0, -67.5999984741211, 0x0000, 0x0053, "")
    PlaceName(-81.9000015258789, 0.0, -26.0, 0x0000, 0x0052, "")
    PlaceName(-75.7300033569336, 0.0, -42.900001525878906, 0x0000, 0x0053, "")
    PlaceName(-64.3499984741211, 0.0, -53.95000076293945, 0x0000, 0x0053, "")
    PlaceName(-27.299999237060547, 0.0, 38.349998474121094, 0x0000, 0x0051, "")
    PlaceName(118.30000305175781, 0.0, -137.8000030517578, 0x0000, 0x0052, "")
    PlaceName(96.19999694824219, 0.0, -255.4499969482422, 0x0000, 0x0053, "")
    PlaceName(79.30000305175781, 0.0, -231.39999389648438, 0x0000, 0x0053, "")

    ChipFrameInfo(1416, 0)                                       # 0

    ScpFunction((
        "Function_0_588",          # 00, 0
        "Function_1_638",          # 01, 1
        "Function_2_711",          # 02, 2
        "Function_3_73C",          # 03, 3
        "Function_4_A9B",          # 04, 4
        "Function_5_AF3",          # 05, 5
        "Function_6_D80",          # 06, 6
        "Function_7_EF6",          # 07, 7
        "Function_8_FE9",          # 08, 8
        "Function_9_1283",         # 09, 9
        "Function_10_13B4",        # 0A, 10
        "Function_11_13FC",        # 0B, 11
        "Function_12_14AF",        # 0C, 12
        "Function_13_1549",        # 0D, 13
        "Function_14_1A2F",        # 0E, 14
        "Function_15_1DAB",        # 0F, 15
        "Function_16_2279",        # 10, 16
    ))


    def Function_0_588(): pass

    label("Function_0_588")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_5C0"),
        (1, "loc_5CC"),
        (2, "loc_5D8"),
        (3, "loc_5E4"),
        (4, "loc_5F0"),
        (5, "loc_5FC"),
        (6, "loc_608"),
        (SWITCH_DEFAULT, "loc_614"),
    )


    label("loc_5C0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_5CC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_5D8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_5E4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_5F0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_5FC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_608")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_614")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_620")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_637")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_620")

    label("loc_637")

    Return()

    # Function_0_588 end

    def Function_1_638(): pass

    label("Function_1_638")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_710")
    OP_95(0xFE, 17250, 2500, -14850, 1000, 0x0)
    OP_95(0xFE, 17250, 2500, -70, 1000, 0x0)
    OP_95(0xFE, 3810, 2500, 8270, 1000, 0x0)
    OP_95(0xFE, -6210, 2500, 23860, 1000, 0x0)
    OP_95(0xFE, -18440, 2500, 23260, 1000, 0x0)
    OP_95(0xFE, -20840, 2450, 19170, 1000, 0x0)
    OP_95(0xFE, -18240, 2500, 6490, 1000, 0x0)
    OP_95(0xFE, -18430, 2500, -3620, 1000, 0x0)
    OP_95(0xFE, -7420, 2500, -14630, 1000, 0x0)
    OP_95(0xFE, 8370, 2390, -14850, 1000, 0x0)
    Jump("Function_1_638")

    label("loc_710")

    Return()

    # Function_1_638 end

    def Function_2_711(): pass

    label("Function_2_711")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_73B")
    OP_94(0xFE, 0xFFFFB2BC, 0x8CA, 0xFFFFBAC8, 0xFFFFF204, 0x3E8)
    Sleep(300)
    Jump("Function_2_711")

    label("loc_73B")

    Return()

    # Function_2_711 end

    def Function_3_73C(): pass

    label("Function_3_73C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A22")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_807")
    SetChrPos(0x0, 30170, 2500, -90, 270)
    SetChrPos(0x1, 30170, 2500, -90, 270)
    SetChrPos(0x2, 30170, 2500, -90, 270)
    SetChrPos(0x3, 30170, 2500, -90, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DA")
    SetChrPos(0x4, 30170, 2500, -90, 270)
    SetChrPos(0x5, 30170, 2500, -90, 270)
    Jump("loc_7F9")

    label("loc_7DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F9")
    SetChrPos(0x4, 30170, 2500, -90, 270)

    label("loc_7F9")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A22")

    label("loc_807")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8CD")
    SetChrPos(0x0, -40390, 0, 24150, 90)
    SetChrPos(0x1, -40390, 0, 24150, 90)
    SetChrPos(0x2, -40390, 0, 24150, 90)
    SetChrPos(0x3, -40390, 0, 24150, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A0")
    SetChrPos(0x4, -40390, 0, 24150, 90)
    SetChrPos(0x5, -40390, 0, 24150, 90)
    Jump("loc_8BF")

    label("loc_8A0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8BF")
    SetChrPos(0x4, -40390, 0, 24150, 90)

    label("loc_8BF")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A22")

    label("loc_8CD")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_981")
    SetChrPos(0x0, -5400, 2500, 35000, 180)
    SetChrPos(0x1, -5400, 2500, 35000, 180)
    SetChrPos(0x2, -5400, 2500, 35000, 180)
    SetChrPos(0x3, -5400, 2500, 35000, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_954")
    SetChrPos(0x4, -5400, 2500, 35000, 180)
    SetChrPos(0x5, -5400, 2500, 35000, 180)
    Jump("loc_973")

    label("loc_954")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_973")
    SetChrPos(0x4, -5400, 2500, 35000, 180)

    label("loc_973")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A22")

    label("loc_981")

    SetChrPos(0x0, 19940, 0, -37920, 0)
    SetChrPos(0x1, 19940, 0, -37920, 0)
    SetChrPos(0x2, 19940, 0, -37920, 0)
    SetChrPos(0x3, 19940, 0, -37920, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9FA")
    SetChrPos(0x4, 19940, 0, -37920, 0)
    SetChrPos(0x5, 19940, 0, -37920, 0)
    Jump("loc_A19")

    label("loc_9FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A19")
    SetChrPos(0x4, 19940, 0, -37920, 0)

    label("loc_A19")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A22")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, -11910, 2490, 8950, 45)
    SetChrPos(0xC, -12830, 2500, 9870, 45)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_A8B")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    Event(0, 13)
    Jump("loc_A9A")

    label("loc_A8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_A9A")
    ClearScenarioFlags(0x22, 1)
    Event(0, 14)

    label("loc_A9A")

    Return()

    # Function_3_73C end

    def Function_4_A9B(): pass

    label("Function_4_A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_AB0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 4)

    label("loc_AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_AC4")
    OP_24(0x7B)
    ClearScenarioFlags(0x0, 5)
    Jump("loc_AE0")

    label("loc_AC4")

    SoundDistance(0x7B, 0xFFFFB32A, 0x99C, 0xFFFFC324, 0x2710, 0x186A0, 0x64, 0x0)

    label("loc_AE0")

    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x6, 0x2)
    ClearMapObjFlags(0x5, 0x4)
    Return()

    # Function_4_A9B end

    def Function_5_AF3(): pass

    label("Function_5_AF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B1C")
    Call(0, 15)
    Return()

    label("loc_B1C")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7C")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B87")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_B87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA7")
    OP_AF(0x81)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D77")

    label("loc_BA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBB")
    Jump("loc_D77")

    label("loc_BBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D77")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_C5F")

    ChrTalk(
        0x8,
        (
            "With that paste,\x01",
            "Surely wonderful\x01",
            "I think that it will be cooked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A little habit comes out\x01",
            "It is charming though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D77")

    label("loc_C5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D01")

    ChrTalk(
        0xFE,
        "welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Popular for some people,\x01",
            "How about \"Nagare tomato soda\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone also drink this\x01",
            "Let's get better!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D77")

    label("loc_D01")


    ChrTalk(
        0xFE,
        (
            "Popular for some people,\x01",
            "How about \"Nagare tomato soda\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone also drink this\x01",
            "Let's get better!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D77")

    Jump("loc_B29")

    label("loc_D7C")

    TalkEnd(0xFE)
    Return()

    # Function_5_AF3 end

    def Function_6_D80(): pass

    label("Function_6_D80")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E68")

    ChrTalk(
        0xFE,
        (
            "I still burn with my eyes ……\x01",
            "No way, Iria-sama like that … ….!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well … … Allowing militant group!\x01",
            "And you forgive, the Imperial Government! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this way, we firmly and independently\x01",
            "There is only thorough anti-war ……!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_EF2")

    label("loc_E68")


    ChrTalk(
        0xFE,
        (
            "Well … … Allowing militant group!\x01",
            "And you forgive, the Imperial Government! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this way, we firmly and independently\x01",
            "There is only thorough anti-war ……!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF2")

    TalkEnd(0xFE)
    Return()

    # Function_6_D80 end

    def Function_7_EF6(): pass

    label("Function_7_EF6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F72")

    ChrTalk(
        0xFE,
        "Come now, How about a balloon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even one, two or three,\x01",
            "Take as much as you can today.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_FE5")

    label("loc_F72")


    ChrTalk(
        0xFE,
        (
            "From the afternoon\x01",
            "Even balloon art classroom\x01",
            "It is scheduled to be held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are interested, please do\x01",
            "Please come and join us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE5")

    TalkEnd(0xFE)
    Return()

    # Function_7_EF6 end

    def Function_8_FE9(): pass

    label("Function_8_FE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1211")

    ChrTalk(
        0xFE,
        "Oh, you guys at the support department.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, good tired.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FThe head office is still recovering, is not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, for the time being\x01",
            "Although it is in tidy up state … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, at the entrance\x01",
            "In a situation where the damage is terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order to restore the reception function,\x01",
            "It will take some time yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, regarding acceptance\x01",
            "The office work temporarily at the police school\x01",
            "I will do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also have Rebecca,\x01",
            "If there is something related to work related work\x01",
            "You should be able to deal with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FIndeed, it is consent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200Fthank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 4)
    Jump("loc_127F")

    label("loc_1211")


    ChrTalk(
        0xFE,
        (
            "Until the head office recovers\x01",
            "It will take a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there is any office work,\x01",
            "You should go to the police school.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_127F")

    TalkEnd(0xFE)
    Return()

    # Function_8_FE9 end

    def Function_9_1283(): pass

    label("Function_9_1283")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_130F")

    ChrTalk(
        0xFE,
        (
            "Have you heard?\x01",
            "Apparently the attack incident during this time\x01",
            "It seems that it was a conspiracy by the empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really\x01",
            "The country of the empire can not forgive.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_13B0")

    label("loc_130F")


    ChrTalk(
        0xFE,
        (
            "But I understood well about this time.\x01",
            "Where they followed the empire they are\x01",
            "It's hard to keep us … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why we want our independence\x01",
            "I have no choice but to push it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B0")

    TalkEnd(0xFE)
    Return()

    # Function_9_1283 end

    def Function_10_13B4(): pass

    label("Function_10_13B4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Doing terrible things to everyone … …\x01",
            "It is a bad guy.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_13B4 end

    def Function_11_13FC(): pass

    label("Function_11_13FC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "今、Citizen会館でやってる\x01",
            "It's a charity event,\x01",
            "It's fun to have various events.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And more than anything, doing this\x01",
            "I think that enjoying will lead to reconstruction\x01",
            "The idea is wonderful.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_13FC end

    def Function_12_14AF(): pass

    label("Function_12_14AF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The event planner\x01",
            "Cross Bell Chamber of Commerce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, every year at the anniversary festival\x01",
            "I think, people from the Chamber of Commerce\x01",
            "It's powerful exciting and powerful.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_14AF end

    def Function_13_1549(): pass

    label("Function_13_1549")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xB, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xB, -11910, 2490, 8950, 45)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, -12830, 2500, 9870, 45)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    Sleep(1000)
    Sound(18, 0, 100, 0)
    UseItem(0x2E7, 0xFF)
    AddItemNumber('克洛斯贝尔时代周刊⑦', 1)
    Sleep(500)
    Sleep(1000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Depending on \"red constellation\"\x01",
            "Crossbell City Trampling#4RA carpet#One week from ──\x02\x03",
            "IBCビルが爆破されたことで\x01",
            "Tensions in neighboring countries increased at a stretch.\x02\x03",
            "In response, Mr. Marybele\x01",
            "Orchis Towerにバックアップしていた\x01",
            "We promptly restore customer data etc. …\x02\x03",
            "By showing perfect correspondence\x01",
            "The ups and downs of neighboring countries were getting drawn.\x02\x03",
            "─ ─ But the scratches left by the hunters are deep,\x01",
            "多くのCitizenはいまだ呆然としていた。\x02\x03",
            "Among them, the big star, Iria · Platier\x01",
            "The news that he suffered a serious injury of mourning\x01",
            "It also gives a great impact to domestic and overseas … ….\x02\x03",
            "Furthermore, the fact that the police headquarters was attacked\x01",
            "The thing that \"red constellation\" can not be grasped\x01",
            "Citizenを言い知れぬ不安に陥れていた。\x02\x03",
            "And ─ ─ behind the \"red constellation\"\x01",
            "Rumors that the Eleventh Empire was\x01",
            "Citizenの間でも囁かれ始めた頃……\x02\x03",
            "It was put off for the incident\x01",
            "A referendum on inquiries about \"the independence of the state\"\x01",
            "Three days later, it was held to be held.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    PlayBGM("ed7563", 0)
    OP_68(-17800, 5250, 30550, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(19500, 0)
    MoveCamera(30, 20, 0, 6000)
    SetCameraDistance(17500, 6000)
    SoundDistance(0x7B, 0xFFFFB32A, 0x99C, 0xFFFFC324, 0x2710, 0x186A0, 0x64, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(6500, 5000, -11300, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    OP_68(-12000, 5000, 6650, 8000)
    MoveCamera(40, 15, 0, 8000)
    SetCameraDistance(14000, 0)
    Sleep(7000)
    StopSound(123, 1000, 20)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ReplaceBGM("ed7150", "ed7563")
    ReplaceBGM("ed7101", "ed7563")
    ReplaceBGM("ed7116", "ed7563")
    ReplaceBGM("ed7117", "ed7563")
    ReplaceBGM("ed7111", "ed7563")
    SetScenarioFlags(0x22, 0)
    NewScene("c120D", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1549 end

    def Function_14_1A2F(): pass

    label("Function_14_1A2F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41400.itc", 0x1E)
    LoadChrToIndex("chr/ch41500.itc", 0x1F)
    LoadChrToIndex("chr/ch24900.itc", 0x20)
    LoadChrToIndex("chr/ch20800.itc", 0x21)
    LoadChrToIndex("chr/ch28100.itc", 0x22)
    LoadChrToIndex("chr/ch28000.itc", 0x23)
    LoadChrToIndex("chr/ch27600.itc", 0x24)
    LoadChrToIndex("chr/ch20400.itc", 0x25)
    LoadChrToIndex("chr/ch21300.itc", 0x26)
    LoadChrToIndex("chr/ch20000.itc", 0x27)
    SoundLoad(821)
    SoundLoad(835)
    ClearChrFlags(0x10, 0x80)
    OP_78(0x4, 0x10)
    OP_49()
    SetChrPos(0x10, 6200, 2500, 12300, 315)
    OP_D5(0x10, 0x0, 0x4CE78, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    ClearMapObjFlags(0x4, 0x4)
    OP_74(0x4, 0x1E)
    OP_70(0x4, 0x2)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 3850, 2500, 11750, 225)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 7250, 2500, 8350, 225)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 4200, 2500, 6700, 45)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 3000, 2500, 6900, 45)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 3000, 2500, 8500, 45)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 2400, 2500, 9200, 45)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 2800, 2500, 4600, 0)
    SetChrChipByIndex(0x18, 0x25)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 4500, 2500, 4700, 0)
    SetChrChipByIndex(0x19, 0x26)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -200, 2500, 8000, 90)
    SetChrChipByIndex(0x1A, 0x27)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 900, 2500, 6700, 45)
    OP_68(6700, 4000, 11200, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    OP_68(5700, 3500, 10200, 10000)
    MoveCamera(45, 17, 0, 10000)
    SetCameraDistance(18000, 10000)
    Sound(821, 2, 60, 0)
    Sound(835, 2, 80, 0)
    FadeToBright(1500, 0)
    OP_0D()
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("President Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "─ ─ at a sudden announcement\x01",
            "There are many people who were surprised.\x02\x03",
            "But now, to the crossbell\x01",
            "unprecedented#6RLet's see#The crisis is approaching.\x02\x03",
            "Trampling on justice,\x01",
            "Trying to deprive our dignity\x01",
            "The wicked will is approaching.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    StopSound(851, 1500, 60)
    StopSound(835, 1500, 80)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 4)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1A2F end

    def Function_15_1DAB(): pass

    label("Function_15_1DAB")

    EventBegin(0x0)
    EventBegin(0x0)
    Fade(500)
    OP_68(4610, 4500, -7760, 0)
    MoveCamera(88, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(11540, 0)
    SetChrPos(0x101, 6140, 2500, -8020, 45)
    SetChrPos(0x102, 5350, 2500, -7210, 45)
    SetChrPos(0x103, 5330, 2500, -8820, 45)
    SetChrPos(0x109, 4540, 2500, -8000, 45)
    SetChrPos(0x105, 4520, 2500, -9610, 45)
    SetChrPos(0x104, 3740, 2500, -8790, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()

    ChrTalk(
        0xFE,
        "welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Popular for some people,\x01",
            "How about \"Nagare tomato soda\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone also drink this\x01",
            "Let's get better!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Mr. Tantos said that\x01",
            "The ingredients of tomatoes are\x01",
            "Condensed extract … …)\x02\x03",
            "(Will you get it here?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Customers, are you ready for your order?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FUm, actually, hey\x01",
            "There is something I would like to consult … …\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd told the situation.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Indeed, then here\x01",
            "How about having it brought?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '苦西红柿酱'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('苦西红柿酱', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        "#00105Fthis is……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, I use it in my house\x01",
            "We made boiled tomatoes\x01",
            "It is paste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you use this, nourishment tonic,\x01",
            "No doubt -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Surely wonderful\x01",
            "I think that it will be cooked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI am saved.\x01",
            "Then, those who pay the price ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, everyone\x01",
            "Help reconstruction\x01",
            "Is it done?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you do not mind\x01",
            "Please take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FI see, I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102Fthank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19C, 5)
    SetScenarioFlags(0x0, 6)
    OP_29(0x8E, 0x1, 0x4)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 5330, 2500, -8020, 56)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_15_1DAB end

    def Function_16_2279(): pass

    label("Function_16_2279")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_228A")
    Jump("loc_2555")

    label("loc_228A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2555")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Charity event\x01",
            "\"~ Let's spread by everyone circle of reconstruction ~\"\x01",
            "In the case of\x01",
            "【Program Overview】\x01",
            "· Solo piano concert\x01",
            "· Miss · Crossbell Contest\x01",
            "· Mass gourmet contest\x01",
            "· Various art work classes\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "  場所 ：クロスベルCitizen会館・多目的ホール \x01",
            "Hall\x01",
            "Date: Today\x01",
            "Organizer: Cross Bell Chamber of Commerce / Crosbell City\x01",
            "In the case of\x01",
            "※ The participation fee of various events,\x01",
            "All will be used for funds for reconstruction assistance. In the case of\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_2555")

    TalkEnd(0xFF)
    Return()

    # Function_16_2279 end

    SaveToFile()

Try(main)
