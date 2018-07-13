from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Elie",                   # 1
        "Tio",                    # 2
        "Noｱl",                  # 3
        "Wazy",                   # 4
        "Fran",                   # 5
        "Rixia",                  # 6
        "Michey",                 # 7
        "Apprentice",             # 8
        "Tourist",                # 9
        "Tourist",                # 10
        "Tourist",                # 11
        "Tourist",                # 12
        "Tourist",                # 13
        "Dummy",                  # 14
        "Fortune Teller",         # 15
        "Zeit",                   # 16
        "Miichie",                # 17
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
        "Function_4_70E",          # 04, 4
        "Function_5_8FD",          # 05, 5
        "Function_6_99D",          # 06, 6
        "Function_7_B41",          # 07, 7
        "Function_8_BFD",          # 08, 8
        "Function_9_D7D",          # 09, 9
        "Function_10_E79",         # 0A, 10
        "Function_11_F98",         # 0B, 11
        "Function_12_10F2",        # 0C, 12
        "Function_13_11D9",        # 0D, 13
        "Function_14_1362",        # 0E, 14
        "Function_15_13BA",        # 0F, 15
        "Function_16_1424",        # 10, 16
        "Function_17_14D4",        # 11, 17
        "Function_18_1688",        # 12, 18
        "Function_19_2055",        # 13, 19
        "Function_20_3053",        # 14, 20
        "Function_21_3107",        # 15, 21
        "Function_22_3FEB",        # 16, 22
        "Function_23_4030",        # 17, 23
        "Function_24_407A",        # 18, 24
        "Function_25_408A",        # 19, 25
        "Function_26_51D6",        # 1A, 26
        "Function_27_6209",        # 1B, 27
        "Function_28_7336",        # 1C, 28
        "Function_29_8272",        # 1D, 29
        "Function_30_8ED6",        # 1E, 30
        "Function_31_9E64",        # 1F, 31
        "Function_32_ACA1",        # 20, 32
        "Function_33_BBC3",        # 21, 33
        "Function_34_CC43",        # 22, 34
        "Function_35_DBFA",        # 23, 35
        "Function_36_EC1E",        # 24, 36
        "Function_37_F4D4",        # 25, 37
        "Function_38_F55C",        # 26, 38
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A4")
    Jump("loc_70A")

    label("loc_5A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BA")
    Jump("loc_70A")

    label("loc_5BA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D0")
    Jump("loc_70A")

    label("loc_5D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E6")
    Jump("loc_70A")

    label("loc_5E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68A")

    ChrTalk(
        0x8,
        (
            "#00100FUhmm, I wonder where I\x01",
            "should spend my last ticket.\x02\x03",
            "#00104FIf possible, I'd like something\x01",
            "that left me a memory...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_70A")

    label("loc_68A")


    ChrTalk(
        0x8,
        (
            "#00100FIf possible, I'd like to use\x01",
            "my last ticket on something\x01",
            "that left me a memory...\x02\x03",
            "#00104FUhhm, what could be good?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70A")

    TalkEnd(0xFE)
    Return()

    # Function_3_58B end

    def Function_4_70E(): pass

    label("Function_4_70E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_727")
    Jump("loc_8F9")

    label("loc_727")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73D")
    Jump("loc_8F9")

    label("loc_73D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_840")

    ChrTalk(
        0x9,
        (
            "#00200FI've been following Michey\x01",
            "since before...\x02\x03",
            "He actually goes around many places,\x01",
            "not only the main attractions.\x02\x03",
            "#00204FIt means he is doing his best to meet\x01",
            "as many fans as possible.\x01",
            "...As expected from Michey.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8CD")

    label("loc_840")


    ChrTalk(
        0x9,
        (
            "#00200FEven so, I couldn't spot "Miichie",\x01",
            "Michey's little sister, yet.\x02\x03",
            "#00204FCould it be that she shows up\x01",
            "only at certain hours...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CD")

    Jump("loc_8F9")

    label("loc_8D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E8")
    Jump("loc_8F9")

    label("loc_8E8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F9")

    label("loc_8F9")

    TalkEnd(0xFE)
    Return()

    # Function_4_70E end

    def Function_5_8FD(): pass

    label("Function_5_8FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_946")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_923")
    Call(0, 16)
    Jump("loc_941")

    label("loc_923")


    ChrTalk(
        0xA,
        "#10106FE-Enough, Fran...\x02",
    )

    CloseMessageWindow()

    label("loc_941")

    Jump("loc_999")

    label("loc_946")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95C")
    Jump("loc_999")

    label("loc_95C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_972")
    Jump("loc_999")

    label("loc_972")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_988")
    Jump("loc_999")

    label("loc_988")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_999")

    label("loc_999")

    TalkEnd(0xFE)
    Return()

    # Function_5_8FD end

    def Function_6_99D(): pass

    label("Function_6_99D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B6")
    Jump("loc_B3D")

    label("loc_9B6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CC")
    Jump("loc_B3D")

    label("loc_9CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E2")
    Jump("loc_B3D")

    label("loc_9E2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC7")

    ChrTalk(
        0xB,
        (
            "#10300FHu hu, this place's sofas\x01",
            "are of fine quality.\x02\x03",
            "#10304FUntil I decide the next place to tour,\x01",
            "I believe I'll rest here as I please.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FHey now...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_B27")

    label("loc_AC7")


    ChrTalk(
        0xB,
        (
            "#10304FHu hu, until I decide the next place to tour,\x01",
            "I believe I'll rest here as I please.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B27")

    Jump("loc_B3D")

    label("loc_B2C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3D")

    label("loc_B3D")

    TalkEnd(0xFE)
    Return()

    # Function_6_99D end

    def Function_7_B41(): pass

    label("Function_7_B41")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B67")
    Call(0, 16)
    Jump("loc_BA1")

    label("loc_B67")


    ChrTalk(
        0xC,
        (
            "#06409FLet's have big sis's fortune\x01",
            "in love divined!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA1")

    Jump("loc_BF9")

    label("loc_BA6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBC")
    Jump("loc_BF9")

    label("loc_BBC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD2")
    Jump("loc_BF9")

    label("loc_BD2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE8")
    Jump("loc_BF9")

    label("loc_BE8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF9")

    label("loc_BF9")

    TalkEnd(0xFE)
    Return()

    # Function_7_B41 end

    def Function_8_BFD(): pass

    label("Function_8_BFD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C16")
    Jump("loc_D79")

    label("loc_C16")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAB")

    ChrTalk(
        0xD,
        (
            "#01805F(A fortune teller of Eastern origin...)\x02\x03",
            "#01803F(It's not that I don't\x01",
            "have any suspect, but...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xD, 0x10)
    Jump("loc_D37")

    label("loc_CAB")


    ChrTalk(
        0xD,
        (
            "#01805FAh...Mr. Lloyd.\x01",
            "H-How long have you been there?\x02\x03",
            "#01809FAhaha...\x01",
            "I was once again impressed by\x01",
            "how amazing the turn waiting is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D37")

    Jump("loc_D79")

    label("loc_D3C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D52")
    Jump("loc_D79")

    label("loc_D52")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D68")
    Jump("loc_D79")

    label("loc_D68")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D79")

    label("loc_D79")

    TalkEnd(0xFE)
    Return()

    # Function_8_BFD end

    def Function_9_D7D(): pass

    label("Function_9_D7D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D96")
    Jump("loc_E75")

    label("loc_D96")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAC")
    Jump("loc_E75")

    label("loc_DAC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E4E")

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "The fortune teller lady of this place\x01",
            "is incredibly capable.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, you can have divined\x01",
            "all kind of things, you know?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E75")

    label("loc_E4E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E64")
    Jump("loc_E75")

    label("loc_E64")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E75")

    label("loc_E75")

    TalkEnd(0xFE)
    Return()

    # Function_9_D7D end

    def Function_10_E79(): pass

    label("Function_10_E79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F94")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Welcome to the "Fortune-telling House"!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Here you can have divined many things\x01",
            "from a remarkable fortune teller!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(I'm playing hide and seek wih Miichie...\x01",
            "I'll refrain from having a good time with\x01",
            "the attractions for now.)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_F97")

    label("loc_F94")

    Call(0, 18)

    label("loc_F97")

    Return()

    # Function_10_E79 end

    def Function_11_F98(): pass

    label("Function_11_F98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_104A")

    ChrTalk(
        0x10,
        (
            "Looking around, there're really\x01",
            "many female customers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I'm glad I came with my girlfriend...\x01",
            "If I were alone, I'd probably be uncomfortable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10EE")

    label("loc_104A")


    ChrTalk(
        0x10,
        (
            "The compatibility reading had a good result\x01",
            "and my girlfriend's mood improved a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If the result had been strange...\x01",
            "It would've probably felt awkward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10EE")

    TalkEnd(0xFE)
    Return()

    # Function_11_F98 end

    def Function_12_10F2(): pass

    label("Function_12_10F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1152")

    ChrTalk(
        0x11,
        (
            "Uhuhu, what could I have divined?\x01",
            "As expected, our compatibility?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11D5")

    label("loc_1152")


    ChrTalk(
        0x11,
        (
            "After having it divined,\x01",
            "it said we are bound by\x01",
            "a thread of fate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Uhuhu uh uh...\x01",
            "My eyes weren't wrong\x01",
            "in choosing him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D5")

    TalkEnd(0xFE)
    Return()

    # Function_12_10F2 end

    def Function_13_11D9(): pass

    label("Function_13_11D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_127E")

    ChrTalk(
        0x12,
        (
            "I came to have divined the\x01",
            "place where I lost my wedding\x01",
            "ring without telling my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "I wonder if my turn isn't coming yet...\x02",
    )

    CloseMessageWindow()
    Jump("loc_135E")

    label("loc_127E")


    ChrTalk(
        0x12,
        (
            "Thinking I had dropped my wedding ring,\x01",
            "I had her divine me the place, but...\x01",
            "Goodness! It was in my pocket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            ""It is hard to see what is under your nose", eh...?\x01",
            "I'm glad I've found it, but\x01",
            "somehow I feel pitiable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_135E")

    TalkEnd(0xFE)
    Return()

    # Function_13_11D9 end

    def Function_14_1362(): pass

    label("Function_14_1362")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B6")

    ChrTalk(
        0x13,
        (
            "I hope I receive a hint about\x01",
            "an amazing encounter...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B6")

    label("loc_13B6")

    TalkEnd(0xFE)
    Return()

    # Function_14_1362 end

    def Function_15_13BA(): pass

    label("Function_15_13BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1420")

    ChrTalk(
        0x14,
        (
            "I couldn't care less about men,\x01",
            "I'll have her read my economic fortune.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1420")

    label("loc_1420")

    TalkEnd(0xFE)
    Return()

    # Function_15_13BA end

    def Function_16_1424(): pass

    label("Function_16_1424")

    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "#06400FBig sis, come on, come on!\x01",
            "Quick, let's get in line.\x02\x03",
            "#06409FAnd let's have your love\x01",
            "fortune read, big sis!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#10111FI-I told you I'm fine!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_16_1424 end

    def Function_17_14D4(): pass

    label("Function_17_14D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1520")
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

    label("loc_1520")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C2")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    Jump("loc_1687")

    label("loc_15C2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15EC")
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E7")
    SetChrFlags(0xD, 0x10)

    label("loc_15E7")

    Jump("loc_1687")

    label("loc_15EC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_160C")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_1687")

    label("loc_160C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1667")
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1647")
    SetChrFlags(0xB, 0x80)

    label("loc_1647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1662")
    ClearChrFlags(0x18, 0x80)

    label("loc_1662")

    Jump("loc_1687")

    label("loc_1667")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1687")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_1687")

    Return()

    # Function_17_14D4 end

    def Function_18_1688(): pass

    label("Function_18_1688")

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
        "Welcome to the "Fortune-telling House"!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Here you can have divined many things\x01",
            "from a remarkable fortune teller!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Two persons can enter.\x01",
            "What do you want to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#6P(...Who should I invite?)\x02",
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
            "#1KWho will you invite?\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Elie")
    MenuCmd(1, 0, "Tio")
    MenuCmd(1, 0, "Randy")
    MenuCmd(1, 0, "Noｱl")
    MenuCmd(1, 0, "Wazy")
    MenuCmd(1, 0, "KeA")
    MenuCmd(1, 0, "Fran")
    MenuCmd(1, 0, "Cecil")
    MenuCmd(1, 0, "Ilya")
    MenuCmd(1, 0, "Rixia")
    MenuCmd(1, 0, "Sully")
    MenuCmd(1, 0, "Quit")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1863")
    MenuCmd(3, 0, 0x0)

    label("loc_1863")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1875")
    MenuCmd(3, 0, 0x1)

    label("loc_1875")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1887")
    MenuCmd(3, 0, 0x2)

    label("loc_1887")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1899")
    MenuCmd(3, 0, 0x3)

    label("loc_1899")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_18AB")
    MenuCmd(3, 0, 0x4)

    label("loc_18AB")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_18BD")
    MenuCmd(3, 0, 0x5)

    label("loc_18BD")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_18CF")
    MenuCmd(3, 0, 0x6)

    label("loc_18CF")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_18E1")
    MenuCmd(3, 0, 0x7)

    label("loc_18E1")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_18F3")
    MenuCmd(3, 0, 0x8)

    label("loc_18F3")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1905")
    MenuCmd(3, 0, 0x9)

    label("loc_1905")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1917")
    MenuCmd(3, 0, 0xA)

    label("loc_1917")

    MenuCmd(2, 0, -1, 55, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FF4")
    OP_D2(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_199D"),
        (1, "loc_19DF"),
        (2, "loc_1A20"),
        (3, "loc_1A63"),
        (4, "loc_1AA5"),
        (5, "loc_1AE7"),
        (6, "loc_1B28"),
        (7, "loc_1B6A"),
        (8, "loc_1BB4"),
        (9, "loc_1BFB"),
        (10, "loc_1C3E"),
        (SWITCH_DEFAULT, "loc_1C81"),
    )


    label("loc_199D")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Elie.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C81")

    label("loc_19DF")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Tio.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C81")

    label("loc_1A20")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Randy.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C81")

    label("loc_1A63")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Noｱl.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C81")

    label("loc_1AA5")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Wazy.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C81")

    label("loc_1AE7")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite KeA.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C81")

    label("loc_1B28")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Fran.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C81")

    label("loc_1B6A")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite sister Cecil.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C81")

    label("loc_1BB4")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Miss Ilya.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C81")

    label("loc_1BFB")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Rixia.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C81")

    label("loc_1C3E")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Sully.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C81")

    label("loc_1C81")

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
        (0, "loc_1D45"),
        (1, "loc_1D54"),
        (2, "loc_1D63"),
        (3, "loc_1D72"),
        (4, "loc_1D81"),
        (5, "loc_1D90"),
        (6, "loc_1D9F"),
        (7, "loc_1DAE"),
        (8, "loc_1DBD"),
        (9, "loc_1DCC"),
        (10, "loc_1DDB"),
        (SWITCH_DEFAULT, "loc_1DEA"),
    )


    label("loc_1D45")

    LoadChrToIndex("chr/ch00102.itc", 0x20)
    SetChrChipByIndex(0x15, 0x0)
    Jump("loc_1DEA")

    label("loc_1D54")

    LoadChrToIndex("chr/ch00202.itc", 0x20)
    SetChrChipByIndex(0x15, 0x1)
    Jump("loc_1DEA")

    label("loc_1D63")

    LoadChrToIndex("chr/ch00302.itc", 0x20)
    SetChrChipByIndex(0x15, 0x21)
    Jump("loc_1DEA")

    label("loc_1D72")

    LoadChrToIndex("chr/ch02902.itc", 0x20)
    SetChrChipByIndex(0x15, 0x2)
    Jump("loc_1DEA")

    label("loc_1D81")

    LoadChrToIndex("chr/ch03002.itc", 0x20)
    SetChrChipByIndex(0x15, 0x3)
    Jump("loc_1DEA")

    label("loc_1D90")

    LoadChrToIndex("chr/ch08202.itc", 0x20)
    SetChrChipByIndex(0x15, 0x22)
    Jump("loc_1DEA")

    label("loc_1D9F")

    LoadChrToIndex("chr/ch08502.itc", 0x20)
    SetChrChipByIndex(0x15, 0x4)
    Jump("loc_1DEA")

    label("loc_1DAE")

    LoadChrToIndex("chr/ch07502.itc", 0x20)
    SetChrChipByIndex(0x15, 0x23)
    Jump("loc_1DEA")

    label("loc_1DBD")

    LoadChrToIndex("chr/ch05102.itc", 0x20)
    SetChrChipByIndex(0x15, 0x24)
    Jump("loc_1DEA")

    label("loc_1DCC")

    LoadChrToIndex("chr/ch05202.itc", 0x20)
    SetChrChipByIndex(0x15, 0x5)
    Jump("loc_1DEA")

    label("loc_1DDB")

    LoadChrToIndex("chr/ch10102.itc", 0x20)
    SetChrChipByIndex(0x15, 0x25)
    Jump("loc_1DEA")

    label("loc_1DEA")

    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x101, -500, 0, 5000, 0)
    SetChrPos(0x15, 500, 0, 5000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xF,
        "I will take your ticket!\x02",
    )

    CloseMessageWindow()
    SubItemNumber(0x35D, 1)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Handed 1 ticket to the staff.\x07\x00\x02",
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
        "Then, please enter!\x02",
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
        (0, "loc_1F29"),
        (1, "loc_1F37"),
        (2, "loc_1F45"),
        (3, "loc_1F53"),
        (4, "loc_1F61"),
        (5, "loc_1F6F"),
        (6, "loc_1F7D"),
        (7, "loc_1F8B"),
        (8, "loc_1F99"),
        (9, "loc_1FA7"),
        (10, "loc_1FB5"),
        (SWITCH_DEFAULT, "loc_1FC3"),
    )


    label("loc_1F29")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1FC3")

    label("loc_1F37")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1FC3")

    label("loc_1F45")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1FC3")

    label("loc_1F53")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1FC3")

    label("loc_1F61")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1FC3")

    label("loc_1F6F")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1FC3")

    label("loc_1F7D")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1FC3")

    label("loc_1F8B")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1FC3")

    label("loc_1F99")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1FC3")

    label("loc_1FA7")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1FC3")

    label("loc_1FB5")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1FC3")

    label("loc_1FC3")

    OP_D2(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FEF")
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()

    label("loc_1FEF")

    Jump("loc_203D")

    label("loc_1FF4")


    ChrTalk(
        0xF,
        "My, are you not entering?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "We will wait for your next visit!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_203D")

    OP_4C(0xF, 0xFF)
    SetChrPos(0x0, 0, 0, 4000, 180)
    EventEnd(0x5)
    Return()

    # Function_18_1688 end

    def Function_19_2055(): pass

    label("Function_19_2055")

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

    def lambda_20E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20E0)

    def lambda_20F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_20F1)

    def lambda_2102():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2102)
    Sleep(0)

    def lambda_211A():
        OP_9B(0x0, 0x15, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_211A)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x15, 0)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x15, 2)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AF5")

    ChrTalk(
        0x16,
        "#5PUh uh, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PCome, sit on these chairs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PO-Ok.\x02",
    )

    CloseMessageWindow()
    Call(0, 20)

    ChrTalk(
        0x101,
        (
            "#00003F#6P(She's just like we heard...\x01",
            "Exotic and mysterious...)\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2238"),
        (1, "loc_22A3"),
        (2, "loc_2319"),
        (3, "loc_2381"),
        (4, "loc_23EF"),
        (5, "loc_248A"),
        (6, "loc_24EF"),
        (7, "loc_255D"),
        (8, "loc_25CA"),
        (9, "loc_2636"),
        (10, "loc_26A0"),
        (SWITCH_DEFAULT, "loc_270C"),
    )


    label("loc_2238")


    NpcTalk(
        0x15,
        "Elie",
        (
            "#00100F#12P(Yes, also, she has her face hidden,\x01",
            "but it looks like a very beautiful person.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270C")

    label("loc_22A3")


    NpcTalk(
        0x15,
        "Tio",
        (
            "#00200F#12P(Yes, furthermore...\x01",
            "Her face is hidden, but it looks\x01",
            "like she is quite a beautiful person.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270C")

    label("loc_2319")


    NpcTalk(
        0x15,
        "Randy",
        (
            "#00300F#12P(Yeah, also...\x01",
            "Her face's hidden, but it looks\x01",
            "like she's a beautiful lady.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270C")

    label("loc_2381")


    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10100F#12P(Yes, also...\x01",
            "Her face is hidden, but it looks like\x01",
            "she's a very beautiful person.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270C")

    label("loc_23EF")


    NpcTalk(
        0x15,
        "Wazy",
        "#10305F#12P(......Eeh......)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P(......Wazy?)\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10304F#12P(Hu hu, she's quite beautiful,\x01",
            "so I was a little surprised.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270C")

    label("loc_248A")


    NpcTalk(
        0x15,
        "KeA",
        (
            "#01100F#12P(Yes, also, her face is hidden, but it\x01",
            "looks like she's a beautiful woman.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270C")

    label("loc_24EF")


    NpcTalk(
        0x15,
        "Fran",
        (
            "#06400F#12P(Yes, also, her face is hidden, but it\x01",
            "looks like she's a greatly beautiful woman.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270C")

    label("loc_255D")


    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05900F#12P(Yes, also, her face is hidden, but it\x01",
            "looks like she is a very beautiful woman.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270C")

    label("loc_25CA")


    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01700F#12P(Yes, also, her face is hidden, but it\x01",
            "looks like she's quite a beautiful woman.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270C")

    label("loc_2636")


    NpcTalk(
        0x15,
        "Rixia",
        (
            "#01802F#12P(Yes... Her face is hidden, but it looks\x01",
            "like she's a very beautiful woman...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270C")

    label("loc_26A0")


    NpcTalk(
        0x15,
        "Sully",
        (
            "#14000F#12P(Yeah, also...\x01",
            "Her face is hidden, but it looks\x01",
            "like she's amazingly beautiful.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270C")

    label("loc_270C")


    ChrTalk(
        0x16,
        (
            "#5PUh uh, what seems to be the matter? \x01",
            "Both of you are staring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThere are others waiting,\x01",
            "so I wouldd like to begin now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6POh, sorry.\x01",
            "Please do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PUh uh. Before that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PWill you first tell\x01",
            "me your blood types?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2879"),
        (1, "loc_28A7"),
        (2, "loc_28D4"),
        (3, "loc_28FB"),
        (4, "loc_2921"),
        (5, "loc_2947"),
        (6, "loc_296C"),
        (7, "loc_2999"),
        (8, "loc_29C8"),
        (9, "loc_2A0F"),
        (10, "loc_2A3E"),
        (SWITCH_DEFAULT, "loc_2A68"),
    )


    label("loc_2879")


    NpcTalk(
        0x15,
        "Elie",
        "#00105F#12PBlood type...is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A68")

    label("loc_28A7")


    NpcTalk(
        0x15,
        "Tio",
        "#00205F#12PBlood type...is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A68")

    label("loc_28D4")


    NpcTalk(
        0x15,
        "Randy",
        "#00305F#12PBlood type?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A68")

    label("loc_28FB")


    NpcTalk(
        0x15,
        "Noｱl",
        "#10105F#12PBlood type?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A68")

    label("loc_2921")


    NpcTalk(
        0x15,
        "Wazy",
        "#10305F#12PBlood type?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A68")

    label("loc_2947")


    NpcTalk(
        0x15,
        "KeA",
        "#01105F#12PBlood type?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A68")

    label("loc_296C")


    NpcTalk(
        0x15,
        "Fran",
        "#06405F#12PBlood type, is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A68")

    label("loc_2999")


    NpcTalk(
        0x15,
        "Cecil",
        "#05905F#12PBlood type...is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A68")

    label("loc_29C8")


    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01705F#12PBlood type...\x01",
            "I wonder what you need it for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A68")

    label("loc_2A0F")


    NpcTalk(
        0x15,
        "Rixia",
        "#01805F#12PBlood type...is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A68")

    label("loc_2A3E")


    NpcTalk(
        0x15,
        "Sully",
        "#14005F#12PBlood type...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A68")

    label("loc_2A68")


    ChrTalk(
        0x16,
        (
            "#5PYes. It is needed for\x01",
            "a proper reading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5POf course I will\x01",
            "not force you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PNo, I don't mind.\x01",
            "...I'm type 0.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C47")

    label("loc_2AF5")


    ChrTalk(
        0x16,
        "#5POh, you are the one from before...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PUh uh, welcome.\x01",
            "Please sit on these chairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYes. \x02",
    )

    CloseMessageWindow()
    Call(0, 20)

    ChrTalk(
        0x16,
        (
            "#5PIt makes me really glad\x01",
            "you have come again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThen, I know it is sudden,\x01",
            "but will you tell me your\x01",
            "blood types?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P...If I remember correctly,\x01",
            "you are a type 0, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYes, you're right.\x02",
    )

    CloseMessageWindow()

    label("loc_2C47")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2C92"),
        (1, "loc_2CBE"),
        (2, "loc_2CE5"),
        (3, "loc_2D0E"),
        (4, "loc_2D34"),
        (5, "loc_2D67"),
        (6, "loc_2E06"),
        (7, "loc_2E52"),
        (8, "loc_2E80"),
        (9, "loc_2EA8"),
        (10, "loc_2F04"),
        (SWITCH_DEFAULT, "loc_2F39"),
    )


    label("loc_2C92")


    NpcTalk(
        0x15,
        "Elie",
        "#00100F#12PUhhm, I'm type A.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F39")

    label("loc_2CBE")


    NpcTalk(
        0x15,
        "Tio",
        "#00200F#12PI am type AB.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F39")

    label("loc_2CE5")


    NpcTalk(
        0x15,
        "Randy",
        "#00300F#12PI'm a B type.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F39")

    label("loc_2D0E")


    NpcTalk(
        0x15,
        "Noｱl",
        "#10100F#12PI'm type A.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F39")

    label("loc_2D34")


    NpcTalk(
        0x15,
        "Wazy",
        "#10300F#12PHu hu, type AB, I think?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F39")

    label("loc_2D67")


    NpcTalk(
        0x15,
        "KeA",
        (
            "#01109F#12PEehm, I'm sure that\x01",
            "KeA is a type B, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah, we confirmed that previously\x01",
            "via examination at St. Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F39")

    label("loc_2E06")


    NpcTalk(
        0x15,
        "Fran",
        "#06409F#12POh, I'm a type 0!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#6PHa ha, we match.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F39")

    label("loc_2E52")


    NpcTalk(
        0x15,
        "Cecil",
        "#05900F#12PEhhm, I am type A.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F39")

    label("loc_2E80")


    NpcTalk(
        0x15,
        "Ilya",
        "#01700F#12PI'm a B type.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F39")

    label("loc_2EA8")


    NpcTalk(
        0x15,
        "Rixia",
        "#01802F#12PAh... I'm also type 0.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#6PHa ha. What a coincidence.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F39")

    label("loc_2F04")


    NpcTalk(
        0x15,
        "Sully",
        (
            "#14000F#12PEehm...\x01",
            "I guess I'm an A.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F39")

    label("loc_2F39")


    ChrTalk(
        0x16,
        "#5PUh uh... Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PThen, what will I be reading this time?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PHmm, let's see...\x02",
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2FF1"),
        (1, "loc_2FF9"),
        (2, "loc_3001"),
        (3, "loc_3009"),
        (4, "loc_3011"),
        (5, "loc_3019"),
        (6, "loc_3021"),
        (7, "loc_3029"),
        (8, "loc_3031"),
        (9, "loc_3039"),
        (10, "loc_3041"),
        (SWITCH_DEFAULT, "loc_3049"),
    )


    label("loc_2FF1")

    Call(0, 25)
    Jump("loc_3049")

    label("loc_2FF9")

    Call(0, 26)
    Jump("loc_3049")

    label("loc_3001")

    Call(0, 27)
    Jump("loc_3049")

    label("loc_3009")

    Call(0, 28)
    Jump("loc_3049")

    label("loc_3011")

    Call(0, 29)
    Jump("loc_3049")

    label("loc_3019")

    Call(0, 30)
    Jump("loc_3049")

    label("loc_3021")

    Call(0, 31)
    Jump("loc_3049")

    label("loc_3029")

    Call(0, 32)
    Jump("loc_3049")

    label("loc_3031")

    Call(0, 33)
    Jump("loc_3049")

    label("loc_3039")

    Call(0, 34)
    Jump("loc_3049")

    label("loc_3041")

    Call(0, 35)
    Jump("loc_3049")

    label("loc_3049")

    OP_24(0x354)
    Call(0, 17)
    Call(0, 21)
    Return()

    # Function_19_2055 end

    def Function_20_3053(): pass

    label("Function_20_3053")

    OP_68(0, 900, 103500, 3000)
    SetCameraDistance(15000, 3000)

    def lambda_3072():
        OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3072)

    def lambda_3087():
        OP_9B(0x0, 0xFE, 0xA, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3087)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x15, 1)

    def lambda_30A4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30A4)

    def lambda_30B1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_30B1)
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

    # Function_20_3053 end

    def Function_21_3107(): pass

    label("Function_21_3107")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_315A"),
        (1, "loc_3163"),
        (2, "loc_316C"),
        (3, "loc_3175"),
        (4, "loc_317E"),
        (5, "loc_3187"),
        (6, "loc_3190"),
        (7, "loc_3199"),
        (8, "loc_31A2"),
        (9, "loc_31AB"),
        (10, "loc_31B4"),
        (SWITCH_DEFAULT, "loc_31BD"),
    )


    label("loc_315A")

    SetChrChipByIndex(0x15, 0x0)
    Jump("loc_31BD")

    label("loc_3163")

    SetChrChipByIndex(0x15, 0x1)
    Jump("loc_31BD")

    label("loc_316C")

    SetChrChipByIndex(0x15, 0x21)
    Jump("loc_31BD")

    label("loc_3175")

    SetChrChipByIndex(0x15, 0x2)
    Jump("loc_31BD")

    label("loc_317E")

    SetChrChipByIndex(0x15, 0x3)
    Jump("loc_31BD")

    label("loc_3187")

    SetChrChipByIndex(0x15, 0x22)
    Jump("loc_31BD")

    label("loc_3190")

    SetChrChipByIndex(0x15, 0x4)
    Jump("loc_31BD")

    label("loc_3199")

    SetChrChipByIndex(0x15, 0x23)
    Jump("loc_31BD")

    label("loc_31A2")

    SetChrChipByIndex(0x15, 0x24)
    Jump("loc_31BD")

    label("loc_31AB")

    SetChrChipByIndex(0x15, 0x5)
    Jump("loc_31BD")

    label("loc_31B4")

    SetChrChipByIndex(0x15, 0x25)
    Jump("loc_31BD")

    label("loc_31BD")

    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -600, 0, 5000, 90)
    SetChrPos(0x15, 600, 0, 5000, 270)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3211")
    SetChrPos(0x17, 1700, 0, 4040, 270)

    label("loc_3211")

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
        (0, "loc_32A7"),
        (1, "loc_33EA"),
        (2, "loc_3523"),
        (3, "loc_363B"),
        (4, "loc_3755"),
        (5, "loc_3889"),
        (6, "loc_39F2"),
        (7, "loc_3B13"),
        (8, "loc_3C2E"),
        (9, "loc_3D7A"),
        (10, "loc_3ED0"),
        (SWITCH_DEFAULT, "loc_3FEA"),
    )


    label("loc_32A7")


    NpcTalk(
        0x15,
        "Elie",
        (
            "#00100F#11P*haah*...somehow it was\x01",
            "a very mysterious moment.\x02\x03",
            "#00104FJudging by that fortune teller's air,\x01",
            "she really seemed she was guessing right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PYeah...\x01",
            "She doesn't look like an ordinary person.\x02\x03",
            "#00000F...Well then, \x01",
            "I'll take off here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Elie",
        "#00100F#11PYes, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3FEA")

    label("loc_33EA")


    NpcTalk(
        0x15,
        "Tio",
        (
            "#00202FI felt quite an aura in that\x01",
            "fortune teller's divination.\x02\x03",
            "#00204FAs expected from the rumors about her,\x01",
            "it seems she's not an ordinary person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FIndeed...\x01",
            "Somehow she seemed a great woman.\x02\x03",
            "#00000F...Well then, \x01",
            "I'll go for now.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Tio",
        "#00200FYes, see you later, then.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3FEA")

    label("loc_3523")


    NpcTalk(
        0x15,
        "Randy",
        (
            "#00309F...*haah*, still, she was\x01",
            "an amazin' lady, huh?\x02\x03",
            "#00304FThat mysterious air was\x01",
            "irresistible, I'd say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha...indeed.\x01",
            "Her reading seemed to\x01",
            "be amazingly coherent.\x02\x03",
            "#00000F...Well then, \x01",
            "I'll go for now.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Randy",
        "#00300FYeah, later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3FEA")

    label("loc_363B")


    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10100F...*phew*, somehow it\x01",
            "was a mysterious moment.\x02\x03",
            "#10104FHer reading was persuasive too...\x01",
            "Somehow it's a strange feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah...\x01",
            "It was quite interesting.\x02\x03",
            "#00000F...Well then, \x01",
            "I'll go for now.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noｱl",
        "#10100FYes, see you later, then!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3FEA")

    label("loc_3755")


    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10300FHu hu, she was quite\x01",
            "the interesting lady.\x02\x03",
            "#10304FI would've liked to speak about\x01",
            "other things a little more, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, indeed.\x01",
            "It's like my outlook on the\x01",
            "world seemed to expand.\x02\x03",
            "#00000F...Well then, \x01",
            "I'll go for now.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Wazy",
        "#10300FYeah, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3FEA")

    label("loc_3889")


    NpcTalk(
        0x15,
        "KeA",
        (
            "#01109FFortune telling...it was very interesting.\x02\x03",
            "#01111FHow can she know all that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FUhhm, I don't know, but...\x01",
            "I'm sure she must've\x01",
            "trained considerably.\x02\x03",
            "#00000F...Well then, \x01",
            "I'll go for now.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "KeA",
        "#01100FYes, see you!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39E3")

    ChrTalk(
        0x17,
        "#01200F...Woof.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    EndChrThread(0x17, 0x0)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    OP_93(0x17, 0xB4, 0x1F4)

    def lambda_39C1():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_39C1)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x15, 3)
    SetChrFlags(0x17, 0x80)
    Jump("loc_39ED")

    label("loc_39E3")

    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)

    label("loc_39ED")

    Jump("loc_3FEA")

    label("loc_39F2")


    NpcTalk(
        0x15,
        "Fran",
        (
            "#06402F*haah*...somehow she\x01",
            "was a mysterious lady.\x02\x03",
            "#06409FI admire cool women like\x01",
            "my big sis but also\x01",
            "persons like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHa ha...there aren't quite any\x01",
            "of that type in Crossbell.\x02\x03",
            "#00000F...Well then, \x01",
            "I'll go for now.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Fran",
        "#06400FYes, see you!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3FEA")

    label("loc_3B13")


    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05909FUh uh...somehow she\x01",
            "was a mysterious woman.\x02\x03",
            "#05904FIt looked like she\x01",
            "had quite a past...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah...I wonder what circumstances\x01",
            "brought her to come to Crossbell.\x02\x03",
            "#00000F...Well then, \x01",
            "I'll go for now.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Cecil",
        "#05900FYes, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3FEA")

    label("loc_3C2E")


    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01702FMan, there're all kind of\x01",
            "amazing people in the world.\x02\x03",
            "#01703FAlthough we met for the first time, I felt like \x01",
            "she could see through me from top to bottom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYes, it's true...\x01",
            "She didn't seem an ordinary person.\x02\x03",
            "#00000F...Well then, \x01",
            "I'll go for now.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Ilya",
        "#01700FYes, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3FEA")

    label("loc_3D7A")


    NpcTalk(
        0x15,
        "Rixia",
        (
            "#01803F(Such masterful fortunetelling...\x01",
            "Could she be...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FRixia, what's wrong?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Rixia",
        (
            "#01805FAh, nothing.\x02\x03",
            "#01802FUh uh, I had a lot of fun having been\x01",
            "able to make a mysterious experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, same for me.\x02\x03",
            "#00000F...Well then, \x01",
            "I'll go for now.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Rixia",
        "#01803FYes, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3FEA")

    label("loc_3ED0")


    NpcTalk(
        0x15,
        "Sully",
        (
            "#14000F...Somehow she was a great fortune teller.\x02\x03",
            "#14006FI don't believe in readings at all,\x01",
            "but I can't say that just this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah...\x01",
            "Indeed, it was a great reading.\x02\x03",
            "#00000F...Well then, \x01",
            "I'll go for now.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Sully",
        "#14000F...Hm, see ya.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3FEA")

    label("loc_3FEA")

    Return()

    # Function_21_3107 end

    def Function_22_3FEB(): pass

    label("Function_22_3FEB")


    def lambda_3FF0():

        label("loc_3FF0")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_3FF0")

    QueueWorkItem2(0x101, 2, lambda_3FF0)
    OP_93(0x15, 0xB4, 0x1F4)

    def lambda_4009():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4009)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x15, 1)
    EndChrThread(0x101, 0x2)
    Return()

    # Function_22_3FEB end

    def Function_23_4030(): pass

    label("Function_23_4030")

    Fade(500)
    Sound(895, 0, 50, 0)
    Sound(852, 2, 70, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 900, 103300, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Return()

    # Function_23_4030 end

    def Function_24_407A(): pass

    label("Function_24_407A")

    Fade(500)
    StopSound(852, 1000, 40)
    StopEffect(0x0, 0x2)
    OP_0D()
    Return()

    # Function_24_407A end

    def Function_25_408A(): pass

    label("Function_25_408A")

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
            "#1KWhat would you like her to tell you?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "About Our Compatibility\x01",      # 0
            "Leave it to Elie\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A9B")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, it is an easy request.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Elie",
        "#00112F#12PL-Lloyd...!?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PWell, we came here on purpose and\x01",
            "we don't even have chances like this.\x02\x03",
            "#00000FWhy don't we do it just to try?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Elie",
        "#00106F#12P"J-Just to try" you say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PUhhm...is something not ok?\x02\x03",
            "#00003FIf you're so not inclined to it, we can stop...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Elie",
        (
            "#00105F#12PI-It's not that I'm not inclined...\x02\x03",
            "#00113FHonestly, I can't believe you're such a...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Elie",
        (
            "#00111F#12P...*haah*, it's nothing.\x02\x03",
            "#00100FExcuse me, please read\x01",
            "out compatibility.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PUh uh, well then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
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
        "Elie",
        "#00101F#12P(*glom*......)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man and a talented\x01",
            "woman brimming with diligence and tolerance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAs comrades with the same goals,\x01",
            "together you overcame many hardships\x01",
            "and are tied by a solid bond...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_464A")
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#5POh...furthermore, because you fell\x01",
            "into some kind of an extreme situation\x01",
            "before, that bond progressed greatly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIt is not set in stone yet, but if you\x01",
            "keep rearing this feeling, eventually\x01",
            "it should become a close relationship.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4716")

    label("loc_464A")


    ChrTalk(
        0x16,
        (
            "#5PYour births may differ, but recognizing\x01",
            "each other's strong points, you can\x01",
            "mutually complement...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf you keep rearing this feeling,\x01",
            "eventually it could turn\x01",
            "into a close relationship.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4716")

    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P...This is what I am able to see.\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Elie",
        "#00112F#12PA c-close relationship...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PUh uh, well then...\x01",
            "It may be rude of me\x01",
            "saying something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHowever, what will be crucial\x01",
            "is your future actions and choices...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PM-Mine?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAt least you will have to make a great\x01",
            "effort to judge the other's feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAlthough unconscious, you have a charming\x01",
            "nature that ends up fascinating your surroundings──\x01",
            "That's the "hint" I can see.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012F#6PC-Charming nature, you say...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Elie",
        "#00106F#12P(I think she got it quite right...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PStill, a reading is just a\x01",
            "reading, not a prediction...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P"Fate" always moves under\x01",
            "the principle of causality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIt can change a lot according\x01",
            "to your future actions...\x01",
            "Remember that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PY-Yes.\x01",
            "I'll keep that in mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51CA")

    label("loc_4A9B")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PElie, do you have something\x01",
            "you want her to divine you?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Elie",
        (
            "#00105F#12POh, can I decide?\x02\x03",
            "#00103FUhhm, let's see...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Elie",
        (
            "#00100F#12PIn this case...\x01",
            "Can I have divined the autonomous\x01",
            "state of Crossbell future?\x02\x03",
            "#00103FWhat is going to happen due to\x01",
            "the independence proposal...\x01",
            "Aren't you concerned about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#6PYeah, indeed.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00000F#6P...Then, could\x01",
            "you please?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x16,
        "#5PUh uh, it is an easy request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
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
        "Elie",
        "#00101F#12P(*glom*......)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5P...Before long, you will be\x01",
            "involved in a very great fate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThe despair of facing a colossal "barrier"\x01",
            "like you have not seen until now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYou are going to savor that.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PHuh...!?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Elie",
        "#00105F#12PW-What do you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P...I do not know what is going to be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThough, those footsteps are\x01",
            "steadily getting closer to you...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P...What I could see ends here.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x15)

    NpcTalk(
        0x15,
        "Elie",
        "#00103F#12P...W-What was that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PA colossal "barrier"...\x01",
            "The despair of facing it...\x02\x03",
            "#00008FWhat could be related to the\x01",
            "Mayor's independence proposal...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P...I do not know the details.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PMy readings are, after all, what\x01",
            "I can read from the hints I get.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Elie",
        (
            "#00106F#12PUhhm, it worries me, but...\x01",
            "For now, I can't help but be concerned about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIt seems I have stirred up\x01",
            "some unnecessary worries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PStill, a reading is just a\x01",
            "reading, not a prediction...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P"Fate" always moves under\x01",
            "the principle of causality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIt can change a lot according\x01",
            "to your future actions...\x01",
            "Remember that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6P...Yes, we'll keep that in mind.\x02",
    )

    CloseMessageWindow()

    label("loc_51CA")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_25_408A end

    def Function_26_51D6(): pass

    label("Function_26_51D6")

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
            "#1KWhat would you like her to tell you?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "About Our Compatibility\x01",      # 0
            "Leave it to Tio\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B49")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, it is an easy request.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6P...I mean, what do you think?\x01",
            "Since we're here, it's just to try.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00203F#12P...Hm, it seems interesting.\x02\x03",
            "#00200FWhatever the result will be,\x01",
            "it seems I will be able to\x01",
            "make my plans for the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P...I don't really get it.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00203F#12PNo, it is fine if you don't get it at all.\x02\x03",
            "#00200FThen, please proceed.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PUh uh, well then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
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
            "#00205F#12P(...I sense a mysterious aura...\x01",
            "What could it be...?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man and a\x01",
            "young girl hiding a superior ability...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAlthough apart in age,\x01",
            "you can trust each other\x01",
            "as equal comrades...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_56CC")
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#5POh...furthermore, because you fell\x01",
            "into some kind of an extreme situation\x01",
            "before, that bond progressed greatly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI think there will be many obstacles,\x01",
            "but the hint I get is that a close\x01",
            "relationship is highly possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_57A4")

    label("loc_56CC")


    ChrTalk(
        0x16,
        (
            "#5PYour births may differ, but recognizing\x01",
            "each other's strong points, you can\x01",
            "mutually complement...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI think there will be many obstacles,\x01",
            "but there is quite the possibility of a\x01",
            "close relationship.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_57A4")

    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P...This is what I am able to see.\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    NpcTalk(
        0x15,
        "Tio",
        "#00204F#12PHm...we received an interesting result.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PUhm, I don't really get it...\x02\x03",
            "#00000FWhat could you referring to\x01",
            ""many obstacles"...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PUh uh, if I had to say...\x01",
            "Social taboos and others' glances...\x01",
            "Those kind of things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PDo you have the resolve to\x01",
            "overcome that, or maybe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PWhat...?\x01",
            "Resolve...\x02\x03",
            "#00003FAlthough I have a deep friendship\x01",
            "with Tio, I'm not at all bothered\x01",
            "by other people's glances...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Tio",
        "#00211F#12P...What an unexpected bombshell statement.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PUh uh, what an interesting man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI will just pray the Goddess that\x01",
            "that personality will not invite you\x01",
            "many disasters in the future.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Tio",
        "#00206F#12PYes, exactly that.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6PU-Uhm...\x01",
            "Could you not talk\x01",
            "leaving me out of it...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61FD")

    label("loc_5B49")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PTio, do you want to have\x01",
            "her divine you something?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00205F#12PIs it all right for me to decide?\x02\x03",
            "#00203F...Let's see...\x02",
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
            "#00200F#12PCan you tell me my\x01",
            "compatibility with Michey?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PYour compatibility with M-Michey...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00202F#12PYes, I really want to know...\x01",
            "If I will be able to meet\x01",
            "Michey in the future too.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        (
            "#5PHm, quite a unique request.\x01",
            "...All right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
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
            "#00205F#12P(...I sense a mysterious aura...\x01",
            "What could it be...?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5P...Your compatibility with Michey...\x01",
            "It seems to be quite good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAs long as you love him,\x01",
            "Michey will sure answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIn the future, many Michey's goods and\x01",
            "meetings at the theme park await you...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P...This is what I am able to see.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Tio",
        "#00202F#12PUh uh, thank you very much.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PW-Well, aren't you glad?\x01",
            "She says that Michey will sure answer.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00204F#12PYes, as a fan, there is\x01",
            "nothing better than this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5POh, one more thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PBefore long, a great trial will\x01",
            "come to you to test your\x01",
            "feelings toward Michey...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI also have that kind of hint.\x01",
            "...Be careful as much as possible, hm?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00200F#12P...It is just what I wish for.\x02\x03",
            "#00201FNo matter what trials come,\x01",
            "nothing will be able to shake\x01",
            "my love towards Michey...\x02\x03",
            "#00204FI will show you that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PUh uh, I am rooting for you.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6P(I-It's no use.\x01",
            "There're too many possible retorts I\x01",
            "could make that I can't deal with them...!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61FD")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_26_51D6 end

    def Function_27_6209(): pass

    label("Function_27_6209")

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
            "#1KWhat would you like her to tell you?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "About Our Compatibility\x01",      # 0
            "Leave it to Randy\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B6D")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, it is an easy request.\x02",
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
            "#00306F#12PI can't believe you...\x01",
            "Ask something like that for a girl you like, no?\x02\x03",
            "#00301FWhat fun is there in checkin'\x01",
            "the compatibility among dudes?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PHa ha, well, what's wrong with it?\x02\x03",
            "#00000FAlso, speaking of compatibility,\x01",
            "there's also the one among male friends, right?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00306F#12PHmm...well, whatever.\x02\x03",
            "#00300FThen lady, please.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PUh uh, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
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
        "#00305F#12P(Ooh...ain't she serious?)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man and a\x01",
            "young man with inner passion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAlways taking the lead as a centripetal force,\x01",
            "a reassuring companion who encourages\x01",
            "and leads the others with his cheerfulness...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_674C")
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#5POh...furthermore, because you fell\x01",
            "into some kind of an extreme situation\x01",
            "before, that deepened greatly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf you deepen your each other understanding\x01",
            "from now on and increase it, you could be\x01",
            "tied by an even more solid bond.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_682E")

    label("loc_674C")


    ChrTalk(
        0x16,
        (
            "#5PYour births may differ, but recognizing\x01",
            "each other's strong points, you can\x01",
            "mutually complement...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf you deepen your each other understanding\x01",
            "from now on and increase it, you could be\x01",
            "tied by a solid bond.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_682E")

    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P...This is what I am able to see.\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00305F#12POoh...somehow it seems\x01",
            "a nice result, huh?\x02\x03",
            "#00304FMilady, peTiote...\x01",
            "Noｱl too...I'm sorry.\x02\x03",
            "#00302FIt seems that Lloyd\x01",
            "will be mine.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00006F#6P...Stop blurting out\x01",
            "inappropriate stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHe is right, I did not get a hint\x01",
            "that you will get that close.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        (
            "#5PHowever, fate is something\x01",
            "that changes if you wish it\x01",
            "strongly to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PSo I can not deny that will\x01",
            "be completely impossible\x01",
            "in the future.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PU-Uhm, if possible,\x01",
            "I'd like you to deny that.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00309F#12PHa ha, don't be shy, don't be.\x02\x03",
            "#00304FIf you wishes for it,\x01",
            "I could be a reliable big bro──\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00011F#6PI'm not being shy or whatever!!\x02\x03",
            "#00006F*haah*, cut me some slack, really...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_732A")

    label("loc_6B6D")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PRandy, why don't you have\x01",
            "her divine you something?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00305F#12PHm? Is it ok for me to decide?\x02\x03",
            "#00303FThen let's see...\x02",
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
            "#00309F#12PHmm, in this case...\x01",
            "Could you tell me my luck in\x01",
            "pickin' up girls from now on?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006F#6PA-Are you fine with that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PYou intend the possibility that a woman you do\x01",
            "not know accepts your invite when talked to...\x01",
            "Am I being right?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Randy",
        "#00309F#12PYes, please!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PUh uh, it is an easy request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
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
        "#00305F#12P(Ooh...ain't she serious?)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5P...About your "picking up girls"...\x01",
            "I would say your chance of success\x01",
            "is about 50/50.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIt seems that many women feel the charm of your\x01",
            "bright nature and handsome looks, however...\x01",
            "There are really many who are vigilant too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIncidentally, even if you were successful,\x01",
            "I can say that in your case, the ratio of\x01",
            "true love you would get is almost zero.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    NpcTalk(
        0x15,
        "Randy",
        "#00306F#12P#4S*ACK*!!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P...This is what I am able to see.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00306F#12PL-Loyd...\x01",
            "It's over for me...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00012F#6PN-Now, now...\x01",
            "Don't feel so down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PUh uh, he is right.\x01",
            "If I can give you an advice...\x01",
            "You must not let escape the love which is near you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PClose to you, there is a woman\x01",
            "who regards you as important...\x01",
            "I had that kind of hint too.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    NpcTalk(
        0x15,
        "Randy",
        "#00305F#12PS-Seriously!?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould she mean...\x01",
            "2nd Lt. Mire──\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00303F#12P──Alright!! Bein' this the case...\x02\x03",
            "#00309FI can only strive to keep pickin' \x01",
            "up girls until I find the cutie\x01",
            "who regards me as important!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        "#00006F#6PH-How could you reach that conclusion...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P(...Pretending to not notice, I believe.\x01",
            "Uh uh, it has nothing to do with me, though.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_732A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_27_6209 end

    def Function_28_7336(): pass

    label("Function_28_7336")

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
            "#1KWhat would you like her to tell you?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "About Our Compatibility\x01",      # 0
            "Leave it to Noｱl\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BB5")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, it is an easy request.\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Noｱl",
        "#10105F#12PM-Mr. Lloyd!?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PHa ha, well, since we're here,\x01",
            "I thought why not to try?\x02\x03",
            "#00000FIf it's troublesome for you, we can stop...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10111F#12PN-No!!\x01",
            "It's not troublesome\x01",
            "or anything...\x02\x03",
            "#10116F(Wait, is it saying this too\x01",
            "spontaneously or...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PUhhm, what's wrong?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10106F#12PI-It's nothing.\x02\x03",
            "#10100F...Uhm, then, please\x01",
            "do your reading.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PUh uh, very well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
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
        "Noｱl",
        "#10105F#12P(Wow...is it some kind of a skill...?)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man and a\x01",
            "girl with a sincere will in her eyes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PYour positions may differ, but through\x01",
            "cooperating towards the same goal to protect\x01",
            "something, you built a strong relationship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf either one takes a step forward and\x01",
            "enters in a deep part of it, it could\x01",
            "turn into something more intimate.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P...This is what I am able to see.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10105F#12PTaking a step forward...is it?\x01",
            "That's the part I'm quite weak in.\x02\x03",
            "#10106FRather, I'm one who draws the lines...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PUh uh, judging from what I see,\x01",
            "you seems the prudent type,\x01",
            "so it can not be helped, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf you do not become somewhat\x01",
            "proactive, will not even the things\x01",
            "you have go away from you?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10103F#12PI-Indeed, it may\x01",
            "be like that, but...\x02\x03",
            "#10101F...But, right.\x01",
            "I too can only try to muster up my\x01",
            "courage when push come to shove...!\x02",
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
            "#00012F#6PE-Ehhm, Noｱl?\x01",
            "Haven't you become a little too serious...?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10105F#12PAh...\x02\x03",
            "#10106F...Y-You're right.\x01",
            "It's just to try anyway...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10105F#12P...Wait, no!\x01",
            "I'm not thinking that\x01",
            "it's a pity at all...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PI-I know, calm\x01",
            "down a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P(Uh uh, unexpectedly, they could be a nice couple.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8266")

    label("loc_7BB5")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PNoｱl, why don't you have\x01",
            "her divine you something?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10105F#12PIs it all right for me to decide?\x02\x03",
            "#10103FUhhm, let's see...\x02",
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
        "Noｱl",
        (
            "#10100F#12PThen, something\x01",
            "like the CGF's future...\x01",
            "What about that?\x02\x03",
            "#10104FEventually, I'll return to the CGF,\x01",
            "I think I should be ready for when\x01",
            "that time comes.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00002F#6PYeah, why not?\x02\x03",
            "#00000FUhhm, then,\x01",
            "please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, it is an easy request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Noｱl",
        "#10105F#12P(Wow...is it some kind of a skill...?)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        "#5P...This is a hint of change.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PBefore not too long,\x01",
            "the organization you belong to\x01",
            "will undergo a kind of change...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAt that time, you will be faced\x01",
            "with some kind of a big decision...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P...This is what I am able to see.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10103F#12PA change...and also, a decision?\x02\x03",
            "#10101FExcuse me, what could that mean...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PUnfortunately, I can not see\x01",
            "that clearly at present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf good or bad, I would say\x01",
            "it will depend by the change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PUhhm, it's true that at the present point,\x01",
            "it could be said that both are possible.\x02\x03",
            "#00000FDepending on the independence \x01",
            "proposal results, it seems that\x01",
            "the CGF's state will change too.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10100F#12PTo the CGF, that could\x01",
            "mean progress or decline...\x02\x03",
            "#10103FI want to wish that it will\x01",
            "be progress, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PI can only say one thing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PMake a decision you will\x01",
            "never regret in your life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PA reading is, after all, a reading...\x01",
            "The future will change so much\x01",
            "with just one of your decisions.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10100F#12PYes, you're right...\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8266")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_28_7336 end

    def Function_29_8272(): pass

    label("Function_29_8272")

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
            "#1KWhat would you like her to tell you?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "About Our Compatibility\x01",      # 0
            "Leave it to Wazy\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89CE")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, it is an easy request.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10302F#12PHu hu, this is rare.\x01",
            "You approaching me,\x01",
            "that is.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00003F#6PN-No, it's not\x01",
            "like that.\x02\x03",
            "#00000FWe came here on purpose,\x01",
            "so I thought to just try.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Wazy",
        "#10309F#12PHu hu, you don't have to be embarrassed.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#00006F#6P...A-Anyway, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PUh uh, all right.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
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
        "#5P(......I see......)\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10309F#12PHu hu, is something wrong,\x01",
            "fortune teller lady?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P...Uh uh, it is nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P......?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man and a\x01",
            "boy who wittily wanders the world...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PWhile your personalities are exactly the opposite,\x01",
            "by recognizing each other's excellent traits\x01",
            "you have built a solid trust...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PDeepening that trust, you could reach a point\x01",
            "to tolerate each other, past and present included, \x01",
            "and you will be tied by a firm bond.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P...This is what I am able to see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PPast and present included...\x02\x03",
            "#00003F...It's true that I didn't\x01",
            "here from you hardly\x01",
            "anything about your past.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10309F#12PHu hu, oh come on.\x01",
            "It may appear like this, but I told\x01",
            "you all without hiding anything.\x02\x03",
            "#10304FAlso, don't you think that it's more\x01",
            "exciting having some small secrets?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6PThen you really are keeping\x01",
            "some secrets...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PUh uh, well, it means you are assiduously together.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThis type of person hardly\x01",
            "shows its real motives.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10304F#12PHu hu, you've heard her.\x02\x03",
            "#10309FBy all means, I would be happy too\x01",
            "if you used an assiduous approach.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        "#00006F#6POh boy...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8ECA")

    label("loc_89CE")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PWazy, why don't you have\x01",
            "her divine you something?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10305F#12POh, can I decide?\x02\x03",
            "#10304FLet's see...\x02",
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
        "Wazy",
        (
            "#10300F#12PIn this case...\x01",
            "What about this?\x02\x03",
            "#10304FI'd like to read if I'll be\x01",
            "able to get what I want in\x01",
            "this land...or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PWhat you want...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10304F#12PHu hu, that's a secret.\x02\x03",
            "#10300FHow about it, lady?\x01",
            "Can you divine that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PUh uh, interesting.\x01",
            "...I will try.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
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
        "#5P(......I see......)\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10309F#12PHu hu, is something wrong,\x01",
            "fortune teller lady?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P...Uh uh, it is nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P......?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PWhat you are seeking...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIs very close to you, but\x01",
            "you can not reach it at all now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PFor now, you just have to wait for the right time...\x01",
            "That is the kind of hint I got.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P...This is what I am able to see.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10304F#12P...I see.\x01",
            "Knowing that much is plenty for me.\x02",
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
            "#00006F#6PI don't know what\x01",
            "what was that at all...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10300F#12PHu hu, that's good for now.\x02\x03",
            "#10304FAlso, don't you think that it's more\x01",
            "exciting having some small secrets?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P*haah*, honestly...\x02",
    )

    CloseMessageWindow()

    label("loc_8ECA")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_29_8272 end

    def Function_30_8ED6(): pass

    label("Function_30_8ED6")

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
            "#1KWhat would you like her to tell you?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "About Our Compatibility\x01",      # 0
            "Leave it to KeA\x01",              # 1
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95D0")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, it is an easy request.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "KeA",
        (
            "#01110F#12PLloyd, "compatibility" is that thing\x01",
            "if we're well-matched or not, right?\x02\x03",
            "#01109FKeA hopes to be well-\x01",
            "matched with Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PHa ha, right.\x01",
            "I'd be happy too if that were the case.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00000F#6P...Uhmm, then, please\x01",
            "make your reading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PUh uh, all right.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
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
        "KeA",
        "#01110F#12P(Wow, so beautiful...)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man and a\x01",
            "girl who brings light in her smile...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHer existence gives you all courage,\x01",
            "your bond has a firm will,\x01",
            ""to protect her"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAs long as you all protect her,\x01",
            "your bond will not come untied.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P...This is what I am able to see.\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    NpcTalk(
        0x15,
        "KeA",
        (
            "#01106F#12P...Maybe KeA is\x01",
            "a bit disappointed.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00005F#6PEh, why is that?\x01",
            "Wasn't that a good result?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "KeA",
        (
            "#01108F#12PHmm...you're right, but it's\x01",
            "a bit different, I'd say.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#5P...Uh uh, young miss.\x01",
            "This divination is not absolute.\x01",
            "You do not need to sigh.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        (
            "#5PAlso, even if now it is a relationship\x01",
            "like that of a chick and its parent bird...\x01",
            "Chicks eventually grow up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThen...their parents notice, you know.\x01",
            "That their children have\x01",
            "become able to fly.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "KeA",
        (
            "#01105F#12P...Is that so?\x01",
            "Yes, it's like that.\x02\x03",
            "#01109FAlright, KeA...\x01",
            "Will become an adult fast!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PHmm, I don't really get it, but...\x01",
            "If you've cheered up, I'm happy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D39")

    label("loc_95D0")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PKeA, why don't you have\x01",
            "her divine you something?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "KeA",
        (
            "#01105F#12PKeA can decide?\x02\x03",
            "#01111FHmm, then...\x02",
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
        "KeA",
        (
            "#01110F#12POh, that's right!\x01",
            "I want KeA and Zeit's\x01",
            "compatibility divined!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x16,
        "#5PZeit...?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00012F#6PE-Eeehm...\x01",
            "It's the...animal that lives\x01",
            "with us at our working place.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        "#5PUh uh, I understand...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAll right, young miss.\x01",
            "Bring here that Zeit.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI will give you my\x01",
            "reading at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6PEeh!?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "KeA",
        (
            "#01110F#12PReally!?\x02\x03",
            "#01109FThen, I'll go and bring him here!!\x02",
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

    def lambda_988E():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_988E)
    WaitChrThread(0x15, 1)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PI-I'm sorry.\x01",
            "Somehow she asked a strange thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PUh uh, it is fine.\x01",
            "Somehow it seems interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P(This woman too is pretty peculiar...)\x02",
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
        "#01200F#12PGrrowl...woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PUh uh, well then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
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
        "KeA",
        "#01110F#12P(Wow, so beautiful...)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PA girl who brings light in her smile and a\x01",
            "proud wolf that watches over its comrades...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PYou can communicate your feelings...\x01",
            "I can see a bond of respect for each other...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PNo matter what will happen in the future,\x01",
            "the wolf will keep strongly watching over you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P...This is what I am able to see.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x2)

    NpcTalk(
        0x15,
        "KeA",
        (
            "#01100F#12PZeit, it seems that we'll be\x01",
            "together in the future too!\x02\x03",
            "#01109FEheheh, are you happy too, Zeit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#01203F#12PGrrowl...woof.\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PHa ha...thank you very much.\x01",
            "Although she made an unreasonable request...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PUh uh, I could do an unusual divination,\x01",
            "so it was a good experience for me too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D39")

    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5P(Also... I could see another\x01",
            "very interesting hint too.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P(I would say that only the Goddess\x01",
            "knows what will happen from now on.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PMiss fortune teller...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PUh uh...it is nothing.\x01",
            "Please come again...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_30_8ED6 end

    def Function_31_9E64(): pass

    label("Function_31_9E64")

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
            "#1KWhat would you like her to tell you?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "About Our Compatibility\x01",      # 0
            "Leave it to Fran\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5B3")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, it is an easy request.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06405F#12POoh, Mr. Lloyd!\x01",
            "You're worried about your\x01",
            "compatibility with me!?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00002F#6PHa ha, well, since it's\x01",
            "a rare chance, I thought\x01",
            "why don't we do it to try...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06409F#12PUh uh, you're right!\x01",
            "Miss fortune teller,\x01",
            "please!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PUh uh, all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
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
        "Fran",
        (
            "#06405F#12P(Waaah...\x01",
            "S-Somehow she's amazing.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man and a girl\x01",
            "who supports him from the shadows...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PBy working together countless times,\x01",
            "you formed a solid trust relationship,\x01",
            "you tied a bond...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#5POh, however...\x01",
            "The girl has someone dear to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PSince those feelings will not change,\x01",
            "it will hardly turn into that kind\x01",
            "of relationship.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P...This is what I am able to see.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06409F#12POoh...it fits to a T!\x01",
            "As expected, as remarkable as I've heard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PUh uh, you are welcome.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PHa ha, somehow I could\x01",
            "picture it in my mind.\x02\x03",
            "#00000FEhm, Fran.\x01",
            "I'll ask this just for reference...\x01",
            "The person dear to you is...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    NpcTalk(
        0x15,
        "Fran",
        "#06409F#12P#4SOf course, it's my big sis!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PUhhm, as I imagined.\x02\x03",
            "#00000FIt's still too early\x01",
            "for that kind of thing\x01",
            "to happen to Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PUh uh, however, in other words...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf you become someone better than her\x01",
            "older sister, will not there be a possibility?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06409F#12PYou're right.\x01",
            "Please do your best, Mr. Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PNo, even if you tell me\x01",
            "to do my best, I...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC95")

    label("loc_A5B3")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PFran, why don't you have\x01",
            "her divine you something?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06405F#12POh, do you allow\x01",
            "me to decide?\x02\x03",
            "#06404FUhhm, let's see...\x02",
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
        "Fran",
        (
            "#06405F#12POh, now that I think about it...!\x02\x03",
            "#06401FMiss fortune teller, could you\x01",
            "find me where Ban Ban is!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PBan Ban...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PWasn't that the stuffed animal\x01",
            "you really treasured, Fran...?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06400F#12PYes, actually, I was thinking to bring\x01",
            "him with me at Michelam, but...\x02\x03",
            "#06406FThe day before, when mother cleaned the\x01",
            "place, it seems it disappeared somewhere\x01",
            "and in the end I couldn't bring it with me!\x02",
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
            "#00006F#6PI-I see...\x02\x03",
            "#00000FEhm, could you please...?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x16,
        "#5PUh uh, it is an easy request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
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
        "Fran",
        (
            "#06405F#12P(Waaah...\x01",
            "S-Somehow it's amazing.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PThe lost stuffed animal...\x01",
            "Could it be a stuffed bear?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06405F#12PE-Exactly!!\x01",
            "You know that!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PUh uh, it is distinctive,\x01",
            "so I figured it out at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PYour stuffed animal, at present...\x01",
            "Is staying in the shadows under your bed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06403F#12PU-Under the bed?\x01",
            "That's odd,\x01",
            "I looked there too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PMaybe, because it is a place you immediately\x01",
            "thought about, you conversely have overlooked it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PIf you look carefully, you will find it for sure.\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Fran",
        "#06409F#12PYes, thank you very much!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        "#00000F#6PHa ha, aren't you glad, Fran?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06406F#12PYes, really!\x01",
            "Without Ban Ban,\x01",
            "I was really sad.\x02\x03",
            "#06409FWhen I'm back tomorrow, I'll look for him at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PUh uh, I am glad I could be of help.\x02",
    )

    CloseMessageWindow()

    label("loc_AC95")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_31_9E64 end

    def Function_32_ACA1(): pass

    label("Function_32_ACA1")

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
            "#1KWhat would you like her to tell you?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "About Our Compatibility\x01",      # 0
            "Leave it to Cecil\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B467")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, it is an easy request.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05900F#12PMy, Lloyd...\x02\x03",
            "#05909FUh uh, even if you ask about\x01",
            "that on purpose, I am sure\x01",
            "our compatibility is perfect.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PHa ha, well, since we're here\x01",
            "let's do that just to try.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00000F#6P...And so,\x01",
            "please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, all right.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
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
            "#05905F#12P(My...\x01",
            "Somehow she is really amazing.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man and a\x01",
            "woman overflowing with a kind spirit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIn the feelings grown since childhood\x01",
            "lies a unique bond...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5P...However, some definite feelings\x01",
            "still resides in the woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PStrong feelings for the person\x01",
            "dear to her who she lost...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P...This is what I am able to see.\x02",
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
            "#05904F#12P...Uh uh, to think she could\x01",
            "guess so perfectly.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00006F#6P...I'm sorry, sister Cecil, to have\x01",
            "asked her to divine such a thing.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05900F#12PMy, you don't have to apologise.\x01",
            "I am honestly glad my compatibility\x01",
            "with you seems to be good...\x02\x03",
            "#05904FAlso, I am glad I could confirm\x01",
            "once again that I didn't forget\x01",
            "Guy. He is still here with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P...No matter what happens,\x01",
            "the feelings for those we love\x01",
            "keep living for all eternity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIt is also because of those,\x01",
            "that you are here now...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05905F#12P...Lady fortune teller, could it be\x01",
            "you lost an important person too...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        "#5P...It seems I said too much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PA mere fortune teller like me\x01",
            "should not have intruded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PNo, they're precious words.\x01",
            "I'll keep them in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PUh uh...you are welcome.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BBB7")

    label("loc_B467")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PSister Cecil, why don't you have\x01",
            "her divine you something?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05905F#12PEh, is it all right for me to decide?\x02\x03",
            "#05904FUh uh, let's see...\x02",
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
            "#05909F#12PThen...I believe I will ask\x01",
            "you to divine me what kind of\x01",
            "bride Lloyd will get in the future.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x101,
        "#00011F#6P#4SHUH.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#6PW-Wait, sister Cecil...?\x01",
            "As you can imagine, it's too embarrassing...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05909F#12PMy, why not?\x01",
            "Your sister wants to know.\x02\x03",
            "#05900FUh uh, please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PUh uh, it is an easy request.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
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
            "#05900F#12P(My...\x01",
            "Somehow she is really amazing.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man and \x01",
            "the woman he will succeed to marry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P............\x01",
            "............\x02",
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
            "#05905F#12PMy...\x01",
            "Is something the matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI am terribly sorry, however...\x01",
            "At this point in time, I can not say anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI have been asked the same thing\x01",
            "many times until now, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PSometimes it happens that I can not narrow down\x01",
            "the subject if there are too many possible women.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PAnd your case is truly like that.\x02",
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
            "#05909F#12PUhhm...is that so?\x01",
            "That was really out of my calculations too.\x02\x03",
            "#05908FLloyd is my vaunted younger brother,\x01",
            "I thought he cared about girls, however...\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P(S-Somehow I feel like\x01",
            "she's talking about me as\x01",
            "having no morals at all...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05903F#12P...Uhhm, Lloyd?\x01",
            "Your sister has become\x01",
            "a little worried, so...\x02\x03",
            "#05901FDon't end up making\x01",
            "girls sad in the\x01",
            "future, all right?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        "#00012F#6PI-I won't!\x02",
    )

    CloseMessageWindow()

    label("loc_BBB7")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_32_ACA1 end

    def Function_33_BBC3(): pass

    label("Function_33_BBC3")

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
            "#1KWhat would you like her to tell you?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "About Our Compatibility\x01",      # 0
            "Leave it to Ilya\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C226")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, it is an easy request.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6P...Wait, I decided\x01",
            "on my own, but\x01",
            "was it all right?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01709F#12PAhaha, isn't it interesting?\x01",
            "Let's have her do this☆\x02\x03",
            "#01704FUh uh, I'm sorry for Cecil, but if \x01",
            "a nice result comes out, I guess I'll\x01",
            "take the younger brother for myself.\x02",
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
            "#00012F#6P...N-Now, in any case,\x01",
            "it's just to try...\x02\x03",
            "#00000FThen, please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, all right.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
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
        "Ilya",
        "#01705F#12P(Eeh...she's serious.)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man and the dancing\x01",
            "princess who burns with passion on stage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHer earnest feelings towards what she aims for,\x01",
            "attract and charm other people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThere is a great probability that it can\x01",
            "turn into a much deeper relationship if he, \x01",
            "who supports her, does it wholeheartedly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHowever...\x01",
            "It is the stage what is precious to her, after all.\x01",
            "It is hard it will turn in something more than that.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P...This is what I am able to see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PHa ha, in the end, for Miss\x01",
            "Ilya the stage is number one.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01700F#12PUh uh, it would seem so.\x02\x03",
            "#01709FEven so, miss fortune teller.\x01",
            "Frankly, I didn't think you could\x01",
            "show me such a reading.\x02\x03",
            "#01700FI think it's not a skill\x01",
            "you master in a day...\x01",
            "It means you've trained somewhere?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jump("loc_CAD2")

    label("loc_C226")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PMiss Ilya, don't you have something\x01",
            "you'd like to have divined?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01705F#12POh, you mean I can decide?\x02\x03",
            "#01703FUhmm, let's see...\x02",
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
        "Ilya",
        (
            "#01709F#12PThen, will Rixia and Sully\x01",
            "surpass me in the future?\x01",
            "...What about something like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PThose two...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01704F#12PWell, frankly, maybe this\x01",
            "shouldn't be something\x01",
            "to divine...\x02\x03",
            "#01702FIt's a way to confirm once again\x01",
            "that my eyes don't fail me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PYour disciples' future...\x01",
            "Do you want me to read that?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01700F#12PYes, I guess so.\x01",
            "Can you?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PUh uh, it is an easy request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
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
        "Ilya",
        "#01705F#12P(Eeh...she's serious.)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PTwo young dancers discovered by the dancing\x01",
            "princess who burns with passion on stage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThey have bottomless talent in them,\x01",
            "but it seems that each one of them\x01",
            "has her own worries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHow to overcome those...\x01",
            "There lies the key to their future.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P...This is what I am able to see.\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    NpcTalk(
        0x15,
        "Ilya",
        "#01703F#12PRixia and Sully's worries, hm...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PMiss Ilya, do you have any idea?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01703F#12PI had noticed that those\x01",
            "girls were both worried\x01",
            "about something, but...\x02\x03",
            "#01700FFrankly, I haven't asked\x01",
            "in detail what those are.\x02\x03",
            "#01704F...Still, everyone has got worries, \x01",
            "to a greater or lesser extent.\x02\x03",
            "It's up to them if they can overcome those...\x01",
            "It's not up to me to butt in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PHa ha, you're strict, or should I\x01",
            "say... That, in a certain sense,\x01",
            "I was expecting this from you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01700F#12PUh uh, well, I believe that\x01",
            "those girls will overcome\x01",
            "their worries.\x02\x03",
            "#01703FI'm sure that when they\x01",
            "do that, my greatest\x01",
            "rivals will be born.\x02\x03",
            "#01709FUhh, somehow my\x01",
            "heart is racing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PYour positiveness...\x01",
            "I would say it is some type of talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PUh uh, I feel a little envious.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01702F#12PUh uh, you're welcome.\x02\x03",
            "#01709FEven so, miss fortune teller.\x01",
            "Frankly, I didn't think you could\x01",
            "show me such a reading.\x02\x03",
            "#01700FI think it's not a skill\x01",
            "you master in a day...\x01",
            "It means you've trained somewhere?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    label("loc_CAD2")


    ChrTalk(
        0x16,
        (
            "#5P...In the past, I joined a certain traveling\x01",
            "troupe and performed many kind of arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI can do this by applying those...\x01",
            "And I will leave it at that.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01705F#12PA traveling troupe...\x01",
            "In other words, a circus?\x02\x03",
            "#01709FUhhm, I'd like\x01",
            "to have seen you\x01",
            "performing once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PHa ha, so do I.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P...Uh uh, you are welcome.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_33_BBC3 end

    def Function_34_CC43(): pass

    label("Function_34_CC43")

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
            "#1KWhat would you like her to tell you?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "About Our Compatibility\x01",      # 0
            "Leave it to Rixia\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4C8")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, it is an easy request.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Rixia",
        "#01805F#12PMr. L-Lloyd...?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PHa ha. I never come to places\x01",
            "like this, so I wanted to try it.\x02\x03",
            "#00000FIf it's troublesome for you, we can stop...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Rixia",
        (
            "#01804F#12P...Uh uh, no.\x02\x03",
            "#01802FYou're right. Since we're here,\x01",
            "this could be interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PUh uh, well then...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
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
        "Rixia",
        "#01801F#12P(...This is...)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PThe young man whose eyes look straight ahead,\x01",
            "and the girl whose eyes are tinged with sorrow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PTrust between you has been blossoming\x01",
            "ever since a certain incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf that emotion grows, it\x01",
            "is quite possible you will\x01",
            "deepen your relationship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHowever... For that to happen,\x01",
            "the darkness afflicting the\x01",
            "girl's heart must be removed...\x02",
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
        "#5P...This is what I am able to see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PA darkness afflicting Rixia's heart?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PWell... I myself do not know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThose are the only hints this\x01",
            "crystal ball is giving me, you see.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Rixia",
        (
            "#01802F#12P...Umm, I think it's\x01",
            "probably my concern over\x01",
            "the renewal performance.\x02\x03",
            "#01809FWhether I can dance properly with\x01",
            "Sully during her big moment...\x01",
            "I've been worried about that lately.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6POh, so that's it.\x02\x03",
            "#00003FBut you've been practicing\x01",
            "so hard for all this time...\x01",
            "I think you'll be just fine.\x02\x03",
            "#00009FI was moved by your performance before... \x01",
            "I don't think there's any need to worry.\x01\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Rixia",
        "#01805F#12P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P...Uh uh, you're good.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        (
            "#5PFor my advice to be immediately put to\x01",
            "use is all a fortune teller can ask for.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PHuh...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#6PT-That's not it, Rixia!\x02\x03",
            "That was never\x01",
            "my intention...!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Rixia",
        (
            "#01809F#12PUh uh, I know.\x02\x03",
            "#01802FThank you very much, Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBEE")

    label("loc_D4C8")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PRixia, why don't you have\x01",
            "her divine you something?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Rixia",
        (
            "#01805F#12PEhm, is it all right\x01",
            "for me to decide?\x02\x03",
            "#01803FL-Let's see...\x02",
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
        "Rixia",
        (
            "#01803F#12PAbout Miss Shirley who we met some time\x01",
            "ago during the kitty searching case...\x02\x03",
            "#01801FCould you please divine if I am\x01",
            "fated to meet again with her?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PRixia...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, if it is only that, it is an easy request.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
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
        "Rixia",
        "#01801F#12P(...This is...)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        "#5PYou and the girl named Shirley...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI get a hint that you will\x01",
            "meet again in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAlthough I do not know when that\x01",
            "will be and in which situation...\x01",
            "But that time will come for sure.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P...This is what I am able to see.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Rixia",
        (
            "#01802F#12P...I see.\x01",
            "Thank you very much.\x02\x03",
            "#01803F("Bloody Shirley"....\x01",
            "As I feared, I have to be on guard.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PEeh, that's somehow unexpected.\x02\x03",
            "She got involved only a little\x01",
            "during the time of Mary's case...\x01",
            "Were you so worried about her?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Rixia",
        (
            "#01802F#12PAh, no...\x01",
            "It's that it didn't come to my mind\x01",
            "anything else I wanted her to divine...\x02\x03",
            "#01804FAlso, she was a very lovely kid,\x01",
            "I'd like to talk to her if we had the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PU-Uhm...\x01",
            "She's an extremely dangerous kid.\x02\x03",
            "#00006FThinking about Elie's case, she's\x01",
            "dangerous even in a different sense...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Rixia",
        "#01805F#12P...Miss Elie's case?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PA-Ah, no,\x01",
            "it's nothing.\x02\x03",
            "#00003F(I-I just imagined some\x01",
            "amazing scene...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P...Uh uh, young miss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf you want, would you\x01",
            "like me to divine what\x01",
            "he was thinking about?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#00012F#6PP-Please cut me some slack!\x02",
    )

    CloseMessageWindow()

    label("loc_DBEE")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_34_CC43 end

    def Function_35_DBFA(): pass

    label("Function_35_DBFA")

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
            "#1KWhat would you like her to tell you?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "About Our Compatibility\x01",      # 0
            "Leave it to Sully\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E383")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, it is an easy request.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Sully",
        (
            "#14011F#12PH-Hey...\x01",
            "What the heck are you thinking!?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00005F#6PHuh...\x01",
            "I-Is that a thing to be so flustered about?\x02\x03",
            "#00009FIt's so rare to be alone with you,\x01",
            "so I thought to divine that to deepen\x01",
            "our friendship in this occasion.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Sully",
        (
            "#14006F#12P(...Is it normal to tell such stuff\x01",
            "straight to someone's face!?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PUh uh, what should I do?\x01",
            "I am fine with anything.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Sully",
        (
            "#14000F#12P...Oh, jeez, I'm ok with that.\x01",
            "Divine it as you please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, then......\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
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
        "Sully",
        "#14005F#12P(......W-What the......?)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man and\x01",
            "a girl with shining possibilities...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E074")

    ChrTalk(
        0x16,
        (
            "#5PYour encounter was really bad,\x01",
            "but it seems you have noticed \x01",
            "his kindness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0B8")

    label("loc_E074")


    ChrTalk(
        0x16,
        (
            "#5PYou seem to have noticed the\x01",
            "kindness overflowing from him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E0B8")


    ChrTalk(
        0x16,
        (
            "#5PWith the passing of time, if you awaken \x01",
            "a meek heart, you could even become as\x01",
            "close as older brother and younger sister.\x02",
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
        "#5P...This is what I am able to see.\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Sully",
        (
            "#14011F#12PW-W-W-W-W-Wh...\x01",
            "What's with that reading!?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PHa ha, indeed.\x01",
            "It's a little embarrassing.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Sully",
        (
            "#14006F#12P"A little embarrassing"\x01",
            "doesn't even count for it!!\x02\x03",
            "#14012FW-Why should I become close to someone\x01",
            "like you as if you were my older brother...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PUh uh...it looks like you get\x01",
            "along quite well even now.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Sully",
        "#14011F#12PW-We don't!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6P(Ha ha, she isn't very honest.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_EC12")

    label("loc_E383")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PSully, why don't you have\x01",
            "her divine you something?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Sully",
        (
            "#14005F#12PEh, can I decide?\x02\x03",
            "#14003FUhmm...\x02",
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
        "Sully",
        (
            "#14003F#12PThen, I'll ask you...\x02\x03",
            "#14000FWill I be able to properly do\x01",
            "my role in the Arc-en-ciel...?\x01",
            "Can you read that?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PSully...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Sully",
        (
            "#14008F#12P...You know...\x01",
            "If a good result were to come now...\x02\x03",
            "#14008FI won't ever have to go\x01",
            "back to those slums, no?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P...It is fine, I will divine that for you.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
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
        "Sully",
        "#14005F#12P(......W-What the......?)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5P...It seems that the road\x01",
            "you are walking on actually\x01",
            "branches in many directions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PCan you keep chasing your dreams\x01",
            "like now or will you end up returning\x01",
            "frustrated to the place you are from...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PYour fate about that\x01",
            "is not set yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAt this point in time, I can not\x01",
            "say it will absolutely be fine.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        "#5P...This is what I was able to see.\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    NpcTalk(
        0x15,
        "Sully",
        (
            "#14003F#12P...I see...\x02\x03",
            "#14008FIf you had told me I'd have\x01",
            "made it for sure, I would've\x01",
            "been able to to feel a little at ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PSully...\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5P...An acquaintance of mine\x01",
            "was also a kid from the slums.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Sully",
        "#14005F#12PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThe moment we met,\x01",
            "that kid's facial expression\x01",
            "was completely desperate, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PWe lived together for a long time and\x01",
            "she became a bright and strong kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThen, that kid met a splendid leader\x01",
            "and now works as a top class Bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PWhat made that girl grow was...\x01",
            "Without a doubt, the encounter with a person.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Sully",
        "#14005F#12PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIn the hint I got before, you\x01",
            "have already met someone\x01",
            "who you can respect, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThen, the rest is up to you...\x01",
            "I think that.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Sully",
        (
            "#14000F#12P...Up to me...huh?\x02\x03",
            "#14003F...Right.\x01",
            "I don't know if I can be as\x01",
            "strong as that Bracer, but...\x02\x03",
            "#14002FAt any rate, I'll do my best now.\x01",
            "...Thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PUh uh...you are welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6P(Ha ha...I'm really glad I invited her.)\x02",
    )

    CloseMessageWindow()

    label("loc_EC12")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_35_DBFA end

    def Function_36_EC1E(): pass

    label("Function_36_EC1E")

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
        "#00000FAh, found you!\x02",
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
            "Eek! You found me☆\x07\x00\x02",
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
            "Mishishi, you sure\x01",
            "are lucky, mister.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "To think you found my\x01",
            "hiding place twice in a row. \x01",
            "That's pretty good!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FI-Is it...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, that was\x01",
            "just a little test.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "You won't be that lucky so\x01",
            "many times in a row!☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EE7B():

        label("loc_EE7B")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_EE7B")

    QueueWorkItem2(0x101, 1, lambda_EE7B)

    def lambda_EE8D():

        label("loc_EE8D")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_EE8D")

    QueueWorkItem2(0xEF, 1, lambda_EE8D)
    SetChrFlags(0x18, 0x1000)
    OP_95(0x18, -3310, 0, 340, 5000, 0x0)
    OP_95(0x18, -240, 0, -2920, 5000, 0x0)

    def lambda_EECC():
        OP_95(0xFE, -80, 0, -8710, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_EECC)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_EFB7")

    ChrTalk(
        0x102,
        (
            "#00105F...She's gone, eh?\x02\x03",
            "#00104FShe was easier to find\x01",
            "than I thought, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F36B")

    label("loc_EFB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_F014")

    ChrTalk(
        0x103,
        (
            "#00205FAnd...she's gone.\x02\x03",
            "#00204FShe was easier to find\x01",
            "than I thought...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F36B")

    label("loc_F014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_F06D")

    ChrTalk(
        0x104,
        (
            "#00305F...Gone, huh?\x02\x03",
            "#00304FShe was easier to find\x01",
            "than I thought...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F36B")

    label("loc_F06D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_F0D3")

    ChrTalk(
        0x109,
        (
            "#10105F...She's gone, eh?\x02\x03",
            "#10104FShe was easier to find\x01",
            "than I thought, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F36B")

    label("loc_F0D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_F13D")

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, there she goes.\x02\x03",
            "#10302FShe was easier to find\x01",
            "than I thought, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F36B")

    label("loc_F13D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_F18A")

    ChrTalk(
        0x153,
        (
            "#01105FShe's goneー\x02\x03",
            "#01102FSomehow she was easy to find.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F36B")

    label("loc_F18A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_F1EE")

    ChrTalk(
        0x156,
        (
            "#06405F...She's gone, eh?\x02\x03",
            "#06404FShe was easier to find\x01",
            "than I thought, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F36B")

    label("loc_F1EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_F24E")

    ChrTalk(
        0x14C,
        (
            "#05905FShe is gone.\x02\x03",
            "#05904FShe was easier to find\x01",
            "than I thought, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F36B")

    label("loc_F24E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_F2B3")

    ChrTalk(
        0x134,
        (
            "#01705FSeems she's gone.\x02\x03",
            "#01706FShe was easier to find\x01",
            "than I thought, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F36B")

    label("loc_F2B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_F319")

    ChrTalk(
        0x135,
        (
            "#01805F...She's gone, eh?\x02\x03",
            "#01803FShe was easier to find\x01",
            "than I thought, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F36B")

    label("loc_F319")


    ChrTalk(
        0x166,
        (
            "#14005F...Gone, eh?\x02\x03",
            "#14006FShe was easier to find\x01",
            "than I thought, though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F36B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_F40C")

    ChrTalk(
        0x101,
        (
            "#00003FY-Yeah. Just because \x01",
            "she loves hide and seek,\x01",
            "maybe she's not good at it...\x02\x03",
            "#00000FAnyway, let's keep up\x01",
            "this pace and look for her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F49F")

    label("loc_F40C")


    ChrTalk(
        0x101,
        (
            "#00003FY-Yeah. Just because \x01",
            "she loves hide and seek,\x01",
            "maybe she's not good at it...\x02\x03",
            "#00000FAnyway, let's keep up\x01",
            "this pace and look for her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F49F")

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

    # Function_36_EC1E end

    def Function_37_F4D4(): pass

    label("Function_37_F4D4")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　 ～Fortune-telling House～ 　　\x01",
            "We predict your fortune concerning\x01",
            "love, finance and other subjects.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_37_F4D4 end

    def Function_38_F55C(): pass

    label("Function_38_F55C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F69C")
    EventBegin(0x1)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xF, 0x0, 0)

    ChrTalk(
        0xF,
        "Welcome to the "Fortune-telling House"!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Here you can have divined many things\x01",
            "from a remarkable fortune teller!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(I'm playing hide and seek wih Miichie...\x01",
            "I'll refrain from having a good time with\x01",
            "the attractions for now.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -70, 0, 4080, 180)
    OP_4C(0xF, 0xFF)
    OP_93(0xF, 0xB4, 0x0)
    EventEnd(0x4)
    Jump("loc_F69F")

    label("loc_F69C")

    Call(0, 18)

    label("loc_F69F")

    Return()

    # Function_38_F55C end

    SaveToFile()

Try(main)
