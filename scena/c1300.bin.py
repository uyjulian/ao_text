from ScenarioHelper import *

def main():
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
        "Security guards",           # 1
        "Security guard",                 # 2
        "Policeman",                   # 3
        "Security guard",                 # 4
        "Policeman",                   # 5
        "Silver",                     # 6
        "Tsao",                 # 7
        "Row",                   # 8
        "Limousine",               # 9
        "Central square",               # 10
        "Nishi dori",                 # 11
        "Administrative district",                 # 12
        "Residential area",                 # 13
        "Entertainment district",                 # 14
        "East Street",                 # 15
        "old Town",                 # 16
        "Harbor district",                 # 17
        "IBC",                 # 18
        "Beside the station",               # 19
        "Back street",                 # 20
        "Ursula interchange",           # 21
        "East Crossbell Highway",       # 22
        "West Crossbell Highway",       # 23
        "Mainz Mountain Road",           # 24
        "Orchis Tower",         # 25
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

    PlaceName(-133.72000122070312, 0.0, -187.47999572753906, 0x0000, 0x0000, "Central square")
    PlaceName(-223.1999969482422, 0.0, -181.35000610351562, 0x0000, 0x0000, "Nishi dori")
    PlaceName(-96.97000122070312, 0.0, -66.3499984741211, 0x0000, 0x0000, "Administrative district")
    PlaceName(-306.2300109863281, 0.0, -79.95999908447266, 0x0000, 0x0000, "Residential area")
    PlaceName(-206.8699951171875, 0.0, -90.8499984741211, 0x0000, 0x0000, "Entertainment district")
    PlaceName(-23.139999389648438, 0.0, -218.77999877929688, 0x0000, 0x0000, "East Street")
    PlaceName(25.18000030517578, 0.0, -293.6400146484375, 0x0000, 0x0000, "old Town")
    PlaceName(14.970000267028809, 0.0, -128.9499969482422, 0x0000, 0x0000, "Harbor district")
    PlaceName(-20.420000076293945, 0.0, -1.0199999809265137, 0x0000, 0x0000, "IBC")
    PlaceName(-118.41000366210938, 0.0, -281.3900146484375, 0x0000, 0x0000, "Beside the station")
    PlaceName(-182.3699951171875, 0.0, -139.83999633789062, 0x0000, 0x0000, "Back street")
    PlaceName(-122.48999786376953, 0.0, -323.5799865722656, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(50.36000061035156, 0.0, -199.72999572753906, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-292.6199951171875, 0.0, -183.38999938964844, 0x0000, 0x0000, "West Crossbell Highway")
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
        "Function_4_15A0",         # 04, 4
        "Function_5_1CAE",         # 05, 5
        "Function_6_269F",         # 06, 6
        "Function_7_26C5",         # 07, 7
        "Function_8_2758",         # 08, 8
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
    Jump("loc_159C")

    label("loc_8C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8D4")
    Jump("loc_159C")

    label("loc_8D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_945")

    ChrTalk(
        0xFE,
        (
            "What is the occupying case in Mainz … …\x01",
            "After all there is an empire behind … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Anyway, it is vigilant.\x02",
    )

    CloseMessageWindow()
    Jump("loc_159C")

    label("loc_945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0E")

    ChrTalk(
        0xFE,
        (
            "Good morning, you guys at the Special Affairs Support Division.\x01",
            "They are exposed to each other's rain,\x01",
            "Let 's keep on tire today as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If anything is Ranfi's story\x01",
            "It seems that rain will also rise in the afternoon,\x01",
            "That's why I have patience until then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A9F")

    label("loc_A0E")


    ChrTalk(
        0xFE,
        (
            "They are exposed to each other's rain,\x01",
            "Let 's keep on tire today as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If anything is Ranfi's story\x01",
            "It seems that rain will also rise in the afternoon,\x01",
            "That's why I have patience until then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9F")

    Jump("loc_159C")

    label("loc_AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3A")

    ChrTalk(
        0xFE,
        (
            "Hmm, such a small child\x01",
            "Join us alone\x01",
            "It is unusual to visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even for families in Bill\x01",
            "I wonder if I came to see you?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BB4")

    label("loc_B3A")


    ChrTalk(
        0xFE,
        (
            "Oops, no.\x01",
            "The things I did with you, the customers\x01",
            "Imitation like snooping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I must refrain from the security department, the mouth.\x02",
    )

    CloseMessageWindow()

    label("loc_BB4")

    Jump("loc_159C")

    label("loc_BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C3A")

    ChrTalk(
        0xFE,
        (
            "Good morning.\x01",
            "It is a nice weather this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This place is as usual\x01",
            "The view is nice,\x01",
            "Air is also fine and it's great.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_159C")

    label("loc_C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CF6")

    ChrTalk(
        0xFE,
        (
            "Crossbell as a nation\x01",
            "Whether or not to be independent …\x01",
            "It is a story that makes me think deeply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "何気にIBCのあり方にも\x01",
            "I think that it is a story involved … …\x01",
            "I can not imagine a fine place like running around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_159C")

    label("loc_CF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F4A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E20")

    ChrTalk(
        0xFE,
        (
            "昨日、IBCに訪れていた\x01",
            "President Rock Smith\x01",
            "I could see it at close range, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Again, that big country\x01",
            "When it becomes the top which brings it together,\x01",
            "The existence is not common in fashionable stones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How about the appearance,\x01",
            "What you say, something like an aura\x01",
            "I felt astonishment.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EB3")

    label("loc_E20")


    ChrTalk(
        0xFE,
        (
            "Sounds suspicious person this morning\x01",
            "このIBCに侵入したらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially what has changed\x01",
            "I think that it was not … …\x01",
            "Shock was not noticed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB3")

    Jump("loc_F45")

    label("loc_EB8")


    ChrTalk(
        0xFE,
        (
            "As you heard about Kaitou B,\x01",
            "It is quite a strange thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Stolen things to various parts of autonomous province\x01",
            "I let go neglecting … ….\x01",
            "What on earth do you want to do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F45")

    Jump("loc_159C")

    label("loc_F4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_11B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1143")

    ChrTalk(
        0xFE,
        (
            "Oh, you guys.\x01",
            "I am sorry,\x01",
            "本日IBCは休行日なんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because, in fact, right now\x01",
            "That rock smith president\x01",
            "I am in the midst of visiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have business,\x01",
            "I wonder if it will come again tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 7)), scpexpr(EXPR_END)), "loc_108B")

    ChrTalk(
        0x101,
        (
            "#00005FWhether the president's tour … …\x02\x03",
            "#00003FCertainly, Ranfi also yesterday\x01",
            "That's what I was saying.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10AA")

    label("loc_108B")


    ChrTalk(
        0x101,
        "#00005FWhether the president's tour … …\x02",
    )

    CloseMessageWindow()

    label("loc_10AA")


    ChrTalk(
        0x104,
        (
            "#00300FWhat kind, is it hanging on running water?\x01",
            "It seems not to be alarmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWell, I tentatively\x01",
            "Without get in the way\x01",
            "Shall we go away adultly?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11AD")

    label("loc_1143")


    ChrTalk(
        0xFE,
        (
            "I am sorry,\x01",
            "本日IBCは休行日なんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have business,\x01",
            "I wonder if it will come again tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11AD")

    Jump("loc_159C")

    label("loc_11B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1235")

    ChrTalk(
        0xFE,
        "From tomorrow, it will be a trade meeting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The alert level of the city is already rising,\x01",
            "We've got a sense of enthusiasm for the security department.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_159C")

    label("loc_1235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1492")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_142C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1381")

    ChrTalk(
        0xFE,
        (
            "President Croise,\x01",
            "No, Mayor Clois\x01",
            "I was able to see you a while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The mayor basically to the new city hall building\x01",
            "I am stuffing, but sometimes like this\x01",
            "You come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Even so,\x01",
            "These two stadts are terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And, in fact,\x01",
            "Because I am wearing it\x01",
            "I really admire you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1427")

    label("loc_1381")


    ChrTalk(
        0xFE,
        (
            "クロスベル市長とIBC総裁……\x01",
            "Thinking carefully,\x01",
            "These two stadts are terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And, in fact,\x01",
            "Because I am wearing it\x01",
            "I really admire you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1427")

    Jump("loc_148D")

    label("loc_142C")


    ChrTalk(
        0xFE,
        (
            "As soon as Croix Mayor\x01",
            "I went back to the new city hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "As usual the footwork is light.\x02",
    )

    CloseMessageWindow()

    label("loc_148D")

    Jump("loc_159C")

    label("loc_1492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_159C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_153B")

    ChrTalk(
        0xFE,
        (
            "Hello.\x01",
            "IBC本社ビルへようこそ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You should go to the reception desk for something else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We are proud of our receptionist\x01",
            "I am supposed to guide you carefully.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_159C")

    label("loc_153B")


    ChrTalk(
        0xFE,
        "You should go to the reception desk for something else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We are proud of our receptionist\x01",
            "I am supposed to guide you carefully.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_159C")

    TalkEnd(0xFE)
    Return()

    # Function_3_8B5 end

    def Function_4_15A0(): pass

    label("Function_4_15A0")

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
        "#11P…… It's a big deal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#03209F#11PHuh, that's great.\x02\x03",
            "#03210FEven just seeing this sight\x01",
            "It is worth the effort to come to Crossbell\x01",
            "It was that it was there.\x02",
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
            "#11P#00702F…… That is a victory.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0xC8, 0x1F4)
    Sleep(200)

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00700F─ ─ oh well, I will go.\x02\x03",
            "Somehow strange rats\x01",
            "You seem to be entering.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_184C():
        TurnDirection(0xE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_184C)
    Sleep(50)

    def lambda_185C():
        TurnDirection(0xF, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_185C)
    Sleep(50)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#03204F#5PYes, I will leave it there.\x02\x03",
            "#03200FAnd tomorrow's event\x01",
            "Do you have a cooperation by all means?\x02\x03",
            "Just because you will come\x01",
            "Considerable foil#2RHaku#Because it is attached.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00702FHun, that's okay.\x02",
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

    def lambda_19AB():
        OP_93(0xFE, 0xD2, 0xC8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_19AB)

    def lambda_19B8():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_19B8)

    def lambda_19D2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_19D2)
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
            "#5PFuu …\x01",
            "As usual it is a devilish mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PWithout that quirk\x01",
            "I am sorry for this ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#03204F#5PHuh, apparently with caprice\x01",
            "It does not seem to mean that.\x02\x03",
            "#03200F\"He\" will cooperate here\x01",
            "There are rules in timing ……\x02\x03",
            "If you have to figure it out\x01",
            "It is rarely refused.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 500)
    Sleep(100)

    ChrTalk(
        0xF,
        "#11PIs that so, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#11PBut with that rule ……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#03209F#5PHuh, it is still a secret.\x02",
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
            "#03204F#11P── So far this is the setup.\x02\x03",
            "#03202FFor the success of the event tomorrow,\x01",
            "Let's keep on trying hard.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(250)
    OP_82(0x1E, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0xF,
        "#11PIs!\x02",
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

    # Function_4_15A0 end

    def Function_5_1CAE(): pass

    label("Function_5_1CAE")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_1DE3")
    SetChrPos(0x1A2, -440, -630, -30610, 0)
    SetChrPos(0x102, 500, -630, -30610, 0)
    SetChrPos(0x101, -1010, -1090, -32509, 0)
    SetChrPos(0x104, 950, -1090, -32509, 0)

    def lambda_1D75():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_1D75)

    def lambda_1D8F():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D8F)
    Sleep(100)

    def lambda_1DAC():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DAC)
    Sleep(50)

    def lambda_1DC9():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1DC9)
    Jump("loc_1F5E")

    label("loc_1DE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_1EA3")
    SetChrPos(0x1A2, -440, -630, -30610, 0)
    SetChrPos(0x102, 500, -630, -30610, 0)
    SetChrPos(0x101, -1010, -1090, -32509, 0)
    SetChrPos(0x109, 950, -1090, -32509, 0)

    def lambda_1E35():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_1E35)

    def lambda_1E4F():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1E4F)
    Sleep(100)

    def lambda_1E6C():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E6C)
    Sleep(50)

    def lambda_1E89():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1E89)
    Jump("loc_1F5E")

    label("loc_1EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1F5E")
    SetChrPos(0x1A2, -440, -630, -30610, 0)
    SetChrPos(0x102, 500, -630, -30610, 0)
    SetChrPos(0x101, -1010, -1090, -32509, 0)
    SetChrPos(0x105, 950, -1090, -32509, 0)

    def lambda_1EF5():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_1EF5)

    def lambda_1F0F():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F0F)
    Sleep(100)

    def lambda_1F2C():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F2C)
    Sleep(50)

    def lambda_1F49():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1F49)

    label("loc_1F5E")

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
            "#5PIBCか……\x01",
            "Hmm, it's a fine building as ever.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#11P#00105FShin is not the first time?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#6Pええ、IBCには当然\x01",
            "Because there is a black moon account as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PBy the way, recently,\x01",
            "I also have my own account open\x01",
            "I started turnip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#6PAs soon as we can pay dividends ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#00000FBy the way, Erie also\x01",
            "You were doing stocks when you were a student?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#5P#00100FYeah, for postgraduate studies\x01",
            "It is a bit grabbed, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        (
            "#6PNo way, Ellie's sister\x01",
            "I was doing a turnip -\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#6PThat's right, before this\x01",
            "I found a good brand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PSteady but there is a future\x01",
            "It has not gotten much attention yet -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6POh, besides that\x01",
            "There are other brands that I recommend -\x02",
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
        "#11P#00105FLet me see……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_2336")
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#12P#00012F(Okay, I guess you said something extra …?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        "#12P#00306F(… … it is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2421")

    label("loc_2336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_23B2")
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#12P#00012F(Okay, I guess you said something extra …?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        "#12P#10106F(……I think.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2421")

    label("loc_23B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_2421")
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#12P#00012F(Okay, I guess you said something extra …?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        "#12P#10306F(…, that's it.\x02",
    )

    CloseMessageWindow()

    label("loc_2421")

    EndChrThread(0x1A2, 0x0)
    OP_64(0x1A2)
    Sleep(500)
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#6P- Ha!\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#6PI'm sorry, your older sister.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PI thought that a common way was found\x01",
            "Become happy and unilaterally …\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x1A2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_2500")

    def lambda_24E0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24E0)
    Sleep(50)

    def lambda_24F0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_24F0)
    Sleep(300)
    Jump("loc_2557")

    label("loc_2500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_252E")

    def lambda_250E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_250E)
    Sleep(50)

    def lambda_251E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_251E)
    Sleep(300)
    Jump("loc_2557")

    label("loc_252E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_2557")

    def lambda_253C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_253C)
    Sleep(50)

    def lambda_254C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_254C)
    Sleep(300)

    label("loc_2557")


    ChrTalk(
        0x102,
        (
            "#11P#00109FHehe, you do not mind me.\x01",
            "I was a bit surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6POh, older sister ……\x01",
            "After all you are like a goddess.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#5PAnyway, if you feel like that here\x01",
            "You can come anytime, so we do not need any guidance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#5PGo to the next place quickly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FOh, ah ……\x02",
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

    # Function_5_1CAE end

    def Function_6_269F(): pass

    label("Function_6_269F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26C4")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_6_269F")

    label("loc_26C4")

    Return()

    # Function_6_269F end

    def Function_7_26C5(): pass

    label("Function_7_26C5")

    EventBegin(0x1)
    TurnDirection(0x1A2, 0x101, 0)

    ChrTalk(
        0x1A2,
        (
            "だからー、別にIBCを\x01",
            "You do not need to show me around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "I will finally go to the next place!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, ah ……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -160, 400, 5710, 180)
    EventEnd(0x4)
    Return()

    # Function_7_26C5 end

    def Function_8_2758(): pass

    label("Function_8_2758")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I. B. C\x01",
            "International Bank of Crossbell\x01\x01",
            "If you are inquiring about your tenant\x01",
            "At the first floor lobby counter\x01",
            "Please voice out.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_2758 end

    SaveToFile()

Try(main)
