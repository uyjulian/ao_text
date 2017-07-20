from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0500.bin",                # FileName
        "c0500",                    # MapName
        "c0500",                    # Location
        0x0026,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("c0500", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 38, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0500",                  # 0
        "Iris",               # 1
        "Bidding bucket",         # 2
        "Policeman",                   # 3
        "Policeman",                   # 4
        "Hunter Sachs",           # 5
        "A hunter",                   # 6
        "Realtor",             # 7
        "Man of the eye",               # 8
        "Redhead girl",             # 9
        "Rector",               # 10
        "Hunting soldier Gareth",             # 11
        "car",                     # 12
        "Grace",               # 13
        "Tsao",                 # 14
        "Row",                   # 15
        "Zile",                 # 16
        "Yuri",                 # 17
        "Sykes",               # 18
        "Reggie",                 # 19
        "Kate policing",             # 20
        "Police investigation",           # 21
        "SE control",                 # 22
        "Muller",               # 23
        "Olivier",               # 24
        "Central square",               # 25
        "Nishi dori",                 # 26
        "Administrative district",                 # 27
        "Residential area",                 # 28
        "Entertainment district",                 # 29
        "East Street",                 # 30
        "old Town",                 # 31
        "Harbor district",                 # 32
        "IBC",                 # 33
        "Beside the station",               # 34
        "Back street",                 # 35
        "Ursula interchange",           # 36
        "East Crossbell Highway",       # 37
        "West Crossbell Highway",       # 38
        "Mainz Mountain Road",           # 39
        "Orchis Tower",         # 40
    ))

    AddCharChip((
        "chr/ch26900.itc",                   # 00
        "chr/ch26700.itc",                   # 01
        "chr/ch30000.itc",                   # 02
        "chr/ch27800.itc",                   # 03
        "chr/ch42800.itc",                   # 04
        "chr/ch42900.itc",                   # 05
        "chr/ch43000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch85150.itc",               # 10
        "monster/ch85151.itc",               # 11
    ))

    DeclNpc(4294961126, 0,       1399,    90,   257,  0x0, 0,   0,   0,   0,   1,   0,   5,   255,  0)
    DeclNpc(4294959706, 0,       2980,    180,  257,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294966496, 0,       40500,   180,  389,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(800,     0,       40500,   180,  389,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4294966496, 0,       40500,   180,  389,  0x0, 0,   4,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(800,     0,       40500,   180,  389,  0x0, 0,   6,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(4294955347, 0,       3000,    180,  449,  0x0, 0,   3,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 28,  8.0,                   -2.0,                  -0.5,                  900.0,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.600000023841858,    0.1666666716337204,    0.10000000149011612,   1.0])
    DeclEvent(0x0000, 0, 29,  -8.0,                  -2.0,                  -0.5,                  576.0,                 [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   2.0,                   0.1666666716337204,    0.10000000894069672,   1.0])
    DeclEvent(0x0000, 0, 34,  0.09000000357627869,   5.46999979019165,      -0.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.04500000178813934,  -2.734999895095825,    0.10000000149011612,   1.0])

    DeclActor(0,       300,     43650,   1000,    0,       1800,    43650,   0x007C, 0,  35, 0x0000)
    DeclActor(18980,   600,     4810,    1000,    18980,   2100,    4810,    0x007C, 0,  36, 0x0000)
    DeclActor(5660,    790,     5620,    1000,    5660,    2000,    5620,    0x007C, 0,  37, 0x0000)

    PlaceName(79.5, 0.0, -9.0, 0x0000, 0x0000, "Central square")
    PlaceName(0.0, 0.0, -76.5, 0x0000, 0x0000, "Nishi dori")
    PlaceName(11.0, 0.0, 116.0, 0x0000, 0x0000, "Administrative district")
    PlaceName(-148.0, 0.0, -60.0, 0x0000, 0x0000, "Residential area")
    PlaceName(-57.25, 0.0, 10.0, 0x0000, 0x0000, "Entertainment district")
    PlaceName(196.0, 0.0, 56.0, 0x0000, 0x0000, "East Street")
    PlaceName(294.0, 0.0, 31.0, 0x0000, 0x0000, "old Town")
    PlaceName(154.0, 0.0, 158.0, 0x0000, 0x0000, "Harbor district")
    PlaceName(20.0, 0.0, 233.0, 0x0000, 0x0000, "IBC")
    PlaceName(168.0, 0.0, -73.0, 0x0000, 0x0000, "Beside the station")
    PlaceName(1.0, 0.0, -9.0, 0x0000, 0x0000, "Back street")
    PlaceName(200.0, 0.0, -112.0, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(240.0, 0.0, 130.0, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-52.0, 0.0, -134.0, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-156.0, 0.0, -17.0, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(-140.0, 0.0, 255.0, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(71.0, 0.0, -49.0, 0x0000, 0x0051, "")
    PlaceName(100.5, 0.0, 38.5, 0x0000, 0x0054, "")
    PlaceName(106.0, 0.0, -31.0, 0x0000, 0x0057, "")
    PlaceName(38.0, 0.0, -18.5, 0x0000, 0x0053, "")
    PlaceName(35.5, 0.0, 32.0, 0x0000, 0x0053, "")
    PlaceName(9.0, 0.0, -57.0, 0x0000, 0x0053, "")
    PlaceName(-23.5, 0.0, -45.0, 0x0000, 0x0053, "")
    PlaceName(-33.0, 0.0, 16.0, 0x0000, 0x0052, "")
    PlaceName(-15.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(6.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(-41.0, 0.0, 118.0, 0x0000, 0x0051, "")
    PlaceName(233.0, 0.0, 91.0, 0x0000, 0x0052, "")
    PlaceName(313.0, 0.0, -26.0, 0x0000, 0x0053, "")
    PlaceName(278.0, 0.0, -19.5, 0x0000, 0x0053, "")

    ChipFrameInfo(2048, 0)                                       # 0

    ScpFunction((
        "Function_0_800",          # 00, 0
        "Function_1_8B0",          # 01, 1
        "Function_2_917",          # 02, 2
        "Function_3_9A0",          # 03, 3
        "Function_4_C78",          # 04, 4
        "Function_5_FF8",          # 05, 5
        "Function_6_1E4E",         # 06, 6
        "Function_7_29F7",         # 07, 7
        "Function_8_2B53",         # 08, 8
        "Function_9_2BA7",         # 09, 9
        "Function_10_2C25",        # 0A, 10
        "Function_11_34B8",        # 0B, 11
        "Function_12_3D07",        # 0C, 12
        "Function_13_401E",        # 0D, 13
        "Function_14_4157",        # 0E, 14
        "Function_15_4184",        # 0F, 15
        "Function_16_41BB",        # 10, 16
        "Function_17_520E",        # 11, 17
        "Function_18_526C",        # 12, 18
        "Function_19_526D",        # 13, 19
        "Function_20_52C3",        # 14, 20
        "Function_21_52C4",        # 15, 21
        "Function_22_5329",        # 16, 22
        "Function_23_532A",        # 17, 23
        "Function_24_595B",        # 18, 24
        "Function_25_5D24",        # 19, 25
        "Function_26_5D4D",        # 1A, 26
        "Function_27_5DB5",        # 1B, 27
        "Function_28_5F4C",        # 1C, 28
        "Function_29_62D7",        # 1D, 29
        "Function_30_663B",        # 1E, 30
        "Function_31_7D2F",        # 1F, 31
        "Function_32_7FC8",        # 20, 32
        "Function_33_84DB",        # 21, 33
        "Function_34_9189",        # 22, 34
        "Function_35_9551",        # 23, 35
        "Function_36_96B0",        # 24, 36
        "Function_37_9710",        # 25, 37
        "Function_38_9747",        # 26, 38
        "Function_39_979E",        # 27, 39
    ))


    def Function_0_800(): pass

    label("Function_0_800")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_838"),
        (1, "loc_844"),
        (2, "loc_850"),
        (3, "loc_85C"),
        (4, "loc_868"),
        (5, "loc_874"),
        (6, "loc_880"),
        (SWITCH_DEFAULT, "loc_88C"),
    )


    label("loc_838")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_898")

    label("loc_844")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_898")

    label("loc_850")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_898")

    label("loc_85C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_898")

    label("loc_868")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_898")

    label("loc_874")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_898")

    label("loc_880")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_898")

    label("loc_88C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_898")

    label("loc_898")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8AF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_898")

    label("loc_8AF")

    Return()

    # Function_0_800 end

    def Function_1_8B0(): pass

    label("Function_1_8B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_916")
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_95(0xFE, -240, 0, 15530, 1000, 0x0)
    Sleep(3600)
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_95(0xFE, -24330, 0, 1400, 1000, 0x0)
    Sleep(1200)
    Jump("Function_1_8B0")

    label("loc_916")

    Return()

    # Function_1_8B0 end

    def Function_2_917(): pass

    label("Function_2_917")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_99F")
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, 8240, 0, 1400, 1000, 0x0)
    Sleep(3600)
    OP_95(0xFE, 740, 0, 1400, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, -24330, 0, 1400, 1000, 0x0)
    Sleep(1200)
    Jump("Function_2_917")

    label("loc_99F")

    Return()

    # Function_2_917 end

    def Function_3_9A0(): pass

    label("Function_3_9A0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B30")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A8F")
    SetChrPos(0x0, 20160, 0, 650, 270)
    SetChrPos(0x1, 20160, 0, 650, 270)
    SetChrPos(0x2, 20160, 0, 650, 270)
    SetChrPos(0x3, 20160, 0, 650, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A62")
    SetChrPos(0x4, 20160, 0, 650, 270)
    SetChrPos(0x5, 20160, 0, 650, 270)
    Jump("loc_A81")

    label("loc_A62")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A81")
    SetChrPos(0x4, 20160, 0, 650, 270)

    label("loc_A81")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B30")

    label("loc_A8F")

    SetChrPos(0x0, -24900, 0, 220, 90)
    SetChrPos(0x1, -24900, 0, 220, 90)
    SetChrPos(0x2, -24900, 0, 220, 90)
    SetChrPos(0x3, -24900, 0, 220, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B08")
    SetChrPos(0x4, -24900, 0, 220, 90)
    SetChrPos(0x5, -24900, 0, 220, 90)
    Jump("loc_B27")

    label("loc_B08")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B27")
    SetChrPos(0x4, -24900, 0, 220, 90)

    label("loc_B27")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B30")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B47")
    Jump("loc_B93")

    label("loc_B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B5F")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_B93")

    label("loc_B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B6D")
    Jump("loc_B93")

    label("loc_B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B80")
    SetChrFlags(0x8, 0x80)
    Jump("loc_B93")

    label("loc_B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B93")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_B93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_BA7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 13)
    Jump("loc_C32")

    label("loc_BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_BBB")
    ClearScenarioFlags(0x22, 1)
    Event(0, 23)
    Jump("loc_C32")

    label("loc_BBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_BCF")
    ClearScenarioFlags(0x22, 2)
    Event(0, 24)
    Jump("loc_C32")

    label("loc_BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_BE8")
    ClearScenarioFlags(0x22, 3)
    SetMapFlags(0x10000000)
    Event(0, 31)
    Jump("loc_C32")

    label("loc_BE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_C01")
    ClearScenarioFlags(0x22, 4)
    SetMapFlags(0x10000000)
    Event(0, 32)
    Jump("loc_C32")

    label("loc_C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_C15")
    ClearScenarioFlags(0x22, 5)
    Event(0, 33)
    Jump("loc_C32")

    label("loc_C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_C32")
    ClearScenarioFlags(0x22, 6)
    SetChrPos(0x0, -10280, 0, 250, 90)

    label("loc_C32")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C4C")
    Event(0, 27)

    label("loc_C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C77")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_C77")

    Return()

    # Function_3_9A0 end

    def Function_4_C78(): pass

    label("Function_4_C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C94")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CC8")

    label("loc_C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CB0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CC8")

    label("loc_CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 0)), scpexpr(EXPR_END)), "loc_CC8")
    SetScenarioFlags(0x0, 3)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x25, 0)

    label("loc_CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_CDC")
    OP_24(0x80)
    ClearScenarioFlags(0x0, 3)
    Jump("loc_D87")

    label("loc_CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D87")
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xE, 0x64, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D7C")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    Sound(128, 1, 100, 0)
    Jump("loc_D87")

    label("loc_D7C")

    StopEffect(0x7, 0x0)
    OP_8A(0x9)
    Sound(128, 1, 60, 0)

    label("loc_D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DF6")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xE, 0x64, 0x0)

    label("loc_DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E18")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x1E, 0x78, 0x0)

    label("loc_E18")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E31")
    OP_10(0x0, 0x0)
    OP_10(0xB, 0x1)
    Jump("loc_E37")

    label("loc_E31")

    OP_10(0x0, 0x1)
    OP_10(0xB, 0x0)

    label("loc_E37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E50")
    BeginChrThread(0x8, 0, 0, 2)
    OP_1B(0x2, 0x0, 0x10)

    label("loc_E50")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E89")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_E89")

    ModifyEventFlags(0, 2, 0x80)
    ClearMapObjFlags(0x2, 0x10)
    OP_70(0x2, 0x0)
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_EAE")
    OP_66(0x0, 0x1)
    Jump("loc_F9F")

    label("loc_EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_ED4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_END)), "loc_ECB")
    SetMapObjFlags(0x2, 0x10)
    Jump("loc_ECF")

    label("loc_ECB")

    OP_66(0x0, 0x1)

    label("loc_ECF")

    Jump("loc_F9F")

    label("loc_ED4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_EE6")
    OP_66(0x0, 0x1)
    Jump("loc_F9F")

    label("loc_EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_EF4")
    Jump("loc_F9F")

    label("loc_EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F07")
    ModifyEventFlags(1, 2, 0x80)
    Jump("loc_F9F")

    label("loc_F07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F1A")
    ModifyEventFlags(1, 2, 0x80)
    Jump("loc_F9F")

    label("loc_F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F2D")
    ModifyEventFlags(1, 2, 0x80)
    Jump("loc_F9F")

    label("loc_F2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_F40")
    ModifyEventFlags(1, 2, 0x80)
    Jump("loc_F9F")

    label("loc_F40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F53")
    ModifyEventFlags(1, 2, 0x80)
    Jump("loc_F9F")

    label("loc_F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_F71")
    SetMapObjFlags(0x2, 0x10)
    OP_1B(0x0, 0x0, 0x26)
    OP_1B(0x1, 0x0, 0x27)
    Jump("loc_F9F")

    label("loc_F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_F83")
    OP_66(0x0, 0x1)
    Jump("loc_F9F")

    label("loc_F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_F9F")
    OP_66(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F9F")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_F9F")

    ClearMapObjFlags(0x3, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FBB")
    OP_70(0x3, 0x5)
    OP_65(0x1, 0x1)

    label("loc_FBB")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FDE")
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)
    OP_66(0x2, 0x1)

    label("loc_FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF7")
    SetMapObjFrame(0xFF, "crimson", 0x0, 0x1)

    label("loc_FF7")

    Return()

    # Function_4_C78 end

    def Function_5_FF8(): pass

    label("Function_5_FF8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_118C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F3")

    ChrTalk(
        0xFE,
        (
            "Because it is somehow difficult time,\x01",
            "Even at the shop, it is a strange solidarity feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am also a rival child\x01",
            "To the top battle,\x01",
            "Anything got better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a hostess, to customers\x01",
            "If you enjoy having it and drinking it\x01",
            "That's good ☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1187")

    label("loc_10F3")


    ChrTalk(
        0xFE,
        (
            "With the rival's child\x01",
            "To the top battle,\x01",
            "Anything got better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a hostess, to customers\x01",
            "If you enjoy having it and drinking it\x01",
            "That's good ☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1187")

    Jump("loc_1E4A")

    label("loc_118C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_119A")
    Jump("loc_1E4A")

    label("loc_119A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_12CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1255")

    ChrTalk(
        0xFE,
        (
            "National independence ……\x01",
            "It is a good sound when you put it in your mouth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The shop people, too,\x01",
            "Look at the President's speech\x01",
            "She seems to have been very happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Somehow I also\x01",
            "I got to be happy ♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_12CA")

    label("loc_1255")


    ChrTalk(
        0xFE,
        (
            "The shop people, too,\x01",
            "Look at the President's speech\x01",
            "She seems to have been very happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Somehow I also\x01",
            "I got to be happy ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12CA")

    Jump("loc_1E4A")

    label("loc_12CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_12DD")
    Jump("loc_1E4A")

    label("loc_12DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1370")

    ChrTalk(
        0xFE,
        (
            "To occupy Mainz,\x01",
            "It is not really a major incident …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The miners,\x01",
            "You came to the store before.\x01",
            "I hope it is safe ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E4A")

    label("loc_1370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_14A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1422")

    ChrTalk(
        0xFE,
        "Listen, listen, big news!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How, in the store of my house\x01",
            "This month's nominated number one\x01",
            "I decided it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, worth the effort\x01",
            "Wow ~!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_149B")

    label("loc_1422")


    ChrTalk(
        0xFE,
        (
            "Finally to the number one wishfully\x01",
            "It has become!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, I will appoint it from now on\x01",
            "It will increase more and more,\x01",
            "I have to do my best!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_149B")

    Jump("loc_1E4A")

    label("loc_14A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_14ED")

    ChrTalk(
        0xFE,
        (
            "The central square is noisy though ….\x01",
            "What, what happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E4A")

    label("loc_14ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1641")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D4")

    ChrTalk(
        0xFE,
        (
            "A rival child competing for the number of nominations,\x01",
            "To increase my nomination\x01",
            "You called the acquaintance to the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why, I do not think that's awful! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I do this,\x01",
            "I can not do anything\x01",
            "I do it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_163C")

    label("loc_15D4")


    ChrTalk(
        0xFE,
        (
            "How to be a child of a rival\x01",
            "I can not lose!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To become number one\x01",
            "Why do you do it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_163C")

    Jump("loc_1E4A")

    label("loc_1641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_179B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1705")

    ChrTalk(
        0xFE,
        (
            "brother,\x01",
            "Would you like to play at our store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Actually, now with the rival's child\x01",
            "You are fighting for the nomination number by the close difference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The winner is number one this month!\x01",
            "So please cooperate, are not you?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1796")

    label("loc_1705")


    ChrTalk(
        0xFE,
        (
            "… Well, I see.\x01",
            "Your older brothers are working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then, when you come to our store\x01",
            "You should nominate me.\x01",
            "Because the number one is on!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1796")

    Jump("loc_1E4A")

    label("loc_179B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_180E")

    ChrTalk(
        0xFE,
        (
            "Recently, the rival child of the store\x01",
            "I have increased my nomination bang bang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have to make sure not to lose.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E4A")

    label("loc_180E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_19C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_193D")

    ChrTalk(
        0xFE,
        (
            "Orkis Tower\x01",
            "It's a really great building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A little out of work,\x01",
            "I have been watching the show,\x01",
            "I'm outraged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A man working in such a place,\x01",
            "I am sure that the economy is really good\x01",
            "People must be different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When entering the restaurant at our place,\x01",
            "I would like you to nominate me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19C0")

    label("loc_193D")


    ChrTalk(
        0xFE,
        (
            "Orkis Tower\x01",
            "It's a really great building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A person working in such a place\x01",
            "When entering the restaurant at our place,\x01",
            "I would like you to nominate me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C0")

    Jump("loc_1E4A")

    label("loc_19C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A86")

    ChrTalk(
        0xFE,
        (
            "I heard from customers,\x01",
            "From tomorrow I have a trade meeting\x01",
            "It seems to begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A festival like a memorial festival\x01",
            "It does not seem to be ….\x01",
            "I wonder what kind of event it is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B17")

    label("loc_1A86")


    ChrTalk(
        0xFE,
        (
            "Oops, I dont.\x01",
            "It is not a matter of mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right now I will not lose to the rival's child\x01",
            "To increase the number of nominations at least one\x01",
            "I have to think about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B17")

    Jump("loc_1E4A")

    label("loc_1B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_1C94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C08")

    ChrTalk(
        0xFE,
        (
            "A little earlier, with red hair\x01",
            "A good gag of odysang\x01",
            "I was around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With a cute girl like a cat,\x01",
            "As you can see the older brother who is like a playboy\x01",
            "It seems I was taking a … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, something\x01",
            "It was a strange sight.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C8F")

    label("loc_1C08")


    ChrTalk(
        0xFE,
        (
            "by the way,\x01",
            "Even my older brother who just caught seeing me,\x01",
            "It was a similar hair color.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is everyone family or something?\x01",
            "I did not look alike.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C8F")

    Jump("loc_1E4A")

    label("loc_1C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1D24")

    ChrTalk(
        0xFE,
        (
            "The area on the back alley is\x01",
            "Is it true that it was put out for sale?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There used to be a fear of black clothes ~ older brother in the front … ….\x01",
            "I wonder what kind of people will go next.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E4A")

    label("loc_1D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1E4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC5")

    ChrTalk(
        0xFE,
        "Uooh, with an iris ~ ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "brother,\x01",
            "Would you like to play at our store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Talking with me drinking,\x01",
            "Let's have a good time ~ spray\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E4A")

    label("loc_1DC5")


    ChrTalk(
        0xFE,
        (
            "Recently, the nomination has also increased\x01",
            "It is very substantial.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Differing from the rival's son,\x01",
            "Among them, Number One Nominated\x01",
            "Because it is going to be!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E4A")

    TalkEnd(0xFE)
    Return()

    # Function_5_FF8 end

    def Function_6_1E4E(): pass

    label("Function_6_1E4E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1F96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F19")

    ChrTalk(
        0xFE,
        (
            "Older brother, older brother,\x01",
            "Would you like to stay in our store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "President Dieter's detention memorial\x01",
            "Hyper happy sale and so on ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… even at the Independence Memorial\x01",
            "Did you do sale with secret?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F91")

    label("loc_1F19")


    ChrTalk(
        0xFE,
        (
            "President Dieter's detention memorial\x01",
            "Hyper happy sale and so on ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… even at the Independence Memorial\x01",
            "Did you do sale with secret?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F91")

    Jump("loc_29F3")

    label("loc_1F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1FA4")
    Jump("loc_29F3")

    label("loc_1FA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_205A")

    ChrTalk(
        0xFE,
        (
            "Older brother, older brother,\x01",
            "At the store of ours is an independent memorial,\x01",
            "During the Super Happy Sale and!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dawn of the crossbell,\x01",
            "Spend time with a cute girl\x01",
            "With Son well!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F3")

    label("loc_205A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_20FD")

    ChrTalk(
        0xFE,
        (
            "Older brother, my shop, too\x01",
            "During this time, I resumed business ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tired mind and body in restoration work,\x01",
            "With pretty girls\x01",
            "Please drink and play and heal! Is it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F3")

    label("loc_20FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_218B")

    ChrTalk(
        0xFE,
        (
            "Occupation incident or what ….\x01",
            "I wish I had become a terrible thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well as expected, this situation\x01",
            "Do not get excited about touring customers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F3")

    label("loc_218B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_222D")

    ChrTalk(
        0xFE,
        (
            "Okay, even if it rained again.\x01",
            "There are few customers, it is painful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yesterday I was talking about a crash accident happening,\x01",
            "What's wrong with the economy?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F3")

    label("loc_222D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2296")

    ChrTalk(
        0xFE,
        (
            "Anything, the square is better\x01",
            "Peepep Pipe noisy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Were there also cases?\x02",
    )

    CloseMessageWindow()
    Jump("loc_29F3")

    label("loc_2296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_23E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_236A")

    ChrTalk(
        0xFE,
        (
            "Today is the usual store of our place\x01",
            "Happy sale and.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Pretty girls\x01",
            "This is another cute costume\x01",
            "I will welcome you ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Missing today,\x01",
            "Do not know when to do next!\x01",
            "Hey Hey, Tsubameki!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_23DF")

    label("loc_236A")


    ChrTalk(
        0xFE,
        (
            "Today is the usual store of our place\x01",
            "Happy sale and.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Missing today,\x01",
            "Do not know when to do next!\x01",
            "Hey Hey, Tsubameki!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23DF")

    Jump("loc_29F3")

    label("loc_23E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_247B")

    ChrTalk(
        0xFE,
        (
            "Recently, how is independence,\x01",
            "It is only a misfortune thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In such a case,\x01",
            "I'm relaxing at our store.\x01",
            "Let me be happy ~ ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F3")

    label("loc_247B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_251C")

    ChrTalk(
        0xFE,
        (
            "I saw it on the street\x01",
            "Police doctors, too,\x01",
            "It seems like you get into a burning sensation ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The person who gets tired of work is the target eye of the customer.\x01",
            "Try calling out later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F3")

    label("loc_251C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_259E")

    ChrTalk(
        0xFE,
        (
            "Heads of countries\x01",
            "You seem to have entered the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you could drink at our store\x01",
            "It will be advertisement yeah.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F3")

    label("loc_259E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2631")

    ChrTalk(
        0xFE,
        (
            "I got into the alley\x01",
            "Crimson's brothers,\x01",
            "People that seems to be good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To, introduce a pretty child\x01",
            "With a new regular person getting on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F3")

    label("loc_2631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_270D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C4")

    ChrTalk(
        0xFE,
        (
            "Ah ~, this is Akan.\x01",
            "I wish I was already in the rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nobody will catch on today.\x01",
            "Do you plan to raise it soon?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2708")

    label("loc_26C4")


    ChrTalk(
        0xFE,
        (
            "…… Redhead's older brother?\x01",
            "Behind the alley just there\x01",
            "It looks like it was in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2708")

    Jump("loc_29F3")

    label("loc_270D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_277E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2728")
    Call(0, 7)
    Jump("loc_2779")

    label("loc_2728")


    ChrTalk(
        0xFE,
        (
            "There are many rainy days\x01",
            "The customer is not getting caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Whew, but in trouble.\x02",
    )

    CloseMessageWindow()

    label("loc_2779")

    Jump("loc_29F3")

    label("loc_277E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_29F3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2847")

    ChrTalk(
        0xFE,
        (
            "Through this place ago\x01",
            "Redhead knee who went to the entertainment district … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That person,\x01",
            "Before this as well\x01",
            "I feel like I saw it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, I am curious.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_28C4")

    label("loc_2847")


    ChrTalk(
        0xFE,
        (
            "If you are redheaded Knee,\x01",
            "I walked toward the entertainment district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before this as well\x01",
            "I feel like I saw it, but …\x01",
            "Well, it is due to mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28C4")

    Jump("loc_29F3")

    label("loc_28C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28DB")
    Call(0, 7)
    Jump("loc_29F3")

    label("loc_28DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29C4")

    ChrTalk(
        0xFE,
        (
            "Hehe, this is rude.\x01",
            "I just missed it this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What did you do when you next visit\x01",
            "I will give you a service ticket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI do not need it.\x01",
            "… … Bribery is also a fine crime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To\x01",
            "Do not worry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_29F3")

    label("loc_29C4")


    ChrTalk(
        0xFE,
        (
            "Hehe, this is rude.\x01",
            "I just missed it this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29F3")

    TalkEnd(0xFE)
    Return()

    # Function_6_1E4E end

    def Function_7_29F7(): pass

    label("Function_7_29F7")


    ChrTalk(
        0x9,
        (
            "Oh, the older brothers\x01",
            "Are you going to have fun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A store of ours, Kawaiko-chan\x01",
            "Mr. Gee!\x01",
            "Hey, come on! What?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F…… Forced bucks are illegal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder what he's doing ….,\x01",
            "Are you a guy of Cassatsu?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hehe, this is rude.\x01",
            "You should miss it this time only, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(Fuu … as usual\x01",
            "Security around here is bad. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 2)
    Return()

    # Function_7_29F7 end

    def Function_8_2B53(): pass

    label("Function_8_2B53")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Currently, this building is\x01",
            "The department is under investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please refrain from entering.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_2B53 end

    def Function_9_2BA7(): pass

    label("Function_9_2BA7")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Because of red constellations,\x01",
            "Outrageous things\x01",
            "It's what made me do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Early in the incident\x01",
            "I hope I can solve it … …\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_2BA7 end

    def Function_10_2C25(): pass

    label("Function_10_2C25")

    EventBegin(0x0)
    SetChrPos(0x101, -600, 0, 37200, 0)
    SetChrPos(0x102, 600, 0, 37200, 0)
    SetChrPos(0x109, -1200, 0, 36000, 0)
    SetChrPos(0x105, 1200, 0, 36000, 0)
    ClearChrFlags(0xE, 0x8)
    SetChrPos(0xE, 0, 0, 27000, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    Fade(1000)
    OP_68(-100, 900, 38010, 0)
    MoveCamera(24, 25, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(17100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00001Fhere……\x01",
            "It is the site of Rubathe shop.\x02\x03",
            "#00003FIt should be a skimless sky now ….\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Male voice",
        (
            "Oh yours,\x01",
            "What are you doing there?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(200, 900, 36700, 3000)
    MoveCamera(36, 27, 0, 3000)
    OP_6E(520, 3000)
    SetCameraDistance(17780, 3000)

    def lambda_2DD7():

        label("loc_2DD7")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_2DD7")

    QueueWorkItem2(0x101, 2, lambda_2DD7)

    def lambda_2DE9():

        label("loc_2DE9")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_2DE9")

    QueueWorkItem2(0x102, 2, lambda_2DE9)

    def lambda_2DFB():

        label("loc_2DFB")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_2DFB")

    QueueWorkItem2(0x109, 2, lambda_2DFB)

    def lambda_2E0D():

        label("loc_2E0D")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_2E0D")

    QueueWorkItem2(0x105, 2, lambda_2E0D)

    def lambda_2E1F():
        OP_95(0xFE, 0, 0, 33500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2E1F)
    WaitChrThread(0xE, 1)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0x101,
        "#00005FWell, you are …?\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)

    NpcTalk(
        0xE,
        "male",
        (
            "#12PKohon, I am in Crossbell City\x01",
            "He is a real estate businessman.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "male",
        (
            "#12PConsigned to the autonomous state government,\x01",
            "I am entrusted with the management of the land in a certain area.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "male",
        "#12PIt will be a problem if you go into the premises without permission.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00103FGovernment entrusted … ….\x01",
            "By the way it is also from the grandpa\x01",
            "I heard that story.\x02\x03",
            "#00100FEven if it is a property that Mafia had\x01",
            "Because I can not leave it alone,\x01",
            "It seems that consignment was decided as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003Fgot it……\x02\x03",
            "#00000FEr, I was disappointed,\x01",
            "We are Crossbell police.\x02\x03",
            "Now a little bit of city\x01",
            "I'm patrolling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12POh, were they police people?\x01",
            "Good work till such a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10100FWell, then then today\x01",
            "Periodic inspection or something on this building?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PDisagreeable……\x01",
            "Actually, this building will soon,\x01",
            "It is supposed to be put out for sale.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#00005FIs this property for sale …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12POh, in fact to several companies a while ago\x01",
            "Have been requested to move in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PAs one of them will come to negotiations today,\x01",
            "I will have you wait here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10105FTo the property of former Mafia\x01",
            "Is it a company that wants to move in? …\x02\x03",
            "#10106FThat's what it is saying ……\x01",
            "All right#6R噵 噵 噵#What'll we do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12PWell, we are also a bit uneasy … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PBecause it is such a large building.\x01",
            "Even management costs alone will not be stupid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PIf someone can undertake it,\x01",
            "There is no reason to refuse us either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10303FWell, as a trader\x01",
            "I want to give up quickly\x01",
            "It is a natural feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FOh, but I will …\x02\x03",
            "#00000FYou do not have to bother me,\x01",
            "Shall we go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00103FYeah … … let's do that.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xE, 0x8)
    SetChrPos(0x0, 90, 0, 80, 180)
    SetScenarioFlags(0x139, 1)
    EventEnd(0x5)
    Return()

    # Function_10_2C25 end

    def Function_11_34B8(): pass

    label("Function_11_34B8")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(0, 1000, 45000, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(17000, 0)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    SetChrPos(0xC, -800, 0, 40500, 180)
    SetChrPos(0xD, 800, 0, 40500, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -600, 0, 29200, 0)
    SetChrPos(0x102, 600, 0, 29200, 0)
    SetChrPos(0x104, 0, 0, 31000, 0)
    SetChrPos(0x109, -600, 0, 28000, 0)
    SetChrPos(0x105, 600, 0, 28000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Fade(1000)
    OP_68(110, 900, 37020, 0)
    MoveCamera(30, 23, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(18000, 0)
    OP_0D()

    def lambda_3602():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3602)

    def lambda_3613():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3613)

    def lambda_3624():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3624)

    def lambda_3635():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3635)

    def lambda_3646():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3646)

    def lambda_3657():
        OP_95(0xFE, -600, 0, 34200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3657)

    def lambda_3671():
        OP_95(0xFE, 600, 0, 34200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3671)

    def lambda_368B():
        OP_95(0xFE, 0, 0, 36000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_368B)

    def lambda_36A5():
        OP_95(0xFE, -1200, 0, 33000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_36A5)

    def lambda_36BF():
        OP_95(0xFE, 1200, 0, 33000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_36BF)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xD,
        "Why are you …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, it is Captain Randolph!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Have you come today, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001F(A red constellation hunter … …\x01",
            "It looks like Randy's face knows. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F…… Sachs, the comfort of the new Negishi\x01",
            "Is not it a nice idea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Haha, thanks, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It is close to the \"Neue-Bran\" branch of the entertainment district,\x01",
            "I'm getting used to it conveniently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FHappy …… It's been as hard as ever.\x02\x03",
            "#00301F…… My uncle today, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh, your head and lady today as well\x01",
            "Where you are about to leave on demand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Something's got a message\x01",
            "I will tell it from me, what will you do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00303F… … Good, did you disturb me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        "#5P#00300FLet's go, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FOh, ah ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Kuku, it is also a captain.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x101, -760, 0, 930, 45)
    SetChrPos(0x102, 1220, 0, 930, 0)
    SetChrPos(0x104, 370, 0, 3760, 0)
    SetChrPos(0x109, 2170, 0, 2080, 315)
    SetChrPos(0x105, 3000, 0, 660, 315)
    OP_68(1930, 1850, 500, 0)
    MoveCamera(323, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12700, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00303F…… Hun,\x01",
            "It seems you used Resident Person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105F\"What?\"\x01",
            "Have you visited recently?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00303FWhile we are talking about some story\x01",
            "There was no tone at all.\x02\x03",
            "#00301FBut apparently,\x01",
            "Even if I go to see you this way\x01",
            "It seems that there is no plan to reveal its appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FHmm, in the near future\x01",
            "Some contacts\x01",
            "It may come in handy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10106FBut when that happens …\x01",
            "For the red constellation on the path\x01",
            "It seems to be only listening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FOh, we cleared up our support request\x01",
            "Let's turn around the places.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 90, 0, 80, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetScenarioFlags(0x14E, 3)
    EventEnd(0x5)
    Return()

    # Function_11_34B8 end

    def Function_12_3D07(): pass

    label("Function_12_3D07")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -400, 110, 43100, 0)
    SetChrPos(0x102, -950, 0, 41870, 0)
    SetChrPos(0x103, 1520, 0, 41870, 0)
    SetChrPos(0x104, 450, 0, 42540, 0)
    SetChrPos(0x109, 1020, 0, 39990, 0)
    SetChrPos(0x105, -400, 0, 40830, 0)
    OP_68(-100, 1950, 41030, 0)
    MoveCamera(359, 23, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(11000, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sound(807, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FThey locked it up huh\x02\x03",
            "#00001FThe investigation of department also ended as usual,\x01",
            "There should not be anyone inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FRun away with such a flying boat,\x01",
            "I wonder where I am now … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FFor them, the guard also\x01",
            "I seem to be wary of it strictly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F…\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)
    Sleep(50)

    ChrTalk(
        0x103,
        "#12P#00200FRandy?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(50)
    TurnDirection(0x102, 0x104, 500)
    TurnDirection(0x105, 0x104, 500)
    TurnDirection(0x109, 0x104, 500)
    Sleep(50)

    ChrTalk(
        0x105,
        "#6P#10308FYou ok?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)
    OP_93(0x104, 0xB4, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#00304FHaha, don't worry\x02\x03",
            "#00301FHowever … … If you see me next time\x01",
            "Do not settle on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FYes, right\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -100, 0, 41030, 180)
    SetScenarioFlags(0x18E, 1)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_12_3D07 end

    def Function_13_401E(): pass

    label("Function_13_401E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SoundLoad(468)
    ClearChrFlags(0x13, 0x80)
    OP_78(0x4, 0x13)
    OP_49()
    SetChrPos(0x13, 18000, 0, 500, 0)
    OP_D5(0x13, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x1, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40E2")
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x8000)
    EndChrThread(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, -8800, 0, 3100, 90)
    SetChrPos(0x8, -7300, 0, 3100, 270)

    label("loc_40E2")

    FadeToBright(1000, 0)
    BeginChrThread(0x13, 3, 0, 14)
    BeginChrThread(0x1D, 1, 0, 15)
    OP_68(-13800, 2750, 3000, 0)
    MoveCamera(57, 7, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    OP_68(-13800, 750, 3000, 7000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 0)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_401E end

    def Function_14_4157(): pass

    label("Function_14_4157")

    SetChrPos(0xFE, 18000, 0, 500, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -37000, 0, 500)
    OP_9F(0x2, 0xFE, 5000, 0x6)
    Return()

    # Function_14_4157 end

    def Function_15_4184(): pass

    label("Function_15_4184")

    Sound(468, 2, 100, 0)
    Sound(458, 0, 60, 0)
    Sleep(1500)
    Sound(491, 0, 90, 0)
    Sleep(400)
    Sound(491, 0, 90, 0)
    Sleep(1100)
    Sound(459, 0, 100, 0)
    Sleep(2500)
    Sound(494, 0, 70, 0)
    StopSound(468, 1000, 100)
    Return()

    # Function_15_4184 end

    def Function_16_41BB(): pass

    label("Function_16_41BB")

    EventBegin(0x0)
    SoundLoad(2753)
    SoundLoad(3834)
    SoundLoad(3941)
    Fade(500)
    OP_68(0, 1950, 3500, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -50, 0, 4650, 0)
    SetChrPos(0x102, -630, 0, 3570, 0)
    SetChrPos(0x109, 910, 0, 2930, 0)
    SetChrPos(0x105, 520, 0, 2260, 0)
    SetChrFlags(0x8, 0x80)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00013F#6P(……!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6P(……Ah……)\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    AddParty(0x3, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch03300.itc", 0x1E)
    LoadChrToIndex("chr/ch03400.itc", 0x1F)
    LoadChrToIndex("chr/ch07400.itc", 0x20)
    LoadChrToIndex("apl/ch51114.itc", 0x21)
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis403.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04601.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04500.itp")
    ClearMapObjFlags(0x2, 0x10)
    OP_32(0xFF, 0xFE, 0x0)
    OP_68(0, 2150, 37500, 0)
    MoveCamera(0, 22, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(19000, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0xF, 0x4)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrPos(0xF, 300, 0, 41500, 180)
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrPos(0x10, -900, 0, 41600, 180)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x11, 0x20)
    SetChrPos(0x11, -3020, 0, 40750, 135)
    SetChrPos(0x104, -200, 0, 37500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    PlayBGM("ed7561", 0)
    OP_25(0x80, 0x50)
    FadeToBright(1000, 0)
    SetCameraDistance(15000, 4500)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 850, 39710, 0)
    MoveCamera(1, 18, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(11100, 0)
    SetChrFlags(0x10, 0x2000)
    SetChrFlags(0xF, 0x2000)
    OP_0D()
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x104,
        "#00311F#2753V#6P#30W─ ─ Uncle, Shirley.\x02",
    )

    CloseMessageWindow()
    OP_24(0xAC1)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x10,
        (
            "#3941V#5P#20WHaha.\x01",
            "Long time brother!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xF65)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0xF,
        (
            "#3834V#11P#30WIt's been two years.\x01",
            "It looks like it has not changed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xEFA)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    OP_C9(0x1, 0x80000000)
    ClearChrFlags(0x10, 0x2000)
    ClearChrFlags(0xF, 0x2000)
    SetChrPos(0x101, -50, 0, 30650, 0)
    SetChrPos(0x102, -630, 0, 29570, 0)
    SetChrPos(0x109, 910, 0, 28930, 0)
    SetChrPos(0x105, 420, 0, 28060, 0)
    SetChrPos(0x104, 0, 0, 37500, 0)
    OP_68(-240, 1350, 37560, 0)
    MoveCamera(325, 14, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(11830, 0)
    Fade(500)

    def lambda_46EB():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_46EB)
    Sleep(50)

    def lambda_4703():
        OP_9B(0x0, 0x102, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4703)
    Sleep(50)

    def lambda_471B():
        OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_471B)
    Sleep(50)

    def lambda_4733():
        OP_9B(0x0, 0x109, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4733)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00007F#6P… …. Randy ……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#6P#NThose people yesterday …!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        "#10303F#6P#NAre the doubtful people trampling together?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x11,
        (
            "#03509F#5PHaha, after all, boyfriend,\x01",
            "Was it the family of this Osan?\x02\x03",
            "#03502FBecause it was the color of the exact same hair\x01",
            "I never thought it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#6P…\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00013F#6PLector Captain ……\x01",
            "Why are you here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6PAbout this acquisition\x01",
            "Is something involved?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#03504F#5POh, I have a back work.\x02\x03",
            "#03510FWell ~, somehow I wear black eyed glasses\x01",
            "It was good to go through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#04609F#11PHuh, I'm looking forward to it!\x02\x03",
            "#04602FAlthough I retreated at the time of the eastern people street\x01",
            "Next time I think I can play it all wonderfully!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00005F#6PToho People Street ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6PLast year in Calvado\x01",
            "War broke with black moon?\x02\x03",
            "#00311F── Hey, your uncle.\x01",
            "Why did you come to Crossbell?\x02\x03",
            "What on earth are you going to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04504F#11PPowered by Translate\x01",
            "It is decided for business.\x02\x03",
            "#04500FRandolph than that.\x01",
            "I have something to tell you.\x02\x03",
            "── Big brother passed away#2RYes#You did it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00305F#6P#40W#2S………Huh………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6PIt is! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04503F#11PAbout six months ago.\x02\x03",
            "It was rebellious with the head of \"west breeze\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#04602F#11PIt is a long-time nemesis\x01",
            "The settlement of \"fighting god\" and \"hunting king\"!\x02\x03",
            "#04612FAlready, it was truly amazing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00308F#6P#40W…………………………………….\x02\x03",
            "#00304F#40W… …. Is that so ……\x02\x03",
            "#30WThat fucking father …… to the end\x01",
            "I guess I passed away while fighting.\x02\x03",
            "#00300F#40W… … You looked satisfied, did not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#04602F#11PYup!\x01",
            "It looked really fun!\x02\x03",
            "#04606FOkay, Shirley too\x01",
            "I want such an opponent ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04504F#11PWell, my brother will not regret.\x02\x03",
            "#04501F─ ─ We are at a loss\x01",
            "Besides being a nonsigning son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#6P……!\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xF,
        (
            "#04504F#5PThe vacation is over, Randolph.\x02\x03",
            "#04502FBecause there is any talk\x01",
            "Keep your body open.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x10,
        "#04609F#11PSee you again, Randy Brother!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x11,
        "#03509F#5PThen, I'm tired.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0xF, 0, 0, 17)
    BeginChrThread(0x10, 0, 0, 19)
    BeginChrThread(0x11, 0, 0, 21)
    WaitChrThread(0xF, 0)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x11, 0)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Sleep(500)
    Fade(500)
    OP_68(-680, 1150, 38230, 0)
    MoveCamera(328, 13, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00108F#6P#N… …. Randy …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10113F#6P#NRandy-senpai …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00008F#6PTwo of them, Randy's …?\x02",
    )

    CloseMessageWindow()
    OP_64(0x104)
    Sleep(500)

    ChrTalk(
        0x104,
        "#00306F#5P#30WAh……\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x190)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#00303F#11P#30WDeputy head of \"Red constellation\"\x01",
            "Sigmund Orlando.\x02\x03",
            "That daughter and one of the commander,\x01",
            "Shirley · Orlando.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrSubChip(0x104, 0x1)
    Sleep(150)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sleep(350)

    ChrTalk(
        0x104,
        (
            "#00311F#11P#30WMy uncle, you and my cousin ……\x01",
            "── It is the strongest worst fighting demon.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(330, 22, 0, 0)
    MoveCamera(333, 30, 0, 4500)
    SetCameraDistance(14500, 4500)
    FadeToDark(0, 16777215, -1)
    FadeToBright(2000, 16777215)
    Sound(896, 0, 100, 0)
    Sleep(1000)
    Sound(966, 0, 70, 0)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    Sleep(2000)
    StopSound(128, 2000, 80)
    WaitBGM()
    OP_29(0xA2, 0x1, 0x6)
    OP_29(0xA1, 0x4, 0x10)
    OP_29(0xA2, 0x4, 0x10)
    SetScenarioFlags(0x20B, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_50F9")
    Jump("loc_50FE")

    label("loc_50F9")

    OP_29(0x67, 0x4, 0x40)

    label("loc_50FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_510F")
    Jump("loc_5114")

    label("loc_510F")

    OP_29(0x6D, 0x4, 0x40)

    label("loc_5114")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5125")
    Jump("loc_512A")

    label("loc_5125")

    OP_29(0x6E, 0x4, 0x40)

    label("loc_512A")

    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E5(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_E0(0x1D, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C9(0x0, 0x10)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x25, 0)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x25, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x2, 0x10)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x1, 0x10)
    OP_E5(0xB)
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_41BB end

    def Function_17_520E(): pass

    label("Function_17_520E")

    OP_95(0xFE, 0, 0, 42270, 2000, 0x0)
    OP_95(0xFE, 0, 300, 43640, 2000, 0x0)
    Sound(103, 0, 100, 0)
    OP_71(0x2, 0x1, 0xA, 0x1, 0x0)
    Sleep(500)

    def lambda_5250():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5250)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
    Return()

    # Function_17_520E end

    def Function_18_526C(): pass

    label("Function_18_526C")

    Return()

    # Function_18_526C end

    def Function_19_526D(): pass

    label("Function_19_526D")

    Sleep(1500)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 0, 0, 42270, 2000, 0x0)
    OP_95(0xFE, 0, 300, 43640, 2000, 0x0)

    def lambda_52A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_52A7)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
    Return()

    # Function_19_526D end

    def Function_20_52C3(): pass

    label("Function_20_52C3")

    Return()

    # Function_20_52C3 end

    def Function_21_52C4(): pass

    label("Function_21_52C4")

    Sleep(2000)
    OP_93(0xFE, 0x2D, 0x1F4)
    OP_95(0xFE, 0, 0, 42270, 2000, 0x0)
    OP_95(0xFE, 0, 300, 43640, 2000, 0x0)

    def lambda_52FB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_52FB)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0xA, 0x0, 0x1, 0x0)
    Return()

    # Function_21_52C4 end

    def Function_22_5329(): pass

    label("Function_22_5329")

    Return()

    # Function_22_5329 end

    def Function_23_532A(): pass

    label("Function_23_532A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(3973)
    SoundLoad(3974)
    LoadChrToIndex("chr/ch03300.itc", 0x1E)
    LoadChrToIndex("chr/ch03400.itc", 0x1F)
    LoadChrToIndex("chr/ch03401.itc", 0x20)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, -3800, 6500, 7700, 20)
    OP_8E(0xF, "Sigmund")
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x10, -2500, 6500, 8100, 20)
    OP_8E(0x10, "Charlie")
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x5)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x12, -2800, 6500, 5900, 20)
    OP_52(0x12, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, -4500, 6500, 5900, 20)
    OP_4B(0xC, 0xFF)
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-3100, 7700, 7000, 0)
    MoveCamera(348, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16540, 0)
    VolumeBGM(0x5A, 0x3E8)
    SetCameraDistance(14540, 3000)
    FadeToBright(2000, 0)
    Sleep(2500)
    OP_63(0x10, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x10,
        (
            "#04602F#3973V#5P#30WUwah!\x01",
            "That building, ridiculous ~!\x02\x03",
            "#04612F#3974VHey, Charlie\x01",
            "I wonder if I will break it! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF86)
    OP_C9(0x1, 0x80000000)
    TurnDirection(0xF, 0x10, 500)
    Sleep(300)

    ChrTalk(
        0xF,
        (
            "#04504F#5PGiggle\x01",
            "I understand the feeling, but stop stopping.\x02\x03",
            "#04500FIn any of those buildings\x01",
            "I'm going to be helpful.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    ChrTalk(
        0x10,
        (
            "#04606F#11PMum, sorry.\x02\x03",
            "#04602Fwhatever,\x01",
            "Will you follow the city with a bra?\x02\x03",
            "#04612FBecause of that building\x01",
            "It seems to be very crowded ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#04504F#5POh, you should go.\x02",
    )

    CloseMessageWindow()
    OP_68(-2220, 7700, 6340, 1500)
    MoveCamera(346, 20, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(14540, 1500)
    OP_92(0x10, 0x0, 0x1DB0, 0x1F4)
    Sound(809, 0, 50, 0)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x1)

    def lambda_56D9():
        OP_9D(0xFE, 0x0, 0x1450, 0x1DB0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_56D9)
    Sleep(300)

    def lambda_56F9():

        label("loc_56F9")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_56F9")

    QueueWorkItem2(0xF, 2, lambda_56F9)

    def lambda_570B():

        label("loc_570B")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_570B")

    QueueWorkItem2(0x12, 2, lambda_570B)

    def lambda_571D():

        label("loc_571D")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_571D")

    QueueWorkItem2(0xC, 2, lambda_571D)
    WaitChrThread(0x10, 1)
    Sound(62, 0, 100, 0)
    OP_92(0x10, 0x0, 0x1004, 0x1F4)

    def lambda_5746():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5746)
    WaitChrThread(0x10, 1)
    Sound(844, 0, 50, 0)
    SetChrSubChip(0x10, 0x2)

    def lambda_576E():
        OP_9D(0xFE, 0x0, 0x0, 0xE10, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_576E)
    WaitChrThread(0x10, 1)
    EndChrThread(0xF, 0x2)
    EndChrThread(0x12, 0x2)
    EndChrThread(0xC, 0x2)
    SetChrFlags(0x10, 0x80)
    Sleep(300)

    ChrTalk(
        0xC,
        "#5PHa ha … … It is truly a lady.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PYo he is that building\x01",
            "Did you like it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04504F#5PHuh, that too.\x02\x03",
            "#04502FBut more than that - ─\x01",
            "I guess you are drunk with the blood premonition.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xF, 500)

    ChrTalk(
        0xC,
        "#6P……!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0xF, 500)

    ChrTalk(
        0x12,
        (
            "#12P……I see.\x01",
            "She looks like Charlie.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-2660, 7700, 8140, 1500)
    MoveCamera(345, 17, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(14500, 1500)
    OP_93(0xF, 0x14, 0x12C)
    OP_6F(0x79)

    ChrTalk(
        0xF,
        (
            "#04504F#5PKuku …… Truly my daughter.\x02\x03",
            "#04502FApparently enough for tomorrow\x01",
            "I do not enjoy it and it seems to be done.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 1)
    NewScene("m0101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_532A end

    def Function_24_595B(): pass

    label("Function_24_595B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    OP_68(20160, 1950, 650, 0)
    MoveCamera(23, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 21160, 0, 650, 270)
    SetChrPos(0x102, 22560, 0, -410, 270)
    SetChrPos(0x103, 23560, 0, 2050, 270)
    SetChrPos(0x104, 24160, 0, -760, 270)
    SetChrPos(0x109, 25160, 0, 1120, 270)
    SetChrPos(0x105, 26260, 0, 250, 270)
    OP_68(360, 1950, 3660, 4800)
    MoveCamera(344, 10, 0, 3000)
    OP_6E(600, 4000)
    SetCameraDistance(16500, 4000)
    BeginChrThread(0x101, 3, 0, 25)
    BeginChrThread(0x102, 3, 0, 25)
    BeginChrThread(0x103, 3, 0, 25)
    BeginChrThread(0x104, 3, 0, 25)
    BeginChrThread(0x109, 3, 0, 25)
    BeginChrThread(0x105, 3, 0, 25)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    Fade(500)
    OP_68(210, 1950, 34660, 0)
    MoveCamera(0, 39, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(13640, 0)
    SetChrPos(0x101, 0, 0, 33570, 0)
    SetChrPos(0x102, -760, 0, 32800, 0)
    SetChrPos(0x103, 940, 0, 32549, 0)
    SetChrPos(0x104, 140, 0, 31650, 0)
    SetChrPos(0x109, 1450, 0, 31370, 0)
    SetChrPos(0x105, -1150, 0, 31220, 0)

    def lambda_5B37():
        OP_95(0xFE, 10, 0, 39370, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B37)
    Sleep(30)

    def lambda_5B54():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B54)
    Sleep(30)

    def lambda_5B6C():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B6C)
    Sleep(50)

    def lambda_5B84():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5B84)
    Sleep(30)

    def lambda_5B9C():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5B9C)

    def lambda_5BB1():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5BB1)
    OP_68(320, 1950, 40090, 6000)
    MoveCamera(9, 40, 0, 5000)
    OP_6E(760, 5000)
    SetCameraDistance(11370, 5000)
    WaitChrThread(0x101, 1)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    Sleep(200)
    TurnDirection(0x101, 0xA, 500)
    TurnDirection(0xA, 0x101, 500)
    Sleep(600)
    OP_93(0x101, 0x3C, 0x1F4)
    TurnDirection(0xB, 0x101, 500)
    Sleep(600)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    def lambda_5C2F():
        OP_95(0xFE, 10, 0, 43000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C2F)
    Sleep(400)
    BeginChrThread(0x102, 3, 0, 26)
    Sleep(600)
    BeginChrThread(0x103, 3, 0, 26)
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(200)
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 26)
    WaitChrThread(0x101, 1)
    Sleep(150)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)

    def lambda_5C94():
        OP_95(0xFE, 0, 0, 45000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C94)

    def lambda_5CAE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5CAE)
    Sleep(100)
    BeginChrThread(0x109, 3, 0, 26)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 26)
    OP_68(-120, 1950, 43100, 5000)
    MoveCamera(9, 43, 0, 5000)
    OP_6E(760, 5000)
    SetCameraDistance(19370, 5000)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("c0510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_595B end

    def Function_25_5D24(): pass

    label("Function_25_5D24")

    OP_95(0xFE, 0, 0, 650, 5000, 0x0)
    OP_95(0xFE, 0, 0, 6000, 5000, 0x0)
    Return()

    # Function_25_5D24 end

    def Function_26_5D4D(): pass

    label("Function_26_5D4D")


    def lambda_5D52():
        OP_95(0xFE, 0, 0, 39370, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D52)
    WaitChrThread(0xFE, 1)

    def lambda_5D70():
        OP_95(0xFE, 0, 0, 43670, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D70)
    WaitChrThread(0xFE, 1)

    def lambda_5D8E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5D8E)

    def lambda_5D9F():
        OP_95(0xFE, 0, 0, 45000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D9F)
    Return()

    # Function_26_5D4D end

    def Function_27_5DB5(): pass

    label("Function_27_5DB5")

    EventBegin(0x0)
    Fade(1000)
    OP_68(0, 900, 40500, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    OP_F0(0x0, 0x5)
    SetChrPos(0x101, -600, 0, 34200, 0)
    SetChrPos(0x102, 600, 0, 34200, 0)
    SetChrPos(0x103, -1200, 0, 33000, 0)
    SetChrPos(0x104, 1200, 0, 33000, 0)
    OP_68(0, 900, 35500, 4000)
    SetCameraDistance(20000, 4000)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#00001F#5PAlready……\x01",
            "It looks like there is no one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#6PEven the police only locked\x01",
            "I should have left it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PThings to say by all means\x01",
            "Have you picked up yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F#11PAnyway let's head in\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 34000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x182, 3)
    EventEnd(0x5)
    Return()

    # Function_27_5DB5 end

    def Function_28_5F4C(): pass

    label("Function_28_5F4C")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch06000.itc", 0x1E)
    LoadChrToIndex("chr/ch06300.itc", 0x20)
    LoadChrToIndex("chr/ch31400.itc", 0x21)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03200.itp")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    EndChrThread(0x8, 0x0)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 0, 0, 3460, 0)
    OP_68(60, 1950, 1170, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(9020, 0)
    OP_0D()
    SetChrPos(0x101, 5800, 0, 1000, 270)
    SetChrPos(0x102, 5000, 0, 0, 270)
    SetChrPos(0x109, 7000, 0, 740, 270)
    SetChrPos(0x105, 6200, 0, -260, 270)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x14,
        (
            "#02101FWell …\x01",
            "It started moving at last.\x02\x03",
            "#02103FIf you are negotiating\x01",
            "Is it OK to write an article?\x02\x03",
            "#02101FThe pressure from the Republic\x01",
            "Recently, though it is decreasing … ….\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    OP_68(4410, 1950, 40, 0)
    MoveCamera(316, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12090, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00005FMr. Grace,\x01",
            "What are you doing?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(1680, 1950, 600, 3000)
    MoveCamera(312, 19, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(11520, 3000)

    def lambda_61C8():
        OP_93(0x14, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_61C8)

    def lambda_61D5():
        OP_95(0x101, 850, 0, 1360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_61D5)
    Sleep(100)

    def lambda_61F2():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_61F2)
    Sleep(100)

    def lambda_620A():
        OP_95(0x105, 0, 0, 360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_620A)
    Sleep(100)

    def lambda_6227():
        OP_9B(0x0, 0x109, 0x0, 0x1194, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6227)
    WaitChrThread(0x109, 1)

    def lambda_6240():
        OP_95(0x109, 1300, 0, 260, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6240)
    Sleep(100)
    OP_6F(0x79)
    WaitChrThread(0x102, 1)

    def lambda_6263():
        OP_95(0x102, -600, 0, 1560, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6263)
    WaitChrThread(0x101, 1)

    def lambda_6281():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6281)

    def lambda_628E():
        OP_93(0x14, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_628E)
    WaitChrThread(0x109, 1)

    def lambda_629F():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_629F)
    Sleep(200)
    WaitChrThread(0x105, 1)

    def lambda_62B3():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_62B3)
    Sleep(200)
    WaitChrThread(0x102, 1)

    def lambda_62C7():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_62C7)
    WaitChrThread(0x105, 1)
    Call(0, 30)
    Return()

    # Function_28_5F4C end

    def Function_29_62D7(): pass

    label("Function_29_62D7")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch06000.itc", 0x1E)
    LoadChrToIndex("chr/ch06300.itc", 0x20)
    LoadChrToIndex("chr/ch31400.itc", 0x21)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03200.itp")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    EndChrThread(0x8, 0x0)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 0, 0, 3460, 0)
    OP_68(60, 1950, 1170, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(9020, 0)
    OP_0D()
    SetChrPos(0x101, -5120, 0, 1430, 90)
    SetChrPos(0x102, -6740, 0, 1310, 90)
    SetChrPos(0x109, -6070, 0, 120, 90)
    SetChrPos(0x105, -8320, 0, 280, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x14,
        (
            "#12P#02101FWell …\x01",
            "It started moving at last.\x02\x03",
            "#02103FIf you are negotiating\x01",
            "Is it OK to write an article?\x02\x03",
            "#02101FThe pressure from the Republic\x01",
            "Recently, though it is decreasing … ….\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    OP_68(250, 1950, 420, 0)
    MoveCamera(305, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(9020, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00005FMr. Grace,\x01",
            "What are you doing?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(1680, 1950, 600, 3000)
    MoveCamera(312, 19, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(11520, 3000)

    def lambda_6557():
        TurnDirection(0x14, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6557)

    def lambda_6564():
        OP_95(0x101, 850, 0, 1360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6564)
    Sleep(100)

    def lambda_6581():
        OP_95(0x102, -600, 0, 1560, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6581)
    Sleep(100)

    def lambda_659E():
        OP_95(0x109, 1300, 0, 260, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_659E)
    Sleep(100)

    def lambda_65BB():
        OP_95(0x105, 0, 0, 360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_65BB)
    Sleep(1000)

    def lambda_65D8():
        OP_93(0x14, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_65D8)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)

    def lambda_65EB():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_65EB)

    def lambda_65F8():
        OP_93(0x14, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_65F8)
    WaitChrThread(0x102, 1)

    def lambda_6609():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6609)
    WaitChrThread(0x109, 1)

    def lambda_661A():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_661A)
    WaitChrThread(0x105, 1)

    def lambda_662B():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_662B)
    WaitChrThread(0x105, 1)
    Call(0, 30)
    Return()

    # Function_29_62D7 end

    def Function_30_663B(): pass

    label("Function_30_663B")

    Sleep(100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x14,
        (
            "What is it …?\x01",
            "Lloyd is not you guys.\x02\x03",
            "I see, the Special Affairs Support Division,\x01",
            "Is not it restarting at last?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        "#6P#00000FYes, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FTio and Randy are\x01",
            "I joined it later, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#02100FThat's a little disappointing.\x02\x03",
            "#02106FJust a moment, Wazy you\x01",
            "I will enter the support section ~.\x02\x03",
            "#02102FSister, indeed soul#5RTake care#You know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHuh, I'm surprised at all.\x02\x03",
            "#10304FWhat is the feature article\x01",
            "I do not mind if you collaborate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00006FYou know.\x02",
    )

    CloseMessageWindow()
    OP_93(0x14, 0xB4, 0x0)

    ChrTalk(
        0x14,
        (
            "#02109FHaha, it looks fun.\x02\x03",
            "#02106FI would like to talk a lot if possible\x01",
            "Take in now.\x02\x03",
            "#02102FWhen it is over, slowly ──\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 2490, 0, 32509, 180)

    NpcTalk(
        0x15,
        "Voice of a young man",
        "#NOh, this is an unusual look.\x02",
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7114", 0)
    Fade(500)
    OP_68(0, 1950, 4810, 0)
    MoveCamera(0, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(8890, 0)
    SetChrPos(0x15, 0, 0, 10350, 180)
    OP_93(0x14, 0x168, 0x0)
    SetChrChipByIndex(0x16, 0x21)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -750, 0, 11350, 180)

    def lambda_6A7B():
        OP_98(0x15, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6A7B)
    Sleep(50)

    def lambda_6A98():
        OP_98(0x16, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6A98)
    Sleep(50)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#N#00005FAh……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#3P#N#00101FTsao branch manager ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x14,
        "#12P#N#02106F……Oops.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(1580, 1750, 1260, 0)
    MoveCamera(315, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12350, 0)
    SetChrPos(0x15, 1000, 0, 3350, 180)
    SetChrPos(0x16, 750, 0, 4350, 180)
    SetChrPos(0x14, -1000, 0, 3460, 90)
    OP_93(0x101, 0x0, 0x0)
    OP_93(0x102, 0x2D, 0x0)
    OP_93(0x109, 0x0, 0x0)
    OP_93(0x105, 0x2D, 0x0)
    OP_0D()
    Sleep(100)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x15,
        (
            "long time no see.\x01",
            "Mr. Lloyd, Ellie.\x02\x03",
            "Well then\x01",
            "Is Noger serious?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#6P#10111FWhy, why …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FOh\x01",
            "It is truly an information network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03204FHuff, no other\x01",
            "Because it is about the Special Affairs Support Division.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x10E, 0x1F4)

    ChrTalk(
        0x15,
        (
            "#03200FBut, I do not like Grace\x01",
            "It is said that the movement of this place was grabbed.\x02\x03",
            "#03209FAs expected, the\x01",
            "It's the Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#02109FNo~……\x01",
            "It is coincidence, so coincidentally!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001F…… Unity, in such a place\x01",
            "What are you doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FOn the site of Rubathe\x01",
            "Was it something you wanted?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0xB4, 0x1F4)

    ChrTalk(
        0x15,
        (
            "#03200FHa ha, have you decided?\x02\x03",
            "#03204FTo keep it as it is\x01",
            "It is too wasteful land.\x02\x03",
            "#03202FSo if our company is effective\x01",
            "I thought about using it.\x02",
        )
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
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00001F……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03203FHoff, Mafia's possessions etc.\x01",
            "It will be hard to put out hands as long as normal.\x02\x03",
            "#03210FBut if we are somewhat#6R噵 噵 噵#\x01",
            "I am used to the property in that hand.\x02\x03",
            "#03204FEven for a contractor\x01",
            "My head will hurt monthly administrative expenses,\x01",
            "I hear that you can do a good deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00010FDamn\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#02101FWell, Mr. Tsao.\x01",
            "Is it possible to write such information?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03200FOh, it does not matter.\x01",
            "It is not an idiot.\x02\x03",
            "#03204FIt is a matter of speculation\x01",
            "I'd like to have a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#02109FOh, haha ….\x01",
            "Of course I do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03200FHuh, then I will excuse you.\x02\x03",
            "Mr. Lloyd, if there is something\x01",
            "Please come and visit our company.\x02\x03",
            "#03204F…… I will go, Lau.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "What.\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x0)

    def lambda_7259():
        OP_9B(0x1, 0x101, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7259)
    Sleep(50)

    def lambda_7271():
        OP_9B(0x1, 0x102, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7271)

    def lambda_7286():
        OP_9B(0x1, 0x109, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7286)
    Sleep(50)

    def lambda_729E():
        OP_9B(0x1, 0x105, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_729E)
    Sleep(50)

    def lambda_72B6():
        OP_95(0x15, -2500, 0, 1660, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_72B6)
    Sleep(500)
    OP_96(0x16, 0x0, 0x0, 0x898, 0x7D0, 0x0)

    def lambda_72E7():
        OP_95(0x15, -12000, 0, 1660, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_72E7)

    def lambda_7301():
        OP_95(0x16, -12000, 0, 1560, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_7301)

    def lambda_731B():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_731B)
    Sleep(50)

    def lambda_732B():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_732B)
    Sleep(50)

    def lambda_733B():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_733B)
    Sleep(50)

    def lambda_734B():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_734B)
    Sleep(50)

    def lambda_735B():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_735B)
    OP_0D()
    WaitChrThread(0x16, 1)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    StopBGM(0xDAC)
    OP_63(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x14)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x101,
        "#12P#00001F………………………….\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7117", 0)

    ChrTalk(
        0x109,
        (
            "#12P#10101FWell, it was a wonderful person.\x02\x03",
            "#10106FLike a frog glared at a snake\x01",
            "I was in the mood … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00103FI see …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FYoung executive Kuro Monday,\x01",
            "\"White Orchids\" Tsao Lee?\x02\x03",
            "#10306FIt looks like more than rumors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FOh, as usual.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(240, 1750, 1140, 3000)
    MoveCamera(326, 26, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(12930, 3000)

    def lambda_7553():
        OP_93(0x14, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7553)

    def lambda_7560():
        OP_95(0x101, 500, 0, 2660, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7560)
    Sleep(100)

    def lambda_757D():
        OP_95(0x102, -710, 0, 1990, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_757D)
    Sleep(100)

    def lambda_759A():
        OP_95(0x109, 900, 0, 1300, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_759A)
    Sleep(100)

    def lambda_75B7():
        OP_95(0x105, -270, 0, 760, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_75B7)
    WaitChrThread(0x101, 1)

    def lambda_75D5():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75D5)
    WaitChrThread(0x102, 1)

    def lambda_75E6():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_75E6)
    WaitChrThread(0x109, 1)

    def lambda_75F7():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_75F7)
    WaitChrThread(0x105, 1)

    def lambda_7608():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7608)
    OP_6F(0x79)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#12P#00001F── Grace.\x01",
            "Kuroun moon this Rubache?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#02101FYeah, warehouse and so on together\x01",
            "I'm planning to buy them all together.\x02\x03",
            "#02103FIf black moon holds here\x01",
            "Crossbell's back society\x01",
            "It will be totally taken over … …\x02\x03",
            "#02101FIt is going to be troublesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F……I'm with you.\x02\x03",
            "#00006FBut when I came to listen\x01",
            "I came across a big scene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FWell, this one too\x01",
            "You may as well tell it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x14,
        (
            "#5P#02105FWell, you guys of Tsao\x01",
            "You came to look for trends?\x02\x03",
            "#02102FAre you pursuing a separate matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FNo, that … …\x02\x03",
            "#00003F(Yes, Mr. Grace is\x01",
            "It seems that there was certainly an acquaintance … …)\x02\x03",
            "#00001FActually, Grace also\x01",
            "I am searching for the person I meet.\x02\x03",
            "I lost a mineral guy at a casino\x01",
            "It is a person who is Lecter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#02105FOh, is that so?\x02\x03",
            "#02103FIf that girl, at Longyuan Hotel\x01",
            "I just caught up earlier.\x02",
        )
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
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00011FWhat! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FIs it true? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#02100FYeah, with an example vacation look\x01",
            "I was sweetly eating.\x02\x03",
            "#02103FBecause I was in a hurry with coverage\x01",
            "I got drowned out, but ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x14,
        (
            "#5P#02105FWell, I can not do this.\x02\x03",
            "#02101FAt least a little more from Tsao\x01",
            "I have to listen to informed information.\x02\x03",
            "#02109F……See ya!\x01",
            "Let's eat again next time!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7B73():
        OP_93(0x101, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B73)

    def lambda_7B80():
        OP_93(0x102, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7B80)

    def lambda_7B8D():
        OP_93(0x109, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7B8D)

    def lambda_7B9A():
        OP_93(0x105, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7B9A)
    OP_95(0x14, -2000, 0, 2000, 5000, 0x0)
    OP_95(0x14, -15000, 0, 2000, 5000, 0x0)
    WaitChrThread(0x14, 1)
    Sleep(100)
    SetChrFlags(0x14, 0x80)
    OP_0D()

    ChrTalk(
        0x101,
        "#00012FOh, as usual …\x02",
    )

    CloseMessageWindow()

    def lambda_7BFF():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7BFF)
    Sleep(100)

    ChrTalk(
        0x105,
        (
            "#6P#10300FBut, in an unexpected place\x01",
            "I did not have sightings information.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7C4E():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7C4E)

    def lambda_7C5B():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C5B)

    def lambda_7C68():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7C68)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#5P#00100FYes, immediately\x01",
            "Let's go to \"Ryuuji\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FI understand.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x20)
    OP_D7(0x21)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, -6170, 0, 1400, 90)
    BeginChrThread(0x8, 0, 0, 1)
    OP_CC(0x1, 0xFF, 0x0)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    SetScenarioFlags(0x130, 2)
    OP_29(0x66, 0x1, 0x2)
    SetChrPos(0x0, -600, 0, 1560, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_30_663B end

    def Function_31_7D2F(): pass

    label("Function_31_7D2F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(23420, 1450, 3590, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_68(16170, 1450, 3590, 3000)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x5, 0x4)
    OP_78(0x5, 0x17)
    SetChrPos(0x17, 16750, 16900, 4000, 0)
    OP_D5(0x17, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 25000, 0, 650, 270)
    SetChrPos(0x102, 27000, 0, 1500, 270)
    SetChrPos(0x109, 29000, 0, 2350, 270)
    SetChrPos(0x105, 31000, 0, 2350, 270)

    def lambda_7E01():
        OP_95(0x101, 15750, 0, 1500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E01)
    Sleep(50)

    def lambda_7E1E():
        OP_95(0x102, 16750, 0, 1200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E1E)
    Sleep(50)

    def lambda_7E3B():
        OP_95(0x109, 17750, 0, 1500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7E3B)
    Sleep(50)

    def lambda_7E58():
        OP_95(0x105, 18750, 0, 2350, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7E58)
    Sleep(50)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_7E83():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E83)
    WaitChrThread(0x102, 1)

    def lambda_7E94():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E94)
    WaitChrThread(0x109, 1)

    def lambda_7EA5():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7EA5)
    WaitChrThread(0x105, 1)

    def lambda_7EB6():
        OP_93(0x105, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7EB6)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x109,
        "#12P#10111FIt really came down ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FBother, bother\x01",
            "I wonder if you were doing it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00106FAnd, let's chase anyway.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FOh, to those in the street\x01",
            "I only have to listen from one end …!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x130, 4)
    OP_29(0x66, 0x1, 0x4)
    SetChrPos(0x0, 16750, 0, 1500, 0)
    ClearMapFlags(0x10000000)
    SetChrFlags(0x17, 0x80)
    SetMapObjFlags(0x5, 0x4)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_31_7D2F end

    def Function_32_7FC8(): pass

    label("Function_32_7FC8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    EndChrThread(0x8, 0x0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis011.itp")
    OP_68(-10220, 1950, 550, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14110, 0)
    SetChrPos(0x101, -10720, 0, 1550, 135)
    SetChrPos(0x102, -9720, 0, 1550, 225)
    SetChrPos(0x109, -11320, 0, -450, 45)
    SetChrPos(0x105, -9120, 0, -450, 315)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#00106FWell, it has become somewhat longer,\x01",
            "This completes the investigation of \"The Emperor's Club\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, do not be like that.\x02",
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81F8")
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
            "◆ \"What is the investigation situation? (For testing)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【It does not change】\x01",                  # 0
            "【There is still a rest】\x01",              # 1
            "【Confirmation of 6 places ended】\x01",      # 2
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
        (0, "loc_81D1"),
        (1, "loc_81D6"),
        (2, "loc_81E7"),
        (SWITCH_DEFAULT, "loc_81F8"),
    )


    label("loc_81D1")

    Jump("loc_81F8")

    label("loc_81D6")

    ClearScenarioFlags(0x131, 5)
    ClearScenarioFlags(0x131, 6)
    ClearScenarioFlags(0x131, 7)
    ClearScenarioFlags(0x132, 2)
    Jump("loc_81F8")

    label("loc_81E7")

    SetScenarioFlags(0x131, 5)
    SetScenarioFlags(0x131, 6)
    SetScenarioFlags(0x131, 7)
    SetScenarioFlags(0x132, 2)
    Jump("loc_81F8")

    label("loc_81F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8250")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, then continue\x01",
            "We will respond to the rest of the survey.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_829D")

    label("loc_8250")

    OP_29(0x6A, 0x1, 0x6)

    ChrTalk(
        0x101,
        (
            "#00000FOK, this is the end of the survey.\x02\x03",
            "Let's return to the municipal hall.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_829D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ Mini game \"Fishing\" is now available.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Occasionally in water places such as highway and town\x01",
            "There is a \"fishing point where ripples are spreading on the water surface\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ Check fishing points\x01",
            "When you have \"fishing rod\" and \"food\" you have\x01",
            "Lloyd starts fishing.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※! When you press the ○ button quickly when the mark comes out\x01",
            "You can catch fish.\x01",
            "(Sometimes I miss it unfortunately.)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ In addition, in the city of Crossbell\x01",
            "There are fishing points in \"Port area\" and \"residential area\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, -6170, 0, 1400, 90)
    BeginChrThread(0x8, 0, 0, 1)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x132, 1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -10220, 0, 550, 180)
    EventEnd(0x5)
    Return()

    # Function_32_7FC8 end

    def Function_33_84DB(): pass

    label("Function_33_84DB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch46500.itc", 0x1E)
    LoadChrToIndex("chr/ch46600.itc", 0x1F)
    LoadChrToIndex("apl/ch51276.itc", 0x20)
    OP_68(-11420, 1650, 160, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12580, 0)
    SetChrPos(0x101, -10990, 0, 1460, 90)
    SetChrPos(0x102, -10980, 0, 290, 90)
    SetChrPos(0x104, -12450, 0, 1970, 90)
    SetChrPos(0x109, -12260, 0, 770, 90)
    SetChrPos(0x105, -12420, 0, -470, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x1F, 0x1E)
    SetChrPos(0x1F, -8340, 0, 1660, 270)
    SetChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrPos(0x1E, -8320, 0, -60, 270)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1E,
        (
            "#12404F…… you guys were having trouble.\x02\x03",
            "Before becoming a big noise thanks to\x01",
            "It seems that I was able to recover this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fmy mother……\x01",
            "Here as well\x01",
            "It was good.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x1E, 500)

    ChrTalk(
        0x1F,
        (
            "#5P#13900FHydrofluoric …… To say that it is inconvenient and it is \"this\".\x01",
            "It's like a way to handle things like things.\x02\x03",
            "#13903F… … no, that kind of treatment\x01",
            "It may not be bad with taste.\x02\x03",
            "#13912FFrom now on,\x01",
            "I will ask you with that kind of treatment, Mueller's firing\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x1F, 500)

    ChrTalk(
        0x1E,
        "#12401F#4S#500WSilence#500Wっ#500WThe#500WFiltration.#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "#5P#13910F…… Sumimasen decita.\x02",
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
    TurnDirection(0x1E, 0x102, 500)

    ChrTalk(
        0x1E,
        (
            "#12400F… … Sorry, this idiot is\x01",
            "It's a relationship I have been with sincerely.\x02\x03",
            "#12406FEvery time, how to ride\x01",
            "Because I am escalating,\x01",
            "Sometimes I must strictly discipline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00309FIt looks like she's having a hard time.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x101, 500)

    ChrTalk(
        0x1F,
        (
            "#13904FWhat do you have a friend to follow\x01",
            "I am always saved.\x02\x03",
            "#13909FHuh, this is probably the gift of the virtue of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FA: You said to Anta\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FHuff, I'm sorry\x01",
            "I feel like accumulating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#12400F… It seems like that.\x02\x03",
            "Laterally\x01",
            "Prepare for you to prepare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#5P#13911FOh my goodness.\x01",
            "It's just a joke, Muller.\x02\x03",
            "#13910F…… you also\x01",
            "Can you please do not fuck me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FOh, haha ….\x01",
            "(In a sense, it might be on good terms …).\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#12400F… … then, I will get rude.\x02\x03",
            "#12404FI was taken care of while I was busy.\x01",
            "Let me thank you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, that is our job.\x02\x03",
            "#00006FWhat is that, that … ….\x01",
            "Please take care to keep an eye on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#12406F… I got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#13910FFu, well … well …\x01",
            "Is this a fun time too?\x02\x03",
            "#13900FThis time, farewell.\x01",
            "There will be times when we meet again, we will meet again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FHaha …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#13910FWell, as me\x01",
            "Rumorous theme parks\x01",
            "I wanted to see you.\x02\x03",
            "#13905FOh, that's right.\x01",
            "Can I request a guide from now?\x02\x03",
            "#13904FHuh, it's a good idea.\x01",
            "If you spend a pleasant mood, surely\x01",
            "Muller's eyebrows wrinkles ……\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x1E, -7500, 0, 690, 2000, 0x0)
    OP_95(0x1E, -7490, 0, 1670, 2000, 0x0)
    OP_93(0x1E, 0x10E, 0x1F4)
    Sound(802, 0, 100, 0)

    ChrTalk(
        0x1F,
        (
            "#13911FOh, Muller! Is it?\x01",
            "Hawaii is just a joke?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x13B, 0x0)
    SetChrChipByIndex(0x1F, 0x20)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x20)

    def lambda_8DF4():
        OP_95(0xFE, 2000, 0, 1310, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_8DF4)
    Sleep(50)

    def lambda_8E11():
        OP_96(0xFE, 0x7D0, 0x0, 0x4F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_8E11)
    Sleep(50)

    ChrTalk(
        0x1F,
        "#11AAare ………………\x02",
    )

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x1E, 1)
    WaitChrThread(0x1F, 1)
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

    ChrTalk(
        0x101,
        (
            "#00012FSomehow somehow wonder people\x01",
            "It was.\x02\x03",
            "#00003FActually, what kind of\x01",
            "I guess they are people …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, that is\x01",
            "Even when we meet again\x01",
            "You should ask him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FTo be honest, sooo\x01",
            "I'm getting tired, but …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#00103F(Although I threatened himself,\x01",
            "That person maybe … …)\x02\x03",
            "#00109F(… … but, it is not indeed like that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#00005FWhat is wrong, Erie?\x01",
            "It seems to be silent from a while ago ….\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#11P#00102FWell, no, nothing.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00303FWell, until now\x01",
            "I guess it's about scoring one case.\x02\x03",
            "#00300FLet's go, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9130():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9130)
    Sleep(50)

    def lambda_9140():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9140)
    Sleep(300)
    OP_62(0x101)

    ChrTalk(
        0x101,
        "#11P#00000FOh, yes.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x24, 3)
    NewScene("c0100", 100, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_33_84DB end

    def Function_34_9189(): pass

    label("Function_34_9189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9197")
    Jump("loc_9550")

    label("loc_9197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_91A5")
    Jump("loc_9550")

    label("loc_91A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_91B3")
    Jump("loc_9550")

    label("loc_91B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9346")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92A4")

    ChrTalk(
        0x101,
        "#00001FThis is Crimson Shokai.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FUncle yours,\x01",
            "Since the incident at the trade meeting\x01",
            "It seems that it hurts the ringing.\x02\x03",
            "#00301FEven if I go, the information is\x01",
            "I can not get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAh……\x01",
            "Let's not go now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_932E")

    label("loc_92A4")


    ChrTalk(
        0x101,
        (
            "#00003FSince the Trade Council,\x01",
            "It seems that it is hiding the ringing.\x02\x03",
            "#00001FI will not get much information,\x01",
            "Let's not go now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_932E")

    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)
    Jump("loc_9550")

    label("loc_9346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_93E2")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FThe Crimson Chamber has one investigation department\x01",
            "You should be wary of it.\x02\x03",
            "Leave it to a department here,\x01",
            "Let's concentrate on our work.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)
    Jump("loc_9550")

    label("loc_93E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9496")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93FD")
    Call(0, 11)
    Jump("loc_9491")

    label("loc_93FD")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003FThe trend of \"red constellation\"\x01",
            "I can not get it here.\x02\x03",
            "#00000FWhile finding support requests,\x01",
            "Let's listen in each place.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)

    label("loc_9491")

    Jump("loc_9550")

    label("loc_9496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_94A4")
    Jump("loc_9550")

    label("loc_94A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_94B2")
    Jump("loc_9550")

    label("loc_94B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9550")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9550")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94D7")
    Call(0, 10)
    Jump("loc_9550")

    label("loc_94D7")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FA real estate agent now\x01",
            "He seems to be waiting for a negotiating opponent.\x02\x03",
            "Why do not you disturb us and let's go.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)

    label("loc_9550")

    Return()

    # Function_34_9189 end

    def Function_35_9551(): pass

    label("Function_35_9551")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_95A4")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems locked up.\x01",
            "There are no signs of people inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_96AC")

    label("loc_95A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_95F4")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems locked up.\x01",
            "There are no signs of people inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_96AC")

    label("loc_95F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_965A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9613")
    TalkEnd(0xFF)
    Call(0, 12)
    Return()

    label("loc_9613")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems locked up.\x01",
            "There are no signs of people inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_96AC")

    label("loc_965A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9668")
    Jump("loc_96AC")

    label("loc_9668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9676")
    Jump("loc_96AC")

    label("loc_9676")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_96AC")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems locked up.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_96AC")

    TalkEnd(0xFF)
    Return()

    # Function_35_9551 end

    def Function_36_96B0(): pass

    label("Function_36_96B0")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ Department store \"Times\" ※\x01",
            "* Only for employees ※\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_36_96B0 end

    def Function_37_9710(): pass

    label("Function_37_9710")

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
    EventEnd(0x3)
    Return()

    # Function_37_9710 end

    def Function_38_9747(): pass

    label("Function_38_9747")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FI will chase Randy -\x01",
            "Let's hurry to the site of Rubathe!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -24330, 0, 210, 90)
    EventEnd(0x4)
    Return()

    # Function_38_9747 end

    def Function_39_979E(): pass

    label("Function_39_979E")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FI will chase Randy -\x01",
            "Let's hurry to the site of Rubathe!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 19310, 0, 650, 270)
    EventEnd(0x4)
    Return()

    # Function_39_979E end

    SaveToFile()

Try(main)
