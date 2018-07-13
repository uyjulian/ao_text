from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c120b.bin",                # FileName
        "c120b",                    # MapName
        "c120b",                    # Location
        0x001A,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 26, 0, 1, 0, 2],
    )

    BuildStringList((
        "c120b",                  # 0
        "Guard Paul",             # 1
        "Receptionist Lanfei",    # 2
        "Chief Roberts",          # 3
        "Jona",                   # 4
        "Guard Bills",            # 5
        "Guard Wong",             # 6
        "Researcher Clay",        # 7
        "Researcher David",       # 8
        "Trader Rizel",           # 9
        "IBC Customer A",         # 10
        "Jaeger",                 # 11
        "Jaeger",                 # 12
        "Jaeger",                 # 13
        "Jaeger",                 # 14
        "Jaeger",                 # 15
        "Jaeger",                 # 16
        "Ogre Sigmund",           # 17
        "Member",                 # 18
        "Member",                 # 19
        "Member",                 # 20
        "Member",                 # 21
        "Member",                 # 22
        "Member",                 # 23
        "Lau",                    # 24
        "車",                     # 25
        "Crescent Moon Ring",     # 26
        "Crescent Moon Ring",     # 27
        "Mob",                    # 28
        "SE制御",                 # 29
        "Central Square",         # 30
        "West Street",            # 31
        "Governmental District",  # 32
        "Residential Street",     # 33
        "Entertainment District", # 34
        "East Street",            # 35
        "Downtown",               # 36
        "Waterfront Area",        # 37
        "IBC",                    # 38
        "Station Street",         # 39
        "Back Street",            # 40
        "St. Ursula Byroad",      # 41
        "East Crossbell Highway", # 42
        "West Crossbell HIghway", # 43
        "Mainz Mountain Road",    # 44
        "Orchis Tower",           # 45
    ))

    AddCharChip((
        "chr/ch28600.itc",                   # 00
        "chr/ch27900.itc",                   # 01
        "chr/ch29300.itc",                   # 02
        "chr/ch06100.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(2720,    2000,    23920,   0,    385,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(1309,    2000,    24540,   0,    385,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(7329,    2000,    22520,   0,    385,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(5929,    2000,    23920,   0,    385,  0x0, 0,   3,   0,   0,   0,   0,   4,   255,  0)
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
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 62,  4.5,                   28.0,                  1.0,                   400.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.44999998807907104,  -7.0,                  -0.19999998807907104,  1.0])

    DeclActor(16750,   4294966296, 4294951556, 1200,    16750,   0,       4294951556, 0x007C, 0,  3,  0x0000)
    DeclActor(21600,   0,       17000,   3000,    21600,   2000,    18500,   0x007C, 0,  66, 0x0000)
    DeclActor(4294949096, 0,       4294948296, 3000,    4294949096, 2000,    4294948296, 0x007C, 0,  67, 0x0000)
    DeclActor(77220,   4294964796, 20290,   2000,    77220,   4294966296, 20290,   0x007C, 0,  70, 0x0000)

    PlaceName(-123.13999938964844, 0.0, -85.1500015258789, 0x0000, 0x0000, "Central Square")
    PlaceName(-209.27000427246094, 0.0, -79.26000213623047, 0x0000, 0x0000, "West Street")
    PlaceName(-87.7699966430664, 0.0, 31.440000534057617, 0x0000, 0x0000, "Governmental District")
    PlaceName(-289.17999267578125, 0.0, 18.34000015258789, 0x0000, 0x0000, "Residential Street")
    PlaceName(-193.5500030517578, 0.0, 7.860000133514404, 0x0000, 0x0000, "Entertainment District")
    PlaceName(-16.700000762939453, 0.0, -115.27999877929688, 0x0000, 0x0000, "East Street")
    PlaceName(29.799999237060547, 0.0, -187.3300018310547, 0x0000, 0x0000, "Downtown")
    PlaceName(19.979999542236328, 0.0, -28.81999969482422, 0x0000, 0x0000, "Waterfront Area")
    PlaceName(-14.079999923706055, 0.0, 94.31999969482422, 0x0000, 0x0000, "IBC")
    PlaceName(-108.4000015258789, 0.0, -175.5399932861328, 0x0000, 0x0000, "Station Street")
    PlaceName(-169.97000122070312, 0.0, -39.29999923706055, 0x0000, 0x0000, "Back Street")
    PlaceName(-112.33000183105469, 0.0, -216.14999389648438, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(54.040000915527344, 0.0, -96.94000244140625, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-276.0799865722656, 0.0, -81.22000122070312, 0x0000, 0x0000, "West Crossbell HIghway")
    PlaceName(-268.2200012207031, 0.0, 49.779998779296875, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(-96.5, 0.0, 203.75, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(-151.9600067138672, 0.0, -103.48999786376953, 0x0000, 0x0051, "")
    PlaceName(-81.55000305175781, 0.0, -69.43000030517578, 0x0000, 0x0054, "")
    PlaceName(-119.87000274658203, 0.0, -113.97000122070312, 0x0000, 0x0057, "")
    PlaceName(-152.94000244140625, 0.0, -65.5, 0x0000, 0x0053, "")
    PlaceName(-126.08999633789062, 0.0, -34.060001373291016, 0x0000, 0x0053, "")
    PlaceName(-192.57000732421875, 0.0, -72.05000305175781, 0x0000, 0x0053, "")
    PlaceName(-205.33999633789062, 0.0, -44.540000915527344, 0x0000, 0x0053, "")
    PlaceName(-173.89999389648438, 0.0, -2.619999885559082, 0x0000, 0x0052, "")
    PlaceName(-167.67999267578125, 0.0, -19.649999618530273, 0x0000, 0x0053, "")
    PlaceName(-156.22000122070312, 0.0, -30.790000915527344, 0x0000, 0x0053, "")
    PlaceName(-118.87999725341797, 0.0, 62.22999954223633, 0x0000, 0x0051, "")
    PlaceName(27.84000015258789, 0.0, -115.27999877929688, 0x0000, 0x0052, "")
    PlaceName(5.570000171661377, 0.0, -233.83999633789062, 0x0000, 0x0053, "")
    PlaceName(-11.460000038146973, 0.0, -209.60000610351562, 0x0000, 0x0053, "")

    ChipFrameInfo(2204, 0)                                       # 0

    ScpFunction((
        "Function_0_89C",          # 00, 0
        "Function_1_94C",          # 01, 1
        "Function_2_9C3",          # 02, 2
        "Function_3_D47",          # 03, 3
        "Function_4_E99",          # 04, 4
        "Function_5_1058",         # 05, 5
        "Function_6_120D",         # 06, 6
        "Function_7_131B",         # 07, 7
        "Function_8_1509",         # 08, 8
        "Function_9_16AF",         # 09, 9
        "Function_10_1730",        # 0A, 10
        "Function_11_17C4",        # 0B, 11
        "Function_12_17DA",        # 0C, 12
        "Function_13_17EA",        # 0D, 13
        "Function_14_3246",        # 0E, 14
        "Function_15_327F",        # 0F, 15
        "Function_16_32B8",        # 10, 16
        "Function_17_33B4",        # 11, 17
        "Function_18_3496",        # 12, 18
        "Function_19_3510",        # 13, 19
        "Function_20_3606",        # 14, 20
        "Function_21_36F7",        # 15, 21
        "Function_22_3771",        # 16, 22
        "Function_23_385D",        # 17, 23
        "Function_24_3947",        # 18, 24
        "Function_25_39C1",        # 19, 25
        "Function_26_3AF6",        # 1A, 26
        "Function_27_3BBF",        # 1B, 27
        "Function_28_3C61",        # 1C, 28
        "Function_29_3DC1",        # 1D, 29
        "Function_30_3EDA",        # 1E, 30
        "Function_31_3F54",        # 1F, 31
        "Function_32_408D",        # 20, 32
        "Function_33_4192",        # 21, 33
        "Function_34_4215",        # 22, 34
        "Function_35_422D",        # 23, 35
        "Function_36_4281",        # 24, 36
        "Function_37_42B5",        # 25, 37
        "Function_38_430D",        # 26, 38
        "Function_39_43AE",        # 27, 39
        "Function_40_450A",        # 28, 40
        "Function_41_45F4",        # 29, 41
        "Function_42_460C",        # 2A, 42
        "Function_43_4681",        # 2B, 43
        "Function_44_47A9",        # 2C, 44
        "Function_45_481D",        # 2D, 45
        "Function_46_4835",        # 2E, 46
        "Function_47_4894",        # 2F, 47
        "Function_48_48B0",        # 30, 48
        "Function_49_48CC",        # 31, 49
        "Function_50_48E8",        # 32, 50
        "Function_51_4A6E",        # 33, 51
        "Function_52_4B11",        # 34, 52
        "Function_53_4BEC",        # 35, 53
        "Function_54_4C5F",        # 36, 54
        "Function_55_4CD5",        # 37, 55
        "Function_56_4D4B",        # 38, 56
        "Function_57_4DA3",        # 39, 57
        "Function_58_4DFB",        # 3A, 58
        "Function_59_4E53",        # 3B, 59
        "Function_60_5AE7",        # 3C, 60
        "Function_61_5B97",        # 3D, 61
        "Function_62_5C0B",        # 3E, 62
        "Function_63_5DAB",        # 3F, 63
        "Function_64_67D9",        # 40, 64
        "Function_65_6819",        # 41, 65
        "Function_66_687A",        # 42, 66
        "Function_67_6D35",        # 43, 67
        "Function_68_6EBF",        # 44, 68
        "Function_69_6F13",        # 45, 69
        "Function_70_6F67",        # 46, 70
    ))


    def Function_0_89C(): pass

    label("Function_0_89C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_8D4"),
        (1, "loc_8E0"),
        (2, "loc_8EC"),
        (3, "loc_8F8"),
        (4, "loc_904"),
        (5, "loc_910"),
        (6, "loc_91C"),
        (SWITCH_DEFAULT, "loc_928"),
    )


    label("loc_8D4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_934")

    label("loc_8E0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_934")

    label("loc_8EC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_934")

    label("loc_8F8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_934")

    label("loc_904")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_934")

    label("loc_910")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_934")

    label("loc_91C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_934")

    label("loc_928")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_934")

    label("loc_934")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_94B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_934")

    label("loc_94B")

    Return()

    # Function_0_89C end

    def Function_1_94C(): pass

    label("Function_1_94C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_95A")
    Jump("loc_977")

    label("loc_95A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 1)), scpexpr(EXPR_END)), "loc_977")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_977")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_98B")
    ClearScenarioFlags(0x22, 0)
    Event(0, 8)
    Jump("loc_9C2")

    label("loc_98B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_99F")
    ClearScenarioFlags(0x22, 1)
    Event(0, 13)
    Jump("loc_9C2")

    label("loc_99F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_9B3")
    ClearScenarioFlags(0x22, 2)
    Event(0, 59)
    Jump("loc_9C2")

    label("loc_9B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_9C2")
    ClearScenarioFlags(0x22, 3)
    Event(0, 63)

    label("loc_9C2")

    Return()

    # Function_1_94C end

    def Function_2_9C3(): pass

    label("Function_2_9C3")

    SoundDistance(0x7E, 0x13E3E, 0x0, 0xFFFF8972, 0x13880, 0xC350, 0x64, 0x0)
    OP_E3(0x13DE4, 0x0, 0x71E8)
    OP_E3(0x13C54, 0x0, 0xD1B0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A0D")
    Sound(868, 1, 60, 0)

    label("loc_A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A20")
    OP_70(0x11, 0x0)
    Jump("loc_A24")

    label("loc_A20")

    OP_70(0x11, 0x1E)

    label("loc_A24")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A3C")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_A3C")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 19000, 10, 16000, 6000, 2000, 0)
    OP_10(0x6, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A70")
    OP_10(0x6, 0x1)
    OP_10(0x1, 0x0)

    label("loc_A70")

    OP_1B(0x0, 0x0, 0x44)
    OP_1B(0x2, 0x0, 0x45)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A90")
    OP_66(0x1, 0x1)

    label("loc_A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C72")
    LoadEffect(0x9, "event/ev15021.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 200000, 300000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "kurotuki00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "knuki", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lwindow2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ent2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kurotuki01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kurotuki01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x1, 0x1)
    SetMapObjFrame(0xFF, "bfire00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "bfire01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "fire00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "fire01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "fire02_add", 0x1, 0x1)
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    ClearChrFlags(0x20, 0x80)
    OP_78(0x12, 0x20)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    OP_74(0x12, 0x1E)
    OP_70(0x12, 0x0)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    SetChrPos(0x20, -18200, 0, -19000, 0)
    Jump("loc_D46")

    label("loc_C72")

    SetMapObjFrame(0xFF, "kurotuki00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "knuki", 0x1, 0x1)
    SetMapObjFrame(0xFF, "lwindow2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ent2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kurotuki01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kurotuki01a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bfire00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bfire01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire02_add", 0x0, 0x1)
    SetMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x14, 0x4)

    label("loc_D46")

    Return()

    # Function_2_9C3 end

    def Function_3_D47(): pass

    label("Function_3_D47")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E43")
    Sound(14, 0, 100, 0)
    OP_74(0x11, 0x1E)
    OP_71(0x11, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1D7, 1)"), scpexpr(EXPR_END)), "loc_DCC")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_E3E")

    label("loc_DCC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x11, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E3E")

    Jump("loc_E8D")

    label("loc_E43")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the chest. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_E8D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_D47 end

    def Function_4_E99(): pass

    label("Function_4_E99")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB6")

    ChrTalk(
        0xB,
        (
            "#02306FInformation about them occasionally\x01",
            "flows in the orbal net too...\x02\x03",
            "#02310FDidn't you hear that those\x01",
            "guys are really bad news!?\x02\x03",
            "#02301FIf you intend to head there,\x01",
            "be sure to be very careful!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYeah...\x01",
            "You too, be careful and find shelter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1054")

    label("loc_FB6")


    ChrTalk(
        0xB,
        (
            "#02306FThose guys... Especially that redheaded\x01",
            "old man is too much bad news, you know.\x02\x03",
            "#02301FIf you intend to head there,\x01",
            "be sure to be very careful!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1054")

    TalkEnd(0xFE)
    Return()

    # Function_4_E99 end

    def Function_5_1058(): pass

    label("Function_5_1058")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1065")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1209")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                 # 0
            "Ask for Healing\x01",      # 1
            "Quit\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1135")

    ChrTalk(
        0xFE,
        "Alright, leave it to me.\x02",
    )

    CloseMessageWindow()
    OP_60(0x0)
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)

    ChrTalk(
        0xFE,
        "Be careful!\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1204")

    label("loc_1135")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1149")
    Jump("loc_1204")

    label("loc_1149")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1204")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "I took with me a mobile recovery\x01",
            "equipment in development at the\x01",
            "Epstein Foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, you can tell me whenever\x01",
            "you want if you need treatment!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1204")

    Jump("loc_1065")

    label("loc_1209")

    TalkEnd(0xFE)
    Return()

    # Function_5_1058 end

    def Function_6_120D(): pass

    label("Function_6_120D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B9")

    ChrTalk(
        0xFE,
        "Such monsters are in the city too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A-At any rate,\x01",
            "please leave the\x01",
            "people here to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll take responsibility\x01",
            "to make them evacuate.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1317")

    label("loc_12B9")


    ChrTalk(
        0xFE,
        (
            "Please leave the\x01",
            "people here to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll take responsibility\x01",
            "to make them evacuate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1317")

    TalkEnd(0xFE)
    Return()

    # Function_6_120D end

    def Function_7_131B(): pass

    label("Function_7_131B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1465")

    ChrTalk(
        0xFE,
        "Everyone, take these...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x5 received.\x02",
        )
    )

    AddItemNumber(0x1F5, 5)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 received.\x02",
        )
    )

    AddItemNumber(0x1FC, 2)
    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    ChrTalk(
        0xFE,
        (
            "They are something that were\x01",
            "at the reception for emergencies.\x01",
            "Please use them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FThank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FPlease be careful too,\x01",
            "Miss Lanfei...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x190, 0)
    Jump("loc_1505")

    label("loc_1465")


    ChrTalk(
        0xFE,
        "Why in the world did such a thing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was relieved since milady Mariabell\x01",
            "is on a business trip, but I still can't\x01",
            "sort out the thoughts in my head.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1505")

    TalkEnd(0xFE)
    Return()

    # Function_7_131B end

    def Function_8_1509(): pass

    label("Function_8_1509")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrFlags(0x153, 0x8)
    SoundLoad(468)
    ClearChrFlags(0x20, 0x80)
    OP_78(0x12, 0x20)
    OP_49()
    SetChrPos(0x20, -20150, 2000, 23000, 90)
    OP_D5(0x20, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0x79, 0xB4, 0x1, 0x20)
    SetMapObjFlags(0x13, 0x1000)
    OP_71(0x13, 0x12D, 0x168, 0x0, 0x20)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15C7")
    ClearChrFlags(0x23, 0x80)
    LoadChrToIndex("chr/ch25200.itc", 0x1E)
    SetChrChipByIndex(0x23, 0x1E)
    SetChrSubChip(0x23, 0x0)
    BeginChrThread(0x23, 0, 0, 0)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -7500, 0, 12700, 0)

    label("loc_15C7")

    FadeToBright(1000, 0)
    BeginChrThread(0x20, 3, 0, 9)
    BeginChrThread(0x24, 1, 0, 11)
    OP_68(-3550, 1500, 30000, 0)
    MoveCamera(60, 8, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(37150, 0)
    OP_68(3700, 1500, 17800, 10000)
    Sleep(8500)
    OP_0D()
    Fade(500)
    EndChrThread(0x20, 0x3)
    EndChrThread(0x24, 0x1)
    BeginChrThread(0x20, 3, 0, 10)
    BeginChrThread(0x24, 1, 0, 12)
    OP_68(14550, 2200, -6000, 0)
    MoveCamera(65, 9, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20500, 0)
    OP_68(-10600, 1000, -12600, 10500)
    MoveCamera(65, 18, 0, 10500)
    SetCameraDistance(33650, 10500)
    Sleep(8500)
    StopSound(468, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 0)
    NewScene("c100B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1509 end

    def Function_9_16AF(): pass

    label("Function_9_16AF")

    SetChrPos(0xFE, -20150, 2000, 23000, 90)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -2900, 2000, 23000)
    OP_9F(0x1, 1650, 2000, 23000)
    OP_9F(0x1, 3750, 2000, 20000)
    OP_9F(0x1, 4350, 350, 14700)
    OP_9F(0x1, 7440, 150, 12600)
    OP_9F(0x1, 12390, 150, 11900)
    OP_9F(0x1, 17950, 150, 10200)
    OP_9F(0x2, 0xFE, 5000, 0x6)
    Return()

    # Function_9_16AF end

    def Function_10_1730(): pass

    label("Function_10_1730")

    SetChrPos(0xFE, 20000, 0, 2350, 180)
    OP_D5(0x20, 0x0, 0x2BF20, 0x0, 0x0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 20000, 0, -8300)
    OP_9F(0x1, 15500, 0, -11000)
    OP_9F(0x1, 9500, 0, -11000)
    OP_9F(0x1, -5500, 0, -11000)
    OP_9F(0x1, -12000, 0, -11000)
    OP_9F(0x1, -17500, 0, -12000)
    OP_9F(0x1, -18500, 0, -25800)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_10_1730 end

    def Function_11_17C4(): pass

    label("Function_11_17C4")

    Sound(468, 2, 100, 0)
    Sound(457, 0, 100, 0)
    Sleep(4000)
    Sound(493, 0, 70, 0)
    Return()

    # Function_11_17C4 end

    def Function_12_17DA(): pass

    label("Function_12_17DA")

    Sound(458, 0, 100, 0)
    Sleep(6000)
    Sound(493, 0, 70, 0)
    Return()

    # Function_12_17DA end

    def Function_13_17EA(): pass

    label("Function_13_17EA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04500.itp")
    LoadChrToIndex("chr/ch03350.itc", 0x23)
    LoadChrToIndex("chr/ch03351.itc", 0x24)
    LoadChrToIndex("chr/ch03352.itc", 0x25)
    LoadChrToIndex("apl/ch51535.itc", 0x26)
    LoadChrToIndex("chr/ch03354.itc", 0x27)
    LoadChrToIndex("chr/ch41950.itc", 0x37)
    LoadChrToIndex("chr/ch41951.itc", 0x38)
    LoadChrToIndex("chr/ch41952.itc", 0x39)
    LoadChrToIndex("apl/ch51537.itc", 0x3A)
    LoadChrToIndex("chr/ch41953.itc", 0x3B)
    LoadChrToIndex("chr/ch42050.itc", 0x3C)
    LoadChrToIndex("chr/ch42051.itc", 0x3D)
    LoadChrToIndex("chr/ch42052.itc", 0x3E)
    LoadChrToIndex("apl/ch51536.itc", 0x3F)
    LoadChrToIndex("chr/ch42053.itc", 0x40)
    LoadChrToIndex("chr/ch42056.itc", 0x41)
    LoadChrToIndex("chr/ch31400.itc", 0x28)
    LoadChrToIndex("chr/ch31452.itc", 0x29)
    LoadChrToIndex("chr/ch31500.itc", 0x2D)
    LoadChrToIndex("chr/ch31551.itc", 0x2E)
    LoadChrToIndex("chr/ch31552.itc", 0x2F)
    LoadChrToIndex("chr/ch31553.itc", 0x30)
    LoadChrToIndex("chr/ch31556.itc", 0x31)
    LoadChrToIndex("chr/ch12500.itc", 0x32)
    LoadChrToIndex("chr/ch12551.itc", 0x33)
    LoadChrToIndex("chr/ch12552.itc", 0x34)
    LoadChrToIndex("chr/ch12553.itc", 0x35)
    LoadChrToIndex("chr/ch12556.itc", 0x36)
    LoadEffect(0x0, "battle/btgun00.eff")
    LoadEffect(0x1, "event/ev15036.eff")
    LoadEffect(0x2, "battle/ms00001.eff")
    LoadEffect(0x3, "eff/cutin33.eff")
    LoadEffect(0x4, "battle/cr033300.eff")
    LoadEffect(0x5, "battle/cr033301.eff")
    LoadEffect(0x6, "event/ev15035.eff")
    LoadEffect(0x7, "event/ev15041.eff")
    LoadEffect(0x8, "battle/sp003000.eff")
    LoadEffect(0xA, "battle/cr004000.eff")
    LoadEffect(0x9, "event/ev15021.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 200000, 300000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundLoad(868)
    SoundLoad(865)
    SoundLoad(861)
    SoundLoad(926)
    SoundLoad(832)
    SoundLoad(3853)
    SoundLoad(3854)
    SoundLoad(3855)
    SetChrChipByIndex(0x18, 0x26)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    OP_52(0x18, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 0x3D)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x3D)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x38)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x38)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x38)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x38)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x1F, 0x28)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    OP_52(0x1F, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x19, 0x2D)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x32)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x2D)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x32)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x2D)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x32)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x21, 0x31)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x21, 0x2)
    SetChrChipByIndex(0x22, 0x36)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    SetChrFlags(0x22, 0x2)
    SetMapObjFrame(0xFF, "kurotuki01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kurotuki01a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bfire00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bfire01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fire02_add", 0x0, 0x1)
    SetMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_68(-8550, 4500, -9450, 0)
    MoveCamera(55, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(29000, 0)
    OP_68(-14250, 4500, 9750, 10000)
    MoveCamera(55, 5, 0, 10000)
    OP_6E(700, 10000)
    SetCameraDistance(29000, 10000)
    Sound(868, 2, 60, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(500)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x12, -29000, 2000, 21700, 90)
    SetChrPos(0x13, -30500, 2000, 23700, 90)
    SetChrPos(0x14, -31000, 2000, 21700, 90)
    SetChrPos(0x15, -32500, 2000, 23700, 90)
    SetChrPos(0x16, -33000, 2000, 21700, 90)
    SetChrPos(0x17, -34500, 2000, 23700, 90)
    OP_68(-27000, 3000, 22700, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13000, 0)
    OP_68(-15500, 3000, 22700, 4000)
    MoveCamera(335, 15, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(15000, 4000)

    def lambda_1D86():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1D86)
    Sleep(50)

    def lambda_1D9E():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1D9E)
    Sleep(50)

    def lambda_1DB6():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1DB6)
    Sleep(50)

    def lambda_1DCE():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1DCE)
    Sleep(50)

    def lambda_1DE6():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1DE6)
    Sleep(50)

    def lambda_1DFE():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1DFE)
    OP_0D()
    Sleep(3000)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x13, 0x1)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    Fade(500)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1F, 17300, 0, 13150, 270)
    SetChrPos(0x19, 19300, 0, 12150, 270)
    SetChrPos(0x1A, 19300, 0, 13150, 270)
    SetChrPos(0x1B, 19300, 0, 14150, 270)
    SetChrPos(0x1C, 20800, 0, 12150, 270)
    SetChrPos(0x1D, 20800, 0, 13150, 270)
    SetChrPos(0x1E, 20800, 0, 14150, 270)
    OP_68(17300, 1000, 13150, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15000, 1500)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x1F,
        "#11P──So they've come.\x02",
    )

    CloseMessageWindow()
    OP_68(19300, 1000, 13150, 1000)
    OP_6F(0x79)

    ChrTalk(
        0x1F,
        (
            "#11PWe'll defend this place to the last.\x01",
            "Don't let them get near the building!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Members")

    AnonymousTalk(
        0xFF,
        "#4SSir!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(17300, 1000, 13150, 500)
    Sound(250, 0, 100, 0)
    SetChrChipByIndex(0x19, 0x2E)
    BeginChrThread(0x19, 1, 0, 14)
    Sleep(50)
    SetChrChipByIndex(0x1B, 0x2E)
    BeginChrThread(0x1B, 1, 0, 15)
    Sleep(50)
    SetChrChipByIndex(0x1A, 0x33)
    BeginChrThread(0x1A, 1, 0, 14)
    Sleep(50)
    Sound(255, 0, 60, 0)
    SetChrChipByIndex(0x1E, 0x33)
    BeginChrThread(0x1E, 1, 0, 15)
    Sleep(50)
    SetChrChipByIndex(0x1C, 0x33)
    BeginChrThread(0x1C, 1, 0, 14)
    Sleep(50)
    SetChrChipByIndex(0x1D, 0x2E)
    BeginChrThread(0x1D, 1, 0, 15)
    Sleep(500)
    Fade(500)
    EndChrThread(0x19, 0x1)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1C, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1E, 0x1)
    SetChrChip(0x1, 0x19, 0x0, 0x0)
    SetChrChip(0x1, 0x1A, 0x0, 0x0)
    SetChrChip(0x1, 0x1B, 0x0, 0x0)
    SetChrChip(0x1, 0x1C, 0x0, 0x0)
    SetChrChip(0x1, 0x1D, 0x0, 0x0)
    SetChrChip(0x1, 0x1E, 0x0, 0x0)
    SetChrPos(0x1F, 15300, 0, 12000, 270)
    SetChrPos(0x19, 10550, 0, 13400, 270)
    SetChrPos(0x1A, 11150, 0, 11000, 270)
    SetChrPos(0x1B, 12150, 0, 12000, 270)
    SetChrPos(0x1C, 13250, 0, 14000, 270)
    SetChrPos(0x1D, 12550, 0, 9800, 270)
    SetChrPos(0x1E, 13800, 0, 14850, 270)
    SetChrPos(0x18, -6150, 10, 12000, 90)
    SetChrPos(0x12, -2450, 0, 13400, 90)
    SetChrPos(0x13, -1850, 0, 11500, 90)
    SetChrPos(0x14, -4750, 0, 14500, 90)
    SetChrPos(0x15, -6700, 0, 13350, 90)
    SetChrPos(0x16, -6100, 0, 11550, 90)
    SetChrPos(0x17, -4500, 0, 10450, 90)
    OP_68(3000, 1000, 13250, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_68(3000, 1000, 12250, 2000)
    MoveCamera(45, 20, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(16000, 2000)
    BeginChrThread(0x12, 0, 0, 41)
    Sleep(50)
    BeginChrThread(0x13, 0, 0, 45)
    Sleep(50)
    BeginChrThread(0x14, 0, 0, 46)
    Sleep(50)
    BeginChrThread(0x15, 0, 0, 47)
    Sleep(50)
    BeginChrThread(0x16, 0, 0, 48)
    Sleep(50)
    BeginChrThread(0x17, 0, 0, 49)
    OP_0D()
    Sound(250, 0, 100, 0)
    BeginChrThread(0x19, 0, 0, 16)
    Sleep(200)
    BeginChrThread(0x1E, 0, 0, 31)
    Sleep(200)
    BeginChrThread(0x1A, 0, 0, 19)
    Sleep(200)
    BeginChrThread(0x1C, 0, 0, 25)
    Sleep(200)
    BeginChrThread(0x1D, 0, 0, 28)
    Sleep(200)
    BeginChrThread(0x1B, 0, 0, 22)
    OP_6F(0x79)
    WaitChrThread(0x19, 0)
    WaitChrThread(0x1A, 0)
    WaitChrThread(0x1B, 0)
    WaitChrThread(0x1C, 0)
    WaitChrThread(0x1D, 0)
    WaitChrThread(0x1E, 0)
    StopSound(865, 500, 90)
    StopSound(861, 500, 50)
    StopEffect(0x0, 0x2)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x14, 0x3)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x17, 0x3)

    ChrTalk(
        0x12,
        "#6PTch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#6PThe damn Heiyue's fighters, eh...?\x02",
    )

    CloseMessageWindow()
    OP_A6(0x12, 0x0, 0x32, 0x1F4, 0xBB8)
    Fade(100)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x12, 0x3C)
    SetChrSubChip(0x12, 0x0)
    OP_0D()

    def lambda_22E5():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_22E5)
    Sleep(50)
    OP_A6(0x17, 0x0, 0x32, 0x1F4, 0xBB8)
    Fade(100)
    Sound(531, 0, 60, 0)
    Sound(358, 0, 60, 0)
    SetChrChipByIndex(0x14, 0x39)
    SetChrSubChip(0x14, 0x1)
    SetChrChipByIndex(0x17, 0x39)
    SetChrSubChip(0x17, 0x1)
    OP_0D()
    OP_68(2000, 1000, 12250, 1000)
    SetCameraDistance(17000, 1000)
    SetChrChipByIndex(0x14, 0x3A)

    def lambda_2354():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2354)
    Sleep(50)
    SetChrChipByIndex(0x17, 0x3A)

    def lambda_2370():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2370)
    Sleep(50)
    SetChrChipByIndex(0x15, 0x3A)

    def lambda_238C():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_238C)
    Sleep(50)
    SetChrChipByIndex(0x16, 0x3A)

    def lambda_23A8():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_23A8)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x3F)

    def lambda_23C4():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_23C4)
    Sleep(50)
    SetChrChipByIndex(0x13, 0x3F)

    def lambda_23E0():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_23E0)
    WaitChrThread(0x12, 1)
    Sound(531, 0, 50, 0)
    Sound(538, 0, 40, 0)
    Sound(540, 0, 40, 0)
    SetChrChipByIndex(0x12, 0x3C)
    SetChrSubChip(0x12, 0x0)
    WaitChrThread(0x13, 1)
    SetChrChipByIndex(0x13, 0x3C)
    SetChrSubChip(0x13, 0x0)
    WaitChrThread(0x14, 1)
    SetChrChipByIndex(0x14, 0x37)
    SetChrSubChip(0x14, 0x0)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x37)
    SetChrSubChip(0x17, 0x0)
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x37)
    SetChrSubChip(0x15, 0x0)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x37)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x18, 0x80)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x18,
        "Bold Voice",
        (
            "#3853V#30A#30WHmpf...\x01",
            "Having vigor is a splendid thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Fade(500)
    OP_68(-1350, 1000, 12000, 0)
    MoveCamera(310, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_F0(0x0, 0x1)
    OP_68(6360, 1000, 12200, 3000)
    MoveCamera(310, 20, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(16000, 3000)
    SetChrPos(0x18, 0, 0, 12000, 90)

    def lambda_2521():
        OP_95(0xFE, 5350, 0, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2521)
    SetChrChipByIndex(0x19, 0x2F)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x34)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x2F)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x34)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x2F)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x34)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x19, 10050, 0, 12700, 0)
    SetChrPos(0x1A, 10050, 0, 10200, 0)
    SetChrPos(0x1B, 10500, 0, 11500, 0)
    SetChrPos(0x1C, 9750, 0, 14200, 0)
    SetChrPos(0x1D, 9050, 0, 9300, 0)
    SetChrPos(0x1E, 8300, 0, 14850, 0)
    SetChrPos(0x12, -1450, 0, 13400, 90)
    SetChrPos(0x13, -850, 0, 10500, 90)
    SetChrPos(0x14, -2750, 0, 14500, 90)
    SetChrPos(0x15, -4700, 0, 13250, 90)
    SetChrPos(0x16, -4100, 0, 10550, 90)
    SetChrPos(0x17, -2500, 0, 9450, 90)

    def lambda_2637():

        label("loc_2637")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_2637")

    QueueWorkItem2(0x19, 2, lambda_2637)

    def lambda_2649():

        label("loc_2649")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_2649")

    QueueWorkItem2(0x1A, 2, lambda_2649)

    def lambda_265B():

        label("loc_265B")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_265B")

    QueueWorkItem2(0x1B, 2, lambda_265B)

    def lambda_266D():

        label("loc_266D")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_266D")

    QueueWorkItem2(0x1C, 2, lambda_266D)

    def lambda_267F():

        label("loc_267F")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_267F")

    QueueWorkItem2(0x1D, 2, lambda_267F)

    def lambda_2691():

        label("loc_2691")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_2691")

    QueueWorkItem2(0x1E, 2, lambda_2691)
    WaitChrThread(0x18, 1)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x19,
        "#11P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#12P"Ogre Rosso"....!\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x18,
        (
            "#3854V#30WEh eh, this is a special\x01",
            "service for you. I'll give you\x01",
            "the chance to get my head.\x02\x03",
            "#3855VYou can come at me all at once.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xF0F)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x1B,
        "#12PWha...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#11PAre you mocking us...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Stop, he's──\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(531, 0, 80, 0)
    Sound(372, 0, 60, 0)
    SetChrChipByIndex(0x18, 0x27)
    SetChrSubChip(0x18, 0x0)
    OP_0D()
    OP_68(5350, 1000, 12000, 2000)
    MoveCamera(315, 35, -15, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x19, 0, 0, 17)
    Sleep(100)
    BeginChrThread(0x1D, 0, 0, 29)
    Sleep(100)
    BeginChrThread(0x1B, 0, 0, 23)
    Sleep(100)
    BeginChrThread(0x1A, 0, 0, 20)
    Sleep(100)
    BeginChrThread(0x1C, 0, 0, 26)
    Sleep(100)
    BeginChrThread(0x1E, 0, 0, 32)
    WaitChrThread(0x19, 0)
    WaitChrThread(0x1A, 0)
    WaitChrThread(0x1B, 0)
    WaitChrThread(0x1C, 0)
    WaitChrThread(0x1D, 0)
    WaitChrThread(0x1E, 0)

    ChrTalk(
        0x18,
        "#04503F#5PHmph──is that all you've got?\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x18, 0, 0, 50)
    MoveCamera(310, 35, -5, 2500)
    SetCameraDistance(14000, 2500)
    Sleep(2500)
    OP_68(5350, 1300, 12000, 300)
    MoveCamera(225, 25, -5, 300)
    SetCameraDistance(12000, 300)
    OP_52(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x19, 0, 0, 18)
    Sleep(50)
    BeginChrThread(0x1A, 0, 0, 21)
    Sleep(50)
    BeginChrThread(0x1B, 0, 0, 24)
    Sleep(50)
    BeginChrThread(0x1C, 0, 0, 27)
    Sleep(50)
    BeginChrThread(0x1D, 0, 0, 30)
    Sleep(50)
    BeginChrThread(0x1E, 0, 0, 33)
    Sleep(500)
    Fade(500)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x1A, 0x0)
    EndChrThread(0x1B, 0x0)
    EndChrThread(0x1C, 0x0)
    EndChrThread(0x1D, 0x0)
    EndChrThread(0x1E, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrPos(0x19, 8150, 0, 11900, 0)
    SetChrPos(0x1A, 4750, 0, 9450, 0)
    SetChrPos(0x1B, 6850, 0, 9800, 0)
    SetChrPos(0x1C, 7150, 0, 14000, 0)
    SetChrPos(0x1D, 3100, 0, 10500, 0)
    SetChrPos(0x1E, 5300, 0, 15750, 0)
    SetChrChipByIndex(0x19, 0x2F)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x34)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x2F)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x34)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x31)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x36)
    SetChrSubChip(0x1E, 0x0)
    OP_68(5350, 1000, 12000, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(10000, 0)
    BeginChrThread(0x18, 0, 0, 52)
    MoveCamera(146, 23, -5, 300)
    SetCameraDistance(12000, 300)
    BeginChrThread(0x19, 0, 0, 18)
    Sleep(50)
    BeginChrThread(0x1A, 0, 0, 21)
    Sleep(50)
    BeginChrThread(0x1B, 0, 0, 24)
    Sleep(50)
    BeginChrThread(0x1C, 0, 0, 27)
    Sleep(50)
    BeginChrThread(0x1D, 0, 0, 30)
    Sleep(50)
    BeginChrThread(0x1E, 0, 0, 33)
    Sleep(500)
    Fade(500)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x1A, 0x0)
    EndChrThread(0x1B, 0x0)
    EndChrThread(0x1C, 0x0)
    EndChrThread(0x1D, 0x0)
    EndChrThread(0x1E, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrPos(0x19, 8150, 0, 11900, 0)
    SetChrPos(0x1A, 4750, 0, 9450, 0)
    SetChrPos(0x1B, 6850, 0, 9800, 0)
    SetChrPos(0x1C, 7150, 0, 14000, 0)
    SetChrPos(0x1D, 3100, 0, 10500, 0)
    SetChrPos(0x1E, 5300, 0, 15750, 0)
    SetChrChipByIndex(0x19, 0x2F)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x34)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x2F)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x34)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x31)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x36)
    SetChrSubChip(0x1E, 0x0)
    OP_68(5350, 1000, 12000, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(10000, 0)
    BeginChrThread(0x18, 0, 0, 52)
    OP_68(5350, 1300, 12000, 300)
    MoveCamera(25, 10, -5, 300)
    SetCameraDistance(12000, 300)
    BeginChrThread(0x19, 0, 0, 18)
    Sleep(50)
    BeginChrThread(0x1A, 0, 0, 21)
    Sleep(50)
    BeginChrThread(0x1B, 0, 0, 24)
    Sleep(50)
    BeginChrThread(0x1C, 0, 0, 27)
    Sleep(50)
    BeginChrThread(0x1D, 0, 0, 30)
    Sleep(50)
    BeginChrThread(0x1E, 0, 0, 33)
    WaitChrThread(0x18, 0)
    WaitChrThread(0x19, 0)
    WaitChrThread(0x1A, 0)
    WaitChrThread(0x1B, 0)
    WaitChrThread(0x1C, 0)
    WaitChrThread(0x1D, 0)
    WaitChrThread(0x1E, 0)
    EndChrThread(0x19, 0x2)
    EndChrThread(0x1A, 0x2)
    EndChrThread(0x1B, 0x2)
    EndChrThread(0x1C, 0x2)
    EndChrThread(0x1D, 0x2)
    EndChrThread(0x1E, 0x2)
    OP_52(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x1E,
        "Gwarg...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "...I-Impossible...\x02",
    )

    CloseMessageWindow()
    OP_68(15300, 800, 12000, 2000)
    MoveCamera(45, 25, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(17000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x1F,
        "#11PKh...!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x1F, 0x29)
    SetChrSubChip(0x1F, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sound(881, 0, 80, 0)
    PlayEffect(0x6, 0x0, 0x1F, 0x1, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x5DC)
    SetCameraDistance(15000, 1600)
    OP_A6(0x1F, 0x0, 0xA, 0x640, 0xBB8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    SetCameraDistance(16000, 100)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)
    Sound(259, 0, 70, 0)
    Sound(832, 2, 100, 0)
    OP_A6(0x1F, 0x0, 0x14, 0x1F4, 0xBB8)
    PlayEffect(0x7, 0x0, 0x1F, 0x1, 0, 100, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x18,
        (
            "#04502F#6P#NEh eh, Cao's right-hand man, eh?\x02\x03",
            "I wouldn't mind facing you, but it's\x01",
            "your boss I have business with.\x02\x03",
            "#04504F──Kill him.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0xC8)
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Jaegers")

    AnonymousTalk(
        0xFF,
        "#5SJaー!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x1F,
        "#11PTsk...!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x12, 7000, 0, 12900, 90)
    SetChrPos(0x13, 7000, 0, 11450, 90)
    BeginChrThread(0x12, 0, 0, 38)
    Sleep(400)
    BeginChrThread(0x13, 0, 0, 42)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)
    Fade(500)
    EndChrThread(0x1F, 0x1)
    SetChrPos(0x1F, 20000, 0, 12500, 270)
    SetChrPos(0x18, 10550, 0, 14450, 90)
    SetChrPos(0x12, 17550, 0, 13400, 90)
    SetChrPos(0x13, 18150, 0, 10500, 90)
    SetChrPos(0x14, 11750, 0, 13500, 90)
    SetChrPos(0x15, 9700, 0, 12250, 90)
    SetChrPos(0x16, 8100, 0, 10550, 90)
    SetChrPos(0x17, 11000, 0, 9450, 90)
    BeginChrThread(0x18, 0, 0, 51)
    ClearChrFlags(0x14, 0x20)
    ClearChrFlags(0x15, 0x20)
    ClearChrFlags(0x16, 0x20)
    ClearChrFlags(0x17, 0x20)
    SetChrChipByIndex(0x12, 0x3C)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x3C)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x38)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x38)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x38)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x38)
    SetChrSubChip(0x17, 0x0)

    def lambda_2FEA():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2FEA)

    def lambda_2FFF():
        OP_9B(0x1, 0xFE, 0x0, 0xFA0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2FFF)

    def lambda_3014():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3014)

    def lambda_3029():
        OP_9B(0x1, 0xFE, 0x0, 0x1770, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3029)

    def lambda_303E():

        label("loc_303E")

        TurnDirection(0xFE, 0x1F, 500)
        Yield()
        Jump("loc_303E")

    QueueWorkItem2(0x14, 2, lambda_303E)

    def lambda_3050():

        label("loc_3050")

        TurnDirection(0xFE, 0x1F, 500)
        Yield()
        Jump("loc_3050")

    QueueWorkItem2(0x17, 2, lambda_3050)

    def lambda_3062():

        label("loc_3062")

        TurnDirection(0xFE, 0x1F, 500)
        Yield()
        Jump("loc_3062")

    QueueWorkItem2(0x15, 2, lambda_3062)

    def lambda_3074():

        label("loc_3074")

        TurnDirection(0xFE, 0x1F, 500)
        Yield()
        Jump("loc_3074")

    QueueWorkItem2(0x16, 2, lambda_3074)
    OP_68(17500, 800, 12500, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_68(21500, 800, 12000, 1000)
    MoveCamera(305, 25, 0, 10000)
    SetCameraDistance(20000, 10000)
    BeginChrThread(0x12, 0, 0, 39)
    OP_0D()
    WaitChrThread(0x14, 1)
    Sound(865, 2, 100, 0)
    Sound(861, 2, 70, 0)
    BeginChrThread(0x14, 0, 0, 35)
    BeginChrThread(0x14, 3, 0, 36)
    WaitChrThread(0x17, 1)
    BeginChrThread(0x17, 0, 0, 35)
    BeginChrThread(0x17, 3, 0, 36)
    WaitChrThread(0x15, 1)
    BeginChrThread(0x15, 0, 0, 35)
    BeginChrThread(0x15, 3, 0, 36)
    WaitChrThread(0x16, 1)
    BeginChrThread(0x16, 0, 0, 35)
    BeginChrThread(0x16, 3, 0, 36)
    Sleep(1200)
    BeginChrThread(0x13, 0, 0, 43)
    Sleep(1200)
    BeginChrThread(0x12, 0, 0, 40)
    Sleep(1500)
    BeginChrThread(0x13, 0, 0, 44)
    Sleep(500)
    StopSound(865, 300, 90)
    StopSound(861, 300, 60)
    EndChrThread(0x14, 0x2)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x14, 0x3)
    SetChrChipByIndex(0x14, 0x38)
    SetChrSubChip(0x14, 0x0)

    def lambda_316A():
        OP_95(0xFE, 26000, 0, 13500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_316A)
    Sleep(100)
    EndChrThread(0x17, 0x2)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x17, 0x3)
    SetChrChipByIndex(0x17, 0x38)
    SetChrSubChip(0x17, 0x0)

    def lambda_319B():
        OP_95(0xFE, 20000, 0, 9140, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_319B)
    Sleep(100)
    EndChrThread(0x15, 0x2)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    SetChrChipByIndex(0x15, 0x38)
    SetChrSubChip(0x15, 0x0)

    def lambda_31CC():
        OP_95(0xFE, 23800, 0, 13000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_31CC)
    Sleep(100)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x16, 0x2)
    SetChrChipByIndex(0x16, 0x38)
    SetChrSubChip(0x16, 0x0)

    def lambda_31FD():
        OP_95(0xFE, 21000, 0, 10350, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_31FD)
    FadeToDark(1000, 0, -1)
    Sleep(100)
    StopSound(868, 900, 50)
    StopSound(832, 900, 90)
    OP_0D()
    OP_24(0x361)
    OP_24(0x35D)
    OP_24(0x39E)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("c121D", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_17EA end

    def Function_14_3246(): pass

    label("Function_14_3246")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_96(0xFE, 0x442A, 0x0, 0x38D6, 0x4E20, 0x0)
    OP_96(0xFE, 0x24EA, 0x0, 0x38D6, 0x4E20, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_14_3246 end

    def Function_15_327F(): pass

    label("Function_15_327F")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_96(0xFE, 0x442A, 0x0, 0x2D1E, 0x4E20, 0x0)
    OP_96(0xFE, 0x24EA, 0x0, 0x2D1E, 0x4E20, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_15_327F end

    def Function_16_32B8(): pass

    label("Function_16_32B8")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_96(0xFE, 0xCB2, 0x0, 0x3458, 0x4E20, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    WaitChrThread(0x12, 0)
    Sound(815, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0xA, 0xFF, 0xFE, 0x3, -500, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)

    def lambda_3359():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3359)
    OP_A6(0x12, 0x0, 0x32, 0x1F4, 0xBB8)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 80, 0)
    OP_9D(0xFE, 0x254E, 0x0, 0x3390, 0x3E8, 0x2710)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_32B8 end

    def Function_17_33B4(): pass

    label("Function_17_33B4")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrSubChip(0xFE, 0x2)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(534, 0, 100, 0)
    OP_9D(0xFE, 0x1A2C, 0x0, 0x2FA8, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    PlayEffect(0xA, 0xFF, 0xFE, 0x3, -500, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    EndChrThread(0x18, 0x0)

    def lambda_3466():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3466)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0x14, 0xFFFFFA24, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_17_33B4 end

    def Function_18_3496(): pass

    label("Function_18_3496")


    def lambda_349B():
        OP_9D(0xFE, 0x399E, 0x0, 0x44F2, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_349B)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(815, 0, 100, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_18_3496 end

    def Function_19_3510(): pass

    label("Function_19_3510")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_96(0xFE, 0x1004, 0x0, 0x2BC0, 0x4E20, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrSubChip(0xFE, 0x2)
    PlayEffect(0xA, 0xFF, 0xFE, 0x3, -500, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(862, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)

    def lambda_35A7():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_35A7)
    OP_A6(0x13, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(250, 0, 100, 0)
    OP_9D(0xFE, 0x254E, 0x0, 0x2AF8, 0x3E8, 0x2710)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_3510 end

    def Function_20_3606(): pass

    label("Function_20_3606")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x12C0, 0x0, 0x22C4, 0x3E8, 0x1388)
    TurnDirection(0xFE, 0x18, 1000)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0x1450, 0x0, 0x2C88, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0xA, 0xFF, 0xFE, 0x3, -500, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    EndChrThread(0x18, 0x0)

    def lambda_36C7():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_36C7)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFF830, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_20_3606 end

    def Function_21_36F7(): pass

    label("Function_21_36F7")


    def lambda_36FC():
        OP_9D(0xFE, 0x960, 0xFFFFFD44, 0xEA6, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36FC)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(815, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_21_36F7 end

    def Function_22_3771(): pass

    label("Function_22_3771")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_96(0xFE, 0x1004, 0x0, 0x2EAE, 0x4E20, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0xA, 0xFF, 0xFE, 0x3, -500, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(885, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)

    def lambda_3808():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFF830, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3808)
    OP_A6(0x13, 0x0, 0x32, 0x1F4, 0xBB8)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x2710, 0x0, 0x2EE0, 0x3E8, 0x2710)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_22_3771 end

    def Function_23_385D(): pass

    label("Function_23_385D")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x1932, 0x0, 0x2774, 0x3E8, 0x1388)
    SetChrSubChip(0xFE, 0x2)
    OP_9D(0xFE, 0x1770, 0x0, 0x2B2A, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0xA, 0xFF, 0xFE, 0x3, -500, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    EndChrThread(0x18, 0x0)

    def lambda_3917():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3917)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_23_385D end

    def Function_24_3947(): pass

    label("Function_24_3947")


    def lambda_394C():
        OP_9D(0xFE, 0x40A6, 0x0, 0xFA, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_394C)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Sound(815, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_24_3947 end

    def Function_25_39C1(): pass

    label("Function_25_39C1")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x2)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0xDAC, 0x0, 0x3426, 0x5DC, 0x2710)
    PlayEffect(0xA, 0xFF, 0xFE, 0x3, -500, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(815, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    SetChrFlags(0x12, 0x20)
    SetChrChipByIndex(0x12, 0x40)
    SetChrSubChip(0x12, 0x3)

    def lambda_3A81():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3A81)
    OP_A6(0x12, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Sound(844, 0, 80, 0)
    OP_9D(0xFE, 0x1482, 0x0, 0x34BC, 0x3E8, 0x2710)
    SetChrSubChip(0xFE, 0x1)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x2422, 0x0, 0x3778, 0x3E8, 0x2710)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_39C1 end

    def Function_26_3AF6(): pass

    label("Function_26_3AF6")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_96(0xFE, 0x18CE, 0x0, 0x31CE, 0x2710, 0x0)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(300)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0xA, 0xFF, 0xFE, 0x3, -500, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(815, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    EndChrThread(0x18, 0x0)

    def lambda_3B8F():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3B8F)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xFFEC, 0xFFFFFA24, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_26_3AF6 end

    def Function_27_3BBF(): pass

    label("Function_27_3BBF")


    def lambda_3BC4():
        OP_9D(0xFE, 0x32C8, 0xBB8, 0x4E20, 0x2B, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BC4)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(815, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_3C26():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3C26)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x20)
    OP_96(0xFE, 0x32C8, 0x0, 0x4E20, 0x1388, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_27_3BBF end

    def Function_28_3C61(): pass

    label("Function_28_3C61")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_96(0xFE, 0x2166, 0x0, 0x2648, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)
    Sound(531, 0, 80, 0)
    Sound(540, 0, 50, 0)
    Sleep(500)
    SetChrSubChip(0xFE, 0x1)
    SetChrPos(0x21, 8550, 0, 9800, 0)
    BeginChrThread(0x21, 3, 0, 34)
    ClearChrFlags(0x21, 0x80)
    Sound(926, 2, 100, 0)
    Sound(538, 0, 100, 0)
    PlayEffect(0x1, 0x0, 0x21, 0x1, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_9A(0x21, 0x17, 0x3E8, 0x3A98, 0x0)
    StopEffect(0x0, 0x0)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x17, 0x3)
    Sound(815, 0, 100, 0)
    Sound(501, 0, 100, 0)
    SetChrChipByIndex(0x17, 0x3B)
    BeginChrThread(0x17, 2, 0, 37)
    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3D3E():
        OP_9D(0xFE, 0xFFFFFE0C, 0x0, 0x28D2, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3D3E)
    PlayEffect(0x2, 0xFF, 0x17, 0x1, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9A(0x21, 0xFE, 0x0, 0x3A98, 0x0)
    OP_24(0x39E)
    Sound(308, 0, 100, 0)
    EndChrThread(0x21, 0x3)
    SetChrFlags(0x21, 0x80)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x17, 1)
    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_28_3C61 end

    def Function_29_3DC1(): pass

    label("Function_29_3DC1")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    Sound(844, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x12C0, 0x0, 0x22C4, 0x3E8, 0x2710)
    OP_9D(0xFE, 0xC1C, 0x0, 0x2904, 0x3E8, 0x2710)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xFE, 0x18, 1000)
    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    SetChrSubChip(0xFE, 0x1)
    SetChrPos(0x21, 3100, 0, 10500, 0)
    BeginChrThread(0x21, 3, 0, 34)
    ClearChrFlags(0x21, 0x80)
    PlayEffect(0x1, 0x0, 0x21, 0x1, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_9A(0x21, 0x18, 0x3E8, 0x2710, 0x0)
    StopEffect(0x0, 0x0)
    EndChrThread(0x18, 0x0)
    Sound(566, 0, 50, 0)

    def lambda_3E9C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3E9C)
    OP_9A(0x21, 0xFE, 0x0, 0x2710, 0x0)
    Sound(308, 0, 100, 0)
    EndChrThread(0x21, 0x3)
    SetChrFlags(0x21, 0x80)
    SetChrSubChip(0xFE, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_29_3DC1 end

    def Function_30_3EDA(): pass

    label("Function_30_3EDA")


    def lambda_3EDF():
        OP_9D(0xFE, 0xFFFFEAB6, 0xFFFFFD44, 0x6A4, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3EDF)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Sound(815, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_30_3EDA end

    def Function_31_3F54(): pass

    label("Function_31_3F54")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_96(0xFE, 0x1E78, 0x0, 0x3A02, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    SetChrSubChip(0xFE, 0x1)
    SetChrPos(0x22, 7800, 0, 14850, 0)
    BeginChrThread(0x22, 3, 0, 34)
    ClearChrFlags(0x22, 0x80)
    PlayEffect(0x1, 0x1, 0x22, 0x1, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_9A(0x22, 0x14, 0x3E8, 0x3A98, 0x0)
    StopEffect(0x1, 0x0)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x14, 0x3)
    SetChrChipByIndex(0x14, 0x40)
    Sound(501, 0, 100, 0)
    BeginChrThread(0x14, 2, 0, 37)
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_4013():
        OP_9D(0xFE, 0xFFFFFD12, 0x0, 0x38A4, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4013)
    PlayEffect(0x2, 0xFF, 0x14, 0x1, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9A(0x22, 0xFE, 0x0, 0x3A98, 0x0)
    EndChrThread(0x22, 0x3)
    SetChrFlags(0x22, 0x80)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_31_3F54 end

    def Function_32_408D(): pass

    label("Function_32_408D")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x14B4, 0x0, 0x3D86, 0x3E8, 0x1388)
    TurnDirection(0xFE, 0x18, 1000)
    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    Sound(532, 0, 100, 0)
    Sound(281, 0, 70, 0)
    SetChrSubChip(0xFE, 0x1)
    SetChrPos(0x22, 5300, 0, 15750, 0)
    BeginChrThread(0x22, 3, 0, 34)
    ClearChrFlags(0x22, 0x80)
    PlayEffect(0x1, 0x1, 0x22, 0x1, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_9A(0x22, 0x18, 0x3E8, 0x3A98, 0x0)
    StopEffect(0x1, 0x0)
    EndChrThread(0x18, 0x0)

    def lambda_4154():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_4154)
    OP_9A(0x22, 0xFE, 0x0, 0x3A98, 0x0)
    Sound(308, 0, 100, 0)
    EndChrThread(0x22, 0x3)
    SetChrFlags(0x22, 0x80)
    SetChrSubChip(0xFE, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_32_408D end

    def Function_33_4192(): pass

    label("Function_33_4192")


    def lambda_4197():
        OP_9D(0xFE, 0x1324, 0x7D0, 0x5FB4, 0xBB8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4197)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(815, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    Sound(514, 0, 100, 0)
    Return()

    # Function_33_4192 end

    def Function_34_4215(): pass

    label("Function_34_4215")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_422C")
    OP_A0(0xFE, 5000, 0x10, 0x17)
    Jump("Function_34_4215")

    label("loc_422C")

    Return()

    # Function_34_4215 end

    def Function_35_422D(): pass

    label("Function_35_422D")

    SetChrChipByIndex(0xFE, 0x39)

    label("loc_4231")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4280")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x1)
    Jump("loc_4231")

    label("loc_4280")

    Return()

    # Function_35_422D end

    def Function_36_4281(): pass

    label("Function_36_4281")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42B4")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_42A8")
    OP_4C(0xFE, 0x0)
    Jump("loc_42AC")

    label("loc_42A8")

    OP_4B(0xFE, 0x0)

    label("loc_42AC")

    Sleep(500)
    Jump("Function_36_4281")

    label("loc_42B4")

    Return()

    # Function_36_4281 end

    def Function_37_42B5(): pass

    label("Function_37_42B5")

    SetChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_37_42B5 end

    def Function_38_430D(): pass

    label("Function_38_430D")

    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x3D)
    OP_95(0xFE, 11200, 0, 12300, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x1)
    Sound(538, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x3778, 0x0, 0x2F44, 0x5DC, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1F, 0x20)

    def lambda_4375():
        OP_9B(0x1, 0xFE, 0x1E, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4375)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(288, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    Return()

    # Function_38_430D end

    def Function_39_43AE(): pass

    label("Function_39_43AE")


    def lambda_43B3():

        label("loc_43B3")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_43B3")

    QueueWorkItem2(0x1F, 2, lambda_43B3)

    def lambda_43C5():

        label("loc_43C5")

        TurnDirection(0xFE, 0x1F, 500)
        Yield()
        Jump("loc_43C5")

    QueueWorkItem2(0x12, 2, lambda_43C5)
    OP_52(0x1F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0x1F, 0x558C, 0x0, 0x319C, 0x3E8, 0x2710)
    OP_52(0x1F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x3D)
    OP_99(0xFE, 0x1F, 0x3E8, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x1)
    Sound(538, 0, 100, 0)
    Sleep(50)
    SetChrFlags(0x1F, 0x20)

    def lambda_4437():
        OP_9B(0x1, 0x1F, 0x1E, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4437)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(288, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0x1F, 1)
    OP_A6(0x1F, 0x0, 0xA, 0x1F4, 0xBB8)
    OP_9A(0x1F, 0x12, 0x3E8, 0x2710, 0x0)
    SetChrSubChip(0x1F, 0x1)
    Sound(533, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x40)
    Sound(501, 0, 100, 0)
    BeginChrThread(0xFE, 1, 0, 37)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(844, 0, 100, 0)
    OP_9D(0xFE, 0x445C, 0x0, 0x32C8, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x1F, 0x0)
    Sleep(500)
    OP_A6(0xFE, 0x0, 0xA, 0x1F4, 0xBB8)
    SetChrChipByIndex(0xFE, 0x3C)
    SetChrSubChip(0xFE, 0x0)
    Sound(532, 0, 100, 0)
    Return()

    # Function_39_43AE end

    def Function_40_450A(): pass

    label("Function_40_450A")

    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x3D)
    OP_96(0xFE, 0x51D6, 0xA, 0x2CEC, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x20)
    Sound(538, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x5B0E, 0xA, 0x288C, 0x5DC, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1F, 0x20)

    def lambda_4577():
        OP_9B(0x1, 0xFE, 0x1E, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4577)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(288, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x3C)
    SetChrSubChip(0xFE, 0x0)
    Sound(538, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x55F0, 0xA, 0x24A4, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_40_450A end

    def Function_41_45F4(): pass

    label("Function_41_45F4")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x3C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_41_45F4 end

    def Function_42_460C(): pass

    label("Function_42_460C")

    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x3D)
    OP_95(0xFE, 15400, 0, 11300, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x41)
    SetChrSubChip(0xFE, 0x1)
    Sound(538, 0, 100, 0)
    SetChrFlags(0x1F, 0x20)

    def lambda_4641():
        OP_9B(0x1, 0xFE, 0xFFE2, 0xFFFFF830, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4641)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(288, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    Return()

    # Function_42_460C end

    def Function_43_4681(): pass

    label("Function_43_4681")


    def lambda_4686():

        label("loc_4686")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_4686")

    QueueWorkItem2(0x1F, 2, lambda_4686)

    def lambda_4698():

        label("loc_4698")

        TurnDirection(0xFE, 0x1F, 500)
        Yield()
        Jump("loc_4698")

    QueueWorkItem2(0x13, 2, lambda_4698)
    Sound(540, 0, 100, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x523A, 0x0, 0x2D1E, 0x5DC, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1F, 0x20)

    def lambda_46F5():
        OP_9B(0x1, 0xFE, 0x1E, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_46F5)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(288, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    Sound(538, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x41)
    SetChrSubChip(0xFE, 0x1)
    SetChrFlags(0xFE, 0x20)
    OP_96(0xFE, 0x5730, 0x0, 0x2EE0, 0x2710, 0x0)
    SetChrFlags(0x1F, 0x20)

    def lambda_475E():
        OP_9B(0x1, 0xFE, 0x5A, 0xFFFFF830, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_475E)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(288, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x3C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_43_4681 end

    def Function_44_47A9(): pass

    label("Function_44_47A9")

    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x3D)
    OP_9A(0xFE, 0x1F, 0x3E8, 0x1770, 0x0)
    Sound(540, 0, 100, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x41)
    SetChrSubChip(0xFE, 0x1)
    SetChrFlags(0x1F, 0x20)

    def lambda_47DD():
        OP_9B(0x1, 0xFE, 0x1E, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_47DD)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(288, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    Return()

    # Function_44_47A9 end

    def Function_45_481D(): pass

    label("Function_45_481D")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x3C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_45_481D end

    def Function_46_4835(): pass

    label("Function_46_4835")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    Sound(865, 2, 100, 0)
    Sound(861, 2, 70, 0)
    PlayEffect(0x8, 0x0, 0xFF, 0x0, 4500, 0, 12000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xFE, 0, 0, 35)
    BeginChrThread(0xFE, 3, 0, 36)
    Return()

    # Function_46_4835 end

    def Function_47_4894(): pass

    label("Function_47_4894")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    BeginChrThread(0xFE, 0, 0, 35)
    BeginChrThread(0xFE, 3, 0, 36)
    Return()

    # Function_47_4894 end

    def Function_48_48B0(): pass

    label("Function_48_48B0")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    BeginChrThread(0xFE, 0, 0, 35)
    BeginChrThread(0xFE, 3, 0, 36)
    Return()

    # Function_48_48B0 end

    def Function_49_48CC(): pass

    label("Function_49_48CC")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    BeginChrThread(0xFE, 0, 0, 35)
    BeginChrThread(0xFE, 3, 0, 36)
    Return()

    # Function_49_48CC end

    def Function_50_48E8(): pass

    label("Function_50_48E8")

    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7D(0xCD, 0x8C, 0x82, 0x0, 0x5DC)
    OP_82(0x32, 0x0, 0xBB8, 0x9C4)
    Sleep(1000)
    Sound(3810, 255, 100, 0)
    Sound(197, 0, 100, 0)
    Sound(183, 0, 100, 0)
    Sound(881, 0, 80, 0)
    PlayEffect(0x5, 0x0, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0xA, 0x5DC, 0xBB8)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sound(196, 0, 100, 0)
    Sound(253, 0, 100, 0)
    Sound(538, 0, 100, 0)
    Sound(3809, 255, 100, 0)
    PlayEffect(0x4, 0x1, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x5)
    OP_93(0xFE, 0x5A, 0x5DC)
    OP_93(0xFE, 0x5A, 0x5DC)
    OP_93(0xFE, 0x5A, 0x5DC)
    OP_93(0xFE, 0x5A, 0x5DC)
    CancelBlur(1000)
    SetChrSubChip(0xFE, 0x4)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)
    Sound(833, 0, 100, 0)
    OP_A6(0xFE, 0x0, 0xA, 0x1F4, 0xBB8)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x3E8)
    Sleep(1000)
    Return()

    # Function_50_48E8 end

    def Function_51_4A6E(): pass

    label("Function_51_4A6E")

    SetChrChipByIndex(0x18, 0x26)
    OP_95(0x18, 19200, 0, 14450, 3000, 0x0)
    OP_95(0x18, 19200, 0, 19500, 3000, 0x0)
    Sound(893, 0, 100, 0)
    SetChrChipByIndex(0x18, 0x25)
    OP_A1(0x18, 0x7D0, 0x5, 0x0, 0x0, 0x0, 0x1, 0x2)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(196, 0, 80, 0)
    Sound(880, 0, 80, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    SetMapObjFlags(0x4, 0x4)
    Sleep(500)
    SetChrChipByIndex(0x18, 0x26)

    def lambda_4AEF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_4AEF)

    def lambda_4B00():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4B00)
    Return()

    # Function_51_4A6E end

    def Function_52_4B11(): pass

    label("Function_52_4B11")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_7D(0xCD, 0x8C, 0x82, 0x0, 0x0)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sound(196, 0, 100, 0)
    Sound(253, 0, 100, 0)
    Sound(538, 0, 100, 0)
    PlayEffect(0x4, 0x1, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x5)
    OP_93(0xFE, 0x5A, 0x5DC)
    OP_93(0xFE, 0x5A, 0x5DC)
    OP_93(0xFE, 0x5A, 0x5DC)
    OP_93(0xFE, 0x5A, 0x5DC)
    CancelBlur(1000)
    SetChrSubChip(0xFE, 0x4)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)
    Sound(833, 0, 100, 0)
    OP_A6(0xFE, 0x0, 0xA, 0x1F4, 0xBB8)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x3E8)
    Sleep(1000)
    Return()

    # Function_52_4B11 end

    def Function_53_4BEC(): pass

    label("Function_53_4BEC")


    def lambda_4BF1():
        OP_95(0xFE, -22000, 0, -17800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4BF1)

    def lambda_4C0B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4C0B)
    WaitChrThread(0xFE, 1)

    def lambda_4C20():
        OP_95(0xFE, -22000, 0, -14500, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C20)
    WaitChrThread(0xFE, 1)

    def lambda_4C3E():
        OP_95(0xFE, -19300, 0, -12200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C3E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_53_4BEC end

    def Function_54_4C5F(): pass

    label("Function_54_4C5F")

    Sleep(600)

    def lambda_4C67():
        OP_95(0xFE, -22000, 0, -17800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C67)

    def lambda_4C81():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4C81)
    WaitChrThread(0xFE, 1)

    def lambda_4C96():
        OP_95(0xFE, -22000, 0, -14500, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C96)
    WaitChrThread(0xFE, 1)

    def lambda_4CB4():
        OP_95(0xFE, -19300, 0, -13300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4CB4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_54_4C5F end

    def Function_55_4CD5(): pass

    label("Function_55_4CD5")

    Sleep(1200)

    def lambda_4CDD():
        OP_95(0xFE, -22000, 0, -17800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4CDD)

    def lambda_4CF7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4CF7)
    WaitChrThread(0xFE, 1)

    def lambda_4D0C():
        OP_95(0xFE, -22000, 0, -14500, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D0C)
    WaitChrThread(0xFE, 1)

    def lambda_4D2A():
        OP_95(0xFE, -20500, 0, -12700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D2A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_55_4CD5 end

    def Function_56_4D4B(): pass

    label("Function_56_4D4B")

    Sleep(100)

    def lambda_4D53():
        OP_95(0xFE, -18000, 0, -17800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D53)

    def lambda_4D6D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4D6D)
    WaitChrThread(0xFE, 1)

    def lambda_4D82():
        OP_95(0xFE, -18000, 0, -13300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D82)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_56_4D4B end

    def Function_57_4DA3(): pass

    label("Function_57_4DA3")

    Sleep(700)

    def lambda_4DAB():
        OP_95(0xFE, -18000, 0, -17800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4DAB)

    def lambda_4DC5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4DC5)
    WaitChrThread(0xFE, 1)

    def lambda_4DDA():
        OP_95(0xFE, -17000, 0, -14100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4DDA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_57_4DA3 end

    def Function_58_4DFB(): pass

    label("Function_58_4DFB")

    Sleep(1300)

    def lambda_4E03():
        OP_95(0xFE, -18000, 0, -17800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E03)

    def lambda_4E1D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4E1D)
    WaitChrThread(0xFE, 1)

    def lambda_4E32():
        OP_95(0xFE, -18000, 0, -14300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E32)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_58_4DFB end

    def Function_59_4E53(): pass

    label("Function_59_4E53")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -20500, 100, -17800, 270)
    SetChrPos(0x102, -20500, 100, -17800, 270)
    SetChrPos(0x103, -19500, 100, -17800, 90)
    SetChrPos(0x104, -20500, 100, -17800, 270)
    SetChrPos(0x109, -19500, 100, -17800, 90)
    SetChrPos(0x105, -19500, 100, -17800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SoundLoad(868)
    Sound(868, 2, 100, 0)
    LoadEffect(0x9, "event/ev15021.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 200000, 300000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "kurotuki00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "knuki", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lwindow2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ent2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kurotuki01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kurotuki01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x1, 0x1)
    SetMapObjFrame(0xFF, "bfire00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "bfire01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "fire00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "fire01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "fire02_add", 0x1, 0x1)
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    ClearChrFlags(0x20, 0x80)
    OP_78(0x12, 0x20)
    OP_49()
    SetChrPos(0x20, -20000, 0, -41000, 0)
    OP_D5(0x20, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0xB5, 0xF0, 0x1, 0x20)
    VolumeBGM(0x64, 0x3E8)
    OP_68(-5000, 1000, 0, 0)
    MoveCamera(45, 11, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(25500, 0)
    MoveCamera(30, 11, 0, 7000)
    SetCameraDistance(30500, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(1000)
    OP_68(22150, 2500, 20700, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27000, 0)
    SetCameraDistance(23000, 4000)
    OP_6F(0x79)
    Fade(500)
    OP_68(-20000, 1900, -31000, 0)
    MoveCamera(45, 31, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(24500, 0)
    OP_68(-20000, 1500, -18300, 3500)
    MoveCamera(45, 27, 0, 3500)
    SetCameraDistance(14500, 3500)
    Sound(459, 0, 100, 0)
    Sound(493, 0, 100, 0)

    def lambda_51FD():
        OP_96(0xFE, 0xFFFFB1E0, 0x0, 0xFFFFB9B0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_51FD)
    Sleep(2000)
    Sound(492, 0, 100, 0)
    WaitChrThread(0x20, 1)
    OP_71(0x12, 0x5B, 0x78, 0x1, 0x0)
    OP_79(0x12)
    OP_6F(0x79)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    Sound(462, 0, 100, 0)
    OP_71(0x12, 0x1, 0x1E, 0x1, 0x0)
    OP_79(0x12)
    OP_68(-20000, 1900, -14300, 3000)
    BeginChrThread(0x101, 3, 0, 53)
    BeginChrThread(0x102, 3, 0, 54)
    BeginChrThread(0x103, 3, 0, 57)
    BeginChrThread(0x104, 3, 0, 55)
    BeginChrThread(0x109, 3, 0, 56)
    BeginChrThread(0x105, 3, 0, 58)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        "#5P#00010FKh...the "Heiyue" building is...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x105,
        (
            "#12P#10306FWell, I can't think that Cao\x01",
            "and his men were easily killed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00307FThere's no time...\x01",
            "In any case, let's head to the IBC!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Randy will be temporarily a\x01",
            "mandatory attack member.\x02\x03",
            "Please select a character to remove\x01",
            "from the present attack members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_543D")
    MenuCmd(1, 0, "Switch Wazy to Support")

    label("loc_543D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5469")
    MenuCmd(1, 0, "Switch Noｱl to Support")

    label("loc_5469")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5496")
    MenuCmd(1, 0, "Switch Lloyd to Support")

    label("loc_5496")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54C2")
    MenuCmd(1, 0, "Switch Elie to Support")

    label("loc_54C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54ED")
    MenuCmd(1, 0, "Switch Tio to Support")

    label("loc_54ED")

    MenuCmd(2, 0, -1, -1, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_553B"),
        (1, "loc_565D"),
        (2, "loc_577F"),
        (3, "loc_58A1"),
        (SWITCH_DEFAULT, "loc_59C3"),
    )


    label("loc_553B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5574")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5574")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5574")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55AD")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55AD")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_55AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55E6")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55E6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_55E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_561F")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_561F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_561F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5658")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5658")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5658")

    Jump("loc_59C3")

    label("loc_565D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5696")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5696")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5696")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56CF")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56CF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_56CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5708")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5708")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5708")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5741")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5741")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5741")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_577A")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_577A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_577A")

    Jump("loc_59C3")

    label("loc_577F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57B8")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57B8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_57B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57F1")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57F1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_57F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_582A")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_582A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_582A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5863")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5863")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5863")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_589C")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_589C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_589C")

    Jump("loc_59C3")

    label("loc_58A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58DA")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58DA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_58DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5913")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5913")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5913")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_594C")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_594C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_594C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5985")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5985")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5985")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59BE")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59BE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_59BE")

    Jump("loc_59C3")

    label("loc_59C3")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (4, "loc_59EB"),
        (8, "loc_5A05"),
        (0, "loc_5A1E"),
        (1, "loc_5A37"),
        (2, "loc_5A50"),
        (SWITCH_DEFAULT, "loc_5A69"),
    )


    label("loc_59EB")

    Call(0, 60)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Call(0, 61)
    OP_49()
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_5A69")

    label("loc_5A05")

    Call(0, 60)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x8, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Call(0, 61)
    AddParty(0x8, 0xFF, 0xFF)
    Jump("loc_5A69")

    label("loc_5A1E")

    Call(0, 60)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x0, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Call(0, 61)
    AddParty(0x0, 0xFF, 0xFF)
    Jump("loc_5A69")

    label("loc_5A37")

    Call(0, 60)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x1, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Call(0, 61)
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_5A69")

    label("loc_5A50")

    Call(0, 60)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x2, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Call(0, 61)
    AddParty(0x2, 0xFF, 0xFF)
    Jump("loc_5A69")

    label("loc_5A69")

    SetChrPos(0x0, -20000, 0, -14000, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x20, -18200, 0, -19000, 0)
    ClearMapObjFlags(0x12, 0x1000)
    OP_70(0x12, 0x0)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    OP_C9(0x0, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFF, 0x0)
    OP_66(0x1, 0x1)
    SetScenarioFlags(0x180, 0)
    OP_29(0xAB, 0x4, 0x2)
    OP_29(0xAB, 0x1, 0x0)
    ModifyEventFlags(1, 0, 0x80)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_59_4E53 end

    def Function_60_5AE7(): pass

    label("Function_60_5AE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B0B")
    RemoveParty(0x4, 0xFF)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B96")

    label("loc_5B0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B2F")
    RemoveParty(0x8, 0xFF)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B96")

    label("loc_5B2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B53")
    RemoveParty(0x0, 0xFF)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B96")

    label("loc_5B53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B77")
    RemoveParty(0x1, 0xFF)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B96")

    label("loc_5B77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B96")
    RemoveParty(0x2, 0xFF)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5B96")

    Return()

    # Function_60_5AE7 end

    def Function_61_5B97(): pass

    label("Function_61_5B97")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BAF")
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_5C0A")

    label("loc_5BAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BC7")
    AddParty(0x8, 0xFF, 0xFF)
    Jump("loc_5C0A")

    label("loc_5BC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BDF")
    AddParty(0x0, 0xFF, 0xFF)
    Jump("loc_5C0A")

    label("loc_5BDF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BF7")
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_5C0A")

    label("loc_5BF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C0A")
    AddParty(0x2, 0xFF, 0xFF)

    label("loc_5C0A")

    Return()

    # Function_61_5B97 end

    def Function_62_5C0B(): pass

    label("Function_62_5C0B")

    EventBegin(0x0)
    Fade(500)
    OP_68(4500, 2900, 23200, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 4000, 2000, 23200, 0)
    SetChrPos(0x102, 5000, 2000, 23200, 0)
    SetChrPos(0x103, 3000, 2000, 22200, 0)
    SetChrPos(0x104, 6000, 2000, 22200, 0)
    SetChrPos(0x109, 5500, 2000, 21200, 0)
    SetChrPos(0x105, 3500, 2000, 21200, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sound(878, 0, 100, 0)
    Sleep(200)
    Sound(871, 0, 40, 0)
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(4500, 4900, 32200, 3000)
    MoveCamera(15, 7, 0, 3000)
    Sleep(1000)
    StopSound(868, 2000, 80)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 0)
    NewScene("c130B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_62_5C0B end

    def Function_63_5DAB(): pass

    label("Function_63_5DAB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch27700.itc", 0x1E)
    LoadChrToIndex("chr/ch32800.itc", 0x1F)
    LoadChrToIndex("chr/ch28100.itc", 0x20)
    LoadChrToIndex("chr/ch29400.itc", 0x21)
    SetChrPos(0x101, 4300, 2000, 21100, 0)
    SetChrPos(0x102, 5100, 2000, 20500, 0)
    SetChrPos(0x103, 2700, 2000, 20700, 45)
    SetChrPos(0x104, 6700, 2000, 21000, 315)
    SetChrPos(0x109, 7300, 2000, 22600, 315)
    SetChrPos(0x105, 1500, 2000, 21200, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 2100, 2000, 23000, 180)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 6800, 2000, 23800, 180)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x4)
    OP_90(0xA, 4900, 5120, 38700, 180)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x4)
    OP_90(0xB, 3900, 5120, 38900, 180)
    SetChrChipByIndex(0xC, 0x0)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 1000, 2000, 24300, 180)
    SetChrChipByIndex(0xD, 0x0)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 5100, 2000, 22800, 180)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 5700, 2000, 24300, 180)
    SetChrChipByIndex(0xF, 0x21)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 3800, 2000, 22700, 180)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 3700, 2000, 25100, 180)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 2100, 2000, 24400, 180)
    OP_68(4500, 2900, 23200, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetCameraDistance(18500, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#12P#00007FAre you all right!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#12PWhat the heck happened!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5PW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PSome guys with guns intruded\x01",
            "and told us to get out the building...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe special alloy gate was\x01",
            "blown up in a moment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PThe "Red Constellation"...\x01",
            "I had heard their danger level was S, but...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)

    NpcTalk(
        0xB,
        "Young Man's Voice",
        "#4PY-You guys!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(4500, 3900, 31200, 0)
    MoveCamera(1, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_68(4740, 2900, 22650, 4000)
    MoveCamera(1, 24, 0, 4000)
    SetCameraDistance(16700, 4000)

    def lambda_61A2():
        OP_96(0xFE, 0xE10, 0x7D0, 0x5DC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_61A2)

    def lambda_61BC():
        OP_96(0xFE, 0x17D4, 0x7D0, 0x6338, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_61BC)

    def lambda_61D6():
        OP_96(0xFE, 0x1644, 0x7D0, 0x5EEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_61D6)

    def lambda_61F0():
        OP_96(0xFE, 0xC80, 0x7D0, 0x620C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_61F0)
    BeginChrThread(0xA, 3, 0, 64)
    Sleep(100)
    BeginChrThread(0xB, 3, 0, 65)
    Sleep(3000)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xF, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0x10, 1)
    OP_6F(0x79)
    OP_95(0x103, 3060, 2000, 21430, 2000, 0x0)

    ChrTalk(
        0x103,
        (
            "#6P#00202FJona, Chief...\x01",
            "Are you in one piece?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P*pant pant*, somehow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PT-They pointed guns at us\x01",
            "all of a sudden, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02311F#5PA-Aren't those guys far worse than\x01",
            "the information going around!?\x02\x03",
            "#02310FFurthermore, that redheaded old man...\x01",
            "Is he their boss!?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00007F"Boss"...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#12PThe "Ogre Rosso"!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02307F#5PYeah!\x01",
            "A monster-like old man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00107FWhat about Bell...!?\x01",
            "Hasn't Bell escaped!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 500)
    Sleep(100)

    ChrTalk(
        0x9,
        (
            "#11PIf you are referring to m-milady,\x01",
            "she is at Michelam right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PShe should have escaped danger!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        "#6P#00106FI-I see...thank goodness.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#5P#10303FIt seems that all the civilians\x01",
            "were neglected...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        (
            "#10110F#11PI wonder what're\x01",
            "they planning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PI dunno, but...\x01",
            "I've got a bad feeling.\x02\x03",
            "#00307FIn any case, let's go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00007FYeah...!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xA, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#12P#00107FEast Street is relatively safe!\x02\x03",
            "Please head there\x01",
            "and rely on the Guild!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PU-Understood!\x02",
    )

    CloseMessageWindow()
    OP_93(0xC, 0x5A, 0x1F4)

    ChrTalk(
        0xC,
        (
            "#5PEveryone, we'll guide you\x01",
            "so please follow us!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 2720, 2000, 23920, 0)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 1310, 2000, 24540, 0)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 7330, 2000, 22520, 0)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 5930, 2000, 23920, 0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_37()
    SetChrPos(0x0, 4500, 2000, 21000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x180, 1)
    ModifyEventFlags(0, 0, 0x80)
    OP_10(0x6, 0x1)
    OP_10(0x1, 0x0)
    Sleep(1000)
    EventEnd(0x5)
    Return()

    # Function_63_5DAB end

    def Function_64_67D9(): pass

    label("Function_64_67D9")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_67F0():
        OP_95(0xFE, 4900, 2000, 22700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_67F0)
    WaitChrThread(0xA, 1)
    SetChrFlags(0xA, 0x4)
    OP_64(0xFE)
    OP_93(0xA, 0xB4, 0x1F4)
    Return()

    # Function_64_67D9 end

    def Function_65_6819(): pass

    label("Function_65_6819")

    Sleep(100)
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_6833():
        OP_95(0xFE, 4400, 2000, 23900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6833)
    WaitChrThread(0xB, 1)

    def lambda_6851():
        OP_95(0xFE, 3900, 2000, 22900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6851)
    WaitChrThread(0xB, 1)
    SetChrFlags(0xB, 0x4)
    OP_64(0xFE)
    OP_93(0xB, 0xB4, 0x1F4)
    Return()

    # Function_65_6819 end

    def Function_66_687A(): pass

    label("Function_66_687A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CAF")
    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 21780, 0, 14720, 0)
    SetChrPos(0x102, 23710, 0, 14820, 0)
    SetChrPos(0x103, 22300, 0, 13530, 0)
    SetChrPos(0x104, 19210, 0, 15090, 15)
    SetChrPos(0x105, 20060, 0, 14060, 15)
    SetChrPos(0x109, 20890, 0, 13130, 0)
    OP_68(20970, 1600, 15970, 0)
    MoveCamera(36, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19850, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00001FThe Heiyue Trade Company completely destroyed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FBy the look of it there's no doubt\x01",
            "that it's my uncle and the others' job.\x02\x03",
            "#00303FThis gunpowder smell...\x01",
            "It's the same type of the explosives\x01",
            "the "Red Constellation" use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FThey seem to be the same that were\x01",
            "used at the old abandoned mine before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FI can't see Cao and his\x01",
            "members around.\x02\x03",
            "#10301FI wonder if they were safely able\x01",
            "to escape before getting killed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FJudging by this terrible scene I can't\x01",
            "think they were uninjured, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FBy the way, I wonder if "Yin"...\x01",
            "If Miss Rixia is all right too.\x02\x03",
            "#00202FThe renewal opening performance\x01",
            "is being held right today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F...I'm worried about her, but we\x01",
            "don't have the time to confirm it now.\x02\x03",
            "#00001FLet's make haste to the IBC!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 21780, 0, 14720, 0)
    SetScenarioFlags(0x190, 2)
    EventEnd(0x5)
    Jump("loc_6D34")

    label("loc_6CAF")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00003F...I can't think that Cao and the\x01",
            "others were killed easily.\x02\x03",
            "#00001FAt any rate, let's make haste to the IBC now!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_6D34")

    Return()

    # Function_66_687A end

    def Function_67_6D35(): pass

    label("Function_67_6D35")

    SetMapFlags(0x80)
    ClearScenarioFlags(0x31, 2)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6EA9")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_6DBD")
    MenuCmd(1, 0, "Rest in Orbal Car")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6DBD")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E24")

    ChrTalk(
        0x101,
        (
            "#00001FThere's no time...\x01",
            "Hurry, let's head to the IBC!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EA4")

    label("loc_6E24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E9A")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_6E5D")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_6E75")

    label("loc_6E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_6E70")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_6E75")

    label("loc_6E70")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_6E75")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6EA4")

    label("loc_6E9A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6EA4")

    Jump("loc_6D54")

    label("loc_6EA9")

    SetMapObjFrame(0x12, "light", 0x1, 0x1)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_67_6D35 end

    def Function_68_6EBF(): pass

    label("Function_68_6EBF")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FThere's no time...\x01",
            "Hurry, let's head to the IBC!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -20180, 0, -24790, 0)
    EventEnd(0x4)
    Return()

    # Function_68_6EBF end

    def Function_69_6F13(): pass

    label("Function_69_6F13")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FThere's no time...\x01",
            "Hurry, let's head to the IBC!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -25280, 2000, 23520, 89)
    EventEnd(0x4)
    Return()

    # Function_69_6F13 end

    def Function_70_6F67(): pass

    label("Function_70_6F67")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　"Lupinus River - First Lighthouse"\x01\x01",
            "Authorized Personnel Only.\x01",
            "　　　　　～Crossbell City～\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_70_6F67 end

    SaveToFile()

Try(main)
