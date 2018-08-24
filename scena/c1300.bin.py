from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1300.bin",                # FileName
        "c1300",                    # MapName
        "c1300",                    # Location
        0x001B,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("c1300", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 27, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1300",                  # 0
        "Guard Bills",            # 1
        "Guard",                  # 2
        "Policeman",              # 3
        "Guard",                  # 4
        "Policeman",              # 5
        "Yin",                    # 6
        "Cao",                    # 7
        "Lau",                    # 8
        "Limousine",              # 9
        "Central Square",         # 10
        "West Street",            # 11
        "Governmental District",  # 12
        "Residential Street",     # 13
        "Entertainment District", # 14
        "East Street",            # 15
        "Downtown",               # 16
        "Waterfront Area",        # 17
        "IBC",                    # 18
        "Station Street",         # 19
        "Back Street",            # 20
        "St. Ursula Byroad",      # 21
        "East Crossbell Highway", # 22
        "West Crossbell HIghway", # 23
        "Mainz Mountain Road",    # 24
        "Orchis Tower",           # 25
    ))

    AddCharChip((
        "chr/ch28600.itc",                   # 00
        "chr/ch30000.itc",                   # 01
    ))

    DeclNpc(3910,    0,       5050,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(1500,    0,       500,     270,  389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(1500,    0,       3000,    270,  389,  0x1, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(4294963796, 0,       500,     90,   389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(4294963796, 0,       3000,    90,   389,  0x1, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 7,   0.0,                   7.300000190734863,     0.0,                   14.0625,               [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.6666666865348816,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   -0.0,                  -4.866666793823242,    -0.0,                  1.0])

    DeclActor(7000,    0,       2300,    1200,    7000,    1700,    2300,    0x007C, 0,  8,  0x0000)

    PlaceName(-133.72000122070312, 0.0, -187.47999572753906, 0x0000, 0x0000, "Central Square")
    PlaceName(-223.1999969482422, 0.0, -181.35000610351562, 0x0000, 0x0000, "West Street")
    PlaceName(-96.97000122070312, 0.0, -66.3499984741211, 0x0000, 0x0000, "Governmental District")
    PlaceName(-306.2300109863281, 0.0, -79.95999908447266, 0x0000, 0x0000, "Residential Street")
    PlaceName(-206.8699951171875, 0.0, -90.8499984741211, 0x0000, 0x0000, "Entertainment District")
    PlaceName(-23.139999389648438, 0.0, -218.77999877929688, 0x0000, 0x0000, "East Street")
    PlaceName(25.18000030517578, 0.0, -293.6400146484375, 0x0000, 0x0000, "Downtown")
    PlaceName(14.970000267028809, 0.0, -128.9499969482422, 0x0000, 0x0000, "Waterfront Area")
    PlaceName(-20.420000076293945, 0.0, -1.0199999809265137, 0x0000, 0x0000, "IBC")
    PlaceName(-118.41000366210938, 0.0, -281.3900146484375, 0x0000, 0x0000, "Station Street")
    PlaceName(-182.3699951171875, 0.0, -139.83999633789062, 0x0000, 0x0000, "Back Street")
    PlaceName(-122.48999786376953, 0.0, -323.5799865722656, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(50.36000061035156, 0.0, -199.72999572753906, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-292.6199951171875, 0.0, -183.38999938964844, 0x0000, 0x0000, "West Crossbell HIghway")
    PlaceName(-284.45001220703125, 0.0, -47.290000915527344, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(-107.0, 0.0, 114.0, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(-163.66000366210938, 0.0, -206.52999877929688, 0x0000, 0x0051, "")
    PlaceName(-90.51000213623047, 0.0, -171.14999389648438, 0x0000, 0x0054, "")
    PlaceName(-130.32000732421875, 0.0, -217.4199981689453, 0x0000, 0x0057, "")
    PlaceName(-164.67999267578125, 0.0, -167.05999755859375, 0x0000, 0x0053, "")
    PlaceName(-136.77999877929688, 0.0, -134.39999389648438, 0x0000, 0x0053, "")
    PlaceName(-205.85000610351562, 0.0, -173.8699951171875, 0x0000, 0x0053, "")
    PlaceName(-219.1199951171875, 0.0, -145.2899932861328, 0x0000, 0x0053, "")
    PlaceName(-186.4600067138672, 0.0, -101.7300033569336, 0x0000, 0x0052, "")
    PlaceName(-179.99000549316406, 0.0, -119.43000030517578, 0x0000, 0x0053, "")
    PlaceName(-168.0800018310547, 0.0, -131.0, 0x0000, 0x0053, "")
    PlaceName(-129.3000030517578, 0.0, -34.369998931884766, 0x0000, 0x0051, "")
    PlaceName(23.139999389648438, 0.0, -218.77999877929688, 0x0000, 0x0052, "")
    PlaceName(0.0, 0.0, -341.95001220703125, 0x0000, 0x0053, "")
    PlaceName(-17.690000534057617, 0.0, -316.7699890136719, 0x0000, 0x0053, "")

    ChipFrameInfo(1176, 0)                                       # 0

    ScpFunction((
        "Function_0_498",          # 00, 0
        "Function_1_548",          # 01, 1
        "Function_2_743",          # 02, 2
        "Function_3_8B5",          # 03, 3
        "Function_4_17D0",         # 04, 4
        "Function_5_1EBF",         # 05, 5
        "Function_6_28B0",         # 06, 6
        "Function_7_28D6",         # 07, 7
        "Function_8_2969",         # 08, 8
    ))


    def Function_0_498(): pass

    label("Function_0_498")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_4D0"),
        (1, "loc_4DC"),
        (2, "loc_4E8"),
        (3, "loc_4F4"),
        (4, "loc_500"),
        (5, "loc_50C"),
        (6, "loc_518"),
        (SWITCH_DEFAULT, "loc_524"),
    )


    label("loc_4D0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_4DC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_4E8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_4F4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_500")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_50C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_518")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_524")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_530")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_547")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_530")

    label("loc_547")

    Return()

    # Function_0_498 end

    def Function_1_548(): pass

    label("Function_1_548")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F7")
    SetChrPos(0x0, -230, -1450, -33980, 0)
    SetChrPos(0x1, -230, -1450, -33980, 0)
    SetChrPos(0x2, -230, -1450, -33980, 0)
    SetChrPos(0x3, -230, -1450, -33980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CF")
    SetChrPos(0x4, -230, -1450, -33980, 0)
    SetChrPos(0x5, -230, -1450, -33980, 0)
    Jump("loc_5EE")

    label("loc_5CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5EE")
    SetChrPos(0x4, -230, -1450, -33980, 0)

    label("loc_5EE")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F7")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_613")
    SetChrFlags(0x8, 0x80)
    Jump("loc_6D2")

    label("loc_613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_626")
    SetChrFlags(0x8, 0x80)
    Jump("loc_6D2")

    label("loc_626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_634")
    Jump("loc_6D2")

    label("loc_634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_642")
    Jump("loc_6D2")

    label("loc_642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_650")
    Jump("loc_6D2")

    label("loc_650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_65E")
    Jump("loc_6D2")

    label("loc_65E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_66C")
    Jump("loc_6D2")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_67A")
    Jump("loc_6D2")

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6AD")
    SetChrPos(0x8, 1600, 0, -21430, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_6D2")

    label("loc_6AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6BB")
    Jump("loc_6D2")

    label("loc_6BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6C9")
    Jump("loc_6D2")

    label("loc_6C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6D2")

    label("loc_6D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_6E1")
    ClearScenarioFlags(0x22, 0)
    Event(0, 4)

    label("loc_6E1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_717")
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_742")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_742")

    Return()

    # Function_1_548 end

    def Function_2_743(): pass

    label("Function_2_743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7F8")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x95, 0xA0, 0xB5, 0xD, 0x19F, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_7F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_856")
    OP_78(0x2, 0x10)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -4990, 0, 2500, 180)
    OP_D5(0x10, 0x0, 0x2BF20, 0x0, 0x0)

    label("loc_856")

    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x14)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88A")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_88A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B4")
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)

    label("loc_8B4")

    Return()

    # Function_2_743 end

    def Function_3_8B5(): pass

    label("Function_3_8B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8C6")
    Jump("loc_17CC")

    label("loc_8C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8D4")
    Jump("loc_17CC")

    label("loc_8D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_958")

    ChrTalk(
        0xFE,
        (
            "About the Mainz\x01",
            "occupation... Is it true the\x01",
            "Empire was behind it...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...In any case,\x01",
            "vigilance is the key.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17CC")

    label("loc_958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4B")

    ChrTalk(
        0xFE,
        (
            "Good morning, SSS ladies and gentlemen.\x01",
            "We're all exposed to the rain, but let's\x01",
            "do our jobs in high spirits today too, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lanfei said it should clear\x01",
            "up this afternoon. We'll\x01",
            "need to hold out until then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AFB")

    label("loc_A4B")


    ChrTalk(
        0xFE,
        (
            "We're all exposed to the rain,\x01",
            "but let's do our jobs in high\x01",
            "spirits today too, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lanfei said it should clear\x01",
            "up this afternoon. We'll\x01",
            "need to hold out until then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFB")

    Jump("loc_17CC")

    label("loc_B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA2")

    ChrTalk(
        0xFE,
        (
            "Hmm. It's unusual for\x01",
            "such a small child to\x01",
            "come visit us alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could she have come to\x01",
            "see a family member in\x01",
            "the building?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C57")

    label("loc_BA2")


    ChrTalk(
        0xFE,
        (
            "Whoops, I mustn't do that. I, of all\x01",
            "people, mustn't pry into a customer's\x01",
            "private life, even unintentionally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a member of the\x01",
            "Security Department, I\x01",
            "must be discreet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C57")

    Jump("loc_17CC")

    label("loc_C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CF5")

    ChrTalk(
        0xFE,
        (
            "Good morning. There's\x01",
            "good weather again this\x01",
            "morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As always, this place has\x01",
            "a nice view and the air\x01",
            "is good. It's the best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17CC")

    label("loc_CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DDC")

    ChrTalk(
        0xFE,
        (
            "Should Crossbell be independent\x01",
            "or not...? It's something to\x01",
            "think deeply about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For some reason, I think it's connected to\x01",
            "how IBC should be too, but... As expected,\x01",
            "I can't picture even the small details.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17CC")

    label("loc_DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1089")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F17")

    ChrTalk(
        0xFE,
        (
            "Yesterday, I saw President\x01",
            "Rocksmith up close when\x01",
            "came to visit IBC, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you might expect, the presence\x01",
            "of a leader of that major a power\x01",
            "isn't at all ordinary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It wasn't his outward appearance,\x01",
            "but, how to say it, I keenly felt\x01",
            "something like an aura.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FD3")

    label("loc_F17")


    ChrTalk(
        0xFE,
        (
            "By the way, they say a\x01",
            "suspicious character\x01",
            "infiltrated IBC this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I didn't think there was anything\x01",
            "especially out of the ordinary\x01",
            "though... I'm shocked I didn't notice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD3")

    Jump("loc_1084")

    label("loc_FD8")


    ChrTalk(
        0xFE,
        (
            "Rumor has it that this\x01",
            "Phantom Thief B is quite\x01",
            "the eccentric.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Traveling all across the state and\x01",
            "abandoning what he stole... Just\x01",
            "what the hell is he thinking!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1084")

    Jump("loc_17CC")

    label("loc_1089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1316")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1293")

    ChrTalk(
        0xFE,
        (
            "Ah, guys. I'm terribly\x01",
            "sorry, but IBC is on\x01",
            "holiday today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And that's actually because\x01",
            "President Rocksmith is currently\x01",
            "here for an inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have business\x01",
            "with us, could you come\x01",
            "again tomorrow?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 7)), scpexpr(EXPR_END)), "loc_11E4")

    ChrTalk(
        0x101,
        (
            "#00005FPresident Rocksmith...?\x02\x03",
            "#00003FIndeed, Lanfei talked\x01",
            "about it yesterday as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1208")

    label("loc_11E4")


    ChrTalk(
        0x101,
        "#00005FPresident Rocksmith...?\x02",
    )

    CloseMessageWindow()

    label("loc_1208")


    ChrTalk(
        0x104,
        (
            "#00300FHow to say it, it seems\x01",
            "they're on high alert\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FRight. In any case,\x01",
            "let's leave before we\x01",
            "bother them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1311")

    label("loc_1293")


    ChrTalk(
        0xFE,
        (
            "I'm terribly sorry, but\x01",
            "today IBC is on holiday\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have business\x01",
            "with us, could you come\x01",
            "again tomorrow?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1311")

    Jump("loc_17CC")

    label("loc_1316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_13BF")

    ChrTalk(
        0xFE,
        (
            "The trade conference\x01",
            "finally starts tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The alert level in the city is\x01",
            "already increased and us security\x01",
            "personnel are naturally fired up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17CC")

    label("loc_13BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1674")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1521")

    ChrTalk(
        0xFE,
        (
            "President Crois... No,\x01",
            "Mayor Crois arrived just\x01",
            "moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Mayor does his job at the\x01",
            "new City Hall building, but\x01",
            "sometimes comes here even now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Even so, it's amazing\x01",
            "that he's able to wear\x01",
            "both hats simultaneously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really admire him\x01",
            "because he's doing so well\x01",
            "at managing both of them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15E6")

    label("loc_1521")


    ChrTalk(
        0xFE,
        (
            "Mayor of Crossbell and IBC President...\x01",
            "Thinking over it, his wearing these two\x01",
            "hats at the same time is amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really admire him\x01",
            "because he's doing so well\x01",
            "at managing both of them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15E6")

    Jump("loc_166F")

    label("loc_15EB")


    ChrTalk(
        0xFE,
        (
            "If you're looking for Mayor\x01",
            "Crois, he's already returned\x01",
            "to the new City Hall building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As usual, he's light on\x01",
            "his feet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_166F")

    Jump("loc_17CC")

    label("loc_1674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_17CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1747")

    ChrTalk(
        0xFE,
        (
            "Good morning. Welcome to\x01",
            "the IBC HQ building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you need something,\x01",
            "you can go to the\x01",
            "reception desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our friendly receptionists\x01",
            "will be more than happy to\x01",
            "assist you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17CC")

    label("loc_1747")


    ChrTalk(
        0xFE,
        (
            "If you need something,\x01",
            "you can go to the\x01",
            "reception desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our friendly receptionists\x01",
            "will be more than happy to\x01",
            "assist you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17CC")

    TalkEnd(0xFE)
    Return()

    # Function_3_8B5 end

    def Function_4_17D0(): pass

    label("Function_4_17D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00500.itc", 0x1E)
    LoadChrToIndex("chr/ch06300.itc", 0x1F)
    LoadChrToIndex("chr/ch31400.itc", 0x20)
    LoadChrToIndex("apl/ch50237.itc", 0x21)
    LoadEffect(0x0, "event\\ev202_00.eff")
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 8000, -7000, -74600, 310)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 8000, -7000, -72500, 310)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 9300, -7000, -73300, 310)
    VolumeBGM(0x5A, 0x3E8)
    OP_68(8000, -5900, -73200, 0)
    MoveCamera(57, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_68(8000, -5900, -73200, 5000)
    MoveCamera(81, 15, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(25000, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(8000, -5900, -73200, 0)
    MoveCamera(64, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14730, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xF,
        (
            "#11PIt's really something\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#03209F#11PHaha, magnificent.\x02\x03",
            "#03210FJust seeing this\x01",
            "spectacle makes me glad\x01",
            "we came to Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(100)
    Sound(2628, 255, 100, 0)
    Sleep(800)

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P#00702F...Good for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0xC8, 0x1F4)
    Sleep(200)

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00700F─Whatever, I'm leaving.\x02\x03",
            "It seems we have a\x01",
            "curious rat infestation.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A6D():
        TurnDirection(0xE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1A6D)
    Sleep(50)

    def lambda_1A7D():
        TurnDirection(0xF, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_1A7D)
    Sleep(50)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#03204F#5PYes, I'll leave that to\x01",
            "you.\x02\x03",
            "#03200FAnd, can we count on\x01",
            "your help with\x01",
            "tomorrow's event?\x02\x03",
            "I'd feel better just\x01",
            "knowing you're there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00702FHmph, fine.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2614, 255, 100, 0)
    Sleep(1200)
    Sound(341, 0, 100, 0)
    OP_68(8119, -5900, -73810, 1000)
    PlayEffect(0x0, 0xFF, 0xD, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChip(0x0, 0xD, 0x1E, 0x12C)

    def lambda_1BAC():
        OP_93(0xFE, 0xD2, 0xC8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1BAC)

    def lambda_1BB9():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1BB9)

    def lambda_1BD3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1BD3)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xD, 2)
    SetChrChip(0x1, 0xD, 0x0, 0x0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P*sigh*... Elusive as\x01",
            "ever, isn't he.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PWe could really do\x01",
            "without that mood of\x01",
            "his, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#03204F#5PHehe, I don't think it's\x01",
            "a mood, really.\x02\x03",
            "#03200FThere's a rule regarding\x01",
            "the timing of "his"\x01",
            "cooperation with us.\x02\x03",
            "If we knew what it was,\x01",
            "he'd rarely be able to\x01",
            "refuse us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 500)
    Sleep(100)

    ChrTalk(
        0xF,
        "#11PR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PBut that rule, what\x01",
            "could it be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#03209F#5PHaha, that's still a\x01",
            "secret.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(7440, -5600, -71690, 1500)
    MoveCamera(71, 11, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(14250, 1500)
    OP_93(0xE, 0x136, 0x190)
    OP_6F(0x79)
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x0)
    Sleep(130)
    SetChrSubChip(0xE, 0x1)
    Sleep(130)
    SetChrSubChip(0xE, 0x2)
    Sleep(130)
    Sound(318, 0, 100, 0)
    SetChrSubChip(0xE, 0x3)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#03204F#11P─Everything's gone\x01",
            "according to plan so\x01",
            "far.\x02\x03",
            "#03202FLet's go the extra mile\x01",
            "to make tomorrow's event\x01",
            "a success.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(250)
    OP_82(0x1E, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0xF,
        "#11PSir!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(14750, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 1)
    NewScene("c0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_17D0 end

    def Function_5_1EBF(): pass

    label("Function_5_1EBF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-10630, 5300, -20350, 0)
    MoveCamera(24, -8, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(15210, 0)
    OP_68(-8590, 7900, -25570, 10000)
    MoveCamera(23, -1, 0, 10000)
    OP_6E(750, 10000)
    SetCameraDistance(27170, 10000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_1FF4")
    SetChrPos(0x1A2, -440, -630, -30610, 0)
    SetChrPos(0x102, 500, -630, -30610, 0)
    SetChrPos(0x101, -1010, -1090, -32509, 0)
    SetChrPos(0x104, 950, -1090, -32509, 0)

    def lambda_1F86():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_1F86)

    def lambda_1FA0():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1FA0)
    Sleep(100)

    def lambda_1FBD():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FBD)
    Sleep(50)

    def lambda_1FDA():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1FDA)
    Jump("loc_216F")

    label("loc_1FF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_20B4")
    SetChrPos(0x1A2, -440, -630, -30610, 0)
    SetChrPos(0x102, 500, -630, -30610, 0)
    SetChrPos(0x101, -1010, -1090, -32509, 0)
    SetChrPos(0x109, 950, -1090, -32509, 0)

    def lambda_2046():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_2046)

    def lambda_2060():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2060)
    Sleep(100)

    def lambda_207D():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_207D)
    Sleep(50)

    def lambda_209A():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_209A)
    Jump("loc_216F")

    label("loc_20B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_216F")
    SetChrPos(0x1A2, -440, -630, -30610, 0)
    SetChrPos(0x102, 500, -630, -30610, 0)
    SetChrPos(0x101, -1010, -1090, -32509, 0)
    SetChrPos(0x105, 950, -1090, -32509, 0)

    def lambda_2106():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_2106)

    def lambda_2120():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2120)
    Sleep(100)

    def lambda_213D():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_213D)
    Sleep(50)

    def lambda_215A():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_215A)

    label("loc_216F")

    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-1300, 1910, -24540, 0)
    MoveCamera(48, 25, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(10770, 0)
    OP_0D()

    ChrTalk(
        0x1A2,
        (
            "#5PIBC, huh. A fine\x01",
            "building, as always.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#11P#00105FIt's not your first time\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#6PYes, because Heiyue has\x01",
            "an account at IBC, of\x01",
            "course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PIncidentally, I recently opened\x01",
            "a personal account as well and\x01",
            "started trading stocks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PI hope there'll be\x01",
            "dividends for me next\x01",
            "time...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#00000FNow that you mention it,\x01",
            "you traded stock as a\x01",
            "student, right Elie?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#5P#00100FWell, I just dabbled in\x01",
            "it for future reference.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        (
            "#6PTo think you traded\x01",
            "stock too―\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#6PThat's right, I found a\x01",
            "good stock not too long\x01",
            "ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PThough it's solid, growth\x01",
            "potential is there and it hasn't\x01",
            "yet gotten much attention...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6POh, there are others I\x01",
            "could recommend as\x01",
            "well...\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x1A2, 0, 0, 6)
    Sleep(800)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#11P#00105FU-Uhmm...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_2571")
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#12P#00012F(Was I too careless?)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        "#12P#00306F(...Yeah.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2638")

    label("loc_2571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_25DA")
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#12P#00012F(Was I too careless?)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        "#12P#10106F(...I think so.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2638")

    label("loc_25DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_2638")
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#12P#00012F(Was I too careless?)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        "#12P#10306F(...Yeah.)\x02",
    )

    CloseMessageWindow()

    label("loc_2638")

    EndChrThread(0x1A2, 0x0)
    OP_64(0x1A2)
    Sleep(500)
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#6P―Ah!\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#6PSorry, miss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PI thought we had\x01",
            "something in common and\x01",
            "got carried away...\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x1A2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_2705")

    def lambda_26E5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26E5)
    Sleep(50)

    def lambda_26F5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_26F5)
    Sleep(300)
    Jump("loc_275C")

    label("loc_2705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_2733")

    def lambda_2713():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2713)
    Sleep(50)

    def lambda_2723():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2723)
    Sleep(300)
    Jump("loc_275C")

    label("loc_2733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_275C")

    def lambda_2741():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2741)
    Sleep(50)

    def lambda_2751():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2751)
    Sleep(300)

    label("loc_275C")


    ChrTalk(
        0x102,
        (
            "#11P#00109FHaha, I don't mind.\x01",
            "Although you surprised\x01",
            "me a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6POh, miss... You really\x01",
            "are like a goddess.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#5PAnyway, I can come here\x01",
            "whenever I want, so I don't\x01",
            "need you to show it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#5PHurry up and show me the\x01",
            "next place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FS-Sure...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C5, 2)
    OP_29(0x73, 0x1, 0x4)
    OP_1B(0x1, 0x0, 0x7)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -210, 0, -24590, 180)
    EventEnd(0x5)
    Return()

    # Function_5_1EBF end

    def Function_6_28B0(): pass

    label("Function_6_28B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28D5")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_6_28B0")

    label("loc_28D5")

    Return()

    # Function_6_28B0 end

    def Function_7_28D6(): pass

    label("Function_7_28D6")

    EventBegin(0x1)
    TurnDirection(0x1A2, 0x101, 0)

    ChrTalk(
        0x1A2,
        (
            "I already told you, I\x01",
            "don't need you to show\x01",
            "me IBC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Let's go somewhere else\x01",
            "already!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FS-Sure...\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -160, 400, 5710, 180)
    EventEnd(0x4)
    Return()

    # Function_7_28D6 end

    def Function_8_2969(): pass

    label("Function_8_2969")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I. B. C.\x01",
            "International Bank of Crossbell\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_2969 end

    SaveToFile()

Try(main)
