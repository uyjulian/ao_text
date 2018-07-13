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
        "Function_4_183C",         # 04, 4
        "Function_5_1F37",         # 05, 5
        "Function_6_29D3",         # 06, 6
        "Function_7_29F9",         # 07, 7
        "Function_8_2A96",         # 08, 8
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
    Jump("loc_1838")

    label("loc_8C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8D4")
    Jump("loc_1838")

    label("loc_8D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_967")

    ChrTalk(
        0xFE,
        (
            "About the Mainz occupation incident...\x01",
            "Is it true there was the Empire behind it...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...In any case, vigilance is the key.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1838")

    label("loc_967")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A69")

    ChrTalk(
        0xFE,
        (
            "Good morning, SSS ladies and gentlemen.\x01",
            "We're all exposed to the rain, but let's\x01",
            "do our job in high spirits today too, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "According to what Miss Lanfei said,\x01",
            "it should clear in the afternoon.\x01",
            "Until then, patience it is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B28")

    label("loc_A69")


    ChrTalk(
        0xFE,
        (
            "We're all exposed to the rain, but let's\x01",
            "do our job in high spirits today too, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "According to what Miss Lanfei said,\x01",
            "it should clear in the afternoon.\x01",
            "Until then, patience it is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B28")

    Jump("loc_1838")

    label("loc_B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE3")

    ChrTalk(
        0xFE,
        (
            "Hm, that such a small child\x01",
            "comes all alone to visit us\x01",
            "is something unusual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could she have come to see a\x01",
            "family member who is in the building?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C80")

    label("loc_BE3")


    ChrTalk(
        0xFE,
        (
            "Oh, no, I can't do that. I, of all\x01",
            "people, have not to unintentionally\x01",
            "inquire about a customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "As someone from the security, I must be discreet.\x02",
    )

    CloseMessageWindow()

    label("loc_C80")

    Jump("loc_1838")

    label("loc_C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D21")

    ChrTalk(
        0xFE,
        (
            "Good morning.\x01",
            "This morning too there's a pleasant weather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As usual, this place has\x01",
            "a nice view and the air\x01",
            "is good. It's the best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1838")

    label("loc_D21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E1F")

    ChrTalk(
        0xFE,
        (
            "Should Crossbell be independent\x01",
            "as a State or not...?\x01",
            "It's something to deeply think about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Inadvertently, I think it's something that\x01",
            "regards how the IBC should be too, but...\x01",
            "As expected, I can't picture even the small details.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1838")

    label("loc_E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1104")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1048")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F86")

    ChrTalk(
        0xFE,
        (
            "Yesterday, I was able to see from\x01",
            "up close President Rocksmith \x01",
            "who came to visit the IBC, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you may expect, when it comes to a top\x01",
            "who keeps together such a major power,\x01",
            "his presence isn't really ordinary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It wasn't his outward appearance,\x01",
            "but, how to say, I keenly felt\x01",
            "something like an aura.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1043")

    label("loc_F86")


    ChrTalk(
        0xFE,
        (
            "By the way, they say that this morning a\x01",
            "suspicious character intruded into the IBC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think that nothing was\x01",
            "especially out of the ordinary, but...\x01",
            "It's a shock I didn't notice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1043")

    Jump("loc_10FF")

    label("loc_1048")


    ChrTalk(
        0xFE,
        (
            "Like I heard, this Phantom Thief B\x01",
            "is quite the eccentric.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Going around and neglecting what he stole\x01",
            "in every land of the autonomous state...\x01",
            "What does that guy want to do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FF")

    Jump("loc_1838")

    label("loc_1104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_13AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132B")

    ChrTalk(
        0xFE,
        (
            "Ah, guys.\x01",
            "I'm terribly sorry,\x01",
            "but today the IBC is on holiday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And that's actually because today\x01",
            "that President Rocksmith is\x01",
            "currently visiting it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have some business, could\x01",
            "you come back again tomorrow?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 7)), scpexpr(EXPR_END)), "loc_126B")

    ChrTalk(
        0x101,
        (
            "#00005FPresident Rocksmith...?\x02\x03",
            "#00003FIndeed, Miss Lanfei too was\x01",
            "talking about it yesterday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_128F")

    label("loc_126B")


    ChrTalk(
        0x101,
        "#00005FPresident Rocksmith...?\x02",
    )

    CloseMessageWindow()

    label("loc_128F")


    ChrTalk(
        0x104,
        (
            "#00300FHow to say, they really seem\x01",
            "to be on high alert here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FRight, in any case, let's\x01",
            "withdraw quietly before\x01",
            "we hindrance them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13A9")

    label("loc_132B")


    ChrTalk(
        0xFE,
        (
            "I'm terribly sorry,\x01",
            "but today the IBC is on holiday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have some business, could\x01",
            "you come back again tomorrow?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13A9")

    Jump("loc_1838")

    label("loc_13AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1453")

    ChrTalk(
        0xFE,
        "The Trade Conference is finally starting tomorrow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The alert level in the city has already increased\x01",
            "and we security are naturally fired up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1838")

    label("loc_1453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1702")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_168E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15BB")

    ChrTalk(
        0xFE,
        (
            "President Crois...\x01",
            "No, Mayor Crois has\x01",
            "arrived moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Mayor does his job at the new\x01",
            "City Hall building, but sometimes\x01",
            "he comes here like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Even so, his wearing these two\x01",
            "hats at the same time is amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Furthermore, because he's \x01",
            "actually doing this splendidly,\x01",
            "he's really admirable.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1689")

    label("loc_15BB")


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
            "Furthermore, because he's \x01",
            "actually doing this splendidly,\x01",
            "he's really admirable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1689")

    Jump("loc_16FD")

    label("loc_168E")


    ChrTalk(
        0xFE,
        (
            "If you're looking for Mayor Crois,\x01",
            "he quickly went back to the new town hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hard working as usual.\x02",
    )

    CloseMessageWindow()

    label("loc_16FD")

    Jump("loc_1838")

    label("loc_1702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1838")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C9")

    ChrTalk(
        0xFE,
        (
            "Good morning. Welcome to\x01",
            "the IBC headquarters building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If you need something, you can go to the reception.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our prized receptionists\x01",
            "will kindly assist you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1838")

    label("loc_17C9")


    ChrTalk(
        0xFE,
        "If you need something, you can go to the reception.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our prized receptionists\x01",
            "will kindly assist you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1838")

    TalkEnd(0xFE)
    Return()

    # Function_3_8B5 end

    def Function_4_183C(): pass

    label("Function_4_183C")

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
        "#11P...It's really something else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#03209F#11PHu hu, magnificent.\x02\x03",
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
            "#5P#00700F──Whatever, I'm leaving.\x02\x03",
            "It seems we have a\x01",
            "strange rat infestation.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1ADF():
        TurnDirection(0xE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1ADF)
    Sleep(50)

    def lambda_1AEF():
        TurnDirection(0xF, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_1AEF)
    Sleep(50)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#03204F#5PYes, I'll leave that to you.\x02\x03",
            "#03200FAnd, can we count on your\x01",
            "help with tomorrow's event?\x02\x03",
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

    def lambda_1C1E():
        OP_93(0xFE, 0xD2, 0xC8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1C1E)

    def lambda_1C2B():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1C2B)

    def lambda_1C45():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1C45)
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
            "#5P*sigh*... Elusive\x01",
            "as ever, isn't he.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PWe could really do without\x01",
            "that temper, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#03204F#5PHu hu, I don't think\x01",
            "it's a temper, really.\x02\x03",
            "#03200FThere's a rule regarding the timing\x01",
            "of "his" cooperation with us...\x02\x03",
            "If we knew what it was, he'd only\x01",
            "rarely be able to refuse us.\x02",
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
        "#11PBut that rule, what could it be...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#03209F#5PHu hu, that's still secret.\x02",
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
            "#03204F#11P──Everything's gone according to plan so far.\x02\x03",
            "#03202FLet's go the extra mile to make\x01",
            "tomorrow's event a success.\x02",
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

    # Function_4_183C end

    def Function_5_1F37(): pass

    label("Function_5_1F37")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_206C")
    SetChrPos(0x1A2, -440, -630, -30610, 0)
    SetChrPos(0x102, 500, -630, -30610, 0)
    SetChrPos(0x101, -1010, -1090, -32509, 0)
    SetChrPos(0x104, 950, -1090, -32509, 0)

    def lambda_1FFE():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_1FFE)

    def lambda_2018():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2018)
    Sleep(100)

    def lambda_2035():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2035)
    Sleep(50)

    def lambda_2052():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2052)
    Jump("loc_21E7")

    label("loc_206C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_212C")
    SetChrPos(0x1A2, -440, -630, -30610, 0)
    SetChrPos(0x102, 500, -630, -30610, 0)
    SetChrPos(0x101, -1010, -1090, -32509, 0)
    SetChrPos(0x109, 950, -1090, -32509, 0)

    def lambda_20BE():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_20BE)

    def lambda_20D8():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20D8)
    Sleep(100)

    def lambda_20F5():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20F5)
    Sleep(50)

    def lambda_2112():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2112)
    Jump("loc_21E7")

    label("loc_212C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_21E7")
    SetChrPos(0x1A2, -440, -630, -30610, 0)
    SetChrPos(0x102, 500, -630, -30610, 0)
    SetChrPos(0x101, -1010, -1090, -32509, 0)
    SetChrPos(0x105, 950, -1090, -32509, 0)

    def lambda_217E():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_217E)

    def lambda_2198():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2198)
    Sleep(100)

    def lambda_21B5():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21B5)
    Sleep(50)

    def lambda_21D2():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_21D2)

    label("loc_21E7")

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
            "#5PThe IBC, eh...?\x01",
            "Hm, a splendid building, as always.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#11P#00105FShing, this is not your first time here?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#6PIt isn't. Naturally there's\x01",
            "a Heiyue's account at IBC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PIncidentally, recently I opened\x01",
            "an account too and started to\x01",
            "deal in stocks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#6PI hope I'll get some dividends next time...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#00000FNow that I think about it, you too were dealing \x01",
            "in stocks when you were a student, Elie?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#5P#00100FYes, well, at a small level,\x01",
            "for future reference.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        (
            "#6PTo think that Miss Elie\x01",
            "was dealing in stocks too...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#6POh, right, some time ago,\x01",
            "I found a nice stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PAlthough solid and with prospects,\x01",
            "I haven't observed it yet that much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6POh, aside from that, there're\x01",
            "other stocks I'd recommend you...\x02",
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
        "#11P#00105FE-Eehm...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_2631")
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#12P#00012F(M-Maybe I said more than I meant to...?)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        "#12P#00306F(...Right?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2724")

    label("loc_2631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_26AE")
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#12P#00012F(M-Maybe I said more than I meant to...?)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        "#12P#10106F(...I think so.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2724")

    label("loc_26AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_2724")
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#12P#00012F(M-Maybe I said more than I meant to...?)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        "#12P#10306F(...You have.)\x02",
    )

    CloseMessageWindow()

    label("loc_2724")

    EndChrThread(0x1A2, 0x0)
    OP_64(0x1A2)
    Sleep(500)
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#6P...Hah!\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#6PI'm sorry, miss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PThinking I found a subject in common,\x01",
            "I unintentionally became happy single-sidedly...\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x1A2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_2811")

    def lambda_27F1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27F1)
    Sleep(50)

    def lambda_2801():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2801)
    Sleep(300)
    Jump("loc_2868")

    label("loc_2811")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_283F")

    def lambda_281F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_281F)
    Sleep(50)

    def lambda_282F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_282F)
    Sleep(300)
    Jump("loc_2868")

    label("loc_283F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_2868")

    def lambda_284D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_284D)
    Sleep(50)

    def lambda_285D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_285D)
    Sleep(300)

    label("loc_2868")


    ChrTalk(
        0x102,
        (
            "#11P#00109F*giggle*, I don't mind.\x01",
            "Although you surprised me a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6POh, miss...\x01",
            "You really are like a goddess.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#5PIn any event, if I feel like it, I can come here\x01",
            "whenever I want, so I don't need you to show me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#5PLet's head for the next place, fast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FY-Yeah...\x02",
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

    # Function_5_1F37 end

    def Function_6_29D3(): pass

    label("Function_6_29D3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29F8")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_6_29D3")

    label("loc_29F8")

    Return()

    # Function_6_29D3 end

    def Function_7_29F9(): pass

    label("Function_7_29F9")

    EventBegin(0x1)
    TurnDirection(0x1A2, 0x101, 0)

    ChrTalk(
        0x1A2,
        (
            "Like I told you, I don't need you\x01",
            "to show me the IBC at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Quick, let's go to the next place!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FY-Yeah...\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -160, 400, 5710, 180)
    EventEnd(0x4)
    Return()

    # Function_7_29F9 end

    def Function_8_2A96(): pass

    label("Function_8_2A96")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I. B. C.\x01",
            "International Bank of Crossbell\x01\x01",
            "Please inquire at the first\x01",
            "floor lobby counter about \x01",
            "all the companies inside.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_2A96 end

    SaveToFile()

Try(main)
