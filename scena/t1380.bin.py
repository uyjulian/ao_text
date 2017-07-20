from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1380.bin",                # FileName
        "t1380",                    # MapName
        "t1380",                    # Location
        0x00BA,                     # MapIndex
        "ed7304",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 186, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1380",                  # 0
        "Erie",                 # 1
        "Tio",                 # 2
        "Noel",                 # 3
        "Waji",                   # 4
        "Franc",                 # 5
        "Lisha",               # 6
        "Missi",               # 7
        "apprentice",                 # 8
        "tourist",                 # 9
        "tourist",                 # 10
        "tourist",                 # 11
        "tourist",                 # 12
        "tourist",                 # 13
        "dummy",                 # 14
        "fortune teller",                 # 15
        "Zeit",               # 16
        "Misee",               # 17
    ))

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch00200.itc",                   # 01
        "chr/ch02900.itc",                   # 02
        "chr/ch03000.itc",                   # 03
        "chr/ch08500.itc",                   # 04
        "chr/ch05200.itc",                   # 05
        "chr/ch10200.itc",                   # 06
        "chr/ch20500.itc",                   # 07
        "chr/ch22802.itc",                   # 08
        "chr/ch22102.itc",                   # 09
        "chr/ch21102.itc",                   # 0A
        "chr/ch24502.itc",                   # 0B
        "chr/ch34302.itc",                   # 0C
        "chr/ch45400.itc",                   # 0D
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

    DeclNpc(4294966337, 0,       4294964197, 0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(4294965747, 0,       4294964796, 45,   389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4294966796, 0,       4294967046, 90,   389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(1500,    0,       4294964947, 90,   389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(500,     0,       4294967046, 270,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       4294967046, 0,    389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(1700,    0,       5940,    180,  389,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       6500,    180,  389,  0x0, 0,   7,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4800,    100,     4400,    270,  389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4800,    100,     3599,    270,  389,  0x0, 0,   9,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294962496, 100,     4000,    90,   389,  0x0, 0,   10,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294962496, 100,     4294966796, 90,   389,  0x0, 0,   11,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4294962496, 100,     4294965796, 90,   389,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294960796, 0,       2609,    180,  389,  0x0, 0,   13,  0,   0,   0,   255, 255, 255,  0)

    DeclEvent(0x0040, 0, 38,  0.0,                   8.0,                   -1.0,                  4.0,                   [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -0.0,                  -2.0,                  0.25,                  1.0])

    DeclActor(4294962246, 0,       2700,    1000,    4294960796, 1500,    2610,    0x007E, 0,  36, 0x0000)
    DeclActor(4294965426, 0,       5380,    1200,    4294965426, 1500,    5380,    0x007C, 0,  37, 0x0000)

    ChipFrameInfo(1068, 0)                                       # 0

    ScpFunction((
        "Function_0_42C",          # 00, 0
        "Function_1_4E4",          # 01, 1
        "Function_2_561",          # 02, 2
        "Function_3_58B",          # 03, 3
        "Function_4_6FD",          # 04, 4
        "Function_5_8E9",          # 05, 5
        "Function_6_990",          # 06, 6
        "Function_7_B06",          # 07, 7
        "Function_8_BBE",          # 08, 8
        "Function_9_D17",          # 09, 9
        "Function_10_DF7",         # 0A, 10
        "Function_11_EE8",         # 0B, 11
        "Function_12_100F",        # 0C, 12
        "Function_13_10ED",        # 0D, 13
        "Function_14_1226",        # 0E, 14
        "Function_15_1276",        # 0F, 15
        "Function_16_12D6",        # 10, 16
        "Function_17_1373",        # 11, 17
        "Function_18_1527",        # 12, 18
        "Function_19_1EE5",        # 13, 19
        "Function_20_2EAA",        # 14, 20
        "Function_21_2F5E",        # 15, 21
        "Function_22_3DD9",        # 16, 22
        "Function_23_3E1E",        # 17, 23
        "Function_24_3E68",        # 18, 24
        "Function_25_3E78",        # 19, 25
        "Function_26_4E08",        # 1A, 26
        "Function_27_5D03",        # 1B, 27
        "Function_28_6C92",        # 1C, 28
        "Function_29_7ADF",        # 1D, 29
        "Function_30_865F",        # 1E, 30
        "Function_31_9528",        # 1F, 31
        "Function_32_A2BB",        # 20, 32
        "Function_33_B0F1",        # 21, 33
        "Function_34_C01A",        # 22, 34
        "Function_35_CF17",        # 23, 35
        "Function_36_DE28",        # 24, 36
        "Function_37_E69C",        # 25, 37
        "Function_38_E700",        # 26, 38
    ))


    def Function_0_42C(): pass

    label("Function_0_42C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_46C"),
        (1, "loc_478"),
        (2, "loc_484"),
        (3, "loc_490"),
        (4, "loc_49C"),
        (5, "loc_4A8"),
        (6, "loc_4B4"),
        (SWITCH_DEFAULT, "loc_4C0"),
    )


    label("loc_46C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_478")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_484")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_490")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_49C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4A8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4E3")

    Return()

    # Function_0_42C end

    def Function_1_4E4(): pass

    label("Function_1_4E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_4F2")
    Jump("loc_560")

    label("loc_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_500")
    Jump("loc_560")

    label("loc_500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_50E")
    Jump("loc_560")

    label("loc_50E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_51F")
    Call(0, 17)
    Jump("loc_560")

    label("loc_51F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_52D")
    Jump("loc_560")

    label("loc_52D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_53B")
    Jump("loc_560")

    label("loc_53B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_549")
    Jump("loc_560")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_557")
    Jump("loc_560")

    label("loc_557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_560")

    label("loc_560")

    Return()

    # Function_1_4E4 end

    def Function_2_561(): pass

    label("Function_2_561")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58A")
    OP_66(0x0, 0x1)

    label("loc_58A")

    Return()

    # Function_2_561 end

    def Function_3_58B(): pass

    label("Function_3_58B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A4")
    Jump("loc_6F9")

    label("loc_5A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BA")
    Jump("loc_6F9")

    label("loc_5BA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D0")
    Jump("loc_6F9")

    label("loc_5D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E6")
    Jump("loc_6F9")

    label("loc_5E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_681")

    ChrTalk(
        0x8,
        (
            "#00100FWell, last ticket\x01",
            "Where should I use it?\x02\x03",
            "#00104FIt will be memorable if you can\x01",
            "Although it is good, but ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6F9")

    label("loc_681")


    ChrTalk(
        0x8,
        (
            "#00100FWhen you can do the last ticket\x01",
            "In places like memories\x01",
            "I'd like to use it ….\x02\x03",
            "#00104FWell, I wonder where I should go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F9")

    TalkEnd(0xFE)
    Return()

    # Function_3_58B end

    def Function_4_6FD(): pass

    label("Function_4_6FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_716")
    Jump("loc_8E5")

    label("loc_716")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72C")
    Jump("loc_8E5")

    label("loc_72C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_829")

    ChrTalk(
        0x9,
        (
            "#00200FMissishi from before\x01",
            "I am tracking it … ….\x02\x03",
            "Not limited to the main attraction,\x01",
            "I am actually traveling around various places.\x02\x03",
            "#00204FSo that fans can meet more\x01",
            "That's why I am doing my best.\x01",
            "…… Truly is MICHI.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8B9")

    label("loc_829")


    ChrTalk(
        0x9,
        (
            "#00200FAnyway, Misashi's sister\x01",
            "I do not see \"Mieee\" yet.\x02\x03",
            "#00204FPerhaps, the time zone that comes out is\x01",
            "Is it limited?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B9")

    Jump("loc_8E5")

    label("loc_8BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D4")
    Jump("loc_8E5")

    label("loc_8D4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E5")

    label("loc_8E5")

    TalkEnd(0xFE)
    Return()

    # Function_4_6FD end

    def Function_5_8E9(): pass

    label("Function_5_8E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_939")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90F")
    Call(0, 16)
    Jump("loc_934")

    label("loc_90F")


    ChrTalk(
        0xA,
        "#10106FEven if it already flies … …\x02",
    )

    CloseMessageWindow()

    label("loc_934")

    Jump("loc_98C")

    label("loc_939")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94F")
    Jump("loc_98C")

    label("loc_94F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_965")
    Jump("loc_98C")

    label("loc_965")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97B")
    Jump("loc_98C")

    label("loc_97B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98C")

    label("loc_98C")

    TalkEnd(0xFE)
    Return()

    # Function_5_8E9 end

    def Function_6_990(): pass

    label("Function_6_990")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A9")
    Jump("loc_B02")

    label("loc_9A9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BF")
    Jump("loc_B02")

    label("loc_9BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D5")
    Jump("loc_B02")

    label("loc_9D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA4")

    ChrTalk(
        0xB,
        (
            "#10300FHuh, here's the sofa\x01",
            "It is quite good to have things.\x02\x03",
            "#10304FUntil we decide where we will go next,\x01",
            "I'd like you to take a day off.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FCome on … …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_AEC")

    label("loc_AA4")


    ChrTalk(
        0xB,
        (
            "#10304FHuff, until we decide where we will turn next\x01",
            "I'd like you to take a day off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AEC")

    Jump("loc_B02")

    label("loc_AF1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B02")

    label("loc_B02")

    TalkEnd(0xFE)
    Return()

    # Function_6_990 end

    def Function_7_B06(): pass

    label("Function_7_B06")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2C")
    Call(0, 16)
    Jump("loc_B62")

    label("loc_B2C")


    ChrTalk(
        0xC,
        (
            "#06409FOnee 's love affair,\x01",
            "Let's take over!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B62")

    Jump("loc_BBA")

    label("loc_B67")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7D")
    Jump("loc_BBA")

    label("loc_B7D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B93")
    Jump("loc_BBA")

    label("loc_B93")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA9")
    Jump("loc_BBA")

    label("loc_BA9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBA")

    label("loc_BBA")

    TalkEnd(0xFE)
    Return()

    # Function_7_B06 end

    def Function_8_BBE(): pass

    label("Function_8_BBE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD7")
    Jump("loc_D13")

    label("loc_BD7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C54")

    ChrTalk(
        0xD,
        (
            "#01805F(Oriental mysterism … …)\x02\x03",
            "#01803F(You do not know it.\x01",
            "There are not … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xD, 0x10)
    Jump("loc_CD1")

    label("loc_C54")


    ChrTalk(
        0xD,
        (
            "#01805FAh … … Lloyd.\x01",
            "Yes, since when?\x02\x03",
            "#01809FHaha ……\x01",
            "I am waiting a lot in order\x01",
            "I was impressed with it again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD1")

    Jump("loc_D13")

    label("loc_CD6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEC")
    Jump("loc_D13")

    label("loc_CEC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D02")
    Jump("loc_D13")

    label("loc_D02")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D13")

    label("loc_D13")

    TalkEnd(0xFE)
    Return()

    # Function_8_BBE end

    def Function_9_D17(): pass

    label("Function_9_D17")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D30")
    Jump("loc_DF3")

    label("loc_D30")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D46")
    Jump("loc_DF3")

    label("loc_D46")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCC")

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "The fortune-teller's older sister here,\x01",
            "I am very good at it ~.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Misashi, various things\x01",
            "It would be nice to fortune it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF3")

    label("loc_DCC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE2")
    Jump("loc_DF3")

    label("loc_DE2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF3")

    label("loc_DF3")

    TalkEnd(0xFE)
    Return()

    # Function_9_D17 end

    def Function_10_DF7(): pass

    label("Function_10_DF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE4")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Welcome to the Fortune Teller!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Here, to the teacher of a heavenly fortune-teller\x01",
            "I will be able to tell you a lot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Mika and hide and seek in … …\x01",
            "What I am playing at attractions now\x01",
            "Let's stop it. )\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_EE7")

    label("loc_EE4")

    Call(0, 18)

    label("loc_EE7")

    Return()

    # Function_10_DF7 end

    def Function_11_EE8(): pass

    label("Function_11_EE8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F7D")

    ChrTalk(
        0x10,
        (
            "As expected, after all\x01",
            "There are a lot of girls' customers … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I am glad because it's with her,\x01",
            "It would be uncomfortable if only one person.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_100B")

    label("loc_F7D")


    ChrTalk(
        0x10,
        (
            "Good compatibility gives good results,\x01",
            "Her humor has improved considerably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If I think that delicate results will come … …\x01",
            "I do not think it's awkward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100B")

    TalkEnd(0xFE)
    Return()

    # Function_11_EE8 end

    def Function_12_100F(): pass

    label("Function_12_100F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1069")

    ChrTalk(
        0x11,
        (
            "Uhufu, I wonder what to make up for you.\x01",
            "I wonder if it is compatible with him after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E9")

    label("loc_1069")


    ChrTalk(
        0x11,
        (
            "If you ask for it,\x01",
            "We are the fateful thread\x01",
            "It is said to be tied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Hehehe …\x01",
            "In my eyes who chose him\x01",
            "There was no mistake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E9")

    TalkEnd(0xFE)
    Return()

    # Function_12_100F end

    def Function_13_10ED(): pass

    label("Function_13_10ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_116E")

    ChrTalk(
        0x12,
        (
            "With a husband in the hide,\x01",
            "The place of the married ring you lost\x01",
            "I came to fortune telling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "I wonder if the order will come soon …\x02",
    )

    CloseMessageWindow()
    Jump("loc_1222")

    label("loc_116E")


    ChrTalk(
        0x12,
        (
            "The wedding ring I thought was dropped,\x01",
            "If you ask for place ……\x01",
            "What a pocket you were in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "It is true that it darkens under the lighthouse …\x01",
            "Although I was glad I found it\x01",
            "It got me somewhat merciless.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1222")

    TalkEnd(0xFE)
    Return()

    # Function_13_10ED end

    def Function_14_1226(): pass

    label("Function_14_1226")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1272")

    ChrTalk(
        0x13,
        (
            "Implicit indication of a nice encounter\x01",
            "I am glad if it comes out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1272")

    label("loc_1272")

    TalkEnd(0xFE)
    Return()

    # Function_14_1226 end

    def Function_15_1276(): pass

    label("Function_15_1276")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12D2")

    ChrTalk(
        0x14,
        (
            "I do not care about a man,\x01",
            "I will have fortune telling luck.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D2")

    label("loc_12D2")

    TalkEnd(0xFE)
    Return()

    # Function_15_1276 end

    def Function_16_12D6(): pass

    label("Function_16_12D6")

    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "#06400FMy sister, Hey Hey ~.\x01",
            "Let's line up quickly ~.\x02\x03",
            "#06409FAnd, Onee's\x01",
            "Have love luck fortune telling!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#10111FIt is good!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_16_12D6 end

    def Function_17_1373(): pass

    label("Function_17_1373")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13BF")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_13BF")

    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x8)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0xA)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0xB)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0xC)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1461")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    Jump("loc_1526")

    label("loc_1461")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148B")
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1486")
    SetChrFlags(0xD, 0x10)

    label("loc_1486")

    Jump("loc_1526")

    label("loc_148B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AB")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_1526")

    label("loc_14AB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1506")
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14E6")
    SetChrFlags(0xB, 0x80)

    label("loc_14E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1501")
    ClearChrFlags(0x18, 0x80)

    label("loc_1501")

    Jump("loc_1526")

    label("loc_1506")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1526")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_1526")

    Return()

    # Function_17_1373 end

    def Function_18_1527(): pass

    label("Function_18_1527")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 1000, 5750, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_4B(0xF, 0xFF)
    SetChrPos(0x101, 0, 0, 5000, 0)
    OP_0D()

    ChrTalk(
        0xF,
        "Welcome to the Fortune Teller!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Here, to the teacher of a heavenly fortune-teller\x01",
            "I will be able to tell you a lot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "You can enter up to 2 people,\x01",
            "What can I do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#6P(Who should I invite…)\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 5, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWho invites you?\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Erie")
    MenuCmd(1, 0, "Tio")
    MenuCmd(1, 0, "Randy")
    MenuCmd(1, 0, "Noel")
    MenuCmd(1, 0, "Waji")
    MenuCmd(1, 0, "Keya")
    MenuCmd(1, 0, "Franc")
    MenuCmd(1, 0, "Cecil")
    MenuCmd(1, 0, "Ilia")
    MenuCmd(1, 0, "Lisha")
    MenuCmd(1, 0, "Shuri")
    MenuCmd(1, 0, "quit")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_16FB")
    MenuCmd(3, 0, 0x0)

    label("loc_16FB")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_170D")
    MenuCmd(3, 0, 0x1)

    label("loc_170D")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_171F")
    MenuCmd(3, 0, 0x2)

    label("loc_171F")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1731")
    MenuCmd(3, 0, 0x3)

    label("loc_1731")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1743")
    MenuCmd(3, 0, 0x4)

    label("loc_1743")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1755")
    MenuCmd(3, 0, 0x5)

    label("loc_1755")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1767")
    MenuCmd(3, 0, 0x6)

    label("loc_1767")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1779")
    MenuCmd(3, 0, 0x7)

    label("loc_1779")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_178B")
    MenuCmd(3, 0, 0x8)

    label("loc_178B")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_179D")
    MenuCmd(3, 0, 0x9)

    label("loc_179D")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_17AF")
    MenuCmd(3, 0, 0xA)

    label("loc_17AF")

    MenuCmd(2, 0, -1, 55, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E84")
    OP_D2(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1835"),
        (1, "loc_1875"),
        (2, "loc_18B5"),
        (3, "loc_18F7"),
        (4, "loc_1937"),
        (5, "loc_1975"),
        (6, "loc_19B5"),
        (7, "loc_19F5"),
        (8, "loc_1A37"),
        (9, "loc_1A7B"),
        (10, "loc_1ABD"),
        (SWITCH_DEFAULT, "loc_1AFD"),
    )


    label("loc_1835")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Okay … let's invite Ellie.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_1875")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Tio.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_18B5")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Randy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_18F7")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Okay … let's invite Noel.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_1937")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Okay … let's invite Wazi.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_1975")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Ka'a.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_19B5")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite the franc.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_19F5")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Cecil 's older sister.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_1A37")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Iria.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_1A7B")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Ok let's ask Rixia)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_1ABD")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Sri.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AFD")

    label("loc_1AFD")

    FadeToDark(500, 0, -1)
    OP_0D()
    LoadEffect(0x0, "event/ev13000.eff")
    LoadChrToIndex("chr/ch14202.itc", 0x1E)
    LoadChrToIndex("chr/ch00002.itc", 0x1F)
    LoadChrToIndex("chr/ch00300.itc", 0x21)
    LoadChrToIndex("chr/ch08200.itc", 0x22)
    LoadChrToIndex("chr/ch07500.itc", 0x23)
    LoadChrToIndex("chr/ch05100.itc", 0x24)
    LoadChrToIndex("chr/ch10100.itc", 0x25)
    LoadChrToIndex("chr/ch02710.itc", 0x26)
    LoadChrToIndex("chr/ch02702.itc", 0x27)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrPos(0x16, 0, 50, 104800, 180)
    ClearChrFlags(0x15, 0x80)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1BC1"),
        (1, "loc_1BD0"),
        (2, "loc_1BDF"),
        (3, "loc_1BEE"),
        (4, "loc_1BFD"),
        (5, "loc_1C0C"),
        (6, "loc_1C1B"),
        (7, "loc_1C2A"),
        (8, "loc_1C39"),
        (9, "loc_1C48"),
        (10, "loc_1C57"),
        (SWITCH_DEFAULT, "loc_1C66"),
    )


    label("loc_1BC1")

    LoadChrToIndex("chr/ch00102.itc", 0x20)
    SetChrChipByIndex(0x15, 0x0)
    Jump("loc_1C66")

    label("loc_1BD0")

    LoadChrToIndex("chr/ch00202.itc", 0x20)
    SetChrChipByIndex(0x15, 0x1)
    Jump("loc_1C66")

    label("loc_1BDF")

    LoadChrToIndex("chr/ch00302.itc", 0x20)
    SetChrChipByIndex(0x15, 0x21)
    Jump("loc_1C66")

    label("loc_1BEE")

    LoadChrToIndex("chr/ch02902.itc", 0x20)
    SetChrChipByIndex(0x15, 0x2)
    Jump("loc_1C66")

    label("loc_1BFD")

    LoadChrToIndex("chr/ch03002.itc", 0x20)
    SetChrChipByIndex(0x15, 0x3)
    Jump("loc_1C66")

    label("loc_1C0C")

    LoadChrToIndex("chr/ch08202.itc", 0x20)
    SetChrChipByIndex(0x15, 0x22)
    Jump("loc_1C66")

    label("loc_1C1B")

    LoadChrToIndex("chr/ch08502.itc", 0x20)
    SetChrChipByIndex(0x15, 0x4)
    Jump("loc_1C66")

    label("loc_1C2A")

    LoadChrToIndex("chr/ch07502.itc", 0x20)
    SetChrChipByIndex(0x15, 0x23)
    Jump("loc_1C66")

    label("loc_1C39")

    LoadChrToIndex("chr/ch05102.itc", 0x20)
    SetChrChipByIndex(0x15, 0x24)
    Jump("loc_1C66")

    label("loc_1C48")

    LoadChrToIndex("chr/ch05202.itc", 0x20)
    SetChrChipByIndex(0x15, 0x5)
    Jump("loc_1C66")

    label("loc_1C57")

    LoadChrToIndex("chr/ch10102.itc", 0x20)
    SetChrChipByIndex(0x15, 0x25)
    Jump("loc_1C66")

    label("loc_1C66")

    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x101, -500, 0, 5000, 0)
    SetChrPos(0x15, 500, 0, 5000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xF,
        "I'll take your tickets then\x02",
    )

    CloseMessageWindow()
    SubItemNumber('米修拉姆·奇幻乐园游乐券', 1)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I handed one ticket to the staff.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xF,
        "Well then please go in\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 19)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x15, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_1DB9"),
        (1, "loc_1DC7"),
        (2, "loc_1DD5"),
        (3, "loc_1DE3"),
        (4, "loc_1DF1"),
        (5, "loc_1DFF"),
        (6, "loc_1E0D"),
        (7, "loc_1E1B"),
        (8, "loc_1E29"),
        (9, "loc_1E37"),
        (10, "loc_1E45"),
        (SWITCH_DEFAULT, "loc_1E53"),
    )


    label("loc_1DB9")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1DC7")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1DD5")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1DE3")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1DF1")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1DFF")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1E0D")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1E1B")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1E29")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1E37")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1E45")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1E53")

    label("loc_1E53")

    OP_D2(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E7F")
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()

    label("loc_1E7F")

    Jump("loc_1ECD")

    label("loc_1E84")


    ChrTalk(
        0xF,
        "Oh, is it not acceptable to you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "I'm waiting for you again!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1ECD")

    OP_4C(0xF, 0xFF)
    SetChrPos(0x0, 0, 0, 4000, 180)
    EventEnd(0x5)
    Return()

    # Function_18_1527 end

    def Function_19_1EE5(): pass

    label("Function_19_1EE5")

    SoundLoad(852)
    SetChrPos(0x101, -500, 0, 93000, 0)
    SetChrPos(0x15, 500, 0, 93000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 900, 97500, 0)
    MoveCamera(0, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    FadeToBright(1000, 0)
    OP_68(0, 900, 100000, 3000)
    Sleep(500)

    def lambda_1F70():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F70)

    def lambda_1F81():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1F81)

    def lambda_1F92():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F92)
    Sleep(0)

    def lambda_1FAA():
        OP_9B(0x0, 0x15, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1FAA)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x15, 0)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x15, 2)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2939")

    ChrTalk(
        0x16,
        "#5PEheh, welcome\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PWell then please sit here\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PR-right\x02",
    )

    CloseMessageWindow()
    Call(0, 20)

    ChrTalk(
        0x101,
        (
            "#00003F#6P(As you heard about the story,\x01",
            "It is an exotic and mysterious person … …)\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_20DD"),
        (1, "loc_2133"),
        (2, "loc_2196"),
        (3, "loc_21FB"),
        (4, "loc_2260"),
        (5, "loc_22FE"),
        (6, "loc_2352"),
        (7, "loc_23AE"),
        (8, "loc_2404"),
        (9, "loc_245C"),
        (10, "loc_24BC"),
        (SWITCH_DEFAULT, "loc_251B"),
    )


    label("loc_20DD")


    NpcTalk(
        0x15,
        "Erie",
        (
            "#00100F#12P(Yeah, and my face is hiding.\x01",
            "It looks like a very beautiful person. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_2133")


    NpcTalk(
        0x15,
        "Tio",
        (
            "#00200F#12P(Yeah, and … …\x01",
            "My face is hiding, but\x01",
            "It looks pretty beautiful. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_2196")


    NpcTalk(
        0x15,
        "Randy",
        (
            "#00300F#12P(Oh, and it … ….\x01",
            "The face is hiding but pretty beautiful\x01",
            "My older sister. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_21FB")


    NpcTalk(
        0x15,
        "Noel",
        (
            "#10100F#12P(Yeah, and … …\x01",
            "I hide my face,\x01",
            "It looks like a very beautiful one. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_2260")


    NpcTalk(
        0x15,
        "Waji",
        "#10305F#12P(………… Hey … … … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P(…… Wadi?)\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Waji",
        (
            "#10304F#12P(Huh, I'm so beautiful\x01",
            "A little surprised. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_22FE")


    NpcTalk(
        0x15,
        "Keya",
        (
            "#01100F#12P(Yeah, and my face is hiding.\x01",
            "It looks like a beautiful human. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_2352")


    NpcTalk(
        0x15,
        "Franc",
        (
            "#06400F#12P(Yeah, and my face is hiding.\x01",
            "It looks like a beautiful woman ~. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_23AE")


    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05900F#12P(Yeah, and my face is hiding.\x01",
            "She looks like a very beautiful person. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_2404")


    NpcTalk(
        0x15,
        "Ilia",
        (
            "#01700F#12P(Yeah, and my face is hiding.\x01",
            "She looks pretty beautiful. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_245C")


    NpcTalk(
        0x15,
        "Lisha",
        (
            "#01802F#12P(Yes … the face is hidden,\x01",
            "It looks like a very beautiful person … …)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_24BC")


    NpcTalk(
        0x15,
        "Shuri",
        (
            "#14000F#12P(Oh, and it … ….\x01",
            "I hide my face,\x01",
            "It looks like a beautiful woman. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251B")

    label("loc_251B")


    ChrTalk(
        0x16,
        (
            "#5PHuhu, what's wrong?\x01",
            "Looking at the face of a human being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PBecause some people are waiting\x01",
            "I'd like to start working right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6POh, I'm sorry.\x01",
            "Well, thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PEhe, well before that\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PFirst of all, your\x01",
            "Could you tell me your blood type?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_269B"),
        (1, "loc_26CA"),
        (2, "loc_26F9"),
        (3, "loc_2726"),
        (4, "loc_2751"),
        (5, "loc_2778"),
        (6, "loc_279F"),
        (7, "loc_27CC"),
        (8, "loc_27FB"),
        (9, "loc_2839"),
        (10, "loc_286A"),
        (SWITCH_DEFAULT, "loc_2893"),
    )


    label("loc_269B")


    NpcTalk(
        0x15,
        "Erie",
        "#00105F#12PBlood type?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_26CA")


    NpcTalk(
        0x15,
        "Tio",
        "#00205F#12PBlood type?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_26F9")


    NpcTalk(
        0x15,
        "Randy",
        "#00305F#12PIs it blood type?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_2726")


    NpcTalk(
        0x15,
        "Noel",
        "#10105F#12PIs it blood type?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_2751")


    NpcTalk(
        0x15,
        "Waji",
        "#10305F#12PBlood type?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_2778")


    NpcTalk(
        0x15,
        "Keya",
        "#01105F#12PBlood type -?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_279F")


    NpcTalk(
        0x15,
        "Franc",
        "#06405F#12PIs it a blood type?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_27CC")


    NpcTalk(
        0x15,
        "Cecil",
        "#05905F#12PBlood type?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_27FB")


    NpcTalk(
        0x15,
        "Ilia",
        (
            "#01705F#12Pblood type……\x01",
            "Is it necessary for something?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_2839")


    NpcTalk(
        0x15,
        "Lisha",
        "#01805F#12PBlood type?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_286A")


    NpcTalk(
        0x15,
        "Shuri",
        "#14005F#12Pblood type……?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_2893")


    ChrTalk(
        0x16,
        (
            "#5PYes, to precisely account for it\x01",
            "It is necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5POf course, impossible\x01",
            "I do not say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PNo, if that is the case.\x01",
            "…… My blood type is O type.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A72")

    label("loc_2939")


    ChrTalk(
        0x16,
        "#5POh, you made up earlier …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PEheh, welcome\x01",
            "Please go to this chair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYes.\x02",
    )

    CloseMessageWindow()
    Call(0, 20)

    ChrTalk(
        0x16,
        (
            "#5PIt seems they came again\x01",
            "I'm happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PWell then,\x01",
            "Your blood type\x01",
            "Could you tell me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P…… You there,\x01",
            "It was certainly O type.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYes, that's right.\x02",
    )

    CloseMessageWindow()

    label("loc_2A72")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2ABD"),
        (1, "loc_2AF6"),
        (2, "loc_2B2D"),
        (3, "loc_2B5A"),
        (4, "loc_2B8B"),
        (5, "loc_2BC6"),
        (6, "loc_2C45"),
        (7, "loc_2CA2"),
        (8, "loc_2CD5"),
        (9, "loc_2D02"),
        (10, "loc_2D5B"),
        (SWITCH_DEFAULT, "loc_2D97"),
    )


    label("loc_2ABD")


    NpcTalk(
        0x15,
        "Erie",
        "#00100F#12PWell, I am A type.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2AF6")


    NpcTalk(
        0x15,
        "Tio",
        "#00200F#12PI am AB type.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2B2D")


    NpcTalk(
        0x15,
        "Randy",
        "#00300F#12PI'm B type.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2B5A")


    NpcTalk(
        0x15,
        "Noel",
        "#10100F#12PI am A type.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2B8B")


    NpcTalk(
        0x15,
        "Waji",
        "#10300F#12PI guess it was AB type surely?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2BC6")


    NpcTalk(
        0x15,
        "Keya",
        (
            "#01109F#12PEr, Ka'aa\x01",
            "Certainly B type.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6POh, before at Ursula hospital\x01",
            "I had something inspected.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2C45")


    NpcTalk(
        0x15,
        "Franc",
        "#06409F#12POh, I am an O type too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#6PHaha, you are the same.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2CA2")


    NpcTalk(
        0x15,
        "Cecil",
        "#05900F#12PEr, I am A type.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2CD5")


    NpcTalk(
        0x15,
        "Ilia",
        "#01700F#12PI am type B.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2D02")


    NpcTalk(
        0x15,
        "Lisha",
        "#01802F#12POh I'm also type O\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#6PAha, what a coincidence\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2D5B")


    NpcTalk(
        0x15,
        "Shuri",
        (
            "#14000F#12PEr …\x01",
            "Perhaps I am A.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D97")

    label("loc_2D97")


    ChrTalk(
        0x16,
        "#5PEhe, thank you\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PWell then what should we read\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PUh, well then\x02",
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2E48"),
        (1, "loc_2E50"),
        (2, "loc_2E58"),
        (3, "loc_2E60"),
        (4, "loc_2E68"),
        (5, "loc_2E70"),
        (6, "loc_2E78"),
        (7, "loc_2E80"),
        (8, "loc_2E88"),
        (9, "loc_2E90"),
        (10, "loc_2E98"),
        (SWITCH_DEFAULT, "loc_2EA0"),
    )


    label("loc_2E48")

    Call(0, 25)
    Jump("loc_2EA0")

    label("loc_2E50")

    Call(0, 26)
    Jump("loc_2EA0")

    label("loc_2E58")

    Call(0, 27)
    Jump("loc_2EA0")

    label("loc_2E60")

    Call(0, 28)
    Jump("loc_2EA0")

    label("loc_2E68")

    Call(0, 29)
    Jump("loc_2EA0")

    label("loc_2E70")

    Call(0, 30)
    Jump("loc_2EA0")

    label("loc_2E78")

    Call(0, 31)
    Jump("loc_2EA0")

    label("loc_2E80")

    Call(0, 32)
    Jump("loc_2EA0")

    label("loc_2E88")

    Call(0, 33)
    Jump("loc_2EA0")

    label("loc_2E90")

    Call(0, 34)
    Jump("loc_2EA0")

    label("loc_2E98")

    Call(0, 35)
    Jump("loc_2EA0")

    label("loc_2EA0")

    OP_24(0x354)
    Call(0, 17)
    Call(0, 21)
    Return()

    # Function_19_1EE5 end

    def Function_20_2EAA(): pass

    label("Function_20_2EAA")

    OP_68(0, 900, 103500, 3000)
    SetCameraDistance(15000, 3000)

    def lambda_2EC9():
        OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2EC9)

    def lambda_2EDE():
        OP_9B(0x0, 0xFE, 0xA, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2EDE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x15, 1)

    def lambda_2EFB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2EFB)

    def lambda_2F08():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2F08)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x15, 2)
    OP_6F(0x79)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -630, 50, 101950, 0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 630, 50, 101950, 0)
    OP_0D()
    Return()

    # Function_20_2EAA end

    def Function_21_2F5E(): pass

    label("Function_21_2F5E")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2FB1"),
        (1, "loc_2FBA"),
        (2, "loc_2FC3"),
        (3, "loc_2FCC"),
        (4, "loc_2FD5"),
        (5, "loc_2FDE"),
        (6, "loc_2FE7"),
        (7, "loc_2FF0"),
        (8, "loc_2FF9"),
        (9, "loc_3002"),
        (10, "loc_300B"),
        (SWITCH_DEFAULT, "loc_3014"),
    )


    label("loc_2FB1")

    SetChrChipByIndex(0x15, 0x0)
    Jump("loc_3014")

    label("loc_2FBA")

    SetChrChipByIndex(0x15, 0x1)
    Jump("loc_3014")

    label("loc_2FC3")

    SetChrChipByIndex(0x15, 0x21)
    Jump("loc_3014")

    label("loc_2FCC")

    SetChrChipByIndex(0x15, 0x2)
    Jump("loc_3014")

    label("loc_2FD5")

    SetChrChipByIndex(0x15, 0x3)
    Jump("loc_3014")

    label("loc_2FDE")

    SetChrChipByIndex(0x15, 0x22)
    Jump("loc_3014")

    label("loc_2FE7")

    SetChrChipByIndex(0x15, 0x4)
    Jump("loc_3014")

    label("loc_2FF0")

    SetChrChipByIndex(0x15, 0x23)
    Jump("loc_3014")

    label("loc_2FF9")

    SetChrChipByIndex(0x15, 0x24)
    Jump("loc_3014")

    label("loc_3002")

    SetChrChipByIndex(0x15, 0x5)
    Jump("loc_3014")

    label("loc_300B")

    SetChrChipByIndex(0x15, 0x25)
    Jump("loc_3014")

    label("loc_3014")

    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -600, 0, 5000, 90)
    SetChrPos(0x15, 600, 0, 5000, 270)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3068")
    SetChrPos(0x17, 1700, 0, 4040, 270)

    label("loc_3068")

    OP_68(0, 1500, 5750, 0)
    OP_68(0, 1000, 5750, 3000)
    MoveCamera(0, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_30FE"),
        (1, "loc_321B"),
        (2, "loc_333B"),
        (3, "loc_346E"),
        (4, "loc_358A"),
        (5, "loc_3695"),
        (6, "loc_3810"),
        (7, "loc_393F"),
        (8, "loc_3A4D"),
        (9, "loc_3B75"),
        (10, "loc_3CBF"),
        (SWITCH_DEFAULT, "loc_3DD8"),
    )


    label("loc_30FE")


    NpcTalk(
        0x15,
        "Erie",
        (
            "#00100F#11PHaa … somehow very\x01",
            "It was a mysterious time.\x02\x03",
            "#00104FTo the atmosphere of that fortune-teller\x01",
            "It seemed like I could be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PAh……\x01",
            "It seems not to be an ordinary person.\x02\x03",
            "#00000FWell then, then\x01",
            "I am here once.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Erie",
        "#00100F#11PWell, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_321B")


    NpcTalk(
        0x15,
        "Tio",
        (
            "#00202FTo that fortune-teller's fortune-telling\x01",
            "I felt quite an aura.\x02\x03",
            "#00204FAfter all there was only a rumorous fortune-teller\x01",
            "It looks like it is not an ordinary person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004Fsurely……\x01",
            "It was kinda kinda person somehow.\x02\x03",
            "#00000FWell then, then\x01",
            "I am here once.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Tio",
        "#00200FWell, see you then.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_333B")


    NpcTalk(
        0x15,
        "Randy",
        (
            "#00309FHap …\x01",
            "I wish you a nice sister.\x02\x03",
            "#00304FThat mysterious atmosphere\x01",
            "Are not you Tamanen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha … for sure.\x01",
            "Fortunately fortunately\x01",
            "It seems that the line was passing.\x02\x03",
            "#00000FWell then, then\x01",
            "I am here once.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Randy",
        "#00300FOh, I guess so.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_346E")


    NpcTalk(
        0x15,
        "Noel",
        (
            "#10100F…… Fuu, somehow tremendously\x01",
            "You had a mysterious time.\x02\x03",
            "#10104FFortune telling was also convincing,\x01",
            "It is somewhat strange feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FAh……\x01",
            "It was quite interesting.\x02\x03",
            "#00000FWell then, then\x01",
            "I am here once.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noel",
        "#10100FWell, see you again!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_358A")


    NpcTalk(
        0x15,
        "Waji",
        (
            "#10300FHugh, it's quite interesting\x01",
            "It was my older sister.\x02\x03",
            "#10304FA little more\x01",
            "I wanted to talk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, for sure.\x01",
            "Somehow the world view\x01",
            "It is likely to spread.\x02\x03",
            "#00000FWell then, then\x01",
            "I am here once.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Waji",
        "#10300FOh, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_3695")


    NpcTalk(
        0x15,
        "Keya",
        (
            "#01109FFortunetelling was very funny.\x02\x03",
            "#01111FWhy do you understand such various things?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FWell, I do not know ……\x01",
            "Surely considerable training\x01",
            "I guess they were loaded.\x02\x03",
            "#00000FWell then, then\x01",
            "I am here once.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Keya",
        "#01100FYes, again!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3801")

    ChrTalk(
        0x17,
        "#01200F……won.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    EndChrThread(0x17, 0x0)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    OP_93(0x17, 0xB4, 0x1F4)

    def lambda_37DF():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_37DF)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x15, 3)
    SetChrFlags(0x17, 0x80)
    Jump("loc_380B")

    label("loc_3801")

    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)

    label("loc_380B")

    Jump("loc_3DD8")

    label("loc_3810")


    NpcTalk(
        0x15,
        "Franc",
        (
            "#06402FHaha, what is it?\x01",
            "It was a mysterious older sister.\x02\x03",
            "#06409FShe looks like an older sister.\x01",
            "I also like a cool woman,\x01",
            "Such a person will adore too ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHahaha … … on the crossbell\x01",
            "It's not quite a type.\x02\x03",
            "#00000FWell then, then\x01",
            "I am here once.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Franc",
        "#06400FYes, again ~!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_393F")


    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05909FHehe …\x01",
            "It was a strange person.\x02\x03",
            "#05904FThere seems to be various pastes\x01",
            "Although it was ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh …… How did it go?\x01",
            "I wonder if you came to the crossbell.\x02\x03",
            "#00000FWell then, then\x01",
            "I am here once.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Cecil",
        "#05900FWell, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_3A4D")


    NpcTalk(
        0x15,
        "Ilia",
        (
            "#01702FWow, in the world\x01",
            "There are various and amazing people.\x02\x03",
            "#01703FFor the first time to see you, for anything\x01",
            "It was like I was being seen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, for sure …\x01",
            "It looked like it was not an ordinary person.\x02\x03",
            "#00000FWell then, then\x01",
            "I am here once.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Ilia",
        "#01700FWell, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_3B75")


    NpcTalk(
        0x15,
        "Lisha",
        (
            "#01803F(That high order occupation ……\x01",
            "Perhaps, that woman … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FRixia, what's wrong\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Lisha",
        (
            "#01805FAh, nothing\x02\x03",
            "#01802FHuhu, I got a magical experience\x01",
            "It was a lot of fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FAhah, same for me\x02\x03",
            "#00000FWell then, then\x01",
            "I am here once.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Lisha",
        "#01803FYes, see you later\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_3CBF")


    NpcTalk(
        0x15,
        "Shuri",
        (
            "#14000F…… It was sort of a terrible fortune-teller.\x02\x03",
            "#14006FI did not really believe in fortunetelling,\x01",
            "I can not say that this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FAh……\x01",
            "It certainly was a terrible fortune telling.\x02\x03",
            "#00000FWell then, then\x01",
            "I am here once.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Shuri",
        "#14000F…… Sounds like that.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DD8")

    label("loc_3DD8")

    Return()

    # Function_21_2F5E end

    def Function_22_3DD9(): pass

    label("Function_22_3DD9")


    def lambda_3DDE():

        label("loc_3DDE")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_3DDE")

    QueueWorkItem2(0x101, 2, lambda_3DDE)
    OP_93(0x15, 0xB4, 0x1F4)

    def lambda_3DF7():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3DF7)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x15, 1)
    EndChrThread(0x101, 0x2)
    Return()

    # Function_22_3DD9 end

    def Function_23_3E1E(): pass

    label("Function_23_3E1E")

    Fade(500)
    Sound(895, 0, 50, 0)
    Sound(852, 2, 70, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 900, 103300, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Return()

    # Function_23_3E1E end

    def Function_24_3E68(): pass

    label("Function_24_3E68")

    Fade(500)
    StopSound(852, 1000, 40)
    StopEffect(0x0, 0x2)
    OP_0D()
    Return()

    # Function_24_3E68 end

    def Function_25_3E78(): pass

    label("Function_25_3E78")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat does it take up to?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Two people compatibility\x01",      # 0
            "Leave it to Ellie\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4737")

    ChrTalk(
        0x101,
        (
            "#00000F#6POur compatibility\x01",
            "Could you please fortune?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, of course\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Erie",
        "#00112F#12PB, Lloyd …! Is it?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PNo, I came by two people\x01",
            "Such opportunities are not easy either.\x02\x03",
            "#00000FWhy do not you try it on a trial basis?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Erie",
        "#00106F#12PYou, you trying degree, are not you …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PEr … Did something masu?\x02\x03",
            "#00003FIf I do not want to do that much, I will ……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Erie",
        (
            "#00105F#12PAh, I mean ….\x02\x03",
            "#00113FWhy does not you like this anymore ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Erie",
        (
            "#00111F#12P…… Ha, nothing.\x02\x03",
            "#00100FI'm sorry, compatibility compatibility\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PHuhu, then …………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Erie",
        "#00101F#12P(Gokuri ……)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PA young man with straight eyes\x01",
            "A diligent and talented woman … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAs a companion with the same purpose\x01",
            "Together with many hardships,\x01",
            "It is bound with a firm bond … …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_4388")
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#5POh … and yet,\x01",
            "By falling into something extreme condition\x01",
            "It seems that it made a big progress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAlthough it is not decisive yet,\x01",
            "If you grow your thoughts like this,\x01",
            "Both can be deep friends.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4413")

    label("loc_4388")


    ChrTalk(
        0x16,
        (
            "#5PBorn differently,\x01",
            "Acknowledge each other's advantages\x01",
            "Supplementary relationship …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf you grow your thoughts like this,\x01",
            "Both are deep friends\x01",
            "You may be getting it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4413")

    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5PWell that's what I'm able to see\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Erie",
        "#00112F#12PWell, deep friends …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHuhu, well ……\x01",
            "That's what I say\x01",
            "It will be noriko.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHowever, it is\x01",
            "Your future actions and choices ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PO, is it me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAt least, feelings of the partner\x01",
            "Effort to make a mind is to keep in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PTo you, unconsciously\x01",
            "Magical charm that surrounds the surroundings ─\x01",
            "Because that suggestion can be seen.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012F#6PWell, it's magic ……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Erie",
        "#00106F#12P(I feel like I'm pretty awed … ….)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PBut fortune tells to the last\x01",
            "It is fortunetelling, not prophecy …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P\"Fate\" is the causal law\x01",
            "Because it is always moving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PDepending on your actions in the future\x01",
            "Any number of things can change …\x01",
            "Remember that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PR-right\x01",
            "I will bear in my heart.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DFC")

    label("loc_4737")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PErie,\x01",
            "Is there anything I want to divorce?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Erie",
        (
            "#00105F#12POh, can I decide?\x02\x03",
            "#00103FWell, well … hey ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Erie",
        (
            "#00100F#12Pin that case……\x01",
            "The future of Crossbell Autonomous Region\x01",
            "Why do not you ask for divination?\x02\x03",
            "#00103FBecause independent advocacy was done\x01",
            "What will happen …\x01",
            "Do not you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#6POh, certainly.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00000F#6P……Well then,\x01",
            "May I ask you?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x16,
        "#5PHehe, I cheap.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Erie",
        "#00101F#12P(Gokuri ……)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5P…… In the near future, you\x01",
            "It can get caught up in a very big cause …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI have never seen it before.\x01",
            "Huge \"wall\" and despair to face … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PIt will taste it.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PHuh……! Is it?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Erie",
        "#00105F#12PWell, that … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P…… I do not know what it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHowever,\x01",
            "I am steadily approaching you … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P…… I have seen it to me.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x15)

    NpcTalk(
        0x15,
        "Erie",
        "#00103F#12P…… Yes, what is it … now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PHuge \"wall\" … ….\x01",
            "Despair to it … …\x02\x03",
            "#00008FNo way, the mayor's\x01",
            "Something in the relationship of independent advocacy … …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P…… I do not know the detail.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PMy fortune tells to the last, imply\x01",
            "Because it is until I read it.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Erie",
        (
            "#00106F#12PWell, though …\x01",
            "We only have to care about it now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PApparently, I worry about extra care.\x01",
            "You seemed to have fueled it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PBut fortune tells to the last\x01",
            "It is fortunetelling, not prophecy …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P\"Fate\" is the causal law\x01",
            "Because it is always moving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PDepending on your actions in the future\x01",
            "Any number of things can change …\x01",
            "Remember that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6P… …. Yes, I will keep myself into account.\x02",
    )

    CloseMessageWindow()

    label("loc_4DFC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_25_3E78 end

    def Function_26_4E08(): pass

    label("Function_26_4E08")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat does it take up to?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Two people compatibility\x01",      # 0
            "Leave it to Tio\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5687")

    ChrTalk(
        0x101,
        (
            "#00000F#6POur compatibility\x01",
            "Could you please fortune?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, of course\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6P…… but what about you?\x01",
            "I came and I tried it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00203F#12P…… Hmm, it looks interesting.\x02\x03",
            "#00200FWhatever the outcome is,\x01",
            "I also wish to change my future direction\x01",
            "You can think about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P…… I do not understand the meaning well.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00203F#12PNo, you do not have to understand it separately.\x02\x03",
            "#00200FThen, please fortune teller.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PHuhu, then then …………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00205F#12P(… perception of a strange aura … ….\x01",
            "Is this all …? )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PA young man with straight eyes\x01",
            "A girl who has outstanding ability … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAge is far apart,\x01",
            "As very equal friends\x01",
            "I trust each other … …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_5297")
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#5POh … and yet,\x01",
            "By falling into something extreme condition\x01",
            "It seems that it made a big progress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI think there are various walls,\x01",
            "The possibility of becoming a deep relationship is quite high\x01",
            "There is an implication that it is.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5326")

    label("loc_5297")


    ChrTalk(
        0x16,
        (
            "#5PBorn differently,\x01",
            "Acknowledge each other's advantages\x01",
            "Supplementary relationship …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI think there are various walls,\x01",
            "The possibility of becoming a close friend\x01",
            "There will be enough.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5326")

    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5PWell that's what I'm able to see\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    NpcTalk(
        0x15,
        "Tio",
        "#00204F#12PHmm … … I got interesting results.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PWell, I mean well … …\x02\x03",
            "#00000F\"Various walls\" is\x01",
            "What on earth are you …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHuhu, if it is said\x01",
            "Social contraindications and others' slook … …\x01",
            "That's the place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThe preparedness to overcome it\x01",
            "If you have it, or … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PEr …\x01",
            "Preparedness is nothing ……\x02\x03",
            "#00003FTo deepen ties with Tio,\x01",
            "Apart from other people's gaze\x01",
            "I do not mind … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Tio",
        "#00211F#12P… what kind of bombs are you saying?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PHeck …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHehe, it is quite an interesting person.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIn the future,\x01",
            "Do not invite many disasters\x01",
            "I just pray to the goddess.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Tio",
        "#00206F#12PYes, it is exactly right.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6PAA no……\x01",
            "Leave me and clean\x01",
            "I wonder if you do not talk ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CF7")

    label("loc_5687")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PTio,\x01",
            "Is there anything I want to divine?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00205F#12PCan I decide?\x02\x03",
            "#00203F……I agree……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00200F#12PMy compatibility with Mitsushita,\x01",
            "Could you please tell me that?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6POnly, compatibility of Mitsite … …?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00202F#12PWell, Mitsutoshi in the future\x01",
            "Can I touch each other and live …?\x01",
            "I'd like you to forte it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        (
            "#5PHmm, it is pretty unique.\x01",
            "… … It would be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00205F#12P(… perception of a strange aura … ….\x01",
            "Is this all …? )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5P…… The compatibility between you and Mitsui … …\x01",
            "Apparently it looks pretty good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAs long as you love,\x01",
            "Missi surely will respond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIn the future as well, only a few good goods and\x01",
            "Contact at the theme park is waiting …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5PWell that's what I'm able to see\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Tio",
        "#00202F#12PHehe, thank you.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PWell, good.\x01",
            "Mitsushi surely responds.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00204F#12PYeah, as a fan\x01",
            "There is nothing more than this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5POh, and another one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIn a while, your\x01",
            "Try the feelings of Missi,\x01",
            "A big ordeal comes …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThere is such an implication.\x01",
            "…… At best you should be careful.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00200F#12P…… I want it.\x02\x03",
            "#00201FWhatever challenges will come,\x01",
            "This love of Miss you\x01",
            "I can not shake it … …\x02\x03",
            "#00204FLet me prove it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHehe, I support you.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6P(Do not do it.\x01",
            "There are too many places\x01",
            "I can not handle it … ___ ___ 0 )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CF7")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_26_4E08 end

    def Function_27_5D03(): pass

    label("Function_27_5D03")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat does it take up to?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Two people compatibility\x01",      # 0
            "Leave it to Randy\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6566")

    ChrTalk(
        0x101,
        (
            "#00000F#6POur compatibility\x01",
            "Could you please fortune?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, of course\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00306F#12PYou … you are,\x01",
            "Do whatever you are interested in.\x02\x03",
            "#00301FInvestigate the compatibility between the bastards\x01",
            "What's fun is that.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PWell, is not it okay?\x02\x03",
            "#00000FEven if I say compatibility with it,\x01",
            "There is also compatibility with male friends, do not you?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00306F#12PHmm … well, it's okay.\x02\x03",
            "#00300FThen, my sister, thank you for asking my best regards.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PHuhu, I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Randy",
        "#00305F#12P(Huh … … Is not it authentic?\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PA young man with straight eyes\x01",
            "A youth who has secret passion … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAlways standing at the head as a centripetal force,\x01",
            "I encourage my friends with that cheerfulness\x01",
            "Encouraging colleagues who have led me …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_6191")
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#5POh … and yet,\x01",
            "By falling into something extreme condition\x01",
            "It seems that it was deepened deeply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PFrom now on, deepen mutual understanding,\x01",
            "By going higher\x01",
            "A hard bond will be formed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6226")

    label("loc_6191")


    ChrTalk(
        0x16,
        (
            "#5PBorn differently,\x01",
            "Acknowledge each other's advantages\x01",
            "Supplementary relationship …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PFrom now on, deepen mutual understanding,\x01",
            "By going higher\x01",
            "A firm bond will be formed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6226")

    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5PWell that's what I'm able to see\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00305F#12PHuh … what the hell?\x01",
            "Is not it a holy result?\x02\x03",
            "#00304FMiss, Tio Suke,\x01",
            "And Noel … bad.\x02\x03",
            "#00302FApparently Lloyd said\x01",
            "It seems to be becoming my thing.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00006F#6P…… Disturbing things\x01",
            "Stop killing me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PWell, that's going to be on that far\x01",
            "I did not mention the suggestion for now.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        (
            "#5PHowever, what is fate is\x01",
            "If you strongly desire\x01",
            "Changing things ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIn the future anything like that\x01",
            "When asked whether it is possible,\x01",
            "I can not deny either.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PAh, that, if you can\x01",
            "I want you to deny.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00309F#12PHahaha, do not you shy, shy.\x02\x03",
            "#00304FIf you want it,\x01",
            "As an anki that I can rely on as well ─\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00011F#6PIt is not a shame or something! It is!\x02\x03",
            "#00006FHaa, please forgive me …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C86")

    label("loc_6566")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PRandy,\x01",
            "Is there anything I want to divine?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00305F#12PCan I decide?\x02\x03",
            "#00303FI see …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00309F#12PHmm, if it was ……\x01",
            "Even in my future Nampa luck\x01",
            "Is it a squirrel?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006F#6PWell, is that okay …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIn brief, you call out\x01",
            "The possibility that a strange woman may take an invitation ……\x01",
            "Is that okay with that?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Randy",
        "#00309F#12PSo thank you for asking!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PHehe, I cheap.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Randy",
        "#00305F#12P(Huh … … Is not it authentic?\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5P…… with your Nanpa ……\x01",
            "The possibility of success is roughly,\x01",
            "I told you to divide it by piece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHaving brightness and neat facial features\x01",
            "There are many women who feel attractive … …\x01",
            "There are many things to be wary of again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PBy the way even if you succeed\x01",
            "In the case of you, the proportion to the true love is\x01",
            "It can be said that it is almost zero.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    NpcTalk(
        0x15,
        "Randy",
        "#00306F#12P#4SKern! It is!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5PWell that's what I'm able to see\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00306F#12PB, Lloyd …\x01",
            "I can not do it anymore ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00012F#6PWell, alright …\x01",
            "Do not be discouraged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHehe, that's right.\x01",
            "If you give advice ……\x01",
            "Do not miss love in familiar places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PVery close to you, you\x01",
            "There is a opposite sexual thinking … ….\x01",
            "There was such an implication.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    NpcTalk(
        0x15,
        "Randy",
        "#00305F#12PMa, Magisu! Is it?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould it be … …\x01",
            "The Mill of the Guard -\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00303F#12P── Okay! If we decide so … …\x02\x03",
            "#00309FI guess you care about me\x01",
            "Until Kawaiko is found,\x01",
            "I only have to work hard on a village!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        "#00006F#6PWhy is it so ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P(… … I do not notice it, I wonder, I wonder.\x01",
            "Hehe, I have nothing to do with it. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C86")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_27_5D03 end

    def Function_28_6C92(): pass

    label("Function_28_6C92")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat does it take up to?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Two people compatibility\x01",      # 0
            "Leave it to Noel\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_747D")

    ChrTalk(
        0x101,
        (
            "#00000F#6POur compatibility\x01",
            "Could you please fortune?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, of course\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Noel",
        "#10105F#12PRo, Mr. Lloyd! Is it?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PWell, it's a good idea.\x01",
            "I am wondering if you should try it.\x02\x03",
            "#00000FWe can quite if it's no good\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noel",
        (
            "#10111F#12PNo! It is!\x01",
            "It is a nuisance or something like that\x01",
            "I do not have it … ….\x02\x03",
            "#10116F(Or, it's also natural\x01",
            "I wonder what he is saying … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PEr, what's wrong?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Noel",
        (
            "#10106F#12PNothing, nothing.\x02\x03",
            "#10100F… Well then, then,\x01",
            "Thank you fortune teller.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PHuhu, let's hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Noel",
        "#10105F#12P(Wow … what kind of technique …?\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PA young man with straight eyes\x01",
            "A daughter secretly honored with honest will … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PDifferent affiliation, to protect something\x01",
            "While cooperating for the same purpose,\x01",
            "Relations that have built strong trust ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PEither step one step\x01",
            "If you enter the deep part,\x01",
            "You can be more intimate.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5PWell that's what I'm able to see\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noel",
        (
            "#10105F#12PTake one step … ….?\x01",
            "It's pretty weak, is not it?\x02\x03",
            "#10106FI wonder if I draw a line … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHuhu, what I saw\x01",
            "You seem to be a cautious type\x01",
            "I think that it can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PSomewhat should be aggressive\x01",
            "Even what is available\x01",
            "Are not you missing out?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noel",
        (
            "#10103F#12PWell, that fish is certainly\x01",
            "There might be, but ……\x02\x03",
            "#10101F… But, that's right.\x01",
            "When I'm in an emergency\x01",
            "I will give courage ……!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PEr, Er, Noel?\x01",
            "I am a bit too serious … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Noel",
        (
            "#10105F#12PHa ha\x02\x03",
            "#10106FThat's right, is not it?\x01",
            "I tried it anyway … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Noel",
        (
            "#10105F#12P…… No!\x01",
            "Separately I am sorry,\x01",
            "It's not like that … !.!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PWell, I know.\x01",
            "Calm down slightly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P(Hehe, I look like a surprisingly good combination.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AD3")

    label("loc_747D")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PNoel,\x01",
            "Is there anything I want to divine?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Noel",
        (
            "#10105F#12PCan I decide?\x02\x03",
            "#10103FWell, that's right …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Noel",
        (
            "#10100F#12PWell then,\x01",
            "The future of the guard …\x01",
            "What is it like?\x02\x03",
            "#10104FI will either return to the guard,\x01",
            "Mind attitude at the time of that\x01",
            "Do you want to keep it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00002F#6POh, is not it good?\x02\x03",
            "#00000FWell then, then\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, of course\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Noel",
        "#10105F#12P(Wow … what kind of technique …?\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        "#5P…… This is an indication of change.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PBefore long,\x01",
            "The organization to which you belong is\x01",
            "Make some change …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAt that time, you make a big decision\x01",
            "You will be pressed … …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5PWell that's what I'm able to see\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noel",
        (
            "#10103F#12PChange … … is it a decision?\x02\x03",
            "#10101FWell, what exactly is that …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PSorry, but at the moment\x01",
            "I can not see it clearly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PBetter or bad, depending on future trends\x01",
            "You said that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PWell, it is certainly the point in time\x01",
            "It seems I can say anything.\x02\x03",
            "#00000FDepending on the outcome of independence advocacy,\x01",
            "The way the guard is\x01",
            "It seems to change.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noel",
        (
            "#10100F#12PFor the guard\x01",
            "Evolution or decline … …\x02\x03",
            "#10103FHopefully, that's evolution\x01",
            "I would like it to be ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5POne thing I can say is … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PEven afterwards,\x01",
            "To make a decision not to regret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PFortunetelling is just fortune telling ……\x01",
            "One way you decide,\x01",
            "Because as the future will change.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noel",
        (
            "#10100F#12PYeah, you are right……\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AD3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_28_6C92 end

    def Function_29_7ADF(): pass

    label("Function_29_7ADF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat does it take up to?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Two people compatibility\x01",      # 0
            "Leave it to Waji\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8179")

    ChrTalk(
        0x101,
        (
            "#00000F#6POur compatibility\x01",
            "Could you please fortune?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, of course\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Waji",
        (
            "#10302F#12PIt is unusual, is not it?\x01",
            "Approach from you\x01",
            "I will not call you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00003F#6PNo,\x01",
            "It's not like that.\x02\x03",
            "#00000FI came to such a place,\x01",
            "I am wondering if you should try it.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Waji",
        "#10309F#12PHuh, I do not need to be shy.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#00006F#6P…… Anyway, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHuhu, that would be nice.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x16)

    ChrTalk(
        0x16,
        "#5P(……I see……)\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Waji",
        (
            "#10309F#12PHuh, what's wrong?\x01",
            "A fortune-teller's older sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P…… Hehe, it's nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PA young man with straight eyes\x01",
            "A boy who is lightly walking around the world ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PWhile being the opposite personality\x01",
            "By acknowledging each other's excellent points,\x01",
            "I have built a solid faith … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PTrust has grown, past and present as well\x01",
            "If you can accept and include it,\x01",
            "A firm bond will be formed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5PWell that's what I'm able to see\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PIncluding past and present …\x02\x03",
            "#00003F…… Certainly from Wadi,\x01",
            "I heard the story of so long ago\x01",
            "Was not there.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Waji",
        (
            "#10309F#12PHuh, huh?\x01",
            "Even this everything\x01",
            "I'm talking about it all over.\x02\x03",
            "#10304FBesides, there are some secrets\x01",
            "Do not you think it will burn a lot?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6PAfter all, secretly\x01",
            "I guess you are … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHehuu, well patronizing well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThis type of hand,\x01",
            "Because I do not show real intention.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Waji",
        (
            "#10304F#12PHuh, it was.\x02\x03",
            "#10309FBy all means persistently approach\x01",
            "I will be glad if you call him.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        "#00006F#6PWhew ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8653")

    label("loc_8179")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PWadi\x01",
            "Is there anything I want to divine?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Waji",
        (
            "#10305F#12POh, can I decide?\x02\x03",
            "#10304FYeah……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Waji",
        (
            "#10300F#12PIf it's the case\x01",
            "How about such a thing?\x02\x03",
            "#10304FIn this place, what I want is\x01",
            "Whether it is available ……\x01",
            "I want you to divorce it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PWhat wishes want … ….?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Waji",
        (
            "#10304F#12PHuh, that is a secret.\x02\x03",
            "#10300FHow about you, sister.\x01",
            "Is it possible for such fortune telling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHehe, it is funny.\x01",
            "……let's do it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x16)

    ChrTalk(
        0x16,
        "#5P(……I see……)\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Waji",
        (
            "#10309F#12PHuh, what's wrong?\x01",
            "A fortune-teller's older sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P…… Hehe, it's nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PThings you look for ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAlthough it is in the immediate vicinity,\x01",
            "Never reach it now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PNow we should just wait for the hour ……\x01",
            "That kind of suggestion comes out.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5PWell that's what I'm able to see\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Waji",
        (
            "#10304F#12P……I see.\x01",
            "It is enough to know only that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00006F#6PWhat is something,\x01",
            "I do not understand at all …\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Waji",
        (
            "#10300F#12PHuh, now it is OK.\x02\x03",
            "#10304FBesides, there are some secrets\x01",
            "Do not you think it will burn a lot?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PHaa, exactly ….\x02",
    )

    CloseMessageWindow()

    label("loc_8653")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_29_7ADF end

    def Function_30_865F(): pass

    label("Function_30_865F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat does it take up to?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Two people compatibility\x01",      # 0
            "Leave it to Ka'aa\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CF0")

    ChrTalk(
        0x101,
        (
            "#00000F#6POur compatibility\x01",
            "Could you please fortune?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, of course\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Keya",
        (
            "#01110F#12PLloyd, \"compatibility\" is said\x01",
            "Is not it suitable for you?\x02\x03",
            "#01109FKia, with Lloyd\x01",
            "I hope it matches well.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PHaha, that's right.\x01",
            "I am glad that so.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00000F#6P… Well then, then,\x01",
            "Please fortune teller.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHuhu, I know.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Keya",
        "#01110F#12P(Wow, somehow Kire … …)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PA young man with straight eyes\x01",
            "A girl who brings light with that smile ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHer existence gives you courage,\x01",
            "You say you guard her\x01",
            "We will tie together with a strong will …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAs long as you guard her,\x01",
            "Never bonds can be solved.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5PWell that's what I'm able to see\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    NpcTalk(
        0x15,
        "Keya",
        (
            "#01106F#12P…… Keya,\x01",
            "It might be a bit disappointing.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00005F#6PWell, why?\x01",
            "You got good results.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Keya",
        (
            "#01108F#12PHmm … it's so,\x01",
            "It is a bit different.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#5P…… Hehe, little lady.\x01",
            "Because this fortune telling is not everything,\x01",
            "There is nothing to lament for.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        (
            "#5PBesides, now like chicks and parent birds\x01",
            "Even if it's a relationship …\x01",
            "Chicks grow big anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAnd … the parent birds will notice.\x01",
            "Just like my children flap\x01",
            "That is to say.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Keya",
        (
            "#01105F#12P……Is that so.\x01",
            "Yeah, that's right.\x02\x03",
            "#01109FWell, Kaoru …\x01",
            "I will finally become an adult!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PWell, I do not know well … ….\x01",
            "I wish I was fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9415")

    label("loc_8CF0")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PKeya,\x01",
            "Is there anything you would like to try out?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Keya",
        (
            "#01105F#12PKaea can decide?\x02\x03",
            "#01111FWell then, then …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Keya",
        (
            "#01110F#12POh, that's right!\x01",
            "With Kea, Zeit\x01",
            "I'd like to divorce your compatibility!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x16,
        "#5PZeit …?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00012F#6PEr, um … ….\x01",
            "I live together in our workplace,\x01",
            "Animals … but what is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        "#5PHehuu, I see. ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5POkay, my daughter.\x01",
            "With that Zeito\x01",
            "Bring it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PEven soon I will occupy it.\x01",
            "Let's give it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6PWhat! Is it?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Keya",
        (
            "#01110F#12PHonto ー! Is it?\x02\x03",
            "#01109FWell then, I will bring you! It is!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 1500, 0, 101500, 270)
    OP_0D()
    OP_93(0x15, 0xB4, 0x1F4)
    OP_63(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)

    def lambda_8FD1():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8FD1)
    WaitChrThread(0x15, 1)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PWell, sorry.\x01",
            "To some extent hesitantly … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHehe, you said.\x01",
            "It seems interesting for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P(This person has changed quite a bit … …)\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 630, 50, 101950, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0x27)
    SetChrSubChip(0x17, 0x0)
    BeginChrThread(0x17, 0, 0, 0)
    SetChrPos(0x17, 2000, 0, 101000, 315)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x17,
        "#01200F#12PGuru …… Won.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHuhu, then …………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Keya",
        "#01110F#12P(Wow, somehow Kire … …)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PWith a girl who brings light with that smile,\x01",
            "A wolf who watches over his friends and is proud … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PWe communicate feelings to you,\x01",
            "You can see bonds that can respect each other …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PNo matter what in the future,\x01",
            "The wolf will keep watching you strongly.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5PWell that's what I'm able to see\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x2)

    NpcTalk(
        0x15,
        "Keya",
        (
            "#01100F#12PZeit, from now on\x01",
            "You seem to be with me!\x02\x03",
            "#01109FEh, are you happy also with Zeit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#01203F#12PGuru …… Won.\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha … Thank you.\x01",
            "Even though I did a bad request … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHuhu, I made fortunetelling fortunetelling\x01",
            "I also had a good experience.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9415")

    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5P(in addition……\x01",
            "Interesting suggestions could also be seen. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P(Woman God only knows what will happen from now,\x01",
            "I wonder if they are. )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PFortune-teller … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHehe … … nothing.\x01",
            "Coming again ……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_30_865F end

    def Function_31_9528(): pass

    label("Function_31_9528")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat does it take up to?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Two people compatibility\x01",      # 0
            "Leave it to Fran\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BEE")

    ChrTalk(
        0x101,
        (
            "#00000F#6POur compatibility\x01",
            "Could you please fortune?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, of course\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Franc",
        (
            "#06405F#12PHuh, Mr. Lloyd!\x01",
            "Compatibility with me,\x01",
            "Are you interested ~! Is it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00002F#6PWell, it's a good opportunity\x01",
            "Let's try it\x01",
            "I thought that … ….\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Franc",
        (
            "#06409F#12PHuh, that is right!\x01",
            "Dear Friends, Best regards\x01",
            "Please~!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PHuhu, I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Franc",
        (
            "#06405F#12P(Wow ~ ….\x01",
            "It is kind of amazing. )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PA young man with straight eyes\x01",
            "A girl who supports them from behind … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PEvery time I work together\x01",
            "A strong relationship of trust is formed,\x01",
            "The bonds were tied …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#5POh, but … ….\x01",
            "She seems to have a feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAs long as that feeling does not change,\x01",
            "To become such a relationship\x01",
            "It will not be first.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5PWell that's what I'm able to see\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Franc",
        (
            "#06409F#12POh … … It is Don Pissha!\x01",
            "Truly, it is a fun rumor to ask rumors!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHehe, you are welcome.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PSomehow\x01",
            "I imagined it though.\x02\x03",
            "#00000FEr, Fran.\x01",
            "I will ask you for reference,\x01",
            "Your mentor is … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    NpcTalk(
        0x15,
        "Franc",
        "#06409F#12P#4SIt is Onishi, Onee! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PWell, it is as you imagined.\x02\x03",
            "#00000FAfter all, to franc\x01",
            "That kind of story comes out\x01",
            "It is still ahead of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHuhu, but if you think in reverse …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf you can become more than her older sister\x01",
            "Is not there a possibility?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Franc",
        (
            "#06409F#12PThat's right~,\x01",
            "Let's do our best, Mr. Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PNo, I wish you good luck\x01",
            "Even if it is said ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2AF")

    label("loc_9BEE")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PFranc,\x01",
            "Is there anything I want to divine?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Franc",
        (
            "#06405F#12POh, let me decide\x01",
            "Can you get it?\x02\x03",
            "#06404FYes, that's right~……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Franc",
        (
            "#06405F#12POh, remember that …!!\x02\x03",
            "#06401FFortune-teller, Bang Bang place\x01",
            "Will you find out! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PBang bang …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PThat's why I take care of Fran\x01",
            "Was not it a stuffed animal …?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Franc",
        (
            "#06400F#12PWell, actually this Michelam too\x01",
            "I was thinking of bringing in … ….\x02\x03",
            "#06406FWhen my mom cleaned the room the other day\x01",
            "She seemed to have gone somewhere,\x01",
            "After all I could not bring ~!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00006F#6PI see, I see … ….\x02\x03",
            "#00000FWell, could you please?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x16,
        "#5PHehe, I cheap.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Franc",
        (
            "#06405F#12P(Wow ~ ….\x01",
            "It is kind of amazing. )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PLost stuffed animal ……\x01",
            "I wonder if a bear's stuffed animal?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Franc",
        (
            "#06405F#12PThat's right! It is!\x01",
            "Do you understand ~! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHehuu, it is distinctive, so I immediately understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PYour stuffed animal is now ……\x01",
            "I am rolling in the shade under the bed …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    NpcTalk(
        0x15,
        "Franc",
        (
            "#06403F#12PBa, are you under the bed?\x01",
            "It is strange, I am also there\x01",
            "I've been looking for … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PProbably because it is a place that I think immediately\x01",
            "On the contrary it probably was missed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PIf you search well, you will definitely find it.\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Franc",
        "#06409F#12POh, thank you!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        "#00000F#6PHaha, good franc.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Franc",
        (
            "#06406F#12PYes, it is true!\x01",
            "Without Bang Bang,\x01",
            "I am truly getting lonesome.\x02\x03",
            "#06409FI will search for it when I return to tomorrow ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHuhuu, thank you for your help.\x02",
    )

    CloseMessageWindow()

    label("loc_A2AF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_31_9528 end

    def Function_32_A2BB(): pass

    label("Function_32_A2BB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat does it take up to?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Two people compatibility\x01",      # 0
            "Leave it to Cecil\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9D9")

    ChrTalk(
        0x101,
        (
            "#00000F#6POur compatibility\x01",
            "Could you please fortune?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, of course\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05900F#12PWell, Lloyd ……\x02\x03",
            "#05909FHehe, such a thing\x01",
            "Even without bothering to bother,\x01",
            "Surely the compatibility is perfect.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PWell, it's a good opportunity\x01",
            "Let's try it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00000F#6P……so,\x01",
            "Thank you for your consideration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, I understand.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05905F#12P(Oh……\x01",
            "It sounds really amazing. )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PA young man with straight eyes\x01",
            "A woman overflowing with spirit of compassion ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PMy feelings were nurtured since I was young,\x01",
            "There is a bondless tie … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5P…… But for women\x01",
            "There is a certain feeling left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PTo the lost feelings,\x01",
            "A strong feeling ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5PWell that's what I'm able to see\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x15)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05904F#12P… … Huhu, this is perfect\x01",
            "I can not accept it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00006F#6P…… Sorry, Cecil elder sister.\x01",
            "I was asked to take over such a thing.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05900F#12POh, I will not apologize.\x01",
            "What seems to be good compatibility with Lloyd\x01",
            "I am happy to be obedient … …\x02\x03",
            "#05904FBesides, I will tell you about Mr. Guy\x01",
            "You can remember what you have forgotten\x01",
            "I'm glad you could check it again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P…… The feelings for those who love me,\x01",
            "No matter what happens\x01",
            "I will live forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAnd, as it is there\x01",
            "There are you now … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05905F#12P…… Fortune-ta, maybe\x01",
            "Are you also an important person …?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        "#5P… … You seem to be talking too much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI like a fortune-teller like me\x01",
            "I did not mean to speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PNo, thankful words.\x01",
            "I will bear in mind the liver.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHehe … … You are welcome.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0E5")

    label("loc_A9D9")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PCecil elder sister,\x01",
            "Is there anything I want to divine?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05905F#12PWell, I wonder if I can decide?\x02\x03",
            "#05904FHuhu, well … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05909F#12PWell then … … Lloyd in the future,\x01",
            "What kind of bride will you receive?\x01",
            "I wonder if you will fortake me fortune.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x101,
        "#00011F#6P#4SOh.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#6PWait a minute, Cecil elder sister …?\x01",
            "I am ashamedly too embarrassed ….\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05909F#12POh my goodness.\x01",
            "Because my older sister wants to know.\x02\x03",
            "#05900FHehe, thank you for your consideration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHehe, I cheap.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05900F#12P(Oh……\x01",
            "It sounds really amazing. )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PTo a young man with straight eyes,\x01",
            "A woman to accomplish, that … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P…\x01",
            "…\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x15, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05905F#12POh……\x01",
            "What's wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI'm sorry but ….\x01",
            "I can not say anything at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PWhat……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI've had some kind of fortune-telling\x01",
            "Although I have been asked … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThere are a lot of women who will be possible,\x01",
            "Sometimes I could not narrow down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PIn your case it is exactly that.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05909F#12PWell … is that so?\x01",
            "Indeed I was out of calculations.\x02\x03",
            "#05908FLloyd is my bragging brother,\x01",
            "The fact that girls do not leave\x01",
            "I thought that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P(Nah, somehow I am\x01",
            "Like an amazing squatting pear\x01",
            "I feel like being told … …)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05903F#12P…… That, Lloyd?\x01",
            "Onee-san, a little worried\x01",
            "It is becoming ……\x02\x03",
            "#05901FSomeday I will have a girl\x01",
            "Something that makes me sad,\x01",
            "Do not let it go.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        "#00012F#6PI will not do it!\x02",
    )

    CloseMessageWindow()

    label("loc_B0E5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_32_A2BB end

    def Function_33_B0F1(): pass

    label("Function_33_B0F1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat does it take up to?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Two people compatibility\x01",      # 0
            "Leave it to Iya\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B68C")

    ChrTalk(
        0x101,
        (
            "#00000F#6POur compatibility\x01",
            "Could you please fortune?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, of course\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6P…… without permission\x01",
            "I decided it,\x01",
            "Was everything okay?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Ilia",
        (
            "#01709F#12PHaha, it looks interesting.\x01",
            "Let's do it ☆\x02\x03",
            "#01704FIt's bad for Huhu, Cecil,\x01",
            "When good results come out, my younger brother\x01",
            "I gotta get it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00012F#6PWell, well,\x01",
            "By doing it for the time being.\x02\x03",
            "#00000FWell then, please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, I understand.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Ilia",
        "#01705F#12P(Well … it is not authentic.\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PA young man with straight eyes\x01",
            "Dancing princess who burns passion on the stage ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PMy wonderful feelings for her goals\x01",
            "Attract and attract others … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf you stick to those who support you,\x01",
            "The possibility of becoming a deeper relationship is\x01",
            "There will be enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHowever……\x01",
            "Her important thing is the stage.\x01",
            "It should be hard to be any further.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5PWell that's what I'm able to see\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PAfter all, Iria\x01",
            "The stage is the best thing.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Ilia",
        (
            "#01700F#12PHuh, it looks like that.\x02\x03",
            "#01709FAnyway, fortuneteller.\x01",
            "Honestly fortune-telling\x01",
            "I did not think it would show off.\x02\x03",
            "#01700FTechnique to be acquired in a little overnight\x01",
            "I do not think so ….\x01",
            "Where did you practice?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jump("loc_BEC3")

    label("loc_B68C")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PMr. Ilya,\x01",
            "Is there anything I want to divorce?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Ilia",
        (
            "#01705F#12POh my good decision?\x02\x03",
            "#01703FWell, well … hey ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Ilia",
        (
            "#01709F#12PWell, Lisha and Sri\x01",
            "Whether you will overtake me in the future!\x01",
            "What about ……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PThose two … …\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Ilia",
        (
            "#01704F#12PWell, honestly, such a thing\x01",
            "It seems like fortune telling\x01",
            "It may not exist, but …\x02\x03",
            "#01702FMy eyes are wrong\x01",
            "It also means to check it again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThe future of your disciple …\x01",
            "Should I occupy that?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Ilia",
        (
            "#01700F#12PWell, I wonder why.\x01",
            "Can you tell me?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PHehe, I cheap.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Ilia",
        "#01705F#12P(Well … it is not authentic.\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PMaihime who burns passion on the stage found out\x01",
            "Two young dancers …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI have an unfamiliar talent,\x01",
            "For each of us\x01",
            "You seem to have trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHow to get over it … …\x01",
            "The key to the future is there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5PWell that's what I'm able to see\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    NpcTalk(
        0x15,
        "Ilia",
        "#01703F#12PLisa and Shri's troubles, or …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PMr. Iria, do you think?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    NpcTalk(
        0x15,
        "Ilia",
        (
            "#01703F#12PEach of these children,\x01",
            "I am having something to worry about\x01",
            "I was aware, but ….\x02\x03",
            "#01700FTo be honest, content\x01",
            "I have not heard it in detail.\x02\x03",
            "#01704F…… But well, everyone has trouble\x01",
            "You have more or less.\x02\x03",
            "Each person may be able to overcome … …\x01",
            "It is not my taste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PIs not it harsh … …\x01",
            "In a sense it seems to be Iria-san.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Ilia",
        (
            "#01700F#12PWell, I am\x01",
            "That they can get over\x01",
            "I believe it, though.\x02\x03",
            "#01703FSurely, when I get over it\x01",
            "My best rival is\x01",
            "It is the moment of being born.\x02\x03",
            "#01709FWell, something\x01",
            "I've been throbbing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIts prospective look … …\x01",
            "It seems like a kind of talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHehe, I feel a little envious.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Ilia",
        (
            "#01702F#12PHuh, you are welcome.\x02\x03",
            "#01709FAnyway, fortuneteller.\x01",
            "Honestly fortune-telling\x01",
            "I did not think it would show off.\x02\x03",
            "#01700FTechnique to be acquired in a little overnight\x01",
            "I do not think so ….\x01",
            "Where did you practice?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    label("loc_BEC3")


    ChrTalk(
        0x16,
        (
            "#5P…… In the past, in a trip of a certain journey\x01",
            "Please do show off various arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIt has become possible to do with its application,\x01",
            "Maybe just tell me.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Ilia",
        (
            "#01705F#12POne point …\x01",
            "What is called a circus.\x02\x03",
            "#01709FWell, you\x01",
            "Where you are active\x01",
            "I wanted to see it once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PIs not it true?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P… … Huhu, you are welcome.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_33_B0F1 end

    def Function_34_C01A(): pass

    label("Function_34_C01A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat does it take up to?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Two people compatibility\x01",      # 0
            "Leave it to Leisha\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C81E")

    ChrTalk(
        0x101,
        (
            "#00000F#6POur compatibility\x01",
            "Could you please fortune?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, of course\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Lisha",
        "#01805F#12PL-lloyd?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PHaha, in a place like this\x01",
            "I came and I thought it would be a test.\x02\x03",
            "#00000FWe can quite if it's no good\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Lisha",
        (
            "#01804F#12PAha, no\x02\x03",
            "#01802FWell, it's a pity\x01",
            "Let me ask you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PEh, well then\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Lisha",
        "#01801F#12P(This is…)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PA young man with straight eyes\x01",
            "A girl whose grief tears her eyes … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PPreviously, I was involved in an incident\x01",
            "A reliable trust is growing for two people … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf you foster this feeling,\x01",
            "The possibility of becoming a deeper relationship is\x01",
            "There will be enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHowever … for that,\x01",
            "The darkness on her heart,\x01",
            "I need to get rid of … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5PWell that's what I'm able to see\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PThe darkness hidden in Rixia's heart?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PI don't know what it is\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PSuch implication is given to this crystal ball\x01",
            "Because it is just reading.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Lisha",
        (
            "#01802F#12PWell, that.\x01",
            "Probably, this time the renewal performance\x01",
            "I think I'm worried.\x02\x03",
            "#01809FOn a sunny stage of Shri's\x01",
            "Is it possible to dance properly …?\x01",
            "Recently I was a bit uneasy.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6POh so that's it\x02\x03",
            "#00003FBut, Lisa has been doing it for quite some time\x01",
            "It seems that he is practicing very hard,\x01",
            "Surely it will be fine.\x02\x03",
            "#00009FIn a performance I had you see before\x01",
            "I was impressed, too ……\x01",
            "There is nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Lisha",
        "#01805F#12P….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PEhe, you're quite good\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        (
            "#5PIt will be practical to promptly give advice\x01",
            "Although it is exhausted as a fortune tellinger.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PHuh\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#6PNo that's not it Rixia!\x02\x03",
            "That kind of spirit\x01",
            "There was that … ….\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Lisha",
        (
            "#01809F#12PEhe, I know\x02\x03",
            "#01802FThank you Lloyd\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF0B")

    label("loc_C81E")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PLisha,\x01",
            "Is there anything I want to divine?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Lisha",
        (
            "#01805F#12PWell, even if I decide\x01",
            "Is that ok?\x02\x03",
            "#01803FThat's right.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Lisha",
        (
            "#01803F#12PIn the meantime, I met him on the matter of finding a kitten\x01",
            "I am Shirley, but ……\x02\x03",
            "#01801FDo you have an edge to see her again,\x01",
            "Would you mind for a moment?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PLisha … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, that's about cheap.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Lisha",
        "#01801F#12P(This is…)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        "#5PA girl whose name is Charlie …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIt is said that it looks again with a crossbell\x01",
            "There is an implication.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PWhen is it and what kind of situation is it\x01",
            "I do not know but ….\x01",
            "It will certainly come at that time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5PWell that's what I'm able to see\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Lisha",
        (
            "#01802F#12P……I see,\x01",
            "Thank you very much.\x02\x03",
            "#01803F(\"Blooded#8RBloody#Shirley \"……\x01",
            "After all we have to be careful. )\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6POh, it is somewhat surprising.\x02\x03",
            "At the time of Mary's case\x01",
            "It was a bit involved,\x01",
            "Was that much worrisome?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Lisha",
        (
            "#01802F#12POh, no\x01",
            "What else you want to occupy\x01",
            "Because I could not think of it.\x02\x03",
            "#01804FMoreover, it was a very pretty child\x01",
            "I want to talk if there is opportunity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PWell, hmm … ….\x01",
            "That is a very dangerous child.\x02\x03",
            "#00006FGiven the matter of Eli\x01",
            "It seems dangerous in another sense ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Lisha",
        "#01805F#12P…… Mr. Erie's case?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6POh no.\x01",
            "Because it is nothing.\x02\x03",
            "#00003F(Wait a bit, awesome sight\x01",
            "I imagined … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P…… Hehe, you lady.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf you do not mind, he is here\x01",
            "What was I thinking,\x01",
            "Shall I give it up?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#00012F#6POr please forgive me!\x02",
    )

    CloseMessageWindow()

    label("loc_CF0B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_34_C01A end

    def Function_35_CF17(): pass

    label("Function_35_CF17")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat does it take up to?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Two people compatibility\x01",      # 0
            "Leave it to Sri\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5E4")

    ChrTalk(
        0x101,
        (
            "#00000F#6POur compatibility\x01",
            "Could you please fortune?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, of course\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Shuri",
        (
            "#14011F#12PHey, hey …\x01",
            "What are you thinking, you do! Is it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00005F#6PHuh\x01",
            "Well, is that enough to panic?\x02\x03",
            "#00009FIt is rare to have you and two people,\x01",
            "Would you be able to deepen your friendship with this machine,\x01",
            "I thought about being fortune-telling.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Shuri",
        (
            "#14006F#12P(… … that,\x01",
            "Saying towards the face, normal! Is it? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHuhu, what should I do?\x01",
            "I do not care anything.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Shuri",
        (
            "#14000F#12P…… ah, now it's okay with that.\x01",
            "Please fortune-telling me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PWell, then ………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Shuri",
        "#14005F#12P(…, what, what …?\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PA young man with straight eyes\x01",
            "A girl who has the potential to shine … …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D338")

    ChrTalk(
        0x16,
        (
            "#5PAlthough the encounter was the worst,\x01",
            "You, on his kindness\x01",
            "You seem to be aware.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D376")

    label("loc_D338")


    ChrTalk(
        0x16,
        (
            "#5PYou come overflowing from him\x01",
            "You seem to be aware of kindness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D376")


    ChrTalk(
        0x16,
        (
            "#5POver time, to you\x01",
            "If a straightforward heart began to bud,\x01",
            "I can become like brother and sister ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5PWell that's what I'm able to see\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Shuri",
        (
            "#14011F#12PWhat, な な な な り ……\x01",
            "What is this fortune telling!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PHaha, indeed\x01",
            "I might be shy.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Shuri",
        (
            "#14006F#12P\"Be a little shy\",\x01",
            "It's nothing like that!\x02\x03",
            "#14012FWhy and you\x01",
            "To be like a brother and sister …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHuh … … Even now enough\x01",
            "They seem to be on good terms.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Shuri",
        "#14011F#12PIf it is not good!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6P(Hey, it is not frank.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DE1C")

    label("loc_D5E4")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PShuri\x01",
            "Is there anything I want to divine?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Shuri",
        (
            "#14005F#12PWell, may I decide?\x02\x03",
            "#14003FWell …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Shuri",
        (
            "#14003F#12PWell then, I will ask ….\x02\x03",
            "#14000FI will be with Alcane shell in the future\x01",
            "Can I do it properly …?\x01",
            "Will you occupy it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PShuri …?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Shuri",
        (
            "#14008F#12P…… Because it is,\x01",
            "If this gives a good result …\x02\x03",
            "#14008FSurely already, such a slum\x01",
            "You do not have to go back, do you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P…… Okay, I'll occupy you.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5P…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Shuri",
        "#14005F#12P(…, what, what …?\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5P…… The way you go,\x01",
            "Indeed branched in various directions\x01",
            "You seem to be doing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PWhether you can keep chasing your dream this way,\x01",
            "Or in frustrated and origin\x01",
            "Are they going back …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PFate still still got it\x01",
            "I have not decided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAt the moment, from my mouth\x01",
            "You can not say that it is absolutely fine.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P…… It looked like this to me.\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    NpcTalk(
        0x15,
        "Shuri",
        (
            "#14003F#12P……I see……\x02\x03",
            "#14008FHere \"You can do absolutely\"\x01",
            "If you say it,\x01",
            "I was relieved a bit though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PShuri …\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5P…… To my acquaintance,\x01",
            "There was a girl from slum.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Shuri",
        "#14005F#12PHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAs soon as we met,\x01",
            "That child despaired everything\x01",
            "I was expressing though ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PWhile living together for a long time,\x01",
            "I became a bright and strong child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThen, met a respectable leader,\x01",
            "Now he is active as a top fighter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIt is that she has grown up … …\x01",
            "There was no doubt \"encounter with people\".\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Shuri",
        "#14005F#12PAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIn the above suggestion,\x01",
            "To you who you can respect already\x01",
            "Are not we meeting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThen, it depends on you … …\x01",
            "I think so.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Shuri",
        (
            "#14000F#12P… … depending on my … …?\x02\x03",
            "#14003F… … That's right.\x01",
            "I like that hurried man\x01",
            "I do not know if it can be strong … …\x02\x03",
            "#14002FAnyway, I'll do my best now.\x01",
            "……Thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHehe … … You are welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6P(Hell …… I guess it was okay to invite me.\x02",
    )

    CloseMessageWindow()

    label("loc_DE1C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_35_CF17 end

    def Function_36_DE28(): pass

    label("Function_36_DE28")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-7780, -1100, 4820, 0)
    MoveCamera(306, 31, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18050, 0)
    SetChrPos(0x101, -3580, 0, 2100, 270)
    SetChrPos(0xEF, -3200, 0, 3370, 270)
    OP_4B(0x18, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00000FGot you!\x02",
    )

    CloseMessageWindow()
    OP_9C(0x18, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    OP_93(0x18, 0x5A, 0x1F4)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Oh you found me!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-5450, -1100, 5050, 0)
    MoveCamera(306, 31, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18050, 0)
    SetChrPos(0x18, -3530, 0, 2710, 90)
    SetChrPos(0x101, -1850, 0, 2040, 270)
    SetChrPos(0xEF, -1850, 0, 3400, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Misashi,\x01",
            "Even the ladies are lucky.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "I am hiding in my place,\x01",
            "To discover two consecutive times,\x01",
            "I saw a reasonable luck.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FI-Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Misashi, but this\x01",
            "Because it is a small miniature.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "So many times no fluke\x01",
            "I will not continue because it ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E099():

        label("loc_E099")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_E099")

    QueueWorkItem2(0x101, 1, lambda_E099)

    def lambda_E0AB():

        label("loc_E0AB")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_E0AB")

    QueueWorkItem2(0xEF, 1, lambda_E0AB)
    SetChrFlags(0x18, 0x1000)
    OP_95(0x18, -3310, 0, 340, 5000, 0x0)
    OP_95(0x18, -240, 0, -2920, 5000, 0x0)

    def lambda_E0EA():
        OP_95(0xFE, -80, 0, -8710, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_E0EA)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    OP_68(310, 1200, -870, 0)
    MoveCamera(323, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14850, 0)
    SetChrPos(0x101, -780, 0, 180, 180)
    SetChrPos(0xEF, 850, 0, 160, 180)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_E1CE")

    ChrTalk(
        0x102,
        (
            "#00105F… … I have gone.\x02\x03",
            "#00104FMore than I thought\x01",
            "It was a pallet but …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E1CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_E22B")

    ChrTalk(
        0x103,
        (
            "#00205FShe's gone\x02\x03",
            "#00204FMore than I thought\x01",
            "It was a palé bare … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E22B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_E284")

    ChrTalk(
        0x104,
        (
            "#00305F…… I went.\x02\x03",
            "#00304FMore than I thought\x01",
            "It was palee but … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_E2E5")

    ChrTalk(
        0x109,
        (
            "#10105F…… I have gone.\x02\x03",
            "#10104FMore than I thought\x01",
            "It was a pallet but …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E2E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_E342")

    ChrTalk(
        0x105,
        (
            "#10304FHuh, I went.\x02\x03",
            "#10302FMore than I thought\x01",
            "It was a pallet but …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_E390")

    ChrTalk(
        0x153,
        (
            "#01105FI went.\x02\x03",
            "#01102FIt was kind of a pale.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_E3F1")

    ChrTalk(
        0x156,
        (
            "#06405F… … I went to see ~.\x02\x03",
            "#06404FMore than I thought\x01",
            "It was a pale bare but ~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E3F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_E44A")

    ChrTalk(
        0x14C,
        (
            "#05905FI went.\x02\x03",
            "#05904FMore than I thought\x01",
            "It was a pallet but …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E44A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_E4A7")

    ChrTalk(
        0x134,
        (
            "#01705FYou seem to have gone.\x02\x03",
            "#01706FMore than I thought\x01",
            "It was a pallet but …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_E508")

    ChrTalk(
        0x135,
        (
            "#01805F…… I have gone.\x02\x03",
            "#01803FMore than I thought\x01",
            "It was a pallet but …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E555")

    label("loc_E508")


    ChrTalk(
        0x166,
        (
            "#14005F…… I went.\x02\x03",
            "#14006FMore than I thought\x01",
            "It was a pallet but …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_E5E8")

    ChrTalk(
        0x101,
        (
            "#00003FWell, yes.\x01",
            "Hide and seek only\x01",
            "Perhaps he is not good at … ….\x02\x03",
            "#00000FAnyway, in this condition\x01",
            "Let's find more and more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E667")

    label("loc_E5E8")


    ChrTalk(
        0x101,
        (
            "#00003FWell, yes.\x01",
            "Hide and seek only\x01",
            "Perhaps he is not good at … ….\x02\x03",
            "#00000FAnyway, in this condition\x01",
            "Let's find more and more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E667")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x7F, 0x1, 0xB)
    SetScenarioFlags(0x1C9, 3)
    OP_65(0x0, 0x1)
    SetChrFlags(0x18, 0x80)
    SetChrPos(0x0, 130, 0, -70, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_36_DE28 end

    def Function_37_E69C(): pass

    label("Function_37_E69C")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "~ Hall of divination ~\x01",
            "Finance luck to love luck, others\x01",
            "I will forecast your destiny\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_37_E69C end

    def Function_38_E700(): pass

    label("Function_38_E700")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E812")
    EventBegin(0x1)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xF, 0x0, 0)

    ChrTalk(
        0xF,
        "Welcome to the Fortune Teller!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Here, to the teacher of a heavenly fortune-teller\x01",
            "I will be able to tell you a lot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Mika and hide and seek in … …\x01",
            "What I am playing at attractions now\x01",
            "Let's stop it. )\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -70, 0, 4080, 180)
    OP_4C(0xF, 0xFF)
    OP_93(0xF, 0xB4, 0x0)
    EventEnd(0x4)
    Jump("loc_E815")

    label("loc_E812")

    Call(0, 18)

    label("loc_E815")

    Return()

    # Function_38_E700 end

    SaveToFile()

Try(main)
