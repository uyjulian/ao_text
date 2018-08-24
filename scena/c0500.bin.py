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
        "Function_6_2088",         # 06, 6
        "Function_7_2E73",         # 07, 7
        "Function_8_2FE0",         # 08, 8
        "Function_9_3056",         # 09, 9
        "Function_10_30D9",        # 0A, 10
        "Function_11_3A7A",        # 0B, 11
        "Function_12_4341",        # 0C, 12
        "Function_13_469B",        # 0D, 13
        "Function_14_47D4",        # 0E, 14
        "Function_15_4801",        # 0F, 15
        "Function_16_4838",        # 10, 16
        "Function_17_596F",        # 11, 17
        "Function_18_59CD",        # 12, 18
        "Function_19_59CE",        # 13, 19
        "Function_20_5A24",        # 14, 20
        "Function_21_5A25",        # 15, 21
        "Function_22_5A8A",        # 16, 22
        "Function_23_5A8B",        # 17, 23
        "Function_24_60B7",        # 18, 24
        "Function_25_6480",        # 19, 25
        "Function_26_64A9",        # 1A, 26
        "Function_27_6511",        # 1B, 27
        "Function_28_66AA",        # 1C, 28
        "Function_29_6A43",        # 1D, 29
        "Function_30_6DB5",        # 1E, 30
        "Function_31_85BF",        # 1F, 31
        "Function_32_887D",        # 20, 32
        "Function_33_8DFA",        # 21, 33
        "Function_34_9B5B",        # 22, 34
        "Function_35_A015",        # 23, 35
        "Function_36_A1A0",        # 24, 36
        "Function_37_A205",        # 25, 37
        "Function_38_A237",        # 26, 38
        "Function_39_A2A4",        # 27, 39
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_11F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1142")

    ChrTalk(
        0xFE,
        (
            "Maybe it's because of these difficult\x01",
            "times, but there's a weird feeling of\x01",
            "solidarity among the people at the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've come to a point where I\x01",
            "don't care to compete for the top\x01",
            "spot with the rival girl anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a hostess, entertaining\x01",
            "the guests and having them\x01",
            "drink is okay☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_11F3")

    label("loc_1142")


    ChrTalk(
        0xFE,
        (
            "I've come to a point where I\x01",
            "don't care to compete for the top\x01",
            "spot with the rival girl anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a hostess, entertaining\x01",
            "the guests and having them\x01",
            "drink is okay☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F3")

    Jump("loc_2084")

    label("loc_11F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1206")
    Jump("loc_2084")

    label("loc_1206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1371")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E2")

    ChrTalk(
        0xFE,
        (
            "State independence...\x01",
            "That has a nice ring to\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The people at the store saw the\x01",
            "President's speech too. It looked\x01",
            "like they really enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Somehow, I became\x01",
            "happy too♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_136C")

    label("loc_12E2")


    ChrTalk(
        0xFE,
        (
            "The people at the store saw the\x01",
            "President's speech too. It looked\x01",
            "like they really enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Somehow, I became\x01",
            "happy too♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_136C")

    Jump("loc_2084")

    label("loc_1371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_137F")
    Jump("loc_2084")

    label("loc_137F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_141D")

    ChrTalk(
        0xFE,
        (
            "Isn't the Mainz\x01",
            "occupation a really big\x01",
            "incident...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And the miners over there\x01",
            "came to our store before,\x01",
            "too. I hope they're safe...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2084")

    label("loc_141D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_156A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CA")

    ChrTalk(
        0xFE,
        (
            "Listen, listen, big\x01",
            "news!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goodness, our store's\x01",
            "number one requested\x01",
            "hostess this month is me!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, it was worth\x01",
            "doing my best!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1565")

    label("loc_14CA")


    ChrTalk(
        0xFE,
        (
            "Finally, I've become the\x01",
            "number one girl I so\x01",
            "longed to be!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. From now on, I'll surely\x01",
            "be requested many more\x01",
            "times... I have to do my best!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1565")

    Jump("loc_2084")

    label("loc_156A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_15C7")

    ChrTalk(
        0xFE,
        (
            "There's noise coming from\x01",
            "Central Square... What,\x01",
            "has something happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2084")

    label("loc_15C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_172A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D6")

    ChrTalk(
        0xFE,
        (
            "The rival girl I compete with for customer\x01",
            "requests called some of her acquaintances\x01",
            "to the store to increase her count!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eeeek, don't you think\x01",
            "that's unfair!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that it's come to\x01",
            "this, I'll pull out\x01",
            "everything in my arsenal!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1725")

    label("loc_16D6")


    ChrTalk(
        0xFE,
        (
            "I won't lose to that\x01",
            "rival girl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll do anything to be\x01",
            "number one!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1725")

    Jump("loc_2084")

    label("loc_172A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_18D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_182E")

    ChrTalk(
        0xFE,
        (
            "Sir, won't you come\x01",
            "visit at our stooore?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Actually, there's a narrow margin\x01",
            "between me and the rival girl. I'm\x01",
            "competing with her for requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whoever wins will be this\x01",
            "month's number one girl!\x01",
            "So help me out, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18D3")

    label("loc_182E")


    ChrTalk(
        0xFE,
        (
            "...Uhhm, I see. You guys\x01",
            "are working, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, when you'll come to the store,\x01",
            "be sure to ask for me, okay? My number\x01",
            "one status is on the line here!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D3")

    Jump("loc_2084")

    label("loc_18D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1957")

    ChrTalk(
        0xFE,
        (
            "Recently, the rival girl at\x01",
            "the store's requests have\x01",
            "been steadily increasing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I mustn't lose either.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2084")

    label("loc_1957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1B23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A88")

    ChrTalk(
        0xFE,
        (
            "Orchis Tower... It's a\x01",
            "magnificent building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I snuck away from work for\x01",
            "a bit to see the unveiling\x01",
            "and I was dumbfounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The people employed\x01",
            "there surely have a\x01",
            "superb view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whether you've come our store\x01",
            "for business or pleasure, be\x01",
            "sure to ask for me, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B1E")

    label("loc_1A88")


    ChrTalk(
        0xFE,
        (
            "Orchis Tower... It's a\x01",
            "magnificent building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When the people working there come\x01",
            "to our store, I'd really like them\x01",
            "to ask for me, you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B1E")

    Jump("loc_2084")

    label("loc_1B23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1CCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C0C")

    ChrTalk(
        0xFE,
        (
            "I heard from a customer\x01",
            "that the trade conference\x01",
            "will open tomorrow morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it doesn't appear to be a festival\x01",
            "like the anniversary one... I wonder what\x01",
            "kind of event it's going to be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CC5")

    label("loc_1C0C")


    ChrTalk(
        0xFE,
        (
            "Oopsie, no, I mustn't.\x01",
            "That's not something I\x01",
            "should be worrying about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, I've got to think of how obtain\x01",
            "the most requests possible, so as\x01",
            "not to lose to that rival girl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC5")

    Jump("loc_2084")

    label("loc_1CCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_1E6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC1")

    ChrTalk(
        0xFE,
        (
            "Just now, a big and\x01",
            "brawny redheaded old man\x01",
            "was around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There was a cute girl who looked like\x01",
            "a cat and a gentleman who plainly\x01",
            "looked like a playboy with him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, it was an odd\x01",
            "scene somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E68")

    label("loc_1DC1")


    ChrTalk(
        0xFE,
        (
            "That reminds me, even the\x01",
            "guy I saw some time ago had\x01",
            "the same exact hair color.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could they all be family?\x01",
            "Although they didn't exactly\x01",
            "resemble each other.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E68")

    Jump("loc_2084")

    label("loc_1E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1F20")

    ChrTalk(
        0xFE,
        (
            "Is it true that the\x01",
            "whole place in the back\x01",
            "alley was sold?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before, there were some scaaary\x01",
            "men in black... I wonder what\x01",
            "kind of people will move in now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2084")

    label("loc_1F20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2084")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FCF")

    ChrTalk(
        0xFE,
        "Teehee, I'm Iris☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sir, won't you come\x01",
            "visit at our stooore?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why don't you pass the\x01",
            "time pleasantly drinking\x01",
            "and chatting with me?㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2084")

    label("loc_1FCF")


    ChrTalk(
        0xFE,
        (
            "Recently my number of\x01",
            "requests have gone up\x01",
            "and I'm very satisfied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll establish a lead on the rival\x01",
            "girl, and eventually I'll become\x01",
            "number one for number of requests!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2084")

    TalkEnd(0xFE)
    Return()

    # Function_5_FF8 end

    def Function_6_2088(): pass

    label("Function_6_2088")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2235")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2184")

    ChrTalk(
        0xFE,
        (
            "Mister, mister, won't\x01",
            "you stop by our store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're currently having a\x01",
            "hyper happy sale to celebrate\x01",
            "President Dieter's arrest!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Keep the fact that we\x01",
            "also had a sale celebrating\x01",
            "independence a secret, 'k?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2230")

    label("loc_2184")


    ChrTalk(
        0xFE,
        (
            "We're currently having a\x01",
            "hyper happy sale to celebrate\x01",
            "President Dieter's arrest!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Keep the fact that we\x01",
            "also had a sale celebrating\x01",
            "independence a secret, 'k?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2230")

    Jump("loc_2E6F")

    label("loc_2235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2243")
    Jump("loc_2E6F")

    label("loc_2243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_230A")

    ChrTalk(
        0xFE,
        (
            "Mister, mister, we're currently\x01",
            "having a super happy sale to\x01",
            "celebrate independence!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's daybreak in Crossbell, so\x01",
            "there won't be any harm in\x01",
            "spending time with a cute girl!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E6F")

    label("loc_230A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_23CD")

    ChrTalk(
        0xFE,
        (
            "Mister, mister, even our\x01",
            "store reopened for\x01",
            "business recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why don't you come to drink, play,\x01",
            "and heal your body and soul fatigued\x01",
            "by the repair work with cute girls?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E6F")

    label("loc_23CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2466")

    ChrTalk(
        0xFE,
        (
            "An occupation... What an\x01",
            "unthinkable thing to\x01",
            "have happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even I am not in the mood\x01",
            "to do the barking in a\x01",
            "situation like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E6F")

    label("loc_2466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2522")

    ChrTalk(
        0xFE,
        (
            "Man, it's raining again.\x01",
            "There's not many customers\x01",
            "either. That's painful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard there was a huge\x01",
            "accident yesterday. It can't be\x01",
            "helped if business isn't good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E6F")

    label("loc_2522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2595")

    ChrTalk(
        0xFE,
        (
            "Heck, it's noisy with\x01",
            "all the sirens from the\x01",
            "square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is it another incident\x01",
            "of some kind?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E6F")

    label("loc_2595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2719")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2684")

    ChrTalk(
        0xFE,
        (
            "Today, we're having our\x01",
            "customary happy sale.\x02",
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
            "If you pass this up today, who\x01",
            "knows when we'll do it again!\x01",
            "Come on, folks! Follow me!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2714")

    label("loc_2684")


    ChrTalk(
        0xFE,
        (
            "Today, we're having our\x01",
            "customary happy sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you pass this up today, who\x01",
            "knows when we'll do it again!\x01",
            "Come on, folks! Follow me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2714")

    Jump("loc_2E6F")

    label("loc_2719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_27E3")

    ChrTalk(
        0xFE,
        (
            "With the recent independence and\x01",
            "all, it's just one complicated\x01",
            "thing after another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You've got to come relax in our\x01",
            "store especially in times like\x01",
            "these! We'll make you happy♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E6F")

    label("loc_27E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_28A0")

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
            "People tired from work are\x01",
            "the target of barking. Hehe,\x01",
            "I'll try speaking to them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E6F")

    label("loc_28A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_293E")

    ChrTalk(
        0xFE,
        (
            "It seems VIPs from all\x01",
            "neighboring countries\x01",
            "have come to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'd be nice publicity\x01",
            "for us if any came to\x01",
            "drink at our store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E6F")

    label("loc_293E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2A07")

    ChrTalk(
        0xFE,
        (
            "The Crimson & Co. men who\x01",
            "moved into the back alley all\x01",
            "look like cheerful people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. If I introduce them to some\x01",
            "cute girls, we'll get ourselves\x01",
            "some new regular customers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E6F")

    label("loc_2A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_2B00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AA7")

    ChrTalk(
        0xFE,
        (
            "Oh my, this won't do. A\x01",
            "downpour has started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I won't be able to reel in\x01",
            "anyone else today. I guess\x01",
            "it's time to pull out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2AFB")

    label("loc_2AA7")


    ChrTalk(
        0xFE,
        (
            "...A red-headed gentleman?\x01",
            "He entered the back alley\x01",
            "over there some time ago.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AFB")

    Jump("loc_2E6F")

    label("loc_2B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2B76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B1B")
    Call(0, 7)
    Jump("loc_2B71")

    label("loc_2B1B")


    ChrTalk(
        0xFE,
        (
            "It's tough to reel in\x01",
            "the customers on rainy\x01",
            "days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Boy, that's troublesome.\x02",
    )

    CloseMessageWindow()

    label("loc_2B71")

    Jump("loc_2E6F")

    label("loc_2B76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2E6F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C66")

    ChrTalk(
        0xFE,
        (
            "The gentleman who passed\x01",
            "through went in the direction\x01",
            "of Entertainment District...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I get the feeling I've\x01",
            "seen that man before\x01",
            "around here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, maybe it's just my\x01",
            "imagination.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2D1F")

    label("loc_2C66")


    ChrTalk(
        0xFE,
        (
            "If you're looking for the\x01",
            "redheaded gentleman, he went\x01",
            "towards Entertainment District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I get the feeling I saw him\x01",
            "around here before, but... Well,\x01",
            "maybe it's my imagination.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D1F")

    Jump("loc_2E6F")

    label("loc_2D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D36")
    Call(0, 7)
    Jump("loc_2E6F")

    label("loc_2D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E38")

    ChrTalk(
        0xFE,
        (
            "Hehe, my bad. Please let\x01",
            "it slide just this once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like, I can give you\x01",
            "service ticket for the next\x01",
            "time you come to our store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWe don't need it.\x01",
            "...Bribery is a crime,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, I'm no match for\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2E6F")

    label("loc_2E38")


    ChrTalk(
        0xFE,
        (
            "Hehe, my bad. Please let\x01",
            "it slide just this once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E6F")

    TalkEnd(0xFE)
    Return()

    # Function_6_2088 end

    def Function_7_2E73(): pass

    label("Function_7_2E73")


    ChrTalk(
        0x9,
        (
            "Oh, ladies and\x01",
            "gentlemen, are you free\x01",
            "now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There's lots of cuties\x01",
            "at our store! Say, wanna\x01",
            "drop by? Eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F...Coercive barking is\x01",
            "illegal, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't say such a\x01",
            "stuffy... Wait, are you\x01",
            "guys with the police?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hehe, my bad. Please let\x01",
            "it slide just this once,\x01",
            "eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(*sigh*... As always,\x01",
            "security's poor in this\x01",
            "area.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 2)
    Return()

    # Function_7_2E73 end

    def Function_8_2FE0(): pass

    label("Function_8_2FE0")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "At present, this building\x01",
            "is under investigation by\x01",
            "Section One.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I ask you to refrain\x01",
            "from entering.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_2FE0 end

    def Function_9_3056(): pass

    label("Function_9_3056")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Those damn Red\x01",
            "Constellation guys. What\x01",
            "are they up to this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope the incident is\x01",
            "resolved quickly, but...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_3056 end

    def Function_10_30D9(): pass

    label("Function_10_30D9")

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
            "#12P#00001FThis place... It's the\x01",
            "building Revache & Co.\x01",
            "abandoned.\x02\x03",
            "#00003FIt should be vacant\x01",
            "right now, but...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Man's Voice",
        (
            "Hey you, what're you\x01",
            "doing there?\x02",
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

    def lambda_32A4():

        label("loc_32A4")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_32A4")

    QueueWorkItem2(0x101, 2, lambda_32A4)

    def lambda_32B6():

        label("loc_32B6")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_32B6")

    QueueWorkItem2(0x102, 2, lambda_32B6)

    def lambda_32C8():

        label("loc_32C8")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_32C8")

    QueueWorkItem2(0x109, 2, lambda_32C8)

    def lambda_32DA():

        label("loc_32DA")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_32DA")

    QueueWorkItem2(0x105, 2, lambda_32DA)

    def lambda_32EC():
        OP_95(0xFE, 0, 0, 33500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_32EC)
    WaitChrThread(0xE, 1)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0x101,
        "#00005FUhmmm, and you are...?\x02",
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
            "#12P*cough*, I run a real\x01",
            "estate agency in\x01",
            "Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Man",
        (
            "#12PThis was consigned to me by the state\x01",
            "government and I was entrusted with\x01",
            "the management of this whole place.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Man",
        (
            "#12PYou'll make things difficult\x01",
            "for me if you enter the\x01",
            "grounds as you please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00103FThe government consigned... Now that\x01",
            "you mention it, I did hear that from\x01",
            "grandfather.\x02\x03",
            "#00100FBecause they can't leave the mafia's\x01",
            "assets alone even for a second, their\x01",
            "consignment was quickly decided upon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FI see...\x02\x03",
            "#00000FUhmm, sorry for the\x01",
            "inconvenience. We're from\x01",
            "the Crossbell Police.\x02\x03",
            "We're currently\x01",
            "patrolling the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12POh, you're police officers?\x01",
            "Thanks for patrolling even\x01",
            "a place like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10100FUmm, so are you doing\x01",
            "periodic inspection of the\x01",
            "building today, or...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PWell... Actually, this\x01",
            "building will be put up for\x01",
            "sale before long, you know.\x02",
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
        (
            "#5P#00005FThe whole thing is on\x01",
            "sale...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PYeah. Several businesses\x01",
            "have expressed interest\x01",
            "in moving in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PA representative of one of them\x01",
            "is coming to negotiate today.\x01",
            "I'm waiting here for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10105FBusinesses expressed interest\x01",
            "in a property formerly owned\x01",
            "by the mafia...?\x02\x03",
            "#10106FHmm. When I say it like\x01",
            "that... Is that really all\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PWell, we're somewhat\x01",
            "worried too, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PIt's just, this building is so\x01",
            "big. Even just the management\x01",
            "costs aren't to be taken lightly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PIf someone wants to do us the\x01",
            "favor of taking it, we've no\x01",
            "reason to turn them down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10303FWell, as a merchant,\x01",
            "wanting to sell it\x01",
            "quickly is only natural.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FYeah, it worries me\x01",
            "though...\x02\x03",
            "#00000FWe're also in the way\x01",
            "here, so, should we go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00103FYes... Let's go.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xE, 0x8)
    SetChrPos(0x0, 90, 0, 80, 180)
    SetScenarioFlags(0x139, 1)
    EventEnd(0x5)
    Return()

    # Function_10_30D9 end

    def Function_11_3A7A(): pass

    label("Function_11_3A7A")

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

    def lambda_3BC4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3BC4)

    def lambda_3BD5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3BD5)

    def lambda_3BE6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3BE6)

    def lambda_3BF7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3BF7)

    def lambda_3C08():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3C08)

    def lambda_3C19():
        OP_95(0xFE, -600, 0, 34200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C19)

    def lambda_3C33():
        OP_95(0xFE, 600, 0, 34200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C33)

    def lambda_3C4D():
        OP_95(0xFE, 0, 0, 36000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3C4D)

    def lambda_3C67():
        OP_95(0xFE, -1200, 0, 33000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3C67)

    def lambda_3C81():
        OP_95(0xFE, 1200, 0, 33000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3C81)
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
        (
            "Ohh, if it isn't Captain\x01",
            "Randolph!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha, you're here again\x01",
            "today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001F(This Red Constellation\x01",
            "jaeger... Looks like\x01",
            "Randy knows him.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F...Sachs, it looks like\x01",
            "your new HQ is quite\x01",
            "comfy, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha, thank goodness it\x01",
            "is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The Entertainment District branch\x01",
            "of Neue-Blanc is nearby too, so\x01",
            "it's quite convenient to use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FHah... You did a good\x01",
            "job, as always.\x02\x03",
            "#00301F...Uncle and Shirley\x01",
            "aren't here today\x01",
            "either?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah, the boss and the\x01",
            "missus went out for\x01",
            "business today as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you have a message\x01",
            "I'll tell them. How\x01",
            "'bout it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F...No, sorry to have\x01",
            "bothered you.\x02",
        )
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
        "#6P#00005FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Thanks for all your hard\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hehe. See ya soon,\x01",
            "Captain.\x02",
        )
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
            "#00303F...Hmph. It seems\x01",
            "they're pretendin' to be\x01",
            "out again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105F"Again" you say... Did\x01",
            "you visit recently?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00303FHe said he had something to\x01",
            "talk about, but that was the\x01",
            "last I've heard of 'im.\x02\x03",
            "#00301FAnyway, it appears that even\x01",
            "if I try to meet 'im, he's got\x01",
            "no intention of showin' up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FHmm, he might contact\x01",
            "you somehow before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10106FBut, if that's the case...\x01",
            "We can only inquire steadily\x01",
            "about Red Constellation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, let's try visiting\x01",
            "various places while taking\x01",
            "care of our support requests.\x02",
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

    # Function_11_3A7A end

    def Function_12_4341(): pass

    label("Function_12_4341")

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
            "#00003F...Looks like it's locked.\x02\x03",
            "#00001FThe Section One investigation is\x01",
            "largely complete too, so there\x01",
            "shouldn't be anyone inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FDisappearing with an airship\x01",
            "like that... I wonder where\x01",
            "they're hiding now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FIt appears that even the\x01",
            "CGF is on guard against\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F...............\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)
    Sleep(50)

    ChrTalk(
        0x103,
        "#12P#00200FRandy...\x02",
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
            "#00304F...Haha, don't worry.\x02\x03",
            "#00301FIt's just... We've got to\x01",
            "settle things once and for all\x01",
            "the next time we meet them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FYeah... That's right.\x02",
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

    # Function_12_4341 end

    def Function_13_469B(): pass

    label("Function_13_469B")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_475F")
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x8000)
    EndChrThread(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, -8800, 0, 3100, 90)
    SetChrPos(0x8, -7300, 0, 3100, 270)

    label("loc_475F")

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

    # Function_13_469B end

    def Function_14_47D4(): pass

    label("Function_14_47D4")

    SetChrPos(0xFE, 18000, 0, 500, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -37000, 0, 500)
    OP_9F(0x2, 0xFE, 5000, 0x6)
    Return()

    # Function_14_47D4 end

    def Function_15_4801(): pass

    label("Function_15_4801")

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

    # Function_15_4801 end

    def Function_16_4838(): pass

    label("Function_16_4838")

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
        "#00311F#2753V#6P#30WUncle... Shirley...\x02",
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
            "#3941V#5P#20WHahaha! Hey Randy! It's been a\x01",
            "while!\x02",
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
            "#3834V#11P#30WWhat's it been, two years? You\x01",
            "haven't changed a bit.\x02",
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

    def lambda_4D70():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4D70)
    Sleep(50)

    def lambda_4D88():
        OP_9B(0x0, 0x102, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4D88)
    Sleep(50)

    def lambda_4DA0():
        OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4DA0)
    Sleep(50)

    def lambda_4DB8():
        OP_9B(0x0, 0x109, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4DB8)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00007F#6P...Randy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10111F#6P#NWait, are they the ones\x01",
            "from yesterday!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10303F#6P#NA bunch of suspicious\x01",
            "characters showed up all\x01",
            "of a sudden, huh.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x11,
        (
            "#03509F#5PAhh, so I was right\x01",
            "after all. You're all\x01",
            "family like I thought.\x02\x03",
            "#03502FI mean the hair color\x01",
            "was kind of a giveaway\x01",
            "but still...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#6P...............\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00013F#6PCaptain Lechter... What\x01",
            "are you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6PDo you have a hand in\x01",
            "the buyout of this\x01",
            "property?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#03504F#5PYeah, it's all a little\x01",
            "sketchy.\x02\x03",
            "#03510FStill, how great is it that\x01",
            "we were able to outwit that\x01",
            "four-eyes from Heiyue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#04609F#11PHaha, I can't wait!\x02\x03",
            "#04602FI was pissed when we had to run away from\x01",
            "the Eastern Quarter, but this time it looks\x01",
            "like I'll be able to play all I want!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00005F#6PEastern Quarter...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6PYour little "war" with\x01",
            "Heiyue in Calvard last\x01",
            "year...\x02\x03",
            "#00311F...Hey, Uncle, why are\x01",
            "you in Crossbell?\x02\x03",
            "What the hell are you\x01",
            "plannin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04504F#11PHehe... Business, ain't\x01",
            "it obvious?\x02\x03",
            "#04500FThat aside, Randolph,\x01",
            "I've got something to\x01",
            "tell you.\x02\x03",
            "─Big bro is dead.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00305F#6P#40W#2S...What...\x02",
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
            "#04503F#11PIt happened about half a\x01",
            "year ago.\x02\x03",
            "The boss of Zephyr and\x01",
            "he killed each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#04602F#11PThe decisive duel between\x01",
            "the War God and Jaeger King,\x01",
            "who were longtime enemies!\x02\x03",
            "#04612FIt was a sight to behold!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00308F#6P#40W............\x02\x03",
            "#00304F#40W...Haha... I see...\x02\x03",
            "#30WMy old man... So died\x01",
            "fightin' to the bitter\x01",
            "end, huh.\x02\x03",
            "#00300F#40W...He looked satisfied,\x01",
            "I bet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#04602F#11PYeah he was havin' a\x01",
            "blast!\x02\x03",
            "#04606FHow nice, Shirley wishes\x01",
            "she had an opponent like\x01",
            "that too~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#04504F#11PWell, he went without\x01",
            "any regrets.\x02\x03",
            "#04501F─Aside from his runaway,\x01",
            "cowardly son, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#6P...!\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xF,
        (
            "#04504F#5PVacation's over,\x01",
            "Randolph.\x02\x03",
            "#04502FWe'll talk soon, so make\x01",
            "yourself available for\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x10,
        "#04609F#11PLater, Randy!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x11,
        "#03509F#5PBuh bye, guys.\x02",
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
        "#00108F#6P#NRandy...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10113F#6P#NYou ok, Randy?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00008F#6PWere those your...\x02",
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
            "#00303F#11P#30WSigmund Orlando, Red\x01",
            "Constellation's vice\x01",
            "commander.\x02\x03",
            "And that girl is Shirley\x01",
            "Orlando, one of their\x01",
            "commanders.\x02",
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
            "─Two of the strongest,\x01",
            "worst battle ogres.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_585A")
    Jump("loc_585F")

    label("loc_585A")

    OP_29(0x67, 0x4, 0x40)

    label("loc_585F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5870")
    Jump("loc_5875")

    label("loc_5870")

    OP_29(0x6D, 0x4, 0x40)

    label("loc_5875")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5886")
    Jump("loc_588B")

    label("loc_5886")

    OP_29(0x6E, 0x4, 0x40)

    label("loc_588B")

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

    # Function_16_4838 end

    def Function_17_596F(): pass

    label("Function_17_596F")

    OP_95(0xFE, 0, 0, 42270, 2000, 0x0)
    OP_95(0xFE, 0, 300, 43640, 2000, 0x0)
    Sound(103, 0, 100, 0)
    OP_71(0x2, 0x1, 0xA, 0x1, 0x0)
    Sleep(500)

    def lambda_59B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_59B1)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
    Return()

    # Function_17_596F end

    def Function_18_59CD(): pass

    label("Function_18_59CD")

    Return()

    # Function_18_59CD end

    def Function_19_59CE(): pass

    label("Function_19_59CE")

    Sleep(1500)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 0, 0, 42270, 2000, 0x0)
    OP_95(0xFE, 0, 300, 43640, 2000, 0x0)

    def lambda_5A08():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5A08)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
    Return()

    # Function_19_59CE end

    def Function_20_5A24(): pass

    label("Function_20_5A24")

    Return()

    # Function_20_5A24 end

    def Function_21_5A25(): pass

    label("Function_21_5A25")

    Sleep(2000)
    OP_93(0xFE, 0x2D, 0x1F4)
    OP_95(0xFE, 0, 0, 42270, 2000, 0x0)
    OP_95(0xFE, 0, 300, 43640, 2000, 0x0)

    def lambda_5A5C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5A5C)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0xA, 0x0, 0x1, 0x0)
    Return()

    # Function_21_5A25 end

    def Function_22_5A8A(): pass

    label("Function_22_5A8A")

    Return()

    # Function_22_5A8A end

    def Function_23_5A8B(): pass

    label("Function_23_5A8B")

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
            "#04602F#3973V#5P#30WWoah! That building's\x01",
            "insane!\x02\x03",
            "#04612F#3974VHey hey, can't we blow\x01",
            "it up?\x02",
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
            "#04504F#5PHaha... I understand how\x01",
            "you feel, but just stop.\x02\x03",
            "#04500FI intend to make good\x01",
            "use of that building\x01",
            "eventually.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    ChrTalk(
        0x10,
        (
            "#04606F#11PMrr, too bad.\x02\x03",
            "#04602FWell anyway, I'm going\x01",
            "to take a walk around\x01",
            "the city, ok?\x02\x03",
            "#04612FIt's crowded thanks to\x01",
            "that building♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#04504F#5PSure, you can go.\x02",
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

    def lambda_5E29():
        OP_9D(0xFE, 0x0, 0x1450, 0x1DB0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5E29)
    Sleep(300)

    def lambda_5E49():

        label("loc_5E49")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_5E49")

    QueueWorkItem2(0xF, 2, lambda_5E49)

    def lambda_5E5B():

        label("loc_5E5B")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_5E5B")

    QueueWorkItem2(0x12, 2, lambda_5E5B)

    def lambda_5E6D():

        label("loc_5E6D")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_5E6D")

    QueueWorkItem2(0xC, 2, lambda_5E6D)
    WaitChrThread(0x10, 1)
    Sound(62, 0, 100, 0)
    OP_92(0x10, 0x0, 0x1004, 0x1F4)

    def lambda_5E96():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5E96)
    WaitChrThread(0x10, 1)
    Sound(844, 0, 50, 0)
    SetChrSubChip(0x10, 0x2)

    def lambda_5EBE():
        OP_9D(0xFE, 0x0, 0x0, 0xE10, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5EBE)
    WaitChrThread(0x10, 1)
    EndChrThread(0xF, 0x2)
    EndChrThread(0x12, 0x2)
    EndChrThread(0xC, 0x2)
    SetChrFlags(0x10, 0x80)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#5PHaha... How very like\x01",
            "her.\x02",
        )
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
            "#04504F#5PHaha, I suppose.\x02\x03",
            "#04502FBut it's more than that─\x01",
            "she's excited by the\x01",
            "anticipation of battle.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xF, 500)

    ChrTalk(
        0xC,
        "#6P...!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0xF, 500)

    ChrTalk(
        0x12,
        (
            "#12PI see. That's very like\x01",
            "Lady Shirley.\x02",
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
            "#04504F#5PHehe... She really is my\x01",
            "daughter.\x02\x03",
            "#04502FI think she'll fully\x01",
            "enjoy herself tomorrow.\x02",
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

    # Function_23_5A8B end

    def Function_24_60B7(): pass

    label("Function_24_60B7")

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

    def lambda_6293():
        OP_95(0xFE, 10, 0, 39370, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6293)
    Sleep(30)

    def lambda_62B0():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_62B0)
    Sleep(30)

    def lambda_62C8():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_62C8)
    Sleep(50)

    def lambda_62E0():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_62E0)
    Sleep(30)

    def lambda_62F8():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_62F8)

    def lambda_630D():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_630D)
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

    def lambda_638B():
        OP_95(0xFE, 10, 0, 43000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_638B)
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

    def lambda_63F0():
        OP_95(0xFE, 0, 0, 45000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_63F0)

    def lambda_640A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_640A)
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

    # Function_24_60B7 end

    def Function_25_6480(): pass

    label("Function_25_6480")

    OP_95(0xFE, 0, 0, 650, 5000, 0x0)
    OP_95(0xFE, 0, 0, 6000, 5000, 0x0)
    Return()

    # Function_25_6480 end

    def Function_26_64A9(): pass

    label("Function_26_64A9")


    def lambda_64AE():
        OP_95(0xFE, 0, 0, 39370, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_64AE)
    WaitChrThread(0xFE, 1)

    def lambda_64CC():
        OP_95(0xFE, 0, 0, 43670, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_64CC)
    WaitChrThread(0xFE, 1)

    def lambda_64EA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_64EA)

    def lambda_64FB():
        OP_95(0xFE, 0, 0, 45000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_64FB)
    Return()

    # Function_26_64A9 end

    def Function_27_6511(): pass

    label("Function_27_6511")

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
            "#00001F#5PIt looks like... There's\x01",
            "no one here anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#6PThe police should've at\x01",
            "least left it locked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PHe's called us here, so\x01",
            "maybe he picked the\x01",
            "lock?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F#11PAnyway, let's enter.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 34000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x182, 3)
    EventEnd(0x5)
    Return()

    # Function_27_6511 end

    def Function_28_66AA(): pass

    label("Function_28_66AA")

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
            "#02101FHmm... They've finally\x01",
            "begun to act.\x02\x03",
            "#02103FSince it's related, should\x01",
            "I make an article on it?\x02\x03",
            "#02101FPressure from the Republic\x01",
            "faction has decreased\x01",
            "recently, but...\x02",
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
            "#00005FHey Grace, what are you\x01",
            "doing?\x02",
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

    def lambda_6934():
        OP_93(0x14, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6934)

    def lambda_6941():
        OP_95(0x101, 850, 0, 1360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6941)
    Sleep(100)

    def lambda_695E():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_695E)
    Sleep(100)

    def lambda_6976():
        OP_95(0x105, 0, 0, 360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6976)
    Sleep(100)

    def lambda_6993():
        OP_9B(0x0, 0x109, 0x0, 0x1194, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6993)
    WaitChrThread(0x109, 1)

    def lambda_69AC():
        OP_95(0x109, 1300, 0, 260, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_69AC)
    Sleep(100)
    OP_6F(0x79)
    WaitChrThread(0x102, 1)

    def lambda_69CF():
        OP_95(0x102, -600, 0, 1560, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_69CF)
    WaitChrThread(0x101, 1)

    def lambda_69ED():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_69ED)

    def lambda_69FA():
        OP_93(0x14, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_69FA)
    WaitChrThread(0x109, 1)

    def lambda_6A0B():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6A0B)
    Sleep(200)
    WaitChrThread(0x105, 1)

    def lambda_6A1F():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6A1F)
    Sleep(200)
    WaitChrThread(0x102, 1)

    def lambda_6A33():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6A33)
    WaitChrThread(0x105, 1)
    Call(0, 30)
    Return()

    # Function_28_66AA end

    def Function_29_6A43(): pass

    label("Function_29_6A43")

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
            "#12P#02101FHmm... They've finally\x01",
            "begun to act.\x02\x03",
            "#02103FSince it's related, should\x01",
            "I make an article on it?\x02\x03",
            "#02101FPressure from the Republic\x01",
            "faction has decreased\x01",
            "recently, but...\x02",
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
            "#00005FHey Grace, what are you\x01",
            "doing?\x02",
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

    def lambda_6CD1():
        TurnDirection(0x14, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6CD1)

    def lambda_6CDE():
        OP_95(0x101, 850, 0, 1360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6CDE)
    Sleep(100)

    def lambda_6CFB():
        OP_95(0x102, -600, 0, 1560, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6CFB)
    Sleep(100)

    def lambda_6D18():
        OP_95(0x109, 1300, 0, 260, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6D18)
    Sleep(100)

    def lambda_6D35():
        OP_95(0x105, 0, 0, 360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6D35)
    Sleep(1000)

    def lambda_6D52():
        OP_93(0x14, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6D52)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)

    def lambda_6D65():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6D65)

    def lambda_6D72():
        OP_93(0x14, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6D72)
    WaitChrThread(0x102, 1)

    def lambda_6D83():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6D83)
    WaitChrThread(0x109, 1)

    def lambda_6D94():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6D94)
    WaitChrThread(0x105, 1)

    def lambda_6DA5():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6DA5)
    WaitChrThread(0x105, 1)
    Call(0, 30)
    Return()

    # Function_29_6A43 end

    def Function_30_6DB5(): pass

    label("Function_30_6DB5")

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
            "W-What? Oh, it's you guys.\x02\x03",
            "So you guys have finally started up\x01",
            "again?\x02",
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
        "#6P#00000FYes, fortunately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FTio and Randy will be\x01",
            "joining us later,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#02100FI see. Too bad.\x02\x03",
            "#02106FBut who would've thought\x01",
            "Wazy'd join the Support\x01",
            "Section, eh?\x02\x03",
            "#02102FI'm really quite\x01",
            "surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHaha, glad to hear it.\x02\x03",
            "#10304FI wouldn't mind if you\x01",
            "put together a special\x01",
            "feature on it, though.\x02",
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
            "#02109FHaha, that sounds fun.\x02\x03",
            "#02106FI'd love to have a nice\x01",
            "long chat, but I've got\x01",
            "my hands full right now.\x02\x03",
            "#02102FOnce I'm finished, then\x01",
            "we can─\x02",
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
        "Youth's Voice",
        (
            "#NMy, what a rare\x01",
            "ensemble.\x02",
        )
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

    def lambda_71E9():
        OP_98(0x15, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_71E9)
    Sleep(50)

    def lambda_7206():
        OP_98(0x16, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_7206)
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
            "Lloyd, Elie. Long time no see.\x02\x03",
            "And─ Wazy and Sgt. Noｱl, I\x01",
            "presume?\x02",
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
        "#6P#10111FH-How do you...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FWow, impressive\x01",
            "information network\x01",
            "you've got there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03204FHaha. You are the\x01",
            "Special Support Section,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x10E, 0x1F4)

    ChrTalk(
        0x15,
        (
            "#03200FBut, to think Grace has\x01",
            "already caught wind of\x01",
            "our actions.\x02\x03",
            "#03209FThat's the renowned\x01",
            "Crossbell Times for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#02109FN-Nah... It's a\x01",
            "coincidence. Yeah, a\x01",
            "coincidence!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FWhat are doing in a\x01",
            "place like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FDid you have some\x01",
            "business at the old\x01",
            "Revache building?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0xB4, 0x1F4)

    ChrTalk(
        0x15,
        (
            "#03200FHaha, isn't it obvious?\x02\x03",
            "#03204FJust letting it rot like\x01",
            "this would be a terrible\x01",
            "waste of land.\x02\x03",
            "#03202FAnd so, my company is\x01",
            "thinking of putting it\x01",
            "to good use.\x02",
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
        "#6P#00001F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03203FHaha. Normally, taking possession of mafia\x01",
            "property is quite difficult.\x02\x03",
            "#03210FHowever in our case, we're somewhat familiar\x01",
            "with that property in particular.\x02\x03",
            "#03204FIf the property was sold to a merchant, the\x01",
            "monthly management costs would be excessive.\x01",
            "So it seems we'll get a good deal on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00010FUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#02101F...Umm, Mr. Cao? Can I\x01",
            "put such info in an\x01",
            "article?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03200FYes, I don't mind. It's\x01",
            "nothing to be ashamed of.\x02\x03",
            "#03204FAlthough I'd like you to cut\x01",
            "us some slack and declare\x01",
            "that it's just speculation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#02109FA-Ahaha... Of course,\x01",
            "I'll keep that in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#03200FHaha. I'll excuse\x01",
            "myself, then.\x02\x03",
            "Lloyd, please come and\x01",
            "see us if you ever need\x01",
            "our help.\x02\x03",
            "#03204F...Lau, we're leaving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Sir.\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x0)

    def lambda_7A4D():
        OP_9B(0x1, 0x101, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A4D)
    Sleep(50)

    def lambda_7A65():
        OP_9B(0x1, 0x102, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A65)

    def lambda_7A7A():
        OP_9B(0x1, 0x109, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7A7A)
    Sleep(50)

    def lambda_7A92():
        OP_9B(0x1, 0x105, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7A92)
    Sleep(50)

    def lambda_7AAA():
        OP_95(0x15, -2500, 0, 1660, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7AAA)
    Sleep(500)
    OP_96(0x16, 0x0, 0x0, 0x898, 0x7D0, 0x0)

    def lambda_7ADB():
        OP_95(0x15, -12000, 0, 1660, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7ADB)

    def lambda_7AF5():
        OP_95(0x16, -12000, 0, 1560, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_7AF5)

    def lambda_7B0F():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B0F)
    Sleep(50)

    def lambda_7B1F():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7B1F)
    Sleep(50)

    def lambda_7B2F():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7B2F)
    Sleep(50)

    def lambda_7B3F():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7B3F)
    Sleep(50)

    def lambda_7B4F():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7B4F)
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
            "#12P#10101FH-He's an incredible\x01",
            "man.\x02\x03",
            "#10106FAlthough I felt like a\x01",
            "frog being watched by a\x01",
            "snake...\x02",
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
            "#6P#10300FSo that's White Orchid\x01",
            "Dragon Cao Lee, youngest of\x01",
            "the Heiyue leaders, huh.\x02\x03",
            "#10306FHe's shrewder than the\x01",
            "rumors say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYeah, he's always like\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(240, 1750, 1140, 3000)
    MoveCamera(326, 26, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(12930, 3000)

    def lambda_7D68():
        OP_93(0x14, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7D68)

    def lambda_7D75():
        OP_95(0x101, 500, 0, 2660, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D75)
    Sleep(100)

    def lambda_7D92():
        OP_95(0x102, -710, 0, 1990, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7D92)
    Sleep(100)

    def lambda_7DAF():
        OP_95(0x109, 900, 0, 1300, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7DAF)
    Sleep(100)

    def lambda_7DCC():
        OP_95(0x105, -270, 0, 760, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7DCC)
    WaitChrThread(0x101, 1)

    def lambda_7DEA():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7DEA)
    WaitChrThread(0x102, 1)

    def lambda_7DFB():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7DFB)
    WaitChrThread(0x109, 1)

    def lambda_7E0C():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7E0C)
    WaitChrThread(0x105, 1)

    def lambda_7E1D():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7E1D)
    OP_6F(0x79)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#12P#00001F─Grace, is Heiyue\x01",
            "interested in the old\x01",
            "Revache building?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#02101FYes. It seems they intend to buy\x01",
            "it and the warehouses together in\x01",
            "one fell swoop.\x02\x03",
            "#02103FIf Heiyue controls this place,\x01",
            "they'll have the whole Crossbell\x01",
            "underworld under their control...\x02\x03",
            "#02101FThis is a troubling development.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F...I agree.\x02\x03",
            "#00006FBut, we witnessed a\x01",
            "great scene on our way\x01",
            "to an investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FRight, we should\x01",
            "probably inform Section\x01",
            "One about this, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x14,
        (
            "#5P#02105FHuh? You guys didn't\x01",
            "come to look into Cao's\x01",
            "actions?\x02\x03",
            "#02102FAre you on a different\x01",
            "case?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FNo, you see...\x02\x03",
            "#00003F(That's right... It seems like\x01",
            "Grace met him before...)\x02\x03",
            "#00001F...Actually, we're looking for\x01",
            "someone else you met before,\x01",
            "Grace.\x02\x03",
            "His name's Lechter. He was the\x01",
            "one who defeated the miner at\x01",
            "the casino back then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#02105FOh, is that right?\x02\x03",
            "#02103FI saw him at The Old\x01",
            "Dragon just now.\x02",
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
        "#12P#00011FHuh!?\x02",
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
            "#5P#02100FYeah. He looked like a vacationer.\x01",
            "It looked like he was enjoying a\x01",
            "meal without a care in the world.\x02\x03",
            "#02103FI was hurrying here, so I didn't\x01",
            "get a chance to speak with him...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x14,
        (
            "#5P#02105FWait, I can't stay here.\x02\x03",
            "#02101FAt the very least, I've\x01",
            "got to get some more\x01",
            "juicy info out of Cao.\x02\x03",
            "#02109F...Bye! Let's get dinner\x01",
            "again sometime!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_840F():
        OP_93(0x101, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_840F)

    def lambda_841C():
        OP_93(0x102, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_841C)

    def lambda_8429():
        OP_93(0x109, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8429)

    def lambda_8436():
        OP_93(0x105, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8436)
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

    def lambda_8498():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8498)
    Sleep(100)

    ChrTalk(
        0x105,
        (
            "#6P#10300FBut, we got an\x01",
            "eyewitness report,\x01",
            "didn't we?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_84E4():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_84E4)

    def lambda_84F1():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_84F1)

    def lambda_84FE():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_84FE)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#5P#00100FYeah, let's hurry to The\x01",
            "Old Dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FRoger that!\x02",
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

    # Function_30_6DB5 end

    def Function_31_85BF(): pass

    label("Function_31_85BF")

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

    def lambda_8691():
        OP_95(0x101, 15750, 0, 1500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8691)
    Sleep(50)

    def lambda_86AE():
        OP_95(0x102, 16750, 0, 1200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_86AE)
    Sleep(50)

    def lambda_86CB():
        OP_95(0x109, 17750, 0, 1500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_86CB)
    Sleep(50)

    def lambda_86E8():
        OP_95(0x105, 18750, 0, 2350, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_86E8)
    Sleep(50)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_8713():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8713)
    WaitChrThread(0x102, 1)

    def lambda_8724():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8724)
    WaitChrThread(0x109, 1)

    def lambda_8735():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8735)
    WaitChrThread(0x105, 1)

    def lambda_8746():
        OP_93(0x105, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8746)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x109,
        (
            "#12P#10111FHe really did come\x01",
            "through here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHaha. I wonder if he\x01",
            "prepared it especially\x01",
            "for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FA-Anyway, let's track\x01",
            "him down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FYeah. We'll have to ask\x01",
            "everyone who passed\x01",
            "through here.\x02",
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

    # Function_31_85BF end

    def Function_32_887D(): pass

    label("Function_32_887D")

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
            "#00106F*sigh*. That sure took a while,\x01",
            "but this ends our investigation\x01",
            "of the "Imperial Fishing Club".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, that's right.\x02",
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AC9")
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
            "◆Investigation Status?\x01",
            "(Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No Change]\x01",                          # 0
            "[Investigations Remaining]\x01",           # 1
            "[All 6 Investigations Finished]\x01",      # 2
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
        (0, "loc_8AA2"),
        (1, "loc_8AA7"),
        (2, "loc_8AB8"),
        (SWITCH_DEFAULT, "loc_8AC9"),
    )


    label("loc_8AA2")

    Jump("loc_8AC9")

    label("loc_8AA7")

    ClearScenarioFlags(0x131, 5)
    ClearScenarioFlags(0x131, 6)
    ClearScenarioFlags(0x131, 7)
    ClearScenarioFlags(0x132, 2)
    Jump("loc_8AC9")

    label("loc_8AB8")

    SetScenarioFlags(0x131, 5)
    SetScenarioFlags(0x131, 6)
    SetScenarioFlags(0x131, 7)
    SetScenarioFlags(0x132, 2)
    Jump("loc_8AC9")

    label("loc_8AC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B23")

    ChrTalk(
        0x101,
        (
            "#00000FAlright, then let's\x01",
            "continue our\x01",
            "investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B9F")

    label("loc_8B23")

    OP_29(0x6A, 0x1, 0x6)

    ChrTalk(
        0x101,
        (
            "#00000FAlright, this wraps up\x01",
            "our investigations.\x02\x03",
            "Let's head back to the\x01",
            "City Meeting Hall and\x01",
            "make our report.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B9F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※You can now access the\x01",
            "[Fishing] minigame.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※In places there is water, such as on\x01",
            "highways or within the city, there are\x01",
            "[Fishing Spots] where ripples appear.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※By examining a fishing spot\x01",
            "and choosing a rod and bait,\x01",
            "Lloyd will begin to fish.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※If you quickly press ○ when the ！ mark\x01",
            "appears, you can pull in the fish. (If\x01",
            "you are unlucky, it can also get away.)\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※In Crossbell City, there are\x01",
            "fishing spots at Waterfront\x01",
            "Area and Residential Street.\x07\x00\x02",
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

    # Function_32_887D end

    def Function_33_8DFA(): pass

    label("Function_33_8DFA")

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
            "#12404FGood work, everyone.\x02\x03",
            "Thanks to you, I was able to\x01",
            "collect this thing before it\x01",
            "made too much of a disturbance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha... We're happy to\x01",
            "have been of service.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x1E, 500)

    ChrTalk(
        0x1F,
        (
            "#5P#13900FHmph... There's no need to refer\x01",
            "to me as "it". You make it sound\x01",
            "as if you're handling an object.\x02\x03",
            "#13903F...Well, I suppose such\x01",
            "treatment has its own charm and\x01",
            "might not be too bad.\x02\x03",
            "#13912FFrom now on, please treat me\x01",
            "that way sometimes, Mueller㈱\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x1F, 500)

    ChrTalk(
        0x1E,
        "#12401F#4S#250WShut#250W it#250W.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "#5P#13910F...Sorry.\x02",
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
            "#12400FSorry. I've known this idiot\x01",
            "for a long time.\x02\x03",
            "#12406FBecause his antics escalate\x01",
            "every time, I have to strictly\x01",
            "discipline him every so often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FHaha, that sounds pretty\x01",
            "difficult.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x101, 500)

    ChrTalk(
        0x1F,
        (
            "#13904FWhat are you saying? It's\x01",
            "helpful to have a friend who\x01",
            "will always cover for you.\x02\x03",
            "#13909FHmph, I am truly gifted to\x01",
            "have such a friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FYou should tell that to\x01",
            "him, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FHehe. I wonder if he\x01",
            "regrets his actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#12400F...I believe so.\x02\x03",
            "I'll give him a stern\x01",
            "lecture later, so he'd\x01",
            "better prepare himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#5P#13911FN-No, please! It was\x01",
            "just a little joke...\x02\x03",
            "#13910FCan you guys not egg him\x01",
            "on, please?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FA-Ahaha... (In a sense,\x01",
            "I guess they do get\x01",
            "along...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#12400FI must be going, then.\x02\x03",
            "#12404FYou helped me during\x01",
            "this busy time. Allow me\x01",
            "to thank you once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FDon't mention it. This sort\x01",
            "of thing is our job.\x02\x03",
            "#00006FI'm not sure how to say this,\x01",
            "but... Please be careful not\x01",
            "to take your eyes off him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#12406F...Oh yes, I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#13910F*sigh*, man... So this is\x01",
            "how my fun time ends, huh.\x02\x03",
            "#13900FI bid you farewell, ladies\x01",
            "and gentlemen. If fate wills\x01",
            "it, we shall meet again.\x02",
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
            "#13910FWell, I personally wanted to go see that\x01",
            "theme park.\x02\x03",
            "#13905FOh, that's right folks. Can I ask you to\x01",
            "take me there now?\x02\x03",
            "#13904FHaha, a good idea, if I do say so myself.\x01",
            "If he has a little fun, I bet even the\x01",
            "crease between Mueller's eyebrows would...\x02",
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
            "#13911FAh, Mueller!? I-It was\x01",
            "just a little joke!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x13B, 0x0)
    SetChrChipByIndex(0x1F, 0x20)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x20)

    def lambda_97D9():
        OP_95(0xFE, 2000, 0, 1310, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_97D9)
    Sleep(50)

    def lambda_97F6():
        OP_96(0xFE, 0x7D0, 0x0, 0x4F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_97F6)
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
            "#00012FYou don't run into\x01",
            "people like that every\x01",
            "day, do you.\x02\x03",
            "#00003FActually though, just\x01",
            "what kind of people were\x01",
            "they, I wonder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, we can always ask\x01",
            "when we see them next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FHonestly, they looked\x01",
            "very worn-out, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#00103F(I threatened him by\x01",
            "mistake back there,\x01",
            "but... Could he be...?)\x02\x03",
            "#00109F(...No. That's\x01",
            "impossible.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#00005FYou've been quiet, Elie.\x01",
            "What's wrong?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#11P#00102FN-Nevermind. It's\x01",
            "nothing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00303FWell, case closed for\x01",
            "now.\x02\x03",
            "#00300FLet's go, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9B06():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B06)
    Sleep(50)

    def lambda_9B16():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9B16)
    Sleep(300)
    OP_62(0x101)

    ChrTalk(
        0x101,
        "#11P#00000FYeah, let's.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x24, 3)
    NewScene("c0100", 100, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_33_8DFA end

    def Function_34_9B5B(): pass

    label("Function_34_9B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9B69")
    Jump("loc_A014")

    label("loc_9B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9B77")
    Jump("loc_A014")

    label("loc_9B77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9B85")
    Jump("loc_A014")

    label("loc_9B85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9DA1")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CB5")

    ChrTalk(
        0x101,
        (
            "#00001FCrimson & Co. is this\x01",
            "way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FUncle and the others seem to have\x01",
            "been keeping a low profile since\x01",
            "the trade conference incident.\x02\x03",
            "#00301FEven if we go there, we won't get\x01",
            "any decent information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah... Let's refrain\x01",
            "from going there for\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_9D89")

    label("loc_9CB5")


    ChrTalk(
        0x101,
        (
            "#00003FIt appears that Crimson & Co. has\x01",
            "been keeping a low profile since\x01",
            "the trade conference incident.\x02\x03",
            "#00001FWe won't be able to get any\x01",
            "important information, so let's\x01",
            "refrain from going there for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D89")

    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)
    Jump("loc_A014")

    label("loc_9DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9E57")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FCrimson & Co. should be\x01",
            "under the surveillance of\x01",
            "Section One.\x02\x03",
            "Let's leave this place to\x01",
            "Section One and concentrate\x01",
            "on our own jobs.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)
    Jump("loc_A014")

    label("loc_9E57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9F4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E72")
    Call(0, 11)
    Jump("loc_9F46")

    label("loc_9E72")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003FIt appears we won't be able\x01",
            "to learn anything about Red\x01",
            "Constellation's actions here.\x02\x03",
            "#00000FLet's keep dealing with\x01",
            "support requests and asking\x01",
            "about them everywhere we can.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)

    label("loc_9F46")

    Jump("loc_A014")

    label("loc_9F4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_9F59")
    Jump("loc_A014")

    label("loc_9F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_9F67")
    Jump("loc_A014")

    label("loc_9F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A014")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A014")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F8C")
    Call(0, 10)
    Jump("loc_A014")

    label("loc_9F8C")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FIt looks like that the real\x01",
            "estate agent is waiting for\x01",
            "a negotiator now.\x02\x03",
            "We're in his way. Let's go.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)

    label("loc_A014")

    Return()

    # Function_34_9B5B end

    def Function_35_A015(): pass

    label("Function_35_A015")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_A076")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears to be locked.\x01",
            "There is no sign of\x01",
            "anyone inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_A19C")

    label("loc_A076")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A0D4")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears to be locked.\x01",
            "There is no sign of\x01",
            "anyone inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_A19C")

    label("loc_A0D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A148")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0F3")
    TalkEnd(0xFF)
    Call(0, 12)
    Return()

    label("loc_A0F3")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears to be locked.\x01",
            "There is no sign of\x01",
            "anyone inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_A19C")

    label("loc_A148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A156")
    Jump("loc_A19C")

    label("loc_A156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A164")
    Jump("loc_A19C")

    label("loc_A164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A19C")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It looks like it's locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_A19C")

    TalkEnd(0xFF)
    Return()

    # Function_35_A015 end

    def Function_36_A1A0(): pass

    label("Function_36_A1A0")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ Times Department Store ※\x01",
            " ※ Employee Entrance Only ※\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_36_A1A0 end

    def Function_37_A205(): pass

    label("Function_37_A205")

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

    # Function_37_A205 end

    def Function_38_A237(): pass

    label("Function_38_A237")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FLet's chase after Randy...\x01",
            "Let's hurry to the\x01",
            "abandoned Revache building!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -24330, 0, 210, 90)
    EventEnd(0x4)
    Return()

    # Function_38_A237 end

    def Function_39_A2A4(): pass

    label("Function_39_A2A4")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FLet's chase after Randy...\x01",
            "Let's hurry to the\x01",
            "abandoned Revache building!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 19310, 0, 650, 270)
    EventEnd(0x4)
    Return()

    # Function_39_A2A4 end

    SaveToFile()

Try(main)
