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
        "Function_4_E98",          # 04, 4
        "Function_5_1033",         # 05, 5
        "Function_6_11DE",         # 06, 6
        "Function_7_12E4",         # 07, 7
        "Function_8_14C8",         # 08, 8
        "Function_9_166E",         # 09, 9
        "Function_10_16EF",        # 0A, 10
        "Function_11_1783",        # 0B, 11
        "Function_12_1799",        # 0C, 12
        "Function_13_17A9",        # 0D, 13
        "Function_14_31E8",        # 0E, 14
        "Function_15_3221",        # 0F, 15
        "Function_16_325A",        # 10, 16
        "Function_17_3356",        # 11, 17
        "Function_18_3438",        # 12, 18
        "Function_19_34B2",        # 13, 19
        "Function_20_35A8",        # 14, 20
        "Function_21_3699",        # 15, 21
        "Function_22_3713",        # 16, 22
        "Function_23_37FF",        # 17, 23
        "Function_24_38E9",        # 18, 24
        "Function_25_3963",        # 19, 25
        "Function_26_3A98",        # 1A, 26
        "Function_27_3B61",        # 1B, 27
        "Function_28_3C03",        # 1C, 28
        "Function_29_3D63",        # 1D, 29
        "Function_30_3E7C",        # 1E, 30
        "Function_31_3EF6",        # 1F, 31
        "Function_32_402F",        # 20, 32
        "Function_33_4134",        # 21, 33
        "Function_34_41B7",        # 22, 34
        "Function_35_41CF",        # 23, 35
        "Function_36_4223",        # 24, 36
        "Function_37_4257",        # 25, 37
        "Function_38_42AF",        # 26, 38
        "Function_39_4350",        # 27, 39
        "Function_40_44AC",        # 28, 40
        "Function_41_4596",        # 29, 41
        "Function_42_45AE",        # 2A, 42
        "Function_43_4623",        # 2B, 43
        "Function_44_474B",        # 2C, 44
        "Function_45_47BF",        # 2D, 45
        "Function_46_47D7",        # 2E, 46
        "Function_47_4836",        # 2F, 47
        "Function_48_4852",        # 30, 48
        "Function_49_486E",        # 31, 49
        "Function_50_488A",        # 32, 50
        "Function_51_4A10",        # 33, 51
        "Function_52_4AB3",        # 34, 52
        "Function_53_4B8E",        # 35, 53
        "Function_54_4C01",        # 36, 54
        "Function_55_4C77",        # 37, 55
        "Function_56_4CED",        # 38, 56
        "Function_57_4D45",        # 39, 57
        "Function_58_4D9D",        # 3A, 58
        "Function_59_4DF5",        # 3B, 59
        "Function_60_5A73",        # 3C, 60
        "Function_61_5B23",        # 3D, 61
        "Function_62_5B97",        # 3E, 62
        "Function_63_5D37",        # 3F, 63
        "Function_64_679B",        # 40, 64
        "Function_65_67DB",        # 41, 65
        "Function_66_683C",        # 42, 66
        "Function_67_6CBF",        # 43, 67
        "Function_68_6E41",        # 44, 68
        "Function_69_6E8B",        # 45, 69
        "Function_70_6ED5",        # 46, 70
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
            "Since you have too many,\x01",
            "you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x11, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E3E")

    Jump("loc_E8C")

    label("loc_E43")

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

    label("loc_E8C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_D47 end

    def Function_4_E98(): pass

    label("Function_4_E98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAC")

    ChrTalk(
        0xB,
        (
            "#02306FInformation about them\x01",
            "occasionally flows in the\x01",
            "orbal net too, but...\x02\x03",
            "#02310FI didn't hear those guys\x01",
            "were this bad, you know!?\x02\x03",
            "#02301FIf you guys are going\x01",
            "there, be really\x01",
            "careful!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYeah, you too. Be\x01",
            "careful and find\x01",
            "shelter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_102F")

    label("loc_FAC")


    ChrTalk(
        0xB,
        (
            "#02306FThose guys are bad\x01",
            "news... Especially that\x01",
            "redheaded old man.\x02\x03",
            "#02301FIf you guys are going\x01",
            "there, be really\x01",
            "careful!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_102F")

    TalkEnd(0xFE)
    Return()

    # Function_4_E98 end

    def Function_5_1033(): pass

    label("Function_5_1033")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1040")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11DA")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                 # 0
            "Ask for healing\x01",      # 1
            "Cancel\x01",               # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_111C")

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
        "Be careful, everyone!\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11D5")

    label("loc_111C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1130")
    Jump("loc_11D5")

    label("loc_1130")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "I brought a mobile recovery\x01",
            "device with me that's in\x01",
            "development at Epstein.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, if you need\x01",
            "treatment, please let me\x01",
            "know!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D5")

    Jump("loc_1040")

    label("loc_11DA")

    TalkEnd(0xFE)
    Return()

    # Function_5_1033 end

    def Function_6_11DE(): pass

    label("Function_6_11DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1284")

    ChrTalk(
        0xFE,
        (
            "That many monsters are\x01",
            "in the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A-Anyway, please leave\x01",
            "the people here to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll take responsibility\x01",
            "for evacuating them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_12E0")

    label("loc_1284")


    ChrTalk(
        0xFE,
        (
            "Please leave the people\x01",
            "here to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll take responsibility\x01",
            "for evacuating them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E0")

    TalkEnd(0xFE)
    Return()

    # Function_6_11DE end

    def Function_7_12E4(): pass

    label("Function_7_12E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141F")

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
            "We keep them at the reception\x01",
            "desk for emergencies. Please\x01",
            "take them.\x02",
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
            "Lanfei...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x190, 0)
    Jump("loc_14C4")

    label("loc_141F")


    ChrTalk(
        0xFE,
        (
            "Why in the world did\x01",
            "they do such a thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was relieved since Lady Mariabell is\x01",
            "out of the office, but I still can't\x01",
            "sort out the thoughts in my head.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C4")

    TalkEnd(0xFE)
    Return()

    # Function_7_12E4 end

    def Function_8_14C8(): pass

    label("Function_8_14C8")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1586")
    ClearChrFlags(0x23, 0x80)
    LoadChrToIndex("chr/ch25200.itc", 0x1E)
    SetChrChipByIndex(0x23, 0x1E)
    SetChrSubChip(0x23, 0x0)
    BeginChrThread(0x23, 0, 0, 0)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -7500, 0, 12700, 0)

    label("loc_1586")

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

    # Function_8_14C8 end

    def Function_9_166E(): pass

    label("Function_9_166E")

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

    # Function_9_166E end

    def Function_10_16EF(): pass

    label("Function_10_16EF")

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

    # Function_10_16EF end

    def Function_11_1783(): pass

    label("Function_11_1783")

    Sound(468, 2, 100, 0)
    Sound(457, 0, 100, 0)
    Sleep(4000)
    Sound(493, 0, 70, 0)
    Return()

    # Function_11_1783 end

    def Function_12_1799(): pass

    label("Function_12_1799")

    Sound(458, 0, 100, 0)
    Sleep(6000)
    Sound(493, 0, 70, 0)
    Return()

    # Function_12_1799 end

    def Function_13_17A9(): pass

    label("Function_13_17A9")

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

    def lambda_1D45():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1D45)
    Sleep(50)

    def lambda_1D5D():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1D5D)
    Sleep(50)

    def lambda_1D75():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1D75)
    Sleep(50)

    def lambda_1D8D():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1D8D)
    Sleep(50)

    def lambda_1DA5():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1DA5)
    Sleep(50)

    def lambda_1DBD():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1DBD)
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
        "#11P─So they've come.\x02",
    )

    CloseMessageWindow()
    OP_68(19300, 1000, 13150, 1000)
    OP_6F(0x79)

    ChrTalk(
        0x1F,
        (
            "#11PWe'll defend this place to\x01",
            "the last. Don't let them\x01",
            "get near the building!\x02",
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
        (
            "#6PThose damn Heiyue\x01",
            "fighters, huh!?\x02",
        )
    )

    CloseMessageWindow()
    OP_A6(0x12, 0x0, 0x32, 0x1F4, 0xBB8)
    Fade(100)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x12, 0x3C)
    SetChrSubChip(0x12, 0x0)
    OP_0D()

    def lambda_22A1():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_22A1)
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

    def lambda_2310():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2310)
    Sleep(50)
    SetChrChipByIndex(0x17, 0x3A)

    def lambda_232C():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_232C)
    Sleep(50)
    SetChrChipByIndex(0x15, 0x3A)

    def lambda_2348():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2348)
    Sleep(50)
    SetChrChipByIndex(0x16, 0x3A)

    def lambda_2364():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2364)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x3F)

    def lambda_2380():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2380)
    Sleep(50)
    SetChrChipByIndex(0x13, 0x3F)

    def lambda_239C():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_239C)
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
            "#3853V#30A#30WHmph... Well at least\x01",
            "you've got spirit.\x02",
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

    def lambda_24DC():
        OP_95(0xFE, 5350, 0, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_24DC)
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

    def lambda_25F2():

        label("loc_25F2")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_25F2")

    QueueWorkItem2(0x19, 2, lambda_25F2)

    def lambda_2604():

        label("loc_2604")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_2604")

    QueueWorkItem2(0x1A, 2, lambda_2604)

    def lambda_2616():

        label("loc_2616")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_2616")

    QueueWorkItem2(0x1B, 2, lambda_2616)

    def lambda_2628():

        label("loc_2628")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_2628")

    QueueWorkItem2(0x1C, 2, lambda_2628)

    def lambda_263A():

        label("loc_263A")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_263A")

    QueueWorkItem2(0x1D, 2, lambda_263A)

    def lambda_264C():

        label("loc_264C")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_264C")

    QueueWorkItem2(0x1E, 2, lambda_264C)
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
        "#12PIt's Ogre Rosso!\x02",
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
            "#3854V#30WHehe. Here's my special freebie for\x01",
            "you. I'll give you a chance at my\x01",
            "head.\x02\x03",
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
        "#11PAre you mocking us!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Stop, he's─\x02",
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
        (
            "#04503F#5PHmph─ Is that all you've\x01",
            "got?\x02",
        )
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
        "Guah!\x02",
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
        "#11PUgh!\x02",
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
            "#04502F#6P#NHehe, Cao's right-hand\x01",
            "man, huh.\x02\x03",
            "I wouldn't mind facing\x01",
            "you, but I've got\x01",
            "business with your boss.\x02\x03",
            "#04504F─Kill him.\x02",
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
        "#11PTch...!\x02",
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

    def lambda_2F8C():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2F8C)

    def lambda_2FA1():
        OP_9B(0x1, 0xFE, 0x0, 0xFA0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2FA1)

    def lambda_2FB6():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2FB6)

    def lambda_2FCB():
        OP_9B(0x1, 0xFE, 0x0, 0x1770, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2FCB)

    def lambda_2FE0():

        label("loc_2FE0")

        TurnDirection(0xFE, 0x1F, 500)
        Yield()
        Jump("loc_2FE0")

    QueueWorkItem2(0x14, 2, lambda_2FE0)

    def lambda_2FF2():

        label("loc_2FF2")

        TurnDirection(0xFE, 0x1F, 500)
        Yield()
        Jump("loc_2FF2")

    QueueWorkItem2(0x17, 2, lambda_2FF2)

    def lambda_3004():

        label("loc_3004")

        TurnDirection(0xFE, 0x1F, 500)
        Yield()
        Jump("loc_3004")

    QueueWorkItem2(0x15, 2, lambda_3004)

    def lambda_3016():

        label("loc_3016")

        TurnDirection(0xFE, 0x1F, 500)
        Yield()
        Jump("loc_3016")

    QueueWorkItem2(0x16, 2, lambda_3016)
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

    def lambda_310C():
        OP_95(0xFE, 26000, 0, 13500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_310C)
    Sleep(100)
    EndChrThread(0x17, 0x2)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x17, 0x3)
    SetChrChipByIndex(0x17, 0x38)
    SetChrSubChip(0x17, 0x0)

    def lambda_313D():
        OP_95(0xFE, 20000, 0, 9140, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_313D)
    Sleep(100)
    EndChrThread(0x15, 0x2)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x15, 0x3)
    SetChrChipByIndex(0x15, 0x38)
    SetChrSubChip(0x15, 0x0)

    def lambda_316E():
        OP_95(0xFE, 23800, 0, 13000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_316E)
    Sleep(100)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x16, 0x2)
    SetChrChipByIndex(0x16, 0x38)
    SetChrSubChip(0x16, 0x0)

    def lambda_319F():
        OP_95(0xFE, 21000, 0, 10350, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_319F)
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

    # Function_13_17A9 end

    def Function_14_31E8(): pass

    label("Function_14_31E8")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_96(0xFE, 0x442A, 0x0, 0x38D6, 0x4E20, 0x0)
    OP_96(0xFE, 0x24EA, 0x0, 0x38D6, 0x4E20, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_14_31E8 end

    def Function_15_3221(): pass

    label("Function_15_3221")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    OP_96(0xFE, 0x442A, 0x0, 0x2D1E, 0x4E20, 0x0)
    OP_96(0xFE, 0x24EA, 0x0, 0x2D1E, 0x4E20, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_15_3221 end

    def Function_16_325A(): pass

    label("Function_16_325A")

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

    def lambda_32FB():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_32FB)
    OP_A6(0x12, 0x0, 0x32, 0x1F4, 0xBB8)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 80, 0)
    OP_9D(0xFE, 0x254E, 0x0, 0x3390, 0x3E8, 0x2710)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_325A end

    def Function_17_3356(): pass

    label("Function_17_3356")

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

    def lambda_3408():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3408)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0x14, 0xFFFFFA24, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_17_3356 end

    def Function_18_3438(): pass

    label("Function_18_3438")


    def lambda_343D():
        OP_9D(0xFE, 0x399E, 0x0, 0x44F2, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_343D)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(815, 0, 100, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_18_3438 end

    def Function_19_34B2(): pass

    label("Function_19_34B2")

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

    def lambda_3549():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3549)
    OP_A6(0x13, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(250, 0, 100, 0)
    OP_9D(0xFE, 0x254E, 0x0, 0x2AF8, 0x3E8, 0x2710)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_34B2 end

    def Function_20_35A8(): pass

    label("Function_20_35A8")

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

    def lambda_3669():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3669)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFF830, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_20_35A8 end

    def Function_21_3699(): pass

    label("Function_21_3699")


    def lambda_369E():
        OP_9D(0xFE, 0x960, 0xFFFFFD44, 0xEA6, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_369E)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(815, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_21_3699 end

    def Function_22_3713(): pass

    label("Function_22_3713")

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

    def lambda_37AA():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFF830, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_37AA)
    OP_A6(0x13, 0x0, 0x32, 0x1F4, 0xBB8)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x2710, 0x0, 0x2EE0, 0x3E8, 0x2710)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_22_3713 end

    def Function_23_37FF(): pass

    label("Function_23_37FF")

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

    def lambda_38B9():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_38B9)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_23_37FF end

    def Function_24_38E9(): pass

    label("Function_24_38E9")


    def lambda_38EE():
        OP_9D(0xFE, 0x40A6, 0x0, 0xFA, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_38EE)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Sound(815, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_24_38E9 end

    def Function_25_3963(): pass

    label("Function_25_3963")

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

    def lambda_3A23():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3A23)
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

    # Function_25_3963 end

    def Function_26_3A98(): pass

    label("Function_26_3A98")

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

    def lambda_3B31():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3B31)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xFFEC, 0xFFFFFA24, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_26_3A98 end

    def Function_27_3B61(): pass

    label("Function_27_3B61")


    def lambda_3B66():
        OP_9D(0xFE, 0x32C8, 0xBB8, 0x4E20, 0x2B, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B66)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(815, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_3BC8():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3BC8)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x20)
    OP_96(0xFE, 0x32C8, 0x0, 0x4E20, 0x1388, 0x0)
    ClearChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_27_3B61 end

    def Function_28_3C03(): pass

    label("Function_28_3C03")

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

    def lambda_3CE0():
        OP_9D(0xFE, 0xFFFFFE0C, 0x0, 0x28D2, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3CE0)
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

    # Function_28_3C03 end

    def Function_29_3D63(): pass

    label("Function_29_3D63")

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

    def lambda_3E3E():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3E3E)
    OP_9A(0x21, 0xFE, 0x0, 0x2710, 0x0)
    Sound(308, 0, 100, 0)
    EndChrThread(0x21, 0x3)
    SetChrFlags(0x21, 0x80)
    SetChrSubChip(0xFE, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_29_3D63 end

    def Function_30_3E7C(): pass

    label("Function_30_3E7C")


    def lambda_3E81():
        OP_9D(0xFE, 0xFFFFEAB6, 0xFFFFFD44, 0x6A4, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E81)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Sound(815, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_30_3E7C end

    def Function_31_3EF6(): pass

    label("Function_31_3EF6")

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

    def lambda_3FB5():
        OP_9D(0xFE, 0xFFFFFD12, 0x0, 0x38A4, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3FB5)
    PlayEffect(0x2, 0xFF, 0x14, 0x1, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9A(0x22, 0xFE, 0x0, 0x3A98, 0x0)
    EndChrThread(0x22, 0x3)
    SetChrFlags(0x22, 0x80)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x14, 1)
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_31_3EF6 end

    def Function_32_402F(): pass

    label("Function_32_402F")

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

    def lambda_40F6():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_40F6)
    OP_9A(0x22, 0xFE, 0x0, 0x3A98, 0x0)
    Sound(308, 0, 100, 0)
    EndChrThread(0x22, 0x3)
    SetChrFlags(0x22, 0x80)
    SetChrSubChip(0xFE, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_32_402F end

    def Function_33_4134(): pass

    label("Function_33_4134")


    def lambda_4139():
        OP_9D(0xFE, 0x1324, 0x7D0, 0x5FB4, 0xBB8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4139)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(815, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    Sound(514, 0, 100, 0)
    Return()

    # Function_33_4134 end

    def Function_34_41B7(): pass

    label("Function_34_41B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41CE")
    OP_A0(0xFE, 5000, 0x10, 0x17)
    Jump("Function_34_41B7")

    label("loc_41CE")

    Return()

    # Function_34_41B7 end

    def Function_35_41CF(): pass

    label("Function_35_41CF")

    SetChrChipByIndex(0xFE, 0x39)

    label("loc_41D3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4222")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x1)
    Jump("loc_41D3")

    label("loc_4222")

    Return()

    # Function_35_41CF end

    def Function_36_4223(): pass

    label("Function_36_4223")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4256")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_424A")
    OP_4C(0xFE, 0x0)
    Jump("loc_424E")

    label("loc_424A")

    OP_4B(0xFE, 0x0)

    label("loc_424E")

    Sleep(500)
    Jump("Function_36_4223")

    label("loc_4256")

    Return()

    # Function_36_4223 end

    def Function_37_4257(): pass

    label("Function_37_4257")

    SetChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_37_4257 end

    def Function_38_42AF(): pass

    label("Function_38_42AF")

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

    def lambda_4317():
        OP_9B(0x1, 0xFE, 0x1E, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4317)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(288, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    Return()

    # Function_38_42AF end

    def Function_39_4350(): pass

    label("Function_39_4350")


    def lambda_4355():

        label("loc_4355")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_4355")

    QueueWorkItem2(0x1F, 2, lambda_4355)

    def lambda_4367():

        label("loc_4367")

        TurnDirection(0xFE, 0x1F, 500)
        Yield()
        Jump("loc_4367")

    QueueWorkItem2(0x12, 2, lambda_4367)
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

    def lambda_43D9():
        OP_9B(0x1, 0x1F, 0x1E, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_43D9)
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

    # Function_39_4350 end

    def Function_40_44AC(): pass

    label("Function_40_44AC")

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

    def lambda_4519():
        OP_9B(0x1, 0xFE, 0x1E, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4519)
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

    # Function_40_44AC end

    def Function_41_4596(): pass

    label("Function_41_4596")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x3C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_41_4596 end

    def Function_42_45AE(): pass

    label("Function_42_45AE")

    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x3D)
    OP_95(0xFE, 15400, 0, 11300, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x41)
    SetChrSubChip(0xFE, 0x1)
    Sound(538, 0, 100, 0)
    SetChrFlags(0x1F, 0x20)

    def lambda_45E3():
        OP_9B(0x1, 0xFE, 0xFFE2, 0xFFFFF830, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_45E3)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(288, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    Return()

    # Function_42_45AE end

    def Function_43_4623(): pass

    label("Function_43_4623")


    def lambda_4628():

        label("loc_4628")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_4628")

    QueueWorkItem2(0x1F, 2, lambda_4628)

    def lambda_463A():

        label("loc_463A")

        TurnDirection(0xFE, 0x1F, 500)
        Yield()
        Jump("loc_463A")

    QueueWorkItem2(0x13, 2, lambda_463A)
    Sound(540, 0, 100, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x523A, 0x0, 0x2D1E, 0x5DC, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1F, 0x20)

    def lambda_4697():
        OP_9B(0x1, 0xFE, 0x1E, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4697)
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

    def lambda_4700():
        OP_9B(0x1, 0xFE, 0x5A, 0xFFFFF830, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4700)
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

    # Function_43_4623 end

    def Function_44_474B(): pass

    label("Function_44_474B")

    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x3D)
    OP_9A(0xFE, 0x1F, 0x3E8, 0x1770, 0x0)
    Sound(540, 0, 100, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x41)
    SetChrSubChip(0xFE, 0x1)
    SetChrFlags(0x1F, 0x20)

    def lambda_477F():
        OP_9B(0x1, 0xFE, 0x1E, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_477F)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(288, 0, 50, 0)
    SetChrSubChip(0xFE, 0x4)
    Return()

    # Function_44_474B end

    def Function_45_47BF(): pass

    label("Function_45_47BF")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x3C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_45_47BF end

    def Function_46_47D7(): pass

    label("Function_46_47D7")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    Sound(865, 2, 100, 0)
    Sound(861, 2, 70, 0)
    PlayEffect(0x8, 0x0, 0xFF, 0x0, 4500, 0, 12000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xFE, 0, 0, 35)
    BeginChrThread(0xFE, 3, 0, 36)
    Return()

    # Function_46_47D7 end

    def Function_47_4836(): pass

    label("Function_47_4836")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    BeginChrThread(0xFE, 0, 0, 35)
    BeginChrThread(0xFE, 3, 0, 36)
    Return()

    # Function_47_4836 end

    def Function_48_4852(): pass

    label("Function_48_4852")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    BeginChrThread(0xFE, 0, 0, 35)
    BeginChrThread(0xFE, 3, 0, 36)
    Return()

    # Function_48_4852 end

    def Function_49_486E(): pass

    label("Function_49_486E")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    BeginChrThread(0xFE, 0, 0, 35)
    BeginChrThread(0xFE, 3, 0, 36)
    Return()

    # Function_49_486E end

    def Function_50_488A(): pass

    label("Function_50_488A")

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

    # Function_50_488A end

    def Function_51_4A10(): pass

    label("Function_51_4A10")

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

    def lambda_4A91():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_4A91)

    def lambda_4AA2():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4AA2)
    Return()

    # Function_51_4A10 end

    def Function_52_4AB3(): pass

    label("Function_52_4AB3")

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

    # Function_52_4AB3 end

    def Function_53_4B8E(): pass

    label("Function_53_4B8E")


    def lambda_4B93():
        OP_95(0xFE, -22000, 0, -17800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B93)

    def lambda_4BAD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4BAD)
    WaitChrThread(0xFE, 1)

    def lambda_4BC2():
        OP_95(0xFE, -22000, 0, -14500, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4BC2)
    WaitChrThread(0xFE, 1)

    def lambda_4BE0():
        OP_95(0xFE, -19300, 0, -12200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4BE0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_53_4B8E end

    def Function_54_4C01(): pass

    label("Function_54_4C01")

    Sleep(600)

    def lambda_4C09():
        OP_95(0xFE, -22000, 0, -17800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C09)

    def lambda_4C23():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4C23)
    WaitChrThread(0xFE, 1)

    def lambda_4C38():
        OP_95(0xFE, -22000, 0, -14500, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C38)
    WaitChrThread(0xFE, 1)

    def lambda_4C56():
        OP_95(0xFE, -19300, 0, -13300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C56)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_54_4C01 end

    def Function_55_4C77(): pass

    label("Function_55_4C77")

    Sleep(1200)

    def lambda_4C7F():
        OP_95(0xFE, -22000, 0, -17800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C7F)

    def lambda_4C99():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4C99)
    WaitChrThread(0xFE, 1)

    def lambda_4CAE():
        OP_95(0xFE, -22000, 0, -14500, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4CAE)
    WaitChrThread(0xFE, 1)

    def lambda_4CCC():
        OP_95(0xFE, -20500, 0, -12700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4CCC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_55_4C77 end

    def Function_56_4CED(): pass

    label("Function_56_4CED")

    Sleep(100)

    def lambda_4CF5():
        OP_95(0xFE, -18000, 0, -17800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4CF5)

    def lambda_4D0F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4D0F)
    WaitChrThread(0xFE, 1)

    def lambda_4D24():
        OP_95(0xFE, -18000, 0, -13300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D24)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_56_4CED end

    def Function_57_4D45(): pass

    label("Function_57_4D45")

    Sleep(700)

    def lambda_4D4D():
        OP_95(0xFE, -18000, 0, -17800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D4D)

    def lambda_4D67():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4D67)
    WaitChrThread(0xFE, 1)

    def lambda_4D7C():
        OP_95(0xFE, -17000, 0, -14100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4D7C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_57_4D45 end

    def Function_58_4D9D(): pass

    label("Function_58_4D9D")

    Sleep(1300)

    def lambda_4DA5():
        OP_95(0xFE, -18000, 0, -17800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4DA5)

    def lambda_4DBF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4DBF)
    WaitChrThread(0xFE, 1)

    def lambda_4DD4():
        OP_95(0xFE, -18000, 0, -14300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4DD4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_58_4D9D end

    def Function_59_4DF5(): pass

    label("Function_59_4DF5")

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

    def lambda_519F():
        OP_96(0xFE, 0xFFFFB1E0, 0x0, 0xFFFFB9B0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_519F)
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
        (
            "#5P#00010FUgh... The Heiyue\x01",
            "office.\x02",
        )
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
            "#12P#10306FWell, I can't think Cao\x01",
            "and the others were\x01",
            "killed so easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00307FThere's no time... Let's\x01",
            "head for IBC!\x02",
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
            "Randy will temporarily be\x01",
            "a mandatory attack\x01",
            "member.\x02\x03",
            "Please select a character\x01",
            "to remove from the\x01",
            "present attack members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53C9")
    MenuCmd(1, 0, "Switch Wazy to Support")

    label("loc_53C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53F5")
    MenuCmd(1, 0, "Switch Noｱl to Support")

    label("loc_53F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5422")
    MenuCmd(1, 0, "Switch Lloyd to Support")

    label("loc_5422")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_544E")
    MenuCmd(1, 0, "Switch Elie to Support")

    label("loc_544E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5479")
    MenuCmd(1, 0, "Switch Tio to Support")

    label("loc_5479")

    MenuCmd(2, 0, -1, -1, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_54C7"),
        (1, "loc_55E9"),
        (2, "loc_570B"),
        (3, "loc_582D"),
        (SWITCH_DEFAULT, "loc_594F"),
    )


    label("loc_54C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5500")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5500")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5500")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5539")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5539")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5539")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5572")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5572")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5572")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55AB")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55AB")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_55AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55E4")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55E4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_55E4")

    Jump("loc_594F")

    label("loc_55E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5622")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5622")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5622")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_565B")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_565B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_565B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5694")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5694")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5694")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56CD")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56CD")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_56CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5706")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5706")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5706")

    Jump("loc_594F")

    label("loc_570B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5744")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5744")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5744")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_577D")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_577D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_577D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57B6")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57B6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_57B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57EF")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57EF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_57EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5828")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5828")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5828")

    Jump("loc_594F")

    label("loc_582D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5866")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5866")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5866")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_589F")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_589F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_589F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58D8")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58D8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_58D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5911")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5911")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5911")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_594A")
    RunExpression(0x1, (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_594A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_594A")

    Jump("loc_594F")

    label("loc_594F")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (4, "loc_5977"),
        (8, "loc_5991"),
        (0, "loc_59AA"),
        (1, "loc_59C3"),
        (2, "loc_59DC"),
        (SWITCH_DEFAULT, "loc_59F5"),
    )


    label("loc_5977")

    Call(0, 60)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Call(0, 61)
    OP_49()
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_59F5")

    label("loc_5991")

    Call(0, 60)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x8, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Call(0, 61)
    AddParty(0x8, 0xFF, 0xFF)
    Jump("loc_59F5")

    label("loc_59AA")

    Call(0, 60)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x0, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Call(0, 61)
    AddParty(0x0, 0xFF, 0xFF)
    Jump("loc_59F5")

    label("loc_59C3")

    Call(0, 60)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x1, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Call(0, 61)
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_59F5")

    label("loc_59DC")

    Call(0, 60)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x2, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Call(0, 61)
    AddParty(0x2, 0xFF, 0xFF)
    Jump("loc_59F5")

    label("loc_59F5")

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

    # Function_59_4DF5 end

    def Function_60_5A73(): pass

    label("Function_60_5A73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A97")
    RemoveParty(0x4, 0xFF)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B22")

    label("loc_5A97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5ABB")
    RemoveParty(0x8, 0xFF)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B22")

    label("loc_5ABB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5ADF")
    RemoveParty(0x0, 0xFF)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B22")

    label("loc_5ADF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B03")
    RemoveParty(0x1, 0xFF)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B22")

    label("loc_5B03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x4, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B22")
    RemoveParty(0x2, 0xFF)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5B22")

    Return()

    # Function_60_5A73 end

    def Function_61_5B23(): pass

    label("Function_61_5B23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B3B")
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_5B96")

    label("loc_5B3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B53")
    AddParty(0x8, 0xFF, 0xFF)
    Jump("loc_5B96")

    label("loc_5B53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B6B")
    AddParty(0x0, 0xFF, 0xFF)
    Jump("loc_5B96")

    label("loc_5B6B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B83")
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_5B96")

    label("loc_5B83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B96")
    AddParty(0x2, 0xFF, 0xFF)

    label("loc_5B96")

    Return()

    # Function_61_5B23 end

    def Function_62_5B97(): pass

    label("Function_62_5B97")

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

    # Function_62_5B97 end

    def Function_63_5D37(): pass

    label("Function_63_5D37")

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
            "#5PSome guys with guns\x01",
            "barged in and told us to\x01",
            "get out of the building!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe special alloy gate\x01",
            "was blown up in an\x01",
            "instant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PRed Constellation... I\x01",
            "heard they had an S\x01",
            "danger level, but...\x02",
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

    def lambda_6129():
        OP_96(0xFE, 0xE10, 0x7D0, 0x5DC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6129)

    def lambda_6143():
        OP_96(0xFE, 0x17D4, 0x7D0, 0x6338, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6143)

    def lambda_615D():
        OP_96(0xFE, 0x1644, 0x7D0, 0x5EEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_615D)

    def lambda_6177():
        OP_96(0xFE, 0xC80, 0x7D0, 0x620C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6177)
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
            "#6P#00202FJona, Chief... So you're\x01",
            "safe.\x02",
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
            "#11PT-They pointed guns at\x01",
            "us all of a sudden,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02311F#5PA-Aren't those guys way more\x01",
            "dangerous than the information\x01",
            "going around says!?\x02\x03",
            "#02310FThe situation is serious... I\x01",
            "wonder if my food cart will be\x01",
            "all right...\x02",
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
        "#6P#00007F"Boss", you said...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310F#12PThe Ogre Rosso!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02307F#5PYeah! A monstrous old\x01",
            "man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00107FWhat about Bell!? Has\x01",
            "Bell escaped!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 500)
    Sleep(100)

    ChrTalk(
        0x9,
        (
            "#11PIf you are referring to\x01",
            "m-milady, she is at\x01",
            "Michelam right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PShe should be out of\x01",
            "danger!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#6P#00106FI-I see... Thank\x01",
            "goodness.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#5P#10303FIt seems a large number of\x01",
            "civilians have been forced\x01",
            "out of the building...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        (
            "#10110F#11PI wonder what they're\x01",
            "planning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PI dunno, but... I've got\x01",
            "this feeling it's\x01",
            "nothin' good.\x02\x03",
            "#00307FAnyway, let's go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00007FRight!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xA, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#12P#00107FEast Street is\x01",
            "relatively safe!\x02\x03",
            "Please head there and\x01",
            "rely on the Guild!\x02",
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
            "#5PEveryone, we'll guide\x01",
            "you so please follow us!\x02",
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

    # Function_63_5D37 end

    def Function_64_679B(): pass

    label("Function_64_679B")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_67B2():
        OP_95(0xFE, 4900, 2000, 22700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_67B2)
    WaitChrThread(0xA, 1)
    SetChrFlags(0xA, 0x4)
    OP_64(0xFE)
    OP_93(0xA, 0xB4, 0x1F4)
    Return()

    # Function_64_679B end

    def Function_65_67DB(): pass

    label("Function_65_67DB")

    Sleep(100)
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_67F5():
        OP_95(0xFE, 4400, 2000, 23900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_67F5)
    WaitChrThread(0xB, 1)

    def lambda_6813():
        OP_95(0xFE, 3900, 2000, 22900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6813)
    WaitChrThread(0xB, 1)
    SetChrFlags(0xB, 0x4)
    OP_64(0xFE)
    OP_93(0xB, 0xB4, 0x1F4)
    Return()

    # Function_65_67DB end

    def Function_66_683C(): pass

    label("Function_66_683C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C50")
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
        (
            "#12P#00001FThe Heiyue Trading Company\x01",
            "building was completely\x01",
            "destroyed, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FFrom the look of it, it's\x01",
            "definitely the work of uncle and\x01",
            "the others.\x02\x03",
            "#00303FThis gunpowder smell... It's the\x01",
            "same as those of the explosives\x01",
            "Red Constellation uses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FIt seems they're the\x01",
            "same as the ones used at\x01",
            "the Old Mine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FThere's no sign of Cao\x01",
            "or his men, is there.\x02\x03",
            "#10301FI wonder if they got\x01",
            "away before they were\x01",
            "done in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FJudging by this terrible\x01",
            "scene I can't think they\x01",
            "got away unscathed, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FBy the way, I wonder if\x01",
            "Yin... If Rixia is all\x01",
            "right.\x02\x03",
            "#00202FThis was opening night\x01",
            "for their renewal\x01",
            "performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FI'm worried about her, but\x01",
            "we don't have the time to\x01",
            "check on that now.\x02\x03",
            "#00001FLet's hurry to IBC!\x02",
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
    Jump("loc_6CBE")

    label("loc_6C50")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00003F...I can't think Cao and\x01",
            "the others were killed\x01",
            "easily.\x02\x03",
            "#00001FAnyway, let's hurry to\x01",
            "IBC!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_6CBE")

    Return()

    # Function_66_683C end

    def Function_67_6CBF(): pass

    label("Function_67_6CBF")

    SetMapFlags(0x80)
    ClearScenarioFlags(0x31, 2)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6CDE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E2B")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_6D47")
    MenuCmd(1, 0, "Rest in Orbal Car")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D47")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DA6")

    ChrTalk(
        0x101,
        (
            "#00001FThere's no time... Let's\x01",
            "hurry to IBC!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E26")

    label("loc_6DA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E1C")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_6DDF")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_6DF7")

    label("loc_6DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_6DF2")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_6DF7")

    label("loc_6DF2")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_6DF7")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E26")

    label("loc_6E1C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6E26")

    Jump("loc_6CDE")

    label("loc_6E2B")

    SetMapObjFrame(0x12, "light", 0x1, 0x1)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_67_6CBF end

    def Function_68_6E41(): pass

    label("Function_68_6E41")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FThere's no time... Let's\x01",
            "hurry to IBC!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -20180, 0, -24790, 0)
    EventEnd(0x4)
    Return()

    # Function_68_6E41 end

    def Function_69_6E8B(): pass

    label("Function_69_6E8B")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FThere's no time... Let's\x01",
            "hurry to IBC!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -25280, 2000, 23520, 89)
    EventEnd(0x4)
    Return()

    # Function_69_6E8B end

    def Function_70_6ED5(): pass

    label("Function_70_6ED5")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　Lupinus River - No. 1 Lighthouse\x01",
            " \x01",
            "Authorized personnel only.\x01",
            "　　　　　～Crossbell City～\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_70_6ED5 end

    SaveToFile()

Try(main)
