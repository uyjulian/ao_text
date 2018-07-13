from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Iris",                   # 1
        "Barker Bish",            # 2
        "Policeman",              # 3
        "Policeman",              # 4
        "Jaeger Sachs",           # 5
        "Jaeger",                 # 6
        "Real Estate Agent",      # 7
        "One-Eyed Man",           # 8
        "Redheaded Girl",         # 9
        "Lechter",                # 10
        "Jaeger Gareth",          # 11
        "車",                     # 12
        "Grace",                  # 13
        "Cao",                    # 14
        "Lau",                    # 15
        "Seire",                  # 16
        "Yuri",                   # 17
        "Sykes",                  # 18
        "Reggie",                 # 19
        "Patrol Officer Kate",    # 20
        "Patrol Officer Frantz",  # 21
        "SE制御",                 # 22
        "Mueller",                # 23
        "Olivier",                # 24
        "Central Square",         # 25
        "West Street",            # 26
        "Governmental District",  # 27
        "Residential Street",     # 28
        "Entertainment District", # 29
        "East Street",            # 30
        "Downtown",               # 31
        "Waterfront Area",        # 32
        "IBC",                    # 33
        "Station Street",         # 34
        "Back Street",            # 35
        "St. Ursula Byroad",      # 36
        "East Crossbell Highway", # 37
        "West Crossbell HIghway", # 38
        "Mainz Mountain Road",    # 39
        "Orchis Tower",           # 40
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

    PlaceName(79.5, 0.0, -9.0, 0x0000, 0x0000, "Central Square")
    PlaceName(0.0, 0.0, -76.5, 0x0000, 0x0000, "West Street")
    PlaceName(11.0, 0.0, 116.0, 0x0000, 0x0000, "Governmental District")
    PlaceName(-148.0, 0.0, -60.0, 0x0000, 0x0000, "Residential Street")
    PlaceName(-57.25, 0.0, 10.0, 0x0000, 0x0000, "Entertainment District")
    PlaceName(196.0, 0.0, 56.0, 0x0000, 0x0000, "East Street")
    PlaceName(294.0, 0.0, 31.0, 0x0000, 0x0000, "Downtown")
    PlaceName(154.0, 0.0, 158.0, 0x0000, 0x0000, "Waterfront Area")
    PlaceName(20.0, 0.0, 233.0, 0x0000, 0x0000, "IBC")
    PlaceName(168.0, 0.0, -73.0, 0x0000, 0x0000, "Station Street")
    PlaceName(1.0, 0.0, -9.0, 0x0000, 0x0000, "Back Street")
    PlaceName(200.0, 0.0, -112.0, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(240.0, 0.0, 130.0, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-52.0, 0.0, -134.0, 0x0000, 0x0000, "West Crossbell HIghway")
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
        "Function_6_2113",         # 06, 6
        "Function_7_2F7F",         # 07, 7
        "Function_8_30FD",         # 08, 8
        "Function_9_3174",         # 09, 9
        "Function_10_3200",        # 0A, 10
        "Function_11_3C14",        # 0B, 11
        "Function_12_453B",        # 0C, 12
        "Function_13_489B",        # 0D, 13
        "Function_14_49D4",        # 0E, 14
        "Function_15_4A01",        # 0F, 15
        "Function_16_4A38",        # 10, 16
        "Function_17_5BA8",        # 11, 17
        "Function_18_5C06",        # 12, 18
        "Function_19_5C07",        # 13, 19
        "Function_20_5C5D",        # 14, 20
        "Function_21_5C5E",        # 15, 21
        "Function_22_5CC3",        # 16, 22
        "Function_23_5CC4",        # 17, 23
        "Function_24_6355",        # 18, 24
        "Function_25_671E",        # 19, 25
        "Function_26_6747",        # 1A, 26
        "Function_27_67AF",        # 1B, 27
        "Function_28_6959",        # 1C, 28
        "Function_29_6D15",        # 1D, 29
        "Function_30_70AA",        # 1E, 30
        "Function_31_8990",        # 1F, 31
        "Function_32_8C46",        # 20, 32
        "Function_33_9222",        # 21, 33
        "Function_34_A00E",        # 22, 34
        "Function_35_A4D2",        # 23, 35
        "Function_36_A65E",        # 24, 36
        "Function_37_A6CD",        # 25, 37
        "Function_38_A6FF",        # 26, 38
        "Function_39_A765",        # 27, 39
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_11F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1140")

    ChrTalk(
        0xFE,
        (
            "Somehow, maybe because it's a hard time,\x01",
            "there's a weird solidarity feeling among\x01",
            "the persons of the establishment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I too have come to a point that\x01",
            "I don't care anymore to compete\x01",
            "for the top with the rival girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a hostess, entertaining\x01",
            "the guests and making\x01",
            "them drink is okay☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_11ED")

    label("loc_1140")


    ChrTalk(
        0xFE,
        (
            "I have come to a point that\x01",
            "I don't care anymore to compete\x01",
            "for the top with the rival girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a hostess, entertaining\x01",
            "the guests and making\x01",
            "them drink is okay☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11ED")

    Jump("loc_210F")

    label("loc_11F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1200")
    Jump("loc_210F")

    label("loc_1200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1389")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12EF")

    ChrTalk(
        0xFE,
        (
            "National independence...\x01",
            "Saying it has a nice ring to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The people of the establishment\x01",
            "too saw the President's speech and\x01",
            "it looks like they really enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Somehow, I became happy too♪\x01\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1384")

    label("loc_12EF")


    ChrTalk(
        0xFE,
        (
            "The people of the establishment\x01",
            "too saw the President's speech and\x01",
            "it looks like they really enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Somehow, I became happy too♪\x01\x02",
    )

    CloseMessageWindow()

    label("loc_1384")

    Jump("loc_210F")

    label("loc_1389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1397")
    Jump("loc_210F")

    label("loc_1397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1434")

    ChrTalk(
        0xFE,
        (
            "Isn't Mainz occupation\x01",
            "really a big incident...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The miners over there too\x01",
            "came to the establishment before.\x01",
            "I hope they're safe...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_210F")

    label("loc_1434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1581")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14E5")

    ChrTalk(
        0xFE,
        "Listen, listen, big news!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goodness, the establishment\x01",
            "this month's designated\x01",
            "number one is me!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, it was worth\x01",
            "it doing my best!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_157C")

    label("loc_14E5")


    ChrTalk(
        0xFE,
        (
            "Finally, I've become the number\x01",
            "one I so longed to be!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, from now on I guess\x01",
            "they will request me more and\x01",
            "more...I have to do my best!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157C")

    Jump("loc_210F")

    label("loc_1581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_15E9")

    ChrTalk(
        0xFE,
        (
            "It's noisy in the Central Square direction...\x01",
            "What, tell me, has something happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_210F")

    label("loc_15E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_174E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16F7")

    ChrTalk(
        0xFE,
        (
            "The rival girl I compete with for number of\x01",
            "nominees, in order to increase her owns,\x01",
            "called acquaintances to the store!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Eeeek, don't you think that's sly!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that things have tuned like this,\x01",
            "I too will do everything I can!!\x01\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1749")

    label("loc_16F7")


    ChrTalk(
        0xFE,
        (
            "I won't lose to\x01",
            "the rival girl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll do anything to\x01",
            "become number one!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1749")

    Jump("loc_210F")

    label("loc_174E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_18E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1849")

    ChrTalk(
        0xFE,
        (
            "Misteeer, won't you come\x01",
            "to have fun at our stooore?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Actually, now I'm competing with the rival\x01",
            "girl for nominees. The margin is narrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who wins, will be this month's number one!\x01",
            "So cooperate with me, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18E1")

    label("loc_1849")


    ChrTalk(
        0xFE,
        (
            "...Uhhm, I see. You\x01",
            "are working, eeh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, when you'll come to the store,\x01",
            "absolutely ask for me, okay?\x01",
            "Being number one is on the line here!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E1")

    Jump("loc_210F")

    label("loc_18E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_195F")

    ChrTalk(
        0xFE,
        (
            "Recently, the rival girl at the store\x01",
            "had her nominees steadily increasing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I too must not lose.\x02",
    )

    CloseMessageWindow()
    Jump("loc_210F")

    label("loc_195F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1B86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ADD")

    ChrTalk(
        0xFE,
        (
            "Orchis Tower...\x01",
            "It's a very magnificent building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I sneaked away from work for a bit\x01",
            "and went to see the inauguration\x01",
            "and I was dumbfounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There must be no other people who\x01",
            "have an incredible view like those\x01",
            "working at such a place, for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you come for business entertainment to our\x01",
            "store, I absolutely want you to ask for me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B81")

    label("loc_1ADD")


    ChrTalk(
        0xFE,
        (
            "Orchis Tower...\x01",
            "It's a very magnificent building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There must be no other people who\x01",
            "have an incredible view like those\x01",
            "working at such a place, for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B81")

    Jump("loc_210F")

    label("loc_1B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1D37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C8E")

    ChrTalk(
        0xFE,
        (
            "I heard it from a customer; it seems\x01",
            "that tomorrow the Trade Conference \x01",
            "is going to be held from the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it doesn't appear to be a\x01",
            "festival like the anniversary one...\x01",
            "I wonder what kind of event is going to be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D32")

    label("loc_1C8E")


    ChrTalk(
        0xFE,
        (
            "Oopsie, no, I mustn't.\x01",
            "It's nothing I have to mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now I must think to increase my\x01",
            "nominees as many as possible,\x01",
            "in order to not lose to the rival girl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D32")

    Jump("loc_210F")

    label("loc_1D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_1EF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E42")

    ChrTalk(
        0xFE,
        (
            "Just before, a big and \x01",
            "brawny old man with red\x01",
            "hair was around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Together with him there were a cute\x01",
            "girl who looked like a cat and a\x01",
            "mister who plainly looked like a playboy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, it somehow\x01",
            "was an odd scene.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EF3")

    label("loc_1E42")


    ChrTalk(
        0xFE,
        (
            "Now that I think about it,\x01",
            "even the mister I saw just some\x01",
            "time ago had the same hair color.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could they all be family?\x01",
            "Although they didn't quite resemble each other.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EF3")

    Jump("loc_210F")

    label("loc_1EF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1FAE")

    ChrTalk(
        0xFE,
        (
            "Is it true that the whole place in\x01",
            "the back of the alley was sold?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before, there were some scaaary men in black...\x01",
            "I wonder what kind of people will move in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_210F")

    label("loc_1FAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_210F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2064")

    ChrTalk(
        0xFE,
        "Teehee, I'm Iris☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Misteeer, won't you come\x01",
            "to have fun at our stooore?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why don't you pass time pleasantly\x01",
            "drinking and chatting with me?㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_210F")

    label("loc_2064")


    ChrTalk(
        0xFE,
        (
            "Recently my nominees have gone\x01",
            "up and I'm very satisfied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll establish a lead on the rival girl,\x01",
            "and eventually I'll become number\x01",
            "one for number of nominees!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_210F")

    TalkEnd(0xFE)
    Return()

    # Function_5_FF8 end

    def Function_6_2113(): pass

    label("Function_6_2113")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_221A")

    ChrTalk(
        0xFE,
        (
            "Mister, mister,  won't\x01",
            "you stop by our store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're currently having a hyper happy sale\x01",
            "to commemorate President Dieter's restriction!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Keep it a secret that we had a sale for\x01",
            "commemorating the independence too, 'k?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_22D0")

    label("loc_221A")


    ChrTalk(
        0xFE,
        (
            "We're currently having a hyper happy sale\x01",
            "to commemorate President Dieter's restriction!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Keep it a secret that we had a sale for\x01",
            "commemorating the independence too, 'k?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D0")

    Jump("loc_2F7B")

    label("loc_22D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_22E3")
    Jump("loc_2F7B")

    label("loc_22E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_23BB")

    ChrTalk(
        0xFE,
        (
            "Mister, mister,  we're currently having\x01",
            "a super happy sale to commemorate\x01",
            "the independence at our store!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's Crossbell daybreak, so there\x01",
            "won't be any harm in spending\x01",
            "time with a cute girl!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F7B")

    label("loc_23BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2477")

    ChrTalk(
        0xFE,
        (
            "Mister, mister, our store too\x01",
            "has reopened business recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why don't you come to drink, play,\x01",
            "heal body and soul, fatigued by the\x01",
            "repair works, with cute girls?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F7B")

    label("loc_2477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2514")

    ChrTalk(
        0xFE,
        (
            "An occupation incident...\x01",
            "What a terrible thing happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even I, in such a situation, am not\x01",
            "in the mood to actively do the barker.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F7B")

    label("loc_2514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_25D1")

    ChrTalk(
        0xFE,
        (
            "Man, it's raining again. Customers\x01",
            "are also few. That's painful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say that yesterday there was a huge accident, \x01",
            "so I can't do anything if business is not good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F7B")

    label("loc_25D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_263D")

    ChrTalk(
        0xFE,
        (
            "Heck, it's noisy with all\x01",
            "the sirens from the square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did an incident happen again?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F7B")

    label("loc_263D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_27D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2735")

    ChrTalk(
        0xFE,
        (
            "Today, our store is having\x01",
            "the customary happy sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The cute girls are going\x01",
            "to welcome you in even\x01",
            "cuter dresses!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you let it go today, I don't\x01",
            "know when we'll do it again!\x01",
            "Come on, come on, follow me!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_27CE")

    label("loc_2735")


    ChrTalk(
        0xFE,
        (
            "Today, our store is having\x01",
            "the customary happy sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you let it go today, I don't\x01",
            "know when we'll do it again!\x01",
            "Come on, come on, follow me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27CE")

    Jump("loc_2F7B")

    label("loc_27D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_289A")

    ChrTalk(
        0xFE,
        (
            "Recently with the independence and all,\x01",
            "it's just one complicated thing after the other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right because times are like this,\x01",
            "come to our store to relax!\x01",
            "We'll make you happy♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F7B")

    label("loc_289A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_295E")

    ChrTalk(
        0xFE,
        (
            "Even the police guys I saw\x01",
            "on main street looked like\x01",
            "they were doing their best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People tired from work are the target of barking.\x01",
            "Eh eh, later I'll try to speak to them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F7B")

    label("loc_295E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2A05")

    ChrTalk(
        0xFE,
        (
            "It appears that VIPs from all the\x01",
            "countries have come to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they were to come to drink at our\x01",
            "store it would make a nice publicity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F7B")

    label("loc_2A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2AD9")

    ChrTalk(
        0xFE,
        (
            "The Crimson & Co.'s men who took\x01",
            "home on the place in the back\x01",
            "all look like cheerful people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eh eh, I'll introduce them some cute girls and\x01",
            "I'll get ourselves some new regular customers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F7B")

    label("loc_2AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_2BDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B7B")

    ChrTalk(
        0xFE,
        (
            "Oh my, this won't do.\x01",
            "It turned into a rainfall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I won't be able to get anyone anymore today.\x01",
            "I guess it's time to pull out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2BD5")

    label("loc_2B7B")


    ChrTalk(
        0xFE,
        (
            "...A red-headed mister?\x01",
            "It seems he went in the back\x01",
            "alley over there some time ago.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BD5")

    Jump("loc_2F7B")

    label("loc_2BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2C4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF5")
    Call(0, 7)
    Jump("loc_2C4A")

    label("loc_2BF5")


    ChrTalk(
        0xFE,
        (
            "On rainy days, you can't\x01",
            "quite pull customers in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Boy, that's troublesome.\x02",
    )

    CloseMessageWindow()

    label("loc_2C4A")

    Jump("loc_2F7B")

    label("loc_2C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2F7B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D4C")

    ChrTalk(
        0xFE,
        (
            "The mister who passed through here before\x01",
            "and went in the Entertainment District direction...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow I have a feeling\x01",
            "I saw that man before\x01",
            "around here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, maybe it's just my imagination.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2E10")

    label("loc_2D4C")


    ChrTalk(
        0xFE,
        (
            "If you're looking for the red-headed mister, he was \x01",
            "walking towards the Entertainment District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have a feeling I saw him\x01",
            "around here before, but...\x01",
            "Well, it's my imagination I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E10")

    Jump("loc_2F7B")

    label("loc_2E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E27")
    Call(0, 7)
    Jump("loc_2F7B")

    label("loc_2E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F3F")

    ChrTalk(
        0xFE,
        (
            "Eh eh, my bad.\x01",
            "Please let it slide just for this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like, I can give you as present a service \x01",
            "ticket for the next time you come to the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWe don't need it.\x01",
            "...Bribery too is a serious crime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eh eh, I'm no\x01",
            "match for you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2F7B")

    label("loc_2F3F")


    ChrTalk(
        0xFE,
        (
            "Eh eh, my bad.\x01",
            "Please let it slide just for this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F7B")

    TalkEnd(0xFE)
    Return()

    # Function_6_2113 end

    def Function_7_2F7F(): pass

    label("Function_7_2F7F")


    ChrTalk(
        0x9,
        (
            "Oh, you misters,\x01",
            "are you free now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At our stores there're\x01",
            "a lot of cuties!\x01",
            "Say, wanna drop by? Eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F...Coercive barking is an illegal act, you know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't say such a stuffy...wait,\x01",
            "are you guys from the police?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Eh eh, my bad.\x01",
            "Please let it slide just for this time, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(*sigh*...public security is poor\x01",
            "around these parts as always.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 2)
    Return()

    # Function_7_2F7F end

    def Function_8_30FD(): pass

    label("Function_8_30FD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "At present, this building is under \x01",
            "investigation by Section One.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I ask you to refrain from entering.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_30FD end

    def Function_9_3174(): pass

    label("Function_9_3174")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Damn Red Constellation guys,\x01",
            "what a crazy thing they pulled out.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It would be nice if the incident\x01",
            "would be solved fast...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_3174 end

    def Function_10_3200(): pass

    label("Function_10_3200")

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
            "#12P#00001FThis place is...\x01",
            "What remains of Revache & Co.\x02\x03",
            "#00003FIt should be an empty shell now...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Man's Voice",
        (
            "Hey you, what're\x01",
            "you doing there?\x02",
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

    def lambda_33BE():

        label("loc_33BE")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_33BE")

    QueueWorkItem2(0x101, 2, lambda_33BE)

    def lambda_33D0():

        label("loc_33D0")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_33D0")

    QueueWorkItem2(0x102, 2, lambda_33D0)

    def lambda_33E2():

        label("loc_33E2")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_33E2")

    QueueWorkItem2(0x109, 2, lambda_33E2)

    def lambda_33F4():

        label("loc_33F4")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_33F4")

    QueueWorkItem2(0x105, 2, lambda_33F4)

    def lambda_3406():
        OP_95(0xFE, 0, 0, 33500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3406)
    WaitChrThread(0xE, 1)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0x101,
        "#00005FUhmmm, you are...?\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)

    NpcTalk(
        0xE,
        "Man",
        (
            "#12P*cough*, I am someone who runs a\x01",
            "real estate agency in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Man",
        (
            "#12PThis was consigned to me by the autonomous\x01",
            "state government and I was entrusted the\x01",
            "entire place management.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Man",
        (
            "#12PYou'll cause me troubles if you\x01",
            "enter the site as you please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00103FThe government consigned...\x01",
            "Now that I think about it, I had heard\x01",
            "such a story from grandfather too.\x02\x03",
            "#00100FBecause they can't leave alone even for\x01",
            "an instant the things the mafia possessed,\x01",
            "he said it was quickly decided their consign.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FI see...\x02\x03",
            "#00000FUhmm, we're sorry for the inconvenience,\x01",
            "we're from the Crossbell Police.\x02\x03",
            "We're currently patrolling\x01",
            "inside the city a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12POh, you're police officers?\x01",
            "Thank you for patrolling even this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10100FEhhm, so today are you making a periodic\x01",
            "inspection for this building or something else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PWell...\x01",
            "Actually, this building has been decided\x01",
            "to be put on sale before long.\x02",
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
        "#5P#00005FThe entire thing is on sale...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PYeah, for a long time a few enterprises\x01",
            "have put out a moving into desire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PBecause today too one of those plans to come\x01",
            "to negotiate, I'm waiting here for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10105FEnterprises issuing moving into desire for\x01",
            "something that formerly belonged to the mafia...?\x02\x03",
            "#10106FWell, saying it like that is...you know...\x01",
            "Is it going to be all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12PWell, we too are somewhat worried, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PAfter all, it's this kind of building.\x01",
            "Even just the management costs are to not be sneezed at.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PIf someone wants to do us the favor to take it,\x01",
            "we too have no reason to turn them down, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10303FWell, as a trader, wanting\x01",
            "to sell it at once it's\x01",
            "a natural sentiment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FYeah, although it worries me...\x02\x03",
            "#00000FWe're also in the way here,\x01",
            "so, should we go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00103FYes...let's go.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xE, 0x8)
    SetChrPos(0x0, 90, 0, 80, 180)
    SetScenarioFlags(0x139, 1)
    EventEnd(0x5)
    Return()

    # Function_10_3200 end

    def Function_11_3C14(): pass

    label("Function_11_3C14")

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

    def lambda_3D5E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D5E)

    def lambda_3D6F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3D6F)

    def lambda_3D80():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3D80)

    def lambda_3D91():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3D91)

    def lambda_3DA2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3DA2)

    def lambda_3DB3():
        OP_95(0xFE, -600, 0, 34200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DB3)

    def lambda_3DCD():
        OP_95(0xFE, 600, 0, 34200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3DCD)

    def lambda_3DE7():
        OP_95(0xFE, 0, 0, 36000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3DE7)

    def lambda_3E01():
        OP_95(0xFE, -1200, 0, 33000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3E01)

    def lambda_3E1B():
        OP_95(0xFE, 1200, 0, 33000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3E1B)
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
        "Oh, you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Ooh, if it isn't Captain Randolph!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Ha ha, did you come today too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001F(Red Constellation jaegers...\x01",
            "They seem to be Randy's acquaintances.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F...Sachs, it looks like your new comfortable\x01",
            "headquarters is quite nice, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Ha ha, thank goodness it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The Entertainment District branch store of "Neue-Blanc"\x01",
            "is close too, so it's quite convenient to use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FHah...you did a good job, as always.\x02\x03",
            "#00301F...Aren't uncle and Shirley here today too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah, today too the boss and the\x01",
            "missus went out for business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you have some message I'll\x01",
            "convey it for you, what about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00303F...No, sorry for have bothered you.\x02",
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
        "#6P#00005FY-Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Thank you, for all your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Eh eh, see ya soon, Captain.\x02",
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
            "#00303F...Hmph.\x01",
            "It seems they're pretendin' to be out again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105F"Again" you say...\x01",
            "Did you visit here recently?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00303FHe said he had something to talk 'bout,\x01",
            "but that was the last I've heard of 'im.\x02\x03",
            "#00301FAnyway, it appears that even\x01",
            "if I'm the one to go meet 'im,\x01",
            "he's got no intention to show up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FHm, it could be that before\x01",
            "long some kind of contact or\x01",
            "other will come from him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10106FBut, if that's the case...\x01",
            "We can only inquire steadily\x01",
            "about the Red Constellation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, let's try going around various places\x01",
            "while taking care of support requests.\x02",
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

    # Function_11_3C14 end

    def Function_12_453B(): pass

    label("Function_12_453B")

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
            "#00003F...It looks like it's locked.\x02\x03",
            "#00001FSection One investigation is over in general too,\x01",
            "so there shouldn't be anyone inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FDisappearing with such an airship...\x01",
            "I wonder where're they hiding now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FIt appears that even the CGF is\x01",
            "being strictly vigilant about them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F............\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)
    Sleep(50)

    ChrTalk(
        0x103,
        "#12P#00200FMr. Randy...\x02",
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
        "#6P#10308F...Are you all right?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)
    OP_93(0x104, 0xB4, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#00304F...Ha ha, don't worry.\x02\x03",
            "#00301FIt's just...that we must settle things once\x01",
            "and for all the next time we meet them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FYeah...you're right.\x02",
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

    # Function_12_453B end

    def Function_13_489B(): pass

    label("Function_13_489B")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_495F")
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x8000)
    EndChrThread(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, -8800, 0, 3100, 90)
    SetChrPos(0x8, -7300, 0, 3100, 270)

    label("loc_495F")

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

    # Function_13_489B end

    def Function_14_49D4(): pass

    label("Function_14_49D4")

    SetChrPos(0xFE, 18000, 0, 500, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -37000, 0, 500)
    OP_9F(0x2, 0xFE, 5000, 0x6)
    Return()

    # Function_14_49D4 end

    def Function_15_4A01(): pass

    label("Function_15_4A01")

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

    # Function_15_4A01 end

    def Function_16_4A38(): pass

    label("Function_16_4A38")

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
        "#00013F#6P(......!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6P(...Ah...)\x02",
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
        "#00311F#2753V#6P#30W──Uncle, Shirley.\x02",
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
            "#3941V#5P#20WAhahah.\x01",
            "Long time no see, Randy bro!\x02",
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
            "#3834V#11P#30WTwo years, eh?\x01",
            "It looks like you haven't changed.\x02",
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

    def lambda_4F6B():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4F6B)
    Sleep(50)

    def lambda_4F83():
        OP_9B(0x0, 0x102, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4F83)
    Sleep(50)

    def lambda_4F9B():
        OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4F9B)
    Sleep(50)

    def lambda_4FB3():
        OP_9B(0x0, 0x109, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4FB3)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00007F#6P...Randy...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#6P#NThe persons f-from yesterday...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        "#10303F#6P#NSuspicious guys all appearing together, eh?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x11,
        (
            "#03509F#5PHa ha, then you're this old man's\x01",
            "family like I thought, eh?\x02\x03",
            "#03502FBecause you have the same exactly red\x01",
            "hair I thought that could be the case, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#6P............\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00013F#6PCaptain Lechter...\x01",
            "Why are you here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6PAre you somehow related\x01",
            "to this purchase?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#03504F#5PYeah, a bit of monkey business.\x02\x03",
            "#03510FMaaan, thank goodness we anticipated\x01",
            "that Heiyue-something four eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#04609F#11PUh uh, I can't wait!\x02\x03",
            "#04602FThat time at the Eastern District I\x01",
            "had to retreat, but this time it seems\x01",
            "I'll be able to play all I want!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00005F#6PThe Eastern District...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6PThe "war" you waged last year\x01",
            "at the Heiyue in Calvard, huh?\x02\x03",
            "#00311F──Say, uncle.\x01",
            "Why have you come to Crossbell?\x02\x03",
            "What the hell are you plannin' to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04504F#11PEh eh...\x01",
            "Business, ain't it obvious?\x02\x03",
            "#04500FMore importantly, Randolph.\x01",
            "I have something to tell you.\x02\x03",
            "──Big bro is dead.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00305F#6P#40W#2S......What.........\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6P!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04503F#11PIt happened about half a year ago.\x02\x03",
            "The boss of "Zephyr" and he killed each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#04602F#11PThe decisive duel between the "War God"\x01",
            "and the "Jaeger King", who had been old\x01",
            "enemies for many years!\x02\x03",
            "#04612FJeez, it was really amazing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00308F#6P#40W............\x02\x03",
            "#00304F#40W...Ha ha...I see...\x02\x03",
            "#30WThat old fart...he died while\x01",
            "fightin' until the end.\x02\x03",
            "#00300F#40W...He looked satisfied, I bet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#04602F#11PYes!\x01",
            "He looked like he had a ton of fun!\x02\x03",
            "#04606FHow nice, Shirley too wishes\x01",
            "she had an opponent like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04504F#11PWell, I guess that big bro had no regrets.\x02\x03",
            "#04501F──Aside from having an unworthy\x01",
            "son wandering somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#6P......!\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xF,
        (
            "#04504F#5PYour vacation is over, Randolph.\x02\x03",
            "#04502FWe'll talk soon, so\x01",
            "make time for me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x10,
        "#04609F#11PSee you later, Randy bro!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x11,
        "#03509F#5PThen, goodbye.\x02",
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
        "#00108F#6P#N...Randy...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10113F#6P#NSenior Randy...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00008F#6PAre those two your...?\x02",
    )

    CloseMessageWindow()
    OP_64(0x104)
    Sleep(500)

    ChrTalk(
        0x104,
        "#00306F#5P#30WYeah...\x02",
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
            "#00303F#11P#30WSigmund Orlando, the\x01",
            ""Red Constellation" vice leader.\x02\x03",
            "And that girl is Shirley Orlando,\x01",
            "one of the commanding officers.\x02",
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
            "#00311F#11P#30WMy uncle and cousin...\x01",
            "──The worst of the worst ogres.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5A93")
    Jump("loc_5A98")

    label("loc_5A93")

    OP_29(0x67, 0x4, 0x40)

    label("loc_5A98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5AA9")
    Jump("loc_5AAE")

    label("loc_5AA9")

    OP_29(0x6D, 0x4, 0x40)

    label("loc_5AAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5ABF")
    Jump("loc_5AC4")

    label("loc_5ABF")

    OP_29(0x6E, 0x4, 0x40)

    label("loc_5AC4")

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

    # Function_16_4A38 end

    def Function_17_5BA8(): pass

    label("Function_17_5BA8")

    OP_95(0xFE, 0, 0, 42270, 2000, 0x0)
    OP_95(0xFE, 0, 300, 43640, 2000, 0x0)
    Sound(103, 0, 100, 0)
    OP_71(0x2, 0x1, 0xA, 0x1, 0x0)
    Sleep(500)

    def lambda_5BEA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5BEA)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
    Return()

    # Function_17_5BA8 end

    def Function_18_5C06(): pass

    label("Function_18_5C06")

    Return()

    # Function_18_5C06 end

    def Function_19_5C07(): pass

    label("Function_19_5C07")

    Sleep(1500)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 0, 0, 42270, 2000, 0x0)
    OP_95(0xFE, 0, 300, 43640, 2000, 0x0)

    def lambda_5C41():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5C41)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
    Return()

    # Function_19_5C07 end

    def Function_20_5C5D(): pass

    label("Function_20_5C5D")

    Return()

    # Function_20_5C5D end

    def Function_21_5C5E(): pass

    label("Function_21_5C5E")

    Sleep(2000)
    OP_93(0xFE, 0x2D, 0x1F4)
    OP_95(0xFE, 0, 0, 42270, 2000, 0x0)
    OP_95(0xFE, 0, 300, 43640, 2000, 0x0)

    def lambda_5C95():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5C95)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0xA, 0x0, 0x1, 0x0)
    Return()

    # Function_21_5C5E end

    def Function_22_5CC3(): pass

    label("Function_22_5CC3")

    Return()

    # Function_22_5CC3 end

    def Function_23_5CC4(): pass

    label("Function_23_5CC4")

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
    OP_8E(0x10, "Shirley")
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
            "#04602F#3973V#5P#30WUwaaah!\x01",
            "That building is out of this world!\x02\x03",
            "#04612F#3974VHey, hey, can Shirley and the\x01",
            "others wreck it down?\x02",
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
            "#04504F#5PHu hu...\x01",
            "I understand how you feel, but stop.\x02\x03",
            "#04500FBefore too long, I intend to have a\x01",
            "use for that building for us too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    ChrTalk(
        0x10,
        (
            "#04606F#11PMrr, too bad.\x02\x03",
            "#04602FOh, whatever, I'm going to\x01",
            "stroll about the city, ok?\x02\x03",
            "#04612FThanks to that building it\x01",
            "appears it's really lively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#04504F#5PYeah, you can go.\x02",
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

    def lambda_609C():
        OP_9D(0xFE, 0x0, 0x1450, 0x1DB0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_609C)
    Sleep(300)

    def lambda_60BC():

        label("loc_60BC")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_60BC")

    QueueWorkItem2(0xF, 2, lambda_60BC)

    def lambda_60CE():

        label("loc_60CE")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_60CE")

    QueueWorkItem2(0x12, 2, lambda_60CE)

    def lambda_60E0():

        label("loc_60E0")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_60E0")

    QueueWorkItem2(0xC, 2, lambda_60E0)
    WaitChrThread(0x10, 1)
    Sound(62, 0, 100, 0)
    OP_92(0x10, 0x0, 0x1004, 0x1F4)

    def lambda_6109():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6109)
    WaitChrThread(0x10, 1)
    Sound(844, 0, 50, 0)
    SetChrSubChip(0x10, 0x2)

    def lambda_6131():
        OP_9D(0xFE, 0x0, 0x0, 0xE10, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6131)
    WaitChrThread(0x10, 1)
    EndChrThread(0xF, 0x2)
    EndChrThread(0x12, 0x2)
    EndChrThread(0xC, 0x2)
    SetChrFlags(0x10, 0x80)
    Sleep(300)

    ChrTalk(
        0xC,
        "#5PHa ha...typical of the missus.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PShe really liked that\x01",
            "building, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04504F#5PHu hu, that is also true.\x02\x03",
            "#04502FBut more than that──\x01",
            "She probably was intoxicated\x01",
            "by a blood presentiment.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xF, 500)

    ChrTalk(
        0xC,
        "#6P......!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0xF, 500)

    ChrTalk(
        0x12,
        (
            "#12P......I see.\x01",
            "Typical of the young miss.\x02",
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
            "#04504F#5PEh eh...she really is my daughter.\x02\x03",
            "#04502FIt appears that tomorrow she'll\x01",
            "be able to fully enjoy herself.\x02",
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

    # Function_23_5CC4 end

    def Function_24_6355(): pass

    label("Function_24_6355")

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

    def lambda_6531():
        OP_95(0xFE, 10, 0, 39370, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6531)
    Sleep(30)

    def lambda_654E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_654E)
    Sleep(30)

    def lambda_6566():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6566)
    Sleep(50)

    def lambda_657E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_657E)
    Sleep(30)

    def lambda_6596():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6596)

    def lambda_65AB():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_65AB)
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

    def lambda_6629():
        OP_95(0xFE, 10, 0, 43000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6629)
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

    def lambda_668E():
        OP_95(0xFE, 0, 0, 45000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_668E)

    def lambda_66A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_66A8)
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

    # Function_24_6355 end

    def Function_25_671E(): pass

    label("Function_25_671E")

    OP_95(0xFE, 0, 0, 650, 5000, 0x0)
    OP_95(0xFE, 0, 0, 6000, 5000, 0x0)
    Return()

    # Function_25_671E end

    def Function_26_6747(): pass

    label("Function_26_6747")


    def lambda_674C():
        OP_95(0xFE, 0, 0, 39370, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_674C)
    WaitChrThread(0xFE, 1)

    def lambda_676A():
        OP_95(0xFE, 0, 0, 43670, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_676A)
    WaitChrThread(0xFE, 1)

    def lambda_6788():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6788)

    def lambda_6799():
        OP_95(0xFE, 0, 0, 45000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6799)
    Return()

    # Function_26_6747 end

    def Function_27_67AF(): pass

    label("Function_27_67AF")

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
            "#00001F#5PIt looks like...\x01",
            "There's no one here anymore\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#6PThe police should've\x01",
            "left it at least locked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PHe's called us here on purpose,\x01",
            "so he has picked the lock too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F#11PAt any rate, let's enter.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 34000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x182, 3)
    EventEnd(0x5)
    Return()

    # Function_27_67AF end

    def Function_28_6959(): pass

    label("Function_28_6959")

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
            "#02101FHmm...\x01",
            "At last they've started to move.\x02\x03",
            "#02103FSince it's something connected,\x01",
            "would it be ok to make it into an article?\x02\x03",
            "#02101FEven pressure from the Republican Faction\x01",
            "has decreased recently, but...\x02",
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
            "#00005FMiss Grace...\x01",
            "What're you doing?\x02",
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

    def lambda_6C06():
        OP_93(0x14, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6C06)

    def lambda_6C13():
        OP_95(0x101, 850, 0, 1360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C13)
    Sleep(100)

    def lambda_6C30():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C30)
    Sleep(100)

    def lambda_6C48():
        OP_95(0x105, 0, 0, 360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6C48)
    Sleep(100)

    def lambda_6C65():
        OP_9B(0x0, 0x109, 0x0, 0x1194, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6C65)
    WaitChrThread(0x109, 1)

    def lambda_6C7E():
        OP_95(0x109, 1300, 0, 260, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6C7E)
    Sleep(100)
    OP_6F(0x79)
    WaitChrThread(0x102, 1)

    def lambda_6CA1():
        OP_95(0x102, -600, 0, 1560, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6CA1)
    WaitChrThread(0x101, 1)

    def lambda_6CBF():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6CBF)

    def lambda_6CCC():
        OP_93(0x14, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6CCC)
    WaitChrThread(0x109, 1)

    def lambda_6CDD():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6CDD)
    Sleep(200)
    WaitChrThread(0x105, 1)

    def lambda_6CF1():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6CF1)
    Sleep(200)
    WaitChrThread(0x102, 1)

    def lambda_6D05():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6D05)
    WaitChrThread(0x105, 1)
    Call(0, 30)
    Return()

    # Function_28_6959 end

    def Function_29_6D15(): pass

    label("Function_29_6D15")

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
            "#12P#02101FHmm...\x01",
            "At last they've started to move.\x02\x03",
            "#02103FSince it's something connected,\x01",
            "would it be ok to make it into an article?\x02\x03",
            "#02101FEven pressure from the Republican Faction\x01",
            "has decreased recently, but...\x02",
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
            "#00005FMiss Grace...\x01",
            "What're you doing?\x02",
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

    def lambda_6FC6():
        TurnDirection(0x14, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6FC6)

    def lambda_6FD3():
        OP_95(0x101, 850, 0, 1360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6FD3)
    Sleep(100)

    def lambda_6FF0():
        OP_95(0x102, -600, 0, 1560, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6FF0)
    Sleep(100)

    def lambda_700D():
        OP_95(0x109, 1300, 0, 260, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_700D)
    Sleep(100)

    def lambda_702A():
        OP_95(0x105, 0, 0, 360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_702A)
    Sleep(1000)

    def lambda_7047():
        OP_93(0x14, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7047)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)

    def lambda_705A():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_705A)

    def lambda_7067():
        OP_93(0x14, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7067)
    WaitChrThread(0x102, 1)

    def lambda_7078():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7078)
    WaitChrThread(0x109, 1)

    def lambda_7089():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7089)
    WaitChrThread(0x105, 1)

    def lambda_709A():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_709A)
    WaitChrThread(0x105, 1)
    Call(0, 30)
    Return()

    # Function_29_6D15 end

    def Function_30_70AA(): pass

    label("Function_30_70AA")

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
            "O-Oh...\x01",
            "If it isn't Lloyd and the others.\x02\x03",
            "I see, the Special Support\x01",
            "Section has finally\x01",
            "restarted operations, eh?\x02",
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
        "#6P#00000FYes, thank goodness it has.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FAs for Tio and Randy, they\x01",
            "are going to rejoin us later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#02100FI see, it's a bit of a pity.\x02\x03",
            "#02106FAnyway, who could've thought that Wazy \x01",
            "would've joined the Support Section, eh?\x02\x03",
            "#02102FBig sis here was really startled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHu hu, I'm glad you were surprised.\x02\x03",
            "#10304FIf you like, I won't mind you putting\x01",
            "together a special feature article.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00006FHey now...\x02",
    )

    CloseMessageWindow()
    OP_93(0x14, 0xB4, 0x0)

    ChrTalk(
        0x14,
        (
            "#02109FHu hu, seems fun, no?\x02\x03",
            "#02106FIf possible I'd like to talk about many things,\x01",
            "but now I'm a liiittle busy.\x02\x03",
            "#02102FAfter I'm finished, then, at leisure──\x02",
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
        "Young Man's Voice",
        "#NMy, what a rare ensemble.\x02",
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

    def lambda_7565():
        OP_98(0x15, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7565)
    Sleep(50)

    def lambda_7582():
        OP_98(0x16, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_7582)
    Sleep(50)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#N#00005FAh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#3P#N#00101FBranch Manager Cao...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x14,
        "#12P#N#02106F...Damn.\x02",
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
            "Long time no see.\x01",
            "Mr. Lloyd, Miss Elie.\x02\x03",
            "And also── Wazy and\x01",
            "Master Sergeant Noｱl, is it?\x02",
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
        "#6P#10111FH-How do you...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FEeh... You really have an \x01",
            "impressive information network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03204FHu hu, since you're the Special\x01",
            "Support Section, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x10E, 0x1F4)

    ChrTalk(
        0x15,
        (
            "#03200FAnyway, who could've thought that Miss Grace\x01",
            "would've been able to catch our moves.\x02\x03",
            "#03209FThat's the renowned\x01",
            "Crossbell Times for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#02109FN-Nooo...\x01",
            "It's a coincidence. Yes, a coincidence!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FWhat in the world\x01",
            "are you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FWhat business do you have\x01",
            "on the old Revache site?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0xB4, 0x1F4)

    ChrTalk(
        0x15,
        (
            "#03200FHa ha, isn't it obvious?\x02\x03",
            "#03204FIt's quite a waste to let this plot\x01",
            "of land unutilised in this way.\x02\x03",
            "#03202FSo my company has thought\x01",
            "to utilise it effectively.\x02",
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
        "#6P#00001F......!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03203FHu hu, normally, putting hands on\x01",
            "things related to the mafia is hard.\x02\x03",
            "#03210FHowever, in our case, we're somewhat\x01",
            "used to these kind of things.\x02\x03",
            "#03204FEven the contractor would've a headache\x01",
            "every month for the management costs,\x01",
            "and so it seems we'll have a good deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00010FKh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#02101F...Mmh, Mr. Cao.\x01",
            "Can I put such info in an article?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03200FYes, I don't mind.\x01",
            "It's nothing to be ashamed of.\x02\x03",
            "#03204FAlthough, I'd like you to cut us some slack\x01",
            "and declare that's just speculation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#02109FA-Ahaha...\x01",
            "Of course, I'll keep that in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03200FHu hu, then I'll excuse myself.\x02\x03",
            "Mr. Lloyd, if something happens,\x01",
            "please come to our company.\x02\x03",
            "#03204F...Let's go, Lau.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Sir.\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x0)

    def lambda_7DE3():
        OP_9B(0x1, 0x101, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7DE3)
    Sleep(50)

    def lambda_7DFB():
        OP_9B(0x1, 0x102, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7DFB)

    def lambda_7E10():
        OP_9B(0x1, 0x109, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7E10)
    Sleep(50)

    def lambda_7E28():
        OP_9B(0x1, 0x105, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7E28)
    Sleep(50)

    def lambda_7E40():
        OP_95(0x15, -2500, 0, 1660, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7E40)
    Sleep(500)
    OP_96(0x16, 0x0, 0x0, 0x898, 0x7D0, 0x0)

    def lambda_7E71():
        OP_95(0x15, -12000, 0, 1660, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7E71)

    def lambda_7E8B():
        OP_95(0x16, -12000, 0, 1560, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_7E8B)

    def lambda_7EA5():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7EA5)
    Sleep(50)

    def lambda_7EB5():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7EB5)
    Sleep(50)

    def lambda_7EC5():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7EC5)
    Sleep(50)

    def lambda_7ED5():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7ED5)
    Sleep(50)

    def lambda_7EE5():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7EE5)
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
        "#12P#00001F............\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7117", 0)

    ChrTalk(
        0x109,
        (
            "#12P#10101FH-He's an incredible man.\x02\x03",
            "#10106FI felt like a frog being\x01",
            "watched by a snake...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00103FRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FThe youngest of all the Heiyue leaders,\x01",
            "the "White Orchid Dragon", Cao Lee.\x02\x03",
            "#10306FHe looks like a shrewder man than rumor goes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FYeah, he's always like that.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(240, 1750, 1140, 3000)
    MoveCamera(326, 26, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(12930, 3000)

    def lambda_8100():
        OP_93(0x14, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8100)

    def lambda_810D():
        OP_95(0x101, 500, 0, 2660, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_810D)
    Sleep(100)

    def lambda_812A():
        OP_95(0x102, -710, 0, 1990, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_812A)
    Sleep(100)

    def lambda_8147():
        OP_95(0x109, 900, 0, 1300, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8147)
    Sleep(100)

    def lambda_8164():
        OP_95(0x105, -270, 0, 760, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8164)
    WaitChrThread(0x101, 1)

    def lambda_8182():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8182)
    WaitChrThread(0x102, 1)

    def lambda_8193():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8193)
    WaitChrThread(0x109, 1)

    def lambda_81A4():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_81A4)
    WaitChrThread(0x105, 1)

    def lambda_81B5():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_81B5)
    OP_6F(0x79)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#12P#00001F──Miss Grace.\x01",
            "Do the Heiyue want to buy the Revache old site?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#02101FYes, it seems they intend to purchase\x01",
            "even the warehouses, all in one go.\x02\x03",
            "#02103FIf the Heiyue seize this place,\x01",
            "Crossbell underground society will\x01",
            "become completely in their hands...\x02\x03",
            "#02101FIt seems it'll be something troublesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F...I agree.\x02\x03",
            "#00006FAt any rate, we just came to get some information\x01",
            "and we happen to come across a great scene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FRight, maybe we should report\x01",
            "this to Section One too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x14,
        (
            "#5P#02105FOh, you guys didn't come to\x01",
            "look into Cao's movements?\x02\x03",
            "#02102FCould you be chasing a different case?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FNo, you see...\x02\x03",
            "#00003F(Oh, right, Miss Grace met him\x01",
            "too if I remember correctly...)\x02\x03",
            "#00001F...Actually, we're looking for a person\x01",
            "you also met before, Miss Grace.\x02\x03",
            "It's a man called Lechter, who\x01",
            "beated that miner at the casino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#02105FAah, is that so?\x02\x03",
            "#02103FIf it's that kid, I spotted him at \x01",
            "The Old Dragon some time ago.\x02",
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
        "#12P#00011FEeh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FR-Really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#02100FYes, he had his usual holiday look \x01",
            "and was eating in a carefree-like way.\x02\x03",
            "#02103FBecause I was in hurry to collect data,\x01",
            "I missed the chance to greet him...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x14,
        (
            "#5P#02105FWait, I can't stay here like this.\x02\x03",
            "#02101FAt least I must get from\x01",
            "Cao a few more infos.\x02\x03",
            "#02109F...Bye!\x01",
            "Next time, let's eat together again!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_87CD():
        OP_93(0x101, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_87CD)

    def lambda_87DA():
        OP_93(0x102, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_87DA)

    def lambda_87E7():
        OP_93(0x109, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_87E7)

    def lambda_87F4():
        OP_93(0x105, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_87F4)
    OP_95(0x14, -2000, 0, 2000, 5000, 0x0)
    OP_95(0x14, -15000, 0, 2000, 5000, 0x0)
    WaitChrThread(0x14, 1)
    Sleep(100)
    SetChrFlags(0x14, 0x80)
    OP_0D()

    ChrTalk(
        0x101,
        "#00012FS-Same as always...\x02",
    )

    CloseMessageWindow()

    def lambda_8856():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8856)
    Sleep(100)

    ChrTalk(
        0x105,
        (
            "#6P#10300FHowever, we unexpectedly got \x01",
            "some eyewitness information.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_88B0():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_88B0)

    def lambda_88BD():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_88BD)

    def lambda_88CA():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_88CA)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#5P#00100FYes, let's go immediately\x01",
            "to "The Old Dragon".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FRoger!\x02",
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

    # Function_30_70AA end

    def Function_31_8990(): pass

    label("Function_31_8990")

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

    def lambda_8A62():
        OP_95(0x101, 15750, 0, 1500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A62)
    Sleep(50)

    def lambda_8A7F():
        OP_95(0x102, 16750, 0, 1200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8A7F)
    Sleep(50)

    def lambda_8A9C():
        OP_95(0x109, 17750, 0, 1500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8A9C)
    Sleep(50)

    def lambda_8AB9():
        OP_95(0x105, 18750, 0, 2350, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8AB9)
    Sleep(50)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_8AE4():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8AE4)
    WaitChrThread(0x102, 1)

    def lambda_8AF5():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8AF5)
    WaitChrThread(0x109, 1)

    def lambda_8B06():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8B06)
    WaitChrThread(0x105, 1)

    def lambda_8B17():
        OP_93(0x105, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8B17)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x109,
        "#12P#10111FHe really got down...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, did he prepare it\x01",
            "on purpose, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00106FA-Anyway, let's follow him!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FYeah, the only thing we can do is\x01",
            "ask every person who's passing by...!\x02",
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

    # Function_31_8990 end

    def Function_32_8C46(): pass

    label("Function_32_8C46")

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
            "#00106F*sigh*, it took us a long time somehow, but now\x01",
            "the "Fishing Emperor Club" investigation is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, that's right.\x02",
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E9D")
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
            "◆[What's the investigation status? (Debug)]\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "  [No changes]\x01",                          # 0
            "  [Some remains]\x01",                        # 1
            "  [Finished checking the 6 places]\x01",      # 2
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
        (0, "loc_8E76"),
        (1, "loc_8E7B"),
        (2, "loc_8E8C"),
        (SWITCH_DEFAULT, "loc_8E9D"),
    )


    label("loc_8E76")

    Jump("loc_8E9D")

    label("loc_8E7B")

    ClearScenarioFlags(0x131, 5)
    ClearScenarioFlags(0x131, 6)
    ClearScenarioFlags(0x131, 7)
    ClearScenarioFlags(0x132, 2)
    Jump("loc_8E9D")

    label("loc_8E8C")

    SetScenarioFlags(0x131, 5)
    SetScenarioFlags(0x131, 6)
    SetScenarioFlags(0x131, 7)
    SetScenarioFlags(0x132, 2)
    Jump("loc_8E9D")

    label("loc_8E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F02")

    ChrTalk(
        0x101,
        (
            "#00000FAlright then, let's continue and\x01",
            "investigate what remains.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F75")

    label("loc_8F02")

    OP_29(0x6A, 0x1, 0x6)

    ChrTalk(
        0x101,
        (
            "#00000FAlright, with this one the investigation is over.\x02\x03",
            "Let's go back to City Meeting Hall to report.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F75")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※You can now access the "fishing" minigame.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※On highways or cities water places, occasionally\x01",
            "  there are "fishing spots where ripples spread on\x01",
            "  the water surface".\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※By inspecting the fishing point and\x01",
            "  choosing the "rod" and "bait" he has \x01",
            "  with him, Lloyd can start to fish.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※If you quickly press the ○ button when the\x01",
            "  ！mark appears, you can pull in the fish.\x01",
            "  (If you are unlucky, it can also get away.)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※Furthermore, inside Crossbell City there\x01",
            "  are fishing spots at the "Waterfront Area"\x01",
            "  and "Residential Street".\x07\x00\x02",
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

    # Function_32_8C46 end

    def Function_33_9222(): pass

    label("Function_33_9222")

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
            "#12404F...Everyone, thank you very much.\x02\x03",
            "Because of you, I could retrieve this\x01",
            "before things turned into quite a clamor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha...\x01",
            "We're glad to have\x01",
            "been of help too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x1E, 500)

    ChrTalk(
        0x1F,
        (
            "#5P#13900FHmph... "This", of all the things\x01",
            "to say, eh? Isn't it a remark like\x01",
            "you were dealing with a thing?\x02\x03",
            "#13903F...Well, even such kind of treatment has a\x01",
            "certain charm and maybe couldn't be bad.\x02\x03",
            "#13912FFrom now on, sometimes, please\x01",
            "treat me that way, Mueller㈱\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x1F, 500)

    ChrTalk(
        0x1E,
        "#12401F#4S#500WWill#500W you#500W shut#500W up.#3S\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "#5P#13910F...I am very sorry.\x02",
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
            "#12400F...Sorry, I've been an acquaintance\x01",
            "of this fool since in the past.\x02\x03",
            "#12406FBecause every time his antics\x01",
            "get worse, every now and then\x01",
            "I have to strictly discipline him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00309FHa ha, it looks like you've got it quite hard, huh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x101, 500)

    ChrTalk(
        0x1F,
        (
            "#13904FWell, it's always helpful having\x01",
            "a friend who supports you.\x02\x03",
            "#13909FHmph, this too is probably a virtue I was born with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FD-Don't tell it\x01",
            "to yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FHu hu, it seems to me that\x01",
            "he's not repenting, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#12400F...It appears so.\x02\x03",
            "I'll severely preach at you\x01",
            "later, so prepare yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#5P#13911FO-Oh come ooon.\x01",
            "It was just a little joke, Mueller.\x02\x03",
            "#13910F...And you guys, could\x01",
            "you not stir him up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FA-Ahaha...\x01",
            "(They could be getting along\x01",
            "well, in a certain sense.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#12400F...Then, it's time to excuse us.\x02\x03",
            "#12404FWe're busy, and you really helped us.\x01",
            "I want to give you my thanks again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FDon't mind it, that's our job.\x02\x03",
            "#00006FHow to say, hmm...\x01",
            "Please be careful to not get\x01",
            "your eyes away from him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#12406F...Acknowledged.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#13910F*sigh*, oh boy...\x01",
            "Is the fun time over now?\x02\x03",
            "#13900FNow I bid you farewell, ladies and gentlemen.\x01",
            "We will meet again, if we're fated to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#13910FWell, personally I wanted\x01",
            "to sightsee that rumored\x01",
            "theme park.\x02\x03",
            "#13905FOh, that's right guys.\x01",
            "Can I request you to guide us now?\x02\x03",
            "#13904FHu hu, it's a good idea, even if I say so myself.\x01",
            "I'm sure that, by passing time in an enjoyable way, \x01",
            "even Mueller's brow wrinkles would...\x02",
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
            "#13911FAh, Mueller!?\x01",
            "I-It was only a light joke, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x13B, 0x0)
    SetChrChipByIndex(0x1F, 0x20)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x20)

    def lambda_9C5E():
        OP_95(0xFE, 2000, 0, 1310, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_9C5E)
    Sleep(50)

    def lambda_9C7B():
        OP_96(0xFE, 0x7D0, 0x0, 0x4F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_9C7B)
    Sleep(50)

    ChrTalk(
        0x1F,
        "#11AHeeeeeey...\x02",
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
            "#00012FI-In a way, they were some\x01",
            "amazing persons.\x02\x03",
            "#00003FAs a matter of fact, \x01",
            "I wonder who they were...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, we can ask them\x01",
            "that too if we'll meet\x01",
            "them again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FFrankly, it seems it would\x01",
            "tire us out a whole lot...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#00103F(He ended up being quite threatened,\x01",
            "but could that man have been...)\x02\x03",
            "#00109F(...N-No, that would be impossible.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#00005FWhat's wrong, Elie?\x01",
            "You've been silent since before...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#11P#00102FN-No, it's nothing.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00303F...Well, the case has been\x01",
            "closed for the present.\x02\x03",
            "#00300FLet's go, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9FB2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9FB2)
    Sleep(50)

    def lambda_9FC2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9FC2)
    Sleep(300)
    OP_62(0x101)

    ChrTalk(
        0x101,
        "#11P#00000FYeah, you're right.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x24, 3)
    NewScene("c0100", 100, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_33_9222 end

    def Function_34_A00E(): pass

    label("Function_34_A00E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A01C")
    Jump("loc_A4D1")

    label("loc_A01C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A02A")
    Jump("loc_A4D1")

    label("loc_A02A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A038")
    Jump("loc_A4D1")

    label("loc_A038")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A258")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A16C")

    ChrTalk(
        0x101,
        "#00001FThe Crimson & Co. is this way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FUncle and the others seem to\x01",
            "have been keeping a low profile\x01",
            "since the Trade Conference incident.\x02\x03",
            "#00301FEven if we go there, we won't\x01",
            "get any decent information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah...\x01",
            "Let's refrain from going there for now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_A240")

    label("loc_A16C")


    ChrTalk(
        0x101,
        (
            "#00003FIt appears that the Crimson & Co. has been keeping\x01",
            "a low profile since the Trade Conference incident.\x02\x03",
            "#00001FWe won't be able to get important information,\x01",
            "so let's refrain from going there for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A240")

    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)
    Jump("loc_A4D1")

    label("loc_A258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A310")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FThe Crimson & Co. should be under\x01",
            "the watch of Section One.\x02\x03",
            "Let's leave this place to Section One\x01",
            "and concentrate ourselves on our job.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)
    Jump("loc_A4D1")

    label("loc_A310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A402")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A32B")
    Call(0, 11)
    Jump("loc_A3FD")

    label("loc_A32B")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003FIt appears that we won't be able to catch intel\x01",
            "on the "Red Constellation" movements here.\x02\x03",
            "#00000FLet's keep dealing with support requests\x01",
            "and try inquiring in every place.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)

    label("loc_A3FD")

    Jump("loc_A4D1")

    label("loc_A402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_A410")
    Jump("loc_A4D1")

    label("loc_A410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A41E")
    Jump("loc_A4D1")

    label("loc_A41E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A4D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A443")
    Call(0, 10)
    Jump("loc_A4D1")

    label("loc_A443")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FIt looks like that the real estate\x01",
            "agent is waiting for a negotiator now.\x02\x03",
            "We're bothering him, so let's go.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)

    label("loc_A4D1")

    Return()

    # Function_34_A00E end

    def Function_35_A4D2(): pass

    label("Function_35_A4D2")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A533")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It looks like it is locked.\x01",
            "You do not sense anyone inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_A65A")

    label("loc_A533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A591")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It looks like it is locked.\x01",
            "You do not sense anyone inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_A65A")

    label("loc_A591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A605")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5B0")
    TalkEnd(0xFF)
    Call(0, 12)
    Return()

    label("loc_A5B0")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It looks like it is locked.\x01",
            "You do not sense anyone inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_A65A")

    label("loc_A605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A613")
    Jump("loc_A65A")

    label("loc_A613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A621")
    Jump("loc_A65A")

    label("loc_A621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A65A")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It looks like it is locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_A65A")

    TalkEnd(0xFF)
    Return()

    # Function_35_A4D2 end

    def Function_36_A65E(): pass

    label("Function_36_A65E")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※　Department Store "Times"　※\x01",
            "※　Employees Exclusive Entry    ※\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_36_A65E end

    def Function_37_A6CD(): pass

    label("Function_37_A6CD")

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
    EventEnd(0x3)
    Return()

    # Function_37_A6CD end

    def Function_38_A6FF(): pass

    label("Function_38_A6FF")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FLet's chase after Randy... Let's\x01",
            "hurry to the former Revache site!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -24330, 0, 210, 90)
    EventEnd(0x4)
    Return()

    # Function_38_A6FF end

    def Function_39_A765(): pass

    label("Function_39_A765")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FLet's chase after Randy... Let's\x01",
            "hurry to the former Revache site!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 19310, 0, 650, 270)
    EventEnd(0x4)
    Return()

    # Function_39_A765 end

    SaveToFile()

Try(main)
